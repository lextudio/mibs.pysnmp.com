# SNMP MIB module (IPMROUTE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IPMROUTE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:10:56 2024
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
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

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
 experimental,
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
    "experimental",
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

ipMRoute1MIB = ModuleIdentity(
    (1, 3, 6, 1, 3, 60)
)
ipMRoute1MIB.setRevisions(
        ("1999-07-22 12:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class IpMRoute1Protocol(Integer32, TextualConvention):
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
        *(("bgmp", 11),
          ("cbt", 7),
          ("dvmrp", 4),
          ("igmpOnly", 10),
          ("local", 2),
          ("mospf", 5),
          ("msdp", 12),
          ("netmgmt", 3),
          ("other", 1),
          ("pimDenseMode", 9),
          ("pimSparseDense", 6),
          ("pimSparseMode", 8))
    )



# MIB Managed Objects in the order of their OIDs

_IpMRoute1MIBObjects_ObjectIdentity = ObjectIdentity
ipMRoute1MIBObjects = _IpMRoute1MIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 3, 60, 1)
)
_IpMRoute1_ObjectIdentity = ObjectIdentity
ipMRoute1 = _IpMRoute1_ObjectIdentity(
    (1, 3, 6, 1, 3, 60, 1, 1)
)


class _IpMRoute1Enable_Type(Integer32):
    """Custom type ipMRoute1Enable based on Integer32"""
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


_IpMRoute1Enable_Type.__name__ = "Integer32"
_IpMRoute1Enable_Object = MibScalar
ipMRoute1Enable = _IpMRoute1Enable_Object(
    (1, 3, 6, 1, 3, 60, 1, 1, 1),
    _IpMRoute1Enable_Type()
)
ipMRoute1Enable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMRoute1Enable.setStatus("current")
_IpMRoute1Table_Object = MibTable
ipMRoute1Table = _IpMRoute1Table_Object(
    (1, 3, 6, 1, 3, 60, 1, 1, 2)
)
if mibBuilder.loadTexts:
    ipMRoute1Table.setStatus("current")
_IpMRoute1Entry_Object = MibTableRow
ipMRoute1Entry = _IpMRoute1Entry_Object(
    (1, 3, 6, 1, 3, 60, 1, 1, 2, 1)
)
ipMRoute1Entry.setIndexNames(
    (0, "IPMROUTE-MIB", "ipMRoute1Group"),
    (0, "IPMROUTE-MIB", "ipMRoute1Source"),
    (0, "IPMROUTE-MIB", "ipMRoute1SourceMask"),
)
if mibBuilder.loadTexts:
    ipMRoute1Entry.setStatus("current")
_IpMRoute1Group_Type = IpAddress
_IpMRoute1Group_Object = MibTableColumn
ipMRoute1Group = _IpMRoute1Group_Object(
    (1, 3, 6, 1, 3, 60, 1, 1, 2, 1, 1),
    _IpMRoute1Group_Type()
)
ipMRoute1Group.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipMRoute1Group.setStatus("current")
_IpMRoute1Source_Type = IpAddress
_IpMRoute1Source_Object = MibTableColumn
ipMRoute1Source = _IpMRoute1Source_Object(
    (1, 3, 6, 1, 3, 60, 1, 1, 2, 1, 2),
    _IpMRoute1Source_Type()
)
ipMRoute1Source.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipMRoute1Source.setStatus("current")
_IpMRoute1SourceMask_Type = IpAddress
_IpMRoute1SourceMask_Object = MibTableColumn
ipMRoute1SourceMask = _IpMRoute1SourceMask_Object(
    (1, 3, 6, 1, 3, 60, 1, 1, 2, 1, 3),
    _IpMRoute1SourceMask_Type()
)
ipMRoute1SourceMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipMRoute1SourceMask.setStatus("current")
_IpMRoute1UpstreamNeighbor_Type = IpAddress
_IpMRoute1UpstreamNeighbor_Object = MibTableColumn
ipMRoute1UpstreamNeighbor = _IpMRoute1UpstreamNeighbor_Object(
    (1, 3, 6, 1, 3, 60, 1, 1, 2, 1, 4),
    _IpMRoute1UpstreamNeighbor_Type()
)
ipMRoute1UpstreamNeighbor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMRoute1UpstreamNeighbor.setStatus("current")
_IpMRoute1InIfIndex_Type = InterfaceIndexOrZero
_IpMRoute1InIfIndex_Object = MibTableColumn
ipMRoute1InIfIndex = _IpMRoute1InIfIndex_Object(
    (1, 3, 6, 1, 3, 60, 1, 1, 2, 1, 5),
    _IpMRoute1InIfIndex_Type()
)
ipMRoute1InIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMRoute1InIfIndex.setStatus("current")
_IpMRoute1UpTime_Type = TimeTicks
_IpMRoute1UpTime_Object = MibTableColumn
ipMRoute1UpTime = _IpMRoute1UpTime_Object(
    (1, 3, 6, 1, 3, 60, 1, 1, 2, 1, 6),
    _IpMRoute1UpTime_Type()
)
ipMRoute1UpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMRoute1UpTime.setStatus("current")
_IpMRoute1ExpiryTime_Type = TimeTicks
_IpMRoute1ExpiryTime_Object = MibTableColumn
ipMRoute1ExpiryTime = _IpMRoute1ExpiryTime_Object(
    (1, 3, 6, 1, 3, 60, 1, 1, 2, 1, 7),
    _IpMRoute1ExpiryTime_Type()
)
ipMRoute1ExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMRoute1ExpiryTime.setStatus("current")
_IpMRoute1Pkts_Type = Counter32
_IpMRoute1Pkts_Object = MibTableColumn
ipMRoute1Pkts = _IpMRoute1Pkts_Object(
    (1, 3, 6, 1, 3, 60, 1, 1, 2, 1, 8),
    _IpMRoute1Pkts_Type()
)
ipMRoute1Pkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMRoute1Pkts.setStatus("current")
_IpMRoute1DifferentInIfPackets_Type = Counter32
_IpMRoute1DifferentInIfPackets_Object = MibTableColumn
ipMRoute1DifferentInIfPackets = _IpMRoute1DifferentInIfPackets_Object(
    (1, 3, 6, 1, 3, 60, 1, 1, 2, 1, 9),
    _IpMRoute1DifferentInIfPackets_Type()
)
ipMRoute1DifferentInIfPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMRoute1DifferentInIfPackets.setStatus("current")
_IpMRoute1Octets_Type = Counter32
_IpMRoute1Octets_Object = MibTableColumn
ipMRoute1Octets = _IpMRoute1Octets_Object(
    (1, 3, 6, 1, 3, 60, 1, 1, 2, 1, 10),
    _IpMRoute1Octets_Type()
)
ipMRoute1Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMRoute1Octets.setStatus("current")
_IpMRoute1Protocol_Type = IpMRoute1Protocol
_IpMRoute1Protocol_Object = MibTableColumn
ipMRoute1Protocol = _IpMRoute1Protocol_Object(
    (1, 3, 6, 1, 3, 60, 1, 1, 2, 1, 11),
    _IpMRoute1Protocol_Type()
)
ipMRoute1Protocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMRoute1Protocol.setStatus("current")


