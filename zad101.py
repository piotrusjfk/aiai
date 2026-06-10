def pasek_postepu(zrobione, wszystko):
    procent = zrobione / wszystko
    ilosc_hashy = round(procent * 10)
    ilosc_minusow = 10 - ilosc_hashy

    rdy = '#' * ilosc_hashy
    nrdy = '-' * ilosc_minusow

    print(f"[{rdy}{nrdy}]")
pasek_postepu(1 , 10)