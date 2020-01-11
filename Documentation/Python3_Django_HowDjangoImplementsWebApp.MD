# Python3 - Django : How Django Implements Web Applications ?

[Key points:]()
1. [Understanding The MVC Pattern](./Python3_Django_HowDjangoImplementsWebApp.MD#understanding-the-mvc-pattern)
1. [Django's Approach](./Python3_Django_HowDjangoImplementsWebApp.MD#djangos-approach)
1. [Django Model](./Python3_Django_HowDjangoImplementsWebApp.MD#django-model)
1. [Django View](./Python3_Django_HowDjangoImplementsWebApp.MD#django-view)
1. [Django Template](./Python3_Django_HowDjangoImplementsWebApp.MD#django-template)
1. [Django Router and URLs](./Python3_Django_HowDjangoImplementsWebApp.MD#django-router-and-urls)

## Understanding The MVC Pattern
- MVC Overview:
  + MVC stands for Model View Controller and basically used for designing software
  + This pattern separates an application into 3 Basic components
    - <b>The Model:</b>
      + The model is basically the representation of your data.Model is the part of the application that handles the data on the logic associated with the real life object like for example in the real life object if you have the book then definitely you know that a book has what in the number of pages the book has what the author's the book has what the dimension. So these are the attribute these are the physical attributes of the book to a basically and maybe if it is a professional object like something that performs action then there are also the actions that the object performs in the real life. Like if I'm modelling that dog or a cat this a dog then a dog grows a dog come back. So the action that can be performed by dog is is part of what the lodge. The properties are the attributes of that particular object so the the the the more the basically handles the data and logic for the physical object that the software the presentation of the physical object than the model also allows us to see its data to the database and to also retrieve its data from the database. So basically in some cases you are in some cases you can use objects that relational mapper to save all the or you'd need to do just see the whole object in the database the object lesson number part picks up all the attributes and right Eskil where as Carl commands that you perform the same thing but basically all the data about the the the the real what object is physically housed is contained in the model.

    - <b>The View:</b>
      + The view the view is responsible for rendering the presentation of the data to the user a capsule it did what in the data that we are modelling so the view is essentially a kind of like a template that shows how this the information about a model should be displayed to a user it's kind of a formatted mechanism of formatting it just like a template one or what it template is a template is something that specified the formats and then when you want to create to just fill in the the the the the the the black disperses to essentially a view is basically shows the formatting of how information should be displayed to the user information about a model should be displayed to the user and we know that the viewer can do you could render  mere content your view could also render like non-html like csv,pdf,word,video,audio,etc. So there are views that go format information in these particular types lacks the GP PDA of war and all the rest. In addition to being able to also render hasty email content and most of the case is not the common one. So the view with format or the or the or the hasty email attacks and also puts the formatting for we are dynamic data will be automatically inserted in our at runtime by the view engine. But that's basically what the viewer does the view is implemented in template.

    - <b>The Controller:</b>
      + The controller is a socially responsible for accepting you to be a request that they jump off the controller as to when that will. When I was talking about how web applications work I made mention of the their request handle last and the controller is a request handler.  So the controller implements method and those methods are substation to be a request and what produce he should be arrested on. So that's basically what they do and their response is usually the response from the controller is usually the data and the templates does demand the basic response that they are the result that comes out of the method within the controller. It is usually the template to use and the data to use without templates in as the name suggests the controller handles users request and responses. It's mediates between the model and the view. So essentially what they did the controller does is will it accept the request from the his shitty pull request and then it depends on the type of entity requests that it is accepted. This say if it is assumption their request to get it to get a data to get something and displayed to the user then it will go to the to the database. If they assume it is stored in the database or whatever it is stored it gets that information. Then depending on whether you want to depending on the format of the data you would at this hash GMO content on his GMO content e.g. specified that appropriate templates to use and then it would give the template and the data to the view engine then gives you engine this along the pipeline. If you take this to item and generic the hasty email or see as your PDA that will be returned to the user.

##  Benefits of using the MVC patterns: 
- It makes it it makes it a lot easier to manage complex application noise issue.
- You divide the application into model view controller then because you are dividing your application to model view controller it makes it easier to manage complex application.
- It also works well for applications with many developers also some is on in large scale applications. Some developers will be working on the front end so were working on the back end to it because this is these natural valleys is split into like model view controller. 
- They view as many women VCAT views mainly the front end part so those those developers are responsible for the front end but. Could be would be able to like you know walk separately from those was creating the model and the controller but it makes it easier to walk in the largest field in the larger project. It also works well for application with many developer.
- It provides that support for a test drive in development because you can do your model and test your model separately.
- You can do your control and test your controller separately.You know they are not tied together.dd They are separate things so you can do that separately and test them separately in a division is almost always also the same. You can test drive and see that the G is working without you having the model no controller ready.

__*Test driven development basically is a method of developing software where in you stop by while writing tests for your application in before you did that the application to kind of like proof that the test has passed*__
    
   ![Alt text](../images/MVCOverview.PNG?raw=true "Title") 
        
## Django's Approach
- Django follows the MVC pattern with some difference


## Django Model
- Django Model serves the same purpose as in traditional MVC. Django model is responsible for passing data into and out of database.

## Django View
- Django view works differently from the traditional MVC View. In Django, the Views - which are mainly python functions- defines the data to display from the Model. It more of less does what the MVC Controllers do, in terms of managing the Model data. The framework itself handle the duties of the controller.

## Django Template
- Django Template is similar to the MVC View in that it contains the HTML snippets and formatting logic that specifies how data should be rendered to the user.

   ![Alt text](../images/MappingDjangoMTC_TraditionalMVC.PNG?raw=true "Title") 
   ![Alt text](../images/DjangoApplicationStructure.PNG?raw=true "Title") 
   ![Alt text](../images/DjangoApplicationStructure1.PNG?raw=true "Title") 
      ![Alt text](../images/DjangoApplicationStructure2.PNG?raw=true "Title") 
         ![Alt text](../images/DjangoApplicationStructure3.PNG?raw=true "Title") 
## Django Router and URLs





















