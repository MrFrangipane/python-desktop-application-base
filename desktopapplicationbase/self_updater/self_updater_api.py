import sys
import subprocess

from pyside6helpers import icons

from desktopapplicationbase.actions import actions_api
from desktopapplicationbase.actions.info import ActionInfo
from desktopapplicationbase.actions.handlers.trigger_simple import TriggerSimpleHandler
from desktopapplicationbase.configuration import configuration_api


def register_actions():
    actions_api.register(ActionInfo(
        name="&Self update...",
        icon=icons.refresh(),
        menu_path=["&File"],
        show_in_systray=False,
        handler=TriggerSimpleHandler(self_update)
    ))


def self_update():
    if "--dev" in sys.argv:
        print("Skipping self update because running in dev mode")
        return

    configuration = configuration_api.get()
    command_items = [sys.executable, "-m", "pip", "install", "--upgrade"]
    subprocess.call(command_items + ["pip"])
    subprocess.call(command_items + [configuration.self_update_package_name])

