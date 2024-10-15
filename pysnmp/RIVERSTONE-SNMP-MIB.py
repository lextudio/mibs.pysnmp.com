# SNMP MIB module (RIVERSTONE-SNMP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RIVERSTONE-SNMP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:47:55 2024
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

(riverstoneMibs,) = mibBuilder.importSymbols(
    "RIVERSTONE-SMI-MIB",
    "riverstoneMibs")

(snmpCommunityEntry,) = mibBuilder.importSymbols(
    "SNMP-COMMUNITY-MIB",
    "snmpCommunityEntry")

(snmpNotifyEntry,
 snmpNotifyFilterEntry,
 snmpNotifyFilterProfileEntry) = mibBuilder.importSymbols(
    "SNMP-NOTIFICATION-MIB",
    "snmpNotifyEntry",
    "snmpNotifyFilterEntry",
    "snmpNotifyFilterProfileEntry")

(snmpTargetAddrEntry,
 snmpTargetParamsEntry) = mibBuilder.importSymbols(
    "SNMP-TARGET-MIB",
    "snmpTargetAddrEntry",
    "snmpTargetParamsEntry")

(usmUserEntry,) = mibBuilder.importSymbols(
    "SNMP-USER-BASED-SM-MIB",
    "usmUserEntry")

(vacmAccessEntry,
 vacmSecurityToGroupEntry,
 vacmViewTreeFamilyEntry) = mibBuilder.importSymbols(
    "SNMP-VIEW-BASED-ACM-MIB",
    "vacmAccessEntry",
    "vacmSecurityToGroupEntry",
    "vacmViewTreeFamilyEntry")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

rsSnmpMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 2, 15)
)
rsSnmpMib.setRevisions(
        ("2000-12-04 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RsSnmpObjects_ObjectIdentity = ObjectIdentity
rsSnmpObjects = _RsSnmpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 2, 15, 1)
)
_RsSnmpV3LastChange_Type = DateAndTime
_RsSnmpV3LastChange_Object = MibScalar
rsSnmpV3LastChange = _RsSnmpV3LastChange_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 15, 1, 1),
    _RsSnmpV3LastChange_Type()
)
rsSnmpV3LastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsSnmpV3LastChange.setStatus("current")
_RsSnmpTargetAddrTable_Object = MibTable
rsSnmpTargetAddrTable = _RsSnmpTargetAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 15, 1, 2)
)
if mibBuilder.loadTexts:
    rsSnmpTargetAddrTable.setStatus("current")
_RsSnmpTargetAddrEntry_Object = MibTableRow
rsSnmpTargetAddrEntry = _RsSnmpTargetAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 15, 1, 2, 1)
)
if mibBuilder.loadTexts:
    rsSnmpTargetAddrEntry.setStatus("current")
_RsSnmpTargetAddrLastChange_Type = DateAndTime
_RsSnmpTargetAddrLastChange_Object = MibTableColumn
rsSnmpTargetAddrLastChange = _RsSnmpTargetAddrLastChange_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 15, 1, 2, 1, 1),
    _RsSnmpTargetAddrLastChange_Type()
)
rsSnmpTargetAddrLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsSnmpTargetAddrLastChange.setStatus("current")
_RsSnmpTargetParamsTable_Object = MibTable
rsSnmpTargetParamsTable = _RsSnmpTargetParamsTable_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 15, 1, 3)
)
if mibBuilder.loadTexts:
    rsSnmpTargetParamsTable.setStatus("current")
_RsSnmpTargetParamsEntry_Object = MibTableRow
rsSnmpTargetParamsEntry = _RsSnmpTargetParamsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 15, 1, 3, 1)
)
if mibBuilder.loadTexts:
    rsSnmpTargetParamsEntry.setStatus("current")
