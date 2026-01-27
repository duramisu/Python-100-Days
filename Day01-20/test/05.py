"""
bmi 计算器
"""
def bmi_calculator():
    height = float(input("请输入您的身高(cm): "))

    weight = float(input("请输入您的体重(公斤): "))

    bmi = weight / (height / 100) ** 2

    print(f"{bmi = :.1f}")

    if 18.5 <= bmi < 24:
        print("你的身材很棒！")

"""
状态码判定测试
"""
def status_code_test():
    status_code = int(input("请输入状态码: "))
    match status_code:
        case 200:
            description = "OK"
            print("请求成功")
        case 401:
            description = "Unauthorized"
            print("未授权访问")
        case 404:
            description = "Not Found"
            print("请求资源不存在")
        case 500:
            description = "Internal Server Error"
            print("服务器内部错误")
        case _:
            description = "Unknown Error"
            print("未知错误")
    print("状态码描述："+description)

"""
要求：
如果输入的成绩在90分以上（含90分），则输出A；
输入的成绩在80分到90分之间（不含90分），则输出B；
输入的成绩在70分到80分之间（不含80分），则输出C；
输入的成绩在60分到70分之间（不含70分），则输出D；
输入的成绩在60分以下，则输出E。
"""
def score_to_grade():
    score = int(input("请输入成绩: "))
    if score >= 90:
        print("A")
        grade = "优秀"
    elif score >= 80:
        print("B")
        grade = "良好"
    elif score >= 70:
        print("C")
        grade = "中等"
    elif score >= 60:
        print("D")
        grade = "及格"
    elif score < 60:
        print("E")
        grade = "不及格"
    print(f'{ grade = }')


"""
主函数
"""
def main():
    score_to_grade()


"""
测试运行
"""
if __name__ == "__main__":
    main()
