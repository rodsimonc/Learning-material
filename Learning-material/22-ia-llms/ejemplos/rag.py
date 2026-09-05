"""
RAG (Retrieval-Augmented Generation): darle al LLM tu información propia.
El truco: NO le mandás todos tus documentos (no entran y sale caro). Buscás
los fragmentos más relevantes a la pregunta, y solo esos se los pasás al LLM
como contexto. Acá probamos la parte de recuperación (retrieval), que es la
que hace que RAG funcione. La generación final la hace el LLM (llm.py).

Nota: en producción se usan "embeddings" (vectores semánticos) de un modelo.
Acá usamos TF-IDF, que captura la misma idea (similitud por contenido) y se
puede correr y probar sin API key. El mecanismo de "buscar lo relevante y
pasarlo como contexto" es idéntico.
"""
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# La "base de conocimiento": fragmentos de la info de la tienda.
DOCUMENTOS = [
    "Podés pagar con MercadoPago, con QR o con transferencia bancaria.",
    "El horario de atención es de 12 a 15 y de 20 a 24, todos los días.",
    "El envío es gratis dentro del barrio para pedidos mayores a 15000 pesos.",
    "Las reservas de mesa se toman hasta para 6 personas por franja horaria.",
    "Los productos sin gluten (sin TACC) están marcados con etiqueta verde.",
]


class Recuperador:
    def __init__(self, documentos):
        self.docs = documentos
        # strip_accents ayuda con tildes; el resto es matching por palabras
        self.vec = TfidfVectorizer(strip_accents="unicode")
        self.matriz = self.vec.fit_transform(documentos)

    def buscar(self, pregunta: str, k: int = 2):
        """Devuelve los k fragmentos más relevantes a la pregunta."""
        q = self.vec.transform([pregunta])
        sims = cosine_similarity(q, self.matriz)[0]
        mejores = sims.argsort()[::-1][:k]
        return [(self.docs[i], round(float(sims[i]), 3)) for i in mejores]


def armar_prompt(pregunta: str, fragmentos: list[str]) -> str:
    """El prompt que se le manda al LLM: contexto recuperado + la pregunta."""
    contexto = "\n".join(f"- {f}" for f in fragmentos)
    return (f"Respondé usando SOLO este contexto:\n{contexto}\n\n"
            f"Pregunta: {pregunta}")
