from machinetranslation import translator, tests
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench(english_text):
    textToTranslate = request.args.get(english_text)
    # Write your code here
    translated_text = textToTranslate['translations'][0]['translation']
    return json.dumps(translated_text, indent=2, ensure_ascii=False)

@app.route("/frenchToEnglish")
def frenchToEnglish(french_text):
    textToTranslate = request.args.get(french_text)
    # Write your code here
    translated_text = textToTranslate['translations'][0]['translation']
    return json.dumps(translated_text, indent=2, ensure_ascii=False)

@app.route("/")
def renderIndexPage():
    # Write the code to render template
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
