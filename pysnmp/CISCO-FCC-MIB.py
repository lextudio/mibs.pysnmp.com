# SNMP MIB module (CISCO-FCC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-FCC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:00:21 2024
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

(FcAddressId,
 VsanIndex) = mibBuilder.importSymbols(
    "CISCO-ST-TC",
    "FcAddressId",
    "VsanIndex")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoFCCMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 365)
)
ciscoFCCMIB.setRevisions(
        ("2004-07-08 00:00",
         "2004-02-25 00:00",
         "2003-08-06 00:00",
         "2003-05-26 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CiscoFCCCongestionState(Integer32, TextualConvention):
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
        *(("congested", 2),
          ("noCongestion", 1),
          ("severelyCongested", 3))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoFCCMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoFCCMIBNotifs = _CiscoFCCMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 365, 0)
)
_CiscoFCCMIBObjects_ObjectIdentity = ObjectIdentity
ciscoFCCMIBObjects = _CiscoFCCMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 365, 1)
)
_CFCCConfig_ObjectIdentity = ObjectIdentity
cFCCConfig = _CFCCConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 365, 1, 1)
)


class _CFCCEnable_Type(Integer32):
    """Custom type cFCCEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_CFCCEnable_Type.__name__ = "Integer32"
_CFCCEnable_Object = MibScalar
cFCCEnable = _CFCCEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 365, 1, 1, 1),
    _CFCCEnable_Type()
)
cFCCEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cFCCEnable.setStatus("current")


class _CFCCPacketPriority_Type(Integer32):
    """Custom type cFCCPacketPriority based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_CFCCPacketPriority_Type.__name__ = "Integer32"
_CFCCPacketPriority_Object = MibScalar
cFCCPacketPriority = _CFCCPacketPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 365, 1, 1, 2),
    _CFCCPacketPriority_Type()
)
cFCCPacketPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cFCCPacketPriority.setStatus("current")


class _CFCCNotificationEnable_Type(TruthValue):
    """Custom type cFCCNotificationEnable based on TruthValue"""


