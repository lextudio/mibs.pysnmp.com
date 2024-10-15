# SNMP MIB module (FRSLD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/FRSLD-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:46:27 2024
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

(DLCI,) = mibBuilder.importSymbols(
    "FRAME-RELAY-DTE-MIB",
    "DLCI")

(CounterBasedGauge64,) = mibBuilder.importSymbols(
    "HCNUM-TC",
    "CounterBasedGauge64")

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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DisplayString,
 RowStatus,
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

frsldMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 95)
)
frsldMIB.setRevisions(
        ("2002-01-03 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class FrsldTxRP(Integer32, TextualConvention):
    status = "current"
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
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("eqiTxLocalRP", 4),
          ("eqiTxRemoteRP", 10),
          ("eqoTxLocalRP", 5),
          ("eqoTxRemoteRP", 11),
          ("ingTxLocalRP", 2),
          ("ingTxRemoteRP", 8),
          ("otherTxLocalRP", 6),
          ("otherTxRemoteRP", 12),
          ("srcLocalRP", 1),
          ("srcRemoteRP", 7),
          ("tpTxLocalRP", 3),
          ("tpTxRemoteRP", 9))
    )



class FrsldRxRP(Integer32, TextualConvention):
    status = "current"
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
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("desLocalRP", 1),
          ("desRemoteRP", 7),
          ("eqiRxLocalRP", 4),
          ("eqiRxRemoteRP", 10),
          ("eqoRxLocalRP", 5),
          ("eqoRxRemoteRP", 11),
          ("ingRxLocalRP", 2),
          ("ingRxRemoteRP", 8),
          ("otherRxLocalRP", 6),
          ("otherRxRemoteRP", 12),
          ("tpRxLocalRP", 3),
          ("tpRxRemoteRP", 9))
    )



# MIB Managed Objects in the order of their OIDs

_FrsldObjects_ObjectIdentity = ObjectIdentity
frsldObjects = _FrsldObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 95, 1)
)
_FrsldPvcCtrlTable_Object = MibTable
frsldPvcCtrlTable = _FrsldPvcCtrlTable_Object(
    (1, 3, 6, 1, 2, 1, 95, 1, 1)
)
if mibBuilder.loadTexts:
    frsldPvcCtrlTable.setStatus("current")
_FrsldPvcCtrlEntry_Object = MibTableRow
frsldPvcCtrlEntry = _FrsldPvcCtrlEntry_Object(
    (1, 3, 6, 1, 2, 1, 95, 1, 1, 1)
)
frsldPvcCtrlEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "FRSLD-MIB", "frsldPvcCtrlDlci"),
    (0, "FRSLD-MIB", "frsldPvcCtrlTransmitRP"),
    (0, "FRSLD-MIB", "frsldPvcCtrlReceiveRP"),
)
if mibBuilder.loadTexts:
    frsldPvcCtrlEntry.setStatus("current")
_FrsldPvcCtrlDlci_Type = DLCI
_FrsldPvcCtrlDlci_Object = MibTableColumn
frsldPvcCtrlDlci = _FrsldPvcCtrlDlci_Object(
    (1, 3, 6, 1, 2, 1, 95, 1, 1, 1, 1),
    _FrsldPvcCtrlDlci_Type()
)
frsldPvcCtrlDlci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    frsldPvcCtrlDlci.setStatus("current")
_FrsldPvcCtrlTransmitRP_Type = FrsldTxRP
_FrsldPvcCtrlTransmitRP_Object = MibTableColumn
frsldPvcCtrlTransmitRP = _FrsldPvcCtrlTransmitRP_Object(
    (1, 3, 6, 1, 2, 1, 95, 1, 1, 1, 2),
    _FrsldPvcCtrlTransmitRP_Type()
)
frsldPvcCtrlTransmitRP.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    frsldPvcCtrlTransmitRP.setStatus("current")
_FrsldPvcCtrlReceiveRP_Type = FrsldRxRP
_FrsldPvcCtrlReceiveRP_Object = MibTableColumn
frsldPvcCtrlReceiveRP = _FrsldPvcCtrlReceiveRP_Object(
    (1, 3, 6, 1, 2, 1, 95, 1, 1, 1, 3),
    _FrsldPvcCtrlReceiveRP_Type()
)
frsldPvcCtrlReceiveRP.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    frsldPvcCtrlReceiveRP.setStatus("current")
_FrsldPvcCtrlStatus_Type = RowStatus
_FrsldPvcCtrlStatus_Object = MibTableColumn
frsldPvcCtrlStatus = _FrsldPvcCtrlStatus_Object(
    (1, 3, 6, 1, 2, 1, 95, 1, 1, 1, 4),
    _FrsldPvcCtrlStatus_Type()
)
frsldPvcCtrlStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    frsldPvcCtrlStatus.setStatus("current")


class _FrsldPvcCtrlPacketFreq_Type(Integer32):
    """Custom type frsldPvcCtrlPacketFreq based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_FrsldPvcCtrlPacketFreq_Type.__name__ = "Integer32"
_FrsldPvcCtrlPacketFreq_Object = MibTableColumn
frsldPvcCtrlPacketFreq = _FrsldPvcCtrlPacketFreq_Object(
    (1, 3, 6, 1, 2, 1, 95, 1, 1, 1, 5),
    _FrsldPvcCtrlPacketFreq_Type()
)
frsldPvcCtrlPacketFreq.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    frsldPvcCtrlPacketFreq.setStatus("current")
if mibBuilder.loadTexts:
    frsldPvcCtrlPacketFreq.setUnits("seconds")


class _FrsldPvcCtrlDelayFrSize_Type(Integer32):
    """Custom type frsldPvcCtrlDelayFrSize based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8188),
    )


_FrsldPvcCtrlDelayFrSize_Type.__name__ = "Integer32"
_FrsldPvcCtrlDelayFrSize_Object = MibTableColumn
frsldPvcCtrlDelayFrSize = _FrsldPvcCtrlDelayFrSize_Object(
    (1, 3, 6, 1, 2, 1, 95, 1, 1, 1, 6),
    _FrsldPvcCtrlDelayFrSize_Type()
)
frsldPvcCtrlDelayFrSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    frsldPvcCtrlDelayFrSize.setStatus("current")
if mibBuilder.loadTexts:
    frsldPvcCtrlDelayFrSize.setUnits("octets")


class _FrsldPvcCtrlDelayType_Type(Integer32):
    """Custom type frsldPvcCtrlDelayType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("oneWay", 1),
          ("roundTrip", 2))
    )


_FrsldPvcCtrlDelayType_Type.__name__ = "Integer32"
_FrsldPvcCtrlDelayType_Object = MibTableColumn
frsldPvcCtrlDelayType = _FrsldPvcCtrlDelayType_Object(
    (1, 3, 6, 1, 2, 1, 95, 1, 1, 1, 7),
    _FrsldPvcCtrlDelayType_Type()
)
frsldPvcCtrlDelayType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    frsldPvcCtrlDelayType.setStatus("current")


class _FrsldPvcCtrlDelayTimeOut_Type(Integer32):
    """Custom type frsldPvcCtrlDelayTimeOut based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_FrsldPvcCtrlDelayTimeOut_Type.__name__ = "Integer32"
_FrsldPvcCtrlDelayTimeOut_Object = MibTableColumn
frsldPvcCtrlDelayTimeOut = _FrsldPvcCtrlDelayTimeOut_Object(
    (1, 3, 6, 1, 2, 1, 95, 1, 1, 1, 8),
    _FrsldPvcCtrlDelayTimeOut_Type()
)
frsldPvcCtrlDelayTimeOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    frsldPvcCtrlDelayTimeOut.setStatus("current")
if mibBuilder.loadTexts:
    frsldPvcCtrlDelayTimeOut.setUnits("seconds")


