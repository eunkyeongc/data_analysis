from xgboost import XGBRegressor
from sklearn.ensemble import RandomForestRegressor

def train_model(X_train, y_train, model_type: str = "xgboost"):
    """
    지정된 회귀 모델을 학습합니다.
    """
    if model_type == "xgboost":
        model = XGBRegressor(n_estimators=100, learning_rate=0.05, random_state=42)
    elif model_type == "rf":
        model = RandomForestRegressor(n_estimators=100, random_state=42)
    else:
        raise ValueError(f"지원하지 않는 모델 유형입니다: {model_type}")
        
    model.fit(X_train, y_train)
    print(f"[Model] {model_type.upper()} 모델 학습 완료")
    return model