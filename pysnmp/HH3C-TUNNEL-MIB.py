# SNMP MIB module (HH3C-TUNNEL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-TUNNEL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:55:09 2024
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

(hh3cCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cCommon")

(InterfaceIndex,
 InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero",
    "ifIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(IPv6FlowLabelOrAny,) = mibBuilder.importSymbols(
    "IPV6-FLOW-LABEL-MIB",
    "IPv6FlowLabelOrAny")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hh3cTunnel = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 53)
)
hh3cTunnel.setRevisions(
        ("2013-02-28 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class Hh3cTunnelType(Integer32, TextualConvention):
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
              12,
              13,
              14,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54)
        )
    )
    namedValues = NamedValues(
        *(("atmp", 9),
          ("direct", 2),
          ("gre", 3),
          ("isatap", 13),
          ("l2f", 7),
          ("l2tp", 5),
          ("minimal", 4),
          ("msdp", 10),
          ("other", 1),
          ("pptp", 6),
          ("sixOverFour", 12),
          ("sixToFour", 11),
          ("teredo", 14),
          ("tunnelModeCrLsp", 49),
          ("tunnelModeIPv4Gre", 36),
          ("tunnelModeIPv4GreDVPN", 46),
          ("tunnelModeIPv4IPv4", 38),
          ("tunnelModeIPv4IPv66to4", 41),
          ("tunnelModeIPv4IPv6Auto", 40),
          ("tunnelModeIPv4IPv6Config", 39),
          ("tunnelModeIPv4IPv6Isatap", 42),
          ("tunnelModeIPv4NVGRE", 53),
          ("tunnelModeIPv4UdpDVPN", 45),
          ("tunnelModeIPv4UdpVxlan", 51),
          ("tunnelModeIPv6Gre", 37),
          ("tunnelModeIPv6GreDVPN", 48),
          ("tunnelModeIPv6IPv4", 43),
          ("tunnelModeIPv6IPv6", 44),
          ("tunnelModeIPv6NVGRE", 54),
          ("tunnelModeIPv6UdpDVPN", 47),
          ("tunnelModeIPv6UdpVxlan", 52),
          ("tunnelModeMax", 50),
          ("tunnelModeReserve", 35),
          ("udp", 8))
    )



# MIB Managed Objects in the order of their OIDs

_Hh3cTunnelMIBObjects_ObjectIdentity = ObjectIdentity
hh3cTunnelMIBObjects = _Hh3cTunnelMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 53, 1)
)
_Hh3cTunnelTables_ObjectIdentity = ObjectIdentity
hh3cTunnelTables = _Hh3cTunnelTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 53, 1, 1)
)
_Hh3cTunnelIfTable_Object = MibTable
hh3cTunnelIfTable = _Hh3cTunnelIfTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 53, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cTunnelIfTable.setStatus("current")
_Hh3cTunnelIfEntry_Object = MibTableRow
hh3cTunnelIfEntry = _Hh3cTunnelIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 53, 1, 1, 1, 1)
)
hh3cTunnelIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hh3cTunnelIfEntry.setStatus("current")
_Hh3cTunnelIfEncapsMethod_Type = Hh3cTunnelType
_Hh3cTunnelIfEncapsMethod_Object = MibTableColumn
hh3cTunnelIfEncapsMethod = _Hh3cTunnelIfEncapsMethod_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 53, 1, 1, 1, 1, 3),
    _Hh3cTunnelIfEncapsMethod_Type()
)
hh3cTunnelIfEncapsMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cTunnelIfEncapsMethod.setStatus("current")


class _Hh3cTunnelIfHopLimit_Type(Integer32):
    """Custom type hh3cTunnelIfHopLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 255),
    )


_Hh3cTunnelIfHopLimit_Type.__name__ = "Integer32"
_Hh3cTunnelIfHopLimit_Object = MibTableColumn
hh3cTunnelIfHopLimit = _Hh3cTunnelIfHopLimit_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 53, 1, 1, 1, 1, 4),
    _Hh3cTunnelIfHopLimit_Type()
)
hh3cTunnelIfHopLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cTunnelIfHopLimit.setStatus("current")


class _Hh3cTunnelIfSecurity_Type(Integer32):
    """Custom type hh3cTunnelIfSecurity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ipsec", 2),
          ("none", 1),
          ("other", 3))
    )


_Hh3cTunnelIfSecurity_Type.__name__ = "Integer32"
_Hh3cTunnelIfSecurity_Object = MibTableColumn
hh3cTunnelIfSecurity = _Hh3cTunnelIfSecurity_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 53, 1, 1, 1, 1, 5),
    _Hh3cTunnelIfSecurity_Type()
)
hh3cTunnelIfSecurity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cTunnelIfSecurity.setStatus("current")


