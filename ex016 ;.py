print('=-='*30)
size = float(input('METROS² À SEREM PINTADOS :'))
lts = (size/3)
latas = int(lts/18)
if  lts% 18 !=0:
    lts += 1
print('=-='*30)
print('VOCE TERA QUE COMPRAR', lts, 'QUANTIA DE LATAS')
print('SEU PREÇO TOTAL FICA EM', lts*80)
print('--'*40)
