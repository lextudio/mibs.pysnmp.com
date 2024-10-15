# SNMP MIB module (OSPF-TRAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/OSPF-TRAP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:35:44 2024
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
 ospfAreaId,
 ospfAreaNssaTranslatorState,
 ospfExtLsdbLimit,
 ospfIfIpAddress,
 ospfIfState,
 ospfLsdbAreaId,
 ospfLsdbLsid,
 ospfLsdbRouterId,
 ospfLsdbType,
 ospfNbrAddressLessIndex,
 ospfNbrIpAddr,
 ospfNbrRestartHelperAge,
 ospfNbrRestartHelperExitReason,
 ospfNbrRestartHelperStatus,
 ospfNbrRtrId,
 ospfNbrState,
 ospfRestartExitReason,
 ospfRestartInterval,
 ospfRestartStatus,
 ospfRouterId,
 ospfVirtIfAreaId,
 ospfVirtIfNeighbor,
 ospfVirtIfState,
 ospfVirtNbrArea,
 ospfVirtNbrRestartHelperAge,
 ospfVirtNbrRestartHelperExitReason,
 ospfVirtNbrRestartHelperStatus,
 ospfVirtNbrRtrId,
 ospfVirtNbrState) = mibBuilder.importSymbols(
    "OSPF-MIB",
    "ospf",
    "ospfAddressLessIf",
    "ospfAreaId",
    "ospfAreaNssaTranslatorState",
    "ospfExtLsdbLimit",
    "ospfIfIpAddress",
    "ospfIfState",
    "ospfLsdbAreaId",
    "ospfLsdbLsid",
    "ospfLsdbRouterId",
    "ospfLsdbType",
    "ospfNbrAddressLessIndex",
    "ospfNbrIpAddr",
    "ospfNbrRestartHelperAge",
    "ospfNbrRestartHelperExitReason",
    "ospfNbrRestartHelperStatus",
    "ospfNbrRtrId",
    "ospfNbrState",
    "ospfRestartExitReason",
    "ospfRestartInterval",
    "ospfRestartStatus",
    "ospfRouterId",
    "ospfVirtIfAreaId",
    "ospfVirtIfNeighbor",
    "ospfVirtIfState",
    "ospfVirtNbrArea",
    "ospfVirtNbrRestartHelperAge",
    "ospfVirtNbrRestartHelperExitReason",
    "ospfVirtNbrRestartHelperStatus",
    "ospfVirtNbrRtrId",
    "ospfVirtNbrState")

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

ospfTrap = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 14, 16)
)
ospfTrap.setRevisions(
        ("2006-11-10 00:00",
         "1995-01-20 12:25")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_OspfTrapControl_ObjectIdentity = ObjectIdentity
ospfTrapControl = _OspfTrapControl_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 14, 16, 1)
)


