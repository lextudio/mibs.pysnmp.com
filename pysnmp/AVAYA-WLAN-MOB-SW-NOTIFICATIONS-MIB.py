# SNMP MIB module (AVAYA-WLAN-MOB-SW-NOTIFICATIONS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AVAYA-WLAN-MOB-SW-NOTIFICATIONS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:44:38 2024
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

(AvWlanMobVlanRole,
 AvWlanMobVlanState,
 AvWlanSwitchNotifAuxLimitsMap) = mibBuilder.importSymbols(
    "AVAYA-WLAN-TC-MIB",
    "AvWlanMobVlanRole",
    "AvWlanMobVlanState",
    "AvWlanSwitchNotifAuxLimitsMap")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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

(DisplayString,
 MacAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention")

(avayaWlanMibs,) = mibBuilder.importSymbols(
    "SYNOPTICS-ROOT-MIB",
    "avayaWlanMibs")


# MODULE-IDENTITY

avayaWlanMobSwitchNotificationsMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 45, 7, 19)
)
avayaWlanMobSwitchNotificationsMib.setRevisions(
        ("2011-12-15 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AvWlanMobSwNotifications_ObjectIdentity = ObjectIdentity
avWlanMobSwNotifications = _AvWlanMobSwNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 7, 19, 0)
)
_AvWlanSwitchNotifications_ObjectIdentity = ObjectIdentity
avWlanSwitchNotifications = _AvWlanSwitchNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 7, 19, 0, 1)
)
_AvWlanMobSwNotificationObjects_ObjectIdentity = ObjectIdentity
avWlanMobSwNotificationObjects = _AvWlanMobSwNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 7, 19, 1)
)
_AvWlanMobSwNotificationAuxObjects_ObjectIdentity = ObjectIdentity
avWlanMobSwNotificationAuxObjects = _AvWlanMobSwNotificationAuxObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 7, 19, 1, 1)
)
_AvWlanNotifAuxMobilityControllerInetAddressType_Type = InetAddressType
_AvWlanNotifAuxMobilityControllerInetAddressType_Object = MibScalar
avWlanNotifAuxMobilityControllerInetAddressType = _AvWlanNotifAuxMobilityControllerInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 45, 7, 19, 1, 1, 1),
    _AvWlanNotifAuxMobilityControllerInetAddressType_Type()
)
avWlanNotifAuxMobilityControllerInetAddressType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    avWlanNotifAuxMobilityControllerInetAddressType.setStatus("current")
_AvWlanNotifAuxMobilityControllerInetAddress_Type = InetAddress
_AvWlanNotifAuxMobilityControllerInetAddress_Object = MibScalar
avWlanNotifAuxMobilityControllerInetAddress = _AvWlanNotifAuxMobilityControllerInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 45, 7, 19, 1, 1, 2),
    _AvWlanNotifAuxMobilityControllerInetAddress_Type()
)
avWlanNotifAuxMobilityControllerInetAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    avWlanNotifAuxMobilityControllerInetAddress.setStatus("current")
_AvWlanNotifAuxNumberOfVlanEntries_Type = Unsigned32
_AvWlanNotifAuxNumberOfVlanEntries_Object = MibScalar
avWlanNotifAuxNumberOfVlanEntries = _AvWlanNotifAuxNumberOfVlanEntries_Object(
    (1, 3, 6, 1, 4, 1, 45, 7, 19, 1, 1, 3),
    _AvWlanNotifAuxNumberOfVlanEntries_Type()
)
avWlanNotifAuxNumberOfVlanEntries.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    avWlanNotifAuxNumberOfVlanEntries.setStatus("current")
_AvWlanNotifAuxMSTDownloadEntries_Type = Unsigned32
_AvWlanNotifAuxMSTDownloadEntries_Object = MibScalar
avWlanNotifAuxMSTDownloadEntries = _AvWlanNotifAuxMSTDownloadEntries_Object(
    (1, 3, 6, 1, 4, 1, 45, 7, 19, 1, 1, 4),
    _AvWlanNotifAuxMSTDownloadEntries_Type()
)
avWlanNotifAuxMSTDownloadEntries.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    avWlanNotifAuxMSTDownloadEntries.setStatus("current")
_AvWlanNotifAuxPeerDeviceInetAddressType_Type = InetAddressType
_AvWlanNotifAuxPeerDeviceInetAddressType_Object = MibScalar
avWlanNotifAuxPeerDeviceInetAddressType = _AvWlanNotifAuxPeerDeviceInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 45, 7, 19, 1, 1, 5),
    _AvWlanNotifAuxPeerDeviceInetAddressType_Type()
)
avWlanNotifAuxPeerDeviceInetAddressType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    avWlanNotifAuxPeerDeviceInetAddressType.setStatus("current")
_AvWlanNotifAuxPeerDeviceInetAddress_Type = InetAddress
_AvWlanNotifAuxPeerDeviceInetAddress_Object = MibScalar
avWlanNotifAuxPeerDeviceInetAddress = _AvWlanNotifAuxPeerDeviceInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 45, 7, 19, 1, 1, 6),
    _AvWlanNotifAuxPeerDeviceInetAddress_Type()
)
avWlanNotifAuxPeerDeviceInetAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    avWlanNotifAuxPeerDeviceInetAddress.setStatus("current")
_AvWlanNotifAuxPeerDeviceAddress_Type = MacAddress
_AvWlanNotifAuxPeerDeviceAddress_Object = MibScalar
avWlanNotifAuxPeerDeviceAddress = _AvWlanNotifAuxPeerDeviceAddress_Object(
    (1, 3, 6, 1, 4, 1, 45, 7, 19, 1, 1, 7),
    _AvWlanNotifAuxPeerDeviceAddress_Type()
)
avWlanNotifAuxPeerDeviceAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    avWlanNotifAuxPeerDeviceAddress.setStatus("current")


