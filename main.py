import data_entry
import image_extraction


def read_page():
    """
    A function that reads an individual sheet of data on a pdf page.

    :return:
    """
    image_extraction.detection  # detects boxes on the image and returns a dictionary
    image_extraction.extraction # extracts boxes on the image and returns a dictionary of the same size


def enter():
    """
    A function that enters a student's dictionary data from their score sheet.

    :return:
    """
    data_entry.init # finds all the boxes
    data_entry.enter # enters the student data and returns errors


# WRAPPER METHODS


def read(filename):
    """
    A function that reads the data from a pdf file and converts it into a pandas dataframe.

    :param filename:
    :return:
    """
    for page in pdf:
        df.append(read_page(page))