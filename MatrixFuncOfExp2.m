function [ matrixsum ] = MatrixFuncOfExp2( Amatrix )
% ����ָ���������ʽ2������ʽ���任
%UNTITLED Summary of this function goes here
%   Detailed explanation goes here
syms s
matrixsum = eye(ndims(Amatrix)) * s;
matrixsum = ilaplace(inv(matrixsum - Amatrix));
end

