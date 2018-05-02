function [ matrixsum ] = MatrixFuncOfExp2( Amatrix )
% 矩阵指数函数表达式2——拉式反变换
%UNTITLED Summary of this function goes here
%   Detailed explanation goes here
syms s
matrixsum = eye(ndims(Amatrix)) * s;
matrixsum = ilaplace(inv(matrixsum - Amatrix));
end

