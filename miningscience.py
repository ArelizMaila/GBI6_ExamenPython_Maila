#Resolver la pregunta 1 
##i. download_pubmed: para descargar la data de 
#PubMed utilizando el ENTREZ de Biopython. El parámetro de entrada para la función es el keyword.
from Bio import Entrez 
import re
import csv

def download_pubmed(keyword): 
    """Docstring download_pubmed.
    """
#necesario decirle a NCBI quien eres 
    Entrez.email = "areliz.maila@gmail.com"
    handle = Entrez.esearch(db="pubmed", 
                            term=keyword,
                            usehistory="y")
    record = Entrez.read(handle)
    id_list = record["IdList"]
    record["Count"]
    webenv = record["WebEnv"]
    query_key = record["QueryKey"]
    handle = Entrez.efetch(db="pubmed",
                            rettype="medline", 
                            retmode="text", 
                            retstart=0,
    retmax=543, webenv=webenv, query_key=query_key)
    filename = keyword+".txt"
    out_handle = open(filename, "w")
    data = handle.read()
    handle.close()
    out_handle.write(data)
    out_handle.close()
    return

#ii. map_science: para su data replique el ejemplo de MapOfScience, donde los puntos resaltados son al menos 5 países

def map_science(tipo):
    """funcion para crear el mapeado en base a la base de datos que obtuvimos con anterioridad"""
    #if tipo == "AD":
    with open(tipo) as f:
        my_text = f.read()
    my_text = re.sub(r'\n\s{6}', ' ', my_text)  
    zipcodes = re.findall(r'[A-Z]{2}\s(\d{5}), USA', my_text)
    unique_zipcodes = list(set(zipcodes))
    zip_coordinates = {}
    with open('zip_coordinates.txt') as f:
        csvr = csv.DictReader(f)
        for row in csvr:
         zip_coordinates[row['ZIP']] = [float(row['LAT']), float(row['LNG'])]
    zip_code = []
    zip_long = []
    zip_lat = []
    zip_count = []
    for z in unique_zipcodes:
    # encontrar coordenadas 
        if z in zip_coordinates.keys():
            zip_code.append(z)
            zip_lat.append(zip_coordinates[z][0])
            zip_long.append(zip_coordinates[z][1])
            zip_count.append(zipcodes.count(z))
#Libreria matplotlib para la creaccion de graficos en dos dimensiones        
    import matplotlib.pyplot as plt
    plt.scatter(zip_long, zip_lat, s = zip_count, c= zip_count)
    plt.colorbar()
# Aplica solo para U.S.A
    plt.xlim(-125,-65)
    plt.ylim(23, 50)
# add a few cities for reference (optional)
    ard = dict(arrowstyle="->")
    plt.annotate('Texas', xy = (-98.5456116, 31.2638905), 
                   xytext = (-98.5456116, 31.2638905), arrowprops = ard)
    plt.annotate('Pensilvania', xy = (-77.7278831, 40.9699889), 
                   xytext = (-77.7278831, 40.9699889), arrowprops= ard)
    plt.annotate('California', xy = (-118.755997, 36.7014631), 
                   xytext = (-118.755997, 36.7014631), arrowprops= ard)
    plt.annotate('Ohio', xy = (-82.6881395, 40.2253569), 
                   xytext = (-82.6881395, 40.2253569), arrowprops= ard)
    plt.annotate('Arizona', xy = (-111.763275, 34.395342), 
                   xytext = (-111.763275, 34.395342), arrowprops= ard)
    plt.annotate('Tennessee', xy = (-86.2820081, 35.7730076), 
                   xytext = (86.2820081, 35.7730076), arrowprops= ard)
    params = plt.gcf()
    plSize = params.get_size_inches()
    params.set_size_inches( (plSize[0] * 3, plSize[1] * 3) )
    return plt.show()




