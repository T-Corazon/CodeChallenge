function kc = CExp( A, B )
%获得能控性指数
%UNTITLED2 Summary of this function goes here
%   Detailed explanation goes here
[m,n] = size(A);
C = A;M = B;kc = 1;
if rank(M) == m
    kc = kc;
else
    while rank(M) < m
        M = [M C*B];
        C = C * A;
        kc = kc + 1;
    end
    kc = kc + 1;
end