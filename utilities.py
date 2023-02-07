import pandas as pd


def write_to_excel(name, list):

    df = pd.DataFrame(list, columns=["Repository", "Stars"])

    df.to_excel("lists/{} Repositories on GitHub.xlsx".format(name),
                sheet_name='Repositories')
