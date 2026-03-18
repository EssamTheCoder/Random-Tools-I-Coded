print("Random Password Generator");
print("V1.0\n");
from random import choice as c

# Colour Lists
reds = ['Red 0','Red 0',
		'Red 1','Red 1',
		'Red 2','Red 2',
		'Red 3','Red 3',
		'Red 4','Red 4',
		'Red 5','Red 5',
		'Red 6','Red 6',
		'Red 7','Red 7',
		'Red 8','Red 8',
		'Red 9','Red 9',
		'Red +2','Red +2',
		'Red Reverse','Red Reverse',
		'Red Skip','Red Skip',
		'Red Flip','Red Flip']

blues = ['Blue 0','Blue 0',
		'Blue 1','Blue 1',
		'Blue 2','Blue 2',
		'Blue 3','Blue 3',
		'Blue 4','Blue 4',
		'Blue 5','Blue 5',
		'Blue 6','Blue 6',
		'Blue 7','Blue 7',
		'Blue 8','Blue 8',
		'Blue 9','Blue 9',
		'Blue +2','Blue +2',
		'Blue Reverse','Blue Reverse',
		'Blue Skip','Blue Skip',
		'Blue Flip','Blue Flip']

greens = ['Green 0','Green 0',
		'Green 1','Green 1',
		'Green 2','Green 2',
		'Green 3','Green 3',
		'Green 4','Green 4',
		'Green 5','Green 5',
		'Green 6','Green 6',
		'Green 7','Green 7',
		'Green 8','Green 8',
		'Green 9','Green 9',
		'Green +2','Green +2',
		'Green Reverse','Green Reverse',
		'Green Skip','Green Skip',
		'Green Flip','Green Flip']

yellows = ['Yellow 0','Yellow 0',
		'Yellow 1','Yellow 1',
		'Yellow 2','Yellow 2',
		'Yellow 3','Yellow 3',
		'Yellow 4','Yellow 4',
		'Yellow 5','Yellow 5',
		'Yellow 6','Yellow 6',
		'Yellow 7','Yellow 7',
		'Yellow 8','Yellow 8',
		'Yellow 9','Yellow 9',
		'Yellow +2','Yellow +2',
		'Yellow Reverse','Yellow Reverse',
		'Yellow Skip','Yellow Skip',
		'Yellow Flip','Yellow Flip']

wilds = ['Wild','Wild','Wild +4','Wild +4']

purples = ['Purple 0','Purple 0',
		'Purple 1','Purple 1',
		'Purple 2','Purple 2',
		'Purple 3','Purple 3',
		'Purple 4','Purple 4',
		'Purple 5','Purple 5',
		'Purple 6','Purple 6',
		'Purple 7','Purple 7',
		'Purple 8','Purple 8',
		'Purple 9','Purple 9',
		'Purple +5','Purple +5',
		'Purple Reverse','Purple Reverse',
		'Purple Skip All','Purple Skip All',
		'Purple Flip','Purple Flip']

magentas = ['Magenta 0','Magenta 0',
		'Magenta 1','Magenta 1',
		'Magenta 2','Magenta 2',
		'Magenta 3','Magenta 3',
		'Magenta 4','Magenta 4',
		'Magenta 5','Magenta 5',
		'Magenta 6','Magenta 6',
		'Magenta 7','Magenta 7',
		'Magenta 8','Magenta 8',
		'Magenta 9','Magenta 9',
		'Magenta +5','Magenta +5',
		'Magenta Reverse','Magenta Reverse',
		'Magenta Skip All','Magenta Skip All',
		'Magenta Flip','Magenta Flip']

oranges = ['Orange 0','Orange 0',
		'Orange 1','Orange 1',
		'Orange 2','Orange 2',
		'Orange 3','Orange 3',
		'Orange 4','Orange 4',
		'Orange 5','Orange 5',
		'Orange 6','Orange 6',
		'Orange 7','Orange 7',
		'Orange 8','Orange 8',
		'Orange 9','Orange 9',
		'Orange +5','Orange +5',
		'Orange Reverse','Orange Reverse',
		'Orange Skip All','Orange Skip All',
		'Orange Flip','Orange Flip']

teals = ['Teal 0','Teal 0',
		'Teal 1','Teal 1',
		'Teal 2','Teal 2',
		'Teal 3','Teal 3',
		'Teal 4','Teal 4',
		'Teal 5','Teal 5',
		'Teal 6','Teal 6',
		'Teal 7','Teal 7',
		'Teal 8','Teal 8',
		'Teal 9','Teal 9',
		'Teal +5','Teal +5',
		'Teal Reverse','Teal Reverse',
		'Teal Skip All','Teal Skip All',
		'Teal Flip','Teal Flip']

darkWilds = ['Wild','Wild','Wild +Colour','Wild +Colour']


#% Function Varaibles
deck = {} #Initiates an empty dict that will house our dec
lightCards = [] #Makes an empty list to store the keys for our dicts

#Puts all the colour lists in two side-lists (yknow, the side of the deck theyre on)
light = [reds,blues,greens,yellows,wilds] 
dark = [purples,oranges,magentas,teals,darkWilds]

#Intialises variables for colour and card selections
colour = 1
card = 1 
colour2 = -1
card2 = -1 


def main():
	for d in range(0,56): #(d for deck) A for loop that selects card pairs and adds them to the deck dictionary.
		# Light-side card
		colour = c(light)
		card = c(colour)
		lightCards.append(card)
		colour.remove(card)

		# Dark-side card
		colour2 = c(dark)
		card2 = c(colour2) 
		colour2.remove(card2)
		deck[f'{card}'] = f'{card2}'

		#Garbage Collector for empty lists
		if len(colour) == 0:
			light.remove(colour)

		if len(colour2) == 0:
			dark.remove(colour2)
	
	for p in range(0,len(lightCards)): #(p for print) prints all 56 pairs of cards in order but *readibly*
		print(f'{lightCards[p]} -> {deck[lightCards[p]]}')

main()