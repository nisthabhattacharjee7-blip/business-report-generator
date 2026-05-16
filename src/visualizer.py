import matplotlib.pyplot as plt


def revenue_chart (df):

    # create a revenue column 
    df['revenue'] = df['quantity'] * df['price']

    # product names 
    products = df['product'].unique()
    
    plt.figure(figsize=(10, 6))
    # create chart 
    plt.bar(products, df['revenue'])

    # chart title 
    plt.title('Revenue by Product')

    # axis labels
    plt.xlabel('Product')
    plt.ylabel('Revenue')

    # save chart
    plt.savefig('output/revenue_chart.png')
    print("\nRevenue chart generated successfully")


def category_chart(df):

    # create a revenue column 
    df['revenue'] = df['quantity'] * df['price']

    # category names 
    categories = df['category'].unique()

    # Group revenue by category 
    category_revenue = df.groupby('category')['revenue'].sum()

    # create chart 
    plt.figure(figsize=(10, 6))
    plt.bar(categories, category_revenue)

    # chart title 
    plt.title('Revenue by Category')

    # axis labels
    plt.xlabel('Category')
    plt.ylabel('Revenue')

    # save chart
    plt.savefig('output/category_chart.png')
    print("\nCategory revenue chart generated successfully")


def category_pie_chart(df):

    # create a revenue column 
    df['revenue'] = df['quantity'] * df['price']

    # category names 
    categories = df['category'].unique()

    # Group revenue by category 
    category_revenue = df.groupby('category')['revenue'].sum()

    # create pie chart
    plt.figure(figsize=(10, 6))
    plt.pie(category_revenue.values,
            labels=category_revenue.index, 
            autopct='%1.1f%%'
    )

    # chart title 
    plt.title('Revenue Distribution by Category')

    # save chart
    plt.savefig('output/category_pie_chart.png')
    print("\nCategory revenue pie chart generated successfully")