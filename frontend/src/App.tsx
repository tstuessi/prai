import { useEffect, useState } from "react";
import type { UserInfo } from "./types/github/User";
import { getUserInfo } from "./hooks/User";
import { UserContext } from "./stores/UserContext";
import { SinglePageApp } from "./components/SinglePageApp";
import { Container } from "react-bootstrap";

function App() {
  const [userInfo, setUserInfo] = useState<UserInfo | null>(null);

  // Initialize the user info
  useEffect(() => {
    async function fetchUserInfo() {
      try {
        const data = await getUserInfo();
        setUserInfo(data);
      } catch (error) {
        console.error("Failed to fetch user info:", error);
      }
    }

    fetchUserInfo();
  }, []);

  return (
    <UserContext.Provider value={{ userInfo, setUserInfo }}>
      <Container fluid style={{ padding: 0 }}>
        <SinglePageApp />
      </Container>
    </UserContext.Provider>

  );
}

export default App;
