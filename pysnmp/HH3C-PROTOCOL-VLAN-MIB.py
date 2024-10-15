# SNMP MIB module (HH3C-PROTOCOL-VLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-PROTOCOL-VLAN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:54:35 2024
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

hh3cProtocolVlan = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 16)
)
hh3cProtocolVlan.setRevisions(
        ("2004-08-31 19:38",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class Hh3cvProtocolVlanProtocolType(Integer32, TextualConvention):
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



class Hh3cvProtocolVlanProtocolSubType(Integer32, TextualConvention):
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

_Hh3cProtocolVlanOperate_ObjectIdentity = ObjectIdentity
hh3cProtocolVlanOperate = _Hh3cProtocolVlanOperate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 16, 1)
)
_Hh3cProtocolNumAllVlan_Type = Integer32
_Hh3cProtocolNumAllVlan_Object = MibScalar
hh3cProtocolNumAllVlan = _Hh3cProtocolNumAllVlan_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 16, 1, 1),
    _Hh3cProtocolNumAllVlan_Type()
)
hh3cProtocolNumAllVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cProtocolNumAllVlan.setStatus("current")
_Hh3cProtocolNumPerVlan_Type = Integer32
_Hh3cProtocolNumPerVlan_Object = MibScalar
hh3cProtocolNumPerVlan = _Hh3cProtocolNumPerVlan_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 16, 1, 2),
    _Hh3cProtocolNumPerVlan_Type()
)
hh3cProtocolNumPerVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cProtocolNumPerVlan.setStatus("current")
_Hh3cProtocolNumAllPort_Type = Integer32
_Hh3cProtocolNumAllPort_Object = MibScalar
hh3cProtocolNumAllPort = _Hh3cProtocolNumAllPort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 16, 1, 3),
    _Hh3cProtocolNumAllPort_Type()
)
hh3cProtocolNumAllPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cProtocolNumAllPort.setStatus("current")
_Hh3cProtocolNumPerPort_Type = Integer32
_Hh3cProtocolNumPerPort_Object = MibScalar
hh3cProtocolNumPerPort = _Hh3cProtocolNumPerPort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 16, 1, 4),
    _Hh3cProtocolNumPerPort_Type()
)
hh3cProtocolNumPerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cProtocolNumPerPort.setStatus("current")
_Hh3cProtocolVlanTable_Object = MibTable
hh3cProtocolVlanTable = _Hh3cProtocolVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 16, 1, 5)
)
if mibBuilder.loadTexts:
    hh3cProtocolVlanTable.setStatus("current")
_Hh3cProtocolVlanEntry_Object = MibTableRow
hh3cProtocolVlanEntry = _Hh3cProtocolVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 16, 1, 5, 1)
)
hh3cProtocolVlanEntry.setIndexNames(
    (0, "HH3C-PROTOCOL-VLAN-MIB", "hh3cProtocolVlanVlanId"),
    (0, "HH3C-PROTOCOL-VLAN-MIB", "hh3cProtocolVlanProtocolIndex"),
)
if mibBuilder.loadTexts:
    hh3cProtocolVlanEntry.setStatus("current")
_Hh3cProtocolVlanVlanId_Type = Integer32
_Hh3cProtocolVlanVlanId_Object = MibTableColumn
hh3cProtocolVlanVlanId = _Hh3cProtocolVlanVlanId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 16, 1, 5, 1, 1),
    _Hh3cProtocolVlanVlanId_Type()
)
hh3cProtocolVlanVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cProtocolVlanVlanId.setStatus("current")
_Hh3cProtocolVlanProtocolIndex_Type = Integer32
_Hh3cProtocolVlanProtocolIndex_Object = MibTableColumn
hh3cProtocolVlanProtocolIndex = _Hh3cProtocolVlanProtocolIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 16, 1, 5, 1, 2),
    _Hh3cProtocolVlanProtocolIndex_Type()
)
hh3cProtocolVlanProtocolIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cProtocolVlanProtocolIndex.setStatus("current")
_Hh3cProtocolVlanProtocolType_Type = Hh3cvProtocolVlanProtocolType
_Hh3cProtocolVlanProtocolType_Object = MibTableColumn
hh3cProtocolVlanProtocolType = _Hh3cProtocolVlanProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 16, 1, 5, 1, 3),
    _Hh3cProtocolVlanProtocolType_Type()
)
hh3cProtocolVlanProtocolType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cProtocolVlanProtocolType.setStatus("current")
_Hh3cProtocolVlanProtocolSubType_Type = Hh3cvProtocolVlanProtocolSubType
_Hh3cProtocolVlanProtocolSubType_Object = MibTableColumn
hh3cProtocolVlanProtocolSubType = _Hh3cProtocolVlanProtocolSubType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 16, 1, 5, 1, 4),
    _Hh3cProtocolVlanProtocolSubType_Type()
)
hh3cProtocolVlanProtocolSubType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cProtocolVlanProtocolSubType.setStatus("current")


