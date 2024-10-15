# SNMP MIB module (TPLINK-SNMPRMON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TPLINK-SNMPRMON-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:06:40 2024
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

(tplinkSnmpMIBObjects,) = mibBuilder.importSymbols(
    "TPLINK-SNMP-MIB",
    "tplinkSnmpMIBObjects")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



class EntryStatus(Integer32, TextualConvention):
    status = "current"
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
        *(("createRequest", 2),
          ("invalid", 4),
          ("underCreation", 3),
          ("valid", 1))
    )



# MIB Managed Objects in the order of their OIDs

_TpSnmpRmonControl_ObjectIdentity = ObjectIdentity
tpSnmpRmonControl = _TpSnmpRmonControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 32, 1, 2)
)
_TpSnmpRmonStatisticsCtrl_ObjectIdentity = ObjectIdentity
tpSnmpRmonStatisticsCtrl = _TpSnmpRmonStatisticsCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 32, 1, 2, 1)
)
_TpSnmpRmonStatsCtrlTable_Object = MibTable
tpSnmpRmonStatsCtrlTable = _TpSnmpRmonStatsCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 32, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    tpSnmpRmonStatsCtrlTable.setStatus("current")
_TpSnmpRmonStatsCtrlEntry_Object = MibTableRow
tpSnmpRmonStatsCtrlEntry = _TpSnmpRmonStatsCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 32, 1, 2, 1, 1, 1)
)
tpSnmpRmonStatsCtrlEntry.setIndexNames(
    (0, "TPLINK-SNMPRMON-MIB", "tpSnmpRmonStatsCtrlIndex"),
)
if mibBuilder.loadTexts:
    tpSnmpRmonStatsCtrlEntry.setStatus("current")


class _TpSnmpRmonStatsCtrlIndex_Type(Integer32):
    """Custom type tpSnmpRmonStatsCtrlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TpSnmpRmonStatsCtrlIndex_Type.__name__ = "Integer32"
_TpSnmpRmonStatsCtrlIndex_Object = MibTableColumn
tpSnmpRmonStatsCtrlIndex = _TpSnmpRmonStatsCtrlIndex_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 32, 1, 2, 1, 1, 1, 1),
    _TpSnmpRmonStatsCtrlIndex_Type()
)
tpSnmpRmonStatsCtrlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpSnmpRmonStatsCtrlIndex.setStatus("current")
_TpSnmpRmonStatsCtrlDataSource_Type = OctetString
_TpSnmpRmonStatsCtrlDataSource_Object = MibTableColumn
tpSnmpRmonStatsCtrlDataSource = _TpSnmpRmonStatsCtrlDataSource_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 32, 1, 2, 1, 1, 1, 2),
    _TpSnmpRmonStatsCtrlDataSource_Type()
)
tpSnmpRmonStatsCtrlDataSource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpSnmpRmonStatsCtrlDataSource.setStatus("current")


class _TpSnmpRmonStatsCtrlOwner_Type(OctetString):
    """Custom type tpSnmpRmonStatsCtrlOwner based on OctetString"""
    defaultValue = OctetString("MibBrowser")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_TpSnmpRmonStatsCtrlOwner_Type.__name__ = "OctetString"
_TpSnmpRmonStatsCtrlOwner_Object = MibTableColumn
tpSnmpRmonStatsCtrlOwner = _TpSnmpRmonStatsCtrlOwner_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 32, 1, 2, 1, 1, 1, 3),
    _TpSnmpRmonStatsCtrlOwner_Type()
)
tpSnmpRmonStatsCtrlOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpSnmpRmonStatsCtrlOwner.setStatus("current")


class _TpSnmpRmonStatsCtrlRowStatus_Type(EntryStatus):
    """Custom type tpSnmpRmonStatsCtrlRowStatus based on EntryStatus"""
    defaultValue = 2


_TpSnmpRmonStatsCtrlRowStatus_Object = MibTableColumn
tpSnmpRmonStatsCtrlRowStatus = _TpSnmpRmonStatsCtrlRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 32, 1, 2, 1, 1, 1, 4),
    _TpSnmpRmonStatsCtrlRowStatus_Type()
)
tpSnmpRmonStatsCtrlRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpSnmpRmonStatsCtrlRowStatus.setStatus("current")
_TpSnmpRmonHistoryCtrl_ObjectIdentity = ObjectIdentity
tpSnmpRmonHistoryCtrl = _TpSnmpRmonHistoryCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 32, 1, 2, 2)
)
_TpSnmpRmonHistoryCtrlTable_Object = MibTable
tpSnmpRmonHistoryCtrlTable = _TpSnmpRmonHistoryCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 32, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    tpSnmpRmonHistoryCtrlTable.setStatus("current")
_TpSnmpRmonHistoryCtrlEntry_Object = MibTableRow
tpSnmpRmonHistoryCtrlEntry = _TpSnmpRmonHistoryCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 32, 1, 2, 2, 1, 1)
)
tpSnmpRmonHistoryCtrlEntry.setIndexNames(
    (0, "TPLINK-SNMPRMON-MIB", "tpSnmpRmonHistoryCtrlIndex"),
)
if mibBuilder.loadTexts:
    tpSnmpRmonHistoryCtrlEntry.setStatus("current")
_TpSnmpRmonHistoryCtrlIndex_Type = Integer32
_TpSnmpRmonHistoryCtrlIndex_Object = MibTableColumn
tpSnmpRmonHistoryCtrlIndex = _TpSnmpRmonHistoryCtrlIndex_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 32, 1, 2, 2, 1, 1, 1),
    _TpSnmpRmonHistoryCtrlIndex_Type()
)
tpSnmpRmonHistoryCtrlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpSnmpRmonHistoryCtrlIndex.setStatus("current")
_TpSnmpRmonHistoryCtrlSourcePort_Type = OctetString
_TpSnmpRmonHistoryCtrlSourcePort_Object = MibTableColumn
tpSnmpRmonHistoryCtrlSourcePort = _TpSnmpRmonHistoryCtrlSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 32, 1, 2, 2, 1, 1, 2),
    _TpSnmpRmonHistoryCtrlSourcePort_Type()
)
tpSnmpRmonHistoryCtrlSourcePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpSnmpRmonHistoryCtrlSourcePort.setStatus("current")


class _TpSnmpRmonHistoryCtrlInterval_Type(Integer32):
    """Custom type tpSnmpRmonHistoryCtrlInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 3600),
    )


