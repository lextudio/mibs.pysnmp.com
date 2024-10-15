# SNMP MIB module (CYAN-XCVR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CYAN-XCVR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:21:19 2024
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

(cyanEntityModules,) = mibBuilder.importSymbols(
    "CYAN-MIB",
    "cyanEntityModules")

(CyanAdminStateTc,
 CyanNoYesTc,
 CyanOpStateQualTc,
 CyanOpStateTc,
 CyanPowerClassTc,
 CyanSecServiceStateTc,
 CyanWdmTypeTc,
 CyanXcvrConnectorCodeTc,
 CyanXcvrIdentifierTc) = mibBuilder.importSymbols(
    "CYAN-TC-MIB",
    "CyanAdminStateTc",
    "CyanNoYesTc",
    "CyanOpStateQualTc",
    "CyanOpStateTc",
    "CyanPowerClassTc",
    "CyanSecServiceStateTc",
    "CyanWdmTypeTc",
    "CyanXcvrConnectorCodeTc",
    "CyanXcvrIdentifierTc")

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

cyanXcvrModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 140)
)
cyanXcvrModule.setRevisions(
        ("2014-12-07 05:45",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CyanXcvrMibObjects_ObjectIdentity = ObjectIdentity
cyanXcvrMibObjects = _CyanXcvrMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 140, 1)
)
_CyanXcvrTable_Object = MibTable
cyanXcvrTable = _CyanXcvrTable_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 140, 1, 1)
)
if mibBuilder.loadTexts:
    cyanXcvrTable.setStatus("current")
_CyanXcvrEntry_Object = MibTableRow
cyanXcvrEntry = _CyanXcvrEntry_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 140, 1, 1, 1)
)
cyanXcvrEntry.setIndexNames(
    (0, "CYAN-XCVR-MIB", "cyanXcvrShelfId"),
    (0, "CYAN-XCVR-MIB", "cyanXcvrModuleId"),
    (0, "CYAN-XCVR-MIB", "cyanXcvrXcvrId"),
)
if mibBuilder.loadTexts:
    cyanXcvrEntry.setStatus("current")


class _CyanXcvrShelfId_Type(Unsigned32):
    """Custom type cyanXcvrShelfId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CyanXcvrShelfId_Type.__name__ = "Unsigned32"
_CyanXcvrShelfId_Object = MibTableColumn
cyanXcvrShelfId = _CyanXcvrShelfId_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 140, 1, 1, 1, 1),
    _CyanXcvrShelfId_Type()
)
cyanXcvrShelfId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cyanXcvrShelfId.setStatus("current")
_CyanXcvrModuleId_Type = Unsigned32
_CyanXcvrModuleId_Object = MibTableColumn
cyanXcvrModuleId = _CyanXcvrModuleId_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 140, 1, 1, 1, 2),
    _CyanXcvrModuleId_Type()
)
cyanXcvrModuleId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cyanXcvrModuleId.setStatus("current")
_CyanXcvrXcvrId_Type = Unsigned32
_CyanXcvrXcvrId_Object = MibTableColumn
cyanXcvrXcvrId = _CyanXcvrXcvrId_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 140, 1, 1, 1, 3),
    _CyanXcvrXcvrId_Type()
)
cyanXcvrXcvrId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cyanXcvrXcvrId.setStatus("current")
_CyanXcvrAdminState_Type = CyanAdminStateTc
_CyanXcvrAdminState_Object = MibTableColumn
cyanXcvrAdminState = _CyanXcvrAdminState_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 140, 1, 1, 1, 4),
    _CyanXcvrAdminState_Type()
)
cyanXcvrAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanXcvrAdminState.setStatus("current")
_CyanXcvrAutoinserviceSoakTimeSec_Type = Integer32
_CyanXcvrAutoinserviceSoakTimeSec_Object = MibTableColumn
cyanXcvrAutoinserviceSoakTimeSec = _CyanXcvrAutoinserviceSoakTimeSec_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 140, 1, 1, 1, 5),
    _CyanXcvrAutoinserviceSoakTimeSec_Type()
)
cyanXcvrAutoinserviceSoakTimeSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanXcvrAutoinserviceSoakTimeSec.setStatus("current")
_CyanXcvrComplianceCode_Type = Counter64
_CyanXcvrComplianceCode_Object = MibTableColumn
cyanXcvrComplianceCode = _CyanXcvrComplianceCode_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 140, 1, 1, 1, 6),
    _CyanXcvrComplianceCode_Type()
)
cyanXcvrComplianceCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanXcvrComplianceCode.setStatus("current")
_CyanXcvrConnectorCode_Type = CyanXcvrConnectorCodeTc
_CyanXcvrConnectorCode_Object = MibTableColumn
cyanXcvrConnectorCode = _CyanXcvrConnectorCode_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 140, 1, 1, 1, 7),
    _CyanXcvrConnectorCode_Type()
)
cyanXcvrConnectorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanXcvrConnectorCode.setStatus("current")


class _CyanXcvrCyanName_Type(DisplayString):
    """Custom type cyanXcvrCyanName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CyanXcvrCyanName_Type.__name__ = "DisplayString"
_CyanXcvrCyanName_Object = MibTableColumn
cyanXcvrCyanName = _CyanXcvrCyanName_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 140, 1, 1, 1, 8),
    _CyanXcvrCyanName_Type()
)
cyanXcvrCyanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanXcvrCyanName.setStatus("current")


