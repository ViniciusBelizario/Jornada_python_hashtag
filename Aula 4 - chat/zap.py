import flet as ft

def main(pagina):
    
    titulo = ft.Text("Zap")

    def entrar_no_chat(event):
        pagina.remove(titulo)
        pagina.remove(botao_iniciar)
        janela.open = False

        pagina.add(chat)
        pagina.add(linha_mensagem)
        mensagem = f"{campo_nome_usuario.value} entrou no chat"
        pagina.pubsub.send_all(mensagem)  
        pagina.update()

    titulo_janela = ft.Text("Bem vindo ao Zap")
    campo_nome_usuario = ft.TextField(label="Escreva seu nome no chat")
    botao_entrar_no_chat= ft.ElevatedButton("Entrar no chat", on_click=entrar_no_chat)

    chat = ft.Column()

    def enviar_mensagem_tunel(mensagem):
        mensagem_usuario = ft.Text(mensagem)
        chat.controls.append(mensagem_usuario)
        pagina.update()
    pagina.pubsub.subscribe(enviar_mensagem_tunel)

    def enviar_mensagem(event):
        texto_mensagem = campo_mensagem_usuario.value
        nome_usuario = campo_nome_usuario.value
        mensagem = f"{nome_usuario}: {texto_mensagem}"
        pagina.pubsub.send_all(mensagem)
        campo_mensagem_usuario.value = ""
        pagina.update()
    
    campo_mensagem_usuario = ft.TextField(label="Digite sua mensagem", on_submit=enviar_mensagem)
    botao_enviar_mensagem = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)

    janela = ft.AlertDialog(title=titulo_janela, content=campo_nome_usuario, actions=[botao_entrar_no_chat])

    linha_mensagem = ft.Row([campo_mensagem_usuario, botao_enviar_mensagem])
    def iniciar_chat(event):
        pagina.dialog = janela
        janela.open = True
        pagina.update()
    botao_iniciar = ft.ElevatedButton("Iniciar Chat", on_click=iniciar_chat)

    pagina.add(titulo)
    pagina.add(botao_iniciar)



ft.app(main, view=ft.WEB_BROWSER)