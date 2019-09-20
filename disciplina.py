# -*- coding: utf-8 -*-

__author__ = "Igor Neves"

import json

def main():
    dict_disciplina={}
    
    dict_disciplina ['CSI001'] = {'Nome':'Analise de Midia Sociais', 'Carga Horaria':'60 Horas', 'Professor':{'Nome':'Felipe Nunes', 'Departamento':'Decsi'}}
    dict_disciplina ['ENP152'] = {'Nome':'Etica e Responsabilidade Socioambiental', 'Carga Horaria':'60 Horas', 'Professor':{'Nome':'Jean Carlos', 'Departamento':'Deemp'}}

    print("##################### DADOS DO DICIONARIO INICIAL ######################")             
    print("Quantidade de elementos: %d" % len(dict_disciplina))
    for disciplina_id in dict_disciplina:
        print ('************** DISCIPLINA ******************')
        print('\tCodigo: %s' % disciplina_id)
        print("\tNome: %s" % dict_disciplina[disciplina_id]['Nome'])   
        print("\tCarga Horaria: %s" % dict_disciplina[disciplina_id]['Carga Horaria'])
        professor=dict_disciplina[disciplina_id]['Professor']
        print('\tProfessor:')
        print('\t\tNome: %s' % professor['Nome'])
        print('\t\tDepartamento: %s' % professor['Departamento'])
    
    print("Todo o dicionario: %s" % dict_disciplina)

    input("Vai salvar o arquivo em formato json")    
    ##################### SALVANDO O JSON ###################### 
    with open('dict_disciplina.json', 'w') as f:
        json.dump(dict_disciplina,f)

    
    input("Vai ler o json")
    ##################### LENDO O JSON ###################### 
    print("\n\n##################### LENDO O JSON SALVO ######################")                             
    dicionario_lido={}
    with open('dict_disciplina.json') as f:
        dicionario_lido = json.load(f)

    for disciplina_id in dicionario_lido:
        print ('************** DISCIPLINA ******************')
        print('\tCodigo: %s' % disciplina_id)
        print("\tNome: %s" % dicionario_lido[disciplina_id]['Nome'])   
        print("\tCarga Horaria: %s" % dicionario_lido[disciplina_id]['Carga Horaria'])
        professor=dicionario_lido[disciplina_id]['Professor']
        print('\tProfessor:')
        print('\t\tNome: %s' % professor['Nome'])
        print('\t\tDepartamento: %s' % professor['Departamento'])
    
    input("vai salvar o arquivo linha por linha json")       
    ##################### SALVANDO O JSON LINHA POR LINHA ###################### 
    with open('dict_disciplina_linha.json', 'w') as f:
        for disciplina_id in dicionario_lido:            
            f.write('%s\n' % (json.dumps({disciplina_id: dicionario_lido[disciplina_id]})))
    

    input("vai ler o arquivo linha por linha json")              
    ##################### LENDO O JSON LINHA POR LINHA ###################### 
    print("\n\n##################### LENDO O JSON LINHA POR LINHA ######################")
    with open('dict_disciplina_linha.json') as f:
        for line in f:
            line = line.strip()
            json_line = json.loads(line)
            print (json_line.keys())
            disciplina_id = list(json_line.keys()).pop()
            disciplina_data = json_line[disciplina_id]
            print ("%s:%s" % (disciplina_id, disciplina_data))    

    
    ##################### SALVANDO COMO TSV ###################### 
    with open('dict_disciplina_tsv.tsv', 'w') as f:
        f.write("disc_id\tdisc_name\tdisc_ch\tdisc_prof\tdisc_profDep\n")
        for disciplina_id in dicionario_lido:
            lista_disciplinas = dicionario_lido[disciplina_id]['Nome']
            num_disciplinas= len(lista_disciplinas)    
            professor=dicionario_lido[disciplina_id]['Professor']       
            f.write("%s\t%s\t%s\t%s\t%s%d\n" %(disciplina_id, 
                dicionario_lido[disciplina_id]['Nome'],
                dicionario_lido[disciplina_id]['Carga Horaria'],
                professor['Nome'],
                professor['Departamento'],
                num_disciplinas ))      

    ##################### LENDO TSV ######################
    print("\n\n##################### LENDO O ARQUIVO TSV ######################")
    with open('dict_disciplina_tsv.tsv') as f:
        for line in f:
            print (line.strip())
            elements = line.strip().split('\t')
            print (elements)

    dict_disciplina_tsv = {}
    with open('dict_disciplina_tsv.tsv') as f:
        f.readline()
        for line in f:
            elements = line.strip().split('\t')
            print(elements)
            dict_disciplina_tsv[elements[0]] = {'Nome':elements[1], 'Carga Horaria':elements[2], 'Professor':{'Nome':elements[3], 'Departamento':elements[4]}}
        for disciplina_id in dict_disciplina_tsv:
            print ('************** DISCIPLINA ******************')
            print('\tCodigo: %s' % disciplina_id)
            print("\tNome: %s" % dict_disciplina_tsv[disciplina_id]['Nome'])   
            print("\tCarga Horaria: %s" % dict_disciplina_tsv[disciplina_id]['Carga Horaria'])
            professor=dict_disciplina_tsv[disciplina_id]['Professor']
            print('\tProfessor:')
            print('\t\tNome: %s' % professor['Nome'])
            print('\t\tDepartamento: %s' % professor['Departamento'])

if __name__ == "__main__":   
    main()