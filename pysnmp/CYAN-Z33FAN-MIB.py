# SNMP MIB module (CYAN-Z33FAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CYAN-Z33FAN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:21:20 2024
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

(CyanTypeTc,
 cyanEntityModules) = mibBuilder.importSymbols(
    "CYAN-MIB",
    "CyanTypeTc",
    "cyanEntityModules")

(CyanAdminStateTc,
 CyanLEDTc,
 CyanOpStateQualTc,
 CyanOpStateTc,
 CyanSecServiceStateTc) = mibBuilder.importSymbols(
    "CYAN-TC-MIB",
    "CyanAdminStateTc",
    "CyanLEDTc",
    "CyanOpStateQualTc",
    "CyanOpStateTc",
    "CyanSecServiceStateTc")

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

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

cyanZ33FanModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 80)
)
cyanZ33FanModule.setRevisions(
        ("2014-12-07 05:45",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CyanZ33FanMibObjects_ObjectIdentity = ObjectIdentity
cyanZ33FanMibObjects = _CyanZ33FanMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 80, 1)
)
_CyanZ33FanTable_Object = MibTable
cyanZ33FanTable = _CyanZ33FanTable_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 80, 1, 1)
)
if mibBuilder.loadTexts:
    cyanZ33FanTable.setStatus("current")
_CyanZ33FanEntry_Object = MibTableRow
cyanZ33FanEntry = _CyanZ33FanEntry_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 80, 1, 1, 1)
)
cyanZ33FanEntry.setIndexNames(
    (0, "CYAN-Z33FAN-MIB", "cyanZ33FanShelfId"),
    (0, "CYAN-Z33FAN-MIB", "cyanZ33FanZ33FanId"),
)
if mibBuilder.loadTexts:
    cyanZ33FanEntry.setStatus("current")


class _CyanZ33FanShelfId_Type(Unsigned32):
    """Custom type cyanZ33FanShelfId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CyanZ33FanShelfId_Type.__name__ = "Unsigned32"
_CyanZ33FanShelfId_Object = MibTableColumn
cyanZ33FanShelfId = _CyanZ33FanShelfId_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 80, 1, 1, 1, 1),
    _CyanZ33FanShelfId_Type()
)
cyanZ33FanShelfId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cyanZ33FanShelfId.setStatus("current")
_CyanZ33FanZ33FanId_Type = Unsigned32
_CyanZ33FanZ33FanId_Object = MibTableColumn
cyanZ33FanZ33FanId = _CyanZ33FanZ33FanId_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 80, 1, 1, 1, 2),
    _CyanZ33FanZ33FanId_Type()
)
cyanZ33FanZ33FanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cyanZ33FanZ33FanId.setStatus("current")
_CyanZ33FanAcoLed_Type = CyanLEDTc
_CyanZ33FanAcoLed_Object = MibTableColumn
cyanZ33FanAcoLed = _CyanZ33FanAcoLed_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 80, 1, 1, 1, 3),
    _CyanZ33FanAcoLed_Type()
)
cyanZ33FanAcoLed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanZ33FanAcoLed.setStatus("current")
_CyanZ33FanAdminState_Type = CyanAdminStateTc
_CyanZ33FanAdminState_Object = MibTableColumn
cyanZ33FanAdminState = _CyanZ33FanAdminState_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 80, 1, 1, 1, 4),
    _CyanZ33FanAdminState_Type()
)
cyanZ33FanAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanZ33FanAdminState.setStatus("current")


class _CyanZ33FanAssetTag_Type(DisplayString):
    """Custom type cyanZ33FanAssetTag based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 124),
    )


