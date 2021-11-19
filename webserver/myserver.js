const express = require('express');
const {exec} = require('child_process');
const { promisify } = require('util');
const cors = require('cors')

const execute = promisify(exec);

// App
const app = express();
app.use(cors({origin: '*'}));
app.get('/', async (req, res) => {
    let cmd = await execute('kubectl exec -ti dpc-64856974b6-pfrwv -- bash -c "./start.sh"');
    let stderr = cmd.stderr
    let text = stderr.split('process')[1]
    return res.status(200).json({msg: text});
});

app.listen(8080, 'localhost');
console.log(`Running server...`);
