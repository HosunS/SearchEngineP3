function pmf = binomial_pmf(x,n,p)
% Template of function for Homework 1 in CS 177
%
%  BINOMIAL_PMF Binomial probability mass function.
%   pmf = BINOMIAL_PMF(x,n,p) returns the binomial probability mass
%   function with parameters n and p at the values in x.
%   (typically x is a vector of integers 0,1,2,....n)
%
%   The size of "pmf" is a vector of the same length as x.   
% 
%   
%                                           CS 177, Spring 2009


% error-checking
if nargin < 3, 
    error('binomial_pmf: Too few inputs','Requires 3 input arguments');
end


% Initialize the pmf vector to zero
pmf = zeros(length(x),1);


for i=1:length(x);
    k = x(i);  % select the ith value in the x vector
    
    %.... you now compute log p(k) as follows - we will compute the value of
    % of pk in the log domain to avoid computing very small or very large
    % numbers that would cause underflow or overflow.  
    
    %....you will need to fill in the rest of details below......
    
    %.... first use nchoosek.m to compute the binomial coefficient "n choose k"
    %.... and take the log of this to begin computing log p(k)
    %... use "help nchoosek" at the MATLAB prompt to find out what it does
    logpk = log(nchoosek(????));
    
    %....now compute the rest of the expression for log p(k)
    % where we need to compute log(p^k) and log[(1-p)^(n-k)]
    logpk = logpk + ????
    
    % finally convert back to get p(k) by computing exp(logpk)
    pmf(i) = exp(logpk);
end

% Notes:
% - we could probably vectorize this computation if we wanted to
%    and make it a bit faster - see vectorization in the MATLAB tutorial
%
% - you could check for possible errors in your computation by
%    summing all the values of pmf (i.e., z = sum(pmf)) and checking that
%    it is equal to 1.
%
% - even computing using logs will still run into problems (with
%   the nchoosek function, since it is based on factorials which
%   grow very large with n) once n starts to get reasonably large. For
%   the cases of large n (e.g., n=1000) you will need to use
%   the approximation to the binomial, binopmf.approx.m, which
%   avoids the use of factorials by using a fairly accurate alternative
%   approximation to the exact binomial pmf formula, that is valid
%   for large n.
 
