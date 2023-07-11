const PORT = 8000
const express = require("express")
const cors = require("cors")
const app = express()

app.use(cors())

const username = process.env.USERNAME
const password = process.env.PASSWORD

app.get("/deals", async (req, res) => {
    try {
        const body = {
            source: "amazon_search",
            domain: "com",
            query: "deal of the day",
            parse: true,
            pages: 1,
        }
        const response = await fetch("https://realtime.oxylabs.io/v1/queries", {
            method: "POST",
            body: JSON.stringify(body),
            headers: {
                "Content-Type": "application/json",
                Authorization: "Basic " + Buffer.from(`${username}:${password}`).toString("base64"),
            },
        })

        console.log(await response.json())
    } catch (err) {
        console.error(err)
    }
})

app.listen(PORT, () => console.log(`DiscountFinder app listening on port ${PORT}!`))