class _FrsldPvcCtrlPurge_Type(Integer32):
    """Custom type frsldPvcCtrlPurge based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 172800),
    )


_FrsldPvcCtrlPurge_Type.__name__ = "Integer32"
_FrsldPvcCtrlPurge_Object = MibTableColumn
frsldPvcCtrlPurge = _FrsldPvcCtrlPurge_Object(
    (1, 3, 6, 1, 2, 1, 95, 1, 1, 1, 9),
    _FrsldPvcCtrlPurge_Type()
)
frsldPvcCtrlPurge.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    frsldPvcCtrlPurge.setStatus("current")
if mibBuilder.loadTexts:
    frsldPvcCtrlPurge.setUnits("seconds")


class _FrsldPvcCtrlDeleteOnPurge_Type(Integer32):
    """Custom type frsldPvcCtrlDeleteOnPurge based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("all", 3),
          ("none", 1),
          ("sampleContols", 2))
    )


_FrsldPvcCtrlDeleteOnPurge_Type.__name__ = "Integer32"
_FrsldPvcCtrlDeleteOnPurge_Object = MibTableColumn
frsldPvcCtrlDeleteOnPurge = _FrsldPvcCtrlDeleteOnPurge_Object(
    (1, 3, 6, 1, 2, 1, 95, 1, 1, 1, 10),
    _FrsldPvcCtrlDeleteOnPurge_Type()
)
frsldPvcCtrlDeleteOnPurge.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    frsldPvcCtrlDeleteOnPurge.setStatus("current")
_FrsldPvcCtrlLastPurgeTime_Type = TimeStamp
_FrsldPvcCtrlLastPurgeTime_Object = MibTableColumn
frsldPvcCtrlLastPurgeTime = _FrsldPvcCtrlLastPurgeTime_Object(
    (1, 3, 6, 1, 2, 1, 95, 1, 1, 1, 11),
    _FrsldPvcCtrlLastPurgeTime_Type()
)
frsldPvcCtrlLastPurgeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frsldPvcCtrlLastPurgeTime.setStatus("current")
_FrsldSmplCtrlTable_Object = MibTable
frsldSmplCtrlTable = _FrsldSmplCtrlTable_Object(
    (1, 3, 6, 1, 2, 1, 95, 1, 2)
)
if mibBuilder.loadTexts:
    frsldSmplCtrlTable.setStatus("current")
_FrsldSmplCtrlEntry_Object = MibTableRow
frsldSmplCtrlEntry = _FrsldSmplCtrlEntry_Object(
    (1, 3, 6, 1, 2, 1, 95, 1, 2, 1)
)
frsldSmplCtrlEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "FRSLD-MIB", "frsldPvcCtrlDlci"),
    (0, "FRSLD-MIB", "frsldPvcCtrlTransmitRP"),
    (0, "FRSLD-MIB", "frsldPvcCtrlReceiveRP"),
    (0, "FRSLD-MIB", "frsldSmplCtrlIdx"),
)
if mibBuilder.loadTexts:
    frsldSmplCtrlEntry.setStatus("current")


class _FrsldSmplCtrlIdx_Type(Integer32):
    """Custom type frsldSmplCtrlIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_FrsldSmplCtrlIdx_Type.__name__ = "Integer32"
_FrsldSmplCtrlIdx_Object = MibTableColumn
frsldSmplCtrlIdx = _FrsldSmplCtrlIdx_Object(
    (1, 3, 6, 1, 2, 1, 95, 1, 2, 1, 1),
    _FrsldSmplCtrlIdx_Type()
)
frsldSmplCtrlIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    frsldSmplCtrlIdx.setStatus("current")
_FrsldSmplCtrlStatus_Type = RowStatus
_FrsldSmplCtrlStatus_Object = MibTableColumn
frsldSmplCtrlStatus = _FrsldSmplCtrlStatus_Object(
    (1, 3, 6, 1, 2, 1, 95, 1, 2, 1, 2),
    _FrsldSmplCtrlStatus_Type()
)
frsldSmplCtrlStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    frsldSmplCtrlStatus.setStatus("current")


class _FrsldSmplCtrlColPeriod_Type(Integer32):
    """Custom type frsldSmplCtrlColPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FrsldSmplCtrlColPeriod_Type.__name__ = "Integer32"
_FrsldSmplCtrlColPeriod_Object = MibTableColumn
frsldSmplCtrlColPeriod = _FrsldSmplCtrlColPeriod_Object(
    (1, 3, 6, 1, 2, 1, 95, 1, 2, 1, 3),
    _FrsldSmplCtrlColPeriod_Type()
)
frsldSmplCtrlColPeriod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    frsldSmplCtrlColPeriod.setStatus("current")
if mibBuilder.loadTexts:
    frsldSmplCtrlColPeriod.setUnits("seconds")


class _FrsldSmplCtrlBuckets_Type(Integer32):
    """Custom type frsldSmplCtrlBuckets based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FrsldSmplCtrlBuckets_Type.__name__ = "Integer32"
_FrsldSmplCtrlBuckets_Object = MibTableColumn
frsldSmplCtrlBuckets = _FrsldSmplCtrlBuckets_Object(
    (1, 3, 6, 1, 2, 1, 95, 1, 2, 1, 4),
    _FrsldSmplCtrlBuckets_Type()
)
frsldSmplCtrlBuckets.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    frsldSmplCtrlBuckets.setStatus("current")


class _FrsldSmplCtrlBucketsGranted_Type(Integer32):
    """Custom type frsldSmplCtrlBucketsGranted based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FrsldSmplCtrlBucketsGranted_Type.__name__ = "Integer32"
_FrsldSmplCtrlBucketsGranted_Object = MibTableColumn
frsldSmplCtrlBucketsGranted = _FrsldSmplCtrlBucketsGranted_Object(
    (1, 3, 6, 1, 2, 1, 95, 1, 2, 1, 5),
    _FrsldSmplCtrlBucketsGranted_Type()
)
frsldSmplCtrlBucketsGranted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frsldSmplCtrlBucketsGranted.setStatus("current")
_FrsldPvcDataTable_Object = MibTable
frsldPvcDataTable = _FrsldPvcDataTable_Object(
    (1, 3, 6, 1, 2, 1, 95, 1, 3)
)
if mibBuilder.loadTexts:
    frsldPvcDataTable.setStatus("current")
_FrsldPvcDataEntry_Object = MibTableRow
frsldPvcDataEntry = _FrsldPvcDataEntry_Object(
    (1, 3, 6, 1, 2, 1, 95, 1, 3, 1)
)
frsldPvcDataEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "FRSLD-MIB", "frsldPvcCtrlDlci"),
    (0, "FRSLD-MIB", "frsldPvcCtrlTransmitRP"),
    (0, "FRSLD-MIB", "frsldPvcCtrlReceiveRP"),
)
if mibBuilder.loadTexts:
    frsldPvcDataEntry.setStatus("current")
