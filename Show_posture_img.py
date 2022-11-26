import tkinter as tk # Tkinter
from PIL import ImageTk, Image
from numpy import size # Pillow
import pafy
import cv2

class Show_img():
    def __init__(self):
        # GUI 설계
        self.win = tk.Tk() # 인스턴스 생성

        self.win.title("올바른 자세") # 제목 표시줄 추가
        self.win.resizable(False, False) # x축, y축 크기 조정 비활성화

        # 라벨 추가
        self.lbl = tk.Label(self.win, text="올바른 자세", font=('맑은 고딕',25,'bold'))
        self.lbl.grid(row=0, column=0) # 라벨 행, 열 배치

        # # 프레임 추가
        # self.frm = tk.Frame(self.win, bg="white", width=720, height=480) # 프레임 너비, 높이 설정
        # self.frm.grid(row=1, column=0) # 격자 행, 열 배치

        # 이미지 추가
        self.img = tk.PhotoImage(file="images/good_posture.gif")

        # 라벨1 추가
        self.lbl1 = tk.Label(self.win, image=self.img)
        self.lbl1.grid()
        
    def start_gui(self):
        self.win.mainloop() #GUI 시작