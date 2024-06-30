package com.intakhab.hospitalmanagementhackonit.Repository;

import com.intakhab.hospitalmanagementhackonit.Model.Appointment;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;
import org.springframework.web.bind.annotation.RequestBody;

import java.util.UUID;

@Repository
public interface AppointmentRepo extends JpaRepository<Appointment, UUID> {
}
