import pathlib

PATH = pathlib.Path(__file__)
RESOURCES = PATH.parent.joinpath('Resources')

STYLEVAR = RESOURCES.joinpath('styleVariables.txt')
STYLE = RESOURCES.joinpath('style.qss')