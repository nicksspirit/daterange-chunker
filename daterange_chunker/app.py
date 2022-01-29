import enaml
from importlib import import_module
from enaml.qt.qt_application import QtApplication
from functools import partial


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
