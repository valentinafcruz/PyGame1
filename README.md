- Titulo do projeto: "Fat Cat Rush"
- Integrantes: Carolina Almeida, Laura Ferreira e Valentina Cruz
- Como rodar o jogo: A mecânica principal do jogo se baseia na movimentação do gato nos eixos X e Y por meio das teclas de setas do computador. O 
objetivo do jogador é pegar todos os peixes para passar para a próxima fase no menor tempo possível. O jogo tem em 3 fases, com níveis de dificuldade diferentes. A primeira possui um mapeamento mais simples, para que o jogador possa entender o jogo. Na segunda fase os cachorros aparecem, eles lançam ossos que matam o gatinho. Se o jogador colidir com os cachorros ou com os ossos, ele morre, aparece a tela de Gameover, e o jogador tem a opção de reinicar o  jogo, da fase1. Entretanto, o tempo cronômetro do jogo continua rodando. A terceira fase possui um número maior de cachorros além de um mapa mais complexo de movimentação. Ao passar da terceira fase, o jogador ganha o jogo e é indicado o tempo em que ele concluiu os mapas das três fases sem morrer.
A inicialização do jogo deve ser feita no arquivo "mecanicaprincipal.py"
- Vídeo demonstração no YouTube: https://youtube.com/shorts/ZkvDb3QM6qo?feature=shared 


Referências:
ChatGPT - foi utilizado para funções específicas no nosso jogo. Segue as indicações do uso de inteligência artificial no nosso projeto:
- A criação de todas as imagens do jogo foram geradas pelo ChatGPT e o histórico do chatGPT está exportado no link (https://chatgpt.com/share/68371d0a-b314-8005-8297-5a696b5d7b0a)
- a função 'evoluir' da classe do player foi 100% retirada do chatGPT, é ela que faz com que o gato fica mais gordinho a cada fase, que passa por três imagens diferentes ()
- a função 'check_collison' foi 100% retirada do chatGPT, ela checa se a próxima posição do gato vai colidir com uma das paredes na lista de paredes, para impedir que ele saia do mapa ou ande por cima das paredes ()
- a estrutura de cálculo e formatação do tempo cronômetro também foi 70% retirada do chatGPT, com algumas adaptações para o que seria mais relevante para nosso jogo (https://chatgpt.com/share/68379154-0968-8013-aeff-9eef621c4de6)
- a função 'paredes' foi 100% retirada do chatGPT, e é ela que foi utilizada para construir o mapa, um retângulo de cada vez 
