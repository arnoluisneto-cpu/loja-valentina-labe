import streamlit as st

# Configuração da Página
st.set_page_config(
    page_title="Loja da Valentina - TikTok Shop",
    page_icon="💜",
    layout="wide"
)

# Estilização CSS personalizada (Estética Roxa Nubank + Verde Limão Neon + Campos Compactos e Limpos)
st.markdown("""
    <style>
    .stApp {
        background-color: #0b0914 !important;
        color: #ffffff !important;
    }
    .main {
        background-color: #0b0914 !important;
    }
    
    /* Botão Principal em Verde Limão Neon */
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
    
    /* Banner Principal Valentina Estilo Nubank com Sombra Neon */
    .hero-banner {
        background: linear-gradient(135deg, #161026 0%, #22153b 100%);
        border: 2px solid #8A2BE2;
        padding: 18px;
        border-radius: 14px;
        text-align: center;
        margin-bottom: 20px;
        box-shadow: 0px 0px 20px rgba(138, 43, 226, 0.3);
    }
    .hero-title {
        font-size: 34px;
        font-weight: 900;
        letter-spacing: 6px;
        color: #00FF66 !important;
        text-shadow: 0 0 12px rgba(0, 255, 102, 0.5);
        margin: 0;
    }
    
    /* Blocos de Upload Compactos com Borda Verde Limão */
    div[data-testid="stFileUploader"] {
        border: 1px solid #00FF66 !important;
        border-radius: 10px !important;
        padding: 8px !important;
        background-color: #161026 !important;
    }
    
    /* Cartões de Resultados */
    .metric-card {
        background-color: #161026 !important;
        border: 1px solid #8A2BE2 !important;
        padding: 16px;
        border-radius: 10px;
        margin-bottom: 15px;
    }
    
    /* Tags de Estilo */
    .tag-estilo {
        background-color: #00FF66 !important;
        color: #000000 !important;
        padding: 3px 8px;
        border-radius: 4px;
        font-weight: bold;
        font-size: 12px;
    }
    
    /* Textos, Labels e Inputs legíveis com placeholders claros */
    h1, h2, h3, label, .stMarkdown {
        color: #ffffff !important;
    }
    
    .stTextInput>div>div>input, .stSelectbox>div>div>select {
        background-color: #161026 !important;
        color: #ffffff !important;
        border: 1px solid #8A2BE2 !important;
        border-radius: 8px !important;
    }
    
    input, select, textarea {
        color: #ffffff !important;
    }
    
    /* Forçar cor clara para os placeholders de exemplo */
    ::placeholder {
        color: #a0a0a0 !important;
        opacity: 1 !important;
    }
    </style>
""", unsafe_allow_html=True)

# 1. BANNER PRINCIPAL DA VALENTINA NO TOPO
st.markdown("""
    <div class="hero-banner">
        <h1 class="hero-title">VALENTINA</h1>
        <p style="color: #b0bec5; font-size: 12px; margin-top: 4px; margin-bottom: 0; letter-spacing: 1px;">LOJA DA VALENTINA • TIKTOK SHOP</p>
    </div>
""", unsafe_allow_html=True)

# 2. SELETORES COMPACTOS ABAIXO (Skin, Proporção, Estilo com 10+ opções)
c_top1, c_top2, c_top3 = st.columns(3)
with c_top1:
    diretor_skin = st.selectbox("Diretor Skin", ["BOY (Elite Director)", "VALENTINA MASTER"])
with c_top2:
    proporcao = st.selectbox("Proporção", ["9:16 (TikTok / Reels)", "16:9 (YouTube / Wide)", "1:1 (Feed)"])
with c_top3:
    estilo_persona = st.selectbox("Estilo de Vídeo", [
        "1. POV Imersivo (Olhando para Baixo)",
        "2. Corpo Inteiro na Rua (Caminhando)",
        "3. Frente ao Espelho (Mirror Selfie)",
        "4. Giro Dinâmico 360° (Mostrando Look)",
        "5. Close Macro Cirúrgico (Foco no Detalhe)",
        "6. Provador de Loja (Review Rápido)",
        "7. Unboxing & Revelação de Surpresa",
        "8. Transição Rápida de Looks (Trend)",
        "9. Rotina do Dia a Dia (Lifestyle)",
        "10. Review Sincero (Boca a Boca)"
    ])

