from .models import Tutorials
from .views import (
    FirstProgramView,
    InstallPythonView,
    JavaView,
    JavaScriptView,
    StartingPythonView,
    VscodeSetupView,
)

__all__ = [
    "Tutorials",
    "FirstProgramView",
    "InstallPythonView",
    "JavaView",
    "JavaScriptView",
    "StartingPythonView",
    "VscodeSetupView"
]

first_program = FirstProgramView.as_view('first_program')
install_python = InstallPythonView.as_view('install_python')
java = JavaView.as_view('java')
javascript = JavaScriptView.as_view('javascript')
starting_python = StartingPythonView.as_view('starting_python')
vscode_setup = VscodeSetupView.as_view('vscode_setup')