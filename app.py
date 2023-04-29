from flask import Flask, render_template, request
import requests
import json
from bs4 import BeautifulSoup

API_KEY = "your-opeai-api-key"
app = Flask(__name__)

def search_openai(query, url=None):
    if url:
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.content, "html.parser")
            
            # Extraire tous les paragraphes
            paragraphs = soup.find_all('p')
            extracted_text = ' '.join([p.get_text() for p in paragraphs])

            return f"Les informations extraites du site Web sont les suivantes : {extracted_text}"
        except Exception as e:
            print(f"Erreur lors de l'extraction des données du site Web : {e}")
            return "Désolé, une erreur s'est produite lors de l'extraction des données du site Web."

    # Si aucune URL n'est fournie, utilisez l'API OpenAI pour répondre à la question
    prompt = f"Veuillez fournir une réponse précise et vérifiable à la question suivante : {query}"
    
    url = "https://api.openai.com/v1/engines/davinci/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }
    data = {
        "prompt": prompt,
        "max_tokens": 100,
        "n": 1,
        "stop": None,
        "temperature": 0.5,
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    response_json = response.json()

    if "choices" in response_json and len(response_json["choices"]) > 0:
        return response_json["choices"][0]["text"].strip()
    else:
        print(f"Erreur inattendue dans la réponse de l'API OpenAI: {response_json}")
        return "Désolé, une erreur s'est produite lors de la recherche de votre réponse."

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    query = request.form['query']
    url = request.form['url']
    answer = search_openai(query, url)
    return render_template('index.html', query=query, answer=answer)

if __name__ == '__main__':
    app.run(debug=True)