class _CyanXcvrCyanPartNumber_Type(DisplayString):
    """Custom type cyanXcvrCyanPartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 42),
    )


_CyanXcvrCyanPartNumber_Type.__name__ = "DisplayString"
_CyanXcvrCyanPartNumber_Object = MibTableColumn
cyanXcvrCyanPartNumber = _CyanXcvrCyanPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 140, 1, 1, 1, 9),
    _CyanXcvrCyanPartNumber_Type()
)
cyanXcvrCyanPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanXcvrCyanPartNumber.setStatus("current")


class _CyanXcvrDescription_Type(DisplayString):
    """Custom type cyanXcvrDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CyanXcvrDescription_Type.__name__ = "DisplayString"
_CyanXcvrDescription_Object = MibTableColumn
cyanXcvrDescription = _CyanXcvrDescription_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 140, 1, 1, 1, 10),
    _CyanXcvrDescription_Type()
)
cyanXcvrDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanXcvrDescription.setStatus("current")
_CyanXcvrIdentifier_Type = DisplayString
_CyanXcvrIdentifier_Object = MibTableColumn
cyanXcvrIdentifier = _CyanXcvrIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 140, 1, 1, 1, 11),
    _CyanXcvrIdentifier_Type()
)
cyanXcvrIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanXcvrIdentifier.setStatus("current")
_CyanXcvrIdentifierCode_Type = CyanXcvrIdentifierTc
_CyanXcvrIdentifierCode_Object = MibTableColumn
cyanXcvrIdentifierCode = _CyanXcvrIdentifierCode_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 140, 1, 1, 1, 12),
    _CyanXcvrIdentifierCode_Type()
)
cyanXcvrIdentifierCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanXcvrIdentifierCode.setStatus("current")
_CyanXcvrLength9_Type = Unsigned32
_CyanXcvrLength9_Object = MibTableColumn
cyanXcvrLength9 = _CyanXcvrLength9_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 140, 1, 1, 1, 13),
    _CyanXcvrLength9_Type()
)
cyanXcvrLength9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanXcvrLength9.setStatus("current")
_CyanXcvrMaxBitRate_Type = Unsigned32
_CyanXcvrMaxBitRate_Object = MibTableColumn
cyanXcvrMaxBitRate = _CyanXcvrMaxBitRate_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 140, 1, 1, 1, 14),
    _CyanXcvrMaxBitRate_Type()
)
cyanXcvrMaxBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanXcvrMaxBitRate.setStatus("current")
_CyanXcvrMfgDateCode_Type = DisplayString
_CyanXcvrMfgDateCode_Object = MibTableColumn
cyanXcvrMfgDateCode = _CyanXcvrMfgDateCode_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 140, 1, 1, 1, 15),
    _CyanXcvrMfgDateCode_Type()
)
cyanXcvrMfgDateCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanXcvrMfgDateCode.setStatus("current")
_CyanXcvrMinBitRate_Type = Unsigned32
_CyanXcvrMinBitRate_Object = MibTableColumn
cyanXcvrMinBitRate = _CyanXcvrMinBitRate_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 140, 1, 1, 1, 16),
    _CyanXcvrMinBitRate_Type()
)
cyanXcvrMinBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanXcvrMinBitRate.setStatus("current")


class _CyanXcvrMmf3Maxlen_Type(Unsigned32):
    """Custom type cyanXcvrMmf3Maxlen based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CyanXcvrMmf3Maxlen_Type.__name__ = "Unsigned32"
_CyanXcvrMmf3Maxlen_Object = MibTableColumn
cyanXcvrMmf3Maxlen = _CyanXcvrMmf3Maxlen_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 140, 1, 1, 1, 17),
    _CyanXcvrMmf3Maxlen_Type()
)
cyanXcvrMmf3Maxlen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanXcvrMmf3Maxlen.setStatus("current")


class _CyanXcvrMmf4Maxlen_Type(Unsigned32):
    """Custom type cyanXcvrMmf4Maxlen based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CyanXcvrMmf4Maxlen_Type.__name__ = "Unsigned32"
_CyanXcvrMmf4Maxlen_Object = MibTableColumn
cyanXcvrMmf4Maxlen = _CyanXcvrMmf4Maxlen_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 140, 1, 1, 1, 18),
    _CyanXcvrMmf4Maxlen_Type()
)
cyanXcvrMmf4Maxlen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanXcvrMmf4Maxlen.setStatus("current")
_CyanXcvrName_Type = DisplayString
_CyanXcvrName_Object = MibTableColumn
cyanXcvrName = _CyanXcvrName_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 140, 1, 1, 1, 19),
    _CyanXcvrName_Type()
)
cyanXcvrName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanXcvrName.setStatus("current")
_CyanXcvrNominalBitRate_Type = Unsigned32
_CyanXcvrNominalBitRate_Object = MibTableColumn
cyanXcvrNominalBitRate = _CyanXcvrNominalBitRate_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 140, 1, 1, 1, 20),
    _CyanXcvrNominalBitRate_Type()
)
cyanXcvrNominalBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanXcvrNominalBitRate.setStatus("current")
_CyanXcvrOidClass_Type = DisplayString
_CyanXcvrOidClass_Object = MibTableColumn
cyanXcvrOidClass = _CyanXcvrOidClass_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 140, 1, 1, 1, 21),
    _CyanXcvrOidClass_Type()
)
cyanXcvrOidClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanXcvrOidClass.setStatus("current")
_CyanXcvrOperState_Type = CyanOpStateTc
_CyanXcvrOperState_Object = MibTableColumn
cyanXcvrOperState = _CyanXcvrOperState_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 140, 1, 1, 1, 22),
    _CyanXcvrOperState_Type()
)
cyanXcvrOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanXcvrOperState.setStatus("current")
_CyanXcvrOperStateQual_Type = CyanOpStateQualTc
_CyanXcvrOperStateQual_Object = MibTableColumn
cyanXcvrOperStateQual = _CyanXcvrOperStateQual_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 140, 1, 1, 1, 23),
    _CyanXcvrOperStateQual_Type()
)
cyanXcvrOperStateQual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanXcvrOperStateQual.setStatus("current")
_CyanXcvrOptSensitivityAdjustSupp_Type = CyanNoYesTc
_CyanXcvrOptSensitivityAdjustSupp_Object = MibTableColumn
cyanXcvrOptSensitivityAdjustSupp = _CyanXcvrOptSensitivityAdjustSupp_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 140, 1, 1, 1, 24),
    _CyanXcvrOptSensitivityAdjustSupp_Type()
)
cyanXcvrOptSensitivityAdjustSupp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanXcvrOptSensitivityAdjustSupp.setStatus("current")


