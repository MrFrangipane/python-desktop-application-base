from desktopapplicationbase._components import _Components
from desktopapplicationbase.configuration.info import ConfigurationInfo


def set_(configuration: ConfigurationInfo):
    _Components().configuration = configuration


def get() -> ConfigurationInfo:
    return _Components().configuration
