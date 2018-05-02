function [ Ac ,Bc ,Cc ] = WonhamCTran2( A ,B ,C)
%旺纳姆能控规范第二型（列搜索）
%UNTITLED4 Summary of this function goes here
%   Detailed explanation goes here
%初始化
[ma,~] = size(A);
[~,nb] = size(B);
%判断系统是否可控
Qc = ctrb(A,B);
if rank(Qc) < ma
    error('系统不可控，请重新输入')
else
    %按列搜索变换阵T
    T = [];
    %k是外循环标志，判断T是否已经满足
    k = 0;
    %构建矩阵S的辅助矩阵S_ass，在每次内循环结束后赋值
    S_ass = zeros(1,nb);
    for i = 1:nb
        for j = 1:ma
            M1 = T;M2 = S_ass(i);
            T = [T (A^(j-1))*B(:,i)]; 
            S_ass(i) =  S_ass(i) + 1; 
            if rank(T) == min(size(T))%若得到的T是线性无关的，则继续寻找
                if rank(T) == ma      %判断判断T是否已经满足
                    k = 1;
                    break
                else
                    continue
                end
            else                      %若得到的T是线性相关的，则跳出内循环并还原T和添加S_ass
                T = M1;
                S_ass(i) = M2;
                break    
            end                    
        end
        if k == 1%T已经满足,退出循环
            break
        end
    end
%得到T的逆矩阵
P = inv(T);
%E每次存储逆矩阵每块最后一行，参数p辅助寻找最后一行
p = 0;S = [];
for i = S_ass
    p = p + i;
    E = P(p,:);
    for j = 0:1:i-1
        S = [S;E*(A^j)];
    end
    if min(size(S)) == ma
        break
    end
end
%输出旺纳姆能控规范第二型Ac、Bc、Cc
K = inv(S);
Ac = S*A*K
Bc = S*B
Cc = C*K
end

