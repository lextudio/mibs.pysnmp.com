# SNMP MIB module (RADLAN-ETS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RADLAN-ETS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:42:18 2024
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
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

(PortList,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList")

(Percents,
 rnd) = mibBuilder.importSymbols(
    "RADLAN-MIB",
    "Percents",
    "rnd")

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
 RowPointer,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowPointer",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

rlEtsMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 89, 201)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class EtsPriorityGroupType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              15)
        )
    )
    namedValues = NamedValues(
        *(("priorityGroup0", 0),
          ("priorityGroup1", 1),
          ("priorityGroup15", 15),
          ("priorityGroup2", 2),
          ("priorityGroup3", 3),
          ("priorityGroup4", 4),
          ("priorityGroup5", 5),
          ("priorityGroup6", 6),
          ("priorityGroup7", 7))
    )



class EtsAdminStatusReasonType(Integer32, TextualConvention):
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
        *(("not-highest-queue", 4),
          ("ok", 1),
          ("too-many-groups", 2),
          ("too-many-queues", 3))
    )



# MIB Managed Objects in the order of their OIDs



class _RlEtsFeatureStatus_Type(TruthValue):
    """Custom type rlEtsFeatureStatus based on TruthValue"""


_RlEtsFeatureStatus_Object = MibScalar
rlEtsFeatureStatus = _RlEtsFeatureStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 201, 1),
    _RlEtsFeatureStatus_Type()
)
rlEtsFeatureStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlEtsFeatureStatus.setStatus("current")
_RlEtsPriorityGroupMappingTable_Object = MibTable
rlEtsPriorityGroupMappingTable = _RlEtsPriorityGroupMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 201, 2)
)
if mibBuilder.loadTexts:
    rlEtsPriorityGroupMappingTable.setStatus("current")
_RlEtsPriorityGroupMappingEntry_Object = MibTableRow
rlEtsPriorityGroupMappingEntry = _RlEtsPriorityGroupMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 201, 2, 1)
)
rlEtsPriorityGroupMappingEntry.setIndexNames(
    (0, "RADLAN-ETS-MIB", "rlEtsPriorityGroupMapping8021QPrio"),
)
if mibBuilder.loadTexts:
    rlEtsPriorityGroupMappingEntry.setStatus("current")


