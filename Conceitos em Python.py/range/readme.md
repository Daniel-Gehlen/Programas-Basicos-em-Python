``` mermaid
graph TD
  start[Start]
  range1[range 10]
  range2[range 1, 11]
  range3[range 0, 30, 5]
  range4[range 0, -10, -1]
  range5[range 0]
  en[End]

  start --> range1
  range1 --> range2
  range2 --> range3
  range3 --> range4
  range4 --> range5
  range5
```