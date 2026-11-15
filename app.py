import json
import os
import streamlit as st

# Configuração da página mantendo a estética visual original
st.set_page_config(
    page_title="Laboratórios Valentina",
    page_icon="💜",
    layout="wide",
)

# Estilização CSS para garantir a identidade visual exata das fotos (Painel verde neon e fundo escuro)
st.markdown(
    """
    <style>
    .stApp {
        background-color: #0e1117;
        color: #ffffff;
    }
    div.stButton > button {
        background: linear-gradient(135deg, #7b2cbf 0%, #9d4edd 100%);
        color: white;
        border-radius: 8px;
        border: none;
        font-weight: 600;
    }
    div.stButton > button:hover {
        background: linear-gradient(135deg, #9d4edd 100%, #c77dff 100%);
        color: white;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# Arquivo permanente no disco para guardar os prompts sem limite
DB_FILE = "moldes_salvos.json"


def carregar_moldes_do_disco():
  if os.path.exists(DB_FILE):
    try:
      with open(DB_FILE, "r", encoding="utf-8") as f:
        dados = json.load(f)
        if isinstance(dados, dict):
          return dados
    except Exception:
      pass
  return {}


def persistir_moldes_no_disco(moldes_dict):
  with open(DB_FILE, "w", encoding="utf-8") as f:
    json.dump(moldes_dict, f, ensure_ascii=False, indent=4)


# Garante que os dados estejam carregados na sessão atual
if "moldes" not in st.session_state:
  st.session_state.moldes = carregar_moldes_do_disco()

# --- ESTÉTICA E ESTRUTURA ORIGINAL EXATA (COMO NAS FOTOS) ---
st.markdown(
    """
    <div style="border: 2px solid #39ff14; border-radius: 12px; padding: 20px; text-align: center; background-color: #121820; margin-bottom: 20px;">
        <h1 style="color: #ffffff; margin: 0; font-family: sans-serif; letter-spacing: 2px;">LABORATÓRIOS VALENTINA</h1>
        <p style="color: #39ff14; margin: 5px 0 0 0; font-size: 13px; font-weight: 600;">LOJA DA VALENTINA - AUTOMATIZAÇÃO DE LOJAS NO TIKTOK</p>
    </div>
""",
    unsafe_allow_html=True,
)

st.markdown("##### ⚡ PAINEL DE CONTROLE RÁPIDO")

# Os 3 blocos originais do topo (Diretor Skin, Proporção, Status Engine)
col_status1, col_status2, col_status3 = st.columns(3)

with col_status1:
  st.markdown("##### 🎯 DIRETOR SKIN")
  st.selectbox(
      "Skin ativa",
      ["BOY (Elite Director)", "Pietra (UGC Master)", "POV Shoes"],
      label_visibility="collapsed",
      key="skin_ativa",
  )

with col_status2:
  st.markdown("##### 📐 PROPORÇÃO")
  st.selectbox(
      "Proporção ativa",
      ["9:16 (TikTok / Reels)", "16:9 (YouTube)"],
      label_visibility="collapsed",
      key="prop_ativa",
  )

with col_status3:
  st.markdown("##### ⚡ STATUS ENGINE")
  st.markdown("`Ativo & Sincronizado`[cite: 2]")

st.divider()

# Seção de Gerenciamento de Moldes (Infinito e Definitivo no Disco)
st.subheader("🛠️ GERENCIAR PROMPTS & MOLDES")

col1, col2 = st.columns(2)

with col1:
  st.markdown("### Adicionar ou Editar Prompt")
  nome_chave = st.text_input("Identificação / Nome do Prompt:")
  conteudo_prompt = st.text_area(
      "Estrutura Técnica Bruta (Sem fala):", height=130
  )

  if st.button("💾 Salvar Prompt Definitivamente", type="primary"):
    if nome_chave and conteudo_prompt:
      st.session_state.moldes[nome_chave] = conteudo_prompt
      persistir_moldes_no_disco(st.session_state.moldes)
      st.success(
          f"Prompt '{nome_chave}' salvo com sucesso! (Total:"
          f" {len(st.session_state.moldes)})"
      )
      st.rerun()
    else:
      st.warning("Preencha o nome e o conteúdo do prompt.")

with col2:
  st.markdown(
      f"### Prompts Salvos no Sistema ({len(st.session_state.moldes)})"
  )

  if st.session_state.moldes:
    for k_nome in list(st.session_state.moldes.keys()):
      st.write(f"📌 **{k_nome}**")
      if st.button(f"🗑️ Apagar '{k_nome}'", key=f"del_inf_{k_nome}"):
        if k_nome in st.session_state.moldes:
          del st.session_state.moldes[k_nome]
          persistir_moldes_no_disco(st.session_state.moldes)
          st.success(f"Prompt '{k_nome}' apagado definitivamente.")
          st.rerun()
  else:
    st.info("Nenhum molde salvo no momento.")

st.divider()

st.subheader("🎬 SELECIONAR ESTILOS PARA GRADE DIÁRIA")
produto_input = st.text_input(
    "Produto do Dia (Ex: Sandália trançada preta, Calça palazzo...)"
)

if st.button("🚀 Gerar Grade com Moldes Salvos"):
  if produto_input and st.session_state.moldes:
    st.success(
        f"Gerando grade para **{produto_input}** usando os moldes salvos!"
    )
    for idx, (m_name, m_struct) in enumerate(
        st.session_state.moldes.items(), 1
    ):
      st.markdown(f"--- \n **Take {idx} ({m_name}):**")
      st.code(
          f"ESTRUTURA TÉCNICA: {m_struct}\n\nFALA GERADA (PT-BR): 'Olha essa"
          f" novidade incrível de {produto_input} que chegou na Loja da"
          " Valentina! Corre no carrinho laranja para garantir a sua antes que"
          " acabe!'"
      )
  elif not st.session_state.moldes:
    st.warning("Adicione pelo menos um molde no sistema antes de gerar.")
  else:
    st.warning("Digite o nome do produto para gerar.")
