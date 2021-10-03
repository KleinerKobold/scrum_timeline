import pandas


def read_excel(file_name: str):
    try:
        sprint_data_df = pandas.read_excel('events.xlsx', sheet_name='Sprints')
        data_df = pandas.read_excel('events.xlsx', sheet_name='Data')
        return (data_df, sprint_data_df)
    except ValueError:
        raise("Unable to load excel file")
