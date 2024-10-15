# SNMP MIB module (CISCO-TBRIDGE-DEV-IF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-TBRIDGE-DEV-IF-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:09:30 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
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
 MacAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention")


# MODULE-IDENTITY

ciscoTBridgeDevIfMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 269)
)
ciscoTBridgeDevIfMIB.setRevisions(
        ("2002-04-03 00:01",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoTBridgeDevIfMIBObjects_ObjectIdentity = ObjectIdentity
ciscoTBridgeDevIfMIBObjects = _CiscoTBridgeDevIfMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 269, 1)
)
_CtbrDevInterface_ObjectIdentity = ObjectIdentity
ctbrDevInterface = _CtbrDevInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 269, 1, 1)
)
_CtbrDevInterfaceTable_Object = MibTable
ctbrDevInterfaceTable = _CtbrDevInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 269, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ctbrDevInterfaceTable.setStatus("current")
_CtbrDevInterfaceEntry_Object = MibTableRow
ctbrDevInterfaceEntry = _CtbrDevInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 269, 1, 1, 1, 1)
)
ctbrDevInterfaceEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ctbrDevInterfaceEntry.setStatus("current")
_CtbrDefaultPhyAddress_Type = MacAddress
_CtbrDefaultPhyAddress_Object = MibTableColumn
ctbrDefaultPhyAddress = _CtbrDefaultPhyAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 269, 1, 1, 1, 1, 1),
    _CtbrDefaultPhyAddress_Type()
)
ctbrDefaultPhyAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctbrDefaultPhyAddress.setStatus("current")
_CtbrPhyAddress_Type = MacAddress
_CtbrPhyAddress_Object = MibTableColumn
ctbrPhyAddress = _CtbrPhyAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 269, 1, 1, 1, 1, 2),
    _CtbrPhyAddress_Type()
)
ctbrPhyAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctbrPhyAddress.setStatus("current")
_CtbrDefaultIpAddrType_Type = InetAddressType
_CtbrDefaultIpAddrType_Object = MibTableColumn
ctbrDefaultIpAddrType = _CtbrDefaultIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 269, 1, 1, 1, 1, 3),
    _CtbrDefaultIpAddrType_Type()
)
ctbrDefaultIpAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctbrDefaultIpAddrType.setStatus("current")
_CtbrDefaultIpAddress_Type = InetAddress
_CtbrDefaultIpAddress_Object = MibTableColumn
ctbrDefaultIpAddress = _CtbrDefaultIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 269, 1, 1, 1, 1, 4),
    _CtbrDefaultIpAddress_Type()
)
ctbrDefaultIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctbrDefaultIpAddress.setStatus("current")
_CtbrDefaultIpMaskType_Type = InetAddressType
_CtbrDefaultIpMaskType_Object = MibTableColumn
ctbrDefaultIpMaskType = _CtbrDefaultIpMaskType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 269, 1, 1, 1, 1, 5),
    _CtbrDefaultIpMaskType_Type()
)
ctbrDefaultIpMaskType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctbrDefaultIpMaskType.setStatus("current")
_CtbrDefaultIpMask_Type = InetAddress
_CtbrDefaultIpMask_Object = MibTableColumn
ctbrDefaultIpMask = _CtbrDefaultIpMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 269, 1, 1, 1, 1, 6),
    _CtbrDefaultIpMask_Type()
)
ctbrDefaultIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctbrDefaultIpMask.setStatus("current")
_CtbrIpAddressType_Type = InetAddressType
_CtbrIpAddressType_Object = MibTableColumn
ctbrIpAddressType = _CtbrIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 269, 1, 1, 1, 1, 7),
    _CtbrIpAddressType_Type()
)
ctbrIpAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctbrIpAddressType.setStatus("current")
_CtbrIpAddress_Type = InetAddress
_CtbrIpAddress_Object = MibTableColumn
ctbrIpAddress = _CtbrIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 269, 1, 1, 1, 1, 8),
    _CtbrIpAddress_Type()
)
ctbrIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctbrIpAddress.setStatus("current")
_CtbrIpMaskType_Type = InetAddressType
_CtbrIpMaskType_Object = MibTableColumn
ctbrIpMaskType = _CtbrIpMaskType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 269, 1, 1, 1, 1, 9),
    _CtbrIpMaskType_Type()
)
ctbrIpMaskType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctbrIpMaskType.setStatus("current")
_CtbrIpMask_Type = InetAddress
_CtbrIpMask_Object = MibTableColumn
ctbrIpMask = _CtbrIpMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 269, 1, 1, 1, 1, 10),
    _CtbrIpMask_Type()
)
ctbrIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctbrIpMask.setStatus("current")
_CtbrMSDUMaxLength_Type = Unsigned32
_CtbrMSDUMaxLength_Object = MibTableColumn
ctbrMSDUMaxLength = _CtbrMSDUMaxLength_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 269, 1, 1, 1, 1, 11),
    _CtbrMSDUMaxLength_Type()
)
ctbrMSDUMaxLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctbrMSDUMaxLength.setStatus("current")
_CiscoTBridgeDevIfMIBConformance_ObjectIdentity = ObjectIdentity
ciscoTBridgeDevIfMIBConformance = _CiscoTBridgeDevIfMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 269, 2)
)
_CiscoTBridgeDevIfMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoTBridgeDevIfMIBCompliances = _CiscoTBridgeDevIfMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 269, 2, 1)
)
_CiscoTBridgeDevIfMIBGroups_ObjectIdentity = ObjectIdentity
ciscoTBridgeDevIfMIBGroups = _CiscoTBridgeDevIfMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 269, 2, 2)
)

