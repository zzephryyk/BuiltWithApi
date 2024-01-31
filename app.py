from Scrapper.BuilWith import Model
from flask import Flask, jsonify, request

app = Flask(__name__)
@app.route("/")
def Home():
    return jsonify({"/SiteLookup": "Working"})

@app.route("/SiteLookup")
def SiteLookup():
    url = request.args.get("url")
    scrape = Model(url)
    scrape.run()
    return jsonify(scrape.content)