st.markdown("---")

# 3. ENTRADAS COMPACTAS E ORGANIZADAS EM DUAS COLUNAS
col_input1, col_input2 = st.columns(2)

with col_input1:
    produto_nome = st.text_input("Produto", placeholder="Ex: Sandália Preta Salto Bloco")
    produto_ref = st.text_input("Link ou Código de Referência", placeholder="Ex: REF-092 ou Link TikTok Shop")
    tipo_produto = st.selectbox("Categoria", [
        "Calçado (Foco nos Pés / Descer Girando)", 
        "Acessório de Pulso (Relógio / Pulseira)", 
        "Acessório de Rosto (Óculos)", 
        "Vestuário / Vestido de Festa",
        "Conjunto Pantalona / Casual",
        "Bolsa / Acessório de Mão",
        "Utilidades & Casa"
    ])
    
with col_input2:
    foto_modelo = st.file_uploader("Foto Modelo", type=["jpg", "jpeg", "png"])
    foto_peca = st.file_uploader("Foto Produto", type=["jpg", "jpeg", "png"])

st.markdown("---")

# 4. BOTÃO DE EXECUÇÃO EM MASSA (6 Horários x 4 Estilos)
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
                    <span class="tag-estilo">ESTILO 1: {estilo_persona}</span>
                    <p style='margin-top:10px; color: #ffffff;'><b>Prompt para o Flow ({proporcao}):</b> Vertical {proporcao} photorealistic UGC video, first-person POV looking down. {foco_cam} Maintaining exact model face and reference product identity without generic changes. Spoken voice-over in português Brasil (Cop exclusiva #{i+1}A): "Meninas, vocês vivem me perguntando onde eu acho peças que unem estilo e durabilidade. Olha esse detalhe de perto! Disponível na Loja da Valentina, clica no carrinho laranja aqui embaixo."</p>
                </div>
                """, unsafe_allow_html=True)

                st.markdown(f"""
                <div class="metric-card">
                    <span class="tag-estilo">ESTILO 3: Giro Dinâmico 360°</span>
                    <p style='margin-top:10px; color: #ffffff;'><b>Prompt para o Flow ({proporcao}):</b> Vertical {proporcao} photorealistic UGC video, dynamic camera spinning around the model showing full outfit and rotating down. {foco_cam} Strict 1:1 match to uploaded model and product photos. Spoken voice-over in português Brasil (Cop exclusiva #{i+1}C): "Olha o caimento disso! Perfeito para qualquer ocasião do dia a dia ou evento. Corre na Loja da Valentina, clica no carrinho laranja e garante o seu."</p>
                </div>
                """, unsafe_allow_html=True)

            with sc2:
                st.markdown(f"""
                <div class="metric-card">
                    <span class="tag-estilo">ESTILO 2: Corpo Inteiro na Rua</span>
                    <p style='margin-top:10px; color: #ffffff;'><b>Prompt para o Flow ({proporcao}):</b> Vertical {proporcao} photorealistic UGC video, full-body outdoor daylight tracking shot walking. {foco_cam} Exact facial features and product features preserved. Spoken voice-over in português Brasil (Cop exclusiva #{i+1}B): "Gente, testei e estou simplesmente apaixonada por essa novidade. Olha como veste bem no corpo! Clica no carrinho laranja na Loja da Valentina e aproveita."</p>
                </div>
                """, unsafe_allow_html=True)

                st.markdown(f"""
                <div class="metric-card">
                    <span class="tag-estilo">ESTILO 4: Frente ao Espelho (Review)</span>
                    <p style='margin-top:10px; color: #ffffff;'><b>Prompt para o Flow ({proporcao}):</b> Vertical {proporcao} photorealistic UGC video, mirror selfie reflection view in a modern aesthetic room. {foco_cam} Absolute fidelity to user's uploaded model and item. Spoken voice-over in português Brasil (Cop exclusiva #{i+1}D): "Chegou reposição e eu não podia deixar de mostrar para vocês o quanto isso aqui é diferenciado. Clica no carrinho laranja da Loja da Valentina agora!"</p>
                </div>
                """, unsafe_allow_html=True)
            
            st.markdown("---")
