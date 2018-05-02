function [ Ac ,Bc ,Cc ] = LuenbergerCTran2( A ,B ,C)
%Luenberger能控规范第二型（行搜索）
%UNTITLED4 Summary of this function goes here
%   Detailed explanation goes here
%初始化
[ma,~] = size(A);
[~,nb] = size(B);
%存储B为B1
B1 = B;
P = [];N = [];%行矩阵N为排列参考
%k是外循环标志，判断T是否已经满足
k = 0;
%判断系统是否可控
Qc = ctrb(A,B);
if rank(Qc) < ma
    error('系统不可控，请重新输入')
else
    %按行搜索变换阵P
    %构建矩阵S的辅助矩阵S_ass，在每次内循环结束后生成相应块矩阵的S_ass
    S_ass = zeros(1,nb);
    for i = 1:ma
        Ass = B;%辅助矩阵Ass，方便列排除
        for j = 1:nb
            M1 = P;M2 = N;M3 = S_ass(j);
            P = [P (A^(i-1))*Ass(:,j)]; 
            N = [N,j*ma+i];
            S_ass(j) =  S_ass(j) + 1; 
            if rank(P) == min(size(P))%若得到的P是线性无关的，则继续寻找
               if rank(P) == ma       %判断判断P是否已经满足
                    k = 1;
                    break
               else
                   continue
               end
            else                      %若得到的P是线性相关的，则删除此前一列并还原P和N和S_ass
                P = M1;
                N = M2;
                S_ass(j) = M3;
                B(:,j) = [];    %B中有一列已经不再考虑，则删除
            end                      
        end
        if k == 1%P已经满足,退出循环
            break
        end
    end
disp(S_ass)
%利用行矩阵N排列P
Res1 = [P;N];
Res2 = sortrows(Res1',ma+1);
Res3 = Res2';
P = Res3(1:ma,:);
%得到P的逆矩阵
T = inv(P);
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
%输出Luenberger能控规范第二型Ac、Bc、Cc
K = inv(S);
Ac = S*A*K
Bc = S*B1
Cc = C*K
end

