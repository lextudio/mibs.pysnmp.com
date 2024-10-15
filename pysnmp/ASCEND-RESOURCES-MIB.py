# SNMP MIB module (ASCEND-RESOURCES-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-RESOURCES-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:42:40 2024
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

(resourcesGroup,) = mibBuilder.importSymbols(
    "ASCEND-MIB",
    "resourcesGroup")

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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ResourceUsageTable_Object = MibTable
resourceUsageTable = _ResourceUsageTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 27, 1)
)
if mibBuilder.loadTexts:
    resourceUsageTable.setStatus("mandatory")
_ResourceUsageEntry_Object = MibTableRow
resourceUsageEntry = _ResourceUsageEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 27, 1, 1)
)
resourceUsageEntry.setIndexNames(
    (0, "ASCEND-RESOURCES-MIB", "usageSlotIndex"),
)
if mibBuilder.loadTexts:
    resourceUsageEntry.setStatus("mandatory")
_UsageSlotIndex_Type = Integer32
_UsageSlotIndex_Object = MibTableColumn
usageSlotIndex = _UsageSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 529, 27, 1, 1, 1),
    _UsageSlotIndex_Type()
)
usageSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usageSlotIndex.setStatus("mandatory")
_UsageAvailable_Type = Integer32
_UsageAvailable_Object = MibTableColumn
usageAvailable = _UsageAvailable_Object(
    (1, 3, 6, 1, 4, 1, 529, 27, 1, 1, 2),
    _UsageAvailable_Type()
)
usageAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usageAvailable.setStatus("mandatory")
_UsageBusy_Type = Integer32
_UsageBusy_Object = MibTableColumn
usageBusy = _UsageBusy_Object(
    (1, 3, 6, 1, 4, 1, 529, 27, 1, 1, 3),
    _UsageBusy_Type()
)
usageBusy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usageBusy.setStatus("mandatory")
_UsageSuspect_Type = Integer32
_UsageSuspect_Object = MibTableColumn
usageSuspect = _UsageSuspect_Object(
    (1, 3, 6, 1, 4, 1, 529, 27, 1, 1, 4),
    _UsageSuspect_Type()
)
usageSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usageSuspect.setStatus("mandatory")
_UsageDisabled_Type = Integer32
_UsageDisabled_Object = MibTableColumn
usageDisabled = _UsageDisabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 27, 1, 1, 5),
    _UsageDisabled_Type()
)
usageDisabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usageDisabled.setStatus("mandatory")
_UsageDead_Type = Integer32
_UsageDead_Object = MibTableColumn
usageDead = _UsageDead_Object(
    (1, 3, 6, 1, 4, 1, 529, 27, 1, 1, 6),
    _UsageDead_Type()
)
usageDead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usageDead.setStatus("mandatory")
_ResourceTable_Object = MibTable
resourceTable = _ResourceTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 27, 2)
)
if mibBuilder.loadTexts:
    resourceTable.setStatus("mandatory")
_ResourceEntry_Object = MibTableRow
resourceEntry = _ResourceEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 27, 2, 1)
)
resourceEntry.setIndexNames(
    (0, "ASCEND-RESOURCES-MIB", "resourceSlotIndex"),
    (0, "ASCEND-RESOURCES-MIB", "resourcePortIndex"),
)
if mibBuilder.loadTexts:
    resourceEntry.setStatus("mandatory")
_ResourceSlotIndex_Type = Integer32
_ResourceSlotIndex_Object = MibTableColumn
resourceSlotIndex = _ResourceSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 529, 27, 2, 1, 1),
    _ResourceSlotIndex_Type()
)
resourceSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resourceSlotIndex.setStatus("mandatory")
_ResourcePortIndex_Type = Integer32
_ResourcePortIndex_Object = MibTableColumn
resourcePortIndex = _ResourcePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 529, 27, 2, 1, 2),
    _ResourcePortIndex_Type()
)
resourcePortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resourcePortIndex.setStatus("mandatory")


class _ResourceConfig_Type(Integer32):
    """Custom type resourceConfig based on Integer32"""
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
        *(("disable", 3),
          ("disableAndChannel", 4),
          ("enable", 2),
          ("other", 1))
    )


