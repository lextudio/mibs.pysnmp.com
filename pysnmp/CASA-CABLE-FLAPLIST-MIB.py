# SNMP MIB module (CASA-CABLE-FLAPLIST-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CASA-CABLE-FLAPLIST-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:53:38 2024
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

(casa,) = mibBuilder.importSymbols(
    "CASA-MIB",
    "casa")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

casaFlapListMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 20858, 10, 11)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CasaMgmt_ObjectIdentity = ObjectIdentity
casaMgmt = _CasaMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20858, 10)
)
_CasaFlapListMIBObjects_ObjectIdentity = ObjectIdentity
casaFlapListMIBObjects = _CasaFlapListMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20858, 10, 11, 1)
)
_CasaFlapListGlobal_ObjectIdentity = ObjectIdentity
casaFlapListGlobal = _CasaFlapListGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20858, 10, 11, 1, 1)
)


class _CasaFlapInsertionTime_Type(Unsigned32):
    """Custom type casaFlapInsertionTime based on Unsigned32"""
    defaultValue = 60


_CasaFlapInsertionTime_Object = MibScalar
casaFlapInsertionTime = _CasaFlapInsertionTime_Object(
    (1, 3, 6, 1, 4, 1, 20858, 10, 11, 1, 1, 1),
    _CasaFlapInsertionTime_Type()
)
casaFlapInsertionTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    casaFlapInsertionTime.setStatus("current")
if mibBuilder.loadTexts:
    casaFlapInsertionTime.setUnits("seconds")


class _CasaFlapMissThreshold_Type(Unsigned32):
    """Custom type casaFlapMissThreshold based on Unsigned32"""
    defaultValue = 6

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_CasaFlapMissThreshold_Type.__name__ = "Unsigned32"
_CasaFlapMissThreshold_Object = MibScalar
casaFlapMissThreshold = _CasaFlapMissThreshold_Object(
    (1, 3, 6, 1, 4, 1, 20858, 10, 11, 1, 1, 2),
    _CasaFlapMissThreshold_Type()
)
casaFlapMissThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    casaFlapMissThreshold.setStatus("current")
if mibBuilder.loadTexts:
    casaFlapMissThreshold.setUnits("times")


class _CasaFlapPowerAdjThreshold_Type(Unsigned32):
    """Custom type casaFlapPowerAdjThreshold based on Unsigned32"""
    defaultValue = 2


_CasaFlapPowerAdjThreshold_Object = MibScalar
casaFlapPowerAdjThreshold = _CasaFlapPowerAdjThreshold_Object(
    (1, 3, 6, 1, 4, 1, 20858, 10, 11, 1, 1, 3),
    _CasaFlapPowerAdjThreshold_Type()
)
casaFlapPowerAdjThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    casaFlapPowerAdjThreshold.setStatus("current")
if mibBuilder.loadTexts:
    casaFlapPowerAdjThreshold.setUnits("dB")


class _CasaFlapListAging_Type(Unsigned32):
    """Custom type casaFlapListAging based on Unsigned32"""
    defaultValue = 10080

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15, 86400),
    )


_CasaFlapListAging_Type.__name__ = "Unsigned32"
_CasaFlapListAging_Object = MibScalar
casaFlapListAging = _CasaFlapListAging_Object(
    (1, 3, 6, 1, 4, 1, 20858, 10, 11, 1, 1, 4),
    _CasaFlapListAging_Type()
)
casaFlapListAging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    casaFlapListAging.setStatus("current")
if mibBuilder.loadTexts:
    casaFlapListAging.setUnits("minutes")


