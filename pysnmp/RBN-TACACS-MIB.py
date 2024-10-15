# SNMP MIB module (RBN-TACACS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RBN-TACACS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:45:27 2024
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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(rbnMgmt,) = mibBuilder.importSymbols(
    "RBN-SMI",
    "rbnMgmt")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

rbnTacacsMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 33)
)
rbnTacacsMib.setRevisions(
        ("2004-03-01 18:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class RbnTacacsState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 3),
          ("unknown", 1),
          ("up", 2))
    )



class RbnTacacsReason(Integer32, TextualConvention):
    status = "current"
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
        *(("packetTimeout", 2),
          ("responding", 1),
          ("serverError", 4),
          ("serverTimeout", 3))
    )



# MIB Managed Objects in the order of their OIDs

_RbnTacacsMIBNotifications_ObjectIdentity = ObjectIdentity
rbnTacacsMIBNotifications = _RbnTacacsMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 33, 0)
)
_RbnTacacsMIBObjects_ObjectIdentity = ObjectIdentity
rbnTacacsMIBObjects = _RbnTacacsMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 33, 1)
)
_RbnTacacsObjects_ObjectIdentity = ObjectIdentity
rbnTacacsObjects = _RbnTacacsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 33, 1, 1)
)
_RbnTacacsAcctObjects_ObjectIdentity = ObjectIdentity
rbnTacacsAcctObjects = _RbnTacacsAcctObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 33, 1, 2)
)
_RbnTacacsNotifyObjects_ObjectIdentity = ObjectIdentity
rbnTacacsNotifyObjects = _RbnTacacsNotifyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 33, 1, 3)
)


class _RbnTacacsContext_Type(SnmpAdminString):
    """Custom type rbnTacacsContext based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_RbnTacacsContext_Type.__name__ = "SnmpAdminString"
_RbnTacacsContext_Object = MibScalar
rbnTacacsContext = _RbnTacacsContext_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 33, 1, 3, 1),
    _RbnTacacsContext_Type()
)
rbnTacacsContext.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbnTacacsContext.setStatus("current")


class _RbnTacacsServerIndex_Type(Unsigned32):
    """Custom type rbnTacacsServerIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_RbnTacacsServerIndex_Type.__name__ = "Unsigned32"
_RbnTacacsServerIndex_Object = MibScalar
rbnTacacsServerIndex = _RbnTacacsServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 33, 1, 3, 2),
    _RbnTacacsServerIndex_Type()
)
rbnTacacsServerIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbnTacacsServerIndex.setStatus("current")
_RbnTacacsServerAddressType_Type = InetAddressType
_RbnTacacsServerAddressType_Object = MibScalar
rbnTacacsServerAddressType = _RbnTacacsServerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 33, 1, 3, 3),
    _RbnTacacsServerAddressType_Type()
)
rbnTacacsServerAddressType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbnTacacsServerAddressType.setStatus("current")
_RbnTacacsServerAddress_Type = InetAddress
_RbnTacacsServerAddress_Object = MibScalar
rbnTacacsServerAddress = _RbnTacacsServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 33, 1, 3, 4),
    _RbnTacacsServerAddress_Type()
)
rbnTacacsServerAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbnTacacsServerAddress.setStatus("current")


class _RbnTacacsServerPort_Type(Unsigned32):
    """Custom type rbnTacacsServerPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RbnTacacsServerPort_Type.__name__ = "Unsigned32"
_RbnTacacsServerPort_Object = MibScalar
rbnTacacsServerPort = _RbnTacacsServerPort_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 33, 1, 3, 5),
    _RbnTacacsServerPort_Type()
)
rbnTacacsServerPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbnTacacsServerPort.setStatus("current")
_RbnTacacsServerState_Type = RbnTacacsState
_RbnTacacsServerState_Object = MibScalar
rbnTacacsServerState = _RbnTacacsServerState_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 33, 1, 3, 6),
    _RbnTacacsServerState_Type()
)
rbnTacacsServerState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbnTacacsServerState.setStatus("current")
_RbnTacacsServerReason_Type = RbnTacacsReason
_RbnTacacsServerReason_Object = MibScalar
rbnTacacsServerReason = _RbnTacacsServerReason_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 33, 1, 3, 7),
    _RbnTacacsServerReason_Type()
)
rbnTacacsServerReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbnTacacsServerReason.setStatus("current")


class _RbnTacacsUserName_Type(SnmpAdminString):
    """Custom type rbnTacacsUserName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RbnTacacsUserName_Type.__name__ = "SnmpAdminString"
_RbnTacacsUserName_Object = MibScalar
rbnTacacsUserName = _RbnTacacsUserName_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 33, 1, 3, 8),
    _RbnTacacsUserName_Type()
)
rbnTacacsUserName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbnTacacsUserName.setStatus("current")


