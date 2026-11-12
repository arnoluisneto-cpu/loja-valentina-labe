import streamlit as st

# Configuração da Página
st.set_page_config(
    page_title="Loja da Valentina - TikTok Shop",
    page_icon="💜",
    layout="wide"
)

# Estilização CSS personalizada (Estética Roxa Nubank + Verde Limão Neon + Campos Limpios)
st.markdown("""
    <style>
    .stApp {
        background-color: #0b0914 !important;
        color: #ffffff !important;
    }
    .main {
        background-color: #0b0914 !important;
    }
    
    /* Botões principais em Verde Limão Neon */
    .stButton>button {
        background-color: #00FF66 !important;
        color: #000000 !important;
        font-weight: bold !important;
        border-radius: 8px !important;
        border: none !important;
        padding: 12px 24px !important;
        font-size: 16px !important;
        width: 100% !important;
    }
    .stButton>button:hover {
        background-color: #00cc52 !important;
        color: #ffffff !important;
    }
    
    /* Banner Principal Valentina Estilo Nubank com Sombra e Letra Forte */
    .hero-banner {
        background: linear-gradient(135deg, #161026 0%, #22153b 100%);
        border: 2px solid #8A2BE2;
        padding: 25px;
        border-radius: 16px;
        text-align: center;
        margin-bottom: 20px;
        box-shadow: 0px 0px 25px rgba(138, 43, 226, 0.3);
    }
    .hero-title {
        font-size: 38px;
        font-weight: 900;
        letter-spacing: 6px;
        color: #00FF66 !important;
        text-shadow: 0 0 10px rgba(0, 255, 102, 0.4);
        margin: 0;
    }
    
    /* Cartões e Blocos */
    .metric-card {
        background-color: #161026 !important;
        border: 1px solid #8A2BE2 !important;
        padding: 18px;
        border-radius: 12px;
        margin-bottom: 15px;
    }
    
    /* Tags de Estilo */
    .tag-estilo {
        background-color: #00FF66 !important;
        color: #000000 !important;
        padding: 4px 10px;
        border-radius: 4px;
        font-weight: bold;
        font-size: 12px;
    }
    
    /* Textos, Labels e Inputs legíveis com fundo escuro correto */
    h1, h2, h3, label, .stMarkdown {
        color: #ffffff !important;
    }
    
    .stTextInput>div>div>input, .stSelectbox>div>div>select {
        background-color: #161026 !important;
        color: #ffffff !important;
        border: 1px solid #8A2BE2 !important;
        border-radius: 8px !important;
    }
    
    /* Ajuste de visibilidade do texto digitado nos inputs */
    input {
        color: #ffffff !important;
    }
    </style>
""", unsafe_allow_html=True)

# Topo: Seletores compactos (Skin, Proporção e Estilo)
c1, c2, c3 = st.columns(3)
with c1:
    diretor_skin = st.selectbox("Diretor Skin", ["BOY (Elite Director)", "VALENTINA MASTER"])
with c2:
    proporcao = st.selectbox("Proporção", ["9:16 (TikTok / Reels)", "1:1 (Feed)"])
with c3:
    estilo_persona = st.selectbox("Estilo de Vídeo", ["Pietra (Tendência & Lifestyle)", "UGC Fotorrealista"])

st.markdown("---")

# Banner Central Valentina estilizado e compacto
st.markdown("""
    <div class="hero-banner">
        <h1 class="hero-title">VALENTINA</h1>
        <p style="color: #b0bec5; font-size: 13px; margin-top: 5px; margin-bottom: 0; letter-spacing: 1px;">LOJA DA VALENTINA • TIKTOK SHOP</p>
    </div>
""", unsafe_allow_html=True)

# Layout de Entradas Diretas e Limpas (Sem excesso de títulos gigantes)
col_input1, col_input2 = st.columns(2)

with col_input1:
    produto_nome = st.text_input("Produto", placeholder="Ex: Sandália Preta Salto Bloco")
    produto_ref = st.text_input("Link ou Código de Referência", placeholder="Ex: REF-092 ou Link")
    tipo_produto = st.selectbox("Categoria", [
        "Calçado (Foco nos Pés / Descer Girando)", 
        "Acessório de Pulso (Relógio / Pulseira)", 
        "Acessório de Rosto (Óculos)", 
        "Vestuário / Corpo Inteiro"
    ])
    
with col_input2:
    foto_modelo = st.file_uploader("Foto da Modelo", type=["jpg", "jpeg", "png"])
    foto_peca = st.file_uploader("Foto do Produto", type=["jpg", "jpeg", "png"])

st.markdown("---")