class _Hh3cProtocolVlanProtocolTypeValue_Type(OctetString):
    """Custom type hh3cProtocolVlanProtocolTypeValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cProtocolVlanProtocolTypeValue_Type.__name__ = "OctetString"
_Hh3cProtocolVlanProtocolTypeValue_Object = MibTableColumn
hh3cProtocolVlanProtocolTypeValue = _Hh3cProtocolVlanProtocolTypeValue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 16, 1, 5, 1, 5),
    _Hh3cProtocolVlanProtocolTypeValue_Type()
)
hh3cProtocolVlanProtocolTypeValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cProtocolVlanProtocolTypeValue.setStatus("current")
_Hh3cProtocolVlanRowStatus_Type = RowStatus
_Hh3cProtocolVlanRowStatus_Object = MibTableColumn
hh3cProtocolVlanRowStatus = _Hh3cProtocolVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 16, 1, 5, 1, 6),
    _Hh3cProtocolVlanRowStatus_Type()
)
hh3cProtocolVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cProtocolVlanRowStatus.setStatus("current")
_Hh3cProtocolVlanPortTable_Object = MibTable
hh3cProtocolVlanPortTable = _Hh3cProtocolVlanPortTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 16, 1, 6)
)
if mibBuilder.loadTexts:
    hh3cProtocolVlanPortTable.setStatus("current")
_Hh3cProtocolVlanPortEntry_Object = MibTableRow
hh3cProtocolVlanPortEntry = _Hh3cProtocolVlanPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 16, 1, 6, 1)
)
hh3cProtocolVlanPortEntry.setIndexNames(
    (0, "HH3C-PROTOCOL-VLAN-MIB", "hh3cProtocolVlanPortIndex"),
    (0, "HH3C-PROTOCOL-VLAN-MIB", "hh3cProtocolVlanPortVlanId"),
    (0, "HH3C-PROTOCOL-VLAN-MIB", "hh3cProtocolVlanPortProtocolId"),
)
if mibBuilder.loadTexts:
    hh3cProtocolVlanPortEntry.setStatus("current")
_Hh3cProtocolVlanPortIndex_Type = Integer32
_Hh3cProtocolVlanPortIndex_Object = MibTableColumn
hh3cProtocolVlanPortIndex = _Hh3cProtocolVlanPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 16, 1, 6, 1, 1),
    _Hh3cProtocolVlanPortIndex_Type()
)
hh3cProtocolVlanPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cProtocolVlanPortIndex.setStatus("current")
_Hh3cProtocolVlanPortVlanId_Type = Integer32
_Hh3cProtocolVlanPortVlanId_Object = MibTableColumn
hh3cProtocolVlanPortVlanId = _Hh3cProtocolVlanPortVlanId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 16, 1, 6, 1, 2),
    _Hh3cProtocolVlanPortVlanId_Type()
)
hh3cProtocolVlanPortVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cProtocolVlanPortVlanId.setStatus("current")
_Hh3cProtocolVlanPortProtocolId_Type = Integer32
_Hh3cProtocolVlanPortProtocolId_Object = MibTableColumn
hh3cProtocolVlanPortProtocolId = _Hh3cProtocolVlanPortProtocolId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 16, 1, 6, 1, 3),
    _Hh3cProtocolVlanPortProtocolId_Type()
)
hh3cProtocolVlanPortProtocolId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cProtocolVlanPortProtocolId.setStatus("current")
_Hh3cProtocolVlanPortProtocolType_Type = Hh3cvProtocolVlanProtocolType
_Hh3cProtocolVlanPortProtocolType_Object = MibTableColumn
hh3cProtocolVlanPortProtocolType = _Hh3cProtocolVlanPortProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 16, 1, 6, 1, 4),
    _Hh3cProtocolVlanPortProtocolType_Type()
)
hh3cProtocolVlanPortProtocolType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cProtocolVlanPortProtocolType.setStatus("current")
_Hh3cProtocolVlanPortProtocolSubType_Type = Hh3cvProtocolVlanProtocolSubType
_Hh3cProtocolVlanPortProtocolSubType_Object = MibTableColumn
hh3cProtocolVlanPortProtocolSubType = _Hh3cProtocolVlanPortProtocolSubType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 16, 1, 6, 1, 5),
    _Hh3cProtocolVlanPortProtocolSubType_Type()
)
hh3cProtocolVlanPortProtocolSubType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cProtocolVlanPortProtocolSubType.setStatus("current")
_Hh3cProtocolVlanPortTypeValue_Type = OctetString
_Hh3cProtocolVlanPortTypeValue_Object = MibTableColumn
hh3cProtocolVlanPortTypeValue = _Hh3cProtocolVlanPortTypeValue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 16, 1, 6, 1, 6),
    _Hh3cProtocolVlanPortTypeValue_Type()
)
hh3cProtocolVlanPortTypeValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cProtocolVlanPortTypeValue.setStatus("current")
_Hh3cProtocolVlanPortRowStatus_Type = RowStatus
_Hh3cProtocolVlanPortRowStatus_Object = MibTableColumn
hh3cProtocolVlanPortRowStatus = _Hh3cProtocolVlanPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 16, 1, 6, 1, 7),
    _Hh3cProtocolVlanPortRowStatus_Type()
)
hh3cProtocolVlanPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cProtocolVlanPortRowStatus.setStatus("current")
_Hh3cDifferentProtocolNumAllPort_Type = Integer32
_Hh3cDifferentProtocolNumAllPort_Object = MibScalar
hh3cDifferentProtocolNumAllPort = _Hh3cDifferentProtocolNumAllPort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 16, 1, 7),
    _Hh3cDifferentProtocolNumAllPort_Type()
)
hh3cDifferentProtocolNumAllPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDifferentProtocolNumAllPort.setStatus("current")
_Hh3cProtocolVlanConformance_ObjectIdentity = ObjectIdentity
hh3cProtocolVlanConformance = _Hh3cProtocolVlanConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 16, 2)
)
_Hh3cProtocolVlanCompliances_ObjectIdentity = ObjectIdentity
hh3cProtocolVlanCompliances = _Hh3cProtocolVlanCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 16, 2, 1)
)
_Hh3cProtocolVlanGroups_ObjectIdentity = ObjectIdentity
hh3cProtocolVlanGroups = _Hh3cProtocolVlanGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 16, 2, 2)
)

# Managed Objects groups

hh3cProtocolVlanOperateGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25506, 2, 16, 2, 2, 1)
)
hh3cProtocolVlanOperateGroup.setObjects(
      *(("HH3C-PROTOCOL-VLAN-MIB", "hh3cProtocolNumAllVlan"),
        ("HH3C-PROTOCOL-VLAN-MIB", "hh3cProtocolNumPerVlan"),
        ("HH3C-PROTOCOL-VLAN-MIB", "hh3cProtocolNumAllPort"),
        ("HH3C-PROTOCOL-VLAN-MIB", "hh3cProtocolNumPerPort"),
        ("HH3C-PROTOCOL-VLAN-MIB", "hh3cDifferentProtocolNumAllPort"))
)
if mibBuilder.loadTexts:
    hh3cProtocolVlanOperateGroup.setStatus("current")

hh3cProtocolVlanProtocolGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25506, 2, 16, 2, 2, 2)
)
hh3cProtocolVlanProtocolGroup.setObjects(
      *(("HH3C-PROTOCOL-VLAN-MIB", "hh3cProtocolVlanProtocolType"),
        ("HH3C-PROTOCOL-VLAN-MIB", "hh3cProtocolVlanProtocolSubType"),
        ("HH3C-PROTOCOL-VLAN-MIB", "hh3cProtocolVlanProtocolTypeValue"),
        ("HH3C-PROTOCOL-VLAN-MIB", "hh3cProtocolVlanRowStatus"))
)
if mibBuilder.loadTexts:
    hh3cProtocolVlanProtocolGroup.setStatus("current")

hh3cProtocolVlanPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25506, 2, 16, 2, 2, 3)
)
hh3cProtocolVlanPortGroup.setObjects(
      *(("HH3C-PROTOCOL-VLAN-MIB", "hh3cProtocolVlanPortProtocolType"),
        ("HH3C-PROTOCOL-VLAN-MIB", "hh3cProtocolVlanPortProtocolSubType"),
        ("HH3C-PROTOCOL-VLAN-MIB", "hh3cProtocolVlanPortTypeValue"),
        ("HH3C-PROTOCOL-VLAN-MIB", "hh3cProtocolVlanPortRowStatus"))
)
if mibBuilder.loadTexts:
    hh3cProtocolVlanPortGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hh3cProtocolVlanCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 25506, 2, 16, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cProtocolVlanCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-PROTOCOL-VLAN-MIB",
    **{"Hh3cvProtocolVlanProtocolType": Hh3cvProtocolVlanProtocolType,
       "Hh3cvProtocolVlanProtocolSubType": Hh3cvProtocolVlanProtocolSubType,
       "hh3cProtocolVlan": hh3cProtocolVlan,
       "hh3cProtocolVlanOperate": hh3cProtocolVlanOperate,
       "hh3cProtocolNumAllVlan": hh3cProtocolNumAllVlan,
       "hh3cProtocolNumPerVlan": hh3cProtocolNumPerVlan,
       "hh3cProtocolNumAllPort": hh3cProtocolNumAllPort,
       "hh3cProtocolNumPerPort": hh3cProtocolNumPerPort,
       "hh3cProtocolVlanTable": hh3cProtocolVlanTable,
       "hh3cProtocolVlanEntry": hh3cProtocolVlanEntry,
       "hh3cProtocolVlanVlanId": hh3cProtocolVlanVlanId,
       "hh3cProtocolVlanProtocolIndex": hh3cProtocolVlanProtocolIndex,
       "hh3cProtocolVlanProtocolType": hh3cProtocolVlanProtocolType,
       "hh3cProtocolVlanProtocolSubType": hh3cProtocolVlanProtocolSubType,
       "hh3cProtocolVlanProtocolTypeValue": hh3cProtocolVlanProtocolTypeValue,
       "hh3cProtocolVlanRowStatus": hh3cProtocolVlanRowStatus,
       "hh3cProtocolVlanPortTable": hh3cProtocolVlanPortTable,
       "hh3cProtocolVlanPortEntry": hh3cProtocolVlanPortEntry,
       "hh3cProtocolVlanPortIndex": hh3cProtocolVlanPortIndex,
       "hh3cProtocolVlanPortVlanId": hh3cProtocolVlanPortVlanId,
       "hh3cProtocolVlanPortProtocolId": hh3cProtocolVlanPortProtocolId,
       "hh3cProtocolVlanPortProtocolType": hh3cProtocolVlanPortProtocolType,
       "hh3cProtocolVlanPortProtocolSubType": hh3cProtocolVlanPortProtocolSubType,
       "hh3cProtocolVlanPortTypeValue": hh3cProtocolVlanPortTypeValue,
       "hh3cProtocolVlanPortRowStatus": hh3cProtocolVlanPortRowStatus,
       "hh3cDifferentProtocolNumAllPort": hh3cDifferentProtocolNumAllPort,
       "hh3cProtocolVlanConformance": hh3cProtocolVlanConformance,
       "hh3cProtocolVlanCompliances": hh3cProtocolVlanCompliances,
       "hh3cProtocolVlanCompliance": hh3cProtocolVlanCompliance,
       "hh3cProtocolVlanGroups": hh3cProtocolVlanGroups,
       "hh3cProtocolVlanOperateGroup": hh3cProtocolVlanOperateGroup,
       "hh3cProtocolVlanProtocolGroup": hh3cProtocolVlanProtocolGroup,
       "hh3cProtocolVlanPortGroup": hh3cProtocolVlanPortGroup}
)
