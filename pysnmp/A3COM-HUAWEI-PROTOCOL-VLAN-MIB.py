# SNMP MIB module (A3COM-HUAWEI-PROTOCOL-VLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/A3COM-HUAWEI-PROTOCOL-VLAN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:28:53 2024
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

h3cProtocolVlan = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 16)
)
h3cProtocolVlan.setRevisions(
        ("2004-08-31 19:38",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class H3cvProtocolVlanProtocolType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              101,
              102,
              103)
        )
    )
    namedValues = NamedValues(
        *(("at", 3),
          ("ip", 1),
          ("ipv6", 4),
          ("ipx", 2),
          ("mode-ethernetii", 103),
          ("mode-llc", 101),
          ("mode-snap", 102))
    )



class H3cvProtocolVlanProtocolSubType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("ethernetii", 2),
          ("etype", 6),
          ("llc", 3),
          ("notused", 1),
          ("raw", 4),
          ("snap", 5))
    )



# MIB Managed Objects in the order of their OIDs

_H3cProtocolVlanOperate_ObjectIdentity = ObjectIdentity
h3cProtocolVlanOperate = _H3cProtocolVlanOperate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 16, 1)
)
_H3cProtocolNumAllVlan_Type = Integer32
_H3cProtocolNumAllVlan_Object = MibScalar
h3cProtocolNumAllVlan = _H3cProtocolNumAllVlan_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 16, 1, 1),
    _H3cProtocolNumAllVlan_Type()
)
h3cProtocolNumAllVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cProtocolNumAllVlan.setStatus("current")
_H3cProtocolNumPerVlan_Type = Integer32
_H3cProtocolNumPerVlan_Object = MibScalar
h3cProtocolNumPerVlan = _H3cProtocolNumPerVlan_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 16, 1, 2),
    _H3cProtocolNumPerVlan_Type()
)
h3cProtocolNumPerVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cProtocolNumPerVlan.setStatus("current")
_H3cProtocolNumAllPort_Type = Integer32
_H3cProtocolNumAllPort_Object = MibScalar
h3cProtocolNumAllPort = _H3cProtocolNumAllPort_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 16, 1, 3),
    _H3cProtocolNumAllPort_Type()
)
h3cProtocolNumAllPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cProtocolNumAllPort.setStatus("current")
_H3cProtocolNumPerPort_Type = Integer32
_H3cProtocolNumPerPort_Object = MibScalar
h3cProtocolNumPerPort = _H3cProtocolNumPerPort_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 16, 1, 4),
    _H3cProtocolNumPerPort_Type()
)
h3cProtocolNumPerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cProtocolNumPerPort.setStatus("current")
_H3cProtocolVlanTable_Object = MibTable
h3cProtocolVlanTable = _H3cProtocolVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 16, 1, 5)
)
if mibBuilder.loadTexts:
    h3cProtocolVlanTable.setStatus("current")
_H3cProtocolVlanEntry_Object = MibTableRow
h3cProtocolVlanEntry = _H3cProtocolVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 16, 1, 5, 1)
)
h3cProtocolVlanEntry.setIndexNames(
    (0, "A3COM-HUAWEI-PROTOCOL-VLAN-MIB", "h3cProtocolVlanVlanId"),
    (0, "A3COM-HUAWEI-PROTOCOL-VLAN-MIB", "h3cProtocolVlanProtocolIndex"),
)
if mibBuilder.loadTexts:
    h3cProtocolVlanEntry.setStatus("current")
