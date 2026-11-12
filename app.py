import streamlit as st
import random

st.set_page_config(
    page_title="Val AI Engine - TikTok Shop Automation",
    page_icon="💜",
    layout="wide"
)

# CSS Comercial / Padrão Multinacional Gringa
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
    
    /* Banner Principal Comercial */
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
    
    /* Inputs, Selects e Dropdowns com fundo roxo escuro e borda em Verde Limão */
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

    /* Blocos de Upload */
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

# 1. TOPO COMERCIAL
st.markdown("""
    <div class="hero-banner">
        <h1 class="hero-title">VAL AI ENGINE</h1>
        <p style="color: #b0bec5; font-size: 12px; margin-top: 5px; margin-bottom: 0; letter-spacing: 2px;">MÁQUINA DE VÍDEOS EM MASSA • TIKTOK SHOP AUTOMATION</p>
    </div>
""", unsafe_allow_html=True)

# 2. SELETORES COM DESCRIÇÃO COMERCIAL DIRETA
c_top1, c_top2, c_top3 = st.columns(3)
with c_top1:
    diretor_skin = st.selectbox(
        "MOTOR DE INTELIGÊNCIA (SKIN)", 
        [
            "DIRECTOR PRO (Cinematográfico & 1:1)", 
            "UGC LIFESTYLE (Influencer & Conversão)"
        ]
    )
    if "DIRECTOR PRO" in diretor_skin:
        st.markdown("<p style='font-size: 11px; color: #00FF66; margin-top: -10px;'>💡 Foco em lentes profissionais, alta nitidez e rigidez técnica.</p>", unsafe_allow_html=True)
    else:
        st.markdown("<p style='font-size: 11px; color: #00FF66; margin-top: -10px;'>💡 Foco em conexão humana, unboxing e tom de influenciadora.</p>", unsafe_allow_html=True)

with c_top2:
    proporcao = st.selectbox("FORMATO DE VÍDEO", ["9:16 (TikTok / Reels)", "16:9 (YouTube / Wide)", "1:1 (Feed)"])
    st.markdown("<p style='font-size: 11px; color: #b0bec5; margin-top: -10px;'>💡 Otimizado para a plataforma escolhida.</p>", unsafe_allow_html=True)

