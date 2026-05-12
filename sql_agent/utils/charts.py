import plotly.express as px

def create_chart(df):

    if len(df.columns) >= 2:

        fig = px.bar(
            df,
            x=df.columns[0],
            y=df.columns[1]
        )

        return fig

    return None