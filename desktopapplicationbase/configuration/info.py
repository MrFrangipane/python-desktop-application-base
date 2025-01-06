from dataclasses import dataclass


@dataclass
class ConfigurationInfo:
    brand: str
    name: str
    icon_filepath: str
    status_bar_logo_filepath: str
    has_systray_icon: bool
