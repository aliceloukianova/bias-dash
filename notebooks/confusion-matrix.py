import pandas as pd
import plotly.express as px


def plot_confusion_matrix(bfw_df):
    # Calculate confusion matrix df
    conf_df = confusion_matrix_df(bfw_df)
    fig = px.imshow(conf_df,
                    labels=dict(x="Subgroup", y="Imposter Subgroup", color="Rank 1 Error"),
                    x=['AF', 'AM', 'BF', 'BM', 'IF', 'IM', 'WF', 'WM'],
                    y=['AF', 'AM', 'BF', 'BM', 'IF', 'IM', 'WF', 'WM'],
                    color_continuous_scale="blues")
    fig.show()


def confusion_matrix_df(bfw_df):
    # An error occurs when label is 0
    bfw_df['error'] = 1 - bfw_df['label']

    # Group by subgroup of initial image, then by subgroup of alleged match
    conf = bfw_df.groupby(by=['a1', 'a2']).sum()['error']

    confusion_npy = conf.values.reshape(1, -1)
    confusion_npy = confusion_npy.reshape((8, -1))

    # A data frame of the error counts indexed row and column by subgroup
    df_conf = pd.DataFrame(confusion_npy, index=bfw_df.a1.unique(),
                           columns=bfw_df.a1.unique())

    # Calculate number of samples per subgroup and divide error count by it to get percent error
    n_samples_per_subgroup = bfw_df.a1.count() / bfw_df.a1.nunique()
    df_conf_percent_error = (df_conf / n_samples_per_subgroup) * 100

    return df_conf_percent_error

