# SNMP MIB module (LANCITY-MCNS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/LANCITY-MCNS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:16:59 2024
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

(dot1dTpPort,) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "dot1dTpPort")

(docsDevEvText,
 docsDevNmAccessEntry) = mibBuilder.importSymbols(
    "DOCS-CABLE-DEVICE-MIB",
    "docsDevEvText",
    "docsDevNmAccessEntry")

(TenthdBmV,) = mibBuilder.importSymbols(
    "DOCS-IF-MIB",
    "TenthdBmV")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(lancity,) = mibBuilder.importSymbols(
    "LANCITY-MIB",
    "lancity")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

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
 MacAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

lancityMcnsMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 482, 60)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_LancityMcnsProducts_ObjectIdentity = ObjectIdentity
lancityMcnsProducts = _LancityMcnsProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 482, 60, 1)
)
_LancityMcnsProdIdCMTS_ObjectIdentity = ObjectIdentity
lancityMcnsProdIdCMTS = _LancityMcnsProdIdCMTS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 482, 60, 1, 1)
)
_LancityMcnsProdIdCM_ObjectIdentity = ObjectIdentity
lancityMcnsProdIdCM = _LancityMcnsProdIdCM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 482, 60, 1, 2)
)
_Lccmtsif_ObjectIdentity = ObjectIdentity
lccmtsif = _Lccmtsif_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 482, 60, 2)
)
_LcCmtsUpstreamTable_Object = MibTable
lcCmtsUpstreamTable = _LcCmtsUpstreamTable_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 2, 1)
)
if mibBuilder.loadTexts:
    lcCmtsUpstreamTable.setStatus("current")
_LcCmtsUpstreamEntry_Object = MibTableRow
lcCmtsUpstreamEntry = _LcCmtsUpstreamEntry_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 2, 1, 1)
)
lcCmtsUpstreamEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    lcCmtsUpstreamEntry.setStatus("current")
_LcCmtsUpMinimumMapSize_Type = Integer32
_LcCmtsUpMinimumMapSize_Object = MibTableColumn
lcCmtsUpMinimumMapSize = _LcCmtsUpMinimumMapSize_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 2, 1, 1, 1),
    _LcCmtsUpMinimumMapSize_Type()
)
lcCmtsUpMinimumMapSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcCmtsUpMinimumMapSize.setStatus("current")
_LcCmtsUpMaximumMapSize_Type = Integer32
_LcCmtsUpMaximumMapSize_Object = MibTableColumn
lcCmtsUpMaximumMapSize = _LcCmtsUpMaximumMapSize_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 2, 1, 1, 2),
    _LcCmtsUpMaximumMapSize_Type()
)
lcCmtsUpMaximumMapSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcCmtsUpMaximumMapSize.setStatus("current")
_LcCmtsUpContentionPerMap_Type = Integer32
_LcCmtsUpContentionPerMap_Object = MibTableColumn
lcCmtsUpContentionPerMap = _LcCmtsUpContentionPerMap_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 2, 1, 1, 3),
    _LcCmtsUpContentionPerMap_Type()
)
lcCmtsUpContentionPerMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcCmtsUpContentionPerMap.setStatus("current")


class _LcCmtsUpRequestDataAllowed_Type(Integer32):
    """Custom type lcCmtsUpRequestDataAllowed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("adaptive", 3),
          ("allowed", 1),
          ("disallowed", 2))
    )


_LcCmtsUpRequestDataAllowed_Type.__name__ = "Integer32"
_LcCmtsUpRequestDataAllowed_Object = MibTableColumn
lcCmtsUpRequestDataAllowed = _LcCmtsUpRequestDataAllowed_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 2, 1, 1, 4),
    _LcCmtsUpRequestDataAllowed_Type()
)
lcCmtsUpRequestDataAllowed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcCmtsUpRequestDataAllowed.setStatus("current")
_LcCmtsUpMaxDataInContention_Type = Integer32
_LcCmtsUpMaxDataInContention_Object = MibTableColumn
lcCmtsUpMaxDataInContention = _LcCmtsUpMaxDataInContention_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 2, 1, 1, 5),
    _LcCmtsUpMaxDataInContention_Type()
)
lcCmtsUpMaxDataInContention.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcCmtsUpMaxDataInContention.setStatus("current")
_LcCmtsUpInitialRangingInterval_Type = Integer32
_LcCmtsUpInitialRangingInterval_Object = MibTableColumn
lcCmtsUpInitialRangingInterval = _LcCmtsUpInitialRangingInterval_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 2, 1, 1, 6),
    _LcCmtsUpInitialRangingInterval_Type()
)
lcCmtsUpInitialRangingInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcCmtsUpInitialRangingInterval.setStatus("current")
if mibBuilder.loadTexts:
    lcCmtsUpInitialRangingInterval.setUnits("microseconds")
_LcCmtsUpHighPriorityThreshold_Type = Integer32
_LcCmtsUpHighPriorityThreshold_Object = MibTableColumn
lcCmtsUpHighPriorityThreshold = _LcCmtsUpHighPriorityThreshold_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 2, 1, 1, 7),
    _LcCmtsUpHighPriorityThreshold_Type()
)
lcCmtsUpHighPriorityThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcCmtsUpHighPriorityThreshold.setStatus("current")


class _LcCmtsUpGuaranteedThreshold_Type(Integer32):
    """Custom type lcCmtsUpGuaranteedThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_LcCmtsUpGuaranteedThreshold_Type.__name__ = "Integer32"
_LcCmtsUpGuaranteedThreshold_Object = MibTableColumn
lcCmtsUpGuaranteedThreshold = _LcCmtsUpGuaranteedThreshold_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 2, 1, 1, 8),
    _LcCmtsUpGuaranteedThreshold_Type()
)
lcCmtsUpGuaranteedThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcCmtsUpGuaranteedThreshold.setStatus("current")
_LcCmtsUpPublicationDelay_Type = Integer32
_LcCmtsUpPublicationDelay_Object = MibTableColumn
lcCmtsUpPublicationDelay = _LcCmtsUpPublicationDelay_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 2, 1, 1, 9),
    _LcCmtsUpPublicationDelay_Type()
)
lcCmtsUpPublicationDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcCmtsUpPublicationDelay.setStatus("current")
if mibBuilder.loadTexts:
    lcCmtsUpPublicationDelay.setUnits("microseconds")
_LcCmtsUpNFlowControlledMaps_Type = Counter32
_LcCmtsUpNFlowControlledMaps_Object = MibTableColumn
lcCmtsUpNFlowControlledMaps = _LcCmtsUpNFlowControlledMaps_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 2, 1, 1, 10),
    _LcCmtsUpNFlowControlledMaps_Type()
)
lcCmtsUpNFlowControlledMaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcCmtsUpNFlowControlledMaps.setStatus("current")
_LcCmtsUpNNonFlowControlledMaps_Type = Counter32
_LcCmtsUpNNonFlowControlledMaps_Object = MibTableColumn
lcCmtsUpNNonFlowControlledMaps = _LcCmtsUpNNonFlowControlledMaps_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 2, 1, 1, 11),
    _LcCmtsUpNNonFlowControlledMaps_Type()
)
lcCmtsUpNNonFlowControlledMaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcCmtsUpNNonFlowControlledMaps.setStatus("current")
_LcCmtsUpChannelPower_Type = TenthdBmV
_LcCmtsUpChannelPower_Object = MibTableColumn
lcCmtsUpChannelPower = _LcCmtsUpChannelPower_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 2, 1, 1, 12),
    _LcCmtsUpChannelPower_Type()
)
lcCmtsUpChannelPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcCmtsUpChannelPower.setStatus("current")
_LcCmtsUpInputPowerWindow_Type = TenthdBmV
_LcCmtsUpInputPowerWindow_Object = MibTableColumn
lcCmtsUpInputPowerWindow = _LcCmtsUpInputPowerWindow_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 2, 1, 1, 13),
    _LcCmtsUpInputPowerWindow_Type()
)
lcCmtsUpInputPowerWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcCmtsUpInputPowerWindow.setStatus("current")
_LcCmtsCurrentTemp_Type = Integer32
_LcCmtsCurrentTemp_Object = MibScalar
lcCmtsCurrentTemp = _LcCmtsCurrentTemp_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 2, 2),
    _LcCmtsCurrentTemp_Type()
)
lcCmtsCurrentTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcCmtsCurrentTemp.setStatus("current")


class _LcCmtsHighTempThreshold_Type(Integer32):
    """Custom type lcCmtsHighTempThreshold based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_LcCmtsHighTempThreshold_Type.__name__ = "Integer32"
_LcCmtsHighTempThreshold_Object = MibScalar
lcCmtsHighTempThreshold = _LcCmtsHighTempThreshold_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 2, 3),
    _LcCmtsHighTempThreshold_Type()
)
lcCmtsHighTempThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcCmtsHighTempThreshold.setStatus("current")
_LccmtsUpstreamIngressAvoidance_ObjectIdentity = ObjectIdentity
lccmtsUpstreamIngressAvoidance = _LccmtsUpstreamIngressAvoidance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 482, 60, 2, 4)
)
_LcCmtsUpstreamIngressAvoidanceEnableTable_Object = MibTable
lcCmtsUpstreamIngressAvoidanceEnableTable = _LcCmtsUpstreamIngressAvoidanceEnableTable_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 2, 4, 1)
)
if mibBuilder.loadTexts:
    lcCmtsUpstreamIngressAvoidanceEnableTable.setStatus("current")
_LcCmtsIngressAvoidanceEnableEntry_Object = MibTableRow
lcCmtsIngressAvoidanceEnableEntry = _LcCmtsIngressAvoidanceEnableEntry_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 2, 4, 1, 1)
)
lcCmtsIngressAvoidanceEnableEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    lcCmtsIngressAvoidanceEnableEntry.setStatus("current")


class _LcCmtsIngressAvoidanceEnable_Type(Integer32):
    """Custom type lcCmtsIngressAvoidanceEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_LcCmtsIngressAvoidanceEnable_Type.__name__ = "Integer32"
_LcCmtsIngressAvoidanceEnable_Object = MibTableColumn
lcCmtsIngressAvoidanceEnable = _LcCmtsIngressAvoidanceEnable_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 2, 4, 1, 1, 1),
    _LcCmtsIngressAvoidanceEnable_Type()
)
lcCmtsIngressAvoidanceEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcCmtsIngressAvoidanceEnable.setStatus("current")


class _LcCmtsMetric1Enable_Type(Integer32):
    """Custom type lcCmtsMetric1Enable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_LcCmtsMetric1Enable_Type.__name__ = "Integer32"
_LcCmtsMetric1Enable_Object = MibTableColumn
lcCmtsMetric1Enable = _LcCmtsMetric1Enable_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 2, 4, 1, 1, 2),
    _LcCmtsMetric1Enable_Type()
)
lcCmtsMetric1Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcCmtsMetric1Enable.setStatus("current")
_LcCmtsIngressAvoidanceFrequencyConfigTable_Object = MibTable
lcCmtsIngressAvoidanceFrequencyConfigTable = _LcCmtsIngressAvoidanceFrequencyConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 2, 4, 2)
)
if mibBuilder.loadTexts:
    lcCmtsIngressAvoidanceFrequencyConfigTable.setStatus("current")
_LcCmtsIngressAvoidanceFrequencyConfigEntry_Object = MibTableRow
lcCmtsIngressAvoidanceFrequencyConfigEntry = _LcCmtsIngressAvoidanceFrequencyConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 2, 4, 2, 1)
)
lcCmtsIngressAvoidanceFrequencyConfigEntry.setIndexNames(
    (0, "LANCITY-MCNS-MIB", "lcCmtsCarrierPathIndex"),
    (0, "LANCITY-MCNS-MIB", "lcCmtsFreqConfigIndex"),
)
if mibBuilder.loadTexts:
    lcCmtsIngressAvoidanceFrequencyConfigEntry.setStatus("current")
_LcCmtsCarrierPathIndex_Type = Integer32
_LcCmtsCarrierPathIndex_Object = MibTableColumn
lcCmtsCarrierPathIndex = _LcCmtsCarrierPathIndex_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 2, 4, 2, 1, 1),
    _LcCmtsCarrierPathIndex_Type()
)
lcCmtsCarrierPathIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lcCmtsCarrierPathIndex.setStatus("current")
_LcCmtsFreqConfigIndex_Type = Integer32
_LcCmtsFreqConfigIndex_Object = MibTableColumn
lcCmtsFreqConfigIndex = _LcCmtsFreqConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 2, 4, 2, 1, 2),
    _LcCmtsFreqConfigIndex_Type()
)
lcCmtsFreqConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lcCmtsFreqConfigIndex.setStatus("current")


class _LcCmtsFreqAvailable_Type(Integer32):
    """Custom type lcCmtsFreqAvailable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_LcCmtsFreqAvailable_Type.__name__ = "Integer32"
_LcCmtsFreqAvailable_Object = MibTableColumn
lcCmtsFreqAvailable = _LcCmtsFreqAvailable_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 2, 4, 2, 1, 3),
    _LcCmtsFreqAvailable_Type()
)
lcCmtsFreqAvailable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcCmtsFreqAvailable.setStatus("current")
_LcCmtsStartFrequency_Type = Integer32
_LcCmtsStartFrequency_Object = MibTableColumn
lcCmtsStartFrequency = _LcCmtsStartFrequency_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 2, 4, 2, 1, 4),
    _LcCmtsStartFrequency_Type()
)
lcCmtsStartFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcCmtsStartFrequency.setStatus("current")
_LcCmtsStopFrequency_Type = Integer32
_LcCmtsStopFrequency_Object = MibTableColumn
lcCmtsStopFrequency = _LcCmtsStopFrequency_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 2, 4, 2, 1, 5),
    _LcCmtsStopFrequency_Type()
)
lcCmtsStopFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcCmtsStopFrequency.setStatus("current")
_LcCmtsIngressAvoidanceChangePrefTable_Object = MibTable
lcCmtsIngressAvoidanceChangePrefTable = _LcCmtsIngressAvoidanceChangePrefTable_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 2, 4, 3)
)
if mibBuilder.loadTexts:
    lcCmtsIngressAvoidanceChangePrefTable.setStatus("current")
_LcCmtsIngressAvoidanceChangePrefEntry_Object = MibTableRow
lcCmtsIngressAvoidanceChangePrefEntry = _LcCmtsIngressAvoidanceChangePrefEntry_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 2, 4, 3, 1)
)
lcCmtsIngressAvoidanceChangePrefEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    lcCmtsIngressAvoidanceChangePrefEntry.setStatus("current")


class _LcCmtsChangePreference_Type(Integer32):
    """Custom type lcCmtsChangePreference based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("frequency", 2),
          ("profile", 1))
    )


_LcCmtsChangePreference_Type.__name__ = "Integer32"
_LcCmtsChangePreference_Object = MibTableColumn
lcCmtsChangePreference = _LcCmtsChangePreference_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 2, 4, 3, 1, 1),
    _LcCmtsChangePreference_Type()
)
lcCmtsChangePreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcCmtsChangePreference.setStatus("current")
_LcCmtsIngressAvoidanceThresholdTable_Object = MibTable
lcCmtsIngressAvoidanceThresholdTable = _LcCmtsIngressAvoidanceThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 2, 4, 4)
)
if mibBuilder.loadTexts:
    lcCmtsIngressAvoidanceThresholdTable.setStatus("current")
_LcCmtsIngressAvoidanceThresholdEntry_Object = MibTableRow
lcCmtsIngressAvoidanceThresholdEntry = _LcCmtsIngressAvoidanceThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 2, 4, 4, 1)
)
lcCmtsIngressAvoidanceThresholdEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    lcCmtsIngressAvoidanceThresholdEntry.setStatus("current")
_LcCmtsMetric1GreenToYellow_Type = Integer32
_LcCmtsMetric1GreenToYellow_Object = MibTableColumn
lcCmtsMetric1GreenToYellow = _LcCmtsMetric1GreenToYellow_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 2, 4, 4, 1, 1),
    _LcCmtsMetric1GreenToYellow_Type()
)
lcCmtsMetric1GreenToYellow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcCmtsMetric1GreenToYellow.setStatus("current")
_LcCmtsMetric1YellowToRed_Type = Integer32
_LcCmtsMetric1YellowToRed_Object = MibTableColumn
lcCmtsMetric1YellowToRed = _LcCmtsMetric1YellowToRed_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 2, 4, 4, 1, 2),
    _LcCmtsMetric1YellowToRed_Type()
)
lcCmtsMetric1YellowToRed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcCmtsMetric1YellowToRed.setStatus("current")
_LcCmtsIngressAvoidanceProfileTable_Object = MibTable
lcCmtsIngressAvoidanceProfileTable = _LcCmtsIngressAvoidanceProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 2, 4, 5)
)
if mibBuilder.loadTexts:
    lcCmtsIngressAvoidanceProfileTable.setStatus("current")
_LcCmtsIngressAvoidanceProfileEntry_Object = MibTableRow
lcCmtsIngressAvoidanceProfileEntry = _LcCmtsIngressAvoidanceProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 2, 4, 5, 1)
)
lcCmtsIngressAvoidanceProfileEntry.setIndexNames(
    (0, "LANCITY-MCNS-MIB", "lcCmtsProfileCarrierPathIndex"),
    (0, "LANCITY-MCNS-MIB", "lcCmtsProfilePreference"),
)
if mibBuilder.loadTexts:
    lcCmtsIngressAvoidanceProfileEntry.setStatus("current")
_LcCmtsProfileCarrierPathIndex_Type = Integer32
_LcCmtsProfileCarrierPathIndex_Object = MibTableColumn
lcCmtsProfileCarrierPathIndex = _LcCmtsProfileCarrierPathIndex_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 2, 4, 5, 1, 1),
    _LcCmtsProfileCarrierPathIndex_Type()
)
lcCmtsProfileCarrierPathIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lcCmtsProfileCarrierPathIndex.setStatus("current")
_LcCmtsProfilePreference_Type = Integer32
_LcCmtsProfilePreference_Object = MibTableColumn
lcCmtsProfilePreference = _LcCmtsProfilePreference_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 2, 4, 5, 1, 2),
    _LcCmtsProfilePreference_Type()
)
lcCmtsProfilePreference.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lcCmtsProfilePreference.setStatus("current")


class _LcCmtsStatus_Type(Integer32):
    """Custom type lcCmtsStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_LcCmtsStatus_Type.__name__ = "Integer32"
_LcCmtsStatus_Object = MibTableColumn
lcCmtsStatus = _LcCmtsStatus_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 2, 4, 5, 1, 3),
    _LcCmtsStatus_Type()
)
lcCmtsStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcCmtsStatus.setStatus("current")
_LcCmtsTransmissionProfileIndex_Type = Integer32
_LcCmtsTransmissionProfileIndex_Object = MibTableColumn
lcCmtsTransmissionProfileIndex = _LcCmtsTransmissionProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 2, 4, 5, 1, 4),
    _LcCmtsTransmissionProfileIndex_Type()
)
lcCmtsTransmissionProfileIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcCmtsTransmissionProfileIndex.setStatus("current")
_LcCmtsIngressAvoidanceTxProfileTable_Object = MibTable
lcCmtsIngressAvoidanceTxProfileTable = _LcCmtsIngressAvoidanceTxProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 2, 4, 6)
)
if mibBuilder.loadTexts:
    lcCmtsIngressAvoidanceTxProfileTable.setStatus("current")
_LcCmtsIngressAvoidanceTxProfileEntry_Object = MibTableRow
lcCmtsIngressAvoidanceTxProfileEntry = _LcCmtsIngressAvoidanceTxProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 2, 4, 6, 1)
)
lcCmtsIngressAvoidanceTxProfileEntry.setIndexNames(
    (0, "LANCITY-MCNS-MIB", "lcCmtsTxProfileIndex"),
)
if mibBuilder.loadTexts:
    lcCmtsIngressAvoidanceTxProfileEntry.setStatus("current")
_LcCmtsTxProfileIndex_Type = Integer32
_LcCmtsTxProfileIndex_Object = MibTableColumn
lcCmtsTxProfileIndex = _LcCmtsTxProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 2, 4, 6, 1, 1),
    _LcCmtsTxProfileIndex_Type()
)
lcCmtsTxProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lcCmtsTxProfileIndex.setStatus("current")
_LcCmtsModulationProfileIndex_Type = Integer32
_LcCmtsModulationProfileIndex_Object = MibTableColumn
lcCmtsModulationProfileIndex = _LcCmtsModulationProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 2, 4, 6, 1, 2),
    _LcCmtsModulationProfileIndex_Type()
)
lcCmtsModulationProfileIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcCmtsModulationProfileIndex.setStatus("current")
_LcCmtsBandwidth_Type = Integer32
_LcCmtsBandwidth_Object = MibTableColumn
lcCmtsBandwidth = _LcCmtsBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 2, 4, 6, 1, 3),
    _LcCmtsBandwidth_Type()
)
lcCmtsBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcCmtsBandwidth.setStatus("current")
_LcCmtsCodingEfficiency_Type = Integer32
_LcCmtsCodingEfficiency_Object = MibTableColumn
lcCmtsCodingEfficiency = _LcCmtsCodingEfficiency_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 2, 4, 6, 1, 4),
    _LcCmtsCodingEfficiency_Type()
)
lcCmtsCodingEfficiency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcCmtsCodingEfficiency.setStatus("current")
_LcCmtsIngressAvoidanceMetricConfigTable_Object = MibTable
lcCmtsIngressAvoidanceMetricConfigTable = _LcCmtsIngressAvoidanceMetricConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 2, 4, 7)
)
if mibBuilder.loadTexts:
    lcCmtsIngressAvoidanceMetricConfigTable.setStatus("current")
