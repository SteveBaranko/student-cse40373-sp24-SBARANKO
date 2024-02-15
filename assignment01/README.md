# cse40373-sp24
ND CSE 40373 - Embedded System Development
Steven Baranko
sbaranko

Hello! This is my first project for Embedded Systems! This one might be kinda iffy, so please 
read if you are struggling to follow along. 

To run the code, just open two terminal instances. Run the client and server code, respectively.
You will want to enter a valid instance of a beacon. I have no idea how a user might figure it out,
but you can test it with TESS-STATIC-00716 which should work. Exit the client code with 
exit

Some quirky little aspects of this code 

  The python code does all of its request handling after preprocessing a single request. I am not 
  sure that this is right. It doesn't feel right, but it seems to work and take like less than a 
  half a second so I am rolling with it. 

  I use scanf in my C code which makes me cringe. However, given what we are doing, I don't expect 
  overflow attacks at the moment, and sscanf will return data every time. 
  This saved me from having to check if we have something idstinct from an empty buffer, which is nice

  I have a weird line where I remove whitespace, 

  I have a weird line in my server.py with a lot of string math. Basically, I could not 
  figure out why the index was not exactly the same as the string I entered. So, 