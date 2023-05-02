import pandas as pd
import CreateData
import ExportScriptResults


def update_asn_reference_field_with_trailer(selen_ob, environ, asn_file, file_length, asn_list, trailer_list,
                                            asn_pass_list):
    selen_ob.launch_environ(environ)
    if environ == 'DEVL':
        print('Please manually type in username and password to login within 30 seconds and wait\n')
        selen_ob.wait(30)

    selen_ob.search_menu('ASNs')
    print('Logged in successfully\n')
    selen_ob.type_keys_enter('asns_menu_primary_fields_dropdown_box_1', 'ASN', True)
    selen_ob.change_position_value_of_element('asns_menu_checkbox_button_', '1')

    print('Beginning loop to modify all asns from file\n')
    for i in range(file_length):
        asn = asn_file.values[i][0]
        trailer = asn_file.values[i][1]
        selen_ob.clear_input_box('asns_menu_primary_fields_asn_id_input_box')
        selen_ob.type_keys_enter('asns_menu_primary_fields_asn_id_input_box', asn, True)
        selen_ob.click('uni_apply_button')
        try:
            selen_ob.set_timeout(10)
            selen_ob.click('asns_menu_checkbox_button_1')
        except AttributeError:
            selen_ob.set_timeout(30)
            asn_list.append(asn)
            trailer_list.append(trailer)
            asn_pass_list.append('ASN DOES NOT EXIST')
            print('asn: ' + asn + ' does not exit\n')
            continue

        selen_ob.set_timeout(30)
        selen_ob.click('uni_edit_header_button')
        selen_ob.switch_to_diff_iframe('edit_ASN_menu_iframe')

        # selen_ob.verify_text_of_element('edit_ASN_menu_ASN_name', asn)

        print('Searched for asn: ' + asn + ' successfuly\n')
        selen_ob.clear_input_box('edit_ASN_menu_ref_field_10_input_box')
        selen_ob.type_keys_enter('edit_ASN_menu_ref_field_10_input_box', trailer, False)
        selen_ob.click('edit_ASN_menu_save_button')

        if not selen_ob.verify_text_of_element('edit_ASN_menu_ref_field_10_value', trailer):
            for j in range(10):
                selen_ob.click('advance_ship_notice_menu_edit_header_button')
                selen_ob.clear_input_box('edit_ASN_menu_ref_field_10_input_box')
                selen_ob.type_keys_enter('edit_ASN_menu_ref_field_10_input_box', trailer, False)
                selen_ob.click('edit_ASN_menu_save_button')
                if selen_ob.verify_text_of_element('edit_ASN_menu_ref_field_10_value', trailer):
                    asn_list.append(asn)
                    trailer_list.append(trailer)
                    asn_pass_list.append('TRAILER ADDED SUCCESSFULLY')
                    print('trailer: ' + trailer + ' added successfully to asn: ' + asn + '\n')
                    break
                if i == 10:
                    asn_list.append(asn)
                    trailer_list.append(trailer)
                    asn_pass_list.append('UNABLE TO ADD TRAILER')
                    print('trailer: ' + trailer + ' unable to add to asn: ' + asn + '\n')
        else:
            asn_list.append(asn)
            trailer_list.append(trailer)
            asn_pass_list.append('TRAILER ADDED SUCCESSFULLY')
            print('trailer: ' + trailer + ' added successfully to asn: ' + asn + '\n')

        selen_ob.switch_to_default_iframe()
        selen_ob.close_num_window('2')

    # selen_ob.logout()
    print('All asns have been modified\n')
    return asn_list, trailer_list, asn_pass_list


def main():
    # create Status list and main selen_ob object to call common methods on - don't change
    selen_ob, Status = CreateData.create_selen_object()
    print('Created main selen_ob object for testing\n')
    # get username and password to login - can change based on what login you want
    # username, password, environ = CreateData.get_login_param('MH')

    # create unique data param to pass into main selen_ob funct - can change ///
    environ = 'DEVL'
    print('Set environment to ' + environ + '\n')
    asn_file = pd.read_excel(r'C:\update_asn_reference_field_with_trailer_asns_list.xlsx', dtype=str)
    print('Found and set file to import asns to modify\n')
    file_length = len(asn_file)
    asn_list = []
    trailer_list = []
    asn_pass_list = []
    print('Set pre-parameters\n')

    try:
        # main function for interacting with selen_ob - change based on what funct want to do ///
        print('Beginning main script process\n')
        asn_list, trailer_list, asn_pass_list = update_asn_reference_field_with_trailer(selen_ob, environ, asn_file,
                                                                                        file_length, asn_list,
                                                                                        trailer_list,
                                                                                        asn_pass_list)
    finally:
        # first setup for exporting script results, get time stamp, directory and screenshot paths - don't change
        time_stamp, directory_path = ExportScriptResults.export_setup()

        # create data dataframe based on what data you want to save and
        # set a unique script results path - can change ///
        data = pd.DataFrame({'ASNs': asn_list, 'TRAILER': trailer_list, 'STATUS': asn_pass_list})
        script_results_path = directory_path + r'/Update_ASN_Reference_Field_With_Trailer Script Results at ' + \
                              time_stamp + '.xlsx'

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
