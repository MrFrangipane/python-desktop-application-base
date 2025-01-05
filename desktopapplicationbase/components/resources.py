import os.path

from pythonhelpers.singleton_path_holder import make_singleton_path_holder


Resources = make_singleton_path_holder(folder_name="resources", start_folder=os.path.dirname(__file__))
