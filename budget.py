class Category:

      def __init__(self,category_name):
        self.name=category_name
        self.ledger=list();

      def __str__(self):
        name_length=len(self.name);
        tick_length=30-name_length;
        start_ticklength=tick_length//2;
        end_ticklength=tick_length-start_ticklength
        title="*" * start_ticklength + self.name+"*" *end_ticklength+"\n"
        eachline="";
        for item in self.ledger:
            describe = item["description"][0:23];
            if len(describe)<23:
               describe=describe + " "*(23-len(describe));
            eachline +=   describe + format(item["amount"],".2f").rjust(7)+"\n"
        total="Total: "+str(self.get_balance()); 
        output=  title+  eachline+ total;  
        return output

      def deposit(self,amount,description=""):
         self.ledger.append({"amount":amount,
                            "description":description}); 

      def withdraw (self,amount,description=""):
         boolean = self.check_funds(amount);
         if (boolean):
           self.ledger.append({"amount":-amount,
                            "description":description}); 
           return True;
         else:
           return False;

      def get_balance (self):
       total=0;
       for item in self.ledger:
            total+=item["amount"];    
       return total; 

      def transfer(self,amount,other_category):
         boolean = self.check_funds(amount);
  
         if (boolean):
             self.withdraw(amount,"Transfer to "+other_category.name )
             other_category.ledger.append({"amount":amount,
                            "description":"Transfer from "+self.name}); 

             return True;
         else:
             return False; 

      def check_funds (self,amount):
            total=self.get_balance();   
            if (total<amount):
                  return False;
            else:
                  return True;     
                                
       

                                             




def create_spend_chart(categories):

  percent = [100,90,80,70,60,50,40,30,20,10,0];
  cat_name=get_catname(categories);
  max_len=max(cat_name,key=len);
  cat_percents=get_percents(categories);
  output = "Percentage spent by category\n"
  for item in percent:
    i=0;
    align =2;
    input=str(item)+"|"
    output+=input.rjust(4);
    while (i<len(cat_percents)):
       if item in cat_percents[i]:
         output+="o".rjust(align);
       else:
         output+=" ".rjust(align); 
       align=3;  
       i+=1; 
    output+="  \n"   
  output+="----------\n".rjust(14);

  j=0;
  while(j<len(max_len)):
    output+="/n ".rjust(4); 
    for item in cat_name:
       if(j<len(item)):
         output+=item[j].rjust(3);
       else:
         output+=" ".rjust(3);
    output+="  "      
    j+=1;      
  return output    



         

def get_catname(categories):
  category_name=list();
  i = 0;
  for item in categories:
      category_name.append(item.name);
  return category_name;  

def get_percents(categories):
  withdraw_perc=list();
  i = 0;
  for item in categories:
      withdraw_perc.append([]);
      rounded=0;
      total_depo=total_deposit(item);
      for entry in item.ledger:
         if (entry["amount"]<0):   
            perc= ((-entry["amount"])*100)/total_depo;
            rounded =round(perc/10)*10;
            withdraw_perc[i].append(rounded);
      i+=1; 
  return withdraw_perc;   

def total_deposit(category):
     total=0;
     for entry in category.ledger:
         if (entry["amount"]>0):
             total+=entry["amount"];
     return total;    
   

