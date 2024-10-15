# SNMP MIB module (LJ4730-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/LJ4730-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:18:46 2024
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
_NetPMLmgmt_ObjectIdentity = ObjectIdentity
netPMLmgmt = _NetPMLmgmt_ObjectIdentity(
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


class _Color_supply_out_action_Type(Integer32):
    """Custom type color_supply_out_action based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eAutoContinueBlack", 2),
          ("eStop", 1))
    )


_Color_supply_out_action_Type.__name__ = "Integer32"
_Color_supply_out_action_Object = MibScalar
color_supply_out_action = _Color_supply_out_action_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 1, 34),
    _Color_supply_out_action_Type()
)
color_supply_out_action.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    color_supply_out_action.setStatus("optional")


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
            1
        )
    )
    namedValues = NamedValues(
        ("eInitiateAction", 1)
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
        ValueSizeConstraint(0, 20),
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
        ValueSizeConstraint(0, 20),
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
_Background_message3_ObjectIdentity = ObjectIdentity
background_message3 = _Background_message3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 2, 37, 3)
)


class _Background_status_msg_line3_part1_Type(OctetString):
    """Custom type background_status_msg_line3_part1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_Background_status_msg_line3_part1_Type.__name__ = "OctetString"
_Background_status_msg_line3_part1_Object = MibScalar
background_status_msg_line3_part1 = _Background_status_msg_line3_part1_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 2, 37, 3, 1),
    _Background_status_msg_line3_part1_Type()
)
background_status_msg_line3_part1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    background_status_msg_line3_part1.setStatus("optional")
_Background_message4_ObjectIdentity = ObjectIdentity
background_message4 = _Background_message4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 2, 37, 4)
)


class _Background_status_msg_line4_part1_Type(OctetString):
    """Custom type background_status_msg_line4_part1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_Background_status_msg_line4_part1_Type.__name__ = "OctetString"
_Background_status_msg_line4_part1_Object = MibScalar
background_status_msg_line4_part1 = _Background_status_msg_line4_part1_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 2, 37, 4, 1),
    _Background_status_msg_line4_part1_Type()
)
background_status_msg_line4_part1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    background_status_msg_line4_part1.setStatus("optional")


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
_Simm_ObjectIdentity = ObjectIdentity
simm = _Simm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 1)
)
_Simm1_ObjectIdentity = ObjectIdentity
simm1 = _Simm1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 1, 1)
)


class _Simm1_type_Type(Integer32):
    """Custom type simm1_type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              7,
              9)
        )
    )
    namedValues = NamedValues(
        *(("eEmpty", 1),
          ("eFlashMemory", 7),
          ("eRamRom", 9),
          ("eReadOnlyMemory", 4),
          ("eUnSupported", 3),
          ("eUnknown", 2),
          ("eVolatileRandomAccessMemory", 5))
    )


_Simm1_type_Type.__name__ = "Integer32"
_Simm1_type_Object = MibScalar
simm1_type = _Simm1_type_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 1, 1, 4),
    _Simm1_type_Type()
)
simm1_type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simm1_type.setStatus("optional")
_Simm1_capacity_Type = Integer32
_Simm1_capacity_Object = MibScalar
simm1_capacity = _Simm1_capacity_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 1, 1, 5),
    _Simm1_capacity_Type()
)
simm1_capacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simm1_capacity.setStatus("optional")
_Simm1_bank_ObjectIdentity = ObjectIdentity
simm1_bank = _Simm1_bank_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 1, 1, 6)
)
_Simm1_bank1_ObjectIdentity = ObjectIdentity
simm1_bank1 = _Simm1_bank1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 1, 1, 6, 1)
)


class _Simm1_bank1_type_Type(Integer32):
    """Custom type simm1_bank1_type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              7,
              9)
        )
    )
    namedValues = NamedValues(
        *(("eEmpty", 1),
          ("eFlashMemory", 7),
          ("eRamRom", 9),
          ("eReadOnlyMemory", 4),
          ("eUnSupported", 3),
          ("eUnknown", 2),
          ("eVolatileRandomAccessMemory", 5))
    )


_Simm1_bank1_type_Type.__name__ = "Integer32"
_Simm1_bank1_type_Object = MibScalar
simm1_bank1_type = _Simm1_bank1_type_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 1, 1, 6, 1, 1),
    _Simm1_bank1_type_Type()
)
simm1_bank1_type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simm1_bank1_type.setStatus("optional")
_Simm1_bank1_capacity_Type = Integer32
_Simm1_bank1_capacity_Object = MibScalar
simm1_bank1_capacity = _Simm1_bank1_capacity_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 1, 1, 6, 1, 2),
    _Simm1_bank1_capacity_Type()
)
simm1_bank1_capacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simm1_bank1_capacity.setStatus("optional")
_Simm1_bank2_ObjectIdentity = ObjectIdentity
simm1_bank2 = _Simm1_bank2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 1, 1, 6, 2)
)


class _Simm1_bank2_type_Type(Integer32):
    """Custom type simm1_bank2_type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              7,
              9)
        )
    )
    namedValues = NamedValues(
        *(("eEmpty", 1),
          ("eFlashMemory", 7),
          ("eRamRom", 9),
          ("eReadOnlyMemory", 4),
          ("eUnSupported", 3),
          ("eUnknown", 2),
          ("eVolatileRandomAccessMemory", 5))
    )


_Simm1_bank2_type_Type.__name__ = "Integer32"
_Simm1_bank2_type_Object = MibScalar
simm1_bank2_type = _Simm1_bank2_type_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 1, 1, 6, 2, 1),
    _Simm1_bank2_type_Type()
)
simm1_bank2_type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simm1_bank2_type.setStatus("optional")
_Simm1_bank2_capacity_Type = Integer32
_Simm1_bank2_capacity_Object = MibScalar
simm1_bank2_capacity = _Simm1_bank2_capacity_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 1, 1, 6, 2, 2),
    _Simm1_bank2_capacity_Type()
)
simm1_bank2_capacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simm1_bank2_capacity.setStatus("optional")
_Simm2_ObjectIdentity = ObjectIdentity
simm2 = _Simm2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 1, 2)
)


class _Simm2_type_Type(Integer32):
    """Custom type simm2_type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              7,
              9)
        )
    )
    namedValues = NamedValues(
        *(("eEmpty", 1),
          ("eFlashMemory", 7),
          ("eRamRom", 9),
          ("eReadOnlyMemory", 4),
          ("eUnSupported", 3),
          ("eUnknown", 2),
          ("eVolatileRandomAccessMemory", 5))
    )


_Simm2_type_Type.__name__ = "Integer32"
_Simm2_type_Object = MibScalar
simm2_type = _Simm2_type_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 1, 2, 4),
    _Simm2_type_Type()
)
simm2_type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simm2_type.setStatus("optional")
_Simm2_capacity_Type = Integer32
_Simm2_capacity_Object = MibScalar
simm2_capacity = _Simm2_capacity_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 1, 2, 5),
    _Simm2_capacity_Type()
)
simm2_capacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simm2_capacity.setStatus("optional")
_Simm2_bank_ObjectIdentity = ObjectIdentity
simm2_bank = _Simm2_bank_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 1, 2, 6)
)
_Simm2_bank1_ObjectIdentity = ObjectIdentity
simm2_bank1 = _Simm2_bank1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 1, 2, 6, 1)
)


class _Simm2_bank1_type_Type(Integer32):
    """Custom type simm2_bank1_type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              7,
              9)
        )
    )
    namedValues = NamedValues(
        *(("eEmpty", 1),
          ("eFlashMemory", 7),
          ("eRamRom", 9),
          ("eReadOnlyMemory", 4),
          ("eUnSupported", 3),
          ("eUnknown", 2),
          ("eVolatileRandomAccessMemory", 5))
    )


_Simm2_bank1_type_Type.__name__ = "Integer32"
_Simm2_bank1_type_Object = MibScalar
simm2_bank1_type = _Simm2_bank1_type_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 1, 2, 6, 1, 1),
    _Simm2_bank1_type_Type()
)
simm2_bank1_type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simm2_bank1_type.setStatus("optional")
_Simm2_bank1_capacity_Type = Integer32
_Simm2_bank1_capacity_Object = MibScalar
simm2_bank1_capacity = _Simm2_bank1_capacity_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 1, 2, 6, 1, 2),
    _Simm2_bank1_capacity_Type()
)
simm2_bank1_capacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simm2_bank1_capacity.setStatus("optional")
_Simm2_bank2_ObjectIdentity = ObjectIdentity
simm2_bank2 = _Simm2_bank2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 1, 2, 6, 2)
)


class _Simm2_bank2_type_Type(Integer32):
    """Custom type simm2_bank2_type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              7,
              9)
        )
    )
    namedValues = NamedValues(
        *(("eEmpty", 1),
          ("eFlashMemory", 7),
          ("eRamRom", 9),
          ("eReadOnlyMemory", 4),
          ("eUnSupported", 3),
          ("eUnknown", 2),
          ("eVolatileRandomAccessMemory", 5))
    )


_Simm2_bank2_type_Type.__name__ = "Integer32"
_Simm2_bank2_type_Object = MibScalar
simm2_bank2_type = _Simm2_bank2_type_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 1, 2, 6, 2, 1),
    _Simm2_bank2_type_Type()
)
simm2_bank2_type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simm2_bank2_type.setStatus("optional")
_Simm2_bank2_capacity_Type = Integer32
_Simm2_bank2_capacity_Object = MibScalar
simm2_bank2_capacity = _Simm2_bank2_capacity_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 1, 2, 6, 2, 2),
    _Simm2_bank2_capacity_Type()
)
simm2_bank2_capacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simm2_bank2_capacity.setStatus("optional")
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
_Mio2_ObjectIdentity = ObjectIdentity
mio2 = _Mio2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 3, 2)
)
_Mio2_model_name_Type = OctetString
_Mio2_model_name_Object = MibScalar
mio2_model_name = _Mio2_model_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 3, 2, 2),
    _Mio2_model_name_Type()
)
mio2_model_name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mio2_model_name.setStatus("optional")
_Mio2_manufacturing_info_Type = OctetString
_Mio2_manufacturing_info_Object = MibScalar
mio2_manufacturing_info = _Mio2_manufacturing_info_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 3, 2, 3),
    _Mio2_manufacturing_info_Type()
)
mio2_manufacturing_info.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mio2_manufacturing_info.setStatus("optional")


class _Mio2_type_Type(Integer32):
    """Custom type mio2_type based on Integer32"""
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


_Mio2_type_Type.__name__ = "Integer32"
_Mio2_type_Object = MibScalar
mio2_type = _Mio2_type_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 3, 2, 4),
    _Mio2_type_Type()
)
mio2_type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mio2_type.setStatus("optional")
_Mio3_ObjectIdentity = ObjectIdentity
mio3 = _Mio3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 3, 3)
)
_Mio3_model_name_Type = OctetString
_Mio3_model_name_Object = MibScalar
mio3_model_name = _Mio3_model_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 3, 3, 2),
    _Mio3_model_name_Type()
)
mio3_model_name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mio3_model_name.setStatus("optional")
_Mio3_manufacturing_info_Type = OctetString
_Mio3_manufacturing_info_Object = MibScalar
mio3_manufacturing_info = _Mio3_manufacturing_info_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 3, 3, 3),
    _Mio3_manufacturing_info_Type()
)
mio3_manufacturing_info.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mio3_manufacturing_info.setStatus("optional")


class _Mio3_type_Type(Integer32):
    """Custom type mio3_type based on Integer32"""
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


_Mio3_type_Type.__name__ = "Integer32"
_Mio3_type_Object = MibScalar
mio3_type = _Mio3_type_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 3, 3, 4),
    _Mio3_type_Type()
)
mio3_type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mio3_type.setStatus("optional")
_Web_server_ObjectIdentity = ObjectIdentity
web_server = _Web_server_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 6)
)
_Settings_web_server_ObjectIdentity = ObjectIdentity
settings_web_server = _Settings_web_server_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 6, 1)
)


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
_Socket_ping_ObjectIdentity = ObjectIdentity
socket_ping = _Socket_ping_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 7)
)


class _Socket_ping_job_events_version_Type(OctetString):
    """Custom type socket_ping_job_events_version based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_Socket_ping_job_events_version_Type.__name__ = "OctetString"
