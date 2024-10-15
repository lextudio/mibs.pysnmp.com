# SNMP MIB module (HUAWEI-LSP-PING-TRACE-TRAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-LSP-PING-TRACE-TRAP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:04:37 2024
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
 iso,
 mgmt) = mibBuilder.importSymbols(
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
    "iso",
    "mgmt")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

hwLsppttMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 302)
)
hwLsppttMIB.setRevisions(
        ("2014-11-17 19:14",
         "2011-08-07 16:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwLspTrapObject_ObjectIdentity = ObjectIdentity
hwLspTrapObject = _HwLspTrapObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 302, 2)
)
_HwLspTunnelID_Type = Integer32
_HwLspTunnelID_Object = MibScalar
hwLspTunnelID = _HwLspTunnelID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 302, 2, 1),
    _HwLspTunnelID_Type()
)
hwLspTunnelID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwLspTunnelID.setStatus("current")
_HwLspSenderAddress_Type = Integer32
_HwLspSenderAddress_Object = MibScalar
hwLspSenderAddress = _HwLspSenderAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 302, 2, 2),
    _HwLspSenderAddress_Type()
)
hwLspSenderAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwLspSenderAddress.setStatus("current")
_HwLspEndPointAddress_Type = Integer32
_HwLspEndPointAddress_Object = MibScalar
hwLspEndPointAddress = _HwLspEndPointAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 302, 2, 3),
    _HwLspEndPointAddress_Type()
)
hwLspEndPointAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwLspEndPointAddress.setStatus("current")
_HwLspTTL_Type = Integer32
_HwLspTTL_Object = MibScalar
hwLspTTL = _HwLspTTL_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 302, 2, 4),
    _HwLspTTL_Type()
)
hwLspTTL.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwLspTTL.setStatus("current")
_HwLspHandle_Type = Integer32
_HwLspHandle_Object = MibScalar
hwLspHandle = _HwLspHandle_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 302, 2, 5),
    _HwLspHandle_Type()
)
hwLspHandle.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwLspHandle.setStatus("current")


