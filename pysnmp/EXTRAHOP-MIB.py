# SNMP MIB module (EXTRAHOP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/EXTRAHOP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:41:17 2024
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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

extrahop = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 32015)
)
extrahop.setRevisions(
        ("2015-05-08 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ExtrahopInfo_ObjectIdentity = ObjectIdentity
extrahopInfo = _ExtrahopInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32015, 0)
)


class _ExtrahopInfoVersionString_Type(DisplayString):
    """Custom type extrahopInfoVersionString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ExtrahopInfoVersionString_Type.__name__ = "DisplayString"
_ExtrahopInfoVersionString_Object = MibScalar
extrahopInfoVersionString = _ExtrahopInfoVersionString_Object(
    (1, 3, 6, 1, 4, 1, 32015, 0, 0),
    _ExtrahopInfoVersionString_Type()
)
extrahopInfoVersionString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extrahopInfoVersionString.setStatus("current")
_ExtrahopInfoVersionMajor_Type = Counter64
_ExtrahopInfoVersionMajor_Object = MibScalar
extrahopInfoVersionMajor = _ExtrahopInfoVersionMajor_Object(
    (1, 3, 6, 1, 4, 1, 32015, 0, 1),
    _ExtrahopInfoVersionMajor_Type()
)
extrahopInfoVersionMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extrahopInfoVersionMajor.setStatus("current")
_ExtrahopInfoVersionMinor_Type = Counter64
_ExtrahopInfoVersionMinor_Object = MibScalar
extrahopInfoVersionMinor = _ExtrahopInfoVersionMinor_Object(
    (1, 3, 6, 1, 4, 1, 32015, 0, 2),
    _ExtrahopInfoVersionMinor_Type()
)
extrahopInfoVersionMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extrahopInfoVersionMinor.setStatus("current")
_ExtrahopInfoVersionBranchRelease_Type = Counter64
_ExtrahopInfoVersionBranchRelease_Object = MibScalar
extrahopInfoVersionBranchRelease = _ExtrahopInfoVersionBranchRelease_Object(
    (1, 3, 6, 1, 4, 1, 32015, 0, 3),
    _ExtrahopInfoVersionBranchRelease_Type()
)
extrahopInfoVersionBranchRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extrahopInfoVersionBranchRelease.setStatus("current")
_ExtrahopInfoVersionRevision_Type = Counter64
_ExtrahopInfoVersionRevision_Object = MibScalar
extrahopInfoVersionRevision = _ExtrahopInfoVersionRevision_Object(
    (1, 3, 6, 1, 4, 1, 32015, 0, 4),
    _ExtrahopInfoVersionRevision_Type()
)
extrahopInfoVersionRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extrahopInfoVersionRevision.setStatus("current")
_ExtrahopAlert_ObjectIdentity = ObjectIdentity
extrahopAlert = _ExtrahopAlert_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32015, 1)
)


class _ExtrahopAlertName_Type(DisplayString):
    """Custom type extrahopAlertName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ExtrahopAlertName_Type.__name__ = "DisplayString"
_ExtrahopAlertName_Object = MibScalar
extrahopAlertName = _ExtrahopAlertName_Object(
    (1, 3, 6, 1, 4, 1, 32015, 1, 1),
    _ExtrahopAlertName_Type()
)
extrahopAlertName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extrahopAlertName.setStatus("current")


class _ExtrahopAlertComment_Type(DisplayString):
    """Custom type extrahopAlertComment based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ExtrahopAlertComment_Type.__name__ = "DisplayString"
_ExtrahopAlertComment_Object = MibScalar
extrahopAlertComment = _ExtrahopAlertComment_Object(
    (1, 3, 6, 1, 4, 1, 32015, 1, 2),
    _ExtrahopAlertComment_Type()
)
extrahopAlertComment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extrahopAlertComment.setStatus("current")


class _ExtrahopAlertObjectType_Type(DisplayString):
    """Custom type extrahopAlertObjectType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ExtrahopAlertObjectType_Type.__name__ = "DisplayString"
