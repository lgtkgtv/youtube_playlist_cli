# ⚙️ Auto-Fuzzing Harness Generation (libFuzzer)

## Objective
Generate fuzz harness for parsers/APIs using libFuzzer-compatible syntax.

## Sections
1. **Describe the target** (C/C++ function, CLI parser)
2. **Generate `extern "C" int LLVMFuzzerTestOneInput`**
3. **Seed corpus setup**
4. **libFuzzer command-line hints**
5. **CI integration tips**

## Prompt Starter
```
Write a libFuzzer harness for a C++ function that parses JSON into structs.
```
