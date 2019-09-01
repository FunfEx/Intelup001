size = float(input('METROS² A SEREM PINTADOS :'))
lts = (size/6)*1.1#add 10% de folga
latas = int(lts/18)
galões_bacanas = int(lts/3.6)
if lts% 18!= 0:
    lts += 1
if lts% 3.6!=0:
    galões_bacanas += 1
mistura = int(lts/18)
mistura2 = int(lts - (mistura*18))/3.6
if lts-(mistura*18)%3.6 !=0:
    mistura2 += 1
print('LATAS SÃO:', lts, 'VALOR É:', lts*80)
print('GALÕES SÃO:', galões_bacanas, 'VALOR É:',    galões_bacanas*25)
print('LATAS SÃO:', mistura, mistura2, 'TOTAL:', (mistura*80)+(mistura2*25))