class _Hh3cTunnelIfTOS_Type(Integer32):
    """Custom type hh3cTunnelIfTOS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, 63),
    )


_Hh3cTunnelIfTOS_Type.__name__ = "Integer32"
_Hh3cTunnelIfTOS_Object = MibTableColumn
hh3cTunnelIfTOS = _Hh3cTunnelIfTOS_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 53, 1, 1, 1, 1, 6),
    _Hh3cTunnelIfTOS_Type()
)
hh3cTunnelIfTOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cTunnelIfTOS.setStatus("current")
_Hh3cTunnelIfFlowLabel_Type = IPv6FlowLabelOrAny
_Hh3cTunnelIfFlowLabel_Object = MibTableColumn
hh3cTunnelIfFlowLabel = _Hh3cTunnelIfFlowLabel_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 53, 1, 1, 1, 1, 7),
    _Hh3cTunnelIfFlowLabel_Type()
)
hh3cTunnelIfFlowLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cTunnelIfFlowLabel.setStatus("current")
_Hh3cTunnelIfAddressType_Type = InetAddressType
_Hh3cTunnelIfAddressType_Object = MibTableColumn
hh3cTunnelIfAddressType = _Hh3cTunnelIfAddressType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 53, 1, 1, 1, 1, 8),
    _Hh3cTunnelIfAddressType_Type()
)
hh3cTunnelIfAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cTunnelIfAddressType.setStatus("current")
_Hh3cTunnelIfLocalInetAddress_Type = InetAddress
_Hh3cTunnelIfLocalInetAddress_Object = MibTableColumn
hh3cTunnelIfLocalInetAddress = _Hh3cTunnelIfLocalInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 53, 1, 1, 1, 1, 9),
    _Hh3cTunnelIfLocalInetAddress_Type()
)
hh3cTunnelIfLocalInetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cTunnelIfLocalInetAddress.setStatus("current")
_Hh3cTunnelIfRemoteInetAddress_Type = InetAddress
_Hh3cTunnelIfRemoteInetAddress_Object = MibTableColumn
hh3cTunnelIfRemoteInetAddress = _Hh3cTunnelIfRemoteInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 53, 1, 1, 1, 1, 10),
    _Hh3cTunnelIfRemoteInetAddress_Type()
)
hh3cTunnelIfRemoteInetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cTunnelIfRemoteInetAddress.setStatus("current")


class _Hh3cTunnelIfEncapsLimit_Type(Integer32):
    """Custom type hh3cTunnelIfEncapsLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 255),
    )


_Hh3cTunnelIfEncapsLimit_Type.__name__ = "Integer32"
_Hh3cTunnelIfEncapsLimit_Object = MibTableColumn
hh3cTunnelIfEncapsLimit = _Hh3cTunnelIfEncapsLimit_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 53, 1, 1, 1, 1, 11),
    _Hh3cTunnelIfEncapsLimit_Type()
)
hh3cTunnelIfEncapsLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cTunnelIfEncapsLimit.setStatus("current")
_Hh3cTunnelInetConfigTable_Object = MibTable
hh3cTunnelInetConfigTable = _Hh3cTunnelInetConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 53, 1, 1, 3)
)
if mibBuilder.loadTexts:
    hh3cTunnelInetConfigTable.setStatus("current")
_Hh3cTunnelInetConfigEntry_Object = MibTableRow
hh3cTunnelInetConfigEntry = _Hh3cTunnelInetConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 53, 1, 1, 3, 1)
)
hh3cTunnelInetConfigEntry.setIndexNames(
    (0, "HH3C-TUNNEL-MIB", "hh3cTunnelInetConfigSlot"),
    (0, "HH3C-TUNNEL-MIB", "hh3cTunnelInetConfigSubSlot"),
    (0, "HH3C-TUNNEL-MIB", "hh3cTunnelInetConfigTunnNum"),
)
if mibBuilder.loadTexts:
    hh3cTunnelInetConfigEntry.setStatus("current")


class _Hh3cTunnelInetConfigSlot_Type(Integer32):
    """Custom type hh3cTunnelInetConfigSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Hh3cTunnelInetConfigSlot_Type.__name__ = "Integer32"
_Hh3cTunnelInetConfigSlot_Object = MibTableColumn
hh3cTunnelInetConfigSlot = _Hh3cTunnelInetConfigSlot_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 53, 1, 1, 3, 1, 1),
    _Hh3cTunnelInetConfigSlot_Type()
)
hh3cTunnelInetConfigSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cTunnelInetConfigSlot.setStatus("current")


class _Hh3cTunnelInetConfigSubSlot_Type(Integer32):
    """Custom type hh3cTunnelInetConfigSubSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Hh3cTunnelInetConfigSubSlot_Type.__name__ = "Integer32"
_Hh3cTunnelInetConfigSubSlot_Object = MibTableColumn
hh3cTunnelInetConfigSubSlot = _Hh3cTunnelInetConfigSubSlot_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 53, 1, 1, 3, 1, 2),
    _Hh3cTunnelInetConfigSubSlot_Type()
)
hh3cTunnelInetConfigSubSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cTunnelInetConfigSubSlot.setStatus("current")


