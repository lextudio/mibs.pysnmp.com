# SNMP MIB module (CISCO-SWITCH-FABRIC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-SWITCH-FABRIC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:09:08 2024
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

(PhysicalIndex,
 entPhysicalIndex) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "PhysicalIndex",
    "entPhysicalIndex")

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

(DateAndTime,
 DisplayString,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoSwitchFabricMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 803)
)
ciscoSwitchFabricMIB.setRevisions(
        ("2014-07-30 00:00",
         "2012-06-12 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CsfFabricLinkType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("centralXbarLink", 7),
          ("fabricFacingLcXbarLink", 4),
          ("fabricXbarInterLink", 6),
          ("fabricXbarLink", 3),
          ("lcXbarInterLink", 5),
          ("other", 1),
          ("qEngineFacingLcXbarLink", 2))
    )



class CsfPercentOrMinusOne(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 100),
    )



# MIB Managed Objects in the order of their OIDs

_CiscoSwitchFabricMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoSwitchFabricMIBNotifs = _CiscoSwitchFabricMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 803, 0)
)
_CiscoSwitchFabricMIBObjects_ObjectIdentity = ObjectIdentity
ciscoSwitchFabricMIBObjects = _CiscoSwitchFabricMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 803, 1)
)
_CsfFabricStatistics_ObjectIdentity = ObjectIdentity
csfFabricStatistics = _CsfFabricStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 803, 1, 1)
)
_CsfFabricUtilTable_Object = MibTable
csfFabricUtilTable = _CsfFabricUtilTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 803, 1, 1, 1)
)
if mibBuilder.loadTexts:
    csfFabricUtilTable.setStatus("current")
_CsfFabricUtilEntry_Object = MibTableRow
csfFabricUtilEntry = _CsfFabricUtilEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 803, 1, 1, 1, 1)
)
csfFabricUtilEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-SWITCH-FABRIC-MIB", "csfFabricUtilLinkType"),
    (0, "CISCO-SWITCH-FABRIC-MIB", "csfFabricUtilIndex"),
)
if mibBuilder.loadTexts:
    csfFabricUtilEntry.setStatus("current")