class _IpMRoute1RtProto_Type(Integer32):
    """Custom type ipMRoute1RtProto based on Integer32"""
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
              12,
              13,
              14,
              15,
              16,
              17)
        )
    )
    namedValues = NamedValues(
        *(("bbnSpfIgp", 12),
          ("bgp", 14),
          ("ciscoEigrp", 16),
          ("ciscoIgrp", 11),
          ("dvmrp", 17),
          ("egp", 5),
          ("esIs", 10),
          ("ggp", 6),
          ("hello", 7),
          ("icmp", 4),
          ("idpr", 15),
          ("isIs", 9),
          ("local", 2),
          ("netmgmt", 3),
          ("ospf", 13),
          ("other", 1),
          ("rip", 8))
    )


_IpMRoute1RtProto_Type.__name__ = "Integer32"
_IpMRoute1RtProto_Object = MibTableColumn
ipMRoute1RtProto = _IpMRoute1RtProto_Object(
    (1, 3, 6, 1, 3, 60, 1, 1, 2, 1, 12),
    _IpMRoute1RtProto_Type()
)
ipMRoute1RtProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMRoute1RtProto.setStatus("current")
_IpMRoute1RtAddress_Type = IpAddress
_IpMRoute1RtAddress_Object = MibTableColumn
ipMRoute1RtAddress = _IpMRoute1RtAddress_Object(
    (1, 3, 6, 1, 3, 60, 1, 1, 2, 1, 13),
    _IpMRoute1RtAddress_Type()
)
ipMRoute1RtAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMRoute1RtAddress.setStatus("current")
_IpMRoute1RtMask_Type = IpAddress
_IpMRoute1RtMask_Object = MibTableColumn
ipMRoute1RtMask = _IpMRoute1RtMask_Object(
    (1, 3, 6, 1, 3, 60, 1, 1, 2, 1, 14),
    _IpMRoute1RtMask_Type()
)
ipMRoute1RtMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMRoute1RtMask.setStatus("current")


