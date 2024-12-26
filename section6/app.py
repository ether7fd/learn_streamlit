from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials

from array import array
import os
from PIL import Image
import sys
import time

import json

# KeyとEndpointの読み込み
with open('secret.json') as f:
    secret = json.load(f)

KEY = secret['KEY']
ENDPOINT = secret['ENDPOINT']

# KeyとEndpointを渡して、computervision_clientを取得する
computervision_client = ComputerVisionClient(ENDPOINT, CognitiveServicesCredentials(KEY))

# 画像内のタグを取得
def get_tags(filepath):
    # filepathの画像を取得する
    local_image = open(filepath, "rb")

    # タグの一覧を取得
    tags_result = computervision_client.tag_image_in_stream(local_image)
    tags = tags_result.tags
    tags_name = []
    # タグ名の一覧を格納
    for tag in tags:
        tags_name.append(tag.name)
        
    return tags_name


# 画像内の物体情報を取得
def detect_objects(filepath):
    local_image = open(filepath, "rb")

    # 画像内のオブジェクト一覧を取得
    detect_objects_results = computervision_client.detect_objects_in_stream(local_image)
    objects = detect_objects_results.objects
    return objects


import streamlit as st
from PIL import ImageDraw
from PIL import ImageFont

# タイトル表示
st.title('物体検出アプリ')

# ファイルのアップロード
uploaded_file = st.file_uploader('Choose an image...', type=['jpg','png'])
if uploaded_file is not None:
    img = Image.open(uploaded_file)
    img_path = f'img/{uploaded_file.name}'
    img.save(img_path)
    objects = detect_objects(img_path)

    # 描画する
    draw = ImageDraw.Draw(img)
    for object in objects:
        # 画像内のオブジェクトの座標、大きさ情報
        ## オブジェクトの左上x座標
        x = object.rectangle.x
        ## オブジェクトの左上y座標
        y = object.rectangle.y
        ## オブジェクトの幅
        w = object.rectangle.w
        ## オブジェクトの高さ
        h = object.rectangle.h
        # オブジェクト名の取得
        caption = object.object_property

        font = ImageFont.truetype(font='./Helvetica 400.ttf', size=50)
        text_w, text_h = draw.textsize(caption, font=font)

        # 矩形を描画
        draw.rectangle([(x, y), (x+w, y+h)], fill=None, outline='green', width=5)
        draw.rectangle([(x, y), (x+text_w, y+text_h)], fill='green')
        # オブジェクト名の描画
        draw.text((x, y), caption, fill='white', font=font)

    st.image(img)

    # タグの一覧を表示
    tags_name = get_tags(img_path)
    tags_name = ', '.join(tags_name)
    st.markdown('**認識されたコンテンツタグ**')
    st.markdown(f'> {tags_name}')    