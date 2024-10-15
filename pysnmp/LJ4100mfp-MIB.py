# SNMP MIB module (LJ4100mfp-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/LJ4100mfp-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:18:40 2024
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
_System_ObjectIdentity = ObjectIdentity
system = _System_ObjectIdentity(
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
_Perm_store_init_occurred_Type = OctetString
_Perm_store_init_occurred_Object = MibScalar
perm_store_init_occurred = _Perm_store_init_occurred_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 2, 10),
    _Perm_store_init_occurred_Type()
)
perm_store_init_occurred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perm_store_init_occurred.setStatus("optional")


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


class _Background_status_msg_line1_part1_Type(DisplayString):
    """Custom type background_status_msg_line1_part1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Background_status_msg_line1_part1_Type.__name__ = "DisplayString"
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


class _Background_status_msg_line2_part1_Type(DisplayString):
    """Custom type background_status_msg_line2_part1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Background_status_msg_line2_part1_Type.__name__ = "DisplayString"
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


class _Background_status_msg_line3_part1_Type(DisplayString):
    """Custom type background_status_msg_line3_part1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Background_status_msg_line3_part1_Type.__name__ = "DisplayString"
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


class _Background_status_msg_line4_part1_Type(DisplayString):
    """Custom type background_status_msg_line4_part1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Background_status_msg_line4_part1_Type.__name__ = "DisplayString"
_Background_status_msg_line4_part1_Object = MibScalar
background_status_msg_line4_part1 = _Background_status_msg_line4_part1_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 2, 37, 4, 1),
    _Background_status_msg_line4_part1_Type()
)
background_status_msg_line4_part1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    background_status_msg_line4_part1.setStatus("optional")


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
_Localization_languages_supported_Type = DisplayString
_Localization_languages_supported_Object = MibScalar
localization_languages_supported = _Localization_languages_supported_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 2, 52),
    _Localization_languages_supported_Type()
)
localization_languages_supported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    localization_languages_supported.setStatus("optional")
_Localization_countries_supported_Type = DisplayString
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
control_panel_key_press.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    control_panel_key_press.setStatus("optional")
_Id_ObjectIdentity = ObjectIdentity
id = _Id_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 3)
)
_Model_number_Type = DisplayString
_Model_number_Object = MibScalar
model_number = _Model_number_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 3, 1),
    _Model_number_Type()
)
model_number.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    model_number.setStatus("optional")


class _Model_name_Type(DisplayString):
    """Custom type model_name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Model_name_Type.__name__ = "DisplayString"
_Model_name_Object = MibScalar
model_name = _Model_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 3, 2),
    _Model_name_Type()
)
model_name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    model_name.setStatus("optional")


class _Serial_number_Type(DisplayString):
    """Custom type serial_number based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_Serial_number_Type.__name__ = "DisplayString"
_Serial_number_Object = MibScalar
serial_number = _Serial_number_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 3, 3),
    _Serial_number_Type()
)
serial_number.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serial_number.setStatus("optional")
_Fw_rom_datecode_Type = DisplayString
_Fw_rom_datecode_Object = MibScalar
fw_rom_datecode = _Fw_rom_datecode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 3, 5),
    _Fw_rom_datecode_Type()
)
fw_rom_datecode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fw_rom_datecode.setStatus("optional")
_Fw_rom_revision_Type = DisplayString
_Fw_rom_revision_Object = MibScalar
fw_rom_revision = _Fw_rom_revision_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 3, 6),
    _Fw_rom_revision_Type()
)
fw_rom_revision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fw_rom_revision.setStatus("optional")


class _Device_name_Type(DisplayString):
    """Custom type device_name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Device_name_Type.__name__ = "DisplayString"
_Device_name_Object = MibScalar
device_name = _Device_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 3, 10),
    _Device_name_Type()
)
device_name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    device_name.setStatus("optional")
_Device_location_Type = DisplayString
_Device_location_Object = MibScalar
device_location = _Device_location_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 3, 11),
    _Device_location_Type()
)
device_location.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    device_location.setStatus("optional")
_Asset_number_Type = DisplayString
_Asset_number_Object = MibScalar
asset_number = _Asset_number_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 3, 12),
    _Asset_number_Type()
)
asset_number.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asset_number.setStatus("optional")
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
_Simm3_ObjectIdentity = ObjectIdentity
simm3 = _Simm3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 1, 3)
)


class _Simm3_type_Type(Integer32):
    """Custom type simm3_type based on Integer32"""
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


_Simm3_type_Type.__name__ = "Integer32"
_Simm3_type_Object = MibScalar
simm3_type = _Simm3_type_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 1, 3, 4),
    _Simm3_type_Type()
)
simm3_type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simm3_type.setStatus("optional")
_Simm3_capacity_Type = Integer32
_Simm3_capacity_Object = MibScalar
simm3_capacity = _Simm3_capacity_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 1, 3, 5),
    _Simm3_capacity_Type()
)
simm3_capacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simm3_capacity.setStatus("optional")
_Simm3_bank_ObjectIdentity = ObjectIdentity
simm3_bank = _Simm3_bank_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 1, 3, 6)
)
_Simm3_bank1_ObjectIdentity = ObjectIdentity
simm3_bank1 = _Simm3_bank1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 1, 3, 6, 1)
)


class _Simm3_bank1_type_Type(Integer32):
    """Custom type simm3_bank1_type based on Integer32"""
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


_Simm3_bank1_type_Type.__name__ = "Integer32"
_Simm3_bank1_type_Object = MibScalar
simm3_bank1_type = _Simm3_bank1_type_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 1, 3, 6, 1, 1),
    _Simm3_bank1_type_Type()
)
simm3_bank1_type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simm3_bank1_type.setStatus("optional")
_Simm3_bank1_capacity_Type = Integer32
_Simm3_bank1_capacity_Object = MibScalar
simm3_bank1_capacity = _Simm3_bank1_capacity_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 1, 3, 6, 1, 2),
    _Simm3_bank1_capacity_Type()
)
simm3_bank1_capacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simm3_bank1_capacity.setStatus("optional")
_Simm3_bank2_ObjectIdentity = ObjectIdentity
simm3_bank2 = _Simm3_bank2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 1, 3, 6, 2)
)


class _Simm3_bank2_type_Type(Integer32):
    """Custom type simm3_bank2_type based on Integer32"""
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


_Simm3_bank2_type_Type.__name__ = "Integer32"
_Simm3_bank2_type_Object = MibScalar
simm3_bank2_type = _Simm3_bank2_type_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 1, 3, 6, 2, 1),
    _Simm3_bank2_type_Type()
)
simm3_bank2_type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simm3_bank2_type.setStatus("optional")
_Simm3_bank2_capacity_Type = Integer32
_Simm3_bank2_capacity_Object = MibScalar
simm3_bank2_capacity = _Simm3_bank2_capacity_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 1, 3, 6, 2, 2),
    _Simm3_bank2_capacity_Type()
)
simm3_bank2_capacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simm3_bank2_capacity.setStatus("optional")
_Simm4_ObjectIdentity = ObjectIdentity
simm4 = _Simm4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 1, 4)
)


class _Simm4_type_Type(Integer32):
    """Custom type simm4_type based on Integer32"""
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


_Simm4_type_Type.__name__ = "Integer32"
_Simm4_type_Object = MibScalar
simm4_type = _Simm4_type_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 1, 4, 4),
    _Simm4_type_Type()
)
simm4_type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simm4_type.setStatus("optional")
_Simm4_capacity_Type = Integer32
_Simm4_capacity_Object = MibScalar
simm4_capacity = _Simm4_capacity_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 1, 4, 5),
    _Simm4_capacity_Type()
)
simm4_capacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simm4_capacity.setStatus("optional")
_Simm4_bank_ObjectIdentity = ObjectIdentity
simm4_bank = _Simm4_bank_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 1, 4, 6)
)
_Simm4_bank1_ObjectIdentity = ObjectIdentity
simm4_bank1 = _Simm4_bank1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 1, 4, 6, 1)
)


class _Simm4_bank1_type_Type(Integer32):
    """Custom type simm4_bank1_type based on Integer32"""
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


_Simm4_bank1_type_Type.__name__ = "Integer32"
_Simm4_bank1_type_Object = MibScalar
simm4_bank1_type = _Simm4_bank1_type_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 1, 4, 6, 1, 1),
    _Simm4_bank1_type_Type()
)
simm4_bank1_type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simm4_bank1_type.setStatus("optional")
_Simm4_bank1_capacity_Type = Integer32
_Simm4_bank1_capacity_Object = MibScalar
simm4_bank1_capacity = _Simm4_bank1_capacity_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 1, 4, 6, 1, 2),
    _Simm4_bank1_capacity_Type()
)
simm4_bank1_capacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simm4_bank1_capacity.setStatus("optional")
_Simm4_bank2_ObjectIdentity = ObjectIdentity
simm4_bank2 = _Simm4_bank2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 1, 4, 6, 2)
)


class _Simm4_bank2_type_Type(Integer32):
    """Custom type simm4_bank2_type based on Integer32"""
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


_Simm4_bank2_type_Type.__name__ = "Integer32"
_Simm4_bank2_type_Object = MibScalar
simm4_bank2_type = _Simm4_bank2_type_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 1, 4, 6, 2, 1),
    _Simm4_bank2_type_Type()
)
simm4_bank2_type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simm4_bank2_type.setStatus("optional")
_Simm4_bank2_capacity_Type = Integer32
_Simm4_bank2_capacity_Object = MibScalar
simm4_bank2_capacity = _Simm4_bank2_capacity_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 1, 4, 6, 2, 2),
    _Simm4_bank2_capacity_Type()
)
simm4_bank2_capacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simm4_bank2_capacity.setStatus("optional")
_Mio_ObjectIdentity = ObjectIdentity
mio = _Mio_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 3)
)
_Mio1_ObjectIdentity = ObjectIdentity
mio1 = _Mio1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 3, 1)
)
_Mio1_model_name_Type = DisplayString
_Mio1_model_name_Object = MibScalar
mio1_model_name = _Mio1_model_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 3, 1, 2),
    _Mio1_model_name_Type()
)
mio1_model_name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mio1_model_name.setStatus("optional")
_Mio1_manufacturing_info_Type = DisplayString
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
_Mio2_model_name_Type = DisplayString
_Mio2_model_name_Object = MibScalar
mio2_model_name = _Mio2_model_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 3, 2, 2),
    _Mio2_model_name_Type()
)
mio2_model_name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mio2_model_name.setStatus("optional")
_Mio2_manufacturing_info_Type = DisplayString
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
_Mio3_model_name_Type = DisplayString
_Mio3_model_name_Object = MibScalar
mio3_model_name = _Mio3_model_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 3, 3, 2),
    _Mio3_model_name_Type()
)
mio3_model_name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mio3_model_name.setStatus("optional")
_Mio3_manufacturing_info_Type = DisplayString
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
_Phd_ObjectIdentity = ObjectIdentity
phd = _Phd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 5)
)
_Phd1_ObjectIdentity = ObjectIdentity
phd1 = _Phd1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 5, 1)
)
_Phd1_model_Type = DisplayString
_Phd1_model_Object = MibScalar
phd1_model = _Phd1_model_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 5, 1, 1),
    _Phd1_model_Type()
)
phd1_model.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phd1_model.setStatus("optional")
_Phd1_manufacturing_info_Type = DisplayString
_Phd1_manufacturing_info_Object = MibScalar
phd1_manufacturing_info = _Phd1_manufacturing_info_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 5, 1, 2),
    _Phd1_manufacturing_info_Type()
)
phd1_manufacturing_info.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phd1_manufacturing_info.setStatus("optional")


class _Phd1_type_Type(Integer32):
    """Custom type phd1_type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            10
        )
    )
    namedValues = NamedValues(
        ("eInputPHD", 10)
    )


_Phd1_type_Type.__name__ = "Integer32"
_Phd1_type_Object = MibScalar
phd1_type = _Phd1_type_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 5, 1, 3),
    _Phd1_type_Type()
)
phd1_type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phd1_type.setStatus("optional")
_Phd1_capacity_Type = Integer32
_Phd1_capacity_Object = MibScalar
phd1_capacity = _Phd1_capacity_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 5, 1, 4),
    _Phd1_capacity_Type()
)
phd1_capacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phd1_capacity.setStatus("optional")
_Phd2_ObjectIdentity = ObjectIdentity
phd2 = _Phd2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 5, 2)
)
_Phd2_model_Type = DisplayString
_Phd2_model_Object = MibScalar
phd2_model = _Phd2_model_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 5, 2, 1),
    _Phd2_model_Type()
)
phd2_model.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phd2_model.setStatus("optional")
_Phd2_manufacturing_info_Type = DisplayString
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
_Phd3_ObjectIdentity = ObjectIdentity
phd3 = _Phd3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 5, 3)
)
_Phd3_model_Type = DisplayString
_Phd3_model_Object = MibScalar
phd3_model = _Phd3_model_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 5, 3, 1),
    _Phd3_model_Type()
)
phd3_model.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phd3_model.setStatus("optional")
_Phd3_manufacturing_info_Type = DisplayString
_Phd3_manufacturing_info_Object = MibScalar
phd3_manufacturing_info = _Phd3_manufacturing_info_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 5, 3, 2),
    _Phd3_manufacturing_info_Type()
)
phd3_manufacturing_info.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phd3_manufacturing_info.setStatus("optional")


class _Phd3_type_Type(Integer32):
    """Custom type phd3_type based on Integer32"""
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


_Phd3_type_Type.__name__ = "Integer32"
_Phd3_type_Object = MibScalar
phd3_type = _Phd3_type_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 5, 3, 3),
    _Phd3_type_Type()
)
phd3_type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phd3_type.setStatus("optional")
_Phd3_capacity_Type = Integer32
_Phd3_capacity_Object = MibScalar
phd3_capacity = _Phd3_capacity_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 5, 3, 4),
    _Phd3_capacity_Type()
)
phd3_capacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phd3_capacity.setStatus("optional")
_Phd4_ObjectIdentity = ObjectIdentity
phd4 = _Phd4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 5, 4)
)
_Phd4_model_Type = DisplayString
_Phd4_model_Object = MibScalar
phd4_model = _Phd4_model_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 5, 4, 1),
    _Phd4_model_Type()
)
phd4_model.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phd4_model.setStatus("optional")
_Phd4_manufacturing_info_Type = DisplayString
_Phd4_manufacturing_info_Object = MibScalar
phd4_manufacturing_info = _Phd4_manufacturing_info_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 5, 4, 2),
    _Phd4_manufacturing_info_Type()
)
phd4_manufacturing_info.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phd4_manufacturing_info.setStatus("optional")


class _Phd4_type_Type(Integer32):
    """Custom type phd4_type based on Integer32"""
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


_Phd4_type_Type.__name__ = "Integer32"
_Phd4_type_Object = MibScalar
phd4_type = _Phd4_type_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 5, 4, 3),
    _Phd4_type_Type()
)
phd4_type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phd4_type.setStatus("optional")
_Phd4_capacity_Type = Integer32
_Phd4_capacity_Object = MibScalar
phd4_capacity = _Phd4_capacity_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 5, 4, 4),
    _Phd4_capacity_Type()
)
phd4_capacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phd4_capacity.setStatus("optional")
_Phd5_ObjectIdentity = ObjectIdentity
phd5 = _Phd5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 5, 5)
)
_Phd5_model_Type = DisplayString
_Phd5_model_Object = MibScalar
phd5_model = _Phd5_model_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 5, 5, 1),
    _Phd5_model_Type()
)
phd5_model.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phd5_model.setStatus("optional")
_Phd5_manufacturing_info_Type = DisplayString
_Phd5_manufacturing_info_Object = MibScalar
phd5_manufacturing_info = _Phd5_manufacturing_info_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 5, 5, 2),
    _Phd5_manufacturing_info_Type()
)
phd5_manufacturing_info.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phd5_manufacturing_info.setStatus("optional")


class _Phd5_type_Type(Integer32):
    """Custom type phd5_type based on Integer32"""
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


_Phd5_type_Type.__name__ = "Integer32"
_Phd5_type_Object = MibScalar
phd5_type = _Phd5_type_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 5, 5, 3),
    _Phd5_type_Type()
)
phd5_type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phd5_type.setStatus("optional")
_Phd5_capacity_Type = Integer32
_Phd5_capacity_Object = MibScalar
phd5_capacity = _Phd5_capacity_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 5, 5, 4),
    _Phd5_capacity_Type()
)
phd5_capacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phd5_capacity.setStatus("optional")
_Phd6_ObjectIdentity = ObjectIdentity
phd6 = _Phd6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 5, 6)
)
_Phd6_model_Type = DisplayString
_Phd6_model_Object = MibScalar
phd6_model = _Phd6_model_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 5, 6, 1),
    _Phd6_model_Type()
)
phd6_model.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phd6_model.setStatus("optional")
_Phd6_manufacturing_info_Type = DisplayString
_Phd6_manufacturing_info_Object = MibScalar
phd6_manufacturing_info = _Phd6_manufacturing_info_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 5, 6, 2),
    _Phd6_manufacturing_info_Type()
)
phd6_manufacturing_info.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phd6_manufacturing_info.setStatus("optional")


class _Phd6_type_Type(Integer32):
    """Custom type phd6_type based on Integer32"""
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


_Phd6_type_Type.__name__ = "Integer32"
_Phd6_type_Object = MibScalar
phd6_type = _Phd6_type_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 5, 6, 3),
    _Phd6_type_Type()
)
phd6_type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phd6_type.setStatus("optional")
_Phd6_capacity_Type = Integer32
_Phd6_capacity_Object = MibScalar
phd6_capacity = _Phd6_capacity_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 5, 6, 4),
    _Phd6_capacity_Type()
)
phd6_capacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phd6_capacity.setStatus("optional")
_Socket_ping_ObjectIdentity = ObjectIdentity
socket_ping = _Socket_ping_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 7)
)


class _Socket_ping_job_events_version_Type(DisplayString):
    """Custom type socket_ping_job_events_version based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_Socket_ping_job_events_version_Type.__name__ = "DisplayString"
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


class _Self_test_Type(Integer32):
    """Custom type self_test based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4)
        )
    )
    namedValues = NamedValues(
        *(("eNonDestructiveSelfTest", 4),
          ("eNotInASelfTest", 1))
    )


_Self_test_Type.__name__ = "Integer32"
_Self_test_Object = MibScalar
self_test = _Self_test_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 5, 1),
    _Self_test_Type()
)
self_test.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    self_test.setStatus("optional")


class _Print_internal_page_Type(Integer32):
    """Custom type print_internal_page based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              7,
              8,
              9,
              100,
              101,
              350,
              450)
        )
    )
    namedValues = NamedValues(
        *(("eDeviceDemoPage1ConfigurationPage", 3),
          ("eDeviceDemoPage5ErrorLog", 7),
          ("eDeviceDemoPage6FileSystemDirectoryListing", 8),
          ("eDeviceDemoPage7MenuMap", 9),
          ("eNotPrintingAnInternalPage", 1),
          ("ePCLFontList1", 350),
          ("ePSFontList", 450),
          ("ePrintUsagePage", 100),
          ("ePrintingAnUnknownInternalPage", 2),
          ("eSuppliesPage", 101))
    )


_Print_internal_page_Type.__name__ = "Integer32"
_Print_internal_page_Object = MibScalar
print_internal_page = _Print_internal_page_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 5, 2),
    _Print_internal_page_Type()
)
print_internal_page.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    print_internal_page.setStatus("optional")
_Engine_self_diagnostic_Type = OctetString
_Engine_self_diagnostic_Object = MibScalar
engine_self_diagnostic = _Engine_self_diagnostic_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 5, 7),
    _Engine_self_diagnostic_Type()
)
engine_self_diagnostic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engine_self_diagnostic.setStatus("optional")
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
        ValueRangeConstraint(0, 32767),
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
_Job_info_name1_Type = DisplayString
_Job_info_name1_Object = MibScalar
job_info_name1 = _Job_info_name1_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 5, 1),
    _Job_info_name1_Type()
)
job_info_name1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    job_info_name1.setStatus("optional")
_Job_info_name2_Type = DisplayString
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
_Job_info_accounting_scanned_media_simplex_count_Type = OctetString
_Job_info_accounting_scanned_media_simplex_count_Object = MibScalar
job_info_accounting_scanned_media_simplex_count = _Job_info_accounting_scanned_media_simplex_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 5, 28, 12),
    _Job_info_accounting_scanned_media_simplex_count_Type()
)
job_info_accounting_scanned_media_simplex_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    job_info_accounting_scanned_media_simplex_count.setStatus("optional")
_Job_info_accounting_scanned_media_duplex_count_Type = OctetString
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
              1000)
        )
    )
    namedValues = NamedValues(
        *(("eAutoCleaningPage", 8),
          ("eCleaningPage", 7),
          ("eCopyInterruptJob", 4),
          ("eCopyJob", 3),
          ("eDigitalSendJob", 9),
          ("eIPPJob", 2),
          ("eInternalPage", 6),
          ("eJetSendJob", 5),
          ("ePrintJob", 1),
          ("eUnknownJob", 1000))
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


class _Held_job_user_name_Type(DisplayString):
    """Custom type held_job_user_name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_Held_job_user_name_Type.__name__ = "DisplayString"
_Held_job_user_name_Object = MibScalar
held_job_user_name = _Held_job_user_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 7, 1, 1),
    _Held_job_user_name_Type()
)
held_job_user_name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    held_job_user_name.setStatus("optional")


class _Held_job_job_name_Type(DisplayString):
    """Custom type held_job_job_name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_Held_job_job_name_Type.__name__ = "DisplayString"
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


class _Held_job_pin_Type(DisplayString):
    """Custom type held_job_pin based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_Held_job_pin_Type.__name__ = "DisplayString"
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


class _Usage_instructions_line1_Type(DisplayString):
    """Custom type usage_instructions_line1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_Usage_instructions_line1_Type.__name__ = "DisplayString"
_Usage_instructions_line1_Object = MibScalar
usage_instructions_line1 = _Usage_instructions_line1_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 16, 1, 5),
    _Usage_instructions_line1_Type()
)
usage_instructions_line1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usage_instructions_line1.setStatus("optional")


class _Usage_instructions_line2_Type(DisplayString):
    """Custom type usage_instructions_line2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_Usage_instructions_line2_Type.__name__ = "DisplayString"
_Usage_instructions_line2_Object = MibScalar
usage_instructions_line2 = _Usage_instructions_line2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 16, 1, 6),
    _Usage_instructions_line2_Type()
)
usage_instructions_line2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usage_instructions_line2.setStatus("optional")


class _Usage_instructions_line3_Type(DisplayString):
    """Custom type usage_instructions_line3 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_Usage_instructions_line3_Type.__name__ = "DisplayString"
_Usage_instructions_line3_Object = MibScalar
usage_instructions_line3 = _Usage_instructions_line3_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 16, 1, 7),
    _Usage_instructions_line3_Type()
)
usage_instructions_line3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usage_instructions_line3.setStatus("optional")


class _Usage_instructions_line4_Type(DisplayString):
    """Custom type usage_instructions_line4 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_Usage_instructions_line4_Type.__name__ = "DisplayString"
_Usage_instructions_line4_Object = MibScalar
usage_instructions_line4 = _Usage_instructions_line4_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 16, 1, 8),
    _Usage_instructions_line4_Type()
)
usage_instructions_line4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usage_instructions_line4.setStatus("optional")
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("eDownloadComplete", 8),
          ("eIdle", 1),
          ("eReceivedImage", 2),
          ("eReceivedImageError", 3),
          ("eVerifiedImage", 4),
          ("eVerifiedImageError", 5),
          ("eWritingImage", 6),
          ("eWritingImageError", 7))
    )


_Firmware_download_current_state_Type.__name__ = "Integer32"
_Firmware_download_current_state_Object = MibScalar
firmware_download_current_state = _Firmware_download_current_state_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 18, 4),
    _Firmware_download_current_state_Type()
)
firmware_download_current_state.setMaxAccess("read-only")
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
_Firmware_download_name_Type = DisplayString
_Firmware_download_name_Object = MibScalar
firmware_download_name = _Firmware_download_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 18, 6),
    _Firmware_download_name_Type()
)
firmware_download_name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firmware_download_name.setStatus("mandatory")
_Firmware_download_version_Type = DisplayString
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
_Os_execute_file_Type = DisplayString
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("eIdle", 1),
          ("eReceivedImage", 2),
          ("eReceivedImageError", 3),
          ("eUpgradeComplete", 8),
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
_Upgradable_devices_name_Type = DisplayString
_Upgradable_devices_name_Object = MibScalar
upgradable_devices_name = _Upgradable_devices_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 20, 6),
    _Upgradable_devices_name_Type()
)
upgradable_devices_name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upgradable_devices_name.setStatus("mandatory")
_Upgradable_devices_version_Type = DisplayString
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


