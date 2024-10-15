# SNMP MIB module (CISCO-LWAPP-CCX-RM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-LWAPP-CCX-RM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:04:12 2024
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

(cLApDot11IfEntry,
 cLApDot11IfSlotId,
 cLApSysMacAddress) = mibBuilder.importSymbols(
    "CISCO-LWAPP-AP-MIB",
    "cLApDot11IfEntry",
    "cLApDot11IfSlotId",
    "cLApSysMacAddress")

(cLWlanConfigEntry,) = mibBuilder.importSymbols(
    "CISCO-LWAPP-WLAN-MIB",
    "cLWlanConfigEntry")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

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
 TextualConvention,
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoLwappCcxRmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 520)
)
ciscoLwappCcxRmMIB.setRevisions(
        ("2012-02-21 00:00",
         "2006-04-11 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoLwappCcxRmMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoLwappCcxRmMIBNotifs = _CiscoLwappCcxRmMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 520, 0)
)
_CiscoLwappCcxRmMIBObjects_ObjectIdentity = ObjectIdentity
ciscoLwappCcxRmMIBObjects = _CiscoLwappCcxRmMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 520, 1)
)
_ClcrDot11aConfigGlobal_ObjectIdentity = ObjectIdentity
clcrDot11aConfigGlobal = _ClcrDot11aConfigGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 520, 1, 1)
)


class _Clcrdot11aBeaconEnabled_Type(TruthValue):
    """Custom type clcrdot11aBeaconEnabled based on TruthValue"""


_Clcrdot11aBeaconEnabled_Object = MibScalar
clcrdot11aBeaconEnabled = _Clcrdot11aBeaconEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 520, 1, 1, 1),
    _Clcrdot11aBeaconEnabled_Type()
)
clcrdot11aBeaconEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clcrdot11aBeaconEnabled.setStatus("current")


class _Clcrdot11aBeaconInterval_Type(TimeInterval):
    """Custom type clcrdot11aBeaconInterval based on TimeInterval"""
    defaultValue = 6000

    subtypeSpec = TimeInterval.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6000, 3240000),
    )


_Clcrdot11aBeaconInterval_Type.__name__ = "TimeInterval"
_Clcrdot11aBeaconInterval_Object = MibScalar
clcrdot11aBeaconInterval = _Clcrdot11aBeaconInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 520, 1, 1, 2),
    _Clcrdot11aBeaconInterval_Type()
)
clcrdot11aBeaconInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clcrdot11aBeaconInterval.setStatus("deprecated")
if mibBuilder.loadTexts:
    clcrdot11aBeaconInterval.setUnits("hundredths-seconds")
_Clcrdot11aBeaconIntvl_Type = TimeInterval
_Clcrdot11aBeaconIntvl_Object = MibScalar
clcrdot11aBeaconIntvl = _Clcrdot11aBeaconIntvl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 520, 1, 1, 3),
    _Clcrdot11aBeaconIntvl_Type()
)
clcrdot11aBeaconIntvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clcrdot11aBeaconIntvl.setStatus("current")
if mibBuilder.loadTexts:
    clcrdot11aBeaconIntvl.setUnits("hundredths-seconds")
_ClcrDot11bConfigGlobal_ObjectIdentity = ObjectIdentity
clcrDot11bConfigGlobal = _ClcrDot11bConfigGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 520, 1, 2)
)


class _Clcrdot11bBeaconEnabled_Type(TruthValue):
    """Custom type clcrdot11bBeaconEnabled based on TruthValue"""


_Clcrdot11bBeaconEnabled_Object = MibScalar
clcrdot11bBeaconEnabled = _Clcrdot11bBeaconEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 520, 1, 2, 1),
    _Clcrdot11bBeaconEnabled_Type()
)
clcrdot11bBeaconEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clcrdot11bBeaconEnabled.setStatus("current")


class _Clcrdot11bBeaconInterval_Type(TimeInterval):
    """Custom type clcrdot11bBeaconInterval based on TimeInterval"""
    defaultValue = 6000

    subtypeSpec = TimeInterval.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6000, 3240000),
    )


