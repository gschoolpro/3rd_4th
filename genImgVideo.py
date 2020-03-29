# -*- coding: utf-8 -*-
# モジュールのインポート
import os
import cv2
import numpy as np

# 画像のサイズ
IMG_SIZE = 512
# ブロックのサイズ
BLOCK_SIZE = 64

# 画像の出力ディレクトリ
img_outdir = './gen_img'
# ディレクトリを作成
os.makedirs(img_outdir)

# 画像を順番に追加していくリスト
outimg_files = []
# 画像ファイル名用カウント変数
img_count = 0


# 画像生成の処理（左上から右下）
for h in range(0, IMG_SIZE, BLOCK_SIZE):
    for w in range(0, IMG_SIZE, BLOCK_SIZE):
        # 画像ファイル名用カウント
        img_count = img_count + 1

        # サイズ IMG_SIZE x IMG_SIZE の白塗り画像を生成
        img = np.empty((IMG_SIZE, IMG_SIZE))
        img.fill(255)

	    # BLOCK_SIZE分だけ白塗り画像に書き込む
        img[h:h+BLOCK_SIZE, w:w+BLOCK_SIZE] = np.full((BLOCK_SIZE, BLOCK_SIZE), 80)

	    # １部分色を変えた画像の出力
        outimg_file = '{}/{:05d}.png'.format(img_outdir, img_count)
        cv2.imwrite(outimg_file, img)

        outimg_files.append(outimg_file)

# 画像生成の処理（右下から左上）
for h in range(IMG_SIZE, 0, -BLOCK_SIZE):
    for w in range(IMG_SIZE, 0, -BLOCK_SIZE):
        # 画像ファイル名用カウント
        img_count = img_count + 1

        # サイズ IMG_SIZE x IMG_SIZE の白塗り画像を生成
        img = np.empty((IMG_SIZE, IMG_SIZE))
        img.fill(255)

    	# BLOCK_SIZE分だけ白塗り画像に黒を書き込む
        img[h-BLOCK_SIZE:h, w-BLOCK_SIZE:w] = np.zeros((BLOCK_SIZE, BLOCK_SIZE))

        # １部分色を変えた画像の出力
        outimg_file = '{}/{:05d}.png'.format(img_outdir, img_count)
        cv2.imwrite(outimg_file, img)

        outimg_files.append(outimg_file)

# 保存する動画の設定
fourcc = cv2.cv.CV_FOURCC(*'XVID')
video = cv2.VideoWriter('genImgVideo.avi', fourcc, 20.0, (IMG_SIZE, IMG_SIZE))

# 画像をつなげる処理
for img_file in outimg_files:
    img = cv2.imread(img_file)
    video.write(img)

video.release()
