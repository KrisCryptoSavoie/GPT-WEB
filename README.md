# GPT-WEB

--------------------- APPLICATION EN COURS DE DEVELOPPEMENT -------------------------------------

        MODE TEST
        



Recherche OpenAI - Application web Flask

Cette application web utilise Flask, Beautiful Soup et l'API OpenAI pour répondre aux questions posées par les utilisateurs. Lorsqu'une URL est fournie, l'application tente d'extraire des informations pertinentes du site Web à l'aide de Beautiful Soup. Si aucune URL n'est fournie, l'application utilise l'API OpenAI pour répondre à la question.

Installation et configuration :

1. Assurez-vous d'avoir Python 3.x installé sur votre système. Vous pouvez le télécharger depuis le site officiel de Python : https://www.python.org/downloads/

2. Ouvrez un terminal (Command Prompt ou PowerShell sur Windows, Terminal sur macOS et Linux) et installez les dépendances nécessaires en exécutant la commande suivante :
   pip install beautifulsoup4 requests flask

   Note : Sur certains systèmes, vous devrez peut-être utiliser "pip3" à la place de "pip".

3. Remplacez "votre_clé_api_openai" par votre clé API OpenAI dans le fichier app.py.

Exécution de l'application :

1. Ouvrez un terminal (Command Prompt ou PowerShell sur Windows, Terminal sur macOS et Linux) et accédez au dossier contenant le fichier app.py.

2. Exécutez la commande suivante pour lancer l'application :
   python app.py

   Note : Sur certains systèmes, vous devrez peut-être utiliser "python3" à la place de "python".

3. Ouvrez un navigateur web et accédez à l'URL suivante :
   http://127.0.0.1:5000/

Utilisation de l'application :

1. Entrez votre question dans le champ "Question".

2. Si vous souhaitez extraire des informations d'un site Web spécifique, entrez l'URL du site dans le champ "URL du site". Sinon, laissez ce champ vide pour utiliser l'API OpenAI.

3. Cliquez sur le bouton "Rechercher" pour soumettre votre question et afficher la réponse.
