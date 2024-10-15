# SNMP MIB module (CYAN-SHELF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CYAN-SHELF-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:21:16 2024
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

(CyanNoYesTc,
 CyanOpStateQualTc,
 CyanOpStateTc,
 CyanSecServiceStateTc) = mibBuilder.importSymbols(
    "CYAN-TC-MIB",
    "CyanNoYesTc",
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

cyanShelfModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 20)
)
cyanShelfModule.setRevisions(
        ("2014-12-07 05:45",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CyanShelfMibObjects_ObjectIdentity = ObjectIdentity
cyanShelfMibObjects = _CyanShelfMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 20, 1)
)
_CyanShelfTable_Object = MibTable
cyanShelfTable = _CyanShelfTable_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 20, 1, 1)
)
if mibBuilder.loadTexts:
    cyanShelfTable.setStatus("current")
_CyanShelfEntry_Object = MibTableRow
cyanShelfEntry = _CyanShelfEntry_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 20, 1, 1, 1)
)
cyanShelfEntry.setIndexNames(
    (0, "CYAN-SHELF-MIB", "cyanShelfShelfId"),
)
if mibBuilder.loadTexts:
    cyanShelfEntry.setStatus("current")


class _CyanShelfShelfId_Type(Unsigned32):
    """Custom type cyanShelfShelfId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CyanShelfShelfId_Type.__name__ = "Unsigned32"
_CyanShelfShelfId_Object = MibTableColumn
cyanShelfShelfId = _CyanShelfShelfId_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 20, 1, 1, 1, 1),
    _CyanShelfShelfId_Type()
)
cyanShelfShelfId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cyanShelfShelfId.setStatus("current")


class _CyanShelfAssetTag_Type(DisplayString):
    """Custom type cyanShelfAssetTag based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 124),
    )


_CyanShelfAssetTag_Type.__name__ = "DisplayString"
_CyanShelfAssetTag_Object = MibTableColumn
cyanShelfAssetTag = _CyanShelfAssetTag_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 20, 1, 1, 1, 2),
    _CyanShelfAssetTag_Type()
)
cyanShelfAssetTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanShelfAssetTag.setStatus("current")
_CyanShelfAutoprovisioningFlag_Type = CyanNoYesTc
_CyanShelfAutoprovisioningFlag_Object = MibTableColumn
cyanShelfAutoprovisioningFlag = _CyanShelfAutoprovisioningFlag_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 20, 1, 1, 1, 3),
    _CyanShelfAutoprovisioningFlag_Type()
)
cyanShelfAutoprovisioningFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanShelfAutoprovisioningFlag.setStatus("current")
_CyanShelfBaseMacAddress_Type = DisplayString
_CyanShelfBaseMacAddress_Object = MibTableColumn
cyanShelfBaseMacAddress = _CyanShelfBaseMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 20, 1, 1, 1, 4),
    _CyanShelfBaseMacAddress_Type()
)
cyanShelfBaseMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanShelfBaseMacAddress.setStatus("current")


class _CyanShelfBay_Type(DisplayString):
    """Custom type cyanShelfBay based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CyanShelfBay_Type.__name__ = "DisplayString"
_CyanShelfBay_Object = MibTableColumn
cyanShelfBay = _CyanShelfBay_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 20, 1, 1, 1, 5),
    _CyanShelfBay_Type()
)
cyanShelfBay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanShelfBay.setStatus("current")
_CyanShelfDaysSinceLastReplacement_Type = Unsigned32
_CyanShelfDaysSinceLastReplacement_Object = MibTableColumn
cyanShelfDaysSinceLastReplacement = _CyanShelfDaysSinceLastReplacement_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 20, 1, 1, 1, 6),
    _CyanShelfDaysSinceLastReplacement_Type()
)
cyanShelfDaysSinceLastReplacement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanShelfDaysSinceLastReplacement.setStatus("current")


class _CyanShelfDescription_Type(DisplayString):
    """Custom type cyanShelfDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CyanShelfDescription_Type.__name__ = "DisplayString"
