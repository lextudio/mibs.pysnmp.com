# SNMP MIB module (IP-MAC-BIND-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IP-MAC-BIND-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:10:35 2024
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

(Ipv6Address,) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6Address")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

swIpMacBindMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 23)
)


# Types definitions



class VlanId(Integer32):
    """Custom type VlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )





class PortList(OctetString):
    """Custom type PortList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SwIpMacBindingCtrl_ObjectIdentity = ObjectIdentity
swIpMacBindingCtrl = _SwIpMacBindingCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 23, 1)
)


class _SwIpMacBindingTrapLogState_Type(Integer32):
    """Custom type swIpMacBindingTrapLogState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 3),
          ("enable", 2),
          ("other", 1))
    )


_SwIpMacBindingTrapLogState_Type.__name__ = "Integer32"
_SwIpMacBindingTrapLogState_Object = MibScalar
swIpMacBindingTrapLogState = _SwIpMacBindingTrapLogState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 23, 1, 1),
    _SwIpMacBindingTrapLogState_Type()
)
swIpMacBindingTrapLogState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swIpMacBindingTrapLogState.setStatus("current")


class _SwIpMacBindingACLMode_Type(Integer32):
    """Custom type swIpMacBindingACLMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 3),
          ("enable", 2),
          ("other", 1))
    )


_SwIpMacBindingACLMode_Type.__name__ = "Integer32"
_SwIpMacBindingACLMode_Object = MibScalar
swIpMacBindingACLMode = _SwIpMacBindingACLMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 23, 1, 2),
    _SwIpMacBindingACLMode_Type()
)
swIpMacBindingACLMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swIpMacBindingACLMode.setStatus("current")


class _SwIpMacBindingRecoveryInterval_Type(Integer32):
    """Custom type swIpMacBindingRecoveryInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwIpMacBindingRecoveryInterval_Type.__name__ = "Integer32"
_SwIpMacBindingRecoveryInterval_Object = MibScalar
swIpMacBindingRecoveryInterval = _SwIpMacBindingRecoveryInterval_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 23, 1, 3),
    _SwIpMacBindingRecoveryInterval_Type()
)
swIpMacBindingRecoveryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swIpMacBindingRecoveryInterval.setStatus("current")


class _SwIpMacBindingDHCPSnoopState_Type(Integer32):
    """Custom type swIpMacBindingDHCPSnoopState based on Integer32"""
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


_SwIpMacBindingDHCPSnoopState_Type.__name__ = "Integer32"
_SwIpMacBindingDHCPSnoopState_Object = MibScalar
swIpMacBindingDHCPSnoopState = _SwIpMacBindingDHCPSnoopState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 23, 1, 4),
    _SwIpMacBindingDHCPSnoopState_Type()
)
swIpMacBindingDHCPSnoopState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swIpMacBindingDHCPSnoopState.setStatus("current")


class _SwIpMacBindingDHCPSnoopEntryClearAllState_Type(Integer32):
    """Custom type swIpMacBindingDHCPSnoopEntryClearAllState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("start", 2))
    )


_SwIpMacBindingDHCPSnoopEntryClearAllState_Type.__name__ = "Integer32"
_SwIpMacBindingDHCPSnoopEntryClearAllState_Object = MibScalar
swIpMacBindingDHCPSnoopEntryClearAllState = _SwIpMacBindingDHCPSnoopEntryClearAllState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 23, 1, 5),
    _SwIpMacBindingDHCPSnoopEntryClearAllState_Type()
)
swIpMacBindingDHCPSnoopEntryClearAllState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swIpMacBindingDHCPSnoopEntryClearAllState.setStatus("current")


class _SwIpMacBindingARPInspectionState_Type(Integer32):
    """Custom type swIpMacBindingARPInspectionState based on Integer32"""
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


_SwIpMacBindingARPInspectionState_Type.__name__ = "Integer32"
_SwIpMacBindingARPInspectionState_Object = MibScalar
swIpMacBindingARPInspectionState = _SwIpMacBindingARPInspectionState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 23, 1, 6),
    _SwIpMacBindingARPInspectionState_Type()
)
swIpMacBindingARPInspectionState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swIpMacBindingARPInspectionState.setStatus("current")


class _SwIpMacBindingIPv6DHCPSnoopState_Type(Integer32):
    """Custom type swIpMacBindingIPv6DHCPSnoopState based on Integer32"""
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


_SwIpMacBindingIPv6DHCPSnoopState_Type.__name__ = "Integer32"
_SwIpMacBindingIPv6DHCPSnoopState_Object = MibScalar
swIpMacBindingIPv6DHCPSnoopState = _SwIpMacBindingIPv6DHCPSnoopState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 23, 1, 7),
    _SwIpMacBindingIPv6DHCPSnoopState_Type()
)
swIpMacBindingIPv6DHCPSnoopState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swIpMacBindingIPv6DHCPSnoopState.setStatus("current")


class _SwIpMacBindingNDSnoopState_Type(Integer32):
    """Custom type swIpMacBindingNDSnoopState based on Integer32"""
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


_SwIpMacBindingNDSnoopState_Type.__name__ = "Integer32"
_SwIpMacBindingNDSnoopState_Object = MibScalar
swIpMacBindingNDSnoopState = _SwIpMacBindingNDSnoopState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 23, 1, 8),
    _SwIpMacBindingNDSnoopState_Type()
)
swIpMacBindingNDSnoopState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swIpMacBindingNDSnoopState.setStatus("current")


class _SwIpMacBindingIPv6DHCPSnoopEntryClearAllState_Type(Integer32):
    """Custom type swIpMacBindingIPv6DHCPSnoopEntryClearAllState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("start", 2))
    )


_SwIpMacBindingIPv6DHCPSnoopEntryClearAllState_Type.__name__ = "Integer32"
_SwIpMacBindingIPv6DHCPSnoopEntryClearAllState_Object = MibScalar
swIpMacBindingIPv6DHCPSnoopEntryClearAllState = _SwIpMacBindingIPv6DHCPSnoopEntryClearAllState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 23, 1, 9),
    _SwIpMacBindingIPv6DHCPSnoopEntryClearAllState_Type()
)
swIpMacBindingIPv6DHCPSnoopEntryClearAllState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swIpMacBindingIPv6DHCPSnoopEntryClearAllState.setStatus("current")


class _SwIpMacBindingNDSnoopEntryClearAllState_Type(Integer32):
    """Custom type swIpMacBindingNDSnoopEntryClearAllState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("start", 2))
    )


