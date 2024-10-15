# SNMP MIB module (CISCO-SERVICE-CONTROL-LINK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-SERVICE-CONTROL-LINK-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:08:07 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(EntPhysicalIndexOrZero,) = mibBuilder.importSymbols(
    "CISCO-TC",
    "EntPhysicalIndexOrZero")

(PhysicalIndex,
 entPhysicalIndex) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "PhysicalIndex",
    "entPhysicalIndex")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoServiceControlLinkMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 631)
)
ciscoServiceControlLinkMIB.setRevisions(
        ("2007-06-26 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CsceLinkModeType(Integer32, TextualConvention):
    status = "current"
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
        *(("bypass", 2),
          ("cutoff", 4),
          ("forwarding", 3),
          ("other", 1),
          ("sniffing", 5))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoSCLinkMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoSCLinkMIBNotifs = _CiscoSCLinkMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 631, 0)
)
_CiscoSCLinkMIBObjects_ObjectIdentity = ObjectIdentity
ciscoSCLinkMIBObjects = _CiscoSCLinkMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 631, 1)
)
_CscLinkNotifsEnabled_Type = TruthValue
_CscLinkNotifsEnabled_Object = MibScalar
cscLinkNotifsEnabled = _CscLinkNotifsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 631, 1, 1),
    _CscLinkNotifsEnabled_Type()
)
cscLinkNotifsEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cscLinkNotifsEnabled.setStatus("current")
_CscLinkStatusTable_Object = MibTable
cscLinkStatusTable = _CscLinkStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 631, 1, 2)
)
if mibBuilder.loadTexts:
    cscLinkStatusTable.setStatus("current")
_CscLinkStatusEntry_Object = MibTableRow
cscLinkStatusEntry = _CscLinkStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 631, 1, 2, 1)
)
cscLinkStatusEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    cscLinkStatusEntry.setStatus("current")
_CscLinkAdminModeOnActive_Type = CsceLinkModeType
_CscLinkAdminModeOnActive_Object = MibTableColumn
cscLinkAdminModeOnActive = _CscLinkAdminModeOnActive_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 631, 1, 2, 1, 1),
    _CscLinkAdminModeOnActive_Type()
)
cscLinkAdminModeOnActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cscLinkAdminModeOnActive.setStatus("current")
_CscLinkAdminModeOnFailure_Type = CsceLinkModeType
_CscLinkAdminModeOnFailure_Object = MibTableColumn
cscLinkAdminModeOnFailure = _CscLinkAdminModeOnFailure_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 631, 1, 2, 1, 2),
    _CscLinkAdminModeOnFailure_Type()
)
cscLinkAdminModeOnFailure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cscLinkAdminModeOnFailure.setStatus("current")
_CscLinkOperMode_Type = CsceLinkModeType
_CscLinkOperMode_Object = MibTableColumn
cscLinkOperMode = _CscLinkOperMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 631, 1, 2, 1, 3),
    _CscLinkOperMode_Type()
)
cscLinkOperMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cscLinkOperMode.setStatus("current")


