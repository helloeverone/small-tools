#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @Time : 2019/12/25 14:10
# author:wangshuai
import subprocess
import os

def dyts():
    print('''
    ===============操作系统管理器===================
            (1) 查看操作系统CPU相关信息           
            (2) 查看内存相关信息           
            (3) 查看操作系统发行版本           
            (4) 查看操作系统内核版本           
            (5) 查看磁盘个数及分区情况           
            (6) 查看磁盘使用及挂载情况         
            (7) 查看磁盘inode使用情况      
            (8) 查看磁盘分区文件系统类型       
            (9) 查看服务器网络相关信息   
            (10)系统内核参数控制
            (11)操作系统进程查看及控制
            (12)通过浏览器动态监控服务器资源使用情况             
            (13)取消
    ===============================================
    ''')

def cpuinfo():

    cpu_jg = os.popen("lscpu |grep 'Architecture' |awk -F ':' '{print $2}'").read().replace(" ", "")
    print("该操作系统cpu架构为:%s" %cpu_jg)
    cpu_family = os.popen("lscpu |grep 'CPU family' |awk -F ':' '{print $2}'").read().replace(" ", "")
    print("该操作系统cpu家族编号为:%s"%cpu_family)
    cpu_num = os.popen('cat /proc/cpuinfo| grep "processor"| wc -l').read().replace(" ","")
    print("该操作系统cpu核心数为:%s"%cpu_num)
    cpu_zp = os.popen("cat /proc/cpuinfo |grep 'cpu MHz' |awk -F ':' '{print $2}' |awk 'NR==1'").read().replace(" ","")
    print("该操作系统cpu主频为:%sMHZ"%cpu_zp)
    cpu_physical = os.popen('cat /proc/cpuinfo |grep "physical id"|sort |uniq|wc -l').read().replace(" ","")
    print("该操作系统物理cpu个数为:%s"%cpu_physical)
    cpu_hx = os.popen("cat /proc/cpuinfo| grep 'name' |awk -F ':' '{print $2}' |awk 'NR==1'").read().replace(" ","")
    print("该操作系统cpu型号为:%s"%cpu_hx)
    cpu1_cache = os.popen("lscpu |grep 'L1d cache' |awk -F ':' '{print $2}'").read().replace(" ", "")
    print("该操作系统单核cpu一级缓存大小为:%s" % cpu1_cache)
    cpu2_cache = os.popen("lscpu |grep 'L2 cache' |awk -F ':' '{print $2}'").read().replace(" ", "")
    print("该操作系统单核cpu二级缓存大小为:%s" % cpu2_cache)
    cpu3_cache = os.popen("lscpu |grep 'L3 cache' |awk -F ':' '{print $2}'").read().replace(" ", "")
    print("该操作系统单核cpu三级缓存大小为:%s" % cpu3_cache)
    line = input()
    if line == '\n':
        return

def meminfo():
    mem_Total = os.popen("cat /proc/meminfo |grep MemTotal |awk -F ':' '{print $2}'").read().replace(" ","")
    print("该操作系统可用内存总量为:%s"%mem_Total)
    mem_Free = os.popen("cat /proc/meminfo |grep MemFree |awk -F ':' '{print $2}'").read().replace(" ","")
    print("该操作系统当前剩余可用内存为:%s" % mem_Free)
    mem_Buffer = os.popen("cat /proc/meminfo |grep Buffers |awk -F ':' '{print $2}'").read().replace(" ","")
    print("该操作系统Buffer容量为:%s" % mem_Buffer)
    mem_Cached = os.popen("cat /proc/meminfo |grep ^Cached |awk -F ':' '{print $2}'").read().replace(" ","")
    print("该操作系统Cached容量为:%s"%mem_Cached)
    swap_Total = os.popen("cat /proc/meminfo |grep SwapTotal |awk -F ':' '{print $2}'").read().replace(" ","")
    print("该操作系统swap交换分区总容量为:%s" %swap_Total)
    swap_Free = os.popen("cat /proc/meminfo |grep SwapFree |awk -F ':' '{print $2}'").read().replace(" ", "")
    print("该操作系统剩余swap交换分区容量为:%s" % swap_Free)
    VmallocTotal = os.popen("cat /proc/meminfo |grep VmallocTotal |awk -F ':' '{print $2}'").read().replace(" ", "")
    print("该操作系统Vmalloc内存总容量为:%s" %VmallocTotal)
    VmallocUsed = os.popen("cat /proc/meminfo |grep VmallocUsed |awk -F ':' '{print $2}'").read().replace(" ", "")
    print("该操作系统Vmalloc内存使用量为:%s" % VmallocUsed)
    line = input()
    if line == '\n':
        return

def linux_release():
    linux_release = os.popen("cat /etc/redhat-release").read()

    print("该操作系统发行版本为:%s" %linux_release)
    line = input()
    if line == '\n':
        return

def linux_kernel():
    linux_kernel = os.popen("cat /proc/version").read()

    print("该操作系统内核版本为:%s" %linux_kernel)
    line = input()
    if line == '\n':
        return
def linux_file_system():
    linux_f_s = os.popen("blkid `df -h |awk 'NR==2'` |awk '{print $3}'").read()

    print("该操作系统磁盘分区文件系统为:%s" %linux_f_s)
    line = input()
    if line == '\n':
        return
