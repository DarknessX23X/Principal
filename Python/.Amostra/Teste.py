lista = [
    "DESENGOMAR",
    "DESENGOMAR",
    "DESENGOMAR",
    "STONE COM PO",
    "STONE COM PO",
    "STONE COM PO",
    "STONE COM PO",
    "STONE COM PO",
    "REDUCAO CLORO",
    "REDUCAO CLORO",
    "NEUTRALIZAR",
    "NEUTRALIZAR",
    "CENTRIFUGA",
    "SECADOR",
    "ALVEJAMENTO IND.",
    "ALVEJAMENTO IND.",
    "ALVEJAMENTO IND.",
    "AMACIAR",
    "CENTRIFUGA",
    "SECADOR",
]

nova_lista = []
anterior = None

for item in lista:
    if item != anterior:
        if anterior is not None:  # Adiciona quebra de linha antes da palavra diferente
            nova_lista.append("")
        nova_lista.append(item)
        anterior = item
    else:
        nova_lista.append(item)

print(nova_lista)