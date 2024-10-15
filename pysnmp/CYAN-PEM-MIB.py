# SNMP MIB module (CYAN-PEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CYAN-PEM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:21:13 2024
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

cyanPemModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 30)
)
cyanPemModule.setRevisions(
        ("2014-12-07 05:45",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CyanPemMibObjects_ObjectIdentity = ObjectIdentity
cyanPemMibObjects = _CyanPemMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 30, 1)
)
_CyanPemTable_Object = MibTable
cyanPemTable = _CyanPemTable_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 30, 1, 1)
)
if mibBuilder.loadTexts:
    cyanPemTable.setStatus("current")
_CyanPemEntry_Object = MibTableRow
cyanPemEntry = _CyanPemEntry_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 30, 1, 1, 1)
)
cyanPemEntry.setIndexNames(
    (0, "CYAN-PEM-MIB", "cyanPemShelfId"),
    (0, "CYAN-PEM-MIB", "cyanPemPemId"),
)
if mibBuilder.loadTexts:
    cyanPemEntry.setStatus("current")


class _CyanPemShelfId_Type(Unsigned32):
    """Custom type cyanPemShelfId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CyanPemShelfId_Type.__name__ = "Unsigned32"
_CyanPemShelfId_Object = MibTableColumn
cyanPemShelfId = _CyanPemShelfId_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 30, 1, 1, 1, 1),
    _CyanPemShelfId_Type()
)
cyanPemShelfId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cyanPemShelfId.setStatus("current")
_CyanPemPemId_Type = Unsigned32
_CyanPemPemId_Object = MibTableColumn
cyanPemPemId = _CyanPemPemId_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 30, 1, 1, 1, 2),
    _CyanPemPemId_Type()
)
cyanPemPemId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cyanPemPemId.setStatus("current")
_CyanPemAdminState_Type = CyanAdminStateTc
_CyanPemAdminState_Object = MibTableColumn
cyanPemAdminState = _CyanPemAdminState_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 30, 1, 1, 1, 3),
    _CyanPemAdminState_Type()
)
cyanPemAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanPemAdminState.setStatus("current")


class _CyanPemAssetTag_Type(DisplayString):
    """Custom type cyanPemAssetTag based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 124),
    )


_CyanPemAssetTag_Type.__name__ = "DisplayString"
_CyanPemAssetTag_Object = MibTableColumn
cyanPemAssetTag = _CyanPemAssetTag_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 30, 1, 1, 1, 4),
    _CyanPemAssetTag_Type()
)
cyanPemAssetTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanPemAssetTag.setStatus("current")
_CyanPemAutoinserviceSoakTimeSec_Type = Integer32
_CyanPemAutoinserviceSoakTimeSec_Object = MibTableColumn
cyanPemAutoinserviceSoakTimeSec = _CyanPemAutoinserviceSoakTimeSec_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 30, 1, 1, 1, 5),
    _CyanPemAutoinserviceSoakTimeSec_Type()
)
cyanPemAutoinserviceSoakTimeSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanPemAutoinserviceSoakTimeSec.setStatus("current")
_CyanPemBaseMacAddress_Type = DisplayString
_CyanPemBaseMacAddress_Object = MibTableColumn
cyanPemBaseMacAddress = _CyanPemBaseMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 30, 1, 1, 1, 6),
    _CyanPemBaseMacAddress_Type()
)
cyanPemBaseMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanPemBaseMacAddress.setStatus("current")


class _CyanPemDescription_Type(DisplayString):
    """Custom type cyanPemDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CyanPemDescription_Type.__name__ = "DisplayString"
_CyanPemDescription_Object = MibTableColumn
cyanPemDescription = _CyanPemDescription_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 30, 1, 1, 1, 7),
    _CyanPemDescription_Type()
)
cyanPemDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanPemDescription.setStatus("current")
_CyanPemIdentifier_Type = DisplayString
_CyanPemIdentifier_Object = MibTableColumn
cyanPemIdentifier = _CyanPemIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 30, 1, 1, 1, 8),
    _CyanPemIdentifier_Type()
)
cyanPemIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanPemIdentifier.setStatus("current")


class _CyanPemMacBlockSize_Type(Unsigned32):
    """Custom type cyanPemMacBlockSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CyanPemMacBlockSize_Type.__name__ = "Unsigned32"
_CyanPemMacBlockSize_Object = MibTableColumn
cyanPemMacBlockSize = _CyanPemMacBlockSize_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 30, 1, 1, 1, 9),
    _CyanPemMacBlockSize_Type()
)
cyanPemMacBlockSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanPemMacBlockSize.setStatus("current")