class _AvWlanNotifAuxPeerDeviceType_Type(Integer32):
    """Custom type avWlanNotifAuxPeerDeviceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("accessPoint", 1),
          ("mobilitySwitch", 2))
    )


_AvWlanNotifAuxPeerDeviceType_Type.__name__ = "Integer32"
_AvWlanNotifAuxPeerDeviceType_Object = MibScalar
avWlanNotifAuxPeerDeviceType = _AvWlanNotifAuxPeerDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 45, 7, 19, 1, 1, 8),
    _AvWlanNotifAuxPeerDeviceType_Type()
)
avWlanNotifAuxPeerDeviceType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    avWlanNotifAuxPeerDeviceType.setStatus("current")


class _AvWlanNotifAuxConnectionFailureReason_Type(Integer32):
    """Custom type avWlanNotifAuxConnectionFailureReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("controlPlane", 2),
          ("kaLoss", 1),
          ("peerReset", 3))
    )


_AvWlanNotifAuxConnectionFailureReason_Type.__name__ = "Integer32"
_AvWlanNotifAuxConnectionFailureReason_Object = MibScalar
avWlanNotifAuxConnectionFailureReason = _AvWlanNotifAuxConnectionFailureReason_Object(
    (1, 3, 6, 1, 4, 1, 45, 7, 19, 1, 1, 9),
    _AvWlanNotifAuxConnectionFailureReason_Type()
)
avWlanNotifAuxConnectionFailureReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    avWlanNotifAuxConnectionFailureReason.setStatus("current")


