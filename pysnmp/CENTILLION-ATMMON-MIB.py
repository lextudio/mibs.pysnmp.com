# SNMP MIB module (CENTILLION-ATMMON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CENTILLION-ATMMON-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:53:58 2024
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

(CardId,
 MacAddress,
 PortId,
 atmMonitor) = mibBuilder.importSymbols(
    "CENTILLION-ROOT-MIB",
    "CardId",
    "MacAddress",
    "PortId",
    "atmMonitor")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AtmPortMonitor_ObjectIdentity = ObjectIdentity
atmPortMonitor = _AtmPortMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 1)
)
_AtmPortStatTable_Object = MibTable
atmPortStatTable = _AtmPortStatTable_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 1, 1)
)
if mibBuilder.loadTexts:
    atmPortStatTable.setStatus("mandatory")
_AtmPortStatEntry_Object = MibTableRow
atmPortStatEntry = _AtmPortStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 1, 1, 1)
)
atmPortStatEntry.setIndexNames(
    (0, "CENTILLION-ATMMON-MIB", "atmStatCardId"),
    (0, "CENTILLION-ATMMON-MIB", "atmStatPortId"),
)
if mibBuilder.loadTexts:
    atmPortStatEntry.setStatus("mandatory")
_AtmStatCardId_Type = CardId
_AtmStatCardId_Object = MibTableColumn
atmStatCardId = _AtmStatCardId_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 1, 1, 1, 1),
    _AtmStatCardId_Type()
)
atmStatCardId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmStatCardId.setStatus("mandatory")
_AtmStatPortId_Type = PortId
_AtmStatPortId_Object = MibTableColumn
atmStatPortId = _AtmStatPortId_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 1, 1, 1, 2),
    _AtmStatPortId_Type()
)
atmStatPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmStatPortId.setStatus("mandatory")


class _AtmSigDetected_Type(Integer32):
    """Custom type atmSigDetected based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nosignal", 2),
          ("signalpresent", 1))
    )


_AtmSigDetected_Type.__name__ = "Integer32"
_AtmSigDetected_Object = MibTableColumn
atmSigDetected = _AtmSigDetected_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 1, 1, 1, 3),
    _AtmSigDetected_Type()
)
atmSigDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSigDetected.setStatus("mandatory")
_AtmRxBadHecCell_Type = Counter32
_AtmRxBadHecCell_Object = MibTableColumn
atmRxBadHecCell = _AtmRxBadHecCell_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 1, 1, 1, 4),
    _AtmRxBadHecCell_Type()
)
atmRxBadHecCell.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmRxBadHecCell.setStatus("mandatory")
_AtmRxDmaDropCell_Type = Counter32
_AtmRxDmaDropCell_Object = MibTableColumn
atmRxDmaDropCell = _AtmRxDmaDropCell_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 1, 1, 1, 5),
    _AtmRxDmaDropCell_Type()
)
atmRxDmaDropCell.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmRxDmaDropCell.setStatus("mandatory")
_AtmRxGoodCell_Type = Counter32
_AtmRxGoodCell_Object = MibTableColumn
atmRxGoodCell = _AtmRxGoodCell_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 1, 1, 1, 6),
    _AtmRxGoodCell_Type()
)
atmRxGoodCell.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmRxGoodCell.setStatus("mandatory")
_AtmTxDmaDropCell_Type = Counter32
_AtmTxDmaDropCell_Object = MibTableColumn
atmTxDmaDropCell = _AtmTxDmaDropCell_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 1, 1, 1, 7),
    _AtmTxDmaDropCell_Type()
)
atmTxDmaDropCell.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTxDmaDropCell.setStatus("mandatory")
_AtmTxGoodCell_Type = Counter32
_AtmTxGoodCell_Object = MibTableColumn
atmTxGoodCell = _AtmTxGoodCell_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 1, 1, 1, 8),
    _AtmTxGoodCell_Type()
)
atmTxGoodCell.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTxGoodCell.setStatus("mandatory")
_AtmSuniFifoOverrun_Type = Counter32
_AtmSuniFifoOverrun_Object = MibTableColumn
atmSuniFifoOverrun = _AtmSuniFifoOverrun_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 1, 1, 1, 9),
    _AtmSuniFifoOverrun_Type()
)
atmSuniFifoOverrun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSuniFifoOverrun.setStatus("mandatory")
_AtmElanMonitor_ObjectIdentity = ObjectIdentity
atmElanMonitor = _AtmElanMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 2)
)
_AtmElanPvcStatisticTable_Object = MibTable
atmElanPvcStatisticTable = _AtmElanPvcStatisticTable_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 2, 1)
)
if mibBuilder.loadTexts:
    atmElanPvcStatisticTable.setStatus("mandatory")
_AtmElanPvcStatisticEntry_Object = MibTableRow
atmElanPvcStatisticEntry = _AtmElanPvcStatisticEntry_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 2, 1, 1)
)
atmElanPvcStatisticEntry.setIndexNames(
    (0, "CENTILLION-ATMMON-MIB", "atmElanId"),
)
if mibBuilder.loadTexts:
    atmElanPvcStatisticEntry.setStatus("mandatory")


class _AtmElanId_Type(Integer32):
    """Custom type atmElanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_AtmElanId_Type.__name__ = "Integer32"
