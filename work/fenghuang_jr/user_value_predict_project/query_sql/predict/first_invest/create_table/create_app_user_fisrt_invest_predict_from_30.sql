create table if not exists  app.app_user_predict_first_invest_predict_set_from_30
(
user_id   string,
age_generation  string,
gender_code   string,
telecom_operators  string,
is_member  string,
lv_name  string,
has_bind_bank_card  string,
card_value  string,
mobile_value  string,
mobile_phone_value  string,
is_register_ump_good  string,
is_new_user_loan  string,
is_register_recharge_good  string,
is_register_invest_good  string,
is_ump_recharge_good  string,
is_ump_invest_good  string,
is_recharge_invest_good  string,
zodiac  string,
chinese_zodiac  string,
mobile_province  string,
first_invest_date  string,
first_invest_amount  string,
first_invest_loan_months  string,
first_invest_rate  string,
first_recharge_date  string,
first_recharge_amount   string,
invest_cnt_7 int,
invest_sum_7 double,
invest_max_7 double,
invest_min_7 double,
invest_avg_7 double,
rate_max_7 double,
rate_min_7 double,
rate_avg_7 double,
days_max_7 double,
days_min_7 double,
days_avg_7 double,
invest_cnt_14 int,
invest_sum_14 double,
invest_max_14 double,
invest_min_14 double,
invest_avg_14 double,
rate_max_14 double,
rate_min_14 double,
rate_avg_14 double,
days_max_14 double,
days_min_14 double,
days_avg_14 double,
invest_cnt_30 int,
invest_sum_30 double,
invest_max_30 double,
invest_min_30 double,
invest_avg_30 double,
rate_max_30 double,
rate_min_30 double,
rate_avg_30 double,
days_max_30 double,
days_min_30 double,
days_avg_30 double,
deposit_cnt_7 int,
deposit_sum_7 double,
deposit_max_7 double,
deposit_min_7 double,
deposit_avg_7 double,
deposit_cnt_14 int,
deposit_sum_14 double,
deposit_max_14 double,
deposit_min_14 double,
deposit_avg_14 double,
deposit_cnt_30 int,
deposit_sum_30 double,
deposit_max_30 double,
deposit_min_30 double,
deposit_avg_30 double,
withdraw_cnt_7 int,
withdraw_sum_7 double,
withdraw_max_7 double,
withdraw_min_7 double,
withdraw_avg_7 double,
withdraw_cnt_14 int,
withdraw_sum_14 double,
withdraw_max_14 double,
withdraw_min_14 double,
withdraw_avg_14 double,
withdraw_cnt_30 int,
withdraw_sum_30 double,
withdraw_max_30 double,
withdraw_min_30 double,
withdraw_avg_30 double,
dt              string
) ROW FORMAT DELIMITED FIELDS TERMINATED BY '\t' LINES TERMINATED BY '\n';





