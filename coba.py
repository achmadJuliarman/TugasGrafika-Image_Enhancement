import cv2 as cv
import numpy as np

def apply_sepia(img):
    # Matrix transformasi untuk konversi ke skala warna sepia
    sepia_matrix = np.array([[0.393, 0.769, 0.189],
                            [0.349, 0.686, 0.168],
                            [0.272, 0.534, 0.131]])

    # Aplikasikan transformasi ke setiap piksel dalam citra
    sepia_img = cv.transform(img, sepia_matrix)

    # Batasi nilai transformasi agar tetap dalam rentang [0, 255]
    sepia_img = np.clip(sepia_img, 0, 255).astype(np.uint8)

    return sepia_img

# Load citra
img = cv.imread('saitama.png')
img = cv.resize(img, (700,400))
assert img is not None, "Citra tidak terbaca"

# Konversi BGR ke RGB
img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)

# Aplikasikan efek sepia
sepia_result = apply_sepia(img_rgb)

# Konversi kembali ke BGR
sepia_result_bgr = cv.cvtColor(sepia_result, cv.COLOR_RGB2BGR)

# Tampilkan citra asli dan citra dengan efek sepia
cv.imshow('Citra Asli', img)
cv.imshow('Citra dengan Efek Sepia', sepia_result_bgr)
cv.waitKey()