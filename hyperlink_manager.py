from tkinter import CURRENT

class HyperlinkManager:
    def __init__(self, text):

        self.text = text

        self.text.tag_config("hyper", foreground="blue")
        self.text.tag_config('dyper', background="yellow", foreground="red")

        self.text.tag_bind("hyper", "<Enter>", self._enter)
        self.text.tag_bind("hyper", "<Leave>", self._leave)
        self.text.tag_bind("hyper", "<Button-1>", self._click)
        self.text.tag_bind("dyper", "<Button-1>", self._click)

        self.reset()

    def reset(self):
        self.links = {}

    def add_default(self, action, param):
        # add an action to the manager.  returns tags to use in
        # associated text widget
        tag = "hyper-%d" % len(self.links)
        self.links[tag] = (action, param)
        return "hyper", tag

    def add_red(self, action, param):
        # add an action to the manager.  returns tags to use in
        # associated text widget
        tag = "dyper-%d" % len(self.links)
        self.links[tag] = (action, param)
        return "dyper", tag

    def _enter(self, event):
        self.text.config(cursor="hand2")

    def _leave(self, event):
        self.text.config(cursor="")

    def _click(self, event):
        for tag in self.text.tag_names(CURRENT):
            if tag[:6] == "hyper-" or tag[:6] == "dyper-":
                self.links[tag][0](self.links[tag][1])
                return