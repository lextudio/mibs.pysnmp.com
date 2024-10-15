# SNMP MIB module (OPSUBP-DEVICE-SIGNALING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/OPSUBP-DEVICE-SIGNALING-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:35:25 2024
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

(nortel,) = mibBuilder.importSymbols(
    "NORTEL-MIB",
    "nortel")

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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

nnOpsUbpDeviceSignalingMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 562, 42, 5, 1, 3)
)
nnOpsUbpDeviceSignalingMIB.setRevisions(
        ("2013-04-12 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NnOPSNetIDGroup_ObjectIdentity = ObjectIdentity
nnOPSNetIDGroup = _NnOPSNetIDGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 42)
)
if mibBuilder.loadTexts:
    nnOPSNetIDGroup.setStatus("current")
_NnOPSMIBS_ObjectIdentity = ObjectIdentity
nnOPSMIBS = _NnOPSMIBS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 42, 5)
)
if mibBuilder.loadTexts:
    nnOPSMIBS.setStatus("current")
_NnOPSQoSRootOID_ObjectIdentity = ObjectIdentity
nnOPSQoSRootOID = _NnOPSQoSRootOID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 42, 5, 1)
)
if mibBuilder.loadTexts:
    nnOPSQoSRootOID.setStatus("current")
_NnOpsUbpDeviceSignalingMIBObjects_ObjectIdentity = ObjectIdentity
nnOpsUbpDeviceSignalingMIBObjects = _NnOpsUbpDeviceSignalingMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 42, 5, 1, 3, 1)
)
if mibBuilder.loadTexts:
    nnOpsUbpDeviceSignalingMIBObjects.setStatus("current")
_UbpNotifyObjects_ObjectIdentity = ObjectIdentity
ubpNotifyObjects = _UbpNotifyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 42, 5, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ubpNotifyObjects.setStatus("current")