_RsSnmpTargetParamsLastChange_Type = DateAndTime
_RsSnmpTargetParamsLastChange_Object = MibTableColumn
rsSnmpTargetParamsLastChange = _RsSnmpTargetParamsLastChange_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 15, 1, 3, 1, 1),
    _RsSnmpTargetParamsLastChange_Type()
)
rsSnmpTargetParamsLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsSnmpTargetParamsLastChange.setStatus("current")
_RsSnmpNotifyTable_Object = MibTable
rsSnmpNotifyTable = _RsSnmpNotifyTable_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 15, 1, 4)
)
if mibBuilder.loadTexts:
    rsSnmpNotifyTable.setStatus("current")
_RsSnmpNotifyEntry_Object = MibTableRow
rsSnmpNotifyEntry = _RsSnmpNotifyEntry_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 15, 1, 4, 1)
)
if mibBuilder.loadTexts:
    rsSnmpNotifyEntry.setStatus("current")
_RsSnmpNotifyLastChange_Type = DateAndTime
_RsSnmpNotifyLastChange_Object = MibTableColumn
rsSnmpNotifyLastChange = _RsSnmpNotifyLastChange_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 15, 1, 4, 1, 1),
    _RsSnmpNotifyLastChange_Type()
)
rsSnmpNotifyLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsSnmpNotifyLastChange.setStatus("current")
_RsSnmpNotifyFilterProfileTable_Object = MibTable
rsSnmpNotifyFilterProfileTable = _RsSnmpNotifyFilterProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 15, 1, 5)
)
if mibBuilder.loadTexts:
    rsSnmpNotifyFilterProfileTable.setStatus("current")
_RsSnmpNotifyFilterProfileEntry_Object = MibTableRow
rsSnmpNotifyFilterProfileEntry = _RsSnmpNotifyFilterProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 15, 1, 5, 1)
)
if mibBuilder.loadTexts:
    rsSnmpNotifyFilterProfileEntry.setStatus("current")
_RsSnmpNotifyFilterProfileLastChange_Type = DateAndTime
_RsSnmpNotifyFilterProfileLastChange_Object = MibTableColumn
rsSnmpNotifyFilterProfileLastChange = _RsSnmpNotifyFilterProfileLastChange_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 15, 1, 5, 1, 1),
    _RsSnmpNotifyFilterProfileLastChange_Type()
)
rsSnmpNotifyFilterProfileLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsSnmpNotifyFilterProfileLastChange.setStatus("current")
_RsSnmpNotifyFilterTable_Object = MibTable
rsSnmpNotifyFilterTable = _RsSnmpNotifyFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 15, 1, 6)
)
if mibBuilder.loadTexts:
    rsSnmpNotifyFilterTable.setStatus("current")
_RsSnmpNotifyFilterEntry_Object = MibTableRow
rsSnmpNotifyFilterEntry = _RsSnmpNotifyFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 15, 1, 6, 1)
)
if mibBuilder.loadTexts:
    rsSnmpNotifyFilterEntry.setStatus("current")
_RsSnmpNotifyFilterLastChange_Type = DateAndTime
_RsSnmpNotifyFilterLastChange_Object = MibTableColumn
rsSnmpNotifyFilterLastChange = _RsSnmpNotifyFilterLastChange_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 15, 1, 6, 1, 1),
    _RsSnmpNotifyFilterLastChange_Type()
)
rsSnmpNotifyFilterLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsSnmpNotifyFilterLastChange.setStatus("current")
_RsUsmUserTable_Object = MibTable
rsUsmUserTable = _RsUsmUserTable_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 15, 1, 7)
)
if mibBuilder.loadTexts:
    rsUsmUserTable.setStatus("current")
_RsUsmUserEntry_Object = MibTableRow
rsUsmUserEntry = _RsUsmUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 15, 1, 7, 1)
)
if mibBuilder.loadTexts:
    rsUsmUserEntry.setStatus("current")
