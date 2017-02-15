create table if not exists app_user_predict_first_invest_account_feature_2017_full
COMMENT '2017年用户投资、充值、提现相关特征'
(
user_id string,
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
invest_cnt_60 int,
invest_sum_60 double,
invest_max_60 double,
invest_min_60 double,
invest_avg_60 double,
rate_max_60 double,
rate_min_60 double,
rate_avg_60 double,
days_max_60 double,
days_min_60 double,
days_avg_60 double,
invest_cnt_90 int,
invest_sum_90 double,
invest_max_90 double,
invest_min_90 double,
invest_avg_90 double,
rate_max_90 double,
rate_min_90 double,
rate_avg_90 double,
days_max_90 double,
days_min_90 double,
days_avg_90 double,
invest_cnt_120 int,
invest_sum_120 double,
invest_max_120 double,
invest_min_120 double,
invest_avg_120 double,
rate_max_120 double,
rate_min_120 double,
rate_avg_120 double,
days_max_120 double,
days_min_120 double,
days_avg_120 double,
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
deposit_cnt_60 int,
deposit_sum_60 double,
deposit_max_60 double,
deposit_min_60 double,
deposit_avg_60 double,
deposit_cnt_90 int,
deposit_sum_90 double,
deposit_max_90 double,
deposit_min_90 double,
deposit_avg_90 double,
deposit_cnt_120 int,
deposit_sum_120 double,
deposit_max_120 double,
deposit_min_120 double,
deposit_avg_120 double,
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
withdraw_cnt_60 int,
withdraw_sum_60 double,
withdraw_max_60 double,
withdraw_min_60 double,
withdraw_avg_60 double,
withdraw_cnt_90 double,
withdraw_sum_90 double,
withdraw_max_90 double,
withdraw_min_90 double,
withdraw_avg_90 double,
withdraw_cnt_120 int,
withdraw_sum_120 double,
withdraw_max_120 double,
withdraw_min_120 double,
withdraw_avg_120 double
) ROW FORMAT DELIMITED FIELDS TERMINATED BY '\u0001' LINES TERMINATED BY '\n';
