import pandas as pd

def human_readable_csv():
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



def read(filename: str) -> pd.DataFrame:
    extension = filename.split('.')[1]
    if extension == "csv":
        pass # TODO
    elif extension == "qif":
        pass # TODO
    elif extension == "ofc":
        pass # TODO
    elif extension == "ofx":
        pass # TODO



def read_csv(filename: str) -> pd.DataFrame:
    return pd.read_csv("data/data_0.csv", sep=';', names=["date", "value", "type", "none", "to", "from", "none2", "liquidity_type"])
# read qif function
# read ofc function
# read ofx function


"""
function: restructure_data
This function takes in a dataframe and cleans it up to make it what subsequent code will expect. The input dataframe must have the following columns : "date", "value", "type", "to", "from", "liquidity_type". The output dataframe must have the following columsn : ""
params:
- dataframe : pd.DataFrame
out:
- pd.DataFrame
"""
def restructure_data(dataframe: pd.DataFrame) -> pd.DataFrame:
    # get dates from data
    data = []
    for d, v, t, i, o, l in zip(dataframe['date'], dataframe['value'], dataframe['type'], dataframe['from'], dataframe['to'], dataframe['liquidity_type']):
        if pd.notna(d):
            dates = d 
        else:
            dates = "None"
        if pd.notna(v):
            values = v 
        else:
            values = 0
        if pd.notna(t):
            types = t 
        else:
            types = "Unknown"
        if l == "Liquide":
            liquidity = True 
        else:
            liquidity = False
        if pd.notna(i):
            notes = i
        elif pd.notna(o):
            notes = o
        else:
            notes = "Unknown"
        data.append((dates, values, types, liquidity, notes))
            
    #print(dataframe)
    print(dates)
    
    clean_data = pd.DataFrame(data=data, columns=["date", "types", "value", "note", "is_cash"])
    print(clean_data)
    return clean_data
