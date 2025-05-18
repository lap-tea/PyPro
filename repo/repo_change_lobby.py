import sys, repo_change_lobby_const as rc, time, os

full_path = rc.REPO_MOD_LOBBY_SIZE_PATH.format(os.getlogin(),rc.REPO_MOD_LOBBY_SIZE_FILE)
try:
    file_result = open(file=full_path,mode='r').read()
except:
    print("Файл недоступен",full_path)
    full_path = input(rc.FILE_NOT_FOUND_TEXT)
    file_result = open(file=full_path, mode='r').read()
print("Загружен файл:",full_path)

par_start = file_result.find(rc.PAR)
val_start = par_start + len(rc.PAR)
val_end = file_result.find("\n",val_start,0)
current_lobby_size = int(file_result[val_start:val_end].strip())
print(rc.CURRENT_LOBBY_SIZE_TEXT,current_lobby_size)

a = input(rc.SET_NEW_LOBBY_SIZE_TEXT)

while not a.isdigit():
    if len(a) == 0:
        rc.CHANGE_LOBBY_SIZE_FLG = False # ничего не ввели - размер лобби не меняем
    else:
        a = input(rc.NOT_DIGIT_TEXT) # ввели что-то что не является цифрой
else:
    a = int(a)
    if a == 0 or a == current_lobby_size:
        rc.CHANGE_LOBBY_SIZE_FLG = False # ввели ноль или то же количество - размер лобби не меняем
    else:
        rc.CHANGE_LOBBY_SIZE_FLG = True

if rc.CHANGE_LOBBY_SIZE_FLG:
    file_result = file_result[:val_start] + str(a) + file_result[val_end:]
    print(rc.NEW_LOBBY_SIZE_TEXT, file_result[val_start:val_end])
    open(file=full_path, mode='w').write(file_result)
else:
    print(rc.CURRENT_LOBBY_SIZE_TEXT,current_lobby_size)
print(f"Закрытие окна через {rc.EXIT_TIME_SEC} секунд")
time.sleep(rc.EXIT_TIME_SEC)
print('new line')