with c_top3:
    estilo_persona = st.selectbox("ESTILO DE CONTEÚDO (NARRATIVA)", [
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
    st.markdown("<p style='font-size: 11px; color: #b0bec5; margin-top: -10px;'>💡 Formato viral extraído das maiores tendências.</p>", unsafe_allow_html=True)

st.markdown("---")

# 3. ENTRADAS DO PRODUTO E UPLOADS COM FOCO COMERCIAL
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

# 4. BANCO DE VARIAÇÕES HUMANIZADAS (ANTI-DETECÇÃO DE ROBÔ)
hooks_abertura = [
    "Meninas, vocês não têm noção da quantidade de mensagens perguntando sobre essa peça.",
    "Gente, eu juro que tô chocada com a qualidade disso aqui, sério.",
    "Olha, se você tava esperando um sinal para garantir o seu look novo, o sinal chegou.",
    "Vocês sabem que eu sou super chata com qualidade, mas isso aqui superou todas as expectativas.",
    "Meninas, olha esse detalhe de perto! Chegou reposição e eu tive que vir correndo mostrar.",
    "Para tudo e olha o caimento dessa peça no corpo, é surreal de perfeito."
]

ctas_fechamento = [
    "Corre para garantir o seu na Loja da Valentina, clica no carrinho laranja aqui embaixo.",
    "Tá com um preço de lançamento absurdo na Loja da Valentina, clica no carrinho laranja.",
    "Disponível agora com frete rápido na Loja da Valentina, clica no carrinho laranja aí na tela.",
    "Não perde tempo porque esgota rápido, clica no carrinho laranja na Loja da Valentina.",
    "Garante o seu direto na Loja da Valentina, clica no carrinho laranja aqui embaixo.",
    "Tudo disponível na Loja da Valentina, clica no carrinho laranja e aproveita a promoção."
]

# 5. BOTÃO DE EXECUÇÃO EM MASSA (6 Horários x 4 Estilos = 24 Vídeos Únicos)
if st.button("🚀 GERAR PACOTE COMERCIAL (6 HORÁRIOS × 4 ESTILOS = 24 VÍDEOS)"):
    if not produto_nome:
        st.warning("⚠️ Por favor, informe o nome do produto.")
    else:
        st.success("✅ Pacote comercial gerado com sucesso! 24 prompts com realismo total e ganchos anti-bloqueio aplicados.")
        
        horarios = [
            "09:00 - Manhã (Abertura de Feed)",
            "12:00 - Almoço (Pico de Engajamento)",
            "15:00 - Tarde (Pausa Comercial)",
            "18:00 - Fim de Tarde (Deslocamento)",
            "19:00 - Noite (Pico Principal de Compra)",
            "23:00 - Fechamento (Último Tiro do Dia)"
        ]
        
        base_realism = "Masterpiece, hyper-realistic 8k resolution, raw aesthetic, natural cinematic lighting, shot on 35mm lens, depth of field, zero digital artifacts, uncompromising 1:1 fidelity to reference face and product."
        
        if "Caminhão" in estilo_persona:
            foco_cam = f"Cinematic hyper-realistic shot of a heavy logistics delivery truck backing up precisely to a modern residential gate, back doors swinging open to reveal massive stacks of branded TikTok Shop boxes for '{produto_nome}'. {base_realism}"
        elif "Calçado" in tipo_produto:
            foco_cam = f"First-person POV looking down. Camera pans smoothly and organically from the model's face down to a macro close-up framing of the exact footwear '{produto_nome}' from the reference image, highlighting fine leather texture, straps, stitching, and heel structure. {base_realism}"
        elif "Pulso" in tipo_produto:
            foco_cam = f"Close-up macro tracking shot focusing precisely on the model's wrist and hand displaying the exact accessory '{produto_nome}' from the reference image, natural skin tones, sharp metallic and material definition. {base_realism}"
        elif "Óculos" in tipo_produto:
            foco_cam = f"Intimate close-up zoom onto the model's face, highlighting the precise eyewear frames, tint, and precise design of '{produto_nome}' from the reference image, natural bokeh background. {base_realism}"
        else:
            foco_cam = f"Full-body head-to-toe dynamic tracking shot showing the exact clothing piece '{produto_nome}' and outfit details matching the reference image perfectly, authentic lighting. {base_realism}"

        for i, h in enumerate(horarios):
            st.markdown(f"### 🕒 Bloco de Postagem: {h}")
            
            sc1, sc2 = st.columns(2)
            
            hook_1 = hooks_abertura[(i * 2) % len(hooks_abertura)]
            cta_1 = ctas_fechamento[(i * 2) % len(ctas_fechamento)]
            
            hook_2 = hooks_abertura[(i * 2 + 1) % len(hooks_abertura)]
            cta_2 = ctas_fechamento[(i * 2 + 1) % len(ctas_fechamento)]
            
            hook_3 = hooks_abertura[(i * 3) % len(hooks_abertura)]
            cta_3 = ctas_fechamento[(i * 3) % len(ctas_fechamento)]
            
            hook_4 = hooks_abertura[(i * 3 + 1) % len(hooks_abertura)]
            cta_4 = ctas_fechamento[(i * 3 + 1) % len(ctas_fechamento)]
            
            with sc1:
                st.markdown(f"""
                <div class="metric-card">
                    <span class="tag-estilo">ESTILO 1: {estilo_persona}</span>
                    <p style='margin-top:10px; color: #ffffff;'><b>Prompt ({proporcao}):</b> Vertical {proporcao} UGC video, professional smartphone camera style. {foco_cam} Strict preservation of original model facial structure and item details. Spoken voice-over in português Brasil (Variação #{i+1}A): "{hook_1} Olha esse detalhe de perto! {cta_1}"</p>
                </div>
                """, unsafe_allow_html=True)

                st.markdown(f"""
                <div class="metric-card">
                    <span class="tag-estilo">ESTILO 3: Giro Dinâmico 360°</span>
                    <p style='margin-top:10px; color: #ffffff;'><b>Prompt ({proporcao}):</b> Vertical {proporcao} UGC video, smooth 360-degree orbital camera rotation around the model. {foco_cam} Absolute 1:1 match to uploaded model and reference asset. Spoken voice-over in português Brasil (Variação #{i+1}C): "{hook_3} O caimento disso aqui no corpo é impecável. {cta_3}"</p>
                </div>
                """, unsafe_allow_html=True)

            with sc2:
                st.markdown(f"""
                <div class="metric-card">
                    <span class="tag-estilo">ESTILO 2: Corpo Inteiro na Rua</span>
                    <p style='margin-top:10px; color: #ffffff;'><b>Prompt ({proporcao}):</b> Vertical {proporcao} UGC video, dynamic daylight outdoor walking shot. {foco_cam} Zero facial morphing, perfect clothing fidelity. Spoken voice-over in português Brasil (Variação #{i+1}B): "{hook_2} Testei na rua e tô simplesmente apaixonada pelo resultado. {cta_2}"</p>
                </div>
                """, unsafe_allow_html=True)

                st.markdown(f"""
                <div class="metric-card">
                    <span class="tag-estilo">ESTILO 4: Frente ao Espelho (Review)</span>
                    <p style='margin-top:10px; color: #ffffff;'><b>Prompt ({proporcao}):</b> Vertical {proporcao} UGC video, authentic mirror reflection perspective in a luxury bedroom. {foco_cam} Pristine realism, zero visual distortions. Spoken voice-over in português Brasil (Variação #{i+1}D): "{hook_4} Não podia deixar de mostrar essa novidade pra vocês. {cta_4}"</p>
                </div>
                """, unsafe_allow_html=True)
            
            st.markdown("---")