_RsUsmUserLastChange_Type = DateAndTime
_RsUsmUserLastChange_Object = MibTableColumn
rsUsmUserLastChange = _RsUsmUserLastChange_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 15, 1, 7, 1, 1),
    _RsUsmUserLastChange_Type()
)
rsUsmUserLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsUsmUserLastChange.setStatus("current")
_RsVacmSecurityToGroupTable_Object = MibTable
rsVacmSecurityToGroupTable = _RsVacmSecurityToGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 15, 1, 8)
)
if mibBuilder.loadTexts:
    rsVacmSecurityToGroupTable.setStatus("current")
_RsVacmSecurityToGroupEntry_Object = MibTableRow
rsVacmSecurityToGroupEntry = _RsVacmSecurityToGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 15, 1, 8, 1)
)
if mibBuilder.loadTexts:
    rsVacmSecurityToGroupEntry.setStatus("current")
_RsVacmSecurityToGroupLastChange_Type = DateAndTime
_RsVacmSecurityToGroupLastChange_Object = MibTableColumn
rsVacmSecurityToGroupLastChange = _RsVacmSecurityToGroupLastChange_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 15, 1, 8, 1, 1),
    _RsVacmSecurityToGroupLastChange_Type()
)
rsVacmSecurityToGroupLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsVacmSecurityToGroupLastChange.setStatus("current")
_RsVacmAccessTable_Object = MibTable
rsVacmAccessTable = _RsVacmAccessTable_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 15, 1, 9)
)
if mibBuilder.loadTexts:
    rsVacmAccessTable.setStatus("current")
_RsVacmAccessEntry_Object = MibTableRow
rsVacmAccessEntry = _RsVacmAccessEntry_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 15, 1, 9, 1)
)
if mibBuilder.loadTexts:
    rsVacmAccessEntry.setStatus("current")
_RsVacmAccessLastChange_Type = DateAndTime
_RsVacmAccessLastChange_Object = MibTableColumn
rsVacmAccessLastChange = _RsVacmAccessLastChange_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 15, 1, 9, 1, 1),
    _RsVacmAccessLastChange_Type()
)
rsVacmAccessLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsVacmAccessLastChange.setStatus("current")
_RsVacmViewTreeFamilyTable_Object = MibTable
rsVacmViewTreeFamilyTable = _RsVacmViewTreeFamilyTable_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 15, 1, 10)
)
if mibBuilder.loadTexts:
    rsVacmViewTreeFamilyTable.setStatus("current")
_RsVacmViewTreeFamilyEntry_Object = MibTableRow
rsVacmViewTreeFamilyEntry = _RsVacmViewTreeFamilyEntry_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 15, 1, 10, 1)
)
if mibBuilder.loadTexts:
    rsVacmViewTreeFamilyEntry.setStatus("current")
_RsVacmViewTreeFamilyLastChange_Type = DateAndTime
_RsVacmViewTreeFamilyLastChange_Object = MibTableColumn
rsVacmViewTreeFamilyLastChange = _RsVacmViewTreeFamilyLastChange_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 15, 1, 10, 1, 1),
    _RsVacmViewTreeFamilyLastChange_Type()
)
rsVacmViewTreeFamilyLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsVacmViewTreeFamilyLastChange.setStatus("current")
_RsSnmpCommunityTable_Object = MibTable
rsSnmpCommunityTable = _RsSnmpCommunityTable_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 15, 1, 11)
)
if mibBuilder.loadTexts:
    rsSnmpCommunityTable.setStatus("current")
_RsSnmpCommunityEntry_Object = MibTableRow
rsSnmpCommunityEntry = _RsSnmpCommunityEntry_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 15, 1, 11, 1)
)
if mibBuilder.loadTexts:
    rsSnmpCommunityEntry.setStatus("current")
