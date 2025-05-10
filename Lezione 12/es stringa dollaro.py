#utente specifica una stringa in ingresso e noi dobbiamo aggiungere un doppio dollaro all'inizio e alla fine della stringa

#es. <in>=gioco 	-->		<out>=$$gioco$$

stringa = input("Inserisci stringa: ")
stringa1 = "$$" + stringa + "$$"

print(stringa1)
