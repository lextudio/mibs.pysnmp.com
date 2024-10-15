# SNMP MIB module (HH3C-SUBNET-VLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-SUBNET-VLAN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:55:02 2024
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

(hh3cCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cCommon")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

hh3cSubnetVlan = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 61)
)
hh3cSubnetVlan.setRevisions(
        ("2005-08-02 13:53",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cSubnetVlanObjects_ObjectIdentity = ObjectIdentity
hh3cSubnetVlanObjects = _Hh3cSubnetVlanObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 61, 1)
)
_Hh3cSubnetVlanScalarObjects_ObjectIdentity = ObjectIdentity
hh3cSubnetVlanScalarObjects = _Hh3cSubnetVlanScalarObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 61, 1, 1)
)
_Hh3cSubnetNumAllVlan_Type = Integer32
_Hh3cSubnetNumAllVlan_Object = MibScalar
hh3cSubnetNumAllVlan = _Hh3cSubnetNumAllVlan_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 61, 1, 1, 1),
    _Hh3cSubnetNumAllVlan_Type()
)
hh3cSubnetNumAllVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSubnetNumAllVlan.setStatus("current")
_Hh3cSubnetNumPerVlan_Type = Integer32
_Hh3cSubnetNumPerVlan_Object = MibScalar
hh3cSubnetNumPerVlan = _Hh3cSubnetNumPerVlan_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 61, 1, 1, 2),
    _Hh3cSubnetNumPerVlan_Type()
)
hh3cSubnetNumPerVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSubnetNumPerVlan.setStatus("current")
_Hh3cSubnetNumAllPort_Type = Integer32
_Hh3cSubnetNumAllPort_Object = MibScalar
hh3cSubnetNumAllPort = _Hh3cSubnetNumAllPort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 61, 1, 1, 3),
    _Hh3cSubnetNumAllPort_Type()
)
hh3cSubnetNumAllPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSubnetNumAllPort.setStatus("current")
_Hh3cSubnetNumPerPort_Type = Integer32
_Hh3cSubnetNumPerPort_Object = MibScalar
hh3cSubnetNumPerPort = _Hh3cSubnetNumPerPort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 61, 1, 1, 4),
    _Hh3cSubnetNumPerPort_Type()
)
hh3cSubnetNumPerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSubnetNumPerPort.setStatus("current")
_Hh3cSubnetVlanTable_Object = MibTable
hh3cSubnetVlanTable = _Hh3cSubnetVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 61, 1, 2)
)
if mibBuilder.loadTexts:
    hh3cSubnetVlanTable.setStatus("current")
_Hh3cSubnetVlanEntry_Object = MibTableRow
hh3cSubnetVlanEntry = _Hh3cSubnetVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 61, 1, 2, 1)
)
hh3cSubnetVlanEntry.setIndexNames(
    (0, "HH3C-SUBNET-VLAN-MIB", "hh3cSubnetVlanVlanId"),
    (0, "HH3C-SUBNET-VLAN-MIB", "hh3cSubnetVlanSubnetIndex"),
)
if mibBuilder.loadTexts:
    hh3cSubnetVlanEntry.setStatus("current")
_Hh3cSubnetVlanVlanId_Type = Integer32
_Hh3cSubnetVlanVlanId_Object = MibTableColumn
hh3cSubnetVlanVlanId = _Hh3cSubnetVlanVlanId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 61, 1, 2, 1, 1),
    _Hh3cSubnetVlanVlanId_Type()
)
hh3cSubnetVlanVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cSubnetVlanVlanId.setStatus("current")
_Hh3cSubnetVlanSubnetIndex_Type = Integer32
_Hh3cSubnetVlanSubnetIndex_Object = MibTableColumn
hh3cSubnetVlanSubnetIndex = _Hh3cSubnetVlanSubnetIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 61, 1, 2, 1, 2),
    _Hh3cSubnetVlanSubnetIndex_Type()
)
hh3cSubnetVlanSubnetIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cSubnetVlanSubnetIndex.setStatus("current")
_Hh3cSubnetVlanVlanIpAddressType_Type = InetAddressType
_Hh3cSubnetVlanVlanIpAddressType_Object = MibTableColumn
hh3cSubnetVlanVlanIpAddressType = _Hh3cSubnetVlanVlanIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 61, 1, 2, 1, 3),
    _Hh3cSubnetVlanVlanIpAddressType_Type()
)
hh3cSubnetVlanVlanIpAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cSubnetVlanVlanIpAddressType.setStatus("current")
_Hh3cSubnetVlanIpAddressValue_Type = InetAddress
_Hh3cSubnetVlanIpAddressValue_Object = MibTableColumn
hh3cSubnetVlanIpAddressValue = _Hh3cSubnetVlanIpAddressValue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 61, 1, 2, 1, 4),
    _Hh3cSubnetVlanIpAddressValue_Type()
)
hh3cSubnetVlanIpAddressValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cSubnetVlanIpAddressValue.setStatus("current")
_Hh3cSubnetVlanNetMaskValue_Type = InetAddress
_Hh3cSubnetVlanNetMaskValue_Object = MibTableColumn
hh3cSubnetVlanNetMaskValue = _Hh3cSubnetVlanNetMaskValue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 61, 1, 2, 1, 5),
    _Hh3cSubnetVlanNetMaskValue_Type()
)
hh3cSubnetVlanNetMaskValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cSubnetVlanNetMaskValue.setStatus("current")
_Hh3cSubnetVlanRowStatus_Type = RowStatus
_Hh3cSubnetVlanRowStatus_Object = MibTableColumn
hh3cSubnetVlanRowStatus = _Hh3cSubnetVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 61, 1, 2, 1, 6),
    _Hh3cSubnetVlanRowStatus_Type()
)
hh3cSubnetVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cSubnetVlanRowStatus.setStatus("current")
_Hh3cSubnetVlanPortCreateTable_Object = MibTable
hh3cSubnetVlanPortCreateTable = _Hh3cSubnetVlanPortCreateTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 61, 1, 3)
)
if mibBuilder.loadTexts:
    hh3cSubnetVlanPortCreateTable.setStatus("current")
