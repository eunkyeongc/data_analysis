import os
import pandas as pd

def load_data(file_path: str = "data/hitter.csv") -> pd.DataFrame:
    """
    KBO 타자 데이터 CSV 파일을 로드합니다.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"파일을 찾을 수 없습니다: {file_path}")
    
    df = pd.read_csv(file_path)
    print(f"[Data Loader] 데이터 로드 완료 - Shape: {df.shape}")
    return df