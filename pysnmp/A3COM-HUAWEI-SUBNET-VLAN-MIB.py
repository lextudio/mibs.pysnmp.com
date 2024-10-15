# SNMP MIB module (A3COM-HUAWEI-SUBNET-VLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/A3COM-HUAWEI-SUBNET-VLAN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:29:08 2024
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

(h3cCommon,) = mibBuilder.importSymbols(
    "A3COM-HUAWEI-OID-MIB",
    "h3cCommon")

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

h3cSubnetVlan = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 61)
)
h3cSubnetVlan.setRevisions(
        ("2005-08-02 13:53",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3cSubnetVlanObjects_ObjectIdentity = ObjectIdentity
h3cSubnetVlanObjects = _H3cSubnetVlanObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 61, 1)
)
_H3cSubnetVlanScalarObjects_ObjectIdentity = ObjectIdentity
h3cSubnetVlanScalarObjects = _H3cSubnetVlanScalarObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 61, 1, 1)
)
_H3cSubnetNumAllVlan_Type = Integer32
_H3cSubnetNumAllVlan_Object = MibScalar
h3cSubnetNumAllVlan = _H3cSubnetNumAllVlan_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 61, 1, 1, 1),
    _H3cSubnetNumAllVlan_Type()
)
h3cSubnetNumAllVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cSubnetNumAllVlan.setStatus("current")
_H3cSubnetNumPerVlan_Type = Integer32
_H3cSubnetNumPerVlan_Object = MibScalar
h3cSubnetNumPerVlan = _H3cSubnetNumPerVlan_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 61, 1, 1, 2),
    _H3cSubnetNumPerVlan_Type()
)
h3cSubnetNumPerVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cSubnetNumPerVlan.setStatus("current")
_H3cSubnetNumAllPort_Type = Integer32
_H3cSubnetNumAllPort_Object = MibScalar
h3cSubnetNumAllPort = _H3cSubnetNumAllPort_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 61, 1, 1, 3),
    _H3cSubnetNumAllPort_Type()
)
h3cSubnetNumAllPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cSubnetNumAllPort.setStatus("current")
_H3cSubnetNumPerPort_Type = Integer32
_H3cSubnetNumPerPort_Object = MibScalar
h3cSubnetNumPerPort = _H3cSubnetNumPerPort_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 61, 1, 1, 4),
    _H3cSubnetNumPerPort_Type()
)
h3cSubnetNumPerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cSubnetNumPerPort.setStatus("current")
_H3cSubnetVlanTable_Object = MibTable
h3cSubnetVlanTable = _H3cSubnetVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 61, 1, 2)
)
if mibBuilder.loadTexts:
    h3cSubnetVlanTable.setStatus("current")
_H3cSubnetVlanEntry_Object = MibTableRow
h3cSubnetVlanEntry = _H3cSubnetVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 61, 1, 2, 1)
)
h3cSubnetVlanEntry.setIndexNames(
    (0, "A3COM-HUAWEI-SUBNET-VLAN-MIB", "h3cSubnetVlanVlanId"),
    (0, "A3COM-HUAWEI-SUBNET-VLAN-MIB", "h3cSubnetVlanSubnetIndex"),
)
if mibBuilder.loadTexts:
    h3cSubnetVlanEntry.setStatus("current")
