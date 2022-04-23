import glob
import os
import re
import numpy as np


def load_files(tail):
    all_files = []
    all_files = glob.glob(f"{tail}/**/*.txt", recursive=True)
    print(all_files)
    return all_files


def parse_file(name):
    location = str(os.getcwd()+"\\"+name)
    file = open(location, "r")
    channels = []
    units = []
    end_position = 0
    for line in file:
        if "UNIT" in line:
            break
        if "&" in line or "]" in line:
            tmpArray = re.findall(r"'([^‘]*)'", line)
            channels.extend(tmpArray)
    for line in file:
        if "CHANNEL" in line:
            break
        if "&" in line or "]" in line:
            tmpArray = re.findall(r"'([^‘]*)'", line)
            units.extend(tmpArray)
    file.seek(0)
    for i, line in enumerate(file):
        if "END" in line:
            print(line, i)
            end_position = i
    end_extra = end_position+1
    print(end_extra)
    data_table = np.loadtxt(
        name,
        skiprows=end_extra,
        unpack=True
    )
    file.close()
    print(data_table, channels)
    return data_table, channels,
