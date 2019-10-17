-- MySQL Script generated by MySQL Workbench
-- Thu Oct 10 00:43:54 2019
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 ;
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`user_information`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`user_information` (
  `user_id` VARCHAR(200) NOT NULL,
  `username` VARCHAR(200) NULL DEFAULT NULL,
  `password` VARCHAR(200) NULL DEFAULT NULL,
  PRIMARY KEY (`user_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`image`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`image` (
  `user_id` VARCHAR(200) NOT NULL,
  `origin_path` VARCHAR(250) NOT NULL,
  `thumb_path` VARCHAR(250) NULL DEFAULT NULL,
  `text_path` VARCHAR(250) NULL,
  PRIMARY KEY (`user_id`, `origin_path`),
  INDEX `fk_picture_path_user_information_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_picture_path_user_information`
    FOREIGN KEY (`user_id`)
    REFERENCES `mydb`.`user_information` (`user_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
