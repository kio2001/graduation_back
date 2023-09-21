from flask import Flask, request, jsonify
import lyricsgenius
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

 
@app.route('/get_lyrics', methods=['GET'])
def get_lyrics():
    artist_name = request.args.get('artist_name')
    song_name = request.args.get('song_name')
    access_token = request.headers.get('Authorization')

    try:
        # 歌詞を取得
        song = genius.search_song(song_name, artist_name)
        if song:
            lyrics = song.lyrics
            return jsonify({'lyrics': lyrics})
        else:
            return jsonify({'error': 'Song not found'})

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)