_CyanZ33FanAssetTag_Type.__name__ = "DisplayString"
_CyanZ33FanAssetTag_Object = MibTableColumn
cyanZ33FanAssetTag = _CyanZ33FanAssetTag_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 80, 1, 1, 1, 5),
    _CyanZ33FanAssetTag_Type()
)
cyanZ33FanAssetTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanZ33FanAssetTag.setStatus("current")
_CyanZ33FanAutoinserviceSoakTimeSec_Type = Integer32
_CyanZ33FanAutoinserviceSoakTimeSec_Object = MibTableColumn
cyanZ33FanAutoinserviceSoakTimeSec = _CyanZ33FanAutoinserviceSoakTimeSec_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 80, 1, 1, 1, 6),
    _CyanZ33FanAutoinserviceSoakTimeSec_Type()
)
cyanZ33FanAutoinserviceSoakTimeSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanZ33FanAutoinserviceSoakTimeSec.setStatus("current")
_CyanZ33FanBaseMacAddress_Type = DisplayString
_CyanZ33FanBaseMacAddress_Object = MibTableColumn
cyanZ33FanBaseMacAddress = _CyanZ33FanBaseMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 80, 1, 1, 1, 7),
    _CyanZ33FanBaseMacAddress_Type()
)
cyanZ33FanBaseMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanZ33FanBaseMacAddress.setStatus("current")
_CyanZ33FanCriticalLed_Type = CyanLEDTc
_CyanZ33FanCriticalLed_Object = MibTableColumn
cyanZ33FanCriticalLed = _CyanZ33FanCriticalLed_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 80, 1, 1, 1, 8),
    _CyanZ33FanCriticalLed_Type()
)
cyanZ33FanCriticalLed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanZ33FanCriticalLed.setStatus("current")


class _CyanZ33FanDescription_Type(DisplayString):
    """Custom type cyanZ33FanDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CyanZ33FanDescription_Type.__name__ = "DisplayString"
_CyanZ33FanDescription_Object = MibTableColumn
cyanZ33FanDescription = _CyanZ33FanDescription_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 80, 1, 1, 1, 9),
    _CyanZ33FanDescription_Type()
)
cyanZ33FanDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanZ33FanDescription.setStatus("current")
_CyanZ33FanFanLed_Type = CyanLEDTc
_CyanZ33FanFanLed_Object = MibTableColumn
cyanZ33FanFanLed = _CyanZ33FanFanLed_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 80, 1, 1, 1, 10),
    _CyanZ33FanFanLed_Type()
)
cyanZ33FanFanLed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanZ33FanFanLed.setStatus("current")
_CyanZ33FanFilterLed_Type = CyanLEDTc
_CyanZ33FanFilterLed_Object = MibTableColumn
cyanZ33FanFilterLed = _CyanZ33FanFilterLed_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 80, 1, 1, 1, 11),
    _CyanZ33FanFilterLed_Type()
)
cyanZ33FanFilterLed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanZ33FanFilterLed.setStatus("current")
_CyanZ33FanIdentifier_Type = DisplayString
_CyanZ33FanIdentifier_Object = MibTableColumn
cyanZ33FanIdentifier = _CyanZ33FanIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 80, 1, 1, 1, 12),
    _CyanZ33FanIdentifier_Type()
)
cyanZ33FanIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanZ33FanIdentifier.setStatus("current")


class _CyanZ33FanMacBlockSize_Type(Unsigned32):
    """Custom type cyanZ33FanMacBlockSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CyanZ33FanMacBlockSize_Type.__name__ = "Unsigned32"
_CyanZ33FanMacBlockSize_Object = MibTableColumn
cyanZ33FanMacBlockSize = _CyanZ33FanMacBlockSize_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 80, 1, 1, 1, 13),
    _CyanZ33FanMacBlockSize_Type()
)
cyanZ33FanMacBlockSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanZ33FanMacBlockSize.setStatus("current")
_CyanZ33FanMajorLed_Type = CyanLEDTc
_CyanZ33FanMajorLed_Object = MibTableColumn
cyanZ33FanMajorLed = _CyanZ33FanMajorLed_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 80, 1, 1, 1, 14),
    _CyanZ33FanMajorLed_Type()
)
cyanZ33FanMajorLed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanZ33FanMajorLed.setStatus("current")


class _CyanZ33FanMfgCleiCode_Type(DisplayString):
    """Custom type cyanZ33FanMfgCleiCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_CyanZ33FanMfgCleiCode_Type.__name__ = "DisplayString"
_CyanZ33FanMfgCleiCode_Object = MibTableColumn
cyanZ33FanMfgCleiCode = _CyanZ33FanMfgCleiCode_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 80, 1, 1, 1, 15),
    _CyanZ33FanMfgCleiCode_Type()
)
cyanZ33FanMfgCleiCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanZ33FanMfgCleiCode.setStatus("current")


class _CyanZ33FanMfgEciCode_Type(DisplayString):
    """Custom type cyanZ33FanMfgEciCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_CyanZ33FanMfgEciCode_Type.__name__ = "DisplayString"
