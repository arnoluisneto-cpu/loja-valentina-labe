import streamlit as st
import random

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

# 3. ENTRADAS DO PRODUTO
col_input1, col_input2 = st.columns(2)

with col_input1:
    produto_nome = st.text_input("NOME DO PRODUTO", placeholder="Ex: Sandália Preta Salto Bloco")
    produto_ref = st.text_input("LINK OU CÓDIGO DE REFERÊNCIA", placeholder="Ex: REF-092 ou Link TikTok Shop")
    tipo_produto = st.selectbox("CATEGORIA DE ATUAÇÃO", [
        "Calçado (Foco nos Pés / Descer Girando)", 
        "Acessório de Pulso (Relógio / Pulseira)", 
        "Acessório de Rosto (Óculos)", 
        "Vestuário / Vestido de Festa",
        "Conjunto Pantalona / Casual",
        "Bolsa / Acessório de Mão",
        "Utilidades & Casa"
    ])
    
with col_input2:
    st.markdown("<p style='font-size:14px; font-weight:600; margin-bottom:5px; color:#ffffff;'>FOTO DA MODELO (FIDELIDADE 1:1)</p>", unsafe_allow_html=True)
    foto_modelo = st.file_uploader("Upload Modelo", type=["jpg", "jpeg", "png"], key="m", label_visibility="collapsed")
    
    st.markdown("<p style='font-size:14px; font-weight:600; margin-top:10px; margin-bottom:5px; color:#ffffff;'>FOTO DO PRODUTO (ALTA DEFINIÇÃO)</p>", unsafe_allow_html=True)
    foto_peca = st.file_uploader("Upload Produto", type=["jpg", "jpeg", "png"], key="p", label_visibility="collapsed")

st.markdown("---")