_H3cSubnetVlanVlanId_Type = Integer32
_H3cSubnetVlanVlanId_Object = MibTableColumn
h3cSubnetVlanVlanId = _H3cSubnetVlanVlanId_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 61, 1, 2, 1, 1),
    _H3cSubnetVlanVlanId_Type()
)
h3cSubnetVlanVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cSubnetVlanVlanId.setStatus("current")
_H3cSubnetVlanSubnetIndex_Type = Integer32
_H3cSubnetVlanSubnetIndex_Object = MibTableColumn
h3cSubnetVlanSubnetIndex = _H3cSubnetVlanSubnetIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 61, 1, 2, 1, 2),
    _H3cSubnetVlanSubnetIndex_Type()
)
h3cSubnetVlanSubnetIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cSubnetVlanSubnetIndex.setStatus("current")
_H3cSubnetVlanVlanIpAddressType_Type = InetAddressType
_H3cSubnetVlanVlanIpAddressType_Object = MibTableColumn
h3cSubnetVlanVlanIpAddressType = _H3cSubnetVlanVlanIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 61, 1, 2, 1, 3),
    _H3cSubnetVlanVlanIpAddressType_Type()
)
h3cSubnetVlanVlanIpAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cSubnetVlanVlanIpAddressType.setStatus("current")
_H3cSubnetVlanIpAddressValue_Type = InetAddress
_H3cSubnetVlanIpAddressValue_Object = MibTableColumn
h3cSubnetVlanIpAddressValue = _H3cSubnetVlanIpAddressValue_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 61, 1, 2, 1, 4),
    _H3cSubnetVlanIpAddressValue_Type()
)
h3cSubnetVlanIpAddressValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cSubnetVlanIpAddressValue.setStatus("current")
_H3cSubnetVlanNetMaskValue_Type = InetAddress
_H3cSubnetVlanNetMaskValue_Object = MibTableColumn
h3cSubnetVlanNetMaskValue = _H3cSubnetVlanNetMaskValue_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 61, 1, 2, 1, 5),
    _H3cSubnetVlanNetMaskValue_Type()
)
h3cSubnetVlanNetMaskValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cSubnetVlanNetMaskValue.setStatus("current")
_H3cSubnetVlanRowStatus_Type = RowStatus
_H3cSubnetVlanRowStatus_Object = MibTableColumn
h3cSubnetVlanRowStatus = _H3cSubnetVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 61, 1, 2, 1, 6),
    _H3cSubnetVlanRowStatus_Type()
)
h3cSubnetVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cSubnetVlanRowStatus.setStatus("current")
_H3cSubnetVlanPortCreateTable_Object = MibTable
h3cSubnetVlanPortCreateTable = _H3cSubnetVlanPortCreateTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 61, 1, 3)
)
if mibBuilder.loadTexts:
    h3cSubnetVlanPortCreateTable.setStatus("current")
_H3cSubnetVlanPortCreateEntry_Object = MibTableRow
h3cSubnetVlanPortCreateEntry = _H3cSubnetVlanPortCreateEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 61, 1, 3, 1)
)
h3cSubnetVlanPortCreateEntry.setIndexNames(
    (0, "A3COM-HUAWEI-SUBNET-VLAN-MIB", "h3cSubnetVlanPortCreateIndex"),
    (0, "A3COM-HUAWEI-SUBNET-VLAN-MIB", "h3cSubnetVlanPortCreateVlanId"),
)
if mibBuilder.loadTexts:
    h3cSubnetVlanPortCreateEntry.setStatus("current")
_H3cSubnetVlanPortCreateIndex_Type = Integer32
_H3cSubnetVlanPortCreateIndex_Object = MibTableColumn
h3cSubnetVlanPortCreateIndex = _H3cSubnetVlanPortCreateIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 61, 1, 3, 1, 1),
    _H3cSubnetVlanPortCreateIndex_Type()
)
h3cSubnetVlanPortCreateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cSubnetVlanPortCreateIndex.setStatus("current")
_H3cSubnetVlanPortCreateVlanId_Type = Integer32
_H3cSubnetVlanPortCreateVlanId_Object = MibTableColumn
h3cSubnetVlanPortCreateVlanId = _H3cSubnetVlanPortCreateVlanId_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 61, 1, 3, 1, 2),
    _H3cSubnetVlanPortCreateVlanId_Type()
)
h3cSubnetVlanPortCreateVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cSubnetVlanPortCreateVlanId.setStatus("current")
_H3cSubnetVlanPortInfoVlanId_Type = Integer32
_H3cSubnetVlanPortInfoVlanId_Object = MibTableColumn
h3cSubnetVlanPortInfoVlanId = _H3cSubnetVlanPortInfoVlanId_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 61, 1, 3, 1, 3),
    _H3cSubnetVlanPortInfoVlanId_Type()
)
h3cSubnetVlanPortInfoVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cSubnetVlanPortInfoVlanId.setStatus("current")
_H3cSubnetVlanPortRowStatus_Type = RowStatus
_H3cSubnetVlanPortRowStatus_Object = MibTableColumn
h3cSubnetVlanPortRowStatus = _H3cSubnetVlanPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 61, 1, 3, 1, 4),
    _H3cSubnetVlanPortRowStatus_Type()
)
h3cSubnetVlanPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cSubnetVlanPortRowStatus.setStatus("current")
_H3cSubnetVlanConformance_ObjectIdentity = ObjectIdentity
h3cSubnetVlanConformance = _H3cSubnetVlanConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 61, 2)
)
_H3cSubnetVlanCompliances_ObjectIdentity = ObjectIdentity
h3cSubnetVlanCompliances = _H3cSubnetVlanCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 61, 2, 1)
)
_H3cSubnetVlanGroups_ObjectIdentity = ObjectIdentity
h3cSubnetVlanGroups = _H3cSubnetVlanGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 61, 2, 2)
)

# Managed Objects groups

