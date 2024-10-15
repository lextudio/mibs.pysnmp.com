# SNMP MIB module (ACLMGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ACLMGMT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:33:31 2024
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

(dlink_common_mgmt,) = mibBuilder.importSymbols(
    "DLINK-ID-REC-MIB",
    "dlink-common-mgmt")

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
    (1, 3, 6, 1, 4, 1, 171, 12, 9)
)


# Types definitions



class PortList(OctetString):
    """Custom type PortList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )




# TEXTUAL-CONVENTIONS



class Ipv6Address(OctetString, TextualConvention):
    status = "current"
    displayHint = "2x:"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )



# MIB Managed Objects in the order of their OIDs

_SwAclCtrl_ObjectIdentity = ObjectIdentity
swAclCtrl = _SwAclCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 1)
)


class _SwCpuInterfacefilterState_Type(Integer32):
    """Custom type swCpuInterfacefilterState based on Integer32"""
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


_SwCpuInterfacefilterState_Type.__name__ = "Integer32"
_SwCpuInterfacefilterState_Object = MibScalar
swCpuInterfacefilterState = _SwCpuInterfacefilterState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 1, 1),
    _SwCpuInterfacefilterState_Type()
)
swCpuInterfacefilterState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swCpuInterfacefilterState.setStatus("current")
_SwACLTotalUsedRuleEntries_Type = Integer32
_SwACLTotalUsedRuleEntries_Object = MibScalar
swACLTotalUsedRuleEntries = _SwACLTotalUsedRuleEntries_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 1, 2),
    _SwACLTotalUsedRuleEntries_Type()
)
swACLTotalUsedRuleEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swACLTotalUsedRuleEntries.setStatus("current")
_SwACLTotalUnusedRuleEntries_Type = Integer32
_SwACLTotalUnusedRuleEntries_Object = MibScalar
swACLTotalUnusedRuleEntries = _SwACLTotalUnusedRuleEntries_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 1, 3),
    _SwACLTotalUnusedRuleEntries_Type()
)
swACLTotalUnusedRuleEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swACLTotalUnusedRuleEntries.setStatus("current")
_SwAclMaskMgmt_ObjectIdentity = ObjectIdentity
swAclMaskMgmt = _SwAclMaskMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 2)
)
_SwACLEthernetTable_Object = MibTable
swACLEthernetTable = _SwACLEthernetTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 2, 1)
)
if mibBuilder.loadTexts:
    swACLEthernetTable.setStatus("current")
_SwACLEthernetEntry_Object = MibTableRow
swACLEthernetEntry = _SwACLEthernetEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 2, 1, 1)
)
swACLEthernetEntry.setIndexNames(
    (0, "ACLMGMT-MIB", "swACLEthernetProfileID"),
)
if mibBuilder.loadTexts:
    swACLEthernetEntry.setStatus("current")
_SwACLEthernetProfileID_Type = Integer32
_SwACLEthernetProfileID_Object = MibTableColumn
swACLEthernetProfileID = _SwACLEthernetProfileID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 2, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 2, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 2, 1, 1, 3),
    _SwACLEthernetMacAddrMaskState_Type()
)
swACLEthernetMacAddrMaskState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLEthernetMacAddrMaskState.setStatus("current")
_SwACLEthernetSrcMacAddrMask_Type = MacAddress
_SwACLEthernetSrcMacAddrMask_Object = MibTableColumn
swACLEthernetSrcMacAddrMask = _SwACLEthernetSrcMacAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 2, 1, 1, 4),
    _SwACLEthernetSrcMacAddrMask_Type()
)
swACLEthernetSrcMacAddrMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLEthernetSrcMacAddrMask.setStatus("current")
_SwACLEthernetDstMacAddrMask_Type = MacAddress
_SwACLEthernetDstMacAddrMask_Object = MibTableColumn
swACLEthernetDstMacAddrMask = _SwACLEthernetDstMacAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 2, 1, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 2, 1, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 2, 1, 1, 7),
    _SwACLEthernetUseEthernetType_Type()
)
swACLEthernetUseEthernetType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLEthernetUseEthernetType.setStatus("current")
_SwACLEthernetRowStatus_Type = RowStatus
_SwACLEthernetRowStatus_Object = MibTableColumn
swACLEthernetRowStatus = _SwACLEthernetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 2, 1, 1, 8),
    _SwACLEthernetRowStatus_Type()
)
swACLEthernetRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLEthernetRowStatus.setStatus("current")


class _SwACLEthernetOwner_Type(Integer32):
    """Custom type swACLEthernetOwner based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("acl", 2),
          ("any", 1),
          ("dhcp", 5),
          ("ext-netbios", 7),
          ("ipbind", 3),
          ("netbios", 6),
          ("other", 4))
    )


_SwACLEthernetOwner_Type.__name__ = "Integer32"
_SwACLEthernetOwner_Object = MibTableColumn
swACLEthernetOwner = _SwACLEthernetOwner_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 2, 1, 1, 9),
    _SwACLEthernetOwner_Type()
)
swACLEthernetOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swACLEthernetOwner.setStatus("current")
_SwACLEthernetUnusedRuleEntries_Type = Integer32
_SwACLEthernetUnusedRuleEntries_Object = MibTableColumn
swACLEthernetUnusedRuleEntries = _SwACLEthernetUnusedRuleEntries_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 2, 1, 1, 10),
    _SwACLEthernetUnusedRuleEntries_Type()
)
swACLEthernetUnusedRuleEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swACLEthernetUnusedRuleEntries.setStatus("current")


class _SwACLEthernetProfileName_Type(DisplayString):
    """Custom type swACLEthernetProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SwACLEthernetProfileName_Type.__name__ = "DisplayString"
_SwACLEthernetProfileName_Object = MibTableColumn
swACLEthernetProfileName = _SwACLEthernetProfileName_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 2, 1, 1, 11),
    _SwACLEthernetProfileName_Type()
)
swACLEthernetProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLEthernetProfileName.setStatus("current")
_SwACLIpTable_Object = MibTable
swACLIpTable = _SwACLIpTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 2, 2)
)
if mibBuilder.loadTexts:
    swACLIpTable.setStatus("current")
_SwACLIpEntry_Object = MibTableRow
swACLIpEntry = _SwACLIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 2, 2, 1)
)
swACLIpEntry.setIndexNames(
    (0, "ACLMGMT-MIB", "swACLIpProfileID"),
)
if mibBuilder.loadTexts:
    swACLIpEntry.setStatus("current")
_SwACLIpProfileID_Type = Integer32
_SwACLIpProfileID_Object = MibTableColumn
swACLIpProfileID = _SwACLIpProfileID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 2, 2, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 2, 2, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 2, 2, 1, 3),
    _SwACLIpIpAddrMaskState_Type()
)
swACLIpIpAddrMaskState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLIpIpAddrMaskState.setStatus("current")
_SwACLIpSrcIpAddrMask_Type = IpAddress
_SwACLIpSrcIpAddrMask_Object = MibTableColumn
swACLIpSrcIpAddrMask = _SwACLIpSrcIpAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 2, 2, 1, 4),
    _SwACLIpSrcIpAddrMask_Type()
)
swACLIpSrcIpAddrMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLIpSrcIpAddrMask.setStatus("current")
_SwACLIpDstIpAddrMask_Type = IpAddress
_SwACLIpDstIpAddrMask_Object = MibTableColumn
swACLIpDstIpAddrMask = _SwACLIpDstIpAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 2, 2, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 2, 2, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 2, 2, 1, 7),
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
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 2, 2, 1, 8),
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
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 2, 2, 1, 9),
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
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 2, 2, 1, 10),
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
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 2, 2, 1, 11),
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
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 2, 2, 1, 12),
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
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 2, 2, 1, 13),
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
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 2, 2, 1, 14),
    _SwACLIpTCPFlagBit_Type()
)
swACLIpTCPFlagBit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLIpTCPFlagBit.setStatus("current")


class _SwACLIpTCPFlagBitMask_Type(Integer32):
    """Custom type swACLIpTCPFlagBitMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_SwACLIpTCPFlagBitMask_Type.__name__ = "Integer32"
_SwACLIpTCPFlagBitMask_Object = MibTableColumn
swACLIpTCPFlagBitMask = _SwACLIpTCPFlagBitMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 2, 2, 1, 15),
    _SwACLIpTCPFlagBitMask_Type()
)
swACLIpTCPFlagBitMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLIpTCPFlagBitMask.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 2, 2, 1, 16),
    _SwACLIpProtoIDOption_Type()
)
swACLIpProtoIDOption.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLIpProtoIDOption.setStatus("current")


class _SwACLIpProtoID_Type(Integer32):
    """Custom type swACLIpProtoID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SwACLIpProtoID_Type.__name__ = "Integer32"
_SwACLIpProtoID_Object = MibTableColumn
swACLIpProtoID = _SwACLIpProtoID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 2, 2, 1, 17),
    _SwACLIpProtoID_Type()
)
swACLIpProtoID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLIpProtoID.setStatus("current")


class _SwACLIpProtoIDMask_Type(OctetString):
    """Custom type swACLIpProtoIDMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_SwACLIpProtoIDMask_Type.__name__ = "OctetString"
_SwACLIpProtoIDMask_Object = MibTableColumn
swACLIpProtoIDMask = _SwACLIpProtoIDMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 2, 2, 1, 18),
    _SwACLIpProtoIDMask_Type()
)
swACLIpProtoIDMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLIpProtoIDMask.setStatus("current")
_SwACLIpRowStatus_Type = RowStatus
_SwACLIpRowStatus_Object = MibTableColumn
swACLIpRowStatus = _SwACLIpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 2, 2, 1, 19),
    _SwACLIpRowStatus_Type()
)
swACLIpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLIpRowStatus.setStatus("current")


class _SwACLIpOwner_Type(Integer32):
    """Custom type swACLIpOwner based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("acl", 2),
          ("any", 1),
          ("dhcp", 5),
          ("ext-netbios", 7),
          ("ipbind", 3),
          ("netbios", 6),
          ("other", 4))
    )


_SwACLIpOwner_Type.__name__ = "Integer32"
_SwACLIpOwner_Object = MibTableColumn
swACLIpOwner = _SwACLIpOwner_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 2, 2, 1, 20),
    _SwACLIpOwner_Type()
)
swACLIpOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swACLIpOwner.setStatus("current")
_SwACLIpUnusedRuleEntries_Type = Integer32
_SwACLIpUnusedRuleEntries_Object = MibTableColumn
swACLIpUnusedRuleEntries = _SwACLIpUnusedRuleEntries_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 2, 2, 1, 22),
    _SwACLIpUnusedRuleEntries_Type()
)
swACLIpUnusedRuleEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swACLIpUnusedRuleEntries.setStatus("current")


class _SwACLIpProfileName_Type(DisplayString):
    """Custom type swACLIpProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SwACLIpProfileName_Type.__name__ = "DisplayString"
_SwACLIpProfileName_Object = MibTableColumn
swACLIpProfileName = _SwACLIpProfileName_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 2, 2, 1, 23),
    _SwACLIpProfileName_Type()
)
swACLIpProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLIpProfileName.setStatus("current")
_SwACLPktContMaskTable_Object = MibTable
swACLPktContMaskTable = _SwACLPktContMaskTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 2, 3)
)
if mibBuilder.loadTexts:
    swACLPktContMaskTable.setStatus("current")
_SwACLPktContMaskEntry_Object = MibTableRow
swACLPktContMaskEntry = _SwACLPktContMaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 2, 3, 1)
)
swACLPktContMaskEntry.setIndexNames(
    (0, "ACLMGMT-MIB", "swACLPktContMaskProfileID"),
)
if mibBuilder.loadTexts:
    swACLPktContMaskEntry.setStatus("current")
_SwACLPktContMaskProfileID_Type = Integer32
_SwACLPktContMaskProfileID_Object = MibTableColumn
swACLPktContMaskProfileID = _SwACLPktContMaskProfileID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 2, 3, 1, 1),
    _SwACLPktContMaskProfileID_Type()
)
swACLPktContMaskProfileID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swACLPktContMaskProfileID.setStatus("current")


class _SwACLPktContMaskOffset0to15_Type(OctetString):
    """Custom type swACLPktContMaskOffset0to15 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_SwACLPktContMaskOffset0to15_Type.__name__ = "OctetString"
_SwACLPktContMaskOffset0to15_Object = MibTableColumn
swACLPktContMaskOffset0to15 = _SwACLPktContMaskOffset0to15_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 2, 3, 1, 2),
    _SwACLPktContMaskOffset0to15_Type()
)
swACLPktContMaskOffset0to15.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLPktContMaskOffset0to15.setStatus("current")


class _SwACLPktContMaskOffset16to31_Type(OctetString):
    """Custom type swACLPktContMaskOffset16to31 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_SwACLPktContMaskOffset16to31_Type.__name__ = "OctetString"
_SwACLPktContMaskOffset16to31_Object = MibTableColumn
swACLPktContMaskOffset16to31 = _SwACLPktContMaskOffset16to31_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 2, 3, 1, 3),
    _SwACLPktContMaskOffset16to31_Type()
)
swACLPktContMaskOffset16to31.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLPktContMaskOffset16to31.setStatus("current")


class _SwACLPktContMaskOffset32to47_Type(OctetString):
    """Custom type swACLPktContMaskOffset32to47 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_SwACLPktContMaskOffset32to47_Type.__name__ = "OctetString"
_SwACLPktContMaskOffset32to47_Object = MibTableColumn
swACLPktContMaskOffset32to47 = _SwACLPktContMaskOffset32to47_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 2, 3, 1, 4),
    _SwACLPktContMaskOffset32to47_Type()
)
swACLPktContMaskOffset32to47.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLPktContMaskOffset32to47.setStatus("current")


class _SwACLPktContMaskOffset48to63_Type(OctetString):
    """Custom type swACLPktContMaskOffset48to63 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_SwACLPktContMaskOffset48to63_Type.__name__ = "OctetString"
_SwACLPktContMaskOffset48to63_Object = MibTableColumn
swACLPktContMaskOffset48to63 = _SwACLPktContMaskOffset48to63_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 2, 3, 1, 5),
    _SwACLPktContMaskOffset48to63_Type()
)
swACLPktContMaskOffset48to63.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLPktContMaskOffset48to63.setStatus("current")


class _SwACLPktContMaskOffset64to79_Type(OctetString):
    """Custom type swACLPktContMaskOffset64to79 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_SwACLPktContMaskOffset64to79_Type.__name__ = "OctetString"
_SwACLPktContMaskOffset64to79_Object = MibTableColumn
swACLPktContMaskOffset64to79 = _SwACLPktContMaskOffset64to79_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 2, 3, 1, 6),
    _SwACLPktContMaskOffset64to79_Type()
)
swACLPktContMaskOffset64to79.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLPktContMaskOffset64to79.setStatus("current")
_SwACLPktContMaskRowStatus_Type = RowStatus
_SwACLPktContMaskRowStatus_Object = MibTableColumn
swACLPktContMaskRowStatus = _SwACLPktContMaskRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 2, 3, 1, 7),
    _SwACLPktContMaskRowStatus_Type()
)
swACLPktContMaskRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLPktContMaskRowStatus.setStatus("current")


class _SwACLPktContMaskOwner_Type(Integer32):
    """Custom type swACLPktContMaskOwner based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("acl", 2),
          ("any", 1),
          ("dhcp", 5),
          ("ext-netbios", 7),
          ("ipbind", 3),
          ("netbios", 6),
          ("other", 4))
    )


_SwACLPktContMaskOwner_Type.__name__ = "Integer32"
_SwACLPktContMaskOwner_Object = MibTableColumn
swACLPktContMaskOwner = _SwACLPktContMaskOwner_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 2, 3, 1, 8),
    _SwACLPktContMaskOwner_Type()
)
swACLPktContMaskOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swACLPktContMaskOwner.setStatus("current")
_SwACLPktContMaskUnusedRuleEntries_Type = Integer32
_SwACLPktContMaskUnusedRuleEntries_Object = MibTableColumn
swACLPktContMaskUnusedRuleEntries = _SwACLPktContMaskUnusedRuleEntries_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 2, 3, 1, 9),
    _SwACLPktContMaskUnusedRuleEntries_Type()
)
swACLPktContMaskUnusedRuleEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swACLPktContMaskUnusedRuleEntries.setStatus("current")


class _SwACLPktContMaskProfileName_Type(DisplayString):
    """Custom type swACLPktContMaskProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SwACLPktContMaskProfileName_Type.__name__ = "DisplayString"
_SwACLPktContMaskProfileName_Object = MibTableColumn
swACLPktContMaskProfileName = _SwACLPktContMaskProfileName_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 2, 3, 1, 10),
    _SwACLPktContMaskProfileName_Type()
)
swACLPktContMaskProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLPktContMaskProfileName.setStatus("current")
_SwACLIpv6MaskTable_Object = MibTable
swACLIpv6MaskTable = _SwACLIpv6MaskTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 2, 4)
)
if mibBuilder.loadTexts:
    swACLIpv6MaskTable.setStatus("current")
_SwACLIpv6MaskEntry_Object = MibTableRow
swACLIpv6MaskEntry = _SwACLIpv6MaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 2, 4, 1)
)
swACLIpv6MaskEntry.setIndexNames(
    (0, "ACLMGMT-MIB", "swACLIpv6MaskProfileID"),
)
if mibBuilder.loadTexts:
    swACLIpv6MaskEntry.setStatus("current")
_SwACLIpv6MaskProfileID_Type = Integer32
_SwACLIpv6MaskProfileID_Object = MibTableColumn
swACLIpv6MaskProfileID = _SwACLIpv6MaskProfileID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 2, 4, 1, 1),
    _SwACLIpv6MaskProfileID_Type()
)
swACLIpv6MaskProfileID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swACLIpv6MaskProfileID.setStatus("current")


class _SwACLIpv6MaskClass_Type(Integer32):
    """Custom type swACLIpv6MaskClass based on Integer32"""
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


_SwACLIpv6MaskClass_Type.__name__ = "Integer32"
_SwACLIpv6MaskClass_Object = MibTableColumn
swACLIpv6MaskClass = _SwACLIpv6MaskClass_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 2, 4, 1, 2),
    _SwACLIpv6MaskClass_Type()
)
swACLIpv6MaskClass.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLIpv6MaskClass.setStatus("current")


class _SwACLIpv6MaskFlowlabel_Type(Integer32):
    """Custom type swACLIpv6MaskFlowlabel based on Integer32"""
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


_SwACLIpv6MaskFlowlabel_Type.__name__ = "Integer32"
_SwACLIpv6MaskFlowlabel_Object = MibTableColumn
swACLIpv6MaskFlowlabel = _SwACLIpv6MaskFlowlabel_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 2, 4, 1, 3),
    _SwACLIpv6MaskFlowlabel_Type()
)
swACLIpv6MaskFlowlabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLIpv6MaskFlowlabel.setStatus("current")


class _SwACLIpv6IpAddrMaskState_Type(Integer32):
    """Custom type swACLIpv6IpAddrMaskState based on Integer32"""
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
        *(("dst-ipv6-addr", 2),
          ("dst-src-ipv6-addr", 4),
          ("other", 1),
          ("src-ipv6-addr", 3))
    )


_SwACLIpv6IpAddrMaskState_Type.__name__ = "Integer32"
_SwACLIpv6IpAddrMaskState_Object = MibTableColumn
swACLIpv6IpAddrMaskState = _SwACLIpv6IpAddrMaskState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 2, 4, 1, 4),
    _SwACLIpv6IpAddrMaskState_Type()
)
swACLIpv6IpAddrMaskState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLIpv6IpAddrMaskState.setStatus("current")
_SwACLIpv6MaskSrcIpv6Mask_Type = Ipv6Address
_SwACLIpv6MaskSrcIpv6Mask_Object = MibTableColumn
swACLIpv6MaskSrcIpv6Mask = _SwACLIpv6MaskSrcIpv6Mask_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 2, 4, 1, 5),
    _SwACLIpv6MaskSrcIpv6Mask_Type()
)
swACLIpv6MaskSrcIpv6Mask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLIpv6MaskSrcIpv6Mask.setStatus("current")
_SwACLIpv6MaskDstIpv6Mask_Type = Ipv6Address
_SwACLIpv6MaskDstIpv6Mask_Object = MibTableColumn
swACLIpv6MaskDstIpv6Mask = _SwACLIpv6MaskDstIpv6Mask_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 2, 4, 1, 6),
    _SwACLIpv6MaskDstIpv6Mask_Type()
)
swACLIpv6MaskDstIpv6Mask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLIpv6MaskDstIpv6Mask.setStatus("current")
_SwACLIpv6MaskRowStatus_Type = RowStatus
_SwACLIpv6MaskRowStatus_Object = MibTableColumn
swACLIpv6MaskRowStatus = _SwACLIpv6MaskRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 2, 4, 1, 7),
    _SwACLIpv6MaskRowStatus_Type()
)
swACLIpv6MaskRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLIpv6MaskRowStatus.setStatus("current")


class _SwACLIpv6MaskOwner_Type(Integer32):
    """Custom type swACLIpv6MaskOwner based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("acl", 2),
          ("any", 1),
          ("dhcp", 5),
          ("ext-netbios", 7),
          ("ipbind", 3),
          ("netbios", 6),
          ("other", 4))
    )


_SwACLIpv6MaskOwner_Type.__name__ = "Integer32"
_SwACLIpv6MaskOwner_Object = MibTableColumn
swACLIpv6MaskOwner = _SwACLIpv6MaskOwner_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 2, 4, 1, 8),
    _SwACLIpv6MaskOwner_Type()
)
swACLIpv6MaskOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swACLIpv6MaskOwner.setStatus("current")
_SwACLIpv6MaskUnusedRuleEntries_Type = Integer32
_SwACLIpv6MaskUnusedRuleEntries_Object = MibTableColumn
swACLIpv6MaskUnusedRuleEntries = _SwACLIpv6MaskUnusedRuleEntries_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 2, 4, 1, 9),
    _SwACLIpv6MaskUnusedRuleEntries_Type()
)
swACLIpv6MaskUnusedRuleEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swACLIpv6MaskUnusedRuleEntries.setStatus("current")


class _SwACLIpv6MaskProfileName_Type(DisplayString):
    """Custom type swACLIpv6MaskProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SwACLIpv6MaskProfileName_Type.__name__ = "DisplayString"
_SwACLIpv6MaskProfileName_Object = MibTableColumn
swACLIpv6MaskProfileName = _SwACLIpv6MaskProfileName_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 2, 4, 1, 10),
    _SwACLIpv6MaskProfileName_Type()
)
swACLIpv6MaskProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLIpv6MaskProfileName.setStatus("current")


class _SwACLIpv6MaskUseProtoType_Type(Integer32):
    """Custom type swACLIpv6MaskUseProtoType based on Integer32"""
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
          ("tcp", 2),
          ("udp", 3))
    )


_SwACLIpv6MaskUseProtoType_Type.__name__ = "Integer32"
_SwACLIpv6MaskUseProtoType_Object = MibTableColumn
swACLIpv6MaskUseProtoType = _SwACLIpv6MaskUseProtoType_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 2, 4, 1, 11),
    _SwACLIpv6MaskUseProtoType_Type()
)
swACLIpv6MaskUseProtoType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLIpv6MaskUseProtoType.setStatus("current")


class _SwACLIpv6MaskTcpOption_Type(Integer32):
    """Custom type swACLIpv6MaskTcpOption based on Integer32"""
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


_SwACLIpv6MaskTcpOption_Type.__name__ = "Integer32"
_SwACLIpv6MaskTcpOption_Object = MibTableColumn
swACLIpv6MaskTcpOption = _SwACLIpv6MaskTcpOption_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 2, 4, 1, 12),
    _SwACLIpv6MaskTcpOption_Type()
)
swACLIpv6MaskTcpOption.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLIpv6MaskTcpOption.setStatus("current")


class _SwACLIpv6MaskUdpOption_Type(Integer32):
    """Custom type swACLIpv6MaskUdpOption based on Integer32"""
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


_SwACLIpv6MaskUdpOption_Type.__name__ = "Integer32"
_SwACLIpv6MaskUdpOption_Object = MibTableColumn
swACLIpv6MaskUdpOption = _SwACLIpv6MaskUdpOption_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 2, 4, 1, 13),
    _SwACLIpv6MaskUdpOption_Type()
)
swACLIpv6MaskUdpOption.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLIpv6MaskUdpOption.setStatus("current")


class _SwACLIpv6MaskTCPorUDPSrcPortMask_Type(OctetString):
    """Custom type swACLIpv6MaskTCPorUDPSrcPortMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_SwACLIpv6MaskTCPorUDPSrcPortMask_Type.__name__ = "OctetString"
