import environment_variables
import os


class VerbDictionary:
    """
    Stores the Language verb and the corresponding english meaning.

    """
    def __init__(self, verb_dictionary=None):
        """
        Initialize a class instance with a verb dictionary.

        Parameters:
        - verb_dictionary (dict or None): A dictionary of word mappings.
        """
        if verb_dictionary is None:
            verb_dictionary = {}
        self.verb_dictionary = verb_dictionary
    
    def read_from_textfile(self, file_name = None):
        """
        Read from a text file and create a dictionary for word mappings.

        Parameters:
        - file_path (str): The path to the text file.

        Returns:
        - dict: A dictionary where keys are words and values are their occurrence counts.
        """
        if file_name == None:
            file_name = os.environ.get('FILE_NAME')

        try:
            with open(file_name, 'r') as file:
                for line in file:
                    split_line = line.split(maxsplit = 1)
                    self.verb_dictionary[split_line[0]] = split_line[1]
        except FileNotFoundError:
            print("Environment Variable for file not set/incorrect")

    def find_meaning_in_dictionary(self, verb_to_find)-> str :
        """
        Returns the meaning of a verb

        Parameters:
        - verb_to_find (str): The verb whose meaning is required

        Returns:
        - str: A string with the meaning of the verb. 
        """
        if verb_to_find in self.verb_dictionary:
            return self.verb_dictionary[verb_to_find]
        else:
            return "NO MEANING FOUND"




                



