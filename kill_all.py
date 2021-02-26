os.getpid()
p = psutil.Process(os.getpid())
nm = p.name()
print(nm)
#############Kill Process Script##################
def kill_all():
    for proc in psutil.process_iter(['pid', 'name', 'username']):
        try:
            if((proc.info['username'] == None)):
                print('skipped :',proc.info['pid'])
            elif((proc.info['name'] == None)):
                print('skipped :',proc.info['pid'])
            elif('WindowsTerminal.exe' in proc.info['name']):
                print('skipped 1 :',proc.info['pid'])
            elif('Qt5gui.exe' in proc.info['name']):
                print('skipped 1 :',proc.info['pid'])
            elif('conhost.exe' in proc.info['name']):
                print('skipped 2 :',proc.info['pid'])
            elif('msedge.exe' in proc.info['name']):
                print('skipped 2 :',proc.info['pid'])
            elif('python.exe' in proc.info['name']):
                print('skipped 2 :',proc.info['pid'])
            elif('explorer.exe' in proc.info['name']):
                print('skipped 2 :',proc.info['pid'])
            elif('cmd.exe' in proc.info['name']):
                print('skipped 2 :',proc.info['pid'])
            elif('sublime_text.exe' in proc.info['name']):
                print('skipped 2 :',proc.info['pid'])               
            elif(psutil.users()[0][0] not in proc.info['username']):
                print('skipped :',proc.info['pid'])
            else:
                print(proc.info)
                #x=input('else : ')
                print('killed')
                proc.kill()
        except Exception as e:
                print(e)
                pass