class _CyanPemMfgCleiCode_Type(DisplayString):
    """Custom type cyanPemMfgCleiCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_CyanPemMfgCleiCode_Type.__name__ = "DisplayString"
_CyanPemMfgCleiCode_Object = MibTableColumn
cyanPemMfgCleiCode = _CyanPemMfgCleiCode_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 30, 1, 1, 1, 10),
    _CyanPemMfgCleiCode_Type()
)
cyanPemMfgCleiCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanPemMfgCleiCode.setStatus("current")


class _CyanPemMfgEciCode_Type(DisplayString):
    """Custom type cyanPemMfgEciCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_CyanPemMfgEciCode_Type.__name__ = "DisplayString"
_CyanPemMfgEciCode_Object = MibTableColumn
cyanPemMfgEciCode = _CyanPemMfgEciCode_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 30, 1, 1, 1, 11),
    _CyanPemMfgEciCode_Type()
)
cyanPemMfgEciCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanPemMfgEciCode.setStatus("current")
_CyanPemMfgModuleId_Type = Unsigned32
_CyanPemMfgModuleId_Object = MibTableColumn
cyanPemMfgModuleId = _CyanPemMfgModuleId_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 30, 1, 1, 1, 12),
    _CyanPemMfgModuleId_Type()
)
cyanPemMfgModuleId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanPemMfgModuleId.setStatus("current")


class _CyanPemMfgPartNumber_Type(DisplayString):
    """Custom type cyanPemMfgPartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CyanPemMfgPartNumber_Type.__name__ = "DisplayString"
_CyanPemMfgPartNumber_Object = MibTableColumn
cyanPemMfgPartNumber = _CyanPemMfgPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 30, 1, 1, 1, 13),
    _CyanPemMfgPartNumber_Type()
)
cyanPemMfgPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanPemMfgPartNumber.setStatus("current")


class _CyanPemMfgRevision_Type(DisplayString):
    """Custom type cyanPemMfgRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_CyanPemMfgRevision_Type.__name__ = "DisplayString"
_CyanPemMfgRevision_Object = MibTableColumn
cyanPemMfgRevision = _CyanPemMfgRevision_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 30, 1, 1, 1, 14),
    _CyanPemMfgRevision_Type()
)
cyanPemMfgRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanPemMfgRevision.setStatus("current")


class _CyanPemMfgSerialNumber_Type(DisplayString):
    """Custom type cyanPemMfgSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CyanPemMfgSerialNumber_Type.__name__ = "DisplayString"
_CyanPemMfgSerialNumber_Object = MibTableColumn
cyanPemMfgSerialNumber = _CyanPemMfgSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 30, 1, 1, 1, 15),
    _CyanPemMfgSerialNumber_Type()
)
cyanPemMfgSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanPemMfgSerialNumber.setStatus("current")
_CyanPemName_Type = DisplayString
_CyanPemName_Object = MibTableColumn
cyanPemName = _CyanPemName_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 30, 1, 1, 1, 16),
    _CyanPemName_Type()
)
cyanPemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanPemName.setStatus("current")
_CyanPemOidClass_Type = DisplayString
_CyanPemOidClass_Object = MibTableColumn
cyanPemOidClass = _CyanPemOidClass_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 30, 1, 1, 1, 17),
    _CyanPemOidClass_Type()
)
cyanPemOidClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanPemOidClass.setStatus("current")
_CyanPemOperState_Type = CyanOpStateTc
_CyanPemOperState_Object = MibTableColumn
cyanPemOperState = _CyanPemOperState_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 30, 1, 1, 1, 18),
    _CyanPemOperState_Type()
)
cyanPemOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanPemOperState.setStatus("current")
_CyanPemOperStateQual_Type = CyanOpStateQualTc
_CyanPemOperStateQual_Object = MibTableColumn
cyanPemOperStateQual = _CyanPemOperStateQual_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 30, 1, 1, 1, 19),
    _CyanPemOperStateQual_Type()
)
cyanPemOperStateQual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanPemOperStateQual.setStatus("current")


class _CyanPemOssLabel_Type(DisplayString):
    """Custom type cyanPemOssLabel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_CyanPemOssLabel_Type.__name__ = "DisplayString"
_CyanPemOssLabel_Object = MibTableColumn
cyanPemOssLabel = _CyanPemOssLabel_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 30, 1, 1, 1, 20),
    _CyanPemOssLabel_Type()
)
cyanPemOssLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanPemOssLabel.setStatus("current")


class _CyanPemOwner_Type(DisplayString):
    """Custom type cyanPemOwner based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_CyanPemOwner_Type.__name__ = "DisplayString"
_CyanPemOwner_Object = MibTableColumn
cyanPemOwner = _CyanPemOwner_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 30, 1, 1, 1, 21),
    _CyanPemOwner_Type()
)
cyanPemOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanPemOwner.setStatus("current")


class _CyanPemPartNumber_Type(DisplayString):
    """Custom type cyanPemPartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 11),
    )


