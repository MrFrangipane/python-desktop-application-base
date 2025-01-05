from desktopapplicationbase.components import Components
from desktopapplicationbase.configuration.configuration import Configuration


def set_(configuration: Configuration):
    Components().configuration = configuration


def get() -> Configuration:
    return Components().configuration