class _Scanner_accessory_dimm1_type_Type(Integer32):
    """Custom type scanner_accessory_dimm1_type based on Integer32"""
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


_Scanner_accessory_dimm1_type_Type.__name__ = "Integer32"
_Scanner_accessory_dimm1_type_Object = MibScalar
scanner_accessory_dimm1_type = _Scanner_accessory_dimm1_type_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 1, 55),
    _Scanner_accessory_dimm1_type_Type()
)
scanner_accessory_dimm1_type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scanner_accessory_dimm1_type.setStatus("optional")


class _Scanner_accessory_dimm2_type_Type(Integer32):
    """Custom type scanner_accessory_dimm2_type based on Integer32"""
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


_Scanner_accessory_dimm2_type_Type.__name__ = "Integer32"
_Scanner_accessory_dimm2_type_Object = MibScalar
scanner_accessory_dimm2_type = _Scanner_accessory_dimm2_type_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 1, 56),
    _Scanner_accessory_dimm2_type_Type()
)
scanner_accessory_dimm2_type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scanner_accessory_dimm2_type.setStatus("optional")
_Scanner_accessory_dimm1_capacity_Type = Integer32
_Scanner_accessory_dimm1_capacity_Object = MibScalar
scanner_accessory_dimm1_capacity = _Scanner_accessory_dimm1_capacity_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 1, 57),
    _Scanner_accessory_dimm1_capacity_Type()
)
scanner_accessory_dimm1_capacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scanner_accessory_dimm1_capacity.setStatus("optional")
_Scanner_accessory_dimm2_capacity_Type = Integer32
_Scanner_accessory_dimm2_capacity_Object = MibScalar
scanner_accessory_dimm2_capacity = _Scanner_accessory_dimm2_capacity_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 1, 58),
    _Scanner_accessory_dimm2_capacity_Type()
)
scanner_accessory_dimm2_capacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scanner_accessory_dimm2_capacity.setStatus("optional")
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
_Scanner_accessory_digital_send_module_url_Type = DisplayString
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
              25,
              26,
              45)
        )
    )
    namedValues = NamedValues(
        *(("eISOandJISA4", 26),
          ("eISOandJISA5", 25),
          ("eJISB5", 45),
          ("eUSExecutive", 1),
          ("eUSLegal", 3),
          ("eUSLetter", 2))
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


class _Default_scan_heavy_media_mode_Type(Integer32):
    """Custom type default_scan_heavy_media_mode based on Integer32"""
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


_Default_scan_heavy_media_mode_Type.__name__ = "Integer32"
_Default_scan_heavy_media_mode_Object = MibScalar
default_scan_heavy_media_mode = _Default_scan_heavy_media_mode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 1, 72),
    _Default_scan_heavy_media_mode_Type()
)
default_scan_heavy_media_mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    default_scan_heavy_media_mode.setStatus("optional")


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
_Scanner_accessory_digital_send_log_event_counter_Type = Integer32
_Scanner_accessory_digital_send_log_event_counter_Object = MibScalar
scanner_accessory_digital_send_log_event_counter = _Scanner_accessory_digital_send_log_event_counter_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 1, 79),
    _Scanner_accessory_digital_send_log_event_counter_Type()
)
scanner_accessory_digital_send_log_event_counter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scanner_accessory_digital_send_log_event_counter.setStatus("optional")
_Scanner_accessory_digital_send_config_email_gateway_Type = DisplayString
_Scanner_accessory_digital_send_config_email_gateway_Object = MibScalar
scanner_accessory_digital_send_config_email_gateway = _Scanner_accessory_digital_send_config_email_gateway_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 1, 80),
    _Scanner_accessory_digital_send_config_email_gateway_Type()
)
scanner_accessory_digital_send_config_email_gateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scanner_accessory_digital_send_config_email_gateway.setStatus("optional")
_Scanner_accessory_digital_send_config_ldap_gateway_Type = DisplayString
_Scanner_accessory_digital_send_config_ldap_gateway_Object = MibScalar
scanner_accessory_digital_send_config_ldap_gateway = _Scanner_accessory_digital_send_config_ldap_gateway_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 1, 81),
    _Scanner_accessory_digital_send_config_ldap_gateway_Type()
)
scanner_accessory_digital_send_config_ldap_gateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scanner_accessory_digital_send_config_ldap_gateway.setStatus("optional")
_Scanner_accessory_digital_send_config_dsm_enabled_fax_Type = Integer32
_Scanner_accessory_digital_send_config_dsm_enabled_fax_Object = MibScalar
scanner_accessory_digital_send_config_dsm_enabled_fax = _Scanner_accessory_digital_send_config_dsm_enabled_fax_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 1, 82),
    _Scanner_accessory_digital_send_config_dsm_enabled_fax_Type()
)
scanner_accessory_digital_send_config_dsm_enabled_fax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scanner_accessory_digital_send_config_dsm_enabled_fax.setStatus("optional")
_Scanner_accessory_digital_send_config_fax_embedded_Type = Integer32
_Scanner_accessory_digital_send_config_fax_embedded_Object = MibScalar
scanner_accessory_digital_send_config_fax_embedded = _Scanner_accessory_digital_send_config_fax_embedded_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 1, 83),
    _Scanner_accessory_digital_send_config_fax_embedded_Type()
)
scanner_accessory_digital_send_config_fax_embedded.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scanner_accessory_digital_send_config_fax_embedded.setStatus("optional")
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
              6)
        )
    )
    namedValues = NamedValues(
        *(("eLowMemory", 4),
          ("eNoError", 1),
          ("eScannerBusy", 6),
          ("eScannerFeederEmpty", 3),
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
              17,
              18,
              25,
              26,
              45,
              65,
              80,
              81,
              90,
              91,
              100,
              101)
        )
    )
    namedValues = NamedValues(
        *(("eCommercial10", 81),
          ("eCustom", 101),
          ("eISOB5", 65),
          ("eISOandJISA4", 26),
          ("eISOandJISA5", 25),
          ("eInternationalB5", 100),
          ("eInternationalC5", 91),
          ("eInternationalDL", 90),
          ("eJISB5", 45),
          ("eJISExecutive", 18),
          ("eMonarch", 80),
          ("eROC16K", 17),
          ("eUSExecutive", 1),
          ("eUSLegal", 3),
          ("eUSLetter", 2))
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
_Default_media_name_Type = DisplayString
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("eInternal", 1),
          ("ePermanentSoft", 2),
          ("eRomSimm2", 11),
          ("eRomSimm3", 12),
          ("eRomSimm4", 13))
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
_Pjl_ObjectIdentity = ObjectIdentity
pjl = _Pjl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 5)
)
_Pjl_password_Type = Integer32
_Pjl_password_Object = MibScalar
pjl_password = _Pjl_password_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 5, 1),
    _Pjl_password_Type()
)
pjl_password.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pjl_password.setStatus("optional")
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
_Webserver_proc_sub_ObjectIdentity = ObjectIdentity
webserver_proc_sub = _Webserver_proc_sub_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 9)
)
_Settings_webserver_ObjectIdentity = ObjectIdentity
settings_webserver = _Settings_webserver_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 9, 1)
)


class _Web_server_password_Type(DisplayString):
    """Custom type web_server_password based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Web_server_password_Type.__name__ = "DisplayString"
_Web_server_password_Object = MibScalar
web_server_password = _Web_server_password_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 9, 1, 1),
    _Web_server_password_Type()
)
web_server_password.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    web_server_password.setStatus("optional")


class _Web_server_url_Type(DisplayString):
    """Custom type web_server_url based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Web_server_url_Type.__name__ = "DisplayString"
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
_Override_media_name_Type = DisplayString
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
              32764,
              32767)
        )
    )
    namedValues = NamedValues(
        *(("eAnyCustomSize", 32764),
          ("eCommercial10", 81),
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


class _Print_density_Type(Integer32):
    """Custom type print_density based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_Print_density_Type.__name__ = "Integer32"
_Print_density_Object = MibScalar
print_density = _Print_density_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 1, 5),
    _Print_density_Type()
)
print_density.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    print_density.setStatus("optional")
_Marking_agent_density_ObjectIdentity = ObjectIdentity
marking_agent_density = _Marking_agent_density_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 1, 9)
)
_Marking_agent_density_setting_Type = Integer32
_Marking_agent_density_setting_Object = MibScalar
marking_agent_density_setting = _Marking_agent_density_setting_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 1, 9, 1),
    _Marking_agent_density_setting_Type()
)
marking_agent_density_setting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    marking_agent_density_setting.setStatus("optional")


class _Autocleaning_page_enable_Type(Integer32):
    """Custom type autocleaning_page_enable based on Integer32"""
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


_Autocleaning_page_enable_Type.__name__ = "Integer32"
_Autocleaning_page_enable_Object = MibScalar
autocleaning_page_enable = _Autocleaning_page_enable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 1, 10),
    _Autocleaning_page_enable_Type()
)
autocleaning_page_enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autocleaning_page_enable.setStatus("optional")
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
        ValueRangeConstraint(0, 300000),
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
_Status_prt_eng_ObjectIdentity = ObjectIdentity
status_prt_eng = _Status_prt_eng_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 2)
)
_Duplex_page_count_Type = Integer32
_Duplex_page_count_Object = MibScalar
duplex_page_count = _Duplex_page_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 2, 22),
    _Duplex_page_count_Type()
)
duplex_page_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    duplex_page_count.setStatus("optional")


class _Print_engine_revision_Type(DisplayString):
    """Custom type print_engine_revision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Print_engine_revision_Type.__name__ = "DisplayString"
_Print_engine_revision_Object = MibScalar
print_engine_revision = _Print_engine_revision_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 2, 26),
    _Print_engine_revision_Type()
)
print_engine_revision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    print_engine_revision.setStatus("optional")
_Intray_ObjectIdentity = ObjectIdentity
intray = _Intray_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 3)
)
_Settings_intray_ObjectIdentity = ObjectIdentity
settings_intray = _Settings_intray_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 3, 1)
)


class _Mp_tray_Type(Integer32):
    """Custom type mp_tray based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("eCassette", 2),
          ("eFirst", 3))
    )


_Mp_tray_Type.__name__ = "Integer32"
_Mp_tray_Object = MibScalar
mp_tray = _Mp_tray_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 3, 1, 5),
    _Mp_tray_Type()
)
mp_tray.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mp_tray.setStatus("optional")


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
              17,
              18,
              25,
              26,
              45,
              65,
              80,
              81,
              90,
              91,
              100,
              101,
              32764,
              32767)
        )
    )
    namedValues = NamedValues(
        *(("eAnyCustomSize", 32764),
          ("eCommercial10", 81),
          ("eCustom", 101),
          ("eISOB5", 65),
          ("eISOandJISA4", 26),
          ("eISOandJISA5", 25),
          ("eInternationalB5", 100),
          ("eInternationalC5", 91),
          ("eInternationalDL", 90),
          ("eJISB5", 45),
          ("eJISExecutive", 18),
          ("eMonarch", 80),
          ("eRock16K", 17),
          ("eUSExecutive", 1),
          ("eUSLegal", 3),
          ("eUSLetter", 2),
          ("eUnknownMediaSize", 32767))
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
              17,
              18,
              25,
              26,
              65,
              80,
              81,
              90,
              91,
              100,
              101,
              32764,
              32767)
        )
    )
    namedValues = NamedValues(
        *(("eAnyCustomSize", 32764),
          ("eCommercial10", 81),
          ("eCustom", 101),
          ("eISOB5", 65),
          ("eISOandJISA4", 26),
          ("eISOandJISA5", 25),
          ("eInternationalB5", 100),
          ("eInternationalC5", 91),
          ("eInternationalDL", 90),
          ("eJISExecutive", 18),
          ("eMonarch", 80),
          ("eRock16K", 17),
          ("eUSExecutive", 1),
          ("eUSLegal", 3),
          ("eUSLetter", 2),
          ("eUnknownMediaSize", 32767))
    )


_Tray2_media_size_loaded_Type.__name__ = "Integer32"
_Tray2_media_size_loaded_Object = MibScalar
tray2_media_size_loaded = _Tray2_media_size_loaded_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 3, 3, 2, 1),
    _Tray2_media_size_loaded_Type()
)
tray2_media_size_loaded.setMaxAccess("read-only")
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
              17,
              18,
              25,
              26,
              65,
              80,
              81,
              90,
              91,
              100,
              101,
              32764,
              32767)
        )
    )
    namedValues = NamedValues(
        *(("eAnyCustomSize", 32764),
          ("eCommercial10", 81),
          ("eCustom", 101),
          ("eISOB5", 65),
          ("eISOandJISA4", 26),
          ("eISOandJISA5", 25),
          ("eInternationalB5", 100),
          ("eInternationalC5", 91),
          ("eInternationalDL", 90),
          ("eJISExecutive", 18),
          ("eMonarch", 80),
          ("eRock16K", 17),
          ("eUSExecutive", 1),
          ("eUSLegal", 3),
          ("eUSLetter", 2),
          ("eUnknownMediaSize", 32767))
    )


_Tray3_media_size_loaded_Type.__name__ = "Integer32"
_Tray3_media_size_loaded_Object = MibScalar
tray3_media_size_loaded = _Tray3_media_size_loaded_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 3, 3, 3, 1),
    _Tray3_media_size_loaded_Type()
)
tray3_media_size_loaded.setMaxAccess("read-only")
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
_Intray4_ObjectIdentity = ObjectIdentity
intray4 = _Intray4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 3, 3, 4)
)


class _Tray4_media_size_loaded_Type(Integer32):
    """Custom type tray4_media_size_loaded based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(80,
              81,
              90,
              91,
              100)
        )
    )
    namedValues = NamedValues(
        *(("eCommercial10", 81),
          ("eInternationalB5", 100),
          ("eInternationalC5", 91),
          ("eInternationalDL", 90),
          ("eMonarch", 80))
    )


_Tray4_media_size_loaded_Type.__name__ = "Integer32"
_Tray4_media_size_loaded_Object = MibScalar
tray4_media_size_loaded = _Tray4_media_size_loaded_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 3, 3, 4, 1),
    _Tray4_media_size_loaded_Type()
)
tray4_media_size_loaded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tray4_media_size_loaded.setStatus("optional")
_Tray4_phd_Type = Integer32
_Tray4_phd_Object = MibScalar
tray4_phd = _Tray4_phd_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 3, 3, 4, 12),
    _Tray4_phd_Type()
)
tray4_phd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tray4_phd.setStatus("optional")
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
              26,
              45,
              101,
              32764,
              32767)
        )
    )
    namedValues = NamedValues(
        *(("eAnyCustomSize", 32764),
          ("eCustom", 101),
          ("eISOandJISA4", 26),
          ("eJISB5", 45),
          ("eUSExecutive", 1),
          ("eUSLegal", 3),
          ("eUSLetter", 2),
          ("eUnknownMediaSize", 32767))
    )


_Tray5_media_size_loaded_Type.__name__ = "Integer32"
_Tray5_media_size_loaded_Object = MibScalar
tray5_media_size_loaded = _Tray5_media_size_loaded_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 3, 3, 5, 1),
    _Tray5_media_size_loaded_Type()
)
tray5_media_size_loaded.setMaxAccess("read-only")
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
              3,
              11,
              26,
              27,
              46)
        )
    )
    namedValues = NamedValues(
        *(("eISOandJISA3", 27),
          ("eISOandJISA4", 26),
          ("eJISB4", 46),
          ("eLedger", 11),
          ("eUSLegal", 3),
          ("eUSLetter", 2))
    )


_Tray6_media_size_loaded_Type.__name__ = "Integer32"
_Tray6_media_size_loaded_Object = MibScalar
tray6_media_size_loaded = _Tray6_media_size_loaded_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 3, 3, 6, 1),
    _Tray6_media_size_loaded_Type()
)
tray6_media_size_loaded.setMaxAccess("read-only")
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
_Intray7_ObjectIdentity = ObjectIdentity
intray7 = _Intray7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 3, 3, 7)
)


class _Tray7_media_size_loaded_Type(Integer32):
    """Custom type tray7_media_size_loaded based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              11,
              26,
              27,
              46)
        )
    )
    namedValues = NamedValues(
        *(("eISOandJISA3", 27),
          ("eISOandJISA4", 26),
          ("eJISB4", 46),
          ("eLedger", 11),
          ("eUSLegal", 3),
          ("eUSLetter", 2))
    )


_Tray7_media_size_loaded_Type.__name__ = "Integer32"
_Tray7_media_size_loaded_Object = MibScalar
tray7_media_size_loaded = _Tray7_media_size_loaded_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 3, 3, 7, 1),
    _Tray7_media_size_loaded_Type()
)
tray7_media_size_loaded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tray7_media_size_loaded.setStatus("optional")
_Tray7_phd_Type = Integer32
_Tray7_phd_Object = MibScalar
tray7_phd = _Tray7_phd_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 3, 3, 7, 12),
    _Tray7_phd_Type()
)
tray7_phd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tray7_phd.setStatus("optional")
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
_Outbin6_ObjectIdentity = ObjectIdentity
outbin6 = _Outbin6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 4, 3, 6)
)
_Outbin6_override_mode_Type = OctetString
_Outbin6_override_mode_Object = MibScalar
outbin6_override_mode = _Outbin6_override_mode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 4, 3, 6, 9),
    _Outbin6_override_mode_Type()
)
outbin6_override_mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outbin6_override_mode.setStatus("optional")
_Outbin6_maximum_binding_Type = Integer32
_Outbin6_maximum_binding_Object = MibScalar
outbin6_maximum_binding = _Outbin6_maximum_binding_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 4, 3, 6, 10),
    _Outbin6_maximum_binding_Type()
)
outbin6_maximum_binding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outbin6_maximum_binding.setStatus("optional")
_Outbin6_phd_Type = Integer32
_Outbin6_phd_Object = MibScalar
outbin6_phd = _Outbin6_phd_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 4, 3, 6, 11),
    _Outbin6_phd_Type()
)
outbin6_phd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outbin6_phd.setStatus("optional")
_Outbin6_error_info_Type = OctetString
_Outbin6_error_info_Object = MibScalar
outbin6_error_info = _Outbin6_error_info_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 4, 3, 6, 12),
    _Outbin6_error_info_Type()
)
outbin6_error_info.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outbin6_error_info.setStatus("optional")
_Outbin7_ObjectIdentity = ObjectIdentity
outbin7 = _Outbin7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 4, 3, 7)
)
_Outbin7_override_mode_Type = OctetString
_Outbin7_override_mode_Object = MibScalar
outbin7_override_mode = _Outbin7_override_mode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 4, 3, 7, 9),
    _Outbin7_override_mode_Type()
)
outbin7_override_mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outbin7_override_mode.setStatus("optional")
_Outbin7_maximum_binding_Type = Integer32
_Outbin7_maximum_binding_Object = MibScalar
outbin7_maximum_binding = _Outbin7_maximum_binding_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 4, 3, 7, 10),
    _Outbin7_maximum_binding_Type()
)
outbin7_maximum_binding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outbin7_maximum_binding.setStatus("optional")
_Outbin7_phd_Type = Integer32
_Outbin7_phd_Object = MibScalar
outbin7_phd = _Outbin7_phd_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 4, 3, 7, 11),
    _Outbin7_phd_Type()
)
outbin7_phd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outbin7_phd.setStatus("optional")
_Outbin7_error_info_Type = OctetString
_Outbin7_error_info_Object = MibScalar
outbin7_error_info = _Outbin7_error_info_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 4, 3, 7, 12),
    _Outbin7_error_info_Type()
)
outbin7_error_info.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outbin7_error_info.setStatus("optional")
_Outbin8_ObjectIdentity = ObjectIdentity
outbin8 = _Outbin8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 4, 3, 8)
)
_Outbin8_override_mode_Type = OctetString
_Outbin8_override_mode_Object = MibScalar
outbin8_override_mode = _Outbin8_override_mode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 4, 3, 8, 9),
    _Outbin8_override_mode_Type()
)
outbin8_override_mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outbin8_override_mode.setStatus("optional")
_Outbin8_maximum_binding_Type = Integer32
_Outbin8_maximum_binding_Object = MibScalar
outbin8_maximum_binding = _Outbin8_maximum_binding_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 4, 3, 8, 10),
    _Outbin8_maximum_binding_Type()
)
outbin8_maximum_binding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outbin8_maximum_binding.setStatus("optional")
_Outbin8_phd_Type = Integer32
_Outbin8_phd_Object = MibScalar
outbin8_phd = _Outbin8_phd_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 4, 3, 8, 11),
    _Outbin8_phd_Type()
)
outbin8_phd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outbin8_phd.setStatus("optional")
_Outbin8_error_info_Type = OctetString
_Outbin8_error_info_Object = MibScalar
outbin8_error_info = _Outbin8_error_info_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 4, 3, 8, 12),
    _Outbin8_error_info_Type()
)
outbin8_error_info.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outbin8_error_info.setStatus("optional")
_Outbin9_ObjectIdentity = ObjectIdentity
outbin9 = _Outbin9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 4, 3, 9)
)
_Outbin9_override_mode_Type = OctetString
_Outbin9_override_mode_Object = MibScalar
outbin9_override_mode = _Outbin9_override_mode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 4, 3, 9, 9),
    _Outbin9_override_mode_Type()
)
outbin9_override_mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outbin9_override_mode.setStatus("optional")
_Outbin9_maximum_binding_Type = Integer32
_Outbin9_maximum_binding_Object = MibScalar
outbin9_maximum_binding = _Outbin9_maximum_binding_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 4, 3, 9, 10),
    _Outbin9_maximum_binding_Type()
)
outbin9_maximum_binding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outbin9_maximum_binding.setStatus("optional")
_Outbin9_phd_Type = Integer32
_Outbin9_phd_Object = MibScalar
outbin9_phd = _Outbin9_phd_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 4, 3, 9, 11),
    _Outbin9_phd_Type()
)
outbin9_phd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outbin9_phd.setStatus("optional")
_Outbin9_error_info_Type = OctetString
_Outbin9_error_info_Object = MibScalar
outbin9_error_info = _Outbin9_error_info_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 4, 3, 9, 12),
    _Outbin9_error_info_Type()
)
outbin9_error_info.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outbin9_error_info.setStatus("optional")
_Outbin10_ObjectIdentity = ObjectIdentity
outbin10 = _Outbin10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 4, 3, 10)
)
_Outbin10_override_mode_Type = OctetString
_Outbin10_override_mode_Object = MibScalar
outbin10_override_mode = _Outbin10_override_mode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 4, 3, 10, 9),
    _Outbin10_override_mode_Type()
)
outbin10_override_mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outbin10_override_mode.setStatus("optional")
_Outbin10_maximum_binding_Type = Integer32
_Outbin10_maximum_binding_Object = MibScalar
outbin10_maximum_binding = _Outbin10_maximum_binding_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 4, 3, 10, 10),
    _Outbin10_maximum_binding_Type()
)
outbin10_maximum_binding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outbin10_maximum_binding.setStatus("optional")
_Outbin10_phd_Type = Integer32
_Outbin10_phd_Object = MibScalar
outbin10_phd = _Outbin10_phd_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 4, 3, 10, 11),
    _Outbin10_phd_Type()
)
outbin10_phd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outbin10_phd.setStatus("optional")
_Outbin10_error_info_Type = OctetString
_Outbin10_error_info_Object = MibScalar
outbin10_error_info = _Outbin10_error_info_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 4, 3, 10, 12),
    _Outbin10_error_info_Type()
)
outbin10_error_info.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outbin10_error_info.setStatus("optional")
_Outbin11_ObjectIdentity = ObjectIdentity
outbin11 = _Outbin11_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 4, 3, 11)
)
_Outbin11_override_mode_Type = OctetString
_Outbin11_override_mode_Object = MibScalar
outbin11_override_mode = _Outbin11_override_mode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 4, 3, 11, 9),
    _Outbin11_override_mode_Type()
)
outbin11_override_mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outbin11_override_mode.setStatus("optional")
_Outbin11_maximum_binding_Type = Integer32
_Outbin11_maximum_binding_Object = MibScalar
outbin11_maximum_binding = _Outbin11_maximum_binding_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 4, 3, 11, 10),
    _Outbin11_maximum_binding_Type()
)
outbin11_maximum_binding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outbin11_maximum_binding.setStatus("optional")
_Outbin11_phd_Type = Integer32
_Outbin11_phd_Object = MibScalar
outbin11_phd = _Outbin11_phd_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 4, 3, 11, 11),
    _Outbin11_phd_Type()
)
outbin11_phd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outbin11_phd.setStatus("optional")
_Outbin11_error_info_Type = OctetString
_Outbin11_error_info_Object = MibScalar
outbin11_error_info = _Outbin11_error_info_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 4, 3, 11, 12),
    _Outbin11_error_info_Type()
)
outbin11_error_info.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outbin11_error_info.setStatus("optional")
_Marking_agent_ObjectIdentity = ObjectIdentity
marking_agent = _Marking_agent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 5)
)
_Settings_marking_agent_ObjectIdentity = ObjectIdentity
settings_marking_agent = _Settings_marking_agent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 5, 1)
)


class _Low_marking_agent_processing_Type(Integer32):
    """Custom type low_marking_agent_processing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eCont", 2),
          ("eStop", 1))
    )


