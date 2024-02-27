+++
author = "Noobosaurus R3x"
title = "Lockbit, la traduction de son message"
date = "2024-02-27T01:15:00Z"
description = "Traduction du message de Lockbit"
type = [
    "posts"
]
categories = [
    "articles"
]
tags = [
    "articles"
]
+++


Ce qui s'est passé. 

Le 19 février 2024, des tests d’intrusion ont eu lieu sur deux de mes serveurs. À 06:39 UTC, j'ai trouvé une erreur 502 Bad Gateway sur le site, j'ai redémarré nginx - rien n'a changé, j'ai redémarré mysql - rien n'a changé, j'ai redémarré PHP - le site a fonctionné. Je n'y ai pas prêté beaucoup d'attention, car après avoir nagé dans l'argent pendant 5 ans, je suis devenu très paresseux et j'ai continué à me promener sur un yacht avec des filles à nichons. À 20 h 47, j'ai constaté que le site affichait une nouvelle erreur 404 Not Found nginx, j'ai essayé d'entrer sur le serveur via SSH et je n'ai pas pu, le mot de passe ne convenait pas, et il s'est avéré plus tard que toutes les informations contenues sur les disques avaient été effacées. 

En raison de ma négligence personnelle et de mon irresponsabilité, je me suis relâché et n'ai pas mis à jour PHP à temps. Les serveurs étaient équipés de la version 8.1.2 de PHP, qui a été testée avec succès, très probablement par la CVE https://www.cvedetails.com/cve/CVE-2023-3824/, ce qui a permis d'accéder aux deux serveurs principaux sur lesquels cette version de PHP était installée. Je me rends compte qu'il ne s'agit peut-être pas de cette CVE, mais de quelque chose d'autre comme une 0day pour PHP, mais je ne peux pas en être sûr à 100 %, car la version installée sur mes serveurs présentait déjà une vulnérabilité connue, et c'est donc très probablement de cette manière que les serveurs d'administration et de chat des victimes, ainsi que le serveur de blog, ont été accédés. Les nouveaux serveurs utilisent désormais la dernière version de PHP 8.3.3. Si quelqu'un connaît une CVE pour cette version, soyez le premier à me le faire savoir et vous serez récompensé. 

Le problème ne concerne pas que moi. Tous ceux qui ont utilisé une version vulnérable de PHP doivent garder à l'esprit que leur serveur a pu être compromis, je suis sûr que de nombreux concurrents ont pu être piratés de la même manière, mais qu'ils n'ont même pas réalisé comment cela s'est produit. Je suis sûr que les forums que je connais sont également piratés de la même manière via PHP, il y a de bonnes raisons d'en être sûr, non seulement à cause de mon piratage mais aussi à cause d'informations provenant de dénonciateurs. J'ai remarqué le problème de PHP par accident, et je suis le seul à disposer d'une infrastructure décentralisée avec différents serveurs, ce qui m'a permis de comprendre rapidement comment l'attaque s'est produite. Si je n'avais pas eu de serveurs de secours sans PHP, je n'aurais probablement pas compris comment le piratage s'est produit.

Le FBI a décidé de pirater maintenant pour une seule raison, parce qu'il ne voulait pas divulguer des informations sur https://fultoncountyga.gov/. Les documents volés contiennent beaucoup de choses intéressantes et des affaires judiciaires de Donald Trump qui pourraient avoir une incidence sur les prochaines élections américaines. Personnellement je voterai pour Trump car la situation à la frontière avec le Mexique est une sorte de cauchemar, Biden devrait prendre sa retraite, c'est une marionnette. S'il n'y avait pas eu l'attaque du FBI, les documents auraient été publiés le jour même, parce que les négociations ont été bloquées, juste après que le partenaire ait posté le communiqué de presse sur le blog, le FBI n'aimait vraiment pas que le public découvre les vraies raisons de l'échec de tous les systèmes de cette ville. S'il n'y avait pas eu la situation des élections, le FBI aurait continué à s'asseoir sur mon serveur en attendant des pistes pour nous arrêter, moi et mes associés, mais tout ce que vous avez à faire pour ne pas vous faire prendre, c'est du blanchiment de crypto-monnaie de qualité. Le FBI peut s'asseoir sur vos ressources et également collecter des informations utiles pour le FBI, mais ne montrez pas au monde entier que vous avez été piraté, car vous ne causez aucun dommage critique, vous n'apportez que des avantages. Quelles conclusions peut-on tirer de cette situation ? Très simple, que je dois attaquer le secteur .gov de plus en plus souvent, c'est après de telles attaques que le FBI sera obligé de me montrer mes faiblesses et mes vulnérabilités et de me rendre plus fort. En attaquant le secteur .gov, vous pouvez savoir exactement si le FBI a la capacité de nous attaquer ou non. 

