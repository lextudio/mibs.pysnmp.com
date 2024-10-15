# SNMP MIB module (RIVERSTONE-LFAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RIVERSTONE-LFAP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:47:47 2024
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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(riverstoneMibs,) = mibBuilder.importSymbols(
    "RIVERSTONE-SMI-MIB",
    "riverstoneMibs")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

rsLfapMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 2, 19)
)
rsLfapMIB.setRevisions(
        ("2001-06-15 00:00",
         "2001-06-08 00:00",
         "2001-05-07 00:00",
         "2001-05-01 00:00",
         "2001-03-03 00:00",
         "2001-02-12 00:00",
         "2001-02-11 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class RSLfapErrorCode(Integer32, TextualConvention):
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
        *(("errorInConfig", 2),
          ("errorNoServer", 4),
          ("resourceExhausted", 3),
          ("unknown", 1))
    )



class RsLfapServerInst(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
        ValueRangeConstraint(0, 0),
    )



class RsTaskPriority(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("low", 3),
          ("medium", 2))
    )



class RSOperState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("lfapDegraded", 4),
          ("lfapError", 5),
          ("lfapNormal", 2),
          ("lfapTest", 3),
          ("unknown", 1))
    )



# MIB Managed Objects in the order of their OIDs

_RsLfapMIBObjects_ObjectIdentity = ObjectIdentity
rsLfapMIBObjects = _RsLfapMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 2, 19, 1)
)
_RsLfapAgentState_ObjectIdentity = ObjectIdentity
rsLfapAgentState = _RsLfapAgentState_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 2, 19, 1, 1)
)


class _RsLfapCapabilities_Type(Bits):
    """Custom type rsLfapCapabilities based on Bits"""
    namedValues = NamedValues(
        *(("rsLfapV4", 0),
          ("rsLfapV5", 1))
    )

_RsLfapCapabilities_Type.__name__ = "Bits"
_RsLfapCapabilities_Object = MibScalar
rsLfapCapabilities = _RsLfapCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 19, 1, 1, 1),
    _RsLfapCapabilities_Type()
)
rsLfapCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsLfapCapabilities.setStatus("current")
_RsLfapAdminState_Type = TruthValue
_RsLfapAdminState_Object = MibScalar
rsLfapAdminState = _RsLfapAdminState_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 19, 1, 1, 2),
    _RsLfapAdminState_Type()
)
rsLfapAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsLfapAdminState.setStatus("current")
_RsLfapOperState_Type = RSOperState
_RsLfapOperState_Object = MibScalar
rsLfapOperState = _RsLfapOperState_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 19, 1, 1, 3),
    _RsLfapOperState_Type()
)
rsLfapOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsLfapOperState.setStatus("current")
_RsLfapLastError_Type = RSLfapErrorCode
_RsLfapLastError_Object = MibScalar
rsLfapLastError = _RsLfapLastError_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 19, 1, 1, 4),
    _RsLfapLastError_Type()
)
rsLfapLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsLfapLastError.setStatus("current")
_RsLfapLastErrorReason_Type = SnmpAdminString
_RsLfapLastErrorReason_Object = MibScalar
rsLfapLastErrorReason = _RsLfapLastErrorReason_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 19, 1, 1, 5),
    _RsLfapLastErrorReason_Type()
)
rsLfapLastErrorReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsLfapLastErrorReason.setStatus("current")
_RsLfapActiveServer_Type = RsLfapServerInst
_RsLfapActiveServer_Object = MibScalar
rsLfapActiveServer = _RsLfapActiveServer_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 19, 1, 1, 6),
    _RsLfapActiveServer_Type()
)
rsLfapActiveServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsLfapActiveServer.setStatus("current")
_RsLfapAgentCfg_ObjectIdentity = ObjectIdentity
rsLfapAgentCfg = _RsLfapAgentCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 2, 19, 1, 2)
)


class _RsLfapPollInterval_Type(Integer32):
    """Custom type rsLfapPollInterval based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1440),
    )


_RsLfapPollInterval_Type.__name__ = "Integer32"
_RsLfapPollInterval_Object = MibScalar
rsLfapPollInterval = _RsLfapPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 19, 1, 2, 1),
    _RsLfapPollInterval_Type()
)
rsLfapPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsLfapPollInterval.setStatus("current")
if mibBuilder.loadTexts:
    rsLfapPollInterval.setUnits("minutes")


class _RsLfapBatchSize_Type(Integer32):
    """Custom type rsLfapBatchSize based on Integer32"""
    defaultValue = 32

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000),
    )


_RsLfapBatchSize_Type.__name__ = "Integer32"
_RsLfapBatchSize_Object = MibScalar
rsLfapBatchSize = _RsLfapBatchSize_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 19, 1, 2, 2),
    _RsLfapBatchSize_Type()
)
rsLfapBatchSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsLfapBatchSize.setStatus("current")
if mibBuilder.loadTexts:
    rsLfapBatchSize.setUnits("records")


class _RsLfapBatchInterval_Type(Integer32):
    """Custom type rsLfapBatchInterval based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000),
    )


