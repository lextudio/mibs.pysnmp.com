# SNMP MIB module (CISCO-IP-STAT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-IP-STAT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:02:45 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 MacAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention")


# MODULE-IDENTITY

ciscoIpStatMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 84)
)
ciscoIpStatMIB.setRevisions(
        ("2001-12-20 23:00",
         "1997-07-18 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class PacketSource(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("input", 1),
          ("output", 2))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoIpStatMIBObjects_ObjectIdentity = ObjectIdentity
ciscoIpStatMIBObjects = _CiscoIpStatMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 84, 1)
)
_CipPrecedence_ObjectIdentity = ObjectIdentity
cipPrecedence = _CipPrecedence_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 84, 1, 1)
)
_CipPrecedenceTable_Object = MibTable
cipPrecedenceTable = _CipPrecedenceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 84, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cipPrecedenceTable.setStatus("current")
_CipPrecedenceEntry_Object = MibTableRow
cipPrecedenceEntry = _CipPrecedenceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 84, 1, 1, 1, 1)
)
cipPrecedenceEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-IP-STAT-MIB", "cipPrecedenceDirection"),
    (0, "CISCO-IP-STAT-MIB", "cipPrecedenceIpPrecedence"),
)
if mibBuilder.loadTexts:
    cipPrecedenceEntry.setStatus("current")
_CipPrecedenceDirection_Type = PacketSource
_CipPrecedenceDirection_Object = MibTableColumn
cipPrecedenceDirection = _CipPrecedenceDirection_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 84, 1, 1, 1, 1, 1),
    _CipPrecedenceDirection_Type()
)
cipPrecedenceDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cipPrecedenceDirection.setStatus("current")


