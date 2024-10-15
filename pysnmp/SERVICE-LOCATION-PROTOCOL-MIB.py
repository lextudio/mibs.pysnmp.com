# SNMP MIB module (SERVICE-LOCATION-PROTOCOL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SERVICE-LOCATION-PROTOCOL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:50:23 2024
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

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DisplayString,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

slpMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 999)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class SlpAgentTypeTC(Integer32, TextualConvention):
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
        *(("da", 1),
          ("sa", 2),
          ("ua", 3))
    )



class SlpScopeSourceTC(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("default", 7),
          ("dhcp", 3),
          ("dhcpDA", 4),
          ("dynamicDA", 5),
          ("dynamicSA", 6),
          ("static", 1),
          ("staticDA", 2))
    )



class SlpAttributeTypeTC(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("attrBoolean", 1),
          ("attrInteger", 2),
          ("attrKeyword", 5),
          ("attrOpaque", 4),
          ("attrString", 3))
    )



# MIB Managed Objects in the order of their OIDs

_SlpMIBObjects_ObjectIdentity = ObjectIdentity
slpMIBObjects = _SlpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 999, 1)
)
_SlpAgent_ObjectIdentity = ObjectIdentity
slpAgent = _SlpAgent_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 999, 1, 1)
)
_SlpAgentTable_Object = MibTable
slpAgentTable = _SlpAgentTable_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 1, 1)
)
if mibBuilder.loadTexts:
    slpAgentTable.setStatus("current")
_SlpAgentEntry_Object = MibTableRow
slpAgentEntry = _SlpAgentEntry_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 1, 1, 1)
)
slpAgentEntry.setIndexNames(
    (0, "SERVICE-LOCATION-PROTOCOL-MIB", "slpAgentIndex"),
)
if mibBuilder.loadTexts:
    slpAgentEntry.setStatus("current")


class _SlpAgentIndex_Type(Integer32):
    """Custom type slpAgentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SlpAgentIndex_Type.__name__ = "Integer32"
_SlpAgentIndex_Object = MibTableColumn
slpAgentIndex = _SlpAgentIndex_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 1, 1, 1, 1),
    _SlpAgentIndex_Type()
)
slpAgentIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    slpAgentIndex.setStatus("current")


class _SlpAgentSWInstalledIndexOrZero_Type(Integer32):
    """Custom type slpAgentSWInstalledIndexOrZero based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SlpAgentSWInstalledIndexOrZero_Type.__name__ = "Integer32"
_SlpAgentSWInstalledIndexOrZero_Object = MibTableColumn
slpAgentSWInstalledIndexOrZero = _SlpAgentSWInstalledIndexOrZero_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 1, 1, 1, 2),
    _SlpAgentSWInstalledIndexOrZero_Type()
)
slpAgentSWInstalledIndexOrZero.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slpAgentSWInstalledIndexOrZero.setStatus("current")


class _SlpAgentName_Type(SnmpAdminString):
    """Custom type slpAgentName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SlpAgentName_Type.__name__ = "SnmpAdminString"
_SlpAgentName_Object = MibTableColumn
slpAgentName = _SlpAgentName_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 1, 1, 1, 3),
    _SlpAgentName_Type()
)
slpAgentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slpAgentName.setStatus("current")
_SlpAgentType_Type = SlpAgentTypeTC
_SlpAgentType_Object = MibTableColumn
slpAgentType = _SlpAgentType_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 1, 1, 1, 4),
    _SlpAgentType_Type()
)
slpAgentType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slpAgentType.setStatus("current")


class _SlpAgentIsBroadcastOnly_Type(TruthValue):
    """Custom type slpAgentIsBroadcastOnly based on TruthValue"""


_SlpAgentIsBroadcastOnly_Object = MibTableColumn
slpAgentIsBroadcastOnly = _SlpAgentIsBroadcastOnly_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 1, 1, 1, 5),
    _SlpAgentIsBroadcastOnly_Type()
)
slpAgentIsBroadcastOnly.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slpAgentIsBroadcastOnly.setStatus("current")


class _SlpAgentActiveDADiscovery_Type(TruthValue):
    """Custom type slpAgentActiveDADiscovery based on TruthValue"""


_SlpAgentActiveDADiscovery_Object = MibTableColumn
slpAgentActiveDADiscovery = _SlpAgentActiveDADiscovery_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 1, 1, 1, 6),
    _SlpAgentActiveDADiscovery_Type()
)
slpAgentActiveDADiscovery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slpAgentActiveDADiscovery.setStatus("current")


class _SlpAgentPassiveDADiscovery_Type(TruthValue):
    """Custom type slpAgentPassiveDADiscovery based on TruthValue"""


_SlpAgentPassiveDADiscovery_Object = MibTableColumn
slpAgentPassiveDADiscovery = _SlpAgentPassiveDADiscovery_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 1, 1, 1, 7),
    _SlpAgentPassiveDADiscovery_Type()
)
slpAgentPassiveDADiscovery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slpAgentPassiveDADiscovery.setStatus("current")


class _SlpAgentMessageTypesSupported_Type(OctetString):
    """Custom type slpAgentMessageTypesSupported based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SlpAgentMessageTypesSupported_Type.__name__ = "OctetString"
