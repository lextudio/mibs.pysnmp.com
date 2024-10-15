# SNMP MIB module (CTRON-SSR-L2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CTRON-SSR-L2-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:19:40 2024
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

(ssrMibs,) = mibBuilder.importSymbols(
    "CTRON-SSR-SMI-MIB",
    "ssrMibs")

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
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

l2MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 500)
)
l2MIB.setRevisions(
        ("1999-09-22 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_L2Group_ObjectIdentity = ObjectIdentity
l2Group = _L2Group_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 2)
)
_L2LearnedEntryDiscards_Type = Counter32
_L2LearnedEntryDiscards_Object = MibScalar
l2LearnedEntryDiscards = _L2LearnedEntryDiscards_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 2, 1),
    _L2LearnedEntryDiscards_Type()
)
l2LearnedEntryDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2LearnedEntryDiscards.setStatus("obsolete")
_L2LearnedMacEntries_Type = Counter32
_L2LearnedMacEntries_Object = MibScalar
l2LearnedMacEntries = _L2LearnedMacEntries_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 2, 2),
    _L2LearnedMacEntries_Type()
)
l2LearnedMacEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2LearnedMacEntries.setStatus("obsolete")
_L2LearnedFlowEntries_Type = Counter32
_L2LearnedFlowEntries_Object = MibScalar
l2LearnedFlowEntries = _L2LearnedFlowEntries_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 2, 3),
    _L2LearnedFlowEntries_Type()
)
l2LearnedFlowEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2LearnedFlowEntries.setStatus("obsolete")
_L2ForwardTable_Object = MibTable
l2ForwardTable = _L2ForwardTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 2, 4)
)
if mibBuilder.loadTexts:
    l2ForwardTable.setStatus("obsolete")
_L2ForwardEntry_Object = MibTableRow
l2ForwardEntry = _L2ForwardEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 2, 4, 1)
)
l2ForwardEntry.setIndexNames(
    (0, "CTRON-SSR-L2-MIB", "l2ForwardFilterId"),
    (0, "CTRON-SSR-L2-MIB", "l2ForwardDstMacAddr"),
    (0, "CTRON-SSR-L2-MIB", "l2ForwardSrcMacAddr"),
    (0, "CTRON-SSR-L2-MIB", "l2ForwardVlanId"),
)
if mibBuilder.loadTexts:
    l2ForwardEntry.setStatus("obsolete")


class _L2ForwardFilterId_Type(Integer32):
    """Custom type l2ForwardFilterId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 14),
    )


_L2ForwardFilterId_Type.__name__ = "Integer32"
_L2ForwardFilterId_Object = MibTableColumn
l2ForwardFilterId = _L2ForwardFilterId_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 2, 4, 1, 1),
    _L2ForwardFilterId_Type()
)
l2ForwardFilterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2ForwardFilterId.setStatus("obsolete")
_L2ForwardDstMacAddr_Type = PhysAddress
_L2ForwardDstMacAddr_Object = MibTableColumn
l2ForwardDstMacAddr = _L2ForwardDstMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 2, 4, 1, 2),
    _L2ForwardDstMacAddr_Type()
)
l2ForwardDstMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2ForwardDstMacAddr.setStatus("obsolete")
_L2ForwardSrcMacAddr_Type = PhysAddress
_L2ForwardSrcMacAddr_Object = MibTableColumn
l2ForwardSrcMacAddr = _L2ForwardSrcMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 2, 4, 1, 3),
    _L2ForwardSrcMacAddr_Type()
)
l2ForwardSrcMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2ForwardSrcMacAddr.setStatus("obsolete")


class _L2ForwardVlanId_Type(Integer32):
    """Custom type l2ForwardVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_L2ForwardVlanId_Type.__name__ = "Integer32"
_L2ForwardVlanId_Object = MibTableColumn
l2ForwardVlanId = _L2ForwardVlanId_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 2, 4, 1, 4),
    _L2ForwardVlanId_Type()
)
l2ForwardVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2ForwardVlanId.setStatus("obsolete")


class _L2ForwardDstPort_Type(Integer32):
    """Custom type l2ForwardDstPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_L2ForwardDstPort_Type.__name__ = "Integer32"
_L2ForwardDstPort_Object = MibTableColumn
l2ForwardDstPort = _L2ForwardDstPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 2, 4, 1, 5),
    _L2ForwardDstPort_Type()
)
l2ForwardDstPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2ForwardDstPort.setStatus("obsolete")


class _L2ForwardInPorts_Type(OctetString):
    """Custom type l2ForwardInPorts based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_L2ForwardInPorts_Type.__name__ = "OctetString"
