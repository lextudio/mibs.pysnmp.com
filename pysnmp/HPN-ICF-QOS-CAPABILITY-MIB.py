# SNMP MIB module (HPN-ICF-QOS-CAPABILITY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-QOS-CAPABILITY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:01:36 2024
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

(hpnicfSNMPAgCpb,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicfSNMPAgCpb")

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

hpnicfQosCapability = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 7, 1)
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

_HpnicfQoSCapabilityMibObjects_ObjectIdentity = ObjectIdentity
hpnicfQoSCapabilityMibObjects = _HpnicfQoSCapabilityMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 7, 1, 1)
)
_HpnicfQoSCapabilityGroup_ObjectIdentity = ObjectIdentity
hpnicfQoSCapabilityGroup = _HpnicfQoSCapabilityGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 7, 1, 1, 1)
)
_HpnicfQoSCapabilityTable_Object = MibTable
hpnicfQoSCapabilityTable = _HpnicfQoSCapabilityTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 7, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hpnicfQoSCapabilityTable.setStatus("current")
_HpnicfQoSCapabilityEntry_Object = MibTableRow
hpnicfQoSCapabilityEntry = _HpnicfQoSCapabilityEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 7, 1, 1, 1, 1, 1)
)
hpnicfQoSCapabilityEntry.setIndexNames(
    (0, "HPN-ICF-QOS-CAPABILITY-MIB", "hpnicfQoSCapabilityPhysicalType"),
    (0, "HPN-ICF-QOS-CAPABILITY-MIB", "hpnicfQoSCapabilityPhysicalIndex"),
    (0, "HPN-ICF-QOS-CAPABILITY-MIB", "hpnicfQoSModuleIndex"),
    (0, "HPN-ICF-QOS-CAPABILITY-MIB", "hpnicfQoSCharacteristicsIndex"),
)
if mibBuilder.loadTexts:
    hpnicfQoSCapabilityEntry.setStatus("current")
_HpnicfQoSCapabilityPhysicalType_Type = CapabilityPhysicalType
_HpnicfQoSCapabilityPhysicalType_Object = MibTableColumn
hpnicfQoSCapabilityPhysicalType = _HpnicfQoSCapabilityPhysicalType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 7, 1, 1, 1, 1, 1, 1),
    _HpnicfQoSCapabilityPhysicalType_Type()
)
hpnicfQoSCapabilityPhysicalType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfQoSCapabilityPhysicalType.setStatus("current")
_HpnicfQoSCapabilityPhysicalIndex_Type = Integer32
_HpnicfQoSCapabilityPhysicalIndex_Object = MibTableColumn
hpnicfQoSCapabilityPhysicalIndex = _HpnicfQoSCapabilityPhysicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 7, 1, 1, 1, 1, 1, 2),
    _HpnicfQoSCapabilityPhysicalIndex_Type()
)
hpnicfQoSCapabilityPhysicalIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfQoSCapabilityPhysicalIndex.setStatus("current")
_HpnicfQoSModuleIndex_Type = Integer32
_HpnicfQoSModuleIndex_Object = MibTableColumn
hpnicfQoSModuleIndex = _HpnicfQoSModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 7, 1, 1, 1, 1, 1, 3),
    _HpnicfQoSModuleIndex_Type()
)
hpnicfQoSModuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfQoSModuleIndex.setStatus("current")
_HpnicfQoSCharacteristicsIndex_Type = Integer32
_HpnicfQoSCharacteristicsIndex_Object = MibTableColumn
hpnicfQoSCharacteristicsIndex = _HpnicfQoSCharacteristicsIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 7, 1, 1, 1, 1, 1, 4),
    _HpnicfQoSCharacteristicsIndex_Type()
)
hpnicfQoSCharacteristicsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfQoSCharacteristicsIndex.setStatus("current")
_HpnicfQoSCharacteristicsValue_Type = Unsigned32
_HpnicfQoSCharacteristicsValue_Object = MibTableColumn
hpnicfQoSCharacteristicsValue = _HpnicfQoSCharacteristicsValue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 7, 1, 1, 1, 1, 1, 5),
    _HpnicfQoSCharacteristicsValue_Type()
)
hpnicfQoSCharacteristicsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfQoSCharacteristicsValue.setStatus("current")
_HpnicfQoSSysCapabilityTable_Object = MibTable
hpnicfQoSSysCapabilityTable = _HpnicfQoSSysCapabilityTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 7, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    hpnicfQoSSysCapabilityTable.setStatus("current")
_HpnicfQoSSysCapabilityEntry_Object = MibTableRow
hpnicfQoSSysCapabilityEntry = _HpnicfQoSSysCapabilityEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 7, 1, 1, 1, 2, 1)
)
hpnicfQoSSysCapabilityEntry.setIndexNames(
    (0, "HPN-ICF-QOS-CAPABILITY-MIB", "hpnicfQoSSysCapModuleIndex"),
    (0, "HPN-ICF-QOS-CAPABILITY-MIB", "hpnicfQoSSysCapCharacteristicsIndex"),
)
if mibBuilder.loadTexts:
    hpnicfQoSSysCapabilityEntry.setStatus("current")