Même si vous avez mis à jour votre version de PHP après avoir lu ces informations, cela ne sera pas suffisant, car vous devez changer l'hébergeur, le serveur, tous les mots de passe possibles, les mots de passe des utilisateurs dans la base de données, auditer le code source et tout migrer, il n'y a aucune garantie que vous n'ayez pas été durci sur le serveur. Il n'y a aucune garantie que le FBI n'ait pas de 0day pour vos serveurs dont ils ont déjà appris assez d'informations pour les pirater à nouveau, donc seul un changement complet de tout ce qui ne peut être que remplacé aidera. 

Tous les autres serveurs avec des blogs de sauvegarde qui n'ont pas installé PHP ne sont pas affectés et continueront à fournir des données volées aux entreprises attaquées. 

En piratant les serveurs, le FBI a obtenu une base de données, des sources de web pannels, des morceaux de lockers qui ne sont pas des sources comme ils le prétendent et une petite partie des outils de déchiffrement non protégés, ils prétendent 1000 outils de déchiffrement, bien qu'il y ait près de 20000 outils de déchiffrement sur le serveur, dont la plupart étaient protégés et ne peuvent pas être utilisés par le FBI. Grâce à la base de données, ils ont découvert les surnoms générés des partenaires, qui n'ont rien à voir avec leurs vrais surnoms sur les forums et même les surnoms dans les messageries, les chats non supprimés avec les entreprises attaquées et, en conséquence, les portefeuilles pour l'argent, qui feront l'objet d'une enquête et d'une recherche pour tous ceux qui ne blanchissent pas de crypto, et éventuellement arrêter les personnes impliquées dans le blanchiment et les accuser d'être mes affiliés, bien qu'ils ne le soient pas. Toutes ces informations n'ont aucune valeur car elles sont toutes transmises au FBI et sans piratage du panel, après chaque transaction par les agents d'assurance ou les négociateurs. 

La seule chose qui a de la valeur et qui constitue une menace potentielle est le code source du panel, parce qu'il est probablement possible de le pirater à l'avenir si vous laissez tout le monde accéder au panel, mais maintenant le panel sera divisé en plusieurs serveurs, pour les partenaires vérifiés et pour les personnes aléatoires, jusqu'à une copie du panel pour un affilié sur un serveur séparé, alors qu'avant il y avait un seul panel pour tout le monde. En raison de la séparation du panel et d'une plus grande décentralisation, de l'absence d'essais de décchiffrement en mode automatique, de la protection maximale des outils de déchiffrement pour chaque entreprise, les risques de piratage seront considérablement réduits. Des fuites du code source du panel ont également eu lieu chez des concurrents, cela ne les a pas empêché de continuer leur travail, cela ne m'arrêtera pas non plus. 

Le FBI dit avoir reçu environ 1000 outils de déchiffrement, un beau chiffre, mais il ne semble pas correspondre à la réalité. En effet, ils ont reçu des outils de déchiffrement non protégés, ces versions du casier qui ont été créées sans la case à cocher "protection maximale des outils de déchiffrement" ne pouvaient être reçues par le FBI qu'au cours des 30 derniers jours, on ne sait pas quel jour le FBI a eu accès au serveur, mais nous connaissons exactement la date de la divulgation du CVE et la date à laquelle PHP a généré une erreur, avant le 19 février, les entreprises attaquées payaient régulièrement, même pour des outils de déchiffrement non protégés, il est donc possible que le FBI ne soit resté qu'une journée sur le serveur, il serait bien que le FBI publie tous les outils de déchiffrement, on pourrait alors leur faire confiance et croire qu'ils possèdent vraiment les outils de déchiffrement, sans bluffer et sans vanter leur supériorité, pas la supériorité d'un pentester intelligent avec une CVE public. Notez que la grande majorité des outils de déchiffrement non protégés proviennent d'affiliés qui chiffrent des dédicas (sic) par force brute et envoient des spams sur des ordinateurs individuels en demandant des rançons de 2000 dollars, c'est-à-dire que même si le FBI possède 1000 outils de déchiffrement, ils ne sont pas d'une grande utilité, l'essentiel étant qu'il n'a pas obtenu tous les outils de déchiffrement pour l'ensemble des 5 années d'activité, soit environ 40000. Il s'avère que le FBI n'a pu mettre la main que sur 2,5 % du nombre total de outils de déchiffrement, c'est certes mauvais, mais ce n'est pas fatal. 