_FrsldPvcDataMissedPolls_Type = Counter32
_FrsldPvcDataMissedPolls_Object = MibTableColumn
frsldPvcDataMissedPolls = _FrsldPvcDataMissedPolls_Object(
    (1, 3, 6, 1, 2, 1, 95, 1, 3, 1, 1),
    _FrsldPvcDataMissedPolls_Type()
)
frsldPvcDataMissedPolls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frsldPvcDataMissedPolls.setStatus("current")
_FrsldPvcDataFrDeliveredC_Type = Counter32
_FrsldPvcDataFrDeliveredC_Object = MibTableColumn
frsldPvcDataFrDeliveredC = _FrsldPvcDataFrDeliveredC_Object(
    (1, 3, 6, 1, 2, 1, 95, 1, 3, 1, 2),
    _FrsldPvcDataFrDeliveredC_Type()
)
frsldPvcDataFrDeliveredC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frsldPvcDataFrDeliveredC.setStatus("current")
_FrsldPvcDataFrDeliveredE_Type = Counter32
_FrsldPvcDataFrDeliveredE_Object = MibTableColumn
frsldPvcDataFrDeliveredE = _FrsldPvcDataFrDeliveredE_Object(
    (1, 3, 6, 1, 2, 1, 95, 1, 3, 1, 3),
    _FrsldPvcDataFrDeliveredE_Type()
)
frsldPvcDataFrDeliveredE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frsldPvcDataFrDeliveredE.setStatus("current")
_FrsldPvcDataFrOfferedC_Type = Counter32
_FrsldPvcDataFrOfferedC_Object = MibTableColumn
frsldPvcDataFrOfferedC = _FrsldPvcDataFrOfferedC_Object(
    (1, 3, 6, 1, 2, 1, 95, 1, 3, 1, 4),
    _FrsldPvcDataFrOfferedC_Type()
)
frsldPvcDataFrOfferedC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frsldPvcDataFrOfferedC.setStatus("current")
_FrsldPvcDataFrOfferedE_Type = Counter32
_FrsldPvcDataFrOfferedE_Object = MibTableColumn
frsldPvcDataFrOfferedE = _FrsldPvcDataFrOfferedE_Object(
    (1, 3, 6, 1, 2, 1, 95, 1, 3, 1, 5),
    _FrsldPvcDataFrOfferedE_Type()
)
frsldPvcDataFrOfferedE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frsldPvcDataFrOfferedE.setStatus("current")
_FrsldPvcDataDataDeliveredC_Type = Counter32
_FrsldPvcDataDataDeliveredC_Object = MibTableColumn
frsldPvcDataDataDeliveredC = _FrsldPvcDataDataDeliveredC_Object(
    (1, 3, 6, 1, 2, 1, 95, 1, 3, 1, 6),
    _FrsldPvcDataDataDeliveredC_Type()
)
frsldPvcDataDataDeliveredC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frsldPvcDataDataDeliveredC.setStatus("current")
_FrsldPvcDataDataDeliveredE_Type = Counter32
_FrsldPvcDataDataDeliveredE_Object = MibTableColumn
frsldPvcDataDataDeliveredE = _FrsldPvcDataDataDeliveredE_Object(
    (1, 3, 6, 1, 2, 1, 95, 1, 3, 1, 7),
    _FrsldPvcDataDataDeliveredE_Type()
)
frsldPvcDataDataDeliveredE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frsldPvcDataDataDeliveredE.setStatus("current")
_FrsldPvcDataDataOfferedC_Type = Counter32
_FrsldPvcDataDataOfferedC_Object = MibTableColumn
frsldPvcDataDataOfferedC = _FrsldPvcDataDataOfferedC_Object(
    (1, 3, 6, 1, 2, 1, 95, 1, 3, 1, 8),
    _FrsldPvcDataDataOfferedC_Type()
)
frsldPvcDataDataOfferedC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frsldPvcDataDataOfferedC.setStatus("current")
_FrsldPvcDataDataOfferedE_Type = Counter32
_FrsldPvcDataDataOfferedE_Object = MibTableColumn
frsldPvcDataDataOfferedE = _FrsldPvcDataDataOfferedE_Object(
    (1, 3, 6, 1, 2, 1, 95, 1, 3, 1, 9),
    _FrsldPvcDataDataOfferedE_Type()
)
frsldPvcDataDataOfferedE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frsldPvcDataDataOfferedE.setStatus("current")
_FrsldPvcDataHCFrDeliveredC_Type = Counter64
_FrsldPvcDataHCFrDeliveredC_Object = MibTableColumn
frsldPvcDataHCFrDeliveredC = _FrsldPvcDataHCFrDeliveredC_Object(
    (1, 3, 6, 1, 2, 1, 95, 1, 3, 1, 10),
    _FrsldPvcDataHCFrDeliveredC_Type()
)
frsldPvcDataHCFrDeliveredC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frsldPvcDataHCFrDeliveredC.setStatus("current")
_FrsldPvcDataHCFrDeliveredE_Type = Counter64
_FrsldPvcDataHCFrDeliveredE_Object = MibTableColumn
frsldPvcDataHCFrDeliveredE = _FrsldPvcDataHCFrDeliveredE_Object(
    (1, 3, 6, 1, 2, 1, 95, 1, 3, 1, 11),
    _FrsldPvcDataHCFrDeliveredE_Type()
)
frsldPvcDataHCFrDeliveredE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frsldPvcDataHCFrDeliveredE.setStatus("current")
_FrsldPvcDataHCFrOfferedC_Type = Counter64
_FrsldPvcDataHCFrOfferedC_Object = MibTableColumn
frsldPvcDataHCFrOfferedC = _FrsldPvcDataHCFrOfferedC_Object(
    (1, 3, 6, 1, 2, 1, 95, 1, 3, 1, 12),
    _FrsldPvcDataHCFrOfferedC_Type()
)
frsldPvcDataHCFrOfferedC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frsldPvcDataHCFrOfferedC.setStatus("current")
_FrsldPvcDataHCFrOfferedE_Type = Counter64
_FrsldPvcDataHCFrOfferedE_Object = MibTableColumn
frsldPvcDataHCFrOfferedE = _FrsldPvcDataHCFrOfferedE_Object(
    (1, 3, 6, 1, 2, 1, 95, 1, 3, 1, 13),
    _FrsldPvcDataHCFrOfferedE_Type()
)
frsldPvcDataHCFrOfferedE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frsldPvcDataHCFrOfferedE.setStatus("current")
_FrsldPvcDataHCDataDeliveredC_Type = Counter64
_FrsldPvcDataHCDataDeliveredC_Object = MibTableColumn
frsldPvcDataHCDataDeliveredC = _FrsldPvcDataHCDataDeliveredC_Object(
    (1, 3, 6, 1, 2, 1, 95, 1, 3, 1, 14),
    _FrsldPvcDataHCDataDeliveredC_Type()
)
frsldPvcDataHCDataDeliveredC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frsldPvcDataHCDataDeliveredC.setStatus("current")
_FrsldPvcDataHCDataDeliveredE_Type = Counter64
_FrsldPvcDataHCDataDeliveredE_Object = MibTableColumn
frsldPvcDataHCDataDeliveredE = _FrsldPvcDataHCDataDeliveredE_Object(
    (1, 3, 6, 1, 2, 1, 95, 1, 3, 1, 15),
    _FrsldPvcDataHCDataDeliveredE_Type()
)
frsldPvcDataHCDataDeliveredE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frsldPvcDataHCDataDeliveredE.setStatus("current")
_FrsldPvcDataHCDataOfferedC_Type = Counter64
_FrsldPvcDataHCDataOfferedC_Object = MibTableColumn
frsldPvcDataHCDataOfferedC = _FrsldPvcDataHCDataOfferedC_Object(
    (1, 3, 6, 1, 2, 1, 95, 1, 3, 1, 16),
    _FrsldPvcDataHCDataOfferedC_Type()
)
frsldPvcDataHCDataOfferedC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frsldPvcDataHCDataOfferedC.setStatus("current")
_FrsldPvcDataHCDataOfferedE_Type = Counter64
_FrsldPvcDataHCDataOfferedE_Object = MibTableColumn
frsldPvcDataHCDataOfferedE = _FrsldPvcDataHCDataOfferedE_Object(
    (1, 3, 6, 1, 2, 1, 95, 1, 3, 1, 17),
    _FrsldPvcDataHCDataOfferedE_Type()
)
frsldPvcDataHCDataOfferedE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frsldPvcDataHCDataOfferedE.setStatus("current")
_FrsldPvcDataUnavailableTime_Type = TimeTicks
_FrsldPvcDataUnavailableTime_Object = MibTableColumn
frsldPvcDataUnavailableTime = _FrsldPvcDataUnavailableTime_Object(
    (1, 3, 6, 1, 2, 1, 95, 1, 3, 1, 18),
    _FrsldPvcDataUnavailableTime_Type()
)
frsldPvcDataUnavailableTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frsldPvcDataUnavailableTime.setStatus("current")
_FrsldPvcDataUnavailables_Type = Counter32
_FrsldPvcDataUnavailables_Object = MibTableColumn
frsldPvcDataUnavailables = _FrsldPvcDataUnavailables_Object(
    (1, 3, 6, 1, 2, 1, 95, 1, 3, 1, 19),
    _FrsldPvcDataUnavailables_Type()
)
frsldPvcDataUnavailables.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frsldPvcDataUnavailables.setStatus("current")
_FrsldPvcSampleTable_Object = MibTable
frsldPvcSampleTable = _FrsldPvcSampleTable_Object(
    (1, 3, 6, 1, 2, 1, 95, 1, 4)
)
if mibBuilder.loadTexts:
    frsldPvcSampleTable.setStatus("current")