class _RlEtsPriorityGroupMapping8021QPrio_Type(Integer32):
    """Custom type rlEtsPriorityGroupMapping8021QPrio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_RlEtsPriorityGroupMapping8021QPrio_Type.__name__ = "Integer32"
_RlEtsPriorityGroupMapping8021QPrio_Object = MibTableColumn
rlEtsPriorityGroupMapping8021QPrio = _RlEtsPriorityGroupMapping8021QPrio_Object(
    (1, 3, 6, 1, 4, 1, 89, 201, 2, 1, 1),
    _RlEtsPriorityGroupMapping8021QPrio_Type()
)
rlEtsPriorityGroupMapping8021QPrio.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlEtsPriorityGroupMapping8021QPrio.setStatus("current")


class _RlEtsPriorityGroupMappingAdminPG_Type(EtsPriorityGroupType):
    """Custom type rlEtsPriorityGroupMappingAdminPG based on EtsPriorityGroupType"""


_RlEtsPriorityGroupMappingAdminPG_Object = MibTableColumn
rlEtsPriorityGroupMappingAdminPG = _RlEtsPriorityGroupMappingAdminPG_Object(
    (1, 3, 6, 1, 4, 1, 89, 201, 2, 1, 2),
    _RlEtsPriorityGroupMappingAdminPG_Type()
)
rlEtsPriorityGroupMappingAdminPG.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlEtsPriorityGroupMappingAdminPG.setStatus("current")


class _RlEtsPriorityGroupMappingOperPG_Type(EtsPriorityGroupType):
    """Custom type rlEtsPriorityGroupMappingOperPG based on EtsPriorityGroupType"""


_RlEtsPriorityGroupMappingOperPG_Object = MibTableColumn
rlEtsPriorityGroupMappingOperPG = _RlEtsPriorityGroupMappingOperPG_Object(
    (1, 3, 6, 1, 4, 1, 89, 201, 2, 1, 3),
    _RlEtsPriorityGroupMappingOperPG_Type()
)
rlEtsPriorityGroupMappingOperPG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlEtsPriorityGroupMappingOperPG.setStatus("current")
_RlEtsPriorityGroupMappingStatus_Type = RowStatus
_RlEtsPriorityGroupMappingStatus_Object = MibTableColumn
rlEtsPriorityGroupMappingStatus = _RlEtsPriorityGroupMappingStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 201, 2, 1, 4),
    _RlEtsPriorityGroupMappingStatus_Type()
)
rlEtsPriorityGroupMappingStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlEtsPriorityGroupMappingStatus.setStatus("current")


class _RlEtsPriorityGroupMappingProblemReason_Type(EtsAdminStatusReasonType):
    """Custom type rlEtsPriorityGroupMappingProblemReason based on EtsAdminStatusReasonType"""


_RlEtsPriorityGroupMappingProblemReason_Object = MibScalar
rlEtsPriorityGroupMappingProblemReason = _RlEtsPriorityGroupMappingProblemReason_Object(
    (1, 3, 6, 1, 4, 1, 89, 201, 3),
    _RlEtsPriorityGroupMappingProblemReason_Type()
)
rlEtsPriorityGroupMappingProblemReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlEtsPriorityGroupMappingProblemReason.setStatus("current")


class _RlEtsPriorityGroupMappingProblemIndex_Type(Integer32):
    """Custom type rlEtsPriorityGroupMappingProblemIndex based on Integer32"""
    defaultValue = 0


_RlEtsPriorityGroupMappingProblemIndex_Object = MibScalar
rlEtsPriorityGroupMappingProblemIndex = _RlEtsPriorityGroupMappingProblemIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 201, 4),
    _RlEtsPriorityGroupMappingProblemIndex_Type()
)
rlEtsPriorityGroupMappingProblemIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlEtsPriorityGroupMappingProblemIndex.setStatus("current")


class _RlEtsPriorityGroupBwAlloc_Type(OctetString):
    """Custom type rlEtsPriorityGroupBwAlloc based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_RlEtsPriorityGroupBwAlloc_Type.__name__ = "OctetString"
_RlEtsPriorityGroupBwAlloc_Object = MibScalar
rlEtsPriorityGroupBwAlloc = _RlEtsPriorityGroupBwAlloc_Object(
    (1, 3, 6, 1, 4, 1, 89, 201, 5),
    _RlEtsPriorityGroupBwAlloc_Type()
)
rlEtsPriorityGroupBwAlloc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlEtsPriorityGroupBwAlloc.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RADLAN-ETS-MIB",
    **{"EtsPriorityGroupType": EtsPriorityGroupType,
       "EtsAdminStatusReasonType": EtsAdminStatusReasonType,
       "rlEtsMib": rlEtsMib,
       "rlEtsFeatureStatus": rlEtsFeatureStatus,
       "rlEtsPriorityGroupMappingTable": rlEtsPriorityGroupMappingTable,
       "rlEtsPriorityGroupMappingEntry": rlEtsPriorityGroupMappingEntry,
       "rlEtsPriorityGroupMapping8021QPrio": rlEtsPriorityGroupMapping8021QPrio,
       "rlEtsPriorityGroupMappingAdminPG": rlEtsPriorityGroupMappingAdminPG,
       "rlEtsPriorityGroupMappingOperPG": rlEtsPriorityGroupMappingOperPG,
       "rlEtsPriorityGroupMappingStatus": rlEtsPriorityGroupMappingStatus,
       "rlEtsPriorityGroupMappingProblemReason": rlEtsPriorityGroupMappingProblemReason,
       "rlEtsPriorityGroupMappingProblemIndex": rlEtsPriorityGroupMappingProblemIndex,
       "rlEtsPriorityGroupBwAlloc": rlEtsPriorityGroupBwAlloc}
)
