import pandas as pd


def write_to_excel(name, list):

    df = pd.DataFrame(list, columns=["Repository", "Stars"])

    df.to_excel("outputs/{} Repositories on GitHub.xlsx".format(name),
                sheet_name='Repositories')