_SwIpMacBindingNDSnoopEntryClearAllState_Type.__name__ = "Integer32"
_SwIpMacBindingNDSnoopEntryClearAllState_Object = MibScalar
swIpMacBindingNDSnoopEntryClearAllState = _SwIpMacBindingNDSnoopEntryClearAllState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 23, 1, 10),
    _SwIpMacBindingNDSnoopEntryClearAllState_Type()
)
swIpMacBindingNDSnoopEntryClearAllState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swIpMacBindingNDSnoopEntryClearAllState.setStatus("current")
_SwIpMacBindingInfo_ObjectIdentity = ObjectIdentity
swIpMacBindingInfo = _SwIpMacBindingInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 23, 2)
)
_SwIpMacBindingPortMgmt_ObjectIdentity = ObjectIdentity
swIpMacBindingPortMgmt = _SwIpMacBindingPortMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 23, 3)
)


class _SwIpMacBindingAllPortState_Type(Integer32):
    """Custom type swIpMacBindingAllPortState based on Integer32"""
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
        *(("disable", 3),
          ("enable-loose", 4),
          ("enable-strict", 2),
          ("other", 1))
    )


_SwIpMacBindingAllPortState_Type.__name__ = "Integer32"
_SwIpMacBindingAllPortState_Object = MibScalar
swIpMacBindingAllPortState = _SwIpMacBindingAllPortState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 23, 3, 1),
    _SwIpMacBindingAllPortState_Type()
)
swIpMacBindingAllPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swIpMacBindingAllPortState.setStatus("current")
_SwIpMacBindingPortTable_Object = MibTable
swIpMacBindingPortTable = _SwIpMacBindingPortTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 23, 3, 2)
)
if mibBuilder.loadTexts:
    swIpMacBindingPortTable.setStatus("current")
_SwIpMacBindingPortEntry_Object = MibTableRow
swIpMacBindingPortEntry = _SwIpMacBindingPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 23, 3, 2, 1)
)
swIpMacBindingPortEntry.setIndexNames(
    (0, "IP-MAC-BIND-MIB", "swIpMacBindingPortIndex"),
)
if mibBuilder.loadTexts:
    swIpMacBindingPortEntry.setStatus("current")


class _SwIpMacBindingPortIndex_Type(Integer32):
    """Custom type swIpMacBindingPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwIpMacBindingPortIndex_Type.__name__ = "Integer32"
_SwIpMacBindingPortIndex_Object = MibTableColumn
swIpMacBindingPortIndex = _SwIpMacBindingPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 23, 3, 2, 1, 1),
    _SwIpMacBindingPortIndex_Type()
)
swIpMacBindingPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIpMacBindingPortIndex.setStatus("current")


class _SwIpMacBindingPortState_Type(Integer32):
    """Custom type swIpMacBindingPortState based on Integer32"""
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
        *(("disable", 3),
          ("enable-loose", 4),
          ("enable-strict", 2),
          ("other", 1))
    )


_SwIpMacBindingPortState_Type.__name__ = "Integer32"
_SwIpMacBindingPortState_Object = MibTableColumn
swIpMacBindingPortState = _SwIpMacBindingPortState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 23, 3, 2, 1, 2),
    _SwIpMacBindingPortState_Type()
)
swIpMacBindingPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swIpMacBindingPortState.setStatus("current")


class _SwIpMacBindingPortZeroIPState_Type(Integer32):
    """Custom type swIpMacBindingPortZeroIPState based on Integer32"""
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


_SwIpMacBindingPortZeroIPState_Type.__name__ = "Integer32"
_SwIpMacBindingPortZeroIPState_Object = MibTableColumn
swIpMacBindingPortZeroIPState = _SwIpMacBindingPortZeroIPState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 23, 3, 2, 1, 3),
    _SwIpMacBindingPortZeroIPState_Type()
)
swIpMacBindingPortZeroIPState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swIpMacBindingPortZeroIPState.setStatus("current")


class _SwIpMacBindingPortForwardDhcpPkt_Type(Integer32):
    """Custom type swIpMacBindingPortForwardDhcpPkt based on Integer32"""
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


_SwIpMacBindingPortForwardDhcpPkt_Type.__name__ = "Integer32"
_SwIpMacBindingPortForwardDhcpPkt_Object = MibTableColumn
swIpMacBindingPortForwardDhcpPkt = _SwIpMacBindingPortForwardDhcpPkt_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 23, 3, 2, 1, 4),
    _SwIpMacBindingPortForwardDhcpPkt_Type()
)
swIpMacBindingPortForwardDhcpPkt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swIpMacBindingPortForwardDhcpPkt.setStatus("current")


class _SwIpMacBindingPortDHCPSnoopMaxEntry_Type(Integer32):
    """Custom type swIpMacBindingPortDHCPSnoopMaxEntry based on Integer32"""
    defaultValue = 0


_SwIpMacBindingPortDHCPSnoopMaxEntry_Object = MibTableColumn
swIpMacBindingPortDHCPSnoopMaxEntry = _SwIpMacBindingPortDHCPSnoopMaxEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 23, 3, 2, 1, 5),
    _SwIpMacBindingPortDHCPSnoopMaxEntry_Type()
)
swIpMacBindingPortDHCPSnoopMaxEntry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swIpMacBindingPortDHCPSnoopMaxEntry.setStatus("current")


class _SwIpMacBindingPortDHCPSnoopEntryClearAction_Type(Integer32):
    """Custom type swIpMacBindingPortDHCPSnoopEntryClearAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("start", 2))
    )


_SwIpMacBindingPortDHCPSnoopEntryClearAction_Type.__name__ = "Integer32"
_SwIpMacBindingPortDHCPSnoopEntryClearAction_Object = MibTableColumn
swIpMacBindingPortDHCPSnoopEntryClearAction = _SwIpMacBindingPortDHCPSnoopEntryClearAction_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 23, 3, 2, 1, 6),
    _SwIpMacBindingPortDHCPSnoopEntryClearAction_Type()
)
swIpMacBindingPortDHCPSnoopEntryClearAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swIpMacBindingPortDHCPSnoopEntryClearAction.setStatus("current")


class _SwIpMacBindingPortMode_Type(Integer32):
    """Custom type swIpMacBindingPortMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("acl", 2),
          ("arp", 1))
    )


_SwIpMacBindingPortMode_Type.__name__ = "Integer32"
_SwIpMacBindingPortMode_Object = MibTableColumn
swIpMacBindingPortMode = _SwIpMacBindingPortMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 23, 3, 2, 1, 7),
    _SwIpMacBindingPortMode_Type()
)
swIpMacBindingPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swIpMacBindingPortMode.setStatus("current")
_SwIpMacBindingPortStopLearningThreshold_Type = Integer32
_SwIpMacBindingPortStopLearningThreshold_Object = MibTableColumn
swIpMacBindingPortStopLearningThreshold = _SwIpMacBindingPortStopLearningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 23, 3, 2, 1, 8),
    _SwIpMacBindingPortStopLearningThreshold_Type()
)
swIpMacBindingPortStopLearningThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swIpMacBindingPortStopLearningThreshold.setStatus("current")


class _SwIpMacBindingPortRecoverLearning_Type(Integer32):
    """Custom type swIpMacBindingPortRecoverLearning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("start", 2))
    )


