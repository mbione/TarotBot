import logging
import random
import telegram
import numpy as np

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

updater = Updater("1034516978:AAHTZOJ39mZP7b8HEvjBNvVOP3Y4YBP0tHU", use_context=True)
bot = telegram.Bot(token="1034516978:AAHTZOJ39mZP7b8HEvjBNvVOP3Y4YBP0tHU")
# Get the dispatcher to register handlers
dp = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


LoucoGerais = ''                
LoucoProfissional = ''              
LoucoRelacionemanto = ''  
LoucoEncoraja = ''                
LoucoAlerta = ''                    
LoucoDia = 'Você deve hoje estar aberto a tudo. Passe dia da forma mais descontraída possível, não leve nada muito a sério e encare até os "acontecimentos mais insólitos" com uma divertida curiosidade. Quanto menos você se prender a idéias às quais está habituado e às experiências já testadas e comprovadas, mais excitante e incomum será seu dia. Caso chegue à conclusão de ter hoje de recomeçar um determinado assunto do zero, então ouse um começo incomum, mais despreocupadamente possível. Permita-se, ao menos uma vez, um pouco de "loucura"!'

MagoGerais = ''           
MagoProfissional = ''              
MagoRelacionemanto = ''  
MagoEncoraja = ''          
MagoAlerta = ''           
MagoDia = ' "Quem, se não você? E quando, se não agora?" é lema do dia. Não hesite em tomar a iniciativa. Você possui uma autoconfiança salutar, sabe que quer e pode, com a concentração necessária, alcançar habilmente seu objetivo. Você conseguirá realizar as suas tarefas com maestria. Hoje é dia ideal para tomar iniciativas ou para colocar as suas habilidades à prova. Mostre do que você é capaz, mantenha-se ágil e seguro nas conversas e nos negócios, e assim conseguirá conquistar os outros para os seus propósitos facilmente.'

SacerdotisaGerais = ''  
SacerdotisaProfissional = ''
SacerdotisaRelacionemanto = ''
SacerdotisaEncoraja = ''
SacerdotisaAlerta = ''
SacerdotisaDia = 'Deixe que dia de hoje venha tranqüilamente ao seu encontro e observe, sem nenhuma intenção ou expectativa, que acontecerá. Deixe que os acontecimentos se desenrolem e só interfira neles quando a sua voz interior lhe disser que faça. Caso os seus afazeres permitam, observe hoje tranqüilamente que se passa em você, quando não está em atividade. O que passa por sua cabeça? Do que você sente necessidade subitamente? Não precisa para isso se obrigar a ficar parado; siga apenas os seus impulsos interiores. Você se surpreenderá com quão intenso e satisfatório será esse dia, aparentemente ocioso. Preste atenção aos seus sonhos em especial, pois eles podem lhe transmitir informações valiosas.'

ImperatrizGerais = ''  
ImperatrizProfissional = ''
ImperatrizRelacionemanto = ''
ImperatrizEncoraja = ''
ImperatrizAlerta = ''
ImperatrizDia = ' Alegre-se pelo dia de hoje. Ele promete ser extremamente excitante. Talvez você seja levado para ar livre, onde espírito e a alma possam se revigorar. Porém, também no seu cotidiano soprará um vento estimulante que trará idéias criativas e impulsos frutíferos. Algo que já vem crescendo há muito tempo dentro de você pode hoje vir à tona, e que estava até agora estagnado receberá um impulso forte de crescimento. O que você iniciar hoje tem boas perspectivas de desenvolver-se magnificamente, pois seu excelente senso de compreensão dos processos naturais de desenvolvimento conduzirá. instintivamente. a fazer o que é certo.'

ImperadorGerais = ''  
ImperadorProfissional = ''
ImperadorRelacionemanto = ''
ImperadorEncoraja = ''
ImperadorAlerta = ''
ImperadorDia = 'Hoje você deve executar as suas tarefas com coerência. Comece agora algo que tenha de ser realizado ou que você gostaria de já ter feito há muito tempo, independentemente do que seja.Você possui agora a energia suficiente, a habilidade e a coerência necessárias para colocar as coisas em ordem, esclarecer dúvidas e concluir tarefas inacabadas. Caso não lhe ocorra nenhuma idéia concreta sobre que você deve fazer. talvez seja apenas caso de arrumar a sua casa a fundo, consertar a sua bicicleta ou pagar contas antigas.'

HierofanteGerais = ''  
HierofanteProfissional = ''
HierofanteRelacionemanto = ''
HierofanteEncoraja = ''
HierofanteAlerta = ''
HierofanteDia = 'Vá ao encontro do dia com uma confiança salutar em Deus. Você tem todos os motivos para estar confiante e, além disso, boas possibilidades de realizar ou vivenciar algo realmente significativo. Não se prenda a rituais enrijecidos e não dê ouvidos a frases ocas e promessas vazias. Saia em busca do que é realmente fundamental, de valores ocultos e intrínsecos, e não se deixe impressionar por aparências. Caso você caia em um conflito de interesses, tome uma decisão de tal forma que daqui a alguns anos você possa lembrar desse dia com a consciência tranqüila.'

AmantesGerais = ''  
AmantesProfissional = ''
AmantesRelacionemanto = ''
AmantesEncoraja = ''
AmantesAlerta = ''
AmantesDia = ' Tome hoje uma decisão arrojada, que pode dizer respeito a uma pessoa, uma coisa ou uma intenção. Caso você esteja até agora hesitante e cheio de dúvidas, dê férias à razão, ouça a sua voz interior e apóie seu coração. Analise quais as diferenças e contradições interiores devem ser superadas e que deve ser feito para unir outra vez que porventura esteja desunido ou desfeito. Nem sempre, quando se tira essa carta, acontece de encontrar-se um grande amor no próximo ponto de ônibus, mas às vezes isso ocorre de fato.'

CarroGerais = ''  
CarroProfissional = ''
CarroRelacionemanto = ''
CarroEncoraja = ''
CarroAlerta = ''
CarroDia = 'Hoje, é chegada a hora de dar a largada. Você não precisa mais esperar. Concentre-se no seu objetivo e avalie mais uma vez se você reuniu tudo o que é necessário, para que ao longo do caminho não falte nada importante ou que você não perca de repente a energia. Porém, se você não estiver preparado de jeito nenhum para um salto ou nem sequer tiver pensado em uma partida, prepare-se então para ver para qual pista de decolagem esse dia irá levá-lo. Pois alguma coisa irá, com certeza, decolar hoje'

ForçaGerais = ''  
ForçaProfissional = ''
ForçaRelacionemanto = ''
ForçaEncoraja = ''
ForçaAlerta = ''
ForçaDia = 'Hoje será um dia agitado. Você se sentirá com vitalidade, repleto de energia e tão cheio de vontade de viver que não deverá se surpreender se for arrebatado por uma paixão. Isso não significa que você deva sair por aí tomando parte de alguma orgia, mas pode permitir-se uma maior dose de animação. Se você compartilhar esse prazer com outra pessoa ou empregá-lo em um processo criativo, poderá apreciar intensamente os seus aspectos fervilhantes e unificadores. Devido à sua energia e ao seu brilho intenso, você hoje superará obstáculos brincando e passará uma imagem atraente e convincente para as outras pessoas'

EremitaGerais = ''  
EremitaProfissional = ''
EremitaRelacionemanto = ''
EremitaEncoraja = ''
EremitaAlerta = ''
EremitaDia = 'Este dia lhe pertence. Dedique-se bastante tempo e não se deixe contagiar pela correria do dia-a-dia. Porém, se você tiver de se dedicar a algum assunto, faça-o com total atenção, sem se deixar pressionar ou influenciar pelos outros. Caso tenha de tomar uma decisão importante, deixe que o assunto amadureça até que você chegue a um posicionamento próprio e inequívoco. Meditar, dar um longo passeio a pé ou simplesmente contemplar um lago pode ajudá-lo a chegar a uma conclusão.'

RodaGerais = ''  
RodaProfissional = ''
RodaRelacionemanto = ''
RodaEncoraja = ''
RodaAlerta = ''
RodaDia = 'Existem dias nos quais temos de enfrentar situações e tarefas inevitáveis. Se você hoje tiver a impressão de que determinadas coisas simplesmente tomam um rumo próprio, não lute contra isso. Parta do princípio de que tudo tem a sua razão de ser, mesmo que o sentido esteja, no momento, oculto para você. Existem boas chances de tudo isso se revelar um caso de sorte no futuro'

JustiçaGerais = ''  
JustiçaProfissional = ''
JustiçaRelacionemanto = ''
JustiçaEncoraja = ''
JustiçaAlerta = ''
JustiçaDia = 'Hoje você deve manter a cabeça fresca. Caso haja um conflito ou uma decisão que precise ser tomada, mantenha uma atitude justa e considere as conseqüências dos seus atos a longo prazo. Você poderá hoje também se confrontar com as conseqüências de uma situação do passado. A depender da forma como você agiu naquela época, hoje poderá alegrar-se sobre um resultado ou encarar o dia com uma sensação de mal-estar.'

