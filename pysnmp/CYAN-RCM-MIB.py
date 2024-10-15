# SNMP MIB module (CYAN-RCM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CYAN-RCM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:21:14 2024
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
 CyanSecServiceStateTc) = mibBuilder.importSymbols(
    "CYAN-TC-MIB",
    "CyanAdminStateTc",
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

cyanRcmModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 70)
)
cyanRcmModule.setRevisions(
        ("2014-12-07 05:45",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CyanRcmMibObjects_ObjectIdentity = ObjectIdentity
cyanRcmMibObjects = _CyanRcmMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 70, 1)
)
_CyanRcmTable_Object = MibTable
cyanRcmTable = _CyanRcmTable_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 70, 1, 1)
)
if mibBuilder.loadTexts:
    cyanRcmTable.setStatus("current")
_CyanRcmEntry_Object = MibTableRow
cyanRcmEntry = _CyanRcmEntry_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 70, 1, 1, 1)
)
cyanRcmEntry.setIndexNames(
    (0, "CYAN-RCM-MIB", "cyanRcmShelfId"),
    (0, "CYAN-RCM-MIB", "cyanRcmRcmId"),
)
if mibBuilder.loadTexts:
    cyanRcmEntry.setStatus("current")


class _CyanRcmShelfId_Type(Unsigned32):
    """Custom type cyanRcmShelfId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CyanRcmShelfId_Type.__name__ = "Unsigned32"
_CyanRcmShelfId_Object = MibTableColumn
cyanRcmShelfId = _CyanRcmShelfId_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 70, 1, 1, 1, 1),
    _CyanRcmShelfId_Type()
)
cyanRcmShelfId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cyanRcmShelfId.setStatus("current")
_CyanRcmRcmId_Type = Unsigned32
_CyanRcmRcmId_Object = MibTableColumn
cyanRcmRcmId = _CyanRcmRcmId_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 70, 1, 1, 1, 2),
    _CyanRcmRcmId_Type()
)
cyanRcmRcmId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cyanRcmRcmId.setStatus("current")
_CyanRcmAdminState_Type = CyanAdminStateTc
_CyanRcmAdminState_Object = MibTableColumn
cyanRcmAdminState = _CyanRcmAdminState_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 70, 1, 1, 1, 3),
    _CyanRcmAdminState_Type()
)
cyanRcmAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanRcmAdminState.setStatus("current")


class _CyanRcmAssetTag_Type(DisplayString):
    """Custom type cyanRcmAssetTag based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 124),
    )


_CyanRcmAssetTag_Type.__name__ = "DisplayString"
_CyanRcmAssetTag_Object = MibTableColumn
cyanRcmAssetTag = _CyanRcmAssetTag_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 70, 1, 1, 1, 4),
    _CyanRcmAssetTag_Type()
)
cyanRcmAssetTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanRcmAssetTag.setStatus("current")
_CyanRcmAutoinserviceSoakTimeSec_Type = Integer32
_CyanRcmAutoinserviceSoakTimeSec_Object = MibTableColumn
cyanRcmAutoinserviceSoakTimeSec = _CyanRcmAutoinserviceSoakTimeSec_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 70, 1, 1, 1, 5),
    _CyanRcmAutoinserviceSoakTimeSec_Type()
)
cyanRcmAutoinserviceSoakTimeSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanRcmAutoinserviceSoakTimeSec.setStatus("current")
_CyanRcmBaseMacAddress_Type = DisplayString
_CyanRcmBaseMacAddress_Object = MibTableColumn
cyanRcmBaseMacAddress = _CyanRcmBaseMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 70, 1, 1, 1, 6),
    _CyanRcmBaseMacAddress_Type()
)
cyanRcmBaseMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanRcmBaseMacAddress.setStatus("current")


class _CyanRcmDescription_Type(DisplayString):
    """Custom type cyanRcmDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CyanRcmDescription_Type.__name__ = "DisplayString"
_CyanRcmDescription_Object = MibTableColumn
cyanRcmDescription = _CyanRcmDescription_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 70, 1, 1, 1, 7),
    _CyanRcmDescription_Type()
)
cyanRcmDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanRcmDescription.setStatus("current")
_CyanRcmIdentifier_Type = DisplayString
_CyanRcmIdentifier_Object = MibTableColumn
cyanRcmIdentifier = _CyanRcmIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 70, 1, 1, 1, 8),
    _CyanRcmIdentifier_Type()
)
cyanRcmIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanRcmIdentifier.setStatus("current")


class _CyanRcmMacBlockSize_Type(Unsigned32):
    """Custom type cyanRcmMacBlockSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CyanRcmMacBlockSize_Type.__name__ = "Unsigned32"
_CyanRcmMacBlockSize_Object = MibTableColumn
cyanRcmMacBlockSize = _CyanRcmMacBlockSize_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 70, 1, 1, 1, 9),
    _CyanRcmMacBlockSize_Type()
)
cyanRcmMacBlockSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanRcmMacBlockSize.setStatus("current")


