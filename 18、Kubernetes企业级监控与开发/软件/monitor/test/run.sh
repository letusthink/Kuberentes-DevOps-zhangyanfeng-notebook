#!/bin/bash
for i in `seq 1000000`
do
  # 产生404状态码数据
  curl --resolve zyf.test.com:80:192.168.128.21 http://zyf.test.com/q
  # 产生200状态码数据
  curl --resolve zyf.test.com:80:192.168.128.21 http://zyf.test.com/check
  # 参数403状态码数据
  curl --resolve zyf.test.com:80:192.168.128.21 http://zyf.test.com/
done
