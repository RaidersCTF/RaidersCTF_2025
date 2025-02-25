from flask import Flask, request, jsonify, redirect
import requests
import os

app = Flask(__name__)

FLAG = 'RaidersCTF{XXXXXXXXXXXXXXXX}'

@app.route('/')
def index():
    return """
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Image URL Validator</title>
        <script src="https://cdn.tailwindcss.com"></script>
    </head>
    <body class="bg-[#0A1727] flex justify-center items-center min-h-screen">
        <div class="bg-white p-6 rounded-lg shadow-lg w-full max-w-md">
            <h1 class="text-2xl font-semibold text-center text-gray-700 mb-4">Image URL Validator</h1>
            <p class="text-center text-gray-600 mb-6">This service checks if an image URL is accessible.</p>
            <form action="/check_url" method="POST" class="space-y-4">
                <input type="text" name="url" placeholder="Enter image URL" class="w-full p-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500">
                <input type="submit" value="Check" class="w-full p-3 bg-[#0A1727] text-white rounded-lg hover:bg-[#2E3C4D] cursor-pointer">
            </form>
        </div>
    </body>
    </html>
    """

@app.route('/check_url', methods=['POST'])
def check_url():
    url = request.form.get('url')
    source_ip = request.form.get('source_ip', None)
    if not url:
        return jsonify({"error": "No URL provided"})
    try:
        if (('internal/api' in url) and (source_ip != '')):
            return redirect(f'/internal/api?source_ip={source_ip}')
        if '/internal/api' in url:
            return redirect('/internal/api')
        response = requests.get(url, timeout=5)
        return jsonify({
            "status": "success",
            "message": f"URL is accessible! Status code: {response.status_code}",
            "content_type": response.headers.get('content-type', 'unknown'),
            "content": response.text
        })
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route('/internal/api', methods=['GET', 'POST'])
def internal_api():
    source_ip = request.args.get('source_ip')

    # This endpoint should only be accessible from localhost
    if source_ip != '127.0.0.1':
        return jsonify({"error": "Access denied"}), 403

    return jsonify({
        "message": "Internal API accessed successfully!",
        "flag": FLAG
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5656)