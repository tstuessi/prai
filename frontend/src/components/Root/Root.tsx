import { Container } from "react-bootstrap";
import { SinglePageApp } from "../SinglePageApp";

export function Root() {
    return (
        <Container fluid style={{ padding: 0 }}>
            <SinglePageApp />
        </Container>
    )
}
