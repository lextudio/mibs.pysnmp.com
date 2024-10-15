# SNMP MIB module (WWP-LEOS-TABLE-CHG-NOTIF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WWP-LEOS-TABLE-CHG-NOTIF-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:15:12 2024
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

(AddressFamilyNumbers,) = mibBuilder.importSymbols(
    "IANA-ADDRESS-FAMILY-NUMBERS-MIB",
    "AddressFamilyNumbers")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(wwpModules,
 wwpModulesLeos) = mibBuilder.importSymbols(
    "WWP-SMI",
    "wwpModules",
    "wwpModulesLeos")


# MODULE-IDENTITY

wwpLeosTableChgNotifMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 9)
)
wwpLeosTableChgNotifMIB.setRevisions(
        ("2002-03-12 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WwpLeosTableChgNotifMIBObjects_ObjectIdentity = ObjectIdentity
wwpLeosTableChgNotifMIBObjects = _WwpLeosTableChgNotifMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 9, 1)
)


class _WwpLeosTableTrapNotifTimer_Type(Integer32):
    """Custom type wwpLeosTableTrapNotifTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 3600),
    )


_WwpLeosTableTrapNotifTimer_Type.__name__ = "Integer32"
_WwpLeosTableTrapNotifTimer_Object = MibScalar
wwpLeosTableTrapNotifTimer = _WwpLeosTableTrapNotifTimer_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 9, 1, 1),
    _WwpLeosTableTrapNotifTimer_Type()
)
wwpLeosTableTrapNotifTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosTableTrapNotifTimer.setStatus("current")


class _WwpLeosListenerRefreshTimer_Type(Integer32):
    """Custom type wwpLeosListenerRefreshTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 1000),
    )


_WwpLeosListenerRefreshTimer_Type.__name__ = "Integer32"
_WwpLeosListenerRefreshTimer_Object = MibScalar
wwpLeosListenerRefreshTimer = _WwpLeosListenerRefreshTimer_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 9, 1, 2),
    _WwpLeosListenerRefreshTimer_Type()
)
wwpLeosListenerRefreshTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosListenerRefreshTimer.setStatus("current")
_WwpLeosTableChgNotifTable_Object = MibTable
wwpLeosTableChgNotifTable = _WwpLeosTableChgNotifTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 9, 1, 4)
)
if mibBuilder.loadTexts:
    wwpLeosTableChgNotifTable.setStatus("current")
_WwpLeosTableChgNotifEntry_Object = MibTableRow
wwpLeosTableChgNotifEntry = _WwpLeosTableChgNotifEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 9, 1, 4, 1)
)
wwpLeosTableChgNotifEntry.setIndexNames(
    (0, "WWP-LEOS-TABLE-CHG-NOTIF-MIB", "wwpLeosTableChgNotifIndex"),
)
if mibBuilder.loadTexts:
    wwpLeosTableChgNotifEntry.setStatus("current")


class _WwpLeosTableChgNotifIndex_Type(Integer32):
    """Custom type wwpLeosTableChgNotifIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_WwpLeosTableChgNotifIndex_Type.__name__ = "Integer32"
_WwpLeosTableChgNotifIndex_Object = MibTableColumn
wwpLeosTableChgNotifIndex = _WwpLeosTableChgNotifIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 9, 1, 4, 1, 1),
    _WwpLeosTableChgNotifIndex_Type()
)
wwpLeosTableChgNotifIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTableChgNotifIndex.setStatus("current")
_WwpLeosTableChgNotifOid_Type = ObjectIdentifier
_WwpLeosTableChgNotifOid_Object = MibTableColumn
wwpLeosTableChgNotifOid = _WwpLeosTableChgNotifOid_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 9, 1, 4, 1, 2),
    _WwpLeosTableChgNotifOid_Type()
)
wwpLeosTableChgNotifOid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTableChgNotifOid.setStatus("current")
_WwpLeosTableChgNotifNumChanges_Type = Counter32
_WwpLeosTableChgNotifNumChanges_Object = MibTableColumn
wwpLeosTableChgNotifNumChanges = _WwpLeosTableChgNotifNumChanges_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 9, 1, 4, 1, 3),
    _WwpLeosTableChgNotifNumChanges_Type()
)
wwpLeosTableChgNotifNumChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTableChgNotifNumChanges.setStatus("current")
_WwpLeosListenerTable_Object = MibTable
wwpLeosListenerTable = _WwpLeosListenerTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 9, 1, 5)
)
if mibBuilder.loadTexts:
    wwpLeosListenerTable.setStatus("current")
_WwpLeosListenerEntry_Object = MibTableRow
wwpLeosListenerEntry = _WwpLeosListenerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 9, 1, 5, 1)
)
wwpLeosListenerEntry.setIndexNames(
    (0, "WWP-LEOS-TABLE-CHG-NOTIF-MIB", "wwpLeosListenerIndex"),
)
if mibBuilder.loadTexts:
    wwpLeosListenerEntry.setStatus("current")


class _WwpLeosListenerIndex_Type(Integer32):
    """Custom type wwpLeosListenerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_WwpLeosListenerIndex_Type.__name__ = "Integer32"