_AtmElanId_Object = MibTableColumn
atmElanId = _AtmElanId_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 2, 1, 1, 1),
    _AtmElanId_Type()
)
atmElanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmElanId.setStatus("mandatory")
_AtmElanPvcInUcastPkt_Type = Integer32
_AtmElanPvcInUcastPkt_Object = MibTableColumn
atmElanPvcInUcastPkt = _AtmElanPvcInUcastPkt_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 2, 1, 1, 2),
    _AtmElanPvcInUcastPkt_Type()
)
atmElanPvcInUcastPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmElanPvcInUcastPkt.setStatus("mandatory")
_AtmElanPvcInMcastPkt_Type = Integer32
_AtmElanPvcInMcastPkt_Object = MibTableColumn
atmElanPvcInMcastPkt = _AtmElanPvcInMcastPkt_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 2, 1, 1, 3),
    _AtmElanPvcInMcastPkt_Type()
)
atmElanPvcInMcastPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmElanPvcInMcastPkt.setStatus("mandatory")
_AtmElanPvcOutUcastPkt_Type = Integer32
_AtmElanPvcOutUcastPkt_Object = MibTableColumn
atmElanPvcOutUcastPkt = _AtmElanPvcOutUcastPkt_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 2, 1, 1, 4),
    _AtmElanPvcOutUcastPkt_Type()
)
atmElanPvcOutUcastPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmElanPvcOutUcastPkt.setStatus("mandatory")
_AtmElanPvcOutMcastPkt_Type = Integer32
_AtmElanPvcOutMcastPkt_Object = MibTableColumn
atmElanPvcOutMcastPkt = _AtmElanPvcOutMcastPkt_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 2, 1, 1, 5),
    _AtmElanPvcOutMcastPkt_Type()
)
atmElanPvcOutMcastPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmElanPvcOutMcastPkt.setStatus("mandatory")
_AtmPvcStatusMonitor_ObjectIdentity = ObjectIdentity
atmPvcStatusMonitor = _AtmPvcStatusMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 3)
)
_AtmPvcStatusTable_Object = MibTable
atmPvcStatusTable = _AtmPvcStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 3, 1)
)
if mibBuilder.loadTexts:
    atmPvcStatusTable.setStatus("mandatory")
_AtmPvcStatusEntry_Object = MibTableRow
atmPvcStatusEntry = _AtmPvcStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 3, 1, 1)
)
atmPvcStatusEntry.setIndexNames(
    (0, "CENTILLION-ATMMON-MIB", "atmPvcCktId"),
)
if mibBuilder.loadTexts:
    atmPvcStatusEntry.setStatus("mandatory")


class _AtmPvcCktId_Type(Integer32):
    """Custom type atmPvcCktId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_AtmPvcCktId_Type.__name__ = "Integer32"
_AtmPvcCktId_Object = MibTableColumn
atmPvcCktId = _AtmPvcCktId_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 3, 1, 1, 1),
    _AtmPvcCktId_Type()
)
atmPvcCktId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPvcCktId.setStatus("mandatory")


class _AtmPvcElanId_Type(Integer32):
    """Custom type atmPvcElanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_AtmPvcElanId_Type.__name__ = "Integer32"
_AtmPvcElanId_Object = MibTableColumn
atmPvcElanId = _AtmPvcElanId_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 3, 1, 1, 2),
    _AtmPvcElanId_Type()
)
atmPvcElanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPvcElanId.setStatus("mandatory")


