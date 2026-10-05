from flask import Flask, render_template, request
from flames import calculate_flames
import re

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():

    result = None
    error = None

    if request.method == "POST":

        your_name = request.form["your_name"].strip()
        person_name = request.form["person_name"].strip()

        # Check if names are empty
        if not your_name or not person_name:

            error = "Please enter both names."

        elif not isinstance(your_name, str) or not isinstance(person_name, str):

            error = "Please enter valid names."

        elif not re.match("^[A-Za-z ]+$", your_name) or not re.match("^[A-Za-z ]+$", person_name):

            error = "Please enter valid names containing only letters"

        else:

            result = calculate_flames(your_name, person_name)

    return render_template(
        "index.html",
        result=result,
        error=error
    )


if __name__ == "__main__":
    app.run(debug=True)
