-- Shows the description of a table
SELECT column_name, data_type, character_maximum_length, is_nullable
FROM information_schema.columns
WHERE table_name = 'first_table' AND table_schema = 'hbtn_0c_0';