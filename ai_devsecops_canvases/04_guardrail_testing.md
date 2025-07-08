# 🛡️ Model Input/Output Guardrail Testing

## Objective
Test LLM outputs against guardrail policies.

## Sections
1. **Inject adversarial inputs (jailbreak, PII)**
2. **Run through model (OpenAI, DeepSeek, etc.)**
3. **Pass output to LLMGuard, Garak, LlamaGuard**
4. **Score for safety / leakage**
5. **Generate Markdown report**

## Prompt Starter
```
Is there any private info in this LLM response? Use LLMGuard + Regex filters to check.
```
