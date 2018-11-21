import xml.etree.ElementTree as ET
import texttable as tt
import fpdf

leerarchivo = ET.parse('animelist.xml')
raiz = leerarchivo.getroot()
ListaType = []
ListaNombre = []
ListaEps = []
ListaNota = []
capitulos = 0
tv = 0
ova = 0
special = 0
movie = 0
def Buscar():
    for nombre in raiz.findall(".anime/series_title"):
        ListaNombre.append(nombre.text)

    for tipo in raiz.findall(".anime/series_type"):
        ListaType.append(tipo.text)
        global tv
        global special
        global movie
        global ova
        if tipo.text == "TV":
            tv = tv + 1
        elif tipo.text == "Special":
            special = special + 1
        elif tipo.text == "Movie":
            movie = movie + 1
        elif tipo.text == "OVA":
            ova = ova + 1

    for caps in raiz.findall(".anime/series_episodes"):
        ListaEps.append(caps.text)
        global capitulos
        capitulos = capitulos + int(caps.text)

    for nota in raiz.findall(".anime/my_score"):
        ListaNota.append(nota.text)

#def ListaGlobal():
#    ValorActual = 0
#    ValorMaxLista = len(ListaNombre)
#    global ListaGlobal
#    ListaGlobal = []
#    while ValorMaxLista != ValorActual:
#        ListaGlobal.append(ListaNombre[ValorActual])
#        ListaGlobal.append(ListaType[ValorActual])
#        ListaGlobal.append(ListaEps[ValorActual])
#        ListaGlobal.append(ListaNota[ValorActual])
#        ValorActual = ValorActual + 1

def PrintColumnas():
    pdf = fpdf.FPDF(format='A4')
    pdf.add_page()
    pdf.add_font('DejaVu', '', 'DejaVuSansCondensed.ttf', uni=True)
    pdf.add_font('DejaVu', 'B', 'DejaVuSansCondensed.ttf', uni=True)
    Tabla = tt.Texttable()
    Nombres = ["Nombre del Anime", "Tipo", "Episodios", "Nota"]
    Valor = 0
    Tabla.header(Nombres)
    pdf.set_font("DejaVu", 'B', size=14)
    pdf.cell(110,10, "Nombre del Anime", 0, 0,"L")
    pdf.cell(27,10, "Tipo", 0, 0,"C")
    pdf.cell(27,10, "Episodios", 0, 0,"C")
    pdf.cell(27,10, "Nota", 0, 0,"C")
    pdf.ln()
    pdf.set_font("DejaVu", size=11)
    for elemento in zip(ListaNombre, ListaType, ListaEps, ListaNota):
        Tabla.add_row(elemento)
        if Valor % 2 == 0:
            pdf.set_fill_color(r=220)
        else:
            pdf.set_fill_color(r=240)
        pdf.set_font("DejaVu", size=9)
        pdf.cell(110,6, ListaNombre[Valor], 0, 0,"L", True)
        pdf.set_font("DejaVu", size=11)
        pdf.cell(27,6, ListaType[Valor], 0, 0,"C", True)
        pdf.cell(27,6, ListaEps[Valor], 0, 0,"C", True)
        pdf.cell(27,6, ListaNota[Valor], 0, 0,"C", True)
        pdf.ln()
        Valor = Valor + 1
    print(Tabla.draw())
    pdf.set_font("DejaVu", size=15)
    pdf.ln()
    pdf.cell(110,10, "Episodios Totales : " + str(capitulos) , 0, 0,"L")
    pdf.ln()
    pdf.set_font("DejaVu", size=13)
    pdf.cell(50,10, "TV : " + str(tv) , 0, 0,"L")
    pdf.cell(59,10, "Peliculas : " + str(movie) , 0, 0,"L")
    pdf.cell(59,10, "Especiales : " + str(special) , 0, 0,"L")
    pdf.cell(59,10, "OVAS : " + str(special) , 0, 0,"L")
    pdf.output("animelist.pdf","F")
Buscar()
#ListaGlobal()
PrintColumnas()
