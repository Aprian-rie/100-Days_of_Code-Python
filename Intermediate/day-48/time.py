import time
# def delay():
#     for i in range(4):
#         print(i)
#         if i == 2:
#             print("2 is reached maboi")
#         time.sleep(5)
#
#
# delay()
# #
# print("2 is reached")
timeout = time.time() + 60
while True:
    print(time.time())
    if time.time() > timeout:
        break
