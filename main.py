import os
import re
import datetime


def main_proc():
    # 本文作成
    line_body = edit_line_body(get_hello_text(get_time()))

    # development commit 用コメント
    line_notify_api = "api_url"

    # 動作確認用 本番時は消す
    print(line_body)


# 現在時間の取得
def get_time():
    now = datetime.datetime.now()
    return now.strftime("%H:%M:%S")


def get_hello_text(now_times):
    if now_times >= '09:00' and now_times <= "10:30":
        hello_text = "おはようございます。"
    else:
        hello_text = "お疲れ様です。"
    return hello_text


def edit_line_body(aisatsu):
    line1 = aisatsu + "\n"
    line2 = "message test" + "\n"

    body = line1 + line2
    return body


# メイン処理起動
main_proc()