class _AvWlanNotifAuxMobilityVlanName_Type(SnmpAdminString):
    """Custom type avWlanNotifAuxMobilityVlanName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AvWlanNotifAuxMobilityVlanName_Type.__name__ = "SnmpAdminString"
_AvWlanNotifAuxMobilityVlanName_Object = MibScalar
avWlanNotifAuxMobilityVlanName = _AvWlanNotifAuxMobilityVlanName_Object(
    (1, 3, 6, 1, 4, 1, 45, 7, 19, 1, 1, 10),
    _AvWlanNotifAuxMobilityVlanName_Type()
)
avWlanNotifAuxMobilityVlanName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    avWlanNotifAuxMobilityVlanName.setStatus("current")
_AvWlanNotifAuxVlanServerInetAddressType_Type = InetAddressType
_AvWlanNotifAuxVlanServerInetAddressType_Object = MibScalar
avWlanNotifAuxVlanServerInetAddressType = _AvWlanNotifAuxVlanServerInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 45, 7, 19, 1, 1, 11),
    _AvWlanNotifAuxVlanServerInetAddressType_Type()
)
avWlanNotifAuxVlanServerInetAddressType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    avWlanNotifAuxVlanServerInetAddressType.setStatus("current")
_AvWlanNotifAuxVlanServerInetAddress_Type = InetAddress
_AvWlanNotifAuxVlanServerInetAddress_Object = MibScalar
avWlanNotifAuxVlanServerInetAddress = _AvWlanNotifAuxVlanServerInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 45, 7, 19, 1, 1, 12),
    _AvWlanNotifAuxVlanServerInetAddress_Type()
)
avWlanNotifAuxVlanServerInetAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    avWlanNotifAuxVlanServerInetAddress.setStatus("current")
_AvWlanNotifAuxVlanServerAddress_Type = MacAddress
_AvWlanNotifAuxVlanServerAddress_Object = MibScalar
avWlanNotifAuxVlanServerAddress = _AvWlanNotifAuxVlanServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 45, 7, 19, 1, 1, 13),
    _AvWlanNotifAuxVlanServerAddress_Type()
)
avWlanNotifAuxVlanServerAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    avWlanNotifAuxVlanServerAddress.setStatus("current")
_AvWlanNotifAuxMobilityVlanSelfGenerationNumber_Type = Unsigned32
_AvWlanNotifAuxMobilityVlanSelfGenerationNumber_Object = MibScalar
avWlanNotifAuxMobilityVlanSelfGenerationNumber = _AvWlanNotifAuxMobilityVlanSelfGenerationNumber_Object(
    (1, 3, 6, 1, 4, 1, 45, 7, 19, 1, 1, 14),
    _AvWlanNotifAuxMobilityVlanSelfGenerationNumber_Type()
)
avWlanNotifAuxMobilityVlanSelfGenerationNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    avWlanNotifAuxMobilityVlanSelfGenerationNumber.setStatus("current")
_AvWlanNotifAuxMobilityVlanPeerGenerationNumber_Type = Unsigned32
_AvWlanNotifAuxMobilityVlanPeerGenerationNumber_Object = MibScalar
avWlanNotifAuxMobilityVlanPeerGenerationNumber = _AvWlanNotifAuxMobilityVlanPeerGenerationNumber_Object(
    (1, 3, 6, 1, 4, 1, 45, 7, 19, 1, 1, 15),
    _AvWlanNotifAuxMobilityVlanPeerGenerationNumber_Type()
)
avWlanNotifAuxMobilityVlanPeerGenerationNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    avWlanNotifAuxMobilityVlanPeerGenerationNumber.setStatus("current")
_AvWlanNotifAuxOldVlanRole_Type = AvWlanMobVlanRole
_AvWlanNotifAuxOldVlanRole_Object = MibScalar
avWlanNotifAuxOldVlanRole = _AvWlanNotifAuxOldVlanRole_Object(
    (1, 3, 6, 1, 4, 1, 45, 7, 19, 1, 1, 16),
    _AvWlanNotifAuxOldVlanRole_Type()
)
avWlanNotifAuxOldVlanRole.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    avWlanNotifAuxOldVlanRole.setStatus("current")
_AvWlanNotifAuxNewVlanRole_Type = AvWlanMobVlanRole
_AvWlanNotifAuxNewVlanRole_Object = MibScalar
avWlanNotifAuxNewVlanRole = _AvWlanNotifAuxNewVlanRole_Object(
    (1, 3, 6, 1, 4, 1, 45, 7, 19, 1, 1, 17),
    _AvWlanNotifAuxNewVlanRole_Type()
)
avWlanNotifAuxNewVlanRole.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    avWlanNotifAuxNewVlanRole.setStatus("current")


class _AvWlanNotifAuxRoleChangeReason_Type(Integer32):
    """Custom type avWlanNotifAuxRoleChangeReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("administrator", 1),
          ("clientRoam", 2))
    )


_AvWlanNotifAuxRoleChangeReason_Type.__name__ = "Integer32"
_AvWlanNotifAuxRoleChangeReason_Object = MibScalar
avWlanNotifAuxRoleChangeReason = _AvWlanNotifAuxRoleChangeReason_Object(
    (1, 3, 6, 1, 4, 1, 45, 7, 19, 1, 1, 18),
    _AvWlanNotifAuxRoleChangeReason_Type()
)
avWlanNotifAuxRoleChangeReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    avWlanNotifAuxRoleChangeReason.setStatus("current")
_AvWlanNotifAuxOldState_Type = AvWlanMobVlanState
_AvWlanNotifAuxOldState_Object = MibScalar
avWlanNotifAuxOldState = _AvWlanNotifAuxOldState_Object(
    (1, 3, 6, 1, 4, 1, 45, 7, 19, 1, 1, 19),
    _AvWlanNotifAuxOldState_Type()
)
avWlanNotifAuxOldState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    avWlanNotifAuxOldState.setStatus("current")
_AvWlanNotifAuxNewState_Type = AvWlanMobVlanState
_AvWlanNotifAuxNewState_Object = MibScalar
avWlanNotifAuxNewState = _AvWlanNotifAuxNewState_Object(
    (1, 3, 6, 1, 4, 1, 45, 7, 19, 1, 1, 20),
    _AvWlanNotifAuxNewState_Type()
)
avWlanNotifAuxNewState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    avWlanNotifAuxNewState.setStatus("current")


