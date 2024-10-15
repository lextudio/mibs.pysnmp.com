# SNMP MIB module (CISCO-L2-DEV-MONITORING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-L2-DEV-MONITORING-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:03:45 2024
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoL2DevMonMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 271)
)
ciscoL2DevMonMIB.setRevisions(
        ("2003-07-22 00:00",
         "2001-09-27 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoL2DevMonMIBNotifications_ObjectIdentity = ObjectIdentity
ciscoL2DevMonMIBNotifications = _CiscoL2DevMonMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 271, 0)
)
_CiscoL2DevMonMIBObjects_ObjectIdentity = ObjectIdentity
ciscoL2DevMonMIBObjects = _CiscoL2DevMonMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 271, 1)
)
_Cl2DevMonConfig_ObjectIdentity = ObjectIdentity
cl2DevMonConfig = _Cl2DevMonConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 271, 1, 1)
)


class _Cl2DevMonInStandbyMode_Type(TruthValue):
    """Custom type cl2DevMonInStandbyMode based on TruthValue"""


_Cl2DevMonInStandbyMode_Object = MibScalar
cl2DevMonInStandbyMode = _Cl2DevMonInStandbyMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 271, 1, 1, 1),
    _Cl2DevMonInStandbyMode_Type()
)
cl2DevMonInStandbyMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cl2DevMonInStandbyMode.setStatus("current")


class _Cl2DevMonNotifEnabled_Type(TruthValue):
    """Custom type cl2DevMonNotifEnabled based on TruthValue"""


_Cl2DevMonNotifEnabled_Object = MibScalar
cl2DevMonNotifEnabled = _Cl2DevMonNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 271, 1, 1, 2),
    _Cl2DevMonNotifEnabled_Type()
)
cl2DevMonNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cl2DevMonNotifEnabled.setStatus("current")
_Cl2DevMonActiveTable_Object = MibTable
cl2DevMonActiveTable = _Cl2DevMonActiveTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 271, 1, 1, 3)
)
if mibBuilder.loadTexts:
    cl2DevMonActiveTable.setStatus("current")
_Cl2DevMonActiveEntry_Object = MibTableRow
cl2DevMonActiveEntry = _Cl2DevMonActiveEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 271, 1, 1, 3, 1)
)
cl2DevMonActiveEntry.setIndexNames(
    (0, "CISCO-L2-DEV-MONITORING-MIB", "cl2DevMonActiveMacAddress"),
)
if mibBuilder.loadTexts:
    cl2DevMonActiveEntry.setStatus("current")
_Cl2DevMonActiveMacAddress_Type = MacAddress
_Cl2DevMonActiveMacAddress_Object = MibTableColumn
cl2DevMonActiveMacAddress = _Cl2DevMonActiveMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 271, 1, 1, 3, 1, 1),
    _Cl2DevMonActiveMacAddress_Type()
)
cl2DevMonActiveMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cl2DevMonActiveMacAddress.setStatus("current")


class _Cl2DevMonActivePollingFrequency_Type(Unsigned32):
    """Custom type cl2DevMonActivePollingFrequency based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_Cl2DevMonActivePollingFrequency_Type.__name__ = "Unsigned32"
_Cl2DevMonActivePollingFrequency_Object = MibTableColumn
cl2DevMonActivePollingFrequency = _Cl2DevMonActivePollingFrequency_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 271, 1, 1, 3, 1, 2),
    _Cl2DevMonActivePollingFrequency_Type()
)
cl2DevMonActivePollingFrequency.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cl2DevMonActivePollingFrequency.setStatus("current")
if mibBuilder.loadTexts:
    cl2DevMonActivePollingFrequency.setUnits("seconds")


class _Cl2DevMonActivePollingTimeOut_Type(Unsigned32):
    """Custom type cl2DevMonActivePollingTimeOut based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_Cl2DevMonActivePollingTimeOut_Type.__name__ = "Unsigned32"
_Cl2DevMonActivePollingTimeOut_Object = MibTableColumn
cl2DevMonActivePollingTimeOut = _Cl2DevMonActivePollingTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 271, 1, 1, 3, 1, 3),
    _Cl2DevMonActivePollingTimeOut_Type()
)
cl2DevMonActivePollingTimeOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cl2DevMonActivePollingTimeOut.setStatus("current")
if mibBuilder.loadTexts:
    cl2DevMonActivePollingTimeOut.setUnits("seconds")
_Cl2DevMonActiveRowStatus_Type = RowStatus
_Cl2DevMonActiveRowStatus_Object = MibTableColumn
cl2DevMonActiveRowStatus = _Cl2DevMonActiveRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 271, 1, 1, 3, 1, 4),
    _Cl2DevMonActiveRowStatus_Type()
)
cl2DevMonActiveRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cl2DevMonActiveRowStatus.setStatus("current")


