# SNMP MIB module (CISCO-SERVICE-CONTROLLER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-SERVICE-CONTROLLER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:08:10 2024
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

(entPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
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

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

ciscoServiceControllerMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 667)
)
ciscoServiceControllerMIB.setRevisions(
        ("2011-03-03 00:00",
         "2008-08-04 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoServiceControlMIBObjects_ObjectIdentity = ObjectIdentity
ciscoServiceControlMIBObjects = _CiscoServiceControlMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 667, 0)
)
_CscGlobalControllersTable_Object = MibTable
cscGlobalControllersTable = _CscGlobalControllersTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 667, 0, 1)
)
if mibBuilder.loadTexts:
    cscGlobalControllersTable.setStatus("current")
_CscGlobalControllersEntry_Object = MibTableRow
cscGlobalControllersEntry = _CscGlobalControllersEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 667, 0, 1, 1)
)
cscGlobalControllersEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-SERVICE-CONTROLLER-MIB", "cscGlobalControllersIndex"),
)
if mibBuilder.loadTexts:
    cscGlobalControllersEntry.setStatus("current")


class _CscGlobalControllersIndex_Type(Unsigned32):
    """Custom type cscGlobalControllersIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CscGlobalControllersIndex_Type.__name__ = "Unsigned32"
_CscGlobalControllersIndex_Object = MibTableColumn
cscGlobalControllersIndex = _CscGlobalControllersIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 667, 0, 1, 1, 1),
    _CscGlobalControllersIndex_Type()
)
cscGlobalControllersIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cscGlobalControllersIndex.setStatus("current")
_CscGlobalControllersId_Type = Unsigned32
_CscGlobalControllersId_Object = MibTableColumn
cscGlobalControllersId = _CscGlobalControllersId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 667, 0, 1, 1, 2),
    _CscGlobalControllersId_Type()
)
cscGlobalControllersId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cscGlobalControllersId.setStatus("current")


class _CscGlobalControllersDescription_Type(SnmpAdminString):
    """Custom type cscGlobalControllersDescription based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CscGlobalControllersDescription_Type.__name__ = "SnmpAdminString"
_CscGlobalControllersDescription_Object = MibTableColumn
cscGlobalControllersDescription = _CscGlobalControllersDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 667, 0, 1, 1, 3),
    _CscGlobalControllersDescription_Type()
)
cscGlobalControllersDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cscGlobalControllersDescription.setStatus("current")


class _CscGlobalControllersBandwidthUnits_Type(Integer32):
    """Custom type cscGlobalControllersBandwidthUnits based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("kbps", 1),
          ("mbps", 2))
    )


_CscGlobalControllersBandwidthUnits_Type.__name__ = "Integer32"
_CscGlobalControllersBandwidthUnits_Object = MibTableColumn
cscGlobalControllersBandwidthUnits = _CscGlobalControllersBandwidthUnits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 667, 0, 1, 1, 4),
    _CscGlobalControllersBandwidthUnits_Type()
)
cscGlobalControllersBandwidthUnits.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cscGlobalControllersBandwidthUnits.setStatus("current")


class _CscGlobalControllersBandwidth_Type(Unsigned32):
    """Custom type cscGlobalControllersBandwidth based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CscGlobalControllersBandwidth_Type.__name__ = "Unsigned32"
_CscGlobalControllersBandwidth_Object = MibTableColumn
cscGlobalControllersBandwidth = _CscGlobalControllersBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 667, 0, 1, 1, 5),
    _CscGlobalControllersBandwidth_Type()
)
cscGlobalControllersBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cscGlobalControllersBandwidth.setStatus("current")


class _CscGlobalControllersUtilization_Type(Unsigned32):
    """Custom type cscGlobalControllersUtilization based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CscGlobalControllersUtilization_Type.__name__ = "Unsigned32"
_CscGlobalControllersUtilization_Object = MibTableColumn
cscGlobalControllersUtilization = _CscGlobalControllersUtilization_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 667, 0, 1, 1, 6),
    _CscGlobalControllersUtilization_Type()
)
cscGlobalControllersUtilization.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cscGlobalControllersUtilization.setStatus("current")
if mibBuilder.loadTexts:
    cscGlobalControllersUtilization.setUnits("percent")
_CscAggregativeGlobalControllersTable_Object = MibTable
cscAggregativeGlobalControllersTable = _CscAggregativeGlobalControllersTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 667, 0, 2)
)
if mibBuilder.loadTexts:
    cscAggregativeGlobalControllersTable.setStatus("current")
_CscAggregativeGlobalControllersEntry_Object = MibTableRow
cscAggregativeGlobalControllersEntry = _CscAggregativeGlobalControllersEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 667, 0, 2, 1)
)
cscAggregativeGlobalControllersEntry.setIndexNames(
    (0, "CISCO-SERVICE-CONTROLLER-MIB", "cscAggregativeGlobalControllersSide"),
    (0, "CISCO-SERVICE-CONTROLLER-MIB", "cscAggregativeGlobalControllersAgcId"),
)
if mibBuilder.loadTexts:
    cscAggregativeGlobalControllersEntry.setStatus("current")


class _CscAggregativeGlobalControllersSide_Type(Integer32):
    """Custom type cscAggregativeGlobalControllersSide based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("network", 2),
          ("subscriber", 1))
    )