_LcCmtsIngressAvoidanceMetricConfigEntry_Object = MibTableRow
lcCmtsIngressAvoidanceMetricConfigEntry = _LcCmtsIngressAvoidanceMetricConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 2, 4, 7, 1)
)
lcCmtsIngressAvoidanceMetricConfigEntry.setIndexNames(
    (0, "LANCITY-MCNS-MIB", "lcCmtsMetricIndex"),
)
if mibBuilder.loadTexts:
    lcCmtsIngressAvoidanceMetricConfigEntry.setStatus("current")
_LcCmtsMetricIndex_Type = Integer32
_LcCmtsMetricIndex_Object = MibTableColumn
lcCmtsMetricIndex = _LcCmtsMetricIndex_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 2, 4, 7, 1, 1),
    _LcCmtsMetricIndex_Type()
)
lcCmtsMetricIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lcCmtsMetricIndex.setStatus("current")
_LcCmtsAgingMultiplier_Type = Integer32
_LcCmtsAgingMultiplier_Object = MibTableColumn
lcCmtsAgingMultiplier = _LcCmtsAgingMultiplier_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 2, 4, 7, 1, 2),
    _LcCmtsAgingMultiplier_Type()
)
lcCmtsAgingMultiplier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcCmtsAgingMultiplier.setStatus("current")
_LcCmtsCalculationTimer_Type = Integer32
_LcCmtsCalculationTimer_Object = MibTableColumn
lcCmtsCalculationTimer = _LcCmtsCalculationTimer_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 2, 4, 7, 1, 3),
    _LcCmtsCalculationTimer_Type()
)
lcCmtsCalculationTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcCmtsCalculationTimer.setStatus("current")
_LcCmtsIngressAvoidanceFreqStatusTable_Object = MibTable
lcCmtsIngressAvoidanceFreqStatusTable = _LcCmtsIngressAvoidanceFreqStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 2, 4, 8)
)
if mibBuilder.loadTexts:
    lcCmtsIngressAvoidanceFreqStatusTable.setStatus("current")
_LcCmtsIngressAvoidanceFreqStatusEntry_Object = MibTableRow
lcCmtsIngressAvoidanceFreqStatusEntry = _LcCmtsIngressAvoidanceFreqStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 2, 4, 8, 1)
)
lcCmtsIngressAvoidanceFreqStatusEntry.setIndexNames(
    (0, "LANCITY-MCNS-MIB", "lcCmtsFreqStatusCarrierPathIndex"),
    (0, "LANCITY-MCNS-MIB", "lcCmtsFreqStatusFreqIndex"),
)
if mibBuilder.loadTexts:
    lcCmtsIngressAvoidanceFreqStatusEntry.setStatus("current")
_LcCmtsFreqStatusCarrierPathIndex_Type = Integer32
_LcCmtsFreqStatusCarrierPathIndex_Object = MibTableColumn
lcCmtsFreqStatusCarrierPathIndex = _LcCmtsFreqStatusCarrierPathIndex_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 2, 4, 8, 1, 1),
    _LcCmtsFreqStatusCarrierPathIndex_Type()
)
lcCmtsFreqStatusCarrierPathIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lcCmtsFreqStatusCarrierPathIndex.setStatus("current")
_LcCmtsFreqStatusFreqIndex_Type = Integer32
_LcCmtsFreqStatusFreqIndex_Object = MibTableColumn
lcCmtsFreqStatusFreqIndex = _LcCmtsFreqStatusFreqIndex_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 2, 4, 8, 1, 2),
    _LcCmtsFreqStatusFreqIndex_Type()
)
lcCmtsFreqStatusFreqIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lcCmtsFreqStatusFreqIndex.setStatus("current")
_LcCmtsFreqStatusFreq_Type = Integer32
_LcCmtsFreqStatusFreq_Object = MibTableColumn
lcCmtsFreqStatusFreq = _LcCmtsFreqStatusFreq_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 2, 4, 8, 1, 3),
    _LcCmtsFreqStatusFreq_Type()
)
lcCmtsFreqStatusFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcCmtsFreqStatusFreq.setStatus("current")


class _LcCmtsFreqStatusFc_Type(Integer32):
    """Custom type lcCmtsFreqStatusFc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_LcCmtsFreqStatusFc_Type.__name__ = "Integer32"
_LcCmtsFreqStatusFc_Object = MibTableColumn
lcCmtsFreqStatusFc = _LcCmtsFreqStatusFc_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 2, 4, 8, 1, 4),
    _LcCmtsFreqStatusFc_Type()
)
lcCmtsFreqStatusFc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcCmtsFreqStatusFc.setStatus("current")


class _LcCmtsFreqStatusAvailable_Type(Integer32):
    """Custom type lcCmtsFreqStatusAvailable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inuse", 2),
          ("no", 0),
          ("reserved", 3),
          ("yes", 1))
    )


_LcCmtsFreqStatusAvailable_Type.__name__ = "Integer32"
_LcCmtsFreqStatusAvailable_Object = MibTableColumn
lcCmtsFreqStatusAvailable = _LcCmtsFreqStatusAvailable_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 2, 4, 8, 1, 5),
    _LcCmtsFreqStatusAvailable_Type()
)
lcCmtsFreqStatusAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcCmtsFreqStatusAvailable.setStatus("current")


class _LcCmtsFreqStatusStatus_Type(Integer32):
    """Custom type lcCmtsFreqStatusStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("unk", 0)
    )


_LcCmtsFreqStatusStatus_Type.__name__ = "Integer32"
_LcCmtsFreqStatusStatus_Object = MibTableColumn
lcCmtsFreqStatusStatus = _LcCmtsFreqStatusStatus_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 2, 4, 8, 1, 6),
    _LcCmtsFreqStatusStatus_Type()
)
lcCmtsFreqStatusStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcCmtsFreqStatusStatus.setStatus("current")
_LcCmtsFreqStatusTimeLastUsed_Type = TimeTicks
_LcCmtsFreqStatusTimeLastUsed_Object = MibTableColumn
lcCmtsFreqStatusTimeLastUsed = _LcCmtsFreqStatusTimeLastUsed_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 2, 4, 8, 1, 7),
    _LcCmtsFreqStatusTimeLastUsed_Type()
)
lcCmtsFreqStatusTimeLastUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcCmtsFreqStatusTimeLastUsed.setStatus("current")
_LcCmtsFreqStatusUpTime_Type = TimeTicks
_LcCmtsFreqStatusUpTime_Object = MibTableColumn
lcCmtsFreqStatusUpTime = _LcCmtsFreqStatusUpTime_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 2, 4, 8, 1, 8),
    _LcCmtsFreqStatusUpTime_Type()
)
lcCmtsFreqStatusUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcCmtsFreqStatusUpTime.setStatus("current")
_LcCmtsUpstreamIngressAvoidanceHealthTable_Object = MibTable
lcCmtsUpstreamIngressAvoidanceHealthTable = _LcCmtsUpstreamIngressAvoidanceHealthTable_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 2, 4, 9)
)
if mibBuilder.loadTexts:
    lcCmtsUpstreamIngressAvoidanceHealthTable.setStatus("current")
_LcCmtsIngressAvoidanceHealthEntry_Object = MibTableRow
lcCmtsIngressAvoidanceHealthEntry = _LcCmtsIngressAvoidanceHealthEntry_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 2, 4, 9, 1)
)
lcCmtsIngressAvoidanceHealthEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    lcCmtsIngressAvoidanceHealthEntry.setStatus("current")
_LcCmtsHealthProfile_Type = Integer32
_LcCmtsHealthProfile_Object = MibTableColumn
lcCmtsHealthProfile = _LcCmtsHealthProfile_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 2, 4, 9, 1, 1),
    _LcCmtsHealthProfile_Type()
)
lcCmtsHealthProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcCmtsHealthProfile.setStatus("current")
_LcCmtsHealthFc_Type = Integer32
_LcCmtsHealthFc_Object = MibTableColumn
lcCmtsHealthFc = _LcCmtsHealthFc_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 2, 4, 9, 1, 2),
    _LcCmtsHealthFc_Type()
)
lcCmtsHealthFc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcCmtsHealthFc.setStatus("current")
_LcCmtsHealthUpTime_Type = TimeTicks
_LcCmtsHealthUpTime_Object = MibTableColumn
lcCmtsHealthUpTime = _LcCmtsHealthUpTime_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 2, 4, 9, 1, 3),
    _LcCmtsHealthUpTime_Type()
)
lcCmtsHealthUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcCmtsHealthUpTime.setStatus("current")


class _LcCmtsMetric1Status_Type(Integer32):
    """Custom type lcCmtsMetric1Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("green", 2),
          ("red", 0),
          ("yellow", 1))
    )


_LcCmtsMetric1Status_Type.__name__ = "Integer32"
_LcCmtsMetric1Status_Object = MibTableColumn
lcCmtsMetric1Status = _LcCmtsMetric1Status_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 2, 4, 9, 1, 4),
    _LcCmtsMetric1Status_Type()
)
lcCmtsMetric1Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcCmtsMetric1Status.setStatus("current")
_LcCmtsMetric1Value_Type = Integer32
_LcCmtsMetric1Value_Object = MibTableColumn
lcCmtsMetric1Value = _LcCmtsMetric1Value_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 2, 4, 9, 1, 5),
    _LcCmtsMetric1Value_Type()
)
lcCmtsMetric1Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcCmtsMetric1Value.setStatus("current")
_LcCmtsMultiUsConfigTable_Object = MibTable
lcCmtsMultiUsConfigTable = _LcCmtsMultiUsConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 2, 5)
)
if mibBuilder.loadTexts:
    lcCmtsMultiUsConfigTable.setStatus("current")
_LcCmtsMultiUsConfigEntry_Object = MibTableRow
lcCmtsMultiUsConfigEntry = _LcCmtsMultiUsConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 2, 5, 1)
)
lcCmtsMultiUsConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    lcCmtsMultiUsConfigEntry.setStatus("current")
_LcCmtsCarrierPath_Type = Integer32
_LcCmtsCarrierPath_Object = MibTableColumn
lcCmtsCarrierPath = _LcCmtsCarrierPath_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 2, 5, 1, 1),
    _LcCmtsCarrierPath_Type()
)
lcCmtsCarrierPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcCmtsCarrierPath.setStatus("current")
_LcCmtsChannelGroup_Type = Integer32
_LcCmtsChannelGroup_Object = MibTableColumn
lcCmtsChannelGroup = _LcCmtsChannelGroup_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 2, 5, 1, 2),
    _LcCmtsChannelGroup_Type()
)
lcCmtsChannelGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcCmtsChannelGroup.setStatus("current")
_LcCmtsFrontFanOn_Type = TruthValue
_LcCmtsFrontFanOn_Object = MibScalar
lcCmtsFrontFanOn = _LcCmtsFrontFanOn_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 2, 6),
    _LcCmtsFrontFanOn_Type()
)
lcCmtsFrontFanOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcCmtsFrontFanOn.setStatus("current")
_LcCmtsMiddleFanOn_Type = TruthValue
_LcCmtsMiddleFanOn_Object = MibScalar
lcCmtsMiddleFanOn = _LcCmtsMiddleFanOn_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 2, 7),
    _LcCmtsMiddleFanOn_Type()
)
lcCmtsMiddleFanOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcCmtsMiddleFanOn.setStatus("current")
_LcCmtsBackFanOn_Type = TruthValue
_LcCmtsBackFanOn_Object = MibScalar
lcCmtsBackFanOn = _LcCmtsBackFanOn_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 2, 8),
    _LcCmtsBackFanOn_Type()
)
lcCmtsBackFanOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcCmtsBackFanOn.setStatus("current")
_Lccmtsifconfig_ObjectIdentity = ObjectIdentity
lccmtsifconfig = _Lccmtsifconfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 482, 60, 2, 9)
)


class _LcCmtsAnnex_Type(Integer32):
    """Custom type lcCmtsAnnex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("annexA", 0),
          ("annexB", 1))
    )


_LcCmtsAnnex_Type.__name__ = "Integer32"
_LcCmtsAnnex_Object = MibScalar
lcCmtsAnnex = _LcCmtsAnnex_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 2, 9, 1),
    _LcCmtsAnnex_Type()
)
lcCmtsAnnex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcCmtsAnnex.setStatus("current")


class _LcCmtsFrequencySplit_Type(Integer32):
    """Custom type lcCmtsFrequencySplit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("euroDOCSIS", 1),
          ("standard", 0))
    )


_LcCmtsFrequencySplit_Type.__name__ = "Integer32"
_LcCmtsFrequencySplit_Object = MibScalar
lcCmtsFrequencySplit = _LcCmtsFrequencySplit_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 2, 9, 2),
    _LcCmtsFrequencySplit_Type()
)
lcCmtsFrequencySplit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcCmtsFrequencySplit.setStatus("current")
_LcEvSyslog2_Type = IpAddress
_LcEvSyslog2_Object = MibScalar
lcEvSyslog2 = _LcEvSyslog2_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 2, 10),
    _LcEvSyslog2_Type()
)
lcEvSyslog2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcEvSyslog2.setStatus("current")
_LcEvSyslog3_Type = IpAddress
_LcEvSyslog3_Object = MibScalar
lcEvSyslog3 = _LcEvSyslog3_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 2, 11),
    _LcEvSyslog3_Type()
)
lcEvSyslog3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcEvSyslog3.setStatus("current")
_LcCpeMacToCmMacTable_Object = MibTable
lcCpeMacToCmMacTable = _LcCpeMacToCmMacTable_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 2, 16)
)
if mibBuilder.loadTexts:
    lcCpeMacToCmMacTable.setStatus("current")
_LcCpeMacToCmMacEntry_Object = MibTableRow
lcCpeMacToCmMacEntry = _LcCpeMacToCmMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 2, 16, 1)
)
lcCpeMacToCmMacEntry.setIndexNames(
    (0, "LANCITY-MCNS-MIB", "lcCpeMac"),
)
if mibBuilder.loadTexts:
    lcCpeMacToCmMacEntry.setStatus("current")
_LcCpeMac_Type = MacAddress
_LcCpeMac_Object = MibTableColumn
lcCpeMac = _LcCpeMac_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 2, 16, 1, 1),
    _LcCpeMac_Type()
)
lcCpeMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lcCpeMac.setStatus("current")
_LcCmMac_Type = MacAddress
_LcCmMac_Object = MibTableColumn
lcCmMac = _LcCmMac_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 2, 16, 1, 2),
    _LcCmMac_Type()
)
lcCmMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcCmMac.setStatus("current")
_LcCmCountsTable_Object = MibTable
lcCmCountsTable = _LcCmCountsTable_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 2, 19)
)
if mibBuilder.loadTexts:
    lcCmCountsTable.setStatus("current")
_LcCmCountsEntry_Object = MibTableRow
lcCmCountsEntry = _LcCmCountsEntry_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 2, 19, 1)
)
lcCmCountsEntry.setIndexNames(
    (0, "LANCITY-MCNS-MIB", "lcCmCountsRowNum"),
)
if mibBuilder.loadTexts:
    lcCmCountsEntry.setStatus("current")
_LcCmCountsRowNum_Type = Counter32
_LcCmCountsRowNum_Object = MibTableColumn
lcCmCountsRowNum = _LcCmCountsRowNum_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 2, 19, 1, 1),
    _LcCmCountsRowNum_Type()
)
lcCmCountsRowNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lcCmCountsRowNum.setStatus("current")
_LcActiveCmCounts_Type = Counter32
_LcActiveCmCounts_Object = MibTableColumn
lcActiveCmCounts = _LcActiveCmCounts_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 2, 19, 1, 2),
    _LcActiveCmCounts_Type()
)
lcActiveCmCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcActiveCmCounts.setStatus("current")
_LcRegisteredCmCounts_Type = Counter32
_LcRegisteredCmCounts_Object = MibTableColumn
lcRegisteredCmCounts = _LcRegisteredCmCounts_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 2, 19, 1, 3),
    _LcRegisteredCmCounts_Type()
)
lcRegisteredCmCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcRegisteredCmCounts.setStatus("current")
_Lccmif_ObjectIdentity = ObjectIdentity
lccmif = _Lccmif_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 482, 60, 3)
)
_Lcifcommon_ObjectIdentity = ObjectIdentity
lcifcommon = _Lcifcommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 482, 60, 4)
)
_Lccmtsdevice_ObjectIdentity = ObjectIdentity
lccmtsdevice = _Lccmtsdevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 482, 60, 5)
)
_LccmtsProvisioning_ObjectIdentity = ObjectIdentity
lccmtsProvisioning = _LccmtsProvisioning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 482, 60, 5, 1)
)


class _LcProvisioningControl_Type(Integer32):
    """Custom type lcProvisioningControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("use-dhcp", 2),
          ("use-dhcp-and-tftp", 1),
          ("use-nvram", 4),
          ("use-tftp", 3))
    )


_LcProvisioningControl_Type.__name__ = "Integer32"
_LcProvisioningControl_Object = MibScalar
lcProvisioningControl = _LcProvisioningControl_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 5, 1, 1),
    _LcProvisioningControl_Type()
)
lcProvisioningControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcProvisioningControl.setStatus("current")
_LcConfigIpAddress_Type = IpAddress
_LcConfigIpAddress_Object = MibScalar
lcConfigIpAddress = _LcConfigIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 5, 1, 2),
    _LcConfigIpAddress_Type()
)
lcConfigIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcConfigIpAddress.setStatus("current")
_LcConfigIpSubnet_Type = IpAddress
_LcConfigIpSubnet_Object = MibScalar
lcConfigIpSubnet = _LcConfigIpSubnet_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 5, 1, 3),
    _LcConfigIpSubnet_Type()
)
lcConfigIpSubnet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcConfigIpSubnet.setStatus("current")
_LcConfigIpGateway_Type = IpAddress
_LcConfigIpGateway_Object = MibScalar
lcConfigIpGateway = _LcConfigIpGateway_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 5, 1, 4),
    _LcConfigIpGateway_Type()
)
lcConfigIpGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcConfigIpGateway.setStatus("current")
_LcConfigTftpAddress_Type = IpAddress
_LcConfigTftpAddress_Object = MibScalar
lcConfigTftpAddress = _LcConfigTftpAddress_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 5, 1, 5),
    _LcConfigTftpAddress_Type()
)
lcConfigTftpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcConfigTftpAddress.setStatus("current")


class _LcConfigTftpFilename_Type(DisplayString):
    """Custom type lcConfigTftpFilename based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_LcConfigTftpFilename_Type.__name__ = "DisplayString"
_LcConfigTftpFilename_Object = MibScalar
lcConfigTftpFilename = _LcConfigTftpFilename_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 5, 1, 6),
    _LcConfigTftpFilename_Type()
)
lcConfigTftpFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcConfigTftpFilename.setStatus("current")
_LcConfigTimeServerAddress_Type = IpAddress
_LcConfigTimeServerAddress_Object = MibScalar
lcConfigTimeServerAddress = _LcConfigTimeServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 5, 1, 7),
    _LcConfigTimeServerAddress_Type()
)
lcConfigTimeServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcConfigTimeServerAddress.setStatus("current")
_LcConfigTimeoffset_Type = Integer32
_LcConfigTimeoffset_Object = MibScalar
lcConfigTimeoffset = _LcConfigTimeoffset_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 5, 1, 8),
    _LcConfigTimeoffset_Type()
)
lcConfigTimeoffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcConfigTimeoffset.setStatus("current")
_LcConfigSNTPAddress_Type = IpAddress
_LcConfigSNTPAddress_Object = MibScalar
lcConfigSNTPAddress = _LcConfigSNTPAddress_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 5, 1, 9),
    _LcConfigSNTPAddress_Type()
)
lcConfigSNTPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcConfigSNTPAddress.setStatus("current")
_LcSerialPortTable_Object = MibTable
lcSerialPortTable = _LcSerialPortTable_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 5, 2)
)
if mibBuilder.loadTexts:
    lcSerialPortTable.setStatus("current")
_LcSerialPortEntry_Object = MibTableRow
lcSerialPortEntry = _LcSerialPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 5, 2, 1)
)
lcSerialPortEntry.setIndexNames(
    (0, "LANCITY-MCNS-MIB", "lcSerialPortNumber"),
)
if mibBuilder.loadTexts:
    lcSerialPortEntry.setStatus("current")
_LcSerialPortNumber_Type = Integer32
_LcSerialPortNumber_Object = MibTableColumn
lcSerialPortNumber = _LcSerialPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 5, 2, 1, 1),
    _LcSerialPortNumber_Type()
)
lcSerialPortNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lcSerialPortNumber.setStatus("current")


class _LcSerialPortBaudRate_Type(Integer32):
    """Custom type lcSerialPortBaudRate based on Integer32"""
    defaultValue = 9600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1200,
              2400,
              4800,
              7200,
              9600,
              12000,
              14400,
              19200,
              28800,
              38400,
              57600,
              64000,
              76800,
              96000,
              115200)
        )
    )
    namedValues = NamedValues(
        *(("baudrate115k", 115200),
          ("baudrate12000b", 12000),
          ("baudrate1200b", 1200),
          ("baudrate14400b", 14400),
          ("baudrate19200b", 19200),
          ("baudrate2400b", 2400),
          ("baudrate28800b", 28800),
          ("baudrate38k", 38400),
          ("baudrate4800b", 4800),
          ("baudrate56k", 57600),
          ("baudrate64k", 64000),
          ("baudrate7200b", 7200),
          ("baudrate76k", 76800),
          ("baudrate9600b", 9600),
          ("baudrate96k", 96000))
    )


