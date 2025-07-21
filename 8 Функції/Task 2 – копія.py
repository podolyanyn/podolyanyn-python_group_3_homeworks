print('Enter the country and push enter, next Enter the capital and push enter:')

def make_country(  name=input(),  capital=input()):

    dict_country = dict()
    dict_country.update({name : capital})
    print(dict_country)

make_country()