_Clcrdot11bBeaconInterval_Type.__name__ = "TimeInterval"
_Clcrdot11bBeaconInterval_Object = MibScalar
clcrdot11bBeaconInterval = _Clcrdot11bBeaconInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 520, 1, 2, 2),
    _Clcrdot11bBeaconInterval_Type()
)
clcrdot11bBeaconInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clcrdot11bBeaconInterval.setStatus("deprecated")
if mibBuilder.loadTexts:
    clcrdot11bBeaconInterval.setUnits("hundredths-seconds")
_Clcrdot11bBeaconIntvl_Type = TimeInterval
_Clcrdot11bBeaconIntvl_Object = MibScalar
clcrdot11bBeaconIntvl = _Clcrdot11bBeaconIntvl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 520, 1, 2, 3),
    _Clcrdot11bBeaconIntvl_Type()
)
clcrdot11bBeaconIntvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clcrdot11bBeaconIntvl.setStatus("current")
if mibBuilder.loadTexts:
    clcrdot11bBeaconIntvl.setUnits("hundredths-seconds")
_ClcrApIfConfig_ObjectIdentity = ObjectIdentity
clcrApIfConfig = _ClcrApIfConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 520, 1, 3)
)
_ClcrAPIfTable_Object = MibTable
clcrAPIfTable = _ClcrAPIfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 520, 1, 3, 1)
)
if mibBuilder.loadTexts:
    clcrAPIfTable.setStatus("current")
_ClcrAPIfEntry_Object = MibTableRow
clcrAPIfEntry = _ClcrAPIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 520, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    clcrAPIfEntry.setStatus("current")


class _ClcrAPIfOverrideGlobal_Type(TruthValue):
    """Custom type clcrAPIfOverrideGlobal based on TruthValue"""


_ClcrAPIfOverrideGlobal_Object = MibTableColumn
clcrAPIfOverrideGlobal = _ClcrAPIfOverrideGlobal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 520, 1, 3, 1, 1, 1),
    _ClcrAPIfOverrideGlobal_Type()
)
clcrAPIfOverrideGlobal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clcrAPIfOverrideGlobal.setStatus("current")


class _ClcrAPIfBeaconEnabled_Type(TruthValue):
    """Custom type clcrAPIfBeaconEnabled based on TruthValue"""


_ClcrAPIfBeaconEnabled_Object = MibTableColumn
clcrAPIfBeaconEnabled = _ClcrAPIfBeaconEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 520, 1, 3, 1, 1, 2),
    _ClcrAPIfBeaconEnabled_Type()
)
clcrAPIfBeaconEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clcrAPIfBeaconEnabled.setStatus("current")


class _ClcrAPIfBeaconInterval_Type(TimeInterval):
    """Custom type clcrAPIfBeaconInterval based on TimeInterval"""
    defaultValue = 6000

    subtypeSpec = TimeInterval.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6000, 3240000),
    )


_ClcrAPIfBeaconInterval_Type.__name__ = "TimeInterval"
_ClcrAPIfBeaconInterval_Object = MibTableColumn
clcrAPIfBeaconInterval = _ClcrAPIfBeaconInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 520, 1, 3, 1, 1, 3),
    _ClcrAPIfBeaconInterval_Type()
)
clcrAPIfBeaconInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clcrAPIfBeaconInterval.setStatus("deprecated")
if mibBuilder.loadTexts:
    clcrAPIfBeaconInterval.setUnits("hundredths-seconds")
_ClcrAPIfBeaconIntvl_Type = TimeInterval
_ClcrAPIfBeaconIntvl_Object = MibTableColumn
clcrAPIfBeaconIntvl = _ClcrAPIfBeaconIntvl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 520, 1, 3, 1, 1, 4),
    _ClcrAPIfBeaconIntvl_Type()
)
clcrAPIfBeaconIntvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clcrAPIfBeaconIntvl.setStatus("current")
if mibBuilder.loadTexts:
    clcrAPIfBeaconIntvl.setUnits("hundredths-seconds")
_ClcrClientMeasurementReport_ObjectIdentity = ObjectIdentity
clcrClientMeasurementReport = _ClcrClientMeasurementReport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 520, 1, 4)
)
_ClcrClientBeaconReportTable_Object = MibTable
clcrClientBeaconReportTable = _ClcrClientBeaconReportTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 520, 1, 4, 1)
)
if mibBuilder.loadTexts:
    clcrClientBeaconReportTable.setStatus("current")
