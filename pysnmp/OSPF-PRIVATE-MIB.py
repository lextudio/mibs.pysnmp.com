# SNMP MIB module (OSPF-PRIVATE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/OSPF-PRIVATE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:35:43 2024
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

(AreaID,
 Metric,
 RouterID,
 TOSType) = mibBuilder.importSymbols(
    "OSPF-MIB",
    "AreaID",
    "Metric",
    "RouterID",
    "TOSType")

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

cjnOspf = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CjnOspfGblConfGroup_ObjectIdentity = ObjectIdentity
cjnOspfGblConfGroup = _CjnOspfGblConfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 1)
)
_CjnOspfRouterId_Type = RouterID
_CjnOspfRouterId_Object = MibScalar
cjnOspfRouterId = _CjnOspfRouterId_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 1, 1),
    _CjnOspfRouterId_Type()
)
cjnOspfRouterId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnOspfRouterId.setStatus("current")
_CjnOspfPathSplit_Type = Integer32
_CjnOspfPathSplit_Object = MibScalar
cjnOspfPathSplit = _CjnOspfPathSplit_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 1, 2),
    _CjnOspfPathSplit_Type()
)
cjnOspfPathSplit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnOspfPathSplit.setStatus("current")
_CjnOspfPeMax_Type = Integer32
_CjnOspfPeMax_Object = MibScalar
cjnOspfPeMax = _CjnOspfPeMax_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 1, 3),
    _CjnOspfPeMax_Type()
)
cjnOspfPeMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnOspfPeMax.setStatus("current")


class _CjnOspfSpfState_Type(Integer32):
    """Custom type cjnOspfSpfState based on Integer32"""
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


_CjnOspfSpfState_Type.__name__ = "Integer32"
_CjnOspfSpfState_Object = MibScalar
cjnOspfSpfState = _CjnOspfSpfState_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 1, 4),
    _CjnOspfSpfState_Type()
)
cjnOspfSpfState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnOspfSpfState.setStatus("current")


class _CjnOspfAsbdrStatus_Type(Integer32):
    """Custom type cjnOspfAsbdrStatus based on Integer32"""
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


_CjnOspfAsbdrStatus_Type.__name__ = "Integer32"
_CjnOspfAsbdrStatus_Object = MibScalar
cjnOspfAsbdrStatus = _CjnOspfAsbdrStatus_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 1, 5),
    _CjnOspfAsbdrStatus_Type()
)
cjnOspfAsbdrStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnOspfAsbdrStatus.setStatus("current")


class _CjnOspfAutoVLinkCreate_Type(Integer32):
    """Custom type cjnOspfAutoVLinkCreate based on Integer32"""
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


_CjnOspfAutoVLinkCreate_Type.__name__ = "Integer32"
_CjnOspfAutoVLinkCreate_Object = MibScalar
cjnOspfAutoVLinkCreate = _CjnOspfAutoVLinkCreate_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 1, 6),
    _CjnOspfAutoVLinkCreate_Type()
)
cjnOspfAutoVLinkCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnOspfAutoVLinkCreate.setStatus("current")


class _CjnOspfSpfHold_Type(Integer32):
    """Custom type cjnOspfSpfHold based on Integer32"""
    defaultValue = 3


_CjnOspfSpfHold_Object = MibScalar
cjnOspfSpfHold = _CjnOspfSpfHold_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 1, 7),
    _CjnOspfSpfHold_Type()
)
cjnOspfSpfHold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnOspfSpfHold.setStatus("current")


class _CjnOspfSpfSuspendTime_Type(Integer32):
    """Custom type cjnOspfSpfSuspendTime based on Integer32"""
    defaultValue = 1000


_CjnOspfSpfSuspendTime_Object = MibScalar
cjnOspfSpfSuspendTime = _CjnOspfSpfSuspendTime_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 1, 8),
    _CjnOspfSpfSuspendTime_Type()
)
cjnOspfSpfSuspendTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnOspfSpfSuspendTime.setStatus("current")


class _CjnOspfLocalExtType_Type(Integer32):
    """Custom type cjnOspfLocalExtType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_CjnOspfLocalExtType_Type.__name__ = "Integer32"
_CjnOspfLocalExtType_Object = MibScalar
cjnOspfLocalExtType = _CjnOspfLocalExtType_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 1, 9),
    _CjnOspfLocalExtType_Type()
)
cjnOspfLocalExtType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnOspfLocalExtType.setStatus("current")


class _CjnOspfRipExtType_Type(Integer32):
    """Custom type cjnOspfRipExtType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_CjnOspfRipExtType_Type.__name__ = "Integer32"
_CjnOspfRipExtType_Object = MibScalar
cjnOspfRipExtType = _CjnOspfRipExtType_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 1, 10),
    _CjnOspfRipExtType_Type()
)
cjnOspfRipExtType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnOspfRipExtType.setStatus("current")


class _CjnOspfSpfStaticExtType_Type(Integer32):
    """Custom type cjnOspfSpfStaticExtType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_CjnOspfSpfStaticExtType_Type.__name__ = "Integer32"
_CjnOspfSpfStaticExtType_Object = MibScalar
cjnOspfSpfStaticExtType = _CjnOspfSpfStaticExtType_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 1, 11),
    _CjnOspfSpfStaticExtType_Type()
)
cjnOspfSpfStaticExtType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnOspfSpfStaticExtType.setStatus("current")


class _CjnOspfLowExtType_Type(Integer32):
    """Custom type cjnOspfLowExtType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_CjnOspfLowExtType_Type.__name__ = "Integer32"
_CjnOspfLowExtType_Object = MibScalar
cjnOspfLowExtType = _CjnOspfLowExtType_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 1, 12),
    _CjnOspfLowExtType_Type()
)
cjnOspfLowExtType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnOspfLowExtType.setStatus("current")


class _CjnOspfTraceFlags_Type(Integer32):
    """Custom type cjnOspfTraceFlags based on Integer32"""
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


_CjnOspfTraceFlags_Type.__name__ = "Integer32"
_CjnOspfTraceFlags_Object = MibScalar
cjnOspfTraceFlags = _CjnOspfTraceFlags_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 1, 13),
    _CjnOspfTraceFlags_Type()
)
cjnOspfTraceFlags.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnOspfTraceFlags.setStatus("current")


class _CjnOspfGlobalStatsReset_Type(Integer32):
    """Custom type cjnOspfGlobalStatsReset based on Integer32"""
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


_CjnOspfGlobalStatsReset_Type.__name__ = "Integer32"
_CjnOspfGlobalStatsReset_Object = MibScalar
cjnOspfGlobalStatsReset = _CjnOspfGlobalStatsReset_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 1, 14),
    _CjnOspfGlobalStatsReset_Type()
)
cjnOspfGlobalStatsReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnOspfGlobalStatsReset.setStatus("current")
_CjnOspfGblStatsGroup_ObjectIdentity = ObjectIdentity
cjnOspfGblStatsGroup = _CjnOspfGblStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 2)
)
_CjnOspfTOSCount_Type = Integer32
_CjnOspfTOSCount_Object = MibScalar
cjnOspfTOSCount = _CjnOspfTOSCount_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 2, 1),
    _CjnOspfTOSCount_Type()
)
cjnOspfTOSCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnOspfTOSCount.setStatus("current")
_CjnOspfRunSpf_Type = Integer32
_CjnOspfRunSpf_Object = MibScalar
cjnOspfRunSpf = _CjnOspfRunSpf_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 2, 2),
    _CjnOspfRunSpf_Type()
)
cjnOspfRunSpf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnOspfRunSpf.setStatus("current")


class _CjnOspfAbdrStatus_Type(Integer32):
    """Custom type cjnOspfAbdrStatus based on Integer32"""
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


_CjnOspfAbdrStatus_Type.__name__ = "Integer32"
_CjnOspfAbdrStatus_Object = MibScalar
cjnOspfAbdrStatus = _CjnOspfAbdrStatus_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 2, 3),
    _CjnOspfAbdrStatus_Type()
)
cjnOspfAbdrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnOspfAbdrStatus.setStatus("current")
_CjnOspfTxNewLsa_Type = Integer32
_CjnOspfTxNewLsa_Object = MibScalar
cjnOspfTxNewLsa = _CjnOspfTxNewLsa_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 2, 4),
    _CjnOspfTxNewLsa_Type()
)
cjnOspfTxNewLsa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnOspfTxNewLsa.setStatus("current")
_CjnOspfRxNewLsa_Type = Integer32
_CjnOspfRxNewLsa_Object = MibScalar
cjnOspfRxNewLsa = _CjnOspfRxNewLsa_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 2, 5),
    _CjnOspfRxNewLsa_Type()
)
cjnOspfRxNewLsa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnOspfRxNewLsa.setStatus("current")
_CjnOspfRxHelloCnt_Type = Integer32
_CjnOspfRxHelloCnt_Object = MibScalar
cjnOspfRxHelloCnt = _CjnOspfRxHelloCnt_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 2, 6),
    _CjnOspfRxHelloCnt_Type()
)
cjnOspfRxHelloCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnOspfRxHelloCnt.setStatus("current")
_CjnOspfTxHelloCnt_Type = Integer32
_CjnOspfTxHelloCnt_Object = MibScalar
cjnOspfTxHelloCnt = _CjnOspfTxHelloCnt_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 2, 7),
    _CjnOspfTxHelloCnt_Type()
)
cjnOspfTxHelloCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnOspfTxHelloCnt.setStatus("current")
_CjnOspfRxDBDescCnt_Type = Integer32
_CjnOspfRxDBDescCnt_Object = MibScalar
cjnOspfRxDBDescCnt = _CjnOspfRxDBDescCnt_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 2, 8),
    _CjnOspfRxDBDescCnt_Type()
)
cjnOspfRxDBDescCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnOspfRxDBDescCnt.setStatus("current")
_CjnOspfTxDBDescCnt_Type = Integer32
_CjnOspfTxDBDescCnt_Object = MibScalar
cjnOspfTxDBDescCnt = _CjnOspfTxDBDescCnt_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 2, 9),
    _CjnOspfTxDBDescCnt_Type()
)
cjnOspfTxDBDescCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnOspfTxDBDescCnt.setStatus("current")
_CjnOspfRxLsaAckCnt_Type = Integer32
_CjnOspfRxLsaAckCnt_Object = MibScalar
cjnOspfRxLsaAckCnt = _CjnOspfRxLsaAckCnt_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 2, 10),
    _CjnOspfRxLsaAckCnt_Type()
)
cjnOspfRxLsaAckCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnOspfRxLsaAckCnt.setStatus("current")
_CjnOspfTxLsaAckCnt_Type = Integer32
_CjnOspfTxLsaAckCnt_Object = MibScalar
cjnOspfTxLsaAckCnt = _CjnOspfTxLsaAckCnt_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 2, 11),
    _CjnOspfTxLsaAckCnt_Type()
)
cjnOspfTxLsaAckCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnOspfTxLsaAckCnt.setStatus("current")
_CjnOspfRxLsaUpdCnt_Type = Integer32
_CjnOspfRxLsaUpdCnt_Object = MibScalar
cjnOspfRxLsaUpdCnt = _CjnOspfRxLsaUpdCnt_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 2, 12),
    _CjnOspfRxLsaUpdCnt_Type()
)
cjnOspfRxLsaUpdCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnOspfRxLsaUpdCnt.setStatus("current")
_CjnOspfTxLsaUpdCnt_Type = Integer32
_CjnOspfTxLsaUpdCnt_Object = MibScalar
cjnOspfTxLsaUpdCnt = _CjnOspfTxLsaUpdCnt_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 2, 13),
    _CjnOspfTxLsaUpdCnt_Type()
)
cjnOspfTxLsaUpdCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnOspfTxLsaUpdCnt.setStatus("current")
_CjnOspfRxLsaReqCnt_Type = Integer32
_CjnOspfRxLsaReqCnt_Object = MibScalar
cjnOspfRxLsaReqCnt = _CjnOspfRxLsaReqCnt_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 2, 14),
    _CjnOspfRxLsaReqCnt_Type()
)
cjnOspfRxLsaReqCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnOspfRxLsaReqCnt.setStatus("current")
_CjnOspfTxLsaReqCnt_Type = Integer32
_CjnOspfTxLsaReqCnt_Object = MibScalar
cjnOspfTxLsaReqCnt = _CjnOspfTxLsaReqCnt_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 2, 15),
    _CjnOspfTxLsaReqCnt_Type()
)
cjnOspfTxLsaReqCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnOspfTxLsaReqCnt.setStatus("current")
_CjnOspfIfTable_Object = MibTable
cjnOspfIfTable = _CjnOspfIfTable_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 3)
)
if mibBuilder.loadTexts:
    cjnOspfIfTable.setStatus("current")