_Low_marking_agent_processing_Type.__name__ = "Integer32"
_Low_marking_agent_processing_Object = MibScalar
low_marking_agent_processing = _Low_marking_agent_processing_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 5, 1, 3),
    _Low_marking_agent_processing_Type()
)
low_marking_agent_processing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    low_marking_agent_processing.setStatus("optional")


class _Out_marking_agent_processing_Type(Integer32):
    """Custom type out_marking_agent_processing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eCont", 2),
          ("eStop", 1))
    )


_Out_marking_agent_processing_Type.__name__ = "Integer32"
_Out_marking_agent_processing_Object = MibScalar
out_marking_agent_processing = _Out_marking_agent_processing_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 5, 1, 10),
    _Out_marking_agent_processing_Type()
)
out_marking_agent_processing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    out_marking_agent_processing.setStatus("optional")
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
              4)
        )
    )
    namedValues = NamedValues(
        *(("eDark", 4),
          ("eLight", 2),
          ("eMedium", 3),
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


class _Default_print_quality_Type(Integer32):
    """Custom type default_print_quality based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Default_print_quality_Type.__name__ = "Integer32"
_Default_print_quality_Object = MibScalar
default_print_quality = _Default_print_quality_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 6, 7),
    _Default_print_quality_Type()
)
default_print_quality.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    default_print_quality.setStatus("optional")
_Ph_ObjectIdentity = ObjectIdentity
ph = _Ph_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 7)
)
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
_Ph3_ObjectIdentity = ObjectIdentity
ph3 = _Ph3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 7, 3, 3)
)
_Phd3_device_specific_command_Type = OctetString
_Phd3_device_specific_command_Object = MibScalar
phd3_device_specific_command = _Phd3_device_specific_command_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 7, 3, 3, 2),
    _Phd3_device_specific_command_Type()
)
phd3_device_specific_command.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    phd3_device_specific_command.setStatus("optional")
_Ph4_ObjectIdentity = ObjectIdentity
ph4 = _Ph4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 7, 3, 4)
)
_Phd4_device_specific_command_Type = OctetString
_Phd4_device_specific_command_Object = MibScalar
phd4_device_specific_command = _Phd4_device_specific_command_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 7, 3, 4, 2),
    _Phd4_device_specific_command_Type()
)
phd4_device_specific_command.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    phd4_device_specific_command.setStatus("optional")
_Ph5_ObjectIdentity = ObjectIdentity
ph5 = _Ph5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 7, 3, 5)
)
_Phd5_device_specific_command_Type = OctetString
_Phd5_device_specific_command_Object = MibScalar
phd5_device_specific_command = _Phd5_device_specific_command_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 7, 3, 5, 2),
    _Phd5_device_specific_command_Type()
)
phd5_device_specific_command.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    phd5_device_specific_command.setStatus("optional")
_Ph6_ObjectIdentity = ObjectIdentity
ph6 = _Ph6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 7, 3, 6)
)
_Phd6_device_specific_command_Type = OctetString
_Phd6_device_specific_command_Object = MibScalar
phd6_device_specific_command = _Phd6_device_specific_command_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 7, 3, 6, 2),
    _Phd6_device_specific_command_Type()
)
phd6_device_specific_command.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    phd6_device_specific_command.setStatus("optional")
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


class _Media1_name_Type(DisplayString):
    """Custom type media1_name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 24),
    )


_Media1_name_Type.__name__ = "DisplayString"
_Media1_name_Object = MibScalar
media1_name = _Media1_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 1, 1),
    _Media1_name_Type()
)
media1_name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    media1_name.setStatus("optional")


class _Media1_short_name_Type(DisplayString):
    """Custom type media1_short_name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 9),
    )


_Media1_short_name_Type.__name__ = "DisplayString"
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


class _Media2_name_Type(DisplayString):
    """Custom type media2_name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 24),
    )


_Media2_name_Type.__name__ = "DisplayString"
_Media2_name_Object = MibScalar
media2_name = _Media2_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 2, 1),
    _Media2_name_Type()
)
media2_name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    media2_name.setStatus("optional")


class _Media2_short_name_Type(DisplayString):
    """Custom type media2_short_name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 9),
    )


_Media2_short_name_Type.__name__ = "DisplayString"
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


class _Media3_name_Type(DisplayString):
    """Custom type media3_name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 24),
    )


_Media3_name_Type.__name__ = "DisplayString"
_Media3_name_Object = MibScalar
media3_name = _Media3_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 3, 1),
    _Media3_name_Type()
)
media3_name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    media3_name.setStatus("optional")


class _Media3_short_name_Type(DisplayString):
    """Custom type media3_short_name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 9),
    )


_Media3_short_name_Type.__name__ = "DisplayString"
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


class _Media4_name_Type(DisplayString):
    """Custom type media4_name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 24),
    )


_Media4_name_Type.__name__ = "DisplayString"
_Media4_name_Object = MibScalar
media4_name = _Media4_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 4, 1),
    _Media4_name_Type()
)
media4_name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    media4_name.setStatus("optional")


class _Media4_short_name_Type(DisplayString):
    """Custom type media4_short_name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 9),
    )


_Media4_short_name_Type.__name__ = "DisplayString"
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


class _Media5_name_Type(DisplayString):
    """Custom type media5_name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 24),
    )


_Media5_name_Type.__name__ = "DisplayString"
_Media5_name_Object = MibScalar
media5_name = _Media5_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 5, 1),
    _Media5_name_Type()
)
media5_name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    media5_name.setStatus("optional")


class _Media5_short_name_Type(DisplayString):
    """Custom type media5_short_name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 9),
    )


_Media5_short_name_Type.__name__ = "DisplayString"
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


class _Media6_name_Type(DisplayString):
    """Custom type media6_name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 24),
    )


_Media6_name_Type.__name__ = "DisplayString"
_Media6_name_Object = MibScalar
media6_name = _Media6_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 6, 1),
    _Media6_name_Type()
)
media6_name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    media6_name.setStatus("optional")


class _Media6_short_name_Type(DisplayString):
    """Custom type media6_short_name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 9),
    )


_Media6_short_name_Type.__name__ = "DisplayString"
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


class _Media7_name_Type(DisplayString):
    """Custom type media7_name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 24),
    )


_Media7_name_Type.__name__ = "DisplayString"
_Media7_name_Object = MibScalar
media7_name = _Media7_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 7, 1),
    _Media7_name_Type()
)
media7_name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    media7_name.setStatus("optional")


class _Media7_short_name_Type(DisplayString):
    """Custom type media7_short_name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 9),
    )


_Media7_short_name_Type.__name__ = "DisplayString"
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


class _Media8_name_Type(DisplayString):
    """Custom type media8_name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 24),
    )


_Media8_name_Type.__name__ = "DisplayString"
_Media8_name_Object = MibScalar
media8_name = _Media8_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 8, 1),
    _Media8_name_Type()
)
media8_name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    media8_name.setStatus("optional")


class _Media8_short_name_Type(DisplayString):
    """Custom type media8_short_name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 9),
    )


_Media8_short_name_Type.__name__ = "DisplayString"
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


class _Media9_name_Type(DisplayString):
    """Custom type media9_name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 24),
    )


_Media9_name_Type.__name__ = "DisplayString"
_Media9_name_Object = MibScalar
media9_name = _Media9_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 9, 1),
    _Media9_name_Type()
)
media9_name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    media9_name.setStatus("optional")


class _Media9_short_name_Type(DisplayString):
    """Custom type media9_short_name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 9),
    )


_Media9_short_name_Type.__name__ = "DisplayString"
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


class _Media10_name_Type(DisplayString):
    """Custom type media10_name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 24),
    )


_Media10_name_Type.__name__ = "DisplayString"
_Media10_name_Object = MibScalar
media10_name = _Media10_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 10, 1),
    _Media10_name_Type()
)
media10_name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    media10_name.setStatus("optional")


class _Media10_short_name_Type(DisplayString):
    """Custom type media10_short_name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 9),
    )


_Media10_short_name_Type.__name__ = "DisplayString"
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


class _Media11_name_Type(DisplayString):
    """Custom type media11_name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 24),
    )


_Media11_name_Type.__name__ = "DisplayString"
_Media11_name_Object = MibScalar
media11_name = _Media11_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 11, 1),
    _Media11_name_Type()
)
media11_name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    media11_name.setStatus("optional")


class _Media11_short_name_Type(DisplayString):
    """Custom type media11_short_name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 9),
    )


_Media11_short_name_Type.__name__ = "DisplayString"
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
_Media11_engine_media_mode_Type = Integer32
_Media11_engine_media_mode_Object = MibScalar
media11_engine_media_mode = _Media11_engine_media_mode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 11, 4),
    _Media11_engine_media_mode_Type()
)
media11_engine_media_mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    media11_engine_media_mode.setStatus("optional")
_Media13_ObjectIdentity = ObjectIdentity
media13 = _Media13_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 13)
)
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


class _Media15_name_Type(DisplayString):
    """Custom type media15_name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 24),
    )


_Media15_name_Type.__name__ = "DisplayString"
_Media15_name_Object = MibScalar
media15_name = _Media15_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 15, 1),
    _Media15_name_Type()
)
media15_name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    media15_name.setStatus("optional")


class _Media15_short_name_Type(DisplayString):
    """Custom type media15_short_name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 9),
    )


_Media15_short_name_Type.__name__ = "DisplayString"
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


class _Media16_name_Type(DisplayString):
    """Custom type media16_name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 24),
    )


_Media16_name_Type.__name__ = "DisplayString"
_Media16_name_Object = MibScalar
media16_name = _Media16_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 16, 1),
    _Media16_name_Type()
)
media16_name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    media16_name.setStatus("optional")


class _Media16_short_name_Type(DisplayString):
    """Custom type media16_short_name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 9),
    )


_Media16_short_name_Type.__name__ = "DisplayString"
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


class _Media17_name_Type(DisplayString):
    """Custom type media17_name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 24),
    )


_Media17_name_Type.__name__ = "DisplayString"
_Media17_name_Object = MibScalar
media17_name = _Media17_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 17, 1),
    _Media17_name_Type()
)
media17_name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    media17_name.setStatus("optional")


class _Media17_short_name_Type(DisplayString):
    """Custom type media17_short_name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 9),
    )


_Media17_short_name_Type.__name__ = "DisplayString"
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


class _Media18_name_Type(DisplayString):
    """Custom type media18_name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 24),
    )


_Media18_name_Type.__name__ = "DisplayString"
_Media18_name_Object = MibScalar
media18_name = _Media18_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 18, 1),
    _Media18_name_Type()
)
media18_name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    media18_name.setStatus("optional")


class _Media18_short_name_Type(DisplayString):
    """Custom type media18_short_name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 9),
    )


_Media18_short_name_Type.__name__ = "DisplayString"
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


class _Media19_name_Type(DisplayString):
    """Custom type media19_name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 24),
    )


_Media19_name_Type.__name__ = "DisplayString"
_Media19_name_Object = MibScalar
media19_name = _Media19_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 19, 1),
    _Media19_name_Type()
)
media19_name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    media19_name.setStatus("optional")


class _Media19_short_name_Type(DisplayString):
    """Custom type media19_short_name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 9),
    )


_Media19_short_name_Type.__name__ = "DisplayString"
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
_Media_modes_ObjectIdentity = ObjectIdentity
media_modes = _Media_modes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 4)
)
_Engine_media_modes_supported1_Type = DisplayString
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


class _Consumable_status_cartridge_model_Type(DisplayString):
    """Custom type consumable_status_cartridge_model based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_Consumable_status_cartridge_model_Type.__name__ = "DisplayString"
_Consumable_status_cartridge_model_Object = MibScalar
consumable_status_cartridge_model = _Consumable_status_cartridge_model_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 10, 1, 1, 1),
    _Consumable_status_cartridge_model_Type()
)
consumable_status_cartridge_model.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    consumable_status_cartridge_model.setStatus("optional")


class _Consumable_status_manufacturing_date_Type(DisplayString):
    """Custom type consumable_status_manufacturing_date based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_Consumable_status_manufacturing_date_Type.__name__ = "DisplayString"
_Consumable_status_manufacturing_date_Object = MibScalar
consumable_status_manufacturing_date = _Consumable_status_manufacturing_date_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 10, 1, 1, 2),
    _Consumable_status_manufacturing_date_Type()
)
consumable_status_manufacturing_date.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    consumable_status_manufacturing_date.setStatus("optional")


class _Consumable_status_serial_number_Type(DisplayString):
    """Custom type consumable_status_serial_number based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_Consumable_status_serial_number_Type.__name__ = "DisplayString"
_Consumable_status_serial_number_Object = MibScalar
consumable_status_serial_number = _Consumable_status_serial_number_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 10, 1, 1, 3),
    _Consumable_status_serial_number_Type()
)
consumable_status_serial_number.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    consumable_status_serial_number.setStatus("optional")


class _Consumable_status_capacity_units_Type(Integer32):
    """Custom type consumable_status_capacity_units based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("e10KPagesAt5PercentCoverage", 3),
          ("e1KPagesAt5PercentCoverage", 2),
          ("ePagesAt5PercentCoverage", 1))
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


class _Consumable_status_reseller_id_Type(Integer32):
    """Custom type consumable_status_reseller_id based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Consumable_status_reseller_id_Type.__name__ = "Integer32"
_Consumable_status_reseller_id_Object = MibScalar
consumable_status_reseller_id = _Consumable_status_reseller_id_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 10, 1, 1, 6),
    _Consumable_status_reseller_id_Type()
)
consumable_status_reseller_id.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    consumable_status_reseller_id.setStatus("optional")
_Consumable_status_info_Type = OctetString
_Consumable_status_info_Object = MibScalar
consumable_status_info = _Consumable_status_info_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 10, 1, 1, 7),
    _Consumable_status_info_Type()
)
consumable_status_info.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    consumable_status_info.setStatus("optional")


class _Consumable_status_first_install_date_Type(DisplayString):
    """Custom type consumable_status_first_install_date based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_Consumable_status_first_install_date_Type.__name__ = "DisplayString"
_Consumable_status_first_install_date_Object = MibScalar
consumable_status_first_install_date = _Consumable_status_first_install_date_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 10, 1, 1, 8),
    _Consumable_status_first_install_date_Type()
)
consumable_status_first_install_date.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    consumable_status_first_install_date.setStatus("optional")


class _Consumable_status_last_use_date_Type(DisplayString):
    """Custom type consumable_status_last_use_date based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_Consumable_status_last_use_date_Type.__name__ = "DisplayString"
_Consumable_status_last_use_date_Object = MibScalar
consumable_status_last_use_date = _Consumable_status_last_use_date_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 10, 1, 1, 9),
    _Consumable_status_last_use_date_Type()
)
consumable_status_last_use_date.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    consumable_status_last_use_date.setStatus("optional")


class _Consumable_status_page_count_a3_ledger_Type(Integer32):
    """Custom type consumable_status_page_count_a3_ledger based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Consumable_status_page_count_a3_ledger_Type.__name__ = "Integer32"
_Consumable_status_page_count_a3_ledger_Object = MibScalar
consumable_status_page_count_a3_ledger = _Consumable_status_page_count_a3_ledger_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 10, 1, 1, 10),
    _Consumable_status_page_count_a3_ledger_Type()
)
consumable_status_page_count_a3_ledger.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    consumable_status_page_count_a3_ledger.setStatus("optional")


class _Consumable_status_page_count_legal_Type(Integer32):
    """Custom type consumable_status_page_count_legal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Consumable_status_page_count_legal_Type.__name__ = "Integer32"
_Consumable_status_page_count_legal_Object = MibScalar
consumable_status_page_count_legal = _Consumable_status_page_count_legal_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 10, 1, 1, 11),
    _Consumable_status_page_count_legal_Type()
)
consumable_status_page_count_legal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    consumable_status_page_count_legal.setStatus("optional")


class _Consumable_status_page_count_a4_letter_Type(Integer32):
    """Custom type consumable_status_page_count_a4_letter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Consumable_status_page_count_a4_letter_Type.__name__ = "Integer32"
_Consumable_status_page_count_a4_letter_Object = MibScalar
consumable_status_page_count_a4_letter = _Consumable_status_page_count_a4_letter_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 10, 1, 1, 12),
    _Consumable_status_page_count_a4_letter_Type()
)
consumable_status_page_count_a4_letter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    consumable_status_page_count_a4_letter.setStatus("optional")


class _Consumable_status_page_count_b5_executive_Type(Integer32):
    """Custom type consumable_status_page_count_b5_executive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Consumable_status_page_count_b5_executive_Type.__name__ = "Integer32"
_Consumable_status_page_count_b5_executive_Object = MibScalar
consumable_status_page_count_b5_executive = _Consumable_status_page_count_b5_executive_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 10, 1, 1, 13),
    _Consumable_status_page_count_b5_executive_Type()
)
consumable_status_page_count_b5_executive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    consumable_status_page_count_b5_executive.setStatus("optional")


class _Consumable_status_page_count_envelope_Type(Integer32):
    """Custom type consumable_status_page_count_envelope based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Consumable_status_page_count_envelope_Type.__name__ = "Integer32"
_Consumable_status_page_count_envelope_Object = MibScalar
consumable_status_page_count_envelope = _Consumable_status_page_count_envelope_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 10, 1, 1, 14),
    _Consumable_status_page_count_envelope_Type()
)
consumable_status_page_count_envelope.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    consumable_status_page_count_envelope.setStatus("optional")


class _Consumable_status_page_count_xy_other_Type(Integer32):
    """Custom type consumable_status_page_count_xy_other based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Consumable_status_page_count_xy_other_Type.__name__ = "Integer32"
_Consumable_status_page_count_xy_other_Object = MibScalar
consumable_status_page_count_xy_other = _Consumable_status_page_count_xy_other_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 10, 1, 1, 15),
    _Consumable_status_page_count_xy_other_Type()
)
consumable_status_page_count_xy_other.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    consumable_status_page_count_xy_other.setStatus("optional")


class _Consumable_status_job_count_Type(Integer32):
    """Custom type consumable_status_job_count based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Consumable_status_job_count_Type.__name__ = "Integer32"
_Consumable_status_job_count_Object = MibScalar
consumable_status_job_count = _Consumable_status_job_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 10, 1, 1, 16),
    _Consumable_status_job_count_Type()
)
consumable_status_job_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    consumable_status_job_count.setStatus("optional")


class _Consumable_status_usage_units_Type(Integer32):
    """Custom type consumable_status_usage_units based on Integer32"""
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
        *(("eGrams", 3),
          ("eImpressions", 6),
          ("eOther", 8),
          ("ePages", 5),
          ("ePercentLifeRemaining", 7),
          ("ePixels", 1),
          ("eRotations", 4),
          ("eTenthsOfGrams", 2))
    )


_Consumable_status_usage_units_Type.__name__ = "Integer32"
_Consumable_status_usage_units_Object = MibScalar
consumable_status_usage_units = _Consumable_status_usage_units_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 10, 1, 1, 17),
    _Consumable_status_usage_units_Type()
)
consumable_status_usage_units.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    consumable_status_usage_units.setStatus("optional")


class _Consumable_status_usage_count_Type(Integer32):
    """Custom type consumable_status_usage_count based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Consumable_status_usage_count_Type.__name__ = "Integer32"
_Consumable_status_usage_count_Object = MibScalar
consumable_status_usage_count = _Consumable_status_usage_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 10, 1, 1, 18),
    _Consumable_status_usage_count_Type()
)
consumable_status_usage_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    consumable_status_usage_count.setStatus("optional")


class _Consumable_status_manufacturer_name_Type(DisplayString):
    """Custom type consumable_status_manufacturer_name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_Consumable_status_manufacturer_name_Type.__name__ = "DisplayString"
_Consumable_status_manufacturer_name_Object = MibScalar
consumable_status_manufacturer_name = _Consumable_status_manufacturer_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 10, 1, 1, 19),
    _Consumable_status_manufacturer_name_Type()
)
consumable_status_manufacturer_name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    consumable_status_manufacturer_name.setStatus("optional")


class _Consumable_status_oem_name_Type(DisplayString):
    """Custom type consumable_status_oem_name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_Consumable_status_oem_name_Type.__name__ = "DisplayString"
_Consumable_status_oem_name_Object = MibScalar
consumable_status_oem_name = _Consumable_status_oem_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 10, 1, 1, 20),
    _Consumable_status_oem_name_Type()
)
consumable_status_oem_name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    consumable_status_oem_name.setStatus("optional")


class _Consumable_reorder_url_Type(DisplayString):
    """Custom type consumable_reorder_url based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Consumable_reorder_url_Type.__name__ = "DisplayString"
_Consumable_reorder_url_Object = MibScalar
consumable_reorder_url = _Consumable_reorder_url_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 10, 2),
    _Consumable_reorder_url_Type()
)
consumable_reorder_url.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    consumable_reorder_url.setStatus("optional")
_Consumable_maintenance_interval_Type = Integer32
_Consumable_maintenance_interval_Object = MibScalar
consumable_maintenance_interval = _Consumable_maintenance_interval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 10, 3),
    _Consumable_maintenance_interval_Type()
)
consumable_maintenance_interval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    consumable_maintenance_interval.setStatus("optional")
_Consumable_maintenance_pages_remaining_Type = Integer32
_Consumable_maintenance_pages_remaining_Object = MibScalar
consumable_maintenance_pages_remaining = _Consumable_maintenance_pages_remaining_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 10, 4),
    _Consumable_maintenance_pages_remaining_Type()
)
consumable_maintenance_pages_remaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    consumable_maintenance_pages_remaining.setStatus("optional")
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
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("eEstimatedPagesRemaining", 2),
          ("ePagesRemaining", 1),
          ("eUnknownUnits", 3))
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
_Consumables_test_ObjectIdentity = ObjectIdentity
consumables_test = _Consumables_test_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 10, 6)
)
_Consumable_test_password_Type = Integer32
_Consumable_test_password_Object = MibScalar
consumable_test_password = _Consumable_test_password_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 10, 6, 1),
    _Consumable_test_password_Type()
)
consumable_test_password.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    consumable_test_password.setStatus("optional")
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
              25,
              26,
              45)
        )
    )
    namedValues = NamedValues(
        *(("eISOandJISA4", 26),
          ("eISOandJISA5", 25),
          ("eJISB5", 45),
          ("eUSExecutive", 1),
          ("eUSLegal", 3),
          ("eUSLetter", 2))
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("eAutoSelect", 1),
          ("eEnvelopeFeeder", 6),
          ("eLowerCassette", 5),
          ("eMPTray", 3),
          ("eThirdCassette", 7),
          ("eTray4", 8),
          ("eTray5", 9),
          ("eTray6", 10),
          ("eTray7", 11),
          ("eTray8", 12),
          ("eTray9", 13),
          ("eUpperCassette", 4))
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
            1
        )
    )
    namedValues = NamedValues(
        ("eOutFaceDown", 1)
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


class _Default_copy_reset_timeout_Type(Integer32):
    """Custom type default_copy_reset_timeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300000),
    )


_Default_copy_reset_timeout_Type.__name__ = "Integer32"
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


class _Default_copier_contrast_Type(Integer32):
    """Custom type default_copier_contrast based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_Default_copier_contrast_Type.__name__ = "Integer32"
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
              3)
        )
    )
    namedValues = NamedValues(
        *(("eClip", 3),
          ("eNone", 1))
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


class _Copy_job_hold_time_Type(Integer32):
    """Custom type copy_job_hold_time based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300000),
    )


_Copy_job_hold_time_Type.__name__ = "Integer32"
_Copy_job_hold_time_Object = MibScalar
copy_job_hold_time = _Copy_job_hold_time_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 5, 1, 43),
    _Copy_job_hold_time_Type()
)
copy_job_hold_time.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    copy_job_hold_time.setStatus("optional")
_Channel_ObjectIdentity = ObjectIdentity
channel = _Channel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 6)
)
_Channelnumberofchannels_Type = Integer32
_Channelnumberofchannels_Object = MibScalar
channelnumberofchannels = _Channelnumberofchannels_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 6, 1),
    _Channelnumberofchannels_Type()
)
channelnumberofchannels.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    channelnumberofchannels.setStatus("optional")
_Channelprinteralert_Type = OctetString
_Channelprinteralert_Object = MibScalar
channelprinteralert = _Channelprinteralert_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 6, 2),
    _Channelprinteralert_Type()
)
channelprinteralert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelprinteralert.setStatus("optional")
_ChannelTable_ObjectIdentity = ObjectIdentity
channelTable = _ChannelTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 6, 3)
)
_ChannelEntry_ObjectIdentity = ObjectIdentity
channelEntry = _ChannelEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 6, 3, 1)
)


class _Channeltype_Type(Integer32):
    """Custom type channeltype based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              7,
              8,
              9,
              10,
              11,
              15,
              38)
        )
    )
    namedValues = NamedValues(
        *(("eChAppleTalkPAP", 7),
          ("eChBidirPortTCP", 38),
          ("eChDLCLLCPort", 15),
          ("eChLPDServer", 8),
          ("eChNetwarePServer", 10),
          ("eChNetwareRPrinter", 9),
          ("eChOther", 1),
          ("eChPort9100", 11))
    )