_TpSnmpRmonHistoryCtrlInterval_Type.__name__ = "Integer32"
_TpSnmpRmonHistoryCtrlInterval_Object = MibTableColumn
tpSnmpRmonHistoryCtrlInterval = _TpSnmpRmonHistoryCtrlInterval_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 32, 1, 2, 2, 1, 1, 3),
    _TpSnmpRmonHistoryCtrlInterval_Type()
)
tpSnmpRmonHistoryCtrlInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpSnmpRmonHistoryCtrlInterval.setStatus("current")


class _TpSnmpRmonHistoryCtrlBucketsRequested_Type(Integer32):
    """Custom type tpSnmpRmonHistoryCtrlBucketsRequested based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TpSnmpRmonHistoryCtrlBucketsRequested_Type.__name__ = "Integer32"
_TpSnmpRmonHistoryCtrlBucketsRequested_Object = MibTableColumn
tpSnmpRmonHistoryCtrlBucketsRequested = _TpSnmpRmonHistoryCtrlBucketsRequested_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 32, 1, 2, 2, 1, 1, 4),
    _TpSnmpRmonHistoryCtrlBucketsRequested_Type()
)
tpSnmpRmonHistoryCtrlBucketsRequested.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpSnmpRmonHistoryCtrlBucketsRequested.setStatus("current")


class _TpSnmpRmonHistoryCtrlOwner_Type(OctetString):
    """Custom type tpSnmpRmonHistoryCtrlOwner based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_TpSnmpRmonHistoryCtrlOwner_Type.__name__ = "OctetString"
_TpSnmpRmonHistoryCtrlOwner_Object = MibTableColumn
tpSnmpRmonHistoryCtrlOwner = _TpSnmpRmonHistoryCtrlOwner_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 32, 1, 2, 2, 1, 1, 5),
    _TpSnmpRmonHistoryCtrlOwner_Type()
)
tpSnmpRmonHistoryCtrlOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpSnmpRmonHistoryCtrlOwner.setStatus("current")


class _TpSnmpRmonHistoryCtrlStatus_Type(Integer32):
    """Custom type tpSnmpRmonHistoryCtrlStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_TpSnmpRmonHistoryCtrlStatus_Type.__name__ = "Integer32"
_TpSnmpRmonHistoryCtrlStatus_Object = MibTableColumn
tpSnmpRmonHistoryCtrlStatus = _TpSnmpRmonHistoryCtrlStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 32, 1, 2, 2, 1, 1, 6),
    _TpSnmpRmonHistoryCtrlStatus_Type()
)
tpSnmpRmonHistoryCtrlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpSnmpRmonHistoryCtrlStatus.setStatus("current")
_TpSnmpRmonHistoryDataTable_Object = MibTable
tpSnmpRmonHistoryDataTable = _TpSnmpRmonHistoryDataTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 32, 1, 2, 2, 2)
)
if mibBuilder.loadTexts:
    tpSnmpRmonHistoryDataTable.setStatus("current")
_TpSnmpRmonHistoryDataEntry_Object = MibTableRow
tpSnmpRmonHistoryDataEntry = _TpSnmpRmonHistoryDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 32, 1, 2, 2, 2, 1)
)
tpSnmpRmonHistoryDataEntry.setIndexNames(
    (0, "TPLINK-SNMPRMON-MIB", "tpSnmpRmonHistoryDataIndex"),
)
if mibBuilder.loadTexts:
    tpSnmpRmonHistoryDataEntry.setStatus("current")


class _TpSnmpRmonHistoryDataIndex_Type(Integer32):
    """Custom type tpSnmpRmonHistoryDataIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TpSnmpRmonHistoryDataIndex_Type.__name__ = "Integer32"
_TpSnmpRmonHistoryDataIndex_Object = MibTableColumn
tpSnmpRmonHistoryDataIndex = _TpSnmpRmonHistoryDataIndex_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 32, 1, 2, 2, 2, 1, 1),
    _TpSnmpRmonHistoryDataIndex_Type()
)
tpSnmpRmonHistoryDataIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpSnmpRmonHistoryDataIndex.setStatus("current")


