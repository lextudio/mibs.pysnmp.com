# SNMP MIB module (RUCKUS-ZD-EVENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RUCKUS-ZD-EVENT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:48:54 2024
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

(ruckusEvents,) = mibBuilder.importSymbols(
    "RUCKUS-ROOT-MIB",
    "ruckusEvents")

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
 MacAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention")


# MODULE-IDENTITY

ruckusZDEventMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuckusZDEventTraps_ObjectIdentity = ObjectIdentity
ruckusZDEventTraps = _RuckusZDEventTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 1)
)
_RuckusZDEventObjects_ObjectIdentity = ObjectIdentity
ruckusZDEventObjects = _RuckusZDEventObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 2)
)
_RuckusZDEventSerial_Type = OctetString
_RuckusZDEventSerial_Object = MibScalar
ruckusZDEventSerial = _RuckusZDEventSerial_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 2, 1),
    _RuckusZDEventSerial_Type()
)
ruckusZDEventSerial.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusZDEventSerial.setStatus("current")
_RuckusZDEventNEID_Type = OctetString
_RuckusZDEventNEID_Object = MibScalar
ruckusZDEventNEID = _RuckusZDEventNEID_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 2, 2),
    _RuckusZDEventNEID_Type()
)
ruckusZDEventNEID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusZDEventNEID.setStatus("current")
_RuckusZDEventSeverity_Type = OctetString
_RuckusZDEventSeverity_Object = MibScalar
ruckusZDEventSeverity = _RuckusZDEventSeverity_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 2, 3),
    _RuckusZDEventSeverity_Type()
)
ruckusZDEventSeverity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusZDEventSeverity.setStatus("current")
_RuckusZDEventType_Type = OctetString
_RuckusZDEventType_Object = MibScalar
ruckusZDEventType = _RuckusZDEventType_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 2, 4),
    _RuckusZDEventType_Type()
)
ruckusZDEventType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusZDEventType.setStatus("current")
_RuckusZDEventTime_Type = OctetString
_RuckusZDEventTime_Object = MibScalar
ruckusZDEventTime = _RuckusZDEventTime_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 2, 5),
    _RuckusZDEventTime_Type()
)
ruckusZDEventTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusZDEventTime.setStatus("current")


