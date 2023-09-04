from typing import TypeAlias
import os


_DP: TypeAlias = str
_MD: TypeAlias = str
_EXCLUDED_DIRS = (
    '__pycache__'
)


def get_dirs_for_celery_tasks(
    src_path: _DP, *, prefix: str = ""
        ) -> list[_MD]:
    """
    Returns directories where will look for the tasks,
    you can define prefix from directories if you want
    """
    dirlist: list[_MD] = []

    for dir_ in os.listdir(src_path):
        dir_path = os.path.join(src_path, dir_)
        if os.path.isdir(dir_path) and dir_ not in _EXCLUDED_DIRS:
            dirlist.append(prefix + "." + dir_)

    return dirlist
