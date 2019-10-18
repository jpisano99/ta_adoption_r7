import csv
import datetime
import time
import xlrd
import os
from my_app.func_lib.open_wb import open_wb
from my_app.settings import app_cfg


def push_list_to_csv(my_list, csv_output, run_dir=app_cfg['UPDATES_SUB_DIR'], tbl_name='table1'):
    path_to_my_app = os.path.join(app_cfg['HOME'], app_cfg['MOUNT_POINT'], app_cfg['MY_APP_DIR'])
    path_to_run_dir = (os.path.join(path_to_my_app, run_dir))
    path_to_file = os.path.join(path_to_run_dir, csv_output)
    print()
    print('CREATING IN DIRECTORY >>>>>>>>>> ', path_to_run_dir)
    print('CREATING SHEET >>>>>>>>>> ', csv_output)
    print()

    # for x, my_row in enumerate(my_list):
    with open(path_to_file, 'w', newline='') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(my_list)

    writeFile.close()
    return


if __name__ == "__main__" and __package__ is None:
    # wb, ws = open_wb(app_cfg['XLS_BOOKINGS'])
    wb, ws = open_wb(app_cfg['XLS_AS_DELIVERY_STATUS'])

    my_csv_list = []
    for my_row in range(ws.nrows):
        my_csv_row = []
        tmp_val = None
        for my_col in range(ws.ncols):
            my_cell = ws.cell(my_row, my_col)

            if my_cell.ctype == xlrd.XL_CELL_DATE:
                tmp_val = datetime.datetime(*xlrd.xldate_as_tuple(my_cell.value, wb.datemode))
                tmp_val = tmp_val.strftime('%D')
                my_csv_row.append(tmp_val)

            elif my_cell.ctype == xlrd.XL_CELL_NUMBER:
                tmp_val = str(my_cell.value)
                my_csv_row.append(tmp_val)

            else:
                # Strip out Unicode characters above value 127
                # Make it all ASCII
                cell_bytes = my_cell.value.encode('ascii', 'ignore')
                tmp_val = cell_bytes.decode('utf-8')
                my_csv_row.append(tmp_val)

        my_csv_list.append(my_csv_row)

    # print(len(my_csv_list))
    # for row in my_csv_list:
    #     for col in row:
    #         print(type(col), col)
    #     break

    push_list_to_csv(my_csv_list, 'my_csv.csv')
    exit()

