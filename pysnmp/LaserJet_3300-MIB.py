# SNMP MIB module (LaserJet_3300-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/LaserJet_3300-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:19:53 2024
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
energy_star.setMaxAccess("read-only")
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
sleep_mode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleep_mode.setStatus("optional")
_Service_password_Type = Integer32
_Service_password_Object = MibScalar
service_password = _Service_password_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 1, 9),
    _Service_password_Type()
)
service_password.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    service_password.setStatus("optional")


class _Device_cfg_download_Type(Integer32):
    """Custom type device_cfg_download based on Integer32"""
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
        *(("eCfgDownloadAborted", 4),
          ("eCfgDownloadActive", 3),
          ("eCfgDownloadDone", 5),
          ("eCfgDownloadIdle", 1),
          ("eCfgDownloadStart", 2))
    )


_Device_cfg_download_Type.__name__ = "Integer32"
_Device_cfg_download_Object = MibScalar
device_cfg_download = _Device_cfg_download_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 1, 11),
    _Device_cfg_download_Type()
)
device_cfg_download.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    device_cfg_download.setStatus("optional")


class _Device_cfg_download_data_type_Type(Integer32):
    """Custom type device_cfg_download_data_type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              6,
              7,
              9)
        )
    )
    namedValues = NamedValues(
        *(("eConfigPrams", 7),
          ("eFaxLogs", 6),
          ("eJunkFaxDialStrings", 9),
          ("eSpeedDials", 5))
    )


_Device_cfg_download_data_type_Type.__name__ = "Integer32"
_Device_cfg_download_data_type_Object = MibScalar
device_cfg_download_data_type = _Device_cfg_download_data_type_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 1, 12),
    _Device_cfg_download_data_type_Type()
)
device_cfg_download_data_type.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    device_cfg_download_data_type.setStatus("optional")


class _Device_cfg_upload_Type(Integer32):
    """Custom type device_cfg_upload based on Integer32"""
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
        *(("eCfgUploadAborted", 4),
          ("eCfgUploadActive", 3),
          ("eCfgUploadDone", 5),
          ("eCfgUploadIdle", 1),
          ("eCfgUploadStart", 2))
    )


_Device_cfg_upload_Type.__name__ = "Integer32"
_Device_cfg_upload_Object = MibScalar
device_cfg_upload = _Device_cfg_upload_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 1, 13),
    _Device_cfg_upload_Type()
)
device_cfg_upload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    device_cfg_upload.setStatus("optional")


class _Device_cfg_upload_data_type_Type(Integer32):
    """Custom type device_cfg_upload_data_type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              6,
              7,
              9)
        )
    )
    namedValues = NamedValues(
        *(("eConfigPrams", 7),
          ("eFaxLogs", 6),
          ("eJunkFaxDialStrings", 9),
          ("eSpeedDials", 5))
    )


_Device_cfg_upload_data_type_Type.__name__ = "Integer32"
_Device_cfg_upload_data_type_Object = MibScalar
device_cfg_upload_data_type = _Device_cfg_upload_data_type_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 1, 14),
    _Device_cfg_upload_data_type_Type()
)
device_cfg_upload_data_type.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    device_cfg_upload_data_type.setStatus("optional")
_Download_timeout_Type = Integer32
_Download_timeout_Object = MibScalar
download_timeout = _Download_timeout_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 1, 17),
    _Download_timeout_Type()
)
download_timeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    download_timeout.setStatus("optional")
_Upload_timeout_Type = Integer32
_Upload_timeout_Object = MibScalar
upload_timeout = _Upload_timeout_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 1, 18),
    _Upload_timeout_Type()
)
upload_timeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upload_timeout.setStatus("optional")


class _Date_display_Type(Integer32):
    """Custom type date_display based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("eDateDisplayDDMMYY", 2),
          ("eDateDisplayMMDDYY", 1),
          ("eDateDisplayYYMMDD", 3))
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
_Device_cfg_param_command_Type = OctetString
_Device_cfg_param_command_Object = MibScalar
device_cfg_param_command = _Device_cfg_param_command_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 1, 23),
    _Device_cfg_param_command_Type()
)
device_cfg_param_command.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    device_cfg_param_command.setStatus("optional")


class _Copier_token_Type(OctetString):
    """Custom type copier_token based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_Copier_token_Type.__name__ = "OctetString"
_Copier_token_Object = MibScalar
copier_token = _Copier_token_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 1, 24),
    _Copier_token_Type()
)
copier_token.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    copier_token.setStatus("optional")


class _Scan_token_Type(OctetString):
    """Custom type scan_token based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_Scan_token_Type.__name__ = "OctetString"
_Scan_token_Object = MibScalar
scan_token = _Scan_token_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 1, 25),
    _Scan_token_Type()
)
scan_token.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scan_token.setStatus("optional")


class _Fax_upload_token_Type(OctetString):
    """Custom type fax_upload_token based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_Fax_upload_token_Type.__name__ = "OctetString"
_Fax_upload_token_Object = MibScalar
fax_upload_token = _Fax_upload_token_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 1, 26),
    _Fax_upload_token_Type()
)
fax_upload_token.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fax_upload_token.setStatus("optional")


class _Fax_download_token_Type(OctetString):
    """Custom type fax_download_token based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_Fax_download_token_Type.__name__ = "OctetString"
_Fax_download_token_Object = MibScalar
fax_download_token = _Fax_download_token_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 1, 27),
    _Fax_download_token_Type()
)
fax_download_token.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fax_download_token.setStatus("optional")


class _Device_config_token_Type(OctetString):
    """Custom type device_config_token based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(128, 128),
    )


_Device_config_token_Type.__name__ = "OctetString"
_Device_config_token_Object = MibScalar
device_config_token = _Device_config_token_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 1, 28),
    _Device_config_token_Type()
)
device_config_token.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    device_config_token.setStatus("optional")
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
              2)
        )
    )
    namedValues = NamedValues(
        *(("eOffline", 2),
          ("eOnline", 1))
    )


_On_off_line_Type.__name__ = "Integer32"
_On_off_line_Object = MibScalar
on_off_line = _On_off_line_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 2, 5),
    _On_off_line_Type()
)
on_off_line.setMaxAccess("read-only")
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


class _Install_date_Type(DisplayString):
    """Custom type install_date based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_Install_date_Type.__name__ = "DisplayString"
_Install_date_Object = MibScalar
install_date = _Install_date_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 2, 8),
    _Install_date_Type()
)
install_date.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    install_date.setStatus("optional")
_Date_and_time_Type = OctetString
_Date_and_time_Object = MibScalar
date_and_time = _Date_and_time_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 2, 17),
    _Date_and_time_Type()
)
date_and_time.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    date_and_time.setStatus("optional")


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
_Collated_originals_support_Type = OctetString
_Collated_originals_support_Object = MibScalar
collated_originals_support = _Collated_originals_support_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 2, 42),
    _Collated_originals_support_Type()
)
collated_originals_support.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    collated_originals_support.setStatus("optional")
_Device_cfg_download_error_Type = Integer32
_Device_cfg_download_error_Object = MibScalar
device_cfg_download_error = _Device_cfg_download_error_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 2, 43),
    _Device_cfg_download_error_Type()
)
device_cfg_download_error.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    device_cfg_download_error.setStatus("optional")
_Device_cfg_upload_error_Type = Integer32
_Device_cfg_upload_error_Object = MibScalar
device_cfg_upload_error = _Device_cfg_upload_error_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 2, 45),
    _Device_cfg_upload_error_Type()
)
device_cfg_upload_error.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    device_cfg_upload_error.setStatus("optional")
_Id_ObjectIdentity = ObjectIdentity
id = _Id_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 3)
)
_Model_name_Type = DisplayString
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
_Fax_local_phone_num_Type = DisplayString
_Fax_local_phone_num_Object = MibScalar
fax_local_phone_num = _Fax_local_phone_num_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 3, 8),
    _Fax_local_phone_num_Type()
)
fax_local_phone_num.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fax_local_phone_num.setStatus("optional")
_Fax_station_name_Type = DisplayString
_Fax_station_name_Object = MibScalar
fax_station_name = _Fax_station_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 3, 9),
    _Fax_station_name_Type()
)
fax_station_name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fax_station_name.setStatus("optional")
_Device_name_Type = DisplayString
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


class _Fax_line_interface_unit_id_Type(Integer32):
    """Custom type fax_line_interface_unit_id based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_Fax_line_interface_unit_id_Type.__name__ = "Integer32"
_Fax_line_interface_unit_id_Object = MibScalar
fax_line_interface_unit_id = _Fax_line_interface_unit_id_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 3, 18),
    _Fax_line_interface_unit_id_Type()
)
fax_line_interface_unit_id.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fax_line_interface_unit_id.setStatus("optional")
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("eEmpty", 1),
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
              4,
              8,
              11,
              12,
              350,
              450)
        )
    )
    namedValues = NamedValues(
        *(("eDeviceDemoPage1ConfigurationPage", 3),
          ("eDeviceDemoPage2", 4),
          ("eDeviceDemoPage6FileSystemDirectoryListing", 8),
          ("eDeviceDemoPage8BlockFaxList", 11),
          ("eDeviceDemoPage9BlockFaxLogReport", 12),
          ("eNotPrintingAnInternalPage", 1),
          ("ePCLFontList1", 350),
          ("ePostScriptFontList1", 450),
          ("ePrintingAnUnknownInternalPage", 2))
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
_Job_ObjectIdentity = ObjectIdentity
job = _Job_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6)
)
_Settings_job_ObjectIdentity = ObjectIdentity
settings_job = _Settings_job_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 1)
)
_Cancel_job_Type = Integer32
_Cancel_job_Object = MibScalar
cancel_job = _Cancel_job_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 1, 2),
    _Cancel_job_Type()
)
cancel_job.setMaxAccess("read-write")
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
        ValueRangeConstraint(-1, 32767),
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
_Fax_job_control_ObjectIdentity = ObjectIdentity
fax_job_control = _Fax_job_control_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 3)
)
_Settings_fax_job_ObjectIdentity = ObjectIdentity
settings_fax_job = _Settings_fax_job_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 3, 1)
)


class _Faxjob_action_Type(Integer32):
    """Custom type faxjob_action based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("eDeleteFaxFromMemory", 3),
          ("ePrintFaxToPrinter", 1))
    )


_Faxjob_action_Type.__name__ = "Integer32"
_Faxjob_action_Object = MibScalar
faxjob_action = _Faxjob_action_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 3, 1, 1),
    _Faxjob_action_Type()
)
faxjob_action.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    faxjob_action.setStatus("optional")
_Faxjob_action_id_Type = Integer32
_Faxjob_action_id_Object = MibScalar
faxjob_action_id = _Faxjob_action_id_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 3, 1, 2),
    _Faxjob_action_id_Type()
)
faxjob_action_id.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    faxjob_action_id.setStatus("optional")


class _Faxjob_tx_type_Type(Integer32):
    """Custom type faxjob_tx_type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              5,
              9)
        )
    )
    namedValues = NamedValues(
        *(("eSrcHostOnly", 2),
          ("eSrcHostToMemoryOnly", 9),
          ("eSrcScannerOnly", 5))
    )


