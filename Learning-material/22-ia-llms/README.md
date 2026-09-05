# 22 · IA y LLMs en tu app

Integrar modelos de lenguaje en una aplicación como una pieza más: chat, streaming, RAG (darle tu información) y function calling (que ejecute acciones). Agnóstico: Claude y OpenAI.

## Qué hay acá
- `manual.html` — 8 capítulos: un LLM es una API, prompts/roles/tokens, streaming, RAG (con retrieval probado), function calling (con dispatch probado), seguridad y costos (prompt injection, alucinaciones), y checklist. Cierra la colección.
- `ejemplos/llm.py` — chat y streaming con Claude y OpenAI (credential-gated), y el dispatch de function calling (probado sin API key).
- `ejemplos/rag.py` — recuperación de RAG con TF-IDF (corre sin API key); en producción se usan embeddings.
- `ejemplos/pruebas.txt` — salida real: retrieval de RAG y dispatch de function calling.

## Probar
```
pip install scikit-learn
python3 -c "import rag; r=rag.Recuperador(rag.DOCUMENTOS); print(r.buscar('¿cómo pago?'))"
# chat con LLM real: pip install anthropic  (y export ANTHROPIC_API_KEY=...)
```