_CyanZ33FanMfgEciCode_Object = MibTableColumn
cyanZ33FanMfgEciCode = _CyanZ33FanMfgEciCode_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 80, 1, 1, 1, 16),
    _CyanZ33FanMfgEciCode_Type()
)
cyanZ33FanMfgEciCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanZ33FanMfgEciCode.setStatus("current")
_CyanZ33FanMfgModuleId_Type = Unsigned32
_CyanZ33FanMfgModuleId_Object = MibTableColumn
cyanZ33FanMfgModuleId = _CyanZ33FanMfgModuleId_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 80, 1, 1, 1, 17),
    _CyanZ33FanMfgModuleId_Type()
)
cyanZ33FanMfgModuleId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanZ33FanMfgModuleId.setStatus("current")


class _CyanZ33FanMfgPartNumber_Type(DisplayString):
    """Custom type cyanZ33FanMfgPartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CyanZ33FanMfgPartNumber_Type.__name__ = "DisplayString"
_CyanZ33FanMfgPartNumber_Object = MibTableColumn
cyanZ33FanMfgPartNumber = _CyanZ33FanMfgPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 80, 1, 1, 1, 18),
    _CyanZ33FanMfgPartNumber_Type()
)
cyanZ33FanMfgPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanZ33FanMfgPartNumber.setStatus("current")


class _CyanZ33FanMfgRevision_Type(DisplayString):
    """Custom type cyanZ33FanMfgRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_CyanZ33FanMfgRevision_Type.__name__ = "DisplayString"
_CyanZ33FanMfgRevision_Object = MibTableColumn
cyanZ33FanMfgRevision = _CyanZ33FanMfgRevision_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 80, 1, 1, 1, 19),
    _CyanZ33FanMfgRevision_Type()
)
cyanZ33FanMfgRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanZ33FanMfgRevision.setStatus("current")


class _CyanZ33FanMfgSerialNumber_Type(DisplayString):
    """Custom type cyanZ33FanMfgSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CyanZ33FanMfgSerialNumber_Type.__name__ = "DisplayString"
_CyanZ33FanMfgSerialNumber_Object = MibTableColumn
cyanZ33FanMfgSerialNumber = _CyanZ33FanMfgSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 80, 1, 1, 1, 20),
    _CyanZ33FanMfgSerialNumber_Type()
)
cyanZ33FanMfgSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanZ33FanMfgSerialNumber.setStatus("current")
_CyanZ33FanMinorLed_Type = CyanLEDTc
_CyanZ33FanMinorLed_Object = MibTableColumn
cyanZ33FanMinorLed = _CyanZ33FanMinorLed_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 80, 1, 1, 1, 21),
    _CyanZ33FanMinorLed_Type()
)
cyanZ33FanMinorLed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanZ33FanMinorLed.setStatus("current")
_CyanZ33FanName_Type = DisplayString
_CyanZ33FanName_Object = MibTableColumn
cyanZ33FanName = _CyanZ33FanName_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 80, 1, 1, 1, 22),
    _CyanZ33FanName_Type()
)
cyanZ33FanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanZ33FanName.setStatus("current")
_CyanZ33FanOidClass_Type = DisplayString
_CyanZ33FanOidClass_Object = MibTableColumn
cyanZ33FanOidClass = _CyanZ33FanOidClass_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 80, 1, 1, 1, 23),
    _CyanZ33FanOidClass_Type()
)
cyanZ33FanOidClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanZ33FanOidClass.setStatus("current")
_CyanZ33FanOperState_Type = CyanOpStateTc
_CyanZ33FanOperState_Object = MibTableColumn
cyanZ33FanOperState = _CyanZ33FanOperState_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 80, 1, 1, 1, 24),
    _CyanZ33FanOperState_Type()
)
cyanZ33FanOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanZ33FanOperState.setStatus("current")
_CyanZ33FanOperStateQual_Type = CyanOpStateQualTc
_CyanZ33FanOperStateQual_Object = MibTableColumn
cyanZ33FanOperStateQual = _CyanZ33FanOperStateQual_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 80, 1, 1, 1, 25),
    _CyanZ33FanOperStateQual_Type()
)
cyanZ33FanOperStateQual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanZ33FanOperStateQual.setStatus("current")


class _CyanZ33FanOssLabel_Type(DisplayString):
    """Custom type cyanZ33FanOssLabel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_CyanZ33FanOssLabel_Type.__name__ = "DisplayString"
