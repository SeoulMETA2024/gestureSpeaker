from flask import Flask, Response
from picamera import PiCamera
from picamera.array import PiRGBArray
import time
import cv2
from music_controller.music_controller import MusicControll
from flask import Flask

MUSIC_LIST = ['music_1.mp3', 'music_2.mp3', 'music_3.mp3']  #샘플 음악 파일 입력

music = MusicControll(MUSIC_LIST)

app = Flask(__name__)

camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 30
raw_capture = PiRGBArray(camera, size=(640, 480))
time.sleep(0.1) 

def generate_frames():
    for frame in camera.capture_continuous(raw_capture, format="bgr", use_video_port=True):
        image = frame.array
        _, buffer = cv2.imencode('.jpg', image)
        frame = buffer.tobytes()
        raw_capture.truncate(0)

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    return ("<html><head><title>Video Streaming</title></head>"
            "<body><h1>Video Streaming</h1>"
            "<img src='/video_feed' width='640' height='480'></body></html>")


@app.route('/start/')
def StartMusic():
    music.music_start()
    return "START"


@app.route('/pause/')
def PauseMusic():
    music.music_stop()
    return "STOP"



@app.route('/next/')
def NextMusic():
    music.next_song()
    return "NEXT"


@app.route('/previous/')
def PreviousMusic():
    music.previous_song()
    return "PREVIOUS"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)