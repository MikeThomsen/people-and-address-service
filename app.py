from flask import Flask, jsonify, request
import usaddress as usa
import probablepeople as pp

app = Flask(__name__)

@app.route("/address", methods=['POST'])
def address():
  tagged = usa.tag(request.json['raw_address'])
  return jsonify(tagged)

@app.route("/person", methods=['POST'])
def person():
  tagged = pp.tag(request.json['raw_person'])
  return jsonify(tagged)

if __name__ == '__main__':
  app.run()

