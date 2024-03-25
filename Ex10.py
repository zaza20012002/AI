def est_trie_croissant(tab):
    for i in range(len(tab) - 1):
        if tab[i] > tab[i + 1]:
            return False
    return True


    
tab = [2,3,20,12,14]

    
if est_trie_croissant(tab):
    print("Le tableau est trié dans l'ordre croissant.")
else:
    print("Le tableau n'est pas trié dans l'ordre croissant.")


