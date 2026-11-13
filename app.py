import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="Valentina Labs - TikTok Shop Automation",
    page_icon="💜",
    layout="wide"
)

# 1. TOPO DA APLICAÇÃO
st.title("💜 VALENTINA LABS • TIKTOK SHOP AUTOMATION")
st.caption("LOJA DA VALENTINA • SCHEDULED MULTI-SCENARIO ENGINE (09:00 - 23:00)")

st.markdown("---")

# 2. SELETORES DO TOPO
c_top1, c_top2 = st.columns(2)
with c_top1:
    diretor_skin = st.selectbox("DIRETOR SKIN", ["BOY (Elite Director)", "UGC LIFESTYLE (Influencer & Conversão)"])
with c_top2:
    proporcao = st.selectbox("PROPORÇÃO", ["9:16 (TikTok / Reels)", "1:1 (Feed)", "16:9 (Wide)"])

st.markdown("---")

# 3. SELEÇÃO DE ESTILOS POR CAIXINHAS
st.subheader("🎬 SELECIONE OS ESTILOS / CENÁRIOS DESEJADOS (MARQUE DE 1 A 8+):")

lista_estilos_disponiveis = [
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
]

col_chk1, col_chk2 = st.columns(2)
estilos_selecionados = []

for i, estilo in enumerate(lista_estilos_disponiveis):
    target_col = col_chk1 if i % 2 == 0 else col_chk2
    with target_col:
        if st.checkbox(estilo, key=f"chk_estilo_{i}"):
            estilos_selecionados.append(estilo)

st.markdown("---")

# 4. ENTRADAS DO PRODUTO
col_input1, col_input2 = st.columns(2)

with col_input1:
    produto_nome = st.text_input("NOME EXATO DO PRODUTO / SKU", placeholder="Ex: Sandália Gigil Salto Bloco...")
    foto_produto_analise = st.file_uploader("Upload Foto Produto", type=["jpg", "jpeg", "png"], key="prod_upload_original")
    tipo_produto = st.selectbox("CATEGORIA DO PRODUTO (FOCO ASSERTIVO)", [
        "Calçado / Tênis / Sandália", 
        "Acessório de Pulso ou Rosto (Relógio / Óculos)", 
        "Vestuário / Vestido / Conjunto / Calça",
        "Bolsa / Acessório de Mão",
        "Utilidades & Outros"
    ])
    
with col_input2:
    foto_modelo = st.file_uploader("Upload Foto Modelo (Face & Corpo 1:1)", type=["jpg", "jpeg", "png"], key="m")
    foto_peca = st.file_uploader("Upload Foto Referência Peça (Isolada)", type=["jpg", "jpeg", "png"], key="p")

st.markdown("---")

# 5. CONFIGURAÇÃO DE FOCO E GRADE DE HORÁRIOS
def get_config_categoria(categoria):
    if "Calçado" in categoria:
        return {
            "foco_posicao": "on her feet, footwear showcase",
            "verbo_local": "nos pés",
            "acao_tryon": "calçando",
            "instrucao_tecnica": "Focus exclusively on footwear display, showing shoes clearly on feet, highlighting heel height and comfort."
        }
    elif "Acessório" in categoria:
        return {
            "foco_posicao": "on her wrist/face, accessory showcase",
            "verbo_local": "no visual",
            "acao_tryon": "usando",
            "instrucao_tecnica": "Focus exclusively on accessory display, highlighting metal finish, details, and elegance."
        }
    elif "Vestuário" in categoria:
        return {
            "foco_posicao": "on her body, apparel outfit",
            "verbo_local": "no corpo",
            "acao_tryon": "vestindo",
            "instrucao_tecnica": "Focus exclusively on apparel display, showing fabric flow, tailoring, and fit on the body."
        }
    elif "Bolsa" in categoria:
        return {
            "foco_posicao": "in her hands, handbag showcase",
            "verbo_local": "no look",
            "acao_tryon": "segurando/usando",
            "instrucao_tecnica": "Focus exclusively on handbag display, highlighting texture, strap, and size."
        }
    else:
        return {
            "foco_posicao": "interacting with product",
            "verbo_local": "perfeito",
            "acao_tryon": "testando",
            "instrucao_tecnica": "Focus on clear product demonstration and interaction."
        }

def get_roteiros_banco(prod, cfg):
    v = cfg["verbo_local"]
    return [
        f"Amiga, para tudo e olha esse(a) {prod} da Loja da Valentina! Qualidade nobre, acabamento impecável {v}. Olha que luxo! Clica no carrinho laranja aqui embaixo e já garante o(a) seu(sua) agora.",
        f"Gente, sério, precisava mostrar a qualidade absurda desse(a) {prod}... material impecável que surpreende {v}. Olha esse detalhe! Corre na Loja da Valentina e clica no carrinho laranja.",
        f"Olha esse achado na Loja da Valentina! Esse(a) {prod} é perfeito(a), acabamento impecável. É um espetáculo de elegância {v}! Clica no carrinho laranja aí embaixo e já garante o(a) seu(sua).",
        f"Meninas, vocês queriam {prod} de altíssima qualidade? Achei! Esse(a) aqui é único(a). Corre na Loja da Valentina, clica no carrinho laranja e aproveita o frete.",
        f"Olha a sofisticação desse(a) {prod} que acabou de chegar... padrão premium impecável. Caimento perfeito {v}! Garante o(a) seu(sua) direto na Loja da Valentina clicando no carrinho laranja.",
        f"Para tudo e presta atenção na qualidade desse(a) {prod}... material maravilhoso e super confortável. Fica deslumbrante {v}! Disponível na Loja da Valentina, clica no carrinho laranja.",
        f"Amiga, elegância e conforto total com esse(a) {prod} da Loja da Valentina. Qualidade de shopping por preço de fábrica! Olha como fica {v}. Clica no carrinho laranja aqui embaixo.",
        f"Gente, eu testei e apaixonei... esse(a) {prod} tem uma qualidade surreal. É perfeito(a) {v}! Disponível na Loja da Valentina, clica no carrinho laranja.",
        f"Olha esse design impecável... esse(a) {prod} combina com tudo! Peça indispensável. Corre lá na Loja da Valentina e clica no carrinho laranja aqui embaixo para garantir.",
        f"Meninas, qualidade de primeira linha que fala, né? Esse(a) {prod} é perfeito demais. Olha como valoriza o visual {v}! Garante o(a) seu(sua) na Loja da Valentina, clica no carrinho laranja."
    ]

