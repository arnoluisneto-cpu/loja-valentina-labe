
import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="Valentina Labs - TikTok Shop Automation",
    page_icon="💜",
    layout="wide"
)

# ESTÉTICA DE ALTO LUXO (Fundo Escuro Puro, Padrão Verde Neon)
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
        width: 100% !important;
    }
    .stButton>button:hover, div[data-testid="stFileUploader"] button:hover {
        background-color: #00cc52 !important;
        color: #ffffff !important;
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
    }
    
    .stTextInput input, .stSelectbox select { color: #ffffff !important; }
    div[data-baseweb="select"] span { color: #ffffff !important; }
    div[data-baseweb="select"] svg { fill: #00FF66 !important; }
    
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
    div[data-testid="stFileUploader"] section { background-color: #161026 !important; }
    div[data-testid="stFileUploader"] span, div[data-testid="stFileUploader"] small, div[data-testid="stFileUploader"] p {
        color: #ffffff !important;
    }
    
    ::placeholder { color: #b0bec5 !important; opacity: 1 !important; }
    
    .metric-card {
        background-color: #161026 !important;
        border: 1.5px solid #8A2BE2 !important;
        padding: 18px;
        border-radius: 12px;
        margin-bottom: 15px;
        box-shadow: 0px 4px 15px rgba(138, 43, 226, 0.2);
        height: 100%;
    }
    
    .tag-estilo {
        background-color: #00FF66 !important;
        color: #000000 !important;
        padding: 4px 10px;
        border-radius: 6px;
        font-weight: bold;
        font-size: 13px;
        display: inline-block;
        margin-bottom: 10px;
    }
    
    h1, h2, h3, label, .stMarkdown {
        color: #ffffff !important;
        font-family: 'Inter', sans-serif !important;
    }
    </style>
""", unsafe_allow_html=True)

# 1. TOPO DA APLICAÇÃO
st.markdown("""
    <div class="hero-banner">
        <h1 class="hero-title">VALENTINA LABS</h1>
        <p style="color: #b0bec5; font-size: 12px; margin-top: 5px; margin-bottom: 0; letter-spacing: 2px;">LOJA DA VALENTINA • TIKTOK SHOP AUTOMATION (21 PROMPTS UNIFORM QUALITY)</p>
    </div>
""", unsafe_allow_html=True)

# 2. SELETORES
c_top1, c_top2, c_top3 = st.columns(3)
with c_top1:
    diretor_skin = st.selectbox("DIRETOR SKIN", ["BOY (Elite Director)", "UGC LIFESTYLE (Influencer & Conversão)"])
with c_top2:
    proporcao = st.selectbox("PROPORÇÃO", ["9:16 (TikTok / Reels)", "1:1 (Feed)", "16:9 (Wide)"])
with c_top3:
    estilo_persona = st.selectbox("ESTILO DE VÍDEO (CONTEXTO)", [
        "1. Caminhão e Van do TikTok Shop Chegando",
        "2. POV Acordando na Cama (Morning Routine)",
        "3. POV Arrumando o Closet / Selecionando Peças",
        "4. POV Imersivo (Olhando para Baixo nos Pés)",
        "5. Corpo Inteiro na Rua (Caminhando no Calçadão)",
        "6. Frente ao Espelho (Mirror Selfie)",
        "7. Giro Dinâmico 360° (Mostrando Caimento)",
        "8. Close Macro Cirúrgico (Detalhes e Textura)",
        "9. Unboxing Surpresa em Cima da Mesa",
        "10. Transição Rápida de Looks",
        "11. Vlog de Rotina Diária Estilo Lifestyle",
        "12. Review Sincero Boca a Boca",
        "13. Provador Rápido de Loja Física",
        "14. Trend do Sofá / Almofada",
        "15. POV Dirigindo o Carro",
        "16. POV Café da Manhã na Mesa Posta",
        "17. Challenge de Transição: Look Casual para Luxo",
        "18. Unboxing Rasgando Pacote do TikTok Shop",
        "19. POV Fitness / Rotação de Estilo Diário",
        "20. POV Encontro Noturno / Night Out Look Reveal"
    ])

st.markdown("---")

# 3. ENTRADAS DO PRODUTO (3 UPLOADS EM VERDE NEON)
col_input1, col_input2 = st.columns(2)

with col_input1:
    produto_nome = st.text_input("NOME EXATO DO PRODUTO / SKU", placeholder="Ex: Sandália Salto Bloco GIGIL")
    
    st.markdown("<p style='font-size:13px; font-weight:700; margin-bottom:4px;'>DESCRIÇÃO DO PRODUTO - UPLOAD FOTO</p>", unsafe_allow_html=True)
    foto_produto_analise = st.file_uploader("Upload Foto Produto", type=["jpg", "jpeg", "png"], key="prod_upload_original", label_visibility="collapsed")

    tipo_produto = st.selectbox("CATEGORIA", [
        "Calçado / Tênis / Sandália", 
        "Acessório de Pulso ou Rosto (Relógio / Óculos)", 
        "Vestuário / Vestido / Conjunto",
        "Bolsa / Acessório de Mão",
        "Utilidades & Outros"
    ])
    
with col_input2:
    st.markdown("<p style='font-size:13px; font-weight:700; margin-bottom:4px;'>1. FOTO MODELO (FACE & CORPO INTEIRO 1:1)</p>", unsafe_allow_html=True)
    foto_modelo = st.file_uploader("Upload Modelo", type=["jpg", "jpeg", "png"], key="m", label_visibility="collapsed")
    
    st.markdown("<p style='font-size:13px; font-weight:700; margin-top:10px; margin-bottom:4px;'>2. FOTO REFERÊNCIA PEÇA (CLONAGEM 1:1)</p>", unsafe_allow_html=True)
    foto_peca = st.file_uploader("Upload Produto", type=["jpg", "jpeg", "png"], key="p", label_visibility="collapsed")

st.markdown("---")

# 4. BANCO EXPANDIDO COM 21 ROTEIROS ÚNICOS (RITMO CALMO + GANCHO FORTE + CTA VALENTINA / CARRINHO LARANJA)
roteiros_21 = [
    "Amiga, para tudo e me escuta... você não tem noção do que acabou de chegar para mim. Exatamente como eu queria... corre lá na Loja da Valentina e clica no carrinho laranja aqui embaixo.",
    "Gente, sério... eu precisava gravar bem calma para vocês verem isso aqui. É surreal de perfeito... está com preço de lançamento na Loja da Valentina, clica no carrinho laranja aí embaixo.",
    "Olha... se você estava na dúvida se valia a pena, presta atenção nisso. Veio idêntico ao anúncio, acabamento impecável... já está disponível na Loja da Valentina, corre e clica no carrinho laranja.",
    "Meninas... vocês me pediram tanto esse modelo exato, e ele chegou superando todas as expectativas. Perfeito demais... garante o seu na Loja da Valentina clicando no carrinho laranja.",
    "Olha isso aqui... reposição oficial que vocês tanto queriam, chegou fresquinho para compor os melhores looks. Maravilhoso... corre para garantir direto na Loja da Valentina, clica no carrinho laranja.",
    "Para tudo e olha a fidelidade absoluta desse produto... sério, impecável em cada detalhe. Vale muito a pena... tudo disponível na Loja da Valentina, clica no carrinho laranja e aproveita.",
    "Meninas do céu, vocês não têm noção da lindeza disso aqui... chegou super rápido e idêntico à foto! Garante o seu na Loja da Valentina clicando no carrinho laranja aqui embaixo.",
    "Olha esse acabamento, sério... é o tipo de peça que todo mundo elogia na rua. Corre para aproveitar na Loja da Valentina, clica no carrinho laranja aí na tela.",
    "Gente, eu estava ansiosa demais para esse pacote chegar... e superou tudo! Perfeito para o dia a dia. Já vai direto na Loja da Valentina e clica no carrinho laranja.",
    "Para quem ama exclusividade e conforto, achou o produto certo. Chegou impecável... corre lá na Loja da Valentina e clica no carrinho laranja aqui embaixo.",
    "Amiga, se você quer acertar em cheio no look, é isso aqui que você precisa. Qualidade surreal... tudo na Loja da Valentina, clica no carrinho laranja.",
    "Olha a perfeição desse detalhe, sério, fiquei sem palavras... reposição limitadíssima na Loja da Valentina, clica no carrinho laranja e garante o seu.",
    "Meninas, chegou o queridinho do momento... exatamente como a gente pediu! Não perde tempo, corre na Loja da Valentina e clica no carrinho laranja.",
    "Gente, eu testei e aprovei de verdade. Qualidade impecável de verdade... disponível agora na Loja da Valentina, clica no carrinho laranja aí embaixo.",
    "Olha esse caimento, olha essa cor... simplesmente apaixonada! Corre para garantir o seu direto na Loja da Valentina, clica no carrinho laranja.",
    "Vocês me mandaram mensagem o dia todo perguntando sobre isso... chegou perfeito! Garante o teu na Loja da Valentina clicando no carrinho laranja.",
    "Amiga, sério, esse aqui é daquele modelo que esgota em minutos... corre para ver na Loja da Valentina, clica no carrinho laranja aqui embaixo.",
    "Olha a embalagem, olha o cuidado... e o produto é melhor ainda ao vivo! Tudo na Loja da Valentina, clica no carrinho laranja e aproveita.",
    "Meninas, fevirei fã número um desse modelo... veio exato como na foto! Corre lá na Loja da Valentina e clica no carrinho laranja.",
    "Gente, preço justo e qualidade de shopping... achei o achado do mês! Disponível na Loja da Valentina, clica no carrinho laranja aí na tela.",
    "Para fechar o dia com chave de ouro, olha o que chegou para mim... perfeito demais! Garante o seu na Loja da Valentina clicando no carrinho laranja."
]

# 5. GERADOR UNIFORME PARA OS 21 PROMPTS
if st.button("🚀 GERAR PACOTE COMPLETO (21 PROMPTS PADRÃO MÁXIMO)"):
    if not produto_nome:
        st.warning("⚠️ Por favor, informe o nome exato do produto.")
    elif not foto_peca or not foto_modelo or not foto_produto_analise:
        st.warning("⚠️ Por favor, faça o upload da FOTO DA MODELO, da FOTO DO PRODUTO e da foto na descrição para ativar a precisão máxima.")
    else:
        agora = datetime.now().strftime("%H:%M:%S")
        st.success(f"✅ Pacote de 21 Prompts gerado às {agora} | Estilo Ativo: [{estilo_persona}] | Qualidade Uniforme Máxima Ativa.")
        
        # LOOP RIGOROSO PARA OS 21 PROMPTS COM QUALIDADE IDÊNTICA DO 1 AO 21
        for idx in range(21):
            roteiro_atual = roteiros_21[idx % len(roteiros_21)]
            prompt_numero = idx + 1

            prompt_final = (
                f"Photorealistic 4K UGC video (13.5s duration, {proporcao.split()[0]}), mobile sensor. ACTIVE STYLE: {estilo_persona}. "
                f"Strict 1:1 pixel lock: identical reference model face and body proportions. "
                f"Rigid product lock: exact '{produto_nome}' matching reference image with zero substitution. "
                f"MAGNETIC HOOK START (0-2s): The video opens immediately with the creator looking straight into the camera, head slightly tilted, delivering a strong, engaging verbal hook with a calm, conversational, natural human tone. "
                f"CALM & FLUID MOVEMENT (2-13s): The creator moves slowly, calmly, and unhurriedly. Hands pick up '{produto_nome}' from a soft luxury bed surface with natural physical weight. The pacing is relaxed and confident, with zero rushing. "
                f"IMMEDIATE FLUID START & CLEAN SCREEN: Absolute zero static frames, zero ghosting, zero overlay transparency, zero floating text, zero subtitles, zero UI overlays, zero watermarks. "
                f"SMOOTH TAIL BUFFER: Action and speech gently taper off towards the final seconds, allowing a natural, unhurried conclusion with zero abrupt audio cuts. "
                f"Fixed static background, organic human movement.\n\n"
                f"LOCUÇÃO (Ritmo calmo, natural e persuasivo): \"{roteiro_atual}\"\n\n"
                f"Negative Prompt: rushed speech, fast jerky movement, static starting frame, ghosting effect, transparent overlay, floating text, subtitles, UI graphics, watermarks, abrupt appearance, pop-up object, harsh audio cut, model swapping, face morphing, background shift, CGI."
            )

            st.markdown(f"### 🎬 Prompt Comercial #{prompt_numero} de 21")
            
            st.markdown(
                '<div class="metric-card">'
                f'<span class="tag-estilo">Take Único #{prompt_numero} (13.5s) - Padrão Rigoroso Valentina Labs</span><br>',
                unsafe_allow_html=True
            )
            
            st.code(prompt_final, language="text")
                
            st.markdown('</div>', unsafe_allow_html=True)
            st.markdown("---")
