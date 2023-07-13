def prob(ser):
    return ser.mean()

def conditional(proposition, given):
    return prob(proposition[given])