class _HpnicfQoSSysCapModuleIndex_Type(Integer32):
    """Custom type hpnicfQoSSysCapModuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpnicfQoSSysCapModuleIndex_Type.__name__ = "Integer32"
_HpnicfQoSSysCapModuleIndex_Object = MibTableColumn
hpnicfQoSSysCapModuleIndex = _HpnicfQoSSysCapModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 7, 1, 1, 1, 2, 1, 1),
    _HpnicfQoSSysCapModuleIndex_Type()
)
hpnicfQoSSysCapModuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfQoSSysCapModuleIndex.setStatus("current")


class _HpnicfQoSSysCapCharacteristicsIndex_Type(Integer32):
    """Custom type hpnicfQoSSysCapCharacteristicsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpnicfQoSSysCapCharacteristicsIndex_Type.__name__ = "Integer32"
_HpnicfQoSSysCapCharacteristicsIndex_Object = MibTableColumn
hpnicfQoSSysCapCharacteristicsIndex = _HpnicfQoSSysCapCharacteristicsIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 7, 1, 1, 1, 2, 1, 2),
    _HpnicfQoSSysCapCharacteristicsIndex_Type()
)
hpnicfQoSSysCapCharacteristicsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfQoSSysCapCharacteristicsIndex.setStatus("current")
_HpnicfQoSSysCapCharacteristicsValue_Type = Unsigned32
_HpnicfQoSSysCapCharacteristicsValue_Object = MibTableColumn
hpnicfQoSSysCapCharacteristicsValue = _HpnicfQoSSysCapCharacteristicsValue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 7, 1, 1, 1, 2, 1, 3),
    _HpnicfQoSSysCapCharacteristicsValue_Type()
)
hpnicfQoSSysCapCharacteristicsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfQoSSysCapCharacteristicsValue.setStatus("current")
_HpnicfQoSIfCapabilityTable_Object = MibTable
hpnicfQoSIfCapabilityTable = _HpnicfQoSIfCapabilityTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 7, 1, 1, 1, 3)
)
if mibBuilder.loadTexts:
    hpnicfQoSIfCapabilityTable.setStatus("current")
_HpnicfQoSIfCapabilityEntry_Object = MibTableRow
hpnicfQoSIfCapabilityEntry = _HpnicfQoSIfCapabilityEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 7, 1, 1, 1, 3, 1)
)
hpnicfQoSIfCapabilityEntry.setIndexNames(
    (0, "HPN-ICF-QOS-CAPABILITY-MIB", "hpnicfQoSIfCapIfIndex"),
    (0, "HPN-ICF-QOS-CAPABILITY-MIB", "hpnicfQoSIfCapModuleIndex"),
    (0, "HPN-ICF-QOS-CAPABILITY-MIB", "hpnicfQoSIfCapCharacteristicsIndex"),
)
if mibBuilder.loadTexts:
    hpnicfQoSIfCapabilityEntry.setStatus("current")


class _HpnicfQoSIfCapIfIndex_Type(Integer32):
    """Custom type hpnicfQoSIfCapIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HpnicfQoSIfCapIfIndex_Type.__name__ = "Integer32"
_HpnicfQoSIfCapIfIndex_Object = MibTableColumn
hpnicfQoSIfCapIfIndex = _HpnicfQoSIfCapIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 7, 1, 1, 1, 3, 1, 1),
    _HpnicfQoSIfCapIfIndex_Type()
)
hpnicfQoSIfCapIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfQoSIfCapIfIndex.setStatus("current")


class _HpnicfQoSIfCapModuleIndex_Type(Integer32):
    """Custom type hpnicfQoSIfCapModuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpnicfQoSIfCapModuleIndex_Type.__name__ = "Integer32"
