# SNMP MIB module (RDN-CABLE-SPECTRUM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RDN-CABLE-SPECTRUM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:45:59 2024
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

(InterfaceIndex,
 ifAdminStatus,
 ifIndex,
 ifOperStatus) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifAdminStatus",
    "ifIndex",
    "ifOperStatus")

(riverdelta,) = mibBuilder.importSymbols(
    "RDN-MIB",
    "riverdelta")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

rdnCableSpectrum = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4981, 6)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RdnCableSpectrumObjects_ObjectIdentity = ObjectIdentity
rdnCableSpectrumObjects = _RdnCableSpectrumObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4981, 6, 1)
)
_RdnFlapObjects_ObjectIdentity = ObjectIdentity
rdnFlapObjects = _RdnFlapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4981, 6, 1, 1)
)
_RdnFlapCmCmtsStatusTable_Object = MibTable
rdnFlapCmCmtsStatusTable = _RdnFlapCmCmtsStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4981, 6, 1, 1, 1)
)
if mibBuilder.loadTexts:
    rdnFlapCmCmtsStatusTable.setStatus("current")
_RdnFlapCmCmtsStatusEntry_Object = MibTableRow
rdnFlapCmCmtsStatusEntry = _RdnFlapCmCmtsStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4981, 6, 1, 1, 1, 1)
)
rdnFlapCmCmtsStatusEntry.setIndexNames(
    (0, "RDN-CABLE-SPECTRUM-MIB", "flapCmCmtsIfIndex"),
)
if mibBuilder.loadTexts:
    rdnFlapCmCmtsStatusEntry.setStatus("current")


class _FlapCmCmtsIfIndex_Type(Integer32):
    """Custom type flapCmCmtsIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_FlapCmCmtsIfIndex_Type.__name__ = "Integer32"
_FlapCmCmtsIfIndex_Object = MibTableColumn
flapCmCmtsIfIndex = _FlapCmCmtsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4981, 6, 1, 1, 1, 1, 1),
    _FlapCmCmtsIfIndex_Type()
)
flapCmCmtsIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    flapCmCmtsIfIndex.setStatus("current")


class _FlapListMaxSize_Type(Integer32):
    """Custom type flapListMaxSize based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )


_FlapListMaxSize_Type.__name__ = "Integer32"
_FlapListMaxSize_Object = MibTableColumn
flapListMaxSize = _FlapListMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 4981, 6, 1, 1, 1, 1, 2),
    _FlapListMaxSize_Type()
)
flapListMaxSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flapListMaxSize.setStatus("current")
if mibBuilder.loadTexts:
    flapListMaxSize.setUnits("modems")


class _FlapListCurrentSize_Type(Gauge32):
    """Custom type flapListCurrentSize based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8191),
    )


_FlapListCurrentSize_Type.__name__ = "Gauge32"
_FlapListCurrentSize_Object = MibTableColumn
flapListCurrentSize = _FlapListCurrentSize_Object(
    (1, 3, 6, 1, 4, 1, 4981, 6, 1, 1, 1, 1, 3),
    _FlapListCurrentSize_Type()
)
flapListCurrentSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flapListCurrentSize.setStatus("current")
if mibBuilder.loadTexts:
    flapListCurrentSize.setUnits("modems")


class _FlapAgingOutTime_Type(Integer32):
    """Custom type flapAgingOutTime based on Integer32"""
    defaultValue = 1440

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 86400),
    )


_FlapAgingOutTime_Type.__name__ = "Integer32"
_FlapAgingOutTime_Object = MibTableColumn
flapAgingOutTime = _FlapAgingOutTime_Object(
    (1, 3, 6, 1, 4, 1, 4981, 6, 1, 1, 1, 1, 4),
    _FlapAgingOutTime_Type()
)
flapAgingOutTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flapAgingOutTime.setStatus("current")
if mibBuilder.loadTexts:
    flapAgingOutTime.setUnits("minutes")


class _FlapInsertionTime_Type(Integer32):
    """Custom type flapInsertionTime based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 86400),
    )


_FlapInsertionTime_Type.__name__ = "Integer32"
_FlapInsertionTime_Object = MibTableColumn
flapInsertionTime = _FlapInsertionTime_Object(
    (1, 3, 6, 1, 4, 1, 4981, 6, 1, 1, 1, 1, 5),
    _FlapInsertionTime_Type()
)
flapInsertionTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flapInsertionTime.setStatus("current")
if mibBuilder.loadTexts:
    flapInsertionTime.setUnits("seconds")