_Socket_ping_job_events_version_Object = MibScalar
socket_ping_job_events_version = _Socket_ping_job_events_version_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 7, 1),
    _Socket_ping_job_events_version_Type()
)
socket_ping_job_events_version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    socket_ping_job_events_version.setStatus("optional")
_Test_ObjectIdentity = ObjectIdentity
test = _Test_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 5)
)
_Engine_self_diagnostic_Type = OctetString
_Engine_self_diagnostic_Object = MibScalar
engine_self_diagnostic = _Engine_self_diagnostic_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 5, 7),
    _Engine_self_diagnostic_Type()
)
engine_self_diagnostic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engine_self_diagnostic.setStatus("optional")
_Engine_parameter_Type = OctetString
_Engine_parameter_Object = MibScalar
engine_parameter = _Engine_parameter_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 5, 8),
    _Engine_parameter_Type()
)
engine_parameter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engine_parameter.setStatus("optional")
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
_Job_info_outbins_used_Type = OctetString
_Job_info_outbins_used_Object = MibScalar
job_info_outbins_used = _Job_info_outbins_used_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 5, 20),
    _Job_info_outbins_used_Type()
)
job_info_outbins_used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    job_info_outbins_used.setStatus("optional")
_Job_info_physical_outbins_used_Type = OctetString
_Job_info_physical_outbins_used_Object = MibScalar
job_info_physical_outbins_used = _Job_info_physical_outbins_used_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 5, 22),
    _Job_info_physical_outbins_used_Type()
)
job_info_physical_outbins_used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    job_info_physical_outbins_used.setStatus("optional")
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
_Job_info_requested_originals_Type = Integer32
_Job_info_requested_originals_Object = MibScalar
job_info_requested_originals = _Job_info_requested_originals_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 5, 24),
    _Job_info_requested_originals_Type()
)
job_info_requested_originals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    job_info_requested_originals.setStatus("optional")
_Job_info_page_count_current_original_Type = Integer32
_Job_info_page_count_current_original_Object = MibScalar
job_info_page_count_current_original = _Job_info_page_count_current_original_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 5, 25),
    _Job_info_page_count_current_original_Type()
)
job_info_page_count_current_original.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    job_info_page_count_current_original.setStatus("optional")
_Job_info_pages_in_original_Type = Integer32
_Job_info_pages_in_original_Object = MibScalar
job_info_pages_in_original = _Job_info_pages_in_original_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 5, 26),
    _Job_info_pages_in_original_Type()
)
job_info_pages_in_original.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    job_info_pages_in_original.setStatus("optional")
_Job_info_printed_originals_Type = Integer32
_Job_info_printed_originals_Object = MibScalar
job_info_printed_originals = _Job_info_printed_originals_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 5, 27),
    _Job_info_printed_originals_Type()
)
job_info_printed_originals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    job_info_printed_originals.setStatus("optional")
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
              20)
        )
    )
    namedValues = NamedValues(
        *(("eBond", 4),
          ("eCardStock", 11),
          ("eColored", 10),
          ("eHeavy", 14),
          ("eLabels", 8),
          ("eLetterhead", 5),
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


class _Job_info_accounting_scanned_media_simplex_count_Type(OctetString):
    """Custom type job_info_accounting_scanned_media_simplex_count based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_Job_info_accounting_scanned_media_simplex_count_Type.__name__ = "OctetString"
_Job_info_accounting_scanned_media_simplex_count_Object = MibScalar
job_info_accounting_scanned_media_simplex_count = _Job_info_accounting_scanned_media_simplex_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 5, 28, 12),
    _Job_info_accounting_scanned_media_simplex_count_Type()
)
job_info_accounting_scanned_media_simplex_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    job_info_accounting_scanned_media_simplex_count.setStatus("optional")


class _Job_info_accounting_scanned_media_duplex_count_Type(OctetString):
    """Custom type job_info_accounting_scanned_media_duplex_count based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_Job_info_accounting_scanned_media_duplex_count_Type.__name__ = "OctetString"
_Job_info_accounting_scanned_media_duplex_count_Object = MibScalar
job_info_accounting_scanned_media_duplex_count = _Job_info_accounting_scanned_media_duplex_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 5, 28, 13),
    _Job_info_accounting_scanned_media_duplex_count_Type()
)
job_info_accounting_scanned_media_duplex_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    job_info_accounting_scanned_media_duplex_count.setStatus("optional")


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
held_job_set_queue_size.setMaxAccess("read-write")
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
_Usage_average_toner_coverage_Type = OctetString
_Usage_average_toner_coverage_Object = MibScalar
usage_average_toner_coverage = _Usage_average_toner_coverage_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 16, 1, 3),
    _Usage_average_toner_coverage_Type()
)
usage_average_toner_coverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usage_average_toner_coverage.setStatus("optional")


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
_Printed_modes_usage_total_Type = Integer32
_Printed_modes_usage_total_Object = MibScalar
printed_modes_usage_total = _Printed_modes_usage_total_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 16, 1, 9),
    _Printed_modes_usage_total_Type()
)
printed_modes_usage_total.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    printed_modes_usage_total.setStatus("optional")
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
_Scanner_accounting_ObjectIdentity = ObjectIdentity
scanner_accounting = _Scanner_accounting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 16, 2)
)
_Scanned_media_usage_ObjectIdentity = ObjectIdentity
scanned_media_usage = _Scanned_media_usage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 16, 2, 1)
)


class _Scanned_media_simplex_count_Type(Integer32):
    """Custom type scanned_media_simplex_count based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 930576247),
    )


_Scanned_media_simplex_count_Type.__name__ = "Integer32"
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
_Printed_modes_accounting_ObjectIdentity = ObjectIdentity
printed_modes_accounting = _Printed_modes_accounting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 16, 4)
)
_Printed_modes_usage_ObjectIdentity = ObjectIdentity
printed_modes_usage = _Printed_modes_usage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 16, 4, 1)
)
_Printed_modes_mono_count_Type = Integer32
_Printed_modes_mono_count_Object = MibScalar
printed_modes_mono_count = _Printed_modes_mono_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 16, 4, 1, 1),
    _Printed_modes_mono_count_Type()
)
printed_modes_mono_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    printed_modes_mono_count.setStatus("optional")
_Printed_modes_color_count_Type = Integer32
_Printed_modes_color_count_Object = MibScalar
printed_modes_color_count = _Printed_modes_color_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 16, 4, 1, 3),
    _Printed_modes_color_count_Type()
)
printed_modes_color_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    printed_modes_color_count.setStatus("optional")
_Printed_modes_total_count_Type = Integer32
_Printed_modes_total_count_Object = MibScalar
printed_modes_total_count = _Printed_modes_total_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 16, 4, 1, 5),
    _Printed_modes_total_count_Type()
)
printed_modes_total_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    printed_modes_total_count.setStatus("optional")
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


class _Scan_sharpening_coefficient_Type(Integer32):
    """Custom type scan_sharpening_coefficient based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_Scan_sharpening_coefficient_Type.__name__ = "Integer32"
_Scan_sharpening_coefficient_Object = MibScalar
scan_sharpening_coefficient = _Scan_sharpening_coefficient_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 1, 15),
    _Scan_sharpening_coefficient_Type()
)
scan_sharpening_coefficient.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scan_sharpening_coefficient.setStatus("optional")


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
_Scanner_accessory_total_copy_pages_printed_Type = Integer32
_Scanner_accessory_total_copy_pages_printed_Object = MibScalar
scanner_accessory_total_copy_pages_printed = _Scanner_accessory_total_copy_pages_printed_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 1, 63),
    _Scanner_accessory_total_copy_pages_printed_Type()
)
scanner_accessory_total_copy_pages_printed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scanner_accessory_total_copy_pages_printed.setStatus("optional")
_Scanner_accessory_digital_send_module_url_Type = OctetString
_Scanner_accessory_digital_send_module_url_Object = MibScalar
scanner_accessory_digital_send_module_url = _Scanner_accessory_digital_send_module_url_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 1, 64),
    _Scanner_accessory_digital_send_module_url_Type()
)
scanner_accessory_digital_send_module_url.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scanner_accessory_digital_send_module_url.setStatus("optional")
_Scanner_accessory_digital_send_status_Type = Integer32
_Scanner_accessory_digital_send_status_Object = MibScalar
scanner_accessory_digital_send_status = _Scanner_accessory_digital_send_status_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 1, 65),
    _Scanner_accessory_digital_send_status_Type()
)
scanner_accessory_digital_send_status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scanner_accessory_digital_send_status.setStatus("optional")


class _Default_scan_original_size_Type(Integer32):
    """Custom type default_scan_original_size based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              10,
              15,
              25,
              26,
              45,
              32767)
        )
    )
    namedValues = NamedValues(
        *(("eFoolscap", 10),
          ("eISOandJISA4", 26),
          ("eISOandJISA5", 25),
          ("eJISB5", 45),
          ("eStatement", 15),
          ("eUSExecutive", 1),
          ("eUSLegal", 3),
          ("eUSLetter", 2),
          ("eUnknownMediaSize", 32767))
    )


_Default_scan_original_size_Type.__name__ = "Integer32"
_Default_scan_original_size_Object = MibScalar
default_scan_original_size = _Default_scan_original_size_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 1, 66),
    _Default_scan_original_size_Type()
)
default_scan_original_size.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    default_scan_original_size.setStatus("optional")


class _Default_scan_text_graphics_mix_Type(Integer32):
    """Custom type default_scan_text_graphics_mix based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_Default_scan_text_graphics_mix_Type.__name__ = "Integer32"
_Default_scan_text_graphics_mix_Object = MibScalar
default_scan_text_graphics_mix = _Default_scan_text_graphics_mix_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 1, 67),
    _Default_scan_text_graphics_mix_Type()
)
default_scan_text_graphics_mix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    default_scan_text_graphics_mix.setStatus("optional")


class _Default_scan_job_mode_Type(Integer32):
    """Custom type default_scan_job_mode based on Integer32"""
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


_Default_scan_job_mode_Type.__name__ = "Integer32"
_Default_scan_job_mode_Object = MibScalar
default_scan_job_mode = _Default_scan_job_mode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 1, 68),
    _Default_scan_job_mode_Type()
)
default_scan_job_mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    default_scan_job_mode.setStatus("optional")


class _Default_scan_background_removal_Type(Integer32):
    """Custom type default_scan_background_removal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_Default_scan_background_removal_Type.__name__ = "Integer32"
_Default_scan_background_removal_Object = MibScalar
default_scan_background_removal = _Default_scan_background_removal_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 1, 69),
    _Default_scan_background_removal_Type()
)
default_scan_background_removal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    default_scan_background_removal.setStatus("optional")


class _Default_scan_image_quality_Type(Integer32):
    """Custom type default_scan_image_quality based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eBest", 2),
          ("eNormal", 1))
    )


_Default_scan_image_quality_Type.__name__ = "Integer32"
_Default_scan_image_quality_Object = MibScalar
default_scan_image_quality = _Default_scan_image_quality_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 1, 70),
    _Default_scan_image_quality_Type()
)
default_scan_image_quality.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    default_scan_image_quality.setStatus("optional")


class _Default_scan_content_orientation_Type(Integer32):
    """Custom type default_scan_content_orientation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eLandscape", 2),
          ("ePortrait", 1))
    )


_Default_scan_content_orientation_Type.__name__ = "Integer32"
_Default_scan_content_orientation_Object = MibScalar
default_scan_content_orientation = _Default_scan_content_orientation_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 1, 71),
    _Default_scan_content_orientation_Type()
)
default_scan_content_orientation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    default_scan_content_orientation.setStatus("optional")


class _Auto_send_reset_Type(Integer32):
    """Custom type auto_send_reset based on Integer32"""
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


_Auto_send_reset_Type.__name__ = "Integer32"
_Auto_send_reset_Object = MibScalar
auto_send_reset = _Auto_send_reset_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 1, 78),
    _Auto_send_reset_Type()
)
auto_send_reset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    auto_send_reset.setStatus("optional")


class _Scanner_accessory_digital_send_log_event_counter_Type(Integer32):
    """Custom type scanner_accessory_digital_send_log_event_counter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_Scanner_accessory_digital_send_log_event_counter_Type.__name__ = "Integer32"
_Scanner_accessory_digital_send_log_event_counter_Object = MibScalar
scanner_accessory_digital_send_log_event_counter = _Scanner_accessory_digital_send_log_event_counter_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 1, 79),
    _Scanner_accessory_digital_send_log_event_counter_Type()
)
scanner_accessory_digital_send_log_event_counter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scanner_accessory_digital_send_log_event_counter.setStatus("optional")


