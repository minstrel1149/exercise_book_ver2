def prob(ser):
    return ser.mean()

def conditional(proposition, given):
    return prob(proposition[given])

def update(table):
    table['unnorm'] = table['prior'] * table['likelihood']
    table['posterior'] = table['unnorm'] / table['unnorm'].sum()
    return table

