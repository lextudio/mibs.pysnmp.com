# SNMP MIB module (HUAWEI-TDM-PSN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-TDM-PSN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:06:13 2024
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

(hwDatacomm,) = mibBuilder.importSymbols(
    "HUAWEI-MIB",
    "hwDatacomm")

(HWL2VpnVcEncapsType,) = mibBuilder.importSymbols(
    "HUAWEI-VPLS-EXT-MIB",
    "HWL2VpnVcEncapsType")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

hwTdmPsnMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 152)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwTdmPsnMIBObjects_ObjectIdentity = ObjectIdentity
hwTdmPsnMIBObjects = _HwTdmPsnMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 152, 1)
)
_HwTdmPsnPerfCurrentTable_Object = MibTable
hwTdmPsnPerfCurrentTable = _HwTdmPsnPerfCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 152, 1, 1)
)
if mibBuilder.loadTexts:
    hwTdmPsnPerfCurrentTable.setStatus("current")
_HwTdmPsnPerfCurrentEntry_Object = MibTableRow
hwTdmPsnPerfCurrentEntry = _HwTdmPsnPerfCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 152, 1, 1, 1)
)
hwTdmPsnPerfCurrentEntry.setIndexNames(
    (0, "HUAWEI-TDM-PSN-MIB", "hwTdmPsnPerfCurrentPwIdIndex"),
    (0, "HUAWEI-TDM-PSN-MIB", "hwTdmPsnPerfCurrentPwTypeIndex"),
)
if mibBuilder.loadTexts:
    hwTdmPsnPerfCurrentEntry.setStatus("current")
