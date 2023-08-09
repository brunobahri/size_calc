import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def calculate():
    try:
        altura = float(entry_dict["entry_altura"].get())
        largura = float(entry_dict["entry_largura"].get())
        profundidade = float(entry_dict["entry_profundidade"].get())

        volume_total = altura * largura * profundidade

        VALOR_CAIXA_G = 91125000  # mm³
        VALOR_CAIXA_M = 50625000  # mm³

        if caixa_combobox.get() == "Caixa G":
            VALOR_CAIXA = VALOR_CAIXA_G
        elif caixa_combobox.get() == "Caixa M":
            VALOR_CAIXA = VALOR_CAIXA_M

        quantidade_na_caixa = int(VALOR_CAIXA / volume_total * 0.9)
        peso_da_peca = float(entry_dict["entry_peso"].get())

        peso_caixa = (peso_da_peca * quantidade_na_caixa) + 1000
        peso_palete_caixa = ((peso_caixa * 20) + 5000) / 1000

        if caixa_combobox.get() == "Caixa G":
            result_g_label.config(text=f"Quantidade na Caixa G: {quantidade_na_caixa}")
            result_m_label.config(text="")
            result_weight_g_label.config(text=f"Peso da Caixa G: {((peso_caixa / 1000)):.2f} kg")
            result_weight_m_label.config(text="")
            result_palete_g_label.config(text=f"Peso do Palete com Caixa G: {peso_palete_caixa:.2f} kg")
            result_palete_m_label.config(text="")
        elif caixa_combobox.get() == "Caixa M":
            result_g_label.config(text="")
            result_m_label.config(text=f"Quantidade na Caixa M: {quantidade_na_caixa}")
            result_weight_g_label.config(text="")
            result_weight_m_label.config(text=f"Peso da Caixa M: {((peso_caixa / 1000)):.2f} kg")
            result_palete_g_label.config(text="")
            result_palete_m_label.config(text=f"Peso do Palete com Caixa M: {peso_palete_caixa:.2f} kg")

        cubagem_label.config(text="CUBAGEM PADRÃO PARA PALETE 2.4m³")

    except ValueError:
        messagebox.showerror("Erro", "Certifique-se de inserir valores válidos.")

app = tk.Tk()
app.title("Calculadora de embalagem")

# Defina o tamanho da janela
app.geometry("480x720")

style = ttk.Style()
style.configure("TFrame", background="#f0f0f0")
style.configure("TLabel", background="#f0f0f0", font='Helvetica 12 bold')
style.configure("TEntry", background="white", font='Helvetica 12', insertwidth=4)
style.configure("TButton", background="#4CAF50", font='Helvetica 12', padding=5)
style.configure("TCombobox", background="white", font='Helvetica 12', padding=4)

frame = ttk.Frame(app)
frame.pack(fill="both", expand=True)
frame.pack_propagate(False)

# Centralize o frame no meio da janela
frame.place(relx=0.5, rely=0.5, anchor="center")

labels_entries = [
    ("Altura da Peça (mm):", "entry_altura"),
    ("Largura da Peça (mm):", "entry_largura"),
    ("Profundidade/Expessura (mm):", "entry_profundidade"),
    ("Peso da Peça (g):", "entry_peso")
]

row_num = 0
entry_dict = {}
for label, entry_name in labels_entries:
    ttk.Label(frame, text=label).grid(row=row_num, column=0, padx=10, pady=15)
    entry = ttk.Entry(frame, font='Helvetica 12')  # Definindo a fonte aqui
    entry.grid(row=row_num, column=1, padx=10, pady=15)
    entry_dict[entry_name] = entry
    row_num += 1

ttk.Label(frame, text="Selecione o modelo de caixa:", font='Helvetica 12').grid(row=row_num, column=0, padx=10, pady=15)
caixa_combobox = ttk.Combobox(frame, values=["Caixa G", "Caixa M"], font='Helvetica 12')
caixa_combobox.grid(row=row_num, column=1, padx=10, pady=15)

calculate_button = ttk.Button(frame, text="Calcular", command=calculate)
calculate_button.grid(row=row_num + 1, columnspan=2, pady=15)

result_g_label = ttk.Label(frame, text="", font='Helvetica 12 bold')
result_g_label.grid(row=row_num + 2, columnspan=2, pady=5)

result_m_label = ttk.Label(frame, text="", font='Helvetica 12 bold')
result_m_label.grid(row=row_num + 3, columnspan=2, pady=5)

result_weight_g_label = ttk.Label(frame, text="", font='Helvetica 12')
result_weight_g_label.grid(row=row_num + 4, columnspan=2, pady=5)

result_weight_m_label = ttk.Label(frame, text="", font='Helvetica 12')
result_weight_m_label.grid(row=row_num + 5, columnspan=2, pady=5)

result_palete_g_label = ttk.Label(frame, text="", font='Helvetica 12')
result_palete_g_label.grid(row=row_num + 6, columnspan=2, pady=5)

result_palete_m_label = ttk.Label(frame, text="", font='Helvetica 12')
result_palete_m_label.grid(row=row_num + 7, columnspan=2, pady=5)

cubagem_label = ttk.Label(frame, text="", font='Helvetica 12 bold')
cubagem_label.grid(row=row_num + 8, columnspan=2, pady=5)

rodape_label = ttk.Label(frame, text="Aplicativo desenvolvido com PYTHON;\nPor Bruno Bahri™\ncontato: brunosbluiz@gmail.com\nTodos os direitos reservados 2023™", font='Helvetica 7 italic')
rodape_label.grid(row=row_num + 9, columnspan=2, pady=10, sticky="s")

app.mainloop()
