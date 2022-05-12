from fileinput import filename
import os

# 関数 neg.txtにbadimgフォルダーから列挙したファイル名を書き込む
def generate_negative_file():
    with open('./cv/neg.txt', 'w') as file:

        for file_name in os.listdir('./cv/badimg'):
            file.write('badimg/' + file_name + '\n')


generate_negative_file()

