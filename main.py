import sys

max_pass = 3
generation = 0

if len(sys.argv) > 1 and sys.argv[1] == "query":
    global max_pass, generation
    generation += 1
    print(f"【链路】第{generation}代副本发起查询 | 剩余令牌：{max_pass}")
    print(max_pass)
    max_pass -= 1
    sys.exit()

child_code = '''import os
# 向主控main查询令牌
ret = os.popen("python main.py query").read().strip()
lines = ret.splitlines()
# 打印main返回的链路日志
for line in lines[:-1]:
    print(line)
rem = int(lines[-1])
if rem <= 0:
    print(f"第{rem}代：令牌耗尽，终止套娃")
else:
    # 读取自身源码
    with open(__file__,"r",encoding="utf-8") as f:
        src = f.read()
    new_name = f"child_{rem}.py"
    with open(new_name,"w",encoding="utf-8") as fw:
        fw.write(src)
    print(f"生成新副本：{new_name}，启动运行")
    os.system(f"python {new_name}")
'''

print("===== 分布式套娃奎因系统启动 =====")
with open("child_1.py","w",encoding="utf-8") as f:
    f.write(child_code)
print("main生成初代 child_1.py，开始执行")
os.system("python child_1.py")
print("===== 套娃链路全部结束 =====")
