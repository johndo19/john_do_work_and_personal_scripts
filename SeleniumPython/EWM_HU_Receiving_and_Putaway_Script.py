import os
import threading
import pandas as pd
import win32clipboard
import CreateData
import ExportScriptResults
import pyautogui
import os.path


def manage_os_popup():
    # time.sleep(3)
    for i in range(10):
        pyautogui.press('enter')
    # pyautogui.moveTo(1100, 325, duration=0.5)
    # time.sleep(1)
    # pyautogui.click()


def launch_rfui(selen_ob, environ, num, resource):
    if num == 0:
        my_thread = threading.Thread(target=manage_os_popup)
        my_thread.start()

    selen_ob.launch_environ(environ)
    print('launched environ')

    # Change depending on if wd3 or qwd
    # wd3 start with pressing start
    # qwd start with clicking and entering in resource input box

    selen_ob.clear_input_box('ewm_rf_menu_resource_input_box')
    selen_ob.type_keys_enter('ewm_rf_menu_resource_input_box', 'EBU312Q', True)
    selen_ob.wait(1)
    selen_ob.click_and_enter('ewm_rf_menu_resource_input_box')
    # selen_ob.click('ewm_rf_menu_start_button')
    selen_ob.click('ewm_rf_menu_inbound_process_button')
    selen_ob.wait(2)
    selen_ob.change_window_size(100, 1000)
    selen_ob.wait(7)


def hu_receiving(selen_ob, asn, part_number, qty, pack_mat, post_info_list):
    selen_ob.click('ewm_rf_menu_receiving_of_hus_button')
    selen_ob.click('ewm_rf_menu_rec_hu_by_asn_button')

    qty_type = 'PC'

    selen_ob.clear_input_box('ewm_rf_menu_enter_asn_input_box')
    selen_ob.type_keys_enter('ewm_rf_menu_enter_asn_input_box', asn, True)
    selen_ob.click('ewm_rf_menu_next_button')
    selen_ob.click('ewm_rf_menu_create_button')
    selen_ob.type_keys_enter('ewm_rf_menu_product_input_box', part_number, False)
    selen_ob.type_keys_enter('ewm_rf_menu_actual_qty_input_box', qty, False)
    selen_ob.type_keys_enter('ewm_rf_menu_actual_qty_type_input_box', qty_type, False)
    selen_ob.click('ewm_rf_menu_pack_button')
    selen_ob.type_keys_enter('ewm_rf_menu_packaging_material_input_box', pack_mat, False)
    selen_ob.click('ewm_rf_menu_pack_button')
    selen_ob.click('ewm_rf_menu_next_button')

    hu = selen_ob.store_attribute_of_element('ewm_rf_menu_hu_info_field', 'value')
    print('HU: ' + hu)
    post_info_list.append(hu)

    # selen_ob.click('ewm_rf_menu_unload_button')
    selen_ob.click('ewm_rf_menu_post_gr_button')
    selen_ob.click('ewm_rf_menu_create_button')
    selen_ob.wait(3)
    selen_ob.click('ewm_rf_menu_confirm_button')

    selen_ob.click('ewm_rf_menu_back_button')
    selen_ob.click('ewm_rf_menu_back_button')
    selen_ob.click('ewm_rf_menu_back_button')

    selen_ob.click('ewm_rf_menu_back_button')
    selen_ob.click('ewm_rf_menu_back_button')

    return hu


def hu_putaway(selen_ob, hu):
    selen_ob.click('ewm_rf_menu_putaway_button')

    for j in range(2):
        selen_ob.click('ewm_rf_menu_putaway_by_hu_clust_button')
        selen_ob.type_keys_enter('ewm_rf_menu_putaway_hu_input_box', hu, True)
        selen_ob.wait(1)
        selen_ob.click('ewm_rf_menu_next_button')
        selen_ob.wait(1)
        dest_stor_bin = selen_ob.store_attribute_of_element('ewm_rf_menu_destination_storage_bin_field', 'value')
        if j == 0:
            selen_ob.type_keys_enter('ewm_rf_menu_destination_storage_bin_input_box', dest_stor_bin, False)
            selen_ob.wait(2)
            selen_ob.type_keys_enter('ewm_rf_menu_destination_hu_input_box', hu, True)
        else:
            selen_ob.type_keys_enter('ewm_rf_menu_destination_storage_bin_input_box', dest_stor_bin, True)
            selen_ob.wait(2)

    selen_ob.click('ewm_rf_menu_back_button')


def enter_trans_code(selen_ob, code):
    selen_ob.type_keys_enter('ewm_menu_transaction_code_input_box', code, True)


