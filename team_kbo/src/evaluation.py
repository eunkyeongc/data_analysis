import os
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error

def evaluate_model(model, X_test, y_test, output_dir: str = "results"):
    """
    모델 예측 성능을 평가하고 예측값 vs 실제값 시각화를 저장합니다.
    """
    os.makedirs(output_dir, exist_ok=True)
    
    predictions = model.predict(X_test)
    
    # 평가 지표 산출
    mse = mean_squared_error(y_test, predictions)
    rmse = np.sqrt(mse)
    mae = mean_absolute_error(y_test, predictions)
    r2 = r2_score(y_test, predictions)
    
    print("\n================ [ 모델 평가 결과 ] ================")
    print(f"RMSE : {rmse:.4f}")
    print(f"MAE  : {mae:.4f}")
    print(f"R²   : {r2:.4f}")
    print("====================================================\n")
    
    # Actual vs Predicted 시각화
    plt.figure(figsize=(8, 6))
    plt.scatter(y_test, predictions, alpha=0.6, color="blue")
    plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2)
    plt.xlabel("실제 OPS (Actual)")
    plt.ylabel("예측 OPS (Predicted)")
    plt.title("OPS 예측값 vs 실제값 비교")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "ops_pred_vs_actual.png"))
    plt.close()
    
    print(f"[Evaluation] 평가 이미지 저장 완료 -> '{output_dir}/ops_pred_vs_actual.png'")
    return {"rmse": rmse, "mae": mae, "r2": r2}