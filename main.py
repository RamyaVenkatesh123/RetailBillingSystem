from tkinter import *
from tkinter import messagebox
import tkinter as tk
import random,os,tempfile,smtplib
#functionality part

def clear():
     bathsoapEntry.delete(0,END)
     facecreamEntry.delete(0,END)
     facewashEntry.delete(0,END)
     hairgelEntry.delete(0,END)
     hairsprayEntry.delete(0,END)
     bodylotionEntry.delete(0,END)
     riceEntry.delete(0,END)
     oilEntry.delete(0,END)
     sugarEntry.delete(0,END)
     wheatEntry.delete(0,END)
     daalEntry.delete(0,END)
     teaEntry.delete(0,END)
     spriteEntry.delete(0,END)
     maazaEntry.delete(0,END)
     frootiEntry.delete(0,END)
     dewEntry.delete(0,END)
     pepsiEntry.delete(0,END)
     cokeEntry.delete(0,END)

     bathsoapEntry.insert(0,0)
     facecreamEntry.insert(0,0)
     facewashEntry.insert(0,0)
     hairgelEntry.insert(0,0)
     hairsprayEntry.insert(0,0)
     bodylotionEntry.insert(0,0)
     daalEntry.insert(0,0)
     oilEntry.insert(0,0)
     riceEntry.insert(0,0)
     wheatEntry.insert(0,0)
     sugarEntry.insert(0,0)
     teaEntry.insert(0,0)
     spriteEntry.insert(0,0)
     dewEntry.insert(0,0)
     pepsiEntry.insert(0,0)
     cokeEntry.insert(0,0)
     maazaEntry.insert(0,0)
     frootiEntry.insert(0,0)

     cosmaticpriceEntry.delete(0,END)
     grocerypriceEntry.delete(0,END)
     drinkspriceEntry.delete(0,END)

     cosmatictaxEntry.delete(0,END)
     grocerytaxEntry.delete(0,END)
     drinkstaxEntry.delete(0,END)

     nameEntry.delete(0,END)
     phoneEntry.delete(0,END)
     billnoEntry.delete(0,END)

     textarea.delete(1.0,END)

def printBill():
     if textarea.get(1.0,END)=='\n':
          messagebox.showerror('Error','Bill is empty')
     else:
          file=tempfile.mktemp('.txt')
          open(file,'w').write(textarea.get(1.0,END))
          os.startfile(file,'print')
          

def searchBill():
     for i in os.listdir('bills/'):
          if i.split('.')[0]==billnoEntry.get():
               f=open(f'bills/{i}','r')
               textarea.delete(1.0,END)
               for data in f:
                    textarea.insert(END,data)
               f.close()
               break
          else:
               messagebox.showerror('Error','Invalid Bill number')

