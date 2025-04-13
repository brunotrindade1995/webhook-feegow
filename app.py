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
