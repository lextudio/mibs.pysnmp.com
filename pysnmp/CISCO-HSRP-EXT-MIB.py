# SNMP MIB module (CISCO-HSRP-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-HSRP-EXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:01:16 2024
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

(cHsrpGrpNumber,) = mibBuilder.importSymbols(
    "CISCO-HSRP-MIB",
    "cHsrpGrpNumber")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoHsrpExtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 107)
)
ciscoHsrpExtMIB.setRevisions(
        ("2010-09-02 00:00",
         "2010-02-05 00:00",
         "2006-02-15 00:00",
         "1998-08-03 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoHsrpExtMIBObjects_ObjectIdentity = ObjectIdentity
ciscoHsrpExtMIBObjects = _CiscoHsrpExtMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 107, 1)
)
_CHsrpExtGroup_ObjectIdentity = ObjectIdentity
cHsrpExtGroup = _CHsrpExtGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 107, 1, 1)
)
_CHsrpExtIfTrackedTable_Object = MibTable
cHsrpExtIfTrackedTable = _CHsrpExtIfTrackedTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 107, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cHsrpExtIfTrackedTable.setStatus("current")
_CHsrpExtIfTrackedEntry_Object = MibTableRow
cHsrpExtIfTrackedEntry = _CHsrpExtIfTrackedEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 107, 1, 1, 1, 1)
)
cHsrpExtIfTrackedEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-HSRP-MIB", "cHsrpGrpNumber"),
    (0, "CISCO-HSRP-EXT-MIB", "cHsrpExtIfTracked"),
)
if mibBuilder.loadTexts:
    cHsrpExtIfTrackedEntry.setStatus("current")
_CHsrpExtIfTracked_Type = InterfaceIndex
_CHsrpExtIfTracked_Object = MibTableColumn
cHsrpExtIfTracked = _CHsrpExtIfTracked_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 107, 1, 1, 1, 1, 1),
    _CHsrpExtIfTracked_Type()
)
cHsrpExtIfTracked.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cHsrpExtIfTracked.setStatus("current")


class _CHsrpExtIfTrackedPriority_Type(Unsigned32):
    """Custom type cHsrpExtIfTrackedPriority based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CHsrpExtIfTrackedPriority_Type.__name__ = "Unsigned32"
_CHsrpExtIfTrackedPriority_Object = MibTableColumn
cHsrpExtIfTrackedPriority = _CHsrpExtIfTrackedPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 107, 1, 1, 1, 1, 2),
    _CHsrpExtIfTrackedPriority_Type()
)
cHsrpExtIfTrackedPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cHsrpExtIfTrackedPriority.setStatus("current")
_CHsrpExtIfTrackedRowStatus_Type = RowStatus
_CHsrpExtIfTrackedRowStatus_Object = MibTableColumn
cHsrpExtIfTrackedRowStatus = _CHsrpExtIfTrackedRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 107, 1, 1, 1, 1, 3),
    _CHsrpExtIfTrackedRowStatus_Type()
)
cHsrpExtIfTrackedRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cHsrpExtIfTrackedRowStatus.setStatus("current")


class _CHsrpExtIfTrackedIpNone_Type(TruthValue):
    """Custom type cHsrpExtIfTrackedIpNone based on TruthValue"""


_CHsrpExtIfTrackedIpNone_Object = MibTableColumn
cHsrpExtIfTrackedIpNone = _CHsrpExtIfTrackedIpNone_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 107, 1, 1, 1, 1, 4),
    _CHsrpExtIfTrackedIpNone_Type()
)
cHsrpExtIfTrackedIpNone.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cHsrpExtIfTrackedIpNone.setStatus("deprecated")
_CHsrpExtSecAddrTable_Object = MibTable
cHsrpExtSecAddrTable = _CHsrpExtSecAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 107, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cHsrpExtSecAddrTable.setStatus("current")
_CHsrpExtSecAddrEntry_Object = MibTableRow
cHsrpExtSecAddrEntry = _CHsrpExtSecAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 107, 1, 1, 2, 1)
)
cHsrpExtSecAddrEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-HSRP-MIB", "cHsrpGrpNumber"),
    (0, "CISCO-HSRP-EXT-MIB", "cHsrpExtSecAddrAddress"),
)
if mibBuilder.loadTexts:
    cHsrpExtSecAddrEntry.setStatus("current")
_CHsrpExtSecAddrAddress_Type = IpAddress
_CHsrpExtSecAddrAddress_Object = MibTableColumn
cHsrpExtSecAddrAddress = _CHsrpExtSecAddrAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 107, 1, 1, 2, 1, 1),
    _CHsrpExtSecAddrAddress_Type()
)
cHsrpExtSecAddrAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cHsrpExtSecAddrAddress.setStatus("current")
_CHsrpExtSecAddrRowStatus_Type = RowStatus
_CHsrpExtSecAddrRowStatus_Object = MibTableColumn
cHsrpExtSecAddrRowStatus = _CHsrpExtSecAddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 107, 1, 1, 2, 1, 2),
    _CHsrpExtSecAddrRowStatus_Type()
)
cHsrpExtSecAddrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cHsrpExtSecAddrRowStatus.setStatus("current")
_CHsrpExtIfStandbyTable_Object = MibTable
cHsrpExtIfStandbyTable = _CHsrpExtIfStandbyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 107, 1, 1, 3)
)
if mibBuilder.loadTexts:
    cHsrpExtIfStandbyTable.setStatus("current")
_CHsrpExtIfStandbyEntry_Object = MibTableRow
cHsrpExtIfStandbyEntry = _CHsrpExtIfStandbyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 107, 1, 1, 3, 1)
)
cHsrpExtIfStandbyEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-HSRP-MIB", "cHsrpGrpNumber"),
    (0, "CISCO-HSRP-EXT-MIB", "cHsrpExtIfStandbyIndex"),
)
if mibBuilder.loadTexts:
    cHsrpExtIfStandbyEntry.setStatus("current")


class _CHsrpExtIfStandbyIndex_Type(Unsigned32):
    """Custom type cHsrpExtIfStandbyIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_CHsrpExtIfStandbyIndex_Type.__name__ = "Unsigned32"