class _Hh3cTunnelInetConfigTunnNum_Type(Integer32):
    """Custom type hh3cTunnelInetConfigTunnNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cTunnelInetConfigTunnNum_Type.__name__ = "Integer32"
_Hh3cTunnelInetConfigTunnNum_Object = MibTableColumn
hh3cTunnelInetConfigTunnNum = _Hh3cTunnelInetConfigTunnNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 53, 1, 1, 3, 1, 3),
    _Hh3cTunnelInetConfigTunnNum_Type()
)
hh3cTunnelInetConfigTunnNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cTunnelInetConfigTunnNum.setStatus("current")
_Hh3cTunnelInetConfigIfIndex_Type = InterfaceIndexOrZero
_Hh3cTunnelInetConfigIfIndex_Object = MibTableColumn
hh3cTunnelInetConfigIfIndex = _Hh3cTunnelInetConfigIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 53, 1, 1, 3, 1, 6),
    _Hh3cTunnelInetConfigIfIndex_Type()
)
hh3cTunnelInetConfigIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cTunnelInetConfigIfIndex.setStatus("current")
_Hh3cTunnelInetConfigStatus_Type = RowStatus
_Hh3cTunnelInetConfigStatus_Object = MibTableColumn
hh3cTunnelInetConfigStatus = _Hh3cTunnelInetConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 53, 1, 1, 3, 1, 7),
    _Hh3cTunnelInetConfigStatus_Type()
)
hh3cTunnelInetConfigStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cTunnelInetConfigStatus.setStatus("current")
_Hh3cTunnelEviTable_Object = MibTable
hh3cTunnelEviTable = _Hh3cTunnelEviTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 53, 1, 1, 4)
)
if mibBuilder.loadTexts:
    hh3cTunnelEviTable.setStatus("current")
_Hh3cTunnelEviEntry_Object = MibTableRow
hh3cTunnelEviEntry = _Hh3cTunnelEviEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 53, 1, 1, 4, 1)
)
hh3cTunnelEviEntry.setIndexNames(
    (0, "HH3C-TUNNEL-MIB", "hh3cTunnelEviTunnNum"),
)
if mibBuilder.loadTexts:
    hh3cTunnelEviEntry.setStatus("current")


class _Hh3cTunnelEviTunnNum_Type(Integer32):
    """Custom type hh3cTunnelEviTunnNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hh3cTunnelEviTunnNum_Type.__name__ = "Integer32"
_Hh3cTunnelEviTunnNum_Object = MibTableColumn
hh3cTunnelEviTunnNum = _Hh3cTunnelEviTunnNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 53, 1, 1, 4, 1, 1),
    _Hh3cTunnelEviTunnNum_Type()
)
hh3cTunnelEviTunnNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cTunnelEviTunnNum.setStatus("current")
_Hh3cTunnelEviIfIndex_Type = InterfaceIndex
_Hh3cTunnelEviIfIndex_Object = MibTableColumn
hh3cTunnelEviIfIndex = _Hh3cTunnelEviIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 53, 1, 1, 4, 1, 2),
    _Hh3cTunnelEviIfIndex_Type()
)
hh3cTunnelEviIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cTunnelEviIfIndex.setStatus("current")
_Hh3cTunnelEviStatus_Type = RowStatus
_Hh3cTunnelEviStatus_Object = MibTableColumn
hh3cTunnelEviStatus = _Hh3cTunnelEviStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 53, 1, 1, 4, 1, 3),
    _Hh3cTunnelEviStatus_Type()
)
hh3cTunnelEviStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cTunnelEviStatus.setStatus("current")
_Hh3cTunnelEviAddressType_Type = InetAddressType
_Hh3cTunnelEviAddressType_Object = MibTableColumn
hh3cTunnelEviAddressType = _Hh3cTunnelEviAddressType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 53, 1, 1, 4, 1, 4),
    _Hh3cTunnelEviAddressType_Type()
)
hh3cTunnelEviAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cTunnelEviAddressType.setStatus("current")
_Hh3cTunnelEviLocalAddr_Type = InetAddress
_Hh3cTunnelEviLocalAddr_Object = MibTableColumn
hh3cTunnelEviLocalAddr = _Hh3cTunnelEviLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 53, 1, 1, 4, 1, 5),
    _Hh3cTunnelEviLocalAddr_Type()
)
hh3cTunnelEviLocalAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cTunnelEviLocalAddr.setStatus("current")


class _Hh3cTunnelEviNetworkID_Type(Integer32):
    """Custom type hh3cTunnelEviNetworkID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_Hh3cTunnelEviNetworkID_Type.__name__ = "Integer32"
_Hh3cTunnelEviNetworkID_Object = MibTableColumn
hh3cTunnelEviNetworkID = _Hh3cTunnelEviNetworkID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 53, 1, 1, 4, 1, 6),
    _Hh3cTunnelEviNetworkID_Type()
)
hh3cTunnelEviNetworkID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cTunnelEviNetworkID.setStatus("current")


class _Hh3cTunnelEviKeepaliveInterval_Type(Integer32):
    """Custom type hh3cTunnelEviKeepaliveInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32767),
    )


_Hh3cTunnelEviKeepaliveInterval_Type.__name__ = "Integer32"
_Hh3cTunnelEviKeepaliveInterval_Object = MibTableColumn
hh3cTunnelEviKeepaliveInterval = _Hh3cTunnelEviKeepaliveInterval_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 53, 1, 1, 4, 1, 7),
    _Hh3cTunnelEviKeepaliveInterval_Type()
)
hh3cTunnelEviKeepaliveInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cTunnelEviKeepaliveInterval.setStatus("current")


class _Hh3cTunnelEviKeepaliveTimes_Type(Integer32):
    """Custom type hh3cTunnelEviKeepaliveTimes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Hh3cTunnelEviKeepaliveTimes_Type.__name__ = "Integer32"
_Hh3cTunnelEviKeepaliveTimes_Object = MibTableColumn
hh3cTunnelEviKeepaliveTimes = _Hh3cTunnelEviKeepaliveTimes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 53, 1, 1, 4, 1, 8),
    _Hh3cTunnelEviKeepaliveTimes_Type()
)
hh3cTunnelEviKeepaliveTimes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cTunnelEviKeepaliveTimes.setStatus("current")
_Hh3cTunnelEviLinkTable_Object = MibTable
hh3cTunnelEviLinkTable = _Hh3cTunnelEviLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 53, 1, 1, 5)
)
if mibBuilder.loadTexts:
    hh3cTunnelEviLinkTable.setStatus("current")
_Hh3cTunnelEviLinkEntry_Object = MibTableRow
hh3cTunnelEviLinkEntry = _Hh3cTunnelEviLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 53, 1, 1, 5, 1)
)
hh3cTunnelEviLinkEntry.setIndexNames(
    (0, "HH3C-TUNNEL-MIB", "hh3cTunnelEviTunnNum"),
    (0, "HH3C-TUNNEL-MIB", "hh3cTunnelEviLinkNum"),
)
if mibBuilder.loadTexts:
    hh3cTunnelEviLinkEntry.setStatus("current")


class _Hh3cTunnelEviLinkNum_Type(Integer32):
    """Custom type hh3cTunnelEviLinkNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hh3cTunnelEviLinkNum_Type.__name__ = "Integer32"