def send_email():
     def send_gmail():
          try:
               ob=smtplib.SMTP('smtp.gmail.com',587)
               ob.starttls()
               ob.login(senderEntry.get(),passwordEntry.get())
               message=email_textarea.get(1.0,END)
               ob.sendmail(senderEntry.get(),receiverEntry.get(),message)
               ob.quit()
               messagebox.showinfo('Success','Bill is successfully sent',parent=root1)
          except smtplib.SMTPAuthenticationError:
               messagebox.showerror('Authentication Error', 'Failed to authenticate. Check your Gmail credentials.', parent=root1)
          except smtplib.SMTPException as e:
               messagebox.showerror('SMTP Error', f'Something went wrong while sending the email: {str(e)}', parent=root1)
          except Exception as e:
               messagebox.showerror('Error', f'An unexpected error occurred: {str(e)}', parent=root1)
     if textarea.get(1.0,END)=='\n':
          messagebox.showerror('Error','Bill is empty')
     else:
          root1=tk.Toplevel()
          root1.title('Send Email')
          root1.config(bg='gray20')
          root1.resizable(0,0)
          

          senderFrame=LabelFrame(root1,text='SENDER',font=('arial',16,'bold'),bd=6,bg='gray30',fg='white')
          senderFrame.grid(row=0,column=0,padx=40,pady=20)

          senderLabel=Label(senderFrame,text="Sender's Email",font=('arial',14,'bold'),bg='gray30',fg='white')
          senderLabel.grid(row=0,column=0,padx=10,pady=8)
          senderEntry=Entry(senderFrame,font=('arial',14,'bold'),bd=2,width=23,relief=RIDGE)
          senderEntry.grid(row=0,column=1,padx=10,pady=8)

          passwordLabel=Label(senderFrame,text="Password",font=('arial',14,'bold'),bg='gray30',fg='white')
          passwordLabel.grid(row=1,column=0,padx=10,pady=8)
          passwordEntry=Entry(senderFrame,font=('arial',14,'bold'),bd=2,width=23,relief=RIDGE,show='*')
          passwordEntry.grid(row=1,column=1,padx=10,pady=8)

          recipientFrame=LabelFrame(root1,text='RECIPIENT',font=('arial',16,'bold'),bd=6,bg='gray30',fg='white')
          recipientFrame.grid(row=1,column=0,padx=40,pady=20)

          receiverLabel=Label(recipientFrame,text="Email Address",font=('arial',14,'bold'),bg='gray30',fg='white')
          receiverLabel.grid(row=0,column=0,padx=10,pady=8)
          receiverEntry=Entry(recipientFrame,font=('arial',14,'bold'),bd=2,width=23,relief=RIDGE)
          receiverEntry.grid(row=0,column=1,padx=10,pady=8)

          messageLabel=Label(recipientFrame,text="Message",font=('arial',14,'bold'),bg='gray30',fg='white')
          messageLabel.grid(row=1,column=0,padx=10,pady=8)
          email_textarea=Text(recipientFrame,font=('arial',14,'bold'),bd=2,relief=SUNKEN,width=42,height=11)
          email_textarea.grid(row=2,column=0,columnspan=2)
          email_textarea.delete(1.0,END)
          email_textarea.insert(END,textarea.get(1.0,END).replace('=','').replace('-','').replace('\t\t','\t'))


          sendButton=Button(root1,text='SEND',font=('arial',16,'bold'),width=15,command=send_gmail)
          sendButton.grid(row=2,column=0,pady=20)


          root1.mainloop()

          



                         
     



if not os.path.exists('bills'):
     os.mkdir('bills')


billnumber=random.randint(500,1000)

def save_bill():
          global billnumber
          result=messagebox.askyesno('Confirm','Do you want to Save the Bill?')
          if result:
               billContent=textarea.get(1.0,END)
               file=open(f'bills\{billnumber}.txt','w')
               file.write(billContent)
               file.close()
               messagebox.showinfo('Success',f'Bill number {billnumber} is saved Successfully')
               billnumber=random.randint(500,1000)

def total():
    global soapprice,facecreamprice,facewashprice,hairsprayprice,hairgelprice,bodylotionprice,riceprice,oilprice,daalprice
    global sugarprice,teaprice,wheatprice,spriteprice,frootiprice,dewprice,maazaprice,cokeprice,pepsiprice
    global totalbill
    #Cosmatic price Calculation
    soapprice=int(bathsoapEntry.get())*20
    facecreamprice=int(facecreamEntry.get())*50
    facewashprice=int(facewashEntry.get())*100
    hairsprayprice=int(hairsprayEntry.get())*150
    hairgelprice=int(hairgelEntry.get())*80
    bodylotionprice=int(bodylotionEntry.get())*60

    totalcosmaticprice=soapprice+facecreamprice+facewashprice+hairgelprice+hairsprayprice+bodylotionprice
    cosmaticpriceEntry.delete(0,END)
    cosmaticpriceEntry.insert(0,f'{totalcosmaticprice} Rs')
    cosmaticTax=totalcosmaticprice*0.12
    cosmatictaxEntry.delete(0,END)
    cosmatictaxEntry.insert(0,f'{cosmaticTax} Rs')

    #grocery price Calculation
    riceprice=int(riceEntry.get())*50
    daalprice=int(daalEntry.get())*100
    oilprice=int(oilEntry.get())*120
    sugarprice=int(sugarEntry.get())*50
    wheatprice=int(wheatEntry.get())*140
    teaprice=int(teaEntry.get())*80

    totalgroceryprice=riceprice+daalprice+oilprice+sugarprice+wheatprice+teaprice
    grocerypriceEntry.delete(0,END)
    grocerypriceEntry.insert(0,f'{totalgroceryprice} Rs')
    groceryTax=totalgroceryprice*0.12
    grocerytaxEntry.delete(0,END)
    grocerytaxEntry.insert(0,f'{groceryTax} Rs')

    #cool drinks price Calculation
    maazaprice=int(maazaEntry.get())*50
    frootiprice=int(frootiEntry.get())*20
    dewprice=int(dewEntry.get())*30
    cokeprice=int(cokeEntry.get())*20
    spriteprice=int(spriteEntry.get())*45
    pepsiprice=int(pepsiEntry.get())*40

    totaldrinksprice=maazaprice+frootiprice+dewprice+spriteprice+pepsiprice+cokeprice
    drinkspriceEntry.delete(0,END)
    drinkspriceEntry.insert(0,f'{totaldrinksprice} Rs')
    drinksTax=totaldrinksprice*0.12
    drinkstaxEntry.delete(0,END)
    drinkstaxEntry.insert(0,f'{drinksTax} Rs')

    totalbill=totalcosmaticprice+totaldrinksprice+totalgroceryprice+cosmaticTax+groceryTax+drinksTax

