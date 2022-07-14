import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('datos\estudiante.csv')
print('ESTUDIANTES')
print(df)

df1 = pd.read_csv('datos\listado_de_asistencia.csv')
print('ASISTENCIAS')
print(df1)

asistencias = pd.merge(df,df1,  how="right" )
print('ASISTENCIAS Y ESTUDIANTES')
print(asistencias)

print('ASISTENCIAS Y ESTUDIANTES POR CEDULA = 2233445566')
print(asistencias[asistencias.cedula == 2233445566])

asistencias[asistencias.cedula == 2233445566].to_csv('datos\datos_de_2233445566.csv', index=True)

asistencias[asistencias.cedula == 2233445566]['materia'].value_counts().plot(kind='bar')
plt.show()