# SNMP MIB module (CISCO-SNMP-TARGET-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-SNMP-TARGET-EXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:08:36 2024
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

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

(snmpTargetAddrEntry,
 snmpTargetAddrName) = mibBuilder.importSymbols(
    "SNMP-TARGET-MIB",
    "snmpTargetAddrEntry",
    "snmpTargetAddrName")

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
 StorageType,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoSnmpTargetExtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 412)
)
ciscoSnmpTargetExtMIB.setRevisions(
        ("2008-11-07 00:00",
         "2007-08-20 00:00",
         "2004-04-01 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoSnmpTargetExtMIBObjects_ObjectIdentity = ObjectIdentity
ciscoSnmpTargetExtMIBObjects = _CiscoSnmpTargetExtMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 412, 1)
)
_CExtSnmpTargetAuthAddr_ObjectIdentity = ObjectIdentity
cExtSnmpTargetAuthAddr = _CExtSnmpTargetAuthAddr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 412, 1, 1)
)
_CExtSnmpTargetAuthInetType_Type = InetAddressType
_CExtSnmpTargetAuthInetType_Object = MibScalar
cExtSnmpTargetAuthInetType = _CExtSnmpTargetAuthInetType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 412, 1, 1, 1),
    _CExtSnmpTargetAuthInetType_Type()
)
cExtSnmpTargetAuthInetType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cExtSnmpTargetAuthInetType.setStatus("current")
_CExtSnmpTargetAuthInetAddr_Type = InetAddress
_CExtSnmpTargetAuthInetAddr_Object = MibScalar
cExtSnmpTargetAuthInetAddr = _CExtSnmpTargetAuthInetAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 412, 1, 1, 2),
    _CExtSnmpTargetAuthInetAddr_Type()
)
cExtSnmpTargetAuthInetAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cExtSnmpTargetAuthInetAddr.setStatus("current")
_CExtSnmpTargetAddrTable_Object = MibTable
cExtSnmpTargetAddrTable = _CExtSnmpTargetAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 412, 1, 2)
)
if mibBuilder.loadTexts:
    cExtSnmpTargetAddrTable.setStatus("current")
_CExtSnmpTargetAddrEntry_Object = MibTableRow
cExtSnmpTargetAddrEntry = _CExtSnmpTargetAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 412, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cExtSnmpTargetAddrEntry.setStatus("current")
_CExtSnmpTargetAddrIntIfIndex_Type = InterfaceIndexOrZero
_CExtSnmpTargetAddrIntIfIndex_Object = MibTableColumn
cExtSnmpTargetAddrIntIfIndex = _CExtSnmpTargetAddrIntIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 412, 1, 2, 1, 1),
    _CExtSnmpTargetAddrIntIfIndex_Type()
)
cExtSnmpTargetAddrIntIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cExtSnmpTargetAddrIntIfIndex.setStatus("current")
_CExtSnmpTargetVrfTable_Object = MibTable
cExtSnmpTargetVrfTable = _CExtSnmpTargetVrfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 412, 1, 3)
)
if mibBuilder.loadTexts:
    cExtSnmpTargetVrfTable.setStatus("current")
_CExtSnmpTargetVrfEntry_Object = MibTableRow
cExtSnmpTargetVrfEntry = _CExtSnmpTargetVrfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 412, 1, 3, 1)
)
cExtSnmpTargetVrfEntry.setIndexNames(
    (0, "SNMP-TARGET-MIB", "snmpTargetAddrName"),
    (0, "CISCO-SNMP-TARGET-EXT-MIB", "cExtSnmpTargetVrfName"),
)
if mibBuilder.loadTexts:
    cExtSnmpTargetVrfEntry.setStatus("current")


