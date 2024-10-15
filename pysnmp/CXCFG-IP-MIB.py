# SNMP MIB module (CXCFG-IP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CXCFG-IP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:20:12 2024
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

(Alias,
 cxCfgIp,
 cxCfgIpSap,
 cxIcmp) = mibBuilder.importSymbols(
    "CXProduct-SMI",
    "Alias",
    "cxCfgIp",
    "cxCfgIpSap",
    "cxIcmp")

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

_CxCfgIpPingTable_Object = MibTable
cxCfgIpPingTable = _CxCfgIpPingTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 11, 1)
)
if mibBuilder.loadTexts:
    cxCfgIpPingTable.setStatus("mandatory")
_CxCfgIpPingEntry_Object = MibTableRow
cxCfgIpPingEntry = _CxCfgIpPingEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 11, 1, 1)
)
cxCfgIpPingEntry.setIndexNames(
    (0, "CXCFG-IP-MIB", "cxCfgIpPingDestAddr"),
)
if mibBuilder.loadTexts:
    cxCfgIpPingEntry.setStatus("mandatory")


class _CxCfgIpPingIndex_Type(Integer32):
    """Custom type cxCfgIpPingIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_CxCfgIpPingIndex_Type.__name__ = "Integer32"
_CxCfgIpPingIndex_Object = MibTableColumn
cxCfgIpPingIndex = _CxCfgIpPingIndex_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 11, 1, 1, 1),
    _CxCfgIpPingIndex_Type()
)
cxCfgIpPingIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxCfgIpPingIndex.setStatus("mandatory")
_CxCfgIpPingDestAddr_Type = IpAddress
_CxCfgIpPingDestAddr_Object = MibTableColumn
cxCfgIpPingDestAddr = _CxCfgIpPingDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 11, 1, 1, 2),
    _CxCfgIpPingDestAddr_Type()
)
cxCfgIpPingDestAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxCfgIpPingDestAddr.setStatus("mandatory")


class _CxCfgIpPingGapsInMs_Type(Integer32):
    """Custom type cxCfgIpPingGapsInMs based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_CxCfgIpPingGapsInMs_Type.__name__ = "Integer32"
_CxCfgIpPingGapsInMs_Object = MibTableColumn
cxCfgIpPingGapsInMs = _CxCfgIpPingGapsInMs_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 11, 1, 1, 3),
    _CxCfgIpPingGapsInMs_Type()
)
cxCfgIpPingGapsInMs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxCfgIpPingGapsInMs.setStatus("mandatory")


class _CxCfgIpPingNbOfPings_Type(Integer32):
    """Custom type cxCfgIpPingNbOfPings based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4000000),
    )


_CxCfgIpPingNbOfPings_Type.__name__ = "Integer32"
_CxCfgIpPingNbOfPings_Object = MibTableColumn
cxCfgIpPingNbOfPings = _CxCfgIpPingNbOfPings_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 11, 1, 1, 4),
    _CxCfgIpPingNbOfPings_Type()
)
cxCfgIpPingNbOfPings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxCfgIpPingNbOfPings.setStatus("mandatory")


class _CxCfgIpPingDataSize_Type(Integer32):
    """Custom type cxCfgIpPingDataSize based on Integer32"""
    defaultValue = 64

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_CxCfgIpPingDataSize_Type.__name__ = "Integer32"
_CxCfgIpPingDataSize_Object = MibTableColumn
cxCfgIpPingDataSize = _CxCfgIpPingDataSize_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 11, 1, 1, 5),
    _CxCfgIpPingDataSize_Type()
)
cxCfgIpPingDataSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxCfgIpPingDataSize.setStatus("mandatory")


class _CxCfgIpPingRowStatus_Type(Integer32):
    """Custom type cxCfgIpPingRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_CxCfgIpPingRowStatus_Type.__name__ = "Integer32"
_CxCfgIpPingRowStatus_Object = MibTableColumn
cxCfgIpPingRowStatus = _CxCfgIpPingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 11, 1, 1, 10),
    _CxCfgIpPingRowStatus_Type()
)
cxCfgIpPingRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxCfgIpPingRowStatus.setStatus("mandatory")