class _IpMRoute1RtType_Type(Integer32):
    """Custom type ipMRoute1RtType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("multicast", 2),
          ("unicast", 1))
    )


_IpMRoute1RtType_Type.__name__ = "Integer32"
_IpMRoute1RtType_Object = MibTableColumn
ipMRoute1RtType = _IpMRoute1RtType_Object(
    (1, 3, 6, 1, 3, 60, 1, 1, 2, 1, 15),
    _IpMRoute1RtType_Type()
)
ipMRoute1RtType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMRoute1RtType.setStatus("current")
_IpMRoute1HCOctets_Type = Counter64
_IpMRoute1HCOctets_Object = MibTableColumn
ipMRoute1HCOctets = _IpMRoute1HCOctets_Object(
    (1, 3, 6, 1, 3, 60, 1, 1, 2, 1, 16),
    _IpMRoute1HCOctets_Type()
)
ipMRoute1HCOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMRoute1HCOctets.setStatus("current")
_IpMRoute1NextHopTable_Object = MibTable
ipMRoute1NextHopTable = _IpMRoute1NextHopTable_Object(
    (1, 3, 6, 1, 3, 60, 1, 1, 3)
)
if mibBuilder.loadTexts:
    ipMRoute1NextHopTable.setStatus("current")
_IpMRoute1NextHopEntry_Object = MibTableRow
ipMRoute1NextHopEntry = _IpMRoute1NextHopEntry_Object(
    (1, 3, 6, 1, 3, 60, 1, 1, 3, 1)
)
ipMRoute1NextHopEntry.setIndexNames(
    (0, "IPMROUTE-MIB", "ipMRoute1NextHopGroup"),
    (0, "IPMROUTE-MIB", "ipMRoute1NextHopSource"),
    (0, "IPMROUTE-MIB", "ipMRoute1NextHopSourceMask"),
    (0, "IPMROUTE-MIB", "ipMRoute1NextHopIfIndex"),
    (0, "IPMROUTE-MIB", "ipMRoute1NextHopAddress"),
)
if mibBuilder.loadTexts:
    ipMRoute1NextHopEntry.setStatus("current")
_IpMRoute1NextHopGroup_Type = IpAddress
_IpMRoute1NextHopGroup_Object = MibTableColumn
ipMRoute1NextHopGroup = _IpMRoute1NextHopGroup_Object(
    (1, 3, 6, 1, 3, 60, 1, 1, 3, 1, 1),
    _IpMRoute1NextHopGroup_Type()
)
ipMRoute1NextHopGroup.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipMRoute1NextHopGroup.setStatus("current")
_IpMRoute1NextHopSource_Type = IpAddress
_IpMRoute1NextHopSource_Object = MibTableColumn
ipMRoute1NextHopSource = _IpMRoute1NextHopSource_Object(
    (1, 3, 6, 1, 3, 60, 1, 1, 3, 1, 2),
    _IpMRoute1NextHopSource_Type()
)
ipMRoute1NextHopSource.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipMRoute1NextHopSource.setStatus("current")
_IpMRoute1NextHopSourceMask_Type = IpAddress
_IpMRoute1NextHopSourceMask_Object = MibTableColumn
ipMRoute1NextHopSourceMask = _IpMRoute1NextHopSourceMask_Object(
    (1, 3, 6, 1, 3, 60, 1, 1, 3, 1, 3),
    _IpMRoute1NextHopSourceMask_Type()
)
ipMRoute1NextHopSourceMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipMRoute1NextHopSourceMask.setStatus("current")
_IpMRoute1NextHopIfIndex_Type = InterfaceIndex
_IpMRoute1NextHopIfIndex_Object = MibTableColumn
ipMRoute1NextHopIfIndex = _IpMRoute1NextHopIfIndex_Object(
    (1, 3, 6, 1, 3, 60, 1, 1, 3, 1, 4),
    _IpMRoute1NextHopIfIndex_Type()
)
ipMRoute1NextHopIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipMRoute1NextHopIfIndex.setStatus("current")
_IpMRoute1NextHopAddress_Type = IpAddress
_IpMRoute1NextHopAddress_Object = MibTableColumn
ipMRoute1NextHopAddress = _IpMRoute1NextHopAddress_Object(
    (1, 3, 6, 1, 3, 60, 1, 1, 3, 1, 5),
    _IpMRoute1NextHopAddress_Type()
)
ipMRoute1NextHopAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipMRoute1NextHopAddress.setStatus("current")


class _IpMRoute1NextHopState_Type(Integer32):
    """Custom type ipMRoute1NextHopState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forwarding", 2),
          ("pruned", 1))
    )