class _TpSnmpRmonHistoryDataSampleIndex_Type(Integer32):
    """Custom type tpSnmpRmonHistoryDataSampleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_TpSnmpRmonHistoryDataSampleIndex_Type.__name__ = "Integer32"
_TpSnmpRmonHistoryDataSampleIndex_Object = MibTableColumn
tpSnmpRmonHistoryDataSampleIndex = _TpSnmpRmonHistoryDataSampleIndex_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 32, 1, 2, 2, 2, 1, 2),
    _TpSnmpRmonHistoryDataSampleIndex_Type()
)
tpSnmpRmonHistoryDataSampleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpSnmpRmonHistoryDataSampleIndex.setStatus("current")
_TpSnmpRmonHistoryDataIntervalStart_Type = TimeTicks
_TpSnmpRmonHistoryDataIntervalStart_Object = MibTableColumn
tpSnmpRmonHistoryDataIntervalStart = _TpSnmpRmonHistoryDataIntervalStart_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 32, 1, 2, 2, 2, 1, 3),
    _TpSnmpRmonHistoryDataIntervalStart_Type()
)
tpSnmpRmonHistoryDataIntervalStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpSnmpRmonHistoryDataIntervalStart.setStatus("current")
_TpSnmpRmonHistoryDataDropEvents_Type = Counter32
_TpSnmpRmonHistoryDataDropEvents_Object = MibTableColumn
tpSnmpRmonHistoryDataDropEvents = _TpSnmpRmonHistoryDataDropEvents_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 32, 1, 2, 2, 2, 1, 4),
    _TpSnmpRmonHistoryDataDropEvents_Type()
)
tpSnmpRmonHistoryDataDropEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpSnmpRmonHistoryDataDropEvents.setStatus("current")
_TpSnmpRmonHistoryDataOctets_Type = Counter32
_TpSnmpRmonHistoryDataOctets_Object = MibTableColumn
tpSnmpRmonHistoryDataOctets = _TpSnmpRmonHistoryDataOctets_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 32, 1, 2, 2, 2, 1, 5),
    _TpSnmpRmonHistoryDataOctets_Type()
)
tpSnmpRmonHistoryDataOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpSnmpRmonHistoryDataOctets.setStatus("current")
if mibBuilder.loadTexts:
    tpSnmpRmonHistoryDataOctets.setUnits("Octets")
_TpSnmpRmonHistoryDataPkts_Type = Counter32
_TpSnmpRmonHistoryDataPkts_Object = MibTableColumn
tpSnmpRmonHistoryDataPkts = _TpSnmpRmonHistoryDataPkts_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 32, 1, 2, 2, 2, 1, 6),
    _TpSnmpRmonHistoryDataPkts_Type()
)
tpSnmpRmonHistoryDataPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpSnmpRmonHistoryDataPkts.setStatus("current")
if mibBuilder.loadTexts:
    tpSnmpRmonHistoryDataPkts.setUnits("Packets")
_TpSnmpRmonHistoryDataBroadcastPkts_Type = Counter32
_TpSnmpRmonHistoryDataBroadcastPkts_Object = MibTableColumn
tpSnmpRmonHistoryDataBroadcastPkts = _TpSnmpRmonHistoryDataBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 32, 1, 2, 2, 2, 1, 7),
    _TpSnmpRmonHistoryDataBroadcastPkts_Type()
)
tpSnmpRmonHistoryDataBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpSnmpRmonHistoryDataBroadcastPkts.setStatus("current")
if mibBuilder.loadTexts:
    tpSnmpRmonHistoryDataBroadcastPkts.setUnits("Packets")
_TpSnmpRmonHistoryDataMulticastPkts_Type = Counter32
_TpSnmpRmonHistoryDataMulticastPkts_Object = MibTableColumn
tpSnmpRmonHistoryDataMulticastPkts = _TpSnmpRmonHistoryDataMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 32, 1, 2, 2, 2, 1, 8),
    _TpSnmpRmonHistoryDataMulticastPkts_Type()
)
tpSnmpRmonHistoryDataMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpSnmpRmonHistoryDataMulticastPkts.setStatus("current")
if mibBuilder.loadTexts:
    tpSnmpRmonHistoryDataMulticastPkts.setUnits("Packets")
_TpSnmpRmonHistoryDataCRCAlignErrors_Type = Counter32
_TpSnmpRmonHistoryDataCRCAlignErrors_Object = MibTableColumn
tpSnmpRmonHistoryDataCRCAlignErrors = _TpSnmpRmonHistoryDataCRCAlignErrors_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 32, 1, 2, 2, 2, 1, 9),
    _TpSnmpRmonHistoryDataCRCAlignErrors_Type()
)
tpSnmpRmonHistoryDataCRCAlignErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpSnmpRmonHistoryDataCRCAlignErrors.setStatus("current")
if mibBuilder.loadTexts:
    tpSnmpRmonHistoryDataCRCAlignErrors.setUnits("Packets")
_TpSnmpRmonHistoryDataUndersizePkts_Type = Counter32
_TpSnmpRmonHistoryDataUndersizePkts_Object = MibTableColumn
tpSnmpRmonHistoryDataUndersizePkts = _TpSnmpRmonHistoryDataUndersizePkts_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 32, 1, 2, 2, 2, 1, 10),
    _TpSnmpRmonHistoryDataUndersizePkts_Type()
)
tpSnmpRmonHistoryDataUndersizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpSnmpRmonHistoryDataUndersizePkts.setStatus("current")
if mibBuilder.loadTexts:
    tpSnmpRmonHistoryDataUndersizePkts.setUnits("Packets")
_TpSnmpRmonHistoryDataOversizePkts_Type = Counter32
_TpSnmpRmonHistoryDataOversizePkts_Object = MibTableColumn
tpSnmpRmonHistoryDataOversizePkts = _TpSnmpRmonHistoryDataOversizePkts_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 32, 1, 2, 2, 2, 1, 11),
    _TpSnmpRmonHistoryDataOversizePkts_Type()
)
tpSnmpRmonHistoryDataOversizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpSnmpRmonHistoryDataOversizePkts.setStatus("current")
if mibBuilder.loadTexts:
    tpSnmpRmonHistoryDataOversizePkts.setUnits("Packets")
_TpSnmpRmonHistoryDataFragments_Type = Counter32
_TpSnmpRmonHistoryDataFragments_Object = MibTableColumn
tpSnmpRmonHistoryDataFragments = _TpSnmpRmonHistoryDataFragments_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 32, 1, 2, 2, 2, 1, 12),
    _TpSnmpRmonHistoryDataFragments_Type()
)
tpSnmpRmonHistoryDataFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpSnmpRmonHistoryDataFragments.setStatus("current")
if mibBuilder.loadTexts:
    tpSnmpRmonHistoryDataFragments.setUnits("Packets")
_TpSnmpRmonHistoryDataJabbers_Type = Counter32
_TpSnmpRmonHistoryDataJabbers_Object = MibTableColumn
tpSnmpRmonHistoryDataJabbers = _TpSnmpRmonHistoryDataJabbers_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 32, 1, 2, 2, 2, 1, 13),
    _TpSnmpRmonHistoryDataJabbers_Type()
)
tpSnmpRmonHistoryDataJabbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpSnmpRmonHistoryDataJabbers.setStatus("current")
if mibBuilder.loadTexts:
    tpSnmpRmonHistoryDataJabbers.setUnits("Packets")
_TpSnmpRmonHistoryDataCollisions_Type = Counter32
_TpSnmpRmonHistoryDataCollisions_Object = MibTableColumn
tpSnmpRmonHistoryDataCollisions = _TpSnmpRmonHistoryDataCollisions_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 32, 1, 2, 2, 2, 1, 14),
    _TpSnmpRmonHistoryDataCollisions_Type()
)
tpSnmpRmonHistoryDataCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpSnmpRmonHistoryDataCollisions.setStatus("current")
if mibBuilder.loadTexts:
    tpSnmpRmonHistoryDataCollisions.setUnits("Collisions")


class _TpSnmpRmonHistoryDataUtilization_Type(Integer32):
    """Custom type tpSnmpRmonHistoryDataUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_TpSnmpRmonHistoryDataUtilization_Type.__name__ = "Integer32"