_LcSerialPortBaudRate_Type.__name__ = "Integer32"
_LcSerialPortBaudRate_Object = MibTableColumn
lcSerialPortBaudRate = _LcSerialPortBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 5, 2, 1, 2),
    _LcSerialPortBaudRate_Type()
)
lcSerialPortBaudRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcSerialPortBaudRate.setStatus("current")


class _LcSerialPortDataBits_Type(Integer32):
    """Custom type lcSerialPortDataBits based on Integer32"""
    defaultValue = 8


_LcSerialPortDataBits_Object = MibTableColumn
lcSerialPortDataBits = _LcSerialPortDataBits_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 5, 2, 1, 3),
    _LcSerialPortDataBits_Type()
)
lcSerialPortDataBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcSerialPortDataBits.setStatus("current")


class _LcSerialPortParity_Type(Integer32):
    """Custom type lcSerialPortParity based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("even", 3),
          ("none", 1),
          ("odd", 2))
    )


_LcSerialPortParity_Type.__name__ = "Integer32"
_LcSerialPortParity_Object = MibTableColumn
lcSerialPortParity = _LcSerialPortParity_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 5, 2, 1, 4),
    _LcSerialPortParity_Type()
)
lcSerialPortParity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcSerialPortParity.setStatus("current")


class _LcSerialPortStopBits_Type(Integer32):
    """Custom type lcSerialPortStopBits based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("s15bit", 2),
          ("s1bit", 1),
          ("s2bit", 3))
    )


_LcSerialPortStopBits_Type.__name__ = "Integer32"
_LcSerialPortStopBits_Object = MibTableColumn
lcSerialPortStopBits = _LcSerialPortStopBits_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 5, 2, 1, 5),
    _LcSerialPortStopBits_Type()
)
lcSerialPortStopBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcSerialPortStopBits.setStatus("current")


class _LcSerialPortModemEnable_Type(Integer32):
    """Custom type lcSerialPortModemEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_LcSerialPortModemEnable_Type.__name__ = "Integer32"
_LcSerialPortModemEnable_Object = MibTableColumn
lcSerialPortModemEnable = _LcSerialPortModemEnable_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 5, 2, 1, 6),
    _LcSerialPortModemEnable_Type()
)
lcSerialPortModemEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcSerialPortModemEnable.setStatus("current")
_LcModemVendorTable_Object = MibTable
lcModemVendorTable = _LcModemVendorTable_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 5, 3)
)
if mibBuilder.loadTexts:
    lcModemVendorTable.setStatus("current")
_LcModemVendorEntry_Object = MibTableRow
lcModemVendorEntry = _LcModemVendorEntry_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 5, 3, 1)
)
lcModemVendorEntry.setIndexNames(
    (0, "LANCITY-MCNS-MIB", "lcModemVendorIndex"),
)
if mibBuilder.loadTexts:
    lcModemVendorEntry.setStatus("current")
_LcModemVendorIndex_Type = Integer32
_LcModemVendorIndex_Object = MibTableColumn
lcModemVendorIndex = _LcModemVendorIndex_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 5, 3, 1, 1),
    _LcModemVendorIndex_Type()
)
lcModemVendorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lcModemVendorIndex.setStatus("current")
_LcModemVendorControl_Type = RowStatus
_LcModemVendorControl_Object = MibTableColumn
lcModemVendorControl = _LcModemVendorControl_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 5, 3, 1, 2),
    _LcModemVendorControl_Type()
)
lcModemVendorControl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lcModemVendorControl.setStatus("current")
_LcModemVendorMacAddress_Type = MacAddress
_LcModemVendorMacAddress_Object = MibTableColumn
lcModemVendorMacAddress = _LcModemVendorMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 5, 3, 1, 3),
    _LcModemVendorMacAddress_Type()
)
lcModemVendorMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lcModemVendorMacAddress.setStatus("current")


class _LcModemVendorMask_Type(MacAddress):
    """Custom type lcModemVendorMask based on MacAddress"""
    defaultHexValue = "ffffff000000"


_LcModemVendorMask_Object = MibTableColumn
lcModemVendorMask = _LcModemVendorMask_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 5, 3, 1, 4),
    _LcModemVendorMask_Type()
)
lcModemVendorMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lcModemVendorMask.setStatus("current")
_LccmtsDPStatistics_ObjectIdentity = ObjectIdentity
lccmtsDPStatistics = _LccmtsDPStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 482, 60, 5, 4)
)
_LcDPStatisticsInterval_Type = Integer32
_LcDPStatisticsInterval_Object = MibScalar
lcDPStatisticsInterval = _LcDPStatisticsInterval_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 5, 4, 1),
    _LcDPStatisticsInterval_Type()
)
lcDPStatisticsInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcDPStatisticsInterval.setStatus("current")
_LcDPStatisticsTable_Object = MibTable
lcDPStatisticsTable = _LcDPStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 5, 4, 2)
)
if mibBuilder.loadTexts:
    lcDPStatisticsTable.setStatus("current")
_LcDPStatisticsEntry_Object = MibTableRow
lcDPStatisticsEntry = _LcDPStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 5, 4, 2, 1)
)
lcDPStatisticsEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dTpPort"),
)
if mibBuilder.loadTexts:
    lcDPStatisticsEntry.setStatus("current")
_LcDPStatisticsTxFrameRate_Type = Integer32
_LcDPStatisticsTxFrameRate_Object = MibTableColumn
lcDPStatisticsTxFrameRate = _LcDPStatisticsTxFrameRate_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 5, 4, 2, 1, 1),
    _LcDPStatisticsTxFrameRate_Type()
)
lcDPStatisticsTxFrameRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcDPStatisticsTxFrameRate.setStatus("current")
_LcDPStatisticsRxFrameRate_Type = Integer32
_LcDPStatisticsRxFrameRate_Object = MibTableColumn
lcDPStatisticsRxFrameRate = _LcDPStatisticsRxFrameRate_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 5, 4, 2, 1, 2),
    _LcDPStatisticsRxFrameRate_Type()
)
lcDPStatisticsRxFrameRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcDPStatisticsRxFrameRate.setStatus("current")
_LcDPStatisticsTxOctetRate_Type = Integer32
_LcDPStatisticsTxOctetRate_Object = MibTableColumn
lcDPStatisticsTxOctetRate = _LcDPStatisticsTxOctetRate_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 5, 4, 2, 1, 3),
    _LcDPStatisticsTxOctetRate_Type()
)
lcDPStatisticsTxOctetRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcDPStatisticsTxOctetRate.setStatus("current")
_LcDPStatisticsRxOctetRate_Type = Integer32
_LcDPStatisticsRxOctetRate_Object = MibTableColumn
lcDPStatisticsRxOctetRate = _LcDPStatisticsRxOctetRate_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 5, 4, 2, 1, 4),
    _LcDPStatisticsRxOctetRate_Type()
)
lcDPStatisticsRxOctetRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcDPStatisticsRxOctetRate.setStatus("current")
_LccmtsDPConfiguration_ObjectIdentity = ObjectIdentity
lccmtsDPConfiguration = _LccmtsDPConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 482, 60, 5, 5)
)


class _LcForwardingMode_Type(Integer32):
    """Custom type lcForwardingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dhcp-arp", 2),
          ("none", 1))
    )


_LcForwardingMode_Type.__name__ = "Integer32"
_LcForwardingMode_Object = MibScalar
lcForwardingMode = _LcForwardingMode_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 5, 5, 1),
    _LcForwardingMode_Type()
)
lcForwardingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcForwardingMode.setStatus("current")


class _LcProxyArp_Type(Integer32):
    """Custom type lcProxyArp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_LcProxyArp_Type.__name__ = "Integer32"
_LcProxyArp_Object = MibScalar
lcProxyArp = _LcProxyArp_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 5, 5, 2),
    _LcProxyArp_Type()
)
lcProxyArp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcProxyArp.setStatus("current")
_LcProxyArpTimeout_Type = Integer32
_LcProxyArpTimeout_Object = MibScalar
lcProxyArpTimeout = _LcProxyArpTimeout_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 5, 5, 3),
    _LcProxyArpTimeout_Type()
)
lcProxyArpTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcProxyArpTimeout.setStatus("current")


class _LcArpSpoofingProtection_Type(Integer32):
    """Custom type lcArpSpoofingProtection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_LcArpSpoofingProtection_Type.__name__ = "Integer32"
_LcArpSpoofingProtection_Object = MibScalar
lcArpSpoofingProtection = _LcArpSpoofingProtection_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 5, 5, 4),
    _LcArpSpoofingProtection_Type()
)
lcArpSpoofingProtection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcArpSpoofingProtection.setStatus("current")


class _LcFunnelMode_Type(Integer32):
    """Custom type lcFunnelMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_LcFunnelMode_Type.__name__ = "Integer32"
_LcFunnelMode_Object = MibScalar
lcFunnelMode = _LcFunnelMode_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 5, 5, 5),
    _LcFunnelMode_Type()
)
lcFunnelMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcFunnelMode.setStatus("current")


class _LcDeregCmAgeTime_Type(Integer32):
    """Custom type lcDeregCmAgeTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 432000),
    )


_LcDeregCmAgeTime_Type.__name__ = "Integer32"
_LcDeregCmAgeTime_Object = MibScalar
lcDeregCmAgeTime = _LcDeregCmAgeTime_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 5, 5, 6),
    _LcDeregCmAgeTime_Type()
)
lcDeregCmAgeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcDeregCmAgeTime.setStatus("current")
if mibBuilder.loadTexts:
    lcDeregCmAgeTime.setUnits("seconds")


class _LcRngNotRegCmAgeTime_Type(Integer32):
    """Custom type lcRngNotRegCmAgeTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 432000),
    )


_LcRngNotRegCmAgeTime_Type.__name__ = "Integer32"
_LcRngNotRegCmAgeTime_Object = MibScalar
lcRngNotRegCmAgeTime = _LcRngNotRegCmAgeTime_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 5, 5, 7),
    _LcRngNotRegCmAgeTime_Type()
)
lcRngNotRegCmAgeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcRngNotRegCmAgeTime.setStatus("current")
if mibBuilder.loadTexts:
    lcRngNotRegCmAgeTime.setUnits("seconds")


class _LcUsedot1dTpAgingTime_Type(Integer32):
    """Custom type lcUsedot1dTpAgingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_LcUsedot1dTpAgingTime_Type.__name__ = "Integer32"
_LcUsedot1dTpAgingTime_Object = MibScalar
lcUsedot1dTpAgingTime = _LcUsedot1dTpAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 5, 5, 8),
    _LcUsedot1dTpAgingTime_Type()
)
lcUsedot1dTpAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcUsedot1dTpAgingTime.setStatus("current")
_LccmtsHwRevisions_ObjectIdentity = ObjectIdentity
lccmtsHwRevisions = _LccmtsHwRevisions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 482, 60, 5, 6)
)
_LccmtsHwRevArbCPLD_Type = Integer32
_LccmtsHwRevArbCPLD_Object = MibScalar
lccmtsHwRevArbCPLD = _LccmtsHwRevArbCPLD_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 5, 6, 1),
    _LccmtsHwRevArbCPLD_Type()
)
lccmtsHwRevArbCPLD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lccmtsHwRevArbCPLD.setStatus("current")
_LccmtsHwRevTxCPLD_Type = Integer32
_LccmtsHwRevTxCPLD_Object = MibScalar
lccmtsHwRevTxCPLD = _LccmtsHwRevTxCPLD_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 5, 6, 2),
    _LccmtsHwRevTxCPLD_Type()
)
lccmtsHwRevTxCPLD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lccmtsHwRevTxCPLD.setStatus("current")
_LccmtsHwRevAFFPGA_Type = Integer32
_LccmtsHwRevAFFPGA_Object = MibScalar
lccmtsHwRevAFFPGA = _LccmtsHwRevAFFPGA_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 5, 6, 3),
    _LccmtsHwRevAFFPGA_Type()
)
lccmtsHwRevAFFPGA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lccmtsHwRevAFFPGA.setStatus("current")
_LccmtsHwRevGT64010_Type = Integer32
_LccmtsHwRevGT64010_Object = MibScalar
lccmtsHwRevGT64010 = _LccmtsHwRevGT64010_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 5, 6, 4),
    _LccmtsHwRevGT64010_Type()
)
lccmtsHwRevGT64010.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lccmtsHwRevGT64010.setStatus("current")
_LccmtsHwRevPLX9080_Type = Integer32
_LccmtsHwRevPLX9080_Object = MibScalar
lccmtsHwRevPLX9080 = _LccmtsHwRevPLX9080_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 5, 6, 5),
    _LccmtsHwRevPLX9080_Type()
)
lccmtsHwRevPLX9080.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lccmtsHwRevPLX9080.setStatus("current")
_LccmtsHwRevBCM3210_Type = Integer32
_LccmtsHwRevBCM3210_Object = MibScalar
lccmtsHwRevBCM3210 = _LccmtsHwRevBCM3210_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 5, 6, 6),
    _LccmtsHwRevBCM3210_Type()
)
lccmtsHwRevBCM3210.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lccmtsHwRevBCM3210.setStatus("current")
_LccmtsHwRevBCM3033_Type = Integer32
_LccmtsHwRevBCM3033_Object = MibScalar
lccmtsHwRevBCM3033 = _LccmtsHwRevBCM3033_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 5, 6, 7),
    _LccmtsHwRevBCM3033_Type()
)
lccmtsHwRevBCM3033.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lccmtsHwRevBCM3033.setStatus("current")
_LccmtsHwRevSunset_Type = Integer32
_LccmtsHwRevSunset_Object = MibScalar
lccmtsHwRevSunset = _LccmtsHwRevSunset_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 5, 6, 8),
    _LccmtsHwRevSunset_Type()
)
lccmtsHwRevSunset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lccmtsHwRevSunset.setStatus("current")
_LccmtsHwRevDEC21143_Type = Integer32
_LccmtsHwRevDEC21143_Object = MibScalar
lccmtsHwRevDEC21143 = _LccmtsHwRevDEC21143_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 5, 6, 9),
    _LccmtsHwRevDEC21143_Type()
)
lccmtsHwRevDEC21143.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lccmtsHwRevDEC21143.setStatus("current")
_LccmtsHwRevLXT970A_Type = Integer32
_LccmtsHwRevLXT970A_Object = MibScalar
lccmtsHwRevLXT970A = _LccmtsHwRevLXT970A_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 5, 6, 10),
    _LccmtsHwRevLXT970A_Type()
)
lccmtsHwRevLXT970A.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lccmtsHwRevLXT970A.setStatus("current")
_LccmtsHwRevLXT970B_Type = Integer32
_LccmtsHwRevLXT970B_Object = MibScalar
lccmtsHwRevLXT970B = _LccmtsHwRevLXT970B_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 5, 6, 11),
    _LccmtsHwRevLXT970B_Type()
)
lccmtsHwRevLXT970B.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lccmtsHwRevLXT970B.setStatus("current")
_LccmtsHwRevRfRxTable_Object = MibTable
lccmtsHwRevRfRxTable = _LccmtsHwRevRfRxTable_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 5, 6, 12)
)
if mibBuilder.loadTexts:
    lccmtsHwRevRfRxTable.setStatus("current")
_LccmtsHwRevRfRxEntry_Object = MibTableRow
lccmtsHwRevRfRxEntry = _LccmtsHwRevRfRxEntry_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 5, 6, 12, 1)
)
lccmtsHwRevRfRxEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    lccmtsHwRevRfRxEntry.setStatus("current")
_LccmtsHwRevBCM3137_Type = Integer32
_LccmtsHwRevBCM3137_Object = MibTableColumn
lccmtsHwRevBCM3137 = _LccmtsHwRevBCM3137_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 5, 6, 12, 1, 1),
    _LccmtsHwRevBCM3137_Type()
)
lccmtsHwRevBCM3137.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lccmtsHwRevBCM3137.setStatus("current")
_LccmtsHwRevRipsaw_Type = Integer32
_LccmtsHwRevRipsaw_Object = MibTableColumn
lccmtsHwRevRipsaw = _LccmtsHwRevRipsaw_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 5, 6, 12, 1, 2),
    _LccmtsHwRevRipsaw_Type()
)
lccmtsHwRevRipsaw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lccmtsHwRevRipsaw.setStatus("current")
_LccmtsPoliceTolerance_ObjectIdentity = ObjectIdentity
lccmtsPoliceTolerance = _LccmtsPoliceTolerance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 482, 60, 5, 7)
)


class _LccmtsUpPolice_Type(Integer32):
    """Custom type lccmtsUpPolice based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_LccmtsUpPolice_Type.__name__ = "Integer32"
_LccmtsUpPolice_Object = MibScalar
lccmtsUpPolice = _LccmtsUpPolice_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 5, 7, 1),
    _LccmtsUpPolice_Type()
)
lccmtsUpPolice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lccmtsUpPolice.setStatus("current")


class _LccmtsDnPolice_Type(Integer32):
    """Custom type lccmtsDnPolice based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_LccmtsDnPolice_Type.__name__ = "Integer32"
_LccmtsDnPolice_Object = MibScalar
lccmtsDnPolice = _LccmtsDnPolice_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 5, 7, 2),
    _LccmtsDnPolice_Type()
)
lccmtsDnPolice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lccmtsDnPolice.setStatus("current")
_LccmtsBOOTPRelay_ObjectIdentity = ObjectIdentity
lccmtsBOOTPRelay = _LccmtsBOOTPRelay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 482, 60, 5, 8)
)


class _LccmtsBOOTPRelayControl_Type(Integer32):
    """Custom type lccmtsBOOTPRelayControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled-cm-only-relay", 4),
          ("enabled-relay-only", 2),
          ("enabled-relay-tagging", 3))
    )


_LccmtsBOOTPRelayControl_Type.__name__ = "Integer32"
_LccmtsBOOTPRelayControl_Object = MibScalar
lccmtsBOOTPRelayControl = _LccmtsBOOTPRelayControl_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 5, 8, 1),
    _LccmtsBOOTPRelayControl_Type()
)
lccmtsBOOTPRelayControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lccmtsBOOTPRelayControl.setStatus("current")
_LccmtsBOOTPRelaySvrTargetTable_Object = MibTable
lccmtsBOOTPRelaySvrTargetTable = _LccmtsBOOTPRelaySvrTargetTable_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 5, 8, 2)
)
if mibBuilder.loadTexts:
    lccmtsBOOTPRelaySvrTargetTable.setStatus("current")
_LccmtsBOOTPRelaySvrTargetEntry_Object = MibTableRow
lccmtsBOOTPRelaySvrTargetEntry = _LccmtsBOOTPRelaySvrTargetEntry_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 5, 8, 2, 1)
)
lccmtsBOOTPRelaySvrTargetEntry.setIndexNames(
    (0, "LANCITY-MCNS-MIB", "lccmtsBOOTPRelayIndex"),
)
if mibBuilder.loadTexts:
    lccmtsBOOTPRelaySvrTargetEntry.setStatus("current")


class _LccmtsBOOTPRelayIndex_Type(Integer32):
    """Custom type lccmtsBOOTPRelayIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_LccmtsBOOTPRelayIndex_Type.__name__ = "Integer32"
_LccmtsBOOTPRelayIndex_Object = MibTableColumn
lccmtsBOOTPRelayIndex = _LccmtsBOOTPRelayIndex_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 5, 8, 2, 1, 1),
    _LccmtsBOOTPRelayIndex_Type()
)
lccmtsBOOTPRelayIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lccmtsBOOTPRelayIndex.setStatus("current")
_LccmtsBOOTPRelaySvrTargetIP_Type = IpAddress
_LccmtsBOOTPRelaySvrTargetIP_Object = MibTableColumn
lccmtsBOOTPRelaySvrTargetIP = _LccmtsBOOTPRelaySvrTargetIP_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 5, 8, 2, 1, 2),
    _LccmtsBOOTPRelaySvrTargetIP_Type()
)
lccmtsBOOTPRelaySvrTargetIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lccmtsBOOTPRelaySvrTargetIP.setStatus("current")


