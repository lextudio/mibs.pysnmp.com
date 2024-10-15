# SNMP MIB module (HUAWEI-TUNNEL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-TUNNEL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:06:18 2024
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

(hwDatacomm,) = mibBuilder.importSymbols(
    "HUAWEI-MIB",
    "hwDatacomm")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(ipv6IfIndex,) = mibBuilder.importSymbols(
    "IPV6-MIB",
    "ipv6IfIndex")

(Ipv6Address,) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6Address")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

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

hwTunnelMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 201)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwTunnelMibObjects_ObjectIdentity = ObjectIdentity
hwTunnelMibObjects = _HwTunnelMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 201, 1)
)
_HwTunnelCfgTable_Object = MibTable
hwTunnelCfgTable = _HwTunnelCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 201, 1, 1)
)
if mibBuilder.loadTexts:
    hwTunnelCfgTable.setStatus("current")
_HwTunnelCfgEntry_Object = MibTableRow
hwTunnelCfgEntry = _HwTunnelCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 201, 1, 1, 1)
)
hwTunnelCfgEntry.setIndexNames(
    (0, "IPV6-MIB", "ipv6IfIndex"),
)
if mibBuilder.loadTexts:
    hwTunnelCfgEntry.setStatus("current")


class _HwTunnelProtocol_Type(Integer32):
    """Custom type hwTunnelProtocol based on Integer32"""
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
        *(("gre", 1),
          ("ipv4Ipv6", 7),
          ("ipv6Ipv4", 3),
          ("ipv6Ipv46to4", 5),
          ("ipv6Ipv4Auto", 4),
          ("ipv6Ipv4Isatap", 6),
          ("mplsTe", 2),
          ("none", 8))
    )


_HwTunnelProtocol_Type.__name__ = "Integer32"
_HwTunnelProtocol_Object = MibTableColumn
hwTunnelProtocol = _HwTunnelProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 201, 1, 1, 1, 1),
    _HwTunnelProtocol_Type()
)
hwTunnelProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwTunnelProtocol.setStatus("current")


class _HwTunnelSourceType_Type(Integer32):
    """Custom type hwTunnelSourceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("interfaceName", 1),
          ("sourceAddress", 2),
          ("unknown", 3))
    )


_HwTunnelSourceType_Type.__name__ = "Integer32"
_HwTunnelSourceType_Object = MibTableColumn
hwTunnelSourceType = _HwTunnelSourceType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 201, 1, 1, 1, 2),
    _HwTunnelSourceType_Type()
)
hwTunnelSourceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwTunnelSourceType.setStatus("current")
_HwTunnelSrcIfName_Type = DisplayString
_HwTunnelSrcIfName_Object = MibTableColumn
hwTunnelSrcIfName = _HwTunnelSrcIfName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 201, 1, 1, 1, 3),
    _HwTunnelSrcIfName_Type()
)
hwTunnelSrcIfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwTunnelSrcIfName.setStatus("current")
_HwTunnelAddrType_Type = InetAddressType
_HwTunnelAddrType_Object = MibTableColumn
hwTunnelAddrType = _HwTunnelAddrType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 201, 1, 1, 1, 4),
    _HwTunnelAddrType_Type()
)
hwTunnelAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwTunnelAddrType.setStatus("current")
_HwTunnelSourceAddr_Type = InetAddress
_HwTunnelSourceAddr_Object = MibTableColumn
hwTunnelSourceAddr = _HwTunnelSourceAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 201, 1, 1, 1, 5),
    _HwTunnelSourceAddr_Type()
)
hwTunnelSourceAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwTunnelSourceAddr.setStatus("current")
_HwTunnelDestinationAddr_Type = InetAddress
_HwTunnelDestinationAddr_Object = MibTableColumn
hwTunnelDestinationAddr = _HwTunnelDestinationAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 201, 1, 1, 1, 6),
    _HwTunnelDestinationAddr_Type()
)
hwTunnelDestinationAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwTunnelDestinationAddr.setStatus("current")


class _HwTunnelCfgUndoFlag_Type(Integer32):
    """Custom type hwTunnelCfgUndoFlag based on Integer32"""
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
        *(("invalid", 4),
          ("undoTunnelDestination", 3),
          ("undoTunnelProtocol", 1),
          ("undoTunnelSource", 2))
    )


_HwTunnelCfgUndoFlag_Type.__name__ = "Integer32"
_HwTunnelCfgUndoFlag_Object = MibTableColumn
hwTunnelCfgUndoFlag = _HwTunnelCfgUndoFlag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 201, 1, 1, 1, 7),
    _HwTunnelCfgUndoFlag_Type()
)
hwTunnelCfgUndoFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwTunnelCfgUndoFlag.setStatus("current")
_HwIpv6Tunnel4Over6CfgTable_Object = MibTable
hwIpv6Tunnel4Over6CfgTable = _HwIpv6Tunnel4Over6CfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 201, 1, 2)
)
if mibBuilder.loadTexts:
    hwIpv6Tunnel4Over6CfgTable.setStatus("current")
_HwIpv6Tunnel4Over6CfgEntry_Object = MibTableRow
hwIpv6Tunnel4Over6CfgEntry = _HwIpv6Tunnel4Over6CfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 201, 1, 2, 1)
)
hwIpv6Tunnel4Over6CfgEntry.setIndexNames(
    (0, "IPV6-MIB", "ipv6IfIndex"),
)
if mibBuilder.loadTexts:
    hwIpv6Tunnel4Over6CfgEntry.setStatus("current")


class _HwIpv6TunnelEncapLimit_Type(Integer32):
    """Custom type hwIpv6TunnelEncapLimit based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HwIpv6TunnelEncapLimit_Type.__name__ = "Integer32"
