function [ Ac ,Bc ,Cc ] = WonhamCTran2( A ,B ,C)
%����ķ�ܿع淶�ڶ��ͣ���������
%UNTITLED4 Summary of this function goes here
%   Detailed explanation goes here
%��ʼ��
[ma,~] = size(A);
[~,nb] = size(B);
%�ж�ϵͳ�Ƿ�ɿ�
Qc = ctrb(A,B);
if rank(Qc) < ma
    error('ϵͳ���ɿأ�����������')
else
    %���������任��T
    T = [];
    %k����ѭ����־���ж�T�Ƿ��Ѿ�����
    k = 0;
    %��������S�ĸ�������S_ass����ÿ����ѭ��������ֵ
    S_ass = zeros(1,nb);
    for i = 1:nb
        for j = 1:ma
            M1 = T;M2 = S_ass(i);
            T = [T (A^(j-1))*B(:,i)]; 
            S_ass(i) =  S_ass(i) + 1; 
            if rank(T) == min(size(T))%���õ���T�������޹صģ������Ѱ��
                if rank(T) == ma      %�ж��ж�T�Ƿ��Ѿ�����
                    k = 1;
                    break
                else
                    continue
                end
            else                      %���õ���T��������صģ���������ѭ������ԭT�����S_ass
                T = M1;
                S_ass(i) = M2;
                break    
            end                    
        end
        if k == 1%T�Ѿ�����,�˳�ѭ��
            break
        end
    end
%�õ�T�������
P = inv(T);
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
%�������ķ�ܿع淶�ڶ���Ac��Bc��Cc
K = inv(S);
Ac = S*A*K
Bc = S*B
Cc = C*K
end

