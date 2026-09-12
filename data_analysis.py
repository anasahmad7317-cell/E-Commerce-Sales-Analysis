import pandas as pd

# ==========================================
# 1. LOAD ORIGINAL DATASET
# ==========================================

df = pd.read_csv(
    r"C:\Users\asus\OneDrive\Desktop\E-Commerce-Sales-Analysis\data\Train.csv"
)

print("Original Dataset Shape:", df.shape)  


# ==========================================
# 2. CHECK DUPLICATES
# ==========================================

print("\nDuplicate Rows:", df.duplicated().sum())

df = df.drop_duplicates()


# ==========================================
# 3. CONVERT DATE
# ==========================================

# Dataset uses DD/MM/YYYY format
df["Date"] = pd.to_datetime(
    df["Date"].astype(str).str.strip(),
    format="%d/%m/%Y",
    errors="coerce"
)


# ==========================================
# 4. CHECK INVALID DATES
# ==========================================

invalid_dates = df["Date"].isnull().sum()

print("\nInvalid Dates:", invalid_dates)


# ==========================================
# 5. CREATE YEAR
# ==========================================

df["Year"] = df["Date"].dt.year


# ==========================================
# 6. CREATE MONTH NUMBER
# ==========================================

df["Month"] = df["Date"].dt.month


# ==========================================
# 7. CREATE MONTH NAME
# ==========================================

df["Month_Name"] = df["Date"].dt.month_name()


# ==========================================
# 8. CREATE YEAR-MONTH
# ==========================================

df["Year_Month"] = df["Date"].dt.to_period("M").astype(str)


# ==========================================
# 9. CREATE QUARTER
# ==========================================

df["Quarter"] = df["Date"].dt.quarter


# ==========================================
# 10. SELLING PRICE ANALYSIS
# ==========================================

print("\nSelling Price Statistics:")
print(df["Selling_Price"].describe())


# ==========================================
# 11. FINAL DATA CHECK
# ==========================================

print("\nFinal Dataset Shape:")
print(df.shape)

print("\nFinal Missing Values:")
print(df.isnull().sum())


# ==========================================
# 12. SAVE CLEANED DATA
# ==========================================

df.to_csv(
    r"C:\Users\asus\OneDrive\Desktop\E-Commerce-Sales-Analysis\data\cleaned_ecommerce_sales.csv",
    index=False
)


print("\n===================================")
print("DATA CLEANING COMPLETED SUCCESSFULLY")
print("===================================")
print("Cleaned Dataset Shape:", df.shape)
print("Cleaned file saved successfully!")

# ==========================================
# 13. DATASET UNDERSTANDING
# ==========================================

print("\n===================================")
print("DATASET UNDERSTANDING")
print("===================================")

# Number of unique values
print("\nUnique Values in Each Column:")
print(df.nunique())


# Date Range
print("\nDate Range:")
print("Minimum Date:", df["Date"].min())
print("Maximum Date:", df["Date"].max())


# Product Categories
print("\nItem Categories:")
print(df["Item_Category"].value_counts())


# Top 10 Brands
print("\nTop 10 Brands:")
print(df["Product_Brand"].value_counts().head(10))


# Rating Distribution
print("\nItem Rating Distribution:")
print(df["Item_Rating"].value_counts().sort_index())


# Selling Price Analysis
print("\nSelling Price:")
print("Minimum Price:", df["Selling_Price"].min())
print("Maximum Price:", df["Selling_Price"].max())
print("Average Price:", df["Selling_Price"].mean())
print("Median Price:", df["Selling_Price"].median())


# Top 10 Most Expensive Products
print("\nTop 10 Most Expensive Products:")
print(
    df[
        ["Product", "Product_Brand", "Item_Category", "Selling_Price"]
    ]
    .sort_values("Selling_Price", ascending=False)
    .head(10)
)


# Top 10 Products by Average Selling Price
print("\nTop 10 Products by Average Selling Price:")
print(
    df.groupby("Product")["Selling_Price"]
    .mean()
    .sort_values(ascending=False)
    .head(10)
)

# ==========================================
# 14. BUSINESS ANALYSIS
# ==========================================

print("\n===================================")
print("BUSINESS ANALYSIS")
print("===================================")


# ------------------------------------------
# 1. CATEGORY-WISE ANALYSIS
# ------------------------------------------

category_analysis = (
    df.groupby("Item_Category")
    .agg(
        Product_Count=("Product", "count"),
        Average_Price=("Selling_Price", "mean"),
        Total_Price=("Selling_Price", "sum"),
        Average_Rating=("Item_Rating", "mean")
    )
    .sort_values("Product_Count", ascending=False)
)

print("\nCategory-wise Analysis:")
print(category_analysis.head(10))


# ------------------------------------------
# 2. BRAND-WISE ANALYSIS
# ------------------------------------------

brand_analysis = (
    df.groupby("Product_Brand")
    .agg(
        Product_Count=("Product", "count"),
        Average_Price=("Selling_Price", "mean"),
        Total_Price=("Selling_Price", "sum"),
        Average_Rating=("Item_Rating", "mean")
    )
    .sort_values("Product_Count", ascending=False)
)

print("\nBrand-wise Analysis:")
print(brand_analysis.head(10))


# ------------------------------------------
# 3. YEAR-WISE ANALYSIS
# ------------------------------------------

