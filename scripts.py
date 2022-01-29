import sys
import subprocess  # noqa: S404
from pathlib import Path
from typing import Any
from importlib import import_module

current_module = __import__(__name__)

BASE_DIR = Path(__file__).resolve().parent
VENV_PYTHON = BASE_DIR / ".venv/Scripts/python"

PACKAGE_NAME = "enaml_demo"
EXECUTABLE_NAME = "person"
ENTRYPOINT = BASE_DIR / PACKAGE_NAME / "person.py"
ASSETS = BASE_DIR / PACKAGE_NAME / "assets"


def resolve(s: Path) -> str:
    return str(s.resolve())


def build():
    pyinstaller = import_module("PyInstaller.__main__")

    enaml_file = BASE_DIR / PACKAGE_NAME / "person_view.enaml"

    pyinstaller.run(
        [
            "-y",
            f"--name={EXECUTABLE_NAME}",
            "--onedir",
            '--console',
            "--clean",
            '--hidden-import="enaml.core.compiler_helpers"',
            '--hidden-import="atom.api"',
            '--hidden-import="enaml.layout.api"',
            '--hidden-import="enaml.core.enamldef_meta"',
            '--hidden-import="enaml.widgets.api"'
            '--hidden-import="enaml.stdlib.fields"'
            f"--add-data={enaml_file}:.",
            resolve(ENTRYPOINT),
        ]
    )


def default(name):
    name = name.replace("_", "-")

    subprocess.run([VENV_PYTHON, "-m", name] + sys.argv[1:])  # noqa: S603


def __getattr__(name: str) -> Any:
    attrs = set(dir(current_module))

    if name not in attrs:
        return lambda: default(name)