class _RuckusZDEventStatus_Type(Integer32):
    """Custom type ruckusZDEventStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("raise", 1))
    )


_RuckusZDEventStatus_Type.__name__ = "Integer32"
_RuckusZDEventStatus_Object = MibScalar
ruckusZDEventStatus = _RuckusZDEventStatus_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 2, 6),
    _RuckusZDEventStatus_Type()
)
ruckusZDEventStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusZDEventStatus.setStatus("current")
_RuckusZDEventTitle_Type = OctetString
_RuckusZDEventTitle_Object = MibScalar
ruckusZDEventTitle = _RuckusZDEventTitle_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 2, 7),
    _RuckusZDEventTitle_Type()
)
ruckusZDEventTitle.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusZDEventTitle.setStatus("current")
_RuckusZDEventContent_Type = OctetString
_RuckusZDEventContent_Object = MibScalar
ruckusZDEventContent = _RuckusZDEventContent_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 2, 8),
    _RuckusZDEventContent_Type()
)
ruckusZDEventContent.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusZDEventContent.setStatus("current")
_RuckusZDEventClientMacAddr_Type = OctetString
_RuckusZDEventClientMacAddr_Object = MibScalar
ruckusZDEventClientMacAddr = _RuckusZDEventClientMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 2, 15),
    _RuckusZDEventClientMacAddr_Type()
)
ruckusZDEventClientMacAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusZDEventClientMacAddr.setStatus("current")
_RuckusZDEventAPMacAddr_Type = OctetString
_RuckusZDEventAPMacAddr_Object = MibScalar
ruckusZDEventAPMacAddr = _RuckusZDEventAPMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 2, 18),
    _RuckusZDEventAPMacAddr_Type()
)
ruckusZDEventAPMacAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusZDEventAPMacAddr.setStatus("current")
_RuckusZDEventRogueMacAddr_Type = OctetString
_RuckusZDEventRogueMacAddr_Object = MibScalar
ruckusZDEventRogueMacAddr = _RuckusZDEventRogueMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 2, 20),
    _RuckusZDEventRogueMacAddr_Type()
)
ruckusZDEventRogueMacAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusZDEventRogueMacAddr.setStatus("current")
_RuckusZDEventSSID_Type = OctetString
_RuckusZDEventSSID_Object = MibScalar
ruckusZDEventSSID = _RuckusZDEventSSID_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 2, 23),
    _RuckusZDEventSSID_Type()
)
ruckusZDEventSSID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusZDEventSSID.setStatus("current")
_RuckusZDEventChannel_Type = Unsigned32
_RuckusZDEventChannel_Object = MibScalar
ruckusZDEventChannel = _RuckusZDEventChannel_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 2, 25),
    _RuckusZDEventChannel_Type()
)
ruckusZDEventChannel.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusZDEventChannel.setStatus("current")
_RuckusZDEventReason_Type = OctetString
_RuckusZDEventReason_Object = MibScalar
ruckusZDEventReason = _RuckusZDEventReason_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 2, 28),
    _RuckusZDEventReason_Type()
)
ruckusZDEventReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusZDEventReason.setStatus("current")
_RuckusZDEventIpAddr_Type = OctetString
_RuckusZDEventIpAddr_Object = MibScalar
ruckusZDEventIpAddr = _RuckusZDEventIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 2, 30),
    _RuckusZDEventIpAddr_Type()
)
ruckusZDEventIpAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusZDEventIpAddr.setStatus("current")

# Managed Objects groups


# Notification objects

ruckusZDEventAPJoinTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 1, 1)
)
ruckusZDEventAPJoinTrap.setObjects(
      *(("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSerial"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventNEID"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSeverity"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventType"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTime"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventStatus"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTitle"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventAPMacAddr"))
)
if mibBuilder.loadTexts:
    ruckusZDEventAPJoinTrap.setStatus(
        "current"
    )

ruckusZDEventSSIDSpoofTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 1, 2)
)
ruckusZDEventSSIDSpoofTrap.setObjects(
      *(("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSerial"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventNEID"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSeverity"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventType"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTime"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventStatus"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTitle"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSSID"))
)
if mibBuilder.loadTexts:
    ruckusZDEventSSIDSpoofTrap.setStatus(
        "current"
    )

ruckusZDEventMACSpoofTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 1, 3)
)
ruckusZDEventMACSpoofTrap.setObjects(
      *(("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSerial"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventNEID"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSeverity"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventType"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTime"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventStatus"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTitle"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSSID"))
)
if mibBuilder.loadTexts:
    ruckusZDEventMACSpoofTrap.setStatus(
        "current"
    )

ruckusZDEventRogueAPTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 1, 4)
)
ruckusZDEventRogueAPTrap.setObjects(
      *(("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSerial"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventNEID"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSeverity"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventType"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTime"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventStatus"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTitle"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSSID"))
)
if mibBuilder.loadTexts:
    ruckusZDEventRogueAPTrap.setStatus(
        "current"
    )

ruckusZDEventAPLostTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 1, 5)
)
ruckusZDEventAPLostTrap.setObjects(
      *(("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSerial"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventNEID"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSeverity"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventType"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTime"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventStatus"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTitle"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventAPMacAddr"))
)
if mibBuilder.loadTexts:
    ruckusZDEventAPLostTrap.setStatus(
        "current"
    )

ruckusZDEventAPLostHeartbeatTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 1, 6)
)
ruckusZDEventAPLostHeartbeatTrap.setObjects(
      *(("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSerial"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventNEID"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSeverity"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventType"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTime"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventStatus"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTitle"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventAPMacAddr"))
)
if mibBuilder.loadTexts:
    ruckusZDEventAPLostHeartbeatTrap.setStatus(
        "current"
    )

ruckusZDEventClientAuthFailBlockTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 1, 7)
)
ruckusZDEventClientAuthFailBlockTrap.setObjects(
      *(("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSerial"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventNEID"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSeverity"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventType"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTime"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventStatus"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTitle"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventClientMacAddr"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventAPMacAddr"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSSID"))
)
if mibBuilder.loadTexts:
    ruckusZDEventClientAuthFailBlockTrap.setStatus(
        "current"
    )

ruckusZDEventAPResetTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 1, 8)
)
ruckusZDEventAPResetTrap.setObjects(
      *(("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSerial"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventNEID"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSeverity"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventType"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTime"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventStatus"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTitle"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventContent"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventAPMacAddr"))
)
if mibBuilder.loadTexts:
    ruckusZDEventAPResetTrap.setStatus(
        "current"
    )

ruckusZDEventIPChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 1, 9)
)
ruckusZDEventIPChangeTrap.setObjects(
      *(("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSerial"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventNEID"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSeverity"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventType"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTime"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventStatus"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTitle"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventContent"))
)
if mibBuilder.loadTexts:
    ruckusZDEventIPChangeTrap.setStatus(
        "current"
    )

ruckusZDEventSystemColdStartTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 1, 10)
)
ruckusZDEventSystemColdStartTrap.setObjects(
      *(("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSerial"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventNEID"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSeverity"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventType"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTime"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventStatus"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTitle"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventContent"))
)
if mibBuilder.loadTexts:
    ruckusZDEventSystemColdStartTrap.setStatus(
        "current"
    )

ruckusZDEventAPChannelChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 1, 11)
)
ruckusZDEventAPChannelChangeTrap.setObjects(
      *(("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSerial"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventNEID"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSeverity"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventType"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTime"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventStatus"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTitle"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventContent"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventAPMacAddr"))
)
if mibBuilder.loadTexts:
    ruckusZDEventAPChannelChangeTrap.setStatus(
        "current"
    )

ruckusZDEventRadiusAuthUnavailableTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 1, 12)
)
ruckusZDEventRadiusAuthUnavailableTrap.setObjects(
      *(("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSerial"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventNEID"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSeverity"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventType"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTime"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventStatus"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTitle"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventContent"))
)
if mibBuilder.loadTexts:
    ruckusZDEventRadiusAuthUnavailableTrap.setStatus(
        "current"
    )

ruckusZDEventRadiusAcctUnavailableTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 1, 13)
)
ruckusZDEventRadiusAcctUnavailableTrap.setObjects(
      *(("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSerial"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventNEID"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSeverity"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventType"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTime"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventStatus"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTitle"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventContent"))
)
if mibBuilder.loadTexts:
    ruckusZDEventRadiusAcctUnavailableTrap.setStatus(
        "current"
    )

ruckusZDEventClientJoinFailAPBusyTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 1, 14)
)
ruckusZDEventClientJoinFailAPBusyTrap.setObjects(
      *(("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSerial"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventNEID"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSeverity"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventType"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTime"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventStatus"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTitle"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventContent"))
)
if mibBuilder.loadTexts:
    ruckusZDEventClientJoinFailAPBusyTrap.setStatus(
        "current"
    )

ruckusZDEventInterferenceADHoc = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 1, 15)
)
ruckusZDEventInterferenceADHoc.setObjects(
      *(("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSerial"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventNEID"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSeverity"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventType"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTime"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventStatus"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTitle"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventContent"))
)
if mibBuilder.loadTexts:
    ruckusZDEventInterferenceADHoc.setStatus(
        "current"
    )

ruckusZDEventImageUpgradeFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 1, 16)
)
ruckusZDEventImageUpgradeFailTrap.setObjects(
      *(("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSerial"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventNEID"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSeverity"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventType"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTime"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventStatus"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTitle"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventContent"))
)
if mibBuilder.loadTexts:
    ruckusZDEventImageUpgradeFailTrap.setStatus(
        "current"
    )

ruckusZDEventHeartbeatTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 1, 22)
)
ruckusZDEventHeartbeatTrap.setObjects(
      *(("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSerial"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventNEID"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSeverity"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventType"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTime"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventStatus"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTitle"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventContent"))
)
if mibBuilder.loadTexts:
    ruckusZDEventHeartbeatTrap.setStatus(
        "current"
    )

ruckusZDEventAttackedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 1, 24)
)
ruckusZDEventAttackedTrap.setObjects(
      *(("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSerial"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventNEID"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSeverity"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventType"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTime"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventStatus"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTitle"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventContent"))
)
if mibBuilder.loadTexts:
    ruckusZDEventAttackedTrap.setStatus(
        "current"
    )

ruckusZDEventSystemWarmStartTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 1, 25)
)
ruckusZDEventSystemWarmStartTrap.setObjects(
      *(("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSerial"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventNEID"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSeverity"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventType"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTime"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventStatus"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTitle"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventContent"))
)
if mibBuilder.loadTexts:
    ruckusZDEventSystemWarmStartTrap.setStatus(
        "current"
    )

ruckusZDEventInterfereAPTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 1, 26)
)
ruckusZDEventInterfereAPTrap.setObjects(
      *(("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSerial"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventNEID"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSeverity"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventType"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTime"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventStatus"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTitle"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventContent"))
)
if mibBuilder.loadTexts:
    ruckusZDEventInterfereAPTrap.setStatus(
        "current"
    )

ruckusZDEventAPSystemColdStartTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 1, 31)
)
ruckusZDEventAPSystemColdStartTrap.setObjects(
      *(("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSerial"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventNEID"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSeverity"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventType"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTime"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventStatus"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTitle"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventContent"))
)
if mibBuilder.loadTexts:
    ruckusZDEventAPSystemColdStartTrap.setStatus(
        "current"
    )

ruckusZDEventAPSystemWarmStartTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 1, 32)
)
ruckusZDEventAPSystemWarmStartTrap.setObjects(
      *(("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSerial"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventNEID"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSeverity"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventType"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTime"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventStatus"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTitle"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventContent"))
)
if mibBuilder.loadTexts:
    ruckusZDEventAPSystemWarmStartTrap.setStatus(
        "current"
    )

ruckusZDEventAPSSIDChangedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 1, 33)
)
ruckusZDEventAPSSIDChangedTrap.setObjects(
      *(("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSerial"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventNEID"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSeverity"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventType"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTime"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventStatus"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTitle"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventContent"))
)
if mibBuilder.loadTexts:
    ruckusZDEventAPSSIDChangedTrap.setStatus(
        "current"
    )

ruckusZDEventAPClientExceedValve = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 1, 34)
)
ruckusZDEventAPClientExceedValve.setObjects(
      *(("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSerial"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventNEID"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSeverity"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventType"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTime"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventStatus"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTitle"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventContent"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventAPMacAddr"))
)
if mibBuilder.loadTexts:
    ruckusZDEventAPClientExceedValve.setStatus(
        "current"
    )

ruckusZDEventAPAvailableStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 1, 35)
)
ruckusZDEventAPAvailableStatusTrap.setObjects(
      *(("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSerial"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventNEID"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSeverity"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventType"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTime"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventStatus"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTitle"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventContent"))
)
if mibBuilder.loadTexts:
    ruckusZDEventAPAvailableStatusTrap.setStatus(
        "current"
    )

ruckusZDEventAPWirelessInterfaceFaultTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 1, 36)
)
ruckusZDEventAPWirelessInterfaceFaultTrap.setObjects(
      *(("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSerial"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventNEID"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSeverity"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventType"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTime"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventStatus"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTitle"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventContent"))
)
if mibBuilder.loadTexts:
    ruckusZDEventAPWirelessInterfaceFaultTrap.setStatus(
        "current"
    )

ruckusZDEventSystemCpuUtilExceedValve = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 1, 37)
)
ruckusZDEventSystemCpuUtilExceedValve.setObjects(
      *(("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSerial"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventNEID"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSeverity"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventType"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTime"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventStatus"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTitle"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventContent"))
)
if mibBuilder.loadTexts:
    ruckusZDEventSystemCpuUtilExceedValve.setStatus(
        "current"
    )

ruckusZDEventSystemMemUtilExceedValve = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 1, 38)
)
ruckusZDEventSystemMemUtilExceedValve.setObjects(
      *(("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSerial"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventNEID"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSeverity"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventType"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTime"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventStatus"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTitle"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventContent"))
)
if mibBuilder.loadTexts:
    ruckusZDEventSystemMemUtilExceedValve.setStatus(
        "current"
    )

ruckusZDEventSystemBandwidthUtilExceedValve = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 1, 39)
)
ruckusZDEventSystemBandwidthUtilExceedValve.setObjects(
      *(("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSerial"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventNEID"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSeverity"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventType"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTime"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventStatus"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTitle"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventContent"))
)
if mibBuilder.loadTexts:
    ruckusZDEventSystemBandwidthUtilExceedValve.setStatus(
        "current"
    )

ruckusZDEventSystemDropPacketRateExceedValve = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 1, 40)
)
ruckusZDEventSystemDropPacketRateExceedValve.setObjects(
      *(("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSerial"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventNEID"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSeverity"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventType"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTime"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventStatus"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTitle"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventContent"))
)
if mibBuilder.loadTexts:
    ruckusZDEventSystemDropPacketRateExceedValve.setStatus(
        "current"
    )

ruckusZDEventAPSyncTimeFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 1, 41)
)
ruckusZDEventAPSyncTimeFail.setObjects(
      *(("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSerial"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventNEID"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSeverity"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventType"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTime"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventStatus"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTitle"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventContent"))
)
if mibBuilder.loadTexts:
    ruckusZDEventAPSyncTimeFail.setStatus(
        "current"
    )

ruckusZDEventSystemCpuUtilClrWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 1, 42)
)
ruckusZDEventSystemCpuUtilClrWarn.setObjects(
      *(("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSerial"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventNEID"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSeverity"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventType"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTime"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventStatus"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTitle"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventContent"))
)
if mibBuilder.loadTexts:
    ruckusZDEventSystemCpuUtilClrWarn.setStatus(
        "current"
    )

ruckusZDEventSystemMemUtilClrwarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 1, 43)
)
ruckusZDEventSystemMemUtilClrwarn.setObjects(
      *(("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSerial"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventNEID"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSeverity"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventType"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTime"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventStatus"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTitle"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventContent"))
)
if mibBuilder.loadTexts:
    ruckusZDEventSystemMemUtilClrwarn.setStatus(
        "current"
    )

ruckusZDEventClientJoin = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 1, 60)
)
ruckusZDEventClientJoin.setObjects(
      *(("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSerial"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventNEID"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSeverity"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventType"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTime"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventStatus"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTitle"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventClientMacAddr"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventAPMacAddr"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSSID"))
)
if mibBuilder.loadTexts:
    ruckusZDEventClientJoin.setStatus(
        "current"
    )

ruckusZDEventClientJoinFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 1, 61)
)
ruckusZDEventClientJoinFailed.setObjects(
      *(("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSerial"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventNEID"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSeverity"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventType"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTime"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventStatus"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTitle"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventClientMacAddr"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventAPMacAddr"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSSID"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventReason"))
)
if mibBuilder.loadTexts:
    ruckusZDEventClientJoinFailed.setStatus(
        "current"
    )

ruckusZDEventClientJoinFailedAPBusy = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 1, 62)
)
ruckusZDEventClientJoinFailedAPBusy.setObjects(
      *(("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSerial"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventNEID"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSeverity"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventType"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTime"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventStatus"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTitle"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventClientMacAddr"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventAPMacAddr"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSSID"))
)
if mibBuilder.loadTexts:
    ruckusZDEventClientJoinFailedAPBusy.setStatus(
        "current"
    )

ruckusZDEventClientDisconnect = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 1, 63)
)
ruckusZDEventClientDisconnect.setObjects(
      *(("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSerial"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventNEID"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSeverity"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventType"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTime"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventStatus"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTitle"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventClientMacAddr"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventAPMacAddr"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSSID"))
)
if mibBuilder.loadTexts:
    ruckusZDEventClientDisconnect.setStatus(
        "current"
    )

ruckusZDEventClientRoamOut = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 1, 64)
)
ruckusZDEventClientRoamOut.setObjects(
      *(("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSerial"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventNEID"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSeverity"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventType"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTime"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventStatus"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTitle"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventClientMacAddr"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventAPMacAddr"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSSID"))
)
if mibBuilder.loadTexts:
    ruckusZDEventClientRoamOut.setStatus(
        "current"
    )

ruckusZDEventClientRoamIn = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 1, 65)
)
ruckusZDEventClientRoamIn.setObjects(
      *(("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSerial"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventNEID"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSeverity"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventType"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTime"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventStatus"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTitle"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventClientMacAddr"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventAPMacAddr"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSSID"))
)
if mibBuilder.loadTexts:
    ruckusZDEventClientRoamIn.setStatus(
        "current"
    )

ruckusZDEventClientAuthFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 1, 66)
)
ruckusZDEventClientAuthFailed.setObjects(
      *(("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSerial"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventNEID"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSeverity"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventType"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTime"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventStatus"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTitle"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventClientMacAddr"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventAPMacAddr"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSSID"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventReason"))
)
if mibBuilder.loadTexts:
    ruckusZDEventClientAuthFailed.setStatus(
        "current"
    )

ruckusZDEventClientAuthorizationFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 1, 67)
)
ruckusZDEventClientAuthorizationFailed.setObjects(
      *(("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSerial"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventNEID"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSeverity"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventType"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTime"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventStatus"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTitle"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventClientMacAddr"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventAPMacAddr"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSSID"))
)
if mibBuilder.loadTexts:
    ruckusZDEventClientAuthorizationFailed.setStatus(
        "current"
    )

ruckusZDEventAPCPUvalve = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 1, 83)
)
ruckusZDEventAPCPUvalve.setObjects(
      *(("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSerial"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventNEID"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSeverity"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventType"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTime"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventStatus"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTitle"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventContent"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventAPMacAddr"))
)
if mibBuilder.loadTexts:
    ruckusZDEventAPCPUvalve.setStatus(
        "current"
    )

ruckusZDEventAPMEMvalve = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 1, 84)
)
ruckusZDEventAPMEMvalve.setObjects(
      *(("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSerial"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventNEID"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSeverity"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventType"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTime"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventStatus"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTitle"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventContent"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventAPMacAddr"))
)
if mibBuilder.loadTexts:
    ruckusZDEventAPMEMvalve.setStatus(
        "current"
    )

ruckusZDEventAPCPUvalveClrwarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 1, 85)
)
ruckusZDEventAPCPUvalveClrwarn.setObjects(
      *(("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSerial"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventNEID"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSeverity"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventType"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTime"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventStatus"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTitle"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventContent"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventAPMacAddr"))
)
if mibBuilder.loadTexts:
    ruckusZDEventAPCPUvalveClrwarn.setStatus(
        "current"
    )

ruckusZDEventAPMEMvalveClrwarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 1, 86)
)
ruckusZDEventAPMEMvalveClrwarn.setObjects(
      *(("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSerial"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventNEID"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSeverity"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventType"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTime"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventStatus"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTitle"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventContent"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventAPMacAddr"))
)
if mibBuilder.loadTexts:
    ruckusZDEventAPMEMvalveClrwarn.setStatus(
        "current"
    )

ruckusZDEventAPNumStaExceedValveClrwarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 1, 87)
)
ruckusZDEventAPNumStaExceedValveClrwarn.setObjects(
      *(("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSerial"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventNEID"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSeverity"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventType"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTime"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventStatus"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTitle"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventContent"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventAPMacAddr"))
)
if mibBuilder.loadTexts:
    ruckusZDEventAPNumStaExceedValveClrwarn.setStatus(
        "current"
    )

ruckusZDEventDhcpPoolFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 1, 88)
)
ruckusZDEventDhcpPoolFull.setObjects(
      *(("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSerial"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventNEID"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSeverity"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventType"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTime"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventStatus"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTitle"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventContent"))
)
if mibBuilder.loadTexts:
    ruckusZDEventDhcpPoolFull.setStatus(
        "current"
    )

ruckusZDEventDhcpPoolAbun = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 1, 89)
)
ruckusZDEventDhcpPoolAbun.setObjects(
      *(("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSerial"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventNEID"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventSeverity"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventType"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTime"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventStatus"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventTitle"),
        ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventContent"))
)
if mibBuilder.loadTexts:
    ruckusZDEventDhcpPoolAbun.setStatus(
        "current"
    )

ruckusZDEventSmartRedundancyChangetoActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 1, 100)
)
ruckusZDEventSmartRedundancyChangetoActive.setObjects(
    ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventIpAddr")
)
if mibBuilder.loadTexts:
    ruckusZDEventSmartRedundancyChangetoActive.setStatus(
        "current"
    )

ruckusZDEventSmartRedundancyActiveConnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 1, 101)
)
ruckusZDEventSmartRedundancyActiveConnected.setObjects(
    ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventIpAddr")
)
if mibBuilder.loadTexts:
    ruckusZDEventSmartRedundancyActiveConnected.setStatus(
        "current"
    )

ruckusZDEventSmartRedundancyActiveDisconnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 1, 102)
)
ruckusZDEventSmartRedundancyActiveDisconnected.setObjects(
    ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventIpAddr")
)
if mibBuilder.loadTexts:
    ruckusZDEventSmartRedundancyActiveDisconnected.setStatus(
        "current"
    )

ruckusZDEventSmartRedundancyStandbyConnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 1, 103)
)
ruckusZDEventSmartRedundancyStandbyConnected.setObjects(
    ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventIpAddr")
)
if mibBuilder.loadTexts:
    ruckusZDEventSmartRedundancyStandbyConnected.setStatus(
        "current"
    )

ruckusZDEventSmartRedundancyStandbyDisconnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 2, 1, 104)
)
ruckusZDEventSmartRedundancyStandbyDisconnected.setObjects(
    ("RUCKUS-ZD-EVENT-MIB", "ruckusZDEventIpAddr")
)
if mibBuilder.loadTexts:
    ruckusZDEventSmartRedundancyStandbyDisconnected.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUCKUS-ZD-EVENT-MIB",
    **{"ruckusZDEventMIB": ruckusZDEventMIB,
       "ruckusZDEventTraps": ruckusZDEventTraps,
       "ruckusZDEventAPJoinTrap": ruckusZDEventAPJoinTrap,
       "ruckusZDEventSSIDSpoofTrap": ruckusZDEventSSIDSpoofTrap,
       "ruckusZDEventMACSpoofTrap": ruckusZDEventMACSpoofTrap,
       "ruckusZDEventRogueAPTrap": ruckusZDEventRogueAPTrap,
       "ruckusZDEventAPLostTrap": ruckusZDEventAPLostTrap,
       "ruckusZDEventAPLostHeartbeatTrap": ruckusZDEventAPLostHeartbeatTrap,
       "ruckusZDEventClientAuthFailBlockTrap": ruckusZDEventClientAuthFailBlockTrap,
       "ruckusZDEventAPResetTrap": ruckusZDEventAPResetTrap,
       "ruckusZDEventIPChangeTrap": ruckusZDEventIPChangeTrap,
       "ruckusZDEventSystemColdStartTrap": ruckusZDEventSystemColdStartTrap,
       "ruckusZDEventAPChannelChangeTrap": ruckusZDEventAPChannelChangeTrap,
       "ruckusZDEventRadiusAuthUnavailableTrap": ruckusZDEventRadiusAuthUnavailableTrap,
       "ruckusZDEventRadiusAcctUnavailableTrap": ruckusZDEventRadiusAcctUnavailableTrap,
       "ruckusZDEventClientJoinFailAPBusyTrap": ruckusZDEventClientJoinFailAPBusyTrap,
       "ruckusZDEventInterferenceADHoc": ruckusZDEventInterferenceADHoc,
       "ruckusZDEventImageUpgradeFailTrap": ruckusZDEventImageUpgradeFailTrap,
       "ruckusZDEventHeartbeatTrap": ruckusZDEventHeartbeatTrap,
       "ruckusZDEventAttackedTrap": ruckusZDEventAttackedTrap,
       "ruckusZDEventSystemWarmStartTrap": ruckusZDEventSystemWarmStartTrap,
       "ruckusZDEventInterfereAPTrap": ruckusZDEventInterfereAPTrap,
       "ruckusZDEventAPSystemColdStartTrap": ruckusZDEventAPSystemColdStartTrap,
       "ruckusZDEventAPSystemWarmStartTrap": ruckusZDEventAPSystemWarmStartTrap,
       "ruckusZDEventAPSSIDChangedTrap": ruckusZDEventAPSSIDChangedTrap,
       "ruckusZDEventAPClientExceedValve": ruckusZDEventAPClientExceedValve,
       "ruckusZDEventAPAvailableStatusTrap": ruckusZDEventAPAvailableStatusTrap,
       "ruckusZDEventAPWirelessInterfaceFaultTrap": ruckusZDEventAPWirelessInterfaceFaultTrap,
       "ruckusZDEventSystemCpuUtilExceedValve": ruckusZDEventSystemCpuUtilExceedValve,
       "ruckusZDEventSystemMemUtilExceedValve": ruckusZDEventSystemMemUtilExceedValve,
       "ruckusZDEventSystemBandwidthUtilExceedValve": ruckusZDEventSystemBandwidthUtilExceedValve,
       "ruckusZDEventSystemDropPacketRateExceedValve": ruckusZDEventSystemDropPacketRateExceedValve,
       "ruckusZDEventAPSyncTimeFail": ruckusZDEventAPSyncTimeFail,
       "ruckusZDEventSystemCpuUtilClrWarn": ruckusZDEventSystemCpuUtilClrWarn,
       "ruckusZDEventSystemMemUtilClrwarn": ruckusZDEventSystemMemUtilClrwarn,
       "ruckusZDEventClientJoin": ruckusZDEventClientJoin,
       "ruckusZDEventClientJoinFailed": ruckusZDEventClientJoinFailed,
       "ruckusZDEventClientJoinFailedAPBusy": ruckusZDEventClientJoinFailedAPBusy,
       "ruckusZDEventClientDisconnect": ruckusZDEventClientDisconnect,
       "ruckusZDEventClientRoamOut": ruckusZDEventClientRoamOut,
       "ruckusZDEventClientRoamIn": ruckusZDEventClientRoamIn,
       "ruckusZDEventClientAuthFailed": ruckusZDEventClientAuthFailed,
       "ruckusZDEventClientAuthorizationFailed": ruckusZDEventClientAuthorizationFailed,
       "ruckusZDEventAPCPUvalve": ruckusZDEventAPCPUvalve,
       "ruckusZDEventAPMEMvalve": ruckusZDEventAPMEMvalve,
       "ruckusZDEventAPCPUvalveClrwarn": ruckusZDEventAPCPUvalveClrwarn,
       "ruckusZDEventAPMEMvalveClrwarn": ruckusZDEventAPMEMvalveClrwarn,
       "ruckusZDEventAPNumStaExceedValveClrwarn": ruckusZDEventAPNumStaExceedValveClrwarn,
       "ruckusZDEventDhcpPoolFull": ruckusZDEventDhcpPoolFull,
       "ruckusZDEventDhcpPoolAbun": ruckusZDEventDhcpPoolAbun,
       "ruckusZDEventSmartRedundancyChangetoActive": ruckusZDEventSmartRedundancyChangetoActive,
       "ruckusZDEventSmartRedundancyActiveConnected": ruckusZDEventSmartRedundancyActiveConnected,
       "ruckusZDEventSmartRedundancyActiveDisconnected": ruckusZDEventSmartRedundancyActiveDisconnected,
       "ruckusZDEventSmartRedundancyStandbyConnected": ruckusZDEventSmartRedundancyStandbyConnected,
       "ruckusZDEventSmartRedundancyStandbyDisconnected": ruckusZDEventSmartRedundancyStandbyDisconnected,
       "ruckusZDEventObjects": ruckusZDEventObjects,
       "ruckusZDEventSerial": ruckusZDEventSerial,
       "ruckusZDEventNEID": ruckusZDEventNEID,
       "ruckusZDEventSeverity": ruckusZDEventSeverity,
       "ruckusZDEventType": ruckusZDEventType,
       "ruckusZDEventTime": ruckusZDEventTime,
       "ruckusZDEventStatus": ruckusZDEventStatus,
       "ruckusZDEventTitle": ruckusZDEventTitle,
       "ruckusZDEventContent": ruckusZDEventContent,
       "ruckusZDEventClientMacAddr": ruckusZDEventClientMacAddr,
       "ruckusZDEventAPMacAddr": ruckusZDEventAPMacAddr,
       "ruckusZDEventRogueMacAddr": ruckusZDEventRogueMacAddr,
       "ruckusZDEventSSID": ruckusZDEventSSID,
       "ruckusZDEventChannel": ruckusZDEventChannel,
       "ruckusZDEventReason": ruckusZDEventReason,
       "ruckusZDEventIpAddr": ruckusZDEventIpAddr}
)
