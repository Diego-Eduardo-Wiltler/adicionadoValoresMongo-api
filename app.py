from fastapi import FastAPI

app = FastAPI()

lista_produtos = [
    {"produto": "Smartphone Samsung Galaxy S21 Ultra", "descricao": "O melhor smartphone da Samsung com câmera de alta resolução e tela AMOLED.", "categoria": "Eletrônicos"},    
    {"produto": "Notebook Dell XPS 13", "descricao": "Um dos melhores notebooks no mercado com alta performance e tela InfinityEdge.", "categoria": "Informática"},    
    {"produto": "Smartwatch Apple Watch Series 6", "descricao": "Um dos melhores smartwatches no mercado com monitoramento de saúde avançado e tela sempre ligada.", "categoria": "Eletrônicos"},    {"produto": "Tablet Apple iPad Pro", "descricao": "O melhor tablet da Apple com tela de alta resolução e processador A12Z Bionic.", "categoria": "Eletrônicos"},    
    {"produto": "Fone de Ouvido Sony WH-1000XM4", "descricao": "Um dos melhores fones de ouvido no mercado com cancelamento de ruído e alta qualidade de som.", "categoria": "Informática"},    
    {"produto": "Smart TV LG OLED CX", "descricao": "A melhor Smart TV da LG com resolução 4K e tecnologia OLED.", "categoria": "Televisores"},
    {"produto": "Câmera Fotográfica Sony A7 III", "descricao": "Uma das melhores câmeras no mercado para fotografia profissional com resolução 4K.", "categoria": "eletrônicos"},    
    {"produto": "Monitor Gamer Alienware 34 AW3420DW", "descricao": "O melhor monitor para jogos no mercado com resolução ultrawide e taxa de atualização de 120Hz.", "categoria": "eletrônicos"},    {"produto": "Impressora Multifuncional HP Laserjet Pro MFP M428fdw", "descricao": "Uma das melhores impressoras multifuncionais no mercado com alta velocidade de impressão e conectividade Wi-Fi.", "categoria": "eletrônicos"},    
    {"produto": "Roteador Wi-Fi Asus RT-AC68U", "descricao": "Um dos melhores roteadores Wi-Fi no mercado com alta velocidade de conexão e segurança avançada.", "categoria": "eletrônicos"},    
    {"produto": "Caixa de Som JBL Xtreme 3", "descricao": "Uma das melhores caixas de som portáteis no mercado com alta qualidade de som e resistência à água.", "categoria": "eletrônicos"},    
    {"produto": "Console PlayStation 5", "descricao": "O mais novo console da Sony com resolução 4K e suporte a tecnologia Ray Tracing.", "categoria": "eletrônicos"},    
    {"produto": "Teclado Gamer Razer Huntsman Elite", "descricao": "Um dos melhores teclados para jogos no mercado com teclas mecânicas e iluminação RGB.", "categoria": "eletrônicos"},    
    {"produto": "Mouse Gamer Logitech G502 HERO", "descricao": "Um dos melhores mouses para jogos no mercado com alta precisão e iluminação RGB.", "categoria": "eletrônicos"},    
    {"produto": "Headset Gamer HyperX Cloud Alpha", "descricao": "Um dos melhores headsets para jogos no mercado com alta qualidade de som e microfone destacável.", "categoria": "eletrônicos"},    {"produto": "Webcam Logitech StreamCam", "descricao": "Uma das melhores webcams no mercado com resolução Full HD e qualidade de imagem superior.", "categoria": "eletrônicos"},
    {"produto": "Drone DJI Mavic Air 2", "descricao": "Um dos melhores drones no mercado com câmera de alta resolução e autonomia de voo de até 34 minutos.", "categoria": "tecnologia"},    
    {"produto": "Cadeira Gamer DXRacer Formula", "descricao": "Uma das melhores cadeiras para jogos no mercado com design ergonômico e ajuste de altura e inclinação.", "categoria": "móveis"},    
    {"produto": "Placa de Vídeo Nvidia GeForce RTX 3080", "descricao": "Uma das melhores placas de vídeo no mercado para jogos e renderização com tecnologia Ray Tracing e memória GDDR6X de alta velocidade", "categoria": "tecnologia"},    
    {"produto": "Smart Speaker Amazon Echo Dot", "descricao": "Um dos melhores smart speakers no mercado com assistente virtual Alexa e integração com diversos dispositivos.", "categoria": "tecnologia"},    {"produto": "Smart Thermostat Nest Learning", "descricao": "Um dos melhores termostatos inteligentes no mercado com aprendizado automático e controle remoto pelo celular.", "categoria": "casa"},    {"produto": "Smart Lock August Wi-Fi Smart Lock", "descricao": "Uma das melhores fechaduras inteligentes no mercado com controle remoto pelo celular e integração com assistentes virtuais.", "categoria": "casa"},    
    {"produto": "Smart Scale Withings Body+", "descricao": "Uma das melhores balanças inteligentes no mercado com monitoramento de saúde avançado e conexão com app no celular.", "categoria": "saúde"},    {"produto": "Smart Garden Click and Grow", "descricao": "Uma das melhores hortas inteligentes no mercado com cultivo automático e conexão com app no celular.", "categoria": "casa"},    
    {"produto": "Drone DJI Phantom 4 Pro", "descricao": "Um dos melhores drones no mercado com câmera de alta resolução e estabilização de imagem avançada.", "categoria": "tecnologia"},    
    {"produto": "Laptop Lenovo ThinkPad X1 Carbon", "descricao": "Um dos melhores laptops corporativos no mercado com alta performance e durabilidade.", "categoria": "tecnologia"},    
    {"produto": "Smart Lock Schlage Encode", "descricao": "Uma das melhores fechaduras inteligentes no mercado com conectividade Wi-Fi e controle remoto pelo celular.", "categoria": "casa"},    
    {"produto": "Smart Speaker Sonos One", "descricao": "Um dos melhores smart speakers no mercado com alta qualidade de som e integração com assistentes virtuais.", "categoria": "tecnologia"},
    {"produto": "Smart Display Google Nest Hub Max", "descricao": "Um dos melhores smart displays no mercado com tela grande e integração com assistente virtual Google Assistant.", "categoria": "tecnologia"},    
    {"produto": "Smartwatch Garmin Forerunner 945", "descricao": "Um dos melhores smartwatches para corrida no mercado com monitoramento avançado de atividade física e GPS.", "categoria": "saúde"},    {"produto": "Soundbar Sonos Arc", "descricao": "Uma das melhores soundbars no mercado com alta qualidade de som e tecnologia Dolby Atmos.", "categoria": "áudio"},    
    {"produto": "Câmera de Segurança Arlo Pro 4", "descricao": "Uma das melhores câmeras de segurança no mercado com resolução 2K e conectividade Wi-Fi.", "categoria": "segurança"},    
    {"produto": "Monitor LG Ultrafine 5K", "descricao": "Um dos melhores monitores no mercado com resolução 5K e conectividade Thunderbolt 3.", "categoria": "tecnologia"},    
    {"produto": "Smart Lock Yale Assure Lock", "descricao": "Uma das melhores fechaduras inteligentes no mercado com controle remoto pelo celular e integração com assistentes virtuais.", "categoria": "casa"},    
    {"produto": "Smart Speaker Bose Home Speaker 500", "descricao": "Um dos melhores smart speakers no mercado com alta qualidade de som e integração com assistentes virtuais.", "categoria": "áudio"},    {"produto": "Smartwatch Samsung Galaxy Watch 3", "descricao": "Um dos melhores smartwatches no mercado com monitoramento de saúde avançado e conectividade LTE.", "categoria": "saúde"},    
    {"produto": "Laptop Apple MacBook Pro", "descricao": "Um dos melhores laptops no mercado com tela Retina e processador de última geração.", "categoria": "tecnologia"},    
    {"produto": "Câmera Mirrorless Fujifilm X-T4", "descricao": "Uma das melhores câmeras no mercado para fotografia e vídeo com resolução 4K e estabilização de imagem no corpo.", "categoria": "fotografia"},    
    {"produto": "HD Externo Seagate Backup Plus", "descricao": "Um dos melhores HDs externos no mercado com alta capacidade de armazenamento e velocidade de transferência de dados.", "categoria": "tecnologia"},    
    {"produto": "Monitor Dell UltraSharp U2719D", "descricao": "Um dos melhores monitores no mercado com resolução QHD e ampla gama de cores.", "categoria": "tecnologia"}, 
    {"produto": "Monitor Dell UltraSharp U2719D", "descricao": "Um dos melhores monitores no mercado com resolução QHD e ampla gama de cores.", "categoria": "Monitores"}, 
    {"produto": "Impressora Fotográfica Canon Selphy CP1300", "descricao": "Uma das melhores impressoras fotográficas portáteis no mercado com qualidade de imagem superior.", "categoria": "Impressoras"}, 
    {"produto": "Projetor Epson Home Cinema 5050UB", "descricao": "Um dos melhores projetores para home theater no mercado com resolução 4K e tecnologia HDR.", "categoria": "Projetores"}, 
    {"produto": "Caixa de Som Bluetooth Bose SoundLink Revolve+", "descricao": "Uma das melhores caixas de som Bluetooth portáteis no mercado com som em 360 graus e resistência à água.", "categoria": "Caixas de Som"},
    {"produto": "Console Xbox Series X", "descricao": "O mais novo console da Microsoft com resolução 4K e suporte a tecnologia Ray Tracing.", "categoria": "Consoles"}, 
    {"produto": "Teclado Mecânico Corsair K95 RGB Platinum XT", "descricao": "Um dos melhores teclados mecânicos no mercado com teclas programáveis e iluminação RGB.", "categoria": "Teclados"}, 
    {"produto": "Mouse sem fio Microsoft Surface", "descricao": "Um dos melhores mouses sem fio no mercado com alta precisão e design ergonômico.", "categoria": "Mouses"}, 
    {"produto": "Headset Bose QuietComfort 35 II", "descricao": "Um dos melhores headsets com cancelamento de ruído no mercado com alta qualidade de som e conforto.", "categoria": "Headsets"}, 
    {"produto": "Câmera de Segurança Arlo Pro 4", "descricao": "Uma das melhores câmeras de segurança no mercado com resolução 2K e visão noturna em cores.", "categoria": "Câmeras de Segurança"}, 
    {"produto": "Smart Speaker Amazon Echo Studio", "descricao": "Um dos melhores smart speakers no mercado com som de alta qualidade e compatibilidade com assistentes virtuais.", "categoria": "Smart Speakers"}, 
    {"produto": "Aspirador de Pó Robô iRobot Roomba i7+", "descricao": "Um dos melhores aspiradores de pó robô no mercado com mapeamento inteligente e esvaziamento automático do coletor.", "categoria": "Aspiradores de Pó"}
] 


