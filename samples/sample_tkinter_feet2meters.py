from tkinter import *
from tkinter import ttk

"""
程序的主入口
"""
def main():
    # 新建一个窗口
    window = Tk()
    # 设置窗口标题
    window.title("Feet to Meters")
    # 设置窗口的大小
    window.geometry("800x600")

    # 新建一个框架
    mainframe = ttk.Frame(window, padding="3 3 12 12")
    # 设置框架的位置
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    # 设置框架的大小
    window.columnconfigure(0, weight=1)
    window.rowconfigure(0, weight=1)

    # 新建一个输入框
    feet = StringVar()
    feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
    feet_entry.grid(column=2, row=1, sticky=(W, E))

    # 新建一个标签
    meters = StringVar()
    ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))

    # 新建一个按钮
    ttk.Button(mainframe, text="Calculate", command=lambda: calculate(feet, meters)).grid(column=3, row=3, sticky=W)

    # 新建三个标签
    ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
    ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
    ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

    # 设置所有的子组件的外边距
    for child in mainframe.winfo_children(): 
        child.grid_configure(padx=5, pady=5)

    # 设置焦点（光标）在输入框上
    feet_entry.focus()
    window.bind("<Return>", lambda event: calculate(feet, meters))

    window.mainloop()

"""
计算输入的英尺数对应的米数
"""
def calculate(feet, meters):
    try:
        value = float(feet.get())
        meters.set(int(0.3048 * value * 10000.0 + 0.5) / 10000.0)
    except ValueError:
        pass
"""
程序的执行入口
"""
if __name__ == "__main__":
    main()