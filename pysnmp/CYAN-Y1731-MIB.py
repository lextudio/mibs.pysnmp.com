# SNMP MIB module (CYAN-Y1731-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CYAN-Y1731-MIB
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

(cyanMibModules,) = mibBuilder.importSymbols(
    "CYAN-MIB",
    "cyanMibModules")

(CyanNoYesTc,) = mibBuilder.importSymbols(
    "CYAN-TC-MIB",
    "CyanNoYesTc")

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

cyanY1731Module = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 28533, 5, 40)
)
cyanY1731Module.setRevisions(
        ("2014-12-07 05:45",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CyanY1731MibObjects_ObjectIdentity = ObjectIdentity
cyanY1731MibObjects = _CyanY1731MibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28533, 5, 40, 1)
)
_CyanY1731MepConfigTable_Object = MibTable
cyanY1731MepConfigTable = _CyanY1731MepConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 40, 1, 1)
)
if mibBuilder.loadTexts:
    cyanY1731MepConfigTable.setStatus("current")
_CyanY1731MepConfigEntry_Object = MibTableRow
cyanY1731MepConfigEntry = _CyanY1731MepConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 40, 1, 1, 1)
)
cyanY1731MepConfigEntry.setIndexNames(
    (0, "CYAN-Y1731-MIB", "cyanY1731MepConfigShelfId"),
    (0, "CYAN-Y1731-MIB", "cyanY1731MepConfigModuleId"),
    (0, "CYAN-Y1731-MIB", "cyanY1731MepConfigMepId"),
)
if mibBuilder.loadTexts:
    cyanY1731MepConfigEntry.setStatus("current")


