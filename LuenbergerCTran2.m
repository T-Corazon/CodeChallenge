function [ Ac ,Bc ,Cc ] = LuenbergerCTran2( A ,B ,C)
%Luenberger�ܿع淶�ڶ��ͣ���������
%UNTITLED4 Summary of this function goes here
%   Detailed explanation goes here
%��ʼ��
[ma,~] = size(A);
[~,nb] = size(B);
%�洢BΪB1
B1 = B;
P = [];N = [];%�о���NΪ���вο�
%k����ѭ����־���ж�T�Ƿ��Ѿ�����
k = 0;
%�ж�ϵͳ�Ƿ�ɿ�
Qc = ctrb(A,B);
if rank(Qc) < ma
    error('ϵͳ���ɿأ�����������')
else
    %���������任��P
    %��������S�ĸ�������S_ass����ÿ����ѭ��������������Ӧ������S_ass
    S_ass = zeros(1,nb);
    for i = 1:ma
        Ass = B;%��������Ass���������ų�
        for j = 1:nb
            M1 = P;M2 = N;M3 = S_ass(j);
            P = [P (A^(i-1))*Ass(:,j)]; 
            N = [N,j*ma+i];
            S_ass(j) =  S_ass(j) + 1; 
            if rank(P) == min(size(P))%���õ���P�������޹صģ������Ѱ��
               if rank(P) == ma       %�ж��ж�P�Ƿ��Ѿ�����
                    k = 1;
                    break
               else
                   continue
               end
            else                      %���õ���P��������صģ���ɾ����ǰһ�в���ԭP��N��S_ass
                P = M1;
                N = M2;
                S_ass(j) = M3;
                B(:,j) = [];    %B����һ���Ѿ����ٿ��ǣ���ɾ��
            end                      
        end
        if k == 1%P�Ѿ�����,�˳�ѭ��
            break
        end
    end
disp(S_ass)
%�����о���N����P
Res1 = [P;N];
Res2 = sortrows(Res1',ma+1);
Res3 = Res2';
P = Res3(1:ma,:);
%�õ�P�������
T = inv(P);
%Eÿ�δ洢�����ÿ�����һ�У�����p����Ѱ�����һ��
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
%���Luenberger�ܿع淶�ڶ���Ac��Bc��Cc
K = inv(S);
Ac = S*A*K
Bc = S*B1
Cc = C*K
end

