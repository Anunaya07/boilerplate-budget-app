class Category:
  def __init__(self,category):
    self.category=category
    self.total=0
    self.withdraw_money=0
    self.ledger=[]
  def check_funds(self,amount):
    if self.total>=amount:
      return True
    return False

  def deposit(self,amount,description=''):
    self.total+=amount
    self.ledger+=[{"amount":amount,"description":description}]

  def withdraw(self,amount,description=''):
    if self.check_funds(amount):
      self.withdraw_money+=amount
      self.ledger+=[{"amount":-amount,"description":description}]
      return True
    return False

  def get_balance(self):
    return self.total-self.withdraw_money

  def transfer(self,amount,category):
    if self.withdraw(amount,f"Transfer to {category.category}"):
         category.deposit(amount,f"Transfer from {self.category}")
         return True
    return False
  
  def __repr__(self):
    n=len(self.category)
    return_str=''
    length=30-n
    starting_point=length//2
    return_str+="*"*(starting_point)
    return_str+=f"{self.category}"
    return_str+="*"*(30-n-starting_point)
    return_str+='\n'
    for i in self.ledger:
      list_keys=list(i.keys())
      desp_key=list_keys[1]
      desp_val=i[desp_key]
      amount_key=list_keys[0]
      amount=' '+format(i[amount_key],".2f")
      n=len(amount)
      desp_val=desp_val[:30-n]
      m=len(desp_val)
      return_str+=desp_val+' '*(30-n-m)+amount
      return_str+='\n'
      total=format(self.total-self.withdraw_money,".2f")
    return_str+="Total: "+total
    return return_str


def create_spend_chart(categories):
  
  percent_list=[]
  total=0
  for i in categories:
      total+=i.withdraw_money
  for i in categories:
    percent=(i.withdraw_money/total)*100
    if percent<10:
      percent_list+=[0]
    else:
     percent=round(percent/10)*10
     percent_list+=[percent]

  return_str='Percentage spent by category\n'
  for i in range(100,-1,-10):
    if i==100:
     return_str+=f"{i}|"
    elif i==0:
      return_str+=f"  {i}|"
    else:
        return_str+=f" {i}|"
    for j in range(len(percent_list)):
      if j==0:
        if i<=percent_list[j]:
          return_str+=' o'
        else:
          return_str+='  '
      else:
        if i<=percent_list[j]:
          return_str+='  o'
        else:
          return_str+='   '
    return_str+='  \n'
  return_str+=' '*4
  return_str+='--'*len(categories)+'----\n'
  return_str+='    '
  max_length=0
  for i in categories:
    if max_length<len(i.category):
      max_length=len(i.category)
  for i in range(len(categories)):
      n=len(categories[i].category)
      categories[i].category=categories[i].category+' '*(max_length-n)
  for i in range(max_length):
    for j in range(len(categories)):
      if j==0:
        return_str+=f' {categories[j].category[i]}'
      else:
        return_str+=f'  {categories[j].category[i]}'
    return_str+='  \n    '
  return return_str[:len(return_str)-5]





  
