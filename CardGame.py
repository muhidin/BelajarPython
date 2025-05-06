# Game Kartu - Nilai Tertinggi dan Terendah
# by Muhidin - NIM 2020130013
import random

# Inisialisasi Variabel konstanta
SUIT_TUPLE = ('Keriting', 'Hati', 'Wajik', 'Waru')
RANK_TUPLE = ('As', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King')

NCARDS = 8

def getCard(deckListIn):
    thisCard = deckListIn.pop()
    return thisCard

def shuffle(deckListIn):
    deckListOut = deckListIn.copy()
    random.shuffle(deckListOut)
    return deckListOut

# Kode Utama
print('Selamat Datang di Game Kartu')
print('Silahkan pilih kartu berikutnya yang ditampilkan lebih tinggi atau lebih rendah dari kartu saat ini')
print('Jika Anda benar, Anda mendapatkan 20 poin; jika salah dikurangi 15 poin')
print('Kamu mendapat 50 poin untuk mulai')
print('')

startingDeckList = []
for suit in SUIT_TUPLE:
    for thisValue, rank in enumerate(RANK_TUPLE):
        cardDict = {'rank': rank, 'suit': suit, 'value': thisValue + 1}
        startingDeckList.append(cardDict)

score = 50

while True:
    print();
    gameDeckList     = shuffle(startingDeckList)
    currentCardDict  = getCard(gameDeckList)
    currentCardRank  = currentCardDict['rank']
    currentCardSuit  = currentCardDict['suit']
    currentCardValue = currentCardDict['value']
    print('Kartu saat ini adalah', currentCardRank, currentCardSuit)
    print()

    for cardNumber in range(0, NCARDS):
        answer = input('Kartu berikutnya lebih tinggi (t) atau rendah (r)? (tekan t atau r): ')
        nextCardDict = getCard(gameDeckList)
        nextCardRank = nextCardDict['rank']
        nextCardSuit = nextCardDict['suit']
        nextCardValue = nextCardDict['value']
        print('Kartu berikutnya adalah', nextCardRank, '', nextCardSuit)

        if answer == 't':
            if nextCardValue > currentCardValue:
                print('Anda Benar, Nilai + 20!')
                score += 20
            else:
                print('Anda Salah, Nilai - 15!')
                score -= 15

        elif answer == 'r':
            if nextCardValue < currentCardValue:
                print('Anda Benar, Nilai + 20!')
                score += 20
            else:
                print('Anda Salah, Nilai - 15!')
                score -= 15

        print('Skor Anda saat ini adalah', score)
        print()
        currentCardRank = nextCardRank
        currentCardValue = nextCardValue

    goAgain = input('Jika Anda ingin bermain lagi, tekan ENTER atau s untuk selesai: ')
    if goAgain == 's':
        print()
        print('Terima kasih telah bermain!')
        print('Skor akhir Anda adalah', score)
        break