_H3cProtocolVlanVlanId_Type = Integer32
_H3cProtocolVlanVlanId_Object = MibTableColumn
h3cProtocolVlanVlanId = _H3cProtocolVlanVlanId_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 16, 1, 5, 1, 1),
    _H3cProtocolVlanVlanId_Type()
)
h3cProtocolVlanVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cProtocolVlanVlanId.setStatus("current")
_H3cProtocolVlanProtocolIndex_Type = Integer32
_H3cProtocolVlanProtocolIndex_Object = MibTableColumn
h3cProtocolVlanProtocolIndex = _H3cProtocolVlanProtocolIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 16, 1, 5, 1, 2),
    _H3cProtocolVlanProtocolIndex_Type()
)
h3cProtocolVlanProtocolIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cProtocolVlanProtocolIndex.setStatus("current")
_H3cProtocolVlanProtocolType_Type = H3cvProtocolVlanProtocolType
_H3cProtocolVlanProtocolType_Object = MibTableColumn
h3cProtocolVlanProtocolType = _H3cProtocolVlanProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 16, 1, 5, 1, 3),
    _H3cProtocolVlanProtocolType_Type()
)
h3cProtocolVlanProtocolType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cProtocolVlanProtocolType.setStatus("current")
_H3cProtocolVlanProtocolSubType_Type = H3cvProtocolVlanProtocolSubType
_H3cProtocolVlanProtocolSubType_Object = MibTableColumn
h3cProtocolVlanProtocolSubType = _H3cProtocolVlanProtocolSubType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 16, 1, 5, 1, 4),
    _H3cProtocolVlanProtocolSubType_Type()
)
h3cProtocolVlanProtocolSubType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cProtocolVlanProtocolSubType.setStatus("current")


