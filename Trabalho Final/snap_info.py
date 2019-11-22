import json

def main():
    dict_marcas = {}
  ##################### LENDO O JSON ###################### 
    print("\n\n##################### LENDO O JSON SALVO ######################")                             
    dicionario_lido={}
    with open('snap.json') as f:
        dicionario_lido = json.load(f)

    for marca_id in dicionario_lido:
        print ('************** MARCA ******************')
        print('\nNome: %s' % marca_id['name'])
        aux =[]
        for valor in marca_id['values']:
            aux.append(valor.strip())
        marca_id['values']=aux
        print("\nValues: %s" % marca_id['values'])
    
    ##################### SALVANDO O JSON ###################### 
    with open('snap.json', 'w') as f:
        json.dump(dicionario_lido,f)

    ##################### LENDO O JSON ###################### 
    #print("\n\n##################### LENDO O JSON SALVO ######################")                             
    #dicionario_aux={}
    #with open('snap.json') as f:
    #    dicionario_aux = json.load(f)
        
    #input("vai salvar o arquivo linha por linha json")       
    ##################### SALVANDO O JSON LINHA POR LINHA ###################### 
    #with open('snap_linha.json', 'w') as f:
    #    for marca_id in dicionario_aux:
    #        for item in marca_id:
    #            f.write('%s\n' % (json.dumps({item: marca_id[item]})))

if __name__ == "__main__":   
    main()