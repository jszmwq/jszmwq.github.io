load("coppersmith.sage")
N = 0xa1888c641a05aeb81b3d1686317a86f104791fe1d570a5b11209f45d09ea401d255a70744e7a2d39520e359c23a9f1209ee47f496dbd279e62ee1648b3a277ced8825298274322e0a7a86deea282676310a73b6bb946fc924c34ac6c8784ff559bf9a004c03fb167ef54aaea90ce587f2f3074b40d7f632022ec8fb12e659953L
e = 3
m = 0x9e67d3a220a3dcf6fc4742052621f543b8c78d5d9813e69272e65ac676672446e5c88887e8bfdfc92ec87ec74c16350e6b539e3bd910b000000000000000000L
 
c = 0x93145ece45f416a11e5e9475518f165365456183c361500c2f78aff263028c90f20b7d97205f54e21f3bcc8a556b457889fde3719d0a0f9c9646f3f0d0a1e4bee0f259f023168fe8cc0511848c1635022fcc20b6088084585e2f8055a9d1b1d6bdb228087900bf7c6d42298f8e45c451562c816e2303990834c94e580bf0cbd1L
ZmodN = Zmod(N)
P.<x> = PolynomialRing(ZmodN)
f = (m + x)^e - c
dd = f.degree()
beta = 1
epsilon = beta / 7
mm = ceil(beta**2 / (dd * epsilon))
tt = floor(dd * mm * ((1/beta) - 1))
XX = ceil(N**((beta**2/dd) - epsilon))
roots = coppersmith_howgrave_univariate(f, N, beta, mm, tt, XX)
print "缺失的m部分是:"+hex(roots[0])
print "完整的m是:自己手动把上面m中的0000000换为缺失的m部分值即可(16进制的)."