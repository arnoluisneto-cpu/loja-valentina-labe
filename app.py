import streamlit as st

# Configuração da Página
st.set_page_config(
    page_title="Loja da Valentina - TikTok Shop Viral Lab",
    page_icon="💜",
    layout="wide"
)

# Estilização CSS unindo o Fundo Roxo com os Detalhes em Verde Limão Neon
st.markdown("""
    <style>
    .main {
        background-color: #0b0914;
        color: #ffffff;
    }
    .stButton>button {
        background-color: #00FF66;
        color: #000000;
        font-weight: bold;
        border-radius: 8px;
        border: none;
        padding: 12px 24px;
        font-size: 16px;
        width: 100%;
    }
    .stButton>button:hover {
        background-color: #00cc52;
        color: #ffffff;
    }
    .hero-banner {
        background: linear-gradient(135deg, #171426 0%, #1f1b36 100%);
        border: 2px solid #00FF66;
        padding: 30px;
        border-radius: 16px;
        text-align: center;
        margin-bottom: 25px;
        box-shadow: 0px 0px 20px rgba(0, 255, 102, 0.2);
    }
    .metric-card {
        background-color: #171426;
        border: 1px solid #00FF66;
        padding: 20px;
        border-radius: 12px;
        margin-bottom: 15px;
    }
    .tag-estilo {
        background-color: #00FF66;
        color: #000000;
        padding: 4px 10px;
        border-radius: 4px;
        font-weight: bold;
        font-size: 12px;
    }
    h1, h2, h3 {
        color: #00FF66 !important;
    }
    </style>
""", unsafe_allow_html=True)

# Topo: Seletores (Diretor Skin, Proporção e Estilo) idênticos à sua referência
col_top1, col_top2, col_top3 = st.columns(3)

with col_top1:
    diretor_skin = st.selectbox("⚡ Diretor Skin", ["BOY (Elite Director)", "VALENTINA MASTER"])

with col_top2:
    proporcao = st.selectbox("Proporção", ["9:16 (TikTok / Reels)", "1:1 (Feed)", "16:9 (YouTube)"])

with col_top3:
    estilo_persona = st.selectbox("Estilo de Vídeo", ["Pietra (Tendência & Lifestyle)", "UGC Fotorrealista 1:1"])

st.markdown("---")

# Banner Central "VALENTINA" com a estética roxa e contorno/destaque verde limão
st.markdown("""
    <div class="hero-banner">
        <h1 style="letter-spacing: 4px; margin-bottom: 5px; color: #00FF66;">VALENTINA</h1>
        <p style="color: #b0bec5; font-size: 14px; margin: 0;">LOJA DA VALENTINA • TIKTOK SHOP VIRAL LAB • PARÂMETROS DE VÍDEO</p>
    </div>
""", unsafe_allow_html=True)

# Layout de Entradas (Parâmetros e Uploads)
col_input1, col_input2 = st.columns(2)

with col_input1:
    st.markdown("### 🎯 Parâmetros do Produto")
    produto_nome = st.text_input("Produto / Peça Principal", placeholder="Ex: Sandália Preta Salto Bloco...")
    produto_ref = st.text_input("Link ou Código de Referência", placeholder="Ex: REF-092 ou Link do TikTok Shop")
    tipo_produto = st.selectbox("Categoria de Foco da Câmera", [
        "Calçado (Foco nos Pés / Descer Girando)", 
        "Acessório de Pulso/Mão (Relógio, Pulseira)", 
        "Acessório de Rosto (Óculos)", 
        "Vestuário / Corpo Inteiro"
    ])
    
with col_input2:
    st.markdown("### 📸 Fidelidade Absoluta (Upload Obrigatório)")
    foto_modelo = st.file_uploader("Foto de Referência da Modelo", type=["jpg", "jpeg", "png"])
    foto_peca = st.file_uploader("Foto Exata do Produto (Proibido gerar genérico)", type=["jpg", "jpeg", "png"])

st.markdown("---")

# Botão de Execução em Massa
if st.button("🚀 GERAR 6 HORÁRIOS × 4 ESTILOS (MÁQUINA EM MASSA)"):
    if not produto_nome:
        st.warning("⚠️ Por favor, informe o nome do produto principal.")
    else:
        st.success("✅ Pacote gerado com sucesso! Fidelidade 1:1 e distribuição em 6 horários aplicadas.")
        
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
            
            c1, c2 = st.columns(2)
            
            with c1:
                st.markdown(f"""
                <div class="metric-card">
                    <span class="tag-estilo">ESTILO 1: POV Imersivo</span>
                    <p style='margin-top:10px;'><b>Prompt para o Flow (9:16):</b> Vertical 9:16 photorealistic UGC video, first-person POV looking down. {foco_cam} Maintaining exact model face and reference product identity without generic changes. Spoken voice-over in português Brasil (Cop exclusiva #{i+1}A): "Meninas, vocês vivem me perguntando onde eu acho peças que unem estilo e durabilidade. Olha esse detalhe de perto! Disponível na Loja da Valentina, clica no carrinho laranja aqui embaixo."</p>
                </div>
                """, unsafe_allow_html=True)

                st.markdown(f"""
                <div class="metric-card">
                    <span class="tag-estilo">ESTILO 3: Girando / Movimento Fluido</span>
                    <p style='margin-top:10px;'><b>Prompt para o Flow (9:16):</b> Vertical 9:16 photorealistic UGC video, dynamic camera spinning around the model showing full outfit and rotating down. {foco_cam} Strict 1:1 match to uploaded model and product photos. Spoken voice-over in português Brasil (Cop exclusiva #{i+1}C): "Olha o caimento disso! Perfeito para qualquer ocasião do dia a dia ou evento. Corre na Loja da Valentina, clica no carrinho laranja e garante o seu."</p>
                </div>
                """, unsafe_allow_html=True)

            with c2:
                st.markdown(f"""
                <div class="metric-card">
                    <span class="tag-estilo">ESTILO 2: Corpo Inteiro na Rua</span>
                    <p style='margin-top:10px;'><b>Prompt para o Flow (9:16):</b> Vertical 9:16 photorealistic UGC video, full-body outdoor daylight tracking shot walking. {foco_cam} Exact facial features and product features preserved. Spoken voice-over in português Brasil (Cop exclusiva #{i+1}B): "Gente, testei e estou simplesmente apaixonada por essa novidade. Olha como veste bem no corpo! Clica no carrinho laranja na Loja da Valentina e aproveita."</p>
                </div>
                """, unsafe_allow_html=True)

                st.markdown(f"""
                <div class="metric-card">
                    <span class="tag-estilo">ESTILO 4: Frente ao Espelho (Review)</span>
                    <p style='margin-top:10px;'><b>Prompt para o Flow (9:16):</b> Vertical 9:16 photorealistic UGC video, mirror selfie reflection view in a modern aesthetic room. {foco_cam} Absolute fidelity to user's uploaded model and item. Spoken voice-over in português Brasil (Cop exclusiva #{i+1}D): "Chegou reposição e eu não podia deixar de mostrar para vocês o quanto isso aqui é diferenciado. Clica no carrinho laranja da Loja da Valentina agora!"</p>
                </div>
                """, unsafe_allow_html=True)
            
            st.markdown("---")