_L2ForwardInPorts_Object = MibTableColumn
l2ForwardInPorts = _L2ForwardInPorts_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 2, 4, 1, 6),
    _L2ForwardInPorts_Type()
)
l2ForwardInPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2ForwardInPorts.setStatus("obsolete")
_L2PriorityTable_Object = MibTable
l2PriorityTable = _L2PriorityTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 2, 5)
)
if mibBuilder.loadTexts:
    l2PriorityTable.setStatus("obsolete")
_L2PriorityEntry_Object = MibTableRow
l2PriorityEntry = _L2PriorityEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 2, 5, 1)
)
l2PriorityEntry.setIndexNames(
    (0, "CTRON-SSR-L2-MIB", "l2PriorityIndex"),
)
if mibBuilder.loadTexts:
    l2PriorityEntry.setStatus("obsolete")


class _L2PriorityIndex_Type(Integer32):
    """Custom type l2PriorityIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_L2PriorityIndex_Type.__name__ = "Integer32"
_L2PriorityIndex_Object = MibTableColumn
l2PriorityIndex = _L2PriorityIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 2, 5, 1, 1),
    _L2PriorityIndex_Type()
)
l2PriorityIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2PriorityIndex.setStatus("obsolete")


class _L2PriorityDesc_Type(OctetString):
    """Custom type l2PriorityDesc based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 25),
    )


_L2PriorityDesc_Type.__name__ = "OctetString"
_L2PriorityDesc_Object = MibTableColumn
l2PriorityDesc = _L2PriorityDesc_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 2, 5, 1, 2),
    _L2PriorityDesc_Type()
)
l2PriorityDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2PriorityDesc.setStatus("obsolete")
_L2PriorityDstMacAddr_Type = PhysAddress
_L2PriorityDstMacAddr_Object = MibTableColumn
l2PriorityDstMacAddr = _L2PriorityDstMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 2, 5, 1, 3),
    _L2PriorityDstMacAddr_Type()
)
l2PriorityDstMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2PriorityDstMacAddr.setStatus("obsolete")
_L2PrioritySrcMacAddr_Type = PhysAddress
_L2PrioritySrcMacAddr_Object = MibTableColumn
l2PrioritySrcMacAddr = _L2PrioritySrcMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 2, 5, 1, 4),
    _L2PrioritySrcMacAddr_Type()
)
l2PrioritySrcMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2PrioritySrcMacAddr.setStatus("obsolete")


class _L2PriorityVlanId_Type(Integer32):
    """Custom type l2PriorityVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_L2PriorityVlanId_Type.__name__ = "Integer32"
_L2PriorityVlanId_Object = MibTableColumn
l2PriorityVlanId = _L2PriorityVlanId_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 2, 5, 1, 5),
    _L2PriorityVlanId_Type()
)
l2PriorityVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2PriorityVlanId.setStatus("obsolete")


class _L2PriorityInPorts_Type(OctetString):
    """Custom type l2PriorityInPorts based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_L2PriorityInPorts_Type.__name__ = "OctetString"
_L2PriorityInPorts_Object = MibTableColumn
l2PriorityInPorts = _L2PriorityInPorts_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 2, 5, 1, 6),
    _L2PriorityInPorts_Type()
)
l2PriorityInPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2PriorityInPorts.setStatus("obsolete")


class _L2Priority_Type(Integer32):
    """Custom type l2Priority based on Integer32"""
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
        *(("control", 4),
          ("high", 3),
          ("low", 1),
          ("medium", 2))
    )


_L2Priority_Type.__name__ = "Integer32"
_L2Priority_Object = MibTableColumn
l2Priority = _L2Priority_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 2, 5, 1, 7),
    _L2Priority_Type()
)
l2Priority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2Priority.setStatus("obsolete")
_L2FilterTable_Object = MibTable
l2FilterTable = _L2FilterTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 2, 6)
)
if mibBuilder.loadTexts:
    l2FilterTable.setStatus("obsolete")