_IpMRoute1NextHopState_Type.__name__ = "Integer32"
_IpMRoute1NextHopState_Object = MibTableColumn
ipMRoute1NextHopState = _IpMRoute1NextHopState_Object(
    (1, 3, 6, 1, 3, 60, 1, 1, 3, 1, 6),
    _IpMRoute1NextHopState_Type()
)
ipMRoute1NextHopState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMRoute1NextHopState.setStatus("current")
_IpMRoute1NextHopUpTime_Type = TimeTicks
_IpMRoute1NextHopUpTime_Object = MibTableColumn
ipMRoute1NextHopUpTime = _IpMRoute1NextHopUpTime_Object(
    (1, 3, 6, 1, 3, 60, 1, 1, 3, 1, 7),
    _IpMRoute1NextHopUpTime_Type()
)
ipMRoute1NextHopUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMRoute1NextHopUpTime.setStatus("current")
_IpMRoute1NextHopExpiryTime_Type = TimeTicks
_IpMRoute1NextHopExpiryTime_Object = MibTableColumn
ipMRoute1NextHopExpiryTime = _IpMRoute1NextHopExpiryTime_Object(
    (1, 3, 6, 1, 3, 60, 1, 1, 3, 1, 8),
    _IpMRoute1NextHopExpiryTime_Type()
)
ipMRoute1NextHopExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMRoute1NextHopExpiryTime.setStatus("current")
_IpMRoute1NextHopClosestMemberHops_Type = Integer32
_IpMRoute1NextHopClosestMemberHops_Object = MibTableColumn
ipMRoute1NextHopClosestMemberHops = _IpMRoute1NextHopClosestMemberHops_Object(
    (1, 3, 6, 1, 3, 60, 1, 1, 3, 1, 9),
    _IpMRoute1NextHopClosestMemberHops_Type()
)
ipMRoute1NextHopClosestMemberHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMRoute1NextHopClosestMemberHops.setStatus("current")
_IpMRoute1NextHopProtocol_Type = IpMRoute1Protocol
_IpMRoute1NextHopProtocol_Object = MibTableColumn
ipMRoute1NextHopProtocol = _IpMRoute1NextHopProtocol_Object(
    (1, 3, 6, 1, 3, 60, 1, 1, 3, 1, 10),
    _IpMRoute1NextHopProtocol_Type()
)
ipMRoute1NextHopProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMRoute1NextHopProtocol.setStatus("current")
_IpMRoute1NextHopPkts_Type = Counter32
_IpMRoute1NextHopPkts_Object = MibTableColumn
ipMRoute1NextHopPkts = _IpMRoute1NextHopPkts_Object(
    (1, 3, 6, 1, 3, 60, 1, 1, 3, 1, 11),
    _IpMRoute1NextHopPkts_Type()
)
ipMRoute1NextHopPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMRoute1NextHopPkts.setStatus("current")
_IpMRoute1InterfaceTable_Object = MibTable
ipMRoute1InterfaceTable = _IpMRoute1InterfaceTable_Object(
    (1, 3, 6, 1, 3, 60, 1, 1, 4)
)
if mibBuilder.loadTexts:
    ipMRoute1InterfaceTable.setStatus("current")
_IpMRoute1InterfaceEntry_Object = MibTableRow
ipMRoute1InterfaceEntry = _IpMRoute1InterfaceEntry_Object(
    (1, 3, 6, 1, 3, 60, 1, 1, 4, 1)
)
ipMRoute1InterfaceEntry.setIndexNames(
    (0, "IPMROUTE-MIB", "ipMRoute1InterfaceIfIndex"),
)
if mibBuilder.loadTexts:
    ipMRoute1InterfaceEntry.setStatus("current")
_IpMRoute1InterfaceIfIndex_Type = InterfaceIndex
_IpMRoute1InterfaceIfIndex_Object = MibTableColumn
ipMRoute1InterfaceIfIndex = _IpMRoute1InterfaceIfIndex_Object(
    (1, 3, 6, 1, 3, 60, 1, 1, 4, 1, 1),
    _IpMRoute1InterfaceIfIndex_Type()
)
ipMRoute1InterfaceIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipMRoute1InterfaceIfIndex.setStatus("current")


