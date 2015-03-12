CREATE OR REPLACE FUNCTION jot_cast_string_float(input_string text)
RETURNS FLOAT
AS $$
DECLARE output_float FLOAT DEFAULT NULL;
BEGIN
  BEGIN
    output_float := input_string::float;
  EXCEPTION WHEN OTHERS THEN
    RAISE NOTICE 'Invalid double precision: "%". Returning NULL.', input_string;
    RETURN NULL;
  END;
RETURN output_float;
END;
$$ LANGUAGE plpgsql
;
