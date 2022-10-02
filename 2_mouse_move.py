import pyautogui

#절대 좌표로 마우스 이동
#pyautogui.moveTo(1000,100)   #지정한 위치로 마우스를 이동(가로x,세로y)
#pyautogui.moveTo(100,200,duration=0.25) #0.25초 동안 100,200 위치로 이동 

# pyautogui.moveTo(100,100,duration=0.5)
# pyautogui.moveTo(1000,100,duration=0.5)
# pyautogui.moveTo(1500,800,duration=0.5)

#상대 좌표로 마우스 이동(move->현재 커서가 있는 위치로 부터)
# pyautogui.moveTo(100,100,duration=0.5)
# print(pyautogui.position())     #마우스의 좌표 출력
# pyautogui.move(100,100,duration=0.5)
# print(pyautogui.position())     #마우스의 좌표 출력
# pyautogui.move(100,100,duration=0.5)
# print(pyautogui.position())     #마우스의 좌표 출력

#마우스 현재위치 좌표 찍기
p=pyautogui.position()
print(p.x,p.y)
print(p[0],p[1])