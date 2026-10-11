# Dns_changer
# ⚡ Quick DNS Changer (Быстрый DNS Чейнджер)

Простая и удобная утилита на Python для смены DNS-сервера в операционной системе Windows в один клик. Помогает быстро переключиться на более быстрый или безопасный DNS (Google, Cloudflare, Quad9) или вернуть настройки по умолчанию.

---

## ✨ Features (Особенности)
* **1-Click Change:** Смена DNS в один клик без захода в глубокие настройки Windows.
* **Popular Providers:** Предустановленные профили Cloudflare, Google Public DNS и Quad9.
* **Auto-Reset:** Возможность сбросить настройки на автоматические (DHCP).
* **Safe Exit:** Настройки сохраняются на уровне системы даже после закрытия программы.
* **UAC Support:** Автоматически запрашивает права администратора при запуске.

---

## 🚀 How to Run (Как запустить)

### Option 1: For Users (Для пользователей)
Вы можете скачать готовый `.exe` файл во вкладке **Releases** справа. Установка не требуется — просто скачайте и запустите.

### Option 2: From Source (Из исходного кода)
Если вы разработчик и хотите запустить проект из кода:

1. Клонируйте репозиторий / Clone the repository:
   ```bash
   git clone https://github.com
   ```
2. Запустите скрипт (требуется установленный Python 3) / Run the script:
   ```bash
   python dns_changer.py
   ```

---

## 🛠 Tech Stack (Технологии)
* **Python 3**
* **Tkinter** (Встроенная графическая библиотека)
* **Windows Netsh CLI** (Системные команды для настройки сети)
* **PyInstaller** (Для сборки в .exe)

---

## 📦 How to Build .exe (Как собрать .exe самостоятельно)
Если вы хотите скомпилировать этот скрипт в один файл самостоятельно, используйте команду:
```bash
pip install pyinstaller
pyinstaller --noconsole --onefile --uac-admin dns_changer.py
```
Готовый файл появится в папке `dist`.
