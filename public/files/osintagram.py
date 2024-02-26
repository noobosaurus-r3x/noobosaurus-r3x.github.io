import argparse
import json
import requests
import phonenumbers
import pycountry
from phonenumbers.phonenumberutil import region_code_for_country_code
from tabulate import tabulate
from termcolor import colored
from tqdm import tqdm

API_HEADERS = {
    'User-Agent': 'Instagram 64.0.0.14.96',
    'Accept-Language': 'en-US',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-IG-App-ID': '937027530717640',
    'Accept-Encoding': 'gzip, deflate'
}

API_URL = 'https://i.instagram.com/api/v1'


class InstagramAPI:
    def __init__(self, session_id):
        self.session_id = session_id
        self.session = requests.Session()
        self.session.headers.update(API_HEADERS)

    def _make_request(self, url):
        try:
            cookies = {'sessionid': self.session_id}
            response = self.session.get(url, cookies=cookies)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise

    def get_user_id(self, username):
        try:
            response = self._make_request(f'https://www.instagram.com/{username}/?__a=1&__d=dis')
            user_id = response["logging_page_id"].strip("profilePage_")
            return user_id, None
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 404:
                return None, 'User not found'
            else:
                return None, 'Rate limit'
        except (json.JSONDecodeError, KeyError):
            return None, 'Error decoding response'

    def get_user_info(self, user_id):
        response = self._make_request(f'{API_URL}/users/{user_id}/info/')
        user_info = response.get('user', {})
        user_info['userID'] = user_id

        # Retrieve additional user information
        profile_pic_url = user_info['hd_profile_pic_url_info']['url']
        website = user_info.get('website', 'N/A')
        email = user_info.get('public_email')

        # Retrieve recent posts
        recent_posts = []
        response = self._make_request(f'{API_URL}/feed/user/{user_id}/')
        posts_data = response.get('items', [])
        for post in posts_data:
            post_url = f"https://www.instagram.com/p/{post['code']}"
            recent_posts.append({'url': post_url, 'caption': post.get('caption', '')})

        # Add additional user information to the user_info dictionary
        user_info['profile_picture'] = profile_pic_url
        user_info['website'] = website
        user_info['recent_posts'] = recent_posts
        user_info['email'] = email

        return user_info

    def get_followers(self, user_id):
        followers = []
        next_max_id = ''
        total_followers = None

        pbar = tqdm(desc='Fetching followers', unit=' followers')

        while True:
            response = self._make_request(f'{API_URL}/friendships/{user_id}/followers/?max_id={next_max_id}')
            users = response.get('users', [])
            followers.extend(users)
            next_max_id = response.get('next_max_id', '')

            if total_followers is None:
                total_followers = response.get('count', len(users))
                pbar.total = total_followers

            pbar.update(len(users))

            if not next_max_id:
                break

        pbar.close()

        return followers

    def get_following(self, user_id):
        following = []
        next_max_id = ''
        total_following = None

        pbar = tqdm(desc='Fetching following', unit=' following')

        while True:
            response = self._make_request(f'{API_URL}/friendships/{user_id}/following/?max_id={next_max_id}')
            users = response.get('users', [])
            following.extend(users)
            next_max_id = response.get('next_max_id', '')

            if total_following is None:
                total_following = response.get('count', len(users))
                pbar.total = total_following

            pbar.update(len(users))

            if not next_max_id:
                break

        pbar.close()

        return following


