# SNMP MIB module (IJ8060-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IJ8060-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:08:59 2024
# On host MacBook-Pro.local platform Darwin version 24.0.0 by user lextm
# Using Python version 3.12.0 (main, Nov 14 2023, 23:52:11) [Clang 15.0.0 (clang-1500.0.40.1)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint,
 ConstraintsUnion) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint",
    "ConstraintsUnion")

# Import SMI symbols from the MIBs this MIB depends on

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hp_ObjectIdentity = ObjectIdentity
hp = _Hp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11)
)
_Dm_ObjectIdentity = ObjectIdentity
dm = _Dm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2)
)
_Device_ObjectIdentity = ObjectIdentity
device = _Device_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1)
)
_Device_system_ObjectIdentity = ObjectIdentity
device_system = _Device_system_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1)
)
_Settings_system_ObjectIdentity = ObjectIdentity
settings_system = _Settings_system_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 1)
)
_Energy_star_Type = Integer32
_Energy_star_Object = MibScalar
energy_star = _Energy_star_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 1, 1),
    _Energy_star_Type()
)
energy_star.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    energy_star.setStatus("optional")


class _Sleep_mode_Type(Integer32):
    """Custom type sleep_mode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eFalse", 1),
          ("eTrue", 2))
    )


_Sleep_mode_Type.__name__ = "Integer32"
_Sleep_mode_Object = MibScalar
sleep_mode = _Sleep_mode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 1, 2),
    _Sleep_mode_Type()
)
sleep_mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleep_mode.setStatus("optional")


class _Date_display_Type(Integer32):
    """Custom type date_display based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("eDateDisplayDD-MMM-YYYY", 5),
          ("eDateDisplayMMM-DD-YYYY", 4),
          ("eDateDisplayYYYY-MMM-DD", 6))
    )


_Date_display_Type.__name__ = "Integer32"
_Date_display_Object = MibScalar
date_display = _Date_display_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 1, 22),
    _Date_display_Type()
)
date_display.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    date_display.setStatus("optional")


class _Mono_color_switching_mode_Type(Integer32):
    """Custom type mono_color_switching_mode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("eAutoSwitch", 1),
          ("eMostlyColor", 2),
          ("eMostlyMono", 3))
    )


_Mono_color_switching_mode_Type.__name__ = "Integer32"
_Mono_color_switching_mode_Object = MibScalar
mono_color_switching_mode = _Mono_color_switching_mode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 1, 31),
    _Mono_color_switching_mode_Type()
)
mono_color_switching_mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mono_color_switching_mode.setStatus("optional")
_Device_configure_ObjectIdentity = ObjectIdentity
device_configure = _Device_configure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 1, 32)
)


class _Device_configure_printer_parameters_Type(OctetString):
    """Custom type device_configure_printer_parameters based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_Device_configure_printer_parameters_Type.__name__ = "OctetString"
_Device_configure_printer_parameters_Object = MibScalar
device_configure_printer_parameters = _Device_configure_printer_parameters_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 1, 32, 12),
    _Device_configure_printer_parameters_Type()
)
device_configure_printer_parameters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    device_configure_printer_parameters.setStatus("optional")


class _Direct_connect_ports_enable_Type(Integer32):
    """Custom type direct_connect_ports_enable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("eFalse", 1),
          ("eTrue", 2),
          ("eUnSupported", 3))
    )


_Direct_connect_ports_enable_Type.__name__ = "Integer32"
_Direct_connect_ports_enable_Object = MibScalar
direct_connect_ports_enable = _Direct_connect_ports_enable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 1, 43),
    _Direct_connect_ports_enable_Type()
)
direct_connect_ports_enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    direct_connect_ports_enable.setStatus("optional")


class _Control_panel_supplies_status_message_Type(Integer32):
    """Custom type control_panel_supplies_status_message based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eDontShow", 2),
          ("eShow", 1))
    )


_Control_panel_supplies_status_message_Type.__name__ = "Integer32"
_Control_panel_supplies_status_message_Object = MibScalar
control_panel_supplies_status_message = _Control_panel_supplies_status_message_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 1, 44),
    _Control_panel_supplies_status_message_Type()
)
control_panel_supplies_status_message.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    control_panel_supplies_status_message.setStatus("optional")


class _Power_state_Type(Integer32):
    """Custom type power_state based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("ePowerStateAwake", 1),
          ("ePowerStateOff", 4),
          ("ePowerStatePowerSave", 2),
          ("ePowerStateSleep", 3),
          ("ePowerStateTransitioningToAwake", 5),
          ("ePowerStateTransitioningToOff", 8),
          ("ePowerStateTransitioningToPowerSave", 6),
          ("ePowerStateTransitioningToSleep", 7))
    )


_Power_state_Type.__name__ = "Integer32"
_Power_state_Object = MibScalar
power_state = _Power_state_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 1, 65),
    _Power_state_Type()
)
power_state.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    power_state.setStatus("optional")
_Factory_reset_Type = Integer32
_Factory_reset_Object = MibScalar
factory_reset = _Factory_reset_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 1, 68),
    _Factory_reset_Type()
)
factory_reset.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    factory_reset.setStatus("optional")


class _Display_long_grain_optimization_warning_Type(Integer32):
    """Custom type display_long_grain_optimization_warning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eDisplay", 2),
          ("eDoNotDisplay", 1))
    )


_Display_long_grain_optimization_warning_Type.__name__ = "Integer32"
_Display_long_grain_optimization_warning_Object = MibScalar
display_long_grain_optimization_warning = _Display_long_grain_optimization_warning_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 1, 84),
    _Display_long_grain_optimization_warning_Type()
)
display_long_grain_optimization_warning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    display_long_grain_optimization_warning.setStatus("optional")


class _Powersave_enable_type_Type(Integer32):
    """Custom type powersave_enable_type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("ePowerSaveCustom", 5),
          ("ePowerSaveMaximize", 4),
          ("ePowerSaveOff", 1),
          ("ePowerSaveUseSleepDelay", 2),
          ("ePowerSaveUseSleepSchedule", 3))
    )


_Powersave_enable_type_Type.__name__ = "Integer32"
_Powersave_enable_type_Object = MibScalar
powersave_enable_type = _Powersave_enable_type_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 1, 89),
    _Powersave_enable_type_Type()
)
powersave_enable_type.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    powersave_enable_type.setStatus("optional")
_Status_system_ObjectIdentity = ObjectIdentity
status_system = _Status_system_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 2)
)


class _On_off_line_Type(Integer32):
    """Custom type on_off_line based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("eOffline", 2),
          ("eOfflineAtEndOfJob", 3),
          ("eOnline", 1))
    )


_On_off_line_Type.__name__ = "Integer32"
_On_off_line_Object = MibScalar
on_off_line = _On_off_line_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 2, 5),
    _On_off_line_Type()
)
on_off_line.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    on_off_line.setStatus("optional")


class __pysmi_continue_Type(Integer32):
    """Custom type _pysmi_continue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("eEjectAndWait", 5),
          ("eInitiateAction", 1),
          ("eRetry", 2),
          ("eRetryAndCheck", 3),
          ("eSelectMediaSize", 6),
          ("eUseLoadedMedia", 4))
    )


__pysmi_continue_Type.__name__ = "Integer32"
__pysmi_continue_Object = MibScalar
_pysmi_continue = __pysmi_continue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 2, 6),
    __pysmi_continue_Type()
)
_pysmi_continue.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    _pysmi_continue.setStatus("optional")


class _Auto_continue_Type(Integer32):
    """Custom type auto_continue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eOff", 1),
          ("eOn", 2))
    )


_Auto_continue_Type.__name__ = "Integer32"
_Auto_continue_Object = MibScalar
auto_continue = _Auto_continue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 2, 7),
    _Auto_continue_Type()
)
auto_continue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    auto_continue.setStatus("optional")


class _Install_date_Type(OctetString):
    """Custom type install_date based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(13, 13),
    )


_Install_date_Type.__name__ = "OctetString"
_Install_date_Object = MibScalar
install_date = _Install_date_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 2, 8),
    _Install_date_Type()
)
install_date.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    install_date.setStatus("optional")
_Perm_store_init_occurred_Type = OctetString
_Perm_store_init_occurred_Object = MibScalar
perm_store_init_occurred = _Perm_store_init_occurred_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 2, 10),
    _Perm_store_init_occurred_Type()
)
perm_store_init_occurred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perm_store_init_occurred.setStatus("optional")


class _Timestamp_Type(OctetString):
    """Custom type timestamp based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(15, 15),
    )


_Timestamp_Type.__name__ = "OctetString"
_Timestamp_Object = MibScalar
timestamp = _Timestamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 2, 13),
    _Timestamp_Type()
)
timestamp.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    timestamp.setStatus("optional")
_Date_and_time_Type = OctetString
_Date_and_time_Object = MibScalar
date_and_time = _Date_and_time_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 2, 17),
    _Date_and_time_Type()
)
date_and_time.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    date_and_time.setStatus("optional")


class _Service_id_Type(OctetString):
    """Custom type service_id based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_Service_id_Type.__name__ = "OctetString"
_Service_id_Object = MibScalar
service_id = _Service_id_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 2, 19),
    _Service_id_Type()
)
service_id.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    service_id.setStatus("optional")
_Display_ObjectIdentity = ObjectIdentity
display = _Display_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 2, 20)
)
_Display_status_ObjectIdentity = ObjectIdentity
display_status = _Display_status_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 2, 20, 1)
)


class _Show_address_Type(Integer32):
    """Custom type show_address based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("eAuto", 3),
          ("eOff", 1))
    )


_Show_address_Type.__name__ = "Integer32"
_Show_address_Object = MibScalar
show_address = _Show_address_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 2, 20, 1, 3),
    _Show_address_Type()
)
show_address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    show_address.setStatus("optional")


class _Time_display_Type(Integer32):
    """Custom type time_display based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eTimeDisplayTwelveHour", 1),
          ("eTimeDisplayTwentyFourHour", 2))
    )


_Time_display_Type.__name__ = "Integer32"
_Time_display_Object = MibScalar
time_display = _Time_display_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 2, 28),
    _Time_display_Type()
)
time_display.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    time_display.setStatus("optional")


class _Job_input_auto_continue_timeout_Type(Integer32):
    """Custom type job_input_auto_continue_timeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 3600),
    )


_Job_input_auto_continue_timeout_Type.__name__ = "Integer32"
_Job_input_auto_continue_timeout_Object = MibScalar
job_input_auto_continue_timeout = _Job_input_auto_continue_timeout_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 2, 35),
    _Job_input_auto_continue_timeout_Type()
)
job_input_auto_continue_timeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    job_input_auto_continue_timeout.setStatus("optional")
_Job_input_auto_continue_mode_Type = OctetString
_Job_input_auto_continue_mode_Object = MibScalar
job_input_auto_continue_mode = _Job_input_auto_continue_mode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 2, 36),
    _Job_input_auto_continue_mode_Type()
)
job_input_auto_continue_mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    job_input_auto_continue_mode.setStatus("optional")
_Background_message_ObjectIdentity = ObjectIdentity
background_message = _Background_message_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 2, 37)
)
_Background_message1_ObjectIdentity = ObjectIdentity
background_message1 = _Background_message1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 2, 37, 1)
)


class _Background_status_msg_line1_part1_Type(OctetString):
    """Custom type background_status_msg_line1_part1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Background_status_msg_line1_part1_Type.__name__ = "OctetString"
_Background_status_msg_line1_part1_Object = MibScalar
background_status_msg_line1_part1 = _Background_status_msg_line1_part1_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 2, 37, 1, 1),
    _Background_status_msg_line1_part1_Type()
)
background_status_msg_line1_part1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    background_status_msg_line1_part1.setStatus("optional")
_Background_message2_ObjectIdentity = ObjectIdentity
background_message2 = _Background_message2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 2, 37, 2)
)


class _Background_status_msg_line2_part1_Type(OctetString):
    """Custom type background_status_msg_line2_part1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Background_status_msg_line2_part1_Type.__name__ = "OctetString"
_Background_status_msg_line2_part1_Object = MibScalar
background_status_msg_line2_part1 = _Background_status_msg_line2_part1_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 2, 37, 2, 1),
    _Background_status_msg_line2_part1_Type()
)
background_status_msg_line2_part1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    background_status_msg_line2_part1.setStatus("optional")


class _Background_status_msg_higher_priority_Type(OctetString):
    """Custom type background_status_msg_higher_priority based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_Background_status_msg_higher_priority_Type.__name__ = "OctetString"
_Background_status_msg_higher_priority_Object = MibScalar
background_status_msg_higher_priority = _Background_status_msg_higher_priority_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 2, 37, 5),
    _Background_status_msg_higher_priority_Type()
)
background_status_msg_higher_priority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    background_status_msg_higher_priority.setStatus("optional")


class _Error_log_clear_Type(Integer32):
    """Custom type error_log_clear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("eClearErrorLog", 1)
    )


_Error_log_clear_Type.__name__ = "Integer32"
_Error_log_clear_Object = MibScalar
error_log_clear = _Error_log_clear_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 2, 38),
    _Error_log_clear_Type()
)
error_log_clear.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    error_log_clear.setStatus("optional")


class _Job_output_auto_continue_timeout_Type(Integer32):
    """Custom type job_output_auto_continue_timeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 3600),
    )


_Job_output_auto_continue_timeout_Type.__name__ = "Integer32"
_Job_output_auto_continue_timeout_Object = MibScalar
job_output_auto_continue_timeout = _Job_output_auto_continue_timeout_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 2, 40),
    _Job_output_auto_continue_timeout_Type()
)
job_output_auto_continue_timeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    job_output_auto_continue_timeout.setStatus("optional")
_Collated_originals_support_Type = OctetString
_Collated_originals_support_Object = MibScalar
collated_originals_support = _Collated_originals_support_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 2, 42),
    _Collated_originals_support_Type()
)
collated_originals_support.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    collated_originals_support.setStatus("optional")
_Localization_languages_supported_Type = OctetString
_Localization_languages_supported_Object = MibScalar
localization_languages_supported = _Localization_languages_supported_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 2, 52),
    _Localization_languages_supported_Type()
)
localization_languages_supported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    localization_languages_supported.setStatus("optional")
_Localization_countries_supported_Type = OctetString
_Localization_countries_supported_Object = MibScalar
localization_countries_supported = _Localization_countries_supported_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 2, 53),
    _Localization_countries_supported_Type()
)
localization_countries_supported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    localization_countries_supported.setStatus("optional")
_Host_application_available_memory_Type = Integer32
_Host_application_available_memory_Object = MibScalar
host_application_available_memory = _Host_application_available_memory_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 2, 59),
    _Host_application_available_memory_Type()
)
host_application_available_memory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    host_application_available_memory.setStatus("optional")


class _Control_panel_button_press_Type(Integer32):
    """Custom type control_panel_button_press based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              9)
        )
    )
    namedValues = NamedValues(
        *(("eCancelJobButton", 9),
          ("eGoButton", 1))
    )


_Control_panel_button_press_Type.__name__ = "Integer32"
_Control_panel_button_press_Object = MibScalar
control_panel_button_press = _Control_panel_button_press_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 2, 60),
    _Control_panel_button_press_Type()
)
control_panel_button_press.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    control_panel_button_press.setStatus("optional")
_Control_panel_display_contents_change_counter_Type = Integer32
_Control_panel_display_contents_change_counter_Object = MibScalar
control_panel_display_contents_change_counter = _Control_panel_display_contents_change_counter_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 2, 63),
    _Control_panel_display_contents_change_counter_Type()
)
control_panel_display_contents_change_counter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    control_panel_display_contents_change_counter.setStatus("optional")
_Control_panel_display_contents_crc_Type = Integer32
_Control_panel_display_contents_crc_Object = MibScalar
control_panel_display_contents_crc = _Control_panel_display_contents_crc_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 2, 64),
    _Control_panel_display_contents_crc_Type()
)
control_panel_display_contents_crc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    control_panel_display_contents_crc.setStatus("optional")
_Control_panel_display_ObjectIdentity = ObjectIdentity
control_panel_display = _Control_panel_display_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 2, 65)
)
_Control_panel_display_graphical_contents_Type = OctetString
_Control_panel_display_graphical_contents_Object = MibScalar
control_panel_display_graphical_contents = _Control_panel_display_graphical_contents_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 2, 65, 1),
    _Control_panel_display_graphical_contents_Type()
)
control_panel_display_graphical_contents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    control_panel_display_graphical_contents.setStatus("optional")


class _Control_panel_key_press_Type(Integer32):
    """Custom type control_panel_key_press based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Control_panel_key_press_Type.__name__ = "Integer32"
_Control_panel_key_press_Object = MibScalar
control_panel_key_press = _Control_panel_key_press_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 2, 66),
    _Control_panel_key_press_Type()
)
control_panel_key_press.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    control_panel_key_press.setStatus("optional")


class _Rtc_time_zone_Type(Integer32):
    """Custom type rtc_time_zone based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73,
              74,
              75)
        )
    )
    namedValues = NamedValues(
        *(("eTzAUSCentral", 66),
          ("eTzAUSEastern", 68),
          ("eTzAfghanistan", 46),
          ("eTzAlaskan", 4),
          ("eTzArab", 40),
          ("eTzArabian", 44),
          ("eTzArabic", 39),
          ("eTzAtlantic", 16),
          ("eTzAzores", 24),
          ("eTzCanadaCentral", 12),
          ("eTzCapeVerde", 25),
          ("eTzCaucasus", 45),
          ("eTzCenAustralia", 65),
          ("eTzCentral", 10),
          ("eTzCentralAmerica", 9),
          ("eTzCentralAsia", 52),
          ("eTzCentralEurope", 29),
          ("eTzCentralEuropean", 31),
          ("eTzCentralPacific", 72),
          ("eTzChina", 57),
          ("eTzDateline", 1),
          ("eTzEAfrica", 42),
          ("eTzEAustralia", 67),
          ("eTzESouthAmerica", 20),
          ("eTzEastern", 14),
          ("eTzEeurope", 34),
          ("eTzEgypt", 35),
          ("eTzEkaterinburg", 47),
          ("eTzFLE", 37),
          ("eTzFiji", 74),
          ("eTzGMT", 27),
          ("eTzGTB", 33),
          ("eTzGreenland", 22),
          ("eTzGreenwich", 26),
          ("eTzHawaiian", 3),
          ("eTzIndia", 49),
          ("eTzIran", 43),
          ("eTzJerusalem", 38),
          ("eTzKorea", 63),
          ("eTzMalayPeninsula", 59),
          ("eTzMexico", 11),
          ("eTzMexico2", 7),
          ("eTzMidAtlantic", 23),
          ("eTzMountain", 8),
          ("eTzMyanmar", 54),
          ("eTzNCentralAsia", 51),
          ("eTzNepal", 50),
          ("eTzNewZealand", 73),
          ("eTzNewfoundland", 19),
          ("eTzNorthAsia", 56),
          ("eTzNorthAsiaEast", 58),
          ("eTzPacific", 5),
          ("eTzPacificSA", 18),
          ("eTzRomance", 30),
          ("eTzRussian", 41),
          ("eTzSAEastern", 21),
          ("eTzSAPacific", 13),
          ("eTzSAWestern", 17),
          ("eTzSEAsia", 55),
          ("eTzSamoa", 2),
          ("eTzSouthAfrica", 36),
          ("eTzSriLanka", 53),
          ("eTzTaipei", 61),
          ("eTzTasmania", 70),
          ("eTzTokyo", 62),
          ("eTzTonga", 75),
          ("eTzUSEastern", 15),
          ("eTzUSMountain", 6),
          ("eTzVladivostok", 71),
          ("eTzWAustralia", 60),
          ("eTzWCentralAfrica", 32),
          ("eTzWEurope", 28),
          ("eTzWestAsia", 48),
          ("eTzWestPacific", 69),
          ("eTzYakutsk", 64))
    )


_Rtc_time_zone_Type.__name__ = "Integer32"
_Rtc_time_zone_Object = MibScalar
rtc_time_zone = _Rtc_time_zone_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 2, 99),
    _Rtc_time_zone_Type()
)
rtc_time_zone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtc_time_zone.setStatus("optional")


class _Automatic_daylight_savings_Type(Integer32):
    """Custom type automatic_daylight_savings based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eOff", 1),
          ("eOn", 2))
    )


_Automatic_daylight_savings_Type.__name__ = "Integer32"
_Automatic_daylight_savings_Object = MibScalar
automatic_daylight_savings = _Automatic_daylight_savings_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 2, 100),
    _Automatic_daylight_savings_Type()
)
automatic_daylight_savings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    automatic_daylight_savings.setStatus("optional")
_Daylight_savings_start_Type = OctetString
_Daylight_savings_start_Object = MibScalar
daylight_savings_start = _Daylight_savings_start_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 2, 101),
    _Daylight_savings_start_Type()
)
daylight_savings_start.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    daylight_savings_start.setStatus("optional")
_Daylight_savings_end_Type = OctetString
_Daylight_savings_end_Object = MibScalar
daylight_savings_end = _Daylight_savings_end_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 2, 102),
    _Daylight_savings_end_Type()
)
daylight_savings_end.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    daylight_savings_end.setStatus("optional")
_Daylight_savings_offset_Type = Integer32
_Daylight_savings_offset_Object = MibScalar
daylight_savings_offset = _Daylight_savings_offset_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 2, 103),
    _Daylight_savings_offset_Type()
)
daylight_savings_offset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    daylight_savings_offset.setStatus("optional")


class _Daylight_savings_reset_Type(Integer32):
    """Custom type daylight_savings_reset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eCustomized", 2),
          ("eResetToDefault", 1))
    )


_Daylight_savings_reset_Type.__name__ = "Integer32"
_Daylight_savings_reset_Object = MibScalar
daylight_savings_reset = _Daylight_savings_reset_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 2, 104),
    _Daylight_savings_reset_Type()
)
daylight_savings_reset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    daylight_savings_reset.setStatus("optional")


class _Email_service_operational_Type(Integer32):
    """Custom type email_service_operational based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eNonOperational", 1),
          ("eOperational", 2))
    )


_Email_service_operational_Type.__name__ = "Integer32"
_Email_service_operational_Object = MibScalar
email_service_operational = _Email_service_operational_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 2, 111),
    _Email_service_operational_Type()
)
email_service_operational.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    email_service_operational.setStatus("optional")
_Id_ObjectIdentity = ObjectIdentity
id = _Id_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 3)
)
_Model_number_Type = OctetString
_Model_number_Object = MibScalar
model_number = _Model_number_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 3, 1),
    _Model_number_Type()
)
model_number.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    model_number.setStatus("optional")


class _Model_name_Type(OctetString):
    """Custom type model_name based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Model_name_Type.__name__ = "OctetString"
_Model_name_Object = MibScalar
model_name = _Model_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 3, 2),
    _Model_name_Type()
)
model_name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    model_name.setStatus("optional")


class _Serial_number_Type(OctetString):
    """Custom type serial_number based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_Serial_number_Type.__name__ = "OctetString"
_Serial_number_Object = MibScalar
serial_number = _Serial_number_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 3, 3),
    _Serial_number_Type()
)
serial_number.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serial_number.setStatus("optional")
_Fw_rom_datecode_Type = OctetString
_Fw_rom_datecode_Object = MibScalar
fw_rom_datecode = _Fw_rom_datecode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 3, 5),
    _Fw_rom_datecode_Type()
)
fw_rom_datecode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fw_rom_datecode.setStatus("optional")
_Fw_rom_revision_Type = OctetString
_Fw_rom_revision_Object = MibScalar
fw_rom_revision = _Fw_rom_revision_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 3, 6),
    _Fw_rom_revision_Type()
)
fw_rom_revision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fw_rom_revision.setStatus("optional")


class _Device_name_Type(OctetString):
    """Custom type device_name based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Device_name_Type.__name__ = "OctetString"
_Device_name_Object = MibScalar
device_name = _Device_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 3, 10),
    _Device_name_Type()
)
device_name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    device_name.setStatus("optional")
_Device_location_Type = OctetString
_Device_location_Object = MibScalar
device_location = _Device_location_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 3, 11),
    _Device_location_Type()
)
device_location.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    device_location.setStatus("optional")
_Asset_number_Type = OctetString
_Asset_number_Object = MibScalar
asset_number = _Asset_number_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 3, 12),
    _Asset_number_Type()
)
asset_number.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asset_number.setStatus("optional")
_Formatter_serial_number_Type = OctetString
_Formatter_serial_number_Object = MibScalar
formatter_serial_number = _Formatter_serial_number_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 3, 20),
    _Formatter_serial_number_Type()
)
formatter_serial_number.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    formatter_serial_number.setStatus("optional")
_Interface_ObjectIdentity = ObjectIdentity
interface = _Interface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4)
)
_Mio_ObjectIdentity = ObjectIdentity
mio = _Mio_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 3)
)
_Mio1_ObjectIdentity = ObjectIdentity
mio1 = _Mio1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 3, 1)
)
_Mio1_model_name_Type = OctetString
_Mio1_model_name_Object = MibScalar
mio1_model_name = _Mio1_model_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 3, 1, 2),
    _Mio1_model_name_Type()
)
mio1_model_name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mio1_model_name.setStatus("optional")
_Mio1_manufacturing_info_Type = OctetString
_Mio1_manufacturing_info_Object = MibScalar
mio1_manufacturing_info = _Mio1_manufacturing_info_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 3, 1, 3),
    _Mio1_manufacturing_info_Type()
)
mio1_manufacturing_info.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mio1_manufacturing_info.setStatus("optional")


class _Mio1_type_Type(Integer32):
    """Custom type mio1_type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              8,
              12)
        )
    )
    namedValues = NamedValues(
        *(("eDiskDrive", 8),
          ("eEmpty", 1),
          ("eIOCard", 12),
          ("eUnknown", 2))
    )


_Mio1_type_Type.__name__ = "Integer32"
_Mio1_type_Object = MibScalar
mio1_type = _Mio1_type_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 3, 1, 4),
    _Mio1_type_Type()
)
mio1_type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mio1_type.setStatus("optional")
_Mio4_ObjectIdentity = ObjectIdentity
mio4 = _Mio4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 3, 4)
)
_Mio4_model_name_Type = OctetString
_Mio4_model_name_Object = MibScalar
mio4_model_name = _Mio4_model_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 3, 4, 2),
    _Mio4_model_name_Type()
)
mio4_model_name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mio4_model_name.setStatus("optional")
_Mio4_manufacturing_info_Type = OctetString
_Mio4_manufacturing_info_Object = MibScalar
mio4_manufacturing_info = _Mio4_manufacturing_info_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 3, 4, 3),
    _Mio4_manufacturing_info_Type()
)
mio4_manufacturing_info.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mio4_manufacturing_info.setStatus("optional")


class _Mio4_type_Type(Integer32):
    """Custom type mio4_type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              12)
        )
    )
    namedValues = NamedValues(
        *(("eEmpty", 1),
          ("eIOCard", 12))
    )


_Mio4_type_Type.__name__ = "Integer32"
_Mio4_type_Object = MibScalar
mio4_type = _Mio4_type_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 3, 4, 4),
    _Mio4_type_Type()
)
mio4_type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mio4_type.setStatus("optional")
_Phd_ObjectIdentity = ObjectIdentity
phd = _Phd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 5)
)
_Phd1_ObjectIdentity = ObjectIdentity
phd1 = _Phd1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 5, 1)
)
_Phd1_diagnostics_nvram_data_Type = OctetString
_Phd1_diagnostics_nvram_data_Object = MibScalar
phd1_diagnostics_nvram_data = _Phd1_diagnostics_nvram_data_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 5, 1, 9),
    _Phd1_diagnostics_nvram_data_Type()
)
phd1_diagnostics_nvram_data.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phd1_diagnostics_nvram_data.setStatus("optional")
_Phd2_ObjectIdentity = ObjectIdentity
phd2 = _Phd2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 5, 2)
)
_Phd2_model_Type = OctetString
_Phd2_model_Object = MibScalar
phd2_model = _Phd2_model_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 5, 2, 1),
    _Phd2_model_Type()
)
phd2_model.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phd2_model.setStatus("optional")
_Phd2_manufacturing_info_Type = OctetString
_Phd2_manufacturing_info_Object = MibScalar
phd2_manufacturing_info = _Phd2_manufacturing_info_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 5, 2, 2),
    _Phd2_manufacturing_info_Type()
)
phd2_manufacturing_info.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phd2_manufacturing_info.setStatus("optional")


class _Phd2_type_Type(Integer32):
    """Custom type phd2_type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              10,
              11,
              13)
        )
    )
    namedValues = NamedValues(
        *(("eBindingPHD", 13),
          ("eInputPHD", 10),
          ("eOutputPHD", 11),
          ("eUnknown", 2))
    )


_Phd2_type_Type.__name__ = "Integer32"
_Phd2_type_Object = MibScalar
phd2_type = _Phd2_type_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 5, 2, 3),
    _Phd2_type_Type()
)
phd2_type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phd2_type.setStatus("optional")
_Phd2_capacity_Type = Integer32
_Phd2_capacity_Object = MibScalar
phd2_capacity = _Phd2_capacity_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 5, 2, 4),
    _Phd2_capacity_Type()
)
phd2_capacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phd2_capacity.setStatus("optional")
_Web_server_ObjectIdentity = ObjectIdentity
web_server = _Web_server_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 6)
)
_Settings_web_server_ObjectIdentity = ObjectIdentity
settings_web_server = _Settings_web_server_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 6, 1)
)


class _Web_proxy_config_enable_Type(Integer32):
    """Custom type web_proxy_config_enable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("eOff", 0),
          ("eOn", 1))
    )


_Web_proxy_config_enable_Type.__name__ = "Integer32"
_Web_proxy_config_enable_Object = MibScalar
web_proxy_config_enable = _Web_proxy_config_enable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 6, 1, 4),
    _Web_proxy_config_enable_Type()
)
web_proxy_config_enable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    web_proxy_config_enable.setStatus("optional")


class _Ews_request_control_panel_supplies_status_Type(Integer32):
    """Custom type ews_request_control_panel_supplies_status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eFalse", 1),
          ("eTrue", 2))
    )


_Ews_request_control_panel_supplies_status_Type.__name__ = "Integer32"
_Ews_request_control_panel_supplies_status_Object = MibScalar
ews_request_control_panel_supplies_status = _Ews_request_control_panel_supplies_status_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 6, 1, 5),
    _Ews_request_control_panel_supplies_status_Type()
)
ews_request_control_panel_supplies_status.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ews_request_control_panel_supplies_status.setStatus("optional")
_Foreign_interface_ObjectIdentity = ObjectIdentity
foreign_interface = _Foreign_interface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 8)
)


class _Fih_extra_pulses_feature_Type(Integer32):
    """Custom type fih_extra_pulses_feature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eDisable", 1),
          ("eEnable", 2))
    )


_Fih_extra_pulses_feature_Type.__name__ = "Integer32"
_Fih_extra_pulses_feature_Object = MibScalar
fih_extra_pulses_feature = _Fih_extra_pulses_feature_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 8, 2),
    _Fih_extra_pulses_feature_Type()
)
fih_extra_pulses_feature.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fih_extra_pulses_feature.setStatus("optional")
_Usb_interface_ObjectIdentity = ObjectIdentity
usb_interface = _Usb_interface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 9)
)


class _Usb_host_supported_Type(Integer32):
    """Custom type usb_host_supported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eFalse", 1),
          ("eTrue", 2))
    )


_Usb_host_supported_Type.__name__ = "Integer32"
_Usb_host_supported_Object = MibScalar
usb_host_supported = _Usb_host_supported_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 9, 1),
    _Usb_host_supported_Type()
)
usb_host_supported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usb_host_supported.setStatus("optional")
_Usb_ObjectIdentity = ObjectIdentity
usb = _Usb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 9, 2)
)
_Usb_serial_number_Type = OctetString
_Usb_serial_number_Object = MibScalar
usb_serial_number = _Usb_serial_number_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 9, 2, 1),
    _Usb_serial_number_Type()
)
usb_serial_number.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usb_serial_number.setStatus("optional")
_Usb_manufacturer_name_Type = OctetString
_Usb_manufacturer_name_Object = MibScalar
usb_manufacturer_name = _Usb_manufacturer_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 9, 2, 2),
    _Usb_manufacturer_name_Type()
)
usb_manufacturer_name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usb_manufacturer_name.setStatus("optional")
_Usb_product_description_Type = OctetString
_Usb_product_description_Object = MibScalar
usb_product_description = _Usb_product_description_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 9, 2, 3),
    _Usb_product_description_Type()
)
usb_product_description.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usb_product_description.setStatus("optional")
_Usb_vendor_id_Type = Integer32
_Usb_vendor_id_Object = MibScalar
usb_vendor_id = _Usb_vendor_id_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 9, 2, 4),
    _Usb_vendor_id_Type()
)
usb_vendor_id.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usb_vendor_id.setStatus("optional")
_Usb_product_id_Type = Integer32
_Usb_product_id_Object = MibScalar
usb_product_id = _Usb_product_id_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 9, 2, 5),
    _Usb_product_id_Type()
)
usb_product_id.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usb_product_id.setStatus("optional")


class _Usb_device_kind_Type(Integer32):
    """Custom type usb_device_kind based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("eUSBCompositeDevice", 3),
          ("eUSBNonStorageDevice", 2),
          ("eUSBStorageDevice", 1),
          ("eUSBUnsupportedDevice", 4))
    )


_Usb_device_kind_Type.__name__ = "Integer32"
_Usb_device_kind_Object = MibScalar
usb_device_kind = _Usb_device_kind_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 9, 2, 6),
    _Usb_device_kind_Type()
)
usb_device_kind.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usb_device_kind.setStatus("optional")
_Usb_driver_name_Type = OctetString
_Usb_driver_name_Object = MibScalar
usb_driver_name = _Usb_driver_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 9, 2, 7),
    _Usb_driver_name_Type()
)
usb_driver_name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usb_driver_name.setStatus("optional")
_Job_ObjectIdentity = ObjectIdentity
job = _Job_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6)
)
_Settings_job_ObjectIdentity = ObjectIdentity
settings_job = _Settings_job_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 1)
)


class _Clearable_warning_Type(Integer32):
    """Custom type clearable_warning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("eJob", 3),
          ("eOn", 2))
    )


_Clearable_warning_Type.__name__ = "Integer32"
_Clearable_warning_Object = MibScalar
clearable_warning = _Clearable_warning_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 1, 1),
    _Clearable_warning_Type()
)
clearable_warning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clearable_warning.setStatus("optional")


class _Cancel_job_Type(Integer32):
    """Custom type cancel_job based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 32767),
    )


_Cancel_job_Type.__name__ = "Integer32"
_Cancel_job_Object = MibScalar
cancel_job = _Cancel_job_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 1, 2),
    _Cancel_job_Type()
)
cancel_job.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    cancel_job.setStatus("optional")


class _Job_info_change_id_Type(OctetString):
    """Custom type job_info_change_id based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_Job_info_change_id_Type.__name__ = "OctetString"
_Job_info_change_id_Object = MibScalar
job_info_change_id = _Job_info_change_id_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 1, 3),
    _Job_info_change_id_Type()
)
job_info_change_id.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    job_info_change_id.setStatus("optional")
_Hold_job_timeout_Type = Integer32
_Hold_job_timeout_Object = MibScalar
hold_job_timeout = _Hold_job_timeout_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 1, 10),
    _Hold_job_timeout_Type()
)
hold_job_timeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hold_job_timeout.setStatus("optional")
_Active_print_jobs_ObjectIdentity = ObjectIdentity
active_print_jobs = _Active_print_jobs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 2)
)
_Job_being_parsed_ObjectIdentity = ObjectIdentity
job_being_parsed = _Job_being_parsed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 2, 1)
)


class _Current_job_parsing_id_Type(Integer32):
    """Custom type current_job_parsing_id based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_Current_job_parsing_id_Type.__name__ = "Integer32"
