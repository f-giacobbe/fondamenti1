#variabile sentinella - conviene avere come guardia del while una singola variabile booleana

#calcolo costo n oggetti
def checkout():
	total = 0
	count = 0
	
	moreItems = True		#variabile sentinella
	
	while moreItems:
		price = float(input("Enter price of item (0 when done): "))
		if price != 0:
			count += 1
			total += price
			print("Subtotal: $", total)	#subtotale (totale corrente)
		else:
			moreItems = False
			
	average = total/count
	
	print("Total items:", count)
	print("Total $", total)
	print("Average price of items $", average)

#in questo caso la fine della funzione è determinata dalla prima istruzione non indentata rispetto alla definizione della funzione
		
checkout()
