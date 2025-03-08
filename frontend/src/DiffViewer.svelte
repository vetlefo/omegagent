<script>
    import { onMount } from 'svelte';

    let actions = [];
    let ws;

    onMount(() => {
        // Connect to WebSocket
        ws = new WebSocket('ws://localhost:8000/ws/discourse');
        
        ws.onmessage = (event) => {
            const data = JSON.parse(event.data);
            actions = [...actions, data.action];
        };
        
        ws.onerror = (error) => {
            console.error('WebSocket error:', error);
        };
        
        ws.onclose = () => {
            console.log('WebSocket connection closed');
        };
        
        return () => {
            ws.close();
        };
    });
</script>

<main>
    <h1>Discourse Manager Actions</h1>
    <ul>
        {#each actions as action}
            <li>{action}</li>
        {/each}
    </ul>
</main>

<style>
    main {
        padding: 1rem;
    }
    ul {
        list-style-type: none;
        padding: 0;
    }
    li {
        margin: 0.5rem 0;
        padding: 0.5rem;
        background-color: #f5f5f5;
        border-radius: 4px;
    }
</style>