# SNMP MIB module (CYAN-BTM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CYAN-BTM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:21:05 2024
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
 CyanOpStateQualTc,
 CyanOpStateTc,
 CyanRelayTc,
 CyanSecServiceStateTc) = mibBuilder.importSymbols(
    "CYAN-TC-MIB",
    "CyanAdminStateTc",
    "CyanOpStateQualTc",
    "CyanOpStateTc",
    "CyanRelayTc",
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

cyanBtmModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 60)
)
cyanBtmModule.setRevisions(
        ("2014-12-07 05:45",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CyanBtmMibObjects_ObjectIdentity = ObjectIdentity
cyanBtmMibObjects = _CyanBtmMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 60, 1)
)
_CyanBtmTable_Object = MibTable
cyanBtmTable = _CyanBtmTable_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 60, 1, 1)
)
if mibBuilder.loadTexts:
    cyanBtmTable.setStatus("current")
_CyanBtmEntry_Object = MibTableRow
cyanBtmEntry = _CyanBtmEntry_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 60, 1, 1, 1)
)
cyanBtmEntry.setIndexNames(
    (0, "CYAN-BTM-MIB", "cyanBtmShelfId"),
    (0, "CYAN-BTM-MIB", "cyanBtmBtmId"),
)
if mibBuilder.loadTexts:
    cyanBtmEntry.setStatus("current")


class _CyanBtmShelfId_Type(Unsigned32):
    """Custom type cyanBtmShelfId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CyanBtmShelfId_Type.__name__ = "Unsigned32"
_CyanBtmShelfId_Object = MibTableColumn
cyanBtmShelfId = _CyanBtmShelfId_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 60, 1, 1, 1, 1),
    _CyanBtmShelfId_Type()
)
cyanBtmShelfId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cyanBtmShelfId.setStatus("current")
_CyanBtmBtmId_Type = Unsigned32
_CyanBtmBtmId_Object = MibTableColumn
cyanBtmBtmId = _CyanBtmBtmId_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 60, 1, 1, 1, 2),
    _CyanBtmBtmId_Type()
)
cyanBtmBtmId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cyanBtmBtmId.setStatus("current")
_CyanBtmAdminState_Type = CyanAdminStateTc
_CyanBtmAdminState_Object = MibTableColumn
cyanBtmAdminState = _CyanBtmAdminState_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 60, 1, 1, 1, 3),
    _CyanBtmAdminState_Type()
)
cyanBtmAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanBtmAdminState.setStatus("current")


class _CyanBtmAssetTag_Type(DisplayString):
    """Custom type cyanBtmAssetTag based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 124),
    )


_CyanBtmAssetTag_Type.__name__ = "DisplayString"
_CyanBtmAssetTag_Object = MibTableColumn
cyanBtmAssetTag = _CyanBtmAssetTag_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 60, 1, 1, 1, 4),
    _CyanBtmAssetTag_Type()
)
cyanBtmAssetTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanBtmAssetTag.setStatus("current")
_CyanBtmAudible_Type = CyanRelayTc
_CyanBtmAudible_Object = MibTableColumn
cyanBtmAudible = _CyanBtmAudible_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 60, 1, 1, 1, 5),
    _CyanBtmAudible_Type()
)
cyanBtmAudible.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanBtmAudible.setStatus("current")
_CyanBtmAutoinserviceSoakTimeSec_Type = Integer32
_CyanBtmAutoinserviceSoakTimeSec_Object = MibTableColumn
cyanBtmAutoinserviceSoakTimeSec = _CyanBtmAutoinserviceSoakTimeSec_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 60, 1, 1, 1, 6),
    _CyanBtmAutoinserviceSoakTimeSec_Type()
)
cyanBtmAutoinserviceSoakTimeSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanBtmAutoinserviceSoakTimeSec.setStatus("current")
_CyanBtmBaseMacAddress_Type = DisplayString
_CyanBtmBaseMacAddress_Object = MibTableColumn
cyanBtmBaseMacAddress = _CyanBtmBaseMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 60, 1, 1, 1, 7),
    _CyanBtmBaseMacAddress_Type()
)
cyanBtmBaseMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanBtmBaseMacAddress.setStatus("current")
_CyanBtmCritical_Type = CyanRelayTc
_CyanBtmCritical_Object = MibTableColumn
cyanBtmCritical = _CyanBtmCritical_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 60, 1, 1, 1, 8),
    _CyanBtmCritical_Type()
)
cyanBtmCritical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanBtmCritical.setStatus("current")