class _IpMRoute1InterfaceTtl_Type(Integer32):
    """Custom type ipMRoute1InterfaceTtl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IpMRoute1InterfaceTtl_Type.__name__ = "Integer32"
_IpMRoute1InterfaceTtl_Object = MibTableColumn
ipMRoute1InterfaceTtl = _IpMRoute1InterfaceTtl_Object(
    (1, 3, 6, 1, 3, 60, 1, 1, 4, 1, 2),
    _IpMRoute1InterfaceTtl_Type()
)
ipMRoute1InterfaceTtl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMRoute1InterfaceTtl.setStatus("current")
_IpMRoute1InterfaceProtocol_Type = IpMRoute1Protocol
_IpMRoute1InterfaceProtocol_Object = MibTableColumn
ipMRoute1InterfaceProtocol = _IpMRoute1InterfaceProtocol_Object(
    (1, 3, 6, 1, 3, 60, 1, 1, 4, 1, 3),
    _IpMRoute1InterfaceProtocol_Type()
)
ipMRoute1InterfaceProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMRoute1InterfaceProtocol.setStatus("current")


class _IpMRoute1InterfaceRateLimit_Type(Integer32):
    """Custom type ipMRoute1InterfaceRateLimit based on Integer32"""
    defaultValue = 0


_IpMRoute1InterfaceRateLimit_Object = MibTableColumn
ipMRoute1InterfaceRateLimit = _IpMRoute1InterfaceRateLimit_Object(
    (1, 3, 6, 1, 3, 60, 1, 1, 4, 1, 4),
    _IpMRoute1InterfaceRateLimit_Type()
)
ipMRoute1InterfaceRateLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMRoute1InterfaceRateLimit.setStatus("current")
_IpMRoute1InterfaceInMcastOctets_Type = Counter32
_IpMRoute1InterfaceInMcastOctets_Object = MibTableColumn
ipMRoute1InterfaceInMcastOctets = _IpMRoute1InterfaceInMcastOctets_Object(
    (1, 3, 6, 1, 3, 60, 1, 1, 4, 1, 5),
    _IpMRoute1InterfaceInMcastOctets_Type()
)
ipMRoute1InterfaceInMcastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMRoute1InterfaceInMcastOctets.setStatus("current")
_IpMRoute1InterfaceOutMcastOctets_Type = Counter32
_IpMRoute1InterfaceOutMcastOctets_Object = MibTableColumn
ipMRoute1InterfaceOutMcastOctets = _IpMRoute1InterfaceOutMcastOctets_Object(
    (1, 3, 6, 1, 3, 60, 1, 1, 4, 1, 6),
    _IpMRoute1InterfaceOutMcastOctets_Type()
)
ipMRoute1InterfaceOutMcastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMRoute1InterfaceOutMcastOctets.setStatus("current")
_IpMRoute1InterfaceHCInMcastOctets_Type = Counter64
_IpMRoute1InterfaceHCInMcastOctets_Object = MibTableColumn
ipMRoute1InterfaceHCInMcastOctets = _IpMRoute1InterfaceHCInMcastOctets_Object(
    (1, 3, 6, 1, 3, 60, 1, 1, 4, 1, 7),
    _IpMRoute1InterfaceHCInMcastOctets_Type()
)
ipMRoute1InterfaceHCInMcastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMRoute1InterfaceHCInMcastOctets.setStatus("current")
_IpMRoute1InterfaceHCOutMcastOctets_Type = Counter64
_IpMRoute1InterfaceHCOutMcastOctets_Object = MibTableColumn
ipMRoute1InterfaceHCOutMcastOctets = _IpMRoute1InterfaceHCOutMcastOctets_Object(
    (1, 3, 6, 1, 3, 60, 1, 1, 4, 1, 8),
    _IpMRoute1InterfaceHCOutMcastOctets_Type()
)
ipMRoute1InterfaceHCOutMcastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMRoute1InterfaceHCOutMcastOctets.setStatus("current")
_IpMRoute1BoundaryTable_Object = MibTable
ipMRoute1BoundaryTable = _IpMRoute1BoundaryTable_Object(
    (1, 3, 6, 1, 3, 60, 1, 1, 5)
)
if mibBuilder.loadTexts:
    ipMRoute1BoundaryTable.setStatus("current")
_IpMRoute1BoundaryEntry_Object = MibTableRow
ipMRoute1BoundaryEntry = _IpMRoute1BoundaryEntry_Object(
    (1, 3, 6, 1, 3, 60, 1, 1, 5, 1)
)
ipMRoute1BoundaryEntry.setIndexNames(
    (0, "IPMROUTE-MIB", "ipMRoute1BoundaryIfIndex"),
    (0, "IPMROUTE-MIB", "ipMRoute1BoundaryAddress"),
    (0, "IPMROUTE-MIB", "ipMRoute1BoundaryAddressMask"),
)
if mibBuilder.loadTexts:
    ipMRoute1BoundaryEntry.setStatus("current")
_IpMRoute1BoundaryIfIndex_Type = InterfaceIndex
_IpMRoute1BoundaryIfIndex_Object = MibTableColumn
ipMRoute1BoundaryIfIndex = _IpMRoute1BoundaryIfIndex_Object(
    (1, 3, 6, 1, 3, 60, 1, 1, 5, 1, 1),
    _IpMRoute1BoundaryIfIndex_Type()
)
ipMRoute1BoundaryIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipMRoute1BoundaryIfIndex.setStatus("current")
_IpMRoute1BoundaryAddress_Type = IpAddress
_IpMRoute1BoundaryAddress_Object = MibTableColumn
ipMRoute1BoundaryAddress = _IpMRoute1BoundaryAddress_Object(
    (1, 3, 6, 1, 3, 60, 1, 1, 5, 1, 2),
    _IpMRoute1BoundaryAddress_Type()
)
ipMRoute1BoundaryAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipMRoute1BoundaryAddress.setStatus("current")
_IpMRoute1BoundaryAddressMask_Type = IpAddress
_IpMRoute1BoundaryAddressMask_Object = MibTableColumn
ipMRoute1BoundaryAddressMask = _IpMRoute1BoundaryAddressMask_Object(
    (1, 3, 6, 1, 3, 60, 1, 1, 5, 1, 3),
    _IpMRoute1BoundaryAddressMask_Type()
)
ipMRoute1BoundaryAddressMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipMRoute1BoundaryAddressMask.setStatus("current")
_IpMRoute1BoundaryStatus_Type = RowStatus
_IpMRoute1BoundaryStatus_Object = MibTableColumn
ipMRoute1BoundaryStatus = _IpMRoute1BoundaryStatus_Object(
    (1, 3, 6, 1, 3, 60, 1, 1, 5, 1, 4),
    _IpMRoute1BoundaryStatus_Type()
)
ipMRoute1BoundaryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMRoute1BoundaryStatus.setStatus("current")
_IpMRoute1ScopeNameTable_Object = MibTable
ipMRoute1ScopeNameTable = _IpMRoute1ScopeNameTable_Object(
    (1, 3, 6, 1, 3, 60, 1, 1, 6)
)
if mibBuilder.loadTexts:
    ipMRoute1ScopeNameTable.setStatus("current")
_IpMRoute1ScopeNameEntry_Object = MibTableRow
ipMRoute1ScopeNameEntry = _IpMRoute1ScopeNameEntry_Object(
    (1, 3, 6, 1, 3, 60, 1, 1, 6, 1)
)
ipMRoute1ScopeNameEntry.setIndexNames(
    (0, "IPMROUTE-MIB", "ipMRoute1ScopeNameAddress"),
    (0, "IPMROUTE-MIB", "ipMRoute1ScopeNameAddressMask"),
    (1, "IPMROUTE-MIB", "ipMRoute1ScopeNameLanguage"),
)
if mibBuilder.loadTexts:
    ipMRoute1ScopeNameEntry.setStatus("current")
_IpMRoute1ScopeNameAddress_Type = IpAddress
_IpMRoute1ScopeNameAddress_Object = MibTableColumn
ipMRoute1ScopeNameAddress = _IpMRoute1ScopeNameAddress_Object(
    (1, 3, 6, 1, 3, 60, 1, 1, 6, 1, 1),
    _IpMRoute1ScopeNameAddress_Type()
)
ipMRoute1ScopeNameAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipMRoute1ScopeNameAddress.setStatus("current")
_IpMRoute1ScopeNameAddressMask_Type = IpAddress
_IpMRoute1ScopeNameAddressMask_Object = MibTableColumn
ipMRoute1ScopeNameAddressMask = _IpMRoute1ScopeNameAddressMask_Object(
    (1, 3, 6, 1, 3, 60, 1, 1, 6, 1, 2),
    _IpMRoute1ScopeNameAddressMask_Type()
)
ipMRoute1ScopeNameAddressMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipMRoute1ScopeNameAddressMask.setStatus("current")


class _IpMRoute1ScopeNameLanguage_Type(DisplayString):
    """Custom type ipMRoute1ScopeNameLanguage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_IpMRoute1ScopeNameLanguage_Type.__name__ = "DisplayString"
