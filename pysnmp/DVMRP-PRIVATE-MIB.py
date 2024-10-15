# SNMP MIB module (DVMRP-PRIVATE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DVMRP-PRIVATE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:33:57 2024
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

(cjnProtocol,) = mibBuilder.importSymbols(
    "Cajun-ROOT",
    "cjnProtocol")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

cjnDvmrp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 13)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CjnDvmrpGblGroup_ObjectIdentity = ObjectIdentity
cjnDvmrpGblGroup = _CjnDvmrpGblGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 13, 1)
)


class _CjnDvmrpIsEnabled_Type(Integer32):
    """Custom type cjnDvmrpIsEnabled based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_CjnDvmrpIsEnabled_Type.__name__ = "Integer32"
_CjnDvmrpIsEnabled_Object = MibScalar
cjnDvmrpIsEnabled = _CjnDvmrpIsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 13, 1, 1),
    _CjnDvmrpIsEnabled_Type()
)
cjnDvmrpIsEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnDvmrpIsEnabled.setStatus("current")


class _CjnDvmrpNbrProbeInterval_Type(Integer32):
    """Custom type cjnDvmrpNbrProbeInterval based on Integer32"""
    defaultValue = 10


_CjnDvmrpNbrProbeInterval_Object = MibScalar
cjnDvmrpNbrProbeInterval = _CjnDvmrpNbrProbeInterval_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 13, 1, 2),
    _CjnDvmrpNbrProbeInterval_Type()
)
cjnDvmrpNbrProbeInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnDvmrpNbrProbeInterval.setStatus("current")


class _CjnDvmrpNbrTimeout_Type(Integer32):
    """Custom type cjnDvmrpNbrTimeout based on Integer32"""
    defaultValue = 35


_CjnDvmrpNbrTimeout_Object = MibScalar
cjnDvmrpNbrTimeout = _CjnDvmrpNbrTimeout_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 13, 1, 3),
    _CjnDvmrpNbrTimeout_Type()
)
cjnDvmrpNbrTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnDvmrpNbrTimeout.setStatus("current")


class _CjnDvmrpMinFlashUpdateInterval_Type(Integer32):
    """Custom type cjnDvmrpMinFlashUpdateInterval based on Integer32"""
    defaultValue = 5


_CjnDvmrpMinFlashUpdateInterval_Object = MibScalar
cjnDvmrpMinFlashUpdateInterval = _CjnDvmrpMinFlashUpdateInterval_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 13, 1, 4),
    _CjnDvmrpMinFlashUpdateInterval_Type()
)
cjnDvmrpMinFlashUpdateInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnDvmrpMinFlashUpdateInterval.setStatus("current")


class _CjnDvmrpMaxRoutes_Type(Integer32):
    """Custom type cjnDvmrpMaxRoutes based on Integer32"""
    defaultValue = 5000


_CjnDvmrpMaxRoutes_Object = MibScalar
cjnDvmrpMaxRoutes = _CjnDvmrpMaxRoutes_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 13, 1, 5),
    _CjnDvmrpMaxRoutes_Type()
)
cjnDvmrpMaxRoutes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnDvmrpMaxRoutes.setStatus("current")


class _CjnDvmrpRteReportInterval_Type(Integer32):
    """Custom type cjnDvmrpRteReportInterval based on Integer32"""
    defaultValue = 60


_CjnDvmrpRteReportInterval_Object = MibScalar
cjnDvmrpRteReportInterval = _CjnDvmrpRteReportInterval_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 13, 1, 6),
    _CjnDvmrpRteReportInterval_Type()
)
cjnDvmrpRteReportInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnDvmrpRteReportInterval.setStatus("current")


class _CjnDvmrpRteExpireTime_Type(Integer32):
    """Custom type cjnDvmrpRteExpireTime based on Integer32"""
    defaultValue = 140


_CjnDvmrpRteExpireTime_Object = MibScalar
cjnDvmrpRteExpireTime = _CjnDvmrpRteExpireTime_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 13, 1, 7),
    _CjnDvmrpRteExpireTime_Type()
)
cjnDvmrpRteExpireTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnDvmrpRteExpireTime.setStatus("current")


class _CjnDvmrpRteHoldTime_Type(Integer32):
    """Custom type cjnDvmrpRteHoldTime based on Integer32"""
    defaultValue = 120


_CjnDvmrpRteHoldTime_Object = MibScalar
cjnDvmrpRteHoldTime = _CjnDvmrpRteHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 13, 1, 8),
    _CjnDvmrpRteHoldTime_Type()
)
cjnDvmrpRteHoldTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnDvmrpRteHoldTime.setStatus("current")


class _CjnDvmrpPruneLifeTime_Type(Integer32):
    """Custom type cjnDvmrpPruneLifeTime based on Integer32"""
    defaultValue = 7200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7200),
    )


_CjnDvmrpPruneLifeTime_Type.__name__ = "Integer32"
_CjnDvmrpPruneLifeTime_Object = MibScalar
cjnDvmrpPruneLifeTime = _CjnDvmrpPruneLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 13, 1, 9),
    _CjnDvmrpPruneLifeTime_Type()
)
cjnDvmrpPruneLifeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnDvmrpPruneLifeTime.setStatus("current")


class _CjnDvmrpPruneRxmitTime_Type(Integer32):
    """Custom type cjnDvmrpPruneRxmitTime based on Integer32"""
    defaultValue = 3


_CjnDvmrpPruneRxmitTime_Object = MibScalar
cjnDvmrpPruneRxmitTime = _CjnDvmrpPruneRxmitTime_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 13, 1, 10),
    _CjnDvmrpPruneRxmitTime_Type()
)
cjnDvmrpPruneRxmitTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnDvmrpPruneRxmitTime.setStatus("current")


class _CjnDvmrpGraftRxmitTime_Type(Integer32):
    """Custom type cjnDvmrpGraftRxmitTime based on Integer32"""
    defaultValue = 5


_CjnDvmrpGraftRxmitTime_Object = MibScalar
cjnDvmrpGraftRxmitTime = _CjnDvmrpGraftRxmitTime_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 13, 1, 11),
    _CjnDvmrpGraftRxmitTime_Type()
)
cjnDvmrpGraftRxmitTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnDvmrpGraftRxmitTime.setStatus("current")


class _CjnDvmrpGlobalStatsReset_Type(Integer32):
    """Custom type cjnDvmrpGlobalStatsReset based on Integer32"""
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


_CjnDvmrpGlobalStatsReset_Type.__name__ = "Integer32"
_CjnDvmrpGlobalStatsReset_Object = MibScalar
cjnDvmrpGlobalStatsReset = _CjnDvmrpGlobalStatsReset_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 13, 1, 12),
    _CjnDvmrpGlobalStatsReset_Type()
)
cjnDvmrpGlobalStatsReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnDvmrpGlobalStatsReset.setStatus("current")
_CjnDvmrpStatsGroup_ObjectIdentity = ObjectIdentity
cjnDvmrpStatsGroup = _CjnDvmrpStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 13, 2)
)
_CjnDvmrpRxProbe_Type = Integer32
_CjnDvmrpRxProbe_Object = MibScalar
cjnDvmrpRxProbe = _CjnDvmrpRxProbe_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 13, 2, 1),
    _CjnDvmrpRxProbe_Type()
)
cjnDvmrpRxProbe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnDvmrpRxProbe.setStatus("current")
_CjnDvmrpTxProbe_Type = Integer32
_CjnDvmrpTxProbe_Object = MibScalar
cjnDvmrpTxProbe = _CjnDvmrpTxProbe_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 13, 2, 2),
    _CjnDvmrpTxProbe_Type()
)
cjnDvmrpTxProbe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnDvmrpTxProbe.setStatus("current")
_CjnDvmrpRxReport_Type = Integer32
_CjnDvmrpRxReport_Object = MibScalar
cjnDvmrpRxReport = _CjnDvmrpRxReport_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 13, 2, 3),
    _CjnDvmrpRxReport_Type()
)
cjnDvmrpRxReport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnDvmrpRxReport.setStatus("current")
_CjnDvmrpTxReport_Type = Integer32
_CjnDvmrpTxReport_Object = MibScalar
cjnDvmrpTxReport = _CjnDvmrpTxReport_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 13, 2, 4),
    _CjnDvmrpTxReport_Type()
)
cjnDvmrpTxReport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnDvmrpTxReport.setStatus("current")
_CjnDvmrpRxPrune_Type = Integer32
_CjnDvmrpRxPrune_Object = MibScalar
cjnDvmrpRxPrune = _CjnDvmrpRxPrune_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 13, 2, 5),
    _CjnDvmrpRxPrune_Type()
)
cjnDvmrpRxPrune.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnDvmrpRxPrune.setStatus("current")
_CjnDvmrpTxPrune_Type = Integer32
_CjnDvmrpTxPrune_Object = MibScalar
cjnDvmrpTxPrune = _CjnDvmrpTxPrune_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 13, 2, 6),
    _CjnDvmrpTxPrune_Type()
)
cjnDvmrpTxPrune.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnDvmrpTxPrune.setStatus("current")
_CjnDvmrpRxGraft_Type = Integer32
_CjnDvmrpRxGraft_Object = MibScalar
cjnDvmrpRxGraft = _CjnDvmrpRxGraft_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 13, 2, 7),
    _CjnDvmrpRxGraft_Type()
)
cjnDvmrpRxGraft.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnDvmrpRxGraft.setStatus("current")
_CjnDvmrpTxGraft_Type = Integer32
_CjnDvmrpTxGraft_Object = MibScalar
cjnDvmrpTxGraft = _CjnDvmrpTxGraft_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 13, 2, 8),
    _CjnDvmrpTxGraft_Type()
)
cjnDvmrpTxGraft.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnDvmrpTxGraft.setStatus("current")
_CjnDvmrpRxGraftAck_Type = Integer32
_CjnDvmrpRxGraftAck_Object = MibScalar
cjnDvmrpRxGraftAck = _CjnDvmrpRxGraftAck_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 13, 2, 9),
    _CjnDvmrpRxGraftAck_Type()
)
cjnDvmrpRxGraftAck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnDvmrpRxGraftAck.setStatus("current")
_CjnDvmrpTxGraftAck_Type = Integer32
_CjnDvmrpTxGraftAck_Object = MibScalar
cjnDvmrpTxGraftAck = _CjnDvmrpTxGraftAck_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 13, 2, 10),
    _CjnDvmrpTxGraftAck_Type()
)
cjnDvmrpTxGraftAck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnDvmrpTxGraftAck.setStatus("current")
_CjnDvmrpRxUnknownCode_Type = Integer32
_CjnDvmrpRxUnknownCode_Object = MibScalar
cjnDvmrpRxUnknownCode = _CjnDvmrpRxUnknownCode_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 13, 2, 11),
    _CjnDvmrpRxUnknownCode_Type()
)
cjnDvmrpRxUnknownCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnDvmrpRxUnknownCode.setStatus("current")
_CjnDvmrpNumValidRts_Type = Integer32
_CjnDvmrpNumValidRts_Object = MibScalar
cjnDvmrpNumValidRts = _CjnDvmrpNumValidRts_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 13, 2, 12),
    _CjnDvmrpNumValidRts_Type()
)
cjnDvmrpNumValidRts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnDvmrpNumValidRts.setStatus("current")
_CjnDvmrpNumRts_Type = Integer32
_CjnDvmrpNumRts_Object = MibScalar
cjnDvmrpNumRts = _CjnDvmrpNumRts_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 13, 2, 13),
    _CjnDvmrpNumRts_Type()
)
cjnDvmrpNumRts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnDvmrpNumRts.setStatus("current")
_CjnDvmrpNumTrigdRts_Type = Integer32
_CjnDvmrpNumTrigdRts_Object = MibScalar
cjnDvmrpNumTrigdRts = _CjnDvmrpNumTrigdRts_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 13, 2, 14),
    _CjnDvmrpNumTrigdRts_Type()
)
cjnDvmrpNumTrigdRts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnDvmrpNumTrigdRts.setStatus("current")
_CjnDvmrpLastRep_Type = Integer32
_CjnDvmrpLastRep_Object = MibScalar
cjnDvmrpLastRep = _CjnDvmrpLastRep_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 13, 2, 15),
    _CjnDvmrpLastRep_Type()
)
cjnDvmrpLastRep.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnDvmrpLastRep.setStatus("current")
_CjnDvmrpIfGroup_ObjectIdentity = ObjectIdentity
cjnDvmrpIfGroup = _CjnDvmrpIfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 13, 3)
)
_CjnDvmrpIfTable_Object = MibTable
cjnDvmrpIfTable = _CjnDvmrpIfTable_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 13, 3, 1)
)
if mibBuilder.loadTexts:
    cjnDvmrpIfTable.setStatus("current")
_CjnDvmrpIfEntry_Object = MibTableRow
cjnDvmrpIfEntry = _CjnDvmrpIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 13, 3, 1, 1)
)
cjnDvmrpIfEntry.setIndexNames(
    (0, "DVMRP-PRIVATE-MIB", "cjnDvmrpIfIndex"),
)
if mibBuilder.loadTexts:
    cjnDvmrpIfEntry.setStatus("current")
_CjnDvmrpIfIndex_Type = Integer32
_CjnDvmrpIfIndex_Object = MibTableColumn
cjnDvmrpIfIndex = _CjnDvmrpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 13, 3, 1, 1, 1),
    _CjnDvmrpIfIndex_Type()
)
cjnDvmrpIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cjnDvmrpIfIndex.setStatus("current")
_CjnDvmrpIfRowStatus_Type = RowStatus
_CjnDvmrpIfRowStatus_Object = MibTableColumn
cjnDvmrpIfRowStatus = _CjnDvmrpIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 13, 3, 1, 1, 2),
    _CjnDvmrpIfRowStatus_Type()
)
cjnDvmrpIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnDvmrpIfRowStatus.setStatus("current")


class _CjnDvmrpIfType_Type(Integer32):
    """Custom type cjnDvmrpIfType based on Integer32"""
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
        *(("broadcast", 0),
          ("ipIpTunnel", 2),
          ("nonEncapsulatedTunnel", 1))
    )


_CjnDvmrpIfType_Type.__name__ = "Integer32"
_CjnDvmrpIfType_Object = MibTableColumn
cjnDvmrpIfType = _CjnDvmrpIfType_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 13, 3, 1, 1, 3),
    _CjnDvmrpIfType_Type()
)
cjnDvmrpIfType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnDvmrpIfType.setStatus("current")
_CjnDvmrpIfTnAddress_Type = IpAddress
_CjnDvmrpIfTnAddress_Object = MibTableColumn
cjnDvmrpIfTnAddress = _CjnDvmrpIfTnAddress_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 13, 3, 1, 1, 4),
    _CjnDvmrpIfTnAddress_Type()
)
cjnDvmrpIfTnAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnDvmrpIfTnAddress.setStatus("current")


class _CjnDvmrpIfMetric_Type(Integer32):
    """Custom type cjnDvmrpIfMetric based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_CjnDvmrpIfMetric_Type.__name__ = "Integer32"
