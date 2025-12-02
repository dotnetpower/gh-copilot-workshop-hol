---
sidebar_position: 14
title: 코드 리팩토링 심화
description: GitHub Copilot을 활용한 대규모 레거시 코드베이스 현대화 및 고급 리팩토링 기법
---

# 코드 리팩토링 심화

## 개요

GitHub Copilot을 활용하여 대규모 레거시 코드베이스를 현대적이고 유지보수 가능한 코드로 변환하는 고급 리팩토링 기법을 학습합니다.

## 대규모 리팩토링 전략

### 1. 점진적 리팩토링

**Strangler Fig 패턴**
```typescript
// Legacy Code
class LegacyOrderService {
  processOrder(orderId: string) {
    // 1000줄의 스파게티 코드
    const order = this.db.query(`SELECT * FROM orders WHERE id = ${orderId}`);
    // ... 복잡한 로직
  }
}

// Step 1: 새로운 서비스 인터페이스 생성
// Copilot Chat: "이 레거시 서비스를 위한 현대적인 인터페이스 설계해줘"

interface OrderService {
  getOrder(orderId: string): Promise<Order>;
  processOrder(order: Order): Promise<ProcessedOrder>;
  validateOrder(order: Order): ValidationResult;
  calculateTotal(order: Order): number;
}

// Step 2: 어댑터 패턴으로 점진적 이전
class OrderServiceAdapter implements OrderService {
  constructor(
    private legacyService: LegacyOrderService,
    private modernService: ModernOrderService
  ) {}
  
  async getOrder(orderId: string): Promise<Order> {
    // Feature flag로 점진적 전환
    if (this.isModernEnabled(orderId)) {
      return this.modernService.getOrder(orderId);
    }
    return this.legacyService.getOrder(orderId);
  }
  
  private isModernEnabled(orderId: string): boolean {
    // 10% 트래픽만 새 서비스로
    return this.hashOrderId(orderId) % 10 === 0;
  }
}
```

### 2. 레거시 코드 이해하기

**Copilot을 활용한 코드 분석**

```python
# Legacy Python Code (이해하기 어려운 코드)
def calc(d, p, t):
    if t == 'A':
        r = d * (1 + p * 0.01)
    elif t == 'B':
        r = d * (1 + p * 0.01) * 0.95
    elif t == 'C':
        r = d * (1 + p * 0.01) * 0.9
    else:
        r = d
    return r if r > 0 else 0

# Copilot Chat에 질문:
# "@workspace 이 함수가 무엇을 하는지 설명해줘. 
#  그리고 더 명확한 이름과 구조로 리팩토링해줘"

# Copilot의 개선된 버전
from enum import Enum
from typing import Union

class CustomerTier(Enum):
    """고객 등급"""
    PREMIUM = 'A'  # 할인 없음
    STANDARD = 'B'  # 5% 할인
    BASIC = 'C'     # 10% 할인
    NONE = 'D'      # 포인트 미적용

def calculate_final_price(
    base_price: float,
    points_percentage: float,
    customer_tier: Union[CustomerTier, str]
) -> float:
    """
    고객 등급과 포인트를 고려한 최종 가격을 계산합니다.
    
    Args:
        base_price: 기본 가격
        points_percentage: 적용할 포인트 비율 (예: 5 = 5%)
        customer_tier: 고객 등급 (A: 프리미엄, B: 스탠다드, C: 베이직)
    
    Returns:
        최종 가격 (0 이상)
    
    Examples:
        >>> calculate_final_price(100, 10, CustomerTier.PREMIUM)
        110.0
        >>> calculate_final_price(100, 10, CustomerTier.STANDARD)
        104.5
    """
    # 포인트 적용 가격
    price_with_points = base_price * (1 + points_percentage * 0.01)
    
    # 등급별 할인율
    tier_discounts = {
        'A': 0.0,   # 할인 없음
        'B': 0.05,  # 5% 할인
        'C': 0.10,  # 10% 할인
    }
    
    tier_value = customer_tier.value if isinstance(customer_tier, CustomerTier) else customer_tier
    discount = tier_discounts.get(tier_value, 0.0)
    
    # 할인 적용
    final_price = price_with_points * (1 - discount)
    
    # 음수 방지
    return max(final_price, 0.0)
```

### 3. 자동화된 리팩토링

**Extract Method**