class _CxCfgIpPingTriggerSend_Type(Integer32):
    """Custom type cxCfgIpPingTriggerSend based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipIdle", 1),
          ("ipSend", 2))
    )


_CxCfgIpPingTriggerSend_Type.__name__ = "Integer32"
_CxCfgIpPingTriggerSend_Object = MibTableColumn
cxCfgIpPingTriggerSend = _CxCfgIpPingTriggerSend_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 11, 1, 1, 11),
    _CxCfgIpPingTriggerSend_Type()
)
cxCfgIpPingTriggerSend.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxCfgIpPingTriggerSend.setStatus("mandatory")
_CxCfgIpPingNbTx_Type = Counter32
_CxCfgIpPingNbTx_Object = MibTableColumn
cxCfgIpPingNbTx = _CxCfgIpPingNbTx_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 11, 1, 1, 20),
    _CxCfgIpPingNbTx_Type()
)
cxCfgIpPingNbTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxCfgIpPingNbTx.setStatus("mandatory")
_CxCfgIpPingNbReplyRx_Type = Counter32
_CxCfgIpPingNbReplyRx_Object = MibTableColumn
cxCfgIpPingNbReplyRx = _CxCfgIpPingNbReplyRx_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 11, 1, 1, 21),
    _CxCfgIpPingNbReplyRx_Type()
)
cxCfgIpPingNbReplyRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxCfgIpPingNbReplyRx.setStatus("mandatory")
_CxCfgIpPingNbErrorRx_Type = Counter32
_CxCfgIpPingNbErrorRx_Object = MibTableColumn
cxCfgIpPingNbErrorRx = _CxCfgIpPingNbErrorRx_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 11, 1, 1, 22),
    _CxCfgIpPingNbErrorRx_Type()
)
cxCfgIpPingNbErrorRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxCfgIpPingNbErrorRx.setStatus("mandatory")
_CxCfgIpPingLastSeqNumRx_Type = Counter32
_CxCfgIpPingLastSeqNumRx_Object = MibTableColumn
cxCfgIpPingLastSeqNumRx = _CxCfgIpPingLastSeqNumRx_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 11, 1, 1, 23),
    _CxCfgIpPingLastSeqNumRx_Type()
)
cxCfgIpPingLastSeqNumRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxCfgIpPingLastSeqNumRx.setStatus("mandatory")
_CxCfgIpPingLastRoundTripInMs_Type = Counter32
_CxCfgIpPingLastRoundTripInMs_Object = MibTableColumn
cxCfgIpPingLastRoundTripInMs = _CxCfgIpPingLastRoundTripInMs_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 11, 1, 1, 24),
    _CxCfgIpPingLastRoundTripInMs_Type()
)
cxCfgIpPingLastRoundTripInMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxCfgIpPingLastRoundTripInMs.setStatus("mandatory")
_CxCfgIpPingAvgRoundTripInMs_Type = Counter32
_CxCfgIpPingAvgRoundTripInMs_Object = MibTableColumn
cxCfgIpPingAvgRoundTripInMs = _CxCfgIpPingAvgRoundTripInMs_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 11, 1, 1, 25),
    _CxCfgIpPingAvgRoundTripInMs_Type()
)
cxCfgIpPingAvgRoundTripInMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxCfgIpPingAvgRoundTripInMs.setStatus("mandatory")
_CxCfgIpPingMinRoundTripInMs_Type = Counter32
_CxCfgIpPingMinRoundTripInMs_Object = MibTableColumn
cxCfgIpPingMinRoundTripInMs = _CxCfgIpPingMinRoundTripInMs_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 11, 1, 1, 26),
    _CxCfgIpPingMinRoundTripInMs_Type()
)
cxCfgIpPingMinRoundTripInMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxCfgIpPingMinRoundTripInMs.setStatus("mandatory")
_CxCfgIpPingMaxRoundTripInMs_Type = Counter32
_CxCfgIpPingMaxRoundTripInMs_Object = MibTableColumn
cxCfgIpPingMaxRoundTripInMs = _CxCfgIpPingMaxRoundTripInMs_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 11, 1, 1, 27),
    _CxCfgIpPingMaxRoundTripInMs_Type()
)
cxCfgIpPingMaxRoundTripInMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxCfgIpPingMaxRoundTripInMs.setStatus("mandatory")
_CxCfgIpPingLastNumHopsTraveled_Type = Counter32
_CxCfgIpPingLastNumHopsTraveled_Object = MibTableColumn
cxCfgIpPingLastNumHopsTraveled = _CxCfgIpPingLastNumHopsTraveled_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 11, 1, 1, 28),
    _CxCfgIpPingLastNumHopsTraveled_Type()
)
cxCfgIpPingLastNumHopsTraveled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxCfgIpPingLastNumHopsTraveled.setStatus("mandatory")
_CxCfgIpAddrTable_Object = MibTable
cxCfgIpAddrTable = _CxCfgIpAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 15, 1)
)
if mibBuilder.loadTexts:
    cxCfgIpAddrTable.setStatus("mandatory")
_CxCfgIpAddrEntry_Object = MibTableRow
cxCfgIpAddrEntry = _CxCfgIpAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 15, 1, 1)
)
cxCfgIpAddrEntry.setIndexNames(
    (0, "CXCFG-IP-MIB", "cxCfgIpAdEntAddr"),
)
if mibBuilder.loadTexts:
    cxCfgIpAddrEntry.setStatus("mandatory")
_CxCfgIpAdEntAddr_Type = IpAddress
_CxCfgIpAdEntAddr_Object = MibTableColumn
cxCfgIpAdEntAddr = _CxCfgIpAdEntAddr_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 15, 1, 1, 1),
    _CxCfgIpAdEntAddr_Type()
)
cxCfgIpAdEntAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxCfgIpAdEntAddr.setStatus("mandatory")
_CxCfgIpAdEntIfIndex_Type = Integer32
_CxCfgIpAdEntIfIndex_Object = MibTableColumn
cxCfgIpAdEntIfIndex = _CxCfgIpAdEntIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 15, 1, 1, 2),
    _CxCfgIpAdEntIfIndex_Type()
)
cxCfgIpAdEntIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxCfgIpAdEntIfIndex.setStatus("mandatory")
_CxCfgIpAdEntNetMask_Type = IpAddress
_CxCfgIpAdEntNetMask_Object = MibTableColumn
cxCfgIpAdEntNetMask = _CxCfgIpAdEntNetMask_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 15, 1, 1, 3),
    _CxCfgIpAdEntNetMask_Type()
)
cxCfgIpAdEntNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxCfgIpAdEntNetMask.setStatus("mandatory")
_CxCfgIpAdEntBcastAddr_Type = Integer32
_CxCfgIpAdEntBcastAddr_Object = MibTableColumn
cxCfgIpAdEntBcastAddr = _CxCfgIpAdEntBcastAddr_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 15, 1, 1, 4),
    _CxCfgIpAdEntBcastAddr_Type()
)
cxCfgIpAdEntBcastAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxCfgIpAdEntBcastAddr.setStatus("mandatory")
_CxCfgIpAdEntSubnetworkSAPAlias_Type = Alias
_CxCfgIpAdEntSubnetworkSAPAlias_Object = MibTableColumn
cxCfgIpAdEntSubnetworkSAPAlias = _CxCfgIpAdEntSubnetworkSAPAlias_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 15, 1, 1, 5),
    _CxCfgIpAdEntSubnetworkSAPAlias_Type()
)
cxCfgIpAdEntSubnetworkSAPAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxCfgIpAdEntSubnetworkSAPAlias.setStatus("mandatory")


class _CxCfgIpAdEntRowStatus_Type(Integer32):
    """Custom type cxCfgIpAdEntRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_CxCfgIpAdEntRowStatus_Type.__name__ = "Integer32"