_HwTdmPsnPerfCurrentPwIdIndex_Type = Unsigned32
_HwTdmPsnPerfCurrentPwIdIndex_Object = MibTableColumn
hwTdmPsnPerfCurrentPwIdIndex = _HwTdmPsnPerfCurrentPwIdIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 152, 1, 1, 1, 1),
    _HwTdmPsnPerfCurrentPwIdIndex_Type()
)
hwTdmPsnPerfCurrentPwIdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwTdmPsnPerfCurrentPwIdIndex.setStatus("current")
_HwTdmPsnPerfCurrentPwTypeIndex_Type = HWL2VpnVcEncapsType
_HwTdmPsnPerfCurrentPwTypeIndex_Object = MibTableColumn
hwTdmPsnPerfCurrentPwTypeIndex = _HwTdmPsnPerfCurrentPwTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 152, 1, 1, 1, 2),
    _HwTdmPsnPerfCurrentPwTypeIndex_Type()
)
hwTdmPsnPerfCurrentPwTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwTdmPsnPerfCurrentPwTypeIndex.setStatus("current")
_HwTdmPsnPerfCurrentMissingPkts_Type = Gauge32
_HwTdmPsnPerfCurrentMissingPkts_Object = MibTableColumn
hwTdmPsnPerfCurrentMissingPkts = _HwTdmPsnPerfCurrentMissingPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 152, 1, 1, 1, 3),
    _HwTdmPsnPerfCurrentMissingPkts_Type()
)
hwTdmPsnPerfCurrentMissingPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTdmPsnPerfCurrentMissingPkts.setStatus("current")
_HwTdmPsnPerfCurrentPktsReorder_Type = Gauge32
_HwTdmPsnPerfCurrentPktsReorder_Object = MibTableColumn
hwTdmPsnPerfCurrentPktsReorder = _HwTdmPsnPerfCurrentPktsReorder_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 152, 1, 1, 1, 4),
    _HwTdmPsnPerfCurrentPktsReorder_Type()
)
hwTdmPsnPerfCurrentPktsReorder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTdmPsnPerfCurrentPktsReorder.setStatus("current")
_HwTdmPsnPerfCurrentJtrBfrUnderruns_Type = Gauge32
_HwTdmPsnPerfCurrentJtrBfrUnderruns_Object = MibTableColumn
hwTdmPsnPerfCurrentJtrBfrUnderruns = _HwTdmPsnPerfCurrentJtrBfrUnderruns_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 152, 1, 1, 1, 5),
    _HwTdmPsnPerfCurrentJtrBfrUnderruns_Type()
)
hwTdmPsnPerfCurrentJtrBfrUnderruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTdmPsnPerfCurrentJtrBfrUnderruns.setStatus("current")
_HwTdmPsnPerfCurrentMisorderDropped_Type = Gauge32
_HwTdmPsnPerfCurrentMisorderDropped_Object = MibTableColumn
hwTdmPsnPerfCurrentMisorderDropped = _HwTdmPsnPerfCurrentMisorderDropped_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 152, 1, 1, 1, 6),
    _HwTdmPsnPerfCurrentMisorderDropped_Type()
)
hwTdmPsnPerfCurrentMisorderDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTdmPsnPerfCurrentMisorderDropped.setStatus("current")
_HwTdmPsnPerfCurrentMalformedPkts_Type = Gauge32
_HwTdmPsnPerfCurrentMalformedPkts_Object = MibTableColumn
hwTdmPsnPerfCurrentMalformedPkts = _HwTdmPsnPerfCurrentMalformedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 152, 1, 1, 1, 7),
    _HwTdmPsnPerfCurrentMalformedPkts_Type()
)
hwTdmPsnPerfCurrentMalformedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTdmPsnPerfCurrentMalformedPkts.setStatus("current")
_HwTdmPsnPerfCurrentErrorSeconds_Type = Gauge32
_HwTdmPsnPerfCurrentErrorSeconds_Object = MibTableColumn
hwTdmPsnPerfCurrentErrorSeconds = _HwTdmPsnPerfCurrentErrorSeconds_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 152, 1, 1, 1, 8),
    _HwTdmPsnPerfCurrentErrorSeconds_Type()
)
hwTdmPsnPerfCurrentErrorSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTdmPsnPerfCurrentErrorSeconds.setStatus("current")
_HwTdmPsnPerfCurrentSeverelyErrorSeconds_Type = Gauge32
_HwTdmPsnPerfCurrentSeverelyErrorSeconds_Object = MibTableColumn
hwTdmPsnPerfCurrentSeverelyErrorSeconds = _HwTdmPsnPerfCurrentSeverelyErrorSeconds_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 152, 1, 1, 1, 9),
    _HwTdmPsnPerfCurrentSeverelyErrorSeconds_Type()
)
hwTdmPsnPerfCurrentSeverelyErrorSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTdmPsnPerfCurrentSeverelyErrorSeconds.setStatus("current")
_HwTdmPsnPerfCurrentUnavailableSeconds_Type = Gauge32
_HwTdmPsnPerfCurrentUnavailableSeconds_Object = MibTableColumn
hwTdmPsnPerfCurrentUnavailableSeconds = _HwTdmPsnPerfCurrentUnavailableSeconds_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 152, 1, 1, 1, 10),
    _HwTdmPsnPerfCurrentUnavailableSeconds_Type()
)
hwTdmPsnPerfCurrentUnavailableSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTdmPsnPerfCurrentUnavailableSeconds.setStatus("current")
_HwTdmPsnPerfCurrentFailureCounts_Type = Gauge32
_HwTdmPsnPerfCurrentFailureCounts_Object = MibTableColumn
hwTdmPsnPerfCurrentFailureCounts = _HwTdmPsnPerfCurrentFailureCounts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 152, 1, 1, 1, 11),
    _HwTdmPsnPerfCurrentFailureCounts_Type()
)
hwTdmPsnPerfCurrentFailureCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTdmPsnPerfCurrentFailureCounts.setStatus("current")
_HwTdmPsnAlarmTable_Object = MibTable
hwTdmPsnAlarmTable = _HwTdmPsnAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 152, 1, 2)
)
if mibBuilder.loadTexts:
    hwTdmPsnAlarmTable.setStatus("current")
_HwTdmPsnAlarmEntry_Object = MibTableRow
hwTdmPsnAlarmEntry = _HwTdmPsnAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 152, 1, 2, 1)
)
hwTdmPsnAlarmEntry.setIndexNames(
    (0, "HUAWEI-TDM-PSN-MIB", "hwTdmPsnAlarmPwIdIndex"),
    (0, "HUAWEI-TDM-PSN-MIB", "hwTdmPsnAlarmPwTypeIndex"),
)
if mibBuilder.loadTexts:
    hwTdmPsnAlarmEntry.setStatus("current")