class _CyanBtmDescription_Type(DisplayString):
    """Custom type cyanBtmDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CyanBtmDescription_Type.__name__ = "DisplayString"
_CyanBtmDescription_Object = MibTableColumn
cyanBtmDescription = _CyanBtmDescription_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 60, 1, 1, 1, 9),
    _CyanBtmDescription_Type()
)
cyanBtmDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanBtmDescription.setStatus("current")
_CyanBtmIdentifier_Type = DisplayString
_CyanBtmIdentifier_Object = MibTableColumn
cyanBtmIdentifier = _CyanBtmIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 60, 1, 1, 1, 10),
    _CyanBtmIdentifier_Type()
)
cyanBtmIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanBtmIdentifier.setStatus("current")


class _CyanBtmMacBlockSize_Type(Unsigned32):
    """Custom type cyanBtmMacBlockSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CyanBtmMacBlockSize_Type.__name__ = "Unsigned32"
_CyanBtmMacBlockSize_Object = MibTableColumn
cyanBtmMacBlockSize = _CyanBtmMacBlockSize_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 60, 1, 1, 1, 11),
    _CyanBtmMacBlockSize_Type()
)
cyanBtmMacBlockSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanBtmMacBlockSize.setStatus("current")
_CyanBtmMajor_Type = CyanRelayTc
_CyanBtmMajor_Object = MibTableColumn
cyanBtmMajor = _CyanBtmMajor_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 60, 1, 1, 1, 12),
    _CyanBtmMajor_Type()
)
cyanBtmMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanBtmMajor.setStatus("current")


class _CyanBtmMfgCleiCode_Type(DisplayString):
    """Custom type cyanBtmMfgCleiCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_CyanBtmMfgCleiCode_Type.__name__ = "DisplayString"
_CyanBtmMfgCleiCode_Object = MibTableColumn
cyanBtmMfgCleiCode = _CyanBtmMfgCleiCode_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 60, 1, 1, 1, 13),
    _CyanBtmMfgCleiCode_Type()
)
cyanBtmMfgCleiCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanBtmMfgCleiCode.setStatus("current")


class _CyanBtmMfgEciCode_Type(DisplayString):
    """Custom type cyanBtmMfgEciCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_CyanBtmMfgEciCode_Type.__name__ = "DisplayString"
_CyanBtmMfgEciCode_Object = MibTableColumn
cyanBtmMfgEciCode = _CyanBtmMfgEciCode_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 60, 1, 1, 1, 14),
    _CyanBtmMfgEciCode_Type()
)
cyanBtmMfgEciCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanBtmMfgEciCode.setStatus("current")
_CyanBtmMfgModuleId_Type = Unsigned32
_CyanBtmMfgModuleId_Object = MibTableColumn
cyanBtmMfgModuleId = _CyanBtmMfgModuleId_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 60, 1, 1, 1, 15),
    _CyanBtmMfgModuleId_Type()
)
cyanBtmMfgModuleId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanBtmMfgModuleId.setStatus("current")


class _CyanBtmMfgPartNumber_Type(DisplayString):
    """Custom type cyanBtmMfgPartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CyanBtmMfgPartNumber_Type.__name__ = "DisplayString"
_CyanBtmMfgPartNumber_Object = MibTableColumn
cyanBtmMfgPartNumber = _CyanBtmMfgPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 60, 1, 1, 1, 16),
    _CyanBtmMfgPartNumber_Type()
)
cyanBtmMfgPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanBtmMfgPartNumber.setStatus("current")


class _CyanBtmMfgRevision_Type(DisplayString):
    """Custom type cyanBtmMfgRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_CyanBtmMfgRevision_Type.__name__ = "DisplayString"
_CyanBtmMfgRevision_Object = MibTableColumn
cyanBtmMfgRevision = _CyanBtmMfgRevision_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 60, 1, 1, 1, 17),
    _CyanBtmMfgRevision_Type()
)
cyanBtmMfgRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanBtmMfgRevision.setStatus("current")


