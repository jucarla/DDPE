import pandas as pd
import joblib

def get_metrics_df(joblib_path: str, index):
    models_reports = joblib.load(joblib_path)

    columns = []
    for key in models_reports.keys():
        columns.append(models_reports[key]['model_config']['hypermodel_name'])

    df = pd.DataFrame(columns=columns)
    mse =[]
    rmse =[]
    mae = []
    nmse = []
    nrmse = []
    r = []
    r2 = []
    for key in models_reports.keys():
        mse.append(models_reports[key]['metrics']['mse'][index])
        rmse.append(models_reports[key]['metrics']['rmse'][index])
        mae.append(models_reports[key]['metrics']['mae'][index])
        nmse.append(models_reports[key]['metrics']['nmse'][index])
        nrmse.append(models_reports[key]['metrics']['nrmse'][index])
        r.append(models_reports[key]['metrics']['r'][index])
        r2.append(models_reports[key]['metrics']['r2'][index])

    df.loc['mse']=mse
    df.loc['rmse']=rmse
    df.loc['mae'] = mae
    df.loc['nmse'] = nmse
    df.loc['nrmse']=nrmse
    df.loc['r']= r
    df.loc['r2']=r2

    df = df.T
    df.reset_index(inplace=True)
    df.columns=['name','mse','rmse','mae','nmse','nrmse','r','r2']

    return df

def get_array_like_metrics(joblib_path):
    df = get_metrics_df('C:/Users/jsilv757/Documents/ML Dash/dashboard/components/models_reports.joblib', 1)
    for i in df.index:
        locals()["df_%s" % i] = f"df_{i}"
        locals()["df_%s" % i] = pd.DataFrame(df.loc[i]).T
        locals()["df_%s" % i] = locals()["df_%s" % i].apply(lambda x: x.explode())
        locals()["df_%s" % i].reset_index(drop=True, inplace=True)
        locals()["df_%s" % i].index = locals()["df_%s" % i].index +1

    return df_r2, df_nmse