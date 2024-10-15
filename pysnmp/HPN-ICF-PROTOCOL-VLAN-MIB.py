# SNMP MIB module (HPN-ICF-PROTOCOL-VLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-PROTOCOL-VLAN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:01:33 2024
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

hpnicfProtocolVlan = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 16)
)
hpnicfProtocolVlan.setRevisions(
        ("2004-08-31 19:38",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class HpnicfvProtocolVlanProtocolType(Integer32, TextualConvention):
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
              103,
              201)
        )
    )
    namedValues = NamedValues(
        *(("at", 3),
          ("ip", 1),
          ("ipv6", 4),
          ("ipx", 2),
          ("mode-ethernetii", 103),
          ("mode-llc", 101),
          ("mode-snap", 102),
          ("notConfigure", 201))
    )



class HpnicfvProtocolVlanProtocolSubType(Integer32, TextualConvention):
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

_HpnicfProtocolVlanOperate_ObjectIdentity = ObjectIdentity
hpnicfProtocolVlanOperate = _HpnicfProtocolVlanOperate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 16, 1)
)
_HpnicfProtocolNumAllVlan_Type = Integer32
_HpnicfProtocolNumAllVlan_Object = MibScalar
hpnicfProtocolNumAllVlan = _HpnicfProtocolNumAllVlan_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 16, 1, 1),
    _HpnicfProtocolNumAllVlan_Type()
)
hpnicfProtocolNumAllVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfProtocolNumAllVlan.setStatus("current")
_HpnicfProtocolNumPerVlan_Type = Integer32
_HpnicfProtocolNumPerVlan_Object = MibScalar
hpnicfProtocolNumPerVlan = _HpnicfProtocolNumPerVlan_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 16, 1, 2),
    _HpnicfProtocolNumPerVlan_Type()
)
hpnicfProtocolNumPerVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfProtocolNumPerVlan.setStatus("current")
_HpnicfProtocolNumAllPort_Type = Integer32
_HpnicfProtocolNumAllPort_Object = MibScalar
hpnicfProtocolNumAllPort = _HpnicfProtocolNumAllPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 16, 1, 3),
    _HpnicfProtocolNumAllPort_Type()
)
hpnicfProtocolNumAllPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfProtocolNumAllPort.setStatus("current")
_HpnicfProtocolNumPerPort_Type = Integer32
_HpnicfProtocolNumPerPort_Object = MibScalar
hpnicfProtocolNumPerPort = _HpnicfProtocolNumPerPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 16, 1, 4),
    _HpnicfProtocolNumPerPort_Type()
)
hpnicfProtocolNumPerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfProtocolNumPerPort.setStatus("current")
_HpnicfProtocolVlanTable_Object = MibTable
hpnicfProtocolVlanTable = _HpnicfProtocolVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 16, 1, 5)
)
if mibBuilder.loadTexts:
    hpnicfProtocolVlanTable.setStatus("current")
_HpnicfProtocolVlanEntry_Object = MibTableRow
hpnicfProtocolVlanEntry = _HpnicfProtocolVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 16, 1, 5, 1)
)
hpnicfProtocolVlanEntry.setIndexNames(
    (0, "HPN-ICF-PROTOCOL-VLAN-MIB", "hpnicfProtocolVlanVlanId"),
    (0, "HPN-ICF-PROTOCOL-VLAN-MIB", "hpnicfProtocolVlanProtocolIndex"),
)
if mibBuilder.loadTexts:
    hpnicfProtocolVlanEntry.setStatus("current")
_HpnicfProtocolVlanVlanId_Type = Integer32
_HpnicfProtocolVlanVlanId_Object = MibTableColumn
hpnicfProtocolVlanVlanId = _HpnicfProtocolVlanVlanId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 16, 1, 5, 1, 1),
    _HpnicfProtocolVlanVlanId_Type()
)
hpnicfProtocolVlanVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfProtocolVlanVlanId.setStatus("current")
_HpnicfProtocolVlanProtocolIndex_Type = Integer32
_HpnicfProtocolVlanProtocolIndex_Object = MibTableColumn
hpnicfProtocolVlanProtocolIndex = _HpnicfProtocolVlanProtocolIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 16, 1, 5, 1, 2),
    _HpnicfProtocolVlanProtocolIndex_Type()
)
hpnicfProtocolVlanProtocolIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfProtocolVlanProtocolIndex.setStatus("current")
_HpnicfProtocolVlanProtocolType_Type = HpnicfvProtocolVlanProtocolType
_HpnicfProtocolVlanProtocolType_Object = MibTableColumn
hpnicfProtocolVlanProtocolType = _HpnicfProtocolVlanProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 16, 1, 5, 1, 3),
    _HpnicfProtocolVlanProtocolType_Type()
)
hpnicfProtocolVlanProtocolType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfProtocolVlanProtocolType.setStatus("current")
_HpnicfProtocolVlanProtocolSubType_Type = HpnicfvProtocolVlanProtocolSubType
_HpnicfProtocolVlanProtocolSubType_Object = MibTableColumn
hpnicfProtocolVlanProtocolSubType = _HpnicfProtocolVlanProtocolSubType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 16, 1, 5, 1, 4),
    _HpnicfProtocolVlanProtocolSubType_Type()
)
hpnicfProtocolVlanProtocolSubType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfProtocolVlanProtocolSubType.setStatus("current")