class _CyanBtmMfgSerialNumber_Type(DisplayString):
    """Custom type cyanBtmMfgSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CyanBtmMfgSerialNumber_Type.__name__ = "DisplayString"
_CyanBtmMfgSerialNumber_Object = MibTableColumn
cyanBtmMfgSerialNumber = _CyanBtmMfgSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 60, 1, 1, 1, 18),
    _CyanBtmMfgSerialNumber_Type()
)
cyanBtmMfgSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanBtmMfgSerialNumber.setStatus("current")
_CyanBtmMinor_Type = CyanRelayTc
_CyanBtmMinor_Object = MibTableColumn
cyanBtmMinor = _CyanBtmMinor_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 60, 1, 1, 1, 19),
    _CyanBtmMinor_Type()
)
cyanBtmMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanBtmMinor.setStatus("current")
_CyanBtmName_Type = DisplayString
_CyanBtmName_Object = MibTableColumn
cyanBtmName = _CyanBtmName_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 60, 1, 1, 1, 20),
    _CyanBtmName_Type()
)
cyanBtmName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanBtmName.setStatus("current")
_CyanBtmOidClass_Type = DisplayString
_CyanBtmOidClass_Object = MibTableColumn
cyanBtmOidClass = _CyanBtmOidClass_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 60, 1, 1, 1, 21),
    _CyanBtmOidClass_Type()
)
cyanBtmOidClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanBtmOidClass.setStatus("current")
_CyanBtmOperState_Type = CyanOpStateTc
_CyanBtmOperState_Object = MibTableColumn
cyanBtmOperState = _CyanBtmOperState_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 60, 1, 1, 1, 22),
    _CyanBtmOperState_Type()
)
cyanBtmOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanBtmOperState.setStatus("current")
_CyanBtmOperStateQual_Type = CyanOpStateQualTc
_CyanBtmOperStateQual_Object = MibTableColumn
cyanBtmOperStateQual = _CyanBtmOperStateQual_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 60, 1, 1, 1, 23),
    _CyanBtmOperStateQual_Type()
)
cyanBtmOperStateQual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanBtmOperStateQual.setStatus("current")


class _CyanBtmOssLabel_Type(DisplayString):
    """Custom type cyanBtmOssLabel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_CyanBtmOssLabel_Type.__name__ = "DisplayString"
_CyanBtmOssLabel_Object = MibTableColumn
cyanBtmOssLabel = _CyanBtmOssLabel_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 60, 1, 1, 1, 24),
    _CyanBtmOssLabel_Type()
)
cyanBtmOssLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanBtmOssLabel.setStatus("current")


class _CyanBtmOwner_Type(DisplayString):
    """Custom type cyanBtmOwner based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_CyanBtmOwner_Type.__name__ = "DisplayString"
_CyanBtmOwner_Object = MibTableColumn
cyanBtmOwner = _CyanBtmOwner_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 60, 1, 1, 1, 25),
    _CyanBtmOwner_Type()
)
cyanBtmOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanBtmOwner.setStatus("current")


class _CyanBtmPartNumber_Type(DisplayString):
    """Custom type cyanBtmPartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 11),
    )


_CyanBtmPartNumber_Type.__name__ = "DisplayString"
_CyanBtmPartNumber_Object = MibTableColumn
cyanBtmPartNumber = _CyanBtmPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 60, 1, 1, 1, 26),
    _CyanBtmPartNumber_Type()
)
cyanBtmPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanBtmPartNumber.setStatus("current")
_CyanBtmSecServState_Type = CyanSecServiceStateTc
_CyanBtmSecServState_Object = MibTableColumn
cyanBtmSecServState = _CyanBtmSecServState_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 60, 1, 1, 1, 27),
    _CyanBtmSecServState_Type()
)
cyanBtmSecServState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanBtmSecServState.setStatus("current")
_CyanBtmType_Type = CyanTypeTc
_CyanBtmType_Object = MibTableColumn
cyanBtmType = _CyanBtmType_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 60, 1, 1, 1, 28),
    _CyanBtmType_Type()
)
cyanBtmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanBtmType.setStatus("current")

# Managed Objects groups

cyanBtmObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 60, 20)
)
cyanBtmObjectGroup.setObjects(
      *(("CYAN-BTM-MIB", "cyanBtmAdminState"),
        ("CYAN-BTM-MIB", "cyanBtmAssetTag"),
        ("CYAN-BTM-MIB", "cyanBtmAudible"),
        ("CYAN-BTM-MIB", "cyanBtmAutoinserviceSoakTimeSec"),
        ("CYAN-BTM-MIB", "cyanBtmBaseMacAddress"),
        ("CYAN-BTM-MIB", "cyanBtmCritical"),
        ("CYAN-BTM-MIB", "cyanBtmDescription"),
        ("CYAN-BTM-MIB", "cyanBtmIdentifier"),
        ("CYAN-BTM-MIB", "cyanBtmMacBlockSize"),
        ("CYAN-BTM-MIB", "cyanBtmMajor"),
        ("CYAN-BTM-MIB", "cyanBtmMfgCleiCode"),
        ("CYAN-BTM-MIB", "cyanBtmMfgEciCode"),
        ("CYAN-BTM-MIB", "cyanBtmMfgModuleId"),
        ("CYAN-BTM-MIB", "cyanBtmMfgPartNumber"),
        ("CYAN-BTM-MIB", "cyanBtmMfgRevision"),
        ("CYAN-BTM-MIB", "cyanBtmMfgSerialNumber"),
        ("CYAN-BTM-MIB", "cyanBtmMinor"),
        ("CYAN-BTM-MIB", "cyanBtmName"),
        ("CYAN-BTM-MIB", "cyanBtmOidClass"),
        ("CYAN-BTM-MIB", "cyanBtmOperState"),
        ("CYAN-BTM-MIB", "cyanBtmOperStateQual"),
        ("CYAN-BTM-MIB", "cyanBtmOssLabel"),
        ("CYAN-BTM-MIB", "cyanBtmOwner"),
        ("CYAN-BTM-MIB", "cyanBtmPartNumber"),
        ("CYAN-BTM-MIB", "cyanBtmSecServState"),
        ("CYAN-BTM-MIB", "cyanBtmType"))
)
if mibBuilder.loadTexts:
    cyanBtmObjectGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cyanBtmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 60, 30)
)
if mibBuilder.loadTexts:
    cyanBtmCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CYAN-BTM-MIB",
    **{"cyanBtmModule": cyanBtmModule,
       "cyanBtmMibObjects": cyanBtmMibObjects,
       "cyanBtmTable": cyanBtmTable,
       "cyanBtmEntry": cyanBtmEntry,
       "cyanBtmShelfId": cyanBtmShelfId,
       "cyanBtmBtmId": cyanBtmBtmId,
       "cyanBtmAdminState": cyanBtmAdminState,
       "cyanBtmAssetTag": cyanBtmAssetTag,
       "cyanBtmAudible": cyanBtmAudible,
       "cyanBtmAutoinserviceSoakTimeSec": cyanBtmAutoinserviceSoakTimeSec,
       "cyanBtmBaseMacAddress": cyanBtmBaseMacAddress,
       "cyanBtmCritical": cyanBtmCritical,
       "cyanBtmDescription": cyanBtmDescription,
       "cyanBtmIdentifier": cyanBtmIdentifier,
       "cyanBtmMacBlockSize": cyanBtmMacBlockSize,
       "cyanBtmMajor": cyanBtmMajor,
       "cyanBtmMfgCleiCode": cyanBtmMfgCleiCode,
       "cyanBtmMfgEciCode": cyanBtmMfgEciCode,
       "cyanBtmMfgModuleId": cyanBtmMfgModuleId,
       "cyanBtmMfgPartNumber": cyanBtmMfgPartNumber,
       "cyanBtmMfgRevision": cyanBtmMfgRevision,
       "cyanBtmMfgSerialNumber": cyanBtmMfgSerialNumber,
       "cyanBtmMinor": cyanBtmMinor,
       "cyanBtmName": cyanBtmName,
       "cyanBtmOidClass": cyanBtmOidClass,
       "cyanBtmOperState": cyanBtmOperState,
       "cyanBtmOperStateQual": cyanBtmOperStateQual,
       "cyanBtmOssLabel": cyanBtmOssLabel,
       "cyanBtmOwner": cyanBtmOwner,
       "cyanBtmPartNumber": cyanBtmPartNumber,
       "cyanBtmSecServState": cyanBtmSecServState,
       "cyanBtmType": cyanBtmType,
       "cyanBtmObjectGroup": cyanBtmObjectGroup,
       "cyanBtmCompliance": cyanBtmCompliance}
)
