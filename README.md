IASO
====

IASO/demo/operation.py
-------
A demo for IASO, run operation.py to get the result for an example input "宝宝腹痛" <br>

IASO/demo/disease.owl
-------
Our ontology file

IASO/demo/Word2Vec/usingWikiAlias
-------
To get the alias for symptom according to Wiki corpus<br>
Here is an examle:
```python
from Word2Vec import usingWikiAlias
match_result = usingWikiAlias.alias(symptom)