_ClcrClientBeaconReportEntry_Object = MibTableRow
clcrClientBeaconReportEntry = _ClcrClientBeaconReportEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 520, 1, 4, 1, 1)
)
clcrClientBeaconReportEntry.setIndexNames(
    (0, "CISCO-LWAPP-CCX-RM-MIB", "clcrClientMacAddress"),
    (0, "CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"),
    (0, "CISCO-LWAPP-AP-MIB", "cLApDot11IfSlotId"),
)
if mibBuilder.loadTexts:
    clcrClientBeaconReportEntry.setStatus("current")
_ClcrClientMacAddress_Type = MacAddress
_ClcrClientMacAddress_Object = MibTableColumn
clcrClientMacAddress = _ClcrClientMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 520, 1, 4, 1, 1, 1),
    _ClcrClientMacAddress_Type()
)
clcrClientMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clcrClientMacAddress.setStatus("current")


class _ClcrClientRxPowerSignal_Type(Integer32):
    """Custom type clcrClientRxPowerSignal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-90, 30),
    )


_ClcrClientRxPowerSignal_Type.__name__ = "Integer32"
_ClcrClientRxPowerSignal_Object = MibTableColumn
clcrClientRxPowerSignal = _ClcrClientRxPowerSignal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 520, 1, 4, 1, 1, 2),
    _ClcrClientRxPowerSignal_Type()
)
clcrClientRxPowerSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clcrClientRxPowerSignal.setStatus("current")
if mibBuilder.loadTexts:
    clcrClientRxPowerSignal.setUnits("dBm")
_ClcrClientTimeStamp_Type = TimeStamp
_ClcrClientTimeStamp_Object = MibTableColumn
clcrClientTimeStamp = _ClcrClientTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 520, 1, 4, 1, 1, 3),
    _ClcrClientTimeStamp_Type()
)
clcrClientTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clcrClientTimeStamp.setStatus("current")
_ClcrWlanConfig_ObjectIdentity = ObjectIdentity
clcrWlanConfig = _ClcrWlanConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 520, 1, 5)
)
_ClcrWlanTable_Object = MibTable
clcrWlanTable = _ClcrWlanTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 520, 1, 5, 1)
)
if mibBuilder.loadTexts:
    clcrWlanTable.setStatus("current")
_ClcrWlanEntry_Object = MibTableRow
clcrWlanEntry = _ClcrWlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 520, 1, 5, 1, 1)
)
if mibBuilder.loadTexts:
    clcrWlanEntry.setStatus("current")
_ClcrVersionIESupport_Type = TruthValue
_ClcrVersionIESupport_Object = MibTableColumn
clcrVersionIESupport = _ClcrVersionIESupport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 520, 1, 5, 1, 1, 1),
    _ClcrVersionIESupport_Type()
)
clcrVersionIESupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clcrVersionIESupport.setStatus("current")


class _ClcrAironetIESupport_Type(TruthValue):
    """Custom type clcrAironetIESupport based on TruthValue"""


_ClcrAironetIESupport_Object = MibTableColumn
clcrAironetIESupport = _ClcrAironetIESupport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 520, 1, 5, 1, 1, 2),
    _ClcrAironetIESupport_Type()
)
clcrAironetIESupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clcrAironetIESupport.setStatus("current")
_CiscoLwappCcxRmMIBConform_ObjectIdentity = ObjectIdentity
ciscoLwappCcxRmMIBConform = _CiscoLwappCcxRmMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 520, 2)
)
_CiscoLwappCcxRmMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoLwappCcxRmMIBCompliances = _CiscoLwappCcxRmMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 520, 2, 1)
)
_CiscoLwappCcxRmMIBGroups_ObjectIdentity = ObjectIdentity
ciscoLwappCcxRmMIBGroups = _CiscoLwappCcxRmMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 520, 2, 2)
)
cLApDot11IfEntry.registerAugmentions(
    ("CISCO-LWAPP-CCX-RM-MIB",
     "clcrAPIfEntry")
)
clcrAPIfEntry.setIndexNames(*cLApDot11IfEntry.getIndexNames())
cLWlanConfigEntry.registerAugmentions(
    ("CISCO-LWAPP-CCX-RM-MIB",
     "clcrWlanEntry")
)
clcrWlanEntry.setIndexNames(*cLWlanConfigEntry.getIndexNames())

# Managed Objects groups

ciscoLwappCcxRmDot11aConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 520, 2, 2, 1)
)
ciscoLwappCcxRmDot11aConfigGroup.setObjects(
      *(("CISCO-LWAPP-CCX-RM-MIB", "clcrdot11aBeaconEnabled"),
        ("CISCO-LWAPP-CCX-RM-MIB", "clcrdot11aBeaconInterval"))
)
if mibBuilder.loadTexts:
    ciscoLwappCcxRmDot11aConfigGroup.setStatus("deprecated")

ciscoLwappCcxRmDot11bConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 520, 2, 2, 2)
)
ciscoLwappCcxRmDot11bConfigGroup.setObjects(
      *(("CISCO-LWAPP-CCX-RM-MIB", "clcrdot11bBeaconEnabled"),
        ("CISCO-LWAPP-CCX-RM-MIB", "clcrdot11bBeaconInterval"))
)
if mibBuilder.loadTexts:
    ciscoLwappCcxRmDot11bConfigGroup.setStatus("deprecated")

ciscoLwappCcxRmApIfConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 520, 2, 2, 3)
)
ciscoLwappCcxRmApIfConfigGroup.setObjects(
      *(("CISCO-LWAPP-CCX-RM-MIB", "clcrAPIfOverrideGlobal"),
        ("CISCO-LWAPP-CCX-RM-MIB", "clcrAPIfBeaconEnabled"),
        ("CISCO-LWAPP-CCX-RM-MIB", "clcrAPIfBeaconInterval"))
)
if mibBuilder.loadTexts:
    ciscoLwappCcxRmApIfConfigGroup.setStatus("deprecated")

ciscoLwappCcxRmBeaconReportGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 520, 2, 2, 4)
)
ciscoLwappCcxRmBeaconReportGroup.setObjects(
      *(("CISCO-LWAPP-CCX-RM-MIB", "clcrClientRxPowerSignal"),
        ("CISCO-LWAPP-CCX-RM-MIB", "clcrClientTimeStamp"))
)
if mibBuilder.loadTexts:
    ciscoLwappCcxRmBeaconReportGroup.setStatus("current")

ciscoLwappCcxRmD11WlanConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 520, 2, 2, 5)
)
ciscoLwappCcxRmD11WlanConfigGroup.setObjects(
      *(("CISCO-LWAPP-CCX-RM-MIB", "clcrVersionIESupport"),
        ("CISCO-LWAPP-CCX-RM-MIB", "clcrAironetIESupport"))
)
if mibBuilder.loadTexts:
    ciscoLwappCcxRmD11WlanConfigGroup.setStatus("current")

ciscoLwappCcxRmDot11aConfigGroupVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 520, 2, 2, 6)
)
ciscoLwappCcxRmDot11aConfigGroupVer1.setObjects(
      *(("CISCO-LWAPP-CCX-RM-MIB", "clcrdot11aBeaconEnabled"),
        ("CISCO-LWAPP-CCX-RM-MIB", "clcrdot11aBeaconIntvl"))
)
if mibBuilder.loadTexts:
    ciscoLwappCcxRmDot11aConfigGroupVer1.setStatus("current")

ciscoLwappCcxRmDot11bConfigGroupVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 520, 2, 2, 7)
)
ciscoLwappCcxRmDot11bConfigGroupVer1.setObjects(
      *(("CISCO-LWAPP-CCX-RM-MIB", "clcrdot11bBeaconEnabled"),
        ("CISCO-LWAPP-CCX-RM-MIB", "clcrdot11bBeaconIntvl"))
)
if mibBuilder.loadTexts:
    ciscoLwappCcxRmDot11bConfigGroupVer1.setStatus("current")

ciscoLwappCcxRmApIfConfigGroupVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 520, 2, 2, 8)
)
ciscoLwappCcxRmApIfConfigGroupVer1.setObjects(
      *(("CISCO-LWAPP-CCX-RM-MIB", "clcrAPIfOverrideGlobal"),
        ("CISCO-LWAPP-CCX-RM-MIB", "clcrAPIfBeaconEnabled"),
        ("CISCO-LWAPP-CCX-RM-MIB", "clcrAPIfBeaconIntvl"))
)
if mibBuilder.loadTexts:
    ciscoLwappCcxRmApIfConfigGroupVer1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoLwappCcxRmMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 520, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoLwappCcxRmMIBCompliance.setStatus(
        "deprecated"
    )

ciscoLwappCcxRmMIBComplianceVer1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 520, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoLwappCcxRmMIBComplianceVer1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-LWAPP-CCX-RM-MIB",
    **{"ciscoLwappCcxRmMIB": ciscoLwappCcxRmMIB,
       "ciscoLwappCcxRmMIBNotifs": ciscoLwappCcxRmMIBNotifs,
       "ciscoLwappCcxRmMIBObjects": ciscoLwappCcxRmMIBObjects,
       "clcrDot11aConfigGlobal": clcrDot11aConfigGlobal,
       "clcrdot11aBeaconEnabled": clcrdot11aBeaconEnabled,
       "clcrdot11aBeaconInterval": clcrdot11aBeaconInterval,
       "clcrdot11aBeaconIntvl": clcrdot11aBeaconIntvl,
       "clcrDot11bConfigGlobal": clcrDot11bConfigGlobal,
       "clcrdot11bBeaconEnabled": clcrdot11bBeaconEnabled,
       "clcrdot11bBeaconInterval": clcrdot11bBeaconInterval,
       "clcrdot11bBeaconIntvl": clcrdot11bBeaconIntvl,
       "clcrApIfConfig": clcrApIfConfig,
       "clcrAPIfTable": clcrAPIfTable,
       "clcrAPIfEntry": clcrAPIfEntry,
       "clcrAPIfOverrideGlobal": clcrAPIfOverrideGlobal,
       "clcrAPIfBeaconEnabled": clcrAPIfBeaconEnabled,
       "clcrAPIfBeaconInterval": clcrAPIfBeaconInterval,
       "clcrAPIfBeaconIntvl": clcrAPIfBeaconIntvl,
       "clcrClientMeasurementReport": clcrClientMeasurementReport,
       "clcrClientBeaconReportTable": clcrClientBeaconReportTable,
       "clcrClientBeaconReportEntry": clcrClientBeaconReportEntry,
       "clcrClientMacAddress": clcrClientMacAddress,
       "clcrClientRxPowerSignal": clcrClientRxPowerSignal,
       "clcrClientTimeStamp": clcrClientTimeStamp,
       "clcrWlanConfig": clcrWlanConfig,
       "clcrWlanTable": clcrWlanTable,
       "clcrWlanEntry": clcrWlanEntry,
       "clcrVersionIESupport": clcrVersionIESupport,
       "clcrAironetIESupport": clcrAironetIESupport,
       "ciscoLwappCcxRmMIBConform": ciscoLwappCcxRmMIBConform,
       "ciscoLwappCcxRmMIBCompliances": ciscoLwappCcxRmMIBCompliances,
       "ciscoLwappCcxRmMIBCompliance": ciscoLwappCcxRmMIBCompliance,
       "ciscoLwappCcxRmMIBComplianceVer1": ciscoLwappCcxRmMIBComplianceVer1,
       "ciscoLwappCcxRmMIBGroups": ciscoLwappCcxRmMIBGroups,
       "ciscoLwappCcxRmDot11aConfigGroup": ciscoLwappCcxRmDot11aConfigGroup,
       "ciscoLwappCcxRmDot11bConfigGroup": ciscoLwappCcxRmDot11bConfigGroup,
       "ciscoLwappCcxRmApIfConfigGroup": ciscoLwappCcxRmApIfConfigGroup,
       "ciscoLwappCcxRmBeaconReportGroup": ciscoLwappCcxRmBeaconReportGroup,
       "ciscoLwappCcxRmD11WlanConfigGroup": ciscoLwappCcxRmD11WlanConfigGroup,
       "ciscoLwappCcxRmDot11aConfigGroupVer1": ciscoLwappCcxRmDot11aConfigGroupVer1,
       "ciscoLwappCcxRmDot11bConfigGroupVer1": ciscoLwappCcxRmDot11bConfigGroupVer1,
       "ciscoLwappCcxRmApIfConfigGroupVer1": ciscoLwappCcxRmApIfConfigGroupVer1}
)
