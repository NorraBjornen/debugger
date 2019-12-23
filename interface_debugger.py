import tkinter as tk
from tkinter import *
from hyperlink_manager import HyperlinkManager
import os
import argparse

global textNumb, text, script_name, hyperlink

state = {}


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

    return parser


def on_link_press(cnt=0):
    global hyperlink
    print(str(cnt) + " pressed")
    for j in range((cnt // 10) + 1):
        textNumb.delete(float(cnt))
    if not state[cnt]:
        textNumb.insert(float(cnt), str(cnt), hyperlink.add_red(on_link_press, cnt))
        state[cnt] = True
    else:
        textNumb.insert(float(cnt), str(cnt), hyperlink.add_default(on_link_press, cnt))
        state[cnt] = False


def start():
    points = []
    for k, v in state.items():
        if v:
            points.append(k)

    length = len(points)
    if length == 0:
        return

    points_pointer = 0
    current = points[points_pointer]
    i = 1
    content = ["import tracer\n", "from tracer import set_breakpoint\n", "tracer.set_trace()\n"]

    with open("script_to_debug.py", "r") as f:
        for line in f:
            if i == current:
                spaces_to_add = ""
                j = 0
                while line[j] == " ":
                    spaces_to_add += " "
                    j += 1
                content.append(spaces_to_add + "set_breakpoint()\n")
                points_pointer += 1
            if length > points_pointer:
                current = points[points_pointer]

            content.append(line)
            i += 1

    with open("temp.py", "w+") as f:
        f.writelines(content)
    os.system('python temp.py')


def get_script():
    content = []
    with open("script_to_debug.py", "r") as f:
        for line in f:
            content.append(line)
    return content


def main():
    parser = create_parser()
    namespace = parser.parse_args()

    global script_name
    script_name = namespace.py

    if script_name is None:
        parser.print_help()
        return

    root = Tk()
    btn = Button(text="Отладить", command=start)
    btn.pack()

    txtFrame = Frame()
    txtFrame.pack()

    global textNumb, text, hyperlink
    textNumb = tk.Text(txtFrame, width=3)
    textNumb.pack(side=LEFT)

    hyperlink = HyperlinkManager(textNumb)

    text = tk.Text(txtFrame)
    i = 1
    for line in get_script():
        text.insert(END, line)
        textNumb.insert(END, str(i) + "\n", hyperlink.add_default(on_link_press, i))
        state[i] = False
        i += 1

    text.pack(side=LEFT)
    root.mainloop()


if __name__ == '__main__':
    main()

