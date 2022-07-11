print("Welcome to my python quiz game :)")

enter = input('Type enter to continue or just type no to dont ig: ')


if enter.lower() != "yes":
    quit


score = 0


China = input('What is capital of china: ')
if China.lower() == "beijing":
    print('look whos a smarty pants 👀')
    score += 1
else:
    print('Bing Bong wrong bitch')


Betty = input('How old is betty white: ')
if Betty.lower() == "99":
    print('yes but unfortunately she ded so')
    score += 1
else:
    print("cmn bro shes ded have some respect")


Milo = input('is milo the cutest rabbit ever or what: ')
if Milo.lower() == 'yes':
    print('that is indeed very much correct sir')
    score += 1

else:
    print('bitch r u dumb ')


Tri = input('Is the bermuda triangle real: ')
if Tri.lower() == "yes":
    print('that is the correct attidude😝')
    score += 1
else:
    print('dont be "brainwahsed" by the gov peasant')

print("your total score is: " + str(score))
if score <= 0:
    print('nice playing loser')
elif score <= 2:
    print('well played dude')
