"""
这是一个学生成绩统计分析程序，用户可连续输入整数成绩，输入“结束”后，
程序自动统计并显示总人数、最高分、最低分、平均分、合格（≥60分）与优秀（≥90分）的人数和百分比；
若无输入则提示无数据。
"""
print("请输入学生成绩，输入“结束”停止录入")
scores = []


def main():
    while True:
        score = input("请输入学生成绩：")
        if score == "结束":
            break
        scores.append(int(score))
    print("总人数：", len(scores))
    print("最高分：", max(scores))
    print("最低分：", min(scores))
    print("平均分：", sum(scores) / len(scores))
    print("合格人数：", len([score for score in scores if score >= 60]))
    print("优秀人数：", len([score for score in scores if score >= 90]))
    print("合格率：", len(
        [score for score in scores if score >= 60]) / len(scores))
    print("优秀率：", len(
        [score for score in scores if score >= 90]) / len(scores))


if __name__ == "__main__":
    main()