_CHsrpExtIfStandbyIndex_Object = MibTableColumn
cHsrpExtIfStandbyIndex = _CHsrpExtIfStandbyIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 107, 1, 1, 3, 1, 1),
    _CHsrpExtIfStandbyIndex_Type()
)
cHsrpExtIfStandbyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cHsrpExtIfStandbyIndex.setStatus("current")
_CHsrpExtIfStandbyDestAddrType_Type = InetAddressType
_CHsrpExtIfStandbyDestAddrType_Object = MibTableColumn
cHsrpExtIfStandbyDestAddrType = _CHsrpExtIfStandbyDestAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 107, 1, 1, 3, 1, 2),
    _CHsrpExtIfStandbyDestAddrType_Type()
)
cHsrpExtIfStandbyDestAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cHsrpExtIfStandbyDestAddrType.setStatus("current")
_CHsrpExtIfStandbyDestAddr_Type = InetAddress
_CHsrpExtIfStandbyDestAddr_Object = MibTableColumn
cHsrpExtIfStandbyDestAddr = _CHsrpExtIfStandbyDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 107, 1, 1, 3, 1, 3),
    _CHsrpExtIfStandbyDestAddr_Type()
)
cHsrpExtIfStandbyDestAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cHsrpExtIfStandbyDestAddr.setStatus("current")
_CHsrpExtIfStandbySourceAddrType_Type = InetAddressType
_CHsrpExtIfStandbySourceAddrType_Object = MibTableColumn
cHsrpExtIfStandbySourceAddrType = _CHsrpExtIfStandbySourceAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 107, 1, 1, 3, 1, 4),
    _CHsrpExtIfStandbySourceAddrType_Type()
)
cHsrpExtIfStandbySourceAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cHsrpExtIfStandbySourceAddrType.setStatus("current")
_CHsrpExtIfStandbySourceAddr_Type = InetAddress
_CHsrpExtIfStandbySourceAddr_Object = MibTableColumn
cHsrpExtIfStandbySourceAddr = _CHsrpExtIfStandbySourceAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 107, 1, 1, 3, 1, 5),
    _CHsrpExtIfStandbySourceAddr_Type()
)
cHsrpExtIfStandbySourceAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cHsrpExtIfStandbySourceAddr.setStatus("current")
_CHsrpExtIfStandbyRowStatus_Type = RowStatus
_CHsrpExtIfStandbyRowStatus_Object = MibTableColumn
cHsrpExtIfStandbyRowStatus = _CHsrpExtIfStandbyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 107, 1, 1, 3, 1, 6),
    _CHsrpExtIfStandbyRowStatus_Type()
)
cHsrpExtIfStandbyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cHsrpExtIfStandbyRowStatus.setStatus("current")
_CHsrpExtIfBIA_ObjectIdentity = ObjectIdentity
cHsrpExtIfBIA = _CHsrpExtIfBIA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 107, 1, 2)
)
_CHsrpExtIfTable_Object = MibTable
cHsrpExtIfTable = _CHsrpExtIfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 107, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cHsrpExtIfTable.setStatus("current")
_CHsrpExtIfEntry_Object = MibTableRow
cHsrpExtIfEntry = _CHsrpExtIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 107, 1, 2, 1, 1)
)
cHsrpExtIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cHsrpExtIfEntry.setStatus("current")


