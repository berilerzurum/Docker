from flask import request, Flask
import json

app2 = Flask(__name__)
@app2.route('/')

def hello_world():
  
  return 'this is response from app2'

if __name__ == '__main__':
  app2.run(debug=True, host='0.0.0.0')
 
#5000 portundan cevap verecek.
