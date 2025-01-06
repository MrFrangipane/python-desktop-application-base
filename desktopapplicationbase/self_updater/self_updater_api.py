import sys
import subprocess

from pyside6helpers import icons, hourglass

from desktopapplicationbase.actions import actions_api
from desktopapplicationbase.actions.handlers.trigger_simple import TriggerSimpleHandler
from desktopapplicationbase.actions.info import ActionInfo
from desktopapplicationbase.application import application_api
from desktopapplicationbase.configuration import configuration_api


def register_actions():
    actions_api.register(ActionInfo(
        name="&Self update...",
        icon=icons.refresh(),
        menu_path=["&File"],
        show_in_systray=False,
        handler=TriggerSimpleHandler(self_update)
    ))


@hourglass.hourglass_wrapper
def self_update():
    if "--dev" in sys.argv:
        print("Skipping self update because running in dev mode")
        return

    configuration = configuration_api.get()
    application = application_api.get_instance()

    command_items = [sys.executable, "-m", "pip", "install"]
    subprocess.call(command_items + ["--upgrade", "pip"])
    subprocess.call(command_items + [configuration.self_update_package_name])

    subprocess.Popen([sys.executable] + sys.argv)

    application.quit()
    application.processEvents()
