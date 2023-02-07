import time

import api
import selentium
import utilities


class Organization(object):
    def __init__(self, name):
        self.name = name

    def excel_file_api(self):
        start = time.time()
        res = api.get_repo_info(self.name)
        print("Runtime: ", time.time() - start)

    def excel_file_selentium(self):
        start = time.time()
        res = selentium.get_repo_info(self.name)
        utilities.write_to_excel(self.name, res)
        print("Runtime: ", time.time() - start)


microsoft = Organization("microsoft")

powershell = Organization("PowerShell")

powershell.excel_file_selentium()
