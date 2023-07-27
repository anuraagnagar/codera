from flask import render_template as render
from flask import views
import json

with open("flask_blog/confi.json", "r") as c:
    params = json.load(c)["parameter"]


class JavaView(views.View):

    template = "tutorial/java/javatutorial.html"

    def dispatch_request(self):
        return render(self.template, params=params)


class JavaScriptView(views.View):

    template = "tutorial/javascript/javascript.html"

    def dispatch_request(self):
        return render(self.template, params=params)


class StartingPythonView(views.View):

    template = "tutorial/python/starting_python.html"

    def dispatch_request(self):
        return render(self.template, params=params)


class InstallPythonView(views.View):

    template = "tutorial/python/install_python.html"

    def dispatch_request(self):
        return render(self.template, params=params)


class VscodeSetupView(views.View):

    template = "tutorial/python/vscode_setup.html"

    def dispatch_request(self):
        return render(self.template, params=params)


class FirstProgramView(views.View):

    template = "tutorial/python/first_program.html"

    def dispatch_request(self):
        return render(self.template, params=params)