_ExtrahopAlertObjectType_Object = MibScalar
extrahopAlertObjectType = _ExtrahopAlertObjectType_Object(
    (1, 3, 6, 1, 4, 1, 32015, 1, 3),
    _ExtrahopAlertObjectType_Type()
)
extrahopAlertObjectType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extrahopAlertObjectType.setStatus("current")


class _ExtrahopAlertObjectName_Type(DisplayString):
    """Custom type extrahopAlertObjectName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ExtrahopAlertObjectName_Type.__name__ = "DisplayString"
_ExtrahopAlertObjectName_Object = MibScalar
extrahopAlertObjectName = _ExtrahopAlertObjectName_Object(
    (1, 3, 6, 1, 4, 1, 32015, 1, 4),
    _ExtrahopAlertObjectName_Type()
)
extrahopAlertObjectName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extrahopAlertObjectName.setStatus("current")


class _ExtrahopAlertExpr_Type(DisplayString):
    """Custom type extrahopAlertExpr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ExtrahopAlertExpr_Type.__name__ = "DisplayString"
_ExtrahopAlertExpr_Object = MibScalar
extrahopAlertExpr = _ExtrahopAlertExpr_Object(
    (1, 3, 6, 1, 4, 1, 32015, 1, 5),
    _ExtrahopAlertExpr_Type()
)
extrahopAlertExpr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extrahopAlertExpr.setStatus("current")


class _ExtrahopAlertValue_Type(DisplayString):
    """Custom type extrahopAlertValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ExtrahopAlertValue_Type.__name__ = "DisplayString"
_ExtrahopAlertValue_Object = MibScalar
extrahopAlertValue = _ExtrahopAlertValue_Object(
    (1, 3, 6, 1, 4, 1, 32015, 1, 6),
    _ExtrahopAlertValue_Type()
)
extrahopAlertValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extrahopAlertValue.setStatus("current")


class _ExtrahopAlertTime_Type(DisplayString):
    """Custom type extrahopAlertTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ExtrahopAlertTime_Type.__name__ = "DisplayString"
_ExtrahopAlertTime_Object = MibScalar
extrahopAlertTime = _ExtrahopAlertTime_Object(
    (1, 3, 6, 1, 4, 1, 32015, 1, 7),
    _ExtrahopAlertTime_Type()
)
extrahopAlertTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extrahopAlertTime.setStatus("current")


class _ExtrahopAlertObjectId_Type(DisplayString):
    """Custom type extrahopAlertObjectId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ExtrahopAlertObjectId_Type.__name__ = "DisplayString"
_ExtrahopAlertObjectId_Object = MibScalar
extrahopAlertObjectId = _ExtrahopAlertObjectId_Object(
    (1, 3, 6, 1, 4, 1, 32015, 1, 8),
    _ExtrahopAlertObjectId_Type()
)
extrahopAlertObjectId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extrahopAlertObjectId.setStatus("current")


class _ExtrahopAlertObjectStrId_Type(DisplayString):
    """Custom type extrahopAlertObjectStrId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ExtrahopAlertObjectStrId_Type.__name__ = "DisplayString"
_ExtrahopAlertObjectStrId_Object = MibScalar
extrahopAlertObjectStrId = _ExtrahopAlertObjectStrId_Object(
    (1, 3, 6, 1, 4, 1, 32015, 1, 9),
    _ExtrahopAlertObjectStrId_Type()
)
extrahopAlertObjectStrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extrahopAlertObjectStrId.setStatus("current")


class _ExtrahopAlertObjectMACAddr_Type(DisplayString):
    """Custom type extrahopAlertObjectMACAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ExtrahopAlertObjectMACAddr_Type.__name__ = "DisplayString"
_ExtrahopAlertObjectMACAddr_Object = MibScalar
extrahopAlertObjectMACAddr = _ExtrahopAlertObjectMACAddr_Object(
    (1, 3, 6, 1, 4, 1, 32015, 1, 10),
    _ExtrahopAlertObjectMACAddr_Type()
)
extrahopAlertObjectMACAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extrahopAlertObjectMACAddr.setStatus("current")


class _ExtrahopAlertObjectIPAddr_Type(DisplayString):
    """Custom type extrahopAlertObjectIPAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ExtrahopAlertObjectIPAddr_Type.__name__ = "DisplayString"
