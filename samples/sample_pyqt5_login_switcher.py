import sys
from PyQt5.QtWidgets import QApplication, QDialog
from components.activation_window import ActivationWindow
from components.login_window import LoginWindow

def main():
    app = QApplication(sys.argv)

    # 创建激活窗口和登录窗口的实例
    activation_window = ActivationWindow()
    login_window = LoginWindow()

    # 设置信号和槽以实现窗口间的切换
    activation_window.switch_to_login_signal.connect(login_window.show)
    login_window.switch_to_activation_signal.connect(activation_window.show)

    current_window = activation_window
    current_window.show()  # 初始显示激活窗口

    # 循环显示窗口，直到任一窗口被接受
    while True:
        result = current_window.exec_()
        if result == QDialog.Accepted:
            # 确保关闭两个窗口
            activation_window.close()
            login_window.close()
            
            break  # 任一窗口接受时继续执行
        
        if current_window.is_closed:
            print("窗口被关闭")
            sys.exit()  # 用户关闭窗口，退出程序

        # 切换窗口
        if current_window is activation_window:
            current_window = login_window
        else:
            current_window = activation_window

    # 运行应用程序主循环
    print("程序正常退出")
    sys.exit()

if __name__ == "__main__":
    main()