_Channeltype_Type.__name__ = "Integer32"
_Channeltype_Object = MibScalar
channeltype = _Channeltype_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 6, 3, 1, 2),
    _Channeltype_Type()
)
channeltype.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    channeltype.setStatus("optional")
_Channelprotocolversion_Type = OctetString
_Channelprotocolversion_Object = MibScalar
channelprotocolversion = _Channelprotocolversion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 6, 3, 1, 3),
    _Channelprotocolversion_Type()
)
channelprotocolversion.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    channelprotocolversion.setStatus("optional")


class _Channelstate_Type(Integer32):
    """Custom type channelstate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("eChNoDataAccepted", 4),
          ("eChOther", 1),
          ("eChPrintDataAccecped", 3))
    )


_Channelstate_Type.__name__ = "Integer32"
_Channelstate_Object = MibScalar
channelstate = _Channelstate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 6, 3, 1, 4),
    _Channelstate_Type()
)
channelstate.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    channelstate.setStatus("optional")
_Channelifindex_Type = Integer32
_Channelifindex_Object = MibScalar
channelifindex = _Channelifindex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 6, 3, 1, 5),
    _Channelifindex_Type()
)
channelifindex.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    channelifindex.setStatus("optional")
_Channelstatus_Type = Integer32
_Channelstatus_Object = MibScalar
channelstatus = _Channelstatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 6, 3, 1, 6),
    _Channelstatus_Type()
)
channelstatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    channelstatus.setStatus("optional")
_Channelinformation_Type = OctetString
_Channelinformation_Object = MibScalar
channelinformation = _Channelinformation_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 6, 3, 1, 7),
    _Channelinformation_Type()
)
channelinformation.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    channelinformation.setStatus("optional")
_Tables_ObjectIdentity = ObjectIdentity
tables = _Tables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 7)
)
_Channel_table_ObjectIdentity = ObjectIdentity
channel_table = _Channel_table_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 7, 2)
)
_Channel_entry_ObjectIdentity = ObjectIdentity
channel_entry = _Channel_entry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 7, 2, 1)
)
_Channel_bytes_sent_Type = Integer32
_Channel_bytes_sent_Object = MibScalar
channel_bytes_sent = _Channel_bytes_sent_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 7, 2, 1, 2),
    _Channel_bytes_sent_Type()
)
channel_bytes_sent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channel_bytes_sent.setStatus("optional")
_Channel_bytes_received_Type = Integer32
_Channel_bytes_received_Object = MibScalar
channel_bytes_received = _Channel_bytes_received_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 7, 2, 1, 3),
    _Channel_bytes_received_Type()
)
channel_bytes_received.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channel_bytes_received.setStatus("optional")
_Channel_io_errors_Type = Integer32
_Channel_io_errors_Object = MibScalar
channel_io_errors = _Channel_io_errors_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 7, 2, 1, 4),
    _Channel_io_errors_Type()
)
channel_io_errors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channel_io_errors.setStatus("optional")
_Channel_jobs_received_Type = Integer32
_Channel_jobs_received_Object = MibScalar
channel_jobs_received = _Channel_jobs_received_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 7, 2, 1, 5),
    _Channel_jobs_received_Type()
)
channel_jobs_received.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channel_jobs_received.setStatus("optional")
_Channel_mio_Type = Integer32
_Channel_mio_Object = MibScalar
channel_mio = _Channel_mio_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 7, 2, 1, 6),
    _Channel_mio_Type()
)
channel_mio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channel_mio.setStatus("optional")
_Printmib_ObjectIdentity = ObjectIdentity
printmib = _Printmib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2)
)
_PrtGeneral_ObjectIdentity = ObjectIdentity
prtGeneral = _PrtGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 5)
)
_PrtGeneralTable_ObjectIdentity = ObjectIdentity
prtGeneralTable = _PrtGeneralTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 5, 1)
)
_PrtGeneralEntry_ObjectIdentity = ObjectIdentity
prtGeneralEntry = _PrtGeneralEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 5, 1, 1)
)


class _Prtgeneralconfigchanges_Type(Integer32):
    """Custom type prtgeneralconfigchanges based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483648),
    )


_Prtgeneralconfigchanges_Type.__name__ = "Integer32"
_Prtgeneralconfigchanges_Object = MibScalar
prtgeneralconfigchanges = _Prtgeneralconfigchanges_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 5, 1, 1, 1),
    _Prtgeneralconfigchanges_Type()
)
prtgeneralconfigchanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtgeneralconfigchanges.setStatus("optional")


class _Prtgeneralcurrentlocalization_Type(Integer32):
    """Custom type prtgeneralcurrentlocalization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_Prtgeneralcurrentlocalization_Type.__name__ = "Integer32"
_Prtgeneralcurrentlocalization_Object = MibScalar
prtgeneralcurrentlocalization = _Prtgeneralcurrentlocalization_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 5, 1, 1, 2),
    _Prtgeneralcurrentlocalization_Type()
)
prtgeneralcurrentlocalization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtgeneralcurrentlocalization.setStatus("optional")


class _Prtgeneralreset_Type(Integer32):
    """Custom type prtgeneralreset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("ePnotResetting", 3),
          ("ePpowerCycleReset", 4),
          ("ePresetToFactoryDefaults", 6),
          ("ePresetToNVRAM", 5))
    )


_Prtgeneralreset_Type.__name__ = "Integer32"
_Prtgeneralreset_Object = MibScalar
prtgeneralreset = _Prtgeneralreset_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 5, 1, 1, 3),
    _Prtgeneralreset_Type()
)
prtgeneralreset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtgeneralreset.setStatus("optional")


class _Prtgeneralcurrentoperator_Type(OctetString):
    """Custom type prtgeneralcurrentoperator based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Prtgeneralcurrentoperator_Type.__name__ = "OctetString"
_Prtgeneralcurrentoperator_Object = MibScalar
prtgeneralcurrentoperator = _Prtgeneralcurrentoperator_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 5, 1, 1, 4),
    _Prtgeneralcurrentoperator_Type()
)
prtgeneralcurrentoperator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtgeneralcurrentoperator.setStatus("optional")


class _Prtgeneralserviceperson_Type(OctetString):
    """Custom type prtgeneralserviceperson based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Prtgeneralserviceperson_Type.__name__ = "OctetString"
_Prtgeneralserviceperson_Object = MibScalar
prtgeneralserviceperson = _Prtgeneralserviceperson_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 5, 1, 1, 5),
    _Prtgeneralserviceperson_Type()
)
prtgeneralserviceperson.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtgeneralserviceperson.setStatus("optional")
_Prtinputdefaultindex_Type = Integer32
_Prtinputdefaultindex_Object = MibScalar
prtinputdefaultindex = _Prtinputdefaultindex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 5, 1, 1, 6),
    _Prtinputdefaultindex_Type()
)
prtinputdefaultindex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtinputdefaultindex.setStatus("optional")
_Prtoutputdefaultindex_Type = Integer32
_Prtoutputdefaultindex_Object = MibScalar
prtoutputdefaultindex = _Prtoutputdefaultindex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 5, 1, 1, 7),
    _Prtoutputdefaultindex_Type()
)
prtoutputdefaultindex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtoutputdefaultindex.setStatus("optional")


class _Prtmarkerdefaultindex_Type(Integer32):
    """Custom type prtmarkerdefaultindex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Prtmarkerdefaultindex_Type.__name__ = "Integer32"
_Prtmarkerdefaultindex_Object = MibScalar
prtmarkerdefaultindex = _Prtmarkerdefaultindex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 5, 1, 1, 8),
    _Prtmarkerdefaultindex_Type()
)
prtmarkerdefaultindex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtmarkerdefaultindex.setStatus("optional")


class _Prtmediapathdefaultindex_Type(Integer32):
    """Custom type prtmediapathdefaultindex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_Prtmediapathdefaultindex_Type.__name__ = "Integer32"
_Prtmediapathdefaultindex_Object = MibScalar
prtmediapathdefaultindex = _Prtmediapathdefaultindex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 5, 1, 1, 9),
    _Prtmediapathdefaultindex_Type()
)
prtmediapathdefaultindex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtmediapathdefaultindex.setStatus("optional")


class _Prtconsolelocalization_Type(Integer32):
    """Custom type prtconsolelocalization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_Prtconsolelocalization_Type.__name__ = "Integer32"
_Prtconsolelocalization_Object = MibScalar
prtconsolelocalization = _Prtconsolelocalization_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 5, 1, 1, 10),
    _Prtconsolelocalization_Type()
)
prtconsolelocalization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtconsolelocalization.setStatus("optional")


class _Prtconsolenumberofdisplaylines_Type(Integer32):
    """Custom type prtconsolenumberofdisplaylines based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Prtconsolenumberofdisplaylines_Type.__name__ = "Integer32"
_Prtconsolenumberofdisplaylines_Object = MibScalar
prtconsolenumberofdisplaylines = _Prtconsolenumberofdisplaylines_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 5, 1, 1, 11),
    _Prtconsolenumberofdisplaylines_Type()
)
prtconsolenumberofdisplaylines.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtconsolenumberofdisplaylines.setStatus("optional")


class _Prtconsolenumberofdisplaychars_Type(Integer32):
    """Custom type prtconsolenumberofdisplaychars based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Prtconsolenumberofdisplaychars_Type.__name__ = "Integer32"
_Prtconsolenumberofdisplaychars_Object = MibScalar
prtconsolenumberofdisplaychars = _Prtconsolenumberofdisplaychars_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 5, 1, 1, 12),
    _Prtconsolenumberofdisplaychars_Type()
)
prtconsolenumberofdisplaychars.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtconsolenumberofdisplaychars.setStatus("optional")


class _Prtconsoledisable_Type(Integer32):
    """Custom type prtconsoledisable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("ePoperatorConsoleDisabled", 4),
          ("ePoperatorConsoleEnabled", 3),
          ("ePoperatorConsoleEnabledLevel1", 5),
          ("ePoperatorConsoleEnabledLevel2", 6))
    )


_Prtconsoledisable_Type.__name__ = "Integer32"
_Prtconsoledisable_Object = MibScalar
prtconsoledisable = _Prtconsoledisable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 5, 1, 1, 13),
    _Prtconsoledisable_Type()
)
prtconsoledisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtconsoledisable.setStatus("optional")


class _Prtgeneralstartuppage_Type(Integer32):
    """Custom type prtgeneralstartuppage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            5
        )
    )
    namedValues = NamedValues(
        ("ePnotPresent", 5)
    )


_Prtgeneralstartuppage_Type.__name__ = "Integer32"
_Prtgeneralstartuppage_Object = MibScalar
prtgeneralstartuppage = _Prtgeneralstartuppage_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 5, 1, 1, 14),
    _Prtgeneralstartuppage_Type()
)
prtgeneralstartuppage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtgeneralstartuppage.setStatus("optional")


class _Prtgeneralbannerpage_Type(Integer32):
    """Custom type prtgeneralbannerpage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            5
        )
    )
    namedValues = NamedValues(
        ("ePnotPresent", 5)
    )


_Prtgeneralbannerpage_Type.__name__ = "Integer32"
_Prtgeneralbannerpage_Object = MibScalar
prtgeneralbannerpage = _Prtgeneralbannerpage_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 5, 1, 1, 15),
    _Prtgeneralbannerpage_Type()
)
prtgeneralbannerpage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtgeneralbannerpage.setStatus("optional")


class _Prtgeneralprintername_Type(OctetString):
    """Custom type prtgeneralprintername based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Prtgeneralprintername_Type.__name__ = "OctetString"
_Prtgeneralprintername_Object = MibScalar
prtgeneralprintername = _Prtgeneralprintername_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 5, 1, 1, 16),
    _Prtgeneralprintername_Type()
)
prtgeneralprintername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtgeneralprintername.setStatus("optional")


class _Prtgeneralserialnumber_Type(OctetString):
    """Custom type prtgeneralserialnumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_Prtgeneralserialnumber_Type.__name__ = "OctetString"
_Prtgeneralserialnumber_Object = MibScalar
prtgeneralserialnumber = _Prtgeneralserialnumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 5, 1, 1, 17),
    _Prtgeneralserialnumber_Type()
)
prtgeneralserialnumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtgeneralserialnumber.setStatus("optional")
_Prtalertcriticalevents_Type = Integer32
_Prtalertcriticalevents_Object = MibScalar
prtalertcriticalevents = _Prtalertcriticalevents_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 5, 1, 1, 18),
    _Prtalertcriticalevents_Type()
)
prtalertcriticalevents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtalertcriticalevents.setStatus("optional")
_Prtalertallevents_Type = Integer32
_Prtalertallevents_Object = MibScalar
prtalertallevents = _Prtalertallevents_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 5, 1, 1, 19),
    _Prtalertallevents_Type()
)
prtalertallevents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtalertallevents.setStatus("optional")
_PrtStorageRefTable_ObjectIdentity = ObjectIdentity
prtStorageRefTable = _PrtStorageRefTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 5, 2)
)
_PrtStorageRefEntry_ObjectIdentity = ObjectIdentity
prtStorageRefEntry = _PrtStorageRefEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 5, 2, 1)
)


class _Prtstoragerefindex_Type(Integer32):
    """Custom type prtstoragerefindex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Prtstoragerefindex_Type.__name__ = "Integer32"
_Prtstoragerefindex_Object = MibScalar
prtstoragerefindex = _Prtstoragerefindex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 5, 2, 1, 2),
    _Prtstoragerefindex_Type()
)
prtstoragerefindex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtstoragerefindex.setStatus("optional")
_PrtDeviceRefTable_ObjectIdentity = ObjectIdentity
prtDeviceRefTable = _PrtDeviceRefTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 5, 3)
)
_PrtDeviceRefEntry_ObjectIdentity = ObjectIdentity
prtDeviceRefEntry = _PrtDeviceRefEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 5, 3, 1)
)


class _Prtdevicerefindex_Type(Integer32):
    """Custom type prtdevicerefindex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Prtdevicerefindex_Type.__name__ = "Integer32"
_Prtdevicerefindex_Object = MibScalar
prtdevicerefindex = _Prtdevicerefindex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 5, 3, 1, 2),
    _Prtdevicerefindex_Type()
)
prtdevicerefindex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtdevicerefindex.setStatus("optional")
_PrtCover_ObjectIdentity = ObjectIdentity
prtCover = _PrtCover_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 6)
)
_PrtCoverTable_ObjectIdentity = ObjectIdentity
prtCoverTable = _PrtCoverTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 6, 1)
)
_PrtCoverEntry_ObjectIdentity = ObjectIdentity
prtCoverEntry = _PrtCoverEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 6, 1, 1)
)


class _Prtcoverdescription_Type(OctetString):
    """Custom type prtcoverdescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Prtcoverdescription_Type.__name__ = "OctetString"
_Prtcoverdescription_Object = MibScalar
prtcoverdescription = _Prtcoverdescription_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 6, 1, 1, 2),
    _Prtcoverdescription_Type()
)
prtcoverdescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtcoverdescription.setStatus("optional")


class _Prtcoverstatus_Type(Integer32):
    """Custom type prtcoverstatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("ePdoorClosed", 4),
          ("ePdoorOpen", 3))
    )


_Prtcoverstatus_Type.__name__ = "Integer32"
_Prtcoverstatus_Object = MibScalar
prtcoverstatus = _Prtcoverstatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 6, 1, 1, 3),
    _Prtcoverstatus_Type()
)
prtcoverstatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtcoverstatus.setStatus("optional")
_PrtLocalization_ObjectIdentity = ObjectIdentity
prtLocalization = _PrtLocalization_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 7)
)
_PrtLocalizationTable_ObjectIdentity = ObjectIdentity
prtLocalizationTable = _PrtLocalizationTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 7, 1)
)
_PrtLocalizationEntry_ObjectIdentity = ObjectIdentity
prtLocalizationEntry = _PrtLocalizationEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 7, 1, 1)
)


class _Prtlocalizationlanguage_Type(OctetString):
    """Custom type prtlocalizationlanguage based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )


_Prtlocalizationlanguage_Type.__name__ = "OctetString"
_Prtlocalizationlanguage_Object = MibScalar
prtlocalizationlanguage = _Prtlocalizationlanguage_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 7, 1, 1, 2),
    _Prtlocalizationlanguage_Type()
)
prtlocalizationlanguage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtlocalizationlanguage.setStatus("optional")


class _Prtlocalizationcountry_Type(OctetString):
    """Custom type prtlocalizationcountry based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )


_Prtlocalizationcountry_Type.__name__ = "OctetString"
_Prtlocalizationcountry_Object = MibScalar
prtlocalizationcountry = _Prtlocalizationcountry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 7, 1, 1, 3),
    _Prtlocalizationcountry_Type()
)
prtlocalizationcountry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtlocalizationcountry.setStatus("optional")


class _Prtlocalizationcharacterset_Type(Integer32):
    """Custom type prtlocalizationcharacterset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            2004
        )
    )
    namedValues = NamedValues(
        ("ePcsHPRoman8", 2004)
    )


_Prtlocalizationcharacterset_Type.__name__ = "Integer32"
_Prtlocalizationcharacterset_Object = MibScalar
prtlocalizationcharacterset = _Prtlocalizationcharacterset_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 7, 1, 1, 4),
    _Prtlocalizationcharacterset_Type()
)
prtlocalizationcharacterset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtlocalizationcharacterset.setStatus("optional")
_PrtInput_ObjectIdentity = ObjectIdentity
prtInput = _PrtInput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 8)
)
_PrtInputTable_ObjectIdentity = ObjectIdentity
prtInputTable = _PrtInputTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 8, 2)
)
_PrtInputEntry_ObjectIdentity = ObjectIdentity
prtInputEntry = _PrtInputEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 8, 2, 1)
)


class _Prtinputtype_Type(Integer32):
    """Custom type prtinputtype based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("ePcontinuousFanFold", 7),
          ("ePcontinuousRoll", 6),
          ("ePother", 1),
          ("ePsheetFeedAutoNonRemovableTray", 4),
          ("ePsheetFeedAutoRemovableTray", 3),
          ("ePsheetFeedManual", 5),
          ("ePunknown", 2))
    )


_Prtinputtype_Type.__name__ = "Integer32"
_Prtinputtype_Object = MibScalar
prtinputtype = _Prtinputtype_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 8, 2, 1, 2),
    _Prtinputtype_Type()
)
prtinputtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtinputtype.setStatus("optional")


class _Prtinputdimunit_Type(Integer32):
    """Custom type prtinputdimunit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("ePmicrometers", 4),
          ("ePtenThousandthsOfInches", 3))
    )


_Prtinputdimunit_Type.__name__ = "Integer32"
_Prtinputdimunit_Object = MibScalar
prtinputdimunit = _Prtinputdimunit_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 8, 2, 1, 3),
    _Prtinputdimunit_Type()
)
prtinputdimunit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtinputdimunit.setStatus("optional")
_Prtinputmediadimfeeddirdeclared_Type = Integer32
_Prtinputmediadimfeeddirdeclared_Object = MibScalar
prtinputmediadimfeeddirdeclared = _Prtinputmediadimfeeddirdeclared_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 8, 2, 1, 4),
    _Prtinputmediadimfeeddirdeclared_Type()
)
prtinputmediadimfeeddirdeclared.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtinputmediadimfeeddirdeclared.setStatus("optional")
_Prtinputmediadimxfeeddirdeclared_Type = Integer32
_Prtinputmediadimxfeeddirdeclared_Object = MibScalar
prtinputmediadimxfeeddirdeclared = _Prtinputmediadimxfeeddirdeclared_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 8, 2, 1, 5),
    _Prtinputmediadimxfeeddirdeclared_Type()
)
prtinputmediadimxfeeddirdeclared.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtinputmediadimxfeeddirdeclared.setStatus("optional")
_Prtinputmediadimfeeddirchosen_Type = Integer32
_Prtinputmediadimfeeddirchosen_Object = MibScalar
prtinputmediadimfeeddirchosen = _Prtinputmediadimfeeddirchosen_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 8, 2, 1, 6),
    _Prtinputmediadimfeeddirchosen_Type()
)
prtinputmediadimfeeddirchosen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtinputmediadimfeeddirchosen.setStatus("optional")
_Prtinputmediadimxfeeddirchosen_Type = Integer32
_Prtinputmediadimxfeeddirchosen_Object = MibScalar
prtinputmediadimxfeeddirchosen = _Prtinputmediadimxfeeddirchosen_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 8, 2, 1, 7),
    _Prtinputmediadimxfeeddirchosen_Type()
)
prtinputmediadimxfeeddirchosen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtinputmediadimxfeeddirchosen.setStatus("optional")


class _Prtinputcapacityunit_Type(Integer32):
    """Custom type prtinputcapacityunit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              8,
              16,
              17)
        )
    )
    namedValues = NamedValues(
        *(("ePfeet", 16),
          ("ePmeters", 17),
          ("ePmicrometers", 4),
          ("ePsheets", 8),
          ("ePtenThousandthsOfInches", 3))
    )


_Prtinputcapacityunit_Type.__name__ = "Integer32"
_Prtinputcapacityunit_Object = MibScalar
prtinputcapacityunit = _Prtinputcapacityunit_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 8, 2, 1, 8),
    _Prtinputcapacityunit_Type()
)
prtinputcapacityunit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtinputcapacityunit.setStatus("optional")
_Prtinputmaxcapacity_Type = Integer32
_Prtinputmaxcapacity_Object = MibScalar
prtinputmaxcapacity = _Prtinputmaxcapacity_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 8, 2, 1, 9),
    _Prtinputmaxcapacity_Type()
)
prtinputmaxcapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtinputmaxcapacity.setStatus("optional")
_Prtinputcurrentlevel_Type = Integer32
_Prtinputcurrentlevel_Object = MibScalar
prtinputcurrentlevel = _Prtinputcurrentlevel_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 8, 2, 1, 10),
    _Prtinputcurrentlevel_Type()
)
prtinputcurrentlevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtinputcurrentlevel.setStatus("optional")
_Prtinputstatus_Type = Integer32
_Prtinputstatus_Object = MibScalar
prtinputstatus = _Prtinputstatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 8, 2, 1, 11),
    _Prtinputstatus_Type()
)
prtinputstatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtinputstatus.setStatus("optional")


class _Prtinputmedianame_Type(OctetString):
    """Custom type prtinputmedianame based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_Prtinputmedianame_Type.__name__ = "OctetString"
_Prtinputmedianame_Object = MibScalar
prtinputmedianame = _Prtinputmedianame_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 8, 2, 1, 12),
    _Prtinputmedianame_Type()
)
prtinputmedianame.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtinputmedianame.setStatus("optional")


class _Prtinputname_Type(OctetString):
    """Custom type prtinputname based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_Prtinputname_Type.__name__ = "OctetString"
_Prtinputname_Object = MibScalar
prtinputname = _Prtinputname_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 8, 2, 1, 13),
    _Prtinputname_Type()
)
prtinputname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtinputname.setStatus("optional")


class _Prtinputvendorname_Type(OctetString):
    """Custom type prtinputvendorname based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_Prtinputvendorname_Type.__name__ = "OctetString"
_Prtinputvendorname_Object = MibScalar
prtinputvendorname = _Prtinputvendorname_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 8, 2, 1, 14),
    _Prtinputvendorname_Type()
)
prtinputvendorname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtinputvendorname.setStatus("optional")


class _Prtinputmodel_Type(OctetString):
    """Custom type prtinputmodel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_Prtinputmodel_Type.__name__ = "OctetString"
_Prtinputmodel_Object = MibScalar
prtinputmodel = _Prtinputmodel_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 8, 2, 1, 15),
    _Prtinputmodel_Type()
)
prtinputmodel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtinputmodel.setStatus("optional")


class _Prtinputversion_Type(OctetString):
    """Custom type prtinputversion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_Prtinputversion_Type.__name__ = "OctetString"
_Prtinputversion_Object = MibScalar
prtinputversion = _Prtinputversion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 8, 2, 1, 16),
    _Prtinputversion_Type()
)
prtinputversion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtinputversion.setStatus("optional")


class _Prtinputserialnumber_Type(OctetString):
    """Custom type prtinputserialnumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_Prtinputserialnumber_Type.__name__ = "OctetString"
