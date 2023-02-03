import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import streamlit as st

def open_csv_pandas(file_path):
    "To open a .csv. Insert the path and it will return the df"
    df = pd.read_csv(file_path, sep=',', encoding='UTF-8', index_col=0)
    return df


def join_csv_without_col(file1_path, file2_path):
    df1 = pd.read_csv(file1_path)
    df2 = pd.read_csv(file2_path)
    df_merged = pd.merge(df1, df2, on='Hotel', how='inner')
    df_merged.drop("Unnamed: 0_x", axis=1, inplace=True)
    df_merged.drop("Unnamed: 0_y", axis=1, inplace=True)
    return df_merged

def filter_by_city(df, selected_city):
    return df[df["Location"] == selected_city]

def compare_result_df(df1, df2):
    # Calculate the mean of each column in df1
    mean_df = pd.DataFrame({
        "Hotel": ["Average"],
        "Trip_Rate": [df1["Trip_Rate"].mean()],
        "Google_Rate": [df1["Google_Rate"].mean()]
    })
    # Concatenate the mean_df and df2
    result_df = pd.concat([mean_df, df2], ignore_index=True)
    selected_result_df = result_df[["Hotel", "Trip_Rate", "Google_Rate"]]
    return selected_result_df

def bar_chart(df, title, x_col, y_col, color):
    st.set_option('deprecation.showPyplotGlobalUse', False)
    plt.figure(figsize=(10, 5))
    sns.barplot(x=x_col, y=y_col, data=df, color=color)
    plt.xticks(rotation=45, ha='right')
    plt.title(title)
    plt.show()
    st.pyplot()