- À partir de ce moment important, où le FBI m'a encouragé, je vais cesser d'être paresseux et faire en sorte qu'absolument tous les builds de lockers bénéficient d'une protection maximale, maintenant il n'y aura pas de déchiffrement d'essai automatique, tous les déchiffrements d'essai et l'émission de outils de déchiffrement se feront uniquement en mode manuel. Ainsi, lors d'une éventuelle prochaine attaque, le FBI ne pourra pas obtenir un seul outils de déchiffrement gratuitement. 

Il est probable que tout le monde a déjà remarqué à quel point le FBI a magnifiquement modifié le design de son blog. Personne n'a jamais reçu de tels honneurs, d'habitude tout le monde se contente de mettre la fiche habituelle avec les louanges de tous les services spéciaux du monde. Bien qu'en fait, une seule personne sur toute la planète mérite des éloges, celle qui a pentesté mon site et choisi la bonne CVE public, je me demande combien il a été payé, combien était son bonus ? Si c'est moins d'un million de dollars, alors venez travailler pour moi, vous gagnerez probablement plus avec moi. Ou venez simplement me parler à tox 3085B89A0C515D2FB124D645906F5D3DA5CB97CEBEA975959AE4F95302A04E1D709C3C4AE9B7 rappelez-vous que j'ai toujours un programme de bug bounty actif et que je paie pour les bugs trouvés. Le FBI n'apprécie pas vos talents, mais moi si, et je suis prêt à payer généreusement. 

Je me demande pourquoi les blogs alpha, revil, hive n'ont pas été conçus aussi joliment ? Pourquoi leurs deanons n'ont-ils pas été publiés ? Alors que le FBI connaît leur identité ? C'est étrange, non ? Parce qu'avec des méthodes aussi stupides, le FBI essaie de m'intimider et de me faire arrêter de travailler. Le designer du FBI devrait travailler pour moi, vous avez bon goût, j'ai particulièrement aimé le nouveau préchargeur, dans la nouvelle mise à jour je devrais faire quelque chose de similaire, les USA, le Royaume-Uni et l'Europe tournent autour de mon logo, idée brillante, juste là je me suis senti très bien, merci. 

Deux de mes affiliés ont été arrêtés, pour être honnête j'en doute beaucoup, ce sont probablement des gens qui blanchissent des crypto-monnaies, peut-être qu'ils travaillaient pour des mélangeurs et échangeurs avec des drops, c'est pour cela qu'ils ont été arrêtés et considérés comme mes partenaires, il serait intéressant de voir la vidéo de l'arrestation, où à leurs domiciles, Lamborghini et ordinateurs portables avec des preuves de leur implication dans nos activités, mais je pense que nous ne la verrons pas, parce que le FBI a arrêté des gens au hasard pour obtenir un certificat de mérite de la part de la direction, dire regardez il y a des arrestations, nous ne recevons pas d'argent pour rien, nous travaillons honnêtement avec vos impôts et emprisonnons des gens au hasard, alors que les vrais pentesters continuent tranquillement leur travail. Basssterlord n'est pas pris, je connais le vrai nom de Basssterlord, et il est différent du pauvre type que le FBI a attrapé. 

Je ne connais aucun journaliste militaire de Sébastopol, le colonel Cassad, et je n'ai jamais fait de don à qui que ce soit, il serait bon que le FBI montre la transaction afin que je puisse vérifier sur la blockchain d'où ils tirent de telles conclusions et pourquoi ils prétendent que c'est moi qui l'ai fait, je ne fais jamais aucune transaction sans un mixeur bitcoin. 

