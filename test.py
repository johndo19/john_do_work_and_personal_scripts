from connection import connect


def main():
    session = connect('QRT')
    session.findById("wnd[0]/tbar[0]/okcd").text = "mm03"
    session.findById("wnd[0]").sendVKey(0)
    session.findById("wnd[0]/usr/ctxtRMMG1-MATNR").text = "T19044"
    session.findById("wnd[0]/usr/ctxtRMMG1-MATNR").caretPosition = 6
    session.findById("wnd[0]").sendVKey(0)
    session.findById("wnd[1]/usr/tblSAPLMGMMTC_VIEW").getAbsoluteRow(0).selected = True
    session.findById("wnd[1]/tbar[0]/btn[0]").press()
    session.findById("wnd[0]/tbar[1]/btn[30]").press()
    session.findById("wnd[0]/usr/tabsTABSPR1/tabpZU03").select()

    demoniator = session.findById(
        "wnd[0]/usr/tabsTABSPR1/tabpZU03/ssubTABFRA1:SAPLMGMM:2110/subSUB2:SAPLMGD1:8020/tblSAPLMGD1TC_ME_8020"
        "/txtSMEINH-UMREN[0,3]").text
    auom = session.findById(
        "wnd[0]/usr/tabsTABSPR1/tabpZU03/ssubTABFRA1:SAPLMGMM:2110/subSUB2:SAPLMGD1:8020/tblSAPLMGD1TC_ME_8020"
        "/ctxtSMEINH-MEINH[1,3]").text
    measurement_unit = session.findById(
        "wnd[0]/usr/tabsTABSPR1/tabpZU03/ssubTABFRA1:SAPLMGMM:2110/subSUB2:SAPLMGD1:8020/tblSAPLMGD1TC_ME_8020/txt"
        "*T006A-MSEHT[2,3]").text
    blank = session.findById(
        "wnd[0]/usr/tabsTABSPR1/tabpZU03/ssubTABFRA1:SAPLMGMM:2110/subSUB2:SAPLMGD1:8020/tblSAPLMGD1TC_ME_8020"
        "/lblTEXT010003[3,3]").text
    numerator = session.findById(
        "wnd[0]/usr/tabsTABSPR1/tabpZU03/ssubTABFRA1:SAPLMGMM:2110/subSUB2:SAPLMGD1:8020/tblSAPLMGD1TC_ME_8020"
        "/txtSMEINH-UMREZ[4,3]").text
    buom = session.findById(
        "wnd[0]/usr/tabsTABSPR1/tabpZU03/ssubTABFRA1:SAPLMGMM:2110/subSUB2:SAPLMGD1:8020/tblSAPLMGD1TC_ME_8020"
        "/ctxtRM03E-MEINS[5,3]").text
    measurement_unit_type = session.findById(
        "wnd[0]/usr/tabsTABSPR1/tabpZU03/ssubTABFRA1:SAPLMGMM:2110/subSUB2:SAPLMGD1:8020/tblSAPLMGD1TC_ME_8020"
        "/txtRM03E-MSEHT[6,3]").text
    test = session.findById(
        "wnd[0]/usr/tabsTABSPR1/tabpZU03/ssubTABFRA1:SAPLMGMM:2110/subSUB2:SAPLMGD1:8020/tblSAPLMGD1TC_ME_8020"
        "/txtRM03E-MSEHT[6,4]").text

    # session.findbyid("wnd[0]").close()
    # session.findById("wnd[1]/usr/btnSPOP-OPTION1").press()

    print("denominator: " + demoniator)
    print("auom: " + auom)
    print("measurement_unit: " + measurement_unit)
    print("blank: " + blank)
    print("numerator: " + numerator)
    print("buom: " + buom)
    print("measurement_unit_type: " + measurement_unit_type)
    print("test: " + test)


main()