_ExtrahopAlertObjectIPAddr_Object = MibScalar
extrahopAlertObjectIPAddr = _ExtrahopAlertObjectIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 32015, 1, 11),
    _ExtrahopAlertObjectIPAddr_Type()
)
extrahopAlertObjectIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extrahopAlertObjectIPAddr.setStatus("current")


class _ExtrahopAlertObjectTags_Type(DisplayString):
    """Custom type extrahopAlertObjectTags based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ExtrahopAlertObjectTags_Type.__name__ = "DisplayString"
_ExtrahopAlertObjectTags_Object = MibScalar
extrahopAlertObjectTags = _ExtrahopAlertObjectTags_Object(
    (1, 3, 6, 1, 4, 1, 32015, 1, 12),
    _ExtrahopAlertObjectTags_Type()
)
extrahopAlertObjectTags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extrahopAlertObjectTags.setStatus("current")


class _ExtrahopAlertObjectURL_Type(DisplayString):
    """Custom type extrahopAlertObjectURL based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ExtrahopAlertObjectURL_Type.__name__ = "DisplayString"
_ExtrahopAlertObjectURL_Object = MibScalar
extrahopAlertObjectURL = _ExtrahopAlertObjectURL_Object(
    (1, 3, 6, 1, 4, 1, 32015, 1, 13),
    _ExtrahopAlertObjectURL_Type()
)
extrahopAlertObjectURL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extrahopAlertObjectURL.setStatus("current")


class _ExtrahopAlertStatName_Type(DisplayString):
    """Custom type extrahopAlertStatName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ExtrahopAlertStatName_Type.__name__ = "DisplayString"
_ExtrahopAlertStatName_Object = MibScalar
extrahopAlertStatName = _ExtrahopAlertStatName_Object(
    (1, 3, 6, 1, 4, 1, 32015, 1, 14),
    _ExtrahopAlertStatName_Type()
)
extrahopAlertStatName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extrahopAlertStatName.setStatus("current")


class _ExtrahopAlertStatFieldName_Type(DisplayString):
    """Custom type extrahopAlertStatFieldName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ExtrahopAlertStatFieldName_Type.__name__ = "DisplayString"
_ExtrahopAlertStatFieldName_Object = MibScalar
extrahopAlertStatFieldName = _ExtrahopAlertStatFieldName_Object(
    (1, 3, 6, 1, 4, 1, 32015, 1, 15),
    _ExtrahopAlertStatFieldName_Type()
)
extrahopAlertStatFieldName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extrahopAlertStatFieldName.setStatus("current")


class _ExtrahopAlertSeverity_Type(Integer32):
    """Custom type extrahopAlertSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("alert", 1),
          ("critical", 2),
          ("debug", 7),
          ("emergency", 0),
          ("error", 3),
          ("info", 6),
          ("notice", 5),
          ("warning", 4))
    )


_ExtrahopAlertSeverity_Type.__name__ = "Integer32"
_ExtrahopAlertSeverity_Object = MibScalar
extrahopAlertSeverity = _ExtrahopAlertSeverity_Object(
    (1, 3, 6, 1, 4, 1, 32015, 1, 16),
    _ExtrahopAlertSeverity_Type()
)
extrahopAlertSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extrahopAlertSeverity.setStatus("current")
_ExtrahopTraps_ObjectIdentity = ObjectIdentity
extrahopTraps = _ExtrahopTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32015, 2)
)
_ExtrahopStats_ObjectIdentity = ObjectIdentity
extrahopStats = _ExtrahopStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32015, 3)
)
_ExtrahopStatsPktsSinceBoot_Type = Counter64
_ExtrahopStatsPktsSinceBoot_Object = MibScalar
extrahopStatsPktsSinceBoot = _ExtrahopStatsPktsSinceBoot_Object(
    (1, 3, 6, 1, 4, 1, 32015, 3, 1),
    _ExtrahopStatsPktsSinceBoot_Type()
)
extrahopStatsPktsSinceBoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extrahopStatsPktsSinceBoot.setStatus("current")
_ExtrahopStatsBytesSinceBoot_Type = Counter64
_ExtrahopStatsBytesSinceBoot_Object = MibScalar
extrahopStatsBytesSinceBoot = _ExtrahopStatsBytesSinceBoot_Object(
    (1, 3, 6, 1, 4, 1, 32015, 3, 2),
    _ExtrahopStatsBytesSinceBoot_Type()
)
extrahopStatsBytesSinceBoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extrahopStatsBytesSinceBoot.setStatus("current")
_ExtrahopObjects_ObjectIdentity = ObjectIdentity
extrahopObjects = _ExtrahopObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32015, 4)
)
_ExtrahopStorageAlert_ObjectIdentity = ObjectIdentity
extrahopStorageAlert = _ExtrahopStorageAlert_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32015, 5)
)


class _ExtrahopStorageAlertRole_Type(DisplayString):
    """Custom type extrahopStorageAlertRole based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ExtrahopStorageAlertRole_Type.__name__ = "DisplayString"
