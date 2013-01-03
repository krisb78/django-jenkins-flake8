from dj_flake8 import run_flake8


VERSION = (0, 0, 1, 'alpha')

if VERSION[-1] != "final":
    __version__ = '.'.join(map(str, VERSION))
else:
    __version__ = '.'.join(map(str, VERSION[:-1]))

__all__ = [
    '__version__',
    'run_flake8
]