class _CyanY1731MepConfigShelfId_Type(Unsigned32):
    """Custom type cyanY1731MepConfigShelfId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CyanY1731MepConfigShelfId_Type.__name__ = "Unsigned32"
_CyanY1731MepConfigShelfId_Object = MibTableColumn
cyanY1731MepConfigShelfId = _CyanY1731MepConfigShelfId_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 40, 1, 1, 1, 1),
    _CyanY1731MepConfigShelfId_Type()
)
cyanY1731MepConfigShelfId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cyanY1731MepConfigShelfId.setStatus("current")
_CyanY1731MepConfigModuleId_Type = Unsigned32
_CyanY1731MepConfigModuleId_Object = MibTableColumn
cyanY1731MepConfigModuleId = _CyanY1731MepConfigModuleId_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 40, 1, 1, 1, 2),
    _CyanY1731MepConfigModuleId_Type()
)
cyanY1731MepConfigModuleId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cyanY1731MepConfigModuleId.setStatus("current")
_CyanY1731MepConfigMepId_Type = Unsigned32
_CyanY1731MepConfigMepId_Object = MibTableColumn
cyanY1731MepConfigMepId = _CyanY1731MepConfigMepId_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 40, 1, 1, 1, 3),
    _CyanY1731MepConfigMepId_Type()
)
cyanY1731MepConfigMepId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cyanY1731MepConfigMepId.setStatus("current")
_CyanY1731MepConfigLMTxInterval_Type = Unsigned32
_CyanY1731MepConfigLMTxInterval_Object = MibTableColumn
cyanY1731MepConfigLMTxInterval = _CyanY1731MepConfigLMTxInterval_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 40, 1, 1, 1, 4),
    _CyanY1731MepConfigLMTxInterval_Type()
)
cyanY1731MepConfigLMTxInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanY1731MepConfigLMTxInterval.setStatus("current")
_CyanY1731MepConfigDMTxInterval_Type = Unsigned32
_CyanY1731MepConfigDMTxInterval_Object = MibTableColumn
cyanY1731MepConfigDMTxInterval = _CyanY1731MepConfigDMTxInterval_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 40, 1, 1, 1, 5),
    _CyanY1731MepConfigDMTxInterval_Type()
)
cyanY1731MepConfigDMTxInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanY1731MepConfigDMTxInterval.setStatus("current")
_CyanY1731MepConfigPmEnabled_Type = CyanNoYesTc
_CyanY1731MepConfigPmEnabled_Object = MibTableColumn
cyanY1731MepConfigPmEnabled = _CyanY1731MepConfigPmEnabled_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 40, 1, 1, 1, 6),
    _CyanY1731MepConfigPmEnabled_Type()
)
cyanY1731MepConfigPmEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanY1731MepConfigPmEnabled.setStatus("current")
_CyanY1731MepConfigOneWayLossEnabled_Type = CyanNoYesTc
_CyanY1731MepConfigOneWayLossEnabled_Object = MibTableColumn
cyanY1731MepConfigOneWayLossEnabled = _CyanY1731MepConfigOneWayLossEnabled_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 40, 1, 1, 1, 7),
    _CyanY1731MepConfigOneWayLossEnabled_Type()
)
cyanY1731MepConfigOneWayLossEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanY1731MepConfigOneWayLossEnabled.setStatus("current")
_CyanY1731MepConfigTwoWayDelayEnabled_Type = CyanNoYesTc
_CyanY1731MepConfigTwoWayDelayEnabled_Object = MibTableColumn
cyanY1731MepConfigTwoWayDelayEnabled = _CyanY1731MepConfigTwoWayDelayEnabled_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 40, 1, 1, 1, 8),
    _CyanY1731MepConfigTwoWayDelayEnabled_Type()
)
cyanY1731MepConfigTwoWayDelayEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanY1731MepConfigTwoWayDelayEnabled.setStatus("current")
_CyanY1731MepConfigTwoWayJitterEnabled_Type = CyanNoYesTc
_CyanY1731MepConfigTwoWayJitterEnabled_Object = MibTableColumn
cyanY1731MepConfigTwoWayJitterEnabled = _CyanY1731MepConfigTwoWayJitterEnabled_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 40, 1, 1, 1, 9),
    _CyanY1731MepConfigTwoWayJitterEnabled_Type()
)
cyanY1731MepConfigTwoWayJitterEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanY1731MepConfigTwoWayJitterEnabled.setStatus("current")
_CyanY1731LMTable_Object = MibTable
cyanY1731LMTable = _CyanY1731LMTable_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 40, 1, 2)
)
if mibBuilder.loadTexts:
    cyanY1731LMTable.setStatus("current")
_CyanY1731LMEntry_Object = MibTableRow
cyanY1731LMEntry = _CyanY1731LMEntry_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 40, 1, 2, 1)
)
cyanY1731LMEntry.setIndexNames(
    (0, "CYAN-Y1731-MIB", "cyanY1731LMShelfId"),
    (0, "CYAN-Y1731-MIB", "cyanY1731LMModuleId"),
    (0, "CYAN-Y1731-MIB", "cyanY1731LMMepId"),
    (0, "CYAN-Y1731-MIB", "cyanY1731LMIndex"),
)
if mibBuilder.loadTexts:
    cyanY1731LMEntry.setStatus("current")


class _CyanY1731LMShelfId_Type(Unsigned32):
    """Custom type cyanY1731LMShelfId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CyanY1731LMShelfId_Type.__name__ = "Unsigned32"
