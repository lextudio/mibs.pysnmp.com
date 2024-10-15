# SNMP MIB module (NETSCREEN-OSPF-TRAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NETSCREEN-OSPF-TRAP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:26:49 2024
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

(nsOspf,
 nsOspfAddressLessIf,
 nsOspfExtLsdbLimit,
 nsOspfIfIpAddress,
 nsOspfIfState,
 nsOspfIfVRID,
 nsOspfLsdbAreaId,
 nsOspfLsdbLsid,
 nsOspfLsdbRouterId,
 nsOspfLsdbType,
 nsOspfLsdbVRID,
 nsOspfNbrAddressLessIndex,
 nsOspfNbrIpAddr,
 nsOspfNbrRtrId,
 nsOspfNbrState,
 nsOspfNbrVRID,
 nsOspfRouterId,
 nsOspfVirtIfAreaId,
 nsOspfVirtIfNeighbor,
 nsOspfVirtIfState,
 nsOspfVirtIfVRID,
 nsOspfVirtNbrArea,
 nsOspfVirtNbrRtrId,
 nsOspfVirtNbrState,
 nsOspfVirtNbrVRID) = mibBuilder.importSymbols(
    "NETSCREEN-OSPF-MIB",
    "nsOspf",
    "nsOspfAddressLessIf",
    "nsOspfExtLsdbLimit",
    "nsOspfIfIpAddress",
    "nsOspfIfState",
    "nsOspfIfVRID",
    "nsOspfLsdbAreaId",
    "nsOspfLsdbLsid",
    "nsOspfLsdbRouterId",
    "nsOspfLsdbType",
    "nsOspfLsdbVRID",
    "nsOspfNbrAddressLessIndex",
    "nsOspfNbrIpAddr",
    "nsOspfNbrRtrId",
    "nsOspfNbrState",
    "nsOspfNbrVRID",
    "nsOspfRouterId",
    "nsOspfVirtIfAreaId",
    "nsOspfVirtIfNeighbor",
    "nsOspfVirtIfState",
    "nsOspfVirtIfVRID",
    "nsOspfVirtNbrArea",
    "nsOspfVirtNbrRtrId",
    "nsOspfVirtNbrState",
    "nsOspfVirtNbrVRID")

(netscreenTrapDesc,
 netscreenTrapType) = mibBuilder.importSymbols(
    "NETSCREEN-TRAP-MIB",
    "netscreenTrapDesc",
    "netscreenTrapType")

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


# MODULE-IDENTITY

nsOspfTrap = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 16)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NsOspfTrapControl_ObjectIdentity = ObjectIdentity
nsOspfTrapControl = _NsOspfTrapControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 16, 1)
)


class _NsOspfSetTrap_Type(OctetString):
    """Custom type nsOspfSetTrap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_NsOspfSetTrap_Type.__name__ = "OctetString"
_NsOspfSetTrap_Object = MibScalar
nsOspfSetTrap = _NsOspfSetTrap_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 16, 1, 1),
    _NsOspfSetTrap_Type()
)
nsOspfSetTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsOspfSetTrap.setStatus("current")


class _NsOspfConfigErrorType_Type(Integer32):
    """Custom type nsOspfConfigErrorType based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("areaMismatch", 2),
          ("authFailure", 6),
          ("authTypeMismatch", 5),
          ("badVersion", 1),
          ("deadIntervalMismatch", 9),
          ("helloIntervalMismatch", 8),
          ("netMaskMismatch", 7),
          ("optionMismatch", 10),
          ("unknownNbmaNbr", 3),
          ("unknownVirtualNbr", 4))
    )


_NsOspfConfigErrorType_Type.__name__ = "Integer32"
_NsOspfConfigErrorType_Object = MibScalar
nsOspfConfigErrorType = _NsOspfConfigErrorType_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 16, 1, 2),
    _NsOspfConfigErrorType_Type()
)
nsOspfConfigErrorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsOspfConfigErrorType.setStatus("current")


class _NsOspfPacketType_Type(Integer32):
    """Custom type nsOspfPacketType based on Integer32"""
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
        *(("dbDescript", 2),
          ("hello", 1),
          ("lsAck", 5),
          ("lsReq", 3),
          ("lsUpdate", 4))
    )


