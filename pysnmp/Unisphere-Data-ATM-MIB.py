# SNMP MIB module (Unisphere-Data-ATM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Unisphere-Data-ATM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:10:18 2024
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

(atmfM4VcTestId,
 atmfM4VcTestObject,
 atmfM4VcTestResult,
 atmfM4VcTestType,
 atmfM4VpTestId,
 atmfM4VpTestObject,
 atmfM4VpTestResult,
 atmfM4VpTestType) = mibBuilder.importSymbols(
    "ATM-FORUM-SNMP-M4-MIB",
    "atmfM4VcTestId",
    "atmfM4VcTestObject",
    "atmfM4VcTestResult",
    "atmfM4VcTestType",
    "atmfM4VpTestId",
    "atmfM4VpTestObject",
    "atmfM4VpTestResult",
    "atmfM4VpTestType")

(atmVclVci,
 atmVclVpi,
 atmVplVpi) = mibBuilder.importSymbols(
    "ATM-MIB",
    "atmVclVci",
    "atmVclVpi",
    "atmVplVpi")

(AtmAddr,
 AtmVcIdentifier,
 AtmVorXAdminStatus,
 AtmVpIdentifier) = mibBuilder.importSymbols(
    "ATM-TC-MIB",
    "AtmAddr",
    "AtmVcIdentifier",
    "AtmVorXAdminStatus",
    "AtmVpIdentifier")

(InterfaceIndex,
 InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero",
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

(DisplayString,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")

(usDataMibs,) = mibBuilder.importSymbols(
    "Unisphere-Data-MIBs",
    "usDataMibs")

(UsdEnable,
 UsdNextIfIndex) = mibBuilder.importSymbols(
    "Unisphere-Data-TC",
    "UsdEnable",
    "UsdNextIfIndex")


# MODULE-IDENTITY

usdAtmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8)
)
usdAtmMIB.setRevisions(
        ("2002-08-09 13:40",
         "2002-01-24 14:00",
         "2001-12-14 18:04",
         "2001-11-26 16:39",
         "2000-11-27 19:51",
         "2000-08-02 00:00",
         "2000-05-12 00:00",
         "2000-01-13 00:00",
         "1999-08-04 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class UsdAtmNbmaMapName(OctetString, TextualConvention):
    status = "current"
    displayHint = "32a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )



class UsdAtmNbmaMapNameOrNull(OctetString, TextualConvention):
    status = "current"
    displayHint = "32a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )



# MIB Managed Objects in the order of their OIDs

_UsdAtmObjects_ObjectIdentity = ObjectIdentity
usdAtmObjects = _UsdAtmObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1)
)
_UsdAtmIfLayer_ObjectIdentity = ObjectIdentity
usdAtmIfLayer = _UsdAtmIfLayer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1)
)
_UsdAtmNextIfIndex_Type = UsdNextIfIndex
_UsdAtmNextIfIndex_Object = MibScalar
usdAtmNextIfIndex = _UsdAtmNextIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 1),
    _UsdAtmNextIfIndex_Type()
)
usdAtmNextIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdAtmNextIfIndex.setStatus("current")
_UsdAtmIfTable_Object = MibTable
usdAtmIfTable = _UsdAtmIfTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 2)
)
if mibBuilder.loadTexts:
    usdAtmIfTable.setStatus("current")
_UsdAtmIfEntry_Object = MibTableRow
usdAtmIfEntry = _UsdAtmIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 2, 1)
)
usdAtmIfEntry.setIndexNames(
    (0, "Unisphere-Data-ATM-MIB", "usdAtmIfIndex"),
)
if mibBuilder.loadTexts:
    usdAtmIfEntry.setStatus("current")
_UsdAtmIfIndex_Type = InterfaceIndex
_UsdAtmIfIndex_Object = MibTableColumn
usdAtmIfIndex = _UsdAtmIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 2, 1, 1),
    _UsdAtmIfIndex_Type()
)
usdAtmIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdAtmIfIndex.setStatus("current")
_UsdAtmIfRowStatus_Type = RowStatus
_UsdAtmIfRowStatus_Object = MibTableColumn
usdAtmIfRowStatus = _UsdAtmIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 2, 1, 2),
    _UsdAtmIfRowStatus_Type()
)
usdAtmIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdAtmIfRowStatus.setStatus("current")
_UsdAtmIfLowerIfIndex_Type = InterfaceIndexOrZero
_UsdAtmIfLowerIfIndex_Object = MibTableColumn
usdAtmIfLowerIfIndex = _UsdAtmIfLowerIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 2, 1, 3),
    _UsdAtmIfLowerIfIndex_Type()
)
usdAtmIfLowerIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdAtmIfLowerIfIndex.setStatus("current")


class _UsdAtmIfIlmiVpi_Type(AtmVpIdentifier):
    """Custom type usdAtmIfIlmiVpi based on AtmVpIdentifier"""
    defaultValue = 0


_UsdAtmIfIlmiVpi_Object = MibTableColumn
usdAtmIfIlmiVpi = _UsdAtmIfIlmiVpi_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 2, 1, 4),
    _UsdAtmIfIlmiVpi_Type()
)
usdAtmIfIlmiVpi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdAtmIfIlmiVpi.setStatus("current")


class _UsdAtmIfIlmiVci_Type(AtmVcIdentifier):
    """Custom type usdAtmIfIlmiVci based on AtmVcIdentifier"""
    defaultValue = 16


_UsdAtmIfIlmiVci_Object = MibTableColumn
usdAtmIfIlmiVci = _UsdAtmIfIlmiVci_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 2, 1, 5),
    _UsdAtmIfIlmiVci_Type()
)
usdAtmIfIlmiVci.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdAtmIfIlmiVci.setStatus("current")


class _UsdAtmIfIlmiVcd_Type(Integer32):
    """Custom type usdAtmIfIlmiVcd based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UsdAtmIfIlmiVcd_Type.__name__ = "Integer32"
_UsdAtmIfIlmiVcd_Object = MibTableColumn
usdAtmIfIlmiVcd = _UsdAtmIfIlmiVcd_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 2, 1, 6),
    _UsdAtmIfIlmiVcd_Type()
)
usdAtmIfIlmiVcd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdAtmIfIlmiVcd.setStatus("current")


class _UsdAtmIfIlmiPollFrequency_Type(Integer32):
    """Custom type usdAtmIfIlmiPollFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_UsdAtmIfIlmiPollFrequency_Type.__name__ = "Integer32"
_UsdAtmIfIlmiPollFrequency_Object = MibTableColumn
usdAtmIfIlmiPollFrequency = _UsdAtmIfIlmiPollFrequency_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 2, 1, 7),
    _UsdAtmIfIlmiPollFrequency_Type()
)
usdAtmIfIlmiPollFrequency.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdAtmIfIlmiPollFrequency.setStatus("current")
if mibBuilder.loadTexts:
    usdAtmIfIlmiPollFrequency.setUnits("seconds")


class _UsdAtmIfIlmiAdminState_Type(Integer32):
    """Custom type usdAtmIfIlmiAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_UsdAtmIfIlmiAdminState_Type.__name__ = "Integer32"
_UsdAtmIfIlmiAdminState_Object = MibTableColumn
usdAtmIfIlmiAdminState = _UsdAtmIfIlmiAdminState_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 2, 1, 8),
    _UsdAtmIfIlmiAdminState_Type()
)
usdAtmIfIlmiAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdAtmIfIlmiAdminState.setStatus("current")


class _UsdAtmIfUniVersion_Type(Integer32):
    """Custom type usdAtmIfUniVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("version3Dot0", 0),
          ("version3Dot1", 1),
          ("version4Dot0", 2))
    )


_UsdAtmIfUniVersion_Type.__name__ = "Integer32"
_UsdAtmIfUniVersion_Object = MibTableColumn
usdAtmIfUniVersion = _UsdAtmIfUniVersion_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 2, 1, 9),
    _UsdAtmIfUniVersion_Type()
)
usdAtmIfUniVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdAtmIfUniVersion.setStatus("current")


class _UsdAtmIfOamCellRxAdminState_Type(Integer32):
    """Custom type usdAtmIfOamCellRxAdminState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("oamCellAdminStateDisabled", 0),
          ("oamCellAdminStateEnabled", 1))
    )


_UsdAtmIfOamCellRxAdminState_Type.__name__ = "Integer32"
_UsdAtmIfOamCellRxAdminState_Object = MibTableColumn
usdAtmIfOamCellRxAdminState = _UsdAtmIfOamCellRxAdminState_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 2, 1, 10),
    _UsdAtmIfOamCellRxAdminState_Type()
)
usdAtmIfOamCellRxAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdAtmIfOamCellRxAdminState.setStatus("current")
_UsdAtmIfInCells_Type = Counter64
_UsdAtmIfInCells_Object = MibTableColumn
usdAtmIfInCells = _UsdAtmIfInCells_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 2, 1, 11),
    _UsdAtmIfInCells_Type()
)
usdAtmIfInCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdAtmIfInCells.setStatus("current")
_UsdAtmIfOutCells_Type = Counter64
_UsdAtmIfOutCells_Object = MibTableColumn
usdAtmIfOutCells = _UsdAtmIfOutCells_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 2, 1, 12),
    _UsdAtmIfOutCells_Type()
)
usdAtmIfOutCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdAtmIfOutCells.setStatus("current")


class _UsdAtmIfVcCount_Type(Integer32):
    """Custom type usdAtmIfVcCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 268431360),
    )


_UsdAtmIfVcCount_Type.__name__ = "Integer32"
_UsdAtmIfVcCount_Object = MibTableColumn
usdAtmIfVcCount = _UsdAtmIfVcCount_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 2, 1, 13),
    _UsdAtmIfVcCount_Type()
)
usdAtmIfVcCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdAtmIfVcCount.setStatus("current")
_UsdAtmIfMapGroup_Type = UsdAtmNbmaMapNameOrNull
_UsdAtmIfMapGroup_Object = MibTableColumn
usdAtmIfMapGroup = _UsdAtmIfMapGroup_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 2, 1, 14),
    _UsdAtmIfMapGroup_Type()
)
usdAtmIfMapGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdAtmIfMapGroup.setStatus("current")


class _UsdAtmIfCacAdminState_Type(UsdEnable):
    """Custom type usdAtmIfCacAdminState based on UsdEnable"""


_UsdAtmIfCacAdminState_Object = MibTableColumn
usdAtmIfCacAdminState = _UsdAtmIfCacAdminState_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 2, 1, 15),
    _UsdAtmIfCacAdminState_Type()
)
usdAtmIfCacAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdAtmIfCacAdminState.setStatus("current")


class _UsdAtmIfCacUbrWeight_Type(Integer32):
    """Custom type usdAtmIfCacUbrWeight based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UsdAtmIfCacUbrWeight_Type.__name__ = "Integer32"
_UsdAtmIfCacUbrWeight_Object = MibTableColumn
usdAtmIfCacUbrWeight = _UsdAtmIfCacUbrWeight_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 2, 1, 16),
    _UsdAtmIfCacUbrWeight_Type()
)
usdAtmIfCacUbrWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdAtmIfCacUbrWeight.setStatus("current")
if mibBuilder.loadTexts:
    usdAtmIfCacUbrWeight.setUnits("kbps")


class _UsdAtmIfCacSubscriptionBandwidth_Type(Integer32):
    """Custom type usdAtmIfCacSubscriptionBandwidth based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UsdAtmIfCacSubscriptionBandwidth_Type.__name__ = "Integer32"
_UsdAtmIfCacSubscriptionBandwidth_Object = MibTableColumn
usdAtmIfCacSubscriptionBandwidth = _UsdAtmIfCacSubscriptionBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 2, 1, 17),
    _UsdAtmIfCacSubscriptionBandwidth_Type()
)
usdAtmIfCacSubscriptionBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdAtmIfCacSubscriptionBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    usdAtmIfCacSubscriptionBandwidth.setUnits("kbps")


class _UsdAtmIfCacAvailableBandwidth_Type(Integer32):
    """Custom type usdAtmIfCacAvailableBandwidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UsdAtmIfCacAvailableBandwidth_Type.__name__ = "Integer32"
_UsdAtmIfCacAvailableBandwidth_Object = MibTableColumn
usdAtmIfCacAvailableBandwidth = _UsdAtmIfCacAvailableBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 2, 1, 18),
    _UsdAtmIfCacAvailableBandwidth_Type()
)
usdAtmIfCacAvailableBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdAtmIfCacAvailableBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    usdAtmIfCacAvailableBandwidth.setUnits("kbps")


class _UsdAtmIfOamCellFilter_Type(Integer32):
    """Custom type usdAtmIfOamCellFilter based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("oamCellFilterAlarm", 1),
          ("oamCellFilterAll", 0))
    )


_UsdAtmIfOamCellFilter_Type.__name__ = "Integer32"
_UsdAtmIfOamCellFilter_Object = MibTableColumn
usdAtmIfOamCellFilter = _UsdAtmIfOamCellFilter_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 2, 1, 23),
    _UsdAtmIfOamCellFilter_Type()
)
usdAtmIfOamCellFilter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdAtmIfOamCellFilter.setStatus("current")
_UsdAtmIfCacUsedBandwidthUpper_Type = Unsigned32
_UsdAtmIfCacUsedBandwidthUpper_Object = MibTableColumn
usdAtmIfCacUsedBandwidthUpper = _UsdAtmIfCacUsedBandwidthUpper_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 2, 1, 24),
    _UsdAtmIfCacUsedBandwidthUpper_Type()
)
usdAtmIfCacUsedBandwidthUpper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdAtmIfCacUsedBandwidthUpper.setStatus("current")
_UsdAtmIfCacUsedBandwidthLower_Type = Unsigned32
_UsdAtmIfCacUsedBandwidthLower_Object = MibTableColumn
usdAtmIfCacUsedBandwidthLower = _UsdAtmIfCacUsedBandwidthLower_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 2, 1, 25),
    _UsdAtmIfCacUsedBandwidthLower_Type()
)
usdAtmIfCacUsedBandwidthLower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdAtmIfCacUsedBandwidthLower.setStatus("current")
_UsdAtmPvcStatisticsTable_Object = MibTable
usdAtmPvcStatisticsTable = _UsdAtmPvcStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 3)
)
if mibBuilder.loadTexts:
    usdAtmPvcStatisticsTable.setStatus("current")
_UsdAtmPvcStatisticsEntry_Object = MibTableRow
usdAtmPvcStatisticsEntry = _UsdAtmPvcStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 3, 1)
)
usdAtmPvcStatisticsEntry.setIndexNames(
    (0, "Unisphere-Data-ATM-MIB", "usdAtmPvcStatsIfIndex"),
    (0, "Unisphere-Data-ATM-MIB", "usdAtmPvcStatsVpi"),
    (0, "Unisphere-Data-ATM-MIB", "usdAtmPvcStatsVci"),
)
if mibBuilder.loadTexts:
    usdAtmPvcStatisticsEntry.setStatus("current")