class _CyanXcvrOssLabel_Type(DisplayString):
    """Custom type cyanXcvrOssLabel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_CyanXcvrOssLabel_Type.__name__ = "DisplayString"
_CyanXcvrOssLabel_Object = MibTableColumn
cyanXcvrOssLabel = _CyanXcvrOssLabel_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 140, 1, 1, 1, 25),
    _CyanXcvrOssLabel_Type()
)
cyanXcvrOssLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanXcvrOssLabel.setStatus("current")
_CyanXcvrOuiCode_Type = Integer32
_CyanXcvrOuiCode_Object = MibTableColumn
cyanXcvrOuiCode = _CyanXcvrOuiCode_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 140, 1, 1, 1, 26),
    _CyanXcvrOuiCode_Type()
)
cyanXcvrOuiCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanXcvrOuiCode.setStatus("current")


class _CyanXcvrOwner_Type(DisplayString):
    """Custom type cyanXcvrOwner based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_CyanXcvrOwner_Type.__name__ = "DisplayString"
_CyanXcvrOwner_Object = MibTableColumn
cyanXcvrOwner = _CyanXcvrOwner_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 140, 1, 1, 1, 27),
    _CyanXcvrOwner_Type()
)
cyanXcvrOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanXcvrOwner.setStatus("current")
_CyanXcvrPartNumber_Type = DisplayString
_CyanXcvrPartNumber_Object = MibTableColumn
cyanXcvrPartNumber = _CyanXcvrPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 140, 1, 1, 1, 28),
    _CyanXcvrPartNumber_Type()
)
cyanXcvrPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanXcvrPartNumber.setStatus("current")
_CyanXcvrPowerClass_Type = CyanPowerClassTc
_CyanXcvrPowerClass_Object = MibTableColumn
cyanXcvrPowerClass = _CyanXcvrPowerClass_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 140, 1, 1, 1, 29),
    _CyanXcvrPowerClass_Type()
)
cyanXcvrPowerClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanXcvrPowerClass.setStatus("current")
_CyanXcvrRealTimeDiagImplemented_Type = CyanNoYesTc
_CyanXcvrRealTimeDiagImplemented_Object = MibTableColumn
cyanXcvrRealTimeDiagImplemented = _CyanXcvrRealTimeDiagImplemented_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 140, 1, 1, 1, 30),
    _CyanXcvrRealTimeDiagImplemented_Type()
)
cyanXcvrRealTimeDiagImplemented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanXcvrRealTimeDiagImplemented.setStatus("current")


class _CyanXcvrRxPwrHiAlrmThres_Type(Integer32):
    """Custom type cyanXcvrRxPwrHiAlrmThres based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128000, 128000),
    )


_CyanXcvrRxPwrHiAlrmThres_Type.__name__ = "Integer32"
_CyanXcvrRxPwrHiAlrmThres_Object = MibTableColumn
cyanXcvrRxPwrHiAlrmThres = _CyanXcvrRxPwrHiAlrmThres_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 140, 1, 1, 1, 31),
    _CyanXcvrRxPwrHiAlrmThres_Type()
)
cyanXcvrRxPwrHiAlrmThres.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanXcvrRxPwrHiAlrmThres.setStatus("current")


class _CyanXcvrRxPwrHiWarnThres_Type(Integer32):
    """Custom type cyanXcvrRxPwrHiWarnThres based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128000, 128000),
    )


_CyanXcvrRxPwrHiWarnThres_Type.__name__ = "Integer32"
_CyanXcvrRxPwrHiWarnThres_Object = MibTableColumn
cyanXcvrRxPwrHiWarnThres = _CyanXcvrRxPwrHiWarnThres_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 140, 1, 1, 1, 32),
    _CyanXcvrRxPwrHiWarnThres_Type()
)
cyanXcvrRxPwrHiWarnThres.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanXcvrRxPwrHiWarnThres.setStatus("current")


