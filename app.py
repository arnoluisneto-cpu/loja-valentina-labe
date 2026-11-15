import json
import os

# Arquivo único e permanente no disco para guardar TODOS os prompts sem limite
DB_FILE = "moldes_salvos.json"


def carregar_moldes_do_disco():
  """Carrega todos os moldes salvos do disco de forma permanente."""
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
  """Salva ou apaga definitivamente no disco, aceitando quantidade infinita."""
  with open(DB_FILE, "w", encoding="utf-8") as f:
    json.dump(moldes_dict, f, ensure_ascii=False, indent=4)


# Garante que os dados estejam carregados na sessão atual
if "moldes" not in st.session_state:
  st.session_state.moldes = carregar_moldes_do_disco()

# --- LÓGICA EXATA DE SALVAR E APAGAR DEFINITIVAMENTE ---
# (Substitua a sua área de botões de salvar/apagar por esta estrutura abaixo)

col1, col2 = st.columns(2)

with col1:
  st.markdown("### Adicionar ou Editar Prompt")
  nome_chave = st.text_input("Identificação / Nome do Prompt:")
  conteudo_prompt = st.text_area(
      "Conteúdo Bruto do Prompt (Sem fala):", height=150
  )

  if st.button("💾 Salvar Prompt Definitivamente", type="primary"):
    if nome_chave and conteudo_prompt:
      # Adiciona ou atualiza na memória e joga direto para o arquivo físico no disco
      st.session_state.moldes[nome_chave] = conteudo_prompt
      persistir_moldes_no_disco(st.session_state.moldes)
      st.success(
          f"Prompt '{nome_chave}' salvo com sucesso! (Total na base:"
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
    # Exibe todos os prompts salvos, permitindo gerenciar infinitos itens
    for k_nome in list(st.session_state.moldes.keys()):
      st.write(f"📌 **{k_nome}**")
      if st.button(f"🗑️ Apagar '{k_nome}'", key=f"del_inf_{k_nome}"):
        # Remove definitivamente da sessão e atualiza o disco
        if k_nome in st.session_state.moldes:
          del st.session_state.moldes[k_nome]
          persistir_moldes_no_disco(st.session_state.moldes)
          st.success(f"Prompt '{k_nome}' apagado definitivamente do sistema.")
          st.rerun()
  else:
    st.info("Nenhum prompt salvo no momento.")
