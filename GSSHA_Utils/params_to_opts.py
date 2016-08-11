import os
from pandas import DataFrame, read_table, to_datetime
from numpy import array, loadtxt, column_stack
from datetime import datetime, timedelta

name = 'goodwin_run1'


def to_tpl(root, input_folder, input_filename, cal_parameters):

    def line_gen(strings):
        pass
    cmt = ''.join([name, '.cmt'])
    full_cmt_path = os.path.join(root, cmt)
    txt = loadtxt(full_cmt_path, dtype=str, delimiter='\t').tolist()
    for row in txt:
        if row.startswith('ROUGHNESS', 'RETENTION', 'GREEN_AMPT_INFILTRATION'):
            id = []
            pos = txt.index(row)
            for item in txt[(pos + 3):]:
                try:
                    id.append(int(item[0]))
                except TypeError:
                    break


            print 'postion of start roughnexx table: {}'.format(pos)
            print 'row value: {}'.format(row)


if __name__ == '__main__':
    home = os.path.expanduser('~')
    print 'home: {}'.format(home)
    root = os.path.join(home, 'Documents', 'USACE', 'Calib_Testing', 'goodwin_v50_runfiles_SLMprep')
    to_tpl(root, name)


