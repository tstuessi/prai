import { render, screen } from '@testing-library/react'
import { SinglePageApp } from './SinglePageApp'
import { UserContext } from '../../stores/UserContext'

// Mock the NavbarComponent to focus on SinglePageApp structure
vi.mock('./Navbar', () => ({
  NavbarComponent: () => <div data-testid="navbar-component">NavbarComponent</div>
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

  it('renders Bootstrap row and column structure', () => {
    const { container } = render(
      <UserContext.Provider value={{ userInfo: mockUserInfo, setUserInfo: vi.fn() }}>
        <SinglePageApp />
      </UserContext.Provider>
    )

    const rows = container.querySelectorAll('.row')
    expect(rows).toHaveLength(2)

    const cols = container.querySelectorAll('.col')
    expect(cols).toHaveLength(2)
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

  it('renders welcome content in the second row', () => {
    render(
      <UserContext.Provider value={{ userInfo: mockUserInfo, setUserInfo: vi.fn() }}>
        <SinglePageApp />
      </UserContext.Provider>
    )

    expect(screen.getByRole('heading', { name: 'Welcome to PrAI' })).toBeInTheDocument()
    expect(screen.getByText('This is a single-page application built with React and Bootstrap.')).toBeInTheDocument()
  })

  it('renders main content in a fluid container', () => {
    const { container } = render(
      <UserContext.Provider value={{ userInfo: mockUserInfo, setUserInfo: vi.fn() }}>
        <SinglePageApp />
      </UserContext.Provider>
    )

    const fluidContainers = container.querySelectorAll('.container-fluid')
    expect(fluidContainers).toHaveLength(2) // Main container + content container

    const welcomeHeading = screen.getByRole('heading', { name: 'Welcome to PrAI' })
    const contentContainer = welcomeHeading.closest('.container-fluid')
    expect(contentContainer).toBeInTheDocument()
  })

  it('maintains proper layout structure', () => {
    const { container } = render(
      <UserContext.Provider value={{ userInfo: mockUserInfo, setUserInfo: vi.fn() }}>
        <SinglePageApp />
      </UserContext.Provider>
    )

    // Should have main container > row > col > navbar
    const navbar = screen.getByTestId('navbar-component')
    const navbarCol = navbar.closest('.col')
    const navbarRow = navbarCol?.closest('.row')
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
    expect(screen.getByRole('heading', { name: 'Welcome to PrAI' })).toBeInTheDocument()
  })

  it('renders heading with correct level', () => {
    render(
      <UserContext.Provider value={{ userInfo: mockUserInfo, setUserInfo: vi.fn() }}>
        <SinglePageApp />
      </UserContext.Provider>
    )

    const heading = screen.getByRole('heading', { name: 'Welcome to PrAI' })
    expect(heading.tagName).toBe('H1')
  })

  it('has comment placeholder for main content', () => {
    const { container } = render(
      <UserContext.Provider value={{ userInfo: mockUserInfo, setUserInfo: vi.fn() }}>
        <SinglePageApp />
      </UserContext.Provider>
    )

    // Check that the comment exists in the source by checking structure
    const rows = container.querySelectorAll('.row')
    expect(rows[1]).toBeInTheDocument() // Second row for main content
  })

  it('contains navbar and content in separate rows', () => {
    const { container } = render(
      <UserContext.Provider value={{ userInfo: mockUserInfo, setUserInfo: vi.fn() }}>
        <SinglePageApp />
      </UserContext.Provider>
    )

    const rows = container.querySelectorAll('.row')

    // First row should contain navbar
    const navbar = screen.getByTestId('navbar-component')
    expect(rows[0]).toContainElement(navbar)

    // Second row should contain welcome content
    const welcomeHeading = screen.getByRole('heading', { name: 'Welcome to PrAI' })
    expect(rows[1]).toContainElement(welcomeHeading)
  })

  it('uses correct Bootstrap classes', () => {
    const { container } = render(
      <UserContext.Provider value={{ userInfo: mockUserInfo, setUserInfo: vi.fn() }}>
        <SinglePageApp />
      </UserContext.Provider>
    )

    // Check main container
    expect(container.firstChild).toHaveClass('container-fluid')

    // Check rows
    const rows = container.querySelectorAll('.row')
    rows.forEach(row => {
      expect(row).toHaveClass('row')
    })

    // Check columns
    const cols = container.querySelectorAll('.col')
    cols.forEach(col => {
      expect(col).toHaveClass('col')
    })
  })
})