class _Scanner_accessory_digital_send_config_email_gateway_Type(OctetString):
    """Custom type scanner_accessory_digital_send_config_email_gateway based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Scanner_accessory_digital_send_config_email_gateway_Type.__name__ = "OctetString"
_Scanner_accessory_digital_send_config_email_gateway_Object = MibScalar
scanner_accessory_digital_send_config_email_gateway = _Scanner_accessory_digital_send_config_email_gateway_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 1, 80),
    _Scanner_accessory_digital_send_config_email_gateway_Type()
)
scanner_accessory_digital_send_config_email_gateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scanner_accessory_digital_send_config_email_gateway.setStatus("optional")


class _Scanner_accessory_digital_send_config_ldap_gateway_Type(OctetString):
    """Custom type scanner_accessory_digital_send_config_ldap_gateway based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Scanner_accessory_digital_send_config_ldap_gateway_Type.__name__ = "OctetString"
_Scanner_accessory_digital_send_config_ldap_gateway_Object = MibScalar
scanner_accessory_digital_send_config_ldap_gateway = _Scanner_accessory_digital_send_config_ldap_gateway_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 1, 81),
    _Scanner_accessory_digital_send_config_ldap_gateway_Type()
)
scanner_accessory_digital_send_config_ldap_gateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scanner_accessory_digital_send_config_ldap_gateway.setStatus("optional")


class _Scanner_accessory_digital_send_config_dsm_enabled_fax_Type(Integer32):
    """Custom type scanner_accessory_digital_send_config_dsm_enabled_fax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_Scanner_accessory_digital_send_config_dsm_enabled_fax_Type.__name__ = "Integer32"
_Scanner_accessory_digital_send_config_dsm_enabled_fax_Object = MibScalar
scanner_accessory_digital_send_config_dsm_enabled_fax = _Scanner_accessory_digital_send_config_dsm_enabled_fax_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 1, 82),
    _Scanner_accessory_digital_send_config_dsm_enabled_fax_Type()
)
scanner_accessory_digital_send_config_dsm_enabled_fax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scanner_accessory_digital_send_config_dsm_enabled_fax.setStatus("optional")


class _Scanner_accessory_digital_send_config_fax_embedded_Type(Integer32):
    """Custom type scanner_accessory_digital_send_config_fax_embedded based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_Scanner_accessory_digital_send_config_fax_embedded_Type.__name__ = "Integer32"
_Scanner_accessory_digital_send_config_fax_embedded_Object = MibScalar
scanner_accessory_digital_send_config_fax_embedded = _Scanner_accessory_digital_send_config_fax_embedded_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 1, 83),
    _Scanner_accessory_digital_send_config_fax_embedded_Type()
)
scanner_accessory_digital_send_config_fax_embedded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scanner_accessory_digital_send_config_fax_embedded.setStatus("optional")


class _Default_scanner_speed_Type(Integer32):
    """Custom type default_scanner_speed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e25ppm", 1),
          ("e50ppm", 2))
    )


_Default_scanner_speed_Type.__name__ = "Integer32"
_Default_scanner_speed_Object = MibScalar
default_scanner_speed = _Default_scanner_speed_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 1, 88),
    _Default_scanner_speed_Type()
)
default_scanner_speed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    default_scanner_speed.setStatus("optional")


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


class _Scanner_accessory_digital_send_home_screen_status_Type(OctetString):
    """Custom type scanner_accessory_digital_send_home_screen_status based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(50, 50),
    )


_Scanner_accessory_digital_send_home_screen_status_Type.__name__ = "OctetString"
_Scanner_accessory_digital_send_home_screen_status_Object = MibScalar
scanner_accessory_digital_send_home_screen_status = _Scanner_accessory_digital_send_home_screen_status_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 1, 91),
    _Scanner_accessory_digital_send_home_screen_status_Type()
)
scanner_accessory_digital_send_home_screen_status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scanner_accessory_digital_send_home_screen_status.setStatus("optional")
_Status_scanner_ObjectIdentity = ObjectIdentity
status_scanner = _Status_scanner_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 2)
)
_Not_ready_source_scanner_Type = OctetString
_Not_ready_source_scanner_Object = MibScalar
not_ready_source_scanner = _Not_ready_source_scanner_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 2, 1),
    _Not_ready_source_scanner_Type()
)
not_ready_source_scanner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    not_ready_source_scanner.setStatus("optional")
_Scan_calibration_download_Type = OctetString
_Scan_calibration_download_Object = MibScalar
scan_calibration_download = _Scan_calibration_download_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 2, 5),
    _Scan_calibration_download_Type()
)
scan_calibration_download.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scan_calibration_download.setStatus("optional")


class _Scan_calibration_error_Type(Integer32):
    """Custom type scan_calibration_error based on Integer32"""
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
        *(("eADFJam", 8),
          ("eADFMispick", 7),
          ("eLowMemory", 4),
          ("eNoError", 1),
          ("eScannerBusy", 6),
          ("eScannerFeederEmpty", 3),
          ("eUncorrectablePixels", 9),
          ("eUnknownCalibrationError", 2),
          ("eWriteFailed", 5))
    )


_Scan_calibration_error_Type.__name__ = "Integer32"
_Scan_calibration_error_Object = MibScalar
scan_calibration_error = _Scan_calibration_error_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 2, 6),
    _Scan_calibration_error_Type()
)
scan_calibration_error.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scan_calibration_error.setStatus("optional")
_Spooler_ObjectIdentity = ObjectIdentity
spooler = _Spooler_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 4)
)
_Settings_spooler_ObjectIdentity = ObjectIdentity
settings_spooler = _Settings_spooler_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 4, 1)
)


class _Mopy_mode_Type(Integer32):
    """Custom type mopy_mode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("eEnhanced", 5),
          ("eOff", 1),
          ("eStandard", 4))
    )


_Mopy_mode_Type.__name__ = "Integer32"
_Mopy_mode_Object = MibScalar
mopy_mode = _Mopy_mode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 4, 1, 1),
    _Mopy_mode_Type()
)
mopy_mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mopy_mode.setStatus("optional")
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
              15,
              17,
              18,
              25,
              26,
              45,
              72,
              80,
              81,
              90,
              91,
              100,
              101,
              32767)
        )
    )
    namedValues = NamedValues(
        *(("eCommercial10", 81),
          ("eCustom", 101),
          ("eFoolscap", 10),
          ("eISOandJISA4", 26),
          ("eISOandJISA5", 25),
          ("eInternationalB5", 100),
          ("eInternationalC5", 91),
          ("eInternationalDL", 90),
          ("eJISB5", 45),
          ("eJISExecutive", 18),
          ("eJapanesePostcardDouble", 72),
          ("eMonarch", 80),
          ("eROC16K", 17),
          ("eStatement", 15),
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
_Pcl_default_font_height_Type = Integer32
_Pcl_default_font_height_Object = MibScalar
pcl_default_font_height = _Pcl_default_font_height_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 3, 3, 13),
    _Pcl_default_font_height_Type()
)
pcl_default_font_height.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pcl_default_font_height.setStatus("optional")


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
_Pcl_default_font_width_Type = Integer32
_Pcl_default_font_width_Object = MibScalar
pcl_default_font_width = _Pcl_default_font_width_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 3, 3, 16),
    _Pcl_default_font_width_Type()
)
pcl_default_font_width.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pcl_default_font_width.setStatus("optional")
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
_Pml_ObjectIdentity = ObjectIdentity
pml = _Pml_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 4)
)
_Pjl_ObjectIdentity = ObjectIdentity
pjl = _Pjl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 5)
)
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
          ("eJapanesePostcardDouble", 72),
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


_Override_media_size_Type.__name__ = "Integer32"
_Override_media_size_Object = MibScalar
override_media_size = _Override_media_size_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 1, 3),
    _Override_media_size_Type()
)
override_media_size.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    override_media_size.setStatus("optional")
_Marking_agent_density_ObjectIdentity = ObjectIdentity
marking_agent_density = _Marking_agent_density_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 1, 9)
)
_Marking_agent_highlights_density_setting_Type = Integer32
_Marking_agent_highlights_density_setting_Object = MibScalar
marking_agent_highlights_density_setting = _Marking_agent_highlights_density_setting_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 1, 9, 2),
    _Marking_agent_highlights_density_setting_Type()
)
marking_agent_highlights_density_setting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    marking_agent_highlights_density_setting.setStatus("optional")
_Marking_agent_midtones_density_setting_Type = Integer32
_Marking_agent_midtones_density_setting_Object = MibScalar
marking_agent_midtones_density_setting = _Marking_agent_midtones_density_setting_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 1, 9, 3),
    _Marking_agent_midtones_density_setting_Type()
)
marking_agent_midtones_density_setting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    marking_agent_midtones_density_setting.setStatus("optional")
_Marking_agent_shadows_density_setting_Type = Integer32
_Marking_agent_shadows_density_setting_Object = MibScalar
marking_agent_shadows_density_setting = _Marking_agent_shadows_density_setting_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 1, 9, 4),
    _Marking_agent_shadows_density_setting_Type()
)
marking_agent_shadows_density_setting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    marking_agent_shadows_density_setting.setStatus("optional")
_Autocleaning_page_frequency_Type = Integer32
_Autocleaning_page_frequency_Object = MibScalar
autocleaning_page_frequency = _Autocleaning_page_frequency_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 1, 11),
    _Autocleaning_page_frequency_Type()
)
autocleaning_page_frequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autocleaning_page_frequency.setStatus("optional")


class _Autocleaning_page_size_Type(Integer32):
    """Custom type autocleaning_page_size based on Integer32"""
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


_Autocleaning_page_size_Type.__name__ = "Integer32"
_Autocleaning_page_size_Object = MibScalar
autocleaning_page_size = _Autocleaning_page_size_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 1, 12),
    _Autocleaning_page_size_Type()
)
autocleaning_page_size.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autocleaning_page_size.setStatus("optional")


class _Default_audible_feedback_Type(Integer32):
    """Custom type default_audible_feedback based on Integer32"""
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


_Default_audible_feedback_Type.__name__ = "Integer32"
_Default_audible_feedback_Object = MibScalar
default_audible_feedback = _Default_audible_feedback_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 1, 14),
    _Default_audible_feedback_Type()
)
default_audible_feedback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    default_audible_feedback.setStatus("optional")


class _Default_reset_send_timeout_Type(Integer32):
    """Custom type default_reset_send_timeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10000, 300000),
    )


_Default_reset_send_timeout_Type.__name__ = "Integer32"
_Default_reset_send_timeout_Object = MibScalar
default_reset_send_timeout = _Default_reset_send_timeout_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 1, 15),
    _Default_reset_send_timeout_Type()
)
default_reset_send_timeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    default_reset_send_timeout.setStatus("optional")


class _Default_authentication_timeout_Type(Integer32):
    """Custom type default_authentication_timeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300000),
    )


_Default_authentication_timeout_Type.__name__ = "Integer32"
_Default_authentication_timeout_Object = MibScalar
default_authentication_timeout = _Default_authentication_timeout_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 1, 16),
    _Default_authentication_timeout_Type()
)
default_authentication_timeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    default_authentication_timeout.setStatus("optional")


class _Default_staple_mode_Type(Integer32):
    """Custom type default_staple_mode based on Integer32"""
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
        *(("eAngled", 3),
          ("eCustomStapleMode", 7),
          ("eNone", 1),
          ("eNormal", 2),
          ("eOppositeCorner", 8),
          ("eSaddleStitch", 9),
          ("eSixStaples", 6),
          ("eThreeStaples", 5),
          ("eTwoStaples", 4))
    )


_Default_staple_mode_Type.__name__ = "Integer32"
_Default_staple_mode_Object = MibScalar
default_staple_mode = _Default_staple_mode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 1, 17),
    _Default_staple_mode_Type()
)
default_staple_mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    default_staple_mode.setStatus("optional")


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


class _Supplies_replace_action_at_setting_Type(Integer32):
    """Custom type supplies_replace_action_at_setting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("eOverrideAtOut", 4),
          ("eStopAtLow", 1),
          ("eStopAtOut", 2))
    )


_Supplies_replace_action_at_setting_Type.__name__ = "Integer32"
_Supplies_replace_action_at_setting_Object = MibScalar
supplies_replace_action_at_setting = _Supplies_replace_action_at_setting_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 1, 25),
    _Supplies_replace_action_at_setting_Type()
)
supplies_replace_action_at_setting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    supplies_replace_action_at_setting.setStatus("optional")