class _CyanXcvrRxPwrLoAlrmThres_Type(Integer32):
    """Custom type cyanXcvrRxPwrLoAlrmThres based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128000, 128000),
    )


_CyanXcvrRxPwrLoAlrmThres_Type.__name__ = "Integer32"
_CyanXcvrRxPwrLoAlrmThres_Object = MibTableColumn
cyanXcvrRxPwrLoAlrmThres = _CyanXcvrRxPwrLoAlrmThres_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 140, 1, 1, 1, 33),
    _CyanXcvrRxPwrLoAlrmThres_Type()
)
cyanXcvrRxPwrLoAlrmThres.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanXcvrRxPwrLoAlrmThres.setStatus("current")


class _CyanXcvrRxPwrLoWarnThres_Type(Integer32):
    """Custom type cyanXcvrRxPwrLoWarnThres based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128000, 128000),
    )


_CyanXcvrRxPwrLoWarnThres_Type.__name__ = "Integer32"
_CyanXcvrRxPwrLoWarnThres_Object = MibTableColumn
cyanXcvrRxPwrLoWarnThres = _CyanXcvrRxPwrLoWarnThres_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 140, 1, 1, 1, 34),
    _CyanXcvrRxPwrLoWarnThres_Type()
)
cyanXcvrRxPwrLoWarnThres.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanXcvrRxPwrLoWarnThres.setStatus("current")
_CyanXcvrSecServState_Type = CyanSecServiceStateTc
_CyanXcvrSecServState_Object = MibTableColumn
cyanXcvrSecServState = _CyanXcvrSecServState_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 140, 1, 1, 1, 35),
    _CyanXcvrSecServState_Type()
)
cyanXcvrSecServState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanXcvrSecServState.setStatus("current")
_CyanXcvrSerialNumber_Type = DisplayString
_CyanXcvrSerialNumber_Object = MibTableColumn
cyanXcvrSerialNumber = _CyanXcvrSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 140, 1, 1, 1, 36),
    _CyanXcvrSerialNumber_Type()
)
cyanXcvrSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanXcvrSerialNumber.setStatus("current")
_CyanXcvrSfpOptions_Type = Unsigned32
_CyanXcvrSfpOptions_Object = MibTableColumn
cyanXcvrSfpOptions = _CyanXcvrSfpOptions_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 140, 1, 1, 1, 37),
    _CyanXcvrSfpOptions_Type()
)
cyanXcvrSfpOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanXcvrSfpOptions.setStatus("current")


class _CyanXcvrTempHiAlrmThres_Type(Integer32):
    """Custom type cyanXcvrTempHiAlrmThres based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128000, 128000),
    )


_CyanXcvrTempHiAlrmThres_Type.__name__ = "Integer32"
_CyanXcvrTempHiAlrmThres_Object = MibTableColumn
cyanXcvrTempHiAlrmThres = _CyanXcvrTempHiAlrmThres_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 140, 1, 1, 1, 38),
    _CyanXcvrTempHiAlrmThres_Type()
)
cyanXcvrTempHiAlrmThres.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanXcvrTempHiAlrmThres.setStatus("current")


class _CyanXcvrTempHiWarnThres_Type(Integer32):
    """Custom type cyanXcvrTempHiWarnThres based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128000, 128000),
    )


_CyanXcvrTempHiWarnThres_Type.__name__ = "Integer32"
_CyanXcvrTempHiWarnThres_Object = MibTableColumn
cyanXcvrTempHiWarnThres = _CyanXcvrTempHiWarnThres_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 140, 1, 1, 1, 39),
    _CyanXcvrTempHiWarnThres_Type()
)
cyanXcvrTempHiWarnThres.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanXcvrTempHiWarnThres.setStatus("current")


class _CyanXcvrTempLoAlrmThres_Type(Integer32):
    """Custom type cyanXcvrTempLoAlrmThres based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128000, 128000),
    )


_CyanXcvrTempLoAlrmThres_Type.__name__ = "Integer32"
_CyanXcvrTempLoAlrmThres_Object = MibTableColumn
cyanXcvrTempLoAlrmThres = _CyanXcvrTempLoAlrmThres_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 140, 1, 1, 1, 40),
    _CyanXcvrTempLoAlrmThres_Type()
)
cyanXcvrTempLoAlrmThres.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanXcvrTempLoAlrmThres.setStatus("current")


class _CyanXcvrTempLoWarnThres_Type(Integer32):
    """Custom type cyanXcvrTempLoWarnThres based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128000, 128000),
    )