_L2FilterEntry_Object = MibTableRow
l2FilterEntry = _L2FilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 2, 6, 1)
)
l2FilterEntry.setIndexNames(
    (0, "CTRON-SSR-L2-MIB", "l2FilterIndex"),
)
if mibBuilder.loadTexts:
    l2FilterEntry.setStatus("obsolete")


class _L2FilterIndex_Type(Integer32):
    """Custom type l2FilterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_L2FilterIndex_Type.__name__ = "Integer32"
_L2FilterIndex_Object = MibTableColumn
l2FilterIndex = _L2FilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 2, 6, 1, 1),
    _L2FilterIndex_Type()
)
l2FilterIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2FilterIndex.setStatus("obsolete")


class _L2FilterDesc_Type(OctetString):
    """Custom type l2FilterDesc based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 25),
    )


_L2FilterDesc_Type.__name__ = "OctetString"
_L2FilterDesc_Object = MibTableColumn
l2FilterDesc = _L2FilterDesc_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 2, 6, 1, 2),
    _L2FilterDesc_Type()
)
l2FilterDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2FilterDesc.setStatus("obsolete")


class _L2FilterType_Type(Integer32):
    """Custom type l2FilterType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("addressFilter", 2),
          ("addressLock", 3),
          ("staticEntry", 1))
    )


_L2FilterType_Type.__name__ = "Integer32"
_L2FilterType_Object = MibTableColumn
l2FilterType = _L2FilterType_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 2, 6, 1, 3),
    _L2FilterType_Type()
)
l2FilterType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2FilterType.setStatus("obsolete")


class _L2FilterRestrictions_Type(Integer32):
    """Custom type l2FilterRestrictions based on Integer32"""
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
        *(("allow", 1),
          ("disallow", 2),
          ("force", 3),
          ("none", 4))
    )


_L2FilterRestrictions_Type.__name__ = "Integer32"
_L2FilterRestrictions_Object = MibTableColumn
l2FilterRestrictions = _L2FilterRestrictions_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 2, 6, 1, 4),
    _L2FilterRestrictions_Type()
)
l2FilterRestrictions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2FilterRestrictions.setStatus("obsolete")
_L2FilterSrcMacAddr_Type = PhysAddress
_L2FilterSrcMacAddr_Object = MibTableColumn
l2FilterSrcMacAddr = _L2FilterSrcMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 2, 6, 1, 5),
    _L2FilterSrcMacAddr_Type()
)
l2FilterSrcMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2FilterSrcMacAddr.setStatus("obsolete")
_L2FilterDstMacAddr_Type = PhysAddress
_L2FilterDstMacAddr_Object = MibTableColumn
l2FilterDstMacAddr = _L2FilterDstMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 2, 6, 1, 6),
    _L2FilterDstMacAddr_Type()
)
l2FilterDstMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2FilterDstMacAddr.setStatus("obsolete")


class _L2FilterVlanId_Type(Integer32):
    """Custom type l2FilterVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_L2FilterVlanId_Type.__name__ = "Integer32"
_L2FilterVlanId_Object = MibTableColumn
l2FilterVlanId = _L2FilterVlanId_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 2, 6, 1, 7),
    _L2FilterVlanId_Type()
)
l2FilterVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2FilterVlanId.setStatus("obsolete")


class _L2FilterInPorts_Type(OctetString):
    """Custom type l2FilterInPorts based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_L2FilterInPorts_Type.__name__ = "OctetString"
_L2FilterInPorts_Object = MibTableColumn
l2FilterInPorts = _L2FilterInPorts_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 2, 6, 1, 8),
    _L2FilterInPorts_Type()
)
l2FilterInPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2FilterInPorts.setStatus("obsolete")


class _L2FilterOutPorts_Type(OctetString):
    """Custom type l2FilterOutPorts based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_L2FilterOutPorts_Type.__name__ = "OctetString"
_L2FilterOutPorts_Object = MibTableColumn
l2FilterOutPorts = _L2FilterOutPorts_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 2, 6, 1, 9),
    _L2FilterOutPorts_Type()
)
l2FilterOutPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2FilterOutPorts.setStatus("obsolete")
_L2PortSecurityTable_Object = MibTable
l2PortSecurityTable = _L2PortSecurityTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 2, 7)
)
if mibBuilder.loadTexts:
    l2PortSecurityTable.setStatus("obsolete")
