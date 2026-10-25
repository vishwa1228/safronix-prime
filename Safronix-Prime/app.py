from flask import Flask, render_template, request, flash, redirect, url_for
import os

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "change-this-before-deployment")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/contact", methods=["POST"])
def contact():
    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip()
    service = request.form.get("service", "").strip()
    message = request.form.get("message", "").strip()

    if not all([name, email, message]):
        flash("Please complete all required fields.", "error")
        return redirect(url_for("home") + "#contact")

    if len(name) > 120 or len(email) > 254 or len(message) > 5000:
        flash("Please shorten your submission and try again.", "error")
        return redirect(url_for("home") + "#contact")

    if "@" not in email or "." not in email.rsplit("@", 1)[-1]:
        flash("Please enter a valid email address.", "error")
        return redirect(url_for("home") + "#contact")

    # TODO: Send the enquiry to your company email or save it
    # to a database. Do not log sensitive form contents.

    app.logger.info("Contact enquiry received for service: %s", service)
    flash(
        "Thank you for contacting Safronix Prime! "
        "Your form is validated, but email delivery must be configured.",
        "success"
    )
    return redirect(url_for("home") + "#contact")


if __name__ == "__main__":
    app.run(debug=True)
