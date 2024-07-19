import os
from fuzzywuzzy import fuzz
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from flask import Flask, send_file, request, jsonify
# import requests
import json
import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("thesis-afea3-firebase-adminsdk-c941w-4b972b5f3e.json")
firebase_admin.initialize_app(cred)

data = pd.read_excel('1_Judul SKRIPSI Prodi TI.xlsx', sheet_name="judul_fix")
x, y = data.shape
documents = []
for i in range(4, x):
    documents.append({
        'npm': data.loc[i][1],
        'nama': data.loc[i][2],
        'judul': data.loc[i][3],
    })

def tfidf_fuzzy_similarity(query, documents):
    # TF-IDF vectorization
    tfidf_vectorizer = TfidfVectorizer()
    document = [i['judul'] for i in documents]
    tfidf_matrix = tfidf_vectorizer.fit_transform(document)

    # log base 10, ex: math.log10(x) or math.log(x, 10)

    # Calculate similarity scores using TF-IDF
    query_vector = tfidf_vectorizer.transform([query])
    tfidf_scores = (query_vector * tfidf_matrix.T).A[0]
    
    # Fuzzy matching and combining with TF-IDF scores
    similarity_scores = []
    for docs, tfidf_score in zip(documents, tfidf_scores):
        doc = docs['judul']
        fuzzy_score = fuzz.token_set_ratio(query, doc)
        similarity_scores.append([docs, tfidf_score * (fuzzy_score / 100)])  # Combine TF-IDF and fuzzy scores
    # Sort documents by combined similarity score   
    similarity_scores.sort(key=lambda x: x[1], reverse=True)
    return similarity_scores

app = Flask(__name__)

# http://nurzz.pythonanywhere.com/get_data?query=implementasi%20algoritma%20winnowing

@app.route("/")
def index():
    return jsonify({
        'status': "success",
        "message": "is working"
    })

@app.route("/get_data", methods=['GET'])
def getdata():
    # Get url params
    db = firestore.client()
    data = db.collection("cek_judul_skripsi").document("judul").get().to_dict()
    documents = [i for i in data['data']]
    query = request.args.get('query')

    if request.method == 'GET':
        return jsonify({
            'query': ''.join(query),
            'status': 'success',
            'data': [i for i in tfidf_fuzzy_similarity(query, documents) if float(i[1]) > 0.25]
        })

def main():
    app.run(port=int(os.environ.get('PORT', 3000)))

if __name__ == "__main__":
    main()
    # db = firestore.client()
    # data = db.collection("cek_judul_skripsi").document("judul").set({
    #     "data": documents
    # })
    # for data in documents:
    #     db.collection("judul").add(data)
    
    # main()
    # endpoint = 'database_get.php'
    # response = requests.get(URL + endpoint)
    # print(response)