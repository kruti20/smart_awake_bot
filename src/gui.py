import tkinter as tk
from threading import Thread
from src.activity_simulator import simulate_activity, stop_activity

class AwakeGUI:

    def __init__(self):

        self.root = tk.Tk()
        self.root.title("Smart Awake Bot")
        self.root.geometry("500x300")

        self.interval_label = tk.Label(self.root, text="Interval (seconds)")
        self.interval_label.pack()

        self.interval_entry = tk.Entry(self.root)
        self.interval_entry.insert(0, "300")
        self.interval_entry.pack()

        self.start_button = tk.Button(self.root, text="Start", command=self.start)
        self.start_button.pack(pady=10)

        self.stop_button = tk.Button(self.root, text="Stop", command=self.stop)
        self.stop_button.pack()

    def start(self):
        interval = int(self.interval_entry.get())

        self.thread = Thread(target=simulate_activity, args=(interval,))
        self.thread.start()

    def stop(self):
        stop_activity()
        self.root.destroy()

    def run(self):
        self.root.mainloop()