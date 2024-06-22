We are using `Linear Programming`
## Instructions
```shell
pip install numpy
pip install scipy
```

```shell
python3 code.py
```



## Mathematical Equations

### Equalities

__borrow__

- usdc : x1 + x2 + x3 + x4 + x5 ≥ 2m
- usdt : y1 + y2 + y3 + y4 + y5 ≥ 3m
- eth : z1 + z2 + z3 ≥ 10m

__supply__ 

- usdt : a1 + a2 + a3 ≤ 1m
- dai : b1 + b2 + b3 ≤ 2.5m
- eth : c1 + c2 + c3 + c4 + c5 + c6 ≤ 9m
- weth : d1 + d2 + d3 ≤ 15m

### Inequalities

- aave : 0.8*(1.75m + a2 + b3 + c4 + d3) ≥ x1 + y1 + z3
- spark : (a1 + b1 + c5)*0.8 ≥ x2 + y3 + z1
- morpho : (a3 + b2 + c6)*0.8 ≥ x3 + y2 + z2
- f eth usdt : c1*0.8 ≥ y4
- f eth usdc : c2*0.8 ≥ x4
- f weth usdc : d1*0.8 ≥ x5
- f weth usdt : d2*0.8 ≥ y5

- all variables ≥ 0


### Objective equation
Z = 0.0776*a1 + 0.0437*a2 + 0.0392*a3 + 0.0998*b1 + 0.0675*b2 + 0.0612*b3 + 0.0866*c1 + 0.0856*c2 + 0.0732*c3 + 0.0163*c4 + 0.0109*c5 + 0.0033*c6 + 0.0338*d1 + 0.0338*d2 + 0.0242*d3 - 0.0813*x1 - 0.0828*x2 - 0.0915*x3 - 0.1505*x4 - 0.1505*x5 - 0.0437*y1 - 0.0768*y2 - 0.0908* y3 - 0.1493*y4 - 0.1493*y5 - 0.019*z1 - 0.0169*z2 - 0.0246*z3