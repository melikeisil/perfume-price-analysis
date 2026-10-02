# Person 2 - Price and Numerical Variable Analysis

## Dataset Review
- Source: Kaggle perfume e-commerce dataset based on eBay perfume listings.
- Files used: `archive/ebay_mens_perfume.csv` and `archive/ebay_womens_perfume.csv`.
- Number of samples: 2000 listings in total (1000 men + 1000 women).
- Number of features after combining: 11.
- Original common features: brand, title, type, price, priceWithCurrency, available, availableText, sold, lastUpdated, itemLocation.
- Added feature for analysis: `gender`.
- Project type: Exploratory Data Analysis (EDA).
- Possible target variable: `gender`.
- Target type if used for modeling: binary classification (Men vs Women).

## Key Findings
- Overall price range: $1.99 to $299.99.
- Men perfume mean price: $46.48; median: $35.71.
- Women perfume mean price: $39.89; median: $32.99.
- Men perfumes are slightly more expensive on average, but both groups are right-skewed because of premium products.
- IQR-based outlier bounds: lower=-26.05, upper=102.02.
- Number of price outliers: 90.
- Correlation between price and sold: -0.090.
- Correlation between price and available: -0.114.
- Interpretation: higher prices have a weak negative relationship with sold and available counts.

## Visualization Notes
- Histogram: shows most products are concentrated at lower price levels with a long right tail.
- Box plot: clearly highlights expensive outlier perfumes.
- Violin plot: compares the full price density of men and women perfume listings.
- Scatter plot: shows that very expensive products do not necessarily have high sales.

## Example Outlier Products
- Women: Michael Kors | $299.99 | sold=92 | available=10 | Michael Kors CLASSIC(Original Formula) Eau De Parfum 3-Pcs Set  / New With Box
- Women: Creed | $285.00 | sold=5 | available=8 | Creed Queen Of Silk Eau De Parfum EDP 2.5oz / 75ml New 2024
- Women: Creed | $275.00 | sold=4 | available=NaN | Creed Queen of Silk Eau De Parfum 2.5oz 75ml Tester With Lid
- Women: Michael Kors | $269.00 | sold=59 | available=NaN | MICHAEL KORS EDP 3.4 Oz Eau De Parfum Spray Women NEW IN BOX SEALED
- Men: Creed | $259.09 | sold=456 | available=10 | Aventus by Creed, 3.3 oz Millesime EDP Spray for Men
- Men: Bvlgari | $250.00 | sold=NaN | available=NaN | Bvlgari Le Gemme Tygar 3.4oz Men's Eau de Parfum
- Men: Dolce&Gabbana | $239.99 | sold=14 | available=10 | Dolce & Gabbana The One Luminous Night 3.3/3.4 oz Eau De Parfum 100 ml Spray Men
- Men: Creed | $212.89 | sold=53 | available=10 | Aventus Cologne by Creed, 3.3 oz Millesime EDP Spray for Men
- Men: Roja | $202.95 | sold=18 | available=2 | Elysium by Roja Parfums, 3.4 oz Parfum Cologne Spray for Men
- Men: Giorgio Armani | $192.00 | sold=37 | available=7 | Acqua Di Gio Absolu Giorgio Armani EDP 125 ML / 4.2 Fl Oz Men Perfume
