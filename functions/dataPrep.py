import pandas as pd
import zipfile
import os

def getDataFrames():
    archiveDataAPath = "../data/archiveDataA.csv.zip"
    archiveDataBPath = "../data/archiveDataB.csv.zip"
    gameBoxPath = "../data/gameBox.csv.zip"
    gameStatsPath = "../data/gameStats.csv.zip"

    def read_csv_from_zip(zip_path, csv_name=None):
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            # List all files in the zip
            file_list = zip_ref.namelist()
            
            if csv_name is None:
                # Take the first CSV file if none specified
                csv_files = [f for f in file_list if f.endswith('.csv')]
                if not csv_files:
                    print(f"No CSV files found in {zip_path}")
                    return None
                csv_file = csv_files[0]
            else:
                # Use the specified CSV name
                csv_file = csv_name
                if csv_file not in file_list:
                    print(f"{csv_file} not found in {zip_path}")
                    return None
            # Extract and read the CSV
            with zip_ref.open(csv_file) as csv_ref:
                df = pd.read_csv(csv_ref)
            
            return df
        

    df_archiveDataA = read_csv_from_zip(archiveDataAPath)
    df_archiveDataB = read_csv_from_zip(archiveDataBPath)
    gameBox= read_csv_from_zip(gameBoxPath)
    gameStats = read_csv_from_zip(gameStatsPath)
    archiveData = pd.concat([df_archiveDataA, df_archiveDataB], axis=0, ignore_index=True)

    return gameBox, gameStats, archiveData