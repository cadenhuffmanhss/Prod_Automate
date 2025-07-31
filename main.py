import pandas as pd


#Upload 3 excels, put data into three dfs
#Combine three dfs into one df\

def read_epic_excel_as_pd(excel_name:str):
    df = pd.read_excel(excel_name, skiprows=8,engine="openpyxl")
    # Find the index of the column
    cutoff_index = df.columns.get_loc("Unnamed: 17")

    # Keep only columns up to the one before 'Unnamed: 17'
    df = df.iloc[:, :cutoff_index]

    return df

def combine_epic_files_into_one_df(df1,df2,df3):
    combined_df = pd.concat([df1, df2, df3], ignore_index=True)

    #Delete and insert

    combined_df.drop("Hosp Acct Name", axis=1, inplace=True)
    combined_df.drop("Hosp Acct ID", axis = 1, inplace = True)
    combined_df.drop("Hosp Acct Balance", axis=1, inplace = True )
    combined_df["User"] = combined_df["User"].str.replace(r"\s*\[\d+\]", "", regex=True)

    return combined_df


def main():

    epic_df_one = read_epic_excel_as_pd("data/epic/HSS_Time_Log_20250731_1345.xlsx")
    epic_df_two = read_epic_excel_as_pd("data/epic/HSS_Time_Log_2_20250731_1413.xlsx")
    epic_df_three = read_epic_excel_as_pd("data/epic/HSS_Time_Log_20250731_1412.xlsx")
    
    combined_epic_df = combine_epic_files_into_one_df(epic_df_one,epic_df_two,epic_df_three)
    #print(epic_df_one.tail())
    print(combined_epic_df.head())
    #print(len(combined_epic_df))


if __name__ == "__main__":
    print("running")
    main()