lista_nomes = [
    "Ana Carolina",
    "Alice Lopes",
    "Arthur Fernandes",
    "Beatriz Souza",
    "Bruno Moraes",
    "Carolina Mendes",
    "Carlos Eduardo",
    "Cassia Nascimento",
    "Cesar Augusto",
    "Daniel Alves",
    "Danilo Oliveira",
    "David Silva",
    "Denise Ferreira",
    "Diego Oliveira",
    "Eduardo Santos",
    "Elias Santos",
    "Fabiana Lima",
    "Felipe Martins",
    "Fernanda Rocha",
    "Flavio Costa",
    "Gabriel Lima",
    "Giovanna Santos",
    "Guilherme Sousa",
    "Heloísa Fernandes",
    "Hugo Castro",
    "Igor Ribeiro",
    "Isadora Rodrigues",
    "Jéssica Silva",
    "João Paulo",
    "José Augusto",
    "Julia Almeida",
    "Karina Santos",
    "Kauan Oliveira",
    "Kézia Costa",
    "Leandro Oliveira",
    "Letícia Alves",
    "Lorena Souza",
    "Lucas Ferreira",
    "Luciana Lima",
    "Luiz Fernando",
    "Manuela Silva",
    "Marcelo Oliveira",
    "Marcos Souza",
    "Maria Eduarda",
    "Matheus Almeida",
    "Mayara Fernandes",
    "Mônica Lopes",
    "Nathalia Souza",
    "Nicolas Alves",
    "Paula Fernandes",
    "Pedro Ribeiro",
    "Priscila Silva",
    "Rafael Costa",
    "Ramon Oliveira",
    "Raquel Santos",
    "Renan Almeida",
    "Roberto Castro",
    "Rodrigo Santos",
    "Samuel Alves",
    "Sara Oliveira",
    "Simone Fernandes",
    "Thiago Souza",
    "Valentina Silva",
    "Vanessa Lima",
    "Victor Ferreira",
    "Vinícius Almeida",
    "Viviane Ribeiro",
    "Wallace Oliveira",
    "Wesley Costa",
    "Yasmin Alves",
    "Yuri Souza",
    "Ethan Adams",
    "Hannah Baker",
    "Oliver Barnes",
    "Sofia Bennett",
    "Liam Black",
    "Avery Brooks",
    "Charlotte Brown",
    "Maxwell Butler",
    "Abigail Campbell",
    "Noah Carter",
    "Ella Chapman",
    "Elijah Clark",
    "Amelia Collins",
    "Alexander Cook",
    "Scarlett Cooper",
    "Mason Cox",
    "Mia Davis",
    "Lucas Diaz",
    "Emily Edwards",
    "William Evans",
    "Harper Foster",
    "Benjamin Garcia",
    "Grace Gibson",
    "Daniel Gonzalez",
    "Chloe Gray",
    "Logan Green",
    "Victoria Hall",
    "Henry Hamilton",
    "Aria Harper",
    "Caleb Harrison",
    "Aurora Hill",
    "Owen Howard",
    "Eva Hughes",
    "Jackson Jackson",
    "Elizabeth James",
    "Levi Jenkins",
    "Evelyn Johnson",
    "Carter Jones",
    "Eva Kelly",
    "Nicholas Kim",
    "Madison King",
    "Elijah Lee",
    "Avery Lewis",
    "Daniel Lopez",
    "Natalie Martin",
    "Grayson Martinez",
    "Avery Mason",
    "Makayla Matthews",
    "Gabriel Mcdonald",
    "Audrey Mitchell",
    "William Moore",
    "Brielle Morgan",
    "Lincoln Morris",
    "Aria Murphy",
    "Isaac Nelson",
    "Hazel Nguyen",
    "Ethan Parker",
    "Avery Perez",
    "Oscar Phillips",
    "Avery Powell",
    "Aurora Price",
    "Elijah Ramirez",
    "Sofia Reed",
    "Jacob Reyes",
    "Audrey Richardson",
    "Noah Rivera",
    "Layla Roberts",
    "Landon Robinson",
    "Avery Rodriguez",
    "Sophie Rogers",
    "Leo Ross",
    "Caroline Russell",
    "Ethan Ryan",
    "Kinsley Sanchez",
    "Jackson Sanders",
    "Liliana Scott",
    "Logan Simmons",
    "Eva Singh",
    "Oliver Smith",
    "Harper Stewart",
    "Landon Sullivan",
    "Aria Taylor",
    "Ethan Thomas",
    "Avery Thompson",
    "Sophia Torres",
    "Avery Turner",
    "Isabella Walker",
    "Carter Ward",
    "Elizabeth Watson",
    "Henry White",
    "Eva Williams",
    "Ethan Wilson",
    "Madison Wood",
    "Mason Wright",
    "Chloe Young"   
]

@app.get("/lista_produtos")
async def get_lista_produtos():
    return {"lista_produtos": lista_produtos}

@app.get("/lista_nomes")
async def get_nomes():
    return {"lista_nomes": lista_nomes}
