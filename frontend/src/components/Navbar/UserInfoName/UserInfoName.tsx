import { useContext } from "react";
import { Navbar } from "react-bootstrap";
import { UserContext } from "../../../App";

export function UserInfoName() {
  const { userInfo } = useContext(UserContext);

  return (
    <Navbar.Text className="text-nowrap">
      {userInfo ? (
        userInfo.name
      ) : (
        <p>Loading...</p>
      )}
    </Navbar.Text>
  )
}
