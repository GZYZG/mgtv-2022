import time
import os


def checkSubmit(df):
    assert len(df) == 1025454
    assert df[['did', 'vid']].duplicated().sum() == 0
    assert df['did'].nunique() == 170909
    assert df['vid'].nunique() <= 13406
    assert set(df['rank'].unique()) == set([1, 2, 3, 4, 5, 6])
    
    print('Congratulations, submit file passes the checks!')
    

def saveSubmit(df, suffix='', out_dir='./output/'):
    checkSubmit(df)
    fn = time.strftime('%Y%m%d-%H:%M:%S')
    fn += f'.{suffix}.csv'
    
    submit.to_csv(os.path.join(out_dir, fn), index=False)
    print('二阶的关联推荐结果保存至 %s%s' % (out_dir, fn))