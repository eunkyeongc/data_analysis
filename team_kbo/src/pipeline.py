from src.data_loader import load_data
from src.preprocessing import preprocess_data
from src.eda import perform_eda
from src.model import train_model
from src.evaluation import evaluate_model

def run_pipeline(data_path: str = "data/hitter.csv", target_col: str = "OPS", model_type: str = "xgboost"):
    """
    데이터 로드부터 평가까지 전체 작업 파이프라인을 실행합니다.
    """
    print(">>> 파이프라인 시작...\n")
    
    # 1. 데이터 로드
    df = load_data(data_path)
    
    # 2. EDA 실행 및 그래프 저장
    perform_eda(df)
    
    # 3. 데이터 전처리
    X_train, X_test, y_train, y_test, full_X = preprocess_data(df, target_col=target_col)
    
    # 4. 모델 학습
    model = train_model(X_train, y_train, model_type=model_type)
    
    # 5. 모델 평가
    metrics = evaluate_model(model, X_test, y_test)
    
    print(">>> 파이프라인이 성공적으로 완료되었습니다!")
    return metrics