_HwIpv6TunnelEncapLimit_Object = MibTableColumn
hwIpv6TunnelEncapLimit = _HwIpv6TunnelEncapLimit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 201, 1, 2, 1, 1),
    _HwIpv6TunnelEncapLimit_Type()
)
hwIpv6TunnelEncapLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIpv6TunnelEncapLimit.setStatus("current")
_HwIpv6TunnelEncapLimitDisable_Type = TruthValue
_HwIpv6TunnelEncapLimitDisable_Object = MibTableColumn
hwIpv6TunnelEncapLimitDisable = _HwIpv6TunnelEncapLimitDisable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 201, 1, 2, 1, 2),
    _HwIpv6TunnelEncapLimitDisable_Type()
)
hwIpv6TunnelEncapLimitDisable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIpv6TunnelEncapLimitDisable.setStatus("current")


class _HwIpv6TunnelFlowLabel_Type(Integer32):
    """Custom type hwIpv6TunnelFlowLabel based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1048575),
    )


_HwIpv6TunnelFlowLabel_Type.__name__ = "Integer32"
_HwIpv6TunnelFlowLabel_Object = MibTableColumn
hwIpv6TunnelFlowLabel = _HwIpv6TunnelFlowLabel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 201, 1, 2, 1, 3),
    _HwIpv6TunnelFlowLabel_Type()
)
hwIpv6TunnelFlowLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIpv6TunnelFlowLabel.setStatus("current")


class _HwIpv6TunnelHopLimit_Type(Integer32):
    """Custom type hwIpv6TunnelHopLimit based on Integer32"""
    defaultValue = 64

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_HwIpv6TunnelHopLimit_Type.__name__ = "Integer32"
_HwIpv6TunnelHopLimit_Object = MibTableColumn
hwIpv6TunnelHopLimit = _HwIpv6TunnelHopLimit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 201, 1, 2, 1, 4),
    _HwIpv6TunnelHopLimit_Type()
)
hwIpv6TunnelHopLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIpv6TunnelHopLimit.setStatus("current")


class _HwIpv6TunnelTrafficClass_Type(Integer32):
    """Custom type hwIpv6TunnelTrafficClass based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HwIpv6TunnelTrafficClass_Type.__name__ = "Integer32"
_HwIpv6TunnelTrafficClass_Object = MibTableColumn
hwIpv6TunnelTrafficClass = _HwIpv6TunnelTrafficClass_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 201, 1, 2, 1, 5),
    _HwIpv6TunnelTrafficClass_Type()
)
hwIpv6TunnelTrafficClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIpv6TunnelTrafficClass.setStatus("current")


class _HwIpv6TunnelTrafficOriginal_Type(TruthValue):
    """Custom type hwIpv6TunnelTrafficOriginal based on TruthValue"""


_HwIpv6TunnelTrafficOriginal_Object = MibTableColumn
hwIpv6TunnelTrafficOriginal = _HwIpv6TunnelTrafficOriginal_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 201, 1, 2, 1, 6),
    _HwIpv6TunnelTrafficOriginal_Type()
)
hwIpv6TunnelTrafficOriginal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIpv6TunnelTrafficOriginal.setStatus("current")


class _HwIPv6Tunnel4Over6CfgUndoFlag_Type(Integer32):
    """Custom type hwIPv6Tunnel4Over6CfgUndoFlag based on Integer32"""
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
        *(("invalid", 5),
          ("undoTunnelEncapLimit", 1),
          ("undoTunnelFlowLabel", 2),
          ("undoTunnelHopLimit", 3),
          ("undoTunnelTrafficClass", 4))
    )