_Prtinputserialnumber_Object = MibScalar
prtinputserialnumber = _Prtinputserialnumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 8, 2, 1, 17),
    _Prtinputserialnumber_Type()
)
prtinputserialnumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtinputserialnumber.setStatus("optional")


class _Prtinputdescription_Type(OctetString):
    """Custom type prtinputdescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Prtinputdescription_Type.__name__ = "OctetString"
_Prtinputdescription_Object = MibScalar
prtinputdescription = _Prtinputdescription_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 8, 2, 1, 18),
    _Prtinputdescription_Type()
)
prtinputdescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtinputdescription.setStatus("optional")


class _Prtinputsecurity_Type(Integer32):
    """Custom type prtinputsecurity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("ePnotPresent", 5),
          ("ePoff", 4),
          ("ePon", 3),
          ("ePother", 1))
    )


_Prtinputsecurity_Type.__name__ = "Integer32"
_Prtinputsecurity_Object = MibScalar
prtinputsecurity = _Prtinputsecurity_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 8, 2, 1, 19),
    _Prtinputsecurity_Type()
)
prtinputsecurity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtinputsecurity.setStatus("optional")
_Prtinputmedialoadtimeout_Type = Integer32
_Prtinputmedialoadtimeout_Object = MibScalar
prtinputmedialoadtimeout = _Prtinputmedialoadtimeout_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 8, 2, 1, 24),
    _Prtinputmedialoadtimeout_Type()
)
prtinputmedialoadtimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtinputmedialoadtimeout.setStatus("optional")
_Prtinputnextindex_Type = Integer32
_Prtinputnextindex_Object = MibScalar
prtinputnextindex = _Prtinputnextindex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 8, 2, 1, 26),
    _Prtinputnextindex_Type()
)
prtinputnextindex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtinputnextindex.setStatus("optional")
_PrtOutput_ObjectIdentity = ObjectIdentity
prtOutput = _PrtOutput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 9)
)
_PrtOutputTable_ObjectIdentity = ObjectIdentity
prtOutputTable = _PrtOutputTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 9, 2)
)
_PrtOutputEntry_ObjectIdentity = ObjectIdentity
prtOutputEntry = _PrtOutputEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 9, 2, 1)
)


class _Prtoutputtype_Type(Integer32):
    """Custom type prtoutputtype based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("ePcontinousFanFold", 7),
          ("ePcontinuousRollDevice", 5),
          ("ePmailBox", 6),
          ("ePother", 1),
          ("ePremovableBin", 3),
          ("ePunRemovableBin", 4),
          ("ePunknown", 2))
    )


_Prtoutputtype_Type.__name__ = "Integer32"
_Prtoutputtype_Object = MibScalar
prtoutputtype = _Prtoutputtype_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 9, 2, 1, 2),
    _Prtoutputtype_Type()
)
prtoutputtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtoutputtype.setStatus("optional")


class _Prtoutputcapacityunit_Type(Integer32):
    """Custom type prtoutputcapacityunit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              8,
              16,
              17)
        )
    )
    namedValues = NamedValues(
        *(("ePfeet", 16),
          ("ePmeters", 17),
          ("ePmicrometers", 4),
          ("ePsheets", 8),
          ("ePtenThousandthsOfInches", 3))
    )


_Prtoutputcapacityunit_Type.__name__ = "Integer32"
_Prtoutputcapacityunit_Object = MibScalar
prtoutputcapacityunit = _Prtoutputcapacityunit_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 9, 2, 1, 3),
    _Prtoutputcapacityunit_Type()
)
prtoutputcapacityunit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtoutputcapacityunit.setStatus("optional")
_Prtoutputmaxcapacity_Type = Integer32
_Prtoutputmaxcapacity_Object = MibScalar
prtoutputmaxcapacity = _Prtoutputmaxcapacity_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 9, 2, 1, 4),
    _Prtoutputmaxcapacity_Type()
)
prtoutputmaxcapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtoutputmaxcapacity.setStatus("optional")
_Prtoutputremainingcapacity_Type = Integer32
_Prtoutputremainingcapacity_Object = MibScalar
prtoutputremainingcapacity = _Prtoutputremainingcapacity_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 9, 2, 1, 5),
    _Prtoutputremainingcapacity_Type()
)
prtoutputremainingcapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtoutputremainingcapacity.setStatus("optional")
_Prtoutputstatus_Type = Integer32
_Prtoutputstatus_Object = MibScalar
prtoutputstatus = _Prtoutputstatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 9, 2, 1, 6),
    _Prtoutputstatus_Type()
)
prtoutputstatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtoutputstatus.setStatus("optional")


class _Prtoutputname_Type(OctetString):
    """Custom type prtoutputname based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_Prtoutputname_Type.__name__ = "OctetString"
_Prtoutputname_Object = MibScalar
prtoutputname = _Prtoutputname_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 9, 2, 1, 7),
    _Prtoutputname_Type()
)
prtoutputname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtoutputname.setStatus("optional")


class _Prtoutputvendorname_Type(OctetString):
    """Custom type prtoutputvendorname based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_Prtoutputvendorname_Type.__name__ = "OctetString"
_Prtoutputvendorname_Object = MibScalar
prtoutputvendorname = _Prtoutputvendorname_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 9, 2, 1, 8),
    _Prtoutputvendorname_Type()
)
prtoutputvendorname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtoutputvendorname.setStatus("optional")


class _Prtoutputmodel_Type(OctetString):
    """Custom type prtoutputmodel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_Prtoutputmodel_Type.__name__ = "OctetString"
_Prtoutputmodel_Object = MibScalar
prtoutputmodel = _Prtoutputmodel_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 9, 2, 1, 9),
    _Prtoutputmodel_Type()
)
prtoutputmodel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtoutputmodel.setStatus("optional")


class _Prtoutputversion_Type(OctetString):
    """Custom type prtoutputversion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_Prtoutputversion_Type.__name__ = "OctetString"
_Prtoutputversion_Object = MibScalar
prtoutputversion = _Prtoutputversion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 9, 2, 1, 10),
    _Prtoutputversion_Type()
)
prtoutputversion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtoutputversion.setStatus("optional")


class _Prtoutputserialnumber_Type(OctetString):
    """Custom type prtoutputserialnumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_Prtoutputserialnumber_Type.__name__ = "OctetString"
_Prtoutputserialnumber_Object = MibScalar
prtoutputserialnumber = _Prtoutputserialnumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 9, 2, 1, 11),
    _Prtoutputserialnumber_Type()
)
prtoutputserialnumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtoutputserialnumber.setStatus("optional")


class _Prtoutputdescription_Type(OctetString):
    """Custom type prtoutputdescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Prtoutputdescription_Type.__name__ = "OctetString"
_Prtoutputdescription_Object = MibScalar
prtoutputdescription = _Prtoutputdescription_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 9, 2, 1, 12),
    _Prtoutputdescription_Type()
)
prtoutputdescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtoutputdescription.setStatus("optional")


class _Prtoutputsecurity_Type(Integer32):
    """Custom type prtoutputsecurity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("ePnotPresent", 5),
          ("ePoff", 4),
          ("ePon", 3),
          ("ePother", 1))
    )


_Prtoutputsecurity_Type.__name__ = "Integer32"
_Prtoutputsecurity_Object = MibScalar
prtoutputsecurity = _Prtoutputsecurity_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 9, 2, 1, 13),
    _Prtoutputsecurity_Type()
)
prtoutputsecurity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtoutputsecurity.setStatus("optional")


class _Prtoutputdimunit_Type(Integer32):
    """Custom type prtoutputdimunit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("ePmicrometers", 4),
          ("ePtenThousandthsOfInches", 3))
    )


_Prtoutputdimunit_Type.__name__ = "Integer32"
_Prtoutputdimunit_Object = MibScalar
prtoutputdimunit = _Prtoutputdimunit_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 9, 2, 1, 14),
    _Prtoutputdimunit_Type()
)
prtoutputdimunit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtoutputdimunit.setStatus("optional")
_Prtoutputmaxdimfeeddir_Type = Integer32
_Prtoutputmaxdimfeeddir_Object = MibScalar
prtoutputmaxdimfeeddir = _Prtoutputmaxdimfeeddir_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 9, 2, 1, 15),
    _Prtoutputmaxdimfeeddir_Type()
)
prtoutputmaxdimfeeddir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtoutputmaxdimfeeddir.setStatus("optional")
_Prtoutputmaxdimxfeeddir_Type = Integer32
_Prtoutputmaxdimxfeeddir_Object = MibScalar
prtoutputmaxdimxfeeddir = _Prtoutputmaxdimxfeeddir_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 9, 2, 1, 16),
    _Prtoutputmaxdimxfeeddir_Type()
)
prtoutputmaxdimxfeeddir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtoutputmaxdimxfeeddir.setStatus("optional")
_Prtoutputmindimfeeddir_Type = Integer32
_Prtoutputmindimfeeddir_Object = MibScalar
prtoutputmindimfeeddir = _Prtoutputmindimfeeddir_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 9, 2, 1, 17),
    _Prtoutputmindimfeeddir_Type()
)
prtoutputmindimfeeddir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtoutputmindimfeeddir.setStatus("optional")
_Prtoutputmindimxfeeddir_Type = Integer32
_Prtoutputmindimxfeeddir_Object = MibScalar
prtoutputmindimxfeeddir = _Prtoutputmindimxfeeddir_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 9, 2, 1, 18),
    _Prtoutputmindimxfeeddir_Type()
)
prtoutputmindimxfeeddir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtoutputmindimxfeeddir.setStatus("optional")


class _Prtoutputstackingorder_Type(Integer32):
    """Custom type prtoutputstackingorder based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("ePfirstToLast", 3),
          ("ePlastToFirst", 4),
          ("ePunknown", 2))
    )


_Prtoutputstackingorder_Type.__name__ = "Integer32"
_Prtoutputstackingorder_Object = MibScalar
prtoutputstackingorder = _Prtoutputstackingorder_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 9, 2, 1, 19),
    _Prtoutputstackingorder_Type()
)
prtoutputstackingorder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtoutputstackingorder.setStatus("optional")


class _Prtoutputpagedeliveryorientation_Type(Integer32):
    """Custom type prtoutputpagedeliveryorientation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("ePfaceDown", 4),
          ("ePfaceUp", 3))
    )


_Prtoutputpagedeliveryorientation_Type.__name__ = "Integer32"
_Prtoutputpagedeliveryorientation_Object = MibScalar
prtoutputpagedeliveryorientation = _Prtoutputpagedeliveryorientation_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 9, 2, 1, 20),
    _Prtoutputpagedeliveryorientation_Type()
)
prtoutputpagedeliveryorientation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtoutputpagedeliveryorientation.setStatus("optional")


class _Prtoutputbursting_Type(Integer32):
    """Custom type prtoutputbursting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("ePnotPresent", 5),
          ("ePoff", 4),
          ("ePon", 3),
          ("ePother", 1))
    )


_Prtoutputbursting_Type.__name__ = "Integer32"
_Prtoutputbursting_Object = MibScalar
prtoutputbursting = _Prtoutputbursting_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 9, 2, 1, 21),
    _Prtoutputbursting_Type()
)
prtoutputbursting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtoutputbursting.setStatus("optional")


class _Prtoutputdecollating_Type(Integer32):
    """Custom type prtoutputdecollating based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("ePnotPresent", 5),
          ("ePoff", 4),
          ("ePon", 3),
          ("ePother", 1))
    )


_Prtoutputdecollating_Type.__name__ = "Integer32"
_Prtoutputdecollating_Object = MibScalar
prtoutputdecollating = _Prtoutputdecollating_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 9, 2, 1, 22),
    _Prtoutputdecollating_Type()
)
prtoutputdecollating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtoutputdecollating.setStatus("optional")


class _Prtoutputpagecollated_Type(Integer32):
    """Custom type prtoutputpagecollated based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("ePnotPresent", 5),
          ("ePoff", 4),
          ("ePon", 3),
          ("ePother", 1))
    )


_Prtoutputpagecollated_Type.__name__ = "Integer32"
_Prtoutputpagecollated_Object = MibScalar
prtoutputpagecollated = _Prtoutputpagecollated_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 9, 2, 1, 23),
    _Prtoutputpagecollated_Type()
)
prtoutputpagecollated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtoutputpagecollated.setStatus("optional")


class _Prtoutputoffsetstacking_Type(Integer32):
    """Custom type prtoutputoffsetstacking based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("ePnotPresent", 5),
          ("ePoff", 4),
          ("ePon", 3),
          ("ePother", 1))
    )


_Prtoutputoffsetstacking_Type.__name__ = "Integer32"
_Prtoutputoffsetstacking_Object = MibScalar
prtoutputoffsetstacking = _Prtoutputoffsetstacking_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 9, 2, 1, 24),
    _Prtoutputoffsetstacking_Type()
)
prtoutputoffsetstacking.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtoutputoffsetstacking.setStatus("optional")
_PrtMarker_ObjectIdentity = ObjectIdentity
prtMarker = _PrtMarker_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 10)
)
_PrtMarkerTable_ObjectIdentity = ObjectIdentity
prtMarkerTable = _PrtMarkerTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 10, 2)
)
_PrtMarkerEntry_ObjectIdentity = ObjectIdentity
prtMarkerEntry = _PrtMarkerEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 10, 2, 1)
)


class _Prtmarkermarktech_Type(Integer32):
    """Custom type prtmarkermarktech based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            4
        )
    )
    namedValues = NamedValues(
        ("ePelectrophotographicLaser", 4)
    )


_Prtmarkermarktech_Type.__name__ = "Integer32"
_Prtmarkermarktech_Object = MibScalar
prtmarkermarktech = _Prtmarkermarktech_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 10, 2, 1, 2),
    _Prtmarkermarktech_Type()
)
prtmarkermarktech.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtmarkermarktech.setStatus("optional")


class _Prtmarkercounterunit_Type(Integer32):
    """Custom type prtmarkercounterunit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            7
        )
    )
    namedValues = NamedValues(
        ("ePimpressions", 7)
    )


_Prtmarkercounterunit_Type.__name__ = "Integer32"
_Prtmarkercounterunit_Object = MibScalar
prtmarkercounterunit = _Prtmarkercounterunit_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 10, 2, 1, 3),
    _Prtmarkercounterunit_Type()
)
prtmarkercounterunit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtmarkercounterunit.setStatus("optional")
_Prtmarkerlifecount_Type = Integer32
_Prtmarkerlifecount_Object = MibScalar
prtmarkerlifecount = _Prtmarkerlifecount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 10, 2, 1, 4),
    _Prtmarkerlifecount_Type()
)
prtmarkerlifecount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtmarkerlifecount.setStatus("optional")
_Prtmarkerpoweroncount_Type = Integer32
_Prtmarkerpoweroncount_Object = MibScalar
prtmarkerpoweroncount = _Prtmarkerpoweroncount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 10, 2, 1, 5),
    _Prtmarkerpoweroncount_Type()
)
prtmarkerpoweroncount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtmarkerpoweroncount.setStatus("optional")


class _Prtmarkerprocesscolorants_Type(Integer32):
    """Custom type prtmarkerprocesscolorants based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Prtmarkerprocesscolorants_Type.__name__ = "Integer32"
_Prtmarkerprocesscolorants_Object = MibScalar
prtmarkerprocesscolorants = _Prtmarkerprocesscolorants_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 10, 2, 1, 6),
    _Prtmarkerprocesscolorants_Type()
)
prtmarkerprocesscolorants.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtmarkerprocesscolorants.setStatus("optional")


class _Prtmarkerspotcolorants_Type(Integer32):
    """Custom type prtmarkerspotcolorants based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Prtmarkerspotcolorants_Type.__name__ = "Integer32"
_Prtmarkerspotcolorants_Object = MibScalar
prtmarkerspotcolorants = _Prtmarkerspotcolorants_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 10, 2, 1, 7),
    _Prtmarkerspotcolorants_Type()
)
prtmarkerspotcolorants.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtmarkerspotcolorants.setStatus("optional")


class _Prtmarkeraddressabilityunit_Type(Integer32):
    """Custom type prtmarkeraddressabilityunit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            3
        )
    )
    namedValues = NamedValues(
        ("ePtenThousandthsOfInches", 3)
    )


_Prtmarkeraddressabilityunit_Type.__name__ = "Integer32"
_Prtmarkeraddressabilityunit_Object = MibScalar
prtmarkeraddressabilityunit = _Prtmarkeraddressabilityunit_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 10, 2, 1, 8),
    _Prtmarkeraddressabilityunit_Type()
)
prtmarkeraddressabilityunit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtmarkeraddressabilityunit.setStatus("optional")
_Prtmarkeraddressabilityfeeddir_Type = Integer32
_Prtmarkeraddressabilityfeeddir_Object = MibScalar
prtmarkeraddressabilityfeeddir = _Prtmarkeraddressabilityfeeddir_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 10, 2, 1, 9),
    _Prtmarkeraddressabilityfeeddir_Type()
)
prtmarkeraddressabilityfeeddir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtmarkeraddressabilityfeeddir.setStatus("optional")
_Prtmarkeraddressabilityxfeeddir_Type = Integer32
_Prtmarkeraddressabilityxfeeddir_Object = MibScalar
prtmarkeraddressabilityxfeeddir = _Prtmarkeraddressabilityxfeeddir_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 10, 2, 1, 10),
    _Prtmarkeraddressabilityxfeeddir_Type()
)
prtmarkeraddressabilityxfeeddir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtmarkeraddressabilityxfeeddir.setStatus("optional")
_Prtmarkernorthmargin_Type = Integer32
_Prtmarkernorthmargin_Object = MibScalar
prtmarkernorthmargin = _Prtmarkernorthmargin_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 10, 2, 1, 11),
    _Prtmarkernorthmargin_Type()
)
prtmarkernorthmargin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtmarkernorthmargin.setStatus("optional")
_Prtmarkersouthmargin_Type = Integer32
_Prtmarkersouthmargin_Object = MibScalar
prtmarkersouthmargin = _Prtmarkersouthmargin_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 10, 2, 1, 12),
    _Prtmarkersouthmargin_Type()
)
prtmarkersouthmargin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtmarkersouthmargin.setStatus("optional")
_Prtmarkerwestmargin_Type = Integer32
_Prtmarkerwestmargin_Object = MibScalar
prtmarkerwestmargin = _Prtmarkerwestmargin_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 10, 2, 1, 13),
    _Prtmarkerwestmargin_Type()
)
prtmarkerwestmargin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtmarkerwestmargin.setStatus("optional")
_Prtmarkereastmargin_Type = Integer32
_Prtmarkereastmargin_Object = MibScalar
prtmarkereastmargin = _Prtmarkereastmargin_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 10, 2, 1, 14),
    _Prtmarkereastmargin_Type()
)
prtmarkereastmargin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtmarkereastmargin.setStatus("optional")
_Prtmarkerstatus_Type = Integer32
_Prtmarkerstatus_Object = MibScalar
prtmarkerstatus = _Prtmarkerstatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 10, 2, 1, 15),
    _Prtmarkerstatus_Type()
)
prtmarkerstatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtmarkerstatus.setStatus("optional")
_PrtMarkerSupplies_ObjectIdentity = ObjectIdentity
prtMarkerSupplies = _PrtMarkerSupplies_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 11)
)
_PrtMarkerSuppliesTable_ObjectIdentity = ObjectIdentity
prtMarkerSuppliesTable = _PrtMarkerSuppliesTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 11, 1)
)
_PrtMarkerSuppliesEntry_ObjectIdentity = ObjectIdentity
prtMarkerSuppliesEntry = _PrtMarkerSuppliesEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 11, 1, 1)
)


class _Prtmarkersuppliesmarkerindex_Type(Integer32):
    """Custom type prtmarkersuppliesmarkerindex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Prtmarkersuppliesmarkerindex_Type.__name__ = "Integer32"
_Prtmarkersuppliesmarkerindex_Object = MibScalar
prtmarkersuppliesmarkerindex = _Prtmarkersuppliesmarkerindex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 11, 1, 1, 2),
    _Prtmarkersuppliesmarkerindex_Type()
)
prtmarkersuppliesmarkerindex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtmarkersuppliesmarkerindex.setStatus("optional")


class _Prtmarkersuppliescolorantindex_Type(Integer32):
    """Custom type prtmarkersuppliescolorantindex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Prtmarkersuppliescolorantindex_Type.__name__ = "Integer32"
_Prtmarkersuppliescolorantindex_Object = MibScalar
prtmarkersuppliescolorantindex = _Prtmarkersuppliescolorantindex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 11, 1, 1, 3),
    _Prtmarkersuppliescolorantindex_Type()
)
prtmarkersuppliescolorantindex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtmarkersuppliescolorantindex.setStatus("optional")


class _Prtmarkersuppliesclass_Type(Integer32):
    """Custom type prtmarkersuppliesclass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            3
        )
    )
    namedValues = NamedValues(
        ("ePsupplyThatIsConsumed", 3)
    )


_Prtmarkersuppliesclass_Type.__name__ = "Integer32"
_Prtmarkersuppliesclass_Object = MibScalar
prtmarkersuppliesclass = _Prtmarkersuppliesclass_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 11, 1, 1, 4),
    _Prtmarkersuppliesclass_Type()
)
prtmarkersuppliesclass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtmarkersuppliesclass.setStatus("optional")


class _Prtmarkersuppliestype_Type(Integer32):
    """Custom type prtmarkersuppliestype based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            3
        )
    )
    namedValues = NamedValues(
        ("ePtoner", 3)
    )


_Prtmarkersuppliestype_Type.__name__ = "Integer32"
_Prtmarkersuppliestype_Object = MibScalar
prtmarkersuppliestype = _Prtmarkersuppliestype_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 11, 1, 1, 5),
    _Prtmarkersuppliestype_Type()
)
prtmarkersuppliestype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtmarkersuppliestype.setStatus("optional")


class _Prtmarkersuppliesdescription_Type(OctetString):
    """Custom type prtmarkersuppliesdescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Prtmarkersuppliesdescription_Type.__name__ = "OctetString"
_Prtmarkersuppliesdescription_Object = MibScalar
prtmarkersuppliesdescription = _Prtmarkersuppliesdescription_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 11, 1, 1, 6),
    _Prtmarkersuppliesdescription_Type()
)
prtmarkersuppliesdescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtmarkersuppliesdescription.setStatus("optional")


class _Prtmarkersuppliessupplyunit_Type(Integer32):
    """Custom type prtmarkersuppliessupplyunit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            13
        )
    )
    namedValues = NamedValues(
        ("ePtenthsOfGrams", 13)
    )


_Prtmarkersuppliessupplyunit_Type.__name__ = "Integer32"
_Prtmarkersuppliessupplyunit_Object = MibScalar
prtmarkersuppliessupplyunit = _Prtmarkersuppliessupplyunit_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 11, 1, 1, 7),
    _Prtmarkersuppliessupplyunit_Type()
)
prtmarkersuppliessupplyunit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtmarkersuppliessupplyunit.setStatus("optional")
_Prtmarkersuppliesmaxcapacity_Type = Integer32
_Prtmarkersuppliesmaxcapacity_Object = MibScalar
prtmarkersuppliesmaxcapacity = _Prtmarkersuppliesmaxcapacity_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 11, 1, 1, 8),
    _Prtmarkersuppliesmaxcapacity_Type()
)
prtmarkersuppliesmaxcapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtmarkersuppliesmaxcapacity.setStatus("optional")
_Prtmarkersupplieslevel_Type = Integer32
_Prtmarkersupplieslevel_Object = MibScalar
prtmarkersupplieslevel = _Prtmarkersupplieslevel_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 11, 1, 1, 9),
    _Prtmarkersupplieslevel_Type()
)
prtmarkersupplieslevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtmarkersupplieslevel.setStatus("optional")
_PrtMarkerColorant_ObjectIdentity = ObjectIdentity
prtMarkerColorant = _PrtMarkerColorant_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 12)
)
_PrtMarkerColorantTable_ObjectIdentity = ObjectIdentity
prtMarkerColorantTable = _PrtMarkerColorantTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 12, 1)
)
_PrtMarkerColorantEntry_ObjectIdentity = ObjectIdentity
prtMarkerColorantEntry = _PrtMarkerColorantEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 12, 1, 1)
)


class _Prtmarkercolorantmarkerindex_Type(Integer32):
    """Custom type prtmarkercolorantmarkerindex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Prtmarkercolorantmarkerindex_Type.__name__ = "Integer32"
_Prtmarkercolorantmarkerindex_Object = MibScalar
prtmarkercolorantmarkerindex = _Prtmarkercolorantmarkerindex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 12, 1, 1, 2),
    _Prtmarkercolorantmarkerindex_Type()
)
prtmarkercolorantmarkerindex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtmarkercolorantmarkerindex.setStatus("optional")


