import pandas as pd
from openpyxl import load_workbook
import sys


class ASNxml:

    def __init__(self, part_number, qty):
        self.file_path = r'C:\Users\ebu312q\Documents\created_asns.xlsx'
        self.asn_file = pd.read_excel(self.file_path)
        self.part_number = str(part_number)
        self.qty = str(qty)
        last_asn = str(self.asn_file['Created_ASNS'].iat[-1])
        last_asn_list = last_asn.split('_', 1)
        asn_num = int(last_asn_list[1]) + 1
        self.random_ASN_id = 'SELENTESTASN_' + str(asn_num)
        self.add_new_asn_to_file()

    def add_new_asn_to_file(self):
        wb = load_workbook(self.file_path)
        ws = wb.worksheets[0]  # select first worksheet
        ws.append([self.random_ASN_id])
        wb.save(self.file_path)

    def get_asn_file(self):
        return self.asn_file

    def get_part_number(self):
        return self.part_number

    def get_qty(self):
        return self.qty

    def get_random_ASN_id(self):
        return self.random_ASN_id

    def create_asn_xml(self):
        xml_asn_part = '<ASN><ASNID>' + self.random_ASN_id + '</ASNID><ASNStatus>20</ASNStatus><BusinessUnit>1' \
                          '</BusinessUnit><OriginFacilityAliasID>CMP</OriginFacilityAliasID><DestinationFacilityAliasID>CMP' \
                          '</DestinationFacilityAliasID><ActualShippedDTTM>12/20/2019 00:00:00</ActualShippedDTTM>' \
                          '<DeliveryStart>12/20/2019 00:00:00</DeliveryStart><DeliveryEnd>12/20/2019 00:00:00</DeliveryEnd>' \
                          '<ExternalSysCreationDTTM>12/20/2019 00:00:00</ExternalSysCreationDTTM><OriginType>P</OriginType>' \
                          '<DestinationType>W</DestinationType><IsCancelled>0</IsCancelled><ASNDetail><PurchaseOrderID>' \
                          'DemoPO001</PurchaseOrderID><PurchaseOrderLineItemID>2</PurchaseOrderLineItemID><ItemName>' \
                          + self.part_number + '</ItemName><Quantity><ShippedQty>' + self.qty + '</ShippedQty><QtyUOM>' \
                          'Unit</QtyUOM></Quantity></ASNDetail></ASN>'\

        return xml_asn_part