_HpnicfQoSIfCapModuleIndex_Object = MibTableColumn
hpnicfQoSIfCapModuleIndex = _HpnicfQoSIfCapModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 7, 1, 1, 1, 3, 1, 2),
    _HpnicfQoSIfCapModuleIndex_Type()
)
hpnicfQoSIfCapModuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfQoSIfCapModuleIndex.setStatus("current")


class _HpnicfQoSIfCapCharacteristicsIndex_Type(Integer32):
    """Custom type hpnicfQoSIfCapCharacteristicsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpnicfQoSIfCapCharacteristicsIndex_Type.__name__ = "Integer32"
_HpnicfQoSIfCapCharacteristicsIndex_Object = MibTableColumn
hpnicfQoSIfCapCharacteristicsIndex = _HpnicfQoSIfCapCharacteristicsIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 7, 1, 1, 1, 3, 1, 3),
    _HpnicfQoSIfCapCharacteristicsIndex_Type()
)
hpnicfQoSIfCapCharacteristicsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfQoSIfCapCharacteristicsIndex.setStatus("current")
_HpnicfQoSIfCapCharacteristicsValue_Type = Unsigned32
_HpnicfQoSIfCapCharacteristicsValue_Object = MibTableColumn
hpnicfQoSIfCapCharacteristicsValue = _HpnicfQoSIfCapCharacteristicsValue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 7, 1, 1, 1, 3, 1, 4),
    _HpnicfQoSIfCapCharacteristicsValue_Type()
)
hpnicfQoSIfCapCharacteristicsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfQoSIfCapCharacteristicsValue.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-QOS-CAPABILITY-MIB",
    **{"CapabilityPhysicalType": CapabilityPhysicalType,
       "hpnicfQosCapability": hpnicfQosCapability,
       "hpnicfQoSCapabilityMibObjects": hpnicfQoSCapabilityMibObjects,
       "hpnicfQoSCapabilityGroup": hpnicfQoSCapabilityGroup,
       "hpnicfQoSCapabilityTable": hpnicfQoSCapabilityTable,
       "hpnicfQoSCapabilityEntry": hpnicfQoSCapabilityEntry,
       "hpnicfQoSCapabilityPhysicalType": hpnicfQoSCapabilityPhysicalType,
       "hpnicfQoSCapabilityPhysicalIndex": hpnicfQoSCapabilityPhysicalIndex,
       "hpnicfQoSModuleIndex": hpnicfQoSModuleIndex,
       "hpnicfQoSCharacteristicsIndex": hpnicfQoSCharacteristicsIndex,
       "hpnicfQoSCharacteristicsValue": hpnicfQoSCharacteristicsValue,
       "hpnicfQoSSysCapabilityTable": hpnicfQoSSysCapabilityTable,
       "hpnicfQoSSysCapabilityEntry": hpnicfQoSSysCapabilityEntry,
       "hpnicfQoSSysCapModuleIndex": hpnicfQoSSysCapModuleIndex,
       "hpnicfQoSSysCapCharacteristicsIndex": hpnicfQoSSysCapCharacteristicsIndex,
       "hpnicfQoSSysCapCharacteristicsValue": hpnicfQoSSysCapCharacteristicsValue,
       "hpnicfQoSIfCapabilityTable": hpnicfQoSIfCapabilityTable,
       "hpnicfQoSIfCapabilityEntry": hpnicfQoSIfCapabilityEntry,
       "hpnicfQoSIfCapIfIndex": hpnicfQoSIfCapIfIndex,
       "hpnicfQoSIfCapModuleIndex": hpnicfQoSIfCapModuleIndex,
       "hpnicfQoSIfCapCharacteristicsIndex": hpnicfQoSIfCapCharacteristicsIndex,
       "hpnicfQoSIfCapCharacteristicsValue": hpnicfQoSIfCapCharacteristicsValue}
)