Si j'ai pu utiliser le même service d'échange de crypto-monnaies que quelqu'un d'Evil Corp, cela ne veut absolument pas dire que j'ai quelque chose à voir avec Evil Corp, encore une fois où sont les transactions ? Comment puis-je savoir qui utilise quel échangeur ? J'utilise différents échangeurs et je ne concentre pas tout mon argent sur un seul échangeur de crypto-monnaie. Blâmons Evil Corp pour les centaines d'autres personnes qui utilisent des échanges accessibles au public. Je n'aime vraiment pas le fait que toutes ces accusations soient faites sans publier les transactions et les portefeuilles, il est donc impossible de vérifier ce qui est vrai. Vous pouvez m'accuser de n'importe quoi sans rien prouver, et il n'y a aucun moyen pour moi de le réfuter, parce qu'il n'y a pas de transactions et de portefeuilles bitcoins. 

Le FBI affirme que mes revenus dépassent les 100 millions de dollars, c'est vrai, je suis très heureux d'avoir supprimé des chats avec des paiements très importants, maintenant je vais supprimer plus souvent et des petits paiements aussi. Ces chiffres montrent que je suis sur la bonne voie, que même si je fais des erreurs, cela ne m'arrête pas et que je corrige mes erreurs et continue à gagner de l'argent. Cela montre qu'aucun piratage du FBI ne peut empêcher une entreprise de prospérer, car ce qui ne me tue pas me rend plus fort. 

Toutes les actions du FBI visent à détruire la réputation de mon programme d'affiliation, ma démoralisation, ils veulent que je parte et que je quitte mon travail, ils veulent me faire peur car ils ne peuvent pas me trouver et m'éliminer, je ne peux pas être arrêté, vous ne pouvez même pas espérer, tant que je serai en vie je continuerai à faire du pentest avec postpaid. 

Je suis très heureux que le FBI m'ait remonté le moral, m'ait donné de l'énergie et m'ait fait oublier les divertissements et les dépenses d'argent, il est très difficile de s'asseoir devant l'ordinateur avec des centaines de millions de dollars, la seule chose qui me motive à travailler, ce sont des concurrents forts et le FBI, il y a un intérêt sportif et un désir de rivalité. Avec des concurrents qui gagneront plus d'argent et attaqueront plus d'entreprises, et avec le FBI, qu'ils puissent m'attraper ou non, et je suis sûr qu'ils ne le pourront pas, vu la façon dont ils travaillent. 

Le FBI a promis de publier mon deanon mais n'a pas tenu sa promesse, ces gens osent mentir sur le fait que je n'ai soi-disant pas supprimé les informations volées aux entreprises après avoir payé la rançon, c'est de la clownerie. Il s'avère que le FBI s'est officiellement reconnu comme menteur et qu'il ment très souvent, comme l'ont déclaré mes avocats familiers Arkady Buch, Dmitry Naskavets et Victor Smilyanets, que je crois maintenant à 100 %. Ils ont fait une tentative stupide pour me discréditer en prétendant que je travaillais pour le FBI, un homme qui chiffre des entreprises américaines tous les jours et gagne des centaines de millions de dollars le fait avec l'approbation du FBI ? C'est comme ça que ça marche ? C'est très astucieux. 

Vous vous demandez pourquoi je travaillerais avec des centaines de millions de dollars ? Et je vous répondrai que je m'ennuie, que j'aime mon travail, qu'il m'apporte la joie de vivre, que l'argent et le luxe n'apportent pas autant de joie que mon travail, que c'est pour cela que je suis prêt à risquer ma vie pour mon travail, que c'est ainsi que la vie devrait être brillante, riche et dangereuse, à mon avis. 

*Quand j'écris le mot FBI, je ne parle pas seulement du FBI, mais aussi de tous ses assistants, qui savent comment arrêter les serveurs des affliés, qui servent de première ligne après avoir volé les données de la société attaquée et qui ne représentent aucune valeur : South West Regional Organized Crime Unit au Royaume-Uni, Metropolitan Police Service au Royaume-Uni, Europol, Gendarmerie-C3N en France, State Criminal Police Office L-K-A et Federal Criminal Police Office en Allemagne, Fedpol et Zurich Cantonal Police en Suisse, National Police Agency au Japon, Australian Federal Police en Australie, Swedish Police Authority en Suède, National Bureau of Investigation en Finlande, Royal Canadian Mounted Police au Canada et National Police aux Pays-Bas. Ne le prenez pas mal, je ne vous ai pas oubliés, vous avez également été très utiles dans cette opération. Mais permettez-moi de vous rappeler que, personnellement, je pense que la seule personne qui mérite un prix et une mention honorable est celle qui a trouvé une CVE PHP public approprié pour mes serveurs, je suppose qu'il s'agit de quelqu'un de Prodaft. 




