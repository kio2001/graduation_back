from flask import Flask, request, jsonify
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins='*', supports_credentials=True) # すべてのエンドポイントにCORSを設定

client_id = '03cdba40b89844e49b62ff7e3d4d2076'
client_secret = '3b3536682e554c22adffed3234ba5253'
client_credentials_manager = spotipy.oauth2.SpotifyClientCredentials(client_id, client_secret)
spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

@app.route('/get_track_info', methods=['GET'])
def get_track_info():
    track_name = request.args.get('track_name')
    artist_name = request.args.get('artist_name')
    
    # 楽曲情報を検索
    result = spotify.search(q=f'track:{track_name} artist:{artist_name}', type='track')
    
    # 最初の楽曲情報を取得
    if result['tracks']['items']:
        track_info = result['tracks']['items'][0]
        return jsonify(track_info)
    else:
        return jsonify({'error': '楽曲が見つかりませんでした'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8083)