import pywintypes

from connection import connect
from time import sleep
import pyautogui
import pytesseract
import os
from PIL import Image
import re
import time
from datetime import date
import pandas as pd


def create_purchase_order(session, part_number, qty, info_list):
    session.findById("wnd[0]").maximize()
    session.findById("wnd[0]/tbar[0]/okcd").text = "me21n"
    session.findById("wnd[0]").sendVKey(0)
    session.findById(
        "wnd[0]/usr/subSUB0:SAPLMEGUI:0013/subSUB0:SAPLMEGUI:0030/subSUB1:SAPLMEGUI:1105/ctxtMEPO_TOPLINE-SUPERFIELD").\
        text = "99999tdy00"
    session.findById(
        "wnd[0]/usr/subSUB0:SAPLMEGUI:0013/subSUB0:SAPLMEGUI:0030/subSUB1:SAPLMEGUI:1105/ctxtMEPO_TOPLINE-SUPERFIELD").\
        setFocus()
    session.findById(
        "wnd[0]/usr/subSUB0:SAPLMEGUI:0013/subSUB0:SAPLMEGUI:0030/subSUB1:SAPLMEGUI:1105/ctxtMEPO_TOPLINE-SUPERFIELD").\
        caretPosition = 10
    session.findById("wnd[0]").sendVKey(0)
    session.findById(
        "wnd[0]/usr/subSUB0:SAPLMEGUI:0013/subSUB1:SAPLMEVIEWS:1100/subSUB2:SAPLMEVIEWS:1200/subSUB1:SAPLMEGUI:1102/"
        "tabsHEADER_DETAIL/tabpTABHDT9/ssubTABSTRIPCONTROL2SUB:SAPLMEGUI:1221/ctxtMEPO1222-EKORG").text = "dy00"
    session.findById(
        "wnd[0]/usr/subSUB0:SAPLMEGUI:0013/subSUB1:SAPLMEVIEWS:1100/subSUB2:SAPLMEVIEWS:1200/subSUB1:SAPLMEGUI:1102/"
        "tabsHEADER_DETAIL/tabpTABHDT9/ssubTABSTRIPCONTROL2SUB:SAPLMEGUI:1221/ctxtMEPO1222-EKORG").setFocus()
    session.findById(
        "wnd[0]/usr/subSUB0:SAPLMEGUI:0013/subSUB1:SAPLMEVIEWS:1100/subSUB2:SAPLMEVIEWS:1200/subSUB1:SAPLMEGUI:1102/"
        "tabsHEADER_DETAIL/tabpTABHDT9/ssubTABSTRIPCONTROL2SUB:SAPLMEGUI:1221/ctxtMEPO1222-EKORG").caretPosition = 4
    session.findById("wnd[0]").sendVKey(0)
    session.findById(
        "wnd[0]/usr/subSUB0:SAPLMEGUI:0013/subSUB1:SAPLMEVIEWS:1100/subSUB2:SAPLMEVIEWS:1200/subSUB1:SAPLMEGUI:1102/"
        "tabsHEADER_DETAIL/tabpTABHDT9/ssubTABSTRIPCONTROL2SUB:SAPLMEGUI:1221/ctxtMEPO1222-EKGRP").text = "d01"
    session.findById(
        "wnd[0]/usr/subSUB0:SAPLMEGUI:0013/subSUB1:SAPLMEVIEWS:1100/subSUB2:SAPLMEVIEWS:1200/subSUB1:SAPLMEGUI:1102/"
        "tabsHEADER_DETAIL/tabpTABHDT9/ssubTABSTRIPCONTROL2SUB:SAPLMEGUI:1221/ctxtMEPO1222-EKGRP").setFocus()
    session.findById(
        "wnd[0]/usr/subSUB0:SAPLMEGUI:0013/subSUB1:SAPLMEVIEWS:1100/subSUB2:SAPLMEVIEWS:1200/subSUB1:SAPLMEGUI:1102/"
        "tabsHEADER_DETAIL/tabpTABHDT9/ssubTABSTRIPCONTROL2SUB:SAPLMEGUI:1221/ctxtMEPO1222-EKGRP").caretPosition = 3
    session.findById("wnd[0]").sendVKey(0)
    session.findById(
        "wnd[0]/usr/subSUB0:SAPLMEGUI:0013/subSUB2:SAPLMEVIEWS:1100/subSUB2:SAPLMEVIEWS:1200/subSUB1:SAPLMEGUI:1211/"
        "tblSAPLMEGUITC_1211/ctxtMEPO1211-EMATN[4,0]").text = part_number
    session.findById(
        "wnd[0]/usr/subSUB0:SAPLMEGUI:0013/subSUB2:SAPLMEVIEWS:1100/subSUB2:SAPLMEVIEWS:1200/subSUB1:SAPLMEGUI:1211/"
        "tblSAPLMEGUITC_1211/ctxtMEPO1211-EMATN[4,0]").setFocus()
    session.findById(
        "wnd[0]/usr/subSUB0:SAPLMEGUI:0013/subSUB2:SAPLMEVIEWS:1100/subSUB2:SAPLMEVIEWS:1200/subSUB1:SAPLMEGUI:1211/"
        "tblSAPLMEGUITC_1211/ctxtMEPO1211-EMATN[4,0]").caretPosition = 8
    session.findById("wnd[0]").sendVKey(0)
    session.findById(
        "wnd[0]/usr/subSUB0:SAPLMEGUI:0010/subSUB2:SAPLMEVIEWS:1100/subSUB2:SAPLMEVIEWS:1200/subSUB1:SAPLMEGUI:1211/"
        "tblSAPLMEGUITC_1211/txtMEPO1211-MENGE[6,0]").text = qty
    session.findById(
        "wnd[0]/usr/subSUB0:SAPLMEGUI:0010/subSUB2:SAPLMEVIEWS:1100/subSUB2:SAPLMEVIEWS:1200/subSUB1:SAPLMEGUI:1211/"
        "tblSAPLMEGUITC_1211/txtMEPO1211-MENGE[6,0]").setFocus()
    session.findById(
        "wnd[0]/usr/subSUB0:SAPLMEGUI:0010/subSUB2:SAPLMEVIEWS:1100/subSUB2:SAPLMEVIEWS:1200/subSUB1:SAPLMEGUI:1211/"
        "tblSAPLMEGUITC_1211/txtMEPO1211-MENGE[6,0]").caretPosition = 17
    session.findById("wnd[0]").sendVKey(0)
    session.findById(
        "wnd[0]/usr/subSUB0:SAPLMEGUI:0010/subSUB2:SAPLMEVIEWS:1100/subSUB2:SAPLMEVIEWS:1200/subSUB1:SAPLMEGUI:1211/"
        "tblSAPLMEGUITC_1211/ctxtMEPO1211-EEIND[9,0]").text = "12.01.2023"
    session.findById(
        "wnd[0]/usr/subSUB0:SAPLMEGUI:0010/subSUB2:SAPLMEVIEWS:1100/subSUB2:SAPLMEVIEWS:1200/subSUB1:SAPLMEGUI:1211/"
        "tblSAPLMEGUITC_1211/ctxtMEPO1211-EEIND[9,0]").setFocus()
    session.findById(
        "wnd[0]/usr/subSUB0:SAPLMEGUI:0010/subSUB2:SAPLMEVIEWS:1100/subSUB2:SAPLMEVIEWS:1200/subSUB1:SAPLMEGUI:1211/"
        "tblSAPLMEGUITC_1211/ctxtMEPO1211-EEIND[9,0]").caretPosition = 10
    session.findById("wnd[0]").sendVKey(0)
    session.findById(
        "wnd[0]/usr/subSUB0:SAPLMEGUI:0010/subSUB2:SAPLMEVIEWS:1100/subSUB2:SAPLMEVIEWS:1200/subSUB1:SAPLMEGUI:1211/"
        "tblSAPLMEGUITC_1211/ctxtMEPO1211-NAME1[15,0]").text = "dy20"
    session.findById(
        "wnd[0]/usr/subSUB0:SAPLMEGUI:0010/subSUB2:SAPLMEVIEWS:1100/subSUB2:SAPLMEVIEWS:1200/subSUB1:SAPLMEGUI:1211/"
        "tblSAPLMEGUITC_1211/ctxtMEPO1211-NAME1[15,0]").setFocus()
    session.findById(
        "wnd[0]/usr/subSUB0:SAPLMEGUI:0010/subSUB2:SAPLMEVIEWS:1100/subSUB2:SAPLMEVIEWS:1200/subSUB1:SAPLMEGUI:1211/"
        "tblSAPLMEGUITC_1211/ctxtMEPO1211-NAME1[15,0]").caretPosition = 4
    session.findById("wnd[0]").sendVKey(0)
    session.findById("wnd[0]/tbar[0]/btn[11]").press()
    session.findById("wnd[1]/usr/btnSPOP-VAROPTION1").press()

    # screenshot_file_path = download_folder + 'po_notification_screenshot.png'
    # pyautogui.screenshot(screenshot_file_path, region=(10, 1013, 400, 25))
    #
    # pytesseract.pytesseract.tesseract_cmd = r'C:\Users\ebu312q\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
    # notification = pytesseract.image_to_string(Image.open(screenshot_file_path), lang='eng', config='--psm 6')
    notification = session.FindById("wnd[0]/sbar").text
    print('Status: ' + notification)

    if 'Standard PO created under the number' in notification:
        po_number = notification.partition('number ')[2]
        # po_number = re.sub("[^0-9]", "", po_number)

    else:
        po_number = 'X' + notification

    session.findById("wnd[0]/tbar[0]/btn[3]").press()

    print('Purchase Order: ' + po_number)
    info_list.append(po_number)
    return po_number