class _Supply_out_user_configured_override_limit_Type(Integer32):
    """Custom type supply_out_user_configured_override_limit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_Supply_out_user_configured_override_limit_Type.__name__ = "Integer32"
_Supply_out_user_configured_override_limit_Object = MibScalar
supply_out_user_configured_override_limit = _Supply_out_user_configured_override_limit_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 1, 26),
    _Supply_out_user_configured_override_limit_Type()
)
supply_out_user_configured_override_limit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    supply_out_user_configured_override_limit.setStatus("optional")
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
_Printer_cal_dhalf_data_ObjectIdentity = ObjectIdentity
printer_cal_dhalf_data = _Printer_cal_dhalf_data_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 2, 37, 3)
)
_Printer_cal_dhalf_data1_Type = OctetString
_Printer_cal_dhalf_data1_Object = MibScalar
printer_cal_dhalf_data1 = _Printer_cal_dhalf_data1_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 2, 37, 3, 1),
    _Printer_cal_dhalf_data1_Type()
)
printer_cal_dhalf_data1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    printer_cal_dhalf_data1.setStatus("optional")
_Printer_cal_dhalf_data2_Type = OctetString
_Printer_cal_dhalf_data2_Object = MibScalar
printer_cal_dhalf_data2 = _Printer_cal_dhalf_data2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 2, 37, 3, 2),
    _Printer_cal_dhalf_data2_Type()
)
printer_cal_dhalf_data2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    printer_cal_dhalf_data2.setStatus("optional")
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
_Printer_cal_cpr_data_Type = OctetString
_Printer_cal_cpr_data_Object = MibScalar
printer_cal_cpr_data = _Printer_cal_cpr_data_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 2, 38, 3),
    _Printer_cal_cpr_data_Type()
)
printer_cal_cpr_data.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    printer_cal_cpr_data.setStatus("optional")
_Supply_out_action_support_Type = OctetString
_Supply_out_action_support_Object = MibScalar
supply_out_action_support = _Supply_out_action_support_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 2, 48),
    _Supply_out_action_support_Type()
)
supply_out_action_support.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    supply_out_action_support.setStatus("optional")


class _Supply_out_device_state_Type(Integer32):
    """Custom type supply_out_device_state based on Integer32"""
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
        *(("eCartridgeOutOverride", 3),
          ("eMonochromePrintingAfterColorCartridgeOut", 4),
          ("eNoSupplyOut", 1),
          ("eOffline", 2))
    )


_Supply_out_device_state_Type.__name__ = "Integer32"
_Supply_out_device_state_Object = MibScalar
supply_out_device_state = _Supply_out_device_state_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 2, 49),
    _Supply_out_device_state_Type()
)
supply_out_device_state.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    supply_out_device_state.setStatus("optional")
_Supply_after_out_state_Type = OctetString
_Supply_after_out_state_Object = MibScalar
supply_after_out_state = _Supply_after_out_state_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 2, 50),
    _Supply_after_out_state_Type()
)
supply_after_out_state.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    supply_after_out_state.setStatus("optional")
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
              15,
              17,
              18,
              25,
              26,
              45,
              72,
              80,
              81,
              90,
              91,
              100,
              101,
              32764,
              32765)
        )
    )
    namedValues = NamedValues(
        *(("eAnyCustomSize", 32764),
          ("eAnySize", 32765),
          ("eCommercial10", 81),
          ("eCustom", 101),
          ("eFoolscap", 10),
          ("eISOandJISA4", 26),
          ("eISOandJISA5", 25),
          ("eInternationalB5", 100),
          ("eInternationalC5", 91),
          ("eInternationalDL", 90),
          ("eJISB5", 45),
          ("eJISExecutive", 18),
          ("eJapansePostcardDouble", 72),
          ("eMonarch", 80),
          ("eROC16K", 17),
          ("eStatement", 15),
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
              17,
              18,
              25,
              26,
              45,
              101,
              32764,
              32765)
        )
    )
    namedValues = NamedValues(
        *(("eAnyCustomSize", 32764),
          ("eAnySize", 32765),
          ("eCustom", 101),
          ("eFoolscap", 10),
          ("eISOandJISA4", 26),
          ("eISOandJISA5", 25),
          ("eJISB5", 45),
          ("eJISExecutive", 18),
          ("eROC16K", 17),
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
              17,
              18,
              25,
              26,
              45,
              101,
              32764,
              32765)
        )
    )
    namedValues = NamedValues(
        *(("eAnyCustomSize", 32764),
          ("eAnySize", 32765),
          ("eCustom", 101),
          ("eFoolscap", 10),
          ("eISOandJISA4", 26),
          ("eISOandJISA5", 25),
          ("eJISB5", 45),
          ("eJISExecutive", 18),
          ("eROC16K", 17),
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
            *(1,
              2,
              3,
              10,
              17,
              18,
              25,
              26,
              45,
              101,
              32764,
              32765)
        )
    )
    namedValues = NamedValues(
        *(("eAnyCustomSize", 32764),
          ("eAnySize", 32765),
          ("eCustom", 101),
          ("eFoolscap", 10),
          ("eISOandJISA4", 26),
          ("eISOandJISA5", 25),
          ("eJISB5", 45),
          ("eJISExecutive", 18),
          ("eROC16K", 17),
          ("eUSExecutive", 1),
          ("eUSLegal", 3),
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
_Marking_agent_ObjectIdentity = ObjectIdentity
marking_agent = _Marking_agent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 5)
)
_Settings_marking_agent_ObjectIdentity = ObjectIdentity
settings_marking_agent = _Settings_marking_agent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 5, 1)
)


class _Marker_density_calibration_Type(Integer32):
    """Custom type marker_density_calibration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("eCalibrateALL", 2),
          ("eCalibrateBlackOnly", 7),
          ("eCalibrateColor", 3),
          ("eCalibrateColorPlaneRegistration", 5),
          ("eCalibrateDrumPhaseAdjustment", 6),
          ("eNotCalibrating", 1))
    )


_Marker_density_calibration_Type.__name__ = "Integer32"
_Marker_density_calibration_Object = MibScalar
marker_density_calibration = _Marker_density_calibration_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 5, 1, 11),
    _Marker_density_calibration_Type()
)
marker_density_calibration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    marker_density_calibration.setStatus("optional")
_Imaging_ObjectIdentity = ObjectIdentity
imaging = _Imaging_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 6)
)


class _Default_ret_Type(Integer32):
    """Custom type default_ret based on Integer32"""
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
        *(("eDark", 4),
          ("eLight", 2),
          ("eMedium", 3),
          ("eNotSet", 5),
          ("eOff", 1))
    )


_Default_ret_Type.__name__ = "Integer32"
_Default_ret_Object = MibScalar
default_ret = _Default_ret_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 6, 5),
    _Default_ret_Type()
)
default_ret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    default_ret.setStatus("optional")


class _Default_mfp_color_space_Type(Integer32):
    """Custom type default_mfp_color_space based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eBiLevel", 1),
          ("eGray", 2))
    )


_Default_mfp_color_space_Type.__name__ = "Integer32"
_Default_mfp_color_space_Object = MibScalar
default_mfp_color_space = _Default_mfp_color_space_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 6, 10),
    _Default_mfp_color_space_Type()
)
default_mfp_color_space.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    default_mfp_color_space.setStatus("optional")
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
media1_name.setMaxAccess("read-write")
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
media1_short_name.setMaxAccess("read-write")
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
_Media1_engine_media_mode_Type = Integer32
_Media1_engine_media_mode_Object = MibScalar
media1_engine_media_mode = _Media1_engine_media_mode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 1, 4),
    _Media1_engine_media_mode_Type()
)
media1_engine_media_mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    media1_engine_media_mode.setStatus("optional")
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
media2_name.setMaxAccess("read-write")
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
media2_short_name.setMaxAccess("read-write")
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
_Media2_engine_media_mode_Type = Integer32
_Media2_engine_media_mode_Object = MibScalar
media2_engine_media_mode = _Media2_engine_media_mode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 2, 4),
    _Media2_engine_media_mode_Type()
)
media2_engine_media_mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    media2_engine_media_mode.setStatus("optional")
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
media3_name.setMaxAccess("read-write")
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
media3_short_name.setMaxAccess("read-write")
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
_Media3_engine_media_mode_Type = Integer32
_Media3_engine_media_mode_Object = MibScalar
media3_engine_media_mode = _Media3_engine_media_mode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 3, 4),
    _Media3_engine_media_mode_Type()
)
media3_engine_media_mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    media3_engine_media_mode.setStatus("optional")
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
media4_name.setMaxAccess("read-write")
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
media4_short_name.setMaxAccess("read-write")
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
_Media4_engine_media_mode_Type = Integer32
_Media4_engine_media_mode_Object = MibScalar
media4_engine_media_mode = _Media4_engine_media_mode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 4, 4),
    _Media4_engine_media_mode_Type()
)
media4_engine_media_mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    media4_engine_media_mode.setStatus("optional")
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
media5_name.setMaxAccess("read-write")
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
media5_short_name.setMaxAccess("read-write")
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
_Media5_engine_media_mode_Type = Integer32
_Media5_engine_media_mode_Object = MibScalar
media5_engine_media_mode = _Media5_engine_media_mode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 5, 4),
    _Media5_engine_media_mode_Type()
)
media5_engine_media_mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    media5_engine_media_mode.setStatus("optional")
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
media6_name.setMaxAccess("read-write")
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
media6_short_name.setMaxAccess("read-write")
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
_Media6_engine_media_mode_Type = Integer32
_Media6_engine_media_mode_Object = MibScalar
media6_engine_media_mode = _Media6_engine_media_mode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 6, 4),
    _Media6_engine_media_mode_Type()
)
media6_engine_media_mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    media6_engine_media_mode.setStatus("optional")
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
media7_name.setMaxAccess("read-write")
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
media7_short_name.setMaxAccess("read-write")
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
_Media7_engine_media_mode_Type = Integer32
_Media7_engine_media_mode_Object = MibScalar
media7_engine_media_mode = _Media7_engine_media_mode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 7, 4),
    _Media7_engine_media_mode_Type()
)
media7_engine_media_mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    media7_engine_media_mode.setStatus("optional")
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
media8_name.setMaxAccess("read-write")
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
media8_short_name.setMaxAccess("read-write")
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
_Media8_engine_media_mode_Type = Integer32
_Media8_engine_media_mode_Object = MibScalar
media8_engine_media_mode = _Media8_engine_media_mode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 8, 4),
    _Media8_engine_media_mode_Type()
)
media8_engine_media_mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    media8_engine_media_mode.setStatus("optional")
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
media9_name.setMaxAccess("read-write")
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
media9_short_name.setMaxAccess("read-write")
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
_Media9_engine_media_mode_Type = Integer32
_Media9_engine_media_mode_Object = MibScalar
media9_engine_media_mode = _Media9_engine_media_mode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 9, 4),
    _Media9_engine_media_mode_Type()
)
media9_engine_media_mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    media9_engine_media_mode.setStatus("optional")
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
media10_name.setMaxAccess("read-write")
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
media10_short_name.setMaxAccess("read-write")
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
_Media10_engine_media_mode_Type = Integer32
_Media10_engine_media_mode_Object = MibScalar
media10_engine_media_mode = _Media10_engine_media_mode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 10, 4),
    _Media10_engine_media_mode_Type()
)
media10_engine_media_mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    media10_engine_media_mode.setStatus("optional")
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
media11_name.setMaxAccess("read-write")
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
media11_short_name.setMaxAccess("read-write")
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
_Media11_engine_media_mode_Type = Integer32
_Media11_engine_media_mode_Object = MibScalar
media11_engine_media_mode = _Media11_engine_media_mode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 11, 4),
    _Media11_engine_media_mode_Type()
)
media11_engine_media_mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    media11_engine_media_mode.setStatus("optional")
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
media12_name.setMaxAccess("read-write")
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
media12_short_name.setMaxAccess("read-write")
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
_Media12_engine_media_mode_Type = Integer32
_Media12_engine_media_mode_Object = MibScalar
media12_engine_media_mode = _Media12_engine_media_mode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 12, 4),
    _Media12_engine_media_mode_Type()
)
media12_engine_media_mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    media12_engine_media_mode.setStatus("optional")
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
media13_name.setMaxAccess("read-write")
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
media13_short_name.setMaxAccess("read-write")
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
_Media13_engine_media_mode_Type = Integer32
_Media13_engine_media_mode_Object = MibScalar
media13_engine_media_mode = _Media13_engine_media_mode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 13, 4),
    _Media13_engine_media_mode_Type()
)
media13_engine_media_mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    media13_engine_media_mode.setStatus("optional")
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
media14_name.setMaxAccess("read-write")
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
media14_short_name.setMaxAccess("read-write")
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
_Media14_engine_media_mode_Type = Integer32
_Media14_engine_media_mode_Object = MibScalar
media14_engine_media_mode = _Media14_engine_media_mode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 14, 4),
    _Media14_engine_media_mode_Type()
)
media14_engine_media_mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    media14_engine_media_mode.setStatus("optional")
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
media15_name.setMaxAccess("read-write")
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
media15_short_name.setMaxAccess("read-write")
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
_Media15_engine_media_mode_Type = Integer32
_Media15_engine_media_mode_Object = MibScalar
media15_engine_media_mode = _Media15_engine_media_mode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 15, 4),
    _Media15_engine_media_mode_Type()
)
media15_engine_media_mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    media15_engine_media_mode.setStatus("optional")
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
media16_name.setMaxAccess("read-write")
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
media16_short_name.setMaxAccess("read-write")
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
_Media16_engine_media_mode_Type = Integer32
_Media16_engine_media_mode_Object = MibScalar
media16_engine_media_mode = _Media16_engine_media_mode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 16, 4),
    _Media16_engine_media_mode_Type()
)
media16_engine_media_mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    media16_engine_media_mode.setStatus("optional")
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
media17_name.setMaxAccess("read-write")
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
media17_short_name.setMaxAccess("read-write")
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
_Media17_engine_media_mode_Type = Integer32
_Media17_engine_media_mode_Object = MibScalar
media17_engine_media_mode = _Media17_engine_media_mode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 17, 4),
    _Media17_engine_media_mode_Type()
)
media17_engine_media_mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    media17_engine_media_mode.setStatus("optional")
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
media18_name.setMaxAccess("read-write")
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
media18_short_name.setMaxAccess("read-write")
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
_Media18_engine_media_mode_Type = Integer32
_Media18_engine_media_mode_Object = MibScalar
media18_engine_media_mode = _Media18_engine_media_mode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 18, 4),
    _Media18_engine_media_mode_Type()
)
media18_engine_media_mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    media18_engine_media_mode.setStatus("optional")
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
media19_name.setMaxAccess("read-write")
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
media19_short_name.setMaxAccess("read-write")
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
_Media19_engine_media_mode_Type = Integer32
_Media19_engine_media_mode_Object = MibScalar
media19_engine_media_mode = _Media19_engine_media_mode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 19, 4),
    _Media19_engine_media_mode_Type()
)
media19_engine_media_mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    media19_engine_media_mode.setStatus("optional")
_Media20_ObjectIdentity = ObjectIdentity
media20 = _Media20_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 20)
)


class _Media20_name_Type(OctetString):
    """Custom type media20_name based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 24),
    )