_WwpLeosListenerIndex_Object = MibTableColumn
wwpLeosListenerIndex = _WwpLeosListenerIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 9, 1, 5, 1, 1),
    _WwpLeosListenerIndex_Type()
)
wwpLeosListenerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosListenerIndex.setStatus("current")
_WwpLeosListenerAddr_Type = DisplayString
_WwpLeosListenerAddr_Object = MibTableColumn
wwpLeosListenerAddr = _WwpLeosListenerAddr_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 9, 1, 5, 1, 2),
    _WwpLeosListenerAddr_Type()
)
wwpLeosListenerAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosListenerAddr.setStatus("current")
_WwpLeosListenerResolvedIp_Type = IpAddress
_WwpLeosListenerResolvedIp_Object = MibTableColumn
wwpLeosListenerResolvedIp = _WwpLeosListenerResolvedIp_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 9, 1, 5, 1, 3),
    _WwpLeosListenerResolvedIp_Type()
)
wwpLeosListenerResolvedIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosListenerResolvedIp.setStatus("current")
_WwpLeosListenerStatus_Type = RowStatus
_WwpLeosListenerStatus_Object = MibTableColumn
wwpLeosListenerStatus = _WwpLeosListenerStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 9, 1, 5, 1, 4),
    _WwpLeosListenerStatus_Type()
)
wwpLeosListenerStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosListenerStatus.setStatus("current")
_WwpLeosTableChgNotif_ObjectIdentity = ObjectIdentity
wwpLeosTableChgNotif = _WwpLeosTableChgNotif_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 9, 1, 7)
)


class _WwpLeosTableChgNotifIndexStr_Type(DisplayString):
    """Custom type wwpLeosTableChgNotifIndexStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_WwpLeosTableChgNotifIndexStr_Type.__name__ = "DisplayString"
_WwpLeosTableChgNotifIndexStr_Object = MibScalar
wwpLeosTableChgNotifIndexStr = _WwpLeosTableChgNotifIndexStr_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 9, 1, 7, 1),
    _WwpLeosTableChgNotifIndexStr_Type()
)
wwpLeosTableChgNotifIndexStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTableChgNotifIndexStr.setStatus("current")


class _WwpLeosListenerRefreshCount_Type(Integer32):
    """Custom type wwpLeosListenerRefreshCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 1000),
    )


_WwpLeosListenerRefreshCount_Type.__name__ = "Integer32"
_WwpLeosListenerRefreshCount_Object = MibScalar
wwpLeosListenerRefreshCount = _WwpLeosListenerRefreshCount_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 9, 1, 7, 2),
    _WwpLeosListenerRefreshCount_Type()
)
wwpLeosListenerRefreshCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosListenerRefreshCount.setStatus("current")
_WwpLeosTableChgNotifMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
wwpLeosTableChgNotifMIBNotificationPrefix = _WwpLeosTableChgNotifMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 9, 2)
)
_WwpLeosTableChgNotifMIBNotifications_ObjectIdentity = ObjectIdentity
wwpLeosTableChgNotifMIBNotifications = _WwpLeosTableChgNotifMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 9, 2, 0)
)
_WwpLeosTableChgNotifMIBConformance_ObjectIdentity = ObjectIdentity
wwpLeosTableChgNotifMIBConformance = _WwpLeosTableChgNotifMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 9, 3)
)
_WwpLeosTableChgNotifMIBCompliances_ObjectIdentity = ObjectIdentity
wwpLeosTableChgNotifMIBCompliances = _WwpLeosTableChgNotifMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 9, 3, 1)
)
_WwpLeosTableChgNotifMIBGroups_ObjectIdentity = ObjectIdentity
wwpLeosTableChgNotifMIBGroups = _WwpLeosTableChgNotifMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 9, 3, 2)
)

