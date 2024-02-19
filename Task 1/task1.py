import pandas as pd
import matplotlib.pyplot as plt

def exercise_0(file):
    printFile = pd.read_csv('transactions.csv')
    return printFile

def exercise_1(df):
    return list(df)

def exercise_2(df, k):
    return df.head(k)

def exercise_3(df, k):
    return df.sample(n=k)

def exercise_4(df):
    uniqueList = df['type'].unique().tolist()
    return uniqueList

def exercise_5(df):
    destination_freq = df['nameDest'].value_counts().head(10)
    return destination_freq

def exercise_6(df):
    fraud_detected = df[df['isFraud'] == True]
    return fraud_detected

def exercise_7(df):
    grouped = df.groupby('nameOrig')['nameDest'].agg(lambda x: len(set(x))).reset_index()
    ascending_df = grouped.sort_values(by='nameDest', ascending=False)
    return ascending_df

def visual_1(df):
    def transaction_counts(df):
        uniqueList = df['type'].value_counts()
        return uniqueList
    def transaction_counts_split_by_fraud(df):
        uniqueList = df[df['isFraud'] == True]['type'].value_counts()
        return uniqueList

    fig, axs = plt.subplots(2, figsize=(6,10))
    transaction_counts(df).plot(ax=axs[0], kind='bar')
    axs[0].set_title('Types of Transactions')
    axs[0].set_xlabel('Transaction Type')
    axs[0].set_ylabel('Count')
    transaction_counts_split_by_fraud(df).plot(ax=axs[1], kind='bar')
    axs[1].set_title('Types of Transactions: Split by Fraud')
    axs[1].set_xlabel('Transaction Type')
    axs[1].set_ylabel('Count')
    fig.suptitle('Transaction Type')
    fig.tight_layout(rect=[0, 0.03, 1, 0.95])
    for ax in axs:
      for p in ax.patches:
          ax.annotate(p.get_height(), (p.get_x(), p.get_height()))

def visual_2(df):
    def query(df):
        df['Origin Account Delta'] = df['oldbalanceOrg'] - df['newbalanceOrig']
        df['Destination Account Delta'] = df['oldbalanceDest'] - df['newbalanceDest']
        return df[df['type'] == 'CASH_OUT']
        
    plot = query(df).plot.scatter(x='Origin Account Delta',y='Destination Account Delta')
    plot.set_title('Source vs Destination Balance Delta For Cash Out Transactions')
    plot.set_xlim(left=-1e3, right=1e3)
    plot.set_ylim(bottom=-1e3, top=1e3)

def exercise_custom(df):
    isFlaggedFraud = df['isFlaggedFraud'].value_counts()
    isFraud = df['isFraud'].value_counts()
    return isFlaggedFraud, isFraud
    
def visual_custom(df):
    fig, ax = plt.subplots(1, figsize=(4, 6))
    for idx, series in enumerate(exercise_custom(df)):
        series.plot(ax=ax, kind='bar', position=idx, width=0.4, label=f'Column {idx}')
    ax.set_title('Fraud Detection')
    ax.set_xlabel('isFlaggedFraud, isFraud')
    ax.set_ylabel('Occurrence')
