import matplotlib.pyplot as plt


def revenue_chart (df):

    # create a revenue column 
    df['revenue'] = df['quantity'] * df['price']

    # product names 
    products = df['product'].unique()

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
    plt.bar(categories, category_revenue)

    # chart title 
    plt.title('Revenue by Category')

    # axis labels
    plt.xlabel('Category')
    plt.ylabel('Revenue')

    # save chart
    plt.savefig('output/category_chart.png')
    print("\nCategory revenue chart generated successfully")