_NsOspfPacketType_Type.__name__ = "Integer32"
_NsOspfPacketType_Object = MibScalar
nsOspfPacketType = _NsOspfPacketType_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 16, 1, 3),
    _NsOspfPacketType_Type()
)
nsOspfPacketType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsOspfPacketType.setStatus("current")
_NsOspfPacketSrc_Type = IpAddress
_NsOspfPacketSrc_Object = MibScalar
nsOspfPacketSrc = _NsOspfPacketSrc_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 16, 1, 4),
    _NsOspfPacketSrc_Type()
)
nsOspfPacketSrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsOspfPacketSrc.setStatus("current")
_NsOspfTraps_ObjectIdentity = ObjectIdentity
nsOspfTraps = _NsOspfTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 16, 2)
)

# Managed Objects groups


# Notification objects

nsOspfVirtIfStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 16, 2, 1)
)
nsOspfVirtIfStateChange.setObjects(
      *(("NETSCREEN-TRAP-MIB", "netscreenTrapType"),
        ("NETSCREEN-TRAP-MIB", "netscreenTrapDesc"),
        ("NETSCREEN-OSPF-MIB", "nsOspfRouterId"),
        ("NETSCREEN-OSPF-MIB", "nsOspfVirtIfAreaId"),
        ("NETSCREEN-OSPF-MIB", "nsOspfVirtIfNeighbor"),
        ("NETSCREEN-OSPF-MIB", "nsOspfVirtIfState"),
        ("NETSCREEN-OSPF-MIB", "nsOspfVirtIfVRID"))
)
if mibBuilder.loadTexts:
    nsOspfVirtIfStateChange.setStatus(
        "current"
    )

nsOspfNbrStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 16, 2, 2)
)
nsOspfNbrStateChange.setObjects(
      *(("NETSCREEN-TRAP-MIB", "netscreenTrapType"),
        ("NETSCREEN-TRAP-MIB", "netscreenTrapDesc"),
        ("NETSCREEN-OSPF-MIB", "nsOspfRouterId"),
        ("NETSCREEN-OSPF-MIB", "nsOspfNbrIpAddr"),
        ("NETSCREEN-OSPF-MIB", "nsOspfNbrAddressLessIndex"),
        ("NETSCREEN-OSPF-MIB", "nsOspfNbrRtrId"),
        ("NETSCREEN-OSPF-MIB", "nsOspfNbrState"),
        ("NETSCREEN-OSPF-MIB", "nsOspfNbrVRID"))
)
if mibBuilder.loadTexts:
    nsOspfNbrStateChange.setStatus(
        "current"
    )

nsOspfVirtNbrStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 16, 2, 3)
)
nsOspfVirtNbrStateChange.setObjects(
      *(("NETSCREEN-TRAP-MIB", "netscreenTrapType"),
        ("NETSCREEN-TRAP-MIB", "netscreenTrapDesc"),
        ("NETSCREEN-OSPF-MIB", "nsOspfRouterId"),
        ("NETSCREEN-OSPF-MIB", "nsOspfVirtNbrArea"),
        ("NETSCREEN-OSPF-MIB", "nsOspfVirtNbrRtrId"),
        ("NETSCREEN-OSPF-MIB", "nsOspfVirtNbrState"),
        ("NETSCREEN-OSPF-MIB", "nsOspfVirtNbrVRID"))
)
if mibBuilder.loadTexts:
    nsOspfVirtNbrStateChange.setStatus(
        "current"
    )

nsOspfIfConfigError = NotificationType(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 16, 2, 4)
)
nsOspfIfConfigError.setObjects(
      *(("NETSCREEN-TRAP-MIB", "netscreenTrapType"),
        ("NETSCREEN-TRAP-MIB", "netscreenTrapDesc"),
        ("NETSCREEN-OSPF-MIB", "nsOspfRouterId"),
        ("NETSCREEN-OSPF-MIB", "nsOspfIfIpAddress"),
        ("NETSCREEN-OSPF-MIB", "nsOspfAddressLessIf"),
        ("NETSCREEN-OSPF-TRAP-MIB", "nsOspfPacketSrc"),
        ("NETSCREEN-OSPF-TRAP-MIB", "nsOspfConfigErrorType"),
        ("NETSCREEN-OSPF-TRAP-MIB", "nsOspfPacketType"),
        ("NETSCREEN-OSPF-MIB", "nsOspfIfVRID"))
)
if mibBuilder.loadTexts:
    nsOspfIfConfigError.setStatus(
        "current"
    )

