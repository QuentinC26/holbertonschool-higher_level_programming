-- Create utilisateur user_0d_1
GRANT CREATE USER IF NOT EXISTS user_0d_1;
GRANT APPLY PASSWORD user_0d_1_pwd TO user_0d_1;
GRANT ALL PRIVILEGES ON localhost TO user_0d_1;