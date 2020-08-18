import enaml
from importlib import import_module
from enaml.qt.qt_application import QtApplication
from functools import partial

try:
    # Include in try/except block if you're also targeting Mac/Linux
    import ctypes

    app_id = 'com.odintech.apps.daterangechunker'
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(app_id)
except ImportError:
    pass

import_view = partial(import_module, package="daterange_chunker.views")


def main() -> None:
    with enaml.imports():
        App = import_view(".App")

    app = QtApplication()

    app_view = App.AppView()  # type: ignore
    app_view.show()

    app.start()


if __name__ == "__main__":
    main()