EnforcadoGerais = ''  
EnforcadoProfissional = ''
EnforcadoRelacionemanto = ''
EnforcadoEncoraja = ''
EnforcadoAlerta = ''
EnforcadoDia = 'Hoje a sua paciência vai ser colocada à prova. Talvez algo que já esteja emperrado há muito tempo continue a ser protelado ou algo com qual você não contava, empaque repentinamente. Não tente solucionar problema à força. Dessa forma, você iria somente atrapalhar ainda mais. Talvez seja suficiente apenas mudar a sua perspectiva para enxergar a situação sob um prisma completamente diferente. Se isso também não ajudar, você terá, quer queira ou não, de fazer algum sacrifício para que as coisas voltem a fluir.'

MorteGerais = ''  
MorteProfissional = ''
MorteRelacionemanto = ''
MorteEncoraja = ''
MorteAlerta = ''
MorteDia = 'Hoje algo chegará ao fim. Alguma coisa acabará ou perderá prazo de validade. Talvez você esteja contente que "isso" tenha finalmente acabado, porém talvez seja difícil desprender-se de algo que provavelmente tenha significado muito para você no passado. De qualquer forma, você pode acreditar que é chegada a hora de dizer adeus. Não tente preservar algo que já tenha acabado. Quando você realmente tiver se desprendido, irá se sentir finalmente livre e aliviado, mesmo que isso no momento pareça difícil de imaginar.'

TemperançaGerais = ''  
TemperançaProfissional = ''
TemperançaRelacionemanto = ''
TemperançaEncoraja = ''
TemperançaAlerta = ''
TemperançaDia = 'Você possui hoje a habilidade para realizar com sucesso uma mistura extraordinária, uma criação notável. Você poderá unir pessoas, descobrir uma forma hábil de solucionar um problema ou criar uma receita requintada. Esse também é dia perfeito para iniciar um vínculo profundo, contornar uma situação incômoda ou dissolver tensões'

DiaboGerais = ''  
DiaboProfissional = ''
DiaboRelacionemanto = ''
DiaboEncoraja = ''
DiaboAlerta = ''
DiaboDia = 'Sem querer fazer com isso uma previsão assustadora, pode ser que você hoje se confronte com seu lado sombrio. Talvez se deixe seduzir a dar um passo impensado ou caia na tentação de agir contra seus princípios. Também podem vir à tona sentimentos sobre os quais você não fazia a mínima idéia ou talvez acreditasse já ter superado há muito tempo, como inveja, ciúme, avidez ou sede de poder. Aborrecerse ou colocar a culpa nos outros ajudará tão pouco quanto tentar controlá-los. Aproveite a oportunidade para iluminar a escuridão, tomando consciência de facetas que não agradam e pesquisando as suas motivações secretas.'

TorreGerais = ''  
TorreProfissional = ''
TorreRelacionemanto = ''
TorreEncoraja = ''
TorreAlerta = ''
TorreDia = 'Hoje não será, certamente, um dia monótono. Conte com uma surpresa que poderá ser vivenciada como algo positivo, ou como um distúrbio intenso que destruirá expectativas concretas. Mesmo que você se chateie ou sofra hoje, quando algo não correr como você esperava — que é perfeitamente compreensível —, mantenha em mente que essa carta indica rompimento com um ambiente sufocante ou a libertação de uma idéia fixa. No futuro, ao olhar para trás, você não lamentará que hoje não deu certo'

EstrelaGerais = ''  
EstrelaProfissional = ''
EstrelaRelacionemanto = ''
EstrelaEncoraja = ''
EstrelaAlerta = ''
EstrelaDia = 'Alegre-se por este dia, pois ele será regido por uma boa estrela. Deixe-se inspirar por um sonho de futuro. O que for começado agora promete decorrer satisfatoriamente, mesmo a longo prazo, pois hoje você terá instinto necessário para enfrentar que virá pela frente. Caso não esteja planejando nada de novo, também valerá a pena restaurar algo antigo. Você se surpreenderá com que encontrará por baixo das camadas deixadas pelo tempo. As vezes, as lembranças também nos conduzem a novas visões.'

LuaGerais = ''  
LuaProfissional = ''
LuaRelacionemanto = ''
LuaEncoraja = ''
LuaAlerta = ''
LuaDia = 'Talvez você já tenha hoje acordado de um pesadelo, ou tenha, por outras razões, uma sensação estranha com relação a este dia. Porém, não se deixe irritar por nenhum fantasma. Ainda que você se sinta pressionado ante as exigências do dia ou ambiente à sua volta faça sentir-se inseguro, você não deve se desviar do seu caminho. Tome consciência de que uma experiência importante e enriquecedora espera por trás da barreira do medo, mas você só poderá chegar até ela se conseguir superar esse obstáculo. Por isso, vá ao encontro do dia mais acordado possível e siga seu caminho cautelosa e prudentemente, apesar de todo medo. Você irá espantar-se com que alcançará por meio disso.'

SolGerais = ''  
SolProfissional = ''
SolRelacionemanto = ''
SolEncoraja = ''
SolAlerta = ''
SolDia = 'Hoje é um dia ensolarado, que deve ser apreciado em toda a sua plenitude ou mesmo vivendo-o despreocupadamente ou comemorando algum triunfo pessoal. Você se sentirá hoje tão autoconfiante e fortalecido que será capaz até de ousar algo novo. Com a sua energia positiva e a sua atitude soberana, você será capaz de motivar e conquistar as pessoas à sua volta. Banhe-se na luz do seu sucesso e permita algo de bom a si mesmo e aos outros à sua volta.'

JulgamentoGerais = ''  
JulgamentoProfissional = ''
JulgamentoRelacionemanto = ''
JulgamentoEncoraja = ''
JulgamentoAlerta = ''
JulgamentoDia = ' Hoje você deve dar uma nova ênfase à sua vida. É indiferente se isso será feito no âmbito da aparência externa ou com relação a coisas fundamentais do seu cotidiano e do ambiente à sua volta. Deixe velhos hábitos para trás e permita que novos ventos soprem por sobre os campos empoeirados. Não se prenda a tradições ultrapassadas e não aposte mais nas coisas aparentemente já comprovadas; em vez disso, abra-se para novas evoluções e tendências atuais, às quais futuro pertence.'

MundoGerais = ''  
MundoProfissional = ''
MundoRelacionemanto = ''
MundoEncoraja = ''
MundoAlerta = ''
MundoDia = ' Hoje você se sentirá cheio de vida, em comunhão consigo e com mundo. Ou as coisas estão andando da forma como você desejou, ou você não se está deixando afetar por possíveis interferências. Desfrute esse dia deixando a sua alma balançar-se e saboreando inteiramente esse sentimento paradisíaco. Você poderá também aproveitar a oportunidade para dissolver hostilidades. Mostre-se reconciliador e promova a paz. Isso irá preenchê-lo com uma imensa alegria.'


AsPausGerais = 'Recomeço repleto de esperanças, iniciativa, força de vontade, determinação, idéia empolgante, impulso criativo, chance de desenvolvimento pessoal, inflamar-se por alguma coisa.'
AsPausProfissional = 'Desejo de realizar novos projetos, tornar-se autônomo, vontade de arriscar-se, crescer com um desafio.'
AsPausRelacionamento = 'Novo começo, revitalização, arder de amor, encontros tempestuosos, sexualidade apaixonada.'
AsPausEncoraja = 'Tomar iniciativa e seguir decididamente em frente. ALERTA SOBRE: Impetuosidade, impaciência e arrogância.'
AsPausAlerta = 'Impetuosidade, impaciência e arrogância.'
AsPausDia = 'Hoje você terá a energia necessária para começar algo novo ou dar um novo impulso a algo que já esteja em andamento. Você enfrentará os desafios deste dia com autoconfiança e entusiasmo. A sua energia contagiante não passará despercebida pelos outros a sua volta e poderá até proporcionar momentos emocionantes no âmbito dos relacionamentos pessoais. Prepare-se para surpresas, esteja aberto a impulsos e aproveite as chances que forem oferecidas'

DoisPausGerais = 'Combatividade, coragem, prazer em correr riscos, força de vontade, inflamar-se por alguma coisa, impor-se espontaneamente, avanço de uma forma forçada, falta de consideração'
DoisPausProfissional = 'Espírito competitivo e rivalidade, desafio profissional, disposição acentuada em assumir riscos, agir com engajamento.'
DoisPausRelacionamento = 'Desejos de conquista, atmosfera inflamada, jogo tenso entre forças dominadoras e submissas, atitudes machistas'
DoisPausEncoraja = 'Arriscar, impor ou conquistar alguma coisa'  
DoisPausAlerta = 'Valentia desconsiderada, ações destrutivas, demonstrações vazias de poder.'
DoisPausDia = 'Hoje ninguém será capaz de segurar seu impulso de seguir em frente. Você será capaz de remover radicalmente os obstáculos do seu caminho. Mas, se você esforçar-se exaustivamente para alcançar os seus objetivos, poderá estar no final totalmente exaurido e de mãos vazias. Não tente fazer a sua vontade prevalecer a qualquer custo. Em vez disso, direcione a sua energia que emana do Elemento Fogo para objetivos que valham a pena ou procure uma outra válvula de escape para a força que está sobrando dentro de você. Gaste sua energia, por exemplo, praticando esportes exaustivos ou participando de competições esportivas.'

