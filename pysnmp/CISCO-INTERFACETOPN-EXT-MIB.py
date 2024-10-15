# SNMP MIB module (CISCO-INTERFACETOPN-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-INTERFACETOPN-EXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:02:32 2024
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

(interfaceTopNControlEntry,) = mibBuilder.importSymbols(
    "INTERFACETOPN-MIB",
    "interfaceTopNControlEntry")

(VlanIndex,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanIndex")

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

ciscoInterfaceTopNExtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 482)
)
ciscoInterfaceTopNExtMIB.setRevisions(
        ("2010-10-19 00:00",
         "2008-01-15 00:00",
         "2006-03-15 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoInterfaceTopNExtMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoInterfaceTopNExtMIBNotifs = _CiscoInterfaceTopNExtMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 482, 0)
)
_CiscoInterfaceTopNExtMIBObjects_ObjectIdentity = ObjectIdentity
ciscoInterfaceTopNExtMIBObjects = _CiscoInterfaceTopNExtMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 482, 1)
)


class _CitneInterfaceTopNCaps_Type(Bits):
    """Custom type citneInterfaceTopNCaps based on Bits"""
    namedValues = NamedValues(
        *(("broadcast", 3),
          ("bytes", 1),
          ("multicast", 4),
          ("overflow", 5),
          ("packets", 2),
          ("utilization", 0))
    )

_CitneInterfaceTopNCaps_Type.__name__ = "Bits"
_CitneInterfaceTopNCaps_Object = MibScalar
citneInterfaceTopNCaps = _CitneInterfaceTopNCaps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 482, 1, 1),
    _CitneInterfaceTopNCaps_Type()
)
citneInterfaceTopNCaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    citneInterfaceTopNCaps.setStatus("current")
_CitneInterfaceTopNControlTable_Object = MibTable
citneInterfaceTopNControlTable = _CitneInterfaceTopNControlTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 482, 1, 2)
)
if mibBuilder.loadTexts:
    citneInterfaceTopNControlTable.setStatus("current")
_CitneInterfaceTopNControlEntry_Object = MibTableRow
citneInterfaceTopNControlEntry = _CitneInterfaceTopNControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 482, 1, 2, 1)
)
if mibBuilder.loadTexts:
    citneInterfaceTopNControlEntry.setStatus("current")


class _CitneInterfaceTopNCounterType_Type(Integer32):
    """Custom type citneInterfaceTopNCounterType based on Integer32"""
    defaultValue = 1

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
        *(("broadcast", 5),
          ("bytes", 3),
          ("multicast", 6),
          ("none", 1),
          ("overflow", 7),
          ("packets", 4),
          ("utilization", 2))
    )


_CitneInterfaceTopNCounterType_Type.__name__ = "Integer32"
_CitneInterfaceTopNCounterType_Object = MibTableColumn
citneInterfaceTopNCounterType = _CitneInterfaceTopNCounterType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 482, 1, 2, 1, 1),
    _CitneInterfaceTopNCounterType_Type()
)
citneInterfaceTopNCounterType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    citneInterfaceTopNCounterType.setStatus("current")


