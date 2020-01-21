# FinSentiment
Collection of sentiment models commonly used in Finance.

## Implementations
1. (LM) Loughran-McDonald
2. (HV) Harvard General Inquirer IV4

## Example Usage
```python
from finsentiment import LM
mdl = LM()
text = '''
  Global and regional economic conditions could materially adversely affect the Company’s business, results of operations, financial condition and growth.
'''
print(mdl.sentiment(text))
>>> -1.0
```
