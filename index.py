import os
from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)

l=os.listdir('static/images/thumbs/')
filelist=[x.split('.')[0] for x in l]

@app.route("/")
def index():
    lista = []
    for image in filelist:
        if image.startswith("C1"):
            lista.append(image)

    return render_template("/index.html", data = lista, count = len(lista))

@app.route("/index2")
def index2():
    lista = []
    for image in filelist:
        if image.startswith("C2"):
            lista.append(image)
    return render_template("/index2.html", data = lista, count = len(lista))
    
@app.route("/index3")
def index3():
    lista = []
    for image in filelist:
        if image.startswith("C3"):
            lista.append(image)
    return render_template("/index3.html", data = lista, count = len(lista))

@app.route("/index4")
def index4():
    lista = []
    for image in filelist:
        if image.startswith("C4"):
            lista.append(image)
    return render_template("/index4.html", data = lista, count = len(lista))

@app.route("/index5")
def index5():
    lista = []
    for image in filelist:
        if image.startswith("C5"):
            lista.append(image)
    return render_template("/index5.html", data = lista, count = len(lista))

if __name__ == '__main__':
    app.run(debug=True)
