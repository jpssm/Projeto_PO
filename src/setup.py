from __future__ import print_function
from ortools.linear_solver import pywraplp
import numpy as np
import pandas as pd
import csv

def csv_to_array(array, csv_file):
    with open(csv_file) as csvfile:
        array = pd.read_csv(csv_file, header=None)
        array.to_csv("teste.csv")

    return array

M = 5570     #Número de municípios que recebem cestas
P = 5570    #Número de municípios que produzem alimentos
A = 100      #Número de alimentos
N = 0        #Número de nutrientes

#Parametros

Q = 0                                              #Quantidade cestas a serem distribuídas no município m ∈ M
R = np.zeros(shape = (N), dtype = np.int32)        #Requisito (em g) do nutriente n ∈ N para cada cesta
O = np.zeros(shape = (N,A), dtype = np.int32)      #Oferta do nutriente n ∈ N (em g por kg) do alimento a ∈ A
D = np.zeros(shape = (A,P), dtype = np.int32)      #Disponibilidade (em toneladas) do alimento a ∈ A no produtor p∈P
C = np.zeros(shape = (A,P), dtype = np.int32)      #Custo (em reais por tonelada) do alimento a ∈ A no produtor p ∈ P.
T = np.zeros(shape = (P,M), dtype = np.int32)      #Custo (em reais por tonelada) de transporte do produtor p ∈ P até o município m ∈ M.

D = csv_to_array(D, "../DATASET/custo_de_produção.csv")

print(D)

# print("#PARAMETROS")

# #Variáveis
# solver = pywraplp.Solver('simple_lp_program', pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)
# d_amp = {} #quantidade (em kg) comprada de alimento a ∈ A pelo unicípio m ∈ M do município p ∈ P.
# for a in range(A):
#     for m in range(M):
#         for p in range(P):
#             if(D[a][p] > 0): 
#                 d_amp[(a,m,p)] = solver.NumVar(0,D[a][p]) 

# #Restrições
# for a in range(A):
#     ct = [[solver.Constraint(D[a][p], D[a][p]) for a in range(A)] for p in range(P)]

#     for m in range(M):
#         ct.SetCoefficient(d_amp[a][m], 1)

# for a in range(A):
#     ct = [[solver.Constraint(Q[m]*R[n]) for m in range(M)] for n in range(N)]

#     #for m in range(M):
#         #ct.SetCoefficient(d_amp[a][m], [O[n][a] for n in range(N)] for a in range(A))


# #Alimento disponível


# #Função Objetivo
# objective = solver.Objective()
# for amp in d_amp:
#     objective.setCoefficient(d_amp[amp],C[a][p]+T[p][m])
    
# objective.SetMinimization()
# #Resolução do problema
