import tkinter as tk
from tkinter import messagebox


def calc_area():
    try:
        top = float(entry_top.get())
        bottom = float(entry_bottom.get())
        height = float(entry_height.get())
        area = (top + bottom) * height / 2
        label_result.config(text=f"梯形的面積: {area:.2f} 平方公分")
    except ValueError:
        messagebox.showerror("輸入錯誤", "請輸入有效的數字")


root = tk.Tk()
root.title("梯形面積計算機")
root.geometry("300x200")

tk.Label(root, text="上底 (公分):").pack()
entry_top = tk.Entry(root)
entry_top.pack()

tk.Label(root, text="下底 (公分):").pack()
entry_bottom = tk.Entry(root)
entry_bottom.pack()

tk.Label(root, text="高 (公分):").pack()
entry_height = tk.Entry(root)
entry_height.pack()

tk.Button(root, text="計算面積", command=calc_area).pack(pady=5)

label_result = tk.Label(root, text="")
label_result.pack()

root.mainloop()
