import { render, screen } from '@testing-library/react'
import { SinglePageApp } from './SinglePageApp'
import { UserContext } from '../../stores/UserContext'

// Mock the NavbarComponent to focus on SinglePageApp structure
vi.mock('./Navbar', () => ({
  NavbarComponent: () => <div data-testid="navbar-component">NavbarComponent</div>
}))

// Mock the Workspace component
vi.mock('./Workspace', () => ({
  Workspace: () => <div data-testid="workspace-component">Workspace</div>
}))

const mockUserInfo = {
  id: 1,
  login: 'testuser',
  name: 'Test User',
  email: 'test@example.com',
  avatar_url: 'https://example.com/avatar.jpg'
}

describe('SinglePageApp', () => {
  it('renders a fluid container with zero padding', () => {
    const { container } = render(
      <UserContext.Provider value={{ userInfo: mockUserInfo, setUserInfo: vi.fn() }}>
        <SinglePageApp />
      </UserContext.Provider>
    )

    const fluidContainer = container.querySelector('.container-fluid')
    expect(fluidContainer).toBeInTheDocument()
    expect(fluidContainer).toHaveStyle({ padding: '0' })
  })

  it('renders Bootstrap row structure', () => {
    const { container } = render(
      <UserContext.Provider value={{ userInfo: mockUserInfo, setUserInfo: vi.fn() }}>
        <SinglePageApp />
      </UserContext.Provider>
    )

    const rows = container.querySelectorAll('.row')
    expect(rows).toHaveLength(1) // Only navbar row in SinglePageApp
  })

  it('renders the NavbarComponent in the first row', () => {
    render(
      <UserContext.Provider value={{ userInfo: mockUserInfo, setUserInfo: vi.fn() }}>
        <SinglePageApp />
      </UserContext.Provider>
    )

    const navbar = screen.getByTestId('navbar-component')
    expect(navbar).toBeInTheDocument()

    // Navbar should be in the first row
    const firstRow = document.querySelector('.row')
    expect(firstRow).toContainElement(navbar)
  })

  it('renders Workspace component', () => {
    render(
      <UserContext.Provider value={{ userInfo: mockUserInfo, setUserInfo: vi.fn() }}>
        <SinglePageApp />
      </UserContext.Provider>
    )

    expect(screen.getByTestId('workspace-component')).toBeInTheDocument()
  })

  it('renders main content in a fluid container', () => {
    const { container } = render(
      <UserContext.Provider value={{ userInfo: mockUserInfo, setUserInfo: vi.fn() }}>
        <SinglePageApp />
      </UserContext.Provider>
    )

    const fluidContainers = container.querySelectorAll('.container-fluid')
    expect(fluidContainers).toHaveLength(1) // Only main container

    const workspace = screen.getByTestId('workspace-component')
    expect(workspace).toBeInTheDocument()
  })

  it('maintains proper layout structure', () => {
    const { container } = render(
      <UserContext.Provider value={{ userInfo: mockUserInfo, setUserInfo: vi.fn() }}>
        <SinglePageApp />
      </UserContext.Provider>
    )

    // Should have main container > row > navbar
    const navbar = screen.getByTestId('navbar-component')
    const navbarRow = navbar.closest('.row')
    const mainContainer = navbarRow?.closest('.container-fluid')

    expect(mainContainer).toBe(container.firstChild)
  })

  it('works with null userInfo context', () => {
    render(
      <UserContext.Provider value={{ userInfo: null, setUserInfo: vi.fn() }}>
        <SinglePageApp />
      </UserContext.Provider>
    )

    expect(screen.getByTestId('navbar-component')).toBeInTheDocument()
    expect(screen.getByTestId('workspace-component')).toBeInTheDocument()
  })

  it('renders navbar in the first row', () => {
    const { container } = render(
      <UserContext.Provider value={{ userInfo: mockUserInfo, setUserInfo: vi.fn() }}>
        <SinglePageApp />
      </UserContext.Provider>
    )

    const navbar = screen.getByTestId('navbar-component')
    const firstRow = container.querySelector('.row')
    expect(firstRow).toContainElement(navbar)
  })

  it('renders workspace outside of rows', () => {
    const { container } = render(
      <UserContext.Provider value={{ userInfo: mockUserInfo, setUserInfo: vi.fn() }}>
        <SinglePageApp />
      </UserContext.Provider>
    )

    const workspace = screen.getByTestId('workspace-component')
    const mainContainer = container.querySelector('.container-fluid')
    expect(mainContainer).toContainElement(workspace)
  })

  it('contains navbar in row and workspace as sibling', () => {
    const { container } = render(
      <UserContext.Provider value={{ userInfo: mockUserInfo, setUserInfo: vi.fn() }}>
        <SinglePageApp />
      </UserContext.Provider>
    )

    const rows = container.querySelectorAll('.row')
    expect(rows).toHaveLength(1)

    // First row should contain navbar
    const navbar = screen.getByTestId('navbar-component')
    expect(rows[0]).toContainElement(navbar)

    // Workspace should be a direct child of main container
    const workspace = screen.getByTestId('workspace-component')
    const mainContainer = container.querySelector('.container-fluid')
    expect(mainContainer).toContainElement(workspace)
  })

  it('uses correct Bootstrap classes', () => {
    const { container } = render(
      <UserContext.Provider value={{ userInfo: mockUserInfo, setUserInfo: vi.fn() }}>
        <SinglePageApp />
      </UserContext.Provider>
    )

    // Check main container
    expect(container.firstChild).toHaveClass('container-fluid')
    expect(container.firstChild).toHaveClass('d-flex')
    expect(container.firstChild).toHaveClass('flex-column')

    // Check row
    const row = container.querySelector('.row')
    expect(row).toHaveClass('row')
  })
})
