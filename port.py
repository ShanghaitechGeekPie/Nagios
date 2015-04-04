import sys,time,socket
#读入相关数据
with open('G:/Documents/源代码/python/3.0/nagios/input_list', 'r') as iput_file:
    input_list = []
    for line in iput_file.readlines():
        input_list.append(line.strip())
#对输入的数据进行分离
ip_list =[]
port_list = []
for i in range(len(input_list)):
    if i % 2 == 0:
        ip_list.append(input_list[i])
        port_list.append(input_list[i+1].split())
    else:pass
#定义端口测试函数
def port_test(ip,port):
    with open('G:/Documents/源代码/python/3.0/nagios/results', 'a') as results:
        try:
            sc=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            sc.settimeout(0.5)
            sc.connect((ip,port))
            print (ip,':',port,':OK')
            result = ip + ':' + str(port) + ':OK' + '\n'
            results.write(result)     
        except socket.timeout:
            print(ip,':',port,':Fail')
            result = ip + ':' + str(port) + ':Fail' + '\n'
            results.write(result)
        except:
            pass
#依次对没每一个ip的每一个端口进行检查
for i in range(len(ip_list)):
    for x in port_list[i]:
        port_test(ip_list[i],int(x))