def format_user_info(user_info):
    output = []
    output.append(colored("Informations about     : ", 'blue') + colored(user_info["username"], 'yellow'))
    output.append(colored("userID                 : ", 'blue') + colored(user_info["userID"], 'yellow'))
    output.append(colored("Full Name              : ", 'blue') + colored(user_info["full_name"], 'yellow'))
    output.append(colored("Verified               : ", 'blue') + colored(str(user_info['is_verified']), 'yellow') +
                  " | " + colored("Is business Account : ", 'blue') + colored(str(user_info["is_business"]), 'yellow'))
    output.append(colored("Is private Account     : ", 'blue') + colored(str(user_info["is_private"]), 'yellow'))
    output.append(colored("Follower               : ", 'blue') + colored(str(user_info["follower_count"]), 'yellow') +
                  " | " + colored("Following : ", 'blue') + colored(str(user_info["following_count"]), 'yellow'))
    output.append(colored("Number of posts        : ", 'blue') + colored(str(user_info["media_count"]), 'yellow'))
    output.append(colored("Number of tag in posts : ", 'blue') + colored(str(user_info["following_tag_count"]), 'yellow'))

    if user_info["external_url"]:
        output.append(colored("External url           : ", 'blue') + colored(user_info["external_url"], 'yellow'))

    output.append(colored("IGTV posts             : ", 'blue') + colored(str(user_info["total_igtv_videos"]), 'yellow'))
    output.append(colored("Biography              : ", 'blue') +
                  colored(("\n" + " " * 25).join(user_info["biography"].split("\n")), 'yellow'))

    if "email" in user_info and user_info["email"]:
        output.append(colored("Email                   : ", 'blue') + colored(user_info["email"], 'yellow'))

    if "public_phone_number" in user_info and str(user_info["public_phone_number"]):
        phone_number = "+" + str(user_info["public_phone_country_code"]) + " " + str(
            user_info["public_phone_number"])

        try:
            parsed_number = phonenumbers.parse(phone_number)
            country_code = region_code_for_country_code(parsed_number.country_code)
            country = pycountry.countries.get(alpha_2=country_code)
            phone_number = f"{phone_number} ({country.name})"
        except phonenumbers.phonenumberutil.NumberParseException:
            pass

        output.append(colored("Public Phone number    : ", 'blue') + colored(phone_number, 'yellow'))

    output.append(colored("Profile Picture        : ", 'blue') + colored(user_info['profile_picture'], 'yellow'))
    output.append(colored("Website                : ", 'blue') + colored(user_info['website'], 'yellow'))

    if user_info['recent_posts']:
        output.append(colored("Recent Posts:", 'blue'))
        for post in user_info['recent_posts']:
            output.append(colored("URL: ", 'blue') + colored(post['url'], 'yellow'))
            caption = post.get('caption', 'N/A')
            if isinstance(caption, str):
                output.append(colored("Caption: ", 'blue') + colored(caption, 'yellow'))
            else:
                output.append(colored("Caption: ", 'blue') + colored("N/A", 'yellow'))
            output.append("")

    return "\n".join(output)


def get_user_followers(api, user_id):
    print("Retrieving followers...")
    followers = api.get_followers(user_id)
    follower_table = [[follower["username"], follower.get("full_name", "")] for follower in followers]
    return tabulate(follower_table, headers=[colored("Username", 'yellow'), colored("Full Name", 'yellow')],
                    tablefmt="presto")


def get_user_following(api, user_id):
    print("Retrieving following...")
    following = api.get_following(user_id)
    following_table = [[account["username"], account.get("full_name", "")] for account in following]
    return tabulate(following_table, headers=[colored("Username", 'yellow'), colored("Full Name", 'yellow')],
                    tablefmt="presto")


def save_output(output, file_path):
    with open(file_path, 'w') as file:
        file.write(output)
    print("Output saved to:", file_path)


def main():
    parser = argparse.ArgumentParser(description="Instagram User Information Retrieval")
    parser.add_argument('-s', '--sessionid', help="Instagram session ID")
    parser.add_argument('-u', '--username', help="Username to retrieve information for")
    parser.add_argument('-o', '--output', help="Output file path")
    parser.add_argument('-i', '--interactive', action='store_true', help="Interactive mode")
    parser.add_argument('-f', '--followers', action='store_true', help="Retrieve and display followers")
    parser.add_argument('-g', '--following', action='store_true', help="Retrieve and display following")
    args = parser.parse_args()

    if args.interactive and (args.sessionid or args.username or args.followers or args.following or args.output):
        parser.error("Interactive mode (-i) cannot be used with other command-line arguments.")

    if args.interactive:
        session_id = input("Enter your Instagram session ID: ")
        username = input("Enter the username to retrieve information for: ")
        followers = input("Retrieve followers? (y/n): ").lower() == "y"
        following = input("Retrieve following? (y/n): ").lower() == "y"
        save_output_option = input("Save output to a file? (y/n): ").lower() == "y"
        output_file = input("Enter the output file path: ") if save_output_option else None
    else:
        session_id = args.sessionid
        username = args.username
        followers = args.followers
        following = args.following
        output_file = args.output

    api = InstagramAPI(session_id)

    user_id, error = api.get_user_id(username)
    if error:
        print(f"Error: {error}")
        return

    user_info = api.get_user_info(user_id)
    output = format_user_info(user_info)

    if followers:
        follower_output = get_user_followers(api, user_id)
        output += "\n" + colored("Followers:", 'blue') + "\n" + follower_output

    if following:
        following_output = get_user_following(api, user_id)
        output += "\n" + colored("Following:", 'blue') + "\n" + following_output

    if output_file:
        save_output(output, output_file)
    else:
        print(output)


if __name__ == '__main__':
    main()