def create_asn(session, po_number, asn, info_list):
    session.findById("wnd[0]").maximize()
    session.findById("wnd[0]/tbar[0]/okcd").text = "vl31n"
    session.findById("wnd[0]").sendVKey(0)
    session.findById("wnd[0]/usr/ctxtLIKP-LIFNR").text = "99999TDY00"
    session.findById("wnd[0]/usr/txtLV50C-BSTNR").text = po_number
    session.findById("wnd[0]/usr/txtRV50A-VERUR_LA").text = asn
    session.findById("wnd[0]/usr/txtRV50A-VERUR_LA").setFocus()
    session.findById("wnd[0]/usr/txtRV50A-VERUR_LA").caretPosition = 12
    session.findById("wnd[0]").sendVKey(0)
    session.findById("wnd[0]/tbar[0]/btn[11]").press()

    # screenshot_file_path = download_folder + 'success_notification_screenshot.png'
    # pyautogui.screenshot(screenshot_file_path, region=(10, 1013, 450, 25))
    #
    # pytesseract.pytesseract.tesseract_cmd = r'C:\Users\ebu312q\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
    # notification = pytesseract.image_to_string(Image.open(screenshot_file_path), lang='eng', config='--psm 6')
    notification = session.FindById("wnd[0]/sbar").text
    print('Status: ' + notification)

    if 'was saved and distributed to the WMS' in notification:
        final_asn = asn

    else:
        final_asn = 'X' + notification

    session.findById("wnd[0]").close()
    session.findById("wnd[1]/usr/btnSPOP-OPTION1").press()

    print('ASN: ' + final_asn)
    info_list.append(final_asn)
    return final_asn


