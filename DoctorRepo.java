package com.intakhab.hospitalmanagementhackonit.Repository;

import com.intakhab.hospitalmanagementhackonit.Model.Doctor;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.UUID;

@Repository
public interface DoctorRepo extends JpaRepository<Doctor, UUID>{
}