_CFCCNotificationEnable_Object = MibScalar
cFCCNotificationEnable = _CFCCNotificationEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 365, 1, 1, 3),
    _CFCCNotificationEnable_Type()
)
cFCCNotificationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cFCCNotificationEnable.setStatus("current")
_CFCCPortEntries_ObjectIdentity = ObjectIdentity
cFCCPortEntries = _CFCCPortEntries_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 365, 1, 2)
)
_CFCCPortTable_Object = MibTable
cFCCPortTable = _CFCCPortTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 365, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cFCCPortTable.setStatus("current")
_CFCCPortEntry_Object = MibTableRow
cFCCPortEntry = _CFCCPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 365, 1, 2, 1, 1)
)
cFCCPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cFCCPortEntry.setStatus("current")
_CFCCEdgeQuenchPktsRecd_Type = Counter32
_CFCCEdgeQuenchPktsRecd_Object = MibTableColumn
cFCCEdgeQuenchPktsRecd = _CFCCEdgeQuenchPktsRecd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 365, 1, 2, 1, 1, 1),
    _CFCCEdgeQuenchPktsRecd_Type()
)
cFCCEdgeQuenchPktsRecd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cFCCEdgeQuenchPktsRecd.setStatus("current")
_CFCCEdgeQuenchPktsSent_Type = Counter32
_CFCCEdgeQuenchPktsSent_Object = MibTableColumn
cFCCEdgeQuenchPktsSent = _CFCCEdgeQuenchPktsSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 365, 1, 2, 1, 1, 2),
    _CFCCEdgeQuenchPktsSent_Type()
)
cFCCEdgeQuenchPktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cFCCEdgeQuenchPktsSent.setStatus("current")
_CFCCPathQuenchPktsRecd_Type = Counter32
_CFCCPathQuenchPktsRecd_Object = MibTableColumn
cFCCPathQuenchPktsRecd = _CFCCPathQuenchPktsRecd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 365, 1, 2, 1, 1, 3),
    _CFCCPathQuenchPktsRecd_Type()
)
cFCCPathQuenchPktsRecd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cFCCPathQuenchPktsRecd.setStatus("current")
_CFCCPathQuenchPktsSent_Type = Counter32
_CFCCPathQuenchPktsSent_Object = MibTableColumn
cFCCPathQuenchPktsSent = _CFCCPathQuenchPktsSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 365, 1, 2, 1, 1, 4),
    _CFCCPathQuenchPktsSent_Type()
)
cFCCPathQuenchPktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cFCCPathQuenchPktsSent.setStatus("current")
_CFCCCurrentCongestionState_Type = CiscoFCCCongestionState
_CFCCCurrentCongestionState_Object = MibTableColumn
cFCCCurrentCongestionState = _CFCCCurrentCongestionState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 365, 1, 2, 1, 1, 5),
    _CFCCCurrentCongestionState_Type()
)
cFCCCurrentCongestionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cFCCCurrentCongestionState.setStatus("current")
_CFCCLastCongestedTime_Type = TimeStamp
_CFCCLastCongestedTime_Object = MibTableColumn
cFCCLastCongestedTime = _CFCCLastCongestedTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 365, 1, 2, 1, 1, 6),
    _CFCCLastCongestedTime_Type()
)
cFCCLastCongestedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cFCCLastCongestedTime.setStatus("current")
_CFCCLastCongestionStartTime_Type = TimeStamp
_CFCCLastCongestionStartTime_Object = MibTableColumn
cFCCLastCongestionStartTime = _CFCCLastCongestionStartTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 365, 1, 2, 1, 1, 7),
    _CFCCLastCongestionStartTime_Type()
)
cFCCLastCongestionStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cFCCLastCongestionStartTime.setStatus("current")
_CFCCIsRateLimitingApplied_Type = TruthValue
_CFCCIsRateLimitingApplied_Object = MibTableColumn
cFCCIsRateLimitingApplied = _CFCCIsRateLimitingApplied_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 365, 1, 2, 1, 1, 8),
    _CFCCIsRateLimitingApplied_Type()
)
cFCCIsRateLimitingApplied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cFCCIsRateLimitingApplied.setStatus("current")
_CFCCNotifObjects_ObjectIdentity = ObjectIdentity
cFCCNotifObjects = _CFCCNotifObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 365, 1, 3)
)
_CFCCCongestionSourceID_Type = FcAddressId
_CFCCCongestionSourceID_Object = MibScalar
cFCCCongestionSourceID = _CFCCCongestionSourceID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 365, 1, 3, 1),
    _CFCCCongestionSourceID_Type()
)
cFCCCongestionSourceID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cFCCCongestionSourceID.setStatus("current")
_CFCCCongestionDestinationID_Type = FcAddressId
_CFCCCongestionDestinationID_Object = MibScalar
cFCCCongestionDestinationID = _CFCCCongestionDestinationID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 365, 1, 3, 2),
    _CFCCCongestionDestinationID_Type()
)
cFCCCongestionDestinationID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cFCCCongestionDestinationID.setStatus("current")
_CFCCCongestionNotifyVSANIndex_Type = VsanIndex
_CFCCCongestionNotifyVSANIndex_Object = MibScalar
cFCCCongestionNotifyVSANIndex = _CFCCCongestionNotifyVSANIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 365, 1, 3, 3),
    _CFCCCongestionNotifyVSANIndex_Type()
)
cFCCCongestionNotifyVSANIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cFCCCongestionNotifyVSANIndex.setStatus("current")
_CFCCCongestionState_Type = CiscoFCCCongestionState
_CFCCCongestionState_Object = MibScalar
cFCCCongestionState = _CFCCCongestionState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 365, 1, 3, 4),
    _CFCCCongestionState_Type()
)
cFCCCongestionState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cFCCCongestionState.setStatus("current")
_CiscoFCCMIBConformance_ObjectIdentity = ObjectIdentity
ciscoFCCMIBConformance = _CiscoFCCMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 365, 2)
)
_CiscoFCCMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoFCCMIBCompliances = _CiscoFCCMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 365, 2, 1)
)
_CiscoFCCMIBGroups_ObjectIdentity = ObjectIdentity
ciscoFCCMIBGroups = _CiscoFCCMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 365, 2, 2)
)

