import streamlit as st

st.set_page_config(
    page_title="Loja da Valentina - TikTok Shop",
    page_icon="💜",
    layout="wide"
)

# CSS Definitivo para zerar o branco em setas/dropdowns e padronizar o Verde Limão Neon
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;900&display=swap');
    
    .stApp, .main, div[data-testid="stVerticalBlock"] {
        background-color: #0b0914 !important;
        color: #ffffff !important;
        font-family: 'Inter', sans-serif !important;
    }
    
    /* Botões Principais e de Upload em Verde Limão Neon com Texto Preto */
    .stButton>button, div[data-testid="stFileUploader"] button {
        background-color: #00FF66 !important;
        color: #000000 !important;
        font-weight: 700 !important;
        border-radius: 8px !important;
        border: none !important;
        padding: 10px 20px !important;
        font-size: 15px !important;
    }
    .stButton>button:hover, div[data-testid="stFileUploader"] button:hover {
        background-color: #00cc52 !important;
        color: #ffffff !important;
    }
    .stButton>button {
        width: 100% !important;
    }
    
    /* Banner Principal Valentina */
    .hero-banner {
        background: linear-gradient(135deg, #161026 0%, #22153b 100%);
        border: 2px solid #8A2BE2;
        padding: 16px;
        border-radius: 12px;
        text-align: center;
        margin-bottom: 15px;
        box-shadow: 0px 0px 20px rgba(138, 43, 226, 0.3);
    }
    .hero-title {
        font-size: 32px;
        font-weight: 900;
        letter-spacing: 5px;
        color: #00FF66 !important;
        text-shadow: 0 0 10px rgba(0, 255, 102, 0.4);
        margin: 0;
    }
    
    /* Inputs, Selects e Setas em Verde Limão Neon */
    input, select, textarea, div[data-baseweb="select"] > div {
        background-color: #161026 !important;
        color: #ffffff !important;
        border: 1px solid #00FF66 !important;
        border-radius: 8px !important;
        font-family: 'Inter', sans-serif !important;
    }
    
    .stTextInput>div>div>input, .stSelectbox>div>div>select {
        background-color: #161026 !important;
        color: #ffffff !important;
        border: 1px solid #00FF66 !important;
        border-radius: 8px !important;
    }
    
    /* Forçar setas e ícones dos dropdowns em Verde Limão */
    div[data-baseweb="select"] svg {
        fill: #00FF66 !important;
    }
    
    div[data-baseweb="popover"], div[data-baseweb="menu"], ul[data-baseweb="menu"] {
        background-color: #161026 !important;
        color: #ffffff !important;
    }

    /* Blocos de Upload com Fundo Escuro e Borda Verde Limão */
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
    
    /* Cartões de Resultados */
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

# 1. VALENTINA NO TOPO
st.markdown("""
    <div class="hero-banner">
        <h1 class="hero-title">VALENTINA</h1>
        <p style="color: #b0bec5; font-size: 11px; margin-top: 3px; margin-bottom: 0; letter-spacing: 1px;">LOJA DA VALENTINA • TIKTOK SHOP</p>
    </div>
""", unsafe_allow_html=True)

# 2. SELETORES NO TOPO COM SETAS E BORDAS EM VERDE LIMÃO
c_top1, c_top2, c_top3 = st.columns(3)
with c_top1:
    diretor_skin = st.selectbox("DIRETOR SKIN", ["BOY (Elite Director)", "VALENTINA MASTER"])
with c_top2:
    proporcao = st.selectbox("PROPORÇÃO", ["9:16 (TikTok / Reels)", "16:9 (YouTube / Wide)", "1:1 (Feed)"])
with c_top3:
    estilo_persona = st.selectbox("ESTILO DE VÍDEO (PENTE-FINO TIKTOK)", [
        "1. POV Acordando na Cama (Morning Routine com o Produto)",
        "2. POV Arrumando o Closet / Selecionando Peças",
        "3. POV Imersivo (Olhando para Baixo nos Pés / Calçado)",
        "4. Corpo Inteiro na Rua (Caminhando no Calçadão com Tráfego)",
        "5. Frente ao Espelho (Mirror Selfie com Transição Secundária)",
        "6. Giro Dinâmico 360° (Mostrando Caimento e Balanço do Tecido)",
        "7. Close Macro Cirúrgico (Foco Total em Costura e Detalhes)",
        "8. Unboxing Surpresa em Cima da Mesa com Ring Light",
        "9. Transição Rápida de Looks (Trend de Troca Instantânea)",
        "10. Vlog de Rotina Diária Estilo Lifestyle (Dia a Dia Corrido)",
        "11. Review Sincero Boca a Boca (Falando Bem de Perto com a Câmera)",
        "12. Provador Rápido de Loja Física (Provando na Frente do Espelho da Loja)",
        "13. Trend do Sofá / Almofada (Apresentação Casual Relaxada)",
        "14. POV Dirigindo o Carro (Mostrando Acessório no Volante/Pulso)",
        "15. POV Café da Manhã na Mesa Posta (Estilo Blogueira Chique)",
        "16. Challenge de Transição: Roupa Simples para Look Completo de Luxo",
        "17. Unboxing Rasgando Pacote do TikTok Shop de Surpresa",
        "18. POV Saindo da Academia / Fitness Check com Estilo",
        "19. Provador em Duas Cores (Mostrando Qual Cor Escolher)",
        "20. "POV Encontro Noturno / Night Out Look Reveal"
    ])

st.markdown("---")

# 3. ENTRADAS DO PRODUTO E UPLOADS COM DESTAQUE VERDE LIMÃO
col_input1, col_input2 = st.columns(2)

with col_input1:
    produto_nome = st.text_input("PRODUTO", placeholder="Ex: Sandália Preta Salto Bloco")
    produto_ref = st.text_input("LINK OU CÓDIGO DE REFERÊNCIA", placeholder="Ex: REF-092 ou Link TikTok Shop")
    tipo_produto = st.selectbox("CATEGORIA", [
        "Calçado (Foco nos Pés / Descer Girando)", 
        "Acessório de Pulso (Relógio / Pulseira)", 
        "Acessório de Rosto (Óculos)", 
        "Vestuário / Vestido de Festa",
        "Conjunto Pantalona / Casual",
        "Bolsa / Acessório de Mão",
        "Utilidades & Casa"
    ])
    
with col_input2:
    st.markdown("<p style='font-size:14px; font-weight:600; margin-bottom:5px; color:#ffffff;'>FOTO MODELO</p>", unsafe_allow_html=True)
    foto_modelo = st.file_uploader("Upload Modelo", type=["jpg", "jpeg", "png"], key="m", label_visibility="collapsed")
    
    st.markdown("<p style='font-size:14px; font-weight:600; margin-top:10px; margin-bottom:5px; color:#ffffff;'>FOTO PRODUTO</p>", unsafe_allow_html=True)
    foto_peca = st.file_uploader("Upload Produto", type=["jpg", "jpeg", "png"], key="p", label_visibility="collapsed")

st.markdown("---")

# 4. BOTÃO DE EXECUÇÃO EM MASSA (6 Horários x 4 Estilos)
if st.button("🚀 GERAR 6 HORÁRIOS × 4 ESTILOS (MÁQUINA EM MASSA)"):
    if not produto_nome:
        st.warning("⚠️ Por favor, informe o nome do produto.")
    else:
        st.success("✅ Pacote gerado com sucesso! Grade de 6 horários e fidelidade 1:1 aplicadas.")
        
        horarios = [
            "09:00 - Manhã (Abertura de Feed)",
            "12:00 - Almoço (Pico de Engajamento)",
            "15:00 - Tarde (Pausa Comercial)",
            "18:00 - Fim de Tarde (Deslocamento)",
            "19:00 - Noite (Pico Principal de Compra)",
            "23:00 - Fechamento (Último Tiro do Dia)"
        ]
        
        if "Calçado" in tipo_produto:
            foco_cam = f"Camera pans smoothly down from the model's face to a macro close-up of the exact footwear '{produto_nome}' from the uploaded reference image, showing precise texture, straps, and heel. Strict 1:1 product match."
        elif "Pulso" in tipo_produto:
            foco_cam = f"Camera focuses precisely on the model's wrist and hand displaying the exact accessory '{produto_nome}' from the reference image, smooth macro tracking shot."
        elif "Óculos" in tipo_produto:
            foco_cam = f"Camera zooms closely onto the model's face, highlighting the exact eyewear frames and lenses of '{produto_nome}' from the reference image."
        else:
            foco_cam = f"Full-body head-to-toe tracking shot showing the exact clothing piece '{produto_nome}' and outfit details matching the reference image."

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
