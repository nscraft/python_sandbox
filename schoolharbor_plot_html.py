# Import packages
import pandas as pd
import plotly.express as px

import time  # for speed test
st = time.time()  # for speed test

# Get operators from user context bus
# API config
# Get data from api (replace flat file with api call)
df = pd.read_csv('AltSource.csv')

# Analyze data
df['Possible'] = 100  # assumes 100 points possible each record
# Excellence
excellence_df = pd.DataFrame(
    {'Series': 'Excellence', 'Values': sum(df['Excellence']), 'Possible': sum(df['Possible'])}, index=[0])
excellence_df['Percent'] = excellence_df['Values'] / excellence_df['Possible']
excellence_fig = px.bar(excellence_df, x='Percent', y='Series', orientation='h')
excellence_fig.update_xaxes(range=[0, 1])
# innovation
innovation_df = pd.DataFrame(
    {'Series': 'Innovation', 'Values': sum(df['Innovation']), 'Possible': sum(df['Possible'])}, index=[0])
innovation_df['Percent'] = innovation_df['Values'] / innovation_df['Possible']
innovation_fig = px.bar(innovation_df, x='Percent', y='Series', orientation='h')
innovation_fig.update_xaxes(range=[0, 1])
# equity
equity_df = pd.DataFrame(
    {'Series': 'Equity', 'Values': sum(df['Equity']), 'Possible': sum(df['Possible'])}, index=[0])
equity_df['Percent'] = equity_df['Values'] / equity_df['Possible']
equity_fig = px.bar(equity_df, x='Percent', y='Series', orientation='h')
equity_fig.update_xaxes(range=[0, 1])
# survey results
survey_df = pd.DataFrame({
    'Lean Practices': sum(df['Lean Practices'])
    , 'Big Data & Analytics': sum(df['Big Data & Analytics'])
    , 'AI & Digital Transformation': sum(df['AI & Digital Transformation'])
    , 'Culture': sum(df['Culture'])
    , 'Strategy': sum(df['Strategy'])}
    , index=[0])
survey_df = pd.melt(survey_df, var_name='Series', value_name='Value')
survey_df['Possible'] = sum(df['Possible'])
survey_df['Percent'] = survey_df['Value'] / survey_df['Possible']
survey_fig = px.bar(survey_df, x='Percent', y='Series', orientation='h')
survey_fig.update_xaxes(range=[0, 1])

# write fig to html file
excellence_fig.write_html('excellence.html')
innovation_fig.write_html('innovation.html')
equity_fig.write_html('equity.html')
survey_fig.write_html('survey.html')

# upload html file
# insert code to send html file from directory to cloud path

# for speed test
print("complete time %.2f" % (time.time() - st))