class _Prtmarkercolorantrole_Type(Integer32):
    """Custom type prtmarkercolorantrole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("ePother", 1),
          ("ePprocess", 3),
          ("ePspot", 4))
    )


_Prtmarkercolorantrole_Type.__name__ = "Integer32"
_Prtmarkercolorantrole_Object = MibScalar
prtmarkercolorantrole = _Prtmarkercolorantrole_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 12, 1, 1, 3),
    _Prtmarkercolorantrole_Type()
)
prtmarkercolorantrole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtmarkercolorantrole.setStatus("optional")


class _Prtmarkercolorantvalue_Type(OctetString):
    """Custom type prtmarkercolorantvalue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Prtmarkercolorantvalue_Type.__name__ = "OctetString"
_Prtmarkercolorantvalue_Object = MibScalar
prtmarkercolorantvalue = _Prtmarkercolorantvalue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 12, 1, 1, 4),
    _Prtmarkercolorantvalue_Type()
)
prtmarkercolorantvalue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtmarkercolorantvalue.setStatus("optional")
_Prtmarkercoloranttonality_Type = Integer32
_Prtmarkercoloranttonality_Object = MibScalar
prtmarkercoloranttonality = _Prtmarkercoloranttonality_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 12, 1, 1, 5),
    _Prtmarkercoloranttonality_Type()
)
prtmarkercoloranttonality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtmarkercoloranttonality.setStatus("optional")
_PrtMediaPath_ObjectIdentity = ObjectIdentity
prtMediaPath = _PrtMediaPath_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 13)
)
_PrtMediaPathTable_ObjectIdentity = ObjectIdentity
prtMediaPathTable = _PrtMediaPathTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 13, 4)
)
_PrtMediaPathEntry_ObjectIdentity = ObjectIdentity
prtMediaPathEntry = _PrtMediaPathEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 13, 4, 1)
)


class _Prtmediapathmaxspeedprintunit_Type(Integer32):
    """Custom type prtmediapathmaxspeedprintunit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            7
        )
    )
    namedValues = NamedValues(
        ("ePimpressionsPerHour", 7)
    )


_Prtmediapathmaxspeedprintunit_Type.__name__ = "Integer32"
_Prtmediapathmaxspeedprintunit_Object = MibScalar
prtmediapathmaxspeedprintunit = _Prtmediapathmaxspeedprintunit_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 13, 4, 1, 2),
    _Prtmediapathmaxspeedprintunit_Type()
)
prtmediapathmaxspeedprintunit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtmediapathmaxspeedprintunit.setStatus("optional")


class _Prtmediapathmediasizeunit_Type(Integer32):
    """Custom type prtmediapathmediasizeunit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("ePmicrometers", 4),
          ("ePtenThousandthsOfInches", 3))
    )


_Prtmediapathmediasizeunit_Type.__name__ = "Integer32"
_Prtmediapathmediasizeunit_Object = MibScalar
prtmediapathmediasizeunit = _Prtmediapathmediasizeunit_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 13, 4, 1, 3),
    _Prtmediapathmediasizeunit_Type()
)
prtmediapathmediasizeunit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtmediapathmediasizeunit.setStatus("optional")
_Prtmediapathmaxspeed_Type = Integer32
_Prtmediapathmaxspeed_Object = MibScalar
prtmediapathmaxspeed = _Prtmediapathmaxspeed_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 13, 4, 1, 4),
    _Prtmediapathmaxspeed_Type()
)
prtmediapathmaxspeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtmediapathmaxspeed.setStatus("optional")
_Prtmediapathmaxmediafeeddir_Type = Integer32
_Prtmediapathmaxmediafeeddir_Object = MibScalar
prtmediapathmaxmediafeeddir = _Prtmediapathmaxmediafeeddir_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 13, 4, 1, 5),
    _Prtmediapathmaxmediafeeddir_Type()
)
prtmediapathmaxmediafeeddir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtmediapathmaxmediafeeddir.setStatus("optional")
_Prtmediapathmaxmediaxfeeddir_Type = Integer32
_Prtmediapathmaxmediaxfeeddir_Object = MibScalar
prtmediapathmaxmediaxfeeddir = _Prtmediapathmaxmediaxfeeddir_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 13, 4, 1, 6),
    _Prtmediapathmaxmediaxfeeddir_Type()
)
prtmediapathmaxmediaxfeeddir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtmediapathmaxmediaxfeeddir.setStatus("optional")
_Prtmediapathminmediafeeddir_Type = Integer32
_Prtmediapathminmediafeeddir_Object = MibScalar
prtmediapathminmediafeeddir = _Prtmediapathminmediafeeddir_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 13, 4, 1, 7),
    _Prtmediapathminmediafeeddir_Type()
)
prtmediapathminmediafeeddir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtmediapathminmediafeeddir.setStatus("optional")
_Prtmediapathminmediaxfeeddir_Type = Integer32
_Prtmediapathminmediaxfeeddir_Object = MibScalar
prtmediapathminmediaxfeeddir = _Prtmediapathminmediaxfeeddir_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 13, 4, 1, 8),
    _Prtmediapathminmediaxfeeddir_Type()
)
prtmediapathminmediaxfeeddir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtmediapathminmediaxfeeddir.setStatus("optional")


class _Prtmediapathtype_Type(Integer32):
    """Custom type prtmediapathtype based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("ePlongEdgeBindingDuplex", 3),
          ("ePshortEdgeBindingDuplex", 4),
          ("ePsimplex", 5))
    )


_Prtmediapathtype_Type.__name__ = "Integer32"
_Prtmediapathtype_Object = MibScalar
prtmediapathtype = _Prtmediapathtype_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 13, 4, 1, 9),
    _Prtmediapathtype_Type()
)
prtmediapathtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtmediapathtype.setStatus("optional")


class _Prtmediapathdescription_Type(OctetString):
    """Custom type prtmediapathdescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Prtmediapathdescription_Type.__name__ = "OctetString"
_Prtmediapathdescription_Object = MibScalar
prtmediapathdescription = _Prtmediapathdescription_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 13, 4, 1, 10),
    _Prtmediapathdescription_Type()
)
prtmediapathdescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtmediapathdescription.setStatus("optional")
_Prtmediapathstatus_Type = Integer32
_Prtmediapathstatus_Object = MibScalar
prtmediapathstatus = _Prtmediapathstatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 13, 4, 1, 11),
    _Prtmediapathstatus_Type()
)
prtmediapathstatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtmediapathstatus.setStatus("optional")
_PrtChannel_ObjectIdentity = ObjectIdentity
prtChannel = _PrtChannel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 14)
)
_PrtChannelTable_ObjectIdentity = ObjectIdentity
prtChannelTable = _PrtChannelTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 14, 1)
)
_PrtChannelEntry_ObjectIdentity = ObjectIdentity
prtChannelEntry = _PrtChannelEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 14, 1, 1)
)


class _Prtchanneltype_Type(Integer32):
    """Custom type prtchanneltype based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              5,
              7,
              9,
              10,
              13,
              15,
              35,
              38,
              41)
        )
    )
    namedValues = NamedValues(
        *(("ePchAppleTalkPAP", 7),
          ("ePchBidirPortTCP", 38),
          ("ePchDLCLLCPort", 15),
          ("ePchFTP", 13),
          ("ePchIEEE1284Port", 5),
          ("ePchIRDA", 35),
          ("ePchNetwarePServer", 10),
          ("ePchNetwareRPrinter", 9),
          ("ePchPortSPX", 41),
          ("ePother", 1))
    )


_Prtchanneltype_Type.__name__ = "Integer32"
_Prtchanneltype_Object = MibScalar
prtchanneltype = _Prtchanneltype_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 14, 1, 1, 2),
    _Prtchanneltype_Type()
)
prtchanneltype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtchanneltype.setStatus("optional")


class _Prtchannelprotocolversion_Type(OctetString):
    """Custom type prtchannelprotocolversion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_Prtchannelprotocolversion_Type.__name__ = "OctetString"
_Prtchannelprotocolversion_Object = MibScalar
prtchannelprotocolversion = _Prtchannelprotocolversion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 14, 1, 1, 3),
    _Prtchannelprotocolversion_Type()
)
prtchannelprotocolversion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtchannelprotocolversion.setStatus("optional")
_Prtchannelcurrentjobcntllangindex_Type = Integer32
_Prtchannelcurrentjobcntllangindex_Object = MibScalar
prtchannelcurrentjobcntllangindex = _Prtchannelcurrentjobcntllangindex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 14, 1, 1, 4),
    _Prtchannelcurrentjobcntllangindex_Type()
)
prtchannelcurrentjobcntllangindex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtchannelcurrentjobcntllangindex.setStatus("optional")
_Prtchanneldefaultpagedesclangindex_Type = Integer32
_Prtchanneldefaultpagedesclangindex_Object = MibScalar
prtchanneldefaultpagedesclangindex = _Prtchanneldefaultpagedesclangindex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 14, 1, 1, 5),
    _Prtchanneldefaultpagedesclangindex_Type()
)
prtchanneldefaultpagedesclangindex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtchanneldefaultpagedesclangindex.setStatus("optional")


class _Prtchannelstate_Type(Integer32):
    """Custom type prtchannelstate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("ePnoDataAccepted", 4),
          ("ePother", 1),
          ("ePprintDataAccepted", 3))
    )


_Prtchannelstate_Type.__name__ = "Integer32"
_Prtchannelstate_Object = MibScalar
prtchannelstate = _Prtchannelstate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 14, 1, 1, 6),
    _Prtchannelstate_Type()
)
prtchannelstate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtchannelstate.setStatus("optional")
_Prtchannelifindex_Type = Integer32
_Prtchannelifindex_Object = MibScalar
prtchannelifindex = _Prtchannelifindex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 14, 1, 1, 7),
    _Prtchannelifindex_Type()
)
prtchannelifindex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtchannelifindex.setStatus("optional")
_Prtchannelstatus_Type = Integer32
_Prtchannelstatus_Object = MibScalar
prtchannelstatus = _Prtchannelstatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 14, 1, 1, 8),
    _Prtchannelstatus_Type()
)
prtchannelstatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtchannelstatus.setStatus("optional")


class _Prtchannelinformation_Type(OctetString):
    """Custom type prtchannelinformation based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Prtchannelinformation_Type.__name__ = "OctetString"
_Prtchannelinformation_Object = MibScalar
prtchannelinformation = _Prtchannelinformation_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 14, 1, 1, 9),
    _Prtchannelinformation_Type()
)
prtchannelinformation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtchannelinformation.setStatus("optional")
_PrtInterpreter_ObjectIdentity = ObjectIdentity
prtInterpreter = _PrtInterpreter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 15)
)
_PrtInterpreterTable_ObjectIdentity = ObjectIdentity
prtInterpreterTable = _PrtInterpreterTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 15, 1)
)
_PrtInterpreterEntry_ObjectIdentity = ObjectIdentity
prtInterpreterEntry = _PrtInterpreterEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 15, 1, 1)
)


class _Prtinterpreterlangfamily_Type(Integer32):
    """Custom type prtinterpreterlangfamily based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              5,
              6,
              37,
              47)
        )
    )
    namedValues = NamedValues(
        *(("ePlangAutomatic", 37),
          ("ePlangPCL", 3),
          ("ePlangPCLXL", 47),
          ("ePlangPJL", 5),
          ("ePlangPS", 6),
          ("ePother", 1))
    )


_Prtinterpreterlangfamily_Type.__name__ = "Integer32"
_Prtinterpreterlangfamily_Object = MibScalar
prtinterpreterlangfamily = _Prtinterpreterlangfamily_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 15, 1, 1, 2),
    _Prtinterpreterlangfamily_Type()
)
prtinterpreterlangfamily.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtinterpreterlangfamily.setStatus("optional")


class _Prtinterpreterlanglevel_Type(OctetString):
    """Custom type prtinterpreterlanglevel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_Prtinterpreterlanglevel_Type.__name__ = "OctetString"
_Prtinterpreterlanglevel_Object = MibScalar
prtinterpreterlanglevel = _Prtinterpreterlanglevel_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 15, 1, 1, 3),
    _Prtinterpreterlanglevel_Type()
)
prtinterpreterlanglevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtinterpreterlanglevel.setStatus("optional")


class _Prtinterpreterlangversion_Type(OctetString):
    """Custom type prtinterpreterlangversion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_Prtinterpreterlangversion_Type.__name__ = "OctetString"
_Prtinterpreterlangversion_Object = MibScalar
prtinterpreterlangversion = _Prtinterpreterlangversion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 15, 1, 1, 4),
    _Prtinterpreterlangversion_Type()
)
prtinterpreterlangversion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtinterpreterlangversion.setStatus("optional")


class _Prtinterpreterdescription_Type(OctetString):
    """Custom type prtinterpreterdescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Prtinterpreterdescription_Type.__name__ = "OctetString"
_Prtinterpreterdescription_Object = MibScalar
prtinterpreterdescription = _Prtinterpreterdescription_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 15, 1, 1, 5),
    _Prtinterpreterdescription_Type()
)
prtinterpreterdescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtinterpreterdescription.setStatus("optional")


class _Prtinterpreterversion_Type(OctetString):
    """Custom type prtinterpreterversion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_Prtinterpreterversion_Type.__name__ = "OctetString"
_Prtinterpreterversion_Object = MibScalar
prtinterpreterversion = _Prtinterpreterversion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 15, 1, 1, 6),
    _Prtinterpreterversion_Type()
)
prtinterpreterversion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtinterpreterversion.setStatus("optional")


class _Prtinterpreterdefaultorientation_Type(Integer32):
    """Custom type prtinterpreterdefaultorientation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("ePlandscape", 4),
          ("ePportrait", 3))
    )


_Prtinterpreterdefaultorientation_Type.__name__ = "Integer32"
_Prtinterpreterdefaultorientation_Object = MibScalar
prtinterpreterdefaultorientation = _Prtinterpreterdefaultorientation_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 15, 1, 1, 7),
    _Prtinterpreterdefaultorientation_Type()
)
prtinterpreterdefaultorientation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtinterpreterdefaultorientation.setStatus("optional")
_Prtinterpreterfeedaddressability_Type = Integer32
_Prtinterpreterfeedaddressability_Object = MibScalar
prtinterpreterfeedaddressability = _Prtinterpreterfeedaddressability_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 15, 1, 1, 8),
    _Prtinterpreterfeedaddressability_Type()
)
prtinterpreterfeedaddressability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtinterpreterfeedaddressability.setStatus("optional")
_Prtinterpreterxfeedaddressability_Type = Integer32
_Prtinterpreterxfeedaddressability_Object = MibScalar
prtinterpreterxfeedaddressability = _Prtinterpreterxfeedaddressability_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 15, 1, 1, 9),
    _Prtinterpreterxfeedaddressability_Type()
)
prtinterpreterxfeedaddressability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtinterpreterxfeedaddressability.setStatus("optional")


class _Prtinterpreterdefaultcharsetin_Type(Integer32):
    """Custom type prtinterpreterdefaultcharsetin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              5,
              12,
              13,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              1004,
              2000,
              2001,
              2002,
              2003,
              2004,
              2005,
              2009,
              2010,
              2011,
              2012,
              2014,
              2017,
              2021,
              2027,
              2087,
              2257)
        )
    )
    namedValues = NamedValues(
        *(("ePcsASCII", 3),
          ("ePcsAdobeStandardEncoding", 2005),
          ("ePcsHPDeskTop", 2021),
          ("ePcsHPLegal", 2017),
          ("ePcsHPPC8Turkish", 2014),
          ("ePcsHPRoman8", 2004),
          ("ePcsISO11SwedishforNames", 21),
          ("ePcsISO15Italian", 22),
          ("ePcsISO17Spanish", 23),
          ("ePcsISO21German", 24),
          ("ePcsISO4UnitedKingdom", 20),
          ("ePcsISO60DanishNorwegian", 25),
          ("ePcsISO69French", 26),
          ("ePcsISOLatin1", 4),
          ("ePcsISOLatin2", 5),
          ("ePcsISOLatin5", 12),
          ("ePcsISOLatin6", 13),
          ("ePcsMacintosh", 2027),
          ("ePcsPC775Baltic", 2087),
          ("ePcsPC850Multilingual", 2009),
          ("ePcsPC8CodePage437", 2011),
          ("ePcsPC8DNDanishNorwegian", 2012),
          ("ePcsPCp852", 2010),
          ("ePcsUnicodeIBM2039", 1004),
          ("ePcsWindows1257Baltic", 2257),
          ("ePcsWindows30Latin1", 2000),
          ("ePcsWindows31Latin1", 2001),
          ("ePcsWindows31Latin2", 2002),
          ("ePcsWindows31Latin5", 2003))
    )


_Prtinterpreterdefaultcharsetin_Type.__name__ = "Integer32"
_Prtinterpreterdefaultcharsetin_Object = MibScalar
prtinterpreterdefaultcharsetin = _Prtinterpreterdefaultcharsetin_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 15, 1, 1, 10),
    _Prtinterpreterdefaultcharsetin_Type()
)
prtinterpreterdefaultcharsetin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtinterpreterdefaultcharsetin.setStatus("optional")


class _Prtinterpreterdefaultcharsetout_Type(Integer32):
    """Custom type prtinterpreterdefaultcharsetout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              2004,
              2005)
        )
    )
    namedValues = NamedValues(
        *(("ePcsASCII", 3),
          ("ePcsAdobeStandardEncoding", 2005),
          ("ePcsHPRoman8", 2004),
          ("ePcsNoDefault", 2))
    )


_Prtinterpreterdefaultcharsetout_Type.__name__ = "Integer32"
_Prtinterpreterdefaultcharsetout_Object = MibScalar
prtinterpreterdefaultcharsetout = _Prtinterpreterdefaultcharsetout_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 15, 1, 1, 11),
    _Prtinterpreterdefaultcharsetout_Type()
)
prtinterpreterdefaultcharsetout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtinterpreterdefaultcharsetout.setStatus("optional")


class _Prtinterpretertwoway_Type(Integer32):
    """Custom type prtinterpretertwoway based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("ePno", 4),
          ("ePyes", 3))
    )


_Prtinterpretertwoway_Type.__name__ = "Integer32"
_Prtinterpretertwoway_Object = MibScalar
prtinterpretertwoway = _Prtinterpretertwoway_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 15, 1, 1, 12),
    _Prtinterpretertwoway_Type()
)
prtinterpretertwoway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtinterpretertwoway.setStatus("optional")
_PrtConsoleDisplayBuffer_ObjectIdentity = ObjectIdentity
prtConsoleDisplayBuffer = _PrtConsoleDisplayBuffer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 16)
)
_PrtConsoleDisplayBufferTable_ObjectIdentity = ObjectIdentity
prtConsoleDisplayBufferTable = _PrtConsoleDisplayBufferTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 16, 5)
)
_PrtConsoleDisplayBufferEntry_ObjectIdentity = ObjectIdentity
prtConsoleDisplayBufferEntry = _PrtConsoleDisplayBufferEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 16, 5, 1)
)


class _Prtconsoledisplaybuffertext_Type(OctetString):
    """Custom type prtconsoledisplaybuffertext based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Prtconsoledisplaybuffertext_Type.__name__ = "OctetString"
_Prtconsoledisplaybuffertext_Object = MibScalar
prtconsoledisplaybuffertext = _Prtconsoledisplaybuffertext_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 16, 5, 1, 2),
    _Prtconsoledisplaybuffertext_Type()
)
prtconsoledisplaybuffertext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtconsoledisplaybuffertext.setStatus("optional")
_PrtConsoleLights_ObjectIdentity = ObjectIdentity
prtConsoleLights = _PrtConsoleLights_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 17)
)
_PrtConsoleLightTable_ObjectIdentity = ObjectIdentity
prtConsoleLightTable = _PrtConsoleLightTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 17, 6)
)
_PrtConsoleLightEntry_ObjectIdentity = ObjectIdentity
prtConsoleLightEntry = _PrtConsoleLightEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 17, 6, 1)
)
_Prtconsoleontime_Type = Integer32
_Prtconsoleontime_Object = MibScalar
prtconsoleontime = _Prtconsoleontime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 17, 6, 1, 2),
    _Prtconsoleontime_Type()
)
prtconsoleontime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtconsoleontime.setStatus("optional")
_Prtconsoleofftime_Type = Integer32
_Prtconsoleofftime_Object = MibScalar
prtconsoleofftime = _Prtconsoleofftime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 17, 6, 1, 3),
    _Prtconsoleofftime_Type()
)
prtconsoleofftime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtconsoleofftime.setStatus("optional")


class _Prtconsolecolor_Type(Integer32):
    """Custom type prtconsolecolor based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("ePblue", 6),
          ("ePcyan", 7),
          ("ePgreen", 5),
          ("ePmagenta", 8),
          ("ePorange", 10),
          ("ePother", 1),
          ("ePred", 4),
          ("ePunknown", 2),
          ("ePwhite", 3),
          ("ePyellow", 9))
    )


_Prtconsolecolor_Type.__name__ = "Integer32"
_Prtconsolecolor_Object = MibScalar
prtconsolecolor = _Prtconsolecolor_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 17, 6, 1, 4),
    _Prtconsolecolor_Type()
)
prtconsolecolor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtconsolecolor.setStatus("optional")


class _Prtconsoledescription_Type(OctetString):
    """Custom type prtconsoledescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Prtconsoledescription_Type.__name__ = "OctetString"
_Prtconsoledescription_Object = MibScalar
prtconsoledescription = _Prtconsoledescription_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 17, 6, 1, 5),
    _Prtconsoledescription_Type()
)
prtconsoledescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtconsoledescription.setStatus("optional")
_PrtAlert_ObjectIdentity = ObjectIdentity
prtAlert = _PrtAlert_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 18)
)
_PrtAlertTable_ObjectIdentity = ObjectIdentity
prtAlertTable = _PrtAlertTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 18, 1)
)
_PrtAlertEntry_ObjectIdentity = ObjectIdentity
prtAlertEntry = _PrtAlertEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 18, 1, 1)
)


class _Prtalertseveritylevel_Type(Integer32):
    """Custom type prtalertseveritylevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("ePcriticalBinaryChangeEvent", 3),
          ("ePother", 1),
          ("ePwarningBinaryChangeEvent", 5),
          ("ePwarningUnaryChangeEvent", 4))
    )


_Prtalertseveritylevel_Type.__name__ = "Integer32"
_Prtalertseveritylevel_Object = MibScalar
prtalertseveritylevel = _Prtalertseveritylevel_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 18, 1, 1, 2),
    _Prtalertseveritylevel_Type()
)
prtalertseveritylevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtalertseveritylevel.setStatus("optional")


class _Prtalerttraininglevel_Type(Integer32):
    """Custom type prtalerttraininglevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("ePfieldService", 5),
          ("ePmanagement", 6),
          ("ePnoInterventionRequired", 7),
          ("ePother", 1),
          ("ePtrained", 4),
          ("ePuntrained", 3))
    )


_Prtalerttraininglevel_Type.__name__ = "Integer32"
_Prtalerttraininglevel_Object = MibScalar
prtalerttraininglevel = _Prtalerttraininglevel_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 18, 1, 1, 3),
    _Prtalerttraininglevel_Type()
)
prtalerttraininglevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtalerttraininglevel.setStatus("optional")


class _Prtalertgroup_Type(Integer32):
    """Custom type prtalertgroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              6,
              8,
              9,
              10,
              11,
              14)
        )
    )
    namedValues = NamedValues(
        *(("ePchannel", 14),
          ("ePcover", 6),
          ("ePgeneralPrinter", 5),
          ("ePinput", 8),
          ("ePmarker", 10),
          ("ePmarkerSupplies", 11),
          ("ePoutput", 9))
    )


_Prtalertgroup_Type.__name__ = "Integer32"
_Prtalertgroup_Object = MibScalar
prtalertgroup = _Prtalertgroup_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 18, 1, 1, 4),
    _Prtalertgroup_Type()
)
prtalertgroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtalertgroup.setStatus("optional")
_Prtalertgroupindex_Type = Integer32
_Prtalertgroupindex_Object = MibScalar
prtalertgroupindex = _Prtalertgroupindex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 18, 1, 1, 5),
    _Prtalertgroupindex_Type()
)
prtalertgroupindex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtalertgroupindex.setStatus("optional")
_Prtalertlocation_Type = Integer32
_Prtalertlocation_Object = MibScalar
prtalertlocation = _Prtalertlocation_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 18, 1, 1, 6),
    _Prtalertlocation_Type()
)
prtalertlocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtalertlocation.setStatus("optional")


class _Prtalertcode_Type(Integer32):
    """Custom type prtalertcode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              8,
              9,
              12,
              13,
              14,
              15,
              22,
              23,
              33,
              34,
              1001,
              1002,
              1101,
              1104)
        )
    )
    namedValues = NamedValues(
        *(("ePcoverOpened", 3),
          ("ePjam", 8),
          ("ePmarkerFuserOverTemperature", 1002),
          ("ePmarkerFuserUnderTemperature", 1001),
          ("ePmarkerTonerAlmostEmpty", 1104),
          ("ePmarkerTonerEmpty", 1101),
          ("ePother", 1),
          ("ePsubunitAlmostEmpty", 12),
          ("ePsubunitAlmostFull", 14),
          ("ePsubunitEmpty", 13),
          ("ePsubunitFull", 15),
          ("ePsubunitMemoryExhausted", 34),
          ("ePsubunitMissing", 9),
          ("ePsubunitMotorFailure", 33),
          ("ePsubunitOffline", 22),
          ("ePsubunitPowerSaver", 23))
    )