_Faxjob_tx_type_Type.__name__ = "Integer32"
_Faxjob_tx_type_Object = MibScalar
faxjob_tx_type = _Faxjob_tx_type_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 3, 1, 3),
    _Faxjob_tx_type_Type()
)
faxjob_tx_type.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    faxjob_tx_type.setStatus("optional")
_Status_fax_job_ObjectIdentity = ObjectIdentity
status_fax_job = _Status_fax_job_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 3, 2)
)
_Faxjob_download_id_Type = Integer32
_Faxjob_download_id_Object = MibScalar
faxjob_download_id = _Faxjob_download_id_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 3, 2, 1),
    _Faxjob_download_id_Type()
)
faxjob_download_id.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    faxjob_download_id.setStatus("optional")
_Faxjob_rx_id_Type = Integer32
_Faxjob_rx_id_Object = MibScalar
faxjob_rx_id = _Faxjob_rx_id_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 3, 2, 2),
    _Faxjob_rx_id_Type()
)
faxjob_rx_id.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    faxjob_rx_id.setStatus("optional")
_Faxjob_tx_id_Type = Integer32
_Faxjob_tx_id_Object = MibScalar
faxjob_tx_id = _Faxjob_tx_id_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 3, 2, 3),
    _Faxjob_tx_id_Type()
)
faxjob_tx_id.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    faxjob_tx_id.setStatus("optional")
_Faxjob_upload_id_Type = Integer32
_Faxjob_upload_id_Object = MibScalar
faxjob_upload_id = _Faxjob_upload_id_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 3, 2, 4),
    _Faxjob_upload_id_Type()
)
faxjob_upload_id.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    faxjob_upload_id.setStatus("optional")
_Faxjob_ObjectIdentity = ObjectIdentity
faxjob = _Faxjob_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 3, 3)
)
_Faxjob_rx_status_ObjectIdentity = ObjectIdentity
faxjob_rx_status = _Faxjob_rx_status_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 3, 3, 1)
)


class _Faxjob_rx_status_1_Type(Integer32):
    """Custom type faxjob_rx_status_1 based on Integer32"""
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
        *(("eFaxRxAnswering", 3),
          ("eFaxRxIdle", 1),
          ("eFaxRxReceiving", 4),
          ("eFaxRxRinging", 2))
    )


_Faxjob_rx_status_1_Type.__name__ = "Integer32"
_Faxjob_rx_status_1_Object = MibScalar
faxjob_rx_status_1 = _Faxjob_rx_status_1_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 3, 3, 1, 1),
    _Faxjob_rx_status_1_Type()
)
faxjob_rx_status_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    faxjob_rx_status_1.setStatus("optional")
_Faxjob_tx_status_ObjectIdentity = ObjectIdentity
faxjob_tx_status = _Faxjob_tx_status_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 3, 3, 3)
)


class _Faxjob_tx_status_1_Type(Integer32):
    """Custom type faxjob_tx_status_1 based on Integer32"""
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
        *(("eFaxTxConnecting", 3),
          ("eFaxTxDialing", 2),
          ("eFaxTxIdle", 1),
          ("eFaxTxTransmitting", 4))
    )


_Faxjob_tx_status_1_Type.__name__ = "Integer32"
_Faxjob_tx_status_1_Object = MibScalar
faxjob_tx_status_1 = _Faxjob_tx_status_1_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 3, 3, 3, 1),
    _Faxjob_tx_status_1_Type()
)
faxjob_tx_status_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    faxjob_tx_status_1.setStatus("optional")
_Faxjob_tx_error_ObjectIdentity = ObjectIdentity
faxjob_tx_error = _Faxjob_tx_error_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 3, 3, 4)
)
_Faxjob_tx_error_1_Type = Integer32
_Faxjob_tx_error_1_Object = MibScalar
faxjob_tx_error_1 = _Faxjob_tx_error_1_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 3, 3, 4, 1),
    _Faxjob_tx_error_1_Type()
)
faxjob_tx_error_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    faxjob_tx_error_1.setStatus("optional")
_Faxjob_tx_current_page_ObjectIdentity = ObjectIdentity
faxjob_tx_current_page = _Faxjob_tx_current_page_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 3, 3, 5)
)
_Faxjob_tx_current_page_1_Type = Integer32
_Faxjob_tx_current_page_1_Object = MibScalar
faxjob_tx_current_page_1 = _Faxjob_tx_current_page_1_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 3, 3, 5, 1),
    _Faxjob_tx_current_page_1_Type()
)
faxjob_tx_current_page_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    faxjob_tx_current_page_1.setStatus("optional")
_Faxjob_rx_current_page_ObjectIdentity = ObjectIdentity
faxjob_rx_current_page = _Faxjob_rx_current_page_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 3, 3, 6)
)
_Faxjob_rx_current_page_1_Type = Integer32
_Faxjob_rx_current_page_1_Object = MibScalar
faxjob_rx_current_page_1 = _Faxjob_rx_current_page_1_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 3, 3, 6, 1),
    _Faxjob_rx_current_page_1_Type()
)
faxjob_rx_current_page_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    faxjob_rx_current_page_1.setStatus("optional")
_Faxjob_rx_duration_ObjectIdentity = ObjectIdentity
faxjob_rx_duration = _Faxjob_rx_duration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 3, 3, 7)
)
_Faxjob_rx_duration_1_Type = Integer32
_Faxjob_rx_duration_1_Object = MibScalar
faxjob_rx_duration_1 = _Faxjob_rx_duration_1_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 3, 3, 7, 1),
    _Faxjob_rx_duration_1_Type()
)
faxjob_rx_duration_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    faxjob_rx_duration_1.setStatus("optional")
_Faxjob_tx_duration_ObjectIdentity = ObjectIdentity
faxjob_tx_duration = _Faxjob_tx_duration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 3, 3, 8)
)
_Faxjob_tx_duration_1_Type = Integer32
_Faxjob_tx_duration_1_Object = MibScalar
faxjob_tx_duration_1 = _Faxjob_tx_duration_1_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 3, 3, 8, 1),
    _Faxjob_tx_duration_1_Type()
)
faxjob_tx_duration_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    faxjob_tx_duration_1.setStatus("optional")
_Fax_activity_log_ObjectIdentity = ObjectIdentity
fax_activity_log = _Fax_activity_log_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 4)
)
_Settings_faxlog_ObjectIdentity = ObjectIdentity
settings_faxlog = _Settings_faxlog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 4, 1)
)


class _Fax_log_action_Type(Integer32):
    """Custom type fax_log_action based on Integer32"""
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
        *(("eClear", 2),
          ("eIdle", 1),
          ("ePrintAll", 4),
          ("ePrintLatest", 3))
    )


_Fax_log_action_Type.__name__ = "Integer32"
_Fax_log_action_Object = MibScalar
fax_log_action = _Fax_log_action_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 4, 1, 1),
    _Fax_log_action_Type()
)
fax_log_action.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fax_log_action.setStatus("optional")


class _Fax_log_reporting_Type(Integer32):
    """Custom type fax_log_reporting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("eErrorOnly", 2),
          ("eNever", 1),
          ("eSendOnly", 3))
    )


_Fax_log_reporting_Type.__name__ = "Integer32"
_Fax_log_reporting_Object = MibScalar
fax_log_reporting = _Fax_log_reporting_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 4, 1, 2),
    _Fax_log_reporting_Type()
)
fax_log_reporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fax_log_reporting.setStatus("optional")
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("eAborted", 3),
          ("eCancelled", 10),
          ("ePrinted", 5),
          ("eProcessing", 11),
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
_Phone_ObjectIdentity = ObjectIdentity
phone = _Phone_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 9)
)
_Dial_ObjectIdentity = ObjectIdentity
dial = _Dial_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 9, 1)
)
_Dial_all_lines_ObjectIdentity = ObjectIdentity
dial_all_lines = _Dial_all_lines_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 9, 1, 1)
)


class _Fax_dial_mode_Type(Integer32):
    """Custom type fax_dial_mode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ePulseDial", 2),
          ("eToneDial", 1))
    )


_Fax_dial_mode_Type.__name__ = "Integer32"
_Fax_dial_mode_Object = MibScalar
fax_dial_mode = _Fax_dial_mode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 9, 1, 1, 1),
    _Fax_dial_mode_Type()
)
fax_dial_mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fax_dial_mode.setStatus("optional")
_Device_redial_Type = OctetString
_Device_redial_Object = MibScalar
device_redial = _Device_redial_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 9, 1, 1, 2),
    _Device_redial_Type()
)
device_redial.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    device_redial.setStatus("optional")


class _Fax_pulse_dial_support_Type(Integer32):
    """Custom type fax_pulse_dial_support based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eNotSupported", 2),
          ("eSupported", 1))
    )


_Fax_pulse_dial_support_Type.__name__ = "Integer32"
_Fax_pulse_dial_support_Object = MibScalar
fax_pulse_dial_support = _Fax_pulse_dial_support_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 9, 1, 1, 3),
    _Fax_pulse_dial_support_Type()
)
fax_pulse_dial_support.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fax_pulse_dial_support.setStatus("optional")
_Answer_ObjectIdentity = ObjectIdentity
answer = _Answer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 9, 2)
)
_Answer_all_lines_ObjectIdentity = ObjectIdentity
answer_all_lines = _Answer_all_lines_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 9, 2, 1)
)


class _Fax_answer_mode_Type(Integer32):
    """Custom type fax_answer_mode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eFaxAnswer", 2),
          ("eManualAnswer", 1))
    )


_Fax_answer_mode_Type.__name__ = "Integer32"
_Fax_answer_mode_Object = MibScalar
fax_answer_mode = _Fax_answer_mode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 9, 2, 1, 1),
    _Fax_answer_mode_Type()
)
fax_answer_mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fax_answer_mode.setStatus("optional")


class _Fax_num_rings_pickup_Type(Integer32):
    """Custom type fax_num_rings_pickup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_Fax_num_rings_pickup_Type.__name__ = "Integer32"
_Fax_num_rings_pickup_Object = MibScalar
fax_num_rings_pickup = _Fax_num_rings_pickup_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 9, 2, 1, 2),
    _Fax_num_rings_pickup_Type()
)
fax_num_rings_pickup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fax_num_rings_pickup.setStatus("optional")
_Device_ring_type_pickup_Type = OctetString
_Device_ring_type_pickup_Object = MibScalar
device_ring_type_pickup = _Device_ring_type_pickup_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 9, 2, 1, 3),
    _Device_ring_type_pickup_Type()
)
device_ring_type_pickup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    device_ring_type_pickup.setStatus("optional")
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
_Scanner_ObjectIdentity = ObjectIdentity
scanner = _Scanner_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2)
)
_Settings_scanner_ObjectIdentity = ObjectIdentity
settings_scanner = _Settings_scanner_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 1)
)


class _Scan_contrast_Type(Integer32):
    """Custom type scan_contrast based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-127, 127),
    )


