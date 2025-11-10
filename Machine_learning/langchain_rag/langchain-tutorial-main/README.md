# RAG 마스터: 랭체인으로 완성하는 LLM 서비스
`RAG 마스터: 랭체인으로 완성하는 LLM 서비스`의 깃허브 저장소입니다.

<img src="https://github.com/user-attachments/assets/3ef39770-4c57-4be0-b4d8-034f3907921e" alt="표지" width="300">

## 업데이트 내역
### 2025-05-18
Graphrag 라이브러리의 최근 업데이트로 인해 이 저장소의 일부 파일이 수정되었습니다. 주요 변경 사항은 다음과 같습니다:

- **ch05_GRAPHRAG_DB구축.ipynb**:
  - Graphrag 인덱싱 명령어가 업데이트되었습니다.
  - 이전: `!graphrag index --root ./working_directory`
  - 현재: `!graphrag index --root ./working_directory --method standard --logger print`

- **ch05_GRAPHRAG_NEO4J_RETRIEVER.ipynb**:
  - REDUCE_SYSTEM_PROMPT의 데이터 참조 형식이 변경되었습니다.
  - 이전: "예시 문장 [Data: Reports (2, 7, 34, 46, 64, +more)]"
  - 현재: "예시 문장 [Data: Entities (35, 39), Relationships (27, 29)]"

- **ch05_GRAPHRAG_NEO4J저장.ipynb**:
  - 여러 Parquet 파일 이름이 변경되었습니다:
    - `create_final_documents.parquet` → `documents.parquet`
    - `create_final_text_units.parquet` → `text_units.parquet`
    - `create_final_entities.parquet` → `entities.parquet`
    - `create_final_relationships.parquet` → `relationships.parquet`
    - `create_final_communities.parquet` → `communities.parquet`
    - `create_final_community_reports.parquet` → `community_reports.parquet`
  - 커뮤니티 보고서 임포트에서 `rank_explanation`이 `rating_explanation`으로 이름이 변경되었습니다.
  - 노드 임포트 섹션이 삭제되었습니다.