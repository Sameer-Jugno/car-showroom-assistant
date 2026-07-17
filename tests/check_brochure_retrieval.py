from app.rag.retriever import retrieve

results = retrieve("What features does the Hyundai Creta have?")
for r in results:
    print(r.score, "-", r.text[:200])
    print("---")