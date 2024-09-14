import os


class FileUtils:

    @staticmethod
    def get_map_file_name_2_path(root_dir, preprocess_key):

        map_file_name_2_path = {}

        for root, dirs, files in os.walk(root_dir):
            for name in files:

                path = os.path.join(root, name)

                processed_name = preprocess_key(name)
                map_file_name_2_path[processed_name] = path

        return map_file_name_2_path