_CjnDvmrpIfMetric_Object = MibTableColumn
cjnDvmrpIfMetric = _CjnDvmrpIfMetric_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 13, 3, 1, 1, 5),
    _CjnDvmrpIfMetric_Type()
)
cjnDvmrpIfMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnDvmrpIfMetric.setStatus("current")


class _CjnDvmrpIfScope_Type(Integer32):
    """Custom type cjnDvmrpIfScope based on Integer32"""
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
        *(("scope0", 0),
          ("scope127", 1),
          ("scope255", 2))
    )


_CjnDvmrpIfScope_Type.__name__ = "Integer32"
_CjnDvmrpIfScope_Object = MibTableColumn
cjnDvmrpIfScope = _CjnDvmrpIfScope_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 13, 3, 1, 1, 6),
    _CjnDvmrpIfScope_Type()
)
cjnDvmrpIfScope.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnDvmrpIfScope.setStatus("current")


class _CjnDvmrpPruneSource_Type(Integer32):
    """Custom type cjnDvmrpPruneSource based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("hostAddr", 1),
          ("networkAddr", 0))
    )


_CjnDvmrpPruneSource_Type.__name__ = "Integer32"
_CjnDvmrpPruneSource_Object = MibTableColumn
cjnDvmrpPruneSource = _CjnDvmrpPruneSource_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 13, 3, 1, 1, 7),
    _CjnDvmrpPruneSource_Type()
)
cjnDvmrpPruneSource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnDvmrpPruneSource.setStatus("current")
_CjnDvmrpIfStatTable_Object = MibTable
cjnDvmrpIfStatTable = _CjnDvmrpIfStatTable_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 13, 3, 2)
)
if mibBuilder.loadTexts:
    cjnDvmrpIfStatTable.setStatus("current")
_CjnDvmrpIfStatEntry_Object = MibTableRow
cjnDvmrpIfStatEntry = _CjnDvmrpIfStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 13, 3, 2, 1)
)
cjnDvmrpIfStatEntry.setIndexNames(
    (0, "DVMRP-PRIVATE-MIB", "cjnDvmrpIfStatIndex"),
)
if mibBuilder.loadTexts:
    cjnDvmrpIfStatEntry.setStatus("current")
_CjnDvmrpIfStatIndex_Type = Integer32
_CjnDvmrpIfStatIndex_Object = MibTableColumn
cjnDvmrpIfStatIndex = _CjnDvmrpIfStatIndex_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 13, 3, 2, 1, 1),
    _CjnDvmrpIfStatIndex_Type()
)
cjnDvmrpIfStatIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cjnDvmrpIfStatIndex.setStatus("current")
_CjnDvmrpIfBadPackets_Type = Integer32
_CjnDvmrpIfBadPackets_Object = MibTableColumn
cjnDvmrpIfBadPackets = _CjnDvmrpIfBadPackets_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 13, 3, 2, 1, 2),
    _CjnDvmrpIfBadPackets_Type()
)
cjnDvmrpIfBadPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnDvmrpIfBadPackets.setStatus("current")
_CjnDvmrpIfBadRoutes_Type = Integer32
_CjnDvmrpIfBadRoutes_Object = MibTableColumn
cjnDvmrpIfBadRoutes = _CjnDvmrpIfBadRoutes_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 13, 3, 2, 1, 3),
    _CjnDvmrpIfBadRoutes_Type()
)
cjnDvmrpIfBadRoutes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnDvmrpIfBadRoutes.setStatus("current")
_CjnDvmrpIfNbrCount_Type = Integer32
_CjnDvmrpIfNbrCount_Object = MibTableColumn
cjnDvmrpIfNbrCount = _CjnDvmrpIfNbrCount_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 13, 3, 2, 1, 4),
    _CjnDvmrpIfNbrCount_Type()
)
cjnDvmrpIfNbrCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnDvmrpIfNbrCount.setStatus("current")
_CjnDvmrpIfSentRoutes_Type = Integer32
_CjnDvmrpIfSentRoutes_Object = MibTableColumn
cjnDvmrpIfSentRoutes = _CjnDvmrpIfSentRoutes_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 13, 3, 2, 1, 5),
    _CjnDvmrpIfSentRoutes_Type()
)
cjnDvmrpIfSentRoutes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnDvmrpIfSentRoutes.setStatus("current")
_CjnDvmrpIfState_Type = Integer32
_CjnDvmrpIfState_Object = MibTableColumn
cjnDvmrpIfState = _CjnDvmrpIfState_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 13, 3, 2, 1, 6),
    _CjnDvmrpIfState_Type()
)
cjnDvmrpIfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnDvmrpIfState.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DVMRP-PRIVATE-MIB",
    **{"cjnDvmrp": cjnDvmrp,
       "cjnDvmrpGblGroup": cjnDvmrpGblGroup,
       "cjnDvmrpIsEnabled": cjnDvmrpIsEnabled,
       "cjnDvmrpNbrProbeInterval": cjnDvmrpNbrProbeInterval,
       "cjnDvmrpNbrTimeout": cjnDvmrpNbrTimeout,
       "cjnDvmrpMinFlashUpdateInterval": cjnDvmrpMinFlashUpdateInterval,
       "cjnDvmrpMaxRoutes": cjnDvmrpMaxRoutes,
       "cjnDvmrpRteReportInterval": cjnDvmrpRteReportInterval,
       "cjnDvmrpRteExpireTime": cjnDvmrpRteExpireTime,
       "cjnDvmrpRteHoldTime": cjnDvmrpRteHoldTime,
       "cjnDvmrpPruneLifeTime": cjnDvmrpPruneLifeTime,
       "cjnDvmrpPruneRxmitTime": cjnDvmrpPruneRxmitTime,
       "cjnDvmrpGraftRxmitTime": cjnDvmrpGraftRxmitTime,
       "cjnDvmrpGlobalStatsReset": cjnDvmrpGlobalStatsReset,
       "cjnDvmrpStatsGroup": cjnDvmrpStatsGroup,
       "cjnDvmrpRxProbe": cjnDvmrpRxProbe,
       "cjnDvmrpTxProbe": cjnDvmrpTxProbe,
       "cjnDvmrpRxReport": cjnDvmrpRxReport,
       "cjnDvmrpTxReport": cjnDvmrpTxReport,
       "cjnDvmrpRxPrune": cjnDvmrpRxPrune,
       "cjnDvmrpTxPrune": cjnDvmrpTxPrune,
       "cjnDvmrpRxGraft": cjnDvmrpRxGraft,
       "cjnDvmrpTxGraft": cjnDvmrpTxGraft,
       "cjnDvmrpRxGraftAck": cjnDvmrpRxGraftAck,
       "cjnDvmrpTxGraftAck": cjnDvmrpTxGraftAck,
       "cjnDvmrpRxUnknownCode": cjnDvmrpRxUnknownCode,
       "cjnDvmrpNumValidRts": cjnDvmrpNumValidRts,
       "cjnDvmrpNumRts": cjnDvmrpNumRts,
       "cjnDvmrpNumTrigdRts": cjnDvmrpNumTrigdRts,
       "cjnDvmrpLastRep": cjnDvmrpLastRep,
       "cjnDvmrpIfGroup": cjnDvmrpIfGroup,
       "cjnDvmrpIfTable": cjnDvmrpIfTable,
       "cjnDvmrpIfEntry": cjnDvmrpIfEntry,
       "cjnDvmrpIfIndex": cjnDvmrpIfIndex,
       "cjnDvmrpIfRowStatus": cjnDvmrpIfRowStatus,
       "cjnDvmrpIfType": cjnDvmrpIfType,
       "cjnDvmrpIfTnAddress": cjnDvmrpIfTnAddress,
       "cjnDvmrpIfMetric": cjnDvmrpIfMetric,
       "cjnDvmrpIfScope": cjnDvmrpIfScope,
       "cjnDvmrpPruneSource": cjnDvmrpPruneSource,
       "cjnDvmrpIfStatTable": cjnDvmrpIfStatTable,
       "cjnDvmrpIfStatEntry": cjnDvmrpIfStatEntry,
       "cjnDvmrpIfStatIndex": cjnDvmrpIfStatIndex,
       "cjnDvmrpIfBadPackets": cjnDvmrpIfBadPackets,
       "cjnDvmrpIfBadRoutes": cjnDvmrpIfBadRoutes,
       "cjnDvmrpIfNbrCount": cjnDvmrpIfNbrCount,
       "cjnDvmrpIfSentRoutes": cjnDvmrpIfSentRoutes,
       "cjnDvmrpIfState": cjnDvmrpIfState}
)
