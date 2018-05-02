function [ Ac ,Bc ,Cc ] = WonhamCTran1( A ,B ,C)
%旺纳姆能控规范第一型（列搜索）
%UNTITLED4 Summary of this function goes here
%   Detailed explanation goes here
%初始化
[ma,~] = size(A);
[~,nb] = size(B);
T = [];N = [];%行矩阵N为排列参考
%k是外循环标志，判断T是否已经满足
k = 0;
%判断系统是否可控
Qc = ctrb(A,B);
if rank(Qc) < ma
    error('系统不可控，请重新输入')
else
    %按列搜索变换阵T
    for i = 1:1:nb
        for j = 0:1:(ma-1)
            M1 = T;M2 = N; 
            T = [T (A^j)*B(:,i)]; 
            N = [N,i*ma+j];
            if rank(T) == min(size(T)) %若得到的T是线性无关的，则继续寻找
                if rank(T) == ma%判断判断T是否已经满足
                    k = 1;
                    break
                else
                    continue
                end
            else%若得到的T是线性相关的，则跳出内循环并还原T和N
                T = M1; 
                N = M2;
                break         
            end                 
        end
        if k == 1%T已经满足,退出循环
            break
        end
    end
%利用行矩阵N排列T
Res1 = [T;N];
Res2 = sortrows(Res1',ma+1);
Res3 = Res2';
T = Res3(1:ma,:);
%输出旺纳姆能控规范第一型Ac、Bc、Cc
P = inv(T);
Ac = P*A*T
Bc = P*B
Cc = C*T
end