_Hh3cTunnelEviLinkNum_Object = MibTableColumn
hh3cTunnelEviLinkNum = _Hh3cTunnelEviLinkNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 53, 1, 1, 5, 1, 1),
    _Hh3cTunnelEviLinkNum_Type()
)
hh3cTunnelEviLinkNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cTunnelEviLinkNum.setStatus("current")
_Hh3cTunnelEviLinkIfIndex_Type = InterfaceIndex
_Hh3cTunnelEviLinkIfIndex_Object = MibTableColumn
hh3cTunnelEviLinkIfIndex = _Hh3cTunnelEviLinkIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 53, 1, 1, 5, 1, 2),
    _Hh3cTunnelEviLinkIfIndex_Type()
)
hh3cTunnelEviLinkIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cTunnelEviLinkIfIndex.setStatus("current")
_Hh3cTunnelEviLinkAddressType_Type = InetAddressType
_Hh3cTunnelEviLinkAddressType_Object = MibTableColumn
hh3cTunnelEviLinkAddressType = _Hh3cTunnelEviLinkAddressType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 53, 1, 1, 5, 1, 3),
    _Hh3cTunnelEviLinkAddressType_Type()
)
hh3cTunnelEviLinkAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cTunnelEviLinkAddressType.setStatus("current")
_Hh3cTunnelEviLinkRemoteAddr_Type = InetAddress
_Hh3cTunnelEviLinkRemoteAddr_Object = MibTableColumn
hh3cTunnelEviLinkRemoteAddr = _Hh3cTunnelEviLinkRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 53, 1, 1, 5, 1, 4),
    _Hh3cTunnelEviLinkRemoteAddr_Type()
)
hh3cTunnelEviLinkRemoteAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cTunnelEviLinkRemoteAddr.setStatus("current")
_Hh3cTunnelGreTable_Object = MibTable
hh3cTunnelGreTable = _Hh3cTunnelGreTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 53, 1, 1, 6)
)
if mibBuilder.loadTexts:
    hh3cTunnelGreTable.setStatus("current")
_Hh3cTunnelGreEntry_Object = MibTableRow
hh3cTunnelGreEntry = _Hh3cTunnelGreEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 53, 1, 1, 6, 1)
)
hh3cTunnelGreEntry.setIndexNames(
    (0, "HH3C-TUNNEL-MIB", "hh3cTunnelGreTunnNum"),
)
if mibBuilder.loadTexts:
    hh3cTunnelGreEntry.setStatus("current")


class _Hh3cTunnelGreTunnNum_Type(Integer32):
    """Custom type hh3cTunnelGreTunnNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hh3cTunnelGreTunnNum_Type.__name__ = "Integer32"
_Hh3cTunnelGreTunnNum_Object = MibTableColumn
hh3cTunnelGreTunnNum = _Hh3cTunnelGreTunnNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 53, 1, 1, 6, 1, 1),
    _Hh3cTunnelGreTunnNum_Type()
)
hh3cTunnelGreTunnNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cTunnelGreTunnNum.setStatus("current")
_Hh3cTunnelGreTunnIfIndex_Type = InterfaceIndex
_Hh3cTunnelGreTunnIfIndex_Object = MibTableColumn
hh3cTunnelGreTunnIfIndex = _Hh3cTunnelGreTunnIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 53, 1, 1, 6, 1, 2),
    _Hh3cTunnelGreTunnIfIndex_Type()
)
hh3cTunnelGreTunnIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cTunnelGreTunnIfIndex.setStatus("current")
_Hh3cTunnelGreAddressType_Type = InetAddressType
_Hh3cTunnelGreAddressType_Object = MibTableColumn
hh3cTunnelGreAddressType = _Hh3cTunnelGreAddressType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 53, 1, 1, 6, 1, 3),
    _Hh3cTunnelGreAddressType_Type()
)
hh3cTunnelGreAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cTunnelGreAddressType.setStatus("current")
_Hh3cTunnelGreLocalAddr_Type = InetAddress
_Hh3cTunnelGreLocalAddr_Object = MibTableColumn
hh3cTunnelGreLocalAddr = _Hh3cTunnelGreLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 53, 1, 1, 6, 1, 4),
    _Hh3cTunnelGreLocalAddr_Type()
)
hh3cTunnelGreLocalAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cTunnelGreLocalAddr.setStatus("current")
_Hh3cTunnelGreRemoteAddr_Type = InetAddress
_Hh3cTunnelGreRemoteAddr_Object = MibTableColumn
hh3cTunnelGreRemoteAddr = _Hh3cTunnelGreRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 53, 1, 1, 6, 1, 5),
    _Hh3cTunnelGreRemoteAddr_Type()
)
hh3cTunnelGreRemoteAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cTunnelGreRemoteAddr.setStatus("current")


class _Hh3cTunnelGreKeepaliveEnabled_Type(TruthValue):
    """Custom type hh3cTunnelGreKeepaliveEnabled based on TruthValue"""


_Hh3cTunnelGreKeepaliveEnabled_Object = MibTableColumn
hh3cTunnelGreKeepaliveEnabled = _Hh3cTunnelGreKeepaliveEnabled_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 53, 1, 1, 6, 1, 6),
    _Hh3cTunnelGreKeepaliveEnabled_Type()
)
hh3cTunnelGreKeepaliveEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cTunnelGreKeepaliveEnabled.setStatus("current")


class _Hh3cTunnelGreKeepaliveInterval_Type(Integer32):
    """Custom type hh3cTunnelGreKeepaliveInterval based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_Hh3cTunnelGreKeepaliveInterval_Type.__name__ = "Integer32"