_ExtrahopStorageAlertRole_Object = MibScalar
extrahopStorageAlertRole = _ExtrahopStorageAlertRole_Object(
    (1, 3, 6, 1, 4, 1, 32015, 5, 1),
    _ExtrahopStorageAlertRole_Type()
)
extrahopStorageAlertRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extrahopStorageAlertRole.setStatus("current")


class _ExtrahopStorageAlertDevice_Type(DisplayString):
    """Custom type extrahopStorageAlertDevice based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ExtrahopStorageAlertDevice_Type.__name__ = "DisplayString"
_ExtrahopStorageAlertDevice_Object = MibScalar
extrahopStorageAlertDevice = _ExtrahopStorageAlertDevice_Object(
    (1, 3, 6, 1, 4, 1, 32015, 5, 2),
    _ExtrahopStorageAlertDevice_Type()
)
extrahopStorageAlertDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extrahopStorageAlertDevice.setStatus("current")


class _ExtrahopStorageAlertStatus_Type(DisplayString):
    """Custom type extrahopStorageAlertStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ExtrahopStorageAlertStatus_Type.__name__ = "DisplayString"
_ExtrahopStorageAlertStatus_Object = MibScalar
extrahopStorageAlertStatus = _ExtrahopStorageAlertStatus_Object(
    (1, 3, 6, 1, 4, 1, 32015, 5, 3),
    _ExtrahopStorageAlertStatus_Type()
)
extrahopStorageAlertStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extrahopStorageAlertStatus.setStatus("current")


class _ExtrahopStorageAlertDetails_Type(DisplayString):
    """Custom type extrahopStorageAlertDetails based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ExtrahopStorageAlertDetails_Type.__name__ = "DisplayString"
_ExtrahopStorageAlertDetails_Object = MibScalar
extrahopStorageAlertDetails = _ExtrahopStorageAlertDetails_Object(
    (1, 3, 6, 1, 4, 1, 32015, 5, 4),
    _ExtrahopStorageAlertDetails_Type()
)
extrahopStorageAlertDetails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extrahopStorageAlertDetails.setStatus("current")


class _ExtrahopStorageAlertSeverity_Type(Integer32):
    """Custom type extrahopStorageAlertSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("alert", 1),
          ("critical", 2),
          ("debug", 7),
          ("emergency", 0),
          ("error", 3),
          ("info", 6),
          ("notice", 5),
          ("warning", 4))
    )


_ExtrahopStorageAlertSeverity_Type.__name__ = "Integer32"
_ExtrahopStorageAlertSeverity_Object = MibScalar
extrahopStorageAlertSeverity = _ExtrahopStorageAlertSeverity_Object(
    (1, 3, 6, 1, 4, 1, 32015, 5, 5),
    _ExtrahopStorageAlertSeverity_Type()
)
extrahopStorageAlertSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extrahopStorageAlertSeverity.setStatus("current")