_CxCfgIpAdEntRowStatus_Object = MibTableColumn
cxCfgIpAdEntRowStatus = _CxCfgIpAdEntRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 15, 1, 1, 6),
    _CxCfgIpAdEntRowStatus_Type()
)
cxCfgIpAdEntRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxCfgIpAdEntRowStatus.setStatus("mandatory")


class _CxCfgIpAdEntState_Type(Integer32):
    """Custom type cxCfgIpAdEntState based on Integer32"""
    defaultValue = 1

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
        *(("off", 2),
          ("on", 1),
          ("onether", 3),
          ("ontoken", 4))
    )


_CxCfgIpAdEntState_Type.__name__ = "Integer32"
_CxCfgIpAdEntState_Object = MibTableColumn
cxCfgIpAdEntState = _CxCfgIpAdEntState_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 15, 1, 1, 7),
    _CxCfgIpAdEntState_Type()
)
cxCfgIpAdEntState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxCfgIpAdEntState.setStatus("mandatory")
_CxCfgIpAdEntPeerAddr_Type = IpAddress
_CxCfgIpAdEntPeerAddr_Object = MibTableColumn
cxCfgIpAdEntPeerAddr = _CxCfgIpAdEntPeerAddr_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 15, 1, 1, 8),
    _CxCfgIpAdEntPeerAddr_Type()
)
cxCfgIpAdEntPeerAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxCfgIpAdEntPeerAddr.setStatus("mandatory")


