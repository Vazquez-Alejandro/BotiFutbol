# BotifutBot - Bot de Noticias de Fútbol

Un bot de Telegram que te envía noticias y actualizaciones de tus equipos de fútbol favoritos.

## 🚀 Características

- ⚽ Seguimiento de múltiples equipos
- 📰 Noticias automáticas de tus equipos
- 🔍 Búsqueda de equipos por nombre
- 📊 Actualizaciones de partidos en tiempo real
- 🎨 Menú interactivo con botones

## 📋 Requisitos

- Python 3.10+
- Token de Bot de Telegram
- API Key de API-Football
- API Key de NewsAPI (opcional)

## ⚙️ Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/Vazquez-Alejandro/botifutbol.git
cd botifutbol
```

### 2. Crear entorno virtual

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# o
venv\Scripts\activate  # Windows
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Configurar variables de entorno

```bash
cp .env.example .env
```

Editar el archivo `.env` con tus credenciales:

```env
TELEGRAM_TOKEN=tu_token_de_telegram
API_FOOTBALL_KEY=tu_api_key_de_api_football
NEWS_API_KEY=tu_api_key_de_newsapi
```

### 5. Ejecutar el bot

```bash
python bot.py
```

## 🔑 Obtención de API Keys

### Telegram Bot Token

1. Habla con [@BotFather](https://t.me/BotFather) en Telegram
2. Crea un nuevo bot con `/newbot`
3. Copia el token que te dé

### API-Football

1. Visita [api-football.com](https://www.api-football.com/)
2. Regístrate para obtener una API key gratuita
3. El plan gratuito permite 100 llamadas/día

### NewsAPI (Opcional)

1. Visita [newsapi.org](https://newsapi.org/)
2. Regístrate para obtener una API key gratuita
3. Plan gratuito: 100 requests/día

## 📁 Estructura del Proyecto

```
botifutbol/
├── bot.py              # Archivo principal
├── requirements.txt    # Dependencias
├── .env.example        # Ejemplo de configuración
├── README.md           # Esta documentación
├── src/
│   ├── __init__.py
│   ├── config.py       # Configuración
│   ├── database.py     # Base de datos SQLite
│   ├── api_client.py   # Cliente API-Football
│   ├── news_client.py  # Cliente NewsAPI
│   └── handlers.py     # Manejadores de comandos
├── assets/
│   └── logo.png        # Logo del bot
├── data/               # Datos (se crea automáticamente)
└── tests/              # Tests
```

## 🎮 Comandos del Bot

| Comando | Descripción |
|---------|-------------|
| `/start` | Inicia el bot y muestra el menú |
| `/equipos` | Muestra tus equipos seguidos |
| `/buscar <nombre>` | Busca un equipo por nombre |
| `/noticias` | Muestra noticias de tus equipos |
| `/ayuda` | Muestra ayuda |

## 🤖 Uso

1. Inicia el bot con `/start`
2. Selecciona "Buscar Equipo" para agregar equipos
3. Recibe notificaciones automáticas de tus equipos
4. Consulta noticias con el botón "Noticias"

## 📝 License

MIT License

## 👨‍💻 Desarrollado por

Tu nombre aquí
