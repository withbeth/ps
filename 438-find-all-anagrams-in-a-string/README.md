
## Try
- 1: SingleSet으로 구현하였으나, 주어지는 단어(p)가 중복가능했으므로 실패.
- 2: 아나그램이 정렬되면 결국 단순한 문자열 비교와 같아지는 특성을 이용하였으나, 타임오버발생하는 인풋 존재;(인풋과 아웃풋 조건이 문제에 주어져있었으면 방지가능한 문제)
- 3: MultiSet과 Words, Window Frequency 메모이제이션이용하여 통과

## FeedBack
- 올바른 방향으로 해결하고 있었으나, 윈도우 캐싱시 어느조건을 캐싱할지에서 헤맸다(문자 자체일지 bool로 체크만 캐쉬할지에 대하여)
- 또한 다중집합 비교도 단순히 문자 카운트만 생각할것이 아니라, 키와 카운트자체가 같은 집합을 비교해야한다는게 나중에 떠올랐다....
- 프리컴퓨팅, 프리캐싱 방법의 중요성(미리 윈도우캐슁을 해놓음에 따라 1중 루프로 해결가능)