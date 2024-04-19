from flask import Flask, render_template, request
from functions import *
import pandas as pd
import chromadb
import ast

path = "D:/my computer/Downloads/data.csv"
df = pd.read_csv(path)

def chroma_store(ids, names, subtitles, embeddings):
  chroma_client = chromadb.Client()
  collection = chroma_client.create_collection(name="my_collection")

  collection.add(
    # embeddings=[embedding for embedding in embeddings],
    embeddings = [ast.literal_eval(embedding) if isinstance(embedding, str) else embedding for embedding in embeddings],
    documents=[f'doc{n}' for n in range(len(ids))],
    metadatas = [{name: subtitle} for name, subtitle in zip(names, subtitles)],
    ids=[str(id) for id in ids]
  )
  return collection

collection = chroma_store(df["ID"].tolist(), df["Name"].tolist(), df["Subtitle"].tolist(), df["embeddings"].tolist())






app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')


@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        query = request.form.get("input_text")
        query_embedding = extract_embeddings("Iron man").numpy()[0]
        results = collection.query(
            query_embeddings=[query_embedding.tolist()],
            n_results=2,
        )
   
        return render_template('index.html', query=query, results=results)

        

if __name__ == "__main__":
    app.run(debug=True)