_SlpAgentMessageTypesSupported_Object = MibTableColumn
slpAgentMessageTypesSupported = _SlpAgentMessageTypesSupported_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 1, 1, 1, 8),
    _SlpAgentMessageTypesSupported_Type()
)
slpAgentMessageTypesSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slpAgentMessageTypesSupported.setStatus("current")


class _SlpAgentExtensionsSupported_Type(OctetString):
    """Custom type slpAgentExtensionsSupported based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SlpAgentExtensionsSupported_Type.__name__ = "OctetString"
_SlpAgentExtensionsSupported_Object = MibTableColumn
slpAgentExtensionsSupported = _SlpAgentExtensionsSupported_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 1, 1, 1, 9),
    _SlpAgentExtensionsSupported_Type()
)
slpAgentExtensionsSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slpAgentExtensionsSupported.setStatus("current")
_SlpScope_ObjectIdentity = ObjectIdentity
slpScope = _SlpScope_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 999, 1, 2)
)
_SlpScopeTable_Object = MibTable
slpScopeTable = _SlpScopeTable_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 2, 1)
)
if mibBuilder.loadTexts:
    slpScopeTable.setStatus("current")
_SlpScopeEntry_Object = MibTableRow
slpScopeEntry = _SlpScopeEntry_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 2, 1, 1)
)
slpScopeEntry.setIndexNames(
    (0, "SERVICE-LOCATION-PROTOCOL-MIB", "slpAgentIndex"),
    (0, "SERVICE-LOCATION-PROTOCOL-MIB", "slpScopeIndex"),
)
if mibBuilder.loadTexts:
    slpScopeEntry.setStatus("current")


class _SlpScopeIndex_Type(Integer32):
    """Custom type slpScopeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SlpScopeIndex_Type.__name__ = "Integer32"
_SlpScopeIndex_Object = MibTableColumn
slpScopeIndex = _SlpScopeIndex_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 2, 1, 1, 1),
    _SlpScopeIndex_Type()
)
slpScopeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    slpScopeIndex.setStatus("current")
_SlpScopeSource_Type = SlpScopeSourceTC
_SlpScopeSource_Object = MibTableColumn
slpScopeSource = _SlpScopeSource_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 2, 1, 1, 2),
    _SlpScopeSource_Type()
)
slpScopeSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slpScopeSource.setStatus("current")


class _SlpScopeValue_Type(SnmpAdminString):
    """Custom type slpScopeValue based on SnmpAdminString"""
    defaultHexValue = ""

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SlpScopeValue_Type.__name__ = "SnmpAdminString"
_SlpScopeValue_Object = MibTableColumn
slpScopeValue = _SlpScopeValue_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 2, 1, 1, 3),
    _SlpScopeValue_Type()
)
slpScopeValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slpScopeValue.setStatus("current")
_SlpAddress_ObjectIdentity = ObjectIdentity
slpAddress = _SlpAddress_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 999, 1, 3)
)
_SlpAddressTable_Object = MibTable
slpAddressTable = _SlpAddressTable_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 3, 1)
)
if mibBuilder.loadTexts:
    slpAddressTable.setStatus("current")
_SlpAddressEntry_Object = MibTableRow
slpAddressEntry = _SlpAddressEntry_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 3, 1, 1)
)
slpAddressEntry.setIndexNames(
    (0, "SERVICE-LOCATION-PROTOCOL-MIB", "slpAgentIndex"),
    (0, "SERVICE-LOCATION-PROTOCOL-MIB", "slpAddressIndex"),
)
if mibBuilder.loadTexts:
    slpAddressEntry.setStatus("current")


