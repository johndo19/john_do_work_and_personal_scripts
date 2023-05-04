import CreateData
import pandas as pd
import os


def export_setup():
    # get date and time - don't change
    date_stamp, time_stamp = CreateData.get_date_and_time()
    # create new directory for script results if one with the date doesn't exit - don't change
    directory_path = r'C:/Script Results/Script Results for ' + date_stamp
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)

    return time_stamp, directory_path


def create_and_export_excel_results(MH, Status, time_stamp, data, script_results_path):
    # take a screenshot of last screen shown, set path for screenshot - don't change
    # screenshot_path_1 = r'C:/Screenshots'
    # screenshot_path_2 = screenshot_path_1 + r'/screenshot_' + time_stamp + '.png'
    # if not os.path.exists(screenshot_path_1):
    #     os.makedirs(screenshot_path_1)
    # MH.take_screenshot(screenshot_path_2)

    # append list of results of all steps that passed - don't change
    Steps = MH.get_Steps()
    Steps.append('SCRIPT FINISHED RUNNING')
    for step in Steps:
        Status.append('PASSED')

    # create dataframes for test results, data, and the screenshot - change param for data ///
    test_results = pd.DataFrame({'Steps': Steps, 'Status': Status})
    # screenshot = pd.DataFrame({'Screenshot': ['Last screen shown', '-->']})

    # create a new excel file with directory path - change file name ///
    writer = pd.ExcelWriter(script_results_path, engine='xlsxwriter')

    # set the dataframes to respective sheets - don't change
    sheets = {'Script Results': test_results, 'Data': data}
    for sheet_name in sheets.keys():
        sheets[sheet_name].to_excel(writer, sheet_name=sheet_name, index=False)

    # insert the screenshot to the screenshot sheet - don't change
    # worksheet = writer.sheets['Screenshot']
    # worksheet.insert_image('B1', screenshot_path_2)

    # save the excel file - don't change
    writer.close()