_FrsldPvcSampleEntry_Object = MibTableRow
frsldPvcSampleEntry = _FrsldPvcSampleEntry_Object(
    (1, 3, 6, 1, 2, 1, 95, 1, 4, 1)
)
frsldPvcSampleEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "FRSLD-MIB", "frsldPvcCtrlDlci"),
    (0, "FRSLD-MIB", "frsldPvcCtrlTransmitRP"),
    (0, "FRSLD-MIB", "frsldPvcCtrlReceiveRP"),
    (0, "FRSLD-MIB", "frsldSmplCtrlIdx"),
    (0, "FRSLD-MIB", "frsldPvcSmplIdx"),
)
if mibBuilder.loadTexts:
    frsldPvcSampleEntry.setStatus("current")


class _FrsldPvcSmplIdx_Type(Integer32):
    """Custom type frsldPvcSmplIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FrsldPvcSmplIdx_Type.__name__ = "Integer32"
_FrsldPvcSmplIdx_Object = MibTableColumn
frsldPvcSmplIdx = _FrsldPvcSmplIdx_Object(
    (1, 3, 6, 1, 2, 1, 95, 1, 4, 1, 1),
    _FrsldPvcSmplIdx_Type()
)
frsldPvcSmplIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    frsldPvcSmplIdx.setStatus("current")
_FrsldPvcSmplDelayMin_Type = Gauge32
_FrsldPvcSmplDelayMin_Object = MibTableColumn
frsldPvcSmplDelayMin = _FrsldPvcSmplDelayMin_Object(
    (1, 3, 6, 1, 2, 1, 95, 1, 4, 1, 2),
    _FrsldPvcSmplDelayMin_Type()
)
frsldPvcSmplDelayMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frsldPvcSmplDelayMin.setStatus("current")
if mibBuilder.loadTexts:
    frsldPvcSmplDelayMin.setUnits("microseconds")
_FrsldPvcSmplDelayMax_Type = Gauge32
_FrsldPvcSmplDelayMax_Object = MibTableColumn
frsldPvcSmplDelayMax = _FrsldPvcSmplDelayMax_Object(
    (1, 3, 6, 1, 2, 1, 95, 1, 4, 1, 3),
    _FrsldPvcSmplDelayMax_Type()
)
frsldPvcSmplDelayMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frsldPvcSmplDelayMax.setStatus("current")
if mibBuilder.loadTexts:
    frsldPvcSmplDelayMax.setUnits("microseconds")
_FrsldPvcSmplDelayAvg_Type = Gauge32
_FrsldPvcSmplDelayAvg_Object = MibTableColumn
frsldPvcSmplDelayAvg = _FrsldPvcSmplDelayAvg_Object(
    (1, 3, 6, 1, 2, 1, 95, 1, 4, 1, 4),
    _FrsldPvcSmplDelayAvg_Type()
)
frsldPvcSmplDelayAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frsldPvcSmplDelayAvg.setStatus("current")
if mibBuilder.loadTexts:
    frsldPvcSmplDelayAvg.setUnits("microseconds")
_FrsldPvcSmplMissedPolls_Type = Gauge32
_FrsldPvcSmplMissedPolls_Object = MibTableColumn
frsldPvcSmplMissedPolls = _FrsldPvcSmplMissedPolls_Object(
    (1, 3, 6, 1, 2, 1, 95, 1, 4, 1, 5),
    _FrsldPvcSmplMissedPolls_Type()
)
frsldPvcSmplMissedPolls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frsldPvcSmplMissedPolls.setStatus("current")
_FrsldPvcSmplFrDeliveredC_Type = Gauge32
_FrsldPvcSmplFrDeliveredC_Object = MibTableColumn
frsldPvcSmplFrDeliveredC = _FrsldPvcSmplFrDeliveredC_Object(
    (1, 3, 6, 1, 2, 1, 95, 1, 4, 1, 6),
    _FrsldPvcSmplFrDeliveredC_Type()
)
frsldPvcSmplFrDeliveredC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frsldPvcSmplFrDeliveredC.setStatus("current")
_FrsldPvcSmplFrDeliveredE_Type = Gauge32
_FrsldPvcSmplFrDeliveredE_Object = MibTableColumn
frsldPvcSmplFrDeliveredE = _FrsldPvcSmplFrDeliveredE_Object(
    (1, 3, 6, 1, 2, 1, 95, 1, 4, 1, 7),
    _FrsldPvcSmplFrDeliveredE_Type()
)
frsldPvcSmplFrDeliveredE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frsldPvcSmplFrDeliveredE.setStatus("current")
_FrsldPvcSmplFrOfferedC_Type = Gauge32
_FrsldPvcSmplFrOfferedC_Object = MibTableColumn
frsldPvcSmplFrOfferedC = _FrsldPvcSmplFrOfferedC_Object(
    (1, 3, 6, 1, 2, 1, 95, 1, 4, 1, 8),
    _FrsldPvcSmplFrOfferedC_Type()
)
frsldPvcSmplFrOfferedC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frsldPvcSmplFrOfferedC.setStatus("current")
_FrsldPvcSmplFrOfferedE_Type = Gauge32
_FrsldPvcSmplFrOfferedE_Object = MibTableColumn
frsldPvcSmplFrOfferedE = _FrsldPvcSmplFrOfferedE_Object(
    (1, 3, 6, 1, 2, 1, 95, 1, 4, 1, 9),
    _FrsldPvcSmplFrOfferedE_Type()
)
frsldPvcSmplFrOfferedE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frsldPvcSmplFrOfferedE.setStatus("current")
_FrsldPvcSmplDataDeliveredC_Type = Gauge32
_FrsldPvcSmplDataDeliveredC_Object = MibTableColumn
frsldPvcSmplDataDeliveredC = _FrsldPvcSmplDataDeliveredC_Object(
    (1, 3, 6, 1, 2, 1, 95, 1, 4, 1, 10),
    _FrsldPvcSmplDataDeliveredC_Type()
)
frsldPvcSmplDataDeliveredC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frsldPvcSmplDataDeliveredC.setStatus("current")
_FrsldPvcSmplDataDeliveredE_Type = Gauge32
_FrsldPvcSmplDataDeliveredE_Object = MibTableColumn
frsldPvcSmplDataDeliveredE = _FrsldPvcSmplDataDeliveredE_Object(
    (1, 3, 6, 1, 2, 1, 95, 1, 4, 1, 11),
    _FrsldPvcSmplDataDeliveredE_Type()
)
frsldPvcSmplDataDeliveredE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frsldPvcSmplDataDeliveredE.setStatus("current")
_FrsldPvcSmplDataOfferedC_Type = Gauge32
_FrsldPvcSmplDataOfferedC_Object = MibTableColumn
frsldPvcSmplDataOfferedC = _FrsldPvcSmplDataOfferedC_Object(
    (1, 3, 6, 1, 2, 1, 95, 1, 4, 1, 12),
    _FrsldPvcSmplDataOfferedC_Type()
)
frsldPvcSmplDataOfferedC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frsldPvcSmplDataOfferedC.setStatus("current")
_FrsldPvcSmplDataOfferedE_Type = Gauge32
_FrsldPvcSmplDataOfferedE_Object = MibTableColumn
frsldPvcSmplDataOfferedE = _FrsldPvcSmplDataOfferedE_Object(
    (1, 3, 6, 1, 2, 1, 95, 1, 4, 1, 13),
    _FrsldPvcSmplDataOfferedE_Type()
)
frsldPvcSmplDataOfferedE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frsldPvcSmplDataOfferedE.setStatus("current")
_FrsldPvcSmplHCFrDeliveredC_Type = CounterBasedGauge64
_FrsldPvcSmplHCFrDeliveredC_Object = MibTableColumn
frsldPvcSmplHCFrDeliveredC = _FrsldPvcSmplHCFrDeliveredC_Object(
    (1, 3, 6, 1, 2, 1, 95, 1, 4, 1, 14),
    _FrsldPvcSmplHCFrDeliveredC_Type()
)
frsldPvcSmplHCFrDeliveredC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frsldPvcSmplHCFrDeliveredC.setStatus("current")
_FrsldPvcSmplHCFrDeliveredE_Type = CounterBasedGauge64
_FrsldPvcSmplHCFrDeliveredE_Object = MibTableColumn
frsldPvcSmplHCFrDeliveredE = _FrsldPvcSmplHCFrDeliveredE_Object(
    (1, 3, 6, 1, 2, 1, 95, 1, 4, 1, 15),
    _FrsldPvcSmplHCFrDeliveredE_Type()
)
frsldPvcSmplHCFrDeliveredE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frsldPvcSmplHCFrDeliveredE.setStatus("current")
_FrsldPvcSmplHCFrOfferedC_Type = CounterBasedGauge64
_FrsldPvcSmplHCFrOfferedC_Object = MibTableColumn
frsldPvcSmplHCFrOfferedC = _FrsldPvcSmplHCFrOfferedC_Object(
    (1, 3, 6, 1, 2, 1, 95, 1, 4, 1, 16),
    _FrsldPvcSmplHCFrOfferedC_Type()
)
frsldPvcSmplHCFrOfferedC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frsldPvcSmplHCFrOfferedC.setStatus("current")
_FrsldPvcSmplHCFrOfferedE_Type = CounterBasedGauge64
_FrsldPvcSmplHCFrOfferedE_Object = MibTableColumn
frsldPvcSmplHCFrOfferedE = _FrsldPvcSmplHCFrOfferedE_Object(
    (1, 3, 6, 1, 2, 1, 95, 1, 4, 1, 17),
    _FrsldPvcSmplHCFrOfferedE_Type()
)
frsldPvcSmplHCFrOfferedE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frsldPvcSmplHCFrOfferedE.setStatus("current")
_FrsldPvcSmplHCDataDeliveredC_Type = CounterBasedGauge64
_FrsldPvcSmplHCDataDeliveredC_Object = MibTableColumn
frsldPvcSmplHCDataDeliveredC = _FrsldPvcSmplHCDataDeliveredC_Object(
    (1, 3, 6, 1, 2, 1, 95, 1, 4, 1, 18),
    _FrsldPvcSmplHCDataDeliveredC_Type()
)
frsldPvcSmplHCDataDeliveredC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frsldPvcSmplHCDataDeliveredC.setStatus("current")
_FrsldPvcSmplHCDataDeliveredE_Type = CounterBasedGauge64
_FrsldPvcSmplHCDataDeliveredE_Object = MibTableColumn
frsldPvcSmplHCDataDeliveredE = _FrsldPvcSmplHCDataDeliveredE_Object(
    (1, 3, 6, 1, 2, 1, 95, 1, 4, 1, 19),
    _FrsldPvcSmplHCDataDeliveredE_Type()
)
frsldPvcSmplHCDataDeliveredE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frsldPvcSmplHCDataDeliveredE.setStatus("current")
_FrsldPvcSmplHCDataOfferedC_Type = CounterBasedGauge64
_FrsldPvcSmplHCDataOfferedC_Object = MibTableColumn
frsldPvcSmplHCDataOfferedC = _FrsldPvcSmplHCDataOfferedC_Object(
    (1, 3, 6, 1, 2, 1, 95, 1, 4, 1, 20),
    _FrsldPvcSmplHCDataOfferedC_Type()
)
frsldPvcSmplHCDataOfferedC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frsldPvcSmplHCDataOfferedC.setStatus("current")
_FrsldPvcSmplHCDataOfferedE_Type = CounterBasedGauge64
_FrsldPvcSmplHCDataOfferedE_Object = MibTableColumn
frsldPvcSmplHCDataOfferedE = _FrsldPvcSmplHCDataOfferedE_Object(
    (1, 3, 6, 1, 2, 1, 95, 1, 4, 1, 21),
    _FrsldPvcSmplHCDataOfferedE_Type()
)
frsldPvcSmplHCDataOfferedE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frsldPvcSmplHCDataOfferedE.setStatus("current")
_FrsldPvcSmplUnavailableTime_Type = TimeTicks
_FrsldPvcSmplUnavailableTime_Object = MibTableColumn
frsldPvcSmplUnavailableTime = _FrsldPvcSmplUnavailableTime_Object(
    (1, 3, 6, 1, 2, 1, 95, 1, 4, 1, 22),
    _FrsldPvcSmplUnavailableTime_Type()
)
frsldPvcSmplUnavailableTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frsldPvcSmplUnavailableTime.setStatus("current")
_FrsldPvcSmplUnavailables_Type = Gauge32
_FrsldPvcSmplUnavailables_Object = MibTableColumn
frsldPvcSmplUnavailables = _FrsldPvcSmplUnavailables_Object(
    (1, 3, 6, 1, 2, 1, 95, 1, 4, 1, 23),
    _FrsldPvcSmplUnavailables_Type()
)
frsldPvcSmplUnavailables.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frsldPvcSmplUnavailables.setStatus("current")
_FrsldPvcSmplStartTime_Type = TimeStamp
_FrsldPvcSmplStartTime_Object = MibTableColumn
frsldPvcSmplStartTime = _FrsldPvcSmplStartTime_Object(
    (1, 3, 6, 1, 2, 1, 95, 1, 4, 1, 24),
    _FrsldPvcSmplStartTime_Type()
)
frsldPvcSmplStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frsldPvcSmplStartTime.setStatus("current")
_FrsldPvcSmplEndTime_Type = TimeStamp
_FrsldPvcSmplEndTime_Object = MibTableColumn
frsldPvcSmplEndTime = _FrsldPvcSmplEndTime_Object(
    (1, 3, 6, 1, 2, 1, 95, 1, 4, 1, 25),
    _FrsldPvcSmplEndTime_Type()
)
frsldPvcSmplEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frsldPvcSmplEndTime.setStatus("current")
_FrsldCapabilities_ObjectIdentity = ObjectIdentity
frsldCapabilities = _FrsldCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 95, 2)
)


class _FrsldPvcCtrlWriteCaps_Type(Bits):
    """Custom type frsldPvcCtrlWriteCaps based on Bits"""
    namedValues = NamedValues(
        *(("frsldPvcCtrlDelayFrSize", 2),
          ("frsldPvcCtrlDelayTimeOut", 4),
          ("frsldPvcCtrlDelayType", 3),
          ("frsldPvcCtrlDeleteOnPurge", 6),
          ("frsldPvcCtrlPacketFreq", 1),
          ("frsldPvcCtrlPurge", 5),
          ("frsldPvcCtrlStatus", 0))
    )

_FrsldPvcCtrlWriteCaps_Type.__name__ = "Bits"
_FrsldPvcCtrlWriteCaps_Object = MibScalar
frsldPvcCtrlWriteCaps = _FrsldPvcCtrlWriteCaps_Object(
    (1, 3, 6, 1, 2, 1, 95, 2, 1),
    _FrsldPvcCtrlWriteCaps_Type()
)
frsldPvcCtrlWriteCaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frsldPvcCtrlWriteCaps.setStatus("current")


class _FrsldSmplCtrlWriteCaps_Type(Bits):
    """Custom type frsldSmplCtrlWriteCaps based on Bits"""
    namedValues = NamedValues(
        *(("frsldSmplCtrlBuckets", 1),
          ("frsldSmplCtrlStatus", 0))
    )

_FrsldSmplCtrlWriteCaps_Type.__name__ = "Bits"
_FrsldSmplCtrlWriteCaps_Object = MibScalar
frsldSmplCtrlWriteCaps = _FrsldSmplCtrlWriteCaps_Object(
    (1, 3, 6, 1, 2, 1, 95, 2, 2),
    _FrsldSmplCtrlWriteCaps_Type()
)
frsldSmplCtrlWriteCaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frsldSmplCtrlWriteCaps.setStatus("current")


class _FrsldRPCaps_Type(Bits):
    """Custom type frsldRPCaps based on Bits"""
    namedValues = NamedValues(
        *(("desLocalRP", 12),
          ("desRemoteRP", 18),
          ("eqiRxLocalRP", 15),
          ("eqiRxRemoteRP", 21),
          ("eqiTxLocalRP", 3),
          ("eqiTxRemoteRP", 9),
          ("eqoRxLocalRP", 16),
          ("eqoRxRemoteRP", 22),
          ("eqoTxLocalRP", 4),
          ("eqoTxRemoteRP", 10),
          ("ingRxLocalRP", 13),
          ("ingRxRemoteRP", 19),
          ("ingTxLocalRP", 1),
          ("ingTxRemoteRP", 7),
          ("otherRxLocalRP", 17),
          ("otherRxRemoteRP", 23),
          ("otherTxLocalRP", 5),
          ("otherTxRemoteRP", 11),
          ("srcLocalRP", 0),
          ("srcRemoteRP", 6),
          ("tpRxLocalRP", 14),
          ("tpRxRemoteRP", 20),
          ("tpTxLocalRP", 2),
          ("tpTxRemoteRP", 8))
    )

_FrsldRPCaps_Type.__name__ = "Bits"
_FrsldRPCaps_Object = MibScalar
frsldRPCaps = _FrsldRPCaps_Object(
    (1, 3, 6, 1, 2, 1, 95, 2, 3),
    _FrsldRPCaps_Type()
)
frsldRPCaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frsldRPCaps.setStatus("current")


class _FrsldMaxPvcCtrls_Type(Integer32):
    """Custom type frsldMaxPvcCtrls based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FrsldMaxPvcCtrls_Type.__name__ = "Integer32"