_SwACLIpv6MaskTCPorUDPSrcPortMask_Object = MibTableColumn
swACLIpv6MaskTCPorUDPSrcPortMask = _SwACLIpv6MaskTCPorUDPSrcPortMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 2, 4, 1, 14),
    _SwACLIpv6MaskTCPorUDPSrcPortMask_Type()
)
swACLIpv6MaskTCPorUDPSrcPortMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLIpv6MaskTCPorUDPSrcPortMask.setStatus("current")


class _SwACLIpv6MaskTCPorUDPDstPortMask_Type(OctetString):
    """Custom type swACLIpv6MaskTCPorUDPDstPortMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_SwACLIpv6MaskTCPorUDPDstPortMask_Type.__name__ = "OctetString"
_SwACLIpv6MaskTCPorUDPDstPortMask_Object = MibTableColumn
swACLIpv6MaskTCPorUDPDstPortMask = _SwACLIpv6MaskTCPorUDPDstPortMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 2, 4, 1, 15),
    _SwACLIpv6MaskTCPorUDPDstPortMask_Type()
)
swACLIpv6MaskTCPorUDPDstPortMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLIpv6MaskTCPorUDPDstPortMask.setStatus("current")


class _SwACLMaskDelAllState_Type(Integer32):
    """Custom type swACLMaskDelAllState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("start", 2))
    )


_SwACLMaskDelAllState_Type.__name__ = "Integer32"
_SwACLMaskDelAllState_Object = MibScalar
swACLMaskDelAllState = _SwACLMaskDelAllState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 2, 5),
    _SwACLMaskDelAllState_Type()
)
swACLMaskDelAllState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swACLMaskDelAllState.setStatus("current")
_SwIBPACLEthernetTable_Object = MibTable
swIBPACLEthernetTable = _SwIBPACLEthernetTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 2, 6)
)
if mibBuilder.loadTexts:
    swIBPACLEthernetTable.setStatus("obsolete")
_SwIBPACLEthernetEntry_Object = MibTableRow
swIBPACLEthernetEntry = _SwIBPACLEthernetEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 2, 6, 1)
)
swIBPACLEthernetEntry.setIndexNames(
    (0, "ACLMGMT-MIB", "swIBPACLEthernetProfileID"),
)
if mibBuilder.loadTexts:
    swIBPACLEthernetEntry.setStatus("obsolete")
_SwIBPACLEthernetProfileID_Type = Integer32
_SwIBPACLEthernetProfileID_Object = MibTableColumn
swIBPACLEthernetProfileID = _SwIBPACLEthernetProfileID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 2, 6, 1, 1),
    _SwIBPACLEthernetProfileID_Type()
)
swIBPACLEthernetProfileID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIBPACLEthernetProfileID.setStatus("obsolete")


class _SwIBPACLEthernetUseEthernetType_Type(Integer32):
    """Custom type swIBPACLEthernetUseEthernetType based on Integer32"""
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


_SwIBPACLEthernetUseEthernetType_Type.__name__ = "Integer32"
_SwIBPACLEthernetUseEthernetType_Object = MibTableColumn
swIBPACLEthernetUseEthernetType = _SwIBPACLEthernetUseEthernetType_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 2, 6, 1, 2),
    _SwIBPACLEthernetUseEthernetType_Type()
)
swIBPACLEthernetUseEthernetType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIBPACLEthernetUseEthernetType.setStatus("obsolete")
_SwIBPACLIpTable_Object = MibTable
swIBPACLIpTable = _SwIBPACLIpTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 2, 7)
)
if mibBuilder.loadTexts:
    swIBPACLIpTable.setStatus("obsolete")
_SwIBPACLIpEntry_Object = MibTableRow
swIBPACLIpEntry = _SwIBPACLIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 2, 7, 1)
)
swIBPACLIpEntry.setIndexNames(
    (0, "ACLMGMT-MIB", "swIBPACLIpProfileID"),
)
if mibBuilder.loadTexts:
    swIBPACLIpEntry.setStatus("obsolete")
_SwIBPACLIpProfileID_Type = Integer32
_SwIBPACLIpProfileID_Object = MibTableColumn
swIBPACLIpProfileID = _SwIBPACLIpProfileID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 2, 7, 1, 1),
    _SwIBPACLIpProfileID_Type()
)
swIBPACLIpProfileID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIBPACLIpProfileID.setStatus("obsolete")
_SwIBPACLIpSrcMacAddrMask_Type = MacAddress
_SwIBPACLIpSrcMacAddrMask_Object = MibTableColumn
swIBPACLIpSrcMacAddrMask = _SwIBPACLIpSrcMacAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 2, 7, 1, 2),
    _SwIBPACLIpSrcMacAddrMask_Type()
)
swIBPACLIpSrcMacAddrMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIBPACLIpSrcMacAddrMask.setStatus("obsolete")
_SwIBPACLIpSrcIpAddrMask_Type = IpAddress
_SwIBPACLIpSrcIpAddrMask_Object = MibTableColumn
swIBPACLIpSrcIpAddrMask = _SwIBPACLIpSrcIpAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 2, 7, 1, 3),
    _SwIBPACLIpSrcIpAddrMask_Type()
)
swIBPACLIpSrcIpAddrMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIBPACLIpSrcIpAddrMask.setStatus("obsolete")
_SwACLPktContMaskOptionTable_Object = MibTable
swACLPktContMaskOptionTable = _SwACLPktContMaskOptionTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 2, 8)
)
if mibBuilder.loadTexts:
    swACLPktContMaskOptionTable.setStatus("current")
_SwACLPktContMaskOptionEntry_Object = MibTableRow
swACLPktContMaskOptionEntry = _SwACLPktContMaskOptionEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 2, 8, 1)
)
swACLPktContMaskOptionEntry.setIndexNames(
    (0, "ACLMGMT-MIB", "swACLPktContMaskOptionProfileID"),
)
if mibBuilder.loadTexts:
    swACLPktContMaskOptionEntry.setStatus("current")
_SwACLPktContMaskOptionProfileID_Type = Integer32
_SwACLPktContMaskOptionProfileID_Object = MibTableColumn
swACLPktContMaskOptionProfileID = _SwACLPktContMaskOptionProfileID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 2, 8, 1, 1),
    _SwACLPktContMaskOptionProfileID_Type()
)
swACLPktContMaskOptionProfileID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swACLPktContMaskOptionProfileID.setStatus("current")


class _SwACLPktContMaskOffsetChunk1State_Type(Integer32):
    """Custom type swACLPktContMaskOffsetChunk1State based on Integer32"""
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


_SwACLPktContMaskOffsetChunk1State_Type.__name__ = "Integer32"
_SwACLPktContMaskOffsetChunk1State_Object = MibTableColumn
swACLPktContMaskOffsetChunk1State = _SwACLPktContMaskOffsetChunk1State_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 2, 8, 1, 2),
    _SwACLPktContMaskOffsetChunk1State_Type()
)
swACLPktContMaskOffsetChunk1State.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLPktContMaskOffsetChunk1State.setStatus("current")


class _SwACLPktContMaskOffsetChunk1OffsetValue_Type(Integer32):
    """Custom type swACLPktContMaskOffsetChunk1OffsetValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_SwACLPktContMaskOffsetChunk1OffsetValue_Type.__name__ = "Integer32"
_SwACLPktContMaskOffsetChunk1OffsetValue_Object = MibTableColumn
swACLPktContMaskOffsetChunk1OffsetValue = _SwACLPktContMaskOffsetChunk1OffsetValue_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 2, 8, 1, 3),
    _SwACLPktContMaskOffsetChunk1OffsetValue_Type()
)
swACLPktContMaskOffsetChunk1OffsetValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLPktContMaskOffsetChunk1OffsetValue.setStatus("current")


class _SwACLPktContMaskOffsetChunk1Mask_Type(OctetString):
    """Custom type swACLPktContMaskOffsetChunk1Mask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_SwACLPktContMaskOffsetChunk1Mask_Type.__name__ = "OctetString"
_SwACLPktContMaskOffsetChunk1Mask_Object = MibTableColumn
swACLPktContMaskOffsetChunk1Mask = _SwACLPktContMaskOffsetChunk1Mask_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 2, 8, 1, 4),
    _SwACLPktContMaskOffsetChunk1Mask_Type()
)
swACLPktContMaskOffsetChunk1Mask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLPktContMaskOffsetChunk1Mask.setStatus("current")


class _SwACLPktContMaskOffsetChunk2State_Type(Integer32):
    """Custom type swACLPktContMaskOffsetChunk2State based on Integer32"""
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


_SwACLPktContMaskOffsetChunk2State_Type.__name__ = "Integer32"
_SwACLPktContMaskOffsetChunk2State_Object = MibTableColumn
swACLPktContMaskOffsetChunk2State = _SwACLPktContMaskOffsetChunk2State_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 2, 8, 1, 5),
    _SwACLPktContMaskOffsetChunk2State_Type()
)
swACLPktContMaskOffsetChunk2State.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLPktContMaskOffsetChunk2State.setStatus("current")


class _SwACLPktContMaskOffsetChunk2OffsetValue_Type(Integer32):
    """Custom type swACLPktContMaskOffsetChunk2OffsetValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_SwACLPktContMaskOffsetChunk2OffsetValue_Type.__name__ = "Integer32"
_SwACLPktContMaskOffsetChunk2OffsetValue_Object = MibTableColumn
swACLPktContMaskOffsetChunk2OffsetValue = _SwACLPktContMaskOffsetChunk2OffsetValue_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 2, 8, 1, 6),
    _SwACLPktContMaskOffsetChunk2OffsetValue_Type()
)
swACLPktContMaskOffsetChunk2OffsetValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLPktContMaskOffsetChunk2OffsetValue.setStatus("current")


class _SwACLPktContMaskOffsetChunk2Mask_Type(OctetString):
    """Custom type swACLPktContMaskOffsetChunk2Mask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_SwACLPktContMaskOffsetChunk2Mask_Type.__name__ = "OctetString"
_SwACLPktContMaskOffsetChunk2Mask_Object = MibTableColumn
swACLPktContMaskOffsetChunk2Mask = _SwACLPktContMaskOffsetChunk2Mask_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 2, 8, 1, 7),
    _SwACLPktContMaskOffsetChunk2Mask_Type()
)
swACLPktContMaskOffsetChunk2Mask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLPktContMaskOffsetChunk2Mask.setStatus("current")


class _SwACLPktContMaskOffsetChunk3State_Type(Integer32):
    """Custom type swACLPktContMaskOffsetChunk3State based on Integer32"""
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


_SwACLPktContMaskOffsetChunk3State_Type.__name__ = "Integer32"
_SwACLPktContMaskOffsetChunk3State_Object = MibTableColumn
swACLPktContMaskOffsetChunk3State = _SwACLPktContMaskOffsetChunk3State_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 2, 8, 1, 8),
    _SwACLPktContMaskOffsetChunk3State_Type()
)
swACLPktContMaskOffsetChunk3State.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLPktContMaskOffsetChunk3State.setStatus("current")


class _SwACLPktContMaskOffsetChunk3OffsetValue_Type(Integer32):
    """Custom type swACLPktContMaskOffsetChunk3OffsetValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_SwACLPktContMaskOffsetChunk3OffsetValue_Type.__name__ = "Integer32"
_SwACLPktContMaskOffsetChunk3OffsetValue_Object = MibTableColumn
swACLPktContMaskOffsetChunk3OffsetValue = _SwACLPktContMaskOffsetChunk3OffsetValue_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 2, 8, 1, 9),
    _SwACLPktContMaskOffsetChunk3OffsetValue_Type()
)
swACLPktContMaskOffsetChunk3OffsetValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLPktContMaskOffsetChunk3OffsetValue.setStatus("current")


class _SwACLPktContMaskOffsetChunk3Mask_Type(OctetString):
    """Custom type swACLPktContMaskOffsetChunk3Mask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_SwACLPktContMaskOffsetChunk3Mask_Type.__name__ = "OctetString"
_SwACLPktContMaskOffsetChunk3Mask_Object = MibTableColumn
swACLPktContMaskOffsetChunk3Mask = _SwACLPktContMaskOffsetChunk3Mask_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 2, 8, 1, 10),
    _SwACLPktContMaskOffsetChunk3Mask_Type()
)
swACLPktContMaskOffsetChunk3Mask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLPktContMaskOffsetChunk3Mask.setStatus("current")


class _SwACLPktContMaskOffsetChunk4State_Type(Integer32):
    """Custom type swACLPktContMaskOffsetChunk4State based on Integer32"""
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


_SwACLPktContMaskOffsetChunk4State_Type.__name__ = "Integer32"
_SwACLPktContMaskOffsetChunk4State_Object = MibTableColumn
swACLPktContMaskOffsetChunk4State = _SwACLPktContMaskOffsetChunk4State_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 2, 8, 1, 11),
    _SwACLPktContMaskOffsetChunk4State_Type()
)
swACLPktContMaskOffsetChunk4State.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLPktContMaskOffsetChunk4State.setStatus("current")


class _SwACLPktContMaskOffsetChunk4OffsetValue_Type(Integer32):
    """Custom type swACLPktContMaskOffsetChunk4OffsetValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_SwACLPktContMaskOffsetChunk4OffsetValue_Type.__name__ = "Integer32"
_SwACLPktContMaskOffsetChunk4OffsetValue_Object = MibTableColumn
swACLPktContMaskOffsetChunk4OffsetValue = _SwACLPktContMaskOffsetChunk4OffsetValue_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 2, 8, 1, 12),
    _SwACLPktContMaskOffsetChunk4OffsetValue_Type()
)
swACLPktContMaskOffsetChunk4OffsetValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLPktContMaskOffsetChunk4OffsetValue.setStatus("current")


class _SwACLPktContMaskOffsetChunk4Mask_Type(OctetString):
    """Custom type swACLPktContMaskOffsetChunk4Mask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_SwACLPktContMaskOffsetChunk4Mask_Type.__name__ = "OctetString"
_SwACLPktContMaskOffsetChunk4Mask_Object = MibTableColumn
swACLPktContMaskOffsetChunk4Mask = _SwACLPktContMaskOffsetChunk4Mask_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 2, 8, 1, 13),
    _SwACLPktContMaskOffsetChunk4Mask_Type()
)
swACLPktContMaskOffsetChunk4Mask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLPktContMaskOffsetChunk4Mask.setStatus("current")
_SwACLPktContMaskOptionRowStatus_Type = RowStatus
_SwACLPktContMaskOptionRowStatus_Object = MibTableColumn
swACLPktContMaskOptionRowStatus = _SwACLPktContMaskOptionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 2, 8, 1, 14),
    _SwACLPktContMaskOptionRowStatus_Type()
)
swACLPktContMaskOptionRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLPktContMaskOptionRowStatus.setStatus("current")


class _SwACLPktContMaskOptionOwner_Type(Integer32):
    """Custom type swACLPktContMaskOptionOwner based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("acl", 2),
          ("any", 1),
          ("dhcp", 5),
          ("ext-netbios", 7),
          ("ipbind", 3),
          ("netbios", 6),
          ("other", 4))
    )


_SwACLPktContMaskOptionOwner_Type.__name__ = "Integer32"
_SwACLPktContMaskOptionOwner_Object = MibTableColumn
swACLPktContMaskOptionOwner = _SwACLPktContMaskOptionOwner_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 2, 8, 1, 15),
    _SwACLPktContMaskOptionOwner_Type()
)
swACLPktContMaskOptionOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swACLPktContMaskOptionOwner.setStatus("current")
_SwACLPktContMaskOptionUnusedRuleEntries_Type = Integer32
_SwACLPktContMaskOptionUnusedRuleEntries_Object = MibTableColumn
swACLPktContMaskOptionUnusedRuleEntries = _SwACLPktContMaskOptionUnusedRuleEntries_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 2, 8, 1, 16),
    _SwACLPktContMaskOptionUnusedRuleEntries_Type()
)
swACLPktContMaskOptionUnusedRuleEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swACLPktContMaskOptionUnusedRuleEntries.setStatus("current")


class _SwACLPktContMaskOptionProfileName_Type(DisplayString):
    """Custom type swACLPktContMaskOptionProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SwACLPktContMaskOptionProfileName_Type.__name__ = "DisplayString"
_SwACLPktContMaskOptionProfileName_Object = MibTableColumn
swACLPktContMaskOptionProfileName = _SwACLPktContMaskOptionProfileName_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 2, 8, 1, 17),
    _SwACLPktContMaskOptionProfileName_Type()
)
swACLPktContMaskOptionProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLPktContMaskOptionProfileName.setStatus("current")
_SwAclRuleMgmt_ObjectIdentity = ObjectIdentity
swAclRuleMgmt = _SwAclRuleMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 3)
)
_SwACLEtherRuleTable_Object = MibTable
swACLEtherRuleTable = _SwACLEtherRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 3, 1)
)
if mibBuilder.loadTexts:
    swACLEtherRuleTable.setStatus("current")
_SwACLEtherRuleEntry_Object = MibTableRow
swACLEtherRuleEntry = _SwACLEtherRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 3, 1, 1)
)
swACLEtherRuleEntry.setIndexNames(
    (0, "ACLMGMT-MIB", "swACLEtherRuleProfileID"),
    (0, "ACLMGMT-MIB", "swACLEtherRuleAccessID"),
)
if mibBuilder.loadTexts:
    swACLEtherRuleEntry.setStatus("current")
_SwACLEtherRuleProfileID_Type = Integer32
_SwACLEtherRuleProfileID_Object = MibTableColumn
swACLEtherRuleProfileID = _SwACLEtherRuleProfileID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 3, 1, 1, 1),
    _SwACLEtherRuleProfileID_Type()
)
swACLEtherRuleProfileID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swACLEtherRuleProfileID.setStatus("current")


class _SwACLEtherRuleAccessID_Type(Integer32):
    """Custom type swACLEtherRuleAccessID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwACLEtherRuleAccessID_Type.__name__ = "Integer32"
_SwACLEtherRuleAccessID_Object = MibTableColumn
swACLEtherRuleAccessID = _SwACLEtherRuleAccessID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 3, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 3, 1, 1, 3),
    _SwACLEtherRuleVlan_Type()
)
swACLEtherRuleVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLEtherRuleVlan.setStatus("current")
_SwACLEtherRuleSrcMacAddress_Type = MacAddress
_SwACLEtherRuleSrcMacAddress_Object = MibTableColumn
swACLEtherRuleSrcMacAddress = _SwACLEtherRuleSrcMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 3, 1, 1, 4),
    _SwACLEtherRuleSrcMacAddress_Type()
)
swACLEtherRuleSrcMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLEtherRuleSrcMacAddress.setStatus("current")
_SwACLEtherRuleDstMacAddress_Type = MacAddress
_SwACLEtherRuleDstMacAddress_Object = MibTableColumn
swACLEtherRuleDstMacAddress = _SwACLEtherRuleDstMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 3, 1, 1, 5),
    _SwACLEtherRuleDstMacAddress_Type()
)
swACLEtherRuleDstMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLEtherRuleDstMacAddress.setStatus("current")


class _SwACLEtherRule8021P_Type(Integer32):
    """Custom type swACLEtherRule8021P based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 7),
    )


_SwACLEtherRule8021P_Type.__name__ = "Integer32"
_SwACLEtherRule8021P_Object = MibTableColumn
swACLEtherRule8021P = _SwACLEtherRule8021P_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 3, 1, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 3, 1, 1, 7),
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
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 3, 1, 1, 8),
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
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 3, 1, 1, 9),
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
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 3, 1, 1, 10),
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
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 3, 1, 1, 11),
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
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 3, 1, 1, 12),
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
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 3, 1, 1, 13),
    _SwACLEtherRulePermit_Type()
)
swACLEtherRulePermit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLEtherRulePermit.setStatus("current")
_SwACLEtherRulePort_Type = PortList
_SwACLEtherRulePort_Object = MibTableColumn
swACLEtherRulePort = _SwACLEtherRulePort_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 3, 1, 1, 14),
    _SwACLEtherRulePort_Type()
)
swACLEtherRulePort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLEtherRulePort.setStatus("current")
_SwACLEtherRuleRowStatus_Type = RowStatus
_SwACLEtherRuleRowStatus_Object = MibTableColumn
swACLEtherRuleRowStatus = _SwACLEtherRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 3, 1, 1, 15),
    _SwACLEtherRuleRowStatus_Type()
)
swACLEtherRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLEtherRuleRowStatus.setStatus("current")


class _SwACLEtherRuleOwner_Type(Integer32):
    """Custom type swACLEtherRuleOwner based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("acl", 2),
          ("any", 1),
          ("dhcp", 5),
          ("ext-netbios", 7),
          ("ipbind", 3),
          ("netbios", 6),
          ("other", 4))
    )


_SwACLEtherRuleOwner_Type.__name__ = "Integer32"
_SwACLEtherRuleOwner_Object = MibTableColumn
swACLEtherRuleOwner = _SwACLEtherRuleOwner_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 3, 1, 1, 16),
    _SwACLEtherRuleOwner_Type()
)
swACLEtherRuleOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swACLEtherRuleOwner.setStatus("current")
_SwACLEtherRuleRxRate_Type = Integer32
_SwACLEtherRuleRxRate_Object = MibTableColumn
swACLEtherRuleRxRate = _SwACLEtherRuleRxRate_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 3, 1, 1, 17),
    _SwACLEtherRuleRxRate_Type()
)
swACLEtherRuleRxRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLEtherRuleRxRate.setStatus("current")


class _SwACLEtherRuleEnableReplaceTosPrecedence_Type(Integer32):
    """Custom type swACLEtherRuleEnableReplaceTosPrecedence based on Integer32"""
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


_SwACLEtherRuleEnableReplaceTosPrecedence_Type.__name__ = "Integer32"
_SwACLEtherRuleEnableReplaceTosPrecedence_Object = MibTableColumn
swACLEtherRuleEnableReplaceTosPrecedence = _SwACLEtherRuleEnableReplaceTosPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 3, 1, 1, 18),
    _SwACLEtherRuleEnableReplaceTosPrecedence_Type()
)
swACLEtherRuleEnableReplaceTosPrecedence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLEtherRuleEnableReplaceTosPrecedence.setStatus("current")


class _SwACLEtherRuleRepTosPrecedence_Type(Integer32):
    """Custom type swACLEtherRuleRepTosPrecedence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_SwACLEtherRuleRepTosPrecedence_Type.__name__ = "Integer32"
_SwACLEtherRuleRepTosPrecedence_Object = MibTableColumn
swACLEtherRuleRepTosPrecedence = _SwACLEtherRuleRepTosPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 3, 1, 1, 19),
    _SwACLEtherRuleRepTosPrecedence_Type()
)
swACLEtherRuleRepTosPrecedence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLEtherRuleRepTosPrecedence.setStatus("current")


class _SwACLEtherRuleVID_Type(Integer32):
    """Custom type swACLEtherRuleVID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_SwACLEtherRuleVID_Type.__name__ = "Integer32"
_SwACLEtherRuleVID_Object = MibTableColumn
swACLEtherRuleVID = _SwACLEtherRuleVID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 3, 1, 1, 20),
    _SwACLEtherRuleVID_Type()
)
swACLEtherRuleVID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLEtherRuleVID.setStatus("current")
_SwACLIpRuleTable_Object = MibTable
swACLIpRuleTable = _SwACLIpRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 3, 2)
)
if mibBuilder.loadTexts:
    swACLIpRuleTable.setStatus("current")
_SwACLIpRuleEntry_Object = MibTableRow
swACLIpRuleEntry = _SwACLIpRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 3, 2, 1)
)
swACLIpRuleEntry.setIndexNames(
    (0, "ACLMGMT-MIB", "swACLIpRuleProfileID"),
    (0, "ACLMGMT-MIB", "swACLIpRuleAccessID"),
)
if mibBuilder.loadTexts:
    swACLIpRuleEntry.setStatus("current")
_SwACLIpRuleProfileID_Type = Integer32
_SwACLIpRuleProfileID_Object = MibTableColumn
swACLIpRuleProfileID = _SwACLIpRuleProfileID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 3, 2, 1, 1),
    _SwACLIpRuleProfileID_Type()
)
swACLIpRuleProfileID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swACLIpRuleProfileID.setStatus("current")


class _SwACLIpRuleAccessID_Type(Integer32):
    """Custom type swACLIpRuleAccessID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwACLIpRuleAccessID_Type.__name__ = "Integer32"
