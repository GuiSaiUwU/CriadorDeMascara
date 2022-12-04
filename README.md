# Criador de Máscara

### Coisas a adicionar:
* Uma interface
* Input de inserir o arquivo .skl
* Um vídeo mostrando o resultado LOL

### Explicação:
* Completamente relacionado a criação de animação personalizada no LOL, é necessario que:
* Você saiba criar, e ter conhecimento de mods 3D
* O mímino de conhecimento sobre edição de bin

### Máscara de animação no LOL:
  - O que são e onde são usadas:
    - São usadas nos arquivos .bin de animação, fazem com que uma animação seja máscarada para que o arquivo .anm influencie apenas ossos especificos, exemplo: Uma animação que todos os ossos possuem 0 valor de influência, mas apenas os ossos do braço e mão estão com o valor de 1, a animação vai afetar apenas os ossos do braço e mão, pois tem valor maior que 1 na máscara
    ![](https://github.com/GuiSaiUwU/CriadorDeMascara/blob/Principal/Imagens/Screenshot_1.png)
    - É basicamente uma fileira de valores entre 0 e 1
      - 0 Representa 0% de influência da animação no osso
      - 1 Representa 100% de influência da animação no osso
      - O valor também pode ser quebrado, 0.5 representa 50%, e assim vai.
      ![](https://github.com/GuiSaiUwU/CriadorDeMascara/blob/Principal/Imagens/Screenshot_2.png)
    - Um belo exemplo de onde é usada:
      - Em campeões como o Graves, que possuem animação de recarregar.
      - A Riot faz 1 animação que animam apenas os ossos do braço recarregando, assim não precisando de fazer variaveis do personagem se mechendo enquanto o braço recarrega a arma
      - Ou seja, o Graves possui uma máscara que faz a animação de recarregar influenciar apenas os braços e mãos
     
### Criaçãod de uma máscara:
  - Você precisa ter os ossos ordenados, e saber o ID dos ossos que você quer que a máscara influencie
  - Algum dia quando eu for gravar um videoe explicando sobre animações permanentes eu elaboro melhor isso haha