class _SlpAddressIndex_Type(Integer32):
    """Custom type slpAddressIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SlpAddressIndex_Type.__name__ = "Integer32"
_SlpAddressIndex_Object = MibTableColumn
slpAddressIndex = _SlpAddressIndex_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 3, 1, 1, 1),
    _SlpAddressIndex_Type()
)
slpAddressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    slpAddressIndex.setStatus("current")
_SlpAddressAgentType_Type = SlpAgentTypeTC
_SlpAddressAgentType_Object = MibTableColumn
slpAddressAgentType = _SlpAddressAgentType_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 3, 1, 1, 2),
    _SlpAddressAgentType_Type()
)
slpAddressAgentType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slpAddressAgentType.setStatus("current")
_SlpAddressSource_Type = SlpScopeSourceTC
_SlpAddressSource_Object = MibTableColumn
slpAddressSource = _SlpAddressSource_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 3, 1, 1, 3),
    _SlpAddressSource_Type()
)
slpAddressSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slpAddressSource.setStatus("current")


class _SlpAddressOrName_Type(SnmpAdminString):
    """Custom type slpAddressOrName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SlpAddressOrName_Type.__name__ = "SnmpAdminString"
_SlpAddressOrName_Object = MibTableColumn
slpAddressOrName = _SlpAddressOrName_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 3, 1, 1, 4),
    _SlpAddressOrName_Type()
)
slpAddressOrName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slpAddressOrName.setStatus("current")
_SlpAttribute_ObjectIdentity = ObjectIdentity
slpAttribute = _SlpAttribute_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 999, 1, 4)
)
_SlpAttributeTable_Object = MibTable
slpAttributeTable = _SlpAttributeTable_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 4, 1)
)
if mibBuilder.loadTexts:
    slpAttributeTable.setStatus("current")
_SlpAttributeEntry_Object = MibTableRow
slpAttributeEntry = _SlpAttributeEntry_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 4, 1, 1)
)
slpAttributeEntry.setIndexNames(
    (0, "SERVICE-LOCATION-PROTOCOL-MIB", "slpAgentIndex"),
    (0, "SERVICE-LOCATION-PROTOCOL-MIB", "slpAttributeIndex"),
)
if mibBuilder.loadTexts:
    slpAttributeEntry.setStatus("current")


class _SlpAttributeIndex_Type(Integer32):
    """Custom type slpAttributeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SlpAttributeIndex_Type.__name__ = "Integer32"
_SlpAttributeIndex_Object = MibTableColumn
slpAttributeIndex = _SlpAttributeIndex_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 4, 1, 1, 1),
    _SlpAttributeIndex_Type()
)
slpAttributeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    slpAttributeIndex.setStatus("current")


class _SlpAttributeName_Type(SnmpAdminString):
    """Custom type slpAttributeName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SlpAttributeName_Type.__name__ = "SnmpAdminString"
_SlpAttributeName_Object = MibTableColumn
slpAttributeName = _SlpAttributeName_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 4, 1, 1, 2),
    _SlpAttributeName_Type()
)
slpAttributeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slpAttributeName.setStatus("current")
_SlpAttributeType_Type = SlpAttributeTypeTC
_SlpAttributeType_Object = MibTableColumn
slpAttributeType = _SlpAttributeType_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 4, 1, 1, 3),
    _SlpAttributeType_Type()
)
slpAttributeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slpAttributeType.setStatus("current")