_UsdAtmPvcStatsIfIndex_Type = InterfaceIndex
_UsdAtmPvcStatsIfIndex_Object = MibTableColumn
usdAtmPvcStatsIfIndex = _UsdAtmPvcStatsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 3, 1, 1),
    _UsdAtmPvcStatsIfIndex_Type()
)
usdAtmPvcStatsIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdAtmPvcStatsIfIndex.setStatus("current")
_UsdAtmPvcStatsVpi_Type = AtmVpIdentifier
_UsdAtmPvcStatsVpi_Object = MibTableColumn
usdAtmPvcStatsVpi = _UsdAtmPvcStatsVpi_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 3, 1, 2),
    _UsdAtmPvcStatsVpi_Type()
)
usdAtmPvcStatsVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdAtmPvcStatsVpi.setStatus("current")
_UsdAtmPvcStatsVci_Type = AtmVcIdentifier
_UsdAtmPvcStatsVci_Object = MibTableColumn
usdAtmPvcStatsVci = _UsdAtmPvcStatsVci_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 3, 1, 3),
    _UsdAtmPvcStatsVci_Type()
)
usdAtmPvcStatsVci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdAtmPvcStatsVci.setStatus("current")
_UsdAtmPvcStatsInCells_Type = Counter64
_UsdAtmPvcStatsInCells_Object = MibTableColumn
usdAtmPvcStatsInCells = _UsdAtmPvcStatsInCells_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 3, 1, 4),
    _UsdAtmPvcStatsInCells_Type()
)
usdAtmPvcStatsInCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdAtmPvcStatsInCells.setStatus("current")
_UsdAtmPvcStatsInCellOctets_Type = Counter64
_UsdAtmPvcStatsInCellOctets_Object = MibTableColumn
usdAtmPvcStatsInCellOctets = _UsdAtmPvcStatsInCellOctets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 3, 1, 5),
    _UsdAtmPvcStatsInCellOctets_Type()
)
usdAtmPvcStatsInCellOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdAtmPvcStatsInCellOctets.setStatus("current")
_UsdAtmPvcStatsInPackets_Type = Counter64
_UsdAtmPvcStatsInPackets_Object = MibTableColumn
usdAtmPvcStatsInPackets = _UsdAtmPvcStatsInPackets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 3, 1, 6),
    _UsdAtmPvcStatsInPackets_Type()
)
usdAtmPvcStatsInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdAtmPvcStatsInPackets.setStatus("current")
_UsdAtmPvcStatsInPacketOctets_Type = Counter64
_UsdAtmPvcStatsInPacketOctets_Object = MibTableColumn
usdAtmPvcStatsInPacketOctets = _UsdAtmPvcStatsInPacketOctets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 3, 1, 7),
    _UsdAtmPvcStatsInPacketOctets_Type()
)
usdAtmPvcStatsInPacketOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdAtmPvcStatsInPacketOctets.setStatus("current")
_UsdAtmPvcStatsOutCells_Type = Counter64
_UsdAtmPvcStatsOutCells_Object = MibTableColumn
usdAtmPvcStatsOutCells = _UsdAtmPvcStatsOutCells_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 3, 1, 8),
    _UsdAtmPvcStatsOutCells_Type()
)
usdAtmPvcStatsOutCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdAtmPvcStatsOutCells.setStatus("current")
_UsdAtmPvcStatsOutCellOctets_Type = Counter64
_UsdAtmPvcStatsOutCellOctets_Object = MibTableColumn
usdAtmPvcStatsOutCellOctets = _UsdAtmPvcStatsOutCellOctets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 3, 1, 9),
    _UsdAtmPvcStatsOutCellOctets_Type()
)
usdAtmPvcStatsOutCellOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdAtmPvcStatsOutCellOctets.setStatus("current")
_UsdAtmPvcStatsOutPackets_Type = Counter64
_UsdAtmPvcStatsOutPackets_Object = MibTableColumn
usdAtmPvcStatsOutPackets = _UsdAtmPvcStatsOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 3, 1, 10),
    _UsdAtmPvcStatsOutPackets_Type()
)
usdAtmPvcStatsOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdAtmPvcStatsOutPackets.setStatus("current")
_UsdAtmPvcStatsOutPacketOctets_Type = Counter64
_UsdAtmPvcStatsOutPacketOctets_Object = MibTableColumn
usdAtmPvcStatsOutPacketOctets = _UsdAtmPvcStatsOutPacketOctets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 3, 1, 11),
    _UsdAtmPvcStatsOutPacketOctets_Type()
)
usdAtmPvcStatsOutPacketOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdAtmPvcStatsOutPacketOctets.setStatus("current")
_UsdAtmPvcStatsInCellErrors_Type = Counter32
_UsdAtmPvcStatsInCellErrors_Object = MibTableColumn
usdAtmPvcStatsInCellErrors = _UsdAtmPvcStatsInCellErrors_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 3, 1, 12),
    _UsdAtmPvcStatsInCellErrors_Type()
)
usdAtmPvcStatsInCellErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdAtmPvcStatsInCellErrors.setStatus("current")
_UsdAtmPvcStatsinPacketErrors_Type = Counter32
_UsdAtmPvcStatsinPacketErrors_Object = MibTableColumn
usdAtmPvcStatsinPacketErrors = _UsdAtmPvcStatsinPacketErrors_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 3, 1, 13),
    _UsdAtmPvcStatsinPacketErrors_Type()
)
usdAtmPvcStatsinPacketErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdAtmPvcStatsinPacketErrors.setStatus("current")
_UsdAtmPvcStatsOutCellErrors_Type = Counter32
_UsdAtmPvcStatsOutCellErrors_Object = MibTableColumn
usdAtmPvcStatsOutCellErrors = _UsdAtmPvcStatsOutCellErrors_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 3, 1, 14),
    _UsdAtmPvcStatsOutCellErrors_Type()
)
usdAtmPvcStatsOutCellErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdAtmPvcStatsOutCellErrors.setStatus("current")
_UsdAtmPvcStatsOutPacketErrors_Type = Counter32
_UsdAtmPvcStatsOutPacketErrors_Object = MibTableColumn
usdAtmPvcStatsOutPacketErrors = _UsdAtmPvcStatsOutPacketErrors_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 3, 1, 15),
    _UsdAtmPvcStatsOutPacketErrors_Type()
)
usdAtmPvcStatsOutPacketErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdAtmPvcStatsOutPacketErrors.setStatus("current")
_UsdAtmPvcStatsInPacketDiscards_Type = Counter32
_UsdAtmPvcStatsInPacketDiscards_Object = MibTableColumn
usdAtmPvcStatsInPacketDiscards = _UsdAtmPvcStatsInPacketDiscards_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 3, 1, 16),
    _UsdAtmPvcStatsInPacketDiscards_Type()
)
usdAtmPvcStatsInPacketDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdAtmPvcStatsInPacketDiscards.setStatus("current")
_UsdAtmPvcStatsInPacketOctetDiscards_Type = Counter32
_UsdAtmPvcStatsInPacketOctetDiscards_Object = MibTableColumn
usdAtmPvcStatsInPacketOctetDiscards = _UsdAtmPvcStatsInPacketOctetDiscards_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 3, 1, 17),
    _UsdAtmPvcStatsInPacketOctetDiscards_Type()
)
usdAtmPvcStatsInPacketOctetDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdAtmPvcStatsInPacketOctetDiscards.setStatus("current")
_UsdAtmPvcStatsInPacketUnknownProtocol_Type = Counter32
_UsdAtmPvcStatsInPacketUnknownProtocol_Object = MibTableColumn
usdAtmPvcStatsInPacketUnknownProtocol = _UsdAtmPvcStatsInPacketUnknownProtocol_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 3, 1, 18),
    _UsdAtmPvcStatsInPacketUnknownProtocol_Type()
)
usdAtmPvcStatsInPacketUnknownProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdAtmPvcStatsInPacketUnknownProtocol.setStatus("current")
_UsdAtmVpTunnelTable_Object = MibTable
usdAtmVpTunnelTable = _UsdAtmVpTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 4)
)
if mibBuilder.loadTexts:
    usdAtmVpTunnelTable.setStatus("current")
_UsdAtmVpTunnelEntry_Object = MibTableRow
usdAtmVpTunnelEntry = _UsdAtmVpTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 4, 1)
)
usdAtmVpTunnelEntry.setIndexNames(
    (0, "Unisphere-Data-ATM-MIB", "usdAtmVpTunnelIfIndex"),
    (0, "Unisphere-Data-ATM-MIB", "usdAtmVpTunnelVpi"),
)
if mibBuilder.loadTexts:
    usdAtmVpTunnelEntry.setStatus("current")
_UsdAtmVpTunnelIfIndex_Type = InterfaceIndex
_UsdAtmVpTunnelIfIndex_Object = MibTableColumn
usdAtmVpTunnelIfIndex = _UsdAtmVpTunnelIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 4, 1, 1),
    _UsdAtmVpTunnelIfIndex_Type()
)
usdAtmVpTunnelIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdAtmVpTunnelIfIndex.setStatus("current")
_UsdAtmVpTunnelVpi_Type = AtmVpIdentifier
_UsdAtmVpTunnelVpi_Object = MibTableColumn
usdAtmVpTunnelVpi = _UsdAtmVpTunnelVpi_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 4, 1, 2),
    _UsdAtmVpTunnelVpi_Type()
)
usdAtmVpTunnelVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdAtmVpTunnelVpi.setStatus("current")


class _UsdAtmVpTunnelKbps_Type(Integer32):
    """Custom type usdAtmVpTunnelKbps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UsdAtmVpTunnelKbps_Type.__name__ = "Integer32"
_UsdAtmVpTunnelKbps_Object = MibTableColumn
usdAtmVpTunnelKbps = _UsdAtmVpTunnelKbps_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 4, 1, 3),
    _UsdAtmVpTunnelKbps_Type()
)
usdAtmVpTunnelKbps.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdAtmVpTunnelKbps.setStatus("current")
if mibBuilder.loadTexts:
    usdAtmVpTunnelKbps.setUnits("kbps")
_UsdAtmVpTunnelRowStatus_Type = RowStatus
_UsdAtmVpTunnelRowStatus_Object = MibTableColumn
usdAtmVpTunnelRowStatus = _UsdAtmVpTunnelRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 4, 1, 4),
    _UsdAtmVpTunnelRowStatus_Type()
)
usdAtmVpTunnelRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdAtmVpTunnelRowStatus.setStatus("current")


class _UsdAtmVpTunnelServiceCategory_Type(Integer32):
    """Custom type usdAtmVpTunnelServiceCategory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cbr", 2),
          ("nrtVbr", 1))
    )


_UsdAtmVpTunnelServiceCategory_Type.__name__ = "Integer32"
_UsdAtmVpTunnelServiceCategory_Object = MibTableColumn
usdAtmVpTunnelServiceCategory = _UsdAtmVpTunnelServiceCategory_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 4, 1, 5),
    _UsdAtmVpTunnelServiceCategory_Type()
)
usdAtmVpTunnelServiceCategory.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdAtmVpTunnelServiceCategory.setStatus("current")
_UsdAtmIfCapabilityTable_Object = MibTable
usdAtmIfCapabilityTable = _UsdAtmIfCapabilityTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 5)
)
if mibBuilder.loadTexts:
    usdAtmIfCapabilityTable.setStatus("current")
_UsdAtmIfCapabilityEntry_Object = MibTableRow
usdAtmIfCapabilityEntry = _UsdAtmIfCapabilityEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 5, 1)
)
usdAtmIfCapabilityEntry.setIndexNames(
    (0, "Unisphere-Data-ATM-MIB", "usdAtmIfCapabilityIndex"),
)
if mibBuilder.loadTexts:
    usdAtmIfCapabilityEntry.setStatus("current")
_UsdAtmIfCapabilityIndex_Type = InterfaceIndex
_UsdAtmIfCapabilityIndex_Object = MibTableColumn
usdAtmIfCapabilityIndex = _UsdAtmIfCapabilityIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 5, 1, 1),
    _UsdAtmIfCapabilityIndex_Type()
)
usdAtmIfCapabilityIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdAtmIfCapabilityIndex.setStatus("current")
_UsdAtmIfCapabilityTrafficShaping_Type = TruthValue
_UsdAtmIfCapabilityTrafficShaping_Object = MibTableColumn
usdAtmIfCapabilityTrafficShaping = _UsdAtmIfCapabilityTrafficShaping_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 5, 1, 2),
    _UsdAtmIfCapabilityTrafficShaping_Type()
)
usdAtmIfCapabilityTrafficShaping.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdAtmIfCapabilityTrafficShaping.setStatus("current")
_UsdAtmIfCapabilityOam_Type = TruthValue
_UsdAtmIfCapabilityOam_Object = MibTableColumn
usdAtmIfCapabilityOam = _UsdAtmIfCapabilityOam_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 5, 1, 3),
    _UsdAtmIfCapabilityOam_Type()
)
usdAtmIfCapabilityOam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdAtmIfCapabilityOam.setStatus("current")


class _UsdAtmIfCapabilityDefaultVcPerVp_Type(Integer32):
    """Custom type usdAtmIfCapabilityDefaultVcPerVp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_UsdAtmIfCapabilityDefaultVcPerVp_Type.__name__ = "Integer32"
_UsdAtmIfCapabilityDefaultVcPerVp_Object = MibTableColumn
usdAtmIfCapabilityDefaultVcPerVp = _UsdAtmIfCapabilityDefaultVcPerVp_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 5, 1, 4),
    _UsdAtmIfCapabilityDefaultVcPerVp_Type()
)
usdAtmIfCapabilityDefaultVcPerVp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdAtmIfCapabilityDefaultVcPerVp.setStatus("current")


class _UsdAtmIfCapabilityNumVpiVciBits_Type(Integer32):
    """Custom type usdAtmIfCapabilityNumVpiVciBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 28),
    )


_UsdAtmIfCapabilityNumVpiVciBits_Type.__name__ = "Integer32"
_UsdAtmIfCapabilityNumVpiVciBits_Object = MibTableColumn
usdAtmIfCapabilityNumVpiVciBits = _UsdAtmIfCapabilityNumVpiVciBits_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 5, 1, 5),
    _UsdAtmIfCapabilityNumVpiVciBits_Type()
)
usdAtmIfCapabilityNumVpiVciBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdAtmIfCapabilityNumVpiVciBits.setStatus("current")


class _UsdAtmIfCapabilityMaxVcd_Type(Integer32):
    """Custom type usdAtmIfCapabilityMaxVcd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UsdAtmIfCapabilityMaxVcd_Type.__name__ = "Integer32"
_UsdAtmIfCapabilityMaxVcd_Object = MibTableColumn
usdAtmIfCapabilityMaxVcd = _UsdAtmIfCapabilityMaxVcd_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 5, 1, 6),
    _UsdAtmIfCapabilityMaxVcd_Type()
)
usdAtmIfCapabilityMaxVcd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdAtmIfCapabilityMaxVcd.setStatus("current")
_UsdAtmIfCapabilityMaxVpi_Type = AtmVpIdentifier
_UsdAtmIfCapabilityMaxVpi_Object = MibTableColumn
usdAtmIfCapabilityMaxVpi = _UsdAtmIfCapabilityMaxVpi_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 5, 1, 7),
    _UsdAtmIfCapabilityMaxVpi_Type()
)
usdAtmIfCapabilityMaxVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdAtmIfCapabilityMaxVpi.setStatus("current")
_UsdAtmIfCapabilityMaxVci_Type = AtmVcIdentifier
_UsdAtmIfCapabilityMaxVci_Object = MibTableColumn
usdAtmIfCapabilityMaxVci = _UsdAtmIfCapabilityMaxVci_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 5, 1, 8),
    _UsdAtmIfCapabilityMaxVci_Type()
)
usdAtmIfCapabilityMaxVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdAtmIfCapabilityMaxVci.setStatus("current")
_UsdAtmIfCapabilityOamCellFilter_Type = TruthValue
_UsdAtmIfCapabilityOamCellFilter_Object = MibTableColumn
usdAtmIfCapabilityOamCellFilter = _UsdAtmIfCapabilityOamCellFilter_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 5, 1, 9),
    _UsdAtmIfCapabilityOamCellFilter_Type()
)
usdAtmIfCapabilityOamCellFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdAtmIfCapabilityOamCellFilter.setStatus("current")
_UsdAtmIfSvcSignallingTable_Object = MibTable
usdAtmIfSvcSignallingTable = _UsdAtmIfSvcSignallingTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 6)
)
if mibBuilder.loadTexts:
    usdAtmIfSvcSignallingTable.setStatus("current")
_UsdAtmIfSvcSignallingEntry_Object = MibTableRow
usdAtmIfSvcSignallingEntry = _UsdAtmIfSvcSignallingEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 6, 1)
)
usdAtmIfSvcSignallingEntry.setIndexNames(
    (0, "Unisphere-Data-ATM-MIB", "usdAtmIfIndex"),
)
if mibBuilder.loadTexts:
    usdAtmIfSvcSignallingEntry.setStatus("current")
_UsdAtmIfSvcSignallingVpi_Type = AtmVpIdentifier
_UsdAtmIfSvcSignallingVpi_Object = MibTableColumn
usdAtmIfSvcSignallingVpi = _UsdAtmIfSvcSignallingVpi_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 6, 1, 1),
    _UsdAtmIfSvcSignallingVpi_Type()
)
usdAtmIfSvcSignallingVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdAtmIfSvcSignallingVpi.setStatus("current")
_UsdAtmIfSvcSignallingVci_Type = AtmVcIdentifier
_UsdAtmIfSvcSignallingVci_Object = MibTableColumn
usdAtmIfSvcSignallingVci = _UsdAtmIfSvcSignallingVci_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 6, 1, 2),
    _UsdAtmIfSvcSignallingVci_Type()
)
usdAtmIfSvcSignallingVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdAtmIfSvcSignallingVci.setStatus("current")
_UsdAtmIfSvcSignallingVcd_Type = AtmVcIdentifier
_UsdAtmIfSvcSignallingVcd_Object = MibTableColumn
usdAtmIfSvcSignallingVcd = _UsdAtmIfSvcSignallingVcd_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 6, 1, 3),
    _UsdAtmIfSvcSignallingVcd_Type()
)
usdAtmIfSvcSignallingVcd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdAtmIfSvcSignallingVcd.setStatus("current")
_UsdAtmIfSvcSignallingAdminStatus_Type = AtmVorXAdminStatus
_UsdAtmIfSvcSignallingAdminStatus_Object = MibTableColumn
usdAtmIfSvcSignallingAdminStatus = _UsdAtmIfSvcSignallingAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 6, 1, 4),
    _UsdAtmIfSvcSignallingAdminStatus_Type()
)
usdAtmIfSvcSignallingAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdAtmIfSvcSignallingAdminStatus.setStatus("current")
_UsdAtmAal5IfLayer_ObjectIdentity = ObjectIdentity
usdAtmAal5IfLayer = _UsdAtmAal5IfLayer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 2)
)
_UsdAtmAal5NextIfIndex_Type = UsdNextIfIndex
_UsdAtmAal5NextIfIndex_Object = MibScalar
usdAtmAal5NextIfIndex = _UsdAtmAal5NextIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 2, 1),
    _UsdAtmAal5NextIfIndex_Type()
)
usdAtmAal5NextIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdAtmAal5NextIfIndex.setStatus("current")
_UsdAtmAal5IfTable_Object = MibTable
usdAtmAal5IfTable = _UsdAtmAal5IfTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 2, 2)
)
if mibBuilder.loadTexts:
    usdAtmAal5IfTable.setStatus("current")
_UsdAtmAal5IfEntry_Object = MibTableRow
usdAtmAal5IfEntry = _UsdAtmAal5IfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 2, 2, 1)
)
usdAtmAal5IfEntry.setIndexNames(
    (0, "Unisphere-Data-ATM-MIB", "usdAtmAal5IfIndex"),
)
if mibBuilder.loadTexts:
    usdAtmAal5IfEntry.setStatus("current")
_UsdAtmAal5IfIndex_Type = InterfaceIndex
_UsdAtmAal5IfIndex_Object = MibTableColumn
usdAtmAal5IfIndex = _UsdAtmAal5IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 2, 2, 1, 1),
    _UsdAtmAal5IfIndex_Type()
)
usdAtmAal5IfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdAtmAal5IfIndex.setStatus("current")
_UsdAtmAal5IfRowStatus_Type = RowStatus
_UsdAtmAal5IfRowStatus_Object = MibTableColumn
usdAtmAal5IfRowStatus = _UsdAtmAal5IfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 2, 2, 1, 2),
    _UsdAtmAal5IfRowStatus_Type()
)
usdAtmAal5IfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdAtmAal5IfRowStatus.setStatus("current")
_UsdAtmAal5IfLowerIfIndex_Type = InterfaceIndexOrZero
_UsdAtmAal5IfLowerIfIndex_Object = MibTableColumn
usdAtmAal5IfLowerIfIndex = _UsdAtmAal5IfLowerIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 2, 2, 1, 3),
    _UsdAtmAal5IfLowerIfIndex_Type()
)
usdAtmAal5IfLowerIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdAtmAal5IfLowerIfIndex.setStatus("current")
_UsdAtmSubIfLayer_ObjectIdentity = ObjectIdentity
usdAtmSubIfLayer = _UsdAtmSubIfLayer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3)
)
_UsdAtmSubIfNextIfIndex_Type = UsdNextIfIndex
_UsdAtmSubIfNextIfIndex_Object = MibScalar
usdAtmSubIfNextIfIndex = _UsdAtmSubIfNextIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3, 1),
    _UsdAtmSubIfNextIfIndex_Type()
)
usdAtmSubIfNextIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdAtmSubIfNextIfIndex.setStatus("current")
_UsdAtmSubIfTable_Object = MibTable
usdAtmSubIfTable = _UsdAtmSubIfTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3, 2)
)
if mibBuilder.loadTexts:
    usdAtmSubIfTable.setStatus("current")
_UsdAtmSubIfEntry_Object = MibTableRow
usdAtmSubIfEntry = _UsdAtmSubIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3, 2, 1)
)
usdAtmSubIfEntry.setIndexNames(
    (0, "Unisphere-Data-ATM-MIB", "usdAtmSubIfIndex"),
)
if mibBuilder.loadTexts:
    usdAtmSubIfEntry.setStatus("current")
_UsdAtmSubIfIndex_Type = InterfaceIndex
_UsdAtmSubIfIndex_Object = MibTableColumn
usdAtmSubIfIndex = _UsdAtmSubIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3, 2, 1, 1),
    _UsdAtmSubIfIndex_Type()
)
usdAtmSubIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdAtmSubIfIndex.setStatus("current")
_UsdAtmSubIfRowStatus_Type = RowStatus
_UsdAtmSubIfRowStatus_Object = MibTableColumn
usdAtmSubIfRowStatus = _UsdAtmSubIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3, 2, 1, 2),
    _UsdAtmSubIfRowStatus_Type()
)
usdAtmSubIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdAtmSubIfRowStatus.setStatus("current")


class _UsdAtmSubIfDistinguisher_Type(Integer32):
    """Custom type usdAtmSubIfDistinguisher based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UsdAtmSubIfDistinguisher_Type.__name__ = "Integer32"
