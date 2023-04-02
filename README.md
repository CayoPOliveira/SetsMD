<!-- @format -->

# Códigos referẽntes a trabalhos da disciplina Matemática Discreta

## Conjuntos: objetivo

Considere o conjunto A = {1, 2, 3, 4, 5}.
Faça um programa para classificar todas as 33.554.432 relações binárias no conjunto A.
A resposta deve ser retornada em um arquivo texto, da forma como o exemplo:

-   Seja A = {1, 2} teremos então 16 relações binárias em A que podem ser classificadas em:
    Simétrica (S), Transitiva (T), Reflexiva (R), Equivalência (E), irreflexiva (I), função (Fu), função
    bijetora (Fb), Função sobrejetora (Fs) e função injetora (Fi).
    A saída deve ser um arquivo texto contendo:

```
{} STI
{(2,2)} ST
{(2,1)} TI
{(2,1)(2,2)} T
{(1,2)} TI
{(1,2)(2,2)} TFu
{(1,2)(2,1)} SIFuFbFsFi
{(1,2)(2,1)(2,2)} S
{(1,1)} ST
{(1,1)(2,2)} RSTEFuFbFsFi
{(1,1)(2,1)} TF
{(1,1)(2,1)(2,2)} RT
{(1,1)(1,2)} T
{(1,1)(1,2)(2,2)} RT
{(1,1)(1,2)(2,1)} S
{(1,1)(1,2)(2,1)(2,2)} RSTE
```

Determine o tempo em que cada teste foi executado e o tamanho do arquivo texto resultado.

## Conjuntos: executando

Para executar o programa é nescessário python 3, você pode instala-lo com o seguinte comando:

```
sudo apt install python3
```

É necessário ter instalado um sistema de gerenciamento de pacotes padrão do python que é o pip, baixado através do comando:

```
sudo apt install python3-pip
```

Através do pip é nescessário instalar o pacote Matplotlib para gerar o gráfico, use o seguinte comando:

```
pip install matplotlib
```

Por fim, para executar o programa utilize o comando:

```
python3 conjuntos.py
```

## Conjuntos: Sobre o código

Como o programa descrevia foi executado e criado os arquivos para um conjunto de 5 elementos, porém foi expandida a simulação para observar o crescimento exponencial do problema e gerar um gráfico, alterando o valor de **n** na linha 135 do arquivo [conjuntos.py](conjuntos.py), para fins de teste não recomendo executar a partir de 6 elementos a menos que a máquina de testes possua boas configurações.

## Relações: objetivo

Fechamento Reflexivo, Simétrico e Transitivo. Faça a implementação de funções que:

1. Recebe um conjunto A, como lista, e uma relação R, como lista de pares ordenados com elementos em A, retornando a representação matricial de R.
2. Recebe a representação matricial de uma relação binária R em um
   conjunto finito e retorna a matriz que representa o fechamento
   reflexivo dessa relação R;
3. Recebe a representação matricial de uma relação binária R em um
   conjunto finito e retorna a matriz que representa o fechamento
   simétrico dessa relação R;
4. Recebe a representação matricial de uma relação binária R em um
   conjunto finito e retorna a matriz que representa o fechamento
   transitivo dessa relação R, usando o algoritmo 1, página 550, livro
   do Rosen;
5. Recebe a representação matricial de uma relação binária R em um
   conjunto finito e retorna a matriz que representa o fechamento
   transitivo dessa relação R, usando o algoritmo de Warshall.
6. Recebe a representação matricial de uma relação binária R em um
   conjunto finito e retorna a matriz que representa a menor relação
   de equivalência que contêm essa relação R.
7. Recebe um conjunto A, como lista, e a representação matricial de R,
   imprimindo a relação R como pares ordenados.

## Relações: executando

Para executar o programa é nescessário python 3, e para executar o programa utilize o comando:

```
python3 relacoes.py
```

## Relações: Sobre o código

O programa gera a vizualização da matriz zero-um da relação, e a partir dela gera o Fecho Reflexivo, Simétrico e Transitivo, também a menor relação de equivalência, a partir disso faz os testes das relações usando os algoritmos desenvolvidos no programa [conjuntos.py](./conjuntos.py)