_SwACLIpRuleAccessID_Object = MibTableColumn
swACLIpRuleAccessID = _SwACLIpRuleAccessID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 3, 2, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 3, 2, 1, 3),
    _SwACLIpRuleVlan_Type()
)
swACLIpRuleVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLIpRuleVlan.setStatus("current")
_SwACLIpRuleSrcIpaddress_Type = IpAddress
_SwACLIpRuleSrcIpaddress_Object = MibTableColumn
swACLIpRuleSrcIpaddress = _SwACLIpRuleSrcIpaddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 3, 2, 1, 4),
    _SwACLIpRuleSrcIpaddress_Type()
)
swACLIpRuleSrcIpaddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLIpRuleSrcIpaddress.setStatus("current")
_SwACLIpRuleDstIpaddress_Type = IpAddress
_SwACLIpRuleDstIpaddress_Object = MibTableColumn
swACLIpRuleDstIpaddress = _SwACLIpRuleDstIpaddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 3, 2, 1, 5),
    _SwACLIpRuleDstIpaddress_Type()
)
swACLIpRuleDstIpaddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLIpRuleDstIpaddress.setStatus("current")


class _SwACLIpRuleDscp_Type(Integer32):
    """Custom type swACLIpRuleDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 63),
    )


_SwACLIpRuleDscp_Type.__name__ = "Integer32"
_SwACLIpRuleDscp_Object = MibTableColumn
swACLIpRuleDscp = _SwACLIpRuleDscp_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 3, 2, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 3, 2, 1, 7),
    _SwACLIpRuleProtocol_Type()
)
swACLIpRuleProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swACLIpRuleProtocol.setStatus("current")


class _SwACLIpRuleType_Type(Integer32):
    """Custom type swACLIpRuleType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 255),
    )


_SwACLIpRuleType_Type.__name__ = "Integer32"
_SwACLIpRuleType_Object = MibTableColumn
swACLIpRuleType = _SwACLIpRuleType_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 3, 2, 1, 8),
    _SwACLIpRuleType_Type()
)
swACLIpRuleType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLIpRuleType.setStatus("current")


class _SwACLIpRuleCode_Type(Integer32):
    """Custom type swACLIpRuleCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 255),
    )


_SwACLIpRuleCode_Type.__name__ = "Integer32"
_SwACLIpRuleCode_Object = MibTableColumn
swACLIpRuleCode = _SwACLIpRuleCode_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 3, 2, 1, 9),
    _SwACLIpRuleCode_Type()
)
swACLIpRuleCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLIpRuleCode.setStatus("current")


class _SwACLIpRuleSrcPort_Type(Integer32):
    """Custom type swACLIpRuleSrcPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_SwACLIpRuleSrcPort_Type.__name__ = "Integer32"
_SwACLIpRuleSrcPort_Object = MibTableColumn
swACLIpRuleSrcPort = _SwACLIpRuleSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 3, 2, 1, 10),
    _SwACLIpRuleSrcPort_Type()
)
swACLIpRuleSrcPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLIpRuleSrcPort.setStatus("current")


class _SwACLIpRuleDstPort_Type(Integer32):
    """Custom type swACLIpRuleDstPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_SwACLIpRuleDstPort_Type.__name__ = "Integer32"
_SwACLIpRuleDstPort_Object = MibTableColumn
swACLIpRuleDstPort = _SwACLIpRuleDstPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 3, 2, 1, 11),
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
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 3, 2, 1, 12),
    _SwACLIpRuleFlagBits_Type()
)
swACLIpRuleFlagBits.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLIpRuleFlagBits.setStatus("current")


class _SwACLIpRuleProtoID_Type(Integer32):
    """Custom type swACLIpRuleProtoID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 255),
    )


_SwACLIpRuleProtoID_Type.__name__ = "Integer32"
_SwACLIpRuleProtoID_Object = MibTableColumn
swACLIpRuleProtoID = _SwACLIpRuleProtoID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 3, 2, 1, 13),
    _SwACLIpRuleProtoID_Type()
)
swACLIpRuleProtoID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLIpRuleProtoID.setStatus("current")


class _SwACLIpRuleUserMask_Type(OctetString):
    """Custom type swACLIpRuleUserMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_SwACLIpRuleUserMask_Type.__name__ = "OctetString"
_SwACLIpRuleUserMask_Object = MibTableColumn
swACLIpRuleUserMask = _SwACLIpRuleUserMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 3, 2, 1, 14),
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
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 3, 2, 1, 15),
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
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 3, 2, 1, 16),
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
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 3, 2, 1, 17),
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
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 3, 2, 1, 18),
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
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 3, 2, 1, 19),
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
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 3, 2, 1, 20),
    _SwACLIpRulePermit_Type()
)
swACLIpRulePermit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLIpRulePermit.setStatus("current")
_SwACLIpRulePort_Type = PortList
_SwACLIpRulePort_Object = MibTableColumn
swACLIpRulePort = _SwACLIpRulePort_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 3, 2, 1, 21),
    _SwACLIpRulePort_Type()
)
swACLIpRulePort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLIpRulePort.setStatus("current")
_SwACLIpRuleRowStatus_Type = RowStatus
_SwACLIpRuleRowStatus_Object = MibTableColumn
swACLIpRuleRowStatus = _SwACLIpRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 3, 2, 1, 22),
    _SwACLIpRuleRowStatus_Type()
)
swACLIpRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLIpRuleRowStatus.setStatus("current")


class _SwACLIpRuleOwner_Type(Integer32):
    """Custom type swACLIpRuleOwner based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("acl", 2),
          ("any", 1),
          ("dhcp", 5),
          ("ext-netbios", 7),
          ("ipbind", 3),
          ("netbios", 6),
          ("other", 4))
    )


_SwACLIpRuleOwner_Type.__name__ = "Integer32"
_SwACLIpRuleOwner_Object = MibTableColumn
swACLIpRuleOwner = _SwACLIpRuleOwner_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 3, 2, 1, 23),
    _SwACLIpRuleOwner_Type()
)
swACLIpRuleOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swACLIpRuleOwner.setStatus("current")
_SwACLIpRuleRxRate_Type = Integer32
_SwACLIpRuleRxRate_Object = MibTableColumn
swACLIpRuleRxRate = _SwACLIpRuleRxRate_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 3, 2, 1, 24),
    _SwACLIpRuleRxRate_Type()
)
swACLIpRuleRxRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLIpRuleRxRate.setStatus("current")


class _SwACLIpRuleEnableReplaceTosPrecedence_Type(Integer32):
    """Custom type swACLIpRuleEnableReplaceTosPrecedence based on Integer32"""
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


_SwACLIpRuleEnableReplaceTosPrecedence_Type.__name__ = "Integer32"
_SwACLIpRuleEnableReplaceTosPrecedence_Object = MibTableColumn
swACLIpRuleEnableReplaceTosPrecedence = _SwACLIpRuleEnableReplaceTosPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 3, 2, 1, 26),
    _SwACLIpRuleEnableReplaceTosPrecedence_Type()
)
swACLIpRuleEnableReplaceTosPrecedence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLIpRuleEnableReplaceTosPrecedence.setStatus("current")


class _SwACLIpRuleRepTosPrecedence_Type(Integer32):
    """Custom type swACLIpRuleRepTosPrecedence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_SwACLIpRuleRepTosPrecedence_Type.__name__ = "Integer32"
_SwACLIpRuleRepTosPrecedence_Object = MibTableColumn
swACLIpRuleRepTosPrecedence = _SwACLIpRuleRepTosPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 3, 2, 1, 27),
    _SwACLIpRuleRepTosPrecedence_Type()
)
swACLIpRuleRepTosPrecedence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLIpRuleRepTosPrecedence.setStatus("current")


class _SwACLIpRuleVID_Type(Integer32):
    """Custom type swACLIpRuleVID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_SwACLIpRuleVID_Type.__name__ = "Integer32"
_SwACLIpRuleVID_Object = MibTableColumn
swACLIpRuleVID = _SwACLIpRuleVID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 3, 2, 1, 28),
    _SwACLIpRuleVID_Type()
)
swACLIpRuleVID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLIpRuleVID.setStatus("current")
_SwACLIpv6RuleTable_Object = MibTable
swACLIpv6RuleTable = _SwACLIpv6RuleTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 3, 4)
)
if mibBuilder.loadTexts:
    swACLIpv6RuleTable.setStatus("current")
_SwACLIpv6RuleEntry_Object = MibTableRow
swACLIpv6RuleEntry = _SwACLIpv6RuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 3, 4, 1)
)
swACLIpv6RuleEntry.setIndexNames(
    (0, "ACLMGMT-MIB", "swACLIpv6RuleProfileID"),
    (0, "ACLMGMT-MIB", "swACLIpv6RuleAccessID"),
)
if mibBuilder.loadTexts:
    swACLIpv6RuleEntry.setStatus("current")
_SwACLIpv6RuleProfileID_Type = Integer32
_SwACLIpv6RuleProfileID_Object = MibTableColumn
swACLIpv6RuleProfileID = _SwACLIpv6RuleProfileID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 3, 4, 1, 1),
    _SwACLIpv6RuleProfileID_Type()
)
swACLIpv6RuleProfileID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swACLIpv6RuleProfileID.setStatus("current")


class _SwACLIpv6RuleAccessID_Type(Integer32):
    """Custom type swACLIpv6RuleAccessID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwACLIpv6RuleAccessID_Type.__name__ = "Integer32"
_SwACLIpv6RuleAccessID_Object = MibTableColumn
swACLIpv6RuleAccessID = _SwACLIpv6RuleAccessID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 3, 4, 1, 2),
    _SwACLIpv6RuleAccessID_Type()
)
swACLIpv6RuleAccessID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swACLIpv6RuleAccessID.setStatus("current")


class _SwACLIpv6RuleClass_Type(Integer32):
    """Custom type swACLIpv6RuleClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SwACLIpv6RuleClass_Type.__name__ = "Integer32"
_SwACLIpv6RuleClass_Object = MibTableColumn
swACLIpv6RuleClass = _SwACLIpv6RuleClass_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 3, 4, 1, 3),
    _SwACLIpv6RuleClass_Type()
)
swACLIpv6RuleClass.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLIpv6RuleClass.setStatus("current")


class _SwACLIpv6RuleFlowlabel_Type(OctetString):
    """Custom type swACLIpv6RuleFlowlabel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_SwACLIpv6RuleFlowlabel_Type.__name__ = "OctetString"
_SwACLIpv6RuleFlowlabel_Object = MibTableColumn
swACLIpv6RuleFlowlabel = _SwACLIpv6RuleFlowlabel_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 3, 4, 1, 4),
    _SwACLIpv6RuleFlowlabel_Type()
)
swACLIpv6RuleFlowlabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLIpv6RuleFlowlabel.setStatus("current")
_SwACLIpv6RuleSrcIpv6Addr_Type = Ipv6Address
_SwACLIpv6RuleSrcIpv6Addr_Object = MibTableColumn
swACLIpv6RuleSrcIpv6Addr = _SwACLIpv6RuleSrcIpv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 3, 4, 1, 5),
    _SwACLIpv6RuleSrcIpv6Addr_Type()
)
swACLIpv6RuleSrcIpv6Addr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLIpv6RuleSrcIpv6Addr.setStatus("current")
_SwACLIpv6RuleDstIpv6Addr_Type = Ipv6Address
_SwACLIpv6RuleDstIpv6Addr_Object = MibTableColumn
swACLIpv6RuleDstIpv6Addr = _SwACLIpv6RuleDstIpv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 3, 4, 1, 6),
    _SwACLIpv6RuleDstIpv6Addr_Type()
)
swACLIpv6RuleDstIpv6Addr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLIpv6RuleDstIpv6Addr.setStatus("current")


class _SwACLIpv6RuleEnablePriority_Type(Integer32):
    """Custom type swACLIpv6RuleEnablePriority based on Integer32"""
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


_SwACLIpv6RuleEnablePriority_Type.__name__ = "Integer32"
_SwACLIpv6RuleEnablePriority_Object = MibTableColumn
swACLIpv6RuleEnablePriority = _SwACLIpv6RuleEnablePriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 3, 4, 1, 7),
    _SwACLIpv6RuleEnablePriority_Type()
)
swACLIpv6RuleEnablePriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLIpv6RuleEnablePriority.setStatus("current")


class _SwACLIpv6RulePriority_Type(Integer32):
    """Custom type swACLIpv6RulePriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_SwACLIpv6RulePriority_Type.__name__ = "Integer32"
_SwACLIpv6RulePriority_Object = MibTableColumn
swACLIpv6RulePriority = _SwACLIpv6RulePriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 3, 4, 1, 8),
    _SwACLIpv6RulePriority_Type()
)
swACLIpv6RulePriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLIpv6RulePriority.setStatus("current")


class _SwACLIpv6RuleReplacePriority_Type(Integer32):
    """Custom type swACLIpv6RuleReplacePriority based on Integer32"""
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


_SwACLIpv6RuleReplacePriority_Type.__name__ = "Integer32"
_SwACLIpv6RuleReplacePriority_Object = MibTableColumn
swACLIpv6RuleReplacePriority = _SwACLIpv6RuleReplacePriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 3, 4, 1, 9),
    _SwACLIpv6RuleReplacePriority_Type()
)
swACLIpv6RuleReplacePriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLIpv6RuleReplacePriority.setStatus("current")


class _SwACLIpv6RulePermit_Type(Integer32):
    """Custom type swACLIpv6RulePermit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("deny", 1),
          ("mirror", 3),
          ("permit", 2))
    )


_SwACLIpv6RulePermit_Type.__name__ = "Integer32"
_SwACLIpv6RulePermit_Object = MibTableColumn
swACLIpv6RulePermit = _SwACLIpv6RulePermit_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 3, 4, 1, 10),
    _SwACLIpv6RulePermit_Type()
)
swACLIpv6RulePermit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLIpv6RulePermit.setStatus("current")
_SwACLIpv6RulePort_Type = PortList
_SwACLIpv6RulePort_Object = MibTableColumn
swACLIpv6RulePort = _SwACLIpv6RulePort_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 3, 4, 1, 11),
    _SwACLIpv6RulePort_Type()
)
swACLIpv6RulePort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLIpv6RulePort.setStatus("current")
_SwACLIpv6RuleRowStatus_Type = RowStatus
_SwACLIpv6RuleRowStatus_Object = MibTableColumn
swACLIpv6RuleRowStatus = _SwACLIpv6RuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 3, 4, 1, 12),
    _SwACLIpv6RuleRowStatus_Type()
)
swACLIpv6RuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLIpv6RuleRowStatus.setStatus("current")


class _SwACLIpv6RuleOwner_Type(Integer32):
    """Custom type swACLIpv6RuleOwner based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("acl", 2),
          ("any", 1),
          ("dhcp", 5),
          ("ext-netbios", 7),
          ("ipbind", 3),
          ("netbios", 6),
          ("other", 4))
    )


_SwACLIpv6RuleOwner_Type.__name__ = "Integer32"
_SwACLIpv6RuleOwner_Object = MibTableColumn
swACLIpv6RuleOwner = _SwACLIpv6RuleOwner_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 3, 4, 1, 13),
    _SwACLIpv6RuleOwner_Type()
)
swACLIpv6RuleOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swACLIpv6RuleOwner.setStatus("current")
_SwACLIpv6RuleRxRate_Type = Integer32
_SwACLIpv6RuleRxRate_Object = MibTableColumn
swACLIpv6RuleRxRate = _SwACLIpv6RuleRxRate_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 3, 4, 1, 14),
    _SwACLIpv6RuleRxRate_Type()
)
swACLIpv6RuleRxRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLIpv6RuleRxRate.setStatus("current")


class _SwACLIpv6RuleEnableReplaceDscp_Type(Integer32):
    """Custom type swACLIpv6RuleEnableReplaceDscp based on Integer32"""
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


_SwACLIpv6RuleEnableReplaceDscp_Type.__name__ = "Integer32"
_SwACLIpv6RuleEnableReplaceDscp_Object = MibTableColumn
swACLIpv6RuleEnableReplaceDscp = _SwACLIpv6RuleEnableReplaceDscp_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 3, 4, 1, 15),
    _SwACLIpv6RuleEnableReplaceDscp_Type()
)
swACLIpv6RuleEnableReplaceDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLIpv6RuleEnableReplaceDscp.setStatus("current")


class _SwACLIpv6RuleRepDscp_Type(Integer32):
    """Custom type swACLIpv6RuleRepDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_SwACLIpv6RuleRepDscp_Type.__name__ = "Integer32"
_SwACLIpv6RuleRepDscp_Object = MibTableColumn
swACLIpv6RuleRepDscp = _SwACLIpv6RuleRepDscp_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 3, 4, 1, 16),
    _SwACLIpv6RuleRepDscp_Type()
)
swACLIpv6RuleRepDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLIpv6RuleRepDscp.setStatus("current")


class _SwACLIpv6RuleEnableReplaceTosPrecedence_Type(Integer32):
    """Custom type swACLIpv6RuleEnableReplaceTosPrecedence based on Integer32"""
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


_SwACLIpv6RuleEnableReplaceTosPrecedence_Type.__name__ = "Integer32"
_SwACLIpv6RuleEnableReplaceTosPrecedence_Object = MibTableColumn
swACLIpv6RuleEnableReplaceTosPrecedence = _SwACLIpv6RuleEnableReplaceTosPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 3, 4, 1, 17),
    _SwACLIpv6RuleEnableReplaceTosPrecedence_Type()
)
swACLIpv6RuleEnableReplaceTosPrecedence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLIpv6RuleEnableReplaceTosPrecedence.setStatus("current")


class _SwACLIpv6RuleRepTosPrecedence_Type(Integer32):
    """Custom type swACLIpv6RuleRepTosPrecedence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_SwACLIpv6RuleRepTosPrecedence_Type.__name__ = "Integer32"
_SwACLIpv6RuleRepTosPrecedence_Object = MibTableColumn
swACLIpv6RuleRepTosPrecedence = _SwACLIpv6RuleRepTosPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 3, 4, 1, 18),
    _SwACLIpv6RuleRepTosPrecedence_Type()
)
swACLIpv6RuleRepTosPrecedence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLIpv6RuleRepTosPrecedence.setStatus("current")


class _SwACLIpv6RuleVID_Type(Integer32):
    """Custom type swACLIpv6RuleVID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_SwACLIpv6RuleVID_Type.__name__ = "Integer32"
_SwACLIpv6RuleVID_Object = MibTableColumn
swACLIpv6RuleVID = _SwACLIpv6RuleVID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 3, 4, 1, 19),
    _SwACLIpv6RuleVID_Type()
)
swACLIpv6RuleVID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLIpv6RuleVID.setStatus("current")


class _SwACLIpv6RuleProtocol_Type(Integer32):
    """Custom type swACLIpv6RuleProtocol based on Integer32"""
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
          ("tcp", 2),
          ("udp", 3))
    )


_SwACLIpv6RuleProtocol_Type.__name__ = "Integer32"
_SwACLIpv6RuleProtocol_Object = MibTableColumn
swACLIpv6RuleProtocol = _SwACLIpv6RuleProtocol_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 3, 4, 1, 20),
    _SwACLIpv6RuleProtocol_Type()
)
swACLIpv6RuleProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLIpv6RuleProtocol.setStatus("current")


class _SwACLIpv6RuleSrcPort_Type(Integer32):
    """Custom type swACLIpv6RuleSrcPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwACLIpv6RuleSrcPort_Type.__name__ = "Integer32"
_SwACLIpv6RuleSrcPort_Object = MibTableColumn
swACLIpv6RuleSrcPort = _SwACLIpv6RuleSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 3, 4, 1, 21),
    _SwACLIpv6RuleSrcPort_Type()
)
swACLIpv6RuleSrcPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLIpv6RuleSrcPort.setStatus("current")


class _SwACLIpv6RuleDstPort_Type(Integer32):
    """Custom type swACLIpv6RuleDstPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwACLIpv6RuleDstPort_Type.__name__ = "Integer32"
_SwACLIpv6RuleDstPort_Object = MibTableColumn
swACLIpv6RuleDstPort = _SwACLIpv6RuleDstPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 3, 4, 1, 22),
    _SwACLIpv6RuleDstPort_Type()
)
swACLIpv6RuleDstPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLIpv6RuleDstPort.setStatus("current")
_SwIBPACLEtherRuleTable_Object = MibTable
swIBPACLEtherRuleTable = _SwIBPACLEtherRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 3, 5)
)
if mibBuilder.loadTexts:
    swIBPACLEtherRuleTable.setStatus("obsolete")
_SwIBPACLEtherRuleEntry_Object = MibTableRow
swIBPACLEtherRuleEntry = _SwIBPACLEtherRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 3, 5, 1)
)
swIBPACLEtherRuleEntry.setIndexNames(
    (0, "ACLMGMT-MIB", "swIBPACLEtherRuleProfileID"),
    (0, "ACLMGMT-MIB", "swIBPACLEtherRuleAccessID"),
)
if mibBuilder.loadTexts:
    swIBPACLEtherRuleEntry.setStatus("obsolete")
_SwIBPACLEtherRuleProfileID_Type = Integer32
_SwIBPACLEtherRuleProfileID_Object = MibTableColumn
swIBPACLEtherRuleProfileID = _SwIBPACLEtherRuleProfileID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 3, 5, 1, 1),
    _SwIBPACLEtherRuleProfileID_Type()
)
swIBPACLEtherRuleProfileID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIBPACLEtherRuleProfileID.setStatus("obsolete")


class _SwIBPACLEtherRuleAccessID_Type(Integer32):
    """Custom type swIBPACLEtherRuleAccessID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwIBPACLEtherRuleAccessID_Type.__name__ = "Integer32"
_SwIBPACLEtherRuleAccessID_Object = MibTableColumn
swIBPACLEtherRuleAccessID = _SwIBPACLEtherRuleAccessID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 3, 5, 1, 2),
    _SwIBPACLEtherRuleAccessID_Type()
)
swIBPACLEtherRuleAccessID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIBPACLEtherRuleAccessID.setStatus("obsolete")


class _SwIBPACLEtherRuleEtherType_Type(OctetString):
    """Custom type swIBPACLEtherRuleEtherType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_SwIBPACLEtherRuleEtherType_Type.__name__ = "OctetString"
_SwIBPACLEtherRuleEtherType_Object = MibTableColumn
swIBPACLEtherRuleEtherType = _SwIBPACLEtherRuleEtherType_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 3, 5, 1, 3),
    _SwIBPACLEtherRuleEtherType_Type()
)
swIBPACLEtherRuleEtherType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIBPACLEtherRuleEtherType.setStatus("obsolete")


class _SwIBPACLEtherRulePermit_Type(Integer32):
    """Custom type swIBPACLEtherRulePermit based on Integer32"""
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


_SwIBPACLEtherRulePermit_Type.__name__ = "Integer32"
_SwIBPACLEtherRulePermit_Object = MibTableColumn
swIBPACLEtherRulePermit = _SwIBPACLEtherRulePermit_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 3, 5, 1, 4),
    _SwIBPACLEtherRulePermit_Type()
)
swIBPACLEtherRulePermit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIBPACLEtherRulePermit.setStatus("obsolete")
_SwIBPACLEtherRulePort_Type = PortList
_SwIBPACLEtherRulePort_Object = MibTableColumn
swIBPACLEtherRulePort = _SwIBPACLEtherRulePort_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 3, 5, 1, 5),
    _SwIBPACLEtherRulePort_Type()
)
swIBPACLEtherRulePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIBPACLEtherRulePort.setStatus("obsolete")
_SwIBPACLIpRuleTable_Object = MibTable
swIBPACLIpRuleTable = _SwIBPACLIpRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 3, 6)
)
if mibBuilder.loadTexts:
    swIBPACLIpRuleTable.setStatus("obsolete")
_SwIBPACLIpRuleEntry_Object = MibTableRow
swIBPACLIpRuleEntry = _SwIBPACLIpRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 3, 6, 1)
)
swIBPACLIpRuleEntry.setIndexNames(
    (0, "ACLMGMT-MIB", "swIBPACLIpRuleProfileID"),
    (0, "ACLMGMT-MIB", "swIBPACLIpRuleAccessID"),
)
if mibBuilder.loadTexts:
    swIBPACLIpRuleEntry.setStatus("obsolete")
_SwIBPACLIpRuleProfileID_Type = Integer32
_SwIBPACLIpRuleProfileID_Object = MibTableColumn
swIBPACLIpRuleProfileID = _SwIBPACLIpRuleProfileID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 3, 6, 1, 1),
    _SwIBPACLIpRuleProfileID_Type()
)
swIBPACLIpRuleProfileID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIBPACLIpRuleProfileID.setStatus("obsolete")


class _SwIBPACLIpRuleAccessID_Type(Integer32):
    """Custom type swIBPACLIpRuleAccessID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwIBPACLIpRuleAccessID_Type.__name__ = "Integer32"
