import matplotlib.pyplot as plt

def show_transaction_nans(df, print_columns=False) :
    plt.figure(figsize=(20, 5))
    plt.plot(df.isna().sum(), marker='o')

    plt.axvspan(0, 5, alpha=0.1, color='tab:blue', label='info1')
    plt.axvspan(6, 11, alpha=0.1, color='tab:orange', label='card')
    plt.axvspan(12, 17, alpha=0.1, color='tab:green', label='info2')
    plt.axvspan(18, 31, alpha=0.1, color='tab:red', label='c')
    plt.axvspan(32, 46, alpha=0.1, color='tab:purple', label='d')
    plt.axvspan(47, 55, alpha=0.1, color='tab:brown', label='m')
    plt.axvspan(56, 394, alpha=0.1, color='tab:pink', label='v')

    plt.ylim(0, df.shape[0])
    plt.title('Num of NaNs, max(ylim)=df.shape[0]')
    plt.ylabel('Num of NaNs')
    plt.xlabel('Features')
    plt.legend()

    plt.show()

    if print_columns == True : 
        print('\n====info1')
        print(df.columns[0:5])
        print('\n====card')
        print(df.columns[6:11])
        print('\n====info2')
        print(df.columns[12:17])
        print('\n====c')
        print(df.columns[18:31])
        print('\n====d')
        print(df.columns[32:46])
        print('\n====m')
        print(df.columns[47:55])
        print('\n====v')
        print(df.columns[56:])
    
    return