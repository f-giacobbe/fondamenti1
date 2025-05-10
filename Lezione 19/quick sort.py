l = [5, 4, 1, 29, 8, 18, 63, 2]

#complessità asintotica -> n log n
#nel peggiore dei casi (lista già ordinata) -> n^2
#non richiede lista ausiliaria
#viene preso il primo elemento della lista (il pivot), e ridistribuisco l'intera lista basandomi sul pivot
#dopodiché, richiamo la funzione sulle due parti in modo ricorsivo