# Managed Objects groups

cFCCConfigurationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 365, 2, 2, 1)
)
cFCCConfigurationGroup.setObjects(
      *(("CISCO-FCC-MIB", "cFCCEnable"),
        ("CISCO-FCC-MIB", "cFCCPacketPriority"),
        ("CISCO-FCC-MIB", "cFCCNotificationEnable"))
)
if mibBuilder.loadTexts:
    cFCCConfigurationGroup.setStatus("current")

cFCCPortEntriesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 365, 2, 2, 2)
)
cFCCPortEntriesGroup.setObjects(
      *(("CISCO-FCC-MIB", "cFCCEdgeQuenchPktsRecd"),
        ("CISCO-FCC-MIB", "cFCCEdgeQuenchPktsSent"),
        ("CISCO-FCC-MIB", "cFCCPathQuenchPktsRecd"),
        ("CISCO-FCC-MIB", "cFCCPathQuenchPktsSent"),
        ("CISCO-FCC-MIB", "cFCCCurrentCongestionState"),
        ("CISCO-FCC-MIB", "cFCCLastCongestedTime"))
)
if mibBuilder.loadTexts:
    cFCCPortEntriesGroup.setStatus("deprecated")

cFCCNotificationObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 365, 2, 2, 3)
)
cFCCNotificationObjectsGroup.setObjects(
      *(("CISCO-FCC-MIB", "cFCCCongestionDestinationID"),
        ("CISCO-FCC-MIB", "cFCCCongestionSourceID"),
        ("CISCO-FCC-MIB", "cFCCCongestionNotifyVSANIndex"),
        ("CISCO-FCC-MIB", "cFCCCongestionState"))
)
if mibBuilder.loadTexts:
    cFCCNotificationObjectsGroup.setStatus("current")

cFCCPortEntriesGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 365, 2, 2, 5)
)
cFCCPortEntriesGroupRev1.setObjects(
      *(("CISCO-FCC-MIB", "cFCCEdgeQuenchPktsRecd"),
        ("CISCO-FCC-MIB", "cFCCEdgeQuenchPktsSent"),
        ("CISCO-FCC-MIB", "cFCCPathQuenchPktsRecd"),
        ("CISCO-FCC-MIB", "cFCCPathQuenchPktsSent"),
        ("CISCO-FCC-MIB", "cFCCCurrentCongestionState"),
        ("CISCO-FCC-MIB", "cFCCLastCongestedTime"),
        ("CISCO-FCC-MIB", "cFCCLastCongestionStartTime"),
        ("CISCO-FCC-MIB", "cFCCIsRateLimitingApplied"))
)
if mibBuilder.loadTexts:
    cFCCPortEntriesGroupRev1.setStatus("current")


# Notification objects

ciscoFCCCongestionStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 365, 0, 1)
)
ciscoFCCCongestionStateChange.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CISCO-FCC-MIB", "cFCCCongestionState"))
)
if mibBuilder.loadTexts:
    ciscoFCCCongestionStateChange.setStatus(
        "current"
    )

ciscoFCCCongestionRateLimitStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 365, 0, 2)
)
ciscoFCCCongestionRateLimitStart.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CISCO-FCC-MIB", "cFCCCongestionSourceID"),
        ("CISCO-FCC-MIB", "cFCCCongestionDestinationID"),
        ("CISCO-FCC-MIB", "cFCCCongestionNotifyVSANIndex"))
)
if mibBuilder.loadTexts:
    ciscoFCCCongestionRateLimitStart.setStatus(
        "current"
    )

