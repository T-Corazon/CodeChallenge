function [ Ac ,Bc ,Cc ] = LuenbergerCTran1( A ,B ,C)
%Luenberger能控规范第一型（行搜索）
%UNTITLED4 Summary of this function goes here
%   Detailed explanation goes here
%初始化
[ma,~] = size(A);
[~,nb] = size(B);
P = [];N = [];%行矩阵N为排列参考
B1 = B;
%k是外循环标志，判断T是否已经满足
k = 0;
%判断系统是否可控
Qc = ctrb(A,B);
if rank(Qc) < ma
    error('系统不可控，请重新输入')
else
    %按行搜索变换阵P
    for i = 0:1:(ma-1)
        Ass = B;%辅助矩阵Ass，方便列排除
        for j = 1:1:nb
            M1 = P;M2 = N;
            P = [P (A^i)*Ass(:,j)]; 
            N = [N,j*ma+i];
            if rank(P) == min(size(P))%若得到的P是线性无关的，则继续寻找
                if rank(P) == ma           %判断判断P是否已经满足
                    k = 1;
                    break
                else
                    continue
                end
            else%若得到的P是线性相关的，则删除此前一列并还原P和N
                P = M1;
                N = M2;
                B(:,j) = []; %B中有一列已经不再考虑，则删除
            end                    
        end
        if k == 1%P已经满足,退出循环
            break
        end
    end
%利用行矩阵N排列P
Res1 = [P;N];
Res2 = sortrows(Res1',ma+1);
Res3 = Res2';
P = Res3(1:ma,:);
%输出Luenberger能控规范第一型Ac、Bc、Cc
T = inv(P);
Ac = T*A*P
Bc = T*B1
Cc = C*P
end