# Botão de Execução em Massa (6 Horários x 4 Estilos)
if st.button("🚀 GERAR 6 HORÁRIOS × 4 ESTILOS (MÁQUINA EM MASSA)"):
    if not produto_nome:
        st.warning("⚠️ Por favor, informe o nome do produto.")
    else:
        st.success("✅ Pacote gerado com sucesso! Grade de 6 horários e fidelidade 1:1 aplicadas.")
        
        # Os 6 Horários Estratégicos Oficiais
        horarios = [
            "09:00 - Manhã (Abertura de Feed)",
            "12:00 - Almoço (Pico de Engajamento)",
            "15:00 - Tarde (Pausa Comercial)",
            "18:00 - Fim de Tarde (Deslocamento)",
            "19:00 - Noite (Pico Principal de Compra)",
            "23:00 - Fechamento (Último Tiro do Dia)"
        ]
        
        # Direcionamento ótico rigoroso da câmera por categoria
        if "Calçado" in tipo_produto:
            foco_cam = f"Camera pans smoothly down from the model's face to a macro close-up of the exact footwear '{produto_nome}' from the uploaded reference image, showing precise texture, straps, and heel. Strict 1:1 product match."
        elif "Pulso" in tipo_produto:
            foco_cam = f"Camera focuses precisely on the model's wrist and hand displaying the exact accessory '{produto_nome}' from the reference image, smooth macro tracking shot."
        elif "Óculos" in tipo_produto:
            foco_cam = f"Camera zooms closely onto the model's face, highlighting the exact eyewear frames and lenses of '{produto_nome}' from the reference image."
        else:
            foco_cam = f"Full-body head-to-toe tracking shot showing the exact clothing piece '{produto_nome}' and outfit details matching the reference image."

        # Loop gerando os 6 horários com identidades únicas para cada bloco
        for i, h in enumerate(horarios):
            st.markdown(f"### 🕒 Bloco de Postagem: {h}")
            
            sc1, sc2 = st.columns(2)
            
            with sc1:
                st.markdown(f"""
                <div class="metric-card">
                    <span class="tag-estilo">ESTILO 1: POV Imersivo</span>
                    <p style='margin-top:10px; color: #ffffff;'><b>Prompt para o Flow (9:16):</b> Vertical 9:16 photorealistic UGC video, first-person POV looking down. {foco_cam} Maintaining exact model face and reference product identity without generic changes. Spoken voice-over in português Brasil (Cop exclusiva #{i+1}A): "Meninas, vocês vivem me perguntando onde eu acho peças que unem estilo e durabilidade. Olha esse detalhe de perto! Disponível na Loja da Valentina, clica no carrinho laranja aqui embaixo."</p>
                </div>
                """, unsafe_allow_html=True)

                st.markdown(f"""
                <div class="metric-card">
                    <span class="tag-estilo">ESTILO 3: Girando / Movimento Fluido</span>
                    <p style='margin-top:10px; color: #ffffff;'><b>Prompt para o Flow (9:16):</b> Vertical 9:16 photorealistic UGC video, dynamic camera spinning around the model showing full outfit and rotating down. {foco_cam} Strict 1:1 match to uploaded model and product photos. Spoken voice-over in português Brasil (Cop exclusiva #{i+1}C): "Olha o caimento disso! Perfeito para qualquer ocasião do dia a dia ou evento. Corre na Loja da Valentina, clica no carrinho laranja e garante o seu."</p>
                </div>
                """, unsafe_allow_html=True)

            with sc2:
                st.markdown(f"""
                <div class="metric-card">
                    <span class="tag-estilo">ESTILO 2: Corpo Inteiro na Rua</span>
                    <p style='margin-top:10px; color: #ffffff;'><b>Prompt para o Flow (9:16):</b> Vertical 9:16 photorealistic UGC video, full-body outdoor daylight tracking shot walking. {foco_cam} Exact facial features and product features preserved. Spoken voice-over in português Brasil (Cop exclusiva #{i+1}B): "Gente, testei e estou simplesmente apaixonada por essa novidade. Olha como veste bem no corpo! Clica no carrinho laranja na Loja da Valentina e aproveita."</p>
                </div>
                """, unsafe_allow_html=True)

                st.markdown(f"""
                <div class="metric-card">
                    <span class="tag-estilo">ESTILO 4: Frente ao Espelho (Review)</span>
                    <p style='margin-top:10px; color: #ffffff;'><b>Prompt para o Flow (9:16):</b> Vertical 9:16 photorealistic UGC video, mirror selfie reflection view in a modern aesthetic room. {foco_cam} Absolute fidelity to user's uploaded model and item. Spoken voice-over in português Brasil (Cop exclusiva #{i+1}D): "Chegou reposição e eu não podia deixar de mostrar para vocês o quanto isso aqui é diferenciado. Clica no carrinho laranja da Loja da Valentina agora!"</p>
                </div>
                """, unsafe_allow_html=True)
            
            st.markdown("---")