_HwIPv6Tunnel4Over6CfgUndoFlag_Type.__name__ = "Integer32"
_HwIPv6Tunnel4Over6CfgUndoFlag_Object = MibTableColumn
hwIPv6Tunnel4Over6CfgUndoFlag = _HwIPv6Tunnel4Over6CfgUndoFlag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 201, 1, 2, 1, 7),
    _HwIPv6Tunnel4Over6CfgUndoFlag_Type()
)
hwIPv6Tunnel4Over6CfgUndoFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIPv6Tunnel4Over6CfgUndoFlag.setStatus("current")
_HwTunnelMibConformance_ObjectIdentity = ObjectIdentity
hwTunnelMibConformance = _HwTunnelMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 201, 2)
)
_HwTunnelCompliances_ObjectIdentity = ObjectIdentity
hwTunnelCompliances = _HwTunnelCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 201, 2, 1)
)
_HwTunnelGroups_ObjectIdentity = ObjectIdentity
hwTunnelGroups = _HwTunnelGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 201, 2, 2)
)

# Managed Objects groups

hwTunnelGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 201, 2, 2, 1)
)
hwTunnelGroup.setObjects(
      *(("HUAWEI-TUNNEL-MIB", "hwTunnelProtocol"),
        ("HUAWEI-TUNNEL-MIB", "hwTunnelSourceType"),
        ("HUAWEI-TUNNEL-MIB", "hwTunnelSrcIfName"),
        ("HUAWEI-TUNNEL-MIB", "hwTunnelAddrType"),
        ("HUAWEI-TUNNEL-MIB", "hwTunnelSourceAddr"),
        ("HUAWEI-TUNNEL-MIB", "hwTunnelDestinationAddr"),
        ("HUAWEI-TUNNEL-MIB", "hwTunnelCfgUndoFlag"),
        ("HUAWEI-TUNNEL-MIB", "hwIpv6TunnelEncapLimit"),
        ("HUAWEI-TUNNEL-MIB", "hwIpv6TunnelEncapLimitDisable"),
        ("HUAWEI-TUNNEL-MIB", "hwIpv6TunnelFlowLabel"),
        ("HUAWEI-TUNNEL-MIB", "hwIpv6TunnelHopLimit"),
        ("HUAWEI-TUNNEL-MIB", "hwIpv6TunnelTrafficClass"),
        ("HUAWEI-TUNNEL-MIB", "hwIpv6TunnelTrafficOriginal"),
        ("HUAWEI-TUNNEL-MIB", "hwIPv6Tunnel4Over6CfgUndoFlag"))
)
if mibBuilder.loadTexts:
    hwTunnelGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hwTunnelCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 201, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hwTunnelCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-TUNNEL-MIB",
    **{"hwTunnelMib": hwTunnelMib,
       "hwTunnelMibObjects": hwTunnelMibObjects,
       "hwTunnelCfgTable": hwTunnelCfgTable,
       "hwTunnelCfgEntry": hwTunnelCfgEntry,
       "hwTunnelProtocol": hwTunnelProtocol,
       "hwTunnelSourceType": hwTunnelSourceType,
       "hwTunnelSrcIfName": hwTunnelSrcIfName,
       "hwTunnelAddrType": hwTunnelAddrType,
       "hwTunnelSourceAddr": hwTunnelSourceAddr,
       "hwTunnelDestinationAddr": hwTunnelDestinationAddr,
       "hwTunnelCfgUndoFlag": hwTunnelCfgUndoFlag,
       "hwIpv6Tunnel4Over6CfgTable": hwIpv6Tunnel4Over6CfgTable,
       "hwIpv6Tunnel4Over6CfgEntry": hwIpv6Tunnel4Over6CfgEntry,
       "hwIpv6TunnelEncapLimit": hwIpv6TunnelEncapLimit,
       "hwIpv6TunnelEncapLimitDisable": hwIpv6TunnelEncapLimitDisable,
       "hwIpv6TunnelFlowLabel": hwIpv6TunnelFlowLabel,
       "hwIpv6TunnelHopLimit": hwIpv6TunnelHopLimit,
       "hwIpv6TunnelTrafficClass": hwIpv6TunnelTrafficClass,
       "hwIpv6TunnelTrafficOriginal": hwIpv6TunnelTrafficOriginal,
       "hwIPv6Tunnel4Over6CfgUndoFlag": hwIPv6Tunnel4Over6CfgUndoFlag,
       "hwTunnelMibConformance": hwTunnelMibConformance,
       "hwTunnelCompliances": hwTunnelCompliances,
       "hwTunnelCompliance": hwTunnelCompliance,
       "hwTunnelGroups": hwTunnelGroups,
       "hwTunnelGroup": hwTunnelGroup}
)
