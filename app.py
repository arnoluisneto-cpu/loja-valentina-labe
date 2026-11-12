import streamlit as st

st.set_page_config(
    page_title="Loja da Valentina - TikTok Shop Viral Lab",
    page_icon="",
    layout="wide"
)

# Estilização visual Dark/Luxury com campos compactos e legíveis
st.markdown("""
    <style>
    /* Fundo geral escuro e elegante */
    .stApp {
        background-color: #0b0b0b;
        color: #ffffff;
    }
    /* Textos nítidos */
    h1, h2, h3, h4, h5, h6, p, span, label {
        color: #ffffff !important;
    }
    /* Barra lateral */
    [data-testid="stSidebar"] {
        background-color: #141416;
        border-right: 1px solid #26262a;
    }
    [data-testid="stSidebar"] label, [data-testid="stSidebar"] span {
        color: #f5f5f7 !important;
    }
    /* Botões elegantes e menores */
    .stButton>button {
        background: linear-gradient(135deg, #d4af37 0%, #aa771c 100%);
        color: white;
        border: none;
        border-radius: 6px;
        font-weight: 600;
        padding: 0.4rem 1rem;
        font-size: 14px;
        box-shadow: 0 4px 10px rgba(212, 175, 55, 0.2);
    }
    .stButton>button:hover {
        background: linear-gradient(135deg, #e5c158 0%, #bb882d 100%);
    }
    /* Caixas de texto e inputs compactos (não ficam grandões) */
    .stTextInput>div>div>input, .stTextArea>div>div>textarea {
        background-color: #161618 !important;
        color: #ffffff !important;
        border: 1px solid #2c2c30 !important;
        border-radius: 6px;
        padding: 6px 10px !important;
        font-size: 14px !important;
    }
    /* Ajuste de altura para inputs de texto ficarem discretos */
    div[data-baseweb="input"] {
        min-height: 36px !important;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🛍️ Loja da Valentina - TikTok Shop Viral Lab")
st.markdown("### Engenharia de Prompts & Gerador de Roteiros UGC (Padrão Elite)")

with st.sidebar:
    st.header("Configuração do Skin")
    skin_mode = st.selectbox("Selecione o Perfil Diretor", ["Boy (Universal Director)", "Pietra (Luxury ASMR)", "Virgínia Routine"])
    st.markdown("---")
    st.info("CTA Fixada: Loja da Valentina & Carrinho Laranja.")

tab1, tab2 = st.tabs(["🎬 Gerador de Roteiro & Prompt", "📊 Gestão de Vitrine"])

with tab1:
    st.subheader("Parâmetros do Vídeo 9:16")
    
    col_ref1, col_ref2 = st.columns(2)
    with col_ref1:
        img_modelo = st.file_uploader("Foto de Referência da Modelo (Face/Corpo)", type=["png", "jpg", "jpeg"])
        roupa = st.text_input("Peça de Roupa / Parte de cima ou Baixo", placeholder="Ex: Calça Pantalona Alfaiataria...")
        calcado = st.text_input("Calçado no Pé da Modelo", placeholder="Ex: Sandália Preta de Salto Baixo")
        
    with col_ref2:
        img_look = st.file_uploader("Foto de Referência do Look / Peça", type=["png", "jpg", "jpeg"])
        acessorio = st.text_input("Acessório em Destaque", placeholder="Ex: Relógio dourado minimalista...")
        beneficio = st.text_input("Principal Benefício / Argumento de Venda", placeholder="Ex: Não marca, tecido fresco...")

    if st.button("Gerar Roteiro e Prompts (PT-BR + EN)"):
        st.success("Roteiro estruturado com sucesso no padrão Loja da Valentina!")
        
        st.markdown("### 📝 Roteiro Falado (Português Brasil)")
        st.markdown("""
        * **Take 1 (0-3s):** "Gente, olha esse look que acabou de chegar na Loja da Valentina!"
        * **Take 2 (3-6s):** "O caimento é surreal de perfeito, não marca nada e super confortável."
        * **Take 3 (6-9s):** "Perfeito para qualquer ocasião, do casual ao elegante."
        * **Take 4 (9-12s):** "Corre para garantir o seu, clica no carrinho laranja aqui embaixo na nossa loja!"
        """)

with tab2:
    st.subheader("Controle de Produtos de Alta Conversão")
    st.markdown("Produtos ativos na vitrine principal:")
    st.metric(label="Sandálias Nude / Preto", value="Alta Conversão", delta="Viral TikTok Shop")
    st.metric(label="Calças Pantalona", value="Estável", delta="Top Vendas")
