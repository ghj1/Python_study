import cv2
import tkinter as tk
from PIL import Image, ImageTk,ImageOps
from keras.models import load_model
import numpy as np
from functools import partial
import speech_recognition as sr
from gettext import gettext
import os
import time
from playsound import playsound
from tkinter import ttk 


model = load_model('keras_model.h5')
model2 = load_model('nose_model.h5') # 모델 읽어오기
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
window = tk.Tk()
window.geometry("1500x550")
window.title('《Honey》 『꿀』 관상')
window.configure(bg='RoyalBlue4')
opencvFrame = tk.Frame(window)
opencvFrame.grid(row=0, column=0, padx=10, pady=2)
lmain = tk.Label(opencvFrame)
lmain.grid(row=0, column=0)
canvas = tk.Canvas(window, width = 493, height = 250)
img = ImageTk.PhotoImage(Image.open("무도관상.jpg"))
canvas.create_image(0, 0,anchor="nw",  image=img)
canvas.place(x=350,y =10)
canvas2 = tk.Canvas(window, width = 493, height = 249)
img2 = ImageTk.PhotoImage(Image.open("관상.jpg"))
canvas2.create_image(0, 0,anchor="nw",  image=img2)
canvas2.place(x=350,y =270)
# opencv 카메라 연결
cap = cv2.VideoCapture(0)
def show_frame():
    _, frame = cap.read()
    frame= frame[200:450,250:480]
    frame = cv2.flip(frame, 1)
    frame = cv2.resize(frame,(300,400))
    # 이미지 처리
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(10, show_frame) # 10마이크로 초 이후 show_frame 다시 불러움
def capture(): # 현재 웹캠 정보를 이미지로 저장하는 함수입니다.
    _, frame = cap.read()
    img_frame = frame 
    img_size = img_frame[200:450,250:480]
    cv2.imwrite('result/screenshot.jpg', img_size)
    print('저장됨')
def printfacetype(i): #관상 프로그램을 출력하는 함수입니다.
    global img, canvas,canvas2
    if os.path.isfile('voice_0.mp3') ==True:
        os.remove('voice_0.mp3')
    time.sleep(2)
    images = np.array(Image.open(i))
    size = (224, 224)
    image = cv2.resize(images, size)
    image = Image.fromarray(image)
    image = ImageOps.fit(image, size, Image.ANTIALIAS)
    image_array = np.asarray(image)
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
    data[0] = normalized_image_array
    prediction = model.predict(data)
    prediction2 = model2.predict(data)
    img = ImageTk.PhotoImage(Image.open("result/screenshot.jpg"))
    canvas.create_image(0, 0,anchor="nw",  image=img)
    #canvas.place(x=350,y =10)
    #canvas = tk.Canvas(window, width = 493, height = 249)
    num = prediction.argmax()
    num2 = prediction2.argmax() #모델 파일과 비교하여 가장 높은 값을 추출함.
    eye =['사자눈, 당신은 항상 앞으로 나아가는 성격입니다.\\n 호탕한 마음을 갖고 있지만 욕심을 낼수록 당신이 사랑하는 사람을 멀어지게 할 수 있습니다.','호랑이눈, 당신은 정의감이 넘치며 자존심이 강합니다. 정의의 사도처럼 행동하고 싶지만 그럴수록 힘들어집니다.','원앙눈, 당신은 재물복이 좋으며 부부 관계가 좋을 것입니다.\n 하지만 음란해지는 것을 경계하여야 합니다.\n','소눈, 당신은 인내심이 강하고 우직하면서도 인자한 성품을 지녔고, 타인에게 친절한 마음을 갖고 있습니다.','거북이눈, 정이 많고 신망이 두터워 신의를 져 버리지 않는 사람입니다. 때로는 손해를 볼 수도 있지만, 사람들이 알아줄 날이 올겁니다.']
    msg = eye[num]
    '''if  num == 0:
        msg = "사자눈, 당신은 항상 앞으로 나아가는 성격입니다. 호탕한 마음을 갖고 있지만 욕심을 낼수록 당신이 사랑하는 사람을 멀어지게 할 수 있습니다.\\n "
    elif num == 1:
        msg = "호랑이눈, 당신은 정의감이 넘치며 자존심이 강합니다. 정의의 사도처럼 행동하고 싶지만 그럴수록 힘들어집니다.\\n "
    elif num == 2:
        msg = "원앙눈, 당신은 재물복이 좋으며 부부 관계가 좋을 것입니다. 하지만 음란해지는 것을 경계하여야 합니다. \\n"
    elif num == 3:
        msg = "소눈, 당신은 인내심이 강하고 우직하면서도 인자한 성품을 지녔고, 타인에게 친절한 마음을 갖고 있습니다. \\n "
    else :
        msg = "거북이눈, 정이 많고 신망이 두터워 신의를 져 버리지 않는 사람입니다. 때로는 손해를 볼 수도 있지만, 사람들이 알아줄 날이 올겁니다. \\n"
    '''
    '''if  num2 == 0:
        msg2 = "용코, 당신은 아름다운 삶을 살 것이고 후세에도 좋은 영향을 줄 것입니다. 한 분야에서 성공할 수 있으니 하루하루 매순간 최선을 다하세요."
    else:
        msg2 = "마늘코, 당신은 사람들에게 인정받고 존경 받을 수 있습니다. 또한 형제 간의 우애가 좋습니다. 말년에 가장 행복한 인생을 살게 될 것입니다. "
    '''
    nose = ['용코, 당신은 아름다운 삶을 살 것이고 후세에도 좋은 영향을 줄 것입니다. \n한 분야에서 성공할 수 있으니 하루하루 매순간 최선을 다하세요.','마늘코, 당신은 사람들에게 인정받고 존경 받을 수 있습니다. 또한 형제 간의 우애가 좋습니다. 말년에 가장 행복한 인생을 살게 될 것입니다.']
    msg2= nose[num2]
    for i in range(1):
        text='당신의 눈은 %s ,당신의 코는 %s ' %(msg,msg2)
        tts= gettext(text,lang='ko')
        filename = 'C:/Users/PC021/voice_%d.mp3'%(i)
        time.sleep(3)
        tts.save(filename)
        print('file saved')
        time.sleep(5)
        playsound(filename,True)
        print('playing music')
        print(text)
        canvas2.create_text(0,0,anchor="nw",text=text)
show_frame()
button_1 = tk.Button(window, text = "얼굴 캡쳐", command = capture, bg= "AntiqueWhite3",
                                fg = "white",font =('gulim.ttc', 20), bd= 0 , relief = "ridge")
button_1.place(x = 30, y = 430) #button1은 캡처하는 버튼입니다.
button_2 = tk.Button(window,  text = "관상", command =partial(printfacetype,'result/screenshot.jpg'), backg = "gray19",
                                fg = "snow", font =('Courier', 20), bd = 0 ,relief = "groove")
button_2.place(x = 220, y = 430) #button2는 관상프로그램 실행 버튼입니다.
window.mainloop()