_CjnOspfIfEntry_Object = MibTableRow
cjnOspfIfEntry = _CjnOspfIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 3, 1)
)
cjnOspfIfEntry.setIndexNames(
    (0, "OSPF-PRIVATE-MIB", "cjnOspfIfIpAddress"),
)
if mibBuilder.loadTexts:
    cjnOspfIfEntry.setStatus("current")
_CjnOspfIfIpAddress_Type = IpAddress
_CjnOspfIfIpAddress_Object = MibTableColumn
cjnOspfIfIpAddress = _CjnOspfIfIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 3, 1, 1),
    _CjnOspfIfIpAddress_Type()
)
cjnOspfIfIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnOspfIfIpAddress.setStatus("current")
_CjnOspfIfRowStatus_Type = RowStatus
_CjnOspfIfRowStatus_Object = MibTableColumn
cjnOspfIfRowStatus = _CjnOspfIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 3, 1, 2),
    _CjnOspfIfRowStatus_Type()
)
cjnOspfIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnOspfIfRowStatus.setStatus("current")
_CjnOspfIfAreaId_Type = AreaID
_CjnOspfIfAreaId_Object = MibTableColumn
cjnOspfIfAreaId = _CjnOspfIfAreaId_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 3, 1, 3),
    _CjnOspfIfAreaId_Type()
)
cjnOspfIfAreaId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnOspfIfAreaId.setStatus("current")
_CjnOspfIfMask_Type = IpAddress
_CjnOspfIfMask_Object = MibTableColumn
cjnOspfIfMask = _CjnOspfIfMask_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 3, 1, 4),
    _CjnOspfIfMask_Type()
)
cjnOspfIfMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnOspfIfMask.setStatus("current")


class _CjnOspfIfType_Type(Integer32):
    """Custom type cjnOspfIfType based on Integer32"""
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
        *(("bcast", 1),
          ("nbma", 2),
          ("pointToMultiPoint", 4),
          ("pointToPoint", 3))
    )


_CjnOspfIfType_Type.__name__ = "Integer32"
_CjnOspfIfType_Object = MibTableColumn
cjnOspfIfType = _CjnOspfIfType_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 3, 1, 5),
    _CjnOspfIfType_Type()
)
cjnOspfIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnOspfIfType.setStatus("current")
_CjnOspfIfCost_Type = Integer32
_CjnOspfIfCost_Object = MibTableColumn
cjnOspfIfCost = _CjnOspfIfCost_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 3, 1, 6),
    _CjnOspfIfCost_Type()
)
cjnOspfIfCost.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnOspfIfCost.setStatus("current")
_CjnOspfIfDrRouterId_Type = RouterID
_CjnOspfIfDrRouterId_Object = MibTableColumn
cjnOspfIfDrRouterId = _CjnOspfIfDrRouterId_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 3, 1, 7),
    _CjnOspfIfDrRouterId_Type()
)
cjnOspfIfDrRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnOspfIfDrRouterId.setStatus("current")
_CjnOspfIfDrIpAddr_Type = IpAddress
_CjnOspfIfDrIpAddr_Object = MibTableColumn
cjnOspfIfDrIpAddr = _CjnOspfIfDrIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 3, 1, 8),
    _CjnOspfIfDrIpAddr_Type()
)
cjnOspfIfDrIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnOspfIfDrIpAddr.setStatus("current")
_CjnOspfIfBDrRouterId_Type = Integer32
_CjnOspfIfBDrRouterId_Object = MibTableColumn
cjnOspfIfBDrRouterId = _CjnOspfIfBDrRouterId_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 3, 1, 9),
    _CjnOspfIfBDrRouterId_Type()
)
cjnOspfIfBDrRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnOspfIfBDrRouterId.setStatus("current")
_CjnOspfIfDrState_Type = Integer32
_CjnOspfIfDrState_Object = MibTableColumn
cjnOspfIfDrState = _CjnOspfIfDrState_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 3, 1, 10),
    _CjnOspfIfDrState_Type()
)
cjnOspfIfDrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnOspfIfDrState.setStatus("current")
_CjnOspfIfHelloTimer_Type = Integer32
_CjnOspfIfHelloTimer_Object = MibTableColumn
cjnOspfIfHelloTimer = _CjnOspfIfHelloTimer_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 3, 1, 11),
    _CjnOspfIfHelloTimer_Type()
)
cjnOspfIfHelloTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnOspfIfHelloTimer.setStatus("current")
_CjnOspfIfDeadInterval_Type = Integer32
_CjnOspfIfDeadInterval_Object = MibTableColumn
cjnOspfIfDeadInterval = _CjnOspfIfDeadInterval_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 3, 1, 12),
    _CjnOspfIfDeadInterval_Type()
)
cjnOspfIfDeadInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnOspfIfDeadInterval.setStatus("current")
_CjnOspfIfRtrPriority_Type = Integer32
_CjnOspfIfRtrPriority_Object = MibTableColumn
cjnOspfIfRtrPriority = _CjnOspfIfRtrPriority_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 3, 1, 13),
    _CjnOspfIfRtrPriority_Type()
)
cjnOspfIfRtrPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnOspfIfRtrPriority.setStatus("current")
_CjnOspfIfRxmtTimer_Type = Integer32
_CjnOspfIfRxmtTimer_Object = MibTableColumn
cjnOspfIfRxmtTimer = _CjnOspfIfRxmtTimer_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 3, 1, 14),
    _CjnOspfIfRxmtTimer_Type()
)
cjnOspfIfRxmtTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnOspfIfRxmtTimer.setStatus("current")
_CjnOspfIfTransitDelay_Type = Integer32
_CjnOspfIfTransitDelay_Object = MibTableColumn
cjnOspfIfTransitDelay = _CjnOspfIfTransitDelay_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 3, 1, 15),
    _CjnOspfIfTransitDelay_Type()
)
cjnOspfIfTransitDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnOspfIfTransitDelay.setStatus("current")


class _CjnOspfIfAuthKey_Type(OctetString):
    """Custom type cjnOspfIfAuthKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_CjnOspfIfAuthKey_Type.__name__ = "OctetString"
_CjnOspfIfAuthKey_Object = MibTableColumn
cjnOspfIfAuthKey = _CjnOspfIfAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 3, 1, 16),
    _CjnOspfIfAuthKey_Type()
)
cjnOspfIfAuthKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnOspfIfAuthKey.setStatus("current")
_CjnOspfIfMd5KeyId_Type = Integer32
_CjnOspfIfMd5KeyId_Object = MibTableColumn
cjnOspfIfMd5KeyId = _CjnOspfIfMd5KeyId_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 3, 1, 17),
    _CjnOspfIfMd5KeyId_Type()
)
cjnOspfIfMd5KeyId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnOspfIfMd5KeyId.setStatus("current")


class _CjnOspfIfMd5KeyFlags_Type(OctetString):
    """Custom type cjnOspfIfMd5KeyFlags based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_CjnOspfIfMd5KeyFlags_Type.__name__ = "OctetString"
_CjnOspfIfMd5KeyFlags_Object = MibTableColumn
cjnOspfIfMd5KeyFlags = _CjnOspfIfMd5KeyFlags_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 3, 1, 18),
    _CjnOspfIfMd5KeyFlags_Type()
)
cjnOspfIfMd5KeyFlags.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnOspfIfMd5KeyFlags.setStatus("current")


class _CjnOspfIfMd5Key_Type(OctetString):
    """Custom type cjnOspfIfMd5Key based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_CjnOspfIfMd5Key_Type.__name__ = "OctetString"
_CjnOspfIfMd5Key_Object = MibTableColumn
cjnOspfIfMd5Key = _CjnOspfIfMd5Key_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 3, 1, 19),
    _CjnOspfIfMd5Key_Type()
)
cjnOspfIfMd5Key.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnOspfIfMd5Key.setStatus("current")


class _CjnOspfIfAuthType_Type(Integer32):
    """Custom type cjnOspfIfAuthType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("md5", 2),
          ("none", 0),
          ("simple", 1))
    )