_Current_job_parsing_id_Object = MibScalar
current_job_parsing_id = _Current_job_parsing_id_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 2, 1, 1),
    _Current_job_parsing_id_Type()
)
current_job_parsing_id.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    current_job_parsing_id.setStatus("optional")
_Job_info_ObjectIdentity = ObjectIdentity
job_info = _Job_info_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 5)
)
_Job_info_name1_Type = OctetString
_Job_info_name1_Object = MibScalar
job_info_name1 = _Job_info_name1_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 5, 1),
    _Job_info_name1_Type()
)
job_info_name1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    job_info_name1.setStatus("optional")
_Job_info_name2_Type = OctetString
_Job_info_name2_Object = MibScalar
job_info_name2 = _Job_info_name2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 5, 2),
    _Job_info_name2_Type()
)
job_info_name2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    job_info_name2.setStatus("optional")
_Job_info_stage_Type = OctetString
_Job_info_stage_Object = MibScalar
job_info_stage = _Job_info_stage_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 5, 10),
    _Job_info_stage_Type()
)
job_info_stage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    job_info_stage.setStatus("optional")
_Job_info_io_source_Type = Integer32
_Job_info_io_source_Object = MibScalar
job_info_io_source = _Job_info_io_source_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 5, 11),
    _Job_info_io_source_Type()
)
job_info_io_source.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    job_info_io_source.setStatus("optional")
_Job_info_pages_processed_Type = Integer32
_Job_info_pages_processed_Object = MibScalar
job_info_pages_processed = _Job_info_pages_processed_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 5, 12),
    _Job_info_pages_processed_Type()
)
job_info_pages_processed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    job_info_pages_processed.setStatus("optional")
_Job_info_pages_printed_Type = Integer32
_Job_info_pages_printed_Object = MibScalar
job_info_pages_printed = _Job_info_pages_printed_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 5, 13),
    _Job_info_pages_printed_Type()
)
job_info_pages_printed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    job_info_pages_printed.setStatus("optional")
_Job_info_size_Type = Integer32
_Job_info_size_Object = MibScalar
job_info_size = _Job_info_size_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 5, 14),
    _Job_info_size_Type()
)
job_info_size.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    job_info_size.setStatus("optional")


class _Job_info_state_Type(Integer32):
    """Custom type job_info_state based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              5,
              7,
              10,
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("eAborted", 3),
          ("eCancelled", 10),
          ("ePrinted", 5),
          ("eProcessing", 11),
          ("eScanning", 12),
          ("eSending", 13),
          ("eTerminating", 7),
          ("eWaitingForResources", 4))
    )


_Job_info_state_Type.__name__ = "Integer32"
_Job_info_state_Object = MibScalar
job_info_state = _Job_info_state_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 5, 15),
    _Job_info_state_Type()
)
job_info_state.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    job_info_state.setStatus("optional")


class _Job_info_outcome_Type(Integer32):
    """Custom type job_info_outcome based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            3
        )
    )
    namedValues = NamedValues(
        ("eOk", 3)
    )


_Job_info_outcome_Type.__name__ = "Integer32"
_Job_info_outcome_Object = MibScalar
job_info_outcome = _Job_info_outcome_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 5, 19),
    _Job_info_outcome_Type()
)
job_info_outcome.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    job_info_outcome.setStatus("optional")
_Job_info_attribute_ObjectIdentity = ObjectIdentity
job_info_attribute = _Job_info_attribute_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 5, 23)
)


class _Job_info_attr_1_Type(OctetString):
    """Custom type job_info_attr_1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_Job_info_attr_1_Type.__name__ = "OctetString"
_Job_info_attr_1_Object = MibScalar
job_info_attr_1 = _Job_info_attr_1_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 5, 23, 1),
    _Job_info_attr_1_Type()
)
job_info_attr_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    job_info_attr_1.setStatus("optional")


class _Job_info_attr_2_Type(OctetString):
    """Custom type job_info_attr_2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_Job_info_attr_2_Type.__name__ = "OctetString"
_Job_info_attr_2_Object = MibScalar
job_info_attr_2 = _Job_info_attr_2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 5, 23, 2),
    _Job_info_attr_2_Type()
)
job_info_attr_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    job_info_attr_2.setStatus("optional")


class _Job_info_attr_3_Type(OctetString):
    """Custom type job_info_attr_3 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_Job_info_attr_3_Type.__name__ = "OctetString"
_Job_info_attr_3_Object = MibScalar
job_info_attr_3 = _Job_info_attr_3_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 5, 23, 3),
    _Job_info_attr_3_Type()
)
job_info_attr_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    job_info_attr_3.setStatus("optional")


class _Job_info_attr_4_Type(OctetString):
    """Custom type job_info_attr_4 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_Job_info_attr_4_Type.__name__ = "OctetString"
_Job_info_attr_4_Object = MibScalar
job_info_attr_4 = _Job_info_attr_4_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 5, 23, 4),
    _Job_info_attr_4_Type()
)
job_info_attr_4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    job_info_attr_4.setStatus("optional")


class _Job_info_attr_5_Type(OctetString):
    """Custom type job_info_attr_5 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_Job_info_attr_5_Type.__name__ = "OctetString"
_Job_info_attr_5_Object = MibScalar
job_info_attr_5 = _Job_info_attr_5_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 5, 23, 5),
    _Job_info_attr_5_Type()
)
job_info_attr_5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    job_info_attr_5.setStatus("optional")


class _Job_info_attr_6_Type(OctetString):
    """Custom type job_info_attr_6 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_Job_info_attr_6_Type.__name__ = "OctetString"
_Job_info_attr_6_Object = MibScalar
job_info_attr_6 = _Job_info_attr_6_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 5, 23, 6),
    _Job_info_attr_6_Type()
)
job_info_attr_6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    job_info_attr_6.setStatus("optional")


class _Job_info_attr_7_Type(OctetString):
    """Custom type job_info_attr_7 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_Job_info_attr_7_Type.__name__ = "OctetString"
_Job_info_attr_7_Object = MibScalar
job_info_attr_7 = _Job_info_attr_7_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 5, 23, 7),
    _Job_info_attr_7_Type()
)
job_info_attr_7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    job_info_attr_7.setStatus("optional")


class _Job_info_attr_8_Type(OctetString):
    """Custom type job_info_attr_8 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_Job_info_attr_8_Type.__name__ = "OctetString"
_Job_info_attr_8_Object = MibScalar
job_info_attr_8 = _Job_info_attr_8_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 5, 23, 8),
    _Job_info_attr_8_Type()
)
job_info_attr_8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    job_info_attr_8.setStatus("optional")


class _Job_info_attr_9_Type(OctetString):
    """Custom type job_info_attr_9 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_Job_info_attr_9_Type.__name__ = "OctetString"
_Job_info_attr_9_Object = MibScalar
job_info_attr_9 = _Job_info_attr_9_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 5, 23, 9),
    _Job_info_attr_9_Type()
)
job_info_attr_9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    job_info_attr_9.setStatus("optional")


class _Job_info_attr_10_Type(OctetString):
    """Custom type job_info_attr_10 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_Job_info_attr_10_Type.__name__ = "OctetString"
_Job_info_attr_10_Object = MibScalar
job_info_attr_10 = _Job_info_attr_10_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 5, 23, 10),
    _Job_info_attr_10_Type()
)
job_info_attr_10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    job_info_attr_10.setStatus("optional")


class _Job_info_attr_11_Type(OctetString):
    """Custom type job_info_attr_11 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_Job_info_attr_11_Type.__name__ = "OctetString"
_Job_info_attr_11_Object = MibScalar
job_info_attr_11 = _Job_info_attr_11_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 5, 23, 11),
    _Job_info_attr_11_Type()
)
job_info_attr_11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    job_info_attr_11.setStatus("optional")


class _Job_info_attr_12_Type(OctetString):
    """Custom type job_info_attr_12 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_Job_info_attr_12_Type.__name__ = "OctetString"
_Job_info_attr_12_Object = MibScalar
job_info_attr_12 = _Job_info_attr_12_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 5, 23, 12),
    _Job_info_attr_12_Type()
)
job_info_attr_12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    job_info_attr_12.setStatus("optional")


class _Job_info_attr_13_Type(OctetString):
    """Custom type job_info_attr_13 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_Job_info_attr_13_Type.__name__ = "OctetString"
_Job_info_attr_13_Object = MibScalar
job_info_attr_13 = _Job_info_attr_13_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 5, 23, 13),
    _Job_info_attr_13_Type()
)
job_info_attr_13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    job_info_attr_13.setStatus("optional")


class _Job_info_attr_14_Type(OctetString):
    """Custom type job_info_attr_14 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_Job_info_attr_14_Type.__name__ = "OctetString"
_Job_info_attr_14_Object = MibScalar
job_info_attr_14 = _Job_info_attr_14_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 5, 23, 14),
    _Job_info_attr_14_Type()
)
job_info_attr_14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    job_info_attr_14.setStatus("optional")


class _Job_info_attr_15_Type(OctetString):
    """Custom type job_info_attr_15 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_Job_info_attr_15_Type.__name__ = "OctetString"
_Job_info_attr_15_Object = MibScalar
job_info_attr_15 = _Job_info_attr_15_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 5, 23, 15),
    _Job_info_attr_15_Type()
)
job_info_attr_15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    job_info_attr_15.setStatus("optional")


class _Job_info_attr_16_Type(OctetString):
    """Custom type job_info_attr_16 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_Job_info_attr_16_Type.__name__ = "OctetString"
_Job_info_attr_16_Object = MibScalar
job_info_attr_16 = _Job_info_attr_16_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 5, 23, 16),
    _Job_info_attr_16_Type()
)
job_info_attr_16.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    job_info_attr_16.setStatus("optional")
_Job_info_accounting_ObjectIdentity = ObjectIdentity
job_info_accounting = _Job_info_accounting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 5, 28)
)


class _Job_info_accounting_media_size_Type(Integer32):
    """Custom type job_info_accounting_media_size based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              11,
              17,
              18,
              19,
              25,
              26,
              27,
              45,
              46,
              65,
              72,
              80,
              81,
              90,
              91,
              100,
              101,
              258,
              282,
              32767)
        )
    )
    namedValues = NamedValues(
        *(("eCommercial10", 81),
          ("eCustom", 101),
          ("eISOB5", 65),
          ("eISOandJISA3", 27),
          ("eISOandJISA4", 26),
          ("eISOandJISA4R", 282),
          ("eISOandJISA5", 25),
          ("eInternationalB5", 100),
          ("eInternationalC5", 91),
          ("eInternationalDL", 90),
          ("eJISB4", 46),
          ("eJISB5", 45),
          ("eJISExecutive", 18),
          ("eJapansePostcardDouble", 72),
          ("eLedger", 11),
          ("eMonarch", 80),
          ("eROC16K", 17),
          ("eROC8K", 19),
          ("eUSExecutive", 1),
          ("eUSLegal", 3),
          ("eUSLetter", 2),
          ("eUSLetterR", 258),
          ("eUnknownMediaSize", 32767))
    )


_Job_info_accounting_media_size_Type.__name__ = "Integer32"
_Job_info_accounting_media_size_Object = MibScalar
job_info_accounting_media_size = _Job_info_accounting_media_size_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 5, 28, 1),
    _Job_info_accounting_media_size_Type()
)
job_info_accounting_media_size.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    job_info_accounting_media_size.setStatus("optional")


class _Job_info_accounting_media_type_Type(Integer32):
    """Custom type job_info_accounting_media_type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              16,
              17,
              18,
              19,
              20,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54)
        )
    )
    namedValues = NamedValues(
        *(("eBond", 4),
          ("eCardStock", 11),
          ("eColored", 10),
          ("eCoverMatte", 52),
          ("eHPBrochMatte", 49),
          ("eHPCoverMatte", 50),
          ("eHPIJTrans", 45),
          ("eHPOfficePaper", 53),
          ("eHPOfficePaperEU", 54),
          ("eHPPremMatte", 48),
          ("eHPSnowman160", 46),
          ("eHPSnowman220", 47),
          ("eHeavy", 14),
          ("eLabels", 8),
          ("eLetterhead", 5),
          ("eMatte", 51),
          ("ePreprinted", 3),
          ("ePrepunched", 13),
          ("eRecycled", 9),
          ("eRough", 12),
          ("eStandardType", 2),
          ("eTransparency", 7),
          ("eUnknownMedia", 1),
          ("eUserType1", 16),
          ("eUserType2", 17),
          ("eUserType3", 18),
          ("eUserType4", 19),
          ("eUserType5", 20))
    )


_Job_info_accounting_media_type_Type.__name__ = "Integer32"
_Job_info_accounting_media_type_Object = MibScalar
job_info_accounting_media_type = _Job_info_accounting_media_type_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 5, 28, 2),
    _Job_info_accounting_media_type_Type()
)
job_info_accounting_media_type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    job_info_accounting_media_type.setStatus("optional")


class _Job_info_accounting_finishing_options_Type(Integer32):
    """Custom type job_info_accounting_finishing_options based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("eFinisher", 5),
          ("eNoFinish", 1),
          ("eOffset", 2),
          ("ePunch", 3),
          ("eStapler", 4))
    )


_Job_info_accounting_finishing_options_Type.__name__ = "Integer32"
_Job_info_accounting_finishing_options_Object = MibScalar
job_info_accounting_finishing_options = _Job_info_accounting_finishing_options_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 5, 28, 3),
    _Job_info_accounting_finishing_options_Type()
)
job_info_accounting_finishing_options.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    job_info_accounting_finishing_options.setStatus("optional")
_Job_info_accounting_media_simplex_count_Type = Integer32
_Job_info_accounting_media_simplex_count_Object = MibScalar
job_info_accounting_media_simplex_count = _Job_info_accounting_media_simplex_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 5, 28, 4),
    _Job_info_accounting_media_simplex_count_Type()
)
job_info_accounting_media_simplex_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    job_info_accounting_media_simplex_count.setStatus("optional")
_Job_info_accounting_media_duplex_count_Type = Integer32
_Job_info_accounting_media_duplex_count_Object = MibScalar
job_info_accounting_media_duplex_count = _Job_info_accounting_media_duplex_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 5, 28, 5),
    _Job_info_accounting_media_duplex_count_Type()
)
job_info_accounting_media_duplex_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    job_info_accounting_media_duplex_count.setStatus("optional")
_Job_info_accounting_grayscale_impression_count_Type = Integer32
_Job_info_accounting_grayscale_impression_count_Object = MibScalar
job_info_accounting_grayscale_impression_count = _Job_info_accounting_grayscale_impression_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 5, 28, 6),
    _Job_info_accounting_grayscale_impression_count_Type()
)
job_info_accounting_grayscale_impression_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    job_info_accounting_grayscale_impression_count.setStatus("optional")
_Job_info_accounting_color_impression_count_Type = Integer32
_Job_info_accounting_color_impression_count_Object = MibScalar
job_info_accounting_color_impression_count = _Job_info_accounting_color_impression_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 5, 28, 7),
    _Job_info_accounting_color_impression_count_Type()
)
job_info_accounting_color_impression_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    job_info_accounting_color_impression_count.setStatus("optional")
_Job_info_accounting_black_dots_Type = Integer32
_Job_info_accounting_black_dots_Object = MibScalar
job_info_accounting_black_dots = _Job_info_accounting_black_dots_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 5, 28, 8),
    _Job_info_accounting_black_dots_Type()
)
job_info_accounting_black_dots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    job_info_accounting_black_dots.setStatus("optional")
_Job_info_accounting_yellow_dots_Type = Integer32
_Job_info_accounting_yellow_dots_Object = MibScalar
job_info_accounting_yellow_dots = _Job_info_accounting_yellow_dots_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 5, 28, 9),
    _Job_info_accounting_yellow_dots_Type()
)
job_info_accounting_yellow_dots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    job_info_accounting_yellow_dots.setStatus("optional")
_Job_info_accounting_cyan_dots_Type = Integer32
_Job_info_accounting_cyan_dots_Object = MibScalar
job_info_accounting_cyan_dots = _Job_info_accounting_cyan_dots_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 5, 28, 10),
    _Job_info_accounting_cyan_dots_Type()
)
job_info_accounting_cyan_dots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    job_info_accounting_cyan_dots.setStatus("optional")
_Job_info_accounting_magenta_dots_Type = Integer32
_Job_info_accounting_magenta_dots_Object = MibScalar
job_info_accounting_magenta_dots = _Job_info_accounting_magenta_dots_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 5, 28, 11),
    _Job_info_accounting_magenta_dots_Type()
)
job_info_accounting_magenta_dots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    job_info_accounting_magenta_dots.setStatus("optional")


class _Job_info_accounting_job_type_Type(Integer32):
    """Custom type job_info_accounting_job_type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              1000)
        )
    )
    namedValues = NamedValues(
        *(("eAutoCleaningPage", 8),
          ("eCleaningPage", 7),
          ("eCopyInterruptJob", 4),
          ("eCopyJob", 3),
          ("eDigitalSendJob", 9),
          ("eFaxPrintJob", 11),
          ("eIPPJob", 2),
          ("eInternalPage", 6),
          ("eJetSendJob", 5),
          ("ePhotoCardPrintJob", 13),
          ("ePrintJob", 1),
          ("eRetrievedJob", 12),
          ("eUnknownJob", 1000),
          ("eWebPrintJob", 10))
    )


_Job_info_accounting_job_type_Type.__name__ = "Integer32"
_Job_info_accounting_job_type_Object = MibScalar
job_info_accounting_job_type = _Job_info_accounting_job_type_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 5, 28, 14),
    _Job_info_accounting_job_type_Type()
)
job_info_accounting_job_type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    job_info_accounting_job_type.setStatus("optional")
_Job_info_accounting_fixer_dots_Type = Integer32
_Job_info_accounting_fixer_dots_Object = MibScalar
job_info_accounting_fixer_dots = _Job_info_accounting_fixer_dots_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 5, 28, 33),
    _Job_info_accounting_fixer_dots_Type()
)
job_info_accounting_fixer_dots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    job_info_accounting_fixer_dots.setStatus("optional")
_Held_job_ObjectIdentity = ObjectIdentity
held_job = _Held_job_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 7)
)
_Held_job_info_ObjectIdentity = ObjectIdentity
held_job_info = _Held_job_info_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 7, 1)
)


class _Held_job_user_name_Type(OctetString):
    """Custom type held_job_user_name based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_Held_job_user_name_Type.__name__ = "OctetString"
_Held_job_user_name_Object = MibScalar
held_job_user_name = _Held_job_user_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 7, 1, 1),
    _Held_job_user_name_Type()
)
held_job_user_name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    held_job_user_name.setStatus("optional")


class _Held_job_job_name_Type(OctetString):
    """Custom type held_job_job_name based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_Held_job_job_name_Type.__name__ = "OctetString"
_Held_job_job_name_Object = MibScalar
held_job_job_name = _Held_job_job_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 7, 1, 2),
    _Held_job_job_name_Type()
)
held_job_job_name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    held_job_job_name.setStatus("optional")


class _Held_job_retention_Type(Integer32):
    """Custom type held_job_retention based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("eHoldOff", 1),
          ("eHoldOn", 2),
          ("eHoldProof", 4),
          ("eHoldStore", 3))
    )


_Held_job_retention_Type.__name__ = "Integer32"
_Held_job_retention_Object = MibScalar
held_job_retention = _Held_job_retention_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 7, 1, 3),
    _Held_job_retention_Type()
)
held_job_retention.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    held_job_retention.setStatus("optional")


class _Held_job_security_Type(Integer32):
    """Custom type held_job_security based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eHoldTypePrivate", 2),
          ("eHoldTypePublic", 1))
    )


_Held_job_security_Type.__name__ = "Integer32"
_Held_job_security_Object = MibScalar
held_job_security = _Held_job_security_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 7, 1, 4),
    _Held_job_security_Type()
)
held_job_security.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    held_job_security.setStatus("optional")


class _Held_job_quantity_Type(Integer32):
    """Custom type held_job_quantity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 999),
    )


_Held_job_quantity_Type.__name__ = "Integer32"
_Held_job_quantity_Object = MibScalar
held_job_quantity = _Held_job_quantity_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 7, 1, 5),
    _Held_job_quantity_Type()
)
held_job_quantity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    held_job_quantity.setStatus("optional")


class _Held_job_pin_Type(OctetString):
    """Custom type held_job_pin based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_Held_job_pin_Type.__name__ = "OctetString"
_Held_job_pin_Object = MibScalar
held_job_pin = _Held_job_pin_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 7, 1, 6),
    _Held_job_pin_Type()
)
held_job_pin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    held_job_pin.setStatus("optional")
_Held_job_control_ObjectIdentity = ObjectIdentity
held_job_control = _Held_job_control_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 7, 2)
)


class _Held_job_print_Type(OctetString):
    """Custom type held_job_print based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )


_Held_job_print_Type.__name__ = "OctetString"
_Held_job_print_Object = MibScalar
held_job_print = _Held_job_print_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 7, 2, 1),
    _Held_job_print_Type()
)
held_job_print.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    held_job_print.setStatus("optional")
_Held_job_delete_Type = Integer32
_Held_job_delete_Object = MibScalar
held_job_delete = _Held_job_delete_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 7, 2, 2),
    _Held_job_delete_Type()
)
held_job_delete.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    held_job_delete.setStatus("optional")


class _Held_job_set_queue_size_Type(Integer32):
    """Custom type held_job_set_queue_size based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Held_job_set_queue_size_Type.__name__ = "Integer32"
_Held_job_set_queue_size_Object = MibScalar
held_job_set_queue_size = _Held_job_set_queue_size_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 7, 2, 3),
    _Held_job_set_queue_size_Type()
)
held_job_set_queue_size.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    held_job_set_queue_size.setStatus("optional")


class _Held_job_enable_Type(Integer32):
    """Custom type held_job_enable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eDisabled", 1),
          ("eEnabled", 2))
    )


_Held_job_enable_Type.__name__ = "Integer32"
_Held_job_enable_Object = MibScalar
held_job_enable = _Held_job_enable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 7, 2, 4),
    _Held_job_enable_Type()
)
held_job_enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    held_job_enable.setStatus("optional")
_File_system_ObjectIdentity = ObjectIdentity
file_system = _File_system_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 10)
)
_Settings_file_system_ObjectIdentity = ObjectIdentity
settings_file_system = _Settings_file_system_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 10, 1)
)
_File_system_max_open_files_Type = Integer32
_File_system_max_open_files_Object = MibScalar
file_system_max_open_files = _File_system_max_open_files_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 10, 1, 2),
    _File_system_max_open_files_Type()
)
file_system_max_open_files.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    file_system_max_open_files.setStatus("optional")
_File_system_set_system_partition_writeable_Type = OctetString
_File_system_set_system_partition_writeable_Object = MibScalar
file_system_set_system_partition_writeable = _File_system_set_system_partition_writeable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 10, 1, 6),
    _File_system_set_system_partition_writeable_Type()
)
file_system_set_system_partition_writeable.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    file_system_set_system_partition_writeable.setStatus("optional")
_File_system_set_system_partition_readonly_Type = Integer32
_File_system_set_system_partition_readonly_Object = MibScalar
file_system_set_system_partition_readonly = _File_system_set_system_partition_readonly_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 10, 1, 7),
    _File_system_set_system_partition_readonly_Type()
)
file_system_set_system_partition_readonly.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    file_system_set_system_partition_readonly.setStatus("optional")
_File_system_delete_files_Type = OctetString
_File_system_delete_files_Object = MibScalar
file_system_delete_files = _File_system_delete_files_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 10, 1, 8),
    _File_system_delete_files_Type()
)
file_system_delete_files.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    file_system_delete_files.setStatus("optional")
_File_system_external_access_capabilities_Type = OctetString
_File_system_external_access_capabilities_Object = MibScalar
file_system_external_access_capabilities = _File_system_external_access_capabilities_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 10, 1, 10),
    _File_system_external_access_capabilities_Type()
)
file_system_external_access_capabilities.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    file_system_external_access_capabilities.setStatus("optional")
_File_system_erase_mode_Type = OctetString
_File_system_erase_mode_Object = MibScalar
file_system_erase_mode = _File_system_erase_mode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 10, 1, 11),
    _File_system_erase_mode_Type()
)
file_system_erase_mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    file_system_erase_mode.setStatus("optional")
_File_system_wipe_disk_Type = Integer32
_File_system_wipe_disk_Object = MibScalar
file_system_wipe_disk = _File_system_wipe_disk_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 10, 1, 12),
    _File_system_wipe_disk_Type()
)
file_system_wipe_disk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    file_system_wipe_disk.setStatus("optional")
_File_system_wipe_disk_status_Type = Integer32
_File_system_wipe_disk_status_Object = MibScalar
file_system_wipe_disk_status = _File_system_wipe_disk_status_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 10, 1, 13),
    _File_system_wipe_disk_status_Type()
)
file_system_wipe_disk_status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    file_system_wipe_disk_status.setStatus("optional")
_File_systems_ObjectIdentity = ObjectIdentity
file_systems = _File_systems_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 10, 3)
)
_File_system2_ObjectIdentity = ObjectIdentity
file_system2 = _File_system2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 10, 3, 2)
)


class _File_system2_initialize_volume_Type(Integer32):
    """Custom type file_system2_initialize_volume based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            2
        )
    )
    namedValues = NamedValues(
        ("eInitializing", 2)
    )


_File_system2_initialize_volume_Type.__name__ = "Integer32"
_File_system2_initialize_volume_Object = MibScalar
file_system2_initialize_volume = _File_system2_initialize_volume_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 10, 3, 2, 6),
    _File_system2_initialize_volume_Type()
)
file_system2_initialize_volume.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    file_system2_initialize_volume.setStatus("optional")
_File_system3_ObjectIdentity = ObjectIdentity
file_system3 = _File_system3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 10, 3, 3)
)


class _File_system3_initialize_volume_Type(Integer32):
    """Custom type file_system3_initialize_volume based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            2
        )
    )
    namedValues = NamedValues(
        ("eInitializing", 2)
    )


_File_system3_initialize_volume_Type.__name__ = "Integer32"
_File_system3_initialize_volume_Object = MibScalar
file_system3_initialize_volume = _File_system3_initialize_volume_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 10, 3, 3, 6),
    _File_system3_initialize_volume_Type()
)
file_system3_initialize_volume.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    file_system3_initialize_volume.setStatus("optional")
_File_system4_ObjectIdentity = ObjectIdentity
file_system4 = _File_system4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 10, 3, 4)
)


class _File_system4_initialize_volume_Type(Integer32):
    """Custom type file_system4_initialize_volume based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            2
        )
    )
    namedValues = NamedValues(
        ("eInitializing", 2)
    )


