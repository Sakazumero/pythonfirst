import tkinter as tk
import random
from datetime import datetime

# ことわざやイディオムのリスト
idioms = [
    "A stitch in time saves nine.",
    "Better late than never.",
    "Curiosity killed the cat.",
    "Don't put all your eggs in one basket.",
    "Every cloud has a silver lining."
]

# 現在の日付を取得し、その日付の基づいてことわざを選ぶ
def get_todays_idiom():
    today = datetime.now().day
    index = today % len(idioms)
    return idioms[index]

# GUIをセットアップ
def setup_gui(root):
    root.title("Daily Idiom")
    root.geometry("400x200")
    
    idiom = get_todays_idiom()
    idiom_label = tk.Label(root, text=idiom, font=("Arial", 14), wraplength=350)
    idiom_label.pack(expand=True)

# メイン関数
def main():
    root = tk.Tk()
    setup_gui(root)
    root.mainloop()

if __name__ == "__main__":
    main()
