# SNMP MIB module (HP-ICF-PROVIDER-BRIDGE) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HP-ICF-PROVIDER-BRIDGE
# Produced by pysmi-1.5.4 at Mon Oct 14 21:58:02 2024
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

(hpSwitch,) = mibBuilder.importSymbols(
    "HP-ICF-OID",
    "hpSwitch")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(dot1qVlanStaticEntry,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "dot1qVlanStaticEntry")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

hpicfProviderBridge = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 40)
)
hpicfProviderBridge.setRevisions(
        ("2008-10-01 00:00",
         "2006-08-15 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpicfProviderBridgeObjects_ObjectIdentity = ObjectIdentity
hpicfProviderBridgeObjects = _HpicfProviderBridgeObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 40, 1)
)
_HpicfProviderBridgeBase_ObjectIdentity = ObjectIdentity
hpicfProviderBridgeBase = _HpicfProviderBridgeBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 40, 1, 1)
)


class _HpicfProviderBridgeType_Type(Integer32):
    """Custom type hpicfProviderBridgeType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("providerEdgeBridge", 3),
          ("svlanBridge", 2),
          ("vlanBridge", 1),
          ("vlanSvlanBridge", 4))
    )


_HpicfProviderBridgeType_Type.__name__ = "Integer32"
_HpicfProviderBridgeType_Object = MibScalar
hpicfProviderBridgeType = _HpicfProviderBridgeType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 40, 1, 1, 1),
    _HpicfProviderBridgeType_Type()
)
hpicfProviderBridgeType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfProviderBridgeType.setStatus("current")


class _HpicfProviderBridgeEtherType_Type(Integer32):
    """Custom type hpicfProviderBridgeEtherType based on Integer32"""
    defaultValue = 34984

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1536, 65535),
    )


_HpicfProviderBridgeEtherType_Type.__name__ = "Integer32"
_HpicfProviderBridgeEtherType_Object = MibScalar
hpicfProviderBridgeEtherType = _HpicfProviderBridgeEtherType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 40, 1, 1, 2),
    _HpicfProviderBridgeEtherType_Type()
)
hpicfProviderBridgeEtherType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfProviderBridgeEtherType.setStatus("current")
_HpicfProviderBridgeVlanTypeTable_Object = MibTable
hpicfProviderBridgeVlanTypeTable = _HpicfProviderBridgeVlanTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 40, 1, 1, 3)
)
if mibBuilder.loadTexts:
    hpicfProviderBridgeVlanTypeTable.setStatus("current")
_HpicfProviderBridgeVlanTypeEntry_Object = MibTableRow
hpicfProviderBridgeVlanTypeEntry = _HpicfProviderBridgeVlanTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 40, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    hpicfProviderBridgeVlanTypeEntry.setStatus("current")


class _HpicfProviderBridgeVlanType_Type(Integer32):
    """Custom type hpicfProviderBridgeVlanType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cvlan", 1),
          ("svlan", 2))
    )


_HpicfProviderBridgeVlanType_Type.__name__ = "Integer32"
_HpicfProviderBridgeVlanType_Object = MibTableColumn
hpicfProviderBridgeVlanType = _HpicfProviderBridgeVlanType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 40, 1, 1, 3, 1, 1),
    _HpicfProviderBridgeVlanType_Type()
)
hpicfProviderBridgeVlanType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfProviderBridgeVlanType.setStatus("current")
_HpicfProviderBridgePortTable_Object = MibTable
hpicfProviderBridgePortTable = _HpicfProviderBridgePortTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 40, 1, 1, 4)
)
if mibBuilder.loadTexts:
    hpicfProviderBridgePortTable.setStatus("current")
_HpicfProviderBridgePortEntry_Object = MibTableRow
hpicfProviderBridgePortEntry = _HpicfProviderBridgePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 40, 1, 1, 4, 1)
)
hpicfProviderBridgePortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpicfProviderBridgePortEntry.setStatus("current")


class _HpicfProviderBridgePortType_Type(Integer32):
    """Custom type hpicfProviderBridgePortType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("customer-edge", 1),
          ("customer-network", 2),
          ("provider-network", 3))
    )


_HpicfProviderBridgePortType_Type.__name__ = "Integer32"
_HpicfProviderBridgePortType_Object = MibTableColumn
hpicfProviderBridgePortType = _HpicfProviderBridgePortType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 40, 1, 1, 4, 1, 1),
    _HpicfProviderBridgePortType_Type()
)
hpicfProviderBridgePortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfProviderBridgePortType.setStatus("current")
_HpicfProviderBridgeConformance_ObjectIdentity = ObjectIdentity
hpicfProviderBridgeConformance = _HpicfProviderBridgeConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 40, 2)
)
_HpicfProviderBridgeGroups_ObjectIdentity = ObjectIdentity
hpicfProviderBridgeGroups = _HpicfProviderBridgeGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 40, 2, 1)
)
_HpicfProviderBridgeCompliances_ObjectIdentity = ObjectIdentity
hpicfProviderBridgeCompliances = _HpicfProviderBridgeCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 40, 2, 2)
)
dot1qVlanStaticEntry.registerAugmentions(
    ("HP-ICF-PROVIDER-BRIDGE",
     "hpicfProviderBridgeVlanTypeEntry")
)
hpicfProviderBridgeVlanTypeEntry.setIndexNames(*dot1qVlanStaticEntry.getIndexNames())

# Managed Objects groups

hpicfProviderBridgeBaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 40, 2, 1, 1)
)
hpicfProviderBridgeBaseGroup.setObjects(
      *(("HP-ICF-PROVIDER-BRIDGE", "hpicfProviderBridgeType"),
        ("HP-ICF-PROVIDER-BRIDGE", "hpicfProviderBridgeEtherType"),
        ("HP-ICF-PROVIDER-BRIDGE", "hpicfProviderBridgePortType"),
        ("HP-ICF-PROVIDER-BRIDGE", "hpicfProviderBridgeVlanType"))
)
if mibBuilder.loadTexts:
    hpicfProviderBridgeBaseGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hpicfProviderBridgeCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 40, 2, 2, 1)
)
if mibBuilder.loadTexts:
    hpicfProviderBridgeCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HP-ICF-PROVIDER-BRIDGE",
    **{"hpicfProviderBridge": hpicfProviderBridge,
       "hpicfProviderBridgeObjects": hpicfProviderBridgeObjects,
       "hpicfProviderBridgeBase": hpicfProviderBridgeBase,
       "hpicfProviderBridgeType": hpicfProviderBridgeType,
       "hpicfProviderBridgeEtherType": hpicfProviderBridgeEtherType,
       "hpicfProviderBridgeVlanTypeTable": hpicfProviderBridgeVlanTypeTable,
       "hpicfProviderBridgeVlanTypeEntry": hpicfProviderBridgeVlanTypeEntry,
       "hpicfProviderBridgeVlanType": hpicfProviderBridgeVlanType,
       "hpicfProviderBridgePortTable": hpicfProviderBridgePortTable,
       "hpicfProviderBridgePortEntry": hpicfProviderBridgePortEntry,
       "hpicfProviderBridgePortType": hpicfProviderBridgePortType,
       "hpicfProviderBridgeConformance": hpicfProviderBridgeConformance,
       "hpicfProviderBridgeGroups": hpicfProviderBridgeGroups,
       "hpicfProviderBridgeBaseGroup": hpicfProviderBridgeBaseGroup,
       "hpicfProviderBridgeCompliances": hpicfProviderBridgeCompliances,
       "hpicfProviderBridgeCompliance": hpicfProviderBridgeCompliance}
)