_File_system4_initialize_volume_Type.__name__ = "Integer32"
_File_system4_initialize_volume_Object = MibScalar
file_system4_initialize_volume = _File_system4_initialize_volume_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 10, 3, 4, 6),
    _File_system4_initialize_volume_Type()
)
file_system4_initialize_volume.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    file_system4_initialize_volume.setStatus("optional")
_Errorlog_ObjectIdentity = ObjectIdentity
errorlog = _Errorlog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11)
)
_Error1_ObjectIdentity = ObjectIdentity
error1 = _Error1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 1)
)
_Error1_time_stamp_Type = Integer32
_Error1_time_stamp_Object = MibScalar
error1_time_stamp = _Error1_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 1, 1),
    _Error1_time_stamp_Type()
)
error1_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error1_time_stamp.setStatus("optional")
_Error1_code_Type = Integer32
_Error1_code_Object = MibScalar
error1_code = _Error1_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 1, 2),
    _Error1_code_Type()
)
error1_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error1_code.setStatus("optional")
_Error1_date_time_Type = OctetString
_Error1_date_time_Object = MibScalar
error1_date_time = _Error1_date_time_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 1, 3),
    _Error1_date_time_Type()
)
error1_date_time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error1_date_time.setStatus("optional")
_Error2_ObjectIdentity = ObjectIdentity
error2 = _Error2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 2)
)
_Error2_time_stamp_Type = Integer32
_Error2_time_stamp_Object = MibScalar
error2_time_stamp = _Error2_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 2, 1),
    _Error2_time_stamp_Type()
)
error2_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error2_time_stamp.setStatus("optional")
_Error2_code_Type = Integer32
_Error2_code_Object = MibScalar
error2_code = _Error2_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 2, 2),
    _Error2_code_Type()
)
error2_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error2_code.setStatus("optional")
_Error2_date_time_Type = OctetString
_Error2_date_time_Object = MibScalar
error2_date_time = _Error2_date_time_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 2, 3),
    _Error2_date_time_Type()
)
error2_date_time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error2_date_time.setStatus("optional")
_Error3_ObjectIdentity = ObjectIdentity
error3 = _Error3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 3)
)
_Error3_time_stamp_Type = Integer32
_Error3_time_stamp_Object = MibScalar
error3_time_stamp = _Error3_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 3, 1),
    _Error3_time_stamp_Type()
)
error3_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error3_time_stamp.setStatus("optional")
_Error3_code_Type = Integer32
_Error3_code_Object = MibScalar
error3_code = _Error3_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 3, 2),
    _Error3_code_Type()
)
error3_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error3_code.setStatus("optional")
_Error3_date_time_Type = OctetString
_Error3_date_time_Object = MibScalar
error3_date_time = _Error3_date_time_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 3, 3),
    _Error3_date_time_Type()
)
error3_date_time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error3_date_time.setStatus("optional")
_Error4_ObjectIdentity = ObjectIdentity
error4 = _Error4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 4)
)
_Error4_time_stamp_Type = Integer32
_Error4_time_stamp_Object = MibScalar
error4_time_stamp = _Error4_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 4, 1),
    _Error4_time_stamp_Type()
)
error4_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error4_time_stamp.setStatus("optional")
_Error4_code_Type = Integer32
_Error4_code_Object = MibScalar
error4_code = _Error4_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 4, 2),
    _Error4_code_Type()
)
error4_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error4_code.setStatus("optional")
_Error4_date_time_Type = OctetString
_Error4_date_time_Object = MibScalar
error4_date_time = _Error4_date_time_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 4, 3),
    _Error4_date_time_Type()
)
error4_date_time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error4_date_time.setStatus("optional")
_Error5_ObjectIdentity = ObjectIdentity
error5 = _Error5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 5)
)
_Error5_time_stamp_Type = Integer32
_Error5_time_stamp_Object = MibScalar
error5_time_stamp = _Error5_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 5, 1),
    _Error5_time_stamp_Type()
)
error5_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error5_time_stamp.setStatus("optional")
_Error5_code_Type = Integer32
_Error5_code_Object = MibScalar
error5_code = _Error5_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 5, 2),
    _Error5_code_Type()
)
error5_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error5_code.setStatus("optional")
_Error5_date_time_Type = OctetString
_Error5_date_time_Object = MibScalar
error5_date_time = _Error5_date_time_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 5, 3),
    _Error5_date_time_Type()
)
error5_date_time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error5_date_time.setStatus("optional")
_Error6_ObjectIdentity = ObjectIdentity
error6 = _Error6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 6)
)
_Error6_time_stamp_Type = Integer32
_Error6_time_stamp_Object = MibScalar
error6_time_stamp = _Error6_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 6, 1),
    _Error6_time_stamp_Type()
)
error6_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error6_time_stamp.setStatus("optional")
_Error6_code_Type = Integer32
_Error6_code_Object = MibScalar
error6_code = _Error6_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 6, 2),
    _Error6_code_Type()
)
error6_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error6_code.setStatus("optional")
_Error6_date_time_Type = OctetString
_Error6_date_time_Object = MibScalar
error6_date_time = _Error6_date_time_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 6, 3),
    _Error6_date_time_Type()
)
error6_date_time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error6_date_time.setStatus("optional")
_Error7_ObjectIdentity = ObjectIdentity
error7 = _Error7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 7)
)
_Error7_time_stamp_Type = Integer32
_Error7_time_stamp_Object = MibScalar
error7_time_stamp = _Error7_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 7, 1),
    _Error7_time_stamp_Type()
)
error7_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error7_time_stamp.setStatus("optional")
_Error7_code_Type = Integer32
_Error7_code_Object = MibScalar
error7_code = _Error7_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 7, 2),
    _Error7_code_Type()
)
error7_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error7_code.setStatus("optional")
_Error7_date_time_Type = OctetString
_Error7_date_time_Object = MibScalar
error7_date_time = _Error7_date_time_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 7, 3),
    _Error7_date_time_Type()
)
error7_date_time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error7_date_time.setStatus("optional")
_Error8_ObjectIdentity = ObjectIdentity
error8 = _Error8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 8)
)
_Error8_time_stamp_Type = Integer32
_Error8_time_stamp_Object = MibScalar
error8_time_stamp = _Error8_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 8, 1),
    _Error8_time_stamp_Type()
)
error8_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error8_time_stamp.setStatus("optional")
_Error8_code_Type = Integer32
_Error8_code_Object = MibScalar
error8_code = _Error8_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 8, 2),
    _Error8_code_Type()
)
error8_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error8_code.setStatus("optional")
_Error8_date_time_Type = OctetString
_Error8_date_time_Object = MibScalar
error8_date_time = _Error8_date_time_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 8, 3),
    _Error8_date_time_Type()
)
error8_date_time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error8_date_time.setStatus("optional")
_Error9_ObjectIdentity = ObjectIdentity
error9 = _Error9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 9)
)
_Error9_time_stamp_Type = Integer32
_Error9_time_stamp_Object = MibScalar
error9_time_stamp = _Error9_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 9, 1),
    _Error9_time_stamp_Type()
)
error9_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error9_time_stamp.setStatus("optional")
_Error9_code_Type = Integer32
_Error9_code_Object = MibScalar
error9_code = _Error9_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 9, 2),
    _Error9_code_Type()
)
error9_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error9_code.setStatus("optional")
_Error9_date_time_Type = OctetString
_Error9_date_time_Object = MibScalar
error9_date_time = _Error9_date_time_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 9, 3),
    _Error9_date_time_Type()
)
error9_date_time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error9_date_time.setStatus("optional")
_Error10_ObjectIdentity = ObjectIdentity
error10 = _Error10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 10)
)
_Error10_time_stamp_Type = Integer32
_Error10_time_stamp_Object = MibScalar
error10_time_stamp = _Error10_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 10, 1),
    _Error10_time_stamp_Type()
)
error10_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error10_time_stamp.setStatus("optional")
_Error10_code_Type = Integer32
_Error10_code_Object = MibScalar
error10_code = _Error10_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 10, 2),
    _Error10_code_Type()
)
error10_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error10_code.setStatus("optional")
_Error10_date_time_Type = OctetString
_Error10_date_time_Object = MibScalar
error10_date_time = _Error10_date_time_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 10, 3),
    _Error10_date_time_Type()
)
error10_date_time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error10_date_time.setStatus("optional")
_Error11_ObjectIdentity = ObjectIdentity
error11 = _Error11_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 11)
)
_Error11_time_stamp_Type = Integer32
_Error11_time_stamp_Object = MibScalar
error11_time_stamp = _Error11_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 11, 1),
    _Error11_time_stamp_Type()
)
error11_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error11_time_stamp.setStatus("optional")
_Error11_code_Type = Integer32
_Error11_code_Object = MibScalar
error11_code = _Error11_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 11, 2),
    _Error11_code_Type()
)
error11_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error11_code.setStatus("optional")
_Error11_date_time_Type = OctetString
_Error11_date_time_Object = MibScalar
error11_date_time = _Error11_date_time_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 11, 3),
    _Error11_date_time_Type()
)
error11_date_time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error11_date_time.setStatus("optional")
_Error12_ObjectIdentity = ObjectIdentity
error12 = _Error12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 12)
)
_Error12_time_stamp_Type = Integer32
_Error12_time_stamp_Object = MibScalar
error12_time_stamp = _Error12_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 12, 1),
    _Error12_time_stamp_Type()
)
error12_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error12_time_stamp.setStatus("optional")
_Error12_code_Type = Integer32
_Error12_code_Object = MibScalar
error12_code = _Error12_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 12, 2),
    _Error12_code_Type()
)
error12_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error12_code.setStatus("optional")
_Error12_date_time_Type = OctetString
_Error12_date_time_Object = MibScalar
error12_date_time = _Error12_date_time_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 12, 3),
    _Error12_date_time_Type()
)
error12_date_time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error12_date_time.setStatus("optional")
_Error13_ObjectIdentity = ObjectIdentity
error13 = _Error13_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 13)
)
_Error13_time_stamp_Type = Integer32
_Error13_time_stamp_Object = MibScalar
error13_time_stamp = _Error13_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 13, 1),
    _Error13_time_stamp_Type()
)
error13_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error13_time_stamp.setStatus("optional")
_Error13_code_Type = Integer32
_Error13_code_Object = MibScalar
error13_code = _Error13_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 13, 2),
    _Error13_code_Type()
)
error13_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error13_code.setStatus("optional")
_Error13_date_time_Type = OctetString
_Error13_date_time_Object = MibScalar
error13_date_time = _Error13_date_time_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 13, 3),
    _Error13_date_time_Type()
)
error13_date_time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error13_date_time.setStatus("optional")
_Error14_ObjectIdentity = ObjectIdentity
error14 = _Error14_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 14)
)
_Error14_time_stamp_Type = Integer32
_Error14_time_stamp_Object = MibScalar
error14_time_stamp = _Error14_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 14, 1),
    _Error14_time_stamp_Type()
)
error14_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error14_time_stamp.setStatus("optional")
_Error14_code_Type = Integer32
_Error14_code_Object = MibScalar
error14_code = _Error14_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 14, 2),
    _Error14_code_Type()
)
error14_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error14_code.setStatus("optional")
_Error14_date_time_Type = OctetString
_Error14_date_time_Object = MibScalar
error14_date_time = _Error14_date_time_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 14, 3),
    _Error14_date_time_Type()
)
error14_date_time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error14_date_time.setStatus("optional")
_Error15_ObjectIdentity = ObjectIdentity
error15 = _Error15_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 15)
)
_Error15_time_stamp_Type = Integer32
_Error15_time_stamp_Object = MibScalar
error15_time_stamp = _Error15_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 15, 1),
    _Error15_time_stamp_Type()
)
error15_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error15_time_stamp.setStatus("optional")
_Error15_code_Type = Integer32
_Error15_code_Object = MibScalar
error15_code = _Error15_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 15, 2),
    _Error15_code_Type()
)
error15_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error15_code.setStatus("optional")
_Error15_date_time_Type = OctetString
_Error15_date_time_Object = MibScalar
error15_date_time = _Error15_date_time_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 15, 3),
    _Error15_date_time_Type()
)
error15_date_time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error15_date_time.setStatus("optional")
_Error16_ObjectIdentity = ObjectIdentity
error16 = _Error16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 16)
)
_Error16_time_stamp_Type = Integer32
_Error16_time_stamp_Object = MibScalar
error16_time_stamp = _Error16_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 16, 1),
    _Error16_time_stamp_Type()
)
error16_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error16_time_stamp.setStatus("optional")
_Error16_code_Type = Integer32
_Error16_code_Object = MibScalar
error16_code = _Error16_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 16, 2),
    _Error16_code_Type()
)
error16_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error16_code.setStatus("optional")
_Error16_date_time_Type = OctetString
_Error16_date_time_Object = MibScalar
error16_date_time = _Error16_date_time_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 16, 3),
    _Error16_date_time_Type()
)
error16_date_time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error16_date_time.setStatus("optional")
_Error17_ObjectIdentity = ObjectIdentity
error17 = _Error17_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 17)
)
_Error17_time_stamp_Type = Integer32
_Error17_time_stamp_Object = MibScalar
error17_time_stamp = _Error17_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 17, 1),
    _Error17_time_stamp_Type()
)
error17_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error17_time_stamp.setStatus("optional")
_Error17_code_Type = Integer32
_Error17_code_Object = MibScalar
error17_code = _Error17_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 17, 2),
    _Error17_code_Type()
)
error17_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error17_code.setStatus("optional")
_Error17_date_time_Type = OctetString
_Error17_date_time_Object = MibScalar
error17_date_time = _Error17_date_time_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 17, 3),
    _Error17_date_time_Type()
)
error17_date_time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error17_date_time.setStatus("optional")
_Error18_ObjectIdentity = ObjectIdentity
error18 = _Error18_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 18)
)
_Error18_time_stamp_Type = Integer32
_Error18_time_stamp_Object = MibScalar
error18_time_stamp = _Error18_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 18, 1),
    _Error18_time_stamp_Type()
)
error18_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error18_time_stamp.setStatus("optional")
_Error18_code_Type = Integer32
_Error18_code_Object = MibScalar
error18_code = _Error18_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 18, 2),
    _Error18_code_Type()
)
error18_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error18_code.setStatus("optional")
_Error18_date_time_Type = OctetString
_Error18_date_time_Object = MibScalar
error18_date_time = _Error18_date_time_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 18, 3),
    _Error18_date_time_Type()
)
error18_date_time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error18_date_time.setStatus("optional")
_Error19_ObjectIdentity = ObjectIdentity
error19 = _Error19_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 19)
)
_Error19_time_stamp_Type = Integer32
_Error19_time_stamp_Object = MibScalar
error19_time_stamp = _Error19_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 19, 1),
    _Error19_time_stamp_Type()
)
error19_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error19_time_stamp.setStatus("optional")
_Error19_code_Type = Integer32
_Error19_code_Object = MibScalar
error19_code = _Error19_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 19, 2),
    _Error19_code_Type()
)
error19_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error19_code.setStatus("optional")
_Error19_date_time_Type = OctetString
_Error19_date_time_Object = MibScalar
error19_date_time = _Error19_date_time_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 19, 3),
    _Error19_date_time_Type()
)
error19_date_time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error19_date_time.setStatus("optional")
_Error20_ObjectIdentity = ObjectIdentity
error20 = _Error20_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 20)
)
_Error20_time_stamp_Type = Integer32
_Error20_time_stamp_Object = MibScalar
error20_time_stamp = _Error20_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 20, 1),
    _Error20_time_stamp_Type()
)
error20_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error20_time_stamp.setStatus("optional")
_Error20_code_Type = Integer32
_Error20_code_Object = MibScalar
error20_code = _Error20_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 20, 2),
    _Error20_code_Type()
)
error20_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error20_code.setStatus("optional")
_Error20_date_time_Type = OctetString
_Error20_date_time_Object = MibScalar
error20_date_time = _Error20_date_time_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 20, 3),
    _Error20_date_time_Type()
)
error20_date_time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error20_date_time.setStatus("optional")
_Error21_ObjectIdentity = ObjectIdentity
error21 = _Error21_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 21)
)
_Error21_time_stamp_Type = Integer32
_Error21_time_stamp_Object = MibScalar
error21_time_stamp = _Error21_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 21, 1),
    _Error21_time_stamp_Type()
)
error21_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error21_time_stamp.setStatus("optional")
_Error21_code_Type = Integer32
_Error21_code_Object = MibScalar
error21_code = _Error21_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 21, 2),
    _Error21_code_Type()
)
error21_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error21_code.setStatus("optional")
_Error21_date_time_Type = OctetString
_Error21_date_time_Object = MibScalar
error21_date_time = _Error21_date_time_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 21, 3),
    _Error21_date_time_Type()
)
error21_date_time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error21_date_time.setStatus("optional")
_Error22_ObjectIdentity = ObjectIdentity
error22 = _Error22_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 22)
)
_Error22_time_stamp_Type = Integer32
_Error22_time_stamp_Object = MibScalar
error22_time_stamp = _Error22_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 22, 1),
    _Error22_time_stamp_Type()
)
error22_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error22_time_stamp.setStatus("optional")
_Error22_code_Type = Integer32
_Error22_code_Object = MibScalar
error22_code = _Error22_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 22, 2),
    _Error22_code_Type()
)
error22_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error22_code.setStatus("optional")
_Error22_date_time_Type = OctetString
_Error22_date_time_Object = MibScalar
error22_date_time = _Error22_date_time_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 22, 3),
    _Error22_date_time_Type()
)
error22_date_time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error22_date_time.setStatus("optional")
_Error23_ObjectIdentity = ObjectIdentity
error23 = _Error23_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 23)
)
_Error23_time_stamp_Type = Integer32
_Error23_time_stamp_Object = MibScalar
error23_time_stamp = _Error23_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 23, 1),
    _Error23_time_stamp_Type()
)
error23_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error23_time_stamp.setStatus("optional")
_Error23_code_Type = Integer32
_Error23_code_Object = MibScalar
error23_code = _Error23_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 23, 2),
    _Error23_code_Type()
)
error23_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error23_code.setStatus("optional")
_Error23_date_time_Type = OctetString
_Error23_date_time_Object = MibScalar
error23_date_time = _Error23_date_time_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 23, 3),
    _Error23_date_time_Type()
)
error23_date_time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error23_date_time.setStatus("optional")
_Error24_ObjectIdentity = ObjectIdentity
error24 = _Error24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 24)
)
_Error24_time_stamp_Type = Integer32
_Error24_time_stamp_Object = MibScalar
error24_time_stamp = _Error24_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 24, 1),
    _Error24_time_stamp_Type()
)
error24_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error24_time_stamp.setStatus("optional")
_Error24_code_Type = Integer32
_Error24_code_Object = MibScalar
error24_code = _Error24_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 24, 2),
    _Error24_code_Type()
)
error24_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error24_code.setStatus("optional")
_Error24_date_time_Type = OctetString
_Error24_date_time_Object = MibScalar
error24_date_time = _Error24_date_time_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 24, 3),
    _Error24_date_time_Type()
)
error24_date_time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error24_date_time.setStatus("optional")
_Error25_ObjectIdentity = ObjectIdentity
error25 = _Error25_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 25)
)
_Error25_time_stamp_Type = Integer32
_Error25_time_stamp_Object = MibScalar
error25_time_stamp = _Error25_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 25, 1),
    _Error25_time_stamp_Type()
)
error25_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error25_time_stamp.setStatus("optional")
_Error25_code_Type = Integer32
_Error25_code_Object = MibScalar
error25_code = _Error25_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 25, 2),
    _Error25_code_Type()
)
error25_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error25_code.setStatus("optional")
_Error25_date_time_Type = OctetString
_Error25_date_time_Object = MibScalar
error25_date_time = _Error25_date_time_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 25, 3),
    _Error25_date_time_Type()
)
error25_date_time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error25_date_time.setStatus("optional")
_Error26_ObjectIdentity = ObjectIdentity
error26 = _Error26_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 26)
)
_Error26_time_stamp_Type = Integer32
_Error26_time_stamp_Object = MibScalar
error26_time_stamp = _Error26_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 26, 1),
    _Error26_time_stamp_Type()
)
error26_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error26_time_stamp.setStatus("optional")
_Error26_code_Type = Integer32
_Error26_code_Object = MibScalar
error26_code = _Error26_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 26, 2),
    _Error26_code_Type()
)
error26_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error26_code.setStatus("optional")
_Error26_date_time_Type = OctetString
_Error26_date_time_Object = MibScalar
error26_date_time = _Error26_date_time_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 26, 3),
    _Error26_date_time_Type()
)
error26_date_time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error26_date_time.setStatus("optional")
_Error27_ObjectIdentity = ObjectIdentity
error27 = _Error27_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 27)
)
_Error27_time_stamp_Type = Integer32
_Error27_time_stamp_Object = MibScalar
error27_time_stamp = _Error27_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 27, 1),
    _Error27_time_stamp_Type()
)
error27_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error27_time_stamp.setStatus("optional")
_Error27_code_Type = Integer32
_Error27_code_Object = MibScalar
error27_code = _Error27_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 27, 2),
    _Error27_code_Type()
)
error27_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error27_code.setStatus("optional")
_Error27_date_time_Type = OctetString
_Error27_date_time_Object = MibScalar
error27_date_time = _Error27_date_time_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 27, 3),
    _Error27_date_time_Type()
)
error27_date_time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error27_date_time.setStatus("optional")
_Error28_ObjectIdentity = ObjectIdentity
error28 = _Error28_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 28)
)
_Error28_time_stamp_Type = Integer32
_Error28_time_stamp_Object = MibScalar
error28_time_stamp = _Error28_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 28, 1),
    _Error28_time_stamp_Type()
)
error28_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error28_time_stamp.setStatus("optional")
_Error28_code_Type = Integer32
_Error28_code_Object = MibScalar
error28_code = _Error28_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 28, 2),
    _Error28_code_Type()
)
error28_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error28_code.setStatus("optional")
_Error28_date_time_Type = OctetString
_Error28_date_time_Object = MibScalar
error28_date_time = _Error28_date_time_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 28, 3),
    _Error28_date_time_Type()
)
error28_date_time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error28_date_time.setStatus("optional")
_Error29_ObjectIdentity = ObjectIdentity
error29 = _Error29_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 29)
)
_Error29_time_stamp_Type = Integer32
_Error29_time_stamp_Object = MibScalar
error29_time_stamp = _Error29_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 29, 1),
    _Error29_time_stamp_Type()
)
error29_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error29_time_stamp.setStatus("optional")
_Error29_code_Type = Integer32
_Error29_code_Object = MibScalar
error29_code = _Error29_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 29, 2),
    _Error29_code_Type()
)
error29_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error29_code.setStatus("optional")
_Error29_date_time_Type = OctetString
_Error29_date_time_Object = MibScalar
error29_date_time = _Error29_date_time_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 29, 3),
    _Error29_date_time_Type()
)
error29_date_time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error29_date_time.setStatus("optional")
_Error30_ObjectIdentity = ObjectIdentity
error30 = _Error30_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 30)
)
_Error30_time_stamp_Type = Integer32
_Error30_time_stamp_Object = MibScalar
error30_time_stamp = _Error30_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 30, 1),
    _Error30_time_stamp_Type()
)
error30_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error30_time_stamp.setStatus("optional")
_Error30_code_Type = Integer32
_Error30_code_Object = MibScalar
error30_code = _Error30_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 30, 2),
    _Error30_code_Type()
)
error30_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error30_code.setStatus("optional")
_Error30_date_time_Type = OctetString
_Error30_date_time_Object = MibScalar
error30_date_time = _Error30_date_time_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 30, 3),
    _Error30_date_time_Type()
)
error30_date_time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error30_date_time.setStatus("optional")
_Error31_ObjectIdentity = ObjectIdentity
error31 = _Error31_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 31)
)
_Error31_time_stamp_Type = Integer32
_Error31_time_stamp_Object = MibScalar
error31_time_stamp = _Error31_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 31, 1),
    _Error31_time_stamp_Type()
)
error31_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error31_time_stamp.setStatus("optional")
_Error31_code_Type = Integer32
_Error31_code_Object = MibScalar
error31_code = _Error31_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 31, 2),
    _Error31_code_Type()
)
error31_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error31_code.setStatus("optional")
_Error31_date_time_Type = OctetString
_Error31_date_time_Object = MibScalar
error31_date_time = _Error31_date_time_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 31, 3),
    _Error31_date_time_Type()
)
error31_date_time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error31_date_time.setStatus("optional")
_Error32_ObjectIdentity = ObjectIdentity
error32 = _Error32_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 32)
)
_Error32_time_stamp_Type = Integer32
_Error32_time_stamp_Object = MibScalar
error32_time_stamp = _Error32_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 32, 1),
    _Error32_time_stamp_Type()
)
error32_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error32_time_stamp.setStatus("optional")
_Error32_code_Type = Integer32
_Error32_code_Object = MibScalar
error32_code = _Error32_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 32, 2),
    _Error32_code_Type()
)
error32_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error32_code.setStatus("optional")
_Error32_date_time_Type = OctetString
_Error32_date_time_Object = MibScalar
error32_date_time = _Error32_date_time_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 32, 3),
    _Error32_date_time_Type()
)
error32_date_time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error32_date_time.setStatus("optional")
_Error33_ObjectIdentity = ObjectIdentity
error33 = _Error33_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 33)
)
_Error33_time_stamp_Type = Integer32
_Error33_time_stamp_Object = MibScalar
error33_time_stamp = _Error33_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 33, 1),
    _Error33_time_stamp_Type()
)
error33_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error33_time_stamp.setStatus("optional")
_Error33_code_Type = Integer32
_Error33_code_Object = MibScalar
error33_code = _Error33_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 33, 2),
    _Error33_code_Type()
)
error33_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error33_code.setStatus("optional")
_Error33_date_time_Type = OctetString
_Error33_date_time_Object = MibScalar
error33_date_time = _Error33_date_time_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 33, 3),
    _Error33_date_time_Type()
)
error33_date_time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error33_date_time.setStatus("optional")
_Error34_ObjectIdentity = ObjectIdentity
error34 = _Error34_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 34)
)
_Error34_time_stamp_Type = Integer32
_Error34_time_stamp_Object = MibScalar
error34_time_stamp = _Error34_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 34, 1),
    _Error34_time_stamp_Type()
)
error34_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error34_time_stamp.setStatus("optional")
_Error34_code_Type = Integer32
_Error34_code_Object = MibScalar
error34_code = _Error34_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 34, 2),
    _Error34_code_Type()
)
error34_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error34_code.setStatus("optional")
_Error34_date_time_Type = OctetString
_Error34_date_time_Object = MibScalar
error34_date_time = _Error34_date_time_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 34, 3),
    _Error34_date_time_Type()
)
error34_date_time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error34_date_time.setStatus("optional")
_Error35_ObjectIdentity = ObjectIdentity
error35 = _Error35_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 35)
)
_Error35_time_stamp_Type = Integer32
_Error35_time_stamp_Object = MibScalar
error35_time_stamp = _Error35_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 35, 1),
    _Error35_time_stamp_Type()
)
error35_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error35_time_stamp.setStatus("optional")
_Error35_code_Type = Integer32
_Error35_code_Object = MibScalar
error35_code = _Error35_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 35, 2),
    _Error35_code_Type()
)
error35_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error35_code.setStatus("optional")
_Error35_date_time_Type = OctetString
_Error35_date_time_Object = MibScalar
error35_date_time = _Error35_date_time_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 35, 3),
    _Error35_date_time_Type()
)
error35_date_time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error35_date_time.setStatus("optional")
_Error36_ObjectIdentity = ObjectIdentity
error36 = _Error36_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 36)
)
_Error36_time_stamp_Type = Integer32
_Error36_time_stamp_Object = MibScalar
error36_time_stamp = _Error36_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 36, 1),
    _Error36_time_stamp_Type()
)
error36_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error36_time_stamp.setStatus("optional")
_Error36_code_Type = Integer32
_Error36_code_Object = MibScalar
error36_code = _Error36_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 36, 2),
    _Error36_code_Type()
)
error36_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error36_code.setStatus("optional")
_Error36_date_time_Type = OctetString
_Error36_date_time_Object = MibScalar
error36_date_time = _Error36_date_time_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 36, 3),
    _Error36_date_time_Type()
)
error36_date_time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error36_date_time.setStatus("optional")
_Error37_ObjectIdentity = ObjectIdentity
error37 = _Error37_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 37)
)
_Error37_time_stamp_Type = Integer32
_Error37_time_stamp_Object = MibScalar
error37_time_stamp = _Error37_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 37, 1),
    _Error37_time_stamp_Type()
)
error37_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error37_time_stamp.setStatus("optional")
_Error37_code_Type = Integer32
_Error37_code_Object = MibScalar
error37_code = _Error37_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 37, 2),
    _Error37_code_Type()
)
error37_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error37_code.setStatus("optional")
_Error37_date_time_Type = OctetString
_Error37_date_time_Object = MibScalar
error37_date_time = _Error37_date_time_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 37, 3),
    _Error37_date_time_Type()
)
error37_date_time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error37_date_time.setStatus("optional")
_Error38_ObjectIdentity = ObjectIdentity
error38 = _Error38_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 38)
)
_Error38_time_stamp_Type = Integer32
_Error38_time_stamp_Object = MibScalar
error38_time_stamp = _Error38_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 38, 1),
    _Error38_time_stamp_Type()
)
error38_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error38_time_stamp.setStatus("optional")
_Error38_code_Type = Integer32
_Error38_code_Object = MibScalar
error38_code = _Error38_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 38, 2),
    _Error38_code_Type()
)
error38_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error38_code.setStatus("optional")
_Error38_date_time_Type = OctetString
_Error38_date_time_Object = MibScalar
error38_date_time = _Error38_date_time_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 38, 3),
    _Error38_date_time_Type()
)
error38_date_time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error38_date_time.setStatus("optional")
_Error39_ObjectIdentity = ObjectIdentity
error39 = _Error39_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 39)
)
_Error39_time_stamp_Type = Integer32
_Error39_time_stamp_Object = MibScalar
error39_time_stamp = _Error39_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 39, 1),
    _Error39_time_stamp_Type()
)
error39_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error39_time_stamp.setStatus("optional")
_Error39_code_Type = Integer32
_Error39_code_Object = MibScalar
error39_code = _Error39_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 39, 2),
    _Error39_code_Type()
)
error39_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error39_code.setStatus("optional")
_Error39_date_time_Type = OctetString
_Error39_date_time_Object = MibScalar
error39_date_time = _Error39_date_time_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 39, 3),
    _Error39_date_time_Type()
)
error39_date_time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error39_date_time.setStatus("optional")
_Error40_ObjectIdentity = ObjectIdentity
error40 = _Error40_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 40)
)
_Error40_time_stamp_Type = Integer32
_Error40_time_stamp_Object = MibScalar
error40_time_stamp = _Error40_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 40, 1),
    _Error40_time_stamp_Type()
)
error40_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error40_time_stamp.setStatus("optional")
_Error40_code_Type = Integer32
_Error40_code_Object = MibScalar
error40_code = _Error40_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 40, 2),
    _Error40_code_Type()
)
error40_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error40_code.setStatus("optional")
_Error40_date_time_Type = OctetString
_Error40_date_time_Object = MibScalar
error40_date_time = _Error40_date_time_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 40, 3),
    _Error40_date_time_Type()
)
error40_date_time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error40_date_time.setStatus("optional")
_Error41_ObjectIdentity = ObjectIdentity
error41 = _Error41_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 41)
)
_Error41_time_stamp_Type = Integer32
_Error41_time_stamp_Object = MibScalar
error41_time_stamp = _Error41_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 41, 1),
    _Error41_time_stamp_Type()
)
error41_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error41_time_stamp.setStatus("optional")
_Error41_code_Type = Integer32
_Error41_code_Object = MibScalar
error41_code = _Error41_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 41, 2),
    _Error41_code_Type()
)
error41_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error41_code.setStatus("optional")
_Error41_date_time_Type = OctetString
_Error41_date_time_Object = MibScalar
error41_date_time = _Error41_date_time_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 41, 3),
    _Error41_date_time_Type()
)
error41_date_time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error41_date_time.setStatus("optional")
_Error42_ObjectIdentity = ObjectIdentity
error42 = _Error42_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 42)
)
_Error42_time_stamp_Type = Integer32
_Error42_time_stamp_Object = MibScalar
error42_time_stamp = _Error42_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 42, 1),
    _Error42_time_stamp_Type()
)
error42_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error42_time_stamp.setStatus("optional")
_Error42_code_Type = Integer32
_Error42_code_Object = MibScalar
error42_code = _Error42_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 42, 2),
    _Error42_code_Type()
)
error42_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error42_code.setStatus("optional")
_Error42_date_time_Type = OctetString
_Error42_date_time_Object = MibScalar
error42_date_time = _Error42_date_time_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 42, 3),
    _Error42_date_time_Type()
)
error42_date_time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error42_date_time.setStatus("optional")
_Error43_ObjectIdentity = ObjectIdentity
error43 = _Error43_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 43)
)
_Error43_time_stamp_Type = Integer32
_Error43_time_stamp_Object = MibScalar
error43_time_stamp = _Error43_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 43, 1),
    _Error43_time_stamp_Type()
)
error43_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error43_time_stamp.setStatus("optional")
_Error43_code_Type = Integer32
_Error43_code_Object = MibScalar
error43_code = _Error43_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 43, 2),
    _Error43_code_Type()
)
error43_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error43_code.setStatus("optional")
_Error43_date_time_Type = OctetString
_Error43_date_time_Object = MibScalar
error43_date_time = _Error43_date_time_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 43, 3),
    _Error43_date_time_Type()
)
error43_date_time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error43_date_time.setStatus("optional")
_Error44_ObjectIdentity = ObjectIdentity
error44 = _Error44_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 44)
)
_Error44_time_stamp_Type = Integer32
_Error44_time_stamp_Object = MibScalar
error44_time_stamp = _Error44_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 44, 1),
    _Error44_time_stamp_Type()
)
error44_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error44_time_stamp.setStatus("optional")
_Error44_code_Type = Integer32
_Error44_code_Object = MibScalar
error44_code = _Error44_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 44, 2),
    _Error44_code_Type()
)
error44_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error44_code.setStatus("optional")
_Error44_date_time_Type = OctetString
_Error44_date_time_Object = MibScalar
error44_date_time = _Error44_date_time_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 44, 3),
    _Error44_date_time_Type()
)
error44_date_time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error44_date_time.setStatus("optional")
_Error45_ObjectIdentity = ObjectIdentity
error45 = _Error45_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 45)
)
_Error45_time_stamp_Type = Integer32
_Error45_time_stamp_Object = MibScalar
error45_time_stamp = _Error45_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 45, 1),
    _Error45_time_stamp_Type()
)
error45_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error45_time_stamp.setStatus("optional")
_Error45_code_Type = Integer32
_Error45_code_Object = MibScalar
error45_code = _Error45_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 45, 2),
    _Error45_code_Type()
)
error45_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error45_code.setStatus("optional")
_Error45_date_time_Type = OctetString
_Error45_date_time_Object = MibScalar
error45_date_time = _Error45_date_time_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 45, 3),
    _Error45_date_time_Type()
)
error45_date_time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error45_date_time.setStatus("optional")
_Error46_ObjectIdentity = ObjectIdentity
error46 = _Error46_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 46)
)
_Error46_time_stamp_Type = Integer32
_Error46_time_stamp_Object = MibScalar
error46_time_stamp = _Error46_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 46, 1),
    _Error46_time_stamp_Type()
)
error46_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error46_time_stamp.setStatus("optional")
_Error46_code_Type = Integer32
_Error46_code_Object = MibScalar
error46_code = _Error46_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 46, 2),
    _Error46_code_Type()
)
error46_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error46_code.setStatus("optional")
_Error46_date_time_Type = OctetString
_Error46_date_time_Object = MibScalar
error46_date_time = _Error46_date_time_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 46, 3),
    _Error46_date_time_Type()
)
error46_date_time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error46_date_time.setStatus("optional")
_Error47_ObjectIdentity = ObjectIdentity
error47 = _Error47_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 47)
)
_Error47_time_stamp_Type = Integer32
_Error47_time_stamp_Object = MibScalar
error47_time_stamp = _Error47_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 47, 1),
    _Error47_time_stamp_Type()
)
error47_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error47_time_stamp.setStatus("optional")
_Error47_code_Type = Integer32
_Error47_code_Object = MibScalar
error47_code = _Error47_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 47, 2),
    _Error47_code_Type()
)
error47_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error47_code.setStatus("optional")
_Error47_date_time_Type = OctetString
_Error47_date_time_Object = MibScalar
error47_date_time = _Error47_date_time_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 47, 3),
    _Error47_date_time_Type()
)
error47_date_time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error47_date_time.setStatus("optional")
_Error48_ObjectIdentity = ObjectIdentity
error48 = _Error48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 48)
)
_Error48_time_stamp_Type = Integer32
_Error48_time_stamp_Object = MibScalar
error48_time_stamp = _Error48_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 48, 1),
    _Error48_time_stamp_Type()
)
error48_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error48_time_stamp.setStatus("optional")
_Error48_code_Type = Integer32
_Error48_code_Object = MibScalar
error48_code = _Error48_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 48, 2),
    _Error48_code_Type()
)
error48_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error48_code.setStatus("optional")
_Error48_date_time_Type = OctetString
_Error48_date_time_Object = MibScalar
error48_date_time = _Error48_date_time_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 48, 3),
    _Error48_date_time_Type()
)
error48_date_time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error48_date_time.setStatus("optional")
_Error49_ObjectIdentity = ObjectIdentity
error49 = _Error49_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 49)
)
_Error49_time_stamp_Type = Integer32
_Error49_time_stamp_Object = MibScalar
error49_time_stamp = _Error49_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 49, 1),
    _Error49_time_stamp_Type()
)
error49_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error49_time_stamp.setStatus("optional")
_Error49_code_Type = Integer32
_Error49_code_Object = MibScalar
error49_code = _Error49_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 49, 2),
    _Error49_code_Type()
)
error49_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error49_code.setStatus("optional")
_Error49_date_time_Type = OctetString
_Error49_date_time_Object = MibScalar
error49_date_time = _Error49_date_time_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 49, 3),
    _Error49_date_time_Type()
)
error49_date_time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error49_date_time.setStatus("optional")
_Error50_ObjectIdentity = ObjectIdentity
error50 = _Error50_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 50)
)
_Error50_time_stamp_Type = Integer32
_Error50_time_stamp_Object = MibScalar
error50_time_stamp = _Error50_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 50, 1),
    _Error50_time_stamp_Type()
)
error50_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error50_time_stamp.setStatus("optional")
_Error50_code_Type = Integer32
_Error50_code_Object = MibScalar
error50_code = _Error50_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 50, 2),
    _Error50_code_Type()
)
error50_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error50_code.setStatus("optional")
_Error50_date_time_Type = OctetString
_Error50_date_time_Object = MibScalar
error50_date_time = _Error50_date_time_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 50, 3),
    _Error50_date_time_Type()
)
error50_date_time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error50_date_time.setStatus("optional")
_Resource_manager_ObjectIdentity = ObjectIdentity
resource_manager = _Resource_manager_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 12)
)
_Mass_storage_resources_ObjectIdentity = ObjectIdentity
mass_storage_resources = _Mass_storage_resources_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 12, 3)
)
_Mass_storage_resource_change_counter_Type = Integer32
_Mass_storage_resource_change_counter_Object = MibScalar
mass_storage_resource_change_counter = _Mass_storage_resource_change_counter_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 12, 3, 1),
    _Mass_storage_resource_change_counter_Type()
)
mass_storage_resource_change_counter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mass_storage_resource_change_counter.setStatus("optional")


class _Mass_storage_resource_changed_Type(Integer32):
    """Custom type mass_storage_resource_changed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            2
        )
    )
    namedValues = NamedValues(
        ("eTrue", 2)
    )


_Mass_storage_resource_changed_Type.__name__ = "Integer32"
_Mass_storage_resource_changed_Object = MibScalar
mass_storage_resource_changed = _Mass_storage_resource_changed_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 12, 3, 2),
    _Mass_storage_resource_changed_Type()
)
mass_storage_resource_changed.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mass_storage_resource_changed.setStatus("optional")
_Remote_procedure_call_ObjectIdentity = ObjectIdentity
remote_procedure_call = _Remote_procedure_call_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 13)
)
_Settings_rpc_ObjectIdentity = ObjectIdentity
settings_rpc = _Settings_rpc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 13, 1)
)
_Rpc_bind_protocol_address_Type = OctetString
_Rpc_bind_protocol_address_Object = MibScalar
rpc_bind_protocol_address = _Rpc_bind_protocol_address_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 13, 1, 2),
    _Rpc_bind_protocol_address_Type()
)
rpc_bind_protocol_address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpc_bind_protocol_address.setStatus("optional")
_Status_rpc_ObjectIdentity = ObjectIdentity
status_rpc = _Status_rpc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 13, 2)
)
_Rpc_bound_protocol_address_Type = OctetString
_Rpc_bound_protocol_address_Object = MibScalar
rpc_bound_protocol_address = _Rpc_bound_protocol_address_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 13, 2, 3),
    _Rpc_bound_protocol_address_Type()
)
rpc_bound_protocol_address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpc_bound_protocol_address.setStatus("optional")
_Mass_storage_block_driver_ObjectIdentity = ObjectIdentity
mass_storage_block_driver = _Mass_storage_block_driver_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 15)
)
_Settings_mass_storage_bd_ObjectIdentity = ObjectIdentity
settings_mass_storage_bd = _Settings_mass_storage_bd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 15, 1)
)


class _Ram_disk_mode_Type(Integer32):
    """Custom type ram_disk_mode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("eAuto", 3),
          ("eOff", 1))
    )


_Ram_disk_mode_Type.__name__ = "Integer32"
_Ram_disk_mode_Object = MibScalar
ram_disk_mode = _Ram_disk_mode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 15, 1, 1),
    _Ram_disk_mode_Type()
)
ram_disk_mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ram_disk_mode.setStatus("optional")
_Ram_disk_size_Type = Integer32
_Ram_disk_size_Object = MibScalar
ram_disk_size = _Ram_disk_size_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 15, 1, 2),
    _Ram_disk_size_Type()
)
ram_disk_size.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ram_disk_size.setStatus("optional")
_Status_mass_storage_bd_ObjectIdentity = ObjectIdentity
status_mass_storage_bd = _Status_mass_storage_bd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 15, 2)
)
_Maximum_ram_disk_memory_Type = Integer32
_Maximum_ram_disk_memory_Object = MibScalar
maximum_ram_disk_memory = _Maximum_ram_disk_memory_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 15, 2, 1),
    _Maximum_ram_disk_memory_Type()
)
maximum_ram_disk_memory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maximum_ram_disk_memory.setStatus("optional")
_Accounting_ObjectIdentity = ObjectIdentity
accounting = _Accounting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 16)
)
_Printer_accounting_ObjectIdentity = ObjectIdentity
printer_accounting = _Printer_accounting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 16, 1)
)
_Printed_media_usage_ObjectIdentity = ObjectIdentity
printed_media_usage = _Printed_media_usage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 16, 1, 1)
)


class _Printed_media_simplex_count_Type(Integer32):
    """Custom type printed_media_simplex_count based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 930576247),
    )


_Printed_media_simplex_count_Type.__name__ = "Integer32"
_Printed_media_simplex_count_Object = MibScalar
printed_media_simplex_count = _Printed_media_simplex_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 16, 1, 1, 1),
    _Printed_media_simplex_count_Type()
)
printed_media_simplex_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    printed_media_simplex_count.setStatus("optional")
_Printed_media_simplex_charge_Type = OctetString
_Printed_media_simplex_charge_Object = MibScalar
printed_media_simplex_charge = _Printed_media_simplex_charge_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 16, 1, 1, 2),
    _Printed_media_simplex_charge_Type()
)
printed_media_simplex_charge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    printed_media_simplex_charge.setStatus("optional")


class _Printed_media_duplex_count_Type(Integer32):
    """Custom type printed_media_duplex_count based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 930576247),
    )


_Printed_media_duplex_count_Type.__name__ = "Integer32"
_Printed_media_duplex_count_Object = MibScalar
printed_media_duplex_count = _Printed_media_duplex_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 16, 1, 1, 3),
    _Printed_media_duplex_count_Type()
)
printed_media_duplex_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    printed_media_duplex_count.setStatus("optional")
_Printed_media_duplex_charge_Type = OctetString
_Printed_media_duplex_charge_Object = MibScalar
printed_media_duplex_charge = _Printed_media_duplex_charge_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 16, 1, 1, 4),
    _Printed_media_duplex_charge_Type()
)
printed_media_duplex_charge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    printed_media_duplex_charge.setStatus("optional")
_Printed_media_total_charge_Type = OctetString
_Printed_media_total_charge_Object = MibScalar
printed_media_total_charge = _Printed_media_total_charge_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 16, 1, 1, 5),
    _Printed_media_total_charge_Type()
)
printed_media_total_charge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    printed_media_total_charge.setStatus("optional")
_Printed_media_maximum_pixels_per_page_Type = Integer32
_Printed_media_maximum_pixels_per_page_Object = MibScalar
printed_media_maximum_pixels_per_page = _Printed_media_maximum_pixels_per_page_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 16, 1, 1, 6),
    _Printed_media_maximum_pixels_per_page_Type()
)
printed_media_maximum_pixels_per_page.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    printed_media_maximum_pixels_per_page.setStatus("optional")
_Printed_media_combined_total_Type = OctetString
_Printed_media_combined_total_Object = MibScalar
printed_media_combined_total = _Printed_media_combined_total_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 16, 1, 1, 7),
    _Printed_media_combined_total_Type()
)
printed_media_combined_total.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    printed_media_combined_total.setStatus("optional")


