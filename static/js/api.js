async function apiget(url) {
    try {
        const response = await fetch(url);
        return await response.json();
    } catch (error) {
        return null;
    }
}
async function apipost(url, data) {
    try {
        const response = await fetch(url, {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify(data)
        });
        return await response.json();
    } catch (error) {
        return null;
    }
}

async function apipatch(url, updatedFields) {
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