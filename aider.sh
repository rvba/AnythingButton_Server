#!/bin/bash
prompt=$(cat prompt_request.txt)
targetfile=AnythingButton_ResultsComponent.cs
echo "prompt:" $prompt
echo "running aider ..."
cd AnythingButton_Results
docker run -it --user $(id -u):$(id -g) --volume $(pwd):/app paulgauthier/aider --openai-api-key $OPENAI_API_KEY --message "$prompt" $targetfile
#echo "committing"
#git commit -m "$prompt"
echo "pushing"
git push