class _Printed_media_dimplex_count_Type(Integer32):
    """Custom type printed_media_dimplex_count based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 930576247),
    )


_Printed_media_dimplex_count_Type.__name__ = "Integer32"
_Printed_media_dimplex_count_Object = MibScalar
printed_media_dimplex_count = _Printed_media_dimplex_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 16, 1, 1, 10),
    _Printed_media_dimplex_count_Type()
)
printed_media_dimplex_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    printed_media_dimplex_count.setStatus("optional")
_Usage_printer_total_charge_Type = OctetString
_Usage_printer_total_charge_Object = MibScalar
usage_printer_total_charge = _Usage_printer_total_charge_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 16, 1, 2),
    _Usage_printer_total_charge_Type()
)
usage_printer_total_charge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usage_printer_total_charge.setStatus("optional")


class _Usage_staple_count_Type(Integer32):
    """Custom type usage_staple_count based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 930576247),
    )


_Usage_staple_count_Type.__name__ = "Integer32"
_Usage_staple_count_Object = MibScalar
usage_staple_count = _Usage_staple_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 16, 1, 4),
    _Usage_staple_count_Type()
)
usage_staple_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usage_staple_count.setStatus("optional")


class _Usage_instructions_line1_Type(OctetString):
    """Custom type usage_instructions_line1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_Usage_instructions_line1_Type.__name__ = "OctetString"
_Usage_instructions_line1_Object = MibScalar
usage_instructions_line1 = _Usage_instructions_line1_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 16, 1, 5),
    _Usage_instructions_line1_Type()
)
usage_instructions_line1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usage_instructions_line1.setStatus("optional")


class _Usage_instructions_line2_Type(OctetString):
    """Custom type usage_instructions_line2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_Usage_instructions_line2_Type.__name__ = "OctetString"
_Usage_instructions_line2_Object = MibScalar
usage_instructions_line2 = _Usage_instructions_line2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 16, 1, 6),
    _Usage_instructions_line2_Type()
)
usage_instructions_line2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usage_instructions_line2.setStatus("optional")


class _Usage_instructions_line3_Type(OctetString):
    """Custom type usage_instructions_line3 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_Usage_instructions_line3_Type.__name__ = "OctetString"
_Usage_instructions_line3_Object = MibScalar
usage_instructions_line3 = _Usage_instructions_line3_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 16, 1, 7),
    _Usage_instructions_line3_Type()
)
usage_instructions_line3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usage_instructions_line3.setStatus("optional")


class _Usage_instructions_line4_Type(OctetString):
    """Custom type usage_instructions_line4 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_Usage_instructions_line4_Type.__name__ = "OctetString"
_Usage_instructions_line4_Object = MibScalar
usage_instructions_line4 = _Usage_instructions_line4_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 16, 1, 8),
    _Usage_instructions_line4_Type()
)
usage_instructions_line4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usage_instructions_line4.setStatus("optional")
_Source_tray_usage_total_Type = Integer32
_Source_tray_usage_total_Object = MibScalar
source_tray_usage_total = _Source_tray_usage_total_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 16, 1, 10),
    _Source_tray_usage_total_Type()
)
source_tray_usage_total.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    source_tray_usage_total.setStatus("optional")
_Destination_bin_usage_total_Type = Integer32
_Destination_bin_usage_total_Object = MibScalar
destination_bin_usage_total = _Destination_bin_usage_total_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 16, 1, 11),
    _Destination_bin_usage_total_Type()
)
destination_bin_usage_total.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    destination_bin_usage_total.setStatus("optional")
_Usage_printer_mono_total_charge_Type = OctetString
_Usage_printer_mono_total_charge_Object = MibScalar
usage_printer_mono_total_charge = _Usage_printer_mono_total_charge_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 16, 1, 12),
    _Usage_printer_mono_total_charge_Type()
)
usage_printer_mono_total_charge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usage_printer_mono_total_charge.setStatus("optional")
_Usage_printer_color_total_charge_Type = OctetString
_Usage_printer_color_total_charge_Object = MibScalar
usage_printer_color_total_charge = _Usage_printer_color_total_charge_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 16, 1, 13),
    _Usage_printer_color_total_charge_Type()
)
usage_printer_color_total_charge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usage_printer_color_total_charge.setStatus("optional")
_Print_meter_usage_ObjectIdentity = ObjectIdentity
print_meter_usage = _Print_meter_usage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 16, 1, 14)
)


class _Print_meter_usage_threshold_Type(Integer32):
    """Custom type print_meter_usage_threshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10000, 350000),
    )


_Print_meter_usage_threshold_Type.__name__ = "Integer32"
_Print_meter_usage_threshold_Object = MibScalar
print_meter_usage_threshold = _Print_meter_usage_threshold_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 16, 1, 14, 2),
    _Print_meter_usage_threshold_Type()
)
print_meter_usage_threshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    print_meter_usage_threshold.setStatus("optional")


class _Print_meter_print_quality_Type(Integer32):
    """Custom type print_meter_print_quality based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ePrintQualityBest", 3),
          ("ePrintQualityGood", 2),
          ("ePrintQualityMono", 1))
    )


_Print_meter_print_quality_Type.__name__ = "Integer32"
_Print_meter_print_quality_Object = MibScalar
print_meter_print_quality = _Print_meter_print_quality_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 16, 1, 14, 3),
    _Print_meter_print_quality_Type()
)
print_meter_print_quality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    print_meter_print_quality.setStatus("optional")


class _Print_meter_simplex_count_Type(Integer32):
    """Custom type print_meter_simplex_count based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 930576247),
    )


_Print_meter_simplex_count_Type.__name__ = "Integer32"
_Print_meter_simplex_count_Object = MibScalar
print_meter_simplex_count = _Print_meter_simplex_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 16, 1, 14, 4),
    _Print_meter_simplex_count_Type()
)
print_meter_simplex_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    print_meter_simplex_count.setStatus("optional")


class _Print_meter_duplex_count_Type(Integer32):
    """Custom type print_meter_duplex_count based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 930576247),
    )


_Print_meter_duplex_count_Type.__name__ = "Integer32"
_Print_meter_duplex_count_Object = MibScalar
print_meter_duplex_count = _Print_meter_duplex_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 16, 1, 14, 5),
    _Print_meter_duplex_count_Type()
)
print_meter_duplex_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    print_meter_duplex_count.setStatus("optional")
_Print_meter_total_charge_Type = OctetString
_Print_meter_total_charge_Object = MibScalar
print_meter_total_charge = _Print_meter_total_charge_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 16, 1, 14, 6),
    _Print_meter_total_charge_Type()
)
print_meter_total_charge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    print_meter_total_charge.setStatus("optional")


class _Print_meter_dimplex_count_Type(Integer32):
    """Custom type print_meter_dimplex_count based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 930576247),
    )


_Print_meter_dimplex_count_Type.__name__ = "Integer32"
_Print_meter_dimplex_count_Object = MibScalar
print_meter_dimplex_count = _Print_meter_dimplex_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 16, 1, 14, 7),
    _Print_meter_dimplex_count_Type()
)
print_meter_dimplex_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    print_meter_dimplex_count.setStatus("optional")


class _Print_meter_simplex_total_Type(Integer32):
    """Custom type print_meter_simplex_total based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 930576247),
    )


_Print_meter_simplex_total_Type.__name__ = "Integer32"
_Print_meter_simplex_total_Object = MibScalar
print_meter_simplex_total = _Print_meter_simplex_total_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 16, 1, 14, 8),
    _Print_meter_simplex_total_Type()
)
print_meter_simplex_total.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    print_meter_simplex_total.setStatus("optional")


class _Print_meter_duplex_total_Type(Integer32):
    """Custom type print_meter_duplex_total based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 930576247),
    )


_Print_meter_duplex_total_Type.__name__ = "Integer32"
_Print_meter_duplex_total_Object = MibScalar
print_meter_duplex_total = _Print_meter_duplex_total_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 16, 1, 14, 9),
    _Print_meter_duplex_total_Type()
)
print_meter_duplex_total.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    print_meter_duplex_total.setStatus("optional")
_Print_meter_category_total_Type = OctetString
_Print_meter_category_total_Object = MibScalar
print_meter_category_total = _Print_meter_category_total_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 16, 1, 14, 10),
    _Print_meter_category_total_Type()
)
print_meter_category_total.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    print_meter_category_total.setStatus("optional")


class _Print_meter_dimplex_total_Type(Integer32):
    """Custom type print_meter_dimplex_total based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 930576247),
    )


_Print_meter_dimplex_total_Type.__name__ = "Integer32"
_Print_meter_dimplex_total_Object = MibScalar
print_meter_dimplex_total = _Print_meter_dimplex_total_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 16, 1, 14, 11),
    _Print_meter_dimplex_total_Type()
)
print_meter_dimplex_total.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    print_meter_dimplex_total.setStatus("optional")
_Usage_printer_mono_simplex_total_Type = Integer32
_Usage_printer_mono_simplex_total_Object = MibScalar
usage_printer_mono_simplex_total = _Usage_printer_mono_simplex_total_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 16, 1, 15),
    _Usage_printer_mono_simplex_total_Type()
)
usage_printer_mono_simplex_total.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usage_printer_mono_simplex_total.setStatus("optional")
_Usage_printer_mono_duplex_total_Type = Integer32
_Usage_printer_mono_duplex_total_Object = MibScalar
usage_printer_mono_duplex_total = _Usage_printer_mono_duplex_total_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 16, 1, 16),
    _Usage_printer_mono_duplex_total_Type()
)
usage_printer_mono_duplex_total.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usage_printer_mono_duplex_total.setStatus("optional")
_Usage_printer_mono_dimplex_total_Type = Integer32
_Usage_printer_mono_dimplex_total_Object = MibScalar
usage_printer_mono_dimplex_total = _Usage_printer_mono_dimplex_total_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 16, 1, 17),
    _Usage_printer_mono_dimplex_total_Type()
)
usage_printer_mono_dimplex_total.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usage_printer_mono_dimplex_total.setStatus("optional")
_Scanner_accounting_ObjectIdentity = ObjectIdentity
scanner_accounting = _Scanner_accounting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 16, 2)
)
_Scanned_media_usage_ObjectIdentity = ObjectIdentity
scanned_media_usage = _Scanned_media_usage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 16, 2, 1)
)
_Scanned_media_simplex_count_Type = Integer32
_Scanned_media_simplex_count_Object = MibScalar
scanned_media_simplex_count = _Scanned_media_simplex_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 16, 2, 1, 1),
    _Scanned_media_simplex_count_Type()
)
scanned_media_simplex_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scanned_media_simplex_count.setStatus("optional")
_Scanned_media_simplex_charge_Type = OctetString
_Scanned_media_simplex_charge_Object = MibScalar
scanned_media_simplex_charge = _Scanned_media_simplex_charge_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 16, 2, 1, 2),
    _Scanned_media_simplex_charge_Type()
)
scanned_media_simplex_charge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scanned_media_simplex_charge.setStatus("optional")


class _Scanned_media_duplex_count_Type(Integer32):
    """Custom type scanned_media_duplex_count based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 930576247),
    )


_Scanned_media_duplex_count_Type.__name__ = "Integer32"
_Scanned_media_duplex_count_Object = MibScalar
scanned_media_duplex_count = _Scanned_media_duplex_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 16, 2, 1, 3),
    _Scanned_media_duplex_count_Type()
)
scanned_media_duplex_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scanned_media_duplex_count.setStatus("optional")
_Scanned_media_duplex_charge_Type = OctetString
_Scanned_media_duplex_charge_Object = MibScalar
scanned_media_duplex_charge = _Scanned_media_duplex_charge_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 16, 2, 1, 4),
    _Scanned_media_duplex_charge_Type()
)
scanned_media_duplex_charge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scanned_media_duplex_charge.setStatus("optional")
_Scanned_media_total_charge_Type = OctetString
_Scanned_media_total_charge_Object = MibScalar
scanned_media_total_charge = _Scanned_media_total_charge_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 16, 2, 1, 5),
    _Scanned_media_total_charge_Type()
)
scanned_media_total_charge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scanned_media_total_charge.setStatus("optional")
_Usage_scanner_total_charge_Type = OctetString
_Usage_scanner_total_charge_Object = MibScalar
usage_scanner_total_charge = _Usage_scanner_total_charge_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 16, 2, 2),
    _Usage_scanner_total_charge_Type()
)
usage_scanner_total_charge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usage_scanner_total_charge.setStatus("optional")
_Printer_color_accounting_ObjectIdentity = ObjectIdentity
printer_color_accounting = _Printer_color_accounting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 16, 3)
)
_Printed_media_color_usage_ObjectIdentity = ObjectIdentity
printed_media_color_usage = _Printed_media_color_usage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 16, 3, 1)
)
_Printed_media_color_simplex_count_Type = Integer32
_Printed_media_color_simplex_count_Object = MibScalar
printed_media_color_simplex_count = _Printed_media_color_simplex_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 16, 3, 1, 1),
    _Printed_media_color_simplex_count_Type()
)
printed_media_color_simplex_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    printed_media_color_simplex_count.setStatus("optional")
_Printed_media_color_duplex_count_Type = Integer32
_Printed_media_color_duplex_count_Object = MibScalar
printed_media_color_duplex_count = _Printed_media_color_duplex_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 16, 3, 1, 3),
    _Printed_media_color_duplex_count_Type()
)
printed_media_color_duplex_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    printed_media_color_duplex_count.setStatus("optional")
_Printed_media_color_total_count_Type = OctetString
_Printed_media_color_total_count_Object = MibScalar
printed_media_color_total_count = _Printed_media_color_total_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 16, 3, 1, 5),
    _Printed_media_color_total_count_Type()
)
printed_media_color_total_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    printed_media_color_total_count.setStatus("optional")
_Printed_media_color_dimplex_count_Type = Integer32
_Printed_media_color_dimplex_count_Object = MibScalar
printed_media_color_dimplex_count = _Printed_media_color_dimplex_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 16, 3, 1, 6),
    _Printed_media_color_dimplex_count_Type()
)
printed_media_color_dimplex_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    printed_media_color_dimplex_count.setStatus("optional")
_Source_tray_accounting_ObjectIdentity = ObjectIdentity
source_tray_accounting = _Source_tray_accounting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 16, 5)
)
_Source_tray_usage_ObjectIdentity = ObjectIdentity
source_tray_usage = _Source_tray_usage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 16, 5, 1)
)
_Source_tray_usage_count_Type = Integer32
_Source_tray_usage_count_Object = MibScalar
source_tray_usage_count = _Source_tray_usage_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 16, 5, 1, 1),
    _Source_tray_usage_count_Type()
)
source_tray_usage_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    source_tray_usage_count.setStatus("optional")
_Destination_bin_accounting_ObjectIdentity = ObjectIdentity
destination_bin_accounting = _Destination_bin_accounting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 16, 6)
)
_Destination_bin_usage_ObjectIdentity = ObjectIdentity
destination_bin_usage = _Destination_bin_usage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 16, 6, 1)
)
_Destination_bin_usage_count_Type = Integer32
_Destination_bin_usage_count_Object = MibScalar
destination_bin_usage_count = _Destination_bin_usage_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 16, 6, 1, 1),
    _Destination_bin_usage_count_Type()
)
destination_bin_usage_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    destination_bin_usage_count.setStatus("optional")
_Firmware_download_ObjectIdentity = ObjectIdentity
firmware_download = _Firmware_download_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 18)
)


class _Firmware_download_write_status_supported_Type(Integer32):
    """Custom type firmware_download_write_status_supported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eFalse", 1),
          ("eTrue", 2))
    )


_Firmware_download_write_status_supported_Type.__name__ = "Integer32"
_Firmware_download_write_status_supported_Object = MibScalar
firmware_download_write_status_supported = _Firmware_download_write_status_supported_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 18, 1),
    _Firmware_download_write_status_supported_Type()
)
firmware_download_write_status_supported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firmware_download_write_status_supported.setStatus("optional")
_Firmware_download_write_time_Type = Integer32
_Firmware_download_write_time_Object = MibScalar
firmware_download_write_time = _Firmware_download_write_time_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 18, 2),
    _Firmware_download_write_time_Type()
)
firmware_download_write_time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firmware_download_write_time.setStatus("optional")
_Firmware_download_write_count_Type = Integer32
_Firmware_download_write_count_Object = MibScalar
firmware_download_write_count = _Firmware_download_write_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 18, 3),
    _Firmware_download_write_count_Type()
)
firmware_download_write_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firmware_download_write_count.setStatus("optional")


class _Firmware_download_current_state_Type(Integer32):
    """Custom type firmware_download_current_state based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("eCancelDownload", 10),
          ("eDownloadComplete", 8),
          ("eIdle", 1),
          ("eOKtoShutDown", 9),
          ("eReceivedImageError", 3),
          ("eReceivingImage", 2),
          ("eShuttingDown", 11),
          ("eVerifiedImageError", 5),
          ("eVerifyingImage", 4),
          ("eWritingImage", 6),
          ("eWritingImageError", 7))
    )


_Firmware_download_current_state_Type.__name__ = "Integer32"
_Firmware_download_current_state_Object = MibScalar
firmware_download_current_state = _Firmware_download_current_state_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 18, 4),
    _Firmware_download_current_state_Type()
)
firmware_download_current_state.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    firmware_download_current_state.setStatus("optional")
_Firmware_download_maximum_write_count_Type = Integer32
_Firmware_download_maximum_write_count_Object = MibScalar
firmware_download_maximum_write_count = _Firmware_download_maximum_write_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 18, 5),
    _Firmware_download_maximum_write_count_Type()
)
firmware_download_maximum_write_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firmware_download_maximum_write_count.setStatus("optional")
_Firmware_download_name_Type = OctetString
_Firmware_download_name_Object = MibScalar
firmware_download_name = _Firmware_download_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 18, 6),
    _Firmware_download_name_Type()
)
firmware_download_name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firmware_download_name.setStatus("mandatory")
_Firmware_download_version_Type = OctetString
_Firmware_download_version_Object = MibScalar
firmware_download_version = _Firmware_download_version_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 18, 7),
    _Firmware_download_version_Type()
)
firmware_download_version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firmware_download_version.setStatus("mandatory")
_Operating_system_ObjectIdentity = ObjectIdentity
operating_system = _Operating_system_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 19)
)
_Os_execute_file_Type = OctetString
_Os_execute_file_Object = MibScalar
os_execute_file = _Os_execute_file_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 19, 1),
    _Os_execute_file_Type()
)
os_execute_file.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    os_execute_file.setStatus("optional")
_Upgradable_devices_ObjectIdentity = ObjectIdentity
upgradable_devices = _Upgradable_devices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 20)
)


class _Upgradable_devices_write_status_supported_Type(Integer32):
    """Custom type upgradable_devices_write_status_supported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eFalse", 1),
          ("eTrue", 2))
    )


_Upgradable_devices_write_status_supported_Type.__name__ = "Integer32"
_Upgradable_devices_write_status_supported_Object = MibScalar
upgradable_devices_write_status_supported = _Upgradable_devices_write_status_supported_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 20, 1),
    _Upgradable_devices_write_status_supported_Type()
)
upgradable_devices_write_status_supported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upgradable_devices_write_status_supported.setStatus("optional")
_Upgradable_devices_write_time_Type = Integer32
_Upgradable_devices_write_time_Object = MibScalar
upgradable_devices_write_time = _Upgradable_devices_write_time_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 20, 2),
    _Upgradable_devices_write_time_Type()
)
upgradable_devices_write_time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upgradable_devices_write_time.setStatus("optional")
_Upgradable_devices_write_count_Type = Integer32
_Upgradable_devices_write_count_Object = MibScalar
upgradable_devices_write_count = _Upgradable_devices_write_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 20, 3),
    _Upgradable_devices_write_count_Type()
)
upgradable_devices_write_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upgradable_devices_write_count.setStatus("optional")


class _Upgradable_devices_current_state_Type(Integer32):
    """Custom type upgradable_devices_current_state based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("eIdle", 1),
          ("eReceivedImage", 2),
          ("eReceivedImageError", 3),
          ("eUpgradeComplete", 8),
          ("eUpgradeSkipped", 9),
          ("eVerifiedImage", 4),
          ("eVerifiedImageError", 5),
          ("eWritingImage", 6),
          ("eWritingImageError", 7))
    )


_Upgradable_devices_current_state_Type.__name__ = "Integer32"
_Upgradable_devices_current_state_Object = MibScalar
upgradable_devices_current_state = _Upgradable_devices_current_state_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 20, 4),
    _Upgradable_devices_current_state_Type()
)
upgradable_devices_current_state.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upgradable_devices_current_state.setStatus("optional")
_Upgradable_devices_max_write_count_Type = Integer32
_Upgradable_devices_max_write_count_Object = MibScalar
upgradable_devices_max_write_count = _Upgradable_devices_max_write_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 20, 5),
    _Upgradable_devices_max_write_count_Type()
)
upgradable_devices_max_write_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upgradable_devices_max_write_count.setStatus("optional")
_Upgradable_devices_name_Type = OctetString
_Upgradable_devices_name_Object = MibScalar
upgradable_devices_name = _Upgradable_devices_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 20, 6),
    _Upgradable_devices_name_Type()
)
upgradable_devices_name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upgradable_devices_name.setStatus("mandatory")
_Upgradable_devices_version_Type = OctetString
_Upgradable_devices_version_Object = MibScalar
upgradable_devices_version = _Upgradable_devices_version_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 20, 7),
    _Upgradable_devices_version_Type()
)
upgradable_devices_version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upgradable_devices_version.setStatus("mandatory")


class _Remote_upgrade_enable_Type(Integer32):
    """Custom type remote_upgrade_enable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eOff", 1),
          ("eOn", 2))
    )


