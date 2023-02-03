# Resumo capítulo 2

Um agente é tudo que pode ser considerado capaz de perceber seu **ambiente** por meio de **sensores** e agir sobre esse ambiente por intermédio de **atuadores**. 

* Se considerarmos por exemplo o corpo humano como um agente, podemos considerar seus olhos, ouvidos e outros orgãos como sensores que percebem o ambiente ao seu redor e as mãos, baços, pernas e outros orgãos como atuadores.
* Se considerar um agente robótico, câmeras, detectores de faixa de infravermelho, receptores de ondas sonoras e outros aparelhos como sensores e podemos considerar um conjunto de motores como seus atuadores.
* Se considerar um agente de software, as entradas de teclas digitadas, pacote de redes e imagens podem ser considerado como sensores e o ato de exibir uma mensagem na tela ou enviar uma mensagem pode ser considerado seus atuadores.

O termo **percecpção** faz referência às entradas perceptivas de um agente em um determinado instante. Já o termo **sequência de percepções** faz referência ao histórico de todas as entradas perceptivas de um agente. 

Em termos matemáticos, afirmamos que o comportamento do agente é descrito pela **função do agente** que mapeia qualquer sequência de percepções específica para uma ação. O termo: **função agente** se difere de **programa do agente** de modo que: a função de agente é uma descrição matemática abstrata; o programa do agente é uma implementação concreta, executada em um sistema físico.

<br/>
<br/>

## Agente racional

De maneira resumida, um **agente racional** é aquele que faz a coisa certa. 

Quando um agente é colocado em um determinado ambiente, espera-se uma sequência de ações de acordo com as percepções que ele recebe. Essa sequência de ações faz com que o ambiente passe por uma sequência de estados. Se a sequência de estados for desejável, o agente teve bom desempenho. Essa noção de “desejável” é capturada por uma medida de desempenho que avalia qualquer sequência dada dos estados do ambiente.

Ou seja, um agente racional é aquele capaz de selecionar a ação que maximize seu critérito de desempenho para cada sequência perceptiva possível por meio da interpretação da sequência perceptível ou qualquer outro conhecimento que o agente tenha disponível.

Se considerarmos o agente aspirador de pó simples que limpa um quadrado se ele estiver sujo e passa para o outro quadrado se o primeiro não estiver sujo. Para que esse agente seja racional devemos definr primeiro o que é a medida de desempenho, o que se conhece sobre o ambiente e quais são os sensores e atuadores que o agente tem. Supondo que:

* A medida de desempenho ofereça o prêmio de um ponto para cada quadrado limpo em cada período de tempo, ao longo de um “tempo de vida” de 1.000 passos de tempo.
* A “geografia” do ambiente seja conhecida a priori (Lado A e Lado B), mas a distribuição da sujeira e a posição inicial do agente não sejam previamente conhecidas. Quadrados limpos permanecem limpos, e a aspiração limpa o quadrado atual. As ações Esquerda e Direita movem o agente para a esquerda e para a direita, exceto quando isso leva o agente para fora do ambiente; nesse caso, o agente permanece onde está.
* As únicas ações disponíveis são Esquerda, Direita e Aspirar.
* O agente percebe corretamente sua posição e se essa posição contém sujeira.

Sob essas condições afirmamos que o agente é racional e espera-se que seu
desempenho seja pelo menos tão alto quanto o de qualquer outro agente. Mas se por acaso o agente oscila desnecessariamente de um lado para outro quando ambos os lados estão limpos e sua medida de desempenho inclua penalidade de um ponto para cada movimento à esquerda ou à direita, o agente ficará em má situação e será considerado como irracional.
<p align="center">
    <img src="https://user-images.githubusercontent.com/62517334/167521458-bcd158de-3470-430b-a930-64fcf8b5b84b.png">
</p>

<br/>
<br/>

## Racionalidade

Racionalidade e perfeição são conceitos diferentes, analisar a rua e perceber que não há veículos trafegando, então atravessar e ser atingido por um meteoro que caía do espaço é uma atitude racional, mas não perfeita. A racionalidade maximiza o **desempenho esperado**, enquanto a perfeição maximiza o **desempenho real**. Ou seja a racionalidade não depende da oniciência, uma escolha racional depende da sequência de percepções até o momento.

A **autonomia** é um fator importante em agentes racionais. Agentes racionais devem ser autônomos, ou seje, ele deve ser capaz de aprender o que puder para compensar um conhecimento prévio parcial, faltante ou incorreto. Agentes que se baseiam somente no conhecimento anterior de seus projetitas e não em suas próprias percepções **não pode ser considerado autônomo**.

<br/>
<br/>

## Especificações do ambiente de tarefas

Ao projetar um agente, a primeira etapa deve ser sempre especificar o **ambiente de tarefa** de forma tão completa quanto possível. Podemos considerar um **ambiente de tarefas** como um conjunto de especificações: medida de desempenho, o ambiente e os atuadores e sensores do agente. A esse conjunto denominamos **PEAS** (**P**erformance, **E**nvironment, **A**ctuators, **S**ensors — desempenho, ambiente, atuadores, sensores).

* **Medida de desempenho:** Quais serão os objetivos do agente a ser projetado ? Quais serão os parâmetros de comparação para saber se o agente cumpriu ou não o seu objetivo ? Quais são as qualidades desejadas para o agente ?
* **Ambiente:** Em que cenário o agente projetado atuará ? Quais objetos, situações, eventos o agente deve reconhecer e interagir ? Qual o *escopo* do seu agente ?
* **Atuadores:** Quais as ferramentas que seu agente utilizará para interagir com o ambiente ? Quais equipamentos são necessários para o seu agente conseguir atingir o seu objetivo ?
* **Sensores:** Quais equipamentos o agente deve possuir para perceber o ambeinte ao seu redor ? Como o agente irá perceber as mudanças no ambiente ?

