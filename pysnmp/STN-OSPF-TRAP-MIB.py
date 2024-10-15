# SNMP MIB module (STN-OSPF-TRAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/STN-OSPF-TRAP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:58:11 2024
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

(ospf,
 ospfAddressLessIf,
 ospfExtLsdbLimit,
 ospfIfIpAddress,
 ospfIfState,
 ospfLsdbAreaId,
 ospfLsdbLsid,
 ospfLsdbRouterId,
 ospfLsdbType,
 ospfNbrAddressLessIndex,
 ospfNbrIpAddr,
 ospfNbrRtrId,
 ospfNbrState,
 ospfRouterId,
 ospfVirtIfAreaId,
 ospfVirtIfNeighbor,
 ospfVirtIfState,
 ospfVirtNbrArea,
 ospfVirtNbrRtrId,
 ospfVirtNbrState) = mibBuilder.importSymbols(
    "OSPF-MIB",
    "ospf",
    "ospfAddressLessIf",
    "ospfExtLsdbLimit",
    "ospfIfIpAddress",
    "ospfIfState",
    "ospfLsdbAreaId",
    "ospfLsdbLsid",
    "ospfLsdbRouterId",
    "ospfLsdbType",
    "ospfNbrAddressLessIndex",
    "ospfNbrIpAddr",
    "ospfNbrRtrId",
    "ospfNbrState",
    "ospfRouterId",
    "ospfVirtIfAreaId",
    "ospfVirtIfNeighbor",
    "ospfVirtIfState",
    "ospfVirtNbrArea",
    "ospfVirtNbrRtrId",
    "ospfVirtNbrState")

(ospfConfigErrorType,
 ospfPacketSrc,
 ospfPacketType) = mibBuilder.importSymbols(
    "OSPF-TRAP-MIB",
    "ospfConfigErrorType",
    "ospfPacketSrc",
    "ospfPacketType")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(stnNotification,) = mibBuilder.importSymbols(
    "SPRING-TIDE-NETWORKS-SMI",
    "stnNotification")

(stnOspfTraps,) = mibBuilder.importSymbols(
    "STN-IPROUTING-MIB",
    "stnOspfTraps")

(stnRouterIndex,) = mibBuilder.importSymbols(
    "STN-ROUTER-MIB",
    "stnRouterIndex")


# MODULE-IDENTITY

stnOspfTrap = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 12, 4, 8, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_StnOspfTrapVars_ObjectIdentity = ObjectIdentity
stnOspfTrapVars = _StnOspfTrapVars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 12, 4, 8, 1, 1)
)
_StnOspfNotificationPrefix_ObjectIdentity = ObjectIdentity
stnOspfNotificationPrefix = _StnOspfNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 12, 4, 8, 1, 2)
)
_StnOspfNotification_ObjectIdentity = ObjectIdentity
stnOspfNotification = _StnOspfNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 12, 4, 8, 1, 2, 0)
)

# Managed Objects groups


# Notification objects

stnOspfVirtIfStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 3551, 2, 12, 4, 8, 1, 2, 0, 1)
)
stnOspfVirtIfStateChange.setObjects(
      *(("STN-ROUTER-MIB", "stnRouterIndex"),
        ("OSPF-MIB", "ospfRouterId"),
        ("OSPF-MIB", "ospfVirtIfAreaId"),
        ("OSPF-MIB", "ospfVirtIfNeighbor"),
        ("OSPF-MIB", "ospfVirtIfState"))
)
if mibBuilder.loadTexts:
    stnOspfVirtIfStateChange.setStatus(
        "current"
    )

stnOspfNbrStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 3551, 2, 12, 4, 8, 1, 2, 0, 2)
)
stnOspfNbrStateChange.setObjects(
      *(("STN-ROUTER-MIB", "stnRouterIndex"),
        ("OSPF-MIB", "ospfRouterId"),
        ("OSPF-MIB", "ospfNbrIpAddr"),
        ("OSPF-MIB", "ospfNbrAddressLessIndex"),
        ("OSPF-MIB", "ospfNbrRtrId"),
        ("OSPF-MIB", "ospfNbrState"))
)
if mibBuilder.loadTexts:
    stnOspfNbrStateChange.setStatus(
        "current"
    )

stnOspfVirtNbrStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 3551, 2, 12, 4, 8, 1, 2, 0, 3)
)
stnOspfVirtNbrStateChange.setObjects(
      *(("STN-ROUTER-MIB", "stnRouterIndex"),
        ("OSPF-MIB", "ospfRouterId"),
        ("OSPF-MIB", "ospfVirtNbrArea"),
        ("OSPF-MIB", "ospfVirtNbrRtrId"),
        ("OSPF-MIB", "ospfVirtNbrState"))
)
if mibBuilder.loadTexts:
    stnOspfVirtNbrStateChange.setStatus(
        "current"
    )

stnOspfIfConfigError = NotificationType(
    (1, 3, 6, 1, 4, 1, 3551, 2, 12, 4, 8, 1, 2, 0, 4)
)
stnOspfIfConfigError.setObjects(
      *(("STN-ROUTER-MIB", "stnRouterIndex"),
        ("OSPF-MIB", "ospfRouterId"),
        ("OSPF-MIB", "ospfIfIpAddress"),
        ("OSPF-MIB", "ospfAddressLessIf"),
        ("OSPF-TRAP-MIB", "ospfPacketSrc"),
        ("OSPF-TRAP-MIB", "ospfConfigErrorType"),
        ("OSPF-TRAP-MIB", "ospfPacketType"))
)
if mibBuilder.loadTexts:
    stnOspfIfConfigError.setStatus(
        "current"
    )

stnOspfVirtIfConfigError = NotificationType(
    (1, 3, 6, 1, 4, 1, 3551, 2, 12, 4, 8, 1, 2, 0, 5)
)
stnOspfVirtIfConfigError.setObjects(
      *(("STN-ROUTER-MIB", "stnRouterIndex"),
        ("OSPF-MIB", "ospfRouterId"),
        ("OSPF-MIB", "ospfVirtIfAreaId"),
        ("OSPF-MIB", "ospfVirtIfNeighbor"),
        ("OSPF-TRAP-MIB", "ospfConfigErrorType"),
        ("OSPF-TRAP-MIB", "ospfPacketType"))
)
if mibBuilder.loadTexts:
    stnOspfVirtIfConfigError.setStatus(
        "current"
    )

stnOspfIfAuthFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3551, 2, 12, 4, 8, 1, 2, 0, 6)
)
stnOspfIfAuthFailure.setObjects(
      *(("STN-ROUTER-MIB", "stnRouterIndex"),
        ("OSPF-MIB", "ospfRouterId"),
        ("OSPF-MIB", "ospfIfIpAddress"),
        ("OSPF-MIB", "ospfAddressLessIf"),
        ("OSPF-TRAP-MIB", "ospfPacketSrc"),
        ("OSPF-TRAP-MIB", "ospfConfigErrorType"),
        ("OSPF-TRAP-MIB", "ospfPacketType"))
)
if mibBuilder.loadTexts:
    stnOspfIfAuthFailure.setStatus(
        "current"
    )

stnOspfVirtIfAuthFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3551, 2, 12, 4, 8, 1, 2, 0, 7)
)
stnOspfVirtIfAuthFailure.setObjects(
      *(("STN-ROUTER-MIB", "stnRouterIndex"),
        ("OSPF-MIB", "ospfRouterId"),
        ("OSPF-MIB", "ospfVirtIfAreaId"),
        ("OSPF-MIB", "ospfVirtIfNeighbor"),
        ("OSPF-TRAP-MIB", "ospfConfigErrorType"),
        ("OSPF-TRAP-MIB", "ospfPacketType"))
)
if mibBuilder.loadTexts:
    stnOspfVirtIfAuthFailure.setStatus(
        "current"
    )