_RsLfapBatchInterval_Type.__name__ = "Integer32"
_RsLfapBatchInterval_Object = MibScalar
rsLfapBatchInterval = _RsLfapBatchInterval_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 19, 1, 2, 3),
    _RsLfapBatchInterval_Type()
)
rsLfapBatchInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsLfapBatchInterval.setStatus("current")
if mibBuilder.loadTexts:
    rsLfapBatchInterval.setUnits("seconds")


class _RsLfapLostContactInterval_Type(Integer32):
    """Custom type rsLfapLostContactInterval based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 2000),
    )


_RsLfapLostContactInterval_Type.__name__ = "Integer32"
_RsLfapLostContactInterval_Object = MibScalar
rsLfapLostContactInterval = _RsLfapLostContactInterval_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 19, 1, 2, 4),
    _RsLfapLostContactInterval_Type()
)
rsLfapLostContactInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsLfapLostContactInterval.setStatus("current")
if mibBuilder.loadTexts:
    rsLfapLostContactInterval.setUnits("seconds")


class _RsLfapServerRetryInterval_Type(Integer32):
    """Custom type rsLfapServerRetryInterval based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000),
    )


_RsLfapServerRetryInterval_Type.__name__ = "Integer32"
_RsLfapServerRetryInterval_Object = MibScalar
rsLfapServerRetryInterval = _RsLfapServerRetryInterval_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 19, 1, 2, 5),
    _RsLfapServerRetryInterval_Type()
)
rsLfapServerRetryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsLfapServerRetryInterval.setStatus("current")
if mibBuilder.loadTexts:
    rsLfapServerRetryInterval.setUnits("seconds")


class _RsLfapMaxTxQueueSize_Type(Integer32):
    """Custom type rsLfapMaxTxQueueSize based on Integer32"""
    defaultValue = 50000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 2000000),
    )


_RsLfapMaxTxQueueSize_Type.__name__ = "Integer32"
_RsLfapMaxTxQueueSize_Object = MibScalar
rsLfapMaxTxQueueSize = _RsLfapMaxTxQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 19, 1, 2, 6),
    _RsLfapMaxTxQueueSize_Type()
)
rsLfapMaxTxQueueSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsLfapMaxTxQueueSize.setStatus("current")
if mibBuilder.loadTexts:
    rsLfapMaxTxQueueSize.setUnits("message count")
_RsLfapTaskPriority_Type = RsTaskPriority
_RsLfapTaskPriority_Object = MibScalar
rsLfapTaskPriority = _RsLfapTaskPriority_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 19, 1, 2, 7),
    _RsLfapTaskPriority_Type()
)
rsLfapTaskPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsLfapTaskPriority.setStatus("current")
if mibBuilder.loadTexts:
    rsLfapTaskPriority.setUnits("seconds")
_RsLfapServerCfg_ObjectIdentity = ObjectIdentity
rsLfapServerCfg = _RsLfapServerCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 2, 19, 1, 3)
)
_RsLfapServerStaticLastChanged_Type = TimeTicks
_RsLfapServerStaticLastChanged_Object = MibScalar
rsLfapServerStaticLastChanged = _RsLfapServerStaticLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 19, 1, 3, 2),
    _RsLfapServerStaticLastChanged_Type()
)
rsLfapServerStaticLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsLfapServerStaticLastChanged.setStatus("current")
_RsLfapServerStaticTable_Object = MibTable
rsLfapServerStaticTable = _RsLfapServerStaticTable_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 19, 1, 3, 3)
)
if mibBuilder.loadTexts:
    rsLfapServerStaticTable.setStatus("current")
_RsLfapServerStaticEntry_Object = MibTableRow
rsLfapServerStaticEntry = _RsLfapServerStaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 19, 1, 3, 3, 1)
)
rsLfapServerStaticEntry.setIndexNames(
    (0, "RIVERSTONE-LFAP-MIB", "rsLfapServerStaticIndex"),
)
if mibBuilder.loadTexts:
    rsLfapServerStaticEntry.setStatus("current")