_L2PortSecurityEntry_Object = MibTableRow
l2PortSecurityEntry = _L2PortSecurityEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 2, 7, 1)
)
l2PortSecurityEntry.setIndexNames(
    (0, "CTRON-SSR-L2-MIB", "l2PortSecurityIndex"),
)
if mibBuilder.loadTexts:
    l2PortSecurityEntry.setStatus("obsolete")


class _L2PortSecurityIndex_Type(Integer32):
    """Custom type l2PortSecurityIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_L2PortSecurityIndex_Type.__name__ = "Integer32"
_L2PortSecurityIndex_Object = MibTableColumn
l2PortSecurityIndex = _L2PortSecurityIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 2, 7, 1, 1),
    _L2PortSecurityIndex_Type()
)
l2PortSecurityIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2PortSecurityIndex.setStatus("obsolete")


class _L2PortSecurityDesc_Type(OctetString):
    """Custom type l2PortSecurityDesc based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 25),
    )


_L2PortSecurityDesc_Type.__name__ = "OctetString"
_L2PortSecurityDesc_Object = MibTableColumn
l2PortSecurityDesc = _L2PortSecurityDesc_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 2, 7, 1, 2),
    _L2PortSecurityDesc_Type()
)
l2PortSecurityDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2PortSecurityDesc.setStatus("obsolete")


class _L2PortSecurityType_Type(Integer32):
    """Custom type l2PortSecurityType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("destinationSecure", 2),
          ("sourceSecure", 1))
    )


_L2PortSecurityType_Type.__name__ = "Integer32"
_L2PortSecurityType_Object = MibTableColumn
l2PortSecurityType = _L2PortSecurityType_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 2, 7, 1, 3),
    _L2PortSecurityType_Type()
)
l2PortSecurityType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2PortSecurityType.setStatus("obsolete")


class _L2PortSecurityVlanId_Type(Integer32):
    """Custom type l2PortSecurityVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_L2PortSecurityVlanId_Type.__name__ = "Integer32"
_L2PortSecurityVlanId_Object = MibTableColumn
l2PortSecurityVlanId = _L2PortSecurityVlanId_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 2, 7, 1, 4),
    _L2PortSecurityVlanId_Type()
)
l2PortSecurityVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2PortSecurityVlanId.setStatus("obsolete")


class _L2PortSecurityInPorts_Type(OctetString):
    """Custom type l2PortSecurityInPorts based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_L2PortSecurityInPorts_Type.__name__ = "OctetString"
_L2PortSecurityInPorts_Object = MibTableColumn
l2PortSecurityInPorts = _L2PortSecurityInPorts_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 2, 7, 1, 5),
    _L2PortSecurityInPorts_Type()
)
l2PortSecurityInPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2PortSecurityInPorts.setStatus("obsolete")
_L2PortTable_Object = MibTable
l2PortTable = _L2PortTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 2, 8)
)
if mibBuilder.loadTexts:
    l2PortTable.setStatus("obsolete")
_L2PortEntry_Object = MibTableRow
l2PortEntry = _L2PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 2, 8, 1)
)
l2PortEntry.setIndexNames(
    (0, "CTRON-SSR-L2-MIB", "l2Port"),
)
if mibBuilder.loadTexts:
    l2PortEntry.setStatus("obsolete")


class _L2Port_Type(Integer32):
    """Custom type l2Port based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_L2Port_Type.__name__ = "Integer32"
_L2Port_Object = MibTableColumn
l2Port = _L2Port_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 2, 8, 1, 1),
    _L2Port_Type()
)
l2Port.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2Port.setStatus("obsolete")


class _L2PortAgingStatus_Type(Integer32):
    """Custom type l2PortAgingStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_L2PortAgingStatus_Type.__name__ = "Integer32"
_L2PortAgingStatus_Object = MibTableColumn
l2PortAgingStatus = _L2PortAgingStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 2, 8, 1, 2),
    _L2PortAgingStatus_Type()
)
l2PortAgingStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2PortAgingStatus.setStatus("obsolete")


class _L2PortAgingTime_Type(Integer32):
    """Custom type l2PortAgingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 1000000),
    )


_L2PortAgingTime_Type.__name__ = "Integer32"
_L2PortAgingTime_Object = MibTableColumn
l2PortAgingTime = _L2PortAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 2, 8, 1, 3),
    _L2PortAgingTime_Type()
)
l2PortAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2PortAgingTime.setStatus("obsolete")


