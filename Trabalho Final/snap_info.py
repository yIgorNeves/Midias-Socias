import json

def main():
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
        del aux[10:17]
        print(len(aux))
        # aux_int=[]
        # for valor in aux:
        #     aux_int.append(int(valor))

        marca_id['values']=aux
        print("\nValues: %s" % marca_id['values'])
    
    ##################### SALVANDO O JSON ###################### 
    with open('snap.json', 'w') as f:
        json.dump(dicionario_lido,f)

    ##################### LENDO O JSON ###################### 
    print("\n\n##################### LENDO O JSON SALVO ######################")                             
    dicionario_aux={}
    with open('snap.json') as f:
       dicionario_aux = json.load(f)
        
    #input("vai salvar o arquivo linha por linha json")       
    ##################### SALVANDO O JSON LINHA POR LINHA ###################### 
    with open('snap_linha.json', 'w') as f:
       for marca_id in dicionario_aux:
           for item in marca_id:
               print(marca_id[item])
               f.write('%s\n' % (json.dumps({item: marca_id[item]})))
    
    ##################### LENDO O JSON LINHA POR LINHA ######################
    with open('snap_linha.json') as f:
        for line in f:
            line = line.strip()
            json_line = json.loads(line)
            print (json_line.keys())
            marca_id = list(json_line.keys()).pop()
            marca_data = json_line[marca_id]
            print ("%s:%s" % (marca_id, marca_data)) 
    
    ##################### SALVANDO COMO TSV ###################### 
    with open('snap_csv.csv', 'w') as f:
        f.write("name,interest_id,values\n")
        for marca_id in dicionario_aux:    
            f.write("%s,%s,%s\n" %( 
                marca_id['name'],
                marca_id['interest_id'],
                marca_id['values']))      
if __name__ == "__main__":   
    main()