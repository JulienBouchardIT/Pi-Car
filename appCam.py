from flask import Flask, render_template, Response, request, jsonify
from camera_pi import Camera
from light_led import *


app = Flask(__name__)


@app.route("/", methods=['GET'])
def home():
    return render_template("index.html")


@app.route("/api/command", methods=['POST'])
def command():
    command = request.form.get('command')
    power = request.form.get('power') == 'true'
    if command == 'up':
        return 'up'
    if command == 'down':
        return 'down'
    if command == 'left':
        return 'left'
    if command == 'right':
        return 'right'


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