class _AtmPvcRemoteSwitchInfoValid_Type(Integer32):
    """Custom type atmPvcRemoteSwitchInfoValid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_AtmPvcRemoteSwitchInfoValid_Type.__name__ = "Integer32"
_AtmPvcRemoteSwitchInfoValid_Object = MibTableColumn
atmPvcRemoteSwitchInfoValid = _AtmPvcRemoteSwitchInfoValid_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 3, 1, 1, 3),
    _AtmPvcRemoteSwitchInfoValid_Type()
)
atmPvcRemoteSwitchInfoValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPvcRemoteSwitchInfoValid.setStatus("mandatory")
_AtmPvcRemoteSwitchMacAddress_Type = MacAddress
_AtmPvcRemoteSwitchMacAddress_Object = MibTableColumn
atmPvcRemoteSwitchMacAddress = _AtmPvcRemoteSwitchMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 3, 1, 1, 4),
    _AtmPvcRemoteSwitchMacAddress_Type()
)
atmPvcRemoteSwitchMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPvcRemoteSwitchMacAddress.setStatus("mandatory")


class _AtmPvcRemoteSwitchPvcStatus_Type(Integer32):
    """Custom type atmPvcRemoteSwitchPvcStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_AtmPvcRemoteSwitchPvcStatus_Type.__name__ = "Integer32"
_AtmPvcRemoteSwitchPvcStatus_Object = MibTableColumn
atmPvcRemoteSwitchPvcStatus = _AtmPvcRemoteSwitchPvcStatus_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 3, 1, 1, 5),
    _AtmPvcRemoteSwitchPvcStatus_Type()
)
atmPvcRemoteSwitchPvcStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPvcRemoteSwitchPvcStatus.setStatus("mandatory")


class _AtmPvcSTPState_Type(Integer32):
    """Custom type atmPvcSTPState based on Integer32"""
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
        *(("blocking", 2),
          ("disabled", 1),
          ("forwarding", 5),
          ("learning", 4),
          ("listening", 3))
    )


_AtmPvcSTPState_Type.__name__ = "Integer32"
_AtmPvcSTPState_Object = MibTableColumn
atmPvcSTPState = _AtmPvcSTPState_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 3, 1, 1, 6),
    _AtmPvcSTPState_Type()
)
atmPvcSTPState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPvcSTPState.setStatus("mandatory")
_AtmPvcRemoteElanId_Type = Integer32
_AtmPvcRemoteElanId_Object = MibTableColumn
atmPvcRemoteElanId = _AtmPvcRemoteElanId_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 3, 1, 1, 7),
    _AtmPvcRemoteElanId_Type()
)
atmPvcRemoteElanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPvcRemoteElanId.setStatus("mandatory")
_AtmPvcRemoteMcpIpAddress_Type = IpAddress
_AtmPvcRemoteMcpIpAddress_Object = MibTableColumn
atmPvcRemoteMcpIpAddress = _AtmPvcRemoteMcpIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 3, 1, 1, 8),
    _AtmPvcRemoteMcpIpAddress_Type()
)
atmPvcRemoteMcpIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPvcRemoteMcpIpAddress.setStatus("mandatory")
_AtmSigMonitor_ObjectIdentity = ObjectIdentity
atmSigMonitor = _AtmSigMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 4)
)
_CnCurPtptConns_Type = Integer32
_CnCurPtptConns_Object = MibScalar
cnCurPtptConns = _CnCurPtptConns_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 4, 1),
    _CnCurPtptConns_Type()
)
cnCurPtptConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnCurPtptConns.setStatus("mandatory")
_CnCurPtmptConns_Type = Integer32
_CnCurPtmptConns_Object = MibScalar
cnCurPtmptConns = _CnCurPtmptConns_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 4, 2),
    _CnCurPtmptConns_Type()
)
cnCurPtmptConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnCurPtmptConns.setStatus("mandatory")
_CnCurActiveConns_Type = Integer32
_CnCurActiveConns_Object = MibScalar
cnCurActiveConns = _CnCurActiveConns_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 4, 3),
    _CnCurActiveConns_Type()
)
cnCurActiveConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnCurActiveConns.setStatus("mandatory")
_CnCurPortConnsTable_Object = MibTable
cnCurPortConnsTable = _CnCurPortConnsTable_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 4, 4)
)
if mibBuilder.loadTexts:
    cnCurPortConnsTable.setStatus("mandatory")