_SwIpMacBindingPortRecoverLearning_Type.__name__ = "Integer32"
_SwIpMacBindingPortRecoverLearning_Object = MibTableColumn
swIpMacBindingPortRecoverLearning = _SwIpMacBindingPortRecoverLearning_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 23, 3, 2, 1, 9),
    _SwIpMacBindingPortRecoverLearning_Type()
)
swIpMacBindingPortRecoverLearning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swIpMacBindingPortRecoverLearning.setStatus("current")


class _SwIpMacBindingPortLearningStatus_Type(Integer32):
    """Custom type swIpMacBindingPortLearningStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("stop", 2))
    )


_SwIpMacBindingPortLearningStatus_Type.__name__ = "Integer32"
_SwIpMacBindingPortLearningStatus_Object = MibTableColumn
swIpMacBindingPortLearningStatus = _SwIpMacBindingPortLearningStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 23, 3, 2, 1, 10),
    _SwIpMacBindingPortLearningStatus_Type()
)
swIpMacBindingPortLearningStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIpMacBindingPortLearningStatus.setStatus("current")


class _SwIpMacBindingPortIPv6State_Type(Integer32):
    """Custom type swIpMacBindingPortIPv6State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2),
          ("other", 1))
    )


_SwIpMacBindingPortIPv6State_Type.__name__ = "Integer32"
_SwIpMacBindingPortIPv6State_Object = MibTableColumn
swIpMacBindingPortIPv6State = _SwIpMacBindingPortIPv6State_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 23, 3, 2, 1, 11),
    _SwIpMacBindingPortIPv6State_Type()
)
swIpMacBindingPortIPv6State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swIpMacBindingPortIPv6State.setStatus("current")


class _SwIpMacBindingPortIPv6DHCPSnoopMaxEntry_Type(Integer32):
    """Custom type swIpMacBindingPortIPv6DHCPSnoopMaxEntry based on Integer32"""
    defaultValue = 0


_SwIpMacBindingPortIPv6DHCPSnoopMaxEntry_Object = MibTableColumn
swIpMacBindingPortIPv6DHCPSnoopMaxEntry = _SwIpMacBindingPortIPv6DHCPSnoopMaxEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 23, 3, 2, 1, 12),
    _SwIpMacBindingPortIPv6DHCPSnoopMaxEntry_Type()
)
swIpMacBindingPortIPv6DHCPSnoopMaxEntry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swIpMacBindingPortIPv6DHCPSnoopMaxEntry.setStatus("current")


class _SwIpMacBindingPortNDSnoopMaxEntry_Type(Integer32):
    """Custom type swIpMacBindingPortNDSnoopMaxEntry based on Integer32"""
    defaultValue = 0


_SwIpMacBindingPortNDSnoopMaxEntry_Object = MibTableColumn
swIpMacBindingPortNDSnoopMaxEntry = _SwIpMacBindingPortNDSnoopMaxEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 23, 3, 2, 1, 13),
    _SwIpMacBindingPortNDSnoopMaxEntry_Type()
)
swIpMacBindingPortNDSnoopMaxEntry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swIpMacBindingPortNDSnoopMaxEntry.setStatus("current")


class _SwIpMacBindingPortIPv6DHCPSnoopEntryClearAction_Type(Integer32):
    """Custom type swIpMacBindingPortIPv6DHCPSnoopEntryClearAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("start", 2))
    )


_SwIpMacBindingPortIPv6DHCPSnoopEntryClearAction_Type.__name__ = "Integer32"
_SwIpMacBindingPortIPv6DHCPSnoopEntryClearAction_Object = MibTableColumn
swIpMacBindingPortIPv6DHCPSnoopEntryClearAction = _SwIpMacBindingPortIPv6DHCPSnoopEntryClearAction_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 23, 3, 2, 1, 14),
    _SwIpMacBindingPortIPv6DHCPSnoopEntryClearAction_Type()
)
swIpMacBindingPortIPv6DHCPSnoopEntryClearAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swIpMacBindingPortIPv6DHCPSnoopEntryClearAction.setStatus("current")


class _SwIpMacBindingPortNDSnoopEntryClearAction_Type(Integer32):
    """Custom type swIpMacBindingPortNDSnoopEntryClearAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("start", 2))
    )


_SwIpMacBindingPortNDSnoopEntryClearAction_Type.__name__ = "Integer32"
_SwIpMacBindingPortNDSnoopEntryClearAction_Object = MibTableColumn
swIpMacBindingPortNDSnoopEntryClearAction = _SwIpMacBindingPortNDSnoopEntryClearAction_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 23, 3, 2, 1, 15),
    _SwIpMacBindingPortNDSnoopEntryClearAction_Type()
)
swIpMacBindingPortNDSnoopEntryClearAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swIpMacBindingPortNDSnoopEntryClearAction.setStatus("current")


class _SwIpMacBindingPortARPInspection_Type(Integer32):
    """Custom type swIpMacBindingPortARPInspection based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("loose", 3),
          ("strict", 2))
    )


_SwIpMacBindingPortARPInspection_Type.__name__ = "Integer32"
_SwIpMacBindingPortARPInspection_Object = MibTableColumn
swIpMacBindingPortARPInspection = _SwIpMacBindingPortARPInspection_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 23, 3, 2, 1, 16),
    _SwIpMacBindingPortARPInspection_Type()
)
swIpMacBindingPortARPInspection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swIpMacBindingPortARPInspection.setStatus("current")


class _SwIpMacBindingPortIPInspection_Type(Integer32):
    """Custom type swIpMacBindingPortIPInspection based on Integer32"""
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


_SwIpMacBindingPortIPInspection_Type.__name__ = "Integer32"
_SwIpMacBindingPortIPInspection_Object = MibTableColumn
swIpMacBindingPortIPInspection = _SwIpMacBindingPortIPInspection_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 23, 3, 2, 1, 17),
    _SwIpMacBindingPortIPInspection_Type()
)
swIpMacBindingPortIPInspection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swIpMacBindingPortIPInspection.setStatus("current")


class _SwIpMacBindingPortIPProtocol_Type(Integer32):
    """Custom type swIpMacBindingPortIPProtocol based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("all", 1),
          ("ipv4", 2),
          ("ipv6", 3))
    )


_SwIpMacBindingPortIPProtocol_Type.__name__ = "Integer32"
_SwIpMacBindingPortIPProtocol_Object = MibTableColumn
swIpMacBindingPortIPProtocol = _SwIpMacBindingPortIPProtocol_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 23, 3, 2, 1, 18),
    _SwIpMacBindingPortIPProtocol_Type()
)
swIpMacBindingPortIPProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swIpMacBindingPortIPProtocol.setStatus("current")
_SwIpMacBindingMgmt_ObjectIdentity = ObjectIdentity
swIpMacBindingMgmt = _SwIpMacBindingMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 23, 4)
)
_SwIpMacBindingTable_Object = MibTable
swIpMacBindingTable = _SwIpMacBindingTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 23, 4, 1)
)
if mibBuilder.loadTexts:
    swIpMacBindingTable.setStatus("current")