_RsLfapServerStaticIndex_Type = RsLfapServerInst
_RsLfapServerStaticIndex_Object = MibTableColumn
rsLfapServerStaticIndex = _RsLfapServerStaticIndex_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 19, 1, 3, 3, 1, 1),
    _RsLfapServerStaticIndex_Type()
)
rsLfapServerStaticIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rsLfapServerStaticIndex.setStatus("current")
_RsLfapServerStaticAddressType_Type = InetAddressType
_RsLfapServerStaticAddressType_Object = MibTableColumn
rsLfapServerStaticAddressType = _RsLfapServerStaticAddressType_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 19, 1, 3, 3, 1, 2),
    _RsLfapServerStaticAddressType_Type()
)
rsLfapServerStaticAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsLfapServerStaticAddressType.setStatus("current")
_RsLfapServerStaticAddress_Type = InetAddress
_RsLfapServerStaticAddress_Object = MibTableColumn
rsLfapServerStaticAddress = _RsLfapServerStaticAddress_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 19, 1, 3, 3, 1, 3),
    _RsLfapServerStaticAddress_Type()
)
rsLfapServerStaticAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsLfapServerStaticAddress.setStatus("current")
_RsLfapServerStaticStatus_Type = RowStatus
_RsLfapServerStaticStatus_Object = MibTableColumn
rsLfapServerStaticStatus = _RsLfapServerStaticStatus_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 19, 1, 3, 3, 1, 4),
    _RsLfapServerStaticStatus_Type()
)
rsLfapServerStaticStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsLfapServerStaticStatus.setStatus("current")
_RsLfapStats_ObjectIdentity = ObjectIdentity
rsLfapStats = _RsLfapStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 2, 19, 1, 4)
)
_RsLfapStatsTable_Object = MibTable
rsLfapStatsTable = _RsLfapStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 19, 1, 4, 1)
)
if mibBuilder.loadTexts:
    rsLfapStatsTable.setStatus("current")
_RsLfapStatsEntry_Object = MibTableRow
rsLfapStatsEntry = _RsLfapStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 19, 1, 4, 1, 1)
)
rsLfapStatsEntry.setIndexNames(
    (0, "RIVERSTONE-LFAP-MIB", "rsLfapServerStaticIndex"),
)
if mibBuilder.loadTexts:
    rsLfapStatsEntry.setStatus("current")