class _FlapMissThreshold_Type(Integer32):
    """Custom type flapMissThreshold based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_FlapMissThreshold_Type.__name__ = "Integer32"
_FlapMissThreshold_Object = MibTableColumn
flapMissThreshold = _FlapMissThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4981, 6, 1, 1, 1, 1, 6),
    _FlapMissThreshold_Type()
)
flapMissThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flapMissThreshold.setStatus("current")
if mibBuilder.loadTexts:
    flapMissThreshold.setUnits("modem")


class _FlapPowerAdjThreshold_Type(Integer32):
    """Custom type flapPowerAdjThreshold based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_FlapPowerAdjThreshold_Type.__name__ = "Integer32"
_FlapPowerAdjThreshold_Object = MibTableColumn
flapPowerAdjThreshold = _FlapPowerAdjThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4981, 6, 1, 1, 1, 1, 7),
    _FlapPowerAdjThreshold_Type()
)
flapPowerAdjThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flapPowerAdjThreshold.setStatus("current")
if mibBuilder.loadTexts:
    flapPowerAdjThreshold.setUnits("dB")


class _FlapListPercentageThreshold_Type(Integer32):
    """Custom type flapListPercentageThreshold based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_FlapListPercentageThreshold_Type.__name__ = "Integer32"
_FlapListPercentageThreshold_Object = MibTableColumn
flapListPercentageThreshold = _FlapListPercentageThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4981, 6, 1, 1, 1, 1, 8),
    _FlapListPercentageThreshold_Type()
)
flapListPercentageThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flapListPercentageThreshold.setStatus("current")


class _FlapListTrapEnable_Type(Integer32):
    """Custom type flapListTrapEnable based on Integer32"""
    defaultValue = 1

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


_FlapListTrapEnable_Type.__name__ = "Integer32"
_FlapListTrapEnable_Object = MibTableColumn
flapListTrapEnable = _FlapListTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 4981, 6, 1, 1, 1, 1, 9),
    _FlapListTrapEnable_Type()
)
flapListTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flapListTrapEnable.setStatus("current")
_RdnFlapCmTable_Object = MibTable
rdnFlapCmTable = _RdnFlapCmTable_Object(
    (1, 3, 6, 1, 4, 1, 4981, 6, 1, 1, 2)
)
if mibBuilder.loadTexts:
    rdnFlapCmTable.setStatus("current")
_RdnFlapCmEntry_Object = MibTableRow
rdnFlapCmEntry = _RdnFlapCmEntry_Object(
    (1, 3, 6, 1, 4, 1, 4981, 6, 1, 1, 2, 1)
)
rdnFlapCmEntry.setIndexNames(
    (0, "RDN-CABLE-SPECTRUM-MIB", "flapCmIndex"),
)
if mibBuilder.loadTexts:
    rdnFlapCmEntry.setStatus("current")
_FlapCmIndex_Type = InterfaceIndex
_FlapCmIndex_Object = MibTableColumn
flapCmIndex = _FlapCmIndex_Object(
    (1, 3, 6, 1, 4, 1, 4981, 6, 1, 1, 2, 1, 1),
    _FlapCmIndex_Type()
)
flapCmIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    flapCmIndex.setStatus("current")


class _CmtsIfIndex_Type(Integer32):
    """Custom type cmtsIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_CmtsIfIndex_Type.__name__ = "Integer32"
