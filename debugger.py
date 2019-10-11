import argparse


def create_parser():
    parser = argparse.ArgumentParser(
        prog='debugger',
        description='Эта программа позволяет отлаживать код, написанный на python',
        epilog='''Автор программы - Муравейник А.О.''',
        add_help=False
    )

    parent_group = parser.add_argument_group(title='Параметры')

    parent_group.add_argument('-h', '--help', action='help', help='Справка')

    parent_group.add_argument('-p', '--py', default=None, help='Указать путь к файлу, который необходимо отладить')
    parent_group.add_argument('-b', '--bp', default=None, help='Через запятую без пробела указать брейкпоинты '
                                                               'в которых программа приостановится')

    return parser


upper_divider = "---------------"
lower_divider = "-------------"
info = "DEBUGGING INTERFACE"


class Handler:

    def __init__(self):
        self.handled_messages = []

    def print(self, message):
        self.handled_messages.append(message)
        print(message)

    def input(self, message):
        self.handled_messages.append(message)
        input(message)


def debug(script_name, breakpoints, handler):
    with open(script_name, "r") as f:
        lines = f.readlines()

    lines = list(map(str.rstrip, lines))

    lines_len = len(lines)

    debugger_vars = dir()

    for i in range(1, lines_len + 1):
        if i in breakpoints:
            inner_vars = list(set(dir()) - set(debugger_vars))
            handler.print("\n\n" + upper_divider + info + upper_divider)
            for var in inner_vars:
                if var == "debugger_vars" or var == "i" or var == "var" or var == "inner_vars":
                    continue
                handler.print("|\t\t" + var + " = " + repr(locals()[var]) + "\t\t\t\t|")
            handler.input(lower_divider + "Press Enter to continue" + lower_divider + "\n\n")
        exec(lines[i-1])


def main():
    parser = create_parser()
    namespace = parser.parse_args()

    script_name = namespace.py

    if script_name is None:
        parser.print_help()
        return

    breakpoints_line = namespace.bp
    if breakpoints_line is None:
        breakpoints = []
    else:
        breakpoints = list(map(int, breakpoints_line.split(',')))

    debug(script_name, breakpoints, Handler())


if __name__ == '__main__':
    main()
