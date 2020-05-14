import pandas as pd
data = {'year': [
    2010, 2011, 2012,
    2010, 2011, 2012,
    2010, 2011, 2012
] ,
    'team': [
        'manu', 'manu',
        'manu', 'chealse',
        'RMadrid', 'RMadrid',
        'ValenciaCF', 'ValenciaCF',
        'ValenciaCF'
] ,
    'wins': [30, 28, 32, 29, 32, 26, 21, 17, 19],
    'draws': [6, 7, 4, 5, 4, 7, 8, 10, 8],
    'losses': [2, 3, 2, 4, 2, 5, 9, 11, 11]
}
football = pd.DataFrame(data , columns = [
    'year', 'team', 'wins', 'draws', 'losses'
]
)
print(football)