_IpMRoute1ScopeNameLanguage_Object = MibTableColumn
ipMRoute1ScopeNameLanguage = _IpMRoute1ScopeNameLanguage_Object(
    (1, 3, 6, 1, 3, 60, 1, 1, 6, 1, 3),
    _IpMRoute1ScopeNameLanguage_Type()
)
ipMRoute1ScopeNameLanguage.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipMRoute1ScopeNameLanguage.setStatus("current")
_IpMRoute1ScopeNameString_Type = SnmpAdminString
_IpMRoute1ScopeNameString_Object = MibTableColumn
ipMRoute1ScopeNameString = _IpMRoute1ScopeNameString_Object(
    (1, 3, 6, 1, 3, 60, 1, 1, 6, 1, 4),
    _IpMRoute1ScopeNameString_Type()
)
ipMRoute1ScopeNameString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMRoute1ScopeNameString.setStatus("current")


class _IpMRoute1ScopeNameDefault_Type(TruthValue):
    """Custom type ipMRoute1ScopeNameDefault based on TruthValue"""


_IpMRoute1ScopeNameDefault_Object = MibTableColumn
ipMRoute1ScopeNameDefault = _IpMRoute1ScopeNameDefault_Object(
    (1, 3, 6, 1, 3, 60, 1, 1, 6, 1, 5),
    _IpMRoute1ScopeNameDefault_Type()
)
ipMRoute1ScopeNameDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMRoute1ScopeNameDefault.setStatus("current")
_IpMRoute1ScopeNameStatus_Type = RowStatus
_IpMRoute1ScopeNameStatus_Object = MibTableColumn
ipMRoute1ScopeNameStatus = _IpMRoute1ScopeNameStatus_Object(
    (1, 3, 6, 1, 3, 60, 1, 1, 6, 1, 6),
    _IpMRoute1ScopeNameStatus_Type()
)
ipMRoute1ScopeNameStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMRoute1ScopeNameStatus.setStatus("current")
_IpMRoute1EntryCount_Type = Gauge32
_IpMRoute1EntryCount_Object = MibScalar
ipMRoute1EntryCount = _IpMRoute1EntryCount_Object(
    (1, 3, 6, 1, 3, 60, 1, 1, 7),
    _IpMRoute1EntryCount_Type()
)
ipMRoute1EntryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMRoute1EntryCount.setStatus("current")
_IpMRoute1MIBConformance_ObjectIdentity = ObjectIdentity
ipMRoute1MIBConformance = _IpMRoute1MIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 3, 60, 2)
)
_IpMRoute1MIBCompliances_ObjectIdentity = ObjectIdentity
ipMRoute1MIBCompliances = _IpMRoute1MIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 3, 60, 2, 1)
)
_IpMRoute1MIBGroups_ObjectIdentity = ObjectIdentity
ipMRoute1MIBGroups = _IpMRoute1MIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 3, 60, 2, 2)
)

# Managed Objects groups