# 4. BANCO DE ROTEIROS ESPECÍFICOS E NARRATIVAS DIRECIONADAS AO PRODUTO
if st.button("🚀 GERAR PACOTE COMERCIAL (6 HORÁRIOS × 4 ESTILOS = 24 VÍDEOS)"):
    if not produto_nome:
        st.warning("⚠️ Por favor, informe o nome do produto.")
    else:
        st.success("✅ Pacote gerado com sucesso! Prompts hiper-realistas 1:1 e falas focadas diretamente no produto.")
        
        horarios = [
            "09:00 - Manhã (Abertura de Feed)",
            "12:00 - Almoço (Pico de Engajamento)",
            "15:00 - Tarde (Pausa Comercial)",
            "18:00 - Fim de Tarde (Deslocamento)",
            "19:00 - Noite (Pico Principal de Compra)",
            "23:00 - Fechamento (Último Tiro do Dia)"
        ]
        
        # Realismo máximo internacional 8K
        base_realism = "Masterpiece, hyper-realistic 8k resolution, raw aesthetic, natural cinematic lighting, shot on 35mm lens, depth of field, zero digital artifacts, uncompromising 1:1 fidelity to reference face and product."
        
        for i, h in enumerate(horarios):
            prod = produto_nome
            
            # Prompts visuais hiper-realistas adaptados exatamente ao estilo e produto escolhidos
            if "Caminhão" in estilo_persona:
                p1 = f"Cinematic hyper-realistic 8K shot. A large delivery truck backs up right to a modern residential gate. The back doors swing open, revealing massive floor-to-ceiling stacks of TikTok Shop boxes specifically labeled '{prod}'. {base_realism}"
                v1 = f"Gente, vocês não vão acreditar! Acabou de estacionar o caminhão de entregas aqui em casa lotado com o carregamento oficial da nossa {prod}! Olha o tamanho desse lote que chegou do TikTok Shop! Para garantir o seu par antes que acabe, corre na Loja da Valentina e clica no carrinho laranja aqui embaixo."
                
                p2 = f"Hyper-realistic outdoor daylight tracking shot. Model opening the rear doors of a delivery van packed with boxes of '{prod}', natural lighting, authentic documentary style. {base_realism}"
                v2 = f"Olha isso aqui, sério! A van de entregas acabou de chegar trazendo reposição em massa da {prod} que vocês tanto pediram. É muita caixa saindo direto para vocês! Aproveita o estoque limitado na Loja da Valentina, clica no carrinho laranja na tela e garante a sua agora."
                
                p3 = f"Ultra-realistic 8K cinematic shot. Delivery driver unboxing a master carton on the sidewalk, showcasing pristine boxes of '{prod}'. {base_realism}"
                v3 = f"Chegou reposição pesada! O motorista acabou de descarregar os fardos lacrados da {prod} direto na nossa central. Qualidade impecável que vocês já conhecem. Clica no carrinho laranja da Loja da Valentina aqui embaixo e aproveita o frete rápido."
                
                p4 = f"First-person cinematic perspective walking towards a heavy logistics truck loaded with boxes of '{prod}', high detail, real textures. {base_realism}"
                v4 = f"Quem acompanha os Stories sabe o quanto eu esperava por esse dia. O caminhão da {prod} encostou de ré no portão! Olha o estoque absurdo que veio para gente. Clica no carrinho laranja da Loja da Valentina e aproveita o preço promocional de lançamento."

            elif "Calçado" in tipo_produto or "Calçado" in estilo_persona:
                p1 = f"First-person POV looking down. Camera pans smoothly from model's face to a macro close-up framing of the exact footwear '{prod}' from the reference image, showing premium leather, stitching, and heel. {base_realism}"
                v1 = f"Meninas, testei essa {prod} na rua e o conforto e a elegância desse salto são indescritíveis. Olha esse acabamento de perto! Perfeita para qualquer ocasião. Corre na Loja da Valentina, clica no carrinho laranja aqui embaixo e garante a sua."
                
                p2 = f"Full-body tracking shot outdoors, model walking dynamically while wearing the exact '{prod}' from the reference image, natural sunlight. {base_realism}"
                v2 = f"Gente, estou completamente apaixonada por como essa {prod} veste bem no corpo e combina com qualquer look. Olha o design impecável! Disponível agora com desconto exclusivo na Loja da Valentina, clica no carrinho laranja."
                
                p3 = f"Macro close-up shot focusing on the model's feet stepping down gracefully wearing the exact '{prod}', cinematic lighting. {base_realism}"
                v3 = f"Para tudo para o brilho e a sofisticação dessa {prod}! Sério, o salto bloco mais confortável que eu já usei na vida. Não fica sem a sua, clica no carrinho laranja da Loja da Valentina aqui embaixo."
                
                p4 = f"Mirror reflection shot in a luxury boutique dressing room, model showing off the exact '{prod}' on her feet. {base_realism}"
                v4 = f"Olha esse close no espelho com a {prod}! Combinação perfeita de estilo e durabilidade que chegou para revolucionar seu guarda-roupa. Clica no carrinho laranja na Loja da Valentina e aproveita."

            else:
                p1 = f"Vertical {proporcao} photorealistic UGC video, professional smartphone camera style, focusing precisely on '{prod}'. {base_realism}"
                v1 = f"Meninas, olha o nível de detalhe dessa {prod} que acabou de chegar! A qualidade superou todas as expectativas. Corre na Loja da Valentina, clica no carrinho laranja aqui embaixo e garante a sua."
                
                p2 = f"Vertical {proporcao} UGC video, dynamic outdoor walking shot showcasing '{prod}'. {base_realism}"
                v2 = f"Gente, testei essa {prod} e tô simplesmente apaixonada pelo caimento. Perfeita para o dia a dia! Clica no carrinho laranja na Loja da Valentina e aproveita o frete rápido."
                
                p3 = f"Vertical {proporcao} UGC video, smooth cinematic lighting showing '{prod}' in pristine detail. {base_realism}"
                v3 = f"Olha esse destaque exclusivo da {prod}! Reposição limitadíssima que acabou de entrar no ar. Clica no carrinho laranja da Loja da Valentina aqui na tela e garante a sua."
                
                p4 = f"Vertical {proporcao} UGC video, mirror reflection view showcasing '{prod}' with absolute 1:1 fidelity. {base_realism}"
                v4 = f"Não podia deixar de mostrar essa novidade incrível da {prod} para vocês. Preço especial de lançamento na Loja da Valentina, clica no carrinho laranja agora!"

            st.markdown(f"### 🕒 Bloco de Postagem: {h}")
            
            sc1, sc2 = st.columns(2)
            
            with sc1:
                st.markdown(f"""
                <div class="metric-card">
                    <span class="tag-estilo">ESTILO 1: {estilo_persona}</span>
                    <p style='margin-top:10px; color: #ffffff;'><b>Prompt ({proporcao}):</b> {p1}<br><br><b>Fala em Português Brasil:</b> "{v1}"</p>
                </div>
                """, unsafe_allow_html=True)

                st.markdown(f"""
                <div class="metric-card">
                    <span class="tag-estilo">ESTILO 3: Giro Dinâmico 360° / Close Detalhado</span>
                    <p style='margin-top:10px; color: #ffffff;'><b>Prompt ({proporcao}):</b> {p3}<br><br><b>Fala em Português Brasil:</b> "{v3}"</p>
                </div>
                """, unsafe_allow_html=True)

            with sc2:
                st.markdown(f"""
                <div class="metric-card">
                    <span class="tag-estilo">ESTILO 2: Corpo Inteiro / Ação Externa</span>
                    <p style='margin-top:10px; color: #ffffff;'><b>Prompt ({proporcao}):</b> {p2}<br><br><b>Fala em Português Brasil:</b> "{v2}"</p>
                </div>
                """, unsafe_allow_html=True)

                st.markdown(f"""
                <div class="metric-card">
                    <span class="tag-estilo">ESTILO 4: Review Próximo à Câmera</span>
                    <p style='margin-top:10px; color: #ffffff;'><b>Prompt ({proporcao}):</b> {p4}<br><br><b>Fala em Português Brasil:</b> "{v4}"</p>
                </div>
                """, unsafe_allow_html=True)
            
            st.markdown("---")
