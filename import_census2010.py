# Dictionary (database) extracted from 'censuspopdata.xlsx' by 'read_census_excel.py' and example of its use.

import census2010

anchorage_pop = census2010.all_data['AK']['Anchorage']['pop']
census_tracts_alaska = census2010.all_data['AK']['Anchorage']['tracts']

print(f'The 2010 population of Anchorage was {str(anchorage_pop)}.')
print(f'Alaska consists of exactly {str(census_tracts_alaska)} tracts of its census.')
