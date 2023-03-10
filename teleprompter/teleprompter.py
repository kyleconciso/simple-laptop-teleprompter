#!/usr/bin/env python3

import argparse
import threading
import tkinter as tk
from pynput import keyboard

class TeleprompterGUI:
    def __init__(self, height: int = 15):
        self.root = tk.Tk()
        self.root.title("Teleprompter")
        self.root.geometry("%dx%d+%d+%d" % (self.root.winfo_screenwidth(), height, 0, 0))
        self.root.overrideredirect(True)
        self.root.wm_attributes("-topmost", True)
        self.label = tk.Label(self.root, text="Welcome! Press left and right arrows to scroll through the text. Prese ESC to terminate. ", font=("Helvetica", height), fg="white", bg="black")
        self.label.pack()

    def update_text(self, new_text: str):
        self.label.config(text=new_text)
        self.label.update()

    def start(self):
        self.root.mainloop()

class Teleprompter:
    def __init__(self, script_file: str, phrase_length: int = 3, height: int = 15):
        self.script_file = script_file
        self.phrase_length = phrase_length
        self.phrases = []
        self.current_phrase = 0
        self.welcome = False
        self.gui = TeleprompterGUI(height)

    def on_press(self, key):
        if self.welcome == False and (key == keyboard.Key.left or key == keyboard.Key.right):
            self.welcome = True
            self.gui.update_text(self.phrases[self.current_phrase])

        elif key == keyboard.Key.left and self.current_phrase > 0:
            self.current_phrase -= 1
            self.gui.update_text(self.phrases[self.current_phrase])

        elif key == keyboard.Key.right and self.current_phrase < (len(self.phrases)-1):
            self.current_phrase += 1
            self.gui.update_text(self.phrases[self.current_phrase])

        elif key == keyboard.Key.home:
            self.current_phrase = 0
            self.gui.update_text(self.phrases[self.current_phrase])

        elif key == keyboard.Key.end:
            self.current_phrase = len(self.phrases)-1
            self.gui.update_text(self.phrases[self.current_phrase])

        elif key == keyboard.Key.esc:
            self.gui.root.destroy()
            self.listener.stop()
            
    def update_text(self, new_text: str):
        self.label.config(text=new_text)
        self.label.update()

    def start_listener(self):
        self.listener = keyboard.Listener(on_press=self.on_press)
        self.listener.start()

    def split_text(self, words: str):
        words = words.replace('\n', ' ').split()
        return [ ' '.join(words[i:i+self.phrase_length]) for i in range(0, len(words), self.phrase_length)]

    def start(self):
        with open(self.script_file, 'r') as file:
            words = file.read()
        self.phrases = self.split_text(words)     
        thread = threading.Thread(target=self.start_listener)
        thread.start()
        self.gui.start()

if __name__ == '__main__':
    print("Welcome! Press left and right arrows to scroll through the text. Press ESC to terminate.")
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--script", type=str, default='script.txt', help="script file to be used for teleprompter")
    parser.add_argument("-p", "--phrase", type=int, default=3, help="phrase length for teleprompter")
    parser.add_argument("-H", "--height", type=int, default=15, help="height of the teleprompter window")
    args = parser.parse_args()
    teleprompter = Teleprompter(args.script, args.phrase, args.height)
    teleprompter.start()