_CnCurPortConnsEntry_Object = MibTableRow
cnCurPortConnsEntry = _CnCurPortConnsEntry_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 4, 4, 1)
)
cnCurPortConnsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cnCurPortConnsEntry.setStatus("mandatory")
_CnCurPortConnsPtptConns_Type = Integer32
_CnCurPortConnsPtptConns_Object = MibTableColumn
cnCurPortConnsPtptConns = _CnCurPortConnsPtptConns_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 4, 4, 1, 1),
    _CnCurPortConnsPtptConns_Type()
)
cnCurPortConnsPtptConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnCurPortConnsPtptConns.setStatus("mandatory")
_CnCurPortConnsPtmptConns_Type = Integer32
_CnCurPortConnsPtmptConns_Object = MibTableColumn
cnCurPortConnsPtmptConns = _CnCurPortConnsPtmptConns_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 4, 4, 1, 2),
    _CnCurPortConnsPtmptConns_Type()
)
cnCurPortConnsPtmptConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnCurPortConnsPtmptConns.setStatus("mandatory")
_CnCurPortConnsActiveConns_Type = Integer32
_CnCurPortConnsActiveConns_Object = MibTableColumn
cnCurPortConnsActiveConns = _CnCurPortConnsActiveConns_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 4, 4, 1, 3),
    _CnCurPortConnsActiveConns_Type()
)
cnCurPortConnsActiveConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnCurPortConnsActiveConns.setStatus("mandatory")
_AtmCardMonitor_ObjectIdentity = ObjectIdentity
atmCardMonitor = _AtmCardMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 5)
)
_AtmCardOperTable_Object = MibTable
atmCardOperTable = _AtmCardOperTable_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 5, 1)
)
if mibBuilder.loadTexts:
    atmCardOperTable.setStatus("mandatory")
_AtmCardOperEntry_Object = MibTableRow
atmCardOperEntry = _AtmCardOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 5, 1, 1)
)
atmCardOperEntry.setIndexNames(
    (0, "CENTILLION-ATMMON-MIB", "atmCardOperCardId"),
)
if mibBuilder.loadTexts:
    atmCardOperEntry.setStatus("mandatory")
