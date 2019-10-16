# PragueControl
Controle de pragas

No Vale do Ribeira, uma espécie de fungo está atacando as bananeiras. A pedido do presidente, pesquisadores brasileiros inventaram um remédio que elimina essa infestação por completo. Ainda não contente com o efeito do remédio em somente uma bananeira, os pesquisadores também criaram um mecanismo que, dia após dia, espalha o remédio para todas as bananeiras adjacentes às bananeiras cujo remédio está ativo. Por exemplo, o remédio é aplicado em uma bananeira específica. No dia seguinte, ele se espalha para as bananeiras adjacentes a esta, e no outro, para as adjacentes às adjacentes da inicial, e assim por diante, até que toda a infestação seja eliminada. Desenvolva um programa que, dadas as bananeiras infectadas e as coordenadas da bananeira onde será aplicado o remédio, verifique a quantidade de dias para que todas as bananeiras estejam curadas.
Entrada

A primeira linha de entrada é composta por um número inteiro representando a quantidade de casos de teste. Cada caso de teste é composto por A (2 ≤ A ≤ 100) e B (2 ≤ B ≤ 100) representando a quantidade de linhas e a quantidade de colunas da matriz, respectivamente. Em seguida, será dada uma matriz binária A x B, com 0 indicando que não há bananeira e 1 indicando que há uma bananeira infectada. Posteriormente, serão dadas as coordenadas iniciais X (1 ≤ X ≤ A) e Y (1 ≤ Y ≤ B) onde será aplicado o remédio. Não haverá bananeiras sem bananeiras adjacentes, isto é, o remédio sempre conseguirá alcançar todas as bananeiras.
Saída

Para cada caso de teste, imprima a quantidade de dias para que a infestação seja completamente eliminada.
Exemplo de entrada

2
3 4
1 0 1 1
1 0 0 1
0 1 1 0
1 1
5 3
1 0 0
0 1 0
0 1 1
0 1 1
1 0 0
2 2

Exemplo de saída

5
3
