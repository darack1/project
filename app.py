from flask import Flask, render_template

app = Flask(__name__)

# Главная страница
@app.route("/")
def index():
    return render_template("index2.html")

# Если в будущем захочешь добавить другие страницы
@app.route("/about")
def about():
    return render_template("about.html")  # если сделаешь такую страницу

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)