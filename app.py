import os
from flask import Flask
from buzz import generator, simulator

app = Flask(__name__)

@app.route("/")
def generate_buzz():
    page = '<html><body><h1>'
    page += generator.generate_buzz()
    page += '<hr width="400" style="border: 3px dotted #0099CC" color="#000000" size="2">'
    page += simulator.generate_simulation()
    page += '</h1></body></html>'
    return page

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)))