_Scan_contrast_Type.__name__ = "Integer32"
_Scan_contrast_Object = MibScalar
scan_contrast = _Scan_contrast_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 1, 1),
    _Scan_contrast_Type()
)
scan_contrast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scan_contrast.setStatus("optional")


class _Scan_resolution_Type(OctetString):
    """Custom type scan_resolution based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_Scan_resolution_Type.__name__ = "OctetString"
_Scan_resolution_Object = MibScalar
scan_resolution = _Scan_resolution_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 1, 2),
    _Scan_resolution_Type()
)
scan_resolution.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scan_resolution.setStatus("optional")


class _Scan_pixel_data_type_Type(Integer32):
    """Custom type scan_pixel_data_type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              8,
              24)
        )
    )
    namedValues = NamedValues(
        *(("e24BitColor", 24),
          ("eBiLevelThesholded", 1),
          ("eGrey256", 8))
    )


_Scan_pixel_data_type_Type.__name__ = "Integer32"
_Scan_pixel_data_type_Object = MibScalar
scan_pixel_data_type = _Scan_pixel_data_type_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 1, 3),
    _Scan_pixel_data_type_Type()
)
scan_pixel_data_type.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scan_pixel_data_type.setStatus("optional")


class _Scan_compression_Type(Integer32):
    """Custom type scan_compression based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("eCompressDefault", 2),
          ("eCompressNone", 1),
          ("eCompressionJPEG", 6),
          ("eCompressionMMR", 5))
    )


_Scan_compression_Type.__name__ = "Integer32"
_Scan_compression_Object = MibScalar
scan_compression = _Scan_compression_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 1, 4),
    _Scan_compression_Type()
)
scan_compression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scan_compression.setStatus("optional")


class _Scan_compression_factor_Type(Integer32):
    """Custom type scan_compression_factor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Scan_compression_factor_Type.__name__ = "Integer32"
_Scan_compression_factor_Object = MibScalar
scan_compression_factor = _Scan_compression_factor_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 1, 5),
    _Scan_compression_factor_Type()
)
scan_compression_factor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scan_compression_factor.setStatus("optional")
_Scan_upload_error_Type = Integer32
_Scan_upload_error_Object = MibScalar
scan_upload_error = _Scan_upload_error_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 1, 6),
    _Scan_upload_error_Type()
)
scan_upload_error.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scan_upload_error.setStatus("optional")


class _Scan_upload_Type(Integer32):
    """Custom type scan_upload based on Integer32"""
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
        *(("eScanUploadAborted", 4),
          ("eScanUploadActive", 3),
          ("eScanUploadDone", 5),
          ("eScanUploadIdle", 1),
          ("eScanUploadNewPage", 6),
          ("eScanUploadStart", 2))
    )


_Scan_upload_Type.__name__ = "Integer32"
_Scan_upload_Object = MibScalar
scan_upload = _Scan_upload_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 1, 12),
    _Scan_upload_Type()
)
scan_upload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scan_upload.setStatus("optional")


class _Default_scanner_margin_left_Type(Integer32):
    """Custom type default_scanner_margin_left based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5088),
    )


_Default_scanner_margin_left_Type.__name__ = "Integer32"
_Default_scanner_margin_left_Object = MibScalar
default_scanner_margin_left = _Default_scanner_margin_left_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 1, 16),
    _Default_scanner_margin_left_Type()
)
default_scanner_margin_left.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    default_scanner_margin_left.setStatus("optional")


class _Default_scanner_margin_right_Type(Integer32):
    """Custom type default_scanner_margin_right based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 5120),
    )


_Default_scanner_margin_right_Type.__name__ = "Integer32"
_Default_scanner_margin_right_Object = MibScalar
default_scanner_margin_right = _Default_scanner_margin_right_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 1, 17),
    _Default_scanner_margin_right_Type()
)
default_scanner_margin_right.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    default_scanner_margin_right.setStatus("optional")
_Scan_calibration_ObjectIdentity = ObjectIdentity
scan_calibration = _Scan_calibration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 1, 32)
)


class _Scan_calibration_target_Type(Integer32):
    """Custom type scan_calibration_target based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ePlaten", 2),
          ("eWhiteSheet", 1))
    )


_Scan_calibration_target_Type.__name__ = "Integer32"
_Scan_calibration_target_Object = MibScalar
scan_calibration_target = _Scan_calibration_target_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 1, 32, 18),
    _Scan_calibration_target_Type()
)
scan_calibration_target.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scan_calibration_target.setStatus("optional")
_Ui_add_option_Type = DisplayString
_Ui_add_option_Object = MibScalar
ui_add_option = _Ui_add_option_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 1, 37),
    _Ui_add_option_Type()
)
ui_add_option.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    ui_add_option.setStatus("optional")
_Ui_select_option_Type = DisplayString
_Ui_select_option_Object = MibScalar
ui_select_option = _Ui_select_option_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 1, 38),
    _Ui_select_option_Type()
)
ui_select_option.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ui_select_option.setStatus("optional")
_Ui_delete_option_Type = DisplayString
_Ui_delete_option_Object = MibScalar
ui_delete_option = _Ui_delete_option_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 1, 42),
    _Ui_delete_option_Type()
)
ui_delete_option.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    ui_delete_option.setStatus("optional")
_Scanner_jam_page_count_Type = Integer32
_Scanner_jam_page_count_Object = MibScalar
scanner_jam_page_count = _Scanner_jam_page_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 1, 43),
    _Scanner_jam_page_count_Type()
)
scanner_jam_page_count.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scanner_jam_page_count.setStatus("optional")
_Scanner_adf_page_count_Type = Integer32
_Scanner_adf_page_count_Object = MibScalar
scanner_adf_page_count = _Scanner_adf_page_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 1, 44),
    _Scanner_adf_page_count_Type()
)
scanner_adf_page_count.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scanner_adf_page_count.setStatus("optional")
_Scan_adf_page_count_Type = Integer32
_Scan_adf_page_count_Object = MibScalar
scan_adf_page_count = _Scan_adf_page_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 1, 45),
    _Scan_adf_page_count_Type()
)
scan_adf_page_count.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scan_adf_page_count.setStatus("optional")


class _Scan_image_type_Type(Integer32):
    """Custom type scan_image_type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("eMixed", 3),
          ("ePhoto", 2),
          ("eText", 1))
    )


_Scan_image_type_Type.__name__ = "Integer32"
_Scan_image_type_Object = MibScalar
scan_image_type = _Scan_image_type_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 1, 46),
    _Scan_image_type_Type()
)
scan_image_type.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scan_image_type.setStatus("optional")


class _Scan_subsample_Type(Integer32):
    """Custom type scan_subsample based on Integer32"""
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
        *(("eFourToFourToFour", 4),
          ("eFourToOneToOne", 1),
          ("eFourToThreeToThree", 3),
          ("eFourToTwoToTwo", 2))
    )


_Scan_subsample_Type.__name__ = "Integer32"
_Scan_subsample_Object = MibScalar
scan_subsample = _Scan_subsample_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 1, 47),
    _Scan_subsample_Type()
)
scan_subsample.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scan_subsample.setStatus("optional")
_Scanner_retrieve_scanline_Type = OctetString
_Scanner_retrieve_scanline_Object = MibScalar
scanner_retrieve_scanline = _Scanner_retrieve_scanline_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 1, 48),
    _Scanner_retrieve_scanline_Type()
)
scanner_retrieve_scanline.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scanner_retrieve_scanline.setStatus("optional")


class _Scanner_motor_control_Type(Integer32):
    """Custom type scanner_motor_control based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-240, 4680),
    )


_Scanner_motor_control_Type.__name__ = "Integer32"
_Scanner_motor_control_Object = MibScalar
scanner_motor_control = _Scanner_motor_control_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 1, 49),
    _Scanner_motor_control_Type()
)
scanner_motor_control.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scanner_motor_control.setStatus("optional")


class _Scan_height_Type(Integer32):
    """Custom type scan_height based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 25200),
    )


_Scan_height_Type.__name__ = "Integer32"
_Scan_height_Object = MibScalar
scan_height = _Scan_height_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 1, 50),
    _Scan_height_Type()
)
scan_height.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scan_height.setStatus("optional")
_Scanner_scanline_statistics_Type = DisplayString
_Scanner_scanline_statistics_Object = MibScalar
scanner_scanline_statistics = _Scanner_scanline_statistics_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 1, 51),
    _Scanner_scanline_statistics_Type()
)
scanner_scanline_statistics.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scanner_scanline_statistics.setStatus("optional")
_Scan_control_descriptor_Type = DisplayString
_Scan_control_descriptor_Object = MibScalar
scan_control_descriptor = _Scan_control_descriptor_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 1, 52),
    _Scan_control_descriptor_Type()
)
scan_control_descriptor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scan_control_descriptor.setStatus("optional")


class _Scan_gamma_correction_Type(OctetString):
    """Custom type scan_gamma_correction based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Scan_gamma_correction_Type.__name__ = "OctetString"
_Scan_gamma_correction_Object = MibScalar
scan_gamma_correction = _Scan_gamma_correction_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 1, 53),
    _Scan_gamma_correction_Type()
)
scan_gamma_correction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scan_gamma_correction.setStatus("optional")


class _Scan_pad_image_Type(Integer32):
    """Custom type scan_pad_image based on Integer32"""
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


_Scan_pad_image_Type.__name__ = "Integer32"
_Scan_pad_image_Object = MibScalar
scan_pad_image = _Scan_pad_image_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 1, 54),
    _Scan_pad_image_Type()
)
scan_pad_image.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scan_pad_image.setStatus("optional")
_Scan_flatbed_page_count_Type = Integer32
_Scan_flatbed_page_count_Object = MibScalar
scan_flatbed_page_count = _Scan_flatbed_page_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 1, 73),
    _Scan_flatbed_page_count_Type()
)
scan_flatbed_page_count.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scan_flatbed_page_count.setStatus("optional")
_Scanner_flatbed_page_count_Type = Integer32
_Scanner_flatbed_page_count_Object = MibScalar
scanner_flatbed_page_count = _Scanner_flatbed_page_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 1, 74),
    _Scanner_flatbed_page_count_Type()
)
scanner_flatbed_page_count.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scanner_flatbed_page_count.setStatus("optional")
_Scanner_modular_hardware_Type = OctetString
_Scanner_modular_hardware_Object = MibScalar
scanner_modular_hardware = _Scanner_modular_hardware_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 1, 75),
    _Scanner_modular_hardware_Type()
)
scanner_modular_hardware.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scanner_modular_hardware.setStatus("optional")


class _Default_scanner_margin_top_Type(Integer32):
    """Custom type default_scanner_margin_top based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 720),
    )


