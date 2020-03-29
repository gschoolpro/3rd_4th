# -*- coding: utf-8 -*-
# モジュールのインポート
import os
import cv2
import numpy as np
from picamera import PiCamera
from time import sleep

# 画像のサイズ
IMG_SIZE = 512
# 撮影する回数
TOTAL = 20
# 撮影から撮影までの行う間隔
delay = 0.1

# 画像の出力ディレクトリ
img_outdir = './cam_img'
# ディレクトリを作成
os.makedirs(img_outdir)

# 画像を順番に追加していくリスト
outimg_files = []
# 画像ファイル名用カウント変数
img_count = 0

# カメラモジュールの読み込み
camera = PiCamera()

# TOTAL枚 分の写真撮影の処理
for h in range(0, TOTAL):
    # 画像ファイル名用カウント
    img_count = img_count + 1

    # 撮影
    camera.resolution = (IMG_SIZE, IMG_SIZE)
    camera.start_preview()
    sleep(delay)
    outimg_file = '{}/{:05d}.png'.format(img_outdir, img_count)
    camera.capture(outimg_file)
    camera.stop_preview()

    # 撮影した写真をリストへ追加
    outimg_files.append(outimg_file)

# 保存する動画の設定
fourcc = cv2.cv.CV_FOURCC(*'XVID')
video = cv2.VideoWriter('camImgVideo.avi', fourcc, 8.0, (IMG_SIZE, IMG_SIZE))

# 画像をつなげる処理
for img_file in outimg_files:
    img = cv2.imread(img_file)
    video.write(img)

video.release()
