import pandas as pd
import numpy as np

# asn_file = pd.read_excel(asn_file_path, dtype=str)
#
# asn_file = pd.read_excel('C:\Users\ebu312q\Downloads\Verifying ASN With No Variance Report for Python Script.xlsx', dtype=str)
# asn_file = pd.read_excel(r'C:\Users\ebu312q\Downloads\Verifying ASN With No Variance Report for Python Script.xlsx', dtype=str)
# asn_file.assign('Variance')
# asn_file.columns
# asn_file.assign('Variance', lambda x:(x['ASN Detail Shipped Quantity']-x['ASN Detail Received Quantity']).abs())
# asn_file.assign(Variance=lambda x:(x['ASN Detail Shipped Quantity']-x['ASN Detail Received Quantity']).abs())
# asn_file.assign(Variance=lambda x:(x['ASN Detail Shipped Quantity'].astype(float)-x['ASN Detail Received Quantity'].astype(float)).abs())
# asn_file.assign(Variance=lambda x:(x['ASN Detail Shipped Quantity'].astype(float)-x['ASN Detail Received Quantity'].astype(float).fillna(0)).abs())
# new_asn = asn_file.assign(Variance=lambda x:(x['ASN Detail Shipped Quantity'].astype(float)-x['ASN Detail Received Quantity'].astype(float).fillna(0)).abs())
# new_asn['Max Variance']=new_asn.groupby(by='ASN ID').max
# new_asn['Max Variance']=new_asn.groupby(by='ASN ID').max()
# new_asn['Max Variance']=new_asn.groupby(by='ASN ID').max().transform()
# new_asn['Max Variance']=new_asn.groupby(by='ASN ID').transform('max')
# new_asn['Max Variance']=new_asn.groupby(by='ASN ID')['Variance'].transform('max')
# asn_confrim=new_asn.query('"Max Variance"==0')
# asn_confrim=new_asn.query('`Max Variance`==0')


def main():
    condition = True

    counter = 0
    while condition:
        for i in range(0, 10):
            print(i)
            counter = counter + 1
            if counter == 5:
                condition = False
                break

main()