_RsSnmpCommunityLastChange_Type = DateAndTime
_RsSnmpCommunityLastChange_Object = MibTableColumn
rsSnmpCommunityLastChange = _RsSnmpCommunityLastChange_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 15, 1, 11, 1, 1),
    _RsSnmpCommunityLastChange_Type()
)
rsSnmpCommunityLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsSnmpCommunityLastChange.setStatus("current")
_RsSnmpConformance_ObjectIdentity = ObjectIdentity
rsSnmpConformance = _RsSnmpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 2, 15, 2)
)
_RsSnmpGroups_ObjectIdentity = ObjectIdentity
rsSnmpGroups = _RsSnmpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 2, 15, 2, 1)
)
_RsSnmpCompliances_ObjectIdentity = ObjectIdentity
rsSnmpCompliances = _RsSnmpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 2, 15, 2, 2)
)
snmpTargetAddrEntry.registerAugmentions(
    ("RIVERSTONE-SNMP-MIB",
     "rsSnmpTargetAddrEntry")
)
rsSnmpTargetAddrEntry.setIndexNames(*snmpTargetAddrEntry.getIndexNames())
snmpTargetParamsEntry.registerAugmentions(
    ("RIVERSTONE-SNMP-MIB",
     "rsSnmpTargetParamsEntry")
)
rsSnmpTargetParamsEntry.setIndexNames(*snmpTargetParamsEntry.getIndexNames())
snmpNotifyEntry.registerAugmentions(
    ("RIVERSTONE-SNMP-MIB",
     "rsSnmpNotifyEntry")
)
rsSnmpNotifyEntry.setIndexNames(*snmpNotifyEntry.getIndexNames())
snmpNotifyFilterProfileEntry.registerAugmentions(
    ("RIVERSTONE-SNMP-MIB",
     "rsSnmpNotifyFilterProfileEntry")
)
rsSnmpNotifyFilterProfileEntry.setIndexNames(*snmpNotifyFilterProfileEntry.getIndexNames())
snmpNotifyFilterEntry.registerAugmentions(
    ("RIVERSTONE-SNMP-MIB",
     "rsSnmpNotifyFilterEntry")
)
rsSnmpNotifyFilterEntry.setIndexNames(*snmpNotifyFilterEntry.getIndexNames())
usmUserEntry.registerAugmentions(
    ("RIVERSTONE-SNMP-MIB",
     "rsUsmUserEntry")
)
rsUsmUserEntry.setIndexNames(*usmUserEntry.getIndexNames())
vacmSecurityToGroupEntry.registerAugmentions(
    ("RIVERSTONE-SNMP-MIB",
     "rsVacmSecurityToGroupEntry")
)
rsVacmSecurityToGroupEntry.setIndexNames(*vacmSecurityToGroupEntry.getIndexNames())
vacmAccessEntry.registerAugmentions(
    ("RIVERSTONE-SNMP-MIB",
     "rsVacmAccessEntry")
)
rsVacmAccessEntry.setIndexNames(*vacmAccessEntry.getIndexNames())
vacmViewTreeFamilyEntry.registerAugmentions(
    ("RIVERSTONE-SNMP-MIB",
     "rsVacmViewTreeFamilyEntry")
)
rsVacmViewTreeFamilyEntry.setIndexNames(*vacmViewTreeFamilyEntry.getIndexNames())
snmpCommunityEntry.registerAugmentions(
    ("RIVERSTONE-SNMP-MIB",
     "rsSnmpCommunityEntry")
)
rsSnmpCommunityEntry.setIndexNames(*snmpCommunityEntry.getIndexNames())

# Managed Objects groups

rsSnmpBaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5567, 2, 15, 2, 1, 1)
)
rsSnmpBaseGroup.setObjects(
      *(("RIVERSTONE-SNMP-MIB", "rsSnmpV3LastChange"),
        ("RIVERSTONE-SNMP-MIB", "rsSnmpTargetAddrLastChange"),
        ("RIVERSTONE-SNMP-MIB", "rsSnmpTargetParamsLastChange"),
        ("RIVERSTONE-SNMP-MIB", "rsSnmpNotifyLastChange"),
        ("RIVERSTONE-SNMP-MIB", "rsSnmpNotifyFilterProfileLastChange"),
        ("RIVERSTONE-SNMP-MIB", "rsSnmpNotifyFilterLastChange"),
        ("RIVERSTONE-SNMP-MIB", "rsUsmUserLastChange"),
        ("RIVERSTONE-SNMP-MIB", "rsVacmSecurityToGroupLastChange"),
        ("RIVERSTONE-SNMP-MIB", "rsVacmAccessLastChange"),
        ("RIVERSTONE-SNMP-MIB", "rsVacmViewTreeFamilyLastChange"),
        ("RIVERSTONE-SNMP-MIB", "rsSnmpCommunityLastChange"))
)
if mibBuilder.loadTexts:
    rsSnmpBaseGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

rsSnmpMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5567, 2, 15, 2, 2, 1)
)
if mibBuilder.loadTexts:
    rsSnmpMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RIVERSTONE-SNMP-MIB",
    **{"rsSnmpMib": rsSnmpMib,
       "rsSnmpObjects": rsSnmpObjects,
       "rsSnmpV3LastChange": rsSnmpV3LastChange,
       "rsSnmpTargetAddrTable": rsSnmpTargetAddrTable,
       "rsSnmpTargetAddrEntry": rsSnmpTargetAddrEntry,
       "rsSnmpTargetAddrLastChange": rsSnmpTargetAddrLastChange,
       "rsSnmpTargetParamsTable": rsSnmpTargetParamsTable,
       "rsSnmpTargetParamsEntry": rsSnmpTargetParamsEntry,
       "rsSnmpTargetParamsLastChange": rsSnmpTargetParamsLastChange,
       "rsSnmpNotifyTable": rsSnmpNotifyTable,
       "rsSnmpNotifyEntry": rsSnmpNotifyEntry,
       "rsSnmpNotifyLastChange": rsSnmpNotifyLastChange,
       "rsSnmpNotifyFilterProfileTable": rsSnmpNotifyFilterProfileTable,
       "rsSnmpNotifyFilterProfileEntry": rsSnmpNotifyFilterProfileEntry,
       "rsSnmpNotifyFilterProfileLastChange": rsSnmpNotifyFilterProfileLastChange,
       "rsSnmpNotifyFilterTable": rsSnmpNotifyFilterTable,
       "rsSnmpNotifyFilterEntry": rsSnmpNotifyFilterEntry,
       "rsSnmpNotifyFilterLastChange": rsSnmpNotifyFilterLastChange,
       "rsUsmUserTable": rsUsmUserTable,
       "rsUsmUserEntry": rsUsmUserEntry,
       "rsUsmUserLastChange": rsUsmUserLastChange,
       "rsVacmSecurityToGroupTable": rsVacmSecurityToGroupTable,
       "rsVacmSecurityToGroupEntry": rsVacmSecurityToGroupEntry,
       "rsVacmSecurityToGroupLastChange": rsVacmSecurityToGroupLastChange,
       "rsVacmAccessTable": rsVacmAccessTable,
       "rsVacmAccessEntry": rsVacmAccessEntry,
       "rsVacmAccessLastChange": rsVacmAccessLastChange,
       "rsVacmViewTreeFamilyTable": rsVacmViewTreeFamilyTable,
       "rsVacmViewTreeFamilyEntry": rsVacmViewTreeFamilyEntry,
       "rsVacmViewTreeFamilyLastChange": rsVacmViewTreeFamilyLastChange,
       "rsSnmpCommunityTable": rsSnmpCommunityTable,
       "rsSnmpCommunityEntry": rsSnmpCommunityEntry,
       "rsSnmpCommunityLastChange": rsSnmpCommunityLastChange,
       "rsSnmpConformance": rsSnmpConformance,
       "rsSnmpGroups": rsSnmpGroups,
       "rsSnmpBaseGroup": rsSnmpBaseGroup,
       "rsSnmpCompliances": rsSnmpCompliances,
       "rsSnmpMibCompliance": rsSnmpMibCompliance}
)
