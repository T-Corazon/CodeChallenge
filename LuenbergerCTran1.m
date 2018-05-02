function [ Ac ,Bc ,Cc ] = LuenbergerCTran1( A ,B ,C)
%Luenberger�ܿع淶��һ�ͣ���������
%UNTITLED4 Summary of this function goes here
%   Detailed explanation goes here
%��ʼ��
[ma,~] = size(A);
[~,nb] = size(B);
P = [];N = [];%�о���NΪ���вο�
B1 = B;
%k����ѭ����־���ж�T�Ƿ��Ѿ�����
k = 0;
%�ж�ϵͳ�Ƿ�ɿ�
Qc = ctrb(A,B);
if rank(Qc) < ma
    error('ϵͳ���ɿأ�����������')
else
    %���������任��P
    for i = 0:1:(ma-1)
        Ass = B;%��������Ass���������ų�
        for j = 1:1:nb
            M1 = P;M2 = N;
            P = [P (A^i)*Ass(:,j)]; 
            N = [N,j*ma+i];
            if rank(P) == min(size(P))%���õ���P�������޹صģ������Ѱ��
                if rank(P) == ma           %�ж��ж�P�Ƿ��Ѿ�����
                    k = 1;
                    break
                else
                    continue
                end
            else%���õ���P��������صģ���ɾ����ǰһ�в���ԭP��N
                P = M1;
                N = M2;
                B(:,j) = []; %B����һ���Ѿ����ٿ��ǣ���ɾ��
            end                    
        end
        if k == 1%P�Ѿ�����,�˳�ѭ��
            break
        end
    end
%�����о���N����P
Res1 = [P;N];
Res2 = sortrows(Res1',ma+1);
Res3 = Res2';
P = Res3(1:ma,:);
%���Luenberger�ܿع淶��һ��Ac��Bc��Cc
T = inv(P);
Ac = T*A*P
Bc = T*B1
Cc = C*P
end

