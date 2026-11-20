import tkinter as tk
from tkinter import messagebox

class ConversaoMoeda:
    def __init__(self, master):
        self.master = master
        self.master.title("Conversão de Moeda")
        self.master.geometry("400x300")
        self.master.resizable(False, False)
        
        self.reais = tk.StringVar()
        self.cotacao_dolar = tk.StringVar()
        self.cotacao_euro = tk.StringVar()
        
        self.valoe_em_dolar = tk.StringVar()
        self.valoe_em_euro = tk.StringVar()
        
        tk.Label(master, text="Valor em Reais (R$):").grid(row=0, column=0, sticky="w", padx=10, pady=10)
        tk.Entry(master, textvariable=self.reais).grid(row=0, column=1, padx=10, pady=10)
        
        tk.Label(master, text="Valor em Dólar ($):").grid(row=1, column=0, sticky="w", padx=10, pady=10)
        tk.Entry(master, textvariable=self.cotacao_dolar).grid(row=1, column=1, padx=10, pady=10)
        
        tk.Label(master, text="Valor em Euro (€):").grid(row=2, column=0, sticky="w", padx=10, pady=10)
        tk.Entry(master, textvariable=self.cotacao_euro).grid(row=2, column=1, padx=10, pady=10)
        
        tk.Button(master, text="Calcular Conversão", command=self.Calcular_conversao).grid(row=3, column=0, padx=15, pady=20)
        tk.Button(master, text="Exibir Resultados", command=self.Exibir_resultados).grid(row=3, column=1, padx=15, pady=5)
    def Calcular_conversao(self):
        try:
            reais = float(self.reais.get().replace(",", "."))
            cotacao_dolar = float(self.cotacao_dolar.get().replace(",", "."))
            cotacao_euro = float(self.cotacao_euro.get().replace(",", "."))
            
            valor_em_dolar = reais / cotacao_dolar
            valor_em_euro = reais / cotacao_euro
            
            self.valoe_em_dolar.set(f"{valor_em_dolar:.2f}")
            self.valoe_em_euro.set(f"{valor_em_euro:.2f}")
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira valores válidos.")
            
    def Exibir_resultados(self):
        janela_resultados = tk.Toplevel(self.master)
        janela_resultados.title("Resultados da Conversão")
        janela_resultados.geometry("300x200")
        
        tk.Label(janela_resultados, text=f"Valor em Reais (R$): {self.reais.get()}").grid(row=1, column=0, padx=10, pady=10)
        tk.Label(janela_resultados, text=f"Valor convertido em Dólar ($): {self.valoe_em_dolar:.2f}").grid(row=1, column=0, padx=10, pady=10)
        tk.Label(janela_resultados, text=f"Valor convertido em Euro (€): {self.valoe_em_euro:.2f}").grid(row=2, column=0, padx=10, pady=10)
        
if __name__ == "__main__":
    root = tk.Tk()
    app = ConversaoMoeda(root)
    root.mainloop()
        
