import psutil

cpu=psutil.cpu_freq() #cpu 프리퀀시
print(cpu)

cpu_core=psutil.cpu_count(logical=False) #cpu 코어 갯수
print(cpu_core)

memory=psutil.virtual_memory() #메모리
print(memory)

disk=psutil.disk_partitions() #디스트
print(disk)

net=psutil.net_io_counters #네트워크크
print(net)