TresPausGerais = 'Base saudável, confiança, sucesso, espírito empreendedor, vitalidade.'
TresPausProfissional = 'Contatos benéficos, vínculos comerciais promissores, perspectivas favoráveis, avanço propício, apoio.'
TresPausRelacionamento = 'Vontade de curtir a vida, atar laços de ternura, vínculo promissor, convivência excitante, harmonia.'
TresPausEncoraja = 'Olhar confiante para futuro e seguir novas metas.'
TresPausAlerta = 'Ultrapassar impetuosamente os limites'
TresPausDia = 'Desfrute da atmosfera primaveril deste dia, não importa em qual estação do ano você esteja. Sacuda os pensamentos tristes para longe e presenteiese com um ramalhete de flores. Caso você ainda não esteja comprometido, sentir-se-á agora intensamente preparado para um novo amor. Hoje talvez surja uma oportunidade para uma paquera. Porém, mesmo sozinho, você vivenciará este dia como sendo extremamente benéfico.'

QuatroPausGerais = ' Ordem e harmonia, dinâmica equilibrada, autoconfiança, equilíbrio'
QuatroPausProfissional = 'Distribuição de lucros, ser pago por um trabalho realizado, resultados visíveis, espírito de grupo dinâmico, eficiência.'
QuatroPausRelacionamento = 'Ser complementado pelo parceiro, convivência harmoniosa, solução de conflitos, encontros enriquecedores, realização sexual, dinâmica saudável na relação.'
QuatroPausEncoraja = 'Encontrar a medida certa entre condescendência e intransigência. '
QuatroPausAlerta = 'Abdicar até de discussões sadias em prol do estabelecimento de uma harmonia.'
QuatroPausDia = 'Tudo que você começar hoje terá boas chances de ser concluído favoravelmente. Você conseguirá até apaziguar diferenças aparentemente intransponíveis e isso preencherá com uma profunda satisfação. Você estará disposto a fazer acordos, sem que precise, para isso, perder de vista os seus interesses. Se por acaso você estiver há algum tempo evitando fazer algo um tanto desagradável, como, por exemplo, dar um telefonema difícil, hoje poderá realizar essa tarefa com sucesso.'

CincoPausGerais = 'Medir forças, ambição, impetuosidade, desafio, ultrapassar limites.'
CincoPausProfissional = 'Concorrência, interesses comerciais diversos, disputar ou defender cargos com persistência, engajamento ambicioso, conquistar "terras novas".'
CincoPausRelacionamento = 'Chegar a um consenso apesar das diferenças, entrar em atrito, conciliar incompatibilidades'
CincoPausEncoraja = ' Ousar algo novo e entrar em uma competição'
CincoPausAlerta = ' Possuir uma ambição desenfreada e tentar impressionar os outros com arrogância'
CincoPausDia = ' Este dia promete ser bem agitado. Alguém poderá cruzar seu caminho, acarretando um choque de interesses. Não fuja do conflito, agarre touro pelos chifres e demonstre claramente que você está no páreo. Se agir com justiça, e além disso com empenho total, você terá boa chance de encontrar uma solução satisfatória. Mesmo que hoje você tenha de lidar com burocratas, não hesite em mostrar seu lado combativo.'

SeisPausGerais = 'Recompensa por serviços prestados, boas notícias, otimismo, vitória.'
SeisPausProfissional = 'Reconhecimento, sucesso encorajador, conclusão bem-sucedida, bons negócios, impulso na carreira, aumento de salário, condecoração.'
SeisPausRelacionamento = 'Superação de dificuldades, desabrochar de um relacionamento caloroso, perspectivas agradáveis'
SeisPausEncoraja = 'Ter confiança de que tudo dará certo.'
SeisPausAlerta = 'Vangloriar-se do seu próprio sucesso com ar de menosprezo pelos outros.'
SeisPausDia = 'Você tem motivos suficientes para alegrar-se, pois hoje é seu dia de sorte! Uma boa notícia está no ar. Principalmente se você passou agora por uma fase cansativa, perceberá como tudo tomará um impulso e se desenvolverá rapidamente. Reconhecimento e uma recompensa adequada Aguardarão agora em todos os lugares em que tenha prestado bons serviços. Desfrute do seu triunfo, demonstre a sua felicidade e comemore adequadamente com os seus amigos.'

SetePausGerais = 'Arriscar-se a seguir sozinho seu próprio caminho, superar-se, lutar contra as adversidades, assumir um risco.'
SetePausProfissional = 'Cargo ameaçado, engajamento intenso, realizar um propósito com determinação e até sozinho, se for necessário'
SetePausRelacionamento = 'Salvar relacionamento de um fracasso por meio de uma manobra ousada ou afastar uma ameaça; dar um novo impulso com decisão a um relacionamento desgastado'
SetePausEncoraja = 'Salvar com bravura uma causa aparentemente perdida.'
SetePausAlerta = 'Superestimar a si mesmo e gastar energia desnecessariamente.'
SetePausDia = 'Uma vitória, que você já contava como certa, poderá hoje estar ameaçada, ou um assunto que seja importante para você poderá subitamente perder significado. Conte com uma possível interferência de pessoas em seus assuntos, com propósito de ameaçar a sua posição. Não fique parado passivamente vendo as suas esperanças se perderem; lute com determinação pela sua causa. Ouse e, se necessário, siga sozinho seu próprio caminho.'

OitoPausGerais = 'Lampejo súbito, solução repentina de um problema, inspirações, "estar ligado à tomada"'
OitoPausProfissional = 'Inovação, idéias empolgantes, desenvolvimentos favoráveis, novos vínculos comerciais, negócios com exterior, aperfeiçoamento, ações rápidas.'
OitoPausRelacionamento = 'Amor à primeira vista, solução repentina de conflitos, impulsos estimulantes, erotismo ardente'
OitoPausEncoraja = 'Abrir-se para novas percepções e agir imediatamente.'
OitoPausAlerta = 'Conclusões apressadas, dar muita ênfase ao intelecto, extravagâncias intelectuais.'
OitoPausDia = 'Uma boa notícia ou um telefonema inesperado poderão, hoje, enchê-lo de energia e mudar surpreendentemente rumo do seu dia. Sua mente estará fervilhando e, entre as muitas idéias que lhe passarão hoje pela cabeça, encontrarse-á a solução de um velho problema. Essa energia poderá, até mesmo, estender-se à sua vida amorosa e explodir como "fogos de artifício". Isso seria, com certeza, a maneira mais prazerosa de canalizar tanto vigor.'

NovePausGerais = 'Dispor de muitas possibilidades, estar cheio de energia, alegrar-se por algo que está por vir, inspiração.'
NovePausProfissional = 'Adentrar solos novos e repletos de perspectivas, ter confiança nas próprias capacidades, começar um projeto com coragem e entusiasmo'
NovePausRelacionamento = 'Estabilidade e unissonância, impulsos estimulantes vindos da alma, novo vínculo forte, intercâmbio intenso, entusiasmo.'
NovePausEncoraja = 'Agir audaciosamente confiando na sua própria intuição'
NovePausAlerta = 'Deixar-se levar por pensamentos megalômanos'
NovePausDia = 'Hoje você deve arriscar-se! Deve ousar experimentar algo para qual lhe tenha faltado coragem até agora. Você poderá confiar completamente na sua intuição, que conduzirá a fazer instintivamente a coisa certa. Poderá também aproveitar a energia inspiradora do dia de hoje para fazer planos agradáveis para futuro, como, por exemplo, programar as suas próximas férias.'

DezPausGerais = 'Realização, Responsabilidade, Carga muito pesada.'
DezPausProfissional = ' Forte pressão por causa do excesso de trabalho, estresse, tormento, tentativa inútil de reconhecimento, medo do futuro profissional, dificuldades de liderança'
DezPausRelacionamento = 'Endurecimento, lutas pelo poder, lutar contra tabus e proibições, sentimentos bloqueados, desesperança'
DezPausEncoraja = 'Reconhecer as suas próprias limitações e agir com responsabilidade.'
DezPausAlerta = 'Demonstrações de poder, intolerância e agressividade reprimida.'
DezPausDia = 'Arme-se hoje com uma boa dose de disciplina e capacidade de resistência. Você poderá precisar delas. Talvez seja agredido por causa das suas opiniões ou alguém tente dominá-lo. Você poderá também entrar em conflito com autoridades, seja com seu chefe ou com a polícia de trânsito. Não se deixe provocar, de forma nenhuma, mantenha-se tranqüilo e sereno, mesmo que isso não seja fácil. Você reconhecerá mais tarde quão inteligente terá sido tomar essa atitude'

