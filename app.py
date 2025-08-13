from flask import Flask, request, send_from_directory, render_template
import os

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        f = request.files["file"]
        f.save(os.path.join(UPLOAD_FOLDER, f.filename))
        return f"""
        ✅ Datei hochgeladen: <a href='/download/{f.filename}'>{f.filename}</a><br>
        <a href='/'>⬅️ Zurück</a>
        """
    return render_template("index.html")

@app.route("/download/<filename>")
def download(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

if __name__ == "__main__":
    app.run()