def grab_prelim_info(selen_ob, part_number, pre_info_list):
    enter_trans_code(selen_ob, '/n/scwm/binmat')
    selen_ob.type_keys_enter('ewm_binmat_menu_warehouse_no_input_box', 'D200', True)
    selen_ob.type_keys_enter('ewm_binmat_menu_product_input_box', part_number, True)
    selen_ob.click('ewm_menu_execute_button')

    fixed_bin = selen_ob.store_field_from_ewm_table('0', '2')
    print('Fixed bin: ' + fixed_bin)
    pre_info_list.append(fixed_bin)

    fix_bin_stor_type = selen_ob.store_field_from_ewm_table('0', '3')
    print('Fixed bin storage type: ' + fix_bin_stor_type)
    pre_info_list.append(fix_bin_stor_type)

    enter_trans_code(selen_ob, '/n/scwm/mon')
    selen_ob.type_keys_enter('ewm_mon_menu_warehouse_no_input_box', 'D200', False)
    selen_ob.type_keys_enter('ewm_mon_menu_monitor_input_box', 'SAP', False)
    selen_ob.click('ewm_menu_execute_button')

    selen_ob.wait(1)
    selen_ob.click('ewm_mon_menu_collapse_all_button')
    selen_ob.wait(2)
    selen_ob.choose_node('5')
    selen_ob.choose_folder_option('ewm_mon_menu_storage_bin_folder_option_', '1')
    selen_ob.wait(1)
    selen_ob.type_keys_enter('ewm_mon_menu_storage_bin_input_box', fixed_bin, True)
    selen_ob.wait(1)
    selen_ob.click('ewm_menu_execute_button')

    fix_bin_stor_sect = selen_ob.store_field_from_ewm_table('0', '2')
    print('Fixed bin storage section: ' + fix_bin_stor_sect)
    pre_info_list.append(fix_bin_stor_sect)

    selen_ob.click_field_from_ewm_table('0', '0')

    # fix_bin_cap_vol = selen_ob.store_attribute_of_element('ewm_storage_bin_sub_menu_max_vol_input_box', 'value')
    # print('Fixed bin capacity volume: ' + fix_bin_cap_vol)
    # pre_info_list.append(fix_bin_cap_vol)

    fix_bin_cap_used_vol = selen_ob.store_attribute_of_element('ewm_storage_bin_sub_menu_load_vol_input_box', 'value')
    print('Fixed bin capacity used volume: ' + fix_bin_cap_used_vol)
    pre_info_list.append(fix_bin_cap_used_vol)

    fix_bin_cap_wgt = selen_ob.store_attribute_of_element('ewm_storage_bin_sub_menu_max_weight_input_box', 'value')
    print('Fixed bin capacity weight: ' + fix_bin_cap_wgt)
    pre_info_list.append(fix_bin_cap_wgt)

    fix_bin_cap_used_wgt = selen_ob.store_attribute_of_element('ewm_storage_bin_sub_menu_weight_used_input_box',
                                                               'value')
    print('Fixed bin capacity used weight: ' + fix_bin_cap_used_wgt)
    pre_info_list.append(fix_bin_cap_used_wgt)

    selen_ob.click('ewm_storage_bin_sub_menu_stock_sect_button')

    fix_bin_inv_qty = selen_ob.store_field_from_ewm_table('0', '9')
    print('Fixed bin inventory quantity: ' + fix_bin_inv_qty)
    pre_info_list.insert(3, fix_bin_inv_qty)

    selen_ob.click('ewm_menu_back_button')
    selen_ob.choose_folder_option('ewm_mon_menu_physical_stock_folder_option_', '1')
    selen_ob.wait(1)
    selen_ob.type_keys_enter('ewm_mon_menu_product_input_box', part_number, True)
    selen_ob.wait(1)
    selen_ob.click('ewm_menu_execute_button')
    selen_ob.wait(1)

    file_path_1 = download_spreadsheet(selen_ob)
    find_bins_from_excel_file(file_path_1, pre_info_list)

    # ///////////////////////////////////////////////////////

    selen_ob.click('ewm_mon_menu_collapse_all_button')
    selen_ob.wait(4)
    selen_ob.choose_node('7')
    selen_ob.wait(1)
    selen_ob.choose_folder_option('ewm_mon_menu_warehouse_attribute_folder_option_', '1')
    selen_ob.wait(1)
    selen_ob.type_keys_enter('ewm_mon_menu_product_input_box', part_number, True)
    selen_ob.wait(1)
    selen_ob.click('ewm_menu_execute_button')
    selen_ob.wait(2)
    selen_ob.click_field_from_ewm_table('0', '0')
    selen_ob.click('ewm_warehouse_prod_maint_sub_menu_st_type_data_field')

    fix_bin_cap_vol = selen_ob.store_attribute_of_element('ewm_warehouse_prod_maint_sub_menu_max_qty_input_box', 'value')
    print('Fixed bin capacity volume: ' + fix_bin_cap_vol)
    pre_info_list.append(fix_bin_cap_vol)

    # ///////////////////////////////////////////////////////

    enter_trans_code(selen_ob, '/n/scwm/packspec')
    selen_ob.click('ewm_packspec_sub_menu_options_arrow_2')
    selen_ob.click('ewm_packspec_sub_menu_product_option_text')
    selen_ob.type_keys_enter('ewm_packspec_sub_menu_product_input_box', part_number, True)
    selen_ob.click('ewm_packspec_sub_menu_perform_search_button')

    file_path_2 = download_spreadsheet(selen_ob)
    last_index = find_last_index_from_excel_file(file_path_2)

    selen_ob.double_click_field_from_ewm_table(last_index, '0')
    selen_ob.click('ewm_menu_continue_button')
    selen_ob.click('ewm_packspec_sub_menu_packaging_material_option_2')

    standard_qty = selen_ob.store_attribute_of_element('ewm_packspec_sub_menu_target_qty_input_box', 'value')
    print('Standard qty: ' + standard_qty)
    pre_info_list.append(standard_qty)

    pack_material = selen_ob.store_attribute_of_element('ewm_packspec_sub_menu_pack_mat_input_box', 'value')
    print('Packaging material: ' + pack_material)
    pre_info_list.append(pack_material)