_Remote_upgrade_enable_Type.__name__ = "Integer32"
_Remote_upgrade_enable_Object = MibScalar
remote_upgrade_enable = _Remote_upgrade_enable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 20, 8),
    _Remote_upgrade_enable_Type()
)
remote_upgrade_enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remote_upgrade_enable.setStatus("mandatory")
_Warninglog_ObjectIdentity = ObjectIdentity
warninglog = _Warninglog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22)
)
_Warning1_ObjectIdentity = ObjectIdentity
warning1 = _Warning1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 1)
)
_Warning1_time_stamp_Type = Integer32
_Warning1_time_stamp_Object = MibScalar
warning1_time_stamp = _Warning1_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 1, 1),
    _Warning1_time_stamp_Type()
)
warning1_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning1_time_stamp.setStatus("optional")
_Warning1_code_Type = Integer32
_Warning1_code_Object = MibScalar
warning1_code = _Warning1_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 1, 2),
    _Warning1_code_Type()
)
warning1_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning1_code.setStatus("optional")
_Warning1_date_time_Type = OctetString
_Warning1_date_time_Object = MibScalar
warning1_date_time = _Warning1_date_time_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 1, 3),
    _Warning1_date_time_Type()
)
warning1_date_time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning1_date_time.setStatus("optional")
_Warning2_ObjectIdentity = ObjectIdentity
warning2 = _Warning2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 2)
)
_Warning2_time_stamp_Type = Integer32
_Warning2_time_stamp_Object = MibScalar
warning2_time_stamp = _Warning2_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 2, 1),
    _Warning2_time_stamp_Type()
)
warning2_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning2_time_stamp.setStatus("optional")
_Warning2_code_Type = Integer32
_Warning2_code_Object = MibScalar
warning2_code = _Warning2_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 2, 2),
    _Warning2_code_Type()
)
warning2_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning2_code.setStatus("optional")
_Warning2_date_time_Type = OctetString
_Warning2_date_time_Object = MibScalar
warning2_date_time = _Warning2_date_time_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 2, 3),
    _Warning2_date_time_Type()
)
warning2_date_time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning2_date_time.setStatus("optional")
_Warning3_ObjectIdentity = ObjectIdentity
warning3 = _Warning3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 3)
)
_Warning3_time_stamp_Type = Integer32
_Warning3_time_stamp_Object = MibScalar
warning3_time_stamp = _Warning3_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 3, 1),
    _Warning3_time_stamp_Type()
)
warning3_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning3_time_stamp.setStatus("optional")
_Warning3_code_Type = Integer32
_Warning3_code_Object = MibScalar
warning3_code = _Warning3_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 3, 2),
    _Warning3_code_Type()
)
warning3_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning3_code.setStatus("optional")
_Warning3_date_time_Type = OctetString
_Warning3_date_time_Object = MibScalar
warning3_date_time = _Warning3_date_time_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 3, 3),
    _Warning3_date_time_Type()
)
warning3_date_time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning3_date_time.setStatus("optional")
_Warning4_ObjectIdentity = ObjectIdentity
warning4 = _Warning4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 4)
)
_Warning4_time_stamp_Type = Integer32
_Warning4_time_stamp_Object = MibScalar
warning4_time_stamp = _Warning4_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 4, 1),
    _Warning4_time_stamp_Type()
)
warning4_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning4_time_stamp.setStatus("optional")
_Warning4_code_Type = Integer32
_Warning4_code_Object = MibScalar
warning4_code = _Warning4_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 4, 2),
    _Warning4_code_Type()
)
warning4_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning4_code.setStatus("optional")
_Warning4_date_time_Type = OctetString
_Warning4_date_time_Object = MibScalar
warning4_date_time = _Warning4_date_time_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 4, 3),
    _Warning4_date_time_Type()
)
warning4_date_time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning4_date_time.setStatus("optional")
_Warning5_ObjectIdentity = ObjectIdentity
warning5 = _Warning5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 5)
)
_Warning5_time_stamp_Type = Integer32
_Warning5_time_stamp_Object = MibScalar
warning5_time_stamp = _Warning5_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 5, 1),
    _Warning5_time_stamp_Type()
)
warning5_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning5_time_stamp.setStatus("optional")
_Warning5_code_Type = Integer32
_Warning5_code_Object = MibScalar
warning5_code = _Warning5_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 5, 2),
    _Warning5_code_Type()
)
warning5_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning5_code.setStatus("optional")
_Warning5_date_time_Type = OctetString
_Warning5_date_time_Object = MibScalar
warning5_date_time = _Warning5_date_time_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 5, 3),
    _Warning5_date_time_Type()
)
warning5_date_time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning5_date_time.setStatus("optional")
_Warning6_ObjectIdentity = ObjectIdentity
warning6 = _Warning6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 6)
)
_Warning6_time_stamp_Type = Integer32
_Warning6_time_stamp_Object = MibScalar
warning6_time_stamp = _Warning6_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 6, 1),
    _Warning6_time_stamp_Type()
)
warning6_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning6_time_stamp.setStatus("optional")
_Warning6_code_Type = Integer32
_Warning6_code_Object = MibScalar
warning6_code = _Warning6_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 6, 2),
    _Warning6_code_Type()
)
warning6_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning6_code.setStatus("optional")
_Warning6_date_time_Type = OctetString
_Warning6_date_time_Object = MibScalar
warning6_date_time = _Warning6_date_time_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 6, 3),
    _Warning6_date_time_Type()
)
warning6_date_time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning6_date_time.setStatus("optional")
_Warning7_ObjectIdentity = ObjectIdentity
warning7 = _Warning7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 7)
)
_Warning7_time_stamp_Type = Integer32
_Warning7_time_stamp_Object = MibScalar
warning7_time_stamp = _Warning7_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 7, 1),
    _Warning7_time_stamp_Type()
)
warning7_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning7_time_stamp.setStatus("optional")
_Warning7_code_Type = Integer32
_Warning7_code_Object = MibScalar
warning7_code = _Warning7_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 7, 2),
    _Warning7_code_Type()
)
warning7_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning7_code.setStatus("optional")
_Warning7_date_time_Type = OctetString
_Warning7_date_time_Object = MibScalar
warning7_date_time = _Warning7_date_time_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 7, 3),
    _Warning7_date_time_Type()
)
warning7_date_time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning7_date_time.setStatus("optional")
_Warning8_ObjectIdentity = ObjectIdentity
warning8 = _Warning8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 8)
)
_Warning8_time_stamp_Type = Integer32
_Warning8_time_stamp_Object = MibScalar
warning8_time_stamp = _Warning8_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 8, 1),
    _Warning8_time_stamp_Type()
)
warning8_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning8_time_stamp.setStatus("optional")
_Warning8_code_Type = Integer32
_Warning8_code_Object = MibScalar
warning8_code = _Warning8_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 8, 2),
    _Warning8_code_Type()
)
warning8_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning8_code.setStatus("optional")
_Warning8_date_time_Type = OctetString
_Warning8_date_time_Object = MibScalar
warning8_date_time = _Warning8_date_time_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 8, 3),
    _Warning8_date_time_Type()
)
warning8_date_time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning8_date_time.setStatus("optional")
_Warning9_ObjectIdentity = ObjectIdentity
warning9 = _Warning9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 9)
)
_Warning9_time_stamp_Type = Integer32
_Warning9_time_stamp_Object = MibScalar
warning9_time_stamp = _Warning9_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 9, 1),
    _Warning9_time_stamp_Type()
)
warning9_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning9_time_stamp.setStatus("optional")
_Warning9_code_Type = Integer32
_Warning9_code_Object = MibScalar
warning9_code = _Warning9_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 9, 2),
    _Warning9_code_Type()
)
warning9_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning9_code.setStatus("optional")
_Warning9_date_time_Type = OctetString
_Warning9_date_time_Object = MibScalar
warning9_date_time = _Warning9_date_time_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 9, 3),
    _Warning9_date_time_Type()
)
warning9_date_time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning9_date_time.setStatus("optional")
_Warning10_ObjectIdentity = ObjectIdentity
warning10 = _Warning10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 10)
)
_Warning10_time_stamp_Type = Integer32
_Warning10_time_stamp_Object = MibScalar
warning10_time_stamp = _Warning10_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 10, 1),
    _Warning10_time_stamp_Type()
)
warning10_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning10_time_stamp.setStatus("optional")
_Warning10_code_Type = Integer32
_Warning10_code_Object = MibScalar
warning10_code = _Warning10_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 10, 2),
    _Warning10_code_Type()
)
warning10_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning10_code.setStatus("optional")
_Warning10_date_time_Type = OctetString
_Warning10_date_time_Object = MibScalar
warning10_date_time = _Warning10_date_time_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 10, 3),
    _Warning10_date_time_Type()
)
warning10_date_time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning10_date_time.setStatus("optional")
_Warning11_ObjectIdentity = ObjectIdentity
warning11 = _Warning11_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 11)
)
_Warning11_time_stamp_Type = Integer32
_Warning11_time_stamp_Object = MibScalar
warning11_time_stamp = _Warning11_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 11, 1),
    _Warning11_time_stamp_Type()
)
warning11_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning11_time_stamp.setStatus("optional")
_Warning11_code_Type = Integer32
_Warning11_code_Object = MibScalar
warning11_code = _Warning11_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 11, 2),
    _Warning11_code_Type()
)
warning11_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning11_code.setStatus("optional")
_Warning11_date_time_Type = OctetString
_Warning11_date_time_Object = MibScalar
warning11_date_time = _Warning11_date_time_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 11, 3),
    _Warning11_date_time_Type()
)
warning11_date_time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning11_date_time.setStatus("optional")
_Warning12_ObjectIdentity = ObjectIdentity
warning12 = _Warning12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 12)
)
_Warning12_time_stamp_Type = Integer32
_Warning12_time_stamp_Object = MibScalar
warning12_time_stamp = _Warning12_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 12, 1),
    _Warning12_time_stamp_Type()
)
warning12_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning12_time_stamp.setStatus("optional")
_Warning12_code_Type = Integer32
_Warning12_code_Object = MibScalar
warning12_code = _Warning12_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 12, 2),
    _Warning12_code_Type()
)
warning12_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning12_code.setStatus("optional")
_Warning12_date_time_Type = OctetString
_Warning12_date_time_Object = MibScalar
warning12_date_time = _Warning12_date_time_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 12, 3),
    _Warning12_date_time_Type()
)
warning12_date_time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning12_date_time.setStatus("optional")
_Warning13_ObjectIdentity = ObjectIdentity
warning13 = _Warning13_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 13)
)
_Warning13_time_stamp_Type = Integer32
_Warning13_time_stamp_Object = MibScalar
warning13_time_stamp = _Warning13_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 13, 1),
    _Warning13_time_stamp_Type()
)
warning13_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning13_time_stamp.setStatus("optional")
_Warning13_code_Type = Integer32
_Warning13_code_Object = MibScalar
warning13_code = _Warning13_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 13, 2),
    _Warning13_code_Type()
)
warning13_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning13_code.setStatus("optional")
_Warning13_date_time_Type = OctetString
_Warning13_date_time_Object = MibScalar
warning13_date_time = _Warning13_date_time_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 13, 3),
    _Warning13_date_time_Type()
)
warning13_date_time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning13_date_time.setStatus("optional")
_Warning14_ObjectIdentity = ObjectIdentity
warning14 = _Warning14_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 14)
)
_Warning14_time_stamp_Type = Integer32
_Warning14_time_stamp_Object = MibScalar
warning14_time_stamp = _Warning14_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 14, 1),
    _Warning14_time_stamp_Type()
)
warning14_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning14_time_stamp.setStatus("optional")
_Warning14_code_Type = Integer32
_Warning14_code_Object = MibScalar
warning14_code = _Warning14_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 14, 2),
    _Warning14_code_Type()
)
warning14_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning14_code.setStatus("optional")
_Warning14_date_time_Type = OctetString
_Warning14_date_time_Object = MibScalar
warning14_date_time = _Warning14_date_time_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 14, 3),
    _Warning14_date_time_Type()
)
warning14_date_time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning14_date_time.setStatus("optional")
_Warning15_ObjectIdentity = ObjectIdentity
warning15 = _Warning15_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 15)
)
_Warning15_time_stamp_Type = Integer32
_Warning15_time_stamp_Object = MibScalar
warning15_time_stamp = _Warning15_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 15, 1),
    _Warning15_time_stamp_Type()
)
warning15_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning15_time_stamp.setStatus("optional")
_Warning15_code_Type = Integer32
_Warning15_code_Object = MibScalar
warning15_code = _Warning15_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 15, 2),
    _Warning15_code_Type()
)
warning15_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning15_code.setStatus("optional")
_Warning15_date_time_Type = OctetString
_Warning15_date_time_Object = MibScalar
warning15_date_time = _Warning15_date_time_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 15, 3),
    _Warning15_date_time_Type()
)
warning15_date_time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning15_date_time.setStatus("optional")
_Warning16_ObjectIdentity = ObjectIdentity
warning16 = _Warning16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 16)
)
_Warning16_time_stamp_Type = Integer32
_Warning16_time_stamp_Object = MibScalar
warning16_time_stamp = _Warning16_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 16, 1),
    _Warning16_time_stamp_Type()
)
warning16_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning16_time_stamp.setStatus("optional")
_Warning16_code_Type = Integer32
_Warning16_code_Object = MibScalar
warning16_code = _Warning16_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 16, 2),
    _Warning16_code_Type()
)
warning16_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning16_code.setStatus("optional")
_Warning16_date_time_Type = OctetString
_Warning16_date_time_Object = MibScalar
warning16_date_time = _Warning16_date_time_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 16, 3),
    _Warning16_date_time_Type()
)
warning16_date_time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning16_date_time.setStatus("optional")
_Warning17_ObjectIdentity = ObjectIdentity
warning17 = _Warning17_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 17)
)
_Warning17_time_stamp_Type = Integer32
_Warning17_time_stamp_Object = MibScalar
warning17_time_stamp = _Warning17_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 17, 1),
    _Warning17_time_stamp_Type()
)
warning17_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning17_time_stamp.setStatus("optional")
_Warning17_code_Type = Integer32
_Warning17_code_Object = MibScalar
warning17_code = _Warning17_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 17, 2),
    _Warning17_code_Type()
)
warning17_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning17_code.setStatus("optional")
_Warning17_date_time_Type = OctetString
_Warning17_date_time_Object = MibScalar
warning17_date_time = _Warning17_date_time_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 17, 3),
    _Warning17_date_time_Type()
)
warning17_date_time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning17_date_time.setStatus("optional")
_Warning18_ObjectIdentity = ObjectIdentity
warning18 = _Warning18_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 18)
)
_Warning18_time_stamp_Type = Integer32
_Warning18_time_stamp_Object = MibScalar
warning18_time_stamp = _Warning18_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 18, 1),
    _Warning18_time_stamp_Type()
)
warning18_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning18_time_stamp.setStatus("optional")
_Warning18_code_Type = Integer32
_Warning18_code_Object = MibScalar
warning18_code = _Warning18_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 18, 2),
    _Warning18_code_Type()
)
warning18_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning18_code.setStatus("optional")
_Warning18_date_time_Type = OctetString
_Warning18_date_time_Object = MibScalar
warning18_date_time = _Warning18_date_time_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 18, 3),
    _Warning18_date_time_Type()
)
warning18_date_time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning18_date_time.setStatus("optional")
_Warning19_ObjectIdentity = ObjectIdentity
warning19 = _Warning19_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 19)
)
_Warning19_time_stamp_Type = Integer32
_Warning19_time_stamp_Object = MibScalar
warning19_time_stamp = _Warning19_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 19, 1),
    _Warning19_time_stamp_Type()
)
warning19_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning19_time_stamp.setStatus("optional")
_Warning19_code_Type = Integer32
_Warning19_code_Object = MibScalar
warning19_code = _Warning19_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 19, 2),
    _Warning19_code_Type()
)
warning19_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning19_code.setStatus("optional")
_Warning19_date_time_Type = OctetString
_Warning19_date_time_Object = MibScalar
warning19_date_time = _Warning19_date_time_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 19, 3),
    _Warning19_date_time_Type()
)
warning19_date_time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning19_date_time.setStatus("optional")
_Warning20_ObjectIdentity = ObjectIdentity
warning20 = _Warning20_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 20)
)
_Warning20_time_stamp_Type = Integer32
_Warning20_time_stamp_Object = MibScalar
warning20_time_stamp = _Warning20_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 20, 1),
    _Warning20_time_stamp_Type()
)
warning20_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning20_time_stamp.setStatus("optional")
_Warning20_code_Type = Integer32
_Warning20_code_Object = MibScalar
warning20_code = _Warning20_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 20, 2),
    _Warning20_code_Type()
)
warning20_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning20_code.setStatus("optional")
_Warning20_date_time_Type = OctetString
_Warning20_date_time_Object = MibScalar
warning20_date_time = _Warning20_date_time_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 20, 3),
    _Warning20_date_time_Type()
)
warning20_date_time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning20_date_time.setStatus("optional")
_Warning21_ObjectIdentity = ObjectIdentity
warning21 = _Warning21_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 21)
)
_Warning21_time_stamp_Type = Integer32
_Warning21_time_stamp_Object = MibScalar
warning21_time_stamp = _Warning21_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 21, 1),
    _Warning21_time_stamp_Type()
)
warning21_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning21_time_stamp.setStatus("optional")
_Warning21_code_Type = Integer32
_Warning21_code_Object = MibScalar
warning21_code = _Warning21_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 21, 2),
    _Warning21_code_Type()
)
warning21_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning21_code.setStatus("optional")
_Warning21_date_time_Type = OctetString
_Warning21_date_time_Object = MibScalar
warning21_date_time = _Warning21_date_time_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 21, 3),
    _Warning21_date_time_Type()
)
warning21_date_time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning21_date_time.setStatus("optional")
_Warning22_ObjectIdentity = ObjectIdentity
warning22 = _Warning22_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 22)
)
_Warning22_time_stamp_Type = Integer32
_Warning22_time_stamp_Object = MibScalar
warning22_time_stamp = _Warning22_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 22, 1),
    _Warning22_time_stamp_Type()
)
warning22_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning22_time_stamp.setStatus("optional")
_Warning22_code_Type = Integer32
_Warning22_code_Object = MibScalar
warning22_code = _Warning22_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 22, 2),
    _Warning22_code_Type()
)
warning22_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning22_code.setStatus("optional")
_Warning22_date_time_Type = OctetString
_Warning22_date_time_Object = MibScalar
warning22_date_time = _Warning22_date_time_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 22, 3),
    _Warning22_date_time_Type()
)
warning22_date_time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning22_date_time.setStatus("optional")
_Warning23_ObjectIdentity = ObjectIdentity
warning23 = _Warning23_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 23)
)
_Warning23_time_stamp_Type = Integer32
_Warning23_time_stamp_Object = MibScalar
warning23_time_stamp = _Warning23_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 23, 1),
    _Warning23_time_stamp_Type()
)
warning23_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning23_time_stamp.setStatus("optional")
_Warning23_code_Type = Integer32
_Warning23_code_Object = MibScalar
warning23_code = _Warning23_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 23, 2),
    _Warning23_code_Type()
)
warning23_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning23_code.setStatus("optional")
_Warning23_date_time_Type = OctetString
_Warning23_date_time_Object = MibScalar
warning23_date_time = _Warning23_date_time_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 23, 3),
    _Warning23_date_time_Type()
)
warning23_date_time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning23_date_time.setStatus("optional")
_Warning24_ObjectIdentity = ObjectIdentity
warning24 = _Warning24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 24)
)
_Warning24_time_stamp_Type = Integer32
_Warning24_time_stamp_Object = MibScalar
warning24_time_stamp = _Warning24_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 24, 1),
    _Warning24_time_stamp_Type()
)
warning24_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning24_time_stamp.setStatus("optional")
_Warning24_code_Type = Integer32
_Warning24_code_Object = MibScalar
warning24_code = _Warning24_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 24, 2),
    _Warning24_code_Type()
)
warning24_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning24_code.setStatus("optional")
_Warning24_date_time_Type = OctetString
_Warning24_date_time_Object = MibScalar
warning24_date_time = _Warning24_date_time_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 24, 3),
    _Warning24_date_time_Type()
)
warning24_date_time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning24_date_time.setStatus("optional")
_Warning25_ObjectIdentity = ObjectIdentity
warning25 = _Warning25_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 25)
)
_Warning25_time_stamp_Type = Integer32
_Warning25_time_stamp_Object = MibScalar
warning25_time_stamp = _Warning25_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 25, 1),
    _Warning25_time_stamp_Type()
)
warning25_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning25_time_stamp.setStatus("optional")
_Warning25_code_Type = Integer32
_Warning25_code_Object = MibScalar
warning25_code = _Warning25_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 25, 2),
    _Warning25_code_Type()
)
warning25_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning25_code.setStatus("optional")
_Warning25_date_time_Type = OctetString
_Warning25_date_time_Object = MibScalar
warning25_date_time = _Warning25_date_time_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 25, 3),
    _Warning25_date_time_Type()
)
warning25_date_time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning25_date_time.setStatus("optional")
_Warning26_ObjectIdentity = ObjectIdentity
warning26 = _Warning26_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 26)
)
_Warning26_time_stamp_Type = Integer32
_Warning26_time_stamp_Object = MibScalar
warning26_time_stamp = _Warning26_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 26, 1),
    _Warning26_time_stamp_Type()
)
warning26_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning26_time_stamp.setStatus("optional")
_Warning26_code_Type = Integer32
_Warning26_code_Object = MibScalar
warning26_code = _Warning26_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 26, 2),
    _Warning26_code_Type()
)
warning26_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning26_code.setStatus("optional")
_Warning26_date_time_Type = OctetString
_Warning26_date_time_Object = MibScalar
warning26_date_time = _Warning26_date_time_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 26, 3),
    _Warning26_date_time_Type()
)
warning26_date_time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning26_date_time.setStatus("optional")
_Warning27_ObjectIdentity = ObjectIdentity
warning27 = _Warning27_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 27)
)
_Warning27_time_stamp_Type = Integer32
_Warning27_time_stamp_Object = MibScalar
warning27_time_stamp = _Warning27_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 27, 1),
    _Warning27_time_stamp_Type()
)
warning27_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning27_time_stamp.setStatus("optional")
_Warning27_code_Type = Integer32
_Warning27_code_Object = MibScalar
warning27_code = _Warning27_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 27, 2),
    _Warning27_code_Type()
)
warning27_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning27_code.setStatus("optional")
_Warning27_date_time_Type = OctetString
_Warning27_date_time_Object = MibScalar
warning27_date_time = _Warning27_date_time_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 27, 3),
    _Warning27_date_time_Type()
)
warning27_date_time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning27_date_time.setStatus("optional")
_Warning28_ObjectIdentity = ObjectIdentity
warning28 = _Warning28_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 28)
)
_Warning28_time_stamp_Type = Integer32
_Warning28_time_stamp_Object = MibScalar
warning28_time_stamp = _Warning28_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 28, 1),
    _Warning28_time_stamp_Type()
)
warning28_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning28_time_stamp.setStatus("optional")
_Warning28_code_Type = Integer32
_Warning28_code_Object = MibScalar
warning28_code = _Warning28_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 28, 2),
    _Warning28_code_Type()
)
warning28_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning28_code.setStatus("optional")
_Warning28_date_time_Type = OctetString
_Warning28_date_time_Object = MibScalar
warning28_date_time = _Warning28_date_time_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 28, 3),
    _Warning28_date_time_Type()
)
warning28_date_time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning28_date_time.setStatus("optional")
_Warning29_ObjectIdentity = ObjectIdentity
warning29 = _Warning29_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 29)
)
_Warning29_time_stamp_Type = Integer32
_Warning29_time_stamp_Object = MibScalar
warning29_time_stamp = _Warning29_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 29, 1),
    _Warning29_time_stamp_Type()
)
warning29_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning29_time_stamp.setStatus("optional")
_Warning29_code_Type = Integer32
_Warning29_code_Object = MibScalar
warning29_code = _Warning29_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 29, 2),
    _Warning29_code_Type()
)
warning29_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning29_code.setStatus("optional")
_Warning29_date_time_Type = OctetString
_Warning29_date_time_Object = MibScalar
warning29_date_time = _Warning29_date_time_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 29, 3),
    _Warning29_date_time_Type()
)
warning29_date_time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning29_date_time.setStatus("optional")
_Warning30_ObjectIdentity = ObjectIdentity
warning30 = _Warning30_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 30)
)
_Warning30_time_stamp_Type = Integer32
_Warning30_time_stamp_Object = MibScalar
warning30_time_stamp = _Warning30_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 30, 1),
    _Warning30_time_stamp_Type()
)
warning30_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning30_time_stamp.setStatus("optional")
_Warning30_code_Type = Integer32
_Warning30_code_Object = MibScalar
warning30_code = _Warning30_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 30, 2),
    _Warning30_code_Type()
)
warning30_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning30_code.setStatus("optional")
_Warning30_date_time_Type = OctetString
_Warning30_date_time_Object = MibScalar
warning30_date_time = _Warning30_date_time_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 30, 3),
    _Warning30_date_time_Type()
)
warning30_date_time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning30_date_time.setStatus("optional")
_Warning31_ObjectIdentity = ObjectIdentity
warning31 = _Warning31_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 31)
)
_Warning31_time_stamp_Type = Integer32
_Warning31_time_stamp_Object = MibScalar
warning31_time_stamp = _Warning31_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 31, 1),
    _Warning31_time_stamp_Type()
)
warning31_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning31_time_stamp.setStatus("optional")
_Warning31_code_Type = Integer32
_Warning31_code_Object = MibScalar
warning31_code = _Warning31_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 31, 2),
    _Warning31_code_Type()
)
warning31_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning31_code.setStatus("optional")
_Warning31_date_time_Type = OctetString
_Warning31_date_time_Object = MibScalar
warning31_date_time = _Warning31_date_time_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 31, 3),
    _Warning31_date_time_Type()
)
warning31_date_time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning31_date_time.setStatus("optional")
_Warning32_ObjectIdentity = ObjectIdentity
warning32 = _Warning32_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 32)
)
_Warning32_time_stamp_Type = Integer32
_Warning32_time_stamp_Object = MibScalar
warning32_time_stamp = _Warning32_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 32, 1),
    _Warning32_time_stamp_Type()
)
warning32_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning32_time_stamp.setStatus("optional")
_Warning32_code_Type = Integer32
_Warning32_code_Object = MibScalar
warning32_code = _Warning32_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 32, 2),
    _Warning32_code_Type()
)
warning32_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning32_code.setStatus("optional")
_Warning32_date_time_Type = OctetString
_Warning32_date_time_Object = MibScalar
warning32_date_time = _Warning32_date_time_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 32, 3),
    _Warning32_date_time_Type()
)
warning32_date_time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning32_date_time.setStatus("optional")
_Warning33_ObjectIdentity = ObjectIdentity
warning33 = _Warning33_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 33)
)
_Warning33_time_stamp_Type = Integer32
_Warning33_time_stamp_Object = MibScalar
warning33_time_stamp = _Warning33_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 33, 1),
    _Warning33_time_stamp_Type()
)
warning33_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning33_time_stamp.setStatus("optional")
_Warning33_code_Type = Integer32
_Warning33_code_Object = MibScalar
warning33_code = _Warning33_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 33, 2),
    _Warning33_code_Type()
)
warning33_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning33_code.setStatus("optional")
_Warning33_date_time_Type = OctetString
_Warning33_date_time_Object = MibScalar
warning33_date_time = _Warning33_date_time_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 33, 3),
    _Warning33_date_time_Type()
)
warning33_date_time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning33_date_time.setStatus("optional")
_Warning34_ObjectIdentity = ObjectIdentity
warning34 = _Warning34_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 34)
)
_Warning34_time_stamp_Type = Integer32
_Warning34_time_stamp_Object = MibScalar
warning34_time_stamp = _Warning34_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 34, 1),
    _Warning34_time_stamp_Type()
)
warning34_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning34_time_stamp.setStatus("optional")
_Warning34_code_Type = Integer32
_Warning34_code_Object = MibScalar
warning34_code = _Warning34_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 34, 2),
    _Warning34_code_Type()
)
warning34_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning34_code.setStatus("optional")
_Warning34_date_time_Type = OctetString
_Warning34_date_time_Object = MibScalar
warning34_date_time = _Warning34_date_time_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 34, 3),
    _Warning34_date_time_Type()
)
warning34_date_time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning34_date_time.setStatus("optional")
_Warning35_ObjectIdentity = ObjectIdentity
warning35 = _Warning35_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 35)
)
_Warning35_time_stamp_Type = Integer32
_Warning35_time_stamp_Object = MibScalar
warning35_time_stamp = _Warning35_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 35, 1),
    _Warning35_time_stamp_Type()
)
warning35_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning35_time_stamp.setStatus("optional")
_Warning35_code_Type = Integer32
_Warning35_code_Object = MibScalar
warning35_code = _Warning35_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 35, 2),
    _Warning35_code_Type()
)
warning35_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning35_code.setStatus("optional")
_Warning35_date_time_Type = OctetString
_Warning35_date_time_Object = MibScalar
warning35_date_time = _Warning35_date_time_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 35, 3),
    _Warning35_date_time_Type()
)
warning35_date_time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning35_date_time.setStatus("optional")
_Warning36_ObjectIdentity = ObjectIdentity
warning36 = _Warning36_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 36)
)
_Warning36_time_stamp_Type = Integer32
_Warning36_time_stamp_Object = MibScalar
warning36_time_stamp = _Warning36_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 36, 1),
    _Warning36_time_stamp_Type()
)
warning36_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning36_time_stamp.setStatus("optional")
_Warning36_code_Type = Integer32
_Warning36_code_Object = MibScalar
warning36_code = _Warning36_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 36, 2),
    _Warning36_code_Type()
)
warning36_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning36_code.setStatus("optional")
_Warning36_date_time_Type = OctetString
_Warning36_date_time_Object = MibScalar
warning36_date_time = _Warning36_date_time_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 36, 3),
    _Warning36_date_time_Type()
)
warning36_date_time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning36_date_time.setStatus("optional")
_Warning37_ObjectIdentity = ObjectIdentity
warning37 = _Warning37_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 37)
)
_Warning37_time_stamp_Type = Integer32
_Warning37_time_stamp_Object = MibScalar
warning37_time_stamp = _Warning37_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 37, 1),
    _Warning37_time_stamp_Type()
)
warning37_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning37_time_stamp.setStatus("optional")
_Warning37_code_Type = Integer32
_Warning37_code_Object = MibScalar
warning37_code = _Warning37_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 37, 2),
    _Warning37_code_Type()
)
warning37_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning37_code.setStatus("optional")
_Warning37_date_time_Type = OctetString
_Warning37_date_time_Object = MibScalar
warning37_date_time = _Warning37_date_time_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 37, 3),
    _Warning37_date_time_Type()
)
warning37_date_time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning37_date_time.setStatus("optional")
_Warning38_ObjectIdentity = ObjectIdentity
warning38 = _Warning38_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 38)
)
_Warning38_time_stamp_Type = Integer32
_Warning38_time_stamp_Object = MibScalar
warning38_time_stamp = _Warning38_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 38, 1),
    _Warning38_time_stamp_Type()
)
warning38_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning38_time_stamp.setStatus("optional")
_Warning38_code_Type = Integer32
_Warning38_code_Object = MibScalar
warning38_code = _Warning38_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 38, 2),
    _Warning38_code_Type()
)
warning38_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning38_code.setStatus("optional")
_Warning38_date_time_Type = OctetString
_Warning38_date_time_Object = MibScalar
warning38_date_time = _Warning38_date_time_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 38, 3),
    _Warning38_date_time_Type()
)
warning38_date_time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning38_date_time.setStatus("optional")
_Warning39_ObjectIdentity = ObjectIdentity
warning39 = _Warning39_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 39)
)
_Warning39_time_stamp_Type = Integer32
_Warning39_time_stamp_Object = MibScalar
warning39_time_stamp = _Warning39_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 39, 1),
    _Warning39_time_stamp_Type()
)
warning39_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning39_time_stamp.setStatus("optional")
_Warning39_code_Type = Integer32
_Warning39_code_Object = MibScalar
warning39_code = _Warning39_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 39, 2),
    _Warning39_code_Type()
)
warning39_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning39_code.setStatus("optional")
_Warning39_date_time_Type = OctetString
_Warning39_date_time_Object = MibScalar
warning39_date_time = _Warning39_date_time_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 39, 3),
    _Warning39_date_time_Type()
)
warning39_date_time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning39_date_time.setStatus("optional")
_Warning40_ObjectIdentity = ObjectIdentity
warning40 = _Warning40_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 40)
)
_Warning40_time_stamp_Type = Integer32
_Warning40_time_stamp_Object = MibScalar
warning40_time_stamp = _Warning40_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 40, 1),
    _Warning40_time_stamp_Type()
)
warning40_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning40_time_stamp.setStatus("optional")
_Warning40_code_Type = Integer32
_Warning40_code_Object = MibScalar
warning40_code = _Warning40_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 40, 2),
    _Warning40_code_Type()
)
warning40_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning40_code.setStatus("optional")
_Warning40_date_time_Type = OctetString
_Warning40_date_time_Object = MibScalar
warning40_date_time = _Warning40_date_time_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 40, 3),
    _Warning40_date_time_Type()
)
warning40_date_time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning40_date_time.setStatus("optional")
_Warning41_ObjectIdentity = ObjectIdentity
warning41 = _Warning41_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 41)
)
_Warning41_time_stamp_Type = Integer32
_Warning41_time_stamp_Object = MibScalar
warning41_time_stamp = _Warning41_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 41, 1),
    _Warning41_time_stamp_Type()
)
warning41_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning41_time_stamp.setStatus("optional")
_Warning41_code_Type = Integer32
_Warning41_code_Object = MibScalar
warning41_code = _Warning41_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 41, 2),
    _Warning41_code_Type()
)
warning41_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning41_code.setStatus("optional")
_Warning41_date_time_Type = OctetString
_Warning41_date_time_Object = MibScalar
warning41_date_time = _Warning41_date_time_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 41, 3),
    _Warning41_date_time_Type()
)
warning41_date_time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning41_date_time.setStatus("optional")
_Warning42_ObjectIdentity = ObjectIdentity
warning42 = _Warning42_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 42)
)
_Warning42_time_stamp_Type = Integer32
_Warning42_time_stamp_Object = MibScalar
warning42_time_stamp = _Warning42_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 42, 1),
    _Warning42_time_stamp_Type()
)
warning42_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning42_time_stamp.setStatus("optional")
_Warning42_code_Type = Integer32
_Warning42_code_Object = MibScalar
warning42_code = _Warning42_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 42, 2),
    _Warning42_code_Type()
)
warning42_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning42_code.setStatus("optional")
_Warning42_date_time_Type = OctetString
_Warning42_date_time_Object = MibScalar
warning42_date_time = _Warning42_date_time_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 42, 3),
    _Warning42_date_time_Type()
)
warning42_date_time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning42_date_time.setStatus("optional")
_Warning43_ObjectIdentity = ObjectIdentity
warning43 = _Warning43_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 43)
)
_Warning43_time_stamp_Type = Integer32
_Warning43_time_stamp_Object = MibScalar
warning43_time_stamp = _Warning43_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 43, 1),
    _Warning43_time_stamp_Type()
)
warning43_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning43_time_stamp.setStatus("optional")
_Warning43_code_Type = Integer32
_Warning43_code_Object = MibScalar
warning43_code = _Warning43_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 43, 2),
    _Warning43_code_Type()
)
warning43_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning43_code.setStatus("optional")
_Warning43_date_time_Type = OctetString
_Warning43_date_time_Object = MibScalar
warning43_date_time = _Warning43_date_time_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 43, 3),
    _Warning43_date_time_Type()
)
warning43_date_time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning43_date_time.setStatus("optional")
_Warning44_ObjectIdentity = ObjectIdentity
warning44 = _Warning44_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 44)
)
_Warning44_time_stamp_Type = Integer32
_Warning44_time_stamp_Object = MibScalar
warning44_time_stamp = _Warning44_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 44, 1),
    _Warning44_time_stamp_Type()
)
warning44_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning44_time_stamp.setStatus("optional")
_Warning44_code_Type = Integer32
_Warning44_code_Object = MibScalar
warning44_code = _Warning44_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 44, 2),
    _Warning44_code_Type()
)
warning44_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning44_code.setStatus("optional")
_Warning44_date_time_Type = OctetString
_Warning44_date_time_Object = MibScalar
warning44_date_time = _Warning44_date_time_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 44, 3),
    _Warning44_date_time_Type()
)
warning44_date_time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning44_date_time.setStatus("optional")
_Warning45_ObjectIdentity = ObjectIdentity
warning45 = _Warning45_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 45)
)
_Warning45_time_stamp_Type = Integer32
_Warning45_time_stamp_Object = MibScalar
warning45_time_stamp = _Warning45_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 45, 1),
    _Warning45_time_stamp_Type()
)
warning45_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning45_time_stamp.setStatus("optional")
_Warning45_code_Type = Integer32
_Warning45_code_Object = MibScalar
warning45_code = _Warning45_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 45, 2),
    _Warning45_code_Type()
)
warning45_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning45_code.setStatus("optional")
_Warning45_date_time_Type = OctetString
_Warning45_date_time_Object = MibScalar
warning45_date_time = _Warning45_date_time_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 45, 3),
    _Warning45_date_time_Type()
)
warning45_date_time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning45_date_time.setStatus("optional")
_Warning46_ObjectIdentity = ObjectIdentity
warning46 = _Warning46_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 46)
)
_Warning46_time_stamp_Type = Integer32
_Warning46_time_stamp_Object = MibScalar
warning46_time_stamp = _Warning46_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 46, 1),
    _Warning46_time_stamp_Type()
)
warning46_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning46_time_stamp.setStatus("optional")
_Warning46_code_Type = Integer32
_Warning46_code_Object = MibScalar
warning46_code = _Warning46_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 46, 2),
    _Warning46_code_Type()
)
warning46_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning46_code.setStatus("optional")
_Warning46_date_time_Type = OctetString
_Warning46_date_time_Object = MibScalar
warning46_date_time = _Warning46_date_time_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 46, 3),
    _Warning46_date_time_Type()
)
warning46_date_time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning46_date_time.setStatus("optional")
_Warning47_ObjectIdentity = ObjectIdentity
warning47 = _Warning47_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 47)
)
_Warning47_time_stamp_Type = Integer32
_Warning47_time_stamp_Object = MibScalar
warning47_time_stamp = _Warning47_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 47, 1),
    _Warning47_time_stamp_Type()
)
warning47_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning47_time_stamp.setStatus("optional")
_Warning47_code_Type = Integer32
_Warning47_code_Object = MibScalar
warning47_code = _Warning47_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 47, 2),
    _Warning47_code_Type()
)
warning47_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning47_code.setStatus("optional")
_Warning47_date_time_Type = OctetString
_Warning47_date_time_Object = MibScalar
warning47_date_time = _Warning47_date_time_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 47, 3),
    _Warning47_date_time_Type()
)
warning47_date_time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning47_date_time.setStatus("optional")
_Warning48_ObjectIdentity = ObjectIdentity
warning48 = _Warning48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 48)
)
_Warning48_time_stamp_Type = Integer32
_Warning48_time_stamp_Object = MibScalar
warning48_time_stamp = _Warning48_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 48, 1),
    _Warning48_time_stamp_Type()
)
warning48_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning48_time_stamp.setStatus("optional")
_Warning48_code_Type = Integer32
_Warning48_code_Object = MibScalar
warning48_code = _Warning48_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 48, 2),
    _Warning48_code_Type()
)
warning48_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning48_code.setStatus("optional")
_Warning48_date_time_Type = OctetString
_Warning48_date_time_Object = MibScalar
warning48_date_time = _Warning48_date_time_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 48, 3),
    _Warning48_date_time_Type()
)
warning48_date_time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning48_date_time.setStatus("optional")
_Warning49_ObjectIdentity = ObjectIdentity
warning49 = _Warning49_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 49)
)
_Warning49_time_stamp_Type = Integer32
_Warning49_time_stamp_Object = MibScalar
warning49_time_stamp = _Warning49_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 49, 1),
    _Warning49_time_stamp_Type()
)
warning49_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning49_time_stamp.setStatus("optional")
_Warning49_code_Type = Integer32
_Warning49_code_Object = MibScalar
warning49_code = _Warning49_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 49, 2),
    _Warning49_code_Type()
)
warning49_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning49_code.setStatus("optional")
_Warning49_date_time_Type = OctetString
_Warning49_date_time_Object = MibScalar
warning49_date_time = _Warning49_date_time_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 49, 3),
    _Warning49_date_time_Type()
)
warning49_date_time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning49_date_time.setStatus("optional")
_Warning50_ObjectIdentity = ObjectIdentity
warning50 = _Warning50_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 50)
)
_Warning50_time_stamp_Type = Integer32
_Warning50_time_stamp_Object = MibScalar
warning50_time_stamp = _Warning50_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 50, 1),
    _Warning50_time_stamp_Type()
)
warning50_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning50_time_stamp.setStatus("optional")
_Warning50_code_Type = Integer32
_Warning50_code_Object = MibScalar
warning50_code = _Warning50_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 50, 2),
    _Warning50_code_Type()
)
warning50_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning50_code.setStatus("optional")
_Warning50_date_time_Type = OctetString
_Warning50_date_time_Object = MibScalar
warning50_date_time = _Warning50_date_time_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 50, 3),
    _Warning50_date_time_Type()
)
warning50_date_time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning50_date_time.setStatus("optional")
_Security_ObjectIdentity = ObjectIdentity
security = _Security_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 23)
)
_Settings_security_ObjectIdentity = ObjectIdentity
settings_security = _Settings_security_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 23, 1)
)


class _Supports_pjl_user_groups_Type(Integer32):
    """Custom type supports_pjl_user_groups based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            2
        )
    )
    namedValues = NamedValues(
        ("eTrue", 2)
    )


_Supports_pjl_user_groups_Type.__name__ = "Integer32"
_Supports_pjl_user_groups_Object = MibScalar
supports_pjl_user_groups = _Supports_pjl_user_groups_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 23, 1, 1),
    _Supports_pjl_user_groups_Type()
)
supports_pjl_user_groups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    supports_pjl_user_groups.setStatus("optional")
_Source_subsystem_ObjectIdentity = ObjectIdentity
source_subsystem = _Source_subsystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2)
)
_Io_ObjectIdentity = ObjectIdentity
io = _Io_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 1)
)
_Settings_io_ObjectIdentity = ObjectIdentity
settings_io = _Settings_io_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 1, 1)
)


class _Io_timeout_Type(Integer32):
    """Custom type io_timeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 300),
    )


_Io_timeout_Type.__name__ = "Integer32"
_Io_timeout_Object = MibScalar
io_timeout = _Io_timeout_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 1, 1, 1),
    _Io_timeout_Type()
)
io_timeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    io_timeout.setStatus("optional")


class _Io_switch_Type(Integer32):
    """Custom type io_switch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("eYes", 1)
    )


_Io_switch_Type.__name__ = "Integer32"
_Io_switch_Object = MibScalar
io_switch = _Io_switch_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 1, 1, 2),
    _Io_switch_Type()
)
io_switch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    io_switch.setStatus("optional")
_Ports_ObjectIdentity = ObjectIdentity
ports = _Ports_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 1, 3)
)
_Port1_ObjectIdentity = ObjectIdentity
port1 = _Port1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 1, 3, 1)
)


class _Port1_parallel_speed_Type(Integer32):
    """Custom type port1_parallel_speed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eFast", 2),
          ("eSlow", 1))
    )


_Port1_parallel_speed_Type.__name__ = "Integer32"
_Port1_parallel_speed_Object = MibScalar
port1_parallel_speed = _Port1_parallel_speed_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 1, 3, 1, 4),
    _Port1_parallel_speed_Type()
)
port1_parallel_speed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port1_parallel_speed.setStatus("optional")


class _Port1_parallel_bidirectionality_Type(Integer32):
    """Custom type port1_parallel_bidirectionality based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eBidirectional", 2),
          ("eUnidirectional", 1))
    )


_Port1_parallel_bidirectionality_Type.__name__ = "Integer32"
_Port1_parallel_bidirectionality_Object = MibScalar
port1_parallel_bidirectionality = _Port1_parallel_bidirectionality_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 1, 3, 1, 5),
    _Port1_parallel_bidirectionality_Type()
)
port1_parallel_bidirectionality.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port1_parallel_bidirectionality.setStatus("optional")
_Scanner_ObjectIdentity = ObjectIdentity
scanner = _Scanner_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2)
)
_Settings_scanner_ObjectIdentity = ObjectIdentity
settings_scanner = _Settings_scanner_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 1)
)


class _Scanner_accessory_adf_sheet_count_Type(Integer32):
    """Custom type scanner_accessory_adf_sheet_count based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Scanner_accessory_adf_sheet_count_Type.__name__ = "Integer32"
_Scanner_accessory_adf_sheet_count_Object = MibScalar
scanner_accessory_adf_sheet_count = _Scanner_accessory_adf_sheet_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 1, 20),
    _Scanner_accessory_adf_sheet_count_Type()
)
scanner_accessory_adf_sheet_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scanner_accessory_adf_sheet_count.setStatus("optional")


class _Scanner_accessory_flatbed_scan_count_Type(Integer32):
    """Custom type scanner_accessory_flatbed_scan_count based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Scanner_accessory_flatbed_scan_count_Type.__name__ = "Integer32"
_Scanner_accessory_flatbed_scan_count_Object = MibScalar
scanner_accessory_flatbed_scan_count = _Scanner_accessory_flatbed_scan_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 1, 21),
    _Scanner_accessory_flatbed_scan_count_Type()
)
scanner_accessory_flatbed_scan_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scanner_accessory_flatbed_scan_count.setStatus("optional")
_Scanner_accessory_adf_one_sided_sheet_count_Type = Integer32
_Scanner_accessory_adf_one_sided_sheet_count_Object = MibScalar
scanner_accessory_adf_one_sided_sheet_count = _Scanner_accessory_adf_one_sided_sheet_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 1, 59),
    _Scanner_accessory_adf_one_sided_sheet_count_Type()
)
scanner_accessory_adf_one_sided_sheet_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scanner_accessory_adf_one_sided_sheet_count.setStatus("optional")
_Scanner_accessory_adf_two_sided_sheet_count_Type = Integer32
_Scanner_accessory_adf_two_sided_sheet_count_Object = MibScalar
scanner_accessory_adf_two_sided_sheet_count = _Scanner_accessory_adf_two_sided_sheet_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 1, 60),
    _Scanner_accessory_adf_two_sided_sheet_count_Type()
)
scanner_accessory_adf_two_sided_sheet_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scanner_accessory_adf_two_sided_sheet_count.setStatus("optional")
_Scanner_accessory_copy_job_scan_count_Type = Integer32
_Scanner_accessory_copy_job_scan_count_Object = MibScalar
scanner_accessory_copy_job_scan_count = _Scanner_accessory_copy_job_scan_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 1, 61),
    _Scanner_accessory_copy_job_scan_count_Type()
)
scanner_accessory_copy_job_scan_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scanner_accessory_copy_job_scan_count.setStatus("optional")
_Scanner_accessory_send_job_scan_count_Type = Integer32
_Scanner_accessory_send_job_scan_count_Object = MibScalar
scanner_accessory_send_job_scan_count = _Scanner_accessory_send_job_scan_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 1, 62),
    _Scanner_accessory_send_job_scan_count_Type()
)
scanner_accessory_send_job_scan_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scanner_accessory_send_job_scan_count.setStatus("optional")


class _Scan_to_folder_count_Type(Integer32):
    """Custom type scan_to_folder_count based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999999),
    )


_Scan_to_folder_count_Type.__name__ = "Integer32"
_Scan_to_folder_count_Object = MibScalar
scan_to_folder_count = _Scan_to_folder_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 1, 89),
    _Scan_to_folder_count_Type()
)
scan_to_folder_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scan_to_folder_count.setStatus("optional")


class _Fax_job_scan_count_Type(Integer32):
    """Custom type fax_job_scan_count based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999999),
    )


_Fax_job_scan_count_Type.__name__ = "Integer32"
_Fax_job_scan_count_Object = MibScalar
fax_job_scan_count = _Fax_job_scan_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 1, 90),
    _Fax_job_scan_count_Type()
)
fax_job_scan_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fax_job_scan_count.setStatus("optional")
_Processing_subsystem_ObjectIdentity = ObjectIdentity
processing_subsystem = _Processing_subsystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3)
)
_Pdl_ObjectIdentity = ObjectIdentity
pdl = _Pdl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 3)
)
_Settings_pdl_ObjectIdentity = ObjectIdentity
settings_pdl = _Settings_pdl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 3, 1)
)
_Default_copies_Type = Integer32
_Default_copies_Object = MibScalar
default_copies = _Default_copies_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 3, 1, 4),
    _Default_copies_Type()
)
default_copies.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    default_copies.setStatus("optional")


class _Form_feed_Type(Integer32):
    """Custom type form_feed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("eInitiateAction", 1)
    )


_Form_feed_Type.__name__ = "Integer32"
_Form_feed_Object = MibScalar
form_feed = _Form_feed_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 3, 1, 5),
    _Form_feed_Type()
)
form_feed.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    form_feed.setStatus("optional")
_Default_vertical_black_resolution_Type = Integer32
_Default_vertical_black_resolution_Object = MibScalar
default_vertical_black_resolution = _Default_vertical_black_resolution_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 3, 1, 8),
    _Default_vertical_black_resolution_Type()
)
default_vertical_black_resolution.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    default_vertical_black_resolution.setStatus("optional")
_Default_horizontal_black_resolution_Type = Integer32
_Default_horizontal_black_resolution_Object = MibScalar
default_horizontal_black_resolution = _Default_horizontal_black_resolution_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 3, 1, 9),
    _Default_horizontal_black_resolution_Type()
)
default_horizontal_black_resolution.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    default_horizontal_black_resolution.setStatus("optional")


