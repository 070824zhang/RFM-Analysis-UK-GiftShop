import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()
db_pwd = os.getenv("DB_PASSWORD")
df = pd.read_csv('rfm_final_result.csv')
print(f"抓到洗好的数据了！一共{len(df)}行。")
engine = create_engine(f'mysql+pymysql://root:{db_pwd}@localhost:3306/rfm_project')
df.to_sql(name='uk_rfm_analysis', con=engine, if_exists='replace', index=False)
print("已经成功进入仓库")