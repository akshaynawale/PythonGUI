#!/usr/bin/env python3

from tkinter import Tk, Button, Label, StringVar
from typing import Dict, Tuple
import psutil
import logging


class IfaceCounters():
    def __init__(self, master):
        """
        Initialize the GUI for the program
        """
        self.main_win = master
        self.top_label = Label(self.main_win, text="Interface Counters:")
        self.top_label.pack()
        self.output_dict: Dict[str, Tuple[str, str]] = {}
        self.get_counter_per_iface()
        self.ifaces = {}
        self.ifaces_data = {}
        for iface, iface_info in self.output_dict.items():
            output_bytes, input_bytes = iface_info
            self.ifaces_data[iface] = StringVar()
            self.ifaces_data[iface].set(f"{iface}:\nInput Bytes: {input_bytes}\nOutput Bytes: {output_bytes}")
            self.ifaces[iface] = Label(self.main_win, textvariable = self.ifaces_data[iface])
            self.ifaces[iface].pack()
        self.refresh = Button(self.main_win, text="Refresh", command=self.run)
        self.refresh.pack()


    def run(self):
        self.get_counter_per_iface()
        for iface, iface_info in self.output_dict.items():
            output_bytes, input_bytes = iface_info
            self.ifaces_data[iface].set( f"{iface}:\nInput Bytes: {input_bytes}\nOutput Bytes: {output_bytes}")


    def get_counter_per_iface(self)->Dict[str, Tuple[str, str]]:
        info_dict = psutil.net_io_counters(pernic=True)
        for iface, iface_info in info_dict.items():
            self.output_dict[iface] = ( iface_info.bytes_sent, iface_info.bytes_recv)
        self.output_dict 



def main():
    root_window = Tk()
    application = IfaceCounters(root_window)
    root_window.mainloop()


if __name__ == "__main__":
    main()
