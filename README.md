# Perfume Price Analysis

This repository contains an exploratory data analysis project built on a Kaggle perfume e-commerce dataset derived from eBay perfume listings.

## Dataset

- Source: Kaggle
- Files:
  - `archive/ebay_mens_perfume.csv`
  - `archive/ebay_womens_perfume.csv`
- Total samples: 2000 listings
- Original features:
  - `brand`
  - `title`
  - `type`
  - `price`
  - `priceWithCurrency`
  - `available`
  - `availableText`
  - `sold`
  - `lastUpdated`
  - `itemLocation`

## Project Focus

This part of the project focuses on price and numerical variable analysis:

- How is the price distributed?
- Are there cheap and expensive products?
- Is there a price difference between men's and women's perfumes?
- Are there outlier products?

## Visualizations

The analysis script produces four EDA visualizations:

- Histogram of perfume prices
- Box plot for price outlier analysis
- Violin plot comparing men's and women's prices
- Scatter plot of `price` vs `sold`

Generated outputs are stored in `outputs/`.

## Files

- `person2_price_analysis.py`: analysis and chart generation script
- `person2_price_analysis.md`: written summary for presentation/report use
- `outputs/`: exported chart images

## Run

```bash
python3 person2_price_analysis.py
```
