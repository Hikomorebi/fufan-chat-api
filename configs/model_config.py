import os

MODEL_ROOT_PATH = ""

TEMPERATURE = 1.0
MAX_TOKENS = 4096
# 默认让大模型采用流式输出
STREAM = True

# 默认启动的模型，如果使用的是其他模型，请替换模型名称
LLM_MODELS = ["zhipu-api"]

RERANKER_MODEL = "bge-reranker-large"
RERANKER_MAX_LENGTH = 1024
# 是否启用reranker模型
USE_RERANKER = True

# 知识库匹配向量数量
VECTOR_SEARCH_TOP_K = 5
# 知识库匹配的距离阈值，一般取值范围在0-1之间，SCORE越小，距离越小从而相关度越高。
SCORE_THRESHOLD = 1.0
# 如果使用ReRank模型
RERANKER_TOP_K = 3

# 搜索引擎匹配结题数量
SEARCH_ENGINE_TOP_K = 3

MODEL_PATH = {
    # 这里定义 本机服务器上存储的大模型权重存储路径
    "local_model": {
        "qwen2_5-7b-instruct": "/home/hkb/hf_models/Qwen2.5-7B-Instruct",
        # 可扩展其他的开源大模型

    },

    # 这里定义 本机服务器上存储的Embedding模型权重存储路径
    "embed_model": {
        "bge-large-zh-v1.5": "/home/hkb/hf_models/bge-large-zh-v1.5",
        # 可扩展其他的Embedding模型
    },

    "reranker": {
        "bge-reranker-large": "/home/hkb/hf_models/bge-reranker-large",

    }
}

ONLINE_LLM_MODEL = {

    # 智谱清言的在线API服务
    "zhipu-api": {
        "api_key": "09dca6001dd34c899267b60fb716085d.XVRP0859K188eyR0",
        "version": "glm-4",
        "provider": "ChatGLMWorker",
    },

    # 可扩展其他的模型在线模型

}

SUPPORT_AGENT_MODEL = [
    "openai-api",  # GPT4 模型
    "qwen-api",  # Qwen Max模型
    "zhipu-api",  # 智谱AI GLM4模型
    "Qwen",  # 所有Qwen系列本地模型
    "chatglm3-6b",
    "internlm2-chat-20b",
    "Orion-14B-Chat-Plugin",
]

# 选用的 Embedding 名称
EMBEDDING_MODEL = "bge-large-zh-v1.5"

# Embedding 模型运行设备。设为 "auto" 会自动检测(会有警告)，也可手动设定为 "cuda","mps","cpu","xpu" 其中之一。
EMBEDDING_DEVICE = "auto"

# 搜索引擎匹配结题数量
SEARCH_ENGINE_TOP_K = 3

# 原始网页搜索结果筛选后保留的有效数量
SEARCH_RERANK_TOP_K = 3

# 历史对话窗口长度
HISTORY_LEN = 5

URL = "https://google.serper.dev/search"
SERPER_API_KEY = "d59c7338ae72d4d4fdd3e39ead6fa9092f3c84f8"  # 这里替换为自己实际的Serper API Key
