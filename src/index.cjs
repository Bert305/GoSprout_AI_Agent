const {Configuration, OpenAIApi} = require("openai");

const config = new Configuration({
    apiKey: process.env.OPENAI_API_KEY
});

const openai = new OpenAIApi(config);

// const runPrompt = async (prompt) => {
//     let response = await openai.createCompletion({
//         model: "text-davinci-003",
//         prompt: prompt,
//         max_tokens: 100
//     });

//     return response.data.choices[0].text;
// }

const runPrompt = async () => {
    const prompt = "5 * 5 + 15";
    const response = await openai.createCompletion({
        model: "text-davinci-003",
        prompt: prompt,
        max_tokens: 100,
        temperature: 1
    });

    console.log(response.data.choices[0].text);
}

runPrompt();