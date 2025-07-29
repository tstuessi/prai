import { render, screen } from '@testing-library/react'
import { UserPicture } from './UserPicture'
import { UserContext } from '../../../../stores/UserContext'

const mockUserInfo = {
  id: 1,
  login: 'testuser',
  name: 'Test User',
  email: 'test@example.com',
  avatar_url: 'https://example.com/avatar.jpg'
}

describe('UserPicture', () => {
  it('renders user avatar when userInfo is provided', () => {
    render(
      <UserContext.Provider value={{ userInfo: mockUserInfo, setUserInfo: vi.fn() }}>
        <UserPicture />
      </UserContext.Provider>
    )

    const img = screen.getByRole('img')
    expect(img).toBeInTheDocument()
    expect(img).toHaveAttribute('src', 'https://example.com/avatar.jpg')
    expect(img).toHaveAttribute('alt', 'Test User')
    expect(img).toHaveAttribute('height', '30')
  })

  it('renders nothing when userInfo is null', () => {
    render(
      <UserContext.Provider value={{ userInfo: null, setUserInfo: vi.fn() }}>
        <UserPicture />
      </UserContext.Provider>
    )

    expect(screen.queryByRole('img')).not.toBeInTheDocument()
  })

  it('applies correct Navbar.Brand wrapper', () => {
    const { container } = render(
      <UserContext.Provider value={{ userInfo: mockUserInfo, setUserInfo: vi.fn() }}>
        <UserPicture />
      </UserContext.Provider>
    )

    const navbarBrand = container.querySelector('.navbar-brand')
    expect(navbarBrand).toBeInTheDocument()
  })

  it('handles user with no name gracefully (undefined alt)', () => {
    const userWithoutName = { ...mockUserInfo, name: null }

    render(
      <UserContext.Provider value={{ userInfo: userWithoutName, setUserInfo: vi.fn() }}>
        <UserPicture />
      </UserContext.Provider>
    )

    const img = screen.getByRole('img')
    expect(img).toBeInTheDocument()
    expect(img).toHaveAttribute('src', 'https://example.com/avatar.jpg')
    expect(img).not.toHaveAttribute('alt')
  })

  it('renders empty alt when name is empty string', () => {
    const userWithEmptyName = { ...mockUserInfo, name: '' }

    render(
      <UserContext.Provider value={{ userInfo: userWithEmptyName, setUserInfo: vi.fn() }}>
        <UserPicture />
      </UserContext.Provider>
    )

    const img = screen.getByRole('img')
    expect(img).toBeInTheDocument()
    expect(img).toHaveAttribute('src', 'https://example.com/avatar.jpg')
    expect(img).not.toHaveAttribute('alt')
  })

  it('handles missing avatar_url', () => {
    const userWithoutAvatar = { ...mockUserInfo, avatar_url: '' }

    render(
      <UserContext.Provider value={{ userInfo: userWithoutAvatar, setUserInfo: vi.fn() }}>
        <UserPicture />
      </UserContext.Provider>
    )

    expect(screen.queryByRole('img')).not.toBeInTheDocument()
  })
})
