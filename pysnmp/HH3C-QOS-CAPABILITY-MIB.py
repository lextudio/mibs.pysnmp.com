# SNMP MIB module (HH3C-QOS-CAPABILITY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-QOS-CAPABILITY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:54:38 2024
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

(hh3cSNMPAgCpb,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cSNMPAgCpb")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

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

hh3cQosCapability = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 7, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CapabilityPhysicalType(Integer32, TextualConvention):
    status = "current"
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
        *(("chassis", 2),
          ("module", 3),
          ("port", 4),
          ("stack", 1))
    )



# MIB Managed Objects in the order of their OIDs

_Hh3cQoSCapabilityMibObjects_ObjectIdentity = ObjectIdentity
hh3cQoSCapabilityMibObjects = _Hh3cQoSCapabilityMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 7, 1, 1)
)
_Hh3cQoSCapabilityGroup_ObjectIdentity = ObjectIdentity
hh3cQoSCapabilityGroup = _Hh3cQoSCapabilityGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 7, 1, 1, 1)
)
_Hh3cQoSCapabilityTable_Object = MibTable
hh3cQoSCapabilityTable = _Hh3cQoSCapabilityTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 7, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cQoSCapabilityTable.setStatus("current")
_Hh3cQoSCapabilityEntry_Object = MibTableRow
hh3cQoSCapabilityEntry = _Hh3cQoSCapabilityEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 7, 1, 1, 1, 1, 1)
)
hh3cQoSCapabilityEntry.setIndexNames(
    (0, "HH3C-QOS-CAPABILITY-MIB", "hh3cQoSCapabilityPhysicalType"),
    (0, "HH3C-QOS-CAPABILITY-MIB", "hh3cQoSCapabilityPhysicalIndex"),
    (0, "HH3C-QOS-CAPABILITY-MIB", "hh3cQoSModuleIndex"),
    (0, "HH3C-QOS-CAPABILITY-MIB", "hh3cQoSCharacteristicsIndex"),
)
if mibBuilder.loadTexts:
    hh3cQoSCapabilityEntry.setStatus("current")
_Hh3cQoSCapabilityPhysicalType_Type = CapabilityPhysicalType
_Hh3cQoSCapabilityPhysicalType_Object = MibTableColumn
hh3cQoSCapabilityPhysicalType = _Hh3cQoSCapabilityPhysicalType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 7, 1, 1, 1, 1, 1, 1),
    _Hh3cQoSCapabilityPhysicalType_Type()
)
hh3cQoSCapabilityPhysicalType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cQoSCapabilityPhysicalType.setStatus("current")
_Hh3cQoSCapabilityPhysicalIndex_Type = Integer32
_Hh3cQoSCapabilityPhysicalIndex_Object = MibTableColumn
hh3cQoSCapabilityPhysicalIndex = _Hh3cQoSCapabilityPhysicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 7, 1, 1, 1, 1, 1, 2),
    _Hh3cQoSCapabilityPhysicalIndex_Type()
)
hh3cQoSCapabilityPhysicalIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cQoSCapabilityPhysicalIndex.setStatus("current")
_Hh3cQoSModuleIndex_Type = Integer32
_Hh3cQoSModuleIndex_Object = MibTableColumn
hh3cQoSModuleIndex = _Hh3cQoSModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 7, 1, 1, 1, 1, 1, 3),
    _Hh3cQoSModuleIndex_Type()
)
hh3cQoSModuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cQoSModuleIndex.setStatus("current")
_Hh3cQoSCharacteristicsIndex_Type = Integer32
_Hh3cQoSCharacteristicsIndex_Object = MibTableColumn
hh3cQoSCharacteristicsIndex = _Hh3cQoSCharacteristicsIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 7, 1, 1, 1, 1, 1, 4),
    _Hh3cQoSCharacteristicsIndex_Type()
)
hh3cQoSCharacteristicsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cQoSCharacteristicsIndex.setStatus("current")
_Hh3cQoSCharacteristicsValue_Type = Unsigned32
_Hh3cQoSCharacteristicsValue_Object = MibTableColumn
hh3cQoSCharacteristicsValue = _Hh3cQoSCharacteristicsValue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 7, 1, 1, 1, 1, 1, 5),
    _Hh3cQoSCharacteristicsValue_Type()
)
hh3cQoSCharacteristicsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cQoSCharacteristicsValue.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-QOS-CAPABILITY-MIB",
    **{"CapabilityPhysicalType": CapabilityPhysicalType,
       "hh3cQosCapability": hh3cQosCapability,
       "hh3cQoSCapabilityMibObjects": hh3cQoSCapabilityMibObjects,
       "hh3cQoSCapabilityGroup": hh3cQoSCapabilityGroup,
       "hh3cQoSCapabilityTable": hh3cQoSCapabilityTable,
       "hh3cQoSCapabilityEntry": hh3cQoSCapabilityEntry,
       "hh3cQoSCapabilityPhysicalType": hh3cQoSCapabilityPhysicalType,
       "hh3cQoSCapabilityPhysicalIndex": hh3cQoSCapabilityPhysicalIndex,
       "hh3cQoSModuleIndex": hh3cQoSModuleIndex,
       "hh3cQoSCharacteristicsIndex": hh3cQoSCharacteristicsIndex,
       "hh3cQoSCharacteristicsValue": hh3cQoSCharacteristicsValue}
)
