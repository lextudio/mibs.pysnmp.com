# SNMP MIB module (ALVARION-USER-SESSION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALVARION-USER-SESSION-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:38:47 2024
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

(alvarionMgmtV2,) = mibBuilder.importSymbols(
    "ALVARION-SMI",
    "alvarionMgmtV2")

(AlvarionSSIDOrNone,) = mibBuilder.importSymbols(
    "ALVARION-TC",
    "AlvarionSSIDOrNone")

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

alvarionUserSessionMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 36)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AlvarionUserSessionMIBObjects_ObjectIdentity = ObjectIdentity
alvarionUserSessionMIBObjects = _AlvarionUserSessionMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 36, 1)
)
_CoUserSessionInfoGroup_ObjectIdentity = ObjectIdentity
coUserSessionInfoGroup = _CoUserSessionInfoGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 36, 1, 1)
)
_CoUserSessACUserMaxCount_Type = Unsigned32
_CoUserSessACUserMaxCount_Object = MibScalar
coUserSessACUserMaxCount = _CoUserSessACUserMaxCount_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 36, 1, 1, 1),
    _CoUserSessACUserMaxCount_Type()
)
coUserSessACUserMaxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coUserSessACUserMaxCount.setStatus("current")
_CoUserSessNonACUserMaxCount_Type = Unsigned32
_CoUserSessNonACUserMaxCount_Object = MibScalar
coUserSessNonACUserMaxCount = _CoUserSessNonACUserMaxCount_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 36, 1, 1, 2),
    _CoUserSessNonACUserMaxCount_Type()
)
coUserSessNonACUserMaxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coUserSessNonACUserMaxCount.setStatus("current")
_CoUserSessACUserCount_Type = Gauge32
_CoUserSessACUserCount_Object = MibScalar
coUserSessACUserCount = _CoUserSessACUserCount_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 36, 1, 1, 3),
    _CoUserSessACUserCount_Type()
)
coUserSessACUserCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coUserSessACUserCount.setStatus("current")
_CoUserSessNonACUserCount_Type = Gauge32
_CoUserSessNonACUserCount_Object = MibScalar
coUserSessNonACUserCount = _CoUserSessNonACUserCount_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 36, 1, 1, 4),
    _CoUserSessNonACUserCount_Type()
)
coUserSessNonACUserCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coUserSessNonACUserCount.setStatus("current")
_CoUserSessionStGroup_ObjectIdentity = ObjectIdentity
coUserSessionStGroup = _CoUserSessionStGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 36, 1, 2)
)
_CoUserSessionTable_Object = MibTable
coUserSessionTable = _CoUserSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 36, 1, 2, 1)
)
if mibBuilder.loadTexts:
    coUserSessionTable.setStatus("current")
_CoUserSessionEntry_Object = MibTableRow
coUserSessionEntry = _CoUserSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 36, 1, 2, 1, 1)
)
coUserSessionEntry.setIndexNames(
    (0, "ALVARION-USER-SESSION-MIB", "coUserSessIndex"),
)
if mibBuilder.loadTexts:
    coUserSessionEntry.setStatus("current")


class _CoUserSessIndex_Type(Integer32):
    """Custom type coUserSessIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CoUserSessIndex_Type.__name__ = "Integer32"
_CoUserSessIndex_Object = MibTableColumn
coUserSessIndex = _CoUserSessIndex_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 36, 1, 2, 1, 1, 1),
    _CoUserSessIndex_Type()
)
coUserSessIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    coUserSessIndex.setStatus("current")


class _CoUserSessUserName_Type(OctetString):
    """Custom type coUserSessUserName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 252),
    )


_CoUserSessUserName_Type.__name__ = "OctetString"
_CoUserSessUserName_Object = MibTableColumn
coUserSessUserName = _CoUserSessUserName_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 36, 1, 2, 1, 1, 2),
    _CoUserSessUserName_Type()
)
coUserSessUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coUserSessUserName.setStatus("current")
_CoUserSessClientIpAddress_Type = IpAddress
_CoUserSessClientIpAddress_Object = MibTableColumn
coUserSessClientIpAddress = _CoUserSessClientIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 36, 1, 2, 1, 1, 3),
    _CoUserSessClientIpAddress_Type()
)
coUserSessClientIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coUserSessClientIpAddress.setStatus("current")
_CoUserSessSessionDuration_Type = Counter32
_CoUserSessSessionDuration_Object = MibTableColumn
coUserSessSessionDuration = _CoUserSessSessionDuration_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 36, 1, 2, 1, 1, 4),
    _CoUserSessSessionDuration_Type()
)
coUserSessSessionDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coUserSessSessionDuration.setStatus("current")
if mibBuilder.loadTexts:
    coUserSessSessionDuration.setUnits("seconds")
