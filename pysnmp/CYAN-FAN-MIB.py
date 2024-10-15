# SNMP MIB module (CYAN-FAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CYAN-FAN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:21:07 2024
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

cyanFanModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 40)
)
cyanFanModule.setRevisions(
        ("2014-12-07 05:45",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CyanFanMibObjects_ObjectIdentity = ObjectIdentity
cyanFanMibObjects = _CyanFanMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 40, 1)
)
_CyanFanTable_Object = MibTable
cyanFanTable = _CyanFanTable_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 40, 1, 1)
)
if mibBuilder.loadTexts:
    cyanFanTable.setStatus("current")
_CyanFanEntry_Object = MibTableRow
cyanFanEntry = _CyanFanEntry_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 40, 1, 1, 1)
)
cyanFanEntry.setIndexNames(
    (0, "CYAN-FAN-MIB", "cyanFanShelfId"),
    (0, "CYAN-FAN-MIB", "cyanFanFanId"),
)
if mibBuilder.loadTexts:
    cyanFanEntry.setStatus("current")


class _CyanFanShelfId_Type(Unsigned32):
    """Custom type cyanFanShelfId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CyanFanShelfId_Type.__name__ = "Unsigned32"
_CyanFanShelfId_Object = MibTableColumn
cyanFanShelfId = _CyanFanShelfId_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 40, 1, 1, 1, 1),
    _CyanFanShelfId_Type()
)
cyanFanShelfId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cyanFanShelfId.setStatus("current")
_CyanFanFanId_Type = Unsigned32
_CyanFanFanId_Object = MibTableColumn
cyanFanFanId = _CyanFanFanId_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 40, 1, 1, 1, 2),
    _CyanFanFanId_Type()
)
cyanFanFanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cyanFanFanId.setStatus("current")
_CyanFanAdminState_Type = CyanAdminStateTc
_CyanFanAdminState_Object = MibTableColumn
cyanFanAdminState = _CyanFanAdminState_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 40, 1, 1, 1, 3),
    _CyanFanAdminState_Type()
)
cyanFanAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanFanAdminState.setStatus("current")
_CyanFanAlarmLed_Type = CyanLEDTc
_CyanFanAlarmLed_Object = MibTableColumn
cyanFanAlarmLed = _CyanFanAlarmLed_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 40, 1, 1, 1, 4),
    _CyanFanAlarmLed_Type()
)
cyanFanAlarmLed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanFanAlarmLed.setStatus("current")


class _CyanFanAssetTag_Type(DisplayString):
    """Custom type cyanFanAssetTag based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 124),
    )


_CyanFanAssetTag_Type.__name__ = "DisplayString"
_CyanFanAssetTag_Object = MibTableColumn
cyanFanAssetTag = _CyanFanAssetTag_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 40, 1, 1, 1, 5),
    _CyanFanAssetTag_Type()
)
cyanFanAssetTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanFanAssetTag.setStatus("current")
_CyanFanAutoinserviceSoakTimeSec_Type = Integer32
_CyanFanAutoinserviceSoakTimeSec_Object = MibTableColumn
cyanFanAutoinserviceSoakTimeSec = _CyanFanAutoinserviceSoakTimeSec_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 40, 1, 1, 1, 6),
    _CyanFanAutoinserviceSoakTimeSec_Type()
)
cyanFanAutoinserviceSoakTimeSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanFanAutoinserviceSoakTimeSec.setStatus("current")
_CyanFanBaseMacAddress_Type = DisplayString
_CyanFanBaseMacAddress_Object = MibTableColumn
cyanFanBaseMacAddress = _CyanFanBaseMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 40, 1, 1, 1, 7),
    _CyanFanBaseMacAddress_Type()
)
cyanFanBaseMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanFanBaseMacAddress.setStatus("current")