_CyanZ33FanOssLabel_Object = MibTableColumn
cyanZ33FanOssLabel = _CyanZ33FanOssLabel_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 80, 1, 1, 1, 26),
    _CyanZ33FanOssLabel_Type()
)
cyanZ33FanOssLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanZ33FanOssLabel.setStatus("current")


class _CyanZ33FanOwner_Type(DisplayString):
    """Custom type cyanZ33FanOwner based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_CyanZ33FanOwner_Type.__name__ = "DisplayString"
_CyanZ33FanOwner_Object = MibTableColumn
cyanZ33FanOwner = _CyanZ33FanOwner_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 80, 1, 1, 1, 27),
    _CyanZ33FanOwner_Type()
)
cyanZ33FanOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanZ33FanOwner.setStatus("current")


class _CyanZ33FanPartNumber_Type(DisplayString):
    """Custom type cyanZ33FanPartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 11),
    )


_CyanZ33FanPartNumber_Type.__name__ = "DisplayString"
_CyanZ33FanPartNumber_Object = MibTableColumn
cyanZ33FanPartNumber = _CyanZ33FanPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 80, 1, 1, 1, 28),
    _CyanZ33FanPartNumber_Type()
)
cyanZ33FanPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanZ33FanPartNumber.setStatus("current")
_CyanZ33FanSecServState_Type = CyanSecServiceStateTc
_CyanZ33FanSecServState_Object = MibTableColumn
cyanZ33FanSecServState = _CyanZ33FanSecServState_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 80, 1, 1, 1, 29),
    _CyanZ33FanSecServState_Type()
)
cyanZ33FanSecServState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanZ33FanSecServState.setStatus("current")
_CyanZ33FanType_Type = CyanTypeTc
_CyanZ33FanType_Object = MibTableColumn
cyanZ33FanType = _CyanZ33FanType_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 80, 1, 1, 1, 30),
    _CyanZ33FanType_Type()
)
cyanZ33FanType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanZ33FanType.setStatus("current")

# Managed Objects groups