class _CHsrpExtIfUseBIA_Type(TruthValue):
    """Custom type cHsrpExtIfUseBIA based on TruthValue"""


_CHsrpExtIfUseBIA_Object = MibTableColumn
cHsrpExtIfUseBIA = _CHsrpExtIfUseBIA_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 107, 1, 2, 1, 1, 1),
    _CHsrpExtIfUseBIA_Type()
)
cHsrpExtIfUseBIA.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cHsrpExtIfUseBIA.setStatus("current")
_CHsrpExtIfRowStatus_Type = RowStatus
_CHsrpExtIfRowStatus_Object = MibTableColumn
cHsrpExtIfRowStatus = _CHsrpExtIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 107, 1, 2, 1, 1, 2),
    _CHsrpExtIfRowStatus_Type()
)
cHsrpExtIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cHsrpExtIfRowStatus.setStatus("current")
_CHsrpExtConformance_ObjectIdentity = ObjectIdentity
cHsrpExtConformance = _CHsrpExtConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 107, 3)
)
_CHsrpExtCompliances_ObjectIdentity = ObjectIdentity
cHsrpExtCompliances = _CHsrpExtCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 107, 3, 1)
)
_CHsrpExtComplianceGroups_ObjectIdentity = ObjectIdentity
cHsrpExtComplianceGroups = _CHsrpExtComplianceGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 107, 3, 2)
)

# Managed Objects groups

cHsrpExtIfTrackedGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 107, 3, 2, 1)
)
cHsrpExtIfTrackedGroup.setObjects(
      *(("CISCO-HSRP-EXT-MIB", "cHsrpExtIfTrackedPriority"),
        ("CISCO-HSRP-EXT-MIB", "cHsrpExtIfTrackedRowStatus"))
)
if mibBuilder.loadTexts:
    cHsrpExtIfTrackedGroup.setStatus("current")

cHsrpExtSecAddrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 107, 3, 2, 2)
)
cHsrpExtSecAddrGroup.setObjects(
    ("CISCO-HSRP-EXT-MIB", "cHsrpExtSecAddrRowStatus")
)
if mibBuilder.loadTexts:
    cHsrpExtSecAddrGroup.setStatus("current")

cHsrpExtIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 107, 3, 2, 3)
)
cHsrpExtIfGroup.setObjects(
      *(("CISCO-HSRP-EXT-MIB", "cHsrpExtIfUseBIA"),
        ("CISCO-HSRP-EXT-MIB", "cHsrpExtIfRowStatus"))
)
if mibBuilder.loadTexts:
    cHsrpExtIfGroup.setStatus("current")

cHsrpExtIfStandbyGroup91 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 107, 3, 2, 4)
)
cHsrpExtIfStandbyGroup91.setObjects(
      *(("CISCO-HSRP-EXT-MIB", "cHsrpExtIfStandbyDestAddrType"),
        ("CISCO-HSRP-EXT-MIB", "cHsrpExtIfStandbyDestAddr"),
        ("CISCO-HSRP-EXT-MIB", "cHsrpExtIfStandbySourceAddrType"),
        ("CISCO-HSRP-EXT-MIB", "cHsrpExtIfStandbySourceAddr"),
        ("CISCO-HSRP-EXT-MIB", "cHsrpExtIfStandbyRowStatus"))
)
if mibBuilder.loadTexts:
    cHsrpExtIfStandbyGroup91.setStatus("current")