def bill_area():
     
    if nameEntry.get()==''or phoneEntry.get()=='':
       messagebox.showerror('Error','Customer details are required')
    elif cosmaticpriceEntry.get()==''and grocerypriceEntry.get()==''and drinkspriceEntry.get()=='':
       messagebox.showerror('Error','No products are selected')
    elif cosmaticpriceEntry.get()=='0 Rs'and grocerypriceEntry.get()=='O Rs' and drinkspriceEntry.get()=='0 Rs':
       messagebox.showerror('Error','No products are selected')
    else:
         
     textarea.delete(1.0,END)

     textarea.insert(END,'\t\t** Welcome Customer **')
     textarea.insert(END,f'\nBill Number: {billnumber}\n')
     textarea.insert(END,f'\nCustomer Name: {nameEntry.get()}\n')
     textarea.insert(END,f'\nCustomer Phone Number: {phoneEntry.get()}\n')
     textarea.insert(END,'\n=======================================================')
     textarea.insert(END,'Product\t\t\t Quantity \t\t\t Price')
     textarea.insert(END,'\n=======================================================')
     if bathsoapEntry.get()!='0':
          textarea.insert(END, f'\nBath Soap \t\t\t{bathsoapEntry.get()}\t\t\t{soapprice} Rs')
     if facecreamEntry.get()!='0':
          textarea.insert(END, f'\nFace Cream \t\t\t{facecreamEntry.get()}\t\t\t{facecreamprice} Rs')
     if facewashEntry.get()!='0':
          textarea.insert(END, f'\nFace Wash \t\t\t{facewashEntry.get()}\t\t\t{facewashprice} Rs')
     if hairsprayEntry.get()!='0':
          textarea.insert(END, f'\nHair Spray \t\t\t{hairsprayEntry.get()}\t\t\t{hairsprayprice} Rs')
     if hairgelEntry.get()!='0':
          textarea.insert(END, f'\nHair Gel \t\t\t{hairgelEntry.get()}\t\t\t{hairgelprice} Rs')
     if riceEntry.get()!='0':
          textarea.insert(END, f'\nRice \t\t\t{riceEntry.get()}\t\t\t{riceprice} Rs')
     if oilEntry.get()!='0':
          textarea.insert(END, f'\nOil \t\t\t{oilEntry.get()}\t\t\t{oilprice} Rs')
     if wheatEntry.get()!='0':
          textarea.insert(END, f'\nWheat \t\t\t{wheatEntry.get()}\t\t\t{wheatprice} Rs')
     if sugarEntry.get()!='0':
          textarea.insert(END, f'\nSugar \t\t\t{sugarEntry.get()}\t\t\t{sugarprice} Rs')
     if daalEntry.get()!='0':
          textarea.insert(END, f'\nDaal \t\t\t{daalEntry.get()}\t\t\t{daalprice} Rs')
     if teaEntry.get()!='0':
          textarea.insert(END, f'\nTea \t\t\t{teaEntry.get()}\t\t\t{teaprice} Rs')
     if spriteEntry.get()!='0':
          textarea.insert(END, f'\nSprite \t\t\t{spriteEntry.get()}\t\t\t{spriteprice} Rs')
     if maazaEntry.get()!='0':
          textarea.insert(END, f'\nMaaza \t\t\t{maazaEntry.get()}\t\t\t{maazaprice} Rs')
     if frootiEntry.get()!='0':
          textarea.insert(END, f'\nFrooti \t\t\t{frootiEntry.get()}\t\t\t{frootiprice} Rs')
     if pepsiEntry.get()!='0':
          textarea.insert(END, f'\nPepsi \t\t\t{pepsiEntry.get()}\t\t\t{pepsiprice} Rs')
     if dewEntry.get()!='0':
          textarea.insert(END, f'\nDew \t\t\t{dewEntry.get()}\t\t\t{dewprice} Rs')
     if cokeEntry.get()!='0':
          textarea.insert(END, f'\nCoke \t\t\t{cokeEntry.get()}\t\t\t{cokeprice} Rs')
     textarea.insert(END,'\n------------------------------------------------')

     if cosmatictaxEntry.get()!='0.0 Rs':
          textarea.insert(END,f'\nCosmatic Tax \t\t\t\t{cosmatictaxEntry.get()}')
     if grocerytaxEntry.get()!='0.0 Rs':
          textarea.insert(END,f'\nGrocery Tax \t\t\t\t{grocerytaxEntry.get()}')
     if drinkstaxEntry.get()!='0.0 Rs':
          textarea.insert(END,f'\nCosmatic Tax \t\t\t\t{drinkstaxEntry.get()}')
          
     textarea.insert(END,f'\n\nTotal Bill \t\t\t\t{totalbill}')
     textarea.insert(END,'\n-------------------------------------------------')
     save_bill()





                         
     
   