_CmtsIfIndex_Object = MibTableColumn
cmtsIfIndex = _CmtsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4981, 6, 1, 1, 2, 1, 2),
    _CmtsIfIndex_Type()
)
cmtsIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmtsIfIndex.setStatus("current")
_FlapCmMacAddress_Type = MacAddress
_FlapCmMacAddress_Object = MibTableColumn
flapCmMacAddress = _FlapCmMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4981, 6, 1, 1, 2, 1, 3),
    _FlapCmMacAddress_Type()
)
flapCmMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flapCmMacAddress.setStatus("current")
_FlapCmUpstreamIfIndex_Type = InterfaceIndex
_FlapCmUpstreamIfIndex_Object = MibTableColumn
flapCmUpstreamIfIndex = _FlapCmUpstreamIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4981, 6, 1, 1, 2, 1, 4),
    _FlapCmUpstreamIfIndex_Type()
)
flapCmUpstreamIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flapCmUpstreamIfIndex.setStatus("current")
_FlapCmDownstreamIfIndex_Type = InterfaceIndex
_FlapCmDownstreamIfIndex_Object = MibTableColumn
flapCmDownstreamIfIndex = _FlapCmDownstreamIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4981, 6, 1, 1, 2, 1, 5),
    _FlapCmDownstreamIfIndex_Type()
)
flapCmDownstreamIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flapCmDownstreamIfIndex.setStatus("current")
_FlapCmInsertionFails_Type = Counter32
_FlapCmInsertionFails_Object = MibTableColumn
flapCmInsertionFails = _FlapCmInsertionFails_Object(
    (1, 3, 6, 1, 4, 1, 4981, 6, 1, 1, 2, 1, 6),
    _FlapCmInsertionFails_Type()
)
flapCmInsertionFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flapCmInsertionFails.setStatus("current")
_FlapCmHits_Type = Counter32
_FlapCmHits_Object = MibTableColumn
flapCmHits = _FlapCmHits_Object(
    (1, 3, 6, 1, 4, 1, 4981, 6, 1, 1, 2, 1, 7),
    _FlapCmHits_Type()
)
flapCmHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flapCmHits.setStatus("current")
_FlapCmMisses_Type = Counter32
_FlapCmMisses_Object = MibTableColumn
flapCmMisses = _FlapCmMisses_Object(
    (1, 3, 6, 1, 4, 1, 4981, 6, 1, 1, 2, 1, 8),
    _FlapCmMisses_Type()
)
flapCmMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flapCmMisses.setStatus("current")
_FlapCmPowerAdjustments_Type = Counter32
_FlapCmPowerAdjustments_Object = MibTableColumn
flapCmPowerAdjustments = _FlapCmPowerAdjustments_Object(
    (1, 3, 6, 1, 4, 1, 4981, 6, 1, 1, 2, 1, 9),
    _FlapCmPowerAdjustments_Type()
)
flapCmPowerAdjustments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flapCmPowerAdjustments.setStatus("current")
_CmFlapCounts_Type = Counter32
_CmFlapCounts_Object = MibTableColumn
cmFlapCounts = _CmFlapCounts_Object(
    (1, 3, 6, 1, 4, 1, 4981, 6, 1, 1, 2, 1, 10),
    _CmFlapCounts_Type()
)
cmFlapCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlapCounts.setStatus("current")
_CmLastFlapTime_Type = DateAndTime
_CmLastFlapTime_Object = MibTableColumn
cmLastFlapTime = _CmLastFlapTime_Object(
    (1, 3, 6, 1, 4, 1, 4981, 6, 1, 1, 2, 1, 11),
    _CmLastFlapTime_Type()
)
cmLastFlapTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmLastFlapTime.setStatus("current")
_CmFlapCreateTime_Type = DateAndTime
_CmFlapCreateTime_Object = MibTableColumn
cmFlapCreateTime = _CmFlapCreateTime_Object(
    (1, 3, 6, 1, 4, 1, 4981, 6, 1, 1, 2, 1, 12),
    _CmFlapCreateTime_Type()
)
cmFlapCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlapCreateTime.setStatus("current")
_CmFlapRowStatus_Type = RowStatus
_CmFlapRowStatus_Object = MibTableColumn
cmFlapRowStatus = _CmFlapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4981, 6, 1, 1, 2, 1, 13),
    _CmFlapRowStatus_Type()
)
cmFlapRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmFlapRowStatus.setStatus("current")


