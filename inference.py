from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["POST"])
def run():
    try:
        data = request.get_json(force=True)
        return jsonify({
            "output": "Success"
        })
    except:
        return jsonify({
            "output": "Error"
        })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7860)
