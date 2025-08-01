import { Container, Row } from "react-bootstrap";
import { NavbarComponent } from "./Navbar";
import { Workspace } from "./Workspace";

export function SinglePageApp() {
  return (
    <Container fluid className="d-flex flex-column" style={{ padding: 0, height: "100vh" }}>
      <Row>
        <NavbarComponent />
      </Row>
      <Workspace />
    </Container>
  )
}