cyanZ33FanObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 80, 20)
)
cyanZ33FanObjectGroup.setObjects(
      *(("CYAN-Z33FAN-MIB", "cyanZ33FanAcoLed"),
        ("CYAN-Z33FAN-MIB", "cyanZ33FanAdminState"),
        ("CYAN-Z33FAN-MIB", "cyanZ33FanAssetTag"),
        ("CYAN-Z33FAN-MIB", "cyanZ33FanAutoinserviceSoakTimeSec"),
        ("CYAN-Z33FAN-MIB", "cyanZ33FanBaseMacAddress"),
        ("CYAN-Z33FAN-MIB", "cyanZ33FanCriticalLed"),
        ("CYAN-Z33FAN-MIB", "cyanZ33FanDescription"),
        ("CYAN-Z33FAN-MIB", "cyanZ33FanFanLed"),
        ("CYAN-Z33FAN-MIB", "cyanZ33FanFilterLed"),
        ("CYAN-Z33FAN-MIB", "cyanZ33FanIdentifier"),
        ("CYAN-Z33FAN-MIB", "cyanZ33FanMacBlockSize"),
        ("CYAN-Z33FAN-MIB", "cyanZ33FanMajorLed"),
        ("CYAN-Z33FAN-MIB", "cyanZ33FanMfgCleiCode"),
        ("CYAN-Z33FAN-MIB", "cyanZ33FanMfgEciCode"),
        ("CYAN-Z33FAN-MIB", "cyanZ33FanMfgModuleId"),
        ("CYAN-Z33FAN-MIB", "cyanZ33FanMfgPartNumber"),
        ("CYAN-Z33FAN-MIB", "cyanZ33FanMfgRevision"),
        ("CYAN-Z33FAN-MIB", "cyanZ33FanMfgSerialNumber"),
        ("CYAN-Z33FAN-MIB", "cyanZ33FanMinorLed"),
        ("CYAN-Z33FAN-MIB", "cyanZ33FanName"),
        ("CYAN-Z33FAN-MIB", "cyanZ33FanOidClass"),
        ("CYAN-Z33FAN-MIB", "cyanZ33FanOperState"),
        ("CYAN-Z33FAN-MIB", "cyanZ33FanOperStateQual"),
        ("CYAN-Z33FAN-MIB", "cyanZ33FanOssLabel"),
        ("CYAN-Z33FAN-MIB", "cyanZ33FanOwner"),
        ("CYAN-Z33FAN-MIB", "cyanZ33FanPartNumber"),
        ("CYAN-Z33FAN-MIB", "cyanZ33FanSecServState"),
        ("CYAN-Z33FAN-MIB", "cyanZ33FanType"))
)
if mibBuilder.loadTexts:
    cyanZ33FanObjectGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cyanZ33FanCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 80, 30)
)
if mibBuilder.loadTexts:
    cyanZ33FanCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CYAN-Z33FAN-MIB",
    **{"cyanZ33FanModule": cyanZ33FanModule,
       "cyanZ33FanMibObjects": cyanZ33FanMibObjects,
       "cyanZ33FanTable": cyanZ33FanTable,
       "cyanZ33FanEntry": cyanZ33FanEntry,
       "cyanZ33FanShelfId": cyanZ33FanShelfId,
       "cyanZ33FanZ33FanId": cyanZ33FanZ33FanId,
       "cyanZ33FanAcoLed": cyanZ33FanAcoLed,
       "cyanZ33FanAdminState": cyanZ33FanAdminState,
       "cyanZ33FanAssetTag": cyanZ33FanAssetTag,
       "cyanZ33FanAutoinserviceSoakTimeSec": cyanZ33FanAutoinserviceSoakTimeSec,
       "cyanZ33FanBaseMacAddress": cyanZ33FanBaseMacAddress,
       "cyanZ33FanCriticalLed": cyanZ33FanCriticalLed,
       "cyanZ33FanDescription": cyanZ33FanDescription,
       "cyanZ33FanFanLed": cyanZ33FanFanLed,
       "cyanZ33FanFilterLed": cyanZ33FanFilterLed,
       "cyanZ33FanIdentifier": cyanZ33FanIdentifier,
       "cyanZ33FanMacBlockSize": cyanZ33FanMacBlockSize,
       "cyanZ33FanMajorLed": cyanZ33FanMajorLed,
       "cyanZ33FanMfgCleiCode": cyanZ33FanMfgCleiCode,
       "cyanZ33FanMfgEciCode": cyanZ33FanMfgEciCode,
       "cyanZ33FanMfgModuleId": cyanZ33FanMfgModuleId,
       "cyanZ33FanMfgPartNumber": cyanZ33FanMfgPartNumber,
       "cyanZ33FanMfgRevision": cyanZ33FanMfgRevision,
       "cyanZ33FanMfgSerialNumber": cyanZ33FanMfgSerialNumber,
       "cyanZ33FanMinorLed": cyanZ33FanMinorLed,
       "cyanZ33FanName": cyanZ33FanName,
       "cyanZ33FanOidClass": cyanZ33FanOidClass,
       "cyanZ33FanOperState": cyanZ33FanOperState,
       "cyanZ33FanOperStateQual": cyanZ33FanOperStateQual,
       "cyanZ33FanOssLabel": cyanZ33FanOssLabel,
       "cyanZ33FanOwner": cyanZ33FanOwner,
       "cyanZ33FanPartNumber": cyanZ33FanPartNumber,
       "cyanZ33FanSecServState": cyanZ33FanSecServState,
       "cyanZ33FanType": cyanZ33FanType,
       "cyanZ33FanObjectGroup": cyanZ33FanObjectGroup,
       "cyanZ33FanCompliance": cyanZ33FanCompliance}
)
