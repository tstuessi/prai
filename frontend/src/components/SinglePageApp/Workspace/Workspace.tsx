import { Col, Row } from "react-bootstrap";

export function Workspace() {
    return (
        <Row className="flex-grow-1">
            <Col>
                This is going to be the list of PRs.
            </Col>
            <Col>
                This is going to be the details of the selected PR.
            </Col>
            <Col>
                This is going to be the LLM chat interface.
            </Col>
        </Row>
    );
}
