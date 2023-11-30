// Currently reads the Replit directory contents from Replit..
// file system and iterates over those files. Need to complete..
// For loop to construct file paths.

import { experimental } from '@replit/extensions';

const {auth, FileSystem} = experimental;

function getAuthToken() {
    return auth.getAuthToken();
}

async function verifyAuthToken(token) {
    return auth.verifyAuthToken(token);
}

async function bridgeToGitHub() {
    const authToken = await getAuthToken();
    const userInfo = await verifyAuthToken(authToken);
    const { payload } = userInfo;

    const files = await FileSystem.readDir('/');

    for (const file of files) {
        const filePath = `/${file.name}`;
    }

    console.log('Bridge to GitHub process completed.');

}

bridgeToGitHub().catch((error) => {
    console.error('An error occurred:', error);
});

// Need to setup HTTP 