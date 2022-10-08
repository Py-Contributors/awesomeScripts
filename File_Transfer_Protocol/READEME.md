# ** File Transfer Protocol**

*for Project of Computer Networking<br /> 

implementation of file transfer protocol using socket<br />
implemented in python, using multiprocessing to handle multi-user connection

### **How to run**
- clone this project
- make sure you have python 3 installed
- run the server by typing `python server.py` (by default server will use localhost, port 12009 for data transfer)
- In a different terminal session, run the client by typing `python client.py` 
- start to give command to the server (see some **commands** below)

### **Main Commands**
- [x] LS
- [x] DIR
- [x] QUIT
- [x] BYE
- [x] EXIT
- [x] PWD
- [x] CD
- [x] LCD
- [x] PROM
- [x] HASH
- [x] MKDIR
- [x] MDELETE
- [x] DELETE
- [x] RENAME
- [x] RMDIR
- [x] GET
- [x] PUT
- [x] MGET
- [x] MPUT


### **Additional Commands**
- [x] PWD, get current remote directory
- [x] CDUP, change to parent remote directory
- [x] CWD <path>, change current remote directory
- [x] MKD <dir_name>, make a directory in remote server
- [x] RMD <dir_name>, remove a directory in remote server
- [x] DELE <file_name>, delete a file in remote server 
- [ ] other commands... see [list of FTP commands](https://en.wikipedia.org/wiki/List_of_FTP_commands)

