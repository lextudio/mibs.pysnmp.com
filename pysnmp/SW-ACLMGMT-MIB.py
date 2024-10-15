# SNMP MIB module (SW-ACLMGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SW-ACLMGMT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:58:47 2024
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

(dlink_mgmt,) = mibBuilder.importSymbols(
    "DLINK-ID-REC-MIB",
    "dlink-mgmt")

(PortList,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

swAclMgmtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 5)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SwAclMaskMgmt_ObjectIdentity = ObjectIdentity
swAclMaskMgmt = _SwAclMaskMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 5, 1)
)
_SwACLEthernetTable_Object = MibTable
swACLEthernetTable = _SwACLEthernetTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 5, 1, 1)
)
if mibBuilder.loadTexts:
    swACLEthernetTable.setStatus("current")
_SwACLEthernetEntry_Object = MibTableRow
swACLEthernetEntry = _SwACLEthernetEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 5, 1, 1, 1)
)
swACLEthernetEntry.setIndexNames(
    (0, "SW-ACLMGMT-MIB", "swACLEthernetProfileID"),
)
if mibBuilder.loadTexts:
    swACLEthernetEntry.setStatus("current")


class _SwACLEthernetProfileID_Type(Integer32):
    """Custom type swACLEthernetProfileID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SwACLEthernetProfileID_Type.__name__ = "Integer32"
_SwACLEthernetProfileID_Object = MibTableColumn
swACLEthernetProfileID = _SwACLEthernetProfileID_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 5, 1, 1, 1, 1),
    _SwACLEthernetProfileID_Type()
)
swACLEthernetProfileID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swACLEthernetProfileID.setStatus("current")


class _SwACLEthernetUsevlan_Type(Integer32):
    """Custom type swACLEthernetUsevlan based on Integer32"""
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


_SwACLEthernetUsevlan_Type.__name__ = "Integer32"
_SwACLEthernetUsevlan_Object = MibTableColumn
swACLEthernetUsevlan = _SwACLEthernetUsevlan_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 5, 1, 1, 1, 2),
    _SwACLEthernetUsevlan_Type()
)
swACLEthernetUsevlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLEthernetUsevlan.setStatus("current")


class _SwACLEthernetMacAddrMaskState_Type(Integer32):
    """Custom type swACLEthernetMacAddrMaskState based on Integer32"""
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
        *(("dst-mac-addr", 2),
          ("dst-src-mac-addr", 4),
          ("other", 1),
          ("src-mac-addr", 3))
    )


_SwACLEthernetMacAddrMaskState_Type.__name__ = "Integer32"
_SwACLEthernetMacAddrMaskState_Object = MibTableColumn
swACLEthernetMacAddrMaskState = _SwACLEthernetMacAddrMaskState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 5, 1, 1, 1, 3),
    _SwACLEthernetMacAddrMaskState_Type()
)
swACLEthernetMacAddrMaskState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLEthernetMacAddrMaskState.setStatus("current")
_SwACLEthernetSrcMacAddrMask_Type = MacAddress
_SwACLEthernetSrcMacAddrMask_Object = MibTableColumn
swACLEthernetSrcMacAddrMask = _SwACLEthernetSrcMacAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 5, 1, 1, 1, 4),
    _SwACLEthernetSrcMacAddrMask_Type()
)
swACLEthernetSrcMacAddrMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLEthernetSrcMacAddrMask.setStatus("current")
_SwACLEthernetDstMacAddrMask_Type = MacAddress
_SwACLEthernetDstMacAddrMask_Object = MibTableColumn
swACLEthernetDstMacAddrMask = _SwACLEthernetDstMacAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 5, 1, 1, 1, 5),
    _SwACLEthernetDstMacAddrMask_Type()
)
swACLEthernetDstMacAddrMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLEthernetDstMacAddrMask.setStatus("current")


class _SwACLEthernetUse8021p_Type(Integer32):
    """Custom type swACLEthernetUse8021p based on Integer32"""
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


_SwACLEthernetUse8021p_Type.__name__ = "Integer32"
_SwACLEthernetUse8021p_Object = MibTableColumn
swACLEthernetUse8021p = _SwACLEthernetUse8021p_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 5, 1, 1, 1, 6),
    _SwACLEthernetUse8021p_Type()
)
swACLEthernetUse8021p.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLEthernetUse8021p.setStatus("current")


class _SwACLEthernetUseEthernetType_Type(Integer32):
    """Custom type swACLEthernetUseEthernetType based on Integer32"""
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


_SwACLEthernetUseEthernetType_Type.__name__ = "Integer32"
_SwACLEthernetUseEthernetType_Object = MibTableColumn
swACLEthernetUseEthernetType = _SwACLEthernetUseEthernetType_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 5, 1, 1, 1, 7),
    _SwACLEthernetUseEthernetType_Type()
)
swACLEthernetUseEthernetType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLEthernetUseEthernetType.setStatus("current")
_SwACLEthernetPort_Type = PortList
_SwACLEthernetPort_Object = MibTableColumn
swACLEthernetPort = _SwACLEthernetPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 5, 1, 1, 1, 8),
    _SwACLEthernetPort_Type()
)
swACLEthernetPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLEthernetPort.setStatus("current")
_SwACLEthernetRowStatus_Type = RowStatus
_SwACLEthernetRowStatus_Object = MibTableColumn
swACLEthernetRowStatus = _SwACLEthernetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 5, 1, 1, 1, 9),
    _SwACLEthernetRowStatus_Type()
)
swACLEthernetRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLEthernetRowStatus.setStatus("current")
_SwACLIpTable_Object = MibTable
swACLIpTable = _SwACLIpTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 5, 1, 2)
)
if mibBuilder.loadTexts:
    swACLIpTable.setStatus("current")
_SwACLIpEntry_Object = MibTableRow
swACLIpEntry = _SwACLIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 5, 1, 2, 1)
)
swACLIpEntry.setIndexNames(
    (0, "SW-ACLMGMT-MIB", "swACLIpProfileID"),
)
if mibBuilder.loadTexts:
    swACLIpEntry.setStatus("current")


class _SwACLIpProfileID_Type(Integer32):
    """Custom type swACLIpProfileID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SwACLIpProfileID_Type.__name__ = "Integer32"
_SwACLIpProfileID_Object = MibTableColumn
swACLIpProfileID = _SwACLIpProfileID_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 5, 1, 2, 1, 1),
    _SwACLIpProfileID_Type()
)
swACLIpProfileID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swACLIpProfileID.setStatus("current")


class _SwACLIpUsevlan_Type(Integer32):
    """Custom type swACLIpUsevlan based on Integer32"""
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


_SwACLIpUsevlan_Type.__name__ = "Integer32"
_SwACLIpUsevlan_Object = MibTableColumn
swACLIpUsevlan = _SwACLIpUsevlan_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 5, 1, 2, 1, 2),
    _SwACLIpUsevlan_Type()
)
swACLIpUsevlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLIpUsevlan.setStatus("current")


