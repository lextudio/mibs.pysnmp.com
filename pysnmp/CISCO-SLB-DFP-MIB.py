# SNMP MIB module (CISCO-SLB-DFP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-SLB-DFP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:08:20 2024
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

ciscoSlbDfpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 689)
)
ciscoSlbDfpMIB.setRevisions(
        ("2009-01-29 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CslbcDfpValue(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



# MIB Managed Objects in the order of their OIDs

_CiscoSlbDfpMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoSlbDfpMIBNotifs = _CiscoSlbDfpMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 689, 0)
)
_CiscoSlbDfpMIBObjects_ObjectIdentity = ObjectIdentity
ciscoSlbDfpMIBObjects = _CiscoSlbDfpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 689, 1)
)


class _CslbcDfpCongestionOnsetThreshold_Type(CslbcDfpValue):
    """Custom type cslbcDfpCongestionOnsetThreshold based on CslbcDfpValue"""
    defaultValue = 0


_CslbcDfpCongestionOnsetThreshold_Object = MibScalar
cslbcDfpCongestionOnsetThreshold = _CslbcDfpCongestionOnsetThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 689, 1, 1),
    _CslbcDfpCongestionOnsetThreshold_Type()
)
cslbcDfpCongestionOnsetThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cslbcDfpCongestionOnsetThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cslbcDfpCongestionOnsetThreshold.setUnits("DFP weight")


class _CslbcDfpCongestionAbateThreshold_Type(CslbcDfpValue):
    """Custom type cslbcDfpCongestionAbateThreshold based on CslbcDfpValue"""
    defaultValue = 0


_CslbcDfpCongestionAbateThreshold_Object = MibScalar
cslbcDfpCongestionAbateThreshold = _CslbcDfpCongestionAbateThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 689, 1, 2),
    _CslbcDfpCongestionAbateThreshold_Type()
)
cslbcDfpCongestionAbateThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cslbcDfpCongestionAbateThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cslbcDfpCongestionAbateThreshold.setUnits("DFP weight")


class _CslbcDfpCongestionThresholdType_Type(Integer32):
    """Custom type cslbcDfpCongestionThresholdType based on Integer32"""
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
        *(("abort", 2),
          ("drop", 4),
          ("redirect", 3),
          ("reject", 1))
    )


_CslbcDfpCongestionThresholdType_Type.__name__ = "Integer32"
_CslbcDfpCongestionThresholdType_Object = MibScalar
cslbcDfpCongestionThresholdType = _CslbcDfpCongestionThresholdType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 689, 1, 3),
    _CslbcDfpCongestionThresholdType_Type()
)
cslbcDfpCongestionThresholdType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cslbcDfpCongestionThresholdType.setStatus("current")
_CslbcProcessorDfpValTable_Object = MibTable
cslbcProcessorDfpValTable = _CslbcProcessorDfpValTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 689, 1, 4)
)
if mibBuilder.loadTexts:
    cslbcProcessorDfpValTable.setStatus("current")
_CslbcProcessorDfpValEntry_Object = MibTableRow
cslbcProcessorDfpValEntry = _CslbcProcessorDfpValEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 689, 1, 4, 1)
)
cslbcProcessorDfpValEntry.setIndexNames(
    (0, "CISCO-SLB-DFP-MIB", "cslbcProcessorDfpValPhysicalIndex"),
)
if mibBuilder.loadTexts:
    cslbcProcessorDfpValEntry.setStatus("current")
_CslbcProcessorDfpValPhysicalIndex_Type = EntPhysicalIndexOrZero
_CslbcProcessorDfpValPhysicalIndex_Object = MibTableColumn
cslbcProcessorDfpValPhysicalIndex = _CslbcProcessorDfpValPhysicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 689, 1, 4, 1, 1),
    _CslbcProcessorDfpValPhysicalIndex_Type()
)
cslbcProcessorDfpValPhysicalIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cslbcProcessorDfpValPhysicalIndex.setStatus("current")
_CslbcProcessorDfpValDescription_Type = SnmpAdminString
_CslbcProcessorDfpValDescription_Object = MibTableColumn
cslbcProcessorDfpValDescription = _CslbcProcessorDfpValDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 689, 1, 4, 1, 2),
    _CslbcProcessorDfpValDescription_Type()
)
cslbcProcessorDfpValDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cslbcProcessorDfpValDescription.setStatus("current")
_CslbcProcessorDfpValDfpValue_Type = CslbcDfpValue
_CslbcProcessorDfpValDfpValue_Object = MibTableColumn
cslbcProcessorDfpValDfpValue = _CslbcProcessorDfpValDfpValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 689, 1, 4, 1, 3),
    _CslbcProcessorDfpValDfpValue_Type()
)
cslbcProcessorDfpValDfpValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cslbcProcessorDfpValDfpValue.setStatus("current")
_CiscoSlbDfpMIBConform_ObjectIdentity = ObjectIdentity
ciscoSlbDfpMIBConform = _CiscoSlbDfpMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 689, 2)
)
_CiscoSlbDfpMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoSlbDfpMIBCompliances = _CiscoSlbDfpMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 689, 2, 1)
)
_CiscoSlbDfpMIBGroups_ObjectIdentity = ObjectIdentity
ciscoSlbDfpMIBGroups = _CiscoSlbDfpMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 689, 2, 2)
)

