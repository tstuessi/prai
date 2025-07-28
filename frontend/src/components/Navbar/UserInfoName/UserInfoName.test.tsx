import { render, screen } from '@testing-library/react'
import { UserInfoName } from './UserInfoName'
import { UserContext } from '../../../stores/UserContext'

const mockUserInfo = {
  id: 1,
  login: 'testuser',
  name: 'Test User',
  email: 'test@example.com',
  avatar_url: 'https://example.com/avatar.jpg'
}

describe('UserInfoName', () => {
  it('renders user name when userInfo is provided', () => {
    render(
      <UserContext.Provider value={{ userInfo: mockUserInfo, setUserInfo: vi.fn() }}>
        <UserInfoName />
      </UserContext.Provider>
    )

    expect(screen.getByText('Test User')).toBeInTheDocument()
  })

  it('renders loading state when userInfo is null', () => {
    render(
      <UserContext.Provider value={{ userInfo: null, setUserInfo: vi.fn() }}>
        <UserInfoName />
      </UserContext.Provider>
    )

    expect(screen.getByText('Loading...')).toBeInTheDocument()
  })

  it('applies correct CSS classes to navbar text', () => {
    render(
      <UserContext.Provider value={{ userInfo: mockUserInfo, setUserInfo: vi.fn() }}>
        <UserInfoName />
      </UserContext.Provider>
    )

    const navbarText = screen.getByText('Test User').closest('.navbar-text')
    expect(navbarText).toHaveClass('navbar-text', 'text-nowrap')
  })

  it('applies correct CSS classes to loading state', () => {
    render(
      <UserContext.Provider value={{ userInfo: null, setUserInfo: vi.fn() }}>
        <UserInfoName />
      </UserContext.Provider>
    )

    const navbarText = screen.getByText('Loading...').closest('.navbar-text')
    expect(navbarText).toHaveClass('navbar-text', 'text-nowrap')
  })

  it('handles user with no name gracefully', () => {
    const userWithoutName = { ...mockUserInfo, name: null }

    render(
      <UserContext.Provider value={{ userInfo: userWithoutName, setUserInfo: vi.fn() }}>
        <UserInfoName />
      </UserContext.Provider>
    )

    expect(screen.queryByText('Test User')).not.toBeInTheDocument()
    const navbarText = document.querySelector('.navbar-text')
    expect(navbarText).toBeInTheDocument()
    expect(navbarText).toHaveTextContent('')
  })

  it('renders empty string name when provided', () => {
    const userWithEmptyName = { ...mockUserInfo, name: '' }

    render(
      <UserContext.Provider value={{ userInfo: userWithEmptyName, setUserInfo: vi.fn() }}>
        <UserInfoName />
      </UserContext.Provider>
    )

    const navbarText = document.querySelector('.navbar-text')
    expect(navbarText).toBeInTheDocument()
    expect(navbarText).toHaveTextContent('')
    expect(navbarText).toHaveClass('navbar-text', 'text-nowrap')
  })
})
