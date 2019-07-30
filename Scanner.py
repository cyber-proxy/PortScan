import os

def kill_port(port):
    find_port = 'netstat -aon | findstr %s' % port
    result = os.popen(find_port)
    text = result.read();
    pid = text[-5: -1]
    find_kill = 'taskill -f -pid %s' %pid
    print(find_kill)
    result = os.popen(find_kill)
    return result.read()

if __name__ == '__main__':
    print kill_port(80)