_HwTdmPsnAlarmPwIdIndex_Type = Unsigned32
_HwTdmPsnAlarmPwIdIndex_Object = MibTableColumn
hwTdmPsnAlarmPwIdIndex = _HwTdmPsnAlarmPwIdIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 152, 1, 2, 1, 1),
    _HwTdmPsnAlarmPwIdIndex_Type()
)
hwTdmPsnAlarmPwIdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwTdmPsnAlarmPwIdIndex.setStatus("current")
_HwTdmPsnAlarmPwTypeIndex_Type = HWL2VpnVcEncapsType
_HwTdmPsnAlarmPwTypeIndex_Object = MibTableColumn
hwTdmPsnAlarmPwTypeIndex = _HwTdmPsnAlarmPwTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 152, 1, 2, 1, 2),
    _HwTdmPsnAlarmPwTypeIndex_Type()
)
hwTdmPsnAlarmPwTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwTdmPsnAlarmPwTypeIndex.setStatus("current")


class _HwTdmPsnAlarmPwStatus_Type(Integer32):
    """Custom type hwTdmPsnAlarmPwStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_HwTdmPsnAlarmPwStatus_Type.__name__ = "Integer32"
_HwTdmPsnAlarmPwStatus_Object = MibTableColumn
hwTdmPsnAlarmPwStatus = _HwTdmPsnAlarmPwStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 152, 1, 2, 1, 3),
    _HwTdmPsnAlarmPwStatus_Type()
)
hwTdmPsnAlarmPwStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTdmPsnAlarmPwStatus.setStatus("current")
_HwTdmPsnAlarmVcIfIndex_Type = InterfaceIndex
_HwTdmPsnAlarmVcIfIndex_Object = MibTableColumn
hwTdmPsnAlarmVcIfIndex = _HwTdmPsnAlarmVcIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 152, 1, 2, 1, 4),
    _HwTdmPsnAlarmVcIfIndex_Type()
)
hwTdmPsnAlarmVcIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTdmPsnAlarmVcIfIndex.setStatus("current")
_HwTdmPsnMIBTraps_ObjectIdentity = ObjectIdentity
hwTdmPsnMIBTraps = _HwTdmPsnMIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 152, 2)
)
_HwTdmPsnMIBConformance_ObjectIdentity = ObjectIdentity
hwTdmPsnMIBConformance = _HwTdmPsnMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 152, 3)
)
_HwTdmPsnMIBCompliances_ObjectIdentity = ObjectIdentity
hwTdmPsnMIBCompliances = _HwTdmPsnMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 152, 3, 1)
)
_HwTdmPsnMIBGroups_ObjectIdentity = ObjectIdentity
hwTdmPsnMIBGroups = _HwTdmPsnMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 152, 3, 2)
)

# Managed Objects groups

hwTdmPsnPerfCurrentGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 152, 3, 2, 1)
)
hwTdmPsnPerfCurrentGroup.setObjects(
      *(("HUAWEI-TDM-PSN-MIB", "hwTdmPsnPerfCurrentMissingPkts"),
        ("HUAWEI-TDM-PSN-MIB", "hwTdmPsnPerfCurrentPktsReorder"),
        ("HUAWEI-TDM-PSN-MIB", "hwTdmPsnPerfCurrentJtrBfrUnderruns"),
        ("HUAWEI-TDM-PSN-MIB", "hwTdmPsnPerfCurrentMisorderDropped"),
        ("HUAWEI-TDM-PSN-MIB", "hwTdmPsnPerfCurrentMalformedPkts"),
        ("HUAWEI-TDM-PSN-MIB", "hwTdmPsnPerfCurrentErrorSeconds"),
        ("HUAWEI-TDM-PSN-MIB", "hwTdmPsnPerfCurrentSeverelyErrorSeconds"),
        ("HUAWEI-TDM-PSN-MIB", "hwTdmPsnPerfCurrentUnavailableSeconds"),
        ("HUAWEI-TDM-PSN-MIB", "hwTdmPsnPerfCurrentFailureCounts"))
)
if mibBuilder.loadTexts:
    hwTdmPsnPerfCurrentGroup.setStatus("current")

hwTdmPsnAlarmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 152, 3, 2, 2)
)
hwTdmPsnAlarmGroup.setObjects(
      *(("HUAWEI-TDM-PSN-MIB", "hwTdmPsnAlarmPwStatus"),
        ("HUAWEI-TDM-PSN-MIB", "hwTdmPsnAlarmVcIfIndex"))
)
if mibBuilder.loadTexts:
    hwTdmPsnAlarmGroup.setStatus("current")


# Notification objects

hwTdmPsnAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 152, 2, 1)
)
hwTdmPsnAlarmTrap.setObjects(
      *(("HUAWEI-TDM-PSN-MIB", "hwTdmPsnAlarmPwStatus"),
        ("HUAWEI-TDM-PSN-MIB", "hwTdmPsnAlarmVcIfIndex"))
)
if mibBuilder.loadTexts:
    hwTdmPsnAlarmTrap.setStatus(
        "current"
    )


# Notifications groups

hwTdmPsnNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 152, 3, 2, 3)
)
hwTdmPsnNotificationGroup.setObjects(
    ("HUAWEI-TDM-PSN-MIB", "hwTdmPsnAlarmTrap")
)
if mibBuilder.loadTexts:
    hwTdmPsnNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hwTdmPsnMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 152, 3, 1, 1)
)
if mibBuilder.loadTexts:
    hwTdmPsnMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-TDM-PSN-MIB",
    **{"hwTdmPsnMIB": hwTdmPsnMIB,
       "hwTdmPsnMIBObjects": hwTdmPsnMIBObjects,
       "hwTdmPsnPerfCurrentTable": hwTdmPsnPerfCurrentTable,
       "hwTdmPsnPerfCurrentEntry": hwTdmPsnPerfCurrentEntry,
       "hwTdmPsnPerfCurrentPwIdIndex": hwTdmPsnPerfCurrentPwIdIndex,
       "hwTdmPsnPerfCurrentPwTypeIndex": hwTdmPsnPerfCurrentPwTypeIndex,
       "hwTdmPsnPerfCurrentMissingPkts": hwTdmPsnPerfCurrentMissingPkts,
       "hwTdmPsnPerfCurrentPktsReorder": hwTdmPsnPerfCurrentPktsReorder,
       "hwTdmPsnPerfCurrentJtrBfrUnderruns": hwTdmPsnPerfCurrentJtrBfrUnderruns,
       "hwTdmPsnPerfCurrentMisorderDropped": hwTdmPsnPerfCurrentMisorderDropped,
       "hwTdmPsnPerfCurrentMalformedPkts": hwTdmPsnPerfCurrentMalformedPkts,
       "hwTdmPsnPerfCurrentErrorSeconds": hwTdmPsnPerfCurrentErrorSeconds,
       "hwTdmPsnPerfCurrentSeverelyErrorSeconds": hwTdmPsnPerfCurrentSeverelyErrorSeconds,
       "hwTdmPsnPerfCurrentUnavailableSeconds": hwTdmPsnPerfCurrentUnavailableSeconds,
       "hwTdmPsnPerfCurrentFailureCounts": hwTdmPsnPerfCurrentFailureCounts,
       "hwTdmPsnAlarmTable": hwTdmPsnAlarmTable,
       "hwTdmPsnAlarmEntry": hwTdmPsnAlarmEntry,
       "hwTdmPsnAlarmPwIdIndex": hwTdmPsnAlarmPwIdIndex,
       "hwTdmPsnAlarmPwTypeIndex": hwTdmPsnAlarmPwTypeIndex,
       "hwTdmPsnAlarmPwStatus": hwTdmPsnAlarmPwStatus,
       "hwTdmPsnAlarmVcIfIndex": hwTdmPsnAlarmVcIfIndex,
       "hwTdmPsnMIBTraps": hwTdmPsnMIBTraps,
       "hwTdmPsnAlarmTrap": hwTdmPsnAlarmTrap,
       "hwTdmPsnMIBConformance": hwTdmPsnMIBConformance,
       "hwTdmPsnMIBCompliances": hwTdmPsnMIBCompliances,
       "hwTdmPsnMIBCompliance": hwTdmPsnMIBCompliance,
       "hwTdmPsnMIBGroups": hwTdmPsnMIBGroups,
       "hwTdmPsnPerfCurrentGroup": hwTdmPsnPerfCurrentGroup,
       "hwTdmPsnAlarmGroup": hwTdmPsnAlarmGroup,
       "hwTdmPsnNotificationGroup": hwTdmPsnNotificationGroup}
)
