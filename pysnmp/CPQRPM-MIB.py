# SNMP MIB module (CPQRPM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CPQRPM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:17:38 2024
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

(compaq,) = mibBuilder.importSymbols(
    "CPQHOST-MIB",
    "compaq")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(sysName,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysName")

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
 NotificationType,
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
    "NotificationType",
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


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CpqRPM_ObjectIdentity = ObjectIdentity
cpqRPM = _CpqRPM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 154)
)
_CpqRPMTrapInfo_ObjectIdentity = ObjectIdentity
cpqRPMTrapInfo = _CpqRPMTrapInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 154, 1)
)


class _CpqRPMTrapDescription_Type(DisplayString):
    """Custom type cpqRPMTrapDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqRPMTrapDescription_Type.__name__ = "DisplayString"
_CpqRPMTrapDescription_Object = MibScalar
cpqRPMTrapDescription = _CpqRPMTrapDescription_Object(
    (1, 3, 6, 1, 4, 1, 232, 154, 1, 1),
    _CpqRPMTrapDescription_Type()
)
cpqRPMTrapDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRPMTrapDescription.setStatus("mandatory")


class _CpqRPMTrapDeviceId_Type(Integer32):
    """Custom type cpqRPMTrapDeviceId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CpqRPMTrapDeviceId_Type.__name__ = "Integer32"
_CpqRPMTrapDeviceId_Object = MibScalar
cpqRPMTrapDeviceId = _CpqRPMTrapDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 232, 154, 1, 2),
    _CpqRPMTrapDeviceId_Type()
)
cpqRPMTrapDeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRPMTrapDeviceId.setStatus("mandatory")


class _CpqRPMTrapDeviceName_Type(DisplayString):
    """Custom type cpqRPMTrapDeviceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_CpqRPMTrapDeviceName_Type.__name__ = "DisplayString"
_CpqRPMTrapDeviceName_Object = MibScalar
cpqRPMTrapDeviceName = _CpqRPMTrapDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 232, 154, 1, 3),
    _CpqRPMTrapDeviceName_Type()
)
cpqRPMTrapDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRPMTrapDeviceName.setStatus("mandatory")


class _CpqRPMTrapDeviceAddress_Type(DisplayString):
    """Custom type cpqRPMTrapDeviceAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_CpqRPMTrapDeviceAddress_Type.__name__ = "DisplayString"
_CpqRPMTrapDeviceAddress_Object = MibScalar
cpqRPMTrapDeviceAddress = _CpqRPMTrapDeviceAddress_Object(
    (1, 3, 6, 1, 4, 1, 232, 154, 1, 4),
    _CpqRPMTrapDeviceAddress_Type()
)
cpqRPMTrapDeviceAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRPMTrapDeviceAddress.setStatus("mandatory")


class _CpqRPMTrapType_Type(Integer32):
    """Custom type cpqRPMTrapType based on Integer32"""
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
        *(("change", 3),
          ("environment", 5),
          ("event", 2),
          ("power", 4),
          ("system", 1))
    )


_CpqRPMTrapType_Type.__name__ = "Integer32"
_CpqRPMTrapType_Object = MibScalar
cpqRPMTrapType = _CpqRPMTrapType_Object(
    (1, 3, 6, 1, 4, 1, 232, 154, 1, 5),
    _CpqRPMTrapType_Type()
)
cpqRPMTrapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRPMTrapType.setStatus("mandatory")


class _CpqRPMTrapSeverity_Type(Integer32):
    """Custom type cpqRPMTrapSeverity based on Integer32"""
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
        *(("critical", 6),
          ("information", 2),
          ("major", 5),
          ("minor", 4),
          ("normal", 3),
          ("unknown", 1))
    )


_CpqRPMTrapSeverity_Type.__name__ = "Integer32"
_CpqRPMTrapSeverity_Object = MibScalar
cpqRPMTrapSeverity = _CpqRPMTrapSeverity_Object(
    (1, 3, 6, 1, 4, 1, 232, 154, 1, 6),
    _CpqRPMTrapSeverity_Type()
)
cpqRPMTrapSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRPMTrapSeverity.setStatus("mandatory")


class _CpqRPMTrapCode_Type(Integer32):
    """Custom type cpqRPMTrapCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CpqRPMTrapCode_Type.__name__ = "Integer32"
_CpqRPMTrapCode_Object = MibScalar
cpqRPMTrapCode = _CpqRPMTrapCode_Object(
    (1, 3, 6, 1, 4, 1, 232, 154, 1, 7),
    _CpqRPMTrapCode_Type()
)
cpqRPMTrapCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRPMTrapCode.setStatus("mandatory")


class _CpqRPMTrapURL_Type(DisplayString):
    """Custom type cpqRPMTrapURL based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqRPMTrapURL_Type.__name__ = "DisplayString"
_CpqRPMTrapURL_Object = MibScalar
cpqRPMTrapURL = _CpqRPMTrapURL_Object(
    (1, 3, 6, 1, 4, 1, 232, 154, 1, 8),
    _CpqRPMTrapURL_Type()
)
cpqRPMTrapURL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqRPMTrapURL.setStatus("mandatory")
_CpqRPMTraps_ObjectIdentity = ObjectIdentity
cpqRPMTraps = _CpqRPMTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 154, 2)
)
_CpqPMTraps_ObjectIdentity = ObjectIdentity
cpqPMTraps = _CpqPMTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 154, 3)
)

# Managed Objects groups


# Notification objects

cpqRPMTrapDeviceConnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 154, 2, 0, 1)
)
cpqRPMTrapDeviceConnected.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQRPM-MIB", "cpqRPMTrapDescription"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceId"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceName"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceAddress"),
        ("CPQRPM-MIB", "cpqRPMTrapType"),
        ("CPQRPM-MIB", "cpqRPMTrapSeverity"),
        ("CPQRPM-MIB", "cpqRPMTrapURL"))
)
if mibBuilder.loadTexts:
    cpqRPMTrapDeviceConnected.setStatus(
        ""
    )

cpqRPMTrapConnectionLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 154, 2, 0, 2)
)
cpqRPMTrapConnectionLost.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQRPM-MIB", "cpqRPMTrapDescription"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceId"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceName"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceAddress"),
        ("CPQRPM-MIB", "cpqRPMTrapType"),
        ("CPQRPM-MIB", "cpqRPMTrapSeverity"),
        ("CPQRPM-MIB", "cpqRPMTrapURL"))
)
if mibBuilder.loadTexts:
    cpqRPMTrapConnectionLost.setStatus(
        ""
    )

cpqRPMTrapLookupFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 154, 2, 0, 3)
)
cpqRPMTrapLookupFailed.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQRPM-MIB", "cpqRPMTrapDescription"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceId"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceName"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceAddress"),
        ("CPQRPM-MIB", "cpqRPMTrapType"),
        ("CPQRPM-MIB", "cpqRPMTrapSeverity"),
        ("CPQRPM-MIB", "cpqRPMTrapURL"))
)
if mibBuilder.loadTexts:
    cpqRPMTrapLookupFailed.setStatus(
        ""
    )

cpqRPMTrapConnectionFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 154, 2, 0, 4)
)
cpqRPMTrapConnectionFailed.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQRPM-MIB", "cpqRPMTrapDescription"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceId"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceName"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceAddress"),
        ("CPQRPM-MIB", "cpqRPMTrapType"),
        ("CPQRPM-MIB", "cpqRPMTrapSeverity"),
        ("CPQRPM-MIB", "cpqRPMTrapURL"))
)
if mibBuilder.loadTexts:
    cpqRPMTrapConnectionFailed.setStatus(
        ""
    )

cpqRPMTrapDeviceSettingsChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 154, 2, 0, 5)
)
cpqRPMTrapDeviceSettingsChanged.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQRPM-MIB", "cpqRPMTrapDescription"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceId"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceName"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceAddress"),
        ("CPQRPM-MIB", "cpqRPMTrapType"),
        ("CPQRPM-MIB", "cpqRPMTrapSeverity"),
        ("CPQRPM-MIB", "cpqRPMTrapURL"))
)
if mibBuilder.loadTexts:
    cpqRPMTrapDeviceSettingsChanged.setStatus(
        ""
    )

cpqRPMTrapCMCTemp1BelowMin = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 154, 2, 0, 10001)
)
cpqRPMTrapCMCTemp1BelowMin.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQRPM-MIB", "cpqRPMTrapDescription"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceId"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceName"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceAddress"),
        ("CPQRPM-MIB", "cpqRPMTrapType"),
        ("CPQRPM-MIB", "cpqRPMTrapSeverity"),
        ("CPQRPM-MIB", "cpqRPMTrapURL"))
)
if mibBuilder.loadTexts:
    cpqRPMTrapCMCTemp1BelowMin.setStatus(
        ""
    )

cpqRPMTrapCMCTemp1AboveWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 154, 2, 0, 10002)
)
cpqRPMTrapCMCTemp1AboveWarn.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQRPM-MIB", "cpqRPMTrapDescription"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceId"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceName"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceAddress"),
        ("CPQRPM-MIB", "cpqRPMTrapType"),
        ("CPQRPM-MIB", "cpqRPMTrapSeverity"),
        ("CPQRPM-MIB", "cpqRPMTrapURL"))
)
if mibBuilder.loadTexts:
    cpqRPMTrapCMCTemp1AboveWarn.setStatus(
        ""
    )

cpqRPMTrapCMCTemp1AboveMax = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 154, 2, 0, 10003)
)
cpqRPMTrapCMCTemp1AboveMax.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQRPM-MIB", "cpqRPMTrapDescription"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceId"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceName"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceAddress"),
        ("CPQRPM-MIB", "cpqRPMTrapType"),
        ("CPQRPM-MIB", "cpqRPMTrapSeverity"),
        ("CPQRPM-MIB", "cpqRPMTrapURL"))
)
if mibBuilder.loadTexts:
    cpqRPMTrapCMCTemp1AboveMax.setStatus(
        ""
    )

cpqRPMTrapCMCTemp1Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 154, 2, 0, 10004)
)
cpqRPMTrapCMCTemp1Normal.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQRPM-MIB", "cpqRPMTrapDescription"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceId"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceName"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceAddress"),
        ("CPQRPM-MIB", "cpqRPMTrapType"),
        ("CPQRPM-MIB", "cpqRPMTrapSeverity"),
        ("CPQRPM-MIB", "cpqRPMTrapURL"))
)
if mibBuilder.loadTexts:
    cpqRPMTrapCMCTemp1Normal.setStatus(
        ""
    )

cpqRPMTrapCMCTemp2BelowMin = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 154, 2, 0, 10005)
)
cpqRPMTrapCMCTemp2BelowMin.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQRPM-MIB", "cpqRPMTrapDescription"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceId"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceName"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceAddress"),
        ("CPQRPM-MIB", "cpqRPMTrapType"),
        ("CPQRPM-MIB", "cpqRPMTrapSeverity"),
        ("CPQRPM-MIB", "cpqRPMTrapURL"))
)
if mibBuilder.loadTexts:
    cpqRPMTrapCMCTemp2BelowMin.setStatus(
        ""
    )

