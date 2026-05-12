def analyze_df(df):

    # create revenue column
    df['revenue'] = df['quantity'] * df['price']
    
    # Total revenue 
    total_revenue = df['revenue'].sum()

    # Average revenue per order
    avg_revenue = df['revenue'].mean()

    # Top selling products
    top_products = df.loc[df['revenue'].idxmax(), 'product']

    return total_revenue, avg_revenue, top_products

    
