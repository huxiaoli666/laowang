class Person:
	#######人类############
	def __init__(self,name):
		self.name = name
		self.gun = None  #人手里的枪
		self.xue = 100
	#老王安装子弹到弹壳中
	def putBullToClap(self,clip,bullet):
		#子弹保存到弹夹里边
		clip.baocunBullet(bullet)

	def putClipToGun(self,clip,gun):
		#保存弹夹到枪中
		gun.baocunClip(clip)  

	#拿枪方法
	def naqiang(self,gun):
		self.gun = gun  #把枪赋值给老王

	def koubanji(self,diren):
		#枪开火
		self.gun.fire(diren)

	def diaoxue(self,typeBull):
		if self.xue >0:
			self.xue -= typeBull   #打中敌人一次，相应的减少血量

	def __str__(self):
		if self.gun:
			return "%s的血量为:%d,他有枪%s"%(self.name,self.xue,self.gun)
		else:
			if self.xue>0:
				return "%s的血量为%d,他没有枪"%(self.name,self.xue)
			else:
				return "%s已挂..."%(self.name)
class Gun:
	######枪类###########
	def __init__(self,name):
		self.name = name  #name 哪种枪
		self.baocun1 = None  #默认情况下，为none   且不能重名    弹夹
	def baocunClip(self,clip):
		if not self.baocun1:  #判断有没有问题，可写可不写    只保存一份
			self.baocun1 = clip   #self.baocun1不是空的值，已经有值了

	#开火
	def fire(self,diren):
		zidan_temp = self.baocun1.jianshaozidan()  #减少子弹的时候判断子弹是否有子弹

		if zidan_temp:   #判断子弹是否成功    代表条件为真
			zidan_temp.dazhong(diren)  


	def __str__(self):
		if self.baocun1:   
			return "当前枪的信息为%s,当前有弹夹"%(self.name)
		else:
			return "当前枪的信息为%s,当前没有弹夹"%(self.name)

class Clip:
	######弹夹######
	def __init__(self,numMax):
		self.numMax = numMax
		self.baocun = []   #放多个子弹 保存子弹

	def baocunBullet(self,bullet):
		#将子弹添加到弹夹里边
		self.baocun.append(bullet)

	#减少子弹
	def jianshaozidan(self):
		if self.baocun:  #判断有没有子弹
			return self.baocun.pop()    #pop代表去除到最后一个  最后一个子弹弹出，说明开火成功
		else:
			return None    #没有子弹的时候，返回None

	def __str__(self):           #测试结果
		return "当前弹夹的状态为%d/%d"%(len(self.baocun),self.numMax)                   #当前弹夹的状态是

class Bullet:
	######子弹类#######
	def __init__(self,typeBull): #  typeBull 代表杀伤力
		self.typeBull = typeBull

	def dazhong(self,diren):
		#敌人掉血
		diren.diaoxue(self.typeBull)

def main():
	#有老王对象
	laowang = Person("老王")
	#枪对象
	qbz95 = Gun("qbz95")
	#弹夹对象
	clip = Clip(20)

	for i in range(10):    #放了10个子弹
		#一堆子弹
		bullet = Bullet(10)
		#老王将子弹放到弹夹中
		laowang.putBullToClap(clip,bullet)

	#将弹夹放到枪中
	laowang.putClipToGun(clip,qbz95)   #弹夹，枪
	# print(qbz95)   #测试
	
	
	#有敌人
	gebilaowang = Person("隔壁老王")
	#老王拿枪
	laowang.naqiang(qbz95)

	#打敌人
	laowang.koubanji(gebilaowang)
	laowang.koubanji(gebilaowang)
	laowang.koubanji(gebilaowang)
	laowang.koubanji(gebilaowang)
	laowang.koubanji(gebilaowang)
	laowang.koubanji(gebilaowang)
	laowang.koubanji(gebilaowang)
	laowang.koubanji(gebilaowang)
	laowang.koubanji(gebilaowang)
	laowang.koubanji(gebilaowang)
	laowang.koubanji(gebilaowang)

	print(laowang)
	print(gebilaowang)


if __name__ == "__main__":
	main()
