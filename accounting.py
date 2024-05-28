import pandas as pd

def human_readable():
    f = open("accounting/data/data_0.csv", "r")
    data = f.readlines()
    f.close()

    text = ""
    for sentence in data:
        replaced = sentence.replace(";", ",")
        text += replaced + "\n"
        print(replaced)

    f = open("accounting/data/data.csv", "w")
    f.writelines(text)

"""
data.replace(';', ',')
print(data)

new_data = pd.read_csv("accounting/data/data_0.csv")

print(new_data.head)
"""