_CoUserSessIdleTime_Type = Counter32
_CoUserSessIdleTime_Object = MibTableColumn
coUserSessIdleTime = _CoUserSessIdleTime_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 36, 1, 2, 1, 1, 5),
    _CoUserSessIdleTime_Type()
)
coUserSessIdleTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coUserSessIdleTime.setStatus("current")
if mibBuilder.loadTexts:
    coUserSessIdleTime.setUnits("seconds")


class _CoUserSessMAPGroupName_Type(OctetString):
    """Custom type coUserSessMAPGroupName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_CoUserSessMAPGroupName_Type.__name__ = "OctetString"
_CoUserSessMAPGroupName_Object = MibTableColumn
coUserSessMAPGroupName = _CoUserSessMAPGroupName_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 36, 1, 2, 1, 1, 6),
    _CoUserSessMAPGroupName_Type()
)
coUserSessMAPGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coUserSessMAPGroupName.setStatus("current")


class _CoUserSessVSCName_Type(OctetString):
    """Custom type coUserSessVSCName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CoUserSessVSCName_Type.__name__ = "OctetString"
_CoUserSessVSCName_Object = MibTableColumn
coUserSessVSCName = _CoUserSessVSCName_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 36, 1, 2, 1, 1, 7),
    _CoUserSessVSCName_Type()
)
coUserSessVSCName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coUserSessVSCName.setStatus("current")
_CoUserSessSSID_Type = AlvarionSSIDOrNone
_CoUserSessSSID_Object = MibTableColumn
coUserSessSSID = _CoUserSessSSID_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 36, 1, 2, 1, 1, 8),
    _CoUserSessSSID_Type()
)
coUserSessSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coUserSessSSID.setStatus("current")


class _CoUserSessVLAN_Type(Integer32):
    """Custom type coUserSessVLAN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_CoUserSessVLAN_Type.__name__ = "Integer32"
_CoUserSessVLAN_Object = MibTableColumn
coUserSessVLAN = _CoUserSessVLAN_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 36, 1, 2, 1, 1, 9),
    _CoUserSessVLAN_Type()
)
coUserSessVLAN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coUserSessVLAN.setStatus("current")


class _CoUserSessPHYType_Type(Integer32):
    """Custom type coUserSessPHYType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ieee802dot11a", 1),
          ("ieee802dot11b", 2),
          ("ieee802dot11g", 3),
          ("unknown", 0))
    )


_CoUserSessPHYType_Type.__name__ = "Integer32"
_CoUserSessPHYType_Object = MibTableColumn
coUserSessPHYType = _CoUserSessPHYType_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 36, 1, 2, 1, 1, 10),
    _CoUserSessPHYType_Type()
)
coUserSessPHYType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coUserSessPHYType.setStatus("current")


class _CoUserSessAuthType_Type(Integer32):
    """Custom type coUserSessAuthType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ac", 1),
          ("nonAc", 2))
    )


_CoUserSessAuthType_Type.__name__ = "Integer32"
_CoUserSessAuthType_Object = MibTableColumn
coUserSessAuthType = _CoUserSessAuthType_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 36, 1, 2, 1, 1, 11),
    _CoUserSessAuthType_Type()
)
coUserSessAuthType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coUserSessAuthType.setStatus("current")


class _CoUserSessCalledStationID_Type(OctetString):
    """Custom type coUserSessCalledStationID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 252),
    )


_CoUserSessCalledStationID_Type.__name__ = "OctetString"
_CoUserSessCalledStationID_Object = MibTableColumn
coUserSessCalledStationID = _CoUserSessCalledStationID_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 36, 1, 2, 1, 1, 12),
    _CoUserSessCalledStationID_Type()
)
coUserSessCalledStationID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coUserSessCalledStationID.setStatus("current")