# Managed Objects groups

ciscoSlbDfpInstanceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 689, 2, 2, 1)
)
ciscoSlbDfpInstanceGroup.setObjects(
      *(("CISCO-SLB-DFP-MIB", "cslbcProcessorDfpValDescription"),
        ("CISCO-SLB-DFP-MIB", "cslbcProcessorDfpValDfpValue"))
)
if mibBuilder.loadTexts:
    ciscoSlbDfpInstanceGroup.setStatus("current")

cslbcSlbDfpScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 689, 2, 2, 2)
)
cslbcSlbDfpScalarsGroup.setObjects(
      *(("CISCO-SLB-DFP-MIB", "cslbcDfpCongestionOnsetThreshold"),
        ("CISCO-SLB-DFP-MIB", "cslbcDfpCongestionAbateThreshold"),
        ("CISCO-SLB-DFP-MIB", "cslbcDfpCongestionThresholdType"))
)
if mibBuilder.loadTexts:
    cslbcSlbDfpScalarsGroup.setStatus("current")


# Notification objects

cslbcSlbDfpCongestionOnset = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 689, 0, 1)
)
cslbcSlbDfpCongestionOnset.setObjects(
      *(("CISCO-SLB-DFP-MIB", "cslbcProcessorDfpValDescription"),
        ("CISCO-SLB-DFP-MIB", "cslbcProcessorDfpValDfpValue"),
        ("CISCO-SLB-DFP-MIB", "cslbcDfpCongestionThresholdType"),
        ("CISCO-SLB-DFP-MIB", "cslbcDfpCongestionOnsetThreshold"))
)
if mibBuilder.loadTexts:
    cslbcSlbDfpCongestionOnset.setStatus(
        "current"
    )

cslbcSlbDfpCongestionAbate = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 689, 0, 2)
)
cslbcSlbDfpCongestionAbate.setObjects(
      *(("CISCO-SLB-DFP-MIB", "cslbcProcessorDfpValDescription"),
        ("CISCO-SLB-DFP-MIB", "cslbcProcessorDfpValDfpValue"),
        ("CISCO-SLB-DFP-MIB", "cslbcDfpCongestionAbateThreshold"),
        ("CISCO-SLB-DFP-MIB", "cslbcDfpCongestionThresholdType"))
)
if mibBuilder.loadTexts:
    cslbcSlbDfpCongestionAbate.setStatus(
        "current"
    )


# Notifications groups

cslbcSlbDfpCongestionGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 689, 2, 2, 3)
)
cslbcSlbDfpCongestionGroup.setObjects(
      *(("CISCO-SLB-DFP-MIB", "cslbcSlbDfpCongestionOnset"),
        ("CISCO-SLB-DFP-MIB", "cslbcSlbDfpCongestionAbate"))
)
if mibBuilder.loadTexts:
    cslbcSlbDfpCongestionGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoSlbDfpMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 689, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoSlbDfpMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-SLB-DFP-MIB",
    **{"CslbcDfpValue": CslbcDfpValue,
       "ciscoSlbDfpMIB": ciscoSlbDfpMIB,
       "ciscoSlbDfpMIBNotifs": ciscoSlbDfpMIBNotifs,
       "cslbcSlbDfpCongestionOnset": cslbcSlbDfpCongestionOnset,
       "cslbcSlbDfpCongestionAbate": cslbcSlbDfpCongestionAbate,
       "ciscoSlbDfpMIBObjects": ciscoSlbDfpMIBObjects,
       "cslbcDfpCongestionOnsetThreshold": cslbcDfpCongestionOnsetThreshold,
       "cslbcDfpCongestionAbateThreshold": cslbcDfpCongestionAbateThreshold,
       "cslbcDfpCongestionThresholdType": cslbcDfpCongestionThresholdType,
       "cslbcProcessorDfpValTable": cslbcProcessorDfpValTable,
       "cslbcProcessorDfpValEntry": cslbcProcessorDfpValEntry,
       "cslbcProcessorDfpValPhysicalIndex": cslbcProcessorDfpValPhysicalIndex,
       "cslbcProcessorDfpValDescription": cslbcProcessorDfpValDescription,
       "cslbcProcessorDfpValDfpValue": cslbcProcessorDfpValDfpValue,
       "ciscoSlbDfpMIBConform": ciscoSlbDfpMIBConform,
       "ciscoSlbDfpMIBCompliances": ciscoSlbDfpMIBCompliances,
       "ciscoSlbDfpMIBCompliance": ciscoSlbDfpMIBCompliance,
       "ciscoSlbDfpMIBGroups": ciscoSlbDfpMIBGroups,
       "ciscoSlbDfpInstanceGroup": ciscoSlbDfpInstanceGroup,
       "cslbcSlbDfpScalarsGroup": cslbcSlbDfpScalarsGroup,
       "cslbcSlbDfpCongestionGroup": cslbcSlbDfpCongestionGroup}
)
