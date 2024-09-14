import os


class FileUtils:

    @staticmethod
    def get_map_file_name_2_path(root_dir):

        map_file_name_2_path = {}

        for root, dirs, files in os.walk(root_dir):
            for name in files:

                path = os.path.join(root, name)
                map_file_name_2_path[name] = path

        return map_file_name_2_path

