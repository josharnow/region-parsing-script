import json
import os
from pathlib import Path


filepath = os.getcwd()
def AppendFile(file_name, data_input=None):
    temp_path = filepath + file_name
    with open(file_name, 'a') as f:
        f.write(f"\n{data_input}")
    print('Execution completed.')

file = open('input.json')
data = json.load(file)

states_by_country_dict = {}
for country in data:
    if country.get('filename'):
        path = Path(f"countries/{country['filename']}.json")
        if path.is_file():
            country_code = country['code']
            states_by_country_dict[f"{country_code}"] = f'{country_code}_STATES'
            region_data = json.load(open(path))
            tup_arr = []
            for region in region_data:
                region_code = region['code'][3:]
                name = region['name']
                tup = (region_code, name)
                tup_arr.append(tup)
            
            data_to_write = f'''\
{country_code}_STATES = [State(abbr, name) for abbr, name in 
    {tuple(tup_arr)}
]
{country_code}_STATES_DICT = CapsDict({{state.abbr: state.name for state in {country_code}_STATES}})
{country_code}_STATES_BY_NAME_DICT = {{state.name.upper(): state for state in {country_code}_STATES}}
'''

            print(data_to_write)
            AppendFile("output.py", data_to_write)

states_by_country = f'''\
STATES_BY_COUNTRY = CapsDict(
    {states_by_country_dict}
)
'''
AppendFile("output.py", states_by_country)
            