_RsLfapStatsSessionUp_Type = TruthValue
_RsLfapStatsSessionUp_Object = MibTableColumn
rsLfapStatsSessionUp = _RsLfapStatsSessionUp_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 19, 1, 4, 1, 1, 1),
    _RsLfapStatsSessionUp_Type()
)
rsLfapStatsSessionUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsLfapStatsSessionUp.setStatus("current")
_RsLfapStatsSessionChangedAt_Type = TimeTicks
_RsLfapStatsSessionChangedAt_Object = MibTableColumn
rsLfapStatsSessionChangedAt = _RsLfapStatsSessionChangedAt_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 19, 1, 4, 1, 1, 2),
    _RsLfapStatsSessionChangedAt_Type()
)
rsLfapStatsSessionChangedAt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsLfapStatsSessionChangedAt.setStatus("current")
_RsLfapStatsTcpConnects_Type = Counter32
_RsLfapStatsTcpConnects_Object = MibTableColumn
rsLfapStatsTcpConnects = _RsLfapStatsTcpConnects_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 19, 1, 4, 1, 1, 3),
    _RsLfapStatsTcpConnects_Type()
)
rsLfapStatsTcpConnects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsLfapStatsTcpConnects.setStatus("current")
_RsLfapStatsTcpConnectFails_Type = Counter32
_RsLfapStatsTcpConnectFails_Object = MibTableColumn
rsLfapStatsTcpConnectFails = _RsLfapStatsTcpConnectFails_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 19, 1, 4, 1, 1, 4),
    _RsLfapStatsTcpConnectFails_Type()
)
rsLfapStatsTcpConnectFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsLfapStatsTcpConnectFails.setStatus("current")
_RsLfapStatsTxVRs_Type = Counter32
_RsLfapStatsTxVRs_Object = MibTableColumn
rsLfapStatsTxVRs = _RsLfapStatsTxVRs_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 19, 1, 4, 1, 1, 5),
    _RsLfapStatsTxVRs_Type()
)
rsLfapStatsTxVRs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsLfapStatsTxVRs.setStatus("current")
_RsLfapStatsTxVRAs_Type = Counter32
_RsLfapStatsTxVRAs_Object = MibTableColumn
rsLfapStatsTxVRAs = _RsLfapStatsTxVRAs_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 19, 1, 4, 1, 1, 6),
    _RsLfapStatsTxVRAs_Type()
)
rsLfapStatsTxVRAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsLfapStatsTxVRAs.setStatus("current")
_RsLfapStatsTxFARs_Type = Counter32
_RsLfapStatsTxFARs_Object = MibTableColumn
rsLfapStatsTxFARs = _RsLfapStatsTxFARs_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 19, 1, 4, 1, 1, 7),
    _RsLfapStatsTxFARs_Type()
)
rsLfapStatsTxFARs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsLfapStatsTxFARs.setStatus("current")
_RsLfapStatsTxFUNs_Type = Counter32
_RsLfapStatsTxFUNs_Object = MibTableColumn
rsLfapStatsTxFUNs = _RsLfapStatsTxFUNs_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 19, 1, 4, 1, 1, 8),
    _RsLfapStatsTxFUNs_Type()
)
rsLfapStatsTxFUNs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsLfapStatsTxFUNs.setStatus("current")
_RsLfapStatsTxARs_Type = Counter32
_RsLfapStatsTxARs_Object = MibTableColumn
rsLfapStatsTxARs = _RsLfapStatsTxARs_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 19, 1, 4, 1, 1, 9),
    _RsLfapStatsTxARs_Type()
)
rsLfapStatsTxARs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsLfapStatsTxARs.setStatus("current")
_RsLfapStatsTxARAs_Type = Counter32
_RsLfapStatsTxARAs_Object = MibTableColumn
rsLfapStatsTxARAs = _RsLfapStatsTxARAs_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 19, 1, 4, 1, 1, 10),
    _RsLfapStatsTxARAs_Type()
)
rsLfapStatsTxARAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsLfapStatsTxARAs.setStatus("current")
_RsLfapStatsMsgsInTxQueue_Type = Integer32
_RsLfapStatsMsgsInTxQueue_Object = MibTableColumn
rsLfapStatsMsgsInTxQueue = _RsLfapStatsMsgsInTxQueue_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 19, 1, 4, 1, 1, 11),
    _RsLfapStatsMsgsInTxQueue_Type()
)
rsLfapStatsMsgsInTxQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsLfapStatsMsgsInTxQueue.setStatus("current")
_RsLfapStatsDropsInTxQueue_Type = Counter32
_RsLfapStatsDropsInTxQueue_Object = MibTableColumn
rsLfapStatsDropsInTxQueue = _RsLfapStatsDropsInTxQueue_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 19, 1, 4, 1, 1, 12),
    _RsLfapStatsDropsInTxQueue_Type()
)
rsLfapStatsDropsInTxQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsLfapStatsDropsInTxQueue.setStatus("current")
_RsLfapStatsDropsInTxQueueWhenUp_Type = Counter32
_RsLfapStatsDropsInTxQueueWhenUp_Object = MibTableColumn
rsLfapStatsDropsInTxQueueWhenUp = _RsLfapStatsDropsInTxQueueWhenUp_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 19, 1, 4, 1, 1, 13),
    _RsLfapStatsDropsInTxQueueWhenUp_Type()
)
rsLfapStatsDropsInTxQueueWhenUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsLfapStatsDropsInTxQueueWhenUp.setStatus("current")
_RsLfapStatsRxVRs_Type = Counter32
_RsLfapStatsRxVRs_Object = MibTableColumn
rsLfapStatsRxVRs = _RsLfapStatsRxVRs_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 19, 1, 4, 1, 1, 14),
    _RsLfapStatsRxVRs_Type()
)
rsLfapStatsRxVRs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsLfapStatsRxVRs.setStatus("current")
_RsLfapStatsRxVRAs_Type = Counter32
_RsLfapStatsRxVRAs_Object = MibTableColumn
rsLfapStatsRxVRAs = _RsLfapStatsRxVRAs_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 19, 1, 4, 1, 1, 15),
    _RsLfapStatsRxVRAs_Type()
)
rsLfapStatsRxVRAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsLfapStatsRxVRAs.setStatus("current")
_RsLfapStatsRxFARs_Type = Counter32
_RsLfapStatsRxFARs_Object = MibTableColumn
rsLfapStatsRxFARs = _RsLfapStatsRxFARs_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 19, 1, 4, 1, 1, 16),
    _RsLfapStatsRxFARs_Type()
)
rsLfapStatsRxFARs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsLfapStatsRxFARs.setStatus("current")
_RsLfapStatsRxFUNs_Type = Counter32
_RsLfapStatsRxFUNs_Object = MibTableColumn
rsLfapStatsRxFUNs = _RsLfapStatsRxFUNs_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 19, 1, 4, 1, 1, 17),
    _RsLfapStatsRxFUNs_Type()
)
rsLfapStatsRxFUNs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsLfapStatsRxFUNs.setStatus("current")
_RsLfapStatsRxARs_Type = Counter32
_RsLfapStatsRxARs_Object = MibTableColumn
rsLfapStatsRxARs = _RsLfapStatsRxARs_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 19, 1, 4, 1, 1, 18),
    _RsLfapStatsRxARs_Type()
)
rsLfapStatsRxARs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsLfapStatsRxARs.setStatus("current")
_RsLfapStatsRxARAs_Type = Counter32
_RsLfapStatsRxARAs_Object = MibTableColumn
rsLfapStatsRxARAs = _RsLfapStatsRxARAs_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 19, 1, 4, 1, 1, 19),
    _RsLfapStatsRxARAs_Type()
)
rsLfapStatsRxARAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsLfapStatsRxARAs.setStatus("current")
_RsLfapStatsMsgsInRxQueue_Type = Integer32
_RsLfapStatsMsgsInRxQueue_Object = MibTableColumn
rsLfapStatsMsgsInRxQueue = _RsLfapStatsMsgsInRxQueue_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 19, 1, 4, 1, 1, 20),
    _RsLfapStatsMsgsInRxQueue_Type()
)
rsLfapStatsMsgsInRxQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsLfapStatsMsgsInRxQueue.setStatus("current")
_RsLfapStatsInvalidMsgsRx_Type = Counter32
_RsLfapStatsInvalidMsgsRx_Object = MibTableColumn
rsLfapStatsInvalidMsgsRx = _RsLfapStatsInvalidMsgsRx_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 19, 1, 4, 1, 1, 21),
    _RsLfapStatsInvalidMsgsRx_Type()
)
rsLfapStatsInvalidMsgsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsLfapStatsInvalidMsgsRx.setStatus("current")
_RsLfapStatsMsgsUnknownRx_Type = Counter32
_RsLfapStatsMsgsUnknownRx_Object = MibTableColumn
rsLfapStatsMsgsUnknownRx = _RsLfapStatsMsgsUnknownRx_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 19, 1, 4, 1, 1, 22),
    _RsLfapStatsMsgsUnknownRx_Type()
)
rsLfapStatsMsgsUnknownRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsLfapStatsMsgsUnknownRx.setStatus("current")
_RsLfapStatsTxLostPackets_Type = Counter64
_RsLfapStatsTxLostPackets_Object = MibTableColumn
rsLfapStatsTxLostPackets = _RsLfapStatsTxLostPackets_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 19, 1, 4, 1, 1, 23),
    _RsLfapStatsTxLostPackets_Type()
)
rsLfapStatsTxLostPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsLfapStatsTxLostPackets.setStatus("current")
_RsLfapStatsTxLostOctets_Type = Counter64
_RsLfapStatsTxLostOctets_Object = MibTableColumn
rsLfapStatsTxLostOctets = _RsLfapStatsTxLostOctets_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 19, 1, 4, 1, 1, 24),
    _RsLfapStatsTxLostOctets_Type()
)
rsLfapStatsTxLostOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsLfapStatsTxLostOctets.setStatus("current")
_RsLfapStatsLostAt_Type = TimeTicks
_RsLfapStatsLostAt_Object = MibTableColumn
rsLfapStatsLostAt = _RsLfapStatsLostAt_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 19, 1, 4, 1, 1, 25),
    _RsLfapStatsLostAt_Type()
)
rsLfapStatsLostAt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsLfapStatsLostAt.setStatus("current")
_RsLfapStatsActiveFlows_Type = Counter32
_RsLfapStatsActiveFlows_Object = MibTableColumn
rsLfapStatsActiveFlows = _RsLfapStatsActiveFlows_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 19, 1, 4, 1, 1, 26),
    _RsLfapStatsActiveFlows_Type()
)
rsLfapStatsActiveFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsLfapStatsActiveFlows.setStatus("current")
_RsLfapStatsFlowRate_Type = Gauge32
_RsLfapStatsFlowRate_Object = MibTableColumn
rsLfapStatsFlowRate = _RsLfapStatsFlowRate_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 19, 1, 4, 1, 1, 27),
    _RsLfapStatsFlowRate_Type()
)
rsLfapStatsFlowRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsLfapStatsFlowRate.setStatus("current")
_RsLfapStatsActiveFlowsPeak_Type = Gauge32
_RsLfapStatsActiveFlowsPeak_Object = MibTableColumn
rsLfapStatsActiveFlowsPeak = _RsLfapStatsActiveFlowsPeak_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 19, 1, 4, 1, 1, 28),
    _RsLfapStatsActiveFlowsPeak_Type()
)
rsLfapStatsActiveFlowsPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsLfapStatsActiveFlowsPeak.setStatus("current")
_RsLfapStatsMsgsInTxQueuePeak_Type = Gauge32
_RsLfapStatsMsgsInTxQueuePeak_Object = MibTableColumn
rsLfapStatsMsgsInTxQueuePeak = _RsLfapStatsMsgsInTxQueuePeak_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 19, 1, 4, 1, 1, 29),
    _RsLfapStatsMsgsInTxQueuePeak_Type()
)
rsLfapStatsMsgsInTxQueuePeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsLfapStatsMsgsInTxQueuePeak.setStatus("current")
_RsLfapStatsFlowsPeakTime_Type = TimeTicks
_RsLfapStatsFlowsPeakTime_Object = MibTableColumn
rsLfapStatsFlowsPeakTime = _RsLfapStatsFlowsPeakTime_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 19, 1, 4, 1, 1, 30),
    _RsLfapStatsFlowsPeakTime_Type()
)
rsLfapStatsFlowsPeakTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsLfapStatsFlowsPeakTime.setStatus("current")
_RsLfapDiag_ObjectIdentity = ObjectIdentity
rsLfapDiag = _RsLfapDiag_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 2, 19, 1, 5)
)
_RsRunLfapSelfTest_Type = TruthValue
_RsRunLfapSelfTest_Object = MibScalar
rsRunLfapSelfTest = _RsRunLfapSelfTest_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 19, 1, 5, 1),
    _RsRunLfapSelfTest_Type()
)
rsRunLfapSelfTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsRunLfapSelfTest.setStatus("current")
_RsLfapMIBEvents_ObjectIdentity = ObjectIdentity
rsLfapMIBEvents = _RsLfapMIBEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 2, 19, 2)
)
_RsLfapMIBEventsPrefix_ObjectIdentity = ObjectIdentity
rsLfapMIBEventsPrefix = _RsLfapMIBEventsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 2, 19, 2, 0)
)
_RsLfapConformance_ObjectIdentity = ObjectIdentity
rsLfapConformance = _RsLfapConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 2, 19, 3)
)
_RsLfapCompliances_ObjectIdentity = ObjectIdentity
rsLfapCompliances = _RsLfapCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 2, 19, 3, 1)
)
_RsLfapGroups_ObjectIdentity = ObjectIdentity
rsLfapGroups = _RsLfapGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 2, 19, 3, 2)
)