class _Default_page_protect_Type(Integer32):
    """Custom type default_page_protect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            2
        )
    )
    namedValues = NamedValues(
        ("eOn", 2)
    )


_Default_page_protect_Type.__name__ = "Integer32"
_Default_page_protect_Object = MibScalar
default_page_protect = _Default_page_protect_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 3, 1, 10),
    _Default_page_protect_Type()
)
default_page_protect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    default_page_protect.setStatus("optional")
_Default_lines_per_page_Type = Integer32
_Default_lines_per_page_Object = MibScalar
default_lines_per_page = _Default_lines_per_page_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 3, 1, 11),
    _Default_lines_per_page_Type()
)
default_lines_per_page.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    default_lines_per_page.setStatus("optional")
_Default_vmi_Type = Integer32
_Default_vmi_Object = MibScalar
default_vmi = _Default_vmi_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 3, 1, 12),
    _Default_vmi_Type()
)
default_vmi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    default_vmi.setStatus("optional")


class _Default_media_size_Type(Integer32):
    """Custom type default_media_size based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              10,
              11,
              15,
              17,
              19,
              24,
              25,
              26,
              27,
              36,
              37,
              39,
              44,
              45,
              46,
              74,
              75,
              101,
              120,
              122,
              32767)
        )
    )
    namedValues = NamedValues(
        *(("eCustom", 101),
          ("eFoolscap", 10),
          ("eISORA3", 39),
          ("eISORA4", 36),
          ("eISOSRA4", 37),
          ("eISOandJISA3", 27),
          ("eISOandJISA4", 26),
          ("eISOandJISA5", 25),
          ("eISOandJISA6", 24),
          ("eIndexCard4x6", 74),
          ("eIndexCard5x7", 122),
          ("eIndexCard5x8", 75),
          ("eJISB4", 46),
          ("eJISB5", 45),
          ("eJISB6", 44),
          ("eLedger", 11),
          ("eROC16K", 17),
          ("eROC8K", 19),
          ("eStatement", 15),
          ("eTabloidExtra", 120),
          ("eUSExecutive", 1),
          ("eUSLegal", 3),
          ("eUSLetter", 2),
          ("eUnknownMediaSize", 32767))
    )


_Default_media_size_Type.__name__ = "Integer32"
_Default_media_size_Object = MibScalar
default_media_size = _Default_media_size_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 3, 1, 13),
    _Default_media_size_Type()
)
default_media_size.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    default_media_size.setStatus("optional")


class _Cold_reset_media_size_Type(Integer32):
    """Custom type cold_reset_media_size based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              26)
        )
    )
    namedValues = NamedValues(
        *(("eISOandJISA4", 26),
          ("eUSLetter", 2))
    )


_Cold_reset_media_size_Type.__name__ = "Integer32"
_Cold_reset_media_size_Object = MibScalar
cold_reset_media_size = _Cold_reset_media_size_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 3, 1, 19),
    _Cold_reset_media_size_Type()
)
cold_reset_media_size.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cold_reset_media_size.setStatus("optional")
_Default_media_name_Type = OctetString
_Default_media_name_Object = MibScalar
default_media_name = _Default_media_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 3, 1, 22),
    _Default_media_name_Type()
)
default_media_name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    default_media_name.setStatus("optional")


class _Reprint_Type(Integer32):
    """Custom type reprint based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("eAuto", 3),
          ("eOff", 1),
          ("eOn", 2))
    )


_Reprint_Type.__name__ = "Integer32"
_Reprint_Object = MibScalar
reprint = _Reprint_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 3, 1, 36),
    _Reprint_Type()
)
reprint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    reprint.setStatus("optional")
_Default_bits_per_pixel_Type = Integer32
_Default_bits_per_pixel_Object = MibScalar
default_bits_per_pixel = _Default_bits_per_pixel_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 3, 1, 39),
    _Default_bits_per_pixel_Type()
)
default_bits_per_pixel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    default_bits_per_pixel.setStatus("optional")
_Status_pdl_ObjectIdentity = ObjectIdentity
status_pdl = _Status_pdl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 3, 2)
)


class _Form_feed_needed_Type(Integer32):
    """Custom type form_feed_needed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eFalse", 1),
          ("eTrue", 2))
    )


_Form_feed_needed_Type.__name__ = "Integer32"
_Form_feed_needed_Object = MibScalar
form_feed_needed = _Form_feed_needed_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 3, 2, 2),
    _Form_feed_needed_Type()
)
form_feed_needed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    form_feed_needed.setStatus("optional")
_Pdl_pcl_ObjectIdentity = ObjectIdentity
pdl_pcl = _Pdl_pcl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 3, 3)
)
_Pcl_total_page_count_Type = Integer32
_Pcl_total_page_count_Object = MibScalar
pcl_total_page_count = _Pcl_total_page_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 3, 3, 5),
    _Pcl_total_page_count_Type()
)
pcl_total_page_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcl_total_page_count.setStatus("optional")


class _Pcl_default_font_source_Type(Integer32):
    """Custom type pcl_default_font_source based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              11,
              12,
              13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("eInternal", 1),
          ("ePermanentSoft", 2),
          ("eRomSimm2", 11),
          ("eRomSimm3", 12),
          ("eRomSimm4", 13),
          ("eRomSimm5", 14))
    )


_Pcl_default_font_source_Type.__name__ = "Integer32"
_Pcl_default_font_source_Object = MibScalar
pcl_default_font_source = _Pcl_default_font_source_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 3, 3, 14),
    _Pcl_default_font_source_Type()
)
pcl_default_font_source.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pcl_default_font_source.setStatus("optional")


class _Pcl_default_font_number_Type(Integer32):
    """Custom type pcl_default_font_number based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Pcl_default_font_number_Type.__name__ = "Integer32"
_Pcl_default_font_number_Object = MibScalar
pcl_default_font_number = _Pcl_default_font_number_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 3, 3, 15),
    _Pcl_default_font_number_Type()
)
pcl_default_font_number.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pcl_default_font_number.setStatus("optional")
_Pdl_postscript_ObjectIdentity = ObjectIdentity
pdl_postscript = _Pdl_postscript_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 3, 4)
)
_Postscript_total_page_count_Type = Integer32
_Postscript_total_page_count_Object = MibScalar
postscript_total_page_count = _Postscript_total_page_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 3, 4, 5),
    _Postscript_total_page_count_Type()
)
postscript_total_page_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    postscript_total_page_count.setStatus("optional")


class _Postscript_print_errors_Type(Integer32):
    """Custom type postscript_print_errors based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eOff", 1),
          ("eOn", 2))
    )


_Postscript_print_errors_Type.__name__ = "Integer32"
_Postscript_print_errors_Object = MibScalar
postscript_print_errors = _Postscript_print_errors_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 3, 4, 11),
    _Postscript_print_errors_Type()
)
postscript_print_errors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    postscript_print_errors.setStatus("optional")


class _Postscript_defer_media_Type(Integer32):
    """Custom type postscript_defer_media based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eDisabled", 1),
          ("eEnabled", 2))
    )


_Postscript_defer_media_Type.__name__ = "Integer32"
_Postscript_defer_media_Object = MibScalar
postscript_defer_media = _Postscript_defer_media_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 3, 4, 14),
    _Postscript_defer_media_Type()
)
postscript_defer_media.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    postscript_defer_media.setStatus("optional")
_Pdl_pdf_ObjectIdentity = ObjectIdentity
pdl_pdf = _Pdl_pdf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 3, 15)
)
_Pdf_version_Type = OctetString
_Pdf_version_Object = MibScalar
pdf_version = _Pdf_version_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 3, 15, 1),
    _Pdf_version_Type()
)
pdf_version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdf_version.setStatus("optional")
_Pdf_total_page_count_Type = Integer32
_Pdf_total_page_count_Object = MibScalar
pdf_total_page_count = _Pdf_total_page_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 3, 15, 2),
    _Pdf_total_page_count_Type()
)
pdf_total_page_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdf_total_page_count.setStatus("optional")


class _Pdf_enabled_Type(Integer32):
    """Custom type pdf_enabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ePDFEnabled", 2),
          ("ePDFNotEnabled", 1))
    )


_Pdf_enabled_Type.__name__ = "Integer32"
_Pdf_enabled_Object = MibScalar
pdf_enabled = _Pdf_enabled_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 3, 15, 3),
    _Pdf_enabled_Type()
)
pdf_enabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdf_enabled.setStatus("optional")


class _Pdf_print_errors_Type(Integer32):
    """Custom type pdf_print_errors based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eOff", 1),
          ("eOn", 2))
    )


_Pdf_print_errors_Type.__name__ = "Integer32"
_Pdf_print_errors_Object = MibScalar
pdf_print_errors = _Pdf_print_errors_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 3, 15, 4),
    _Pdf_print_errors_Type()
)
pdf_print_errors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdf_print_errors.setStatus("optional")
_Fax_proc_sub_ObjectIdentity = ObjectIdentity
fax_proc_sub = _Fax_proc_sub_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 7)
)
_Settings_fax_proc_sub_ObjectIdentity = ObjectIdentity
settings_fax_proc_sub = _Settings_fax_proc_sub_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 7, 1)
)
_Fax_print_page_count_Type = Integer32
_Fax_print_page_count_Object = MibScalar
fax_print_page_count = _Fax_print_page_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 7, 1, 32),
    _Fax_print_page_count_Type()
)
fax_print_page_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fax_print_page_count.setStatus("optional")
_Status_fax_proc_sub_ObjectIdentity = ObjectIdentity
status_fax_proc_sub = _Status_fax_proc_sub_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 7, 2)
)


class _Pcfax_send_enabled_Type(Integer32):
    """Custom type pcfax_send_enabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eDisabled", 1),
          ("eEnabled", 2))
    )


_Pcfax_send_enabled_Type.__name__ = "Integer32"
_Pcfax_send_enabled_Object = MibScalar
pcfax_send_enabled = _Pcfax_send_enabled_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 7, 2, 13),
    _Pcfax_send_enabled_Type()
)
pcfax_send_enabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcfax_send_enabled.setStatus("optional")


class _Pcfax_send_operational_Type(Integer32):
    """Custom type pcfax_send_operational based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eNonOperational", 1),
          ("eOperational", 2))
    )


_Pcfax_send_operational_Type.__name__ = "Integer32"
_Pcfax_send_operational_Object = MibScalar
pcfax_send_operational = _Pcfax_send_operational_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 7, 2, 14),
    _Pcfax_send_operational_Type()
)
pcfax_send_operational.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcfax_send_operational.setStatus("optional")


class _Fax_notification_available_Type(Integer32):
    """Custom type fax_notification_available based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eAvailable", 2),
          ("eNotAvailable", 1))
    )


_Fax_notification_available_Type.__name__ = "Integer32"
_Fax_notification_available_Object = MibScalar
fax_notification_available = _Fax_notification_available_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 7, 2, 15),
    _Fax_notification_available_Type()
)
fax_notification_available.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fax_notification_available.setStatus("optional")


class _Fax_billing_code_enabled_Type(Integer32):
    """Custom type fax_billing_code_enabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eDisabled", 1),
          ("eEnabled", 2))
    )


_Fax_billing_code_enabled_Type.__name__ = "Integer32"
_Fax_billing_code_enabled_Object = MibScalar
fax_billing_code_enabled = _Fax_billing_code_enabled_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 7, 2, 16),
    _Fax_billing_code_enabled_Type()
)
fax_billing_code_enabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fax_billing_code_enabled.setStatus("optional")
_Fax_billing_code_minlength_Type = Integer32
_Fax_billing_code_minlength_Object = MibScalar
fax_billing_code_minlength = _Fax_billing_code_minlength_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 7, 2, 17),
    _Fax_billing_code_minlength_Type()
)
fax_billing_code_minlength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fax_billing_code_minlength.setStatus("optional")
_Fax_billing_code_Type = OctetString
_Fax_billing_code_Object = MibScalar
fax_billing_code = _Fax_billing_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 7, 2, 18),
    _Fax_billing_code_Type()
)
fax_billing_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fax_billing_code.setStatus("optional")
_Webserver_proc_sub_ObjectIdentity = ObjectIdentity
webserver_proc_sub = _Webserver_proc_sub_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 9)
)
_Settings_webserver_ObjectIdentity = ObjectIdentity
settings_webserver = _Settings_webserver_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 9, 1)
)


class _Web_server_url_Type(OctetString):
    """Custom type web_server_url based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Web_server_url_Type.__name__ = "OctetString"
_Web_server_url_Object = MibScalar
web_server_url = _Web_server_url_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 9, 1, 2),
    _Web_server_url_Type()
)
web_server_url.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    web_server_url.setStatus("optional")
_Web_server_security_Type = OctetString
_Web_server_security_Object = MibScalar
web_server_security = _Web_server_security_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 9, 1, 3),
    _Web_server_security_Type()
)
web_server_security.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    web_server_security.setStatus("optional")
_Destination_subsystem_ObjectIdentity = ObjectIdentity
destination_subsystem = _Destination_subsystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4)
)
_Print_engine_ObjectIdentity = ObjectIdentity
print_engine = _Print_engine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1)
)
_Settings_prt_eng_ObjectIdentity = ObjectIdentity
settings_prt_eng = _Settings_prt_eng_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 1)
)
_Override_media_name_Type = OctetString
_Override_media_name_Object = MibScalar
override_media_name = _Override_media_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 1, 2),
    _Override_media_name_Type()
)
override_media_name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    override_media_name.setStatus("optional")


class _Override_media_size_Type(Integer32):
    """Custom type override_media_size based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              11,
              17,
              18,
              19,
              25,
              26,
              27,
              36,
              37,
              39,
              45,
              46,
              65,
              72,
              74,
              75,
              80,
              81,
              90,
              91,
              100,
              101,
              120,
              122,
              258,
              282,
              32767)
        )
    )
    namedValues = NamedValues(
        *(("eCommercial10", 81),
          ("eCustom", 101),
          ("eISOB5", 65),
          ("eISORA3", 39),
          ("eISORA4", 36),
          ("eISOSRA4", 37),
          ("eISOandJISA3", 27),
          ("eISOandJISA4", 26),
          ("eISOandJISA4R", 282),
          ("eISOandJISA5", 25),
          ("eIndexCard4x6", 74),
          ("eIndexCard5x7", 122),
          ("eIndexCard5x8", 75),
          ("eInternationalB5", 100),
          ("eInternationalC5", 91),
          ("eInternationalDL", 90),
          ("eJISB4", 46),
          ("eJISB5", 45),
          ("eJISExecutive", 18),
          ("eJapanesePostcardDouble", 72),
          ("eLedger", 11),
          ("eMonarch", 80),
          ("eROC16K", 17),
          ("eROC8K", 19),
          ("eTabloidExtra", 120),
          ("eUSExecutive", 1),
          ("eUSLegal", 3),
          ("eUSLetter", 2),
          ("eUSLetterR", 258),
          ("eUnknownMediaSize", 32767))
    )


_Override_media_size_Type.__name__ = "Integer32"
_Override_media_size_Object = MibScalar
override_media_size = _Override_media_size_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 1, 3),
    _Override_media_size_Type()
)
override_media_size.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    override_media_size.setStatus("optional")


class _Configurable_low_threshold_setting_Type(Integer32):
    """Custom type configurable_low_threshold_setting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Configurable_low_threshold_setting_Type.__name__ = "Integer32"
_Configurable_low_threshold_setting_Object = MibScalar
configurable_low_threshold_setting = _Configurable_low_threshold_setting_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 1, 24),
    _Configurable_low_threshold_setting_Type()
)
configurable_low_threshold_setting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configurable_low_threshold_setting.setStatus("optional")
_Cartridge_out_override_control_Type = Integer32
_Cartridge_out_override_control_Object = MibScalar
cartridge_out_override_control = _Cartridge_out_override_control_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 1, 27),
    _Cartridge_out_override_control_Type()
)
cartridge_out_override_control.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    cartridge_out_override_control.setStatus("optional")


class _Duplex_blank_pages_Type(Integer32):
    """Custom type duplex_blank_pages based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eDuplexBlankPagesAuto", 1),
          ("eDuplexBlankPagesYes", 2))
    )


_Duplex_blank_pages_Type.__name__ = "Integer32"
_Duplex_blank_pages_Object = MibScalar
duplex_blank_pages = _Duplex_blank_pages_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 1, 28),
    _Duplex_blank_pages_Type()
)
duplex_blank_pages.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    duplex_blank_pages.setStatus("optional")
_Finisher_image_rotation_Type = OctetString
_Finisher_image_rotation_Object = MibScalar
finisher_image_rotation = _Finisher_image_rotation_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 1, 31),
    _Finisher_image_rotation_Type()
)
finisher_image_rotation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    finisher_image_rotation.setStatus("optional")
_Status_prt_eng_ObjectIdentity = ObjectIdentity
status_prt_eng = _Status_prt_eng_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 2)
)
_Total_engine_page_count_Type = Integer32
_Total_engine_page_count_Object = MibScalar
total_engine_page_count = _Total_engine_page_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 2, 5),
    _Total_engine_page_count_Type()
)
total_engine_page_count.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    total_engine_page_count.setStatus("optional")
_Total_color_page_count_Type = Integer32
_Total_color_page_count_Object = MibScalar
total_color_page_count = _Total_color_page_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 2, 7),
    _Total_color_page_count_Type()
)
total_color_page_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    total_color_page_count.setStatus("optional")
_Duplex_page_count_Type = Integer32
_Duplex_page_count_Object = MibScalar
duplex_page_count = _Duplex_page_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 2, 22),
    _Duplex_page_count_Type()
)
duplex_page_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    duplex_page_count.setStatus("optional")


class _Print_engine_revision_Type(OctetString):
    """Custom type print_engine_revision based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Print_engine_revision_Type.__name__ = "OctetString"
_Print_engine_revision_Object = MibScalar
print_engine_revision = _Print_engine_revision_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 2, 26),
    _Print_engine_revision_Type()
)
print_engine_revision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    print_engine_revision.setStatus("optional")
_Printer_calibration_dhalf_ObjectIdentity = ObjectIdentity
printer_calibration_dhalf = _Printer_calibration_dhalf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 2, 37)
)
_Printer_cal_dhalf_page_count_Type = Integer32
_Printer_cal_dhalf_page_count_Object = MibScalar
printer_cal_dhalf_page_count = _Printer_cal_dhalf_page_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 2, 37, 1),
    _Printer_cal_dhalf_page_count_Type()
)
printer_cal_dhalf_page_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    printer_cal_dhalf_page_count.setStatus("optional")
_Printer_cal_dhalf_utc_Type = Integer32
_Printer_cal_dhalf_utc_Object = MibScalar
printer_cal_dhalf_utc = _Printer_cal_dhalf_utc_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 2, 37, 2),
    _Printer_cal_dhalf_utc_Type()
)
printer_cal_dhalf_utc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    printer_cal_dhalf_utc.setStatus("optional")
_Printer_calibration_cpr_ObjectIdentity = ObjectIdentity
printer_calibration_cpr = _Printer_calibration_cpr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 2, 38)
)
_Printer_cal_cpr_page_count_Type = Integer32
_Printer_cal_cpr_page_count_Object = MibScalar
printer_cal_cpr_page_count = _Printer_cal_cpr_page_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 2, 38, 1),
    _Printer_cal_cpr_page_count_Type()
)
printer_cal_cpr_page_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    printer_cal_cpr_page_count.setStatus("optional")
_Printer_cal_cpr_utc_Type = Integer32
_Printer_cal_cpr_utc_Object = MibScalar
printer_cal_cpr_utc = _Printer_cal_cpr_utc_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 2, 38, 2),
    _Printer_cal_cpr_utc_Type()
)
printer_cal_cpr_utc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    printer_cal_cpr_utc.setStatus("optional")
_Intray_ObjectIdentity = ObjectIdentity
intray = _Intray_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 3)
)
_Settings_intray_ObjectIdentity = ObjectIdentity
settings_intray = _Settings_intray_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 3, 1)
)


class _Input_tray_auto_select_Type(Integer32):
    """Custom type input_tray_auto_select based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eOff", 1),
          ("eOn", 2))
    )


_Input_tray_auto_select_Type.__name__ = "Integer32"
_Input_tray_auto_select_Object = MibScalar
input_tray_auto_select = _Input_tray_auto_select_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 3, 1, 2),
    _Input_tray_auto_select_Type()
)
input_tray_auto_select.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    input_tray_auto_select.setStatus("optional")
_Custom_paper_feed_dim_Type = Integer32
_Custom_paper_feed_dim_Object = MibScalar
custom_paper_feed_dim = _Custom_paper_feed_dim_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 3, 1, 8),
    _Custom_paper_feed_dim_Type()
)
custom_paper_feed_dim.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    custom_paper_feed_dim.setStatus("optional")
_Custom_paper_xfeed_dim_Type = Integer32
_Custom_paper_xfeed_dim_Object = MibScalar
custom_paper_xfeed_dim = _Custom_paper_xfeed_dim_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 3, 1, 9),
    _Custom_paper_xfeed_dim_Type()
)
custom_paper_xfeed_dim.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    custom_paper_xfeed_dim.setStatus("optional")


class _Default_custom_paper_dim_unit_Type(Integer32):
    """Custom type default_custom_paper_dim_unit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("eMicrometers", 4),
          ("eTenThousandthsOfInches", 3))
    )


_Default_custom_paper_dim_unit_Type.__name__ = "Integer32"
_Default_custom_paper_dim_unit_Object = MibScalar
default_custom_paper_dim_unit = _Default_custom_paper_dim_unit_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 3, 1, 10),
    _Default_custom_paper_dim_unit_Type()
)
default_custom_paper_dim_unit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    default_custom_paper_dim_unit.setStatus("optional")
_Default_custom_paper_feed_dim_Type = Integer32
_Default_custom_paper_feed_dim_Object = MibScalar
default_custom_paper_feed_dim = _Default_custom_paper_feed_dim_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 3, 1, 11),
    _Default_custom_paper_feed_dim_Type()
)
default_custom_paper_feed_dim.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    default_custom_paper_feed_dim.setStatus("optional")
_Default_custom_paper_xfeed_dim_Type = Integer32
_Default_custom_paper_xfeed_dim_Object = MibScalar
default_custom_paper_xfeed_dim = _Default_custom_paper_xfeed_dim_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 3, 1, 12),
    _Default_custom_paper_xfeed_dim_Type()
)
default_custom_paper_xfeed_dim.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    default_custom_paper_xfeed_dim.setStatus("optional")
_Input_tray_max_media_feed_dim_Type = Integer32
_Input_tray_max_media_feed_dim_Object = MibScalar
input_tray_max_media_feed_dim = _Input_tray_max_media_feed_dim_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 3, 1, 14),
    _Input_tray_max_media_feed_dim_Type()
)
input_tray_max_media_feed_dim.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    input_tray_max_media_feed_dim.setStatus("optional")
_Input_tray_max_media_xfeed_dim_Type = Integer32
_Input_tray_max_media_xfeed_dim_Object = MibScalar
input_tray_max_media_xfeed_dim = _Input_tray_max_media_xfeed_dim_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 3, 1, 15),
    _Input_tray_max_media_xfeed_dim_Type()
)
input_tray_max_media_xfeed_dim.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    input_tray_max_media_xfeed_dim.setStatus("optional")
_Input_tray_min_media_feed_dim_Type = Integer32
_Input_tray_min_media_feed_dim_Object = MibScalar
input_tray_min_media_feed_dim = _Input_tray_min_media_feed_dim_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 3, 1, 16),
    _Input_tray_min_media_feed_dim_Type()
)
input_tray_min_media_feed_dim.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    input_tray_min_media_feed_dim.setStatus("optional")
_Input_tray_min_media_xfeed_dim_Type = Integer32
_Input_tray_min_media_xfeed_dim_Object = MibScalar
input_tray_min_media_xfeed_dim = _Input_tray_min_media_xfeed_dim_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 3, 1, 17),
    _Input_tray_min_media_xfeed_dim_Type()
)
input_tray_min_media_xfeed_dim.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    input_tray_min_media_xfeed_dim.setStatus("optional")


class _Tray_prompt_Type(Integer32):
    """Custom type tray_prompt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eDisplay", 2),
          ("eDoNotDisplay", 1))
    )


_Tray_prompt_Type.__name__ = "Integer32"
_Tray_prompt_Object = MibScalar
tray_prompt = _Tray_prompt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 3, 1, 19),
    _Tray_prompt_Type()
)
tray_prompt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tray_prompt.setStatus("optional")
_Intrays_ObjectIdentity = ObjectIdentity
intrays = _Intrays_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 3, 3)
)
_Intray1_ObjectIdentity = ObjectIdentity
intray1 = _Intray1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 3, 3, 1)
)


class _Tray1_media_size_loaded_Type(Integer32):
    """Custom type tray1_media_size_loaded based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              10,
              11,
              15,
              17,
              19,
              25,
              26,
              27,
              36,
              37,
              39,
              44,
              45,
              46,
              74,
              75,
              101,
              120,
              122,
              32764,
              32765)
        )
    )
    namedValues = NamedValues(
        *(("eAnyCustomSize", 32764),
          ("eAnySize", 32765),
          ("eCustom", 101),
          ("eFoolscap", 10),
          ("eISORA3", 39),
          ("eISORA4", 36),
          ("eISOSRA4", 37),
          ("eISOandJISA3", 27),
          ("eISOandJISA4", 26),
          ("eISOandJISA5", 25),
          ("eIndexCard4x6", 74),
          ("eIndexCard5x7", 122),
          ("eIndexCard5x8", 75),
          ("eJISB4", 46),
          ("eJISB5", 45),
          ("eJISB6", 44),
          ("eLedger", 11),
          ("eROC16K", 17),
          ("eROC8K", 19),
          ("eStatement", 15),
          ("eTabloidExtra", 120),
          ("eUSExecutive", 1),
          ("eUSLegal", 3),
          ("eUSLetter", 2))
    )


_Tray1_media_size_loaded_Type.__name__ = "Integer32"
_Tray1_media_size_loaded_Object = MibScalar
tray1_media_size_loaded = _Tray1_media_size_loaded_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 3, 3, 1, 1),
    _Tray1_media_size_loaded_Type()
)
tray1_media_size_loaded.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tray1_media_size_loaded.setStatus("optional")
_Tray1_phd_Type = Integer32
_Tray1_phd_Object = MibScalar
tray1_phd = _Tray1_phd_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 3, 3, 1, 12),
    _Tray1_phd_Type()
)
tray1_phd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tray1_phd.setStatus("optional")
_Intray2_ObjectIdentity = ObjectIdentity
intray2 = _Intray2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 3, 3, 2)
)


class _Tray2_media_size_loaded_Type(Integer32):
    """Custom type tray2_media_size_loaded based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              10,
              11,
              15,
              25,
              26,
              27,
              45,
              46)
        )
    )
    namedValues = NamedValues(
        *(("eFoolscap", 10),
          ("eISOandJISA3", 27),
          ("eISOandJISA4", 26),
          ("eISOandJISA5", 25),
          ("eJISB4", 46),
          ("eJISB5", 45),
          ("eLedger", 11),
          ("eStatement", 15),
          ("eUSExecutive", 1),
          ("eUSLegal", 3),
          ("eUSLetter", 2))
    )


_Tray2_media_size_loaded_Type.__name__ = "Integer32"
_Tray2_media_size_loaded_Object = MibScalar
tray2_media_size_loaded = _Tray2_media_size_loaded_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 3, 3, 2, 1),
    _Tray2_media_size_loaded_Type()
)
tray2_media_size_loaded.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tray2_media_size_loaded.setStatus("optional")
_Tray2_phd_Type = Integer32
_Tray2_phd_Object = MibScalar
tray2_phd = _Tray2_phd_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 3, 3, 2, 12),
    _Tray2_phd_Type()
)
tray2_phd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tray2_phd.setStatus("optional")
_Intray3_ObjectIdentity = ObjectIdentity
intray3 = _Intray3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 3, 3, 3)
)


class _Tray3_media_size_loaded_Type(Integer32):
    """Custom type tray3_media_size_loaded based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              10,
              11,
              15,
              25,
              26,
              27,
              45,
              46)
        )
    )
    namedValues = NamedValues(
        *(("eFoolscap", 10),
          ("eISOandJISA3", 27),
          ("eISOandJISA4", 26),
          ("eISOandJISA5", 25),
          ("eJISB4", 46),
          ("eJISB5", 45),
          ("eLedger", 11),
          ("eStatement", 15),
          ("eUSExecutive", 1),
          ("eUSLegal", 3),
          ("eUSLetter", 2))
    )


_Tray3_media_size_loaded_Type.__name__ = "Integer32"
_Tray3_media_size_loaded_Object = MibScalar
tray3_media_size_loaded = _Tray3_media_size_loaded_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 3, 3, 3, 1),
    _Tray3_media_size_loaded_Type()
)
tray3_media_size_loaded.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tray3_media_size_loaded.setStatus("optional")
_Tray3_phd_Type = Integer32
_Tray3_phd_Object = MibScalar
tray3_phd = _Tray3_phd_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 3, 3, 3, 12),
    _Tray3_phd_Type()
)
tray3_phd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tray3_phd.setStatus("optional")
_Intray5_ObjectIdentity = ObjectIdentity
intray5 = _Intray5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 3, 3, 5)
)


class _Tray5_media_size_loaded_Type(Integer32):
    """Custom type tray5_media_size_loaded based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              26)
        )
    )
    namedValues = NamedValues(
        *(("eISOandJISA4", 26),
          ("eUSLetter", 2))
    )


_Tray5_media_size_loaded_Type.__name__ = "Integer32"
_Tray5_media_size_loaded_Object = MibScalar
tray5_media_size_loaded = _Tray5_media_size_loaded_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 3, 3, 5, 1),
    _Tray5_media_size_loaded_Type()
)
tray5_media_size_loaded.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tray5_media_size_loaded.setStatus("optional")
_Tray5_phd_Type = Integer32
_Tray5_phd_Object = MibScalar
tray5_phd = _Tray5_phd_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 3, 3, 5, 12),
    _Tray5_phd_Type()
)
tray5_phd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tray5_phd.setStatus("optional")
_Intray6_ObjectIdentity = ObjectIdentity
intray6 = _Intray6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 3, 3, 6)
)


class _Tray6_media_size_loaded_Type(Integer32):
    """Custom type tray6_media_size_loaded based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              26)
        )
    )
    namedValues = NamedValues(
        *(("eISOandJISA4", 26),
          ("eUSLetter", 2))
    )


_Tray6_media_size_loaded_Type.__name__ = "Integer32"
_Tray6_media_size_loaded_Object = MibScalar
tray6_media_size_loaded = _Tray6_media_size_loaded_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 3, 3, 6, 1),
    _Tray6_media_size_loaded_Type()
)
tray6_media_size_loaded.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tray6_media_size_loaded.setStatus("optional")
_Tray6_phd_Type = Integer32
_Tray6_phd_Object = MibScalar
tray6_phd = _Tray6_phd_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 3, 3, 6, 12),
    _Tray6_phd_Type()
)
tray6_phd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tray6_phd.setStatus("optional")
_Outbin_ObjectIdentity = ObjectIdentity
outbin = _Outbin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 4)
)
_Settings_outbin_ObjectIdentity = ObjectIdentity
settings_outbin = _Settings_outbin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 4, 1)
)
_Overflow_bin_Type = Integer32
_Overflow_bin_Object = MibScalar
overflow_bin = _Overflow_bin_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 4, 1, 4),
    _Overflow_bin_Type()
)
overflow_bin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    overflow_bin.setStatus("optional")
_Outbins_ObjectIdentity = ObjectIdentity
outbins = _Outbins_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 4, 3)
)
_Outbin1_ObjectIdentity = ObjectIdentity
outbin1 = _Outbin1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 4, 3, 1)
)
_Outbin1_override_mode_Type = OctetString
_Outbin1_override_mode_Object = MibScalar
outbin1_override_mode = _Outbin1_override_mode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 4, 3, 1, 9),
    _Outbin1_override_mode_Type()
)
outbin1_override_mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outbin1_override_mode.setStatus("optional")
_Outbin1_maximum_binding_Type = Integer32
_Outbin1_maximum_binding_Object = MibScalar
outbin1_maximum_binding = _Outbin1_maximum_binding_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 4, 3, 1, 10),
    _Outbin1_maximum_binding_Type()
)
outbin1_maximum_binding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outbin1_maximum_binding.setStatus("optional")
_Outbin1_phd_Type = Integer32
_Outbin1_phd_Object = MibScalar
outbin1_phd = _Outbin1_phd_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 4, 3, 1, 11),
    _Outbin1_phd_Type()
)
outbin1_phd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outbin1_phd.setStatus("optional")
_Outbin1_error_info_Type = OctetString
_Outbin1_error_info_Object = MibScalar
outbin1_error_info = _Outbin1_error_info_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 4, 3, 1, 12),
    _Outbin1_error_info_Type()
)
outbin1_error_info.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outbin1_error_info.setStatus("optional")
_Outbin2_ObjectIdentity = ObjectIdentity
outbin2 = _Outbin2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 4, 3, 2)
)
_Outbin2_override_mode_Type = OctetString
_Outbin2_override_mode_Object = MibScalar
outbin2_override_mode = _Outbin2_override_mode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 4, 3, 2, 9),
    _Outbin2_override_mode_Type()
)
outbin2_override_mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outbin2_override_mode.setStatus("optional")
_Outbin2_maximum_binding_Type = Integer32
_Outbin2_maximum_binding_Object = MibScalar
outbin2_maximum_binding = _Outbin2_maximum_binding_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 4, 3, 2, 10),
    _Outbin2_maximum_binding_Type()
)
outbin2_maximum_binding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outbin2_maximum_binding.setStatus("optional")
_Outbin2_phd_Type = Integer32
_Outbin2_phd_Object = MibScalar
outbin2_phd = _Outbin2_phd_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 4, 3, 2, 11),
    _Outbin2_phd_Type()
)
outbin2_phd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outbin2_phd.setStatus("optional")
_Outbin2_error_info_Type = OctetString
_Outbin2_error_info_Object = MibScalar
outbin2_error_info = _Outbin2_error_info_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 4, 3, 2, 12),
    _Outbin2_error_info_Type()
)
outbin2_error_info.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outbin2_error_info.setStatus("optional")
_Outbin3_ObjectIdentity = ObjectIdentity
outbin3 = _Outbin3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 4, 3, 3)
)
_Outbin3_override_mode_Type = OctetString
_Outbin3_override_mode_Object = MibScalar
outbin3_override_mode = _Outbin3_override_mode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 4, 3, 3, 9),
    _Outbin3_override_mode_Type()
)
outbin3_override_mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outbin3_override_mode.setStatus("optional")
_Outbin3_maximum_binding_Type = Integer32
_Outbin3_maximum_binding_Object = MibScalar
outbin3_maximum_binding = _Outbin3_maximum_binding_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 4, 3, 3, 10),
    _Outbin3_maximum_binding_Type()
)
outbin3_maximum_binding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outbin3_maximum_binding.setStatus("optional")
_Outbin3_phd_Type = Integer32
_Outbin3_phd_Object = MibScalar
outbin3_phd = _Outbin3_phd_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 4, 3, 3, 11),
    _Outbin3_phd_Type()
)
outbin3_phd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outbin3_phd.setStatus("optional")
_Outbin3_error_info_Type = OctetString
_Outbin3_error_info_Object = MibScalar
outbin3_error_info = _Outbin3_error_info_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 4, 3, 3, 12),
    _Outbin3_error_info_Type()
)
outbin3_error_info.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outbin3_error_info.setStatus("optional")
_Outbin4_ObjectIdentity = ObjectIdentity
outbin4 = _Outbin4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 4, 3, 4)
)
_Outbin4_override_mode_Type = OctetString
_Outbin4_override_mode_Object = MibScalar
outbin4_override_mode = _Outbin4_override_mode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 4, 3, 4, 9),
    _Outbin4_override_mode_Type()
)
outbin4_override_mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outbin4_override_mode.setStatus("optional")
_Outbin4_maximum_binding_Type = Integer32
_Outbin4_maximum_binding_Object = MibScalar
outbin4_maximum_binding = _Outbin4_maximum_binding_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 4, 3, 4, 10),
    _Outbin4_maximum_binding_Type()
)
outbin4_maximum_binding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outbin4_maximum_binding.setStatus("optional")
_Outbin4_phd_Type = Integer32
_Outbin4_phd_Object = MibScalar
outbin4_phd = _Outbin4_phd_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 4, 3, 4, 11),
    _Outbin4_phd_Type()
)
outbin4_phd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outbin4_phd.setStatus("optional")
_Outbin4_error_info_Type = OctetString
_Outbin4_error_info_Object = MibScalar
outbin4_error_info = _Outbin4_error_info_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 4, 3, 4, 12),
    _Outbin4_error_info_Type()
)
outbin4_error_info.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outbin4_error_info.setStatus("optional")
_Outbin5_ObjectIdentity = ObjectIdentity
outbin5 = _Outbin5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 4, 3, 5)
)
_Outbin5_override_mode_Type = OctetString
_Outbin5_override_mode_Object = MibScalar
outbin5_override_mode = _Outbin5_override_mode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 4, 3, 5, 9),
    _Outbin5_override_mode_Type()
)
outbin5_override_mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outbin5_override_mode.setStatus("optional")
_Outbin5_maximum_binding_Type = Integer32
_Outbin5_maximum_binding_Object = MibScalar
outbin5_maximum_binding = _Outbin5_maximum_binding_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 4, 3, 5, 10),
    _Outbin5_maximum_binding_Type()
)
outbin5_maximum_binding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outbin5_maximum_binding.setStatus("optional")
_Outbin5_phd_Type = Integer32
_Outbin5_phd_Object = MibScalar
outbin5_phd = _Outbin5_phd_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 4, 3, 5, 11),
    _Outbin5_phd_Type()
)
outbin5_phd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outbin5_phd.setStatus("optional")
_Outbin5_error_info_Type = OctetString
_Outbin5_error_info_Object = MibScalar
outbin5_error_info = _Outbin5_error_info_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 4, 3, 5, 12),
    _Outbin5_error_info_Type()
)
outbin5_error_info.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outbin5_error_info.setStatus("optional")
_Imaging_ObjectIdentity = ObjectIdentity
imaging = _Imaging_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 6)
)


