import tkinter as tk
import time

def update_clock():
    current_time = time.strftime("%H:%M:%S")
    clock_label.config(text=current_time)
    clock_label.after(1000, update_clock)  # 每隔1000毫秒 (1秒) 更新一次

# 创建Tkinter窗口
root = tk.Tk()
root.title("时钟")

# 创建一个标签用于显示时间
clock_label = tk.Label(root, font=("Helvetica", 48), bg="#ffffff", fg="#2476bf")
clock_label.pack(anchor='center', fill='both', expand=True)

# 初始化时钟更新
update_clock()

# 运行Tkinter事件循环
root.mainloop()
