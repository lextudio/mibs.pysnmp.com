# SNMP MIB module (HPN-ICF-TUNNEL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-TUNNEL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:02:03 2024
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

(hpnicfCommon,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicfCommon")

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

hpnicfTunnel = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 53)
)
hpnicfTunnel.setRevisions(
        ("2013-02-28 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class HpnicfTunnelType(Integer32, TextualConvention):
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

_HpnicfTunnelMIBObjects_ObjectIdentity = ObjectIdentity
hpnicfTunnelMIBObjects = _HpnicfTunnelMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 53, 1)
)
_HpnicfTunnelTables_ObjectIdentity = ObjectIdentity
hpnicfTunnelTables = _HpnicfTunnelTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 53, 1, 1)
)
_HpnicfTunnelIfTable_Object = MibTable
hpnicfTunnelIfTable = _HpnicfTunnelIfTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 53, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hpnicfTunnelIfTable.setStatus("current")
_HpnicfTunnelIfEntry_Object = MibTableRow
hpnicfTunnelIfEntry = _HpnicfTunnelIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 53, 1, 1, 1, 1)
)
hpnicfTunnelIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpnicfTunnelIfEntry.setStatus("current")
_HpnicfTunnelIfEncapsMethod_Type = HpnicfTunnelType
_HpnicfTunnelIfEncapsMethod_Object = MibTableColumn
hpnicfTunnelIfEncapsMethod = _HpnicfTunnelIfEncapsMethod_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 53, 1, 1, 1, 1, 3),
    _HpnicfTunnelIfEncapsMethod_Type()
)
hpnicfTunnelIfEncapsMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfTunnelIfEncapsMethod.setStatus("current")


class _HpnicfTunnelIfHopLimit_Type(Integer32):
    """Custom type hpnicfTunnelIfHopLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 255),
    )


_HpnicfTunnelIfHopLimit_Type.__name__ = "Integer32"
_HpnicfTunnelIfHopLimit_Object = MibTableColumn
hpnicfTunnelIfHopLimit = _HpnicfTunnelIfHopLimit_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 53, 1, 1, 1, 1, 4),
    _HpnicfTunnelIfHopLimit_Type()
)
hpnicfTunnelIfHopLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfTunnelIfHopLimit.setStatus("current")


class _HpnicfTunnelIfSecurity_Type(Integer32):
    """Custom type hpnicfTunnelIfSecurity based on Integer32"""
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


_HpnicfTunnelIfSecurity_Type.__name__ = "Integer32"
_HpnicfTunnelIfSecurity_Object = MibTableColumn
hpnicfTunnelIfSecurity = _HpnicfTunnelIfSecurity_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 53, 1, 1, 1, 1, 5),
    _HpnicfTunnelIfSecurity_Type()
)
hpnicfTunnelIfSecurity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfTunnelIfSecurity.setStatus("current")


class _HpnicfTunnelIfTOS_Type(Integer32):
    """Custom type hpnicfTunnelIfTOS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, 63),
    )


_HpnicfTunnelIfTOS_Type.__name__ = "Integer32"
_HpnicfTunnelIfTOS_Object = MibTableColumn
hpnicfTunnelIfTOS = _HpnicfTunnelIfTOS_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 53, 1, 1, 1, 1, 6),
    _HpnicfTunnelIfTOS_Type()
)
hpnicfTunnelIfTOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfTunnelIfTOS.setStatus("current")
_HpnicfTunnelIfFlowLabel_Type = IPv6FlowLabelOrAny
_HpnicfTunnelIfFlowLabel_Object = MibTableColumn
hpnicfTunnelIfFlowLabel = _HpnicfTunnelIfFlowLabel_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 53, 1, 1, 1, 1, 7),
    _HpnicfTunnelIfFlowLabel_Type()
)
hpnicfTunnelIfFlowLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfTunnelIfFlowLabel.setStatus("current")
_HpnicfTunnelIfAddressType_Type = InetAddressType
_HpnicfTunnelIfAddressType_Object = MibTableColumn
hpnicfTunnelIfAddressType = _HpnicfTunnelIfAddressType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 53, 1, 1, 1, 1, 8),
    _HpnicfTunnelIfAddressType_Type()
)
hpnicfTunnelIfAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfTunnelIfAddressType.setStatus("current")
_HpnicfTunnelIfLocalInetAddress_Type = InetAddress
_HpnicfTunnelIfLocalInetAddress_Object = MibTableColumn
hpnicfTunnelIfLocalInetAddress = _HpnicfTunnelIfLocalInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 53, 1, 1, 1, 1, 9),
    _HpnicfTunnelIfLocalInetAddress_Type()
)
hpnicfTunnelIfLocalInetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfTunnelIfLocalInetAddress.setStatus("current")
_HpnicfTunnelIfRemoteInetAddress_Type = InetAddress
_HpnicfTunnelIfRemoteInetAddress_Object = MibTableColumn
hpnicfTunnelIfRemoteInetAddress = _HpnicfTunnelIfRemoteInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 53, 1, 1, 1, 1, 10),
    _HpnicfTunnelIfRemoteInetAddress_Type()
)
hpnicfTunnelIfRemoteInetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfTunnelIfRemoteInetAddress.setStatus("current")