def read_rt3_data(part_number, info_list):
    session = connect('RT3')
    session.findById("wnd[0]/tbar[0]/okcd").text = "mm03"
    session.findById("wnd[0]").sendVKey(0)
    session.findById("wnd[0]/usr/ctxtRMMG1-MATNR").text = part_number
    session.findById("wnd[0]/usr/ctxtRMMG1-MATNR").caretPosition = 6
    session.findById("wnd[0]").sendVKey(0)
    session.findById("wnd[1]/usr/tblSAPLMGMMTC_VIEW").getAbsoluteRow(0).selected = True
    session.findById("wnd[1]/tbar[0]/btn[0]").press()
    session.findById("wnd[0]/tbar[1]/btn[30]").press()
    session.findById("wnd[0]/usr/tabsTABSPR1/tabpZU03").select()

    not_found_qdy_row = True
    row = 0
    while not_found_qdy_row:
        auom = session.findById(
            "wnd[0]/usr/tabsTABSPR1/tabpZU03/ssubTABFRA1:SAPLMGMM:2110/subSUB2:SAPLMGD1:8020/tblSAPLMGD1TC_ME_8020"
            "/ctxtSMEINH-MEINH[1," + str(row) + "]").text
        if auom == 'QDY':
            not_found_qdy_row = False
        else:
            row = row + 1

    row = str(row)

    length = session.findById(
        "wnd[0]/usr/tabsTABSPR1/tabpZU03/ssubTABFRA1:SAPLMGMM:2110/subSUB2:SAPLMGD1:8020/tblSAPLMGD1TC_ME_8020"
        "/txtSMEINH-LAENG[11," + row + "]").text
    width = session.findById(
        "wnd[0]/usr/tabsTABSPR1/tabpZU03/ssubTABFRA1:SAPLMGMM:2110/subSUB2:SAPLMGD1:8020/tblSAPLMGD1TC_ME_8020"
        "/txtSMEINH-BREIT[12," + row + "]").text
    height = session.findById(
        "wnd[0]/usr/tabsTABSPR1/tabpZU03/ssubTABFRA1:SAPLMGMM:2110/subSUB2:SAPLMGD1:8020/tblSAPLMGD1TC_ME_8020"
        "/txtSMEINH-HOEHE[13," + row + "]").text

    print(length)
    print(width)
    print(height)

    info_list.append(length)
    info_list.append(width)
    info_list.append(height)

    session.findbyid("wnd[0]").close()
    session.findById("wnd[1]/usr/btnSPOP-OPTION1").press()


