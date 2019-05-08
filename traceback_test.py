import traceback
try:
    print(2 / 0)
except Exception as e:
    print(traceback.format_exc())
    print("hoge")
