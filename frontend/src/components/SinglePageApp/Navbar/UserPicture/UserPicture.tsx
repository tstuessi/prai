import { useContext } from "react";
import { Navbar } from "react-bootstrap";
import { UserContext } from "../../../../stores/UserContext";


export function UserPicture() {
  const { userInfo } = useContext(UserContext);
  return (
    <>
      {userInfo && userInfo.avatar_url ? (
        <Navbar.Brand>
          <img src={userInfo.avatar_url} alt={userInfo.name || undefined} height={"30"} />
        </Navbar.Brand>
      ) : null}
    </>
  )
}