_UsdAtmSubIfDistinguisher_Object = MibTableColumn
usdAtmSubIfDistinguisher = _UsdAtmSubIfDistinguisher_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3, 2, 1, 3),
    _UsdAtmSubIfDistinguisher_Type()
)
usdAtmSubIfDistinguisher.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdAtmSubIfDistinguisher.setStatus("current")
_UsdAtmSubIfLowerIfIndex_Type = InterfaceIndexOrZero
_UsdAtmSubIfLowerIfIndex_Object = MibTableColumn
usdAtmSubIfLowerIfIndex = _UsdAtmSubIfLowerIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3, 2, 1, 4),
    _UsdAtmSubIfLowerIfIndex_Type()
)
usdAtmSubIfLowerIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdAtmSubIfLowerIfIndex.setStatus("current")


class _UsdAtmSubIfNbma_Type(TruthValue):
    """Custom type usdAtmSubIfNbma based on TruthValue"""


_UsdAtmSubIfNbma_Object = MibTableColumn
usdAtmSubIfNbma = _UsdAtmSubIfNbma_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3, 2, 1, 5),
    _UsdAtmSubIfNbma_Type()
)
usdAtmSubIfNbma.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdAtmSubIfNbma.setStatus("current")


class _UsdAtmSubIfAddress_Type(AtmAddr):
    """Custom type usdAtmSubIfAddress based on AtmAddr"""
    defaultHexValue = ""

    subtypeSpec = AtmAddr.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(7, 7),
        ValueSizeConstraint(20, 20),
    )


_UsdAtmSubIfAddress_Type.__name__ = "AtmAddr"
_UsdAtmSubIfAddress_Object = MibTableColumn
usdAtmSubIfAddress = _UsdAtmSubIfAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3, 2, 1, 6),
    _UsdAtmSubIfAddress_Type()
)
usdAtmSubIfAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdAtmSubIfAddress.setStatus("current")
_UsdAtmSubIfVccTable_Object = MibTable
usdAtmSubIfVccTable = _UsdAtmSubIfVccTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3, 3)
)
if mibBuilder.loadTexts:
    usdAtmSubIfVccTable.setStatus("current")
_UsdAtmSubIfVccEntry_Object = MibTableRow
usdAtmSubIfVccEntry = _UsdAtmSubIfVccEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3, 3, 1)
)
usdAtmSubIfVccEntry.setIndexNames(
    (0, "Unisphere-Data-ATM-MIB", "usdAtmSubIfIndex"),
    (0, "Unisphere-Data-ATM-MIB", "usdAtmSubIfVccVpi"),
    (0, "Unisphere-Data-ATM-MIB", "usdAtmSubIfVccVci"),
)
if mibBuilder.loadTexts:
    usdAtmSubIfVccEntry.setStatus("current")
_UsdAtmSubIfVccVpi_Type = AtmVpIdentifier
_UsdAtmSubIfVccVpi_Object = MibTableColumn
usdAtmSubIfVccVpi = _UsdAtmSubIfVccVpi_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3, 3, 1, 1),
    _UsdAtmSubIfVccVpi_Type()
)
usdAtmSubIfVccVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdAtmSubIfVccVpi.setStatus("current")
_UsdAtmSubIfVccVci_Type = AtmVcIdentifier
_UsdAtmSubIfVccVci_Object = MibTableColumn
usdAtmSubIfVccVci = _UsdAtmSubIfVccVci_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3, 3, 1, 2),
    _UsdAtmSubIfVccVci_Type()
)
usdAtmSubIfVccVci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdAtmSubIfVccVci.setStatus("current")
_UsdAtmSubIfVccRowStatus_Type = RowStatus
_UsdAtmSubIfVccRowStatus_Object = MibTableColumn
usdAtmSubIfVccRowStatus = _UsdAtmSubIfVccRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3, 3, 1, 3),
    _UsdAtmSubIfVccRowStatus_Type()
)
usdAtmSubIfVccRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdAtmSubIfVccRowStatus.setStatus("current")


class _UsdAtmSubIfVccVcd_Type(Integer32):
    """Custom type usdAtmSubIfVccVcd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UsdAtmSubIfVccVcd_Type.__name__ = "Integer32"
_UsdAtmSubIfVccVcd_Object = MibTableColumn
usdAtmSubIfVccVcd = _UsdAtmSubIfVccVcd_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3, 3, 1, 4),
    _UsdAtmSubIfVccVcd_Type()
)
usdAtmSubIfVccVcd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdAtmSubIfVccVcd.setStatus("current")


class _UsdAtmSubIfVccType_Type(Integer32):
    """Custom type usdAtmSubIfVccType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("autoconfig", 2),
          ("rfc1483Llc", 1),
          ("rfc1483VcMux", 0))
    )


_UsdAtmSubIfVccType_Type.__name__ = "Integer32"
_UsdAtmSubIfVccType_Object = MibTableColumn
usdAtmSubIfVccType = _UsdAtmSubIfVccType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3, 3, 1, 5),
    _UsdAtmSubIfVccType_Type()
)
usdAtmSubIfVccType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdAtmSubIfVccType.setStatus("current")


class _UsdAtmSubIfVccServiceCategory_Type(Integer32):
    """Custom type usdAtmSubIfVccServiceCategory based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("cbr", 3),
          ("nrtVbr", 2),
          ("rtVbr", 4),
          ("ubr", 0),
          ("ubrPcr", 1))
    )


_UsdAtmSubIfVccServiceCategory_Type.__name__ = "Integer32"
_UsdAtmSubIfVccServiceCategory_Object = MibTableColumn
usdAtmSubIfVccServiceCategory = _UsdAtmSubIfVccServiceCategory_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3, 3, 1, 6),
    _UsdAtmSubIfVccServiceCategory_Type()
)
usdAtmSubIfVccServiceCategory.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdAtmSubIfVccServiceCategory.setStatus("current")


class _UsdAtmSubIfVccPcr_Type(Integer32):
    """Custom type usdAtmSubIfVccPcr based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UsdAtmSubIfVccPcr_Type.__name__ = "Integer32"
_UsdAtmSubIfVccPcr_Object = MibTableColumn
usdAtmSubIfVccPcr = _UsdAtmSubIfVccPcr_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3, 3, 1, 7),
    _UsdAtmSubIfVccPcr_Type()
)
usdAtmSubIfVccPcr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdAtmSubIfVccPcr.setStatus("current")
if mibBuilder.loadTexts:
    usdAtmSubIfVccPcr.setUnits("kbps")


class _UsdAtmSubIfVccScr_Type(Integer32):
    """Custom type usdAtmSubIfVccScr based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UsdAtmSubIfVccScr_Type.__name__ = "Integer32"
_UsdAtmSubIfVccScr_Object = MibTableColumn
usdAtmSubIfVccScr = _UsdAtmSubIfVccScr_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3, 3, 1, 8),
    _UsdAtmSubIfVccScr_Type()
)
usdAtmSubIfVccScr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdAtmSubIfVccScr.setStatus("current")
if mibBuilder.loadTexts:
    usdAtmSubIfVccScr.setUnits("kbps")


class _UsdAtmSubIfVccMbs_Type(Integer32):
    """Custom type usdAtmSubIfVccMbs based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UsdAtmSubIfVccMbs_Type.__name__ = "Integer32"
_UsdAtmSubIfVccMbs_Object = MibTableColumn
usdAtmSubIfVccMbs = _UsdAtmSubIfVccMbs_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3, 3, 1, 9),
    _UsdAtmSubIfVccMbs_Type()
)
usdAtmSubIfVccMbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdAtmSubIfVccMbs.setStatus("current")
if mibBuilder.loadTexts:
    usdAtmSubIfVccMbs.setUnits("cells")
_UsdAtmSubIfInverseArp_Type = TruthValue
_UsdAtmSubIfInverseArp_Object = MibTableColumn
usdAtmSubIfInverseArp = _UsdAtmSubIfInverseArp_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3, 3, 1, 10),
    _UsdAtmSubIfInverseArp_Type()
)
usdAtmSubIfInverseArp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdAtmSubIfInverseArp.setStatus("current")


class _UsdAtmSubIfInverseArpRefresh_Type(Integer32):
    """Custom type usdAtmSubIfInverseArpRefresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UsdAtmSubIfInverseArpRefresh_Type.__name__ = "Integer32"
_UsdAtmSubIfInverseArpRefresh_Object = MibTableColumn
usdAtmSubIfInverseArpRefresh = _UsdAtmSubIfInverseArpRefresh_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3, 3, 1, 11),
    _UsdAtmSubIfInverseArpRefresh_Type()
)
usdAtmSubIfInverseArpRefresh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdAtmSubIfInverseArpRefresh.setStatus("current")
if mibBuilder.loadTexts:
    usdAtmSubIfInverseArpRefresh.setUnits("minutes")
_UsdAtmCircuitOamTable_Object = MibTable
usdAtmCircuitOamTable = _UsdAtmCircuitOamTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3, 4)
)
if mibBuilder.loadTexts:
    usdAtmCircuitOamTable.setStatus("current")
_UsdAtmCircuitOamEntry_Object = MibTableRow
usdAtmCircuitOamEntry = _UsdAtmCircuitOamEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3, 4, 1)
)
usdAtmCircuitOamEntry.setIndexNames(
    (0, "Unisphere-Data-ATM-MIB", "usdAtmCircuitOamIfIndex"),
    (0, "Unisphere-Data-ATM-MIB", "usdAtmCircuitOamVpi"),
    (0, "Unisphere-Data-ATM-MIB", "usdAtmCircuitOamVci"),
)
if mibBuilder.loadTexts:
    usdAtmCircuitOamEntry.setStatus("current")
_UsdAtmCircuitOamIfIndex_Type = InterfaceIndex
_UsdAtmCircuitOamIfIndex_Object = MibTableColumn
usdAtmCircuitOamIfIndex = _UsdAtmCircuitOamIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3, 4, 1, 1),
    _UsdAtmCircuitOamIfIndex_Type()
)
usdAtmCircuitOamIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdAtmCircuitOamIfIndex.setStatus("current")
_UsdAtmCircuitOamVpi_Type = AtmVpIdentifier
_UsdAtmCircuitOamVpi_Object = MibTableColumn
usdAtmCircuitOamVpi = _UsdAtmCircuitOamVpi_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3, 4, 1, 2),
    _UsdAtmCircuitOamVpi_Type()
)
usdAtmCircuitOamVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdAtmCircuitOamVpi.setStatus("current")
_UsdAtmCircuitOamVci_Type = AtmVcIdentifier
_UsdAtmCircuitOamVci_Object = MibTableColumn
usdAtmCircuitOamVci = _UsdAtmCircuitOamVci_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3, 4, 1, 3),
    _UsdAtmCircuitOamVci_Type()
)
usdAtmCircuitOamVci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdAtmCircuitOamVci.setStatus("current")


class _UsdAtmCircuitOamAdminStatus_Type(Integer32):
    """Custom type usdAtmCircuitOamAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("oamAdminStateDisabled", 1),
          ("oamAdminStateEnabled", 2))
    )


_UsdAtmCircuitOamAdminStatus_Type.__name__ = "Integer32"
_UsdAtmCircuitOamAdminStatus_Object = MibTableColumn
usdAtmCircuitOamAdminStatus = _UsdAtmCircuitOamAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3, 4, 1, 4),
    _UsdAtmCircuitOamAdminStatus_Type()
)
usdAtmCircuitOamAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdAtmCircuitOamAdminStatus.setStatus("current")


class _UsdAtmCircuitOamLoopbackOperStatus_Type(Integer32):
    """Custom type usdAtmCircuitOamLoopbackOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("oamOperStatusDisabled", 1),
          ("oamOperStatusFailed", 4),
          ("oamOperStatusNotSupported", 0),
          ("oamOperStatusReceived", 3),
          ("oamOperStatusSent", 2))
    )


_UsdAtmCircuitOamLoopbackOperStatus_Type.__name__ = "Integer32"
_UsdAtmCircuitOamLoopbackOperStatus_Object = MibTableColumn
usdAtmCircuitOamLoopbackOperStatus = _UsdAtmCircuitOamLoopbackOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3, 4, 1, 5),
    _UsdAtmCircuitOamLoopbackOperStatus_Type()
)
usdAtmCircuitOamLoopbackOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdAtmCircuitOamLoopbackOperStatus.setStatus("current")


class _UsdAtmCircuitVcOamOperStatus_Type(Integer32):
    """Custom type usdAtmCircuitVcOamOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("oamVcOperStateAisState", 0),
          ("oamVcOperStateDown", 5),
          ("oamVcOperStateDownRetry", 2),
          ("oamVcOperStateNotManaged", 6),
          ("oamVcOperStateRdiState", 1),
          ("oamVcOperStateUp", 4),
          ("oamVcOperStateUpRetry", 3))
    )


_UsdAtmCircuitVcOamOperStatus_Type.__name__ = "Integer32"
_UsdAtmCircuitVcOamOperStatus_Object = MibTableColumn
usdAtmCircuitVcOamOperStatus = _UsdAtmCircuitVcOamOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3, 4, 1, 6),
    _UsdAtmCircuitVcOamOperStatus_Type()
)
usdAtmCircuitVcOamOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdAtmCircuitVcOamOperStatus.setStatus("current")


