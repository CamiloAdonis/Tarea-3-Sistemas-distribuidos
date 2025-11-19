-- Cargar datos
raw_data = LOAD '/input/responses_export.csv' USING PigStorage(',') AS (
    id:chararray, question_title:chararray, question_content:chararray,
    best_answer:chararray, llm_answer:chararray, cosine_score:chararray,
    rouge_score:chararray, length_score:chararray, question_hash:chararray,
    access_count:chararray, created_at:chararray
);

-- Filtrar header
clean_data = FILTER raw_data BY id != 'id' AND best_answer IS NOT NULL AND llm_answer IS NOT NULL;

-- Separar respuestas (convertir a minúsculas)
yahoo_responses = FOREACH clean_data GENERATE LOWER(best_answer) AS text;
llm_responses = FOREACH clean_data GENERATE LOWER(llm_answer) AS text;

-- Procesar Yahoo CON TODOS LOS FILTROS
yahoo_words = FOREACH yahoo_responses GENERATE FLATTEN(TOKENIZE(text)) AS word;
yahoo_clean = FILTER yahoo_words BY 
    SIZE(word) > 2 AND
    word MATCHES '^[a-z]+$' AND
    NOT (word MATCHES 'el|la|los|las|de|del|y|en|un|una|que|es|se|con|por|para|the|and|of|to|a|in|is|it|you|that|he|was|for|on|are|as|with|his|they|i|at|be|this|have|from');
yahoo_group = GROUP yahoo_clean BY word;
yahoo_count = FOREACH yahoo_group GENERATE group AS palabra, COUNT(yahoo_clean) AS frecuencia;
yahoo_sorted = ORDER yahoo_count BY frecuencia DESC;

-- Procesar LLM CON TODOS LOS FILTROS
llm_words = FOREACH llm_responses GENERATE FLATTEN(TOKENIZE(text)) AS word;
llm_clean = FILTER llm_words BY 
    SIZE(word) > 2 AND
    word MATCHES '^[a-z]+$' AND
    NOT (word MATCHES 'el|la|los|las|de|del|y|en|un|una|que|es|se|con|por|para|the|and|of|to|a|in|is|it|you|that|he|was|for|on|are|as|with|his|they|i|at|be|this|have|from');
llm_group = GROUP llm_clean BY word;
llm_count = FOREACH llm_group GENERATE group AS palabra, COUNT(llm_clean) AS frecuencia;
llm_sorted = ORDER llm_count BY frecuencia DESC;

-- Guardar resultados
STORE yahoo_sorted INTO '/output/yahoo_wordcount';
STORE llm_sorted INTO '/output/llm_wordcount';