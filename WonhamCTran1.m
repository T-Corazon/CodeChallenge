function [ Ac ,Bc ,Cc ] = WonhamCTran1( A ,B ,C)
%����ķ�ܿع淶��һ�ͣ���������
%UNTITLED4 Summary of this function goes here
%   Detailed explanation goes here
%��ʼ��
[ma,~] = size(A);
[~,nb] = size(B);
T = [];N = [];%�о���NΪ���вο�
%k����ѭ����־���ж�T�Ƿ��Ѿ�����
k = 0;
%�ж�ϵͳ�Ƿ�ɿ�
Qc = ctrb(A,B);
if rank(Qc) < ma
    error('ϵͳ���ɿأ�����������')
else
    %���������任��T
    for i = 1:1:nb
        for j = 0:1:(ma-1)
            M1 = T;M2 = N; 
            T = [T (A^j)*B(:,i)]; 
            N = [N,i*ma+j];
            if rank(T) == min(size(T)) %���õ���T�������޹صģ������Ѱ��
                if rank(T) == ma%�ж��ж�T�Ƿ��Ѿ�����
                    k = 1;
                    break
                else
                    continue
                end
            else%���õ���T��������صģ���������ѭ������ԭT��N
                T = M1; 
                N = M2;
                break         
            end                 
        end
        if k == 1%T�Ѿ�����,�˳�ѭ��
            break
        end
    end
%�����о���N����T
Res1 = [T;N];
Res2 = sortrows(Res1',ma+1);
Res3 = Res2';
T = Res3(1:ma,:);
%�������ķ�ܿع淶��һ��Ac��Bc��Cc
P = inv(T);
Ac = P*A*T
Bc = P*B
Cc = C*T
end

