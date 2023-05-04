import pandas as pd
import CreateData
import ExportScriptResults


def verify_asn_with_no_variance(selen_ob, environ, asn_confirm_array, asn_list, asn_pass_list):
    selen_ob.launch_environ(environ)
    if environ == 'DEVL':
        print('Please manually type in username and password to login within 30 seconds and wait\n')
        # selen_ob.wait(30)

    selen_ob.search_menu('ASNs')
    print('Logged in successfully\n')
    selen_ob.type_keys_enter('asns_menu_primary_fields_dropdown_box_1', 'ASN', True)
    selen_ob.change_position_value_of_element('asns_menu_checkbox_button_', '1', ']')

    print('Beginning loop to modify all asns from file\n')
    for i in range(len(asn_confirm_array)):
        asn = asn_confirm_array[i]
        selen_ob.clear_input_box('asns_menu_primary_fields_asn_id_input_box')
        selen_ob.type_keys_enter('asns_menu_primary_fields_asn_id_input_box', asn, True)
        selen_ob.click('uni_apply_button')

        try:
            selen_ob.set_timeout(5)
            selen_ob.click('asns_menu_checkbox_button_1')
        except AttributeError:
            selen_ob.set_timeout(30)
            asn_list.append(asn)
            asn_pass_list.append('ASN DOES NOT EXIST')
            print('asn: ' + asn + ' does not exit\n')
            continue

        selen_ob.set_timeout(30)
        print('Searched for asn: ' + asn + ' successfuly\n')
        selen_ob.click('uni_more_button')
        selen_ob.click('uni_verify_asn_button')

        try:
            selen_ob.set_timeout(5)
            selen_ob.click('asns_menu_cannot_verify_message')
            asn_list.append(asn)
            asn_pass_list.append('ASN ALREADY VERIFIED')
            print('asn: ' + asn + ' has already been verified\n')
            continue
        except AttributeError:
            selen_ob.set_timeout(30)

        selen_ob.switch_to_diff_iframe('verify_asn_menu_iframe')
        # selen_ob.click('verify_asn_menu_verify_asn_button', False)

        asn_list.append(asn)
        asn_pass_list.append('ASN VERIFIED')

        selen_ob.switch_to_default_iframe()
        selen_ob.close_num_window('2')

    # selen_ob.logout()
    print('All asns have been verified\n')
    return asn_list, asn_pass_list


def main():
    # create Status list and main selen_ob object to call common methods on - don't change
    selen_ob, Status = CreateData.create_selen_object()
    print('Created main selen_ob object for testing\n')
    # get username and password to login - can change based on what login you want
    # username, password, environ = CreateData.get_login_param('MH')

    # create unique data param to pass into main selen_ob funct - can change ///
    environ = 'PROD'
    print('Set environment to ' + environ + '\n')

    # Steps to grab sci report and download as excel file to import to script
    selen_ob.launch_link('https://partssci.deere.com/bi/?pathRef=.public_folders%2FJohn%2BDeere%2BContent%2FReports'
                         '%2FWorkshop%2FJohn%2FVerifying%2BASN%2BWith%2BNo%2BVariance%2BReport%2Bfor%2BPython%2BScript'
                         '&action=run&format=HTML')
    selen_ob.wait(20)
    selen_ob.click('sci_report_menu_refresh_button')
    selen_ob.wait(3)
    selen_ob.click('sci_report_menu_run_button')
    selen_ob.wait(3)
    selen_ob.click('sci_report_menu_run_submenu_button')
    selen_ob.wait(1)
    selen_ob.click('sci_report_menu_run_excel_data_option')
    selen_ob.wait(10)

    asn_file_path = CreateData.find_files('Verifying ASN With No Variance Report for Python Script.xlsx', 'C:/')
    print(asn_file_path)
    print('Successfuly found sci report of asns to download and import to script\n')

    asn_file = pd.read_excel(asn_file_path, dtype=str)
    print('Found and set file to import asns to modify\n')
    new_asn = asn_file.assign(Variance=lambda x: (x['ASN Detail Shipped Quantity'].astype(float) -
                                                  x['ASN Detail Received Quantity'].astype(float).fillna(0)).abs())
    new_asn['Max Variance'] = new_asn.groupby(by='ASN ID')['Variance'].transform('max')
    asn_confirm = new_asn.query('`Max Variance`==0')
    asn_confirm_array = asn_confirm['ASN ID'].unique()

    # print(len(asn_confirm_array))
    # print(asn_confirm_array)
    # print(asn_confirm_array[0])
    # print(asn_confirm_array[1])

    asn_list = []
    asn_pass_list = []
    # asn_confirm_array = []
    print('Set pre-parameters\n')

    try:
        # main function for interacting with selen_ob - change based on what funct want to do ///
        print('Beginning main script process\n')
        asn_list, asn_pass_list = verify_asn_with_no_variance(selen_ob, environ, asn_confirm_array, asn_list,
                                                              asn_pass_list)
    finally:
        # first setup for exporting script results, get time stamp, directory and screenshot paths - don't change
        time_stamp, directory_path = ExportScriptResults.export_setup()

        # create data dataframe based on what data you want to save and set a unique script results path - can change
        # ///
        data = pd.DataFrame({'ASNs': asn_list, 'STATUS': asn_pass_list})
        script_results_path = directory_path + r'/Verify_ASN_With_No_Variance Script Results at ' + time_stamp + '.xlsx'

        # export excel file for script results - don't change
        ExportScriptResults.create_and_export_excel_results(selen_ob, Status, time_stamp, data, script_results_path)
        # selen_ob.get_driver().quit()
        # print('Closed automated browser window\n')
        print('SCRIPT HAS FINISHED RUNNING\n')
        print('Exported results in excel file, please check in the Scripts Results folder in your C drive\n')
        print('If you want to run the script again with new asns, modify the asns.xlsx file with new asns and trailer '
              'numbers and run the script again\n')
        print('Make sure to close the automated browser window and console window before running script again')


main()