class _CasaFlapListMaxSize_Type(Unsigned32):
    """Custom type casaFlapListMaxSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CasaFlapListMaxSize_Type.__name__ = "Unsigned32"
_CasaFlapListMaxSize_Object = MibScalar
casaFlapListMaxSize = _CasaFlapListMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 20858, 10, 11, 1, 1, 5),
    _CasaFlapListMaxSize_Type()
)
casaFlapListMaxSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    casaFlapListMaxSize.setStatus("current")
if mibBuilder.loadTexts:
    casaFlapListMaxSize.setUnits("entries")
_CasaFlapListResetAll_Type = TruthValue
_CasaFlapListResetAll_Object = MibScalar
casaFlapListResetAll = _CasaFlapListResetAll_Object(
    (1, 3, 6, 1, 4, 1, 20858, 10, 11, 1, 1, 6),
    _CasaFlapListResetAll_Type()
)
casaFlapListResetAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    casaFlapListResetAll.setStatus("current")
_CasaFlapListLastResetTime_Type = DateAndTime
_CasaFlapListLastResetTime_Object = MibScalar
casaFlapListLastResetTime = _CasaFlapListLastResetTime_Object(
    (1, 3, 6, 1, 4, 1, 20858, 10, 11, 1, 1, 7),
    _CasaFlapListLastResetTime_Type()
)
casaFlapListLastResetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casaFlapListLastResetTime.setStatus("current")
_CasaFlapListClearAll_Type = TruthValue
_CasaFlapListClearAll_Object = MibScalar
casaFlapListClearAll = _CasaFlapListClearAll_Object(
    (1, 3, 6, 1, 4, 1, 20858, 10, 11, 1, 1, 8),
    _CasaFlapListClearAll_Type()
)
casaFlapListClearAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    casaFlapListClearAll.setStatus("current")
_CasaFlapListLastClearTime_Type = DateAndTime
_CasaFlapListLastClearTime_Object = MibScalar
casaFlapListLastClearTime = _CasaFlapListLastClearTime_Object(
    (1, 3, 6, 1, 4, 1, 20858, 10, 11, 1, 1, 9),
    _CasaFlapListLastClearTime_Type()
)
casaFlapListLastClearTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casaFlapListLastClearTime.setStatus("current")


class _CasaFlapListCheckInterval_Type(Unsigned32):
    """Custom type casaFlapListCheckInterval based on Unsigned32"""
    defaultValue = 120


_CasaFlapListCheckInterval_Object = MibScalar
casaFlapListCheckInterval = _CasaFlapListCheckInterval_Object(
    (1, 3, 6, 1, 4, 1, 20858, 10, 11, 1, 1, 10),
    _CasaFlapListCheckInterval_Type()
)
casaFlapListCheckInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    casaFlapListCheckInterval.setStatus("current")
if mibBuilder.loadTexts:
    casaFlapListCheckInterval.setUnits("minutes")
_CasaFlapListTable_Object = MibTable
casaFlapListTable = _CasaFlapListTable_Object(
    (1, 3, 6, 1, 4, 1, 20858, 10, 11, 1, 2)
)
if mibBuilder.loadTexts:
    casaFlapListTable.setStatus("current")
_CasaFlapListEntry_Object = MibTableRow
casaFlapListEntry = _CasaFlapListEntry_Object(
    (1, 3, 6, 1, 4, 1, 20858, 10, 11, 1, 2, 1)
)
casaFlapListEntry.setIndexNames(
    (0, "CASA-CABLE-FLAPLIST-MIB", "casaFlapCmMacAddress"),
)
if mibBuilder.loadTexts:
    casaFlapListEntry.setStatus("current")
_CasaFlapCmMacAddress_Type = MacAddress
_CasaFlapCmMacAddress_Object = MibTableColumn
casaFlapCmMacAddress = _CasaFlapCmMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 20858, 10, 11, 1, 2, 1, 1),
    _CasaFlapCmMacAddress_Type()
)
casaFlapCmMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casaFlapCmMacAddress.setStatus("current")
_CasaFlapCmUpstreamIfIndex_Type = Unsigned32
_CasaFlapCmUpstreamIfIndex_Object = MibTableColumn
casaFlapCmUpstreamIfIndex = _CasaFlapCmUpstreamIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 20858, 10, 11, 1, 2, 1, 2),
    _CasaFlapCmUpstreamIfIndex_Type()
)
casaFlapCmUpstreamIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casaFlapCmUpstreamIfIndex.setStatus("current")
_CasaFlapCmDownstreamIfIndex_Type = Unsigned32
_CasaFlapCmDownstreamIfIndex_Object = MibTableColumn
casaFlapCmDownstreamIfIndex = _CasaFlapCmDownstreamIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 20858, 10, 11, 1, 2, 1, 3),
    _CasaFlapCmDownstreamIfIndex_Type()
)
casaFlapCmDownstreamIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casaFlapCmDownstreamIfIndex.setStatus("current")
_CasaFlapCmInsertionFails_Type = Integer32
_CasaFlapCmInsertionFails_Object = MibTableColumn
casaFlapCmInsertionFails = _CasaFlapCmInsertionFails_Object(
    (1, 3, 6, 1, 4, 1, 20858, 10, 11, 1, 2, 1, 4),
    _CasaFlapCmInsertionFails_Type()
)
casaFlapCmInsertionFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casaFlapCmInsertionFails.setStatus("current")
if mibBuilder.loadTexts:
    casaFlapCmInsertionFails.setUnits("times")
_CasaFlapCmHits_Type = Unsigned32
_CasaFlapCmHits_Object = MibTableColumn
casaFlapCmHits = _CasaFlapCmHits_Object(
    (1, 3, 6, 1, 4, 1, 20858, 10, 11, 1, 2, 1, 5),
    _CasaFlapCmHits_Type()
)
casaFlapCmHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casaFlapCmHits.setStatus("current")
if mibBuilder.loadTexts:
    casaFlapCmHits.setUnits("times")
_CasaFlapCmMisses_Type = Unsigned32
_CasaFlapCmMisses_Object = MibTableColumn
casaFlapCmMisses = _CasaFlapCmMisses_Object(
    (1, 3, 6, 1, 4, 1, 20858, 10, 11, 1, 2, 1, 6),
    _CasaFlapCmMisses_Type()
)
casaFlapCmMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casaFlapCmMisses.setStatus("current")
if mibBuilder.loadTexts:
    casaFlapCmMisses.setUnits("times")
_CasaFlapCmCRCCounts_Type = Integer32
_CasaFlapCmCRCCounts_Object = MibTableColumn
casaFlapCmCRCCounts = _CasaFlapCmCRCCounts_Object(
    (1, 3, 6, 1, 4, 1, 20858, 10, 11, 1, 2, 1, 7),
    _CasaFlapCmCRCCounts_Type()
)
casaFlapCmCRCCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casaFlapCmCRCCounts.setStatus("current")
_CasaFlapCmPowerAdjustments_Type = Unsigned32
_CasaFlapCmPowerAdjustments_Object = MibTableColumn
casaFlapCmPowerAdjustments = _CasaFlapCmPowerAdjustments_Object(
    (1, 3, 6, 1, 4, 1, 20858, 10, 11, 1, 2, 1, 8),
    _CasaFlapCmPowerAdjustments_Type()
)
casaFlapCmPowerAdjustments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casaFlapCmPowerAdjustments.setStatus("current")
_CasaFlapCmFlapCounts_Type = Integer32
_CasaFlapCmFlapCounts_Object = MibTableColumn
casaFlapCmFlapCounts = _CasaFlapCmFlapCounts_Object(
    (1, 3, 6, 1, 4, 1, 20858, 10, 11, 1, 2, 1, 9),
    _CasaFlapCmFlapCounts_Type()
)
casaFlapCmFlapCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casaFlapCmFlapCounts.setStatus("current")
_CasaFlapCmLastFlapTime_Type = DateAndTime
_CasaFlapCmLastFlapTime_Object = MibTableColumn
casaFlapCmLastFlapTime = _CasaFlapCmLastFlapTime_Object(
    (1, 3, 6, 1, 4, 1, 20858, 10, 11, 1, 2, 1, 10),
    _CasaFlapCmLastFlapTime_Type()
)
casaFlapCmLastFlapTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casaFlapCmLastFlapTime.setStatus("current")
_CasaFlapCmFlapRowStatus_Type = RowStatus
_CasaFlapCmFlapRowStatus_Object = MibTableColumn
casaFlapCmFlapRowStatus = _CasaFlapCmFlapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 20858, 10, 11, 1, 2, 1, 11),
    _CasaFlapCmFlapRowStatus_Type()
)
casaFlapCmFlapRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    casaFlapCmFlapRowStatus.setStatus("current")
_CasaFlapListGroups_ObjectIdentity = ObjectIdentity
casaFlapListGroups = _CasaFlapListGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20858, 10, 11, 2)
)
_CasaFlapListCompliances_ObjectIdentity = ObjectIdentity
casaFlapListCompliances = _CasaFlapListCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20858, 10, 11, 3)
)

# Managed Objects groups

casaFlapListGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 20858, 10, 11, 2, 1)
)
casaFlapListGroup.setObjects(
      *(("CASA-CABLE-FLAPLIST-MIB", "casaFlapInsertionTime"),
        ("CASA-CABLE-FLAPLIST-MIB", "casaFlapMissThreshold"),
        ("CASA-CABLE-FLAPLIST-MIB", "casaFlapPowerAdjThreshold"),
        ("CASA-CABLE-FLAPLIST-MIB", "casaFlapListAging"),
        ("CASA-CABLE-FLAPLIST-MIB", "casaFlapListMaxSize"),
        ("CASA-CABLE-FLAPLIST-MIB", "casaFlapListResetAll"),
        ("CASA-CABLE-FLAPLIST-MIB", "casaFlapListLastResetTime"),
        ("CASA-CABLE-FLAPLIST-MIB", "casaFlapListClearAll"),
        ("CASA-CABLE-FLAPLIST-MIB", "casaFlapListLastClearTime"),
        ("CASA-CABLE-FLAPLIST-MIB", "casaFlapListCheckInterval"),
        ("CASA-CABLE-FLAPLIST-MIB", "casaFlapCmUpstreamIfIndex"),
        ("CASA-CABLE-FLAPLIST-MIB", "casaFlapCmDownstreamIfIndex"),
        ("CASA-CABLE-FLAPLIST-MIB", "casaFlapCmInsertionFails"),
        ("CASA-CABLE-FLAPLIST-MIB", "casaFlapCmHits"),
        ("CASA-CABLE-FLAPLIST-MIB", "casaFlapCmMisses"),
        ("CASA-CABLE-FLAPLIST-MIB", "casaFlapCmCRCCounts"),
        ("CASA-CABLE-FLAPLIST-MIB", "casaFlapCmPowerAdjustments"),
        ("CASA-CABLE-FLAPLIST-MIB", "casaFlapCmFlapCounts"),
        ("CASA-CABLE-FLAPLIST-MIB", "casaFlapCmLastFlapTime"),
        ("CASA-CABLE-FLAPLIST-MIB", "casaFlapCmFlapRowStatus"))
)
if mibBuilder.loadTexts:
    casaFlapListGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

casaFlapListCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 20858, 10, 11, 3, 1)
)
if mibBuilder.loadTexts:
    casaFlapListCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CASA-CABLE-FLAPLIST-MIB",
    **{"casaMgmt": casaMgmt,
       "casaFlapListMib": casaFlapListMib,
       "casaFlapListMIBObjects": casaFlapListMIBObjects,
       "casaFlapListGlobal": casaFlapListGlobal,
       "casaFlapInsertionTime": casaFlapInsertionTime,
       "casaFlapMissThreshold": casaFlapMissThreshold,
       "casaFlapPowerAdjThreshold": casaFlapPowerAdjThreshold,
       "casaFlapListAging": casaFlapListAging,
       "casaFlapListMaxSize": casaFlapListMaxSize,
       "casaFlapListResetAll": casaFlapListResetAll,
       "casaFlapListLastResetTime": casaFlapListLastResetTime,
       "casaFlapListClearAll": casaFlapListClearAll,
       "casaFlapListLastClearTime": casaFlapListLastClearTime,
       "casaFlapListCheckInterval": casaFlapListCheckInterval,
       "casaFlapListTable": casaFlapListTable,
       "casaFlapListEntry": casaFlapListEntry,
       "casaFlapCmMacAddress": casaFlapCmMacAddress,
       "casaFlapCmUpstreamIfIndex": casaFlapCmUpstreamIfIndex,
       "casaFlapCmDownstreamIfIndex": casaFlapCmDownstreamIfIndex,
       "casaFlapCmInsertionFails": casaFlapCmInsertionFails,
       "casaFlapCmHits": casaFlapCmHits,
       "casaFlapCmMisses": casaFlapCmMisses,
       "casaFlapCmCRCCounts": casaFlapCmCRCCounts,
       "casaFlapCmPowerAdjustments": casaFlapCmPowerAdjustments,
       "casaFlapCmFlapCounts": casaFlapCmFlapCounts,
       "casaFlapCmLastFlapTime": casaFlapCmLastFlapTime,
       "casaFlapCmFlapRowStatus": casaFlapCmFlapRowStatus,
       "casaFlapListGroups": casaFlapListGroups,
       "casaFlapListGroup": casaFlapListGroup,
       "casaFlapListCompliances": casaFlapListCompliances,
       "casaFlapListCompliance": casaFlapListCompliance}
)