class _OspfSetTrap_Type(OctetString):
    """Custom type ospfSetTrap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_OspfSetTrap_Type.__name__ = "OctetString"
_OspfSetTrap_Object = MibScalar
ospfSetTrap = _OspfSetTrap_Object(
    (1, 3, 6, 1, 2, 1, 14, 16, 1, 1),
    _OspfSetTrap_Type()
)
ospfSetTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfSetTrap.setStatus("current")


class _OspfConfigErrorType_Type(Integer32):
    """Custom type ospfConfigErrorType based on Integer32"""
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("areaMismatch", 2),
          ("authFailure", 6),
          ("authTypeMismatch", 5),
          ("badVersion", 1),
          ("deadIntervalMismatch", 9),
          ("duplicateRouterId", 12),
          ("helloIntervalMismatch", 8),
          ("mtuMismatch", 11),
          ("netMaskMismatch", 7),
          ("noError", 13),
          ("optionMismatch", 10),
          ("unknownNbmaNbr", 3),
          ("unknownVirtualNbr", 4))
    )


_OspfConfigErrorType_Type.__name__ = "Integer32"
_OspfConfigErrorType_Object = MibScalar
ospfConfigErrorType = _OspfConfigErrorType_Object(
    (1, 3, 6, 1, 2, 1, 14, 16, 1, 2),
    _OspfConfigErrorType_Type()
)
ospfConfigErrorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfConfigErrorType.setStatus("current")


class _OspfPacketType_Type(Integer32):
    """Custom type ospfPacketType based on Integer32"""
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
        *(("dbDescript", 2),
          ("hello", 1),
          ("lsAck", 5),
          ("lsReq", 3),
          ("lsUpdate", 4),
          ("nullPacket", 6))
    )


_OspfPacketType_Type.__name__ = "Integer32"
_OspfPacketType_Object = MibScalar
ospfPacketType = _OspfPacketType_Object(
    (1, 3, 6, 1, 2, 1, 14, 16, 1, 3),
    _OspfPacketType_Type()
)
ospfPacketType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPacketType.setStatus("current")
_OspfPacketSrc_Type = IpAddress
_OspfPacketSrc_Object = MibScalar
ospfPacketSrc = _OspfPacketSrc_Object(
    (1, 3, 6, 1, 2, 1, 14, 16, 1, 4),
    _OspfPacketSrc_Type()
)
ospfPacketSrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPacketSrc.setStatus("current")
_OspfTraps_ObjectIdentity = ObjectIdentity
ospfTraps = _OspfTraps_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 14, 16, 2)
)
_OspfTrapConformance_ObjectIdentity = ObjectIdentity
ospfTrapConformance = _OspfTrapConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 14, 16, 3)
)
_OspfTrapGroups_ObjectIdentity = ObjectIdentity
ospfTrapGroups = _OspfTrapGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 14, 16, 3, 1)
)
_OspfTrapCompliances_ObjectIdentity = ObjectIdentity
ospfTrapCompliances = _OspfTrapCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 14, 16, 3, 2)
)

# Managed Objects groups

ospfTrapControlGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 14, 16, 3, 1, 1)
)
ospfTrapControlGroup.setObjects(
      *(("OSPF-TRAP-MIB", "ospfSetTrap"),
        ("OSPF-TRAP-MIB", "ospfConfigErrorType"),
        ("OSPF-TRAP-MIB", "ospfPacketType"),
        ("OSPF-TRAP-MIB", "ospfPacketSrc"))
)
if mibBuilder.loadTexts:
    ospfTrapControlGroup.setStatus("current")


# Notification objects

ospfVirtIfStateChange = NotificationType(
    (1, 3, 6, 1, 2, 1, 14, 16, 2, 1)
)
ospfVirtIfStateChange.setObjects(
      *(("OSPF-MIB", "ospfRouterId"),
        ("OSPF-MIB", "ospfVirtIfAreaId"),
        ("OSPF-MIB", "ospfVirtIfNeighbor"),
        ("OSPF-MIB", "ospfVirtIfState"))
)
if mibBuilder.loadTexts:
    ospfVirtIfStateChange.setStatus(
        "current"
    )

ospfNbrStateChange = NotificationType(
    (1, 3, 6, 1, 2, 1, 14, 16, 2, 2)
)
ospfNbrStateChange.setObjects(
      *(("OSPF-MIB", "ospfRouterId"),
        ("OSPF-MIB", "ospfNbrIpAddr"),
        ("OSPF-MIB", "ospfNbrAddressLessIndex"),
        ("OSPF-MIB", "ospfNbrRtrId"),
        ("OSPF-MIB", "ospfNbrState"))
)
if mibBuilder.loadTexts:
    ospfNbrStateChange.setStatus(
        "current"
    )

ospfVirtNbrStateChange = NotificationType(
    (1, 3, 6, 1, 2, 1, 14, 16, 2, 3)
)
ospfVirtNbrStateChange.setObjects(
      *(("OSPF-MIB", "ospfRouterId"),
        ("OSPF-MIB", "ospfVirtNbrArea"),
        ("OSPF-MIB", "ospfVirtNbrRtrId"),
        ("OSPF-MIB", "ospfVirtNbrState"))
)
if mibBuilder.loadTexts:
    ospfVirtNbrStateChange.setStatus(
        "current"
    )

ospfIfConfigError = NotificationType(
    (1, 3, 6, 1, 2, 1, 14, 16, 2, 4)
)
ospfIfConfigError.setObjects(
      *(("OSPF-MIB", "ospfRouterId"),
        ("OSPF-MIB", "ospfIfIpAddress"),
        ("OSPF-MIB", "ospfAddressLessIf"),
        ("OSPF-TRAP-MIB", "ospfPacketSrc"),
        ("OSPF-TRAP-MIB", "ospfConfigErrorType"),
        ("OSPF-TRAP-MIB", "ospfPacketType"))
)
if mibBuilder.loadTexts:
    ospfIfConfigError.setStatus(
        "current"
    )

ospfVirtIfConfigError = NotificationType(
    (1, 3, 6, 1, 2, 1, 14, 16, 2, 5)
)
ospfVirtIfConfigError.setObjects(
      *(("OSPF-MIB", "ospfRouterId"),
        ("OSPF-MIB", "ospfVirtIfAreaId"),
        ("OSPF-MIB", "ospfVirtIfNeighbor"),
        ("OSPF-TRAP-MIB", "ospfConfigErrorType"),
        ("OSPF-TRAP-MIB", "ospfPacketType"))
)
if mibBuilder.loadTexts:
    ospfVirtIfConfigError.setStatus(
        "current"
    )

ospfIfAuthFailure = NotificationType(
    (1, 3, 6, 1, 2, 1, 14, 16, 2, 6)
)
ospfIfAuthFailure.setObjects(
      *(("OSPF-MIB", "ospfRouterId"),
        ("OSPF-MIB", "ospfIfIpAddress"),
        ("OSPF-MIB", "ospfAddressLessIf"),
        ("OSPF-TRAP-MIB", "ospfPacketSrc"),
        ("OSPF-TRAP-MIB", "ospfConfigErrorType"),
        ("OSPF-TRAP-MIB", "ospfPacketType"))
)
if mibBuilder.loadTexts:
    ospfIfAuthFailure.setStatus(
        "current"
    )

ospfVirtIfAuthFailure = NotificationType(
    (1, 3, 6, 1, 2, 1, 14, 16, 2, 7)
)
ospfVirtIfAuthFailure.setObjects(
      *(("OSPF-MIB", "ospfRouterId"),
        ("OSPF-MIB", "ospfVirtIfAreaId"),
        ("OSPF-MIB", "ospfVirtIfNeighbor"),
        ("OSPF-TRAP-MIB", "ospfConfigErrorType"),
        ("OSPF-TRAP-MIB", "ospfPacketType"))
)
if mibBuilder.loadTexts:
    ospfVirtIfAuthFailure.setStatus(
        "current"
    )

ospfIfRxBadPacket = NotificationType(
    (1, 3, 6, 1, 2, 1, 14, 16, 2, 8)
)
ospfIfRxBadPacket.setObjects(
      *(("OSPF-MIB", "ospfRouterId"),
        ("OSPF-MIB", "ospfIfIpAddress"),
        ("OSPF-MIB", "ospfAddressLessIf"),
        ("OSPF-TRAP-MIB", "ospfPacketSrc"),
        ("OSPF-TRAP-MIB", "ospfPacketType"))
)
if mibBuilder.loadTexts:
    ospfIfRxBadPacket.setStatus(
        "current"
    )

ospfVirtIfRxBadPacket = NotificationType(
    (1, 3, 6, 1, 2, 1, 14, 16, 2, 9)
)
ospfVirtIfRxBadPacket.setObjects(
      *(("OSPF-MIB", "ospfRouterId"),
        ("OSPF-MIB", "ospfVirtIfAreaId"),
        ("OSPF-MIB", "ospfVirtIfNeighbor"),
        ("OSPF-TRAP-MIB", "ospfPacketType"))
)
if mibBuilder.loadTexts:
    ospfVirtIfRxBadPacket.setStatus(
        "current"
    )

ospfTxRetransmit = NotificationType(
    (1, 3, 6, 1, 2, 1, 14, 16, 2, 10)
)
ospfTxRetransmit.setObjects(
      *(("OSPF-MIB", "ospfRouterId"),
        ("OSPF-MIB", "ospfIfIpAddress"),
        ("OSPF-MIB", "ospfAddressLessIf"),
        ("OSPF-MIB", "ospfNbrRtrId"),
        ("OSPF-TRAP-MIB", "ospfPacketType"),
        ("OSPF-MIB", "ospfLsdbType"),
        ("OSPF-MIB", "ospfLsdbLsid"),
        ("OSPF-MIB", "ospfLsdbRouterId"))
)
if mibBuilder.loadTexts:
    ospfTxRetransmit.setStatus(
        "current"
    )

ospfVirtIfTxRetransmit = NotificationType(
    (1, 3, 6, 1, 2, 1, 14, 16, 2, 11)
)
ospfVirtIfTxRetransmit.setObjects(
      *(("OSPF-MIB", "ospfRouterId"),
        ("OSPF-MIB", "ospfVirtIfAreaId"),
        ("OSPF-MIB", "ospfVirtIfNeighbor"),
        ("OSPF-TRAP-MIB", "ospfPacketType"),
        ("OSPF-MIB", "ospfLsdbType"),
        ("OSPF-MIB", "ospfLsdbLsid"),
        ("OSPF-MIB", "ospfLsdbRouterId"))
)
if mibBuilder.loadTexts:
    ospfVirtIfTxRetransmit.setStatus(
        "current"
    )

ospfOriginateLsa = NotificationType(
    (1, 3, 6, 1, 2, 1, 14, 16, 2, 12)
)
ospfOriginateLsa.setObjects(
      *(("OSPF-MIB", "ospfRouterId"),
        ("OSPF-MIB", "ospfLsdbAreaId"),
        ("OSPF-MIB", "ospfLsdbType"),
        ("OSPF-MIB", "ospfLsdbLsid"),
        ("OSPF-MIB", "ospfLsdbRouterId"))
)
if mibBuilder.loadTexts:
    ospfOriginateLsa.setStatus(
        "current"
    )

ospfMaxAgeLsa = NotificationType(
    (1, 3, 6, 1, 2, 1, 14, 16, 2, 13)
)
ospfMaxAgeLsa.setObjects(
      *(("OSPF-MIB", "ospfRouterId"),
        ("OSPF-MIB", "ospfLsdbAreaId"),
        ("OSPF-MIB", "ospfLsdbType"),
        ("OSPF-MIB", "ospfLsdbLsid"),
        ("OSPF-MIB", "ospfLsdbRouterId"))
)
if mibBuilder.loadTexts:
    ospfMaxAgeLsa.setStatus(
        "current"
    )

ospfLsdbOverflow = NotificationType(
    (1, 3, 6, 1, 2, 1, 14, 16, 2, 14)
)
ospfLsdbOverflow.setObjects(
      *(("OSPF-MIB", "ospfRouterId"),
        ("OSPF-MIB", "ospfExtLsdbLimit"))
)
if mibBuilder.loadTexts:
    ospfLsdbOverflow.setStatus(
        "current"
    )

ospfLsdbApproachingOverflow = NotificationType(
    (1, 3, 6, 1, 2, 1, 14, 16, 2, 15)
)
ospfLsdbApproachingOverflow.setObjects(
      *(("OSPF-MIB", "ospfRouterId"),
        ("OSPF-MIB", "ospfExtLsdbLimit"))
)
if mibBuilder.loadTexts:
    ospfLsdbApproachingOverflow.setStatus(
        "current"
    )

ospfIfStateChange = NotificationType(
    (1, 3, 6, 1, 2, 1, 14, 16, 2, 16)
)
ospfIfStateChange.setObjects(
      *(("OSPF-MIB", "ospfRouterId"),
        ("OSPF-MIB", "ospfIfIpAddress"),
        ("OSPF-MIB", "ospfAddressLessIf"),
        ("OSPF-MIB", "ospfIfState"))
)
if mibBuilder.loadTexts:
    ospfIfStateChange.setStatus(
        "current"
    )

ospfNssaTranslatorStatusChange = NotificationType(
    (1, 3, 6, 1, 2, 1, 14, 16, 2, 17)
)
ospfNssaTranslatorStatusChange.setObjects(
      *(("OSPF-MIB", "ospfRouterId"),
        ("OSPF-MIB", "ospfAreaId"),
        ("OSPF-MIB", "ospfAreaNssaTranslatorState"))
)
if mibBuilder.loadTexts:
    ospfNssaTranslatorStatusChange.setStatus(
        "current"
    )

ospfRestartStatusChange = NotificationType(
    (1, 3, 6, 1, 2, 1, 14, 16, 2, 18)
)
ospfRestartStatusChange.setObjects(
      *(("OSPF-MIB", "ospfRouterId"),
        ("OSPF-MIB", "ospfRestartStatus"),
        ("OSPF-MIB", "ospfRestartInterval"),
        ("OSPF-MIB", "ospfRestartExitReason"))
)
if mibBuilder.loadTexts:
    ospfRestartStatusChange.setStatus(
        "current"
    )

ospfNbrRestartHelperStatusChange = NotificationType(
    (1, 3, 6, 1, 2, 1, 14, 16, 2, 19)
)
ospfNbrRestartHelperStatusChange.setObjects(
      *(("OSPF-MIB", "ospfRouterId"),
        ("OSPF-MIB", "ospfNbrIpAddr"),
        ("OSPF-MIB", "ospfNbrAddressLessIndex"),
        ("OSPF-MIB", "ospfNbrRtrId"),
        ("OSPF-MIB", "ospfNbrRestartHelperStatus"),
        ("OSPF-MIB", "ospfNbrRestartHelperAge"),
        ("OSPF-MIB", "ospfNbrRestartHelperExitReason"))
)
if mibBuilder.loadTexts:
    ospfNbrRestartHelperStatusChange.setStatus(
        "current"
    )

ospfVirtNbrRestartHelperStatusChange = NotificationType(
    (1, 3, 6, 1, 2, 1, 14, 16, 2, 20)
)
ospfVirtNbrRestartHelperStatusChange.setObjects(
      *(("OSPF-MIB", "ospfRouterId"),
        ("OSPF-MIB", "ospfVirtNbrArea"),
        ("OSPF-MIB", "ospfVirtNbrRtrId"),
        ("OSPF-MIB", "ospfVirtNbrRestartHelperStatus"),
        ("OSPF-MIB", "ospfVirtNbrRestartHelperAge"),
        ("OSPF-MIB", "ospfVirtNbrRestartHelperExitReason"))
)
if mibBuilder.loadTexts:
    ospfVirtNbrRestartHelperStatusChange.setStatus(
        "current"
    )


# Notifications groups

ospfTrapEventGroup = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 14, 16, 3, 1, 2)
)
ospfTrapEventGroup.setObjects(
      *(("OSPF-TRAP-MIB", "ospfVirtIfStateChange"),
        ("OSPF-TRAP-MIB", "ospfNbrStateChange"),
        ("OSPF-TRAP-MIB", "ospfVirtNbrStateChange"),
        ("OSPF-TRAP-MIB", "ospfIfConfigError"),
        ("OSPF-TRAP-MIB", "ospfVirtIfConfigError"),
        ("OSPF-TRAP-MIB", "ospfIfAuthFailure"),
        ("OSPF-TRAP-MIB", "ospfVirtIfAuthFailure"),
        ("OSPF-TRAP-MIB", "ospfIfRxBadPacket"),
        ("OSPF-TRAP-MIB", "ospfVirtIfRxBadPacket"),
        ("OSPF-TRAP-MIB", "ospfTxRetransmit"),
        ("OSPF-TRAP-MIB", "ospfVirtIfTxRetransmit"),
        ("OSPF-TRAP-MIB", "ospfOriginateLsa"),
        ("OSPF-TRAP-MIB", "ospfMaxAgeLsa"),
        ("OSPF-TRAP-MIB", "ospfLsdbOverflow"),
        ("OSPF-TRAP-MIB", "ospfLsdbApproachingOverflow"),
        ("OSPF-TRAP-MIB", "ospfIfStateChange"),
        ("OSPF-TRAP-MIB", "ospfNssaTranslatorStatusChange"),
        ("OSPF-TRAP-MIB", "ospfRestartStatusChange"),
        ("OSPF-TRAP-MIB", "ospfNbrRestartHelperStatusChange"),
        ("OSPF-TRAP-MIB", "ospfVirtNbrRestartHelperStatusChange"))
)
if mibBuilder.loadTexts:
    ospfTrapEventGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ospfTrapCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 14, 16, 3, 2, 1)
)
if mibBuilder.loadTexts:
    ospfTrapCompliance.setStatus(
        "obsolete"
    )

ospfTrapCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 14, 16, 3, 2, 2)
)
if mibBuilder.loadTexts:
    ospfTrapCompliance2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OSPF-TRAP-MIB",
    **{"ospfTrap": ospfTrap,
       "ospfTrapControl": ospfTrapControl,
       "ospfSetTrap": ospfSetTrap,
       "ospfConfigErrorType": ospfConfigErrorType,
       "ospfPacketType": ospfPacketType,
       "ospfPacketSrc": ospfPacketSrc,
       "ospfTraps": ospfTraps,
       "ospfVirtIfStateChange": ospfVirtIfStateChange,
       "ospfNbrStateChange": ospfNbrStateChange,
       "ospfVirtNbrStateChange": ospfVirtNbrStateChange,
       "ospfIfConfigError": ospfIfConfigError,
       "ospfVirtIfConfigError": ospfVirtIfConfigError,
       "ospfIfAuthFailure": ospfIfAuthFailure,
       "ospfVirtIfAuthFailure": ospfVirtIfAuthFailure,
       "ospfIfRxBadPacket": ospfIfRxBadPacket,
       "ospfVirtIfRxBadPacket": ospfVirtIfRxBadPacket,
       "ospfTxRetransmit": ospfTxRetransmit,
       "ospfVirtIfTxRetransmit": ospfVirtIfTxRetransmit,
       "ospfOriginateLsa": ospfOriginateLsa,
       "ospfMaxAgeLsa": ospfMaxAgeLsa,
       "ospfLsdbOverflow": ospfLsdbOverflow,
       "ospfLsdbApproachingOverflow": ospfLsdbApproachingOverflow,
       "ospfIfStateChange": ospfIfStateChange,
       "ospfNssaTranslatorStatusChange": ospfNssaTranslatorStatusChange,
       "ospfRestartStatusChange": ospfRestartStatusChange,
       "ospfNbrRestartHelperStatusChange": ospfNbrRestartHelperStatusChange,
       "ospfVirtNbrRestartHelperStatusChange": ospfVirtNbrRestartHelperStatusChange,
       "ospfTrapConformance": ospfTrapConformance,
       "ospfTrapGroups": ospfTrapGroups,
       "ospfTrapControlGroup": ospfTrapControlGroup,
       "ospfTrapEventGroup": ospfTrapEventGroup,
       "ospfTrapCompliances": ospfTrapCompliances,
       "ospfTrapCompliance": ospfTrapCompliance,
       "ospfTrapCompliance2": ospfTrapCompliance2}
)