ipMRoute1MIBBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 60, 2, 2, 1)
)
ipMRoute1MIBBasicGroup.setObjects(
      *(("IPMROUTE-MIB", "ipMRoute1Enable"),
        ("IPMROUTE-MIB", "ipMRoute1EntryCount"),
        ("IPMROUTE-MIB", "ipMRoute1UpstreamNeighbor"),
        ("IPMROUTE-MIB", "ipMRoute1InIfIndex"),
        ("IPMROUTE-MIB", "ipMRoute1UpTime"),
        ("IPMROUTE-MIB", "ipMRoute1ExpiryTime"),
        ("IPMROUTE-MIB", "ipMRoute1NextHopState"),
        ("IPMROUTE-MIB", "ipMRoute1NextHopUpTime"),
        ("IPMROUTE-MIB", "ipMRoute1NextHopExpiryTime"),
        ("IPMROUTE-MIB", "ipMRoute1NextHopProtocol"),
        ("IPMROUTE-MIB", "ipMRoute1NextHopPkts"),
        ("IPMROUTE-MIB", "ipMRoute1InterfaceTtl"),
        ("IPMROUTE-MIB", "ipMRoute1InterfaceProtocol"),
        ("IPMROUTE-MIB", "ipMRoute1InterfaceRateLimit"),
        ("IPMROUTE-MIB", "ipMRoute1InterfaceInMcastOctets"),
        ("IPMROUTE-MIB", "ipMRoute1InterfaceOutMcastOctets"),
        ("IPMROUTE-MIB", "ipMRoute1Protocol"))
)
if mibBuilder.loadTexts:
    ipMRoute1MIBBasicGroup.setStatus("current")

ipMRoute1MIBHopCountGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 60, 2, 2, 2)
)
ipMRoute1MIBHopCountGroup.setObjects(
    ("IPMROUTE-MIB", "ipMRoute1NextHopClosestMemberHops")
)
if mibBuilder.loadTexts:
    ipMRoute1MIBHopCountGroup.setStatus("current")

ipMRoute1MIBBoundaryGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 60, 2, 2, 3)
)
ipMRoute1MIBBoundaryGroup.setObjects(
      *(("IPMROUTE-MIB", "ipMRoute1BoundaryStatus"),
        ("IPMROUTE-MIB", "ipMRoute1ScopeNameString"),
        ("IPMROUTE-MIB", "ipMRoute1ScopeNameDefault"),
        ("IPMROUTE-MIB", "ipMRoute1ScopeNameStatus"))
)
if mibBuilder.loadTexts:
    ipMRoute1MIBBoundaryGroup.setStatus("current")

ipMRoute1MIBPktsOutGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 60, 2, 2, 4)
)
ipMRoute1MIBPktsOutGroup.setObjects(
    ("IPMROUTE-MIB", "ipMRoute1NextHopPkts")
)
if mibBuilder.loadTexts:
    ipMRoute1MIBPktsOutGroup.setStatus("current")

ipMRoute1MIBHCInterfaceGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 60, 2, 2, 5)
)
ipMRoute1MIBHCInterfaceGroup.setObjects(
      *(("IPMROUTE-MIB", "ipMRoute1InterfaceHCInMcastOctets"),
        ("IPMROUTE-MIB", "ipMRoute1InterfaceHCOutMcastOctets"),
        ("IPMROUTE-MIB", "ipMRoute1HCOctets"))
)
if mibBuilder.loadTexts:
    ipMRoute1MIBHCInterfaceGroup.setStatus("current")

ipMRoute1MIBRouteGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 60, 2, 2, 6)
)
ipMRoute1MIBRouteGroup.setObjects(
      *(("IPMROUTE-MIB", "ipMRoute1RtProto"),
        ("IPMROUTE-MIB", "ipMRoute1RtAddress"),
        ("IPMROUTE-MIB", "ipMRoute1RtMask"),
        ("IPMROUTE-MIB", "ipMRoute1RtType"))
)
if mibBuilder.loadTexts:
    ipMRoute1MIBRouteGroup.setStatus("current")

