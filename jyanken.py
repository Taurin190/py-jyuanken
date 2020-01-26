# coding: utf-8
import random


def show_input_error():
    print("入力値は1~3の数字で入力してください。")
    exit(1)


def get_selection_str(num):
    if num == 1:
        return "グー"
    elif num == 2:
        return "チョキ"
    elif num == 3:
        return "パー"
    else:
        exit(1)


print("最初はグー、じゃんけん...")
print("（グー 1, チョキ 2, パー 3）")

selection = input()
if selection != "1" and selection != "2" and selection != "3":
    show_input_error()
selection_num = int(selection)
enemy_selection_num = random.randint(1, 3)
result_num = (selection_num - enemy_selection_num) % 3

print("あなた：" + get_selection_str(selection_num))
print("あいて：" + get_selection_str(enemy_selection_num))

if result_num == 0:
    print("「引き分けです。」")
elif result_num == 1:
    print("「あなたの負けです。」")
elif result_num == 2:
    print("「あなたの勝ちです。」")