```javascript
// Before: 긴 함수
function processUserRegistration(userData) {
  // 입력 검증 (20줄)
  if (!userData.email || !userData.email.includes('@')) {
    throw new Error('Invalid email');
  }
  if (!userData.password || userData.password.length < 8) {
    throw new Error('Password too short');
  }
  // ... 더 많은 검증
  
  // 비밀번호 해싱 (10줄)
  const salt = crypto.randomBytes(16);
  const hash = crypto.pbkdf2Sync(userData.password, salt, 1000, 64, 'sha512');
  
  // DB 저장 (15줄)
  const user = {
    email: userData.email.toLowerCase(),
    passwordHash: hash.toString('hex'),
    passwordSalt: salt.toString('hex'),
    createdAt: new Date()
  };
  db.users.insert(user);
  
  // 환영 이메일 발송 (20줄)
  // ...
  
  return user;
}

// Copilot Chat: "이 함수를 Extract Method 패턴으로 리팩토링해줘"

// After: 작은 함수들로 분리
interface UserRegistrationData {
  email: string;
  password: string;
  name?: string;
}

interface User {
  id: string;
  email: string;
  passwordHash: string;
  passwordSalt: string;
  createdAt: Date;
}

function processUserRegistration(userData: UserRegistrationData): User {
  validateUserData(userData);
  
  const hashedPassword = hashPassword(userData.password);
  const user = createUserRecord(userData, hashedPassword);
  const savedUser = saveUserToDatabase(user);
  
  sendWelcomeEmail(savedUser.email).catch(err => 
    console.error('Failed to send welcome email:', err)
  );
  
  return savedUser;
}

function validateUserData(userData: UserRegistrationData): void {
  if (!isValidEmail(userData.email)) {
    throw new Error('Invalid email address');
  }
  
  if (!isValidPassword(userData.password)) {
    throw new Error('Password must be at least 8 characters');
  }
}

function hashPassword(password: string): { hash: string; salt: string } {
  const salt = crypto.randomBytes(16);
  const hash = crypto.pbkdf2Sync(password, salt, 100000, 64, 'sha512');
  
  return {
    hash: hash.toString('hex'),
    salt: salt.toString('hex')
  };
}

// ... 나머지 함수들
```

## 패턴 기반 리팩토링

### 1. 싱글톤 → 의존성 주입

```csharp
// Before: 싱글톤 패턴 (테스트 어려움)
public class DatabaseConnection
{
    private static DatabaseConnection _instance;
    private SqlConnection _connection;
    
    private DatabaseConnection()
    {
        _connection = new SqlConnection(
            "Server=prod;Database=main;..."
        );
    }
    
    public static DatabaseConnection Instance
    {
        get
        {
            if (_instance == null)
                _instance = new DatabaseConnection();
            return _instance;
        }
    }
    
    public void ExecuteQuery(string sql) { /* ... */ }
}

// 사용 예
public class OrderService
{
    public void ProcessOrder(int orderId)
    {
        DatabaseConnection.Instance.ExecuteQuery($"UPDATE orders SET status = 'processed' WHERE id = {orderId}");
    }
}

// Copilot Chat: "이 싱글톤을 의존성 주입 패턴으로 리팩토링하고,
//                테스트 가능하게 만들어줘"

// After: 의존성 주입 (테스트 용이, 유연함)
public interface IDatabaseConnection
{
    Task<int> ExecuteNonQueryAsync(string sql, object parameters = null);
    Task<T> ExecuteScalarAsync<T>(string sql, object parameters = null);
    Task<IEnumerable<T>> QueryAsync<T>(string sql, object parameters = null);
}

public class SqlDatabaseConnection : IDatabaseConnection
{
    private readonly string _connectionString;
    
    public SqlDatabaseConnection(IConfiguration configuration)
    {
        _connectionString = configuration.GetConnectionString("DefaultConnection");
    }
    
    public async Task<int> ExecuteNonQueryAsync(string sql, object parameters = null)
    {
        using var connection = new SqlConnection(_connectionString);
        return await connection.ExecuteAsync(sql, parameters);
    }
    
    // ... 나머지 메서드 구현
}

public class OrderService
{
    private readonly IDatabaseConnection _db;
    private readonly ILogger<OrderService> _logger;
    
    public OrderService(IDatabaseConnection db, ILogger<OrderService> logger)
    {
        _db = db ?? throw new ArgumentNullException(nameof(db));
        _logger = logger ?? throw new ArgumentNullException(nameof(logger));
    }
    
    public async Task ProcessOrderAsync(int orderId)
    {
        const string sql = "UPDATE orders SET status = @status WHERE id = @id";
        await _db.ExecuteNonQueryAsync(sql, new { status = "processed", id = orderId });
        _logger.LogInformation("Order {OrderId} processed", orderId);
    }
}

// DI 컨테이너 설정
services.AddScoped<IDatabaseConnection, SqlDatabaseConnection>();
services.AddScoped<OrderService>();

// 테스트
public class OrderServiceTests
{
    [Fact]
    public async Task ProcessOrder_UpdatesDatabase()
    {
        // Arrange
        var mockDb = new Mock<IDatabaseConnection>();
        var mockLogger = new Mock<ILogger<OrderService>>();
        var service = new OrderService(mockDb.Object, mockLogger.Object);
        
        // Act
        await service.ProcessOrderAsync(123);
        
        // Assert
        mockDb.Verify(db => db.ExecuteNonQueryAsync(
            It.IsAny<string>(),
            It.Is<object>(p => /* 검증 로직 */)
        ), Times.Once);
    }
}
```

