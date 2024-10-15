# SNMP MIB module (RADLAN-VOIP-SNOOP) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RADLAN-VOIP-SNOOP
# Produced by pysmi-1.5.4 at Mon Oct 14 22:43:56 2024
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
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType,
 InetVersion,
 InetZoneIndex) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType",
    "InetVersion",
    "InetZoneIndex")

(VlanId,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanId")

(rnd,) = mibBuilder.importSymbols(
    "RADLAN-MIB",
    "rnd")

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
 MacAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

rlVoipSnoop = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 89, 213)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class RlVoipQosType(Integer32, TextualConvention):
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
        *(("dscp", 3),
          ("queue", 1),
          ("vpt", 2))
    )



class RlVoipMngSnoopIfIndexStatus(Integer32, TextualConvention):
    status = "current"
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



class RlVoipProtocolType(Integer32, TextualConvention):
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
        *(("h323", 2),
          ("sccp", 3),
          ("sip", 1))
    )



class RlVoipTcpUdpType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tcp", 2),
          ("udp", 1))
    )



# MIB Managed Objects in the order of their OIDs

_RlVoipMngSnoopEnableScalar_Type = TruthValue
_RlVoipMngSnoopEnableScalar_Object = MibScalar
rlVoipMngSnoopEnableScalar = _RlVoipMngSnoopEnableScalar_Object(
    (1, 3, 6, 1, 4, 1, 89, 213, 1),
    _RlVoipMngSnoopEnableScalar_Type()
)
rlVoipMngSnoopEnableScalar.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlVoipMngSnoopEnableScalar.setStatus("current")
_RlVoipMngSnoopQosTable_Object = MibTable
rlVoipMngSnoopQosTable = _RlVoipMngSnoopQosTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 213, 2)
)
if mibBuilder.loadTexts:
    rlVoipMngSnoopQosTable.setStatus("current")
_RlVoipMngSnoopQosEntry_Object = MibTableRow
rlVoipMngSnoopQosEntry = _RlVoipMngSnoopQosEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 213, 2, 1)
)
rlVoipMngSnoopQosEntry.setIndexNames(
    (0, "RADLAN-VOIP-SNOOP", "rlVoipMngSnoopQosType"),
)
if mibBuilder.loadTexts:
    rlVoipMngSnoopQosEntry.setStatus("current")
_RlVoipMngSnoopQosType_Type = RlVoipQosType
_RlVoipMngSnoopQosType_Object = MibTableColumn
rlVoipMngSnoopQosType = _RlVoipMngSnoopQosType_Object(
    (1, 3, 6, 1, 4, 1, 89, 213, 2, 1, 1),
    _RlVoipMngSnoopQosType_Type()
)
rlVoipMngSnoopQosType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlVoipMngSnoopQosType.setStatus("current")


