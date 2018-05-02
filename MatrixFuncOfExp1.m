function [ matrixsum ] = MatrixFuncOfExp1( Amatrix,t,n )
% 矩阵指数函数表达式1——定义
%UNTITLED2 Summary of this function goes here
%   Detailed explanation goes here
if n<1
    error('please input correct "n"');
elseif n==1
    matrixsum = eye(ndims(Amatrix));
else
    matrixsum = eye(ndims(Amatrix));
    for i = 1:n-1
    matrixsum = matrixsum + (Amatrix.* t)^i/factorial(i);
    end
end



