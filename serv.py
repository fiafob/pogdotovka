import flask
import json

app = flask.Flask(__name__)
app.config["SECRET_KEY"] = "jkfd"


@app.route("/", methods=["GET", "POST"])
def return_data():
    a = {
        "Egor": [{"matan": 85, "rus": 79},
                 {"rus": 80, "info": 90}],
        "Alim": [{"matan": 79, "info": 100}]
        }
    return flask.jsonify(a)


def main():
    app.run(port=8080, host="127.0.0.1")


if __name__ == "__main__":
    main()
