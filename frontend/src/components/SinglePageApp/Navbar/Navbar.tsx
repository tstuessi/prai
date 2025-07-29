import Navbar from 'react-bootstrap/Navbar';
import { UserPicture } from './UserPicture';
import { UserInfoName } from './UserInfoName';
import { Container } from 'react-bootstrap';

export function NavbarComponent() {
  return (
    <Navbar className="bg-body-tertiary" style={{ paddingLeft: '1rem', paddingRight: '1rem' }}>
      <Container fluid>
        <Navbar.Brand href="#home">PrAI</Navbar.Brand>
        <Navbar.Toggle />
        <Navbar.Collapse className="justify-content-end">
          <UserPicture />
          <UserInfoName />
        </Navbar.Collapse>
      </Container>
    </Navbar >
  );
}
