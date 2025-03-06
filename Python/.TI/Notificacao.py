from plyer import notification

notification.notify(
    title='Minha Notificação',
    message='Esta é uma mensagem de teste!',    
    timeout=10  # Tempo em segundos que a notificação permanece visível (opcional)
)