class _LccmtsBOOTPRelayClntSelectionMask_Type(Integer32):
    """Custom type lccmtsBOOTPRelayClntSelectionMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("target-handles-CM-only", 1),
          ("target-handles-CPE-only", 2),
          ("target-handles-any", 3))
    )


_LccmtsBOOTPRelayClntSelectionMask_Type.__name__ = "Integer32"
_LccmtsBOOTPRelayClntSelectionMask_Object = MibTableColumn
lccmtsBOOTPRelayClntSelectionMask = _LccmtsBOOTPRelayClntSelectionMask_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 5, 8, 2, 1, 3),
    _LccmtsBOOTPRelayClntSelectionMask_Type()
)
lccmtsBOOTPRelayClntSelectionMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lccmtsBOOTPRelayClntSelectionMask.setStatus("current")
_LccmtsBOOTPRelaySvrTargetHits_Type = Counter32
_LccmtsBOOTPRelaySvrTargetHits_Object = MibTableColumn
lccmtsBOOTPRelaySvrTargetHits = _LccmtsBOOTPRelaySvrTargetHits_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 5, 8, 2, 1, 4),
    _LccmtsBOOTPRelaySvrTargetHits_Type()
)
lccmtsBOOTPRelaySvrTargetHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lccmtsBOOTPRelaySvrTargetHits.setStatus("current")
_LccmtsBOOTPRelayRowStatus_Type = RowStatus
_LccmtsBOOTPRelayRowStatus_Object = MibTableColumn
lccmtsBOOTPRelayRowStatus = _LccmtsBOOTPRelayRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 5, 8, 2, 1, 5),
    _LccmtsBOOTPRelayRowStatus_Type()
)
lccmtsBOOTPRelayRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lccmtsBOOTPRelayRowStatus.setStatus("current")
_LccmtsBOOTPRelayBadLengthDiscards_Type = Counter32
_LccmtsBOOTPRelayBadLengthDiscards_Object = MibScalar
lccmtsBOOTPRelayBadLengthDiscards = _LccmtsBOOTPRelayBadLengthDiscards_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 5, 8, 3),
    _LccmtsBOOTPRelayBadLengthDiscards_Type()
)
lccmtsBOOTPRelayBadLengthDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lccmtsBOOTPRelayBadLengthDiscards.setStatus("current")
_LccmtsBOOTPRelayLocalOriginDiscards_Type = Counter32
_LccmtsBOOTPRelayLocalOriginDiscards_Object = MibScalar
lccmtsBOOTPRelayLocalOriginDiscards = _LccmtsBOOTPRelayLocalOriginDiscards_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 5, 8, 4),
    _LccmtsBOOTPRelayLocalOriginDiscards_Type()
)
lccmtsBOOTPRelayLocalOriginDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lccmtsBOOTPRelayLocalOriginDiscards.setStatus("current")
_LccmtsBOOTPRelayExcessiveHopsDiscards_Type = Counter32
_LccmtsBOOTPRelayExcessiveHopsDiscards_Object = MibScalar
lccmtsBOOTPRelayExcessiveHopsDiscards = _LccmtsBOOTPRelayExcessiveHopsDiscards_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 5, 8, 5),
    _LccmtsBOOTPRelayExcessiveHopsDiscards_Type()
)
lccmtsBOOTPRelayExcessiveHopsDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lccmtsBOOTPRelayExcessiveHopsDiscards.setStatus("current")
_LccmtsBOOTPRelayGatewayAddrCopies_Type = Counter32
_LccmtsBOOTPRelayGatewayAddrCopies_Object = MibScalar
lccmtsBOOTPRelayGatewayAddrCopies = _LccmtsBOOTPRelayGatewayAddrCopies_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 5, 8, 6),
    _LccmtsBOOTPRelayGatewayAddrCopies_Type()
)
lccmtsBOOTPRelayGatewayAddrCopies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lccmtsBOOTPRelayGatewayAddrCopies.setStatus("current")
_LccmtsBOOTPRelayLocalAddrSinks_Type = Counter32
_LccmtsBOOTPRelayLocalAddrSinks_Object = MibScalar
lccmtsBOOTPRelayLocalAddrSinks = _LccmtsBOOTPRelayLocalAddrSinks_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 5, 8, 7),
    _LccmtsBOOTPRelayLocalAddrSinks_Type()
)
lccmtsBOOTPRelayLocalAddrSinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lccmtsBOOTPRelayLocalAddrSinks.setStatus("current")
_LccmtsBOOTPRelayWrongGatewayAddrDiscards_Type = Counter32
_LccmtsBOOTPRelayWrongGatewayAddrDiscards_Object = MibScalar
lccmtsBOOTPRelayWrongGatewayAddrDiscards = _LccmtsBOOTPRelayWrongGatewayAddrDiscards_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 5, 8, 8),
    _LccmtsBOOTPRelayWrongGatewayAddrDiscards_Type()
)
lccmtsBOOTPRelayWrongGatewayAddrDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lccmtsBOOTPRelayWrongGatewayAddrDiscards.setStatus("current")
_LccmtsBOOTPRelayNoCopyBufDiscards_Type = Counter32
_LccmtsBOOTPRelayNoCopyBufDiscards_Object = MibScalar
lccmtsBOOTPRelayNoCopyBufDiscards = _LccmtsBOOTPRelayNoCopyBufDiscards_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 5, 8, 9),
    _LccmtsBOOTPRelayNoCopyBufDiscards_Type()
)
lccmtsBOOTPRelayNoCopyBufDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lccmtsBOOTPRelayNoCopyBufDiscards.setStatus("current")
_LccmtsBOOTPRelayMiscSilentDiscards_Type = Counter32
_LccmtsBOOTPRelayMiscSilentDiscards_Object = MibScalar
lccmtsBOOTPRelayMiscSilentDiscards = _LccmtsBOOTPRelayMiscSilentDiscards_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 5, 8, 10),
    _LccmtsBOOTPRelayMiscSilentDiscards_Type()
)
lccmtsBOOTPRelayMiscSilentDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lccmtsBOOTPRelayMiscSilentDiscards.setStatus("current")
_LccmtsBOOTPRelayNoEpilBufDiscards_Type = Counter32
_LccmtsBOOTPRelayNoEpilBufDiscards_Object = MibScalar
lccmtsBOOTPRelayNoEpilBufDiscards = _LccmtsBOOTPRelayNoEpilBufDiscards_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 5, 8, 11),
    _LccmtsBOOTPRelayNoEpilBufDiscards_Type()
)
lccmtsBOOTPRelayNoEpilBufDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lccmtsBOOTPRelayNoEpilBufDiscards.setStatus("current")
_LccmtsBOOTPRelayClntDstPortDiscards_Type = Counter32
_LccmtsBOOTPRelayClntDstPortDiscards_Object = MibScalar
lccmtsBOOTPRelayClntDstPortDiscards = _LccmtsBOOTPRelayClntDstPortDiscards_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 5, 8, 12),
    _LccmtsBOOTPRelayClntDstPortDiscards_Type()
)
lccmtsBOOTPRelayClntDstPortDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lccmtsBOOTPRelayClntDstPortDiscards.setStatus("current")
_LccmtsBOOTPRelayRawRequests_Type = Counter32
_LccmtsBOOTPRelayRawRequests_Object = MibScalar
lccmtsBOOTPRelayRawRequests = _LccmtsBOOTPRelayRawRequests_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 5, 8, 13),
    _LccmtsBOOTPRelayRawRequests_Type()
)
lccmtsBOOTPRelayRawRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lccmtsBOOTPRelayRawRequests.setStatus("current")
_LccmtsBOOTPRelayRawReplies_Type = Counter32
_LccmtsBOOTPRelayRawReplies_Object = MibScalar
lccmtsBOOTPRelayRawReplies = _LccmtsBOOTPRelayRawReplies_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 5, 8, 14),
    _LccmtsBOOTPRelayRawReplies_Type()
)
lccmtsBOOTPRelayRawReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lccmtsBOOTPRelayRawReplies.setStatus("current")
_LccmtsBOOTPRelayRqstFromCM_Type = Counter32
_LccmtsBOOTPRelayRqstFromCM_Object = MibScalar
lccmtsBOOTPRelayRqstFromCM = _LccmtsBOOTPRelayRqstFromCM_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 5, 8, 15),
    _LccmtsBOOTPRelayRqstFromCM_Type()
)
lccmtsBOOTPRelayRqstFromCM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lccmtsBOOTPRelayRqstFromCM.setStatus("current")
_LccmtsBOOTPRelayRqstFromCPE_Type = Counter32
_LccmtsBOOTPRelayRqstFromCPE_Object = MibScalar
lccmtsBOOTPRelayRqstFromCPE = _LccmtsBOOTPRelayRqstFromCPE_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 5, 8, 16),
    _LccmtsBOOTPRelayRqstFromCPE_Type()
)
lccmtsBOOTPRelayRqstFromCPE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lccmtsBOOTPRelayRqstFromCPE.setStatus("current")
_LccmtsBOOTPRelayDPCATVPuts_Type = Counter32
_LccmtsBOOTPRelayDPCATVPuts_Object = MibScalar
lccmtsBOOTPRelayDPCATVPuts = _LccmtsBOOTPRelayDPCATVPuts_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 5, 8, 17),
    _LccmtsBOOTPRelayDPCATVPuts_Type()
)
lccmtsBOOTPRelayDPCATVPuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lccmtsBOOTPRelayDPCATVPuts.setStatus("current")
_LccmtsBOOTPRelayDPEnetPuts_Type = Counter32
_LccmtsBOOTPRelayDPEnetPuts_Object = MibScalar
lccmtsBOOTPRelayDPEnetPuts = _LccmtsBOOTPRelayDPEnetPuts_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 5, 8, 18),
    _LccmtsBOOTPRelayDPEnetPuts_Type()
)
lccmtsBOOTPRelayDPEnetPuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lccmtsBOOTPRelayDPEnetPuts.setStatus("current")
_LccmtsBOOTPRelayEpilUDPBufSends_Type = Counter32
_LccmtsBOOTPRelayEpilUDPBufSends_Object = MibScalar
lccmtsBOOTPRelayEpilUDPBufSends = _LccmtsBOOTPRelayEpilUDPBufSends_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 5, 8, 19),
    _LccmtsBOOTPRelayEpilUDPBufSends_Type()
)
lccmtsBOOTPRelayEpilUDPBufSends.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lccmtsBOOTPRelayEpilUDPBufSends.setStatus("current")
_LccmtsBOOTPRelayNullMACTags_Type = Counter32
_LccmtsBOOTPRelayNullMACTags_Object = MibScalar
lccmtsBOOTPRelayNullMACTags = _LccmtsBOOTPRelayNullMACTags_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 5, 8, 20),
    _LccmtsBOOTPRelayNullMACTags_Type()
)
lccmtsBOOTPRelayNullMACTags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lccmtsBOOTPRelayNullMACTags.setStatus("current")
_LccmtsBOOTPRelayNonNullMACTags_Type = Counter32
_LccmtsBOOTPRelayNonNullMACTags_Object = MibScalar
lccmtsBOOTPRelayNonNullMACTags = _LccmtsBOOTPRelayNonNullMACTags_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 5, 8, 21),
    _LccmtsBOOTPRelayNonNullMACTags_Type()
)
lccmtsBOOTPRelayNonNullMACTags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lccmtsBOOTPRelayNonNullMACTags.setStatus("current")
_LccmtsBOOTPRelayWrongPortRqstDiscards_Type = Counter32
_LccmtsBOOTPRelayWrongPortRqstDiscards_Object = MibScalar
lccmtsBOOTPRelayWrongPortRqstDiscards = _LccmtsBOOTPRelayWrongPortRqstDiscards_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 5, 8, 22),
    _LccmtsBOOTPRelayWrongPortRqstDiscards_Type()
)
lccmtsBOOTPRelayWrongPortRqstDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lccmtsBOOTPRelayWrongPortRqstDiscards.setStatus("current")
_LccmtsBOOTPRelayWrongPortReplyDiscards_Type = Counter32
_LccmtsBOOTPRelayWrongPortReplyDiscards_Object = MibScalar
lccmtsBOOTPRelayWrongPortReplyDiscards = _LccmtsBOOTPRelayWrongPortReplyDiscards_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 5, 8, 23),
    _LccmtsBOOTPRelayWrongPortReplyDiscards_Type()
)
lccmtsBOOTPRelayWrongPortReplyDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lccmtsBOOTPRelayWrongPortReplyDiscards.setStatus("current")
_LccmtsDNSResolver_ObjectIdentity = ObjectIdentity
lccmtsDNSResolver = _LccmtsDNSResolver_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 482, 60, 5, 9)
)


class _LccmtsDNSResolverControl_Type(Integer32):
    """Custom type lccmtsDNSResolverControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_LccmtsDNSResolverControl_Type.__name__ = "Integer32"
_LccmtsDNSResolverControl_Object = MibScalar
lccmtsDNSResolverControl = _LccmtsDNSResolverControl_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 5, 9, 1),
    _LccmtsDNSResolverControl_Type()
)
lccmtsDNSResolverControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lccmtsDNSResolverControl.setStatus("current")


class _LccmtsDNSResolverServiceType_Type(Integer32):
    """Custom type lccmtsDNSResolverServiceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("iterativeOnly", 2),
          ("recursiveAndIterative", 3),
          ("recursiveOnly", 1))
    )


_LccmtsDNSResolverServiceType_Type.__name__ = "Integer32"
_LccmtsDNSResolverServiceType_Object = MibScalar
lccmtsDNSResolverServiceType = _LccmtsDNSResolverServiceType_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 5, 9, 2),
    _LccmtsDNSResolverServiceType_Type()
)
lccmtsDNSResolverServiceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lccmtsDNSResolverServiceType.setStatus("current")


class _LccmtsDNSResolverServersCfgd_Type(Integer32):
    """Custom type lccmtsDNSResolverServersCfgd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_LccmtsDNSResolverServersCfgd_Type.__name__ = "Integer32"
_LccmtsDNSResolverServersCfgd_Object = MibScalar
lccmtsDNSResolverServersCfgd = _LccmtsDNSResolverServersCfgd_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 5, 9, 3),
    _LccmtsDNSResolverServersCfgd_Type()
)
lccmtsDNSResolverServersCfgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lccmtsDNSResolverServersCfgd.setStatus("current")
_LccmtsDNSResolverServerTable_Object = MibTable
lccmtsDNSResolverServerTable = _LccmtsDNSResolverServerTable_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 5, 9, 4)
)
if mibBuilder.loadTexts:
    lccmtsDNSResolverServerTable.setStatus("current")
_LccmtsDNSResolverServerEntry_Object = MibTableRow
lccmtsDNSResolverServerEntry = _LccmtsDNSResolverServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 5, 9, 4, 1)
)
lccmtsDNSResolverServerEntry.setIndexNames(
    (0, "LANCITY-MCNS-MIB", "lccmtsDNSResolverIndex"),
)
if mibBuilder.loadTexts:
    lccmtsDNSResolverServerEntry.setStatus("current")


class _LccmtsDNSResolverIndex_Type(Integer32):
    """Custom type lccmtsDNSResolverIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_LccmtsDNSResolverIndex_Type.__name__ = "Integer32"
_LccmtsDNSResolverIndex_Object = MibTableColumn
lccmtsDNSResolverIndex = _LccmtsDNSResolverIndex_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 5, 9, 4, 1, 1),
    _LccmtsDNSResolverIndex_Type()
)
lccmtsDNSResolverIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lccmtsDNSResolverIndex.setStatus("current")
_LccmtsDNSResolverServerIP_Type = IpAddress
_LccmtsDNSResolverServerIP_Object = MibTableColumn
lccmtsDNSResolverServerIP = _LccmtsDNSResolverServerIP_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 5, 9, 4, 1, 2),
    _LccmtsDNSResolverServerIP_Type()
)
lccmtsDNSResolverServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lccmtsDNSResolverServerIP.setStatus("current")


class _LccmtsDNSResolverServerPriority_Type(Integer32):
    """Custom type lccmtsDNSResolverServerPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_LccmtsDNSResolverServerPriority_Type.__name__ = "Integer32"
_LccmtsDNSResolverServerPriority_Object = MibTableColumn
lccmtsDNSResolverServerPriority = _LccmtsDNSResolverServerPriority_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 5, 9, 4, 1, 3),
    _LccmtsDNSResolverServerPriority_Type()
)
lccmtsDNSResolverServerPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lccmtsDNSResolverServerPriority.setStatus("current")


class _LccmtsDNSResolverServerName_Type(DisplayString):
    """Custom type lccmtsDNSResolverServerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_LccmtsDNSResolverServerName_Type.__name__ = "DisplayString"
_LccmtsDNSResolverServerName_Object = MibTableColumn
lccmtsDNSResolverServerName = _LccmtsDNSResolverServerName_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 5, 9, 4, 1, 4),
    _LccmtsDNSResolverServerName_Type()
)
lccmtsDNSResolverServerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lccmtsDNSResolverServerName.setStatus("current")
_LccmtsDNSResolverRowStatus_Type = RowStatus
_LccmtsDNSResolverRowStatus_Object = MibTableColumn
lccmtsDNSResolverRowStatus = _LccmtsDNSResolverRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 5, 9, 4, 1, 5),
    _LccmtsDNSResolverRowStatus_Type()
)
lccmtsDNSResolverRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lccmtsDNSResolverRowStatus.setStatus("current")
_LccmtsDevServer_ObjectIdentity = ObjectIdentity
lccmtsDevServer = _LccmtsDevServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 482, 60, 5, 10)
)


class _LccmtsDevServerBootState_Type(Integer32):
    """Custom type lccmtsDevServerBootState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("forwardingDenied", 8),
          ("operational", 1),
          ("other", 9),
          ("refusedByCmts", 7),
          ("unknown", 10),
          ("waitingForDhcpOffer", 3),
          ("waitingForDhcpResponse", 4),
          ("waitingForTftp", 6),
          ("waitingForTimeServer", 5))
    )


_LccmtsDevServerBootState_Type.__name__ = "Integer32"
_LccmtsDevServerBootState_Object = MibScalar
lccmtsDevServerBootState = _LccmtsDevServerBootState_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 5, 10, 1),
    _LccmtsDevServerBootState_Type()
)
lccmtsDevServerBootState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lccmtsDevServerBootState.setStatus("current")
_LccmtsDevServerDhcp_Type = IpAddress
_LccmtsDevServerDhcp_Object = MibScalar
lccmtsDevServerDhcp = _LccmtsDevServerDhcp_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 5, 10, 2),
    _LccmtsDevServerDhcp_Type()
)
lccmtsDevServerDhcp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lccmtsDevServerDhcp.setStatus("current")
_LccmtsDevServerTime_Type = IpAddress
_LccmtsDevServerTime_Object = MibScalar
lccmtsDevServerTime = _LccmtsDevServerTime_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 5, 10, 3),
    _LccmtsDevServerTime_Type()
)
lccmtsDevServerTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lccmtsDevServerTime.setStatus("current")
_LccmtsDevServerTftp_Type = IpAddress
_LccmtsDevServerTftp_Object = MibScalar
lccmtsDevServerTftp = _LccmtsDevServerTftp_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 5, 10, 4),
    _LccmtsDevServerTftp_Type()
)
lccmtsDevServerTftp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lccmtsDevServerTftp.setStatus("current")
_LccmtsDevServerConfigFile_Type = DisplayString
_LccmtsDevServerConfigFile_Object = MibScalar
lccmtsDevServerConfigFile = _LccmtsDevServerConfigFile_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 5, 10, 5),
    _LccmtsDevServerConfigFile_Type()
)
lccmtsDevServerConfigFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lccmtsDevServerConfigFile.setStatus("current")
_Lccmdevice_ObjectIdentity = ObjectIdentity
lccmdevice = _Lccmdevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 482, 60, 6)
)
_LcScanningFrequencyTable_Object = MibTable
lcScanningFrequencyTable = _LcScanningFrequencyTable_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 6, 1)
)
if mibBuilder.loadTexts:
    lcScanningFrequencyTable.setStatus("current")
_LcScanningFrequencyEntry_Object = MibTableRow
lcScanningFrequencyEntry = _LcScanningFrequencyEntry_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 6, 1, 1)
)
lcScanningFrequencyEntry.setIndexNames(
    (0, "LANCITY-MCNS-MIB", "lcScanIndex"),
)
if mibBuilder.loadTexts:
    lcScanningFrequencyEntry.setStatus("current")
_LcScanControl_Type = RowStatus
_LcScanControl_Object = MibTableColumn
lcScanControl = _LcScanControl_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 6, 1, 1, 1),
    _LcScanControl_Type()
)
lcScanControl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lcScanControl.setStatus("current")


class _LcScanIndex_Type(Integer32):
    """Custom type lcScanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_LcScanIndex_Type.__name__ = "Integer32"
_LcScanIndex_Object = MibTableColumn
lcScanIndex = _LcScanIndex_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 6, 1, 1, 2),
    _LcScanIndex_Type()
)
lcScanIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lcScanIndex.setStatus("current")
_LcScanFreqStart_Type = Integer32
_LcScanFreqStart_Object = MibTableColumn
lcScanFreqStart = _LcScanFreqStart_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 6, 1, 1, 3),
    _LcScanFreqStart_Type()
)
lcScanFreqStart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lcScanFreqStart.setStatus("current")
if mibBuilder.loadTexts:
    lcScanFreqStart.setUnits("kilohertz")
_LcScanFreqEnd_Type = Integer32
_LcScanFreqEnd_Object = MibTableColumn
lcScanFreqEnd = _LcScanFreqEnd_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 6, 1, 1, 4),
    _LcScanFreqEnd_Type()
)
lcScanFreqEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lcScanFreqEnd.setStatus("current")
if mibBuilder.loadTexts:
    lcScanFreqEnd.setUnits("kilohertz")


class _LcScanUseHrc_Type(TruthValue):
    """Custom type lcScanUseHrc based on TruthValue"""
    defaultValue = 2


_LcScanUseHrc_Object = MibTableColumn
lcScanUseHrc = _LcScanUseHrc_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 6, 1, 1, 5),
    _LcScanUseHrc_Type()
)
lcScanUseHrc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lcScanUseHrc.setStatus("current")
_LcScanStep_Type = Integer32
_LcScanStep_Object = MibTableColumn
lcScanStep = _LcScanStep_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 6, 1, 1, 6),
    _LcScanStep_Type()
)
lcScanStep.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lcScanStep.setStatus("current")
if mibBuilder.loadTexts:
    lcScanStep.setUnits("kilohertz")


class _LcScanChannelWidth_Type(Integer32):
    """Custom type lcScanChannelWidth based on Integer32"""
    defaultValue = 6000


_LcScanChannelWidth_Object = MibTableColumn
lcScanChannelWidth = _LcScanChannelWidth_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 6, 1, 1, 7),
    _LcScanChannelWidth_Type()
)
lcScanChannelWidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lcScanChannelWidth.setStatus("current")
if mibBuilder.loadTexts:
    lcScanChannelWidth.setUnits("kilohertz")
_LccmAddress_ObjectIdentity = ObjectIdentity
lccmAddress = _LccmAddress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 482, 60, 6, 2)
)
_LccmIpAddress_Type = IpAddress
_LccmIpAddress_Object = MibScalar
lccmIpAddress = _LccmIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 6, 2, 1),
    _LccmIpAddress_Type()
)
lccmIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lccmIpAddress.setStatus("current")
_LccmIpSubnet_Type = IpAddress
_LccmIpSubnet_Object = MibScalar
lccmIpSubnet = _LccmIpSubnet_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 6, 2, 2),
    _LccmIpSubnet_Type()
)
lccmIpSubnet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lccmIpSubnet.setStatus("current")
_Lcdevicecommon_ObjectIdentity = ObjectIdentity
lcdevicecommon = _Lcdevicecommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 482, 60, 7)
)
_LcTrapTypeTable_Object = MibTable
lcTrapTypeTable = _LcTrapTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 7, 1)
)
if mibBuilder.loadTexts:
    lcTrapTypeTable.setStatus("current")
_LcTrapTypeEntry_Object = MibTableRow
lcTrapTypeEntry = _LcTrapTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 7, 1, 1)
)
lcTrapTypeEntry.setIndexNames(
    (0, "LANCITY-MCNS-MIB", "lcTrapTypeIndex"),
)
if mibBuilder.loadTexts:
    lcTrapTypeEntry.setStatus("current")


class _LcTrapTypeIndex_Type(Integer32):
    """Custom type lcTrapTypeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              9)
        )
    )
    namedValues = NamedValues(
        *(("authenticationFailureTrap", 5),
          ("coldstartTrap", 1),
          ("lcMcastJoinTrap", 9),
          ("linkDownTrap", 4),
          ("linkUpTrap", 3),
          ("newRootTrap", 7),
          ("topologyChangeTrap", 6),
          ("warmstartTrap", 2))
    )