class _SwACLIpIpAddrMaskState_Type(Integer32):
    """Custom type swACLIpIpAddrMaskState based on Integer32"""
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
        *(("dst-ip-addr", 2),
          ("dst-src-ip-addr", 4),
          ("other", 1),
          ("src-ip-addr", 3))
    )


_SwACLIpIpAddrMaskState_Type.__name__ = "Integer32"
_SwACLIpIpAddrMaskState_Object = MibTableColumn
swACLIpIpAddrMaskState = _SwACLIpIpAddrMaskState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 5, 1, 2, 1, 3),
    _SwACLIpIpAddrMaskState_Type()
)
swACLIpIpAddrMaskState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLIpIpAddrMaskState.setStatus("current")
_SwACLIpSrcIpAddrMask_Type = IpAddress
_SwACLIpSrcIpAddrMask_Object = MibTableColumn
swACLIpSrcIpAddrMask = _SwACLIpSrcIpAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 5, 1, 2, 1, 4),
    _SwACLIpSrcIpAddrMask_Type()
)
swACLIpSrcIpAddrMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLIpSrcIpAddrMask.setStatus("current")
_SwACLIpDstIpAddrMask_Type = IpAddress
_SwACLIpDstIpAddrMask_Object = MibTableColumn
swACLIpDstIpAddrMask = _SwACLIpDstIpAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 5, 1, 2, 1, 5),
    _SwACLIpDstIpAddrMask_Type()
)
swACLIpDstIpAddrMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLIpDstIpAddrMask.setStatus("current")


class _SwACLIpUseDSCP_Type(Integer32):
    """Custom type swACLIpUseDSCP based on Integer32"""
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


_SwACLIpUseDSCP_Type.__name__ = "Integer32"
_SwACLIpUseDSCP_Object = MibTableColumn
swACLIpUseDSCP = _SwACLIpUseDSCP_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 5, 1, 2, 1, 6),
    _SwACLIpUseDSCP_Type()
)
swACLIpUseDSCP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLIpUseDSCP.setStatus("current")


class _SwACLIpUseProtoType_Type(Integer32):
    """Custom type swACLIpUseProtoType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("icmp", 2),
          ("igmp", 3),
          ("none", 1),
          ("protocolId", 6),
          ("tcp", 4),
          ("udp", 5))
    )


_SwACLIpUseProtoType_Type.__name__ = "Integer32"
_SwACLIpUseProtoType_Object = MibTableColumn
swACLIpUseProtoType = _SwACLIpUseProtoType_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 5, 1, 2, 1, 7),
    _SwACLIpUseProtoType_Type()
)
swACLIpUseProtoType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLIpUseProtoType.setStatus("current")


class _SwACLIpIcmpOption_Type(Integer32):
    """Custom type swACLIpIcmpOption based on Integer32"""
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
        *(("code", 3),
          ("none", 1),
          ("type", 2),
          ("type-code", 4))
    )


_SwACLIpIcmpOption_Type.__name__ = "Integer32"
_SwACLIpIcmpOption_Object = MibTableColumn
swACLIpIcmpOption = _SwACLIpIcmpOption_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 5, 1, 2, 1, 8),
    _SwACLIpIcmpOption_Type()
)
swACLIpIcmpOption.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLIpIcmpOption.setStatus("current")


class _SwACLIpIgmpOption_Type(Integer32):
    """Custom type swACLIpIgmpOption based on Integer32"""
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


_SwACLIpIgmpOption_Type.__name__ = "Integer32"
_SwACLIpIgmpOption_Object = MibTableColumn
swACLIpIgmpOption = _SwACLIpIgmpOption_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 5, 1, 2, 1, 9),
    _SwACLIpIgmpOption_Type()
)
swACLIpIgmpOption.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLIpIgmpOption.setStatus("current")


class _SwACLIpTcpOption_Type(Integer32):
    """Custom type swACLIpTcpOption based on Integer32"""
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
        *(("dst-addr", 2),
          ("dst-src-addr", 4),
          ("other", 1),
          ("src-addr", 3))
    )


_SwACLIpTcpOption_Type.__name__ = "Integer32"
_SwACLIpTcpOption_Object = MibTableColumn
swACLIpTcpOption = _SwACLIpTcpOption_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 5, 1, 2, 1, 10),
    _SwACLIpTcpOption_Type()
)
swACLIpTcpOption.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLIpTcpOption.setStatus("current")


class _SwACLIpUdpOption_Type(Integer32):
    """Custom type swACLIpUdpOption based on Integer32"""
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
        *(("dst-addr", 2),
          ("dst-src-addr", 4),
          ("other", 1),
          ("src-addr", 3))
    )


_SwACLIpUdpOption_Type.__name__ = "Integer32"
_SwACLIpUdpOption_Object = MibTableColumn
swACLIpUdpOption = _SwACLIpUdpOption_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 5, 1, 2, 1, 11),
    _SwACLIpUdpOption_Type()
)
swACLIpUdpOption.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLIpUdpOption.setStatus("current")


class _SwACLIpTCPorUDPSrcPortMask_Type(OctetString):
    """Custom type swACLIpTCPorUDPSrcPortMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_SwACLIpTCPorUDPSrcPortMask_Type.__name__ = "OctetString"
_SwACLIpTCPorUDPSrcPortMask_Object = MibTableColumn
swACLIpTCPorUDPSrcPortMask = _SwACLIpTCPorUDPSrcPortMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 5, 1, 2, 1, 12),
    _SwACLIpTCPorUDPSrcPortMask_Type()
)
swACLIpTCPorUDPSrcPortMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLIpTCPorUDPSrcPortMask.setStatus("current")


class _SwACLIpTCPorUDPDstPortMask_Type(OctetString):
    """Custom type swACLIpTCPorUDPDstPortMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_SwACLIpTCPorUDPDstPortMask_Type.__name__ = "OctetString"
_SwACLIpTCPorUDPDstPortMask_Object = MibTableColumn
swACLIpTCPorUDPDstPortMask = _SwACLIpTCPorUDPDstPortMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 5, 1, 2, 1, 13),
    _SwACLIpTCPorUDPDstPortMask_Type()
)
swACLIpTCPorUDPDstPortMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLIpTCPorUDPDstPortMask.setStatus("current")


class _SwACLIpTCPFlagBit_Type(Integer32):
    """Custom type swACLIpTCPFlagBit based on Integer32"""
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


_SwACLIpTCPFlagBit_Type.__name__ = "Integer32"
_SwACLIpTCPFlagBit_Object = MibTableColumn
swACLIpTCPFlagBit = _SwACLIpTCPFlagBit_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 5, 1, 2, 1, 14),
    _SwACLIpTCPFlagBit_Type()
)
swACLIpTCPFlagBit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLIpTCPFlagBit.setStatus("current")


class _SwACLIpProtoIDOption_Type(Integer32):
    """Custom type swACLIpProtoIDOption based on Integer32"""
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


_SwACLIpProtoIDOption_Type.__name__ = "Integer32"
_SwACLIpProtoIDOption_Object = MibTableColumn
swACLIpProtoIDOption = _SwACLIpProtoIDOption_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 5, 1, 2, 1, 16),
    _SwACLIpProtoIDOption_Type()
)
swACLIpProtoIDOption.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLIpProtoIDOption.setStatus("current")


class _SwACLIpProtoIDMask_Type(OctetString):
    """Custom type swACLIpProtoIDMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_SwACLIpProtoIDMask_Type.__name__ = "OctetString"