class _UbpNotifyDeviceIdentifierType_Type(Integer32):
    """Custom type ubpNotifyDeviceIdentifierType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("devicemgmtadd", 1),
          ("snmpengineid", 2))
    )


_UbpNotifyDeviceIdentifierType_Type.__name__ = "Integer32"
_UbpNotifyDeviceIdentifierType_Object = MibScalar
ubpNotifyDeviceIdentifierType = _UbpNotifyDeviceIdentifierType_Object(
    (1, 3, 6, 1, 4, 1, 562, 42, 5, 1, 3, 1, 1, 1),
    _UbpNotifyDeviceIdentifierType_Type()
)
ubpNotifyDeviceIdentifierType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ubpNotifyDeviceIdentifierType.setStatus("current")
_UbpNotifyDeviceIdentifier_Type = DisplayString
_UbpNotifyDeviceIdentifier_Object = MibScalar
ubpNotifyDeviceIdentifier = _UbpNotifyDeviceIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 562, 42, 5, 1, 3, 1, 1, 2),
    _UbpNotifyDeviceIdentifier_Type()
)
ubpNotifyDeviceIdentifier.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ubpNotifyDeviceIdentifier.setStatus("current")
_UbpNotifyEAPAccessPortEntityIdentifier_Type = DisplayString
_UbpNotifyEAPAccessPortEntityIdentifier_Object = MibScalar
ubpNotifyEAPAccessPortEntityIdentifier = _UbpNotifyEAPAccessPortEntityIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 562, 42, 5, 1, 3, 1, 1, 3),
    _UbpNotifyEAPAccessPortEntityIdentifier_Type()
)
ubpNotifyEAPAccessPortEntityIdentifier.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ubpNotifyEAPAccessPortEntityIdentifier.setStatus("current")
_UbpNotifyEAPUserIdentifier_Type = DisplayString
_UbpNotifyEAPUserIdentifier_Object = MibScalar
ubpNotifyEAPUserIdentifier = _UbpNotifyEAPUserIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 562, 42, 5, 1, 3, 1, 1, 4),
    _UbpNotifyEAPUserIdentifier_Type()
)
ubpNotifyEAPUserIdentifier.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ubpNotifyEAPUserIdentifier.setStatus("current")
_UbpNotifyEAPUserGroupIdentifier_Type = DisplayString
_UbpNotifyEAPUserGroupIdentifier_Object = MibScalar
ubpNotifyEAPUserGroupIdentifier = _UbpNotifyEAPUserGroupIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 562, 42, 5, 1, 3, 1, 1, 5),
    _UbpNotifyEAPUserGroupIdentifier_Type()
)
ubpNotifyEAPUserGroupIdentifier.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ubpNotifyEAPUserGroupIdentifier.setStatus("current")
_UbpNotifyEAPUserRoles_Type = DisplayString
_UbpNotifyEAPUserRoles_Object = MibScalar
ubpNotifyEAPUserRoles = _UbpNotifyEAPUserRoles_Object(
    (1, 3, 6, 1, 4, 1, 562, 42, 5, 1, 3, 1, 1, 6),
    _UbpNotifyEAPUserRoles_Type()
)
ubpNotifyEAPUserRoles.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ubpNotifyEAPUserRoles.setStatus("current")
_UbpNotifyEAPSignalSequenceNumber_Type = Unsigned32
_UbpNotifyEAPSignalSequenceNumber_Object = MibScalar
ubpNotifyEAPSignalSequenceNumber = _UbpNotifyEAPSignalSequenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 562, 42, 5, 1, 3, 1, 1, 7),
    _UbpNotifyEAPSignalSequenceNumber_Type()
)
ubpNotifyEAPSignalSequenceNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ubpNotifyEAPSignalSequenceNumber.setStatus("current")
_UbpNotifyEAPSessionStartSignalSequenceNumber_Type = Unsigned32
_UbpNotifyEAPSessionStartSignalSequenceNumber_Object = MibScalar
ubpNotifyEAPSessionStartSignalSequenceNumber = _UbpNotifyEAPSessionStartSignalSequenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 562, 42, 5, 1, 3, 1, 1, 8),
    _UbpNotifyEAPSessionStartSignalSequenceNumber_Type()
)
ubpNotifyEAPSessionStartSignalSequenceNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ubpNotifyEAPSessionStartSignalSequenceNumber.setStatus("current")


class _UbpNotifyEAPSessionEndReason_Type(Integer32):
    """Custom type ubpNotifyEAPSessionEndReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eapsessionEndOther", 2),
          ("eapsessionEndUserlogoff", 1))
    )


_UbpNotifyEAPSessionEndReason_Type.__name__ = "Integer32"
_UbpNotifyEAPSessionEndReason_Object = MibScalar
ubpNotifyEAPSessionEndReason = _UbpNotifyEAPSessionEndReason_Object(
    (1, 3, 6, 1, 4, 1, 562, 42, 5, 1, 3, 1, 1, 9),
    _UbpNotifyEAPSessionEndReason_Type()
)
ubpNotifyEAPSessionEndReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ubpNotifyEAPSessionEndReason.setStatus("current")


