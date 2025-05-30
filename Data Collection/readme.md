# StackExchange Dataset Collection

This project helps you collect and clean a dataset of answers from StackExchange using a predefined query.

---

## Step 1: Prepare the Query

1. Open the file `stack_exchange_query.pdf`.
2. It contains:
   - A StackExchange **search link**.
   - A **query** to retrieve relevant posts for dataset creation.
---

## Step 2: Scrape Answers

Use the script below to collect answers (solutions) from StackExchange and remove the number (upvote) from answer:

```bash
python scrap_train_answer.py
python remove_number_from_answer.py