_LcTrapTypeIndex_Type.__name__ = "Integer32"
_LcTrapTypeIndex_Object = MibTableColumn
lcTrapTypeIndex = _LcTrapTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 7, 1, 1, 1),
    _LcTrapTypeIndex_Type()
)
lcTrapTypeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcTrapTypeIndex.setStatus("current")


class _LcTrapTypeStatus_Type(Integer32):
    """Custom type lcTrapTypeStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noTrap", 2),
          ("sendTrap", 1))
    )


_LcTrapTypeStatus_Type.__name__ = "Integer32"
_LcTrapTypeStatus_Object = MibTableColumn
lcTrapTypeStatus = _LcTrapTypeStatus_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 7, 1, 1, 2),
    _LcTrapTypeStatus_Type()
)
lcTrapTypeStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcTrapTypeStatus.setStatus("current")


class _LcBootedAlbumFilename_Type(DisplayString):
    """Custom type lcBootedAlbumFilename based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LcBootedAlbumFilename_Type.__name__ = "DisplayString"
_LcBootedAlbumFilename_Object = MibScalar
lcBootedAlbumFilename = _LcBootedAlbumFilename_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 7, 2),
    _LcBootedAlbumFilename_Type()
)
lcBootedAlbumFilename.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcBootedAlbumFilename.setStatus("current")
_LcBootedAlbumSequenceNumber_Type = Counter32
_LcBootedAlbumSequenceNumber_Object = MibScalar
lcBootedAlbumSequenceNumber = _LcBootedAlbumSequenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 7, 3),
    _LcBootedAlbumSequenceNumber_Type()
)
lcBootedAlbumSequenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcBootedAlbumSequenceNumber.setStatus("current")
_Lctrapvars_ObjectIdentity = ObjectIdentity
lctrapvars = _Lctrapvars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 482, 60, 7, 4)
)


class _LcAuthFailErrorStatus_Type(Integer32):
    """Custom type lcAuthFailErrorStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("nmAccessTableRestriction", 1),
          ("noWriteAccessToMibVar", 2),
          ("other", 3))
    )


_LcAuthFailErrorStatus_Type.__name__ = "Integer32"
_LcAuthFailErrorStatus_Object = MibScalar
lcAuthFailErrorStatus = _LcAuthFailErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 7, 4, 1),
    _LcAuthFailErrorStatus_Type()
)
lcAuthFailErrorStatus.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lcAuthFailErrorStatus.setStatus("current")


class _LcAuthFailCommunityString_Type(DisplayString):
    """Custom type lcAuthFailCommunityString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LcAuthFailCommunityString_Type.__name__ = "DisplayString"
_LcAuthFailCommunityString_Object = MibScalar
lcAuthFailCommunityString = _LcAuthFailCommunityString_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 7, 4, 2),
    _LcAuthFailCommunityString_Type()
)
lcAuthFailCommunityString.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lcAuthFailCommunityString.setStatus("current")
_LcAuthFailIpAddr_Type = IpAddress
_LcAuthFailIpAddr_Object = MibScalar
lcAuthFailIpAddr = _LcAuthFailIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 7, 4, 3),
    _LcAuthFailIpAddr_Type()
)
lcAuthFailIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lcAuthFailIpAddr.setStatus("current")


class _LcAuthFailInterface_Type(Integer32):
    """Custom type lcAuthFailInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("catv", 2),
          ("ethernet", 1),
          ("other", 3))
    )


_LcAuthFailInterface_Type.__name__ = "Integer32"
_LcAuthFailInterface_Object = MibScalar
lcAuthFailInterface = _LcAuthFailInterface_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 7, 4, 4),
    _LcAuthFailInterface_Type()
)
lcAuthFailInterface.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lcAuthFailInterface.setStatus("current")


class _LcIpFiltSendDu_Type(Integer32):
    """Custom type lcIpFiltSendDu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_LcIpFiltSendDu_Type.__name__ = "Integer32"
_LcIpFiltSendDu_Object = MibScalar
lcIpFiltSendDu = _LcIpFiltSendDu_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 7, 5),
    _LcIpFiltSendDu_Type()
)
lcIpFiltSendDu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcIpFiltSendDu.setStatus("current")
_LcMulticastGroup_ObjectIdentity = ObjectIdentity
lcMulticastGroup = _LcMulticastGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 482, 60, 7, 6)
)


class _LcMcastControl_Type(Integer32):
    """Custom type lcMcastControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("discard", 2),
          ("igmp", 3),
          ("pass", 1),
          ("trap", 4))
    )


_LcMcastControl_Type.__name__ = "Integer32"
_LcMcastControl_Object = MibScalar
lcMcastControl = _LcMcastControl_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 7, 6, 1),
    _LcMcastControl_Type()
)
lcMcastControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcMcastControl.setStatus("current")
_LcMcastAddressTable_Object = MibTable
lcMcastAddressTable = _LcMcastAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 7, 6, 2)
)
if mibBuilder.loadTexts:
    lcMcastAddressTable.setStatus("current")
_LcMcastAddressEntry_Object = MibTableRow
lcMcastAddressEntry = _LcMcastAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 7, 6, 2, 1)
)
lcMcastAddressEntry.setIndexNames(
    (0, "LANCITY-MCNS-MIB", "lcMcastAddress"),
)
if mibBuilder.loadTexts:
    lcMcastAddressEntry.setStatus("current")
_LcMcastAddress_Type = IpAddress
_LcMcastAddress_Object = MibTableColumn
lcMcastAddress = _LcMcastAddress_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 7, 6, 2, 1, 1),
    _LcMcastAddress_Type()
)
lcMcastAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lcMcastAddress.setStatus("current")
_LcMcastAdminState_Type = RowStatus
_LcMcastAdminState_Object = MibTableColumn
lcMcastAdminState = _LcMcastAdminState_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 7, 6, 2, 1, 2),
    _LcMcastAdminState_Type()
)
lcMcastAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lcMcastAdminState.setStatus("current")


class _LcMcastOperState_Type(Integer32):
    """Custom type lcMcastOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("delaying", 2),
          ("idle", 3),
          ("nonmember", 1),
          ("static", 4))
    )


_LcMcastOperState_Type.__name__ = "Integer32"
_LcMcastOperState_Object = MibTableColumn
lcMcastOperState = _LcMcastOperState_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 7, 6, 2, 1, 3),
    _LcMcastOperState_Type()
)
lcMcastOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcMcastOperState.setStatus("current")
_LcMcastTtl_Type = TimeTicks
_LcMcastTtl_Object = MibTableColumn
lcMcastTtl = _LcMcastTtl_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 7, 6, 2, 1, 4),
    _LcMcastTtl_Type()
)
lcMcastTtl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcMcastTtl.setStatus("current")
_LcMcastTrapAddress_Type = IpAddress
_LcMcastTrapAddress_Object = MibScalar
lcMcastTrapAddress = _LcMcastTrapAddress_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 7, 6, 3),
    _LcMcastTrapAddress_Type()
)
lcMcastTrapAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lcMcastTrapAddress.setStatus("current")
_LcRestartFromFactoryDefaults_Type = TruthValue
_LcRestartFromFactoryDefaults_Object = MibScalar
lcRestartFromFactoryDefaults = _LcRestartFromFactoryDefaults_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 7, 7),
    _LcRestartFromFactoryDefaults_Type()
)
lcRestartFromFactoryDefaults.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcRestartFromFactoryDefaults.setStatus("current")
_LcPhyTable_Object = MibTable
lcPhyTable = _LcPhyTable_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 7, 8)
)
if mibBuilder.loadTexts:
    lcPhyTable.setStatus("current")
_LcPhyEntry_Object = MibTableRow
lcPhyEntry = _LcPhyEntry_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 7, 8, 1)
)
lcPhyEntry.setIndexNames(
    (0, "LANCITY-MCNS-MIB", "lcPhyIndex"),
)
if mibBuilder.loadTexts:
    lcPhyEntry.setStatus("current")


class _LcPhyIndex_Type(Integer32):
    """Custom type lcPhyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("aux1", 2),
          ("primary", 1))
    )


_LcPhyIndex_Type.__name__ = "Integer32"
_LcPhyIndex_Object = MibTableColumn
lcPhyIndex = _LcPhyIndex_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 7, 8, 1, 1),
    _LcPhyIndex_Type()
)
lcPhyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcPhyIndex.setStatus("current")


class _LcPhyEnable_Type(TruthValue):
    """Custom type lcPhyEnable based on TruthValue"""
    defaultValue = 1


_LcPhyEnable_Object = MibTableColumn
lcPhyEnable = _LcPhyEnable_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 7, 8, 1, 2),
    _LcPhyEnable_Type()
)
lcPhyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcPhyEnable.setStatus("current")


class _LcPhyAutoNegotiate_Type(TruthValue):
    """Custom type lcPhyAutoNegotiate based on TruthValue"""
    defaultValue = 1


_LcPhyAutoNegotiate_Object = MibTableColumn
lcPhyAutoNegotiate = _LcPhyAutoNegotiate_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 7, 8, 1, 3),
    _LcPhyAutoNegotiate_Type()
)
lcPhyAutoNegotiate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcPhyAutoNegotiate.setStatus("current")
_LcPhyActive_Type = TruthValue
_LcPhyActive_Object = MibTableColumn
lcPhyActive = _LcPhyActive_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 7, 8, 1, 4),
    _LcPhyActive_Type()
)
lcPhyActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcPhyActive.setStatus("current")


class _LcPhySpeed_Type(Integer32):
    """Custom type lcPhySpeed based on Integer32"""
    defaultValue = 10000000


_LcPhySpeed_Object = MibTableColumn
lcPhySpeed = _LcPhySpeed_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 7, 8, 1, 5),
    _LcPhySpeed_Type()
)
lcPhySpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcPhySpeed.setStatus("current")


class _LcPhyFullDuplex_Type(TruthValue):
    """Custom type lcPhyFullDuplex based on TruthValue"""
    defaultValue = 2


_LcPhyFullDuplex_Object = MibTableColumn
lcPhyFullDuplex = _LcPhyFullDuplex_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 7, 8, 1, 6),
    _LcPhyFullDuplex_Type()
)
lcPhyFullDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcPhyFullDuplex.setStatus("current")
_LcStickyYellowTable_Object = MibTable
lcStickyYellowTable = _LcStickyYellowTable_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 7, 9)
)
if mibBuilder.loadTexts:
    lcStickyYellowTable.setStatus("current")
_LcStickyYellowEntry_Object = MibTableRow
lcStickyYellowEntry = _LcStickyYellowEntry_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 7, 9, 1)
)
lcStickyYellowEntry.setIndexNames(
    (0, "LANCITY-MCNS-MIB", "lcStickyYellowIndex"),
)
if mibBuilder.loadTexts:
    lcStickyYellowEntry.setStatus("current")
_LcStickyYellowIndex_Type = Integer32
_LcStickyYellowIndex_Object = MibTableColumn
lcStickyYellowIndex = _LcStickyYellowIndex_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 7, 9, 1, 1),
    _LcStickyYellowIndex_Type()
)
lcStickyYellowIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lcStickyYellowIndex.setStatus("current")
_LcStickyYellowPad_Type = DisplayString
_LcStickyYellowPad_Object = MibTableColumn
lcStickyYellowPad = _LcStickyYellowPad_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 7, 9, 1, 2),
    _LcStickyYellowPad_Type()
)
lcStickyYellowPad.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lcStickyYellowPad.setStatus("current")
_LcResetFilters_Type = TruthValue
_LcResetFilters_Object = MibScalar
lcResetFilters = _LcResetFilters_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 7, 10),
    _LcResetFilters_Type()
)
lcResetFilters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcResetFilters.setStatus("current")
_LcResetNmAccessTable_Type = TruthValue
_LcResetNmAccessTable_Object = MibScalar
lcResetNmAccessTable = _LcResetNmAccessTable_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 7, 11),
    _LcResetNmAccessTable_Type()
)
lcResetNmAccessTable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcResetNmAccessTable.setStatus("current")


class _LcFlashPersistenceSwitch_Type(Bits):
    """Custom type lcFlashPersistenceSwitch based on Bits"""
    namedValues = NamedValues(
        *(("llcIpFilters", 1),
          ("nmAccess", 0))
    )

_LcFlashPersistenceSwitch_Type.__name__ = "Bits"
_LcFlashPersistenceSwitch_Object = MibScalar
lcFlashPersistenceSwitch = _LcFlashPersistenceSwitch_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 7, 12),
    _LcFlashPersistenceSwitch_Type()
)
lcFlashPersistenceSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcFlashPersistenceSwitch.setStatus("current")
_LcConcatenationEnabled_Type = TruthValue
_LcConcatenationEnabled_Object = MibScalar
lcConcatenationEnabled = _LcConcatenationEnabled_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 7, 13),
    _LcConcatenationEnabled_Type()
)
lcConcatenationEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcConcatenationEnabled.setStatus("current")
_LcConsoleAccess_ObjectIdentity = ObjectIdentity
lcConsoleAccess = _LcConsoleAccess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 482, 60, 7, 14)
)
_LcConsoleUserTable_Object = MibTable
lcConsoleUserTable = _LcConsoleUserTable_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 7, 14, 1)
)
if mibBuilder.loadTexts:
    lcConsoleUserTable.setStatus("current")
_LcConsoleUserEntry_Object = MibTableRow
lcConsoleUserEntry = _LcConsoleUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 7, 14, 1, 1)
)
lcConsoleUserEntry.setIndexNames(
    (0, "LANCITY-MCNS-MIB", "lcConsoleUserIndex"),
)
if mibBuilder.loadTexts:
    lcConsoleUserEntry.setStatus("current")
_LcConsoleUserIndex_Type = Integer32
_LcConsoleUserIndex_Object = MibTableColumn
lcConsoleUserIndex = _LcConsoleUserIndex_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 7, 14, 1, 1, 1),
    _LcConsoleUserIndex_Type()
)
lcConsoleUserIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lcConsoleUserIndex.setStatus("current")
_LcConsoleUserStatus_Type = RowStatus
_LcConsoleUserStatus_Object = MibTableColumn
lcConsoleUserStatus = _LcConsoleUserStatus_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 7, 14, 1, 1, 2),
    _LcConsoleUserStatus_Type()
)
lcConsoleUserStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lcConsoleUserStatus.setStatus("current")


class _LcConsoleUserName_Type(DisplayString):
    """Custom type lcConsoleUserName based on DisplayString"""
    defaultValue = OctetString("root")


_LcConsoleUserName_Object = MibTableColumn
lcConsoleUserName = _LcConsoleUserName_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 7, 14, 1, 1, 3),
    _LcConsoleUserName_Type()
)
lcConsoleUserName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lcConsoleUserName.setStatus("current")
_LcConsoleUserPassword_Type = DisplayString
_LcConsoleUserPassword_Object = MibTableColumn
lcConsoleUserPassword = _LcConsoleUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 7, 14, 1, 1, 4),
    _LcConsoleUserPassword_Type()
)
lcConsoleUserPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lcConsoleUserPassword.setStatus("current")


class _LcConsoleUserLevel_Type(Integer32):
    """Custom type lcConsoleUserLevel based on Integer32"""
    defaultValue = 1


_LcConsoleUserLevel_Object = MibTableColumn
lcConsoleUserLevel = _LcConsoleUserLevel_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 7, 14, 1, 1, 5),
    _LcConsoleUserLevel_Type()
)
lcConsoleUserLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lcConsoleUserLevel.setStatus("current")
_LcConsoleLevelTable_Object = MibTable
lcConsoleLevelTable = _LcConsoleLevelTable_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 7, 14, 2)
)
if mibBuilder.loadTexts:
    lcConsoleLevelTable.setStatus("current")
_LcConsoleLevelEntry_Object = MibTableRow
lcConsoleLevelEntry = _LcConsoleLevelEntry_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 7, 14, 2, 1)
)
lcConsoleLevelEntry.setIndexNames(
    (0, "LANCITY-MCNS-MIB", "lcConsoleLevelIndex"),
)
if mibBuilder.loadTexts:
    lcConsoleLevelEntry.setStatus("current")
_LcConsoleLevelIndex_Type = Integer32
_LcConsoleLevelIndex_Object = MibTableColumn
lcConsoleLevelIndex = _LcConsoleLevelIndex_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 7, 14, 2, 1, 1),
    _LcConsoleLevelIndex_Type()
)
lcConsoleLevelIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lcConsoleLevelIndex.setStatus("current")
_LcConsoleLevelStatus_Type = RowStatus
_LcConsoleLevelStatus_Object = MibTableColumn
lcConsoleLevelStatus = _LcConsoleLevelStatus_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 7, 14, 2, 1, 2),
    _LcConsoleLevelStatus_Type()
)
lcConsoleLevelStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lcConsoleLevelStatus.setStatus("current")
_LcConsoleLevelName_Type = DisplayString
_LcConsoleLevelName_Object = MibTableColumn
lcConsoleLevelName = _LcConsoleLevelName_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 7, 14, 2, 1, 3),
    _LcConsoleLevelName_Type()
)
lcConsoleLevelName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lcConsoleLevelName.setStatus("current")


class _LcConsoleLevelMethod_Type(Integer32):
    """Custom type lcConsoleLevelMethod based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("snmpv1", 1)
    )


_LcConsoleLevelMethod_Type.__name__ = "Integer32"
_LcConsoleLevelMethod_Object = MibTableColumn
lcConsoleLevelMethod = _LcConsoleLevelMethod_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 7, 14, 2, 1, 4),
    _LcConsoleLevelMethod_Type()
)
lcConsoleLevelMethod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lcConsoleLevelMethod.setStatus("current")
_LcConsoleLevelSecurityName_Type = DisplayString
_LcConsoleLevelSecurityName_Object = MibTableColumn
lcConsoleLevelSecurityName = _LcConsoleLevelSecurityName_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 7, 14, 2, 1, 5),
    _LcConsoleLevelSecurityName_Type()
)
lcConsoleLevelSecurityName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lcConsoleLevelSecurityName.setStatus("current")


class _LcTelnetAllowedSessions_Type(Integer32):
    """Custom type lcTelnetAllowedSessions based on Integer32"""
    defaultValue = 5


_LcTelnetAllowedSessions_Object = MibScalar
lcTelnetAllowedSessions = _LcTelnetAllowedSessions_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 7, 14, 3),
    _LcTelnetAllowedSessions_Type()
)
lcTelnetAllowedSessions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcTelnetAllowedSessions.setStatus("current")


class _LcSessionInactivityTimeout_Type(Integer32):
    """Custom type lcSessionInactivityTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10080),
    )


_LcSessionInactivityTimeout_Type.__name__ = "Integer32"
_LcSessionInactivityTimeout_Object = MibScalar
lcSessionInactivityTimeout = _LcSessionInactivityTimeout_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 7, 14, 4),
    _LcSessionInactivityTimeout_Type()
)
lcSessionInactivityTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcSessionInactivityTimeout.setStatus("current")
if mibBuilder.loadTexts:
    lcSessionInactivityTimeout.setUnits("minutes")
_LcNmAccessExtensionTable_Object = MibTable
lcNmAccessExtensionTable = _LcNmAccessExtensionTable_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 7, 15)
)
if mibBuilder.loadTexts:
    lcNmAccessExtensionTable.setStatus("current")
_LcNmAccessExtensionEntry_Object = MibTableRow
lcNmAccessExtensionEntry = _LcNmAccessExtensionEntry_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 7, 15, 1)
)
if mibBuilder.loadTexts:
    lcNmAccessExtensionEntry.setStatus("current")


class _LcNmAccessAdditionalPrivileges_Type(Bits):
    """Custom type lcNmAccessAdditionalPrivileges based on Bits"""
    namedValues = NamedValues(
        *(("accountManager", 1),
          ("resetAllowed", 0))
    )

_LcNmAccessAdditionalPrivileges_Type.__name__ = "Bits"
_LcNmAccessAdditionalPrivileges_Object = MibTableColumn
lcNmAccessAdditionalPrivileges = _LcNmAccessAdditionalPrivileges_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 7, 15, 1, 1),
    _LcNmAccessAdditionalPrivileges_Type()
)
lcNmAccessAdditionalPrivileges.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lcNmAccessAdditionalPrivileges.setStatus("current")


class _LcIpFiltIcmp9_Type(Integer32):
    """Custom type lcIpFiltIcmp9 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_LcIpFiltIcmp9_Type.__name__ = "Integer32"