class _FlapTrapType_Type(Integer32):
    """Custom type flapTrapType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("insertion", 3),
          ("power", 1),
          ("ranging", 2))
    )


_FlapTrapType_Type.__name__ = "Integer32"
_FlapTrapType_Object = MibScalar
flapTrapType = _FlapTrapType_Object(
    (1, 3, 6, 1, 4, 1, 4981, 6, 1, 1, 4),
    _FlapTrapType_Type()
)
flapTrapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flapTrapType.setStatus("current")
_RdnCableSpectrumNotificationPrefix_ObjectIdentity = ObjectIdentity
rdnCableSpectrumNotificationPrefix = _RdnCableSpectrumNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4981, 6, 2)
)
_CableSpectrumMIBNotifications_ObjectIdentity = ObjectIdentity
cableSpectrumMIBNotifications = _CableSpectrumMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4981, 6, 2, 0)
)
_RdnCableSpectrumConformance_ObjectIdentity = ObjectIdentity
rdnCableSpectrumConformance = _RdnCableSpectrumConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4981, 6, 3)
)
_RdnCableSpectrumCompliances_ObjectIdentity = ObjectIdentity
rdnCableSpectrumCompliances = _RdnCableSpectrumCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4981, 6, 3, 1)
)
_RdnCableSpectrumGroups_ObjectIdentity = ObjectIdentity
rdnCableSpectrumGroups = _RdnCableSpectrumGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4981, 6, 3, 2)
)

# Managed Objects groups

rdnFlapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4981, 6, 3, 2, 1)
)
rdnFlapGroup.setObjects(
      *(("RDN-CABLE-SPECTRUM-MIB", "flapListMaxSize"),
        ("RDN-CABLE-SPECTRUM-MIB", "flapListCurrentSize"),
        ("RDN-CABLE-SPECTRUM-MIB", "flapAgingOutTime"),
        ("RDN-CABLE-SPECTRUM-MIB", "flapInsertionTime"),
        ("RDN-CABLE-SPECTRUM-MIB", "flapMissThreshold"),
        ("RDN-CABLE-SPECTRUM-MIB", "flapPowerAdjThreshold"),
        ("RDN-CABLE-SPECTRUM-MIB", "cmtsIfIndex"),
        ("RDN-CABLE-SPECTRUM-MIB", "flapCmMacAddress"),
        ("RDN-CABLE-SPECTRUM-MIB", "flapCmUpstreamIfIndex"),
        ("RDN-CABLE-SPECTRUM-MIB", "flapCmDownstreamIfIndex"),
        ("RDN-CABLE-SPECTRUM-MIB", "flapCmInsertionFails"),
        ("RDN-CABLE-SPECTRUM-MIB", "flapCmHits"),
        ("RDN-CABLE-SPECTRUM-MIB", "flapCmMisses"),
        ("RDN-CABLE-SPECTRUM-MIB", "flapCmPowerAdjustments"),
        ("RDN-CABLE-SPECTRUM-MIB", "cmFlapCounts"),
        ("RDN-CABLE-SPECTRUM-MIB", "cmLastFlapTime"),
        ("RDN-CABLE-SPECTRUM-MIB", "cmFlapCreateTime"),
        ("RDN-CABLE-SPECTRUM-MIB", "cmFlapRowStatus"),
        ("RDN-CABLE-SPECTRUM-MIB", "flapListPercentageThreshold"),
        ("RDN-CABLE-SPECTRUM-MIB", "flapListTrapEnable"))
)
if mibBuilder.loadTexts:
    rdnFlapGroup.setStatus("current")


# Notification objects

flapListTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4981, 6, 1, 1, 3)
)
flapListTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifAdminStatus"),
        ("IF-MIB", "ifOperStatus"))
)
if mibBuilder.loadTexts:
    flapListTrap.setStatus(
        "current"
    )

flapModemTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4981, 6, 1, 1, 5)
)
flapModemTrap.setObjects(
      *(("RDN-CABLE-SPECTRUM-MIB", "flapCmMacAddress"),
        ("RDN-CABLE-SPECTRUM-MIB", "flapTrapType"))
)
if mibBuilder.loadTexts:
    flapModemTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4981, 6, 3, 1, 1)
)
if mibBuilder.loadTexts:
    compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RDN-CABLE-SPECTRUM-MIB",
    **{"rdnCableSpectrum": rdnCableSpectrum,
       "rdnCableSpectrumObjects": rdnCableSpectrumObjects,
       "rdnFlapObjects": rdnFlapObjects,
       "rdnFlapCmCmtsStatusTable": rdnFlapCmCmtsStatusTable,
       "rdnFlapCmCmtsStatusEntry": rdnFlapCmCmtsStatusEntry,
       "flapCmCmtsIfIndex": flapCmCmtsIfIndex,
       "flapListMaxSize": flapListMaxSize,
       "flapListCurrentSize": flapListCurrentSize,
       "flapAgingOutTime": flapAgingOutTime,
       "flapInsertionTime": flapInsertionTime,
       "flapMissThreshold": flapMissThreshold,
       "flapPowerAdjThreshold": flapPowerAdjThreshold,
       "flapListPercentageThreshold": flapListPercentageThreshold,
       "flapListTrapEnable": flapListTrapEnable,
       "rdnFlapCmTable": rdnFlapCmTable,
       "rdnFlapCmEntry": rdnFlapCmEntry,
       "flapCmIndex": flapCmIndex,
       "cmtsIfIndex": cmtsIfIndex,
       "flapCmMacAddress": flapCmMacAddress,
       "flapCmUpstreamIfIndex": flapCmUpstreamIfIndex,
       "flapCmDownstreamIfIndex": flapCmDownstreamIfIndex,
       "flapCmInsertionFails": flapCmInsertionFails,
       "flapCmHits": flapCmHits,
       "flapCmMisses": flapCmMisses,
       "flapCmPowerAdjustments": flapCmPowerAdjustments,
       "cmFlapCounts": cmFlapCounts,
       "cmLastFlapTime": cmLastFlapTime,
       "cmFlapCreateTime": cmFlapCreateTime,
       "cmFlapRowStatus": cmFlapRowStatus,
       "flapListTrap": flapListTrap,
       "flapTrapType": flapTrapType,
       "flapModemTrap": flapModemTrap,
       "rdnCableSpectrumNotificationPrefix": rdnCableSpectrumNotificationPrefix,
       "cableSpectrumMIBNotifications": cableSpectrumMIBNotifications,
       "rdnCableSpectrumConformance": rdnCableSpectrumConformance,
       "rdnCableSpectrumCompliances": rdnCableSpectrumCompliances,
       "compliance": compliance,
       "rdnCableSpectrumGroups": rdnCableSpectrumGroups,
       "rdnFlapGroup": rdnFlapGroup}
)