#GUI part
root=tk.Tk()
root.title('Retail Billing System')
root.geometry('1278x685')
root.iconbitmap('icon.ico')
headingLabel=Label(root,text='Retail Billing System',font=('times new roman',30,'bold'),bg='gray20',fg='gold',bd=12,relief=GROOVE)
headingLabel.pack(fill=X)

customer_details_frame=LabelFrame(root,text='Customer Details',font=('times new roman',15,'bold'),
                                  fg='gold',bd=8,relief=GROOVE,bg='gray20')
customer_details_frame.pack(fill=X)

nameLabel=Label(customer_details_frame,text='Name',font=('times new roman',15,'bold'),bg='gray20',fg='white')
nameLabel.grid(row=0,column=0,padx=20,pady=2)
nameEntry=Entry(customer_details_frame,font=('arial',15),bd=7,width=18)
nameEntry.grid(row=0,column=1,padx=8)

phoneLabel=Label(customer_details_frame,text='Phone Number',font=('times new roman',15,'bold'),bg='gray20',fg='white')
phoneLabel.grid(row=0,column=2,padx=20,pady=2)
phoneEntry=Entry(customer_details_frame,font=('arial',15),bd=7,width=18)
phoneEntry.grid(row=0,column=3,padx=8)

billnoLabel=Label(customer_details_frame,text='Bill Number',font=('times new roman',15,'bold'),bg='gray20',fg='white')
billnoLabel.grid(row=0,column=4,padx=20,pady=2)
billnoEntry=Entry(customer_details_frame,font=('arial',15),bd=7,width=18)
billnoEntry.grid(row=0,column=5,padx=8)

searchButton=Button(customer_details_frame,text='Search',font=('arial',12,'bold'),bd=7,width=10,command=searchBill)
searchButton.grid(row=0,column=9,padx=20,pady=8)

productsFrame=Frame(root)
productsFrame.pack(fill=X)

cosmeticsFrame=LabelFrame(productsFrame,text='Cosmetics',font=('times new roman',15,'bold'),
                          fg='gold',bd=8,relief=GROOVE,bg='gray20')
cosmeticsFrame.grid(row=0,column=0)

bathsoapLabel=Label(cosmeticsFrame,text='Bath Soap',font=('times new roman',15,'bold'),bg='gray20',fg='white')
bathsoapLabel.grid(row=0,column=0,pady=9,padx=10,sticky='W')
bathsoapEntry=Entry(cosmeticsFrame,font=('times new roman',15,'bold'),bd=5,width=10)
bathsoapEntry.grid(row=0,column=1,pady=9,padx=10)
bathsoapEntry.insert(0,0)