_CyanPemPartNumber_Type.__name__ = "DisplayString"
_CyanPemPartNumber_Object = MibTableColumn
cyanPemPartNumber = _CyanPemPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 30, 1, 1, 1, 22),
    _CyanPemPartNumber_Type()
)
cyanPemPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanPemPartNumber.setStatus("current")
_CyanPemSecServState_Type = CyanSecServiceStateTc
_CyanPemSecServState_Object = MibTableColumn
cyanPemSecServState = _CyanPemSecServState_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 30, 1, 1, 1, 23),
    _CyanPemSecServState_Type()
)
cyanPemSecServState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanPemSecServState.setStatus("current")
_CyanPemType_Type = CyanTypeTc
_CyanPemType_Object = MibTableColumn
cyanPemType = _CyanPemType_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 30, 1, 1, 1, 24),
    _CyanPemType_Type()
)
cyanPemType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanPemType.setStatus("current")

# Managed Objects groups

cyanPemObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 30, 20)
)
cyanPemObjectGroup.setObjects(
      *(("CYAN-PEM-MIB", "cyanPemAdminState"),
        ("CYAN-PEM-MIB", "cyanPemAssetTag"),
        ("CYAN-PEM-MIB", "cyanPemAutoinserviceSoakTimeSec"),
        ("CYAN-PEM-MIB", "cyanPemBaseMacAddress"),
        ("CYAN-PEM-MIB", "cyanPemDescription"),
        ("CYAN-PEM-MIB", "cyanPemIdentifier"),
        ("CYAN-PEM-MIB", "cyanPemMacBlockSize"),
        ("CYAN-PEM-MIB", "cyanPemMfgCleiCode"),
        ("CYAN-PEM-MIB", "cyanPemMfgEciCode"),
        ("CYAN-PEM-MIB", "cyanPemMfgModuleId"),
        ("CYAN-PEM-MIB", "cyanPemMfgPartNumber"),
        ("CYAN-PEM-MIB", "cyanPemMfgRevision"),
        ("CYAN-PEM-MIB", "cyanPemMfgSerialNumber"),
        ("CYAN-PEM-MIB", "cyanPemName"),
        ("CYAN-PEM-MIB", "cyanPemOidClass"),
        ("CYAN-PEM-MIB", "cyanPemOperState"),
        ("CYAN-PEM-MIB", "cyanPemOperStateQual"),
        ("CYAN-PEM-MIB", "cyanPemOssLabel"),
        ("CYAN-PEM-MIB", "cyanPemOwner"),
        ("CYAN-PEM-MIB", "cyanPemPartNumber"),
        ("CYAN-PEM-MIB", "cyanPemSecServState"),
        ("CYAN-PEM-MIB", "cyanPemType"))
)
if mibBuilder.loadTexts:
    cyanPemObjectGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cyanPemCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 30, 30)
)
if mibBuilder.loadTexts:
    cyanPemCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CYAN-PEM-MIB",
    **{"cyanPemModule": cyanPemModule,
       "cyanPemMibObjects": cyanPemMibObjects,
       "cyanPemTable": cyanPemTable,
       "cyanPemEntry": cyanPemEntry,
       "cyanPemShelfId": cyanPemShelfId,
       "cyanPemPemId": cyanPemPemId,
       "cyanPemAdminState": cyanPemAdminState,
       "cyanPemAssetTag": cyanPemAssetTag,
       "cyanPemAutoinserviceSoakTimeSec": cyanPemAutoinserviceSoakTimeSec,
       "cyanPemBaseMacAddress": cyanPemBaseMacAddress,
       "cyanPemDescription": cyanPemDescription,
       "cyanPemIdentifier": cyanPemIdentifier,
       "cyanPemMacBlockSize": cyanPemMacBlockSize,
       "cyanPemMfgCleiCode": cyanPemMfgCleiCode,
       "cyanPemMfgEciCode": cyanPemMfgEciCode,
       "cyanPemMfgModuleId": cyanPemMfgModuleId,
       "cyanPemMfgPartNumber": cyanPemMfgPartNumber,
       "cyanPemMfgRevision": cyanPemMfgRevision,
       "cyanPemMfgSerialNumber": cyanPemMfgSerialNumber,
       "cyanPemName": cyanPemName,
       "cyanPemOidClass": cyanPemOidClass,
       "cyanPemOperState": cyanPemOperState,
       "cyanPemOperStateQual": cyanPemOperStateQual,
       "cyanPemOssLabel": cyanPemOssLabel,
       "cyanPemOwner": cyanPemOwner,
       "cyanPemPartNumber": cyanPemPartNumber,
       "cyanPemSecServState": cyanPemSecServState,
       "cyanPemType": cyanPemType,
       "cyanPemObjectGroup": cyanPemObjectGroup,
       "cyanPemCompliance": cyanPemCompliance}
)