class _CipPrecedenceIpPrecedence_Type(Integer32):
    """Custom type cipPrecedenceIpPrecedence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_CipPrecedenceIpPrecedence_Type.__name__ = "Integer32"
_CipPrecedenceIpPrecedence_Object = MibTableColumn
cipPrecedenceIpPrecedence = _CipPrecedenceIpPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 84, 1, 1, 1, 1, 2),
    _CipPrecedenceIpPrecedence_Type()
)
cipPrecedenceIpPrecedence.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cipPrecedenceIpPrecedence.setStatus("current")
_CipPrecedenceSwitchedPkts_Type = Counter32
_CipPrecedenceSwitchedPkts_Object = MibTableColumn
cipPrecedenceSwitchedPkts = _CipPrecedenceSwitchedPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 84, 1, 1, 1, 1, 3),
    _CipPrecedenceSwitchedPkts_Type()
)
cipPrecedenceSwitchedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipPrecedenceSwitchedPkts.setStatus("current")
if mibBuilder.loadTexts:
    cipPrecedenceSwitchedPkts.setUnits("packets")
_CipPrecedenceSwitchedBytes_Type = Counter32
_CipPrecedenceSwitchedBytes_Object = MibTableColumn
cipPrecedenceSwitchedBytes = _CipPrecedenceSwitchedBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 84, 1, 1, 1, 1, 4),
    _CipPrecedenceSwitchedBytes_Type()
)
cipPrecedenceSwitchedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipPrecedenceSwitchedBytes.setStatus("current")
if mibBuilder.loadTexts:
    cipPrecedenceSwitchedBytes.setUnits("bytes")
_CipPrecedenceXTable_Object = MibTable
cipPrecedenceXTable = _CipPrecedenceXTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 84, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cipPrecedenceXTable.setStatus("current")
_CipPrecedenceXEntry_Object = MibTableRow
cipPrecedenceXEntry = _CipPrecedenceXEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 84, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cipPrecedenceXEntry.setStatus("current")
_CipPrecedenceHCSwitchedPkts_Type = Counter64
_CipPrecedenceHCSwitchedPkts_Object = MibTableColumn
cipPrecedenceHCSwitchedPkts = _CipPrecedenceHCSwitchedPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 84, 1, 1, 2, 1, 1),
    _CipPrecedenceHCSwitchedPkts_Type()
)
cipPrecedenceHCSwitchedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipPrecedenceHCSwitchedPkts.setStatus("current")
if mibBuilder.loadTexts:
    cipPrecedenceHCSwitchedPkts.setUnits("packets")
_CipPrecedenceHCSwitchedBytes_Type = Counter64
_CipPrecedenceHCSwitchedBytes_Object = MibTableColumn
cipPrecedenceHCSwitchedBytes = _CipPrecedenceHCSwitchedBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 84, 1, 1, 2, 1, 2),
    _CipPrecedenceHCSwitchedBytes_Type()
)
cipPrecedenceHCSwitchedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipPrecedenceHCSwitchedBytes.setStatus("current")
if mibBuilder.loadTexts:
    cipPrecedenceHCSwitchedBytes.setUnits("bytes")
_CipMacIf_ObjectIdentity = ObjectIdentity
cipMacIf = _CipMacIf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 84, 1, 2)
)
_CipMacTable_Object = MibTable
cipMacTable = _CipMacTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 84, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cipMacTable.setStatus("current")
_CipMacEntry_Object = MibTableRow
cipMacEntry = _CipMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 84, 1, 2, 1, 1)
)
cipMacEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-IP-STAT-MIB", "cipMacDirection"),
    (0, "CISCO-IP-STAT-MIB", "cipMacAddress"),
)
if mibBuilder.loadTexts:
    cipMacEntry.setStatus("current")
_CipMacDirection_Type = PacketSource
_CipMacDirection_Object = MibTableColumn
cipMacDirection = _CipMacDirection_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 84, 1, 2, 1, 1, 1),
    _CipMacDirection_Type()
)
cipMacDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cipMacDirection.setStatus("current")
_CipMacAddress_Type = MacAddress
_CipMacAddress_Object = MibTableColumn
cipMacAddress = _CipMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 84, 1, 2, 1, 1, 2),
    _CipMacAddress_Type()
)
cipMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cipMacAddress.setStatus("current")
_CipMacSwitchedPkts_Type = Counter32
_CipMacSwitchedPkts_Object = MibTableColumn
cipMacSwitchedPkts = _CipMacSwitchedPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 84, 1, 2, 1, 1, 3),
    _CipMacSwitchedPkts_Type()
)
cipMacSwitchedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipMacSwitchedPkts.setStatus("current")
if mibBuilder.loadTexts:
    cipMacSwitchedPkts.setUnits("packets")
_CipMacSwitchedBytes_Type = Counter32
_CipMacSwitchedBytes_Object = MibTableColumn
cipMacSwitchedBytes = _CipMacSwitchedBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 84, 1, 2, 1, 1, 4),
    _CipMacSwitchedBytes_Type()
)
cipMacSwitchedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipMacSwitchedBytes.setStatus("current")
if mibBuilder.loadTexts:
    cipMacSwitchedBytes.setUnits("bytes")
_CipMacFreeTable_Object = MibTable
cipMacFreeTable = _CipMacFreeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 84, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cipMacFreeTable.setStatus("current")
_CipMacFreeEntry_Object = MibTableRow
cipMacFreeEntry = _CipMacFreeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 84, 1, 2, 2, 1)
)
cipMacFreeEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-IP-STAT-MIB", "cipMacFreeDirection"),
)
if mibBuilder.loadTexts:
    cipMacFreeEntry.setStatus("current")
_CipMacFreeDirection_Type = PacketSource
_CipMacFreeDirection_Object = MibTableColumn
cipMacFreeDirection = _CipMacFreeDirection_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 84, 1, 2, 2, 1, 1),
    _CipMacFreeDirection_Type()
)
cipMacFreeDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cipMacFreeDirection.setStatus("current")
_CipMacFreeCount_Type = Gauge32
_CipMacFreeCount_Object = MibTableColumn
cipMacFreeCount = _CipMacFreeCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 84, 1, 2, 2, 1, 2),
    _CipMacFreeCount_Type()
)
cipMacFreeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipMacFreeCount.setStatus("current")
_CipMacXTable_Object = MibTable
cipMacXTable = _CipMacXTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 84, 1, 2, 3)
)
if mibBuilder.loadTexts:
    cipMacXTable.setStatus("current")
_CipMacXEntry_Object = MibTableRow
cipMacXEntry = _CipMacXEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 84, 1, 2, 3, 1)
)
if mibBuilder.loadTexts:
    cipMacXEntry.setStatus("current")
_CipMacHCSwitchedPkts_Type = Counter64
_CipMacHCSwitchedPkts_Object = MibTableColumn
cipMacHCSwitchedPkts = _CipMacHCSwitchedPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 84, 1, 2, 3, 1, 1),
    _CipMacHCSwitchedPkts_Type()
)
cipMacHCSwitchedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipMacHCSwitchedPkts.setStatus("current")
if mibBuilder.loadTexts:
    cipMacHCSwitchedPkts.setUnits("packets")
_CipMacHCSwitchedBytes_Type = Counter64
_CipMacHCSwitchedBytes_Object = MibTableColumn
cipMacHCSwitchedBytes = _CipMacHCSwitchedBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 84, 1, 2, 3, 1, 2),
    _CipMacHCSwitchedBytes_Type()
)
cipMacHCSwitchedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipMacHCSwitchedBytes.setStatus("current")
if mibBuilder.loadTexts:
    cipMacHCSwitchedBytes.setUnits("bytes")
_CiscoIpStatMIBConformance_ObjectIdentity = ObjectIdentity
ciscoIpStatMIBConformance = _CiscoIpStatMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 84, 3)
)
_CiscoIpStatMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoIpStatMIBCompliances = _CiscoIpStatMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 84, 3, 1)
)
_CiscoIpStatMIBGroups_ObjectIdentity = ObjectIdentity
ciscoIpStatMIBGroups = _CiscoIpStatMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 84, 3, 2)
)
cipPrecedenceEntry.registerAugmentions(
    ("CISCO-IP-STAT-MIB",
     "cipPrecedenceXEntry")
)
cipPrecedenceXEntry.setIndexNames(*cipPrecedenceEntry.getIndexNames())
cipMacEntry.registerAugmentions(
    ("CISCO-IP-STAT-MIB",
     "cipMacXEntry")
)
cipMacXEntry.setIndexNames(*cipMacEntry.getIndexNames())

# Managed Objects groups

ciscoIpStatMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 84, 3, 2, 1)
)
ciscoIpStatMIBGroup.setObjects(
      *(("CISCO-IP-STAT-MIB", "cipPrecedenceSwitchedPkts"),
        ("CISCO-IP-STAT-MIB", "cipPrecedenceSwitchedBytes"),
        ("CISCO-IP-STAT-MIB", "cipMacSwitchedPkts"),
        ("CISCO-IP-STAT-MIB", "cipMacSwitchedBytes"),
        ("CISCO-IP-STAT-MIB", "cipMacFreeCount"))
)
if mibBuilder.loadTexts:
    ciscoIpStatMIBGroup.setStatus("current")

ciscoIpStatHCMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 84, 3, 2, 2)
)
ciscoIpStatHCMIBGroup.setObjects(
      *(("CISCO-IP-STAT-MIB", "cipPrecedenceHCSwitchedPkts"),
        ("CISCO-IP-STAT-MIB", "cipPrecedenceHCSwitchedBytes"),
        ("CISCO-IP-STAT-MIB", "cipMacHCSwitchedPkts"),
        ("CISCO-IP-STAT-MIB", "cipMacHCSwitchedBytes"))
)
if mibBuilder.loadTexts:
    ciscoIpStatHCMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoIpStatMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 84, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoIpStatMIBCompliance.setStatus(
        "deprecated"
    )

ciscoIpStatMIBComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 84, 3, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoIpStatMIBComplianceRev2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-IP-STAT-MIB",
    **{"PacketSource": PacketSource,
       "ciscoIpStatMIB": ciscoIpStatMIB,
       "ciscoIpStatMIBObjects": ciscoIpStatMIBObjects,
       "cipPrecedence": cipPrecedence,
       "cipPrecedenceTable": cipPrecedenceTable,
       "cipPrecedenceEntry": cipPrecedenceEntry,
       "cipPrecedenceDirection": cipPrecedenceDirection,
       "cipPrecedenceIpPrecedence": cipPrecedenceIpPrecedence,
       "cipPrecedenceSwitchedPkts": cipPrecedenceSwitchedPkts,
       "cipPrecedenceSwitchedBytes": cipPrecedenceSwitchedBytes,
       "cipPrecedenceXTable": cipPrecedenceXTable,
       "cipPrecedenceXEntry": cipPrecedenceXEntry,
       "cipPrecedenceHCSwitchedPkts": cipPrecedenceHCSwitchedPkts,
       "cipPrecedenceHCSwitchedBytes": cipPrecedenceHCSwitchedBytes,
       "cipMacIf": cipMacIf,
       "cipMacTable": cipMacTable,
       "cipMacEntry": cipMacEntry,
       "cipMacDirection": cipMacDirection,
       "cipMacAddress": cipMacAddress,
       "cipMacSwitchedPkts": cipMacSwitchedPkts,
       "cipMacSwitchedBytes": cipMacSwitchedBytes,
       "cipMacFreeTable": cipMacFreeTable,
       "cipMacFreeEntry": cipMacFreeEntry,
       "cipMacFreeDirection": cipMacFreeDirection,
       "cipMacFreeCount": cipMacFreeCount,
       "cipMacXTable": cipMacXTable,
       "cipMacXEntry": cipMacXEntry,
       "cipMacHCSwitchedPkts": cipMacHCSwitchedPkts,
       "cipMacHCSwitchedBytes": cipMacHCSwitchedBytes,
       "ciscoIpStatMIBConformance": ciscoIpStatMIBConformance,
       "ciscoIpStatMIBCompliances": ciscoIpStatMIBCompliances,
       "ciscoIpStatMIBCompliance": ciscoIpStatMIBCompliance,
       "ciscoIpStatMIBComplianceRev2": ciscoIpStatMIBComplianceRev2,
       "ciscoIpStatMIBGroups": ciscoIpStatMIBGroups,
       "ciscoIpStatMIBGroup": ciscoIpStatMIBGroup,
       "ciscoIpStatHCMIBGroup": ciscoIpStatHCMIBGroup}
)