_LcIpFiltIcmp9_Object = MibScalar
lcIpFiltIcmp9 = _LcIpFiltIcmp9_Object(
    (1, 3, 6, 1, 4, 1, 482, 60, 7, 16),
    _LcIpFiltIcmp9_Type()
)
lcIpFiltIcmp9.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcIpFiltIcmp9.setStatus("current")
docsDevNmAccessEntry.registerAugmentions(
    ("LANCITY-MCNS-MIB",
     "lcNmAccessExtensionEntry")
)
lcNmAccessExtensionEntry.setIndexNames(*docsDevNmAccessEntry.getIndexNames())

# Managed Objects groups


# Notification objects

lcErrKernelFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 100)
)
lcErrKernelFailure.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrKernelFailure.setStatus(
        ""
    )

lcErrNuSendItemFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 101)
)
lcErrNuSendItemFailure.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrNuSendItemFailure.setStatus(
        ""
    )

lcErrUnknown = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 200)
)
lcErrUnknown.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrUnknown.setStatus(
        ""
    )

lcErrSystemError = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 201)
)
lcErrSystemError.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrSystemError.setStatus(
        ""
    )

lcErrTest = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 202)
)
lcErrTest.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrTest.setStatus(
        ""
    )

lcErrAssert = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 203)
)
lcErrAssert.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrAssert.setStatus(
        ""
    )

lcErrShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 204)
)
lcErrShutdown.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrShutdown.setStatus(
        ""
    )

lcErrFshReset = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 205)
)
lcErrFshReset.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrFshReset.setStatus(
        ""
    )

lcErrRptReset = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 206)
)
lcErrRptReset.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrRptReset.setStatus(
        ""
    )

lcErrSystemError2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 207)
)
lcErrSystemError2.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrSystemError2.setStatus(
        ""
    )

lcErrWatchdogReset = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 208)
)
lcErrWatchdogReset.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrWatchdogReset.setStatus(
        ""
    )

lcMsgBacktrace = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 209)
)
lcMsgBacktrace.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcMsgBacktrace.setStatus(
        ""
    )

lcMsgBacktraceEnded = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 210)
)
lcMsgBacktraceEnded.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcMsgBacktraceEnded.setStatus(
        ""
    )

lcMsgBacktrace2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 211)
)
lcMsgBacktrace2.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcMsgBacktrace2.setStatus(
        ""
    )

lcMsgDSMakeHistoryEntry = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 212)
)
lcMsgDSMakeHistoryEntry.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcMsgDSMakeHistoryEntry.setStatus(
        ""
    )

lcMsgPowerSwitchCrash = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 213)
)
lcMsgPowerSwitchCrash.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcMsgPowerSwitchCrash.setStatus(
        ""
    )

lcMsgNullEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 214)
)
lcMsgNullEvent.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcMsgNullEvent.setStatus(
        ""
    )

lcErrRegMemory = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 300)
)
lcErrRegMemory.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrRegMemory.setStatus(
        ""
    )

lcErrRegRestartRegistration = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 301)
)
lcErrRegRestartRegistration.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrRegRestartRegistration.setStatus(
        ""
    )

lcErrRegNoInitSid = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 302)
)
lcErrRegNoInitSid.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrRegNoInitSid.setStatus(
        ""
    )

lcErrRegRangingFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 303)
)
lcErrRegRangingFailed.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrRegRangingFailed.setStatus(
        ""
    )

lcErrRegInvalidRanging = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 304)
)
lcErrRegInvalidRanging.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrRegInvalidRanging.setStatus(
        ""
    )

lcErrRegRangingTimeout = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 305)
)
lcErrRegRangingTimeout.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrRegRangingTimeout.setStatus(
        ""
    )

lcErrRegInvalidRegistration = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 306)
)
lcErrRegInvalidRegistration.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrRegInvalidRegistration.setStatus(
        ""
    )

lcErrRegNoModemIp = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 307)
)
lcErrRegNoModemIp.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrRegNoModemIp.setStatus(
        ""
    )

lcErrRegNoIpAtAll = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 308)
)
lcErrRegNoIpAtAll.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrRegNoIpAtAll.setStatus(
        ""
    )

lcErrRegUnpackingFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 309)
)
lcErrRegUnpackingFail.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrRegUnpackingFail.setStatus(
        ""
    )

lcErrRegRegisteredAlready = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 310)
)
lcErrRegRegisteredAlready.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrRegRegisteredAlready.setStatus(
        ""
    )

lcErrRegValidationFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 311)
)
lcErrRegValidationFail.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrRegValidationFail.setStatus(
        ""
    )

lcErrRegNoRegSid = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 312)
)
lcErrRegNoRegSid.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrRegNoRegSid.setStatus(
        ""
    )

lcErrCmctrlGenericEmergency = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 400)
)
lcErrCmctrlGenericEmergency.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrCmctrlGenericEmergency.setStatus(
        ""
    )

lcErrCmctrlGenericDebug = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 401)
)
lcErrCmctrlGenericDebug.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrCmctrlGenericDebug.setStatus(
        ""
    )

lcErrCmctrlUccNotSupported = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 402)
)
lcErrCmctrlUccNotSupported.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrCmctrlUccNotSupported.setStatus(
        ""
    )

lcErrCtInvalidEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 403)
)
lcErrCtInvalidEvent.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrCtInvalidEvent.setStatus(
        ""
    )

lcErrLossOfSynch = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 404)
)
lcErrLossOfSynch.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrLossOfSynch.setStatus(
        ""
    )

lcErrAcquiredSynch = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 405)
)
lcErrAcquiredSynch.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrAcquiredSynch.setStatus(
        ""
    )

lcErrCmctrlUcdComplete = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 406)
)
lcErrCmctrlUcdComplete.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrCmctrlUcdComplete.setStatus(
        ""
    )

lcErrCmctrlUccRx = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 407)
)
lcErrCmctrlUccRx.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrCmctrlUccRx.setStatus(
        ""
    )

lcErrRescan = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 408)
)
lcErrRescan.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrRescan.setStatus(
        ""
    )

lcErrLostPulse = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 409)
)
lcErrLostPulse.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrLostPulse.setStatus(
        ""
    )

lcErrLostSynch = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 410)
)
lcErrLostSynch.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrLostSynch.setStatus(
        ""
    )

lcErrIrqPhy1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 411)
)
lcErrIrqPhy1.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrIrqPhy1.setStatus(
        ""
    )

lcErrIrqPhy2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 412)
)
lcErrIrqPhy2.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrIrqPhy2.setStatus(
        ""
    )

lcErrCtRangeAbort = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 413)
)
lcErrCtRangeAbort.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrCtRangeAbort.setStatus(
        ""
    )

lcErrCtTxAdjustments = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 414)
)
lcErrCtTxAdjustments.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrCtTxAdjustments.setStatus(
        ""
    )

lcErrCtRangingComplete = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 415)
)
lcErrCtRangingComplete.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrCtRangingComplete.setStatus(
        ""
    )

lcErrUnexpectedBpdu = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 500)
)
lcErrUnexpectedBpdu.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrUnexpectedBpdu.setStatus(
        ""
    )

lcErrAllocatorInternal = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 600)
)
lcErrAllocatorInternal.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrAllocatorInternal.setStatus(
        ""
    )

lcErrAllocatorResource = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 601)
)
lcErrAllocatorResource.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrAllocatorResource.setStatus(
        ""
    )

lcErrHedpBufCountError = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 700)
)
lcErrHedpBufCountError.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrHedpBufCountError.setStatus(
        ""
    )

lcErrHedpIpSecurityAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 701)
)
lcErrHedpIpSecurityAlarm.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrHedpIpSecurityAlarm.setStatus(
        ""
    )

lcErrHedpMacSecurityAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 702)
)
lcErrHedpMacSecurityAlarm.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrHedpMacSecurityAlarm.setStatus(
        ""
    )

lcErrHedpHashResources = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 703)
)
lcErrHedpHashResources.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrHedpHashResources.setStatus(
        ""
    )

lcErrHedpHashLookup = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 704)
)
lcErrHedpHashLookup.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrHedpHashLookup.setStatus(
        ""
    )

lcErrHedpInvalidMacFrame = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 705)
)
lcErrHedpInvalidMacFrame.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrHedpInvalidMacFrame.setStatus(
        ""
    )

lcErrHedpNonsupportedEhdr = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 706)
)
lcErrHedpNonsupportedEhdr.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrHedpNonsupportedEhdr.setStatus(
        ""
    )

lcErrHedpInvalidEhdr = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 707)
)
lcErrHedpInvalidEhdr.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrHedpInvalidEhdr.setStatus(
        ""
    )

lcErrHedpLookupFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 708)
)
lcErrHedpLookupFailed.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrHedpLookupFailed.setStatus(
        ""
    )

lcErrHedpMtdDebug = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 709)
)
lcErrHedpMtdDebug.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrHedpMtdDebug.setStatus(
        ""
    )

lcErrHedpInvalidEhdr28 = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 710)
)
lcErrHedpInvalidEhdr28.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrHedpInvalidEhdr28.setStatus(
        ""
    )

lcErrHedpInvalidEhdr56 = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 711)
)
lcErrHedpInvalidEhdr56.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrHedpInvalidEhdr56.setStatus(
        ""
    )

lcErrHedpInvalidEhdr84 = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 712)
)
lcErrHedpInvalidEhdr84.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrHedpInvalidEhdr84.setStatus(
        ""
    )

lcErrHedpInvalidEhdr112 = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 713)
)
lcErrHedpInvalidEhdr112.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrHedpInvalidEhdr112.setStatus(
        ""
    )

lcErrHedpMtdOccurred = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 714)
)
lcErrHedpMtdOccurred.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrHedpMtdOccurred.setStatus(
        ""
    )

lcErrHedpMtdOccurred2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 715)
)
lcErrHedpMtdOccurred2.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrHedpMtdOccurred2.setStatus(
        ""
    )

lcErrHedpMtdOccurred3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 716)
)
lcErrHedpMtdOccurred3.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrHedpMtdOccurred3.setStatus(
        ""
    )

lcErrHedpDhcpTrace = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 717)
)
lcErrHedpDhcpTrace.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrHedpDhcpTrace.setStatus(
        ""
    )

lcErrHedpDescNotSupported = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 718)
)
lcErrHedpDescNotSupported.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrHedpDescNotSupported.setStatus(
        ""
    )

lcErrHedpRxTooLong = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 719)
)
lcErrHedpRxTooLong.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrHedpRxTooLong.setStatus(
        ""
    )

lcErrHedpDump1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 720)
)
lcErrHedpDump1.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrHedpDump1.setStatus(
        ""
    )

lcErrHedpDump2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 721)
)
lcErrHedpDump2.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrHedpDump2.setStatus(
        ""
    )

lcErrSmGenericEmergency = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 800)
)
lcErrSmGenericEmergency.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrSmGenericEmergency.setStatus(
        ""
    )

lcErrSmGenericDebug = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 801)
)
lcErrSmGenericDebug.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrSmGenericDebug.setStatus(
        ""
    )

lcErrSmMallocFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 802)
)
lcErrSmMallocFailure.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrSmMallocFailure.setStatus(
        ""
    )

lcErrSmFreeFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 803)
)
lcErrSmFreeFailure.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrSmFreeFailure.setStatus(
        ""
    )

lcErrSmRestart = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 804)
)
lcErrSmRestart.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrSmRestart.setStatus(
        ""
    )

lcErrSmTempTooHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 805)
)
lcErrSmTempTooHigh.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrSmTempTooHigh.setStatus(
        ""
    )

lcErrSmProcSpeedNotice = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 806)
)
lcErrSmProcSpeedNotice.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrSmProcSpeedNotice.setStatus(
        ""
    )

lcSmProcNoTimeServerDhcp = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 807)
)
lcSmProcNoTimeServerDhcp.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcSmProcNoTimeServerDhcp.setStatus(
        ""
    )

lcSmProcTimeServerDhcp = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 808)
)
lcSmProcTimeServerDhcp.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcSmProcTimeServerDhcp.setStatus(
        ""
    )

lcSmProcTimeServerContacted = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 809)
)
lcSmProcTimeServerContacted.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcSmProcTimeServerContacted.setStatus(
        ""
    )

lcSmProcTimeServerNotContacted = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 810)
)
lcSmProcTimeServerNotContacted.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcSmProcTimeServerNotContacted.setStatus(
        ""
    )

lcErrSmBadTrapType = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 811)
)
lcErrSmBadTrapType.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrSmBadTrapType.setStatus(
        ""
    )

lcErrSmBadTrapMsgCreation = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 812)
)
lcErrSmBadTrapMsgCreation.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrSmBadTrapMsgCreation.setStatus(
        ""
    )

lcErrSmMibPrvsnError = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 813)
)
lcErrSmMibPrvsnError.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrSmMibPrvsnError.setStatus(
        ""
    )

lcDhcpMissingBasic = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 814)
)
lcDhcpMissingBasic.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcDhcpMissingBasic.setStatus(
        ""
    )

lcDhcpMissingRequired = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 815)
)
lcDhcpMissingRequired.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcDhcpMissingRequired.setStatus(
        ""
    )

lcDhcpMissingRouter = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 816)
)
lcDhcpMissingRouter.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcDhcpMissingRouter.setStatus(
        ""
    )

lcSmTimeserverIcmp = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 817)
)
lcSmTimeserverIcmp.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcSmTimeserverIcmp.setStatus(
        ""
    )

lcErrPrvsnGenericError = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 819)
)
lcErrPrvsnGenericError.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrPrvsnGenericError.setStatus(
        ""
    )

lcErrSmGenericInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 820)
)
lcErrSmGenericInformation.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrSmGenericInformation.setStatus(
        ""
    )

lcErrSmTftpFileTooBig = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 821)
)
lcErrSmTftpFileTooBig.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrSmTftpFileTooBig.setStatus(
        ""
    )

lcErrSmDhcpGotNak = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 822)
)
lcErrSmDhcpGotNak.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrSmDhcpGotNak.setStatus(
        ""
    )

lcErrSmDhcpIncompleteOffer = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 823)
)
lcErrSmDhcpIncompleteOffer.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrSmDhcpIncompleteOffer.setStatus(
        ""
    )

lcErrSmDhcpNoOffer = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 824)
)
lcErrSmDhcpNoOffer.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrSmDhcpNoOffer.setStatus(
        ""
    )

lcErrSmDhcpSentDecline = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 825)
)
lcErrSmDhcpSentDecline.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrSmDhcpSentDecline.setStatus(
        ""
    )

lcErrSmBootpRelayCantWork = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 826)
)
lcErrSmBootpRelayCantWork.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrSmBootpRelayCantWork.setStatus(
        ""
    )

lcErrSmBootpRelayNowWorks = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 827)
)
lcErrSmBootpRelayNowWorks.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrSmBootpRelayNowWorks.setStatus(
        ""
    )

lcErrFiltGenericDebug = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 1200)
)
lcErrFiltGenericDebug.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrFiltGenericDebug.setStatus(
        ""
    )

lcErrFiltInvalidFlashValue = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 1201)
)
lcErrFiltInvalidFlashValue.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrFiltInvalidFlashValue.setStatus(
        ""
    )

lcErrFiltIpTblEntryNotActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 1202)
)
lcErrFiltIpTblEntryNotActive.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrFiltIpTblEntryNotActive.setStatus(
        ""
    )

lcErrFiltLlcTblEntryNotActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 1203)
)
lcErrFiltLlcTblEntryNotActive.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrFiltLlcTblEntryNotActive.setStatus(
        ""
    )

lcErrFiltGenericInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 1204)
)
lcErrFiltGenericInformation.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrFiltGenericInformation.setStatus(
        ""
    )

lcErrSmSwUpgradeGenericNotice = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 1300)
)
lcErrSmSwUpgradeGenericNotice.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrSmSwUpgradeGenericNotice.setStatus(
        ""
    )

lcErrSmSwUpgradeFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 1301)
)
lcErrSmSwUpgradeFail.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrSmSwUpgradeFail.setStatus(
        ""
    )

lcErrSmSwUpgradeFailReset = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 1302)
)
lcErrSmSwUpgradeFailReset.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrSmSwUpgradeFailReset.setStatus(
        ""
    )

lcErrSmSwUpgradeCompletion = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 1303)
)
lcErrSmSwUpgradeCompletion.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrSmSwUpgradeCompletion.setStatus(
        ""
    )

lcErrSmSwUpgradeCancelled = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 1304)
)
lcErrSmSwUpgradeCancelled.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrSmSwUpgradeCancelled.setStatus(
        ""
    )

lcErrSmSwUpgradeOverride = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 1305)
)
lcErrSmSwUpgradeOverride.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrSmSwUpgradeOverride.setStatus(
        ""
    )

lcErrSmFlashProgrammingError = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 1306)
)
lcErrSmFlashProgrammingError.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrSmFlashProgrammingError.setStatus(
        ""
    )

lcErrSmFlashProgrammingErrorReset = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 1307)
)
lcErrSmFlashProgrammingErrorReset.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrSmFlashProgrammingErrorReset.setStatus(
        ""
    )

lcErrSmFlashEraseFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 1308)
)
lcErrSmFlashEraseFail.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrSmFlashEraseFail.setStatus(
        ""
    )

lcErrSmFlashEraseFailReset = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 1309)
)
lcErrSmFlashEraseFailReset.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrSmFlashEraseFailReset.setStatus(
        ""
    )

lcErrSmFlashCorruptionReset = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 1310)
)
lcErrSmFlashCorruptionReset.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrSmFlashCorruptionReset.setStatus(
        ""
    )

lcErrSmFlashBlockInvalidReset = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 1311)
)
lcErrSmFlashBlockInvalidReset.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrSmFlashBlockInvalidReset.setStatus(
        ""
    )

lcErrSmSwUpgradeTftpError = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 1312)
)
lcErrSmSwUpgradeTftpError.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrSmSwUpgradeTftpError.setStatus(
        ""
    )

lcErrSmSwUpgradeTftpErrorReset = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 1313)
)
lcErrSmSwUpgradeTftpErrorReset.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrSmSwUpgradeTftpErrorReset.setStatus(
        ""
    )

lcErrSmSwUpgradeAllocFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 1314)
)
lcErrSmSwUpgradeAllocFail.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrSmSwUpgradeAllocFail.setStatus(
        ""
    )

lcErrSmSwUpgradeGenericError = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 1315)
)
lcErrSmSwUpgradeGenericError.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrSmSwUpgradeGenericError.setStatus(
        ""
    )

lcErrSmSwUpgradeProductError = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 1316)
)
lcErrSmSwUpgradeProductError.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrSmSwUpgradeProductError.setStatus(
        ""
    )

lcErrSmSwUpgradeTftpMsg = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 1317)
)
lcErrSmSwUpgradeTftpMsg.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrSmSwUpgradeTftpMsg.setStatus(
        ""
    )

lcErrScnBadFrequency = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 1400)
)
lcErrScnBadFrequency.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrScnBadFrequency.setStatus(
        ""
    )

lcScnTunerBroken = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 1401)
)
lcScnTunerBroken.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcScnTunerBroken.setStatus(
        ""
    )

lcScnTunerHung = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 1402)
)
lcScnTunerHung.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcScnTunerHung.setStatus(
        ""
    )

lcScnStartUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 1403)
)
lcScnStartUp.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcScnStartUp.setStatus(
        ""
    )

lcErrCliGeneral = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 1500)
)
lcErrCliGeneral.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrCliGeneral.setStatus(
        ""
    )

lcInfoCliLogin = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 1501)
)
lcInfoCliLogin.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcInfoCliLogin.setStatus(
        ""
    )

lcInfoCliLogout = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 1502)
)
lcInfoCliLogout.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcInfoCliLogout.setStatus(
        ""
    )

lcInfoCliLoginFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 1503)
)
lcInfoCliLoginFail.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcInfoCliLoginFail.setStatus(
        ""
    )

lcInfoCliSessionTimeout = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 1504)
)
lcInfoCliSessionTimeout.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcInfoCliSessionTimeout.setStatus(
        ""
    )

lcInfoCliCommand = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 1505)
)
lcInfoCliCommand.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcInfoCliCommand.setStatus(
        ""
    )

lcInfoCliConsoleSnmpSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 1506)
)
lcInfoCliConsoleSnmpSet.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcInfoCliConsoleSnmpSet.setStatus(
        ""
    )

lcInfoCliTelnetSnmpSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 1507)
)
lcInfoCliTelnetSnmpSet.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcInfoCliTelnetSnmpSet.setStatus(
        ""
    )

lcErrBcmInitFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 1600)
)
lcErrBcmInitFailure.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrBcmInitFailure.setStatus(
        ""
    )

lcMsgNoPowerTables = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 1601)
)
lcMsgNoPowerTables.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcMsgNoPowerTables.setStatus(
        ""
    )