# Managed Objects groups


# Notification objects

wwpLeosTableChgTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 9, 2, 0, 1)
)
wwpLeosTableChgTrap.setObjects(
      *(("WWP-LEOS-TABLE-CHG-NOTIF-MIB", "wwpLeosTableChgNotifOid"),
        ("WWP-LEOS-TABLE-CHG-NOTIF-MIB", "wwpLeosTableChgNotifNumChanges"),
        ("WWP-LEOS-TABLE-CHG-NOTIF-MIB", "wwpLeosTableChgNotifIndexStr"))
)
if mibBuilder.loadTexts:
    wwpLeosTableChgTrap.setStatus(
        "current"
    )

wwpLeosTableRefreshTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 9, 2, 0, 2)
)
wwpLeosTableRefreshTrap.setObjects(
    ("WWP-LEOS-TABLE-CHG-NOTIF-MIB", "wwpLeosListenerRefreshCount")
)
if mibBuilder.loadTexts:
    wwpLeosTableRefreshTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WWP-LEOS-TABLE-CHG-NOTIF-MIB",
    **{"wwpLeosTableChgNotifMIB": wwpLeosTableChgNotifMIB,
       "wwpLeosTableChgNotifMIBObjects": wwpLeosTableChgNotifMIBObjects,
       "wwpLeosTableTrapNotifTimer": wwpLeosTableTrapNotifTimer,
       "wwpLeosListenerRefreshTimer": wwpLeosListenerRefreshTimer,
       "wwpLeosTableChgNotifTable": wwpLeosTableChgNotifTable,
       "wwpLeosTableChgNotifEntry": wwpLeosTableChgNotifEntry,
       "wwpLeosTableChgNotifIndex": wwpLeosTableChgNotifIndex,
       "wwpLeosTableChgNotifOid": wwpLeosTableChgNotifOid,
       "wwpLeosTableChgNotifNumChanges": wwpLeosTableChgNotifNumChanges,
       "wwpLeosListenerTable": wwpLeosListenerTable,
       "wwpLeosListenerEntry": wwpLeosListenerEntry,
       "wwpLeosListenerIndex": wwpLeosListenerIndex,
       "wwpLeosListenerAddr": wwpLeosListenerAddr,
       "wwpLeosListenerResolvedIp": wwpLeosListenerResolvedIp,
       "wwpLeosListenerStatus": wwpLeosListenerStatus,
       "wwpLeosTableChgNotif": wwpLeosTableChgNotif,
       "wwpLeosTableChgNotifIndexStr": wwpLeosTableChgNotifIndexStr,
       "wwpLeosListenerRefreshCount": wwpLeosListenerRefreshCount,
       "wwpLeosTableChgNotifMIBNotificationPrefix": wwpLeosTableChgNotifMIBNotificationPrefix,
       "wwpLeosTableChgNotifMIBNotifications": wwpLeosTableChgNotifMIBNotifications,
       "wwpLeosTableChgTrap": wwpLeosTableChgTrap,
       "wwpLeosTableRefreshTrap": wwpLeosTableRefreshTrap,
       "wwpLeosTableChgNotifMIBConformance": wwpLeosTableChgNotifMIBConformance,
       "wwpLeosTableChgNotifMIBCompliances": wwpLeosTableChgNotifMIBCompliances,
       "wwpLeosTableChgNotifMIBGroups": wwpLeosTableChgNotifMIBGroups}
)
