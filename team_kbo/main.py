from src.pipeline import run_pipeline

if __name__ == "__main__":
    # 전체 분석 파이프라인 실행
    # target_col: 예측하고자 하는 타겟 컬럼명 (기본값: 'OPS')
    run_pipeline(
        data_path="data/hitter.csv",
        target_col="OPS",
        model_type="xgboost"
    )