_Default_scanner_margin_top_Type.__name__ = "Integer32"
_Default_scanner_margin_top_Object = MibScalar
default_scanner_margin_top = _Default_scanner_margin_top_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 1, 76),
    _Default_scanner_margin_top_Type()
)
default_scanner_margin_top.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    default_scanner_margin_top.setStatus("optional")
_Scan_max_line_width_Type = Integer32
_Scan_max_line_width_Object = MibScalar
scan_max_line_width = _Scan_max_line_width_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 1, 77),
    _Scan_max_line_width_Type()
)
scan_max_line_width.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scan_max_line_width.setStatus("optional")
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
_Scan_resolution_range_Type = DisplayString
_Scan_resolution_range_Object = MibScalar
scan_resolution_range = _Scan_resolution_range_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 2, 3),
    _Scan_resolution_range_Type()
)
scan_resolution_range.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scan_resolution_range.setStatus("optional")
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


class _Scanner_button_status_Type(Integer32):
    """Custom type scanner_button_status based on Integer32"""
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


_Scanner_button_status_Type.__name__ = "Integer32"
_Scanner_button_status_Object = MibScalar
scanner_button_status = _Scanner_button_status_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 2, 7),
    _Scanner_button_status_Type()
)
scanner_button_status.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scanner_button_status.setStatus("optional")
_Scanner_lamp_gain_value_Type = DisplayString
_Scanner_lamp_gain_value_Object = MibScalar
scanner_lamp_gain_value = _Scanner_lamp_gain_value_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 2, 8),
    _Scanner_lamp_gain_value_Type()
)
scanner_lamp_gain_value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scanner_lamp_gain_value.setStatus("optional")
_Scanner_light_monitor_window_Type = DisplayString
_Scanner_light_monitor_window_Object = MibScalar
scanner_light_monitor_window = _Scanner_light_monitor_window_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 2, 9),
    _Scanner_light_monitor_window_Type()
)
scanner_light_monitor_window.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scanner_light_monitor_window.setStatus("optional")
_Scanner_reference_position_Type = DisplayString
_Scanner_reference_position_Object = MibScalar
scanner_reference_position = _Scanner_reference_position_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 2, 10),
    _Scanner_reference_position_Type()
)
scanner_reference_position.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scanner_reference_position.setStatus("optional")
_Scanner_sensor_manufacturer_Type = DisplayString
_Scanner_sensor_manufacturer_Object = MibScalar
scanner_sensor_manufacturer = _Scanner_sensor_manufacturer_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 2, 11),
    _Scanner_sensor_manufacturer_Type()
)
scanner_sensor_manufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scanner_sensor_manufacturer.setStatus("optional")
_Fax_receive_ObjectIdentity = ObjectIdentity
fax_receive = _Fax_receive_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 3)
)
_Settings_fax_receive_ObjectIdentity = ObjectIdentity
settings_fax_receive = _Settings_fax_receive_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 3, 1)
)


class _Fax_receive_stamping_enable_Type(Integer32):
    """Custom type fax_receive_stamping_enable based on Integer32"""
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


_Fax_receive_stamping_enable_Type.__name__ = "Integer32"
_Fax_receive_stamping_enable_Object = MibScalar
fax_receive_stamping_enable = _Fax_receive_stamping_enable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 3, 1, 1),
    _Fax_receive_stamping_enable_Type()
)
fax_receive_stamping_enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fax_receive_stamping_enable.setStatus("optional")
_Status_fax_receive_ObjectIdentity = ObjectIdentity
status_fax_receive = _Status_fax_receive_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 3, 2)
)
_Not_ready_fax_receive_Type = OctetString
_Not_ready_fax_receive_Object = MibScalar
not_ready_fax_receive = _Not_ready_fax_receive_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 3, 2, 1),
    _Not_ready_fax_receive_Type()
)
not_ready_fax_receive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    not_ready_fax_receive.setStatus("optional")
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


class _Default_copies_Type(Integer32):
    """Custom type default_copies based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 999),
    )


_Default_copies_Type.__name__ = "Integer32"
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
_Maximum_resource_saving_memory_Type = Integer32
_Maximum_resource_saving_memory_Object = MibScalar
maximum_resource_saving_memory = _Maximum_resource_saving_memory_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 3, 1, 7),
    _Maximum_resource_saving_memory_Type()
)
maximum_resource_saving_memory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maximum_resource_saving_memory.setStatus("optional")
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
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("eAuto", 3),
          ("eOn", 2))
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
              17,
              25,
              26,
              45,
              71,
              72,
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
          ("eFoolscap", 10),
          ("eISOandJISA4", 26),
          ("eISOandJISA5", 25),
          ("eInternationalB5", 100),
          ("eInternationalC5", 91),
          ("eInternationalDL", 90),
          ("eJISB5", 45),
          ("eJapanesePostcardDouble", 72),
          ("eJapanesePostcardSingle", 71),
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


class _Wide_a4_Type(Integer32):
    """Custom type wide_a4 based on Integer32"""
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


_Wide_a4_Type.__name__ = "Integer32"
_Wide_a4_Object = MibScalar
wide_a4 = _Wide_a4_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 3, 1, 37),
    _Wide_a4_Type()
)
wide_a4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wide_a4.setStatus("optional")


class _Dark_courier_Type(Integer32):
    """Custom type dark_courier based on Integer32"""
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


_Dark_courier_Type.__name__ = "Integer32"
_Dark_courier_Object = MibScalar
dark_courier = _Dark_courier_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 3, 1, 38),
    _Dark_courier_Type()
)
dark_courier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dark_courier.setStatus("optional")
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
_Pcl_resource_saving_memory_size_Type = Integer32
_Pcl_resource_saving_memory_size_Object = MibScalar
pcl_resource_saving_memory_size = _Pcl_resource_saving_memory_size_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 3, 3, 2),
    _Pcl_resource_saving_memory_size_Type()
)
pcl_resource_saving_memory_size.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pcl_resource_saving_memory_size.setStatus("optional")
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("eInternal", 1),
          ("ePermanentSoft", 2),
          ("eRomSimm1", 10))
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
_Fax_rxscale_Type = Integer32
_Fax_rxscale_Object = MibScalar
fax_rxscale = _Fax_rxscale_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 7, 1, 1),
    _Fax_rxscale_Type()
)
fax_rxscale.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fax_rxscale.setStatus("optional")


class _Fax_noise_volume_Type(Integer32):
    """Custom type fax_noise_volume based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_Fax_noise_volume_Type.__name__ = "Integer32"
_Fax_noise_volume_Object = MibScalar
fax_noise_volume = _Fax_noise_volume_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 7, 1, 3),
    _Fax_noise_volume_Type()
)
fax_noise_volume.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fax_noise_volume.setStatus("optional")


class _Fax_download_Type(Integer32):
    """Custom type fax_download based on Integer32"""
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
        *(("eFaxDownloadAborted", 4),
          ("eFaxDownloadActive", 3),
          ("eFaxDownloadDone", 5),
          ("eFaxDownloadIdle", 1),
          ("eFaxDownloadStart", 2))
    )


_Fax_download_Type.__name__ = "Integer32"
_Fax_download_Object = MibScalar
fax_download = _Fax_download_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 7, 1, 6),
    _Fax_download_Type()
)
fax_download.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fax_download.setStatus("optional")


class _Fax_silent_detection_Type(Integer32):
    """Custom type fax_silent_detection based on Integer32"""
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


_Fax_silent_detection_Type.__name__ = "Integer32"
_Fax_silent_detection_Object = MibScalar
fax_silent_detection = _Fax_silent_detection_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 7, 1, 7),
    _Fax_silent_detection_Type()
)
fax_silent_detection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fax_silent_detection.setStatus("optional")


class _Fax_ring_enable_Type(Integer32):
    """Custom type fax_ring_enable based on Integer32"""
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


_Fax_ring_enable_Type.__name__ = "Integer32"
_Fax_ring_enable_Object = MibScalar
fax_ring_enable = _Fax_ring_enable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 7, 1, 8),
    _Fax_ring_enable_Type()
)
fax_ring_enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fax_ring_enable.setStatus("optional")


class _Fax_country_Type(Integer32):
    """Custom type fax_country based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(6,
              13,
              14,
              15,
              19,
              21,
              23,
              27,
              29,
              30,
              31,
              34,
              35,
              37,
              39,
              40,
              41,
              43,
              44,
              45,
              46,
              47,
              51,
              55,
              56,
              62,
              63,
              64)
        )
    )
    namedValues = NamedValues(
        *(("eAustralia", 23),
          ("eAustria", 34),
          ("eBelgium", 45),
          ("eCanadaFrench", 14),
          ("eChina", 6),
          ("eDenmark", 40),
          ("eFinland", 46),
          ("eFrance", 47),
          ("eGermany", 39),
          ("eHongKong", 29),
          ("eHungary", 62),
          ("eIreland", 44),
          ("eIsrael", 21),
          ("eItaly", 51),
          ("eMalaysia", 27),
          ("eMexicoAndLatinAmerica", 13),
          ("eNetherlands", 35),
          ("eNewZealand", 19),
          ("eNorway", 43),
          ("ePoland", 56),
          ("eRussia", 64),
          ("eSingapore", 30),
          ("eSpain", 55),
          ("eSweden", 41),
          ("eSwitzerlandFrench", 37),
          ("eUkraine", 63),
          ("eUnitedKingdom", 31),
          ("eUnitedStatesAndCanadaEnglish", 15))
    )


_Fax_country_Type.__name__ = "Integer32"
_Fax_country_Object = MibScalar
fax_country = _Fax_country_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 7, 1, 9),
    _Fax_country_Type()
)
fax_country.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fax_country.setStatus("optional")
_Fax_tx_phone_number_Type = DisplayString
_Fax_tx_phone_number_Object = MibScalar
fax_tx_phone_number = _Fax_tx_phone_number_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 7, 1, 10),
    _Fax_tx_phone_number_Type()
)
fax_tx_phone_number.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    fax_tx_phone_number.setStatus("optional")
_Fax_redial_time_Type = Integer32
_Fax_redial_time_Object = MibScalar
fax_redial_time = _Fax_redial_time_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 7, 1, 14),
    _Fax_redial_time_Type()
)
fax_redial_time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fax_redial_time.setStatus("optional")
_Fax_pstn_access_code_Type = DisplayString
_Fax_pstn_access_code_Object = MibScalar
fax_pstn_access_code = _Fax_pstn_access_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 7, 1, 18),
    _Fax_pstn_access_code_Type()
)
fax_pstn_access_code.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fax_pstn_access_code.setStatus("optional")


class _Fax_rx_disposition_Type(Integer32):
    """Custom type fax_rx_disposition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("eForwardElsePrint", 6),
          ("ePrintOnly", 1),
          ("eUploadElsePrint", 4),
          ("eUploadOnly", 2))
    )


