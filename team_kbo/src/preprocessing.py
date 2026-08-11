import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def preprocess_data(df: pd.DataFrame, target_col: str = "OPS", test_size: float = 0.2, random_state: int = 42):
    """
    데이터 전처리, 결측치 처리 및 학습/검증 데이터 분리를 수행합니다.
    """
    df = df.copy()
    
    # 1. 수치형/범주형 컬럼 처리 (필요시 수정)
    # 수치형 변수만 선택하거나 범주형 변수를 인코딩합니다.
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
    
    # 타겟 변수 결측치 제거
    df = df.dropna(subset=[target_col])
    
    # 수치형 결측치 중앙값 채우기
    for col in numeric_cols:
        if col != target_col:
            df[col] = df[col].fillna(df[col].median())
            
    # 피처(X)와 타겟(y) 분리
    X = df[numeric_cols].drop(columns=[target_col])
    y = df[target_col]
    
    # Train / Test 분리
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state
    )
    
    # 스케일링
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # 컬럼 이름 유지용 DataFrame 변환
    X_train_scaled = pd.DataFrame(X_train_scaled, columns=X.columns)
    X_test_scaled = pd.DataFrame(X_test_scaled, columns=X.columns)
    
    print("[Preprocessing] 전처리 및 데이터 분리 완료")
    return X_train_scaled, X_test_scaled, y_train, y_test, X