_CsfFabricUtilLinkType_Type = CsfFabricLinkType
_CsfFabricUtilLinkType_Object = MibTableColumn
csfFabricUtilLinkType = _CsfFabricUtilLinkType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 803, 1, 1, 1, 1, 1),
    _CsfFabricUtilLinkType_Type()
)
csfFabricUtilLinkType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    csfFabricUtilLinkType.setStatus("current")
_CsfFabricUtilIndex_Type = Unsigned32
_CsfFabricUtilIndex_Object = MibTableColumn
csfFabricUtilIndex = _CsfFabricUtilIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 803, 1, 1, 1, 1, 2),
    _CsfFabricUtilIndex_Type()
)
csfFabricUtilIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    csfFabricUtilIndex.setStatus("current")
_CsfFabricUtilDescr_Type = SnmpAdminString
_CsfFabricUtilDescr_Object = MibTableColumn
csfFabricUtilDescr = _CsfFabricUtilDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 803, 1, 1, 1, 1, 3),
    _CsfFabricUtilDescr_Type()
)
csfFabricUtilDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csfFabricUtilDescr.setStatus("current")
_CsfFabricUtilBandwidth_Type = Unsigned32
_CsfFabricUtilBandwidth_Object = MibTableColumn
csfFabricUtilBandwidth = _CsfFabricUtilBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 803, 1, 1, 1, 1, 4),
    _CsfFabricUtilBandwidth_Type()
)
csfFabricUtilBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csfFabricUtilBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    csfFabricUtilBandwidth.setUnits("gigabits per second")
_CsfFabricUtilIn_Type = CsfPercentOrMinusOne
_CsfFabricUtilIn_Object = MibTableColumn
csfFabricUtilIn = _CsfFabricUtilIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 803, 1, 1, 1, 1, 5),
    _CsfFabricUtilIn_Type()
)
csfFabricUtilIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csfFabricUtilIn.setStatus("current")
_CsfFabricUtilInPeak_Type = CsfPercentOrMinusOne
_CsfFabricUtilInPeak_Object = MibTableColumn
csfFabricUtilInPeak = _CsfFabricUtilInPeak_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 803, 1, 1, 1, 1, 6),
    _CsfFabricUtilInPeak_Type()
)
csfFabricUtilInPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csfFabricUtilInPeak.setStatus("current")
_CsfFabricUtilInPeakTime_Type = DateAndTime
_CsfFabricUtilInPeakTime_Object = MibTableColumn
csfFabricUtilInPeakTime = _CsfFabricUtilInPeakTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 803, 1, 1, 1, 1, 7),
    _CsfFabricUtilInPeakTime_Type()
)
csfFabricUtilInPeakTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csfFabricUtilInPeakTime.setStatus("current")
_CsfFabricUtilOut_Type = CsfPercentOrMinusOne
_CsfFabricUtilOut_Object = MibTableColumn
csfFabricUtilOut = _CsfFabricUtilOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 803, 1, 1, 1, 1, 8),
    _CsfFabricUtilOut_Type()
)
csfFabricUtilOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csfFabricUtilOut.setStatus("current")
_CsfFabricUtilOutPeak_Type = CsfPercentOrMinusOne
_CsfFabricUtilOutPeak_Object = MibTableColumn
csfFabricUtilOutPeak = _CsfFabricUtilOutPeak_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 803, 1, 1, 1, 1, 9),
    _CsfFabricUtilOutPeak_Type()
)
csfFabricUtilOutPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csfFabricUtilOutPeak.setStatus("current")
_CsfFabricUtilOutPeakTime_Type = DateAndTime
_CsfFabricUtilOutPeakTime_Object = MibTableColumn
csfFabricUtilOutPeakTime = _CsfFabricUtilOutPeakTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 803, 1, 1, 1, 1, 10),
    _CsfFabricUtilOutPeakTime_Type()
)
csfFabricUtilOutPeakTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csfFabricUtilOutPeakTime.setStatus("current")
_CsfNotifsControl_ObjectIdentity = ObjectIdentity
csfNotifsControl = _CsfNotifsControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 803, 1, 2)
)
_CsfFabricCrcErrorNotifEnable_Type = TruthValue
_CsfFabricCrcErrorNotifEnable_Object = MibScalar
csfFabricCrcErrorNotifEnable = _CsfFabricCrcErrorNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 803, 1, 2, 1),
    _CsfFabricCrcErrorNotifEnable_Type()
)
csfFabricCrcErrorNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csfFabricCrcErrorNotifEnable.setStatus("current")
_CsfNotifsOnlyInfo_ObjectIdentity = ObjectIdentity
csfNotifsOnlyInfo = _CsfNotifsOnlyInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 803, 1, 3)
)
_CsfFabricCrcErrorEntPhysicalIndex_Type = PhysicalIndex
_CsfFabricCrcErrorEntPhysicalIndex_Object = MibScalar
csfFabricCrcErrorEntPhysicalIndex = _CsfFabricCrcErrorEntPhysicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 803, 1, 3, 1),
    _CsfFabricCrcErrorEntPhysicalIndex_Type()
)
csfFabricCrcErrorEntPhysicalIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    csfFabricCrcErrorEntPhysicalIndex.setStatus("current")
_CsfFabricCrcErrorDescr_Type = SnmpAdminString
_CsfFabricCrcErrorDescr_Object = MibScalar
csfFabricCrcErrorDescr = _CsfFabricCrcErrorDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 803, 1, 3, 2),
    _CsfFabricCrcErrorDescr_Type()
)
csfFabricCrcErrorDescr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    csfFabricCrcErrorDescr.setStatus("current")
_CiscoSwitchFabricMIBConform_ObjectIdentity = ObjectIdentity
ciscoSwitchFabricMIBConform = _CiscoSwitchFabricMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 803, 2)
)
_CsfSwitchFabricMIBCompliances_ObjectIdentity = ObjectIdentity
csfSwitchFabricMIBCompliances = _CsfSwitchFabricMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 803, 2, 1)
)
_CsfSwitchFabricMIBGroups_ObjectIdentity = ObjectIdentity
csfSwitchFabricMIBGroups = _CsfSwitchFabricMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 803, 2, 2)
)

# Managed Objects groups

csfFabricUtilGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 803, 2, 2, 1)
)
csfFabricUtilGroup.setObjects(
      *(("CISCO-SWITCH-FABRIC-MIB", "csfFabricUtilDescr"),
        ("CISCO-SWITCH-FABRIC-MIB", "csfFabricUtilBandwidth"),
        ("CISCO-SWITCH-FABRIC-MIB", "csfFabricUtilIn"),
        ("CISCO-SWITCH-FABRIC-MIB", "csfFabricUtilInPeak"),
        ("CISCO-SWITCH-FABRIC-MIB", "csfFabricUtilInPeakTime"),
        ("CISCO-SWITCH-FABRIC-MIB", "csfFabricUtilOut"),
        ("CISCO-SWITCH-FABRIC-MIB", "csfFabricUtilOutPeak"),
        ("CISCO-SWITCH-FABRIC-MIB", "csfFabricUtilOutPeakTime"))
)
if mibBuilder.loadTexts:
    csfFabricUtilGroup.setStatus("current")

csfFabricCrcErrorNotifsControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 803, 2, 2, 2)
)
csfFabricCrcErrorNotifsControlGroup.setObjects(
    ("CISCO-SWITCH-FABRIC-MIB", "csfFabricCrcErrorNotifEnable")
)
if mibBuilder.loadTexts:
    csfFabricCrcErrorNotifsControlGroup.setStatus("current")

csfFabricCrcErrorNotifsInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 803, 2, 2, 3)
)
csfFabricCrcErrorNotifsInfoGroup.setObjects(
      *(("CISCO-SWITCH-FABRIC-MIB", "csfFabricCrcErrorEntPhysicalIndex"),
        ("CISCO-SWITCH-FABRIC-MIB", "csfFabricCrcErrorDescr"))
)
if mibBuilder.loadTexts:
    csfFabricCrcErrorNotifsInfoGroup.setStatus("current")


# Notification objects

csfFabricCrcErrorNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 803, 0, 1)
)
csfFabricCrcErrorNotif.setObjects(
      *(("CISCO-SWITCH-FABRIC-MIB", "csfFabricCrcErrorEntPhysicalIndex"),
        ("CISCO-SWITCH-FABRIC-MIB", "csfFabricCrcErrorDescr"))
)
if mibBuilder.loadTexts:
    csfFabricCrcErrorNotif.setStatus(
        "current"
    )


# Notifications groups

csfFabricCrcErrorNotifsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 803, 2, 2, 4)
)
csfFabricCrcErrorNotifsGroup.setObjects(
    ("CISCO-SWITCH-FABRIC-MIB", "csfFabricCrcErrorNotif")
)
if mibBuilder.loadTexts:
    csfFabricCrcErrorNotifsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

csfSwitchFabricMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 803, 2, 1, 1)
)
if mibBuilder.loadTexts:
    csfSwitchFabricMIBCompliance.setStatus(
        "deprecated"
    )

csfSwitchFabricMIBCompliance1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 803, 2, 1, 2)
)
if mibBuilder.loadTexts:
    csfSwitchFabricMIBCompliance1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-SWITCH-FABRIC-MIB",
    **{"CsfFabricLinkType": CsfFabricLinkType,
       "CsfPercentOrMinusOne": CsfPercentOrMinusOne,
       "ciscoSwitchFabricMIB": ciscoSwitchFabricMIB,
       "ciscoSwitchFabricMIBNotifs": ciscoSwitchFabricMIBNotifs,
       "csfFabricCrcErrorNotif": csfFabricCrcErrorNotif,
       "ciscoSwitchFabricMIBObjects": ciscoSwitchFabricMIBObjects,
       "csfFabricStatistics": csfFabricStatistics,
       "csfFabricUtilTable": csfFabricUtilTable,
       "csfFabricUtilEntry": csfFabricUtilEntry,
       "csfFabricUtilLinkType": csfFabricUtilLinkType,
       "csfFabricUtilIndex": csfFabricUtilIndex,
       "csfFabricUtilDescr": csfFabricUtilDescr,
       "csfFabricUtilBandwidth": csfFabricUtilBandwidth,
       "csfFabricUtilIn": csfFabricUtilIn,
       "csfFabricUtilInPeak": csfFabricUtilInPeak,
       "csfFabricUtilInPeakTime": csfFabricUtilInPeakTime,
       "csfFabricUtilOut": csfFabricUtilOut,
       "csfFabricUtilOutPeak": csfFabricUtilOutPeak,
       "csfFabricUtilOutPeakTime": csfFabricUtilOutPeakTime,
       "csfNotifsControl": csfNotifsControl,
       "csfFabricCrcErrorNotifEnable": csfFabricCrcErrorNotifEnable,
       "csfNotifsOnlyInfo": csfNotifsOnlyInfo,
       "csfFabricCrcErrorEntPhysicalIndex": csfFabricCrcErrorEntPhysicalIndex,
       "csfFabricCrcErrorDescr": csfFabricCrcErrorDescr,
       "ciscoSwitchFabricMIBConform": ciscoSwitchFabricMIBConform,
       "csfSwitchFabricMIBCompliances": csfSwitchFabricMIBCompliances,
       "csfSwitchFabricMIBCompliance": csfSwitchFabricMIBCompliance,
       "csfSwitchFabricMIBCompliance1": csfSwitchFabricMIBCompliance1,
       "csfSwitchFabricMIBGroups": csfSwitchFabricMIBGroups,
       "csfFabricUtilGroup": csfFabricUtilGroup,
       "csfFabricCrcErrorNotifsControlGroup": csfFabricCrcErrorNotifsControlGroup,
       "csfFabricCrcErrorNotifsInfoGroup": csfFabricCrcErrorNotifsInfoGroup,
       "csfFabricCrcErrorNotifsGroup": csfFabricCrcErrorNotifsGroup}
)