# Managed Objects groups

rsLfapAgentStateGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5567, 2, 19, 3, 2, 1)
)
rsLfapAgentStateGroup.setObjects(
      *(("RIVERSTONE-LFAP-MIB", "rsLfapCapabilities"),
        ("RIVERSTONE-LFAP-MIB", "rsLfapAdminState"),
        ("RIVERSTONE-LFAP-MIB", "rsLfapOperState"),
        ("RIVERSTONE-LFAP-MIB", "rsLfapLastError"),
        ("RIVERSTONE-LFAP-MIB", "rsLfapLastErrorReason"),
        ("RIVERSTONE-LFAP-MIB", "rsLfapActiveServer"))
)
if mibBuilder.loadTexts:
    rsLfapAgentStateGroup.setStatus("current")

rsLfapAgentCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5567, 2, 19, 3, 2, 2)
)
rsLfapAgentCfgGroup.setObjects(
      *(("RIVERSTONE-LFAP-MIB", "rsLfapPollInterval"),
        ("RIVERSTONE-LFAP-MIB", "rsLfapBatchSize"),
        ("RIVERSTONE-LFAP-MIB", "rsLfapBatchInterval"),
        ("RIVERSTONE-LFAP-MIB", "rsLfapLostContactInterval"),
        ("RIVERSTONE-LFAP-MIB", "rsLfapServerRetryInterval"),
        ("RIVERSTONE-LFAP-MIB", "rsLfapMaxTxQueueSize"),
        ("RIVERSTONE-LFAP-MIB", "rsLfapTaskPriority"))
)
if mibBuilder.loadTexts:
    rsLfapAgentCfgGroup.setStatus("current")

rsLfapServerStaticGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5567, 2, 19, 3, 2, 3)
)
rsLfapServerStaticGroup.setObjects(
      *(("RIVERSTONE-LFAP-MIB", "rsLfapServerStaticLastChanged"),
        ("RIVERSTONE-LFAP-MIB", "rsLfapServerStaticAddressType"),
        ("RIVERSTONE-LFAP-MIB", "rsLfapServerStaticAddress"),
        ("RIVERSTONE-LFAP-MIB", "rsLfapServerStaticStatus"))
)
if mibBuilder.loadTexts:
    rsLfapServerStaticGroup.setStatus("current")

rsLfapStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5567, 2, 19, 3, 2, 4)
)
rsLfapStatsGroup.setObjects(
      *(("RIVERSTONE-LFAP-MIB", "rsLfapStatsSessionUp"),
        ("RIVERSTONE-LFAP-MIB", "rsLfapStatsSessionChangedAt"),
        ("RIVERSTONE-LFAP-MIB", "rsLfapStatsTcpConnects"),
        ("RIVERSTONE-LFAP-MIB", "rsLfapStatsTcpConnectFails"),
        ("RIVERSTONE-LFAP-MIB", "rsLfapStatsTxVRs"),
        ("RIVERSTONE-LFAP-MIB", "rsLfapStatsTxVRAs"),
        ("RIVERSTONE-LFAP-MIB", "rsLfapStatsTxFARs"),
        ("RIVERSTONE-LFAP-MIB", "rsLfapStatsTxFUNs"),
        ("RIVERSTONE-LFAP-MIB", "rsLfapStatsTxARs"),
        ("RIVERSTONE-LFAP-MIB", "rsLfapStatsTxARAs"),
        ("RIVERSTONE-LFAP-MIB", "rsLfapStatsMsgsInTxQueue"),
        ("RIVERSTONE-LFAP-MIB", "rsLfapStatsDropsInTxQueue"),
        ("RIVERSTONE-LFAP-MIB", "rsLfapStatsDropsInTxQueueWhenUp"),
        ("RIVERSTONE-LFAP-MIB", "rsLfapStatsRxVRs"),
        ("RIVERSTONE-LFAP-MIB", "rsLfapStatsRxVRAs"),
        ("RIVERSTONE-LFAP-MIB", "rsLfapStatsRxFARs"),
        ("RIVERSTONE-LFAP-MIB", "rsLfapStatsRxFUNs"),
        ("RIVERSTONE-LFAP-MIB", "rsLfapStatsRxARs"),
        ("RIVERSTONE-LFAP-MIB", "rsLfapStatsRxARAs"),
        ("RIVERSTONE-LFAP-MIB", "rsLfapStatsMsgsInRxQueue"),
        ("RIVERSTONE-LFAP-MIB", "rsLfapStatsInvalidMsgsRx"),
        ("RIVERSTONE-LFAP-MIB", "rsLfapStatsMsgsUnknownRx"),
        ("RIVERSTONE-LFAP-MIB", "rsLfapStatsTxLostPackets"),
        ("RIVERSTONE-LFAP-MIB", "rsLfapStatsTxLostOctets"),
        ("RIVERSTONE-LFAP-MIB", "rsLfapStatsLostAt"),
        ("RIVERSTONE-LFAP-MIB", "rsLfapStatsActiveFlows"),
        ("RIVERSTONE-LFAP-MIB", "rsLfapStatsFlowRate"),
        ("RIVERSTONE-LFAP-MIB", "rsLfapStatsActiveFlowsPeak"),
        ("RIVERSTONE-LFAP-MIB", "rsLfapStatsMsgsInTxQueuePeak"),
        ("RIVERSTONE-LFAP-MIB", "rsLfapStatsFlowsPeakTime"))
)
if mibBuilder.loadTexts:
    rsLfapStatsGroup.setStatus("current")

rsLfapDiagGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5567, 2, 19, 3, 2, 5)
)
rsLfapDiagGroup.setObjects(
    ("RIVERSTONE-LFAP-MIB", "rsRunLfapSelfTest")
)
if mibBuilder.loadTexts:
    rsLfapDiagGroup.setStatus("current")


# Notification objects

rsLfapNoServer = NotificationType(
    (1, 3, 6, 1, 4, 1, 5567, 2, 19, 2, 0, 1)
)
rsLfapNoServer.setObjects(
      *(("RIVERSTONE-LFAP-MIB", "rsLfapStatsSessionChangedAt"),
        ("RIVERSTONE-LFAP-MIB", "rsLfapStatsTcpConnectFails"))
)
if mibBuilder.loadTexts:
    rsLfapNoServer.setStatus(
        "current"
    )

rsLfapLostMessage = NotificationType(
    (1, 3, 6, 1, 4, 1, 5567, 2, 19, 2, 0, 2)
)
rsLfapLostMessage.setObjects(
      *(("RIVERSTONE-LFAP-MIB", "rsLfapStatsSessionChangedAt"),
        ("RIVERSTONE-LFAP-MIB", "rsLfapStatsLostAt"),
        ("RIVERSTONE-LFAP-MIB", "rsLfapStatsSessionUp"))
)
if mibBuilder.loadTexts:
    rsLfapLostMessage.setStatus(
        "current"
    )

rsLfapQueueFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 5567, 2, 19, 2, 0, 3)
)
rsLfapQueueFull.setObjects(
      *(("RIVERSTONE-LFAP-MIB", "rsLfapStatsDropsInTxQueue"),
        ("RIVERSTONE-LFAP-MIB", "rsLfapMaxTxQueueSize"),
        ("RIVERSTONE-LFAP-MIB", "rsLfapStatsSessionUp"))
)
if mibBuilder.loadTexts:
    rsLfapQueueFull.setStatus(
        "current"
    )


# Notifications groups

rsLfapNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 5567, 2, 19, 3, 2, 6)
)
rsLfapNotificationGroup.setObjects(
      *(("RIVERSTONE-LFAP-MIB", "rsLfapNoServer"),
        ("RIVERSTONE-LFAP-MIB", "rsLfapLostMessage"),
        ("RIVERSTONE-LFAP-MIB", "rsLfapQueueFull"))
)
if mibBuilder.loadTexts:
    rsLfapNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

rsLfapAgentCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5567, 2, 19, 3, 1, 1)
)
if mibBuilder.loadTexts:
    rsLfapAgentCompliance.setStatus(
        "current"
    )

rsLfapServerCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5567, 2, 19, 3, 1, 2)
)
if mibBuilder.loadTexts:
    rsLfapServerCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RIVERSTONE-LFAP-MIB",
    **{"RSLfapErrorCode": RSLfapErrorCode,
       "RsLfapServerInst": RsLfapServerInst,
       "RsTaskPriority": RsTaskPriority,
       "RSOperState": RSOperState,
       "rsLfapMIB": rsLfapMIB,
       "rsLfapMIBObjects": rsLfapMIBObjects,
       "rsLfapAgentState": rsLfapAgentState,
       "rsLfapCapabilities": rsLfapCapabilities,
       "rsLfapAdminState": rsLfapAdminState,
       "rsLfapOperState": rsLfapOperState,
       "rsLfapLastError": rsLfapLastError,
       "rsLfapLastErrorReason": rsLfapLastErrorReason,
       "rsLfapActiveServer": rsLfapActiveServer,
       "rsLfapAgentCfg": rsLfapAgentCfg,
       "rsLfapPollInterval": rsLfapPollInterval,
       "rsLfapBatchSize": rsLfapBatchSize,
       "rsLfapBatchInterval": rsLfapBatchInterval,
       "rsLfapLostContactInterval": rsLfapLostContactInterval,
       "rsLfapServerRetryInterval": rsLfapServerRetryInterval,
       "rsLfapMaxTxQueueSize": rsLfapMaxTxQueueSize,
       "rsLfapTaskPriority": rsLfapTaskPriority,
       "rsLfapServerCfg": rsLfapServerCfg,
       "rsLfapServerStaticLastChanged": rsLfapServerStaticLastChanged,
       "rsLfapServerStaticTable": rsLfapServerStaticTable,
       "rsLfapServerStaticEntry": rsLfapServerStaticEntry,
       "rsLfapServerStaticIndex": rsLfapServerStaticIndex,
       "rsLfapServerStaticAddressType": rsLfapServerStaticAddressType,
       "rsLfapServerStaticAddress": rsLfapServerStaticAddress,
       "rsLfapServerStaticStatus": rsLfapServerStaticStatus,
       "rsLfapStats": rsLfapStats,
       "rsLfapStatsTable": rsLfapStatsTable,
       "rsLfapStatsEntry": rsLfapStatsEntry,
       "rsLfapStatsSessionUp": rsLfapStatsSessionUp,
       "rsLfapStatsSessionChangedAt": rsLfapStatsSessionChangedAt,
       "rsLfapStatsTcpConnects": rsLfapStatsTcpConnects,
       "rsLfapStatsTcpConnectFails": rsLfapStatsTcpConnectFails,
       "rsLfapStatsTxVRs": rsLfapStatsTxVRs,
       "rsLfapStatsTxVRAs": rsLfapStatsTxVRAs,
       "rsLfapStatsTxFARs": rsLfapStatsTxFARs,
       "rsLfapStatsTxFUNs": rsLfapStatsTxFUNs,
       "rsLfapStatsTxARs": rsLfapStatsTxARs,
       "rsLfapStatsTxARAs": rsLfapStatsTxARAs,
       "rsLfapStatsMsgsInTxQueue": rsLfapStatsMsgsInTxQueue,
       "rsLfapStatsDropsInTxQueue": rsLfapStatsDropsInTxQueue,
       "rsLfapStatsDropsInTxQueueWhenUp": rsLfapStatsDropsInTxQueueWhenUp,
       "rsLfapStatsRxVRs": rsLfapStatsRxVRs,
       "rsLfapStatsRxVRAs": rsLfapStatsRxVRAs,
       "rsLfapStatsRxFARs": rsLfapStatsRxFARs,
       "rsLfapStatsRxFUNs": rsLfapStatsRxFUNs,
       "rsLfapStatsRxARs": rsLfapStatsRxARs,
       "rsLfapStatsRxARAs": rsLfapStatsRxARAs,
       "rsLfapStatsMsgsInRxQueue": rsLfapStatsMsgsInRxQueue,
       "rsLfapStatsInvalidMsgsRx": rsLfapStatsInvalidMsgsRx,
       "rsLfapStatsMsgsUnknownRx": rsLfapStatsMsgsUnknownRx,
       "rsLfapStatsTxLostPackets": rsLfapStatsTxLostPackets,
       "rsLfapStatsTxLostOctets": rsLfapStatsTxLostOctets,
       "rsLfapStatsLostAt": rsLfapStatsLostAt,
       "rsLfapStatsActiveFlows": rsLfapStatsActiveFlows,
       "rsLfapStatsFlowRate": rsLfapStatsFlowRate,
       "rsLfapStatsActiveFlowsPeak": rsLfapStatsActiveFlowsPeak,
       "rsLfapStatsMsgsInTxQueuePeak": rsLfapStatsMsgsInTxQueuePeak,
       "rsLfapStatsFlowsPeakTime": rsLfapStatsFlowsPeakTime,
       "rsLfapDiag": rsLfapDiag,
       "rsRunLfapSelfTest": rsRunLfapSelfTest,
       "rsLfapMIBEvents": rsLfapMIBEvents,
       "rsLfapMIBEventsPrefix": rsLfapMIBEventsPrefix,
       "rsLfapNoServer": rsLfapNoServer,
       "rsLfapLostMessage": rsLfapLostMessage,
       "rsLfapQueueFull": rsLfapQueueFull,
       "rsLfapConformance": rsLfapConformance,
       "rsLfapCompliances": rsLfapCompliances,
       "rsLfapAgentCompliance": rsLfapAgentCompliance,
       "rsLfapServerCompliance": rsLfapServerCompliance,
       "rsLfapGroups": rsLfapGroups,
       "rsLfapAgentStateGroup": rsLfapAgentStateGroup,
       "rsLfapAgentCfgGroup": rsLfapAgentCfgGroup,
       "rsLfapServerStaticGroup": rsLfapServerStaticGroup,
       "rsLfapStatsGroup": rsLfapStatsGroup,
       "rsLfapDiagGroup": rsLfapDiagGroup,
       "rsLfapNotificationGroup": rsLfapNotificationGroup}
)