cHsrpExtIfTrackedGroupSup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 107, 3, 2, 5)
)
cHsrpExtIfTrackedGroupSup1.setObjects(
    ("CISCO-HSRP-EXT-MIB", "cHsrpExtIfTrackedIpNone")
)
if mibBuilder.loadTexts:
    cHsrpExtIfTrackedGroupSup1.setStatus("deprecated")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cHsrpExtCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 107, 3, 1, 1)
)
if mibBuilder.loadTexts:
    cHsrpExtCompliance.setStatus(
        "deprecated"
    )

cHsrpExtComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 107, 3, 1, 2)
)
if mibBuilder.loadTexts:
    cHsrpExtComplianceRev1.setStatus(
        "deprecated"
    )

cHsrpExtComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 107, 3, 1, 3)
)
if mibBuilder.loadTexts:
    cHsrpExtComplianceRev2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-HSRP-EXT-MIB",
    **{"ciscoHsrpExtMIB": ciscoHsrpExtMIB,
       "ciscoHsrpExtMIBObjects": ciscoHsrpExtMIBObjects,
       "cHsrpExtGroup": cHsrpExtGroup,
       "cHsrpExtIfTrackedTable": cHsrpExtIfTrackedTable,
       "cHsrpExtIfTrackedEntry": cHsrpExtIfTrackedEntry,
       "cHsrpExtIfTracked": cHsrpExtIfTracked,
       "cHsrpExtIfTrackedPriority": cHsrpExtIfTrackedPriority,
       "cHsrpExtIfTrackedRowStatus": cHsrpExtIfTrackedRowStatus,
       "cHsrpExtIfTrackedIpNone": cHsrpExtIfTrackedIpNone,
       "cHsrpExtSecAddrTable": cHsrpExtSecAddrTable,
       "cHsrpExtSecAddrEntry": cHsrpExtSecAddrEntry,
       "cHsrpExtSecAddrAddress": cHsrpExtSecAddrAddress,
       "cHsrpExtSecAddrRowStatus": cHsrpExtSecAddrRowStatus,
       "cHsrpExtIfStandbyTable": cHsrpExtIfStandbyTable,
       "cHsrpExtIfStandbyEntry": cHsrpExtIfStandbyEntry,
       "cHsrpExtIfStandbyIndex": cHsrpExtIfStandbyIndex,
       "cHsrpExtIfStandbyDestAddrType": cHsrpExtIfStandbyDestAddrType,
       "cHsrpExtIfStandbyDestAddr": cHsrpExtIfStandbyDestAddr,
       "cHsrpExtIfStandbySourceAddrType": cHsrpExtIfStandbySourceAddrType,
       "cHsrpExtIfStandbySourceAddr": cHsrpExtIfStandbySourceAddr,
       "cHsrpExtIfStandbyRowStatus": cHsrpExtIfStandbyRowStatus,
       "cHsrpExtIfBIA": cHsrpExtIfBIA,
       "cHsrpExtIfTable": cHsrpExtIfTable,
       "cHsrpExtIfEntry": cHsrpExtIfEntry,
       "cHsrpExtIfUseBIA": cHsrpExtIfUseBIA,
       "cHsrpExtIfRowStatus": cHsrpExtIfRowStatus,
       "cHsrpExtConformance": cHsrpExtConformance,
       "cHsrpExtCompliances": cHsrpExtCompliances,
       "cHsrpExtCompliance": cHsrpExtCompliance,
       "cHsrpExtComplianceRev1": cHsrpExtComplianceRev1,
       "cHsrpExtComplianceRev2": cHsrpExtComplianceRev2,
       "cHsrpExtComplianceGroups": cHsrpExtComplianceGroups,
       "cHsrpExtIfTrackedGroup": cHsrpExtIfTrackedGroup,
       "cHsrpExtSecAddrGroup": cHsrpExtSecAddrGroup,
       "cHsrpExtIfGroup": cHsrpExtIfGroup,
       "cHsrpExtIfStandbyGroup91": cHsrpExtIfStandbyGroup91,
       "cHsrpExtIfTrackedGroupSup1": cHsrpExtIfTrackedGroupSup1}
)
