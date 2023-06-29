from connection import connect


def main():
    session = connect('RT3')
    session.findById("wnd[0]/tbar[0]/okcd").text = "mm03"
    session.findById("wnd[0]").sendVKey(0)
    session.findById("wnd[0]/usr/ctxtRMMG1-MATNR").text = 'M169500'
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

    # session.findbyid("wnd[0]").close()
    # session.findById("wnd[1]/usr/btnSPOP-OPTION1").press()


main()
