import random

def guess_the_number():
    # 生成一个1到100之间的随机数
    secret_number = random.randint(1, 100)
    
    print("欢迎参加猜数游戏！")
    print("我已经选好了一个1到100之间的整数。你的任务是猜出这个数字。")

    attempts = 0

    while True:
        # 获取玩家的猜测
        guess = int(input("请输入你的猜测："))

        # 猜测次数加1
        attempts += 1

        # 判断猜测是否正确
        if guess == secret_number:
            print(f"恭喜你，猜对了！你用了 {attempts} 次尝试。")
            break
        elif guess < secret_number:
            print("猜的数字太小了，请再试一次。")
        else:
            print("猜的数字太大了，请再试一次。")


guess_the_number()
