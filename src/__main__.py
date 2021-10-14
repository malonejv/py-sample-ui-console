# Proyecto Python y MySql:
# - Login y registro
# - CRUD de notas

import sys
from injector import Injector
from mainAction import MainAction
from infrastructure.ioc import FrontModule
from backend.infrastructure.ioc import BackendModule


def main() -> None:
    injector = Injector([FrontModule, BackendModule()])
    mainAction = injector.get(MainAction)
    mainAction.Init()

    # mainAction = MainAction()
    # mainAction.Init()


if __name__ == '__main__':
    main(*sys.argv[1:])