_Media20_name_Type.__name__ = "OctetString"
_Media20_name_Object = MibScalar
media20_name = _Media20_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 20, 1),
    _Media20_name_Type()
)
media20_name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    media20_name.setStatus("optional")


class _Media20_short_name_Type(OctetString):
    """Custom type media20_short_name based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 9),
    )


_Media20_short_name_Type.__name__ = "OctetString"
_Media20_short_name_Object = MibScalar
media20_short_name = _Media20_short_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 20, 2),
    _Media20_short_name_Type()
)
media20_short_name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    media20_short_name.setStatus("optional")
_Media20_page_count_Type = Integer32
_Media20_page_count_Object = MibScalar
media20_page_count = _Media20_page_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 20, 3),
    _Media20_page_count_Type()
)
media20_page_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    media20_page_count.setStatus("optional")
_Media20_engine_media_mode_Type = Integer32
_Media20_engine_media_mode_Object = MibScalar
media20_engine_media_mode = _Media20_engine_media_mode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 20, 4),
    _Media20_engine_media_mode_Type()
)
media20_engine_media_mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    media20_engine_media_mode.setStatus("optional")
_Media21_ObjectIdentity = ObjectIdentity
media21 = _Media21_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 21)
)


class _Media21_name_Type(OctetString):
    """Custom type media21_name based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 24),
    )


_Media21_name_Type.__name__ = "OctetString"
_Media21_name_Object = MibScalar
media21_name = _Media21_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 21, 1),
    _Media21_name_Type()
)
media21_name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    media21_name.setStatus("optional")


class _Media21_short_name_Type(OctetString):
    """Custom type media21_short_name based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 9),
    )


_Media21_short_name_Type.__name__ = "OctetString"
_Media21_short_name_Object = MibScalar
media21_short_name = _Media21_short_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 21, 2),
    _Media21_short_name_Type()
)
media21_short_name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    media21_short_name.setStatus("optional")
_Media21_page_count_Type = Integer32
_Media21_page_count_Object = MibScalar
media21_page_count = _Media21_page_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 21, 3),
    _Media21_page_count_Type()
)
media21_page_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    media21_page_count.setStatus("optional")
_Media21_engine_media_mode_Type = Integer32
_Media21_engine_media_mode_Object = MibScalar
media21_engine_media_mode = _Media21_engine_media_mode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 21, 4),
    _Media21_engine_media_mode_Type()
)
media21_engine_media_mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    media21_engine_media_mode.setStatus("optional")
_Media22_ObjectIdentity = ObjectIdentity
media22 = _Media22_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 22)
)


class _Media22_name_Type(OctetString):
    """Custom type media22_name based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 24),
    )


_Media22_name_Type.__name__ = "OctetString"
_Media22_name_Object = MibScalar
media22_name = _Media22_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 22, 1),
    _Media22_name_Type()
)
media22_name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    media22_name.setStatus("optional")


class _Media22_short_name_Type(OctetString):
    """Custom type media22_short_name based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 9),
    )


_Media22_short_name_Type.__name__ = "OctetString"
_Media22_short_name_Object = MibScalar
media22_short_name = _Media22_short_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 22, 2),
    _Media22_short_name_Type()
)
media22_short_name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    media22_short_name.setStatus("optional")
_Media22_page_count_Type = Integer32
_Media22_page_count_Object = MibScalar
media22_page_count = _Media22_page_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 22, 3),
    _Media22_page_count_Type()
)
media22_page_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    media22_page_count.setStatus("optional")
_Media22_engine_media_mode_Type = Integer32
_Media22_engine_media_mode_Object = MibScalar
media22_engine_media_mode = _Media22_engine_media_mode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 22, 4),
    _Media22_engine_media_mode_Type()
)
media22_engine_media_mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    media22_engine_media_mode.setStatus("optional")
_Media23_ObjectIdentity = ObjectIdentity
media23 = _Media23_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 23)
)


class _Media23_name_Type(OctetString):
    """Custom type media23_name based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 24),
    )


_Media23_name_Type.__name__ = "OctetString"
_Media23_name_Object = MibScalar
media23_name = _Media23_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 23, 1),
    _Media23_name_Type()
)
media23_name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    media23_name.setStatus("optional")


class _Media23_short_name_Type(OctetString):
    """Custom type media23_short_name based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 9),
    )


_Media23_short_name_Type.__name__ = "OctetString"
_Media23_short_name_Object = MibScalar
media23_short_name = _Media23_short_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 23, 2),
    _Media23_short_name_Type()
)
media23_short_name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    media23_short_name.setStatus("optional")
_Media23_page_count_Type = Integer32
_Media23_page_count_Object = MibScalar
media23_page_count = _Media23_page_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 23, 3),
    _Media23_page_count_Type()
)
media23_page_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    media23_page_count.setStatus("optional")
_Media23_engine_media_mode_Type = Integer32
_Media23_engine_media_mode_Object = MibScalar
media23_engine_media_mode = _Media23_engine_media_mode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 23, 4),
    _Media23_engine_media_mode_Type()
)
media23_engine_media_mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    media23_engine_media_mode.setStatus("optional")
_Media24_ObjectIdentity = ObjectIdentity
media24 = _Media24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 24)
)


class _Media24_name_Type(OctetString):
    """Custom type media24_name based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 24),
    )


_Media24_name_Type.__name__ = "OctetString"
_Media24_name_Object = MibScalar
media24_name = _Media24_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 24, 1),
    _Media24_name_Type()
)
media24_name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    media24_name.setStatus("optional")


class _Media24_short_name_Type(OctetString):
    """Custom type media24_short_name based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 9),
    )


_Media24_short_name_Type.__name__ = "OctetString"
_Media24_short_name_Object = MibScalar
media24_short_name = _Media24_short_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 24, 2),
    _Media24_short_name_Type()
)
media24_short_name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    media24_short_name.setStatus("optional")
_Media24_page_count_Type = Integer32
_Media24_page_count_Object = MibScalar
media24_page_count = _Media24_page_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 24, 3),
    _Media24_page_count_Type()
)
media24_page_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    media24_page_count.setStatus("optional")
_Media24_engine_media_mode_Type = Integer32
_Media24_engine_media_mode_Object = MibScalar
media24_engine_media_mode = _Media24_engine_media_mode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 24, 4),
    _Media24_engine_media_mode_Type()
)
media24_engine_media_mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    media24_engine_media_mode.setStatus("optional")
_Media25_ObjectIdentity = ObjectIdentity
media25 = _Media25_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 25)
)


class _Media25_name_Type(OctetString):
    """Custom type media25_name based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 24),
    )


_Media25_name_Type.__name__ = "OctetString"
_Media25_name_Object = MibScalar
media25_name = _Media25_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 25, 1),
    _Media25_name_Type()
)
media25_name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    media25_name.setStatus("optional")


class _Media25_short_name_Type(OctetString):
    """Custom type media25_short_name based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 9),
    )


_Media25_short_name_Type.__name__ = "OctetString"
_Media25_short_name_Object = MibScalar
media25_short_name = _Media25_short_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 25, 2),
    _Media25_short_name_Type()
)
media25_short_name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    media25_short_name.setStatus("optional")
_Media25_page_count_Type = Integer32
_Media25_page_count_Object = MibScalar
media25_page_count = _Media25_page_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 25, 3),
    _Media25_page_count_Type()
)
media25_page_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    media25_page_count.setStatus("optional")
_Media25_engine_media_mode_Type = Integer32
_Media25_engine_media_mode_Object = MibScalar
media25_engine_media_mode = _Media25_engine_media_mode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 25, 4),
    _Media25_engine_media_mode_Type()
)
media25_engine_media_mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    media25_engine_media_mode.setStatus("optional")
_Media26_ObjectIdentity = ObjectIdentity
media26 = _Media26_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 26)
)


class _Media26_name_Type(OctetString):
    """Custom type media26_name based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 24),
    )


_Media26_name_Type.__name__ = "OctetString"
_Media26_name_Object = MibScalar
media26_name = _Media26_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 26, 1),
    _Media26_name_Type()
)
media26_name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    media26_name.setStatus("optional")


class _Media26_short_name_Type(OctetString):
    """Custom type media26_short_name based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 9),
    )


_Media26_short_name_Type.__name__ = "OctetString"
_Media26_short_name_Object = MibScalar
media26_short_name = _Media26_short_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 26, 2),
    _Media26_short_name_Type()
)
media26_short_name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    media26_short_name.setStatus("optional")
_Media26_page_count_Type = Integer32
_Media26_page_count_Object = MibScalar
media26_page_count = _Media26_page_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 26, 3),
    _Media26_page_count_Type()
)
media26_page_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    media26_page_count.setStatus("optional")
_Media26_engine_media_mode_Type = Integer32
_Media26_engine_media_mode_Object = MibScalar
media26_engine_media_mode = _Media26_engine_media_mode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 26, 4),
    _Media26_engine_media_mode_Type()
)
media26_engine_media_mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    media26_engine_media_mode.setStatus("optional")
_Media_modes_ObjectIdentity = ObjectIdentity
media_modes = _Media_modes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 4)
)
_Engine_media_modes_supported1_Type = OctetString
_Engine_media_modes_supported1_Object = MibScalar
engine_media_modes_supported1 = _Engine_media_modes_supported1_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 4, 1),
    _Engine_media_modes_supported1_Type()
)
engine_media_modes_supported1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engine_media_modes_supported1.setStatus("optional")
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


class _Consumable_status_formatter_color_page_count_Type(Integer32):
    """Custom type consumable_status_formatter_color_page_count based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32768),
    )


