# Better instruction training data for LLMs 
This is an attempt to create a high-quality and open database of instructions to fine-tune LLMs on. It's based on the original dataset from https://github.com/tatsu-lab/stanford_alpaca and is meant to improve on it. 

Most of the data was generated unsupervised by a LLM (`text-davinci-003`), which, while cheap, isn't always free of errors and does not always meet high quality standards. By creating an open and curated dataset, we're hoping to bring humans into the loop and support a wider range of verification and generation methods. This might also help close the gap to commercial and closed datasets.

Example:
```
{
  "id": "0a0cd377-0c86-4247-b2ca-454b4327748d",
  "instruction": "Given a general topic, write a paragraph about it.",
  "input": "Friendship",
  "output": "Friendship is one of life's most cherished gifts. It is the bond between two people formed out of unconditional love and understanding, no matter the distance or time apart. True friends can make a rainy day seem brighter with their optimism and their ability to make the best out of any situation. They support each other through thick and thin, never abandoning each other. Good friends will never deliberately hurt each other and will always come to the aid of one another. Friends are people who we can trust and depend on, who always have our back. Friendship takes dedication and patience, but with the right attitude it can become a lifelong bond that brings people together forever.",
  "license": "stanford-alpaca-unknown",
  "generation-type": "openai-text-davinci-003",
  "generation-reference": "https://github.com/tatsu-lab/stanford_alpaca/blob/main/alpaca_data.json",
  "modified": [],
  "verified": [],
  "tags": []
}
```

## Tenets
- Human verification is best, but automated verification is better than nothing
- Source data is cheap. If it's too hard to fix a given instruction, it should be deleted
- Metadata should be as clean as possible

## Licensing
Using LLM generated text as training data for other LLMs might violate the usage terms of the original LLM owner and its legal position is unclear to me. Human provided text in this repository should be under an open license. 

The `license` field on each instruction is meant to capture this in a machine-readable way. 

## Metadata
Metadata fields are meant to be machine readable, so it'll be useful to keep them consistent. However, since this repository is relatively new, these conventions need to be established first. Here are some suggestions: 

### `generation-type` and `generation-reference`
These fields contain information of where the instruction has been sourced or generated from. These should not be updated when instructions are modified.
### `modified` and `verified` 
These are meant to be arrays of how (if at all) a given instruction has been verified or modified. Suggested fields: `human`, `openai-text-davinci-003`, `my-custom-script-x`, etc. 
### `tags` 
Not currently used, but meant to annotate the topic of an instructions. For example `maths`, `rhyming`, etc.  

## Full data

You can find a full and combined version of this data [here https://github.com/marekventur/better-instructions/blob/main/generated/full.json?raw=true.] A queryable datasette-lite version can be accessed [here https://lite.datasette.io/?json=https://github.com/marekventur/better-instructions/blob/main/generated/full.json?raw=true]

## How to contribute
- Fork this repository
- Modify instructions (they're all in `./data/`)
- Commit and push
- Send pull request back to this repository

## Tooling
This repository is meant to contain only the data (and related scripts for validation and assembly). Tools to help filter, generate and verify should be hosted independently. 

<TBD: Add list of tools>

## Todo
- Write tool: UI to walk through random instructions and allow users to rate and modify
- Write tool: Use other LLMs to assess quality of existing prompts
- Add automatically updated counter to README
