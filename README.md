<!-- @format -->

# ConjuntosMD

## Objetivo

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

## Executando

Para executar o programa é nescessário python 3, você pode instala-lo com o seguinte comando:

```
sudo apt install python3
```

Deve ter instalado um sistema de gerenciamento de pacotes padrão do python que é o pip, baixado através do comando:

```
sudo apt install python3-pip
```

Através do pip é nescessário instalar os pacotes:

-   Matplotlib