class _CyanFanDescription_Type(DisplayString):
    """Custom type cyanFanDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CyanFanDescription_Type.__name__ = "DisplayString"
_CyanFanDescription_Object = MibTableColumn
cyanFanDescription = _CyanFanDescription_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 40, 1, 1, 1, 8),
    _CyanFanDescription_Type()
)
cyanFanDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanFanDescription.setStatus("current")
_CyanFanHotSwapLed_Type = CyanLEDTc
_CyanFanHotSwapLed_Object = MibTableColumn
cyanFanHotSwapLed = _CyanFanHotSwapLed_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 40, 1, 1, 1, 9),
    _CyanFanHotSwapLed_Type()
)
cyanFanHotSwapLed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanFanHotSwapLed.setStatus("current")
_CyanFanIdentifier_Type = DisplayString
_CyanFanIdentifier_Object = MibTableColumn
cyanFanIdentifier = _CyanFanIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 40, 1, 1, 1, 10),
    _CyanFanIdentifier_Type()
)
cyanFanIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanFanIdentifier.setStatus("current")


class _CyanFanMacBlockSize_Type(Unsigned32):
    """Custom type cyanFanMacBlockSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CyanFanMacBlockSize_Type.__name__ = "Unsigned32"
_CyanFanMacBlockSize_Object = MibTableColumn
cyanFanMacBlockSize = _CyanFanMacBlockSize_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 40, 1, 1, 1, 11),
    _CyanFanMacBlockSize_Type()
)
cyanFanMacBlockSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanFanMacBlockSize.setStatus("current")


class _CyanFanMfgCleiCode_Type(DisplayString):
    """Custom type cyanFanMfgCleiCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_CyanFanMfgCleiCode_Type.__name__ = "DisplayString"
_CyanFanMfgCleiCode_Object = MibTableColumn
cyanFanMfgCleiCode = _CyanFanMfgCleiCode_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 40, 1, 1, 1, 12),
    _CyanFanMfgCleiCode_Type()
)
cyanFanMfgCleiCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanFanMfgCleiCode.setStatus("current")


class _CyanFanMfgEciCode_Type(DisplayString):
    """Custom type cyanFanMfgEciCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_CyanFanMfgEciCode_Type.__name__ = "DisplayString"
_CyanFanMfgEciCode_Object = MibTableColumn
cyanFanMfgEciCode = _CyanFanMfgEciCode_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 40, 1, 1, 1, 13),
    _CyanFanMfgEciCode_Type()
)
cyanFanMfgEciCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanFanMfgEciCode.setStatus("current")
_CyanFanMfgModuleId_Type = Unsigned32
_CyanFanMfgModuleId_Object = MibTableColumn
cyanFanMfgModuleId = _CyanFanMfgModuleId_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 40, 1, 1, 1, 14),
    _CyanFanMfgModuleId_Type()
)
cyanFanMfgModuleId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanFanMfgModuleId.setStatus("current")


class _CyanFanMfgPartNumber_Type(DisplayString):
    """Custom type cyanFanMfgPartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CyanFanMfgPartNumber_Type.__name__ = "DisplayString"
_CyanFanMfgPartNumber_Object = MibTableColumn
cyanFanMfgPartNumber = _CyanFanMfgPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 40, 1, 1, 1, 15),
    _CyanFanMfgPartNumber_Type()
)
cyanFanMfgPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanFanMfgPartNumber.setStatus("current")


class _CyanFanMfgRevision_Type(DisplayString):
    """Custom type cyanFanMfgRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_CyanFanMfgRevision_Type.__name__ = "DisplayString"
_CyanFanMfgRevision_Object = MibTableColumn
cyanFanMfgRevision = _CyanFanMfgRevision_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 40, 1, 1, 1, 16),
    _CyanFanMfgRevision_Type()
)
cyanFanMfgRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanFanMfgRevision.setStatus("current")


