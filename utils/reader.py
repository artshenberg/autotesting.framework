import json
import os


class DataLoader:
    """
    Loading test data from specified file.
    """
    @staticmethod
    def get_filepath(project_directory_name):
        current_directory = os.getcwd().split('/')
        project_name_dictionary = current_directory.index(project_directory_name)
        current_directory = current_directory[:project_name_dictionary + 1]
        return '/'.join(current_directory)

    @staticmethod
    def open_file(project_directory_name, filename):
        """
        Deserialize test data fom .json file.
        :param filename: file. Format is like "/dir/some.json"
        :return: dict.
        """
        file_path = os.path.abspath(os.path.join(DataLoader.get_filepath(project_directory_name), filename))
        with open(file_path, 'r', encoding='utf-8') as test_data_file:
            test_data = json.load(test_data_file)
        return test_data
