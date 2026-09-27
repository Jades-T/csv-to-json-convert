import pandas as pd

def main():
    """ Function that reads the csv file and generates the json file."""

    dataframe = pd.read_csv("people.csv")
    dataframe.to_json("people_output.json", orient="records", indent=2)

if __name__ == '__main__':
    main()