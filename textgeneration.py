import markovify

# Read dataset
with open("story.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Train Markov model
model = markovify.Text(text, state_size=1)

print("Generated Text:\n")

generated_text = ""

for i in range(30):
    sentence = model.make_short_sentence(120)

    if sentence:
        print(sentence)
        generated_text += sentence + "\n"

# Save generated text
with open("generated_text.txt", "w", encoding="utf-8") as f:
    f.write(generated_text)

print("\nGenerated text saved as generated_text.txt")