PagePausGerais = 'Dinâmica, impulsiva e cheia de vida, amazona, impulso inicial, novo começo impetuoso, entusiasmo, espírito de aventura, impaciência.'
PagePausProfissional = 'Idéias inovadoras que necessitam ser expressas, início de uma carreira profissional.'
PagePausRelacionamento = 'Vontade de curtir a vida, paixão tempestuosa, desejo sexual, paquera excitante, fogo de palha, "pular a cerca"'
PagePausEncoraja = 'Viver de uma forma espontânea e cheia de ânimo.'
PagePausAlerta = 'Comportamento teatral e humores variáveis e impulsivos.'
PagePausDia = 'Hoje você quer tudo ou nada. Você não se dará por satisfeito com meios-termos. Você estará tão radiante de energia que mal poderá esperar para contagiar os outros com seu entusiasmo. No amor, isso poderá conduzi-lo a um encontro apaixonante. De qualquer jeito, você estará disposto a deixar-se levar por uma aventura, sem se preocupar com as conseqüências. De fato, hoje não terá nada que impeça de deixar a razão de lado e, pelo menos uma vez, agir de acordo com os princípios do prazer.'

CavaleiroPausGerais = 'Conquistador, herói, corredor, a pessoa colérica, novo impulso, iniciativa, entusiasmo.'
CavaleiroPausProfissional = 'Estar à disposição para trabalhar, vontade de se arriscar, coragem para tornar-se autônomo, espírito pioneiro, começar algo novo com todo entusiasmo.'
CavaleiroPausRelacionamento = 'Paixões selvagens, erotismo exigente, aventura arriscada, satisfação do desejo de uma forma espontânea, porém também infantil. Humores imprevisíveis.'
CavaleiroPausEncoraja = 'Encarar a vida de uma maneira aberta e cheia de autoconfiança.'
CavaleiroPausAlerta = 'Satisfação espontânea de desejos à custa de objetivos a longo prazo.'
CavaleiroPausDia = 'Para ter uma experiência realmente intensa, você hoje aceitará até correr riscos. De preferência, você gostaria de mostrar para todos quem realmente traz dentro de si. Porém, se afrouxar as rédeas na hora errada, poderá, com seu jeito enérgico, passar por cima de alguém e até aborrecer-se com os seus vizinhos ou colegas de trabalho. Por isso, procure palco adequado para a sua encenação. Quebre algum recorde ou saia e divirta-se'

RainhaPausGerais = 'Autoconfiança sadia, espírito empreendedor, franqueza, impulsividade, independência, auto-realização, mulher enérgica, carismática. generosa e madura.'
RainhaPausProfissional = 'Realizar-se profissionalmente com consciência de suas capacidades, ter competência para assumir grandes tarefas, promoção, tornar-se autônomo, assumir posições de liderança'
RainhaPausRelacionamento = 'Relação madura de igual para igual, leve submissão, tantra do amor, calor humano.'
RainhaPausEncoraja = ' Expressar suas necessidades pessoais e responder por si mesmo.'
RainhaPausAlerta = ' Egocentrismo e imposição de suas vontades a qualquer preço.'
RainhaPausDia = 'Hoje é você quem manda! Você está sentindo-se forte, sabe exatamente que quer e está preparado para realizar tarefas complicadas, mesmo que as tenha de fazer sozinho. Graças a essa determinação, você poderá ter êxito ao dar passos decisivos. Você causará uma impressão bem convincente nas pessoas à sua volta por causa de sua atitude soberana, e elas se deixarão empolgar, motivar e conduzir por você com prazer. É também possível que uma mulher enérgica e com força de vontade represente hoje um papel importante no seu dia.'

ReiPausGerais = 'Confiança em si mesmo, coragem, lutar por um ideal, forte espírito de iniciativa, homem maduro com força de vontade e dinamismo, personalidade que serve de exemplo para os outros, espírito de liderança.'
ReiPausProfissional = 'Qualidades de liderança, motivação para novos projetos, realizar trabalhos pioneiros, soberania, trabalhar com autoconfiança e independência.'
ReiPausRelacionamento = 'Convivência agitada de igual para igual entre dois parceiros, generosidade e vontade de tomar parte em discussões construtivas. vínculo dinâmico'
ReiPausEncoraja = 'Agir com determinação. objetividade e coragem.'
ReiPausAlerta = 'Vaidade, intolerância e egoísmo.'
ReiPausDia = 'Hoje é um dia em que você poderá conquistar mundo! Você estará faiscando de energia e mal poderá esperar para contagiar as pessoas à sua volta com seu entusiasmo. Você saberá exatamente que quer, apostará em grandes metas e terá agora boa oportunidade de alcançá-las. Você conseguirá realizar com facilidade que para os outros parece difícil. Com tanto entusiasmo e tanta confiança, você deverá ter cuidado para não atropelar as outras pessoas sem nenhuma consideração. Também pode ser que hoje um homem interessante e temperamental venha ao seu encontro'

AsCopas = ''
AsCopas = ''
AsCopas = ''
AsCopas = ''
AsCopas = ''
AsCopasDia = 'Hoje você vai receber uma boa ajuda. Aproveite momento favorável para ousar fazer algo que prometa satisfação. As chances são boas, principalmente no que diz respeito aos assuntos do coração. Se você aproximar-se das outras pessoas despreocupadamente, poderá cair, de fato, diretamente nos braços de uma sorte grande. Você poderá também encontrar a paz interior, solucionando um problema antigo ou, finalmente, fazendo as pazes com alguém.'

DoisCopas = ''
DoisCopas = ''
DoisCopas = ''
DoisCopas = ''
DoisCopas = ''
DoisCopasDia = ' Hoje, trunfo é coração! Este dia será dominado por uma profunda simpatia, um grande amor ou uma reconciliação. Deixe as "antenas" da sua alma "ligadas", pois hoje você poderá apaixonar-se outra vez. Caso você já esteja comprometido, irá pairar no ar uma sensação de retomo da primavera. Não fique apenas parado esperando que a sorte grande venha bater à sua porta, faça também a sua parte para que a deusa Fortuna possa presenteá-lo e as setas do cupido não sejam atiradas no vazio'

TresCopas = ''
TresCopas = ''
TresCopas = ''
TresCopas = ''
TresCopas = ''
TresCopasDia = 'Alegre-se com dia de hoje, pois ele presenteará com abundância. Desfrute lado bom da vida, faça uso de suas diversas possibilidades e mostre-se grato pelos prazeres que a vida lhe oferece neste momento. O melhor de tudo é poder compartilhar a sua alegria com outras pessoas. Convide seus melhores amigos, desfrute de bons momentos ao lado da sua família ou encha de mimos alguém que você ama. Afinal de contas, não é todo dia que temos tantas razões para comemorar.'

QuatroCopas = ''
QuatroCopas = ''
QuatroCopas = ''
QuatroCopas = ''
QuatroCopas = ''
QuatroCopasDia = 'Gaste bastante tempo saboreando dia de hoje. Você atingiu um ápice temporário e merece tirar uma folga. Desfrute deste dia e não esquente a cabeça com problemas que possam ser resolvidos amanhã, caso eles não se solucionem por si mesmos. Em vez disso, alegre-se pela simpatia e dedicação que lhe serão direcionadas hoje. Já que a vida lhe está oferecendo tantas coisas boas, você poderá também demonstrar seu lado generoso com as outras pessoas.'

CincoCopas = ''
CincoCopas = ''
CincoCopas = ''
CincoCopas = ''
CincoCopas = ''
CincoCopasDia = 'Hoje você terá de contar com uma freada. Alguma coisa pela qual você já se havia alegrado, ou que já contava como certa, não acontecerá como você esperava. Caso seja apenas uma coisa insignificante, enfrente a situação com bom humor. Porém, tratando-se da dissolução de algo realmente importante, você deverá suportar fato com calma, sem esconder a sua decepção. Quanto mais consciente e sincero você encarar as suas esperanças fracassadas, mais rápido sentirá outra vez chão embaixo dos seus pés'

SeisCopas = ''
SeisCopas = ''
SeisCopas = ''
SeisCopas = ''
SeisCopas = ''
SeisCopasDia = 'Hoje você terá motivos suficientes para sair pulando de alegria. Se você vai sair por aí literalmente pulando ou se vai fazê-lo dentro de si, tanto faz, contanto que você não se contenha. Demonstre que você está bem em todos os sentidos. Ainda mais se estiver se sentindo como se tivesse renascido, depois de ter passado por uma fase ruim; saboreie intensamente a doçura da vida. Faça uma festa ou celebre a si mesmo e satisfaça aquele desejo que você já vem guardando há muito tempo.'