_SwACLIpProtoIDMask_Object = MibTableColumn
swACLIpProtoIDMask = _SwACLIpProtoIDMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 5, 1, 2, 1, 17),
    _SwACLIpProtoIDMask_Type()
)
swACLIpProtoIDMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLIpProtoIDMask.setStatus("current")
_SwACLIpPort_Type = PortList
_SwACLIpPort_Object = MibTableColumn
swACLIpPort = _SwACLIpPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 5, 1, 2, 1, 18),
    _SwACLIpPort_Type()
)
swACLIpPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLIpPort.setStatus("current")
_SwACLIpRowStatus_Type = RowStatus
_SwACLIpRowStatus_Object = MibTableColumn
swACLIpRowStatus = _SwACLIpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 5, 1, 2, 1, 19),
    _SwACLIpRowStatus_Type()
)
swACLIpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLIpRowStatus.setStatus("current")


class _SwACLIpTCPFlagBitMask_Type(Integer32):
    """Custom type swACLIpTCPFlagBitMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_SwACLIpTCPFlagBitMask_Type.__name__ = "Integer32"
_SwACLIpTCPFlagBitMask_Object = MibTableColumn
swACLIpTCPFlagBitMask = _SwACLIpTCPFlagBitMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 5, 1, 2, 1, 115),
    _SwACLIpTCPFlagBitMask_Type()
)
swACLIpTCPFlagBitMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLIpTCPFlagBitMask.setStatus("current")
_SwACLPayloadTable_Object = MibTable
swACLPayloadTable = _SwACLPayloadTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 5, 1, 3)
)
if mibBuilder.loadTexts:
    swACLPayloadTable.setStatus("current")
_SwACLPayloadEntry_Object = MibTableRow
swACLPayloadEntry = _SwACLPayloadEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 5, 1, 3, 1)
)
swACLPayloadEntry.setIndexNames(
    (0, "SW-ACLMGMT-MIB", "swACLPayloadProfileID"),
)
if mibBuilder.loadTexts:
    swACLPayloadEntry.setStatus("current")


class _SwACLPayloadProfileID_Type(Integer32):
    """Custom type swACLPayloadProfileID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SwACLPayloadProfileID_Type.__name__ = "Integer32"
_SwACLPayloadProfileID_Object = MibTableColumn
swACLPayloadProfileID = _SwACLPayloadProfileID_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 5, 1, 3, 1, 1),
    _SwACLPayloadProfileID_Type()
)
swACLPayloadProfileID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swACLPayloadProfileID.setStatus("current")
_SwACLPayloadPort_Type = PortList
_SwACLPayloadPort_Object = MibTableColumn
swACLPayloadPort = _SwACLPayloadPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 5, 1, 3, 1, 2),
    _SwACLPayloadPort_Type()
)
swACLPayloadPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLPayloadPort.setStatus("current")


class _SwACLPayloadOffSet0to15_Type(OctetString):
    """Custom type swACLPayloadOffSet0to15 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_SwACLPayloadOffSet0to15_Type.__name__ = "OctetString"
_SwACLPayloadOffSet0to15_Object = MibTableColumn
swACLPayloadOffSet0to15 = _SwACLPayloadOffSet0to15_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 5, 1, 3, 1, 3),
    _SwACLPayloadOffSet0to15_Type()
)
swACLPayloadOffSet0to15.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLPayloadOffSet0to15.setStatus("current")


class _SwACLPayloadOffSet16to31_Type(OctetString):
    """Custom type swACLPayloadOffSet16to31 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_SwACLPayloadOffSet16to31_Type.__name__ = "OctetString"
_SwACLPayloadOffSet16to31_Object = MibTableColumn
swACLPayloadOffSet16to31 = _SwACLPayloadOffSet16to31_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 5, 1, 3, 1, 4),
    _SwACLPayloadOffSet16to31_Type()
)
swACLPayloadOffSet16to31.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLPayloadOffSet16to31.setStatus("current")


class _SwACLPayloadOffSet32to47_Type(OctetString):
    """Custom type swACLPayloadOffSet32to47 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_SwACLPayloadOffSet32to47_Type.__name__ = "OctetString"
_SwACLPayloadOffSet32to47_Object = MibTableColumn
swACLPayloadOffSet32to47 = _SwACLPayloadOffSet32to47_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 5, 1, 3, 1, 5),
    _SwACLPayloadOffSet32to47_Type()
)
swACLPayloadOffSet32to47.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLPayloadOffSet32to47.setStatus("current")


class _SwACLPayloadOffSet48to63_Type(OctetString):
    """Custom type swACLPayloadOffSet48to63 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_SwACLPayloadOffSet48to63_Type.__name__ = "OctetString"
_SwACLPayloadOffSet48to63_Object = MibTableColumn
swACLPayloadOffSet48to63 = _SwACLPayloadOffSet48to63_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 5, 1, 3, 1, 6),
    _SwACLPayloadOffSet48to63_Type()
)
swACLPayloadOffSet48to63.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLPayloadOffSet48to63.setStatus("current")


class _SwACLPayloadOffSet64to79_Type(OctetString):
    """Custom type swACLPayloadOffSet64to79 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_SwACLPayloadOffSet64to79_Type.__name__ = "OctetString"
_SwACLPayloadOffSet64to79_Object = MibTableColumn
swACLPayloadOffSet64to79 = _SwACLPayloadOffSet64to79_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 5, 1, 3, 1, 7),
    _SwACLPayloadOffSet64to79_Type()
)
swACLPayloadOffSet64to79.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLPayloadOffSet64to79.setStatus("current")
_SwACLPayloadRowStatus_Type = RowStatus
_SwACLPayloadRowStatus_Object = MibTableColumn
swACLPayloadRowStatus = _SwACLPayloadRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 5, 1, 3, 1, 8),
    _SwACLPayloadRowStatus_Type()
)
swACLPayloadRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLPayloadRowStatus.setStatus("current")
_SwAclRuleMgmt_ObjectIdentity = ObjectIdentity
swAclRuleMgmt = _SwAclRuleMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 5, 2)
)
_SwACLEtherRuleTable_Object = MibTable
swACLEtherRuleTable = _SwACLEtherRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 5, 2, 1)
)
if mibBuilder.loadTexts:
    swACLEtherRuleTable.setStatus("current")
_SwACLEtherRuleEntry_Object = MibTableRow
swACLEtherRuleEntry = _SwACLEtherRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 5, 2, 1, 1)
)
swACLEtherRuleEntry.setIndexNames(
    (0, "SW-ACLMGMT-MIB", "swACLEtherRuleProfileID"),
    (0, "SW-ACLMGMT-MIB", "swACLEtherRuleAccessID"),
)
if mibBuilder.loadTexts:
    swACLEtherRuleEntry.setStatus("current")


class _SwACLEtherRuleProfileID_Type(Integer32):
    """Custom type swACLEtherRuleProfileID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SwACLEtherRuleProfileID_Type.__name__ = "Integer32"
