import { useContext } from "react";
import { Navbar } from "react-bootstrap";
import { UserContext } from "../../../stores/UserContext";


export function UserPicture() {
  const { userInfo } = useContext(UserContext);
  return (
    <Navbar.Brand>
      {userInfo ? <img src={userInfo.avatar_url} alt={userInfo.name || undefined} height={"30"} /> : null}
    </Navbar.Brand>
  )
}
