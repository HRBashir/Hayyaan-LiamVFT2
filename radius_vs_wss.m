%% variables
u = 0.004;       % dynamic viscosity (Pa/s)
vm = 0.1;        % blood velocity (m/s)
y = 0.006;       % distance from the centre (m)
r1 = 0.012;       % radius of aorta (m)
r2 = 0.024;
r3 = 0.036;
r4 = 0.048;
%% Calcullation
WSS1 = -(2*u*vm*y) / (r1^2)   % value for WSS (S^-1)
WSS2 = -(2*u*vm*y) / (r2^2)   % value for WSS (S^-1)
WSS3 = -(2*u*vm*y) / (r3^2)   % value for WSS (S^-1)
WSS4 = -(2*u*vm*y) / (r4^2)   % value for WSS (S^-1)
x = [WSS1 WSS2 WSS3 WSS4];
y = [r1 r2 r3 r4];
%% Graph 
figure; plot(x,y)
title('Radius vs WSS');
xlabel('WSS (s^-1)')
ylabel('Radius (m)')