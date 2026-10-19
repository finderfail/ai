import os
from pathlib import Path

from dotenv import load_dotenv

ROOT_DIR = Path(__file__).resolve().parent.parent
load_dotenv(ROOT_DIR / ".env")

if os.getenv("EMBEDDING_OFFLINE", "1") == "1":
    os.environ.setdefault("HF_HUB_OFFLINE", "1")
    os.environ.setdefault("TRANSFORMERS_OFFLINE", "1")
    os.environ.setdefault("HF_HUB_DISABLE_TELEMETRY", "1")
    os.environ.setdefault("HF_HUB_DISABLE_IMPLICIT_TOKEN", "1")
    os.environ.setdefault("HF_HUB_ETAG_TIMEOUT", "1")
    os.environ.setdefault("DO_NOT_TRACK", "1")
    os.environ.setdefault("TOKENIZERS_PARALLELISM", "false")
    os.environ.setdefault("ANONYMIZED_TELEMETRY", "False")

KB_DIR = ROOT_DIR / "data" / "kb"
TALK_DIR = ROOT_DIR / "data" / "talk"
INFO_DIR = ROOT_DIR / "data" / "info"
AI_DIR = ROOT_DIR / "data" / "AI"
JS_DIR = ROOT_DIR / "data" / "javascript"
CURRENCY_DIR = ROOT_DIR / "data" / "currencies"
SOURCES_DIR = ROOT_DIR / "data" / "sources"
GUIDELINES_DIR = ROOT_DIR / "data" / "guidelines"
CLANG_DIR = ROOT_DIR / "data" / "clang"
FINETUNES_DIR = ROOT_DIR / "data" / "finetunes"
PERSONA_DIR = ROOT_DIR / "data" / "persona"
BOUNDARIES_DIR = ROOT_DIR / "data" / "boundaries"
DIALOG_RU_DIR = ROOT_DIR / "data" / "dialog_ru"
DIALOG_JA_DIR = ROOT_DIR / "data" / "dialog_ja"
INSULTS_DIR = ROOT_DIR / "data" / "insults"
BASH_DIR = ROOT_DIR / "data" / "bash"
GIT_DIR = ROOT_DIR / "data" / "git"
PAYMENTS_DIR = ROOT_DIR / "data" / "payments"
PROCESSING_DIR = ROOT_DIR / "data" / "processing"
BANKS_RU_DIR = ROOT_DIR / "data" / "banks_ru"
BANKS_JP_DIR = ROOT_DIR / "data" / "banks_jp"
EXPRESS_DIR = ROOT_DIR / "data" / "express"
REST_API_DIR = ROOT_DIR / "data" / "rest_api"
NODEJS_DIR = ROOT_DIR / "data" / "nodejs"
COMPANY_DIR = ROOT_DIR / "data" / "company"
CSS_DIR = ROOT_DIR / "data" / "css"
CSS1_DIR = ROOT_DIR / "data" / "css1"
HTML5_DIR = ROOT_DIR / "data" / "html5"
HTML3_DIR = ROOT_DIR / "data" / "html3"
EXAMPLES_HTML_CSS_DIR = ROOT_DIR / "data" / "examples_html_css"
INDEX_DIR = ROOT_DIR / "index"
INDEX_EMBEDDINGS_PATH = INDEX_DIR / "embeddings.npy"
INDEX_CHUNKS_PATH = INDEX_DIR / "chunks.json"
INDEX_LEXICAL_PATH = INDEX_DIR / "lexical.json"
INDEX_META_PATH = INDEX_DIR / "meta.json"

DOMAIN_DIRS = {
    "matan": KB_DIR,
    "talk": TALK_DIR,
    "info": INFO_DIR,
    "ai": AI_DIR,
    "javascript": JS_DIR,
    "currencies": CURRENCY_DIR,
    "sources": SOURCES_DIR,
    "guidelines": GUIDELINES_DIR,
    "clang": CLANG_DIR,
    "finetunes": FINETUNES_DIR,
    "boundaries": BOUNDARIES_DIR,
    "dialog_ru": DIALOG_RU_DIR,
    "dialog_ja": DIALOG_JA_DIR,
    "insults": INSULTS_DIR,
    "bash": BASH_DIR,
    "git": GIT_DIR,
    "payments": PAYMENTS_DIR,
    "processing": PROCESSING_DIR,
    "banks_ru": BANKS_RU_DIR,
    "banks_jp": BANKS_JP_DIR,
    "express": EXPRESS_DIR,
    "rest_api": REST_API_DIR,
    "nodejs": NODEJS_DIR,
    "company": COMPANY_DIR,
    "css": CSS_DIR,
    "css1": CSS1_DIR,
    "html5": HTML5_DIR,
    "html3": HTML3_DIR,
    "examples_html_css": EXAMPLES_HTML_CSS_DIR,
}

