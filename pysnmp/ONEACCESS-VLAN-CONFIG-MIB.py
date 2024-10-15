# SNMP MIB module (ONEACCESS-VLAN-CONFIG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ONEACCESS-VLAN-CONFIG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:35:07 2024
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

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(oacExpIMIp,
 oacMIBModules) = mibBuilder.importSymbols(
    "ONEACCESS-GLOBAL-REG",
    "oacExpIMIp",
    "oacMIBModules")

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

oaVlanConfigMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 1, 100, 681)
)
oaVlanConfigMIB.setRevisions(
        ("2011-06-15 00:00",
         "2010-07-08 00:01")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class SPVlanEtherType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("etherType-8100", 1),
          ("etherType-88a8", 3),
          ("etherType-9100", 2))
    )



# MIB Managed Objects in the order of their OIDs

_OacVlanConfig_ObjectIdentity = ObjectIdentity
oacVlanConfig = _OacVlanConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 6)
)
_OacVlanConfigObjects_ObjectIdentity = ObjectIdentity
oacVlanConfigObjects = _OacVlanConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 6, 1)
)
_OacVlanMappingConfigInterfaceObjects_ObjectIdentity = ObjectIdentity
oacVlanMappingConfigInterfaceObjects = _OacVlanMappingConfigInterfaceObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 6, 1, 1)
)
_OacVlanConfigInterfaceTable_Object = MibTable
oacVlanConfigInterfaceTable = _OacVlanConfigInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 6, 1, 1, 1)
)
if mibBuilder.loadTexts:
    oacVlanConfigInterfaceTable.setStatus("current")
_OacVlanConfigInterfaceEntry_Object = MibTableRow
oacVlanConfigInterfaceEntry = _OacVlanConfigInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 6, 1, 1, 1, 1)
)
oacVlanConfigInterfaceEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    oacVlanConfigInterfaceEntry.setStatus("current")


class _OacVlanConfigInterfaceDot1qValue_Type(Integer32):
    """Custom type oacVlanConfigInterfaceDot1qValue based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_OacVlanConfigInterfaceDot1qValue_Type.__name__ = "Integer32"
_OacVlanConfigInterfaceDot1qValue_Object = MibTableColumn
oacVlanConfigInterfaceDot1qValue = _OacVlanConfigInterfaceDot1qValue_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 6, 1, 1, 1, 1, 1),
    _OacVlanConfigInterfaceDot1qValue_Type()
)
oacVlanConfigInterfaceDot1qValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oacVlanConfigInterfaceDot1qValue.setStatus("current")


class _OacVlanConfigInterfaceSecondDot1qValue_Type(Integer32):
    """Custom type oacVlanConfigInterfaceSecondDot1qValue based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_OacVlanConfigInterfaceSecondDot1qValue_Type.__name__ = "Integer32"
_OacVlanConfigInterfaceSecondDot1qValue_Object = MibTableColumn
oacVlanConfigInterfaceSecondDot1qValue = _OacVlanConfigInterfaceSecondDot1qValue_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 6, 1, 1, 1, 1, 2),
    _OacVlanConfigInterfaceSecondDot1qValue_Type()
)
oacVlanConfigInterfaceSecondDot1qValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oacVlanConfigInterfaceSecondDot1qValue.setStatus("current")