class _AvWlanNotifAuxStateChangeReason_Type(Integer32):
    """Custom type avWlanNotifAuxStateChangeReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("localVlanDeleted", 3),
          ("mobVlanCreated", 2),
          ("mobVlanDeleted", 1))
    )


_AvWlanNotifAuxStateChangeReason_Type.__name__ = "Integer32"
_AvWlanNotifAuxStateChangeReason_Object = MibScalar
avWlanNotifAuxStateChangeReason = _AvWlanNotifAuxStateChangeReason_Object(
    (1, 3, 6, 1, 4, 1, 45, 7, 19, 1, 1, 21),
    _AvWlanNotifAuxStateChangeReason_Type()
)
avWlanNotifAuxStateChangeReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    avWlanNotifAuxStateChangeReason.setStatus("current")
_AvWlanNotifAuxVlanState_Type = AvWlanMobVlanState
_AvWlanNotifAuxVlanState_Object = MibScalar
avWlanNotifAuxVlanState = _AvWlanNotifAuxVlanState_Object(
    (1, 3, 6, 1, 4, 1, 45, 7, 19, 1, 1, 22),
    _AvWlanNotifAuxVlanState_Type()
)
avWlanNotifAuxVlanState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    avWlanNotifAuxVlanState.setStatus("current")


class _AvWlanNotifAuxRemoveReason_Type(Integer32):
    """Custom type avWlanNotifAuxRemoveReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("administrator", 1),
          ("lvidDeletion", 2))
    )


_AvWlanNotifAuxRemoveReason_Type.__name__ = "Integer32"
_AvWlanNotifAuxRemoveReason_Object = MibScalar
avWlanNotifAuxRemoveReason = _AvWlanNotifAuxRemoveReason_Object(
    (1, 3, 6, 1, 4, 1, 45, 7, 19, 1, 1, 23),
    _AvWlanNotifAuxRemoveReason_Type()
)
avWlanNotifAuxRemoveReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    avWlanNotifAuxRemoveReason.setStatus("current")


