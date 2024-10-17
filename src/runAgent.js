import dotenv from 'dotenv';
import OpenAI from "openai";
const configuration = { apiKey: process.env.OPENAI_API_KEY };

dotenv.config();

const sleep = (ms) => new Promise((resolve) => setTimeout(resolve, ms));



// Configuration for the OpenAI client.
const client = new OpenAI(configuration);

// Enter your Assistant ID here.
const ASSISTANT_ID = "asst_VHUser1fAmMqSubO31QRf";

async function main() {
    // Create a thread with a message.
    let createResponse = await client.betaThreadsCreate({
        messages: [
            {
                role: "user",
                // Update this with the query you want to use.
                content: "5 * 5 + 15",
            }
        ]
    });

    let thread = createResponse.data;
    console.log(`👉 Thread Created: ${thread.id}`);

    // Submit the thread to the assistant (as a new run).
    let run = await client.betaThreadsRunsCreate({
        thread_id: thread.id,
        assistant_id: ASSISTANT_ID
    });

    console.log(`👉 Run Created: ${run.data.id}`);

    // Wait for run to complete.
    while (run.data.status !== "completed") {
        run = await client.betaThreadsRunsRetrieve({
            thread_id: thread.id,
            run_id: run.data.id
        });
        console.log(`🏃 Run Status: ${run.data.status}`);
        await sleep(1000);
    }

    console.log(`🏁 Run Completed!`);

    // Get the latest message from the thread.
    let messagesResponse = await client.betaThreadsMessagesList({
        thread_id: thread.id
    });
    let messages = messagesResponse.data;

    // Print the latest message.
    let latestMessage = messages[messages.length - 1]; // Assuming latest message is at the end
    console.log(`💬 Response: ${latestMessage.content}`);
}

main();