_CscAggregativeGlobalControllersSide_Type.__name__ = "Integer32"
_CscAggregativeGlobalControllersSide_Object = MibTableColumn
cscAggregativeGlobalControllersSide = _CscAggregativeGlobalControllersSide_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 667, 0, 2, 1, 1),
    _CscAggregativeGlobalControllersSide_Type()
)
cscAggregativeGlobalControllersSide.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cscAggregativeGlobalControllersSide.setStatus("current")


class _CscAggregativeGlobalControllersAgcId_Type(Unsigned32):
    """Custom type cscAggregativeGlobalControllersAgcId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_CscAggregativeGlobalControllersAgcId_Type.__name__ = "Unsigned32"
_CscAggregativeGlobalControllersAgcId_Object = MibTableColumn
cscAggregativeGlobalControllersAgcId = _CscAggregativeGlobalControllersAgcId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 667, 0, 2, 1, 2),
    _CscAggregativeGlobalControllersAgcId_Type()
)
cscAggregativeGlobalControllersAgcId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cscAggregativeGlobalControllersAgcId.setStatus("current")
_CscAggregativeGlobalControllersLimit_Type = Gauge32
_CscAggregativeGlobalControllersLimit_Object = MibTableColumn
cscAggregativeGlobalControllersLimit = _CscAggregativeGlobalControllersLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 667, 0, 2, 1, 3),
    _CscAggregativeGlobalControllersLimit_Type()
)
cscAggregativeGlobalControllersLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cscAggregativeGlobalControllersLimit.setStatus("current")
if mibBuilder.loadTexts:
    cscAggregativeGlobalControllersLimit.setUnits("kbps")
_CscAggregativeGlobalControllersRate_Type = Gauge32
_CscAggregativeGlobalControllersRate_Object = MibTableColumn
cscAggregativeGlobalControllersRate = _CscAggregativeGlobalControllersRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 667, 0, 2, 1, 4),
    _CscAggregativeGlobalControllersRate_Type()
)
cscAggregativeGlobalControllersRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cscAggregativeGlobalControllersRate.setStatus("current")
if mibBuilder.loadTexts:
    cscAggregativeGlobalControllersRate.setUnits("kbps")
_CscAggregativeGlobalControllersLinkTable_Object = MibTable
cscAggregativeGlobalControllersLinkTable = _CscAggregativeGlobalControllersLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 667, 0, 3)
)
if mibBuilder.loadTexts:
    cscAggregativeGlobalControllersLinkTable.setStatus("current")
_CscAggregativeGlobalControllersLinkEntry_Object = MibTableRow
cscAggregativeGlobalControllersLinkEntry = _CscAggregativeGlobalControllersLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 667, 0, 3, 1)
)
cscAggregativeGlobalControllersLinkEntry.setIndexNames(
    (0, "CISCO-SERVICE-CONTROLLER-MIB", "cscAggregativeGlobalControllersLinkIndex"),
    (0, "CISCO-SERVICE-CONTROLLER-MIB", "cscAggregativeGlobalControllersLinkSide"),
    (0, "CISCO-SERVICE-CONTROLLER-MIB", "cscAggregativeGlobalControllersLinkAgcId"),
)
if mibBuilder.loadTexts:
    cscAggregativeGlobalControllersLinkEntry.setStatus("current")


class _CscAggregativeGlobalControllersLinkIndex_Type(Unsigned32):
    """Custom type cscAggregativeGlobalControllersLinkIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CscAggregativeGlobalControllersLinkIndex_Type.__name__ = "Unsigned32"
_CscAggregativeGlobalControllersLinkIndex_Object = MibTableColumn
cscAggregativeGlobalControllersLinkIndex = _CscAggregativeGlobalControllersLinkIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 667, 0, 3, 1, 1),
    _CscAggregativeGlobalControllersLinkIndex_Type()
)
cscAggregativeGlobalControllersLinkIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cscAggregativeGlobalControllersLinkIndex.setStatus("current")