_SwACLEtherRuleProfileID_Object = MibTableColumn
swACLEtherRuleProfileID = _SwACLEtherRuleProfileID_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 5, 2, 1, 1, 1),
    _SwACLEtherRuleProfileID_Type()
)
swACLEtherRuleProfileID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swACLEtherRuleProfileID.setStatus("current")


class _SwACLEtherRuleAccessID_Type(Integer32):
    """Custom type swACLEtherRuleAccessID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SwACLEtherRuleAccessID_Type.__name__ = "Integer32"
_SwACLEtherRuleAccessID_Object = MibTableColumn
swACLEtherRuleAccessID = _SwACLEtherRuleAccessID_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 5, 2, 1, 1, 2),
    _SwACLEtherRuleAccessID_Type()
)
swACLEtherRuleAccessID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swACLEtherRuleAccessID.setStatus("current")


class _SwACLEtherRuleVlan_Type(SnmpAdminString):
    """Custom type swACLEtherRuleVlan based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SwACLEtherRuleVlan_Type.__name__ = "SnmpAdminString"
_SwACLEtherRuleVlan_Object = MibTableColumn
swACLEtherRuleVlan = _SwACLEtherRuleVlan_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 5, 2, 1, 1, 3),
    _SwACLEtherRuleVlan_Type()
)
swACLEtherRuleVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLEtherRuleVlan.setStatus("current")
_SwACLEtherRuleSrcMacAddress_Type = MacAddress
_SwACLEtherRuleSrcMacAddress_Object = MibTableColumn
swACLEtherRuleSrcMacAddress = _SwACLEtherRuleSrcMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 5, 2, 1, 1, 4),
    _SwACLEtherRuleSrcMacAddress_Type()
)
swACLEtherRuleSrcMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLEtherRuleSrcMacAddress.setStatus("current")
_SwACLEtherRuleDstMacAddress_Type = MacAddress
_SwACLEtherRuleDstMacAddress_Object = MibTableColumn
swACLEtherRuleDstMacAddress = _SwACLEtherRuleDstMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 5, 2, 1, 1, 5),
    _SwACLEtherRuleDstMacAddress_Type()
)
swACLEtherRuleDstMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLEtherRuleDstMacAddress.setStatus("current")


class _SwACLEtherRule8021P_Type(Integer32):
    """Custom type swACLEtherRule8021P based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_SwACLEtherRule8021P_Type.__name__ = "Integer32"
_SwACLEtherRule8021P_Object = MibTableColumn
swACLEtherRule8021P = _SwACLEtherRule8021P_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 5, 2, 1, 1, 6),
    _SwACLEtherRule8021P_Type()
)
swACLEtherRule8021P.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLEtherRule8021P.setStatus("current")


class _SwACLEtherRuleEtherType_Type(OctetString):
    """Custom type swACLEtherRuleEtherType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_SwACLEtherRuleEtherType_Type.__name__ = "OctetString"
_SwACLEtherRuleEtherType_Object = MibTableColumn
swACLEtherRuleEtherType = _SwACLEtherRuleEtherType_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 5, 2, 1, 1, 7),
    _SwACLEtherRuleEtherType_Type()
)
swACLEtherRuleEtherType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLEtherRuleEtherType.setStatus("current")


class _SwACLEtherRuleEnablePriority_Type(Integer32):
    """Custom type swACLEtherRuleEnablePriority based on Integer32"""
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


_SwACLEtherRuleEnablePriority_Type.__name__ = "Integer32"
_SwACLEtherRuleEnablePriority_Object = MibTableColumn
swACLEtherRuleEnablePriority = _SwACLEtherRuleEnablePriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 5, 2, 1, 1, 8),
    _SwACLEtherRuleEnablePriority_Type()
)
swACLEtherRuleEnablePriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLEtherRuleEnablePriority.setStatus("current")


class _SwACLEtherRulePriority_Type(Integer32):
    """Custom type swACLEtherRulePriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_SwACLEtherRulePriority_Type.__name__ = "Integer32"
_SwACLEtherRulePriority_Object = MibTableColumn
swACLEtherRulePriority = _SwACLEtherRulePriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 5, 2, 1, 1, 9),
    _SwACLEtherRulePriority_Type()
)
swACLEtherRulePriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLEtherRulePriority.setStatus("current")


class _SwACLEtherRuleReplacePriority_Type(Integer32):
    """Custom type swACLEtherRuleReplacePriority based on Integer32"""
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


_SwACLEtherRuleReplacePriority_Type.__name__ = "Integer32"
_SwACLEtherRuleReplacePriority_Object = MibTableColumn
swACLEtherRuleReplacePriority = _SwACLEtherRuleReplacePriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 5, 2, 1, 1, 10),
    _SwACLEtherRuleReplacePriority_Type()
)
swACLEtherRuleReplacePriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLEtherRuleReplacePriority.setStatus("current")


class _SwACLEtherRuleEnableReplaceDscp_Type(Integer32):
    """Custom type swACLEtherRuleEnableReplaceDscp based on Integer32"""
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


_SwACLEtherRuleEnableReplaceDscp_Type.__name__ = "Integer32"
_SwACLEtherRuleEnableReplaceDscp_Object = MibTableColumn
swACLEtherRuleEnableReplaceDscp = _SwACLEtherRuleEnableReplaceDscp_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 5, 2, 1, 1, 11),
    _SwACLEtherRuleEnableReplaceDscp_Type()
)
swACLEtherRuleEnableReplaceDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLEtherRuleEnableReplaceDscp.setStatus("current")


class _SwACLEtherRuleRepDscp_Type(Integer32):
    """Custom type swACLEtherRuleRepDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_SwACLEtherRuleRepDscp_Type.__name__ = "Integer32"
_SwACLEtherRuleRepDscp_Object = MibTableColumn
swACLEtherRuleRepDscp = _SwACLEtherRuleRepDscp_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 5, 2, 1, 1, 12),
    _SwACLEtherRuleRepDscp_Type()
)
swACLEtherRuleRepDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLEtherRuleRepDscp.setStatus("current")


