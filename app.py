import os
from flask import Flask, send_from_directory, render_template

app = Flask(__name__, template_folder='.')

# 1. Rota para liberar a pasta de vídeos
@app.route('/videos/<path:filename>')
def serve_videos(filename):
    return send_from_directory('videos', filename)

# 2. Rota para liberar a pasta de imagens
@app.route('/images/<path:filename>')
def serve_imagens(filename):
    return send_from_directory('images', filename)

@app.route('/.well-known/discord')
def discord_verification():
    dh = os.getenv('dh', '')

    if dh and not dh.startswith('dh='):
        return f"dh={dh}"
    
    return dh

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':

    app.run(host='0.0.0.0', port=8080)

