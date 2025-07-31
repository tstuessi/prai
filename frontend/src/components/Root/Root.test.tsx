import { render, screen } from '@testing-library/react'
import { Root } from './Root'
import { UserContext } from '../../stores/UserContext'

// Mock the SinglePageApp component to focus on Root structure
vi.mock('../SinglePageApp', () => ({
  SinglePageApp: () => <div data-testid="single-page-app">SinglePageApp</div>
}))

const mockUserInfo = {
  id: 1,
  login: 'testuser',
  name: 'Test User',
  email: 'test@example.com',
  avatar_url: 'https://example.com/avatar.jpg'
}

describe('Root', () => {
  it('renders a fluid container with zero padding', () => {
    const { container } = render(
      <UserContext.Provider value={{ userInfo: mockUserInfo, setUserInfo: vi.fn() }}>
        <Root />
      </UserContext.Provider>
    )

    const fluidContainer = container.querySelector('.container-fluid')
    expect(fluidContainer).toBeInTheDocument()
    expect(fluidContainer).toHaveStyle({ padding: '0' })
  })

  it('renders the SinglePageApp component', () => {
    render(
      <UserContext.Provider value={{ userInfo: mockUserInfo, setUserInfo: vi.fn() }}>
        <Root />
      </UserContext.Provider>
    )

    expect(screen.getByTestId('single-page-app')).toBeInTheDocument()
  })

  it('works with null userInfo context', () => {
    render(
      <UserContext.Provider value={{ userInfo: null, setUserInfo: vi.fn() }}>
        <Root />
      </UserContext.Provider>
    )

    expect(screen.getByTestId('single-page-app')).toBeInTheDocument()
    const fluidContainer = document.querySelector('.container-fluid')
    expect(fluidContainer).toBeInTheDocument()
  })

  it('contains SinglePageApp within the fluid container', () => {
    render(
      <UserContext.Provider value={{ userInfo: mockUserInfo, setUserInfo: vi.fn() }}>
        <Root />
      </UserContext.Provider>
    )

    const fluidContainer = document.querySelector('.container-fluid')
    const singlePageApp = screen.getByTestId('single-page-app')

    expect(fluidContainer).toContainElement(singlePageApp)
  })

  it('renders with minimal DOM structure', () => {
    const { container } = render(
      <UserContext.Provider value={{ userInfo: mockUserInfo, setUserInfo: vi.fn() }}>
        <Root />
      </UserContext.Provider>
    )

    // Root should only contain a single container with SinglePageApp inside
    const rootElement = container.firstChild
    expect(rootElement).toHaveClass('container-fluid')
    expect(rootElement?.childNodes).toHaveLength(1)
  })

  it('maintains Bootstrap container-fluid class', () => {
    const { container } = render(
      <UserContext.Provider value={{ userInfo: mockUserInfo, setUserInfo: vi.fn() }}>
        <Root />
      </UserContext.Provider>
    )

    const containerElement = container.querySelector('.container-fluid')
    expect(containerElement).toHaveClass('container-fluid')
    expect(containerElement).not.toHaveClass('container')
  })
})
