from telnetlib import STATUS
from django.db import models

from apps.accounts.models import Account

class RaspberrySettings(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True)
    created_by = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="created_raspberry_settings")
    updated_at = models.DateField(auto_now_add=True)
    updated_by = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="updated_raspberries_settings")

    #OBD PIDs
    PIDS_A = models.BooleanField(default=False)
    STATUS = models.BooleanField(default=False)
    FREEZE_DTC = models.BooleanField(default=False)
    FUEL_STATUS = models.BooleanField(default=False)
    ENGINE_LOAD = models.BooleanField(default=False)
    COOLANT_TEMP = models.BooleanField(default=False)
    SHORT_FUEL_TRIM_1 = models.BooleanField(default=False)
    LONG_FUEL_TRIM_1 = models.BooleanField(default=False)
    SHORT_FUEL_TRIM_2 = models.BooleanField(default=False)
    LONG_FUEL_TRIM_2 = models.BooleanField(default=False)
    FUEL_PRESSURE = models.BooleanField(default=False)
    INTAKE_PRESSURE = models.BooleanField(default=False)
    RPM = models.BooleanField(default=False)
    SPEED = models.BooleanField(default=False)
    TIMING_ADVANCE = models.BooleanField(default=False)
    INTAKE_TEMP = models.BooleanField(default=False)
    MAF = models.BooleanField(default=False)
    THROTTLE_POS = models.BooleanField(default=False)
    AIR_STATUS = models.BooleanField(default=False)
    O2_SENSORS = models.BooleanField(default=False)
    O2_B1S1 = models.BooleanField(default=False)
    O2_B1S2 = models.BooleanField(default=False)
    O2_B1S3 = models.BooleanField(default=False)
    O2_B1S4 = models.BooleanField(default=False)
    O2_B2S1 = models.BooleanField(default=False)
    O2_B2S2 = models.BooleanField(default=False)
    O2_B2S3 = models.BooleanField(default=False)
    O2_B2S4 = models.BooleanField(default=False)
    OBD_COMPLIANCE = models.BooleanField(default=False)
    O2_SENSORS_ALT = models.BooleanField(default=False)
    AUX_INPUT_STATUS = models.BooleanField(default=False)
    RUN_TIME = models.BooleanField(default=False)
    PIDS_B = models.BooleanField(default=False)
    DISTANCE_W_MIL = models.BooleanField(default=False)
    FUEL_RAIL_PRESSURE_VAC = models.BooleanField(default=False)
    FUEL_RAIL_PRESSURE_DIRECT = models.BooleanField(default=False)
    O2_S1_WR_VOLTAGE = models.BooleanField(default=False)
    O2_S2_WR_VOLTAGE = models.BooleanField(default=False)
    O2_S3_WR_VOLTAGE = models.BooleanField(default=False)
    O2_S4_WR_VOLTAGE = models.BooleanField(default=False)
    O2_S5_WR_VOLTAGE = models.BooleanField(default=False)
    O2_S6_WR_VOLTAGE = models.BooleanField(default=False)
    O2_S7_WR_VOLTAGE = models.BooleanField(default=False)
    O2_S8_WR_VOLTAGE = models.BooleanField(default=False)
    COMMANDED_EGR = models.BooleanField(default=False)
    EGR_ERROR = models.BooleanField(default=False)
    EVAPORATIVE_PURGE = models.BooleanField(default=False)
    FUEL_LEVEL = models.BooleanField(default=False)
    WARMUPS_SINCE_DTC_CLEAR = models.BooleanField(default=False)
    DISTANCE_SINCE_DTC_CLEAR = models.BooleanField(default=False)
    EVAP_VAPOR_PRESSURE = models.BooleanField(default=False)
    BAROMETRIC_PRESSURE = models.BooleanField(default=False)
    O2_S1_WR_CURRENT = models.BooleanField(default=False)
    O2_S2_WR_CURRENT = models.BooleanField(default=False)
    O2_S3_WR_CURRENT = models.BooleanField(default=False)
    O2_S4_WR_CURRENT = models.BooleanField(default=False)
    O2_S5_WR_CURRENT = models.BooleanField(default=False)
    O2_S6_WR_CURRENT = models.BooleanField(default=False)
    O2_S7_WR_CURRENT = models.BooleanField(default=False)
    O2_S8_WR_CURRENT = models.BooleanField(default=False)
    CATALYST_TEMP_B1S1 = models.BooleanField(default=False)
    CATALYST_TEMP_B2S1 = models.BooleanField(default=False)
    CATALYST_TEMP_B1S2 = models.BooleanField(default=False)
    CATALYST_TEMP_B2S2 = models.BooleanField(default=False)
    PIDS_C = models.BooleanField(default=False)
    STATUS_DRIVE_CYCLE = models.BooleanField(default=False)
    CONTROL_MODULE_VOLTAGE = models.BooleanField(default=False)
    ABSOLUTE_LOAD = models.BooleanField(default=False)
    COMMANDED_EQUIV_RATIO = models.BooleanField(default=False)
    RELATIVE_THROTTLE_POS = models.BooleanField(default=False)
    AMBIANT_AIR_TEMP = models.BooleanField(default=False)
    THROTTLE_POS_B = models.BooleanField(default=False)
    THROTTLE_POS_C = models.BooleanField(default=False)
    ACCELERATOR_POS_D = models.BooleanField(default=False)
    ACCELERATOR_POS_E = models.BooleanField(default=False)
    ACCELERATOR_POS_F = models.BooleanField(default=False)
    THROTTLE_ACTUATOR = models.BooleanField(default=False)
    RUN_TIME_MIL = models.BooleanField(default=False)
    TIME_SINCE_DTC_CLEARED = models.BooleanField(default=False)
    MAX_MAF = models.BooleanField(default=False)
    FUEL_TYPE = models.BooleanField(default=False)
    ETHANOL_PERCENT = models.BooleanField(default=False)
    EVAP_VAPOR_PRESSURE_ABS = models.BooleanField(default=False)
    EVAP_VAPOR_PRESSURE_ALT = models.BooleanField(default=False)
    SHORT_O2_TRIM_B1 = models.BooleanField(default=False)
    LONG_O2_TRIM_B1 = models.BooleanField(default=False)
    SHORT_O2_TRIM_B2 = models.BooleanField(default=False)
    LONG_O2_TRIM_B2 = models.BooleanField(default=False)
    FUEL_RAIL_PRESSURE_ABS = models.BooleanField(default=False)
    RELATIVE_ACCEL_POS = models.BooleanField(default=False)
    HYBRID_BATTERY_REMAINING = models.BooleanField(default=False)
    OIL_TEMP = models.BooleanField(default=False)
    FUEL_INJECT_TIMING = models.BooleanField(default=False)
    FUEL_RATE = models.BooleanField(default=False)

class Raspberry(models.Model):
    name = models.CharField(max_length=255)
    raspberry_account = models.OneToOneField(Account, on_delete=models.CASCADE, related_name="raspberry", null=True, blank=True)
    used_by = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="used_raspberries", null=True, blank=True)
    settings = models.ForeignKey(RaspberrySettings, on_delete=models.CASCADE, related_name="raspberries", null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)
    created_by = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="created_raspberries")
    updated_at = models.DateField(auto_now=True)
    updated_by = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="updated_raspberries")