### 2. 콜백 지옥 → async/await

```javascript
// Before: 콜백 지옥
function getUserOrders(userId, callback) {
  db.users.findById(userId, function(err, user) {
    if (err) return callback(err);
    
    db.orders.findByUserId(user.id, function(err, orders) {
      if (err) return callback(err);
      
      const orderDetails = [];
      let processed = 0;
      
      orders.forEach(function(order) {
        db.orderItems.findByOrderId(order.id, function(err, items) {
          if (err) return callback(err);
          
          orderDetails.push({ order, items });
          processed++;
          
          if (processed === orders.length) {
            callback(null, orderDetails);
          }
        });
      });
    });
  });
}

// Copilot Chat: "이 콜백 지옥을 async/await으로 리팩토링해줘"

// After: async/await
async function getUserOrders(userId: string): Promise<OrderDetails[]> {
  try {
    // 사용자 조회
    const user = await db.users.findById(userId);
    if (!user) {
      throw new Error(`User not found: ${userId}`);
    }
    
    // 주문 목록 조회
    const orders = await db.orders.findByUserId(user.id);
    
    // 주문 상세 정보 병렬 조회
    const orderDetails = await Promise.all(
      orders.map(async (order) => {
        const items = await db.orderItems.findByOrderId(order.id);
        return { order, items };
      })
    );
    
    return orderDetails;
    
  } catch (error) {
    console.error('Failed to get user orders:', error);
    throw new Error(`Failed to retrieve orders for user ${userId}`);
  }
}

// 사용 예
async function displayUserOrders(userId: string) {
  try {
    const orders = await getUserOrders(userId);
    console.log(`Found ${orders.length} orders for user ${userId}`);
    return orders;
  } catch (error) {
    console.error('Error displaying orders:', error);
    return [];
  }
}
```

## 레거시 코드 현대화

### C# 레거시 → 현대 C# 변환

```csharp
// Before: 레거시 C# 코드
public class UserService
{
    private UserRepository userRepository;
    
    public UserService(UserRepository userRepository)
    {
        this.userRepository = userRepository;
    }
    
    public User FindUserById(long? id)
    {
        if (id == null)
        {
            throw new ArgumentException("ID cannot be null");
        }
        
        User user = userRepository.FindById(id.Value);
        if (user == null)
        {
            throw new UserNotFoundException("User not found: " + id);
        }
        
        return user;
    }
    
    public List<User> FindActiveUsers()
    {
        List<User> allUsers = userRepository.FindAll();
        List<User> activeUsers = new List<User>();
        
        foreach (User user in allUsers)
        {
            if (user.IsActive)
            {
                activeUsers.Add(user);
            }
        }
        
        return activeUsers;
    }
}

// Copilot Chat: "이 C# 코드를 현대적인 C# 12 스타일로 변환하고 
//                nullable 참조 타입과 LINQ를 활용하도록 개선해줘"

// After: 현대 C# 12 스타일
// 필요한 using: System.Runtime.CompilerServices (EnumeratorCancellation용)
public class UserService(IUserRepository userRepository)
{
    public User FindUserById(long? id)
    {
        ArgumentNullException.ThrowIfNull(id);
        
        return userRepository.FindById(id.Value)
            ?? throw new UserNotFoundException($"User not found: {id}");
    }
    
    public IEnumerable<User> FindActiveUsers() =>
        userRepository.FindAll()
            .Where(user => user.IsActive);
    
    // 추가 개선: 비동기 처리
    public async Task<User> FindUserByIdAsync(long? id, CancellationToken cancellationToken = default)
    {
        ArgumentNullException.ThrowIfNull(id);
        
        return await userRepository.FindByIdAsync(id.Value, cancellationToken)
            ?? throw new UserNotFoundException($"User not found: {id}");
    }
    
    // IAsyncEnumerable을 사용한 스트리밍
    public async IAsyncEnumerable<User> GetActiveUsersAsync(
        [EnumeratorCancellation] CancellationToken cancellationToken = default)
    {
        await foreach (var user in userRepository.GetAllAsync(cancellationToken))
        {
            if (user.IsActive)
            {
                yield return user;
            }
        }
    }
}
```

### Python 2 → Python 3 현대화