class _Print_quality_level_Type(Integer32):
    """Custom type print_quality_level based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("eBestPQ", 3),
          ("eDraftPQ", 1),
          ("eNormal", 2))
    )


_Print_quality_level_Type.__name__ = "Integer32"
_Print_quality_level_Object = MibScalar
print_quality_level = _Print_quality_level_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 6, 9),
    _Print_quality_level_Type()
)
print_quality_level.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    print_quality_level.setStatus("optional")
_Ph_ObjectIdentity = ObjectIdentity
ph = _Ph_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 7)
)
_Settings_ph_ObjectIdentity = ObjectIdentity
settings_ph = _Settings_ph_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 7, 1)
)


class _Tray_disable_use_instead_Type(Integer32):
    """Custom type tray_disable_use_instead based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eDisabled", 1),
          ("eEnabled", 2))
    )


_Tray_disable_use_instead_Type.__name__ = "Integer32"
_Tray_disable_use_instead_Object = MibScalar
tray_disable_use_instead = _Tray_disable_use_instead_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 7, 1, 1),
    _Tray_disable_use_instead_Type()
)
tray_disable_use_instead.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tray_disable_use_instead.setStatus("optional")
_Ph_devices_ObjectIdentity = ObjectIdentity
ph_devices = _Ph_devices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 7, 3)
)
_Ph2_ObjectIdentity = ObjectIdentity
ph2 = _Ph2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 7, 3, 2)
)
_Phd2_device_specific_command_Type = OctetString
_Phd2_device_specific_command_Object = MibScalar
phd2_device_specific_command = _Phd2_device_specific_command_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 7, 3, 2, 2),
    _Phd2_device_specific_command_Type()
)
phd2_device_specific_command.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    phd2_device_specific_command.setStatus("optional")
_Print_media_ObjectIdentity = ObjectIdentity
print_media = _Print_media_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8)
)
_Settings_print_media_ObjectIdentity = ObjectIdentity
settings_print_media = _Settings_print_media_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 1)
)
_Media_names_available_Type = OctetString
_Media_names_available_Object = MibScalar
media_names_available = _Media_names_available_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 1, 1),
    _Media_names_available_Type()
)
media_names_available.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    media_names_available.setStatus("optional")
_North_edge_offset_Type = Integer32
_North_edge_offset_Object = MibScalar
north_edge_offset = _North_edge_offset_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 1, 2),
    _North_edge_offset_Type()
)
north_edge_offset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    north_edge_offset.setStatus("optional")
_Media_info_ObjectIdentity = ObjectIdentity
media_info = _Media_info_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3)
)
_Media1_ObjectIdentity = ObjectIdentity
media1 = _Media1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 1)
)


class _Media1_name_Type(OctetString):
    """Custom type media1_name based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 24),
    )


_Media1_name_Type.__name__ = "OctetString"
_Media1_name_Object = MibScalar
media1_name = _Media1_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 1, 1),
    _Media1_name_Type()
)
media1_name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    media1_name.setStatus("optional")


class _Media1_short_name_Type(OctetString):
    """Custom type media1_short_name based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 9),
    )


_Media1_short_name_Type.__name__ = "OctetString"
_Media1_short_name_Object = MibScalar
media1_short_name = _Media1_short_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 1, 2),
    _Media1_short_name_Type()
)
media1_short_name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    media1_short_name.setStatus("optional")
_Media1_page_count_Type = Integer32
_Media1_page_count_Object = MibScalar
media1_page_count = _Media1_page_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 1, 3),
    _Media1_page_count_Type()
)
media1_page_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    media1_page_count.setStatus("optional")
_Media2_ObjectIdentity = ObjectIdentity
media2 = _Media2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 2)
)


class _Media2_name_Type(OctetString):
    """Custom type media2_name based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 24),
    )


_Media2_name_Type.__name__ = "OctetString"
_Media2_name_Object = MibScalar
media2_name = _Media2_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 2, 1),
    _Media2_name_Type()
)
media2_name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    media2_name.setStatus("optional")


class _Media2_short_name_Type(OctetString):
    """Custom type media2_short_name based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 9),
    )


_Media2_short_name_Type.__name__ = "OctetString"
_Media2_short_name_Object = MibScalar
media2_short_name = _Media2_short_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 2, 2),
    _Media2_short_name_Type()
)
media2_short_name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    media2_short_name.setStatus("optional")
_Media2_page_count_Type = Integer32
_Media2_page_count_Object = MibScalar
media2_page_count = _Media2_page_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 2, 3),
    _Media2_page_count_Type()
)
media2_page_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    media2_page_count.setStatus("optional")
_Media3_ObjectIdentity = ObjectIdentity
media3 = _Media3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 3)
)


class _Media3_name_Type(OctetString):
    """Custom type media3_name based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 24),
    )


_Media3_name_Type.__name__ = "OctetString"
_Media3_name_Object = MibScalar
media3_name = _Media3_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 3, 1),
    _Media3_name_Type()
)
media3_name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    media3_name.setStatus("optional")


class _Media3_short_name_Type(OctetString):
    """Custom type media3_short_name based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 9),
    )


_Media3_short_name_Type.__name__ = "OctetString"
_Media3_short_name_Object = MibScalar
media3_short_name = _Media3_short_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 3, 2),
    _Media3_short_name_Type()
)
media3_short_name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    media3_short_name.setStatus("optional")
_Media3_page_count_Type = Integer32
_Media3_page_count_Object = MibScalar
media3_page_count = _Media3_page_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 3, 3),
    _Media3_page_count_Type()
)
media3_page_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    media3_page_count.setStatus("optional")
_Media4_ObjectIdentity = ObjectIdentity
media4 = _Media4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 4)
)


class _Media4_name_Type(OctetString):
    """Custom type media4_name based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 24),
    )


_Media4_name_Type.__name__ = "OctetString"
_Media4_name_Object = MibScalar
media4_name = _Media4_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 4, 1),
    _Media4_name_Type()
)
media4_name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    media4_name.setStatus("optional")


class _Media4_short_name_Type(OctetString):
    """Custom type media4_short_name based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 9),
    )


_Media4_short_name_Type.__name__ = "OctetString"
_Media4_short_name_Object = MibScalar
media4_short_name = _Media4_short_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 4, 2),
    _Media4_short_name_Type()
)
media4_short_name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    media4_short_name.setStatus("optional")
_Media4_page_count_Type = Integer32
_Media4_page_count_Object = MibScalar
media4_page_count = _Media4_page_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 4, 3),
    _Media4_page_count_Type()
)
media4_page_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    media4_page_count.setStatus("optional")
_Media5_ObjectIdentity = ObjectIdentity
media5 = _Media5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 5)
)


class _Media5_name_Type(OctetString):
    """Custom type media5_name based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 24),
    )


_Media5_name_Type.__name__ = "OctetString"
_Media5_name_Object = MibScalar
media5_name = _Media5_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 5, 1),
    _Media5_name_Type()
)
media5_name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    media5_name.setStatus("optional")


class _Media5_short_name_Type(OctetString):
    """Custom type media5_short_name based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 9),
    )


_Media5_short_name_Type.__name__ = "OctetString"
_Media5_short_name_Object = MibScalar
media5_short_name = _Media5_short_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 5, 2),
    _Media5_short_name_Type()
)
media5_short_name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    media5_short_name.setStatus("optional")
_Media5_page_count_Type = Integer32
_Media5_page_count_Object = MibScalar
media5_page_count = _Media5_page_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 5, 3),
    _Media5_page_count_Type()
)
media5_page_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    media5_page_count.setStatus("optional")
_Media6_ObjectIdentity = ObjectIdentity
media6 = _Media6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 6)
)


class _Media6_name_Type(OctetString):
    """Custom type media6_name based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 24),
    )


_Media6_name_Type.__name__ = "OctetString"
_Media6_name_Object = MibScalar
media6_name = _Media6_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 6, 1),
    _Media6_name_Type()
)
media6_name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    media6_name.setStatus("optional")


class _Media6_short_name_Type(OctetString):
    """Custom type media6_short_name based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 9),
    )


_Media6_short_name_Type.__name__ = "OctetString"
_Media6_short_name_Object = MibScalar
media6_short_name = _Media6_short_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 6, 2),
    _Media6_short_name_Type()
)
media6_short_name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    media6_short_name.setStatus("optional")
_Media6_page_count_Type = Integer32
_Media6_page_count_Object = MibScalar
media6_page_count = _Media6_page_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 6, 3),
    _Media6_page_count_Type()
)
media6_page_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    media6_page_count.setStatus("optional")
_Media7_ObjectIdentity = ObjectIdentity
media7 = _Media7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 7)
)


class _Media7_name_Type(OctetString):
    """Custom type media7_name based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 24),
    )


_Media7_name_Type.__name__ = "OctetString"
_Media7_name_Object = MibScalar
media7_name = _Media7_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 7, 1),
    _Media7_name_Type()
)
media7_name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    media7_name.setStatus("optional")


class _Media7_short_name_Type(OctetString):
    """Custom type media7_short_name based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 9),
    )


_Media7_short_name_Type.__name__ = "OctetString"
_Media7_short_name_Object = MibScalar
media7_short_name = _Media7_short_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 7, 2),
    _Media7_short_name_Type()
)
media7_short_name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    media7_short_name.setStatus("optional")
_Media7_page_count_Type = Integer32
_Media7_page_count_Object = MibScalar
media7_page_count = _Media7_page_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 7, 3),
    _Media7_page_count_Type()
)
media7_page_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    media7_page_count.setStatus("optional")
_Media8_ObjectIdentity = ObjectIdentity
media8 = _Media8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 8)
)


class _Media8_name_Type(OctetString):
    """Custom type media8_name based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 24),
    )


_Media8_name_Type.__name__ = "OctetString"
_Media8_name_Object = MibScalar
media8_name = _Media8_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 8, 1),
    _Media8_name_Type()
)
media8_name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    media8_name.setStatus("optional")


class _Media8_short_name_Type(OctetString):
    """Custom type media8_short_name based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 9),
    )


_Media8_short_name_Type.__name__ = "OctetString"
_Media8_short_name_Object = MibScalar
media8_short_name = _Media8_short_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 8, 2),
    _Media8_short_name_Type()
)
media8_short_name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    media8_short_name.setStatus("optional")
_Media8_page_count_Type = Integer32
_Media8_page_count_Object = MibScalar
media8_page_count = _Media8_page_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 8, 3),
    _Media8_page_count_Type()
)
media8_page_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    media8_page_count.setStatus("optional")
_Media9_ObjectIdentity = ObjectIdentity
media9 = _Media9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 9)
)


class _Media9_name_Type(OctetString):
    """Custom type media9_name based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 24),
    )


_Media9_name_Type.__name__ = "OctetString"
_Media9_name_Object = MibScalar
media9_name = _Media9_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 9, 1),
    _Media9_name_Type()
)
media9_name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    media9_name.setStatus("optional")


class _Media9_short_name_Type(OctetString):
    """Custom type media9_short_name based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 9),
    )


_Media9_short_name_Type.__name__ = "OctetString"
_Media9_short_name_Object = MibScalar
media9_short_name = _Media9_short_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 9, 2),
    _Media9_short_name_Type()
)
media9_short_name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    media9_short_name.setStatus("optional")
_Media9_page_count_Type = Integer32
_Media9_page_count_Object = MibScalar
media9_page_count = _Media9_page_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 9, 3),
    _Media9_page_count_Type()
)
media9_page_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    media9_page_count.setStatus("optional")
_Media10_ObjectIdentity = ObjectIdentity
media10 = _Media10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 10)
)


class _Media10_name_Type(OctetString):
    """Custom type media10_name based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 24),
    )


_Media10_name_Type.__name__ = "OctetString"
_Media10_name_Object = MibScalar
media10_name = _Media10_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 10, 1),
    _Media10_name_Type()
)
media10_name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    media10_name.setStatus("optional")


class _Media10_short_name_Type(OctetString):
    """Custom type media10_short_name based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 9),
    )


_Media10_short_name_Type.__name__ = "OctetString"
_Media10_short_name_Object = MibScalar
media10_short_name = _Media10_short_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 10, 2),
    _Media10_short_name_Type()
)
media10_short_name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    media10_short_name.setStatus("optional")
_Media10_page_count_Type = Integer32
_Media10_page_count_Object = MibScalar
media10_page_count = _Media10_page_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 10, 3),
    _Media10_page_count_Type()
)
media10_page_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    media10_page_count.setStatus("optional")
_Media11_ObjectIdentity = ObjectIdentity
media11 = _Media11_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 11)
)


class _Media11_name_Type(OctetString):
    """Custom type media11_name based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 24),
    )


_Media11_name_Type.__name__ = "OctetString"
_Media11_name_Object = MibScalar
media11_name = _Media11_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 11, 1),
    _Media11_name_Type()
)
media11_name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    media11_name.setStatus("optional")


class _Media11_short_name_Type(OctetString):
    """Custom type media11_short_name based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 9),
    )


_Media11_short_name_Type.__name__ = "OctetString"
_Media11_short_name_Object = MibScalar
media11_short_name = _Media11_short_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 11, 2),
    _Media11_short_name_Type()
)
media11_short_name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    media11_short_name.setStatus("optional")
_Media11_page_count_Type = Integer32
_Media11_page_count_Object = MibScalar
media11_page_count = _Media11_page_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 11, 3),
    _Media11_page_count_Type()
)
media11_page_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    media11_page_count.setStatus("optional")
_Media12_ObjectIdentity = ObjectIdentity
media12 = _Media12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 12)
)


class _Media12_name_Type(OctetString):
    """Custom type media12_name based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 24),
    )


_Media12_name_Type.__name__ = "OctetString"
_Media12_name_Object = MibScalar
media12_name = _Media12_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 12, 1),
    _Media12_name_Type()
)
media12_name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    media12_name.setStatus("optional")


class _Media12_short_name_Type(OctetString):
    """Custom type media12_short_name based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 9),
    )


_Media12_short_name_Type.__name__ = "OctetString"
_Media12_short_name_Object = MibScalar
media12_short_name = _Media12_short_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 12, 2),
    _Media12_short_name_Type()
)
media12_short_name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    media12_short_name.setStatus("optional")
_Media12_page_count_Type = Integer32
_Media12_page_count_Object = MibScalar
media12_page_count = _Media12_page_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 12, 3),
    _Media12_page_count_Type()
)
media12_page_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    media12_page_count.setStatus("optional")
_Media13_ObjectIdentity = ObjectIdentity
media13 = _Media13_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 13)
)


class _Media13_name_Type(OctetString):
    """Custom type media13_name based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 24),
    )


_Media13_name_Type.__name__ = "OctetString"
_Media13_name_Object = MibScalar
media13_name = _Media13_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 13, 1),
    _Media13_name_Type()
)
media13_name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    media13_name.setStatus("optional")


class _Media13_short_name_Type(OctetString):
    """Custom type media13_short_name based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 9),
    )


_Media13_short_name_Type.__name__ = "OctetString"
_Media13_short_name_Object = MibScalar
media13_short_name = _Media13_short_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 13, 2),
    _Media13_short_name_Type()
)
media13_short_name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    media13_short_name.setStatus("optional")
_Media13_page_count_Type = Integer32
_Media13_page_count_Object = MibScalar
media13_page_count = _Media13_page_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 13, 3),
    _Media13_page_count_Type()
)
media13_page_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    media13_page_count.setStatus("optional")
_Media14_ObjectIdentity = ObjectIdentity
media14 = _Media14_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 14)
)


class _Media14_name_Type(OctetString):
    """Custom type media14_name based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 24),
    )


_Media14_name_Type.__name__ = "OctetString"
_Media14_name_Object = MibScalar
media14_name = _Media14_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 14, 1),
    _Media14_name_Type()
)
media14_name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    media14_name.setStatus("optional")


class _Media14_short_name_Type(OctetString):
    """Custom type media14_short_name based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 9),
    )


_Media14_short_name_Type.__name__ = "OctetString"
_Media14_short_name_Object = MibScalar
media14_short_name = _Media14_short_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 14, 2),
    _Media14_short_name_Type()
)
media14_short_name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    media14_short_name.setStatus("optional")
_Media14_page_count_Type = Integer32
_Media14_page_count_Object = MibScalar
media14_page_count = _Media14_page_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 14, 3),
    _Media14_page_count_Type()
)
media14_page_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    media14_page_count.setStatus("optional")
_Media15_ObjectIdentity = ObjectIdentity
media15 = _Media15_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 15)
)


class _Media15_name_Type(OctetString):
    """Custom type media15_name based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 24),
    )


_Media15_name_Type.__name__ = "OctetString"
_Media15_name_Object = MibScalar
media15_name = _Media15_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 15, 1),
    _Media15_name_Type()
)
media15_name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    media15_name.setStatus("optional")


class _Media15_short_name_Type(OctetString):
    """Custom type media15_short_name based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 9),
    )


_Media15_short_name_Type.__name__ = "OctetString"
_Media15_short_name_Object = MibScalar
media15_short_name = _Media15_short_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 15, 2),
    _Media15_short_name_Type()
)
media15_short_name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    media15_short_name.setStatus("optional")
_Media15_page_count_Type = Integer32
_Media15_page_count_Object = MibScalar
media15_page_count = _Media15_page_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 15, 3),
    _Media15_page_count_Type()
)
media15_page_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    media15_page_count.setStatus("optional")
_Media16_ObjectIdentity = ObjectIdentity
media16 = _Media16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 16)
)


class _Media16_name_Type(OctetString):
    """Custom type media16_name based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 24),
    )


_Media16_name_Type.__name__ = "OctetString"
_Media16_name_Object = MibScalar
media16_name = _Media16_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 16, 1),
    _Media16_name_Type()
)
media16_name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    media16_name.setStatus("optional")


class _Media16_short_name_Type(OctetString):
    """Custom type media16_short_name based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 9),
    )


_Media16_short_name_Type.__name__ = "OctetString"
_Media16_short_name_Object = MibScalar
media16_short_name = _Media16_short_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 16, 2),
    _Media16_short_name_Type()
)
media16_short_name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    media16_short_name.setStatus("optional")
_Media16_page_count_Type = Integer32
_Media16_page_count_Object = MibScalar
media16_page_count = _Media16_page_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 16, 3),
    _Media16_page_count_Type()
)
media16_page_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    media16_page_count.setStatus("optional")
_Media17_ObjectIdentity = ObjectIdentity
media17 = _Media17_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 17)
)


class _Media17_name_Type(OctetString):
    """Custom type media17_name based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 24),
    )


_Media17_name_Type.__name__ = "OctetString"
_Media17_name_Object = MibScalar
media17_name = _Media17_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 17, 1),
    _Media17_name_Type()
)
media17_name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    media17_name.setStatus("optional")


class _Media17_short_name_Type(OctetString):
    """Custom type media17_short_name based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 9),
    )


_Media17_short_name_Type.__name__ = "OctetString"
_Media17_short_name_Object = MibScalar
media17_short_name = _Media17_short_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 17, 2),
    _Media17_short_name_Type()
)
media17_short_name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    media17_short_name.setStatus("optional")
_Media17_page_count_Type = Integer32
_Media17_page_count_Object = MibScalar
media17_page_count = _Media17_page_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 17, 3),
    _Media17_page_count_Type()
)
media17_page_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    media17_page_count.setStatus("optional")
_Media18_ObjectIdentity = ObjectIdentity
media18 = _Media18_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 18)
)


class _Media18_name_Type(OctetString):
    """Custom type media18_name based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 24),
    )


_Media18_name_Type.__name__ = "OctetString"
_Media18_name_Object = MibScalar
media18_name = _Media18_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 18, 1),
    _Media18_name_Type()
)
media18_name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    media18_name.setStatus("optional")


class _Media18_short_name_Type(OctetString):
    """Custom type media18_short_name based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 9),
    )


_Media18_short_name_Type.__name__ = "OctetString"
_Media18_short_name_Object = MibScalar
media18_short_name = _Media18_short_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 18, 2),
    _Media18_short_name_Type()
)
media18_short_name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    media18_short_name.setStatus("optional")
_Media18_page_count_Type = Integer32
_Media18_page_count_Object = MibScalar
media18_page_count = _Media18_page_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 18, 3),
    _Media18_page_count_Type()
)
media18_page_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    media18_page_count.setStatus("optional")
_Media19_ObjectIdentity = ObjectIdentity
media19 = _Media19_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 19)
)


class _Media19_name_Type(OctetString):
    """Custom type media19_name based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 24),
    )


_Media19_name_Type.__name__ = "OctetString"
_Media19_name_Object = MibScalar
media19_name = _Media19_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 19, 1),
    _Media19_name_Type()
)
media19_name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    media19_name.setStatus("optional")


class _Media19_short_name_Type(OctetString):
    """Custom type media19_short_name based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 9),
    )


_Media19_short_name_Type.__name__ = "OctetString"
_Media19_short_name_Object = MibScalar
media19_short_name = _Media19_short_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 19, 2),
    _Media19_short_name_Type()
)
media19_short_name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    media19_short_name.setStatus("optional")
_Media19_page_count_Type = Integer32
_Media19_page_count_Object = MibScalar
media19_page_count = _Media19_page_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 19, 3),
    _Media19_page_count_Type()
)
media19_page_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    media19_page_count.setStatus("optional")
_Media_size_ObjectIdentity = ObjectIdentity
media_size = _Media_size_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 5)
)
_Media_size_count_Type = Integer32
_Media_size_count_Object = MibScalar
media_size_count = _Media_size_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 5, 1),
    _Media_size_count_Type()
)
media_size_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    media_size_count.setStatus("optional")
_Media_size_west_edge_first_side_offset_Type = Integer32
_Media_size_west_edge_first_side_offset_Object = MibScalar
media_size_west_edge_first_side_offset = _Media_size_west_edge_first_side_offset_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 5, 2),
    _Media_size_west_edge_first_side_offset_Type()
)
media_size_west_edge_first_side_offset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    media_size_west_edge_first_side_offset.setStatus("optional")
_Media_size_west_edge_second_side_offset_Type = Integer32
_Media_size_west_edge_second_side_offset_Object = MibScalar
media_size_west_edge_second_side_offset = _Media_size_west_edge_second_side_offset_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 5, 3),
    _Media_size_west_edge_second_side_offset_Type()
)
media_size_west_edge_second_side_offset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    media_size_west_edge_second_side_offset.setStatus("optional")
_Media_size_west_edge_side_offset_by_tray_Type = Integer32
_Media_size_west_edge_side_offset_by_tray_Object = MibScalar
media_size_west_edge_side_offset_by_tray = _Media_size_west_edge_side_offset_by_tray_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 5, 4),
    _Media_size_west_edge_side_offset_by_tray_Type()
)
media_size_west_edge_side_offset_by_tray.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    media_size_west_edge_side_offset_by_tray.setStatus("optional")
_Media_counts_ObjectIdentity = ObjectIdentity
media_counts = _Media_counts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 7)
)
_Non_assured_oht_page_count_Type = Integer32
_Non_assured_oht_page_count_Object = MibScalar
non_assured_oht_page_count = _Non_assured_oht_page_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 7, 1),
    _Non_assured_oht_page_count_Type()
)
non_assured_oht_page_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    non_assured_oht_page_count.setStatus("optional")
_Media_types_ObjectIdentity = ObjectIdentity
media_types = _Media_types_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 8)
)
_Media_number_of_type_supported_Type = Integer32
_Media_number_of_type_supported_Object = MibScalar
media_number_of_type_supported = _Media_number_of_type_supported_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 8, 1),
    _Media_number_of_type_supported_Type()
)
media_number_of_type_supported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    media_number_of_type_supported.setStatus("optional")
_Consumables_ObjectIdentity = ObjectIdentity
consumables = _Consumables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 10)
)
_Consumables_1_ObjectIdentity = ObjectIdentity
consumables_1 = _Consumables_1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 10, 1)
)
_Consumable_status_ObjectIdentity = ObjectIdentity
consumable_status = _Consumable_status_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 10, 1, 1)
)


class _Consumable_status_capacity_units_Type(Integer32):
    """Custom type consumable_status_capacity_units based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            4
        )
    )
    namedValues = NamedValues(
        ("eMilliliter", 4)
    )


_Consumable_status_capacity_units_Type.__name__ = "Integer32"
_Consumable_status_capacity_units_Object = MibScalar
consumable_status_capacity_units = _Consumable_status_capacity_units_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 10, 1, 1, 4),
    _Consumable_status_capacity_units_Type()
)
consumable_status_capacity_units.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    consumable_status_capacity_units.setStatus("optional")


class _Consumable_status_total_capacity_Type(Integer32):
    """Custom type consumable_status_total_capacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Consumable_status_total_capacity_Type.__name__ = "Integer32"
_Consumable_status_total_capacity_Object = MibScalar
consumable_status_total_capacity = _Consumable_status_total_capacity_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 10, 1, 1, 5),
    _Consumable_status_total_capacity_Type()
)
consumable_status_total_capacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    consumable_status_total_capacity.setStatus("optional")
_Consumable_status_expiration_date_Type = OctetString
_Consumable_status_expiration_date_Object = MibScalar
consumable_status_expiration_date = _Consumable_status_expiration_date_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 10, 1, 1, 79),
    _Consumable_status_expiration_date_Type()
)
consumable_status_expiration_date.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    consumable_status_expiration_date.setStatus("mandatory")


class _Consumable_reorder_url_Type(OctetString):
    """Custom type consumable_reorder_url based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Consumable_reorder_url_Type.__name__ = "OctetString"
_Consumable_reorder_url_Object = MibScalar
consumable_reorder_url = _Consumable_reorder_url_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 10, 2),
    _Consumable_reorder_url_Type()
)
consumable_reorder_url.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    consumable_reorder_url.setStatus("optional")
_Consumables_status_ObjectIdentity = ObjectIdentity
consumables_status = _Consumables_status_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 10, 5)
)
_Consumables_life_ObjectIdentity = ObjectIdentity
consumables_life = _Consumables_life_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 10, 5, 1)
)
_Consumable_life_usage_units_remaining_Type = Integer32
_Consumable_life_usage_units_remaining_Object = MibScalar
consumable_life_usage_units_remaining = _Consumable_life_usage_units_remaining_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 10, 5, 1, 1),
    _Consumable_life_usage_units_remaining_Type()
)
consumable_life_usage_units_remaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    consumable_life_usage_units_remaining.setStatus("optional")


class _Consumable_life_usage_units_Type(Integer32):
    """Custom type consumable_life_usage_units based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eEstimatedPagesRemaining", 2),
          ("ePagesRemaining", 1))
    )


_Consumable_life_usage_units_Type.__name__ = "Integer32"
_Consumable_life_usage_units_Object = MibScalar
consumable_life_usage_units = _Consumable_life_usage_units_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 10, 5, 1, 2),
    _Consumable_life_usage_units_Type()
)
consumable_life_usage_units.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    consumable_life_usage_units.setStatus("optional")
_Consumable_life_low_threshold_Type = Integer32
_Consumable_life_low_threshold_Object = MibScalar
consumable_life_low_threshold = _Consumable_life_low_threshold_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 10, 5, 1, 3),
    _Consumable_life_low_threshold_Type()
)
consumable_life_low_threshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    consumable_life_low_threshold.setStatus("optional")
_Consumable_current_state_Type = OctetString
_Consumable_current_state_Object = MibScalar
consumable_current_state = _Consumable_current_state_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 10, 7),
    _Consumable_current_state_Type()
)
consumable_current_state.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    consumable_current_state.setStatus("optional")
_Consumable_string_ObjectIdentity = ObjectIdentity
consumable_string = _Consumable_string_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 10, 8)
)


class _Consumable_string_information_Type(OctetString):
    """Custom type consumable_string_information based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 287),
    )


_Consumable_string_information_Type.__name__ = "OctetString"
_Consumable_string_information_Object = MibScalar
consumable_string_information = _Consumable_string_information_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 10, 8, 1),
    _Consumable_string_information_Type()
)
consumable_string_information.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    consumable_string_information.setStatus("optional")


class _Consumable_string_information_reset_Type(Integer32):
    """Custom type consumable_string_information_reset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eCustomized", 2),
          ("ePresetToNVRAM", 1))
    )


