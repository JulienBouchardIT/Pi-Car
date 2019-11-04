from flask import Flask, render_template, request
from light_led import *

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def home():
    print(request)
    if request.method == 'POST':
        if request.form.get('red_button') == 'red':
            red()
        elif request.form.get('green_button') == 'green':
            green()
        elif request.form.get('blue_button') == 'blue':
            blue()
        elif request.form.get('on_button') == 'on':
            on()
        elif request.form.get('off_button') == 'off':
            off()
    return render_template("home.html")

@app.route("/api/<string:command>/")
def execute(command):
 if command == "on":
  on()
  return "on DONE"
 elif command == "off":
  off()
  return command+" DONE"
 elif command == "red":
  red()
  return command+" DONE"
 elif command == "green":
  green()
  return command+" DONE"
 elif command == "blue":
  blue()
  return command+" DONE"
 else:
  return "Invalid args"

if __name__ == "__main__":
 app.run(host="0.0.0.0",port=80,debug=True)