class _SwACLEtherRulePermit_Type(Integer32):
    """Custom type swACLEtherRulePermit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 1),
          ("permit", 2))
    )


_SwACLEtherRulePermit_Type.__name__ = "Integer32"
_SwACLEtherRulePermit_Object = MibTableColumn
swACLEtherRulePermit = _SwACLEtherRulePermit_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 5, 2, 1, 1, 14),
    _SwACLEtherRulePermit_Type()
)
swACLEtherRulePermit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLEtherRulePermit.setStatus("current")
_SwACLEtherRuleRowStatus_Type = RowStatus
_SwACLEtherRuleRowStatus_Object = MibTableColumn
swACLEtherRuleRowStatus = _SwACLEtherRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 5, 2, 1, 1, 15),
    _SwACLEtherRuleRowStatus_Type()
)
swACLEtherRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLEtherRuleRowStatus.setStatus("current")
_SwACLIpRuleTable_Object = MibTable
swACLIpRuleTable = _SwACLIpRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 5, 2, 2)
)
if mibBuilder.loadTexts:
    swACLIpRuleTable.setStatus("current")
_SwACLIpRuleEntry_Object = MibTableRow
swACLIpRuleEntry = _SwACLIpRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 5, 2, 2, 1)
)
swACLIpRuleEntry.setIndexNames(
    (0, "SW-ACLMGMT-MIB", "swACLIpRuleProfileID"),
    (0, "SW-ACLMGMT-MIB", "swACLIpRuleAccessID"),
)
if mibBuilder.loadTexts:
    swACLIpRuleEntry.setStatus("current")


class _SwACLIpRuleProfileID_Type(Integer32):
    """Custom type swACLIpRuleProfileID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SwACLIpRuleProfileID_Type.__name__ = "Integer32"
_SwACLIpRuleProfileID_Object = MibTableColumn
swACLIpRuleProfileID = _SwACLIpRuleProfileID_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 5, 2, 2, 1, 1),
    _SwACLIpRuleProfileID_Type()
)
swACLIpRuleProfileID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swACLIpRuleProfileID.setStatus("current")


class _SwACLIpRuleAccessID_Type(Integer32):
    """Custom type swACLIpRuleAccessID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SwACLIpRuleAccessID_Type.__name__ = "Integer32"
_SwACLIpRuleAccessID_Object = MibTableColumn
swACLIpRuleAccessID = _SwACLIpRuleAccessID_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 5, 2, 2, 1, 2),
    _SwACLIpRuleAccessID_Type()
)
swACLIpRuleAccessID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swACLIpRuleAccessID.setStatus("current")


class _SwACLIpRuleVlan_Type(SnmpAdminString):
    """Custom type swACLIpRuleVlan based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SwACLIpRuleVlan_Type.__name__ = "SnmpAdminString"
_SwACLIpRuleVlan_Object = MibTableColumn
swACLIpRuleVlan = _SwACLIpRuleVlan_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 5, 2, 2, 1, 3),
    _SwACLIpRuleVlan_Type()
)
swACLIpRuleVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLIpRuleVlan.setStatus("current")
_SwACLIpRuleSrcIpaddress_Type = IpAddress
_SwACLIpRuleSrcIpaddress_Object = MibTableColumn
swACLIpRuleSrcIpaddress = _SwACLIpRuleSrcIpaddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 5, 2, 2, 1, 4),
    _SwACLIpRuleSrcIpaddress_Type()
)
swACLIpRuleSrcIpaddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLIpRuleSrcIpaddress.setStatus("current")
_SwACLIpRuleDstIpaddress_Type = IpAddress
_SwACLIpRuleDstIpaddress_Object = MibTableColumn
swACLIpRuleDstIpaddress = _SwACLIpRuleDstIpaddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 5, 2, 2, 1, 5),
    _SwACLIpRuleDstIpaddress_Type()
)
swACLIpRuleDstIpaddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLIpRuleDstIpaddress.setStatus("current")


class _SwACLIpRuleDscp_Type(Integer32):
    """Custom type swACLIpRuleDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_SwACLIpRuleDscp_Type.__name__ = "Integer32"
_SwACLIpRuleDscp_Object = MibTableColumn
swACLIpRuleDscp = _SwACLIpRuleDscp_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 5, 2, 2, 1, 6),
    _SwACLIpRuleDscp_Type()
)
swACLIpRuleDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLIpRuleDscp.setStatus("current")


class _SwACLIpRuleProtocol_Type(Integer32):
    """Custom type swACLIpRuleProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("icmp", 2),
          ("igmp", 3),
          ("none", 1),
          ("protocolId", 6),
          ("tcp", 4),
          ("udp", 5))
    )


_SwACLIpRuleProtocol_Type.__name__ = "Integer32"
_SwACLIpRuleProtocol_Object = MibTableColumn
swACLIpRuleProtocol = _SwACLIpRuleProtocol_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 5, 2, 2, 1, 7),
    _SwACLIpRuleProtocol_Type()
)
swACLIpRuleProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swACLIpRuleProtocol.setStatus("current")


class _SwACLIpRuleType_Type(Integer32):
    """Custom type swACLIpRuleType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SwACLIpRuleType_Type.__name__ = "Integer32"
_SwACLIpRuleType_Object = MibTableColumn
swACLIpRuleType = _SwACLIpRuleType_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 5, 2, 2, 1, 8),
    _SwACLIpRuleType_Type()
)
swACLIpRuleType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLIpRuleType.setStatus("current")


class _SwACLIpRuleCode_Type(Integer32):
    """Custom type swACLIpRuleCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SwACLIpRuleCode_Type.__name__ = "Integer32"
_SwACLIpRuleCode_Object = MibTableColumn
swACLIpRuleCode = _SwACLIpRuleCode_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 5, 2, 2, 1, 9),
    _SwACLIpRuleCode_Type()
)
swACLIpRuleCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLIpRuleCode.setStatus("current")


class _SwACLIpRuleSrcPort_Type(Integer32):
    """Custom type swACLIpRuleSrcPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwACLIpRuleSrcPort_Type.__name__ = "Integer32"
_SwACLIpRuleSrcPort_Object = MibTableColumn
swACLIpRuleSrcPort = _SwACLIpRuleSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 5, 2, 2, 1, 10),
    _SwACLIpRuleSrcPort_Type()
)
swACLIpRuleSrcPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLIpRuleSrcPort.setStatus("current")


class _SwACLIpRuleDstPort_Type(Integer32):
    """Custom type swACLIpRuleDstPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwACLIpRuleDstPort_Type.__name__ = "Integer32"
_SwACLIpRuleDstPort_Object = MibTableColumn
swACLIpRuleDstPort = _SwACLIpRuleDstPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 5, 2, 2, 1, 11),
    _SwACLIpRuleDstPort_Type()
)
swACLIpRuleDstPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLIpRuleDstPort.setStatus("current")


class _SwACLIpRuleFlagBits_Type(Integer32):
    """Custom type swACLIpRuleFlagBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_SwACLIpRuleFlagBits_Type.__name__ = "Integer32"
_SwACLIpRuleFlagBits_Object = MibTableColumn
swACLIpRuleFlagBits = _SwACLIpRuleFlagBits_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 5, 2, 2, 1, 12),
    _SwACLIpRuleFlagBits_Type()
)
swACLIpRuleFlagBits.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLIpRuleFlagBits.setStatus("current")


class _SwACLIpRuleProtoID_Type(Integer32):
    """Custom type swACLIpRuleProtoID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SwACLIpRuleProtoID_Type.__name__ = "Integer32"