_CyanY1731LMShelfId_Object = MibTableColumn
cyanY1731LMShelfId = _CyanY1731LMShelfId_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 40, 1, 2, 1, 1),
    _CyanY1731LMShelfId_Type()
)
cyanY1731LMShelfId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cyanY1731LMShelfId.setStatus("current")
_CyanY1731LMModuleId_Type = Unsigned32
_CyanY1731LMModuleId_Object = MibTableColumn
cyanY1731LMModuleId = _CyanY1731LMModuleId_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 40, 1, 2, 1, 2),
    _CyanY1731LMModuleId_Type()
)
cyanY1731LMModuleId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cyanY1731LMModuleId.setStatus("current")
_CyanY1731LMMepId_Type = Unsigned32
_CyanY1731LMMepId_Object = MibTableColumn
cyanY1731LMMepId = _CyanY1731LMMepId_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 40, 1, 2, 1, 3),
    _CyanY1731LMMepId_Type()
)
cyanY1731LMMepId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cyanY1731LMMepId.setStatus("current")
_CyanY1731LMIndex_Type = Unsigned32
_CyanY1731LMIndex_Object = MibTableColumn
cyanY1731LMIndex = _CyanY1731LMIndex_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 40, 1, 2, 1, 4),
    _CyanY1731LMIndex_Type()
)
cyanY1731LMIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cyanY1731LMIndex.setStatus("current")
_CyanY1731LMNe15MinPmCount_Type = Unsigned32
_CyanY1731LMNe15MinPmCount_Object = MibTableColumn
cyanY1731LMNe15MinPmCount = _CyanY1731LMNe15MinPmCount_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 40, 1, 2, 1, 5),
    _CyanY1731LMNe15MinPmCount_Type()
)
cyanY1731LMNe15MinPmCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanY1731LMNe15MinPmCount.setStatus("current")
_CyanY1731LMNe15MinPmTimestamp_Type = Unsigned32
_CyanY1731LMNe15MinPmTimestamp_Object = MibTableColumn
cyanY1731LMNe15MinPmTimestamp = _CyanY1731LMNe15MinPmTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 40, 1, 2, 1, 6),
    _CyanY1731LMNe15MinPmTimestamp_Type()
)
cyanY1731LMNe15MinPmTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanY1731LMNe15MinPmTimestamp.setStatus("current")
_CyanY1731LMFe15MinPmCount_Type = Unsigned32
_CyanY1731LMFe15MinPmCount_Object = MibTableColumn
cyanY1731LMFe15MinPmCount = _CyanY1731LMFe15MinPmCount_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 40, 1, 2, 1, 7),
    _CyanY1731LMFe15MinPmCount_Type()
)
cyanY1731LMFe15MinPmCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanY1731LMFe15MinPmCount.setStatus("current")
_CyanY1731LMFe15MinPmTimestamp_Type = Unsigned32
_CyanY1731LMFe15MinPmTimestamp_Object = MibTableColumn
cyanY1731LMFe15MinPmTimestamp = _CyanY1731LMFe15MinPmTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 40, 1, 2, 1, 8),
    _CyanY1731LMFe15MinPmTimestamp_Type()
)
cyanY1731LMFe15MinPmTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanY1731LMFe15MinPmTimestamp.setStatus("current")
_CyanY1731LMRatioNe15MinHighValue_Type = Unsigned32
_CyanY1731LMRatioNe15MinHighValue_Object = MibTableColumn
cyanY1731LMRatioNe15MinHighValue = _CyanY1731LMRatioNe15MinHighValue_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 40, 1, 2, 1, 9),
    _CyanY1731LMRatioNe15MinHighValue_Type()
)
cyanY1731LMRatioNe15MinHighValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanY1731LMRatioNe15MinHighValue.setStatus("current")
_CyanY1731LMRatioNe15MinLowValue_Type = Unsigned32
_CyanY1731LMRatioNe15MinLowValue_Object = MibTableColumn
cyanY1731LMRatioNe15MinLowValue = _CyanY1731LMRatioNe15MinLowValue_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 40, 1, 2, 1, 10),
    _CyanY1731LMRatioNe15MinLowValue_Type()
)
cyanY1731LMRatioNe15MinLowValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanY1731LMRatioNe15MinLowValue.setStatus("current")
_CyanY1731LMRatioNe15MinAvgValue_Type = Unsigned32
_CyanY1731LMRatioNe15MinAvgValue_Object = MibTableColumn
cyanY1731LMRatioNe15MinAvgValue = _CyanY1731LMRatioNe15MinAvgValue_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 40, 1, 2, 1, 11),
    _CyanY1731LMRatioNe15MinAvgValue_Type()
)
cyanY1731LMRatioNe15MinAvgValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanY1731LMRatioNe15MinAvgValue.setStatus("current")
_CyanY1731LMRatioNe15MinTimestamp_Type = Unsigned32
_CyanY1731LMRatioNe15MinTimestamp_Object = MibTableColumn
cyanY1731LMRatioNe15MinTimestamp = _CyanY1731LMRatioNe15MinTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 40, 1, 2, 1, 12),
    _CyanY1731LMRatioNe15MinTimestamp_Type()
)
cyanY1731LMRatioNe15MinTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanY1731LMRatioNe15MinTimestamp.setStatus("current")
_CyanY1731LMRatioFe15MinHighValue_Type = Unsigned32
_CyanY1731LMRatioFe15MinHighValue_Object = MibTableColumn
cyanY1731LMRatioFe15MinHighValue = _CyanY1731LMRatioFe15MinHighValue_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 40, 1, 2, 1, 13),
    _CyanY1731LMRatioFe15MinHighValue_Type()
)
cyanY1731LMRatioFe15MinHighValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanY1731LMRatioFe15MinHighValue.setStatus("current")
_CyanY1731LMRatioFe15MinLowValue_Type = Unsigned32
_CyanY1731LMRatioFe15MinLowValue_Object = MibTableColumn
cyanY1731LMRatioFe15MinLowValue = _CyanY1731LMRatioFe15MinLowValue_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 40, 1, 2, 1, 14),
    _CyanY1731LMRatioFe15MinLowValue_Type()
)
cyanY1731LMRatioFe15MinLowValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanY1731LMRatioFe15MinLowValue.setStatus("current")
_CyanY1731LMRatioFe15MinAvgValue_Type = Unsigned32
_CyanY1731LMRatioFe15MinAvgValue_Object = MibTableColumn
cyanY1731LMRatioFe15MinAvgValue = _CyanY1731LMRatioFe15MinAvgValue_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 40, 1, 2, 1, 15),
    _CyanY1731LMRatioFe15MinAvgValue_Type()
)
cyanY1731LMRatioFe15MinAvgValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanY1731LMRatioFe15MinAvgValue.setStatus("current")
_CyanY1731LMRatioFe15MinTimestamp_Type = Unsigned32
_CyanY1731LMRatioFe15MinTimestamp_Object = MibTableColumn
cyanY1731LMRatioFe15MinTimestamp = _CyanY1731LMRatioFe15MinTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 40, 1, 2, 1, 16),
    _CyanY1731LMRatioFe15MinTimestamp_Type()
)
cyanY1731LMRatioFe15MinTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanY1731LMRatioFe15MinTimestamp.setStatus("current")
_CyanY1731DMTable_Object = MibTable
cyanY1731DMTable = _CyanY1731DMTable_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 40, 1, 3)
)
if mibBuilder.loadTexts:
    cyanY1731DMTable.setStatus("current")
