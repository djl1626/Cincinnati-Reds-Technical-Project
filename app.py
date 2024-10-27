import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px


@st.cache_data()
def load_data():
    overall_predictions = pd.read_csv("Data/predictions.csv")
    batters_count_predictions = pd.read_csv("Data/predictions_by_count.csv")
    names = dict(
        zip(overall_predictions['BATTER_ID'], overall_predictions['PLAYER_NAME']))
    return overall_predictions, batters_count_predictions, names


st.title("2024 Batter Pitch Mix Prediction Dashboard")


def generate_plots(player, count):
    if len(player) != 0:
        player = player[0]
        if len(count) == 0:
            plotting_df = season_predictions.query("BATTER_ID == @player")[['BATTER_ID', 'PLAYER_NAME', 'PITCH_TYPE_FB', 'PITCH_TYPE_BB', 'PITCH_TYPE_OS']]\
                .rename(columns={"PITCH_TYPE_FB": 'Fastball',
                                 "PITCH_TYPE_BB": "Breaking Ball",
                                 "PITCH_TYPE_OS": "Off-speed"}).melt(id_vars=['BATTER_ID', 'PLAYER_NAME'],
                                                                     value_vars=[
                                     'Fastball', 'Breaking Ball', 'Off-speed'],
                var_name='PITCH_TYPE', value_name='Predicted Percentage')
            plotting_df['Predicted Percentage'] = round(
                100 * plotting_df['Predicted Percentage'], 2)
            fig = px.line_polar(
                plotting_df, r='Predicted Percentage', theta='PITCH_TYPE', line_close=True, range_r=[0, plotting_df['Predicted Percentage'].max()])
            st.table(plotting_df)
            st.plotly_chart(fig)
        else:
            balls = int(count[0][0])
            strikes = int(count[0][2])
            plotting_df = count_predictions.query("BATTER_ID == @player & BALLS == @balls & STRIKES == @strikes")[['BATTER_ID', 'PLAYER_NAME', 'mean_fastball', 'mean_breaking_ball', 'mean_offspeed']]\
                .rename(columns={'mean_fastball': 'Fastball',
                                 'mean_breaking_ball': 'Breaking Ball',
                                 'mean_offspeed': 'Off-speed'}).melt(id_vars=['BATTER_ID', 'PLAYER_NAME'],
                                                                     value_vars=[
                                     'Fastball', 'Breaking Ball', 'Off-speed'],
                var_name='PITCH_TYPE', value_name='Predicted Percentage')
            plotting_df['Predicted Percentage'] = round(
                100 * plotting_df['Predicted Percentage'], 2)
            fig = px.line_polar(
                plotting_df, r='Predicted Percentage', theta='PITCH_TYPE', line_close=True, range_r=[0, plotting_df['Predicted Percentage'].max()])
            st.table(plotting_df)
            st.plotly_chart(fig)


season_predictions, count_predictions, names = load_data()

with st.sidebar.form(key="Filters"):
    st.subheader("Data Filters:")
    player = st.multiselect("Player", options=pd.unique(
        season_predictions['BATTER_ID']), format_func=lambda pitcher: names[pitcher], placeholder="Choose a Player...", default=None)
    count = st.multiselect("Batter's Count", options=['0-0', '0-1', '0-2', '1-0', '1-1', '1-2',
                           '2-0', '2-1', '2-2', '3-0', '3-1', '3-2'], placeholder="Choose a Count...", default=None)
    st.form_submit_button("Apply")

if len(player) != 0:
    generate_plots(player, count)
