import sys
import linecache


def set_trace():
    sys.settrace(dispatch)


def dispatch(frame, event, arg):
    line = linecache.getline(
        frame.f_code.co_filename,
        frame.f_lineno
    )
    print(line)
    cmd = True
    while cmd:
        cmd = input('Введите имя переменной для вывода: ')
        run_cmd(cmd, frame)
    return dispatch


def run_cmd(cmd, frame):
    if cmd in frame.f_locals:
        print(frame.f_locals[cmd])
