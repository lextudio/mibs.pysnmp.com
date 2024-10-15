# SNMP MIB module (TPT-NGFW-SYSTEM-INFO-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TPT-NGFW-SYSTEM-INFO-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:07:00 2024
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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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

(DateAndTime,
 DisplayString,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention",
    "TruthValue")

(tpt_ngfw_compls,
 tpt_ngfw_eventsV2,
 tpt_ngfw_groups,
 tpt_ngfw_objs,
 tptNgfwNotifySeverity) = mibBuilder.importSymbols(
    "TPT-NGFW-REG-MIB",
    "tpt-ngfw-compls",
    "tpt-ngfw-eventsV2",
    "tpt-ngfw-groups",
    "tpt-ngfw-objs",
    "tptNgfwNotifySeverity")


# MODULE-IDENTITY

tptNgfwSystemInfo = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 1)
)
tptNgfwSystemInfo.setRevisions(
        ("2016-05-25 18:54",
         "2013-01-03 17:39")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class FipsState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("crypto", 2),
          ("disabled", 1),
          ("full", 3))
    )



class BuildType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("development", 2),
          ("production", 1))
    )



# MIB Managed Objects in the order of their OIDs



class _TptNgfwSystemSerial_Type(SnmpAdminString):
    """Custom type tptNgfwSystemSerial based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_TptNgfwSystemSerial_Type.__name__ = "SnmpAdminString"
_TptNgfwSystemSerial_Object = MibScalar
tptNgfwSystemSerial = _TptNgfwSystemSerial_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 1, 1),
    _TptNgfwSystemSerial_Type()
)
tptNgfwSystemSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptNgfwSystemSerial.setStatus("current")


class _TptNgfwSystemSoftwareVersion_Type(SnmpAdminString):
    """Custom type tptNgfwSystemSoftwareVersion based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_TptNgfwSystemSoftwareVersion_Type.__name__ = "SnmpAdminString"
_TptNgfwSystemSoftwareVersion_Object = MibScalar
tptNgfwSystemSoftwareVersion = _TptNgfwSystemSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 1, 2),
    _TptNgfwSystemSoftwareVersion_Type()
)
tptNgfwSystemSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptNgfwSystemSoftwareVersion.setStatus("current")
_TptNgfwSystemBuildDate_Type = DateAndTime
_TptNgfwSystemBuildDate_Object = MibScalar
tptNgfwSystemBuildDate = _TptNgfwSystemBuildDate_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 1, 3),
    _TptNgfwSystemBuildDate_Type()
)
tptNgfwSystemBuildDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptNgfwSystemBuildDate.setStatus("current")
_TptNgfwSystemBuildType_Type = BuildType
_TptNgfwSystemBuildType_Object = MibScalar
tptNgfwSystemBuildType = _TptNgfwSystemBuildType_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 1, 4),
    _TptNgfwSystemBuildType_Type()
)
tptNgfwSystemBuildType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptNgfwSystemBuildType.setStatus("current")


class _TptNgfwSystemBuildRevision_Type(SnmpAdminString):
    """Custom type tptNgfwSystemBuildRevision based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_TptNgfwSystemBuildRevision_Type.__name__ = "SnmpAdminString"
_TptNgfwSystemBuildRevision_Object = MibScalar
tptNgfwSystemBuildRevision = _TptNgfwSystemBuildRevision_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 1, 5),
    _TptNgfwSystemBuildRevision_Type()
)
tptNgfwSystemBuildRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptNgfwSystemBuildRevision.setStatus("current")


class _TptNgfwSystemDigitalVaccineVersion_Type(SnmpAdminString):
    """Custom type tptNgfwSystemDigitalVaccineVersion based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_TptNgfwSystemDigitalVaccineVersion_Type.__name__ = "SnmpAdminString"
_TptNgfwSystemDigitalVaccineVersion_Object = MibScalar
tptNgfwSystemDigitalVaccineVersion = _TptNgfwSystemDigitalVaccineVersion_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 1, 6),
    _TptNgfwSystemDigitalVaccineVersion_Type()
)
tptNgfwSystemDigitalVaccineVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptNgfwSystemDigitalVaccineVersion.setStatus("current")