SeteCopas = ''
SeteCopas = ''
SeteCopas = ''
SeteCopas = ''
SeteCopas = ''
SeteCopasDia = 'Hoje não se deixe seduzir, por mais atraente que a oferta lhe pareça. Você pode acabar caindo em um atoleiro de esperanças falsas, do qual só sairá com muita dificuldade. Evite situações obscuras, tudo que for mórbido ou não for transparente, e recuse, de preferência, algo que lhe possa parecer muito atraente à primeira vista, mas que só irá trazer vantagens a curto prazo. Fique de olhos bem abertos e tome bastante cuidado com álcool e outras drogas.'

OitoCopas = ''
OitoCopas = ''
OitoCopas = ''
OitoCopas = ''
OitoCopas = ''
OitoCopasDia = 'Hoje você poderá atolar-se na lama. Mesmo que a culpa não seja toda sua, você colaborou em parte para que isso acontecesse. Já que a situação está muito confusa, você deve tentar sair mais rápido possível desse lamaçal. É também muito importante que você se conscientize das razões que levaram a essa paralisação. Só assim você poderá evitar que esse mesmo erro seja cometido outra vez no futuro.'

NoveCopas = ''
NoveCopas = ''
NoveCopas = ''
NoveCopas = ''
NoveCopas = ''
NoveCopasDia = 'Hoje você rirá à vontade, pois a sorte estará ao seu lado! Tudo correrá maravilhosamente bem e se desenvolverá como você queria. Aproveite. Você poderá aumentar a sua alegria ainda mais, se compartilhá-la com os outros à sua volta. Dê um passeio com a família ou convide amigos para irem à sua casa. É claro que você também poderá aproveitar vento a seu favor para resolver facilmente algumas coisas que já queria ter feito há muito tempo.'

DezCopas = ''
DezCopas = ''
DezCopas = ''
DezCopas = ''
DezCopas = ''
DezCopasDia = 'Celebre todas as festas que aparecerem. Hoje você terá boas razões para isso. Ou porque você conseguiu concluir algo com sucesso, por estar feliz e agradecido por um resultado positivo, ou simplesmente por estar sob todos os aspectos satisfeito consigo mesmo e com a vida. Faça algo de bom para si mesmo, encontre-se com amigos e saboreie essa despreocupação, enquanto ela durar.'

PageCopas = ''
PageCopas = ''
PageCopas = ''
PageCopas = ''
PageCopas = ''
PageCopasDia = 'Não se admire se você hoje for inundado por um anseio profundo ou por sentimentos temos de amor. Agora, mais do que nunca, você estará aberto para um encontro romântico e, ao mesmo tempo, também suscetível a todo tipo de tentações. Você deverá deixar-se envolver, pois tudo indica que terá uma experiência encantadora, que despertará emoções dentro de você até então desconhecidas.'

CavaleiroCopas = ''
CavaleiroCopas = ''
CavaleiroCopas = ''
CavaleiroCopas = ''
CavaleiroCopas = ''
CavaleiroCopasDia = ' O dia de hoje dará asas à sua alma. Não somente a cabeça e coração estarão harmonizando-se agradavelmente um com outro, como você também vivenciará um impulso emocional, que elevará para sétimo céu. Aproveite a oportunidade para colocar em ordem coisas que necessitem tanto de imaginação quanto de razão. Sobretudo se alguma coisa estiver emperrada no âmbito dos relacionamentos. liberte-a hoje.'

RainhaCopas = ''
RainhaCopas = ''
RainhaCopas = ''
RainhaCopas = ''
RainhaCopas = ''
RainhaCopasDia = 'Sua abertura emocional deixará hoje bastante receptivo às necessidades do ambiente ao seu redor e, ao mesmo tempo, vulnerável a uma possível rigidez. Mesmo assim, você deverá aproximar-se dos outros com total confiança, pois a sua forte intuição protegerá de dificuldades. Dê uma atenção especial aos seus sonhos! Você poderá conhecer uma mulher simpática, com capacidades mediúnicas, que aproximará do lado misterioso e enigmático da vida.'

ReiCopas = ''
ReiCopas = ''
ReiCopas = ''
ReiCopas = ''
ReiCopas = ''
ReiCopasDia = ' Hoje você deve utilizar toda a sua energia para atingir um objetivo que já se encontra a seu alcance. Empenhe-se mais uma vez com todo seu engajamento para alcançá-lo. Agora, mais do que nunca, você perceberá quão fortemente é apoiado por seus sentimentos e inspirado por sua imaginação fértil. Também pode acontecer de hoje um homem compreensivo e simpático cruzar seu caminho ou desempenhar um papel importante no seu dia. Você perceberá a sua presença como algo enriquecedor e que lhe fará bem.'

AsEspadas = ''
AsEspadas = ''
AsEspadas = ''
AsEspadas = ''
AsEspadas = ''
AsEspadasDia = 'Uma idéia vibrante irá ajudá-lo hoje a solucionar um problema incômodo ou a compreender algo que tem sido para você um enigma já há algum tempo. Fique de olhos abertos e deixe suas "antenas ligadas". Dessa forma, você terá uma visão ampla da situação e ao mesmo tempo a oportunidade de tomar uma decisão inteligente ou de elucidar algo que já deveria ter sido esclarecido há muito tempo.'

DoisEspadas = ''
DoisEspadas = ''
DoisEspadas = ''
DoisEspadas = ''
DoisEspadas = ''
DoisEspadasDia = 'Hoje você deve descansar as armas. Uma possível solução para um conflito inflamado surgirá inesperadamente. Não hesite em dar primeiro passo, mostre-se disposto a negociar e faça uma proposta justa para adversário. Para que isso não se torne apenas uma paz aparente, terá de ser encontrado um denominador comum, no qual ninguém seja prejudicado. Quando vocês estiverem juntos, mais tarde, fumando cachimbo da paz, você se sentirá bem mais relaxado e satisfeito.'

TresEspadas = ''
TresEspadas = ''
TresEspadas = ''
TresEspadas = ''
TresEspadas = ''
TresEspadasDia = 'Hoje, quer você queira ou não, terá de se confrontar com uma situação desagradável. O seu dia pode ser abalado por um golpe entristecedor, uma notícia decepcionante ou uma decisão dolorosa. Quanto mais controlado e sereno você encarar essa situação, mais rápido ela se resolverá. Portanto, faça que deve ser feito. Dê aquele telefonema desagradável e não adie mais uma vez a sua consulta ao dentista.'

QuatroEspadas = ''
QuatroEspadas = ''
QuatroEspadas = ''
QuatroEspadas = ''
QuatroEspadas = ''
QuatroEspadasDia = 'Não confie no sossego. Uma calmaria não é nenhuma garantia de que a tempestade não recomeçará a qualquer momento. O seu problema só está resolvido aparentemente, e não se resolverá por si só, futuramente. Mesmo que as suas manobras de dispersão tenham vindo na hora certa, para você não ter de se confrontar com esse assunto desagradável, mais importante agora é aproveitar essa oportunidade para encontrar uma verdadeira solução para problema.'

CincoEspadas = ''
CincoEspadas = ''
CincoEspadas = ''
CincoEspadas = ''
CincoEspadas = ''
CincoEspadasDia = 'Hoje você deve se prevenir. Talvez tenha de se defender contra uma infâmia, uma calúnia maldosa ou uma chicana. Enfrente tudo da melhor maneira possível e mantenha em mente que, mesmo depois de uma "sexta-feira negra", segue um fim de semana no qual você pode se recuperar. Se você conseguir reconhecer a sua participação para que as coisas tenham chegado a esse ponto, talvez consiga evitar passar por uma situação desagradável como essa no futuro.'

SeisEspadas = ''
SeisEspadas = ''
SeisEspadas = ''
SeisEspadas = ''
SeisEspadas = ''
SeisEspadasDia = 'Hoje, procure informar-se. Amplie os seus horizontes intelectuais deixando-se estimular ou indo especificamente atrás de uma informação pela qual você se vem interessando há muito tempo. Navegue na internet, remexa uma livraria, procure por ofertas interessantes em um jornal ou analise programa de cursos oferecidos por alguma instituição na sua cidade. Talvez você possa até programar uma excursão cultural ao teatro, a uma exposição ou a uma palestra interessante'

SeteEspadas = ''
SeteEspadas = ''
SeteEspadas = ''
SeteEspadas = ''
SeteEspadas = ''
SeteEspadasDia = 'Hoje você deve tomar cuidado. As suas boas intenções serão colocadas à prova. Se você subestimar as suas barreiras e fraquezas interiores, pode contar que, em um prazo muito curto de tempo, não conseguirá ir muito mais adiante. Além disso, você estará hoje tendendo a enganar a si mesmo, em vez de encarar a realidade de frente. Por isso, mantenha os olhos abertos ao tratar de contratos ou outros acordos e leia com particular atenção que está escrito em letras miúdas, para não ser ludibriado.'

OitoEspadas = ''
OitoEspadas = ''
OitoEspadas = ''
OitoEspadas = ''
OitoEspadas = ''
OitoEspadasDia = 'Tome cuidado, hoje, para não perder fio da meada. Mantenha-se perseverante, paciente e assuma as suas decisões. Não se deixe desanimar, mesmo que alguém interrompa constantemente quando estiver falando, mesmo que você fique preso em um engarrafamento ou que barreiras apareçam à sua frente, vindas de lugares inesperados. Esses empecilhos podem desviá-lo um pouco da sua rota, mas, se você não perder a sua meta de vista, irá por fim alcançá-la.'