class _UbpNotifyEAPAccessPortEntityOpenFlag_Type(Integer32):
    """Custom type ubpNotifyEAPAccessPortEntityOpenFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("eapAccessPortFlagNotApplicable", 1),
          ("eapAccessPortOpenNotRequired", 3),
          ("eapAccessPortOpenRequired", 2))
    )


_UbpNotifyEAPAccessPortEntityOpenFlag_Type.__name__ = "Integer32"
_UbpNotifyEAPAccessPortEntityOpenFlag_Object = MibScalar
ubpNotifyEAPAccessPortEntityOpenFlag = _UbpNotifyEAPAccessPortEntityOpenFlag_Object(
    (1, 3, 6, 1, 4, 1, 562, 42, 5, 1, 3, 1, 1, 10),
    _UbpNotifyEAPAccessPortEntityOpenFlag_Type()
)
ubpNotifyEAPAccessPortEntityOpenFlag.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ubpNotifyEAPAccessPortEntityOpenFlag.setStatus("current")
_UbpDeviceSignalingMIBNotifications_ObjectIdentity = ObjectIdentity
ubpDeviceSignalingMIBNotifications = _UbpDeviceSignalingMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 42, 5, 1, 3, 2)
)
_NnOpsUbpDeviceSignalingMIBConformance_ObjectIdentity = ObjectIdentity
nnOpsUbpDeviceSignalingMIBConformance = _NnOpsUbpDeviceSignalingMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 42, 5, 1, 3, 3)
)
if mibBuilder.loadTexts:
    nnOpsUbpDeviceSignalingMIBConformance.setStatus("current")
_NnOpsUbpDeviceSignalingMIBCompliances_ObjectIdentity = ObjectIdentity
nnOpsUbpDeviceSignalingMIBCompliances = _NnOpsUbpDeviceSignalingMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 42, 5, 1, 3, 3, 1)
)
_NnOpsUbpDeviceSignalingMIBGroups_ObjectIdentity = ObjectIdentity
nnOpsUbpDeviceSignalingMIBGroups = _NnOpsUbpDeviceSignalingMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 42, 5, 1, 3, 3, 2)
)

# Managed Objects groups

ubpNotifyObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 562, 42, 5, 1, 3, 3, 2, 1)
)
ubpNotifyObjectsGroup.setObjects(
      *(("OPSUBP-DEVICE-SIGNALING-MIB", "ubpNotifyDeviceIdentifierType"),
        ("OPSUBP-DEVICE-SIGNALING-MIB", "ubpNotifyDeviceIdentifier"),
        ("OPSUBP-DEVICE-SIGNALING-MIB", "ubpNotifyEAPAccessPortEntityIdentifier"),
        ("OPSUBP-DEVICE-SIGNALING-MIB", "ubpNotifyEAPUserIdentifier"),
        ("OPSUBP-DEVICE-SIGNALING-MIB", "ubpNotifyEAPUserGroupIdentifier"),
        ("OPSUBP-DEVICE-SIGNALING-MIB", "ubpNotifyEAPUserRoles"),
        ("OPSUBP-DEVICE-SIGNALING-MIB", "ubpNotifyEAPSignalSequenceNumber"),
        ("OPSUBP-DEVICE-SIGNALING-MIB", "ubpNotifyEAPSessionStartSignalSequenceNumber"),
        ("OPSUBP-DEVICE-SIGNALING-MIB", "ubpNotifyEAPSessionEndReason"),
        ("OPSUBP-DEVICE-SIGNALING-MIB", "ubpNotifyEAPAccessPortEntityOpenFlag"))
)
if mibBuilder.loadTexts:
    ubpNotifyObjectsGroup.setStatus("current")


# Notification objects

ubpEAPSessionStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 562, 42, 5, 1, 3, 2, 1)
)
ubpEAPSessionStart.setObjects(
      *(("OPSUBP-DEVICE-SIGNALING-MIB", "ubpNotifyDeviceIdentifierType"),
        ("OPSUBP-DEVICE-SIGNALING-MIB", "ubpNotifyDeviceIdentifier"),
        ("OPSUBP-DEVICE-SIGNALING-MIB", "ubpNotifyEAPAccessPortEntityIdentifier"),
        ("OPSUBP-DEVICE-SIGNALING-MIB", "ubpNotifyEAPUserIdentifier"),
        ("OPSUBP-DEVICE-SIGNALING-MIB", "ubpNotifyEAPUserGroupIdentifier"),
        ("OPSUBP-DEVICE-SIGNALING-MIB", "ubpNotifyEAPUserRoles"),
        ("OPSUBP-DEVICE-SIGNALING-MIB", "ubpNotifyEAPSignalSequenceNumber"),
        ("OPSUBP-DEVICE-SIGNALING-MIB", "ubpNotifyEAPAccessPortEntityOpenFlag"))
)
if mibBuilder.loadTexts:
    ubpEAPSessionStart.setStatus(
        "current"
    )

ubpEAPSessionEnd = NotificationType(
    (1, 3, 6, 1, 4, 1, 562, 42, 5, 1, 3, 2, 2)
)
ubpEAPSessionEnd.setObjects(
      *(("OPSUBP-DEVICE-SIGNALING-MIB", "ubpNotifyDeviceIdentifierType"),
        ("OPSUBP-DEVICE-SIGNALING-MIB", "ubpNotifyDeviceIdentifier"),
        ("OPSUBP-DEVICE-SIGNALING-MIB", "ubpNotifyEAPAccessPortEntityIdentifier"),
        ("OPSUBP-DEVICE-SIGNALING-MIB", "ubpNotifyEAPUserIdentifier"),
        ("OPSUBP-DEVICE-SIGNALING-MIB", "ubpNotifyEAPSessionEndReason"),
        ("OPSUBP-DEVICE-SIGNALING-MIB", "ubpNotifyEAPSignalSequenceNumber"),
        ("OPSUBP-DEVICE-SIGNALING-MIB", "ubpNotifyEAPSessionStartSignalSequenceNumber"))
)
if mibBuilder.loadTexts:
    ubpEAPSessionEnd.setStatus(
        "current"
    )


# Notifications groups

serverNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 562, 42, 5, 1, 3, 3, 2, 2)
)
serverNotificationsGroup.setObjects(
      *(("OPSUBP-DEVICE-SIGNALING-MIB", "ubpEAPSessionStart"),
        ("OPSUBP-DEVICE-SIGNALING-MIB", "ubpEAPSessionEnd"))
)
if mibBuilder.loadTexts:
    serverNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

nnOpsUbpDeviceSignalingMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 562, 42, 5, 1, 3, 3, 1, 1)
)
if mibBuilder.loadTexts:
    nnOpsUbpDeviceSignalingMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OPSUBP-DEVICE-SIGNALING-MIB",
    **{"nnOPSNetIDGroup": nnOPSNetIDGroup,
       "nnOPSMIBS": nnOPSMIBS,
       "nnOPSQoSRootOID": nnOPSQoSRootOID,
       "nnOpsUbpDeviceSignalingMIB": nnOpsUbpDeviceSignalingMIB,
       "nnOpsUbpDeviceSignalingMIBObjects": nnOpsUbpDeviceSignalingMIBObjects,
       "ubpNotifyObjects": ubpNotifyObjects,
       "ubpNotifyDeviceIdentifierType": ubpNotifyDeviceIdentifierType,
       "ubpNotifyDeviceIdentifier": ubpNotifyDeviceIdentifier,
       "ubpNotifyEAPAccessPortEntityIdentifier": ubpNotifyEAPAccessPortEntityIdentifier,
       "ubpNotifyEAPUserIdentifier": ubpNotifyEAPUserIdentifier,
       "ubpNotifyEAPUserGroupIdentifier": ubpNotifyEAPUserGroupIdentifier,
       "ubpNotifyEAPUserRoles": ubpNotifyEAPUserRoles,
       "ubpNotifyEAPSignalSequenceNumber": ubpNotifyEAPSignalSequenceNumber,
       "ubpNotifyEAPSessionStartSignalSequenceNumber": ubpNotifyEAPSessionStartSignalSequenceNumber,
       "ubpNotifyEAPSessionEndReason": ubpNotifyEAPSessionEndReason,
       "ubpNotifyEAPAccessPortEntityOpenFlag": ubpNotifyEAPAccessPortEntityOpenFlag,
       "ubpDeviceSignalingMIBNotifications": ubpDeviceSignalingMIBNotifications,
       "ubpEAPSessionStart": ubpEAPSessionStart,
       "ubpEAPSessionEnd": ubpEAPSessionEnd,
       "nnOpsUbpDeviceSignalingMIBConformance": nnOpsUbpDeviceSignalingMIBConformance,
       "nnOpsUbpDeviceSignalingMIBCompliances": nnOpsUbpDeviceSignalingMIBCompliances,
       "nnOpsUbpDeviceSignalingMIBCompliance": nnOpsUbpDeviceSignalingMIBCompliance,
       "nnOpsUbpDeviceSignalingMIBGroups": nnOpsUbpDeviceSignalingMIBGroups,
       "ubpNotifyObjectsGroup": ubpNotifyObjectsGroup,
       "serverNotificationsGroup": serverNotificationsGroup}
)