_Fax_rx_disposition_Type.__name__ = "Integer32"
_Fax_rx_disposition_Object = MibScalar
fax_rx_disposition = _Fax_rx_disposition_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 7, 1, 19),
    _Fax_rx_disposition_Type()
)
fax_rx_disposition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fax_rx_disposition.setStatus("optional")


class _Fax_error_correction_mode_Type(Integer32):
    """Custom type fax_error_correction_mode based on Integer32"""
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


_Fax_error_correction_mode_Type.__name__ = "Integer32"
_Fax_error_correction_mode_Object = MibScalar
fax_error_correction_mode = _Fax_error_correction_mode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 7, 1, 21),
    _Fax_error_correction_mode_Type()
)
fax_error_correction_mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fax_error_correction_mode.setStatus("optional")


class _Fax_report_transmission_Type(Integer32):
    """Custom type fax_report_transmission based on Integer32"""
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
        *(("eNone", 1),
          ("ePrintReport", 2),
          ("ePrintReportOnError", 4),
          ("ePrintReportOnReceiveError", 6),
          ("ePrintReportOnSend", 3),
          ("ePrintReportOnSendError", 5))
    )


_Fax_report_transmission_Type.__name__ = "Integer32"
_Fax_report_transmission_Object = MibScalar
fax_report_transmission = _Fax_report_transmission_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 7, 1, 22),
    _Fax_report_transmission_Type()
)
fax_report_transmission.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fax_report_transmission.setStatus("optional")


class _Fax_report_activity_log_Type(Integer32):
    """Custom type fax_report_activity_log based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eNever", 1),
          ("eThreshold", 2))
    )


_Fax_report_activity_log_Type.__name__ = "Integer32"
_Fax_report_activity_log_Object = MibScalar
fax_report_activity_log = _Fax_report_activity_log_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 7, 1, 23),
    _Fax_report_activity_log_Type()
)
fax_report_activity_log.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fax_report_activity_log.setStatus("optional")


class _Fax_dial_tone_detection_Type(Integer32):
    """Custom type fax_dial_tone_detection based on Integer32"""
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


_Fax_dial_tone_detection_Type.__name__ = "Integer32"
_Fax_dial_tone_detection_Object = MibScalar
fax_dial_tone_detection = _Fax_dial_tone_detection_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 7, 1, 24),
    _Fax_dial_tone_detection_Type()
)
fax_dial_tone_detection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fax_dial_tone_detection.setStatus("optional")


class _Fax_alarm_volume_Type(Integer32):
    """Custom type fax_alarm_volume based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Fax_alarm_volume_Type.__name__ = "Integer32"
_Fax_alarm_volume_Object = MibScalar
fax_alarm_volume = _Fax_alarm_volume_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 7, 1, 25),
    _Fax_alarm_volume_Type()
)
fax_alarm_volume.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fax_alarm_volume.setStatus("optional")


class _Fax_beep_volume_Type(Integer32):
    """Custom type fax_beep_volume based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Fax_beep_volume_Type.__name__ = "Integer32"
_Fax_beep_volume_Object = MibScalar
fax_beep_volume = _Fax_beep_volume_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 7, 1, 26),
    _Fax_beep_volume_Type()
)
fax_beep_volume.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fax_beep_volume.setStatus("optional")


class _Fax_ring_volume_Type(Integer32):
    """Custom type fax_ring_volume based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Fax_ring_volume_Type.__name__ = "Integer32"
_Fax_ring_volume_Object = MibScalar
fax_ring_volume = _Fax_ring_volume_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 7, 1, 27),
    _Fax_ring_volume_Type()
)
fax_ring_volume.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fax_ring_volume.setStatus("optional")
_Fax_master_host_Type = DisplayString
_Fax_master_host_Object = MibScalar
fax_master_host = _Fax_master_host_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 7, 1, 28),
    _Fax_master_host_Type()
)
fax_master_host.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fax_master_host.setStatus("optional")


class _Fax_thumbnail_enable_Type(Integer32):
    """Custom type fax_thumbnail_enable based on Integer32"""
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


_Fax_thumbnail_enable_Type.__name__ = "Integer32"
_Fax_thumbnail_enable_Object = MibScalar
fax_thumbnail_enable = _Fax_thumbnail_enable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 7, 1, 29),
    _Fax_thumbnail_enable_Type()
)
fax_thumbnail_enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fax_thumbnail_enable.setStatus("optional")


class _Fax_phone_pickup_enable_Type(Integer32):
    """Custom type fax_phone_pickup_enable based on Integer32"""
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


_Fax_phone_pickup_enable_Type.__name__ = "Integer32"
_Fax_phone_pickup_enable_Object = MibScalar
fax_phone_pickup_enable = _Fax_phone_pickup_enable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 7, 1, 30),
    _Fax_phone_pickup_enable_Type()
)
fax_phone_pickup_enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fax_phone_pickup_enable.setStatus("optional")
_Fax_adf_scan_count_Type = Integer32
_Fax_adf_scan_count_Object = MibScalar
fax_adf_scan_count = _Fax_adf_scan_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 7, 1, 31),
    _Fax_adf_scan_count_Type()
)
fax_adf_scan_count.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fax_adf_scan_count.setStatus("optional")
_Fax_print_page_count_Type = Integer32
_Fax_print_page_count_Object = MibScalar
fax_print_page_count = _Fax_print_page_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 7, 1, 32),
    _Fax_print_page_count_Type()
)
fax_print_page_count.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fax_print_page_count.setStatus("optional")
_Fax_download_page_count_Type = Integer32
_Fax_download_page_count_Object = MibScalar
fax_download_page_count = _Fax_download_page_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 7, 1, 33),
    _Fax_download_page_count_Type()
)
fax_download_page_count.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fax_download_page_count.setStatus("optional")
_Fax_upload_page_count_Type = Integer32
_Fax_upload_page_count_Object = MibScalar
fax_upload_page_count = _Fax_upload_page_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 7, 1, 34),
    _Fax_upload_page_count_Type()
)
fax_upload_page_count.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fax_upload_page_count.setStatus("optional")
_Status_fax_proc_sub_ObjectIdentity = ObjectIdentity
status_fax_proc_sub = _Status_fax_proc_sub_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 7, 2)
)


class _Fax_upload_Type(Integer32):
    """Custom type fax_upload based on Integer32"""
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
        *(("eFaxUploadAborted", 4),
          ("eFaxUploadActive", 3),
          ("eFaxUploadDone", 5),
          ("eFaxUploadIdle", 1),
          ("eFaxUploadNeeded", 6),
          ("eFaxUploadStart", 2))
    )


_Fax_upload_Type.__name__ = "Integer32"
_Fax_upload_Object = MibScalar
fax_upload = _Fax_upload_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 7, 2, 1),
    _Fax_upload_Type()
)
fax_upload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fax_upload.setStatus("optional")


class _Fax_min_rings_pickup_Type(Integer32):
    """Custom type fax_min_rings_pickup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_Fax_min_rings_pickup_Type.__name__ = "Integer32"
_Fax_min_rings_pickup_Object = MibScalar
fax_min_rings_pickup = _Fax_min_rings_pickup_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 7, 2, 2),
    _Fax_min_rings_pickup_Type()
)
fax_min_rings_pickup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fax_min_rings_pickup.setStatus("optional")


class _Fax_max_rings_pickup_Type(Integer32):
    """Custom type fax_max_rings_pickup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_Fax_max_rings_pickup_Type.__name__ = "Integer32"
_Fax_max_rings_pickup_Object = MibScalar
fax_max_rings_pickup = _Fax_max_rings_pickup_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 7, 2, 3),
    _Fax_max_rings_pickup_Type()
)
fax_max_rings_pickup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fax_max_rings_pickup.setStatus("optional")
_Fax_max_redials_Type = Integer32
_Fax_max_redials_Object = MibScalar
fax_max_redials = _Fax_max_redials_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 7, 2, 4),
    _Fax_max_redials_Type()
)
fax_max_redials.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fax_max_redials.setStatus("optional")
_Fax_additional_wait_Type = Integer32
_Fax_additional_wait_Object = MibScalar
fax_additional_wait = _Fax_additional_wait_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 7, 2, 5),
    _Fax_additional_wait_Type()
)
fax_additional_wait.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fax_additional_wait.setStatus("optional")
_Fax_download_error_Type = Integer32
_Fax_download_error_Object = MibScalar
fax_download_error = _Fax_download_error_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 7, 2, 6),
    _Fax_download_error_Type()
)
fax_download_error.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fax_download_error.setStatus("optional")
_Fax_upload_error_Type = Integer32
_Fax_upload_error_Object = MibScalar
fax_upload_error = _Fax_upload_error_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 7, 2, 7),
    _Fax_upload_error_Type()
)
fax_upload_error.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fax_upload_error.setStatus("optional")


class _Fax_firmware_revision_Type(DisplayString):
    """Custom type fax_firmware_revision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_Fax_firmware_revision_Type.__name__ = "DisplayString"
_Fax_firmware_revision_Object = MibScalar
fax_firmware_revision = _Fax_firmware_revision_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 7, 2, 8),
    _Fax_firmware_revision_Type()
)
fax_firmware_revision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fax_firmware_revision.setStatus("optional")
_Fax_forwarding_ObjectIdentity = ObjectIdentity
fax_forwarding = _Fax_forwarding_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 7, 3)
)
_Fax_forwarding_phone_num_Type = DisplayString
_Fax_forwarding_phone_num_Object = MibScalar
fax_forwarding_phone_num = _Fax_forwarding_phone_num_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 7, 3, 3),
    _Fax_forwarding_phone_num_Type()
)
fax_forwarding_phone_num.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fax_forwarding_phone_num.setStatus("optional")
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


class _Override_media_size_Type(Integer32):
    """Custom type override_media_size based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              10,
              17,
              25,
              26,
              45,
              71,
              72,
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
          ("eFoolscap", 10),
          ("eISOandJISA4", 26),
          ("eISOandJISA5", 25),
          ("eInternationalB5", 100),
          ("eInternationalC5", 91),
          ("eInternationalDL", 90),
          ("eJISB5", 45),
          ("eJapanesePostcardDouble", 72),
          ("eJapanesePostcardSingle", 71),
          ("eMonarch", 80),
          ("eROC16K", 17),
          ("eUSExecutive", 1),
          ("eUSLegal", 3),
          ("eUSLetter", 2))
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
_Print_engine_jam_count_Type = Integer32
_Print_engine_jam_count_Object = MibScalar
print_engine_jam_count = _Print_engine_jam_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 2, 34),
    _Print_engine_jam_count_Type()
)
print_engine_jam_count.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    print_engine_jam_count.setStatus("optional")
_Print_engine_mispick_count_Type = Integer32
_Print_engine_mispick_count_Object = MibScalar
print_engine_mispick_count = _Print_engine_mispick_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 2, 35),
    _Print_engine_mispick_count_Type()
)
print_engine_mispick_count.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    print_engine_mispick_count.setStatus("optional")
_Intray_ObjectIdentity = ObjectIdentity
intray = _Intray_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 3)
)
_Settings_intray_ObjectIdentity = ObjectIdentity
settings_intray = _Settings_intray_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 3, 1)
)