class _HpnicfProtocolVlanProtocolTypeValue_Type(OctetString):
    """Custom type hpnicfProtocolVlanProtocolTypeValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnicfProtocolVlanProtocolTypeValue_Type.__name__ = "OctetString"
_HpnicfProtocolVlanProtocolTypeValue_Object = MibTableColumn
hpnicfProtocolVlanProtocolTypeValue = _HpnicfProtocolVlanProtocolTypeValue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 16, 1, 5, 1, 5),
    _HpnicfProtocolVlanProtocolTypeValue_Type()
)
hpnicfProtocolVlanProtocolTypeValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfProtocolVlanProtocolTypeValue.setStatus("current")
_HpnicfProtocolVlanRowStatus_Type = RowStatus
_HpnicfProtocolVlanRowStatus_Object = MibTableColumn
hpnicfProtocolVlanRowStatus = _HpnicfProtocolVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 16, 1, 5, 1, 6),
    _HpnicfProtocolVlanRowStatus_Type()
)
hpnicfProtocolVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfProtocolVlanRowStatus.setStatus("current")
_HpnicfProtocolVlanPortTable_Object = MibTable
hpnicfProtocolVlanPortTable = _HpnicfProtocolVlanPortTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 16, 1, 6)
)
if mibBuilder.loadTexts:
    hpnicfProtocolVlanPortTable.setStatus("current")
_HpnicfProtocolVlanPortEntry_Object = MibTableRow
hpnicfProtocolVlanPortEntry = _HpnicfProtocolVlanPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 16, 1, 6, 1)
)
hpnicfProtocolVlanPortEntry.setIndexNames(
    (0, "HPN-ICF-PROTOCOL-VLAN-MIB", "hpnicfProtocolVlanPortIndex"),
    (0, "HPN-ICF-PROTOCOL-VLAN-MIB", "hpnicfProtocolVlanPortVlanId"),
    (0, "HPN-ICF-PROTOCOL-VLAN-MIB", "hpnicfProtocolVlanPortProtocolId"),
)
if mibBuilder.loadTexts:
    hpnicfProtocolVlanPortEntry.setStatus("current")
_HpnicfProtocolVlanPortIndex_Type = Integer32
_HpnicfProtocolVlanPortIndex_Object = MibTableColumn
hpnicfProtocolVlanPortIndex = _HpnicfProtocolVlanPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 16, 1, 6, 1, 1),
    _HpnicfProtocolVlanPortIndex_Type()
)
hpnicfProtocolVlanPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfProtocolVlanPortIndex.setStatus("current")
_HpnicfProtocolVlanPortVlanId_Type = Integer32
_HpnicfProtocolVlanPortVlanId_Object = MibTableColumn
hpnicfProtocolVlanPortVlanId = _HpnicfProtocolVlanPortVlanId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 16, 1, 6, 1, 2),
    _HpnicfProtocolVlanPortVlanId_Type()
)
hpnicfProtocolVlanPortVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfProtocolVlanPortVlanId.setStatus("current")
_HpnicfProtocolVlanPortProtocolId_Type = Integer32
_HpnicfProtocolVlanPortProtocolId_Object = MibTableColumn
hpnicfProtocolVlanPortProtocolId = _HpnicfProtocolVlanPortProtocolId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 16, 1, 6, 1, 3),
    _HpnicfProtocolVlanPortProtocolId_Type()
)
hpnicfProtocolVlanPortProtocolId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfProtocolVlanPortProtocolId.setStatus("current")
_HpnicfProtocolVlanPortProtocolType_Type = HpnicfvProtocolVlanProtocolType
_HpnicfProtocolVlanPortProtocolType_Object = MibTableColumn
hpnicfProtocolVlanPortProtocolType = _HpnicfProtocolVlanPortProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 16, 1, 6, 1, 4),
    _HpnicfProtocolVlanPortProtocolType_Type()
)
hpnicfProtocolVlanPortProtocolType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfProtocolVlanPortProtocolType.setStatus("current")
_HpnicfProtocolVlanPortProtocolSubType_Type = HpnicfvProtocolVlanProtocolSubType
_HpnicfProtocolVlanPortProtocolSubType_Object = MibTableColumn
hpnicfProtocolVlanPortProtocolSubType = _HpnicfProtocolVlanPortProtocolSubType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 16, 1, 6, 1, 5),
    _HpnicfProtocolVlanPortProtocolSubType_Type()
)
hpnicfProtocolVlanPortProtocolSubType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfProtocolVlanPortProtocolSubType.setStatus("current")
_HpnicfProtocolVlanPortTypeValue_Type = OctetString
_HpnicfProtocolVlanPortTypeValue_Object = MibTableColumn
hpnicfProtocolVlanPortTypeValue = _HpnicfProtocolVlanPortTypeValue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 16, 1, 6, 1, 6),
    _HpnicfProtocolVlanPortTypeValue_Type()
)
hpnicfProtocolVlanPortTypeValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfProtocolVlanPortTypeValue.setStatus("current")
_HpnicfProtocolVlanPortRowStatus_Type = RowStatus
_HpnicfProtocolVlanPortRowStatus_Object = MibTableColumn
hpnicfProtocolVlanPortRowStatus = _HpnicfProtocolVlanPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 16, 1, 6, 1, 7),
    _HpnicfProtocolVlanPortRowStatus_Type()
)
hpnicfProtocolVlanPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfProtocolVlanPortRowStatus.setStatus("current")


class _HpnicfProtocolVlanPortStatus_Type(Integer32):
    """Custom type hpnicfProtocolVlanPortStatus based on Integer32"""
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


_HpnicfProtocolVlanPortStatus_Type.__name__ = "Integer32"
_HpnicfProtocolVlanPortStatus_Object = MibTableColumn
hpnicfProtocolVlanPortStatus = _HpnicfProtocolVlanPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 16, 1, 6, 1, 8),
    _HpnicfProtocolVlanPortStatus_Type()
)
hpnicfProtocolVlanPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfProtocolVlanPortStatus.setStatus("current")
_HpnicfDifferentProtocolNumAllPort_Type = Integer32
_HpnicfDifferentProtocolNumAllPort_Object = MibScalar
hpnicfDifferentProtocolNumAllPort = _HpnicfDifferentProtocolNumAllPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 16, 1, 7),
    _HpnicfDifferentProtocolNumAllPort_Type()
)
hpnicfDifferentProtocolNumAllPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDifferentProtocolNumAllPort.setStatus("current")
_HpnicfProtocolVlanConformance_ObjectIdentity = ObjectIdentity
hpnicfProtocolVlanConformance = _HpnicfProtocolVlanConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 16, 2)
)
_HpnicfProtocolVlanCompliances_ObjectIdentity = ObjectIdentity
hpnicfProtocolVlanCompliances = _HpnicfProtocolVlanCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 16, 2, 1)
)
_HpnicfProtocolVlanGroups_ObjectIdentity = ObjectIdentity
hpnicfProtocolVlanGroups = _HpnicfProtocolVlanGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 16, 2, 2)
)

# Managed Objects groups

hpnicfProtocolVlanOperateGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 16, 2, 2, 1)
)
hpnicfProtocolVlanOperateGroup.setObjects(
      *(("HPN-ICF-PROTOCOL-VLAN-MIB", "hpnicfProtocolNumAllVlan"),
        ("HPN-ICF-PROTOCOL-VLAN-MIB", "hpnicfProtocolNumPerVlan"),
        ("HPN-ICF-PROTOCOL-VLAN-MIB", "hpnicfProtocolNumAllPort"),
        ("HPN-ICF-PROTOCOL-VLAN-MIB", "hpnicfProtocolNumPerPort"),
        ("HPN-ICF-PROTOCOL-VLAN-MIB", "hpnicfDifferentProtocolNumAllPort"))
)
if mibBuilder.loadTexts:
    hpnicfProtocolVlanOperateGroup.setStatus("current")

hpnicfProtocolVlanProtocolGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 16, 2, 2, 2)
)
hpnicfProtocolVlanProtocolGroup.setObjects(
      *(("HPN-ICF-PROTOCOL-VLAN-MIB", "hpnicfProtocolVlanProtocolType"),
        ("HPN-ICF-PROTOCOL-VLAN-MIB", "hpnicfProtocolVlanProtocolSubType"),
        ("HPN-ICF-PROTOCOL-VLAN-MIB", "hpnicfProtocolVlanProtocolTypeValue"),
        ("HPN-ICF-PROTOCOL-VLAN-MIB", "hpnicfProtocolVlanRowStatus"))
)
if mibBuilder.loadTexts:
    hpnicfProtocolVlanProtocolGroup.setStatus("current")

hpnicfProtocolVlanPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 16, 2, 2, 3)
)
hpnicfProtocolVlanPortGroup.setObjects(
      *(("HPN-ICF-PROTOCOL-VLAN-MIB", "hpnicfProtocolVlanPortProtocolType"),
        ("HPN-ICF-PROTOCOL-VLAN-MIB", "hpnicfProtocolVlanPortProtocolSubType"),
        ("HPN-ICF-PROTOCOL-VLAN-MIB", "hpnicfProtocolVlanPortTypeValue"),
        ("HPN-ICF-PROTOCOL-VLAN-MIB", "hpnicfProtocolVlanPortRowStatus"))
)
if mibBuilder.loadTexts:
    hpnicfProtocolVlanPortGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hpnicfProtocolVlanCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 16, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hpnicfProtocolVlanCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-PROTOCOL-VLAN-MIB",
    **{"HpnicfvProtocolVlanProtocolType": HpnicfvProtocolVlanProtocolType,
       "HpnicfvProtocolVlanProtocolSubType": HpnicfvProtocolVlanProtocolSubType,
       "hpnicfProtocolVlan": hpnicfProtocolVlan,
       "hpnicfProtocolVlanOperate": hpnicfProtocolVlanOperate,
       "hpnicfProtocolNumAllVlan": hpnicfProtocolNumAllVlan,
       "hpnicfProtocolNumPerVlan": hpnicfProtocolNumPerVlan,
       "hpnicfProtocolNumAllPort": hpnicfProtocolNumAllPort,
       "hpnicfProtocolNumPerPort": hpnicfProtocolNumPerPort,
       "hpnicfProtocolVlanTable": hpnicfProtocolVlanTable,
       "hpnicfProtocolVlanEntry": hpnicfProtocolVlanEntry,
       "hpnicfProtocolVlanVlanId": hpnicfProtocolVlanVlanId,
       "hpnicfProtocolVlanProtocolIndex": hpnicfProtocolVlanProtocolIndex,
       "hpnicfProtocolVlanProtocolType": hpnicfProtocolVlanProtocolType,
       "hpnicfProtocolVlanProtocolSubType": hpnicfProtocolVlanProtocolSubType,
       "hpnicfProtocolVlanProtocolTypeValue": hpnicfProtocolVlanProtocolTypeValue,
       "hpnicfProtocolVlanRowStatus": hpnicfProtocolVlanRowStatus,
       "hpnicfProtocolVlanPortTable": hpnicfProtocolVlanPortTable,
       "hpnicfProtocolVlanPortEntry": hpnicfProtocolVlanPortEntry,
       "hpnicfProtocolVlanPortIndex": hpnicfProtocolVlanPortIndex,
       "hpnicfProtocolVlanPortVlanId": hpnicfProtocolVlanPortVlanId,
       "hpnicfProtocolVlanPortProtocolId": hpnicfProtocolVlanPortProtocolId,
       "hpnicfProtocolVlanPortProtocolType": hpnicfProtocolVlanPortProtocolType,
       "hpnicfProtocolVlanPortProtocolSubType": hpnicfProtocolVlanPortProtocolSubType,
       "hpnicfProtocolVlanPortTypeValue": hpnicfProtocolVlanPortTypeValue,
       "hpnicfProtocolVlanPortRowStatus": hpnicfProtocolVlanPortRowStatus,
       "hpnicfProtocolVlanPortStatus": hpnicfProtocolVlanPortStatus,
       "hpnicfDifferentProtocolNumAllPort": hpnicfDifferentProtocolNumAllPort,
       "hpnicfProtocolVlanConformance": hpnicfProtocolVlanConformance,
       "hpnicfProtocolVlanCompliances": hpnicfProtocolVlanCompliances,
       "hpnicfProtocolVlanCompliance": hpnicfProtocolVlanCompliance,
       "hpnicfProtocolVlanGroups": hpnicfProtocolVlanGroups,
       "hpnicfProtocolVlanOperateGroup": hpnicfProtocolVlanOperateGroup,
       "hpnicfProtocolVlanProtocolGroup": hpnicfProtocolVlanProtocolGroup,
       "hpnicfProtocolVlanPortGroup": hpnicfProtocolVlanPortGroup}
)