_Consumable_string_information_reset_Type.__name__ = "Integer32"
_Consumable_string_information_reset_Object = MibScalar
consumable_string_information_reset = _Consumable_string_information_reset_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 10, 8, 2),
    _Consumable_string_information_reset_Type()
)
consumable_string_information_reset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    consumable_string_information_reset.setStatus("optional")
_Consumable_notification_status_Type = OctetString
_Consumable_notification_status_Object = MibScalar
consumable_notification_status = _Consumable_notification_status_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 10, 10),
    _Consumable_notification_status_Type()
)
consumable_notification_status.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    consumable_notification_status.setStatus("optional")
_Consumable_pages_printed_with_supply_Type = Integer32
_Consumable_pages_printed_with_supply_Object = MibScalar
consumable_pages_printed_with_supply = _Consumable_pages_printed_with_supply_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 10, 11),
    _Consumable_pages_printed_with_supply_Type()
)
consumable_pages_printed_with_supply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    consumable_pages_printed_with_supply.setStatus("optional")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IJ8060-MIB",
    **{"DisplayString": DisplayString,
       "hp": hp,
       "dm": dm,
       "device": device,
       "device-system": device_system,
       "settings-system": settings_system,
       "energy-star": energy_star,
       "sleep-mode": sleep_mode,
       "date-display": date_display,
       "mono-color-switching-mode": mono_color_switching_mode,
       "device-configure": device_configure,
       "device-configure-printer-parameters": device_configure_printer_parameters,
       "direct-connect-ports-enable": direct_connect_ports_enable,
       "control-panel-supplies-status-message": control_panel_supplies_status_message,
       "power-state": power_state,
       "factory-reset": factory_reset,
       "display-long-grain-optimization-warning": display_long_grain_optimization_warning,
       "powersave-enable-type": powersave_enable_type,
       "status-system": status_system,
       "on-off-line": on_off_line,
       "continue": _pysmi_continue,
       "auto-continue": auto_continue,
       "install-date": install_date,
       "perm-store-init-occurred": perm_store_init_occurred,
       "timestamp": timestamp,
       "date-and-time": date_and_time,
       "service-id": service_id,
       "display": display,
       "display-status": display_status,
       "show-address": show_address,
       "time-display": time_display,
       "job-input-auto-continue-timeout": job_input_auto_continue_timeout,
       "job-input-auto-continue-mode": job_input_auto_continue_mode,
       "background-message": background_message,
       "background-message1": background_message1,
       "background-status-msg-line1-part1": background_status_msg_line1_part1,
       "background-message2": background_message2,
       "background-status-msg-line2-part1": background_status_msg_line2_part1,
       "background-status-msg-higher-priority": background_status_msg_higher_priority,
       "error-log-clear": error_log_clear,
       "job-output-auto-continue-timeout": job_output_auto_continue_timeout,
       "collated-originals-support": collated_originals_support,
       "localization-languages-supported": localization_languages_supported,
       "localization-countries-supported": localization_countries_supported,
       "host-application-available-memory": host_application_available_memory,
       "control-panel-button-press": control_panel_button_press,
       "control-panel-display-contents-change-counter": control_panel_display_contents_change_counter,
       "control-panel-display-contents-crc": control_panel_display_contents_crc,
       "control-panel-display": control_panel_display,
       "control-panel-display-graphical-contents": control_panel_display_graphical_contents,
       "control-panel-key-press": control_panel_key_press,
       "rtc-time-zone": rtc_time_zone,
       "automatic-daylight-savings": automatic_daylight_savings,
       "daylight-savings-start": daylight_savings_start,
       "daylight-savings-end": daylight_savings_end,
       "daylight-savings-offset": daylight_savings_offset,
       "daylight-savings-reset": daylight_savings_reset,
       "email-service-operational": email_service_operational,
       "id": id,
       "model-number": model_number,
       "model-name": model_name,
       "serial-number": serial_number,
       "fw-rom-datecode": fw_rom_datecode,
       "fw-rom-revision": fw_rom_revision,
       "device-name": device_name,
       "device-location": device_location,
       "asset-number": asset_number,
       "formatter-serial-number": formatter_serial_number,
       "interface": interface,
       "mio": mio,
       "mio1": mio1,
       "mio1-model-name": mio1_model_name,
       "mio1-manufacturing-info": mio1_manufacturing_info,
       "mio1-type": mio1_type,
       "mio4": mio4,
       "mio4-model-name": mio4_model_name,
       "mio4-manufacturing-info": mio4_manufacturing_info,
       "mio4-type": mio4_type,
       "phd": phd,
       "phd1": phd1,
       "phd1-diagnostics-nvram-data": phd1_diagnostics_nvram_data,
       "phd2": phd2,
       "phd2-model": phd2_model,
       "phd2-manufacturing-info": phd2_manufacturing_info,
       "phd2-type": phd2_type,
       "phd2-capacity": phd2_capacity,
       "web-server": web_server,
       "settings-web-server": settings_web_server,
       "web-proxy-config-enable": web_proxy_config_enable,
       "ews-request-control-panel-supplies-status": ews_request_control_panel_supplies_status,
       "foreign-interface": foreign_interface,
       "fih-extra-pulses-feature": fih_extra_pulses_feature,
       "usb-interface": usb_interface,
       "usb-host-supported": usb_host_supported,
       "usb": usb,
       "usb-serial-number": usb_serial_number,
       "usb-manufacturer-name": usb_manufacturer_name,
       "usb-product-description": usb_product_description,
       "usb-vendor-id": usb_vendor_id,
       "usb-product-id": usb_product_id,
       "usb-device-kind": usb_device_kind,
       "usb-driver-name": usb_driver_name,
       "job": job,
       "settings-job": settings_job,
       "clearable-warning": clearable_warning,
       "cancel-job": cancel_job,
       "job-info-change-id": job_info_change_id,
       "hold-job-timeout": hold_job_timeout,
       "active-print-jobs": active_print_jobs,
       "job-being-parsed": job_being_parsed,
       "current-job-parsing-id": current_job_parsing_id,
       "job-info": job_info,
       "job-info-name1": job_info_name1,
       "job-info-name2": job_info_name2,
       "job-info-stage": job_info_stage,
       "job-info-io-source": job_info_io_source,
       "job-info-pages-processed": job_info_pages_processed,
       "job-info-pages-printed": job_info_pages_printed,
       "job-info-size": job_info_size,
       "job-info-state": job_info_state,
       "job-info-outcome": job_info_outcome,
       "job-info-attribute": job_info_attribute,
       "job-info-attr-1": job_info_attr_1,
       "job-info-attr-2": job_info_attr_2,
       "job-info-attr-3": job_info_attr_3,
       "job-info-attr-4": job_info_attr_4,
       "job-info-attr-5": job_info_attr_5,
       "job-info-attr-6": job_info_attr_6,
       "job-info-attr-7": job_info_attr_7,
       "job-info-attr-8": job_info_attr_8,
       "job-info-attr-9": job_info_attr_9,
       "job-info-attr-10": job_info_attr_10,
       "job-info-attr-11": job_info_attr_11,
       "job-info-attr-12": job_info_attr_12,
       "job-info-attr-13": job_info_attr_13,
       "job-info-attr-14": job_info_attr_14,
       "job-info-attr-15": job_info_attr_15,
       "job-info-attr-16": job_info_attr_16,
       "job-info-accounting": job_info_accounting,
       "job-info-accounting-media-size": job_info_accounting_media_size,
       "job-info-accounting-media-type": job_info_accounting_media_type,
       "job-info-accounting-finishing-options": job_info_accounting_finishing_options,
       "job-info-accounting-media-simplex-count": job_info_accounting_media_simplex_count,
       "job-info-accounting-media-duplex-count": job_info_accounting_media_duplex_count,
       "job-info-accounting-grayscale-impression-count": job_info_accounting_grayscale_impression_count,
       "job-info-accounting-color-impression-count": job_info_accounting_color_impression_count,
       "job-info-accounting-black-dots": job_info_accounting_black_dots,
       "job-info-accounting-yellow-dots": job_info_accounting_yellow_dots,
       "job-info-accounting-cyan-dots": job_info_accounting_cyan_dots,
       "job-info-accounting-magenta-dots": job_info_accounting_magenta_dots,
       "job-info-accounting-job-type": job_info_accounting_job_type,
       "job-info-accounting-fixer-dots": job_info_accounting_fixer_dots,
       "held-job": held_job,
       "held-job-info": held_job_info,
       "held-job-user-name": held_job_user_name,
       "held-job-job-name": held_job_job_name,
       "held-job-retention": held_job_retention,
       "held-job-security": held_job_security,
       "held-job-quantity": held_job_quantity,
       "held-job-pin": held_job_pin,
       "held-job-control": held_job_control,
       "held-job-print": held_job_print,
       "held-job-delete": held_job_delete,
       "held-job-set-queue-size": held_job_set_queue_size,
       "held-job-enable": held_job_enable,
       "file-system": file_system,
       "settings-file-system": settings_file_system,
       "file-system-max-open-files": file_system_max_open_files,
       "file-system-set-system-partition-writeable": file_system_set_system_partition_writeable,
       "file-system-set-system-partition-readonly": file_system_set_system_partition_readonly,
       "file-system-delete-files": file_system_delete_files,
       "file-system-external-access-capabilities": file_system_external_access_capabilities,
       "file-system-erase-mode": file_system_erase_mode,
       "file-system-wipe-disk": file_system_wipe_disk,
       "file-system-wipe-disk-status": file_system_wipe_disk_status,
       "file-systems": file_systems,
       "file-system2": file_system2,
       "file-system2-initialize-volume": file_system2_initialize_volume,
       "file-system3": file_system3,
       "file-system3-initialize-volume": file_system3_initialize_volume,
       "file-system4": file_system4,
       "file-system4-initialize-volume": file_system4_initialize_volume,
       "errorlog": errorlog,
       "error1": error1,
       "error1-time-stamp": error1_time_stamp,
       "error1-code": error1_code,
       "error1-date-time": error1_date_time,
       "error2": error2,
       "error2-time-stamp": error2_time_stamp,
       "error2-code": error2_code,
       "error2-date-time": error2_date_time,
       "error3": error3,
       "error3-time-stamp": error3_time_stamp,
       "error3-code": error3_code,
       "error3-date-time": error3_date_time,
       "error4": error4,
       "error4-time-stamp": error4_time_stamp,
       "error4-code": error4_code,
       "error4-date-time": error4_date_time,
       "error5": error5,
       "error5-time-stamp": error5_time_stamp,
       "error5-code": error5_code,
       "error5-date-time": error5_date_time,
       "error6": error6,
       "error6-time-stamp": error6_time_stamp,
       "error6-code": error6_code,
       "error6-date-time": error6_date_time,
       "error7": error7,
       "error7-time-stamp": error7_time_stamp,
       "error7-code": error7_code,
       "error7-date-time": error7_date_time,
       "error8": error8,
       "error8-time-stamp": error8_time_stamp,
       "error8-code": error8_code,
       "error8-date-time": error8_date_time,
       "error9": error9,
       "error9-time-stamp": error9_time_stamp,
       "error9-code": error9_code,
       "error9-date-time": error9_date_time,
       "error10": error10,
       "error10-time-stamp": error10_time_stamp,
       "error10-code": error10_code,
       "error10-date-time": error10_date_time,
       "error11": error11,
       "error11-time-stamp": error11_time_stamp,
       "error11-code": error11_code,
       "error11-date-time": error11_date_time,
       "error12": error12,
       "error12-time-stamp": error12_time_stamp,
       "error12-code": error12_code,
       "error12-date-time": error12_date_time,
       "error13": error13,
       "error13-time-stamp": error13_time_stamp,
       "error13-code": error13_code,
       "error13-date-time": error13_date_time,
       "error14": error14,
       "error14-time-stamp": error14_time_stamp,
       "error14-code": error14_code,
       "error14-date-time": error14_date_time,
       "error15": error15,
       "error15-time-stamp": error15_time_stamp,
       "error15-code": error15_code,
       "error15-date-time": error15_date_time,
       "error16": error16,
       "error16-time-stamp": error16_time_stamp,
       "error16-code": error16_code,
       "error16-date-time": error16_date_time,
       "error17": error17,
       "error17-time-stamp": error17_time_stamp,
       "error17-code": error17_code,
       "error17-date-time": error17_date_time,
       "error18": error18,
       "error18-time-stamp": error18_time_stamp,
       "error18-code": error18_code,
       "error18-date-time": error18_date_time,
       "error19": error19,
       "error19-time-stamp": error19_time_stamp,
       "error19-code": error19_code,
       "error19-date-time": error19_date_time,
       "error20": error20,
       "error20-time-stamp": error20_time_stamp,
       "error20-code": error20_code,
       "error20-date-time": error20_date_time,
       "error21": error21,
       "error21-time-stamp": error21_time_stamp,
       "error21-code": error21_code,
       "error21-date-time": error21_date_time,
       "error22": error22,
       "error22-time-stamp": error22_time_stamp,
       "error22-code": error22_code,
       "error22-date-time": error22_date_time,
       "error23": error23,
       "error23-time-stamp": error23_time_stamp,
       "error23-code": error23_code,
       "error23-date-time": error23_date_time,
       "error24": error24,
       "error24-time-stamp": error24_time_stamp,
       "error24-code": error24_code,
       "error24-date-time": error24_date_time,
       "error25": error25,
       "error25-time-stamp": error25_time_stamp,
       "error25-code": error25_code,
       "error25-date-time": error25_date_time,
       "error26": error26,
       "error26-time-stamp": error26_time_stamp,
       "error26-code": error26_code,
       "error26-date-time": error26_date_time,
       "error27": error27,
       "error27-time-stamp": error27_time_stamp,
       "error27-code": error27_code,
       "error27-date-time": error27_date_time,
       "error28": error28,
       "error28-time-stamp": error28_time_stamp,
       "error28-code": error28_code,
       "error28-date-time": error28_date_time,
       "error29": error29,
       "error29-time-stamp": error29_time_stamp,
       "error29-code": error29_code,
       "error29-date-time": error29_date_time,
       "error30": error30,
       "error30-time-stamp": error30_time_stamp,
       "error30-code": error30_code,
       "error30-date-time": error30_date_time,
       "error31": error31,
       "error31-time-stamp": error31_time_stamp,
       "error31-code": error31_code,
       "error31-date-time": error31_date_time,
       "error32": error32,
       "error32-time-stamp": error32_time_stamp,
       "error32-code": error32_code,
       "error32-date-time": error32_date_time,
       "error33": error33,
       "error33-time-stamp": error33_time_stamp,
       "error33-code": error33_code,
       "error33-date-time": error33_date_time,
       "error34": error34,
       "error34-time-stamp": error34_time_stamp,
       "error34-code": error34_code,
       "error34-date-time": error34_date_time,
       "error35": error35,
       "error35-time-stamp": error35_time_stamp,
       "error35-code": error35_code,
       "error35-date-time": error35_date_time,
       "error36": error36,
       "error36-time-stamp": error36_time_stamp,
       "error36-code": error36_code,
       "error36-date-time": error36_date_time,
       "error37": error37,
       "error37-time-stamp": error37_time_stamp,
       "error37-code": error37_code,
       "error37-date-time": error37_date_time,
       "error38": error38,
       "error38-time-stamp": error38_time_stamp,
       "error38-code": error38_code,
       "error38-date-time": error38_date_time,
       "error39": error39,
       "error39-time-stamp": error39_time_stamp,
       "error39-code": error39_code,
       "error39-date-time": error39_date_time,
       "error40": error40,
       "error40-time-stamp": error40_time_stamp,
       "error40-code": error40_code,
       "error40-date-time": error40_date_time,
       "error41": error41,
       "error41-time-stamp": error41_time_stamp,
       "error41-code": error41_code,
       "error41-date-time": error41_date_time,
       "error42": error42,
       "error42-time-stamp": error42_time_stamp,
       "error42-code": error42_code,
       "error42-date-time": error42_date_time,
       "error43": error43,
       "error43-time-stamp": error43_time_stamp,
       "error43-code": error43_code,
       "error43-date-time": error43_date_time,
       "error44": error44,
       "error44-time-stamp": error44_time_stamp,
       "error44-code": error44_code,
       "error44-date-time": error44_date_time,
       "error45": error45,
       "error45-time-stamp": error45_time_stamp,
       "error45-code": error45_code,
       "error45-date-time": error45_date_time,
       "error46": error46,
       "error46-time-stamp": error46_time_stamp,
       "error46-code": error46_code,
       "error46-date-time": error46_date_time,
       "error47": error47,
       "error47-time-stamp": error47_time_stamp,
       "error47-code": error47_code,
       "error47-date-time": error47_date_time,
       "error48": error48,
       "error48-time-stamp": error48_time_stamp,
       "error48-code": error48_code,
       "error48-date-time": error48_date_time,
       "error49": error49,
       "error49-time-stamp": error49_time_stamp,
       "error49-code": error49_code,
       "error49-date-time": error49_date_time,
       "error50": error50,
       "error50-time-stamp": error50_time_stamp,
       "error50-code": error50_code,
       "error50-date-time": error50_date_time,
       "resource-manager": resource_manager,
       "mass-storage-resources": mass_storage_resources,
       "mass-storage-resource-change-counter": mass_storage_resource_change_counter,
       "mass-storage-resource-changed": mass_storage_resource_changed,
       "remote-procedure-call": remote_procedure_call,
       "settings-rpc": settings_rpc,
       "rpc-bind-protocol-address": rpc_bind_protocol_address,
       "status-rpc": status_rpc,
       "rpc-bound-protocol-address": rpc_bound_protocol_address,
       "mass-storage-block-driver": mass_storage_block_driver,
       "settings-mass-storage-bd": settings_mass_storage_bd,
       "ram-disk-mode": ram_disk_mode,
       "ram-disk-size": ram_disk_size,
       "status-mass-storage-bd": status_mass_storage_bd,
       "maximum-ram-disk-memory": maximum_ram_disk_memory,
       "accounting": accounting,
       "printer-accounting": printer_accounting,
       "printed-media-usage": printed_media_usage,
       "printed-media-simplex-count": printed_media_simplex_count,
       "printed-media-simplex-charge": printed_media_simplex_charge,
       "printed-media-duplex-count": printed_media_duplex_count,
       "printed-media-duplex-charge": printed_media_duplex_charge,
       "printed-media-total-charge": printed_media_total_charge,
       "printed-media-maximum-pixels-per-page": printed_media_maximum_pixels_per_page,
       "printed-media-combined-total": printed_media_combined_total,
       "printed-media-dimplex-count": printed_media_dimplex_count,
       "usage-printer-total-charge": usage_printer_total_charge,
       "usage-staple-count": usage_staple_count,
       "usage-instructions-line1": usage_instructions_line1,
       "usage-instructions-line2": usage_instructions_line2,
       "usage-instructions-line3": usage_instructions_line3,
       "usage-instructions-line4": usage_instructions_line4,
       "source-tray-usage-total": source_tray_usage_total,
       "destination-bin-usage-total": destination_bin_usage_total,
       "usage-printer-mono-total-charge": usage_printer_mono_total_charge,
       "usage-printer-color-total-charge": usage_printer_color_total_charge,
       "print-meter-usage": print_meter_usage,
       "print-meter-usage-threshold": print_meter_usage_threshold,
       "print-meter-print-quality": print_meter_print_quality,
       "print-meter-simplex-count": print_meter_simplex_count,
       "print-meter-duplex-count": print_meter_duplex_count,
       "print-meter-total-charge": print_meter_total_charge,
       "print-meter-dimplex-count": print_meter_dimplex_count,
       "print-meter-simplex-total": print_meter_simplex_total,
       "print-meter-duplex-total": print_meter_duplex_total,
       "print-meter-category-total": print_meter_category_total,
       "print-meter-dimplex-total": print_meter_dimplex_total,
       "usage-printer-mono-simplex-total": usage_printer_mono_simplex_total,
       "usage-printer-mono-duplex-total": usage_printer_mono_duplex_total,
       "usage-printer-mono-dimplex-total": usage_printer_mono_dimplex_total,
       "scanner-accounting": scanner_accounting,
       "scanned-media-usage": scanned_media_usage,
       "scanned-media-simplex-count": scanned_media_simplex_count,
       "scanned-media-simplex-charge": scanned_media_simplex_charge,
       "scanned-media-duplex-count": scanned_media_duplex_count,
       "scanned-media-duplex-charge": scanned_media_duplex_charge,
       "scanned-media-total-charge": scanned_media_total_charge,
       "usage-scanner-total-charge": usage_scanner_total_charge,
       "printer-color-accounting": printer_color_accounting,
       "printed-media-color-usage": printed_media_color_usage,
       "printed-media-color-simplex-count": printed_media_color_simplex_count,
       "printed-media-color-duplex-count": printed_media_color_duplex_count,
       "printed-media-color-total-count": printed_media_color_total_count,
       "printed-media-color-dimplex-count": printed_media_color_dimplex_count,
       "source-tray-accounting": source_tray_accounting,
       "source-tray-usage": source_tray_usage,
       "source-tray-usage-count": source_tray_usage_count,
       "destination-bin-accounting": destination_bin_accounting,
       "destination-bin-usage": destination_bin_usage,
       "destination-bin-usage-count": destination_bin_usage_count,
       "firmware-download": firmware_download,
       "firmware-download-write-status-supported": firmware_download_write_status_supported,
       "firmware-download-write-time": firmware_download_write_time,
       "firmware-download-write-count": firmware_download_write_count,
       "firmware-download-current-state": firmware_download_current_state,
       "firmware-download-maximum-write-count": firmware_download_maximum_write_count,
       "firmware-download-name": firmware_download_name,
       "firmware-download-version": firmware_download_version,
       "operating-system": operating_system,
       "os-execute-file": os_execute_file,
       "upgradable-devices": upgradable_devices,
       "upgradable-devices-write-status-supported": upgradable_devices_write_status_supported,
       "upgradable-devices-write-time": upgradable_devices_write_time,
       "upgradable-devices-write-count": upgradable_devices_write_count,
       "upgradable-devices-current-state": upgradable_devices_current_state,
       "upgradable-devices-max-write-count": upgradable_devices_max_write_count,
       "upgradable-devices-name": upgradable_devices_name,
       "upgradable-devices-version": upgradable_devices_version,
       "remote-upgrade-enable": remote_upgrade_enable,
       "warninglog": warninglog,
       "warning1": warning1,
       "warning1-time-stamp": warning1_time_stamp,
       "warning1-code": warning1_code,
       "warning1-date-time": warning1_date_time,
       "warning2": warning2,
       "warning2-time-stamp": warning2_time_stamp,
       "warning2-code": warning2_code,
       "warning2-date-time": warning2_date_time,
       "warning3": warning3,
       "warning3-time-stamp": warning3_time_stamp,
       "warning3-code": warning3_code,
       "warning3-date-time": warning3_date_time,
       "warning4": warning4,
       "warning4-time-stamp": warning4_time_stamp,
       "warning4-code": warning4_code,
       "warning4-date-time": warning4_date_time,
       "warning5": warning5,
       "warning5-time-stamp": warning5_time_stamp,
       "warning5-code": warning5_code,
       "warning5-date-time": warning5_date_time,
       "warning6": warning6,
       "warning6-time-stamp": warning6_time_stamp,
       "warning6-code": warning6_code,
       "warning6-date-time": warning6_date_time,
       "warning7": warning7,
       "warning7-time-stamp": warning7_time_stamp,
       "warning7-code": warning7_code,
       "warning7-date-time": warning7_date_time,
       "warning8": warning8,
       "warning8-time-stamp": warning8_time_stamp,
       "warning8-code": warning8_code,
       "warning8-date-time": warning8_date_time,
       "warning9": warning9,
       "warning9-time-stamp": warning9_time_stamp,
       "warning9-code": warning9_code,
       "warning9-date-time": warning9_date_time,
       "warning10": warning10,
       "warning10-time-stamp": warning10_time_stamp,
       "warning10-code": warning10_code,
       "warning10-date-time": warning10_date_time,
       "warning11": warning11,
       "warning11-time-stamp": warning11_time_stamp,
       "warning11-code": warning11_code,
       "warning11-date-time": warning11_date_time,
       "warning12": warning12,
       "warning12-time-stamp": warning12_time_stamp,
       "warning12-code": warning12_code,
       "warning12-date-time": warning12_date_time,
       "warning13": warning13,
       "warning13-time-stamp": warning13_time_stamp,
       "warning13-code": warning13_code,
       "warning13-date-time": warning13_date_time,
       "warning14": warning14,
       "warning14-time-stamp": warning14_time_stamp,
       "warning14-code": warning14_code,
       "warning14-date-time": warning14_date_time,
       "warning15": warning15,
       "warning15-time-stamp": warning15_time_stamp,
       "warning15-code": warning15_code,
       "warning15-date-time": warning15_date_time,
       "warning16": warning16,
       "warning16-time-stamp": warning16_time_stamp,
       "warning16-code": warning16_code,
       "warning16-date-time": warning16_date_time,
       "warning17": warning17,
       "warning17-time-stamp": warning17_time_stamp,
       "warning17-code": warning17_code,
       "warning17-date-time": warning17_date_time,
       "warning18": warning18,
       "warning18-time-stamp": warning18_time_stamp,
       "warning18-code": warning18_code,
       "warning18-date-time": warning18_date_time,
       "warning19": warning19,
       "warning19-time-stamp": warning19_time_stamp,
       "warning19-code": warning19_code,
       "warning19-date-time": warning19_date_time,
       "warning20": warning20,
       "warning20-time-stamp": warning20_time_stamp,
       "warning20-code": warning20_code,
       "warning20-date-time": warning20_date_time,
       "warning21": warning21,
       "warning21-time-stamp": warning21_time_stamp,
       "warning21-code": warning21_code,
       "warning21-date-time": warning21_date_time,
       "warning22": warning22,
       "warning22-time-stamp": warning22_time_stamp,
       "warning22-code": warning22_code,
       "warning22-date-time": warning22_date_time,
       "warning23": warning23,
       "warning23-time-stamp": warning23_time_stamp,
       "warning23-code": warning23_code,
       "warning23-date-time": warning23_date_time,
       "warning24": warning24,
       "warning24-time-stamp": warning24_time_stamp,
       "warning24-code": warning24_code,
       "warning24-date-time": warning24_date_time,
       "warning25": warning25,
       "warning25-time-stamp": warning25_time_stamp,
       "warning25-code": warning25_code,
       "warning25-date-time": warning25_date_time,
       "warning26": warning26,
       "warning26-time-stamp": warning26_time_stamp,
       "warning26-code": warning26_code,
       "warning26-date-time": warning26_date_time,
       "warning27": warning27,
       "warning27-time-stamp": warning27_time_stamp,
       "warning27-code": warning27_code,
       "warning27-date-time": warning27_date_time,
       "warning28": warning28,
       "warning28-time-stamp": warning28_time_stamp,
       "warning28-code": warning28_code,
       "warning28-date-time": warning28_date_time,
       "warning29": warning29,
       "warning29-time-stamp": warning29_time_stamp,
       "warning29-code": warning29_code,
       "warning29-date-time": warning29_date_time,
       "warning30": warning30,
       "warning30-time-stamp": warning30_time_stamp,
       "warning30-code": warning30_code,
       "warning30-date-time": warning30_date_time,
       "warning31": warning31,
       "warning31-time-stamp": warning31_time_stamp,
       "warning31-code": warning31_code,
       "warning31-date-time": warning31_date_time,
       "warning32": warning32,
       "warning32-time-stamp": warning32_time_stamp,
       "warning32-code": warning32_code,
       "warning32-date-time": warning32_date_time,
       "warning33": warning33,
       "warning33-time-stamp": warning33_time_stamp,
       "warning33-code": warning33_code,
       "warning33-date-time": warning33_date_time,
       "warning34": warning34,
       "warning34-time-stamp": warning34_time_stamp,
       "warning34-code": warning34_code,
       "warning34-date-time": warning34_date_time,
       "warning35": warning35,
       "warning35-time-stamp": warning35_time_stamp,
       "warning35-code": warning35_code,
       "warning35-date-time": warning35_date_time,
       "warning36": warning36,
       "warning36-time-stamp": warning36_time_stamp,
       "warning36-code": warning36_code,
       "warning36-date-time": warning36_date_time,
       "warning37": warning37,
       "warning37-time-stamp": warning37_time_stamp,
       "warning37-code": warning37_code,
       "warning37-date-time": warning37_date_time,
       "warning38": warning38,
       "warning38-time-stamp": warning38_time_stamp,
       "warning38-code": warning38_code,
       "warning38-date-time": warning38_date_time,
       "warning39": warning39,
       "warning39-time-stamp": warning39_time_stamp,
       "warning39-code": warning39_code,
       "warning39-date-time": warning39_date_time,
       "warning40": warning40,
       "warning40-time-stamp": warning40_time_stamp,
       "warning40-code": warning40_code,
       "warning40-date-time": warning40_date_time,
       "warning41": warning41,
       "warning41-time-stamp": warning41_time_stamp,
       "warning41-code": warning41_code,
       "warning41-date-time": warning41_date_time,
       "warning42": warning42,
       "warning42-time-stamp": warning42_time_stamp,
       "warning42-code": warning42_code,
       "warning42-date-time": warning42_date_time,
       "warning43": warning43,
       "warning43-time-stamp": warning43_time_stamp,
       "warning43-code": warning43_code,
       "warning43-date-time": warning43_date_time,
       "warning44": warning44,
       "warning44-time-stamp": warning44_time_stamp,
       "warning44-code": warning44_code,
       "warning44-date-time": warning44_date_time,
       "warning45": warning45,
       "warning45-time-stamp": warning45_time_stamp,
       "warning45-code": warning45_code,
       "warning45-date-time": warning45_date_time,
       "warning46": warning46,
       "warning46-time-stamp": warning46_time_stamp,
       "warning46-code": warning46_code,
       "warning46-date-time": warning46_date_time,
       "warning47": warning47,
       "warning47-time-stamp": warning47_time_stamp,
       "warning47-code": warning47_code,
       "warning47-date-time": warning47_date_time,
       "warning48": warning48,
       "warning48-time-stamp": warning48_time_stamp,
       "warning48-code": warning48_code,
       "warning48-date-time": warning48_date_time,
       "warning49": warning49,
       "warning49-time-stamp": warning49_time_stamp,
       "warning49-code": warning49_code,
       "warning49-date-time": warning49_date_time,
       "warning50": warning50,
       "warning50-time-stamp": warning50_time_stamp,
       "warning50-code": warning50_code,
       "warning50-date-time": warning50_date_time,
       "security": security,
       "settings-security": settings_security,
       "supports-pjl-user-groups": supports_pjl_user_groups,
       "source-subsystem": source_subsystem,
       "io": io,
       "settings-io": settings_io,
       "io-timeout": io_timeout,
       "io-switch": io_switch,
       "ports": ports,
       "port1": port1,
       "port1-parallel-speed": port1_parallel_speed,
       "port1-parallel-bidirectionality": port1_parallel_bidirectionality,
       "scanner": scanner,
       "settings-scanner": settings_scanner,
       "scanner-accessory-adf-sheet-count": scanner_accessory_adf_sheet_count,
       "scanner-accessory-flatbed-scan-count": scanner_accessory_flatbed_scan_count,
       "scanner-accessory-adf-one-sided-sheet-count": scanner_accessory_adf_one_sided_sheet_count,
       "scanner-accessory-adf-two-sided-sheet-count": scanner_accessory_adf_two_sided_sheet_count,
       "scanner-accessory-copy-job-scan-count": scanner_accessory_copy_job_scan_count,
       "scanner-accessory-send-job-scan-count": scanner_accessory_send_job_scan_count,
       "scan-to-folder-count": scan_to_folder_count,
       "fax-job-scan-count": fax_job_scan_count,
       "processing-subsystem": processing_subsystem,
       "pdl": pdl,
       "settings-pdl": settings_pdl,
       "default-copies": default_copies,
       "form-feed": form_feed,
       "default-vertical-black-resolution": default_vertical_black_resolution,
       "default-horizontal-black-resolution": default_horizontal_black_resolution,
       "default-page-protect": default_page_protect,
       "default-lines-per-page": default_lines_per_page,
       "default-vmi": default_vmi,
       "default-media-size": default_media_size,
       "cold-reset-media-size": cold_reset_media_size,
       "default-media-name": default_media_name,
       "reprint": reprint,
       "default-bits-per-pixel": default_bits_per_pixel,
       "status-pdl": status_pdl,
       "form-feed-needed": form_feed_needed,
       "pdl-pcl": pdl_pcl,
       "pcl-total-page-count": pcl_total_page_count,
       "pcl-default-font-source": pcl_default_font_source,
       "pcl-default-font-number": pcl_default_font_number,
       "pdl-postscript": pdl_postscript,
       "postscript-total-page-count": postscript_total_page_count,
       "postscript-print-errors": postscript_print_errors,
       "postscript-defer-media": postscript_defer_media,
       "pdl-pdf": pdl_pdf,
       "pdf-version": pdf_version,
       "pdf-total-page-count": pdf_total_page_count,
       "pdf-enabled": pdf_enabled,
       "pdf-print-errors": pdf_print_errors,
       "fax-proc-sub": fax_proc_sub,
       "settings-fax-proc-sub": settings_fax_proc_sub,
       "fax-print-page-count": fax_print_page_count,
       "status-fax-proc-sub": status_fax_proc_sub,
       "pcfax-send-enabled": pcfax_send_enabled,
       "pcfax-send-operational": pcfax_send_operational,
       "fax-notification-available": fax_notification_available,
       "fax-billing-code-enabled": fax_billing_code_enabled,
       "fax-billing-code-minlength": fax_billing_code_minlength,
       "fax-billing-code": fax_billing_code,
       "webserver-proc-sub": webserver_proc_sub,
       "settings-webserver": settings_webserver,
       "web-server-url": web_server_url,
       "web-server-security": web_server_security,
       "destination-subsystem": destination_subsystem,
       "print-engine": print_engine,
       "settings-prt-eng": settings_prt_eng,
       "override-media-name": override_media_name,
       "override-media-size": override_media_size,
       "configurable-low-threshold-setting": configurable_low_threshold_setting,
       "cartridge-out-override-control": cartridge_out_override_control,
       "duplex-blank-pages": duplex_blank_pages,
       "finisher-image-rotation": finisher_image_rotation,
       "status-prt-eng": status_prt_eng,
       "total-engine-page-count": total_engine_page_count,
       "total-color-page-count": total_color_page_count,
       "duplex-page-count": duplex_page_count,
       "print-engine-revision": print_engine_revision,
       "printer-calibration-dhalf": printer_calibration_dhalf,
       "printer-cal-dhalf-page-count": printer_cal_dhalf_page_count,
       "printer-cal-dhalf-utc": printer_cal_dhalf_utc,
       "printer-calibration-cpr": printer_calibration_cpr,
       "printer-cal-cpr-page-count": printer_cal_cpr_page_count,
       "printer-cal-cpr-utc": printer_cal_cpr_utc,
       "intray": intray,
       "settings-intray": settings_intray,
       "input-tray-auto-select": input_tray_auto_select,
       "custom-paper-feed-dim": custom_paper_feed_dim,
       "custom-paper-xfeed-dim": custom_paper_xfeed_dim,
       "default-custom-paper-dim-unit": default_custom_paper_dim_unit,
       "default-custom-paper-feed-dim": default_custom_paper_feed_dim,
       "default-custom-paper-xfeed-dim": default_custom_paper_xfeed_dim,
       "input-tray-max-media-feed-dim": input_tray_max_media_feed_dim,
       "input-tray-max-media-xfeed-dim": input_tray_max_media_xfeed_dim,
       "input-tray-min-media-feed-dim": input_tray_min_media_feed_dim,
       "input-tray-min-media-xfeed-dim": input_tray_min_media_xfeed_dim,
       "tray-prompt": tray_prompt,
       "intrays": intrays,
       "intray1": intray1,
       "tray1-media-size-loaded": tray1_media_size_loaded,
       "tray1-phd": tray1_phd,
       "intray2": intray2,
       "tray2-media-size-loaded": tray2_media_size_loaded,
       "tray2-phd": tray2_phd,
       "intray3": intray3,
       "tray3-media-size-loaded": tray3_media_size_loaded,
       "tray3-phd": tray3_phd,
       "intray5": intray5,
       "tray5-media-size-loaded": tray5_media_size_loaded,
       "tray5-phd": tray5_phd,
       "intray6": intray6,
       "tray6-media-size-loaded": tray6_media_size_loaded,
       "tray6-phd": tray6_phd,
       "outbin": outbin,
       "settings-outbin": settings_outbin,
       "overflow-bin": overflow_bin,
       "outbins": outbins,
       "outbin1": outbin1,
       "outbin1-override-mode": outbin1_override_mode,
       "outbin1-maximum-binding": outbin1_maximum_binding,
       "outbin1-phd": outbin1_phd,
       "outbin1-error-info": outbin1_error_info,
       "outbin2": outbin2,
       "outbin2-override-mode": outbin2_override_mode,
       "outbin2-maximum-binding": outbin2_maximum_binding,
       "outbin2-phd": outbin2_phd,
       "outbin2-error-info": outbin2_error_info,
       "outbin3": outbin3,
       "outbin3-override-mode": outbin3_override_mode,
       "outbin3-maximum-binding": outbin3_maximum_binding,
       "outbin3-phd": outbin3_phd,
       "outbin3-error-info": outbin3_error_info,
       "outbin4": outbin4,
       "outbin4-override-mode": outbin4_override_mode,
       "outbin4-maximum-binding": outbin4_maximum_binding,
       "outbin4-phd": outbin4_phd,
       "outbin4-error-info": outbin4_error_info,
       "outbin5": outbin5,
       "outbin5-override-mode": outbin5_override_mode,
       "outbin5-maximum-binding": outbin5_maximum_binding,
       "outbin5-phd": outbin5_phd,
       "outbin5-error-info": outbin5_error_info,
       "imaging": imaging,
       "print-quality-level": print_quality_level,
       "ph": ph,
       "settings-ph": settings_ph,
       "tray-disable-use-instead": tray_disable_use_instead,
       "ph-devices": ph_devices,
       "ph2": ph2,
       "phd2-device-specific-command": phd2_device_specific_command,
       "print-media": print_media,
       "settings-print-media": settings_print_media,
       "media-names-available": media_names_available,
       "north-edge-offset": north_edge_offset,
       "media-info": media_info,
       "media1": media1,
       "media1-name": media1_name,
       "media1-short-name": media1_short_name,
       "media1-page-count": media1_page_count,
       "media2": media2,
       "media2-name": media2_name,
       "media2-short-name": media2_short_name,
       "media2-page-count": media2_page_count,
       "media3": media3,
       "media3-name": media3_name,
       "media3-short-name": media3_short_name,
       "media3-page-count": media3_page_count,
       "media4": media4,
       "media4-name": media4_name,
       "media4-short-name": media4_short_name,
       "media4-page-count": media4_page_count,
       "media5": media5,
       "media5-name": media5_name,
       "media5-short-name": media5_short_name,
       "media5-page-count": media5_page_count,
       "media6": media6,
       "media6-name": media6_name,
       "media6-short-name": media6_short_name,
       "media6-page-count": media6_page_count,
       "media7": media7,
       "media7-name": media7_name,
       "media7-short-name": media7_short_name,
       "media7-page-count": media7_page_count,
       "media8": media8,
       "media8-name": media8_name,
       "media8-short-name": media8_short_name,
       "media8-page-count": media8_page_count,
       "media9": media9,
       "media9-name": media9_name,
       "media9-short-name": media9_short_name,
       "media9-page-count": media9_page_count,
       "media10": media10,
       "media10-name": media10_name,
       "media10-short-name": media10_short_name,
       "media10-page-count": media10_page_count,
       "media11": media11,
       "media11-name": media11_name,
       "media11-short-name": media11_short_name,
       "media11-page-count": media11_page_count,
       "media12": media12,
       "media12-name": media12_name,
       "media12-short-name": media12_short_name,
       "media12-page-count": media12_page_count,
       "media13": media13,
       "media13-name": media13_name,
       "media13-short-name": media13_short_name,
       "media13-page-count": media13_page_count,
       "media14": media14,
       "media14-name": media14_name,
       "media14-short-name": media14_short_name,
       "media14-page-count": media14_page_count,
       "media15": media15,
       "media15-name": media15_name,
       "media15-short-name": media15_short_name,
       "media15-page-count": media15_page_count,
       "media16": media16,
       "media16-name": media16_name,
       "media16-short-name": media16_short_name,
       "media16-page-count": media16_page_count,
       "media17": media17,
       "media17-name": media17_name,
       "media17-short-name": media17_short_name,
       "media17-page-count": media17_page_count,
       "media18": media18,
       "media18-name": media18_name,
       "media18-short-name": media18_short_name,
       "media18-page-count": media18_page_count,
       "media19": media19,
       "media19-name": media19_name,
       "media19-short-name": media19_short_name,
       "media19-page-count": media19_page_count,
       "media-size": media_size,
       "media-size-count": media_size_count,
       "media-size-west-edge-first-side-offset": media_size_west_edge_first_side_offset,
       "media-size-west-edge-second-side-offset": media_size_west_edge_second_side_offset,
       "media-size-west-edge-side-offset-by-tray": media_size_west_edge_side_offset_by_tray,
       "media-counts": media_counts,
       "non-assured-oht-page-count": non_assured_oht_page_count,
       "media-types": media_types,
       "media-number-of-type-supported": media_number_of_type_supported,
       "consumables": consumables,
       "consumables-1": consumables_1,
       "consumable-status": consumable_status,
       "consumable-status-capacity-units": consumable_status_capacity_units,
       "consumable-status-total-capacity": consumable_status_total_capacity,
       "consumable-status-expiration-date": consumable_status_expiration_date,
       "consumable-reorder-url": consumable_reorder_url,
       "consumables-status": consumables_status,
       "consumables-life": consumables_life,
       "consumable-life-usage-units-remaining": consumable_life_usage_units_remaining,
       "consumable-life-usage-units": consumable_life_usage_units,
       "consumable-life-low-threshold": consumable_life_low_threshold,
       "consumable-current-state": consumable_current_state,
       "consumable-string": consumable_string,
       "consumable-string-information": consumable_string_information,
       "consumable-string-information-reset": consumable_string_information_reset,
       "consumable-notification-status": consumable_notification_status,
       "consumable-pages-printed-with-supply": consumable_pages_printed_with_supply}
)
