from music_controller.music_controller import MusicControll
from flask import Flask


MUSIC_LIST = [] #샘플 음악 파일 입력

music = MusicControll(MUSIC_LIST)

app = Flask(__name__)

@app.route('/')
def ConnectionTest():
    return "Success"

@app.route('/start/')
def StartMusic():
    music.music_start()

@app.route('/pause/')
def PauseMusic():
    music.music_stop()

@app.route('/next/')
def StartMusic():
    music.next_song()

@app.route('/previous/')
def StartMusic():
    music.previous_song()

if __name__ == '__main__':
    app.run(debug=True)