class _HpnicfTunnelIfEncapsLimit_Type(Integer32):
    """Custom type hpnicfTunnelIfEncapsLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 255),
    )


_HpnicfTunnelIfEncapsLimit_Type.__name__ = "Integer32"
_HpnicfTunnelIfEncapsLimit_Object = MibTableColumn
hpnicfTunnelIfEncapsLimit = _HpnicfTunnelIfEncapsLimit_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 53, 1, 1, 1, 1, 11),
    _HpnicfTunnelIfEncapsLimit_Type()
)
hpnicfTunnelIfEncapsLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfTunnelIfEncapsLimit.setStatus("current")
_HpnicfTunnelInetConfigTable_Object = MibTable
hpnicfTunnelInetConfigTable = _HpnicfTunnelInetConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 53, 1, 1, 3)
)
if mibBuilder.loadTexts:
    hpnicfTunnelInetConfigTable.setStatus("current")
_HpnicfTunnelInetConfigEntry_Object = MibTableRow
hpnicfTunnelInetConfigEntry = _HpnicfTunnelInetConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 53, 1, 1, 3, 1)
)
hpnicfTunnelInetConfigEntry.setIndexNames(
    (0, "HPN-ICF-TUNNEL-MIB", "hpnicfTunnelInetConfigSlot"),
    (0, "HPN-ICF-TUNNEL-MIB", "hpnicfTunnelInetConfigSubSlot"),
    (0, "HPN-ICF-TUNNEL-MIB", "hpnicfTunnelInetConfigTunnNum"),
)
if mibBuilder.loadTexts:
    hpnicfTunnelInetConfigEntry.setStatus("current")


class _HpnicfTunnelInetConfigSlot_Type(Integer32):
    """Custom type hpnicfTunnelInetConfigSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpnicfTunnelInetConfigSlot_Type.__name__ = "Integer32"
_HpnicfTunnelInetConfigSlot_Object = MibTableColumn
hpnicfTunnelInetConfigSlot = _HpnicfTunnelInetConfigSlot_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 53, 1, 1, 3, 1, 1),
    _HpnicfTunnelInetConfigSlot_Type()
)
hpnicfTunnelInetConfigSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfTunnelInetConfigSlot.setStatus("current")


class _HpnicfTunnelInetConfigSubSlot_Type(Integer32):
    """Custom type hpnicfTunnelInetConfigSubSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpnicfTunnelInetConfigSubSlot_Type.__name__ = "Integer32"
_HpnicfTunnelInetConfigSubSlot_Object = MibTableColumn
hpnicfTunnelInetConfigSubSlot = _HpnicfTunnelInetConfigSubSlot_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 53, 1, 1, 3, 1, 2),
    _HpnicfTunnelInetConfigSubSlot_Type()
)
hpnicfTunnelInetConfigSubSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfTunnelInetConfigSubSlot.setStatus("current")


class _HpnicfTunnelInetConfigTunnNum_Type(Integer32):
    """Custom type hpnicfTunnelInetConfigTunnNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnicfTunnelInetConfigTunnNum_Type.__name__ = "Integer32"
_HpnicfTunnelInetConfigTunnNum_Object = MibTableColumn
hpnicfTunnelInetConfigTunnNum = _HpnicfTunnelInetConfigTunnNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 53, 1, 1, 3, 1, 3),
    _HpnicfTunnelInetConfigTunnNum_Type()
)
hpnicfTunnelInetConfigTunnNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfTunnelInetConfigTunnNum.setStatus("current")
_HpnicfTunnelInetConfigIfIndex_Type = InterfaceIndexOrZero
_HpnicfTunnelInetConfigIfIndex_Object = MibTableColumn
hpnicfTunnelInetConfigIfIndex = _HpnicfTunnelInetConfigIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 53, 1, 1, 3, 1, 6),
    _HpnicfTunnelInetConfigIfIndex_Type()
)
hpnicfTunnelInetConfigIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfTunnelInetConfigIfIndex.setStatus("current")
_HpnicfTunnelInetConfigStatus_Type = RowStatus
_HpnicfTunnelInetConfigStatus_Object = MibTableColumn
hpnicfTunnelInetConfigStatus = _HpnicfTunnelInetConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 53, 1, 1, 3, 1, 7),
    _HpnicfTunnelInetConfigStatus_Type()
)
hpnicfTunnelInetConfigStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfTunnelInetConfigStatus.setStatus("current")
_HpnicfTunnelEviTable_Object = MibTable
hpnicfTunnelEviTable = _HpnicfTunnelEviTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 53, 1, 1, 4)
)
if mibBuilder.loadTexts:
    hpnicfTunnelEviTable.setStatus("current")
_HpnicfTunnelEviEntry_Object = MibTableRow
hpnicfTunnelEviEntry = _HpnicfTunnelEviEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 53, 1, 1, 4, 1)
)
hpnicfTunnelEviEntry.setIndexNames(
    (0, "HPN-ICF-TUNNEL-MIB", "hpnicfTunnelEviTunnNum"),
)
if mibBuilder.loadTexts:
    hpnicfTunnelEviEntry.setStatus("current")