_Hh3cTunnelGreKeepaliveInterval_Object = MibTableColumn
hh3cTunnelGreKeepaliveInterval = _Hh3cTunnelGreKeepaliveInterval_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 53, 1, 1, 6, 1, 7),
    _Hh3cTunnelGreKeepaliveInterval_Type()
)
hh3cTunnelGreKeepaliveInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cTunnelGreKeepaliveInterval.setStatus("current")


class _Hh3cTunnelGreKeepaliveTimes_Type(Integer32):
    """Custom type hh3cTunnelGreKeepaliveTimes based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Hh3cTunnelGreKeepaliveTimes_Type.__name__ = "Integer32"
_Hh3cTunnelGreKeepaliveTimes_Object = MibTableColumn
hh3cTunnelGreKeepaliveTimes = _Hh3cTunnelGreKeepaliveTimes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 53, 1, 1, 6, 1, 8),
    _Hh3cTunnelGreKeepaliveTimes_Type()
)
hh3cTunnelGreKeepaliveTimes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cTunnelGreKeepaliveTimes.setStatus("current")


class _Hh3cTunnelGreSlbgGroupNum_Type(Unsigned32):
    """Custom type hh3cTunnelGreSlbgGroupNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Hh3cTunnelGreSlbgGroupNum_Type.__name__ = "Unsigned32"
_Hh3cTunnelGreSlbgGroupNum_Object = MibTableColumn
hh3cTunnelGreSlbgGroupNum = _Hh3cTunnelGreSlbgGroupNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 53, 1, 1, 6, 1, 9),
    _Hh3cTunnelGreSlbgGroupNum_Type()
)
hh3cTunnelGreSlbgGroupNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cTunnelGreSlbgGroupNum.setStatus("current")
_Hh3cTunnelGreTunnStatus_Type = RowStatus
_Hh3cTunnelGreTunnStatus_Object = MibTableColumn
hh3cTunnelGreTunnStatus = _Hh3cTunnelGreTunnStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 53, 1, 1, 6, 1, 10),
    _Hh3cTunnelGreTunnStatus_Type()
)
hh3cTunnelGreTunnStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cTunnelGreTunnStatus.setStatus("current")
_Hh3cTunnelVxlanIfTable_Object = MibTable
hh3cTunnelVxlanIfTable = _Hh3cTunnelVxlanIfTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 53, 1, 1, 7)
)
if mibBuilder.loadTexts:
    hh3cTunnelVxlanIfTable.setStatus("current")
_Hh3cTunnelVxlanIfEntry_Object = MibTableRow
hh3cTunnelVxlanIfEntry = _Hh3cTunnelVxlanIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 53, 1, 1, 7, 1)
)
hh3cTunnelVxlanIfEntry.setIndexNames(
    (0, "HH3C-TUNNEL-MIB", "hh3cTunnelVxlanIfTunnNum"),
)
if mibBuilder.loadTexts:
    hh3cTunnelVxlanIfEntry.setStatus("current")


class _Hh3cTunnelVxlanIfTunnNum_Type(Integer32):
    """Custom type hh3cTunnelVxlanIfTunnNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hh3cTunnelVxlanIfTunnNum_Type.__name__ = "Integer32"
_Hh3cTunnelVxlanIfTunnNum_Object = MibTableColumn
hh3cTunnelVxlanIfTunnNum = _Hh3cTunnelVxlanIfTunnNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 53, 1, 1, 7, 1, 1),
    _Hh3cTunnelVxlanIfTunnNum_Type()
)
hh3cTunnelVxlanIfTunnNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cTunnelVxlanIfTunnNum.setStatus("current")
_Hh3cTunnelVxlanTunnIfIndex_Type = InterfaceIndex
_Hh3cTunnelVxlanTunnIfIndex_Object = MibTableColumn
hh3cTunnelVxlanTunnIfIndex = _Hh3cTunnelVxlanTunnIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 53, 1, 1, 7, 1, 2),
    _Hh3cTunnelVxlanTunnIfIndex_Type()
)
hh3cTunnelVxlanTunnIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cTunnelVxlanTunnIfIndex.setStatus("current")
_Hh3cTunnelVxlanIfAddressType_Type = InetAddressType
_Hh3cTunnelVxlanIfAddressType_Object = MibTableColumn
hh3cTunnelVxlanIfAddressType = _Hh3cTunnelVxlanIfAddressType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 53, 1, 1, 7, 1, 3),
    _Hh3cTunnelVxlanIfAddressType_Type()
)
hh3cTunnelVxlanIfAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cTunnelVxlanIfAddressType.setStatus("current")
_Hh3cTunnelVxlanIfLocalAddr_Type = InetAddress
_Hh3cTunnelVxlanIfLocalAddr_Object = MibTableColumn
hh3cTunnelVxlanIfLocalAddr = _Hh3cTunnelVxlanIfLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 53, 1, 1, 7, 1, 4),
    _Hh3cTunnelVxlanIfLocalAddr_Type()
)
hh3cTunnelVxlanIfLocalAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cTunnelVxlanIfLocalAddr.setStatus("current")
_Hh3cTunnelVxlanIfRemoteAddr_Type = InetAddress
_Hh3cTunnelVxlanIfRemoteAddr_Object = MibTableColumn
hh3cTunnelVxlanIfRemoteAddr = _Hh3cTunnelVxlanIfRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 53, 1, 1, 7, 1, 5),
    _Hh3cTunnelVxlanIfRemoteAddr_Type()
)
hh3cTunnelVxlanIfRemoteAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cTunnelVxlanIfRemoteAddr.setStatus("current")
_Hh3cTunnelVxlanIfStatus_Type = RowStatus
_Hh3cTunnelVxlanIfStatus_Object = MibTableColumn
hh3cTunnelVxlanIfStatus = _Hh3cTunnelVxlanIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 53, 1, 1, 7, 1, 6),
    _Hh3cTunnelVxlanIfStatus_Type()
)
hh3cTunnelVxlanIfStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cTunnelVxlanIfStatus.setStatus("current")
_Hh3cTunnelVxlanConfigGroup_ObjectIdentity = ObjectIdentity
hh3cTunnelVxlanConfigGroup = _Hh3cTunnelVxlanConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 53, 1, 1, 8)
)


class _Hh3cTunnelVxlanUdpPort_Type(Integer32):
    """Custom type hh3cTunnelVxlanUdpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Hh3cTunnelVxlanUdpPort_Type.__name__ = "Integer32"