class _Custom_paper_dim_unit_Type(Integer32):
    """Custom type custom_paper_dim_unit based on Integer32"""
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


_Custom_paper_dim_unit_Type.__name__ = "Integer32"
_Custom_paper_dim_unit_Object = MibScalar
custom_paper_dim_unit = _Custom_paper_dim_unit_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 3, 1, 7),
    _Custom_paper_dim_unit_Type()
)
custom_paper_dim_unit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    custom_paper_dim_unit.setStatus("optional")
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
_Intrays_ObjectIdentity = ObjectIdentity
intrays = _Intrays_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 3, 3)
)
_Intray1_ObjectIdentity = ObjectIdentity
intray1 = _Intray1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 3, 3, 1)
)


class _Tray1_fuser_temperature_Type(Integer32):
    """Custom type tray1_fuser_temperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Tray1_fuser_temperature_Type.__name__ = "Integer32"
_Tray1_fuser_temperature_Object = MibScalar
tray1_fuser_temperature = _Tray1_fuser_temperature_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 3, 3, 1, 13),
    _Tray1_fuser_temperature_Type()
)
tray1_fuser_temperature.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tray1_fuser_temperature.setStatus("optional")
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
_Fax_send_ObjectIdentity = ObjectIdentity
fax_send = _Fax_send_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 2)
)
_Settings_fax_send_ObjectIdentity = ObjectIdentity
settings_fax_send = _Settings_fax_send_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 2, 1)
)


class _Fax_resolution_Type(OctetString):
    """Custom type fax_resolution based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_Fax_resolution_Type.__name__ = "OctetString"
_Fax_resolution_Object = MibScalar
fax_resolution = _Fax_resolution_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 2, 1, 1),
    _Fax_resolution_Type()
)
fax_resolution.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fax_resolution.setStatus("optional")


class _Fax_contrast_Type(Integer32):
    """Custom type fax_contrast based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-127, 127),
    )


_Fax_contrast_Type.__name__ = "Integer32"
_Fax_contrast_Object = MibScalar
fax_contrast = _Fax_contrast_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 2, 1, 2),
    _Fax_contrast_Type()
)
fax_contrast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fax_contrast.setStatus("optional")


class _Fax_pixel_data_type_Type(Integer32):
    """Custom type fax_pixel_data_type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eBiLevelHalfToned", 2),
          ("eBiLevelThesholded", 1))
    )


_Fax_pixel_data_type_Type.__name__ = "Integer32"
_Fax_pixel_data_type_Object = MibScalar
fax_pixel_data_type = _Fax_pixel_data_type_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 2, 1, 3),
    _Fax_pixel_data_type_Type()
)
fax_pixel_data_type.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fax_pixel_data_type.setStatus("optional")
_Status_fax_send_ObjectIdentity = ObjectIdentity
status_fax_send = _Status_fax_send_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 2, 2)
)
_Not_ready_fax_send_Type = OctetString
_Not_ready_fax_send_Object = MibScalar
not_ready_fax_send = _Not_ready_fax_send_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 2, 2, 1),
    _Not_ready_fax_send_Type()
)
not_ready_fax_send.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    not_ready_fax_send.setStatus("optional")
_Transmit_fax_ObjectIdentity = ObjectIdentity
transmit_fax = _Transmit_fax_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 2, 5)
)


class _Fax_allow_redials_Type(Integer32):
    """Custom type fax_allow_redials based on Integer32"""
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


_Fax_allow_redials_Type.__name__ = "Integer32"
_Fax_allow_redials_Object = MibScalar
fax_allow_redials = _Fax_allow_redials_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 2, 5, 3),
    _Fax_allow_redials_Type()
)
fax_allow_redials.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fax_allow_redials.setStatus("optional")
_Copier_ObjectIdentity = ObjectIdentity
copier = _Copier_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 5)
)
_Settings_copier_ObjectIdentity = ObjectIdentity
settings_copier = _Settings_copier_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 5, 1)
)


class _Copier_contrast_Type(Integer32):
    """Custom type copier_contrast based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-127, 127),
    )


_Copier_contrast_Type.__name__ = "Integer32"
_Copier_contrast_Object = MibScalar
copier_contrast = _Copier_contrast_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 5, 1, 2),
    _Copier_contrast_Type()
)
copier_contrast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    copier_contrast.setStatus("optional")


class _Copier_reduction_Type(Integer32):
    """Custom type copier_reduction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(25, 400),
    )


_Copier_reduction_Type.__name__ = "Integer32"
_Copier_reduction_Object = MibScalar
copier_reduction = _Copier_reduction_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 5, 1, 4),
    _Copier_reduction_Type()
)
copier_reduction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    copier_reduction.setStatus("optional")


class _Copier_num_copies_Type(Integer32):
    """Custom type copier_num_copies based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_Copier_num_copies_Type.__name__ = "Integer32"
_Copier_num_copies_Object = MibScalar
copier_num_copies = _Copier_num_copies_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 5, 1, 6),
    _Copier_num_copies_Type()
)
copier_num_copies.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    copier_num_copies.setStatus("optional")


class _Copier_collation_Type(Integer32):
    """Custom type copier_collation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eCollateDisabled", 1),
          ("eCollateForward", 2))
    )


_Copier_collation_Type.__name__ = "Integer32"
_Copier_collation_Object = MibScalar
copier_collation = _Copier_collation_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 5, 1, 7),
    _Copier_collation_Type()
)
copier_collation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    copier_collation.setStatus("optional")
_Copier_enlargement_maximum_Type = Integer32
_Copier_enlargement_maximum_Object = MibScalar
copier_enlargement_maximum = _Copier_enlargement_maximum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 5, 1, 11),
    _Copier_enlargement_maximum_Type()
)
copier_enlargement_maximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    copier_enlargement_maximum.setStatus("optional")
_Copier_reduction_maximum_Type = Integer32
_Copier_reduction_maximum_Object = MibScalar
copier_reduction_maximum = _Copier_reduction_maximum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 5, 1, 12),
    _Copier_reduction_maximum_Type()
)
copier_reduction_maximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    copier_reduction_maximum.setStatus("optional")


class _Copier_quality_Type(Integer32):
    """Custom type copier_quality based on Integer32"""
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
        *(("eCopierQualityBest", 5),
          ("eCopierQualityDraft", 4),
          ("eCopierQualityFast", 1),
          ("eCopierQualityNormal", 2),
          ("eCopierQualityPresentation", 3))
    )


_Copier_quality_Type.__name__ = "Integer32"
_Copier_quality_Object = MibScalar
copier_quality = _Copier_quality_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 5, 1, 13),
    _Copier_quality_Type()
)
copier_quality.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    copier_quality.setStatus("optional")
_Copier_adf_page_count_Type = Integer32
_Copier_adf_page_count_Object = MibScalar
copier_adf_page_count = _Copier_adf_page_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 5, 1, 19),
    _Copier_adf_page_count_Type()
)
copier_adf_page_count.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    copier_adf_page_count.setStatus("optional")
_Copier_print_page_count_Type = Integer32
_Copier_print_page_count_Object = MibScalar
copier_print_page_count = _Copier_print_page_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 5, 1, 20),
    _Copier_print_page_count_Type()
)
copier_print_page_count.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    copier_print_page_count.setStatus("optional")


class _Copier_job_media_size_Type(Integer32):
    """Custom type copier_job_media_size based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              26)
        )
    )
    namedValues = NamedValues(
        *(("eISOandJISA4", 26),
          ("eUSLegal", 3),
          ("eUSLetter", 2))
    )


_Copier_job_media_size_Type.__name__ = "Integer32"
_Copier_job_media_size_Object = MibScalar
copier_job_media_size = _Copier_job_media_size_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 5, 1, 21),
    _Copier_job_media_size_Type()
)
copier_job_media_size.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    copier_job_media_size.setStatus("optional")


class _Copier_job_quality_Type(Integer32):
    """Custom type copier_job_quality based on Integer32"""
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
        *(("eCopierQualityBest", 5),
          ("eCopierQualityDraft", 4),
          ("eCopierQualityFast", 1),
          ("eCopierQualityNormal", 2),
          ("eCopierQualityPresentation", 3))
    )


_Copier_job_quality_Type.__name__ = "Integer32"
_Copier_job_quality_Object = MibScalar
copier_job_quality = _Copier_job_quality_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 5, 1, 22),
    _Copier_job_quality_Type()
)
copier_job_quality.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    copier_job_quality.setStatus("optional")


class _Copier_job_collation_Type(Integer32):
    """Custom type copier_job_collation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eCollateDisabled", 1),
          ("eCollateForward", 2))
    )


_Copier_job_collation_Type.__name__ = "Integer32"
_Copier_job_collation_Object = MibScalar
copier_job_collation = _Copier_job_collation_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 5, 1, 23),
    _Copier_job_collation_Type()
)
copier_job_collation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    copier_job_collation.setStatus("optional")


class _Copier_job_num_copies_Type(Integer32):
    """Custom type copier_job_num_copies based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_Copier_job_num_copies_Type.__name__ = "Integer32"
_Copier_job_num_copies_Object = MibScalar
copier_job_num_copies = _Copier_job_num_copies_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 5, 1, 24),
    _Copier_job_num_copies_Type()
)
copier_job_num_copies.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    copier_job_num_copies.setStatus("optional")


class _Copier_job_reduction_Type(Integer32):
    """Custom type copier_job_reduction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(25, 400),
    )


_Copier_job_reduction_Type.__name__ = "Integer32"
_Copier_job_reduction_Object = MibScalar
copier_job_reduction = _Copier_job_reduction_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 5, 1, 25),
    _Copier_job_reduction_Type()
)
copier_job_reduction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    copier_job_reduction.setStatus("optional")


