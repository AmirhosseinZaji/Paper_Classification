import tiktoken
import os


def count_tokens(text):
    # Initialize the tokenizer for a specific OpenAI model (e.g., gpt-3.5-turbo or gpt-4)
    encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")

    # Tokenize the text
    tokens = encoding.encode(text)

    # Return the length of the tokens
    return len(tokens)


def process_files(input_folder, output_file):
    with open(output_file, 'w') as out_file:
        for filename in os.listdir(input_folder):
            if filename.endswith(".txt"):
                file_path = os.path.join(input_folder, filename)
                with open(file_path, 'r', encoding='utf-8') as file:
                    text = file.read()
                    token_count = count_tokens(text)
                    out_file.write(f"{filename}: {token_count}\n")
                    print(f"Processed {filename}: {token_count} tokens")


if __name__ == "__main__":
    input_folder = "papers/txts"
    output_file = "papers/token_counts.txt"
    process_files(input_folder, output_file)
