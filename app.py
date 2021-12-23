from flask import Flask, render_template, request, redirect
import hashlib
from db import DB

# Flask APP Instance
app = Flask(__name__)
# Database Instance
db = DB()


@app.route('/', methods=["POST", "GET"])
def index():
    # URL Shortened State
    shortened = ""
    if request.method == "POST":
        # On URL Shortened Post Method, get the URL entered in the form
        url = request.form.get("url", "")
        # Use the hashlib, SHA256 Hash Algorithm To Hash The URL
        hashed = hashlib.shake_256(url.encode())
        # Get 6 Character URL_ID
        shortened = hashed.digest(6)
        # Use The URL_ID To Get A Node Key
        node = db.get_node(shortened)
        # Using The Key To Get Database Node / Server Instance
        server = db.get_db(node)
        # Insert Data Into the respective Database Table
        cursor = server.cursor()
        cursor.execute(f"""INSERT INTO url_table(url, url_id)values('{url}', '{shortened}')""")
        server.commit()

    return render_template("index.html", shortened=f"http://127.0.0.1:5000/{shortened}" if shortened else "")


@app.route('/favicon.ico')
def favicon():
    return ""


@app.route('/<string:key>', methods=["GET"])
def url_page(key):
    try:
        # Get The Node Key Using URL_ID/Key
        node = db.get_node(key)
        # Get DB Server Instance Using The node
        server = db.get_db(node)
        # Getting Data From Database Table
        cursor = server.cursor()
        cursor.execute(f"""SELECT * FROM url_table WHERE url_id = '{key}'""")
        output = cursor.fetchone()
        server.commit()
        # Redirect To The URL
        return redirect(f"{output[1]}")

    except Exception as e:
        return f"Error {e}"


if __name__ == '__main__':
    app.run(debug=True)