_SwIpMacBindingEntry_Object = MibTableRow
swIpMacBindingEntry = _SwIpMacBindingEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 23, 4, 1, 1)
)
swIpMacBindingEntry.setIndexNames(
    (0, "IP-MAC-BIND-MIB", "swIpMacBindingIpIndex"),
)
if mibBuilder.loadTexts:
    swIpMacBindingEntry.setStatus("current")
_SwIpMacBindingIpIndex_Type = IpAddress
_SwIpMacBindingIpIndex_Object = MibTableColumn
swIpMacBindingIpIndex = _SwIpMacBindingIpIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 23, 4, 1, 1, 1),
    _SwIpMacBindingIpIndex_Type()
)
swIpMacBindingIpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIpMacBindingIpIndex.setStatus("current")
_SwIpMacBindingMac_Type = MacAddress
_SwIpMacBindingMac_Object = MibTableColumn
swIpMacBindingMac = _SwIpMacBindingMac_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 23, 4, 1, 1, 2),
    _SwIpMacBindingMac_Type()
)
swIpMacBindingMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swIpMacBindingMac.setStatus("current")
_SwIpMacBindingStatus_Type = RowStatus
_SwIpMacBindingStatus_Object = MibTableColumn
swIpMacBindingStatus = _SwIpMacBindingStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 23, 4, 1, 1, 3),
    _SwIpMacBindingStatus_Type()
)
swIpMacBindingStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swIpMacBindingStatus.setStatus("current")
_SwIpMacBindingPorts_Type = PortList
_SwIpMacBindingPorts_Object = MibTableColumn
swIpMacBindingPorts = _SwIpMacBindingPorts_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 23, 4, 1, 1, 4),
    _SwIpMacBindingPorts_Type()
)
swIpMacBindingPorts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swIpMacBindingPorts.setStatus("current")


class _SwIpMacBindingAction_Type(Integer32):
    """Custom type swIpMacBindingAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 1))
    )


_SwIpMacBindingAction_Type.__name__ = "Integer32"
_SwIpMacBindingAction_Object = MibTableColumn
swIpMacBindingAction = _SwIpMacBindingAction_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 23, 4, 1, 1, 5),
    _SwIpMacBindingAction_Type()
)
swIpMacBindingAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIpMacBindingAction.setStatus("current")


class _SwIpMacBindingMode_Type(Integer32):
    """Custom type swIpMacBindingMode based on Integer32"""
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
        *(("acl", 2),
          ("arp", 1),
          ("dhcp-snooping", 3),
          ("static", 4))
    )


_SwIpMacBindingMode_Type.__name__ = "Integer32"
_SwIpMacBindingMode_Object = MibTableColumn
swIpMacBindingMode = _SwIpMacBindingMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 23, 4, 1, 1, 6),
    _SwIpMacBindingMode_Type()
)
swIpMacBindingMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swIpMacBindingMode.setStatus("current")


class _SwIpMacBindingAclStatus_Type(Integer32):
    """Custom type swIpMacBindingAclStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 1))
    )


_SwIpMacBindingAclStatus_Type.__name__ = "Integer32"
_SwIpMacBindingAclStatus_Object = MibTableColumn
swIpMacBindingAclStatus = _SwIpMacBindingAclStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 23, 4, 1, 1, 7),
    _SwIpMacBindingAclStatus_Type()
)
swIpMacBindingAclStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIpMacBindingAclStatus.setStatus("current")
_SwIpMacBindingBlockedTable_Object = MibTable
swIpMacBindingBlockedTable = _SwIpMacBindingBlockedTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 23, 4, 2)
)
if mibBuilder.loadTexts:
    swIpMacBindingBlockedTable.setStatus("current")
_SwIpMacBindingBlockedEntry_Object = MibTableRow
swIpMacBindingBlockedEntry = _SwIpMacBindingBlockedEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 23, 4, 2, 1)
)
swIpMacBindingBlockedEntry.setIndexNames(
    (0, "IP-MAC-BIND-MIB", "swIpMacBindingBlockedVID"),
    (0, "IP-MAC-BIND-MIB", "swIpMacBindingBlockedMac"),
)
if mibBuilder.loadTexts:
    swIpMacBindingBlockedEntry.setStatus("current")
_SwIpMacBindingBlockedVID_Type = VlanId
_SwIpMacBindingBlockedVID_Object = MibTableColumn
swIpMacBindingBlockedVID = _SwIpMacBindingBlockedVID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 23, 4, 2, 1, 1),
    _SwIpMacBindingBlockedVID_Type()
)
swIpMacBindingBlockedVID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIpMacBindingBlockedVID.setStatus("current")
_SwIpMacBindingBlockedMac_Type = MacAddress
_SwIpMacBindingBlockedMac_Object = MibTableColumn
swIpMacBindingBlockedMac = _SwIpMacBindingBlockedMac_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 23, 4, 2, 1, 2),
    _SwIpMacBindingBlockedMac_Type()
)
swIpMacBindingBlockedMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIpMacBindingBlockedMac.setStatus("current")
_SwIpMacBindingBlockedVlanName_Type = DisplayString
_SwIpMacBindingBlockedVlanName_Object = MibTableColumn
swIpMacBindingBlockedVlanName = _SwIpMacBindingBlockedVlanName_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 23, 4, 2, 1, 3),
    _SwIpMacBindingBlockedVlanName_Type()
)
swIpMacBindingBlockedVlanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIpMacBindingBlockedVlanName.setStatus("current")


class _SwIpMacBindingBlockedPort_Type(Integer32):
    """Custom type swIpMacBindingBlockedPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwIpMacBindingBlockedPort_Type.__name__ = "Integer32"
_SwIpMacBindingBlockedPort_Object = MibTableColumn
swIpMacBindingBlockedPort = _SwIpMacBindingBlockedPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 23, 4, 2, 1, 4),
    _SwIpMacBindingBlockedPort_Type()
)
swIpMacBindingBlockedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIpMacBindingBlockedPort.setStatus("current")


class _SwIpMacBindingBlockedType_Type(Integer32):
    """Custom type swIpMacBindingBlockedType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("blockByAddrBind", 2),
          ("delete", 3),
          ("other", 1))
    )


