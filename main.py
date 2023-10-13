import requests
import customtkinter as ctk
import json
from tkinter import messagebox

class ChatGtp():
    def __init__(self):
        self.api_key = 'Sua API'

    def integrar_chat(self):
        self.headers = {"Authorization": f"Bearer {self.api_key}", "Content-Type": "application/json"}
        self.link = "https://api.openai.com/v1/chat/completions"
        self.id_modelo = "gpt-3.5-turbo"
        self.body_mensagem = {
            "model": self.id_modelo,
            "messages": [{"role": "user", "content": f"{self.pesquisa_entry.get()}"}]
        }
        self.body_mensagem = json.dumps(self.body_mensagem)
        self.requisicao = requests.post(self.link, headers=self.headers, data=self.body_mensagem)
        self.resposta = self.requisicao.json()
        self.mensagem = self.resposta["choices"][0]["message"]["content"]
        self.resultado = messagebox.showinfo('Pesquisa',self.mensagem)

class App(ctk.CTk,ChatGtp):
    def __init__(self):
        ctk.CTk.__init__(self)
        ChatGtp.__init__(self)
        self.configuracoes_janela_inicial()
        self.tela_chatgpt()

    def configuracoes_janela_inicial(self):
        self.title('Chatgpt')
        self.resizable(0,0)
        self.largura_tela = self.winfo_screenwidth()
        self.altura_tela = self.winfo_screenheight()
        self.largura_janela = 300
        self.altura_janela = 200
        self.posicao_x = (self.largura_tela - self.largura_janela) // 2
        self.posicao_y = (self.altura_tela - self.altura_janela) // 2
        self.geometry(f'{self.largura_janela}x{self.altura_janela}+{self.posicao_x}+{self.posicao_y}')

    def tela_chatgpt(self):
        self.mensagem_inicial = ctk.CTkLabel(self,text='Faça sua pesquisa')
        self.mensagem_inicial.pack(padx=10,pady=10)

        self.pesquisa_entry = ctk.CTkEntry(self,placeholder_text='Pesquisar')
        self.pesquisa_entry.pack(padx=10,pady=10)

        self.pesquisa_butao = ctk.CTkButton(self,text='Pesquisar',command=self.integrar_chat)
        self.pesquisa_butao.pack(side='left',padx=10)

        self.parar_chat = ctk.CTkButton(self,text='Sair',command=self.sair)
        self.parar_chat.pack(side='left',padx=10)
    
    def sair(self):
        self.quit()
    

if __name__=='__main__':
    app = App()
    app.mainloop()