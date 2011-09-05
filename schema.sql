SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL';

CREATE SCHEMA IF NOT EXISTS `sysstat` DEFAULT CHARACTER SET utf8 COLLATE utf8_bin ;
USE `sysstat` ;

-- -----------------------------------------------------
-- Table `sysstat`.`host`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `sysstat`.`host` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT ,
  `name` VARCHAR(45) NOT NULL ,
  `uuid` VARCHAR(45) NOT NULL ,
  PRIMARY KEY (`id`) ,
  UNIQUE INDEX `uuid_UNIQUE` (`uuid` ASC) )
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `sysstat`.`interface`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `sysstat`.`interface` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT ,
  `host_id` INT UNSIGNED NOT NULL ,
  `name` VARCHAR(45) NOT NULL ,
  PRIMARY KEY (`id`) ,
  INDEX `fk_interface_host1` (`host_id` ASC) ,
  CONSTRAINT `fk_interface_host1`
    FOREIGN KEY (`host_id` )
    REFERENCES `sysstat`.`host` (`id` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `sysstat`.`stats_interface`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `sysstat`.`stats_interface` (
  `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT ,
  `interface_id` INT UNSIGNED NOT NULL ,
  `in` BIGINT UNSIGNED NOT NULL ,
  `out` BIGINT UNSIGNED NOT NULL ,
  `time` DATETIME NOT NULL ,
  PRIMARY KEY (`id`) ,
  INDEX `fk_stats_interface_interface` (`interface_id` ASC) ,
  INDEX `time` (`time` ASC) ,
  CONSTRAINT `fk_stats_interface_interface`
    FOREIGN KEY (`interface_id` )
    REFERENCES `sysstat`.`interface` (`id` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `sysstat`.`mount`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `sysstat`.`mount` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT ,
  `host_id` INT UNSIGNED NOT NULL ,
  `mountpoint` VARCHAR(256) NOT NULL ,
  PRIMARY KEY (`id`) ,
  INDEX `fk_disk_host1` (`host_id` ASC) ,
  CONSTRAINT `fk_disk_host1`
    FOREIGN KEY (`host_id` )
    REFERENCES `sysstat`.`host` (`id` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `sysstat`.`stats_mount`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `sysstat`.`stats_mount` (
  `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT ,
  `mount_id` INT UNSIGNED NOT NULL ,
  `used` BIGINT UNSIGNED NOT NULL ,
  `available` BIGINT UNSIGNED NOT NULL ,
  `time` DATETIME NOT NULL ,
  PRIMARY KEY (`id`) ,
  INDEX `fk_stats_mount_mount1` (`mount_id` ASC) ,
  INDEX `time` (`time` ASC) ,
  CONSTRAINT `fk_stats_mount_mount1`
    FOREIGN KEY (`mount_id` )
    REFERENCES `sysstat`.`mount` (`id` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `sysstat`.`iptables_target`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `sysstat`.`iptables_target` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT ,
  `host_id` INT UNSIGNED NOT NULL ,
  `name` VARCHAR(45) NOT NULL ,
  PRIMARY KEY (`id`) ,
  INDEX `fk_iptables_targets_host1` (`host_id` ASC) ,
  CONSTRAINT `fk_iptables_targets_host1`
    FOREIGN KEY (`host_id` )
    REFERENCES `sysstat`.`host` (`id` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `sysstat`.`stats_iptables_target`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `sysstat`.`stats_iptables_target` (
  `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT ,
  `iptables_targets_id` INT UNSIGNED NOT NULL ,
  `data` BIGINT UNSIGNED NOT NULL ,
  `time` DATETIME NOT NULL ,
  PRIMARY KEY (`id`) ,
  INDEX `fk_stats_iptables_iptables_targets1` (`iptables_targets_id` ASC) ,
  INDEX `time` (`time` ASC) ,
  CONSTRAINT `fk_stats_iptables_iptables_targets1`
    FOREIGN KEY (`iptables_targets_id` )
    REFERENCES `sysstat`.`iptables_target` (`id` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `sysstat`.`stats_cpu`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `sysstat`.`stats_cpu` (
  `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT ,
  `host_id` INT UNSIGNED NOT NULL ,
  `loadavg_1` DECIMAL(3,2) UNSIGNED NOT NULL ,
  `loadavg_5` DECIMAL(3,2) UNSIGNED NOT NULL ,
  `loadavg_15` DECIMAL(3,2) UNSIGNED NOT NULL ,
  `usr` DECIMAL(3,2) UNSIGNED NOT NULL ,
  `nice` DECIMAL(3,2) UNSIGNED NOT NULL ,
  `sys` DECIMAL(3,2) UNSIGNED NOT NULL ,
  `iowait` DECIMAL(3,2) UNSIGNED NOT NULL ,
  `irq` DECIMAL(3,2) UNSIGNED NOT NULL ,
  `steal` DECIMAL(3,2) UNSIGNED NOT NULL ,
  `guest` DECIMAL(3,2) UNSIGNED NOT NULL ,
  `idle` DECIMAL(3,2) UNSIGNED NOT NULL ,
  `soft` DECIMAL(3,2) UNSIGNED NOT NULL ,
  `time` DATETIME NOT NULL ,
  PRIMARY KEY (`id`) ,
  INDEX `fk_stats_cup_host1` (`host_id` ASC) ,
  INDEX `time` (`time` ASC) ,
  CONSTRAINT `fk_stats_cup_host1`
    FOREIGN KEY (`host_id` )
    REFERENCES `sysstat`.`host` (`id` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `sysstat`.`stats_memory`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `sysstat`.`stats_memory` (
  `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT ,
  `host_id` INT UNSIGNED NOT NULL ,
  `mem_free` INT UNSIGNED NOT NULL ,
  `mem_total` INT UNSIGNED NOT NULL ,
  `swap_free` INT UNSIGNED NOT NULL ,
  `swap_total` INT UNSIGNED NOT NULL ,
  `time` DATETIME NOT NULL ,
  PRIMARY KEY (`id`) ,
  INDEX `fk_memory_host1` (`host_id` ASC) ,
  INDEX `time` (`time` ASC) ,
  CONSTRAINT `fk_memory_host1`
    FOREIGN KEY (`host_id` )
    REFERENCES `sysstat`.`host` (`id` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `sysstat`.`enabled_module`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `sysstat`.`enabled_module` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT ,
  `host_id` INT UNSIGNED NOT NULL ,
  `module` VARCHAR(45) NOT NULL ,
  `status` TINYINT(1)  NOT NULL ,
  PRIMARY KEY (`id`) ,
  INDEX `fk_enabled_module_host1` (`host_id` ASC) ,
  CONSTRAINT `fk_enabled_module_host1`
    FOREIGN KEY (`host_id` )
    REFERENCES `sysstat`.`host` (`id` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;



SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