_AtmCardOperCardId_Type = CardId
_AtmCardOperCardId_Object = MibTableColumn
atmCardOperCardId = _AtmCardOperCardId_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 5, 1, 1, 1),
    _AtmCardOperCardId_Type()
)
atmCardOperCardId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmCardOperCardId.setStatus("mandatory")
_AtmCardOperExtClockSource_Type = Integer32
_AtmCardOperExtClockSource_Object = MibTableColumn
atmCardOperExtClockSource = _AtmCardOperExtClockSource_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 5, 1, 1, 2),
    _AtmCardOperExtClockSource_Type()
)
atmCardOperExtClockSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmCardOperExtClockSource.setStatus("mandatory")
_AtmStatusEnqMonitor_ObjectIdentity = ObjectIdentity
atmStatusEnqMonitor = _AtmStatusEnqMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 6)
)
_CnStsEnqPTPCalls_Type = Integer32
_CnStsEnqPTPCalls_Object = MibScalar
cnStsEnqPTPCalls = _CnStsEnqPTPCalls_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 6, 1),
    _CnStsEnqPTPCalls_Type()
)
cnStsEnqPTPCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnStsEnqPTPCalls.setStatus("mandatory")
_CnStsEnqActiveParties_Type = Integer32
_CnStsEnqActiveParties_Object = MibScalar
cnStsEnqActiveParties = _CnStsEnqActiveParties_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 6, 2),
    _CnStsEnqActiveParties_Type()
)
cnStsEnqActiveParties.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnStsEnqActiveParties.setStatus("mandatory")
_CnStsEnqSent_Type = Integer32
_CnStsEnqSent_Object = MibScalar
cnStsEnqSent = _CnStsEnqSent_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 6, 3),
    _CnStsEnqSent_Type()
)
cnStsEnqSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnStsEnqSent.setStatus("mandatory")
_CnStsEnqCfmsRecvd_Type = Integer32
_CnStsEnqCfmsRecvd_Object = MibScalar
cnStsEnqCfmsRecvd = _CnStsEnqCfmsRecvd_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 6, 4),
    _CnStsEnqCfmsRecvd_Type()
)
cnStsEnqCfmsRecvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnStsEnqCfmsRecvd.setStatus("mandatory")
_CnStsEnqRetried_Type = Integer32
_CnStsEnqRetried_Object = MibScalar
cnStsEnqRetried = _CnStsEnqRetried_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 6, 5),
    _CnStsEnqRetried_Type()
)
cnStsEnqRetried.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnStsEnqRetried.setStatus("mandatory")
_CnStsEnqTimeOuts_Type = Integer32
_CnStsEnqTimeOuts_Object = MibScalar
cnStsEnqTimeOuts = _CnStsEnqTimeOuts_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 6, 6),
    _CnStsEnqTimeOuts_Type()
)
cnStsEnqTimeOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnStsEnqTimeOuts.setStatus("mandatory")
_CnStsEnqQueueSize_Type = Integer32
_CnStsEnqQueueSize_Object = MibScalar
cnStsEnqQueueSize = _CnStsEnqQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 6, 7),
    _CnStsEnqQueueSize_Type()
)
cnStsEnqQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnStsEnqQueueSize.setStatus("mandatory")
_CnStsEnqCallsCleared_Type = Integer32
_CnStsEnqCallsCleared_Object = MibScalar
cnStsEnqCallsCleared = _CnStsEnqCallsCleared_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 6, 8),
    _CnStsEnqCallsCleared_Type()
)
cnStsEnqCallsCleared.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnStsEnqCallsCleared.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CENTILLION-ATMMON-MIB",
    **{"atmPortMonitor": atmPortMonitor,
       "atmPortStatTable": atmPortStatTable,
       "atmPortStatEntry": atmPortStatEntry,
       "atmStatCardId": atmStatCardId,
       "atmStatPortId": atmStatPortId,
       "atmSigDetected": atmSigDetected,
       "atmRxBadHecCell": atmRxBadHecCell,
       "atmRxDmaDropCell": atmRxDmaDropCell,
       "atmRxGoodCell": atmRxGoodCell,
       "atmTxDmaDropCell": atmTxDmaDropCell,
       "atmTxGoodCell": atmTxGoodCell,
       "atmSuniFifoOverrun": atmSuniFifoOverrun,
       "atmElanMonitor": atmElanMonitor,
       "atmElanPvcStatisticTable": atmElanPvcStatisticTable,
       "atmElanPvcStatisticEntry": atmElanPvcStatisticEntry,
       "atmElanId": atmElanId,
       "atmElanPvcInUcastPkt": atmElanPvcInUcastPkt,
       "atmElanPvcInMcastPkt": atmElanPvcInMcastPkt,
       "atmElanPvcOutUcastPkt": atmElanPvcOutUcastPkt,
       "atmElanPvcOutMcastPkt": atmElanPvcOutMcastPkt,
       "atmPvcStatusMonitor": atmPvcStatusMonitor,
       "atmPvcStatusTable": atmPvcStatusTable,
       "atmPvcStatusEntry": atmPvcStatusEntry,
       "atmPvcCktId": atmPvcCktId,
       "atmPvcElanId": atmPvcElanId,
       "atmPvcRemoteSwitchInfoValid": atmPvcRemoteSwitchInfoValid,
       "atmPvcRemoteSwitchMacAddress": atmPvcRemoteSwitchMacAddress,
       "atmPvcRemoteSwitchPvcStatus": atmPvcRemoteSwitchPvcStatus,
       "atmPvcSTPState": atmPvcSTPState,
       "atmPvcRemoteElanId": atmPvcRemoteElanId,
       "atmPvcRemoteMcpIpAddress": atmPvcRemoteMcpIpAddress,
       "atmSigMonitor": atmSigMonitor,
       "cnCurPtptConns": cnCurPtptConns,
       "cnCurPtmptConns": cnCurPtmptConns,
       "cnCurActiveConns": cnCurActiveConns,
       "cnCurPortConnsTable": cnCurPortConnsTable,
       "cnCurPortConnsEntry": cnCurPortConnsEntry,
       "cnCurPortConnsPtptConns": cnCurPortConnsPtptConns,
       "cnCurPortConnsPtmptConns": cnCurPortConnsPtmptConns,
       "cnCurPortConnsActiveConns": cnCurPortConnsActiveConns,
       "atmCardMonitor": atmCardMonitor,
       "atmCardOperTable": atmCardOperTable,
       "atmCardOperEntry": atmCardOperEntry,
       "atmCardOperCardId": atmCardOperCardId,
       "atmCardOperExtClockSource": atmCardOperExtClockSource,
       "atmStatusEnqMonitor": atmStatusEnqMonitor,
       "cnStsEnqPTPCalls": cnStsEnqPTPCalls,
       "cnStsEnqActiveParties": cnStsEnqActiveParties,
       "cnStsEnqSent": cnStsEnqSent,
       "cnStsEnqCfmsRecvd": cnStsEnqCfmsRecvd,
       "cnStsEnqRetried": cnStsEnqRetried,
       "cnStsEnqTimeOuts": cnStsEnqTimeOuts,
       "cnStsEnqQueueSize": cnStsEnqQueueSize,
       "cnStsEnqCallsCleared": cnStsEnqCallsCleared}
)