_SwIBPACLIpRuleAccessID_Object = MibTableColumn
swIBPACLIpRuleAccessID = _SwIBPACLIpRuleAccessID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 3, 6, 1, 2),
    _SwIBPACLIpRuleAccessID_Type()
)
swIBPACLIpRuleAccessID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIBPACLIpRuleAccessID.setStatus("obsolete")
_SwIBPACLIpRuleSrcMacAddress_Type = MacAddress
_SwIBPACLIpRuleSrcMacAddress_Object = MibTableColumn
swIBPACLIpRuleSrcMacAddress = _SwIBPACLIpRuleSrcMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 3, 6, 1, 3),
    _SwIBPACLIpRuleSrcMacAddress_Type()
)
swIBPACLIpRuleSrcMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIBPACLIpRuleSrcMacAddress.setStatus("obsolete")
_SwIBPACLIpRuleSrcIpaddress_Type = IpAddress
_SwIBPACLIpRuleSrcIpaddress_Object = MibTableColumn
swIBPACLIpRuleSrcIpaddress = _SwIBPACLIpRuleSrcIpaddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 3, 6, 1, 4),
    _SwIBPACLIpRuleSrcIpaddress_Type()
)
swIBPACLIpRuleSrcIpaddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIBPACLIpRuleSrcIpaddress.setStatus("obsolete")


class _SwIBPACLIpRulePermit_Type(Integer32):
    """Custom type swIBPACLIpRulePermit based on Integer32"""
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


_SwIBPACLIpRulePermit_Type.__name__ = "Integer32"
_SwIBPACLIpRulePermit_Object = MibTableColumn
swIBPACLIpRulePermit = _SwIBPACLIpRulePermit_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 3, 6, 1, 5),
    _SwIBPACLIpRulePermit_Type()
)
swIBPACLIpRulePermit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIBPACLIpRulePermit.setStatus("obsolete")
_SwIBPACLIpRulePort_Type = PortList
_SwIBPACLIpRulePort_Object = MibTableColumn
swIBPACLIpRulePort = _SwIBPACLIpRulePort_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 3, 6, 1, 6),
    _SwIBPACLIpRulePort_Type()
)
swIBPACLIpRulePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIBPACLIpRulePort.setStatus("obsolete")
_SwACLCounterTable_Object = MibTable
swACLCounterTable = _SwACLCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 3, 8)
)
if mibBuilder.loadTexts:
    swACLCounterTable.setStatus("current")
_SwACLCounterEntry_Object = MibTableRow
swACLCounterEntry = _SwACLCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 3, 8, 1)
)
swACLCounterEntry.setIndexNames(
    (0, "ACLMGMT-MIB", "swACLCounterProfileID"),
    (0, "ACLMGMT-MIB", "swACLCounterAccessID"),
)
if mibBuilder.loadTexts:
    swACLCounterEntry.setStatus("current")
_SwACLCounterProfileID_Type = Integer32
_SwACLCounterProfileID_Object = MibTableColumn
swACLCounterProfileID = _SwACLCounterProfileID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 3, 8, 1, 1),
    _SwACLCounterProfileID_Type()
)
swACLCounterProfileID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swACLCounterProfileID.setStatus("current")


class _SwACLCounterAccessID_Type(Integer32):
    """Custom type swACLCounterAccessID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SwACLCounterAccessID_Type.__name__ = "Integer32"
_SwACLCounterAccessID_Object = MibTableColumn
swACLCounterAccessID = _SwACLCounterAccessID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 3, 8, 1, 2),
    _SwACLCounterAccessID_Type()
)
swACLCounterAccessID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swACLCounterAccessID.setStatus("current")


class _SwACLCounterState_Type(Integer32):
    """Custom type swACLCounterState based on Integer32"""
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


_SwACLCounterState_Type.__name__ = "Integer32"
_SwACLCounterState_Object = MibTableColumn
swACLCounterState = _SwACLCounterState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 3, 8, 1, 3),
    _SwACLCounterState_Type()
)
swACLCounterState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swACLCounterState.setStatus("current")
_SwACLCounterTotalCounter_Type = Counter64
_SwACLCounterTotalCounter_Object = MibTableColumn
swACLCounterTotalCounter = _SwACLCounterTotalCounter_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 3, 8, 1, 4),
    _SwACLCounterTotalCounter_Type()
)
swACLCounterTotalCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swACLCounterTotalCounter.setStatus("current")
_SwACLCounterGreenCounter_Type = Counter64
_SwACLCounterGreenCounter_Object = MibTableColumn
swACLCounterGreenCounter = _SwACLCounterGreenCounter_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 3, 8, 1, 5),
    _SwACLCounterGreenCounter_Type()
)
swACLCounterGreenCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swACLCounterGreenCounter.setStatus("current")
_SwACLCounterYellowCounter_Type = Counter64
_SwACLCounterYellowCounter_Object = MibTableColumn
swACLCounterYellowCounter = _SwACLCounterYellowCounter_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 3, 8, 1, 6),
    _SwACLCounterYellowCounter_Type()
)
swACLCounterYellowCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swACLCounterYellowCounter.setStatus("current")
_SwACLCounterRedCounter_Type = Counter64
_SwACLCounterRedCounter_Object = MibTableColumn
swACLCounterRedCounter = _SwACLCounterRedCounter_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 3, 8, 1, 7),
    _SwACLCounterRedCounter_Type()
)
swACLCounterRedCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swACLCounterRedCounter.setStatus("current")
_SwACLPktContRuleVarOffsetTable_Object = MibTable
swACLPktContRuleVarOffsetTable = _SwACLPktContRuleVarOffsetTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 3, 9)
)
if mibBuilder.loadTexts:
    swACLPktContRuleVarOffsetTable.setStatus("current")
_SwACLPktContRuleVarOffsetEntry_Object = MibTableRow
swACLPktContRuleVarOffsetEntry = _SwACLPktContRuleVarOffsetEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 3, 9, 1)
)
swACLPktContRuleVarOffsetEntry.setIndexNames(
    (0, "ACLMGMT-MIB", "swACLPktContRuleVarOffsetProfileID"),
    (0, "ACLMGMT-MIB", "swACLPktContRuleVarOffsetAccessID"),
)
if mibBuilder.loadTexts:
    swACLPktContRuleVarOffsetEntry.setStatus("current")


class _SwACLPktContRuleVarOffsetProfileID_Type(Integer32):
    """Custom type swACLPktContRuleVarOffsetProfileID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_SwACLPktContRuleVarOffsetProfileID_Type.__name__ = "Integer32"
_SwACLPktContRuleVarOffsetProfileID_Object = MibTableColumn
swACLPktContRuleVarOffsetProfileID = _SwACLPktContRuleVarOffsetProfileID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 3, 9, 1, 1),
    _SwACLPktContRuleVarOffsetProfileID_Type()
)
swACLPktContRuleVarOffsetProfileID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swACLPktContRuleVarOffsetProfileID.setStatus("current")


class _SwACLPktContRuleVarOffsetAccessID_Type(Integer32):
    """Custom type swACLPktContRuleVarOffsetAccessID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SwACLPktContRuleVarOffsetAccessID_Type.__name__ = "Integer32"
_SwACLPktContRuleVarOffsetAccessID_Object = MibTableColumn
swACLPktContRuleVarOffsetAccessID = _SwACLPktContRuleVarOffsetAccessID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 3, 9, 1, 2),
    _SwACLPktContRuleVarOffsetAccessID_Type()
)
swACLPktContRuleVarOffsetAccessID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swACLPktContRuleVarOffsetAccessID.setStatus("current")


class _SwACLPktContRuleVarOffsetOffsetIndex1_Type(Integer32):
    """Custom type swACLPktContRuleVarOffsetOffsetIndex1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 76),
    )


_SwACLPktContRuleVarOffsetOffsetIndex1_Type.__name__ = "Integer32"
_SwACLPktContRuleVarOffsetOffsetIndex1_Object = MibTableColumn
swACLPktContRuleVarOffsetOffsetIndex1 = _SwACLPktContRuleVarOffsetOffsetIndex1_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 3, 9, 1, 8),
    _SwACLPktContRuleVarOffsetOffsetIndex1_Type()
)
swACLPktContRuleVarOffsetOffsetIndex1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLPktContRuleVarOffsetOffsetIndex1.setStatus("current")


class _SwACLPktContRuleVarOffsetMask1_Type(OctetString):
    """Custom type swACLPktContRuleVarOffsetMask1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_SwACLPktContRuleVarOffsetMask1_Type.__name__ = "OctetString"
_SwACLPktContRuleVarOffsetMask1_Object = MibTableColumn
swACLPktContRuleVarOffsetMask1 = _SwACLPktContRuleVarOffsetMask1_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 3, 9, 1, 9),
    _SwACLPktContRuleVarOffsetMask1_Type()
)
swACLPktContRuleVarOffsetMask1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swACLPktContRuleVarOffsetMask1.setStatus("current")


class _SwACLPktContRuleVarOffsetData1_Type(OctetString):
    """Custom type swACLPktContRuleVarOffsetData1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_SwACLPktContRuleVarOffsetData1_Type.__name__ = "OctetString"
_SwACLPktContRuleVarOffsetData1_Object = MibTableColumn
swACLPktContRuleVarOffsetData1 = _SwACLPktContRuleVarOffsetData1_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 3, 9, 1, 10),
    _SwACLPktContRuleVarOffsetData1_Type()
)
swACLPktContRuleVarOffsetData1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLPktContRuleVarOffsetData1.setStatus("current")


class _SwACLPktContRuleVarOffsetOffsetIndex2_Type(Integer32):
    """Custom type swACLPktContRuleVarOffsetOffsetIndex2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 76),
    )


_SwACLPktContRuleVarOffsetOffsetIndex2_Type.__name__ = "Integer32"
_SwACLPktContRuleVarOffsetOffsetIndex2_Object = MibTableColumn
swACLPktContRuleVarOffsetOffsetIndex2 = _SwACLPktContRuleVarOffsetOffsetIndex2_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 3, 9, 1, 11),
    _SwACLPktContRuleVarOffsetOffsetIndex2_Type()
)
swACLPktContRuleVarOffsetOffsetIndex2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLPktContRuleVarOffsetOffsetIndex2.setStatus("current")


class _SwACLPktContRuleVarOffsetMask2_Type(OctetString):
    """Custom type swACLPktContRuleVarOffsetMask2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_SwACLPktContRuleVarOffsetMask2_Type.__name__ = "OctetString"
_SwACLPktContRuleVarOffsetMask2_Object = MibTableColumn
swACLPktContRuleVarOffsetMask2 = _SwACLPktContRuleVarOffsetMask2_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 3, 9, 1, 12),
    _SwACLPktContRuleVarOffsetMask2_Type()
)
swACLPktContRuleVarOffsetMask2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swACLPktContRuleVarOffsetMask2.setStatus("current")


class _SwACLPktContRuleVarOffsetData2_Type(OctetString):
    """Custom type swACLPktContRuleVarOffsetData2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_SwACLPktContRuleVarOffsetData2_Type.__name__ = "OctetString"
_SwACLPktContRuleVarOffsetData2_Object = MibTableColumn
swACLPktContRuleVarOffsetData2 = _SwACLPktContRuleVarOffsetData2_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 3, 9, 1, 13),
    _SwACLPktContRuleVarOffsetData2_Type()
)
swACLPktContRuleVarOffsetData2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLPktContRuleVarOffsetData2.setStatus("current")


class _SwACLPktContRuleVarOffsetOffsetIndex3_Type(Integer32):
    """Custom type swACLPktContRuleVarOffsetOffsetIndex3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 76),
    )


_SwACLPktContRuleVarOffsetOffsetIndex3_Type.__name__ = "Integer32"
_SwACLPktContRuleVarOffsetOffsetIndex3_Object = MibTableColumn
swACLPktContRuleVarOffsetOffsetIndex3 = _SwACLPktContRuleVarOffsetOffsetIndex3_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 3, 9, 1, 14),
    _SwACLPktContRuleVarOffsetOffsetIndex3_Type()
)
swACLPktContRuleVarOffsetOffsetIndex3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLPktContRuleVarOffsetOffsetIndex3.setStatus("current")


class _SwACLPktContRuleVarOffsetMask3_Type(OctetString):
    """Custom type swACLPktContRuleVarOffsetMask3 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_SwACLPktContRuleVarOffsetMask3_Type.__name__ = "OctetString"
_SwACLPktContRuleVarOffsetMask3_Object = MibTableColumn
swACLPktContRuleVarOffsetMask3 = _SwACLPktContRuleVarOffsetMask3_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 3, 9, 1, 15),
    _SwACLPktContRuleVarOffsetMask3_Type()
)
swACLPktContRuleVarOffsetMask3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swACLPktContRuleVarOffsetMask3.setStatus("current")


class _SwACLPktContRuleVarOffsetData3_Type(OctetString):
    """Custom type swACLPktContRuleVarOffsetData3 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_SwACLPktContRuleVarOffsetData3_Type.__name__ = "OctetString"
_SwACLPktContRuleVarOffsetData3_Object = MibTableColumn
swACLPktContRuleVarOffsetData3 = _SwACLPktContRuleVarOffsetData3_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 3, 9, 1, 16),
    _SwACLPktContRuleVarOffsetData3_Type()
)
swACLPktContRuleVarOffsetData3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLPktContRuleVarOffsetData3.setStatus("current")


class _SwACLPktContRuleVarOffsetOffsetIndex4_Type(Integer32):
    """Custom type swACLPktContRuleVarOffsetOffsetIndex4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 76),
    )


_SwACLPktContRuleVarOffsetOffsetIndex4_Type.__name__ = "Integer32"
_SwACLPktContRuleVarOffsetOffsetIndex4_Object = MibTableColumn
swACLPktContRuleVarOffsetOffsetIndex4 = _SwACLPktContRuleVarOffsetOffsetIndex4_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 3, 9, 1, 17),
    _SwACLPktContRuleVarOffsetOffsetIndex4_Type()
)
swACLPktContRuleVarOffsetOffsetIndex4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLPktContRuleVarOffsetOffsetIndex4.setStatus("current")


class _SwACLPktContRuleVarOffsetMask4_Type(OctetString):
    """Custom type swACLPktContRuleVarOffsetMask4 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_SwACLPktContRuleVarOffsetMask4_Type.__name__ = "OctetString"
_SwACLPktContRuleVarOffsetMask4_Object = MibTableColumn
swACLPktContRuleVarOffsetMask4 = _SwACLPktContRuleVarOffsetMask4_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 3, 9, 1, 18),
    _SwACLPktContRuleVarOffsetMask4_Type()
)
swACLPktContRuleVarOffsetMask4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swACLPktContRuleVarOffsetMask4.setStatus("current")


class _SwACLPktContRuleVarOffsetData4_Type(OctetString):
    """Custom type swACLPktContRuleVarOffsetData4 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_SwACLPktContRuleVarOffsetData4_Type.__name__ = "OctetString"
_SwACLPktContRuleVarOffsetData4_Object = MibTableColumn
swACLPktContRuleVarOffsetData4 = _SwACLPktContRuleVarOffsetData4_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 3, 9, 1, 19),
    _SwACLPktContRuleVarOffsetData4_Type()
)
swACLPktContRuleVarOffsetData4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLPktContRuleVarOffsetData4.setStatus("current")


class _SwACLPktContRuleVarOffsetOffsetIndex5_Type(Integer32):
    """Custom type swACLPktContRuleVarOffsetOffsetIndex5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 76),
    )


_SwACLPktContRuleVarOffsetOffsetIndex5_Type.__name__ = "Integer32"
_SwACLPktContRuleVarOffsetOffsetIndex5_Object = MibTableColumn
swACLPktContRuleVarOffsetOffsetIndex5 = _SwACLPktContRuleVarOffsetOffsetIndex5_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 3, 9, 1, 20),
    _SwACLPktContRuleVarOffsetOffsetIndex5_Type()
)
swACLPktContRuleVarOffsetOffsetIndex5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLPktContRuleVarOffsetOffsetIndex5.setStatus("current")


class _SwACLPktContRuleVarOffsetMask5_Type(OctetString):
    """Custom type swACLPktContRuleVarOffsetMask5 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_SwACLPktContRuleVarOffsetMask5_Type.__name__ = "OctetString"
_SwACLPktContRuleVarOffsetMask5_Object = MibTableColumn
swACLPktContRuleVarOffsetMask5 = _SwACLPktContRuleVarOffsetMask5_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 3, 9, 1, 21),
    _SwACLPktContRuleVarOffsetMask5_Type()
)
swACLPktContRuleVarOffsetMask5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swACLPktContRuleVarOffsetMask5.setStatus("current")


class _SwACLPktContRuleVarOffsetData5_Type(OctetString):
    """Custom type swACLPktContRuleVarOffsetData5 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_SwACLPktContRuleVarOffsetData5_Type.__name__ = "OctetString"
_SwACLPktContRuleVarOffsetData5_Object = MibTableColumn
swACLPktContRuleVarOffsetData5 = _SwACLPktContRuleVarOffsetData5_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 3, 9, 1, 22),
    _SwACLPktContRuleVarOffsetData5_Type()
)
swACLPktContRuleVarOffsetData5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLPktContRuleVarOffsetData5.setStatus("current")


class _SwACLPktContRuleVarOffsetEnablePriority_Type(Integer32):
    """Custom type swACLPktContRuleVarOffsetEnablePriority based on Integer32"""
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


_SwACLPktContRuleVarOffsetEnablePriority_Type.__name__ = "Integer32"
_SwACLPktContRuleVarOffsetEnablePriority_Object = MibTableColumn
swACLPktContRuleVarOffsetEnablePriority = _SwACLPktContRuleVarOffsetEnablePriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 3, 9, 1, 23),
    _SwACLPktContRuleVarOffsetEnablePriority_Type()
)
swACLPktContRuleVarOffsetEnablePriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLPktContRuleVarOffsetEnablePriority.setStatus("current")


class _SwACLPktContRuleVarOffsetPriority_Type(Integer32):
    """Custom type swACLPktContRuleVarOffsetPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_SwACLPktContRuleVarOffsetPriority_Type.__name__ = "Integer32"
_SwACLPktContRuleVarOffsetPriority_Object = MibTableColumn
swACLPktContRuleVarOffsetPriority = _SwACLPktContRuleVarOffsetPriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 3, 9, 1, 24),
    _SwACLPktContRuleVarOffsetPriority_Type()
)
swACLPktContRuleVarOffsetPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLPktContRuleVarOffsetPriority.setStatus("current")


class _SwACLPktContRuleVarOffsetReplacePriority_Type(Integer32):
    """Custom type swACLPktContRuleVarOffsetReplacePriority based on Integer32"""
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


_SwACLPktContRuleVarOffsetReplacePriority_Type.__name__ = "Integer32"
_SwACLPktContRuleVarOffsetReplacePriority_Object = MibTableColumn
swACLPktContRuleVarOffsetReplacePriority = _SwACLPktContRuleVarOffsetReplacePriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 3, 9, 1, 25),
    _SwACLPktContRuleVarOffsetReplacePriority_Type()
)
swACLPktContRuleVarOffsetReplacePriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLPktContRuleVarOffsetReplacePriority.setStatus("current")


class _SwACLPktContRuleVarOffsetRxRate_Type(Integer32):
    """Custom type swACLPktContRuleVarOffsetRxRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 1024000),
    )


_SwACLPktContRuleVarOffsetRxRate_Type.__name__ = "Integer32"
_SwACLPktContRuleVarOffsetRxRate_Object = MibTableColumn
swACLPktContRuleVarOffsetRxRate = _SwACLPktContRuleVarOffsetRxRate_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 3, 9, 1, 28),
    _SwACLPktContRuleVarOffsetRxRate_Type()
)
swACLPktContRuleVarOffsetRxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swACLPktContRuleVarOffsetRxRate.setStatus("current")


class _SwACLPktContRuleVarOffsetPermit_Type(Integer32):
    """Custom type swACLPktContRuleVarOffsetPermit based on Integer32"""
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


_SwACLPktContRuleVarOffsetPermit_Type.__name__ = "Integer32"
_SwACLPktContRuleVarOffsetPermit_Object = MibTableColumn
swACLPktContRuleVarOffsetPermit = _SwACLPktContRuleVarOffsetPermit_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 3, 9, 1, 29),
    _SwACLPktContRuleVarOffsetPermit_Type()
)
swACLPktContRuleVarOffsetPermit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLPktContRuleVarOffsetPermit.setStatus("current")
_SwACLPktContRuleVarOffsetPort_Type = PortList
_SwACLPktContRuleVarOffsetPort_Object = MibTableColumn
swACLPktContRuleVarOffsetPort = _SwACLPktContRuleVarOffsetPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 3, 9, 1, 30),
    _SwACLPktContRuleVarOffsetPort_Type()
)
swACLPktContRuleVarOffsetPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLPktContRuleVarOffsetPort.setStatus("current")
_SwACLPktContRuleVarOffsetRowStatus_Type = RowStatus
_SwACLPktContRuleVarOffsetRowStatus_Object = MibTableColumn
swACLPktContRuleVarOffsetRowStatus = _SwACLPktContRuleVarOffsetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 3, 9, 1, 33),
    _SwACLPktContRuleVarOffsetRowStatus_Type()
)
swACLPktContRuleVarOffsetRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLPktContRuleVarOffsetRowStatus.setStatus("current")


