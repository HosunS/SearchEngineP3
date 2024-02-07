function [predictions] = nbayes_predict(params,testdata)
% function [predictions] = nbayes_predict(params,testdata)
%
%  function to make class label predictions on test data,
%  using a naive Bayes model (as described by the structure "params") 
%
%  Inputs 
%     params: a stucture for the parameters for a Naive Bayes classifier
%     params(j).mprobs(k): probability that variable j takes value k
%     params(j).cprobs(k,i): conditional probability
%                          of prob(variable j = value k | class = value i) 
%     params(1).classprobs(i): probability that class variable = i 
%
%     testdata: n x d data matrix, d features/variables and n observations 
%
%  Outputs
%     predictions: n x 1 vector of class predictions  (for the homework
%      dataset, these take on values of 1 or 2)
%

  
% .....determine the number of test data points, etc.....
nclasses = 2;
ntest = ....
d = ....

% for each of the test data points
  for m=1:ntest
     x = testdata(m,:);
     % for each class value calculate log[ p(x|c) p(c) ]
     for classi=1:nclasses; 
        ......
        for varj=1:d 
            ......
        end
    end
    % select the maximum value over all classes as the predicted class
    .......
    % store the class prediction for each test data point 
    ........
end

 
              
