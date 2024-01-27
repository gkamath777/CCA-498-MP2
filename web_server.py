from flask import Flask, request, jsonify

app = Flask(__name__)
seed_value = 0

@app.route('/', methods=['GET', 'POST'])
def handle_seed():
    global seed_value

    if request.method == 'GET':
        return str(seed_value)

    if request.method == 'POST':
        try:
            data = request.get_json()
            new_seed = int(data['num'])
            seed_value = new_seed
            return jsonify({"message": "Seed value updated successfully"}), 200
        except (KeyError, ValueError):
            return jsonify({"error": "Invalid JSON format or 'num' not found or not an integer"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

