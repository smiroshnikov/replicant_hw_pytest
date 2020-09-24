import os
import random


class FileUtils:
    @staticmethod
    def pick_a_random_file_from_folder(path_to_folder) -> str:
        """
        Utility that provides a random filepath from folder
        :param path_to_folder: path to json files
        :return: randomly selected json
        """
        fl = []
        for path in os.listdir(path_to_folder):
            full_path = os.path.join(path_to_folder, path)
            if os.path.isfile(full_path):
                fl.append(full_path)
        return random.choice(fl)

    @staticmethod
    def get_absolute_file_path(p):
        import os
        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname, p)
        return filename


if __name__ == '__main__':
    # _PATH_TO_JSON_FOLDER = "fake_json_files"
    _PATH_TO_JSON_FOLDER = "C:\\Users\\Art3m15\\IdeaProjects\\replicant_hw_no_bdd\\fake_json_files"
    # print(os.pardir)
    # print(full_path(_PATH_TO_JSON_FOLDER))
    for _ in range(0, 100):
        print(FileUtils.pick_a_random_file_from_folder(FileUtils.get_absolute_file_path(_PATH_TO_JSON_FOLDER)))
