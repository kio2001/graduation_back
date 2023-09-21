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

@app.route('/get_artist', methods=['GET'])
def get_artist():
    name = request.args.get('name')
    print("name", name)
    result = spotify.search(q='artist:' + name, type='artist')
    return jsonify(result['artists'])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8082) 