ciscoFCCCongestionRateLimitEnd = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 365, 0, 3)
)
ciscoFCCCongestionRateLimitEnd.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CISCO-FCC-MIB", "cFCCCongestionSourceID"),
        ("CISCO-FCC-MIB", "cFCCCongestionDestinationID"),
        ("CISCO-FCC-MIB", "cFCCCongestionNotifyVSANIndex"))
)
if mibBuilder.loadTexts:
    ciscoFCCCongestionRateLimitEnd.setStatus(
        "current"
    )


# Notifications groups

cFCCNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 365, 2, 2, 4)
)
cFCCNotificationGroup.setObjects(
      *(("CISCO-FCC-MIB", "ciscoFCCCongestionStateChange"),
        ("CISCO-FCC-MIB", "ciscoFCCCongestionRateLimitStart"),
        ("CISCO-FCC-MIB", "ciscoFCCCongestionRateLimitEnd"))
)
if mibBuilder.loadTexts:
    cFCCNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoFCCMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 365, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoFCCMIBCompliance.setStatus(
        "deprecated"
    )

ciscoFCCMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 365, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoFCCMIBComplianceRev1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FCC-MIB",
    **{"CiscoFCCCongestionState": CiscoFCCCongestionState,
       "ciscoFCCMIB": ciscoFCCMIB,
       "ciscoFCCMIBNotifs": ciscoFCCMIBNotifs,
       "ciscoFCCCongestionStateChange": ciscoFCCCongestionStateChange,
       "ciscoFCCCongestionRateLimitStart": ciscoFCCCongestionRateLimitStart,
       "ciscoFCCCongestionRateLimitEnd": ciscoFCCCongestionRateLimitEnd,
       "ciscoFCCMIBObjects": ciscoFCCMIBObjects,
       "cFCCConfig": cFCCConfig,
       "cFCCEnable": cFCCEnable,
       "cFCCPacketPriority": cFCCPacketPriority,
       "cFCCNotificationEnable": cFCCNotificationEnable,
       "cFCCPortEntries": cFCCPortEntries,
       "cFCCPortTable": cFCCPortTable,
       "cFCCPortEntry": cFCCPortEntry,
       "cFCCEdgeQuenchPktsRecd": cFCCEdgeQuenchPktsRecd,
       "cFCCEdgeQuenchPktsSent": cFCCEdgeQuenchPktsSent,
       "cFCCPathQuenchPktsRecd": cFCCPathQuenchPktsRecd,
       "cFCCPathQuenchPktsSent": cFCCPathQuenchPktsSent,
       "cFCCCurrentCongestionState": cFCCCurrentCongestionState,
       "cFCCLastCongestedTime": cFCCLastCongestedTime,
       "cFCCLastCongestionStartTime": cFCCLastCongestionStartTime,
       "cFCCIsRateLimitingApplied": cFCCIsRateLimitingApplied,
       "cFCCNotifObjects": cFCCNotifObjects,
       "cFCCCongestionSourceID": cFCCCongestionSourceID,
       "cFCCCongestionDestinationID": cFCCCongestionDestinationID,
       "cFCCCongestionNotifyVSANIndex": cFCCCongestionNotifyVSANIndex,
       "cFCCCongestionState": cFCCCongestionState,
       "ciscoFCCMIBConformance": ciscoFCCMIBConformance,
       "ciscoFCCMIBCompliances": ciscoFCCMIBCompliances,
       "ciscoFCCMIBCompliance": ciscoFCCMIBCompliance,
       "ciscoFCCMIBComplianceRev1": ciscoFCCMIBComplianceRev1,
       "ciscoFCCMIBGroups": ciscoFCCMIBGroups,
       "cFCCConfigurationGroup": cFCCConfigurationGroup,
       "cFCCPortEntriesGroup": cFCCPortEntriesGroup,
       "cFCCNotificationObjectsGroup": cFCCNotificationObjectsGroup,
       "cFCCNotificationGroup": cFCCNotificationGroup,
       "cFCCPortEntriesGroupRev1": cFCCPortEntriesGroupRev1}
)
