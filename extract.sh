FILENAME=testmini_text_ans
echo /home/yerong2/MathVerse/data/${FILENAME}_extraction.json
python evaluation/extract_answer_s1.py \
	--model_output_file /home/yerong2/MathVerse/data/$FILENAME.json \
	--save_file /home/yerong2/MathVerse/data/${FILENAME}_extraction.json\
	--cache \
	--trunk_response 30 \
	--save_every 20 \
	--api_key $OPENAIKEY
