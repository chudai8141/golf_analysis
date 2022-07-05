import os
from typing import List

from matplotlib import pyplot as plt

import bvh


imf_name = ['IMF1', 'IMF2', 'IMF3', 'IMF4', 'IMF5', 'IMF6', 'IMF7', 'IMF8']


def plot(
    spectrum_time,
    freq_all_data,
    amp_all_data,
    Nod,
    frame,
    start,
    end,
    joint_name,
    select_data,
    save_path
):
    plt.clf()
    plt.figure(dpi=200, figsize=(16, 9))
    plt.rcParams['font.family'] = 'Times new Roman'
    plt.rcParams['font.size'] = 30
    for n in range(start, end):
        plt.scatter(spectrum_time[n, :], freq_all_data[n, :], s = 100, c=amp_all_data[n, :frame], cmap='jet')
    ax = plt.gca()
    ax.set_facecolor([0.0, 0.0, 0.5])
    plt.ylim(0, 10)
    plt.xlabel('time [s]')
    plt.ylabel('frequency [Hz]')
    plt.colorbar()
    file_name = '_'.join(imf_name[start:end])
    # print('save figure', os.path.join(save_path, file_name) )
    plt.savefig(os.path.join(save_path, file_name))
    plt.close()

def output_bvh(result_memd_list:List):
    output_path = 'output_bvh'
    file_number = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth']

    for result_memd in result_memd_list:
        user = result_memd.user.user
        memd_data = result_memd.imf
        dt = result_memd.dt
        text = result_memd.text
        ballistic = result_memd.user.ballistic
        file_num = file_number.pop(0)
        trend = memd_data[-1]
        if not os.path.isdir(output_path):
            os.mkdir(output_path)
        if not os.path.isdir(os.path.join(output_path, user)):
            os.mkdir(os.path.join(output_path, user))
        if not os.path.isdir(os.path.join(output_path, user, ballistic)):
            os.mkdir(os.path.join(output_path, user, ballistic))
        if not os.path.isdir(os.path.join(output_path, user, ballistic, file_num)):
            os.mkdir(os.path.join(output_path, user, ballistic, file_num))

        for nod in range(len(memd_data)):
            if nod != memd_data.shape[0] - 1:
                file_name = os.path.join(output_path, user, ballistic, file_num, '_imf_' + str(nod+1))
                data = memd_data[nod] + trend
            else:
                file_name = os.path.join(output_path, user, ballistic, file_num, 'trend')
                data = trend

            bvh.bvhoutput(data.T, dt, file_name, text)