class _HpnicfTunnelEviTunnNum_Type(Integer32):
    """Custom type hpnicfTunnelEviTunnNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpnicfTunnelEviTunnNum_Type.__name__ = "Integer32"
_HpnicfTunnelEviTunnNum_Object = MibTableColumn
hpnicfTunnelEviTunnNum = _HpnicfTunnelEviTunnNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 53, 1, 1, 4, 1, 1),
    _HpnicfTunnelEviTunnNum_Type()
)
hpnicfTunnelEviTunnNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfTunnelEviTunnNum.setStatus("current")
_HpnicfTunnelEviIfIndex_Type = InterfaceIndex
_HpnicfTunnelEviIfIndex_Object = MibTableColumn
hpnicfTunnelEviIfIndex = _HpnicfTunnelEviIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 53, 1, 1, 4, 1, 2),
    _HpnicfTunnelEviIfIndex_Type()
)
hpnicfTunnelEviIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfTunnelEviIfIndex.setStatus("current")
_HpnicfTunnelEviStatus_Type = RowStatus
_HpnicfTunnelEviStatus_Object = MibTableColumn
hpnicfTunnelEviStatus = _HpnicfTunnelEviStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 53, 1, 1, 4, 1, 3),
    _HpnicfTunnelEviStatus_Type()
)
hpnicfTunnelEviStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfTunnelEviStatus.setStatus("current")
_HpnicfTunnelEviAddressType_Type = InetAddressType
_HpnicfTunnelEviAddressType_Object = MibTableColumn
hpnicfTunnelEviAddressType = _HpnicfTunnelEviAddressType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 53, 1, 1, 4, 1, 4),
    _HpnicfTunnelEviAddressType_Type()
)
hpnicfTunnelEviAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfTunnelEviAddressType.setStatus("current")
_HpnicfTunnelEviLocalAddr_Type = InetAddress
_HpnicfTunnelEviLocalAddr_Object = MibTableColumn
hpnicfTunnelEviLocalAddr = _HpnicfTunnelEviLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 53, 1, 1, 4, 1, 5),
    _HpnicfTunnelEviLocalAddr_Type()
)
hpnicfTunnelEviLocalAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfTunnelEviLocalAddr.setStatus("current")


class _HpnicfTunnelEviNetworkID_Type(Integer32):
    """Custom type hpnicfTunnelEviNetworkID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_HpnicfTunnelEviNetworkID_Type.__name__ = "Integer32"
_HpnicfTunnelEviNetworkID_Object = MibTableColumn
hpnicfTunnelEviNetworkID = _HpnicfTunnelEviNetworkID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 53, 1, 1, 4, 1, 6),
    _HpnicfTunnelEviNetworkID_Type()
)
hpnicfTunnelEviNetworkID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfTunnelEviNetworkID.setStatus("current")


class _HpnicfTunnelEviKeepaliveInterval_Type(Integer32):
    """Custom type hpnicfTunnelEviKeepaliveInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32767),
    )


_HpnicfTunnelEviKeepaliveInterval_Type.__name__ = "Integer32"
_HpnicfTunnelEviKeepaliveInterval_Object = MibTableColumn
hpnicfTunnelEviKeepaliveInterval = _HpnicfTunnelEviKeepaliveInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 53, 1, 1, 4, 1, 7),
    _HpnicfTunnelEviKeepaliveInterval_Type()
)
hpnicfTunnelEviKeepaliveInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfTunnelEviKeepaliveInterval.setStatus("current")


class _HpnicfTunnelEviKeepaliveTimes_Type(Integer32):
    """Custom type hpnicfTunnelEviKeepaliveTimes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_HpnicfTunnelEviKeepaliveTimes_Type.__name__ = "Integer32"
_HpnicfTunnelEviKeepaliveTimes_Object = MibTableColumn
hpnicfTunnelEviKeepaliveTimes = _HpnicfTunnelEviKeepaliveTimes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 53, 1, 1, 4, 1, 8),
    _HpnicfTunnelEviKeepaliveTimes_Type()
)
hpnicfTunnelEviKeepaliveTimes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfTunnelEviKeepaliveTimes.setStatus("current")
_HpnicfTunnelEviLinkTable_Object = MibTable
hpnicfTunnelEviLinkTable = _HpnicfTunnelEviLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 53, 1, 1, 5)
)
if mibBuilder.loadTexts:
    hpnicfTunnelEviLinkTable.setStatus("current")
_HpnicfTunnelEviLinkEntry_Object = MibTableRow
hpnicfTunnelEviLinkEntry = _HpnicfTunnelEviLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 53, 1, 1, 5, 1)
)
hpnicfTunnelEviLinkEntry.setIndexNames(
    (0, "HPN-ICF-TUNNEL-MIB", "hpnicfTunnelEviTunnNum"),
    (0, "HPN-ICF-TUNNEL-MIB", "hpnicfTunnelEviLinkNum"),
)
if mibBuilder.loadTexts:
    hpnicfTunnelEviLinkEntry.setStatus("current")