OPT_IN_DOMAINS = {
    "css1": r"css\s*-?\s*(?:1|level\s*1|уровня\s*1)\b|css\s*1\.0|первой версии css|ｃｓｓ１",
    "html3": r"html\s*-?\s*3(?:\.2|\.0)?\b|html\s*3\.2|третьей версии html",
}

ALL_DOMAINS = set(DOMAIN_DIRS.keys())

GOVERNANCE_DATA_DIR = ROOT_DIR / "data-governance"
GOVERNANCE_DOMAIN_PREFIX = "governance/"
GOVERNANCE_DOMAIN_DIRS = (
    {
        f"{GOVERNANCE_DOMAIN_PREFIX}{path.name}": path
        for path in sorted(GOVERNANCE_DATA_DIR.iterdir())
        if path.is_dir()
    }
    if GOVERNANCE_DATA_DIR.exists()
    else {}
)
GOVERNANCE_DOMAINS = set(GOVERNANCE_DOMAIN_DIRS.keys())

EMBEDDING_MODEL_NAME = os.getenv("EMBEDDING_MODEL_NAME", "intfloat/multilingual-e5-small")

OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "gemma3:270m")
OLLAMA_HOST = os.getenv("OLLAMA_HOST", "http://127.0.0.1:11434").rstrip("/")
OLLAMA_TIMEOUT = float(os.getenv("OLLAMA_TIMEOUT", "300"))
OLLAMA_KEEP_ALIVE = os.getenv("OLLAMA_KEEP_ALIVE", "30m")

REPEAT_PENALTY = float(os.getenv("REPEAT_PENALTY", "1.15"))
TOP_P = float(os.getenv("TOP_P", "0.9"))

MAX_FILE_CHARS = int(os.getenv("MAX_FILE_CHARS", "1000"))
NUM_CTX = int(os.getenv("NUM_CTX", "4096"))
CONTEXT_CHAR_BUDGET = int(os.getenv("CONTEXT_CHAR_BUDGET", "4000"))

RELEVANCE_THRESHOLD = float(os.getenv("RELEVANCE_THRESHOLD", "0.822"))
RELEVANCE_Z_MIN = float(os.getenv("RELEVANCE_Z_MIN", "2.0"))
RELEVANCE_MARGIN = float(os.getenv("RELEVANCE_MARGIN", "0.03"))
ENTITY_FOCUS = os.getenv("ENTITY_FOCUS", "1") == "1"
RARE_TOKEN_IDF = float(os.getenv("RARE_TOKEN_IDF", "3.0"))
PHRASE_MAX_DF = int(os.getenv("PHRASE_MAX_DF", "10"))
LEXICAL_COVERAGE_MIN = float(os.getenv("LEXICAL_COVERAGE_MIN", "0.28"))

WEB_HOST = os.getenv("WEB_HOST", "0.0.0.0")
WEB_PORT = int(os.getenv("WEB_PORT", "8000"))

SYSTEM_PROMPT = (
    "Ты — агент, который внимательно слушает пользователя и выполняет поставленные им задачи. "
    "Отвечай по делу, без самолюбования и без лишних представлений."
)

LANGUAGES = {
    "ru": {
        "label": "Русский",
        "instruction": (
            "Всегда отвечай на русском языке. Если пользователь прямо просит ответить "
            "на другом языке, отвечай на том языке, который он попросил."
        ),
    },
    "ja": {
        "label": "日本語",
        "instruction": (
            "Всегда отвечай на японском языке (日本語). Если пользователь прямо просит "
            "ответить на другом языке, отвечай на том языке, который он попросил. "
            "常に日本語で回答してください。ただし、ユーザーが別の言語での回答を明示的に"
            "求めた場合は、その言語で回答してください。"
        ),
    },
}

DEFAULT_LANGUAGE = "ru"

FACT_RULES = (
    "Если не уверен в факте — скажи меньше или честно ответь, что не знаешь. "
    "Не приписывай одной организации, продукту или человеку факты о другой, "
    "даже если они упомянуты рядом в справочных материалах. Не выдумывай названия, "
    "даты, цифры и услуги."
)

