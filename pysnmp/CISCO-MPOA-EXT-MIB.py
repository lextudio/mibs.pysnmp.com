# SNMP MIB module (CISCO-MPOA-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-MPOA-EXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:05:57 2024
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

(AtmAddress,) = mibBuilder.importSymbols(
    "ATM-FORUM-TC-MIB",
    "AtmAddress")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(VciInteger,
 VpiInteger) = mibBuilder.importSymbols(
    "LAN-EMULATION-CLIENT-MIB",
    "VciInteger",
    "VpiInteger")

(mpcIndex,
 mpsIndex) = mibBuilder.importSymbols(
    "MPOA-MIB",
    "mpcIndex",
    "mpsIndex")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

ciscoMpoaExtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 99999)
)
ciscoMpoaExtMIB.setRevisions(
        ("2000-01-10 12:30",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoMpoaExtMIBObjects_ObjectIdentity = ObjectIdentity
ciscoMpoaExtMIBObjects = _CiscoMpoaExtMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 99999, 1)
)
_CMpcExtShortcutVCC_ObjectIdentity = ObjectIdentity
cMpcExtShortcutVCC = _CMpcExtShortcutVCC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 99999, 1, 1)
)
_CMpcExtShortcutVCCTable_Object = MibTable
cMpcExtShortcutVCCTable = _CMpcExtShortcutVCCTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99999, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cMpcExtShortcutVCCTable.setStatus("current")
_CMpcExtShortcutVCCEntry_Object = MibTableRow
cMpcExtShortcutVCCEntry = _CMpcExtShortcutVCCEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99999, 1, 1, 1, 1)
)
cMpcExtShortcutVCCEntry.setIndexNames(
    (0, "MPOA-MIB", "mpcIndex"),
    (0, "CISCO-MPOA-EXT-MIB", "cmpcSCVpi"),
    (0, "CISCO-MPOA-EXT-MIB", "cmpcSCVci"),
)
if mibBuilder.loadTexts:
    cMpcExtShortcutVCCEntry.setStatus("current")
_CmpcSCVpi_Type = VpiInteger
_CmpcSCVpi_Object = MibTableColumn
cmpcSCVpi = _CmpcSCVpi_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99999, 1, 1, 1, 1, 1),
    _CmpcSCVpi_Type()
)
cmpcSCVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmpcSCVpi.setStatus("current")
_CmpcSCVci_Type = VciInteger
_CmpcSCVci_Object = MibTableColumn
cmpcSCVci = _CmpcSCVci_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99999, 1, 1, 1, 1, 2),
    _CmpcSCVci_Type()
)
cmpcSCVci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmpcSCVci.setStatus("current")
_CmpcDestAtmAddr_Type = AtmAddress
_CmpcDestAtmAddr_Object = MibTableColumn
cmpcDestAtmAddr = _CmpcDestAtmAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99999, 1, 1, 1, 1, 3),
    _CmpcDestAtmAddr_Type()
)
cmpcDestAtmAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmpcDestAtmAddr.setStatus("current")
_CMpcInterface_ObjectIdentity = ObjectIdentity
cMpcInterface = _CMpcInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 99999, 1, 2)
)
_CMpcInterfaceMappingTable_Object = MibTable
cMpcInterfaceMappingTable = _CMpcInterfaceMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99999, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cMpcInterfaceMappingTable.setStatus("current")
_CMpcInterfaceMappingEntry_Object = MibTableRow
cMpcInterfaceMappingEntry = _CMpcInterfaceMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99999, 1, 2, 1, 1)
)
cMpcInterfaceMappingEntry.setIndexNames(
    (0, "MPOA-MIB", "mpcIndex"),
)
if mibBuilder.loadTexts:
    cMpcInterfaceMappingEntry.setStatus("current")
_CMpcInterfaceMappingIndex_Type = InterfaceIndex
_CMpcInterfaceMappingIndex_Object = MibTableColumn
cMpcInterfaceMappingIndex = _CMpcInterfaceMappingIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99999, 1, 2, 1, 1, 1),
    _CMpcInterfaceMappingIndex_Type()
)
cMpcInterfaceMappingIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cMpcInterfaceMappingIndex.setStatus("current")
_CMpcInterfaceMappingRowStatus_Type = RowStatus
_CMpcInterfaceMappingRowStatus_Object = MibTableColumn
cMpcInterfaceMappingRowStatus = _CMpcInterfaceMappingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99999, 1, 2, 1, 1, 2),
    _CMpcInterfaceMappingRowStatus_Type()
)
cMpcInterfaceMappingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cMpcInterfaceMappingRowStatus.setStatus("current")
_CMpsInterface_ObjectIdentity = ObjectIdentity
cMpsInterface = _CMpsInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 99999, 1, 3)
)
_CMpsInterfaceMappingTable_Object = MibTable
cMpsInterfaceMappingTable = _CMpsInterfaceMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99999, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cMpsInterfaceMappingTable.setStatus("current")
_CMpsInterfaceMappingEntry_Object = MibTableRow
cMpsInterfaceMappingEntry = _CMpsInterfaceMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99999, 1, 3, 1, 1)
)
cMpsInterfaceMappingEntry.setIndexNames(
    (0, "MPOA-MIB", "mpsIndex"),
)
if mibBuilder.loadTexts:
    cMpsInterfaceMappingEntry.setStatus("current")
