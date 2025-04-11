✅ 1. **Core Annotations**
-------------------------

| Annotation | Purpose |
| --- | --- |
| `@SpringBootApplication` | Main entry point; combines `@Configuration`, `@EnableAutoConfiguration`, `@ComponentScan` |
| `@Component` | Generic component class (managed by Spring container) |
| `@Autowired` | Automatically injects dependencies |
| `@Value` | Injects values from `application.properties` |

* * * * *

✅ 2. **Stereotype Annotations (Layer Separation)**
--------------------------------------------------

| Annotation | Purpose |
| --- | --- |
| `@Component` | Generic Spring-managed component |
| `@Service` | Marks a service class (business logic layer) |
| `@Repository` | Marks DAO classes (data access layer), enables exception translation |
| `@Controller` | Marks a web controller (used in MVC) |
| `@RestController` | Combines `@Controller` and `@ResponseBody` for REST APIs |

* * * * *

✅ 3. **Spring Web / REST Annotations**
--------------------------------------

| Annotation | Purpose |
| --- | --- |
| `@GetMapping` | Handles HTTP GET requests |
| `@PostMapping` | Handles HTTP POST requests |
| `@PutMapping` | Handles HTTP PUT requests |
| `@DeleteMapping` | Handles HTTP DELETE requests |
| `@RequestMapping` | General-purpose mapping (can be used with any method) |
| `@RequestParam` | Binds query params (e.g., `/users?id=1`) |
| `@PathVariable` | Binds URI path segments (e.g., `/users/1`) |
| `@RequestBody` | Binds JSON body to a Java object |
| `@ResponseBody` | Converts Java object to JSON response |

* * * * *

✅ 4. **Data / JPA Annotations**
-------------------------------

| Annotation | Purpose |
| --- | --- |
| `@Entity` | Marks a class as a JPA entity (table) |
| `@Id` | Marks the primary key field |
| `@GeneratedValue` | Auto-generates ID values |
| `@Column` | Configures a database column |
| `@Table` | Optional: sets table name |
| `@ManyToOne` / `@OneToMany` / `@ManyToMany` / `@OneToOne` | Sets relationships between entities |
| `@JoinColumn` | Configures foreign key column |
| `@JoinTable` | Configures join table for many-to-many |

* * * * *

✅ 5. **Configuration & Lifecycle**
----------------------------------

| Annotation | Purpose |
| --- | --- |
| `@Configuration` | Marks a class as a configuration source |
| `@Bean` | Declares a bean method inside `@Configuration` |
| `@EnableAutoConfiguration` | Enables Spring Boot's auto-config |
| `@ComponentScan` | Scans for Spring components |

* * * * *

✅ 6. **Testing**
----------------

| Annotation | Purpose |
| --- | --- |
| `@SpringBootTest` | Loads full Spring context for integration tests |
| `@MockBean` | Mocks a bean inside Spring context |
| `@WebMvcTest` | Loads only web-related components for testing controllers |
| `@DataJpaTest` | Tests only the repository layer |

* * * * *

✅ 7. **Bonus Lombok Annotations You Might See:**
----------------

| Annotation | Purpose |
| --- | --- |
| `@Data` | Combines `@Getter`, `@Setter`, `@ToString`, `@EqualsAndHashCode`, and `@RequiredArgsConstructor` |
| `@Getter` / `@Setter` | Generates getter/setter methods |
| `@AllArgsConstructor` | Generates constructor with **all fields** |
| `@NoArgsConstructor` | Generates constructor with **no fields** |
| `@Builder` | Implements builder pattern |
| `@ToString` | Generates `toString()` method |
