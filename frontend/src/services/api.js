export async function healthCheck() {
  return fetch('/api/health').then((res) => res.json());
}
