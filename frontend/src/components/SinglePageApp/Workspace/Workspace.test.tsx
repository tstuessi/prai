import { render, screen } from '@testing-library/react'
import { Workspace } from './Workspace'

describe('Workspace', () => {
  it('renders workspace component', () => {
    render(<Workspace />)

    expect(screen.getByText('This is going to be the list of PRs.')).toBeInTheDocument()
    expect(screen.getByText('This is going to be the details of the selected PR.')).toBeInTheDocument()
    expect(screen.getByText('This is going to be the LLM chat interface.')).toBeInTheDocument()
  })

  it('renders with correct Bootstrap classes', () => {
    const { container } = render(<Workspace />)

    const row = container.querySelector('.row')
    expect(row).toBeInTheDocument()
    expect(row).toHaveClass('flex-grow-1')

    const cols = container.querySelectorAll('.col')
    expect(cols).toHaveLength(3)
  })
})