_Hh3cSubnetVlanPortCreateEntry_Object = MibTableRow
hh3cSubnetVlanPortCreateEntry = _Hh3cSubnetVlanPortCreateEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 61, 1, 3, 1)
)
hh3cSubnetVlanPortCreateEntry.setIndexNames(
    (0, "HH3C-SUBNET-VLAN-MIB", "hh3cSubnetVlanPortCreateIndex"),
    (0, "HH3C-SUBNET-VLAN-MIB", "hh3cSubnetVlanPortCreateVlanId"),
)
if mibBuilder.loadTexts:
    hh3cSubnetVlanPortCreateEntry.setStatus("current")
_Hh3cSubnetVlanPortCreateIndex_Type = Integer32
_Hh3cSubnetVlanPortCreateIndex_Object = MibTableColumn
hh3cSubnetVlanPortCreateIndex = _Hh3cSubnetVlanPortCreateIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 61, 1, 3, 1, 1),
    _Hh3cSubnetVlanPortCreateIndex_Type()
)
hh3cSubnetVlanPortCreateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cSubnetVlanPortCreateIndex.setStatus("current")
_Hh3cSubnetVlanPortCreateVlanId_Type = Integer32
_Hh3cSubnetVlanPortCreateVlanId_Object = MibTableColumn
hh3cSubnetVlanPortCreateVlanId = _Hh3cSubnetVlanPortCreateVlanId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 61, 1, 3, 1, 2),
    _Hh3cSubnetVlanPortCreateVlanId_Type()
)
hh3cSubnetVlanPortCreateVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cSubnetVlanPortCreateVlanId.setStatus("current")
_Hh3cSubnetVlanPortInfoVlanId_Type = Integer32
_Hh3cSubnetVlanPortInfoVlanId_Object = MibTableColumn
hh3cSubnetVlanPortInfoVlanId = _Hh3cSubnetVlanPortInfoVlanId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 61, 1, 3, 1, 3),
    _Hh3cSubnetVlanPortInfoVlanId_Type()
)
hh3cSubnetVlanPortInfoVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSubnetVlanPortInfoVlanId.setStatus("current")
_Hh3cSubnetVlanPortRowStatus_Type = RowStatus
_Hh3cSubnetVlanPortRowStatus_Object = MibTableColumn
hh3cSubnetVlanPortRowStatus = _Hh3cSubnetVlanPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 61, 1, 3, 1, 4),
    _Hh3cSubnetVlanPortRowStatus_Type()
)
hh3cSubnetVlanPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cSubnetVlanPortRowStatus.setStatus("current")
_Hh3cSubnetVlanConformance_ObjectIdentity = ObjectIdentity
hh3cSubnetVlanConformance = _Hh3cSubnetVlanConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 61, 2)
)
_Hh3cSubnetVlanCompliances_ObjectIdentity = ObjectIdentity
hh3cSubnetVlanCompliances = _Hh3cSubnetVlanCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 61, 2, 1)
)
_Hh3cSubnetVlanGroups_ObjectIdentity = ObjectIdentity
hh3cSubnetVlanGroups = _Hh3cSubnetVlanGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 61, 2, 2)
)

# Managed Objects groups

