import { useEffect, useState } from "react";
import type { UserInfo } from "./types/github/User";
import { Root } from "./components/Root";
import { getUserInfo } from "./hooks/User";
import { UserContext } from "./stores/UserContext";

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
      <Root />
    </UserContext.Provider>

  );
}

export default App;