class _L2PortDemandAgeHiBound_Type(Integer32):
    """Custom type l2PortDemandAgeHiBound based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_L2PortDemandAgeHiBound_Type.__name__ = "Integer32"
_L2PortDemandAgeHiBound_Object = MibTableColumn
l2PortDemandAgeHiBound = _L2PortDemandAgeHiBound_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 2, 8, 1, 4),
    _L2PortDemandAgeHiBound_Type()
)
l2PortDemandAgeHiBound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2PortDemandAgeHiBound.setStatus("obsolete")


class _L2PortDemandAgeLowBound_Type(Integer32):
    """Custom type l2PortDemandAgeLowBound based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_L2PortDemandAgeLowBound_Type.__name__ = "Integer32"
_L2PortDemandAgeLowBound_Object = MibTableColumn
l2PortDemandAgeLowBound = _L2PortDemandAgeLowBound_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 2, 8, 1, 5),
    _L2PortDemandAgeLowBound_Type()
)
l2PortDemandAgeLowBound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2PortDemandAgeLowBound.setStatus("obsolete")
_L2PortDemandAgeCount_Type = Counter32
_L2PortDemandAgeCount_Object = MibTableColumn
l2PortDemandAgeCount = _L2PortDemandAgeCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 2, 8, 1, 6),
    _L2PortDemandAgeCount_Type()
)
l2PortDemandAgeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2PortDemandAgeCount.setStatus("obsolete")
_L2PortLearnedEntryDiscards_Type = Counter32
_L2PortLearnedEntryDiscards_Object = MibTableColumn
l2PortLearnedEntryDiscards = _L2PortLearnedEntryDiscards_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 2, 8, 1, 7),
    _L2PortLearnedEntryDiscards_Type()
)
l2PortLearnedEntryDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2PortLearnedEntryDiscards.setStatus("obsolete")
_L2PortSrcEntries_Type = Counter32
_L2PortSrcEntries_Object = MibTableColumn
l2PortSrcEntries = _L2PortSrcEntries_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 2, 8, 1, 8),
    _L2PortSrcEntries_Type()
)
l2PortSrcEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2PortSrcEntries.setStatus("obsolete")
_L2PortDstEntries_Type = Counter32
_L2PortDstEntries_Object = MibTableColumn
l2PortDstEntries = _L2PortDstEntries_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 2, 8, 1, 9),
    _L2PortDstEntries_Type()
)
l2PortDstEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2PortDstEntries.setStatus("obsolete")
_L2PortMgmtEntries_Type = Counter32
_L2PortMgmtEntries_Object = MibTableColumn
l2PortMgmtEntries = _L2PortMgmtEntries_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 2, 8, 1, 10),
    _L2PortMgmtEntries_Type()
)
l2PortMgmtEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2PortMgmtEntries.setStatus("obsolete")


class _L2PortMaxInfo_Type(Integer32):
    """Custom type l2PortMaxInfo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_L2PortMaxInfo_Type.__name__ = "Integer32"
_L2PortMaxInfo_Object = MibTableColumn
l2PortMaxInfo = _L2PortMaxInfo_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 2, 8, 1, 11),
    _L2PortMaxInfo_Type()
)
l2PortMaxInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2PortMaxInfo.setStatus("obsolete")
_L2PortInFrames_Type = Counter32
_L2PortInFrames_Object = MibTableColumn
l2PortInFrames = _L2PortInFrames_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 2, 8, 1, 12),
    _L2PortInFrames_Type()
)
l2PortInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2PortInFrames.setStatus("obsolete")
_L2PortOutFrames_Type = Counter32
_L2PortOutFrames_Object = MibTableColumn
l2PortOutFrames = _L2PortOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 2, 8, 1, 13),
    _L2PortOutFrames_Type()
)
l2PortOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2PortOutFrames.setStatus("obsolete")
_L2PortForwardTable_Object = MibTable
l2PortForwardTable = _L2PortForwardTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 2, 9)
)
if mibBuilder.loadTexts:
    l2PortForwardTable.setStatus("obsolete")
_L2PortForwardEntry_Object = MibTableRow
l2PortForwardEntry = _L2PortForwardEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 2, 9, 1)
)
l2PortForwardEntry.setIndexNames(
    (0, "CTRON-SSR-L2-MIB", "l2PortForwardPort"),
    (0, "CTRON-SSR-L2-MIB", "l2PortForwardIndex"),
)
if mibBuilder.loadTexts:
    l2PortForwardEntry.setStatus("obsolete")


class _L2PortForwardPort_Type(Integer32):
    """Custom type l2PortForwardPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_L2PortForwardPort_Type.__name__ = "Integer32"
