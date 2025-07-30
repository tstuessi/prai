import createClient from "openapi-fetch";
import type { paths } from "../types/api";

const client = createClient<paths>({
  baseUrl: "http://localhost:8000",
});

async function getUserInfo() {
  const { data, error } = await client.GET("/api/github/user");
  if (error) {
    throw error;
  }
  return data;
}

export { getUserInfo };