class _SwACLPktContRuleVarOffsetReplacePriorityWith_Type(Integer32):
    """Custom type swACLPktContRuleVarOffsetReplacePriorityWith based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_SwACLPktContRuleVarOffsetReplacePriorityWith_Type.__name__ = "Integer32"
_SwACLPktContRuleVarOffsetReplacePriorityWith_Object = MibTableColumn
swACLPktContRuleVarOffsetReplacePriorityWith = _SwACLPktContRuleVarOffsetReplacePriorityWith_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 3, 9, 1, 34),
    _SwACLPktContRuleVarOffsetReplacePriorityWith_Type()
)
swACLPktContRuleVarOffsetReplacePriorityWith.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swACLPktContRuleVarOffsetReplacePriorityWith.setStatus("current")
_SwCpuAclMaskMgmt_ObjectIdentity = ObjectIdentity
swCpuAclMaskMgmt = _SwCpuAclMaskMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 4)
)
_SwCpuAclEthernetTable_Object = MibTable
swCpuAclEthernetTable = _SwCpuAclEthernetTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 4, 1)
)
if mibBuilder.loadTexts:
    swCpuAclEthernetTable.setStatus("current")
_SwCpuAclEthernetEntry_Object = MibTableRow
swCpuAclEthernetEntry = _SwCpuAclEthernetEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 4, 1, 1)
)
swCpuAclEthernetEntry.setIndexNames(
    (0, "ACLMGMT-MIB", "swCpuAclEthernetProfileID"),
)
if mibBuilder.loadTexts:
    swCpuAclEthernetEntry.setStatus("current")
_SwCpuAclEthernetProfileID_Type = Integer32
_SwCpuAclEthernetProfileID_Object = MibTableColumn
swCpuAclEthernetProfileID = _SwCpuAclEthernetProfileID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 4, 1, 1, 1),
    _SwCpuAclEthernetProfileID_Type()
)
swCpuAclEthernetProfileID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swCpuAclEthernetProfileID.setStatus("current")


class _SwCpuAclEthernetUsevlan_Type(Integer32):
    """Custom type swCpuAclEthernetUsevlan based on Integer32"""
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


_SwCpuAclEthernetUsevlan_Type.__name__ = "Integer32"
_SwCpuAclEthernetUsevlan_Object = MibTableColumn
swCpuAclEthernetUsevlan = _SwCpuAclEthernetUsevlan_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 4, 1, 1, 2),
    _SwCpuAclEthernetUsevlan_Type()
)
swCpuAclEthernetUsevlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swCpuAclEthernetUsevlan.setStatus("current")


class _SwCpuAclEthernetMacAddrMaskState_Type(Integer32):
    """Custom type swCpuAclEthernetMacAddrMaskState based on Integer32"""
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


_SwCpuAclEthernetMacAddrMaskState_Type.__name__ = "Integer32"
_SwCpuAclEthernetMacAddrMaskState_Object = MibTableColumn
swCpuAclEthernetMacAddrMaskState = _SwCpuAclEthernetMacAddrMaskState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 4, 1, 1, 3),
    _SwCpuAclEthernetMacAddrMaskState_Type()
)
swCpuAclEthernetMacAddrMaskState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swCpuAclEthernetMacAddrMaskState.setStatus("current")
_SwCpuAclEthernetSrcMacAddrMask_Type = MacAddress
_SwCpuAclEthernetSrcMacAddrMask_Object = MibTableColumn
swCpuAclEthernetSrcMacAddrMask = _SwCpuAclEthernetSrcMacAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 4, 1, 1, 4),
    _SwCpuAclEthernetSrcMacAddrMask_Type()
)
swCpuAclEthernetSrcMacAddrMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swCpuAclEthernetSrcMacAddrMask.setStatus("current")
_SwCpuAclEthernetDstMacAddrMask_Type = MacAddress
_SwCpuAclEthernetDstMacAddrMask_Object = MibTableColumn
swCpuAclEthernetDstMacAddrMask = _SwCpuAclEthernetDstMacAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 4, 1, 1, 5),
    _SwCpuAclEthernetDstMacAddrMask_Type()
)
swCpuAclEthernetDstMacAddrMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swCpuAclEthernetDstMacAddrMask.setStatus("current")


class _SwCpuAclEthernetUse8021p_Type(Integer32):
    """Custom type swCpuAclEthernetUse8021p based on Integer32"""
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


_SwCpuAclEthernetUse8021p_Type.__name__ = "Integer32"
_SwCpuAclEthernetUse8021p_Object = MibTableColumn
swCpuAclEthernetUse8021p = _SwCpuAclEthernetUse8021p_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 4, 1, 1, 6),
    _SwCpuAclEthernetUse8021p_Type()
)
swCpuAclEthernetUse8021p.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swCpuAclEthernetUse8021p.setStatus("current")


class _SwCpuAclEthernetUseEthernetType_Type(Integer32):
    """Custom type swCpuAclEthernetUseEthernetType based on Integer32"""
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


_SwCpuAclEthernetUseEthernetType_Type.__name__ = "Integer32"
_SwCpuAclEthernetUseEthernetType_Object = MibTableColumn
swCpuAclEthernetUseEthernetType = _SwCpuAclEthernetUseEthernetType_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 4, 1, 1, 7),
    _SwCpuAclEthernetUseEthernetType_Type()
)
swCpuAclEthernetUseEthernetType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swCpuAclEthernetUseEthernetType.setStatus("current")
_SwCpuAclEthernetRowStatus_Type = RowStatus
_SwCpuAclEthernetRowStatus_Object = MibTableColumn
swCpuAclEthernetRowStatus = _SwCpuAclEthernetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 4, 1, 1, 8),
    _SwCpuAclEthernetRowStatus_Type()
)
swCpuAclEthernetRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swCpuAclEthernetRowStatus.setStatus("current")
_SwCpuAclIpTable_Object = MibTable
swCpuAclIpTable = _SwCpuAclIpTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 4, 2)
)
if mibBuilder.loadTexts:
    swCpuAclIpTable.setStatus("current")
_SwCpuAclIpEntry_Object = MibTableRow
swCpuAclIpEntry = _SwCpuAclIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 4, 2, 1)
)
swCpuAclIpEntry.setIndexNames(
    (0, "ACLMGMT-MIB", "swCpuAclIpProfileID"),
)
if mibBuilder.loadTexts:
    swCpuAclIpEntry.setStatus("current")
_SwCpuAclIpProfileID_Type = Integer32
_SwCpuAclIpProfileID_Object = MibTableColumn
swCpuAclIpProfileID = _SwCpuAclIpProfileID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 4, 2, 1, 1),
    _SwCpuAclIpProfileID_Type()
)
swCpuAclIpProfileID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swCpuAclIpProfileID.setStatus("current")


class _SwCpuAclIpUsevlan_Type(Integer32):
    """Custom type swCpuAclIpUsevlan based on Integer32"""
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


_SwCpuAclIpUsevlan_Type.__name__ = "Integer32"
_SwCpuAclIpUsevlan_Object = MibTableColumn
swCpuAclIpUsevlan = _SwCpuAclIpUsevlan_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 4, 2, 1, 2),
    _SwCpuAclIpUsevlan_Type()
)
swCpuAclIpUsevlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swCpuAclIpUsevlan.setStatus("current")


class _SwCpuAclIpIpAddrMaskState_Type(Integer32):
    """Custom type swCpuAclIpIpAddrMaskState based on Integer32"""
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


_SwCpuAclIpIpAddrMaskState_Type.__name__ = "Integer32"
_SwCpuAclIpIpAddrMaskState_Object = MibTableColumn
swCpuAclIpIpAddrMaskState = _SwCpuAclIpIpAddrMaskState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 4, 2, 1, 3),
    _SwCpuAclIpIpAddrMaskState_Type()
)
swCpuAclIpIpAddrMaskState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swCpuAclIpIpAddrMaskState.setStatus("current")
_SwCpuAclIpSrcIpAddrMask_Type = IpAddress
_SwCpuAclIpSrcIpAddrMask_Object = MibTableColumn
swCpuAclIpSrcIpAddrMask = _SwCpuAclIpSrcIpAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 4, 2, 1, 4),
    _SwCpuAclIpSrcIpAddrMask_Type()
)
swCpuAclIpSrcIpAddrMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swCpuAclIpSrcIpAddrMask.setStatus("current")
_SwCpuAclIpDstIpAddrMask_Type = IpAddress
_SwCpuAclIpDstIpAddrMask_Object = MibTableColumn
swCpuAclIpDstIpAddrMask = _SwCpuAclIpDstIpAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 4, 2, 1, 5),
    _SwCpuAclIpDstIpAddrMask_Type()
)
swCpuAclIpDstIpAddrMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swCpuAclIpDstIpAddrMask.setStatus("current")


class _SwCpuAclIpUseDSCP_Type(Integer32):
    """Custom type swCpuAclIpUseDSCP based on Integer32"""
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


_SwCpuAclIpUseDSCP_Type.__name__ = "Integer32"
_SwCpuAclIpUseDSCP_Object = MibTableColumn
swCpuAclIpUseDSCP = _SwCpuAclIpUseDSCP_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 4, 2, 1, 6),
    _SwCpuAclIpUseDSCP_Type()
)
swCpuAclIpUseDSCP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swCpuAclIpUseDSCP.setStatus("current")


class _SwCpuAclIpUseProtoType_Type(Integer32):
    """Custom type swCpuAclIpUseProtoType based on Integer32"""
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


_SwCpuAclIpUseProtoType_Type.__name__ = "Integer32"
_SwCpuAclIpUseProtoType_Object = MibTableColumn
swCpuAclIpUseProtoType = _SwCpuAclIpUseProtoType_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 4, 2, 1, 7),
    _SwCpuAclIpUseProtoType_Type()
)
swCpuAclIpUseProtoType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swCpuAclIpUseProtoType.setStatus("current")


class _SwCpuAclIpIcmpOption_Type(Integer32):
    """Custom type swCpuAclIpIcmpOption based on Integer32"""
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


_SwCpuAclIpIcmpOption_Type.__name__ = "Integer32"
_SwCpuAclIpIcmpOption_Object = MibTableColumn
swCpuAclIpIcmpOption = _SwCpuAclIpIcmpOption_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 4, 2, 1, 8),
    _SwCpuAclIpIcmpOption_Type()
)
swCpuAclIpIcmpOption.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swCpuAclIpIcmpOption.setStatus("current")


class _SwCpuAclIpIgmpOption_Type(Integer32):
    """Custom type swCpuAclIpIgmpOption based on Integer32"""
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


_SwCpuAclIpIgmpOption_Type.__name__ = "Integer32"
_SwCpuAclIpIgmpOption_Object = MibTableColumn
swCpuAclIpIgmpOption = _SwCpuAclIpIgmpOption_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 4, 2, 1, 9),
    _SwCpuAclIpIgmpOption_Type()
)
swCpuAclIpIgmpOption.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swCpuAclIpIgmpOption.setStatus("current")


class _SwCpuAclIpTcpOption_Type(Integer32):
    """Custom type swCpuAclIpTcpOption based on Integer32"""
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


_SwCpuAclIpTcpOption_Type.__name__ = "Integer32"
_SwCpuAclIpTcpOption_Object = MibTableColumn
swCpuAclIpTcpOption = _SwCpuAclIpTcpOption_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 4, 2, 1, 10),
    _SwCpuAclIpTcpOption_Type()
)
swCpuAclIpTcpOption.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swCpuAclIpTcpOption.setStatus("current")


class _SwCpuAclIpUdpOption_Type(Integer32):
    """Custom type swCpuAclIpUdpOption based on Integer32"""
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


_SwCpuAclIpUdpOption_Type.__name__ = "Integer32"
_SwCpuAclIpUdpOption_Object = MibTableColumn
swCpuAclIpUdpOption = _SwCpuAclIpUdpOption_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 4, 2, 1, 11),
    _SwCpuAclIpUdpOption_Type()
)
swCpuAclIpUdpOption.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swCpuAclIpUdpOption.setStatus("current")


class _SwCpuAclIpTCPorUDPSrcPortMask_Type(OctetString):
    """Custom type swCpuAclIpTCPorUDPSrcPortMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_SwCpuAclIpTCPorUDPSrcPortMask_Type.__name__ = "OctetString"
_SwCpuAclIpTCPorUDPSrcPortMask_Object = MibTableColumn
swCpuAclIpTCPorUDPSrcPortMask = _SwCpuAclIpTCPorUDPSrcPortMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 4, 2, 1, 12),
    _SwCpuAclIpTCPorUDPSrcPortMask_Type()
)
swCpuAclIpTCPorUDPSrcPortMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swCpuAclIpTCPorUDPSrcPortMask.setStatus("current")


class _SwCpuAclIpTCPorUDPDstPortMask_Type(OctetString):
    """Custom type swCpuAclIpTCPorUDPDstPortMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_SwCpuAclIpTCPorUDPDstPortMask_Type.__name__ = "OctetString"
_SwCpuAclIpTCPorUDPDstPortMask_Object = MibTableColumn
swCpuAclIpTCPorUDPDstPortMask = _SwCpuAclIpTCPorUDPDstPortMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 4, 2, 1, 13),
    _SwCpuAclIpTCPorUDPDstPortMask_Type()
)
swCpuAclIpTCPorUDPDstPortMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swCpuAclIpTCPorUDPDstPortMask.setStatus("current")


class _SwCpuAclIpTCPFlagBit_Type(Integer32):
    """Custom type swCpuAclIpTCPFlagBit based on Integer32"""
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


_SwCpuAclIpTCPFlagBit_Type.__name__ = "Integer32"
_SwCpuAclIpTCPFlagBit_Object = MibTableColumn
swCpuAclIpTCPFlagBit = _SwCpuAclIpTCPFlagBit_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 4, 2, 1, 14),
    _SwCpuAclIpTCPFlagBit_Type()
)
swCpuAclIpTCPFlagBit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swCpuAclIpTCPFlagBit.setStatus("current")


class _SwCpuAclIpTCPFlagBitMask_Type(Integer32):
    """Custom type swCpuAclIpTCPFlagBitMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_SwCpuAclIpTCPFlagBitMask_Type.__name__ = "Integer32"
_SwCpuAclIpTCPFlagBitMask_Object = MibTableColumn
swCpuAclIpTCPFlagBitMask = _SwCpuAclIpTCPFlagBitMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 4, 2, 1, 15),
    _SwCpuAclIpTCPFlagBitMask_Type()
)
swCpuAclIpTCPFlagBitMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swCpuAclIpTCPFlagBitMask.setStatus("current")


class _SwCpuAclIpProtoIDOption_Type(Integer32):
    """Custom type swCpuAclIpProtoIDOption based on Integer32"""
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


_SwCpuAclIpProtoIDOption_Type.__name__ = "Integer32"
_SwCpuAclIpProtoIDOption_Object = MibTableColumn
swCpuAclIpProtoIDOption = _SwCpuAclIpProtoIDOption_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 4, 2, 1, 16),
    _SwCpuAclIpProtoIDOption_Type()
)
swCpuAclIpProtoIDOption.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swCpuAclIpProtoIDOption.setStatus("current")


class _SwCpuAclIpProtoID_Type(Integer32):
    """Custom type swCpuAclIpProtoID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SwCpuAclIpProtoID_Type.__name__ = "Integer32"
_SwCpuAclIpProtoID_Object = MibTableColumn
swCpuAclIpProtoID = _SwCpuAclIpProtoID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 4, 2, 1, 17),
    _SwCpuAclIpProtoID_Type()
)
swCpuAclIpProtoID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swCpuAclIpProtoID.setStatus("current")


class _SwCpuAclIpProtoIDMask_Type(OctetString):
    """Custom type swCpuAclIpProtoIDMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_SwCpuAclIpProtoIDMask_Type.__name__ = "OctetString"
_SwCpuAclIpProtoIDMask_Object = MibTableColumn
swCpuAclIpProtoIDMask = _SwCpuAclIpProtoIDMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 4, 2, 1, 18),
    _SwCpuAclIpProtoIDMask_Type()
)
swCpuAclIpProtoIDMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swCpuAclIpProtoIDMask.setStatus("current")
_SwCpuAclIpRowStatus_Type = RowStatus
_SwCpuAclIpRowStatus_Object = MibTableColumn
swCpuAclIpRowStatus = _SwCpuAclIpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 4, 2, 1, 19),
    _SwCpuAclIpRowStatus_Type()
)
swCpuAclIpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swCpuAclIpRowStatus.setStatus("current")
_SwCpuAclPktContMaskTable_Object = MibTable
swCpuAclPktContMaskTable = _SwCpuAclPktContMaskTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 4, 3)
)
if mibBuilder.loadTexts:
    swCpuAclPktContMaskTable.setStatus("current")
_SwCpuAclPktContMaskEntry_Object = MibTableRow
swCpuAclPktContMaskEntry = _SwCpuAclPktContMaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 4, 3, 1)
)
swCpuAclPktContMaskEntry.setIndexNames(
    (0, "ACLMGMT-MIB", "swCpuAclPktContMaskProfileID"),
)
if mibBuilder.loadTexts:
    swCpuAclPktContMaskEntry.setStatus("current")
_SwCpuAclPktContMaskProfileID_Type = Integer32
_SwCpuAclPktContMaskProfileID_Object = MibTableColumn
swCpuAclPktContMaskProfileID = _SwCpuAclPktContMaskProfileID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 4, 3, 1, 1),
    _SwCpuAclPktContMaskProfileID_Type()
)
swCpuAclPktContMaskProfileID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swCpuAclPktContMaskProfileID.setStatus("current")


class _SwCpuAclPktContMaskOffset0to15_Type(OctetString):
    """Custom type swCpuAclPktContMaskOffset0to15 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_SwCpuAclPktContMaskOffset0to15_Type.__name__ = "OctetString"
_SwCpuAclPktContMaskOffset0to15_Object = MibTableColumn
swCpuAclPktContMaskOffset0to15 = _SwCpuAclPktContMaskOffset0to15_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 4, 3, 1, 2),
    _SwCpuAclPktContMaskOffset0to15_Type()
)
swCpuAclPktContMaskOffset0to15.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swCpuAclPktContMaskOffset0to15.setStatus("current")


class _SwCpuAclPktContMaskOffset16to31_Type(OctetString):
    """Custom type swCpuAclPktContMaskOffset16to31 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_SwCpuAclPktContMaskOffset16to31_Type.__name__ = "OctetString"
_SwCpuAclPktContMaskOffset16to31_Object = MibTableColumn
swCpuAclPktContMaskOffset16to31 = _SwCpuAclPktContMaskOffset16to31_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 4, 3, 1, 3),
    _SwCpuAclPktContMaskOffset16to31_Type()
)
swCpuAclPktContMaskOffset16to31.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swCpuAclPktContMaskOffset16to31.setStatus("current")


class _SwCpuAclPktContMaskOffset32to47_Type(OctetString):
    """Custom type swCpuAclPktContMaskOffset32to47 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_SwCpuAclPktContMaskOffset32to47_Type.__name__ = "OctetString"
_SwCpuAclPktContMaskOffset32to47_Object = MibTableColumn
swCpuAclPktContMaskOffset32to47 = _SwCpuAclPktContMaskOffset32to47_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 4, 3, 1, 4),
    _SwCpuAclPktContMaskOffset32to47_Type()
)
swCpuAclPktContMaskOffset32to47.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swCpuAclPktContMaskOffset32to47.setStatus("current")


class _SwCpuAclPktContMaskOffset48to63_Type(OctetString):
    """Custom type swCpuAclPktContMaskOffset48to63 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_SwCpuAclPktContMaskOffset48to63_Type.__name__ = "OctetString"
_SwCpuAclPktContMaskOffset48to63_Object = MibTableColumn
swCpuAclPktContMaskOffset48to63 = _SwCpuAclPktContMaskOffset48to63_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 4, 3, 1, 5),
    _SwCpuAclPktContMaskOffset48to63_Type()
)
swCpuAclPktContMaskOffset48to63.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swCpuAclPktContMaskOffset48to63.setStatus("current")


class _SwCpuAclPktContMaskOffset64to79_Type(OctetString):
    """Custom type swCpuAclPktContMaskOffset64to79 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_SwCpuAclPktContMaskOffset64to79_Type.__name__ = "OctetString"
_SwCpuAclPktContMaskOffset64to79_Object = MibTableColumn
swCpuAclPktContMaskOffset64to79 = _SwCpuAclPktContMaskOffset64to79_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 4, 3, 1, 6),
    _SwCpuAclPktContMaskOffset64to79_Type()
)
swCpuAclPktContMaskOffset64to79.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swCpuAclPktContMaskOffset64to79.setStatus("current")
_SwCpuAclPktContMaskRowStatus_Type = RowStatus
_SwCpuAclPktContMaskRowStatus_Object = MibTableColumn
swCpuAclPktContMaskRowStatus = _SwCpuAclPktContMaskRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 4, 3, 1, 7),
    _SwCpuAclPktContMaskRowStatus_Type()
)
swCpuAclPktContMaskRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swCpuAclPktContMaskRowStatus.setStatus("current")
_SwCpuAclIpv6MaskTable_Object = MibTable
swCpuAclIpv6MaskTable = _SwCpuAclIpv6MaskTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 4, 4)
)
if mibBuilder.loadTexts:
    swCpuAclIpv6MaskTable.setStatus("current")
_SwCpuAclIpv6MaskEntry_Object = MibTableRow
swCpuAclIpv6MaskEntry = _SwCpuAclIpv6MaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 4, 4, 1)
)
swCpuAclIpv6MaskEntry.setIndexNames(
    (0, "ACLMGMT-MIB", "swCpuAclIpv6MaskProfileID"),
)
if mibBuilder.loadTexts:
    swCpuAclIpv6MaskEntry.setStatus("current")
_SwCpuAclIpv6MaskProfileID_Type = Integer32
_SwCpuAclIpv6MaskProfileID_Object = MibTableColumn
swCpuAclIpv6MaskProfileID = _SwCpuAclIpv6MaskProfileID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 4, 4, 1, 1),
    _SwCpuAclIpv6MaskProfileID_Type()
)
swCpuAclIpv6MaskProfileID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swCpuAclIpv6MaskProfileID.setStatus("current")


class _SwCpuAclIpv6MaskClass_Type(Integer32):
    """Custom type swCpuAclIpv6MaskClass based on Integer32"""
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


_SwCpuAclIpv6MaskClass_Type.__name__ = "Integer32"
_SwCpuAclIpv6MaskClass_Object = MibTableColumn
swCpuAclIpv6MaskClass = _SwCpuAclIpv6MaskClass_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 4, 4, 1, 2),
    _SwCpuAclIpv6MaskClass_Type()
)
swCpuAclIpv6MaskClass.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swCpuAclIpv6MaskClass.setStatus("current")


class _SwCpuAclIpv6MaskFlowlabel_Type(Integer32):
    """Custom type swCpuAclIpv6MaskFlowlabel based on Integer32"""
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


_SwCpuAclIpv6MaskFlowlabel_Type.__name__ = "Integer32"
_SwCpuAclIpv6MaskFlowlabel_Object = MibTableColumn
swCpuAclIpv6MaskFlowlabel = _SwCpuAclIpv6MaskFlowlabel_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 4, 4, 1, 3),
    _SwCpuAclIpv6MaskFlowlabel_Type()
)
swCpuAclIpv6MaskFlowlabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swCpuAclIpv6MaskFlowlabel.setStatus("current")


class _SwCpuAclIpv6IpAddrMaskState_Type(Integer32):
    """Custom type swCpuAclIpv6IpAddrMaskState based on Integer32"""
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
        *(("dst-ipv6-addr", 2),
          ("dst-src-ipv6-addr", 4),
          ("other", 1),
          ("src-ipv6-addr", 3))
    )


_SwCpuAclIpv6IpAddrMaskState_Type.__name__ = "Integer32"
_SwCpuAclIpv6IpAddrMaskState_Object = MibTableColumn
swCpuAclIpv6IpAddrMaskState = _SwCpuAclIpv6IpAddrMaskState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 4, 4, 1, 4),
    _SwCpuAclIpv6IpAddrMaskState_Type()
)
swCpuAclIpv6IpAddrMaskState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swCpuAclIpv6IpAddrMaskState.setStatus("current")
_SwCpuAclIpv6MaskSrcIpv6Mask_Type = Ipv6Address
_SwCpuAclIpv6MaskSrcIpv6Mask_Object = MibTableColumn
swCpuAclIpv6MaskSrcIpv6Mask = _SwCpuAclIpv6MaskSrcIpv6Mask_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 4, 4, 1, 5),
    _SwCpuAclIpv6MaskSrcIpv6Mask_Type()
)
swCpuAclIpv6MaskSrcIpv6Mask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swCpuAclIpv6MaskSrcIpv6Mask.setStatus("current")
_SwCpuAclIpv6MaskDstIpv6Mask_Type = Ipv6Address
_SwCpuAclIpv6MaskDstIpv6Mask_Object = MibTableColumn
swCpuAclIpv6MaskDstIpv6Mask = _SwCpuAclIpv6MaskDstIpv6Mask_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 4, 4, 1, 6),
    _SwCpuAclIpv6MaskDstIpv6Mask_Type()
)
swCpuAclIpv6MaskDstIpv6Mask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swCpuAclIpv6MaskDstIpv6Mask.setStatus("current")
_SwCpuAclIpv6MaskRowStatus_Type = RowStatus
_SwCpuAclIpv6MaskRowStatus_Object = MibTableColumn
swCpuAclIpv6MaskRowStatus = _SwCpuAclIpv6MaskRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 4, 4, 1, 7),
    _SwCpuAclIpv6MaskRowStatus_Type()
)
swCpuAclIpv6MaskRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swCpuAclIpv6MaskRowStatus.setStatus("current")


class _SwCpuACLMaskDelAllState_Type(Integer32):
    """Custom type swCpuACLMaskDelAllState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("start", 2))
    )


_SwCpuACLMaskDelAllState_Type.__name__ = "Integer32"
_SwCpuACLMaskDelAllState_Object = MibScalar
swCpuACLMaskDelAllState = _SwCpuACLMaskDelAllState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 4, 5),
    _SwCpuACLMaskDelAllState_Type()
)
swCpuACLMaskDelAllState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swCpuACLMaskDelAllState.setStatus("current")
_SwCpuAclRuleMgmt_ObjectIdentity = ObjectIdentity
swCpuAclRuleMgmt = _SwCpuAclRuleMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 5)
)
_SwCpuAclEtherRuleTable_Object = MibTable
swCpuAclEtherRuleTable = _SwCpuAclEtherRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 5, 1)
)
if mibBuilder.loadTexts:
    swCpuAclEtherRuleTable.setStatus("current")
_SwCpuAclEtherRuleEntry_Object = MibTableRow
swCpuAclEtherRuleEntry = _SwCpuAclEtherRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 5, 1, 1)
)
swCpuAclEtherRuleEntry.setIndexNames(
    (0, "ACLMGMT-MIB", "swCpuAclEtherRuleProfileID"),
    (0, "ACLMGMT-MIB", "swCpuAclEtherRuleAccessID"),
)
if mibBuilder.loadTexts:
    swCpuAclEtherRuleEntry.setStatus("current")
_SwCpuAclEtherRuleProfileID_Type = Integer32
_SwCpuAclEtherRuleProfileID_Object = MibTableColumn
swCpuAclEtherRuleProfileID = _SwCpuAclEtherRuleProfileID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 5, 1, 1, 1),
    _SwCpuAclEtherRuleProfileID_Type()
)
swCpuAclEtherRuleProfileID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swCpuAclEtherRuleProfileID.setStatus("current")