_SwIpMacBindingBlockedType_Type.__name__ = "Integer32"
_SwIpMacBindingBlockedType_Object = MibTableColumn
swIpMacBindingBlockedType = _SwIpMacBindingBlockedType_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 23, 4, 2, 1, 5),
    _SwIpMacBindingBlockedType_Type()
)
swIpMacBindingBlockedType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swIpMacBindingBlockedType.setStatus("obsolete")
_SwIpMacBindingBlockedTime_Type = DateAndTime
_SwIpMacBindingBlockedTime_Object = MibTableColumn
swIpMacBindingBlockedTime = _SwIpMacBindingBlockedTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 23, 4, 2, 1, 6),
    _SwIpMacBindingBlockedTime_Type()
)
swIpMacBindingBlockedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIpMacBindingBlockedTime.setStatus("current")
_SwIpMacBindingBlockedStatus_Type = RowStatus
_SwIpMacBindingBlockedStatus_Object = MibTableColumn
swIpMacBindingBlockedStatus = _SwIpMacBindingBlockedStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 23, 4, 2, 1, 7),
    _SwIpMacBindingBlockedStatus_Type()
)
swIpMacBindingBlockedStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swIpMacBindingBlockedStatus.setStatus("current")
_SwIpMacBindingDHCPSnoopTable_Object = MibTable
swIpMacBindingDHCPSnoopTable = _SwIpMacBindingDHCPSnoopTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 23, 4, 3)
)
if mibBuilder.loadTexts:
    swIpMacBindingDHCPSnoopTable.setStatus("current")
_SwIpMacBindingDHCPSnoopEntry_Object = MibTableRow
swIpMacBindingDHCPSnoopEntry = _SwIpMacBindingDHCPSnoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 23, 4, 3, 1)
)
swIpMacBindingDHCPSnoopEntry.setIndexNames(
    (0, "IP-MAC-BIND-MIB", "swIpMacBindingDHCPSnoopIpIndex"),
)
if mibBuilder.loadTexts:
    swIpMacBindingDHCPSnoopEntry.setStatus("current")
_SwIpMacBindingDHCPSnoopIpIndex_Type = IpAddress
_SwIpMacBindingDHCPSnoopIpIndex_Object = MibTableColumn
swIpMacBindingDHCPSnoopIpIndex = _SwIpMacBindingDHCPSnoopIpIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 23, 4, 3, 1, 1),
    _SwIpMacBindingDHCPSnoopIpIndex_Type()
)
swIpMacBindingDHCPSnoopIpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIpMacBindingDHCPSnoopIpIndex.setStatus("current")
_SwIpMacBindingDHCPSnoopMac_Type = MacAddress
_SwIpMacBindingDHCPSnoopMac_Object = MibTableColumn
swIpMacBindingDHCPSnoopMac = _SwIpMacBindingDHCPSnoopMac_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 23, 4, 3, 1, 2),
    _SwIpMacBindingDHCPSnoopMac_Type()
)
swIpMacBindingDHCPSnoopMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIpMacBindingDHCPSnoopMac.setStatus("current")
_SwIpMacBindingDHCPSnoopLeaseTime_Type = Integer32
_SwIpMacBindingDHCPSnoopLeaseTime_Object = MibTableColumn
swIpMacBindingDHCPSnoopLeaseTime = _SwIpMacBindingDHCPSnoopLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 23, 4, 3, 1, 3),
    _SwIpMacBindingDHCPSnoopLeaseTime_Type()
)
swIpMacBindingDHCPSnoopLeaseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIpMacBindingDHCPSnoopLeaseTime.setStatus("current")
_SwIpMacBindingDHCPSnoopPort_Type = Integer32
_SwIpMacBindingDHCPSnoopPort_Object = MibTableColumn
swIpMacBindingDHCPSnoopPort = _SwIpMacBindingDHCPSnoopPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 23, 4, 3, 1, 4),
    _SwIpMacBindingDHCPSnoopPort_Type()
)
swIpMacBindingDHCPSnoopPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIpMacBindingDHCPSnoopPort.setStatus("current")


class _SwIpMacBindingDHCPSnoopStatus_Type(Integer32):
    """Custom type swIpMacBindingDHCPSnoopStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 1))
    )


_SwIpMacBindingDHCPSnoopStatus_Type.__name__ = "Integer32"
_SwIpMacBindingDHCPSnoopStatus_Object = MibTableColumn
swIpMacBindingDHCPSnoopStatus = _SwIpMacBindingDHCPSnoopStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 23, 4, 3, 1, 5),
    _SwIpMacBindingDHCPSnoopStatus_Type()
)
swIpMacBindingDHCPSnoopStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIpMacBindingDHCPSnoopStatus.setStatus("current")
_SwIpMacBindingIPv6Table_Object = MibTable
swIpMacBindingIPv6Table = _SwIpMacBindingIPv6Table_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 23, 4, 4)
)
if mibBuilder.loadTexts:
    swIpMacBindingIPv6Table.setStatus("current")
_SwIpMacBindingIPv6Entry_Object = MibTableRow
swIpMacBindingIPv6Entry = _SwIpMacBindingIPv6Entry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 23, 4, 4, 1)
)
swIpMacBindingIPv6Entry.setIndexNames(
    (0, "IP-MAC-BIND-MIB", "swIpMacBindingIPv6Addr"),
)
if mibBuilder.loadTexts:
    swIpMacBindingIPv6Entry.setStatus("current")
_SwIpMacBindingIPv6Addr_Type = Ipv6Address
_SwIpMacBindingIPv6Addr_Object = MibTableColumn
swIpMacBindingIPv6Addr = _SwIpMacBindingIPv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 23, 4, 4, 1, 1),
    _SwIpMacBindingIPv6Addr_Type()
)
swIpMacBindingIPv6Addr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIpMacBindingIPv6Addr.setStatus("current")
_SwIpMacBindingIPv6MacAddr_Type = MacAddress
_SwIpMacBindingIPv6MacAddr_Object = MibTableColumn
swIpMacBindingIPv6MacAddr = _SwIpMacBindingIPv6MacAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 23, 4, 4, 1, 2),
    _SwIpMacBindingIPv6MacAddr_Type()
)
swIpMacBindingIPv6MacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swIpMacBindingIPv6MacAddr.setStatus("current")
_SwIpMacBindingIPv6Portlist_Type = PortList
_SwIpMacBindingIPv6Portlist_Object = MibTableColumn
swIpMacBindingIPv6Portlist = _SwIpMacBindingIPv6Portlist_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 23, 4, 4, 1, 3),
    _SwIpMacBindingIPv6Portlist_Type()
)
swIpMacBindingIPv6Portlist.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swIpMacBindingIPv6Portlist.setStatus("current")


class _SwIpMacBindingIPv6Mode_Type(Integer32):
    """Custom type swIpMacBindingIPv6Mode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dhcp-snooping", 2),
          ("nd-snooping", 3),
          ("static", 1))
    )


_SwIpMacBindingIPv6Mode_Type.__name__ = "Integer32"
_SwIpMacBindingIPv6Mode_Object = MibTableColumn
swIpMacBindingIPv6Mode = _SwIpMacBindingIPv6Mode_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 23, 4, 4, 1, 4),
    _SwIpMacBindingIPv6Mode_Type()
)
swIpMacBindingIPv6Mode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIpMacBindingIPv6Mode.setStatus("current")