class _HpnicfTunnelEviLinkNum_Type(Integer32):
    """Custom type hpnicfTunnelEviLinkNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpnicfTunnelEviLinkNum_Type.__name__ = "Integer32"
_HpnicfTunnelEviLinkNum_Object = MibTableColumn
hpnicfTunnelEviLinkNum = _HpnicfTunnelEviLinkNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 53, 1, 1, 5, 1, 1),
    _HpnicfTunnelEviLinkNum_Type()
)
hpnicfTunnelEviLinkNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfTunnelEviLinkNum.setStatus("current")
_HpnicfTunnelEviLinkIfIndex_Type = InterfaceIndex
_HpnicfTunnelEviLinkIfIndex_Object = MibTableColumn
hpnicfTunnelEviLinkIfIndex = _HpnicfTunnelEviLinkIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 53, 1, 1, 5, 1, 2),
    _HpnicfTunnelEviLinkIfIndex_Type()
)
hpnicfTunnelEviLinkIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfTunnelEviLinkIfIndex.setStatus("current")
_HpnicfTunnelEviLinkAddressType_Type = InetAddressType
_HpnicfTunnelEviLinkAddressType_Object = MibTableColumn
hpnicfTunnelEviLinkAddressType = _HpnicfTunnelEviLinkAddressType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 53, 1, 1, 5, 1, 3),
    _HpnicfTunnelEviLinkAddressType_Type()
)
hpnicfTunnelEviLinkAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfTunnelEviLinkAddressType.setStatus("current")
_HpnicfTunnelEviLinkRemoteAddr_Type = InetAddress
_HpnicfTunnelEviLinkRemoteAddr_Object = MibTableColumn
hpnicfTunnelEviLinkRemoteAddr = _HpnicfTunnelEviLinkRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 53, 1, 1, 5, 1, 4),
    _HpnicfTunnelEviLinkRemoteAddr_Type()
)
hpnicfTunnelEviLinkRemoteAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfTunnelEviLinkRemoteAddr.setStatus("current")
_HpnicfTunnelGreTable_Object = MibTable
hpnicfTunnelGreTable = _HpnicfTunnelGreTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 53, 1, 1, 6)
)
if mibBuilder.loadTexts:
    hpnicfTunnelGreTable.setStatus("current")
_HpnicfTunnelGreEntry_Object = MibTableRow
hpnicfTunnelGreEntry = _HpnicfTunnelGreEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 53, 1, 1, 6, 1)
)
hpnicfTunnelGreEntry.setIndexNames(
    (0, "HPN-ICF-TUNNEL-MIB", "hpnicfTunnelGreTunnNum"),
)
if mibBuilder.loadTexts:
    hpnicfTunnelGreEntry.setStatus("current")


class _HpnicfTunnelGreTunnNum_Type(Integer32):
    """Custom type hpnicfTunnelGreTunnNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpnicfTunnelGreTunnNum_Type.__name__ = "Integer32"
_HpnicfTunnelGreTunnNum_Object = MibTableColumn
hpnicfTunnelGreTunnNum = _HpnicfTunnelGreTunnNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 53, 1, 1, 6, 1, 1),
    _HpnicfTunnelGreTunnNum_Type()
)
hpnicfTunnelGreTunnNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfTunnelGreTunnNum.setStatus("current")
_HpnicfTunnelGreTunnIfIndex_Type = InterfaceIndex
_HpnicfTunnelGreTunnIfIndex_Object = MibTableColumn
hpnicfTunnelGreTunnIfIndex = _HpnicfTunnelGreTunnIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 53, 1, 1, 6, 1, 2),
    _HpnicfTunnelGreTunnIfIndex_Type()
)
hpnicfTunnelGreTunnIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfTunnelGreTunnIfIndex.setStatus("current")
_HpnicfTunnelGreAddressType_Type = InetAddressType
_HpnicfTunnelGreAddressType_Object = MibTableColumn
hpnicfTunnelGreAddressType = _HpnicfTunnelGreAddressType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 53, 1, 1, 6, 1, 3),
    _HpnicfTunnelGreAddressType_Type()
)
hpnicfTunnelGreAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfTunnelGreAddressType.setStatus("current")
_HpnicfTunnelGreLocalAddr_Type = InetAddress
_HpnicfTunnelGreLocalAddr_Object = MibTableColumn
hpnicfTunnelGreLocalAddr = _HpnicfTunnelGreLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 53, 1, 1, 6, 1, 4),
    _HpnicfTunnelGreLocalAddr_Type()
)
hpnicfTunnelGreLocalAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfTunnelGreLocalAddr.setStatus("current")
_HpnicfTunnelGreRemoteAddr_Type = InetAddress
_HpnicfTunnelGreRemoteAddr_Object = MibTableColumn
hpnicfTunnelGreRemoteAddr = _HpnicfTunnelGreRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 53, 1, 1, 6, 1, 5),
    _HpnicfTunnelGreRemoteAddr_Type()
)
hpnicfTunnelGreRemoteAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfTunnelGreRemoteAddr.setStatus("current")


class _HpnicfTunnelGreKeepaliveEnabled_Type(TruthValue):
    """Custom type hpnicfTunnelGreKeepaliveEnabled based on TruthValue"""


_HpnicfTunnelGreKeepaliveEnabled_Object = MibTableColumn
hpnicfTunnelGreKeepaliveEnabled = _HpnicfTunnelGreKeepaliveEnabled_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 53, 1, 1, 6, 1, 6),
    _HpnicfTunnelGreKeepaliveEnabled_Type()
)
hpnicfTunnelGreKeepaliveEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfTunnelGreKeepaliveEnabled.setStatus("current")


class _HpnicfTunnelGreKeepaliveInterval_Type(Integer32):
    """Custom type hpnicfTunnelGreKeepaliveInterval based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_HpnicfTunnelGreKeepaliveInterval_Type.__name__ = "Integer32"
_HpnicfTunnelGreKeepaliveInterval_Object = MibTableColumn
hpnicfTunnelGreKeepaliveInterval = _HpnicfTunnelGreKeepaliveInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 53, 1, 1, 6, 1, 7),
    _HpnicfTunnelGreKeepaliveInterval_Type()
)
hpnicfTunnelGreKeepaliveInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfTunnelGreKeepaliveInterval.setStatus("current")


class _HpnicfTunnelGreKeepaliveTimes_Type(Integer32):
    """Custom type hpnicfTunnelGreKeepaliveTimes based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpnicfTunnelGreKeepaliveTimes_Type.__name__ = "Integer32"