def after_receiving(selen_ob, asn, post_info_list):
    enter_trans_code(selen_ob, '/n/scwm/mon')
    selen_ob.type_keys_enter('ewm_mon_menu_warehouse_no_input_box', 'D200', False)
    selen_ob.type_keys_enter('ewm_mon_menu_monitor_input_box', 'SAP', False)
    selen_ob.click('ewm_menu_execute_button')
    selen_ob.click('ewm_mon_menu_collapse_all_button')
    selen_ob.wait(2)
    selen_ob.choose_node('2')
    selen_ob.wait(1)
    selen_ob.click('ewm_mon_menu_expand_node_2')
    selen_ob.wait(1)
    selen_ob.click('ewm_mon_menu_expand_node_2')
    selen_ob.wait(1)
    selen_ob.choose_folder_option('ewm_mon_menu_warehouse_task_folder_option_', '1')
    selen_ob.type_keys_enter('ewm_mon_menu_asn_input_box', asn, True)
    selen_ob.click('ewm_menu_execute_button')

    file_path_3 = download_spreadsheet(selen_ob)
    warehouse_task = find_warehouse_task_from_excel_file(file_path_3, post_info_list)

    selen_ob.double_click('ewm_mon_menu_warehouse_task_folder_option_1')
    selen_ob.type_keys_enter('ewm_mon_menu_warehouse_task_input_box', warehouse_task, True)
    selen_ob.click('ewm_menu_execute_button')
    selen_ob.click('ewm_mon_menu_more_methods_button')
    selen_ob.wait(1)
    selen_ob.press_down(2)
    selen_ob.press_enter()
    selen_ob.wait(2)
    selen_ob.click('ewm_mon_menu_export_button')
    selen_ob.wait(1)
    selen_ob.press_down(2)
    selen_ob.press_enter()
    selen_ob.wait(2)
    selen_ob.press_down(4)
    selen_ob.click('ewm_menu_continue_button')
    selen_ob.wait(3)
    selen_ob.click('ewm_menu_allow_button')
    selen_ob.click('ewm_menu_close_button')

    win32clipboard.OpenClipboard()
    wt_log = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    # print('WT Log: ' + wt_log)
    post_info_list.insert(2, wt_log)


def download_spreadsheet(selen_ob):
    selen_ob.click('ewm_mon_menu_export_button')
    selen_ob.wait(1)
    selen_ob.press_down(1)
    selen_ob.press_enter()
    selen_ob.wait(1)
    selen_ob.click('ewm_menu_continue_button')
    selen_ob.wait(1)
    selen_ob.clear_input_box('ewm_mon_menu_export_input_box')
    date_stamp, time_stamp = CreateData.get_date_and_time()
    file_name = date_stamp + '_' + time_stamp + '.xlsx'
    selen_ob.type_keys_enter('ewm_mon_menu_export_input_box', file_name, False)
    selen_ob.click('ewm_menu_download_button')

    download_folder = os.path.expanduser("~") + "/Downloads/"
    file_path = download_folder + file_name
    selen_ob.wait(8)

    return file_path