class _CoUserSessCallingStationID_Type(OctetString):
    """Custom type coUserSessCallingStationID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 252),
    )


_CoUserSessCallingStationID_Type.__name__ = "OctetString"
_CoUserSessCallingStationID_Object = MibTableColumn
coUserSessCallingStationID = _CoUserSessCallingStationID_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 36, 1, 2, 1, 1, 13),
    _CoUserSessCallingStationID_Type()
)
coUserSessCallingStationID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coUserSessCallingStationID.setStatus("current")


class _CoUserSessRADIUSServerProfileName_Type(OctetString):
    """Custom type coUserSessRADIUSServerProfileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_CoUserSessRADIUSServerProfileName_Type.__name__ = "OctetString"
_CoUserSessRADIUSServerProfileName_Object = MibTableColumn
coUserSessRADIUSServerProfileName = _CoUserSessRADIUSServerProfileName_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 36, 1, 2, 1, 1, 14),
    _CoUserSessRADIUSServerProfileName_Type()
)
coUserSessRADIUSServerProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coUserSessRADIUSServerProfileName.setStatus("current")
_CoUserSessRADIUSServerIpAddress_Type = IpAddress
_CoUserSessRADIUSServerIpAddress_Object = MibTableColumn
coUserSessRADIUSServerIpAddress = _CoUserSessRADIUSServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 36, 1, 2, 1, 1, 15),
    _CoUserSessRADIUSServerIpAddress_Type()
)
coUserSessRADIUSServerIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coUserSessRADIUSServerIpAddress.setStatus("current")
_CoUserSessBytesSent_Type = Counter64
_CoUserSessBytesSent_Object = MibTableColumn
coUserSessBytesSent = _CoUserSessBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 36, 1, 2, 1, 1, 16),
    _CoUserSessBytesSent_Type()
)
coUserSessBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coUserSessBytesSent.setStatus("current")
_CoUserSessBytesReceived_Type = Counter64
_CoUserSessBytesReceived_Object = MibTableColumn
coUserSessBytesReceived = _CoUserSessBytesReceived_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 36, 1, 2, 1, 1, 17),
    _CoUserSessBytesReceived_Type()
)
coUserSessBytesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coUserSessBytesReceived.setStatus("current")
_CoUserSessPacketsSent_Type = Counter32
_CoUserSessPacketsSent_Object = MibTableColumn
coUserSessPacketsSent = _CoUserSessPacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 36, 1, 2, 1, 1, 18),
    _CoUserSessPacketsSent_Type()
)
coUserSessPacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coUserSessPacketsSent.setStatus("current")
_CoUserSessPacketsReceived_Type = Counter32
_CoUserSessPacketsReceived_Object = MibTableColumn
coUserSessPacketsReceived = _CoUserSessPacketsReceived_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 36, 1, 2, 1, 1, 19),
    _CoUserSessPacketsReceived_Type()
)
coUserSessPacketsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coUserSessPacketsReceived.setStatus("current")
_UserSessionMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
userSessionMIBNotificationPrefix = _UserSessionMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 36, 2)
)
_UserSessionMIBNotifications_ObjectIdentity = ObjectIdentity
userSessionMIBNotifications = _UserSessionMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 36, 2, 0)
)
_AlvarionUserSessionMIBConformance_ObjectIdentity = ObjectIdentity
alvarionUserSessionMIBConformance = _AlvarionUserSessionMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 36, 3)
)
_AlvarionUserSessionMIBCompliances_ObjectIdentity = ObjectIdentity
alvarionUserSessionMIBCompliances = _AlvarionUserSessionMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 36, 3, 1)
)
_AlvarionUserSessionMIBGroups_ObjectIdentity = ObjectIdentity
alvarionUserSessionMIBGroups = _AlvarionUserSessionMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 36, 3, 2)
)

# Managed Objects groups

alvarionUserSessionInfoMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 36, 3, 2, 1)
)
alvarionUserSessionInfoMIBGroup.setObjects(
      *(("ALVARION-USER-SESSION-MIB", "coUserSessACUserMaxCount"),
        ("ALVARION-USER-SESSION-MIB", "coUserSessNonACUserMaxCount"),
        ("ALVARION-USER-SESSION-MIB", "coUserSessACUserCount"),
        ("ALVARION-USER-SESSION-MIB", "coUserSessNonACUserCount"))
)
if mibBuilder.loadTexts:
    alvarionUserSessionInfoMIBGroup.setStatus("current")

alvarionUserSessionStMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 36, 3, 2, 2)
)
alvarionUserSessionStMIBGroup.setObjects(
      *(("ALVARION-USER-SESSION-MIB", "coUserSessUserName"),
        ("ALVARION-USER-SESSION-MIB", "coUserSessClientIpAddress"),
        ("ALVARION-USER-SESSION-MIB", "coUserSessSessionDuration"),
        ("ALVARION-USER-SESSION-MIB", "coUserSessIdleTime"),
        ("ALVARION-USER-SESSION-MIB", "coUserSessMAPGroupName"),
        ("ALVARION-USER-SESSION-MIB", "coUserSessVSCName"),
        ("ALVARION-USER-SESSION-MIB", "coUserSessSSID"),
        ("ALVARION-USER-SESSION-MIB", "coUserSessVLAN"),
        ("ALVARION-USER-SESSION-MIB", "coUserSessPHYType"),
        ("ALVARION-USER-SESSION-MIB", "coUserSessAuthType"),
        ("ALVARION-USER-SESSION-MIB", "coUserSessCalledStationID"),
        ("ALVARION-USER-SESSION-MIB", "coUserSessCallingStationID"),
        ("ALVARION-USER-SESSION-MIB", "coUserSessRADIUSServerProfileName"),
        ("ALVARION-USER-SESSION-MIB", "coUserSessRADIUSServerIpAddress"),
        ("ALVARION-USER-SESSION-MIB", "coUserSessBytesSent"),
        ("ALVARION-USER-SESSION-MIB", "coUserSessBytesReceived"),
        ("ALVARION-USER-SESSION-MIB", "coUserSessPacketsSent"),
        ("ALVARION-USER-SESSION-MIB", "coUserSessPacketsReceived"))
)
if mibBuilder.loadTexts:
    alvarionUserSessionStMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

alvarionUserSessionMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 36, 3, 1, 1)
)
if mibBuilder.loadTexts:
    alvarionUserSessionMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALVARION-USER-SESSION-MIB",
    **{"alvarionUserSessionMIB": alvarionUserSessionMIB,
       "alvarionUserSessionMIBObjects": alvarionUserSessionMIBObjects,
       "coUserSessionInfoGroup": coUserSessionInfoGroup,
       "coUserSessACUserMaxCount": coUserSessACUserMaxCount,
       "coUserSessNonACUserMaxCount": coUserSessNonACUserMaxCount,
       "coUserSessACUserCount": coUserSessACUserCount,
       "coUserSessNonACUserCount": coUserSessNonACUserCount,
       "coUserSessionStGroup": coUserSessionStGroup,
       "coUserSessionTable": coUserSessionTable,
       "coUserSessionEntry": coUserSessionEntry,
       "coUserSessIndex": coUserSessIndex,
       "coUserSessUserName": coUserSessUserName,
       "coUserSessClientIpAddress": coUserSessClientIpAddress,
       "coUserSessSessionDuration": coUserSessSessionDuration,
       "coUserSessIdleTime": coUserSessIdleTime,
       "coUserSessMAPGroupName": coUserSessMAPGroupName,
       "coUserSessVSCName": coUserSessVSCName,
       "coUserSessSSID": coUserSessSSID,
       "coUserSessVLAN": coUserSessVLAN,
       "coUserSessPHYType": coUserSessPHYType,
       "coUserSessAuthType": coUserSessAuthType,
       "coUserSessCalledStationID": coUserSessCalledStationID,
       "coUserSessCallingStationID": coUserSessCallingStationID,
       "coUserSessRADIUSServerProfileName": coUserSessRADIUSServerProfileName,
       "coUserSessRADIUSServerIpAddress": coUserSessRADIUSServerIpAddress,
       "coUserSessBytesSent": coUserSessBytesSent,
       "coUserSessBytesReceived": coUserSessBytesReceived,
       "coUserSessPacketsSent": coUserSessPacketsSent,
       "coUserSessPacketsReceived": coUserSessPacketsReceived,
       "userSessionMIBNotificationPrefix": userSessionMIBNotificationPrefix,
       "userSessionMIBNotifications": userSessionMIBNotifications,
       "alvarionUserSessionMIBConformance": alvarionUserSessionMIBConformance,
       "alvarionUserSessionMIBCompliances": alvarionUserSessionMIBCompliances,
       "alvarionUserSessionMIBCompliance": alvarionUserSessionMIBCompliance,
       "alvarionUserSessionMIBGroups": alvarionUserSessionMIBGroups,
       "alvarionUserSessionInfoMIBGroup": alvarionUserSessionInfoMIBGroup,
       "alvarionUserSessionStMIBGroup": alvarionUserSessionStMIBGroup}
)
