import tkinter
import subprocess
import os

def output(cmd):
    list=cmd.split()
    data=subprocess.Popen(list, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out1=data.communicate()[0].decode('ascii')
    out=str(out1).strip('\n')
    return out

user=output('whoami')

if user=='root':
    print('running as root, all correct.')
else:
    print('not running as root, running as: '+output('whoami'))
    exit()
def closewin():
    root.destroy()

def checkinstalled():
    home=os.environ['HOME']
    out=os.listdir(home+'/TSARSOFT/')
    return out

def uninstall(prog):
    home=os.environ['HOME']
    os.system('rm -r '+home+'/TSARSOFT/'+prog)
    os.system('rm -r /bin/'+prog.lower())

def installprog(program):
    os.system('mkdir ~/TSARSOFT')
    os.system('mkdir ~/TSARSOFT/'+program)
    os.system('cd ~/TSARSOFT/'+program)
    os.system('rm ~/TSARSOFT/'+program+'/* -r')
    os.system('wget \'https://github.com/TSARSOFT/'+program+'/blob/master/'+program+'-latest.zip?raw=true\' -P ~/TSARSOFT/'+program+'/')
    os.system('mv ~/TSARSOFT/'+program+'/'+program+'-latest.zip?raw=true ~/TSARSOFT/'+program+'/'+program+'-latest.zip')
    os.system('unzip ~/TSARSOFT/'+program+'/'+program+'-latest.zip -d  ~/TSARSOFT/'+program+'/')
    os.system('echo \'python3 ~/TSARSOFT/'+program+'/latest/'+program+'.py\' >> ~/TSARSOFT/'+program+'/run.sh')
    os.system('chmod 777 ~/TSARSOFT/'+program+'/run.sh')
    os.system('cp ~/TSARSOFT/'+program+'/run.sh /bin/'+program.lower())
    updatelist()

def douninstall():
    uninstall(installed.get(tkinter.ACTIVE))
    updatelist()

root=tkinter.Tk()
root.title('TSARPKG graphical package manager')
root.geometry('1000x500')

menbar=tkinter.Menu()
menfile=tkinter.Menu()

menbar.add_cascade(menu=menfile, label='File')

root.config(menu=menbar)

menfile.add_command(label='close', command=lambda:closewin())

install=tkinter.LabelFrame(root, text='install')
install.pack(side='left', fill='y')

manager=tkinter.LabelFrame(root, text='manage')
manager.pack(side='right', fill='y')

installed=tkinter.Listbox(manager)
installed.grid(row=0, column=0)

def updatelist():
    installed.delete(0, tkinter.END)
    for items in checkinstalled():
        installed.insert(tkinter.END, items)

updatelist()
tkinter.Button(manager, text='uninstall', command=lambda:douninstall()).grid(row=1, column=0)

default=tkinter.StringVar()
default.set('TSARED')

select=tkinter.OptionMenu(install, default, 'TSARED', 'TSARCTL')
select.grid(row=0, column=0)

tkinter.Button(install, text='install', command=lambda:installprog(default.get())).grid(row=0, column=1)