class _SwCpuAclEtherRuleAccessID_Type(Integer32):
    """Custom type swCpuAclEtherRuleAccessID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SwCpuAclEtherRuleAccessID_Type.__name__ = "Integer32"
_SwCpuAclEtherRuleAccessID_Object = MibTableColumn
swCpuAclEtherRuleAccessID = _SwCpuAclEtherRuleAccessID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 5, 1, 1, 2),
    _SwCpuAclEtherRuleAccessID_Type()
)
swCpuAclEtherRuleAccessID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swCpuAclEtherRuleAccessID.setStatus("current")


class _SwCpuAclEtherRuleVlan_Type(SnmpAdminString):
    """Custom type swCpuAclEtherRuleVlan based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SwCpuAclEtherRuleVlan_Type.__name__ = "SnmpAdminString"
_SwCpuAclEtherRuleVlan_Object = MibTableColumn
swCpuAclEtherRuleVlan = _SwCpuAclEtherRuleVlan_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 5, 1, 1, 3),
    _SwCpuAclEtherRuleVlan_Type()
)
swCpuAclEtherRuleVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swCpuAclEtherRuleVlan.setStatus("current")
_SwCpuAclEtherRuleSrcMacAddress_Type = MacAddress
_SwCpuAclEtherRuleSrcMacAddress_Object = MibTableColumn
swCpuAclEtherRuleSrcMacAddress = _SwCpuAclEtherRuleSrcMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 5, 1, 1, 4),
    _SwCpuAclEtherRuleSrcMacAddress_Type()
)
swCpuAclEtherRuleSrcMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swCpuAclEtherRuleSrcMacAddress.setStatus("current")
_SwCpuAclEtherRuleDstMacAddress_Type = MacAddress
_SwCpuAclEtherRuleDstMacAddress_Object = MibTableColumn
swCpuAclEtherRuleDstMacAddress = _SwCpuAclEtherRuleDstMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 5, 1, 1, 5),
    _SwCpuAclEtherRuleDstMacAddress_Type()
)
swCpuAclEtherRuleDstMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swCpuAclEtherRuleDstMacAddress.setStatus("current")


class _SwCpuAclEtherRule8021P_Type(Integer32):
    """Custom type swCpuAclEtherRule8021P based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 7),
    )


_SwCpuAclEtherRule8021P_Type.__name__ = "Integer32"
_SwCpuAclEtherRule8021P_Object = MibTableColumn
swCpuAclEtherRule8021P = _SwCpuAclEtherRule8021P_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 5, 1, 1, 6),
    _SwCpuAclEtherRule8021P_Type()
)
swCpuAclEtherRule8021P.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swCpuAclEtherRule8021P.setStatus("current")


class _SwCpuAclEtherRuleEtherType_Type(OctetString):
    """Custom type swCpuAclEtherRuleEtherType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_SwCpuAclEtherRuleEtherType_Type.__name__ = "OctetString"
_SwCpuAclEtherRuleEtherType_Object = MibTableColumn
swCpuAclEtherRuleEtherType = _SwCpuAclEtherRuleEtherType_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 5, 1, 1, 7),
    _SwCpuAclEtherRuleEtherType_Type()
)
swCpuAclEtherRuleEtherType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swCpuAclEtherRuleEtherType.setStatus("current")


class _SwCpuAclEtherRulePermit_Type(Integer32):
    """Custom type swCpuAclEtherRulePermit based on Integer32"""
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


_SwCpuAclEtherRulePermit_Type.__name__ = "Integer32"
_SwCpuAclEtherRulePermit_Object = MibTableColumn
swCpuAclEtherRulePermit = _SwCpuAclEtherRulePermit_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 5, 1, 1, 8),
    _SwCpuAclEtherRulePermit_Type()
)
swCpuAclEtherRulePermit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swCpuAclEtherRulePermit.setStatus("current")
_SwCpuAclEtherRuleRowStatus_Type = RowStatus
_SwCpuAclEtherRuleRowStatus_Object = MibTableColumn
swCpuAclEtherRuleRowStatus = _SwCpuAclEtherRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 5, 1, 1, 9),
    _SwCpuAclEtherRuleRowStatus_Type()
)
swCpuAclEtherRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swCpuAclEtherRuleRowStatus.setStatus("current")
_SwCpuAclEtherRulePort_Type = PortList
_SwCpuAclEtherRulePort_Object = MibTableColumn
swCpuAclEtherRulePort = _SwCpuAclEtherRulePort_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 5, 1, 1, 10),
    _SwCpuAclEtherRulePort_Type()
)
swCpuAclEtherRulePort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swCpuAclEtherRulePort.setStatus("current")
_SwCpuAclIpRuleTable_Object = MibTable
swCpuAclIpRuleTable = _SwCpuAclIpRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 5, 2)
)
if mibBuilder.loadTexts:
    swCpuAclIpRuleTable.setStatus("current")
_SwCpuAclIpRuleEntry_Object = MibTableRow
swCpuAclIpRuleEntry = _SwCpuAclIpRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 5, 2, 1)
)
swCpuAclIpRuleEntry.setIndexNames(
    (0, "ACLMGMT-MIB", "swCpuAclIpRuleProfileID"),
    (0, "ACLMGMT-MIB", "swCpuAclIpRuleAccessID"),
)
if mibBuilder.loadTexts:
    swCpuAclIpRuleEntry.setStatus("current")
_SwCpuAclIpRuleProfileID_Type = Integer32
_SwCpuAclIpRuleProfileID_Object = MibTableColumn
swCpuAclIpRuleProfileID = _SwCpuAclIpRuleProfileID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 5, 2, 1, 1),
    _SwCpuAclIpRuleProfileID_Type()
)
swCpuAclIpRuleProfileID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swCpuAclIpRuleProfileID.setStatus("current")


class _SwCpuAclIpRuleAccessID_Type(Integer32):
    """Custom type swCpuAclIpRuleAccessID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SwCpuAclIpRuleAccessID_Type.__name__ = "Integer32"
_SwCpuAclIpRuleAccessID_Object = MibTableColumn
swCpuAclIpRuleAccessID = _SwCpuAclIpRuleAccessID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 5, 2, 1, 2),
    _SwCpuAclIpRuleAccessID_Type()
)
swCpuAclIpRuleAccessID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swCpuAclIpRuleAccessID.setStatus("current")


class _SwCpuAclIpRuleVlan_Type(SnmpAdminString):
    """Custom type swCpuAclIpRuleVlan based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SwCpuAclIpRuleVlan_Type.__name__ = "SnmpAdminString"
_SwCpuAclIpRuleVlan_Object = MibTableColumn
swCpuAclIpRuleVlan = _SwCpuAclIpRuleVlan_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 5, 2, 1, 3),
    _SwCpuAclIpRuleVlan_Type()
)
swCpuAclIpRuleVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swCpuAclIpRuleVlan.setStatus("current")
_SwCpuAclIpRuleSrcIpaddress_Type = IpAddress
_SwCpuAclIpRuleSrcIpaddress_Object = MibTableColumn
swCpuAclIpRuleSrcIpaddress = _SwCpuAclIpRuleSrcIpaddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 5, 2, 1, 4),
    _SwCpuAclIpRuleSrcIpaddress_Type()
)
swCpuAclIpRuleSrcIpaddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swCpuAclIpRuleSrcIpaddress.setStatus("current")
_SwCpuAclIpRuleDstIpaddress_Type = IpAddress
_SwCpuAclIpRuleDstIpaddress_Object = MibTableColumn
swCpuAclIpRuleDstIpaddress = _SwCpuAclIpRuleDstIpaddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 5, 2, 1, 5),
    _SwCpuAclIpRuleDstIpaddress_Type()
)
swCpuAclIpRuleDstIpaddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swCpuAclIpRuleDstIpaddress.setStatus("current")


class _SwCpuAclIpRuleDscp_Type(Integer32):
    """Custom type swCpuAclIpRuleDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 63),
    )


_SwCpuAclIpRuleDscp_Type.__name__ = "Integer32"
_SwCpuAclIpRuleDscp_Object = MibTableColumn
swCpuAclIpRuleDscp = _SwCpuAclIpRuleDscp_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 5, 2, 1, 6),
    _SwCpuAclIpRuleDscp_Type()
)
swCpuAclIpRuleDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swCpuAclIpRuleDscp.setStatus("current")


class _SwCpuAclIpRuleProtocol_Type(Integer32):
    """Custom type swCpuAclIpRuleProtocol based on Integer32"""
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


_SwCpuAclIpRuleProtocol_Type.__name__ = "Integer32"
_SwCpuAclIpRuleProtocol_Object = MibTableColumn
swCpuAclIpRuleProtocol = _SwCpuAclIpRuleProtocol_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 5, 2, 1, 7),
    _SwCpuAclIpRuleProtocol_Type()
)
swCpuAclIpRuleProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swCpuAclIpRuleProtocol.setStatus("current")


class _SwCpuAclIpRuleType_Type(Integer32):
    """Custom type swCpuAclIpRuleType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 255),
    )


_SwCpuAclIpRuleType_Type.__name__ = "Integer32"
_SwCpuAclIpRuleType_Object = MibTableColumn
swCpuAclIpRuleType = _SwCpuAclIpRuleType_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 5, 2, 1, 8),
    _SwCpuAclIpRuleType_Type()
)
swCpuAclIpRuleType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swCpuAclIpRuleType.setStatus("current")


class _SwCpuAclIpRuleCode_Type(Integer32):
    """Custom type swCpuAclIpRuleCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 255),
    )


_SwCpuAclIpRuleCode_Type.__name__ = "Integer32"
_SwCpuAclIpRuleCode_Object = MibTableColumn
swCpuAclIpRuleCode = _SwCpuAclIpRuleCode_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 5, 2, 1, 9),
    _SwCpuAclIpRuleCode_Type()
)
swCpuAclIpRuleCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swCpuAclIpRuleCode.setStatus("current")


class _SwCpuAclIpRuleSrcPort_Type(Integer32):
    """Custom type swCpuAclIpRuleSrcPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_SwCpuAclIpRuleSrcPort_Type.__name__ = "Integer32"
_SwCpuAclIpRuleSrcPort_Object = MibTableColumn
swCpuAclIpRuleSrcPort = _SwCpuAclIpRuleSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 5, 2, 1, 10),
    _SwCpuAclIpRuleSrcPort_Type()
)
swCpuAclIpRuleSrcPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swCpuAclIpRuleSrcPort.setStatus("current")


class _SwCpuAclIpRuleDstPort_Type(Integer32):
    """Custom type swCpuAclIpRuleDstPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_SwCpuAclIpRuleDstPort_Type.__name__ = "Integer32"
_SwCpuAclIpRuleDstPort_Object = MibTableColumn
swCpuAclIpRuleDstPort = _SwCpuAclIpRuleDstPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 5, 2, 1, 11),
    _SwCpuAclIpRuleDstPort_Type()
)
swCpuAclIpRuleDstPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swCpuAclIpRuleDstPort.setStatus("current")


class _SwCpuAclIpRuleFlagBits_Type(Integer32):
    """Custom type swCpuAclIpRuleFlagBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_SwCpuAclIpRuleFlagBits_Type.__name__ = "Integer32"
_SwCpuAclIpRuleFlagBits_Object = MibTableColumn
swCpuAclIpRuleFlagBits = _SwCpuAclIpRuleFlagBits_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 5, 2, 1, 12),
    _SwCpuAclIpRuleFlagBits_Type()
)
swCpuAclIpRuleFlagBits.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swCpuAclIpRuleFlagBits.setStatus("current")


class _SwCpuAclIpRuleProtoID_Type(Integer32):
    """Custom type swCpuAclIpRuleProtoID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 255),
    )


_SwCpuAclIpRuleProtoID_Type.__name__ = "Integer32"
_SwCpuAclIpRuleProtoID_Object = MibTableColumn
swCpuAclIpRuleProtoID = _SwCpuAclIpRuleProtoID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 5, 2, 1, 13),
    _SwCpuAclIpRuleProtoID_Type()
)
swCpuAclIpRuleProtoID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swCpuAclIpRuleProtoID.setStatus("current")


class _SwCpuAclIpRuleUserMask_Type(OctetString):
    """Custom type swCpuAclIpRuleUserMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_SwCpuAclIpRuleUserMask_Type.__name__ = "OctetString"
_SwCpuAclIpRuleUserMask_Object = MibTableColumn
swCpuAclIpRuleUserMask = _SwCpuAclIpRuleUserMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 5, 2, 1, 14),
    _SwCpuAclIpRuleUserMask_Type()
)
swCpuAclIpRuleUserMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swCpuAclIpRuleUserMask.setStatus("current")


class _SwCpuAclIpRulePermit_Type(Integer32):
    """Custom type swCpuAclIpRulePermit based on Integer32"""
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


_SwCpuAclIpRulePermit_Type.__name__ = "Integer32"
_SwCpuAclIpRulePermit_Object = MibTableColumn
swCpuAclIpRulePermit = _SwCpuAclIpRulePermit_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 5, 2, 1, 15),
    _SwCpuAclIpRulePermit_Type()
)
swCpuAclIpRulePermit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swCpuAclIpRulePermit.setStatus("current")
_SwCpuAclIpRuleRowStatus_Type = RowStatus
_SwCpuAclIpRuleRowStatus_Object = MibTableColumn
swCpuAclIpRuleRowStatus = _SwCpuAclIpRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 5, 2, 1, 16),
    _SwCpuAclIpRuleRowStatus_Type()
)
swCpuAclIpRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swCpuAclIpRuleRowStatus.setStatus("current")
_SwCpuAclIpRulePort_Type = PortList
_SwCpuAclIpRulePort_Object = MibTableColumn
swCpuAclIpRulePort = _SwCpuAclIpRulePort_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 5, 2, 1, 17),
    _SwCpuAclIpRulePort_Type()
)
swCpuAclIpRulePort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swCpuAclIpRulePort.setStatus("current")
_SwCpuAclPktContRuleTable_Object = MibTable
swCpuAclPktContRuleTable = _SwCpuAclPktContRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 5, 3)
)
if mibBuilder.loadTexts:
    swCpuAclPktContRuleTable.setStatus("current")
_SwCpuAclPktContRuleEntry_Object = MibTableRow
swCpuAclPktContRuleEntry = _SwCpuAclPktContRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 5, 3, 1)
)
swCpuAclPktContRuleEntry.setIndexNames(
    (0, "ACLMGMT-MIB", "swCpuAclPktContRuleProfileID"),
    (0, "ACLMGMT-MIB", "swCpuAclPktContRuleAccessID"),
)
if mibBuilder.loadTexts:
    swCpuAclPktContRuleEntry.setStatus("current")
_SwCpuAclPktContRuleProfileID_Type = Integer32
_SwCpuAclPktContRuleProfileID_Object = MibTableColumn
swCpuAclPktContRuleProfileID = _SwCpuAclPktContRuleProfileID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 5, 3, 1, 1),
    _SwCpuAclPktContRuleProfileID_Type()
)
swCpuAclPktContRuleProfileID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swCpuAclPktContRuleProfileID.setStatus("current")


class _SwCpuAclPktContRuleAccessID_Type(Integer32):
    """Custom type swCpuAclPktContRuleAccessID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SwCpuAclPktContRuleAccessID_Type.__name__ = "Integer32"
_SwCpuAclPktContRuleAccessID_Object = MibTableColumn
swCpuAclPktContRuleAccessID = _SwCpuAclPktContRuleAccessID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 5, 3, 1, 2),
    _SwCpuAclPktContRuleAccessID_Type()
)
swCpuAclPktContRuleAccessID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swCpuAclPktContRuleAccessID.setStatus("current")


class _SwCpuAclPktContRuleOffset0to15_Type(OctetString):
    """Custom type swCpuAclPktContRuleOffset0to15 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_SwCpuAclPktContRuleOffset0to15_Type.__name__ = "OctetString"
_SwCpuAclPktContRuleOffset0to15_Object = MibTableColumn
swCpuAclPktContRuleOffset0to15 = _SwCpuAclPktContRuleOffset0to15_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 5, 3, 1, 3),
    _SwCpuAclPktContRuleOffset0to15_Type()
)
swCpuAclPktContRuleOffset0to15.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swCpuAclPktContRuleOffset0to15.setStatus("current")


class _SwCpuAclPktContRuleOffset16to31_Type(OctetString):
    """Custom type swCpuAclPktContRuleOffset16to31 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_SwCpuAclPktContRuleOffset16to31_Type.__name__ = "OctetString"
_SwCpuAclPktContRuleOffset16to31_Object = MibTableColumn
swCpuAclPktContRuleOffset16to31 = _SwCpuAclPktContRuleOffset16to31_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 5, 3, 1, 4),
    _SwCpuAclPktContRuleOffset16to31_Type()
)
swCpuAclPktContRuleOffset16to31.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swCpuAclPktContRuleOffset16to31.setStatus("current")


class _SwCpuAclPktContRuleOffset32to47_Type(OctetString):
    """Custom type swCpuAclPktContRuleOffset32to47 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_SwCpuAclPktContRuleOffset32to47_Type.__name__ = "OctetString"
_SwCpuAclPktContRuleOffset32to47_Object = MibTableColumn
swCpuAclPktContRuleOffset32to47 = _SwCpuAclPktContRuleOffset32to47_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 5, 3, 1, 5),
    _SwCpuAclPktContRuleOffset32to47_Type()
)
swCpuAclPktContRuleOffset32to47.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swCpuAclPktContRuleOffset32to47.setStatus("current")


class _SwCpuAclPktContRuleOffset48to63_Type(OctetString):
    """Custom type swCpuAclPktContRuleOffset48to63 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_SwCpuAclPktContRuleOffset48to63_Type.__name__ = "OctetString"
_SwCpuAclPktContRuleOffset48to63_Object = MibTableColumn
swCpuAclPktContRuleOffset48to63 = _SwCpuAclPktContRuleOffset48to63_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 5, 3, 1, 6),
    _SwCpuAclPktContRuleOffset48to63_Type()
)
swCpuAclPktContRuleOffset48to63.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swCpuAclPktContRuleOffset48to63.setStatus("current")


class _SwCpuAclPktContRuleOffset64to79_Type(OctetString):
    """Custom type swCpuAclPktContRuleOffset64to79 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_SwCpuAclPktContRuleOffset64to79_Type.__name__ = "OctetString"
_SwCpuAclPktContRuleOffset64to79_Object = MibTableColumn
swCpuAclPktContRuleOffset64to79 = _SwCpuAclPktContRuleOffset64to79_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 5, 3, 1, 7),
    _SwCpuAclPktContRuleOffset64to79_Type()
)
swCpuAclPktContRuleOffset64to79.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swCpuAclPktContRuleOffset64to79.setStatus("current")


class _SwCpuAclPktContRulePermit_Type(Integer32):
    """Custom type swCpuAclPktContRulePermit based on Integer32"""
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


_SwCpuAclPktContRulePermit_Type.__name__ = "Integer32"
_SwCpuAclPktContRulePermit_Object = MibTableColumn
swCpuAclPktContRulePermit = _SwCpuAclPktContRulePermit_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 5, 3, 1, 8),
    _SwCpuAclPktContRulePermit_Type()
)
swCpuAclPktContRulePermit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swCpuAclPktContRulePermit.setStatus("current")
_SwCpuAclPktContRuleRowStatus_Type = RowStatus
_SwCpuAclPktContRuleRowStatus_Object = MibTableColumn
swCpuAclPktContRuleRowStatus = _SwCpuAclPktContRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 5, 3, 1, 9),
    _SwCpuAclPktContRuleRowStatus_Type()
)
swCpuAclPktContRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swCpuAclPktContRuleRowStatus.setStatus("current")
_SwCpuAclPktContRulePort_Type = PortList
_SwCpuAclPktContRulePort_Object = MibTableColumn
swCpuAclPktContRulePort = _SwCpuAclPktContRulePort_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 5, 3, 1, 10),
    _SwCpuAclPktContRulePort_Type()
)
swCpuAclPktContRulePort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swCpuAclPktContRulePort.setStatus("current")
_SwCpuAclIpv6RuleTable_Object = MibTable
swCpuAclIpv6RuleTable = _SwCpuAclIpv6RuleTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 5, 4)
)
if mibBuilder.loadTexts:
    swCpuAclIpv6RuleTable.setStatus("current")
_SwCpuAclIpv6RuleEntry_Object = MibTableRow
swCpuAclIpv6RuleEntry = _SwCpuAclIpv6RuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 5, 4, 1)
)
swCpuAclIpv6RuleEntry.setIndexNames(
    (0, "ACLMGMT-MIB", "swCpuAclIpv6RuleProfileID"),
    (0, "ACLMGMT-MIB", "swCpuAclIpv6RuleAccessID"),
)
if mibBuilder.loadTexts:
    swCpuAclIpv6RuleEntry.setStatus("current")
_SwCpuAclIpv6RuleProfileID_Type = Integer32
_SwCpuAclIpv6RuleProfileID_Object = MibTableColumn
swCpuAclIpv6RuleProfileID = _SwCpuAclIpv6RuleProfileID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 5, 4, 1, 1),
    _SwCpuAclIpv6RuleProfileID_Type()
)
swCpuAclIpv6RuleProfileID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swCpuAclIpv6RuleProfileID.setStatus("current")


class _SwCpuAclIpv6RuleAccessID_Type(Integer32):
    """Custom type swCpuAclIpv6RuleAccessID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SwCpuAclIpv6RuleAccessID_Type.__name__ = "Integer32"
_SwCpuAclIpv6RuleAccessID_Object = MibTableColumn
swCpuAclIpv6RuleAccessID = _SwCpuAclIpv6RuleAccessID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 5, 4, 1, 2),
    _SwCpuAclIpv6RuleAccessID_Type()
)
swCpuAclIpv6RuleAccessID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swCpuAclIpv6RuleAccessID.setStatus("current")


class _SwCpuAclIpv6RuleClass_Type(Integer32):
    """Custom type swCpuAclIpv6RuleClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SwCpuAclIpv6RuleClass_Type.__name__ = "Integer32"
_SwCpuAclIpv6RuleClass_Object = MibTableColumn
swCpuAclIpv6RuleClass = _SwCpuAclIpv6RuleClass_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 5, 4, 1, 3),
    _SwCpuAclIpv6RuleClass_Type()
)
swCpuAclIpv6RuleClass.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swCpuAclIpv6RuleClass.setStatus("current")


class _SwCpuAclIpv6RuleFlowlabel_Type(OctetString):
    """Custom type swCpuAclIpv6RuleFlowlabel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_SwCpuAclIpv6RuleFlowlabel_Type.__name__ = "OctetString"
_SwCpuAclIpv6RuleFlowlabel_Object = MibTableColumn
swCpuAclIpv6RuleFlowlabel = _SwCpuAclIpv6RuleFlowlabel_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 5, 4, 1, 4),
    _SwCpuAclIpv6RuleFlowlabel_Type()
)
swCpuAclIpv6RuleFlowlabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swCpuAclIpv6RuleFlowlabel.setStatus("current")
_SwCpuAclIpv6RuleSrcIpv6Addr_Type = Ipv6Address
_SwCpuAclIpv6RuleSrcIpv6Addr_Object = MibTableColumn
swCpuAclIpv6RuleSrcIpv6Addr = _SwCpuAclIpv6RuleSrcIpv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 5, 4, 1, 5),
    _SwCpuAclIpv6RuleSrcIpv6Addr_Type()
)
swCpuAclIpv6RuleSrcIpv6Addr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swCpuAclIpv6RuleSrcIpv6Addr.setStatus("current")
_SwCpuAclIpv6RuleDstIpv6Addr_Type = Ipv6Address
_SwCpuAclIpv6RuleDstIpv6Addr_Object = MibTableColumn
swCpuAclIpv6RuleDstIpv6Addr = _SwCpuAclIpv6RuleDstIpv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 5, 4, 1, 6),
    _SwCpuAclIpv6RuleDstIpv6Addr_Type()
)
swCpuAclIpv6RuleDstIpv6Addr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swCpuAclIpv6RuleDstIpv6Addr.setStatus("current")


class _SwCpuAclIpv6RulePermit_Type(Integer32):
    """Custom type swCpuAclIpv6RulePermit based on Integer32"""
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


_SwCpuAclIpv6RulePermit_Type.__name__ = "Integer32"
_SwCpuAclIpv6RulePermit_Object = MibTableColumn
swCpuAclIpv6RulePermit = _SwCpuAclIpv6RulePermit_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 5, 4, 1, 7),
    _SwCpuAclIpv6RulePermit_Type()
)
swCpuAclIpv6RulePermit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swCpuAclIpv6RulePermit.setStatus("current")
_SwCpuAclIpv6RuleRowStatus_Type = RowStatus
_SwCpuAclIpv6RuleRowStatus_Object = MibTableColumn
swCpuAclIpv6RuleRowStatus = _SwCpuAclIpv6RuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 5, 4, 1, 8),
    _SwCpuAclIpv6RuleRowStatus_Type()
)
swCpuAclIpv6RuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swCpuAclIpv6RuleRowStatus.setStatus("current")
_SwCpuAclIpv6RulePort_Type = PortList
_SwCpuAclIpv6RulePort_Object = MibTableColumn
swCpuAclIpv6RulePort = _SwCpuAclIpv6RulePort_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 5, 4, 1, 9),
    _SwCpuAclIpv6RulePort_Type()
)
swCpuAclIpv6RulePort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swCpuAclIpv6RulePort.setStatus("current")
_SwAclMeteringMgmt_ObjectIdentity = ObjectIdentity
swAclMeteringMgmt = _SwAclMeteringMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 6)
)
_SwAclMeterTable_Object = MibTable
swAclMeterTable = _SwAclMeterTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 6, 1)
)
if mibBuilder.loadTexts:
    swAclMeterTable.setStatus("current")
_SwAclMeterEntry_Object = MibTableRow
swAclMeterEntry = _SwAclMeterEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 6, 1, 1)
)
swAclMeterEntry.setIndexNames(
    (0, "ACLMGMT-MIB", "swAclMeterProfileID"),
    (0, "ACLMGMT-MIB", "swAclMeterAccessID"),
)
if mibBuilder.loadTexts:
    swAclMeterEntry.setStatus("current")
_SwAclMeterProfileID_Type = Integer32
_SwAclMeterProfileID_Object = MibTableColumn
swAclMeterProfileID = _SwAclMeterProfileID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 6, 1, 1, 1),
    _SwAclMeterProfileID_Type()
)
swAclMeterProfileID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAclMeterProfileID.setStatus("current")


class _SwAclMeterAccessID_Type(Integer32):
    """Custom type swAclMeterAccessID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SwAclMeterAccessID_Type.__name__ = "Integer32"