class _CitneInterfaceTopNInterfaceType_Type(Integer32):
    """Custom type citneInterfaceTopNInterfaceType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("all", 1),
          ("ethernet", 2),
          ("fastEthernet", 3),
          ("fortyGigaEthernet", 9),
          ("gigaEthernet", 4),
          ("layer2", 7),
          ("layer3", 8),
          ("portChannel", 6),
          ("tenGigaEthernet", 5))
    )


_CitneInterfaceTopNInterfaceType_Type.__name__ = "Integer32"
_CitneInterfaceTopNInterfaceType_Object = MibTableColumn
citneInterfaceTopNInterfaceType = _CitneInterfaceTopNInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 482, 1, 2, 1, 2),
    _CitneInterfaceTopNInterfaceType_Type()
)
citneInterfaceTopNInterfaceType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    citneInterfaceTopNInterfaceType.setStatus("current")


class _CitneInterfaceTopNVlanNumber_Type(VlanIndex):
    """Custom type citneInterfaceTopNVlanNumber based on VlanIndex"""
    defaultValue = 0


_CitneInterfaceTopNVlanNumber_Object = MibTableColumn
citneInterfaceTopNVlanNumber = _CitneInterfaceTopNVlanNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 482, 1, 2, 1, 3),
    _CitneInterfaceTopNVlanNumber_Type()
)
citneInterfaceTopNVlanNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    citneInterfaceTopNVlanNumber.setStatus("current")
_CiscoInterfaceTopNExtMIBConform_ObjectIdentity = ObjectIdentity
ciscoInterfaceTopNExtMIBConform = _CiscoInterfaceTopNExtMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 482, 2)
)
_CiscoIfTopNExtMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoIfTopNExtMIBCompliances = _CiscoIfTopNExtMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 482, 2, 1)
)
_CiscoIfTopNExtMIBGroups_ObjectIdentity = ObjectIdentity
ciscoIfTopNExtMIBGroups = _CiscoIfTopNExtMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 482, 2, 2)
)
interfaceTopNControlEntry.registerAugmentions(
    ("CISCO-INTERFACETOPN-EXT-MIB",
     "citneInterfaceTopNControlEntry")
)
citneInterfaceTopNControlEntry.setIndexNames(*interfaceTopNControlEntry.getIndexNames())

# Managed Objects groups

ciscoIfTopNExtCapsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 482, 2, 2, 1)
)
ciscoIfTopNExtCapsGroup.setObjects(
    ("CISCO-INTERFACETOPN-EXT-MIB", "citneInterfaceTopNCaps")
)
if mibBuilder.loadTexts:
    ciscoIfTopNExtCapsGroup.setStatus("current")

ciscoIfTopNExtControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 482, 2, 2, 2)
)
ciscoIfTopNExtControlGroup.setObjects(
      *(("CISCO-INTERFACETOPN-EXT-MIB", "citneInterfaceTopNCounterType"),
        ("CISCO-INTERFACETOPN-EXT-MIB", "citneInterfaceTopNInterfaceType"))
)
if mibBuilder.loadTexts:
    ciscoIfTopNExtControlGroup.setStatus("current")

ciscoIfTopNExtCtrlVlanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 482, 2, 2, 3)
)
ciscoIfTopNExtCtrlVlanGroup.setObjects(
    ("CISCO-INTERFACETOPN-EXT-MIB", "citneInterfaceTopNVlanNumber")
)
if mibBuilder.loadTexts:
    ciscoIfTopNExtCtrlVlanGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoIfTopNExtMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 482, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoIfTopNExtMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-INTERFACETOPN-EXT-MIB",
    **{"ciscoInterfaceTopNExtMIB": ciscoInterfaceTopNExtMIB,
       "ciscoInterfaceTopNExtMIBNotifs": ciscoInterfaceTopNExtMIBNotifs,
       "ciscoInterfaceTopNExtMIBObjects": ciscoInterfaceTopNExtMIBObjects,
       "citneInterfaceTopNCaps": citneInterfaceTopNCaps,
       "citneInterfaceTopNControlTable": citneInterfaceTopNControlTable,
       "citneInterfaceTopNControlEntry": citneInterfaceTopNControlEntry,
       "citneInterfaceTopNCounterType": citneInterfaceTopNCounterType,
       "citneInterfaceTopNInterfaceType": citneInterfaceTopNInterfaceType,
       "citneInterfaceTopNVlanNumber": citneInterfaceTopNVlanNumber,
       "ciscoInterfaceTopNExtMIBConform": ciscoInterfaceTopNExtMIBConform,
       "ciscoIfTopNExtMIBCompliances": ciscoIfTopNExtMIBCompliances,
       "ciscoIfTopNExtMIBCompliance": ciscoIfTopNExtMIBCompliance,
       "ciscoIfTopNExtMIBGroups": ciscoIfTopNExtMIBGroups,
       "ciscoIfTopNExtCapsGroup": ciscoIfTopNExtCapsGroup,
       "ciscoIfTopNExtControlGroup": ciscoIfTopNExtControlGroup,
       "ciscoIfTopNExtCtrlVlanGroup": ciscoIfTopNExtCtrlVlanGroup}
)