Une liste de domaines de blogs de sauvegarde que le FBI n'a pas pu atteindre parce que PHP n'est pas installé sur ces serveurs. 

Ces serveurs hébergent non seulement les entreprises que vous pouvez voir sur le domaine principal, mais aussi de nombreuses entreprises qui ont été remises pour téléchargement manuel, c'est-à-dire des liens qui sont secrets et publiés si l'entreprise refuse de payer la rançon, par exemple :
http://lockbit7z2jwcskxpbokpemdxmltipntwlkmidcll2qirbu7ykg46eyd.onion/secret/d8103cc7ba967d32a268d5cb3cff5b29/8x8.com
http://lockbit7z2jwcskxpbokpemdxmltipntwlkmidcll2qirbu7ykg46eyd.onion/secret/7bbed20cee2fef7f16def020b3690b0f/muellersystems.com
http://lockbit7z2jwcskxpbokpemdxmltipntwlkmidcll2qirbu7ykg46eyd.onion/secret/7b20fb8ef3064e45ce4954446cc6e858/boeing.com
http://lockbit7z2jwcskxpbokpemdxmltipntwlkmidcll2qirbu7ykg46eyd.onion/secret/c852ee1bccff6830b7316afb016be962/estes-express.com
http://lockbit7z2jwcskxpbokpemdxmltipntwlkmidcll2qirbu7ykg46eyd.onion/secret/a38cdf047c11d9a8cdcff00da7f62385/cityofclarksville.com
http://lockbit7z2jwcskxpbokpemdxmltipntwlkmidcll2qirbu7ykg46eyd.onion/secret/23f187fabd0681c79f1b0107275bdd27/esser-ps.de
http://lockbit7z2jwcskxpbokpemdxmltipntwlkmidcll2qirbu7ykg46eyd.onion/secret/8c877f8eae9e950552605a44f0485835/heinrichseegers.de
http://lockbit7z2jwcskxpbokpemdxmltipntwlkmidcll2qirbu7ykg46eyd.onion/secret/0fa4f7c543ddc8203f772322a2b0203e/hotelemc2.com
http://lockbit7z2jwcskxpbokpemdxmltipntwlkmidcll2qirbu7ykg46eyd.onion/secret/46216a24a00ccd4cdc6d96c7c82ebd69/roehr-stolberg.de
http://lockbit7z2jwcskxpbokpemdxmltipntwlkmidcll2qirbu7ykg46eyd.onion/secret/ab738d1822d63fa3e81193b75b89fb8b/roth-werkzeugbau.de
http://lockbit7z2jwcskxpbokpemdxmltipntwlkmidcll2qirbu7ykg46eyd.onion/secret/dd20772d156397072e50c5ce8af54994/schuett-grundei.de
http://lockbit7z2jwcskxpbokpemdxmltipntwlkmidcll2qirbu7ykg46eyd.onion/secret/0b8fe87adbd6a829b1af92bbb482f473/starkpower.de
http://lockbit7z2jwcskxpbokpemdxmltipntwlkmidcll2qirbu7ykg46eyd.onion/secret/8d1ff2c9e62ae75972b8371b789c8a69/thewalkerschool.org
http://lockbit7z2jwcskxpbokpemdxmltipntwlkmidcll2qirbu7ykg46eyd.onion/secret/b7f14428465e73416571d7f0ace4e1f8/unitednotions.com
http://lockbit7z2jwcskxpbokpemdxmltipntwlkmidcll2qirbu7ykg46eyd.onion/secret/cad65f46efbec2e5f1ab35d1b1d40b34/wombleco.com
http://lockbit7z2jwcskxpbokpemdxmltipntwlkmidcll2qirbu7ykg46eyd.onion/secret/2a366160a6eeba8ffb0d21d734148e57/gitiusa.com
http://lockbit7z2jwcskxpbokpemdxmltipntwlkmidcll2qirbu7ykg46eyd.onion/secret/70ef5f8ac50d8d7e09ad8c4478cff8e8/Good-Lawyer.com
http://lockbit7z2jwcskxpbokpemdxmltipntwlkmidcll2qirbu7ykg46eyd.onion/secret/12eee65c430a7f2a3a8317acb68b1303/aei.cc
http://lockbit7z2jwcskxpbokpemdxmltipntwlkmidcll2qirbu7ykg46eyd.onion/secret/b946864a63e28e9177d4a5fe7834ed1d/carsonteam.com
http://lockbit7z2mmiz3ryxafn5kapbvbbiywsxwovasfkgf5dqqp5kxlajad.onion/secret/5c60836b0eccdc9845b9c9e278e0033a/dena.de/
Ces entreprises et bien d'autres ont été sauvées, elles seront publiées plus tard dans un nouveau blog.

