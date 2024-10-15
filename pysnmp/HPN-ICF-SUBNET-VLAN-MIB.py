# SNMP MIB module (HPN-ICF-SUBNET-VLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-SUBNET-VLAN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:01:56 2024
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

(hpnicfCommon,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicfCommon")

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

hpnicfSubnetVlan = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 61)
)
hpnicfSubnetVlan.setRevisions(
        ("2005-08-02 13:53",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpnicfSubnetVlanObjects_ObjectIdentity = ObjectIdentity
hpnicfSubnetVlanObjects = _HpnicfSubnetVlanObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 61, 1)
)
_HpnicfSubnetVlanScalarObjects_ObjectIdentity = ObjectIdentity
hpnicfSubnetVlanScalarObjects = _HpnicfSubnetVlanScalarObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 61, 1, 1)
)
_HpnicfSubnetNumAllVlan_Type = Integer32
_HpnicfSubnetNumAllVlan_Object = MibScalar
hpnicfSubnetNumAllVlan = _HpnicfSubnetNumAllVlan_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 61, 1, 1, 1),
    _HpnicfSubnetNumAllVlan_Type()
)
hpnicfSubnetNumAllVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfSubnetNumAllVlan.setStatus("current")
_HpnicfSubnetNumPerVlan_Type = Integer32
_HpnicfSubnetNumPerVlan_Object = MibScalar
hpnicfSubnetNumPerVlan = _HpnicfSubnetNumPerVlan_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 61, 1, 1, 2),
    _HpnicfSubnetNumPerVlan_Type()
)
hpnicfSubnetNumPerVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfSubnetNumPerVlan.setStatus("current")
_HpnicfSubnetNumAllPort_Type = Integer32
_HpnicfSubnetNumAllPort_Object = MibScalar
hpnicfSubnetNumAllPort = _HpnicfSubnetNumAllPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 61, 1, 1, 3),
    _HpnicfSubnetNumAllPort_Type()
)
hpnicfSubnetNumAllPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfSubnetNumAllPort.setStatus("current")
_HpnicfSubnetNumPerPort_Type = Integer32
_HpnicfSubnetNumPerPort_Object = MibScalar
hpnicfSubnetNumPerPort = _HpnicfSubnetNumPerPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 61, 1, 1, 4),
    _HpnicfSubnetNumPerPort_Type()
)
hpnicfSubnetNumPerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfSubnetNumPerPort.setStatus("current")
_HpnicfSubnetVlanTable_Object = MibTable
hpnicfSubnetVlanTable = _HpnicfSubnetVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 61, 1, 2)
)
if mibBuilder.loadTexts:
    hpnicfSubnetVlanTable.setStatus("current")
_HpnicfSubnetVlanEntry_Object = MibTableRow
hpnicfSubnetVlanEntry = _HpnicfSubnetVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 61, 1, 2, 1)
)
hpnicfSubnetVlanEntry.setIndexNames(
    (0, "HPN-ICF-SUBNET-VLAN-MIB", "hpnicfSubnetVlanVlanId"),
    (0, "HPN-ICF-SUBNET-VLAN-MIB", "hpnicfSubnetVlanSubnetIndex"),
)
if mibBuilder.loadTexts:
    hpnicfSubnetVlanEntry.setStatus("current")
_HpnicfSubnetVlanVlanId_Type = Integer32
_HpnicfSubnetVlanVlanId_Object = MibTableColumn
hpnicfSubnetVlanVlanId = _HpnicfSubnetVlanVlanId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 61, 1, 2, 1, 1),
    _HpnicfSubnetVlanVlanId_Type()
)
hpnicfSubnetVlanVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfSubnetVlanVlanId.setStatus("current")
_HpnicfSubnetVlanSubnetIndex_Type = Integer32
_HpnicfSubnetVlanSubnetIndex_Object = MibTableColumn
hpnicfSubnetVlanSubnetIndex = _HpnicfSubnetVlanSubnetIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 61, 1, 2, 1, 2),
    _HpnicfSubnetVlanSubnetIndex_Type()
)
hpnicfSubnetVlanSubnetIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfSubnetVlanSubnetIndex.setStatus("current")
_HpnicfSubnetVlanVlanIpAddressType_Type = InetAddressType
_HpnicfSubnetVlanVlanIpAddressType_Object = MibTableColumn
hpnicfSubnetVlanVlanIpAddressType = _HpnicfSubnetVlanVlanIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 61, 1, 2, 1, 3),
    _HpnicfSubnetVlanVlanIpAddressType_Type()
)
hpnicfSubnetVlanVlanIpAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfSubnetVlanVlanIpAddressType.setStatus("current")
_HpnicfSubnetVlanIpAddressValue_Type = InetAddress
_HpnicfSubnetVlanIpAddressValue_Object = MibTableColumn
hpnicfSubnetVlanIpAddressValue = _HpnicfSubnetVlanIpAddressValue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 61, 1, 2, 1, 4),
    _HpnicfSubnetVlanIpAddressValue_Type()
)
hpnicfSubnetVlanIpAddressValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfSubnetVlanIpAddressValue.setStatus("current")
_HpnicfSubnetVlanNetMaskValue_Type = InetAddress
_HpnicfSubnetVlanNetMaskValue_Object = MibTableColumn
hpnicfSubnetVlanNetMaskValue = _HpnicfSubnetVlanNetMaskValue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 61, 1, 2, 1, 5),
    _HpnicfSubnetVlanNetMaskValue_Type()
)
hpnicfSubnetVlanNetMaskValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfSubnetVlanNetMaskValue.setStatus("current")
_HpnicfSubnetVlanRowStatus_Type = RowStatus
_HpnicfSubnetVlanRowStatus_Object = MibTableColumn
hpnicfSubnetVlanRowStatus = _HpnicfSubnetVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 61, 1, 2, 1, 6),
    _HpnicfSubnetVlanRowStatus_Type()
)
hpnicfSubnetVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfSubnetVlanRowStatus.setStatus("current")
_HpnicfSubnetVlanPortCreateTable_Object = MibTable
hpnicfSubnetVlanPortCreateTable = _HpnicfSubnetVlanPortCreateTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 61, 1, 3)
)
if mibBuilder.loadTexts:
    hpnicfSubnetVlanPortCreateTable.setStatus("current")