_CyanXcvrTempLoWarnThres_Type.__name__ = "Integer32"
_CyanXcvrTempLoWarnThres_Object = MibTableColumn
cyanXcvrTempLoWarnThres = _CyanXcvrTempLoWarnThres_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 140, 1, 1, 1, 41),
    _CyanXcvrTempLoWarnThres_Type()
)
cyanXcvrTempLoWarnThres.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanXcvrTempLoWarnThres.setStatus("current")
_CyanXcvrTemperature_Type = Integer32
_CyanXcvrTemperature_Object = MibTableColumn
cyanXcvrTemperature = _CyanXcvrTemperature_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 140, 1, 1, 1, 42),
    _CyanXcvrTemperature_Type()
)
cyanXcvrTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanXcvrTemperature.setStatus("current")
_CyanXcvrTxBiasCurrent_Type = Integer32
_CyanXcvrTxBiasCurrent_Object = MibTableColumn
cyanXcvrTxBiasCurrent = _CyanXcvrTxBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 140, 1, 1, 1, 43),
    _CyanXcvrTxBiasCurrent_Type()
)
cyanXcvrTxBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanXcvrTxBiasCurrent.setStatus("current")
_CyanXcvrTxBiasHiAlrmThres_Type = Integer32
_CyanXcvrTxBiasHiAlrmThres_Object = MibTableColumn
cyanXcvrTxBiasHiAlrmThres = _CyanXcvrTxBiasHiAlrmThres_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 140, 1, 1, 1, 44),
    _CyanXcvrTxBiasHiAlrmThres_Type()
)
cyanXcvrTxBiasHiAlrmThres.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanXcvrTxBiasHiAlrmThres.setStatus("current")
_CyanXcvrTxBiasHiWarnThres_Type = Integer32
_CyanXcvrTxBiasHiWarnThres_Object = MibTableColumn
cyanXcvrTxBiasHiWarnThres = _CyanXcvrTxBiasHiWarnThres_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 140, 1, 1, 1, 45),
    _CyanXcvrTxBiasHiWarnThres_Type()
)
cyanXcvrTxBiasHiWarnThres.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanXcvrTxBiasHiWarnThres.setStatus("current")
_CyanXcvrTxBiasLoAlrmThres_Type = Integer32
_CyanXcvrTxBiasLoAlrmThres_Object = MibTableColumn
cyanXcvrTxBiasLoAlrmThres = _CyanXcvrTxBiasLoAlrmThres_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 140, 1, 1, 1, 46),
    _CyanXcvrTxBiasLoAlrmThres_Type()
)
cyanXcvrTxBiasLoAlrmThres.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanXcvrTxBiasLoAlrmThres.setStatus("current")
_CyanXcvrTxBiasLoWarnThres_Type = Integer32
_CyanXcvrTxBiasLoWarnThres_Object = MibTableColumn
cyanXcvrTxBiasLoWarnThres = _CyanXcvrTxBiasLoWarnThres_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 140, 1, 1, 1, 47),
    _CyanXcvrTxBiasLoWarnThres_Type()
)
cyanXcvrTxBiasLoWarnThres.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanXcvrTxBiasLoWarnThres.setStatus("current")


class _CyanXcvrTxPwrHiAlrmThres_Type(Integer32):
    """Custom type cyanXcvrTxPwrHiAlrmThres based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128000, 128000),
    )


_CyanXcvrTxPwrHiAlrmThres_Type.__name__ = "Integer32"
_CyanXcvrTxPwrHiAlrmThres_Object = MibTableColumn
cyanXcvrTxPwrHiAlrmThres = _CyanXcvrTxPwrHiAlrmThres_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 140, 1, 1, 1, 48),
    _CyanXcvrTxPwrHiAlrmThres_Type()
)
cyanXcvrTxPwrHiAlrmThres.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanXcvrTxPwrHiAlrmThres.setStatus("current")


class _CyanXcvrTxPwrHiWarnThres_Type(Integer32):
    """Custom type cyanXcvrTxPwrHiWarnThres based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128000, 128000),
    )


_CyanXcvrTxPwrHiWarnThres_Type.__name__ = "Integer32"
_CyanXcvrTxPwrHiWarnThres_Object = MibTableColumn
cyanXcvrTxPwrHiWarnThres = _CyanXcvrTxPwrHiWarnThres_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 140, 1, 1, 1, 49),
    _CyanXcvrTxPwrHiWarnThres_Type()
)
cyanXcvrTxPwrHiWarnThres.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanXcvrTxPwrHiWarnThres.setStatus("current")


class _CyanXcvrTxPwrLoAlrmThres_Type(Integer32):
    """Custom type cyanXcvrTxPwrLoAlrmThres based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128000, 128000),
    )


_CyanXcvrTxPwrLoAlrmThres_Type.__name__ = "Integer32"
_CyanXcvrTxPwrLoAlrmThres_Object = MibTableColumn
cyanXcvrTxPwrLoAlrmThres = _CyanXcvrTxPwrLoAlrmThres_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 140, 1, 1, 1, 50),
    _CyanXcvrTxPwrLoAlrmThres_Type()
)
cyanXcvrTxPwrLoAlrmThres.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanXcvrTxPwrLoAlrmThres.setStatus("current")


class _CyanXcvrTxPwrLoWarnThres_Type(Integer32):
    """Custom type cyanXcvrTxPwrLoWarnThres based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128000, 128000),
    )


_CyanXcvrTxPwrLoWarnThres_Type.__name__ = "Integer32"
_CyanXcvrTxPwrLoWarnThres_Object = MibTableColumn
cyanXcvrTxPwrLoWarnThres = _CyanXcvrTxPwrLoWarnThres_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 140, 1, 1, 1, 51),
    _CyanXcvrTxPwrLoWarnThres_Type()
)
cyanXcvrTxPwrLoWarnThres.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanXcvrTxPwrLoWarnThres.setStatus("current")
_CyanXcvrVccVoltHiAlrmThres_Type = Integer32
_CyanXcvrVccVoltHiAlrmThres_Object = MibTableColumn
cyanXcvrVccVoltHiAlrmThres = _CyanXcvrVccVoltHiAlrmThres_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 140, 1, 1, 1, 52),
    _CyanXcvrVccVoltHiAlrmThres_Type()
)
cyanXcvrVccVoltHiAlrmThres.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanXcvrVccVoltHiAlrmThres.setStatus("current")
_CyanXcvrVccVoltHiWarnThres_Type = Integer32
_CyanXcvrVccVoltHiWarnThres_Object = MibTableColumn
cyanXcvrVccVoltHiWarnThres = _CyanXcvrVccVoltHiWarnThres_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 140, 1, 1, 1, 53),
    _CyanXcvrVccVoltHiWarnThres_Type()
)
cyanXcvrVccVoltHiWarnThres.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanXcvrVccVoltHiWarnThres.setStatus("current")
_CyanXcvrVccVoltLoAlrmThres_Type = Integer32
_CyanXcvrVccVoltLoAlrmThres_Object = MibTableColumn
cyanXcvrVccVoltLoAlrmThres = _CyanXcvrVccVoltLoAlrmThres_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 140, 1, 1, 1, 54),
    _CyanXcvrVccVoltLoAlrmThres_Type()
)
cyanXcvrVccVoltLoAlrmThres.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanXcvrVccVoltLoAlrmThres.setStatus("current")
_CyanXcvrVccVoltLoWarnThres_Type = Integer32
_CyanXcvrVccVoltLoWarnThres_Object = MibTableColumn
cyanXcvrVccVoltLoWarnThres = _CyanXcvrVccVoltLoWarnThres_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 140, 1, 1, 1, 55),
    _CyanXcvrVccVoltLoWarnThres_Type()
)
cyanXcvrVccVoltLoWarnThres.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanXcvrVccVoltLoWarnThres.setStatus("current")
_CyanXcvrVccVoltage_Type = Integer32
_CyanXcvrVccVoltage_Object = MibTableColumn
cyanXcvrVccVoltage = _CyanXcvrVccVoltage_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 140, 1, 1, 1, 56),
    _CyanXcvrVccVoltage_Type()
)
cyanXcvrVccVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanXcvrVccVoltage.setStatus("current")


