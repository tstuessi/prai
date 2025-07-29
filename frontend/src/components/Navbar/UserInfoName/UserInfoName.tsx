import { useContext } from "react";
import { Navbar } from "react-bootstrap";
import { UserContext } from "../../../stores/UserContext";

export function UserInfoName() {
  const { userInfo } = useContext(UserContext);

  return (
    <Navbar.Text className="text-nowrap">
      {userInfo ? (
        userInfo.name
      ) : (
        "Loading..."
      )}
    </Navbar.Text>
  )
}
