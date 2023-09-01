``` mermaid
graph TD
  subgraph linear_interpolation_function
    linear_interpolation[linear_interpolation]
    check_input[Verifica entrada]
    find_indices[Encontra índices]
    perform_interpolation[Realiza interpolação]
  end

  subgraph Exemplo
    x_known[[0, 1, 2, 3, 4, 5]]
    y_known[[0, 2, 4, 6, 8, 10]]
    x_interp[2.5]
    y_interp[linear_interpolation]
    print_result["Print resultado"]
  end

  linear_interpolation --> check_input
  linear_interpolation --> find_indices
  linear_interpolation --> perform_interpolation
  check_input --> x_known
  check_input --> y_known
  check_input --> x_interp
  find_indices --> idx_left
  find_indices --> idx_right
  perform_interpolation --> x_left
  perform_interpolation --> x_right
  perform_interpolation --> y_left
  perform_interpolation --> y_right
  perform_interpolation --> slope
  perform_interpolation --> y_interp

  x_known --> linear_interpolation
  y_known --> linear_interpolation
  x_interp --> linear_interpolation
  linear_interpolation --> y_interp
  y_interp --> print_result
```