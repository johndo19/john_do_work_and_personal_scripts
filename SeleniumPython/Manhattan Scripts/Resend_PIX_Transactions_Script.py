import os
import pandas as pd
import CreateData
import ExportScriptResults


def resend_pix_transactions(selen_ob, environ, df, row_to_start_index, length, status_df):
    selen_ob.launch_environ(environ)
    print('Launching MH enironment\n')
    if environ == 'DEVL':
        print('Please manually type in username and password to login within 30 seconds and wait\n')
        selen_ob.wait(30)

    print('Logged in successfully\n')
    selen_ob.search_menu_going_down('Pix Transactions', 1)
    selen_ob.wait(5)
    selen_ob.double_click('pix_trans_menu_header_field')
    selen_ob.switch_to_diff_iframe('pix_trans_menu_iframe')
    print('Looking at pix trans menu\n')

    print('Beginning loop to resend pix transactions from excel file\n')
    # df_set = set(df['TransactionNumber'].to_list())
    counter = row_to_start_index
    for row in range(row_to_start_index, length):
        selen_ob.click('pix_trans_menu_quick_filter_button')
        selen_ob.click('pix_trans_menu_saved_filters_button')
        selen_ob.click('pix_trans_menu_apply_button')

        trans_num = str(df['TransactionNumber'].iloc[row])
        trans_type = str(df['TransactionType'].iloc[row])
        trans_code = str(df['TransactionCode'].iloc[row])
        item = str(df['ItemName'].iloc[row])
        lpn = str(df['LPNNumber'].iloc[row])
        if lpn == "nan":
            lpn = ""
        date_created = str(df['DateCreated'].iloc[row])
        date_modified = str(df['DateModified'].iloc[row])

        print('Found pix trans num param\n')
        print('Created status list\n')
        status_list = []

        # date_list = date_created.split(":", 1)
        # new_min = str(int(date_list[1]) + 1)
        # date_modified = date_list[0] + ":" + new_min

        print("trans_num: " + trans_num)
        print("trans_type: " + trans_type)
        print("trans_code: " + trans_code)
        print("item: " + item)
        print("lpn: " + lpn)
        print("date_created: " + date_created)
        print("date_modified: " + date_modified + "\n")

        selen_ob.choose_pix_trans_type_and_code_options(trans_type, trans_code)
        selen_ob.type_keys_enter('pix_trans_menu_saved_filters_submenu_created_date_from_input_box', date_created,
                                 False)
        selen_ob.type_keys_enter('pix_trans_menu_saved_filters_submenu_created_date_to_input_box', date_modified, False)
        selen_ob.type_keys_enter('pix_trans_menu_saved_filters_submenu_ilpn_input_box', lpn, False)
        selen_ob.type_keys_enter('pix_trans_menu_saved_filters_submenu_item_input_box', item, False)
        selen_ob.click('pix_trans_menu_saved_filters_submenu_apply_button')

        print('Chose pix trans param to search for\n')

        selen_ob.wait(3)

        print('Reading pix trans menu table, looping through rows to find correct trans num\n')
        status_list = selen_ob.read_mh_pix_trans_table(trans_num, status_list)
        status_df.loc[len(status_df.index)] = status_list
        counter = counter + 1
        print("Analyzed pix trans num: " + str(counter) + " of " + str(length) + "\n")

    return status_df


def main():
    # create Status list and main selen_ob object to call common methods on - don't change
    selen_ob, Status = CreateData.create_selen_object()
    print('Created main selen_ob object for testing\n')

    # create unique data param to pass into main selen_ob funct - can change ///
    environ = 'PROD'
    print('Set environment to ' + environ + '\n')

    download_folder_path = os.path.expanduser("~") + "/Downloads/"
    print('Found download folder\n')
    excel_file_path = download_folder_path + 'pix_trans_resend.xlsx'
    print('Found excel file\n')
    df = pd.read_excel(excel_file_path, dtype=str)
    print('Set excel file to import pix transactions to resend\n')

    df['DateCreated'] = pd.to_datetime(df['DateCreated']).dt.strftime('%d/%m/%Y %H:%M')
    df['DateModified'] = pd.to_datetime(df['DateModified']).dt.strftime('%d/%m/%Y %H:%M')
    print('Modified date created and date modified columns to correct date and time format\n')

    length = len(df.index)
    temp_df = df.loc[df['Status'].isna()].head(1)
    row_to_start_index = temp_df.index[0]
    print('Found row to start at in excel file\n')

    status_df = pd.DataFrame(columns=['STATUS'])
    print('Created status_df\n')

    print('Set pre-parameters\n')

    try:
        # main function for interacting with selen_ob - change based on what funct want to do ///
        print('Beginning main script process\n')
        status_df = resend_pix_transactions(selen_ob, environ, df, row_to_start_index, length, status_df)
    finally:
        # first setup for exporting script results, get time stamp, directory and screenshot paths - don't change
        time_stamp, directory_path = ExportScriptResults.export_setup()
        print('Found path to export script results to\n')

        # create data dataframe based on what data you want to save and
        # set a unique script results path - can change ///

        script_results_path = directory_path + r'/Resend_PIX_Transactions_Script Script Results at ' + time_stamp + \
                              '.xlsx'
        print('Set path to export script results\n')

        # export excel file for script results - don't change
        ExportScriptResults.create_and_export_excel_results(selen_ob, Status, time_stamp, status_df, script_results_path)
        print('Created script results\n')

        with pd.ExcelWriter(excel_file_path, mode="a", engine="openpyxl", if_sheet_exists="overlay") as writer:
            status_df.to_excel(writer, sheet_name="Sheet1", header=False, startrow=row_to_start_index + 1, startcol=7,
                               index=False)
        print('Set status_df to pix_trans_resend excel file\n')

        # selen_ob.get_driver().quit()
        # print('Closed automated browser window\n')

        print('SCRIPT HAS FINISHED RUNNING\n')
        print('Exported results in excel file, please check in the Scripts Results folder in your C drive\n')
        print('If you want to run the script again with new pix transactions, modify the pix_trans_resend.xlsx file '
              'with new pix transaction numbers and run the script again, ensuring their status column is blank\n')
        print('Make sure to close the automated browser window and console window before running script again')


main()