_TpSnmpRmonHistoryDataUtilization_Object = MibTableColumn
tpSnmpRmonHistoryDataUtilization = _TpSnmpRmonHistoryDataUtilization_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 32, 1, 2, 2, 2, 1, 15),
    _TpSnmpRmonHistoryDataUtilization_Type()
)
tpSnmpRmonHistoryDataUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpSnmpRmonHistoryDataUtilization.setStatus("current")
_TpSnmpRmonEventCtrl_ObjectIdentity = ObjectIdentity
tpSnmpRmonEventCtrl = _TpSnmpRmonEventCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 32, 1, 2, 3)
)
_TpSnmpRmonEventCtrlTable_Object = MibTable
tpSnmpRmonEventCtrlTable = _TpSnmpRmonEventCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 32, 1, 2, 3, 1)
)
if mibBuilder.loadTexts:
    tpSnmpRmonEventCtrlTable.setStatus("current")
_TpSnmpRmonEventCtrlEntry_Object = MibTableRow
tpSnmpRmonEventCtrlEntry = _TpSnmpRmonEventCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 32, 1, 2, 3, 1, 1)
)
tpSnmpRmonEventCtrlEntry.setIndexNames(
    (0, "TPLINK-SNMPRMON-MIB", "tpSnmpRmonEventCtrlIndex"),
)
if mibBuilder.loadTexts:
    tpSnmpRmonEventCtrlEntry.setStatus("current")
_TpSnmpRmonEventCtrlIndex_Type = Integer32
_TpSnmpRmonEventCtrlIndex_Object = MibTableColumn
tpSnmpRmonEventCtrlIndex = _TpSnmpRmonEventCtrlIndex_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 32, 1, 2, 3, 1, 1, 1),
    _TpSnmpRmonEventCtrlIndex_Type()
)
tpSnmpRmonEventCtrlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpSnmpRmonEventCtrlIndex.setStatus("current")


class _TpSnmpRmonEventCtrlUserName_Type(OctetString):
    """Custom type tpSnmpRmonEventCtrlUserName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_TpSnmpRmonEventCtrlUserName_Type.__name__ = "OctetString"
_TpSnmpRmonEventCtrlUserName_Object = MibTableColumn
tpSnmpRmonEventCtrlUserName = _TpSnmpRmonEventCtrlUserName_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 32, 1, 2, 3, 1, 1, 2),
    _TpSnmpRmonEventCtrlUserName_Type()
)
tpSnmpRmonEventCtrlUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpSnmpRmonEventCtrlUserName.setStatus("current")


class _TpSnmpRmonEventCtrlDesc_Type(OctetString):
    """Custom type tpSnmpRmonEventCtrlDesc based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_TpSnmpRmonEventCtrlDesc_Type.__name__ = "OctetString"
_TpSnmpRmonEventCtrlDesc_Object = MibTableColumn
tpSnmpRmonEventCtrlDesc = _TpSnmpRmonEventCtrlDesc_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 32, 1, 2, 3, 1, 1, 3),
    _TpSnmpRmonEventCtrlDesc_Type()
)
tpSnmpRmonEventCtrlDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpSnmpRmonEventCtrlDesc.setStatus("current")


class _TpSnmpRmonEventCtrlType_Type(Integer32):
    """Custom type tpSnmpRmonEventCtrlType based on Integer32"""
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
        *(("log", 2),
          ("logandtrap", 4),
          ("none", 1),
          ("snmptrap", 3))
    )