class _TptNgfwSystemModel_Type(SnmpAdminString):
    """Custom type tptNgfwSystemModel based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_TptNgfwSystemModel_Type.__name__ = "SnmpAdminString"
_TptNgfwSystemModel_Object = MibScalar
tptNgfwSystemModel = _TptNgfwSystemModel_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 1, 7),
    _TptNgfwSystemModel_Type()
)
tptNgfwSystemModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptNgfwSystemModel.setStatus("current")


class _TptNgfwSystemHardwareSerial_Type(SnmpAdminString):
    """Custom type tptNgfwSystemHardwareSerial based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_TptNgfwSystemHardwareSerial_Type.__name__ = "SnmpAdminString"
_TptNgfwSystemHardwareSerial_Object = MibScalar
tptNgfwSystemHardwareSerial = _TptNgfwSystemHardwareSerial_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 1, 8),
    _TptNgfwSystemHardwareSerial_Type()
)
tptNgfwSystemHardwareSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptNgfwSystemHardwareSerial.setStatus("current")


class _TptNgfwSystemHardwareRevision_Type(SnmpAdminString):
    """Custom type tptNgfwSystemHardwareRevision based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_TptNgfwSystemHardwareRevision_Type.__name__ = "SnmpAdminString"
_TptNgfwSystemHardwareRevision_Object = MibScalar
tptNgfwSystemHardwareRevision = _TptNgfwSystemHardwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 1, 9),
    _TptNgfwSystemHardwareRevision_Type()
)
tptNgfwSystemHardwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptNgfwSystemHardwareRevision.setStatus("current")


class _TptNgfwSystemFailsafeVersion_Type(SnmpAdminString):
    """Custom type tptNgfwSystemFailsafeVersion based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_TptNgfwSystemFailsafeVersion_Type.__name__ = "SnmpAdminString"
_TptNgfwSystemFailsafeVersion_Object = MibScalar
tptNgfwSystemFailsafeVersion = _TptNgfwSystemFailsafeVersion_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 1, 10),
    _TptNgfwSystemFailsafeVersion_Type()
)
tptNgfwSystemFailsafeVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptNgfwSystemFailsafeVersion.setStatus("current")
_TptNgfwSystemBootTime_Type = DateAndTime
_TptNgfwSystemBootTime_Object = MibScalar
tptNgfwSystemBootTime = _TptNgfwSystemBootTime_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 1, 11),
    _TptNgfwSystemBootTime_Type()
)
tptNgfwSystemBootTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptNgfwSystemBootTime.setStatus("current")
_TptNgfwSystemUpTime_Type = TimeTicks
_TptNgfwSystemUpTime_Object = MibScalar
tptNgfwSystemUpTime = _TptNgfwSystemUpTime_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 1, 12),
    _TptNgfwSystemUpTime_Type()
)
tptNgfwSystemUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptNgfwSystemUpTime.setStatus("current")
_TptNgfwSystemSmsManaged_Type = TruthValue
_TptNgfwSystemSmsManaged_Object = MibScalar
tptNgfwSystemSmsManaged = _TptNgfwSystemSmsManaged_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 1, 13),
    _TptNgfwSystemSmsManaged_Type()
)
tptNgfwSystemSmsManaged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptNgfwSystemSmsManaged.setStatus("current")
_TptNgfwSystemSmsIpAddressType_Type = InetAddressType
_TptNgfwSystemSmsIpAddressType_Object = MibScalar
tptNgfwSystemSmsIpAddressType = _TptNgfwSystemSmsIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 1, 14),
    _TptNgfwSystemSmsIpAddressType_Type()
)
tptNgfwSystemSmsIpAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptNgfwSystemSmsIpAddressType.setStatus("current")
_TptNgfwSystemSmsIpAddress_Type = InetAddress
_TptNgfwSystemSmsIpAddress_Object = MibScalar
tptNgfwSystemSmsIpAddress = _TptNgfwSystemSmsIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 1, 15),
    _TptNgfwSystemSmsIpAddress_Type()
)
tptNgfwSystemSmsIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptNgfwSystemSmsIpAddress.setStatus("current")
_TptNgfwSystemFipsAdminState_Type = FipsState
_TptNgfwSystemFipsAdminState_Object = MibScalar
tptNgfwSystemFipsAdminState = _TptNgfwSystemFipsAdminState_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 1, 16),
    _TptNgfwSystemFipsAdminState_Type()
)
tptNgfwSystemFipsAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptNgfwSystemFipsAdminState.setStatus("current")
_TptNgfwSystemFipsOperState_Type = FipsState
_TptNgfwSystemFipsOperState_Object = MibScalar
tptNgfwSystemFipsOperState = _TptNgfwSystemFipsOperState_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 1, 17),
    _TptNgfwSystemFipsOperState_Type()
)
tptNgfwSystemFipsOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptNgfwSystemFipsOperState.setStatus("current")
_TptNgfwSystemMasterKeySet_Type = TruthValue
_TptNgfwSystemMasterKeySet_Object = MibScalar
tptNgfwSystemMasterKeySet = _TptNgfwSystemMasterKeySet_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 1, 18),
    _TptNgfwSystemMasterKeySet_Type()
)
tptNgfwSystemMasterKeySet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptNgfwSystemMasterKeySet.setStatus("current")

