%% Uppgift 4
% Beräkna totala antalet brev som skickas om varje person som får ett brev
% skickar ett brev till 3 personer därefter. Första personen skickar 20 brev.
%
% Vi ska använda funktionen sum().
brev = 20 * sum(3.^(0:9));
%%
% vilket ger oss
%
disp(brev);
%%
% antalet brev som skickas är alltså $590480$.