_Hh3cTunnelVxlanUdpPort_Object = MibScalar
hh3cTunnelVxlanUdpPort = _Hh3cTunnelVxlanUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 53, 1, 1, 8, 1),
    _Hh3cTunnelVxlanUdpPort_Type()
)
hh3cTunnelVxlanUdpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cTunnelVxlanUdpPort.setStatus("current")
_Hh3cTunnelVxlanDropWrongCksmPkt_Type = TruthValue
_Hh3cTunnelVxlanDropWrongCksmPkt_Object = MibScalar
hh3cTunnelVxlanDropWrongCksmPkt = _Hh3cTunnelVxlanDropWrongCksmPkt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 53, 1, 1, 8, 2),
    _Hh3cTunnelVxlanDropWrongCksmPkt_Type()
)
hh3cTunnelVxlanDropWrongCksmPkt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cTunnelVxlanDropWrongCksmPkt.setStatus("current")
_Hh3cTunnelVxlanDropVlanTagPkt_Type = TruthValue
_Hh3cTunnelVxlanDropVlanTagPkt_Object = MibScalar
hh3cTunnelVxlanDropVlanTagPkt = _Hh3cTunnelVxlanDropVlanTagPkt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 53, 1, 1, 8, 3),
    _Hh3cTunnelVxlanDropVlanTagPkt_Type()
)
hh3cTunnelVxlanDropVlanTagPkt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cTunnelVxlanDropVlanTagPkt.setStatus("current")
_Hh3cTunnelAvailableIDGroup_ObjectIdentity = ObjectIdentity
hh3cTunnelAvailableIDGroup = _Hh3cTunnelAvailableIDGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 53, 1, 1, 9)
)


class _Hh3cTunnelAvailableID_Type(Integer32):
    """Custom type hh3cTunnelAvailableID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 2147483647),
    )


_Hh3cTunnelAvailableID_Type.__name__ = "Integer32"
_Hh3cTunnelAvailableID_Object = MibScalar
hh3cTunnelAvailableID = _Hh3cTunnelAvailableID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 53, 1, 1, 9, 1),
    _Hh3cTunnelAvailableID_Type()
)
hh3cTunnelAvailableID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cTunnelAvailableID.setStatus("current")
_Hh3cTunnelTotalNumTable_Object = MibTable
hh3cTunnelTotalNumTable = _Hh3cTunnelTotalNumTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 53, 1, 1, 10)
)
if mibBuilder.loadTexts:
    hh3cTunnelTotalNumTable.setStatus("current")
_Hh3cTunnelTotalNumEntry_Object = MibTableRow
hh3cTunnelTotalNumEntry = _Hh3cTunnelTotalNumEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 53, 1, 1, 10, 1)
)
hh3cTunnelTotalNumEntry.setIndexNames(
    (0, "HH3C-TUNNEL-MIB", "hh3cTunnelEncapsMethod"),
)
if mibBuilder.loadTexts:
    hh3cTunnelTotalNumEntry.setStatus("current")
_Hh3cTunnelEncapsMethod_Type = Hh3cTunnelType
_Hh3cTunnelEncapsMethod_Object = MibTableColumn
hh3cTunnelEncapsMethod = _Hh3cTunnelEncapsMethod_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 53, 1, 1, 10, 1, 1),
    _Hh3cTunnelEncapsMethod_Type()
)
hh3cTunnelEncapsMethod.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cTunnelEncapsMethod.setStatus("current")
_Hh3cTunnelTotalNum_Type = Unsigned32
_Hh3cTunnelTotalNum_Object = MibTableColumn
hh3cTunnelTotalNum = _Hh3cTunnelTotalNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 53, 1, 1, 10, 1, 2),
    _Hh3cTunnelTotalNum_Type()
)
hh3cTunnelTotalNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cTunnelTotalNum.setStatus("current")
_Hh3cTunnelNvgreIfTable_Object = MibTable
hh3cTunnelNvgreIfTable = _Hh3cTunnelNvgreIfTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 53, 1, 1, 11)
)
if mibBuilder.loadTexts:
    hh3cTunnelNvgreIfTable.setStatus("current")
_Hh3cTunnelNvgreIfEntry_Object = MibTableRow
hh3cTunnelNvgreIfEntry = _Hh3cTunnelNvgreIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 53, 1, 1, 11, 1)
)
hh3cTunnelNvgreIfEntry.setIndexNames(
    (0, "HH3C-TUNNEL-MIB", "hh3cTunnelNvgreIfTunnNum"),
)
if mibBuilder.loadTexts:
    hh3cTunnelNvgreIfEntry.setStatus("current")


class _Hh3cTunnelNvgreIfTunnNum_Type(Integer32):
    """Custom type hh3cTunnelNvgreIfTunnNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hh3cTunnelNvgreIfTunnNum_Type.__name__ = "Integer32"