class _CyanXcvrVendorName_Type(DisplayString):
    """Custom type cyanXcvrVendorName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CyanXcvrVendorName_Type.__name__ = "DisplayString"
_CyanXcvrVendorName_Object = MibTableColumn
cyanXcvrVendorName = _CyanXcvrVendorName_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 140, 1, 1, 1, 57),
    _CyanXcvrVendorName_Type()
)
cyanXcvrVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanXcvrVendorName.setStatus("current")


class _CyanXcvrVendorRev_Type(DisplayString):
    """Custom type cyanXcvrVendorRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_CyanXcvrVendorRev_Type.__name__ = "DisplayString"
_CyanXcvrVendorRev_Object = MibTableColumn
cyanXcvrVendorRev = _CyanXcvrVendorRev_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 140, 1, 1, 1, 58),
    _CyanXcvrVendorRev_Type()
)
cyanXcvrVendorRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanXcvrVendorRev.setStatus("current")
_CyanXcvrWavelength_Type = Integer32
_CyanXcvrWavelength_Object = MibTableColumn
cyanXcvrWavelength = _CyanXcvrWavelength_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 140, 1, 1, 1, 59),
    _CyanXcvrWavelength_Type()
)
cyanXcvrWavelength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanXcvrWavelength.setStatus("current")
_CyanXcvrWdmType_Type = CyanWdmTypeTc
_CyanXcvrWdmType_Object = MibTableColumn
cyanXcvrWdmType = _CyanXcvrWdmType_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 140, 1, 1, 1, 60),
    _CyanXcvrWdmType_Type()
)
cyanXcvrWdmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanXcvrWdmType.setStatus("current")
_CyanXcvrWlenError_Type = Integer32
_CyanXcvrWlenError_Object = MibTableColumn
cyanXcvrWlenError = _CyanXcvrWlenError_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 140, 1, 1, 1, 61),
    _CyanXcvrWlenError_Type()
)
cyanXcvrWlenError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanXcvrWlenError.setStatus("current")
_CyanXcvrWlenIsTunable_Type = CyanNoYesTc
_CyanXcvrWlenIsTunable_Object = MibTableColumn
cyanXcvrWlenIsTunable = _CyanXcvrWlenIsTunable_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 140, 1, 1, 1, 62),
    _CyanXcvrWlenIsTunable_Type()
)
cyanXcvrWlenIsTunable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanXcvrWlenIsTunable.setStatus("current")
_CyanXcvrWlenSetpoint_Type = Integer32
_CyanXcvrWlenSetpoint_Object = MibTableColumn
cyanXcvrWlenSetpoint = _CyanXcvrWlenSetpoint_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 140, 1, 1, 1, 63),
    _CyanXcvrWlenSetpoint_Type()
)
cyanXcvrWlenSetpoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanXcvrWlenSetpoint.setStatus("current")
_CyanXcvrWlenTolerance_Type = Integer32
_CyanXcvrWlenTolerance_Object = MibTableColumn
cyanXcvrWlenTolerance = _CyanXcvrWlenTolerance_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 140, 1, 1, 1, 64),
    _CyanXcvrWlenTolerance_Type()
)
cyanXcvrWlenTolerance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanXcvrWlenTolerance.setStatus("current")

# Managed Objects groups

cyanXcvrObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 140, 20)
)
cyanXcvrObjectGroup.setObjects(
      *(("CYAN-XCVR-MIB", "cyanXcvrAdminState"),
        ("CYAN-XCVR-MIB", "cyanXcvrAutoinserviceSoakTimeSec"),
        ("CYAN-XCVR-MIB", "cyanXcvrComplianceCode"),
        ("CYAN-XCVR-MIB", "cyanXcvrConnectorCode"),
        ("CYAN-XCVR-MIB", "cyanXcvrCyanName"),
        ("CYAN-XCVR-MIB", "cyanXcvrCyanPartNumber"),
        ("CYAN-XCVR-MIB", "cyanXcvrDescription"),
        ("CYAN-XCVR-MIB", "cyanXcvrIdentifier"),
        ("CYAN-XCVR-MIB", "cyanXcvrIdentifierCode"),
        ("CYAN-XCVR-MIB", "cyanXcvrLength9"),
        ("CYAN-XCVR-MIB", "cyanXcvrMaxBitRate"),
        ("CYAN-XCVR-MIB", "cyanXcvrMfgDateCode"),
        ("CYAN-XCVR-MIB", "cyanXcvrMinBitRate"),
        ("CYAN-XCVR-MIB", "cyanXcvrMmf3Maxlen"),
        ("CYAN-XCVR-MIB", "cyanXcvrMmf4Maxlen"),
        ("CYAN-XCVR-MIB", "cyanXcvrName"),
        ("CYAN-XCVR-MIB", "cyanXcvrNominalBitRate"),
        ("CYAN-XCVR-MIB", "cyanXcvrOidClass"),
        ("CYAN-XCVR-MIB", "cyanXcvrOperState"),
        ("CYAN-XCVR-MIB", "cyanXcvrOperStateQual"),
        ("CYAN-XCVR-MIB", "cyanXcvrOptSensitivityAdjustSupp"),
        ("CYAN-XCVR-MIB", "cyanXcvrOssLabel"),
        ("CYAN-XCVR-MIB", "cyanXcvrOuiCode"),
        ("CYAN-XCVR-MIB", "cyanXcvrOwner"),
        ("CYAN-XCVR-MIB", "cyanXcvrPartNumber"),
        ("CYAN-XCVR-MIB", "cyanXcvrPowerClass"),
        ("CYAN-XCVR-MIB", "cyanXcvrRealTimeDiagImplemented"),
        ("CYAN-XCVR-MIB", "cyanXcvrRxPwrHiAlrmThres"),
        ("CYAN-XCVR-MIB", "cyanXcvrRxPwrHiWarnThres"),
        ("CYAN-XCVR-MIB", "cyanXcvrRxPwrLoAlrmThres"),
        ("CYAN-XCVR-MIB", "cyanXcvrRxPwrLoWarnThres"),
        ("CYAN-XCVR-MIB", "cyanXcvrSecServState"),
        ("CYAN-XCVR-MIB", "cyanXcvrSerialNumber"),
        ("CYAN-XCVR-MIB", "cyanXcvrSfpOptions"),
        ("CYAN-XCVR-MIB", "cyanXcvrTempHiAlrmThres"),
        ("CYAN-XCVR-MIB", "cyanXcvrTempHiWarnThres"),
        ("CYAN-XCVR-MIB", "cyanXcvrTempLoAlrmThres"),
        ("CYAN-XCVR-MIB", "cyanXcvrTempLoWarnThres"),
        ("CYAN-XCVR-MIB", "cyanXcvrTemperature"),
        ("CYAN-XCVR-MIB", "cyanXcvrTxBiasCurrent"),
        ("CYAN-XCVR-MIB", "cyanXcvrTxBiasHiAlrmThres"),
        ("CYAN-XCVR-MIB", "cyanXcvrTxBiasHiWarnThres"),
        ("CYAN-XCVR-MIB", "cyanXcvrTxBiasLoAlrmThres"),
        ("CYAN-XCVR-MIB", "cyanXcvrTxBiasLoWarnThres"),
        ("CYAN-XCVR-MIB", "cyanXcvrTxPwrHiAlrmThres"),
        ("CYAN-XCVR-MIB", "cyanXcvrTxPwrHiWarnThres"),
        ("CYAN-XCVR-MIB", "cyanXcvrTxPwrLoAlrmThres"),
        ("CYAN-XCVR-MIB", "cyanXcvrTxPwrLoWarnThres"),
        ("CYAN-XCVR-MIB", "cyanXcvrVccVoltHiAlrmThres"),
        ("CYAN-XCVR-MIB", "cyanXcvrVccVoltHiWarnThres"),
        ("CYAN-XCVR-MIB", "cyanXcvrVccVoltLoAlrmThres"),
        ("CYAN-XCVR-MIB", "cyanXcvrVccVoltLoWarnThres"),
        ("CYAN-XCVR-MIB", "cyanXcvrVccVoltage"),
        ("CYAN-XCVR-MIB", "cyanXcvrVendorName"),
        ("CYAN-XCVR-MIB", "cyanXcvrVendorRev"),
        ("CYAN-XCVR-MIB", "cyanXcvrWavelength"),
        ("CYAN-XCVR-MIB", "cyanXcvrWdmType"),
        ("CYAN-XCVR-MIB", "cyanXcvrWlenError"),
        ("CYAN-XCVR-MIB", "cyanXcvrWlenIsTunable"),
        ("CYAN-XCVR-MIB", "cyanXcvrWlenSetpoint"),
        ("CYAN-XCVR-MIB", "cyanXcvrWlenTolerance"))
)
if mibBuilder.loadTexts:
    cyanXcvrObjectGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cyanXcvrCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 140, 30)
)
if mibBuilder.loadTexts:
    cyanXcvrCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CYAN-XCVR-MIB",
    **{"cyanXcvrModule": cyanXcvrModule,
       "cyanXcvrMibObjects": cyanXcvrMibObjects,
       "cyanXcvrTable": cyanXcvrTable,
       "cyanXcvrEntry": cyanXcvrEntry,
       "cyanXcvrShelfId": cyanXcvrShelfId,
       "cyanXcvrModuleId": cyanXcvrModuleId,
       "cyanXcvrXcvrId": cyanXcvrXcvrId,
       "cyanXcvrAdminState": cyanXcvrAdminState,
       "cyanXcvrAutoinserviceSoakTimeSec": cyanXcvrAutoinserviceSoakTimeSec,
       "cyanXcvrComplianceCode": cyanXcvrComplianceCode,
       "cyanXcvrConnectorCode": cyanXcvrConnectorCode,
       "cyanXcvrCyanName": cyanXcvrCyanName,
       "cyanXcvrCyanPartNumber": cyanXcvrCyanPartNumber,
       "cyanXcvrDescription": cyanXcvrDescription,
       "cyanXcvrIdentifier": cyanXcvrIdentifier,
       "cyanXcvrIdentifierCode": cyanXcvrIdentifierCode,
       "cyanXcvrLength9": cyanXcvrLength9,
       "cyanXcvrMaxBitRate": cyanXcvrMaxBitRate,
       "cyanXcvrMfgDateCode": cyanXcvrMfgDateCode,
       "cyanXcvrMinBitRate": cyanXcvrMinBitRate,
       "cyanXcvrMmf3Maxlen": cyanXcvrMmf3Maxlen,
       "cyanXcvrMmf4Maxlen": cyanXcvrMmf4Maxlen,
       "cyanXcvrName": cyanXcvrName,
       "cyanXcvrNominalBitRate": cyanXcvrNominalBitRate,
       "cyanXcvrOidClass": cyanXcvrOidClass,
       "cyanXcvrOperState": cyanXcvrOperState,
       "cyanXcvrOperStateQual": cyanXcvrOperStateQual,
       "cyanXcvrOptSensitivityAdjustSupp": cyanXcvrOptSensitivityAdjustSupp,
       "cyanXcvrOssLabel": cyanXcvrOssLabel,
       "cyanXcvrOuiCode": cyanXcvrOuiCode,
       "cyanXcvrOwner": cyanXcvrOwner,
       "cyanXcvrPartNumber": cyanXcvrPartNumber,
       "cyanXcvrPowerClass": cyanXcvrPowerClass,
       "cyanXcvrRealTimeDiagImplemented": cyanXcvrRealTimeDiagImplemented,
       "cyanXcvrRxPwrHiAlrmThres": cyanXcvrRxPwrHiAlrmThres,
       "cyanXcvrRxPwrHiWarnThres": cyanXcvrRxPwrHiWarnThres,
       "cyanXcvrRxPwrLoAlrmThres": cyanXcvrRxPwrLoAlrmThres,
       "cyanXcvrRxPwrLoWarnThres": cyanXcvrRxPwrLoWarnThres,
       "cyanXcvrSecServState": cyanXcvrSecServState,
       "cyanXcvrSerialNumber": cyanXcvrSerialNumber,
       "cyanXcvrSfpOptions": cyanXcvrSfpOptions,
       "cyanXcvrTempHiAlrmThres": cyanXcvrTempHiAlrmThres,
       "cyanXcvrTempHiWarnThres": cyanXcvrTempHiWarnThres,
       "cyanXcvrTempLoAlrmThres": cyanXcvrTempLoAlrmThres,
       "cyanXcvrTempLoWarnThres": cyanXcvrTempLoWarnThres,
       "cyanXcvrTemperature": cyanXcvrTemperature,
       "cyanXcvrTxBiasCurrent": cyanXcvrTxBiasCurrent,
       "cyanXcvrTxBiasHiAlrmThres": cyanXcvrTxBiasHiAlrmThres,
       "cyanXcvrTxBiasHiWarnThres": cyanXcvrTxBiasHiWarnThres,
       "cyanXcvrTxBiasLoAlrmThres": cyanXcvrTxBiasLoAlrmThres,
       "cyanXcvrTxBiasLoWarnThres": cyanXcvrTxBiasLoWarnThres,
       "cyanXcvrTxPwrHiAlrmThres": cyanXcvrTxPwrHiAlrmThres,
       "cyanXcvrTxPwrHiWarnThres": cyanXcvrTxPwrHiWarnThres,
       "cyanXcvrTxPwrLoAlrmThres": cyanXcvrTxPwrLoAlrmThres,
       "cyanXcvrTxPwrLoWarnThres": cyanXcvrTxPwrLoWarnThres,
       "cyanXcvrVccVoltHiAlrmThres": cyanXcvrVccVoltHiAlrmThres,
       "cyanXcvrVccVoltHiWarnThres": cyanXcvrVccVoltHiWarnThres,
       "cyanXcvrVccVoltLoAlrmThres": cyanXcvrVccVoltLoAlrmThres,
       "cyanXcvrVccVoltLoWarnThres": cyanXcvrVccVoltLoWarnThres,
       "cyanXcvrVccVoltage": cyanXcvrVccVoltage,
       "cyanXcvrVendorName": cyanXcvrVendorName,
       "cyanXcvrVendorRev": cyanXcvrVendorRev,
       "cyanXcvrWavelength": cyanXcvrWavelength,
       "cyanXcvrWdmType": cyanXcvrWdmType,
       "cyanXcvrWlenError": cyanXcvrWlenError,
       "cyanXcvrWlenIsTunable": cyanXcvrWlenIsTunable,
       "cyanXcvrWlenSetpoint": cyanXcvrWlenSetpoint,
       "cyanXcvrWlenTolerance": cyanXcvrWlenTolerance,
       "cyanXcvrObjectGroup": cyanXcvrObjectGroup,
       "cyanXcvrCompliance": cyanXcvrCompliance}
)