class _Cl2DevMonActiveRadioMacType_Type(Integer32):
    """Custom type cl2DevMonActiveRadioMacType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ieee802dot11a", 1),
          ("ieee802dot11b", 2),
          ("ieee802dot11g", 3))
    )


_Cl2DevMonActiveRadioMacType_Type.__name__ = "Integer32"
_Cl2DevMonActiveRadioMacType_Object = MibTableColumn
cl2DevMonActiveRadioMacType = _Cl2DevMonActiveRadioMacType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 271, 1, 1, 3, 1, 5),
    _Cl2DevMonActiveRadioMacType_Type()
)
cl2DevMonActiveRadioMacType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cl2DevMonActiveRadioMacType.setStatus("current")
_Cl2DevMonActiveLocalRadioIndex_Type = InterfaceIndex
_Cl2DevMonActiveLocalRadioIndex_Object = MibTableColumn
cl2DevMonActiveLocalRadioIndex = _Cl2DevMonActiveLocalRadioIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 271, 1, 1, 3, 1, 6),
    _Cl2DevMonActiveLocalRadioIndex_Type()
)
cl2DevMonActiveLocalRadioIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cl2DevMonActiveLocalRadioIndex.setStatus("current")
_CiscoL2DevMonMIBConformance_ObjectIdentity = ObjectIdentity
ciscoL2DevMonMIBConformance = _CiscoL2DevMonMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 271, 2)
)
_CiscoL2DevMonMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoL2DevMonMIBCompliances = _CiscoL2DevMonMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 271, 2, 1)
)
_CiscoL2DevMonMIBGroups_ObjectIdentity = ObjectIdentity
ciscoL2DevMonMIBGroups = _CiscoL2DevMonMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 271, 2, 2)
)

# Managed Objects groups

ciscoL2DevMonConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 271, 2, 2, 1)
)
ciscoL2DevMonConfigGroup.setObjects(
      *(("CISCO-L2-DEV-MONITORING-MIB", "cl2DevMonInStandbyMode"),
        ("CISCO-L2-DEV-MONITORING-MIB", "cl2DevMonNotifEnabled"),
        ("CISCO-L2-DEV-MONITORING-MIB", "cl2DevMonActivePollingFrequency"),
        ("CISCO-L2-DEV-MONITORING-MIB", "cl2DevMonActivePollingTimeOut"),
        ("CISCO-L2-DEV-MONITORING-MIB", "cl2DevMonActiveRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoL2DevMonConfigGroup.setStatus("current")

ciscoL2DevMonRadioConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 271, 2, 2, 3)
)
ciscoL2DevMonRadioConfigGroup.setObjects(
      *(("CISCO-L2-DEV-MONITORING-MIB", "cl2DevMonActiveRadioMacType"),
        ("CISCO-L2-DEV-MONITORING-MIB", "cl2DevMonActiveLocalRadioIndex"))
)
if mibBuilder.loadTexts:
    ciscoL2DevMonRadioConfigGroup.setStatus("current")


# Notification objects

cl2DevMonSwitchover = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 271, 0, 1)
)
cl2DevMonSwitchover.setObjects(
      *(("CISCO-L2-DEV-MONITORING-MIB", "cl2DevMonActivePollingFrequency"),
        ("CISCO-L2-DEV-MONITORING-MIB", "cl2DevMonActivePollingTimeOut"))
)
if mibBuilder.loadTexts:
    cl2DevMonSwitchover.setStatus(
        "current"
    )


# Notifications groups

ciscoL2DevMonNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 271, 2, 2, 2)
)
ciscoL2DevMonNotificationGroup.setObjects(
    ("CISCO-L2-DEV-MONITORING-MIB", "cl2DevMonSwitchover")
)
if mibBuilder.loadTexts:
    ciscoL2DevMonNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoL2DevMonCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 271, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoL2DevMonCompliance.setStatus(
        "deprecated"
    )

ciscoL2DevMonComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 271, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoL2DevMonComplianceRev1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-L2-DEV-MONITORING-MIB",
    **{"ciscoL2DevMonMIB": ciscoL2DevMonMIB,
       "ciscoL2DevMonMIBNotifications": ciscoL2DevMonMIBNotifications,
       "cl2DevMonSwitchover": cl2DevMonSwitchover,
       "ciscoL2DevMonMIBObjects": ciscoL2DevMonMIBObjects,
       "cl2DevMonConfig": cl2DevMonConfig,
       "cl2DevMonInStandbyMode": cl2DevMonInStandbyMode,
       "cl2DevMonNotifEnabled": cl2DevMonNotifEnabled,
       "cl2DevMonActiveTable": cl2DevMonActiveTable,
       "cl2DevMonActiveEntry": cl2DevMonActiveEntry,
       "cl2DevMonActiveMacAddress": cl2DevMonActiveMacAddress,
       "cl2DevMonActivePollingFrequency": cl2DevMonActivePollingFrequency,
       "cl2DevMonActivePollingTimeOut": cl2DevMonActivePollingTimeOut,
       "cl2DevMonActiveRowStatus": cl2DevMonActiveRowStatus,
       "cl2DevMonActiveRadioMacType": cl2DevMonActiveRadioMacType,
       "cl2DevMonActiveLocalRadioIndex": cl2DevMonActiveLocalRadioIndex,
       "ciscoL2DevMonMIBConformance": ciscoL2DevMonMIBConformance,
       "ciscoL2DevMonMIBCompliances": ciscoL2DevMonMIBCompliances,
       "ciscoL2DevMonCompliance": ciscoL2DevMonCompliance,
       "ciscoL2DevMonComplianceRev1": ciscoL2DevMonComplianceRev1,
       "ciscoL2DevMonMIBGroups": ciscoL2DevMonMIBGroups,
       "ciscoL2DevMonConfigGroup": ciscoL2DevMonConfigGroup,
       "ciscoL2DevMonNotificationGroup": ciscoL2DevMonNotificationGroup,
       "ciscoL2DevMonRadioConfigGroup": ciscoL2DevMonRadioConfigGroup}
)