class _CscAggregativeGlobalControllersLinkSide_Type(Integer32):
    """Custom type cscAggregativeGlobalControllersLinkSide based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("network", 2),
          ("subscriber", 1))
    )


_CscAggregativeGlobalControllersLinkSide_Type.__name__ = "Integer32"
_CscAggregativeGlobalControllersLinkSide_Object = MibTableColumn
cscAggregativeGlobalControllersLinkSide = _CscAggregativeGlobalControllersLinkSide_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 667, 0, 3, 1, 2),
    _CscAggregativeGlobalControllersLinkSide_Type()
)
cscAggregativeGlobalControllersLinkSide.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cscAggregativeGlobalControllersLinkSide.setStatus("current")


class _CscAggregativeGlobalControllersLinkAgcId_Type(Unsigned32):
    """Custom type cscAggregativeGlobalControllersLinkAgcId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_CscAggregativeGlobalControllersLinkAgcId_Type.__name__ = "Unsigned32"
_CscAggregativeGlobalControllersLinkAgcId_Object = MibTableColumn
cscAggregativeGlobalControllersLinkAgcId = _CscAggregativeGlobalControllersLinkAgcId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 667, 0, 3, 1, 3),
    _CscAggregativeGlobalControllersLinkAgcId_Type()
)
cscAggregativeGlobalControllersLinkAgcId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cscAggregativeGlobalControllersLinkAgcId.setStatus("current")
_CscAggregativeGlobalControllersLinkEnforcedRate_Type = Gauge32
_CscAggregativeGlobalControllersLinkEnforcedRate_Object = MibTableColumn
cscAggregativeGlobalControllersLinkEnforcedRate = _CscAggregativeGlobalControllersLinkEnforcedRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 667, 0, 3, 1, 4),
    _CscAggregativeGlobalControllersLinkEnforcedRate_Type()
)
cscAggregativeGlobalControllersLinkEnforcedRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cscAggregativeGlobalControllersLinkEnforcedRate.setStatus("current")
if mibBuilder.loadTexts:
    cscAggregativeGlobalControllersLinkEnforcedRate.setUnits("kbps")
_CscAggregativeGlobalControllersCommittedInformationRate_Type = Gauge32
_CscAggregativeGlobalControllersCommittedInformationRate_Object = MibTableColumn
cscAggregativeGlobalControllersCommittedInformationRate = _CscAggregativeGlobalControllersCommittedInformationRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 667, 0, 3, 1, 5),
    _CscAggregativeGlobalControllersCommittedInformationRate_Type()
)
cscAggregativeGlobalControllersCommittedInformationRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cscAggregativeGlobalControllersCommittedInformationRate.setStatus("current")
if mibBuilder.loadTexts:
    cscAggregativeGlobalControllersCommittedInformationRate.setUnits("kbps")
_CscAggregativeGlobalControllersPeakInformationRate_Type = Gauge32
_CscAggregativeGlobalControllersPeakInformationRate_Object = MibTableColumn
cscAggregativeGlobalControllersPeakInformationRate = _CscAggregativeGlobalControllersPeakInformationRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 667, 0, 3, 1, 6),
    _CscAggregativeGlobalControllersPeakInformationRate_Type()
)
cscAggregativeGlobalControllersPeakInformationRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cscAggregativeGlobalControllersPeakInformationRate.setStatus("current")
if mibBuilder.loadTexts:
    cscAggregativeGlobalControllersPeakInformationRate.setUnits("kbps")