_Consumable_status_formatter_color_page_count_Type.__name__ = "Integer32"
_Consumable_status_formatter_color_page_count_Object = MibScalar
consumable_status_formatter_color_page_count = _Consumable_status_formatter_color_page_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 10, 1, 1, 46),
    _Consumable_status_formatter_color_page_count_Type()
)
consumable_status_formatter_color_page_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    consumable_status_formatter_color_page_count.setStatus("optional")


class _Consumable_status_page_count_out_while_cartridge_out_override_active_Type(Integer32):
    """Custom type consumable_status_page_count_out_while_cartridge_out_override_active based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Consumable_status_page_count_out_while_cartridge_out_override_active_Type.__name__ = "Integer32"
_Consumable_status_page_count_out_while_cartridge_out_override_active_Object = MibScalar
consumable_status_page_count_out_while_cartridge_out_override_active = _Consumable_status_page_count_out_while_cartridge_out_override_active_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 10, 1, 1, 60),
    _Consumable_status_page_count_out_while_cartridge_out_override_active_Type()
)
consumable_status_page_count_out_while_cartridge_out_override_active.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    consumable_status_page_count_out_while_cartridge_out_override_active.setStatus("optional")


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
            1
        )
    )
    namedValues = NamedValues(
        ("ePresetToNVRAM", 1)
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


class _Device_used_while_cartridge_out_override_active_Type(Integer32):
    """Custom type device_used_while_cartridge_out_override_active based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eNotUsed", 1),
          ("eUsed", 2))
    )


_Device_used_while_cartridge_out_override_active_Type.__name__ = "Integer32"
_Device_used_while_cartridge_out_override_active_Object = MibScalar
device_used_while_cartridge_out_override_active = _Device_used_while_cartridge_out_override_active_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 10, 9),
    _Device_used_while_cartridge_out_override_active_Type()
)
device_used_while_cartridge_out_override_active.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    device_used_while_cartridge_out_override_active.setStatus("optional")
_Consumable_notification_status_Type = OctetString
_Consumable_notification_status_Object = MibScalar
consumable_notification_status = _Consumable_notification_status_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 10, 10),
    _Consumable_notification_status_Type()
)
consumable_notification_status.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    consumable_notification_status.setStatus("optional")
_Print_meter_ObjectIdentity = ObjectIdentity
print_meter = _Print_meter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 11)
)
_Printer_average_ObjectIdentity = ObjectIdentity
printer_average = _Printer_average_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 11, 1)
)
_Printer_average_marking_agent_coverage_Type = OctetString
_Printer_average_marking_agent_coverage_Object = MibScalar
printer_average_marking_agent_coverage = _Printer_average_marking_agent_coverage_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 11, 1, 1),
    _Printer_average_marking_agent_coverage_Type()
)
printer_average_marking_agent_coverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    printer_average_marking_agent_coverage.setStatus("optional")
_Printer_average_marking_agent_coverage_sum_Type = OctetString
_Printer_average_marking_agent_coverage_sum_Object = MibScalar
printer_average_marking_agent_coverage_sum = _Printer_average_marking_agent_coverage_sum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 11, 1, 2),
    _Printer_average_marking_agent_coverage_sum_Type()
)
printer_average_marking_agent_coverage_sum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    printer_average_marking_agent_coverage_sum.setStatus("optional")
_Printer_average_marking_agent_coverage_sum_squared_Type = OctetString
_Printer_average_marking_agent_coverage_sum_squared_Object = MibScalar
printer_average_marking_agent_coverage_sum_squared = _Printer_average_marking_agent_coverage_sum_squared_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 11, 1, 3),
    _Printer_average_marking_agent_coverage_sum_squared_Type()
)
printer_average_marking_agent_coverage_sum_squared.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    printer_average_marking_agent_coverage_sum_squared.setStatus("optional")
_Printer_average_marking_agent_units_per_gram_Type = OctetString
_Printer_average_marking_agent_units_per_gram_Object = MibScalar
printer_average_marking_agent_units_per_gram = _Printer_average_marking_agent_units_per_gram_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 11, 1, 4),
    _Printer_average_marking_agent_units_per_gram_Type()
)
printer_average_marking_agent_units_per_gram.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    printer_average_marking_agent_units_per_gram.setStatus("optional")
_Printer_average_marking_agent_coverage_actual_Type = OctetString
_Printer_average_marking_agent_coverage_actual_Object = MibScalar
printer_average_marking_agent_coverage_actual = _Printer_average_marking_agent_coverage_actual_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 11, 1, 5),
    _Printer_average_marking_agent_coverage_actual_Type()
)
printer_average_marking_agent_coverage_actual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    printer_average_marking_agent_coverage_actual.setStatus("optional")
_Menus_ObjectIdentity = ObjectIdentity
menus = _Menus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 13)
)
_Copier_ObjectIdentity = ObjectIdentity
copier = _Copier_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 5)
)
_Settings_copier_ObjectIdentity = ObjectIdentity
settings_copier = _Settings_copier_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 5, 1)
)


class _Default_copier_media_size_Type(Integer32):
    """Custom type default_copier_media_size based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              10,
              15,
              17,
              18,
              25,
              26,
              45,
              72,
              80,
              81,
              90,
              91,
              100,
              32767)
        )
    )
    namedValues = NamedValues(
        *(("eCommercial10", 81),
          ("eFoolscap", 10),
          ("eISOandJISA4", 26),
          ("eISOandJISA5", 25),
          ("eInternationalB5", 100),
          ("eInternationalC5", 91),
          ("eInternationalDL", 90),
          ("eJISB5", 45),
          ("eJISExecutive", 18),
          ("eJapansePostcardDouble", 72),
          ("eMonarch", 80),
          ("eROC16K", 17),
          ("eStatement", 15),
          ("eUSExecutive", 1),
          ("eUSLegal", 3),
          ("eUSLetter", 2),
          ("eUnknownMediaSize", 32767))
    )


_Default_copier_media_size_Type.__name__ = "Integer32"
_Default_copier_media_size_Object = MibScalar
default_copier_media_size = _Default_copier_media_size_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 5, 1, 9),
    _Default_copier_media_size_Type()
)
default_copier_media_size.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    default_copier_media_size.setStatus("optional")


class _Default_copier_image_type_Type(Integer32):
    """Custom type default_copier_image_type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("eGraphic", 2),
          ("eMixed", 3),
          ("eText", 1))
    )


_Default_copier_image_type_Type.__name__ = "Integer32"
_Default_copier_image_type_Object = MibScalar
default_copier_image_type = _Default_copier_image_type_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 5, 1, 10),
    _Default_copier_image_type_Type()
)
default_copier_image_type.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    default_copier_image_type.setStatus("optional")


class _Copier_media_type_Type(Integer32):
    """Custom type copier_media_type based on Integer32"""
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
              21,
              22,
              23,
              24,
              25)
        )
    )
    namedValues = NamedValues(
        *(("eCopierMediaTypeAdvancedPhoto", 16),
          ("eCopierMediaTypeAutomatic", 15),
          ("eCopierMediaTypeBochureMatte", 8),
          ("eCopierMediaTypeBrightWhite", 2),
          ("eCopierMediaTypeBrochureGlossy", 9),
          ("eCopierMediaTypeEverydayPhoto", 12),
          ("eCopierMediaTypeFastTransparency", 7),
          ("eCopierMediaTypeIronOnMirrored", 17),
          ("eCopierMediaTypeIronon", 6),
          ("eCopierMediaTypeOtherPhoto", 14),
          ("eCopierMediaTypePhoto", 3),
          ("eCopierMediaTypePhotoGlossy", 10),
          ("eCopierMediaTypePhotoMatte", 11),
          ("eCopierMediaTypePhotoQualInkjet", 13),
          ("eCopierMediaTypePlain", 1),
          ("eCopierMediaTypeSpecial", 4),
          ("eCopierMediaTypeTransparency", 5),
          ("eGlossFilm", 24),
          ("eHeavyGloss", 23),
          ("eMediaTypeEnvelope", 22),
          ("eMediaTypeLight", 21),
          ("eNonHPHeavyGloss", 25))
    )


_Copier_media_type_Type.__name__ = "Integer32"
_Copier_media_type_Object = MibScalar
copier_media_type = _Copier_media_type_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 5, 1, 14),
    _Copier_media_type_Type()
)
copier_media_type.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    copier_media_type.setStatus("optional")


class _Default_copy_duplex_mode_Type(Integer32):
    """Custom type default_copy_duplex_mode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("eDuplexToDuplex", 5),
          ("eDuplexToSimplex", 4),
          ("eSimplexToDuplex", 2),
          ("eSimplexToSimplex", 1))
    )


_Default_copy_duplex_mode_Type.__name__ = "Integer32"
_Default_copy_duplex_mode_Object = MibScalar
default_copy_duplex_mode = _Default_copy_duplex_mode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 5, 1, 28),
    _Default_copy_duplex_mode_Type()
)
default_copy_duplex_mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    default_copy_duplex_mode.setStatus("optional")


class _Default_copy_input_tray_Type(Integer32):
    """Custom type default_copy_input_tray based on Integer32"""
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
        *(("eInTray1", 1),
          ("eInTray2", 2),
          ("eInTray3", 3),
          ("eInTray4", 4))
    )


_Default_copy_input_tray_Type.__name__ = "Integer32"
_Default_copy_input_tray_Object = MibScalar
default_copy_input_tray = _Default_copy_input_tray_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 5, 1, 29),
    _Default_copy_input_tray_Type()
)
default_copy_input_tray.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    default_copy_input_tray.setStatus("optional")


class _Default_copy_output_bin_Type(Integer32):
    """Custom type default_copy_output_bin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("eOutBin1", 1),
          ("eOutBin2", 2),
          ("eOutBin3", 3))
    )


_Default_copy_output_bin_Type.__name__ = "Integer32"
_Default_copy_output_bin_Object = MibScalar
default_copy_output_bin = _Default_copy_output_bin_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 5, 1, 30),
    _Default_copy_output_bin_Type()
)
default_copy_output_bin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    default_copy_output_bin.setStatus("optional")
_Default_copy_reset_timeout_Type = Integer32
_Default_copy_reset_timeout_Object = MibScalar
default_copy_reset_timeout = _Default_copy_reset_timeout_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 5, 1, 31),
    _Default_copy_reset_timeout_Type()
)
default_copy_reset_timeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    default_copy_reset_timeout.setStatus("optional")


class _Default_copier_quantity_Type(Integer32):
    """Custom type default_copier_quantity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 999),
    )


_Default_copier_quantity_Type.__name__ = "Integer32"
_Default_copier_quantity_Object = MibScalar
default_copier_quantity = _Default_copier_quantity_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 5, 1, 32),
    _Default_copier_quantity_Type()
)
default_copier_quantity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    default_copier_quantity.setStatus("optional")


class _Default_copier_flip_pages_up_Type(Integer32):
    """Custom type default_copier_flip_pages_up based on Integer32"""
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


_Default_copier_flip_pages_up_Type.__name__ = "Integer32"
_Default_copier_flip_pages_up_Object = MibScalar
default_copier_flip_pages_up = _Default_copier_flip_pages_up_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 5, 1, 33),
    _Default_copier_flip_pages_up_Type()
)
default_copier_flip_pages_up.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    default_copier_flip_pages_up.setStatus("optional")


class _Default_copier_pages_per_sheet_Type(Integer32):
    """Custom type default_copier_pages_per_sheet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("eFourUpNOrder", 7),
          ("eFourUpZOrder", 8),
          ("eNone", 1),
          ("eTwoUp", 6))
    )


_Default_copier_pages_per_sheet_Type.__name__ = "Integer32"
_Default_copier_pages_per_sheet_Object = MibScalar
default_copier_pages_per_sheet = _Default_copier_pages_per_sheet_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 5, 1, 34),
    _Default_copier_pages_per_sheet_Type()
)
default_copier_pages_per_sheet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    default_copier_pages_per_sheet.setStatus("optional")


class _Default_copier_page_borders_Type(Integer32):
    """Custom type default_copier_page_borders based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eLine", 2),
          ("eNone", 1))
    )


_Default_copier_page_borders_Type.__name__ = "Integer32"
_Default_copier_page_borders_Object = MibScalar
default_copier_page_borders = _Default_copier_page_borders_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 5, 1, 35),
    _Default_copier_page_borders_Type()
)
default_copier_page_borders.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    default_copier_page_borders.setStatus("optional")


class _Default_copier_collate_Type(Integer32):
    """Custom type default_copier_collate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eCollate", 1),
          ("eUncollate", 2))
    )


