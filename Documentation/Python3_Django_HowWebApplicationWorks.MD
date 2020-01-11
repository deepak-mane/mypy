# Python3 - Django : How Web Application Works?

If you understand how web applications work generally how the general principle of web application work then it becomes a lot easier to understand when I start implementing like when you start talking about it as without net Django No. Download the rest you will you will understand the pattern everything follows the same pattern and that is basically why I've decided to dedicate this section to kind of like putting you through how web applications work so that you understand the core concepts and how everything works. [To see the big picture](./images/HowWebApplicationWorks.PNG?raw=true). So in this particular section we'll be we'll be competent through lectures.

Basically 
- [We'll look at data communication pattern](./Python3_Django_HowWebApplicationWorks.MD#data-dommunication-pattern) 
- [We'll look at data storage pattern](./Python3_Django_HowWebApplicationWorks.MD#data-storage-pattern)
- [We'll look at data presentation pattern](./Python3_Django_HowWebApplicationWorks.MD#data-presentation-pattern)

so every web application is made up of these three components. How does the Web application communicate with the browser and how does the Web application store  the data. Because the core at the heart of every web application is your ability to store data and your ability to search through those data and the ability to retrieve those data and your ability to audit. They did that in the database so data storage is the key component of every application. Then another key component of web application is data presentation because most of the cases you want to be able to do that I presume you want to be able to present the information you are retrieving to the user you can present the information through the through like your web page you get the information could also be presented to lucky if you are talking about rest api just the raw data you can that's all locked in if you're working with console application you can display the information on the console what for the sake of this web application we'll be looking at how to present information on the web so that our presentation is a key component of every application but that's basically why I've included this so if you understand this three component you've pretty much understood how how web applications work did not.

So on the big picture before I conclude this introduction on the big picture I just want to show you the big picture of how web applications work but this is basically a big picture showing how web applications work that essentially your web you have the user these the user like yourself trying to assess what Web the Web address via your browser. So now you have the web server the web server is bsically where your application is hosted your application is hosted in their web server so your application has it database is fast information your application also has static files statics file these real you see all the hasty email templates you would display to the user all the haste DMA pages the pages the pages of your web application do you have the user assessing the browser assessing a web application who study in their sidebar via their browser on he's on his local mission.

So what these are those is that they use the word type in the address of their web application or the web server in their browser then the browser will communicate to the web server and what the Web site does is the web server we send the request of the web application that the web application we get the data fetch the data and also get the template etched in my template map the data into the template and return on the information onto the web server then the web server we said we sent a food ACMA page to the browser then the browser we kind of like load the food done and should the user. The web page is visibly how how it works is generally key in the address of the Web site via the web.

We had the web browser application look at it the browser we sent a message to the web server that works of our who has the is hosting the web application that the web server we always talk to the web application it is the duty of the application to fetch the data and gets the ACMA template map the time today the appropriate data and appropriate ACMA file together and then send the food fire to the brand to the web server the works of our will now send the full ACMA pasted your browser the browser will not display the page a full Dom page to the user that the user can use the user will generally be assessed and will be using like your desktop or your laptop you know are your or your tablets. But this basically how web applications work the big picture.
## Big Picture
![Alt text](../images/HowWebApplicationWorks.PNG?raw=true "Title")

## Data Dommunication Pattern. 
- Main Actors: The environment of a web application consists of the following :
  + Client : This is the browser
  + Network : This is the Internet(www) which serves as communication channel between webserver and browser.
  + Webservers : This os where our application lives.
  + Apps (Build in Webserver) - This is you web application. It runs on the Webserver. This what we will build on Django.
- The Rule of Engagement: HTTP - HyperText Transfer Protocol, how browser interacts with webserver. How message's are sent.
- Resources, URL and Routers - 
  + Resources : Anything that can be obtained from the web (Includes web pages, information from database)
  + URL : Uniform Resource Locator, specifies the address of a resources that is located on a webserver.
  + Routers : A router is a schema located within the webserver that maps a URL to a specific Resources.
- Request and Response:
  + Http Request are the messages that the client sends to the server.There are different types of request that the client can send to the server. These include.
    + Http Get Request: This is used to retrieve data from the server.
    + Http Post Request: This is used to send data to the server.
    + Http Put Request: This is used to replace a specific data with a new data.
    + Http Delete Request: This is used to delete a specific data in the server.
  + Http Response is the message the server returns to the client in response to a request. Http Response has two parts:
    + Response Header: This contains additional information about the data that is being requested such as its content type, when it was last updated, and if the data is to cached.
    + Response Body: This is the main body of the message containing the data that is requested.
    
    ![Alt text](../images/RequestAndResponse.PNG?raw=true "Title") 
    
- Types of Response: The response from the webserver is usually of two types:
  + Html Content
  + Non-Html Content: such as below
    + Plain text
    + Images
    + Documents (pdf,word,excel,csv)
    + Audio clips
    + Video clips    
- Request Handlers: These are ususally framework specific class objects that implement methods that accepts the http request, processes that request and returns a http response. This reponse can be either *html* or *non-html* content. For HTML content, the hdandler specifies the template to render and any associated data that the template may need.

    ![Alt text](../images/RequestHandlers.PNG?raw=true "Title") 
    
## Data Storage Pattern. 
- Types of Data
  + Static Data: Dates doesn't change often. Ex: HTML,CSS,JavaScript files,Images,Video
  + Dynamic Data: Data changes frequently. Ex: Data stored in database,like inventory of books on ecommerce website.
- The Database
  + Web is all about transmitting data between the client and the webserver. Huge amount of information needed to be stored so that they can be queried for any relevant information.
  + Database is a computer system that allows us to store information so that they can searched and retrieved.
  + Ex: MySWL,MSSQL,Sqlite,Mongo,PostgreSQL
- SQL : Structured Query Language is used to communicate to Database , and peform create,read,update and delete.
- Object Relational Mapper - ORM : ORM enables object oriented programming languages to represent the database as an object allowing us to manipulate the database using the programming constructs.Some examples of ORM are:
  + Entity Framework
  + Hibernate
  + NHibernate
  + Dapper
  + Eloquent

## Data Presentation Pattern 


