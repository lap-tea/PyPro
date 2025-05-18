import py_in_exe_const as pe, os, time, subprocess
# os.system("chcp 65001 > nul") # поправить
# -- установка pip если нужно
if not os.system(pe.PIP_INSTALL):
    print(os.system(pe.PIP_VERSION))
else:
    print(pe.PIP_INSTALLED)
    time.sleep(pe.EXIT_TIME_SEC)

# -- проверяем/задаём переменные среды для pip
path = os.environ.get(pe.PATH).split(";")
cmd = subprocess.Popen("where pip", shell=True, stdout=subprocess.PIPE)
for line in cmd.stdout:
    line = line.strip().decode()
    file = line.split("\\")[-1]
    line = line.replace(file,'')
    if line in path:
        print(pe.ENV_VAR_EXISTS,line)
    elif line.strip("\\") in path:
        print(pe.ENV_VAR_EXISTS,line.strip("\\"))
    else:
        os.environ[pe.PATH] = os.environ[pe.PATH]+";"+line
        print("Переменная среду дополнена", line.strip("\\"))
time.sleep(pe.EXIT_TIME_SEC)

# -- установка pyinstaller если нужно
if bool(os.system(pe.PYINSTALLER_EXISTS)):
    os.system(pe.PYINSTALLER_INSTALL)
    print(pe.PYINSTALLER_INSTALL_TEXT)
    time.sleep(pe.EXIT_TIME_SEC)

# -- начался процесс запаковки
file_correct_flg = False
file_path = input(pe.FILE_PATH).strip()
while not file_correct_flg:
    file_name = file_path.split("\\")[-1]
    if file_name.split(".")[-1].lower() == 'py' and os.path.exists(file_path):
        file_correct_flg = True
    else:
        file_path = input(pe.WRONG_FILE_TEXT).strip()
        file_correct_flg = False
file_path = file_path.replace(file_name,'')
os.chdir(file_path) # сменить рабочий каталог на каталог с файлом
print("Текущий каталог",os.getcwd())
os.system(pe.INSTALL_COMMAND + file_name) # вызов консоли запаковать файл в экзешник
print(f"Закрытие окна через {pe.EXIT_TIME_SEC} секунд")
time.sleep(pe.EXIT_TIME_SEC)