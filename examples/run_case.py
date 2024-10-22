import cmd_register as cmd

# 註冊一個裝飾器函數, 其容器為run_funcs
run_funcs = []
run_register = cmd.new_register(run_funcs, lambda f: print(f"run: {f.__name__}"))

@run_register
def say():
    print("hello")

@run_register
def bar():
    print("world")

if __name__ == '__main__':
    say()
    while 1:
        print("Please select the function number to execute:")
        print("0 exit")
        for idx, func in enumerate(run_funcs, 1):
            print(f"{idx} {func.__name__}")

        choice = input(": ")

        if int(choice) <= 0:
            exit(int(choice))
        try:
            choice_num = int(choice)
            if 1 <= choice_num <= len(run_funcs):
                run_funcs[choice_num - 1]()
            else:
                print("Invalid selection")
        except ValueError:
            print("Invalid input, please enter a number")
