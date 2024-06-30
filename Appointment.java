package com.intakhab.hospitalmanagementhackonit.Model;

import jakarta.persistence.*;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.time.LocalDate;
import java.time.LocalTime;
import java.util.UUID;

@Entity
@Data
@NoArgsConstructor
@AllArgsConstructor
public class Appointment {
    @Id
    @GeneratedValue(strategy = GenerationType.UUID)
    private UUID id;
    private String patientName;
    private int age;
    private String symptoms;
    private String gender;
    private int consultationFee;
    private LocalDate appointmentDate;
    private LocalTime appointmentTime;
    private UUID doctorid;
    @ManyToOne
    private Doctor doctor;
    @ManyToOne
    private User user;

}
