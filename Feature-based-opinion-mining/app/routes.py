from flask import render_template, url_for, redirect
from app import app
from app.model.model import extract_reviews, model_vars
import os

@app.route('/')
def index():
    datasets = []
    files = os.listdir(os.path.join(app.static_folder, 'datasets'))
    # datasets_folder = os.path.join(app.static_folder, 'datasets')
    for file in files:
        # print(os.path.join(datasets_folder, file), file)
        # reviews = extract_reviews(os.path.join(datasets_folder, file), file)
        datasets.append(file)
    return render_template('index.html', datasets=datasets)


@app.route('/<filename>/result')
def result(filename):
    result = extract_reviews(os.path.join(app.static_folder, 'datasets'), filename)
    reviews = result["reviews"]
    reviews.sort(key=lambda x: x[0])
    cm = url_for('static', filename='img/' + filename + ".jpg")
    return render_template('result.html', reviews=reviews, scores=result["scores"], cm=cm, filename=filename)