stnOspfIfRxBadPacket = NotificationType(
    (1, 3, 6, 1, 4, 1, 3551, 2, 12, 4, 8, 1, 2, 0, 8)
)
stnOspfIfRxBadPacket.setObjects(
      *(("STN-ROUTER-MIB", "stnRouterIndex"),
        ("OSPF-MIB", "ospfRouterId"),
        ("OSPF-MIB", "ospfIfIpAddress"),
        ("OSPF-MIB", "ospfAddressLessIf"),
        ("OSPF-TRAP-MIB", "ospfPacketSrc"),
        ("OSPF-TRAP-MIB", "ospfPacketType"))
)
if mibBuilder.loadTexts:
    stnOspfIfRxBadPacket.setStatus(
        "current"
    )

stnOspfVirtIfRxBadPacket = NotificationType(
    (1, 3, 6, 1, 4, 1, 3551, 2, 12, 4, 8, 1, 2, 0, 9)
)
stnOspfVirtIfRxBadPacket.setObjects(
      *(("STN-ROUTER-MIB", "stnRouterIndex"),
        ("OSPF-MIB", "ospfRouterId"),
        ("OSPF-MIB", "ospfVirtIfAreaId"),
        ("OSPF-MIB", "ospfVirtIfNeighbor"),
        ("OSPF-TRAP-MIB", "ospfPacketType"))
)
if mibBuilder.loadTexts:
    stnOspfVirtIfRxBadPacket.setStatus(
        "current"
    )

stnOspfTxRetransmit = NotificationType(
    (1, 3, 6, 1, 4, 1, 3551, 2, 12, 4, 8, 1, 2, 0, 10)
)
stnOspfTxRetransmit.setObjects(
      *(("STN-ROUTER-MIB", "stnRouterIndex"),
        ("OSPF-MIB", "ospfRouterId"),
        ("OSPF-MIB", "ospfIfIpAddress"),
        ("OSPF-MIB", "ospfAddressLessIf"),
        ("OSPF-MIB", "ospfNbrRtrId"),
        ("OSPF-TRAP-MIB", "ospfPacketType"),
        ("OSPF-MIB", "ospfLsdbType"),
        ("OSPF-MIB", "ospfLsdbLsid"),
        ("OSPF-MIB", "ospfLsdbRouterId"))
)
if mibBuilder.loadTexts:
    stnOspfTxRetransmit.setStatus(
        "current"
    )

stnOspfVirtIfTxRetransmit = NotificationType(
    (1, 3, 6, 1, 4, 1, 3551, 2, 12, 4, 8, 1, 2, 0, 11)
)
stnOspfVirtIfTxRetransmit.setObjects(
      *(("STN-ROUTER-MIB", "stnRouterIndex"),
        ("OSPF-MIB", "ospfRouterId"),
        ("OSPF-MIB", "ospfVirtIfAreaId"),
        ("OSPF-MIB", "ospfVirtIfNeighbor"),
        ("OSPF-TRAP-MIB", "ospfPacketType"),
        ("OSPF-MIB", "ospfLsdbType"),
        ("OSPF-MIB", "ospfLsdbLsid"),
        ("OSPF-MIB", "ospfLsdbRouterId"))
)
if mibBuilder.loadTexts:
    stnOspfVirtIfTxRetransmit.setStatus(
        "current"
    )

stnOspfOriginateLsa = NotificationType(
    (1, 3, 6, 1, 4, 1, 3551, 2, 12, 4, 8, 1, 2, 0, 12)
)
stnOspfOriginateLsa.setObjects(
      *(("STN-ROUTER-MIB", "stnRouterIndex"),
        ("OSPF-MIB", "ospfRouterId"),
        ("OSPF-MIB", "ospfLsdbAreaId"),
        ("OSPF-MIB", "ospfLsdbType"),
        ("OSPF-MIB", "ospfLsdbLsid"),
        ("OSPF-MIB", "ospfLsdbRouterId"))
)
if mibBuilder.loadTexts:
    stnOspfOriginateLsa.setStatus(
        "current"
    )