cpqRPMTrapCMCTemp2AboveWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 154, 2, 0, 10006)
)
cpqRPMTrapCMCTemp2AboveWarn.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQRPM-MIB", "cpqRPMTrapDescription"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceId"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceName"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceAddress"),
        ("CPQRPM-MIB", "cpqRPMTrapType"),
        ("CPQRPM-MIB", "cpqRPMTrapSeverity"),
        ("CPQRPM-MIB", "cpqRPMTrapURL"))
)
if mibBuilder.loadTexts:
    cpqRPMTrapCMCTemp2AboveWarn.setStatus(
        ""
    )

cpqRPMTrapCMCTemp2AboveMax = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 154, 2, 0, 10007)
)
cpqRPMTrapCMCTemp2AboveMax.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQRPM-MIB", "cpqRPMTrapDescription"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceId"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceName"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceAddress"),
        ("CPQRPM-MIB", "cpqRPMTrapType"),
        ("CPQRPM-MIB", "cpqRPMTrapSeverity"),
        ("CPQRPM-MIB", "cpqRPMTrapURL"))
)
if mibBuilder.loadTexts:
    cpqRPMTrapCMCTemp2AboveMax.setStatus(
        ""
    )

cpqRPMTrapCMCTemp2Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 154, 2, 0, 10008)
)
cpqRPMTrapCMCTemp2Normal.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQRPM-MIB", "cpqRPMTrapDescription"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceId"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceName"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceAddress"),
        ("CPQRPM-MIB", "cpqRPMTrapType"),
        ("CPQRPM-MIB", "cpqRPMTrapSeverity"),
        ("CPQRPM-MIB", "cpqRPMTrapURL"))
)
if mibBuilder.loadTexts:
    cpqRPMTrapCMCTemp2Normal.setStatus(
        ""
    )

cpqRPMTrapCMCVoltUnder = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 154, 2, 0, 10011)
)
cpqRPMTrapCMCVoltUnder.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQRPM-MIB", "cpqRPMTrapDescription"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceId"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceName"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceAddress"),
        ("CPQRPM-MIB", "cpqRPMTrapType"),
        ("CPQRPM-MIB", "cpqRPMTrapSeverity"),
        ("CPQRPM-MIB", "cpqRPMTrapURL"))
)
if mibBuilder.loadTexts:
    cpqRPMTrapCMCVoltUnder.setStatus(
        ""
    )

cpqRPMTrapCMCVoltOver = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 154, 2, 0, 10012)
)
cpqRPMTrapCMCVoltOver.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQRPM-MIB", "cpqRPMTrapDescription"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceId"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceName"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceAddress"),
        ("CPQRPM-MIB", "cpqRPMTrapType"),
        ("CPQRPM-MIB", "cpqRPMTrapSeverity"),
        ("CPQRPM-MIB", "cpqRPMTrapURL"))
)
if mibBuilder.loadTexts:
    cpqRPMTrapCMCVoltOver.setStatus(
        ""
    )

cpqRPMTrapCMCVoltNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 154, 2, 0, 10013)
)
cpqRPMTrapCMCVoltNormal.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQRPM-MIB", "cpqRPMTrapDescription"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceId"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceName"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceAddress"),
        ("CPQRPM-MIB", "cpqRPMTrapType"),
        ("CPQRPM-MIB", "cpqRPMTrapSeverity"),
        ("CPQRPM-MIB", "cpqRPMTrapURL"))
)
if mibBuilder.loadTexts:
    cpqRPMTrapCMCVoltNormal.setStatus(
        ""
    )

cpqRPMTrapCMCHmdtUnder = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 154, 2, 0, 10021)
)
cpqRPMTrapCMCHmdtUnder.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQRPM-MIB", "cpqRPMTrapDescription"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceId"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceName"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceAddress"),
        ("CPQRPM-MIB", "cpqRPMTrapType"),
        ("CPQRPM-MIB", "cpqRPMTrapSeverity"),
        ("CPQRPM-MIB", "cpqRPMTrapURL"))
)
if mibBuilder.loadTexts:
    cpqRPMTrapCMCHmdtUnder.setStatus(
        ""
    )

cpqRPMTrapCMCHmdtOver = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 154, 2, 0, 10022)
)
cpqRPMTrapCMCHmdtOver.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQRPM-MIB", "cpqRPMTrapDescription"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceId"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceName"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceAddress"),
        ("CPQRPM-MIB", "cpqRPMTrapType"),
        ("CPQRPM-MIB", "cpqRPMTrapSeverity"),
        ("CPQRPM-MIB", "cpqRPMTrapURL"))
)
if mibBuilder.loadTexts:
    cpqRPMTrapCMCHmdtOver.setStatus(
        ""
    )

cpqRPMTrapCMCHmdtNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 154, 2, 0, 10023)
)
cpqRPMTrapCMCHmdtNormal.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQRPM-MIB", "cpqRPMTrapDescription"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceId"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceName"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceAddress"),
        ("CPQRPM-MIB", "cpqRPMTrapType"),
        ("CPQRPM-MIB", "cpqRPMTrapSeverity"),
        ("CPQRPM-MIB", "cpqRPMTrapURL"))
)
if mibBuilder.loadTexts:
    cpqRPMTrapCMCHmdtNormal.setStatus(
        ""
    )

cpqRPMTrapCMCSmokeDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 154, 2, 0, 10031)
)
cpqRPMTrapCMCSmokeDetected.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQRPM-MIB", "cpqRPMTrapDescription"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceId"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceName"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceAddress"),
        ("CPQRPM-MIB", "cpqRPMTrapType"),
        ("CPQRPM-MIB", "cpqRPMTrapSeverity"),
        ("CPQRPM-MIB", "cpqRPMTrapURL"))
)
if mibBuilder.loadTexts:
    cpqRPMTrapCMCSmokeDetected.setStatus(
        ""
    )

cpqRPMTrapCMCSmokeCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 154, 2, 0, 10032)
)
cpqRPMTrapCMCSmokeCleared.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQRPM-MIB", "cpqRPMTrapDescription"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceId"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceName"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceAddress"),
        ("CPQRPM-MIB", "cpqRPMTrapType"),
        ("CPQRPM-MIB", "cpqRPMTrapSeverity"),
        ("CPQRPM-MIB", "cpqRPMTrapURL"))
)
if mibBuilder.loadTexts:
    cpqRPMTrapCMCSmokeCleared.setStatus(
        ""
    )

cpqRPMTrapCMCShockDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 154, 2, 0, 10041)
)
cpqRPMTrapCMCShockDetected.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQRPM-MIB", "cpqRPMTrapDescription"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceId"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceName"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceAddress"),
        ("CPQRPM-MIB", "cpqRPMTrapType"),
        ("CPQRPM-MIB", "cpqRPMTrapSeverity"),
        ("CPQRPM-MIB", "cpqRPMTrapURL"))
)
if mibBuilder.loadTexts:
    cpqRPMTrapCMCShockDetected.setStatus(
        ""
    )

cpqRPMTrapCMCShockCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 154, 2, 0, 10042)
)
cpqRPMTrapCMCShockCleared.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQRPM-MIB", "cpqRPMTrapDescription"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceId"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceName"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceAddress"),
        ("CPQRPM-MIB", "cpqRPMTrapType"),
        ("CPQRPM-MIB", "cpqRPMTrapSeverity"),
        ("CPQRPM-MIB", "cpqRPMTrapURL"))
)
if mibBuilder.loadTexts:
    cpqRPMTrapCMCShockCleared.setStatus(
        ""
    )

cpqRPMTrapCMCAux1Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 154, 2, 0, 10051)
)
cpqRPMTrapCMCAux1Alarm.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQRPM-MIB", "cpqRPMTrapDescription"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceId"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceName"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceAddress"),
        ("CPQRPM-MIB", "cpqRPMTrapType"),
        ("CPQRPM-MIB", "cpqRPMTrapSeverity"),
        ("CPQRPM-MIB", "cpqRPMTrapURL"))
)
if mibBuilder.loadTexts:
    cpqRPMTrapCMCAux1Alarm.setStatus(
        ""
    )

cpqRPMTrapCMCAux1Cleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 154, 2, 0, 10052)
)
cpqRPMTrapCMCAux1Cleared.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQRPM-MIB", "cpqRPMTrapDescription"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceId"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceName"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceAddress"),
        ("CPQRPM-MIB", "cpqRPMTrapType"),
        ("CPQRPM-MIB", "cpqRPMTrapSeverity"),
        ("CPQRPM-MIB", "cpqRPMTrapURL"))
)
if mibBuilder.loadTexts:
    cpqRPMTrapCMCAux1Cleared.setStatus(
        ""
    )

cpqRPMTrapCMCAux2Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 154, 2, 0, 10053)
)
cpqRPMTrapCMCAux2Alarm.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQRPM-MIB", "cpqRPMTrapDescription"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceId"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceName"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceAddress"),
        ("CPQRPM-MIB", "cpqRPMTrapType"),
        ("CPQRPM-MIB", "cpqRPMTrapSeverity"),
        ("CPQRPM-MIB", "cpqRPMTrapURL"))
)
if mibBuilder.loadTexts:
    cpqRPMTrapCMCAux2Alarm.setStatus(
        ""
    )

cpqRPMTrapCMCAux2Cleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 154, 2, 0, 10054)
)
cpqRPMTrapCMCAux2Cleared.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQRPM-MIB", "cpqRPMTrapDescription"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceId"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceName"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceAddress"),
        ("CPQRPM-MIB", "cpqRPMTrapType"),
        ("CPQRPM-MIB", "cpqRPMTrapSeverity"),
        ("CPQRPM-MIB", "cpqRPMTrapURL"))
)
if mibBuilder.loadTexts:
    cpqRPMTrapCMCAux2Cleared.setStatus(
        ""
    )

cpqRPMTrapCMCInput1Opened = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 154, 2, 0, 10101)
)
cpqRPMTrapCMCInput1Opened.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQRPM-MIB", "cpqRPMTrapDescription"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceId"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceName"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceAddress"),
        ("CPQRPM-MIB", "cpqRPMTrapType"),
        ("CPQRPM-MIB", "cpqRPMTrapSeverity"),
        ("CPQRPM-MIB", "cpqRPMTrapURL"))
)
if mibBuilder.loadTexts:
    cpqRPMTrapCMCInput1Opened.setStatus(
        ""
    )

cpqRPMTrapCMCInput1Closed = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 154, 2, 0, 10102)
)
cpqRPMTrapCMCInput1Closed.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQRPM-MIB", "cpqRPMTrapDescription"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceId"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceName"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceAddress"),
        ("CPQRPM-MIB", "cpqRPMTrapType"),
        ("CPQRPM-MIB", "cpqRPMTrapSeverity"),
        ("CPQRPM-MIB", "cpqRPMTrapURL"))
)
if mibBuilder.loadTexts:
    cpqRPMTrapCMCInput1Closed.setStatus(
        ""
    )

