from flask import Flask, request, send_from_directory, render_template
import flask_cors
import os

app = Flask(__name__)
flask_cors.CORS(app)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        f = request.files["file"]
        f.save(os.path.join(UPLOAD_FOLDER, f.filename))
        return f"""
        <!DOCTYPE html>
        <html lang="de">
        <head>
        <meta charset="UTF-8">
        <title>Upload erfolgreich</title>
        <style>
            body {{
            font-family: 'Inter', sans-serif;
            background: #f0f4f8;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            }}
            .message-box {{
            background: white;
            padding: 30px;
            border-radius: 12px;
            box-shadow: 0 8px 16px rgba(0,0,0,0.1);
            text-align: center;
            }}
            a {{
            display: inline-block;
            margin-top: 10px;
            color: #4a90e2;
            text-decoration: none;
            font-weight: 600;
            }}
            a:hover {{
            text-decoration: underline;
            }}
            button {{
            margin-top: 10px;
            padding: 10px 20px;
            font-size: 14px;
            border: none;
            border-radius: 8px;
            background-color: #4a90e2;
            color: white;
            cursor: pointer;
            transition: background-color 0.3s ease;
            }}
            button:hover {{
            background-color: #357ab8;
            }}
            .copied {{
            margin-top: 10px;
            font-size: 13px;
            color: green;
            display: none;
            }}
        </style>
        </head>
        <body>
        <div class="message-box">
            <h2>✅ Datei erfolgreich hochgeladen!</h2>
            <p><a id="download-link" href='/download/{f.filename}'>📥 {f.filename} herunterladen</a></p>
            <button onclick="copyLink()">🔗 Link kopieren</button>
            <div class="copied" id="copied-msg">✅ Link kopiert!</div>
            <p><a href='/'>⬅️ Neue Datei hochladen</a></p>
        </div>

        <script>
            function copyLink() {{
            const link = window.location.origin + document.getElementById("download-link").getAttribute("href");
            navigator.clipboard.writeText(link).then(() => {{
                const msg = document.getElementById("copied-msg");
                msg.style.display = "block";
                setTimeout(() => msg.style.display = "none", 2000);
            }});
            }}
        </script>
        </body>
        </html>
        """


    return render_template("index.html")

@app.route("/download/<filename>")
def download(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

if __name__ == "__main__":
    app.run()