```python
# Before: Python 2 스타일
def process_data(data):
    if not data:
        raise Exception("No data")
    
    result = []
    for item in data:
        if item.has_key('value'):
            result.append(item['value'])
    
    return result

# Copilot Chat: "Python 3로 현대화하고 타입 힌트와 
#                최신 기능을 사용하도록 개선해줘"

# After: Python 3 현대화
from typing import List, Dict, Any, Optional
from dataclasses import dataclass

@dataclass
class DataItem:
    """데이터 항목"""
    value: float
    name: str
    metadata: Optional[Dict[str, Any]] = None

def process_data(data: List[DataItem]) -> List[float]:
    """
    데이터 항목 리스트에서 값을 추출합니다.
    
    Args:
        data: 처리할 데이터 항목 리스트
    
    Returns:
        추출된 값들의 리스트
    
    Raises:
        ValueError: 데이터가 비어있는 경우
    
    Examples:
        >>> items = [DataItem(value=1.0, name="a"), DataItem(value=2.0, name="b")]
        >>> process_data(items)
        [1.0, 2.0]
    """
    if not data:
        raise ValueError("데이터가 비어있습니다")
    
    # List comprehension 사용
    return [item.value for item in data]

# 더 나아가: 함수형 프로그래밍 스타일
from functools import reduce
from operator import add

def process_data_functional(data: List[DataItem]) -> float:
    """데이터 항목들의 값을 합산합니다."""
    if not data:
        raise ValueError("데이터가 비어있습니다")
    
    return reduce(add, (item.value for item in data), 0.0)
```

## 성능 리팩토링

### N+1 쿼리 문제 해결

```typescript
// Before: N+1 쿼리 문제
async function getBlogPostsWithComments() {
  const posts = await db.posts.findAll(); // 1번 쿼리
  
  for (const post of posts) {
    // N번 쿼리 (posts 개수만큼)
    post.comments = await db.comments.findByPostId(post.id);
  }
  
  return posts;
}

// Copilot Chat: "N+1 쿼리 문제를 해결하고 성능을 최적화해줘"

// After: JOIN 또는 일괄 로드
async function getBlogPostsWithComments(): Promise<PostWithComments[]> {
  // Option 1: SQL JOIN 사용
  const postsWithComments = await db.query(`
    SELECT 
      p.*,
      json_agg(c.*) as comments
    FROM posts p
    LEFT JOIN comments c ON c.post_id = p.id
    GROUP BY p.id
  `);
  
  return postsWithComments;
}

// Option 2: DataLoader 패턴
import DataLoader from 'dataloader';

const commentLoader = new DataLoader(async (postIds: string[]) => {
  const comments = await db.comments.findByPostIds(postIds);
  
  // postId별로 그룹화
  const commentsByPostId = new Map<string, Comment[]>();
  for (const comment of comments) {
    const existing = commentsByPostId.get(comment.postId) || [];
    existing.push(comment);
    commentsByPostId.set(comment.postId, existing);
  }
  
  // postIds 순서대로 반환
  return postIds.map(id => commentsByPostId.get(id) || []);
});

async function getBlogPostsWithCommentsOptimized() {
  const posts = await db.posts.findAll();
  
  // 일괄 로드 (1번의 추가 쿼리)
  const commentsArrays = await Promise.all(
    posts.map(post => commentLoader.load(post.id))
  );
  
  return posts.map((post, index) => ({
    ...post,
    comments: commentsArrays[index]
  }));
}
```

## 리팩토링 체크리스트

### Before 리팩토링
- [ ] 현재 코드의 동작을 완전히 이해
- [ ] 포괄적인 테스트 작성 (리팩토링 안전망)
- [ ] 리팩토링 목표 명확히 정의
- [ ] 작은 단위로 나눌 수 있는지 확인
- [ ] 버전 관리 시스템에 커밋

### During 리팩토링
- [ ] 한 번에 하나의 리팩토링만 수행
- [ ] 각 단계마다 테스트 실행
- [ ] 기능 변경과 리팩토링 분리
- [ ] 자주 커밋
- [ ] Copilot 제안을 검증

### After 리팩토링
- [ ] 모든 테스트 통과 확인
- [ ] 성능 영향 측정
- [ ] 코드 리뷰 요청
- [ ] 문서 업데이트
- [ ] 팀원에게 변경 사항 공유

## 다음 단계

다음 섹션에서는 CI/CD 자동화에 GitHub Copilot을 활용하는 방법을 학습합니다.

---

**참고 자료**
- [Refactoring by Martin Fowler](https://refactoring.com/)
- [Working Effectively with Legacy Code](https://www.amazon.com/Working-Effectively-Legacy-Michael-Feathers/dp/0131177052)
