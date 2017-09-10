cijferICOR=7
cijferPROG=6
cijferCSN=8
som= cijferICOR+cijferPROG+cijferCSN
gemiddelde= float(som/3)
beloning= float(som*30)
overzicht='Mijn cijfers (gemiddeld een '+str(gemiddelde)+') leveren een beloning van € '+str(beloning)+' op!'
print (overzicht)