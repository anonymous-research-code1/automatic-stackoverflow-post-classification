import time
from selenium.webdriver.common.by import By
from selenium import webdriver
import pandas as pd

df = pd.read_csv("torch_dataset.csv")
driver = webdriver.Chrome()
base_url = 'https://stackoverflow.com/questions/'

for idx, row in df.iterrows():
    try:
        if(row['answer'].startswith("Your Answer")):  ###some questions do not have answer. they start with 'Your Answer', meaning to input answer
            print(idx, row['id'])
            # continue
            df.at[idx, 'answer'] = None
            df.to_csv("merged_torch_updated.csv", index=False)

        if pd.notnull(row['answer']):
            continue
        
    except: #initially there is no column answer. This block will be activated for the first run
        pass 
    id = row['id']
    url = base_url + str(id)
    driver.get(url)
    time.sleep(2)

    elements = driver.find_elements(By.XPATH, "//*[contains(@id, 'answer-')]")
    answer = None

    if len(elements) > 1:
        try:
            answer = elements[1].text.split("""Share
        Improve this answer
        Follow""")[0]
        except Exception as e:
            print(f"Error scraping answer for ID {id}: {e}")

    df.at[idx, 'answer'] = answer
    # df.to_csv("merged_torch_updated.csv", index=False)

driver.quit()
