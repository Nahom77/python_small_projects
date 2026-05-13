# 3.3. Calculcate	the	sum	of	nested	arrays
# This	problem asks	you	to	sum	up	all	of	the	numbers	within	an
# array,	but	the	array	may	also	contains
# other	arrays	with	numbers.	This	is	what	we	call a
# nested	array. For	example:
# [1, 1, 1, [3, 4, [8]], [5]]
# is	a	nested	array	and	summing	all	the	elements	should
# produce	23. We	will	solve	this	problem	by
# implementing	a	recursive	function	where	if	an	array	is
# encountered	within an	array,	we	simply	sum	all
# of	the	inner	arrays elements	and	then	add	that	to	the	final
# 	result. For	example,	with	the	code	solution
# below	applied	to	the	above	array,	the	following	steps	would
# take	place:
# 1. result	=	1
# 2. result	=	1	+	1	=	2
# 3. result	=	2	+	1	=	3
# 4. result	=	3	+	sumNested([3,	4,	[8]])
# 4.1. result	=	3
# 4.2. result	=	3	+	4
# 4.3. result	=	7	+	sumNested([8])
# 4.3.1. result	=	8
# 5. result	=	3	+	15	=	18
# 6. result	=	18	+	sumNested([5])
# 6.1. result	=	5
# 7. result	=	18	+	5	=	23


def sumNested(arr):
    result = 0

    for i in range(len(arr)):
        if type(arr[i]) is not int:
            result += sumNested(arr[i])
        else:
            result += arr[i]

    return result
