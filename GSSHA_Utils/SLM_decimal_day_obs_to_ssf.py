import os
from pandas import DataFrame, read_table, to_datetime
from numpy import array, savetxt, column_stack
from datetime import datetime, timedelta

in_loc = 'goodwin_v50_runfiles_run1'
in_file = 'extend82.g1.obs.si'

yr = 1982


def reformat_obs_to_ssf(root_dir, input_location, input_file, year):

    df = read_table(os.path.join(root_dir, input_location, input_file), header=None,
                    sep='       ', names=['Dec Day', 'Q'], index_col=None)

    new_ind = []
    for ind, row in df.iterrows():
        new_ind.append(day_repr(row[0], year))
    new_ind = array(new_ind)
    ser = array(df['Q'])
    df = DataFrame(ser, index=new_ind, columns=['Q cfs'])
    obs_str = array(['obs_flows' for x in range(0, len(df))])
    ind = to_datetime(df.index)
    obs_datetime = ind.strftime('%Y/%m/%d    %H:%M:%S')
    obs_datetime = array(obs_datetime, dtype=object)
    recs = column_stack((obs_str, obs_datetime, df))

    fmt = '\t'.join(['%s'])
    with open('{}\\dates_for_sim_outlet_hydrograph.txt'.format(os.path.join(root, in_loc)), 'wb') as f:
        # f.write('{}{}{}{}'.format(str_1, os.linesep, str_2, os.linesep))
        savetxt(f, obs_datetime, fmt=fmt, delimiter='\t', newline=os.linesep)

    fmt = '\t'.join(['%s'] + ['%s'] + ['%10.6f'])
    with open('{}\\{}_obs_data.txt'.format(os.path.join(root, in_loc), input_file.strip('.si')), 'wb') as f:
        # f.write('{}{}{}{}'.format(str_1, os.linesep, str_2, os.linesep))
        savetxt(f, recs, fmt=fmt, delimiter='\t', newline=os.linesep)
    print df


def day_repr(fractional_day, year, doy=True, fractional_year=False):
        dec = str(fractional_day)
        dec_split = dec.split('.')
        day_part_str = '.{}'.format(dec_split[1])
        day, day_part_flt = int(dec_split[0]), float(day_part_str)
        hour_dec = day_part_flt * 24
        hour_split = str(hour_dec).split('.')
        hour, hour_part = int(hour_split[0]), float('.{}'.format(hour_split[1]))
        min_part = str(round(hour_part * 60)).split('.')
        min = int(min_part[0])
        tup = datetime(year, 1, 1) + timedelta(days=day, hours=hour, minutes=min)
        return tup

if __name__ == '__main__':
    home = os.path.expanduser('~')
    print 'home: {}'.format(home)
    root = os.path.join(home, 'Documents', 'USACE', 'Calib_Testing')
    reformat_obs_to_ssf(root, in_loc, in_file, yr)

# ==================================EOF=================================