facecreamLabel=Label(cosmeticsFrame,text='Face Cream',font=('times new roman',15,'bold'),bg='gray20',fg='white')
facecreamLabel.grid(row=1,column=0,pady=9,padx=10,sticky='W')
facecreamEntry=Entry(cosmeticsFrame,font=('times new roman',15,'bold'),bd=5,width=10)
facecreamEntry.grid(row=1,column=1,pady=9,padx=10)
facecreamEntry.insert(0,0)

facewashLabel=Label(cosmeticsFrame,text='Face Wash',font=('times new roman',15,'bold'),bg='gray20',fg='white')
facewashLabel.grid(row=2,column=0,pady=9,padx=10,sticky='W')
facewashEntry=Entry(cosmeticsFrame,font=('times new roman',15,'bold'),bd=5,width=10)
facewashEntry.grid(row=2,column=1,pady=9,padx=10)
facewashEntry.insert(0,0)

hairsprayLabel=Label(cosmeticsFrame,text='Hair Spray',font=('times new roman',15,'bold'),bg='gray20',fg='white')
hairsprayLabel.grid(row=3,column=0,pady=9,padx=10,sticky='W')
hairsprayEntry=Entry(cosmeticsFrame,font=('times new roman',15,'bold'),bd=5,width=10)
hairsprayEntry.grid(row=3,column=1,pady=9,padx=10)
hairsprayEntry.insert(0,0)

hairgelLabel=Label(cosmeticsFrame,text='Hair Gel',font=('times new roman',15,'bold'),bg='gray20',fg='white')
hairgelLabel.grid(row=4,column=0,pady=9,padx=10,sticky='W')
hairgelEntry=Entry(cosmeticsFrame,font=('times new roman',15,'bold'),bd=5,width=10)
hairgelEntry.grid(row=4,column=1,pady=9,padx=10)
hairgelEntry.insert(0,0)

bodylotionLabel=Label(cosmeticsFrame,text='Body Lotion',font=('times new roman',15,'bold'),bg='gray20',fg='white')
bodylotionLabel.grid(row=5,column=0,pady=9,padx=10,sticky='W')
bodylotionEntry=Entry(cosmeticsFrame,font=('times new roman',15,'bold'),bd=5,width=10)
bodylotionEntry.grid(row=5,column=1,pady=9,padx=10)
bodylotionEntry.insert(0,0)

groceryFrame=LabelFrame(productsFrame,text='Groceries',font=('times new roman',15,'bold'),
                          fg='gold',bd=8,relief=GROOVE,bg='gray20')
groceryFrame.grid(row=0,column=1)

riceLabel=Label(groceryFrame,text='Rice',font=('times new roman',15,'bold'),bg='gray20',fg='white')
riceLabel.grid(row=0,column=0,pady=9,padx=10,sticky='W')
riceEntry=Entry(groceryFrame,font=('times new roman',15,'bold'),bd=5,width=10)
riceEntry.grid(row=0,column=1,pady=9,padx=10)
riceEntry.insert(0,0)

oilLabel=Label(groceryFrame,text='Oil',font=('times new roman',15,'bold'),bg='gray20',fg='white')
oilLabel.grid(row=1,column=0,pady=9,padx=10,sticky='W')
oilEntry=Entry(groceryFrame,font=('times new roman',15,'bold'),bd=5,width=10)
oilEntry.grid(row=1,column=1,pady=9,padx=10)
oilEntry.insert(0,0)

daalLabel=Label(groceryFrame,text='Daal',font=('times new roman',15,'bold'),bg='gray20',fg='white')
daalLabel.grid(row=2,column=0,pady=9,padx=10,sticky='W')
daalEntry=Entry(groceryFrame,font=('times new roman',15,'bold'),bd=5,width=10)
daalEntry.grid(row=2,column=1,pady=9,padx=10)
daalEntry.insert(0,0)

wheatLabel=Label(groceryFrame,text='Wheat',font=('times new roman',15,'bold'),bg='gray20',fg='white')
wheatLabel.grid(row=3,column=0,pady=9,padx=10,sticky='W')
wheatEntry=Entry(groceryFrame,font=('times new roman',15,'bold'),bd=5,width=10)
wheatEntry.grid(row=3,column=1,pady=9,padx=10)
wheatEntry.insert(0,0)