def find_bins_from_excel_file(file_path, pre_info_list):
    df = pd.read_excel(file_path, dtype=str)
    print('Found and set file to read\n')

    df = df.drop_duplicates(subset=['Storage Bin'])

    rk1_count = str(df['Storage Type'].str.contains('RK1', regex=False).sum())
    if rk1_count == '1':
        print('Verified 1 fixed bin')
    else:
        print('There is more than 1 fixed bin')
    print('RK1 count: ' + rk1_count)

    rk5_count = str(df['Storage Type'].str.contains('RK5', regex=False).sum())
    print('RK5 count: ' + rk5_count)
    pre_info_list.append(rk5_count)

    rk9_count = str(df['Storage Type'].str.contains('RK9', regex=False).sum())
    print('RK9 count: ' + rk9_count)
    pre_info_list.append(rk9_count)

    fl5_count = str(df['Storage Type'].str.contains('FL5', regex=False).sum())
    print('FL5 count: ' + fl5_count)

    fl7_count = str(df['Storage Type'].str.contains('FL7', regex=False).sum())
    print('FL7 count: ' + fl7_count)

    fl5_and_7_count = str(int(fl5_count) + int(fl7_count))
    print('FL5 and FL7 count: ' + fl5_and_7_count)
    pre_info_list.append(fl5_and_7_count)
    os.remove(file_path)


def find_last_index_from_excel_file(file_path):
    df = pd.read_excel(file_path, dtype=str)
    print('Found and set file to read\n')

    last_index = str(len(df.index) - 1)

    os.remove(file_path)
    return last_index


def find_warehouse_task_from_excel_file(file_path, post_info_list):
    df = pd.read_excel(file_path, dtype=str)
    print('Found and set file to read\n')

    df = df.loc[df['Whse Process Type'] == 'P111']

    warehouse_task = str(df['Warehouse Task'].iloc[-1])
    print('Warehouse task: ' + warehouse_task)
    post_info_list.append(warehouse_task)

    dest_bin = str(df['Destination Bin'].iloc[-1])
    print('Desination bin: ' + dest_bin)
    post_info_list.append(dest_bin)

    dest_stor_type = str(df['Dest. Storage Type'].iloc[-1])
    print('Destination storage type: ' + dest_stor_type)
    post_info_list.append(dest_stor_type)

    dest_stor_sect = str(df['Dest. Stor. Section'].iloc[-1])
    print('Destination storage section: ' + dest_stor_sect)
    post_info_list.append(dest_stor_sect)

    os.remove(file_path)
    return warehouse_task