def main():
    environ = 'QRT'
    download_folder = os.path.expanduser("~") + "/Downloads/"
    results_file_path = download_folder + 'created_asns.xlsx'
    main_df = pd.read_excel(results_file_path, sheet_name='Sheet1', dtype=str)

    length = len(main_df.index)
    temp_df = main_df.loc[main_df.isna().any(axis=1)].head(1)
    row_to_start_index = temp_df.index[0]

    is_po_cell_filled = not (pd.isna(temp_df['Purchase Order'].iloc[0]))
    is_asn_cell_empty = pd.isna(temp_df['ASN'].iloc[0])
    is_asn_col_blank = is_po_cell_filled and is_asn_cell_empty

    results_df = pd.DataFrame(columns=['Purchase Order', 'ASN'])

    session = connect(environ)

    try:
        num = 0
        for row in range(row_to_start_index, length):
            if not (is_asn_col_blank is True and num == 0):
                part_number = str(main_df['Part Number'].iloc[row])
                qty = str(main_df['Qty'].iloc[row])
                results_info_list = []

                po_number = create_purchase_order(session, part_number, qty, results_info_list)

                if po_number != 'X':
                    date_stamp = str(date.today().strftime("%m%d%Y"))
                    time_stamp = str(time.strftime("%H%M%S", time.localtime()))
                    asn = 'TESTASN' + date_stamp + time_stamp

                    final_asn = create_asn(session, po_number, asn, results_info_list)
                    if final_asn != 'X':
                        print('Successfully created Purchase Order: ' + po_number + ' and ASN: ' + final_asn)
                    else:
                        print('Purchase order was created, but could not create asn')

                else:
                    print('Purchase Order could not be created, cannot create asn')
                    results_info_list.append('X')

                results_df.loc[len(results_df.index)] = results_info_list

            else:
                po_number = str(main_df['Purchase Order'].iloc[row])
                print('Purchase Order: ' + po_number)
                results_info_list = [po_number]

                if po_number != 'X':
                    date_stamp = str(date.today().strftime("%m%d%Y"))
                    time_stamp = str(time.strftime("%H%M%S", time.localtime()))
                    asn = 'TESTASN' + date_stamp + time_stamp

                    final_asn = create_asn(session, po_number, asn, results_info_list)
                    if final_asn != 'X':
                        print('Successfully created Purchase Order: ' + po_number + ' and ASN: ' + final_asn)
                    else:
                        print('Purchase order was created, but could not create asn')

                else:
                    print('Purchase Order could not be created, cannot create asn')
                    results_info_list.append('X')

                results_df.loc[len(results_df.index)] = results_info_list

    finally:
        with pd.ExcelWriter(results_file_path, mode="a", engine="openpyxl",
                            if_sheet_exists="overlay") as writer:
            results_df.style.set_properties(
                **{'background-color': '#BDD7EE', 'color': 'black', 'border': '1.3px solid black'}).to_excel \
                (writer, sheet_name="Sheet1", header=False, startrow=row_to_start_index + 1, startcol=2,
                 index=False)


main()