# Managed Objects groups

ctbrDevIfConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 269, 2, 2, 1)
)
ctbrDevIfConfigGroup.setObjects(
      *(("CISCO-TBRIDGE-DEV-IF-MIB", "ctbrDefaultPhyAddress"),
        ("CISCO-TBRIDGE-DEV-IF-MIB", "ctbrPhyAddress"),
        ("CISCO-TBRIDGE-DEV-IF-MIB", "ctbrDefaultIpAddrType"),
        ("CISCO-TBRIDGE-DEV-IF-MIB", "ctbrDefaultIpAddress"),
        ("CISCO-TBRIDGE-DEV-IF-MIB", "ctbrDefaultIpMaskType"),
        ("CISCO-TBRIDGE-DEV-IF-MIB", "ctbrDefaultIpMask"),
        ("CISCO-TBRIDGE-DEV-IF-MIB", "ctbrIpAddressType"),
        ("CISCO-TBRIDGE-DEV-IF-MIB", "ctbrIpAddress"),
        ("CISCO-TBRIDGE-DEV-IF-MIB", "ctbrIpMaskType"),
        ("CISCO-TBRIDGE-DEV-IF-MIB", "ctbrIpMask"),
        ("CISCO-TBRIDGE-DEV-IF-MIB", "ctbrMSDUMaxLength"))
)
if mibBuilder.loadTexts:
    ctbrDevIfConfigGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoTBridgeDevIfCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 269, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoTBridgeDevIfCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-TBRIDGE-DEV-IF-MIB",
    **{"ciscoTBridgeDevIfMIB": ciscoTBridgeDevIfMIB,
       "ciscoTBridgeDevIfMIBObjects": ciscoTBridgeDevIfMIBObjects,
       "ctbrDevInterface": ctbrDevInterface,
       "ctbrDevInterfaceTable": ctbrDevInterfaceTable,
       "ctbrDevInterfaceEntry": ctbrDevInterfaceEntry,
       "ctbrDefaultPhyAddress": ctbrDefaultPhyAddress,
       "ctbrPhyAddress": ctbrPhyAddress,
       "ctbrDefaultIpAddrType": ctbrDefaultIpAddrType,
       "ctbrDefaultIpAddress": ctbrDefaultIpAddress,
       "ctbrDefaultIpMaskType": ctbrDefaultIpMaskType,
       "ctbrDefaultIpMask": ctbrDefaultIpMask,
       "ctbrIpAddressType": ctbrIpAddressType,
       "ctbrIpAddress": ctbrIpAddress,
       "ctbrIpMaskType": ctbrIpMaskType,
       "ctbrIpMask": ctbrIpMask,
       "ctbrMSDUMaxLength": ctbrMSDUMaxLength,
       "ciscoTBridgeDevIfMIBConformance": ciscoTBridgeDevIfMIBConformance,
       "ciscoTBridgeDevIfMIBCompliances": ciscoTBridgeDevIfMIBCompliances,
       "ciscoTBridgeDevIfCompliance": ciscoTBridgeDevIfCompliance,
       "ciscoTBridgeDevIfMIBGroups": ciscoTBridgeDevIfMIBGroups,
       "ctbrDevIfConfigGroup": ctbrDevIfConfigGroup}
)
