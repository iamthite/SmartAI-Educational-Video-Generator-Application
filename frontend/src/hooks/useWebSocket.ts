// ============================================
// frontend/src/hooks/useWebSocket.ts
// ============================================
import { useState, useEffect, useRef } from 'react';

interface WebSocketMessage {
  progress: number;
  status: string;
  message: string;
  timestamp: string;
}

export const useWebSocket = (clientId: string) => {
  const [progress, setProgress] = useState(0);
  const [status, setStatus] = useState('idle');
  const [message, setMessage] = useState('');
  const [isConnected, setIsConnected] = useState(false);
  const ws = useRef<WebSocket | null>(null);

  useEffect(() => {
    if (!clientId) return;

    const wsUrl = `ws://localhost:8000/ws/${clientId}`;
    ws.current = new WebSocket(wsUrl);

    ws.current.onopen = () => {
      console.log('WebSocket connected');
      setIsConnected(true);
    };

    ws.current.onmessage = (event) => {
      try {
        const data: WebSocketMessage = JSON.parse(event.data);
        setProgress(data.progress);
        setStatus(data.status);
        setMessage(data.message);
      } catch (error) {
        console.error('Failed to parse WebSocket message:', error);
      }
    };

    ws.current.onerror = (error) => {
      console.error('WebSocket error:', error);
      setIsConnected(false);
    };

    ws.current.onclose = () => {
      console.log('WebSocket disconnected');
      setIsConnected(false);
    };

    return () => {
      if (ws.current) {
        ws.current.close();
      }
    };
  }, [clientId]);

  return { progress, status, message, isConnected };
};


