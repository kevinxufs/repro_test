import pandas as pd

data_path = 'C:/Users/xukev/Desktop/Turing_Work/test_repo/example_data.csv'

df = pd.read_csv(data_path)

df.loc[0, 'world'] = 'mod'

df.to_csv('C:/Users/xukev/Desktop/Turing_Work/test_repo/output_data.csv', index = False)