_Default_copier_collate_Type.__name__ = "Integer32"
_Default_copier_collate_Object = MibScalar
default_copier_collate = _Default_copier_collate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 5, 1, 36),
    _Default_copier_collate_Type()
)
default_copier_collate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    default_copier_collate.setStatus("optional")
_Default_copier_contrast_Type = Integer32
_Default_copier_contrast_Object = MibScalar
default_copier_contrast = _Default_copier_contrast_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 5, 1, 37),
    _Default_copier_contrast_Type()
)
default_copier_contrast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    default_copier_contrast.setStatus("optional")


class _Default_copier_edge_to_edge_Type(Integer32):
    """Custom type default_copier_edge_to_edge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("eClip", 3),
          ("eNone", 1),
          ("eScale", 2))
    )


_Default_copier_edge_to_edge_Type.__name__ = "Integer32"
_Default_copier_edge_to_edge_Object = MibScalar
default_copier_edge_to_edge = _Default_copier_edge_to_edge_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 5, 1, 38),
    _Default_copier_edge_to_edge_Type()
)
default_copier_edge_to_edge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    default_copier_edge_to_edge.setStatus("optional")


class _Copy_job_scan_ahead_Type(Integer32):
    """Custom type copy_job_scan_ahead based on Integer32"""
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


_Copy_job_scan_ahead_Type.__name__ = "Integer32"
_Copy_job_scan_ahead_Object = MibScalar
copy_job_scan_ahead = _Copy_job_scan_ahead_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 5, 1, 39),
    _Copy_job_scan_ahead_Type()
)
copy_job_scan_ahead.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    copy_job_scan_ahead.setStatus("optional")


class _Copy_job_auto_interrupt_Type(Integer32):
    """Custom type copy_job_auto_interrupt based on Integer32"""
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


_Copy_job_auto_interrupt_Type.__name__ = "Integer32"
_Copy_job_auto_interrupt_Object = MibScalar
copy_job_auto_interrupt = _Copy_job_auto_interrupt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 5, 1, 40),
    _Copy_job_auto_interrupt_Type()
)
copy_job_auto_interrupt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    copy_job_auto_interrupt.setStatus("optional")


class _Copy_job_interrupt_copy_jobs_Type(Integer32):
    """Custom type copy_job_interrupt_copy_jobs based on Integer32"""
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


_Copy_job_interrupt_copy_jobs_Type.__name__ = "Integer32"
_Copy_job_interrupt_copy_jobs_Object = MibScalar
copy_job_interrupt_copy_jobs = _Copy_job_interrupt_copy_jobs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 5, 1, 41),
    _Copy_job_interrupt_copy_jobs_Type()
)
copy_job_interrupt_copy_jobs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    copy_job_interrupt_copy_jobs.setStatus("optional")


class _Copy_job_hold_off_print_jobs_Type(Integer32):
    """Custom type copy_job_hold_off_print_jobs based on Integer32"""
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


_Copy_job_hold_off_print_jobs_Type.__name__ = "Integer32"
_Copy_job_hold_off_print_jobs_Object = MibScalar
copy_job_hold_off_print_jobs = _Copy_job_hold_off_print_jobs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 5, 1, 42),
    _Copy_job_hold_off_print_jobs_Type()
)
copy_job_hold_off_print_jobs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    copy_job_hold_off_print_jobs.setStatus("optional")
_Copy_job_hold_time_Type = Integer32
_Copy_job_hold_time_Object = MibScalar
copy_job_hold_time = _Copy_job_hold_time_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 5, 1, 43),
    _Copy_job_hold_time_Type()
)
copy_job_hold_time.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    copy_job_hold_time.setStatus("optional")


class _Default_copy_job_chromaticity_Type(Integer32):
    """Custom type default_copy_job_chromaticity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eColor", 2),
          ("eMono", 1))
    )


_Default_copy_job_chromaticity_Type.__name__ = "Integer32"
_Default_copy_job_chromaticity_Object = MibScalar
default_copy_job_chromaticity = _Default_copy_job_chromaticity_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 5, 1, 58),
    _Default_copy_job_chromaticity_Type()
)
default_copy_job_chromaticity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    default_copy_job_chromaticity.setStatus("optional")


class _First_copy_speed_Type(Integer32):
    """Custom type first_copy_speed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eEarlyWarmup", 2),
          ("eNoEarlyWarmup", 1))
    )


_First_copy_speed_Type.__name__ = "Integer32"
_First_copy_speed_Object = MibScalar
first_copy_speed = _First_copy_speed_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 5, 1, 59),
    _First_copy_speed_Type()
)
first_copy_speed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    first_copy_speed.setStatus("optional")


class _Copier_job_border_setting_Type(Integer32):
    """Custom type copier_job_border_setting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eWithBorders", 1),
          ("eWithoutBorders", 2))
    )


_Copier_job_border_setting_Type.__name__ = "Integer32"
_Copier_job_border_setting_Object = MibScalar
copier_job_border_setting = _Copier_job_border_setting_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 5, 1, 60),
    _Copier_job_border_setting_Type()
)
copier_job_border_setting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    copier_job_border_setting.setStatus("optional")


