function [Ac,bc,cc] = SISOCTran2(A,b,c)
% 第二能控规范性转换函数
%UNTITLED Summary of this function goes here
%   Detailed explanation goes here
[m,n] = size(A);
Qc = b;
for i = 1:1:m-1
    Qc = [(A^i)*b Qc];
end
P = inv(Qc);
Ac = Qc*A*P
bc = Qc*b
cc = c*P
end