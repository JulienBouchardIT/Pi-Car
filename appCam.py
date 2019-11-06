from flask import Flask, render_template, Response, request
from camera_pi import Camera
from light_led import *

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        if request.form.get('red_button') == 'red':
            red()
        elif request.form.get('green_button') == 'green':
            green()
        elif request.form.get('blue_button') == 'blue':
            blue()
        elif request.form.get('on_button') == 'ON':
            on()
        elif request.form.get('off_button') == 'OFF':
            off()
        return Response
    else:
        return render_template("index.html")


@app.route("/api/command", methods=['POST'])
def command():
    command = request.form.get('command')
    power = request.form.get('power') == 'true'
    if command == 'up':
        up(power)
    if command == 'down':
        down(power)
    if command == 'left':
        left(power)
    if command == 'right':
        right(power)


def gen(camera):
    """Video streaming generator function."""
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True, threaded=True)