_TpSnmpRmonEventCtrlType_Type.__name__ = "Integer32"
_TpSnmpRmonEventCtrlType_Object = MibTableColumn
tpSnmpRmonEventCtrlType = _TpSnmpRmonEventCtrlType_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 32, 1, 2, 3, 1, 1, 4),
    _TpSnmpRmonEventCtrlType_Type()
)
tpSnmpRmonEventCtrlType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpSnmpRmonEventCtrlType.setStatus("current")


class _TpSnmpRmonEventCtrlOwner_Type(OctetString):
    """Custom type tpSnmpRmonEventCtrlOwner based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_TpSnmpRmonEventCtrlOwner_Type.__name__ = "OctetString"
_TpSnmpRmonEventCtrlOwner_Object = MibTableColumn
tpSnmpRmonEventCtrlOwner = _TpSnmpRmonEventCtrlOwner_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 32, 1, 2, 3, 1, 1, 5),
    _TpSnmpRmonEventCtrlOwner_Type()
)
tpSnmpRmonEventCtrlOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpSnmpRmonEventCtrlOwner.setStatus("current")


class _TpSnmpRmonEventCtrlStatus_Type(Integer32):
    """Custom type tpSnmpRmonEventCtrlStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_TpSnmpRmonEventCtrlStatus_Type.__name__ = "Integer32"
_TpSnmpRmonEventCtrlStatus_Object = MibTableColumn
tpSnmpRmonEventCtrlStatus = _TpSnmpRmonEventCtrlStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 32, 1, 2, 3, 1, 1, 6),
    _TpSnmpRmonEventCtrlStatus_Type()
)
tpSnmpRmonEventCtrlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpSnmpRmonEventCtrlStatus.setStatus("current")
_TpSnmpRmonEventLogTable_Object = MibTable
tpSnmpRmonEventLogTable = _TpSnmpRmonEventLogTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 32, 1, 2, 3, 2)
)
if mibBuilder.loadTexts:
    tpSnmpRmonEventLogTable.setStatus("current")
_TpSnmpRmonEventLogEntry_Object = MibTableRow
tpSnmpRmonEventLogEntry = _TpSnmpRmonEventLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 32, 1, 2, 3, 2, 1)
)
tpSnmpRmonEventLogEntry.setIndexNames(
    (0, "TPLINK-SNMPRMON-MIB", "tpSnmpRmonEventLogEventIndex"),
    (0, "TPLINK-SNMPRMON-MIB", "tpSnmpRmonEventLogIndex"),
)
if mibBuilder.loadTexts:
    tpSnmpRmonEventLogEntry.setStatus("current")


class _TpSnmpRmonEventLogEventIndex_Type(Integer32):
    """Custom type tpSnmpRmonEventLogEventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TpSnmpRmonEventLogEventIndex_Type.__name__ = "Integer32"
_TpSnmpRmonEventLogEventIndex_Object = MibTableColumn
tpSnmpRmonEventLogEventIndex = _TpSnmpRmonEventLogEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 32, 1, 2, 3, 2, 1, 1),
    _TpSnmpRmonEventLogEventIndex_Type()
)
tpSnmpRmonEventLogEventIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpSnmpRmonEventLogEventIndex.setStatus("current")


class _TpSnmpRmonEventLogIndex_Type(Integer32):
    """Custom type tpSnmpRmonEventLogIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_TpSnmpRmonEventLogIndex_Type.__name__ = "Integer32"
_TpSnmpRmonEventLogIndex_Object = MibTableColumn
tpSnmpRmonEventLogIndex = _TpSnmpRmonEventLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 32, 1, 2, 3, 2, 1, 2),
    _TpSnmpRmonEventLogIndex_Type()
)
tpSnmpRmonEventLogIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpSnmpRmonEventLogIndex.setStatus("current")
_TpSnmpRmonEventLogTime_Type = TimeTicks
_TpSnmpRmonEventLogTime_Object = MibTableColumn
tpSnmpRmonEventLogTime = _TpSnmpRmonEventLogTime_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 32, 1, 2, 3, 2, 1, 3),
    _TpSnmpRmonEventLogTime_Type()
)
tpSnmpRmonEventLogTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpSnmpRmonEventLogTime.setStatus("current")