class _CxCfgIpAdEntRtProto_Type(Integer32):
    """Custom type cxCfgIpAdEntRtProto based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("ospf", 3),
          ("rip", 2))
    )


_CxCfgIpAdEntRtProto_Type.__name__ = "Integer32"
_CxCfgIpAdEntRtProto_Object = MibTableColumn
cxCfgIpAdEntRtProto = _CxCfgIpAdEntRtProto_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 15, 1, 1, 9),
    _CxCfgIpAdEntRtProto_Type()
)
cxCfgIpAdEntRtProto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxCfgIpAdEntRtProto.setStatus("mandatory")


class _CxCfgIpAdEntMtu_Type(Integer32):
    """Custom type cxCfgIpAdEntMtu based on Integer32"""
    defaultValue = 1600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 4096),
    )


_CxCfgIpAdEntMtu_Type.__name__ = "Integer32"
_CxCfgIpAdEntMtu_Object = MibTableColumn
cxCfgIpAdEntMtu = _CxCfgIpAdEntMtu_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 15, 1, 1, 10),
    _CxCfgIpAdEntMtu_Type()
)
cxCfgIpAdEntMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxCfgIpAdEntMtu.setStatus("mandatory")


class _CxCfgIpAdEntReplyToRARP_Type(Integer32):
    """Custom type cxCfgIpAdEntReplyToRARP based on Integer32"""
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


_CxCfgIpAdEntReplyToRARP_Type.__name__ = "Integer32"
_CxCfgIpAdEntReplyToRARP_Object = MibTableColumn
cxCfgIpAdEntReplyToRARP = _CxCfgIpAdEntReplyToRARP_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 15, 1, 1, 11),
    _CxCfgIpAdEntReplyToRARP_Type()
)
cxCfgIpAdEntReplyToRARP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxCfgIpAdEntReplyToRARP.setStatus("mandatory")


class _CxCfgIpAdEntSRSupport_Type(Integer32):
    """Custom type cxCfgIpAdEntSRSupport based on Integer32"""
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


_CxCfgIpAdEntSRSupport_Type.__name__ = "Integer32"
_CxCfgIpAdEntSRSupport_Object = MibTableColumn
cxCfgIpAdEntSRSupport = _CxCfgIpAdEntSRSupport_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 15, 1, 1, 12),
    _CxCfgIpAdEntSRSupport_Type()
)
cxCfgIpAdEntSRSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxCfgIpAdEntSRSupport.setStatus("mandatory")


class _CxCfgIpRIP_Type(Integer32):
    """Custom type cxCfgIpRIP based on Integer32"""
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


_CxCfgIpRIP_Type.__name__ = "Integer32"
_CxCfgIpRIP_Object = MibScalar
cxCfgIpRIP = _CxCfgIpRIP_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 16, 1),
    _CxCfgIpRIP_Type()
)
cxCfgIpRIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxCfgIpRIP.setStatus("mandatory")


class _CxCfgRIPII_Type(Integer32):
    """Custom type cxCfgRIPII based on Integer32"""
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


_CxCfgRIPII_Type.__name__ = "Integer32"
_CxCfgRIPII_Object = MibScalar
cxCfgRIPII = _CxCfgRIPII_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 16, 2),
    _CxCfgRIPII_Type()
)
cxCfgRIPII.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxCfgRIPII.setStatus("mandatory")


class _CxCfgIpMibLevel_Type(Integer32):
    """Custom type cxCfgIpMibLevel based on Integer32"""
    defaultValue = 0


_CxCfgIpMibLevel_Object = MibScalar
cxCfgIpMibLevel = _CxCfgIpMibLevel_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 16, 3),
    _CxCfgIpMibLevel_Type()
)
cxCfgIpMibLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxCfgIpMibLevel.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CXCFG-IP-MIB",
    **{"cxCfgIpPingTable": cxCfgIpPingTable,
       "cxCfgIpPingEntry": cxCfgIpPingEntry,
       "cxCfgIpPingIndex": cxCfgIpPingIndex,
       "cxCfgIpPingDestAddr": cxCfgIpPingDestAddr,
       "cxCfgIpPingGapsInMs": cxCfgIpPingGapsInMs,
       "cxCfgIpPingNbOfPings": cxCfgIpPingNbOfPings,
       "cxCfgIpPingDataSize": cxCfgIpPingDataSize,
       "cxCfgIpPingRowStatus": cxCfgIpPingRowStatus,
       "cxCfgIpPingTriggerSend": cxCfgIpPingTriggerSend,
       "cxCfgIpPingNbTx": cxCfgIpPingNbTx,
       "cxCfgIpPingNbReplyRx": cxCfgIpPingNbReplyRx,
       "cxCfgIpPingNbErrorRx": cxCfgIpPingNbErrorRx,
       "cxCfgIpPingLastSeqNumRx": cxCfgIpPingLastSeqNumRx,
       "cxCfgIpPingLastRoundTripInMs": cxCfgIpPingLastRoundTripInMs,
       "cxCfgIpPingAvgRoundTripInMs": cxCfgIpPingAvgRoundTripInMs,
       "cxCfgIpPingMinRoundTripInMs": cxCfgIpPingMinRoundTripInMs,
       "cxCfgIpPingMaxRoundTripInMs": cxCfgIpPingMaxRoundTripInMs,
       "cxCfgIpPingLastNumHopsTraveled": cxCfgIpPingLastNumHopsTraveled,
       "cxCfgIpAddrTable": cxCfgIpAddrTable,
       "cxCfgIpAddrEntry": cxCfgIpAddrEntry,
       "cxCfgIpAdEntAddr": cxCfgIpAdEntAddr,
       "cxCfgIpAdEntIfIndex": cxCfgIpAdEntIfIndex,
       "cxCfgIpAdEntNetMask": cxCfgIpAdEntNetMask,
       "cxCfgIpAdEntBcastAddr": cxCfgIpAdEntBcastAddr,
       "cxCfgIpAdEntSubnetworkSAPAlias": cxCfgIpAdEntSubnetworkSAPAlias,
       "cxCfgIpAdEntRowStatus": cxCfgIpAdEntRowStatus,
       "cxCfgIpAdEntState": cxCfgIpAdEntState,
       "cxCfgIpAdEntPeerAddr": cxCfgIpAdEntPeerAddr,
       "cxCfgIpAdEntRtProto": cxCfgIpAdEntRtProto,
       "cxCfgIpAdEntMtu": cxCfgIpAdEntMtu,
       "cxCfgIpAdEntReplyToRARP": cxCfgIpAdEntReplyToRARP,
       "cxCfgIpAdEntSRSupport": cxCfgIpAdEntSRSupport,
       "cxCfgIpRIP": cxCfgIpRIP,
       "cxCfgRIPII": cxCfgRIPII,
       "cxCfgIpMibLevel": cxCfgIpMibLevel}
)
