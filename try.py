from collections import ChainMap
a  = {"name":'james', "age":20,"address":'thomas salako street,ogba',"phone":37822}
b  = {"name":'olu', "age":36,"address":'oke ira street,ogba',"phone":98876}
c  = {"name":'kate', "age":80,"address":'kington kete street,ogba',"phone":174528}

d = ChainMap(a,b,c)
print(d)