STRICT_GROUNDING = (
    "Отвечай только на основе справочных материалов выше. Если в них нет ответа, "
    "прямо скажи, что в базе знаний этого нет, и не добавляй фактов от себя."
)

CONTEXT_HEADER = (
    "СПРАВОЧНЫЕ МАТЕРИАЛЫ (это твои внутренние заметки, а не часть диалога). "
    "Используй их, если они относятся к вопросу."
)

CONTEXT_FOOTER = (
    "КОНЕЦ СПРАВОЧНЫХ МАТЕРИАЛОВ. Никогда не пересказывай и не цитируй их целиком, "
    "не упоминай сам факт их наличия и не вставляй в ответ заголовки вроде "
    "«Справочные материалы» или «Информация для ответа». "
    "Отвечай только на заданный вопрос."
)

DRAFT_SYSTEM_PROMPT = (
    "Ты помогаешь оператору переписки составить черновик ответа в характерном для "
    "аккаунта стиле, описанном ниже. Ты не отправляешь сообщение сам — только "
    "предлагаешь текст, который человек прочитает, при необходимости отредактирует "
    "и отправит сам. Если во входящем сообщении есть оскорбления, домогательства "
    "или неприемлемые темы — не отвечай тем же тоном: предложи спокойный ответ, "
    "который обозначает границу и уводит разговор в приемлемое русло. Дай один "
    "вариант текста, без пояснений и без нескольких вариантов на выбор."
)

DRAFT_TEMPERATURE = float(os.getenv("DRAFT_TEMPERATURE", "0.6"))

TEMPERATURE = float(os.getenv("TEMPERATURE", "0.3"))

RAG_DOMAINS = ALL_DOMAINS

MODELS = {
    "flock": {
        "label": "FLOCK",
        "ollama_model": os.getenv("FLOCK_OLLAMA_MODEL", "gemma3:1b"),
        "governance_only": False,
        "rag_limit": int(os.getenv("FLOCK_RAG_LIMIT", "2")),
        "rag_margin": float(os.getenv("FLOCK_RAG_MARGIN", "0.08")),
        "history_limit": int(os.getenv("FLOCK_HISTORY_LIMIT", "4")),
        "temperature": float(os.getenv("FLOCK_TEMPERATURE", "0.3")),
        "num_predict": int(os.getenv("FLOCK_MAX_TOKENS", "320")),
        "style": STRICT_GROUNDING,
        "compact": False,
    },
    "kriloud-flash": {
        "label": "Flash",
        "ollama_model": os.getenv("FLASH_OLLAMA_MODEL", OLLAMA_MODEL),
        "governance_only": False,
        "rag_limit": int(os.getenv("FLASH_RAG_LIMIT", "1")),
        "rag_margin": None,
        "history_limit": int(os.getenv("FLASH_HISTORY_LIMIT", "2")),
        "temperature": float(os.getenv("FLASH_TEMPERATURE", "0.1")),
        "num_predict": int(os.getenv("FLASH_MAX_TOKENS", "600")),
        "style": None,
        "compact": True,
    },
}

DEFAULT_MODEL = "flock"

FLASH_SYSTEM_PROMPT = (
    "Ты быстрый ассистент. Отвечай одним-двумя короткими предложениями, сразу по сути. "
    "Если нужна команда или код — дай только её, одной строкой."
)
FLASH_HINT_CHARS = int(os.getenv("FLASH_HINT_CHARS", "600"))

RAG_PROMPT_SUFFIX = (
    "Ниже почти всегда дан контекст из базы знаний. Доверяй ему больше, "
    "чем собственным знаниям, и следуй ему как можно точнее. "
    "Используй собственные знания, если контекст не относится к вопросу или неполон."
)


def model_request(model_id: str, history: list[dict] | None) -> dict:
    model = MODELS.get(model_id, MODELS[DEFAULT_MODEL])
    if history and model["history_limit"] is not None:
        history = history[-model["history_limit"]:] if model["history_limit"] > 0 else []
    options = {"num_predict": model["num_predict"]} if model["num_predict"] else None
    return {
        "history": history,
        "ollama_model": model["ollama_model"],
        "max_hints": model["rag_limit"],
        "rag_margin": model["rag_margin"],
        "temperature": model["temperature"],
        "options": options,
        "client_system": model["style"],
        "compact": model["compact"],
    }
