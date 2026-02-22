import re
import json
from langchain_core.documents import Document


def load_recipes(filepath):
    """
    Load and clean recipes from a json file.

    Args:
        filepath (str): path to the json recipe file

    Returns:
        list[Document]: cleaned recipe documents
    """
    with open(filepath, "r") as f:
        data = json.load(f)

    documents = []

    for recipe in data.values():
        title = (recipe.get("title") or "").strip()
        instructions = (recipe.get("instructions") or "").strip().split("\n")[0]
        ingredients_raw = recipe.get("ingredients") or []

        if not title or not instructions:
            continue

        seen = set()
        ingredients = []
        for ing in ingredients_raw:

            #while scraping ad text was injected into ingredient strings
            ing = re.sub(r"advertisement", "", ing, flags=re.IGNORECASE).strip()
            if ing and ing not in seen:
                seen.add(ing)
                ingredients.append(ing)

        if len(ingredients) < 2:
            continue

        documents.append(Document(
            page_content=(
                f"title: {title}\n"
                f"ingredients: {', '.join(ingredients)}\n"
                f"instructions: {instructions}"
            ),
            metadata={
                "title": title,
                "source": filepath,
                "ingredients": ", ".join(ingredients),
            },
        ))

    return documents