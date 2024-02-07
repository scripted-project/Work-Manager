async function apiGET(url) {
    try {
        const response = await fetch(url);
        const data = await response.json()
        data["code"] = response.status;
        return data
    } catch (error) {
        return null;
    }
}
async function apiPOST(url, data) {
    try {
        const response = await fetch(url, {
            method: 'POST',
            headers: {'Cntent-Type': 'application/json'},
            body: JSON.stringify(data)
        });
        return await response.json();
    } catch (error) {
        return null;
    }
}

async function apiPATCH(url, updatedFields) {
    try {
        const response = await fetch(url, {
            method: 'PATCH',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify(updatedFields)
        });
        return await response.json();
    } catch (error) {
        return null;
    }
}
module.exports = {
    apiGET, apiPATCH, apiPOST
}