_CjnOspfIfAuthType_Type.__name__ = "Integer32"
_CjnOspfIfAuthType_Object = MibTableColumn
cjnOspfIfAuthType = _CjnOspfIfAuthType_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 3, 1, 20),
    _CjnOspfIfAuthType_Type()
)
cjnOspfIfAuthType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnOspfIfAuthType.setStatus("current")
_CjnOspfIfMtu_Type = Integer32
_CjnOspfIfMtu_Object = MibTableColumn
cjnOspfIfMtu = _CjnOspfIfMtu_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 3, 1, 21),
    _CjnOspfIfMtu_Type()
)
cjnOspfIfMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnOspfIfMtu.setStatus("current")


class _CjnOspfIfPollInterval_Type(Integer32):
    """Custom type cjnOspfIfPollInterval based on Integer32"""
    defaultValue = 120


_CjnOspfIfPollInterval_Object = MibTableColumn
cjnOspfIfPollInterval = _CjnOspfIfPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 3, 1, 22),
    _CjnOspfIfPollInterval_Type()
)
cjnOspfIfPollInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnOspfIfPollInterval.setStatus("current")
_CjnOspfVirtIfTable_Object = MibTable
cjnOspfVirtIfTable = _CjnOspfVirtIfTable_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 4)
)
if mibBuilder.loadTexts:
    cjnOspfVirtIfTable.setStatus("current")
_CjnOspfVirtIfEntry_Object = MibTableRow
cjnOspfVirtIfEntry = _CjnOspfVirtIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 4, 1)
)
cjnOspfVirtIfEntry.setIndexNames(
    (0, "OSPF-PRIVATE-MIB", "cjnOspfVirtIfAreaId"),
    (0, "OSPF-PRIVATE-MIB", "cjnOspfVirtIfNbrRtrId"),
)
if mibBuilder.loadTexts:
    cjnOspfVirtIfEntry.setStatus("current")
_CjnOspfVirtIfAreaId_Type = AreaID
_CjnOspfVirtIfAreaId_Object = MibTableColumn
cjnOspfVirtIfAreaId = _CjnOspfVirtIfAreaId_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 4, 1, 1),
    _CjnOspfVirtIfAreaId_Type()
)
cjnOspfVirtIfAreaId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnOspfVirtIfAreaId.setStatus("current")
_CjnOspfVirtIfNbrRtrId_Type = RouterID
_CjnOspfVirtIfNbrRtrId_Object = MibTableColumn
cjnOspfVirtIfNbrRtrId = _CjnOspfVirtIfNbrRtrId_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 4, 1, 2),
    _CjnOspfVirtIfNbrRtrId_Type()
)
cjnOspfVirtIfNbrRtrId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnOspfVirtIfNbrRtrId.setStatus("current")
_CjnOspfVirtIfRowStatus_Type = RowStatus
_CjnOspfVirtIfRowStatus_Object = MibTableColumn
cjnOspfVirtIfRowStatus = _CjnOspfVirtIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 4, 1, 3),
    _CjnOspfVirtIfRowStatus_Type()
)
cjnOspfVirtIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnOspfVirtIfRowStatus.setStatus("current")
_CjnOspfVirtIfDrRouterId_Type = RouterID
_CjnOspfVirtIfDrRouterId_Object = MibTableColumn
cjnOspfVirtIfDrRouterId = _CjnOspfVirtIfDrRouterId_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 4, 1, 4),
    _CjnOspfVirtIfDrRouterId_Type()
)
cjnOspfVirtIfDrRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnOspfVirtIfDrRouterId.setStatus("current")
_CjnOspfVirtIfDrIpAddr_Type = IpAddress
_CjnOspfVirtIfDrIpAddr_Object = MibTableColumn
cjnOspfVirtIfDrIpAddr = _CjnOspfVirtIfDrIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 4, 1, 5),
    _CjnOspfVirtIfDrIpAddr_Type()
)
cjnOspfVirtIfDrIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnOspfVirtIfDrIpAddr.setStatus("current")
_CjnOspfVirtIfBDrRouterId_Type = RouterID
_CjnOspfVirtIfBDrRouterId_Object = MibTableColumn
cjnOspfVirtIfBDrRouterId = _CjnOspfVirtIfBDrRouterId_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 4, 1, 6),
    _CjnOspfVirtIfBDrRouterId_Type()
)
cjnOspfVirtIfBDrRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnOspfVirtIfBDrRouterId.setStatus("current")


class _CjnOspfVirtIfDrState_Type(Integer32):
    """Custom type cjnOspfVirtIfDrState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("backupDesignatedRouter", 3),
          ("desigatedRouter", 2),
          ("notDesignatedRouter", 1))
    )


_CjnOspfVirtIfDrState_Type.__name__ = "Integer32"
_CjnOspfVirtIfDrState_Object = MibTableColumn
cjnOspfVirtIfDrState = _CjnOspfVirtIfDrState_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 4, 1, 7),
    _CjnOspfVirtIfDrState_Type()
)
cjnOspfVirtIfDrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnOspfVirtIfDrState.setStatus("current")
_CjnOspfVirtIfHelloTimer_Type = Integer32
_CjnOspfVirtIfHelloTimer_Object = MibTableColumn
cjnOspfVirtIfHelloTimer = _CjnOspfVirtIfHelloTimer_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 4, 1, 8),
    _CjnOspfVirtIfHelloTimer_Type()
)
cjnOspfVirtIfHelloTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnOspfVirtIfHelloTimer.setStatus("current")
_CjnOspfVirtIfDeadInterval_Type = Integer32
_CjnOspfVirtIfDeadInterval_Object = MibTableColumn
cjnOspfVirtIfDeadInterval = _CjnOspfVirtIfDeadInterval_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 4, 1, 9),
    _CjnOspfVirtIfDeadInterval_Type()
)
cjnOspfVirtIfDeadInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnOspfVirtIfDeadInterval.setStatus("current")
_CjnOspfVirtIfRtrPriority_Type = Integer32
_CjnOspfVirtIfRtrPriority_Object = MibTableColumn
cjnOspfVirtIfRtrPriority = _CjnOspfVirtIfRtrPriority_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 4, 1, 10),
    _CjnOspfVirtIfRtrPriority_Type()
)
cjnOspfVirtIfRtrPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnOspfVirtIfRtrPriority.setStatus("current")
_CjnOspfVirtIfRxmtTimer_Type = Integer32
_CjnOspfVirtIfRxmtTimer_Object = MibTableColumn
cjnOspfVirtIfRxmtTimer = _CjnOspfVirtIfRxmtTimer_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 4, 1, 11),
    _CjnOspfVirtIfRxmtTimer_Type()
)
cjnOspfVirtIfRxmtTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnOspfVirtIfRxmtTimer.setStatus("current")
_CjnOspfVirtIfTransitDelay_Type = Integer32
_CjnOspfVirtIfTransitDelay_Object = MibTableColumn
cjnOspfVirtIfTransitDelay = _CjnOspfVirtIfTransitDelay_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 4, 1, 12),
    _CjnOspfVirtIfTransitDelay_Type()
)
cjnOspfVirtIfTransitDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnOspfVirtIfTransitDelay.setStatus("current")


class _CjnOspfVirtIfAuthKey_Type(OctetString):
    """Custom type cjnOspfVirtIfAuthKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_CjnOspfVirtIfAuthKey_Type.__name__ = "OctetString"
_CjnOspfVirtIfAuthKey_Object = MibTableColumn
cjnOspfVirtIfAuthKey = _CjnOspfVirtIfAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 4, 1, 13),
    _CjnOspfVirtIfAuthKey_Type()
)
cjnOspfVirtIfAuthKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnOspfVirtIfAuthKey.setStatus("current")


class _CjnOspfVirtIfMd5Key_Type(OctetString):
    """Custom type cjnOspfVirtIfMd5Key based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_CjnOspfVirtIfMd5Key_Type.__name__ = "OctetString"
_CjnOspfVirtIfMd5Key_Object = MibTableColumn
cjnOspfVirtIfMd5Key = _CjnOspfVirtIfMd5Key_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 4, 1, 14),
    _CjnOspfVirtIfMd5Key_Type()
)
cjnOspfVirtIfMd5Key.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnOspfVirtIfMd5Key.setStatus("current")
_CjnOspfVirtIfMd5KeyId_Type = Integer32
_CjnOspfVirtIfMd5KeyId_Object = MibTableColumn
cjnOspfVirtIfMd5KeyId = _CjnOspfVirtIfMd5KeyId_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 4, 1, 15),
    _CjnOspfVirtIfMd5KeyId_Type()
)
cjnOspfVirtIfMd5KeyId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnOspfVirtIfMd5KeyId.setStatus("current")


class _CjnOspfVirtIfMd5KeyFlags_Type(OctetString):
    """Custom type cjnOspfVirtIfMd5KeyFlags based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_CjnOspfVirtIfMd5KeyFlags_Type.__name__ = "OctetString"
_CjnOspfVirtIfMd5KeyFlags_Object = MibTableColumn
cjnOspfVirtIfMd5KeyFlags = _CjnOspfVirtIfMd5KeyFlags_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 4, 1, 16),
    _CjnOspfVirtIfMd5KeyFlags_Type()
)
cjnOspfVirtIfMd5KeyFlags.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnOspfVirtIfMd5KeyFlags.setStatus("current")


class _CjnOspfVirtIfAuthType_Type(Integer32):
    """Custom type cjnOspfVirtIfAuthType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("md5", 2),
          ("none", 0),
          ("simple", 1))
    )


_CjnOspfVirtIfAuthType_Type.__name__ = "Integer32"
_CjnOspfVirtIfAuthType_Object = MibTableColumn
cjnOspfVirtIfAuthType = _CjnOspfVirtIfAuthType_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 4, 1, 17),
    _CjnOspfVirtIfAuthType_Type()
)
cjnOspfVirtIfAuthType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnOspfVirtIfAuthType.setStatus("current")
_CjnOspfAreaTable_Object = MibTable
cjnOspfAreaTable = _CjnOspfAreaTable_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 5)
)
if mibBuilder.loadTexts:
    cjnOspfAreaTable.setStatus("current")
_CjnOspfAreaEntry_Object = MibTableRow
cjnOspfAreaEntry = _CjnOspfAreaEntry_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 5, 1)
)
cjnOspfAreaEntry.setIndexNames(
    (0, "OSPF-PRIVATE-MIB", "cjnOspfAreaId"),
)
if mibBuilder.loadTexts:
    cjnOspfAreaEntry.setStatus("current")
_CjnOspfAreaId_Type = AreaID
_CjnOspfAreaId_Object = MibTableColumn
cjnOspfAreaId = _CjnOspfAreaId_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 5, 1, 1),
    _CjnOspfAreaId_Type()
)
cjnOspfAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnOspfAreaId.setStatus("current")
_CjnOspfAreaRowStatus_Type = RowStatus
_CjnOspfAreaRowStatus_Object = MibTableColumn
cjnOspfAreaRowStatus = _CjnOspfAreaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 5, 1, 2),
    _CjnOspfAreaRowStatus_Type()
)
cjnOspfAreaRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnOspfAreaRowStatus.setStatus("current")


class _CjnOspfAreaType_Type(Integer32):
    """Custom type cjnOspfAreaType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nonStub", 0),
          ("nssa", 2),
          ("stub", 1))
    )


