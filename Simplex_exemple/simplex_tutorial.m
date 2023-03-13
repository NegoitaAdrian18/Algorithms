%   The canonical form of the problem
%   MAX: 8X1+9X2+5X3
%   Constrangeri:   x1  + x2  + 2x3 + x4 + 0  + 0  =2
%                   2x1 + 3x2 + 4x3 + 0 +  x5 + 0  =3
%                   6x1 + 6x2 + 2x3 + 0 +  0  + x6 =8
%      x1,x2,x3,x4,x5,x6 > 0

A=[1 1 2 1 0 0 ; 2 3 4 0 1 0; 6 6 2 0 0 1];
b=[2;3;8];
c=[8;9;5;0;0;];

% For this problem i will use the initial basic feasible solution corresponding to using x4, x5, x6 as basic variables. 
%Initial basis : sB = [4 5 6]

sB = [4 5 6];

% Finding the innitial basis matrix:
 
mB = A(:,sB);

%Solving for the initial basic feasible solution
x = zeros(6,1); 
x(sB) = mB^-1*b; 

% report on my initial basic feasible solution (bsf)
fprintf('Basic elements are: \n');
fprintf('%d ',sB);
fprintf('\n');

fprintf('Initial bsf is the vector: \n');
fprintf('%f\n', x);
