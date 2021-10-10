import time
import webbrowser
i = int(input("Input number: "))
typee = "bar"

resulty = []

result = i + 0

while result != 1:
    if (result % 2) != 0:
        result = (result * 3) + 1
    else:
        result = result / 2
    print(int(result))
    resulty.append(result)

r = []
for i in range(len(resulty)):
    r.append('%20')

webbrowser.open("https://quickchart.io/chart?title=3N%2B1&c={type:" + f'"{typee}"' + ",data:{labels:" + f"{r}" +" , datasets:[{label:'3N%2B1',data:" + f"{resulty}" + "}]}}") # Also makes a nice chart.