class _OacVlanConfigInterfaceDefaultPriority_Type(Integer32):
    """Custom type oacVlanConfigInterfaceDefaultPriority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_OacVlanConfigInterfaceDefaultPriority_Type.__name__ = "Integer32"
_OacVlanConfigInterfaceDefaultPriority_Object = MibTableColumn
oacVlanConfigInterfaceDefaultPriority = _OacVlanConfigInterfaceDefaultPriority_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 6, 1, 1, 1, 1, 3),
    _OacVlanConfigInterfaceDefaultPriority_Type()
)
oacVlanConfigInterfaceDefaultPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oacVlanConfigInterfaceDefaultPriority.setStatus("current")
_OacVlanConfigInterfaceRowStatus_Type = RowStatus
_OacVlanConfigInterfaceRowStatus_Object = MibTableColumn
oacVlanConfigInterfaceRowStatus = _OacVlanConfigInterfaceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 6, 1, 1, 1, 1, 4),
    _OacVlanConfigInterfaceRowStatus_Type()
)
oacVlanConfigInterfaceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oacVlanConfigInterfaceRowStatus.setStatus("current")
_OacVlanMappingConfigObjects_ObjectIdentity = ObjectIdentity
oacVlanMappingConfigObjects = _OacVlanMappingConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 6, 1, 2)
)
_VlanMappingTable_Object = MibTable
vlanMappingTable = _VlanMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 6, 1, 2, 1)
)
if mibBuilder.loadTexts:
    vlanMappingTable.setStatus("current")
_VlanMappingEntry_Object = MibTableRow
vlanMappingEntry = _VlanMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 6, 1, 2, 1, 1)
)
vlanMappingEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ONEACCESS-VLAN-CONFIG-MIB", "outerSPVlan"),
)
if mibBuilder.loadTexts:
    vlanMappingEntry.setStatus("current")


class _InnerCVlan_Type(OctetString):
    """Custom type innerCVlan based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 100),
    )


_InnerCVlan_Type.__name__ = "OctetString"
_InnerCVlan_Object = MibTableColumn
innerCVlan = _InnerCVlan_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 6, 1, 2, 1, 1, 1),
    _InnerCVlan_Type()
)
innerCVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    innerCVlan.setStatus("current")


class _OuterSPVlan_Type(Unsigned32):
    """Custom type outerSPVlan based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_OuterSPVlan_Type.__name__ = "Unsigned32"
_OuterSPVlan_Object = MibTableColumn
outerSPVlan = _OuterSPVlan_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 6, 1, 2, 1, 1, 2),
    _OuterSPVlan_Type()
)
outerSPVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    outerSPVlan.setStatus("current")
_OuterEtherType_Type = SPVlanEtherType
_OuterEtherType_Object = MibTableColumn
outerEtherType = _OuterEtherType_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 6, 1, 2, 1, 1, 3),
    _OuterEtherType_Type()
)
outerEtherType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    outerEtherType.setStatus("current")
_VlanMappingRowStatus_Type = RowStatus
_VlanMappingRowStatus_Object = MibTableColumn
vlanMappingRowStatus = _VlanMappingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 6, 1, 2, 1, 1, 4),
    _VlanMappingRowStatus_Type()
)
vlanMappingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanMappingRowStatus.setStatus("current")
_OacVlanConfigConformance_ObjectIdentity = ObjectIdentity
oacVlanConfigConformance = _OacVlanConfigConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 6, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ONEACCESS-VLAN-CONFIG-MIB",
    **{"SPVlanEtherType": SPVlanEtherType,
       "oaVlanConfigMIB": oaVlanConfigMIB,
       "oacVlanConfig": oacVlanConfig,
       "oacVlanConfigObjects": oacVlanConfigObjects,
       "oacVlanMappingConfigInterfaceObjects": oacVlanMappingConfigInterfaceObjects,
       "oacVlanConfigInterfaceTable": oacVlanConfigInterfaceTable,
       "oacVlanConfigInterfaceEntry": oacVlanConfigInterfaceEntry,
       "oacVlanConfigInterfaceDot1qValue": oacVlanConfigInterfaceDot1qValue,
       "oacVlanConfigInterfaceSecondDot1qValue": oacVlanConfigInterfaceSecondDot1qValue,
       "oacVlanConfigInterfaceDefaultPriority": oacVlanConfigInterfaceDefaultPriority,
       "oacVlanConfigInterfaceRowStatus": oacVlanConfigInterfaceRowStatus,
       "oacVlanMappingConfigObjects": oacVlanMappingConfigObjects,
       "vlanMappingTable": vlanMappingTable,
       "vlanMappingEntry": vlanMappingEntry,
       "innerCVlan": innerCVlan,
       "outerSPVlan": outerSPVlan,
       "outerEtherType": outerEtherType,
       "vlanMappingRowStatus": vlanMappingRowStatus,
       "oacVlanConfigConformance": oacVlanConfigConformance}
)
