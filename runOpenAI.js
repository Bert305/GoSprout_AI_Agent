const { spawn } = require('child_process');
const path = require('path');

// Spawn Python process
const pythonProcess = spawn('python', [path.join(__dirname, 'main.py'), 'arg1', 'arg2']);

// Capture Python output
pythonProcess.stdout.on('data', (data) => {
  console.log(`Output: ${data}`);
});

// Handle errors
pythonProcess.stderr.on('data', (data) => {
  console.error(`Error: ${data}`);
});

// Handle process exit
pythonProcess.on('close', (code) => {
  console.log(`Python process exited with code ${code}`);
});
