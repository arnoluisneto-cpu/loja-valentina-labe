import json
import os
import streamlit as st

# Configuração da página e identidade visual original (Estilo Nubank / Dark Moderno)
st.set_page_config(
    page_title="Laboratórios Valentina",
    page_icon="💜",
    layout="wide",
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

# --- INTERFACE ORIGINAL EXATA ---
st.title("LABORATÓRIOS VALENTINA")
st.markdown(
    "**LOJA DA VALENTINA - AUTOMATIZAÇÃO DE LOJAS NO TIKTOK** 💜"
)

st.divider()

# Painel de controle rápido original (Estilo Nubank)
col_a, col_b, col_c = st.columns(3)
with col_a:
  st.markdown("### 🎯 DIRETOR SKIN")
  st.markdown("`BOY (Elite Director)`")
with col_b:
  st.markdown("### 📐 PROPORÇÃO")
  st.markdown("`9:16 (TikTok / Reels)`")
with col_c:
  st.markdown("### ⚡ STATUS ENGINE")
  st.markdown("`Ativo & Sincronizado`")

st.divider()

st.subheader("🛠️ PAINEL DE CONTROLE RÁPIDO")

col1, col2 = st.columns(2)

with col1:
  st.markdown("### Adicionar ou Editar Prompt")
  nome_molde = st.text_input("Nome do Prompt:")
  conteudo_molde = st.text_area("Estrutura Técnica Bruta:", height=130)

  if st.button("💾 Salvar Prompt Definitivamente", type="primary"):
    if nome_molde and conteudo_molde:
      st.session_state.moldes[nome_molde] = conteudo_molde
      persistir_moldes_no_disco(st.session_state.moldes)
      st.success(f"Prompt '{nome_molde}' salvo com sucesso!")
      st.rerun()
    else:
      st.warning("Preencha o nome e o conteúdo do prompt.")

with col2:
  st.markdown(
      f"### Prompts Salvos no Sistema ({len(st.session_state.moldes)})"
  )
  if st.session_state.moldes:
    for m_nome in list(st.session_state.moldes.keys()):
      st.write(f"📌 **{m_nome}**")
      if st.button(f"🗑️ Apagar {m_nome}", key=f"del_inf_{m_nome}"):
        if m_nome in st.session_state.moldes:
          del st.session_state.moldes[m_nome]
          persistir_moldes_no_disco(st.session_state.moldes)
          st.success(f"Prompt '{m_nome}' apagado definitivamente.")
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
