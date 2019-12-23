import sys
import linecache

dispatch_next = False
dispatch_current = False


def set_trace():
    sys.settrace(dispatch)


def set_breakpoint():
    global dispatch_next
    dispatch_next = True


def dispatch(frame, event, arg):
    global dispatch_next, dispatch_current
    if dispatch_next:
        if dispatch_current:
            line = linecache.getline(
                frame.f_code.co_filename,
                frame.f_lineno
            )
            print("Следующая строка: " + line)
            cmd = True
            while cmd:
                cmd = input('Введите имя переменной для вывода: ')
                print_var(cmd, frame)
            dispatch_next = False
            dispatch_current = False
        else:
            dispatch_current = True
    return dispatch


def print_var(var, frame):
    if var in frame.f_locals:
        print(frame.f_locals[var])