_HpnicfSubnetVlanPortCreateEntry_Object = MibTableRow
hpnicfSubnetVlanPortCreateEntry = _HpnicfSubnetVlanPortCreateEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 61, 1, 3, 1)
)
hpnicfSubnetVlanPortCreateEntry.setIndexNames(
    (0, "HPN-ICF-SUBNET-VLAN-MIB", "hpnicfSubnetVlanPortCreateIndex"),
    (0, "HPN-ICF-SUBNET-VLAN-MIB", "hpnicfSubnetVlanPortCreateVlanId"),
)
if mibBuilder.loadTexts:
    hpnicfSubnetVlanPortCreateEntry.setStatus("current")
_HpnicfSubnetVlanPortCreateIndex_Type = Integer32
_HpnicfSubnetVlanPortCreateIndex_Object = MibTableColumn
hpnicfSubnetVlanPortCreateIndex = _HpnicfSubnetVlanPortCreateIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 61, 1, 3, 1, 1),
    _HpnicfSubnetVlanPortCreateIndex_Type()
)
hpnicfSubnetVlanPortCreateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfSubnetVlanPortCreateIndex.setStatus("current")
_HpnicfSubnetVlanPortCreateVlanId_Type = Integer32
_HpnicfSubnetVlanPortCreateVlanId_Object = MibTableColumn
hpnicfSubnetVlanPortCreateVlanId = _HpnicfSubnetVlanPortCreateVlanId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 61, 1, 3, 1, 2),
    _HpnicfSubnetVlanPortCreateVlanId_Type()
)
hpnicfSubnetVlanPortCreateVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfSubnetVlanPortCreateVlanId.setStatus("current")
_HpnicfSubnetVlanPortInfoVlanId_Type = Integer32
_HpnicfSubnetVlanPortInfoVlanId_Object = MibTableColumn
hpnicfSubnetVlanPortInfoVlanId = _HpnicfSubnetVlanPortInfoVlanId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 61, 1, 3, 1, 3),
    _HpnicfSubnetVlanPortInfoVlanId_Type()
)
hpnicfSubnetVlanPortInfoVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfSubnetVlanPortInfoVlanId.setStatus("current")
_HpnicfSubnetVlanPortRowStatus_Type = RowStatus
_HpnicfSubnetVlanPortRowStatus_Object = MibTableColumn
hpnicfSubnetVlanPortRowStatus = _HpnicfSubnetVlanPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 61, 1, 3, 1, 4),
    _HpnicfSubnetVlanPortRowStatus_Type()
)
hpnicfSubnetVlanPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfSubnetVlanPortRowStatus.setStatus("current")


