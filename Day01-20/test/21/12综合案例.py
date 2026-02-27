"""
综合案例：答题闯关挑战赛
关卡设置：一共 3 个关卡，每个关卡只有一道题。答对进入下一关，3 关都通过则挑战成功。
答题规则：
  答错可重试，每道题有 3 次回答机会，若 3 次均答错，则挑战失败，游戏自动结束。
  如果用户输入为空，则提示重新作答，且不浪费回答机会。
  如果用户输入字母 q，则直接退出游戏。
"""


def main():
    print("欢迎来到答题闯关挑战赛！")
    print("请依次回答以下问题，答对进入下一关，3关都通过则挑战成功。")
    print("答错可重试，每道题有 3 次回答机会，若 3 次均答错，则挑战失败，游戏自动结束。")
    print("如果用户输入为空，则提示重新作答，且不浪费回答机会。")
    print("如果用户输入字母 q，则直接退出游戏。")
    print("请开始作答：")
    # 题目与答案
    ques1, ans1 = 'Python中用于输出的函数是？', 'print'
    ques2, ans2 = 'Python中用于表示逻辑“并且”的关键字是？', 'and'
    ques3, ans3 = 'Python属于编译型还是解释型？', '解释型'
    max_level = 3
    max_try_times = 3
    is_playing = True

    for level in range(1, max_level + 1):

        print(f"**************第 {level} 关**************")
        if (level == 1):
            question, answer = ques1, ans1
        elif (level == 2):
            question, answer = ques2, ans2
        elif (level == 3):
            question, answer = ques3, ans3
        # 记录当前尝试次数
        try_times = 0
        while try_times < max_try_times:
            print(question)
            user_input = input("请输入答案：")
            if answer == user_input:
                print("✅回答正确!!!")
                break
            elif answer == "":
                print("⚠ 您输入的答案为空，请重新作答。")
                continue
            elif user_input == "q":
                print("👋 您已退出游戏。")
                is_playing = False
                break
            else:
                # 计算剩余次数
                remaining_times = max_try_times - try_times - 1
                if remaining_times > 0:
                    print(f"⚠ 回答错误，请重新作答。您还有 {remaining_times} 次机会。")
                else:
                    print(f'😢挑战失败，本题的正确答案是：{answer}，游戏结束！')
                    is_playing = False
                    break
        # 每次进入下一关以前，看一下is_playing，如果is_playing为False，则退出作答，反之可以继续答题
        if not is_playing:
            break
    if is_playing:
        print("🎉🎉🎉恭喜您！全部通关！🎉🎉🎉")


if __name__ == '__main__':
    main()