class _SwIpMacBindingIPv6ACLStatus_Type(Integer32):
    """Custom type swIpMacBindingIPv6ACLStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 1))
    )


_SwIpMacBindingIPv6ACLStatus_Type.__name__ = "Integer32"
_SwIpMacBindingIPv6ACLStatus_Object = MibTableColumn
swIpMacBindingIPv6ACLStatus = _SwIpMacBindingIPv6ACLStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 23, 4, 4, 1, 5),
    _SwIpMacBindingIPv6ACLStatus_Type()
)
swIpMacBindingIPv6ACLStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIpMacBindingIPv6ACLStatus.setStatus("current")
_SwIpMacBindingIPv6RowStatus_Type = RowStatus
_SwIpMacBindingIPv6RowStatus_Object = MibTableColumn
swIpMacBindingIPv6RowStatus = _SwIpMacBindingIPv6RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 23, 4, 4, 1, 6),
    _SwIpMacBindingIPv6RowStatus_Type()
)
swIpMacBindingIPv6RowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swIpMacBindingIPv6RowStatus.setStatus("current")
_SwIpMacBindingIPv6DHCPSnoopTable_Object = MibTable
swIpMacBindingIPv6DHCPSnoopTable = _SwIpMacBindingIPv6DHCPSnoopTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 23, 4, 5)
)
if mibBuilder.loadTexts:
    swIpMacBindingIPv6DHCPSnoopTable.setStatus("current")
_SwIpMacBindingIPv6DHCPSnoopEntry_Object = MibTableRow
swIpMacBindingIPv6DHCPSnoopEntry = _SwIpMacBindingIPv6DHCPSnoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 23, 4, 5, 1)
)
swIpMacBindingIPv6DHCPSnoopEntry.setIndexNames(
    (0, "IP-MAC-BIND-MIB", "swIpMacBindingIPv6DHCPSnoopAddr"),
)
if mibBuilder.loadTexts:
    swIpMacBindingIPv6DHCPSnoopEntry.setStatus("current")
_SwIpMacBindingIPv6DHCPSnoopAddr_Type = Ipv6Address
_SwIpMacBindingIPv6DHCPSnoopAddr_Object = MibTableColumn
swIpMacBindingIPv6DHCPSnoopAddr = _SwIpMacBindingIPv6DHCPSnoopAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 23, 4, 5, 1, 1),
    _SwIpMacBindingIPv6DHCPSnoopAddr_Type()
)
swIpMacBindingIPv6DHCPSnoopAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIpMacBindingIPv6DHCPSnoopAddr.setStatus("current")
_SwIpMacBindingIPv6DHCPSnoopMac_Type = MacAddress
_SwIpMacBindingIPv6DHCPSnoopMac_Object = MibTableColumn
swIpMacBindingIPv6DHCPSnoopMac = _SwIpMacBindingIPv6DHCPSnoopMac_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 23, 4, 5, 1, 2),
    _SwIpMacBindingIPv6DHCPSnoopMac_Type()
)
swIpMacBindingIPv6DHCPSnoopMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIpMacBindingIPv6DHCPSnoopMac.setStatus("current")
_SwIpMacBindingIPv6DHCPSnoopLeaseTime_Type = Integer32
_SwIpMacBindingIPv6DHCPSnoopLeaseTime_Object = MibTableColumn
swIpMacBindingIPv6DHCPSnoopLeaseTime = _SwIpMacBindingIPv6DHCPSnoopLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 23, 4, 5, 1, 3),
    _SwIpMacBindingIPv6DHCPSnoopLeaseTime_Type()
)
swIpMacBindingIPv6DHCPSnoopLeaseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIpMacBindingIPv6DHCPSnoopLeaseTime.setStatus("current")
_SwIpMacBindingIPv6DHCPSnoopPort_Type = Integer32
_SwIpMacBindingIPv6DHCPSnoopPort_Object = MibTableColumn
swIpMacBindingIPv6DHCPSnoopPort = _SwIpMacBindingIPv6DHCPSnoopPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 23, 4, 5, 1, 4),
    _SwIpMacBindingIPv6DHCPSnoopPort_Type()
)
swIpMacBindingIPv6DHCPSnoopPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIpMacBindingIPv6DHCPSnoopPort.setStatus("current")


class _SwIpMacBindingIPv6DHCPSnoopStatus_Type(Integer32):
    """Custom type swIpMacBindingIPv6DHCPSnoopStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 1))
    )


_SwIpMacBindingIPv6DHCPSnoopStatus_Type.__name__ = "Integer32"
_SwIpMacBindingIPv6DHCPSnoopStatus_Object = MibTableColumn
swIpMacBindingIPv6DHCPSnoopStatus = _SwIpMacBindingIPv6DHCPSnoopStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 23, 4, 5, 1, 5),
    _SwIpMacBindingIPv6DHCPSnoopStatus_Type()
)
swIpMacBindingIPv6DHCPSnoopStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIpMacBindingIPv6DHCPSnoopStatus.setStatus("current")
_SwIpMacBindingNDSnoopTable_Object = MibTable
swIpMacBindingNDSnoopTable = _SwIpMacBindingNDSnoopTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 23, 4, 6)
)
if mibBuilder.loadTexts:
    swIpMacBindingNDSnoopTable.setStatus("current")
_SwIpMacBindingNDSnoopEntry_Object = MibTableRow
swIpMacBindingNDSnoopEntry = _SwIpMacBindingNDSnoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 23, 4, 6, 1)
)
swIpMacBindingNDSnoopEntry.setIndexNames(
    (0, "IP-MAC-BIND-MIB", "swIpMacBindingNDSnoopAddr"),
)
if mibBuilder.loadTexts:
    swIpMacBindingNDSnoopEntry.setStatus("current")
_SwIpMacBindingNDSnoopAddr_Type = Ipv6Address
_SwIpMacBindingNDSnoopAddr_Object = MibTableColumn
swIpMacBindingNDSnoopAddr = _SwIpMacBindingNDSnoopAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 23, 4, 6, 1, 1),
    _SwIpMacBindingNDSnoopAddr_Type()
)
swIpMacBindingNDSnoopAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIpMacBindingNDSnoopAddr.setStatus("current")
_SwIpMacBindingNDSnoopMac_Type = MacAddress
_SwIpMacBindingNDSnoopMac_Object = MibTableColumn
swIpMacBindingNDSnoopMac = _SwIpMacBindingNDSnoopMac_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 23, 4, 6, 1, 2),
    _SwIpMacBindingNDSnoopMac_Type()
)
swIpMacBindingNDSnoopMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIpMacBindingNDSnoopMac.setStatus("current")
_SwIpMacBindingNDSnoopLeaseTime_Type = Integer32
_SwIpMacBindingNDSnoopLeaseTime_Object = MibTableColumn
swIpMacBindingNDSnoopLeaseTime = _SwIpMacBindingNDSnoopLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 23, 4, 6, 1, 3),
    _SwIpMacBindingNDSnoopLeaseTime_Type()
)
swIpMacBindingNDSnoopLeaseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIpMacBindingNDSnoopLeaseTime.setStatus("current")
_SwIpMacBindingNDSnoopPort_Type = Integer32
_SwIpMacBindingNDSnoopPort_Object = MibTableColumn
swIpMacBindingNDSnoopPort = _SwIpMacBindingNDSnoopPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 23, 4, 6, 1, 4),
    _SwIpMacBindingNDSnoopPort_Type()
)
swIpMacBindingNDSnoopPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIpMacBindingNDSnoopPort.setStatus("current")