_CyanY1731DMEntry_Object = MibTableRow
cyanY1731DMEntry = _CyanY1731DMEntry_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 40, 1, 3, 1)
)
cyanY1731DMEntry.setIndexNames(
    (0, "CYAN-Y1731-MIB", "cyanY1731DMShelfId"),
    (0, "CYAN-Y1731-MIB", "cyanY1731DMModuleId"),
    (0, "CYAN-Y1731-MIB", "cyanY1731DMMepId"),
    (0, "CYAN-Y1731-MIB", "cyanY1731DMMepIndex"),
)
if mibBuilder.loadTexts:
    cyanY1731DMEntry.setStatus("current")


class _CyanY1731DMShelfId_Type(Unsigned32):
    """Custom type cyanY1731DMShelfId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CyanY1731DMShelfId_Type.__name__ = "Unsigned32"
_CyanY1731DMShelfId_Object = MibTableColumn
cyanY1731DMShelfId = _CyanY1731DMShelfId_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 40, 1, 3, 1, 1),
    _CyanY1731DMShelfId_Type()
)
cyanY1731DMShelfId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cyanY1731DMShelfId.setStatus("current")
_CyanY1731DMModuleId_Type = Unsigned32
_CyanY1731DMModuleId_Object = MibTableColumn
cyanY1731DMModuleId = _CyanY1731DMModuleId_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 40, 1, 3, 1, 2),
    _CyanY1731DMModuleId_Type()
)
cyanY1731DMModuleId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cyanY1731DMModuleId.setStatus("current")
_CyanY1731DMMepId_Type = Unsigned32
_CyanY1731DMMepId_Object = MibTableColumn
cyanY1731DMMepId = _CyanY1731DMMepId_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 40, 1, 3, 1, 3),
    _CyanY1731DMMepId_Type()
)
cyanY1731DMMepId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cyanY1731DMMepId.setStatus("current")
_CyanY1731DMMepIndex_Type = Unsigned32
_CyanY1731DMMepIndex_Object = MibTableColumn
cyanY1731DMMepIndex = _CyanY1731DMMepIndex_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 40, 1, 3, 1, 4),
    _CyanY1731DMMepIndex_Type()
)
cyanY1731DMMepIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cyanY1731DMMepIndex.setStatus("current")
_CyanY1731DMTwoWayDelay15MinHighValue_Type = Unsigned32
_CyanY1731DMTwoWayDelay15MinHighValue_Object = MibTableColumn
cyanY1731DMTwoWayDelay15MinHighValue = _CyanY1731DMTwoWayDelay15MinHighValue_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 40, 1, 3, 1, 5),
    _CyanY1731DMTwoWayDelay15MinHighValue_Type()
)
cyanY1731DMTwoWayDelay15MinHighValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanY1731DMTwoWayDelay15MinHighValue.setStatus("current")
_CyanY1731DMTwoWayDelay15MinLowValue_Type = Unsigned32
_CyanY1731DMTwoWayDelay15MinLowValue_Object = MibTableColumn
cyanY1731DMTwoWayDelay15MinLowValue = _CyanY1731DMTwoWayDelay15MinLowValue_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 40, 1, 3, 1, 6),
    _CyanY1731DMTwoWayDelay15MinLowValue_Type()
)
cyanY1731DMTwoWayDelay15MinLowValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanY1731DMTwoWayDelay15MinLowValue.setStatus("current")
_CyanY1731DMTwoWayDelay15MinAvgValue_Type = Unsigned32
_CyanY1731DMTwoWayDelay15MinAvgValue_Object = MibTableColumn
cyanY1731DMTwoWayDelay15MinAvgValue = _CyanY1731DMTwoWayDelay15MinAvgValue_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 40, 1, 3, 1, 7),
    _CyanY1731DMTwoWayDelay15MinAvgValue_Type()
)
cyanY1731DMTwoWayDelay15MinAvgValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanY1731DMTwoWayDelay15MinAvgValue.setStatus("current")
_CyanY1731DMTwoWayDelay15MinTimestamp_Type = Unsigned32
_CyanY1731DMTwoWayDelay15MinTimestamp_Object = MibTableColumn
cyanY1731DMTwoWayDelay15MinTimestamp = _CyanY1731DMTwoWayDelay15MinTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 40, 1, 3, 1, 8),
    _CyanY1731DMTwoWayDelay15MinTimestamp_Type()
)
cyanY1731DMTwoWayDelay15MinTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanY1731DMTwoWayDelay15MinTimestamp.setStatus("current")
_CyanY1731DMTwoWayDelayVar15MinHighValue_Type = Unsigned32
_CyanY1731DMTwoWayDelayVar15MinHighValue_Object = MibTableColumn
cyanY1731DMTwoWayDelayVar15MinHighValue = _CyanY1731DMTwoWayDelayVar15MinHighValue_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 40, 1, 3, 1, 9),
    _CyanY1731DMTwoWayDelayVar15MinHighValue_Type()
)
cyanY1731DMTwoWayDelayVar15MinHighValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanY1731DMTwoWayDelayVar15MinHighValue.setStatus("current")
_CyanY1731DMTwoWayDelayVar15MinLowValue_Type = Unsigned32
_CyanY1731DMTwoWayDelayVar15MinLowValue_Object = MibTableColumn
cyanY1731DMTwoWayDelayVar15MinLowValue = _CyanY1731DMTwoWayDelayVar15MinLowValue_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 40, 1, 3, 1, 10),
    _CyanY1731DMTwoWayDelayVar15MinLowValue_Type()
)
cyanY1731DMTwoWayDelayVar15MinLowValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanY1731DMTwoWayDelayVar15MinLowValue.setStatus("current")
_CyanY1731DMTwoWayDelayVar15MinAvgValue_Type = Unsigned32
_CyanY1731DMTwoWayDelayVar15MinAvgValue_Object = MibTableColumn
cyanY1731DMTwoWayDelayVar15MinAvgValue = _CyanY1731DMTwoWayDelayVar15MinAvgValue_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 40, 1, 3, 1, 11),
    _CyanY1731DMTwoWayDelayVar15MinAvgValue_Type()
)
cyanY1731DMTwoWayDelayVar15MinAvgValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanY1731DMTwoWayDelayVar15MinAvgValue.setStatus("current")
_CyanY1731DMTwoWayDelayVar15MinTimestamp_Type = Unsigned32
_CyanY1731DMTwoWayDelayVar15MinTimestamp_Object = MibTableColumn
cyanY1731DMTwoWayDelayVar15MinTimestamp = _CyanY1731DMTwoWayDelayVar15MinTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 40, 1, 3, 1, 12),
    _CyanY1731DMTwoWayDelayVar15MinTimestamp_Type()
)
cyanY1731DMTwoWayDelayVar15MinTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanY1731DMTwoWayDelayVar15MinTimestamp.setStatus("current")

# Managed Objects groups

cyanY1731MepConfigObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 28533, 5, 40, 100)
)
cyanY1731MepConfigObjectGroup.setObjects(
      *(("CYAN-Y1731-MIB", "cyanY1731MepConfigLMTxInterval"),
        ("CYAN-Y1731-MIB", "cyanY1731MepConfigDMTxInterval"),
        ("CYAN-Y1731-MIB", "cyanY1731MepConfigPmEnabled"),
        ("CYAN-Y1731-MIB", "cyanY1731MepConfigOneWayLossEnabled"),
        ("CYAN-Y1731-MIB", "cyanY1731MepConfigTwoWayDelayEnabled"),
        ("CYAN-Y1731-MIB", "cyanY1731MepConfigTwoWayJitterEnabled"))
)
if mibBuilder.loadTexts:
    cyanY1731MepConfigObjectGroup.setStatus("current")

cyanY1731LMObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 28533, 5, 40, 102)
)
cyanY1731LMObjectGroup.setObjects(
      *(("CYAN-Y1731-MIB", "cyanY1731LMNe15MinPmCount"),
        ("CYAN-Y1731-MIB", "cyanY1731LMNe15MinPmTimestamp"),
        ("CYAN-Y1731-MIB", "cyanY1731LMFe15MinPmCount"),
        ("CYAN-Y1731-MIB", "cyanY1731LMFe15MinPmTimestamp"),
        ("CYAN-Y1731-MIB", "cyanY1731LMRatioNe15MinHighValue"),
        ("CYAN-Y1731-MIB", "cyanY1731LMRatioNe15MinLowValue"),
        ("CYAN-Y1731-MIB", "cyanY1731LMRatioNe15MinAvgValue"),
        ("CYAN-Y1731-MIB", "cyanY1731LMRatioNe15MinTimestamp"),
        ("CYAN-Y1731-MIB", "cyanY1731LMRatioFe15MinHighValue"),
        ("CYAN-Y1731-MIB", "cyanY1731LMRatioFe15MinLowValue"),
        ("CYAN-Y1731-MIB", "cyanY1731LMRatioFe15MinAvgValue"),
        ("CYAN-Y1731-MIB", "cyanY1731LMRatioFe15MinTimestamp"))
)
if mibBuilder.loadTexts:
    cyanY1731LMObjectGroup.setStatus("current")

cyanY1731DMObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 28533, 5, 40, 104)
)
cyanY1731DMObjectGroup.setObjects(
      *(("CYAN-Y1731-MIB", "cyanY1731DMTwoWayDelay15MinHighValue"),
        ("CYAN-Y1731-MIB", "cyanY1731DMTwoWayDelay15MinLowValue"),
        ("CYAN-Y1731-MIB", "cyanY1731DMTwoWayDelay15MinAvgValue"),
        ("CYAN-Y1731-MIB", "cyanY1731DMTwoWayDelay15MinTimestamp"),
        ("CYAN-Y1731-MIB", "cyanY1731DMTwoWayDelayVar15MinHighValue"),
        ("CYAN-Y1731-MIB", "cyanY1731DMTwoWayDelayVar15MinLowValue"),
        ("CYAN-Y1731-MIB", "cyanY1731DMTwoWayDelayVar15MinAvgValue"),
        ("CYAN-Y1731-MIB", "cyanY1731DMTwoWayDelayVar15MinTimestamp"))
)
if mibBuilder.loadTexts:
    cyanY1731DMObjectGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cyanY1731MepConfigCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 28533, 5, 40, 101)
)
if mibBuilder.loadTexts:
    cyanY1731MepConfigCompliance.setStatus(
        "current"
    )

cyanY1731LMCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 28533, 5, 40, 103)
)
if mibBuilder.loadTexts:
    cyanY1731LMCompliance.setStatus(
        "current"
    )

cyanY1731DMCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 28533, 5, 40, 105)
)
if mibBuilder.loadTexts:
    cyanY1731DMCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CYAN-Y1731-MIB",
    **{"cyanY1731Module": cyanY1731Module,
       "cyanY1731MibObjects": cyanY1731MibObjects,
       "cyanY1731MepConfigTable": cyanY1731MepConfigTable,
       "cyanY1731MepConfigEntry": cyanY1731MepConfigEntry,
       "cyanY1731MepConfigShelfId": cyanY1731MepConfigShelfId,
       "cyanY1731MepConfigModuleId": cyanY1731MepConfigModuleId,
       "cyanY1731MepConfigMepId": cyanY1731MepConfigMepId,
       "cyanY1731MepConfigLMTxInterval": cyanY1731MepConfigLMTxInterval,
       "cyanY1731MepConfigDMTxInterval": cyanY1731MepConfigDMTxInterval,
       "cyanY1731MepConfigPmEnabled": cyanY1731MepConfigPmEnabled,
       "cyanY1731MepConfigOneWayLossEnabled": cyanY1731MepConfigOneWayLossEnabled,
       "cyanY1731MepConfigTwoWayDelayEnabled": cyanY1731MepConfigTwoWayDelayEnabled,
       "cyanY1731MepConfigTwoWayJitterEnabled": cyanY1731MepConfigTwoWayJitterEnabled,
       "cyanY1731LMTable": cyanY1731LMTable,
       "cyanY1731LMEntry": cyanY1731LMEntry,
       "cyanY1731LMShelfId": cyanY1731LMShelfId,
       "cyanY1731LMModuleId": cyanY1731LMModuleId,
       "cyanY1731LMMepId": cyanY1731LMMepId,
       "cyanY1731LMIndex": cyanY1731LMIndex,
       "cyanY1731LMNe15MinPmCount": cyanY1731LMNe15MinPmCount,
       "cyanY1731LMNe15MinPmTimestamp": cyanY1731LMNe15MinPmTimestamp,
       "cyanY1731LMFe15MinPmCount": cyanY1731LMFe15MinPmCount,
       "cyanY1731LMFe15MinPmTimestamp": cyanY1731LMFe15MinPmTimestamp,
       "cyanY1731LMRatioNe15MinHighValue": cyanY1731LMRatioNe15MinHighValue,
       "cyanY1731LMRatioNe15MinLowValue": cyanY1731LMRatioNe15MinLowValue,
       "cyanY1731LMRatioNe15MinAvgValue": cyanY1731LMRatioNe15MinAvgValue,
       "cyanY1731LMRatioNe15MinTimestamp": cyanY1731LMRatioNe15MinTimestamp,
       "cyanY1731LMRatioFe15MinHighValue": cyanY1731LMRatioFe15MinHighValue,
       "cyanY1731LMRatioFe15MinLowValue": cyanY1731LMRatioFe15MinLowValue,
       "cyanY1731LMRatioFe15MinAvgValue": cyanY1731LMRatioFe15MinAvgValue,
       "cyanY1731LMRatioFe15MinTimestamp": cyanY1731LMRatioFe15MinTimestamp,
       "cyanY1731DMTable": cyanY1731DMTable,
       "cyanY1731DMEntry": cyanY1731DMEntry,
       "cyanY1731DMShelfId": cyanY1731DMShelfId,
       "cyanY1731DMModuleId": cyanY1731DMModuleId,
       "cyanY1731DMMepId": cyanY1731DMMepId,
       "cyanY1731DMMepIndex": cyanY1731DMMepIndex,
       "cyanY1731DMTwoWayDelay15MinHighValue": cyanY1731DMTwoWayDelay15MinHighValue,
       "cyanY1731DMTwoWayDelay15MinLowValue": cyanY1731DMTwoWayDelay15MinLowValue,
       "cyanY1731DMTwoWayDelay15MinAvgValue": cyanY1731DMTwoWayDelay15MinAvgValue,
       "cyanY1731DMTwoWayDelay15MinTimestamp": cyanY1731DMTwoWayDelay15MinTimestamp,
       "cyanY1731DMTwoWayDelayVar15MinHighValue": cyanY1731DMTwoWayDelayVar15MinHighValue,
       "cyanY1731DMTwoWayDelayVar15MinLowValue": cyanY1731DMTwoWayDelayVar15MinLowValue,
       "cyanY1731DMTwoWayDelayVar15MinAvgValue": cyanY1731DMTwoWayDelayVar15MinAvgValue,
       "cyanY1731DMTwoWayDelayVar15MinTimestamp": cyanY1731DMTwoWayDelayVar15MinTimestamp,
       "cyanY1731MepConfigObjectGroup": cyanY1731MepConfigObjectGroup,
       "cyanY1731MepConfigCompliance": cyanY1731MepConfigCompliance,
       "cyanY1731LMObjectGroup": cyanY1731LMObjectGroup,
       "cyanY1731LMCompliance": cyanY1731LMCompliance,
       "cyanY1731DMObjectGroup": cyanY1731DMObjectGroup,
       "cyanY1731DMCompliance": cyanY1731DMCompliance}
)
