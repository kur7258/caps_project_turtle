import tkinter as tk # Tkinter
from PIL import ImageTk, Image
from numpy import size # Pillow
import pafy
import cv2

class Show_video():
    def __init__(self):
        # GUI 설계
        self.win = tk.Tk() # 인스턴스 생성

        self.win.title("자세 교정 방법") # 제목 표시줄 추가
        self.win.resizable(False, False) # x축, y축 크기 조정 비활성화

        # 라벨 추가
        self.lbl = tk.Label(self.win, text="자세 개선 방법", font=('맑은 고딕',25,'bold'))
        self.lbl.grid(row=0, column=0) # 라벨 행, 열 배치

        # 프레임 추가
        self.frm = tk.Frame(self.win, bg="white", width=720, height=480) # 프레임 너비, 높이 설정
        self.frm.grid(row=1, column=0) # 격자 행, 열 배치

        # 라벨1 추가
        self.lbl1 = tk.Label(self.frm)
        self.lbl1.grid()
        
        self.url = "https://www.youtube.com/watch?v=jD5EwJncYLw"
        self.video = pafy.new(self.url)

        self.best = self.video.getbest(preftype="mp4")
        print("best resolution : {}".format(self.best.resolution))

        self.cap = cv2.VideoCapture(self.best.url) 


    def video_play(self):
        ret, frame = self.cap.read() # 프레임이 올바르게 읽히면 ret은 True
        if not ret:
            self.cap.release() # 작업 완료 후 해제
            return
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(frame) # Image 객체로 변환
        imgtk = ImageTk.PhotoImage(image=img) # ImageTk 객체로 변환
        # OpenCV 동영상
        self.lbl1.imgtk = imgtk
        self.lbl1.configure(image=imgtk)
        self.lbl1.after(10, self.video_play)

    def start_gui(self):
        self.video_play()
        self.win.mainloop() #GUI 시작