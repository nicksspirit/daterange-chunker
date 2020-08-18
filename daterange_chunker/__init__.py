import importlib.resources as pkg_resources
from pathlib import Path


def resource_path(resrc: str) -> Path:
    with pkg_resources.path(f"{__package__}.assets", resrc) as resrc_path:
        return resrc_path.resolve()