class _HwLspIPv4VpnName_Type(OctetString):
    """Custom type hwLspIPv4VpnName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_HwLspIPv4VpnName_Type.__name__ = "OctetString"
_HwLspIPv4VpnName_Object = MibScalar
hwLspIPv4VpnName = _HwLspIPv4VpnName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 302, 2, 6),
    _HwLspIPv4VpnName_Type()
)
hwLspIPv4VpnName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwLspIPv4VpnName.setStatus("current")
_HwLspIPv4VpnSrcAddr_Type = Integer32
_HwLspIPv4VpnSrcAddr_Object = MibScalar
hwLspIPv4VpnSrcAddr = _HwLspIPv4VpnSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 302, 2, 7),
    _HwLspIPv4VpnSrcAddr_Type()
)
hwLspIPv4VpnSrcAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwLspIPv4VpnSrcAddr.setStatus("current")
_HwLspIPv4VpnDstAddr_Type = Integer32
_HwLspIPv4VpnDstAddr_Object = MibScalar
hwLspIPv4VpnDstAddr = _HwLspIPv4VpnDstAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 302, 2, 8),
    _HwLspIPv4VpnDstAddr_Type()
)
hwLspIPv4VpnDstAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwLspIPv4VpnDstAddr.setStatus("current")
_HwLspNotifications_ObjectIdentity = ObjectIdentity
hwLspNotifications = _HwLspNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 302, 3)
)
_HwLspConformance_ObjectIdentity = ObjectIdentity
hwLspConformance = _HwLspConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 302, 4)
)
_HwLspGroup_ObjectIdentity = ObjectIdentity
hwLspGroup = _HwLspGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 302, 4, 1)
)
_HwLspCompliances_ObjectIdentity = ObjectIdentity
hwLspCompliances = _HwLspCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 302, 4, 2)
)

# Managed Objects groups

hwLspObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 302, 4, 1, 2)
)
hwLspObjectGroup.setObjects(
      *(("HUAWEI-LSP-PING-TRACE-TRAP-MIB", "hwLspTunnelID"),
        ("HUAWEI-LSP-PING-TRACE-TRAP-MIB", "hwLspTTL"),
        ("HUAWEI-LSP-PING-TRACE-TRAP-MIB", "hwLspHandle"),
        ("HUAWEI-LSP-PING-TRACE-TRAP-MIB", "hwLspSenderAddress"),
        ("HUAWEI-LSP-PING-TRACE-TRAP-MIB", "hwLspEndPointAddress"),
        ("HUAWEI-LSP-PING-TRACE-TRAP-MIB", "hwLspIPv4VpnName"),
        ("HUAWEI-LSP-PING-TRACE-TRAP-MIB", "hwLspIPv4VpnSrcAddr"),
        ("HUAWEI-LSP-PING-TRACE-TRAP-MIB", "hwLspIPv4VpnDstAddr"))
)
if mibBuilder.loadTexts:
    hwLspObjectGroup.setStatus("current")


# Notification objects

hwLspPingProbe = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 302, 3, 1)
)
hwLspPingProbe.setObjects(
      *(("HUAWEI-LSP-PING-TRACE-TRAP-MIB", "hwLspTunnelID"),
        ("HUAWEI-LSP-PING-TRACE-TRAP-MIB", "hwLspSenderAddress"),
        ("HUAWEI-LSP-PING-TRACE-TRAP-MIB", "hwLspEndPointAddress"),
        ("HUAWEI-LSP-PING-TRACE-TRAP-MIB", "hwLspTTL"),
        ("HUAWEI-LSP-PING-TRACE-TRAP-MIB", "hwLspHandle"))
)
if mibBuilder.loadTexts:
    hwLspPingProbe.setStatus(
        "current"
    )

hwLspTraceProbe = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 302, 3, 2)
)
hwLspTraceProbe.setObjects(
      *(("HUAWEI-LSP-PING-TRACE-TRAP-MIB", "hwLspTunnelID"),
        ("HUAWEI-LSP-PING-TRACE-TRAP-MIB", "hwLspSenderAddress"),
        ("HUAWEI-LSP-PING-TRACE-TRAP-MIB", "hwLspEndPointAddress"),
        ("HUAWEI-LSP-PING-TRACE-TRAP-MIB", "hwLspTTL"),
        ("HUAWEI-LSP-PING-TRACE-TRAP-MIB", "hwLspHandle"))
)
if mibBuilder.loadTexts:
    hwLspTraceProbe.setStatus(
        "current"
    )

hwLspPingIPv4VpnProbe = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 302, 3, 3)
)
hwLspPingIPv4VpnProbe.setObjects(
      *(("HUAWEI-LSP-PING-TRACE-TRAP-MIB", "hwLspIPv4VpnName"),
        ("HUAWEI-LSP-PING-TRACE-TRAP-MIB", "hwLspIPv4VpnSrcAddr"),
        ("HUAWEI-LSP-PING-TRACE-TRAP-MIB", "hwLspIPv4VpnDstAddr"),
        ("HUAWEI-LSP-PING-TRACE-TRAP-MIB", "hwLspTTL"),
        ("HUAWEI-LSP-PING-TRACE-TRAP-MIB", "hwLspHandle"))
)
if mibBuilder.loadTexts:
    hwLspPingIPv4VpnProbe.setStatus(
        "current"
    )


# Notifications groups

hwLspNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 302, 4, 1, 1)
)
hwLspNotificationsGroup.setObjects(
      *(("HUAWEI-LSP-PING-TRACE-TRAP-MIB", "hwLspPingProbe"),
        ("HUAWEI-LSP-PING-TRACE-TRAP-MIB", "hwLspTraceProbe"),
        ("HUAWEI-LSP-PING-TRACE-TRAP-MIB", "hwLspPingIPv4VpnProbe"))
)
if mibBuilder.loadTexts:
    hwLspNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hwLspCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 302, 4, 2, 1)
)
if mibBuilder.loadTexts:
    hwLspCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-LSP-PING-TRACE-TRAP-MIB",
    **{"hwLsppttMIB": hwLsppttMIB,
       "hwLspTrapObject": hwLspTrapObject,
       "hwLspTunnelID": hwLspTunnelID,
       "hwLspSenderAddress": hwLspSenderAddress,
       "hwLspEndPointAddress": hwLspEndPointAddress,
       "hwLspTTL": hwLspTTL,
       "hwLspHandle": hwLspHandle,
       "hwLspIPv4VpnName": hwLspIPv4VpnName,
       "hwLspIPv4VpnSrcAddr": hwLspIPv4VpnSrcAddr,
       "hwLspIPv4VpnDstAddr": hwLspIPv4VpnDstAddr,
       "hwLspNotifications": hwLspNotifications,
       "hwLspPingProbe": hwLspPingProbe,
       "hwLspTraceProbe": hwLspTraceProbe,
       "hwLspPingIPv4VpnProbe": hwLspPingIPv4VpnProbe,
       "hwLspConformance": hwLspConformance,
       "hwLspGroup": hwLspGroup,
       "hwLspNotificationsGroup": hwLspNotificationsGroup,
       "hwLspObjectGroup": hwLspObjectGroup,
       "hwLspCompliances": hwLspCompliances,
       "hwLspCompliance": hwLspCompliance}
)
