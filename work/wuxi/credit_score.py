#  __author__ = 'litongyang'
# -*- coding: utf-8 -*-

# ------企业信用模型-------

import work.wuxi.cite_score as cite  # 表彰
import work.wuxi.credit_real_score as credit_real  # 非失信
import work.wuxi.dishonesty_score as dishonesty  # 失信



class CreditScore:
    def __init__(self):
        self.cite_class = cite.CiteScore()
        self.creditReal_class = credit_real.CreditRealScore()
        self.dishonesty_class = dishonesty.DeshonestyScore()
        self.weight_cite = 1  # 表彰权重
        self.weight_good_brand = 1  # 驰名商标权重
        self.weight_brand_register = 1  # 贯标权重
        self.weight_credit = 1  # 信用评定等级权重
        self.weight_certification_levels = 1  # 工商认证等级权重
        self.weight_brand_c = 1  # C标权重
        self.weight_gongjijin = 1  # 公积金权重
        self.weight_owe = 1  # 欠税权重
        self.weight_penalty = 1  # 行政处罚权重
        self.weight_blackList= 1  # 黑名单权重
        self.weight_bad_loan = 1  # 不良贷款权重
        self.weight_illegal = 1  # 企业违法权重

        self.weight_cite = 1  # 表彰权重
        self.weight_base = 1  # 基本信息权重
        self.weight_credit_real = 1 # 非失信权重
        self.weight_dishonesty = 1  # 失信权重


        self.cite_score = {}
        self.credit_real_score = {}
        self.dishonesty_score = {}
        self.credit_score = {}

    # 计算表彰得分
    def compute_cite_score(self):
        cnt = 0
        self.cite_class.get_data()
        self.cite_class.compute_biaozhang_score()
        self.cite_class.compute_good_brand_score()

        self.cite_class.score_biaozhang = {key:float(value) * self.weight_brand_register for key,value in self.cite_class.score_biaozhang.items()}
        self.cite_class.good_brand_score = {key:float(value) * self.weight_good_brand for key,value in self.cite_class.good_brand_score.items()}
        for id,value in self.cite_class.score_biaozhang.items():
            score_one = value
            if self.cite_class.good_brand_score.has_key(id):
                score_one += self.cite_class.good_brand_score[id]
            self.cite_score[id] = score_one
        for k,v in self.cite_score.items():
            if v !=0:
                cnt += 1
            print k,v
        print cnt



    # 计算非失信得分
    # noinspection PyBroadException
    def compute_credit_real_score(self):
        cnt = 0
        self.creditReal_class.get_data()
        self.creditReal_class.process_data()
        self.creditReal_class.compute_brand_register_score()
        self.creditReal_class.compute_credit_score()
        self.creditReal_class.compute_certification_levels_score()
        self.creditReal_class.compute_brand_c_score()

        # print len(self.creditReal_class.brand_register_score)
        self.creditReal_class.brand_register_score = {key:float(value) * self.weight_brand_register for key,value in self.creditReal_class.brand_register_score.items()}
        self.creditReal_class.credit_assess_score = {key:float(value) * self.weight_credit for key,value in self.creditReal_class.credit_assess_score.items()}
        self.creditReal_class.certification_levels_score = {key:float(value) * self.weight_certification_levels for key,value in self.creditReal_class.certification_levels_score.items()}
        self.creditReal_class.brand_c_score = {key:float(value) * self.weight_brand_c for key,value in self.creditReal_class.brand_c_score.items()}
        # for k,v in self.creditReal_class.brand_register_score.items():
        #     if v != 0:
        #         print v
        for id,value in self.creditReal_class.credit_assess_score.items():
            score_one = value
            x = value
            # print score_one
            if self.creditReal_class.brand_register_score.has_key(id):
                score_one += self.creditReal_class.brand_register_score[id]
            if self.creditReal_class.certification_levels_score.has_key(id):
                score_one += self.creditReal_class.certification_levels_score[id]
            if self.creditReal_class.brand_c_score.has_key(id):
                score_one += self.creditReal_class.brand_c_score[id]
            self.credit_real_score[id] = score_one

            # # 查看非信用的得分数量
            # if x != score_one:
            #     cnt +=1
            # print cnt

        for k,v in self.credit_real_score.items():
            if v   >0:
                cnt +=1
            print k,':',v
        print cnt

    # 计算失信得分
    def compute_dishonesty_score(self):
        cnt = 0
        self.dishonesty_class.get_data()
        self.dishonesty_class.process_data()
        self.dishonesty_class.compute_gongjijin_score()
        self.dishonesty_class.compute_qianshui_score()
        self.dishonesty_class.compute_penalty_score()
        self.dishonesty_class.compute_black_list_score()
        self.dishonesty_class.compute_bad_loan_score()
        self.dishonesty_class.compute_illegal_score()
        # print len(self.dishonesty_class.common_reserve_score)
        self.dishonesty_class.common_reserve_score = {key:float(value) * self.weight_gongjijin for key,value in self.dishonesty_class.common_reserve_score.items()}
        self.dishonesty_class.owing_taxes_score = {key:float(value) * self.weight_owe for key,value in self.dishonesty_class.owing_taxes_score.items()}
        self.dishonesty_class.penalty_score = {key:float(value) * self.weight_penalty for key,value in self.dishonesty_class.penalty_score.items()}
        self.dishonesty_class.black_list_score = {key:float(value) * self.weight_blackList for key,value in self.dishonesty_class.black_list_score.items()}
        self.dishonesty_class.bad_loan_score = {key:float(value) * self.weight_bad_loan for key,value in self.dishonesty_class.bad_loan_score.items()}
        self.dishonesty_class.illegal_score = {key:float(value) * self.weight_illegal for key,value in self.dishonesty_class.illegal_score.items()}
        for id, value in self.dishonesty_class.penalty_score.items():
            score_one = self.weight_penalty * value
            if self.dishonesty_class.common_reserve_score.has_key(id):
                score_one += self.dishonesty_class.common_reserve_score[id]
            if self.dishonesty_class.owing_taxes_score.has_key(id):
                score_one += self.dishonesty_class.owing_taxes_score[id]
            if self.dishonesty_class.black_list_score.has_key(id):
                score_one += self.dishonesty_class.black_list_score[id]
            if self.dishonesty_class.bad_loan_score.has_key(id):
                score_one += self.dishonesty_class.bad_loan_score[id]
            if self.dishonesty_class.illegal_score.has_key(id):
                score_one += self.weight_illegal * self.dishonesty_class.illegal_score[id]
            self.dishonesty_score[id] = score_one
        for k,v in self.dishonesty_score.items():
            if v !=0:
                cnt +=1
            print k,':',v
        print cnt

    # 计算企业的信用得分
    def compute_credit_score(self):
        cnt = 0
        for id,value in self.credit_real_score.items():
            score_one = value
            if self.dishonesty_score.has_key(id):
                score_one += self.weight_dishonesty * self.dishonesty_score[id]
            if self.cite_score.has_key(id):
                score_one += self.weight_cite * self.cite_score[id]
            if self.credit_score.has_key(id):
                score_one += self.weight_credit * self.credit_score[id]
            self.credit_score[id] = score_one
        for k,v in self.credit_score.items():
            cnt += 1
            print k,v
        print cnt

if __name__ == '__main__':
    credit_score = CreditScore()
    credit_score.compute_cite_score()
    credit_score.compute_credit_real_score()
    credit_score.compute_dishonesty_score()
    credit_score.compute_credit_score()