_CjnOspfAreaType_Type.__name__ = "Integer32"
_CjnOspfAreaType_Object = MibTableColumn
cjnOspfAreaType = _CjnOspfAreaType_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 5, 1, 3),
    _CjnOspfAreaType_Type()
)
cjnOspfAreaType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnOspfAreaType.setStatus("current")


class _CjnOspfAreaTranslate_Type(Integer32):
    """Custom type cjnOspfAreaTranslate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noTranslation", 0),
          ("translate", 1))
    )


_CjnOspfAreaTranslate_Type.__name__ = "Integer32"
_CjnOspfAreaTranslate_Object = MibTableColumn
cjnOspfAreaTranslate = _CjnOspfAreaTranslate_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 5, 1, 4),
    _CjnOspfAreaTranslate_Type()
)
cjnOspfAreaTranslate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnOspfAreaTranslate.setStatus("current")
_CjnOspfAreaStubCost_Type = Integer32
_CjnOspfAreaStubCost_Object = MibTableColumn
cjnOspfAreaStubCost = _CjnOspfAreaStubCost_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 5, 1, 5),
    _CjnOspfAreaStubCost_Type()
)
cjnOspfAreaStubCost.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnOspfAreaStubCost.setStatus("current")


class _CjnOspfAreaT3Filter_Type(Integer32):
    """Custom type cjnOspfAreaT3Filter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("filter", 1),
          ("noFiltering", 0))
    )


_CjnOspfAreaT3Filter_Type.__name__ = "Integer32"
_CjnOspfAreaT3Filter_Object = MibTableColumn
cjnOspfAreaT3Filter = _CjnOspfAreaT3Filter_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 5, 1, 6),
    _CjnOspfAreaT3Filter_Type()
)
cjnOspfAreaT3Filter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnOspfAreaT3Filter.setStatus("current")
_CjnOspfAreaSpfRuns_Type = Integer32
_CjnOspfAreaSpfRuns_Object = MibTableColumn
cjnOspfAreaSpfRuns = _CjnOspfAreaSpfRuns_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 5, 1, 7),
    _CjnOspfAreaSpfRuns_Type()
)
cjnOspfAreaSpfRuns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnOspfAreaSpfRuns.setStatus("current")
_CjnOspfAreaAbdrCnt_Type = Integer32
_CjnOspfAreaAbdrCnt_Object = MibTableColumn
cjnOspfAreaAbdrCnt = _CjnOspfAreaAbdrCnt_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 5, 1, 8),
    _CjnOspfAreaAbdrCnt_Type()
)
cjnOspfAreaAbdrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnOspfAreaAbdrCnt.setStatus("current")
_CjnOspfAreaAsbdrCnt_Type = Integer32
_CjnOspfAreaAsbdrCnt_Object = MibTableColumn
cjnOspfAreaAsbdrCnt = _CjnOspfAreaAsbdrCnt_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 5, 1, 9),
    _CjnOspfAreaAsbdrCnt_Type()
)
cjnOspfAreaAsbdrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnOspfAreaAsbdrCnt.setStatus("current")
_CjnOspfAreaNetCnt_Type = Integer32
_CjnOspfAreaNetCnt_Object = MibTableColumn
cjnOspfAreaNetCnt = _CjnOspfAreaNetCnt_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 5, 1, 10),
    _CjnOspfAreaNetCnt_Type()
)
cjnOspfAreaNetCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnOspfAreaNetCnt.setStatus("current")
_CjnOspfCnfgRangeTable_Object = MibTable
cjnOspfCnfgRangeTable = _CjnOspfCnfgRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 6)
)
if mibBuilder.loadTexts:
    cjnOspfCnfgRangeTable.setStatus("obsolete")
_CjnOspfCnfgRangeEntry_Object = MibTableRow
cjnOspfCnfgRangeEntry = _CjnOspfCnfgRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 6, 1)
)
cjnOspfCnfgRangeEntry.setIndexNames(
    (0, "OSPF-PRIVATE-MIB", "cjnOspfCnfgRangeAreaId"),
    (0, "OSPF-PRIVATE-MIB", "cjnOspfCnfgRangeIpAddr"),
    (0, "OSPF-PRIVATE-MIB", "cjnOspfCnfgRangeMask"),
)
if mibBuilder.loadTexts:
    cjnOspfCnfgRangeEntry.setStatus("obsolete")
_CjnOspfCnfgRangeAreaId_Type = AreaID
_CjnOspfCnfgRangeAreaId_Object = MibTableColumn
cjnOspfCnfgRangeAreaId = _CjnOspfCnfgRangeAreaId_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 6, 1, 1),
    _CjnOspfCnfgRangeAreaId_Type()
)
cjnOspfCnfgRangeAreaId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnOspfCnfgRangeAreaId.setStatus("current")
_CjnOspfCnfgRangeIpAddr_Type = IpAddress
_CjnOspfCnfgRangeIpAddr_Object = MibTableColumn
cjnOspfCnfgRangeIpAddr = _CjnOspfCnfgRangeIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 6, 1, 2),
    _CjnOspfCnfgRangeIpAddr_Type()
)
cjnOspfCnfgRangeIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnOspfCnfgRangeIpAddr.setStatus("current")
_CjnOspfCnfgRangeMask_Type = IpAddress
_CjnOspfCnfgRangeMask_Object = MibTableColumn
cjnOspfCnfgRangeMask = _CjnOspfCnfgRangeMask_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 6, 1, 3),
    _CjnOspfCnfgRangeMask_Type()
)
cjnOspfCnfgRangeMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnOspfCnfgRangeMask.setStatus("current")
_CjnOspfCnfgRowStatus_Type = RowStatus
_CjnOspfCnfgRowStatus_Object = MibTableColumn
cjnOspfCnfgRowStatus = _CjnOspfCnfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 6, 1, 4),
    _CjnOspfCnfgRowStatus_Type()
)
cjnOspfCnfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnOspfCnfgRowStatus.setStatus("current")


class _CjnOspfCnfgRangeAdv_Type(Integer32):
    """Custom type cjnOspfCnfgRangeAdv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("advertising", 1),
          ("notAdvertising", 0))
    )


_CjnOspfCnfgRangeAdv_Type.__name__ = "Integer32"
_CjnOspfCnfgRangeAdv_Object = MibTableColumn
cjnOspfCnfgRangeAdv = _CjnOspfCnfgRangeAdv_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 6, 1, 5),
    _CjnOspfCnfgRangeAdv_Type()
)
cjnOspfCnfgRangeAdv.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnOspfCnfgRangeAdv.setStatus("current")
_CjnOspfNbrTable_Object = MibTable
cjnOspfNbrTable = _CjnOspfNbrTable_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 7)
)
if mibBuilder.loadTexts:
    cjnOspfNbrTable.setStatus("current")
_CjnOspfNbrEntry_Object = MibTableRow
cjnOspfNbrEntry = _CjnOspfNbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 7, 1)
)
cjnOspfNbrEntry.setIndexNames(
    (0, "OSPF-PRIVATE-MIB", "cjnOspfNbrIpAddr"),
)
if mibBuilder.loadTexts:
    cjnOspfNbrEntry.setStatus("current")
_CjnOspfNbrIpAddr_Type = IpAddress
_CjnOspfNbrIpAddr_Object = MibTableColumn
cjnOspfNbrIpAddr = _CjnOspfNbrIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 7, 1, 1),
    _CjnOspfNbrIpAddr_Type()
)
cjnOspfNbrIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnOspfNbrIpAddr.setStatus("current")


class _CjnOspfNbrState_Type(Integer32):
    """Custom type cjnOspfNbrState based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("attempt", 2),
          ("down", 1),
          ("exchange", 6),
          ("exchangeStart", 5),
          ("full", 8),
          ("init", 3),
          ("loading", 7),
          ("twoWay", 4))
    )


_CjnOspfNbrState_Type.__name__ = "Integer32"
_CjnOspfNbrState_Object = MibTableColumn
cjnOspfNbrState = _CjnOspfNbrState_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 7, 1, 2),
    _CjnOspfNbrState_Type()
)
cjnOspfNbrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnOspfNbrState.setStatus("current")
_CjnOspfNbrRtrId_Type = RouterID
_CjnOspfNbrRtrId_Object = MibTableColumn
cjnOspfNbrRtrId = _CjnOspfNbrRtrId_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 7, 1, 3),
    _CjnOspfNbrRtrId_Type()
)
cjnOspfNbrRtrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnOspfNbrRtrId.setStatus("current")


