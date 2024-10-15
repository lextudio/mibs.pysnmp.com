# SNMP MIB module (CT-PRIORITY-QUEUING) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CT-PRIORITY-QUEUING
# Produced by pysmi-1.5.4 at Mon Oct 14 21:18:20 2024
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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Cabletron_ObjectIdentity = ObjectIdentity
cabletron = _Cabletron_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52)
)
_Mibs_ObjectIdentity = ObjectIdentity
mibs = _Mibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4)
)
_CtronExp_ObjectIdentity = ObjectIdentity
ctronExp = _CtronExp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2)
)
_CtVLANMib_ObjectIdentity = ObjectIdentity
ctVLANMib = _CtVLANMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12)
)
_CtVLANMgr_ObjectIdentity = ObjectIdentity
ctVLANMgr = _CtVLANMgr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1)
)
_CtPriority_ObjectIdentity = ObjectIdentity
ctPriority = _CtPriority_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 4)
)
_CtBasePriority_ObjectIdentity = ObjectIdentity
ctBasePriority = _CtBasePriority_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 4, 2)
)
_CtUserDefPriority_ObjectIdentity = ObjectIdentity
ctUserDefPriority = _CtUserDefPriority_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 4, 2, 1)
)
_CtUserDefTable_Object = MibTable
ctUserDefTable = _CtUserDefTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 4, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ctUserDefTable.setStatus("obsolete")
_CtUserDefEntry_Object = MibTableRow
ctUserDefEntry = _CtUserDefEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 4, 2, 1, 1, 1)
)
ctUserDefEntry.setIndexNames(
    (0, "CT-PRIORITY-QUEUING", "ctUserDefPriorityIndex"),
)
if mibBuilder.loadTexts:
    ctUserDefEntry.setStatus("obsolete")
_CtUserDefPriorityIndex_Type = Integer32
_CtUserDefPriorityIndex_Object = MibTableColumn
ctUserDefPriorityIndex = _CtUserDefPriorityIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 4, 2, 1, 1, 1, 1),
    _CtUserDefPriorityIndex_Type()
)
ctUserDefPriorityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctUserDefPriorityIndex.setStatus("obsolete")


class _CtUserDefPriorityValue_Type(Integer32):
    """Custom type ctUserDefPriorityValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_CtUserDefPriorityValue_Type.__name__ = "Integer32"
_CtUserDefPriorityValue_Object = MibTableColumn
ctUserDefPriorityValue = _CtUserDefPriorityValue_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 4, 2, 1, 1, 1, 2),
    _CtUserDefPriorityValue_Type()
)
ctUserDefPriorityValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctUserDefPriorityValue.setStatus("obsolete")


class _CtUserDefNumTrafficClass_Type(Integer32):
    """Custom type ctUserDefNumTrafficClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_CtUserDefNumTrafficClass_Type.__name__ = "Integer32"
_CtUserDefNumTrafficClass_Object = MibTableColumn
ctUserDefNumTrafficClass = _CtUserDefNumTrafficClass_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 4, 2, 1, 1, 1, 3),
    _CtUserDefNumTrafficClass_Type()
)
ctUserDefNumTrafficClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctUserDefNumTrafficClass.setStatus("obsolete")
_CtRegenPriority_ObjectIdentity = ObjectIdentity
ctRegenPriority = _CtRegenPriority_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 4, 2, 2)
)
_CtRegenerationTable_Object = MibTable
ctRegenerationTable = _CtRegenerationTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 4, 2, 2, 1)
)
if mibBuilder.loadTexts:
    ctRegenerationTable.setStatus("obsolete")
_CtRegenerationEntry_Object = MibTableRow
ctRegenerationEntry = _CtRegenerationEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 4, 2, 2, 1, 1)
)
ctRegenerationEntry.setIndexNames(
    (0, "CT-PRIORITY-QUEUING", "ctRegenerationIndex"),
    (0, "CT-PRIORITY-QUEUING", "ctRegenerationId"),
)
if mibBuilder.loadTexts:
    ctRegenerationEntry.setStatus("obsolete")
