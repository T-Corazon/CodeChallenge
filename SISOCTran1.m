function [Ac,bc,cc] = SISOCTran1(A,b,c)
% ��һ�ܿع淶��ת������
%UNTITLED Summary of this function goes here
%   Detailed explanation goes here
[m,n] = size(A);
Qc = b;
for i = 1:1:m-1
    Qc = [Qc (A^i)*b];
end
P = inv(Qc);
Ac = P*A*Qc
bc = P*b
cc = c*Qc
end

