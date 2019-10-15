from my_app.func_lib.db_tools import create_tables
from my_app.func_lib.get_list_from_ss import get_list_from_ss
from my_app.func_lib.open_wb  import open_wb
from my_app.func_lib.push_list_to_xls import push_list_to_xls
from my_app.pre_run_file_checks import pre_run_file_checks


# Use this file to place scripts that are called from views.py
def get_customer():
    print('Hello from main.py')
    # print('EXECUTING pre run checks')
    # pre_run_file_checks()
    # print('DONE EXECUTING pre run checks')

    # Try creating a Test_Table in the mySQL DB from Models.py
    create_tables("Test_Table")

    # Try retrieving a SmartSheet
    ss_test_list = get_list_from_ss('Tetration SKUs')
    print('Rows in my SmartSheet', len(ss_test_list))

    # Try writing an xlsx file to local storage
    push_list_to_xls(ss_test_list, 'my_test_sheet.xlsx')

    # Try opening an xlsx file from local storage
    xws, wb = open_wb('my_test_sheet.xlsx')
    return 'Hello from Main.py: I read: '+ str(len(ss_test_list)) + ' rows from SmartSheets'


if __name__ == "__main__" and __package__ is None:
    get_customer()
    exit()