_CtRegenerationIndex_Type = Integer32
_CtRegenerationIndex_Object = MibTableColumn
ctRegenerationIndex = _CtRegenerationIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 4, 2, 2, 1, 1, 1),
    _CtRegenerationIndex_Type()
)
ctRegenerationIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctRegenerationIndex.setStatus("obsolete")
_CtRegenerationId_Type = Integer32
_CtRegenerationId_Object = MibTableColumn
ctRegenerationId = _CtRegenerationId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 4, 2, 2, 1, 1, 2),
    _CtRegenerationId_Type()
)
ctRegenerationId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctRegenerationId.setStatus("obsolete")


class _CtRegenerationValue_Type(Integer32):
    """Custom type ctRegenerationValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_CtRegenerationValue_Type.__name__ = "Integer32"
_CtRegenerationValue_Object = MibTableColumn
ctRegenerationValue = _CtRegenerationValue_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 4, 2, 2, 1, 1, 3),
    _CtRegenerationValue_Type()
)
ctRegenerationValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctRegenerationValue.setStatus("obsolete")
_CtTrafPriority_ObjectIdentity = ObjectIdentity
ctTrafPriority = _CtTrafPriority_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 4, 2, 3)
)
_CtTrafClassTable_Object = MibTable
ctTrafClassTable = _CtTrafClassTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 4, 2, 3, 1)
)
if mibBuilder.loadTexts:
    ctTrafClassTable.setStatus("obsolete")
_CtTrafClassEntry_Object = MibTableRow
ctTrafClassEntry = _CtTrafClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 4, 2, 3, 1, 1)
)
ctTrafClassEntry.setIndexNames(
    (0, "CT-PRIORITY-QUEUING", "ctTrafClassIndex"),
    (0, "CT-PRIORITY-QUEUING", "ctTrafClassId"),
)
if mibBuilder.loadTexts:
    ctTrafClassEntry.setStatus("obsolete")
_CtTrafClassIndex_Type = Integer32
_CtTrafClassIndex_Object = MibTableColumn
ctTrafClassIndex = _CtTrafClassIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 4, 2, 3, 1, 1, 1),
    _CtTrafClassIndex_Type()
)
ctTrafClassIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctTrafClassIndex.setStatus("obsolete")
_CtTrafClassId_Type = Integer32
_CtTrafClassId_Object = MibTableColumn
ctTrafClassId = _CtTrafClassId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 4, 2, 3, 1, 1, 2),
    _CtTrafClassId_Type()
)
ctTrafClassId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctTrafClassId.setStatus("obsolete")
_CtTrafClassValue_Type = Integer32
_CtTrafClassValue_Object = MibTableColumn
ctTrafClassValue = _CtTrafClassValue_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 4, 2, 3, 1, 1, 3),
    _CtTrafClassValue_Type()
)
ctTrafClassValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctTrafClassValue.setStatus("obsolete")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CT-PRIORITY-QUEUING",
    **{"cabletron": cabletron,
       "mibs": mibs,
       "ctronExp": ctronExp,
       "ctVLANMib": ctVLANMib,
       "ctVLANMgr": ctVLANMgr,
       "ctPriority": ctPriority,
       "ctBasePriority": ctBasePriority,
       "ctUserDefPriority": ctUserDefPriority,
       "ctUserDefTable": ctUserDefTable,
       "ctUserDefEntry": ctUserDefEntry,
       "ctUserDefPriorityIndex": ctUserDefPriorityIndex,
       "ctUserDefPriorityValue": ctUserDefPriorityValue,
       "ctUserDefNumTrafficClass": ctUserDefNumTrafficClass,
       "ctRegenPriority": ctRegenPriority,
       "ctRegenerationTable": ctRegenerationTable,
       "ctRegenerationEntry": ctRegenerationEntry,
       "ctRegenerationIndex": ctRegenerationIndex,
       "ctRegenerationId": ctRegenerationId,
       "ctRegenerationValue": ctRegenerationValue,
       "ctTrafPriority": ctTrafPriority,
       "ctTrafClassTable": ctTrafClassTable,
       "ctTrafClassEntry": ctTrafClassEntry,
       "ctTrafClassIndex": ctTrafClassIndex,
       "ctTrafClassId": ctTrafClassId,
       "ctTrafClassValue": ctTrafClassValue}
)