class _UsdAtmCircuitOamLoopbackFrequency_Type(Integer32):
    """Custom type usdAtmCircuitOamLoopbackFrequency based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_UsdAtmCircuitOamLoopbackFrequency_Type.__name__ = "Integer32"
_UsdAtmCircuitOamLoopbackFrequency_Object = MibTableColumn
usdAtmCircuitOamLoopbackFrequency = _UsdAtmCircuitOamLoopbackFrequency_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3, 4, 1, 7),
    _UsdAtmCircuitOamLoopbackFrequency_Type()
)
usdAtmCircuitOamLoopbackFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdAtmCircuitOamLoopbackFrequency.setStatus("current")
if mibBuilder.loadTexts:
    usdAtmCircuitOamLoopbackFrequency.setUnits("seconds")
_UsdAtmCircuitInOamF5Cells_Type = Counter32
_UsdAtmCircuitInOamF5Cells_Object = MibTableColumn
usdAtmCircuitInOamF5Cells = _UsdAtmCircuitInOamF5Cells_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3, 4, 1, 8),
    _UsdAtmCircuitInOamF5Cells_Type()
)
usdAtmCircuitInOamF5Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdAtmCircuitInOamF5Cells.setStatus("current")
if mibBuilder.loadTexts:
    usdAtmCircuitInOamF5Cells.setUnits("cells")
_UsdAtmCircuitInOamCellsDropped_Type = Counter32
_UsdAtmCircuitInOamCellsDropped_Object = MibTableColumn
usdAtmCircuitInOamCellsDropped = _UsdAtmCircuitInOamCellsDropped_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3, 4, 1, 9),
    _UsdAtmCircuitInOamCellsDropped_Type()
)
usdAtmCircuitInOamCellsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdAtmCircuitInOamCellsDropped.setStatus("current")
if mibBuilder.loadTexts:
    usdAtmCircuitInOamCellsDropped.setUnits("cells")
_UsdAtmCircuitOutOamF5Cells_Type = Counter32
_UsdAtmCircuitOutOamF5Cells_Object = MibTableColumn
usdAtmCircuitOutOamF5Cells = _UsdAtmCircuitOutOamF5Cells_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3, 4, 1, 10),
    _UsdAtmCircuitOutOamF5Cells_Type()
)
usdAtmCircuitOutOamF5Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdAtmCircuitOutOamF5Cells.setStatus("current")
if mibBuilder.loadTexts:
    usdAtmCircuitOutOamF5Cells.setUnits("cells")
_UsdAtmCircuitInOamF5EndToEndLoopbackCells_Type = Counter32
_UsdAtmCircuitInOamF5EndToEndLoopbackCells_Object = MibTableColumn
usdAtmCircuitInOamF5EndToEndLoopbackCells = _UsdAtmCircuitInOamF5EndToEndLoopbackCells_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3, 4, 1, 11),
    _UsdAtmCircuitInOamF5EndToEndLoopbackCells_Type()
)
usdAtmCircuitInOamF5EndToEndLoopbackCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdAtmCircuitInOamF5EndToEndLoopbackCells.setStatus("current")
if mibBuilder.loadTexts:
    usdAtmCircuitInOamF5EndToEndLoopbackCells.setUnits("cells")
_UsdAtmCircuitInOamF5SegmentLoopbackCells_Type = Counter32
_UsdAtmCircuitInOamF5SegmentLoopbackCells_Object = MibTableColumn
usdAtmCircuitInOamF5SegmentLoopbackCells = _UsdAtmCircuitInOamF5SegmentLoopbackCells_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3, 4, 1, 12),
    _UsdAtmCircuitInOamF5SegmentLoopbackCells_Type()
)
usdAtmCircuitInOamF5SegmentLoopbackCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdAtmCircuitInOamF5SegmentLoopbackCells.setStatus("current")
if mibBuilder.loadTexts:
    usdAtmCircuitInOamF5SegmentLoopbackCells.setUnits("cells")
_UsdAtmCircuitInOamF5AisCells_Type = Counter32
_UsdAtmCircuitInOamF5AisCells_Object = MibTableColumn
usdAtmCircuitInOamF5AisCells = _UsdAtmCircuitInOamF5AisCells_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3, 4, 1, 13),
    _UsdAtmCircuitInOamF5AisCells_Type()
)
usdAtmCircuitInOamF5AisCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdAtmCircuitInOamF5AisCells.setStatus("current")
if mibBuilder.loadTexts:
    usdAtmCircuitInOamF5AisCells.setUnits("cells")
_UsdAtmCircuitInOamF5RdiCells_Type = Counter32
_UsdAtmCircuitInOamF5RdiCells_Object = MibTableColumn
usdAtmCircuitInOamF5RdiCells = _UsdAtmCircuitInOamF5RdiCells_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3, 4, 1, 14),
    _UsdAtmCircuitInOamF5RdiCells_Type()
)
usdAtmCircuitInOamF5RdiCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdAtmCircuitInOamF5RdiCells.setStatus("current")
if mibBuilder.loadTexts:
    usdAtmCircuitInOamF5RdiCells.setUnits("cells")
_UsdAtmCircuitOutOamF5EndToEndLoopbackCells_Type = Counter32
_UsdAtmCircuitOutOamF5EndToEndLoopbackCells_Object = MibTableColumn
usdAtmCircuitOutOamF5EndToEndLoopbackCells = _UsdAtmCircuitOutOamF5EndToEndLoopbackCells_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3, 4, 1, 15),
    _UsdAtmCircuitOutOamF5EndToEndLoopbackCells_Type()
)
usdAtmCircuitOutOamF5EndToEndLoopbackCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdAtmCircuitOutOamF5EndToEndLoopbackCells.setStatus("current")
if mibBuilder.loadTexts:
    usdAtmCircuitOutOamF5EndToEndLoopbackCells.setUnits("cells")
_UsdAtmCircuitOutOamF5SegmentLoopbackCells_Type = Counter32
_UsdAtmCircuitOutOamF5SegmentLoopbackCells_Object = MibTableColumn
usdAtmCircuitOutOamF5SegmentLoopbackCells = _UsdAtmCircuitOutOamF5SegmentLoopbackCells_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3, 4, 1, 16),
    _UsdAtmCircuitOutOamF5SegmentLoopbackCells_Type()
)
usdAtmCircuitOutOamF5SegmentLoopbackCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdAtmCircuitOutOamF5SegmentLoopbackCells.setStatus("current")
if mibBuilder.loadTexts:
    usdAtmCircuitOutOamF5SegmentLoopbackCells.setUnits("cells")
_UsdAtmCircuitOutOamF5RdiCells_Type = Counter32
_UsdAtmCircuitOutOamF5RdiCells_Object = MibTableColumn
usdAtmCircuitOutOamF5RdiCells = _UsdAtmCircuitOutOamF5RdiCells_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3, 4, 1, 17),
    _UsdAtmCircuitOutOamF5RdiCells_Type()
)
usdAtmCircuitOutOamF5RdiCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdAtmCircuitOutOamF5RdiCells.setStatus("current")
if mibBuilder.loadTexts:
    usdAtmCircuitOutOamF5RdiCells.setUnits("cells")
_UsdAtmSubIfVccTrafficShapingTable_Object = MibTable
usdAtmSubIfVccTrafficShapingTable = _UsdAtmSubIfVccTrafficShapingTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3, 5)
)
if mibBuilder.loadTexts:
    usdAtmSubIfVccTrafficShapingTable.setStatus("current")
_UsdAtmSubIfVccTrafficShapingEntry_Object = MibTableRow
usdAtmSubIfVccTrafficShapingEntry = _UsdAtmSubIfVccTrafficShapingEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3, 5, 1)
)
if mibBuilder.loadTexts:
    usdAtmSubIfVccTrafficShapingEntry.setStatus("current")
_UsdAtmSubIfVccTrafficShapingCdvt_Type = Unsigned32
_UsdAtmSubIfVccTrafficShapingCdvt_Object = MibTableColumn
usdAtmSubIfVccTrafficShapingCdvt = _UsdAtmSubIfVccTrafficShapingCdvt_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3, 5, 1, 1),
    _UsdAtmSubIfVccTrafficShapingCdvt_Type()
)
usdAtmSubIfVccTrafficShapingCdvt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdAtmSubIfVccTrafficShapingCdvt.setStatus("current")
if mibBuilder.loadTexts:
    usdAtmSubIfVccTrafficShapingCdvt.setUnits("tenths of a microsecond")
_UsdAtmSubIfVccTrafficShapingClp0_Type = TruthValue
_UsdAtmSubIfVccTrafficShapingClp0_Object = MibTableColumn
usdAtmSubIfVccTrafficShapingClp0 = _UsdAtmSubIfVccTrafficShapingClp0_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3, 5, 1, 2),
    _UsdAtmSubIfVccTrafficShapingClp0_Type()
)
usdAtmSubIfVccTrafficShapingClp0.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdAtmSubIfVccTrafficShapingClp0.setStatus("current")
_UsdAtmSubIfVccTrafficShapingTagging_Type = TruthValue
_UsdAtmSubIfVccTrafficShapingTagging_Object = MibTableColumn
usdAtmSubIfVccTrafficShapingTagging = _UsdAtmSubIfVccTrafficShapingTagging_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3, 5, 1, 3),
    _UsdAtmSubIfVccTrafficShapingTagging_Type()
)
usdAtmSubIfVccTrafficShapingTagging.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdAtmSubIfVccTrafficShapingTagging.setStatus("current")
_UsdAtmSubIfVccTrafficShapingPoliceObserve_Type = TruthValue
_UsdAtmSubIfVccTrafficShapingPoliceObserve_Object = MibTableColumn
usdAtmSubIfVccTrafficShapingPoliceObserve = _UsdAtmSubIfVccTrafficShapingPoliceObserve_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3, 5, 1, 4),
    _UsdAtmSubIfVccTrafficShapingPoliceObserve_Type()
)
usdAtmSubIfVccTrafficShapingPoliceObserve.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdAtmSubIfVccTrafficShapingPoliceObserve.setStatus("current")
_UsdAtmSubIfVccTrafficShapingPacketShaping_Type = TruthValue
_UsdAtmSubIfVccTrafficShapingPacketShaping_Object = MibTableColumn
usdAtmSubIfVccTrafficShapingPacketShaping = _UsdAtmSubIfVccTrafficShapingPacketShaping_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3, 5, 1, 5),
    _UsdAtmSubIfVccTrafficShapingPacketShaping_Type()
)
usdAtmSubIfVccTrafficShapingPacketShaping.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdAtmSubIfVccTrafficShapingPacketShaping.setStatus("current")
_UsdAtmSubIfSvcConfigTable_Object = MibTable
usdAtmSubIfSvcConfigTable = _UsdAtmSubIfSvcConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3, 6)
)
if mibBuilder.loadTexts:
    usdAtmSubIfSvcConfigTable.setStatus("current")
_UsdAtmSubIfSvcConfigEntry_Object = MibTableRow
usdAtmSubIfSvcConfigEntry = _UsdAtmSubIfSvcConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3, 6, 1)
)
usdAtmSubIfSvcConfigEntry.setIndexNames(
    (0, "Unisphere-Data-ATM-MIB", "usdAtmSubIfIndex"),
)
if mibBuilder.loadTexts:
    usdAtmSubIfSvcConfigEntry.setStatus("current")
_UsdAtmSubIfSvcRowStatus_Type = RowStatus
_UsdAtmSubIfSvcRowStatus_Object = MibTableColumn
usdAtmSubIfSvcRowStatus = _UsdAtmSubIfSvcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3, 6, 1, 1),
    _UsdAtmSubIfSvcRowStatus_Type()
)
usdAtmSubIfSvcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdAtmSubIfSvcRowStatus.setStatus("current")


class _UsdAtmSubIfSvcConfigDestAtmAddress_Type(AtmAddr):
    """Custom type usdAtmSubIfSvcConfigDestAtmAddress based on AtmAddr"""
    subtypeSpec = AtmAddr.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_UsdAtmSubIfSvcConfigDestAtmAddress_Type.__name__ = "AtmAddr"
_UsdAtmSubIfSvcConfigDestAtmAddress_Object = MibTableColumn
usdAtmSubIfSvcConfigDestAtmAddress = _UsdAtmSubIfSvcConfigDestAtmAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3, 6, 1, 2),
    _UsdAtmSubIfSvcConfigDestAtmAddress_Type()
)
usdAtmSubIfSvcConfigDestAtmAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdAtmSubIfSvcConfigDestAtmAddress.setStatus("current")


class _UsdAtmSubIfSvcConfigCircuitType_Type(Integer32):
    """Custom type usdAtmSubIfSvcConfigCircuitType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("rfc1483Llc", 1),
          ("rfc1483VcMux", 0))
    )


_UsdAtmSubIfSvcConfigCircuitType_Type.__name__ = "Integer32"
_UsdAtmSubIfSvcConfigCircuitType_Object = MibTableColumn
usdAtmSubIfSvcConfigCircuitType = _UsdAtmSubIfSvcConfigCircuitType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3, 6, 1, 3),
    _UsdAtmSubIfSvcConfigCircuitType_Type()
)
usdAtmSubIfSvcConfigCircuitType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdAtmSubIfSvcConfigCircuitType.setStatus("current")


class _UsdAtmSubIfSvcConfigServiceCategory_Type(Integer32):
    """Custom type usdAtmSubIfSvcConfigServiceCategory based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("cbr", 3),
          ("nrtVbr", 2),
          ("rtVbr", 4),
          ("ubr", 0),
          ("ubrPcr", 1))
    )


_UsdAtmSubIfSvcConfigServiceCategory_Type.__name__ = "Integer32"
_UsdAtmSubIfSvcConfigServiceCategory_Object = MibTableColumn
usdAtmSubIfSvcConfigServiceCategory = _UsdAtmSubIfSvcConfigServiceCategory_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3, 6, 1, 4),
    _UsdAtmSubIfSvcConfigServiceCategory_Type()
)
usdAtmSubIfSvcConfigServiceCategory.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdAtmSubIfSvcConfigServiceCategory.setStatus("current")


class _UsdAtmSubIfSvcConfigPcr_Type(Unsigned32):
    """Custom type usdAtmSubIfSvcConfigPcr based on Unsigned32"""
    defaultValue = 0


_UsdAtmSubIfSvcConfigPcr_Object = MibTableColumn
usdAtmSubIfSvcConfigPcr = _UsdAtmSubIfSvcConfigPcr_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3, 6, 1, 5),
    _UsdAtmSubIfSvcConfigPcr_Type()
)
usdAtmSubIfSvcConfigPcr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdAtmSubIfSvcConfigPcr.setStatus("current")
if mibBuilder.loadTexts:
    usdAtmSubIfSvcConfigPcr.setUnits("kbps")


class _UsdAtmSubIfSvcConfigScr_Type(Unsigned32):
    """Custom type usdAtmSubIfSvcConfigScr based on Unsigned32"""
    defaultValue = 0


_UsdAtmSubIfSvcConfigScr_Object = MibTableColumn
usdAtmSubIfSvcConfigScr = _UsdAtmSubIfSvcConfigScr_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3, 6, 1, 6),
    _UsdAtmSubIfSvcConfigScr_Type()
)
usdAtmSubIfSvcConfigScr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdAtmSubIfSvcConfigScr.setStatus("current")
if mibBuilder.loadTexts:
    usdAtmSubIfSvcConfigScr.setUnits("kbps")


class _UsdAtmSubIfSvcConfigMbs_Type(Unsigned32):
    """Custom type usdAtmSubIfSvcConfigMbs based on Unsigned32"""
    defaultValue = 0


_UsdAtmSubIfSvcConfigMbs_Object = MibTableColumn
usdAtmSubIfSvcConfigMbs = _UsdAtmSubIfSvcConfigMbs_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3, 6, 1, 7),
    _UsdAtmSubIfSvcConfigMbs_Type()
)
usdAtmSubIfSvcConfigMbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdAtmSubIfSvcConfigMbs.setStatus("current")
if mibBuilder.loadTexts:
    usdAtmSubIfSvcConfigMbs.setUnits("cells")
_UsdAtmSubIfSvcConfigCdvt_Type = Unsigned32
_UsdAtmSubIfSvcConfigCdvt_Object = MibTableColumn
usdAtmSubIfSvcConfigCdvt = _UsdAtmSubIfSvcConfigCdvt_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3, 6, 1, 8),
    _UsdAtmSubIfSvcConfigCdvt_Type()
)
usdAtmSubIfSvcConfigCdvt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdAtmSubIfSvcConfigCdvt.setStatus("current")
if mibBuilder.loadTexts:
    usdAtmSubIfSvcConfigCdvt.setUnits("100us")
_UsdAtmSubIfSvcConfigClp0_Type = TruthValue
_UsdAtmSubIfSvcConfigClp0_Object = MibTableColumn
usdAtmSubIfSvcConfigClp0 = _UsdAtmSubIfSvcConfigClp0_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3, 6, 1, 9),
    _UsdAtmSubIfSvcConfigClp0_Type()
)
usdAtmSubIfSvcConfigClp0.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdAtmSubIfSvcConfigClp0.setStatus("current")
_UsdAtmSubIfSvcConfigTagging_Type = TruthValue
_UsdAtmSubIfSvcConfigTagging_Object = MibTableColumn
usdAtmSubIfSvcConfigTagging = _UsdAtmSubIfSvcConfigTagging_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3, 6, 1, 10),
    _UsdAtmSubIfSvcConfigTagging_Type()
)
usdAtmSubIfSvcConfigTagging.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdAtmSubIfSvcConfigTagging.setStatus("current")
_UsdAtmSubIfSvcConfigObserve_Type = TruthValue
_UsdAtmSubIfSvcConfigObserve_Object = MibTableColumn
usdAtmSubIfSvcConfigObserve = _UsdAtmSubIfSvcConfigObserve_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3, 6, 1, 11),
    _UsdAtmSubIfSvcConfigObserve_Type()
)
usdAtmSubIfSvcConfigObserve.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdAtmSubIfSvcConfigObserve.setStatus("current")
_UsdAtmSubIfSvcConfigPacketDiscard_Type = TruthValue
_UsdAtmSubIfSvcConfigPacketDiscard_Object = MibTableColumn
usdAtmSubIfSvcConfigPacketDiscard = _UsdAtmSubIfSvcConfigPacketDiscard_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3, 6, 1, 12),
    _UsdAtmSubIfSvcConfigPacketDiscard_Type()
)
usdAtmSubIfSvcConfigPacketDiscard.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdAtmSubIfSvcConfigPacketDiscard.setStatus("current")
_UsdAtmNbma_ObjectIdentity = ObjectIdentity
usdAtmNbma = _UsdAtmNbma_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 4)
)
_UsdAtmNbmaMapTable_Object = MibTable
usdAtmNbmaMapTable = _UsdAtmNbmaMapTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 4, 1)
)
if mibBuilder.loadTexts:
    usdAtmNbmaMapTable.setStatus("current")
_UsdAtmNbmaMapEntry_Object = MibTableRow
usdAtmNbmaMapEntry = _UsdAtmNbmaMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 4, 1, 1)
)
usdAtmNbmaMapEntry.setIndexNames(
    (0, "Unisphere-Data-ATM-MIB", "usdAtmNbmaMapName"),
    (0, "Unisphere-Data-ATM-MIB", "usdAtmNbmaMapVcd"),
)
if mibBuilder.loadTexts:
    usdAtmNbmaMapEntry.setStatus("current")
_UsdAtmNbmaMapName_Type = UsdAtmNbmaMapName
_UsdAtmNbmaMapName_Object = MibTableColumn
usdAtmNbmaMapName = _UsdAtmNbmaMapName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 4, 1, 1, 1),
    _UsdAtmNbmaMapName_Type()
)
usdAtmNbmaMapName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdAtmNbmaMapName.setStatus("current")


class _UsdAtmNbmaMapVcd_Type(Integer32):
    """Custom type usdAtmNbmaMapVcd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UsdAtmNbmaMapVcd_Type.__name__ = "Integer32"
