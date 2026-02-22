from langchain_ollama import OllamaLLM
from src.retriever import load_retriever


def generate_answer(question, chroma_directory, embedding_model, language_model, ollama_host):
    """
    generate an answer to a recipe question.

    Args:
        question (str): user question
        chroma_directory (str): path to chromadb 
        embedding_model (str): embedding model name
        language_model (str): llm model name

    Returns:
        dict: answer and recipe titles
    """

    llm = OllamaLLM(model=language_model, base_url=ollama_host)
    retriever = load_retriever(chroma_directory, embedding_model, ollama_host)

    search_query = llm.invoke(
        f"rewrite this as a short recipe search query, return only the query:\n{question}"
    )
    docs = retriever.invoke(search_query)

    context_parts = []
    for doc in docs:
        context_parts.append(doc.page_content)
    context = "\n\n".join(context_parts)

    sources = []
    for doc in docs:
        sources.append(doc.metadata["title"])

    prompt = f"""you are a helpful cooking assistant for a recipe website.
    a user asked you a question and you have retrieved the most relevant recipes from the database.
    use only the recipes provided below to answer the question.
    if the user lists ingredients they have, suggest which recipes they can make and what they might be missing.
    if the user asks about a specific recipe, give them detailed information about it.
    always mention the recipe name in your answer.
    be concise and practical.

retrieved recipes:
{context}

user question: {question}

your answer:"""

    answer_text = llm.invoke(prompt)

    return {
        "answer": answer_text,
        "sources": sources,
    }