_Prtalertcode_Type.__name__ = "Integer32"
_Prtalertcode_Object = MibScalar
prtalertcode = _Prtalertcode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 18, 1, 1, 7),
    _Prtalertcode_Type()
)
prtalertcode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtalertcode.setStatus("optional")


class _Prtalertdescription_Type(OctetString):
    """Custom type prtalertdescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Prtalertdescription_Type.__name__ = "OctetString"
_Prtalertdescription_Object = MibScalar
prtalertdescription = _Prtalertdescription_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 18, 1, 1, 8),
    _Prtalertdescription_Type()
)
prtalertdescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtalertdescription.setStatus("optional")
_Prtalerttime_Type = Integer32
_Prtalerttime_Object = MibScalar
prtalerttime = _Prtalerttime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 18, 1, 1, 9),
    _Prtalerttime_Type()
)
prtalerttime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtalerttime.setStatus("optional")
_Hrm_ObjectIdentity = ObjectIdentity
hrm = _Hrm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 3)
)
_HrStorage_ObjectIdentity = ObjectIdentity
hrStorage = _HrStorage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 3, 2)
)
_Hrmemorysize_Type = Integer32
_Hrmemorysize_Object = MibScalar
hrmemorysize = _Hrmemorysize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 3, 2, 2),
    _Hrmemorysize_Type()
)
hrmemorysize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrmemorysize.setStatus("mandatory")
_HrStorageTable_ObjectIdentity = ObjectIdentity
hrStorageTable = _HrStorageTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 3, 2, 3)
)
_HrStorageEntry_ObjectIdentity = ObjectIdentity
hrStorageEntry = _HrStorageEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 3, 2, 3, 1)
)


class _Hrstorageindex_Type(Integer32):
    """Custom type hrstorageindex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hrstorageindex_Type.__name__ = "Integer32"
_Hrstorageindex_Object = MibScalar
hrstorageindex = _Hrstorageindex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 3, 2, 3, 1, 1),
    _Hrstorageindex_Type()
)
hrstorageindex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrstorageindex.setStatus("mandatory")
_Hrstoragetype_Type = ObjectIdentifier
_Hrstoragetype_Object = MibScalar
hrstoragetype = _Hrstoragetype_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 3, 2, 3, 1, 2),
    _Hrstoragetype_Type()
)
hrstoragetype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrstoragetype.setStatus("mandatory")
_Hrstoragedescr_Type = OctetString
_Hrstoragedescr_Object = MibScalar
hrstoragedescr = _Hrstoragedescr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 3, 2, 3, 1, 3),
    _Hrstoragedescr_Type()
)
hrstoragedescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrstoragedescr.setStatus("mandatory")


class _Hrstorageallocationunits_Type(Integer32):
    """Custom type hrstorageallocationunits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hrstorageallocationunits_Type.__name__ = "Integer32"
_Hrstorageallocationunits_Object = MibScalar
hrstorageallocationunits = _Hrstorageallocationunits_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 3, 2, 3, 1, 4),
    _Hrstorageallocationunits_Type()
)
hrstorageallocationunits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrstorageallocationunits.setStatus("mandatory")


class _Hrstoragesize_Type(Integer32):
    """Custom type hrstoragesize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Hrstoragesize_Type.__name__ = "Integer32"
_Hrstoragesize_Object = MibScalar
hrstoragesize = _Hrstoragesize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 3, 2, 3, 1, 5),
    _Hrstoragesize_Type()
)
hrstoragesize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrstoragesize.setStatus("mandatory")


class _Hrstorageused_Type(Integer32):
    """Custom type hrstorageused based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Hrstorageused_Type.__name__ = "Integer32"
_Hrstorageused_Object = MibScalar
hrstorageused = _Hrstorageused_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 3, 2, 3, 1, 6),
    _Hrstorageused_Type()
)
hrstorageused.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrstorageused.setStatus("mandatory")
_Hrstorageallocationfailures_Type = Integer32
_Hrstorageallocationfailures_Object = MibScalar
hrstorageallocationfailures = _Hrstorageallocationfailures_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 3, 2, 3, 1, 7),
    _Hrstorageallocationfailures_Type()
)
hrstorageallocationfailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrstorageallocationfailures.setStatus("mandatory")
_HrDevice_ObjectIdentity = ObjectIdentity
hrDevice = _HrDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 3, 3)
)
_HrDeviceTable_ObjectIdentity = ObjectIdentity
hrDeviceTable = _HrDeviceTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 3, 3, 2)
)
_HrDeviceEntry_ObjectIdentity = ObjectIdentity
hrDeviceEntry = _HrDeviceEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 3, 3, 2, 1)
)


class _Hrdeviceindex_Type(Integer32):
    """Custom type hrdeviceindex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hrdeviceindex_Type.__name__ = "Integer32"
_Hrdeviceindex_Object = MibScalar
hrdeviceindex = _Hrdeviceindex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 3, 3, 2, 1, 1),
    _Hrdeviceindex_Type()
)
hrdeviceindex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrdeviceindex.setStatus("mandatory")
_Hrdevicetype_Type = ObjectIdentifier
_Hrdevicetype_Object = MibScalar
hrdevicetype = _Hrdevicetype_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 3, 3, 2, 1, 2),
    _Hrdevicetype_Type()
)
hrdevicetype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrdevicetype.setStatus("mandatory")


class _Hrdevicedescr_Type(OctetString):
    """Custom type hrdevicedescr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Hrdevicedescr_Type.__name__ = "OctetString"
_Hrdevicedescr_Object = MibScalar
hrdevicedescr = _Hrdevicedescr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 3, 3, 2, 1, 3),
    _Hrdevicedescr_Type()
)
hrdevicedescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrdevicedescr.setStatus("mandatory")
_Hrdeviceid_Type = ObjectIdentifier
_Hrdeviceid_Object = MibScalar
hrdeviceid = _Hrdeviceid_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 3, 3, 2, 1, 4),
    _Hrdeviceid_Type()
)
hrdeviceid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrdeviceid.setStatus("mandatory")


class _Hrdevicestatus_Type(Integer32):
    """Custom type hrdevicestatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              5)
        )
    )
    namedValues = NamedValues(
        *(("eHdown", 5),
          ("eHrunning", 2),
          ("eHwarning", 3))
    )


_Hrdevicestatus_Type.__name__ = "Integer32"
_Hrdevicestatus_Object = MibScalar
hrdevicestatus = _Hrdevicestatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 3, 3, 2, 1, 5),
    _Hrdevicestatus_Type()
)
hrdevicestatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrdevicestatus.setStatus("mandatory")
_Hrdeviceerrors_Type = Integer32
_Hrdeviceerrors_Object = MibScalar
hrdeviceerrors = _Hrdeviceerrors_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 3, 3, 2, 1, 6),
    _Hrdeviceerrors_Type()
)
hrdeviceerrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrdeviceerrors.setStatus("mandatory")
_HrPrinterTable_ObjectIdentity = ObjectIdentity
hrPrinterTable = _HrPrinterTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 3, 3, 5)
)
_HrPrinterEntry_ObjectIdentity = ObjectIdentity
hrPrinterEntry = _HrPrinterEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 3, 3, 5, 1)
)


class _Hrprinterstatus_Type(Integer32):
    """Custom type hrprinterstatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("eHidle", 3),
          ("eHother", 1),
          ("eHprinting", 4),
          ("eHwarmup", 5))
    )


_Hrprinterstatus_Type.__name__ = "Integer32"
_Hrprinterstatus_Object = MibScalar
hrprinterstatus = _Hrprinterstatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 3, 3, 5, 1, 1),
    _Hrprinterstatus_Type()
)
hrprinterstatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrprinterstatus.setStatus("mandatory")
_Hrprinterdetectederrorstate_Type = OctetString
_Hrprinterdetectederrorstate_Object = MibScalar
hrprinterdetectederrorstate = _Hrprinterdetectederrorstate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 3, 3, 5, 1, 2),
    _Hrprinterdetectederrorstate_Type()
)
hrprinterdetectederrorstate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrprinterdetectederrorstate.setStatus("mandatory")
_HrDiskStorageTable_ObjectIdentity = ObjectIdentity
hrDiskStorageTable = _HrDiskStorageTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 3, 3, 6)
)
_HrDiskStorageEntry_ObjectIdentity = ObjectIdentity
hrDiskStorageEntry = _HrDiskStorageEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 3, 3, 6, 1)
)


class _Hrdiskstorageaccess_Type(Integer32):
    """Custom type hrdiskstorageaccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eHreadOnly", 2),
          ("eHreadWrite", 1))
    )


_Hrdiskstorageaccess_Type.__name__ = "Integer32"
_Hrdiskstorageaccess_Object = MibScalar
hrdiskstorageaccess = _Hrdiskstorageaccess_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 3, 3, 6, 1, 1),
    _Hrdiskstorageaccess_Type()
)
hrdiskstorageaccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hrdiskstorageaccess.setStatus("mandatory")


class _Hrdiskstoragemedia_Type(Integer32):
    """Custom type hrdiskstoragemedia based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              8)
        )
    )
    namedValues = NamedValues(
        *(("eHhardDisk", 3),
          ("eHother", 1),
          ("eHramDisk", 8))
    )


_Hrdiskstoragemedia_Type.__name__ = "Integer32"
_Hrdiskstoragemedia_Object = MibScalar
hrdiskstoragemedia = _Hrdiskstoragemedia_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 3, 3, 6, 1, 2),
    _Hrdiskstoragemedia_Type()
)
hrdiskstoragemedia.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrdiskstoragemedia.setStatus("mandatory")


class _Hrdiskstorageremoveble_Type(Integer32):
    """Custom type hrdiskstorageremoveble based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            2
        )
    )
    namedValues = NamedValues(
        ("eHfalse", 2)
    )


_Hrdiskstorageremoveble_Type.__name__ = "Integer32"
_Hrdiskstorageremoveble_Object = MibScalar
hrdiskstorageremoveble = _Hrdiskstorageremoveble_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 3, 3, 6, 1, 3),
    _Hrdiskstorageremoveble_Type()
)
hrdiskstorageremoveble.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrdiskstorageremoveble.setStatus("mandatory")
_Hrdiskstoragecapacity_Type = Integer32
_Hrdiskstoragecapacity_Object = MibScalar
hrdiskstoragecapacity = _Hrdiskstoragecapacity_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 3, 3, 6, 1, 4),
    _Hrdiskstoragecapacity_Type()
)
hrdiskstoragecapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrdiskstoragecapacity.setStatus("mandatory")
_HrPartitionTable_ObjectIdentity = ObjectIdentity
hrPartitionTable = _HrPartitionTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 3, 3, 7)
)
_HrPartitionEntry_ObjectIdentity = ObjectIdentity
hrPartitionEntry = _HrPartitionEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 3, 3, 7, 1)
)


class _Hrpartitionindex_Type(Integer32):
    """Custom type hrpartitionindex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hrpartitionindex_Type.__name__ = "Integer32"
_Hrpartitionindex_Object = MibScalar
hrpartitionindex = _Hrpartitionindex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 3, 3, 7, 1, 1),
    _Hrpartitionindex_Type()
)
hrpartitionindex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrpartitionindex.setStatus("mandatory")


class _Hrpartitionlabel_Type(OctetString):
    """Custom type hrpartitionlabel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 11),
    )


_Hrpartitionlabel_Type.__name__ = "OctetString"
_Hrpartitionlabel_Object = MibScalar
hrpartitionlabel = _Hrpartitionlabel_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 3, 3, 7, 1, 2),
    _Hrpartitionlabel_Type()
)
hrpartitionlabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hrpartitionlabel.setStatus("mandatory")
_Hrpartitionid_Type = OctetString
_Hrpartitionid_Object = MibScalar
hrpartitionid = _Hrpartitionid_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 3, 3, 7, 1, 3),
    _Hrpartitionid_Type()
)
hrpartitionid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrpartitionid.setStatus("mandatory")
_Hrpartitionsize_Type = Integer32
_Hrpartitionsize_Object = MibScalar
hrpartitionsize = _Hrpartitionsize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 3, 3, 7, 1, 4),
    _Hrpartitionsize_Type()
)
hrpartitionsize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrpartitionsize.setStatus("mandatory")


class _Hrpartitionfsindex_Type(Integer32):
    """Custom type hrpartitionfsindex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Hrpartitionfsindex_Type.__name__ = "Integer32"
_Hrpartitionfsindex_Object = MibScalar
hrpartitionfsindex = _Hrpartitionfsindex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 3, 3, 7, 1, 5),
    _Hrpartitionfsindex_Type()
)
hrpartitionfsindex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrpartitionfsindex.setStatus("mandatory")
_HrFSTable_ObjectIdentity = ObjectIdentity
hrFSTable = _HrFSTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 3, 3, 8)
)
_HrFSEntry_ObjectIdentity = ObjectIdentity
hrFSEntry = _HrFSEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 3, 3, 8, 1)
)


class _Hrfsindex_Type(Integer32):
    """Custom type hrfsindex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hrfsindex_Type.__name__ = "Integer32"
_Hrfsindex_Object = MibScalar
hrfsindex = _Hrfsindex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 3, 3, 8, 1, 1),
    _Hrfsindex_Type()
)
hrfsindex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrfsindex.setStatus("mandatory")
_Hrfsmountpoint_Type = OctetString
_Hrfsmountpoint_Object = MibScalar
hrfsmountpoint = _Hrfsmountpoint_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 3, 3, 8, 1, 2),
    _Hrfsmountpoint_Type()
)
hrfsmountpoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrfsmountpoint.setStatus("mandatory")
_Hrfsremotemountpoint_Type = OctetString
_Hrfsremotemountpoint_Object = MibScalar
hrfsremotemountpoint = _Hrfsremotemountpoint_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 3, 3, 8, 1, 3),
    _Hrfsremotemountpoint_Type()
)
hrfsremotemountpoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrfsremotemountpoint.setStatus("mandatory")
_Hrfstype_Type = ObjectIdentifier
_Hrfstype_Object = MibScalar
hrfstype = _Hrfstype_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 3, 3, 8, 1, 4),
    _Hrfstype_Type()
)
hrfstype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrfstype.setStatus("mandatory")


class _Hrfsaccess_Type(Integer32):
    """Custom type hrfsaccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eHreadOnly", 2),
          ("eHreadWrite", 1))
    )


_Hrfsaccess_Type.__name__ = "Integer32"
_Hrfsaccess_Object = MibScalar
hrfsaccess = _Hrfsaccess_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 3, 3, 8, 1, 5),
    _Hrfsaccess_Type()
)
hrfsaccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hrfsaccess.setStatus("mandatory")


class _Hrfsbootable_Type(Integer32):
    """Custom type hrfsbootable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            2
        )
    )
    namedValues = NamedValues(
        ("eHfalse", 2)
    )


_Hrfsbootable_Type.__name__ = "Integer32"
_Hrfsbootable_Object = MibScalar
hrfsbootable = _Hrfsbootable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 3, 3, 8, 1, 6),
    _Hrfsbootable_Type()
)
hrfsbootable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrfsbootable.setStatus("mandatory")