cpqRPMTrapCMCInput2Opened = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 154, 2, 0, 10103)
)
cpqRPMTrapCMCInput2Opened.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQRPM-MIB", "cpqRPMTrapDescription"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceId"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceName"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceAddress"),
        ("CPQRPM-MIB", "cpqRPMTrapType"),
        ("CPQRPM-MIB", "cpqRPMTrapSeverity"),
        ("CPQRPM-MIB", "cpqRPMTrapURL"))
)
if mibBuilder.loadTexts:
    cpqRPMTrapCMCInput2Opened.setStatus(
        ""
    )

cpqRPMTrapCMCInput2Closed = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 154, 2, 0, 10104)
)
cpqRPMTrapCMCInput2Closed.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQRPM-MIB", "cpqRPMTrapDescription"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceId"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceName"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceAddress"),
        ("CPQRPM-MIB", "cpqRPMTrapType"),
        ("CPQRPM-MIB", "cpqRPMTrapSeverity"),
        ("CPQRPM-MIB", "cpqRPMTrapURL"))
)
if mibBuilder.loadTexts:
    cpqRPMTrapCMCInput2Closed.setStatus(
        ""
    )

cpqRPMTrapCMCInput3Opened = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 154, 2, 0, 10105)
)
cpqRPMTrapCMCInput3Opened.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQRPM-MIB", "cpqRPMTrapDescription"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceId"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceName"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceAddress"),
        ("CPQRPM-MIB", "cpqRPMTrapType"),
        ("CPQRPM-MIB", "cpqRPMTrapSeverity"),
        ("CPQRPM-MIB", "cpqRPMTrapURL"))
)
if mibBuilder.loadTexts:
    cpqRPMTrapCMCInput3Opened.setStatus(
        ""
    )

cpqRPMTrapCMCInput3Closed = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 154, 2, 0, 10106)
)
cpqRPMTrapCMCInput3Closed.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQRPM-MIB", "cpqRPMTrapDescription"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceId"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceName"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceAddress"),
        ("CPQRPM-MIB", "cpqRPMTrapType"),
        ("CPQRPM-MIB", "cpqRPMTrapSeverity"),
        ("CPQRPM-MIB", "cpqRPMTrapURL"))
)
if mibBuilder.loadTexts:
    cpqRPMTrapCMCInput3Closed.setStatus(
        ""
    )

cpqRPMTrapCMCInput4Opened = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 154, 2, 0, 10107)
)
cpqRPMTrapCMCInput4Opened.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQRPM-MIB", "cpqRPMTrapDescription"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceId"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceName"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceAddress"),
        ("CPQRPM-MIB", "cpqRPMTrapType"),
        ("CPQRPM-MIB", "cpqRPMTrapSeverity"),
        ("CPQRPM-MIB", "cpqRPMTrapURL"))
)
if mibBuilder.loadTexts:
    cpqRPMTrapCMCInput4Opened.setStatus(
        ""
    )

cpqRPMTrapCMCInput4Closed = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 154, 2, 0, 10108)
)
cpqRPMTrapCMCInput4Closed.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQRPM-MIB", "cpqRPMTrapDescription"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceId"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceName"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceAddress"),
        ("CPQRPM-MIB", "cpqRPMTrapType"),
        ("CPQRPM-MIB", "cpqRPMTrapSeverity"),
        ("CPQRPM-MIB", "cpqRPMTrapURL"))
)
if mibBuilder.loadTexts:
    cpqRPMTrapCMCInput4Closed.setStatus(
        ""
    )

cpqRPMTrapCMCLockset1Unlocked = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 154, 2, 0, 10111)
)
cpqRPMTrapCMCLockset1Unlocked.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQRPM-MIB", "cpqRPMTrapDescription"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceId"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceName"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceAddress"),
        ("CPQRPM-MIB", "cpqRPMTrapType"),
        ("CPQRPM-MIB", "cpqRPMTrapSeverity"),
        ("CPQRPM-MIB", "cpqRPMTrapURL"))
)
if mibBuilder.loadTexts:
    cpqRPMTrapCMCLockset1Unlocked.setStatus(
        ""
    )

cpqRPMTrapCMCLockset1FailedToLock = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 154, 2, 0, 10112)
)
cpqRPMTrapCMCLockset1FailedToLock.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQRPM-MIB", "cpqRPMTrapDescription"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceId"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceName"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceAddress"),
        ("CPQRPM-MIB", "cpqRPMTrapType"),
        ("CPQRPM-MIB", "cpqRPMTrapSeverity"),
        ("CPQRPM-MIB", "cpqRPMTrapURL"))
)
if mibBuilder.loadTexts:
    cpqRPMTrapCMCLockset1FailedToLock.setStatus(
        ""
    )

cpqRPMTrapCMCLockset1Error = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 154, 2, 0, 10113)
)
cpqRPMTrapCMCLockset1Error.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQRPM-MIB", "cpqRPMTrapDescription"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceId"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceName"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceAddress"),
        ("CPQRPM-MIB", "cpqRPMTrapType"),
        ("CPQRPM-MIB", "cpqRPMTrapSeverity"),
        ("CPQRPM-MIB", "cpqRPMTrapURL"))
)
if mibBuilder.loadTexts:
    cpqRPMTrapCMCLockset1Error.setStatus(
        ""
    )

cpqRPMTrapCMCLockset1Locked = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 154, 2, 0, 10114)
)
cpqRPMTrapCMCLockset1Locked.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQRPM-MIB", "cpqRPMTrapDescription"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceId"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceName"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceAddress"),
        ("CPQRPM-MIB", "cpqRPMTrapType"),
        ("CPQRPM-MIB", "cpqRPMTrapSeverity"),
        ("CPQRPM-MIB", "cpqRPMTrapURL"))
)
if mibBuilder.loadTexts:
    cpqRPMTrapCMCLockset1Locked.setStatus(
        ""
    )

cpqRPMTrapCMCLockset2Unlocked = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 154, 2, 0, 10116)
)
cpqRPMTrapCMCLockset2Unlocked.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQRPM-MIB", "cpqRPMTrapDescription"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceId"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceName"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceAddress"),
        ("CPQRPM-MIB", "cpqRPMTrapType"),
        ("CPQRPM-MIB", "cpqRPMTrapSeverity"),
        ("CPQRPM-MIB", "cpqRPMTrapURL"))
)
if mibBuilder.loadTexts:
    cpqRPMTrapCMCLockset2Unlocked.setStatus(
        ""
    )

cpqRPMTrapCMCLockset2FailedToLock = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 154, 2, 0, 10117)
)
cpqRPMTrapCMCLockset2FailedToLock.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQRPM-MIB", "cpqRPMTrapDescription"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceId"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceName"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceAddress"),
        ("CPQRPM-MIB", "cpqRPMTrapType"),
        ("CPQRPM-MIB", "cpqRPMTrapSeverity"),
        ("CPQRPM-MIB", "cpqRPMTrapURL"))
)
if mibBuilder.loadTexts:
    cpqRPMTrapCMCLockset2FailedToLock.setStatus(
        ""
    )

cpqRPMTrapCMCLockset2Error = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 154, 2, 0, 10118)
)
cpqRPMTrapCMCLockset2Error.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQRPM-MIB", "cpqRPMTrapDescription"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceId"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceName"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceAddress"),
        ("CPQRPM-MIB", "cpqRPMTrapType"),
        ("CPQRPM-MIB", "cpqRPMTrapSeverity"),
        ("CPQRPM-MIB", "cpqRPMTrapURL"))
)
if mibBuilder.loadTexts:
    cpqRPMTrapCMCLockset2Error.setStatus(
        ""
    )

cpqRPMTrapCMCLockset2Locked = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 154, 2, 0, 10119)
)
cpqRPMTrapCMCLockset2Locked.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQRPM-MIB", "cpqRPMTrapDescription"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceId"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceName"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceAddress"),
        ("CPQRPM-MIB", "cpqRPMTrapType"),
        ("CPQRPM-MIB", "cpqRPMTrapSeverity"),
        ("CPQRPM-MIB", "cpqRPMTrapURL"))
)
if mibBuilder.loadTexts:
    cpqRPMTrapCMCLockset2Locked.setStatus(
        ""
    )

cpqRPMTrapCMCLockset1Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 154, 2, 0, 10134)
)
cpqRPMTrapCMCLockset1Normal.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQRPM-MIB", "cpqRPMTrapDescription"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceId"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceName"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceAddress"),
        ("CPQRPM-MIB", "cpqRPMTrapType"),
        ("CPQRPM-MIB", "cpqRPMTrapSeverity"),
        ("CPQRPM-MIB", "cpqRPMTrapURL"))
)
if mibBuilder.loadTexts:
    cpqRPMTrapCMCLockset1Normal.setStatus(
        ""
    )

cpqRPMTrapCMCLockset2Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 154, 2, 0, 10135)
)
cpqRPMTrapCMCLockset2Normal.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQRPM-MIB", "cpqRPMTrapDescription"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceId"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceName"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceAddress"),
        ("CPQRPM-MIB", "cpqRPMTrapType"),
        ("CPQRPM-MIB", "cpqRPMTrapSeverity"),
        ("CPQRPM-MIB", "cpqRPMTrapURL"))
)
if mibBuilder.loadTexts:
    cpqRPMTrapCMCLockset2Normal.setStatus(
        ""
    )

cpqRPMTrapUPSInputVoltageBelowMin = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 154, 2, 0, 20001)
)
cpqRPMTrapUPSInputVoltageBelowMin.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQRPM-MIB", "cpqRPMTrapDescription"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceId"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceName"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceAddress"),
        ("CPQRPM-MIB", "cpqRPMTrapType"),
        ("CPQRPM-MIB", "cpqRPMTrapSeverity"))
)
if mibBuilder.loadTexts:
    cpqRPMTrapUPSInputVoltageBelowMin.setStatus(
        ""
    )

cpqRPMTrapUPSInputVoltageAboveMax = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 154, 2, 0, 20002)
)
cpqRPMTrapUPSInputVoltageAboveMax.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQRPM-MIB", "cpqRPMTrapDescription"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceId"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceName"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceAddress"),
        ("CPQRPM-MIB", "cpqRPMTrapType"),
        ("CPQRPM-MIB", "cpqRPMTrapSeverity"))
)
if mibBuilder.loadTexts:
    cpqRPMTrapUPSInputVoltageAboveMax.setStatus(
        ""
    )

cpqRPMTrapUPSInputVoltageNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 154, 2, 0, 20003)
)
cpqRPMTrapUPSInputVoltageNormal.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQRPM-MIB", "cpqRPMTrapDescription"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceId"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceName"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceAddress"),
        ("CPQRPM-MIB", "cpqRPMTrapType"),
        ("CPQRPM-MIB", "cpqRPMTrapSeverity"),
        ("CPQRPM-MIB", "cpqRPMTrapURL"))
)
if mibBuilder.loadTexts:
    cpqRPMTrapUPSInputVoltageNormal.setStatus(
        ""
    )

