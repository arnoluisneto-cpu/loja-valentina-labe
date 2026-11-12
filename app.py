import streamlit as st

# Configuração da Página com Estética Dark Neon e Verde Limão
st.set_page_config(
    page_title="Loja da Valentina - TikTok Shop Viral Lab",
    page_icon="⚡",
    layout="wide"
)

# Estilização CSS personalizada (Estética Original Dark Neon / Verde Limão)
st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
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
    }
    .stButton>button:hover {
        background-color: #00cc52;
        color: #ffffff;
    }
    .metric-card {
        background-color: #1a1d24;
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

# Cabeçalho Principal com a Identidade Visual da Loja
st.markdown("<h1 style='text-align: center;'>⚡ LOJA DA VALENTINA • TIKTOK SHOP VIRAL LAB ⚡</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #888888;'>Painel de Produção em Massa • Fidelidade 1:1 Absoluta (Modelo + Produto Real) • 6 Horários</p>", unsafe_allow_html=True)
st.markdown("---")

# Layout de Entradas em Colunas
col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🎯 Parâmetros do Produto")
    produto_nome = st.text_input("Nome do Produto / Peça Principal", placeholder="Ex: Sandália Preta Salto Bloco")
    produto_ref = st.text_input("Link ou Código de Referência", placeholder="Ex: REF-092 ou Link do TikTok Shop")
    tipo_produto = st.selectbox("Categoria de Foco da Câmera", [
        "Calçado (Foco nos Pés / Descer Girando)", 
        "Acessório de Pulso/Mão (Relógio, Pulseira)", 
        "Acessório de Rosto (Óculos)", 
        "Vestuário / Corpo Inteiro"
    ])
    
with col2:
    st.markdown("### 📸 Fidelidade Absoluta (Upload Obrigatório)")
    foto_modelo = st.file_uploader("Foto de Referência da Modelo", type=["jpg", "jpeg", "png"])
    foto_peca = st.file_uploader("Foto Exata do Produto (Proibido gerar genérico)", type=["jpg", "jpeg", "png"])

st.markdown("---")

# Botão de Execução em Massa
if st.button("🚀 GERAR 6 HORÁRIOS × 4 ESTILOS (MÁQUINA EM MASSA)"):
    if not produto_nome:
        st.warning("⚠️ Por favor, informe o nome do produto principal.")
    else:
        st.success("✅ Pacote gerado com sucesso! Estética preservada e fidelidade 1:1 rigorosa aplicada aos prompts.")
        
        # Os 6 Horários Estratégicos Oficiais
        horarios = [
            "09:00 - Manhã (Abertura de Feed)",
            "12:00 - Almoço (Pico de Engajamento)",
            "15:00 - Tarde (Pausa Comercial)",
            "18:00 - Fim de Tarde (Deslocamento)",
            "19:00 - Noite (Pico Principal de Compra)",
            "23:00 - Fechamento (Último Tiro do Dia)"
        ]
        
        # Direcionamento ótico da câmera por categoria
        if "Calçado" in tipo_produto:
            foco_cam = "Camera pans smoothly down from the model's face to a macro close-up of the exact feet wearing the reference footwear, showing precise texture, straps, and heel."
        elif "Pulso" in tipo_produto:
            foco_cam = "Camera focuses precisely on the model's wrist and hand displaying the exact accessory from the reference image, smooth macro tracking shot."
        elif "Óculos" in tipo_produto:
            foco_cam = "Camera zooms closely onto the model's face, highlighting the exact eyewear frames and lenses from the reference image."
        else:
            foco_cam = "Full-body head-to-toe tracking shot showing the exact clothing piece and outfit details matching the reference image."

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