_Hh3cTunnelNvgreIfTunnNum_Object = MibTableColumn
hh3cTunnelNvgreIfTunnNum = _Hh3cTunnelNvgreIfTunnNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 53, 1, 1, 11, 1, 1),
    _Hh3cTunnelNvgreIfTunnNum_Type()
)
hh3cTunnelNvgreIfTunnNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cTunnelNvgreIfTunnNum.setStatus("current")
_Hh3cTunnelNvgreTunnIfIndex_Type = InterfaceIndex
_Hh3cTunnelNvgreTunnIfIndex_Object = MibTableColumn
hh3cTunnelNvgreTunnIfIndex = _Hh3cTunnelNvgreTunnIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 53, 1, 1, 11, 1, 2),
    _Hh3cTunnelNvgreTunnIfIndex_Type()
)
hh3cTunnelNvgreTunnIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cTunnelNvgreTunnIfIndex.setStatus("current")
_Hh3cTunnelNvgreIfAddressType_Type = InetAddressType
_Hh3cTunnelNvgreIfAddressType_Object = MibTableColumn
hh3cTunnelNvgreIfAddressType = _Hh3cTunnelNvgreIfAddressType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 53, 1, 1, 11, 1, 3),
    _Hh3cTunnelNvgreIfAddressType_Type()
)
hh3cTunnelNvgreIfAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cTunnelNvgreIfAddressType.setStatus("current")
_Hh3cTunnelNvgreIfLocalAddr_Type = InetAddress
_Hh3cTunnelNvgreIfLocalAddr_Object = MibTableColumn
hh3cTunnelNvgreIfLocalAddr = _Hh3cTunnelNvgreIfLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 53, 1, 1, 11, 1, 4),
    _Hh3cTunnelNvgreIfLocalAddr_Type()
)
hh3cTunnelNvgreIfLocalAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cTunnelNvgreIfLocalAddr.setStatus("current")
_Hh3cTunnelNvgreIfRemoteAddr_Type = InetAddress
_Hh3cTunnelNvgreIfRemoteAddr_Object = MibTableColumn
hh3cTunnelNvgreIfRemoteAddr = _Hh3cTunnelNvgreIfRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 53, 1, 1, 11, 1, 5),
    _Hh3cTunnelNvgreIfRemoteAddr_Type()
)
hh3cTunnelNvgreIfRemoteAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cTunnelNvgreIfRemoteAddr.setStatus("current")
_Hh3cTunnelNvgreIfStatus_Type = RowStatus
_Hh3cTunnelNvgreIfStatus_Object = MibTableColumn
hh3cTunnelNvgreIfStatus = _Hh3cTunnelNvgreIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 53, 1, 1, 11, 1, 6),
    _Hh3cTunnelNvgreIfStatus_Type()
)
hh3cTunnelNvgreIfStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cTunnelNvgreIfStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-TUNNEL-MIB",
    **{"Hh3cTunnelType": Hh3cTunnelType,
       "hh3cTunnel": hh3cTunnel,
       "hh3cTunnelMIBObjects": hh3cTunnelMIBObjects,
       "hh3cTunnelTables": hh3cTunnelTables,
       "hh3cTunnelIfTable": hh3cTunnelIfTable,
       "hh3cTunnelIfEntry": hh3cTunnelIfEntry,
       "hh3cTunnelIfEncapsMethod": hh3cTunnelIfEncapsMethod,
       "hh3cTunnelIfHopLimit": hh3cTunnelIfHopLimit,
       "hh3cTunnelIfSecurity": hh3cTunnelIfSecurity,
       "hh3cTunnelIfTOS": hh3cTunnelIfTOS,
       "hh3cTunnelIfFlowLabel": hh3cTunnelIfFlowLabel,
       "hh3cTunnelIfAddressType": hh3cTunnelIfAddressType,
       "hh3cTunnelIfLocalInetAddress": hh3cTunnelIfLocalInetAddress,
       "hh3cTunnelIfRemoteInetAddress": hh3cTunnelIfRemoteInetAddress,
       "hh3cTunnelIfEncapsLimit": hh3cTunnelIfEncapsLimit,
       "hh3cTunnelInetConfigTable": hh3cTunnelInetConfigTable,
       "hh3cTunnelInetConfigEntry": hh3cTunnelInetConfigEntry,
       "hh3cTunnelInetConfigSlot": hh3cTunnelInetConfigSlot,
       "hh3cTunnelInetConfigSubSlot": hh3cTunnelInetConfigSubSlot,
       "hh3cTunnelInetConfigTunnNum": hh3cTunnelInetConfigTunnNum,
       "hh3cTunnelInetConfigIfIndex": hh3cTunnelInetConfigIfIndex,
       "hh3cTunnelInetConfigStatus": hh3cTunnelInetConfigStatus,
       "hh3cTunnelEviTable": hh3cTunnelEviTable,
       "hh3cTunnelEviEntry": hh3cTunnelEviEntry,
       "hh3cTunnelEviTunnNum": hh3cTunnelEviTunnNum,
       "hh3cTunnelEviIfIndex": hh3cTunnelEviIfIndex,
       "hh3cTunnelEviStatus": hh3cTunnelEviStatus,
       "hh3cTunnelEviAddressType": hh3cTunnelEviAddressType,
       "hh3cTunnelEviLocalAddr": hh3cTunnelEviLocalAddr,
       "hh3cTunnelEviNetworkID": hh3cTunnelEviNetworkID,
       "hh3cTunnelEviKeepaliveInterval": hh3cTunnelEviKeepaliveInterval,
       "hh3cTunnelEviKeepaliveTimes": hh3cTunnelEviKeepaliveTimes,
       "hh3cTunnelEviLinkTable": hh3cTunnelEviLinkTable,
       "hh3cTunnelEviLinkEntry": hh3cTunnelEviLinkEntry,
       "hh3cTunnelEviLinkNum": hh3cTunnelEviLinkNum,
       "hh3cTunnelEviLinkIfIndex": hh3cTunnelEviLinkIfIndex,
       "hh3cTunnelEviLinkAddressType": hh3cTunnelEviLinkAddressType,
       "hh3cTunnelEviLinkRemoteAddr": hh3cTunnelEviLinkRemoteAddr,
       "hh3cTunnelGreTable": hh3cTunnelGreTable,
       "hh3cTunnelGreEntry": hh3cTunnelGreEntry,
       "hh3cTunnelGreTunnNum": hh3cTunnelGreTunnNum,
       "hh3cTunnelGreTunnIfIndex": hh3cTunnelGreTunnIfIndex,
       "hh3cTunnelGreAddressType": hh3cTunnelGreAddressType,
       "hh3cTunnelGreLocalAddr": hh3cTunnelGreLocalAddr,
       "hh3cTunnelGreRemoteAddr": hh3cTunnelGreRemoteAddr,
       "hh3cTunnelGreKeepaliveEnabled": hh3cTunnelGreKeepaliveEnabled,
       "hh3cTunnelGreKeepaliveInterval": hh3cTunnelGreKeepaliveInterval,
       "hh3cTunnelGreKeepaliveTimes": hh3cTunnelGreKeepaliveTimes,
       "hh3cTunnelGreSlbgGroupNum": hh3cTunnelGreSlbgGroupNum,
       "hh3cTunnelGreTunnStatus": hh3cTunnelGreTunnStatus,
       "hh3cTunnelVxlanIfTable": hh3cTunnelVxlanIfTable,
       "hh3cTunnelVxlanIfEntry": hh3cTunnelVxlanIfEntry,
       "hh3cTunnelVxlanIfTunnNum": hh3cTunnelVxlanIfTunnNum,
       "hh3cTunnelVxlanTunnIfIndex": hh3cTunnelVxlanTunnIfIndex,
       "hh3cTunnelVxlanIfAddressType": hh3cTunnelVxlanIfAddressType,
       "hh3cTunnelVxlanIfLocalAddr": hh3cTunnelVxlanIfLocalAddr,
       "hh3cTunnelVxlanIfRemoteAddr": hh3cTunnelVxlanIfRemoteAddr,
       "hh3cTunnelVxlanIfStatus": hh3cTunnelVxlanIfStatus,
       "hh3cTunnelVxlanConfigGroup": hh3cTunnelVxlanConfigGroup,
       "hh3cTunnelVxlanUdpPort": hh3cTunnelVxlanUdpPort,
       "hh3cTunnelVxlanDropWrongCksmPkt": hh3cTunnelVxlanDropWrongCksmPkt,
       "hh3cTunnelVxlanDropVlanTagPkt": hh3cTunnelVxlanDropVlanTagPkt,
       "hh3cTunnelAvailableIDGroup": hh3cTunnelAvailableIDGroup,
       "hh3cTunnelAvailableID": hh3cTunnelAvailableID,
       "hh3cTunnelTotalNumTable": hh3cTunnelTotalNumTable,
       "hh3cTunnelTotalNumEntry": hh3cTunnelTotalNumEntry,
       "hh3cTunnelEncapsMethod": hh3cTunnelEncapsMethod,
       "hh3cTunnelTotalNum": hh3cTunnelTotalNum,
       "hh3cTunnelNvgreIfTable": hh3cTunnelNvgreIfTable,
       "hh3cTunnelNvgreIfEntry": hh3cTunnelNvgreIfEntry,
       "hh3cTunnelNvgreIfTunnNum": hh3cTunnelNvgreIfTunnNum,
       "hh3cTunnelNvgreTunnIfIndex": hh3cTunnelNvgreTunnIfIndex,
       "hh3cTunnelNvgreIfAddressType": hh3cTunnelNvgreIfAddressType,
       "hh3cTunnelNvgreIfLocalAddr": hh3cTunnelNvgreIfLocalAddr,
       "hh3cTunnelNvgreIfRemoteAddr": hh3cTunnelNvgreIfRemoteAddr,
       "hh3cTunnelNvgreIfStatus": hh3cTunnelNvgreIfStatus}
)
