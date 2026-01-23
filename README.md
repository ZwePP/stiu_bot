### Install Requirements
```
pip install -r requirements.txt

```
If having a pip issue with pywinpty.
Delete it from requirements.txt


### Local LLM
Install ollama to run LLM locally .

```
ollama run mistral
```
To install Mistral. 

After installing requirements and LLM.

### How to run
1) To upload Handbook PDF to ChromaDB
```
python -m core.main
```
2) Running a bot in console
```
python -m core.rag
```