class _Color_copy_enabled_Type(Integer32):
    """Custom type color_copy_enabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eDisable", 2),
          ("eEnable", 1))
    )


_Color_copy_enabled_Type.__name__ = "Integer32"
_Color_copy_enabled_Object = MibScalar
color_copy_enabled = _Color_copy_enabled_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 5, 1, 67),
    _Color_copy_enabled_Type()
)
color_copy_enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    color_copy_enabled.setStatus("optional")
_Channel_ObjectIdentity = ObjectIdentity
channel = _Channel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 6)
)
_Channelprinteralert_Type = OctetString
_Channelprinteralert_Object = MibScalar
channelprinteralert = _Channelprinteralert_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 6, 2),
    _Channelprinteralert_Type()
)
channelprinteralert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelprinteralert.setStatus("optional")
_Tables_ObjectIdentity = ObjectIdentity
tables = _Tables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 7)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LJ4730-MIB",
    **{"DisplayString": DisplayString,
       "hp": hp,
       "netPMLmgmt": netPMLmgmt,
       "device": device,
       "device-system": device_system,
       "settings-system": settings_system,
       "energy-star": energy_star,
       "sleep-mode": sleep_mode,
       "date-display": date_display,
       "mono-color-switching-mode": mono_color_switching_mode,
       "device-configure": device_configure,
       "device-configure-printer-parameters": device_configure_printer_parameters,
       "color-supply-out-action": color_supply_out_action,
       "direct-connect-ports-enable": direct_connect_ports_enable,
       "control-panel-supplies-status-message": control_panel_supplies_status_message,
       "status-system": status_system,
       "on-off-line": on_off_line,
       "continue": _pysmi_continue,
       "auto-continue": auto_continue,
       "install-date": install_date,
       "perm-store-init-occurred": perm_store_init_occurred,
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
       "background-message3": background_message3,
       "background-status-msg-line3-part1": background_status_msg_line3_part1,
       "background-message4": background_message4,
       "background-status-msg-line4-part1": background_status_msg_line4_part1,
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
       "simm": simm,
       "simm1": simm1,
       "simm1-type": simm1_type,
       "simm1-capacity": simm1_capacity,
       "simm1-bank": simm1_bank,
       "simm1-bank1": simm1_bank1,
       "simm1-bank1-type": simm1_bank1_type,
       "simm1-bank1-capacity": simm1_bank1_capacity,
       "simm1-bank2": simm1_bank2,
       "simm1-bank2-type": simm1_bank2_type,
       "simm1-bank2-capacity": simm1_bank2_capacity,
       "simm2": simm2,
       "simm2-type": simm2_type,
       "simm2-capacity": simm2_capacity,
       "simm2-bank": simm2_bank,
       "simm2-bank1": simm2_bank1,
       "simm2-bank1-type": simm2_bank1_type,
       "simm2-bank1-capacity": simm2_bank1_capacity,
       "simm2-bank2": simm2_bank2,
       "simm2-bank2-type": simm2_bank2_type,
       "simm2-bank2-capacity": simm2_bank2_capacity,
       "mio": mio,
       "mio1": mio1,
       "mio1-model-name": mio1_model_name,
       "mio1-manufacturing-info": mio1_manufacturing_info,
       "mio1-type": mio1_type,
       "mio2": mio2,
       "mio2-model-name": mio2_model_name,
       "mio2-manufacturing-info": mio2_manufacturing_info,
       "mio2-type": mio2_type,
       "mio3": mio3,
       "mio3-model-name": mio3_model_name,
       "mio3-manufacturing-info": mio3_manufacturing_info,
       "mio3-type": mio3_type,
       "web-server": web_server,
       "settings-web-server": settings_web_server,
       "ews-request-control-panel-supplies-status": ews_request_control_panel_supplies_status,
       "socket-ping": socket_ping,
       "socket-ping-job-events-version": socket_ping_job_events_version,
       "test": test,
       "engine-self-diagnostic": engine_self_diagnostic,
       "engine-parameter": engine_parameter,
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
       "job-info-outbins-used": job_info_outbins_used,
       "job-info-physical-outbins-used": job_info_physical_outbins_used,
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
       "job-info-requested-originals": job_info_requested_originals,
       "job-info-page-count-current-original": job_info_page_count_current_original,
       "job-info-pages-in-original": job_info_pages_in_original,
       "job-info-printed-originals": job_info_printed_originals,
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
       "job-info-accounting-scanned-media-simplex-count": job_info_accounting_scanned_media_simplex_count,
       "job-info-accounting-scanned-media-duplex-count": job_info_accounting_scanned_media_duplex_count,
       "job-info-accounting-job-type": job_info_accounting_job_type,
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
       "usage-average-toner-coverage": usage_average_toner_coverage,
       "usage-staple-count": usage_staple_count,
       "usage-instructions-line1": usage_instructions_line1,
       "usage-instructions-line2": usage_instructions_line2,
       "usage-instructions-line3": usage_instructions_line3,
       "usage-instructions-line4": usage_instructions_line4,
       "printed-modes-usage-total": printed_modes_usage_total,
       "source-tray-usage-total": source_tray_usage_total,
       "destination-bin-usage-total": destination_bin_usage_total,
       "usage-printer-mono-total-charge": usage_printer_mono_total_charge,
       "usage-printer-color-total-charge": usage_printer_color_total_charge,
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
       "printed-modes-accounting": printed_modes_accounting,
       "printed-modes-usage": printed_modes_usage,
       "printed-modes-mono-count": printed_modes_mono_count,
       "printed-modes-color-count": printed_modes_color_count,
       "printed-modes-total-count": printed_modes_total_count,
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
       "scan-sharpening-coefficient": scan_sharpening_coefficient,
       "scanner-accessory-adf-sheet-count": scanner_accessory_adf_sheet_count,
       "scanner-accessory-flatbed-scan-count": scanner_accessory_flatbed_scan_count,
       "scanner-accessory-adf-one-sided-sheet-count": scanner_accessory_adf_one_sided_sheet_count,
       "scanner-accessory-adf-two-sided-sheet-count": scanner_accessory_adf_two_sided_sheet_count,
       "scanner-accessory-copy-job-scan-count": scanner_accessory_copy_job_scan_count,
       "scanner-accessory-send-job-scan-count": scanner_accessory_send_job_scan_count,
       "scanner-accessory-total-copy-pages-printed": scanner_accessory_total_copy_pages_printed,
       "scanner-accessory-digital-send-module-url": scanner_accessory_digital_send_module_url,
       "scanner-accessory-digital-send-status": scanner_accessory_digital_send_status,
       "default-scan-original-size": default_scan_original_size,
       "default-scan-text-graphics-mix": default_scan_text_graphics_mix,
       "default-scan-job-mode": default_scan_job_mode,
       "default-scan-background-removal": default_scan_background_removal,
       "default-scan-image-quality": default_scan_image_quality,
       "default-scan-content-orientation": default_scan_content_orientation,
       "auto-send-reset": auto_send_reset,
       "scanner-accessory-digital-send-log-event-counter": scanner_accessory_digital_send_log_event_counter,
       "scanner-accessory-digital-send-config-email-gateway": scanner_accessory_digital_send_config_email_gateway,
       "scanner-accessory-digital-send-config-ldap-gateway": scanner_accessory_digital_send_config_ldap_gateway,
       "scanner-accessory-digital-send-config-dsm-enabled-fax": scanner_accessory_digital_send_config_dsm_enabled_fax,
       "scanner-accessory-digital-send-config-fax-embedded": scanner_accessory_digital_send_config_fax_embedded,
       "default-scanner-speed": default_scanner_speed,
       "scan-to-folder-count": scan_to_folder_count,
       "fax-job-scan-count": fax_job_scan_count,
       "scanner-accessory-digital-send-home-screen-status": scanner_accessory_digital_send_home_screen_status,
       "status-scanner": status_scanner,
       "not-ready-source-scanner": not_ready_source_scanner,
       "scan-calibration-download": scan_calibration_download,
       "scan-calibration-error": scan_calibration_error,
       "spooler": spooler,
       "settings-spooler": settings_spooler,
       "mopy-mode": mopy_mode,
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
       "pcl-default-font-height": pcl_default_font_height,
       "pcl-default-font-source": pcl_default_font_source,
       "pcl-default-font-number": pcl_default_font_number,
       "pcl-default-font-width": pcl_default_font_width,
       "pdl-postscript": pdl_postscript,
       "postscript-total-page-count": postscript_total_page_count,
       "postscript-print-errors": postscript_print_errors,
       "postscript-defer-media": postscript_defer_media,
       "pml": pml,
       "pjl": pjl,
       "webserver-proc-sub": webserver_proc_sub,
       "settings-webserver": settings_webserver,
       "web-server-url": web_server_url,
       "web-server-security": web_server_security,
       "destination-subsystem": destination_subsystem,
       "print-engine": print_engine,
       "settings-prt-eng": settings_prt_eng,
       "override-media-name": override_media_name,
       "override-media-size": override_media_size,
       "marking-agent-density": marking_agent_density,
       "marking-agent-highlights-density-setting": marking_agent_highlights_density_setting,
       "marking-agent-midtones-density-setting": marking_agent_midtones_density_setting,
       "marking-agent-shadows-density-setting": marking_agent_shadows_density_setting,
       "autocleaning-page-frequency": autocleaning_page_frequency,
       "autocleaning-page-size": autocleaning_page_size,
       "default-audible-feedback": default_audible_feedback,
       "default-reset-send-timeout": default_reset_send_timeout,
       "default-authentication-timeout": default_authentication_timeout,
       "default-staple-mode": default_staple_mode,
       "configurable-low-threshold-setting": configurable_low_threshold_setting,
       "supplies-replace-action-at-setting": supplies_replace_action_at_setting,
       "supply-out-user-configured-override-limit": supply_out_user_configured_override_limit,
       "cartridge-out-override-control": cartridge_out_override_control,
       "duplex-blank-pages": duplex_blank_pages,
       "finisher-image-rotation": finisher_image_rotation,
       "status-prt-eng": status_prt_eng,
       "total-color-page-count": total_color_page_count,
       "duplex-page-count": duplex_page_count,
       "print-engine-revision": print_engine_revision,
       "printer-calibration-dhalf": printer_calibration_dhalf,
       "printer-cal-dhalf-page-count": printer_cal_dhalf_page_count,
       "printer-cal-dhalf-utc": printer_cal_dhalf_utc,
       "printer-cal-dhalf-data": printer_cal_dhalf_data,
       "printer-cal-dhalf-data1": printer_cal_dhalf_data1,
       "printer-cal-dhalf-data2": printer_cal_dhalf_data2,
       "printer-calibration-cpr": printer_calibration_cpr,
       "printer-cal-cpr-page-count": printer_cal_cpr_page_count,
       "printer-cal-cpr-utc": printer_cal_cpr_utc,
       "printer-cal-cpr-data": printer_cal_cpr_data,
       "supply-out-action-support": supply_out_action_support,
       "supply-out-device-state": supply_out_device_state,
       "supply-after-out-state": supply_after_out_state,
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
       "outbin": outbin,
       "settings-outbin": settings_outbin,
       "overflow-bin": overflow_bin,
       "outbins": outbins,
       "outbin1": outbin1,
       "outbin1-override-mode": outbin1_override_mode,
       "marking-agent": marking_agent,
       "settings-marking-agent": settings_marking_agent,
       "marker-density-calibration": marker_density_calibration,
       "imaging": imaging,
       "default-ret": default_ret,
       "default-mfp-color-space": default_mfp_color_space,
       "ph": ph,
       "settings-ph": settings_ph,
       "tray-disable-use-instead": tray_disable_use_instead,
       "print-media": print_media,
       "settings-print-media": settings_print_media,
       "media-names-available": media_names_available,
       "north-edge-offset": north_edge_offset,
       "media-info": media_info,
       "media1": media1,
       "media1-name": media1_name,
       "media1-short-name": media1_short_name,
       "media1-page-count": media1_page_count,
       "media1-engine-media-mode": media1_engine_media_mode,
       "media2": media2,
       "media2-name": media2_name,
       "media2-short-name": media2_short_name,
       "media2-page-count": media2_page_count,
       "media2-engine-media-mode": media2_engine_media_mode,
       "media3": media3,
       "media3-name": media3_name,
       "media3-short-name": media3_short_name,
       "media3-page-count": media3_page_count,
       "media3-engine-media-mode": media3_engine_media_mode,
       "media4": media4,
       "media4-name": media4_name,
       "media4-short-name": media4_short_name,
       "media4-page-count": media4_page_count,
       "media4-engine-media-mode": media4_engine_media_mode,
       "media5": media5,
       "media5-name": media5_name,
       "media5-short-name": media5_short_name,
       "media5-page-count": media5_page_count,
       "media5-engine-media-mode": media5_engine_media_mode,
       "media6": media6,
       "media6-name": media6_name,
       "media6-short-name": media6_short_name,
       "media6-page-count": media6_page_count,
       "media6-engine-media-mode": media6_engine_media_mode,
       "media7": media7,
       "media7-name": media7_name,
       "media7-short-name": media7_short_name,
       "media7-page-count": media7_page_count,
       "media7-engine-media-mode": media7_engine_media_mode,
       "media8": media8,
       "media8-name": media8_name,
       "media8-short-name": media8_short_name,
       "media8-page-count": media8_page_count,
       "media8-engine-media-mode": media8_engine_media_mode,
       "media9": media9,
       "media9-name": media9_name,
       "media9-short-name": media9_short_name,
       "media9-page-count": media9_page_count,
       "media9-engine-media-mode": media9_engine_media_mode,
       "media10": media10,
       "media10-name": media10_name,
       "media10-short-name": media10_short_name,
       "media10-page-count": media10_page_count,
       "media10-engine-media-mode": media10_engine_media_mode,
       "media11": media11,
       "media11-name": media11_name,
       "media11-short-name": media11_short_name,
       "media11-page-count": media11_page_count,
       "media11-engine-media-mode": media11_engine_media_mode,
       "media12": media12,
       "media12-name": media12_name,
       "media12-short-name": media12_short_name,
       "media12-page-count": media12_page_count,
       "media12-engine-media-mode": media12_engine_media_mode,
       "media13": media13,
       "media13-name": media13_name,
       "media13-short-name": media13_short_name,
       "media13-page-count": media13_page_count,
       "media13-engine-media-mode": media13_engine_media_mode,
       "media14": media14,
       "media14-name": media14_name,
       "media14-short-name": media14_short_name,
       "media14-page-count": media14_page_count,
       "media14-engine-media-mode": media14_engine_media_mode,
       "media15": media15,
       "media15-name": media15_name,
       "media15-short-name": media15_short_name,
       "media15-page-count": media15_page_count,
       "media15-engine-media-mode": media15_engine_media_mode,
       "media16": media16,
       "media16-name": media16_name,
       "media16-short-name": media16_short_name,
       "media16-page-count": media16_page_count,
       "media16-engine-media-mode": media16_engine_media_mode,
       "media17": media17,
       "media17-name": media17_name,
       "media17-short-name": media17_short_name,
       "media17-page-count": media17_page_count,
       "media17-engine-media-mode": media17_engine_media_mode,
       "media18": media18,
       "media18-name": media18_name,
       "media18-short-name": media18_short_name,
       "media18-page-count": media18_page_count,
       "media18-engine-media-mode": media18_engine_media_mode,
       "media19": media19,
       "media19-name": media19_name,
       "media19-short-name": media19_short_name,
       "media19-page-count": media19_page_count,
       "media19-engine-media-mode": media19_engine_media_mode,
       "media20": media20,
       "media20-name": media20_name,
       "media20-short-name": media20_short_name,
       "media20-page-count": media20_page_count,
       "media20-engine-media-mode": media20_engine_media_mode,
       "media21": media21,
       "media21-name": media21_name,
       "media21-short-name": media21_short_name,
       "media21-page-count": media21_page_count,
       "media21-engine-media-mode": media21_engine_media_mode,
       "media22": media22,
       "media22-name": media22_name,
       "media22-short-name": media22_short_name,
       "media22-page-count": media22_page_count,
       "media22-engine-media-mode": media22_engine_media_mode,
       "media23": media23,
       "media23-name": media23_name,
       "media23-short-name": media23_short_name,
       "media23-page-count": media23_page_count,
       "media23-engine-media-mode": media23_engine_media_mode,
       "media24": media24,
       "media24-name": media24_name,
       "media24-short-name": media24_short_name,
       "media24-page-count": media24_page_count,
       "media24-engine-media-mode": media24_engine_media_mode,
       "media25": media25,
       "media25-name": media25_name,
       "media25-short-name": media25_short_name,
       "media25-page-count": media25_page_count,
       "media25-engine-media-mode": media25_engine_media_mode,
       "media26": media26,
       "media26-name": media26_name,
       "media26-short-name": media26_short_name,
       "media26-page-count": media26_page_count,
       "media26-engine-media-mode": media26_engine_media_mode,
       "media-modes": media_modes,
       "engine-media-modes-supported1": engine_media_modes_supported1,
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
       "consumable-status-formatter-color-page-count": consumable_status_formatter_color_page_count,
       "consumable-status-page-count-out-while-cartridge-out-override-active": consumable_status_page_count_out_while_cartridge_out_override_active,
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
       "device-used-while-cartridge-out-override-active": device_used_while_cartridge_out_override_active,
       "consumable-notification-status": consumable_notification_status,
       "print-meter": print_meter,
       "printer-average": printer_average,
       "printer-average-marking-agent-coverage": printer_average_marking_agent_coverage,
       "printer-average-marking-agent-coverage-sum": printer_average_marking_agent_coverage_sum,
       "printer-average-marking-agent-coverage-sum-squared": printer_average_marking_agent_coverage_sum_squared,
       "printer-average-marking-agent-units-per-gram": printer_average_marking_agent_units_per_gram,
       "printer-average-marking-agent-coverage-actual": printer_average_marking_agent_coverage_actual,
       "menus": menus,
       "copier": copier,
       "settings-copier": settings_copier,
       "default-copier-media-size": default_copier_media_size,
       "default-copier-image-type": default_copier_image_type,
       "copier-media-type": copier_media_type,
       "default-copy-duplex-mode": default_copy_duplex_mode,
       "default-copy-input-tray": default_copy_input_tray,
       "default-copy-output-bin": default_copy_output_bin,
       "default-copy-reset-timeout": default_copy_reset_timeout,
       "default-copier-quantity": default_copier_quantity,
       "default-copier-flip-pages-up": default_copier_flip_pages_up,
       "default-copier-pages-per-sheet": default_copier_pages_per_sheet,
       "default-copier-page-borders": default_copier_page_borders,
       "default-copier-collate": default_copier_collate,
       "default-copier-contrast": default_copier_contrast,
       "default-copier-edge-to-edge": default_copier_edge_to_edge,
       "copy-job-scan-ahead": copy_job_scan_ahead,
       "copy-job-auto-interrupt": copy_job_auto_interrupt,
       "copy-job-interrupt-copy-jobs": copy_job_interrupt_copy_jobs,
       "copy-job-hold-off-print-jobs": copy_job_hold_off_print_jobs,
       "copy-job-hold-time": copy_job_hold_time,
       "default-copy-job-chromaticity": default_copy_job_chromaticity,
       "first-copy-speed": first_copy_speed,
       "copier-job-border-setting": copier_job_border_setting,
       "color-copy-enabled": color_copy_enabled,
       "channel": channel,
       "channelprinteralert": channelprinteralert,
       "tables": tables}
)
