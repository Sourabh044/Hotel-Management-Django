from django.db import models
# from Bill import models
# Create your models here.
# class user(AbstractBaseUser):
#     id = models.AutoField(primary_key=True, editable=False , unique=True)
#     Name = models.CharField(max_length=256)
#     # Phone_No = models.CharField(max_length=10 , unique=True)
#     email = models.EmailField(max_length=254 , unique= True)
#     genderChoice = [('M','Male'),('F', 'Female')]
#     mobile = models.CharField(max_length=12, unique=True)
#     Check_in = models.DateField(null=True)
#     Check_out =models.DateField(null=True)
#     # BookingId = models.AutoField(editable=True , null= True)  
#     RoomNo = models.IntegerField( null = True, unique=True)
#     gender = models.CharField(max_length=6, choices=genderChoice)
#     active = models.BooleanField()
#     staff = models.BooleanField()
#     admin= models.BooleanField()
#     dateofbirth = models.DateField()
   
#     USERNAME_FIELD = "email"
#     # REQUIRED_FIELDS=[]
#     objects =UserManager()
    
#     @property
#     def is_staff(self):
#         return self.staff
    
    
#     @property
#     def is_admin(self):
#         return self.admin

#     @property
#     def is_active(self):
#         return self.active
    
    
#     def get_fullname(self):
#         return self.Name

# class UserManager(BaseUserManager):
#    def create_user(self,name, mobile,email,dateOfbirth, gender, isActive=True, isAdmin=False, isStaff=False,password=None):
#        if not mobile:
#            raise ValueError("Mobile Number is required")
#        if not email:
#            raise ValueError("EmailId is required")
#        if not password:
#            raise ValueError("Password is required")
       
#        user_obj =self.model(
#            email = self.normalize_email(email),
#            mobile = mobile,
#            name = name,
#        )
#        user_obj.dateOfbirth = dateOfbirth
#        user_obj.gender = gender
#        user_obj.active = isActive
#        user_obj.staff  = isStaff
#        user_obj.admin = isAdmin
#        user_obj.set_password(password)
#        user_obj.save(using=self._db)
#        return user_obj

#    def create_superuser(self,email, isActive=True, isAdmin=True, isStaff=True, password = None):
#        user_obj =self.model(
#            email = email #(if ucmnt this then add the  mobile in the defination)
#        )
#        user_obj.email = email
#        user_obj.active = isActive
#        user_obj.staff  = isStaff
#        user_obj.admin = isAdmin
#        user_obj.set_password(password)
#        user_obj.save(using=self._db)
#        return user_obj

#    def create_staffuser(self,name, mobile,email,dateOfbirth, gender, isActive=True, isAdmin=False, isStaff=True,password=None):
#        user_obj =self.model(
#            email = self.normalize_email(email),
#            mobile = mobile,
#            name = name,
#        )
#        user_obj.dateOfbirth = dateOfbirth
#        user_obj.gender = gender
#        user_obj.active = isActive
#        user_obj.staff  = isStaff
#        user_obj.admin = isAdmin
#        user_obj.set_password(password)
#        user_obj.save(using=self._db)
#        return user_obj


# class user(models.Model):
#     id = models.AutoField(primary_key=True, editable=False , unique=True)
#     Name = models.CharField(max_length=200)
#     Phone_No = models.CharField(max_length=10 , unique=True)
#     Email = models.EmailField(max_length=254 , unique= True)
#     Check_in = models.DateField(null=True)
#     Check_out =models.DateField(null=True)
#     # BookingId = models.AutoField(editable=True , null= True)
#     RoomNo = models.IntegerField( null= True, unique=True)

#     def __str__(self):
#         return self.Name