hh3cSubnetVlanScalarObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25506, 2, 61, 2, 2, 1)
)
hh3cSubnetVlanScalarObjectGroup.setObjects(
      *(("HH3C-SUBNET-VLAN-MIB", "hh3cSubnetNumAllVlan"),
        ("HH3C-SUBNET-VLAN-MIB", "hh3cSubnetNumPerVlan"),
        ("HH3C-SUBNET-VLAN-MIB", "hh3cSubnetNumAllPort"),
        ("HH3C-SUBNET-VLAN-MIB", "hh3cSubnetNumPerPort"))
)
if mibBuilder.loadTexts:
    hh3cSubnetVlanScalarObjectGroup.setStatus("current")

hh3cSubnetVlanSubnetGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25506, 2, 61, 2, 2, 2)
)
hh3cSubnetVlanSubnetGroup.setObjects(
      *(("HH3C-SUBNET-VLAN-MIB", "hh3cSubnetVlanVlanIpAddressType"),
        ("HH3C-SUBNET-VLAN-MIB", "hh3cSubnetVlanIpAddressValue"),
        ("HH3C-SUBNET-VLAN-MIB", "hh3cSubnetVlanNetMaskValue"),
        ("HH3C-SUBNET-VLAN-MIB", "hh3cSubnetVlanRowStatus"))
)
if mibBuilder.loadTexts:
    hh3cSubnetVlanSubnetGroup.setStatus("current")

hh3cSubnetVlanPortCreateGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25506, 2, 61, 2, 2, 3)
)
hh3cSubnetVlanPortCreateGroup.setObjects(
      *(("HH3C-SUBNET-VLAN-MIB", "hh3cSubnetVlanPortInfoVlanId"),
        ("HH3C-SUBNET-VLAN-MIB", "hh3cSubnetVlanPortRowStatus"))
)
if mibBuilder.loadTexts:
    hh3cSubnetVlanPortCreateGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hh3cSubnetVlanCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 25506, 2, 61, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cSubnetVlanCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-SUBNET-VLAN-MIB",
    **{"hh3cSubnetVlan": hh3cSubnetVlan,
       "hh3cSubnetVlanObjects": hh3cSubnetVlanObjects,
       "hh3cSubnetVlanScalarObjects": hh3cSubnetVlanScalarObjects,
       "hh3cSubnetNumAllVlan": hh3cSubnetNumAllVlan,
       "hh3cSubnetNumPerVlan": hh3cSubnetNumPerVlan,
       "hh3cSubnetNumAllPort": hh3cSubnetNumAllPort,
       "hh3cSubnetNumPerPort": hh3cSubnetNumPerPort,
       "hh3cSubnetVlanTable": hh3cSubnetVlanTable,
       "hh3cSubnetVlanEntry": hh3cSubnetVlanEntry,
       "hh3cSubnetVlanVlanId": hh3cSubnetVlanVlanId,
       "hh3cSubnetVlanSubnetIndex": hh3cSubnetVlanSubnetIndex,
       "hh3cSubnetVlanVlanIpAddressType": hh3cSubnetVlanVlanIpAddressType,
       "hh3cSubnetVlanIpAddressValue": hh3cSubnetVlanIpAddressValue,
       "hh3cSubnetVlanNetMaskValue": hh3cSubnetVlanNetMaskValue,
       "hh3cSubnetVlanRowStatus": hh3cSubnetVlanRowStatus,
       "hh3cSubnetVlanPortCreateTable": hh3cSubnetVlanPortCreateTable,
       "hh3cSubnetVlanPortCreateEntry": hh3cSubnetVlanPortCreateEntry,
       "hh3cSubnetVlanPortCreateIndex": hh3cSubnetVlanPortCreateIndex,
       "hh3cSubnetVlanPortCreateVlanId": hh3cSubnetVlanPortCreateVlanId,
       "hh3cSubnetVlanPortInfoVlanId": hh3cSubnetVlanPortInfoVlanId,
       "hh3cSubnetVlanPortRowStatus": hh3cSubnetVlanPortRowStatus,
       "hh3cSubnetVlanConformance": hh3cSubnetVlanConformance,
       "hh3cSubnetVlanCompliances": hh3cSubnetVlanCompliances,
       "hh3cSubnetVlanCompliance": hh3cSubnetVlanCompliance,
       "hh3cSubnetVlanGroups": hh3cSubnetVlanGroups,
       "hh3cSubnetVlanScalarObjectGroup": hh3cSubnetVlanScalarObjectGroup,
       "hh3cSubnetVlanSubnetGroup": hh3cSubnetVlanSubnetGroup,
       "hh3cSubnetVlanPortCreateGroup": hh3cSubnetVlanPortCreateGroup}
)
