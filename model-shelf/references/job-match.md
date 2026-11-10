# Job match

How Model Shelf answers the job the user typed. Read this before Step 5.

## What the user gives

A job in plain words, for example a small chat model for client work, or a model that describes photos. Optionally a memory budget in GB.

## Who does what

- The document expert reads the model cards on the NAS in Step 3, including the cards beside parked models. It names each need in the job, quotes the lines about use, languages, memory and license, and says which cards state a use that covers each need.
- The parent does not add to that. It arranges the expert's matches, adds the file sizes from Step 1, and writes the answer below.

## Rules

1. Split the job into needs, as the expert named them. A job such as a small coding model and a speech to text model holds two needs.
2. Only models that have a name can be matched. A file that is not identified has no card to read, so list it under Could not match with the reason.
3. A model fits a need only when a quoted card line states a use that covers it. Show that line in quotation marks with the file it came from. If the card says nothing about use, write use not stated and do not count it as a fit.
4. For each need, use the first outcome that holds:
   - On the shelf. A model in an active model folder fits. Show it.
   - Parked. A parked model fits and nothing on the shelf does. Show it and put a bring back line in the plan.
   - What to get. Nothing the user owns fits. Write the What to get section from model-guide.md.
5. If the user gave a memory budget, put the file size and any quoted memory line beside the budget. Say whether the file size is under or over the budget. This is arithmetic on file size only. It does not promise that the model will run.
6. Order the fits by how directly the quoted line covers the need, then by smaller file size.

## What to get

- Write it only for needs that nothing the user owns covers.
- Take every model from model-guide.md and from nowhere else. Never name a model that is not in the guide.
- For each pick, show the model id, its task, the license as listed, its size against the budget, and the access note. Add the date the guide was checked.
- Say plainly that Model Shelf does not download models. The user downloads from the model page, puts the file in a model folder, and runs Model Shelf again.
- If no guide entry covers the need, say the guide has no entry for it, then say what to look for: the task, a file size under the budget, and a license line to read first.

## License lines

People who do client work need to see the license line before they pick a model. Model Shelf shows it and stops there.

- Quote the exact license line and name its source, which is either the model card or the file header.
- If the header and the card state different license strings, show both and say they differ.
- If neither states one, write no license line found.
- Add this sentence once under the job answer: Model Shelf quotes license lines and does not interpret them. This is not legal advice. Read the full license before you rely on it.
- Do not describe a model as fine or not fine for any use. Do not rank models by license. The user decides.

## Layout of the job answer

```text
For your job: a small coding model and a speech to text model, memory budget 4 GB

Need 1. A small coding model
- On the shelf, or Parked (bring it back, see the plan): MODEL NAME (FILE NAME, SIZE)
  Use, quoted from CARD FILE: "EXACT LINE"
  Memory, quoted from CARD FILE: "EXACT LINE". File size is under the 4 GB budget.
  License line, from CARD FILE: "EXACT LINE"

Need 2. A speech to text model
- Nothing you own covers this need.

Did not fit
- MODEL NAME. Use, quoted from CARD FILE: "EXACT LINE"

Could not match
- FILE NAME. Not identified, so there is no card to read.

What to get (from the Model Shelf guide, checked on GUIDE DATE)
- For need 2: MODEL ID. Task: TASK. License as listed: LICENSE. Size: SIZE, under or over your budget. Access: ACCESS NOTE.
Model Shelf does not download models. Download it from its model page, put it in a model folder, and run Model Shelf again.

Model Shelf quotes license lines and does not interpret them. This is not legal advice. Read the full license before you rely on it.
```

The words in capital letters in this layout are filled with real values from Steps 1 to 4 and from the guide.
