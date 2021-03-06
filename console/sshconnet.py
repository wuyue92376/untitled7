import paramiko
def connectssh(hostname,port,username,password,command):
    # 创建SSH对象
    ssh = paramiko.SSHClient()
    # 允许连接不在know_hosts文件中的主机
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # 连接服务器
    ssh.connect(hostname=hostname, port=port, username=username, password=password)
    # 执行命令
    stdin,stdout,stderr = ssh.exec_command(command)
    rightinfo=stdout.read()
    errorinfo=stderr.read()
    f=(bool(errorinfo))
    #获取命令结果
    if f:
        result= errorinfo
    else:
        result=rightinfo

    #关闭连接
    ssh.close()
    print(result)
    return result