_HpnicfTunnelGreKeepaliveTimes_Object = MibTableColumn
hpnicfTunnelGreKeepaliveTimes = _HpnicfTunnelGreKeepaliveTimes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 53, 1, 1, 6, 1, 8),
    _HpnicfTunnelGreKeepaliveTimes_Type()
)
hpnicfTunnelGreKeepaliveTimes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfTunnelGreKeepaliveTimes.setStatus("current")


class _HpnicfTunnelGreSlbgGroupNum_Type(Unsigned32):
    """Custom type hpnicfTunnelGreSlbgGroupNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HpnicfTunnelGreSlbgGroupNum_Type.__name__ = "Unsigned32"
_HpnicfTunnelGreSlbgGroupNum_Object = MibTableColumn
hpnicfTunnelGreSlbgGroupNum = _HpnicfTunnelGreSlbgGroupNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 53, 1, 1, 6, 1, 9),
    _HpnicfTunnelGreSlbgGroupNum_Type()
)
hpnicfTunnelGreSlbgGroupNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfTunnelGreSlbgGroupNum.setStatus("current")
_HpnicfTunnelGreTunnStatus_Type = RowStatus
_HpnicfTunnelGreTunnStatus_Object = MibTableColumn
hpnicfTunnelGreTunnStatus = _HpnicfTunnelGreTunnStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 53, 1, 1, 6, 1, 10),
    _HpnicfTunnelGreTunnStatus_Type()
)
hpnicfTunnelGreTunnStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfTunnelGreTunnStatus.setStatus("current")
_HpnicfTunnelVxlanIfTable_Object = MibTable
hpnicfTunnelVxlanIfTable = _HpnicfTunnelVxlanIfTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 53, 1, 1, 7)
)
if mibBuilder.loadTexts:
    hpnicfTunnelVxlanIfTable.setStatus("current")
_HpnicfTunnelVxlanIfEntry_Object = MibTableRow
hpnicfTunnelVxlanIfEntry = _HpnicfTunnelVxlanIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 53, 1, 1, 7, 1)
)
hpnicfTunnelVxlanIfEntry.setIndexNames(
    (0, "HPN-ICF-TUNNEL-MIB", "hpnicfTunnelVxlanIfTunnNum"),
)
if mibBuilder.loadTexts:
    hpnicfTunnelVxlanIfEntry.setStatus("current")


class _HpnicfTunnelVxlanIfTunnNum_Type(Integer32):
    """Custom type hpnicfTunnelVxlanIfTunnNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpnicfTunnelVxlanIfTunnNum_Type.__name__ = "Integer32"
_HpnicfTunnelVxlanIfTunnNum_Object = MibTableColumn
hpnicfTunnelVxlanIfTunnNum = _HpnicfTunnelVxlanIfTunnNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 53, 1, 1, 7, 1, 1),
    _HpnicfTunnelVxlanIfTunnNum_Type()
)
hpnicfTunnelVxlanIfTunnNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfTunnelVxlanIfTunnNum.setStatus("current")
_HpnicfTunnelVxlanTunnIfIndex_Type = InterfaceIndex
_HpnicfTunnelVxlanTunnIfIndex_Object = MibTableColumn
hpnicfTunnelVxlanTunnIfIndex = _HpnicfTunnelVxlanTunnIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 53, 1, 1, 7, 1, 2),
    _HpnicfTunnelVxlanTunnIfIndex_Type()
)
hpnicfTunnelVxlanTunnIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfTunnelVxlanTunnIfIndex.setStatus("current")
_HpnicfTunnelVxlanIfAddressType_Type = InetAddressType
_HpnicfTunnelVxlanIfAddressType_Object = MibTableColumn
hpnicfTunnelVxlanIfAddressType = _HpnicfTunnelVxlanIfAddressType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 53, 1, 1, 7, 1, 3),
    _HpnicfTunnelVxlanIfAddressType_Type()
)
hpnicfTunnelVxlanIfAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfTunnelVxlanIfAddressType.setStatus("current")
_HpnicfTunnelVxlanIfLocalAddr_Type = InetAddress
_HpnicfTunnelVxlanIfLocalAddr_Object = MibTableColumn
hpnicfTunnelVxlanIfLocalAddr = _HpnicfTunnelVxlanIfLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 53, 1, 1, 7, 1, 4),
    _HpnicfTunnelVxlanIfLocalAddr_Type()
)
hpnicfTunnelVxlanIfLocalAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfTunnelVxlanIfLocalAddr.setStatus("current")
_HpnicfTunnelVxlanIfRemoteAddr_Type = InetAddress
_HpnicfTunnelVxlanIfRemoteAddr_Object = MibTableColumn
hpnicfTunnelVxlanIfRemoteAddr = _HpnicfTunnelVxlanIfRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 53, 1, 1, 7, 1, 5),
    _HpnicfTunnelVxlanIfRemoteAddr_Type()
)
hpnicfTunnelVxlanIfRemoteAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfTunnelVxlanIfRemoteAddr.setStatus("current")
_HpnicfTunnelVxlanIfStatus_Type = RowStatus
_HpnicfTunnelVxlanIfStatus_Object = MibTableColumn
hpnicfTunnelVxlanIfStatus = _HpnicfTunnelVxlanIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 53, 1, 1, 7, 1, 6),
    _HpnicfTunnelVxlanIfStatus_Type()
)
hpnicfTunnelVxlanIfStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfTunnelVxlanIfStatus.setStatus("current")
_HpnicfTunnelVxlanConfigGroup_ObjectIdentity = ObjectIdentity
hpnicfTunnelVxlanConfigGroup = _HpnicfTunnelVxlanConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 53, 1, 1, 8)
)


