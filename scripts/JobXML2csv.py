# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import xml.etree.ElementTree as ET
import pandas as pd
import sys

# <codecell>

archivo = sys.argv[1]
salida = sys.argv[2]

tree = ET.parse(archivo)
root = tree.getroot()

# <codecell>

puntos = root[0].findall('PointRecord')

estaciones = root[0].findall('StationRecord')

prismas = root[0].findall('TargetRecord')

puntgrid = root[1].findall('Point')


dfpun = []#pd.DataFrame()
dfest = []#pd.DataFrame()
dfpri = []#pd.DataFrame()
dfpgrid = []#pd.DataFrame()

# <codecell>

for j in puntos:
    dfpun.append(pd.DataFrame(
                         {i.tag:i.text for i in j.iter()}
                         ,index=[j.attrib['ID']]))
dfpun = pd.concat(dfpun)

for j in estaciones:
    dfest.append(pd.DataFrame(
                         {i.tag:i.text for i in j.iter()}
                         ,index=[j.attrib['ID']]))
dfest = pd.concat(dfest)

for j in prismas:
    dfpri.append(pd.DataFrame(
                         {i.tag:i.text for i in j.iter()}
                         ,index=[j.attrib['ID']]))
dfpri = pd.concat(dfpri)

# <codecell>

for j in puntgrid:
    dfpgrid.append(pd.DataFrame(
                         { i.tag: i.text for i in j.find('Grid') }
                         ,index=[j.find('ID').text]))

dfpgrid = pd.concat(dfpgrid)

# <codecell>

dfest = dfest.reindex(dfpun.StationID)
dfpri = dfpri.reindex(dfpun.TargetID)
dfpgrid = dfpgrid.reindex(dfpun.index.values)

# <codecell>

dfest = dfest.set_index(dfpun.index)
dfpri = dfpri.set_index(dfpun.index)
dfpgrid = dfpgrid.set_index(dfpun.index)

# <codecell>

dfpri = dfpri.rename(columns={i:'Prisma_'+i for i in ['MeasuredHeight','MeasurementMethod','VerticalOffset','HorizontalOffset'] })
dfpun = dfpun.rename(columns={i:'Lect_'+i for i in ['East', 'Elevation', 'North', 'VerticalOffset'] })
dfest = dfest.rename(columns={i:'Est_'+i for i in ['Note', 'Notes'] })


dfpun = dfpun.join(dfest)
dfpun = dfpun.join(dfpri)
dfpun = dfpun.join(dfpgrid)

# <codecell>

columnas = ['StationName','Name','EDMDistance','HorizontalCircle','VerticalCircle','TheodoliteHeight',
            'TargetHeight','East','North','Elevation','Code','PrismType','PrismConstant',
            'Prisma_HorizontalOffset','Prisma_VerticalOffset','Method','Classification']

columnasb = ['Estacion','Visado','Distancia','ang_H','ang_V','H_Instrumento',
            'H_mira','Este','Norte','Cota','TEXT','Tipo_prisma','constante',
            'Prisma_DH','Prisma_DV','Tipo_Obs','Tipo_pto']

# <codecell>

dfpun = dfpun[columnas].rename(columns={i:j for i,j in zip(columnas,columnasb)})

# <codecell>

dfpun.to_csv(salida, encoding='utf-8')