class _Copier_job_contrast_Type(Integer32):
    """Custom type copier_job_contrast based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-127, 127),
    )


_Copier_job_contrast_Type.__name__ = "Integer32"
_Copier_job_contrast_Object = MibScalar
copier_job_contrast = _Copier_job_contrast_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 5, 1, 26),
    _Copier_job_contrast_Type()
)
copier_job_contrast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    copier_job_contrast.setStatus("optional")


class _Copier_job_Type(Integer32):
    """Custom type copier_job based on Integer32"""
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
        *(("eCopierAborting", 4),
          ("eCopierActive", 3),
          ("eCopierIdle", 1),
          ("eCopierSetup", 5),
          ("eCopierStart", 2))
    )


_Copier_job_Type.__name__ = "Integer32"
_Copier_job_Object = MibScalar
copier_job = _Copier_job_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 5, 1, 27),
    _Copier_job_Type()
)
copier_job.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    copier_job.setStatus("optional")
_Copier_flatbed_page_count_Type = Integer32
_Copier_flatbed_page_count_Object = MibScalar
copier_flatbed_page_count = _Copier_flatbed_page_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 5, 1, 44),
    _Copier_flatbed_page_count_Type()
)
copier_flatbed_page_count.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    copier_flatbed_page_count.setStatus("optional")


class _Copier_pages_per_sheet_Type(Integer32):
    """Custom type copier_pages_per_sheet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ePagesPerSheet1", 1),
          ("ePagesPerSheet2", 2),
          ("ePagesPerSheet4", 3))
    )


_Copier_pages_per_sheet_Type.__name__ = "Integer32"
_Copier_pages_per_sheet_Object = MibScalar
copier_pages_per_sheet = _Copier_pages_per_sheet_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 5, 1, 45),
    _Copier_pages_per_sheet_Type()
)
copier_pages_per_sheet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    copier_pages_per_sheet.setStatus("optional")


class _Copier_job_pages_per_sheet_Type(Integer32):
    """Custom type copier_job_pages_per_sheet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ePagesPerSheet1", 1),
          ("ePagesPerSheet2", 2),
          ("ePagesPerSheet4", 3))
    )


_Copier_job_pages_per_sheet_Type.__name__ = "Integer32"
_Copier_job_pages_per_sheet_Object = MibScalar
copier_job_pages_per_sheet = _Copier_job_pages_per_sheet_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 5, 1, 46),
    _Copier_job_pages_per_sheet_Type()
)
copier_job_pages_per_sheet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    copier_job_pages_per_sheet.setStatus("optional")


class _Copier_fit_to_page_Type(Integer32):
    """Custom type copier_fit_to_page based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eFitToPageDisabled", 1),
          ("eFitToPageEnabled", 2))
    )


_Copier_fit_to_page_Type.__name__ = "Integer32"
_Copier_fit_to_page_Object = MibScalar
copier_fit_to_page = _Copier_fit_to_page_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 5, 1, 47),
    _Copier_fit_to_page_Type()
)
copier_fit_to_page.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    copier_fit_to_page.setStatus("optional")


class _Copier_job_fit_to_page_Type(Integer32):
    """Custom type copier_job_fit_to_page based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eFitToPageDisabled", 1),
          ("eFitToPageEnabled", 2))
    )


_Copier_job_fit_to_page_Type.__name__ = "Integer32"
_Copier_job_fit_to_page_Object = MibScalar
copier_job_fit_to_page = _Copier_job_fit_to_page_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 5, 1, 48),
    _Copier_job_fit_to_page_Type()
)
copier_job_fit_to_page.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    copier_job_fit_to_page.setStatus("optional")
_Copier_pages_per_sheet_maximum_Type = Integer32
_Copier_pages_per_sheet_maximum_Object = MibScalar
copier_pages_per_sheet_maximum = _Copier_pages_per_sheet_maximum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 5, 1, 49),
    _Copier_pages_per_sheet_maximum_Type()
)
copier_pages_per_sheet_maximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    copier_pages_per_sheet_maximum.setStatus("optional")
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
_Prtgeneralconfigchanges_Type = Integer32
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
        ValueRangeConstraint(1, 16),
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
prtoutputdefaultindex.setMaxAccess("read-only")
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
prtmediapathdefaultindex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtmediapathdefaultindex.setStatus("optional")


class _Prtconsolelocalization_Type(Integer32):
    """Custom type prtconsolelocalization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
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
            3
        )
    )
    namedValues = NamedValues(
        ("ePoperatorConsoleEnabled", 3)
    )