class _CyanRcmMfgCleiCode_Type(DisplayString):
    """Custom type cyanRcmMfgCleiCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_CyanRcmMfgCleiCode_Type.__name__ = "DisplayString"
_CyanRcmMfgCleiCode_Object = MibTableColumn
cyanRcmMfgCleiCode = _CyanRcmMfgCleiCode_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 70, 1, 1, 1, 10),
    _CyanRcmMfgCleiCode_Type()
)
cyanRcmMfgCleiCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanRcmMfgCleiCode.setStatus("current")


class _CyanRcmMfgEciCode_Type(DisplayString):
    """Custom type cyanRcmMfgEciCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_CyanRcmMfgEciCode_Type.__name__ = "DisplayString"
_CyanRcmMfgEciCode_Object = MibTableColumn
cyanRcmMfgEciCode = _CyanRcmMfgEciCode_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 70, 1, 1, 1, 11),
    _CyanRcmMfgEciCode_Type()
)
cyanRcmMfgEciCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanRcmMfgEciCode.setStatus("current")
_CyanRcmMfgModuleId_Type = Unsigned32
_CyanRcmMfgModuleId_Object = MibTableColumn
cyanRcmMfgModuleId = _CyanRcmMfgModuleId_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 70, 1, 1, 1, 12),
    _CyanRcmMfgModuleId_Type()
)
cyanRcmMfgModuleId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanRcmMfgModuleId.setStatus("current")


class _CyanRcmMfgPartNumber_Type(DisplayString):
    """Custom type cyanRcmMfgPartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CyanRcmMfgPartNumber_Type.__name__ = "DisplayString"
_CyanRcmMfgPartNumber_Object = MibTableColumn
cyanRcmMfgPartNumber = _CyanRcmMfgPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 70, 1, 1, 1, 13),
    _CyanRcmMfgPartNumber_Type()
)
cyanRcmMfgPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanRcmMfgPartNumber.setStatus("current")


class _CyanRcmMfgRevision_Type(DisplayString):
    """Custom type cyanRcmMfgRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_CyanRcmMfgRevision_Type.__name__ = "DisplayString"
_CyanRcmMfgRevision_Object = MibTableColumn
cyanRcmMfgRevision = _CyanRcmMfgRevision_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 70, 1, 1, 1, 14),
    _CyanRcmMfgRevision_Type()
)
cyanRcmMfgRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanRcmMfgRevision.setStatus("current")


class _CyanRcmMfgSerialNumber_Type(DisplayString):
    """Custom type cyanRcmMfgSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CyanRcmMfgSerialNumber_Type.__name__ = "DisplayString"
_CyanRcmMfgSerialNumber_Object = MibTableColumn
cyanRcmMfgSerialNumber = _CyanRcmMfgSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 70, 1, 1, 1, 15),
    _CyanRcmMfgSerialNumber_Type()
)
cyanRcmMfgSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanRcmMfgSerialNumber.setStatus("current")
_CyanRcmName_Type = DisplayString
_CyanRcmName_Object = MibTableColumn
cyanRcmName = _CyanRcmName_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 70, 1, 1, 1, 16),
    _CyanRcmName_Type()
)
cyanRcmName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanRcmName.setStatus("current")
_CyanRcmOidClass_Type = DisplayString
_CyanRcmOidClass_Object = MibTableColumn
cyanRcmOidClass = _CyanRcmOidClass_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 70, 1, 1, 1, 17),
    _CyanRcmOidClass_Type()
)
cyanRcmOidClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanRcmOidClass.setStatus("current")
_CyanRcmOperState_Type = CyanOpStateTc
_CyanRcmOperState_Object = MibTableColumn
cyanRcmOperState = _CyanRcmOperState_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 70, 1, 1, 1, 18),
    _CyanRcmOperState_Type()
)
cyanRcmOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanRcmOperState.setStatus("current")
_CyanRcmOperStateQual_Type = CyanOpStateQualTc
_CyanRcmOperStateQual_Object = MibTableColumn
cyanRcmOperStateQual = _CyanRcmOperStateQual_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 70, 1, 1, 1, 19),
    _CyanRcmOperStateQual_Type()
)
cyanRcmOperStateQual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanRcmOperStateQual.setStatus("current")


class _CyanRcmOssLabel_Type(DisplayString):
    """Custom type cyanRcmOssLabel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_CyanRcmOssLabel_Type.__name__ = "DisplayString"
_CyanRcmOssLabel_Object = MibTableColumn
cyanRcmOssLabel = _CyanRcmOssLabel_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 70, 1, 1, 1, 20),
    _CyanRcmOssLabel_Type()
)
cyanRcmOssLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanRcmOssLabel.setStatus("current")


class _CyanRcmOwner_Type(DisplayString):
    """Custom type cyanRcmOwner based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_CyanRcmOwner_Type.__name__ = "DisplayString"
_CyanRcmOwner_Object = MibTableColumn
cyanRcmOwner = _CyanRcmOwner_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 70, 1, 1, 1, 21),
    _CyanRcmOwner_Type()
)
cyanRcmOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanRcmOwner.setStatus("current")


class _CyanRcmPartNumber_Type(DisplayString):
    """Custom type cyanRcmPartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 11),
    )


