#! /usr/bin/env python
# -*- coding: utf-8 -*-
# --- create by :UwbDataPreprocess at : 17-5-7  下午5:09

import os

import re


import numpy as np

import matplotlib.pyplot as plt
import array

class UwbDataPre:
    def __init__(self,dir_name):
        self.file_name = dir_name

        self.start_time = 0.0

        self.tmp_array = array.array('d')

        for file in os.listdir(dir_name):
            print(file)
            if 'uwbdata.txt' in file:
                self.file_name += file
                self.start_time = float(file.split('_')[0])

        print("filr name is :" , self.file_name)
        print("start_time :" , self.start_time)


        this_file = open(self.file_name)

        is_new_ob=False

        mac_list = list()

        for line in this_file.readlines():
            # print(line)
            if line.split(' ')[2] == '@R':
                # print(line)
                if line.split(' ')[3] == '1' or line.split(' ')[3] == '0':
                    mac_name = line.split(' ')[4]
                    if mac_name not in mac_list:
                        mac_list.append(mac_name)


        print("mac list :" , mac_list)
        this_file.close()
        this_file=open(self.file_name)

        is_first_line = True

        for line in this_file.readlines():
            if is_first_line:
                self.start_time -= float(line[1:10])
                is_first_line=False

            if line.split(' ')[2] == '@R':
                print(line)
                if line.split(' ')[3] != 'F1':
                    print(line)
                    mac_name = line.split(' ')[4]
                    self.tmp_array.append(float(self.start_time+float(line[1:10])))
                    print("time : ", float(self.start_time + float(line[1:10])))
                    for i in range(len(mac_list)):



                        if mac_name != mac_list[i]:
                            self.tmp_array.append(-10.0)
                        else:
                            self.tmp_array.append(float(line.split(' ')[5]))


        self.result_uwb = np.frombuffer(self.tmp_array,dtype=np.float).reshape([-1,5])

        print(self.result_uwb)


        np.savetxt(dir_name+"uwb_result.csv",self.result_uwb,delimiter=',')


        plt.figure()
        plt.plot(self.result_uwb[:,0],'r')
        plt.show()

        # self.start_time





if __name__ == '__main__':
    udp = UwbDataPre("/home/steve/Data/FastUwbDemo/2/")