_UsdAtmNbmaMapVcd_Object = MibTableColumn
usdAtmNbmaMapVcd = _UsdAtmNbmaMapVcd_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 4, 1, 1, 2),
    _UsdAtmNbmaMapVcd_Type()
)
usdAtmNbmaMapVcd.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdAtmNbmaMapVcd.setStatus("current")
_UsdAtmNbmaMapIpAddress_Type = IpAddress
_UsdAtmNbmaMapIpAddress_Object = MibTableColumn
usdAtmNbmaMapIpAddress = _UsdAtmNbmaMapIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 4, 1, 1, 3),
    _UsdAtmNbmaMapIpAddress_Type()
)
usdAtmNbmaMapIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdAtmNbmaMapIpAddress.setStatus("current")
_UsdAtmNbmaMapVpi_Type = AtmVpIdentifier
_UsdAtmNbmaMapVpi_Object = MibTableColumn
usdAtmNbmaMapVpi = _UsdAtmNbmaMapVpi_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 4, 1, 1, 4),
    _UsdAtmNbmaMapVpi_Type()
)
usdAtmNbmaMapVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdAtmNbmaMapVpi.setStatus("current")
_UsdAtmNbmaMapVci_Type = AtmVcIdentifier
_UsdAtmNbmaMapVci_Object = MibTableColumn
usdAtmNbmaMapVci = _UsdAtmNbmaMapVci_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 4, 1, 1, 5),
    _UsdAtmNbmaMapVci_Type()
)
usdAtmNbmaMapVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdAtmNbmaMapVci.setStatus("current")
_UsdAtmNbmaMapIfIndex_Type = InterfaceIndexOrZero
_UsdAtmNbmaMapIfIndex_Object = MibTableColumn
usdAtmNbmaMapIfIndex = _UsdAtmNbmaMapIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 4, 1, 1, 6),
    _UsdAtmNbmaMapIfIndex_Type()
)
usdAtmNbmaMapIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdAtmNbmaMapIfIndex.setStatus("current")
_UsdAtmNbmaMapBroadcast_Type = TruthValue
_UsdAtmNbmaMapBroadcast_Object = MibTableColumn
usdAtmNbmaMapBroadcast = _UsdAtmNbmaMapBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 4, 1, 1, 7),
    _UsdAtmNbmaMapBroadcast_Type()
)
usdAtmNbmaMapBroadcast.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdAtmNbmaMapBroadcast.setStatus("current")
_UsdAtmNbmaMapRowStatus_Type = RowStatus
_UsdAtmNbmaMapRowStatus_Object = MibTableColumn
usdAtmNbmaMapRowStatus = _UsdAtmNbmaMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 4, 1, 1, 8),
    _UsdAtmNbmaMapRowStatus_Type()
)
usdAtmNbmaMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdAtmNbmaMapRowStatus.setStatus("current")
_UsdAtmNbmaMapListTable_Object = MibTable
usdAtmNbmaMapListTable = _UsdAtmNbmaMapListTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 4, 2)
)
if mibBuilder.loadTexts:
    usdAtmNbmaMapListTable.setStatus("current")
_UsdAtmNbmaMapListEntry_Object = MibTableRow
usdAtmNbmaMapListEntry = _UsdAtmNbmaMapListEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 4, 2, 1)
)
usdAtmNbmaMapListEntry.setIndexNames(
    (1, "Unisphere-Data-ATM-MIB", "usdAtmNbmaMapListName"),
)
if mibBuilder.loadTexts:
    usdAtmNbmaMapListEntry.setStatus("current")
_UsdAtmNbmaMapListName_Type = UsdAtmNbmaMapName
_UsdAtmNbmaMapListName_Object = MibTableColumn
usdAtmNbmaMapListName = _UsdAtmNbmaMapListName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 4, 2, 1, 1),
    _UsdAtmNbmaMapListName_Type()
)
usdAtmNbmaMapListName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdAtmNbmaMapListName.setStatus("current")
_UsdAtmNbmaMapListRowStatus_Type = RowStatus
_UsdAtmNbmaMapListRowStatus_Object = MibTableColumn
usdAtmNbmaMapListRowStatus = _UsdAtmNbmaMapListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 4, 2, 1, 2),
    _UsdAtmNbmaMapListRowStatus_Type()
)
usdAtmNbmaMapListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdAtmNbmaMapListRowStatus.setStatus("current")
_UsdAtmPing_ObjectIdentity = ObjectIdentity
usdAtmPing = _UsdAtmPing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 5)
)
_UsdAtmPingTestTypes_ObjectIdentity = ObjectIdentity
usdAtmPingTestTypes = _UsdAtmPingTestTypes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 5, 1)
)
_UsdAtmPingTestOamSeg_ObjectIdentity = ObjectIdentity
usdAtmPingTestOamSeg = _UsdAtmPingTestOamSeg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 5, 1, 1)
)
if mibBuilder.loadTexts:
    usdAtmPingTestOamSeg.setStatus("current")
_UsdAtmPingTestOamE2E_ObjectIdentity = ObjectIdentity
usdAtmPingTestOamE2E = _UsdAtmPingTestOamE2E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 5, 1, 2)
)
if mibBuilder.loadTexts:
    usdAtmPingTestOamE2E.setStatus("current")
_UsdAtmVpPingTable_Object = MibTable
usdAtmVpPingTable = _UsdAtmVpPingTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 5, 2)
)
if mibBuilder.loadTexts:
    usdAtmVpPingTable.setStatus("current")
_UsdAtmVpPingEntry_Object = MibTableRow
usdAtmVpPingEntry = _UsdAtmVpPingEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 5, 2, 1)
)
usdAtmVpPingEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ATM-MIB", "atmVplVpi"),
    (0, "ATM-FORUM-SNMP-M4-MIB", "atmfM4VpTestObject"),
)
if mibBuilder.loadTexts:
    usdAtmVpPingEntry.setStatus("current")


class _UsdAtmVpPingProbeCount_Type(Unsigned32):
    """Custom type usdAtmVpPingProbeCount based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_UsdAtmVpPingProbeCount_Type.__name__ = "Unsigned32"
_UsdAtmVpPingProbeCount_Object = MibTableColumn
usdAtmVpPingProbeCount = _UsdAtmVpPingProbeCount_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 5, 2, 1, 1),
    _UsdAtmVpPingProbeCount_Type()
)
usdAtmVpPingProbeCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdAtmVpPingProbeCount.setStatus("current")
if mibBuilder.loadTexts:
    usdAtmVpPingProbeCount.setUnits("probes")


class _UsdAtmVpPingTimeOut_Type(Unsigned32):
    """Custom type usdAtmVpPingTimeOut based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_UsdAtmVpPingTimeOut_Type.__name__ = "Unsigned32"
_UsdAtmVpPingTimeOut_Object = MibTableColumn
usdAtmVpPingTimeOut = _UsdAtmVpPingTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 5, 2, 1, 2),
    _UsdAtmVpPingTimeOut_Type()
)
usdAtmVpPingTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdAtmVpPingTimeOut.setStatus("current")
if mibBuilder.loadTexts:
    usdAtmVpPingTimeOut.setUnits("seconds")


class _UsdAtmVpPingCtlTrapGeneration_Type(Bits):
    """Custom type usdAtmVpPingCtlTrapGeneration based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        ("testCompletion", 0)
    )

_UsdAtmVpPingCtlTrapGeneration_Type.__name__ = "Bits"
_UsdAtmVpPingCtlTrapGeneration_Object = MibTableColumn
usdAtmVpPingCtlTrapGeneration = _UsdAtmVpPingCtlTrapGeneration_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 5, 2, 1, 3),
    _UsdAtmVpPingCtlTrapGeneration_Type()
)
usdAtmVpPingCtlTrapGeneration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdAtmVpPingCtlTrapGeneration.setStatus("current")


class _UsdAtmVpPingSentProbes_Type(Unsigned32):
    """Custom type usdAtmVpPingSentProbes based on Unsigned32"""
    defaultValue = 0


_UsdAtmVpPingSentProbes_Object = MibTableColumn
usdAtmVpPingSentProbes = _UsdAtmVpPingSentProbes_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 5, 2, 1, 4),
    _UsdAtmVpPingSentProbes_Type()
)
usdAtmVpPingSentProbes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdAtmVpPingSentProbes.setStatus("current")
if mibBuilder.loadTexts:
    usdAtmVpPingSentProbes.setUnits("probes")


class _UsdAtmVpPingProbeResponses_Type(Unsigned32):
    """Custom type usdAtmVpPingProbeResponses based on Unsigned32"""
    defaultValue = 0


_UsdAtmVpPingProbeResponses_Object = MibTableColumn
usdAtmVpPingProbeResponses = _UsdAtmVpPingProbeResponses_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 5, 2, 1, 5),
    _UsdAtmVpPingProbeResponses_Type()
)
usdAtmVpPingProbeResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdAtmVpPingProbeResponses.setStatus("current")
if mibBuilder.loadTexts:
    usdAtmVpPingProbeResponses.setUnits("probes")


class _UsdAtmVpPingStartTime_Type(TimeStamp):
    """Custom type usdAtmVpPingStartTime based on TimeStamp"""
    defaultValue = 0


_UsdAtmVpPingStartTime_Object = MibTableColumn
usdAtmVpPingStartTime = _UsdAtmVpPingStartTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 5, 2, 1, 6),
    _UsdAtmVpPingStartTime_Type()
)
usdAtmVpPingStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdAtmVpPingStartTime.setStatus("current")
_UsdAtmVpPingMinRtt_Type = Unsigned32
_UsdAtmVpPingMinRtt_Object = MibTableColumn
usdAtmVpPingMinRtt = _UsdAtmVpPingMinRtt_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 5, 2, 1, 7),
    _UsdAtmVpPingMinRtt_Type()
)
usdAtmVpPingMinRtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdAtmVpPingMinRtt.setStatus("current")
if mibBuilder.loadTexts:
    usdAtmVpPingMinRtt.setUnits("milliseconds")
_UsdAtmVpPingMaxRtt_Type = Unsigned32
_UsdAtmVpPingMaxRtt_Object = MibTableColumn
usdAtmVpPingMaxRtt = _UsdAtmVpPingMaxRtt_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 5, 2, 1, 8),
    _UsdAtmVpPingMaxRtt_Type()
)
usdAtmVpPingMaxRtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdAtmVpPingMaxRtt.setStatus("current")
if mibBuilder.loadTexts:
    usdAtmVpPingMaxRtt.setUnits("milliseconds")
_UsdAtmVpPingAverageRtt_Type = Unsigned32
_UsdAtmVpPingAverageRtt_Object = MibTableColumn
usdAtmVpPingAverageRtt = _UsdAtmVpPingAverageRtt_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 5, 2, 1, 9),
    _UsdAtmVpPingAverageRtt_Type()
)
usdAtmVpPingAverageRtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdAtmVpPingAverageRtt.setStatus("current")
if mibBuilder.loadTexts:
    usdAtmVpPingAverageRtt.setUnits("milliseconds")
_UsdAtmVcPingTable_Object = MibTable
usdAtmVcPingTable = _UsdAtmVcPingTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 5, 3)
)
if mibBuilder.loadTexts:
    usdAtmVcPingTable.setStatus("current")
_UsdAtmVcPingEntry_Object = MibTableRow
usdAtmVcPingEntry = _UsdAtmVcPingEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 5, 3, 1)
)
usdAtmVcPingEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ATM-MIB", "atmVclVpi"),
    (0, "ATM-MIB", "atmVclVci"),
    (0, "ATM-FORUM-SNMP-M4-MIB", "atmfM4VcTestObject"),
)
if mibBuilder.loadTexts:
    usdAtmVcPingEntry.setStatus("current")


class _UsdAtmVcPingProbeCount_Type(Unsigned32):
    """Custom type usdAtmVcPingProbeCount based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_UsdAtmVcPingProbeCount_Type.__name__ = "Unsigned32"
_UsdAtmVcPingProbeCount_Object = MibTableColumn
usdAtmVcPingProbeCount = _UsdAtmVcPingProbeCount_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 5, 3, 1, 1),
    _UsdAtmVcPingProbeCount_Type()
)
usdAtmVcPingProbeCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdAtmVcPingProbeCount.setStatus("current")
if mibBuilder.loadTexts:
    usdAtmVcPingProbeCount.setUnits("probes")


class _UsdAtmVcPingTimeOut_Type(Unsigned32):
    """Custom type usdAtmVcPingTimeOut based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_UsdAtmVcPingTimeOut_Type.__name__ = "Unsigned32"
_UsdAtmVcPingTimeOut_Object = MibTableColumn
usdAtmVcPingTimeOut = _UsdAtmVcPingTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 5, 3, 1, 2),
    _UsdAtmVcPingTimeOut_Type()
)
usdAtmVcPingTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdAtmVcPingTimeOut.setStatus("current")
if mibBuilder.loadTexts:
    usdAtmVcPingTimeOut.setUnits("seconds")


class _UsdAtmVcPingCtlTrapGeneration_Type(Bits):
    """Custom type usdAtmVcPingCtlTrapGeneration based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        ("testCompletion", 0)
    )

_UsdAtmVcPingCtlTrapGeneration_Type.__name__ = "Bits"
_UsdAtmVcPingCtlTrapGeneration_Object = MibTableColumn
usdAtmVcPingCtlTrapGeneration = _UsdAtmVcPingCtlTrapGeneration_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 5, 3, 1, 3),
    _UsdAtmVcPingCtlTrapGeneration_Type()
)
usdAtmVcPingCtlTrapGeneration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdAtmVcPingCtlTrapGeneration.setStatus("current")


class _UsdAtmVcPingSentProbes_Type(Unsigned32):
    """Custom type usdAtmVcPingSentProbes based on Unsigned32"""
    defaultValue = 0


_UsdAtmVcPingSentProbes_Object = MibTableColumn
usdAtmVcPingSentProbes = _UsdAtmVcPingSentProbes_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 5, 3, 1, 4),
    _UsdAtmVcPingSentProbes_Type()
)
usdAtmVcPingSentProbes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdAtmVcPingSentProbes.setStatus("current")
if mibBuilder.loadTexts:
    usdAtmVcPingSentProbes.setUnits("probes")


class _UsdAtmVcPingProbeResponses_Type(Unsigned32):
    """Custom type usdAtmVcPingProbeResponses based on Unsigned32"""
    defaultValue = 0


_UsdAtmVcPingProbeResponses_Object = MibTableColumn
usdAtmVcPingProbeResponses = _UsdAtmVcPingProbeResponses_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 5, 3, 1, 5),
    _UsdAtmVcPingProbeResponses_Type()
)
usdAtmVcPingProbeResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdAtmVcPingProbeResponses.setStatus("current")
if mibBuilder.loadTexts:
    usdAtmVcPingProbeResponses.setUnits("probes")


class _UsdAtmVcPingStartTime_Type(TimeStamp):
    """Custom type usdAtmVcPingStartTime based on TimeStamp"""
    defaultValue = 0


_UsdAtmVcPingStartTime_Object = MibTableColumn
usdAtmVcPingStartTime = _UsdAtmVcPingStartTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 5, 3, 1, 6),
    _UsdAtmVcPingStartTime_Type()
)
usdAtmVcPingStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdAtmVcPingStartTime.setStatus("current")
_UsdAtmVcPingMinRtt_Type = Unsigned32
_UsdAtmVcPingMinRtt_Object = MibTableColumn
usdAtmVcPingMinRtt = _UsdAtmVcPingMinRtt_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 5, 3, 1, 7),
    _UsdAtmVcPingMinRtt_Type()
)
usdAtmVcPingMinRtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdAtmVcPingMinRtt.setStatus("current")
if mibBuilder.loadTexts:
    usdAtmVcPingMinRtt.setUnits("milliseconds")
_UsdAtmVcPingMaxRtt_Type = Unsigned32
_UsdAtmVcPingMaxRtt_Object = MibTableColumn
usdAtmVcPingMaxRtt = _UsdAtmVcPingMaxRtt_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 5, 3, 1, 8),
    _UsdAtmVcPingMaxRtt_Type()
)
usdAtmVcPingMaxRtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdAtmVcPingMaxRtt.setStatus("current")
if mibBuilder.loadTexts:
    usdAtmVcPingMaxRtt.setUnits("milliseconds")
_UsdAtmVcPingAverageRtt_Type = Unsigned32
_UsdAtmVcPingAverageRtt_Object = MibTableColumn
usdAtmVcPingAverageRtt = _UsdAtmVcPingAverageRtt_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 5, 3, 1, 9),
    _UsdAtmVcPingAverageRtt_Type()
)
usdAtmVcPingAverageRtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdAtmVcPingAverageRtt.setStatus("current")
if mibBuilder.loadTexts:
    usdAtmVcPingAverageRtt.setUnits("milliseconds")
_UsdAtmTraps_ObjectIdentity = ObjectIdentity
usdAtmTraps = _UsdAtmTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 3)
)
_UsdAtmTrapPrefix_ObjectIdentity = ObjectIdentity
usdAtmTrapPrefix = _UsdAtmTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 3, 0)
)
_UsdAtmConformance_ObjectIdentity = ObjectIdentity
usdAtmConformance = _UsdAtmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 4)
)
_UsdAtmCompliances_ObjectIdentity = ObjectIdentity
usdAtmCompliances = _UsdAtmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 4, 1)
)
_UsdAtmGroups_ObjectIdentity = ObjectIdentity
usdAtmGroups = _UsdAtmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 4, 2)
)
usdAtmSubIfVccEntry.registerAugmentions(
    ("Unisphere-Data-ATM-MIB",
     "usdAtmSubIfVccTrafficShapingEntry")
)
usdAtmSubIfVccTrafficShapingEntry.setIndexNames(*usdAtmSubIfVccEntry.getIndexNames())