_SwACLIpRuleProtoID_Object = MibTableColumn
swACLIpRuleProtoID = _SwACLIpRuleProtoID_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 5, 2, 2, 1, 13),
    _SwACLIpRuleProtoID_Type()
)
swACLIpRuleProtoID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLIpRuleProtoID.setStatus("current")


class _SwACLIpRuleUserMask_Type(OctetString):
    """Custom type swACLIpRuleUserMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_SwACLIpRuleUserMask_Type.__name__ = "OctetString"
_SwACLIpRuleUserMask_Object = MibTableColumn
swACLIpRuleUserMask = _SwACLIpRuleUserMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 5, 2, 2, 1, 14),
    _SwACLIpRuleUserMask_Type()
)
swACLIpRuleUserMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLIpRuleUserMask.setStatus("current")


class _SwACLIpRuleEnablePriority_Type(Integer32):
    """Custom type swACLIpRuleEnablePriority based on Integer32"""
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


_SwACLIpRuleEnablePriority_Type.__name__ = "Integer32"
_SwACLIpRuleEnablePriority_Object = MibTableColumn
swACLIpRuleEnablePriority = _SwACLIpRuleEnablePriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 5, 2, 2, 1, 15),
    _SwACLIpRuleEnablePriority_Type()
)
swACLIpRuleEnablePriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLIpRuleEnablePriority.setStatus("current")


class _SwACLIpRulePriority_Type(Integer32):
    """Custom type swACLIpRulePriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_SwACLIpRulePriority_Type.__name__ = "Integer32"
_SwACLIpRulePriority_Object = MibTableColumn
swACLIpRulePriority = _SwACLIpRulePriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 5, 2, 2, 1, 16),
    _SwACLIpRulePriority_Type()
)
swACLIpRulePriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLIpRulePriority.setStatus("current")


class _SwACLIpRuleReplacePriority_Type(Integer32):
    """Custom type swACLIpRuleReplacePriority based on Integer32"""
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


_SwACLIpRuleReplacePriority_Type.__name__ = "Integer32"
_SwACLIpRuleReplacePriority_Object = MibTableColumn
swACLIpRuleReplacePriority = _SwACLIpRuleReplacePriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 5, 2, 2, 1, 17),
    _SwACLIpRuleReplacePriority_Type()
)
swACLIpRuleReplacePriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLIpRuleReplacePriority.setStatus("current")


class _SwACLIpRuleEnableReplaceDscp_Type(Integer32):
    """Custom type swACLIpRuleEnableReplaceDscp based on Integer32"""
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


_SwACLIpRuleEnableReplaceDscp_Type.__name__ = "Integer32"
_SwACLIpRuleEnableReplaceDscp_Object = MibTableColumn
swACLIpRuleEnableReplaceDscp = _SwACLIpRuleEnableReplaceDscp_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 5, 2, 2, 1, 18),
    _SwACLIpRuleEnableReplaceDscp_Type()
)
swACLIpRuleEnableReplaceDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLIpRuleEnableReplaceDscp.setStatus("current")


class _SwACLIpRuleRepDscp_Type(Integer32):
    """Custom type swACLIpRuleRepDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_SwACLIpRuleRepDscp_Type.__name__ = "Integer32"
_SwACLIpRuleRepDscp_Object = MibTableColumn
swACLIpRuleRepDscp = _SwACLIpRuleRepDscp_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 5, 2, 2, 1, 19),
    _SwACLIpRuleRepDscp_Type()
)
swACLIpRuleRepDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLIpRuleRepDscp.setStatus("current")


class _SwACLIpRulePermit_Type(Integer32):
    """Custom type swACLIpRulePermit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 1),
          ("permit", 2))
    )


_SwACLIpRulePermit_Type.__name__ = "Integer32"
_SwACLIpRulePermit_Object = MibTableColumn
swACLIpRulePermit = _SwACLIpRulePermit_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 5, 2, 2, 1, 21),
    _SwACLIpRulePermit_Type()
)
swACLIpRulePermit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLIpRulePermit.setStatus("current")
_SwACLIpRuleRowStatus_Type = RowStatus
_SwACLIpRuleRowStatus_Object = MibTableColumn
swACLIpRuleRowStatus = _SwACLIpRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 5, 2, 2, 1, 22),
    _SwACLIpRuleRowStatus_Type()
)
swACLIpRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLIpRuleRowStatus.setStatus("current")
_SwACLPayloadRuleTable_Object = MibTable
swACLPayloadRuleTable = _SwACLPayloadRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 5, 2, 3)
)
if mibBuilder.loadTexts:
    swACLPayloadRuleTable.setStatus("current")
_SwACLPayloadRuleEntry_Object = MibTableRow
swACLPayloadRuleEntry = _SwACLPayloadRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 5, 2, 3, 1)
)
swACLPayloadRuleEntry.setIndexNames(
    (0, "SW-ACLMGMT-MIB", "swACLPayloadRuleProfileID"),
    (0, "SW-ACLMGMT-MIB", "swACLPayloadRuleAccessID"),
)
if mibBuilder.loadTexts:
    swACLPayloadRuleEntry.setStatus("current")


class _SwACLPayloadRuleProfileID_Type(Integer32):
    """Custom type swACLPayloadRuleProfileID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SwACLPayloadRuleProfileID_Type.__name__ = "Integer32"
_SwACLPayloadRuleProfileID_Object = MibTableColumn
swACLPayloadRuleProfileID = _SwACLPayloadRuleProfileID_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 5, 2, 3, 1, 1),
    _SwACLPayloadRuleProfileID_Type()
)
swACLPayloadRuleProfileID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swACLPayloadRuleProfileID.setStatus("current")


class _SwACLPayloadRuleAccessID_Type(Integer32):
    """Custom type swACLPayloadRuleAccessID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SwACLPayloadRuleAccessID_Type.__name__ = "Integer32"
_SwACLPayloadRuleAccessID_Object = MibTableColumn
swACLPayloadRuleAccessID = _SwACLPayloadRuleAccessID_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 5, 2, 3, 1, 2),
    _SwACLPayloadRuleAccessID_Type()
)
swACLPayloadRuleAccessID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swACLPayloadRuleAccessID.setStatus("current")


class _SwACLPayloadRuleOffSet0to15_Type(OctetString):
    """Custom type swACLPayloadRuleOffSet0to15 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_SwACLPayloadRuleOffSet0to15_Type.__name__ = "OctetString"
_SwACLPayloadRuleOffSet0to15_Object = MibTableColumn
swACLPayloadRuleOffSet0to15 = _SwACLPayloadRuleOffSet0to15_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 5, 2, 3, 1, 4),
    _SwACLPayloadRuleOffSet0to15_Type()
)
swACLPayloadRuleOffSet0to15.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLPayloadRuleOffSet0to15.setStatus("current")


class _SwACLPayloadRuleOffSet16to31_Type(OctetString):
    """Custom type swACLPayloadRuleOffSet16to31 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_SwACLPayloadRuleOffSet16to31_Type.__name__ = "OctetString"
