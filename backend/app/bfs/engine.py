# engine.py – placeholder for BFS traversal engine

"""WebSocket‑based BFS traversal implementation.
The engine receives a start node (or set of nodes) and streams traversal
steps (queue, visited set, current node) to the client.
"""

from fastapi import WebSocket
import asyncio

class BFSTraversal:
    def __init__(self, graph):
        self.graph = graph

    async def traverse(self, start_nodes, websocket: WebSocket):
        visited = set()
        queue = list(start_nodes)
        await websocket.send_json({"type": "init", "queue": queue, "visited": []})
        while queue:
            node = queue.pop(0)
            visited.add(node)
            # In a real implementation, retrieve neighbors from the graph
            neighbors = []  # TODO: fetch actual neighbors
            for n in neighbors:
                if n not in visited and n not in queue:
                    queue.append(n)
            await websocket.send_json({
                "type": "step",
                "current": node,
                "queue": queue,
                "visited": list(visited)
            })
            await asyncio.sleep(0.5)  # simulate animation pacing
        await websocket.send_json({"type": "done", "visited": list(visited)})
