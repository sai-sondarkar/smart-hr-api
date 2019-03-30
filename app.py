
from fuzzywuzzy import fuzz
from flask import Flask, abort, jsonify, request



app = Flask(__name__)

@app.route('/api', methods=['POST'])
def match_competency():
    data = request.get_json(force=True)
    
    num = fuzz.ratio('skilla skillb skillc','skilla skillb')
    output = {'match': int(num)}
    print(output)
    return jsonify(results=output)

if __name__ == '__main__':
    app.run()
 #   app.run(host='0.0.0.0',port='80')

    
