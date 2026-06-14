from flask import Flask, request, jsonify, send_file
import requests
import urllib.parse
import base64

app = Flask(__name__, static_folder='.', static_url_path='')

STYLE_PROMPTS = {
    'Anime':     'anime style, vibrant colors, detailed illustration, high quality, beautiful character portrait, cel shading',
    'Realistic': 'realistic, photorealistic, detailed portrait, professional photography, cinematic lighting, 8k ultra detailed',
    'Cyberpunk': 'cyberpunk aesthetic, neon lights, futuristic city background, sci-fi, detailed, high quality, blade runner style',
    'Fantasy':   'fantasy art style, magical atmosphere, epic composition, detailed digital painting, high quality, artstation',
    'Oil Paint': 'oil painting, artistic masterpiece, rich textures, painterly brushstrokes, museum quality, impressionist',
    'Pixel Art': 'pixel art, retro game sprite, 16-bit style, detailed pixel character, clean crisp pixels',
}

QUALITY_SUFFIX = ', masterpiece, best quality, sharp focus, intricate details'
NEGATIVE = 'blurry, low quality, deformed, ugly, bad anatomy, watermark, text'

@app.route('/')
def index():
    return send_file('avatar_ai_spatial.html')

@app.route('/api/generate', methods=['POST'])
def generate():
    data = request.get_json() or {}
    prompt   = data.get('prompt', 'beautiful character portrait').strip()
    style    = data.get('style', 'Anime')
    seed     = int(data.get('seed', 42069))
    width    = int(data.get('width', 512))
    height   = int(data.get('height', 512))

    style_suffix = STYLE_PROMPTS.get(style, STYLE_PROMPTS['Anime'])
    full_prompt  = f"{prompt}, {style_suffix}{QUALITY_SUFFIX}" if prompt else f"{style_suffix}{QUALITY_SUFFIX}"

    encoded = urllib.parse.quote(full_prompt)
    url = (
        f"https://image.pollinations.ai/prompt/{encoded}"
        f"?width={width}&height={height}&seed={seed}&model=flux&nologo=true&enhance=true"
    )

    try:
        resp = requests.get(url, timeout=120)
        if resp.status_code == 200:
            img_b64 = base64.b64encode(resp.content).decode('utf-8')
            ctype   = resp.headers.get('content-type', 'image/jpeg')
            return jsonify({'success': True, 'image': img_b64, 'content_type': ctype})
        else:
            return jsonify({'success': False, 'error': f'Upstream {resp.status_code}'}), 502
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

if __name__ == '__main__':
    print('AvatarAI Spatial — http://0.0.0.0:5000', flush=True)
    app.run(host='0.0.0.0', port=5000, debug=False)