h3cSubnetVlanScalarObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 61, 2, 2, 1)
)
h3cSubnetVlanScalarObjectGroup.setObjects(
      *(("A3COM-HUAWEI-SUBNET-VLAN-MIB", "h3cSubnetNumAllVlan"),
        ("A3COM-HUAWEI-SUBNET-VLAN-MIB", "h3cSubnetNumPerVlan"),
        ("A3COM-HUAWEI-SUBNET-VLAN-MIB", "h3cSubnetNumAllPort"),
        ("A3COM-HUAWEI-SUBNET-VLAN-MIB", "h3cSubnetNumPerPort"))
)
if mibBuilder.loadTexts:
    h3cSubnetVlanScalarObjectGroup.setStatus("current")

h3cSubnetVlanSubnetGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 61, 2, 2, 2)
)
h3cSubnetVlanSubnetGroup.setObjects(
      *(("A3COM-HUAWEI-SUBNET-VLAN-MIB", "h3cSubnetVlanVlanIpAddressType"),
        ("A3COM-HUAWEI-SUBNET-VLAN-MIB", "h3cSubnetVlanIpAddressValue"),
        ("A3COM-HUAWEI-SUBNET-VLAN-MIB", "h3cSubnetVlanNetMaskValue"),
        ("A3COM-HUAWEI-SUBNET-VLAN-MIB", "h3cSubnetVlanRowStatus"))
)
if mibBuilder.loadTexts:
    h3cSubnetVlanSubnetGroup.setStatus("current")

h3cSubnetVlanPortCreateGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 61, 2, 2, 3)
)
h3cSubnetVlanPortCreateGroup.setObjects(
      *(("A3COM-HUAWEI-SUBNET-VLAN-MIB", "h3cSubnetVlanPortInfoVlanId"),
        ("A3COM-HUAWEI-SUBNET-VLAN-MIB", "h3cSubnetVlanPortRowStatus"))
)
if mibBuilder.loadTexts:
    h3cSubnetVlanPortCreateGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

h3cSubnetVlanCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 61, 2, 1, 1)
)
if mibBuilder.loadTexts:
    h3cSubnetVlanCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "A3COM-HUAWEI-SUBNET-VLAN-MIB",
    **{"h3cSubnetVlan": h3cSubnetVlan,
       "h3cSubnetVlanObjects": h3cSubnetVlanObjects,
       "h3cSubnetVlanScalarObjects": h3cSubnetVlanScalarObjects,
       "h3cSubnetNumAllVlan": h3cSubnetNumAllVlan,
       "h3cSubnetNumPerVlan": h3cSubnetNumPerVlan,
       "h3cSubnetNumAllPort": h3cSubnetNumAllPort,
       "h3cSubnetNumPerPort": h3cSubnetNumPerPort,
       "h3cSubnetVlanTable": h3cSubnetVlanTable,
       "h3cSubnetVlanEntry": h3cSubnetVlanEntry,
       "h3cSubnetVlanVlanId": h3cSubnetVlanVlanId,
       "h3cSubnetVlanSubnetIndex": h3cSubnetVlanSubnetIndex,
       "h3cSubnetVlanVlanIpAddressType": h3cSubnetVlanVlanIpAddressType,
       "h3cSubnetVlanIpAddressValue": h3cSubnetVlanIpAddressValue,
       "h3cSubnetVlanNetMaskValue": h3cSubnetVlanNetMaskValue,
       "h3cSubnetVlanRowStatus": h3cSubnetVlanRowStatus,
       "h3cSubnetVlanPortCreateTable": h3cSubnetVlanPortCreateTable,
       "h3cSubnetVlanPortCreateEntry": h3cSubnetVlanPortCreateEntry,
       "h3cSubnetVlanPortCreateIndex": h3cSubnetVlanPortCreateIndex,
       "h3cSubnetVlanPortCreateVlanId": h3cSubnetVlanPortCreateVlanId,
       "h3cSubnetVlanPortInfoVlanId": h3cSubnetVlanPortInfoVlanId,
       "h3cSubnetVlanPortRowStatus": h3cSubnetVlanPortRowStatus,
       "h3cSubnetVlanConformance": h3cSubnetVlanConformance,
       "h3cSubnetVlanCompliances": h3cSubnetVlanCompliances,
       "h3cSubnetVlanCompliance": h3cSubnetVlanCompliance,
       "h3cSubnetVlanGroups": h3cSubnetVlanGroups,
       "h3cSubnetVlanScalarObjectGroup": h3cSubnetVlanScalarObjectGroup,
       "h3cSubnetVlanSubnetGroup": h3cSubnetVlanSubnetGroup,
       "h3cSubnetVlanPortCreateGroup": h3cSubnetVlanPortCreateGroup}
)