# Managed Objects groups

usdAtmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 4, 2, 1)
)
usdAtmGroup.setObjects(
      *(("Unisphere-Data-ATM-MIB", "usdAtmNextIfIndex"),
        ("Unisphere-Data-ATM-MIB", "usdAtmIfRowStatus"),
        ("Unisphere-Data-ATM-MIB", "usdAtmIfLowerIfIndex"),
        ("Unisphere-Data-ATM-MIB", "usdAtmIfIlmiVpi"),
        ("Unisphere-Data-ATM-MIB", "usdAtmIfIlmiVci"),
        ("Unisphere-Data-ATM-MIB", "usdAtmIfIlmiVcd"),
        ("Unisphere-Data-ATM-MIB", "usdAtmIfIlmiPollFrequency"),
        ("Unisphere-Data-ATM-MIB", "usdAtmIfIlmiAdminState"),
        ("Unisphere-Data-ATM-MIB", "usdAtmIfUniVersion"),
        ("Unisphere-Data-ATM-MIB", "usdAtmIfOamCellRxAdminState"),
        ("Unisphere-Data-ATM-MIB", "usdAtmIfInCells"),
        ("Unisphere-Data-ATM-MIB", "usdAtmIfOutCells"),
        ("Unisphere-Data-ATM-MIB", "usdAtmIfVcCount"),
        ("Unisphere-Data-ATM-MIB", "usdAtmPvcStatsInCells"),
        ("Unisphere-Data-ATM-MIB", "usdAtmPvcStatsInCellOctets"),
        ("Unisphere-Data-ATM-MIB", "usdAtmPvcStatsInPackets"),
        ("Unisphere-Data-ATM-MIB", "usdAtmPvcStatsInPacketOctets"),
        ("Unisphere-Data-ATM-MIB", "usdAtmPvcStatsOutCells"),
        ("Unisphere-Data-ATM-MIB", "usdAtmPvcStatsOutCellOctets"),
        ("Unisphere-Data-ATM-MIB", "usdAtmPvcStatsOutPackets"),
        ("Unisphere-Data-ATM-MIB", "usdAtmPvcStatsOutPacketOctets"),
        ("Unisphere-Data-ATM-MIB", "usdAtmPvcStatsInCellErrors"),
        ("Unisphere-Data-ATM-MIB", "usdAtmPvcStatsinPacketErrors"),
        ("Unisphere-Data-ATM-MIB", "usdAtmPvcStatsOutCellErrors"),
        ("Unisphere-Data-ATM-MIB", "usdAtmPvcStatsOutPacketErrors"),
        ("Unisphere-Data-ATM-MIB", "usdAtmPvcStatsInPacketDiscards"),
        ("Unisphere-Data-ATM-MIB", "usdAtmPvcStatsInPacketOctetDiscards"),
        ("Unisphere-Data-ATM-MIB", "usdAtmIfCapabilityTrafficShaping"),
        ("Unisphere-Data-ATM-MIB", "usdAtmIfCapabilityOam"),
        ("Unisphere-Data-ATM-MIB", "usdAtmIfCapabilityDefaultVcPerVp"),
        ("Unisphere-Data-ATM-MIB", "usdAtmIfCapabilityNumVpiVciBits"),
        ("Unisphere-Data-ATM-MIB", "usdAtmIfCapabilityMaxVcd"),
        ("Unisphere-Data-ATM-MIB", "usdAtmIfCapabilityMaxVpi"),
        ("Unisphere-Data-ATM-MIB", "usdAtmIfCapabilityMaxVci"))
)
if mibBuilder.loadTexts:
    usdAtmGroup.setStatus("obsolete")

usdAtmAal5Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 4, 2, 2)
)
usdAtmAal5Group.setObjects(
      *(("Unisphere-Data-ATM-MIB", "usdAtmAal5NextIfIndex"),
        ("Unisphere-Data-ATM-MIB", "usdAtmAal5IfRowStatus"),
        ("Unisphere-Data-ATM-MIB", "usdAtmAal5IfLowerIfIndex"))
)
if mibBuilder.loadTexts:
    usdAtmAal5Group.setStatus("current")

usdAtmSubIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 4, 2, 3)
)
usdAtmSubIfGroup.setObjects(
      *(("Unisphere-Data-ATM-MIB", "usdAtmSubIfNextIfIndex"),
        ("Unisphere-Data-ATM-MIB", "usdAtmSubIfRowStatus"),
        ("Unisphere-Data-ATM-MIB", "usdAtmSubIfDistinguisher"),
        ("Unisphere-Data-ATM-MIB", "usdAtmSubIfLowerIfIndex"),
        ("Unisphere-Data-ATM-MIB", "usdAtmSubIfVccRowStatus"),
        ("Unisphere-Data-ATM-MIB", "usdAtmSubIfVccVcd"),
        ("Unisphere-Data-ATM-MIB", "usdAtmSubIfVccType"),
        ("Unisphere-Data-ATM-MIB", "usdAtmSubIfVccServiceCategory"),
        ("Unisphere-Data-ATM-MIB", "usdAtmSubIfVccPcr"),
        ("Unisphere-Data-ATM-MIB", "usdAtmSubIfVccScr"),
        ("Unisphere-Data-ATM-MIB", "usdAtmSubIfVccMbs"),
        ("Unisphere-Data-ATM-MIB", "usdAtmCircuitOamAdminStatus"),
        ("Unisphere-Data-ATM-MIB", "usdAtmCircuitOamLoopbackOperStatus"),
        ("Unisphere-Data-ATM-MIB", "usdAtmCircuitVcOamOperStatus"),
        ("Unisphere-Data-ATM-MIB", "usdAtmCircuitOamLoopbackFrequency"),
        ("Unisphere-Data-ATM-MIB", "usdAtmCircuitInOamF5Cells"),
        ("Unisphere-Data-ATM-MIB", "usdAtmCircuitInOamCellsDropped"),
        ("Unisphere-Data-ATM-MIB", "usdAtmCircuitOutOamF5Cells"),
        ("Unisphere-Data-ATM-MIB", "usdAtmCircuitInOamF5EndToEndLoopbackCells"),
        ("Unisphere-Data-ATM-MIB", "usdAtmCircuitInOamF5SegmentLoopbackCells"),
        ("Unisphere-Data-ATM-MIB", "usdAtmCircuitInOamF5AisCells"),
        ("Unisphere-Data-ATM-MIB", "usdAtmCircuitInOamF5RdiCells"),
        ("Unisphere-Data-ATM-MIB", "usdAtmCircuitOutOamF5EndToEndLoopbackCells"),
        ("Unisphere-Data-ATM-MIB", "usdAtmCircuitOutOamF5SegmentLoopbackCells"),
        ("Unisphere-Data-ATM-MIB", "usdAtmCircuitOutOamF5RdiCells"))
)
if mibBuilder.loadTexts:
    usdAtmSubIfGroup.setStatus("obsolete")

usdAtmVpTunnelGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 4, 2, 4)
)
usdAtmVpTunnelGroup.setObjects(
      *(("Unisphere-Data-ATM-MIB", "usdAtmVpTunnelKbps"),
        ("Unisphere-Data-ATM-MIB", "usdAtmVpTunnelRowStatus"),
        ("Unisphere-Data-ATM-MIB", "usdAtmVpTunnelServiceCategory"))
)
if mibBuilder.loadTexts:
    usdAtmVpTunnelGroup.setStatus("current")

usdAtmNbmaMapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 4, 2, 5)
)
usdAtmNbmaMapGroup.setObjects(
      *(("Unisphere-Data-ATM-MIB", "usdAtmNbmaMapIpAddress"),
        ("Unisphere-Data-ATM-MIB", "usdAtmNbmaMapVpi"),
        ("Unisphere-Data-ATM-MIB", "usdAtmNbmaMapVci"),
        ("Unisphere-Data-ATM-MIB", "usdAtmNbmaMapIfIndex"),
        ("Unisphere-Data-ATM-MIB", "usdAtmNbmaMapBroadcast"),
        ("Unisphere-Data-ATM-MIB", "usdAtmNbmaMapRowStatus"),
        ("Unisphere-Data-ATM-MIB", "usdAtmNbmaMapListRowStatus"))
)
if mibBuilder.loadTexts:
    usdAtmNbmaMapGroup.setStatus("current")

usdAtmSubIfGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 4, 2, 6)
)
usdAtmSubIfGroup2.setObjects(
      *(("Unisphere-Data-ATM-MIB", "usdAtmSubIfNextIfIndex"),
        ("Unisphere-Data-ATM-MIB", "usdAtmSubIfRowStatus"),
        ("Unisphere-Data-ATM-MIB", "usdAtmSubIfDistinguisher"),
        ("Unisphere-Data-ATM-MIB", "usdAtmSubIfLowerIfIndex"),
        ("Unisphere-Data-ATM-MIB", "usdAtmSubIfNbma"),
        ("Unisphere-Data-ATM-MIB", "usdAtmSubIfVccRowStatus"),
        ("Unisphere-Data-ATM-MIB", "usdAtmSubIfVccVcd"),
        ("Unisphere-Data-ATM-MIB", "usdAtmSubIfVccType"),
        ("Unisphere-Data-ATM-MIB", "usdAtmSubIfVccServiceCategory"),
        ("Unisphere-Data-ATM-MIB", "usdAtmSubIfVccPcr"),
        ("Unisphere-Data-ATM-MIB", "usdAtmSubIfVccScr"),
        ("Unisphere-Data-ATM-MIB", "usdAtmSubIfVccMbs"),
        ("Unisphere-Data-ATM-MIB", "usdAtmSubIfInverseArp"),
        ("Unisphere-Data-ATM-MIB", "usdAtmSubIfInverseArpRefresh"),
        ("Unisphere-Data-ATM-MIB", "usdAtmCircuitOamAdminStatus"),
        ("Unisphere-Data-ATM-MIB", "usdAtmCircuitOamLoopbackOperStatus"),
        ("Unisphere-Data-ATM-MIB", "usdAtmCircuitVcOamOperStatus"),
        ("Unisphere-Data-ATM-MIB", "usdAtmCircuitOamLoopbackFrequency"),
        ("Unisphere-Data-ATM-MIB", "usdAtmCircuitInOamF5Cells"),
        ("Unisphere-Data-ATM-MIB", "usdAtmCircuitInOamCellsDropped"),
        ("Unisphere-Data-ATM-MIB", "usdAtmCircuitOutOamF5Cells"),
        ("Unisphere-Data-ATM-MIB", "usdAtmCircuitInOamF5EndToEndLoopbackCells"),
        ("Unisphere-Data-ATM-MIB", "usdAtmCircuitInOamF5SegmentLoopbackCells"),
        ("Unisphere-Data-ATM-MIB", "usdAtmCircuitInOamF5AisCells"),
        ("Unisphere-Data-ATM-MIB", "usdAtmCircuitInOamF5RdiCells"),
        ("Unisphere-Data-ATM-MIB", "usdAtmCircuitOutOamF5EndToEndLoopbackCells"),
        ("Unisphere-Data-ATM-MIB", "usdAtmCircuitOutOamF5SegmentLoopbackCells"),
        ("Unisphere-Data-ATM-MIB", "usdAtmCircuitOutOamF5RdiCells"))
)
if mibBuilder.loadTexts:
    usdAtmSubIfGroup2.setStatus("obsolete")

usdAtmVpPingControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 4, 2, 7)
)
usdAtmVpPingControlGroup.setObjects(
      *(("Unisphere-Data-ATM-MIB", "usdAtmVpPingProbeCount"),
        ("Unisphere-Data-ATM-MIB", "usdAtmVpPingTimeOut"),
        ("Unisphere-Data-ATM-MIB", "usdAtmVpPingCtlTrapGeneration"),
        ("Unisphere-Data-ATM-MIB", "usdAtmVpPingSentProbes"),
        ("Unisphere-Data-ATM-MIB", "usdAtmVpPingProbeResponses"),
        ("Unisphere-Data-ATM-MIB", "usdAtmVpPingStartTime"),
        ("Unisphere-Data-ATM-MIB", "usdAtmVpPingMinRtt"),
        ("Unisphere-Data-ATM-MIB", "usdAtmVpPingMaxRtt"),
        ("Unisphere-Data-ATM-MIB", "usdAtmVpPingAverageRtt"))
)
if mibBuilder.loadTexts:
    usdAtmVpPingControlGroup.setStatus("current")

usdAtmVcPingControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 4, 2, 8)
)
usdAtmVcPingControlGroup.setObjects(
      *(("Unisphere-Data-ATM-MIB", "usdAtmVcPingProbeCount"),
        ("Unisphere-Data-ATM-MIB", "usdAtmVcPingTimeOut"),
        ("Unisphere-Data-ATM-MIB", "usdAtmVcPingCtlTrapGeneration"),
        ("Unisphere-Data-ATM-MIB", "usdAtmVcPingSentProbes"),
        ("Unisphere-Data-ATM-MIB", "usdAtmVcPingProbeResponses"),
        ("Unisphere-Data-ATM-MIB", "usdAtmVcPingStartTime"),
        ("Unisphere-Data-ATM-MIB", "usdAtmVcPingMinRtt"),
        ("Unisphere-Data-ATM-MIB", "usdAtmVcPingMaxRtt"),
        ("Unisphere-Data-ATM-MIB", "usdAtmVcPingAverageRtt"))
)
if mibBuilder.loadTexts:
    usdAtmVcPingControlGroup.setStatus("current")

usdAtmGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 4, 2, 10)
)
usdAtmGroup2.setObjects(
      *(("Unisphere-Data-ATM-MIB", "usdAtmNextIfIndex"),
        ("Unisphere-Data-ATM-MIB", "usdAtmIfRowStatus"),
        ("Unisphere-Data-ATM-MIB", "usdAtmIfLowerIfIndex"),
        ("Unisphere-Data-ATM-MIB", "usdAtmIfIlmiVpi"),
        ("Unisphere-Data-ATM-MIB", "usdAtmIfIlmiVci"),
        ("Unisphere-Data-ATM-MIB", "usdAtmIfIlmiVcd"),
        ("Unisphere-Data-ATM-MIB", "usdAtmIfIlmiPollFrequency"),
        ("Unisphere-Data-ATM-MIB", "usdAtmIfIlmiAdminState"),
        ("Unisphere-Data-ATM-MIB", "usdAtmIfUniVersion"),
        ("Unisphere-Data-ATM-MIB", "usdAtmIfOamCellRxAdminState"),
        ("Unisphere-Data-ATM-MIB", "usdAtmIfInCells"),
        ("Unisphere-Data-ATM-MIB", "usdAtmIfOutCells"),
        ("Unisphere-Data-ATM-MIB", "usdAtmIfVcCount"),
        ("Unisphere-Data-ATM-MIB", "usdAtmIfMapGroup"),
        ("Unisphere-Data-ATM-MIB", "usdAtmIfOamCellFilter"),
        ("Unisphere-Data-ATM-MIB", "usdAtmPvcStatsInCells"),
        ("Unisphere-Data-ATM-MIB", "usdAtmPvcStatsInCellOctets"),
        ("Unisphere-Data-ATM-MIB", "usdAtmPvcStatsInPackets"),
        ("Unisphere-Data-ATM-MIB", "usdAtmPvcStatsInPacketOctets"),
        ("Unisphere-Data-ATM-MIB", "usdAtmPvcStatsOutCells"),
        ("Unisphere-Data-ATM-MIB", "usdAtmPvcStatsOutCellOctets"),
        ("Unisphere-Data-ATM-MIB", "usdAtmPvcStatsOutPackets"),
        ("Unisphere-Data-ATM-MIB", "usdAtmPvcStatsOutPacketOctets"),
        ("Unisphere-Data-ATM-MIB", "usdAtmPvcStatsInCellErrors"),
        ("Unisphere-Data-ATM-MIB", "usdAtmPvcStatsinPacketErrors"),
        ("Unisphere-Data-ATM-MIB", "usdAtmPvcStatsOutCellErrors"),
        ("Unisphere-Data-ATM-MIB", "usdAtmPvcStatsOutPacketErrors"),
        ("Unisphere-Data-ATM-MIB", "usdAtmPvcStatsInPacketDiscards"),
        ("Unisphere-Data-ATM-MIB", "usdAtmPvcStatsInPacketOctetDiscards"),
        ("Unisphere-Data-ATM-MIB", "usdAtmPvcStatsInPacketUnknownProtocol"),
        ("Unisphere-Data-ATM-MIB", "usdAtmIfCapabilityTrafficShaping"),
        ("Unisphere-Data-ATM-MIB", "usdAtmIfCapabilityOam"),
        ("Unisphere-Data-ATM-MIB", "usdAtmIfCapabilityDefaultVcPerVp"),
        ("Unisphere-Data-ATM-MIB", "usdAtmIfCapabilityNumVpiVciBits"),
        ("Unisphere-Data-ATM-MIB", "usdAtmIfCapabilityMaxVcd"),
        ("Unisphere-Data-ATM-MIB", "usdAtmIfCapabilityMaxVpi"),
        ("Unisphere-Data-ATM-MIB", "usdAtmIfCapabilityMaxVci"),
        ("Unisphere-Data-ATM-MIB", "usdAtmIfCapabilityOamCellFilter"))
)
if mibBuilder.loadTexts:
    usdAtmGroup2.setStatus("obsolete")

usdAtmTrafficShapingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 4, 2, 11)
)
usdAtmTrafficShapingGroup.setObjects(
      *(("Unisphere-Data-ATM-MIB", "usdAtmSubIfVccTrafficShapingCdvt"),
        ("Unisphere-Data-ATM-MIB", "usdAtmSubIfVccTrafficShapingClp0"),
        ("Unisphere-Data-ATM-MIB", "usdAtmSubIfVccTrafficShapingTagging"),
        ("Unisphere-Data-ATM-MIB", "usdAtmSubIfVccTrafficShapingPoliceObserve"),
        ("Unisphere-Data-ATM-MIB", "usdAtmSubIfVccTrafficShapingPacketShaping"))
)
if mibBuilder.loadTexts:
    usdAtmTrafficShapingGroup.setStatus("current")

usdAtmGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 4, 2, 12)
)
usdAtmGroup3.setObjects(
      *(("Unisphere-Data-ATM-MIB", "usdAtmNextIfIndex"),
        ("Unisphere-Data-ATM-MIB", "usdAtmIfRowStatus"),
        ("Unisphere-Data-ATM-MIB", "usdAtmIfLowerIfIndex"),
        ("Unisphere-Data-ATM-MIB", "usdAtmIfIlmiVpi"),
        ("Unisphere-Data-ATM-MIB", "usdAtmIfIlmiVci"),
        ("Unisphere-Data-ATM-MIB", "usdAtmIfIlmiVcd"),
        ("Unisphere-Data-ATM-MIB", "usdAtmIfIlmiPollFrequency"),
        ("Unisphere-Data-ATM-MIB", "usdAtmIfIlmiAdminState"),
        ("Unisphere-Data-ATM-MIB", "usdAtmIfUniVersion"),
        ("Unisphere-Data-ATM-MIB", "usdAtmIfOamCellRxAdminState"),
        ("Unisphere-Data-ATM-MIB", "usdAtmIfInCells"),
        ("Unisphere-Data-ATM-MIB", "usdAtmIfOutCells"),
        ("Unisphere-Data-ATM-MIB", "usdAtmIfVcCount"),
        ("Unisphere-Data-ATM-MIB", "usdAtmIfMapGroup"),
        ("Unisphere-Data-ATM-MIB", "usdAtmIfCacAdminState"),
        ("Unisphere-Data-ATM-MIB", "usdAtmIfCacUbrWeight"),
        ("Unisphere-Data-ATM-MIB", "usdAtmIfCacSubscriptionBandwidth"),
        ("Unisphere-Data-ATM-MIB", "usdAtmIfCacAvailableBandwidth"),
        ("Unisphere-Data-ATM-MIB", "usdAtmIfOamCellFilter"),
        ("Unisphere-Data-ATM-MIB", "usdAtmPvcStatsInCells"),
        ("Unisphere-Data-ATM-MIB", "usdAtmPvcStatsInCellOctets"),
        ("Unisphere-Data-ATM-MIB", "usdAtmPvcStatsInPackets"),
        ("Unisphere-Data-ATM-MIB", "usdAtmPvcStatsInPacketOctets"),
        ("Unisphere-Data-ATM-MIB", "usdAtmPvcStatsOutCells"),
        ("Unisphere-Data-ATM-MIB", "usdAtmPvcStatsOutCellOctets"),
        ("Unisphere-Data-ATM-MIB", "usdAtmPvcStatsOutPackets"),
        ("Unisphere-Data-ATM-MIB", "usdAtmPvcStatsOutPacketOctets"),
        ("Unisphere-Data-ATM-MIB", "usdAtmPvcStatsInCellErrors"),
        ("Unisphere-Data-ATM-MIB", "usdAtmPvcStatsinPacketErrors"),
        ("Unisphere-Data-ATM-MIB", "usdAtmPvcStatsOutCellErrors"),
        ("Unisphere-Data-ATM-MIB", "usdAtmPvcStatsOutPacketErrors"),
        ("Unisphere-Data-ATM-MIB", "usdAtmPvcStatsInPacketDiscards"),
        ("Unisphere-Data-ATM-MIB", "usdAtmPvcStatsInPacketOctetDiscards"),
        ("Unisphere-Data-ATM-MIB", "usdAtmPvcStatsInPacketUnknownProtocol"),
        ("Unisphere-Data-ATM-MIB", "usdAtmIfCapabilityTrafficShaping"),
        ("Unisphere-Data-ATM-MIB", "usdAtmIfCapabilityOam"),
        ("Unisphere-Data-ATM-MIB", "usdAtmIfCapabilityDefaultVcPerVp"),
        ("Unisphere-Data-ATM-MIB", "usdAtmIfCapabilityNumVpiVciBits"),
        ("Unisphere-Data-ATM-MIB", "usdAtmIfCapabilityMaxVcd"),
        ("Unisphere-Data-ATM-MIB", "usdAtmIfCapabilityMaxVpi"),
        ("Unisphere-Data-ATM-MIB", "usdAtmIfCapabilityMaxVci"),
        ("Unisphere-Data-ATM-MIB", "usdAtmIfCapabilityOamCellFilter"))
)
if mibBuilder.loadTexts:
    usdAtmGroup3.setStatus("obsolete")

usdAtmGroup4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 4, 2, 13)
)
usdAtmGroup4.setObjects(
      *(("Unisphere-Data-ATM-MIB", "usdAtmNextIfIndex"),
        ("Unisphere-Data-ATM-MIB", "usdAtmIfRowStatus"),
        ("Unisphere-Data-ATM-MIB", "usdAtmIfLowerIfIndex"),
        ("Unisphere-Data-ATM-MIB", "usdAtmIfIlmiVpi"),
        ("Unisphere-Data-ATM-MIB", "usdAtmIfIlmiVci"),
        ("Unisphere-Data-ATM-MIB", "usdAtmIfIlmiVcd"),
        ("Unisphere-Data-ATM-MIB", "usdAtmIfIlmiPollFrequency"),
        ("Unisphere-Data-ATM-MIB", "usdAtmIfIlmiAdminState"),
        ("Unisphere-Data-ATM-MIB", "usdAtmIfUniVersion"),
        ("Unisphere-Data-ATM-MIB", "usdAtmIfOamCellRxAdminState"),
        ("Unisphere-Data-ATM-MIB", "usdAtmIfInCells"),
        ("Unisphere-Data-ATM-MIB", "usdAtmIfOutCells"),
        ("Unisphere-Data-ATM-MIB", "usdAtmIfVcCount"),
        ("Unisphere-Data-ATM-MIB", "usdAtmIfMapGroup"),
        ("Unisphere-Data-ATM-MIB", "usdAtmIfCacAdminState"),
        ("Unisphere-Data-ATM-MIB", "usdAtmIfCacUbrWeight"),
        ("Unisphere-Data-ATM-MIB", "usdAtmIfCacSubscriptionBandwidth"),
        ("Unisphere-Data-ATM-MIB", "usdAtmIfCacAvailableBandwidth"),
        ("Unisphere-Data-ATM-MIB", "usdAtmIfOamCellFilter"),
        ("Unisphere-Data-ATM-MIB", "usdAtmIfCacUsedBandwidthUpper"),
        ("Unisphere-Data-ATM-MIB", "usdAtmIfCacUsedBandwidthLower"),
        ("Unisphere-Data-ATM-MIB", "usdAtmPvcStatsInCells"),
        ("Unisphere-Data-ATM-MIB", "usdAtmPvcStatsInCellOctets"),
        ("Unisphere-Data-ATM-MIB", "usdAtmPvcStatsInPackets"),
        ("Unisphere-Data-ATM-MIB", "usdAtmPvcStatsInPacketOctets"),
        ("Unisphere-Data-ATM-MIB", "usdAtmPvcStatsOutCells"),
        ("Unisphere-Data-ATM-MIB", "usdAtmPvcStatsOutCellOctets"),
        ("Unisphere-Data-ATM-MIB", "usdAtmPvcStatsOutPackets"),
        ("Unisphere-Data-ATM-MIB", "usdAtmPvcStatsOutPacketOctets"),
        ("Unisphere-Data-ATM-MIB", "usdAtmPvcStatsInCellErrors"),
        ("Unisphere-Data-ATM-MIB", "usdAtmPvcStatsinPacketErrors"),
        ("Unisphere-Data-ATM-MIB", "usdAtmPvcStatsOutCellErrors"),
        ("Unisphere-Data-ATM-MIB", "usdAtmPvcStatsOutPacketErrors"),
        ("Unisphere-Data-ATM-MIB", "usdAtmPvcStatsInPacketDiscards"),
        ("Unisphere-Data-ATM-MIB", "usdAtmPvcStatsInPacketOctetDiscards"),
        ("Unisphere-Data-ATM-MIB", "usdAtmPvcStatsInPacketUnknownProtocol"),
        ("Unisphere-Data-ATM-MIB", "usdAtmIfCapabilityTrafficShaping"),
        ("Unisphere-Data-ATM-MIB", "usdAtmIfCapabilityOam"),
        ("Unisphere-Data-ATM-MIB", "usdAtmIfCapabilityDefaultVcPerVp"),
        ("Unisphere-Data-ATM-MIB", "usdAtmIfCapabilityNumVpiVciBits"),
        ("Unisphere-Data-ATM-MIB", "usdAtmIfCapabilityMaxVcd"),
        ("Unisphere-Data-ATM-MIB", "usdAtmIfCapabilityMaxVpi"),
        ("Unisphere-Data-ATM-MIB", "usdAtmIfCapabilityMaxVci"),
        ("Unisphere-Data-ATM-MIB", "usdAtmIfCapabilityOamCellFilter"))
)
if mibBuilder.loadTexts:
    usdAtmGroup4.setStatus("current")

usdAtmSvcGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 4, 2, 14)
)
usdAtmSvcGroup.setObjects(
      *(("Unisphere-Data-ATM-MIB", "usdAtmIfSvcSignallingVpi"),
        ("Unisphere-Data-ATM-MIB", "usdAtmIfSvcSignallingVci"),
        ("Unisphere-Data-ATM-MIB", "usdAtmIfSvcSignallingVcd"),
        ("Unisphere-Data-ATM-MIB", "usdAtmIfSvcSignallingAdminStatus"),
        ("Unisphere-Data-ATM-MIB", "usdAtmSubIfSvcRowStatus"),
        ("Unisphere-Data-ATM-MIB", "usdAtmSubIfSvcConfigDestAtmAddress"),
        ("Unisphere-Data-ATM-MIB", "usdAtmSubIfSvcConfigCircuitType"),
        ("Unisphere-Data-ATM-MIB", "usdAtmSubIfSvcConfigServiceCategory"),
        ("Unisphere-Data-ATM-MIB", "usdAtmSubIfSvcConfigPcr"),
        ("Unisphere-Data-ATM-MIB", "usdAtmSubIfSvcConfigScr"),
        ("Unisphere-Data-ATM-MIB", "usdAtmSubIfSvcConfigMbs"),
        ("Unisphere-Data-ATM-MIB", "usdAtmSubIfSvcConfigCdvt"),
        ("Unisphere-Data-ATM-MIB", "usdAtmSubIfSvcConfigClp0"),
        ("Unisphere-Data-ATM-MIB", "usdAtmSubIfSvcConfigTagging"),
        ("Unisphere-Data-ATM-MIB", "usdAtmSubIfSvcConfigObserve"),
        ("Unisphere-Data-ATM-MIB", "usdAtmSubIfSvcConfigPacketDiscard"))
)
if mibBuilder.loadTexts:
    usdAtmSvcGroup.setStatus("current")

usdAtmSubIfGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 4, 2, 15)
)
usdAtmSubIfGroup3.setObjects(
      *(("Unisphere-Data-ATM-MIB", "usdAtmSubIfNextIfIndex"),
        ("Unisphere-Data-ATM-MIB", "usdAtmSubIfRowStatus"),
        ("Unisphere-Data-ATM-MIB", "usdAtmSubIfDistinguisher"),
        ("Unisphere-Data-ATM-MIB", "usdAtmSubIfLowerIfIndex"),
        ("Unisphere-Data-ATM-MIB", "usdAtmSubIfNbma"),
        ("Unisphere-Data-ATM-MIB", "usdAtmSubIfAddress"),
        ("Unisphere-Data-ATM-MIB", "usdAtmSubIfVccRowStatus"),
        ("Unisphere-Data-ATM-MIB", "usdAtmSubIfVccVcd"),
        ("Unisphere-Data-ATM-MIB", "usdAtmSubIfVccType"),
        ("Unisphere-Data-ATM-MIB", "usdAtmSubIfVccServiceCategory"),
        ("Unisphere-Data-ATM-MIB", "usdAtmSubIfVccPcr"),
        ("Unisphere-Data-ATM-MIB", "usdAtmSubIfVccScr"),
        ("Unisphere-Data-ATM-MIB", "usdAtmSubIfVccMbs"),
        ("Unisphere-Data-ATM-MIB", "usdAtmSubIfInverseArp"),
        ("Unisphere-Data-ATM-MIB", "usdAtmSubIfInverseArpRefresh"),
        ("Unisphere-Data-ATM-MIB", "usdAtmCircuitOamAdminStatus"),
        ("Unisphere-Data-ATM-MIB", "usdAtmCircuitOamLoopbackOperStatus"),
        ("Unisphere-Data-ATM-MIB", "usdAtmCircuitVcOamOperStatus"),
        ("Unisphere-Data-ATM-MIB", "usdAtmCircuitOamLoopbackFrequency"),
        ("Unisphere-Data-ATM-MIB", "usdAtmCircuitInOamF5Cells"),
        ("Unisphere-Data-ATM-MIB", "usdAtmCircuitInOamCellsDropped"),
        ("Unisphere-Data-ATM-MIB", "usdAtmCircuitOutOamF5Cells"),
        ("Unisphere-Data-ATM-MIB", "usdAtmCircuitInOamF5EndToEndLoopbackCells"),
        ("Unisphere-Data-ATM-MIB", "usdAtmCircuitInOamF5SegmentLoopbackCells"),
        ("Unisphere-Data-ATM-MIB", "usdAtmCircuitInOamF5AisCells"),
        ("Unisphere-Data-ATM-MIB", "usdAtmCircuitInOamF5RdiCells"),
        ("Unisphere-Data-ATM-MIB", "usdAtmCircuitOutOamF5EndToEndLoopbackCells"),
        ("Unisphere-Data-ATM-MIB", "usdAtmCircuitOutOamF5SegmentLoopbackCells"),
        ("Unisphere-Data-ATM-MIB", "usdAtmCircuitOutOamF5RdiCells"))
)
if mibBuilder.loadTexts:
    usdAtmSubIfGroup3.setStatus("current")


# Notification objects

usdAtmVpPingTestCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 3, 0, 1)
)
usdAtmVpPingTestCompleted.setObjects(
      *(("ATM-FORUM-SNMP-M4-MIB", "atmfM4VpTestId"),
        ("ATM-FORUM-SNMP-M4-MIB", "atmfM4VpTestType"),
        ("ATM-FORUM-SNMP-M4-MIB", "atmfM4VpTestResult"),
        ("Unisphere-Data-ATM-MIB", "usdAtmVpPingProbeCount"),
        ("Unisphere-Data-ATM-MIB", "usdAtmVpPingSentProbes"),
        ("Unisphere-Data-ATM-MIB", "usdAtmVpPingProbeResponses"),
        ("Unisphere-Data-ATM-MIB", "usdAtmVpPingMinRtt"),
        ("Unisphere-Data-ATM-MIB", "usdAtmVpPingMaxRtt"),
        ("Unisphere-Data-ATM-MIB", "usdAtmVpPingAverageRtt"))
)
if mibBuilder.loadTexts:
    usdAtmVpPingTestCompleted.setStatus(
        "current"
    )

usdAtmVcPingTestCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 3, 0, 2)
)
usdAtmVcPingTestCompleted.setObjects(
      *(("ATM-FORUM-SNMP-M4-MIB", "atmfM4VcTestId"),
        ("ATM-FORUM-SNMP-M4-MIB", "atmfM4VcTestType"),
        ("ATM-FORUM-SNMP-M4-MIB", "atmfM4VcTestResult"),
        ("Unisphere-Data-ATM-MIB", "usdAtmVcPingProbeCount"),
        ("Unisphere-Data-ATM-MIB", "usdAtmVcPingSentProbes"),
        ("Unisphere-Data-ATM-MIB", "usdAtmVcPingProbeResponses"),
        ("Unisphere-Data-ATM-MIB", "usdAtmVcPingMinRtt"),
        ("Unisphere-Data-ATM-MIB", "usdAtmVcPingMaxRtt"),
        ("Unisphere-Data-ATM-MIB", "usdAtmVcPingAverageRtt"))
)
if mibBuilder.loadTexts:
    usdAtmVcPingTestCompleted.setStatus(
        "current"
    )


# Notifications groups

usdAtmPingTrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 4, 2, 9)
)
usdAtmPingTrapGroup.setObjects(
      *(("Unisphere-Data-ATM-MIB", "usdAtmVpPingTestCompleted"),
        ("Unisphere-Data-ATM-MIB", "usdAtmVcPingTestCompleted"))
)
if mibBuilder.loadTexts:
    usdAtmPingTrapGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

usdAtmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 4, 1, 1)
)
if mibBuilder.loadTexts:
    usdAtmCompliance.setStatus(
        "obsolete"
    )

usdAtmCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 4, 1, 2)
)
if mibBuilder.loadTexts:
    usdAtmCompliance2.setStatus(
        "obsolete"
    )

usdAtmCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 4, 1, 3)
)
if mibBuilder.loadTexts:
    usdAtmCompliance3.setStatus(
        "obsolete"
    )

usdAtmCompliance4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 4, 1, 4)
)
if mibBuilder.loadTexts:
    usdAtmCompliance4.setStatus(
        "obsolete"
    )