_CyanShelfDescription_Object = MibTableColumn
cyanShelfDescription = _CyanShelfDescription_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 20, 1, 1, 1, 7),
    _CyanShelfDescription_Type()
)
cyanShelfDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanShelfDescription.setStatus("current")
_CyanShelfFanFilterReplacingIntervalDays_Type = Unsigned32
_CyanShelfFanFilterReplacingIntervalDays_Object = MibTableColumn
cyanShelfFanFilterReplacingIntervalDays = _CyanShelfFanFilterReplacingIntervalDays_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 20, 1, 1, 1, 8),
    _CyanShelfFanFilterReplacingIntervalDays_Type()
)
cyanShelfFanFilterReplacingIntervalDays.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanShelfFanFilterReplacingIntervalDays.setStatus("current")
_CyanShelfFanSpeed_Type = Integer32
_CyanShelfFanSpeed_Object = MibTableColumn
cyanShelfFanSpeed = _CyanShelfFanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 20, 1, 1, 1, 9),
    _CyanShelfFanSpeed_Type()
)
cyanShelfFanSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanShelfFanSpeed.setStatus("current")
_CyanShelfIdentifier_Type = DisplayString
_CyanShelfIdentifier_Object = MibTableColumn
cyanShelfIdentifier = _CyanShelfIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 20, 1, 1, 1, 10),
    _CyanShelfIdentifier_Type()
)
cyanShelfIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanShelfIdentifier.setStatus("current")


class _CyanShelfMacBlockSize_Type(Unsigned32):
    """Custom type cyanShelfMacBlockSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CyanShelfMacBlockSize_Type.__name__ = "Unsigned32"
_CyanShelfMacBlockSize_Object = MibTableColumn
cyanShelfMacBlockSize = _CyanShelfMacBlockSize_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 20, 1, 1, 1, 11),
    _CyanShelfMacBlockSize_Type()
)
cyanShelfMacBlockSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanShelfMacBlockSize.setStatus("current")


class _CyanShelfMfgCleiCode_Type(DisplayString):
    """Custom type cyanShelfMfgCleiCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_CyanShelfMfgCleiCode_Type.__name__ = "DisplayString"
_CyanShelfMfgCleiCode_Object = MibTableColumn
cyanShelfMfgCleiCode = _CyanShelfMfgCleiCode_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 20, 1, 1, 1, 12),
    _CyanShelfMfgCleiCode_Type()
)
cyanShelfMfgCleiCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanShelfMfgCleiCode.setStatus("current")


class _CyanShelfMfgEciCode_Type(DisplayString):
    """Custom type cyanShelfMfgEciCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_CyanShelfMfgEciCode_Type.__name__ = "DisplayString"
_CyanShelfMfgEciCode_Object = MibTableColumn
cyanShelfMfgEciCode = _CyanShelfMfgEciCode_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 20, 1, 1, 1, 13),
    _CyanShelfMfgEciCode_Type()
)
cyanShelfMfgEciCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanShelfMfgEciCode.setStatus("current")
_CyanShelfMfgModuleId_Type = Unsigned32
_CyanShelfMfgModuleId_Object = MibTableColumn
cyanShelfMfgModuleId = _CyanShelfMfgModuleId_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 20, 1, 1, 1, 14),
    _CyanShelfMfgModuleId_Type()
)
cyanShelfMfgModuleId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanShelfMfgModuleId.setStatus("current")


class _CyanShelfMfgPartNumber_Type(DisplayString):
    """Custom type cyanShelfMfgPartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CyanShelfMfgPartNumber_Type.__name__ = "DisplayString"
_CyanShelfMfgPartNumber_Object = MibTableColumn
cyanShelfMfgPartNumber = _CyanShelfMfgPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 20, 1, 1, 1, 15),
    _CyanShelfMfgPartNumber_Type()
)
cyanShelfMfgPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanShelfMfgPartNumber.setStatus("current")


class _CyanShelfMfgRevision_Type(DisplayString):
    """Custom type cyanShelfMfgRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_CyanShelfMfgRevision_Type.__name__ = "DisplayString"
_CyanShelfMfgRevision_Object = MibTableColumn
cyanShelfMfgRevision = _CyanShelfMfgRevision_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 20, 1, 1, 1, 16),
    _CyanShelfMfgRevision_Type()
)
cyanShelfMfgRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanShelfMfgRevision.setStatus("current")


class _CyanShelfMfgSerialNumber_Type(DisplayString):
    """Custom type cyanShelfMfgSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CyanShelfMfgSerialNumber_Type.__name__ = "DisplayString"
