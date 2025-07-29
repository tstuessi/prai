import { Col, Container, Row } from "react-bootstrap";
import { NavbarComponent } from "./Navbar";

export function SinglePageApp() {
  return (
    <Container fluid style={{ padding: 0 }}>
      <Row>
        <Col>
          <NavbarComponent />
        </Col>
      </Row>
      <Row>
        {/* Main content will go here */}
        <Col>
          <Container fluid>
            <h1> Welcome to PrAI</h1>
            <p>This is a single-page application built with React and Bootstrap.</p>
          </Container>
        </Col>
      </Row>
    </Container>
  )
}
