import pyautogui

# pyautogui.sleep(3)  #3초 대기
# print(pyautogui.position())

# pyautogui.click(1180,16,duration=1)     #마우스 클릭
# pyautogui.mouseDown()                   #마우스 클릭 누루고 있기
# pyautogui.mouseUp()                     #마우스 클릭 떼기

# pyautogui.doubleClick()         #더블클릭
# pyautogui.click(clicks=500)     #클릭이 500번


# pyautogui.rightClick()  #마우스 우클릭
# pyautogui.middleClick() #마우스 횔 클릭

#드래그 업 다운(1)
# pyautogui.moveTo(329,416,duration=0.5)   
# pyautogui.mouseDown() 
# pyautogui.moveTo(839,686,duration=0.5)      
# pyautogui.mouseUp() 

#드래그 업 다운(2)
# pyautogui.moveTo(381,208,duration=0.5)
# pyautogui.drag(100,208,duration=0.5)      #현재 위치 기준으로 좌표로 드래그,duration값을 줘야댐(duration값을 주지 않으면 너무 빠른 동작으로 안됨)
# pyautogui.dragTo(100,100,duration=0.5)      #절대 좌표로 드래그

#마우스 스크롤
pyautogui.scroll(300)   #양수이면 위 방향으로 300만큼 스크롤
pyautogui.scroll(-800)   #음수이면 아래 방향으로 -800만큼 스크롤




