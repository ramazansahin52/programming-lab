#verilen kelime tersten okunuşu ile aynı ise True farklı ise False döndüren fonksiyon
def pandigital(kelime):
    if(kelime==kelime[::-1]):
        return True
    else:
        return False
print((pandigital("kavak")))
