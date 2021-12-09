from transformers import PegasusForConditionalGeneration, AutoTokenizer
# import torch


def text_summerize(src_text):

  model_name = 'google/pegasus-xsum'

  device = 'cpu'

  tokenizer = AutoTokenizer.from_pretrained(model_name)

  model = PegasusForConditionalGeneration.from_pretrained(model_name).to(device)

  batch = tokenizer(src_text, truncation=True, padding='longest', return_tensors="pt").to(device)
  
  translated = model.generate(**batch)
  
  return tokenizer.batch_decode(translated, skip_special_tokens=True)

def summarize(txt):

    summary = text_summerize(txt)[0]

    return summary

def startpy():

    txt = 'Marvel Studios Eternals is now the worst reviewed film in the Marvel Cinematic Universe, as per review aggregation site Rotten Tomatoes. After 92 reviews, this Chloe Zhao directorial has a score of 64 per cent, which is lower than Thor: Dark World, the movie which previously held the record for the lowest Rotten Tomatoes score for an MCU movie.Of course, the score can change significantly in either direction once the film is out in theatres and more critics get to see it. But one thing is certain, the film has divided critics like no other MCU film.'

    summary = summarize(txt)

    print (summary)


if __name__=='__main__':

    startpy()