_SwAclMeterAccessID_Object = MibTableColumn
swAclMeterAccessID = _SwAclMeterAccessID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 6, 1, 1, 2),
    _SwAclMeterAccessID_Type()
)
swAclMeterAccessID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAclMeterAccessID.setStatus("current")
_SwAclMeterRate_Type = Integer32
_SwAclMeterRate_Object = MibTableColumn
swAclMeterRate = _SwAclMeterRate_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 6, 1, 1, 3),
    _SwAclMeterRate_Type()
)
swAclMeterRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swAclMeterRate.setStatus("current")


class _SwAclMeterActionForRateExceed_Type(Integer32):
    """Custom type swAclMeterActionForRateExceed based on Integer32"""
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
        *(("drop-packet", 2),
          ("other", 1),
          ("remark-dscp", 4),
          ("set-drop-precedence", 3))
    )


_SwAclMeterActionForRateExceed_Type.__name__ = "Integer32"
_SwAclMeterActionForRateExceed_Object = MibTableColumn
swAclMeterActionForRateExceed = _SwAclMeterActionForRateExceed_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 6, 1, 1, 4),
    _SwAclMeterActionForRateExceed_Type()
)
swAclMeterActionForRateExceed.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swAclMeterActionForRateExceed.setStatus("current")


class _SwAclMeterRemarkDscp_Type(Integer32):
    """Custom type swAclMeterRemarkDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_SwAclMeterRemarkDscp_Type.__name__ = "Integer32"
_SwAclMeterRemarkDscp_Object = MibTableColumn
swAclMeterRemarkDscp = _SwAclMeterRemarkDscp_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 6, 1, 1, 5),
    _SwAclMeterRemarkDscp_Type()
)
swAclMeterRemarkDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swAclMeterRemarkDscp.setStatus("current")
_SwAclMeterBurstSize_Type = Integer32
_SwAclMeterBurstSize_Object = MibTableColumn
swAclMeterBurstSize = _SwAclMeterBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 6, 1, 1, 6),
    _SwAclMeterBurstSize_Type()
)
swAclMeterBurstSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swAclMeterBurstSize.setStatus("current")


class _SwAclMeterMode_Type(Integer32):
    """Custom type swAclMeterMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("sr-tcm", 3),
          ("tr-tcm", 2))
    )


_SwAclMeterMode_Type.__name__ = "Integer32"
_SwAclMeterMode_Object = MibTableColumn
swAclMeterMode = _SwAclMeterMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 6, 1, 1, 7),
    _SwAclMeterMode_Type()
)
swAclMeterMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swAclMeterMode.setStatus("current")


class _SwAclMeterTrtcmCir_Type(Integer32):
    """Custom type swAclMeterTrtcmCir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 156249),
    )


_SwAclMeterTrtcmCir_Type.__name__ = "Integer32"
_SwAclMeterTrtcmCir_Object = MibTableColumn
swAclMeterTrtcmCir = _SwAclMeterTrtcmCir_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 6, 1, 1, 8),
    _SwAclMeterTrtcmCir_Type()
)
swAclMeterTrtcmCir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swAclMeterTrtcmCir.setStatus("current")


class _SwAclMeterTrtcmCbs_Type(Integer32):
    """Custom type swAclMeterTrtcmCbs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16384),
    )


_SwAclMeterTrtcmCbs_Type.__name__ = "Integer32"
_SwAclMeterTrtcmCbs_Object = MibTableColumn
swAclMeterTrtcmCbs = _SwAclMeterTrtcmCbs_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 6, 1, 1, 9),
    _SwAclMeterTrtcmCbs_Type()
)
swAclMeterTrtcmCbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swAclMeterTrtcmCbs.setStatus("current")


class _SwAclMeterTrtcmPir_Type(Integer32):
    """Custom type swAclMeterTrtcmPir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 156249),
    )


_SwAclMeterTrtcmPir_Type.__name__ = "Integer32"
_SwAclMeterTrtcmPir_Object = MibTableColumn
swAclMeterTrtcmPir = _SwAclMeterTrtcmPir_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 6, 1, 1, 10),
    _SwAclMeterTrtcmPir_Type()
)
swAclMeterTrtcmPir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swAclMeterTrtcmPir.setStatus("current")


class _SwAclMeterTrtcmPbs_Type(Integer32):
    """Custom type swAclMeterTrtcmPbs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16384),
    )


_SwAclMeterTrtcmPbs_Type.__name__ = "Integer32"
_SwAclMeterTrtcmPbs_Object = MibTableColumn
swAclMeterTrtcmPbs = _SwAclMeterTrtcmPbs_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 6, 1, 1, 11),
    _SwAclMeterTrtcmPbs_Type()
)
swAclMeterTrtcmPbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swAclMeterTrtcmPbs.setStatus("current")


class _SwAclMeterTrtcmColorMode_Type(Integer32):
    """Custom type swAclMeterTrtcmColorMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("color-aware", 2),
          ("color-blind", 1))
    )


_SwAclMeterTrtcmColorMode_Type.__name__ = "Integer32"
_SwAclMeterTrtcmColorMode_Object = MibTableColumn
swAclMeterTrtcmColorMode = _SwAclMeterTrtcmColorMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 6, 1, 1, 12),
    _SwAclMeterTrtcmColorMode_Type()
)
swAclMeterTrtcmColorMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swAclMeterTrtcmColorMode.setStatus("current")


class _SwAclMeterTrtcmConformState_Type(Integer32):
    """Custom type swAclMeterTrtcmConformState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("permit", 2),
          ("replace-dscp", 3))
    )


_SwAclMeterTrtcmConformState_Type.__name__ = "Integer32"
_SwAclMeterTrtcmConformState_Object = MibTableColumn
swAclMeterTrtcmConformState = _SwAclMeterTrtcmConformState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 6, 1, 1, 13),
    _SwAclMeterTrtcmConformState_Type()
)
swAclMeterTrtcmConformState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swAclMeterTrtcmConformState.setStatus("current")


class _SwAclMeterTrtcmConformReplaceDscp_Type(Integer32):
    """Custom type swAclMeterTrtcmConformReplaceDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_SwAclMeterTrtcmConformReplaceDscp_Type.__name__ = "Integer32"
_SwAclMeterTrtcmConformReplaceDscp_Object = MibTableColumn
swAclMeterTrtcmConformReplaceDscp = _SwAclMeterTrtcmConformReplaceDscp_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 6, 1, 1, 14),
    _SwAclMeterTrtcmConformReplaceDscp_Type()
)
swAclMeterTrtcmConformReplaceDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swAclMeterTrtcmConformReplaceDscp.setStatus("current")


class _SwAclMeterTrtcmConformCounterState_Type(Integer32):
    """Custom type swAclMeterTrtcmConformCounterState based on Integer32"""
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


_SwAclMeterTrtcmConformCounterState_Type.__name__ = "Integer32"
_SwAclMeterTrtcmConformCounterState_Object = MibTableColumn
swAclMeterTrtcmConformCounterState = _SwAclMeterTrtcmConformCounterState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 6, 1, 1, 15),
    _SwAclMeterTrtcmConformCounterState_Type()
)
swAclMeterTrtcmConformCounterState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swAclMeterTrtcmConformCounterState.setStatus("current")


class _SwAclMeterTrtcmExceedState_Type(Integer32):
    """Custom type swAclMeterTrtcmExceedState based on Integer32"""
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
        *(("drop", 4),
          ("other", 1),
          ("permit", 2),
          ("replace-dscp", 3))
    )


_SwAclMeterTrtcmExceedState_Type.__name__ = "Integer32"
_SwAclMeterTrtcmExceedState_Object = MibTableColumn
swAclMeterTrtcmExceedState = _SwAclMeterTrtcmExceedState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 6, 1, 1, 16),
    _SwAclMeterTrtcmExceedState_Type()
)
swAclMeterTrtcmExceedState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swAclMeterTrtcmExceedState.setStatus("current")


class _SwAclMeterTrtcmExceedReplaceDscp_Type(Integer32):
    """Custom type swAclMeterTrtcmExceedReplaceDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_SwAclMeterTrtcmExceedReplaceDscp_Type.__name__ = "Integer32"
_SwAclMeterTrtcmExceedReplaceDscp_Object = MibTableColumn
swAclMeterTrtcmExceedReplaceDscp = _SwAclMeterTrtcmExceedReplaceDscp_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 6, 1, 1, 17),
    _SwAclMeterTrtcmExceedReplaceDscp_Type()
)
swAclMeterTrtcmExceedReplaceDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swAclMeterTrtcmExceedReplaceDscp.setStatus("current")


class _SwAclMeterTrtcmExceedCounterState_Type(Integer32):
    """Custom type swAclMeterTrtcmExceedCounterState based on Integer32"""
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


_SwAclMeterTrtcmExceedCounterState_Type.__name__ = "Integer32"
_SwAclMeterTrtcmExceedCounterState_Object = MibTableColumn
swAclMeterTrtcmExceedCounterState = _SwAclMeterTrtcmExceedCounterState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 6, 1, 1, 18),
    _SwAclMeterTrtcmExceedCounterState_Type()
)
swAclMeterTrtcmExceedCounterState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swAclMeterTrtcmExceedCounterState.setStatus("current")


class _SwAclMeterTrtcmViolateState_Type(Integer32):
    """Custom type swAclMeterTrtcmViolateState based on Integer32"""
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
        *(("drop", 4),
          ("other", 1),
          ("permit", 2),
          ("replace-dscp", 3))
    )


_SwAclMeterTrtcmViolateState_Type.__name__ = "Integer32"
_SwAclMeterTrtcmViolateState_Object = MibTableColumn
swAclMeterTrtcmViolateState = _SwAclMeterTrtcmViolateState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 6, 1, 1, 19),
    _SwAclMeterTrtcmViolateState_Type()
)
swAclMeterTrtcmViolateState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swAclMeterTrtcmViolateState.setStatus("current")


class _SwAclMeterTrtcmViolateReplaceDscp_Type(Integer32):
    """Custom type swAclMeterTrtcmViolateReplaceDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_SwAclMeterTrtcmViolateReplaceDscp_Type.__name__ = "Integer32"
_SwAclMeterTrtcmViolateReplaceDscp_Object = MibTableColumn
swAclMeterTrtcmViolateReplaceDscp = _SwAclMeterTrtcmViolateReplaceDscp_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 6, 1, 1, 20),
    _SwAclMeterTrtcmViolateReplaceDscp_Type()
)
swAclMeterTrtcmViolateReplaceDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swAclMeterTrtcmViolateReplaceDscp.setStatus("current")


class _SwAclMeterTrtcmViolateCounterState_Type(Integer32):
    """Custom type swAclMeterTrtcmViolateCounterState based on Integer32"""
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


_SwAclMeterTrtcmViolateCounterState_Type.__name__ = "Integer32"
_SwAclMeterTrtcmViolateCounterState_Object = MibTableColumn
swAclMeterTrtcmViolateCounterState = _SwAclMeterTrtcmViolateCounterState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 6, 1, 1, 21),
    _SwAclMeterTrtcmViolateCounterState_Type()
)
swAclMeterTrtcmViolateCounterState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swAclMeterTrtcmViolateCounterState.setStatus("current")


class _SwAclMeterSrtcmCir_Type(Integer32):
    """Custom type swAclMeterSrtcmCir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 156249),
    )


_SwAclMeterSrtcmCir_Type.__name__ = "Integer32"
_SwAclMeterSrtcmCir_Object = MibTableColumn
swAclMeterSrtcmCir = _SwAclMeterSrtcmCir_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 6, 1, 1, 22),
    _SwAclMeterSrtcmCir_Type()
)
swAclMeterSrtcmCir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swAclMeterSrtcmCir.setStatus("current")


class _SwAclMeterSrtcmCbs_Type(Integer32):
    """Custom type swAclMeterSrtcmCbs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16384),
    )


_SwAclMeterSrtcmCbs_Type.__name__ = "Integer32"
_SwAclMeterSrtcmCbs_Object = MibTableColumn
swAclMeterSrtcmCbs = _SwAclMeterSrtcmCbs_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 6, 1, 1, 23),
    _SwAclMeterSrtcmCbs_Type()
)
swAclMeterSrtcmCbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swAclMeterSrtcmCbs.setStatus("current")


class _SwAclMeterSrtcmEbs_Type(Integer32):
    """Custom type swAclMeterSrtcmEbs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16384),
    )


_SwAclMeterSrtcmEbs_Type.__name__ = "Integer32"
_SwAclMeterSrtcmEbs_Object = MibTableColumn
swAclMeterSrtcmEbs = _SwAclMeterSrtcmEbs_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 6, 1, 1, 24),
    _SwAclMeterSrtcmEbs_Type()
)
swAclMeterSrtcmEbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swAclMeterSrtcmEbs.setStatus("current")


class _SwAclMeterSrtcmColorMode_Type(Integer32):
    """Custom type swAclMeterSrtcmColorMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("color-aware", 2),
          ("color-blind", 1))
    )


_SwAclMeterSrtcmColorMode_Type.__name__ = "Integer32"
_SwAclMeterSrtcmColorMode_Object = MibTableColumn
swAclMeterSrtcmColorMode = _SwAclMeterSrtcmColorMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 6, 1, 1, 25),
    _SwAclMeterSrtcmColorMode_Type()
)
swAclMeterSrtcmColorMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swAclMeterSrtcmColorMode.setStatus("current")


class _SwAclMeterSrtcmConformState_Type(Integer32):
    """Custom type swAclMeterSrtcmConformState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("permit", 2),
          ("replace-dscp", 3))
    )


_SwAclMeterSrtcmConformState_Type.__name__ = "Integer32"
_SwAclMeterSrtcmConformState_Object = MibTableColumn
swAclMeterSrtcmConformState = _SwAclMeterSrtcmConformState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 6, 1, 1, 26),
    _SwAclMeterSrtcmConformState_Type()
)
swAclMeterSrtcmConformState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swAclMeterSrtcmConformState.setStatus("current")


class _SwAclMeterSrtcmConformReplaceDscp_Type(Integer32):
    """Custom type swAclMeterSrtcmConformReplaceDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_SwAclMeterSrtcmConformReplaceDscp_Type.__name__ = "Integer32"
_SwAclMeterSrtcmConformReplaceDscp_Object = MibTableColumn
swAclMeterSrtcmConformReplaceDscp = _SwAclMeterSrtcmConformReplaceDscp_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 6, 1, 1, 27),
    _SwAclMeterSrtcmConformReplaceDscp_Type()
)
swAclMeterSrtcmConformReplaceDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swAclMeterSrtcmConformReplaceDscp.setStatus("current")


class _SwAclMeterSrtcmConformCounterState_Type(Integer32):
    """Custom type swAclMeterSrtcmConformCounterState based on Integer32"""
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


_SwAclMeterSrtcmConformCounterState_Type.__name__ = "Integer32"
_SwAclMeterSrtcmConformCounterState_Object = MibTableColumn
swAclMeterSrtcmConformCounterState = _SwAclMeterSrtcmConformCounterState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 6, 1, 1, 28),
    _SwAclMeterSrtcmConformCounterState_Type()
)
swAclMeterSrtcmConformCounterState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swAclMeterSrtcmConformCounterState.setStatus("current")


class _SwAclMeterSrtcmExceedState_Type(Integer32):
    """Custom type swAclMeterSrtcmExceedState based on Integer32"""
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
        *(("drop", 4),
          ("other", 1),
          ("permit", 2),
          ("replace-dscp", 3))
    )


_SwAclMeterSrtcmExceedState_Type.__name__ = "Integer32"
_SwAclMeterSrtcmExceedState_Object = MibTableColumn
swAclMeterSrtcmExceedState = _SwAclMeterSrtcmExceedState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 6, 1, 1, 29),
    _SwAclMeterSrtcmExceedState_Type()
)
swAclMeterSrtcmExceedState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swAclMeterSrtcmExceedState.setStatus("current")


class _SwAclMeterSrtcmExceedReplaceDscp_Type(Integer32):
    """Custom type swAclMeterSrtcmExceedReplaceDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_SwAclMeterSrtcmExceedReplaceDscp_Type.__name__ = "Integer32"
_SwAclMeterSrtcmExceedReplaceDscp_Object = MibTableColumn
swAclMeterSrtcmExceedReplaceDscp = _SwAclMeterSrtcmExceedReplaceDscp_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 6, 1, 1, 30),
    _SwAclMeterSrtcmExceedReplaceDscp_Type()
)
swAclMeterSrtcmExceedReplaceDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swAclMeterSrtcmExceedReplaceDscp.setStatus("current")


class _SwAclMeterSrtcmExceedCounterState_Type(Integer32):
    """Custom type swAclMeterSrtcmExceedCounterState based on Integer32"""
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


_SwAclMeterSrtcmExceedCounterState_Type.__name__ = "Integer32"
_SwAclMeterSrtcmExceedCounterState_Object = MibTableColumn
swAclMeterSrtcmExceedCounterState = _SwAclMeterSrtcmExceedCounterState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 6, 1, 1, 31),
    _SwAclMeterSrtcmExceedCounterState_Type()
)
swAclMeterSrtcmExceedCounterState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swAclMeterSrtcmExceedCounterState.setStatus("current")


class _SwAclMeterSrtcmViolateState_Type(Integer32):
    """Custom type swAclMeterSrtcmViolateState based on Integer32"""
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
        *(("drop", 4),
          ("other", 1),
          ("permit", 2),
          ("replace-dscp", 3))
    )


_SwAclMeterSrtcmViolateState_Type.__name__ = "Integer32"
_SwAclMeterSrtcmViolateState_Object = MibTableColumn
swAclMeterSrtcmViolateState = _SwAclMeterSrtcmViolateState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 6, 1, 1, 32),
    _SwAclMeterSrtcmViolateState_Type()
)
swAclMeterSrtcmViolateState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swAclMeterSrtcmViolateState.setStatus("current")