class _H3cProtocolVlanProtocolTypeValue_Type(OctetString):
    """Custom type h3cProtocolVlanProtocolTypeValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_H3cProtocolVlanProtocolTypeValue_Type.__name__ = "OctetString"
_H3cProtocolVlanProtocolTypeValue_Object = MibTableColumn
h3cProtocolVlanProtocolTypeValue = _H3cProtocolVlanProtocolTypeValue_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 16, 1, 5, 1, 5),
    _H3cProtocolVlanProtocolTypeValue_Type()
)
h3cProtocolVlanProtocolTypeValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cProtocolVlanProtocolTypeValue.setStatus("current")
_H3cProtocolVlanRowStatus_Type = RowStatus
_H3cProtocolVlanRowStatus_Object = MibTableColumn
h3cProtocolVlanRowStatus = _H3cProtocolVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 16, 1, 5, 1, 6),
    _H3cProtocolVlanRowStatus_Type()
)
h3cProtocolVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cProtocolVlanRowStatus.setStatus("current")
_H3cProtocolVlanPortTable_Object = MibTable
h3cProtocolVlanPortTable = _H3cProtocolVlanPortTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 16, 1, 6)
)
if mibBuilder.loadTexts:
    h3cProtocolVlanPortTable.setStatus("current")
_H3cProtocolVlanPortEntry_Object = MibTableRow
h3cProtocolVlanPortEntry = _H3cProtocolVlanPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 16, 1, 6, 1)
)
h3cProtocolVlanPortEntry.setIndexNames(
    (0, "A3COM-HUAWEI-PROTOCOL-VLAN-MIB", "h3cProtocolVlanPortIndex"),
    (0, "A3COM-HUAWEI-PROTOCOL-VLAN-MIB", "h3cProtocolVlanPortVlanId"),
    (0, "A3COM-HUAWEI-PROTOCOL-VLAN-MIB", "h3cProtocolVlanPortProtocolId"),
)
if mibBuilder.loadTexts:
    h3cProtocolVlanPortEntry.setStatus("current")
_H3cProtocolVlanPortIndex_Type = Integer32
_H3cProtocolVlanPortIndex_Object = MibTableColumn
h3cProtocolVlanPortIndex = _H3cProtocolVlanPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 16, 1, 6, 1, 1),
    _H3cProtocolVlanPortIndex_Type()
)
h3cProtocolVlanPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cProtocolVlanPortIndex.setStatus("current")
_H3cProtocolVlanPortVlanId_Type = Integer32
_H3cProtocolVlanPortVlanId_Object = MibTableColumn
h3cProtocolVlanPortVlanId = _H3cProtocolVlanPortVlanId_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 16, 1, 6, 1, 2),
    _H3cProtocolVlanPortVlanId_Type()
)
h3cProtocolVlanPortVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cProtocolVlanPortVlanId.setStatus("current")
_H3cProtocolVlanPortProtocolId_Type = Integer32
_H3cProtocolVlanPortProtocolId_Object = MibTableColumn
h3cProtocolVlanPortProtocolId = _H3cProtocolVlanPortProtocolId_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 16, 1, 6, 1, 3),
    _H3cProtocolVlanPortProtocolId_Type()
)
h3cProtocolVlanPortProtocolId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cProtocolVlanPortProtocolId.setStatus("current")
_H3cProtocolVlanPortProtocolType_Type = H3cvProtocolVlanProtocolType
_H3cProtocolVlanPortProtocolType_Object = MibTableColumn
h3cProtocolVlanPortProtocolType = _H3cProtocolVlanPortProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 16, 1, 6, 1, 4),
    _H3cProtocolVlanPortProtocolType_Type()
)
h3cProtocolVlanPortProtocolType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cProtocolVlanPortProtocolType.setStatus("current")
_H3cProtocolVlanPortProtocolSubType_Type = H3cvProtocolVlanProtocolSubType
_H3cProtocolVlanPortProtocolSubType_Object = MibTableColumn
h3cProtocolVlanPortProtocolSubType = _H3cProtocolVlanPortProtocolSubType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 16, 1, 6, 1, 5),
    _H3cProtocolVlanPortProtocolSubType_Type()
)
h3cProtocolVlanPortProtocolSubType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cProtocolVlanPortProtocolSubType.setStatus("current")
_H3cProtocolVlanPortTypeValue_Type = OctetString
_H3cProtocolVlanPortTypeValue_Object = MibTableColumn
h3cProtocolVlanPortTypeValue = _H3cProtocolVlanPortTypeValue_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 16, 1, 6, 1, 6),
    _H3cProtocolVlanPortTypeValue_Type()
)
h3cProtocolVlanPortTypeValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cProtocolVlanPortTypeValue.setStatus("current")
_H3cProtocolVlanPortRowStatus_Type = RowStatus
_H3cProtocolVlanPortRowStatus_Object = MibTableColumn
h3cProtocolVlanPortRowStatus = _H3cProtocolVlanPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 16, 1, 6, 1, 7),
    _H3cProtocolVlanPortRowStatus_Type()
)
h3cProtocolVlanPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cProtocolVlanPortRowStatus.setStatus("current")
_H3cDifferentProtocolNumAllPort_Type = Integer32
_H3cDifferentProtocolNumAllPort_Object = MibScalar
h3cDifferentProtocolNumAllPort = _H3cDifferentProtocolNumAllPort_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 16, 1, 7),
    _H3cDifferentProtocolNumAllPort_Type()
)
h3cDifferentProtocolNumAllPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDifferentProtocolNumAllPort.setStatus("current")
_H3cProtocolVlanConformance_ObjectIdentity = ObjectIdentity
h3cProtocolVlanConformance = _H3cProtocolVlanConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 16, 2)
)
_H3cProtocolVlanCompliances_ObjectIdentity = ObjectIdentity
h3cProtocolVlanCompliances = _H3cProtocolVlanCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 16, 2, 1)
)
_H3cProtocolVlanGroups_ObjectIdentity = ObjectIdentity
h3cProtocolVlanGroups = _H3cProtocolVlanGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 16, 2, 2)
)

# Managed Objects groups

h3cProtocolVlanOperateGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 16, 2, 2, 1)
)
h3cProtocolVlanOperateGroup.setObjects(
      *(("A3COM-HUAWEI-PROTOCOL-VLAN-MIB", "h3cProtocolNumAllVlan"),
        ("A3COM-HUAWEI-PROTOCOL-VLAN-MIB", "h3cProtocolNumPerVlan"),
        ("A3COM-HUAWEI-PROTOCOL-VLAN-MIB", "h3cProtocolNumAllPort"),
        ("A3COM-HUAWEI-PROTOCOL-VLAN-MIB", "h3cProtocolNumPerPort"),
        ("A3COM-HUAWEI-PROTOCOL-VLAN-MIB", "h3cDifferentProtocolNumAllPort"))
)
if mibBuilder.loadTexts:
    h3cProtocolVlanOperateGroup.setStatus("current")

h3cProtocolVlanProtocolGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 16, 2, 2, 2)
)
h3cProtocolVlanProtocolGroup.setObjects(
      *(("A3COM-HUAWEI-PROTOCOL-VLAN-MIB", "h3cProtocolVlanProtocolType"),
        ("A3COM-HUAWEI-PROTOCOL-VLAN-MIB", "h3cProtocolVlanProtocolSubType"),
        ("A3COM-HUAWEI-PROTOCOL-VLAN-MIB", "h3cProtocolVlanProtocolTypeValue"),
        ("A3COM-HUAWEI-PROTOCOL-VLAN-MIB", "h3cProtocolVlanRowStatus"))
)
if mibBuilder.loadTexts:
    h3cProtocolVlanProtocolGroup.setStatus("current")

h3cProtocolVlanPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 16, 2, 2, 3)
)
h3cProtocolVlanPortGroup.setObjects(
      *(("A3COM-HUAWEI-PROTOCOL-VLAN-MIB", "h3cProtocolVlanPortProtocolType"),
        ("A3COM-HUAWEI-PROTOCOL-VLAN-MIB", "h3cProtocolVlanPortProtocolSubType"),
        ("A3COM-HUAWEI-PROTOCOL-VLAN-MIB", "h3cProtocolVlanPortTypeValue"),
        ("A3COM-HUAWEI-PROTOCOL-VLAN-MIB", "h3cProtocolVlanPortRowStatus"))
)
if mibBuilder.loadTexts:
    h3cProtocolVlanPortGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

h3cProtocolVlanCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 16, 2, 1, 1)
)
if mibBuilder.loadTexts:
    h3cProtocolVlanCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "A3COM-HUAWEI-PROTOCOL-VLAN-MIB",
    **{"H3cvProtocolVlanProtocolType": H3cvProtocolVlanProtocolType,
       "H3cvProtocolVlanProtocolSubType": H3cvProtocolVlanProtocolSubType,
       "h3cProtocolVlan": h3cProtocolVlan,
       "h3cProtocolVlanOperate": h3cProtocolVlanOperate,
       "h3cProtocolNumAllVlan": h3cProtocolNumAllVlan,
       "h3cProtocolNumPerVlan": h3cProtocolNumPerVlan,
       "h3cProtocolNumAllPort": h3cProtocolNumAllPort,
       "h3cProtocolNumPerPort": h3cProtocolNumPerPort,
       "h3cProtocolVlanTable": h3cProtocolVlanTable,
       "h3cProtocolVlanEntry": h3cProtocolVlanEntry,
       "h3cProtocolVlanVlanId": h3cProtocolVlanVlanId,
       "h3cProtocolVlanProtocolIndex": h3cProtocolVlanProtocolIndex,
       "h3cProtocolVlanProtocolType": h3cProtocolVlanProtocolType,
       "h3cProtocolVlanProtocolSubType": h3cProtocolVlanProtocolSubType,
       "h3cProtocolVlanProtocolTypeValue": h3cProtocolVlanProtocolTypeValue,
       "h3cProtocolVlanRowStatus": h3cProtocolVlanRowStatus,
       "h3cProtocolVlanPortTable": h3cProtocolVlanPortTable,
       "h3cProtocolVlanPortEntry": h3cProtocolVlanPortEntry,
       "h3cProtocolVlanPortIndex": h3cProtocolVlanPortIndex,
       "h3cProtocolVlanPortVlanId": h3cProtocolVlanPortVlanId,
       "h3cProtocolVlanPortProtocolId": h3cProtocolVlanPortProtocolId,
       "h3cProtocolVlanPortProtocolType": h3cProtocolVlanPortProtocolType,
       "h3cProtocolVlanPortProtocolSubType": h3cProtocolVlanPortProtocolSubType,
       "h3cProtocolVlanPortTypeValue": h3cProtocolVlanPortTypeValue,
       "h3cProtocolVlanPortRowStatus": h3cProtocolVlanPortRowStatus,
       "h3cDifferentProtocolNumAllPort": h3cDifferentProtocolNumAllPort,
       "h3cProtocolVlanConformance": h3cProtocolVlanConformance,
       "h3cProtocolVlanCompliances": h3cProtocolVlanCompliances,
       "h3cProtocolVlanCompliance": h3cProtocolVlanCompliance,
       "h3cProtocolVlanGroups": h3cProtocolVlanGroups,
       "h3cProtocolVlanOperateGroup": h3cProtocolVlanOperateGroup,
       "h3cProtocolVlanProtocolGroup": h3cProtocolVlanProtocolGroup,
       "h3cProtocolVlanPortGroup": h3cProtocolVlanPortGroup}
)
