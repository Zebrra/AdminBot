# AdminBot
# Sommaire
- [Présentation](#présentation)

-  [Liste des modules](#liste-des-modules)
	- [Présentation des modules](#présentation-des-modules)
	- [Installation](#installation)
 
- [Liste des fonctions](#liste-des-fonctions)
	- [Fonctions du prefixe](#fonctions-du-prefixe)
		- [show_prefix](#show_prefix)
		- [change_prefix](#change_prefix)
	- [Fonctions help](#fonctions-help)
		- [help](#help)
		- [listing](#listing)
	- [Fonctions admin](#fonctions-admin)
		- [mute](#mute)
		- [unmute](#unmute)
		- [ban](#ban)
		- [unban](#unban)
		- [show_ban](#show_ban)
		- [kick](#kick)
		- [warn](#warn)
		- [show_warn](#show_warn)
		- [purge](#purge)
	- [Fonction infos](#fonctions-infos)
		- [server_info](#server_info)
		- [user_info](#user_info)
	- [Fonction embeds](#fonctions-embeds)
		- [embeds](#embeds)

# Présentation
La bot AdminBot est comme son nom l'indique, un bot d'administration pour un serveur Discord, il gère donc uniquement les fonctions d'administration avec quelques fonctions supplémentaire type utilitaire (comme les informations et le formatage d'embeds) mais qui se joignent parfaitement à de la modération/administration d'un serveur.

À L'exception des fonctions utilitaires, toute les fonctions du bot s'utilise avec des perms d'admin sauf car particulier certaines fonctions nécessite des perms inférieur, comme la gestion des messages ou alors la possibilités de bannir un membre, etc.

Chaque bot sur ce GitHub peuvent être assemblé comme un puzzle et fonctionneront, il suffit simplement d'adapter le fichier ``main.py`` pour acceuillir la création de la base de données, l'import des modules, etc.

# Liste des modules
### Présentation des modules
Les modules à installer sur votre machine d'hébergement sont nécessaire au bon fonctionnement du bot. Hormis les modules natif à Python, le bot à besoin de modules externe, tel que ``discord.py``,  etc.

Voici les modules requis par le bot : 
```python
discord.py>=1.7.3
aiosqlite>=0.17.0
python-dotenv>=0.19.2
aiohttp>=3.8.1
```
### Installation
Pour installer ces modules il suffit à l'aide du terminal se déplacer dans le dossier de configuration
```console
cd /AdminBot/config
```
Et d'utiliser la commande  :
```console
pip install --upgrade -r requirements.txt
```
cette fonction permet à l'aide du fichier ``requirements.txt`` d'installer tout les modules requis d'un seul coup et de les mettre à jour si possible.
# Liste des fonctions

## Fonctions du prefixe
#### show_prefix
> **Utiliser cette fonction, permet de connaître le préfixe du bot, en revanche le préfixe est également affiché dans le statut d'activité du bot.**
> Cette fonction ne prends aucun paramètre et aucune permissions ne sont requise.

#### change_prefix
> **Cette fonction permet la modification du préfixe du bot (pratique si d'autre bot du serveur utilisent le même préfixe).**
> Cette fonction prend donc en paramètre le nouveau préfixe du bot. Et la permission d'administrateur est requise.
```
!change_prefix $
```

## Fonctions help
#### help
> Cette fonction prends plusieurs type de paramètres. En revanche aucune permissions sont requise pour s'en servir.
> **Cette fonction est un peu particulière appellée sans paramètre, elle permet d'afficher un listing complet des modules (cogs) du bot comme le montre cette image :**
  
<img src="https://cdn.discordapp.com/attachments/837802340802625536/948704537349357609/HELP0.png" width="50%">
> **En revanche c'est également une fonction qui prend des paramètres, les noms des cogs seront toujours affiché avec une majuscule, et les fonctions toujours en miniscules. Donc si je veux savoir les fonctions qui sont contenue dans le modules ``Help`` ou bien ``CogSetupLog`` il me suffit de les appeler comme ci dessous :**

<img src="https://cdn.discordapp.com/attachments/837802340802625536/948705559882891304/Help.png" width="50%">
> **De cette même manière je peux savoir pour les fonctions, afin de connaître leurs syntaxe, si c'est une fonction qui s'utilise avec ou sans paramètres :**

<img src="https://cdn.discordapp.com/attachments/837802340802625536/948704205349195786/Help2.png" width="50%">
#### listing
> **Cette fonctions permet simplement de faire une liste de toute les fonctions du bot sans infos supplémentaire.**
> Ne prend aucun paramètre et aucune permissions sont requise.
## Fonctions admin
#### mute
> **Cette fonction permet de mute un utilisateur, en lui affectant un role ``Muted`` qui lui retire toute permissions de discussion (chat écris et vocal)**
> Cette fonction prend donc en paramètre l'utilisateur (mention ou ID) et la permission ``manage_messages`` est requise.
#### unmute
> **Cette fonction permet de retirer le rôles ``Muted`` qui lui retire toute permissions de discussion (chat écris et vocal) et donc cette fonction lui permet de chatter à nouveau**
> Cette fonction prend donc en paramètre l'utilisateur (mention ou ID) et la raison (facultatif). La permission ``manage_messages`` est requise.
#### ban
> **Cette fonction permet de bannir un utilisateur du serveur.**
> Cette fonction prends donc en paramètre l'utilisateur (mention ou ID) et la raison (facultatif). La permission ``ban_members`` est requise.
#### unban
> **Cette fonction permet de débannir un utilisateur du serveur.**
> Cette fonction prends donc en paramètre l'utilisateur (ID) et la raison (facultatif). La permission ``ban_members`` est requise.
#### show_ban
> **Cette fonction permet d'afficher la liste des utilisateurs banni**
> Elle ne prends donc aucun paramètre, mais requière la permission ``kick_members``.
#### kick
> **Permet d'exclure un utilisateur du serveur**
> Cette fonction prends en paramètre l'utilisateur (mention ou ID) et la raison (facultatif). Il faut avoir la permissions ``kick_members``.
#### warn
> **Permet de warn (avertir) un utilisateur. Les deux premières fois un rôle lui sera ajouté. (Avertissement 1 et Avertissement 2) et au troisième c'est le ban.**
> Cette fonction prend donc en paramètre l'utilisateur (mention ou ID) et la raison (facultatif). La permission ``ban_members`` est requise.
#### show_warn
> **Affiche la liste des utilisateurs warn du serveur, ou alors la liste des warn d'un utilisateur en question**
> Cette fonction prend donc en paramètre l'utilisateur (mention ou ID) si il faut voir les warns d'un seul utilisateur, ou alors aucun paramètre si il faut voir tout les warns. La permission ``ban_members`` est requise.
#### purge
> **Permet de supprimer un nombre de message**
> Cette fonction prends donc en paramètre le nombre de message à supprimer. La permission ``manage_messages`` est requise.
## Fonctions infos
#### server_info
> **Affiche les informations du serveur discord**
> Ne prends aucun paramètre et aucune permissions sont requise.
#### user_info
> **Afiche les informations d'un utilisateur**
> =Prends en paramètre l'utilisateur (mention ou alors ID) et aucune permissions sont requise.
## Fonction embeds
#### embeds
> **Formatte tout simplement un message dans un embed avec couleur aléatoire. L'embed prends en charge les images (png, jpeg) et les GIF.**
> La fonction prends donc en paramètre le message, mais aucune permissions sont requise pour s'en servir.
