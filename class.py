import time

import utilities.api as api
import utilities.excel as ex
import utilities.selenium as selenium


class Organization(object):
    def __init__(self, name, org):
        self.name = name
        self.org = org

    def excel_file_api(self):
        start = time.time()
        res = api.get_repo_info(self.name)
        print("Runtime: ", time.time() - start)

    def excel_file_selenium(self):
        start = time.time()
        res = selenium.get_repo_info(self.name)
        ex.write_to_excel(self.name, res)
        print("Runtime: ", time.time() - start)


# Examples

microsoft = Organization(name="Microsoft", org=True)
powershell = Organization(name="PowerShell", org=True)
caneplayz = Organization(name="CanePlayz", org=False)


caneplayz.excel_file_selenium()