_FrsldMaxPvcCtrls_Object = MibScalar
frsldMaxPvcCtrls = _FrsldMaxPvcCtrls_Object(
    (1, 3, 6, 1, 2, 1, 95, 2, 4),
    _FrsldMaxPvcCtrls_Type()
)
frsldMaxPvcCtrls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frsldMaxPvcCtrls.setStatus("current")
_FrsldNumPvcCtrls_Type = Gauge32
_FrsldNumPvcCtrls_Object = MibScalar
frsldNumPvcCtrls = _FrsldNumPvcCtrls_Object(
    (1, 3, 6, 1, 2, 1, 95, 2, 5),
    _FrsldNumPvcCtrls_Type()
)
frsldNumPvcCtrls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frsldNumPvcCtrls.setStatus("current")


class _FrsldMaxSmplCtrls_Type(Integer32):
    """Custom type frsldMaxSmplCtrls based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FrsldMaxSmplCtrls_Type.__name__ = "Integer32"
_FrsldMaxSmplCtrls_Object = MibScalar
frsldMaxSmplCtrls = _FrsldMaxSmplCtrls_Object(
    (1, 3, 6, 1, 2, 1, 95, 2, 6),
    _FrsldMaxSmplCtrls_Type()
)
frsldMaxSmplCtrls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frsldMaxSmplCtrls.setStatus("current")
_FrsldNumSmplCtrls_Type = Gauge32
_FrsldNumSmplCtrls_Object = MibScalar
frsldNumSmplCtrls = _FrsldNumSmplCtrls_Object(
    (1, 3, 6, 1, 2, 1, 95, 2, 7),
    _FrsldNumSmplCtrls_Type()
)
frsldNumSmplCtrls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frsldNumSmplCtrls.setStatus("current")
_FrsldConformance_ObjectIdentity = ObjectIdentity
frsldConformance = _FrsldConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 95, 3)
)
_FrsldMIBGroups_ObjectIdentity = ObjectIdentity
frsldMIBGroups = _FrsldMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 95, 3, 1)
)
_FrsldMIBCompliances_ObjectIdentity = ObjectIdentity
frsldMIBCompliances = _FrsldMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 95, 3, 2)
)

# Managed Objects groups

frsldPvcReqCtrlGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 95, 3, 1, 1)
)
frsldPvcReqCtrlGroup.setObjects(
      *(("FRSLD-MIB", "frsldPvcCtrlStatus"),
        ("FRSLD-MIB", "frsldPvcCtrlPurge"),
        ("FRSLD-MIB", "frsldPvcCtrlDeleteOnPurge"),
        ("FRSLD-MIB", "frsldPvcCtrlLastPurgeTime"))
)
if mibBuilder.loadTexts:
    frsldPvcReqCtrlGroup.setStatus("current")

frsldPvcPacketGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 95, 3, 1, 2)
)
frsldPvcPacketGroup.setObjects(
    ("FRSLD-MIB", "frsldPvcCtrlPacketFreq")
)
if mibBuilder.loadTexts:
    frsldPvcPacketGroup.setStatus("current")

frsldPvcDelayCtrlGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 95, 3, 1, 3)
)
frsldPvcDelayCtrlGroup.setObjects(
      *(("FRSLD-MIB", "frsldPvcCtrlDelayFrSize"),
        ("FRSLD-MIB", "frsldPvcCtrlDelayType"),
        ("FRSLD-MIB", "frsldPvcCtrlDelayTimeOut"))
)
if mibBuilder.loadTexts:
    frsldPvcDelayCtrlGroup.setStatus("current")

frsldPvcSampleCtrlGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 95, 3, 1, 4)
)
frsldPvcSampleCtrlGroup.setObjects(
      *(("FRSLD-MIB", "frsldSmplCtrlStatus"),
        ("FRSLD-MIB", "frsldSmplCtrlColPeriod"),
        ("FRSLD-MIB", "frsldSmplCtrlBuckets"),
        ("FRSLD-MIB", "frsldSmplCtrlBucketsGranted"))
)
if mibBuilder.loadTexts:
    frsldPvcSampleCtrlGroup.setStatus("current")

frsldPvcReqDataGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 95, 3, 1, 5)
)
frsldPvcReqDataGroup.setObjects(
      *(("FRSLD-MIB", "frsldPvcDataFrDeliveredC"),
        ("FRSLD-MIB", "frsldPvcDataFrDeliveredE"),
        ("FRSLD-MIB", "frsldPvcDataFrOfferedC"),
        ("FRSLD-MIB", "frsldPvcDataFrOfferedE"),
        ("FRSLD-MIB", "frsldPvcDataDataDeliveredC"),
        ("FRSLD-MIB", "frsldPvcDataDataDeliveredE"),
        ("FRSLD-MIB", "frsldPvcDataDataOfferedC"),
        ("FRSLD-MIB", "frsldPvcDataDataOfferedE"),
        ("FRSLD-MIB", "frsldPvcDataUnavailableTime"),
        ("FRSLD-MIB", "frsldPvcDataUnavailables"))
)
if mibBuilder.loadTexts:
    frsldPvcReqDataGroup.setStatus("current")

frsldPvcDelayDataGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 95, 3, 1, 6)
)
frsldPvcDelayDataGroup.setObjects(
    ("FRSLD-MIB", "frsldPvcDataMissedPolls")
)
if mibBuilder.loadTexts:
    frsldPvcDelayDataGroup.setStatus("current")

frsldPvcHCFrameDataGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 95, 3, 1, 7)
)
frsldPvcHCFrameDataGroup.setObjects(
      *(("FRSLD-MIB", "frsldPvcDataHCFrDeliveredC"),
        ("FRSLD-MIB", "frsldPvcDataHCFrDeliveredE"),
        ("FRSLD-MIB", "frsldPvcDataHCFrOfferedC"),
        ("FRSLD-MIB", "frsldPvcDataHCFrOfferedE"))
)
if mibBuilder.loadTexts:
    frsldPvcHCFrameDataGroup.setStatus("current")

frsldPvcHCOctetDataGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 95, 3, 1, 8)
)
frsldPvcHCOctetDataGroup.setObjects(
      *(("FRSLD-MIB", "frsldPvcDataHCDataDeliveredC"),
        ("FRSLD-MIB", "frsldPvcDataHCDataDeliveredE"),
        ("FRSLD-MIB", "frsldPvcDataHCDataOfferedC"),
        ("FRSLD-MIB", "frsldPvcDataHCDataOfferedE"))
)
if mibBuilder.loadTexts:
    frsldPvcHCOctetDataGroup.setStatus("current")

frsldPvcSampleDelayGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 95, 3, 1, 9)
)
frsldPvcSampleDelayGroup.setObjects(
      *(("FRSLD-MIB", "frsldPvcSmplDelayMin"),
        ("FRSLD-MIB", "frsldPvcSmplDelayMax"),
        ("FRSLD-MIB", "frsldPvcSmplDelayAvg"),
        ("FRSLD-MIB", "frsldPvcSmplMissedPolls"))
)
if mibBuilder.loadTexts:
    frsldPvcSampleDelayGroup.setStatus("current")

frsldPvcSampleDataGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 95, 3, 1, 10)
)
frsldPvcSampleDataGroup.setObjects(
      *(("FRSLD-MIB", "frsldPvcSmplFrDeliveredC"),
        ("FRSLD-MIB", "frsldPvcSmplFrDeliveredE"),
        ("FRSLD-MIB", "frsldPvcSmplFrOfferedC"),
        ("FRSLD-MIB", "frsldPvcSmplFrOfferedE"),
        ("FRSLD-MIB", "frsldPvcSmplDataDeliveredC"),
        ("FRSLD-MIB", "frsldPvcSmplDataDeliveredE"),
        ("FRSLD-MIB", "frsldPvcSmplDataOfferedC"),
        ("FRSLD-MIB", "frsldPvcSmplDataOfferedE"))
)
if mibBuilder.loadTexts:
    frsldPvcSampleDataGroup.setStatus("current")

frsldPvcSampleHCFrameGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 95, 3, 1, 11)
)
frsldPvcSampleHCFrameGroup.setObjects(
      *(("FRSLD-MIB", "frsldPvcSmplHCFrDeliveredC"),
        ("FRSLD-MIB", "frsldPvcSmplHCFrDeliveredE"),
        ("FRSLD-MIB", "frsldPvcSmplHCFrOfferedC"),
        ("FRSLD-MIB", "frsldPvcSmplHCFrOfferedE"))
)
if mibBuilder.loadTexts:
    frsldPvcSampleHCFrameGroup.setStatus("current")

frsldPvcSampleHCDataGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 95, 3, 1, 12)
)
frsldPvcSampleHCDataGroup.setObjects(
      *(("FRSLD-MIB", "frsldPvcSmplHCDataDeliveredC"),
        ("FRSLD-MIB", "frsldPvcSmplHCDataDeliveredE"),
        ("FRSLD-MIB", "frsldPvcSmplHCDataOfferedC"),
        ("FRSLD-MIB", "frsldPvcSmplHCDataOfferedE"))
)
if mibBuilder.loadTexts:
    frsldPvcSampleHCDataGroup.setStatus("current")

frsldPvcSampleAvailGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 95, 3, 1, 13)
)
frsldPvcSampleAvailGroup.setObjects(
      *(("FRSLD-MIB", "frsldPvcSmplUnavailableTime"),
        ("FRSLD-MIB", "frsldPvcSmplUnavailables"))
)
if mibBuilder.loadTexts:
    frsldPvcSampleAvailGroup.setStatus("current")

frsldPvcSampleGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 95, 3, 1, 14)
)
frsldPvcSampleGeneralGroup.setObjects(
      *(("FRSLD-MIB", "frsldPvcSmplStartTime"),
        ("FRSLD-MIB", "frsldPvcSmplEndTime"))
)
if mibBuilder.loadTexts:
    frsldPvcSampleGeneralGroup.setStatus("current")

frsldCapabilitiesGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 95, 3, 1, 15)
)
frsldCapabilitiesGroup.setObjects(
      *(("FRSLD-MIB", "frsldPvcCtrlWriteCaps"),
        ("FRSLD-MIB", "frsldSmplCtrlWriteCaps"),
        ("FRSLD-MIB", "frsldRPCaps"),
        ("FRSLD-MIB", "frsldMaxPvcCtrls"),
        ("FRSLD-MIB", "frsldNumPvcCtrls"),
        ("FRSLD-MIB", "frsldMaxSmplCtrls"),
        ("FRSLD-MIB", "frsldNumSmplCtrls"))
)
if mibBuilder.loadTexts:
    frsldCapabilitiesGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

frsldCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 95, 3, 2, 1)
)
if mibBuilder.loadTexts:
    frsldCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FRSLD-MIB",
    **{"FrsldTxRP": FrsldTxRP,
       "FrsldRxRP": FrsldRxRP,
       "frsldMIB": frsldMIB,
       "frsldObjects": frsldObjects,
       "frsldPvcCtrlTable": frsldPvcCtrlTable,
       "frsldPvcCtrlEntry": frsldPvcCtrlEntry,
       "frsldPvcCtrlDlci": frsldPvcCtrlDlci,
       "frsldPvcCtrlTransmitRP": frsldPvcCtrlTransmitRP,
       "frsldPvcCtrlReceiveRP": frsldPvcCtrlReceiveRP,
       "frsldPvcCtrlStatus": frsldPvcCtrlStatus,
       "frsldPvcCtrlPacketFreq": frsldPvcCtrlPacketFreq,
       "frsldPvcCtrlDelayFrSize": frsldPvcCtrlDelayFrSize,
       "frsldPvcCtrlDelayType": frsldPvcCtrlDelayType,
       "frsldPvcCtrlDelayTimeOut": frsldPvcCtrlDelayTimeOut,
       "frsldPvcCtrlPurge": frsldPvcCtrlPurge,
       "frsldPvcCtrlDeleteOnPurge": frsldPvcCtrlDeleteOnPurge,
       "frsldPvcCtrlLastPurgeTime": frsldPvcCtrlLastPurgeTime,
       "frsldSmplCtrlTable": frsldSmplCtrlTable,
       "frsldSmplCtrlEntry": frsldSmplCtrlEntry,
       "frsldSmplCtrlIdx": frsldSmplCtrlIdx,
       "frsldSmplCtrlStatus": frsldSmplCtrlStatus,
       "frsldSmplCtrlColPeriod": frsldSmplCtrlColPeriod,
       "frsldSmplCtrlBuckets": frsldSmplCtrlBuckets,
       "frsldSmplCtrlBucketsGranted": frsldSmplCtrlBucketsGranted,
       "frsldPvcDataTable": frsldPvcDataTable,
       "frsldPvcDataEntry": frsldPvcDataEntry,
       "frsldPvcDataMissedPolls": frsldPvcDataMissedPolls,
       "frsldPvcDataFrDeliveredC": frsldPvcDataFrDeliveredC,
       "frsldPvcDataFrDeliveredE": frsldPvcDataFrDeliveredE,
       "frsldPvcDataFrOfferedC": frsldPvcDataFrOfferedC,
       "frsldPvcDataFrOfferedE": frsldPvcDataFrOfferedE,
       "frsldPvcDataDataDeliveredC": frsldPvcDataDataDeliveredC,
       "frsldPvcDataDataDeliveredE": frsldPvcDataDataDeliveredE,
       "frsldPvcDataDataOfferedC": frsldPvcDataDataOfferedC,
       "frsldPvcDataDataOfferedE": frsldPvcDataDataOfferedE,
       "frsldPvcDataHCFrDeliveredC": frsldPvcDataHCFrDeliveredC,
       "frsldPvcDataHCFrDeliveredE": frsldPvcDataHCFrDeliveredE,
       "frsldPvcDataHCFrOfferedC": frsldPvcDataHCFrOfferedC,
       "frsldPvcDataHCFrOfferedE": frsldPvcDataHCFrOfferedE,
       "frsldPvcDataHCDataDeliveredC": frsldPvcDataHCDataDeliveredC,
       "frsldPvcDataHCDataDeliveredE": frsldPvcDataHCDataDeliveredE,
       "frsldPvcDataHCDataOfferedC": frsldPvcDataHCDataOfferedC,
       "frsldPvcDataHCDataOfferedE": frsldPvcDataHCDataOfferedE,
       "frsldPvcDataUnavailableTime": frsldPvcDataUnavailableTime,
       "frsldPvcDataUnavailables": frsldPvcDataUnavailables,
       "frsldPvcSampleTable": frsldPvcSampleTable,
       "frsldPvcSampleEntry": frsldPvcSampleEntry,
       "frsldPvcSmplIdx": frsldPvcSmplIdx,
       "frsldPvcSmplDelayMin": frsldPvcSmplDelayMin,
       "frsldPvcSmplDelayMax": frsldPvcSmplDelayMax,
       "frsldPvcSmplDelayAvg": frsldPvcSmplDelayAvg,
       "frsldPvcSmplMissedPolls": frsldPvcSmplMissedPolls,
       "frsldPvcSmplFrDeliveredC": frsldPvcSmplFrDeliveredC,
       "frsldPvcSmplFrDeliveredE": frsldPvcSmplFrDeliveredE,
       "frsldPvcSmplFrOfferedC": frsldPvcSmplFrOfferedC,
       "frsldPvcSmplFrOfferedE": frsldPvcSmplFrOfferedE,
       "frsldPvcSmplDataDeliveredC": frsldPvcSmplDataDeliveredC,
       "frsldPvcSmplDataDeliveredE": frsldPvcSmplDataDeliveredE,
       "frsldPvcSmplDataOfferedC": frsldPvcSmplDataOfferedC,
       "frsldPvcSmplDataOfferedE": frsldPvcSmplDataOfferedE,
       "frsldPvcSmplHCFrDeliveredC": frsldPvcSmplHCFrDeliveredC,
       "frsldPvcSmplHCFrDeliveredE": frsldPvcSmplHCFrDeliveredE,
       "frsldPvcSmplHCFrOfferedC": frsldPvcSmplHCFrOfferedC,
       "frsldPvcSmplHCFrOfferedE": frsldPvcSmplHCFrOfferedE,
       "frsldPvcSmplHCDataDeliveredC": frsldPvcSmplHCDataDeliveredC,
       "frsldPvcSmplHCDataDeliveredE": frsldPvcSmplHCDataDeliveredE,
       "frsldPvcSmplHCDataOfferedC": frsldPvcSmplHCDataOfferedC,
       "frsldPvcSmplHCDataOfferedE": frsldPvcSmplHCDataOfferedE,
       "frsldPvcSmplUnavailableTime": frsldPvcSmplUnavailableTime,
       "frsldPvcSmplUnavailables": frsldPvcSmplUnavailables,
       "frsldPvcSmplStartTime": frsldPvcSmplStartTime,
       "frsldPvcSmplEndTime": frsldPvcSmplEndTime,
       "frsldCapabilities": frsldCapabilities,
       "frsldPvcCtrlWriteCaps": frsldPvcCtrlWriteCaps,
       "frsldSmplCtrlWriteCaps": frsldSmplCtrlWriteCaps,
       "frsldRPCaps": frsldRPCaps,
       "frsldMaxPvcCtrls": frsldMaxPvcCtrls,
       "frsldNumPvcCtrls": frsldNumPvcCtrls,
       "frsldMaxSmplCtrls": frsldMaxSmplCtrls,
       "frsldNumSmplCtrls": frsldNumSmplCtrls,
       "frsldConformance": frsldConformance,
       "frsldMIBGroups": frsldMIBGroups,
       "frsldPvcReqCtrlGroup": frsldPvcReqCtrlGroup,
       "frsldPvcPacketGroup": frsldPvcPacketGroup,
       "frsldPvcDelayCtrlGroup": frsldPvcDelayCtrlGroup,
       "frsldPvcSampleCtrlGroup": frsldPvcSampleCtrlGroup,
       "frsldPvcReqDataGroup": frsldPvcReqDataGroup,
       "frsldPvcDelayDataGroup": frsldPvcDelayDataGroup,
       "frsldPvcHCFrameDataGroup": frsldPvcHCFrameDataGroup,
       "frsldPvcHCOctetDataGroup": frsldPvcHCOctetDataGroup,
       "frsldPvcSampleDelayGroup": frsldPvcSampleDelayGroup,
       "frsldPvcSampleDataGroup": frsldPvcSampleDataGroup,
       "frsldPvcSampleHCFrameGroup": frsldPvcSampleHCFrameGroup,
       "frsldPvcSampleHCDataGroup": frsldPvcSampleHCDataGroup,
       "frsldPvcSampleAvailGroup": frsldPvcSampleAvailGroup,
       "frsldPvcSampleGeneralGroup": frsldPvcSampleGeneralGroup,
       "frsldCapabilitiesGroup": frsldCapabilitiesGroup,
       "frsldMIBCompliances": frsldMIBCompliances,
       "frsldCompliance": frsldCompliance}
)
