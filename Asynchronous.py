import asyncio
import json
from datetime import datetime

async def task2(names, prices):
    with open("data_2.json", "a") as files:
        files.write(names)




async def task1():
    with open('data_1.json', 'r') as file:
        data = json.load(file)
        print('task_1')
        names = []
        prices = []
        for i in data["course"]:
            names.append(i["name"])
            prices.append(i["price"])



# async def task3():
#     await asyncio.gather(task1())
#     await asyncio.sleep(15)
#     print("Task 3 completed")
#
# async def task4():
#     await asyncio.gather(task2())
#     await asyncio.sleep(4)
#
#     print("Task 4 completed")
#
# async def main():
#     await asyncio.gather(task4(), task1(), task2(), task3())
#
# if __name__ == "__main__":
#     print(datetime.now().time())
#     asyncio.run(main())
#     print(datetime.now().time())
#
#

#
# import time
# from datetime import datetime
#
# def task_4():
#     time.sleep(7)
#     return "Task 4 "
#
#
# def task_3():
#     time.sleep(2)
#     return "Task 3 "
#
#
# def task_2():
#     time.sleep(5)
#     return "Task 2 "
#
#
# def task_1():
#     time.sleep(2)
#     return "Task 1 "
#
#
# def main():
#     print(task_4())
#     print(task_1())
#     print(task_3())
#     print(task_2())
#
#
# if __name__ == "__main__":
#     print(datetime.now().time())
#     main()
#     print(datetime.now().time())
