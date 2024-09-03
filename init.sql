-- init.sql
CREATE TABLE IF NOT EXISTS jokes (
    id SERIAL PRIMARY KEY,
    level VARCHAR(10),
    language VARCHAR(10),
    joke TEXT
);

INSERT INTO jokes (level, language, joke) VALUES
('low', 'en-us', 'Why do surfers dont like reheated food? Because they dont like microwave'),
('medium', 'en-us', 'Why dont skeletons skydive? They dont have the guts to do it.'),
('high', 'en-us', 'How many programmers does it take to change a light bulb? None. It’s a hardware problem.'),
('low', 'pt-br', 'Por que os surfistas não curtem comida requentada? Porque eles não gostam de microondas! kkk'),
('medium', 'pt-br', 'Por que os esqueletos não pulam de para-quedas? Porque eles não tem estomago pra isso'),
('high', 'pt-br', 'Quantos programadores são necessários para trocar uma lâmpada? Nenhum. É um problema de hardware.');
