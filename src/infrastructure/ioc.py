from injector import Binder, Module, provider, singleton
from backend.infrastructure.configHelper import ConfigHelper
from mainAction import MainAction

class FrontModule(Module):
    """Class for configure injector module"""
    
    def configure(self, binder: Binder) -> None:
        binder.bind(MainAction)

    
    @singleton
    @provider
    def provide_configuration(self) -> ConfigHelper:
      config = ConfigHelper("Config.json")
      return config