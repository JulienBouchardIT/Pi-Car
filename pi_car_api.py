from flask import Flask, render_template, request, Response
from camera import VideoCamera
from light_led import *

app = Flask(__name__)
video_camera = VideoCamera(flip=True) # creates a camera object, flip vertically


@app.route("/", methods=['GET', 'POST'])
def home():
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
    elif command == "off":
        off()
    elif command == "red":
        red()
    elif command == "green":
        green()
    elif command == "blue":
        blue()
    else:
        return "Invalid args"
    return command+" DONE"


def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@app.route('/video_feed')
def video_feed():
    return Response(gen(video_camera),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == "__main__":
 app.run(host="0.0.0.0", port=80, debug=True)
