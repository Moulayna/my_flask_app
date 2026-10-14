from flask import Flask
import home

app = Flask(__name__)


@app.route("/")
def home_page():
  return home.home_page()


# @app.route("/projects")
# def projects():
#   return "Hello, World!"

# @app.route("/cv")
# def cv():
#   return "Hello, World!"


# @app.route("/publications")
# def publications():
#   return "Hello, World!"

# @app.route("/contact")
# def contact():
#   return "Hello, World!"


if __name__ == "__main__":
  app.run(debug=True)