class _TpSnmpRmonEventLogDescription_Type(OctetString):
    """Custom type tpSnmpRmonEventLogDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TpSnmpRmonEventLogDescription_Type.__name__ = "OctetString"
_TpSnmpRmonEventLogDescription_Object = MibTableColumn
tpSnmpRmonEventLogDescription = _TpSnmpRmonEventLogDescription_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 32, 1, 2, 3, 2, 1, 4),
    _TpSnmpRmonEventLogDescription_Type()
)
tpSnmpRmonEventLogDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpSnmpRmonEventLogDescription.setStatus("current")
_TpSnmpRmonAlarmCtrl_ObjectIdentity = ObjectIdentity
tpSnmpRmonAlarmCtrl = _TpSnmpRmonAlarmCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 32, 1, 2, 4)
)
_TpSnmpRmonAlarmCtrlTable_Object = MibTable
tpSnmpRmonAlarmCtrlTable = _TpSnmpRmonAlarmCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 32, 1, 2, 4, 1)
)
if mibBuilder.loadTexts:
    tpSnmpRmonAlarmCtrlTable.setStatus("current")
_TpSnmpRmonAlarmCtrlEntry_Object = MibTableRow
tpSnmpRmonAlarmCtrlEntry = _TpSnmpRmonAlarmCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 32, 1, 2, 4, 1, 1)
)
tpSnmpRmonAlarmCtrlEntry.setIndexNames(
    (0, "TPLINK-SNMPRMON-MIB", "tpSnmpRmonAlarmCtrlIndex"),
)
if mibBuilder.loadTexts:
    tpSnmpRmonAlarmCtrlEntry.setStatus("current")
_TpSnmpRmonAlarmCtrlIndex_Type = Integer32
_TpSnmpRmonAlarmCtrlIndex_Object = MibTableColumn
tpSnmpRmonAlarmCtrlIndex = _TpSnmpRmonAlarmCtrlIndex_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 32, 1, 2, 4, 1, 1, 1),
    _TpSnmpRmonAlarmCtrlIndex_Type()
)
tpSnmpRmonAlarmCtrlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpSnmpRmonAlarmCtrlIndex.setStatus("current")


class _TpSnmpRmonAlarmCtrlVariable_Type(Integer32):
    """Custom type tpSnmpRmonAlarmCtrlVariable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("bPackets", 6),
          ("collisions", 13),
          ("crcAlignErr", 8),
          ("dropEvent", 3),
          ("fragments", 11),
          ("jabbers", 12),
          ("mPackets", 7),
          ("oversize", 10),
          ("packet64Bytes", 14),
          ("packetFrom1024to10240", 19),
          ("packetFrom128to255", 16),
          ("packetFrom256to511", 17),
          ("packetFrom512to1023", 18),
          ("packetFrom65to127", 15),
          ("recBytes", 4),
          ("recPackets", 5),
          ("undersize", 9))
    )


_TpSnmpRmonAlarmCtrlVariable_Type.__name__ = "Integer32"
_TpSnmpRmonAlarmCtrlVariable_Object = MibTableColumn
tpSnmpRmonAlarmCtrlVariable = _TpSnmpRmonAlarmCtrlVariable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 32, 1, 2, 4, 1, 1, 2),
    _TpSnmpRmonAlarmCtrlVariable_Type()
)
tpSnmpRmonAlarmCtrlVariable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpSnmpRmonAlarmCtrlVariable.setStatus("current")


class _TpSnmpRmonAlarmCtrlStatisticsIndex_Type(Integer32):
    """Custom type tpSnmpRmonAlarmCtrlStatisticsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TpSnmpRmonAlarmCtrlStatisticsIndex_Type.__name__ = "Integer32"
_TpSnmpRmonAlarmCtrlStatisticsIndex_Object = MibTableColumn
tpSnmpRmonAlarmCtrlStatisticsIndex = _TpSnmpRmonAlarmCtrlStatisticsIndex_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 32, 1, 2, 4, 1, 1, 3),
    _TpSnmpRmonAlarmCtrlStatisticsIndex_Type()
)
tpSnmpRmonAlarmCtrlStatisticsIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpSnmpRmonAlarmCtrlStatisticsIndex.setStatus("current")


class _TpSnmpRmonAlarmCtrlSampleType_Type(Integer32):
    """Custom type tpSnmpRmonAlarmCtrlSampleType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("absoluteValue", 1),
          ("deltaValue", 2))
    )


_TpSnmpRmonAlarmCtrlSampleType_Type.__name__ = "Integer32"
_TpSnmpRmonAlarmCtrlSampleType_Object = MibTableColumn
tpSnmpRmonAlarmCtrlSampleType = _TpSnmpRmonAlarmCtrlSampleType_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 32, 1, 2, 4, 1, 1, 4),
    _TpSnmpRmonAlarmCtrlSampleType_Type()
)
tpSnmpRmonAlarmCtrlSampleType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpSnmpRmonAlarmCtrlSampleType.setStatus("current")


class _TpSnmpRmonAlarmCtrlRisingThreshold_Type(Integer32):
    """Custom type tpSnmpRmonAlarmCtrlRisingThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TpSnmpRmonAlarmCtrlRisingThreshold_Type.__name__ = "Integer32"
_TpSnmpRmonAlarmCtrlRisingThreshold_Object = MibTableColumn
tpSnmpRmonAlarmCtrlRisingThreshold = _TpSnmpRmonAlarmCtrlRisingThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 32, 1, 2, 4, 1, 1, 5),
    _TpSnmpRmonAlarmCtrlRisingThreshold_Type()
)
tpSnmpRmonAlarmCtrlRisingThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpSnmpRmonAlarmCtrlRisingThreshold.setStatus("current")


class _TpSnmpRmonAlarmCtrlRisingEvent_Type(Integer32):
    """Custom type tpSnmpRmonAlarmCtrlRisingEvent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_TpSnmpRmonAlarmCtrlRisingEvent_Type.__name__ = "Integer32"
_TpSnmpRmonAlarmCtrlRisingEvent_Object = MibTableColumn
tpSnmpRmonAlarmCtrlRisingEvent = _TpSnmpRmonAlarmCtrlRisingEvent_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 32, 1, 2, 4, 1, 1, 6),
    _TpSnmpRmonAlarmCtrlRisingEvent_Type()
)
tpSnmpRmonAlarmCtrlRisingEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpSnmpRmonAlarmCtrlRisingEvent.setStatus("current")