nsOspfVirtIfConfigError = NotificationType(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 16, 2, 5)
)
nsOspfVirtIfConfigError.setObjects(
      *(("NETSCREEN-TRAP-MIB", "netscreenTrapType"),
        ("NETSCREEN-TRAP-MIB", "netscreenTrapDesc"),
        ("NETSCREEN-OSPF-MIB", "nsOspfRouterId"),
        ("NETSCREEN-OSPF-MIB", "nsOspfVirtIfAreaId"),
        ("NETSCREEN-OSPF-MIB", "nsOspfVirtIfNeighbor"),
        ("NETSCREEN-OSPF-TRAP-MIB", "nsOspfConfigErrorType"),
        ("NETSCREEN-OSPF-TRAP-MIB", "nsOspfPacketType"),
        ("NETSCREEN-OSPF-MIB", "nsOspfVirtIfVRID"))
)
if mibBuilder.loadTexts:
    nsOspfVirtIfConfigError.setStatus(
        "current"
    )

nsOspfIfAuthFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 16, 2, 6)
)
nsOspfIfAuthFailure.setObjects(
      *(("NETSCREEN-TRAP-MIB", "netscreenTrapType"),
        ("NETSCREEN-TRAP-MIB", "netscreenTrapDesc"),
        ("NETSCREEN-OSPF-MIB", "nsOspfRouterId"),
        ("NETSCREEN-OSPF-MIB", "nsOspfIfIpAddress"),
        ("NETSCREEN-OSPF-MIB", "nsOspfAddressLessIf"),
        ("NETSCREEN-OSPF-TRAP-MIB", "nsOspfPacketSrc"),
        ("NETSCREEN-OSPF-TRAP-MIB", "nsOspfConfigErrorType"),
        ("NETSCREEN-OSPF-TRAP-MIB", "nsOspfPacketType"),
        ("NETSCREEN-OSPF-MIB", "nsOspfIfVRID"))
)
if mibBuilder.loadTexts:
    nsOspfIfAuthFailure.setStatus(
        "current"
    )

nsOspfVirtIfAuthFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 16, 2, 7)
)
nsOspfVirtIfAuthFailure.setObjects(
      *(("NETSCREEN-TRAP-MIB", "netscreenTrapType"),
        ("NETSCREEN-TRAP-MIB", "netscreenTrapDesc"),
        ("NETSCREEN-OSPF-MIB", "nsOspfRouterId"),
        ("NETSCREEN-OSPF-MIB", "nsOspfVirtIfAreaId"),
        ("NETSCREEN-OSPF-MIB", "nsOspfVirtIfNeighbor"),
        ("NETSCREEN-OSPF-TRAP-MIB", "nsOspfConfigErrorType"),
        ("NETSCREEN-OSPF-TRAP-MIB", "nsOspfPacketType"),
        ("NETSCREEN-OSPF-MIB", "nsOspfVirtIfVRID"))
)
if mibBuilder.loadTexts:
    nsOspfVirtIfAuthFailure.setStatus(
        "current"
    )

nsOspfIfRxBadPacket = NotificationType(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 16, 2, 8)
)
nsOspfIfRxBadPacket.setObjects(
      *(("NETSCREEN-TRAP-MIB", "netscreenTrapType"),
        ("NETSCREEN-TRAP-MIB", "netscreenTrapDesc"),
        ("NETSCREEN-OSPF-MIB", "nsOspfRouterId"),
        ("NETSCREEN-OSPF-MIB", "nsOspfIfIpAddress"),
        ("NETSCREEN-OSPF-MIB", "nsOspfAddressLessIf"),
        ("NETSCREEN-OSPF-TRAP-MIB", "nsOspfPacketSrc"),
        ("NETSCREEN-OSPF-TRAP-MIB", "nsOspfPacketType"),
        ("NETSCREEN-OSPF-MIB", "nsOspfIfVRID"))
)
if mibBuilder.loadTexts:
    nsOspfIfRxBadPacket.setStatus(
        "current"
    )

