import pandas as pd
import CreateData
import ExportScriptResults


def create_random_xmls(MH, username, password, environ, params_for_asns_file, num_of_asns):
    MH.launch_manh(environ)
    if environ == 'DEVL':
        MH.login(username, password)
    complete_asn_xml, asn_list = CreateData.create_asns(params_for_asns_file, num_of_asns)
    MH.post_message_xml_and_verify(complete_asn_xml)
    MH.logout()
    print('Full Script Pass')
    return asn_list


def main():
    # create Status list and main MH object to call common methods on - don't change
    MH, Status = CreateData.create_MH_object()
    # get username and password to login - can change based on what login you want
    username, password, environ = CreateData.get_login_param('MH')
    params_for_asns_file = pd.read_excel(r'C:\Users\ebu312q\Documents\params_for_asns.xlsx')
    asn_list = []
    num_of_asns = 10

    try:
        # main function for interacting with MH - change based on what funct want to do ///
        asn_list = create_random_xmls(MH, username, password, environ, params_for_asns_file, num_of_asns)
    finally:
        # first setup for exporting script results, get time stamp, directory and screenshot paths - don't change
        time_stamp, directory_path = ExportScriptResults.export_setup()

        # create data dataframe based on what data you want to save and set a unique script results path - can change ///
        data = pd.DataFrame({'ASNs': asn_list})
        script_results_path = directory_path + r'/Create_Random_XMLS Results at ' + time_stamp + '.xlsx'

        # export excel file for script results - don't change
        ExportScriptResults.create_and_export_excel_results(MH, Status, time_stamp, data, script_results_path)

        MH.get_driver().quit()


main()
