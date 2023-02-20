from PIL import ImageGrab
import numpy as np
import cv2
import sounddevice as sd
from scipy.io.wavfile import write

# 設定錄音參數
fs = 44100  # 取樣頻率
duration = 60 # 持續時間

# 創建 OpenCV 視窗
cv2.namedWindow('screen', cv2.WINDOW_NORMAL)

# 獲取螢幕大小
image = ImageGrab.grab()
width, height = image.size

# 設定影片編碼器
fourcc = cv2.VideoWriter_fourcc(*'XVID')

# 創建影片寫入器
video = cv2.VideoWriter('test.avi', fourcc, 25, (width, height))

# 開始錄音
print("Start recording...")
myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=2)

while True:
    # 獲取螢幕畫面
    img_rgb = ImageGrab.grab()
    img_bgr = cv2.cvtColor(np.array(img_rgb), cv2.COLOR_RGB2BGR)
    
    # 寫入畫面
    video.write(img_bgr)
    
    # 顯示畫面
    cv2.imshow('screen', img_bgr)

    # 如果按下 q 鍵，則結束迴圈
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 結束錄音
sd.wait()
sd.stop()
write('output.wav', fs, myrecording)

# 釋放影片寫入器，關閉 OpenCV 視窗
video.release()
cv2.destroyAllWindows()

# 完成
print("Done!")
