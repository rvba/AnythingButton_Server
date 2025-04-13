---
title: DeepSeekV3-API
emoji: 📚
colorFrom: blue
colorTo: red
sdk: docker
pinned: false
---

### Alternative to Open AI Model
Use generate for Mixtral-8x7B-Instruct and generate_deepseek DeepSeek-V3. Default to DeepSeek.

## Usage
* Huggingface Space - Docker Template - Upload Files
* Settings - New Secret. Set 'HF_TOKEN' after obtaining gated access to the desirable model.
* Modify system prompt in agent.py
* Change model as necessary in generate.py
* Make Request
```bash
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{
        "prompt": "Please make a script that says hello world in C#.""
      }' \
  https://pinlpt-mixtral-8x7b-api.hf.space/generate/
'''
