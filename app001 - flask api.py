from flask import Flask, jsonify


#app instance
app = Flask(__name__)

#http://127.0.0.1:5000/api/home
@app.route("/api/home", methods=['GET'])
def return_home():
    return jsonify({
        'message':"Hello world!"
    })

if __name__ == "__main__":
    app.run(debug=True)