_L2PortForwardPort_Object = MibTableColumn
l2PortForwardPort = _L2PortForwardPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 2, 9, 1, 1),
    _L2PortForwardPort_Type()
)
l2PortForwardPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2PortForwardPort.setStatus("obsolete")


class _L2PortForwardIndex_Type(Integer32):
    """Custom type l2PortForwardIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_L2PortForwardIndex_Type.__name__ = "Integer32"
_L2PortForwardIndex_Object = MibTableColumn
l2PortForwardIndex = _L2PortForwardIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 2, 9, 1, 2),
    _L2PortForwardIndex_Type()
)
l2PortForwardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2PortForwardIndex.setStatus("obsolete")
_L2PortForwardDstMacAddr_Type = PhysAddress
_L2PortForwardDstMacAddr_Object = MibTableColumn
l2PortForwardDstMacAddr = _L2PortForwardDstMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 2, 9, 1, 3),
    _L2PortForwardDstMacAddr_Type()
)
l2PortForwardDstMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2PortForwardDstMacAddr.setStatus("obsolete")
_L2PortForwardSrcMacAddr_Type = PhysAddress
_L2PortForwardSrcMacAddr_Object = MibTableColumn
l2PortForwardSrcMacAddr = _L2PortForwardSrcMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 2, 9, 1, 4),
    _L2PortForwardSrcMacAddr_Type()
)
l2PortForwardSrcMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2PortForwardSrcMacAddr.setStatus("obsolete")


class _L2PortForwardVlanId_Type(Integer32):
    """Custom type l2PortForwardVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_L2PortForwardVlanId_Type.__name__ = "Integer32"
_L2PortForwardVlanId_Object = MibTableColumn
l2PortForwardVlanId = _L2PortForwardVlanId_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 2, 9, 1, 5),
    _L2PortForwardVlanId_Type()
)
l2PortForwardVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2PortForwardVlanId.setStatus("obsolete")