_CyanRcmPartNumber_Type.__name__ = "DisplayString"
_CyanRcmPartNumber_Object = MibTableColumn
cyanRcmPartNumber = _CyanRcmPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 70, 1, 1, 1, 22),
    _CyanRcmPartNumber_Type()
)
cyanRcmPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanRcmPartNumber.setStatus("current")
_CyanRcmSecServState_Type = CyanSecServiceStateTc
_CyanRcmSecServState_Object = MibTableColumn
cyanRcmSecServState = _CyanRcmSecServState_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 70, 1, 1, 1, 23),
    _CyanRcmSecServState_Type()
)
cyanRcmSecServState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanRcmSecServState.setStatus("current")
_CyanRcmType_Type = CyanTypeTc
_CyanRcmType_Object = MibTableColumn
cyanRcmType = _CyanRcmType_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 70, 1, 1, 1, 24),
    _CyanRcmType_Type()
)
cyanRcmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanRcmType.setStatus("current")

# Managed Objects groups

cyanRcmObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 70, 20)
)
cyanRcmObjectGroup.setObjects(
      *(("CYAN-RCM-MIB", "cyanRcmAdminState"),
        ("CYAN-RCM-MIB", "cyanRcmAssetTag"),
        ("CYAN-RCM-MIB", "cyanRcmAutoinserviceSoakTimeSec"),
        ("CYAN-RCM-MIB", "cyanRcmBaseMacAddress"),
        ("CYAN-RCM-MIB", "cyanRcmDescription"),
        ("CYAN-RCM-MIB", "cyanRcmIdentifier"),
        ("CYAN-RCM-MIB", "cyanRcmMacBlockSize"),
        ("CYAN-RCM-MIB", "cyanRcmMfgCleiCode"),
        ("CYAN-RCM-MIB", "cyanRcmMfgEciCode"),
        ("CYAN-RCM-MIB", "cyanRcmMfgModuleId"),
        ("CYAN-RCM-MIB", "cyanRcmMfgPartNumber"),
        ("CYAN-RCM-MIB", "cyanRcmMfgRevision"),
        ("CYAN-RCM-MIB", "cyanRcmMfgSerialNumber"),
        ("CYAN-RCM-MIB", "cyanRcmName"),
        ("CYAN-RCM-MIB", "cyanRcmOidClass"),
        ("CYAN-RCM-MIB", "cyanRcmOperState"),
        ("CYAN-RCM-MIB", "cyanRcmOperStateQual"),
        ("CYAN-RCM-MIB", "cyanRcmOssLabel"),
        ("CYAN-RCM-MIB", "cyanRcmOwner"),
        ("CYAN-RCM-MIB", "cyanRcmPartNumber"),
        ("CYAN-RCM-MIB", "cyanRcmSecServState"),
        ("CYAN-RCM-MIB", "cyanRcmType"))
)
if mibBuilder.loadTexts:
    cyanRcmObjectGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cyanRcmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 70, 30)
)
if mibBuilder.loadTexts:
    cyanRcmCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CYAN-RCM-MIB",
    **{"cyanRcmModule": cyanRcmModule,
       "cyanRcmMibObjects": cyanRcmMibObjects,
       "cyanRcmTable": cyanRcmTable,
       "cyanRcmEntry": cyanRcmEntry,
       "cyanRcmShelfId": cyanRcmShelfId,
       "cyanRcmRcmId": cyanRcmRcmId,
       "cyanRcmAdminState": cyanRcmAdminState,
       "cyanRcmAssetTag": cyanRcmAssetTag,
       "cyanRcmAutoinserviceSoakTimeSec": cyanRcmAutoinserviceSoakTimeSec,
       "cyanRcmBaseMacAddress": cyanRcmBaseMacAddress,
       "cyanRcmDescription": cyanRcmDescription,
       "cyanRcmIdentifier": cyanRcmIdentifier,
       "cyanRcmMacBlockSize": cyanRcmMacBlockSize,
       "cyanRcmMfgCleiCode": cyanRcmMfgCleiCode,
       "cyanRcmMfgEciCode": cyanRcmMfgEciCode,
       "cyanRcmMfgModuleId": cyanRcmMfgModuleId,
       "cyanRcmMfgPartNumber": cyanRcmMfgPartNumber,
       "cyanRcmMfgRevision": cyanRcmMfgRevision,
       "cyanRcmMfgSerialNumber": cyanRcmMfgSerialNumber,
       "cyanRcmName": cyanRcmName,
       "cyanRcmOidClass": cyanRcmOidClass,
       "cyanRcmOperState": cyanRcmOperState,
       "cyanRcmOperStateQual": cyanRcmOperStateQual,
       "cyanRcmOssLabel": cyanRcmOssLabel,
       "cyanRcmOwner": cyanRcmOwner,
       "cyanRcmPartNumber": cyanRcmPartNumber,
       "cyanRcmSecServState": cyanRcmSecServState,
       "cyanRcmType": cyanRcmType,
       "cyanRcmObjectGroup": cyanRcmObjectGroup,
       "cyanRcmCompliance": cyanRcmCompliance}
)
