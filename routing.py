from flask import Flask
# from flask.helpers import make_response
app = Flask(__name__)


# # 404
# @app.errorhandler(404)
# def not_found():
#   print("="*5,"404", "="*5)
#   return make_response("nothing here", 404)

@app.route('/<path:dummy>')
def fallback(dummy):
    return 'This one catches everything else'

@app.route("/")
@app.route("/index")
def start():
  print("---> /")
  return "Hello World!"

@app.route("/dojo")
def dojo():
  print("---> /dojo")
  return "Dojo!"

@app.route("/say/<name>")
def say(name):
  print("---> /say/"+ name)
  return "hello " + name.capitalize() 

# Create one url pattern and function that can handle the following examples (HINT: int() will come in handy! For example int("35") returns 35):
# localhost:5000/repeat/35/hello - have it say "hello" 35 times
# localhost:5000/repeat/80/bye - have it say "bye" 80 times
# localhost:5000/repeat/99/dogs - have it say "dogs" 99 times
@app.route("/repeat/<int:num>/<string>")
def pattern(num, string):
  print(f"---> /repeat {num}x {string}")
  return string * num
  # return string * int(num)
  

if __name__=="__main__":
  app.run(debug=True)