class _ExtrahopStorageAlertMachine_Type(DisplayString):
    """Custom type extrahopStorageAlertMachine based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ExtrahopStorageAlertMachine_Type.__name__ = "DisplayString"
_ExtrahopStorageAlertMachine_Object = MibScalar
extrahopStorageAlertMachine = _ExtrahopStorageAlertMachine_Object(
    (1, 3, 6, 1, 4, 1, 32015, 5, 6),
    _ExtrahopStorageAlertMachine_Type()
)
extrahopStorageAlertMachine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extrahopStorageAlertMachine.setStatus("current")

# Managed Objects groups

extrahopObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 32015, 4, 1)
)
extrahopObjectGroup.setObjects(
      *(("EXTRAHOP-MIB", "extrahopAlertName"),
        ("EXTRAHOP-MIB", "extrahopAlertComment"),
        ("EXTRAHOP-MIB", "extrahopAlertObjectType"),
        ("EXTRAHOP-MIB", "extrahopAlertObjectName"),
        ("EXTRAHOP-MIB", "extrahopAlertExpr"),
        ("EXTRAHOP-MIB", "extrahopAlertValue"),
        ("EXTRAHOP-MIB", "extrahopAlertTime"),
        ("EXTRAHOP-MIB", "extrahopAlertObjectId"),
        ("EXTRAHOP-MIB", "extrahopAlertObjectStrId"),
        ("EXTRAHOP-MIB", "extrahopAlertObjectMACAddr"),
        ("EXTRAHOP-MIB", "extrahopAlertObjectIPAddr"),
        ("EXTRAHOP-MIB", "extrahopAlertObjectTags"),
        ("EXTRAHOP-MIB", "extrahopAlertObjectURL"),
        ("EXTRAHOP-MIB", "extrahopAlertStatName"),
        ("EXTRAHOP-MIB", "extrahopAlertStatFieldName"),
        ("EXTRAHOP-MIB", "extrahopAlertSeverity"),
        ("EXTRAHOP-MIB", "extrahopStatsPktsSinceBoot"),
        ("EXTRAHOP-MIB", "extrahopStatsBytesSinceBoot"),
        ("EXTRAHOP-MIB", "extrahopStorageAlertRole"),
        ("EXTRAHOP-MIB", "extrahopStorageAlertDevice"),
        ("EXTRAHOP-MIB", "extrahopStorageAlertStatus"),
        ("EXTRAHOP-MIB", "extrahopStorageAlertDetails"),
        ("EXTRAHOP-MIB", "extrahopStorageAlertSeverity"),
        ("EXTRAHOP-MIB", "extrahopStorageAlertMachine"))
)
if mibBuilder.loadTexts:
    extrahopObjectGroup.setStatus("current")


# Notification objects

extrahopAlertTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 32015, 2, 1)
)
extrahopAlertTrap.setObjects(
      *(("EXTRAHOP-MIB", "extrahopAlertName"),
        ("EXTRAHOP-MIB", "extrahopAlertComment"),
        ("EXTRAHOP-MIB", "extrahopAlertObjectType"),
        ("EXTRAHOP-MIB", "extrahopAlertObjectName"),
        ("EXTRAHOP-MIB", "extrahopAlertExpr"),
        ("EXTRAHOP-MIB", "extrahopAlertValue"),
        ("EXTRAHOP-MIB", "extrahopAlertTime"),
        ("EXTRAHOP-MIB", "extrahopAlertObjectId"),
        ("EXTRAHOP-MIB", "extrahopAlertObjectStrId"),
        ("EXTRAHOP-MIB", "extrahopAlertObjectMACAddr"),
        ("EXTRAHOP-MIB", "extrahopAlertObjectIPAddr"),
        ("EXTRAHOP-MIB", "extrahopAlertObjectTags"),
        ("EXTRAHOP-MIB", "extrahopAlertObjectURL"),
        ("EXTRAHOP-MIB", "extrahopAlertStatName"),
        ("EXTRAHOP-MIB", "extrahopAlertStatFieldName"),
        ("EXTRAHOP-MIB", "extrahopAlertSeverity"))
)
if mibBuilder.loadTexts:
    extrahopAlertTrap.setStatus(
        "current"
    )

extrahopStorageAlertTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 32015, 2, 2)
)
extrahopStorageAlertTrap.setObjects(
      *(("EXTRAHOP-MIB", "extrahopStorageAlertRole"),
        ("EXTRAHOP-MIB", "extrahopStorageAlertDevice"),
        ("EXTRAHOP-MIB", "extrahopStorageAlertStatus"),
        ("EXTRAHOP-MIB", "extrahopStorageAlertDetails"),
        ("EXTRAHOP-MIB", "extrahopStorageAlertSeverity"),
        ("EXTRAHOP-MIB", "extrahopStorageAlertMachine"))
)
if mibBuilder.loadTexts:
    extrahopStorageAlertTrap.setStatus(
        "current"
    )


# Notifications groups

extrahopNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 32015, 4, 2)
)
extrahopNotificationGroup.setObjects(
      *(("EXTRAHOP-MIB", "extrahopAlertTrap"),
        ("EXTRAHOP-MIB", "extrahopStorageAlertTrap"))
)
if mibBuilder.loadTexts:
    extrahopNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EXTRAHOP-MIB",
    **{"extrahop": extrahop,
       "extrahopInfo": extrahopInfo,
       "extrahopInfoVersionString": extrahopInfoVersionString,
       "extrahopInfoVersionMajor": extrahopInfoVersionMajor,
       "extrahopInfoVersionMinor": extrahopInfoVersionMinor,
       "extrahopInfoVersionBranchRelease": extrahopInfoVersionBranchRelease,
       "extrahopInfoVersionRevision": extrahopInfoVersionRevision,
       "extrahopAlert": extrahopAlert,
       "extrahopAlertName": extrahopAlertName,
       "extrahopAlertComment": extrahopAlertComment,
       "extrahopAlertObjectType": extrahopAlertObjectType,
       "extrahopAlertObjectName": extrahopAlertObjectName,
       "extrahopAlertExpr": extrahopAlertExpr,
       "extrahopAlertValue": extrahopAlertValue,
       "extrahopAlertTime": extrahopAlertTime,
       "extrahopAlertObjectId": extrahopAlertObjectId,
       "extrahopAlertObjectStrId": extrahopAlertObjectStrId,
       "extrahopAlertObjectMACAddr": extrahopAlertObjectMACAddr,
       "extrahopAlertObjectIPAddr": extrahopAlertObjectIPAddr,
       "extrahopAlertObjectTags": extrahopAlertObjectTags,
       "extrahopAlertObjectURL": extrahopAlertObjectURL,
       "extrahopAlertStatName": extrahopAlertStatName,
       "extrahopAlertStatFieldName": extrahopAlertStatFieldName,
       "extrahopAlertSeverity": extrahopAlertSeverity,
       "extrahopTraps": extrahopTraps,
       "extrahopAlertTrap": extrahopAlertTrap,
       "extrahopStorageAlertTrap": extrahopStorageAlertTrap,
       "extrahopStats": extrahopStats,
       "extrahopStatsPktsSinceBoot": extrahopStatsPktsSinceBoot,
       "extrahopStatsBytesSinceBoot": extrahopStatsBytesSinceBoot,
       "extrahopObjects": extrahopObjects,
       "extrahopObjectGroup": extrahopObjectGroup,
       "extrahopNotificationGroup": extrahopNotificationGroup,
       "extrahopStorageAlert": extrahopStorageAlert,
       "extrahopStorageAlertRole": extrahopStorageAlertRole,
       "extrahopStorageAlertDevice": extrahopStorageAlertDevice,
       "extrahopStorageAlertStatus": extrahopStorageAlertStatus,
       "extrahopStorageAlertDetails": extrahopStorageAlertDetails,
       "extrahopStorageAlertSeverity": extrahopStorageAlertSeverity,
       "extrahopStorageAlertMachine": extrahopStorageAlertMachine}
)
