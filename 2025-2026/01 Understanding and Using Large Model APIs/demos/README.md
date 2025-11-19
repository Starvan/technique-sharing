# demos

如果需要安装环境，尝试下面的命令：

```bash
python -m venv .venv   
source ./.venv/bin/activate  
pip install requests python-dotenv
```

参考的JSON：

```json
data: {
  "id": "019a8fdafd091c809cf14705cced6e75",
  "object": "chat.completion.chunk",
  "created": 1763350084,
  "model": "Qwen/Qwen2.5-7B-Instruct",
  "choices": [
    {
      "index": 0,
      "delta": {
        "content": "",
        "reasoning_content": null,
        "role": "assistant"
      },
      "finish_reason": null
    }
  ],
  "system_fingerprint": "",
  "usage": {
    "prompt_tokens": 30,
    "completion_tokens": 0,
    "total_tokens": 30
  }
}

data: {
  "id": "019a8fdafd091c809cf14705cced6e75",
  "object": "chat.completion.chunk",
  "created": 1763350084,
  "model": "Qwen/Qwen2.5-7B-Instruct",
  "choices": [
    {
      "index": 0,
      "delta": {
        "content": "你好",
        "reasoning_content": null
      },
      "finish_reason": null
    }
  ],
  "system_fingerprint": "",
  "usage": {
    "prompt_tokens": 30,
    "completion_tokens": 1,
    "total_tokens": 31
  }
}

data: {
  "id": "019a8fdafd091c809cf14705cced6e75",
  "object": "chat.completion.chunk",
  "created": 1763350084,
  "model": "Qwen/Qwen2.5-7B-Instruct",
  "choices": [
    {
      "index": 0,
      "delta": {
        "content": "！",
        "reasoning_content": null
      },
      "finish_reason": null
    }
  ],
  "system_fingerprint": "",
  "usage": {
    "prompt_tokens": 30,
    "completion_tokens": 2,
    "total_tokens": 32
  }
}

data: {
  "id": "019a8fdafd091c809cf14705cced6e75",
  "object": "chat.completion.chunk",
  "created": 1763350084,
  "model": "Qwen/Qwen2.5-7B-Instruct",
  "choices": [
    {
      "index": 0,
      "delta": {
        "content": "有什么",
        "reasoning_content": null
      },
      "finish_reason": null
    }
  ],
  "system_fingerprint": "",
  "usage": {
    "prompt_tokens": 30,
    "completion_tokens": 3,
    "total_tokens": 33
  }
}

data: {
  "id": "019a8fdafd091c809cf14705cced6e75",
  "object": "chat.completion.chunk",
  "created": 1763350084,
  "model": "Qwen/Qwen2.5-7B-Instruct",
  "choices": [
    {
      "index": 0,
      "delta": {
        "content": "问题",
        "reasoning_content": null
      },
      "finish_reason": null
    }
  ],
  "system_fingerprint": "",
  "usage": {
    "prompt_tokens": 30,
    "completion_tokens": 4,
    "total_tokens": 34
  }
}

data: {
  "id": "019a8fdafd091c809cf14705cced6e75",
  "object": "chat.completion.chunk",
  "created": 1763350084,
  "model": "Qwen/Qwen2.5-7B-Instruct",
  "choices": [
    {
      "index": 0,
      "delta": {
        "content": "或者",
        "reasoning_content": null
      },
      "finish_reason": null
    }
  ],
  "system_fingerprint": "",
  "usage": {
    "prompt_tokens": 30,
    "completion_tokens": 5,
    "total_tokens": 35
  }
}

data: {
  "id": "019a8fdafd091c809cf14705cced6e75",
  "object": "chat.completion.chunk",
  "created": 1763350084,
  "model": "Qwen/Qwen2.5-7B-Instruct",
  "choices": [
    {
      "index": 0,
      "delta": {
        "content": "需要",
        "reasoning_content": null
      },
      "finish_reason": null
    }
  ],
  "system_fingerprint": "",
  "usage": {
    "prompt_tokens": 30,
    "completion_tokens": 6,
    "total_tokens": 36
  }
}

data: {
  "id": "019a8fdafd091c809cf14705cced6e75",
  "object": "chat.completion.chunk",
  "created": 1763350084,
  "model": "Qwen/Qwen2.5-7B-Instruct",
  "choices": [
    {
      "index": 0,
      "delta": {
        "content": "帮助",
        "reasoning_content": null
      },
      "finish_reason": null
    }
  ],
  "system_fingerprint": "",
  "usage": {
    "prompt_tokens": 30,
    "completion_tokens": 7,
    "total_tokens": 37
  }
}

data: {
  "id": "019a8fdafd091c809cf14705cced6e75",
  "object": "chat.completion.chunk",
  "created": 1763350084,
  "model": "Qwen/Qwen2.5-7B-Instruct",
  "choices": [
    {
      "index": 0,
      "delta": {
        "content": "的",
        "reasoning_content": null
      },
      "finish_reason": null
    }
  ],
  "system_fingerprint": "",
  "usage": {
    "prompt_tokens": 30,
    "completion_tokens": 8,
    "total_tokens": 38
  }
}

data: {
  "id": "019a8fdafd091c809cf14705cced6e75",
  "object": "chat.completion.chunk",
  "created": 1763350084,
  "model": "Qwen/Qwen2.5-7B-Instruct",
  "choices": [
    {
      "index": 0,
      "delta": {
        "content": "吗",
        "reasoning_content": null
      },
      "finish_reason": null
    }
  ],
  "system_fingerprint": "",
  "usage": {
    "prompt_tokens": 30,
    "completion_tokens": 9,
    "total_tokens": 39
  }
}

data: {
  "id": "019a8fdafd091c809cf14705cced6e75",
  "object": "chat.completion.chunk",
  "created": 1763350084,
  "model": "Qwen/Qwen2.5-7B-Instruct",
  "choices": [
    {
      "index": 0,
      "delta": {
        "content": "？",
        "reasoning_content": null
      },
      "finish_reason": null
    }
  ],
  "system_fingerprint": "",
  "usage": {
    "prompt_tokens": 30,
    "completion_tokens": 10,
    "total_tokens": 40
  }
}

data: {
  "id": "019a8fdafd091c809cf14705cced6e75",
  "object": "chat.completion.chunk",
  "created": 1763350084,
  "model": "Qwen/Qwen2.5-7B-Instruct",
  "choices": [
    {
      "index": 0,
      "delta": {
        "content": "",
        "reasoning_content": null
      },
      "finish_reason": "stop" # 逻辑上的完成
    }
  ],
  "system_fingerprint": "",
  "usage": {
    "prompt_tokens": 30,
    "completion_tokens": 10,
    "total_tokens": 40
  }
}

data: [DONE]

```