NoveEspadas = ''
NoveEspadas = ''
NoveEspadas = ''
NoveEspadas = ''
NoveEspadas = ''
NoveEspadasDia = 'Caso você hoje esteja torturando-se ou atormentando-se com dúvidas sobre si mesmo ou imaginando cenários horríveis, faça tudo que puder para despertar mais rápido possível desse pesadelo. Se você estiver realmente sendo ameaçado por forças externas, existem duas possibilidades de reação: se não tiver para onde correr, faça das tripas coração e enfrente a situação de uma vez por todas; porém, se houver realmente uma saída alternativa, decida-se por ela'

DezEspadas = ''
DezEspadas = ''
DezEspadas = ''
DezEspadas = ''
DezEspadas = ''
DezEspadasDia = 'Coloque um ponto final. Talvez você seja hoje obrigado a interromper ou desistir inesperadamente de algo que lhe seja muito importante. Pode acontecer também de se sentir aliviado pelo término de algo que há muito tempo vinha sendo um peso para você, deprimindo-o e atormentando. Em todo caso, você deve tomar cuidado para não se deixar levar por uma fúria destrutiva ou jogar algo para alto, atitudes das quais possa se arrepender no futuro.'

PageEspadas = ''
PageEspadas = ''
PageEspadas = ''
PageEspadas = ''
PageEspadas = ''
PageEspadasDia = 'Hoje você não está para brincadeiras. Você está agressivo e sente-se pessoalmente atacado mais rapidamente do que de costume. Obviamente, isso poderá causar problemas. Se você não se importar com isso, deixe que seu mau humor corra solto. Por outro lado, poderá aproveitar a oportunidade para fazer uma autocrítica. Talvez as criticas que estejam sendo feitas a você não sejam assim tão despropositadas e sem fundamento. Se você estiver disposto a ouvir atentamente, isso poderá ajudá-lo bastante.'

CavaleiroEspadas = ''
CavaleiroEspadas = ''
CavaleiroEspadas = ''
CavaleiroEspadas = ''
CavaleiroEspadas = ''
CavaleiroEspadasDia = 'Hoje você estará se sentindo indeciso. Você se aborrecerá por estar disperso, por não conseguir coordenar suas muitas idéias ou por ser rejeitado pelos outros. Talvez você se confronte hoje com uma pessoa eloqüente e bem esperta. Não deixe que ela confunda com sua astúcia e não se transtorne com seu cinismo ou pela confusão que ela provoca. 0 melhor a fazer é comprar essa briga.'

RainhaEspadas = ''
RainhaEspadas = ''
RainhaEspadas = ''
RainhaEspadas = ''
RainhaEspadas = ''
RainhaEspadasDia = 'Hoje poderá lhe ocorrer um lampejo de fato genial. Se você conseguir identificar que vem constrangendo ou bloqueando ultimamente, terá boa chance de conseguir libertar-se, de uma vez por todas, por meio de uma decisão clara. Preste atenção para que, nos seus esforços em agir com independência, você não seja muito radical, senão acabará afastando-se muito do seu objetivo. Hoje também pode acontecer de uma mulher inteligente desempenhar um papel importante no seu dia. Mantenha os seus ouvidos atentos para escutar que ela tem a lhe dizer.'

ReiEspadas = ''
ReiEspadas = ''
ReiEspadas = ''
ReiEspadas = ''
ReiEspadas = ''
ReiEspadasDia = 'Hoje você irá diretamente ao seu objetivo. Você poderá entusiasmar as outras pessoas com os seus planos, já que possui os conceitos mais convincentes e os melhores argumentos, além de apresentá-los com charme e espirituosidade. Aproveite essa clareza mental, sobretudo para tomar decisões que já deveriam ter sido tomadas. Caso você esteja com um problema que não consegue resolver há muito tempo, procure hoje a ajuda profissional de um especialista.'

AsMoedas = ''
AsMoedas = ''
AsMoedas = ''
AsMoedas = ''
AsMoedas = ''
AsMoedasDia = 'Tente hoje forjar a sua própria sorte. Procure uma pechincha, seja indo às compras, em uma agência de viagens ou no boletim de cotação da bolsa de valores. Reconheça a oportunidade que se apresenta principalmente para todas as intenções e investimentos que não tenham como objetivo vantagens a curto prazo. Coloque hoje a pedra fundamental para um projeto no qual as perspectivas a longo prazo lhe sejam muito importantes.'

DoisMoedas = ''
DoisMoedas = ''
DoisMoedas = ''
DoisMoedas = ''
DoisMoedas = ''
DoisMoedasDia = 'Hoje você poderá se confrontar com um conflito de interesses, no qual tenha de jogar com aparentes contradições. Permaneça flexível e deixe as opções abertas. Qualquer atitude parcial irá agora conduzi-lo forçosamente a um beco sem saída, no qual você será, por causa de circunstâncias externas, obrigado a modificar as suas idéias. Se, por outro lado, você dispuser de possibilidades variadas, será possível agregar posições, que até momento eram opostas, para formar uma totalidade.'

TresMoedas = ''
TresMoedas = ''
TresMoedas = ''
TresMoedas = ''
TresMoedas = ''
TresMoedasDia = 'Hoje você deve arregaçar as mangas. Está na hora de realizar com determinação aquela tarefa que você vem adiando com desânimo até momento. Isso poderá significar construir um novo futuro: organizar seu jardim, fazer um saneamento nas bases da sua relação ou estruturar as suas finanças, tanto faz. Remova da sua frente as coisas que estão bloqueando seu caminho e leve seu plano adiante passo a passo, até que você esteja satisfeito com resultado.'

QuatroMoedas = ''
QuatroMoedas = ''
QuatroMoedas = ''
QuatroMoedas = ''
QuatroMoedas = ''
QuatroMoedasDia = 'Hoje você conseguirá resolver algo que já aborrece há muito tempo. Você conseguirá afastar que tem incomodado ou esclarecer e estruturar uma situação confusa. Não hesite em demarcar seu terreno nitidamente e proteger-se de ataques invejosos ou hostis. Assuma responsabilidades e concentre-se completamente nas coisas que estão ao seu encargo. Aproveite dia, se for possível, para colocar algo importante a salvo.'

CincoMoedas = ''
CincoMoedas = ''
CincoMoedas = ''
CincoMoedas = ''
CincoMoedas = ''
CincoMoedasDia = 'Hoje a maré estará baixa para você financeiramente, ou por algum motivo você será obrigado a restringir os seus gastos. De qualquer forma, não será um dia em que as coisas correrão facilmente. Se você estiver envolvido em uma situação problemática, não se torture mais desnecessariamente. Verifique se seu esforço ainda vale a pena. Ainda que a constatação seja dolorosa, talvez tenha chegado a hora de seguir outro caminho mais promissor e que poupe de mais frustrações.'

SeisMoedas = ''
SeisMoedas = ''
SeisMoedas = ''
SeisMoedas = ''
SeisMoedas = ''
SeisMoedasDia = 'Este dia será um sucesso. Se for preciso, reúna forças para tomar um novo impulso. Você realizará com facilidade tudo aquilo que até agora estava confuso ou vinha dando errado, seja isso um trabalho incômodo, a complicada coordenação dos seus compromissos ou seu programa de exercícios físicos. Mesmo que se trate de uma melhoria das suas condições financeiras, de qualquer forma, não deixe que este dia passe sem que aproveite'

SeteMoedas = ''
SeteMoedas = ''
SeteMoedas = ''
SeteMoedas = ''
SeteMoedas = ''
SeteMoedasDia = 'Tome cuidado, pois algo pode dar errado. É melhor deixar para fazer amanhã as coisas que são de fato importantes para você. Talvez você tenha de presenciar perecimento ou definhamento de algo. Não tente manter isso vivo artificialmente. O seu tempo já chegou ao fim. Quanto mais rápido você se der conta disso, mais cedo terá a chance de superar decepção e a crise que acompanham essa situação.'

OitoMoedas = ''
OitoMoedas = ''
OitoMoedas = ''
OitoMoedas = ''
OitoMoedas = ''
OitoMoedasDia = 'Recoste-se e deixe que tempo trabalhe por você. Você tem um bom faro para perceber que é viável e deverá planejar com calma todos os passos seguintes. Somente impaciência, leviandade e burrice podem impedir um bom resultado. Por isso, não se deixe pressionar por uma eventual pressa no ambiente à sua volta. De preferência, em vez disso, faça alguma coisa pelo seu bem-estar físico e mental.'

