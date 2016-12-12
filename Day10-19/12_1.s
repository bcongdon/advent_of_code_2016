.text
main:

l0: 	add 	$t0, $0, 1
l1: 	add 	$t1, $0, 1
l2: 	add 	$t3, $0, 26
l3: 	bne 	$0, $t2, l5
l4: 	bne 	$0, 1, l9
l5: 	add 	$t2, $0, 7
l6: 	add 	$t3, $t3, 1
l7: 	sub 	$t2, $t2, 1
l8: 	bne 	$0, $t2, l6
l9: 	add 	$t2, $0, $t0
l10: 	add 	$t0, $t0, 1
l11: 	sub 	$t1, $t1, 1
l12: 	bne 	$0, $t1, l10
l13: 	add 	$t1, $0, $t2
l14: 	sub 	$t3, $t3, 1
l15: 	bne 	$0, $t3, l9
l16: 	add 	$t2, $0, 17
l17: 	add 	$t3, $0, 18
l18: 	add 	$t0, $t0, 1
l19: 	sub 	$t3, $t3, 1
l20: 	bne 	$0, $t3, l18
l21: 	sub 	$t2, $t2, 1
l22: 	bne 	$0, $t2, l17
	move 	$a0, $t0
	li 	$v0, 1
	syscall
