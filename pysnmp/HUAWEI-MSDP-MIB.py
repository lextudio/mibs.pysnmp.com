# SNMP MIB module (HUAWEI-MSDP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-MSDP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:05:14 2024
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

(msdpPeerFsmEstablishedTransitions,
 msdpPeerRemoteAddress,
 msdpPeerState) = mibBuilder.importSymbols(
    "MSDP-MIB",
    "msdpPeerFsmEstablishedTransitions",
    "msdpPeerRemoteAddress",
    "msdpPeerState")

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

hwMsdpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 218)
)
hwMsdpMIB.setRevisions(
        ("2015-02-05 00:00",
         "2009-10-31 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwMsdpMIBObjects_ObjectIdentity = ObjectIdentity
hwMsdpMIBObjects = _HwMsdpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 218, 1)
)
_HwMsdp_ObjectIdentity = ObjectIdentity
hwMsdp = _HwMsdp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 218, 1, 1)
)
_HwMsdpObjects_ObjectIdentity = ObjectIdentity
hwMsdpObjects = _HwMsdpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 218, 1, 1, 1)
)
_HwMsdpTrapsObjects_ObjectIdentity = ObjectIdentity
hwMsdpTrapsObjects = _HwMsdpTrapsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 218, 1, 1, 2)
)
_HwMsdpInstanceID_Type = Unsigned32
_HwMsdpInstanceID_Object = MibScalar
hwMsdpInstanceID = _HwMsdpInstanceID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 218, 1, 1, 2, 1),
    _HwMsdpInstanceID_Type()
)
hwMsdpInstanceID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwMsdpInstanceID.setStatus("current")
_HwMsdpInstanceName_Type = DisplayString
_HwMsdpInstanceName_Object = MibScalar
hwMsdpInstanceName = _HwMsdpInstanceName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 218, 1, 1, 2, 2),
    _HwMsdpInstanceName_Type()
)
hwMsdpInstanceName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwMsdpInstanceName.setStatus("current")


class _HwMsdpNotificationReason_Type(Integer32):
    """Custom type hwMsdpNotificationReason based on Integer32"""
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
              100)
        )
    )
    namedValues = NamedValues(
        *(("alarmClear", 100),
          ("alarmTimeout", 9),
          ("deletePeer", 8),
          ("holdTimerExpired", 1),
          ("peerUpAgain", 7),
          ("receiveInvalidTLV", 4),
          ("receiveNotificationTLV", 5),
          ("sockerError", 3),
          ("tcpNotEstablish", 2),
          ("userOperation", 6))
    )


_HwMsdpNotificationReason_Type.__name__ = "Integer32"
_HwMsdpNotificationReason_Object = MibScalar
hwMsdpNotificationReason = _HwMsdpNotificationReason_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 218, 1, 1, 2, 3),
    _HwMsdpNotificationReason_Type()
)
hwMsdpNotificationReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwMsdpNotificationReason.setStatus("current")
_HwMsdpTraps_ObjectIdentity = ObjectIdentity
hwMsdpTraps = _HwMsdpTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 218, 1, 1, 3)
)
_HwMsdpMIBConformance_ObjectIdentity = ObjectIdentity
hwMsdpMIBConformance = _HwMsdpMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 218, 1, 1, 4)
)
_HwMsdpMIBCompliances_ObjectIdentity = ObjectIdentity
hwMsdpMIBCompliances = _HwMsdpMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 218, 1, 1, 4, 1)
)
_HwMsdpMIBGroups_ObjectIdentity = ObjectIdentity
hwMsdpMIBGroups = _HwMsdpMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 218, 1, 1, 4, 2)
)

# Managed Objects groups

hwMsdpMIBPeerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 218, 1, 1, 4, 2, 1)
)
hwMsdpMIBPeerGroup.setObjects(
      *(("HUAWEI-MSDP-MIB", "hwMsdpNotificationReason"),
        ("HUAWEI-MSDP-MIB", "hwMsdpInstanceName"),
        ("HUAWEI-MSDP-MIB", "hwMsdpInstanceID"))
)
if mibBuilder.loadTexts:
    hwMsdpMIBPeerGroup.setStatus("current")


# Notification objects

hwMsdpNeighborUnavailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 218, 1, 1, 3, 1)
)
hwMsdpNeighborUnavailable.setObjects(
      *(("HUAWEI-MSDP-MIB", "hwMsdpInstanceID"),
        ("HUAWEI-MSDP-MIB", "hwMsdpInstanceName"),
        ("MSDP-MIB", "msdpPeerState"),
        ("HUAWEI-MSDP-MIB", "hwMsdpNotificationReason"))
)
if mibBuilder.loadTexts:
    hwMsdpNeighborUnavailable.setStatus(
        "current"
    )

hwMsdpNeighborUnvailableClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 218, 1, 1, 3, 2)
)
hwMsdpNeighborUnvailableClear.setObjects(
      *(("HUAWEI-MSDP-MIB", "hwMsdpInstanceID"),
        ("HUAWEI-MSDP-MIB", "hwMsdpInstanceName"),
        ("MSDP-MIB", "msdpPeerState"),
        ("HUAWEI-MSDP-MIB", "hwMsdpNotificationReason"))
)
if mibBuilder.loadTexts:
    hwMsdpNeighborUnvailableClear.setStatus(
        "current"
    )


# Notifications groups

hwMsdpMIBNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 218, 1, 1, 4, 2, 2)
)
hwMsdpMIBNotificationGroup.setObjects(
      *(("HUAWEI-MSDP-MIB", "hwMsdpNeighborUnavailable"),
        ("HUAWEI-MSDP-MIB", "hwMsdpNeighborUnvailableClear"))
)
if mibBuilder.loadTexts:
    hwMsdpMIBNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hwMsdpMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 218, 1, 1, 4, 1, 1)
)
if mibBuilder.loadTexts:
    hwMsdpMIBCompliance.setStatus(
        "deprecated"
    )

hwMsdpMIBFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 218, 1, 1, 4, 1, 2)
)
if mibBuilder.loadTexts:
    hwMsdpMIBFullCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-MSDP-MIB",
    **{"hwMsdpMIB": hwMsdpMIB,
       "hwMsdpMIBObjects": hwMsdpMIBObjects,
       "hwMsdp": hwMsdp,
       "hwMsdpObjects": hwMsdpObjects,
       "hwMsdpTrapsObjects": hwMsdpTrapsObjects,
       "hwMsdpInstanceID": hwMsdpInstanceID,
       "hwMsdpInstanceName": hwMsdpInstanceName,
       "hwMsdpNotificationReason": hwMsdpNotificationReason,
       "hwMsdpTraps": hwMsdpTraps,
       "hwMsdpNeighborUnavailable": hwMsdpNeighborUnavailable,
       "hwMsdpNeighborUnvailableClear": hwMsdpNeighborUnvailableClear,
       "hwMsdpMIBConformance": hwMsdpMIBConformance,
       "hwMsdpMIBCompliances": hwMsdpMIBCompliances,
       "hwMsdpMIBCompliance": hwMsdpMIBCompliance,
       "hwMsdpMIBFullCompliance": hwMsdpMIBFullCompliance,
       "hwMsdpMIBGroups": hwMsdpMIBGroups,
       "hwMsdpMIBPeerGroup": hwMsdpMIBPeerGroup,
       "hwMsdpMIBNotificationGroup": hwMsdpMIBNotificationGroup}
)
