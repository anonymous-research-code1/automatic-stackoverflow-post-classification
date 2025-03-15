import pandas as pd
def process_answer(value, idx):
    try:
        return "\n".join(value.split("\n")[1:])
    except Exception as e:
        print(f"Index {idx}: {value}", end = "\n-----------------------\n") #For nan instances (no answer)
        return value

df = pd.read_csv("merged_tf_keras_with_ans_summary.csv")
df['answer'] = [
    process_answer(value, idx) for idx, value in enumerate(df['answer'])
] #remove the number (upvote) infront of the answer
df.to_csv("merged_tf_keras_with_ans_summary.csv", index=False)
