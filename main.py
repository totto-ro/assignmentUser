from User import User

adrienUser = User( "Adrien")
adrienUser.deposit( 101 )
adrienUser.deposit( 101 )
adrienUser.deposit( 201 )
adrienUser.withdraw( 101 )
adrienUser.printInfo()

mrNibblesUser = User( "Mr. Nibbles")
mrNibblesUser.deposit( 1200 )
mrNibblesUser.deposit( 2200 )
mrNibblesUser.withdraw( 1200 )
mrNibblesUser.withdraw( 1000 )
mrNibblesUser.printInfo()

bennyUser = User( "Benny Bob")
bennyUser.deposit( 1500 )
bennyUser.withdraw( 1000 )
bennyUser.withdraw( 5000 )
bennyUser.withdraw( 3000 )
bennyUser.printInfo()

adrienUser.transfer( bennyUser, 250 )
adrienUser.printInfo()
bennyUser.printInfo()