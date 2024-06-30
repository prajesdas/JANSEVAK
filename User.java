package com.intakhab.hospitalmanagementhackonit.Model;

import com.intakhab.hospitalmanagementhackonit.Enum.UserAction;
import com.intakhab.hospitalmanagementhackonit.Enum.UserRole;
import jakarta.persistence.*;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
import org.springframework.web.bind.annotation.PostMapping;

import java.time.LocalDate;
import java.time.LocalDateTime;
import java.util.List;
import java.util.UUID;

@Entity
@Data
@NoArgsConstructor
@AllArgsConstructor
public class User {
    @Id
    @GeneratedValue(strategy = GenerationType.UUID)
    private UUID id;
    private String name;
    private String email;
    private String mobile;
    private String username;
    private String password;
    @Enumerated(EnumType.STRING)
    private UserRole role;
    @Enumerated(EnumType.STRING)
    private UserAction action;
    private LocalDate registrationDate;
    private String token;
    private long tokenExpiryTime;
    @OneToMany(mappedBy = "user")
    private List<Appointment> appointmentList;

}