cpqRPMTrapUPSOutputVoltageBelowMin = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 154, 2, 0, 20011)
)
cpqRPMTrapUPSOutputVoltageBelowMin.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQRPM-MIB", "cpqRPMTrapDescription"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceId"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceName"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceAddress"),
        ("CPQRPM-MIB", "cpqRPMTrapType"),
        ("CPQRPM-MIB", "cpqRPMTrapSeverity"))
)
if mibBuilder.loadTexts:
    cpqRPMTrapUPSOutputVoltageBelowMin.setStatus(
        ""
    )

cpqRPMTrapUPSOutputVoltageAboveMax = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 154, 2, 0, 20012)
)
cpqRPMTrapUPSOutputVoltageAboveMax.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQRPM-MIB", "cpqRPMTrapDescription"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceId"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceName"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceAddress"),
        ("CPQRPM-MIB", "cpqRPMTrapType"),
        ("CPQRPM-MIB", "cpqRPMTrapSeverity"))
)
if mibBuilder.loadTexts:
    cpqRPMTrapUPSOutputVoltageAboveMax.setStatus(
        ""
    )

cpqRPMTrapUPSOutputOverload = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 154, 2, 0, 20014)
)
cpqRPMTrapUPSOutputOverload.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQRPM-MIB", "cpqRPMTrapDescription"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceId"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceName"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceAddress"),
        ("CPQRPM-MIB", "cpqRPMTrapType"),
        ("CPQRPM-MIB", "cpqRPMTrapSeverity"),
        ("CPQRPM-MIB", "cpqRPMTrapURL"))
)
if mibBuilder.loadTexts:
    cpqRPMTrapUPSOutputOverload.setStatus(
        ""
    )

cpqRPMTrapUPSOutputOverloadCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 154, 2, 0, 20015)
)
cpqRPMTrapUPSOutputOverloadCleared.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQRPM-MIB", "cpqRPMTrapDescription"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceId"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceName"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceAddress"),
        ("CPQRPM-MIB", "cpqRPMTrapType"),
        ("CPQRPM-MIB", "cpqRPMTrapSeverity"),
        ("CPQRPM-MIB", "cpqRPMTrapURL"))
)
if mibBuilder.loadTexts:
    cpqRPMTrapUPSOutputOverloadCleared.setStatus(
        ""
    )

cpqRPMTrapUPSBatteryDepleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 154, 2, 0, 20022)
)
cpqRPMTrapUPSBatteryDepleted.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQRPM-MIB", "cpqRPMTrapDescription"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceId"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceName"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceAddress"),
        ("CPQRPM-MIB", "cpqRPMTrapType"),
        ("CPQRPM-MIB", "cpqRPMTrapSeverity"))
)
if mibBuilder.loadTexts:
    cpqRPMTrapUPSBatteryDepleted.setStatus(
        ""
    )

cpqRPMTrapUPSBatteryLevelNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 154, 2, 0, 20023)
)
cpqRPMTrapUPSBatteryLevelNormal.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQRPM-MIB", "cpqRPMTrapDescription"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceId"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceName"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceAddress"),
        ("CPQRPM-MIB", "cpqRPMTrapType"),
        ("CPQRPM-MIB", "cpqRPMTrapSeverity"),
        ("CPQRPM-MIB", "cpqRPMTrapURL"))
)
if mibBuilder.loadTexts:
    cpqRPMTrapUPSBatteryLevelNormal.setStatus(
        ""
    )

cpqRPMTrapUPSOnBypass = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 154, 2, 0, 20032)
)
cpqRPMTrapUPSOnBypass.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQRPM-MIB", "cpqRPMTrapDescription"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceId"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceName"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceAddress"),
        ("CPQRPM-MIB", "cpqRPMTrapType"),
        ("CPQRPM-MIB", "cpqRPMTrapSeverity"))
)
if mibBuilder.loadTexts:
    cpqRPMTrapUPSOnBypass.setStatus(
        ""
    )

cpqRPMTrapUPSTemperatureLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 154, 2, 0, 20101)
)
cpqRPMTrapUPSTemperatureLow.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQRPM-MIB", "cpqRPMTrapDescription"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceId"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceName"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceAddress"),
        ("CPQRPM-MIB", "cpqRPMTrapType"),
        ("CPQRPM-MIB", "cpqRPMTrapSeverity"))
)
if mibBuilder.loadTexts:
    cpqRPMTrapUPSTemperatureLow.setStatus(
        ""
    )

cpqRPMTrapUPSTemperatureHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 154, 2, 0, 20102)
)
cpqRPMTrapUPSTemperatureHigh.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQRPM-MIB", "cpqRPMTrapDescription"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceId"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceName"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceAddress"),
        ("CPQRPM-MIB", "cpqRPMTrapType"),
        ("CPQRPM-MIB", "cpqRPMTrapSeverity"))
)
if mibBuilder.loadTexts:
    cpqRPMTrapUPSTemperatureHigh.setStatus(
        ""
    )

cpqRPMTrapUPSTemperatureNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 154, 2, 0, 20103)
)
cpqRPMTrapUPSTemperatureNormal.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQRPM-MIB", "cpqRPMTrapDescription"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceId"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceName"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceAddress"),
        ("CPQRPM-MIB", "cpqRPMTrapType"),
        ("CPQRPM-MIB", "cpqRPMTrapSeverity"),
        ("CPQRPM-MIB", "cpqRPMTrapURL"))
)
if mibBuilder.loadTexts:
    cpqRPMTrapUPSTemperatureNormal.setStatus(
        ""
    )

cpqRPMTrapUPSInternalFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 154, 2, 0, 20111)
)
cpqRPMTrapUPSInternalFailure.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQRPM-MIB", "cpqRPMTrapDescription"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceId"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceName"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceAddress"),
        ("CPQRPM-MIB", "cpqRPMTrapType"),
        ("CPQRPM-MIB", "cpqRPMTrapSeverity"),
        ("CPQRPM-MIB", "cpqRPMTrapURL"))
)
if mibBuilder.loadTexts:
    cpqRPMTrapUPSInternalFailure.setStatus(
        ""
    )

cpqRPMTrapUPSInternalFailureCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 154, 2, 0, 20112)
)
cpqRPMTrapUPSInternalFailureCleared.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQRPM-MIB", "cpqRPMTrapDescription"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceId"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceName"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceAddress"),
        ("CPQRPM-MIB", "cpqRPMTrapType"),
        ("CPQRPM-MIB", "cpqRPMTrapSeverity"),
        ("CPQRPM-MIB", "cpqRPMTrapURL"))
)
if mibBuilder.loadTexts:
    cpqRPMTrapUPSInternalFailureCleared.setStatus(
        ""
    )

cpqRPMTrapUPSBatteryFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 154, 2, 0, 20121)
)
cpqRPMTrapUPSBatteryFailure.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQRPM-MIB", "cpqRPMTrapDescription"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceId"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceName"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceAddress"),
        ("CPQRPM-MIB", "cpqRPMTrapType"),
        ("CPQRPM-MIB", "cpqRPMTrapSeverity"),
        ("CPQRPM-MIB", "cpqRPMTrapURL"))
)
if mibBuilder.loadTexts:
    cpqRPMTrapUPSBatteryFailure.setStatus(
        ""
    )

cpqRPMTrapUPSBatteryFailureCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 154, 2, 0, 20122)
)
cpqRPMTrapUPSBatteryFailureCleared.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQRPM-MIB", "cpqRPMTrapDescription"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceId"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceName"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceAddress"),
        ("CPQRPM-MIB", "cpqRPMTrapType"),
        ("CPQRPM-MIB", "cpqRPMTrapSeverity"),
        ("CPQRPM-MIB", "cpqRPMTrapURL"))
)
if mibBuilder.loadTexts:
    cpqRPMTrapUPSBatteryFailureCleared.setStatus(
        ""
    )

cpqRPMTrapUPSDiagnosticTestFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 154, 2, 0, 20131)
)
cpqRPMTrapUPSDiagnosticTestFailed.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQRPM-MIB", "cpqRPMTrapDescription"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceId"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceName"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceAddress"),
        ("CPQRPM-MIB", "cpqRPMTrapType"),
        ("CPQRPM-MIB", "cpqRPMTrapSeverity"))
)
if mibBuilder.loadTexts:
    cpqRPMTrapUPSDiagnosticTestFailed.setStatus(
        ""
    )

cpqRPMTrapUPSDiagnosticTestSucceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 154, 2, 0, 20132)
)
cpqRPMTrapUPSDiagnosticTestSucceeded.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQRPM-MIB", "cpqRPMTrapDescription"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceId"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceName"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceAddress"),
        ("CPQRPM-MIB", "cpqRPMTrapType"),
        ("CPQRPM-MIB", "cpqRPMTrapSeverity"))
)
if mibBuilder.loadTexts:
    cpqRPMTrapUPSDiagnosticTestSucceeded.setStatus(
        ""
    )

cpqRPMTrapUPSInputUnderOverFreq = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 154, 2, 0, 20141)
)
cpqRPMTrapUPSInputUnderOverFreq.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQRPM-MIB", "cpqRPMTrapDescription"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceId"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceName"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceAddress"),
        ("CPQRPM-MIB", "cpqRPMTrapType"),
        ("CPQRPM-MIB", "cpqRPMTrapSeverity"))
)
if mibBuilder.loadTexts:
    cpqRPMTrapUPSInputUnderOverFreq.setStatus(
        ""
    )

cpqRPMTrapUPSInputUnderOverFreqCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 154, 2, 0, 20142)
)
cpqRPMTrapUPSInputUnderOverFreqCleared.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQRPM-MIB", "cpqRPMTrapDescription"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceId"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceName"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceAddress"),
        ("CPQRPM-MIB", "cpqRPMTrapType"),
        ("CPQRPM-MIB", "cpqRPMTrapSeverity"))
)
if mibBuilder.loadTexts:
    cpqRPMTrapUPSInputUnderOverFreqCleared.setStatus(
        ""
    )

cppqRPMtrapUPSStartedOnBattery = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 154, 2, 0, 20151)
)
cppqRPMtrapUPSStartedOnBattery.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQRPM-MIB", "cpqRPMTrapDescription"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceId"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceName"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceAddress"),
        ("CPQRPM-MIB", "cpqRPMTrapType"),
        ("CPQRPM-MIB", "cpqRPMTrapSeverity"),
        ("CPQRPM-MIB", "cpqRPMTrapURL"))
)
if mibBuilder.loadTexts:
    cppqRPMtrapUPSStartedOnBattery.setStatus(
        ""
    )

