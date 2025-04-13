from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/disponibilidade', methods=['POST'])
def disponibilidade():
    return jsonify({
        "especialidade": "Cardiologia",
        "medico": "Dr. Paulo Silveira",
        "horarios": [
            "15/04 - 09:00",
            "15/04 - 10:30",
            "15/04 - 14:00"
        ]
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
