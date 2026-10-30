from flask import Flask
import home
import projects
import health
import haii
import responsibledesign 
import page_wrapper

app = Flask(__name__)


@app.route("/")
def home_page():
  return page_wrapper.page_wrapper("Homepage",home.home_page())


@app.route("/projects")
def project():
  return page_wrapper.page_wrapper("project", projects.projects())

@app.route("/health")
def healths():
  return page_wrapper.page_wrapper("health", health.health_project())

@app.route("/haii")
def HAIIs():
  return page_wrapper.page_wrapper("HAIIs", haii.haii_project())

@app.route("/responsible design")
def Responsibledesigns():
  return page_wrapper.page_wrapper("responsible design", responsibledesign.responsibledesign_project())


@app.route("/cv")
def cv():
  return "Hello, World!"


@app.route("/publications")
def publications():
  return "Hello, World!"

@app.route("/contact")
def contact():
  return "Hello, World!"


if __name__ == "__main__":
  app.run(debug=True)