class _CscAggregativeGlobalControllersAssuranceLevel_Type(Unsigned32):
    """Custom type cscAggregativeGlobalControllersAssuranceLevel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_CscAggregativeGlobalControllersAssuranceLevel_Type.__name__ = "Unsigned32"
_CscAggregativeGlobalControllersAssuranceLevel_Object = MibTableColumn
cscAggregativeGlobalControllersAssuranceLevel = _CscAggregativeGlobalControllersAssuranceLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 667, 0, 3, 1, 7),
    _CscAggregativeGlobalControllersAssuranceLevel_Type()
)
cscAggregativeGlobalControllersAssuranceLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cscAggregativeGlobalControllersAssuranceLevel.setStatus("current")
_CiscoServiceControlMIBConform_ObjectIdentity = ObjectIdentity
ciscoServiceControlMIBConform = _CiscoServiceControlMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 667, 1)
)
_CiscoServiceControlMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoServiceControlMIBCompliances = _CiscoServiceControlMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 667, 1, 1)
)
_CiscoServiceControlMIBObjectGroups_ObjectIdentity = ObjectIdentity
ciscoServiceControlMIBObjectGroups = _CiscoServiceControlMIBObjectGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 667, 1, 2)
)

# Managed Objects groups

ciscoServiceControlMIBGlobalControllersObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 667, 1, 2, 1)
)
ciscoServiceControlMIBGlobalControllersObjectGroup.setObjects(
      *(("CISCO-SERVICE-CONTROLLER-MIB", "cscGlobalControllersDescription"),
        ("CISCO-SERVICE-CONTROLLER-MIB", "cscGlobalControllersBandwidth"),
        ("CISCO-SERVICE-CONTROLLER-MIB", "cscGlobalControllersUtilization"),
        ("CISCO-SERVICE-CONTROLLER-MIB", "cscGlobalControllersBandwidthUnits"),
        ("CISCO-SERVICE-CONTROLLER-MIB", "cscGlobalControllersId"))
)
if mibBuilder.loadTexts:
    ciscoServiceControlMIBGlobalControllersObjectGroup.setStatus("current")

ciscoServiceControlAGCMIBObjectGroups = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 667, 1, 2, 2)
)
ciscoServiceControlAGCMIBObjectGroups.setObjects(
      *(("CISCO-SERVICE-CONTROLLER-MIB", "cscAggregativeGlobalControllersLimit"),
        ("CISCO-SERVICE-CONTROLLER-MIB", "cscAggregativeGlobalControllersRate"),
        ("CISCO-SERVICE-CONTROLLER-MIB", "cscAggregativeGlobalControllersLinkEnforcedRate"),
        ("CISCO-SERVICE-CONTROLLER-MIB", "cscAggregativeGlobalControllersPeakInformationRate"),
        ("CISCO-SERVICE-CONTROLLER-MIB", "cscAggregativeGlobalControllersCommittedInformationRate"),
        ("CISCO-SERVICE-CONTROLLER-MIB", "cscAggregativeGlobalControllersAssuranceLevel"))
)
if mibBuilder.loadTexts:
    ciscoServiceControlAGCMIBObjectGroups.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoServiceControlMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 667, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoServiceControlMIBCompliance.setStatus(
        "deprecated"
    )

ciscoServiceControlMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 667, 1, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoServiceControlMIBComplianceRev1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-SERVICE-CONTROLLER-MIB",
    **{"ciscoServiceControllerMIB": ciscoServiceControllerMIB,
       "ciscoServiceControlMIBObjects": ciscoServiceControlMIBObjects,
       "cscGlobalControllersTable": cscGlobalControllersTable,
       "cscGlobalControllersEntry": cscGlobalControllersEntry,
       "cscGlobalControllersIndex": cscGlobalControllersIndex,
       "cscGlobalControllersId": cscGlobalControllersId,
       "cscGlobalControllersDescription": cscGlobalControllersDescription,
       "cscGlobalControllersBandwidthUnits": cscGlobalControllersBandwidthUnits,
       "cscGlobalControllersBandwidth": cscGlobalControllersBandwidth,
       "cscGlobalControllersUtilization": cscGlobalControllersUtilization,
       "cscAggregativeGlobalControllersTable": cscAggregativeGlobalControllersTable,
       "cscAggregativeGlobalControllersEntry": cscAggregativeGlobalControllersEntry,
       "cscAggregativeGlobalControllersSide": cscAggregativeGlobalControllersSide,
       "cscAggregativeGlobalControllersAgcId": cscAggregativeGlobalControllersAgcId,
       "cscAggregativeGlobalControllersLimit": cscAggregativeGlobalControllersLimit,
       "cscAggregativeGlobalControllersRate": cscAggregativeGlobalControllersRate,
       "cscAggregativeGlobalControllersLinkTable": cscAggregativeGlobalControllersLinkTable,
       "cscAggregativeGlobalControllersLinkEntry": cscAggregativeGlobalControllersLinkEntry,
       "cscAggregativeGlobalControllersLinkIndex": cscAggregativeGlobalControllersLinkIndex,
       "cscAggregativeGlobalControllersLinkSide": cscAggregativeGlobalControllersLinkSide,
       "cscAggregativeGlobalControllersLinkAgcId": cscAggregativeGlobalControllersLinkAgcId,
       "cscAggregativeGlobalControllersLinkEnforcedRate": cscAggregativeGlobalControllersLinkEnforcedRate,
       "cscAggregativeGlobalControllersCommittedInformationRate": cscAggregativeGlobalControllersCommittedInformationRate,
       "cscAggregativeGlobalControllersPeakInformationRate": cscAggregativeGlobalControllersPeakInformationRate,
       "cscAggregativeGlobalControllersAssuranceLevel": cscAggregativeGlobalControllersAssuranceLevel,
       "ciscoServiceControlMIBConform": ciscoServiceControlMIBConform,
       "ciscoServiceControlMIBCompliances": ciscoServiceControlMIBCompliances,
       "ciscoServiceControlMIBCompliance": ciscoServiceControlMIBCompliance,
       "ciscoServiceControlMIBComplianceRev1": ciscoServiceControlMIBComplianceRev1,
       "ciscoServiceControlMIBObjectGroups": ciscoServiceControlMIBObjectGroups,
       "ciscoServiceControlMIBGlobalControllersObjectGroup": ciscoServiceControlMIBGlobalControllersObjectGroup,
       "ciscoServiceControlAGCMIBObjectGroups": ciscoServiceControlAGCMIBObjectGroups}
)