class _SwAclMeterSrtcmViolateReplaceDscp_Type(Integer32):
    """Custom type swAclMeterSrtcmViolateReplaceDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_SwAclMeterSrtcmViolateReplaceDscp_Type.__name__ = "Integer32"
_SwAclMeterSrtcmViolateReplaceDscp_Object = MibTableColumn
swAclMeterSrtcmViolateReplaceDscp = _SwAclMeterSrtcmViolateReplaceDscp_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 6, 1, 1, 33),
    _SwAclMeterSrtcmViolateReplaceDscp_Type()
)
swAclMeterSrtcmViolateReplaceDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swAclMeterSrtcmViolateReplaceDscp.setStatus("current")


class _SwAclMeterSrtcmViolateCounterState_Type(Integer32):
    """Custom type swAclMeterSrtcmViolateCounterState based on Integer32"""
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


_SwAclMeterSrtcmViolateCounterState_Type.__name__ = "Integer32"
_SwAclMeterSrtcmViolateCounterState_Object = MibTableColumn
swAclMeterSrtcmViolateCounterState = _SwAclMeterSrtcmViolateCounterState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 6, 1, 1, 34),
    _SwAclMeterSrtcmViolateCounterState_Type()
)
swAclMeterSrtcmViolateCounterState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swAclMeterSrtcmViolateCounterState.setStatus("current")
_SwAclMeterRowStatus_Type = RowStatus
_SwAclMeterRowStatus_Object = MibTableColumn
swAclMeterRowStatus = _SwAclMeterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 6, 1, 1, 35),
    _SwAclMeterRowStatus_Type()
)
swAclMeterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swAclMeterRowStatus.setStatus("current")
_SwAclMeteringNumOfEntryInUse_Type = Integer32
_SwAclMeteringNumOfEntryInUse_Object = MibScalar
swAclMeteringNumOfEntryInUse = _SwAclMeteringNumOfEntryInUse_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 9, 6, 2),
    _SwAclMeteringNumOfEntryInUse_Type()
)
swAclMeteringNumOfEntryInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAclMeteringNumOfEntryInUse.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ACLMGMT-MIB",
    **{"PortList": PortList,
       "Ipv6Address": Ipv6Address,
       "swAclMgmtMIB": swAclMgmtMIB,
       "swAclCtrl": swAclCtrl,
       "swCpuInterfacefilterState": swCpuInterfacefilterState,
       "swACLTotalUsedRuleEntries": swACLTotalUsedRuleEntries,
       "swACLTotalUnusedRuleEntries": swACLTotalUnusedRuleEntries,
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
       "swACLEthernetRowStatus": swACLEthernetRowStatus,
       "swACLEthernetOwner": swACLEthernetOwner,
       "swACLEthernetUnusedRuleEntries": swACLEthernetUnusedRuleEntries,
       "swACLEthernetProfileName": swACLEthernetProfileName,
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
       "swACLIpTCPFlagBitMask": swACLIpTCPFlagBitMask,
       "swACLIpProtoIDOption": swACLIpProtoIDOption,
       "swACLIpProtoID": swACLIpProtoID,
       "swACLIpProtoIDMask": swACLIpProtoIDMask,
       "swACLIpRowStatus": swACLIpRowStatus,
       "swACLIpOwner": swACLIpOwner,
       "swACLIpUnusedRuleEntries": swACLIpUnusedRuleEntries,
       "swACLIpProfileName": swACLIpProfileName,
       "swACLPktContMaskTable": swACLPktContMaskTable,
       "swACLPktContMaskEntry": swACLPktContMaskEntry,
       "swACLPktContMaskProfileID": swACLPktContMaskProfileID,
       "swACLPktContMaskOffset0to15": swACLPktContMaskOffset0to15,
       "swACLPktContMaskOffset16to31": swACLPktContMaskOffset16to31,
       "swACLPktContMaskOffset32to47": swACLPktContMaskOffset32to47,
       "swACLPktContMaskOffset48to63": swACLPktContMaskOffset48to63,
       "swACLPktContMaskOffset64to79": swACLPktContMaskOffset64to79,
       "swACLPktContMaskRowStatus": swACLPktContMaskRowStatus,
       "swACLPktContMaskOwner": swACLPktContMaskOwner,
       "swACLPktContMaskUnusedRuleEntries": swACLPktContMaskUnusedRuleEntries,
       "swACLPktContMaskProfileName": swACLPktContMaskProfileName,
       "swACLIpv6MaskTable": swACLIpv6MaskTable,
       "swACLIpv6MaskEntry": swACLIpv6MaskEntry,
       "swACLIpv6MaskProfileID": swACLIpv6MaskProfileID,
       "swACLIpv6MaskClass": swACLIpv6MaskClass,
       "swACLIpv6MaskFlowlabel": swACLIpv6MaskFlowlabel,
       "swACLIpv6IpAddrMaskState": swACLIpv6IpAddrMaskState,
       "swACLIpv6MaskSrcIpv6Mask": swACLIpv6MaskSrcIpv6Mask,
       "swACLIpv6MaskDstIpv6Mask": swACLIpv6MaskDstIpv6Mask,
       "swACLIpv6MaskRowStatus": swACLIpv6MaskRowStatus,
       "swACLIpv6MaskOwner": swACLIpv6MaskOwner,
       "swACLIpv6MaskUnusedRuleEntries": swACLIpv6MaskUnusedRuleEntries,
       "swACLIpv6MaskProfileName": swACLIpv6MaskProfileName,
       "swACLIpv6MaskUseProtoType": swACLIpv6MaskUseProtoType,
       "swACLIpv6MaskTcpOption": swACLIpv6MaskTcpOption,
       "swACLIpv6MaskUdpOption": swACLIpv6MaskUdpOption,
       "swACLIpv6MaskTCPorUDPSrcPortMask": swACLIpv6MaskTCPorUDPSrcPortMask,
       "swACLIpv6MaskTCPorUDPDstPortMask": swACLIpv6MaskTCPorUDPDstPortMask,
       "swACLMaskDelAllState": swACLMaskDelAllState,
       "swIBPACLEthernetTable": swIBPACLEthernetTable,
       "swIBPACLEthernetEntry": swIBPACLEthernetEntry,
       "swIBPACLEthernetProfileID": swIBPACLEthernetProfileID,
       "swIBPACLEthernetUseEthernetType": swIBPACLEthernetUseEthernetType,
       "swIBPACLIpTable": swIBPACLIpTable,
       "swIBPACLIpEntry": swIBPACLIpEntry,
       "swIBPACLIpProfileID": swIBPACLIpProfileID,
       "swIBPACLIpSrcMacAddrMask": swIBPACLIpSrcMacAddrMask,
       "swIBPACLIpSrcIpAddrMask": swIBPACLIpSrcIpAddrMask,
       "swACLPktContMaskOptionTable": swACLPktContMaskOptionTable,
       "swACLPktContMaskOptionEntry": swACLPktContMaskOptionEntry,
       "swACLPktContMaskOptionProfileID": swACLPktContMaskOptionProfileID,
       "swACLPktContMaskOffsetChunk1State": swACLPktContMaskOffsetChunk1State,
       "swACLPktContMaskOffsetChunk1OffsetValue": swACLPktContMaskOffsetChunk1OffsetValue,
       "swACLPktContMaskOffsetChunk1Mask": swACLPktContMaskOffsetChunk1Mask,
       "swACLPktContMaskOffsetChunk2State": swACLPktContMaskOffsetChunk2State,
       "swACLPktContMaskOffsetChunk2OffsetValue": swACLPktContMaskOffsetChunk2OffsetValue,
       "swACLPktContMaskOffsetChunk2Mask": swACLPktContMaskOffsetChunk2Mask,
       "swACLPktContMaskOffsetChunk3State": swACLPktContMaskOffsetChunk3State,
       "swACLPktContMaskOffsetChunk3OffsetValue": swACLPktContMaskOffsetChunk3OffsetValue,
       "swACLPktContMaskOffsetChunk3Mask": swACLPktContMaskOffsetChunk3Mask,
       "swACLPktContMaskOffsetChunk4State": swACLPktContMaskOffsetChunk4State,
       "swACLPktContMaskOffsetChunk4OffsetValue": swACLPktContMaskOffsetChunk4OffsetValue,
       "swACLPktContMaskOffsetChunk4Mask": swACLPktContMaskOffsetChunk4Mask,
       "swACLPktContMaskOptionRowStatus": swACLPktContMaskOptionRowStatus,
       "swACLPktContMaskOptionOwner": swACLPktContMaskOptionOwner,
       "swACLPktContMaskOptionUnusedRuleEntries": swACLPktContMaskOptionUnusedRuleEntries,
       "swACLPktContMaskOptionProfileName": swACLPktContMaskOptionProfileName,
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
       "swACLEtherRulePort": swACLEtherRulePort,
       "swACLEtherRuleRowStatus": swACLEtherRuleRowStatus,
       "swACLEtherRuleOwner": swACLEtherRuleOwner,
       "swACLEtherRuleRxRate": swACLEtherRuleRxRate,
       "swACLEtherRuleEnableReplaceTosPrecedence": swACLEtherRuleEnableReplaceTosPrecedence,
       "swACLEtherRuleRepTosPrecedence": swACLEtherRuleRepTosPrecedence,
       "swACLEtherRuleVID": swACLEtherRuleVID,
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
       "swACLIpRulePort": swACLIpRulePort,
       "swACLIpRuleRowStatus": swACLIpRuleRowStatus,
       "swACLIpRuleOwner": swACLIpRuleOwner,
       "swACLIpRuleRxRate": swACLIpRuleRxRate,
       "swACLIpRuleEnableReplaceTosPrecedence": swACLIpRuleEnableReplaceTosPrecedence,
       "swACLIpRuleRepTosPrecedence": swACLIpRuleRepTosPrecedence,
       "swACLIpRuleVID": swACLIpRuleVID,
       "swACLIpv6RuleTable": swACLIpv6RuleTable,
       "swACLIpv6RuleEntry": swACLIpv6RuleEntry,
       "swACLIpv6RuleProfileID": swACLIpv6RuleProfileID,
       "swACLIpv6RuleAccessID": swACLIpv6RuleAccessID,
       "swACLIpv6RuleClass": swACLIpv6RuleClass,
       "swACLIpv6RuleFlowlabel": swACLIpv6RuleFlowlabel,
       "swACLIpv6RuleSrcIpv6Addr": swACLIpv6RuleSrcIpv6Addr,
       "swACLIpv6RuleDstIpv6Addr": swACLIpv6RuleDstIpv6Addr,
       "swACLIpv6RuleEnablePriority": swACLIpv6RuleEnablePriority,
       "swACLIpv6RulePriority": swACLIpv6RulePriority,
       "swACLIpv6RuleReplacePriority": swACLIpv6RuleReplacePriority,
       "swACLIpv6RulePermit": swACLIpv6RulePermit,
       "swACLIpv6RulePort": swACLIpv6RulePort,
       "swACLIpv6RuleRowStatus": swACLIpv6RuleRowStatus,
       "swACLIpv6RuleOwner": swACLIpv6RuleOwner,
       "swACLIpv6RuleRxRate": swACLIpv6RuleRxRate,
       "swACLIpv6RuleEnableReplaceDscp": swACLIpv6RuleEnableReplaceDscp,
       "swACLIpv6RuleRepDscp": swACLIpv6RuleRepDscp,
       "swACLIpv6RuleEnableReplaceTosPrecedence": swACLIpv6RuleEnableReplaceTosPrecedence,
       "swACLIpv6RuleRepTosPrecedence": swACLIpv6RuleRepTosPrecedence,
       "swACLIpv6RuleVID": swACLIpv6RuleVID,
       "swACLIpv6RuleProtocol": swACLIpv6RuleProtocol,
       "swACLIpv6RuleSrcPort": swACLIpv6RuleSrcPort,
       "swACLIpv6RuleDstPort": swACLIpv6RuleDstPort,
       "swIBPACLEtherRuleTable": swIBPACLEtherRuleTable,
       "swIBPACLEtherRuleEntry": swIBPACLEtherRuleEntry,
       "swIBPACLEtherRuleProfileID": swIBPACLEtherRuleProfileID,
       "swIBPACLEtherRuleAccessID": swIBPACLEtherRuleAccessID,
       "swIBPACLEtherRuleEtherType": swIBPACLEtherRuleEtherType,
       "swIBPACLEtherRulePermit": swIBPACLEtherRulePermit,
       "swIBPACLEtherRulePort": swIBPACLEtherRulePort,
       "swIBPACLIpRuleTable": swIBPACLIpRuleTable,
       "swIBPACLIpRuleEntry": swIBPACLIpRuleEntry,
       "swIBPACLIpRuleProfileID": swIBPACLIpRuleProfileID,
       "swIBPACLIpRuleAccessID": swIBPACLIpRuleAccessID,
       "swIBPACLIpRuleSrcMacAddress": swIBPACLIpRuleSrcMacAddress,
       "swIBPACLIpRuleSrcIpaddress": swIBPACLIpRuleSrcIpaddress,
       "swIBPACLIpRulePermit": swIBPACLIpRulePermit,
       "swIBPACLIpRulePort": swIBPACLIpRulePort,
       "swACLCounterTable": swACLCounterTable,
       "swACLCounterEntry": swACLCounterEntry,
       "swACLCounterProfileID": swACLCounterProfileID,
       "swACLCounterAccessID": swACLCounterAccessID,
       "swACLCounterState": swACLCounterState,
       "swACLCounterTotalCounter": swACLCounterTotalCounter,
       "swACLCounterGreenCounter": swACLCounterGreenCounter,
       "swACLCounterYellowCounter": swACLCounterYellowCounter,
       "swACLCounterRedCounter": swACLCounterRedCounter,
       "swACLPktContRuleVarOffsetTable": swACLPktContRuleVarOffsetTable,
       "swACLPktContRuleVarOffsetEntry": swACLPktContRuleVarOffsetEntry,
       "swACLPktContRuleVarOffsetProfileID": swACLPktContRuleVarOffsetProfileID,
       "swACLPktContRuleVarOffsetAccessID": swACLPktContRuleVarOffsetAccessID,
       "swACLPktContRuleVarOffsetOffsetIndex1": swACLPktContRuleVarOffsetOffsetIndex1,
       "swACLPktContRuleVarOffsetMask1": swACLPktContRuleVarOffsetMask1,
       "swACLPktContRuleVarOffsetData1": swACLPktContRuleVarOffsetData1,
       "swACLPktContRuleVarOffsetOffsetIndex2": swACLPktContRuleVarOffsetOffsetIndex2,
       "swACLPktContRuleVarOffsetMask2": swACLPktContRuleVarOffsetMask2,
       "swACLPktContRuleVarOffsetData2": swACLPktContRuleVarOffsetData2,
       "swACLPktContRuleVarOffsetOffsetIndex3": swACLPktContRuleVarOffsetOffsetIndex3,
       "swACLPktContRuleVarOffsetMask3": swACLPktContRuleVarOffsetMask3,
       "swACLPktContRuleVarOffsetData3": swACLPktContRuleVarOffsetData3,
       "swACLPktContRuleVarOffsetOffsetIndex4": swACLPktContRuleVarOffsetOffsetIndex4,
       "swACLPktContRuleVarOffsetMask4": swACLPktContRuleVarOffsetMask4,
       "swACLPktContRuleVarOffsetData4": swACLPktContRuleVarOffsetData4,
       "swACLPktContRuleVarOffsetOffsetIndex5": swACLPktContRuleVarOffsetOffsetIndex5,
       "swACLPktContRuleVarOffsetMask5": swACLPktContRuleVarOffsetMask5,
       "swACLPktContRuleVarOffsetData5": swACLPktContRuleVarOffsetData5,
       "swACLPktContRuleVarOffsetEnablePriority": swACLPktContRuleVarOffsetEnablePriority,
       "swACLPktContRuleVarOffsetPriority": swACLPktContRuleVarOffsetPriority,
       "swACLPktContRuleVarOffsetReplacePriority": swACLPktContRuleVarOffsetReplacePriority,
       "swACLPktContRuleVarOffsetRxRate": swACLPktContRuleVarOffsetRxRate,
       "swACLPktContRuleVarOffsetPermit": swACLPktContRuleVarOffsetPermit,
       "swACLPktContRuleVarOffsetPort": swACLPktContRuleVarOffsetPort,
       "swACLPktContRuleVarOffsetRowStatus": swACLPktContRuleVarOffsetRowStatus,
       "swACLPktContRuleVarOffsetReplacePriorityWith": swACLPktContRuleVarOffsetReplacePriorityWith,
       "swCpuAclMaskMgmt": swCpuAclMaskMgmt,
       "swCpuAclEthernetTable": swCpuAclEthernetTable,
       "swCpuAclEthernetEntry": swCpuAclEthernetEntry,
       "swCpuAclEthernetProfileID": swCpuAclEthernetProfileID,
       "swCpuAclEthernetUsevlan": swCpuAclEthernetUsevlan,
       "swCpuAclEthernetMacAddrMaskState": swCpuAclEthernetMacAddrMaskState,
       "swCpuAclEthernetSrcMacAddrMask": swCpuAclEthernetSrcMacAddrMask,
       "swCpuAclEthernetDstMacAddrMask": swCpuAclEthernetDstMacAddrMask,
       "swCpuAclEthernetUse8021p": swCpuAclEthernetUse8021p,
       "swCpuAclEthernetUseEthernetType": swCpuAclEthernetUseEthernetType,
       "swCpuAclEthernetRowStatus": swCpuAclEthernetRowStatus,
       "swCpuAclIpTable": swCpuAclIpTable,
       "swCpuAclIpEntry": swCpuAclIpEntry,
       "swCpuAclIpProfileID": swCpuAclIpProfileID,
       "swCpuAclIpUsevlan": swCpuAclIpUsevlan,
       "swCpuAclIpIpAddrMaskState": swCpuAclIpIpAddrMaskState,
       "swCpuAclIpSrcIpAddrMask": swCpuAclIpSrcIpAddrMask,
       "swCpuAclIpDstIpAddrMask": swCpuAclIpDstIpAddrMask,
       "swCpuAclIpUseDSCP": swCpuAclIpUseDSCP,
       "swCpuAclIpUseProtoType": swCpuAclIpUseProtoType,
       "swCpuAclIpIcmpOption": swCpuAclIpIcmpOption,
       "swCpuAclIpIgmpOption": swCpuAclIpIgmpOption,
       "swCpuAclIpTcpOption": swCpuAclIpTcpOption,
       "swCpuAclIpUdpOption": swCpuAclIpUdpOption,
       "swCpuAclIpTCPorUDPSrcPortMask": swCpuAclIpTCPorUDPSrcPortMask,
       "swCpuAclIpTCPorUDPDstPortMask": swCpuAclIpTCPorUDPDstPortMask,
       "swCpuAclIpTCPFlagBit": swCpuAclIpTCPFlagBit,
       "swCpuAclIpTCPFlagBitMask": swCpuAclIpTCPFlagBitMask,
       "swCpuAclIpProtoIDOption": swCpuAclIpProtoIDOption,
       "swCpuAclIpProtoID": swCpuAclIpProtoID,
       "swCpuAclIpProtoIDMask": swCpuAclIpProtoIDMask,
       "swCpuAclIpRowStatus": swCpuAclIpRowStatus,
       "swCpuAclPktContMaskTable": swCpuAclPktContMaskTable,
       "swCpuAclPktContMaskEntry": swCpuAclPktContMaskEntry,
       "swCpuAclPktContMaskProfileID": swCpuAclPktContMaskProfileID,
       "swCpuAclPktContMaskOffset0to15": swCpuAclPktContMaskOffset0to15,
       "swCpuAclPktContMaskOffset16to31": swCpuAclPktContMaskOffset16to31,
       "swCpuAclPktContMaskOffset32to47": swCpuAclPktContMaskOffset32to47,
       "swCpuAclPktContMaskOffset48to63": swCpuAclPktContMaskOffset48to63,
       "swCpuAclPktContMaskOffset64to79": swCpuAclPktContMaskOffset64to79,
       "swCpuAclPktContMaskRowStatus": swCpuAclPktContMaskRowStatus,
       "swCpuAclIpv6MaskTable": swCpuAclIpv6MaskTable,
       "swCpuAclIpv6MaskEntry": swCpuAclIpv6MaskEntry,
       "swCpuAclIpv6MaskProfileID": swCpuAclIpv6MaskProfileID,
       "swCpuAclIpv6MaskClass": swCpuAclIpv6MaskClass,
       "swCpuAclIpv6MaskFlowlabel": swCpuAclIpv6MaskFlowlabel,
       "swCpuAclIpv6IpAddrMaskState": swCpuAclIpv6IpAddrMaskState,
       "swCpuAclIpv6MaskSrcIpv6Mask": swCpuAclIpv6MaskSrcIpv6Mask,
       "swCpuAclIpv6MaskDstIpv6Mask": swCpuAclIpv6MaskDstIpv6Mask,
       "swCpuAclIpv6MaskRowStatus": swCpuAclIpv6MaskRowStatus,
       "swCpuACLMaskDelAllState": swCpuACLMaskDelAllState,
       "swCpuAclRuleMgmt": swCpuAclRuleMgmt,
       "swCpuAclEtherRuleTable": swCpuAclEtherRuleTable,
       "swCpuAclEtherRuleEntry": swCpuAclEtherRuleEntry,
       "swCpuAclEtherRuleProfileID": swCpuAclEtherRuleProfileID,
       "swCpuAclEtherRuleAccessID": swCpuAclEtherRuleAccessID,
       "swCpuAclEtherRuleVlan": swCpuAclEtherRuleVlan,
       "swCpuAclEtherRuleSrcMacAddress": swCpuAclEtherRuleSrcMacAddress,
       "swCpuAclEtherRuleDstMacAddress": swCpuAclEtherRuleDstMacAddress,
       "swCpuAclEtherRule8021P": swCpuAclEtherRule8021P,
       "swCpuAclEtherRuleEtherType": swCpuAclEtherRuleEtherType,
       "swCpuAclEtherRulePermit": swCpuAclEtherRulePermit,
       "swCpuAclEtherRuleRowStatus": swCpuAclEtherRuleRowStatus,
       "swCpuAclEtherRulePort": swCpuAclEtherRulePort,
       "swCpuAclIpRuleTable": swCpuAclIpRuleTable,
       "swCpuAclIpRuleEntry": swCpuAclIpRuleEntry,
       "swCpuAclIpRuleProfileID": swCpuAclIpRuleProfileID,
       "swCpuAclIpRuleAccessID": swCpuAclIpRuleAccessID,
       "swCpuAclIpRuleVlan": swCpuAclIpRuleVlan,
       "swCpuAclIpRuleSrcIpaddress": swCpuAclIpRuleSrcIpaddress,
       "swCpuAclIpRuleDstIpaddress": swCpuAclIpRuleDstIpaddress,
       "swCpuAclIpRuleDscp": swCpuAclIpRuleDscp,
       "swCpuAclIpRuleProtocol": swCpuAclIpRuleProtocol,
       "swCpuAclIpRuleType": swCpuAclIpRuleType,
       "swCpuAclIpRuleCode": swCpuAclIpRuleCode,
       "swCpuAclIpRuleSrcPort": swCpuAclIpRuleSrcPort,
       "swCpuAclIpRuleDstPort": swCpuAclIpRuleDstPort,
       "swCpuAclIpRuleFlagBits": swCpuAclIpRuleFlagBits,
       "swCpuAclIpRuleProtoID": swCpuAclIpRuleProtoID,
       "swCpuAclIpRuleUserMask": swCpuAclIpRuleUserMask,
       "swCpuAclIpRulePermit": swCpuAclIpRulePermit,
       "swCpuAclIpRuleRowStatus": swCpuAclIpRuleRowStatus,
       "swCpuAclIpRulePort": swCpuAclIpRulePort,
       "swCpuAclPktContRuleTable": swCpuAclPktContRuleTable,
       "swCpuAclPktContRuleEntry": swCpuAclPktContRuleEntry,
       "swCpuAclPktContRuleProfileID": swCpuAclPktContRuleProfileID,
       "swCpuAclPktContRuleAccessID": swCpuAclPktContRuleAccessID,
       "swCpuAclPktContRuleOffset0to15": swCpuAclPktContRuleOffset0to15,
       "swCpuAclPktContRuleOffset16to31": swCpuAclPktContRuleOffset16to31,
       "swCpuAclPktContRuleOffset32to47": swCpuAclPktContRuleOffset32to47,
       "swCpuAclPktContRuleOffset48to63": swCpuAclPktContRuleOffset48to63,
       "swCpuAclPktContRuleOffset64to79": swCpuAclPktContRuleOffset64to79,
       "swCpuAclPktContRulePermit": swCpuAclPktContRulePermit,
       "swCpuAclPktContRuleRowStatus": swCpuAclPktContRuleRowStatus,
       "swCpuAclPktContRulePort": swCpuAclPktContRulePort,
       "swCpuAclIpv6RuleTable": swCpuAclIpv6RuleTable,
       "swCpuAclIpv6RuleEntry": swCpuAclIpv6RuleEntry,
       "swCpuAclIpv6RuleProfileID": swCpuAclIpv6RuleProfileID,
       "swCpuAclIpv6RuleAccessID": swCpuAclIpv6RuleAccessID,
       "swCpuAclIpv6RuleClass": swCpuAclIpv6RuleClass,
       "swCpuAclIpv6RuleFlowlabel": swCpuAclIpv6RuleFlowlabel,
       "swCpuAclIpv6RuleSrcIpv6Addr": swCpuAclIpv6RuleSrcIpv6Addr,
       "swCpuAclIpv6RuleDstIpv6Addr": swCpuAclIpv6RuleDstIpv6Addr,
       "swCpuAclIpv6RulePermit": swCpuAclIpv6RulePermit,
       "swCpuAclIpv6RuleRowStatus": swCpuAclIpv6RuleRowStatus,
       "swCpuAclIpv6RulePort": swCpuAclIpv6RulePort,
       "swAclMeteringMgmt": swAclMeteringMgmt,
       "swAclMeterTable": swAclMeterTable,
       "swAclMeterEntry": swAclMeterEntry,
       "swAclMeterProfileID": swAclMeterProfileID,
       "swAclMeterAccessID": swAclMeterAccessID,
       "swAclMeterRate": swAclMeterRate,
       "swAclMeterActionForRateExceed": swAclMeterActionForRateExceed,
       "swAclMeterRemarkDscp": swAclMeterRemarkDscp,
       "swAclMeterBurstSize": swAclMeterBurstSize,
       "swAclMeterMode": swAclMeterMode,
       "swAclMeterTrtcmCir": swAclMeterTrtcmCir,
       "swAclMeterTrtcmCbs": swAclMeterTrtcmCbs,
       "swAclMeterTrtcmPir": swAclMeterTrtcmPir,
       "swAclMeterTrtcmPbs": swAclMeterTrtcmPbs,
       "swAclMeterTrtcmColorMode": swAclMeterTrtcmColorMode,
       "swAclMeterTrtcmConformState": swAclMeterTrtcmConformState,
       "swAclMeterTrtcmConformReplaceDscp": swAclMeterTrtcmConformReplaceDscp,
       "swAclMeterTrtcmConformCounterState": swAclMeterTrtcmConformCounterState,
       "swAclMeterTrtcmExceedState": swAclMeterTrtcmExceedState,
       "swAclMeterTrtcmExceedReplaceDscp": swAclMeterTrtcmExceedReplaceDscp,
       "swAclMeterTrtcmExceedCounterState": swAclMeterTrtcmExceedCounterState,
       "swAclMeterTrtcmViolateState": swAclMeterTrtcmViolateState,
       "swAclMeterTrtcmViolateReplaceDscp": swAclMeterTrtcmViolateReplaceDscp,
       "swAclMeterTrtcmViolateCounterState": swAclMeterTrtcmViolateCounterState,
       "swAclMeterSrtcmCir": swAclMeterSrtcmCir,
       "swAclMeterSrtcmCbs": swAclMeterSrtcmCbs,
       "swAclMeterSrtcmEbs": swAclMeterSrtcmEbs,
       "swAclMeterSrtcmColorMode": swAclMeterSrtcmColorMode,
       "swAclMeterSrtcmConformState": swAclMeterSrtcmConformState,
       "swAclMeterSrtcmConformReplaceDscp": swAclMeterSrtcmConformReplaceDscp,
       "swAclMeterSrtcmConformCounterState": swAclMeterSrtcmConformCounterState,
       "swAclMeterSrtcmExceedState": swAclMeterSrtcmExceedState,
       "swAclMeterSrtcmExceedReplaceDscp": swAclMeterSrtcmExceedReplaceDscp,
       "swAclMeterSrtcmExceedCounterState": swAclMeterSrtcmExceedCounterState,
       "swAclMeterSrtcmViolateState": swAclMeterSrtcmViolateState,
       "swAclMeterSrtcmViolateReplaceDscp": swAclMeterSrtcmViolateReplaceDscp,
       "swAclMeterSrtcmViolateCounterState": swAclMeterSrtcmViolateCounterState,
       "swAclMeterRowStatus": swAclMeterRowStatus,
       "swAclMeteringNumOfEntryInUse": swAclMeteringNumOfEntryInUse}
)
