import time

import utilities.api as api
import utilities.excel as ex
import utilities.selenium as selenium


class Organization(object):
    def __init__(self, name):
        self.name = name

    def excel_file_api(self):
        start = time.time()
        res = api.get_repo_info(self.name)
        print("Runtime: ", time.time() - start)

    def excel_file_selentium(self):
        start = time.time()
        res = selenium.get_repo_info(self.name)
        ex.write_to_excel(self.name, res)
        print("Runtime: ", time.time() - start)


microsoft = Organization("microsoft")

powershell = Organization("PowerShell")

powershell.excel_file_selentium()