class _AvWlanNotifAuxControlFrameType_Type(Integer32):
    """Custom type avWlanNotifAuxControlFrameType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("igmpLeave", 2),
          ("igmpReport", 1))
    )


_AvWlanNotifAuxControlFrameType_Type.__name__ = "Integer32"
_AvWlanNotifAuxControlFrameType_Object = MibScalar
avWlanNotifAuxControlFrameType = _AvWlanNotifAuxControlFrameType_Object(
    (1, 3, 6, 1, 4, 1, 45, 7, 19, 1, 1, 24),
    _AvWlanNotifAuxControlFrameType_Type()
)
avWlanNotifAuxControlFrameType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    avWlanNotifAuxControlFrameType.setStatus("current")
_AvWlanNotifAuxInetAddressType_Type = InetAddressType
_AvWlanNotifAuxInetAddressType_Object = MibScalar
avWlanNotifAuxInetAddressType = _AvWlanNotifAuxInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 45, 7, 19, 1, 1, 25),
    _AvWlanNotifAuxInetAddressType_Type()
)
avWlanNotifAuxInetAddressType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    avWlanNotifAuxInetAddressType.setStatus("current")
_AvWlanNotifAuxInetAddress_Type = InetAddress
_AvWlanNotifAuxInetAddress_Object = MibScalar
avWlanNotifAuxInetAddress = _AvWlanNotifAuxInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 45, 7, 19, 1, 1, 26),
    _AvWlanNotifAuxInetAddress_Type()
)
avWlanNotifAuxInetAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    avWlanNotifAuxInetAddress.setStatus("current")
_AvWlanSwitchNotifAuxAuxLimitsReached_Type = AvWlanSwitchNotifAuxLimitsMap
_AvWlanSwitchNotifAuxAuxLimitsReached_Object = MibScalar
avWlanSwitchNotifAuxAuxLimitsReached = _AvWlanSwitchNotifAuxAuxLimitsReached_Object(
    (1, 3, 6, 1, 4, 1, 45, 7, 19, 1, 1, 27),
    _AvWlanSwitchNotifAuxAuxLimitsReached_Type()
)
avWlanSwitchNotifAuxAuxLimitsReached.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    avWlanSwitchNotifAuxAuxLimitsReached.setStatus("current")

# Managed Objects groups


# Notification objects

avWlanSwitchMCPConnectionEstablished = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 7, 19, 0, 1, 1)
)
avWlanSwitchMCPConnectionEstablished.setObjects(
      *(("AVAYA-WLAN-MOB-SW-NOTIFICATIONS-MIB", "avWlanNotifAuxMobilityControllerInetAddressType"),
        ("AVAYA-WLAN-MOB-SW-NOTIFICATIONS-MIB", "avWlanNotifAuxMobilityControllerInetAddress"))
)
if mibBuilder.loadTexts:
    avWlanSwitchMCPConnectionEstablished.setStatus(
        "current"
    )

avWlanSwitchMCPLostConnection = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 7, 19, 0, 1, 2)
)
avWlanSwitchMCPLostConnection.setObjects(
      *(("AVAYA-WLAN-MOB-SW-NOTIFICATIONS-MIB", "avWlanNotifAuxMobilityControllerInetAddressType"),
        ("AVAYA-WLAN-MOB-SW-NOTIFICATIONS-MIB", "avWlanNotifAuxMobilityControllerInetAddress"))
)
if mibBuilder.loadTexts:
    avWlanSwitchMCPLostConnection.setStatus(
        "current"
    )

avWlanSwitchMVTDownload = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 7, 19, 0, 1, 3)
)
avWlanSwitchMVTDownload.setObjects(
      *(("AVAYA-WLAN-MOB-SW-NOTIFICATIONS-MIB", "avWlanNotifAuxMobilityControllerInetAddressType"),
        ("AVAYA-WLAN-MOB-SW-NOTIFICATIONS-MIB", "avWlanNotifAuxMobilityControllerInetAddress"),
        ("AVAYA-WLAN-MOB-SW-NOTIFICATIONS-MIB", "avWlanNotifAuxNumberOfVlanEntries"))
)
if mibBuilder.loadTexts:
    avWlanSwitchMVTDownload.setStatus(
        "current"
    )

avWlanSwitchMSTDownload = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 7, 19, 0, 1, 4)
)
avWlanSwitchMSTDownload.setObjects(
      *(("AVAYA-WLAN-MOB-SW-NOTIFICATIONS-MIB", "avWlanNotifAuxMobilityControllerInetAddressType"),
        ("AVAYA-WLAN-MOB-SW-NOTIFICATIONS-MIB", "avWlanNotifAuxMobilityControllerInetAddress"),
        ("AVAYA-WLAN-MOB-SW-NOTIFICATIONS-MIB", "avWlanNotifAuxMSTDownloadEntries"))
)
if mibBuilder.loadTexts:
    avWlanSwitchMSTDownload.setStatus(
        "current"
    )

avWlanSwitchPeerDeviceConnectionEstablished = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 7, 19, 0, 1, 5)
)
avWlanSwitchPeerDeviceConnectionEstablished.setObjects(
      *(("AVAYA-WLAN-MOB-SW-NOTIFICATIONS-MIB", "avWlanNotifAuxPeerDeviceInetAddressType"),
        ("AVAYA-WLAN-MOB-SW-NOTIFICATIONS-MIB", "avWlanNotifAuxPeerDeviceInetAddress"),
        ("AVAYA-WLAN-MOB-SW-NOTIFICATIONS-MIB", "avWlanNotifAuxPeerDeviceAddress"),
        ("AVAYA-WLAN-MOB-SW-NOTIFICATIONS-MIB", "avWlanNotifAuxPeerDeviceType"))
)
if mibBuilder.loadTexts:
    avWlanSwitchPeerDeviceConnectionEstablished.setStatus(
        "current"
    )

avWlanSwitchPeerDeviceLostConnection = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 7, 19, 0, 1, 6)
)
avWlanSwitchPeerDeviceLostConnection.setObjects(
      *(("AVAYA-WLAN-MOB-SW-NOTIFICATIONS-MIB", "avWlanNotifAuxPeerDeviceInetAddressType"),
        ("AVAYA-WLAN-MOB-SW-NOTIFICATIONS-MIB", "avWlanNotifAuxPeerDeviceInetAddress"),
        ("AVAYA-WLAN-MOB-SW-NOTIFICATIONS-MIB", "avWlanNotifAuxPeerDeviceAddress"),
        ("AVAYA-WLAN-MOB-SW-NOTIFICATIONS-MIB", "avWlanNotifAuxPeerDeviceType"),
        ("AVAYA-WLAN-MOB-SW-NOTIFICATIONS-MIB", "avWlanNotifAuxConnectionFailureReason"))
)
if mibBuilder.loadTexts:
    avWlanSwitchPeerDeviceLostConnection.setStatus(
        "current"
    )

avWlanSwitchVlanServerElected = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 7, 19, 0, 1, 7)
)
avWlanSwitchVlanServerElected.setObjects(
      *(("AVAYA-WLAN-MOB-SW-NOTIFICATIONS-MIB", "avWlanNotifAuxMobilityVlanName"),
        ("AVAYA-WLAN-MOB-SW-NOTIFICATIONS-MIB", "avWlanNotifAuxVlanServerInetAddressType"),
        ("AVAYA-WLAN-MOB-SW-NOTIFICATIONS-MIB", "avWlanNotifAuxVlanServerInetAddress"),
        ("AVAYA-WLAN-MOB-SW-NOTIFICATIONS-MIB", "avWlanNotifAuxVlanServerAddress"))
)
if mibBuilder.loadTexts:
    avWlanSwitchVlanServerElected.setStatus(
        "current"
    )

avWlanSwitchLostConnectionToVlanServer = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 7, 19, 0, 1, 8)
)
avWlanSwitchLostConnectionToVlanServer.setObjects(
      *(("AVAYA-WLAN-MOB-SW-NOTIFICATIONS-MIB", "avWlanNotifAuxMobilityVlanName"),
        ("AVAYA-WLAN-MOB-SW-NOTIFICATIONS-MIB", "avWlanNotifAuxVlanServerInetAddressType"),
        ("AVAYA-WLAN-MOB-SW-NOTIFICATIONS-MIB", "avWlanNotifAuxVlanServerInetAddress"),
        ("AVAYA-WLAN-MOB-SW-NOTIFICATIONS-MIB", "avWlanNotifAuxVlanServerAddress"))
)
if mibBuilder.loadTexts:
    avWlanSwitchLostConnectionToVlanServer.setStatus(
        "current"
    )

avWlanSwitchVlanGenNumberMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 7, 19, 0, 1, 9)
)
avWlanSwitchVlanGenNumberMismatch.setObjects(
      *(("AVAYA-WLAN-MOB-SW-NOTIFICATIONS-MIB", "avWlanNotifAuxMobilityVlanName"),
        ("AVAYA-WLAN-MOB-SW-NOTIFICATIONS-MIB", "avWlanNotifAuxMobilityVlanSelfGenerationNumber"),
        ("AVAYA-WLAN-MOB-SW-NOTIFICATIONS-MIB", "avWlanNotifAuxMobilityVlanPeerGenerationNumber"))
)
if mibBuilder.loadTexts:
    avWlanSwitchVlanGenNumberMismatch.setStatus(
        "current"
    )

avWlanSwitchVlanRoleChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 7, 19, 0, 1, 10)
)
avWlanSwitchVlanRoleChanged.setObjects(
      *(("AVAYA-WLAN-MOB-SW-NOTIFICATIONS-MIB", "avWlanNotifAuxMobilityVlanName"),
        ("AVAYA-WLAN-MOB-SW-NOTIFICATIONS-MIB", "avWlanNotifAuxOldVlanRole"),
        ("AVAYA-WLAN-MOB-SW-NOTIFICATIONS-MIB", "avWlanNotifAuxNewVlanRole"),
        ("AVAYA-WLAN-MOB-SW-NOTIFICATIONS-MIB", "avWlanNotifAuxRoleChangeReason"))
)
if mibBuilder.loadTexts:
    avWlanSwitchVlanRoleChanged.setStatus(
        "current"
    )

avWlanSwitchVlanMapStateChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 7, 19, 0, 1, 11)
)
avWlanSwitchVlanMapStateChanged.setObjects(
      *(("AVAYA-WLAN-MOB-SW-NOTIFICATIONS-MIB", "avWlanNotifAuxMobilityVlanName"),
        ("AVAYA-WLAN-MOB-SW-NOTIFICATIONS-MIB", "avWlanNotifAuxOldState"),
        ("AVAYA-WLAN-MOB-SW-NOTIFICATIONS-MIB", "avWlanNotifAuxNewState"),
        ("AVAYA-WLAN-MOB-SW-NOTIFICATIONS-MIB", "avWlanNotifAuxStateChangeReason"))
)
if mibBuilder.loadTexts:
    avWlanSwitchVlanMapStateChanged.setStatus(
        "current"
    )

avWlanSwitchVlanMapRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 7, 19, 0, 1, 12)
)
avWlanSwitchVlanMapRemoved.setObjects(
      *(("AVAYA-WLAN-MOB-SW-NOTIFICATIONS-MIB", "avWlanNotifAuxMobilityVlanName"),
        ("AVAYA-WLAN-MOB-SW-NOTIFICATIONS-MIB", "avWlanNotifAuxVlanState"),
        ("AVAYA-WLAN-MOB-SW-NOTIFICATIONS-MIB", "avWlanNotifAuxRemoveReason"))
)
if mibBuilder.loadTexts:
    avWlanSwitchVlanMapRemoved.setStatus(
        "current"
    )

avWlanSwitchVlanTrackAffected = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 7, 19, 0, 1, 13)
)
avWlanSwitchVlanTrackAffected.setObjects(
    ("AVAYA-WLAN-MOB-SW-NOTIFICATIONS-MIB", "avWlanNotifAuxMobilityVlanName")
)
if mibBuilder.loadTexts:
    avWlanSwitchVlanTrackAffected.setStatus(
        "current"
    )

avWlanSwitchIgmpSnoopingEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 7, 19, 0, 1, 14)
)
avWlanSwitchIgmpSnoopingEnabled.setObjects(
    ("AVAYA-WLAN-MOB-SW-NOTIFICATIONS-MIB", "avWlanNotifAuxMobilityVlanName")
)
if mibBuilder.loadTexts:
    avWlanSwitchIgmpSnoopingEnabled.setStatus(
        "current"
    )

avWlanSwitchIgmpSnoopingDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 7, 19, 0, 1, 15)
)
avWlanSwitchIgmpSnoopingDisabled.setObjects(
    ("AVAYA-WLAN-MOB-SW-NOTIFICATIONS-MIB", "avWlanNotifAuxMobilityVlanName")
)
if mibBuilder.loadTexts:
    avWlanSwitchIgmpSnoopingDisabled.setStatus(
        "current"
    )

avWlanSwitchIgmpControlFrameReceived = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 7, 19, 0, 1, 16)
)
avWlanSwitchIgmpControlFrameReceived.setObjects(
      *(("AVAYA-WLAN-MOB-SW-NOTIFICATIONS-MIB", "avWlanNotifAuxMobilityVlanName"),
        ("AVAYA-WLAN-MOB-SW-NOTIFICATIONS-MIB", "avWlanNotifAuxControlFrameType"),
        ("AVAYA-WLAN-MOB-SW-NOTIFICATIONS-MIB", "avWlanNotifAuxPeerDeviceType"),
        ("AVAYA-WLAN-MOB-SW-NOTIFICATIONS-MIB", "avWlanNotifAuxInetAddressType"),
        ("AVAYA-WLAN-MOB-SW-NOTIFICATIONS-MIB", "avWlanNotifAuxInetAddress"))
)
if mibBuilder.loadTexts:
    avWlanSwitchIgmpControlFrameReceived.setStatus(
        "current"
    )

avWlanSwitchLimitsReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 7, 19, 0, 1, 17)
)
avWlanSwitchLimitsReached.setObjects(
    ("AVAYA-WLAN-MOB-SW-NOTIFICATIONS-MIB", "avWlanSwitchNotifAuxAuxLimitsReached")
)
if mibBuilder.loadTexts:
    avWlanSwitchLimitsReached.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AVAYA-WLAN-MOB-SW-NOTIFICATIONS-MIB",
    **{"avayaWlanMobSwitchNotificationsMib": avayaWlanMobSwitchNotificationsMib,
       "avWlanMobSwNotifications": avWlanMobSwNotifications,
       "avWlanSwitchNotifications": avWlanSwitchNotifications,
       "avWlanSwitchMCPConnectionEstablished": avWlanSwitchMCPConnectionEstablished,
       "avWlanSwitchMCPLostConnection": avWlanSwitchMCPLostConnection,
       "avWlanSwitchMVTDownload": avWlanSwitchMVTDownload,
       "avWlanSwitchMSTDownload": avWlanSwitchMSTDownload,
       "avWlanSwitchPeerDeviceConnectionEstablished": avWlanSwitchPeerDeviceConnectionEstablished,
       "avWlanSwitchPeerDeviceLostConnection": avWlanSwitchPeerDeviceLostConnection,
       "avWlanSwitchVlanServerElected": avWlanSwitchVlanServerElected,
       "avWlanSwitchLostConnectionToVlanServer": avWlanSwitchLostConnectionToVlanServer,
       "avWlanSwitchVlanGenNumberMismatch": avWlanSwitchVlanGenNumberMismatch,
       "avWlanSwitchVlanRoleChanged": avWlanSwitchVlanRoleChanged,
       "avWlanSwitchVlanMapStateChanged": avWlanSwitchVlanMapStateChanged,
       "avWlanSwitchVlanMapRemoved": avWlanSwitchVlanMapRemoved,
       "avWlanSwitchVlanTrackAffected": avWlanSwitchVlanTrackAffected,
       "avWlanSwitchIgmpSnoopingEnabled": avWlanSwitchIgmpSnoopingEnabled,
       "avWlanSwitchIgmpSnoopingDisabled": avWlanSwitchIgmpSnoopingDisabled,
       "avWlanSwitchIgmpControlFrameReceived": avWlanSwitchIgmpControlFrameReceived,
       "avWlanSwitchLimitsReached": avWlanSwitchLimitsReached,
       "avWlanMobSwNotificationObjects": avWlanMobSwNotificationObjects,
       "avWlanMobSwNotificationAuxObjects": avWlanMobSwNotificationAuxObjects,
       "avWlanNotifAuxMobilityControllerInetAddressType": avWlanNotifAuxMobilityControllerInetAddressType,
       "avWlanNotifAuxMobilityControllerInetAddress": avWlanNotifAuxMobilityControllerInetAddress,
       "avWlanNotifAuxNumberOfVlanEntries": avWlanNotifAuxNumberOfVlanEntries,
       "avWlanNotifAuxMSTDownloadEntries": avWlanNotifAuxMSTDownloadEntries,
       "avWlanNotifAuxPeerDeviceInetAddressType": avWlanNotifAuxPeerDeviceInetAddressType,
       "avWlanNotifAuxPeerDeviceInetAddress": avWlanNotifAuxPeerDeviceInetAddress,
       "avWlanNotifAuxPeerDeviceAddress": avWlanNotifAuxPeerDeviceAddress,
       "avWlanNotifAuxPeerDeviceType": avWlanNotifAuxPeerDeviceType,
       "avWlanNotifAuxConnectionFailureReason": avWlanNotifAuxConnectionFailureReason,
       "avWlanNotifAuxMobilityVlanName": avWlanNotifAuxMobilityVlanName,
       "avWlanNotifAuxVlanServerInetAddressType": avWlanNotifAuxVlanServerInetAddressType,
       "avWlanNotifAuxVlanServerInetAddress": avWlanNotifAuxVlanServerInetAddress,
       "avWlanNotifAuxVlanServerAddress": avWlanNotifAuxVlanServerAddress,
       "avWlanNotifAuxMobilityVlanSelfGenerationNumber": avWlanNotifAuxMobilityVlanSelfGenerationNumber,
       "avWlanNotifAuxMobilityVlanPeerGenerationNumber": avWlanNotifAuxMobilityVlanPeerGenerationNumber,
       "avWlanNotifAuxOldVlanRole": avWlanNotifAuxOldVlanRole,
       "avWlanNotifAuxNewVlanRole": avWlanNotifAuxNewVlanRole,
       "avWlanNotifAuxRoleChangeReason": avWlanNotifAuxRoleChangeReason,
       "avWlanNotifAuxOldState": avWlanNotifAuxOldState,
       "avWlanNotifAuxNewState": avWlanNotifAuxNewState,
       "avWlanNotifAuxStateChangeReason": avWlanNotifAuxStateChangeReason,
       "avWlanNotifAuxVlanState": avWlanNotifAuxVlanState,
       "avWlanNotifAuxRemoveReason": avWlanNotifAuxRemoveReason,
       "avWlanNotifAuxControlFrameType": avWlanNotifAuxControlFrameType,
       "avWlanNotifAuxInetAddressType": avWlanNotifAuxInetAddressType,
       "avWlanNotifAuxInetAddress": avWlanNotifAuxInetAddress,
       "avWlanSwitchNotifAuxAuxLimitsReached": avWlanSwitchNotifAuxAuxLimitsReached}
)