class _HpnicfSubnetVlanPortStatus_Type(Integer32):
    """Custom type hpnicfSubnetVlanPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_HpnicfSubnetVlanPortStatus_Type.__name__ = "Integer32"
_HpnicfSubnetVlanPortStatus_Object = MibTableColumn
hpnicfSubnetVlanPortStatus = _HpnicfSubnetVlanPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 61, 1, 3, 1, 5),
    _HpnicfSubnetVlanPortStatus_Type()
)
hpnicfSubnetVlanPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfSubnetVlanPortStatus.setStatus("current")
_HpnicfSubnetVlanConformance_ObjectIdentity = ObjectIdentity
hpnicfSubnetVlanConformance = _HpnicfSubnetVlanConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 61, 2)
)
_HpnicfSubnetVlanCompliances_ObjectIdentity = ObjectIdentity
hpnicfSubnetVlanCompliances = _HpnicfSubnetVlanCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 61, 2, 1)
)
_HpnicfSubnetVlanGroups_ObjectIdentity = ObjectIdentity
hpnicfSubnetVlanGroups = _HpnicfSubnetVlanGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 61, 2, 2)
)

# Managed Objects groups

hpnicfSubnetVlanScalarObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 61, 2, 2, 1)
)
hpnicfSubnetVlanScalarObjectGroup.setObjects(
      *(("HPN-ICF-SUBNET-VLAN-MIB", "hpnicfSubnetNumAllVlan"),
        ("HPN-ICF-SUBNET-VLAN-MIB", "hpnicfSubnetNumPerVlan"),
        ("HPN-ICF-SUBNET-VLAN-MIB", "hpnicfSubnetNumAllPort"),
        ("HPN-ICF-SUBNET-VLAN-MIB", "hpnicfSubnetNumPerPort"))
)
if mibBuilder.loadTexts:
    hpnicfSubnetVlanScalarObjectGroup.setStatus("current")

hpnicfSubnetVlanSubnetGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 61, 2, 2, 2)
)
hpnicfSubnetVlanSubnetGroup.setObjects(
      *(("HPN-ICF-SUBNET-VLAN-MIB", "hpnicfSubnetVlanVlanIpAddressType"),
        ("HPN-ICF-SUBNET-VLAN-MIB", "hpnicfSubnetVlanIpAddressValue"),
        ("HPN-ICF-SUBNET-VLAN-MIB", "hpnicfSubnetVlanNetMaskValue"),
        ("HPN-ICF-SUBNET-VLAN-MIB", "hpnicfSubnetVlanRowStatus"))
)
if mibBuilder.loadTexts:
    hpnicfSubnetVlanSubnetGroup.setStatus("current")

hpnicfSubnetVlanPortCreateGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 61, 2, 2, 3)
)
hpnicfSubnetVlanPortCreateGroup.setObjects(
      *(("HPN-ICF-SUBNET-VLAN-MIB", "hpnicfSubnetVlanPortInfoVlanId"),
        ("HPN-ICF-SUBNET-VLAN-MIB", "hpnicfSubnetVlanPortRowStatus"))
)
if mibBuilder.loadTexts:
    hpnicfSubnetVlanPortCreateGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hpnicfSubnetVlanCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 61, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hpnicfSubnetVlanCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-SUBNET-VLAN-MIB",
    **{"hpnicfSubnetVlan": hpnicfSubnetVlan,
       "hpnicfSubnetVlanObjects": hpnicfSubnetVlanObjects,
       "hpnicfSubnetVlanScalarObjects": hpnicfSubnetVlanScalarObjects,
       "hpnicfSubnetNumAllVlan": hpnicfSubnetNumAllVlan,
       "hpnicfSubnetNumPerVlan": hpnicfSubnetNumPerVlan,
       "hpnicfSubnetNumAllPort": hpnicfSubnetNumAllPort,
       "hpnicfSubnetNumPerPort": hpnicfSubnetNumPerPort,
       "hpnicfSubnetVlanTable": hpnicfSubnetVlanTable,
       "hpnicfSubnetVlanEntry": hpnicfSubnetVlanEntry,
       "hpnicfSubnetVlanVlanId": hpnicfSubnetVlanVlanId,
       "hpnicfSubnetVlanSubnetIndex": hpnicfSubnetVlanSubnetIndex,
       "hpnicfSubnetVlanVlanIpAddressType": hpnicfSubnetVlanVlanIpAddressType,
       "hpnicfSubnetVlanIpAddressValue": hpnicfSubnetVlanIpAddressValue,
       "hpnicfSubnetVlanNetMaskValue": hpnicfSubnetVlanNetMaskValue,
       "hpnicfSubnetVlanRowStatus": hpnicfSubnetVlanRowStatus,
       "hpnicfSubnetVlanPortCreateTable": hpnicfSubnetVlanPortCreateTable,
       "hpnicfSubnetVlanPortCreateEntry": hpnicfSubnetVlanPortCreateEntry,
       "hpnicfSubnetVlanPortCreateIndex": hpnicfSubnetVlanPortCreateIndex,
       "hpnicfSubnetVlanPortCreateVlanId": hpnicfSubnetVlanPortCreateVlanId,
       "hpnicfSubnetVlanPortInfoVlanId": hpnicfSubnetVlanPortInfoVlanId,
       "hpnicfSubnetVlanPortRowStatus": hpnicfSubnetVlanPortRowStatus,
       "hpnicfSubnetVlanPortStatus": hpnicfSubnetVlanPortStatus,
       "hpnicfSubnetVlanConformance": hpnicfSubnetVlanConformance,
       "hpnicfSubnetVlanCompliances": hpnicfSubnetVlanCompliances,
       "hpnicfSubnetVlanCompliance": hpnicfSubnetVlanCompliance,
       "hpnicfSubnetVlanGroups": hpnicfSubnetVlanGroups,
       "hpnicfSubnetVlanScalarObjectGroup": hpnicfSubnetVlanScalarObjectGroup,
       "hpnicfSubnetVlanSubnetGroup": hpnicfSubnetVlanSubnetGroup,
       "hpnicfSubnetVlanPortCreateGroup": hpnicfSubnetVlanPortCreateGroup}
)
