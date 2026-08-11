import os
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# 한글 폰트 설정 (Mac/Windows 호환)
plt.rcParams['font.family'] = 'Malgun Gothic' if os.name == 'nt' else 'AppleGothic'
plt.rcParams['axes.unicode_minus'] = False

def perform_eda(df: pd.DataFrame, output_dir: str = "results"):
    """
    탐색적 데이터 분석(EDA) 시각화 이미지를 생성하고 results 디렉터리에 저장합니다.
    """
    os.makedirs(output_dir, exist_ok=True)
    numeric_df = df.select_dtypes(include=['float64', 'int64'])
    
    # 1. Boxplot (이상치 확인)
    plt.figure(figsize=(12, 6))
    sns.boxplot(data=numeric_df.iloc[:, :10])  # 상위 10개 피처 확인
    plt.title("주요 피처 Boxplot")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "boxplot_check.png"))
    plt.close()
    
    # 2. Histogram (분포 확인)
    numeric_df.hist(figsize=(14, 10), bins=20)
    plt.suptitle("주요 피처 히스토그램", fontsize=16)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "histogram_check.png"))
    plt.close()
    
    # 3. Correlation Heatmap
    plt.figure(figsize=(10, 8))
    sns.heatmap(numeric_df.corr(), annot=True, fmt=".2f", cmap="coolwarm", linewidths=0.5)
    plt.title("상관관계 상관계수 히트맵")
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "correlation_heatmap.png"))
    plt.close()
    
    print(f"[EDA] 시각화 이미지 저장 완료 -> '{output_dir}'")