class _Hrfsstorageindex_Type(Integer32):
    """Custom type hrfsstorageindex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Hrfsstorageindex_Type.__name__ = "Integer32"
_Hrfsstorageindex_Object = MibScalar
hrfsstorageindex = _Hrfsstorageindex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 3, 3, 8, 1, 7),
    _Hrfsstorageindex_Type()
)
hrfsstorageindex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrfsstorageindex.setStatus("mandatory")
_Hrfslastfullbackupdate_Type = OctetString
_Hrfslastfullbackupdate_Object = MibScalar
hrfslastfullbackupdate = _Hrfslastfullbackupdate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 3, 3, 8, 1, 8),
    _Hrfslastfullbackupdate_Type()
)
hrfslastfullbackupdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrfslastfullbackupdate.setStatus("mandatory")
_Hrfslastpartialbackupdate_Type = OctetString
_Hrfslastpartialbackupdate_Object = MibScalar
hrfslastpartialbackupdate = _Hrfslastpartialbackupdate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 3, 3, 8, 1, 9),
    _Hrfslastpartialbackupdate_Type()
)
hrfslastpartialbackupdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrfslastpartialbackupdate.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LJ4100mfp-MIB",
    **{"DisplayString": DisplayString,
       "hp": hp,
       "dm": dm,
       "device": device,
       "system": system,
       "settings-system": settings_system,
       "energy-star": energy_star,
       "sleep-mode": sleep_mode,
       "status-system": status_system,
       "on-off-line": on_off_line,
       "continue": _pysmi_continue,
       "auto-continue": auto_continue,
       "perm-store-init-occurred": perm_store_init_occurred,
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
       "simm3": simm3,
       "simm3-type": simm3_type,
       "simm3-capacity": simm3_capacity,
       "simm3-bank": simm3_bank,
       "simm3-bank1": simm3_bank1,
       "simm3-bank1-type": simm3_bank1_type,
       "simm3-bank1-capacity": simm3_bank1_capacity,
       "simm3-bank2": simm3_bank2,
       "simm3-bank2-type": simm3_bank2_type,
       "simm3-bank2-capacity": simm3_bank2_capacity,
       "simm4": simm4,
       "simm4-type": simm4_type,
       "simm4-capacity": simm4_capacity,
       "simm4-bank": simm4_bank,
       "simm4-bank1": simm4_bank1,
       "simm4-bank1-type": simm4_bank1_type,
       "simm4-bank1-capacity": simm4_bank1_capacity,
       "simm4-bank2": simm4_bank2,
       "simm4-bank2-type": simm4_bank2_type,
       "simm4-bank2-capacity": simm4_bank2_capacity,
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
       "phd": phd,
       "phd1": phd1,
       "phd1-model": phd1_model,
       "phd1-manufacturing-info": phd1_manufacturing_info,
       "phd1-type": phd1_type,
       "phd1-capacity": phd1_capacity,
       "phd2": phd2,
       "phd2-model": phd2_model,
       "phd2-manufacturing-info": phd2_manufacturing_info,
       "phd2-type": phd2_type,
       "phd2-capacity": phd2_capacity,
       "phd3": phd3,
       "phd3-model": phd3_model,
       "phd3-manufacturing-info": phd3_manufacturing_info,
       "phd3-type": phd3_type,
       "phd3-capacity": phd3_capacity,
       "phd4": phd4,
       "phd4-model": phd4_model,
       "phd4-manufacturing-info": phd4_manufacturing_info,
       "phd4-type": phd4_type,
       "phd4-capacity": phd4_capacity,
       "phd5": phd5,
       "phd5-model": phd5_model,
       "phd5-manufacturing-info": phd5_manufacturing_info,
       "phd5-type": phd5_type,
       "phd5-capacity": phd5_capacity,
       "phd6": phd6,
       "phd6-model": phd6_model,
       "phd6-manufacturing-info": phd6_manufacturing_info,
       "phd6-type": phd6_type,
       "phd6-capacity": phd6_capacity,
       "socket-ping": socket_ping,
       "socket-ping-job-events-version": socket_ping_job_events_version,
       "test": test,
       "self-test": self_test,
       "print-internal-page": print_internal_page,
       "engine-self-diagnostic": engine_self_diagnostic,
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
       "error2": error2,
       "error2-time-stamp": error2_time_stamp,
       "error2-code": error2_code,
       "error3": error3,
       "error3-time-stamp": error3_time_stamp,
       "error3-code": error3_code,
       "error4": error4,
       "error4-time-stamp": error4_time_stamp,
       "error4-code": error4_code,
       "error5": error5,
       "error5-time-stamp": error5_time_stamp,
       "error5-code": error5_code,
       "error6": error6,
       "error6-time-stamp": error6_time_stamp,
       "error6-code": error6_code,
       "error7": error7,
       "error7-time-stamp": error7_time_stamp,
       "error7-code": error7_code,
       "error8": error8,
       "error8-time-stamp": error8_time_stamp,
       "error8-code": error8_code,
       "error9": error9,
       "error9-time-stamp": error9_time_stamp,
       "error9-code": error9_code,
       "error10": error10,
       "error10-time-stamp": error10_time_stamp,
       "error10-code": error10_code,
       "error11": error11,
       "error11-time-stamp": error11_time_stamp,
       "error11-code": error11_code,
       "error12": error12,
       "error12-time-stamp": error12_time_stamp,
       "error12-code": error12_code,
       "error13": error13,
       "error13-time-stamp": error13_time_stamp,
       "error13-code": error13_code,
       "error14": error14,
       "error14-time-stamp": error14_time_stamp,
       "error14-code": error14_code,
       "error15": error15,
       "error15-time-stamp": error15_time_stamp,
       "error15-code": error15_code,
       "error16": error16,
       "error16-time-stamp": error16_time_stamp,
       "error16-code": error16_code,
       "error17": error17,
       "error17-time-stamp": error17_time_stamp,
       "error17-code": error17_code,
       "error18": error18,
       "error18-time-stamp": error18_time_stamp,
       "error18-code": error18_code,
       "error19": error19,
       "error19-time-stamp": error19_time_stamp,
       "error19-code": error19_code,
       "error20": error20,
       "error20-time-stamp": error20_time_stamp,
       "error20-code": error20_code,
       "error21": error21,
       "error21-time-stamp": error21_time_stamp,
       "error21-code": error21_code,
       "error22": error22,
       "error22-time-stamp": error22_time_stamp,
       "error22-code": error22_code,
       "error23": error23,
       "error23-time-stamp": error23_time_stamp,
       "error23-code": error23_code,
       "error24": error24,
       "error24-time-stamp": error24_time_stamp,
       "error24-code": error24_code,
       "error25": error25,
       "error25-time-stamp": error25_time_stamp,
       "error25-code": error25_code,
       "error26": error26,
       "error26-time-stamp": error26_time_stamp,
       "error26-code": error26_code,
       "error27": error27,
       "error27-time-stamp": error27_time_stamp,
       "error27-code": error27_code,
       "error28": error28,
       "error28-time-stamp": error28_time_stamp,
       "error28-code": error28_code,
       "error29": error29,
       "error29-time-stamp": error29_time_stamp,
       "error29-code": error29_code,
       "error30": error30,
       "error30-time-stamp": error30_time_stamp,
       "error30-code": error30_code,
       "error31": error31,
       "error31-time-stamp": error31_time_stamp,
       "error31-code": error31_code,
       "error32": error32,
       "error32-time-stamp": error32_time_stamp,
       "error32-code": error32_code,
       "error33": error33,
       "error33-time-stamp": error33_time_stamp,
       "error33-code": error33_code,
       "error34": error34,
       "error34-time-stamp": error34_time_stamp,
       "error34-code": error34_code,
       "error35": error35,
       "error35-time-stamp": error35_time_stamp,
       "error35-code": error35_code,
       "error36": error36,
       "error36-time-stamp": error36_time_stamp,
       "error36-code": error36_code,
       "error37": error37,
       "error37-time-stamp": error37_time_stamp,
       "error37-code": error37_code,
       "error38": error38,
       "error38-time-stamp": error38_time_stamp,
       "error38-code": error38_code,
       "error39": error39,
       "error39-time-stamp": error39_time_stamp,
       "error39-code": error39_code,
       "error40": error40,
       "error40-time-stamp": error40_time_stamp,
       "error40-code": error40_code,
       "error41": error41,
       "error41-time-stamp": error41_time_stamp,
       "error41-code": error41_code,
       "error42": error42,
       "error42-time-stamp": error42_time_stamp,
       "error42-code": error42_code,
       "error43": error43,
       "error43-time-stamp": error43_time_stamp,
       "error43-code": error43_code,
       "error44": error44,
       "error44-time-stamp": error44_time_stamp,
       "error44-code": error44_code,
       "error45": error45,
       "error45-time-stamp": error45_time_stamp,
       "error45-code": error45_code,
       "error46": error46,
       "error46-time-stamp": error46_time_stamp,
       "error46-code": error46_code,
       "error47": error47,
       "error47-time-stamp": error47_time_stamp,
       "error47-code": error47_code,
       "error48": error48,
       "error48-time-stamp": error48_time_stamp,
       "error48-code": error48_code,
       "error49": error49,
       "error49-time-stamp": error49_time_stamp,
       "error49-code": error49_code,
       "error50": error50,
       "error50-time-stamp": error50_time_stamp,
       "error50-code": error50_code,
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
       "usage-printer-total-charge": usage_printer_total_charge,
       "usage-average-toner-coverage": usage_average_toner_coverage,
       "usage-instructions-line1": usage_instructions_line1,
       "usage-instructions-line2": usage_instructions_line2,
       "usage-instructions-line3": usage_instructions_line3,
       "usage-instructions-line4": usage_instructions_line4,
       "scanner-accounting": scanner_accounting,
       "scanned-media-usage": scanned_media_usage,
       "scanned-media-simplex-count": scanned_media_simplex_count,
       "scanned-media-simplex-charge": scanned_media_simplex_charge,
       "scanned-media-duplex-count": scanned_media_duplex_count,
       "scanned-media-duplex-charge": scanned_media_duplex_charge,
       "scanned-media-total-charge": scanned_media_total_charge,
       "usage-scanner-total-charge": usage_scanner_total_charge,
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
       "scanner-accessory-dimm1-type": scanner_accessory_dimm1_type,
       "scanner-accessory-dimm2-type": scanner_accessory_dimm2_type,
       "scanner-accessory-dimm1-capacity": scanner_accessory_dimm1_capacity,
       "scanner-accessory-dimm2-capacity": scanner_accessory_dimm2_capacity,
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
       "default-scan-heavy-media-mode": default_scan_heavy_media_mode,
       "auto-send-reset": auto_send_reset,
       "scanner-accessory-digital-send-log-event-counter": scanner_accessory_digital_send_log_event_counter,
       "scanner-accessory-digital-send-config-email-gateway": scanner_accessory_digital_send_config_email_gateway,
       "scanner-accessory-digital-send-config-ldap-gateway": scanner_accessory_digital_send_config_ldap_gateway,
       "scanner-accessory-digital-send-config-dsm-enabled-fax": scanner_accessory_digital_send_config_dsm_enabled_fax,
       "scanner-accessory-digital-send-config-fax-embedded": scanner_accessory_digital_send_config_fax_embedded,
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
       "pjl": pjl,
       "pjl-password": pjl_password,
       "fax-proc-sub": fax_proc_sub,
       "settings-fax-proc-sub": settings_fax_proc_sub,
       "fax-print-page-count": fax_print_page_count,
       "webserver-proc-sub": webserver_proc_sub,
       "settings-webserver": settings_webserver,
       "web-server-password": web_server_password,
       "web-server-url": web_server_url,
       "web-server-security": web_server_security,
       "destination-subsystem": destination_subsystem,
       "print-engine": print_engine,
       "settings-prt-eng": settings_prt_eng,
       "override-media-name": override_media_name,
       "override-media-size": override_media_size,
       "print-density": print_density,
       "marking-agent-density": marking_agent_density,
       "marking-agent-density-setting": marking_agent_density_setting,
       "autocleaning-page-enable": autocleaning_page_enable,
       "autocleaning-page-frequency": autocleaning_page_frequency,
       "autocleaning-page-size": autocleaning_page_size,
       "default-audible-feedback": default_audible_feedback,
       "default-reset-send-timeout": default_reset_send_timeout,
       "default-authentication-timeout": default_authentication_timeout,
       "status-prt-eng": status_prt_eng,
       "duplex-page-count": duplex_page_count,
       "print-engine-revision": print_engine_revision,
       "intray": intray,
       "settings-intray": settings_intray,
       "mp-tray": mp_tray,
       "default-custom-paper-dim-unit": default_custom_paper_dim_unit,
       "default-custom-paper-feed-dim": default_custom_paper_feed_dim,
       "default-custom-paper-xfeed-dim": default_custom_paper_xfeed_dim,
       "input-tray-max-media-feed-dim": input_tray_max_media_feed_dim,
       "input-tray-max-media-xfeed-dim": input_tray_max_media_xfeed_dim,
       "input-tray-min-media-feed-dim": input_tray_min_media_feed_dim,
       "input-tray-min-media-xfeed-dim": input_tray_min_media_xfeed_dim,
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
       "intray4": intray4,
       "tray4-media-size-loaded": tray4_media_size_loaded,
       "tray4-phd": tray4_phd,
       "intray5": intray5,
       "tray5-media-size-loaded": tray5_media_size_loaded,
       "tray5-phd": tray5_phd,
       "intray6": intray6,
       "tray6-media-size-loaded": tray6_media_size_loaded,
       "tray6-phd": tray6_phd,
       "intray7": intray7,
       "tray7-media-size-loaded": tray7_media_size_loaded,
       "tray7-phd": tray7_phd,
       "outbin": outbin,
       "settings-outbin": settings_outbin,
       "overflow-bin": overflow_bin,
       "outbins": outbins,
       "outbin1": outbin1,
       "outbin1-override-mode": outbin1_override_mode,
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
       "outbin6": outbin6,
       "outbin6-override-mode": outbin6_override_mode,
       "outbin6-maximum-binding": outbin6_maximum_binding,
       "outbin6-phd": outbin6_phd,
       "outbin6-error-info": outbin6_error_info,
       "outbin7": outbin7,
       "outbin7-override-mode": outbin7_override_mode,
       "outbin7-maximum-binding": outbin7_maximum_binding,
       "outbin7-phd": outbin7_phd,
       "outbin7-error-info": outbin7_error_info,
       "outbin8": outbin8,
       "outbin8-override-mode": outbin8_override_mode,
       "outbin8-maximum-binding": outbin8_maximum_binding,
       "outbin8-phd": outbin8_phd,
       "outbin8-error-info": outbin8_error_info,
       "outbin9": outbin9,
       "outbin9-override-mode": outbin9_override_mode,
       "outbin9-maximum-binding": outbin9_maximum_binding,
       "outbin9-phd": outbin9_phd,
       "outbin9-error-info": outbin9_error_info,
       "outbin10": outbin10,
       "outbin10-override-mode": outbin10_override_mode,
       "outbin10-maximum-binding": outbin10_maximum_binding,
       "outbin10-phd": outbin10_phd,
       "outbin10-error-info": outbin10_error_info,
       "outbin11": outbin11,
       "outbin11-override-mode": outbin11_override_mode,
       "outbin11-maximum-binding": outbin11_maximum_binding,
       "outbin11-phd": outbin11_phd,
       "outbin11-error-info": outbin11_error_info,
       "marking-agent": marking_agent,
       "settings-marking-agent": settings_marking_agent,
       "low-marking-agent-processing": low_marking_agent_processing,
       "out-marking-agent-processing": out_marking_agent_processing,
       "imaging": imaging,
       "default-ret": default_ret,
       "default-print-quality": default_print_quality,
       "ph": ph,
       "ph-devices": ph_devices,
       "ph2": ph2,
       "phd2-device-specific-command": phd2_device_specific_command,
       "ph3": ph3,
       "phd3-device-specific-command": phd3_device_specific_command,
       "ph4": ph4,
       "phd4-device-specific-command": phd4_device_specific_command,
       "ph5": ph5,
       "phd5-device-specific-command": phd5_device_specific_command,
       "ph6": ph6,
       "phd6-device-specific-command": phd6_device_specific_command,
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
       "media13": media13,
       "media13-engine-media-mode": media13_engine_media_mode,
       "media14": media14,
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
       "media-modes": media_modes,
       "engine-media-modes-supported1": engine_media_modes_supported1,
       "media-size": media_size,
       "media-size-count": media_size_count,
       "media-size-west-edge-first-side-offset": media_size_west_edge_first_side_offset,
       "media-size-west-edge-second-side-offset": media_size_west_edge_second_side_offset,
       "media-size-west-edge-side-offset-by-tray": media_size_west_edge_side_offset_by_tray,
       "consumables": consumables,
       "consumables-1": consumables_1,
       "consumable-status": consumable_status,
       "consumable-status-cartridge-model": consumable_status_cartridge_model,
       "consumable-status-manufacturing-date": consumable_status_manufacturing_date,
       "consumable-status-serial-number": consumable_status_serial_number,
       "consumable-status-capacity-units": consumable_status_capacity_units,
       "consumable-status-total-capacity": consumable_status_total_capacity,
       "consumable-status-reseller-id": consumable_status_reseller_id,
       "consumable-status-info": consumable_status_info,
       "consumable-status-first-install-date": consumable_status_first_install_date,
       "consumable-status-last-use-date": consumable_status_last_use_date,
       "consumable-status-page-count-a3-ledger": consumable_status_page_count_a3_ledger,
       "consumable-status-page-count-legal": consumable_status_page_count_legal,
       "consumable-status-page-count-a4-letter": consumable_status_page_count_a4_letter,
       "consumable-status-page-count-b5-executive": consumable_status_page_count_b5_executive,
       "consumable-status-page-count-envelope": consumable_status_page_count_envelope,
       "consumable-status-page-count-xy-other": consumable_status_page_count_xy_other,
       "consumable-status-job-count": consumable_status_job_count,
       "consumable-status-usage-units": consumable_status_usage_units,
       "consumable-status-usage-count": consumable_status_usage_count,
       "consumable-status-manufacturer-name": consumable_status_manufacturer_name,
       "consumable-status-oem-name": consumable_status_oem_name,
       "consumable-reorder-url": consumable_reorder_url,
       "consumable-maintenance-interval": consumable_maintenance_interval,
       "consumable-maintenance-pages-remaining": consumable_maintenance_pages_remaining,
       "consumables-status": consumables_status,
       "consumables-life": consumables_life,
       "consumable-life-usage-units-remaining": consumable_life_usage_units_remaining,
       "consumable-life-usage-units": consumable_life_usage_units,
       "consumables-test": consumables_test,
       "consumable-test-password": consumable_test_password,
       "print-meter": print_meter,
       "printer-average": printer_average,
       "printer-average-marking-agent-coverage": printer_average_marking_agent_coverage,
       "printer-average-marking-agent-coverage-sum": printer_average_marking_agent_coverage_sum,
       "printer-average-marking-agent-coverage-sum-squared": printer_average_marking_agent_coverage_sum_squared,
       "printer-average-marking-agent-units-per-gram": printer_average_marking_agent_units_per_gram,
       "copier": copier,
       "settings-copier": settings_copier,
       "default-copier-media-size": default_copier_media_size,
       "default-copier-image-type": default_copier_image_type,
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
       "channel": channel,
       "channelnumberofchannels": channelnumberofchannels,
       "channelprinteralert": channelprinteralert,
       "channelTable": channelTable,
       "channelEntry": channelEntry,
       "channeltype": channeltype,
       "channelprotocolversion": channelprotocolversion,
       "channelstate": channelstate,
       "channelifindex": channelifindex,
       "channelstatus": channelstatus,
       "channelinformation": channelinformation,
       "tables": tables,
       "channel-table": channel_table,
       "channel-entry": channel_entry,
       "channel-bytes-sent": channel_bytes_sent,
       "channel-bytes-received": channel_bytes_received,
       "channel-io-errors": channel_io_errors,
       "channel-jobs-received": channel_jobs_received,
       "channel-mio": channel_mio,
       "printmib": printmib,
       "prtGeneral": prtGeneral,
       "prtGeneralTable": prtGeneralTable,
       "prtGeneralEntry": prtGeneralEntry,
       "prtgeneralconfigchanges": prtgeneralconfigchanges,
       "prtgeneralcurrentlocalization": prtgeneralcurrentlocalization,
       "prtgeneralreset": prtgeneralreset,
       "prtgeneralcurrentoperator": prtgeneralcurrentoperator,
       "prtgeneralserviceperson": prtgeneralserviceperson,
       "prtinputdefaultindex": prtinputdefaultindex,
       "prtoutputdefaultindex": prtoutputdefaultindex,
       "prtmarkerdefaultindex": prtmarkerdefaultindex,
       "prtmediapathdefaultindex": prtmediapathdefaultindex,
       "prtconsolelocalization": prtconsolelocalization,
       "prtconsolenumberofdisplaylines": prtconsolenumberofdisplaylines,
       "prtconsolenumberofdisplaychars": prtconsolenumberofdisplaychars,
       "prtconsoledisable": prtconsoledisable,
       "prtgeneralstartuppage": prtgeneralstartuppage,
       "prtgeneralbannerpage": prtgeneralbannerpage,
       "prtgeneralprintername": prtgeneralprintername,
       "prtgeneralserialnumber": prtgeneralserialnumber,
       "prtalertcriticalevents": prtalertcriticalevents,
       "prtalertallevents": prtalertallevents,
       "prtStorageRefTable": prtStorageRefTable,
       "prtStorageRefEntry": prtStorageRefEntry,
       "prtstoragerefindex": prtstoragerefindex,
       "prtDeviceRefTable": prtDeviceRefTable,
       "prtDeviceRefEntry": prtDeviceRefEntry,
       "prtdevicerefindex": prtdevicerefindex,
       "prtCover": prtCover,
       "prtCoverTable": prtCoverTable,
       "prtCoverEntry": prtCoverEntry,
       "prtcoverdescription": prtcoverdescription,
       "prtcoverstatus": prtcoverstatus,
       "prtLocalization": prtLocalization,
       "prtLocalizationTable": prtLocalizationTable,
       "prtLocalizationEntry": prtLocalizationEntry,
       "prtlocalizationlanguage": prtlocalizationlanguage,
       "prtlocalizationcountry": prtlocalizationcountry,
       "prtlocalizationcharacterset": prtlocalizationcharacterset,
       "prtInput": prtInput,
       "prtInputTable": prtInputTable,
       "prtInputEntry": prtInputEntry,
       "prtinputtype": prtinputtype,
       "prtinputdimunit": prtinputdimunit,
       "prtinputmediadimfeeddirdeclared": prtinputmediadimfeeddirdeclared,
       "prtinputmediadimxfeeddirdeclared": prtinputmediadimxfeeddirdeclared,
       "prtinputmediadimfeeddirchosen": prtinputmediadimfeeddirchosen,
       "prtinputmediadimxfeeddirchosen": prtinputmediadimxfeeddirchosen,
       "prtinputcapacityunit": prtinputcapacityunit,
       "prtinputmaxcapacity": prtinputmaxcapacity,
       "prtinputcurrentlevel": prtinputcurrentlevel,
       "prtinputstatus": prtinputstatus,
       "prtinputmedianame": prtinputmedianame,
       "prtinputname": prtinputname,
       "prtinputvendorname": prtinputvendorname,
       "prtinputmodel": prtinputmodel,
       "prtinputversion": prtinputversion,
       "prtinputserialnumber": prtinputserialnumber,
       "prtinputdescription": prtinputdescription,
       "prtinputsecurity": prtinputsecurity,
       "prtinputmedialoadtimeout": prtinputmedialoadtimeout,
       "prtinputnextindex": prtinputnextindex,
       "prtOutput": prtOutput,
       "prtOutputTable": prtOutputTable,
       "prtOutputEntry": prtOutputEntry,
       "prtoutputtype": prtoutputtype,
       "prtoutputcapacityunit": prtoutputcapacityunit,
       "prtoutputmaxcapacity": prtoutputmaxcapacity,
       "prtoutputremainingcapacity": prtoutputremainingcapacity,
       "prtoutputstatus": prtoutputstatus,
       "prtoutputname": prtoutputname,
       "prtoutputvendorname": prtoutputvendorname,
       "prtoutputmodel": prtoutputmodel,
       "prtoutputversion": prtoutputversion,
       "prtoutputserialnumber": prtoutputserialnumber,
       "prtoutputdescription": prtoutputdescription,
       "prtoutputsecurity": prtoutputsecurity,
       "prtoutputdimunit": prtoutputdimunit,
       "prtoutputmaxdimfeeddir": prtoutputmaxdimfeeddir,
       "prtoutputmaxdimxfeeddir": prtoutputmaxdimxfeeddir,
       "prtoutputmindimfeeddir": prtoutputmindimfeeddir,
       "prtoutputmindimxfeeddir": prtoutputmindimxfeeddir,
       "prtoutputstackingorder": prtoutputstackingorder,
       "prtoutputpagedeliveryorientation": prtoutputpagedeliveryorientation,
       "prtoutputbursting": prtoutputbursting,
       "prtoutputdecollating": prtoutputdecollating,
       "prtoutputpagecollated": prtoutputpagecollated,
       "prtoutputoffsetstacking": prtoutputoffsetstacking,
       "prtMarker": prtMarker,
       "prtMarkerTable": prtMarkerTable,
       "prtMarkerEntry": prtMarkerEntry,
       "prtmarkermarktech": prtmarkermarktech,
       "prtmarkercounterunit": prtmarkercounterunit,
       "prtmarkerlifecount": prtmarkerlifecount,
       "prtmarkerpoweroncount": prtmarkerpoweroncount,
       "prtmarkerprocesscolorants": prtmarkerprocesscolorants,
       "prtmarkerspotcolorants": prtmarkerspotcolorants,
       "prtmarkeraddressabilityunit": prtmarkeraddressabilityunit,
       "prtmarkeraddressabilityfeeddir": prtmarkeraddressabilityfeeddir,
       "prtmarkeraddressabilityxfeeddir": prtmarkeraddressabilityxfeeddir,
       "prtmarkernorthmargin": prtmarkernorthmargin,
       "prtmarkersouthmargin": prtmarkersouthmargin,
       "prtmarkerwestmargin": prtmarkerwestmargin,
       "prtmarkereastmargin": prtmarkereastmargin,
       "prtmarkerstatus": prtmarkerstatus,
       "prtMarkerSupplies": prtMarkerSupplies,
       "prtMarkerSuppliesTable": prtMarkerSuppliesTable,
       "prtMarkerSuppliesEntry": prtMarkerSuppliesEntry,
       "prtmarkersuppliesmarkerindex": prtmarkersuppliesmarkerindex,
       "prtmarkersuppliescolorantindex": prtmarkersuppliescolorantindex,
       "prtmarkersuppliesclass": prtmarkersuppliesclass,
       "prtmarkersuppliestype": prtmarkersuppliestype,
       "prtmarkersuppliesdescription": prtmarkersuppliesdescription,
       "prtmarkersuppliessupplyunit": prtmarkersuppliessupplyunit,
       "prtmarkersuppliesmaxcapacity": prtmarkersuppliesmaxcapacity,
       "prtmarkersupplieslevel": prtmarkersupplieslevel,
       "prtMarkerColorant": prtMarkerColorant,
       "prtMarkerColorantTable": prtMarkerColorantTable,
       "prtMarkerColorantEntry": prtMarkerColorantEntry,
       "prtmarkercolorantmarkerindex": prtmarkercolorantmarkerindex,
       "prtmarkercolorantrole": prtmarkercolorantrole,
       "prtmarkercolorantvalue": prtmarkercolorantvalue,
       "prtmarkercoloranttonality": prtmarkercoloranttonality,
       "prtMediaPath": prtMediaPath,
       "prtMediaPathTable": prtMediaPathTable,
       "prtMediaPathEntry": prtMediaPathEntry,
       "prtmediapathmaxspeedprintunit": prtmediapathmaxspeedprintunit,
       "prtmediapathmediasizeunit": prtmediapathmediasizeunit,
       "prtmediapathmaxspeed": prtmediapathmaxspeed,
       "prtmediapathmaxmediafeeddir": prtmediapathmaxmediafeeddir,
       "prtmediapathmaxmediaxfeeddir": prtmediapathmaxmediaxfeeddir,
       "prtmediapathminmediafeeddir": prtmediapathminmediafeeddir,
       "prtmediapathminmediaxfeeddir": prtmediapathminmediaxfeeddir,
       "prtmediapathtype": prtmediapathtype,
       "prtmediapathdescription": prtmediapathdescription,
       "prtmediapathstatus": prtmediapathstatus,
       "prtChannel": prtChannel,
       "prtChannelTable": prtChannelTable,
       "prtChannelEntry": prtChannelEntry,
       "prtchanneltype": prtchanneltype,
       "prtchannelprotocolversion": prtchannelprotocolversion,
       "prtchannelcurrentjobcntllangindex": prtchannelcurrentjobcntllangindex,
       "prtchanneldefaultpagedesclangindex": prtchanneldefaultpagedesclangindex,
       "prtchannelstate": prtchannelstate,
       "prtchannelifindex": prtchannelifindex,
       "prtchannelstatus": prtchannelstatus,
       "prtchannelinformation": prtchannelinformation,
       "prtInterpreter": prtInterpreter,
       "prtInterpreterTable": prtInterpreterTable,
       "prtInterpreterEntry": prtInterpreterEntry,
       "prtinterpreterlangfamily": prtinterpreterlangfamily,
       "prtinterpreterlanglevel": prtinterpreterlanglevel,
       "prtinterpreterlangversion": prtinterpreterlangversion,
       "prtinterpreterdescription": prtinterpreterdescription,
       "prtinterpreterversion": prtinterpreterversion,
       "prtinterpreterdefaultorientation": prtinterpreterdefaultorientation,
       "prtinterpreterfeedaddressability": prtinterpreterfeedaddressability,
       "prtinterpreterxfeedaddressability": prtinterpreterxfeedaddressability,
       "prtinterpreterdefaultcharsetin": prtinterpreterdefaultcharsetin,
       "prtinterpreterdefaultcharsetout": prtinterpreterdefaultcharsetout,
       "prtinterpretertwoway": prtinterpretertwoway,
       "prtConsoleDisplayBuffer": prtConsoleDisplayBuffer,
       "prtConsoleDisplayBufferTable": prtConsoleDisplayBufferTable,
       "prtConsoleDisplayBufferEntry": prtConsoleDisplayBufferEntry,
       "prtconsoledisplaybuffertext": prtconsoledisplaybuffertext,
       "prtConsoleLights": prtConsoleLights,
       "prtConsoleLightTable": prtConsoleLightTable,
       "prtConsoleLightEntry": prtConsoleLightEntry,
       "prtconsoleontime": prtconsoleontime,
       "prtconsoleofftime": prtconsoleofftime,
       "prtconsolecolor": prtconsolecolor,
       "prtconsoledescription": prtconsoledescription,
       "prtAlert": prtAlert,
       "prtAlertTable": prtAlertTable,
       "prtAlertEntry": prtAlertEntry,
       "prtalertseveritylevel": prtalertseveritylevel,
       "prtalerttraininglevel": prtalerttraininglevel,
       "prtalertgroup": prtalertgroup,
       "prtalertgroupindex": prtalertgroupindex,
       "prtalertlocation": prtalertlocation,
       "prtalertcode": prtalertcode,
       "prtalertdescription": prtalertdescription,
       "prtalerttime": prtalerttime,
       "hrm": hrm,
       "hrStorage": hrStorage,
       "hrmemorysize": hrmemorysize,
       "hrStorageTable": hrStorageTable,
       "hrStorageEntry": hrStorageEntry,
       "hrstorageindex": hrstorageindex,
       "hrstoragetype": hrstoragetype,
       "hrstoragedescr": hrstoragedescr,
       "hrstorageallocationunits": hrstorageallocationunits,
       "hrstoragesize": hrstoragesize,
       "hrstorageused": hrstorageused,
       "hrstorageallocationfailures": hrstorageallocationfailures,
       "hrDevice": hrDevice,
       "hrDeviceTable": hrDeviceTable,
       "hrDeviceEntry": hrDeviceEntry,
       "hrdeviceindex": hrdeviceindex,
       "hrdevicetype": hrdevicetype,
       "hrdevicedescr": hrdevicedescr,
       "hrdeviceid": hrdeviceid,
       "hrdevicestatus": hrdevicestatus,
       "hrdeviceerrors": hrdeviceerrors,
       "hrPrinterTable": hrPrinterTable,
       "hrPrinterEntry": hrPrinterEntry,
       "hrprinterstatus": hrprinterstatus,
       "hrprinterdetectederrorstate": hrprinterdetectederrorstate,
       "hrDiskStorageTable": hrDiskStorageTable,
       "hrDiskStorageEntry": hrDiskStorageEntry,
       "hrdiskstorageaccess": hrdiskstorageaccess,
       "hrdiskstoragemedia": hrdiskstoragemedia,
       "hrdiskstorageremoveble": hrdiskstorageremoveble,
       "hrdiskstoragecapacity": hrdiskstoragecapacity,
       "hrPartitionTable": hrPartitionTable,
       "hrPartitionEntry": hrPartitionEntry,
       "hrpartitionindex": hrpartitionindex,
       "hrpartitionlabel": hrpartitionlabel,
       "hrpartitionid": hrpartitionid,
       "hrpartitionsize": hrpartitionsize,
       "hrpartitionfsindex": hrpartitionfsindex,
       "hrFSTable": hrFSTable,
       "hrFSEntry": hrFSEntry,
       "hrfsindex": hrfsindex,
       "hrfsmountpoint": hrfsmountpoint,
       "hrfsremotemountpoint": hrfsremotemountpoint,
       "hrfstype": hrfstype,
       "hrfsaccess": hrfsaccess,
       "hrfsbootable": hrfsbootable,
       "hrfsstorageindex": hrfsstorageindex,
       "hrfslastfullbackupdate": hrfslastfullbackupdate,
       "hrfslastpartialbackupdate": hrfslastpartialbackupdate}
)