_CMpsInterfaceMappingIndex_Type = InterfaceIndex
_CMpsInterfaceMappingIndex_Object = MibTableColumn
cMpsInterfaceMappingIndex = _CMpsInterfaceMappingIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99999, 1, 3, 1, 1, 1),
    _CMpsInterfaceMappingIndex_Type()
)
cMpsInterfaceMappingIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cMpsInterfaceMappingIndex.setStatus("current")
_CMpsInterfaceMappingRowStatus_Type = RowStatus
_CMpsInterfaceMappingRowStatus_Object = MibTableColumn
cMpsInterfaceMappingRowStatus = _CMpsInterfaceMappingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99999, 1, 3, 1, 1, 2),
    _CMpsInterfaceMappingRowStatus_Type()
)
cMpsInterfaceMappingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cMpsInterfaceMappingRowStatus.setStatus("current")
_CiscoMpoaExtMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
ciscoMpoaExtMIBNotificationPrefix = _CiscoMpoaExtMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 99999, 2)
)
_CiscoMpoaExtMIBNotifications_ObjectIdentity = ObjectIdentity
ciscoMpoaExtMIBNotifications = _CiscoMpoaExtMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 99999, 2, 0)
)
_CiscoMpoaExtMIBConformance_ObjectIdentity = ObjectIdentity
ciscoMpoaExtMIBConformance = _CiscoMpoaExtMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 99999, 3)
)
_CiscoMpoaExtMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoMpoaExtMIBCompliances = _CiscoMpoaExtMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 99999, 3, 1)
)
_CiscoMpoaExtMIBGroups_ObjectIdentity = ObjectIdentity
ciscoMpoaExtMIBGroups = _CiscoMpoaExtMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 99999, 3, 2)
)

# Managed Objects groups

ciscoMpoaExtShorcutVCCMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 99999, 3, 2, 1)
)
ciscoMpoaExtShorcutVCCMIBGroup.setObjects(
    ("CISCO-MPOA-EXT-MIB", "cmpcDestAtmAddr")
)
if mibBuilder.loadTexts:
    ciscoMpoaExtShorcutVCCMIBGroup.setStatus("current")

ciscoMpoaExtMpcInterfaceMappingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 99999, 3, 2, 2)
)
ciscoMpoaExtMpcInterfaceMappingGroup.setObjects(
      *(("CISCO-MPOA-EXT-MIB", "cMpcInterfaceMappingIndex"),
        ("CISCO-MPOA-EXT-MIB", "cMpcInterfaceMappingRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoMpoaExtMpcInterfaceMappingGroup.setStatus("current")

ciscoMpoaExtMpsInterfaceMappingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 99999, 3, 2, 3)
)
ciscoMpoaExtMpsInterfaceMappingGroup.setObjects(
      *(("CISCO-MPOA-EXT-MIB", "cMpsInterfaceMappingIndex"),
        ("CISCO-MPOA-EXT-MIB", "cMpsInterfaceMappingRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoMpoaExtMpsInterfaceMappingGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoMpoaExtMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 99999, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoMpoaExtMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-MPOA-EXT-MIB",
    **{"ciscoMpoaExtMIB": ciscoMpoaExtMIB,
       "ciscoMpoaExtMIBObjects": ciscoMpoaExtMIBObjects,
       "cMpcExtShortcutVCC": cMpcExtShortcutVCC,
       "cMpcExtShortcutVCCTable": cMpcExtShortcutVCCTable,
       "cMpcExtShortcutVCCEntry": cMpcExtShortcutVCCEntry,
       "cmpcSCVpi": cmpcSCVpi,
       "cmpcSCVci": cmpcSCVci,
       "cmpcDestAtmAddr": cmpcDestAtmAddr,
       "cMpcInterface": cMpcInterface,
       "cMpcInterfaceMappingTable": cMpcInterfaceMappingTable,
       "cMpcInterfaceMappingEntry": cMpcInterfaceMappingEntry,
       "cMpcInterfaceMappingIndex": cMpcInterfaceMappingIndex,
       "cMpcInterfaceMappingRowStatus": cMpcInterfaceMappingRowStatus,
       "cMpsInterface": cMpsInterface,
       "cMpsInterfaceMappingTable": cMpsInterfaceMappingTable,
       "cMpsInterfaceMappingEntry": cMpsInterfaceMappingEntry,
       "cMpsInterfaceMappingIndex": cMpsInterfaceMappingIndex,
       "cMpsInterfaceMappingRowStatus": cMpsInterfaceMappingRowStatus,
       "ciscoMpoaExtMIBNotificationPrefix": ciscoMpoaExtMIBNotificationPrefix,
       "ciscoMpoaExtMIBNotifications": ciscoMpoaExtMIBNotifications,
       "ciscoMpoaExtMIBConformance": ciscoMpoaExtMIBConformance,
       "ciscoMpoaExtMIBCompliances": ciscoMpoaExtMIBCompliances,
       "ciscoMpoaExtMIBCompliance": ciscoMpoaExtMIBCompliance,
       "ciscoMpoaExtMIBGroups": ciscoMpoaExtMIBGroups,
       "ciscoMpoaExtShorcutVCCMIBGroup": ciscoMpoaExtShorcutVCCMIBGroup,
       "ciscoMpoaExtMpcInterfaceMappingGroup": ciscoMpoaExtMpcInterfaceMappingGroup,
       "ciscoMpoaExtMpsInterfaceMappingGroup": ciscoMpoaExtMpsInterfaceMappingGroup}
)