class _SwIpMacBindingNDSnoopStatus_Type(Integer32):
    """Custom type swIpMacBindingNDSnoopStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 1))
    )


_SwIpMacBindingNDSnoopStatus_Type.__name__ = "Integer32"
_SwIpMacBindingNDSnoopStatus_Object = MibTableColumn
swIpMacBindingNDSnoopStatus = _SwIpMacBindingNDSnoopStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 23, 4, 6, 1, 5),
    _SwIpMacBindingNDSnoopStatus_Type()
)
swIpMacBindingNDSnoopStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIpMacBindingNDSnoopStatus.setStatus("current")
_SwIpMacBindingNotify_ObjectIdentity = ObjectIdentity
swIpMacBindingNotify = _SwIpMacBindingNotify_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 23, 5)
)
_SwIpMacBindingNotifyPrefix_ObjectIdentity = ObjectIdentity
swIpMacBindingNotifyPrefix = _SwIpMacBindingNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 23, 5, 0)
)
_SwIpMacBindingNotificationBidings_ObjectIdentity = ObjectIdentity
swIpMacBindingNotificationBidings = _SwIpMacBindingNotificationBidings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 23, 5, 2)
)
_SwIpMacBindingViolationIP_Type = IpAddress
_SwIpMacBindingViolationIP_Object = MibScalar
swIpMacBindingViolationIP = _SwIpMacBindingViolationIP_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 23, 5, 2, 1),
    _SwIpMacBindingViolationIP_Type()
)
swIpMacBindingViolationIP.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    swIpMacBindingViolationIP.setStatus("current")
_SwIpMacBindingViolationMac_Type = MacAddress
_SwIpMacBindingViolationMac_Object = MibScalar
swIpMacBindingViolationMac = _SwIpMacBindingViolationMac_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 23, 5, 2, 2),
    _SwIpMacBindingViolationMac_Type()
)
swIpMacBindingViolationMac.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    swIpMacBindingViolationMac.setStatus("current")
_SwIpMacBindingViolationIPv6Addr_Type = Ipv6Address
_SwIpMacBindingViolationIPv6Addr_Object = MibScalar
swIpMacBindingViolationIPv6Addr = _SwIpMacBindingViolationIPv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 23, 5, 2, 3),
    _SwIpMacBindingViolationIPv6Addr_Type()
)
swIpMacBindingViolationIPv6Addr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    swIpMacBindingViolationIPv6Addr.setStatus("current")

# Managed Objects groups


# Notification objects

swIpMacBindingViolationTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 12, 23, 5, 0, 1)
)
swIpMacBindingViolationTrap.setObjects(
      *(("IP-MAC-BIND-MIB", "swIpMacBindingPortIndex"),
        ("IP-MAC-BIND-MIB", "swIpMacBindingViolationIP"),
        ("IP-MAC-BIND-MIB", "swIpMacBindingViolationMac"))
)
if mibBuilder.loadTexts:
    swIpMacBindingViolationTrap.setStatus(
        "current"
    )

swIpMacBindingStopLearningTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 12, 23, 5, 0, 2)
)
swIpMacBindingStopLearningTrap.setObjects(
    ("IP-MAC-BIND-MIB", "swIpMacBindingPortIndex")
)
if mibBuilder.loadTexts:
    swIpMacBindingStopLearningTrap.setStatus(
        "current"
    )

swIpMacBindingRecoverLearningTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 12, 23, 5, 0, 3)
)
swIpMacBindingRecoverLearningTrap.setObjects(
    ("IP-MAC-BIND-MIB", "swIpMacBindingPortIndex")
)
if mibBuilder.loadTexts:
    swIpMacBindingRecoverLearningTrap.setStatus(
        "current"
    )

swIpMacBindingIPv6ViolationTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 12, 23, 5, 0, 4)
)
swIpMacBindingIPv6ViolationTrap.setObjects(
      *(("IP-MAC-BIND-MIB", "swIpMacBindingPortIndex"),
        ("IP-MAC-BIND-MIB", "swIpMacBindingViolationIPv6Addr"),
        ("IP-MAC-BIND-MIB", "swIpMacBindingViolationMac"))
)
if mibBuilder.loadTexts:
    swIpMacBindingIPv6ViolationTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IP-MAC-BIND-MIB",
    **{"VlanId": VlanId,
       "PortList": PortList,
       "swIpMacBindMIB": swIpMacBindMIB,
       "swIpMacBindingCtrl": swIpMacBindingCtrl,
       "swIpMacBindingTrapLogState": swIpMacBindingTrapLogState,
       "swIpMacBindingACLMode": swIpMacBindingACLMode,
       "swIpMacBindingRecoveryInterval": swIpMacBindingRecoveryInterval,
       "swIpMacBindingDHCPSnoopState": swIpMacBindingDHCPSnoopState,
       "swIpMacBindingDHCPSnoopEntryClearAllState": swIpMacBindingDHCPSnoopEntryClearAllState,
       "swIpMacBindingARPInspectionState": swIpMacBindingARPInspectionState,
       "swIpMacBindingIPv6DHCPSnoopState": swIpMacBindingIPv6DHCPSnoopState,
       "swIpMacBindingNDSnoopState": swIpMacBindingNDSnoopState,
       "swIpMacBindingIPv6DHCPSnoopEntryClearAllState": swIpMacBindingIPv6DHCPSnoopEntryClearAllState,
       "swIpMacBindingNDSnoopEntryClearAllState": swIpMacBindingNDSnoopEntryClearAllState,
       "swIpMacBindingInfo": swIpMacBindingInfo,
       "swIpMacBindingPortMgmt": swIpMacBindingPortMgmt,
       "swIpMacBindingAllPortState": swIpMacBindingAllPortState,
       "swIpMacBindingPortTable": swIpMacBindingPortTable,
       "swIpMacBindingPortEntry": swIpMacBindingPortEntry,
       "swIpMacBindingPortIndex": swIpMacBindingPortIndex,
       "swIpMacBindingPortState": swIpMacBindingPortState,
       "swIpMacBindingPortZeroIPState": swIpMacBindingPortZeroIPState,
       "swIpMacBindingPortForwardDhcpPkt": swIpMacBindingPortForwardDhcpPkt,
       "swIpMacBindingPortDHCPSnoopMaxEntry": swIpMacBindingPortDHCPSnoopMaxEntry,
       "swIpMacBindingPortDHCPSnoopEntryClearAction": swIpMacBindingPortDHCPSnoopEntryClearAction,
       "swIpMacBindingPortMode": swIpMacBindingPortMode,
       "swIpMacBindingPortStopLearningThreshold": swIpMacBindingPortStopLearningThreshold,
       "swIpMacBindingPortRecoverLearning": swIpMacBindingPortRecoverLearning,
       "swIpMacBindingPortLearningStatus": swIpMacBindingPortLearningStatus,
       "swIpMacBindingPortIPv6State": swIpMacBindingPortIPv6State,
       "swIpMacBindingPortIPv6DHCPSnoopMaxEntry": swIpMacBindingPortIPv6DHCPSnoopMaxEntry,
       "swIpMacBindingPortNDSnoopMaxEntry": swIpMacBindingPortNDSnoopMaxEntry,
       "swIpMacBindingPortIPv6DHCPSnoopEntryClearAction": swIpMacBindingPortIPv6DHCPSnoopEntryClearAction,
       "swIpMacBindingPortNDSnoopEntryClearAction": swIpMacBindingPortNDSnoopEntryClearAction,
       "swIpMacBindingPortARPInspection": swIpMacBindingPortARPInspection,
       "swIpMacBindingPortIPInspection": swIpMacBindingPortIPInspection,
       "swIpMacBindingPortIPProtocol": swIpMacBindingPortIPProtocol,
       "swIpMacBindingMgmt": swIpMacBindingMgmt,
       "swIpMacBindingTable": swIpMacBindingTable,
       "swIpMacBindingEntry": swIpMacBindingEntry,
       "swIpMacBindingIpIndex": swIpMacBindingIpIndex,
       "swIpMacBindingMac": swIpMacBindingMac,
       "swIpMacBindingStatus": swIpMacBindingStatus,
       "swIpMacBindingPorts": swIpMacBindingPorts,
       "swIpMacBindingAction": swIpMacBindingAction,
       "swIpMacBindingMode": swIpMacBindingMode,
       "swIpMacBindingAclStatus": swIpMacBindingAclStatus,
       "swIpMacBindingBlockedTable": swIpMacBindingBlockedTable,
       "swIpMacBindingBlockedEntry": swIpMacBindingBlockedEntry,
       "swIpMacBindingBlockedVID": swIpMacBindingBlockedVID,
       "swIpMacBindingBlockedMac": swIpMacBindingBlockedMac,
       "swIpMacBindingBlockedVlanName": swIpMacBindingBlockedVlanName,
       "swIpMacBindingBlockedPort": swIpMacBindingBlockedPort,
       "swIpMacBindingBlockedType": swIpMacBindingBlockedType,
       "swIpMacBindingBlockedTime": swIpMacBindingBlockedTime,
       "swIpMacBindingBlockedStatus": swIpMacBindingBlockedStatus,
       "swIpMacBindingDHCPSnoopTable": swIpMacBindingDHCPSnoopTable,
       "swIpMacBindingDHCPSnoopEntry": swIpMacBindingDHCPSnoopEntry,
       "swIpMacBindingDHCPSnoopIpIndex": swIpMacBindingDHCPSnoopIpIndex,
       "swIpMacBindingDHCPSnoopMac": swIpMacBindingDHCPSnoopMac,
       "swIpMacBindingDHCPSnoopLeaseTime": swIpMacBindingDHCPSnoopLeaseTime,
       "swIpMacBindingDHCPSnoopPort": swIpMacBindingDHCPSnoopPort,
       "swIpMacBindingDHCPSnoopStatus": swIpMacBindingDHCPSnoopStatus,
       "swIpMacBindingIPv6Table": swIpMacBindingIPv6Table,
       "swIpMacBindingIPv6Entry": swIpMacBindingIPv6Entry,
       "swIpMacBindingIPv6Addr": swIpMacBindingIPv6Addr,
       "swIpMacBindingIPv6MacAddr": swIpMacBindingIPv6MacAddr,
       "swIpMacBindingIPv6Portlist": swIpMacBindingIPv6Portlist,
       "swIpMacBindingIPv6Mode": swIpMacBindingIPv6Mode,
       "swIpMacBindingIPv6ACLStatus": swIpMacBindingIPv6ACLStatus,
       "swIpMacBindingIPv6RowStatus": swIpMacBindingIPv6RowStatus,
       "swIpMacBindingIPv6DHCPSnoopTable": swIpMacBindingIPv6DHCPSnoopTable,
       "swIpMacBindingIPv6DHCPSnoopEntry": swIpMacBindingIPv6DHCPSnoopEntry,
       "swIpMacBindingIPv6DHCPSnoopAddr": swIpMacBindingIPv6DHCPSnoopAddr,
       "swIpMacBindingIPv6DHCPSnoopMac": swIpMacBindingIPv6DHCPSnoopMac,
       "swIpMacBindingIPv6DHCPSnoopLeaseTime": swIpMacBindingIPv6DHCPSnoopLeaseTime,
       "swIpMacBindingIPv6DHCPSnoopPort": swIpMacBindingIPv6DHCPSnoopPort,
       "swIpMacBindingIPv6DHCPSnoopStatus": swIpMacBindingIPv6DHCPSnoopStatus,
       "swIpMacBindingNDSnoopTable": swIpMacBindingNDSnoopTable,
       "swIpMacBindingNDSnoopEntry": swIpMacBindingNDSnoopEntry,
       "swIpMacBindingNDSnoopAddr": swIpMacBindingNDSnoopAddr,
       "swIpMacBindingNDSnoopMac": swIpMacBindingNDSnoopMac,
       "swIpMacBindingNDSnoopLeaseTime": swIpMacBindingNDSnoopLeaseTime,
       "swIpMacBindingNDSnoopPort": swIpMacBindingNDSnoopPort,
       "swIpMacBindingNDSnoopStatus": swIpMacBindingNDSnoopStatus,
       "swIpMacBindingNotify": swIpMacBindingNotify,
       "swIpMacBindingNotifyPrefix": swIpMacBindingNotifyPrefix,
       "swIpMacBindingViolationTrap": swIpMacBindingViolationTrap,
       "swIpMacBindingStopLearningTrap": swIpMacBindingStopLearningTrap,
       "swIpMacBindingRecoverLearningTrap": swIpMacBindingRecoverLearningTrap,
       "swIpMacBindingIPv6ViolationTrap": swIpMacBindingIPv6ViolationTrap,
       "swIpMacBindingNotificationBidings": swIpMacBindingNotificationBidings,
       "swIpMacBindingViolationIP": swIpMacBindingViolationIP,
       "swIpMacBindingViolationMac": swIpMacBindingViolationMac,
       "swIpMacBindingViolationIPv6Addr": swIpMacBindingViolationIPv6Addr}
)