class _CyanFanMfgSerialNumber_Type(DisplayString):
    """Custom type cyanFanMfgSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CyanFanMfgSerialNumber_Type.__name__ = "DisplayString"
_CyanFanMfgSerialNumber_Object = MibTableColumn
cyanFanMfgSerialNumber = _CyanFanMfgSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 40, 1, 1, 1, 17),
    _CyanFanMfgSerialNumber_Type()
)
cyanFanMfgSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanFanMfgSerialNumber.setStatus("current")
_CyanFanName_Type = DisplayString
_CyanFanName_Object = MibTableColumn
cyanFanName = _CyanFanName_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 40, 1, 1, 1, 18),
    _CyanFanName_Type()
)
cyanFanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanFanName.setStatus("current")
_CyanFanOidClass_Type = DisplayString
_CyanFanOidClass_Object = MibTableColumn
cyanFanOidClass = _CyanFanOidClass_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 40, 1, 1, 1, 19),
    _CyanFanOidClass_Type()
)
cyanFanOidClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanFanOidClass.setStatus("current")
_CyanFanOperState_Type = CyanOpStateTc
_CyanFanOperState_Object = MibTableColumn
cyanFanOperState = _CyanFanOperState_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 40, 1, 1, 1, 20),
    _CyanFanOperState_Type()
)
cyanFanOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanFanOperState.setStatus("current")
_CyanFanOperStateQual_Type = CyanOpStateQualTc
_CyanFanOperStateQual_Object = MibTableColumn
cyanFanOperStateQual = _CyanFanOperStateQual_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 40, 1, 1, 1, 21),
    _CyanFanOperStateQual_Type()
)
cyanFanOperStateQual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanFanOperStateQual.setStatus("current")


class _CyanFanOssLabel_Type(DisplayString):
    """Custom type cyanFanOssLabel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_CyanFanOssLabel_Type.__name__ = "DisplayString"
_CyanFanOssLabel_Object = MibTableColumn
cyanFanOssLabel = _CyanFanOssLabel_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 40, 1, 1, 1, 22),
    _CyanFanOssLabel_Type()
)
cyanFanOssLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanFanOssLabel.setStatus("current")


class _CyanFanOwner_Type(DisplayString):
    """Custom type cyanFanOwner based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_CyanFanOwner_Type.__name__ = "DisplayString"
_CyanFanOwner_Object = MibTableColumn
cyanFanOwner = _CyanFanOwner_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 40, 1, 1, 1, 23),
    _CyanFanOwner_Type()
)
cyanFanOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanFanOwner.setStatus("current")


class _CyanFanPartNumber_Type(DisplayString):
    """Custom type cyanFanPartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 11),
    )


_CyanFanPartNumber_Type.__name__ = "DisplayString"
_CyanFanPartNumber_Object = MibTableColumn
cyanFanPartNumber = _CyanFanPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 40, 1, 1, 1, 24),
    _CyanFanPartNumber_Type()
)
cyanFanPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanFanPartNumber.setStatus("current")
_CyanFanPowerLed_Type = CyanLEDTc
_CyanFanPowerLed_Object = MibTableColumn
cyanFanPowerLed = _CyanFanPowerLed_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 40, 1, 1, 1, 25),
    _CyanFanPowerLed_Type()
)
cyanFanPowerLed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanFanPowerLed.setStatus("current")
_CyanFanSecServState_Type = CyanSecServiceStateTc
_CyanFanSecServState_Object = MibTableColumn
cyanFanSecServState = _CyanFanSecServState_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 40, 1, 1, 1, 26),
    _CyanFanSecServState_Type()
)
cyanFanSecServState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanFanSecServState.setStatus("current")
_CyanFanType_Type = CyanTypeTc
_CyanFanType_Object = MibTableColumn
cyanFanType = _CyanFanType_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 40, 1, 1, 1, 27),
    _CyanFanType_Type()
)
cyanFanType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanFanType.setStatus("current")

# Managed Objects groups

cyanFanObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 40, 20)
)
cyanFanObjectGroup.setObjects(
      *(("CYAN-FAN-MIB", "cyanFanAdminState"),
        ("CYAN-FAN-MIB", "cyanFanAlarmLed"),
        ("CYAN-FAN-MIB", "cyanFanAssetTag"),
        ("CYAN-FAN-MIB", "cyanFanAutoinserviceSoakTimeSec"),
        ("CYAN-FAN-MIB", "cyanFanBaseMacAddress"),
        ("CYAN-FAN-MIB", "cyanFanDescription"),
        ("CYAN-FAN-MIB", "cyanFanHotSwapLed"),
        ("CYAN-FAN-MIB", "cyanFanIdentifier"),
        ("CYAN-FAN-MIB", "cyanFanMacBlockSize"),
        ("CYAN-FAN-MIB", "cyanFanMfgCleiCode"),
        ("CYAN-FAN-MIB", "cyanFanMfgEciCode"),
        ("CYAN-FAN-MIB", "cyanFanMfgModuleId"),
        ("CYAN-FAN-MIB", "cyanFanMfgPartNumber"),
        ("CYAN-FAN-MIB", "cyanFanMfgRevision"),
        ("CYAN-FAN-MIB", "cyanFanMfgSerialNumber"),
        ("CYAN-FAN-MIB", "cyanFanName"),
        ("CYAN-FAN-MIB", "cyanFanOidClass"),
        ("CYAN-FAN-MIB", "cyanFanOperState"),
        ("CYAN-FAN-MIB", "cyanFanOperStateQual"),
        ("CYAN-FAN-MIB", "cyanFanOssLabel"),
        ("CYAN-FAN-MIB", "cyanFanOwner"),
        ("CYAN-FAN-MIB", "cyanFanPartNumber"),
        ("CYAN-FAN-MIB", "cyanFanPowerLed"),
        ("CYAN-FAN-MIB", "cyanFanSecServState"),
        ("CYAN-FAN-MIB", "cyanFanType"))
)
if mibBuilder.loadTexts:
    cyanFanObjectGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cyanFanCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 40, 30)
)
if mibBuilder.loadTexts:
    cyanFanCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CYAN-FAN-MIB",
    **{"cyanFanModule": cyanFanModule,
       "cyanFanMibObjects": cyanFanMibObjects,
       "cyanFanTable": cyanFanTable,
       "cyanFanEntry": cyanFanEntry,
       "cyanFanShelfId": cyanFanShelfId,
       "cyanFanFanId": cyanFanFanId,
       "cyanFanAdminState": cyanFanAdminState,
       "cyanFanAlarmLed": cyanFanAlarmLed,
       "cyanFanAssetTag": cyanFanAssetTag,
       "cyanFanAutoinserviceSoakTimeSec": cyanFanAutoinserviceSoakTimeSec,
       "cyanFanBaseMacAddress": cyanFanBaseMacAddress,
       "cyanFanDescription": cyanFanDescription,
       "cyanFanHotSwapLed": cyanFanHotSwapLed,
       "cyanFanIdentifier": cyanFanIdentifier,
       "cyanFanMacBlockSize": cyanFanMacBlockSize,
       "cyanFanMfgCleiCode": cyanFanMfgCleiCode,
       "cyanFanMfgEciCode": cyanFanMfgEciCode,
       "cyanFanMfgModuleId": cyanFanMfgModuleId,
       "cyanFanMfgPartNumber": cyanFanMfgPartNumber,
       "cyanFanMfgRevision": cyanFanMfgRevision,
       "cyanFanMfgSerialNumber": cyanFanMfgSerialNumber,
       "cyanFanName": cyanFanName,
       "cyanFanOidClass": cyanFanOidClass,
       "cyanFanOperState": cyanFanOperState,
       "cyanFanOperStateQual": cyanFanOperStateQual,
       "cyanFanOssLabel": cyanFanOssLabel,
       "cyanFanOwner": cyanFanOwner,
       "cyanFanPartNumber": cyanFanPartNumber,
       "cyanFanPowerLed": cyanFanPowerLed,
       "cyanFanSecServState": cyanFanSecServState,
       "cyanFanType": cyanFanType,
       "cyanFanObjectGroup": cyanFanObjectGroup,
       "cyanFanCompliance": cyanFanCompliance}
)