class _CExtSnmpTargetVrfName_Type(SnmpAdminString):
    """Custom type cExtSnmpTargetVrfName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CExtSnmpTargetVrfName_Type.__name__ = "SnmpAdminString"
_CExtSnmpTargetVrfName_Object = MibTableColumn
cExtSnmpTargetVrfName = _CExtSnmpTargetVrfName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 412, 1, 3, 1, 1),
    _CExtSnmpTargetVrfName_Type()
)
cExtSnmpTargetVrfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cExtSnmpTargetVrfName.setStatus("current")


class _CExtSnmpTargetVrfRoute_Type(TruthValue):
    """Custom type cExtSnmpTargetVrfRoute based on TruthValue"""


_CExtSnmpTargetVrfRoute_Object = MibTableColumn
cExtSnmpTargetVrfRoute = _CExtSnmpTargetVrfRoute_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 412, 1, 3, 1, 2),
    _CExtSnmpTargetVrfRoute_Type()
)
cExtSnmpTargetVrfRoute.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cExtSnmpTargetVrfRoute.setStatus("current")


class _CExtSnmpTargetVrfFilter_Type(TruthValue):
    """Custom type cExtSnmpTargetVrfFilter based on TruthValue"""


_CExtSnmpTargetVrfFilter_Object = MibTableColumn
cExtSnmpTargetVrfFilter = _CExtSnmpTargetVrfFilter_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 412, 1, 3, 1, 3),
    _CExtSnmpTargetVrfFilter_Type()
)
cExtSnmpTargetVrfFilter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cExtSnmpTargetVrfFilter.setStatus("current")


class _CExtSnmpTargetVrfStorage_Type(StorageType):
    """Custom type cExtSnmpTargetVrfStorage based on StorageType"""


_CExtSnmpTargetVrfStorage_Object = MibTableColumn
cExtSnmpTargetVrfStorage = _CExtSnmpTargetVrfStorage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 412, 1, 3, 1, 4),
    _CExtSnmpTargetVrfStorage_Type()
)
cExtSnmpTargetVrfStorage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cExtSnmpTargetVrfStorage.setStatus("current")
_CExtSnmpTargetVrfStatus_Type = RowStatus
_CExtSnmpTargetVrfStatus_Object = MibTableColumn
cExtSnmpTargetVrfStatus = _CExtSnmpTargetVrfStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 412, 1, 3, 1, 5),
    _CExtSnmpTargetVrfStatus_Type()
)
cExtSnmpTargetVrfStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cExtSnmpTargetVrfStatus.setStatus("current")
_CExtSnmpNotifGblTrapSrcIfIndex_Type = InterfaceIndexOrZero
_CExtSnmpNotifGblTrapSrcIfIndex_Object = MibScalar
cExtSnmpNotifGblTrapSrcIfIndex = _CExtSnmpNotifGblTrapSrcIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 412, 1, 4),
    _CExtSnmpNotifGblTrapSrcIfIndex_Type()
)
cExtSnmpNotifGblTrapSrcIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cExtSnmpNotifGblTrapSrcIfIndex.setStatus("current")
_CExtSnmpNotifGblInformSrcIfIndex_Type = InterfaceIndexOrZero
_CExtSnmpNotifGblInformSrcIfIndex_Object = MibScalar
cExtSnmpNotifGblInformSrcIfIndex = _CExtSnmpNotifGblInformSrcIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 412, 1, 5),
    _CExtSnmpNotifGblInformSrcIfIndex_Type()
)
cExtSnmpNotifGblInformSrcIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cExtSnmpNotifGblInformSrcIfIndex.setStatus("current")
_CiscoSnmpTargetExtMIBConformance_ObjectIdentity = ObjectIdentity
ciscoSnmpTargetExtMIBConformance = _CiscoSnmpTargetExtMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 412, 2)
)
_CiscoSnmpTargetExtMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoSnmpTargetExtMIBCompliances = _CiscoSnmpTargetExtMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 412, 2, 1)
)
_CiscoSnmpTargetExtMIBGroups_ObjectIdentity = ObjectIdentity
ciscoSnmpTargetExtMIBGroups = _CiscoSnmpTargetExtMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 412, 2, 2)
)
snmpTargetAddrEntry.registerAugmentions(
    ("CISCO-SNMP-TARGET-EXT-MIB",
     "cExtSnmpTargetAddrEntry")
)
cExtSnmpTargetAddrEntry.setIndexNames(*snmpTargetAddrEntry.getIndexNames())

# Managed Objects groups

ciscoSnmpTargetAuthFailureGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 412, 2, 2, 1)
)
ciscoSnmpTargetAuthFailureGroup.setObjects(
      *(("CISCO-SNMP-TARGET-EXT-MIB", "cExtSnmpTargetAuthInetType"),
        ("CISCO-SNMP-TARGET-EXT-MIB", "cExtSnmpTargetAuthInetAddr"))
)
if mibBuilder.loadTexts:
    ciscoSnmpTargetAuthFailureGroup.setStatus("current")

ciscoSnmpTargetExtMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 412, 2, 2, 2)
)
ciscoSnmpTargetExtMIBGroup.setObjects(
    ("CISCO-SNMP-TARGET-EXT-MIB", "cExtSnmpTargetAddrIntIfIndex")
)
if mibBuilder.loadTexts:
    ciscoSnmpTargetExtMIBGroup.setStatus("current")

ciscoSnmpTargetExtVrfMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 412, 2, 2, 3)
)
ciscoSnmpTargetExtVrfMIBGroup.setObjects(
      *(("CISCO-SNMP-TARGET-EXT-MIB", "cExtSnmpTargetVrfRoute"),
        ("CISCO-SNMP-TARGET-EXT-MIB", "cExtSnmpTargetVrfFilter"),
        ("CISCO-SNMP-TARGET-EXT-MIB", "cExtSnmpTargetVrfStorage"),
        ("CISCO-SNMP-TARGET-EXT-MIB", "cExtSnmpTargetVrfStatus"))
)
if mibBuilder.loadTexts:
    ciscoSnmpTargetExtVrfMIBGroup.setStatus("current")

ciscoSnmpTargetNotifSrcIntGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 412, 2, 2, 4)
)
ciscoSnmpTargetNotifSrcIntGroup.setObjects(
      *(("CISCO-SNMP-TARGET-EXT-MIB", "cExtSnmpNotifGblTrapSrcIfIndex"),
        ("CISCO-SNMP-TARGET-EXT-MIB", "cExtSnmpNotifGblInformSrcIfIndex"))
)
if mibBuilder.loadTexts:
    ciscoSnmpTargetNotifSrcIntGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoSnmpTargetExtMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 412, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoSnmpTargetExtMIBCompliance.setStatus(
        "deprecated"
    )

ciscoSnmpTargetExtMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 412, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoSnmpTargetExtMIBComplianceRev1.setStatus(
        "deprecated"
    )

ciscoSnmpTargetExtMIBComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 412, 2, 1, 3)
)
if mibBuilder.loadTexts:
    ciscoSnmpTargetExtMIBComplianceRev2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-SNMP-TARGET-EXT-MIB",
    **{"ciscoSnmpTargetExtMIB": ciscoSnmpTargetExtMIB,
       "ciscoSnmpTargetExtMIBObjects": ciscoSnmpTargetExtMIBObjects,
       "cExtSnmpTargetAuthAddr": cExtSnmpTargetAuthAddr,
       "cExtSnmpTargetAuthInetType": cExtSnmpTargetAuthInetType,
       "cExtSnmpTargetAuthInetAddr": cExtSnmpTargetAuthInetAddr,
       "cExtSnmpTargetAddrTable": cExtSnmpTargetAddrTable,
       "cExtSnmpTargetAddrEntry": cExtSnmpTargetAddrEntry,
       "cExtSnmpTargetAddrIntIfIndex": cExtSnmpTargetAddrIntIfIndex,
       "cExtSnmpTargetVrfTable": cExtSnmpTargetVrfTable,
       "cExtSnmpTargetVrfEntry": cExtSnmpTargetVrfEntry,
       "cExtSnmpTargetVrfName": cExtSnmpTargetVrfName,
       "cExtSnmpTargetVrfRoute": cExtSnmpTargetVrfRoute,
       "cExtSnmpTargetVrfFilter": cExtSnmpTargetVrfFilter,
       "cExtSnmpTargetVrfStorage": cExtSnmpTargetVrfStorage,
       "cExtSnmpTargetVrfStatus": cExtSnmpTargetVrfStatus,
       "cExtSnmpNotifGblTrapSrcIfIndex": cExtSnmpNotifGblTrapSrcIfIndex,
       "cExtSnmpNotifGblInformSrcIfIndex": cExtSnmpNotifGblInformSrcIfIndex,
       "ciscoSnmpTargetExtMIBConformance": ciscoSnmpTargetExtMIBConformance,
       "ciscoSnmpTargetExtMIBCompliances": ciscoSnmpTargetExtMIBCompliances,
       "ciscoSnmpTargetExtMIBCompliance": ciscoSnmpTargetExtMIBCompliance,
       "ciscoSnmpTargetExtMIBComplianceRev1": ciscoSnmpTargetExtMIBComplianceRev1,
       "ciscoSnmpTargetExtMIBComplianceRev2": ciscoSnmpTargetExtMIBComplianceRev2,
       "ciscoSnmpTargetExtMIBGroups": ciscoSnmpTargetExtMIBGroups,
       "ciscoSnmpTargetAuthFailureGroup": ciscoSnmpTargetAuthFailureGroup,
       "ciscoSnmpTargetExtMIBGroup": ciscoSnmpTargetExtMIBGroup,
       "ciscoSnmpTargetExtVrfMIBGroup": ciscoSnmpTargetExtVrfMIBGroup,
       "ciscoSnmpTargetNotifSrcIntGroup": ciscoSnmpTargetNotifSrcIntGroup}
)