def main():
    # create Status list and main selen_ob object to call common methods on - don't change
    selen_ob, Status = CreateData.create_selen_object()
    print('Created main selen_ob object for testing\n')

    # create unique data param to pass into main selen_ob funct - can change ///
    environ = 'EWM_qwd'
    environ_rf = 'EWM_qwd_rfui'
    resource = 'EBU312Q'

    download_folder = os.path.expanduser("~") + "/Downloads/"
    ewm_file_path = download_folder + 'AutoTestingFields.xlsx'
    main_df = pd.read_excel(ewm_file_path, dtype=str)

    length = len(main_df.index)
    temp_df = main_df.loc[main_df.isna().any(axis=1)].head(1)
    row_to_start_index = temp_df.index[0]

    is_hu_cell_empty = pd.isna(temp_df['HU NUMBER'].iloc[0])
    is_stad_pack_mat_cell_filled = not (pd.isna(temp_df['STANDARD PACK MAT'].iloc[0]))
    is_receiving_row_blank = is_hu_cell_empty and is_stad_pack_mat_cell_filled

    pre_info_df = pd.DataFrame(columns=['FIXED BIN', 'FIXED BIN STOR TYPE', 'FIXED BIN STOR SECT', 'FIXED BIN INV (QTY)'
        , 'FIXED BIN CAP(VOL)', 'FIXED BIN CAP USED(VOL)', 'FIXED BIN CAP(WGT)',
                                        'FIXED BIN CAP USED(WGT)', '# OF RACK RESERVE BINS (xRK5)',
                                        '# OF RACK OVRFL RESERVE BINS (xRK9)', '# OF BULK RSV BINS (xFL5/7)',
                                        'STANDARD QTY (PACKSPEC)', 'STANDARD PACK MAT'])

    post_info_df = pd.DataFrame(columns=['HU NUMBER', 'WHSE TASK', 'WT LOG', 'DEST BIN', 'DEST BIN STORAGE TYPE',
                                         'DEST BIN STOR SECT'])

    print('Set pre-parameters\n')

    try:
        # main function for interacting with selen_ob - change based on what funct want to do ///
        print('Beginning main script process\n')
        num = 0
        for row in range(row_to_start_index, length):
            if not (is_receiving_row_blank is True and num == 0):
                # do both pre info gathering and receiving/post info
                asn = str(main_df['ASN'].iloc[row])
                part_number = str(main_df['PART NUMBER'].iloc[row])
                qty = str(main_df['QTY (PCS)'].iloc[row])
                pack_mat = str(main_df['PACK MATERIAL'].iloc[row])

                pre_info_list = []
                post_info_list = []

                selen_ob.launch_environ(environ)
                grab_prelim_info(selen_ob, part_number, pre_info_list)
                pre_info_df.loc[len(pre_info_df.index)] = pre_info_list

                launch_rfui(selen_ob, environ_rf, num, resource)
                num = num + 1
                hu = hu_receiving(selen_ob, asn, part_number, qty, pack_mat, post_info_list)
                hu_putaway(selen_ob, hu)

                selen_ob.click('ewm_rf_menu_exit_button')
                selen_ob.click('ewm_rf_menu_save_button')
                selen_ob.wait(2)
                selen_ob.change_window_size(1800, 1000)

                selen_ob.launch_environ(environ)
                after_receiving(selen_ob, asn, post_info_list)
                post_info_df.loc[len(post_info_df.index)] = post_info_list
                print('Finished line: ' + str(num) + ', index ' + str(row) + ' in excel file')
            else:
                # just do receiving/post info
                asn = str(main_df['ASN'].iloc[row])
                part_number = str(main_df['PART NUMBER'].iloc[row])
                qty = str(main_df['QTY (PCS)'].iloc[row])
                pack_mat = str(main_df['PACK MATERIAL'].iloc[row])

                post_info_list = []

                launch_rfui(selen_ob, environ_rf, num, resource)
                num = num + 1
                hu = hu_receiving(selen_ob, asn, part_number, qty, pack_mat, post_info_list)
                hu_putaway(selen_ob, hu)

                selen_ob.click('ewm_rf_menu_exit_button')
                selen_ob.click('ewm_rf_menu_save_button')
                selen_ob.wait(2)
                selen_ob.change_window_size(1800, 1000)

                selen_ob.launch_environ(environ)
                after_receiving(selen_ob, asn, post_info_list)
                post_info_df.loc[len(post_info_df.index)] = post_info_list
                print('Finished line: ' + str(num) + ', index ' + str(row) + ' in excel file')

    finally:
        # first setup for exporting script results, get time stamp, directory and screenshot paths - don't change
        time_stamp, directory_path = ExportScriptResults.export_setup()

        # create data dataframe based on what data you want to save and set a unique script results path - can change
        # ///
        # data = pd.DataFrame({'HUs': hu_list, 'PREV LOC': previous_loc_list, 'CURRENT LOC': current_loc_list})
        script_results_path = directory_path + r'/EWM_HU_Receiving_and_Putaway_Script Results at ' + time_stamp + '.xlsx'

        # export excel file for script results - don't change
        ExportScriptResults.create_and_export_excel_results(selen_ob, Status, time_stamp, main_df, script_results_path)

        with pd.ExcelWriter(ewm_file_path, mode="a", engine="openpyxl", if_sheet_exists="overlay") as writer:
            pre_info_df.style.set_properties(**{'background-color': '#FFFF00', 'color': 'black'}).to_excel \
                (writer, sheet_name="Sheet1", header=False, startrow=row_to_start_index + 1, startcol=4, index=False)

        with pd.ExcelWriter(ewm_file_path, mode="a", engine="openpyxl", if_sheet_exists="overlay") as writer:
            post_info_df.style.set_properties(**{'background-color': '#00B0F0', 'color': 'black'}).to_excel \
                (writer, sheet_name="Sheet1", header=False, startrow=row_to_start_index + 1, startcol=17, index=False)

        os.system(ewm_file_path)

        # selen_ob.get_driver().quit()
        # print('Closed automated browser window\n')
        print('SCRIPT HAS FINISHED RUNNING\n')
        print('Exported results in excel file, please check in the Scripts Results folder in your C drive\n')
        print('Make sure to close the console window before running script again')


main()