_CyanShelfMfgSerialNumber_Object = MibTableColumn
cyanShelfMfgSerialNumber = _CyanShelfMfgSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 20, 1, 1, 1, 17),
    _CyanShelfMfgSerialNumber_Type()
)
cyanShelfMfgSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanShelfMfgSerialNumber.setStatus("current")
_CyanShelfName_Type = DisplayString
_CyanShelfName_Object = MibTableColumn
cyanShelfName = _CyanShelfName_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 20, 1, 1, 1, 18),
    _CyanShelfName_Type()
)
cyanShelfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanShelfName.setStatus("current")
_CyanShelfOidClass_Type = DisplayString
_CyanShelfOidClass_Object = MibTableColumn
cyanShelfOidClass = _CyanShelfOidClass_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 20, 1, 1, 1, 19),
    _CyanShelfOidClass_Type()
)
cyanShelfOidClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanShelfOidClass.setStatus("current")
_CyanShelfOperState_Type = CyanOpStateTc
_CyanShelfOperState_Object = MibTableColumn
cyanShelfOperState = _CyanShelfOperState_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 20, 1, 1, 1, 20),
    _CyanShelfOperState_Type()
)
cyanShelfOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanShelfOperState.setStatus("current")
_CyanShelfOperStateQual_Type = CyanOpStateQualTc
_CyanShelfOperStateQual_Object = MibTableColumn
cyanShelfOperStateQual = _CyanShelfOperStateQual_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 20, 1, 1, 1, 21),
    _CyanShelfOperStateQual_Type()
)
cyanShelfOperStateQual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanShelfOperStateQual.setStatus("current")


class _CyanShelfOssLabel_Type(DisplayString):
    """Custom type cyanShelfOssLabel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_CyanShelfOssLabel_Type.__name__ = "DisplayString"
_CyanShelfOssLabel_Object = MibTableColumn
cyanShelfOssLabel = _CyanShelfOssLabel_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 20, 1, 1, 1, 22),
    _CyanShelfOssLabel_Type()
)
cyanShelfOssLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanShelfOssLabel.setStatus("current")


class _CyanShelfOwner_Type(DisplayString):
    """Custom type cyanShelfOwner based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_CyanShelfOwner_Type.__name__ = "DisplayString"
_CyanShelfOwner_Object = MibTableColumn
cyanShelfOwner = _CyanShelfOwner_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 20, 1, 1, 1, 23),
    _CyanShelfOwner_Type()
)
cyanShelfOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanShelfOwner.setStatus("current")


class _CyanShelfRackUnits_Type(DisplayString):
    """Custom type cyanShelfRackUnits based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CyanShelfRackUnits_Type.__name__ = "DisplayString"
_CyanShelfRackUnits_Object = MibTableColumn
cyanShelfRackUnits = _CyanShelfRackUnits_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 20, 1, 1, 1, 24),
    _CyanShelfRackUnits_Type()
)
cyanShelfRackUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanShelfRackUnits.setStatus("current")


class _CyanShelfRelayRack_Type(DisplayString):
    """Custom type cyanShelfRelayRack based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CyanShelfRelayRack_Type.__name__ = "DisplayString"
_CyanShelfRelayRack_Object = MibTableColumn
cyanShelfRelayRack = _CyanShelfRelayRack_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 20, 1, 1, 1, 25),
    _CyanShelfRelayRack_Type()
)
cyanShelfRelayRack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanShelfRelayRack.setStatus("current")
_CyanShelfSecServState_Type = CyanSecServiceStateTc
_CyanShelfSecServState_Object = MibTableColumn
cyanShelfSecServState = _CyanShelfSecServState_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 20, 1, 1, 1, 26),
    _CyanShelfSecServState_Type()
)
cyanShelfSecServState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanShelfSecServState.setStatus("current")
_CyanShelfType_Type = CyanTypeTc
_CyanShelfType_Object = MibTableColumn
cyanShelfType = _CyanShelfType_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 20, 1, 1, 1, 27),
    _CyanShelfType_Type()
)
cyanShelfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanShelfType.setStatus("current")

# Managed Objects groups

cyanShelfObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 20, 20)
)
cyanShelfObjectGroup.setObjects(
      *(("CYAN-SHELF-MIB", "cyanShelfAssetTag"),
        ("CYAN-SHELF-MIB", "cyanShelfAutoprovisioningFlag"),
        ("CYAN-SHELF-MIB", "cyanShelfBaseMacAddress"),
        ("CYAN-SHELF-MIB", "cyanShelfBay"),
        ("CYAN-SHELF-MIB", "cyanShelfDaysSinceLastReplacement"),
        ("CYAN-SHELF-MIB", "cyanShelfDescription"),
        ("CYAN-SHELF-MIB", "cyanShelfFanFilterReplacingIntervalDays"),
        ("CYAN-SHELF-MIB", "cyanShelfFanSpeed"),
        ("CYAN-SHELF-MIB", "cyanShelfIdentifier"),
        ("CYAN-SHELF-MIB", "cyanShelfMacBlockSize"),
        ("CYAN-SHELF-MIB", "cyanShelfMfgCleiCode"),
        ("CYAN-SHELF-MIB", "cyanShelfMfgEciCode"),
        ("CYAN-SHELF-MIB", "cyanShelfMfgModuleId"),
        ("CYAN-SHELF-MIB", "cyanShelfMfgPartNumber"),
        ("CYAN-SHELF-MIB", "cyanShelfMfgRevision"),
        ("CYAN-SHELF-MIB", "cyanShelfMfgSerialNumber"),
        ("CYAN-SHELF-MIB", "cyanShelfName"),
        ("CYAN-SHELF-MIB", "cyanShelfOidClass"),
        ("CYAN-SHELF-MIB", "cyanShelfOperState"),
        ("CYAN-SHELF-MIB", "cyanShelfOperStateQual"),
        ("CYAN-SHELF-MIB", "cyanShelfOssLabel"),
        ("CYAN-SHELF-MIB", "cyanShelfOwner"),
        ("CYAN-SHELF-MIB", "cyanShelfRackUnits"),
        ("CYAN-SHELF-MIB", "cyanShelfRelayRack"),
        ("CYAN-SHELF-MIB", "cyanShelfSecServState"),
        ("CYAN-SHELF-MIB", "cyanShelfType"))
)
if mibBuilder.loadTexts:
    cyanShelfObjectGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cyanShelfCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 20, 30)
)
if mibBuilder.loadTexts:
    cyanShelfCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CYAN-SHELF-MIB",
    **{"cyanShelfModule": cyanShelfModule,
       "cyanShelfMibObjects": cyanShelfMibObjects,
       "cyanShelfTable": cyanShelfTable,
       "cyanShelfEntry": cyanShelfEntry,
       "cyanShelfShelfId": cyanShelfShelfId,
       "cyanShelfAssetTag": cyanShelfAssetTag,
       "cyanShelfAutoprovisioningFlag": cyanShelfAutoprovisioningFlag,
       "cyanShelfBaseMacAddress": cyanShelfBaseMacAddress,
       "cyanShelfBay": cyanShelfBay,
       "cyanShelfDaysSinceLastReplacement": cyanShelfDaysSinceLastReplacement,
       "cyanShelfDescription": cyanShelfDescription,
       "cyanShelfFanFilterReplacingIntervalDays": cyanShelfFanFilterReplacingIntervalDays,
       "cyanShelfFanSpeed": cyanShelfFanSpeed,
       "cyanShelfIdentifier": cyanShelfIdentifier,
       "cyanShelfMacBlockSize": cyanShelfMacBlockSize,
       "cyanShelfMfgCleiCode": cyanShelfMfgCleiCode,
       "cyanShelfMfgEciCode": cyanShelfMfgEciCode,
       "cyanShelfMfgModuleId": cyanShelfMfgModuleId,
       "cyanShelfMfgPartNumber": cyanShelfMfgPartNumber,
       "cyanShelfMfgRevision": cyanShelfMfgRevision,
       "cyanShelfMfgSerialNumber": cyanShelfMfgSerialNumber,
       "cyanShelfName": cyanShelfName,
       "cyanShelfOidClass": cyanShelfOidClass,
       "cyanShelfOperState": cyanShelfOperState,
       "cyanShelfOperStateQual": cyanShelfOperStateQual,
       "cyanShelfOssLabel": cyanShelfOssLabel,
       "cyanShelfOwner": cyanShelfOwner,
       "cyanShelfRackUnits": cyanShelfRackUnits,
       "cyanShelfRelayRack": cyanShelfRelayRack,
       "cyanShelfSecServState": cyanShelfSecServState,
       "cyanShelfType": cyanShelfType,
       "cyanShelfObjectGroup": cyanShelfObjectGroup,
       "cyanShelfCompliance": cyanShelfCompliance}
)
