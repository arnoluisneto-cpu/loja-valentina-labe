import streamlit as st
import random
import urllib.parse

st.set_page_config(
    page_title="Valentina Labs - TikTok Shop Automation",
    page_icon="💜",
    layout="wide"
)

# CSS Comercial Limpo e Direto / Padrão Multinacional Gringa
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;900&display=swap');
    
    .stApp, .main, div[data-testid="stVerticalBlock"] {
        background-color: #0b0914 !important;
        color: #ffffff !important;
        font-family: 'Inter', sans-serif !important;
    }
    
    .stButton>button, div[data-testid="stFileUploader"] button {
        background-color: #00FF66 !important;
        color: #000000 !important;
        font-weight: 700 !important;
        border-radius: 8px !important;
        border: none !important;
        padding: 12px 20px !important;
        font-size: 16px !important;
    }
    .stButton>button:hover, div[data-testid="stFileUploader"] button:hover {
        background-color: #00cc52 !important;
        color: #ffffff !important;
    }
    .stButton>button {
        width: 100% !important;
    }
    
    .hero-banner {
        background: linear-gradient(135deg, #161026 0%, #22153b 100%);
        border: 2px solid #8A2BE2;
        padding: 20px;
        border-radius: 12px;
        text-align: center;
        margin-bottom: 20px;
        box-shadow: 0px 0px 25px rgba(138, 43, 226, 0.4);
    }
    .hero-title {
        font-size: 34px;
        font-weight: 900;
        letter-spacing: 4px;
        color: #00FF66 !important;
        text-shadow: 0 0 12px rgba(0, 255, 102, 0.5);
        margin: 0;
    }
    
    input, select, textarea, div[data-baseweb="select"] > div {
        background-color: #161026 !important;
        color: #ffffff !important;
        border: 1.5px solid #00FF66 !important;
        border-radius: 8px !important;
        font-family: 'Inter', sans-serif !important;
    }
    
    .stTextInput>div>div>input, .stSelectbox>div>div>select {
        background-color: #161026 !important;
        color: #ffffff !important;
        border: 1.5px solid #00FF66 !important;
        border-radius: 8px !important;
    }
    
    div[data-baseweb="select"] svg, span[data-baseweb="icon"] svg {
        fill: #00FF66 !important;
        color: #00FF66 !important;
    }
    
    div[data-baseweb="popover"], div[data-baseweb="menu"], ul[data-baseweb="menu"] {
        background-color: #161026 !important;
        color: #ffffff !important;
        border: 1.5px solid #00FF66 !important;
    }

    div[data-testid="stFileUploader"] {
        background-color: #161026 !important;
        border: 2px solid #00FF66 !important;
        border-radius: 10px !important;
        padding: 12px !important;
    }
    div[data-testid="stFileUploader"] section {
        background-color: #161026 !important;
    }
    div[data-testid="stFileUploader"] span, div[data-testid="stFileUploader"] small, div[data-testid="stFileUploader"] p {
        color: #ffffff !important;
    }
    
    ::placeholder {
        color: #b0bec5 !important;
        opacity: 1 !important;
    }
    
    .metric-card {
        background-color: #161026 !important;
        border: 1px solid #8A2BE2 !important;
        padding: 16px;
        border-radius: 10px;
        margin-bottom: 15px;
    }
    
    .tag-estilo {
        background-color: #00FF66 !important;
        color: #000000 !important;
        padding: 3px 8px;
        border-radius: 4px;
        font-weight: bold;
        font-size: 12px;
    }
    
    h1, h2, h3, label, .stMarkdown {
        color: #ffffff !important;
        font-family: 'Inter', sans-serif !important;
    }
    </style>
""", unsafe_allow_html=True)

# 1. TOPO COMERCIAL
st.markdown("""
    <div class="hero-banner">
        <h1 class="hero-title">VALENTINA LABS</h1>
        <p style="color: #b0bec5; font-size: 12px; margin-top: 5px; margin-bottom: 0; letter-spacing: 2px;">MÁQUINA DE VÍDEOS EM MASSA • TIKTOK SHOP AUTOMATION</p>
    </div>
""", unsafe_allow_html=True)

# 2. SELETORES
c_top1, c_top2, c_top3 = st.columns(3)
with c_top1:
    diretor_skin = st.selectbox(
        "MOTOR DE INTELIGÊNCIA (SKIN)", 
        [
            "DIRECTOR PRO (Cinematográfico & 1:1)", 
            "UGC LIFESTYLE (Influencer & Conversão)"
        ]
    )
with c_top2:
    proporcao = st.selectbox("FORMATO DE VÍDEO", ["9:16 (TikTok / Reels)", "16:9 (YouTube / Wide)", "1:1 (Feed)"])
with c_top3:
    estilo_persona = st.selectbox("ESTILO DE CONTEÚDO", [
        "1. Caminhão e Van do TikTok Shop Chegando de Ré na Casa com Caixas",
        "2. POV Acordando na Cama (Morning Routine com o Produto)",
        "3. POV Arrumando o Closet / Selecionando Peças",
        "4. POV Imersivo (Olhando para Baixo nos Pés / Calçado)",
        "5. Corpo Inteiro na Rua (Caminhando no Calçadão com Tráfego)",
        "6. Frente ao Espelho (Mirror Selfie com Transição Secundária)",
        "7. Giro Dinâmico 360° (Mostrando Caimento e Balanço do Tecido)",
        "8. Close Macro Cirúrgico (Foco Total em Costura e Detalhes)",
        "9. Unboxing Surpresa em Cima da Mesa com Ring Light",
        "10. Transição Rápida de Looks (Trend de Troca Instantânea)",
        "11. Vlog de Rotina Diária Estilo Lifestyle (Dia a Dia Corrido)",
        "12. Review Sincero Boca a Boca (Falando Bem de Perto com a Câmera)",
        "13. Provador Rápido de Loja Física (Provando na Frente do Espelho)",
        "14. Trend do Sofá / Almofada (Apresentação Casual Relaxada)",
        "15. POV Dirigindo o Carro (Mostrando Acessório no Volante/Pulso)",
        "16. POV Café da Manhã na Mesa Posta (Estilo Blogueira Chique)",
        "17. Challenge de Transição: Roupa Simples para Look Completo de Luxo",
        "18. Unboxing Rasgando Pacote do TikTok Shop de Surpresa",
        "19. POV Saindo da Academia / Fitness Check com Estilo",
        "20. POV Encontro Noturno / Night Out Look Reveal"
    ])

st.markdown("---")

# 3. ENTRADAS DO PRODUTO (100% UNIVERSAIS E DINÂMICAS)
col_input1, col_input2 = st.columns(2)

with col_input1:
    produto_nome = st.text_input("DESCRIÇÃO DO PRODUTO (DIGITE MANUALMENTE)", placeholder="Ex: Vestido Longo Elegante / Relógio Smartwatch / Bolsa de Couro")
    produto_link = st.text_input("LINK OU CÓDIGO DE REFERÊNCIA DO TIKTOK SHOP", placeholder="Ex: https://tiktok.com/shop/item/... ou REF-092")
    tipo_produto = st.selectbox("CATEGORIA GERAL", [
        "Calçado / Tênis / Sandália", 
        "Acessório de Pulso (Relógio / Pulseira)", 
        "Acessório de Rosto (Óculos / Joia)", 
        "Vestuário / Vestido / Conjunto",
        "Bolsa / Acessório de Mão",
        "Utilidades & Outros"
    ])
    
with col_input2:
    st.markdown("<p style='font-size:14px; font-weight:600; margin-bottom:5px; color:#ffffff;'>FOTO DA MODELO (FIDELIDADE 1:1 ABSOLUTA)</p>", unsafe_allow_html=True)
    foto_modelo = st.file_uploader("Upload Modelo", type=["jpg", "jpeg", "png"], key="m", label_visibility="collapsed")
    
    st.markdown("<p style='font-size:14px; font-weight:600; margin-top:10px; margin-bottom:5px; color:#ffffff;'>FOTO DO PRODUTO (ALTA DEFINIÇÃO)</p>", unsafe_allow_html=True)
    foto_peca = st.file_uploader("Upload Produto", type=["jpg", "jpeg", "png"], key="p", label_visibility="collapsed")

st.markdown("---")

# 4. GERADOR UNIVERSAL DINÂMICO BASEADO NO LINK E NA DESCRIÇÃO DO USUÁRIO
if st.button("🚀 GERAR PACOTE COMERCIAL (6 HORÁRIOS × 4 ESTILOS = 24 VÍDEOS)"):
    if not produto_nome:
        st.warning("⚠️ Por favor, informe a descrição do produto.")
    else:
        link_analalisado = "Link de referência integrado" if produto_link else "Descrição manual informada"
        if produto_link:
            parsed_url = urllib.parse.urlparse(produto_link)
            if parsed_url.netloc:
                link_analalisado = f"Origem do link: {parsed_url.netloc}"

        st.success(f"✅ Pacote universal gerado com sucesso! ({link_analalisado}) - Adaptado 100% ao produto informado.")
        
        horarios = [
            "09:00 - Manhã (Abertura de Feed)",
            "12:00 - Almoço (Pico de Engajamento)",
            "15:00 - Tarde (Pausa Comercial)",
            "18:00 - Fim de Tarde (Deslocamento)",
            "19:00 - Noite (Pico Principal de Compra)",
            "23:00 - Fechamento (Último Tiro do Dia)"
        ]
        
        base_realism = (
            f"Masterpiece, hyper-realistic 8k resolution, raw aesthetic, natural cinematic lighting, shot on 35mm lens, depth of field, zero digital artifacts. "
            f"LINK & PRODUCT REFERENCE ANALYSIS: Extracting specs from source link '{produto_link}' and description '{produto_nome}'. "
            "STRICT 1:1 MODEL & PRODUCT FIDELITY: The exact facial structure, skin tone, hair, and identity from the uploaded reference model photo must be precisely preserved in every single frame without any changes. "
            "EXACT PRODUCT MATCH: The item in the video must match the reference product photo and description down to every minor detail, color, texture, and branding. "
            "NO RANDOM OBJECTS OR SCENERY CHANGES: Absolute realism, strictly prohibiting AI from inventing extra accessories or altering background elements."
        )
        
        for i, h in enumerate(horarios):
            prod = produto_nome
            
            if "Caminhão" in estilo_persona:
                p1 = f"Ultra-realistic cinematic sequence. Featuring the exact reference model matching the uploaded photo 1:1. The model starts inside a modern bedroom, walks towards the glass door, opens it, and steps outside. In front of the gate, a massive delivery truck is parked in reverse, doors open with stacked branded boxes of '{prod}'. The model opens a box and holds the exact item '{prod}' in her hands to showcase it. {base_realism}"
                v1 = f"Meninas, vocês não têm noção! Eu estava no quarto organizando minhas coisas, olhei lá fora e o caminhão de entregas acabou de encostar de ré no portão lotado com o novo lote de {prod}! Olha eu com o produto aqui tirando direto da caixa que acabei de pegar na mão. Chegou muita mercadoria e todo esse estoque está com um preço super promocional na Loja da Valentina. Clica no carrinho laranja aqui embaixo e garante o seu."
                
                p2 = f"Photorealistic 8K continuous shot. Featuring the exact reference model with 1:1 face match. The model opens her front door to a delivery van packed with branded boxes of '{prod}', takes a box, opens it, and lifts the exact item '{prod}' with her hands to show the camera. {base_realism}"
                v2 = f"Gente, olha isso! Abri a porta de casa agora pouco e me deparei com a van de entregas trazendo o carregamento completo de {prod}! Está cheio de caixas da marca aqui na frente, e estou abrindo para mostrar o produto de perto na minha mão. Todo esse estoque recém-chegado está com uma promoção especial na Loja da Valentina, clica no carrinho laranja aqui embaixo para aproveitar."
                
                p3 = f"Cinematic real-world tracking shot. Exact reference model matching the uploaded photo 1:1. The model walks to the front porch as a logistics truck opens its rear bay. She reaches into a box and holds up the exact item '{prod}' in her hands, showing crisp branding and details. {base_realism}"
                v3 = f"Olha o tamanho dessa entrega que acabou de chegar aqui em casa! Veio direto para abastecer nosso estoque com {prod}. Estou segurando o item na mão para vocês verem o acabamento perfeito. Aproveita que este lote está saindo por um preço promocional exclusivo na Loja da Valentina, clica no carrinho laranja aqui embaixo."
                
                p4 = f"First-person realistic perspective. Exact reference model with strict 1:1 facial preservation. She opens her house door, approaches a delivery truck parked in the driveway, opens a carton, and showcases the exact item '{prod}' in her hands. {base_realism}"
                v4 = f"Quem me acompanha sabe o quanto eu esperava por esse dia. O caminhão de {prod} veio de ré direto no meu portão! Estou mostrando o produto diretamente da caixa na minha mão. Tudo isso já está disponível na Loja da Valentina com uma promoção imperdível, clica no carrinho laranja aqui embaixo."

            elif "Calçado" in tipo_produto or "Calçado" in estilo_persona:
                p1 = f"First-person POV looking down. Featuring the exact reference model matching the uploaded photo 1:1, wearing the exact footwear item '{prod}' on her feet. Camera pans smoothly from the model's face down to a macro close-up framing of the footwear, then she holds the exact item in her hands. {base_realism}"
                v1 = f"Meninas, testei {prod} no pé e o conforto disso é surreal. Olha esse acabamento na minha mão de perto! Esse lote chegou com um preço super promocional na Loja da Valentina, clica no carrinho laranja aqui embaixo e garante o seu."
                
                p2 = f"Full-body tracking shot outdoors, exact reference model with 1:1 facial match, wearing the exact item '{prod}' on her feet and holding another unit in her hands. {base_realism}"
                v2 = f"Gente, estou completamente apaixonada por como {prod} veste bem no corpo e combina com qualquer look. Disponível agora com desconto promocional na Loja da Valentina, corre para aproveitar."
                
                p3 = f"Macro close-up shot focusing on the model's feet wearing the exact item '{prod}', then lifting her foot or holding the piece in her hands for detailed inspection. Cinematic lighting. {base_realism}"
                v3 = f"Para tudo para o brilho e a sofisticação de {prod}! Qualidade impecável, tanto no uso quanto mostrando os detalhes na mão. Aproveita que está na promoção na Loja da Valentina, clica no carrinho laranja."
                
                p4 = f"Mirror reflection shot in a luxury boutique dressing room, exact reference model with strict 1:1 identity match, wearing the exact item '{prod}' and showcasing it to the mirror. {base_realism}"
                v4 = f"Olha esse close no espelho com {prod}! Qualidade impecável que chegou com preço promocional na Loja da Valentina, clica no carrinho laranja agora!"

            else:
                p1 = f"Vertical {proporcao} photorealistic UGC video, professional smartphone camera style, showcasing the exact item '{prod}' in her hands and interacting with it. Exact reference model with strict 1:1 face match. {base_realism}"
                v1 = f"Meninas, olha o nível de detalhe de {prod} que estou segurando na mão! A qualidade superou todas as expectativas e veio com um preço super promocional na Loja da Valentina. Clica no carrinho laranja aqui embaixo."
                
                p2 = f"Vertical {proporcao} UGC video, dynamic outdoor walking shot showcasing {prod}. Exact reference model with strict 1:1 face match. {base_realism}"
                v2 = f"Gente, testei {prod} e tô apaixonada por como o resultado ficou perfeito. Aproveita a promoção na Loja da Valentina, clica no carrinho laranja."
                
                p3 = f"Vertical {proporcao} UGC video, smooth cinematic lighting showing {prod} in pristine detail. Strict 1:1 face match. {base_realism}"
                v3 = f"Olha esse destaque exclusivo de {prod}! Reposição fresquinha que entrou em promoção na Loja da Valentina, clica no carrinho laranja aqui na tela."
                
                p4 = f"Vertical {proporcao} UGC video, mirror reflection view showcasing {prod} with absolute 1:1 fidelity. Strict 1:1 face match. {base_realism}"
                v4 = f"Não podia deixar de mostrar essa novidade incrível de {prod} para vocês. Preço promocional imperdível na Loja da Valentina, clica no carrinho laranja agora!"

            st.markdown(f"### 🕒 Bloco de Postagem: {h}")
            
            sc1, sc2 = st.columns(2)
            
            with sc1:
                st.markdown(f"""
                <div class="metric-card">
                    <span class="tag-estilo">ESTILO 1: {estilo_persona}</span>
                </div>
                """, unsafe_allow_html=True)
                st.text_area(f"Prompt Visual (Estilo 1 - Bloco {i})", p1, key=f"p1_{i}", height=100)
                st.text_area(f"Fala em Português (Estilo 1 - Bloco {i})", v1, key=f"v1_{i}", height=70)

                st.markdown(f"""
                <div class="metric-card" style="margin-top: 15px;">
                    <span class="tag-estilo">ESTILO 3: Giro Dinâmico 360° / Close Detalhado</span>
                </div>
                """, unsafe_allow_html=True)
                st.text_area(f"Prompt Visual (Estilo 3 - Bloco {i})", p3, key=f"p3_{i}", height=100)
                st.text_area(f"Fala em Português (Estilo 3 - Bloco {i})", v3, key=f"v3_{i}", height=70)

            with sc2:
                st.markdown(f"""
                <div class="metric-card">
                    <span class="tag-estilo">ESTILO 2: Corpo Inteiro / Ação Externa</span>
                </div>
                """, unsafe_allow_html=True)
                st.text_area(f"Prompt Visual (Estilo 2 - Bloco {i})", p2, key=f"p2_{i}", height=100)
                st.text_area(f"Fala em Português (Estilo 2 - Bloco {i})", v2, key=f"v2_{i}", height=70)

                st.markdown(f"""
                <div class="metric-card" style="margin-top: 15px;">
                    <span class="tag-estilo">ESTILO 4: Review Próximo à Câmera</span>
                </div>
                """, unsafe_allow_html=True)
                st.text_area(f"Prompt Visual (Estilo 4 - Bloco {i})", p4, key=f"p4_{i}", height=100)
                st.text_area(f"Fala em Português (Estilo 4 - Bloco {i})", v4, key=f"v4_{i}", height=70)
            
            st.markdown("---")
