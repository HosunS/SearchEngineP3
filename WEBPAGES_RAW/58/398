function pmf =  binopmf_approx(x,n,p);
% approximates the binomial probability mass function (using a
% Gaussian approximation) for the integer values stored in the 
% x vector (e.g., 0,1,2,....n) 
%
% n and p are the parameters of the binomial model
%
%                                               CS 177, Spring 2009

pmf = zeros(1,length(x));  % initialize the vector of pmf values to zero
for i=1:length(x)  % for each value in the x vector
    k = x(i);
    % compute the log of the probability of k, using the Gaussian
    % approximation
    logpk = -0.5*log(2*pi*n*p*(1-p));
    logpk = -(k-n*p)*(k-n*p)/(2*n*p*(1-p))+logpk;
    % now exponentiate to get the probability of k
    pmf(i) = exp(logpk);
end