class _TpSnmpRmonAlarmCtrlFallingThreshold_Type(Integer32):
    """Custom type tpSnmpRmonAlarmCtrlFallingThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TpSnmpRmonAlarmCtrlFallingThreshold_Type.__name__ = "Integer32"
_TpSnmpRmonAlarmCtrlFallingThreshold_Object = MibTableColumn
tpSnmpRmonAlarmCtrlFallingThreshold = _TpSnmpRmonAlarmCtrlFallingThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 32, 1, 2, 4, 1, 1, 7),
    _TpSnmpRmonAlarmCtrlFallingThreshold_Type()
)
tpSnmpRmonAlarmCtrlFallingThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpSnmpRmonAlarmCtrlFallingThreshold.setStatus("current")


class _TpSnmpRmonAlarmCtrlFallingEvent_Type(Integer32):
    """Custom type tpSnmpRmonAlarmCtrlFallingEvent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_TpSnmpRmonAlarmCtrlFallingEvent_Type.__name__ = "Integer32"
_TpSnmpRmonAlarmCtrlFallingEvent_Object = MibTableColumn
tpSnmpRmonAlarmCtrlFallingEvent = _TpSnmpRmonAlarmCtrlFallingEvent_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 32, 1, 2, 4, 1, 1, 8),
    _TpSnmpRmonAlarmCtrlFallingEvent_Type()
)
tpSnmpRmonAlarmCtrlFallingEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpSnmpRmonAlarmCtrlFallingEvent.setStatus("current")


class _TpSnmpRmonAlarmCtrlStartUp_Type(Integer32):
    """Custom type tpSnmpRmonAlarmCtrlStartUp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fallingAlarm", 2),
          ("risingAlarm", 1),
          ("risingOrFallingAlarm", 3))
    )


_TpSnmpRmonAlarmCtrlStartUp_Type.__name__ = "Integer32"
_TpSnmpRmonAlarmCtrlStartUp_Object = MibTableColumn
tpSnmpRmonAlarmCtrlStartUp = _TpSnmpRmonAlarmCtrlStartUp_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 32, 1, 2, 4, 1, 1, 9),
    _TpSnmpRmonAlarmCtrlStartUp_Type()
)
tpSnmpRmonAlarmCtrlStartUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpSnmpRmonAlarmCtrlStartUp.setStatus("current")


class _TpSnmpRmonAlarmCtrlInterval_Type(Integer32):
    """Custom type tpSnmpRmonAlarmCtrlInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 3600),
    )


_TpSnmpRmonAlarmCtrlInterval_Type.__name__ = "Integer32"
_TpSnmpRmonAlarmCtrlInterval_Object = MibTableColumn
tpSnmpRmonAlarmCtrlInterval = _TpSnmpRmonAlarmCtrlInterval_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 32, 1, 2, 4, 1, 1, 10),
    _TpSnmpRmonAlarmCtrlInterval_Type()
)
tpSnmpRmonAlarmCtrlInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpSnmpRmonAlarmCtrlInterval.setStatus("current")


class _TpSnmpRmonAlarmCtrlOwner_Type(OctetString):
    """Custom type tpSnmpRmonAlarmCtrlOwner based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_TpSnmpRmonAlarmCtrlOwner_Type.__name__ = "OctetString"
_TpSnmpRmonAlarmCtrlOwner_Object = MibTableColumn
tpSnmpRmonAlarmCtrlOwner = _TpSnmpRmonAlarmCtrlOwner_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 32, 1, 2, 4, 1, 1, 11),
    _TpSnmpRmonAlarmCtrlOwner_Type()
)
tpSnmpRmonAlarmCtrlOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpSnmpRmonAlarmCtrlOwner.setStatus("current")


class _TpSnmpRmonAlarmCtrlStatus_Type(Integer32):
    """Custom type tpSnmpRmonAlarmCtrlStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_TpSnmpRmonAlarmCtrlStatus_Type.__name__ = "Integer32"