NoveMoedas = ''
NoveMoedas = ''
NoveMoedas = ''
NoveMoedas = ''
NoveMoedas = ''
NoveMoedasDia = 'Prepare-se para uma surpresa agradável. Ela poderá vir pelo correio, chegar como uma visita inesperada ou possivelmente estar à sua espera no seu local de trabalho. Também não fará mal se você der uma ajudazinha à sua própria sorte, tomando uma iniciativa. Aproveite momento propício e saia à caça do tesouro. Faça alguma coisa que você até então nunca tenha ousado, experimente algo novo ou compre ao menos um bilhete de loteria.'

DezMoedas = ''
DezMoedas = ''
DezMoedas = ''
DezMoedas = ''
DezMoedas = ''
DezMoedasDia = 'Hoje, utilize os vários recursos disponíveis. Os frutos estão só esperando para serem colhidos. Tome consciência da sua riqueza e proporcione algo de bom para si e para os outros. Se você estiver para fechar um negócio, ou se aparecer uma boa oportunidade para ganhar dinheiro, você deve aproveitar dia para fazê-lo. Tudo que você tocar hoje tem a tendência de se transformar em ouro'

PageMoedas = ''
PageMoedas = ''
PageMoedas = ''
PageMoedas = ''
PageMoedas = ''
PageMoedasDia = 'Hoje, você se encontra no terreno da realidade. Atividades concretas irão atraí-lo muito mais do que idéias mirabolantes e especulativas. Com seu senso prático para solucionar as coisas, você conseguirá com facilidade organizar seu dia-a-dia. Caso trabalho no jardim ou algum outro trabalho manual tenha sido negligenciado nos últimos tempos, você sentirá hoje prazer em realizar essas tarefas. Além disso, sentirá uma enorme vontade de se deliciar com os prazeres da vida. Reserve para isso bastante tempo e aproveite a ótima oportunidade.'

CavaleiroMoedas = ''
CavaleiroMoedas = ''
CavaleiroMoedas = ''
CavaleiroMoedas = ''
CavaleiroMoedas = ''
CavaleiroMoedasDia = 'Hoje, ninguém ou nada poderá derrubá-lo. Você seguirá seu caminho firmemente com a resistência e senso de realidade necessários para concretizar com êxito as suas tarefas. Você estará sentindo-se tão forte e em tão boa forma que certamente não se esquivará de nenhuma prova de força. Porém, você iria gostar mais ainda de se dedicar a um prazer sensual, qual você pudesse desfrutar intensamente'

RainhaMoedas = ''
RainhaMoedas = ''
RainhaMoedas = ''
RainhaMoedas = ''
RainhaMoedas = ''
RainhaMoedasDia = 'Hoje, não se deixe confundir por ninguém ou ser colocado sob pressão. Faça aquilo que você resolveu fazer com calma e tranqüilidade. Você sabe que um bom vinho leva anos para amadurecer. Por isso, não perca de vista a sua meta a longo prazo, e semeie seu campo com paciência e cuidado, para que você possa colher abundantemente. Hoje também uma mulher com um instinto materno e um carisma natural e sensual pode desempenhar um papel importante para você. Confie no conselho que ela lhe dará.'

ReiMoedas = ''
ReiMoedas = ''
ReiMoedas = ''
ReiMoedas = ''
ReiMoedas = ''
ReiMoedasDia = 'Hoje, você deve contemplar os frutos dos seus esforços e desfrutar do seu sucesso. Tome consciência da sua riqueza e descanse sobre os louros da vitória. Se lhe ocorrerem idéias sobre planos que você gostaria de realizar a seguir, é um bom sinal. Mas, tão bom e tão importante quanto isso, seria nos próximos tempos proteger intensamente que já foi conquistado. Talvez um homem bondoso, porém com um jeito austero, desempenhe um papel importante para você no dia de hoje. Ouça os seus conselhos ou aceite as suas sugestões.'



ArcanosMaiores = [
    ['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite00.jpg', '00 - O louco'],
    ['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite01.jpg', '01 - O Mago'], 
    ['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite02.jpg', '02 - A Sacerdotisa'],
    ['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite03.jpg', '03 - A Imperatriz'],
    ['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite04.jpg', '04 - O Imperador'],
    ['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite05.jpg', '05 - O Hierofante'],
    ['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite06.jpg', '06 - Os Amantes'],
    ['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite07.jpg', '07 - O Carro'],
    ['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite08.jpg', '08 - A Força'],
    ['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite09.jpg', '09 - O Eremita'],
    ['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite10.jpg', '10 - A Roda da Fortuna'],
    ['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite11.jpg', '11 - A Justiça'],
    ['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite12.jpg', '12 - O Enforcado'],
    ['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite13.jpg', '13 - A Morte'],
    ['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite14.jpg', '14 - A Temperança'],
    ['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite15.jpg', '15 - O Diabo'],
    ['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite16.jpg', '16 - A Torre'],
    ['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite17.jpg', '17 - A Estrela'],
    ['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite18.jpg', '18 - A Lua'],
    ['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite19.jpg', '19 - O Sol'],
    ['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite20.jpg', '20 - O Julgamento'],
    ['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite21.jpg', '21 - O Mundo']
    ]
ArcanosMenores = [
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite22.jpg', 'Ás de Paus', AsPausDia, AsPausProfissional, AsPausRelacionamento, AsPausEncoraja, AsPausAlerta, AsPausGerais],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite23.jpg', '2 de Paus', DoisPausDia, DoisPausProfissional, DoisPausRelacionamento, DoisPausEncoraja, DoisPausAlerta, DoisPausGerais],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite24.jpg', '3 de Paus', TresPausDia, TresPausProfissional, TresPausRelacionamento, TresPausEncoraja, TresPausAlerta, TresPausGerais],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite25.jpg', '4 de Paus', QuatroPausDia, QuatroPausProfissional, QuatroPausRelacionamento, QuatroPausEncoraja, QuatroPausAlerta, QuatroPausGerais],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite26.jpg', '5 de Paus', CincoPausDia, CincoPausProfissional, CincoPausRelacionamento, CincoPausEncoraja, CincoPausAlerta, CincoPausGerais],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite27.jpg', '6 de Paus', SeisPausDia, SeisPausProfissional, SeisPausRelacionamento, SeisPausEncoraja, SeisPausAlerta, SeisPausGerais],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite28.jpg', '7 de Paus', SetePausDia, SetePausProfissional, SetePausRelacionamento, SetePausEncoraja, SetePausAlerta, SetePausGerais],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite29.jpg', '8 de Paus', OitoPausDia, OitoPausProfissional, OitoPausRelacionamento, OitoPausEncoraja, OitoPausAlerta, OitoPausGerais],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite30.jpg', '9 de Paus', NovePausDia, NovePausProfissional, NovePausRelacionamento, NovePausEncoraja, NovePausAlerta, NovePausGerais],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite31.jpg', '10 de Paus', DezPausDia, DezPausProfissional, DezPausRelacionamento, DezPausEncoraja, DezPausAlerta, DezPausGerais],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite32.jpg', 'Valete de Paus', PagePausDia, PagePausProfissional, PagePausRelacionamento, PagePausEncoraja, PagePausAlerta, PagePausGerais],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite33.jpg', 'Cavaleiro de Paus', CavaleiroPausDia, CavaleiroPausProfissional, CavaleiroPausRelacionamento, CavaleiroPausEncoraja, CavaleiroPausAlerta, CavaleiroPausGerais],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite34.jpg', 'Rainha de Paus', RainhaPausDia, RainhaPausProfissional, RainhaPausRelacionamento, RainhaPausEncoraja, RainhaPausAlerta, RainhaPausGerais],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite35.jpg', 'Rei de Paus', ReiPausDia, ReiPausProfissional, ReiPausRelacionamento, ReiPausEncoraja, ReiPausAlerta, ReiPausGerais],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite36.jpg', 'Ás de Copas'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite37.jpg', '2 de Copas'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite38.jpg', '3 de Copas'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite39.jpg', '4 de Copas'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite40.jpg', '5 de Copas'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite41.jpg', '6 de Copas'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite42.jpg', '7 de Copas'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite43.jpg', '8 de Copas'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite44.jpg', '9 de Copas'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite45.jpg', '10 de Copas'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite46.jpg', 'Valete de Copas'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite47.jpg', 'Cavaleiro de Copas'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite48.jpg', 'Rainha de Copas'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite49.jpg', 'Rei de Copas'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite50.jpg', 'Ás de Espadas'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite51.jpg', '2 de Espadas'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite52.jpg', '3 de Espadas'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite53.jpg', '4 de Espadas'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite54.jpg', '5 de Espadas'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite55.jpg', '6 de Espadas'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite56.jpg', '7 de Espadas'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite57.jpg', '8 de Espadas'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite58.jpg', '9 de Espadas'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite59.jpg', '10 de Espadas'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite60.jpg', 'Valete de Espadas'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite61.jpg', 'Cavaleiro de Espadas'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite62.jpg', 'Rainha de Espadas'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite63.jpg', 'Rei de Espadas'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite64.jpg', 'Ás de Moedas'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite65.jpg', '2 de Moedas'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite66.jpg', '3 de Moedas'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite67.jpg', '4 de Moedas'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite68.jpg', '5 de Moedas'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite69.jpg', '6 de Moedas'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite70.jpg', '7 de Moedas'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite71.jpg', '8 de Moedas'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite72.jpg', '9 de Moedas'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite73.jpg', '10 de Moedas'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite74.jpg', 'Valete de Moedas'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite75.jpg', 'Cavaleiro de Moedas'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite76.jpg', 'Rainha de Moedas'],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite77.jpg', 'Rei de Moedas']
]