cppqRPMtrapUPSStartedOnBatteryCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 154, 2, 0, 20152)
)
cppqRPMtrapUPSStartedOnBatteryCleared.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQRPM-MIB", "cpqRPMTrapDescription"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceId"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceName"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceAddress"),
        ("CPQRPM-MIB", "cpqRPMTrapType"),
        ("CPQRPM-MIB", "cpqRPMTrapSeverity"),
        ("CPQRPM-MIB", "cpqRPMTrapURL"))
)
if mibBuilder.loadTexts:
    cppqRPMtrapUPSStartedOnBatteryCleared.setStatus(
        ""
    )

cpqRPMTrapUPSBypassNotAvailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 154, 2, 0, 20161)
)
cpqRPMTrapUPSBypassNotAvailable.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQRPM-MIB", "cpqRPMTrapDescription"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceId"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceName"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceAddress"),
        ("CPQRPM-MIB", "cpqRPMTrapType"),
        ("CPQRPM-MIB", "cpqRPMTrapSeverity"),
        ("CPQRPM-MIB", "cpqRPMTrapURL"))
)
if mibBuilder.loadTexts:
    cpqRPMTrapUPSBypassNotAvailable.setStatus(
        ""
    )

cpqRPMTrapUPSBypassNotAvailableCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 154, 2, 0, 20162)
)
cpqRPMTrapUPSBypassNotAvailableCleared.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQRPM-MIB", "cpqRPMTrapDescription"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceId"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceName"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceAddress"),
        ("CPQRPM-MIB", "cpqRPMTrapType"),
        ("CPQRPM-MIB", "cpqRPMTrapSeverity"),
        ("CPQRPM-MIB", "cpqRPMTrapURL"))
)
if mibBuilder.loadTexts:
    cpqRPMTrapUPSBypassNotAvailableCleared.setStatus(
        ""
    )

cpqRPMTrapUPSUtilityFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 154, 2, 0, 20171)
)
cpqRPMTrapUPSUtilityFail.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQRPM-MIB", "cpqRPMTrapDescription"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceId"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceName"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceAddress"),
        ("CPQRPM-MIB", "cpqRPMTrapType"),
        ("CPQRPM-MIB", "cpqRPMTrapSeverity"))
)
if mibBuilder.loadTexts:
    cpqRPMTrapUPSUtilityFail.setStatus(
        ""
    )

cpqRPMTrapUPSUtilityFailCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 154, 2, 0, 20172)
)
cpqRPMTrapUPSUtilityFailCleared.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQRPM-MIB", "cpqRPMTrapDescription"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceId"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceName"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceAddress"),
        ("CPQRPM-MIB", "cpqRPMTrapType"),
        ("CPQRPM-MIB", "cpqRPMTrapSeverity"))
)
if mibBuilder.loadTexts:
    cpqRPMTrapUPSUtilityFailCleared.setStatus(
        ""
    )

cpqRPMTrapUPSUtilityNotPresent = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 154, 2, 0, 20181)
)
cpqRPMTrapUPSUtilityNotPresent.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQRPM-MIB", "cpqRPMTrapDescription"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceId"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceName"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceAddress"),
        ("CPQRPM-MIB", "cpqRPMTrapType"),
        ("CPQRPM-MIB", "cpqRPMTrapSeverity"))
)
if mibBuilder.loadTexts:
    cpqRPMTrapUPSUtilityNotPresent.setStatus(
        ""
    )

cpqRPMTrapUPSUtilityNotPresentCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 154, 2, 0, 20182)
)
cpqRPMTrapUPSUtilityNotPresentCleared.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQRPM-MIB", "cpqRPMTrapDescription"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceId"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceName"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceAddress"),
        ("CPQRPM-MIB", "cpqRPMTrapType"),
        ("CPQRPM-MIB", "cpqRPMTrapSeverity"))
)
if mibBuilder.loadTexts:
    cpqRPMTrapUPSUtilityNotPresentCleared.setStatus(
        ""
    )

cpqRPMTrapUPSBypassManualTurnedOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 154, 2, 0, 20191)
)
cpqRPMTrapUPSBypassManualTurnedOn.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQRPM-MIB", "cpqRPMTrapDescription"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceId"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceName"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceAddress"),
        ("CPQRPM-MIB", "cpqRPMTrapType"),
        ("CPQRPM-MIB", "cpqRPMTrapSeverity"))
)
if mibBuilder.loadTexts:
    cpqRPMTrapUPSBypassManualTurnedOn.setStatus(
        ""
    )

cpqRPMTrapUPSBypassManualTurnedOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 154, 2, 0, 20192)
)
cpqRPMTrapUPSBypassManualTurnedOff.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQRPM-MIB", "cpqRPMTrapDescription"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceId"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceName"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceAddress"),
        ("CPQRPM-MIB", "cpqRPMTrapType"),
        ("CPQRPM-MIB", "cpqRPMTrapSeverity"))
)
if mibBuilder.loadTexts:
    cpqRPMTrapUPSBypassManualTurnedOff.setStatus(
        ""
    )

cpqRPMTrapUPSSiteWiringFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 154, 2, 0, 20201)
)
cpqRPMTrapUPSSiteWiringFault.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQRPM-MIB", "cpqRPMTrapDescription"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceId"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceName"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceAddress"),
        ("CPQRPM-MIB", "cpqRPMTrapType"),
        ("CPQRPM-MIB", "cpqRPMTrapSeverity"),
        ("CPQRPM-MIB", "cpqRPMTrapURL"))
)
if mibBuilder.loadTexts:
    cpqRPMTrapUPSSiteWiringFault.setStatus(
        ""
    )

cpqRPMTrapUPSSiteWiringNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 154, 2, 0, 20202)
)
cpqRPMTrapUPSSiteWiringNormal.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQRPM-MIB", "cpqRPMTrapDescription"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceId"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceName"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceAddress"),
        ("CPQRPM-MIB", "cpqRPMTrapType"),
        ("CPQRPM-MIB", "cpqRPMTrapSeverity"),
        ("CPQRPM-MIB", "cpqRPMTrapURL"))
)
if mibBuilder.loadTexts:
    cpqRPMTrapUPSSiteWiringNormal.setStatus(
        ""
    )

cpqRPMtrapUPSTemperatureOutOfRange = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 154, 2, 0, 21007)
)
cpqRPMtrapUPSTemperatureOutOfRange.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQRPM-MIB", "cpqRPMTrapDescription"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceId"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceName"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceAddress"),
        ("CPQRPM-MIB", "cpqRPMTrapType"),
        ("CPQRPM-MIB", "cpqRPMTrapSeverity"),
        ("CPQRPM-MIB", "cpqRPMTrapURL"))
)
if mibBuilder.loadTexts:
    cpqRPMtrapUPSTemperatureOutOfRange.setStatus(
        ""
    )

cpqRPMtrapUPSTemperatureOutOfRangeCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 154, 2, 0, 21008)
)
cpqRPMtrapUPSTemperatureOutOfRangeCleared.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQRPM-MIB", "cpqRPMTrapDescription"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceId"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceName"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceAddress"),
        ("CPQRPM-MIB", "cpqRPMTrapType"),
        ("CPQRPM-MIB", "cpqRPMTrapSeverity"),
        ("CPQRPM-MIB", "cpqRPMTrapURL"))
)
if mibBuilder.loadTexts:
    cpqRPMtrapUPSTemperatureOutOfRangeCleared.setStatus(
        ""
    )

cpqRPMTrapUPSShutdownPending = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 154, 2, 0, 21011)
)
cpqRPMTrapUPSShutdownPending.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQRPM-MIB", "cpqRPMTrapDescription"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceId"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceName"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceAddress"),
        ("CPQRPM-MIB", "cpqRPMTrapType"),
        ("CPQRPM-MIB", "cpqRPMTrapSeverity"),
        ("CPQRPM-MIB", "cpqRPMTrapURL"))
)
if mibBuilder.loadTexts:
    cpqRPMTrapUPSShutdownPending.setStatus(
        ""
    )

cpqRPMTrapUPSShutdownPendingCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 154, 2, 0, 21012)
)
cpqRPMTrapUPSShutdownPendingCleared.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQRPM-MIB", "cpqRPMTrapDescription"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceId"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceName"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceAddress"),
        ("CPQRPM-MIB", "cpqRPMTrapType"),
        ("CPQRPM-MIB", "cpqRPMTrapSeverity"),
        ("CPQRPM-MIB", "cpqRPMTrapURL"))
)
if mibBuilder.loadTexts:
    cpqRPMTrapUPSShutdownPendingCleared.setStatus(
        ""
    )

cpqRPMTrapUPSShutdownImminent = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 154, 2, 0, 21013)
)
cpqRPMTrapUPSShutdownImminent.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQRPM-MIB", "cpqRPMTrapDescription"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceId"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceName"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceAddress"),
        ("CPQRPM-MIB", "cpqRPMTrapType"),
        ("CPQRPM-MIB", "cpqRPMTrapSeverity"),
        ("CPQRPM-MIB", "cpqRPMTrapURL"))
)
if mibBuilder.loadTexts:
    cpqRPMTrapUPSShutdownImminent.setStatus(
        ""
    )

cpqRPMTrapUPSShutdownImminentCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 154, 2, 0, 21014)
)
cpqRPMTrapUPSShutdownImminentCleared.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQRPM-MIB", "cpqRPMTrapDescription"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceId"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceName"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceAddress"),
        ("CPQRPM-MIB", "cpqRPMTrapType"),
        ("CPQRPM-MIB", "cpqRPMTrapSeverity"),
        ("CPQRPM-MIB", "cpqRPMTrapURL"))
)
if mibBuilder.loadTexts:
    cpqRPMTrapUPSShutdownImminentCleared.setStatus(
        ""
    )

cpqRPMtrapUPSOutputoutofRange = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 154, 2, 0, 21019)
)
cpqRPMtrapUPSOutputoutofRange.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQRPM-MIB", "cpqRPMTrapDescription"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceId"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceName"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceAddress"),
        ("CPQRPM-MIB", "cpqRPMTrapType"),
        ("CPQRPM-MIB", "cpqRPMTrapSeverity"),
        ("CPQRPM-MIB", "cpqRPMTrapURL"))
)
if mibBuilder.loadTexts:
    cpqRPMtrapUPSOutputoutofRange.setStatus(
        ""
    )

cpqRPMTrapUPSOutputVoltageNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 154, 2, 0, 21020)
)
cpqRPMTrapUPSOutputVoltageNormal.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQRPM-MIB", "cpqRPMTrapDescription"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceId"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceName"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceAddress"),
        ("CPQRPM-MIB", "cpqRPMTrapType"),
        ("CPQRPM-MIB", "cpqRPMTrapSeverity"),
        ("CPQRPM-MIB", "cpqRPMTrapURL"))
)
if mibBuilder.loadTexts:
    cpqRPMTrapUPSOutputVoltageNormal.setStatus(
        ""
    )

