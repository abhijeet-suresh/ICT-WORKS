def convert_temperature(value, input_scale, output_scale):
    if input_scale == 'C':
        if output_scale == 'F':
            return value * 1.8 + 32
        else:
            return value
    elif input_scale == 'F':
        if output_scale == 'C':
            return (value - 32) / 1.8
        else:
            return value
    else:
        return value
    
while True:
    
    print('Enter the input temperature value:')
    value = float(input())

    print('Enter the input temperature scale (C, F):')
    input_scale = input().upper()

    print('Enter the output temperature scale (C, F):')
    output_scale = input().upper()

    
    result = convert_temperature(value, input_scale, output_scale)
    print(f'{value} {input_scale} = {result} {output_scale}')
    
    break
  