TodosArcanos = [
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite00.jpg', '00 - O Louco', LoucoDia],
    ['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite01.jpg', '01 - O Mago', MagoDia], 
    ['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite02.jpg', '02 - A Sacerdotisa', SacerdotisaDia],
    ['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite03.jpg', '03 - A Imperatriz', ImperatrizDia],
    ['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite04.jpg', '04 - O Imperador', ImperadorDia],
    ['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite05.jpg', '05 - O Hierofante', HierofanteDia],
    ['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite06.jpg', '06 - Os Amantes', AmantesDia],
    ['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite07.jpg', '07 - O Carro', CarroDia],
    ['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite08.jpg', '08 - A Força', ForçaDia],
    ['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite09.jpg', '09 - O Eremita', EremitaDia],
    ['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite10.jpg', '10 - A Roda da Fortuna', RodaDia],
    ['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite11.jpg', '11 - A Justiça', JustiçaDia],
    ['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite12.jpg', '12 - O Enforcado', EnforcadoDia],
    ['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite13.jpg', '13 - A Morte', MorteDia],
    ['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite14.jpg', '14 - A Temperança', TemperançaDia],
    ['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite15.jpg', '15 - O Diabo', DiaboDia],
    ['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite16.jpg', '16 - A Torre', TorreDia],
    ['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite17.jpg', '17 - A Estrela', EstrelaDia],
    ['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite18.jpg', '18 - A Lua', LuaDia],
    ['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite19.jpg', '19 - O Sol', SolDia],
    ['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite20.jpg', '20 - O Julgamento', JulgamentoDia],
    ['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite21.jpg', '21 - O Mundo', MundoDia],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite22.jpg', 'Ás de Paus', AsPausDia, AsPausProfissional, AsPausRelacionamento, AsPausEncoraja, AsPausAlerta, AsPausGerais],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite23.jpg', '2 de Paus', DoisPausDia, DoisPausProfissional, DoisPausRelacionamento, DoisPausEncoraja, DoisPausAlerta, DoisPausGerais],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite24.jpg', '3 de Paus', TresPausDia, TresPausProfissional, TresPausRelacionamento, TresPausEncoraja, TresPausAlerta, TresPausGerais],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite25.jpg', '4 de Paus', QuatroPausDia, QuatroPausProfissional, QuatroPausRelacionamento, QuatroPausEncoraja, QuatroPausAlerta, QuatroPausGerais],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite26.jpg', '5 de Paus', CincoPausDia, CincoPausProfissional, CincoPausRelacionamento, CincoPausEncoraja, CincoPausAlerta, CincoPausGerais],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite27.jpg', '6 de Paus', SeisPausDia, SeisPausProfissional, SeisPausRelacionamento, SeisPausEncoraja, SeisPausAlerta, SeisPausGerais],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite28.jpg', '7 de Paus', SetePausDia, SetePausProfissional, SetePausRelacionamento, SetePausEncoraja, SetePausAlerta, SetePausGerais],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite29.jpg', '8 de Paus', OitoPausDia, OitoPausProfissional, OitoPausRelacionamento, OitoPausEncoraja, OitoPausAlerta, OitoPausGerais],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite30.jpg', '9 de Paus', NovePausDia, NovePausProfissional, NovePausRelacionamento, NovePausEncoraja, NovePausAlerta, NovePausGerais],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite31.jpg', '10 de Paus', DezPausDia, DezPausProfissional, DezPausRelacionamento, DezPausEncoraja, DezPausAlerta, DezPausGerais],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite32.jpg', 'Valete de Paus', PagePausDia, PagePausProfissional, PagePausRelacionamento, PagePausEncoraja, PagePausAlerta, PagePausGerais],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite33.jpg', 'Cavaleiro de Paus', CavaleiroPausDia, CavaleiroPausProfissional, CavaleiroPausRelacionamento, CavaleiroPausEncoraja, CavaleiroPausAlerta, CavaleiroPausGerais],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite34.jpg', 'Rainha de Paus', RainhaPausDia, RainhaPausProfissional, RainhaPausRelacionamento, RainhaPausEncoraja, RainhaPausAlerta, RainhaPausGerais],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite35.jpg', 'Rei de Paus' , ReiPausDia, ReiPausProfissional, ReiPausRelacionamento, ReiPausEncoraja, ReiPausAlerta, ReiPausGerais],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite36.jpg', 'Ás de Copas', AsCopasDia],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite37.jpg', '2 de Copas', DoisCopasDia],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite38.jpg', '3 de Copas', TresCopasDia],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite39.jpg', '4 de Copas', QuatroCopasDia],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite40.jpg', '5 de Copas', CincoCopasDia],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite41.jpg', '6 de Copas', SeisCopasDia],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite42.jpg', '7 de Copas', SeteCopasDia],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite43.jpg', '8 de Copas', OitoCopasDia],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite44.jpg', '9 de Copas', NoveCopasDia],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite45.jpg', '10 de Copas', DezCopasDia],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite46.jpg', 'Valete de Copas', PageCopasDia],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite47.jpg', 'Cavaleiro de Copas', CavaleiroCopasDia],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite48.jpg', 'Rainha de Copas', RainhaCopasDia],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite49.jpg', 'Rei de Copas', ReiCopasDia],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite50.jpg', 'Ás de Espadas', AsEspadasDia],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite51.jpg', '2 de Espadas', DoisEspadasDia],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite52.jpg', '3 de Espadas', TresEspadasDia],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite53.jpg', '4 de Espadas', QuatroEspadasDia],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite54.jpg', '5 de Espadas', CincoEspadasDia],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite55.jpg', '6 de Espadas', SeisEspadasDia],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite56.jpg', '7 de Espadas', SeteEspadasDia],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite57.jpg', '8 de Espadas', OitoEspadasDia],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite58.jpg', '9 de Espadas', NoveEspadasDia],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite59.jpg', '10 de Espadas', DezEspadasDia],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite60.jpg', 'Valete de Espadas', PageEspadasDia],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite61.jpg', 'Cavaleiro de Espadas', CavaleiroEspadasDia],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite62.jpg', 'Rainha de Espadas', RainhaEspadasDia],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite63.jpg', 'Rei de Espadas', ReiEspadasDia],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite64.jpg', 'Ás de Moedas', AsMoedasDia],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite65.jpg', '2 de Moedas', DoisMoedasDia],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite66.jpg', '3 de Moedas', TresMoedasDia],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite67.jpg', '4 de Moedas', QuatroMoedasDia],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite68.jpg', '5 de Moedas', CincoMoedasDia],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite69.jpg', '6 de Moedas', SeisMoedasDia],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite70.jpg', '7 de Moedas', SeteMoedasDia],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite71.jpg', '8 de Moedas', OitoMoedasDia],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite72.jpg', '9 de Moedas', NoveMoedasDia],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite73.jpg', '10 de Moedas', DezMoedasDia],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite74.jpg', 'Valete de Moedas', PageMoedasDia],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite75.jpg', 'Cavaleiro de Moedas', CavaleiroMoedasDia],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite76.jpg', 'Rainha de Moedas', RainhaMoedasDia],
	['https://raw.githubusercontent.com/mbione/TarotBot/master/img/RW/riderwaite77.jpg', 'Rei de Moedas', ReiMoedasDia]
]


def start(update, context):

    update.message.reply_text('Bot ainda em testes, envia /dia para receber a carta que fala sobre o seu dia de hoje.')


def dia(update, context):

    random.shuffle(ArcanosMenores)
    random.shuffle(ArcanosMaiores)
    random.shuffle(TodosArcanos)

    #bot.sendPhoto(chat_id, Arcanos[0][0], Arcanos[0][1])
    chat_id = update.message.chat_id
    bot.sendPhoto(chat_id, TodosArcanos[0][0], TodosArcanos[0][1])
    update.message.reply_text(TodosArcanos[0][2])
    #bot.sendPhoto(chat_id, ArcanosMenores[0][0], ArcanosMenores[0][1])


def error(update, context):

    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():

    #updater = Updater("1034516978:AAHTZOJ39mZP7b8HEvjBNvVOP3Y4YBP0tHU", use_context=True)
    #dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("dia", dia))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    updater.idle()


if __name__ == '__main__': 
    main()









    