<p align="center">
    <img src="https://user-images.githubusercontent.com/62517334/167676671-04344637-adf2-4109-a58a-be42bab836d9.png"/>
</p>

<br/>
<br/>

## Propriedades do ambiente de tarefas

* **Completamente observável** *VERSUS* **parcialmente observável**:
    * Um ambiente de tarefa é de fato **completamente observável** se os sensores detectam todos os aspectos que são relevantes para a escolha da ação; por sua vez, a relevância depende da medida de desempenho.
    * Um ambiente poderia ser **parcialmente observável** devido ao ruído e a sensores imprecisos ou porque partes do estado estão simplesmente ausentes nos dados do sensor — por exemplo, um agente aspirador de pó com apenas um sensor de sujeira local não pode saber se há sujeira em outros quadrados.
* **Agente único** *versus* **multiagente**: 
    * **Agentes únicos:** são aqueles que operam sozinhos, não dependem e não sofrem interferência da ação de outros agentes. Por exemplo: um agente que resolva palavras cruzadas, um agente de correção ortográfica, o agente aspirador de pó...
    * **Multiagente:** são aqueles agentes que de alguma forma interagem com um outro agente B, ou seja, as ações de um agente B irão impactar diretamente na medida de desempenho do agente A. Em uma partida de xadrez por exemplo, cada agente tem como objetivo maximizar sua medida de desempenho e minimizar a medida do inimigo. Caracterizando uma relação competitiva entre os agentes.
        >**multiagentes** podem ser considerados **agentes únicos** desde que tratem as ações dos demais agentes como fenômenos naturais, semlhantes ao vento, chuva, folhas...
* **Determinístico** *versus* **estocástico**: 
    * Se o próximo estado do ambiente é completamente determinado pelo estado atual e pela ação executada pelo agente, dizemos que o ambiente é determinístico.
    *  “estocástico” geralmente implica que a incerteza sobre os resultados é quantificada em termos de probabilidades; um **ambiente não determinístico** é aquele em que as ações são caracterizadas por seus resultados possíveis, sem probabilidade associada a ele. As descrições do ambiente não determinístico são normalmente associadas às medidas de desempenho que exigem que o agente tenha sucesso em todos os resultados possíveis de suas ações.
* **Episódico** *versus* **sequencial**:

    * Em um ambiente de tarefa **episódico**, a experiência do agente é dividida em episódios atômicos. Em cada episódio, o agente recebe uma percepção e em seguida executa uma única ação. É crucial que o episódio seguinte não dependa das ações executadas em episódios anteriores. Ou seja, em ambientes episódicos a escolha da ação de cada episódio só depende exclusivamente do episódio. Por exemplo, um agente que tem de localizar peças defeituosas em uma linha de montagem baseia cada decisão na peça atual,independentemente das decisões anteriores.
    * Em ambientes **sequenciais**, a decisão atual poderia afetar todas as decisões futuras. Jogar xadrez e dirigir um táxi são sequenciais: em ambos os casos, ações em curto prazo podem ter consequências a longo prazo.
* **Estático** *versus* **dinâmico**:
    * Em **ambientes estáticos** o agente não precisa continuar a observar o mundo enquanto está decidindo sobre a realização de uma ação nem precisa se preocupar com a passagem do tempo.
    * Por outro lado, **ambientes dinâmicos** estão continuamente perguntando ao agente o que ele deseja fazer; se ele ainda não tiver se decidido, isso será considerado a decisão de não fazer nada.
    * Se o próprio ambiente não mudar com a passagem do tempo, mas o nível de desempenho do agente se alterar, diremos que o ambiente é **semidinâmico**.
    >Se o ambiente puder se alterar enquanto um agente está deliberando, dizemos que o ambiente é dinâmico para esse agente; caso contrário, ele é estático
* **Discreto** *versus* **contínuo**: A distinção entre discreto e contínuo aplica-se ao estado do ambiente, ao modo como o tempo é tratado, e ainda às percepções e ações do agente.

* **Conhecido** *versus* **desconhecido**:
    * Em um **ambiente conhecido**, são fornecidas as saídas (ou probabilidades das saídas se o ambiente for estocástico) para todas as ações.
    * Se o **ambiente for desconhecido**, o agente terá de aprender como funciona, a fim de tomar boas decisões.

<br/>
<br/>

## Estrutura de Agentes
O **programa do agente** implementa a função do agente. Existe uma variedade de projetos básicos de programas de agentes, refletindo o tipo de informação explicitada e usada no processo de decisão. Os projetos variam em eficiência, síntese e flexibilidade. O projeto ssapropriado do programa do agente depende da natureza do ambiente.

### Agente reativo simples
É considerado o tipo de agente mais simples e se caracterizam por ter inteligência limitada. Esses agentes selecionam ações com base na percepção atual, ignorando o restante do histórico de percepções.
<p align="center">
    <img src = "https://user-images.githubusercontent.com/62517334/167700748-282c47bf-d0ab-4247-a8a1-bfcbaf5fe2ef.png">
</p>
<p align="center">
    <img src = "https://user-images.githubusercontent.com/62517334/167700988-c79e0a64-518b-49f3-bc50-da90d1984e8b.png">
</p>