GRADE_HORARIOS = ["09:00", "11:00", "13:00", "15:00", "17:00", "19:00", "21:00", "23:00"]

# 6. GERADOR
if st.button("🚀 GERAR PROMPTS DA GRADE DIÁRIA"):
    if not produto_nome:
        st.warning("⚠️ Por favor, informe o nome exato do produto.")
    elif not foto_peca or not foto_modelo or not foto_produto_analise:
        st.warning("⚠️ Por favor, faça o upload de todas as fotos necessárias.")
    elif not estilos_selecionados:
        st.warning("⚠️ Por favor, selecione pelo menos 1 estilo nas caixinhas acima.")
    else:
        agora = datetime.now().strftime("%H:%M:%S")
        total_gerados = len(estilos_selecionados)
        st.success(f"✅ Gerados {total_gerados} prompts às {agora} para '{produto_nome}'.")
        
        cfg = get_config_categoria(tipo_produto)
        banco_roteiros = get_roteiros_banco(produto_nome, cfg)
        
        for idx, estilo_atual in enumerate(estilos_selecionados):
            prompt_numero = idx + 1
            roteiro_atual = banco_roteiros[idx % len(banco_roteiros)]
            horario_postagem = GRADE_HORARIOS[idx % len(GRADE_HORARIOS)]

            prompt_final = (
                f"Masterpiece 8K UHD viral TikTok Shop UGC video powered by Arri Alexa cinema color science (10-second precise duration, {proporcao.split()[0]}), RAW optical sensor. ACTIVE STYLE: {estilo_atual}. "
                f"STRICT ASSERTIVE CATEGORY & ZERO MIC PROTOCOL: {cfg['instrucao_tecnica']}. Strictly binding uploaded model reference face/body and isolated product reference pixels of '{produto_nome}' with zero alterations. "
                f"Absolute zero microphones, NO lapel mics, NO clip-on mics, NO wireless mics on clothing, NO earphones, NO floating gadgets, NO text overlays, NO subtitles, NO watermarks, NO UI graphics, NO branding. Bare clothes, clean collarbone, completely bare clothing surface with zero attachments. "
                f"Cinematic Visual Engineering: hyper-detailed micro-textures on material weave, razor-sharp natural focus, rich dynamic contrast with zero washed-out shadows, professional 3-point studio lighting, lifelike human skin pores, and glossy vibrant color grading. "
                f"Strict 1:1 pixel lock: identical reference model face and body proportions. "
                f"Rigid product lock: exact '{produto_nome}' matching reference image with zero substitution. "
                f"VIRAL HOOK & FLUID TRY-ON FLOW (0-10s): The video opens dynamically with the creator looking straight into the camera holding '{produto_nome}' for the first 2 seconds delivering a strong magnetic hook, then seamlessly transitions at second 2 already {cfg['acao_tryon']} '{produto_nome}' ({cfg['foco_posicao']}) in a chic mirror/dressing room setting, pacing her speech evenly across the full 10 seconds while interacting directly with the item. "
                f"IMMEDIATE FLUID START & CLEAN SCREEN: Absolute zero static frames, zero ghosting, zero overlay transparency, zero floating text, zero subtitles, zero UI overlays, zero watermarks. "
                f"SMOOTH TAIL BUFFER: Action and speech naturally conclude right at 10 seconds with zero abrupt audio cuts and zero dead silence. "
                f"Fixed static background, organic human movement.\n\n"
                f"LOCUÇÃO RÍTMICA (10s com distribuição equilibrada de fala e conversão): \"{roteiro_atual}\"\n\n"
                f"Absolute Negative Prompt / Anti-Mic & Anti-Artifact Engine: microphone, lapel mic, clip-on microphone, wireless mic, badge, pin, earphones, clipped accessories, floating gadgets, washed-out colors, dull lighting, blurry details, soft focus, digital noise, flat lighting, early speech ending, dead silence at the end, staying only holding the item without wearing it, no try-on, over 10s, rushed speech, fast jerky movement, static starting frame, ghosting effect, transparent overlay, floating text, subtitles, UI graphics, watermarks, abrupt appearance, pop-up object, harsh audio cut, model swapping, face morphing, background shift, CGI."
            )

            st.markdown(f"### 🎬 Prompt Comercial #{prompt_numero} • ⏰ Horário: {horario_postagem}")
            st.info(f"Cenário: {estilo_atual}")
            st.code(prompt_final, language="text")
            st.markdown("---")