sugarLabel=Label(groceryFrame,text='Sugar',font=('times new roman',15,'bold'),bg='gray20',fg='white')
sugarLabel.grid(row=4,column=0,pady=9,padx=10,sticky='W')
sugarEntry=Entry(groceryFrame,font=('times new roman',15,'bold'),bd=5,width=10)
sugarEntry.grid(row=4,column=1,pady=9,padx=10)
sugarEntry.insert(0,0)

teaLabel=Label(groceryFrame,text='Tea',font=('times new roman',15,'bold'),bg='gray20',fg='white')
teaLabel.grid(row=5,column=0,pady=9,padx=10,sticky='W')
teaEntry=Entry(groceryFrame,font=('times new roman',15,'bold'),bd=5,width=10)
teaEntry.grid(row=5,column=1,pady=9,padx=10)
teaEntry.insert(0,0)

colddrinksFrame=LabelFrame(productsFrame,text='Cold Drinks',font=('times new roman',15,'bold'),
                          fg='gold',bd=8,relief=GROOVE,bg='gray20')
colddrinksFrame.grid(row=0,column=2)

maazaLabel=Label(colddrinksFrame,text='Maaza',font=('times new roman',15,'bold'),bg='gray20',fg='white')
maazaLabel.grid(row=0,column=0,pady=9,padx=10,sticky='W')
maazaEntry=Entry(colddrinksFrame,font=('times new roman',15,'bold'),bd=5,width=10)
maazaEntry.grid(row=0,column=1,pady=9,padx=10)
maazaEntry.insert(0,0)

pepsiLabel=Label(colddrinksFrame,text='Pepsi',font=('times new roman',15,'bold'),bg='gray20',fg='white')
pepsiLabel.grid(row=1,column=0,pady=9,padx=10,sticky='W')
pepsiEntry=Entry(colddrinksFrame,font=('times new roman',15,'bold'),bd=5,width=10)
pepsiEntry.grid(row=1,column=1,pady=9,padx=10)
pepsiEntry.insert(0,0)

spriteLabel=Label(colddrinksFrame,text='Sprite',font=('times new roman',15,'bold'),bg='gray20',fg='white')
spriteLabel.grid(row=2,column=0,pady=9,padx=10,sticky='W')
spriteEntry=Entry(colddrinksFrame,font=('times new roman',15,'bold'),bd=5,width=10)
spriteEntry.grid(row=2,column=1,pady=9,padx=10)
spriteEntry.insert(0,0)

dewLabel=Label(colddrinksFrame,text='Dew',font=('times new roman',15,'bold'),bg='gray20',fg='white')
dewLabel.grid(row=3,column=0,pady=9,padx=10,sticky='W')
dewEntry=Entry(colddrinksFrame,font=('times new roman',15,'bold'),bd=5,width=10)
dewEntry.grid(row=3,column=1,pady=9,padx=10)
dewEntry.insert(0,0)

frootiLabel=Label(colddrinksFrame,text='Frooti',font=('times new roman',15,'bold'),bg='gray20',fg='white')
frootiLabel.grid(row=4,column=0,pady=9,padx=10,sticky='W')
frootiEntry=Entry(colddrinksFrame,font=('times new roman',15,'bold'),bd=5,width=10)
frootiEntry.grid(row=4,column=1,pady=9,padx=10)
frootiEntry.insert(0,0)

cokeLabel=Label(colddrinksFrame,text='Coca Cola',font=('times new roman',15,'bold'),bg='gray20',fg='white')
cokeLabel.grid(row=5,column=0,pady=9,padx=10,sticky='W')
cokeEntry=Entry(colddrinksFrame,font=('times new roman',15,'bold'),bd=5,width=10)
cokeEntry.grid(row=5,column=1,pady=9,padx=10)
cokeEntry.insert(0,0)

billFrame=Frame(productsFrame,bd=8,relief=GROOVE)
billFrame.grid(row=0,column=3,padx=10)

billareaLabel=Label(billFrame,text='Bill Area',font=('times new roman',15,'bold'),bd=7,relief=GROOVE)
billareaLabel.pack(fill=X)

scrollbar=Scrollbar(billFrame,orient=VERTICAL)
scrollbar.pack(side=RIGHT,fill=Y)
textarea=Text(billFrame,height=18,width=55,yscrollcommand=scrollbar.set)
textarea.pack()
scrollbar.config(command=textarea.yview)