_SwACLPayloadRuleOffSet16to31_Object = MibTableColumn
swACLPayloadRuleOffSet16to31 = _SwACLPayloadRuleOffSet16to31_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 5, 2, 3, 1, 5),
    _SwACLPayloadRuleOffSet16to31_Type()
)
swACLPayloadRuleOffSet16to31.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLPayloadRuleOffSet16to31.setStatus("current")


class _SwACLPayloadRuleOffSet32to47_Type(OctetString):
    """Custom type swACLPayloadRuleOffSet32to47 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_SwACLPayloadRuleOffSet32to47_Type.__name__ = "OctetString"
_SwACLPayloadRuleOffSet32to47_Object = MibTableColumn
swACLPayloadRuleOffSet32to47 = _SwACLPayloadRuleOffSet32to47_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 5, 2, 3, 1, 6),
    _SwACLPayloadRuleOffSet32to47_Type()
)
swACLPayloadRuleOffSet32to47.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLPayloadRuleOffSet32to47.setStatus("current")


class _SwACLPayloadRuleOffSet48to63_Type(OctetString):
    """Custom type swACLPayloadRuleOffSet48to63 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_SwACLPayloadRuleOffSet48to63_Type.__name__ = "OctetString"
_SwACLPayloadRuleOffSet48to63_Object = MibTableColumn
swACLPayloadRuleOffSet48to63 = _SwACLPayloadRuleOffSet48to63_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 5, 2, 3, 1, 7),
    _SwACLPayloadRuleOffSet48to63_Type()
)
swACLPayloadRuleOffSet48to63.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLPayloadRuleOffSet48to63.setStatus("current")


class _SwACLPayloadRuleOffSet64to79_Type(OctetString):
    """Custom type swACLPayloadRuleOffSet64to79 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_SwACLPayloadRuleOffSet64to79_Type.__name__ = "OctetString"
_SwACLPayloadRuleOffSet64to79_Object = MibTableColumn
swACLPayloadRuleOffSet64to79 = _SwACLPayloadRuleOffSet64to79_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 5, 2, 3, 1, 8),
    _SwACLPayloadRuleOffSet64to79_Type()
)
swACLPayloadRuleOffSet64to79.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLPayloadRuleOffSet64to79.setStatus("current")


class _SwACLPayloadRuleEnablePriority_Type(Integer32):
    """Custom type swACLPayloadRuleEnablePriority based on Integer32"""
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


_SwACLPayloadRuleEnablePriority_Type.__name__ = "Integer32"
_SwACLPayloadRuleEnablePriority_Object = MibTableColumn
swACLPayloadRuleEnablePriority = _SwACLPayloadRuleEnablePriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 5, 2, 3, 1, 9),
    _SwACLPayloadRuleEnablePriority_Type()
)
swACLPayloadRuleEnablePriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLPayloadRuleEnablePriority.setStatus("current")


class _SwACLPayloadRulePriority_Type(Integer32):
    """Custom type swACLPayloadRulePriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_SwACLPayloadRulePriority_Type.__name__ = "Integer32"
_SwACLPayloadRulePriority_Object = MibTableColumn
swACLPayloadRulePriority = _SwACLPayloadRulePriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 5, 2, 3, 1, 10),
    _SwACLPayloadRulePriority_Type()
)
swACLPayloadRulePriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLPayloadRulePriority.setStatus("current")


class _SwACLPayloadRuleReplacePriority_Type(Integer32):
    """Custom type swACLPayloadRuleReplacePriority based on Integer32"""
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


_SwACLPayloadRuleReplacePriority_Type.__name__ = "Integer32"
_SwACLPayloadRuleReplacePriority_Object = MibTableColumn
swACLPayloadRuleReplacePriority = _SwACLPayloadRuleReplacePriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 5, 2, 3, 1, 11),
    _SwACLPayloadRuleReplacePriority_Type()
)
swACLPayloadRuleReplacePriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLPayloadRuleReplacePriority.setStatus("current")


class _SwACLPayloadRuleEnableReplaceDscp_Type(Integer32):
    """Custom type swACLPayloadRuleEnableReplaceDscp based on Integer32"""
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


_SwACLPayloadRuleEnableReplaceDscp_Type.__name__ = "Integer32"
_SwACLPayloadRuleEnableReplaceDscp_Object = MibTableColumn
swACLPayloadRuleEnableReplaceDscp = _SwACLPayloadRuleEnableReplaceDscp_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 5, 2, 3, 1, 12),
    _SwACLPayloadRuleEnableReplaceDscp_Type()
)
swACLPayloadRuleEnableReplaceDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLPayloadRuleEnableReplaceDscp.setStatus("current")


class _SwACLPayloadRuleRepDscp_Type(Integer32):
    """Custom type swACLPayloadRuleRepDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_SwACLPayloadRuleRepDscp_Type.__name__ = "Integer32"
_SwACLPayloadRuleRepDscp_Object = MibTableColumn
swACLPayloadRuleRepDscp = _SwACLPayloadRuleRepDscp_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 5, 2, 3, 1, 13),
    _SwACLPayloadRuleRepDscp_Type()
)
swACLPayloadRuleRepDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLPayloadRuleRepDscp.setStatus("current")


class _SwACLPayloadRulePermit_Type(Integer32):
    """Custom type swACLPayloadRulePermit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 1),
          ("permit", 2))
    )


