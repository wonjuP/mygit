#-----------------------------------------------------------
# 화면 캡처 함수
#   - pathToSave: 저장경로 및 파일명
#   - fileName: 저장 파일명 
#   - typeExt: 이미지 파일 확장자
#-----------------------------------------------------------
def CaptureScreen(pathToSave, fileName, typeExt):
    import pyautogui
    import os
    from PIL import Image, ImageGrab
    
    if not os.path.exists(pathToSave):
        # 해당 경로가 없으면 생성
        os.makedirs(pathToSave)
    fileName = fileName+"."+typeExt
    pathToSave = os.path.join(pathToSave, fileName)
    print('pathToSave :', pathToSave)
    try:
       #box = (0, 0, 1920, 1080)
       box = None #Full Screenshot
       img = ImageGrab.grab(box)
       img.save(pathToSave, typeExt)
    
    except:
       try:
           myScreenshot = pyautogui.screenshot()
           myScreenshot.save(pathToSave)
           
       except:
           print("Image capture failed")
           
    return pathToSave
    
#------------------------------------------------------------