# coding: utf-8
import pandas as pd
import json
from pandas.io.json import json_normalize

with open('data/world_bank_projects.json') as f:
    load = json.load(f)
    
df = pd.DataFrame(load)

top_ten_countries = df.countryname.value_counts().head(10)

projects = json_normalize(load, 'mjsector_namecode')
top_ten_projects = projects.name.value_counts().head(10)

# I do not actually see any null values...
project_to_code_map = projects.drop_duplicates() # does not show nulls