ipMRoute1MIBPktsGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 60, 2, 2, 7)
)
ipMRoute1MIBPktsGroup.setObjects(
      *(("IPMROUTE-MIB", "ipMRoute1Pkts"),
        ("IPMROUTE-MIB", "ipMRoute1DifferentInIfPackets"),
        ("IPMROUTE-MIB", "ipMRoute1Octets"))
)
if mibBuilder.loadTexts:
    ipMRoute1MIBPktsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ipMRoute1MIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 3, 60, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ipMRoute1MIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IPMROUTE-MIB",
    **{"IpMRoute1Protocol": IpMRoute1Protocol,
       "ipMRoute1MIB": ipMRoute1MIB,
       "ipMRoute1MIBObjects": ipMRoute1MIBObjects,
       "ipMRoute1": ipMRoute1,
       "ipMRoute1Enable": ipMRoute1Enable,
       "ipMRoute1Table": ipMRoute1Table,
       "ipMRoute1Entry": ipMRoute1Entry,
       "ipMRoute1Group": ipMRoute1Group,
       "ipMRoute1Source": ipMRoute1Source,
       "ipMRoute1SourceMask": ipMRoute1SourceMask,
       "ipMRoute1UpstreamNeighbor": ipMRoute1UpstreamNeighbor,
       "ipMRoute1InIfIndex": ipMRoute1InIfIndex,
       "ipMRoute1UpTime": ipMRoute1UpTime,
       "ipMRoute1ExpiryTime": ipMRoute1ExpiryTime,
       "ipMRoute1Pkts": ipMRoute1Pkts,
       "ipMRoute1DifferentInIfPackets": ipMRoute1DifferentInIfPackets,
       "ipMRoute1Octets": ipMRoute1Octets,
       "ipMRoute1Protocol": ipMRoute1Protocol,
       "ipMRoute1RtProto": ipMRoute1RtProto,
       "ipMRoute1RtAddress": ipMRoute1RtAddress,
       "ipMRoute1RtMask": ipMRoute1RtMask,
       "ipMRoute1RtType": ipMRoute1RtType,
       "ipMRoute1HCOctets": ipMRoute1HCOctets,
       "ipMRoute1NextHopTable": ipMRoute1NextHopTable,
       "ipMRoute1NextHopEntry": ipMRoute1NextHopEntry,
       "ipMRoute1NextHopGroup": ipMRoute1NextHopGroup,
       "ipMRoute1NextHopSource": ipMRoute1NextHopSource,
       "ipMRoute1NextHopSourceMask": ipMRoute1NextHopSourceMask,
       "ipMRoute1NextHopIfIndex": ipMRoute1NextHopIfIndex,
       "ipMRoute1NextHopAddress": ipMRoute1NextHopAddress,
       "ipMRoute1NextHopState": ipMRoute1NextHopState,
       "ipMRoute1NextHopUpTime": ipMRoute1NextHopUpTime,
       "ipMRoute1NextHopExpiryTime": ipMRoute1NextHopExpiryTime,
       "ipMRoute1NextHopClosestMemberHops": ipMRoute1NextHopClosestMemberHops,
       "ipMRoute1NextHopProtocol": ipMRoute1NextHopProtocol,
       "ipMRoute1NextHopPkts": ipMRoute1NextHopPkts,
       "ipMRoute1InterfaceTable": ipMRoute1InterfaceTable,
       "ipMRoute1InterfaceEntry": ipMRoute1InterfaceEntry,
       "ipMRoute1InterfaceIfIndex": ipMRoute1InterfaceIfIndex,
       "ipMRoute1InterfaceTtl": ipMRoute1InterfaceTtl,
       "ipMRoute1InterfaceProtocol": ipMRoute1InterfaceProtocol,
       "ipMRoute1InterfaceRateLimit": ipMRoute1InterfaceRateLimit,
       "ipMRoute1InterfaceInMcastOctets": ipMRoute1InterfaceInMcastOctets,
       "ipMRoute1InterfaceOutMcastOctets": ipMRoute1InterfaceOutMcastOctets,
       "ipMRoute1InterfaceHCInMcastOctets": ipMRoute1InterfaceHCInMcastOctets,
       "ipMRoute1InterfaceHCOutMcastOctets": ipMRoute1InterfaceHCOutMcastOctets,
       "ipMRoute1BoundaryTable": ipMRoute1BoundaryTable,
       "ipMRoute1BoundaryEntry": ipMRoute1BoundaryEntry,
       "ipMRoute1BoundaryIfIndex": ipMRoute1BoundaryIfIndex,
       "ipMRoute1BoundaryAddress": ipMRoute1BoundaryAddress,
       "ipMRoute1BoundaryAddressMask": ipMRoute1BoundaryAddressMask,
       "ipMRoute1BoundaryStatus": ipMRoute1BoundaryStatus,
       "ipMRoute1ScopeNameTable": ipMRoute1ScopeNameTable,
       "ipMRoute1ScopeNameEntry": ipMRoute1ScopeNameEntry,
       "ipMRoute1ScopeNameAddress": ipMRoute1ScopeNameAddress,
       "ipMRoute1ScopeNameAddressMask": ipMRoute1ScopeNameAddressMask,
       "ipMRoute1ScopeNameLanguage": ipMRoute1ScopeNameLanguage,
       "ipMRoute1ScopeNameString": ipMRoute1ScopeNameString,
       "ipMRoute1ScopeNameDefault": ipMRoute1ScopeNameDefault,
       "ipMRoute1ScopeNameStatus": ipMRoute1ScopeNameStatus,
       "ipMRoute1EntryCount": ipMRoute1EntryCount,
       "ipMRoute1MIBConformance": ipMRoute1MIBConformance,
       "ipMRoute1MIBCompliances": ipMRoute1MIBCompliances,
       "ipMRoute1MIBCompliance": ipMRoute1MIBCompliance,
       "ipMRoute1MIBGroups": ipMRoute1MIBGroups,
       "ipMRoute1MIBBasicGroup": ipMRoute1MIBBasicGroup,
       "ipMRoute1MIBHopCountGroup": ipMRoute1MIBHopCountGroup,
       "ipMRoute1MIBBoundaryGroup": ipMRoute1MIBBoundaryGroup,
       "ipMRoute1MIBPktsOutGroup": ipMRoute1MIBPktsOutGroup,
       "ipMRoute1MIBHCInterfaceGroup": ipMRoute1MIBHCInterfaceGroup,
       "ipMRoute1MIBRouteGroup": ipMRoute1MIBRouteGroup,
       "ipMRoute1MIBPktsGroup": ipMRoute1MIBPktsGroup}
)
