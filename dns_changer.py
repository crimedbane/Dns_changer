import os
import sys
import ctypes
import tkinter as tk
from tkinter import messagebox

# Словарь с популярными DNS-серверами (Имя: [Основной, Альтернативный])
DNS_PROVIDERS = {
    "Cloudflare (1.1.1.1)": ["1.1.1.1", "1.0.0.1"],
    "Google (8.8.8.8)": ["8.8.8.8", "8.8.4.4"],
    "Quad9 (Безопасный)": ["9.9.9.9", "149.112.112.112"],
    "Сбросить (Автоматически)": ["dhcp", "dhcp"]
}

# В Windows обычно используется имя адаптера "Wi-Fi" или "Ethernet".
# Наш скрипт попытается изменить настройки для обоих, чтобы точно сработало.
NETWORK_INTERFACES = ["Wi-Fi", "Ethernet", "Беспроводная сеть", "Подключение по локальной сети"]

def is_admin():
    """Проверяем, запущен ли скрипт с правами администратора"""
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def change_dns():
    """Основная функция смены DNS"""
    selected = dns_listbox.get(tk.ACTIVE)
    if not selected:
        messagebox.showwarning("Внимание", "Пожалуйста, выберите DNS из списка!")
        return

    primary, secondary = DNS_PROVIDERS[selected]

    try:
        for interface in NETWORK_INTERFACES:
            if primary == "dhcp":
                # Сброс на автоматическое получение DNS от провайдера
                os.system(f'netsh interface ipv4 set dns name="{interface}" source=dhcp')
            else:
                # Установка основного и альтернативного DNS
                os.system(f'netsh interface ipv4 set dns name="{interface}" static {primary} primary')
                os.system(f'netsh interface ipv4 add dns name="{interface}" {secondary} index=2')
        
        # Очищаем кэш DNS в системе, чтобы изменения вступили в силу сразу
        os.system('ipconfig /flushdns')
        messagebox.showinfo("Успех", f"DNS успешно изменен на:\n{selected}")
    
    except Exception as e:
        messagebox.showerror("Ошибка", f"Не удалось изменить DNS: {e}")

# --- Создание графического интерфейса (GUI) ---
if not is_admin():
    # Если запуск без прав админа, просим систему перезапустить скрипт с правами админа
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
    sys.exit()

# Создаем главное окно
root = tk.Tk()
root.title("Быстрый DNS Чейнджер")
root.geometry("350x280")
root.resizable(False, False)

# Заголовок
label = tk.Label(root, text="Выберите DNS-сервер:", font=("Arial", 12, "bold"), pady=10)
label.pack()

# Список (Listbox) для выбора сервера
dns_listbox = tk.Listbox(root, font=("Arial", 11), height=5, justify="center")
for provider in DNS_PROVIDERS.keys():
    dns_listbox.insert(tk.END, provider)
dns_listbox.pack(pady=10, fill=tk.X, padx=20)
dns_listbox.activate(0) # Активируем первый элемент по умолчанию

# Кнопка применения
apply_btn = tk.Button(root, text="Применить в 1 клик", font=("Arial", 11, "bold"), 
                      bg="#4CAF50", fg="white", command=change_dns, pady=8)
apply_btn.pack(pady=15, fill=tk.X, padx=20)

# Запуск программы
root.mainloop()