stnOspfMaxAgeLsa = NotificationType(
    (1, 3, 6, 1, 4, 1, 3551, 2, 12, 4, 8, 1, 2, 0, 13)
)
stnOspfMaxAgeLsa.setObjects(
      *(("STN-ROUTER-MIB", "stnRouterIndex"),
        ("OSPF-MIB", "ospfRouterId"),
        ("OSPF-MIB", "ospfLsdbAreaId"),
        ("OSPF-MIB", "ospfLsdbType"),
        ("OSPF-MIB", "ospfLsdbLsid"),
        ("OSPF-MIB", "ospfLsdbRouterId"))
)
if mibBuilder.loadTexts:
    stnOspfMaxAgeLsa.setStatus(
        "current"
    )

stnOspfLsdbOverflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 3551, 2, 12, 4, 8, 1, 2, 0, 14)
)
stnOspfLsdbOverflow.setObjects(
      *(("STN-ROUTER-MIB", "stnRouterIndex"),
        ("OSPF-MIB", "ospfRouterId"),
        ("OSPF-MIB", "ospfExtLsdbLimit"))
)
if mibBuilder.loadTexts:
    stnOspfLsdbOverflow.setStatus(
        "current"
    )

stnOspfLsdbApproachingOverflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 3551, 2, 12, 4, 8, 1, 2, 0, 15)
)
stnOspfLsdbApproachingOverflow.setObjects(
      *(("STN-ROUTER-MIB", "stnRouterIndex"),
        ("OSPF-MIB", "ospfRouterId"),
        ("OSPF-MIB", "ospfExtLsdbLimit"))
)
if mibBuilder.loadTexts:
    stnOspfLsdbApproachingOverflow.setStatus(
        "current"
    )

stnOspfIfStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 3551, 2, 12, 4, 8, 1, 2, 0, 16)
)
stnOspfIfStateChange.setObjects(
      *(("STN-ROUTER-MIB", "stnRouterIndex"),
        ("OSPF-MIB", "ospfRouterId"),
        ("OSPF-MIB", "ospfIfIpAddress"),
        ("OSPF-MIB", "ospfAddressLessIf"),
        ("OSPF-MIB", "ospfIfState"))
)
if mibBuilder.loadTexts:
    stnOspfIfStateChange.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "STN-OSPF-TRAP-MIB",
    **{"stnOspfTrap": stnOspfTrap,
       "stnOspfTrapVars": stnOspfTrapVars,
       "stnOspfNotificationPrefix": stnOspfNotificationPrefix,
       "stnOspfNotification": stnOspfNotification,
       "stnOspfVirtIfStateChange": stnOspfVirtIfStateChange,
       "stnOspfNbrStateChange": stnOspfNbrStateChange,
       "stnOspfVirtNbrStateChange": stnOspfVirtNbrStateChange,
       "stnOspfIfConfigError": stnOspfIfConfigError,
       "stnOspfVirtIfConfigError": stnOspfVirtIfConfigError,
       "stnOspfIfAuthFailure": stnOspfIfAuthFailure,
       "stnOspfVirtIfAuthFailure": stnOspfVirtIfAuthFailure,
       "stnOspfIfRxBadPacket": stnOspfIfRxBadPacket,
       "stnOspfVirtIfRxBadPacket": stnOspfVirtIfRxBadPacket,
       "stnOspfTxRetransmit": stnOspfTxRetransmit,
       "stnOspfVirtIfTxRetransmit": stnOspfVirtIfTxRetransmit,
       "stnOspfOriginateLsa": stnOspfOriginateLsa,
       "stnOspfMaxAgeLsa": stnOspfMaxAgeLsa,
       "stnOspfLsdbOverflow": stnOspfLsdbOverflow,
       "stnOspfLsdbApproachingOverflow": stnOspfLsdbApproachingOverflow,
       "stnOspfIfStateChange": stnOspfIfStateChange}
)
