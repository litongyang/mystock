-- 下载首次投资60天的用户预测其未来两个月的投资的训练集表
set hive.exec.compress.output=false;
insert overwrite local directory '/root/user_value_predict/train/data/first_invest/first_invest_60' row format delimited fields terminated by '\t'

select *
from
app.app_user_predict_first_invest_train_set_from_60