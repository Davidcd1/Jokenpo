from random import randint
import customtkinter as ctk
from PIL import Image

pontuacao = 0

# Cores
COR_FUNDO = "#1e1e2e"
COR_TEXTO = "#f5e0dc"
COR_BOTAO = "#89b4fa"
COR_TEXTO_BOTAO = "#1e1e2e"
TAMANHO_BOTAO = (80, 40)

# Setup da UI
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

# Janela principal
janela = ctk.CTk()
janela.iconbitmap("icon.ico")
largura_janela = 600
altura_janela = 500
janela.title("JOKENPÔ")
janela.configure(fg_color=COR_FUNDO)
janela.resizable(False, False)

# Centraliza a janela na tela
largura_tela = janela.winfo_screenwidth()
altura_tela = janela.winfo_screenheight()
janela.geometry(f"{largura_janela}x{altura_janela}+{int((largura_tela - largura_janela) / 2)}+{int((altura_tela - altura_janela) / 2)}")

# Frame principal
frame = ctk.CTkFrame(janela, fg_color=COR_FUNDO, corner_radius=20)
frame.pack(expand=True, fill="both", padx=20, pady=20)

# Título do jogo
titulo = ctk.CTkLabel(frame, text="🔹 JOKENPÔ", text_color=COR_TEXTO, font=("Arial", 24))
titulo.pack(pady=30)

# Imagens
img_pedra = ctk.CTkImage(Image.open("pedra.png"), size=(25, 25))
img_papel = ctk.CTkImage(Image.open("papel.png"), size=(25, 25))
img_tesoura = ctk.CTkImage(Image.open("tesoura.png"), size=(25, 25))
imagem_resultado = ctk.CTkImage(Image.open("default.png"), size=(80, 80))
img_robo = ctk.CTkImage(Image.open("robo.png"), size=(45, 40))

# Frame pro avatar do robô e jogada da máquina
frame_robo = ctk.CTkFrame(frame, fg_color="transparent")
frame_robo.pack(anchor="ne", padx=10)

# Imagem do robô
label_robo = ctk.CTkLabel(frame_robo, image=img_robo, text="")
label_robo.pack()

# Frame com fundo pra jogada da máquina (como se fosse um botão)
frame_jogada_maquina = ctk.CTkFrame(frame_robo, fg_color="#58440B", corner_radius=15)
frame_jogada_maquina.pack(pady=5)

# Label da imagem dentro do frame
label_jogada_maquina = ctk.CTkLabel(frame_jogada_maquina, text="", fg_color="transparent", width=50, height=25)
label_jogada_maquina.pack(padx=10, pady=10)


# Frame do resultado (imagem e texto)
frame_resultado = ctk.CTkFrame(frame, fg_color="#313244", corner_radius=15)
frame_resultado.pack(pady=10)

# Imagem padrão
label_resultado = ctk.CTkLabel(frame_resultado, text="", image=imagem_resultado, fg_color="transparent")
label_resultado.pack(padx=20, pady=20)

# Label da pontuação
label_pontuacao = ctk.CTkLabel(frame, text=f"Pontuação: {pontuacao}", text_color=COR_TEXTO, font=("Arial", 12))
label_pontuacao.pack(pady=10)

# ========== Funções do jogo ==========

# Pega a jogada da máquina, compara com a do jogador e atualiza a interface
def jogar(jogada_usuario):
    if jogada_usuario == 1:
        label_jogada_jogador.configure(image=img_pedra)
    elif jogada_usuario == 2:
        label_jogada_jogador.configure(image=img_papel)
    elif jogada_usuario == 3:
        label_jogada_jogador.configure(image=img_tesoura)

    global pontuacao
    jogada_maquina = jogada_da_maquina()
    resultado = comparar(jogada_usuario, jogada_maquina)
    label_resultado.configure(text=resultado)
    label_pontuacao.configure(text=f"Pontuação {pontuacao}")


# Gera uma jogada aleatória pra máquina (1 = pedra, 2 = papel, 3 = tesoura)
def jogada_da_maquina():
    jogada = randint(1, 3)
    # Atualiza imagem da jogada da máquina
    if jogada == 1:
        label_jogada_maquina.configure(image=img_pedra)
    elif jogada == 2:
        label_jogada_maquina.configure(image=img_papel)
    elif jogada == 3:
        label_jogada_maquina.configure(image=img_tesoura)
    return jogada

# Compara as jogadas e atualiza a pontuação
def comparar(jogada_usuario, jogada_maquina):
    global pontuacao
    if jogada_usuario == jogada_maquina:
        return "Empate!"
    vencedor = (jogada_usuario - jogada_maquina) % 3
    if vencedor == 1:
        pontuacao += 1
        return "Você venceu!"
    else:
        pontuacao -= 1
        return "Você perdeu!"


# =====================================

# Frame onde ficam os botões
frame_botoes = ctk.CTkFrame(frame, fg_color="transparent")
frame_botoes.pack(side="bottom", pady=20)

# Botão PEDRA
botao_pedra = ctk.CTkButton(
    frame_botoes, text="", image=img_pedra, compound="top",
    width=TAMANHO_BOTAO[0], height=TAMANHO_BOTAO[1],
    fg_color=COR_BOTAO, text_color=COR_TEXTO_BOTAO, hover_color="#74c7ec",
    corner_radius=15, command=lambda: jogar(1)
)
botao_pedra.grid(row=0, column=0, padx=10)

# Botão PAPEL
botao_papel = ctk.CTkButton(
    frame_botoes, text="", image=img_papel, compound="top",
    width=TAMANHO_BOTAO[0], height=TAMANHO_BOTAO[1],
    fg_color=COR_BOTAO, text_color=COR_TEXTO_BOTAO, hover_color="#74c7ec",
    corner_radius=15, command=lambda: jogar(2)
)
botao_papel.grid(row=0, column=1, padx=10)

# Botão TESOURA
botao_tesoura = ctk.CTkButton(
    frame_botoes, text="", image=img_tesoura, compound="top",
    width=TAMANHO_BOTAO[0], height=TAMANHO_BOTAO[1],
    fg_color=COR_BOTAO, text_color=COR_TEXTO_BOTAO, hover_color="#74c7ec",
    corner_radius=15, command=lambda: jogar(3)
)
botao_tesoura.grid(row=0, column=2, padx=10)

# Frame da jogada do jogador (renomeado pra não conflitar)
frame_jogada_jogador = ctk.CTkFrame(frame_botoes, fg_color="#58440B", corner_radius=15)

frame_jogada_jogador.grid(row=0, column=8, padx=10)

# Label da imagem do jogador dentro do frame
label_jogada_jogador = ctk.CTkLabel(frame_jogada_jogador, text="", fg_color="transparent", width=50, height=25)
label_jogada_jogador.pack(padx=10, pady=10)


# Inicia a interface
janela.mainloop()