nsOspfVirtIfRxBadPacket = NotificationType(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 16, 2, 9)
)
nsOspfVirtIfRxBadPacket.setObjects(
      *(("NETSCREEN-TRAP-MIB", "netscreenTrapType"),
        ("NETSCREEN-TRAP-MIB", "netscreenTrapDesc"),
        ("NETSCREEN-OSPF-MIB", "nsOspfRouterId"),
        ("NETSCREEN-OSPF-MIB", "nsOspfVirtIfAreaId"),
        ("NETSCREEN-OSPF-MIB", "nsOspfVirtIfNeighbor"),
        ("NETSCREEN-OSPF-TRAP-MIB", "nsOspfPacketType"),
        ("NETSCREEN-OSPF-MIB", "nsOspfVirtIfVRID"))
)
if mibBuilder.loadTexts:
    nsOspfVirtIfRxBadPacket.setStatus(
        "current"
    )

nsOspfTxRetransmit = NotificationType(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 16, 2, 10)
)
nsOspfTxRetransmit.setObjects(
      *(("NETSCREEN-TRAP-MIB", "netscreenTrapType"),
        ("NETSCREEN-TRAP-MIB", "netscreenTrapDesc"),
        ("NETSCREEN-OSPF-MIB", "nsOspfRouterId"),
        ("NETSCREEN-OSPF-MIB", "nsOspfIfIpAddress"),
        ("NETSCREEN-OSPF-MIB", "nsOspfAddressLessIf"),
        ("NETSCREEN-OSPF-MIB", "nsOspfNbrRtrId"),
        ("NETSCREEN-OSPF-TRAP-MIB", "nsOspfPacketType"),
        ("NETSCREEN-OSPF-MIB", "nsOspfLsdbType"),
        ("NETSCREEN-OSPF-MIB", "nsOspfLsdbLsid"),
        ("NETSCREEN-OSPF-MIB", "nsOspfLsdbRouterId"),
        ("NETSCREEN-OSPF-MIB", "nsOspfLsdbVRID"))
)
if mibBuilder.loadTexts:
    nsOspfTxRetransmit.setStatus(
        "current"
    )

nsOspfVirtIfTxRetransmit = NotificationType(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 16, 2, 11)
)
nsOspfVirtIfTxRetransmit.setObjects(
      *(("NETSCREEN-TRAP-MIB", "netscreenTrapType"),
        ("NETSCREEN-TRAP-MIB", "netscreenTrapDesc"),
        ("NETSCREEN-OSPF-MIB", "nsOspfRouterId"),
        ("NETSCREEN-OSPF-MIB", "nsOspfVirtIfAreaId"),
        ("NETSCREEN-OSPF-MIB", "nsOspfVirtIfNeighbor"),
        ("NETSCREEN-OSPF-TRAP-MIB", "nsOspfPacketType"),
        ("NETSCREEN-OSPF-MIB", "nsOspfLsdbType"),
        ("NETSCREEN-OSPF-MIB", "nsOspfLsdbLsid"),
        ("NETSCREEN-OSPF-MIB", "nsOspfLsdbRouterId"),
        ("NETSCREEN-OSPF-MIB", "nsOspfLsdbVRID"))
)
if mibBuilder.loadTexts:
    nsOspfVirtIfTxRetransmit.setStatus(
        "current"
    )

nsOspfOriginateLsa = NotificationType(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 16, 2, 12)
)
nsOspfOriginateLsa.setObjects(
      *(("NETSCREEN-TRAP-MIB", "netscreenTrapType"),
        ("NETSCREEN-TRAP-MIB", "netscreenTrapDesc"),
        ("NETSCREEN-OSPF-MIB", "nsOspfRouterId"),
        ("NETSCREEN-OSPF-MIB", "nsOspfLsdbAreaId"),
        ("NETSCREEN-OSPF-MIB", "nsOspfLsdbType"),
        ("NETSCREEN-OSPF-MIB", "nsOspfLsdbLsid"),
        ("NETSCREEN-OSPF-MIB", "nsOspfLsdbRouterId"),
        ("NETSCREEN-OSPF-MIB", "nsOspfLsdbVRID"))
)
if mibBuilder.loadTexts:
    nsOspfOriginateLsa.setStatus(
        "current"
    )

nsOspfMaxAgeLsa = NotificationType(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 16, 2, 13)
)
nsOspfMaxAgeLsa.setObjects(
      *(("NETSCREEN-TRAP-MIB", "netscreenTrapType"),
        ("NETSCREEN-TRAP-MIB", "netscreenTrapDesc"),
        ("NETSCREEN-OSPF-MIB", "nsOspfRouterId"),
        ("NETSCREEN-OSPF-MIB", "nsOspfLsdbAreaId"),
        ("NETSCREEN-OSPF-MIB", "nsOspfLsdbType"),
        ("NETSCREEN-OSPF-MIB", "nsOspfLsdbLsid"),
        ("NETSCREEN-OSPF-MIB", "nsOspfLsdbRouterId"),
        ("NETSCREEN-OSPF-MIB", "nsOspfLsdbVRID"))
)
if mibBuilder.loadTexts:
    nsOspfMaxAgeLsa.setStatus(
        "current"
    )

nsOspfLsdbOverflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 16, 2, 14)
)
nsOspfLsdbOverflow.setObjects(
      *(("NETSCREEN-TRAP-MIB", "netscreenTrapType"),
        ("NETSCREEN-TRAP-MIB", "netscreenTrapDesc"),
        ("NETSCREEN-OSPF-MIB", "nsOspfRouterId"),
        ("NETSCREEN-OSPF-MIB", "nsOspfExtLsdbLimit"),
        ("NETSCREEN-OSPF-MIB", "nsOspfLsdbVRID"))
)
if mibBuilder.loadTexts:
    nsOspfLsdbOverflow.setStatus(
        "current"
    )

nsOspfLsdbApproachingOverflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 16, 2, 15)
)
nsOspfLsdbApproachingOverflow.setObjects(
      *(("NETSCREEN-TRAP-MIB", "netscreenTrapType"),
        ("NETSCREEN-TRAP-MIB", "netscreenTrapDesc"),
        ("NETSCREEN-OSPF-MIB", "nsOspfRouterId"),
        ("NETSCREEN-OSPF-MIB", "nsOspfExtLsdbLimit"),
        ("NETSCREEN-OSPF-MIB", "nsOspfLsdbVRID"))
)
if mibBuilder.loadTexts:
    nsOspfLsdbApproachingOverflow.setStatus(
        "current"
    )

nsOspfIfStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 16, 2, 16)
)
nsOspfIfStateChange.setObjects(
      *(("NETSCREEN-TRAP-MIB", "netscreenTrapType"),
        ("NETSCREEN-TRAP-MIB", "netscreenTrapDesc"),
        ("NETSCREEN-OSPF-MIB", "nsOspfRouterId"),
        ("NETSCREEN-OSPF-MIB", "nsOspfIfIpAddress"),
        ("NETSCREEN-OSPF-MIB", "nsOspfAddressLessIf"),
        ("NETSCREEN-OSPF-MIB", "nsOspfIfState"),
        ("NETSCREEN-OSPF-MIB", "nsOspfIfVRID"))
)
if mibBuilder.loadTexts:
    nsOspfIfStateChange.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NETSCREEN-OSPF-TRAP-MIB",
    **{"nsOspfTrap": nsOspfTrap,
       "nsOspfTrapControl": nsOspfTrapControl,
       "nsOspfSetTrap": nsOspfSetTrap,
       "nsOspfConfigErrorType": nsOspfConfigErrorType,
       "nsOspfPacketType": nsOspfPacketType,
       "nsOspfPacketSrc": nsOspfPacketSrc,
       "nsOspfTraps": nsOspfTraps,
       "nsOspfVirtIfStateChange": nsOspfVirtIfStateChange,
       "nsOspfNbrStateChange": nsOspfNbrStateChange,
       "nsOspfVirtNbrStateChange": nsOspfVirtNbrStateChange,
       "nsOspfIfConfigError": nsOspfIfConfigError,
       "nsOspfVirtIfConfigError": nsOspfVirtIfConfigError,
       "nsOspfIfAuthFailure": nsOspfIfAuthFailure,
       "nsOspfVirtIfAuthFailure": nsOspfVirtIfAuthFailure,
       "nsOspfIfRxBadPacket": nsOspfIfRxBadPacket,
       "nsOspfVirtIfRxBadPacket": nsOspfVirtIfRxBadPacket,
       "nsOspfTxRetransmit": nsOspfTxRetransmit,
       "nsOspfVirtIfTxRetransmit": nsOspfVirtIfTxRetransmit,
       "nsOspfOriginateLsa": nsOspfOriginateLsa,
       "nsOspfMaxAgeLsa": nsOspfMaxAgeLsa,
       "nsOspfLsdbOverflow": nsOspfLsdbOverflow,
       "nsOspfLsdbApproachingOverflow": nsOspfLsdbApproachingOverflow,
       "nsOspfIfStateChange": nsOspfIfStateChange}
)