_TpSnmpRmonAlarmCtrlStatus_Object = MibTableColumn
tpSnmpRmonAlarmCtrlStatus = _TpSnmpRmonAlarmCtrlStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 32, 1, 2, 4, 1, 1, 12),
    _TpSnmpRmonAlarmCtrlStatus_Type()
)
tpSnmpRmonAlarmCtrlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpSnmpRmonAlarmCtrlStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPLINK-SNMPRMON-MIB",
    **{"EntryStatus": EntryStatus,
       "tpSnmpRmonControl": tpSnmpRmonControl,
       "tpSnmpRmonStatisticsCtrl": tpSnmpRmonStatisticsCtrl,
       "tpSnmpRmonStatsCtrlTable": tpSnmpRmonStatsCtrlTable,
       "tpSnmpRmonStatsCtrlEntry": tpSnmpRmonStatsCtrlEntry,
       "tpSnmpRmonStatsCtrlIndex": tpSnmpRmonStatsCtrlIndex,
       "tpSnmpRmonStatsCtrlDataSource": tpSnmpRmonStatsCtrlDataSource,
       "tpSnmpRmonStatsCtrlOwner": tpSnmpRmonStatsCtrlOwner,
       "tpSnmpRmonStatsCtrlRowStatus": tpSnmpRmonStatsCtrlRowStatus,
       "tpSnmpRmonHistoryCtrl": tpSnmpRmonHistoryCtrl,
       "tpSnmpRmonHistoryCtrlTable": tpSnmpRmonHistoryCtrlTable,
       "tpSnmpRmonHistoryCtrlEntry": tpSnmpRmonHistoryCtrlEntry,
       "tpSnmpRmonHistoryCtrlIndex": tpSnmpRmonHistoryCtrlIndex,
       "tpSnmpRmonHistoryCtrlSourcePort": tpSnmpRmonHistoryCtrlSourcePort,
       "tpSnmpRmonHistoryCtrlInterval": tpSnmpRmonHistoryCtrlInterval,
       "tpSnmpRmonHistoryCtrlBucketsRequested": tpSnmpRmonHistoryCtrlBucketsRequested,
       "tpSnmpRmonHistoryCtrlOwner": tpSnmpRmonHistoryCtrlOwner,
       "tpSnmpRmonHistoryCtrlStatus": tpSnmpRmonHistoryCtrlStatus,
       "tpSnmpRmonHistoryDataTable": tpSnmpRmonHistoryDataTable,
       "tpSnmpRmonHistoryDataEntry": tpSnmpRmonHistoryDataEntry,
       "tpSnmpRmonHistoryDataIndex": tpSnmpRmonHistoryDataIndex,
       "tpSnmpRmonHistoryDataSampleIndex": tpSnmpRmonHistoryDataSampleIndex,
       "tpSnmpRmonHistoryDataIntervalStart": tpSnmpRmonHistoryDataIntervalStart,
       "tpSnmpRmonHistoryDataDropEvents": tpSnmpRmonHistoryDataDropEvents,
       "tpSnmpRmonHistoryDataOctets": tpSnmpRmonHistoryDataOctets,
       "tpSnmpRmonHistoryDataPkts": tpSnmpRmonHistoryDataPkts,
       "tpSnmpRmonHistoryDataBroadcastPkts": tpSnmpRmonHistoryDataBroadcastPkts,
       "tpSnmpRmonHistoryDataMulticastPkts": tpSnmpRmonHistoryDataMulticastPkts,
       "tpSnmpRmonHistoryDataCRCAlignErrors": tpSnmpRmonHistoryDataCRCAlignErrors,
       "tpSnmpRmonHistoryDataUndersizePkts": tpSnmpRmonHistoryDataUndersizePkts,
       "tpSnmpRmonHistoryDataOversizePkts": tpSnmpRmonHistoryDataOversizePkts,
       "tpSnmpRmonHistoryDataFragments": tpSnmpRmonHistoryDataFragments,
       "tpSnmpRmonHistoryDataJabbers": tpSnmpRmonHistoryDataJabbers,
       "tpSnmpRmonHistoryDataCollisions": tpSnmpRmonHistoryDataCollisions,
       "tpSnmpRmonHistoryDataUtilization": tpSnmpRmonHistoryDataUtilization,
       "tpSnmpRmonEventCtrl": tpSnmpRmonEventCtrl,
       "tpSnmpRmonEventCtrlTable": tpSnmpRmonEventCtrlTable,
       "tpSnmpRmonEventCtrlEntry": tpSnmpRmonEventCtrlEntry,
       "tpSnmpRmonEventCtrlIndex": tpSnmpRmonEventCtrlIndex,
       "tpSnmpRmonEventCtrlUserName": tpSnmpRmonEventCtrlUserName,
       "tpSnmpRmonEventCtrlDesc": tpSnmpRmonEventCtrlDesc,
       "tpSnmpRmonEventCtrlType": tpSnmpRmonEventCtrlType,
       "tpSnmpRmonEventCtrlOwner": tpSnmpRmonEventCtrlOwner,
       "tpSnmpRmonEventCtrlStatus": tpSnmpRmonEventCtrlStatus,
       "tpSnmpRmonEventLogTable": tpSnmpRmonEventLogTable,
       "tpSnmpRmonEventLogEntry": tpSnmpRmonEventLogEntry,
       "tpSnmpRmonEventLogEventIndex": tpSnmpRmonEventLogEventIndex,
       "tpSnmpRmonEventLogIndex": tpSnmpRmonEventLogIndex,
       "tpSnmpRmonEventLogTime": tpSnmpRmonEventLogTime,
       "tpSnmpRmonEventLogDescription": tpSnmpRmonEventLogDescription,
       "tpSnmpRmonAlarmCtrl": tpSnmpRmonAlarmCtrl,
       "tpSnmpRmonAlarmCtrlTable": tpSnmpRmonAlarmCtrlTable,
       "tpSnmpRmonAlarmCtrlEntry": tpSnmpRmonAlarmCtrlEntry,
       "tpSnmpRmonAlarmCtrlIndex": tpSnmpRmonAlarmCtrlIndex,
       "tpSnmpRmonAlarmCtrlVariable": tpSnmpRmonAlarmCtrlVariable,
       "tpSnmpRmonAlarmCtrlStatisticsIndex": tpSnmpRmonAlarmCtrlStatisticsIndex,
       "tpSnmpRmonAlarmCtrlSampleType": tpSnmpRmonAlarmCtrlSampleType,
       "tpSnmpRmonAlarmCtrlRisingThreshold": tpSnmpRmonAlarmCtrlRisingThreshold,
       "tpSnmpRmonAlarmCtrlRisingEvent": tpSnmpRmonAlarmCtrlRisingEvent,
       "tpSnmpRmonAlarmCtrlFallingThreshold": tpSnmpRmonAlarmCtrlFallingThreshold,
       "tpSnmpRmonAlarmCtrlFallingEvent": tpSnmpRmonAlarmCtrlFallingEvent,
       "tpSnmpRmonAlarmCtrlStartUp": tpSnmpRmonAlarmCtrlStartUp,
       "tpSnmpRmonAlarmCtrlInterval": tpSnmpRmonAlarmCtrlInterval,
       "tpSnmpRmonAlarmCtrlOwner": tpSnmpRmonAlarmCtrlOwner,
       "tpSnmpRmonAlarmCtrlStatus": tpSnmpRmonAlarmCtrlStatus}
)
