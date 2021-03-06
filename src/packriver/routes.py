import spacy
import PyPDF2
from spacy.matcher import Matcher
from packriver import app
from flask import (render_template, request)

nlp = spacy.load("en_core_web_sm")


@app.route('/')
@app.route('/home')
def index():
    return render_template("index.html")

@app.route('/demo1',  methods=('GET', 'POST'))
def summary_demo():
    text_verbs = []
    if request.method == 'POST':
        text = request.form['user_text']
        matcher = Matcher(nlp.vocab)
        pattern = [{'POS': 'VERB', 'OP': '?'},
           {'POS': 'ADV', 'OP': '*'},
           {'POS': 'AUX', 'OP': '*'},
           {'POS': 'VERB', 'OP': '+'}]
        matcher.add("PROPER_NOUN", [pattern])
        doc = nlp(text)
        matches = matcher(doc)
        print (len(matches))
        for match in matches[:20]:
            text_verbs.append(doc[match[1]:match[2]])
        print(text_verbs)
    return render_template("summary.html", text_verbs=text_verbs)


@app.route('/<word>',  methods=('GET', 'POST'))
def term_demo(word):
    info = word
    return render_template("info_term.html", info=info)

@app.route('/upload',  methods=('GET','POST'))
def upload_pdf():
    data = []
    if request.method == 'POST':
        reader = PyPDF2.PdfFileReader('CELEX 32014L0030 EN TXT.pdf')
        numOfPages = reader.getNumPages()
        for i in range(0, numOfPages):
            print("Page Number: " + str(i))
            print("- - - - - - - - - - - - - - - - - - - -")
            pageObj = reader.getPage(i)
            print(pageObj.extractText())
            data.append(pageObj.extractText())
            print("- - - - - - - - - - - - - - - - - - - -")
    return render_template("upload_pdf.html", data=data)