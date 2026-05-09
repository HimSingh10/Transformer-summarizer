from transformers import pipeline

print("Loading model...")

summarizer = pipeline("summarization", model="t5-small")

print("Model loaded successfully!")

text = """
Artificial Intelligence (AI) is revolutionizing industries across the globe. It allows machines to learn from data,
identify patterns, and make decisions with minimal human intervention. From healthcare to finance, AI is being used
to improve efficiency, reduce costs, and enhance customer experiences. However, it also raises ethical concerns
regarding privacy, job displacement, and decision-making transparency.
"""

print("Generating summary...")

result = summarizer(text, max_length=25, min_length=10, do_sample=False)

print("Summary:")
print(result[0]['summary_text'])