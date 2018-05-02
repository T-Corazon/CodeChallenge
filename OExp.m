function ko = OExp( A, C )
%获得能观性指数
%UNTITLED2 Summary of this function goes here
%   Detailed explanation goes here
[m,n] = size(A);
D = A;M = C;ko = 1;
if rank(M) == m
    ko = ko;
else
    while rank(M) < m
        M = [M C*D];
        D = D * A;
        ko = ko + 1;
    end
    ko = ko + 1;
end