def disk_info():
    disk_info = os.popen("lsblk").read()
    disk_num = os.popen("fdisk -lu |grep sectors |grep Disk |wc -l").read()
    print('''==============磁盘个数及分区情况================''')
    print(disk_info)
    print("该操作系统磁盘个数为:%s" % disk_num)
    line = input()
    if line == '\n':
        return
def disk_use():
    print('''===================磁盘使用及挂载情况=======================''')
    disk_use = os.popen("df -h").read()
    print(disk_use)
    line = input()
    if line == '\n':
        return
def disk_inode():
    print('''===================磁盘inode使用情况=======================''')
    disk_inode = os.popen("df -i").read()
    print(disk_inode)
    line = input()
    if line == '\n':
        return
def allps():
    while True:
        print('''
        ===================进程控制面板=======================
                    (1) 查看当前系统运行的所有进程信息           
                    (2) 查看进程详细状态          
                    (3) 强制结束指定进程
                    (4) 返回主控制面板
        
        ''')
        input_num = int(input("请输命令编号："))
        if input_num == 4:
            return
        if input_num == 1:
            print('''===================当前系统运行的所有进程信息=======================''')
            all_ps = os.popen("ps -aux").read()
            print(all_ps)
        if input_num == 2:
            print('''===================输入进程Pid可查看进程详细状态=======================''')
            Pid = input("请输Pid号：")
            Pid_detial = os.popen("cat /proc/%s/status"%Pid).read()
            print(Pid_detial)
        if input_num == 3:
            Pid_kid = input("请输入需要强制kill掉的进程Pid号：")
            Pid_detial = os.popen("kill -9 %s"%Pid_kid).read()
        line = input()
        if line == '\n':
            break



def system_cl():
    while True:
        print('''
        ===================系统内核参数控制面板=======================
        (1) 设置进程ID最大值                       
        (2) 设置服务器禁止响应imcp数据包          
        (3) 开启服务器路由转发功能                    
        (4) 设置服务器只响应目的IP地址为接收网卡上的本地地址的arp请求
        (5) 返回主控制面板
        ''')
        input_num = int(input("请输命令编号："))
        if input_num == 5:
            return
        if input_num == 1:
            pid_max = int(input("请输Pid最大值："))
            print('''==========sysctl信息==========''')
            all_ps = os.popen("echo %d > /proc/sys/kernel/pid_max"%pid_max).read()
            print(os.popen("sysctl -a |grep pid_max").read())
        if input_num == 2:
            print('''==========sysctl信息==========''')
            os.popen("echo 1 > /proc/sys/net/ipv4/icmp_echo_ignore_all").read()
            print(os.popen("sysctl -a |grep icmp_echo_ignore_all").read())
        if input_num == 3:
            print('''==========sysctl信息==========''')
            os.popen("echo 1 > /proc/sys/net/ipv4/ip_forward").read()
            print(os.popen("sysctl -a |grep ip_forward |awk 'NR==1'").read())
        if input_num == 4:
            print('''==========sysctl信息==========''')
            os.popen("echo 1 > /proc/sys/net/ipv4/conf/all/arp_ignore").read()
            print(os.popen("sysctl -a |grep arp_ignore |awk 'NR==1'").read())
        line = input()
        if line == '\n':
            break
def network_info():
    while True:
        print('''
        ===================服务器网络相关信息=======================
        (1) 查看本机服务器IP地址                       
        (2) 查看服务器网络连接信息           
        (3) 查看服务器开放的服务及对应端口号                      
        (4) 设置服务器只响应目的IP地址为接收网卡上的本地地址的arp请求
        (5) 返回主控制面板
        ''')
        input_num = int(input("请输命令编号："))
        if input_num == 5:
            return
        if input_num == 1:
            net_ip = os.popen("ifconfig |awk 'NR==2' |awk '{print $2}'").read()
            print("该服务器内网IP为:%s"%net_ip)
        if input_num == 2:
            print('''==========服务器网络连接信息==========''')
            net_lj = os.popen("netstat -ntu").read()
            print(net_lj)
        if input_num == 3:
            print('''==========开放的服务及对应端口号==========''')
            net_fw = os.popen("netstat -tlnup").read()
            print(net_fw)
        line = input()
        if line == '\n':
            break
def glances():
    # glances_web = os.popen("glances -w").read()
    # print(glances_web)
    gnet_ip = os.popen("ifconfig |awk 'NR==2' |awk '{print $2}'").read()
    glances_web=(os.system("glances -w >> /dev/null&"))
    if glances_web == 0:

        stroutput = "Glances Web User Interface started on http://0.0.0.0:61208/".replace("0.0.0.0", gnet_ip).replace("\n", "")
        print(stroutput)

    else:
        print("glances web service start fail!")

    line = input()
    if line == '\n':
        return

if __name__ == "__main__":

    while True:
        dyts()

        input_num = int(input("请输命令编号：").replace("\n", ""))
        if input_num == 13:
            exit()
        if input_num == 1:
            cpuinfo()
        if input_num == 2:
            meminfo()
        if input_num == 3:
            linux_release()
        if input_num == 4:
            linux_kernel()
        if input_num == 5:
            disk_info()
        if input_num == 6:
            disk_use()
        if input_num == 7:
            disk_inode()
        if input_num == 8:
            linux_file_system()
        if input_num == 9:
            network_info()
        if input_num == 10:
            system_cl()
        if input_num == 11:
            allps()
        if input_num == 12:
            glances()

