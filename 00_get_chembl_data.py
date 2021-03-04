from chembl_webresource_client.new_client import new_client
import json
import re
from sys import argv
import pandas as pd

accession = 'herg'

def looks_like_number(x):
    try:
        float(x)
        return True
    except:
        return False

def queryChembl(accession=None):
    print('''
        # =========================================================
        # 1. Use UniProt accession to get target details
        # =========================================================
    ''')

    target = new_client.target
    activity = new_client.activity
    herg = target.search(accession)[0]
    herg_activities = activity.filter(target_chembl_id=herg['target_chembl_id']).filter(standard_type="Ki")

    res = pd.DataFrame.from_dict(herg_activities)
    output_name = '%s_compound_from_chembl.csv' % accession
    res.to_csv(output_name)

if __name__ == '__main__':
    queryChembl(accession)
