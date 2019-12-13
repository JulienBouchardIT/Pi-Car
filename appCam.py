from flask import Flask, render_template, Response, request, jsonify
from camera_pi import Camera
from motor_control import *
import json


app = Flask(__name__)


@app.route("/", methods=['GET'])
def home():
    return render_template("index.html")


@app.route("/api/command", methods=['POST'])
def command():
    command = request.form.get('command')
    power = request.form.get('power') == 'true'

    print('Command:' + command + ' ' + str(power))

    if power:
        if command == 'up':
            forward()
        if command == 'down':
            backward()
        if command == 'left':
            right()
        if command == 'right':
            left()
    else:
        stop()
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'}


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
    app.run(host='0.0.0.0', port=5000, debug=True, threaded=True)
