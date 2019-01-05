# -*- coding: utf-8 -*-
import os
import sys
Failed = 0
VERSION = "2.8"


SETUP_ITEMS = [
    "version='{0}'"]
INSTALL_ITEMS = [
    "[Version {0}](https://github.com/sepandhaghighi/art/archive/v{0}.zip)",
    "pip install art=={0}",
    "pip3 install art=={0}",
    'easy_install "art=={0}"']
CHANGELOG_ITEMS = [
    "## [{0}]",
    "https://github.com/sepandhaghighi/art/compare/v{0}...HEAD",
    "[{0}]:"]
ART_LIST_ITEMS = ["### Version : {0}"]
FONT_LIST_ITEMS = ['font_list(\\"art {0}\\")',"### Version : {0}"]
PARAMS_ITEMS = ['VERSION = "{0}"']
FILES = {
    "setup.py": SETUP_ITEMS, "INSTALL.md": INSTALL_ITEMS, "CHANGELOG.md": CHANGELOG_ITEMS, "FontList.ipynb": FONT_LIST_ITEMS,"ArtList.ipynb":ART_LIST_ITEMS, os.path.join("art","art.py"): PARAMS_ITEMS}

TEST_NUMBER = len(FILES.keys())


def print_result(failed=False):
    message = "Version tag tests "
    if not failed:
        print("\n" + message + "passed!")
    else:
        print("\n" + message + "failed!")
    print("Passed : " + str(TEST_NUMBER - Failed) + "/" + str(TEST_NUMBER))


if __name__ == "__main__":
    for file_name in FILES.keys():
        try:
            file_content = open(file_name, "r", errors='ignore').read()
            for test_item in FILES[file_name]:
                if file_content.find(test_item.format(VERSION)) == -1:
                    print("Incorrect version tag in " + file_name)
                    Failed += 1
                    break
        except Exception as e:
            print("Error in " + file_name + "\n" + "Message : " + str(e))

    if Failed == 0:
        print_result(False)
        sys.exit(0)
    else:
        print_result(True)
        sys.exit(1)