# Managed Objects groups

tptNgfwSystemInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 1, 1, 1)
)
tptNgfwSystemInfoGroup.setObjects(
      *(("TPT-NGFW-SYSTEM-INFO-MIB", "tptNgfwSystemSerial"),
        ("TPT-NGFW-SYSTEM-INFO-MIB", "tptNgfwSystemSoftwareVersion"),
        ("TPT-NGFW-SYSTEM-INFO-MIB", "tptNgfwSystemBuildDate"),
        ("TPT-NGFW-SYSTEM-INFO-MIB", "tptNgfwSystemBuildType"),
        ("TPT-NGFW-SYSTEM-INFO-MIB", "tptNgfwSystemBuildRevision"),
        ("TPT-NGFW-SYSTEM-INFO-MIB", "tptNgfwSystemDigitalVaccineVersion"),
        ("TPT-NGFW-SYSTEM-INFO-MIB", "tptNgfwSystemModel"),
        ("TPT-NGFW-SYSTEM-INFO-MIB", "tptNgfwSystemHardwareSerial"),
        ("TPT-NGFW-SYSTEM-INFO-MIB", "tptNgfwSystemHardwareRevision"),
        ("TPT-NGFW-SYSTEM-INFO-MIB", "tptNgfwSystemFailsafeVersion"),
        ("TPT-NGFW-SYSTEM-INFO-MIB", "tptNgfwSystemBootTime"),
        ("TPT-NGFW-SYSTEM-INFO-MIB", "tptNgfwSystemUpTime"),
        ("TPT-NGFW-SYSTEM-INFO-MIB", "tptNgfwSystemSmsManaged"),
        ("TPT-NGFW-SYSTEM-INFO-MIB", "tptNgfwSystemSmsIpAddressType"),
        ("TPT-NGFW-SYSTEM-INFO-MIB", "tptNgfwSystemSmsIpAddress"),
        ("TPT-NGFW-SYSTEM-INFO-MIB", "tptNgfwSystemFipsAdminState"),
        ("TPT-NGFW-SYSTEM-INFO-MIB", "tptNgfwSystemFipsOperState"),
        ("TPT-NGFW-SYSTEM-INFO-MIB", "tptNgfwSystemMasterKeySet"))
)
if mibBuilder.loadTexts:
    tptNgfwSystemInfoGroup.setStatus("current")


# Notification objects

tptNgfwSystemReadyNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 3, 0, 11)
)
tptNgfwSystemReadyNotify.setObjects(
      *(("TPT-NGFW-SYSTEM-INFO-MIB", "tptNgfwSystemSerial"),
        ("TPT-NGFW-REG-MIB", "tptNgfwNotifySeverity"))
)
if mibBuilder.loadTexts:
    tptNgfwSystemReadyNotify.setStatus(
        "current"
    )

tptNgfwSystemShutdownNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 3, 0, 12)
)
tptNgfwSystemShutdownNotify.setObjects(
      *(("TPT-NGFW-SYSTEM-INFO-MIB", "tptNgfwSystemSerial"),
        ("TPT-NGFW-REG-MIB", "tptNgfwNotifySeverity"))
)
if mibBuilder.loadTexts:
    tptNgfwSystemShutdownNotify.setStatus(
        "current"
    )

tptNgfwSystemSmsNotAuthNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 3, 0, 13)
)
tptNgfwSystemSmsNotAuthNotify.setObjects(
      *(("TPT-NGFW-SYSTEM-INFO-MIB", "tptNgfwSystemSerial"),
        ("TPT-NGFW-SYSTEM-INFO-MIB", "tptNgfwSystemSmsIpAddressType"),
        ("TPT-NGFW-SYSTEM-INFO-MIB", "tptNgfwSystemSmsIpAddress"),
        ("TPT-NGFW-REG-MIB", "tptNgfwNotifySeverity"))
)
if mibBuilder.loadTexts:
    tptNgfwSystemSmsNotAuthNotify.setStatus(
        "current"
    )


# Notifications groups

tptNgfwSystemNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 1, 1, 9)
)
tptNgfwSystemNotificationGroup.setObjects(
      *(("TPT-NGFW-SYSTEM-INFO-MIB", "tptNgfwSystemReadyNotify"),
        ("TPT-NGFW-SYSTEM-INFO-MIB", "tptNgfwSystemShutdownNotify"),
        ("TPT-NGFW-SYSTEM-INFO-MIB", "tptNgfwSystemSmsNotAuthNotify"))
)
if mibBuilder.loadTexts:
    tptNgfwSystemNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

tptNgfwSystemInfoCompl = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 1, 2, 1)
)
if mibBuilder.loadTexts:
    tptNgfwSystemInfoCompl.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPT-NGFW-SYSTEM-INFO-MIB",
    **{"FipsState": FipsState,
       "BuildType": BuildType,
       "tptNgfwSystemInfoGroup": tptNgfwSystemInfoGroup,
       "tptNgfwSystemNotificationGroup": tptNgfwSystemNotificationGroup,
       "tptNgfwSystemInfoCompl": tptNgfwSystemInfoCompl,
       "tptNgfwSystemInfo": tptNgfwSystemInfo,
       "tptNgfwSystemSerial": tptNgfwSystemSerial,
       "tptNgfwSystemSoftwareVersion": tptNgfwSystemSoftwareVersion,
       "tptNgfwSystemBuildDate": tptNgfwSystemBuildDate,
       "tptNgfwSystemBuildType": tptNgfwSystemBuildType,
       "tptNgfwSystemBuildRevision": tptNgfwSystemBuildRevision,
       "tptNgfwSystemDigitalVaccineVersion": tptNgfwSystemDigitalVaccineVersion,
       "tptNgfwSystemModel": tptNgfwSystemModel,
       "tptNgfwSystemHardwareSerial": tptNgfwSystemHardwareSerial,
       "tptNgfwSystemHardwareRevision": tptNgfwSystemHardwareRevision,
       "tptNgfwSystemFailsafeVersion": tptNgfwSystemFailsafeVersion,
       "tptNgfwSystemBootTime": tptNgfwSystemBootTime,
       "tptNgfwSystemUpTime": tptNgfwSystemUpTime,
       "tptNgfwSystemSmsManaged": tptNgfwSystemSmsManaged,
       "tptNgfwSystemSmsIpAddressType": tptNgfwSystemSmsIpAddressType,
       "tptNgfwSystemSmsIpAddress": tptNgfwSystemSmsIpAddress,
       "tptNgfwSystemFipsAdminState": tptNgfwSystemFipsAdminState,
       "tptNgfwSystemFipsOperState": tptNgfwSystemFipsOperState,
       "tptNgfwSystemMasterKeySet": tptNgfwSystemMasterKeySet,
       "tptNgfwSystemReadyNotify": tptNgfwSystemReadyNotify,
       "tptNgfwSystemShutdownNotify": tptNgfwSystemShutdownNotify,
       "tptNgfwSystemSmsNotAuthNotify": tptNgfwSystemSmsNotAuthNotify}
)