class _RbnTacacsServerMsg_Type(SnmpAdminString):
    """Custom type rbnTacacsServerMsg based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_RbnTacacsServerMsg_Type.__name__ = "SnmpAdminString"
_RbnTacacsServerMsg_Object = MibScalar
rbnTacacsServerMsg = _RbnTacacsServerMsg_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 33, 1, 3, 9),
    _RbnTacacsServerMsg_Type()
)
rbnTacacsServerMsg.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbnTacacsServerMsg.setStatus("current")
_RbnTacacsMIBConformance_ObjectIdentity = ObjectIdentity
rbnTacacsMIBConformance = _RbnTacacsMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 33, 2)
)
_RbnTacacsCompliances_ObjectIdentity = ObjectIdentity
rbnTacacsCompliances = _RbnTacacsCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 33, 2, 1)
)
_RbnTacacsGroups_ObjectIdentity = ObjectIdentity
rbnTacacsGroups = _RbnTacacsGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 33, 2, 2)
)

# Managed Objects groups

rbnTacacsNotifyObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 33, 2, 2, 2)
)
rbnTacacsNotifyObjectsGroup.setObjects(
      *(("RBN-TACACS-MIB", "rbnTacacsContext"),
        ("RBN-TACACS-MIB", "rbnTacacsServerIndex"),
        ("RBN-TACACS-MIB", "rbnTacacsServerAddressType"),
        ("RBN-TACACS-MIB", "rbnTacacsServerAddress"),
        ("RBN-TACACS-MIB", "rbnTacacsServerPort"),
        ("RBN-TACACS-MIB", "rbnTacacsServerState"),
        ("RBN-TACACS-MIB", "rbnTacacsServerReason"),
        ("RBN-TACACS-MIB", "rbnTacacsUserName"),
        ("RBN-TACACS-MIB", "rbnTacacsServerMsg"))
)
if mibBuilder.loadTexts:
    rbnTacacsNotifyObjectsGroup.setStatus("current")


# Notification objects

rbnTacacsStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2352, 2, 33, 0, 1)
)
rbnTacacsStateChange.setObjects(
      *(("RBN-TACACS-MIB", "rbnTacacsContext"),
        ("RBN-TACACS-MIB", "rbnTacacsServerIndex"),
        ("RBN-TACACS-MIB", "rbnTacacsServerAddressType"),
        ("RBN-TACACS-MIB", "rbnTacacsServerAddress"),
        ("RBN-TACACS-MIB", "rbnTacacsServerPort"),
        ("RBN-TACACS-MIB", "rbnTacacsServerState"),
        ("RBN-TACACS-MIB", "rbnTacacsServerReason"),
        ("RBN-TACACS-MIB", "rbnTacacsUserName"),
        ("RBN-TACACS-MIB", "rbnTacacsServerMsg"))
)
if mibBuilder.loadTexts:
    rbnTacacsStateChange.setStatus(
        "current"
    )


# Notifications groups

rbnTacacsNotifyGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 33, 2, 2, 3)
)
rbnTacacsNotifyGroup.setObjects(
    ("RBN-TACACS-MIB", "rbnTacacsStateChange")
)
if mibBuilder.loadTexts:
    rbnTacacsNotifyGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

rbnTacacsCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2352, 2, 33, 2, 1, 1)
)
if mibBuilder.loadTexts:
    rbnTacacsCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RBN-TACACS-MIB",
    **{"RbnTacacsState": RbnTacacsState,
       "RbnTacacsReason": RbnTacacsReason,
       "rbnTacacsMib": rbnTacacsMib,
       "rbnTacacsMIBNotifications": rbnTacacsMIBNotifications,
       "rbnTacacsStateChange": rbnTacacsStateChange,
       "rbnTacacsMIBObjects": rbnTacacsMIBObjects,
       "rbnTacacsObjects": rbnTacacsObjects,
       "rbnTacacsAcctObjects": rbnTacacsAcctObjects,
       "rbnTacacsNotifyObjects": rbnTacacsNotifyObjects,
       "rbnTacacsContext": rbnTacacsContext,
       "rbnTacacsServerIndex": rbnTacacsServerIndex,
       "rbnTacacsServerAddressType": rbnTacacsServerAddressType,
       "rbnTacacsServerAddress": rbnTacacsServerAddress,
       "rbnTacacsServerPort": rbnTacacsServerPort,
       "rbnTacacsServerState": rbnTacacsServerState,
       "rbnTacacsServerReason": rbnTacacsServerReason,
       "rbnTacacsUserName": rbnTacacsUserName,
       "rbnTacacsServerMsg": rbnTacacsServerMsg,
       "rbnTacacsMIBConformance": rbnTacacsMIBConformance,
       "rbnTacacsCompliances": rbnTacacsCompliances,
       "rbnTacacsCompliance": rbnTacacsCompliance,
       "rbnTacacsGroups": rbnTacacsGroups,
       "rbnTacacsNotifyObjectsGroup": rbnTacacsNotifyObjectsGroup,
       "rbnTacacsNotifyGroup": rbnTacacsNotifyGroup}
)