class _L2PortForwardDstPort_Type(Integer32):
    """Custom type l2PortForwardDstPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_L2PortForwardDstPort_Type.__name__ = "Integer32"
_L2PortForwardDstPort_Object = MibTableColumn
l2PortForwardDstPort = _L2PortForwardDstPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 2, 9, 1, 6),
    _L2PortForwardDstPort_Type()
)
l2PortForwardDstPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2PortForwardDstPort.setStatus("obsolete")


class _L2PortForwardStatus_Type(Integer32):
    """Custom type l2PortForwardStatus based on Integer32"""
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
        *(("invalid", 2),
          ("learned", 3),
          ("mgmt", 5),
          ("other", 1),
          ("self", 4))
    )


_L2PortForwardStatus_Type.__name__ = "Integer32"
_L2PortForwardStatus_Object = MibTableColumn
l2PortForwardStatus = _L2PortForwardStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 2, 9, 1, 7),
    _L2PortForwardStatus_Type()
)
l2PortForwardStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2PortForwardStatus.setStatus("obsolete")
_L2PortForwardLastDetectedTime_Type = TimeTicks
_L2PortForwardLastDetectedTime_Object = MibTableColumn
l2PortForwardLastDetectedTime = _L2PortForwardLastDetectedTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 2, 9, 1, 8),
    _L2PortForwardLastDetectedTime_Type()
)
l2PortForwardLastDetectedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2PortForwardLastDetectedTime.setStatus("obsolete")
_L2Conformance_ObjectIdentity = ObjectIdentity
l2Conformance = _L2Conformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 500, 2)
)
_L2Compliances_ObjectIdentity = ObjectIdentity
l2Compliances = _L2Compliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 500, 2, 1)
)
_L2Groups_ObjectIdentity = ObjectIdentity
l2Groups = _L2Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 500, 2, 2)
)

# Managed Objects groups

l2ConfGroupV10 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 500, 2, 2, 1)
)
l2ConfGroupV10.setObjects(
      *(("CTRON-SSR-L2-MIB", "l2LearnedEntryDiscards"),
        ("CTRON-SSR-L2-MIB", "l2LearnedMacEntries"),
        ("CTRON-SSR-L2-MIB", "l2LearnedFlowEntries"),
        ("CTRON-SSR-L2-MIB", "l2ForwardFilterId"),
        ("CTRON-SSR-L2-MIB", "l2ForwardDstMacAddr"),
        ("CTRON-SSR-L2-MIB", "l2ForwardSrcMacAddr"),
        ("CTRON-SSR-L2-MIB", "l2ForwardVlanId"),
        ("CTRON-SSR-L2-MIB", "l2ForwardDstPort"),
        ("CTRON-SSR-L2-MIB", "l2ForwardInPorts"),
        ("CTRON-SSR-L2-MIB", "l2PriorityIndex"),
        ("CTRON-SSR-L2-MIB", "l2PriorityDesc"),
        ("CTRON-SSR-L2-MIB", "l2PriorityDstMacAddr"),
        ("CTRON-SSR-L2-MIB", "l2PrioritySrcMacAddr"),
        ("CTRON-SSR-L2-MIB", "l2PriorityVlanId"),
        ("CTRON-SSR-L2-MIB", "l2PriorityInPorts"),
        ("CTRON-SSR-L2-MIB", "l2Priority"),
        ("CTRON-SSR-L2-MIB", "l2FilterIndex"),
        ("CTRON-SSR-L2-MIB", "l2FilterDesc"),
        ("CTRON-SSR-L2-MIB", "l2FilterType"),
        ("CTRON-SSR-L2-MIB", "l2FilterRestrictions"),
        ("CTRON-SSR-L2-MIB", "l2FilterSrcMacAddr"),
        ("CTRON-SSR-L2-MIB", "l2FilterDstMacAddr"),
        ("CTRON-SSR-L2-MIB", "l2FilterVlanId"),
        ("CTRON-SSR-L2-MIB", "l2FilterInPorts"),
        ("CTRON-SSR-L2-MIB", "l2FilterOutPorts"),
        ("CTRON-SSR-L2-MIB", "l2PortSecurityIndex"),
        ("CTRON-SSR-L2-MIB", "l2PortSecurityDesc"),
        ("CTRON-SSR-L2-MIB", "l2PortSecurityType"),
        ("CTRON-SSR-L2-MIB", "l2PortSecurityVlanId"),
        ("CTRON-SSR-L2-MIB", "l2PortSecurityInPorts"),
        ("CTRON-SSR-L2-MIB", "l2Port"),
        ("CTRON-SSR-L2-MIB", "l2PortAgingStatus"),
        ("CTRON-SSR-L2-MIB", "l2PortAgingTime"),
        ("CTRON-SSR-L2-MIB", "l2PortDemandAgeHiBound"),
        ("CTRON-SSR-L2-MIB", "l2PortDemandAgeLowBound"),
        ("CTRON-SSR-L2-MIB", "l2PortDemandAgeCount"),
        ("CTRON-SSR-L2-MIB", "l2PortLearnedEntryDiscards"),
        ("CTRON-SSR-L2-MIB", "l2PortSrcEntries"),
        ("CTRON-SSR-L2-MIB", "l2PortDstEntries"),
        ("CTRON-SSR-L2-MIB", "l2PortMgmtEntries"),
        ("CTRON-SSR-L2-MIB", "l2PortMaxInfo"),
        ("CTRON-SSR-L2-MIB", "l2PortInFrames"),
        ("CTRON-SSR-L2-MIB", "l2PortOutFrames"),
        ("CTRON-SSR-L2-MIB", "l2PortForwardPort"),
        ("CTRON-SSR-L2-MIB", "l2PortForwardIndex"),
        ("CTRON-SSR-L2-MIB", "l2PortForwardDstMacAddr"),
        ("CTRON-SSR-L2-MIB", "l2PortForwardSrcMacAddr"),
        ("CTRON-SSR-L2-MIB", "l2PortForwardVlanId"),
        ("CTRON-SSR-L2-MIB", "l2PortForwardDstPort"),
        ("CTRON-SSR-L2-MIB", "l2PortForwardStatus"),
        ("CTRON-SSR-L2-MIB", "l2PortForwardLastDetectedTime"))
)
if mibBuilder.loadTexts:
    l2ConfGroupV10.setStatus("obsolete")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

l2ComplianceV10 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 500, 2, 2, 1, 1)
)
if mibBuilder.loadTexts:
    l2ComplianceV10.setStatus(
        "obsolete"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CTRON-SSR-L2-MIB",
    **{"l2Group": l2Group,
       "l2LearnedEntryDiscards": l2LearnedEntryDiscards,
       "l2LearnedMacEntries": l2LearnedMacEntries,
       "l2LearnedFlowEntries": l2LearnedFlowEntries,
       "l2ForwardTable": l2ForwardTable,
       "l2ForwardEntry": l2ForwardEntry,
       "l2ForwardFilterId": l2ForwardFilterId,
       "l2ForwardDstMacAddr": l2ForwardDstMacAddr,
       "l2ForwardSrcMacAddr": l2ForwardSrcMacAddr,
       "l2ForwardVlanId": l2ForwardVlanId,
       "l2ForwardDstPort": l2ForwardDstPort,
       "l2ForwardInPorts": l2ForwardInPorts,
       "l2PriorityTable": l2PriorityTable,
       "l2PriorityEntry": l2PriorityEntry,
       "l2PriorityIndex": l2PriorityIndex,
       "l2PriorityDesc": l2PriorityDesc,
       "l2PriorityDstMacAddr": l2PriorityDstMacAddr,
       "l2PrioritySrcMacAddr": l2PrioritySrcMacAddr,
       "l2PriorityVlanId": l2PriorityVlanId,
       "l2PriorityInPorts": l2PriorityInPorts,
       "l2Priority": l2Priority,
       "l2FilterTable": l2FilterTable,
       "l2FilterEntry": l2FilterEntry,
       "l2FilterIndex": l2FilterIndex,
       "l2FilterDesc": l2FilterDesc,
       "l2FilterType": l2FilterType,
       "l2FilterRestrictions": l2FilterRestrictions,
       "l2FilterSrcMacAddr": l2FilterSrcMacAddr,
       "l2FilterDstMacAddr": l2FilterDstMacAddr,
       "l2FilterVlanId": l2FilterVlanId,
       "l2FilterInPorts": l2FilterInPorts,
       "l2FilterOutPorts": l2FilterOutPorts,
       "l2PortSecurityTable": l2PortSecurityTable,
       "l2PortSecurityEntry": l2PortSecurityEntry,
       "l2PortSecurityIndex": l2PortSecurityIndex,
       "l2PortSecurityDesc": l2PortSecurityDesc,
       "l2PortSecurityType": l2PortSecurityType,
       "l2PortSecurityVlanId": l2PortSecurityVlanId,
       "l2PortSecurityInPorts": l2PortSecurityInPorts,
       "l2PortTable": l2PortTable,
       "l2PortEntry": l2PortEntry,
       "l2Port": l2Port,
       "l2PortAgingStatus": l2PortAgingStatus,
       "l2PortAgingTime": l2PortAgingTime,
       "l2PortDemandAgeHiBound": l2PortDemandAgeHiBound,
       "l2PortDemandAgeLowBound": l2PortDemandAgeLowBound,
       "l2PortDemandAgeCount": l2PortDemandAgeCount,
       "l2PortLearnedEntryDiscards": l2PortLearnedEntryDiscards,
       "l2PortSrcEntries": l2PortSrcEntries,
       "l2PortDstEntries": l2PortDstEntries,
       "l2PortMgmtEntries": l2PortMgmtEntries,
       "l2PortMaxInfo": l2PortMaxInfo,
       "l2PortInFrames": l2PortInFrames,
       "l2PortOutFrames": l2PortOutFrames,
       "l2PortForwardTable": l2PortForwardTable,
       "l2PortForwardEntry": l2PortForwardEntry,
       "l2PortForwardPort": l2PortForwardPort,
       "l2PortForwardIndex": l2PortForwardIndex,
       "l2PortForwardDstMacAddr": l2PortForwardDstMacAddr,
       "l2PortForwardSrcMacAddr": l2PortForwardSrcMacAddr,
       "l2PortForwardVlanId": l2PortForwardVlanId,
       "l2PortForwardDstPort": l2PortForwardDstPort,
       "l2PortForwardStatus": l2PortForwardStatus,
       "l2PortForwardLastDetectedTime": l2PortForwardLastDetectedTime,
       "l2MIB": l2MIB,
       "l2Conformance": l2Conformance,
       "l2Compliances": l2Compliances,
       "l2Groups": l2Groups,
       "l2ConfGroupV10": l2ConfGroupV10,
       "l2ComplianceV10": l2ComplianceV10}
)