class _SlpAttributeValue_Type(SnmpAdminString):
    """Custom type slpAttributeValue based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SlpAttributeValue_Type.__name__ = "SnmpAdminString"
_SlpAttributeValue_Object = MibTableColumn
slpAttributeValue = _SlpAttributeValue_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 4, 1, 1, 4),
    _SlpAttributeValue_Type()
)
slpAttributeValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slpAttributeValue.setStatus("current")
_SlpMIBConformance_ObjectIdentity = ObjectIdentity
slpMIBConformance = _SlpMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 999, 2)
)
_SlpMIBObjectGroups_ObjectIdentity = ObjectIdentity
slpMIBObjectGroups = _SlpMIBObjectGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 999, 2, 2)
)

# Managed Objects groups

slpAgentGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 999, 2, 2, 1)
)
slpAgentGroup.setObjects(
      *(("SERVICE-LOCATION-PROTOCOL-MIB", "slpAgentSWInstalledIndexOrZero"),
        ("SERVICE-LOCATION-PROTOCOL-MIB", "slpAgentName"),
        ("SERVICE-LOCATION-PROTOCOL-MIB", "slpAgentType"),
        ("SERVICE-LOCATION-PROTOCOL-MIB", "slpAgentIsBroadcastOnly"),
        ("SERVICE-LOCATION-PROTOCOL-MIB", "slpAgentActiveDADiscovery"),
        ("SERVICE-LOCATION-PROTOCOL-MIB", "slpAgentPassiveDADiscovery"),
        ("SERVICE-LOCATION-PROTOCOL-MIB", "slpAgentMessageTypesSupported"),
        ("SERVICE-LOCATION-PROTOCOL-MIB", "slpAgentExtensionsSupported"))
)
if mibBuilder.loadTexts:
    slpAgentGroup.setStatus("current")

slpScopeGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 999, 2, 2, 2)
)
slpScopeGroup.setObjects(
      *(("SERVICE-LOCATION-PROTOCOL-MIB", "slpScopeSource"),
        ("SERVICE-LOCATION-PROTOCOL-MIB", "slpScopeValue"))
)
if mibBuilder.loadTexts:
    slpScopeGroup.setStatus("current")

slpAddressGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 999, 2, 2, 3)
)
slpAddressGroup.setObjects(
      *(("SERVICE-LOCATION-PROTOCOL-MIB", "slpAddressAgentType"),
        ("SERVICE-LOCATION-PROTOCOL-MIB", "slpAddressSource"),
        ("SERVICE-LOCATION-PROTOCOL-MIB", "slpAddressOrName"))
)
if mibBuilder.loadTexts:
    slpAddressGroup.setStatus("current")

slpAttributeGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 999, 2, 2, 4)
)
slpAttributeGroup.setObjects(
      *(("SERVICE-LOCATION-PROTOCOL-MIB", "slpAttributeName"),
        ("SERVICE-LOCATION-PROTOCOL-MIB", "slpAttributeType"),
        ("SERVICE-LOCATION-PROTOCOL-MIB", "slpAttributeValue"))
)
if mibBuilder.loadTexts:
    slpAttributeGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

slpMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 999, 2, 1)
)
if mibBuilder.loadTexts:
    slpMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SERVICE-LOCATION-PROTOCOL-MIB",
    **{"SlpAgentTypeTC": SlpAgentTypeTC,
       "SlpScopeSourceTC": SlpScopeSourceTC,
       "SlpAttributeTypeTC": SlpAttributeTypeTC,
       "slpMIB": slpMIB,
       "slpMIBObjects": slpMIBObjects,
       "slpAgent": slpAgent,
       "slpAgentTable": slpAgentTable,
       "slpAgentEntry": slpAgentEntry,
       "slpAgentIndex": slpAgentIndex,
       "slpAgentSWInstalledIndexOrZero": slpAgentSWInstalledIndexOrZero,
       "slpAgentName": slpAgentName,
       "slpAgentType": slpAgentType,
       "slpAgentIsBroadcastOnly": slpAgentIsBroadcastOnly,
       "slpAgentActiveDADiscovery": slpAgentActiveDADiscovery,
       "slpAgentPassiveDADiscovery": slpAgentPassiveDADiscovery,
       "slpAgentMessageTypesSupported": slpAgentMessageTypesSupported,
       "slpAgentExtensionsSupported": slpAgentExtensionsSupported,
       "slpScope": slpScope,
       "slpScopeTable": slpScopeTable,
       "slpScopeEntry": slpScopeEntry,
       "slpScopeIndex": slpScopeIndex,
       "slpScopeSource": slpScopeSource,
       "slpScopeValue": slpScopeValue,
       "slpAddress": slpAddress,
       "slpAddressTable": slpAddressTable,
       "slpAddressEntry": slpAddressEntry,
       "slpAddressIndex": slpAddressIndex,
       "slpAddressAgentType": slpAddressAgentType,
       "slpAddressSource": slpAddressSource,
       "slpAddressOrName": slpAddressOrName,
       "slpAttribute": slpAttribute,
       "slpAttributeTable": slpAttributeTable,
       "slpAttributeEntry": slpAttributeEntry,
       "slpAttributeIndex": slpAttributeIndex,
       "slpAttributeName": slpAttributeName,
       "slpAttributeType": slpAttributeType,
       "slpAttributeValue": slpAttributeValue,
       "slpMIBConformance": slpMIBConformance,
       "slpMIBCompliance": slpMIBCompliance,
       "slpMIBObjectGroups": slpMIBObjectGroups,
       "slpAgentGroup": slpAgentGroup,
       "slpScopeGroup": slpScopeGroup,
       "slpAddressGroup": slpAddressGroup,
       "slpAttributeGroup": slpAttributeGroup}
)