year_analysis = (
    df.groupby("Year")
    .agg(
        Product_Count=("Product", "count"),
        Average_Price=("Selling_Price", "mean"),
        Total_Price=("Selling_Price", "sum"),
        Average_Rating=("Item_Rating", "mean")
    )
    .sort_index()
)

print("\nYear-wise Analysis:")
print(year_analysis)


# ------------------------------------------
# 4. RATING-WISE ANALYSIS
# ------------------------------------------

rating_analysis = (
    df.groupby("Item_Rating")
    .agg(
        Product_Count=("Product", "count"),
        Average_Price=("Selling_Price", "mean")
    )
    .sort_index()
)

print("\nRating-wise Analysis:")
print(rating_analysis)


# ------------------------------------------
# 5. PRICE RANGE ANALYSIS
# ------------------------------------------

df["Price_Range"] = pd.cut(
    df["Selling_Price"],
    bins=[0, 500, 1000, 5000, 10000, float("inf")],
    labels=[
        "₹0–₹500",
        "₹501–₹1,000",
        "₹1,001–₹5,000",
        "₹5,001–₹10,000",
        "Above ₹10,000"
    ]
)

price_range_analysis = (
    df.groupby("Price_Range", observed=False)
    .agg(
        Product_Count=("Product", "count"),
        Average_Rating=("Item_Rating", "mean")
    )
)

print("\nPrice Range Analysis:")
print(price_range_analysis)


# ------------------------------------------
# 6. TOP 10 HIGHEST RATED PRODUCTS
# ------------------------------------------

top_rated_products = (
    df[
        [
            "Product",
            "Product_Brand",
            "Item_Category",
            "Item_Rating",
            "Selling_Price"
        ]
    ]
    .sort_values(
        ["Item_Rating", "Selling_Price"],
        ascending=[False, False]
    )
    .head(10)
)

print("\nTop 10 Highest Rated Products:")
print(top_rated_products)


# ------------------------------------------
# 7. FINAL SUMMARY
# ------------------------------------------

print("\n===================================")
print("BUSINESS ANALYSIS COMPLETED")
print("===================================")

# ==========================================
# 15. DATA VISUALIZATION
# ==========================================

import matplotlib.pyplot as plt


# ------------------------------------------
# CHART 1: TOP 10 CATEGORIES
# ------------------------------------------

top_categories = (
    df["Item_Category"]
    .value_counts()
    .head(10)
)

plt.figure(figsize=(10, 6))

top_categories.sort_values().plot(
    kind="barh"
)

plt.title("Top 10 Categories by Product Count")
plt.xlabel("Number of Products")
plt.ylabel("Category")
plt.tight_layout()

plt.savefig(
    r"C:\Users\asus\OneDrive\Desktop\E-Commerce-Sales-Analysis\screenshots\top_categories.png"
)

plt.show()


# ------------------------------------------
# CHART 2: YEAR-WISE AVERAGE PRICE
# ------------------------------------------

year_price = (
    df.groupby("Year")["Selling_Price"]
    .mean()
)

plt.figure(figsize=(10, 6))

year_price.plot(
    kind="line",
    marker="o"
)

plt.title("Year-wise Average Selling Price")
plt.xlabel("Year")
plt.ylabel("Average Selling Price (₹)")
plt.grid(True)
plt.tight_layout()

plt.savefig(
    r"C:\Users\asus\OneDrive\Desktop\E-Commerce-Sales-Analysis\screenshots\year_average_price.png"
)

plt.show()


# ------------------------------------------
# CHART 3: CATEGORY-WISE AVERAGE RATING
# ------------------------------------------

category_rating = (
    df.groupby("Item_Category")["Item_Rating"]
    .mean()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(10, 6))

category_rating.sort_values().plot(
    kind="barh"
)

plt.title("Top 10 Categories by Average Rating")
plt.xlabel("Average Rating")
plt.ylabel("Category")
plt.tight_layout()

plt.savefig(
    r"C:\Users\asus\OneDrive\Desktop\E-Commerce-Sales-Analysis\screenshots\category_rating.png"
)

plt.show()


# ------------------------------------------
# CHART 4: SELLING PRICE DISTRIBUTION
# ------------------------------------------

plt.figure(figsize=(10, 6))

plt.hist(
    df["Selling_Price"],
    bins=50
)

plt.title("Selling Price Distribution")
plt.xlabel("Selling Price (₹)")
plt.ylabel("Number of Products")
plt.tight_layout()

plt.savefig(
    r"C:\Users\asus\OneDrive\Desktop\E-Commerce-Sales-Analysis\screenshots\price_distribution.png"
)

plt.show()


# ------------------------------------------
# CHART 5: TOP 10 BRANDS
# ------------------------------------------

top_brands = (
    df["Product_Brand"]
    .value_counts()
    .head(10)
)

plt.figure(figsize=(10, 6))

top_brands.sort_values().plot(
    kind="barh"
)

plt.title("Top 10 Brands by Product Count")
plt.xlabel("Number of Products")
plt.ylabel("Brand")
plt.tight_layout()

plt.savefig(
    r"C:\Users\asus\OneDrive\Desktop\E-Commerce-Sales-Analysis\screenshots\top_brands.png"
)

plt.show()


print("\n===================================")
print("VISUALIZATION COMPLETED")
print("===================================")