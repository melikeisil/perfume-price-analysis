from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "archive"
OUTPUT_DIR = BASE_DIR / "outputs"


def load_data() -> pd.DataFrame:
    mens = pd.read_csv(DATA_DIR / "ebay_mens_perfume.csv")
    womens = pd.read_csv(DATA_DIR / "ebay_womens_perfume.csv")

    mens["gender"] = "Men"
    womens["gender"] = "Women"

    df = pd.concat([mens, womens], ignore_index=True)
    df["sold"] = pd.to_numeric(df["sold"], errors="coerce")
    df["available"] = pd.to_numeric(df["available"], errors="coerce")
    df["price"] = pd.to_numeric(df["price"], errors="coerce")
    return df


def save_histogram(df: pd.DataFrame) -> None:
    plt.figure(figsize=(10, 6))
    sns.histplot(data=df, x="price", bins=35, color="#c96f3b", edgecolor="white")
    plt.title("Histogram of Perfume Prices")
    plt.xlabel("Price (USD)")
    plt.ylabel("Number of Products")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "histogram_price_distribution.png", dpi=200)
    plt.close()


def save_boxplot(df: pd.DataFrame) -> None:
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=df, x="price", color="#6a9c89")
    plt.title("Box Plot of Perfume Prices")
    plt.xlabel("Price (USD)")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "boxplot_price_outliers.png", dpi=200)
    plt.close()


def save_violinplot(df: pd.DataFrame) -> None:
    plt.figure(figsize=(10, 6))
    sns.violinplot(
        data=df,
        x="gender",
        y="price",
        hue="gender",
        palette={"Men": "#457b9d", "Women": "#e76f51"},
        inner="quartile",
        cut=0,
        legend=False,
    )
    plt.title("Violin Plot of Prices by Gender Category")
    plt.xlabel("Perfume Category")
    plt.ylabel("Price (USD)")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "violinplot_gender_price.png", dpi=200)
    plt.close()


def save_scatterplot(df: pd.DataFrame) -> None:
    scatter_df = df.dropna(subset=["price", "sold"])
    plt.figure(figsize=(10, 6))
    sns.scatterplot(
        data=scatter_df,
        x="price",
        y="sold",
        hue="gender",
        alpha=0.7,
        palette={"Men": "#457b9d", "Women": "#e76f51"},
    )
    plt.title("Scatter Plot of Price vs Sold")
    plt.xlabel("Price (USD)")
    plt.ylabel("Units Sold")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "scatter_price_vs_sold.png", dpi=200)
    plt.close()


def build_summary(df: pd.DataFrame) -> str:
    total_samples = len(df)
    total_features = len(df.columns)
    summary = df.groupby("gender")["price"].describe().round(2)

    q1 = df["price"].quantile(0.25)
    q3 = df["price"].quantile(0.75)
    iqr = q3 - q1
    upper_bound = q3 + 1.5 * iqr
    lower_bound = q1 - 1.5 * iqr
    outliers = df[(df["price"] < lower_bound) | (df["price"] > upper_bound)].sort_values(
        "price", ascending=False
    )
    top_outliers = outliers[["gender", "brand", "title", "price", "sold", "available"]].head(10)

    corr_price_sold = df[["price", "sold"]].corr().iloc[0, 1]
    corr_price_available = df[["price", "available"]].corr().iloc[0, 1]

    lines = [
        "# Person 2 - Price and Numerical Variable Analysis",
        "",
        "## Dataset Review",
        "- Source: Kaggle perfume e-commerce dataset based on eBay perfume listings.",
        "- Files used: `archive/ebay_mens_perfume.csv` and `archive/ebay_womens_perfume.csv`.",
        f"- Number of samples: {total_samples} listings in total (1000 men + 1000 women).",
        f"- Number of features after combining: {total_features}.",
        "- Original common features: brand, title, type, price, priceWithCurrency, available, availableText, sold, lastUpdated, itemLocation.",
        "- Added feature for analysis: `gender`.",
        "- Project type: Exploratory Data Analysis (EDA).",
        "- Possible target variable: `gender`.",
        "- Target type if used for modeling: binary classification (Men vs Women).",
        "",
        "## Key Findings",
        f"- Overall price range: ${df['price'].min():.2f} to ${df['price'].max():.2f}.",
        f"- Men perfume mean price: ${summary.loc['Men', 'mean']:.2f}; median: ${summary.loc['Men', '50%']:.2f}.",
        f"- Women perfume mean price: ${summary.loc['Women', 'mean']:.2f}; median: ${summary.loc['Women', '50%']:.2f}.",
        "- Men perfumes are slightly more expensive on average, but both groups are right-skewed because of premium products.",
        f"- IQR-based outlier bounds: lower={lower_bound:.2f}, upper={upper_bound:.2f}.",
        f"- Number of price outliers: {len(outliers)}.",
        f"- Correlation between price and sold: {corr_price_sold:.3f}.",
        f"- Correlation between price and available: {corr_price_available:.3f}.",
        "- Interpretation: higher prices have a weak negative relationship with sold and available counts.",
        "",
        "## Visualization Notes",
        "- Histogram: shows most products are concentrated at lower price levels with a long right tail.",
        "- Box plot: clearly highlights expensive outlier perfumes.",
        "- Violin plot: compares the full price density of men and women perfume listings.",
        "- Scatter plot: shows that very expensive products do not necessarily have high sales.",
        "",
        "## Example Outlier Products",
    ]

    for row in top_outliers.itertuples(index=False):
        brand = "Unknown" if pd.isna(row.brand) else row.brand
        sold = "NaN" if pd.isna(row.sold) else f"{row.sold:.0f}"
        available = "NaN" if pd.isna(row.available) else f"{row.available:.0f}"
        lines.append(
            f"- {row.gender}: {brand} | ${row.price:.2f} | sold={sold} | available={available} | {row.title}"
        )

    return "\n".join(lines) + "\n"


def main() -> None:
    OUTPUT_DIR.mkdir(exist_ok=True)
    sns.set_theme(style="whitegrid")

    df = load_data()
    save_histogram(df)
    save_boxplot(df)
    save_violinplot(df)
    save_scatterplot(df)

    summary_text = build_summary(df)
    (BASE_DIR / "person2_price_analysis.md").write_text(summary_text, encoding="utf-8")
    print("Analysis complete.")
    print(f"Outputs saved to: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