class _HpnicfTunnelVxlanUdpPort_Type(Integer32):
    """Custom type hpnicfTunnelVxlanUdpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpnicfTunnelVxlanUdpPort_Type.__name__ = "Integer32"
_HpnicfTunnelVxlanUdpPort_Object = MibScalar
hpnicfTunnelVxlanUdpPort = _HpnicfTunnelVxlanUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 53, 1, 1, 8, 1),
    _HpnicfTunnelVxlanUdpPort_Type()
)
hpnicfTunnelVxlanUdpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfTunnelVxlanUdpPort.setStatus("current")
_HpnicfTunnelVxlanDropWrongCksmPkt_Type = TruthValue
_HpnicfTunnelVxlanDropWrongCksmPkt_Object = MibScalar
hpnicfTunnelVxlanDropWrongCksmPkt = _HpnicfTunnelVxlanDropWrongCksmPkt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 53, 1, 1, 8, 2),
    _HpnicfTunnelVxlanDropWrongCksmPkt_Type()
)
hpnicfTunnelVxlanDropWrongCksmPkt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfTunnelVxlanDropWrongCksmPkt.setStatus("current")
_HpnicfTunnelVxlanDropVlanTagPkt_Type = TruthValue
_HpnicfTunnelVxlanDropVlanTagPkt_Object = MibScalar
hpnicfTunnelVxlanDropVlanTagPkt = _HpnicfTunnelVxlanDropVlanTagPkt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 53, 1, 1, 8, 3),
    _HpnicfTunnelVxlanDropVlanTagPkt_Type()
)
hpnicfTunnelVxlanDropVlanTagPkt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfTunnelVxlanDropVlanTagPkt.setStatus("current")
_HpnicfTunnelAvailableIDGroup_ObjectIdentity = ObjectIdentity
hpnicfTunnelAvailableIDGroup = _HpnicfTunnelAvailableIDGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 53, 1, 1, 9)
)


class _HpnicfTunnelAvailableID_Type(Integer32):
    """Custom type hpnicfTunnelAvailableID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 2147483647),
    )


_HpnicfTunnelAvailableID_Type.__name__ = "Integer32"
_HpnicfTunnelAvailableID_Object = MibScalar
hpnicfTunnelAvailableID = _HpnicfTunnelAvailableID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 53, 1, 1, 9, 1),
    _HpnicfTunnelAvailableID_Type()
)
hpnicfTunnelAvailableID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfTunnelAvailableID.setStatus("current")
_HpnicfTunnelTotalNumTable_Object = MibTable
hpnicfTunnelTotalNumTable = _HpnicfTunnelTotalNumTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 53, 1, 1, 10)
)
if mibBuilder.loadTexts:
    hpnicfTunnelTotalNumTable.setStatus("current")
_HpnicfTunnelTotalNumEntry_Object = MibTableRow
hpnicfTunnelTotalNumEntry = _HpnicfTunnelTotalNumEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 53, 1, 1, 10, 1)
)
hpnicfTunnelTotalNumEntry.setIndexNames(
    (0, "HPN-ICF-TUNNEL-MIB", "hpnicfTunnelEncapsMethod"),
)
if mibBuilder.loadTexts:
    hpnicfTunnelTotalNumEntry.setStatus("current")
_HpnicfTunnelEncapsMethod_Type = HpnicfTunnelType
_HpnicfTunnelEncapsMethod_Object = MibTableColumn
hpnicfTunnelEncapsMethod = _HpnicfTunnelEncapsMethod_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 53, 1, 1, 10, 1, 1),
    _HpnicfTunnelEncapsMethod_Type()
)
hpnicfTunnelEncapsMethod.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfTunnelEncapsMethod.setStatus("current")
_HpnicfTunnelTotalNum_Type = Unsigned32
_HpnicfTunnelTotalNum_Object = MibTableColumn
hpnicfTunnelTotalNum = _HpnicfTunnelTotalNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 53, 1, 1, 10, 1, 2),
    _HpnicfTunnelTotalNum_Type()
)
hpnicfTunnelTotalNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfTunnelTotalNum.setStatus("current")
_HpnicfTunnelNvgreIfTable_Object = MibTable
hpnicfTunnelNvgreIfTable = _HpnicfTunnelNvgreIfTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 53, 1, 1, 11)
)
if mibBuilder.loadTexts:
    hpnicfTunnelNvgreIfTable.setStatus("current")
_HpnicfTunnelNvgreIfEntry_Object = MibTableRow
hpnicfTunnelNvgreIfEntry = _HpnicfTunnelNvgreIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 53, 1, 1, 11, 1)
)
hpnicfTunnelNvgreIfEntry.setIndexNames(
    (0, "HPN-ICF-TUNNEL-MIB", "hpnicfTunnelNvgreIfTunnNum"),
)
if mibBuilder.loadTexts:
    hpnicfTunnelNvgreIfEntry.setStatus("current")