billmenuFrame=LabelFrame(root,text='Bill Menu',font=('times new roman',15,'bold'),
                          fg='gold',bd=8,relief=GROOVE,bg='gray20')
billmenuFrame.pack()

cosmaticpriceLabel=Label(billmenuFrame,text='Cosmatic Price',font=('times new roman',14,'bold'),bg='gray20',fg='white')
cosmaticpriceLabel.grid(row=0,column=0,pady=6,padx=10,sticky='W')
cosmaticpriceEntry=Entry(billmenuFrame,font=('times new roman',15,'bold'),bd=5,width=10)
cosmaticpriceEntry.grid(row=0,column=1,pady=6,padx=10)

grocerypriceLabel=Label(billmenuFrame,text='Grocery Price',font=('times new roman',14,'bold'),bg='gray20',fg='white')
grocerypriceLabel.grid(row=1,column=0,pady=6,padx=10,sticky='W')
grocerypriceEntry=Entry(billmenuFrame,font=('times new roman',15,'bold'),bd=5,width=10)
grocerypriceEntry.grid(row=1,column=1,pady=6,padx=10)

drinkspriceLabel=Label(billmenuFrame,text='Cold Drink Price',font=('times new roman',14,'bold'),bg='gray20',fg='white')
drinkspriceLabel.grid(row=2,column=0,pady=6,padx=10,sticky='W')
drinkspriceEntry=Entry(billmenuFrame,font=('times new roman',15,'bold'),bd=5,width=10)
drinkspriceEntry.grid(row=2,column=1,pady=6,padx=10)

cosmatictaxLabel=Label(billmenuFrame,text='Cosmatic Tax',font=('times new roman',14,'bold'),bg='gray20',fg='white')
cosmatictaxLabel.grid(row=0,column=2,pady=6,padx=10,sticky='W')
cosmatictaxEntry=Entry(billmenuFrame,font=('times new roman',15,'bold'),bd=5,width=10)
cosmatictaxEntry.grid(row=0,column=3,pady=6,padx=10)

grocerytaxLabel=Label(billmenuFrame,text='Grocery Tax',font=('times new roman',14,'bold'),bg='gray20',fg='white')
grocerytaxLabel.grid(row=1,column=2,pady=6,padx=10,sticky='W')
grocerytaxEntry=Entry(billmenuFrame,font=('times new roman',15,'bold'),bd=5,width=10)
grocerytaxEntry.grid(row=1,column=3,pady=6,padx=10)

drinkstaxLabel=Label(billmenuFrame,text='Cold Drink Tax',font=('times new roman',14,'bold'),bg='gray20',fg='white')
drinkstaxLabel.grid(row=2,column=2,pady=6,padx=10,sticky='W')
drinkstaxEntry=Entry(billmenuFrame,font=('times new roman',15,'bold'),bd=5,width=10)
drinkstaxEntry.grid(row=2,column=3,pady=6,padx=10)

buttonFrame=Frame(billmenuFrame,bd=8,relief=GROOVE)
buttonFrame.grid(row=0,column=4,rowspan=3)

totalButton=tk.Button(buttonFrame,text='Total',font=('arial',16,'bold'),bg='gray20',bd=5,fg='white',width=8,pady=10,command=total)
totalButton.grid(row=0,column=0,pady=20,padx=5)
billButton=tk.Button(buttonFrame,text='Bill',font=('arial',16,'bold'),bg='gray20',bd=5,fg='white',width=8,pady=10,command=bill_area)
billButton.grid(row=0,column=1,pady=20,padx=5)
mailButton=tk.Button(buttonFrame,text='Mail',font=('arial',16,'bold'),bg='gray20',bd=5,fg='white',width=8,pady=10,command=send_email)
mailButton.grid(row=0,column=2,pady=20,padx=5)
printButton=tk.Button(buttonFrame,text='Print',font=('arial',16,'bold'),bg='gray20',bd=5,fg='white',width=8,pady=10,command=printBill)
printButton.grid(row=0,column=3,pady=20,padx=5)
clearButton=tk.Button(buttonFrame,text='Clear',font=('arial',16,'bold'),bg='gray20',bd=5,fg='white',width=8,pady=10,command=clear)
clearButton.grid(row=0,column=4,pady=20,padx=5)
root.mainloop()