class _CscLinkAdminReflectionEnable_Type(Integer32):
    """Custom type cscLinkAdminReflectionEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("reflectionDisabled", 3),
          ("reflectionEnabled", 1),
          ("reflectionOnAllPortsEnabled", 2))
    )


_CscLinkAdminReflectionEnable_Type.__name__ = "Integer32"
_CscLinkAdminReflectionEnable_Object = MibTableColumn
cscLinkAdminReflectionEnable = _CscLinkAdminReflectionEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 631, 1, 2, 1, 4),
    _CscLinkAdminReflectionEnable_Type()
)
cscLinkAdminReflectionEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cscLinkAdminReflectionEnable.setStatus("current")
_CscLinkSubscriberSidePortIndex_Type = EntPhysicalIndexOrZero
_CscLinkSubscriberSidePortIndex_Object = MibTableColumn
cscLinkSubscriberSidePortIndex = _CscLinkSubscriberSidePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 631, 1, 2, 1, 5),
    _CscLinkSubscriberSidePortIndex_Type()
)
cscLinkSubscriberSidePortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cscLinkSubscriberSidePortIndex.setStatus("current")
_CscLinkNetworkSidePortIndex_Type = EntPhysicalIndexOrZero
_CscLinkNetworkSidePortIndex_Object = MibTableColumn
cscLinkNetworkSidePortIndex = _CscLinkNetworkSidePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 631, 1, 2, 1, 6),
    _CscLinkNetworkSidePortIndex_Type()
)
cscLinkNetworkSidePortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cscLinkNetworkSidePortIndex.setStatus("current")


class _CscLinkAdminReflectionState_Type(Integer32):
    """Custom type cscLinkAdminReflectionState based on Integer32"""
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
        *(("noLinkReflection", 1),
          ("reflectingFailureToBoth", 4),
          ("reflectingFailureToNetwork", 2),
          ("reflectingFailureToSubscriber", 3))
    )


_CscLinkAdminReflectionState_Type.__name__ = "Integer32"
_CscLinkAdminReflectionState_Object = MibTableColumn
cscLinkAdminReflectionState = _CscLinkAdminReflectionState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 631, 1, 2, 1, 7),
    _CscLinkAdminReflectionState_Type()
)
cscLinkAdminReflectionState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cscLinkAdminReflectionState.setStatus("current")
_CiscoSCLinkMIBConform_ObjectIdentity = ObjectIdentity
ciscoSCLinkMIBConform = _CiscoSCLinkMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 631, 2)
)
_CiscoSCLinkMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoSCLinkMIBCompliances = _CiscoSCLinkMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 631, 2, 1)
)
_CiscoSCLinkMIBObjectGroups_ObjectIdentity = ObjectIdentity
ciscoSCLinkMIBObjectGroups = _CiscoSCLinkMIBObjectGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 631, 2, 2)
)

# Managed Objects groups

cSCLinkMIBObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 631, 2, 2, 1)
)
cSCLinkMIBObjectGroup.setObjects(
      *(("CISCO-SERVICE-CONTROL-LINK-MIB", "cscLinkAdminModeOnActive"),
        ("CISCO-SERVICE-CONTROL-LINK-MIB", "cscLinkAdminModeOnFailure"),
        ("CISCO-SERVICE-CONTROL-LINK-MIB", "cscLinkOperMode"),
        ("CISCO-SERVICE-CONTROL-LINK-MIB", "cscLinkAdminReflectionEnable"),
        ("CISCO-SERVICE-CONTROL-LINK-MIB", "cscLinkSubscriberSidePortIndex"),
        ("CISCO-SERVICE-CONTROL-LINK-MIB", "cscLinkNetworkSidePortIndex"),
        ("CISCO-SERVICE-CONTROL-LINK-MIB", "cscLinkAdminReflectionState"))
)
if mibBuilder.loadTexts:
    cSCLinkMIBObjectGroup.setStatus("current")

cSCLinkNotifControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 631, 2, 2, 3)
)
cSCLinkNotifControlGroup.setObjects(
    ("CISCO-SERVICE-CONTROL-LINK-MIB", "cscLinkNotifsEnabled")
)
if mibBuilder.loadTexts:
    cSCLinkNotifControlGroup.setStatus("current")


# Notification objects

ciscoServiceControlLinkModeChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 631, 0, 1)
)
ciscoServiceControlLinkModeChange.setObjects(
    ("CISCO-SERVICE-CONTROL-LINK-MIB", "cscLinkOperMode")
)
if mibBuilder.loadTexts:
    ciscoServiceControlLinkModeChange.setStatus(
        "current"
    )


# Notifications groups

cSCLinkMIBNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 631, 2, 2, 2)
)
cSCLinkMIBNotificationGroup.setObjects(
    ("CISCO-SERVICE-CONTROL-LINK-MIB", "ciscoServiceControlLinkModeChange")
)
if mibBuilder.loadTexts:
    cSCLinkMIBNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

cServiceLinkMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 631, 2, 1, 1)
)
if mibBuilder.loadTexts:
    cServiceLinkMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-SERVICE-CONTROL-LINK-MIB",
    **{"CsceLinkModeType": CsceLinkModeType,
       "ciscoServiceControlLinkMIB": ciscoServiceControlLinkMIB,
       "ciscoSCLinkMIBNotifs": ciscoSCLinkMIBNotifs,
       "ciscoServiceControlLinkModeChange": ciscoServiceControlLinkModeChange,
       "ciscoSCLinkMIBObjects": ciscoSCLinkMIBObjects,
       "cscLinkNotifsEnabled": cscLinkNotifsEnabled,
       "cscLinkStatusTable": cscLinkStatusTable,
       "cscLinkStatusEntry": cscLinkStatusEntry,
       "cscLinkAdminModeOnActive": cscLinkAdminModeOnActive,
       "cscLinkAdminModeOnFailure": cscLinkAdminModeOnFailure,
       "cscLinkOperMode": cscLinkOperMode,
       "cscLinkAdminReflectionEnable": cscLinkAdminReflectionEnable,
       "cscLinkSubscriberSidePortIndex": cscLinkSubscriberSidePortIndex,
       "cscLinkNetworkSidePortIndex": cscLinkNetworkSidePortIndex,
       "cscLinkAdminReflectionState": cscLinkAdminReflectionState,
       "ciscoSCLinkMIBConform": ciscoSCLinkMIBConform,
       "ciscoSCLinkMIBCompliances": ciscoSCLinkMIBCompliances,
       "cServiceLinkMIBCompliance": cServiceLinkMIBCompliance,
       "ciscoSCLinkMIBObjectGroups": ciscoSCLinkMIBObjectGroups,
       "cSCLinkMIBObjectGroup": cSCLinkMIBObjectGroup,
       "cSCLinkMIBNotificationGroup": cSCLinkMIBNotificationGroup,
       "cSCLinkNotifControlGroup": cSCLinkNotifControlGroup}
)