class _CjnOspfNbrMasterSlave_Type(Integer32):
    """Custom type cjnOspfNbrMasterSlave based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("master", 1),
          ("slave", 0))
    )


_CjnOspfNbrMasterSlave_Type.__name__ = "Integer32"
_CjnOspfNbrMasterSlave_Object = MibTableColumn
cjnOspfNbrMasterSlave = _CjnOspfNbrMasterSlave_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 7, 1, 4),
    _CjnOspfNbrMasterSlave_Type()
)
cjnOspfNbrMasterSlave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnOspfNbrMasterSlave.setStatus("current")
_CjnOspfNbrDrIpAddr_Type = Integer32
_CjnOspfNbrDrIpAddr_Object = MibTableColumn
cjnOspfNbrDrIpAddr = _CjnOspfNbrDrIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 7, 1, 5),
    _CjnOspfNbrDrIpAddr_Type()
)
cjnOspfNbrDrIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnOspfNbrDrIpAddr.setStatus("current")
_CjnOspfNbrBackUpIpAddr_Type = IpAddress
_CjnOspfNbrBackUpIpAddr_Object = MibTableColumn
cjnOspfNbrBackUpIpAddr = _CjnOspfNbrBackUpIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 7, 1, 6),
    _CjnOspfNbrBackUpIpAddr_Type()
)
cjnOspfNbrBackUpIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnOspfNbrBackUpIpAddr.setStatus("current")
_CjnOspfNbrDDNum_Type = Integer32
_CjnOspfNbrDDNum_Object = MibTableColumn
cjnOspfNbrDDNum = _CjnOspfNbrDDNum_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 7, 1, 7),
    _CjnOspfNbrDDNum_Type()
)
cjnOspfNbrDDNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnOspfNbrDDNum.setStatus("current")
_CjnOspfLsaHdrTable_Object = MibTable
cjnOspfLsaHdrTable = _CjnOspfLsaHdrTable_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 8)
)
if mibBuilder.loadTexts:
    cjnOspfLsaHdrTable.setStatus("current")
_CjnOspfLsaHdrEntry_Object = MibTableRow
cjnOspfLsaHdrEntry = _CjnOspfLsaHdrEntry_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 8, 1)
)
cjnOspfLsaHdrEntry.setIndexNames(
    (0, "OSPF-PRIVATE-MIB", "cjnOspfLsaHdrAreaId"),
    (0, "OSPF-PRIVATE-MIB", "cjnOspfLsaHdrLsaType"),
    (0, "OSPF-PRIVATE-MIB", "cjnOspfLsaHdrAdvRtrId"),
    (0, "OSPF-PRIVATE-MIB", "cjnOspfLsaHdrLsId"),
)
if mibBuilder.loadTexts:
    cjnOspfLsaHdrEntry.setStatus("current")
_CjnOspfLsaHdrAreaId_Type = AreaID
_CjnOspfLsaHdrAreaId_Object = MibTableColumn
cjnOspfLsaHdrAreaId = _CjnOspfLsaHdrAreaId_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 8, 1, 1),
    _CjnOspfLsaHdrAreaId_Type()
)
cjnOspfLsaHdrAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnOspfLsaHdrAreaId.setStatus("current")
_CjnOspfLsaHdrLsaType_Type = Integer32
_CjnOspfLsaHdrLsaType_Object = MibTableColumn
cjnOspfLsaHdrLsaType = _CjnOspfLsaHdrLsaType_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 8, 1, 2),
    _CjnOspfLsaHdrLsaType_Type()
)
cjnOspfLsaHdrLsaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnOspfLsaHdrLsaType.setStatus("current")
_CjnOspfLsaHdrAdvRtrId_Type = IpAddress
_CjnOspfLsaHdrAdvRtrId_Object = MibTableColumn
cjnOspfLsaHdrAdvRtrId = _CjnOspfLsaHdrAdvRtrId_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 8, 1, 3),
    _CjnOspfLsaHdrAdvRtrId_Type()
)
cjnOspfLsaHdrAdvRtrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnOspfLsaHdrAdvRtrId.setStatus("current")
_CjnOspfLsaHdrLsId_Type = IpAddress
_CjnOspfLsaHdrLsId_Object = MibTableColumn
cjnOspfLsaHdrLsId = _CjnOspfLsaHdrLsId_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 8, 1, 4),
    _CjnOspfLsaHdrLsId_Type()
)
cjnOspfLsaHdrLsId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnOspfLsaHdrLsId.setStatus("current")
_CjnOspfLsaHdrLsaAge_Type = Integer32
_CjnOspfLsaHdrLsaAge_Object = MibTableColumn
cjnOspfLsaHdrLsaAge = _CjnOspfLsaHdrLsaAge_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 8, 1, 5),
    _CjnOspfLsaHdrLsaAge_Type()
)
cjnOspfLsaHdrLsaAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnOspfLsaHdrLsaAge.setStatus("current")
_CjnOspfLsaHdrChecksum_Type = Integer32
_CjnOspfLsaHdrChecksum_Object = MibTableColumn
cjnOspfLsaHdrChecksum = _CjnOspfLsaHdrChecksum_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 8, 1, 6),
    _CjnOspfLsaHdrChecksum_Type()
)
cjnOspfLsaHdrChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnOspfLsaHdrChecksum.setStatus("current")
_CjnOspfLsaHdrSequence_Type = Integer32
_CjnOspfLsaHdrSequence_Object = MibTableColumn
cjnOspfLsaHdrSequence = _CjnOspfLsaHdrSequence_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 8, 1, 7),
    _CjnOspfLsaHdrSequence_Type()
)
cjnOspfLsaHdrSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnOspfLsaHdrSequence.setStatus("current")
_CjnOspfExtLsdbTable_Object = MibTable
cjnOspfExtLsdbTable = _CjnOspfExtLsdbTable_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 9)
)
if mibBuilder.loadTexts:
    cjnOspfExtLsdbTable.setStatus("current")
_CjnOspfExtLsdbEntry_Object = MibTableRow
cjnOspfExtLsdbEntry = _CjnOspfExtLsdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 9, 1)
)
cjnOspfExtLsdbEntry.setIndexNames(
    (0, "OSPF-PRIVATE-MIB", "cjnOspfExtLsdbType"),
    (0, "OSPF-PRIVATE-MIB", "cjnOspfExtLsdbAdvRtrId"),
    (0, "OSPF-PRIVATE-MIB", "cjnOspfExtLsdbLsId"),
)
if mibBuilder.loadTexts:
    cjnOspfExtLsdbEntry.setStatus("current")
_CjnOspfExtLsdbType_Type = Integer32
_CjnOspfExtLsdbType_Object = MibTableColumn
cjnOspfExtLsdbType = _CjnOspfExtLsdbType_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 9, 1, 1),
    _CjnOspfExtLsdbType_Type()
)
cjnOspfExtLsdbType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnOspfExtLsdbType.setStatus("current")
_CjnOspfExtLsdbAdvRtrId_Type = IpAddress
_CjnOspfExtLsdbAdvRtrId_Object = MibTableColumn
cjnOspfExtLsdbAdvRtrId = _CjnOspfExtLsdbAdvRtrId_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 9, 1, 2),
    _CjnOspfExtLsdbAdvRtrId_Type()
)
cjnOspfExtLsdbAdvRtrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnOspfExtLsdbAdvRtrId.setStatus("current")
_CjnOspfExtLsdbLsId_Type = IpAddress
_CjnOspfExtLsdbLsId_Object = MibTableColumn
cjnOspfExtLsdbLsId = _CjnOspfExtLsdbLsId_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 9, 1, 3),
    _CjnOspfExtLsdbLsId_Type()
)
cjnOspfExtLsdbLsId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnOspfExtLsdbLsId.setStatus("current")
_CjnOspfExtLsdbAge_Type = Integer32
_CjnOspfExtLsdbAge_Object = MibTableColumn
cjnOspfExtLsdbAge = _CjnOspfExtLsdbAge_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 9, 1, 4),
    _CjnOspfExtLsdbAge_Type()
)
cjnOspfExtLsdbAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnOspfExtLsdbAge.setStatus("current")
_CjnOspfExtLsdbLsdbChecksum_Type = Integer32
_CjnOspfExtLsdbLsdbChecksum_Object = MibTableColumn
cjnOspfExtLsdbLsdbChecksum = _CjnOspfExtLsdbLsdbChecksum_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 9, 1, 5),
    _CjnOspfExtLsdbLsdbChecksum_Type()
)
cjnOspfExtLsdbLsdbChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnOspfExtLsdbLsdbChecksum.setStatus("current")
_CjnOspfExtLsdbSequence_Type = Integer32
_CjnOspfExtLsdbSequence_Object = MibTableColumn
cjnOspfExtLsdbSequence = _CjnOspfExtLsdbSequence_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 9, 1, 6),
    _CjnOspfExtLsdbSequence_Type()
)
cjnOspfExtLsdbSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnOspfExtLsdbSequence.setStatus("current")
_CjnOspfExtLsdNetMask_Type = IpAddress
_CjnOspfExtLsdNetMask_Object = MibTableColumn
cjnOspfExtLsdNetMask = _CjnOspfExtLsdNetMask_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 9, 1, 7),
    _CjnOspfExtLsdNetMask_Type()
)
cjnOspfExtLsdNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnOspfExtLsdNetMask.setStatus("current")
_CjnOspfExtLsdbTOS_Type = TOSType
_CjnOspfExtLsdbTOS_Object = MibTableColumn
cjnOspfExtLsdbTOS = _CjnOspfExtLsdbTOS_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 9, 1, 8),
    _CjnOspfExtLsdbTOS_Type()
)
cjnOspfExtLsdbTOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnOspfExtLsdbTOS.setStatus("current")
_CjnOspfExtLsdbMetric_Type = Metric
_CjnOspfExtLsdbMetric_Object = MibTableColumn
cjnOspfExtLsdbMetric = _CjnOspfExtLsdbMetric_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 9, 1, 9),
    _CjnOspfExtLsdbMetric_Type()
)
cjnOspfExtLsdbMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnOspfExtLsdbMetric.setStatus("current")
_CjnOspfExtLsdForwardingAddress_Type = IpAddress
_CjnOspfExtLsdForwardingAddress_Object = MibTableColumn
cjnOspfExtLsdForwardingAddress = _CjnOspfExtLsdForwardingAddress_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 9, 1, 10),
    _CjnOspfExtLsdForwardingAddress_Type()
)
cjnOspfExtLsdForwardingAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnOspfExtLsdForwardingAddress.setStatus("current")
_CjnOspfExtLsdbRouteTag_Type = IpAddress
_CjnOspfExtLsdbRouteTag_Object = MibTableColumn
cjnOspfExtLsdbRouteTag = _CjnOspfExtLsdbRouteTag_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 9, 1, 11),
    _CjnOspfExtLsdbRouteTag_Type()
)
cjnOspfExtLsdbRouteTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnOspfExtLsdbRouteTag.setStatus("current")
_CjnOspfNetLsdbTable_Object = MibTable
cjnOspfNetLsdbTable = _CjnOspfNetLsdbTable_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 10)
)
if mibBuilder.loadTexts:
    cjnOspfNetLsdbTable.setStatus("current")
_CjnOspfNetLsdbEntry_Object = MibTableRow
cjnOspfNetLsdbEntry = _CjnOspfNetLsdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 10, 1)
)
cjnOspfNetLsdbEntry.setIndexNames(
    (0, "OSPF-PRIVATE-MIB", "cjnOspfNetLsdbAreaId"),
    (0, "OSPF-PRIVATE-MIB", "cjnOspfNetLsdbType"),
    (0, "OSPF-PRIVATE-MIB", "cjnOspfNetLsdbAdvRtrId"),
    (0, "OSPF-PRIVATE-MIB", "cjnOspfNetLsdbLsId"),
)
if mibBuilder.loadTexts:
    cjnOspfNetLsdbEntry.setStatus("current")
_CjnOspfNetLsdbAreaId_Type = AreaID
_CjnOspfNetLsdbAreaId_Object = MibTableColumn
cjnOspfNetLsdbAreaId = _CjnOspfNetLsdbAreaId_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 10, 1, 1),
    _CjnOspfNetLsdbAreaId_Type()
)
cjnOspfNetLsdbAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnOspfNetLsdbAreaId.setStatus("current")
_CjnOspfNetLsdbType_Type = Integer32
_CjnOspfNetLsdbType_Object = MibTableColumn
cjnOspfNetLsdbType = _CjnOspfNetLsdbType_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 10, 1, 2),
    _CjnOspfNetLsdbType_Type()
)
cjnOspfNetLsdbType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnOspfNetLsdbType.setStatus("current")
_CjnOspfNetLsdbAdvRtrId_Type = IpAddress
_CjnOspfNetLsdbAdvRtrId_Object = MibTableColumn
cjnOspfNetLsdbAdvRtrId = _CjnOspfNetLsdbAdvRtrId_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 10, 1, 3),
    _CjnOspfNetLsdbAdvRtrId_Type()
)
cjnOspfNetLsdbAdvRtrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnOspfNetLsdbAdvRtrId.setStatus("current")
_CjnOspfNetLsdbLsId_Type = IpAddress
_CjnOspfNetLsdbLsId_Object = MibTableColumn
cjnOspfNetLsdbLsId = _CjnOspfNetLsdbLsId_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 10, 1, 4),
    _CjnOspfNetLsdbLsId_Type()
)
cjnOspfNetLsdbLsId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnOspfNetLsdbLsId.setStatus("current")
_CjnOspfNetLsdbAge_Type = Integer32
_CjnOspfNetLsdbAge_Object = MibTableColumn
cjnOspfNetLsdbAge = _CjnOspfNetLsdbAge_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 10, 1, 5),
    _CjnOspfNetLsdbAge_Type()
)
cjnOspfNetLsdbAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnOspfNetLsdbAge.setStatus("current")
_CjnOspfNetLsdbLsdbChecksum_Type = Integer32
_CjnOspfNetLsdbLsdbChecksum_Object = MibTableColumn
cjnOspfNetLsdbLsdbChecksum = _CjnOspfNetLsdbLsdbChecksum_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 10, 1, 6),
    _CjnOspfNetLsdbLsdbChecksum_Type()
)
cjnOspfNetLsdbLsdbChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnOspfNetLsdbLsdbChecksum.setStatus("current")
_CjnOspfNetLsdbSequence_Type = Integer32
_CjnOspfNetLsdbSequence_Object = MibTableColumn
cjnOspfNetLsdbSequence = _CjnOspfNetLsdbSequence_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 10, 1, 7),
    _CjnOspfNetLsdbSequence_Type()
)
cjnOspfNetLsdbSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnOspfNetLsdbSequence.setStatus("current")
_CjnOspfNetLsdNetMask_Type = IpAddress
_CjnOspfNetLsdNetMask_Object = MibTableColumn
cjnOspfNetLsdNetMask = _CjnOspfNetLsdNetMask_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 10, 1, 8),
    _CjnOspfNetLsdNetMask_Type()
)
cjnOspfNetLsdNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnOspfNetLsdNetMask.setStatus("current")
_CjnOspfRouterLsdbTable_Object = MibTable
cjnOspfRouterLsdbTable = _CjnOspfRouterLsdbTable_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 11)
)
if mibBuilder.loadTexts:
    cjnOspfRouterLsdbTable.setStatus("current")
_CjnOspfRouterLsdbEntry_Object = MibTableRow
cjnOspfRouterLsdbEntry = _CjnOspfRouterLsdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 11, 1)
)
cjnOspfRouterLsdbEntry.setIndexNames(
    (0, "OSPF-PRIVATE-MIB", "cjnOspfRouterLsdbAreaId"),
    (0, "OSPF-PRIVATE-MIB", "cjnOspfRouterLsdbType"),
    (0, "OSPF-PRIVATE-MIB", "cjnOspfRouterLsdbRtrId"),
    (0, "OSPF-PRIVATE-MIB", "cjnOspfRouterLsdbLsId"),
)
if mibBuilder.loadTexts:
    cjnOspfRouterLsdbEntry.setStatus("current")
_CjnOspfRouterLsdbAreaId_Type = AreaID
_CjnOspfRouterLsdbAreaId_Object = MibTableColumn
cjnOspfRouterLsdbAreaId = _CjnOspfRouterLsdbAreaId_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 11, 1, 1),
    _CjnOspfRouterLsdbAreaId_Type()
)
cjnOspfRouterLsdbAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnOspfRouterLsdbAreaId.setStatus("current")


class _CjnOspfRouterLsdbType_Type(Integer32):
    """Custom type cjnOspfRouterLsdbType based on Integer32"""
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
        *(("bcast", 1),
          ("nbma", 2),
          ("pointToMultiPoint", 4),
          ("pointToPoint", 3))
    )


_CjnOspfRouterLsdbType_Type.__name__ = "Integer32"
_CjnOspfRouterLsdbType_Object = MibTableColumn
cjnOspfRouterLsdbType = _CjnOspfRouterLsdbType_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 11, 1, 2),
    _CjnOspfRouterLsdbType_Type()
)
cjnOspfRouterLsdbType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnOspfRouterLsdbType.setStatus("current")
_CjnOspfRouterLsdbRtrId_Type = IpAddress
_CjnOspfRouterLsdbRtrId_Object = MibTableColumn
cjnOspfRouterLsdbRtrId = _CjnOspfRouterLsdbRtrId_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 11, 1, 3),
    _CjnOspfRouterLsdbRtrId_Type()
)
cjnOspfRouterLsdbRtrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnOspfRouterLsdbRtrId.setStatus("current")
_CjnOspfRouterLsdbLsId_Type = IpAddress
_CjnOspfRouterLsdbLsId_Object = MibTableColumn
cjnOspfRouterLsdbLsId = _CjnOspfRouterLsdbLsId_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 11, 1, 4),
    _CjnOspfRouterLsdbLsId_Type()
)
cjnOspfRouterLsdbLsId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnOspfRouterLsdbLsId.setStatus("current")
_CjnOspfRouterLsdbLinkData_Type = Integer32
_CjnOspfRouterLsdbLinkData_Object = MibTableColumn
cjnOspfRouterLsdbLinkData = _CjnOspfRouterLsdbLinkData_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 11, 1, 5),
    _CjnOspfRouterLsdbLinkData_Type()
)
cjnOspfRouterLsdbLinkData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnOspfRouterLsdbLinkData.setStatus("current")
_CjnOspfRouterLsdbNumOfTos_Type = Integer32
_CjnOspfRouterLsdbNumOfTos_Object = MibTableColumn
cjnOspfRouterLsdbNumOfTos = _CjnOspfRouterLsdbNumOfTos_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 11, 1, 6),
    _CjnOspfRouterLsdbNumOfTos_Type()
)
cjnOspfRouterLsdbNumOfTos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnOspfRouterLsdbNumOfTos.setStatus("current")
_CjnOspfRouterLsdbMet_Type = Integer32
_CjnOspfRouterLsdbMet_Object = MibTableColumn
cjnOspfRouterLsdbMet = _CjnOspfRouterLsdbMet_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 11, 1, 7),
    _CjnOspfRouterLsdbMet_Type()
)
cjnOspfRouterLsdbMet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnOspfRouterLsdbMet.setStatus("current")
_CjnOspfRouterLsaHdrTable_Object = MibTable
cjnOspfRouterLsaHdrTable = _CjnOspfRouterLsaHdrTable_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 12)
)
if mibBuilder.loadTexts:
    cjnOspfRouterLsaHdrTable.setStatus("current")
_CjnOspfRouterLsaHdrEntry_Object = MibTableRow
cjnOspfRouterLsaHdrEntry = _CjnOspfRouterLsaHdrEntry_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 12, 1)
)
cjnOspfRouterLsaHdrEntry.setIndexNames(
    (0, "OSPF-PRIVATE-MIB", "cjnOspfRouterLsaHdrAreaId"),
    (0, "OSPF-PRIVATE-MIB", "cjnOspfRouterLsaHdrType"),
    (0, "OSPF-PRIVATE-MIB", "cjnOspfRouterLsaHdrAdvRtrId"),
    (0, "OSPF-PRIVATE-MIB", "cjnOspfRouterLsaHdrLsId"),
)
if mibBuilder.loadTexts:
    cjnOspfRouterLsaHdrEntry.setStatus("current")
_CjnOspfRouterLsaHdrAreaId_Type = AreaID
_CjnOspfRouterLsaHdrAreaId_Object = MibTableColumn
cjnOspfRouterLsaHdrAreaId = _CjnOspfRouterLsaHdrAreaId_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 12, 1, 1),
    _CjnOspfRouterLsaHdrAreaId_Type()
)
cjnOspfRouterLsaHdrAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnOspfRouterLsaHdrAreaId.setStatus("current")
_CjnOspfRouterLsaHdrType_Type = Integer32
_CjnOspfRouterLsaHdrType_Object = MibTableColumn
cjnOspfRouterLsaHdrType = _CjnOspfRouterLsaHdrType_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 12, 1, 2),
    _CjnOspfRouterLsaHdrType_Type()
)
cjnOspfRouterLsaHdrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnOspfRouterLsaHdrType.setStatus("current")
_CjnOspfRouterLsaHdrAdvRtrId_Type = IpAddress
_CjnOspfRouterLsaHdrAdvRtrId_Object = MibTableColumn
cjnOspfRouterLsaHdrAdvRtrId = _CjnOspfRouterLsaHdrAdvRtrId_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 12, 1, 3),
    _CjnOspfRouterLsaHdrAdvRtrId_Type()
)
cjnOspfRouterLsaHdrAdvRtrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnOspfRouterLsaHdrAdvRtrId.setStatus("current")
_CjnOspfRouterLsaHdrLsId_Type = IpAddress
_CjnOspfRouterLsaHdrLsId_Object = MibTableColumn
cjnOspfRouterLsaHdrLsId = _CjnOspfRouterLsaHdrLsId_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 12, 1, 4),
    _CjnOspfRouterLsaHdrLsId_Type()
)
cjnOspfRouterLsaHdrLsId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnOspfRouterLsaHdrLsId.setStatus("current")
_CjnOspfRouterLsaHdrAge_Type = Integer32
_CjnOspfRouterLsaHdrAge_Object = MibTableColumn
cjnOspfRouterLsaHdrAge = _CjnOspfRouterLsaHdrAge_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 12, 1, 5),
    _CjnOspfRouterLsaHdrAge_Type()
)
cjnOspfRouterLsaHdrAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnOspfRouterLsaHdrAge.setStatus("current")
_CjnOspfRouterLsaHdrChecksum_Type = Integer32
_CjnOspfRouterLsaHdrChecksum_Object = MibTableColumn
cjnOspfRouterLsaHdrChecksum = _CjnOspfRouterLsaHdrChecksum_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 12, 1, 6),
    _CjnOspfRouterLsaHdrChecksum_Type()
)
cjnOspfRouterLsaHdrChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnOspfRouterLsaHdrChecksum.setStatus("current")
_CjnOspfRouterLsaHdrSequence_Type = Integer32
_CjnOspfRouterLsaHdrSequence_Object = MibTableColumn
cjnOspfRouterLsaHdrSequence = _CjnOspfRouterLsaHdrSequence_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 12, 1, 7),
    _CjnOspfRouterLsaHdrSequence_Type()
)
cjnOspfRouterLsaHdrSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnOspfRouterLsaHdrSequence.setStatus("current")
_CjnOspfRouterLsaHdrFlags_Type = Integer32
_CjnOspfRouterLsaHdrFlags_Object = MibTableColumn
cjnOspfRouterLsaHdrFlags = _CjnOspfRouterLsaHdrFlags_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 12, 1, 8),
    _CjnOspfRouterLsaHdrFlags_Type()
)
cjnOspfRouterLsaHdrFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnOspfRouterLsaHdrFlags.setStatus("current")
_CjnOspfRouterLsaHdrLinkCount_Type = Integer32
_CjnOspfRouterLsaHdrLinkCount_Object = MibTableColumn
cjnOspfRouterLsaHdrLinkCount = _CjnOspfRouterLsaHdrLinkCount_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 12, 1, 9),
    _CjnOspfRouterLsaHdrLinkCount_Type()
)
cjnOspfRouterLsaHdrLinkCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnOspfRouterLsaHdrLinkCount.setStatus("current")
_CjnOspfSumLsaTable_Object = MibTable
cjnOspfSumLsaTable = _CjnOspfSumLsaTable_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 13)
)
if mibBuilder.loadTexts:
    cjnOspfSumLsaTable.setStatus("current")
_CjnOspfSumLsaEntry_Object = MibTableRow
cjnOspfSumLsaEntry = _CjnOspfSumLsaEntry_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 13, 1)
)
cjnOspfSumLsaEntry.setIndexNames(
    (0, "OSPF-PRIVATE-MIB", "cjnOspfSumLsaType"),
    (0, "OSPF-PRIVATE-MIB", "cjnOspfSumLsaAdvRtrId"),
    (0, "OSPF-PRIVATE-MIB", "cjnOspfSumLsaLsId"),
)
if mibBuilder.loadTexts:
    cjnOspfSumLsaEntry.setStatus("current")
_CjnOspfSumLsaType_Type = Integer32
_CjnOspfSumLsaType_Object = MibTableColumn
cjnOspfSumLsaType = _CjnOspfSumLsaType_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 13, 1, 1),
    _CjnOspfSumLsaType_Type()
)
cjnOspfSumLsaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnOspfSumLsaType.setStatus("current")
_CjnOspfSumLsaAdvRtrId_Type = IpAddress
_CjnOspfSumLsaAdvRtrId_Object = MibTableColumn
cjnOspfSumLsaAdvRtrId = _CjnOspfSumLsaAdvRtrId_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 13, 1, 2),
    _CjnOspfSumLsaAdvRtrId_Type()
)
cjnOspfSumLsaAdvRtrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnOspfSumLsaAdvRtrId.setStatus("current")
_CjnOspfSumLsaLsId_Type = IpAddress
_CjnOspfSumLsaLsId_Object = MibTableColumn
cjnOspfSumLsaLsId = _CjnOspfSumLsaLsId_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 13, 1, 3),
    _CjnOspfSumLsaLsId_Type()
)
cjnOspfSumLsaLsId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnOspfSumLsaLsId.setStatus("current")
_CjnOspfSumLsaLsdbAge_Type = Integer32
_CjnOspfSumLsaLsdbAge_Object = MibTableColumn
cjnOspfSumLsaLsdbAge = _CjnOspfSumLsaLsdbAge_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 13, 1, 4),
    _CjnOspfSumLsaLsdbAge_Type()
)
cjnOspfSumLsaLsdbAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnOspfSumLsaLsdbAge.setStatus("current")
_CjnOspfSumLsaChecksum_Type = Integer32
_CjnOspfSumLsaChecksum_Object = MibTableColumn
cjnOspfSumLsaChecksum = _CjnOspfSumLsaChecksum_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 13, 1, 5),
    _CjnOspfSumLsaChecksum_Type()
)
cjnOspfSumLsaChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnOspfSumLsaChecksum.setStatus("current")
_CjnOspfSumLsaSequence_Type = Integer32
_CjnOspfSumLsaSequence_Object = MibTableColumn
cjnOspfSumLsaSequence = _CjnOspfSumLsaSequence_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 13, 1, 6),
    _CjnOspfSumLsaSequence_Type()
)
cjnOspfSumLsaSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnOspfSumLsaSequence.setStatus("current")
_CjnOspfSumLsaMask_Type = IpAddress
_CjnOspfSumLsaMask_Object = MibTableColumn
cjnOspfSumLsaMask = _CjnOspfSumLsaMask_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 13, 1, 7),
    _CjnOspfSumLsaMask_Type()
)
cjnOspfSumLsaMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnOspfSumLsaMask.setStatus("current")
_CjnOspfSumLsaTOS_Type = TOSType
_CjnOspfSumLsaTOS_Object = MibTableColumn
cjnOspfSumLsaTOS = _CjnOspfSumLsaTOS_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 13, 1, 8),
    _CjnOspfSumLsaTOS_Type()
)
cjnOspfSumLsaTOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnOspfSumLsaTOS.setStatus("current")
_CjnOspfSumLsaMetric_Type = Metric
_CjnOspfSumLsaMetric_Object = MibTableColumn
cjnOspfSumLsaMetric = _CjnOspfSumLsaMetric_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9, 13, 1, 9),
    _CjnOspfSumLsaMetric_Type()
)
cjnOspfSumLsaMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnOspfSumLsaMetric.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OSPF-PRIVATE-MIB",
    **{"cjnOspf": cjnOspf,
       "cjnOspfGblConfGroup": cjnOspfGblConfGroup,
       "cjnOspfRouterId": cjnOspfRouterId,
       "cjnOspfPathSplit": cjnOspfPathSplit,
       "cjnOspfPeMax": cjnOspfPeMax,
       "cjnOspfSpfState": cjnOspfSpfState,
       "cjnOspfAsbdrStatus": cjnOspfAsbdrStatus,
       "cjnOspfAutoVLinkCreate": cjnOspfAutoVLinkCreate,
       "cjnOspfSpfHold": cjnOspfSpfHold,
       "cjnOspfSpfSuspendTime": cjnOspfSpfSuspendTime,
       "cjnOspfLocalExtType": cjnOspfLocalExtType,
       "cjnOspfRipExtType": cjnOspfRipExtType,
       "cjnOspfSpfStaticExtType": cjnOspfSpfStaticExtType,
       "cjnOspfLowExtType": cjnOspfLowExtType,
       "cjnOspfTraceFlags": cjnOspfTraceFlags,
       "cjnOspfGlobalStatsReset": cjnOspfGlobalStatsReset,
       "cjnOspfGblStatsGroup": cjnOspfGblStatsGroup,
       "cjnOspfTOSCount": cjnOspfTOSCount,
       "cjnOspfRunSpf": cjnOspfRunSpf,
       "cjnOspfAbdrStatus": cjnOspfAbdrStatus,
       "cjnOspfTxNewLsa": cjnOspfTxNewLsa,
       "cjnOspfRxNewLsa": cjnOspfRxNewLsa,
       "cjnOspfRxHelloCnt": cjnOspfRxHelloCnt,
       "cjnOspfTxHelloCnt": cjnOspfTxHelloCnt,
       "cjnOspfRxDBDescCnt": cjnOspfRxDBDescCnt,
       "cjnOspfTxDBDescCnt": cjnOspfTxDBDescCnt,
       "cjnOspfRxLsaAckCnt": cjnOspfRxLsaAckCnt,
       "cjnOspfTxLsaAckCnt": cjnOspfTxLsaAckCnt,
       "cjnOspfRxLsaUpdCnt": cjnOspfRxLsaUpdCnt,
       "cjnOspfTxLsaUpdCnt": cjnOspfTxLsaUpdCnt,
       "cjnOspfRxLsaReqCnt": cjnOspfRxLsaReqCnt,
       "cjnOspfTxLsaReqCnt": cjnOspfTxLsaReqCnt,
       "cjnOspfIfTable": cjnOspfIfTable,
       "cjnOspfIfEntry": cjnOspfIfEntry,
       "cjnOspfIfIpAddress": cjnOspfIfIpAddress,
       "cjnOspfIfRowStatus": cjnOspfIfRowStatus,
       "cjnOspfIfAreaId": cjnOspfIfAreaId,
       "cjnOspfIfMask": cjnOspfIfMask,
       "cjnOspfIfType": cjnOspfIfType,
       "cjnOspfIfCost": cjnOspfIfCost,
       "cjnOspfIfDrRouterId": cjnOspfIfDrRouterId,
       "cjnOspfIfDrIpAddr": cjnOspfIfDrIpAddr,
       "cjnOspfIfBDrRouterId": cjnOspfIfBDrRouterId,
       "cjnOspfIfDrState": cjnOspfIfDrState,
       "cjnOspfIfHelloTimer": cjnOspfIfHelloTimer,
       "cjnOspfIfDeadInterval": cjnOspfIfDeadInterval,
       "cjnOspfIfRtrPriority": cjnOspfIfRtrPriority,
       "cjnOspfIfRxmtTimer": cjnOspfIfRxmtTimer,
       "cjnOspfIfTransitDelay": cjnOspfIfTransitDelay,
       "cjnOspfIfAuthKey": cjnOspfIfAuthKey,
       "cjnOspfIfMd5KeyId": cjnOspfIfMd5KeyId,
       "cjnOspfIfMd5KeyFlags": cjnOspfIfMd5KeyFlags,
       "cjnOspfIfMd5Key": cjnOspfIfMd5Key,
       "cjnOspfIfAuthType": cjnOspfIfAuthType,
       "cjnOspfIfMtu": cjnOspfIfMtu,
       "cjnOspfIfPollInterval": cjnOspfIfPollInterval,
       "cjnOspfVirtIfTable": cjnOspfVirtIfTable,
       "cjnOspfVirtIfEntry": cjnOspfVirtIfEntry,
       "cjnOspfVirtIfAreaId": cjnOspfVirtIfAreaId,
       "cjnOspfVirtIfNbrRtrId": cjnOspfVirtIfNbrRtrId,
       "cjnOspfVirtIfRowStatus": cjnOspfVirtIfRowStatus,
       "cjnOspfVirtIfDrRouterId": cjnOspfVirtIfDrRouterId,
       "cjnOspfVirtIfDrIpAddr": cjnOspfVirtIfDrIpAddr,
       "cjnOspfVirtIfBDrRouterId": cjnOspfVirtIfBDrRouterId,
       "cjnOspfVirtIfDrState": cjnOspfVirtIfDrState,
       "cjnOspfVirtIfHelloTimer": cjnOspfVirtIfHelloTimer,
       "cjnOspfVirtIfDeadInterval": cjnOspfVirtIfDeadInterval,
       "cjnOspfVirtIfRtrPriority": cjnOspfVirtIfRtrPriority,
       "cjnOspfVirtIfRxmtTimer": cjnOspfVirtIfRxmtTimer,
       "cjnOspfVirtIfTransitDelay": cjnOspfVirtIfTransitDelay,
       "cjnOspfVirtIfAuthKey": cjnOspfVirtIfAuthKey,
       "cjnOspfVirtIfMd5Key": cjnOspfVirtIfMd5Key,
       "cjnOspfVirtIfMd5KeyId": cjnOspfVirtIfMd5KeyId,
       "cjnOspfVirtIfMd5KeyFlags": cjnOspfVirtIfMd5KeyFlags,
       "cjnOspfVirtIfAuthType": cjnOspfVirtIfAuthType,
       "cjnOspfAreaTable": cjnOspfAreaTable,
       "cjnOspfAreaEntry": cjnOspfAreaEntry,
       "cjnOspfAreaId": cjnOspfAreaId,
       "cjnOspfAreaRowStatus": cjnOspfAreaRowStatus,
       "cjnOspfAreaType": cjnOspfAreaType,
       "cjnOspfAreaTranslate": cjnOspfAreaTranslate,
       "cjnOspfAreaStubCost": cjnOspfAreaStubCost,
       "cjnOspfAreaT3Filter": cjnOspfAreaT3Filter,
       "cjnOspfAreaSpfRuns": cjnOspfAreaSpfRuns,
       "cjnOspfAreaAbdrCnt": cjnOspfAreaAbdrCnt,
       "cjnOspfAreaAsbdrCnt": cjnOspfAreaAsbdrCnt,
       "cjnOspfAreaNetCnt": cjnOspfAreaNetCnt,
       "cjnOspfCnfgRangeTable": cjnOspfCnfgRangeTable,
       "cjnOspfCnfgRangeEntry": cjnOspfCnfgRangeEntry,
       "cjnOspfCnfgRangeAreaId": cjnOspfCnfgRangeAreaId,
       "cjnOspfCnfgRangeIpAddr": cjnOspfCnfgRangeIpAddr,
       "cjnOspfCnfgRangeMask": cjnOspfCnfgRangeMask,
       "cjnOspfCnfgRowStatus": cjnOspfCnfgRowStatus,
       "cjnOspfCnfgRangeAdv": cjnOspfCnfgRangeAdv,
       "cjnOspfNbrTable": cjnOspfNbrTable,
       "cjnOspfNbrEntry": cjnOspfNbrEntry,
       "cjnOspfNbrIpAddr": cjnOspfNbrIpAddr,
       "cjnOspfNbrState": cjnOspfNbrState,
       "cjnOspfNbrRtrId": cjnOspfNbrRtrId,
       "cjnOspfNbrMasterSlave": cjnOspfNbrMasterSlave,
       "cjnOspfNbrDrIpAddr": cjnOspfNbrDrIpAddr,
       "cjnOspfNbrBackUpIpAddr": cjnOspfNbrBackUpIpAddr,
       "cjnOspfNbrDDNum": cjnOspfNbrDDNum,
       "cjnOspfLsaHdrTable": cjnOspfLsaHdrTable,
       "cjnOspfLsaHdrEntry": cjnOspfLsaHdrEntry,
       "cjnOspfLsaHdrAreaId": cjnOspfLsaHdrAreaId,
       "cjnOspfLsaHdrLsaType": cjnOspfLsaHdrLsaType,
       "cjnOspfLsaHdrAdvRtrId": cjnOspfLsaHdrAdvRtrId,
       "cjnOspfLsaHdrLsId": cjnOspfLsaHdrLsId,
       "cjnOspfLsaHdrLsaAge": cjnOspfLsaHdrLsaAge,
       "cjnOspfLsaHdrChecksum": cjnOspfLsaHdrChecksum,
       "cjnOspfLsaHdrSequence": cjnOspfLsaHdrSequence,
       "cjnOspfExtLsdbTable": cjnOspfExtLsdbTable,
       "cjnOspfExtLsdbEntry": cjnOspfExtLsdbEntry,
       "cjnOspfExtLsdbType": cjnOspfExtLsdbType,
       "cjnOspfExtLsdbAdvRtrId": cjnOspfExtLsdbAdvRtrId,
       "cjnOspfExtLsdbLsId": cjnOspfExtLsdbLsId,
       "cjnOspfExtLsdbAge": cjnOspfExtLsdbAge,
       "cjnOspfExtLsdbLsdbChecksum": cjnOspfExtLsdbLsdbChecksum,
       "cjnOspfExtLsdbSequence": cjnOspfExtLsdbSequence,
       "cjnOspfExtLsdNetMask": cjnOspfExtLsdNetMask,
       "cjnOspfExtLsdbTOS": cjnOspfExtLsdbTOS,
       "cjnOspfExtLsdbMetric": cjnOspfExtLsdbMetric,
       "cjnOspfExtLsdForwardingAddress": cjnOspfExtLsdForwardingAddress,
       "cjnOspfExtLsdbRouteTag": cjnOspfExtLsdbRouteTag,
       "cjnOspfNetLsdbTable": cjnOspfNetLsdbTable,
       "cjnOspfNetLsdbEntry": cjnOspfNetLsdbEntry,
       "cjnOspfNetLsdbAreaId": cjnOspfNetLsdbAreaId,
       "cjnOspfNetLsdbType": cjnOspfNetLsdbType,
       "cjnOspfNetLsdbAdvRtrId": cjnOspfNetLsdbAdvRtrId,
       "cjnOspfNetLsdbLsId": cjnOspfNetLsdbLsId,
       "cjnOspfNetLsdbAge": cjnOspfNetLsdbAge,
       "cjnOspfNetLsdbLsdbChecksum": cjnOspfNetLsdbLsdbChecksum,
       "cjnOspfNetLsdbSequence": cjnOspfNetLsdbSequence,
       "cjnOspfNetLsdNetMask": cjnOspfNetLsdNetMask,
       "cjnOspfRouterLsdbTable": cjnOspfRouterLsdbTable,
       "cjnOspfRouterLsdbEntry": cjnOspfRouterLsdbEntry,
       "cjnOspfRouterLsdbAreaId": cjnOspfRouterLsdbAreaId,
       "cjnOspfRouterLsdbType": cjnOspfRouterLsdbType,
       "cjnOspfRouterLsdbRtrId": cjnOspfRouterLsdbRtrId,
       "cjnOspfRouterLsdbLsId": cjnOspfRouterLsdbLsId,
       "cjnOspfRouterLsdbLinkData": cjnOspfRouterLsdbLinkData,
       "cjnOspfRouterLsdbNumOfTos": cjnOspfRouterLsdbNumOfTos,
       "cjnOspfRouterLsdbMet": cjnOspfRouterLsdbMet,
       "cjnOspfRouterLsaHdrTable": cjnOspfRouterLsaHdrTable,
       "cjnOspfRouterLsaHdrEntry": cjnOspfRouterLsaHdrEntry,
       "cjnOspfRouterLsaHdrAreaId": cjnOspfRouterLsaHdrAreaId,
       "cjnOspfRouterLsaHdrType": cjnOspfRouterLsaHdrType,
       "cjnOspfRouterLsaHdrAdvRtrId": cjnOspfRouterLsaHdrAdvRtrId,
       "cjnOspfRouterLsaHdrLsId": cjnOspfRouterLsaHdrLsId,
       "cjnOspfRouterLsaHdrAge": cjnOspfRouterLsaHdrAge,
       "cjnOspfRouterLsaHdrChecksum": cjnOspfRouterLsaHdrChecksum,
       "cjnOspfRouterLsaHdrSequence": cjnOspfRouterLsaHdrSequence,
       "cjnOspfRouterLsaHdrFlags": cjnOspfRouterLsaHdrFlags,
       "cjnOspfRouterLsaHdrLinkCount": cjnOspfRouterLsaHdrLinkCount,
       "cjnOspfSumLsaTable": cjnOspfSumLsaTable,
       "cjnOspfSumLsaEntry": cjnOspfSumLsaEntry,
       "cjnOspfSumLsaType": cjnOspfSumLsaType,
       "cjnOspfSumLsaAdvRtrId": cjnOspfSumLsaAdvRtrId,
       "cjnOspfSumLsaLsId": cjnOspfSumLsaLsId,
       "cjnOspfSumLsaLsdbAge": cjnOspfSumLsaLsdbAge,
       "cjnOspfSumLsaChecksum": cjnOspfSumLsaChecksum,
       "cjnOspfSumLsaSequence": cjnOspfSumLsaSequence,
       "cjnOspfSumLsaMask": cjnOspfSumLsaMask,
       "cjnOspfSumLsaTOS": cjnOspfSumLsaTOS,
       "cjnOspfSumLsaMetric": cjnOspfSumLsaMetric}
)