_Prtconsoledisable_Type.__name__ = "Integer32"
_Prtconsoledisable_Object = MibScalar
prtconsoledisable = _Prtconsoledisable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 5, 1, 1, 13),
    _Prtconsoledisable_Type()
)
prtconsoledisable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtconsoledisable.setStatus("optional")


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
        ValueSizeConstraint(0, 11),
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
            *(5,
              8,
              12,
              2004)
        )
    )
    namedValues = NamedValues(
        *(("ePcsHPRoman8", 2004),
          ("ePcsISOLatin2", 5),
          ("ePcsISOLatin5", 12),
          ("ePcsISOLatinCyrillic", 8))
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
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("ePsheetFeedAutoNonRemovableTray", 4),
          ("ePsheetFeedAutoRemovableTray", 3))
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
prtinputdimunit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtinputdimunit.setStatus("optional")
_Prtinputmediadimfeeddirdeclared_Type = Integer32
_Prtinputmediadimfeeddirdeclared_Object = MibScalar
prtinputmediadimfeeddirdeclared = _Prtinputmediadimfeeddirdeclared_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 8, 2, 1, 4),
    _Prtinputmediadimfeeddirdeclared_Type()
)
prtinputmediadimfeeddirdeclared.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtinputmediadimfeeddirdeclared.setStatus("optional")
_Prtinputmediadimxfeeddirdeclared_Type = Integer32
_Prtinputmediadimxfeeddirdeclared_Object = MibScalar
prtinputmediadimxfeeddirdeclared = _Prtinputmediadimxfeeddirdeclared_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 8, 2, 1, 5),
    _Prtinputmediadimxfeeddirdeclared_Type()
)
prtinputmediadimxfeeddirdeclared.setMaxAccess("read-only")
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
            8
        )
    )
    namedValues = NamedValues(
        ("ePsheets", 8)
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
prtinputmedianame.setMaxAccess("read-only")
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
            *(1,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("ePother", 1),
          ("ePreceptacleThatIsFilled", 4),
          ("ePsupplyThatIsConsumed", 3))
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
            5
        )
    )
    namedValues = NamedValues(
        ("ePsimplex", 5)
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
              10,
              11,
              15,
              34,
              38)
        )
    )
    namedValues = NamedValues(
        *(("ePchAppleTalkPAP", 7),
          ("ePchBidirPortTCP", 38),
          ("ePchDLCLLCPort", 15),
          ("ePchIEEE1284Port", 5),
          ("ePchNetwarePServer", 10),
          ("ePchPort9100", 11),
          ("ePchUSB", 34),
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
            *(1,
              3,
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
              2027)
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
          ("ePcsPC850Multilingual", 2009),
          ("ePcsPC8CodePage437", 2011),
          ("ePcsPC8DNDanishNorwegian", 2012),
          ("ePcsPCp852", 2010),
          ("ePcsUnicodeIBM2039", 1004),
          ("ePcsWindows30Latin1", 2000),
          ("ePcsWindows31Latin1", 2001),
          ("ePcsWindows31Latin2", 2002),
          ("ePcsWindows31Latin5", 2003),
          ("ePother", 1))
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
              2,
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
          ("ePunknown", 2),
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
              14)
        )
    )
    namedValues = NamedValues(
        *(("ePchannel", 14),
          ("ePcover", 6),
          ("ePgeneralPrinter", 5),
          ("ePinput", 8),
          ("ePmarker", 10),
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
              801,
              808)
        )
    )
    namedValues = NamedValues(
        *(("ePcoverOpened", 3),
          ("ePinputMediaSupplyEmpty", 808),
          ("ePinputMediaTrayMissing", 801),
          ("ePjam", 8),
          ("ePother", 1))
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
        ValueSizeConstraint(0, 64),
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

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LaserJet_3300-MIB",
    **{"DisplayString": DisplayString,
       "hp": hp,
       "dm": dm,
       "device": device,
       "system": system,
       "settings-system": settings_system,
       "energy-star": energy_star,
       "sleep-mode": sleep_mode,
       "service-password": service_password,
       "device-cfg-download": device_cfg_download,
       "device-cfg-download-data-type": device_cfg_download_data_type,
       "device-cfg-upload": device_cfg_upload,
       "device-cfg-upload-data-type": device_cfg_upload_data_type,
       "download-timeout": download_timeout,
       "upload-timeout": upload_timeout,
       "date-display": date_display,
       "device-cfg-param-command": device_cfg_param_command,
       "copier-token": copier_token,
       "scan-token": scan_token,
       "fax-upload-token": fax_upload_token,
       "fax-download-token": fax_download_token,
       "device-config-token": device_config_token,
       "status-system": status_system,
       "on-off-line": on_off_line,
       "continue": _pysmi_continue,
       "auto-continue": auto_continue,
       "install-date": install_date,
       "date-and-time": date_and_time,
       "time-display": time_display,
       "error-log-clear": error_log_clear,
       "collated-originals-support": collated_originals_support,
       "device-cfg-download-error": device_cfg_download_error,
       "device-cfg-upload-error": device_cfg_upload_error,
       "id": id,
       "model-name": model_name,
       "serial-number": serial_number,
       "fw-rom-datecode": fw_rom_datecode,
       "fax-local-phone-num": fax_local_phone_num,
       "fax-station-name": fax_station_name,
       "device-name": device_name,
       "device-location": device_location,
       "asset-number": asset_number,
       "fax-line-interface-unit-id": fax_line_interface_unit_id,
       "interface": interface,
       "simm": simm,
       "simm1": simm1,
       "simm1-type": simm1_type,
       "simm1-capacity": simm1_capacity,
       "test": test,
       "self-test": self_test,
       "print-internal-page": print_internal_page,
       "job": job,
       "settings-job": settings_job,
       "cancel-job": cancel_job,
       "job-info-change-id": job_info_change_id,
       "active-print-jobs": active_print_jobs,
       "job-being-parsed": job_being_parsed,
       "current-job-parsing-id": current_job_parsing_id,
       "fax-job-control": fax_job_control,
       "settings-fax-job": settings_fax_job,
       "faxjob-action": faxjob_action,
       "faxjob-action-id": faxjob_action_id,
       "faxjob-tx-type": faxjob_tx_type,
       "status-fax-job": status_fax_job,
       "faxjob-download-id": faxjob_download_id,
       "faxjob-rx-id": faxjob_rx_id,
       "faxjob-tx-id": faxjob_tx_id,
       "faxjob-upload-id": faxjob_upload_id,
       "faxjob": faxjob,
       "faxjob-rx-status": faxjob_rx_status,
       "faxjob-rx-status-1": faxjob_rx_status_1,
       "faxjob-tx-status": faxjob_tx_status,
       "faxjob-tx-status-1": faxjob_tx_status_1,
       "faxjob-tx-error": faxjob_tx_error,
       "faxjob-tx-error-1": faxjob_tx_error_1,
       "faxjob-tx-current-page": faxjob_tx_current_page,
       "faxjob-tx-current-page-1": faxjob_tx_current_page_1,
       "faxjob-rx-current-page": faxjob_rx_current_page,
       "faxjob-rx-current-page-1": faxjob_rx_current_page_1,
       "faxjob-rx-duration": faxjob_rx_duration,
       "faxjob-rx-duration-1": faxjob_rx_duration_1,
       "faxjob-tx-duration": faxjob_tx_duration,
       "faxjob-tx-duration-1": faxjob_tx_duration_1,
       "fax-activity-log": fax_activity_log,
       "settings-faxlog": settings_faxlog,
       "fax-log-action": fax_log_action,
       "fax-log-reporting": fax_log_reporting,
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
       "phone": phone,
       "dial": dial,
       "dial-all-lines": dial_all_lines,
       "fax-dial-mode": fax_dial_mode,
       "device-redial": device_redial,
       "fax-pulse-dial-support": fax_pulse_dial_support,
       "answer": answer,
       "answer-all-lines": answer_all_lines,
       "fax-answer-mode": fax_answer_mode,
       "fax-num-rings-pickup": fax_num_rings_pickup,
       "device-ring-type-pickup": device_ring_type_pickup,
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
       "source-subsystem": source_subsystem,
       "io": io,
       "settings-io": settings_io,
       "io-timeout": io_timeout,
       "io-switch": io_switch,
       "scanner": scanner,
       "settings-scanner": settings_scanner,
       "scan-contrast": scan_contrast,
       "scan-resolution": scan_resolution,
       "scan-pixel-data-type": scan_pixel_data_type,
       "scan-compression": scan_compression,
       "scan-compression-factor": scan_compression_factor,
       "scan-upload-error": scan_upload_error,
       "scan-upload": scan_upload,
       "default-scanner-margin-left": default_scanner_margin_left,
       "default-scanner-margin-right": default_scanner_margin_right,
       "scan-calibration": scan_calibration,
       "scan-calibration-target": scan_calibration_target,
       "ui-add-option": ui_add_option,
       "ui-select-option": ui_select_option,
       "ui-delete-option": ui_delete_option,
       "scanner-jam-page-count": scanner_jam_page_count,
       "scanner-adf-page-count": scanner_adf_page_count,
       "scan-adf-page-count": scan_adf_page_count,
       "scan-image-type": scan_image_type,
       "scan-subsample": scan_subsample,
       "scanner-retrieve-scanline": scanner_retrieve_scanline,
       "scanner-motor-control": scanner_motor_control,
       "scan-height": scan_height,
       "scanner-scanline-statistics": scanner_scanline_statistics,
       "scan-control-descriptor": scan_control_descriptor,
       "scan-gamma-correction": scan_gamma_correction,
       "scan-pad-image": scan_pad_image,
       "scan-flatbed-page-count": scan_flatbed_page_count,
       "scanner-flatbed-page-count": scanner_flatbed_page_count,
       "scanner-modular-hardware": scanner_modular_hardware,
       "default-scanner-margin-top": default_scanner_margin_top,
       "scan-max-line-width": scan_max_line_width,
       "status-scanner": status_scanner,
       "not-ready-source-scanner": not_ready_source_scanner,
       "scan-resolution-range": scan_resolution_range,
       "scan-calibration-download": scan_calibration_download,
       "scan-calibration-error": scan_calibration_error,
       "scanner-button-status": scanner_button_status,
       "scanner-lamp-gain-value": scanner_lamp_gain_value,
       "scanner-light-monitor-window": scanner_light_monitor_window,
       "scanner-reference-position": scanner_reference_position,
       "scanner-sensor-manufacturer": scanner_sensor_manufacturer,
       "fax-receive": fax_receive,
       "settings-fax-receive": settings_fax_receive,
       "fax-receive-stamping-enable": fax_receive_stamping_enable,
       "status-fax-receive": status_fax_receive,
       "not-ready-fax-receive": not_ready_fax_receive,
       "processing-subsystem": processing_subsystem,
       "pdl": pdl,
       "settings-pdl": settings_pdl,
       "default-copies": default_copies,
       "form-feed": form_feed,
       "maximum-resource-saving-memory": maximum_resource_saving_memory,
       "default-vertical-black-resolution": default_vertical_black_resolution,
       "default-horizontal-black-resolution": default_horizontal_black_resolution,
       "default-page-protect": default_page_protect,
       "default-lines-per-page": default_lines_per_page,
       "default-vmi": default_vmi,
       "default-media-size": default_media_size,
       "cold-reset-media-size": cold_reset_media_size,
       "reprint": reprint,
       "wide-a4": wide_a4,
       "dark-courier": dark_courier,
       "default-bits-per-pixel": default_bits_per_pixel,
       "status-pdl": status_pdl,
       "form-feed-needed": form_feed_needed,
       "pdl-pcl": pdl_pcl,
       "pcl-resource-saving-memory-size": pcl_resource_saving_memory_size,
       "pcl-default-font-height": pcl_default_font_height,
       "pcl-default-font-source": pcl_default_font_source,
       "pcl-default-font-number": pcl_default_font_number,
       "pcl-default-font-width": pcl_default_font_width,
       "pjl": pjl,
       "pjl-password": pjl_password,
       "fax-proc-sub": fax_proc_sub,
       "settings-fax-proc-sub": settings_fax_proc_sub,
       "fax-rxscale": fax_rxscale,
       "fax-noise-volume": fax_noise_volume,
       "fax-download": fax_download,
       "fax-silent-detection": fax_silent_detection,
       "fax-ring-enable": fax_ring_enable,
       "fax-country": fax_country,
       "fax-tx-phone-number": fax_tx_phone_number,
       "fax-redial-time": fax_redial_time,
       "fax-pstn-access-code": fax_pstn_access_code,
       "fax-rx-disposition": fax_rx_disposition,
       "fax-error-correction-mode": fax_error_correction_mode,
       "fax-report-transmission": fax_report_transmission,
       "fax-report-activity-log": fax_report_activity_log,
       "fax-dial-tone-detection": fax_dial_tone_detection,
       "fax-alarm-volume": fax_alarm_volume,
       "fax-beep-volume": fax_beep_volume,
       "fax-ring-volume": fax_ring_volume,
       "fax-master-host": fax_master_host,
       "fax-thumbnail-enable": fax_thumbnail_enable,
       "fax-phone-pickup-enable": fax_phone_pickup_enable,
       "fax-adf-scan-count": fax_adf_scan_count,
       "fax-print-page-count": fax_print_page_count,
       "fax-download-page-count": fax_download_page_count,
       "fax-upload-page-count": fax_upload_page_count,
       "status-fax-proc-sub": status_fax_proc_sub,
       "fax-upload": fax_upload,
       "fax-min-rings-pickup": fax_min_rings_pickup,
       "fax-max-rings-pickup": fax_max_rings_pickup,
       "fax-max-redials": fax_max_redials,
       "fax-additional-wait": fax_additional_wait,
       "fax-download-error": fax_download_error,
       "fax-upload-error": fax_upload_error,
       "fax-firmware-revision": fax_firmware_revision,
       "fax-forwarding": fax_forwarding,
       "fax-forwarding-phone-num": fax_forwarding_phone_num,
       "destination-subsystem": destination_subsystem,
       "print-engine": print_engine,
       "settings-prt-eng": settings_prt_eng,
       "override-media-size": override_media_size,
       "print-density": print_density,
       "status-prt-eng": status_prt_eng,
       "total-engine-page-count": total_engine_page_count,
       "print-engine-jam-count": print_engine_jam_count,
       "print-engine-mispick-count": print_engine_mispick_count,
       "intray": intray,
       "settings-intray": settings_intray,
       "custom-paper-dim-unit": custom_paper_dim_unit,
       "custom-paper-feed-dim": custom_paper_feed_dim,
       "custom-paper-xfeed-dim": custom_paper_xfeed_dim,
       "intrays": intrays,
       "intray1": intray1,
       "tray1-fuser-temperature": tray1_fuser_temperature,
       "imaging": imaging,
       "default-ret": default_ret,
       "default-print-quality": default_print_quality,
       "fax-send": fax_send,
       "settings-fax-send": settings_fax_send,
       "fax-resolution": fax_resolution,
       "fax-contrast": fax_contrast,
       "fax-pixel-data-type": fax_pixel_data_type,
       "status-fax-send": status_fax_send,
       "not-ready-fax-send": not_ready_fax_send,
       "transmit-fax": transmit_fax,
       "fax-allow-redials": fax_allow_redials,
       "copier": copier,
       "settings-copier": settings_copier,
       "copier-contrast": copier_contrast,
       "copier-reduction": copier_reduction,
       "copier-num-copies": copier_num_copies,
       "copier-collation": copier_collation,
       "copier-enlargement-maximum": copier_enlargement_maximum,
       "copier-reduction-maximum": copier_reduction_maximum,
       "copier-quality": copier_quality,
       "copier-adf-page-count": copier_adf_page_count,
       "copier-print-page-count": copier_print_page_count,
       "copier-job-media-size": copier_job_media_size,
       "copier-job-quality": copier_job_quality,
       "copier-job-collation": copier_job_collation,
       "copier-job-num-copies": copier_job_num_copies,
       "copier-job-reduction": copier_job_reduction,
       "copier-job-contrast": copier_job_contrast,
       "copier-job": copier_job,
       "copier-flatbed-page-count": copier_flatbed_page_count,
       "copier-pages-per-sheet": copier_pages_per_sheet,
       "copier-job-pages-per-sheet": copier_job_pages_per_sheet,
       "copier-fit-to-page": copier_fit_to_page,
       "copier-job-fit-to-page": copier_job_fit_to_page,
       "copier-pages-per-sheet-maximum": copier_pages_per_sheet_maximum,
       "tables": tables,
       "channel-table": channel_table,
       "channel-entry": channel_entry,
       "channel-bytes-sent": channel_bytes_sent,
       "channel-bytes-received": channel_bytes_received,
       "channel-io-errors": channel_io_errors,
       "channel-jobs-received": channel_jobs_received,
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
       "prtOutput": prtOutput,
       "prtOutputTable": prtOutputTable,
       "prtOutputEntry": prtOutputEntry,
       "prtoutputtype": prtoutputtype,
       "prtoutputcapacityunit": prtoutputcapacityunit,
       "prtoutputmaxcapacity": prtoutputmaxcapacity,
       "prtoutputremainingcapacity": prtoutputremainingcapacity,
       "prtoutputstatus": prtoutputstatus,
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
       "hrprinterdetectederrorstate": hrprinterdetectederrorstate}
)