_SwACLPayloadRulePermit_Type.__name__ = "Integer32"
_SwACLPayloadRulePermit_Object = MibTableColumn
swACLPayloadRulePermit = _SwACLPayloadRulePermit_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 5, 2, 3, 1, 14),
    _SwACLPayloadRulePermit_Type()
)
swACLPayloadRulePermit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLPayloadRulePermit.setStatus("current")
_SwACLPayloadRuleRowStatus_Type = RowStatus
_SwACLPayloadRuleRowStatus_Object = MibTableColumn
swACLPayloadRuleRowStatus = _SwACLPayloadRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 5, 2, 3, 1, 15),
    _SwACLPayloadRuleRowStatus_Type()
)
swACLPayloadRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLPayloadRuleRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SW-ACLMGMT-MIB",
    **{"swAclMgmtMIB": swAclMgmtMIB,
       "swAclMaskMgmt": swAclMaskMgmt,
       "swACLEthernetTable": swACLEthernetTable,
       "swACLEthernetEntry": swACLEthernetEntry,
       "swACLEthernetProfileID": swACLEthernetProfileID,
       "swACLEthernetUsevlan": swACLEthernetUsevlan,
       "swACLEthernetMacAddrMaskState": swACLEthernetMacAddrMaskState,
       "swACLEthernetSrcMacAddrMask": swACLEthernetSrcMacAddrMask,
       "swACLEthernetDstMacAddrMask": swACLEthernetDstMacAddrMask,
       "swACLEthernetUse8021p": swACLEthernetUse8021p,
       "swACLEthernetUseEthernetType": swACLEthernetUseEthernetType,
       "swACLEthernetPort": swACLEthernetPort,
       "swACLEthernetRowStatus": swACLEthernetRowStatus,
       "swACLIpTable": swACLIpTable,
       "swACLIpEntry": swACLIpEntry,
       "swACLIpProfileID": swACLIpProfileID,
       "swACLIpUsevlan": swACLIpUsevlan,
       "swACLIpIpAddrMaskState": swACLIpIpAddrMaskState,
       "swACLIpSrcIpAddrMask": swACLIpSrcIpAddrMask,
       "swACLIpDstIpAddrMask": swACLIpDstIpAddrMask,
       "swACLIpUseDSCP": swACLIpUseDSCP,
       "swACLIpUseProtoType": swACLIpUseProtoType,
       "swACLIpIcmpOption": swACLIpIcmpOption,
       "swACLIpIgmpOption": swACLIpIgmpOption,
       "swACLIpTcpOption": swACLIpTcpOption,
       "swACLIpUdpOption": swACLIpUdpOption,
       "swACLIpTCPorUDPSrcPortMask": swACLIpTCPorUDPSrcPortMask,
       "swACLIpTCPorUDPDstPortMask": swACLIpTCPorUDPDstPortMask,
       "swACLIpTCPFlagBit": swACLIpTCPFlagBit,
       "swACLIpProtoIDOption": swACLIpProtoIDOption,
       "swACLIpProtoIDMask": swACLIpProtoIDMask,
       "swACLIpPort": swACLIpPort,
       "swACLIpRowStatus": swACLIpRowStatus,
       "swACLIpTCPFlagBitMask": swACLIpTCPFlagBitMask,
       "swACLPayloadTable": swACLPayloadTable,
       "swACLPayloadEntry": swACLPayloadEntry,
       "swACLPayloadProfileID": swACLPayloadProfileID,
       "swACLPayloadPort": swACLPayloadPort,
       "swACLPayloadOffSet0to15": swACLPayloadOffSet0to15,
       "swACLPayloadOffSet16to31": swACLPayloadOffSet16to31,
       "swACLPayloadOffSet32to47": swACLPayloadOffSet32to47,
       "swACLPayloadOffSet48to63": swACLPayloadOffSet48to63,
       "swACLPayloadOffSet64to79": swACLPayloadOffSet64to79,
       "swACLPayloadRowStatus": swACLPayloadRowStatus,
       "swAclRuleMgmt": swAclRuleMgmt,
       "swACLEtherRuleTable": swACLEtherRuleTable,
       "swACLEtherRuleEntry": swACLEtherRuleEntry,
       "swACLEtherRuleProfileID": swACLEtherRuleProfileID,
       "swACLEtherRuleAccessID": swACLEtherRuleAccessID,
       "swACLEtherRuleVlan": swACLEtherRuleVlan,
       "swACLEtherRuleSrcMacAddress": swACLEtherRuleSrcMacAddress,
       "swACLEtherRuleDstMacAddress": swACLEtherRuleDstMacAddress,
       "swACLEtherRule8021P": swACLEtherRule8021P,
       "swACLEtherRuleEtherType": swACLEtherRuleEtherType,
       "swACLEtherRuleEnablePriority": swACLEtherRuleEnablePriority,
       "swACLEtherRulePriority": swACLEtherRulePriority,
       "swACLEtherRuleReplacePriority": swACLEtherRuleReplacePriority,
       "swACLEtherRuleEnableReplaceDscp": swACLEtherRuleEnableReplaceDscp,
       "swACLEtherRuleRepDscp": swACLEtherRuleRepDscp,
       "swACLEtherRulePermit": swACLEtherRulePermit,
       "swACLEtherRuleRowStatus": swACLEtherRuleRowStatus,
       "swACLIpRuleTable": swACLIpRuleTable,
       "swACLIpRuleEntry": swACLIpRuleEntry,
       "swACLIpRuleProfileID": swACLIpRuleProfileID,
       "swACLIpRuleAccessID": swACLIpRuleAccessID,
       "swACLIpRuleVlan": swACLIpRuleVlan,
       "swACLIpRuleSrcIpaddress": swACLIpRuleSrcIpaddress,
       "swACLIpRuleDstIpaddress": swACLIpRuleDstIpaddress,
       "swACLIpRuleDscp": swACLIpRuleDscp,
       "swACLIpRuleProtocol": swACLIpRuleProtocol,
       "swACLIpRuleType": swACLIpRuleType,
       "swACLIpRuleCode": swACLIpRuleCode,
       "swACLIpRuleSrcPort": swACLIpRuleSrcPort,
       "swACLIpRuleDstPort": swACLIpRuleDstPort,
       "swACLIpRuleFlagBits": swACLIpRuleFlagBits,
       "swACLIpRuleProtoID": swACLIpRuleProtoID,
       "swACLIpRuleUserMask": swACLIpRuleUserMask,
       "swACLIpRuleEnablePriority": swACLIpRuleEnablePriority,
       "swACLIpRulePriority": swACLIpRulePriority,
       "swACLIpRuleReplacePriority": swACLIpRuleReplacePriority,
       "swACLIpRuleEnableReplaceDscp": swACLIpRuleEnableReplaceDscp,
       "swACLIpRuleRepDscp": swACLIpRuleRepDscp,
       "swACLIpRulePermit": swACLIpRulePermit,
       "swACLIpRuleRowStatus": swACLIpRuleRowStatus,
       "swACLPayloadRuleTable": swACLPayloadRuleTable,
       "swACLPayloadRuleEntry": swACLPayloadRuleEntry,
       "swACLPayloadRuleProfileID": swACLPayloadRuleProfileID,
       "swACLPayloadRuleAccessID": swACLPayloadRuleAccessID,
       "swACLPayloadRuleOffSet0to15": swACLPayloadRuleOffSet0to15,
       "swACLPayloadRuleOffSet16to31": swACLPayloadRuleOffSet16to31,
       "swACLPayloadRuleOffSet32to47": swACLPayloadRuleOffSet32to47,
       "swACLPayloadRuleOffSet48to63": swACLPayloadRuleOffSet48to63,
       "swACLPayloadRuleOffSet64to79": swACLPayloadRuleOffSet64to79,
       "swACLPayloadRuleEnablePriority": swACLPayloadRuleEnablePriority,
       "swACLPayloadRulePriority": swACLPayloadRulePriority,
       "swACLPayloadRuleReplacePriority": swACLPayloadRuleReplacePriority,
       "swACLPayloadRuleEnableReplaceDscp": swACLPayloadRuleEnableReplaceDscp,
       "swACLPayloadRuleRepDscp": swACLPayloadRuleRepDscp,
       "swACLPayloadRulePermit": swACLPayloadRulePermit,
       "swACLPayloadRuleRowStatus": swACLPayloadRuleRowStatus}
)