cpqRPMtrapUPSInputOutofRange = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 154, 2, 0, 21021)
)
cpqRPMtrapUPSInputOutofRange.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQRPM-MIB", "cpqRPMTrapDescription"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceId"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceName"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceAddress"),
        ("CPQRPM-MIB", "cpqRPMTrapType"),
        ("CPQRPM-MIB", "cpqRPMTrapSeverity"),
        ("CPQRPM-MIB", "cpqRPMTrapURL"))
)
if mibBuilder.loadTexts:
    cpqRPMtrapUPSInputOutofRange.setStatus(
        ""
    )

cpqRPMtrapUPSInputOutofRangeCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 154, 2, 0, 21022)
)
cpqRPMtrapUPSInputOutofRangeCleared.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQRPM-MIB", "cpqRPMTrapDescription"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceId"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceName"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceAddress"),
        ("CPQRPM-MIB", "cpqRPMTrapType"),
        ("CPQRPM-MIB", "cpqRPMTrapSeverity"),
        ("CPQRPM-MIB", "cpqRPMTrapURL"))
)
if mibBuilder.loadTexts:
    cpqRPMtrapUPSInputOutofRangeCleared.setStatus(
        ""
    )

cpqRPMTrapUPSLossOfRedundancy = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 154, 2, 0, 21023)
)
cpqRPMTrapUPSLossOfRedundancy.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQRPM-MIB", "cpqRPMTrapDescription"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceId"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceName"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceAddress"),
        ("CPQRPM-MIB", "cpqRPMTrapType"),
        ("CPQRPM-MIB", "cpqRPMTrapSeverity"),
        ("CPQRPM-MIB", "cpqRPMTrapURL"))
)
if mibBuilder.loadTexts:
    cpqRPMTrapUPSLossOfRedundancy.setStatus(
        ""
    )

cpqRPMTrapUPSLossOfRedundancyCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 154, 2, 0, 21024)
)
cpqRPMTrapUPSLossOfRedundancyCleared.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQRPM-MIB", "cpqRPMTrapDescription"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceId"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceName"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceAddress"),
        ("CPQRPM-MIB", "cpqRPMTrapType"),
        ("CPQRPM-MIB", "cpqRPMTrapSeverity"),
        ("CPQRPM-MIB", "cpqRPMTrapURL"))
)
if mibBuilder.loadTexts:
    cpqRPMTrapUPSLossOfRedundancyCleared.setStatus(
        ""
    )

cpqRPMTrapUPSOnBuck = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 154, 2, 0, 21029)
)
cpqRPMTrapUPSOnBuck.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQRPM-MIB", "cpqRPMTrapDescription"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceId"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceName"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceAddress"),
        ("CPQRPM-MIB", "cpqRPMTrapType"),
        ("CPQRPM-MIB", "cpqRPMTrapSeverity"))
)
if mibBuilder.loadTexts:
    cpqRPMTrapUPSOnBuck.setStatus(
        ""
    )

cpqRPMTrapUPSOnBoost = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 154, 2, 0, 21031)
)
cpqRPMTrapUPSOnBoost.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQRPM-MIB", "cpqRPMTrapDescription"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceId"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceName"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceAddress"),
        ("CPQRPM-MIB", "cpqRPMTrapType"),
        ("CPQRPM-MIB", "cpqRPMTrapSeverity"))
)
if mibBuilder.loadTexts:
    cpqRPMTrapUPSOnBoost.setStatus(
        ""
    )

cpqRPMTrapUPSManualLoadDumped = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 154, 2, 0, 21033)
)
cpqRPMTrapUPSManualLoadDumped.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQRPM-MIB", "cpqRPMTrapDescription"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceId"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceName"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceAddress"),
        ("CPQRPM-MIB", "cpqRPMTrapType"),
        ("CPQRPM-MIB", "cpqRPMTrapSeverity"),
        ("CPQRPM-MIB", "cpqRPMTrapURL"))
)
if mibBuilder.loadTexts:
    cpqRPMTrapUPSManualLoadDumped.setStatus(
        ""
    )

cpqRPMTrapUPSManualLoadDumpedCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 154, 2, 0, 21034)
)
cpqRPMTrapUPSManualLoadDumpedCleared.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQRPM-MIB", "cpqRPMTrapDescription"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceId"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceName"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceAddress"),
        ("CPQRPM-MIB", "cpqRPMTrapType"),
        ("CPQRPM-MIB", "cpqRPMTrapSeverity"),
        ("CPQRPM-MIB", "cpqRPMTrapURL"))
)
if mibBuilder.loadTexts:
    cpqRPMTrapUPSManualLoadDumpedCleared.setStatus(
        ""
    )

cpqRPMTrapUPSFanFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 154, 2, 0, 21035)
)
cpqRPMTrapUPSFanFailure.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQRPM-MIB", "cpqRPMTrapDescription"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceId"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceName"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceAddress"),
        ("CPQRPM-MIB", "cpqRPMTrapType"),
        ("CPQRPM-MIB", "cpqRPMTrapSeverity"),
        ("CPQRPM-MIB", "cpqRPMTrapURL"))
)
if mibBuilder.loadTexts:
    cpqRPMTrapUPSFanFailure.setStatus(
        ""
    )

cpqRPMTrapUPSFanFailureCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 154, 2, 0, 21036)
)
cpqRPMTrapUPSFanFailureCleared.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQRPM-MIB", "cpqRPMTrapDescription"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceId"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceName"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceAddress"),
        ("CPQRPM-MIB", "cpqRPMTrapType"),
        ("CPQRPM-MIB", "cpqRPMTrapSeverity"),
        ("CPQRPM-MIB", "cpqRPMTrapURL"))
)
if mibBuilder.loadTexts:
    cpqRPMTrapUPSFanFailureCleared.setStatus(
        ""
    )

cpqRPMTrapUPSEPOInitiated = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 154, 2, 0, 21037)
)
cpqRPMTrapUPSEPOInitiated.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQRPM-MIB", "cpqRPMTrapDescription"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceId"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceName"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceAddress"),
        ("CPQRPM-MIB", "cpqRPMTrapType"),
        ("CPQRPM-MIB", "cpqRPMTrapSeverity"),
        ("CPQRPM-MIB", "cpqRPMTrapURL"))
)
if mibBuilder.loadTexts:
    cpqRPMTrapUPSEPOInitiated.setStatus(
        ""
    )

cpqRPMTrapUPSCheckBreaker = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 154, 2, 0, 21041)
)
cpqRPMTrapUPSCheckBreaker.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQRPM-MIB", "cpqRPMTrapDescription"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceId"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceName"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceAddress"),
        ("CPQRPM-MIB", "cpqRPMTrapType"),
        ("CPQRPM-MIB", "cpqRPMTrapSeverity"),
        ("CPQRPM-MIB", "cpqRPMTrapURL"))
)
if mibBuilder.loadTexts:
    cpqRPMTrapUPSCheckBreaker.setStatus(
        ""
    )

cpqRPMTrapUPSCheckBreakerCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 154, 2, 0, 21042)
)
cpqRPMTrapUPSCheckBreakerCleared.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQRPM-MIB", "cpqRPMTrapDescription"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceId"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceName"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceAddress"),
        ("CPQRPM-MIB", "cpqRPMTrapType"),
        ("CPQRPM-MIB", "cpqRPMTrapSeverity"),
        ("CPQRPM-MIB", "cpqRPMTrapURL"))
)
if mibBuilder.loadTexts:
    cpqRPMTrapUPSCheckBreakerCleared.setStatus(
        ""
    )

cpqRPMTrapUPSCabinetDoorOpen = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 154, 2, 0, 21045)
)
cpqRPMTrapUPSCabinetDoorOpen.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQRPM-MIB", "cpqRPMTrapDescription"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceId"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceName"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceAddress"),
        ("CPQRPM-MIB", "cpqRPMTrapType"),
        ("CPQRPM-MIB", "cpqRPMTrapSeverity"),
        ("CPQRPM-MIB", "cpqRPMTrapURL"))
)
if mibBuilder.loadTexts:
    cpqRPMTrapUPSCabinetDoorOpen.setStatus(
        ""
    )

cpqRPMTrapUPSCabinetDoorOpenCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 154, 2, 0, 21046)
)
cpqRPMTrapUPSCabinetDoorOpenCleared.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQRPM-MIB", "cpqRPMTrapDescription"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceId"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceName"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceAddress"),
        ("CPQRPM-MIB", "cpqRPMTrapType"),
        ("CPQRPM-MIB", "cpqRPMTrapSeverity"),
        ("CPQRPM-MIB", "cpqRPMTrapURL"))
)
if mibBuilder.loadTexts:
    cpqRPMTrapUPSCabinetDoorOpenCleared.setStatus(
        ""
    )

cpqRPMtrapUPSBypassOnAuto = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 154, 2, 0, 21047)
)
cpqRPMtrapUPSBypassOnAuto.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQRPM-MIB", "cpqRPMTrapDescription"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceId"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceName"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceAddress"),
        ("CPQRPM-MIB", "cpqRPMTrapType"),
        ("CPQRPM-MIB", "cpqRPMTrapSeverity"),
        ("CPQRPM-MIB", "cpqRPMTrapURL"))
)
if mibBuilder.loadTexts:
    cpqRPMtrapUPSBypassOnAuto.setStatus(
        ""
    )

cpqRPMtrapUPSBypassOnAutoCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 154, 2, 0, 21048)
)
cpqRPMtrapUPSBypassOnAutoCleared.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQRPM-MIB", "cpqRPMTrapDescription"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceId"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceName"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceAddress"),
        ("CPQRPM-MIB", "cpqRPMTrapType"),
        ("CPQRPM-MIB", "cpqRPMTrapSeverity"),
        ("CPQRPM-MIB", "cpqRPMTrapURL"))
)
if mibBuilder.loadTexts:
    cpqRPMtrapUPSBypassOnAutoCleared.setStatus(
        ""
    )

cpqRPMTrapUPSBatteriesDisconnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 154, 2, 0, 21053)
)
cpqRPMTrapUPSBatteriesDisconnected.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQRPM-MIB", "cpqRPMTrapDescription"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceId"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceName"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceAddress"),
        ("CPQRPM-MIB", "cpqRPMTrapType"),
        ("CPQRPM-MIB", "cpqRPMTrapSeverity"),
        ("CPQRPM-MIB", "cpqRPMTrapURL"))
)
if mibBuilder.loadTexts:
    cpqRPMTrapUPSBatteriesDisconnected.setStatus(
        ""
    )

cpqRPMTrapUPSBatteriesDisconnectedCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 154, 2, 0, 21054)
)
cpqRPMTrapUPSBatteriesDisconnectedCleared.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQRPM-MIB", "cpqRPMTrapDescription"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceId"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceName"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceAddress"),
        ("CPQRPM-MIB", "cpqRPMTrapType"),
        ("CPQRPM-MIB", "cpqRPMTrapSeverity"),
        ("CPQRPM-MIB", "cpqRPMTrapURL"))
)
if mibBuilder.loadTexts:
    cpqRPMTrapUPSBatteriesDisconnectedCleared.setStatus(
        ""
    )

cpqRPMTrapUPSBatteryLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 154, 2, 0, 21055)
)
cpqRPMTrapUPSBatteryLow.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQRPM-MIB", "cpqRPMTrapDescription"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceId"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceName"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceAddress"),
        ("CPQRPM-MIB", "cpqRPMTrapType"),
        ("CPQRPM-MIB", "cpqRPMTrapSeverity"),
        ("CPQRPM-MIB", "cpqRPMTrapURL"))
)
if mibBuilder.loadTexts:
    cpqRPMTrapUPSBatteryLow.setStatus(
        ""
    )

cpqRPMTrapUPSBatteryLowCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 154, 2, 0, 21056)
)
cpqRPMTrapUPSBatteryLowCleared.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQRPM-MIB", "cpqRPMTrapDescription"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceId"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceName"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceAddress"),
        ("CPQRPM-MIB", "cpqRPMTrapType"),
        ("CPQRPM-MIB", "cpqRPMTrapSeverity"),
        ("CPQRPM-MIB", "cpqRPMTrapURL"))
)
if mibBuilder.loadTexts:
    cpqRPMTrapUPSBatteryLowCleared.setStatus(
        ""
    )

cpqRPMTrapUPSBatteryDischarged = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 154, 2, 0, 21057)
)
cpqRPMTrapUPSBatteryDischarged.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQRPM-MIB", "cpqRPMTrapDescription"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceId"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceName"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceAddress"),
        ("CPQRPM-MIB", "cpqRPMTrapType"),
        ("CPQRPM-MIB", "cpqRPMTrapSeverity"),
        ("CPQRPM-MIB", "cpqRPMTrapURL"))
)
if mibBuilder.loadTexts:
    cpqRPMTrapUPSBatteryDischarged.setStatus(
        ""
    )

cpqRPMTrapUPSBatteryDischargedCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 154, 2, 0, 21058)
)
cpqRPMTrapUPSBatteryDischargedCleared.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQRPM-MIB", "cpqRPMTrapDescription"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceId"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceName"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceAddress"),
        ("CPQRPM-MIB", "cpqRPMTrapType"),
        ("CPQRPM-MIB", "cpqRPMTrapSeverity"),
        ("CPQRPM-MIB", "cpqRPMTrapURL"))
)
if mibBuilder.loadTexts:
    cpqRPMTrapUPSBatteryDischargedCleared.setStatus(
        ""
    )

cpqRPMtrapUPSBypassONManual = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 154, 2, 0, 21059)
)
cpqRPMtrapUPSBypassONManual.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQRPM-MIB", "cpqRPMTrapDescription"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceId"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceName"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceAddress"),
        ("CPQRPM-MIB", "cpqRPMTrapType"),
        ("CPQRPM-MIB", "cpqRPMTrapSeverity"),
        ("CPQRPM-MIB", "cpqRPMTrapURL"))
)
if mibBuilder.loadTexts:
    cpqRPMtrapUPSBypassONManual.setStatus(
        ""
    )

cpqRPMtrapUPSBypassOffManual = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 154, 2, 0, 21060)
)
cpqRPMtrapUPSBypassOffManual.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQRPM-MIB", "cpqRPMTrapDescription"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceId"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceName"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceAddress"),
        ("CPQRPM-MIB", "cpqRPMTrapType"),
        ("CPQRPM-MIB", "cpqRPMTrapSeverity"),
        ("CPQRPM-MIB", "cpqRPMTrapURL"))
)
if mibBuilder.loadTexts:
    cpqRPMtrapUPSBypassOffManual.setStatus(
        ""
    )

cpqRPMTrapUPSOnBattery = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 154, 2, 0, 21063)
)
cpqRPMTrapUPSOnBattery.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQRPM-MIB", "cpqRPMTrapDescription"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceId"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceName"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceAddress"),
        ("CPQRPM-MIB", "cpqRPMTrapType"),
        ("CPQRPM-MIB", "cpqRPMTrapSeverity"),
        ("CPQRPM-MIB", "cpqRPMTrapURL"))
)
if mibBuilder.loadTexts:
    cpqRPMTrapUPSOnBattery.setStatus(
        ""
    )

cpqRPMTrapUPSOnUtilityPower = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 154, 2, 0, 21064)
)
cpqRPMTrapUPSOnUtilityPower.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQRPM-MIB", "cpqRPMTrapDescription"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceId"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceName"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceAddress"),
        ("CPQRPM-MIB", "cpqRPMTrapType"),
        ("CPQRPM-MIB", "cpqRPMTrapSeverity"),
        ("CPQRPM-MIB", "cpqRPMTrapURL"))
)
if mibBuilder.loadTexts:
    cpqRPMTrapUPSOnUtilityPower.setStatus(
        ""
    )

cpqRPMTrapUPSDCStartOccurred = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 154, 2, 0, 29998)
)
cpqRPMTrapUPSDCStartOccurred.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQRPM-MIB", "cpqRPMTrapDescription"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceId"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceName"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceAddress"),
        ("CPQRPM-MIB", "cpqRPMTrapType"),
        ("CPQRPM-MIB", "cpqRPMTrapSeverity"))
)
if mibBuilder.loadTexts:
    cpqRPMTrapUPSDCStartOccurred.setStatus(
        ""
    )

cpqRPMTrapUPSDCStartOccurredCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 154, 2, 0, 29999)
)
cpqRPMTrapUPSDCStartOccurredCleared.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQRPM-MIB", "cpqRPMTrapDescription"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceId"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceName"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceAddress"),
        ("CPQRPM-MIB", "cpqRPMTrapType"),
        ("CPQRPM-MIB", "cpqRPMTrapSeverity"))
)
if mibBuilder.loadTexts:
    cpqRPMTrapUPSDCStartOccurredCleared.setStatus(
        ""
    )

cpqRPMTestTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 154, 2, 0, 50001)
)
cpqRPMTestTrap.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQRPM-MIB", "cpqRPMTrapDescription"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceId"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceName"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceAddress"),
        ("CPQRPM-MIB", "cpqRPMTrapType"),
        ("CPQRPM-MIB", "cpqRPMTrapSeverity"))
)
if mibBuilder.loadTexts:
    cpqRPMTestTrap.setStatus(
        ""
    )

cpqPMTrapCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 154, 3, 0, 1)
)
cpqPMTrapCritical.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQRPM-MIB", "cpqRPMTrapCode"),
        ("CPQRPM-MIB", "cpqRPMTrapDescription"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceName"),
        ("CPQRPM-MIB", "cpqRPMTrapURL"))
)
if mibBuilder.loadTexts:
    cpqPMTrapCritical.setStatus(
        ""
    )

cpqPMTrapWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 154, 3, 0, 2)
)
cpqPMTrapWarning.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQRPM-MIB", "cpqRPMTrapCode"),
        ("CPQRPM-MIB", "cpqRPMTrapDescription"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceName"),
        ("CPQRPM-MIB", "cpqRPMTrapURL"))
)
if mibBuilder.loadTexts:
    cpqPMTrapWarning.setStatus(
        ""
    )

cpqPMTrapInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 154, 3, 0, 3)
)
cpqPMTrapInformation.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQRPM-MIB", "cpqRPMTrapCode"),
        ("CPQRPM-MIB", "cpqRPMTrapDescription"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceName"),
        ("CPQRPM-MIB", "cpqRPMTrapURL"))
)
if mibBuilder.loadTexts:
    cpqPMTrapInformation.setStatus(
        ""
    )

cpqPMTrapCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 154, 3, 0, 4)
)
cpqPMTrapCleared.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQRPM-MIB", "cpqRPMTrapCode"),
        ("CPQRPM-MIB", "cpqRPMTrapDescription"),
        ("CPQRPM-MIB", "cpqRPMTrapDeviceName"),
        ("CPQRPM-MIB", "cpqRPMTrapURL"))
)
if mibBuilder.loadTexts:
    cpqPMTrapCleared.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CPQRPM-MIB",
    **{"cpqRPM": cpqRPM,
       "cpqRPMTrapInfo": cpqRPMTrapInfo,
       "cpqRPMTrapDescription": cpqRPMTrapDescription,
       "cpqRPMTrapDeviceId": cpqRPMTrapDeviceId,
       "cpqRPMTrapDeviceName": cpqRPMTrapDeviceName,
       "cpqRPMTrapDeviceAddress": cpqRPMTrapDeviceAddress,
       "cpqRPMTrapType": cpqRPMTrapType,
       "cpqRPMTrapSeverity": cpqRPMTrapSeverity,
       "cpqRPMTrapCode": cpqRPMTrapCode,
       "cpqRPMTrapURL": cpqRPMTrapURL,
       "cpqRPMTraps": cpqRPMTraps,
       "cpqRPMTrapDeviceConnected": cpqRPMTrapDeviceConnected,
       "cpqRPMTrapConnectionLost": cpqRPMTrapConnectionLost,
       "cpqRPMTrapLookupFailed": cpqRPMTrapLookupFailed,
       "cpqRPMTrapConnectionFailed": cpqRPMTrapConnectionFailed,
       "cpqRPMTrapDeviceSettingsChanged": cpqRPMTrapDeviceSettingsChanged,
       "cpqRPMTrapCMCTemp1BelowMin": cpqRPMTrapCMCTemp1BelowMin,
       "cpqRPMTrapCMCTemp1AboveWarn": cpqRPMTrapCMCTemp1AboveWarn,
       "cpqRPMTrapCMCTemp1AboveMax": cpqRPMTrapCMCTemp1AboveMax,
       "cpqRPMTrapCMCTemp1Normal": cpqRPMTrapCMCTemp1Normal,
       "cpqRPMTrapCMCTemp2BelowMin": cpqRPMTrapCMCTemp2BelowMin,
       "cpqRPMTrapCMCTemp2AboveWarn": cpqRPMTrapCMCTemp2AboveWarn,
       "cpqRPMTrapCMCTemp2AboveMax": cpqRPMTrapCMCTemp2AboveMax,
       "cpqRPMTrapCMCTemp2Normal": cpqRPMTrapCMCTemp2Normal,
       "cpqRPMTrapCMCVoltUnder": cpqRPMTrapCMCVoltUnder,
       "cpqRPMTrapCMCVoltOver": cpqRPMTrapCMCVoltOver,
       "cpqRPMTrapCMCVoltNormal": cpqRPMTrapCMCVoltNormal,
       "cpqRPMTrapCMCHmdtUnder": cpqRPMTrapCMCHmdtUnder,
       "cpqRPMTrapCMCHmdtOver": cpqRPMTrapCMCHmdtOver,
       "cpqRPMTrapCMCHmdtNormal": cpqRPMTrapCMCHmdtNormal,
       "cpqRPMTrapCMCSmokeDetected": cpqRPMTrapCMCSmokeDetected,
       "cpqRPMTrapCMCSmokeCleared": cpqRPMTrapCMCSmokeCleared,
       "cpqRPMTrapCMCShockDetected": cpqRPMTrapCMCShockDetected,
       "cpqRPMTrapCMCShockCleared": cpqRPMTrapCMCShockCleared,
       "cpqRPMTrapCMCAux1Alarm": cpqRPMTrapCMCAux1Alarm,
       "cpqRPMTrapCMCAux1Cleared": cpqRPMTrapCMCAux1Cleared,
       "cpqRPMTrapCMCAux2Alarm": cpqRPMTrapCMCAux2Alarm,
       "cpqRPMTrapCMCAux2Cleared": cpqRPMTrapCMCAux2Cleared,
       "cpqRPMTrapCMCInput1Opened": cpqRPMTrapCMCInput1Opened,
       "cpqRPMTrapCMCInput1Closed": cpqRPMTrapCMCInput1Closed,
       "cpqRPMTrapCMCInput2Opened": cpqRPMTrapCMCInput2Opened,
       "cpqRPMTrapCMCInput2Closed": cpqRPMTrapCMCInput2Closed,
       "cpqRPMTrapCMCInput3Opened": cpqRPMTrapCMCInput3Opened,
       "cpqRPMTrapCMCInput3Closed": cpqRPMTrapCMCInput3Closed,
       "cpqRPMTrapCMCInput4Opened": cpqRPMTrapCMCInput4Opened,
       "cpqRPMTrapCMCInput4Closed": cpqRPMTrapCMCInput4Closed,
       "cpqRPMTrapCMCLockset1Unlocked": cpqRPMTrapCMCLockset1Unlocked,
       "cpqRPMTrapCMCLockset1FailedToLock": cpqRPMTrapCMCLockset1FailedToLock,
       "cpqRPMTrapCMCLockset1Error": cpqRPMTrapCMCLockset1Error,
       "cpqRPMTrapCMCLockset1Locked": cpqRPMTrapCMCLockset1Locked,
       "cpqRPMTrapCMCLockset2Unlocked": cpqRPMTrapCMCLockset2Unlocked,
       "cpqRPMTrapCMCLockset2FailedToLock": cpqRPMTrapCMCLockset2FailedToLock,
       "cpqRPMTrapCMCLockset2Error": cpqRPMTrapCMCLockset2Error,
       "cpqRPMTrapCMCLockset2Locked": cpqRPMTrapCMCLockset2Locked,
       "cpqRPMTrapCMCLockset1Normal": cpqRPMTrapCMCLockset1Normal,
       "cpqRPMTrapCMCLockset2Normal": cpqRPMTrapCMCLockset2Normal,
       "cpqRPMTrapUPSInputVoltageBelowMin": cpqRPMTrapUPSInputVoltageBelowMin,
       "cpqRPMTrapUPSInputVoltageAboveMax": cpqRPMTrapUPSInputVoltageAboveMax,
       "cpqRPMTrapUPSInputVoltageNormal": cpqRPMTrapUPSInputVoltageNormal,
       "cpqRPMTrapUPSOutputVoltageBelowMin": cpqRPMTrapUPSOutputVoltageBelowMin,
       "cpqRPMTrapUPSOutputVoltageAboveMax": cpqRPMTrapUPSOutputVoltageAboveMax,
       "cpqRPMTrapUPSOutputOverload": cpqRPMTrapUPSOutputOverload,
       "cpqRPMTrapUPSOutputOverloadCleared": cpqRPMTrapUPSOutputOverloadCleared,
       "cpqRPMTrapUPSBatteryDepleted": cpqRPMTrapUPSBatteryDepleted,
       "cpqRPMTrapUPSBatteryLevelNormal": cpqRPMTrapUPSBatteryLevelNormal,
       "cpqRPMTrapUPSOnBypass": cpqRPMTrapUPSOnBypass,
       "cpqRPMTrapUPSTemperatureLow": cpqRPMTrapUPSTemperatureLow,
       "cpqRPMTrapUPSTemperatureHigh": cpqRPMTrapUPSTemperatureHigh,
       "cpqRPMTrapUPSTemperatureNormal": cpqRPMTrapUPSTemperatureNormal,
       "cpqRPMTrapUPSInternalFailure": cpqRPMTrapUPSInternalFailure,
       "cpqRPMTrapUPSInternalFailureCleared": cpqRPMTrapUPSInternalFailureCleared,
       "cpqRPMTrapUPSBatteryFailure": cpqRPMTrapUPSBatteryFailure,
       "cpqRPMTrapUPSBatteryFailureCleared": cpqRPMTrapUPSBatteryFailureCleared,
       "cpqRPMTrapUPSDiagnosticTestFailed": cpqRPMTrapUPSDiagnosticTestFailed,
       "cpqRPMTrapUPSDiagnosticTestSucceeded": cpqRPMTrapUPSDiagnosticTestSucceeded,
       "cpqRPMTrapUPSInputUnderOverFreq": cpqRPMTrapUPSInputUnderOverFreq,
       "cpqRPMTrapUPSInputUnderOverFreqCleared": cpqRPMTrapUPSInputUnderOverFreqCleared,
       "cppqRPMtrapUPSStartedOnBattery": cppqRPMtrapUPSStartedOnBattery,
       "cppqRPMtrapUPSStartedOnBatteryCleared": cppqRPMtrapUPSStartedOnBatteryCleared,
       "cpqRPMTrapUPSBypassNotAvailable": cpqRPMTrapUPSBypassNotAvailable,
       "cpqRPMTrapUPSBypassNotAvailableCleared": cpqRPMTrapUPSBypassNotAvailableCleared,
       "cpqRPMTrapUPSUtilityFail": cpqRPMTrapUPSUtilityFail,
       "cpqRPMTrapUPSUtilityFailCleared": cpqRPMTrapUPSUtilityFailCleared,
       "cpqRPMTrapUPSUtilityNotPresent": cpqRPMTrapUPSUtilityNotPresent,
       "cpqRPMTrapUPSUtilityNotPresentCleared": cpqRPMTrapUPSUtilityNotPresentCleared,
       "cpqRPMTrapUPSBypassManualTurnedOn": cpqRPMTrapUPSBypassManualTurnedOn,
       "cpqRPMTrapUPSBypassManualTurnedOff": cpqRPMTrapUPSBypassManualTurnedOff,
       "cpqRPMTrapUPSSiteWiringFault": cpqRPMTrapUPSSiteWiringFault,
       "cpqRPMTrapUPSSiteWiringNormal": cpqRPMTrapUPSSiteWiringNormal,
       "cpqRPMtrapUPSTemperatureOutOfRange": cpqRPMtrapUPSTemperatureOutOfRange,
       "cpqRPMtrapUPSTemperatureOutOfRangeCleared": cpqRPMtrapUPSTemperatureOutOfRangeCleared,
       "cpqRPMTrapUPSShutdownPending": cpqRPMTrapUPSShutdownPending,
       "cpqRPMTrapUPSShutdownPendingCleared": cpqRPMTrapUPSShutdownPendingCleared,
       "cpqRPMTrapUPSShutdownImminent": cpqRPMTrapUPSShutdownImminent,
       "cpqRPMTrapUPSShutdownImminentCleared": cpqRPMTrapUPSShutdownImminentCleared,
       "cpqRPMtrapUPSOutputoutofRange": cpqRPMtrapUPSOutputoutofRange,
       "cpqRPMTrapUPSOutputVoltageNormal": cpqRPMTrapUPSOutputVoltageNormal,
       "cpqRPMtrapUPSInputOutofRange": cpqRPMtrapUPSInputOutofRange,
       "cpqRPMtrapUPSInputOutofRangeCleared": cpqRPMtrapUPSInputOutofRangeCleared,
       "cpqRPMTrapUPSLossOfRedundancy": cpqRPMTrapUPSLossOfRedundancy,
       "cpqRPMTrapUPSLossOfRedundancyCleared": cpqRPMTrapUPSLossOfRedundancyCleared,
       "cpqRPMTrapUPSOnBuck": cpqRPMTrapUPSOnBuck,
       "cpqRPMTrapUPSOnBoost": cpqRPMTrapUPSOnBoost,
       "cpqRPMTrapUPSManualLoadDumped": cpqRPMTrapUPSManualLoadDumped,
       "cpqRPMTrapUPSManualLoadDumpedCleared": cpqRPMTrapUPSManualLoadDumpedCleared,
       "cpqRPMTrapUPSFanFailure": cpqRPMTrapUPSFanFailure,
       "cpqRPMTrapUPSFanFailureCleared": cpqRPMTrapUPSFanFailureCleared,
       "cpqRPMTrapUPSEPOInitiated": cpqRPMTrapUPSEPOInitiated,
       "cpqRPMTrapUPSCheckBreaker": cpqRPMTrapUPSCheckBreaker,
       "cpqRPMTrapUPSCheckBreakerCleared": cpqRPMTrapUPSCheckBreakerCleared,
       "cpqRPMTrapUPSCabinetDoorOpen": cpqRPMTrapUPSCabinetDoorOpen,
       "cpqRPMTrapUPSCabinetDoorOpenCleared": cpqRPMTrapUPSCabinetDoorOpenCleared,
       "cpqRPMtrapUPSBypassOnAuto": cpqRPMtrapUPSBypassOnAuto,
       "cpqRPMtrapUPSBypassOnAutoCleared": cpqRPMtrapUPSBypassOnAutoCleared,
       "cpqRPMTrapUPSBatteriesDisconnected": cpqRPMTrapUPSBatteriesDisconnected,
       "cpqRPMTrapUPSBatteriesDisconnectedCleared": cpqRPMTrapUPSBatteriesDisconnectedCleared,
       "cpqRPMTrapUPSBatteryLow": cpqRPMTrapUPSBatteryLow,
       "cpqRPMTrapUPSBatteryLowCleared": cpqRPMTrapUPSBatteryLowCleared,
       "cpqRPMTrapUPSBatteryDischarged": cpqRPMTrapUPSBatteryDischarged,
       "cpqRPMTrapUPSBatteryDischargedCleared": cpqRPMTrapUPSBatteryDischargedCleared,
       "cpqRPMtrapUPSBypassONManual": cpqRPMtrapUPSBypassONManual,
       "cpqRPMtrapUPSBypassOffManual": cpqRPMtrapUPSBypassOffManual,
       "cpqRPMTrapUPSOnBattery": cpqRPMTrapUPSOnBattery,
       "cpqRPMTrapUPSOnUtilityPower": cpqRPMTrapUPSOnUtilityPower,
       "cpqRPMTrapUPSDCStartOccurred": cpqRPMTrapUPSDCStartOccurred,
       "cpqRPMTrapUPSDCStartOccurredCleared": cpqRPMTrapUPSDCStartOccurredCleared,
       "cpqRPMTestTrap": cpqRPMTestTrap,
       "cpqPMTraps": cpqPMTraps,
       "cpqPMTrapCritical": cpqPMTrapCritical,
       "cpqPMTrapWarning": cpqPMTrapWarning,
       "cpqPMTrapInformation": cpqPMTrapInformation,
       "cpqPMTrapCleared": cpqPMTrapCleared}
)
