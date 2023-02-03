# Prolog
Foram realizadas Atividade para a familiarização da linguagem prolog. As execuções foram feitas no site swish.swi-prolog.org. Nesse sentido, foram dadas algumas informações de uma árvore genealógica a seguir:
 - homem(joao)
 - homem(joaquim).
 - homem(marcelino).
 - homem(aristedes).

 - mulher(joana).
 - mulher(serafina).
 - mulher(maria).
 - mulher(ana).

 - progenitor(joao, joaquim).
 - progenitor(joao, serafina).
 - progenitor(joana, joaquim).
 - progenitor(joana, serafina).

 - progenitor(serafina, maria).
 - progenitor(serafina, ana).

 - progenitor(joaquim, marcelino).

 - progenitor(marcelino, aristedes).
 - progenitor(maria, aristedes).

A atividade está toda em arquivo .txt com todas as respostas.

---
### Formulação das questões porpostas

 - 1- pai(josé, joaquim).
 - 2- mae(joana, Filhos).
 - 3- primo(marcelino, [joao, joaquim, marcelino, aristedes, joana, serafina, maria, ana], Primos).
 - 4- tio(Tio, Sobrinha).
 - 5- ascendente(aristedes,[joao, joaquim, marcelino, aristedes, joana, serafina, maria, ana], Ascendentes). 
 - 6- irmaoirma(maria,[joao, joaquim, marcelino, aristedes, joana, serafina, maria, ana], Irmaos, Irmas)