"""
Python实现常用的10大排序算法程序，部分排序包括多种实现
"""

def bubble_sort(lyst):
	for i in range(len(lyst)):
		for j in range(len(lyst)-1, i, -1):
			if lyst[j] < lyst[j-1]:
				lyst[j], lyst[j-1] = lyst[j-1], lyst[j]


def select_sort(lyst):
	for i in range(len(lyst)):
		minIndex = i
		for j in range(i+1,len(lyst)):
			if lyst[j] < lyst[minIndex]:
				minIndex = j
		lyst[i], lyst[minIndex] = lyst[minIndex], lyst[i]


def insert_sort(lyst):
	for i in range(1, len(lyst)):
		j, temp = i-1, lyst[i]
		while j >= 0 and lyst[j] > temp:
			lyst[j+1], j = lyst[j], j-1
		lyst[j+1] = temp


def shell_sort_iteration(lyst):
	gap = len(lyst)//2
	while gap:
		for i in range(gap, len(lyst)):
			j, temp = i-gap, lyst[i]
			while j >= 0 and lyst[j] > temp:
				lyst[j+gap], j = lyst[j], j-gap
			lyst[j+gap] = temp
		gap //= 2


def shell_sort_recursion(lyst):
	def shell_helper(lyst, gap):
		if not gap:
			return
		for i in range(gap, len(lyst)):
			j, temp = i-gap, lyst[i]
			while j >= 0 and lyst[j] > temp:
				lyst[j+gap], j = lyst[j], j-gap
			lyst[j+gap] = temp
		shell_helper(lyst, gap//2)

	gap = len(lyst)//2
	shell_helper(lyst, gap)


def merge_sort_recursion(lyst, left=0, right=-1):
	if right == -1:
		right = len(lyst)
	if left >= right - 1:
		return 
	mid = (left+right)//2
	merge_sort_recursion(lyst, left, mid)
	merge_sort_recursion(lyst, mid, right)
	temp = lyst[left:right][:]#仅拷贝完成当前排序的一段
	l, r, index = 0, mid-left, left#三个索引分别指向temp表的左端、temp表的中点和原列表的排序左端
	while l<mid-left and r<right-left:
		if temp[l] <= temp[r]:
			lyst[index], l = temp[l], l+1
		else:
			lyst[index], r = temp[r], r+1
		index += 1
	lyst[index:right] = temp[l:mid-left] if l < mid-left  else temp[r:]#拼接剩余的部分

def merge_sort_iteration(lyst):
	length = len(lyst)
	size = 1
	while size<length:#从步长1开始归并，直至
		temp = lyst[:]
		for i in range((length//(2*size))+1):###当前步长下，需要分多少归并区间
			start = i*2*size ##每一块归并区间的起点
			l, r = start, start+size ##归并区间的左右起点
			index = start
			while l < start+size and r < min(start+2*size, length):#对左右子区间进行归并
				if temp[l] <= temp[r]:
					lyst[index], l = temp[l], l+1
				else:
					lyst[index], r = temp[r], r+1
				index += 1
			lyst[index:min(start+2*size, length)] = temp[l:start+size] if l < start+size  else temp[r:min(start+2*size, length)]#拼接剩余的部分
		size *= 2


def quick_sort_recursion(lyst):
	def quick_helper1(lyst, left, right):
		"""快慢指针确定分界，其中slow表示下区间的右界, left,right为左闭右开区间"""
		if left >= right-1:
			return
		pivot = left
		slow = left
		for fast in range(left+1, right):
			if lyst[fast] <= lyst[pivot]:
				slow += 1
				lyst[fast], lyst[slow] = lyst[slow], lyst[fast]
		lyst[pivot], lyst[slow] = lyst[slow], lyst[pivot]
		quick_helper1(lyst,left, slow)
		quick_helper1(lyst, slow+1, right)

	def quick_helper2(lyst, left, right):
		"""左右指针确定分界，其中l或l-1表示下区间的右界, left,right为左闭右开区间"""
		if left >= right-1:
			return
		pivot = left
		l, r = left+1, right-1
		while l < r:
			if lyst[l] <= lyst[pivot]:
				l += 1
			elif lyst[r] > lyst[pivot]:
				r -= 1
			else:
				lyst[l], lyst[r] = lyst[r], lyst[l]
				l += 1
				r -= 1
		if lyst[l] > lyst[pivot]:
			l -= 1
		lyst[pivot], lyst[l] = lyst[l], lyst[pivot]
		quick_helper2(lyst,left,l)
		quick_helper2(lyst, l+1, right)

	quick_helper1(lyst, 0, len(lyst))


def quick_sort_iteration(lyst):
	unSort = [(0, len(lyst))]#定义待排序区间列表
	while unSort:
		left, right = unSort.pop()#取出一个待排序区间：[left, right)
		pivot = slow = left
		for fast in range(left+1, right):
			if lyst[fast] <= lyst[pivot]:
				slow += 1
				lyst[fast], lyst[slow] = lyst[slow], lyst[fast]
		lyst[pivot], lyst[slow] = lyst[slow], lyst[pivot]
		if slow-left > 1:
			unSort.append((left, slow))
		if right - slow-1 > 1:
			unSort.append((slow+1, right))


def heap_sort(lyst):
	def max_heapify(lyst, i, length):
		l, r = 2*i+1, 2*i+2
		maxIndex = i
		if l<length and lyst[maxIndex]<lyst[l]:
			maxIndex = l
		if r<length and lyst[maxIndex]<lyst[r]:
			maxIndex = r
		if maxIndex != i:
			lyst[i], lyst[maxIndex] = lyst[maxIndex], lyst[i]
			max_heapify(lyst, maxIndex, length)

	def build_heap(lyst):
		for i in range(len(lyst)//2,-1,-1):
			max_heapify(lyst, i, len(lyst))

	build_heap(lyst)
	for i in range(len(lyst)-1,0,-1):
		lyst[0], lyst[i] = lyst[i], lyst[0]
		max_heapify(lyst, 0, i)


def count_sort(lyst):
	maxValue = max(lyst)
	minValue = min(lyst)
	counts = [0]*(maxValue - minValue + 1)
	for num in lyst:
		counts[num-minValue] += 1#将取值归一到 min--max之间
	cur = 0
	for index, count in enumerate(counts):
		if count == 0:
			continue
		lyst[cur:cur+count] = [index+minValue]*count
		cur += count


def radix_sort_iteration(lyst):
	minNum = min(lyst)
	n = len(str(max(lyst)-minNum))#计算归一化后的最大位数，即最大值与最小值差的位数
	for bit in range(n):
		buckets = {i:[] for i in range(10)}#以10为基数，设置10个桶
		for num in lyst:
			index = int((num-minNum)/(10**bit))%10#计算桶标号
			buckets[index].append(num)
		lyst[:] = [num for i in range(10) for num in buckets[i]]


def radix_sort_recursion(lyst):
	def radix_helper(lyst, bit, n):
		if bit >= n:
			return
		minNum = min(lyst)
		buckets = {i:[] for i in range(10)}#以10为基数，设置10个桶
		for num in lyst:
			index = int((num-minNum)/(10**bit))%10#计算桶标号
			buckets[index].append(num)
		lyst[:] = [num for i in range(10) for num in buckets[i]]
		radix_helper(lyst, bit+1, n)

	n = len(str(max(lyst)-min(lyst)))#计算归一化后的最大位数，即最大值与最小值差的位数
	radix_helper(lyst, 0, n)


def bucket_sort(lyst):
	n = max(10, len(lyst)//10)#设置至少10个、最多len/10个桶，此时平均每个桶中10个元素
	minNum = min(lyst)
	d = (max(lyst) - minNum+1)/n
	buckets = {i:[] for i in range(n)}
	for num in lyst:
		index = int((num-minNum)/d)##取整得到桶标号
		buckets[index].append(num)
	lyst[:] = [num for i in range(n) for num in sorted(buckets[i])]


if __name__ == '__main__':
	lyst = list(range(1,10001))
	from random import shuffle
	shuffle(lyst)
	# print(lyst)
	# radix_sort(lyst)
	# print(lyst)
	import time
	sorts = [bubble_sort, 
			select_sort, 
			insert_sort, 
			shell_sort_iteration, shell_sort_recursion, 
			merge_sort_recursion, merge_sort_iteration, 
			quick_sort_recursion, quick_sort_iteration,
			heap_sort, 
			count_sort, 
			radix_sort_iteration, radix_sort_recursion, 
			bucket_sort]
	for sort in sorts:
		start = time.time()
		sort(lyst[:]) 
		print(f"Time used by {sort.__name__}:", time.time()-start)

"""
Time used by bubble_sort: 10.429074764251709
Time used by select_sort: 3.9225099086761475
Time used by insert_sort: 4.868975877761841
Time used by shell_sort_iteration: 0.07384204864501953
Time used by shell_sort_recursion: 0.0568084716796875
Time used by merge_sort_recursion: 0.049866437911987305
Time used by merge_sort_iteration: 0.07679462432861328
Time used by quick_sort_recursion: 0.02994680404663086
Time used by quick_sort_iteration: 0.032884836196899414
Time used by heap_sort: 0.07779192924499512
Time used by count_sort: 0.004985332489013672
Time used by radix_sort_iteration: 0.028949260711669922
Time used by radix_sort_recursion: 0.02690863609313965
Time used by bucket_sort: 0.006009101867675781
"""