import json
import os.path

from desktopapplicationbase.components.components import Components
from desktopapplicationbase.domain_contract.project_persistence import AbstractProjectPersistence


class ProjectPersistence(AbstractProjectPersistence):

    def reset(self):
        pass

    def open(self, filepath):
        pass

    def save(self, filepath):
        data = {
            "file_version": 1
        }
        with open(filepath, "w") as file:
            json.dump(data, file, indent=4)
