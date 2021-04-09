from flask import Flask, Blueprint, jsonify

app = Flask("__name__")


@app.route('/', methods=['GET', 'POST'])
def func():
    return jsonify({"Егор": {
                    "русский": 81,
                    "математика": 96,
                    "информатика": 100},
                    "Алим": {
                    "русский": 80,
                    "математика": 100,
                    "информатика": 100}})


@app.route('/get_data/<name>,<int:age>')
def api(name, age):
    a = {
        "Егор": {"русский": 80,"матемтика": 80,"информатика": 75},
        "Алим": {"русский": 75,"матемтика": 68,"информатика": 78,'age':age}
    }
    return jsonify(a[name])


if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1")