import os
import sys
import pandas as pd
import CreateData
import ExportScriptResults
import os.path
from connection import connect
import time
from datetime import date


def main():
    date_stamp = date.today().strftime("%m%d%Y")
    time_stamp = time.strftime("%H%M%S", time.localtime())
    print(date_stamp + time_stamp)


main()
