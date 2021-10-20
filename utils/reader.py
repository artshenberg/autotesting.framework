import json
import os


class DataLoader:
    """
    Loading test data from specified file.
    """

    @staticmethod
    def open_file(filename):
        """
        Deserialize test data fom .json file.
        :param filename: file. Format is like "/dir/some.json"
        :return: dict.
        """
        file_path = os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), '..' + filename))
        with open(file_path, 'r', encoding='utf-8') as test_data_file:
            test_data = json.load(test_data_file)
        return test_data