lcErrBcmReceiverHwRev = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 1602)
)
lcErrBcmReceiverHwRev.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrBcmReceiverHwRev.setStatus(
        ""
    )

lcErrCmMtd = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 1700)
)
lcErrCmMtd.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrCmMtd.setStatus(
        ""
    )

lcErrCmPciParity = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 1701)
)
lcErrCmPciParity.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrCmPciParity.setStatus(
        ""
    )

lcErrMibSnmpReset = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 1800)
)
lcErrMibSnmpReset.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrMibSnmpReset.setStatus(
        ""
    )

lcMcastJoin = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 1850)
)
lcMcastJoin.setObjects(
    ("LANCITY-MCNS-MIB", "lcMcastTrapAddress")
)
if mibBuilder.loadTexts:
    lcMcastJoin.setStatus(
        ""
    )

lcErrGalPciParity = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 1900)
)
lcErrGalPciParity.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrGalPciParity.setStatus(
        ""
    )

lcErrBpEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 2000)
)
lcErrBpEnabled.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrBpEnabled.setStatus(
        ""
    )

lcErrBpHardwareInitFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 2001)
)
lcErrBpHardwareInitFailure.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrBpHardwareInitFailure.setStatus(
        ""
    )

lcErrBpKeyWriteFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 2002)
)
lcErrBpKeyWriteFailure.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrBpKeyWriteFailure.setStatus(
        ""
    )

lcErrBpVectWriteFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 2003)
)
lcErrBpVectWriteFailure.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrBpVectWriteFailure.setStatus(
        ""
    )

lcErrBpHardcodedRsaKeyPair = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 2004)
)
lcErrBpHardcodedRsaKeyPair.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrBpHardcodedRsaKeyPair.setStatus(
        ""
    )

lcErrHebpAuthEncryptFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 2100)
)
lcErrHebpAuthEncryptFailure.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrHebpAuthEncryptFailure.setStatus(
        ""
    )

lcErrHebpHardwareInitFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 2101)
)
lcErrHebpHardwareInitFailure.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrHebpHardwareInitFailure.setStatus(
        ""
    )

lcErrHebpKeyWriteFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 2102)
)
lcErrHebpKeyWriteFailure.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrHebpKeyWriteFailure.setStatus(
        ""
    )

lcErrHebpVectWriteFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 2103)
)
lcErrHebpVectWriteFailure.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrHebpVectWriteFailure.setStatus(
        ""
    )

lcErrHebpMacsDontMatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 2104)
)
lcErrHebpMacsDontMatch.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrHebpMacsDontMatch.setStatus(
        ""
    )

lcErrHebpAttemptedPubKeyChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 2105)
)
lcErrHebpAttemptedPubKeyChange.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrHebpAttemptedPubKeyChange.setStatus(
        ""
    )

lcErrCruInitFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 2200)
)
lcErrCruInitFailure.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrCruInitFailure.setStatus(
        ""
    )

lcErrMfgTlvReadError = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 2300)
)
lcErrMfgTlvReadError.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrMfgTlvReadError.setStatus(
        ""
    )

lcErrUcNoHw = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 2400)
)
lcErrUcNoHw.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrUcNoHw.setStatus(
        ""
    )

lcErrUcNoCal = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 2401)
)
lcErrUcNoCal.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrUcNoCal.setStatus(
        ""
    )

lcErrUcNoLock = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 2402)
)
lcErrUcNoLock.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrUcNoLock.setStatus(
        ""
    )

lcErrUcPowerSupply = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 2403)
)
lcErrUcPowerSupply.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrUcPowerSupply.setStatus(
        ""
    )

lcErrUcOutputPower = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 2404)
)
lcErrUcOutputPower.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrUcOutputPower.setStatus(
        ""
    )

lcErrPacDsConfigFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 2500)
)
lcErrPacDsConfigFailure.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrPacDsConfigFailure.setStatus(
        ""
    )

lcErrPacUsConfigFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 2501)
)
lcErrPacUsConfigFailure.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrPacUsConfigFailure.setStatus(
        ""
    )

lcPacDsCenterFreqChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 2502)
)
lcPacDsCenterFreqChange.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcPacDsCenterFreqChange.setStatus(
        ""
    )

lcPacDsBandwidthChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 2503)
)
lcPacDsBandwidthChange.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcPacDsBandwidthChange.setStatus(
        ""
    )

lcPacDsModulationChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 2504)
)
lcPacDsModulationChange.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcPacDsModulationChange.setStatus(
        ""
    )

lcPacDsInterleaveChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 2505)
)
lcPacDsInterleaveChange.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcPacDsInterleaveChange.setStatus(
        ""
    )

lcPacDsPowerChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 2506)
)
lcPacDsPowerChange.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcPacDsPowerChange.setStatus(
        ""
    )

lcErrTestMacHeader = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 2600)
)
lcErrTestMacHeader.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrTestMacHeader.setStatus(
        ""
    )

lcErrTestEhdr20 = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 2601)
)
lcErrTestEhdr20.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrTestEhdr20.setStatus(
        ""
    )

lcIngressAvoidanceActionTaken = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 2700)
)
lcIngressAvoidanceActionTaken.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcIngressAvoidanceActionTaken.setStatus(
        ""
    )

lcErrCruFrontFanStatusOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 2800)
)
lcErrCruFrontFanStatusOff.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrCruFrontFanStatusOff.setStatus(
        ""
    )

lcErrCruFrontFanStatusOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 2801)
)
lcErrCruFrontFanStatusOn.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrCruFrontFanStatusOn.setStatus(
        ""
    )

lcErrCruMiddleFanStatusOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 2802)
)
lcErrCruMiddleFanStatusOff.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrCruMiddleFanStatusOff.setStatus(
        ""
    )

lcErrCruMiddleFanStatusOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 2803)
)
lcErrCruMiddleFanStatusOn.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrCruMiddleFanStatusOn.setStatus(
        ""
    )

lcErrCruBackFanStatusOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 2804)
)
lcErrCruBackFanStatusOff.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrCruBackFanStatusOff.setStatus(
        ""
    )

lcErrCruBackFanStatusOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 2805)
)
lcErrCruBackFanStatusOn.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrCruBackFanStatusOn.setStatus(
        ""
    )

lcErrTelnetMallocFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 3000)
)
lcErrTelnetMallocFailure.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrTelnetMallocFailure.setStatus(
        ""
    )

lcErrTelnetFreeFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 3001)
)
lcErrTelnetFreeFailure.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrTelnetFreeFailure.setStatus(
        ""
    )

lcErrTelnetTcbCreateFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 3002)
)
lcErrTelnetTcbCreateFailure.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrTelnetTcbCreateFailure.setStatus(
        ""
    )

lcErrTelnetTnCreateListenerFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 3003)
)
lcErrTelnetTnCreateListenerFailure.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrTelnetTnCreateListenerFailure.setStatus(
        ""
    )

lcErrTelnetTcpStartFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 482, 0, 3004)
)
lcErrTelnetTcpStartFailure.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText")
)
if mibBuilder.loadTexts:
    lcErrTelnetTcpStartFailure.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LANCITY-MCNS-MIB",
    **{"lcErrKernelFailure": lcErrKernelFailure,
       "lcErrNuSendItemFailure": lcErrNuSendItemFailure,
       "lcErrUnknown": lcErrUnknown,
       "lcErrSystemError": lcErrSystemError,
       "lcErrTest": lcErrTest,
       "lcErrAssert": lcErrAssert,
       "lcErrShutdown": lcErrShutdown,
       "lcErrFshReset": lcErrFshReset,
       "lcErrRptReset": lcErrRptReset,
       "lcErrSystemError2": lcErrSystemError2,
       "lcErrWatchdogReset": lcErrWatchdogReset,
       "lcMsgBacktrace": lcMsgBacktrace,
       "lcMsgBacktraceEnded": lcMsgBacktraceEnded,
       "lcMsgBacktrace2": lcMsgBacktrace2,
       "lcMsgDSMakeHistoryEntry": lcMsgDSMakeHistoryEntry,
       "lcMsgPowerSwitchCrash": lcMsgPowerSwitchCrash,
       "lcMsgNullEvent": lcMsgNullEvent,
       "lcErrRegMemory": lcErrRegMemory,
       "lcErrRegRestartRegistration": lcErrRegRestartRegistration,
       "lcErrRegNoInitSid": lcErrRegNoInitSid,
       "lcErrRegRangingFailed": lcErrRegRangingFailed,
       "lcErrRegInvalidRanging": lcErrRegInvalidRanging,
       "lcErrRegRangingTimeout": lcErrRegRangingTimeout,
       "lcErrRegInvalidRegistration": lcErrRegInvalidRegistration,
       "lcErrRegNoModemIp": lcErrRegNoModemIp,
       "lcErrRegNoIpAtAll": lcErrRegNoIpAtAll,
       "lcErrRegUnpackingFail": lcErrRegUnpackingFail,
       "lcErrRegRegisteredAlready": lcErrRegRegisteredAlready,
       "lcErrRegValidationFail": lcErrRegValidationFail,
       "lcErrRegNoRegSid": lcErrRegNoRegSid,
       "lcErrCmctrlGenericEmergency": lcErrCmctrlGenericEmergency,
       "lcErrCmctrlGenericDebug": lcErrCmctrlGenericDebug,
       "lcErrCmctrlUccNotSupported": lcErrCmctrlUccNotSupported,
       "lcErrCtInvalidEvent": lcErrCtInvalidEvent,
       "lcErrLossOfSynch": lcErrLossOfSynch,
       "lcErrAcquiredSynch": lcErrAcquiredSynch,
       "lcErrCmctrlUcdComplete": lcErrCmctrlUcdComplete,
       "lcErrCmctrlUccRx": lcErrCmctrlUccRx,
       "lcErrRescan": lcErrRescan,
       "lcErrLostPulse": lcErrLostPulse,
       "lcErrLostSynch": lcErrLostSynch,
       "lcErrIrqPhy1": lcErrIrqPhy1,
       "lcErrIrqPhy2": lcErrIrqPhy2,
       "lcErrCtRangeAbort": lcErrCtRangeAbort,
       "lcErrCtTxAdjustments": lcErrCtTxAdjustments,
       "lcErrCtRangingComplete": lcErrCtRangingComplete,
       "lcErrUnexpectedBpdu": lcErrUnexpectedBpdu,
       "lcErrAllocatorInternal": lcErrAllocatorInternal,
       "lcErrAllocatorResource": lcErrAllocatorResource,
       "lcErrHedpBufCountError": lcErrHedpBufCountError,
       "lcErrHedpIpSecurityAlarm": lcErrHedpIpSecurityAlarm,
       "lcErrHedpMacSecurityAlarm": lcErrHedpMacSecurityAlarm,
       "lcErrHedpHashResources": lcErrHedpHashResources,
       "lcErrHedpHashLookup": lcErrHedpHashLookup,
       "lcErrHedpInvalidMacFrame": lcErrHedpInvalidMacFrame,
       "lcErrHedpNonsupportedEhdr": lcErrHedpNonsupportedEhdr,
       "lcErrHedpInvalidEhdr": lcErrHedpInvalidEhdr,
       "lcErrHedpLookupFailed": lcErrHedpLookupFailed,
       "lcErrHedpMtdDebug": lcErrHedpMtdDebug,
       "lcErrHedpInvalidEhdr28": lcErrHedpInvalidEhdr28,
       "lcErrHedpInvalidEhdr56": lcErrHedpInvalidEhdr56,
       "lcErrHedpInvalidEhdr84": lcErrHedpInvalidEhdr84,
       "lcErrHedpInvalidEhdr112": lcErrHedpInvalidEhdr112,
       "lcErrHedpMtdOccurred": lcErrHedpMtdOccurred,
       "lcErrHedpMtdOccurred2": lcErrHedpMtdOccurred2,
       "lcErrHedpMtdOccurred3": lcErrHedpMtdOccurred3,
       "lcErrHedpDhcpTrace": lcErrHedpDhcpTrace,
       "lcErrHedpDescNotSupported": lcErrHedpDescNotSupported,
       "lcErrHedpRxTooLong": lcErrHedpRxTooLong,
       "lcErrHedpDump1": lcErrHedpDump1,
       "lcErrHedpDump2": lcErrHedpDump2,
       "lcErrSmGenericEmergency": lcErrSmGenericEmergency,
       "lcErrSmGenericDebug": lcErrSmGenericDebug,
       "lcErrSmMallocFailure": lcErrSmMallocFailure,
       "lcErrSmFreeFailure": lcErrSmFreeFailure,
       "lcErrSmRestart": lcErrSmRestart,
       "lcErrSmTempTooHigh": lcErrSmTempTooHigh,
       "lcErrSmProcSpeedNotice": lcErrSmProcSpeedNotice,
       "lcSmProcNoTimeServerDhcp": lcSmProcNoTimeServerDhcp,
       "lcSmProcTimeServerDhcp": lcSmProcTimeServerDhcp,
       "lcSmProcTimeServerContacted": lcSmProcTimeServerContacted,
       "lcSmProcTimeServerNotContacted": lcSmProcTimeServerNotContacted,
       "lcErrSmBadTrapType": lcErrSmBadTrapType,
       "lcErrSmBadTrapMsgCreation": lcErrSmBadTrapMsgCreation,
       "lcErrSmMibPrvsnError": lcErrSmMibPrvsnError,
       "lcDhcpMissingBasic": lcDhcpMissingBasic,
       "lcDhcpMissingRequired": lcDhcpMissingRequired,
       "lcDhcpMissingRouter": lcDhcpMissingRouter,
       "lcSmTimeserverIcmp": lcSmTimeserverIcmp,
       "lcErrPrvsnGenericError": lcErrPrvsnGenericError,
       "lcErrSmGenericInformation": lcErrSmGenericInformation,
       "lcErrSmTftpFileTooBig": lcErrSmTftpFileTooBig,
       "lcErrSmDhcpGotNak": lcErrSmDhcpGotNak,
       "lcErrSmDhcpIncompleteOffer": lcErrSmDhcpIncompleteOffer,
       "lcErrSmDhcpNoOffer": lcErrSmDhcpNoOffer,
       "lcErrSmDhcpSentDecline": lcErrSmDhcpSentDecline,
       "lcErrSmBootpRelayCantWork": lcErrSmBootpRelayCantWork,
       "lcErrSmBootpRelayNowWorks": lcErrSmBootpRelayNowWorks,
       "lcErrFiltGenericDebug": lcErrFiltGenericDebug,
       "lcErrFiltInvalidFlashValue": lcErrFiltInvalidFlashValue,
       "lcErrFiltIpTblEntryNotActive": lcErrFiltIpTblEntryNotActive,
       "lcErrFiltLlcTblEntryNotActive": lcErrFiltLlcTblEntryNotActive,
       "lcErrFiltGenericInformation": lcErrFiltGenericInformation,
       "lcErrSmSwUpgradeGenericNotice": lcErrSmSwUpgradeGenericNotice,
       "lcErrSmSwUpgradeFail": lcErrSmSwUpgradeFail,
       "lcErrSmSwUpgradeFailReset": lcErrSmSwUpgradeFailReset,
       "lcErrSmSwUpgradeCompletion": lcErrSmSwUpgradeCompletion,
       "lcErrSmSwUpgradeCancelled": lcErrSmSwUpgradeCancelled,
       "lcErrSmSwUpgradeOverride": lcErrSmSwUpgradeOverride,
       "lcErrSmFlashProgrammingError": lcErrSmFlashProgrammingError,
       "lcErrSmFlashProgrammingErrorReset": lcErrSmFlashProgrammingErrorReset,
       "lcErrSmFlashEraseFail": lcErrSmFlashEraseFail,
       "lcErrSmFlashEraseFailReset": lcErrSmFlashEraseFailReset,
       "lcErrSmFlashCorruptionReset": lcErrSmFlashCorruptionReset,
       "lcErrSmFlashBlockInvalidReset": lcErrSmFlashBlockInvalidReset,
       "lcErrSmSwUpgradeTftpError": lcErrSmSwUpgradeTftpError,
       "lcErrSmSwUpgradeTftpErrorReset": lcErrSmSwUpgradeTftpErrorReset,
       "lcErrSmSwUpgradeAllocFail": lcErrSmSwUpgradeAllocFail,
       "lcErrSmSwUpgradeGenericError": lcErrSmSwUpgradeGenericError,
       "lcErrSmSwUpgradeProductError": lcErrSmSwUpgradeProductError,
       "lcErrSmSwUpgradeTftpMsg": lcErrSmSwUpgradeTftpMsg,
       "lcErrScnBadFrequency": lcErrScnBadFrequency,
       "lcScnTunerBroken": lcScnTunerBroken,
       "lcScnTunerHung": lcScnTunerHung,
       "lcScnStartUp": lcScnStartUp,
       "lcErrCliGeneral": lcErrCliGeneral,
       "lcInfoCliLogin": lcInfoCliLogin,
       "lcInfoCliLogout": lcInfoCliLogout,
       "lcInfoCliLoginFail": lcInfoCliLoginFail,
       "lcInfoCliSessionTimeout": lcInfoCliSessionTimeout,
       "lcInfoCliCommand": lcInfoCliCommand,
       "lcInfoCliConsoleSnmpSet": lcInfoCliConsoleSnmpSet,
       "lcInfoCliTelnetSnmpSet": lcInfoCliTelnetSnmpSet,
       "lcErrBcmInitFailure": lcErrBcmInitFailure,
       "lcMsgNoPowerTables": lcMsgNoPowerTables,
       "lcErrBcmReceiverHwRev": lcErrBcmReceiverHwRev,
       "lcErrCmMtd": lcErrCmMtd,
       "lcErrCmPciParity": lcErrCmPciParity,
       "lcErrMibSnmpReset": lcErrMibSnmpReset,
       "lcMcastJoin": lcMcastJoin,
       "lcErrGalPciParity": lcErrGalPciParity,
       "lcErrBpEnabled": lcErrBpEnabled,
       "lcErrBpHardwareInitFailure": lcErrBpHardwareInitFailure,
       "lcErrBpKeyWriteFailure": lcErrBpKeyWriteFailure,
       "lcErrBpVectWriteFailure": lcErrBpVectWriteFailure,
       "lcErrBpHardcodedRsaKeyPair": lcErrBpHardcodedRsaKeyPair,
       "lcErrHebpAuthEncryptFailure": lcErrHebpAuthEncryptFailure,
       "lcErrHebpHardwareInitFailure": lcErrHebpHardwareInitFailure,
       "lcErrHebpKeyWriteFailure": lcErrHebpKeyWriteFailure,
       "lcErrHebpVectWriteFailure": lcErrHebpVectWriteFailure,
       "lcErrHebpMacsDontMatch": lcErrHebpMacsDontMatch,
       "lcErrHebpAttemptedPubKeyChange": lcErrHebpAttemptedPubKeyChange,
       "lcErrCruInitFailure": lcErrCruInitFailure,
       "lcErrMfgTlvReadError": lcErrMfgTlvReadError,
       "lcErrUcNoHw": lcErrUcNoHw,
       "lcErrUcNoCal": lcErrUcNoCal,
       "lcErrUcNoLock": lcErrUcNoLock,
       "lcErrUcPowerSupply": lcErrUcPowerSupply,
       "lcErrUcOutputPower": lcErrUcOutputPower,
       "lcErrPacDsConfigFailure": lcErrPacDsConfigFailure,
       "lcErrPacUsConfigFailure": lcErrPacUsConfigFailure,
       "lcPacDsCenterFreqChange": lcPacDsCenterFreqChange,
       "lcPacDsBandwidthChange": lcPacDsBandwidthChange,
       "lcPacDsModulationChange": lcPacDsModulationChange,
       "lcPacDsInterleaveChange": lcPacDsInterleaveChange,
       "lcPacDsPowerChange": lcPacDsPowerChange,
       "lcErrTestMacHeader": lcErrTestMacHeader,
       "lcErrTestEhdr20": lcErrTestEhdr20,
       "lcIngressAvoidanceActionTaken": lcIngressAvoidanceActionTaken,
       "lcErrCruFrontFanStatusOff": lcErrCruFrontFanStatusOff,
       "lcErrCruFrontFanStatusOn": lcErrCruFrontFanStatusOn,
       "lcErrCruMiddleFanStatusOff": lcErrCruMiddleFanStatusOff,
       "lcErrCruMiddleFanStatusOn": lcErrCruMiddleFanStatusOn,
       "lcErrCruBackFanStatusOff": lcErrCruBackFanStatusOff,
       "lcErrCruBackFanStatusOn": lcErrCruBackFanStatusOn,
       "lcErrTelnetMallocFailure": lcErrTelnetMallocFailure,
       "lcErrTelnetFreeFailure": lcErrTelnetFreeFailure,
       "lcErrTelnetTcbCreateFailure": lcErrTelnetTcbCreateFailure,
       "lcErrTelnetTnCreateListenerFailure": lcErrTelnetTnCreateListenerFailure,
       "lcErrTelnetTcpStartFailure": lcErrTelnetTcpStartFailure,
       "lancityMcnsMib": lancityMcnsMib,
       "lancityMcnsProducts": lancityMcnsProducts,
       "lancityMcnsProdIdCMTS": lancityMcnsProdIdCMTS,
       "lancityMcnsProdIdCM": lancityMcnsProdIdCM,
       "lccmtsif": lccmtsif,
       "lcCmtsUpstreamTable": lcCmtsUpstreamTable,
       "lcCmtsUpstreamEntry": lcCmtsUpstreamEntry,
       "lcCmtsUpMinimumMapSize": lcCmtsUpMinimumMapSize,
       "lcCmtsUpMaximumMapSize": lcCmtsUpMaximumMapSize,
       "lcCmtsUpContentionPerMap": lcCmtsUpContentionPerMap,
       "lcCmtsUpRequestDataAllowed": lcCmtsUpRequestDataAllowed,
       "lcCmtsUpMaxDataInContention": lcCmtsUpMaxDataInContention,
       "lcCmtsUpInitialRangingInterval": lcCmtsUpInitialRangingInterval,
       "lcCmtsUpHighPriorityThreshold": lcCmtsUpHighPriorityThreshold,
       "lcCmtsUpGuaranteedThreshold": lcCmtsUpGuaranteedThreshold,
       "lcCmtsUpPublicationDelay": lcCmtsUpPublicationDelay,
       "lcCmtsUpNFlowControlledMaps": lcCmtsUpNFlowControlledMaps,
       "lcCmtsUpNNonFlowControlledMaps": lcCmtsUpNNonFlowControlledMaps,
       "lcCmtsUpChannelPower": lcCmtsUpChannelPower,
       "lcCmtsUpInputPowerWindow": lcCmtsUpInputPowerWindow,
       "lcCmtsCurrentTemp": lcCmtsCurrentTemp,
       "lcCmtsHighTempThreshold": lcCmtsHighTempThreshold,
       "lccmtsUpstreamIngressAvoidance": lccmtsUpstreamIngressAvoidance,
       "lcCmtsUpstreamIngressAvoidanceEnableTable": lcCmtsUpstreamIngressAvoidanceEnableTable,
       "lcCmtsIngressAvoidanceEnableEntry": lcCmtsIngressAvoidanceEnableEntry,
       "lcCmtsIngressAvoidanceEnable": lcCmtsIngressAvoidanceEnable,
       "lcCmtsMetric1Enable": lcCmtsMetric1Enable,
       "lcCmtsIngressAvoidanceFrequencyConfigTable": lcCmtsIngressAvoidanceFrequencyConfigTable,
       "lcCmtsIngressAvoidanceFrequencyConfigEntry": lcCmtsIngressAvoidanceFrequencyConfigEntry,
       "lcCmtsCarrierPathIndex": lcCmtsCarrierPathIndex,
       "lcCmtsFreqConfigIndex": lcCmtsFreqConfigIndex,
       "lcCmtsFreqAvailable": lcCmtsFreqAvailable,
       "lcCmtsStartFrequency": lcCmtsStartFrequency,
       "lcCmtsStopFrequency": lcCmtsStopFrequency,
       "lcCmtsIngressAvoidanceChangePrefTable": lcCmtsIngressAvoidanceChangePrefTable,
       "lcCmtsIngressAvoidanceChangePrefEntry": lcCmtsIngressAvoidanceChangePrefEntry,
       "lcCmtsChangePreference": lcCmtsChangePreference,
       "lcCmtsIngressAvoidanceThresholdTable": lcCmtsIngressAvoidanceThresholdTable,
       "lcCmtsIngressAvoidanceThresholdEntry": lcCmtsIngressAvoidanceThresholdEntry,
       "lcCmtsMetric1GreenToYellow": lcCmtsMetric1GreenToYellow,
       "lcCmtsMetric1YellowToRed": lcCmtsMetric1YellowToRed,
       "lcCmtsIngressAvoidanceProfileTable": lcCmtsIngressAvoidanceProfileTable,
       "lcCmtsIngressAvoidanceProfileEntry": lcCmtsIngressAvoidanceProfileEntry,
       "lcCmtsProfileCarrierPathIndex": lcCmtsProfileCarrierPathIndex,
       "lcCmtsProfilePreference": lcCmtsProfilePreference,
       "lcCmtsStatus": lcCmtsStatus,
       "lcCmtsTransmissionProfileIndex": lcCmtsTransmissionProfileIndex,
       "lcCmtsIngressAvoidanceTxProfileTable": lcCmtsIngressAvoidanceTxProfileTable,
       "lcCmtsIngressAvoidanceTxProfileEntry": lcCmtsIngressAvoidanceTxProfileEntry,
       "lcCmtsTxProfileIndex": lcCmtsTxProfileIndex,
       "lcCmtsModulationProfileIndex": lcCmtsModulationProfileIndex,
       "lcCmtsBandwidth": lcCmtsBandwidth,
       "lcCmtsCodingEfficiency": lcCmtsCodingEfficiency,
       "lcCmtsIngressAvoidanceMetricConfigTable": lcCmtsIngressAvoidanceMetricConfigTable,
       "lcCmtsIngressAvoidanceMetricConfigEntry": lcCmtsIngressAvoidanceMetricConfigEntry,
       "lcCmtsMetricIndex": lcCmtsMetricIndex,
       "lcCmtsAgingMultiplier": lcCmtsAgingMultiplier,
       "lcCmtsCalculationTimer": lcCmtsCalculationTimer,
       "lcCmtsIngressAvoidanceFreqStatusTable": lcCmtsIngressAvoidanceFreqStatusTable,
       "lcCmtsIngressAvoidanceFreqStatusEntry": lcCmtsIngressAvoidanceFreqStatusEntry,
       "lcCmtsFreqStatusCarrierPathIndex": lcCmtsFreqStatusCarrierPathIndex,
       "lcCmtsFreqStatusFreqIndex": lcCmtsFreqStatusFreqIndex,
       "lcCmtsFreqStatusFreq": lcCmtsFreqStatusFreq,
       "lcCmtsFreqStatusFc": lcCmtsFreqStatusFc,
       "lcCmtsFreqStatusAvailable": lcCmtsFreqStatusAvailable,
       "lcCmtsFreqStatusStatus": lcCmtsFreqStatusStatus,
       "lcCmtsFreqStatusTimeLastUsed": lcCmtsFreqStatusTimeLastUsed,
       "lcCmtsFreqStatusUpTime": lcCmtsFreqStatusUpTime,
       "lcCmtsUpstreamIngressAvoidanceHealthTable": lcCmtsUpstreamIngressAvoidanceHealthTable,
       "lcCmtsIngressAvoidanceHealthEntry": lcCmtsIngressAvoidanceHealthEntry,
       "lcCmtsHealthProfile": lcCmtsHealthProfile,
       "lcCmtsHealthFc": lcCmtsHealthFc,
       "lcCmtsHealthUpTime": lcCmtsHealthUpTime,
       "lcCmtsMetric1Status": lcCmtsMetric1Status,
       "lcCmtsMetric1Value": lcCmtsMetric1Value,
       "lcCmtsMultiUsConfigTable": lcCmtsMultiUsConfigTable,
       "lcCmtsMultiUsConfigEntry": lcCmtsMultiUsConfigEntry,
       "lcCmtsCarrierPath": lcCmtsCarrierPath,
       "lcCmtsChannelGroup": lcCmtsChannelGroup,
       "lcCmtsFrontFanOn": lcCmtsFrontFanOn,
       "lcCmtsMiddleFanOn": lcCmtsMiddleFanOn,
       "lcCmtsBackFanOn": lcCmtsBackFanOn,
       "lccmtsifconfig": lccmtsifconfig,
       "lcCmtsAnnex": lcCmtsAnnex,
       "lcCmtsFrequencySplit": lcCmtsFrequencySplit,
       "lcEvSyslog2": lcEvSyslog2,
       "lcEvSyslog3": lcEvSyslog3,
       "lcCpeMacToCmMacTable": lcCpeMacToCmMacTable,
       "lcCpeMacToCmMacEntry": lcCpeMacToCmMacEntry,
       "lcCpeMac": lcCpeMac,
       "lcCmMac": lcCmMac,
       "lcCmCountsTable": lcCmCountsTable,
       "lcCmCountsEntry": lcCmCountsEntry,
       "lcCmCountsRowNum": lcCmCountsRowNum,
       "lcActiveCmCounts": lcActiveCmCounts,
       "lcRegisteredCmCounts": lcRegisteredCmCounts,
       "lccmif": lccmif,
       "lcifcommon": lcifcommon,
       "lccmtsdevice": lccmtsdevice,
       "lccmtsProvisioning": lccmtsProvisioning,
       "lcProvisioningControl": lcProvisioningControl,
       "lcConfigIpAddress": lcConfigIpAddress,
       "lcConfigIpSubnet": lcConfigIpSubnet,
       "lcConfigIpGateway": lcConfigIpGateway,
       "lcConfigTftpAddress": lcConfigTftpAddress,
       "lcConfigTftpFilename": lcConfigTftpFilename,
       "lcConfigTimeServerAddress": lcConfigTimeServerAddress,
       "lcConfigTimeoffset": lcConfigTimeoffset,
       "lcConfigSNTPAddress": lcConfigSNTPAddress,
       "lcSerialPortTable": lcSerialPortTable,
       "lcSerialPortEntry": lcSerialPortEntry,
       "lcSerialPortNumber": lcSerialPortNumber,
       "lcSerialPortBaudRate": lcSerialPortBaudRate,
       "lcSerialPortDataBits": lcSerialPortDataBits,
       "lcSerialPortParity": lcSerialPortParity,
       "lcSerialPortStopBits": lcSerialPortStopBits,
       "lcSerialPortModemEnable": lcSerialPortModemEnable,
       "lcModemVendorTable": lcModemVendorTable,
       "lcModemVendorEntry": lcModemVendorEntry,
       "lcModemVendorIndex": lcModemVendorIndex,
       "lcModemVendorControl": lcModemVendorControl,
       "lcModemVendorMacAddress": lcModemVendorMacAddress,
       "lcModemVendorMask": lcModemVendorMask,
       "lccmtsDPStatistics": lccmtsDPStatistics,
       "lcDPStatisticsInterval": lcDPStatisticsInterval,
       "lcDPStatisticsTable": lcDPStatisticsTable,
       "lcDPStatisticsEntry": lcDPStatisticsEntry,
       "lcDPStatisticsTxFrameRate": lcDPStatisticsTxFrameRate,
       "lcDPStatisticsRxFrameRate": lcDPStatisticsRxFrameRate,
       "lcDPStatisticsTxOctetRate": lcDPStatisticsTxOctetRate,
       "lcDPStatisticsRxOctetRate": lcDPStatisticsRxOctetRate,
       "lccmtsDPConfiguration": lccmtsDPConfiguration,
       "lcForwardingMode": lcForwardingMode,
       "lcProxyArp": lcProxyArp,
       "lcProxyArpTimeout": lcProxyArpTimeout,
       "lcArpSpoofingProtection": lcArpSpoofingProtection,
       "lcFunnelMode": lcFunnelMode,
       "lcDeregCmAgeTime": lcDeregCmAgeTime,
       "lcRngNotRegCmAgeTime": lcRngNotRegCmAgeTime,
       "lcUsedot1dTpAgingTime": lcUsedot1dTpAgingTime,
       "lccmtsHwRevisions": lccmtsHwRevisions,
       "lccmtsHwRevArbCPLD": lccmtsHwRevArbCPLD,
       "lccmtsHwRevTxCPLD": lccmtsHwRevTxCPLD,
       "lccmtsHwRevAFFPGA": lccmtsHwRevAFFPGA,
       "lccmtsHwRevGT64010": lccmtsHwRevGT64010,
       "lccmtsHwRevPLX9080": lccmtsHwRevPLX9080,
       "lccmtsHwRevBCM3210": lccmtsHwRevBCM3210,
       "lccmtsHwRevBCM3033": lccmtsHwRevBCM3033,
       "lccmtsHwRevSunset": lccmtsHwRevSunset,
       "lccmtsHwRevDEC21143": lccmtsHwRevDEC21143,
       "lccmtsHwRevLXT970A": lccmtsHwRevLXT970A,
       "lccmtsHwRevLXT970B": lccmtsHwRevLXT970B,
       "lccmtsHwRevRfRxTable": lccmtsHwRevRfRxTable,
       "lccmtsHwRevRfRxEntry": lccmtsHwRevRfRxEntry,
       "lccmtsHwRevBCM3137": lccmtsHwRevBCM3137,
       "lccmtsHwRevRipsaw": lccmtsHwRevRipsaw,
       "lccmtsPoliceTolerance": lccmtsPoliceTolerance,
       "lccmtsUpPolice": lccmtsUpPolice,
       "lccmtsDnPolice": lccmtsDnPolice,
       "lccmtsBOOTPRelay": lccmtsBOOTPRelay,
       "lccmtsBOOTPRelayControl": lccmtsBOOTPRelayControl,
       "lccmtsBOOTPRelaySvrTargetTable": lccmtsBOOTPRelaySvrTargetTable,
       "lccmtsBOOTPRelaySvrTargetEntry": lccmtsBOOTPRelaySvrTargetEntry,
       "lccmtsBOOTPRelayIndex": lccmtsBOOTPRelayIndex,
       "lccmtsBOOTPRelaySvrTargetIP": lccmtsBOOTPRelaySvrTargetIP,
       "lccmtsBOOTPRelayClntSelectionMask": lccmtsBOOTPRelayClntSelectionMask,
       "lccmtsBOOTPRelaySvrTargetHits": lccmtsBOOTPRelaySvrTargetHits,
       "lccmtsBOOTPRelayRowStatus": lccmtsBOOTPRelayRowStatus,
       "lccmtsBOOTPRelayBadLengthDiscards": lccmtsBOOTPRelayBadLengthDiscards,
       "lccmtsBOOTPRelayLocalOriginDiscards": lccmtsBOOTPRelayLocalOriginDiscards,
       "lccmtsBOOTPRelayExcessiveHopsDiscards": lccmtsBOOTPRelayExcessiveHopsDiscards,
       "lccmtsBOOTPRelayGatewayAddrCopies": lccmtsBOOTPRelayGatewayAddrCopies,
       "lccmtsBOOTPRelayLocalAddrSinks": lccmtsBOOTPRelayLocalAddrSinks,
       "lccmtsBOOTPRelayWrongGatewayAddrDiscards": lccmtsBOOTPRelayWrongGatewayAddrDiscards,
       "lccmtsBOOTPRelayNoCopyBufDiscards": lccmtsBOOTPRelayNoCopyBufDiscards,
       "lccmtsBOOTPRelayMiscSilentDiscards": lccmtsBOOTPRelayMiscSilentDiscards,
       "lccmtsBOOTPRelayNoEpilBufDiscards": lccmtsBOOTPRelayNoEpilBufDiscards,
       "lccmtsBOOTPRelayClntDstPortDiscards": lccmtsBOOTPRelayClntDstPortDiscards,
       "lccmtsBOOTPRelayRawRequests": lccmtsBOOTPRelayRawRequests,
       "lccmtsBOOTPRelayRawReplies": lccmtsBOOTPRelayRawReplies,
       "lccmtsBOOTPRelayRqstFromCM": lccmtsBOOTPRelayRqstFromCM,
       "lccmtsBOOTPRelayRqstFromCPE": lccmtsBOOTPRelayRqstFromCPE,
       "lccmtsBOOTPRelayDPCATVPuts": lccmtsBOOTPRelayDPCATVPuts,
       "lccmtsBOOTPRelayDPEnetPuts": lccmtsBOOTPRelayDPEnetPuts,
       "lccmtsBOOTPRelayEpilUDPBufSends": lccmtsBOOTPRelayEpilUDPBufSends,
       "lccmtsBOOTPRelayNullMACTags": lccmtsBOOTPRelayNullMACTags,
       "lccmtsBOOTPRelayNonNullMACTags": lccmtsBOOTPRelayNonNullMACTags,
       "lccmtsBOOTPRelayWrongPortRqstDiscards": lccmtsBOOTPRelayWrongPortRqstDiscards,
       "lccmtsBOOTPRelayWrongPortReplyDiscards": lccmtsBOOTPRelayWrongPortReplyDiscards,
       "lccmtsDNSResolver": lccmtsDNSResolver,
       "lccmtsDNSResolverControl": lccmtsDNSResolverControl,
       "lccmtsDNSResolverServiceType": lccmtsDNSResolverServiceType,
       "lccmtsDNSResolverServersCfgd": lccmtsDNSResolverServersCfgd,
       "lccmtsDNSResolverServerTable": lccmtsDNSResolverServerTable,
       "lccmtsDNSResolverServerEntry": lccmtsDNSResolverServerEntry,
       "lccmtsDNSResolverIndex": lccmtsDNSResolverIndex,
       "lccmtsDNSResolverServerIP": lccmtsDNSResolverServerIP,
       "lccmtsDNSResolverServerPriority": lccmtsDNSResolverServerPriority,
       "lccmtsDNSResolverServerName": lccmtsDNSResolverServerName,
       "lccmtsDNSResolverRowStatus": lccmtsDNSResolverRowStatus,
       "lccmtsDevServer": lccmtsDevServer,
       "lccmtsDevServerBootState": lccmtsDevServerBootState,
       "lccmtsDevServerDhcp": lccmtsDevServerDhcp,
       "lccmtsDevServerTime": lccmtsDevServerTime,
       "lccmtsDevServerTftp": lccmtsDevServerTftp,
       "lccmtsDevServerConfigFile": lccmtsDevServerConfigFile,
       "lccmdevice": lccmdevice,
       "lcScanningFrequencyTable": lcScanningFrequencyTable,
       "lcScanningFrequencyEntry": lcScanningFrequencyEntry,
       "lcScanControl": lcScanControl,
       "lcScanIndex": lcScanIndex,
       "lcScanFreqStart": lcScanFreqStart,
       "lcScanFreqEnd": lcScanFreqEnd,
       "lcScanUseHrc": lcScanUseHrc,
       "lcScanStep": lcScanStep,
       "lcScanChannelWidth": lcScanChannelWidth,
       "lccmAddress": lccmAddress,
       "lccmIpAddress": lccmIpAddress,
       "lccmIpSubnet": lccmIpSubnet,
       "lcdevicecommon": lcdevicecommon,
       "lcTrapTypeTable": lcTrapTypeTable,
       "lcTrapTypeEntry": lcTrapTypeEntry,
       "lcTrapTypeIndex": lcTrapTypeIndex,
       "lcTrapTypeStatus": lcTrapTypeStatus,
       "lcBootedAlbumFilename": lcBootedAlbumFilename,
       "lcBootedAlbumSequenceNumber": lcBootedAlbumSequenceNumber,
       "lctrapvars": lctrapvars,
       "lcAuthFailErrorStatus": lcAuthFailErrorStatus,
       "lcAuthFailCommunityString": lcAuthFailCommunityString,
       "lcAuthFailIpAddr": lcAuthFailIpAddr,
       "lcAuthFailInterface": lcAuthFailInterface,
       "lcIpFiltSendDu": lcIpFiltSendDu,
       "lcMulticastGroup": lcMulticastGroup,
       "lcMcastControl": lcMcastControl,
       "lcMcastAddressTable": lcMcastAddressTable,
       "lcMcastAddressEntry": lcMcastAddressEntry,
       "lcMcastAddress": lcMcastAddress,
       "lcMcastAdminState": lcMcastAdminState,
       "lcMcastOperState": lcMcastOperState,
       "lcMcastTtl": lcMcastTtl,
       "lcMcastTrapAddress": lcMcastTrapAddress,
       "lcRestartFromFactoryDefaults": lcRestartFromFactoryDefaults,
       "lcPhyTable": lcPhyTable,
       "lcPhyEntry": lcPhyEntry,
       "lcPhyIndex": lcPhyIndex,
       "lcPhyEnable": lcPhyEnable,
       "lcPhyAutoNegotiate": lcPhyAutoNegotiate,
       "lcPhyActive": lcPhyActive,
       "lcPhySpeed": lcPhySpeed,
       "lcPhyFullDuplex": lcPhyFullDuplex,
       "lcStickyYellowTable": lcStickyYellowTable,
       "lcStickyYellowEntry": lcStickyYellowEntry,
       "lcStickyYellowIndex": lcStickyYellowIndex,
       "lcStickyYellowPad": lcStickyYellowPad,
       "lcResetFilters": lcResetFilters,
       "lcResetNmAccessTable": lcResetNmAccessTable,
       "lcFlashPersistenceSwitch": lcFlashPersistenceSwitch,
       "lcConcatenationEnabled": lcConcatenationEnabled,
       "lcConsoleAccess": lcConsoleAccess,
       "lcConsoleUserTable": lcConsoleUserTable,
       "lcConsoleUserEntry": lcConsoleUserEntry,
       "lcConsoleUserIndex": lcConsoleUserIndex,
       "lcConsoleUserStatus": lcConsoleUserStatus,
       "lcConsoleUserName": lcConsoleUserName,
       "lcConsoleUserPassword": lcConsoleUserPassword,
       "lcConsoleUserLevel": lcConsoleUserLevel,
       "lcConsoleLevelTable": lcConsoleLevelTable,
       "lcConsoleLevelEntry": lcConsoleLevelEntry,
       "lcConsoleLevelIndex": lcConsoleLevelIndex,
       "lcConsoleLevelStatus": lcConsoleLevelStatus,
       "lcConsoleLevelName": lcConsoleLevelName,
       "lcConsoleLevelMethod": lcConsoleLevelMethod,
       "lcConsoleLevelSecurityName": lcConsoleLevelSecurityName,
       "lcTelnetAllowedSessions": lcTelnetAllowedSessions,
       "lcSessionInactivityTimeout": lcSessionInactivityTimeout,
       "lcNmAccessExtensionTable": lcNmAccessExtensionTable,
       "lcNmAccessExtensionEntry": lcNmAccessExtensionEntry,
       "lcNmAccessAdditionalPrivileges": lcNmAccessAdditionalPrivileges,
       "lcIpFiltIcmp9": lcIpFiltIcmp9}
)