_ResourceConfig_Type.__name__ = "Integer32"
_ResourceConfig_Object = MibTableColumn
resourceConfig = _ResourceConfig_Object(
    (1, 3, 6, 1, 4, 1, 529, 27, 2, 1, 3),
    _ResourceConfig_Type()
)
resourceConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    resourceConfig.setStatus("mandatory")


class _ResourceState_Type(Integer32):
    """Custom type resourceState based on Integer32"""
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
        *(("disabled", 7),
          ("disabledChan", 8),
          ("failedPost", 3),
          ("idle", 4),
          ("notApplicable", 1),
          ("online", 5),
          ("other", 2),
          ("reserved", 9),
          ("virtualConnect", 6))
    )


_ResourceState_Type.__name__ = "Integer32"
_ResourceState_Object = MibTableColumn
resourceState = _ResourceState_Object(
    (1, 3, 6, 1, 4, 1, 529, 27, 2, 1, 4),
    _ResourceState_Type()
)
resourceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resourceState.setStatus("mandatory")


class _ResourceCallType_Type(Integer32):
    """Custom type resourceCallType based on Integer32"""
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
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("async", 3),
          ("isdnAsyncV110", 7),
          ("isdnAsyncV120", 6),
          ("isdnAsyncV32", 9),
          ("isdnAsyncVdsp", 10),
          ("isdnSync", 5),
          ("notApplicable", 1),
          ("other", 2),
          ("sync", 4),
          ("virtual", 8))
    )


_ResourceCallType_Type.__name__ = "Integer32"
_ResourceCallType_Object = MibTableColumn
resourceCallType = _ResourceCallType_Object(
    (1, 3, 6, 1, 4, 1, 529, 27, 2, 1, 5),
    _ResourceCallType_Type()
)
resourceCallType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resourceCallType.setStatus("mandatory")


class _ResourceCallDirection_Type(Integer32):
    """Custom type resourceCallDirection based on Integer32"""
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
        *(("answered", 4),
          ("notApplicable", 1),
          ("originated", 3),
          ("other", 2))
    )


_ResourceCallDirection_Type.__name__ = "Integer32"
_ResourceCallDirection_Object = MibTableColumn
resourceCallDirection = _ResourceCallDirection_Object(
    (1, 3, 6, 1, 4, 1, 529, 27, 2, 1, 6),
    _ResourceCallDirection_Type()
)
resourceCallDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resourceCallDirection.setStatus("mandatory")
_ResourceUsedCounts_Type = Counter32
_ResourceUsedCounts_Object = MibTableColumn
resourceUsedCounts = _ResourceUsedCounts_Object(
    (1, 3, 6, 1, 4, 1, 529, 27, 2, 1, 7),
    _ResourceUsedCounts_Type()
)
resourceUsedCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resourceUsedCounts.setStatus("mandatory")
_ResourceBadCounts_Type = Counter32
_ResourceBadCounts_Object = MibTableColumn
resourceBadCounts = _ResourceBadCounts_Object(
    (1, 3, 6, 1, 4, 1, 529, 27, 2, 1, 8),
    _ResourceBadCounts_Type()
)
resourceBadCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resourceBadCounts.setStatus("mandatory")
_ResourceLast32_Type = Integer32
_ResourceLast32_Object = MibTableColumn
resourceLast32 = _ResourceLast32_Object(
    (1, 3, 6, 1, 4, 1, 529, 27, 2, 1, 9),
    _ResourceLast32_Type()
)
resourceLast32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resourceLast32.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-RESOURCES-MIB",
    **{"resourceUsageTable": resourceUsageTable,
       "resourceUsageEntry": resourceUsageEntry,
       "usageSlotIndex": usageSlotIndex,
       "usageAvailable": usageAvailable,
       "usageBusy": usageBusy,
       "usageSuspect": usageSuspect,
       "usageDisabled": usageDisabled,
       "usageDead": usageDead,
       "resourceTable": resourceTable,
       "resourceEntry": resourceEntry,
       "resourceSlotIndex": resourceSlotIndex,
       "resourcePortIndex": resourcePortIndex,
       "resourceConfig": resourceConfig,
       "resourceState": resourceState,
       "resourceCallType": resourceCallType,
       "resourceCallDirection": resourceCallDirection,
       "resourceUsedCounts": resourceUsedCounts,
       "resourceBadCounts": resourceBadCounts,
       "resourceLast32": resourceLast32}
)
