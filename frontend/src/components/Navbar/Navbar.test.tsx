import { render, screen } from '@testing-library/react'
import { NavbarComponent } from './Navbar'
import { UserContext } from '../../stores/UserContext'

// Mock the child components to focus on Navbar structure
vi.mock('./UserPicture', () => ({
  UserPicture: () => <div data-testid="user-picture">UserPicture</div>
}))

vi.mock('./UserInfoName', () => ({
  UserInfoName: () => <div data-testid="user-info-name">UserInfoName</div>
}))

const mockUserInfo = {
  id: 1,
  login: 'testuser',
  name: 'Test User',
  email: 'test@example.com',
  avatar_url: 'https://example.com/avatar.jpg'
}

describe('NavbarComponent', () => {
  it('renders the navbar with correct structure', () => {
    render(
      <UserContext.Provider value={{ userInfo: mockUserInfo, setUserInfo: vi.fn() }}>
        <NavbarComponent />
      </UserContext.Provider>
    )

    // Check navbar exists
    const navbar = document.querySelector('.navbar')
    expect(navbar).toBeInTheDocument()
    expect(navbar).toHaveClass('bg-body-tertiary')
  })

  it('applies correct padding styles', () => {
    render(
      <UserContext.Provider value={{ userInfo: mockUserInfo, setUserInfo: vi.fn() }}>
        <NavbarComponent />
      </UserContext.Provider>
    )

    const navbar = document.querySelector('.navbar')
    expect(navbar).toHaveStyle({
      paddingLeft: '1rem',
      paddingRight: '1rem'
    })
  })

  it('renders the PrAI brand link', () => {
    render(
      <UserContext.Provider value={{ userInfo: mockUserInfo, setUserInfo: vi.fn() }}>
        <NavbarComponent />
      </UserContext.Provider>
    )

    const brandLink = screen.getByRole('link', { name: 'PrAI' })
    expect(brandLink).toBeInTheDocument()
    expect(brandLink).toHaveAttribute('href', '#home')
    expect(brandLink).toHaveClass('navbar-brand')
  })

  it('contains a fluid container', () => {
    render(
      <UserContext.Provider value={{ userInfo: mockUserInfo, setUserInfo: vi.fn() }}>
        <NavbarComponent />
      </UserContext.Provider>
    )

    const container = document.querySelector('.container-fluid')
    expect(container).toBeInTheDocument()
  })

  it('renders navbar toggle button', () => {
    render(
      <UserContext.Provider value={{ userInfo: mockUserInfo, setUserInfo: vi.fn() }}>
        <NavbarComponent />
      </UserContext.Provider>
    )

    const toggle = document.querySelector('.navbar-toggler')
    expect(toggle).toBeInTheDocument()
  })

  it('renders navbar collapse with correct classes', () => {
    render(
      <UserContext.Provider value={{ userInfo: mockUserInfo, setUserInfo: vi.fn() }}>
        <NavbarComponent />
      </UserContext.Provider>
    )

    const collapse = document.querySelector('.navbar-collapse')
    expect(collapse).toBeInTheDocument()
    expect(collapse).toHaveClass('justify-content-end')
  })

  it('renders UserPicture component', () => {
    render(
      <UserContext.Provider value={{ userInfo: mockUserInfo, setUserInfo: vi.fn() }}>
        <NavbarComponent />
      </UserContext.Provider>
    )

    expect(screen.getByTestId('user-picture')).toBeInTheDocument()
  })

  it('renders UserInfoName component', () => {
    render(
      <UserContext.Provider value={{ userInfo: mockUserInfo, setUserInfo: vi.fn() }}>
        <NavbarComponent />
      </UserContext.Provider>
    )

    expect(screen.getByTestId('user-info-name')).toBeInTheDocument()
  })

  it('renders both user components in the collapse section', () => {
    render(
      <UserContext.Provider value={{ userInfo: mockUserInfo, setUserInfo: vi.fn() }}>
        <NavbarComponent />
      </UserContext.Provider>
    )

    const collapse = document.querySelector('.navbar-collapse')
    const userPicture = screen.getByTestId('user-picture')
    const userInfoName = screen.getByTestId('user-info-name')

    expect(collapse).toContainElement(userPicture)
    expect(collapse).toContainElement(userInfoName)
  })

  it('works with null userInfo context', () => {
    render(
      <UserContext.Provider value={{ userInfo: null, setUserInfo: vi.fn() }}>
        <NavbarComponent />
      </UserContext.Provider>
    )

    // Should still render navbar structure
    expect(document.querySelector('.navbar')).toBeInTheDocument()
    expect(screen.getByRole('link', { name: 'PrAI' })).toBeInTheDocument()
    expect(screen.getByTestId('user-picture')).toBeInTheDocument()
    expect(screen.getByTestId('user-info-name')).toBeInTheDocument()
  })

  it('maintains proper component order in collapse section', () => {
    render(
      <UserContext.Provider value={{ userInfo: mockUserInfo, setUserInfo: vi.fn() }}>
        <NavbarComponent />
      </UserContext.Provider>
    )

    const userPicture = screen.getByTestId('user-picture')
    const userInfoName = screen.getByTestId('user-info-name')

    // Check that UserPicture appears before UserInfoName in DOM order
    const allElements = screen.getAllByTestId(/user-/)
    expect(allElements[0]).toBe(userPicture)
    expect(allElements[1]).toBe(userInfoName)
  })
})