Miroirs de blog de sauvegarde, n'importe quel domaine peut être substitué aux liens secrets, au cas où un domaine serait surchargé paer des personnes voulant télécharger les données volées :
http://lockbit7z2jwcskxpbokpemdxmltipntwlkmidcll2qirbu7ykg46eyd.onion/
http://lockbit7z2mmiz3ryxafn5kapbvbbiywsxwovasfkgf5dqqp5kxlajad.onion/
http://lockbit7z2og4jlsmdy7dzty3g42eu3gh2sx2b6ywtvhrjtss7li4fyd.onion/
http://lockbit7z355oalq4hiy5p7de64l6rsqutwlvydqje56uvevcc57r6qd.onion/
http://lockbit7z36ynytxwjzuoao46ck7b3753gpedary3qvuizn3iczhe4id.onion/
http://lockbit7z37ntefjdbjextn6tmdkry4j546ejnru5cejeguitiopvhad.onion/
http://lockbit7z3azdoxdpqxzliszutufbc2fldagztdu47xyucp25p4xtqad.onion/
http://lockbit7z3ddvg5vuez2vznt73ljqgwx5tnuqaa2ye7lns742yiv2zyd.onion/
http://lockbit7z3hv7ev5knxbrhsvv2mmu2rddwqizdz4vwfvxt5izrq6zqqd.onion/
http://lockbit7z3ujnkhxwahhjduh5me2updvzxewhhc5qvk2snxezoi5drad.onion/
http://lockbit7z4bsm63m3dagp5xglyacr4z4bwytkvkkwtn6enmuo5fi5iyd.onion/
http://lockbit7z4cgxvictidwfxpuiov4scdw34nxotmbdjyxpkvkg34mykyd.onion/
http://lockbit7z4k5zer5fbqi2vdq5sx2vuggatwyqvoodrkhubxftyrvncid.onion/
http://lockbit7z4ndl6thsct34yd47jrzdkpnfg3acfvpacuccb45pnars2ad.onion/

Nouveaux domaines du blog principal
http://lockbit3753ekiocyo5epmpy6klmejchjtzddoekjlnt6mu3qh4de2id.onion/
http://lockbit3g3ohd3katajf6zaehxz4h4cnhmz5t735zpltywhwpc6oy3id.onion/
http://lockbit3olp7oetlc4tl5zydnoluphh7fvdt5oa6arcp2757r7xkutid.onion/
http://lockbit435xk3ki62yun7z5nhwz6jyjdp2c64j5vge536if2eny3gtid.onion/
http://lockbit4lahhluquhoka3t4spqym2m3dhe66d6lr337glmnlgg2nndad.onion/
http://lockbit6knrauo3qafoksvl742vieqbujxw7rd6ofzdtapjb4rrawqad.onion/
http://lockbit7ouvrsdgtojeoj5hvu6bljqtghitekwpdy3b6y62ixtsu5jqd.onion/

Même après le piratage du FBI, les données volées seront publiées sur le blog, il n'y a aucune chance de détruire les données volées sans paiement. Et après avoir introduit une protection maximale sur chaque build de locker, il n'y aura aucune chance de déchiffrement gratuit même pour 2,5 % des entreprises attaquées.

Les nouveaux affiliés peuvent travailler dans mon programme d'affiliation s'ils ont une réputation sur les forums, peuvent prouver qu'ils sont des pentesters avec post-paiement, ou en faisant un dépôt de 2 bitcoins, l'augmentation du dépôt est due à la preuve et à la belle publicité du FBI, qui est que mes affiliés et moi gagnons ensemble des centaines de millions de dollars, et que aucun FBI avec leurs assistants ne peut me faire peur et m'arrêter, la stabilité du service est garantie par des années de travail continu.

Écrivez à tox 3085B89A0C515D2FB124D645906F5D3DA5CB97CEBEA975959AE4F95302A04E1D709C3C4AE9B7

Pourquoi a-t-il fallu 4 jours pour récupérer ? Parce que je devais modifier le code source pour la dernière version de PHP, car il y avait une incompatibilité.

Cordialement, LockBit.
24 février 2024