class _RlVoipMngSnoopQosValue_Type(Integer32):
    """Custom type rlVoipMngSnoopQosValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_RlVoipMngSnoopQosValue_Type.__name__ = "Integer32"
_RlVoipMngSnoopQosValue_Object = MibTableColumn
rlVoipMngSnoopQosValue = _RlVoipMngSnoopQosValue_Object(
    (1, 3, 6, 1, 4, 1, 89, 213, 2, 1, 2),
    _RlVoipMngSnoopQosValue_Type()
)
rlVoipMngSnoopQosValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlVoipMngSnoopQosValue.setStatus("current")
_RlVoipMngSnoopIfIndexTable_Object = MibTable
rlVoipMngSnoopIfIndexTable = _RlVoipMngSnoopIfIndexTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 213, 3)
)
if mibBuilder.loadTexts:
    rlVoipMngSnoopIfIndexTable.setStatus("current")
_RlVoipMngSnoopIfIndexEntry_Object = MibTableRow
rlVoipMngSnoopIfIndexEntry = _RlVoipMngSnoopIfIndexEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 213, 3, 1)
)
rlVoipMngSnoopIfIndexEntry.setIndexNames(
    (0, "RADLAN-VOIP-SNOOP", "rlVoipMngSnoopIfIndex"),
)
if mibBuilder.loadTexts:
    rlVoipMngSnoopIfIndexEntry.setStatus("current")
_RlVoipMngSnoopIfIndex_Type = Integer32
_RlVoipMngSnoopIfIndex_Object = MibTableColumn
rlVoipMngSnoopIfIndex = _RlVoipMngSnoopIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 213, 3, 1, 1),
    _RlVoipMngSnoopIfIndex_Type()
)
rlVoipMngSnoopIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlVoipMngSnoopIfIndex.setStatus("current")
_RlVoipMngSnoopIfIndexStatus_Type = RlVoipMngSnoopIfIndexStatus
_RlVoipMngSnoopIfIndexStatus_Object = MibTableColumn
rlVoipMngSnoopIfIndexStatus = _RlVoipMngSnoopIfIndexStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 213, 3, 1, 2),
    _RlVoipMngSnoopIfIndexStatus_Type()
)
rlVoipMngSnoopIfIndexStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlVoipMngSnoopIfIndexStatus.setStatus("current")
_RlVoipMngSnoopSessionTable_Object = MibTable
rlVoipMngSnoopSessionTable = _RlVoipMngSnoopSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 213, 4)
)
if mibBuilder.loadTexts:
    rlVoipMngSnoopSessionTable.setStatus("current")
_RlVoipMngSnoopSessionEntry_Object = MibTableRow
rlVoipMngSnoopSessionEntry = _RlVoipMngSnoopSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 213, 4, 1)
)
rlVoipMngSnoopSessionEntry.setIndexNames(
    (0, "RADLAN-VOIP-SNOOP", "rlVoipMngSnoopSessionDstIpAddrType"),
    (0, "RADLAN-VOIP-SNOOP", "rlVoipMngSnoopSessionDstIpAddr"),
    (0, "RADLAN-VOIP-SNOOP", "rlVoipMngSnoopSessionSrcIpAddrType"),
    (0, "RADLAN-VOIP-SNOOP", "rlVoipMngSnoopSessionSrcIpAddr"),
    (0, "RADLAN-VOIP-SNOOP", "rlVoipMngSnoopSessionDstUdpRtp"),
    (0, "RADLAN-VOIP-SNOOP", "rlVoipMngSnoopSessionDstUdpRtcp"),
    (0, "RADLAN-VOIP-SNOOP", "rlVoipMngSnoopSessionSrcUdpRtp"),
    (0, "RADLAN-VOIP-SNOOP", "rlVoipMngSnoopSessionSrcUdpRtcp"),
)
if mibBuilder.loadTexts:
    rlVoipMngSnoopSessionEntry.setStatus("current")
_RlVoipMngSnoopSessionDstIpAddrType_Type = InetAddressType
_RlVoipMngSnoopSessionDstIpAddrType_Object = MibTableColumn
rlVoipMngSnoopSessionDstIpAddrType = _RlVoipMngSnoopSessionDstIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 89, 213, 4, 1, 1),
    _RlVoipMngSnoopSessionDstIpAddrType_Type()
)
rlVoipMngSnoopSessionDstIpAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlVoipMngSnoopSessionDstIpAddrType.setStatus("current")
_RlVoipMngSnoopSessionDstIpAddr_Type = InetAddress
_RlVoipMngSnoopSessionDstIpAddr_Object = MibTableColumn
rlVoipMngSnoopSessionDstIpAddr = _RlVoipMngSnoopSessionDstIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 213, 4, 1, 2),
    _RlVoipMngSnoopSessionDstIpAddr_Type()
)
rlVoipMngSnoopSessionDstIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlVoipMngSnoopSessionDstIpAddr.setStatus("current")
_RlVoipMngSnoopSessionSrcIpAddrType_Type = InetAddressType
_RlVoipMngSnoopSessionSrcIpAddrType_Object = MibTableColumn
rlVoipMngSnoopSessionSrcIpAddrType = _RlVoipMngSnoopSessionSrcIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 89, 213, 4, 1, 3),
    _RlVoipMngSnoopSessionSrcIpAddrType_Type()
)
rlVoipMngSnoopSessionSrcIpAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlVoipMngSnoopSessionSrcIpAddrType.setStatus("current")
_RlVoipMngSnoopSessionSrcIpAddr_Type = InetAddress
_RlVoipMngSnoopSessionSrcIpAddr_Object = MibTableColumn
rlVoipMngSnoopSessionSrcIpAddr = _RlVoipMngSnoopSessionSrcIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 213, 4, 1, 4),
    _RlVoipMngSnoopSessionSrcIpAddr_Type()
)
rlVoipMngSnoopSessionSrcIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlVoipMngSnoopSessionSrcIpAddr.setStatus("current")
_RlVoipMngSnoopSessionDstUdpRtp_Type = Integer32
_RlVoipMngSnoopSessionDstUdpRtp_Object = MibTableColumn
rlVoipMngSnoopSessionDstUdpRtp = _RlVoipMngSnoopSessionDstUdpRtp_Object(
    (1, 3, 6, 1, 4, 1, 89, 213, 4, 1, 5),
    _RlVoipMngSnoopSessionDstUdpRtp_Type()
)
rlVoipMngSnoopSessionDstUdpRtp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlVoipMngSnoopSessionDstUdpRtp.setStatus("current")
_RlVoipMngSnoopSessionDstUdpRtcp_Type = Integer32
_RlVoipMngSnoopSessionDstUdpRtcp_Object = MibTableColumn
rlVoipMngSnoopSessionDstUdpRtcp = _RlVoipMngSnoopSessionDstUdpRtcp_Object(
    (1, 3, 6, 1, 4, 1, 89, 213, 4, 1, 6),
    _RlVoipMngSnoopSessionDstUdpRtcp_Type()
)
rlVoipMngSnoopSessionDstUdpRtcp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlVoipMngSnoopSessionDstUdpRtcp.setStatus("current")
_RlVoipMngSnoopSessionSrcUdpRtp_Type = Integer32
_RlVoipMngSnoopSessionSrcUdpRtp_Object = MibTableColumn
rlVoipMngSnoopSessionSrcUdpRtp = _RlVoipMngSnoopSessionSrcUdpRtp_Object(
    (1, 3, 6, 1, 4, 1, 89, 213, 4, 1, 7),
    _RlVoipMngSnoopSessionSrcUdpRtp_Type()
)
rlVoipMngSnoopSessionSrcUdpRtp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlVoipMngSnoopSessionSrcUdpRtp.setStatus("current")
_RlVoipMngSnoopSessionSrcUdpRtcp_Type = Integer32
_RlVoipMngSnoopSessionSrcUdpRtcp_Object = MibTableColumn
rlVoipMngSnoopSessionSrcUdpRtcp = _RlVoipMngSnoopSessionSrcUdpRtcp_Object(
    (1, 3, 6, 1, 4, 1, 89, 213, 4, 1, 8),
    _RlVoipMngSnoopSessionSrcUdpRtcp_Type()
)
rlVoipMngSnoopSessionSrcUdpRtcp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlVoipMngSnoopSessionSrcUdpRtcp.setStatus("current")
_RlVoipMngSnoopSessionProtocolType_Type = RlVoipProtocolType
_RlVoipMngSnoopSessionProtocolType_Object = MibTableColumn
rlVoipMngSnoopSessionProtocolType = _RlVoipMngSnoopSessionProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 89, 213, 4, 1, 9),
    _RlVoipMngSnoopSessionProtocolType_Type()
)
rlVoipMngSnoopSessionProtocolType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlVoipMngSnoopSessionProtocolType.setStatus("current")
_RlVoipMngSnoopSessionSessionId_Type = Integer32
_RlVoipMngSnoopSessionSessionId_Object = MibTableColumn
rlVoipMngSnoopSessionSessionId = _RlVoipMngSnoopSessionSessionId_Object(
    (1, 3, 6, 1, 4, 1, 89, 213, 4, 1, 10),
    _RlVoipMngSnoopSessionSessionId_Type()
)
rlVoipMngSnoopSessionSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlVoipMngSnoopSessionSessionId.setStatus("current")
_RlVoipMngSnoopSessionTcpUdpType_Type = RlVoipTcpUdpType
_RlVoipMngSnoopSessionTcpUdpType_Object = MibTableColumn
rlVoipMngSnoopSessionTcpUdpType = _RlVoipMngSnoopSessionTcpUdpType_Object(
    (1, 3, 6, 1, 4, 1, 89, 213, 4, 1, 11),
    _RlVoipMngSnoopSessionTcpUdpType_Type()
)
rlVoipMngSnoopSessionTcpUdpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlVoipMngSnoopSessionTcpUdpType.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RADLAN-VOIP-SNOOP",
    **{"RlVoipQosType": RlVoipQosType,
       "RlVoipMngSnoopIfIndexStatus": RlVoipMngSnoopIfIndexStatus,
       "RlVoipProtocolType": RlVoipProtocolType,
       "RlVoipTcpUdpType": RlVoipTcpUdpType,
       "rlVoipSnoop": rlVoipSnoop,
       "rlVoipMngSnoopEnableScalar": rlVoipMngSnoopEnableScalar,
       "rlVoipMngSnoopQosTable": rlVoipMngSnoopQosTable,
       "rlVoipMngSnoopQosEntry": rlVoipMngSnoopQosEntry,
       "rlVoipMngSnoopQosType": rlVoipMngSnoopQosType,
       "rlVoipMngSnoopQosValue": rlVoipMngSnoopQosValue,
       "rlVoipMngSnoopIfIndexTable": rlVoipMngSnoopIfIndexTable,
       "rlVoipMngSnoopIfIndexEntry": rlVoipMngSnoopIfIndexEntry,
       "rlVoipMngSnoopIfIndex": rlVoipMngSnoopIfIndex,
       "rlVoipMngSnoopIfIndexStatus": rlVoipMngSnoopIfIndexStatus,
       "rlVoipMngSnoopSessionTable": rlVoipMngSnoopSessionTable,
       "rlVoipMngSnoopSessionEntry": rlVoipMngSnoopSessionEntry,
       "rlVoipMngSnoopSessionDstIpAddrType": rlVoipMngSnoopSessionDstIpAddrType,
       "rlVoipMngSnoopSessionDstIpAddr": rlVoipMngSnoopSessionDstIpAddr,
       "rlVoipMngSnoopSessionSrcIpAddrType": rlVoipMngSnoopSessionSrcIpAddrType,
       "rlVoipMngSnoopSessionSrcIpAddr": rlVoipMngSnoopSessionSrcIpAddr,
       "rlVoipMngSnoopSessionDstUdpRtp": rlVoipMngSnoopSessionDstUdpRtp,
       "rlVoipMngSnoopSessionDstUdpRtcp": rlVoipMngSnoopSessionDstUdpRtcp,
       "rlVoipMngSnoopSessionSrcUdpRtp": rlVoipMngSnoopSessionSrcUdpRtp,
       "rlVoipMngSnoopSessionSrcUdpRtcp": rlVoipMngSnoopSessionSrcUdpRtcp,
       "rlVoipMngSnoopSessionProtocolType": rlVoipMngSnoopSessionProtocolType,
       "rlVoipMngSnoopSessionSessionId": rlVoipMngSnoopSessionSessionId,
       "rlVoipMngSnoopSessionTcpUdpType": rlVoipMngSnoopSessionTcpUdpType}
)