usdAtmCompliance5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 4, 1, 5)
)
if mibBuilder.loadTexts:
    usdAtmCompliance5.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Unisphere-Data-ATM-MIB",
    **{"UsdAtmNbmaMapName": UsdAtmNbmaMapName,
       "UsdAtmNbmaMapNameOrNull": UsdAtmNbmaMapNameOrNull,
       "usdAtmMIB": usdAtmMIB,
       "usdAtmObjects": usdAtmObjects,
       "usdAtmIfLayer": usdAtmIfLayer,
       "usdAtmNextIfIndex": usdAtmNextIfIndex,
       "usdAtmIfTable": usdAtmIfTable,
       "usdAtmIfEntry": usdAtmIfEntry,
       "usdAtmIfIndex": usdAtmIfIndex,
       "usdAtmIfRowStatus": usdAtmIfRowStatus,
       "usdAtmIfLowerIfIndex": usdAtmIfLowerIfIndex,
       "usdAtmIfIlmiVpi": usdAtmIfIlmiVpi,
       "usdAtmIfIlmiVci": usdAtmIfIlmiVci,
       "usdAtmIfIlmiVcd": usdAtmIfIlmiVcd,
       "usdAtmIfIlmiPollFrequency": usdAtmIfIlmiPollFrequency,
       "usdAtmIfIlmiAdminState": usdAtmIfIlmiAdminState,
       "usdAtmIfUniVersion": usdAtmIfUniVersion,
       "usdAtmIfOamCellRxAdminState": usdAtmIfOamCellRxAdminState,
       "usdAtmIfInCells": usdAtmIfInCells,
       "usdAtmIfOutCells": usdAtmIfOutCells,
       "usdAtmIfVcCount": usdAtmIfVcCount,
       "usdAtmIfMapGroup": usdAtmIfMapGroup,
       "usdAtmIfCacAdminState": usdAtmIfCacAdminState,
       "usdAtmIfCacUbrWeight": usdAtmIfCacUbrWeight,
       "usdAtmIfCacSubscriptionBandwidth": usdAtmIfCacSubscriptionBandwidth,
       "usdAtmIfCacAvailableBandwidth": usdAtmIfCacAvailableBandwidth,
       "usdAtmIfOamCellFilter": usdAtmIfOamCellFilter,
       "usdAtmIfCacUsedBandwidthUpper": usdAtmIfCacUsedBandwidthUpper,
       "usdAtmIfCacUsedBandwidthLower": usdAtmIfCacUsedBandwidthLower,
       "usdAtmPvcStatisticsTable": usdAtmPvcStatisticsTable,
       "usdAtmPvcStatisticsEntry": usdAtmPvcStatisticsEntry,
       "usdAtmPvcStatsIfIndex": usdAtmPvcStatsIfIndex,
       "usdAtmPvcStatsVpi": usdAtmPvcStatsVpi,
       "usdAtmPvcStatsVci": usdAtmPvcStatsVci,
       "usdAtmPvcStatsInCells": usdAtmPvcStatsInCells,
       "usdAtmPvcStatsInCellOctets": usdAtmPvcStatsInCellOctets,
       "usdAtmPvcStatsInPackets": usdAtmPvcStatsInPackets,
       "usdAtmPvcStatsInPacketOctets": usdAtmPvcStatsInPacketOctets,
       "usdAtmPvcStatsOutCells": usdAtmPvcStatsOutCells,
       "usdAtmPvcStatsOutCellOctets": usdAtmPvcStatsOutCellOctets,
       "usdAtmPvcStatsOutPackets": usdAtmPvcStatsOutPackets,
       "usdAtmPvcStatsOutPacketOctets": usdAtmPvcStatsOutPacketOctets,
       "usdAtmPvcStatsInCellErrors": usdAtmPvcStatsInCellErrors,
       "usdAtmPvcStatsinPacketErrors": usdAtmPvcStatsinPacketErrors,
       "usdAtmPvcStatsOutCellErrors": usdAtmPvcStatsOutCellErrors,
       "usdAtmPvcStatsOutPacketErrors": usdAtmPvcStatsOutPacketErrors,
       "usdAtmPvcStatsInPacketDiscards": usdAtmPvcStatsInPacketDiscards,
       "usdAtmPvcStatsInPacketOctetDiscards": usdAtmPvcStatsInPacketOctetDiscards,
       "usdAtmPvcStatsInPacketUnknownProtocol": usdAtmPvcStatsInPacketUnknownProtocol,
       "usdAtmVpTunnelTable": usdAtmVpTunnelTable,
       "usdAtmVpTunnelEntry": usdAtmVpTunnelEntry,
       "usdAtmVpTunnelIfIndex": usdAtmVpTunnelIfIndex,
       "usdAtmVpTunnelVpi": usdAtmVpTunnelVpi,
       "usdAtmVpTunnelKbps": usdAtmVpTunnelKbps,
       "usdAtmVpTunnelRowStatus": usdAtmVpTunnelRowStatus,
       "usdAtmVpTunnelServiceCategory": usdAtmVpTunnelServiceCategory,
       "usdAtmIfCapabilityTable": usdAtmIfCapabilityTable,
       "usdAtmIfCapabilityEntry": usdAtmIfCapabilityEntry,
       "usdAtmIfCapabilityIndex": usdAtmIfCapabilityIndex,
       "usdAtmIfCapabilityTrafficShaping": usdAtmIfCapabilityTrafficShaping,
       "usdAtmIfCapabilityOam": usdAtmIfCapabilityOam,
       "usdAtmIfCapabilityDefaultVcPerVp": usdAtmIfCapabilityDefaultVcPerVp,
       "usdAtmIfCapabilityNumVpiVciBits": usdAtmIfCapabilityNumVpiVciBits,
       "usdAtmIfCapabilityMaxVcd": usdAtmIfCapabilityMaxVcd,
       "usdAtmIfCapabilityMaxVpi": usdAtmIfCapabilityMaxVpi,
       "usdAtmIfCapabilityMaxVci": usdAtmIfCapabilityMaxVci,
       "usdAtmIfCapabilityOamCellFilter": usdAtmIfCapabilityOamCellFilter,
       "usdAtmIfSvcSignallingTable": usdAtmIfSvcSignallingTable,
       "usdAtmIfSvcSignallingEntry": usdAtmIfSvcSignallingEntry,
       "usdAtmIfSvcSignallingVpi": usdAtmIfSvcSignallingVpi,
       "usdAtmIfSvcSignallingVci": usdAtmIfSvcSignallingVci,
       "usdAtmIfSvcSignallingVcd": usdAtmIfSvcSignallingVcd,
       "usdAtmIfSvcSignallingAdminStatus": usdAtmIfSvcSignallingAdminStatus,
       "usdAtmAal5IfLayer": usdAtmAal5IfLayer,
       "usdAtmAal5NextIfIndex": usdAtmAal5NextIfIndex,
       "usdAtmAal5IfTable": usdAtmAal5IfTable,
       "usdAtmAal5IfEntry": usdAtmAal5IfEntry,
       "usdAtmAal5IfIndex": usdAtmAal5IfIndex,
       "usdAtmAal5IfRowStatus": usdAtmAal5IfRowStatus,
       "usdAtmAal5IfLowerIfIndex": usdAtmAal5IfLowerIfIndex,
       "usdAtmSubIfLayer": usdAtmSubIfLayer,
       "usdAtmSubIfNextIfIndex": usdAtmSubIfNextIfIndex,
       "usdAtmSubIfTable": usdAtmSubIfTable,
       "usdAtmSubIfEntry": usdAtmSubIfEntry,
       "usdAtmSubIfIndex": usdAtmSubIfIndex,
       "usdAtmSubIfRowStatus": usdAtmSubIfRowStatus,
       "usdAtmSubIfDistinguisher": usdAtmSubIfDistinguisher,
       "usdAtmSubIfLowerIfIndex": usdAtmSubIfLowerIfIndex,
       "usdAtmSubIfNbma": usdAtmSubIfNbma,
       "usdAtmSubIfAddress": usdAtmSubIfAddress,
       "usdAtmSubIfVccTable": usdAtmSubIfVccTable,
       "usdAtmSubIfVccEntry": usdAtmSubIfVccEntry,
       "usdAtmSubIfVccVpi": usdAtmSubIfVccVpi,
       "usdAtmSubIfVccVci": usdAtmSubIfVccVci,
       "usdAtmSubIfVccRowStatus": usdAtmSubIfVccRowStatus,
       "usdAtmSubIfVccVcd": usdAtmSubIfVccVcd,
       "usdAtmSubIfVccType": usdAtmSubIfVccType,
       "usdAtmSubIfVccServiceCategory": usdAtmSubIfVccServiceCategory,
       "usdAtmSubIfVccPcr": usdAtmSubIfVccPcr,
       "usdAtmSubIfVccScr": usdAtmSubIfVccScr,
       "usdAtmSubIfVccMbs": usdAtmSubIfVccMbs,
       "usdAtmSubIfInverseArp": usdAtmSubIfInverseArp,
       "usdAtmSubIfInverseArpRefresh": usdAtmSubIfInverseArpRefresh,
       "usdAtmCircuitOamTable": usdAtmCircuitOamTable,
       "usdAtmCircuitOamEntry": usdAtmCircuitOamEntry,
       "usdAtmCircuitOamIfIndex": usdAtmCircuitOamIfIndex,
       "usdAtmCircuitOamVpi": usdAtmCircuitOamVpi,
       "usdAtmCircuitOamVci": usdAtmCircuitOamVci,
       "usdAtmCircuitOamAdminStatus": usdAtmCircuitOamAdminStatus,
       "usdAtmCircuitOamLoopbackOperStatus": usdAtmCircuitOamLoopbackOperStatus,
       "usdAtmCircuitVcOamOperStatus": usdAtmCircuitVcOamOperStatus,
       "usdAtmCircuitOamLoopbackFrequency": usdAtmCircuitOamLoopbackFrequency,
       "usdAtmCircuitInOamF5Cells": usdAtmCircuitInOamF5Cells,
       "usdAtmCircuitInOamCellsDropped": usdAtmCircuitInOamCellsDropped,
       "usdAtmCircuitOutOamF5Cells": usdAtmCircuitOutOamF5Cells,
       "usdAtmCircuitInOamF5EndToEndLoopbackCells": usdAtmCircuitInOamF5EndToEndLoopbackCells,
       "usdAtmCircuitInOamF5SegmentLoopbackCells": usdAtmCircuitInOamF5SegmentLoopbackCells,
       "usdAtmCircuitInOamF5AisCells": usdAtmCircuitInOamF5AisCells,
       "usdAtmCircuitInOamF5RdiCells": usdAtmCircuitInOamF5RdiCells,
       "usdAtmCircuitOutOamF5EndToEndLoopbackCells": usdAtmCircuitOutOamF5EndToEndLoopbackCells,
       "usdAtmCircuitOutOamF5SegmentLoopbackCells": usdAtmCircuitOutOamF5SegmentLoopbackCells,
       "usdAtmCircuitOutOamF5RdiCells": usdAtmCircuitOutOamF5RdiCells,
       "usdAtmSubIfVccTrafficShapingTable": usdAtmSubIfVccTrafficShapingTable,
       "usdAtmSubIfVccTrafficShapingEntry": usdAtmSubIfVccTrafficShapingEntry,
       "usdAtmSubIfVccTrafficShapingCdvt": usdAtmSubIfVccTrafficShapingCdvt,
       "usdAtmSubIfVccTrafficShapingClp0": usdAtmSubIfVccTrafficShapingClp0,
       "usdAtmSubIfVccTrafficShapingTagging": usdAtmSubIfVccTrafficShapingTagging,
       "usdAtmSubIfVccTrafficShapingPoliceObserve": usdAtmSubIfVccTrafficShapingPoliceObserve,
       "usdAtmSubIfVccTrafficShapingPacketShaping": usdAtmSubIfVccTrafficShapingPacketShaping,
       "usdAtmSubIfSvcConfigTable": usdAtmSubIfSvcConfigTable,
       "usdAtmSubIfSvcConfigEntry": usdAtmSubIfSvcConfigEntry,
       "usdAtmSubIfSvcRowStatus": usdAtmSubIfSvcRowStatus,
       "usdAtmSubIfSvcConfigDestAtmAddress": usdAtmSubIfSvcConfigDestAtmAddress,
       "usdAtmSubIfSvcConfigCircuitType": usdAtmSubIfSvcConfigCircuitType,
       "usdAtmSubIfSvcConfigServiceCategory": usdAtmSubIfSvcConfigServiceCategory,
       "usdAtmSubIfSvcConfigPcr": usdAtmSubIfSvcConfigPcr,
       "usdAtmSubIfSvcConfigScr": usdAtmSubIfSvcConfigScr,
       "usdAtmSubIfSvcConfigMbs": usdAtmSubIfSvcConfigMbs,
       "usdAtmSubIfSvcConfigCdvt": usdAtmSubIfSvcConfigCdvt,
       "usdAtmSubIfSvcConfigClp0": usdAtmSubIfSvcConfigClp0,
       "usdAtmSubIfSvcConfigTagging": usdAtmSubIfSvcConfigTagging,
       "usdAtmSubIfSvcConfigObserve": usdAtmSubIfSvcConfigObserve,
       "usdAtmSubIfSvcConfigPacketDiscard": usdAtmSubIfSvcConfigPacketDiscard,
       "usdAtmNbma": usdAtmNbma,
       "usdAtmNbmaMapTable": usdAtmNbmaMapTable,
       "usdAtmNbmaMapEntry": usdAtmNbmaMapEntry,
       "usdAtmNbmaMapName": usdAtmNbmaMapName,
       "usdAtmNbmaMapVcd": usdAtmNbmaMapVcd,
       "usdAtmNbmaMapIpAddress": usdAtmNbmaMapIpAddress,
       "usdAtmNbmaMapVpi": usdAtmNbmaMapVpi,
       "usdAtmNbmaMapVci": usdAtmNbmaMapVci,
       "usdAtmNbmaMapIfIndex": usdAtmNbmaMapIfIndex,
       "usdAtmNbmaMapBroadcast": usdAtmNbmaMapBroadcast,
       "usdAtmNbmaMapRowStatus": usdAtmNbmaMapRowStatus,
       "usdAtmNbmaMapListTable": usdAtmNbmaMapListTable,
       "usdAtmNbmaMapListEntry": usdAtmNbmaMapListEntry,
       "usdAtmNbmaMapListName": usdAtmNbmaMapListName,
       "usdAtmNbmaMapListRowStatus": usdAtmNbmaMapListRowStatus,
       "usdAtmPing": usdAtmPing,
       "usdAtmPingTestTypes": usdAtmPingTestTypes,
       "usdAtmPingTestOamSeg": usdAtmPingTestOamSeg,
       "usdAtmPingTestOamE2E": usdAtmPingTestOamE2E,
       "usdAtmVpPingTable": usdAtmVpPingTable,
       "usdAtmVpPingEntry": usdAtmVpPingEntry,
       "usdAtmVpPingProbeCount": usdAtmVpPingProbeCount,
       "usdAtmVpPingTimeOut": usdAtmVpPingTimeOut,
       "usdAtmVpPingCtlTrapGeneration": usdAtmVpPingCtlTrapGeneration,
       "usdAtmVpPingSentProbes": usdAtmVpPingSentProbes,
       "usdAtmVpPingProbeResponses": usdAtmVpPingProbeResponses,
       "usdAtmVpPingStartTime": usdAtmVpPingStartTime,
       "usdAtmVpPingMinRtt": usdAtmVpPingMinRtt,
       "usdAtmVpPingMaxRtt": usdAtmVpPingMaxRtt,
       "usdAtmVpPingAverageRtt": usdAtmVpPingAverageRtt,
       "usdAtmVcPingTable": usdAtmVcPingTable,
       "usdAtmVcPingEntry": usdAtmVcPingEntry,
       "usdAtmVcPingProbeCount": usdAtmVcPingProbeCount,
       "usdAtmVcPingTimeOut": usdAtmVcPingTimeOut,
       "usdAtmVcPingCtlTrapGeneration": usdAtmVcPingCtlTrapGeneration,
       "usdAtmVcPingSentProbes": usdAtmVcPingSentProbes,
       "usdAtmVcPingProbeResponses": usdAtmVcPingProbeResponses,
       "usdAtmVcPingStartTime": usdAtmVcPingStartTime,
       "usdAtmVcPingMinRtt": usdAtmVcPingMinRtt,
       "usdAtmVcPingMaxRtt": usdAtmVcPingMaxRtt,
       "usdAtmVcPingAverageRtt": usdAtmVcPingAverageRtt,
       "usdAtmTraps": usdAtmTraps,
       "usdAtmTrapPrefix": usdAtmTrapPrefix,
       "usdAtmVpPingTestCompleted": usdAtmVpPingTestCompleted,
       "usdAtmVcPingTestCompleted": usdAtmVcPingTestCompleted,
       "usdAtmConformance": usdAtmConformance,
       "usdAtmCompliances": usdAtmCompliances,
       "usdAtmCompliance": usdAtmCompliance,
       "usdAtmCompliance2": usdAtmCompliance2,
       "usdAtmCompliance3": usdAtmCompliance3,
       "usdAtmCompliance4": usdAtmCompliance4,
       "usdAtmCompliance5": usdAtmCompliance5,
       "usdAtmGroups": usdAtmGroups,
       "usdAtmGroup": usdAtmGroup,
       "usdAtmAal5Group": usdAtmAal5Group,
       "usdAtmSubIfGroup": usdAtmSubIfGroup,
       "usdAtmVpTunnelGroup": usdAtmVpTunnelGroup,
       "usdAtmNbmaMapGroup": usdAtmNbmaMapGroup,
       "usdAtmSubIfGroup2": usdAtmSubIfGroup2,
       "usdAtmVpPingControlGroup": usdAtmVpPingControlGroup,
       "usdAtmVcPingControlGroup": usdAtmVcPingControlGroup,
       "usdAtmPingTrapGroup": usdAtmPingTrapGroup,
       "usdAtmGroup2": usdAtmGroup2,
       "usdAtmTrafficShapingGroup": usdAtmTrafficShapingGroup,
       "usdAtmGroup3": usdAtmGroup3,
       "usdAtmGroup4": usdAtmGroup4,
       "usdAtmSvcGroup": usdAtmSvcGroup,
       "usdAtmSubIfGroup3": usdAtmSubIfGroup3}
)
