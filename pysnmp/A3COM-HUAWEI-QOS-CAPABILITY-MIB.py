# SNMP MIB module (A3COM-HUAWEI-QOS-CAPABILITY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/A3COM-HUAWEI-QOS-CAPABILITY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:28:55 2024
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

(h3cSNMPAgCpb,) = mibBuilder.importSymbols(
    "A3COM-HUAWEI-OID-MIB",
    "h3cSNMPAgCpb")

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

h3cQosCapability = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 7, 1)
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

_H3cQoSCapabilityMibObjects_ObjectIdentity = ObjectIdentity
h3cQoSCapabilityMibObjects = _H3cQoSCapabilityMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 7, 1, 1)
)
_H3cQoSCapabilityGroup_ObjectIdentity = ObjectIdentity
h3cQoSCapabilityGroup = _H3cQoSCapabilityGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 7, 1, 1, 1)
)
_H3cQoSCapabilityTable_Object = MibTable
h3cQoSCapabilityTable = _H3cQoSCapabilityTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 7, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    h3cQoSCapabilityTable.setStatus("current")
_H3cQoSCapabilityEntry_Object = MibTableRow
h3cQoSCapabilityEntry = _H3cQoSCapabilityEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 7, 1, 1, 1, 1, 1)
)
h3cQoSCapabilityEntry.setIndexNames(
    (0, "A3COM-HUAWEI-QOS-CAPABILITY-MIB", "h3cQoSCapabilityPhysicalType"),
    (0, "A3COM-HUAWEI-QOS-CAPABILITY-MIB", "h3cQoSCapabilityPhysicalIndex"),
    (0, "A3COM-HUAWEI-QOS-CAPABILITY-MIB", "h3cQoSModuleIndex"),
    (0, "A3COM-HUAWEI-QOS-CAPABILITY-MIB", "h3cQoSCharacteristicsIndex"),
)
if mibBuilder.loadTexts:
    h3cQoSCapabilityEntry.setStatus("current")
_H3cQoSCapabilityPhysicalType_Type = CapabilityPhysicalType
_H3cQoSCapabilityPhysicalType_Object = MibTableColumn
h3cQoSCapabilityPhysicalType = _H3cQoSCapabilityPhysicalType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 7, 1, 1, 1, 1, 1, 1),
    _H3cQoSCapabilityPhysicalType_Type()
)
h3cQoSCapabilityPhysicalType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cQoSCapabilityPhysicalType.setStatus("current")
_H3cQoSCapabilityPhysicalIndex_Type = Integer32
_H3cQoSCapabilityPhysicalIndex_Object = MibTableColumn
h3cQoSCapabilityPhysicalIndex = _H3cQoSCapabilityPhysicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 7, 1, 1, 1, 1, 1, 2),
    _H3cQoSCapabilityPhysicalIndex_Type()
)
h3cQoSCapabilityPhysicalIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cQoSCapabilityPhysicalIndex.setStatus("current")
_H3cQoSModuleIndex_Type = Integer32
_H3cQoSModuleIndex_Object = MibTableColumn
h3cQoSModuleIndex = _H3cQoSModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 7, 1, 1, 1, 1, 1, 3),
    _H3cQoSModuleIndex_Type()
)
h3cQoSModuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cQoSModuleIndex.setStatus("current")
_H3cQoSCharacteristicsIndex_Type = Integer32
_H3cQoSCharacteristicsIndex_Object = MibTableColumn
h3cQoSCharacteristicsIndex = _H3cQoSCharacteristicsIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 7, 1, 1, 1, 1, 1, 4),
    _H3cQoSCharacteristicsIndex_Type()
)
h3cQoSCharacteristicsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cQoSCharacteristicsIndex.setStatus("current")
_H3cQoSCharacteristicsValue_Type = Unsigned32
_H3cQoSCharacteristicsValue_Object = MibTableColumn
h3cQoSCharacteristicsValue = _H3cQoSCharacteristicsValue_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 7, 1, 1, 1, 1, 1, 5),
    _H3cQoSCharacteristicsValue_Type()
)
h3cQoSCharacteristicsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cQoSCharacteristicsValue.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "A3COM-HUAWEI-QOS-CAPABILITY-MIB",
    **{"CapabilityPhysicalType": CapabilityPhysicalType,
       "h3cQosCapability": h3cQosCapability,
       "h3cQoSCapabilityMibObjects": h3cQoSCapabilityMibObjects,
       "h3cQoSCapabilityGroup": h3cQoSCapabilityGroup,
       "h3cQoSCapabilityTable": h3cQoSCapabilityTable,
       "h3cQoSCapabilityEntry": h3cQoSCapabilityEntry,
       "h3cQoSCapabilityPhysicalType": h3cQoSCapabilityPhysicalType,
       "h3cQoSCapabilityPhysicalIndex": h3cQoSCapabilityPhysicalIndex,
       "h3cQoSModuleIndex": h3cQoSModuleIndex,
       "h3cQoSCharacteristicsIndex": h3cQoSCharacteristicsIndex,
       "h3cQoSCharacteristicsValue": h3cQoSCharacteristicsValue}
)