class _HpnicfTunnelNvgreIfTunnNum_Type(Integer32):
    """Custom type hpnicfTunnelNvgreIfTunnNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpnicfTunnelNvgreIfTunnNum_Type.__name__ = "Integer32"
_HpnicfTunnelNvgreIfTunnNum_Object = MibTableColumn
hpnicfTunnelNvgreIfTunnNum = _HpnicfTunnelNvgreIfTunnNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 53, 1, 1, 11, 1, 1),
    _HpnicfTunnelNvgreIfTunnNum_Type()
)
hpnicfTunnelNvgreIfTunnNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfTunnelNvgreIfTunnNum.setStatus("current")
_HpnicfTunnelNvgreTunnIfIndex_Type = InterfaceIndex
_HpnicfTunnelNvgreTunnIfIndex_Object = MibTableColumn
hpnicfTunnelNvgreTunnIfIndex = _HpnicfTunnelNvgreTunnIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 53, 1, 1, 11, 1, 2),
    _HpnicfTunnelNvgreTunnIfIndex_Type()
)
hpnicfTunnelNvgreTunnIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfTunnelNvgreTunnIfIndex.setStatus("current")
_HpnicfTunnelNvgreIfAddressType_Type = InetAddressType
_HpnicfTunnelNvgreIfAddressType_Object = MibTableColumn
hpnicfTunnelNvgreIfAddressType = _HpnicfTunnelNvgreIfAddressType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 53, 1, 1, 11, 1, 3),
    _HpnicfTunnelNvgreIfAddressType_Type()
)
hpnicfTunnelNvgreIfAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfTunnelNvgreIfAddressType.setStatus("current")
_HpnicfTunnelNvgreIfLocalAddr_Type = InetAddress
_HpnicfTunnelNvgreIfLocalAddr_Object = MibTableColumn
hpnicfTunnelNvgreIfLocalAddr = _HpnicfTunnelNvgreIfLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 53, 1, 1, 11, 1, 4),
    _HpnicfTunnelNvgreIfLocalAddr_Type()
)
hpnicfTunnelNvgreIfLocalAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfTunnelNvgreIfLocalAddr.setStatus("current")
_HpnicfTunnelNvgreIfRemoteAddr_Type = InetAddress
_HpnicfTunnelNvgreIfRemoteAddr_Object = MibTableColumn
hpnicfTunnelNvgreIfRemoteAddr = _HpnicfTunnelNvgreIfRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 53, 1, 1, 11, 1, 5),
    _HpnicfTunnelNvgreIfRemoteAddr_Type()
)
hpnicfTunnelNvgreIfRemoteAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfTunnelNvgreIfRemoteAddr.setStatus("current")
_HpnicfTunnelNvgreIfStatus_Type = RowStatus
_HpnicfTunnelNvgreIfStatus_Object = MibTableColumn
hpnicfTunnelNvgreIfStatus = _HpnicfTunnelNvgreIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 53, 1, 1, 11, 1, 6),
    _HpnicfTunnelNvgreIfStatus_Type()
)
hpnicfTunnelNvgreIfStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfTunnelNvgreIfStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-TUNNEL-MIB",
    **{"HpnicfTunnelType": HpnicfTunnelType,
       "hpnicfTunnel": hpnicfTunnel,
       "hpnicfTunnelMIBObjects": hpnicfTunnelMIBObjects,
       "hpnicfTunnelTables": hpnicfTunnelTables,
       "hpnicfTunnelIfTable": hpnicfTunnelIfTable,
       "hpnicfTunnelIfEntry": hpnicfTunnelIfEntry,
       "hpnicfTunnelIfEncapsMethod": hpnicfTunnelIfEncapsMethod,
       "hpnicfTunnelIfHopLimit": hpnicfTunnelIfHopLimit,
       "hpnicfTunnelIfSecurity": hpnicfTunnelIfSecurity,
       "hpnicfTunnelIfTOS": hpnicfTunnelIfTOS,
       "hpnicfTunnelIfFlowLabel": hpnicfTunnelIfFlowLabel,
       "hpnicfTunnelIfAddressType": hpnicfTunnelIfAddressType,
       "hpnicfTunnelIfLocalInetAddress": hpnicfTunnelIfLocalInetAddress,
       "hpnicfTunnelIfRemoteInetAddress": hpnicfTunnelIfRemoteInetAddress,
       "hpnicfTunnelIfEncapsLimit": hpnicfTunnelIfEncapsLimit,
       "hpnicfTunnelInetConfigTable": hpnicfTunnelInetConfigTable,
       "hpnicfTunnelInetConfigEntry": hpnicfTunnelInetConfigEntry,
       "hpnicfTunnelInetConfigSlot": hpnicfTunnelInetConfigSlot,
       "hpnicfTunnelInetConfigSubSlot": hpnicfTunnelInetConfigSubSlot,
       "hpnicfTunnelInetConfigTunnNum": hpnicfTunnelInetConfigTunnNum,
       "hpnicfTunnelInetConfigIfIndex": hpnicfTunnelInetConfigIfIndex,
       "hpnicfTunnelInetConfigStatus": hpnicfTunnelInetConfigStatus,
       "hpnicfTunnelEviTable": hpnicfTunnelEviTable,
       "hpnicfTunnelEviEntry": hpnicfTunnelEviEntry,
       "hpnicfTunnelEviTunnNum": hpnicfTunnelEviTunnNum,
       "hpnicfTunnelEviIfIndex": hpnicfTunnelEviIfIndex,
       "hpnicfTunnelEviStatus": hpnicfTunnelEviStatus,
       "hpnicfTunnelEviAddressType": hpnicfTunnelEviAddressType,
       "hpnicfTunnelEviLocalAddr": hpnicfTunnelEviLocalAddr,
       "hpnicfTunnelEviNetworkID": hpnicfTunnelEviNetworkID,
       "hpnicfTunnelEviKeepaliveInterval": hpnicfTunnelEviKeepaliveInterval,
       "hpnicfTunnelEviKeepaliveTimes": hpnicfTunnelEviKeepaliveTimes,
       "hpnicfTunnelEviLinkTable": hpnicfTunnelEviLinkTable,
       "hpnicfTunnelEviLinkEntry": hpnicfTunnelEviLinkEntry,
       "hpnicfTunnelEviLinkNum": hpnicfTunnelEviLinkNum,
       "hpnicfTunnelEviLinkIfIndex": hpnicfTunnelEviLinkIfIndex,
       "hpnicfTunnelEviLinkAddressType": hpnicfTunnelEviLinkAddressType,
       "hpnicfTunnelEviLinkRemoteAddr": hpnicfTunnelEviLinkRemoteAddr,
       "hpnicfTunnelGreTable": hpnicfTunnelGreTable,
       "hpnicfTunnelGreEntry": hpnicfTunnelGreEntry,
       "hpnicfTunnelGreTunnNum": hpnicfTunnelGreTunnNum,
       "hpnicfTunnelGreTunnIfIndex": hpnicfTunnelGreTunnIfIndex,
       "hpnicfTunnelGreAddressType": hpnicfTunnelGreAddressType,
       "hpnicfTunnelGreLocalAddr": hpnicfTunnelGreLocalAddr,
       "hpnicfTunnelGreRemoteAddr": hpnicfTunnelGreRemoteAddr,
       "hpnicfTunnelGreKeepaliveEnabled": hpnicfTunnelGreKeepaliveEnabled,
       "hpnicfTunnelGreKeepaliveInterval": hpnicfTunnelGreKeepaliveInterval,
       "hpnicfTunnelGreKeepaliveTimes": hpnicfTunnelGreKeepaliveTimes,
       "hpnicfTunnelGreSlbgGroupNum": hpnicfTunnelGreSlbgGroupNum,
       "hpnicfTunnelGreTunnStatus": hpnicfTunnelGreTunnStatus,
       "hpnicfTunnelVxlanIfTable": hpnicfTunnelVxlanIfTable,
       "hpnicfTunnelVxlanIfEntry": hpnicfTunnelVxlanIfEntry,
       "hpnicfTunnelVxlanIfTunnNum": hpnicfTunnelVxlanIfTunnNum,
       "hpnicfTunnelVxlanTunnIfIndex": hpnicfTunnelVxlanTunnIfIndex,
       "hpnicfTunnelVxlanIfAddressType": hpnicfTunnelVxlanIfAddressType,
       "hpnicfTunnelVxlanIfLocalAddr": hpnicfTunnelVxlanIfLocalAddr,
       "hpnicfTunnelVxlanIfRemoteAddr": hpnicfTunnelVxlanIfRemoteAddr,
       "hpnicfTunnelVxlanIfStatus": hpnicfTunnelVxlanIfStatus,
       "hpnicfTunnelVxlanConfigGroup": hpnicfTunnelVxlanConfigGroup,
       "hpnicfTunnelVxlanUdpPort": hpnicfTunnelVxlanUdpPort,
       "hpnicfTunnelVxlanDropWrongCksmPkt": hpnicfTunnelVxlanDropWrongCksmPkt,
       "hpnicfTunnelVxlanDropVlanTagPkt": hpnicfTunnelVxlanDropVlanTagPkt,
       "hpnicfTunnelAvailableIDGroup": hpnicfTunnelAvailableIDGroup,
       "hpnicfTunnelAvailableID": hpnicfTunnelAvailableID,
       "hpnicfTunnelTotalNumTable": hpnicfTunnelTotalNumTable,
       "hpnicfTunnelTotalNumEntry": hpnicfTunnelTotalNumEntry,
       "hpnicfTunnelEncapsMethod": hpnicfTunnelEncapsMethod,
       "hpnicfTunnelTotalNum": hpnicfTunnelTotalNum,
       "hpnicfTunnelNvgreIfTable": hpnicfTunnelNvgreIfTable,
       "hpnicfTunnelNvgreIfEntry": hpnicfTunnelNvgreIfEntry,
       "hpnicfTunnelNvgreIfTunnNum": hpnicfTunnelNvgreIfTunnNum,
       "hpnicfTunnelNvgreTunnIfIndex": hpnicfTunnelNvgreTunnIfIndex,
       "hpnicfTunnelNvgreIfAddressType": hpnicfTunnelNvgreIfAddressType,
       "hpnicfTunnelNvgreIfLocalAddr": hpnicfTunnelNvgreIfLocalAddr,
       "hpnicfTunnelNvgreIfRemoteAddr": hpnicfTunnelNvgreIfRemoteAddr,
       "hpnicfTunnelNvgreIfStatus": hpnicfTunnelNvgreIfStatus}
)
