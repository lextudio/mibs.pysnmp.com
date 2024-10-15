# SNMP MIB module (ADTRAN-AOS-QOS) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ADTRAN-AOS-QOS
# Produced by pysmi-1.5.4 at Mon Oct 14 20:34:13 2024
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

(adGenAOSConformance,
 adGenAOSRouter) = mibBuilder.importSymbols(
    "ADTRAN-AOS",
    "adGenAOSConformance",
    "adGenAOSRouter")

(adIdentity,) = mibBuilder.importSymbols(
    "ADTRAN-MIB",
    "adIdentity")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

adGenAOSQoSMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 53, 2, 1)
)
adGenAOSQoSMib.setRevisions(
        ("2011-06-17 00:00",
         "2011-05-17 00:00",
         "2010-05-19 00:00",
         "2009-03-04 00:00",
         "2008-09-16 00:00",
         "2008-08-20 00:00",
         "2008-07-11 00:00",
         "2008-06-25 00:00",
         "2008-06-06 00:00",
         "2008-06-04 00:00",
         "2008-04-17 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class Unsigned64(Counter64, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_AdGenAOSQos_ObjectIdentity = ObjectIdentity
adGenAOSQos = _AdGenAOSQos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 1)
)
_AdGenAOSQoSMapSetTable_Object = MibTable
adGenAOSQoSMapSetTable = _AdGenAOSQoSMapSetTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 1, 1)
)
if mibBuilder.loadTexts:
    adGenAOSQoSMapSetTable.setStatus("current")
_AdGenAOSQoSMapSetEntry_Object = MibTableRow
adGenAOSQoSMapSetEntry = _AdGenAOSQoSMapSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 1, 1, 1)
)
adGenAOSQoSMapSetEntry.setIndexNames(
    (0, "ADTRAN-AOS-QOS", "adGenAOSQoSMapSetId"),
)
if mibBuilder.loadTexts:
    adGenAOSQoSMapSetEntry.setStatus("current")
_AdGenAOSQoSMapSetId_Type = Unsigned32
_AdGenAOSQoSMapSetId_Object = MibTableColumn
adGenAOSQoSMapSetId = _AdGenAOSQoSMapSetId_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 1, 1, 1, 1),
    _AdGenAOSQoSMapSetId_Type()
)
adGenAOSQoSMapSetId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSQoSMapSetId.setStatus("current")
_AdGenAOSQoSMapSetName_Type = DisplayString
_AdGenAOSQoSMapSetName_Object = MibTableColumn
adGenAOSQoSMapSetName = _AdGenAOSQoSMapSetName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 1, 1, 1, 2),
    _AdGenAOSQoSMapSetName_Type()
)
adGenAOSQoSMapSetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSQoSMapSetName.setStatus("current")
_AdGenAOSQoSMapIsChild_Type = TruthValue
_AdGenAOSQoSMapIsChild_Object = MibTableColumn
adGenAOSQoSMapIsChild = _AdGenAOSQoSMapIsChild_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 1, 1, 1, 3),
    _AdGenAOSQoSMapIsChild_Type()
)
adGenAOSQoSMapIsChild.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSQoSMapIsChild.setStatus("current")
_AdGenAOSQoSMapEntriesTable_Object = MibTable
adGenAOSQoSMapEntriesTable = _AdGenAOSQoSMapEntriesTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 1, 2)
)
if mibBuilder.loadTexts:
    adGenAOSQoSMapEntriesTable.setStatus("current")
_AdGenAOSQoSMapEntriesEntry_Object = MibTableRow
adGenAOSQoSMapEntriesEntry = _AdGenAOSQoSMapEntriesEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 1, 2, 1)
)
adGenAOSQoSMapEntriesEntry.setIndexNames(
    (0, "ADTRAN-AOS-QOS", "adGenAOSQoSMapSetId"),
    (0, "ADTRAN-AOS-QOS", "adGenAOSQoSMapEntryId"),
)
if mibBuilder.loadTexts:
    adGenAOSQoSMapEntriesEntry.setStatus("current")
_AdGenAOSQoSMapEntryId_Type = Unsigned32
_AdGenAOSQoSMapEntryId_Object = MibTableColumn
adGenAOSQoSMapEntryId = _AdGenAOSQoSMapEntryId_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 1, 2, 1, 1),
    _AdGenAOSQoSMapEntryId_Type()
)
adGenAOSQoSMapEntryId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSQoSMapEntryId.setStatus("current")
_AdGenAOSQoSMapSeqNum_Type = Unsigned32
_AdGenAOSQoSMapSeqNum_Object = MibTableColumn
adGenAOSQoSMapSeqNum = _AdGenAOSQoSMapSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 1, 2, 1, 2),
    _AdGenAOSQoSMapSeqNum_Type()
)
adGenAOSQoSMapSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSQoSMapSeqNum.setStatus("current")
_AdGenAOSQoSMapEntrySetName_Type = DisplayString
_AdGenAOSQoSMapEntrySetName_Object = MibTableColumn
adGenAOSQoSMapEntrySetName = _AdGenAOSQoSMapEntrySetName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 1, 2, 1, 3),
    _AdGenAOSQoSMapEntrySetName_Type()
)
adGenAOSQoSMapEntrySetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSQoSMapEntrySetName.setStatus("current")
_AdGenAOSQoSMapChildSetName_Type = DisplayString
_AdGenAOSQoSMapChildSetName_Object = MibTableColumn
adGenAOSQoSMapChildSetName = _AdGenAOSQoSMapChildSetName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 1, 2, 1, 4),
    _AdGenAOSQoSMapChildSetName_Type()
)
adGenAOSQoSMapChildSetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSQoSMapChildSetName.setStatus("current")


class _AdGenAOSQoSMapQueuingActionType_Type(Integer32):
    """Custom type adGenAOSQoSMapQueuingActionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("classBased", 3),
          ("none", 1),
          ("priority", 2))
    )


_AdGenAOSQoSMapQueuingActionType_Type.__name__ = "Integer32"
_AdGenAOSQoSMapQueuingActionType_Object = MibTableColumn
adGenAOSQoSMapQueuingActionType = _AdGenAOSQoSMapQueuingActionType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 1, 2, 1, 5),
    _AdGenAOSQoSMapQueuingActionType_Type()
)
adGenAOSQoSMapQueuingActionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSQoSMapQueuingActionType.setStatus("current")


class _AdGenAOSQoSMapQueuingBWType_Type(Integer32):
    """Custom type adGenAOSQoSMapQueuingBWType based on Integer32"""
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
        *(("absolute", 2),
          ("none", 1),
          ("percent", 3),
          ("percentRemaining", 4))
    )


_AdGenAOSQoSMapQueuingBWType_Type.__name__ = "Integer32"
_AdGenAOSQoSMapQueuingBWType_Object = MibTableColumn
adGenAOSQoSMapQueuingBWType = _AdGenAOSQoSMapQueuingBWType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 1, 2, 1, 6),
    _AdGenAOSQoSMapQueuingBWType_Type()
)
adGenAOSQoSMapQueuingBWType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSQoSMapQueuingBWType.setStatus("current")
_AdGenAOSQoSMapQueuingBWValue_Type = Unsigned32
_AdGenAOSQoSMapQueuingBWValue_Object = MibTableColumn
adGenAOSQoSMapQueuingBWValue = _AdGenAOSQoSMapQueuingBWValue_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 1, 2, 1, 7),
    _AdGenAOSQoSMapQueuingBWValue_Type()
)
adGenAOSQoSMapQueuingBWValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSQoSMapQueuingBWValue.setStatus("current")
_AdGenAOSQoSMapQueuingBurstValue_Type = Unsigned32
_AdGenAOSQoSMapQueuingBurstValue_Object = MibTableColumn
adGenAOSQoSMapQueuingBurstValue = _AdGenAOSQoSMapQueuingBurstValue_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 1, 2, 1, 8),
    _AdGenAOSQoSMapQueuingBurstValue_Type()
)
adGenAOSQoSMapQueuingBurstValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSQoSMapQueuingBurstValue.setStatus("current")


class _AdGenAOSQoSMapMatchAll_Type(Integer32):
    """Custom type adGenAOSQoSMapMatchAll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AdGenAOSQoSMapMatchAll_Type.__name__ = "Integer32"
_AdGenAOSQoSMapMatchAll_Object = MibTableColumn
adGenAOSQoSMapMatchAll = _AdGenAOSQoSMapMatchAll_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 1, 2, 1, 9),
    _AdGenAOSQoSMapMatchAll_Type()
)
adGenAOSQoSMapMatchAll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSQoSMapMatchAll.setStatus("current")


class _AdGenAOSQoSMapDscpMarkState_Type(Integer32):
    """Custom type adGenAOSQoSMapDscpMarkState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AdGenAOSQoSMapDscpMarkState_Type.__name__ = "Integer32"
_AdGenAOSQoSMapDscpMarkState_Object = MibTableColumn
adGenAOSQoSMapDscpMarkState = _AdGenAOSQoSMapDscpMarkState_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 1, 2, 1, 10),
    _AdGenAOSQoSMapDscpMarkState_Type()
)
adGenAOSQoSMapDscpMarkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSQoSMapDscpMarkState.setStatus("current")
_AdGenAOSQoSMapDscpMarkValue_Type = Unsigned32
_AdGenAOSQoSMapDscpMarkValue_Object = MibTableColumn
adGenAOSQoSMapDscpMarkValue = _AdGenAOSQoSMapDscpMarkValue_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 1, 2, 1, 11),
    _AdGenAOSQoSMapDscpMarkValue_Type()
)
adGenAOSQoSMapDscpMarkValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSQoSMapDscpMarkValue.setStatus("current")
_AdGenAOSQoSMapDscpMarkString_Type = DisplayString
_AdGenAOSQoSMapDscpMarkString_Object = MibTableColumn
adGenAOSQoSMapDscpMarkString = _AdGenAOSQoSMapDscpMarkString_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 1, 2, 1, 12),
    _AdGenAOSQoSMapDscpMarkString_Type()
)
adGenAOSQoSMapDscpMarkString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSQoSMapDscpMarkString.setStatus("current")


class _AdGenAOSQoSMapPrecedenceMarkState_Type(Integer32):
    """Custom type adGenAOSQoSMapPrecedenceMarkState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AdGenAOSQoSMapPrecedenceMarkState_Type.__name__ = "Integer32"
_AdGenAOSQoSMapPrecedenceMarkState_Object = MibTableColumn
adGenAOSQoSMapPrecedenceMarkState = _AdGenAOSQoSMapPrecedenceMarkState_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 1, 2, 1, 13),
    _AdGenAOSQoSMapPrecedenceMarkState_Type()
)
adGenAOSQoSMapPrecedenceMarkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSQoSMapPrecedenceMarkState.setStatus("current")
_AdGenAOSQoSMapPrecedenceMarkValue_Type = Unsigned32
_AdGenAOSQoSMapPrecedenceMarkValue_Object = MibTableColumn
adGenAOSQoSMapPrecedenceMarkValue = _AdGenAOSQoSMapPrecedenceMarkValue_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 1, 2, 1, 14),
    _AdGenAOSQoSMapPrecedenceMarkValue_Type()
)
adGenAOSQoSMapPrecedenceMarkValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSQoSMapPrecedenceMarkValue.setStatus("current")


class _AdGenAOSQoSMapCosMarkState_Type(Integer32):
    """Custom type adGenAOSQoSMapCosMarkState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AdGenAOSQoSMapCosMarkState_Type.__name__ = "Integer32"
_AdGenAOSQoSMapCosMarkState_Object = MibTableColumn
adGenAOSQoSMapCosMarkState = _AdGenAOSQoSMapCosMarkState_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 1, 2, 1, 15),
    _AdGenAOSQoSMapCosMarkState_Type()
)
adGenAOSQoSMapCosMarkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSQoSMapCosMarkState.setStatus("current")
_AdGenAOSQoSMapCosMarkValue_Type = Unsigned32
_AdGenAOSQoSMapCosMarkValue_Object = MibTableColumn
adGenAOSQoSMapCosMarkValue = _AdGenAOSQoSMapCosMarkValue_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 1, 2, 1, 16),
    _AdGenAOSQoSMapCosMarkValue_Type()
)
adGenAOSQoSMapCosMarkValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSQoSMapCosMarkValue.setStatus("current")


class _AdGenAOSQoSMapShapeState_Type(Integer32):
    """Custom type adGenAOSQoSMapShapeState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AdGenAOSQoSMapShapeState_Type.__name__ = "Integer32"
_AdGenAOSQoSMapShapeState_Object = MibTableColumn
adGenAOSQoSMapShapeState = _AdGenAOSQoSMapShapeState_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 1, 2, 1, 17),
    _AdGenAOSQoSMapShapeState_Type()
)
adGenAOSQoSMapShapeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSQoSMapShapeState.setStatus("current")
_AdGenAOSQoSMapShapeValue_Type = Unsigned32
_AdGenAOSQoSMapShapeValue_Object = MibTableColumn
adGenAOSQoSMapShapeValue = _AdGenAOSQoSMapShapeValue_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 1, 2, 1, 18),
    _AdGenAOSQoSMapShapeValue_Type()
)
adGenAOSQoSMapShapeValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSQoSMapShapeValue.setStatus("current")
_AdGenAOSQoSMapShapeBurst_Type = Unsigned32
_AdGenAOSQoSMapShapeBurst_Object = MibTableColumn
adGenAOSQoSMapShapeBurst = _AdGenAOSQoSMapShapeBurst_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 1, 2, 1, 19),
    _AdGenAOSQoSMapShapeBurst_Type()
)
adGenAOSQoSMapShapeBurst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSQoSMapShapeBurst.setStatus("current")


class _AdGenAOSQoSMapShapeEthOverhead_Type(Integer32):
    """Custom type adGenAOSQoSMapShapeEthOverhead based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AdGenAOSQoSMapShapeEthOverhead_Type.__name__ = "Integer32"
_AdGenAOSQoSMapShapeEthOverhead_Object = MibTableColumn
adGenAOSQoSMapShapeEthOverhead = _AdGenAOSQoSMapShapeEthOverhead_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 1, 2, 1, 20),
    _AdGenAOSQoSMapShapeEthOverhead_Type()
)
adGenAOSQoSMapShapeEthOverhead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSQoSMapShapeEthOverhead.setStatus("current")


class _AdGenAOSQoSMapClearCounters_Type(Integer32):
    """Custom type adGenAOSQoSMapClearCounters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear", 1)
    )


_AdGenAOSQoSMapClearCounters_Type.__name__ = "Integer32"
_AdGenAOSQoSMapClearCounters_Object = MibTableColumn
adGenAOSQoSMapClearCounters = _AdGenAOSQoSMapClearCounters_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 1, 2, 1, 21),
    _AdGenAOSQoSMapClearCounters_Type()
)
adGenAOSQoSMapClearCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSQoSMapClearCounters.setStatus("current")


class _AdGenAOSQoSMapPriorityStrictRateLimiting_Type(Integer32):
    """Custom type adGenAOSQoSMapPriorityStrictRateLimiting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AdGenAOSQoSMapPriorityStrictRateLimiting_Type.__name__ = "Integer32"
_AdGenAOSQoSMapPriorityStrictRateLimiting_Object = MibTableColumn
adGenAOSQoSMapPriorityStrictRateLimiting = _AdGenAOSQoSMapPriorityStrictRateLimiting_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 1, 2, 1, 22),
    _AdGenAOSQoSMapPriorityStrictRateLimiting_Type()
)
adGenAOSQoSMapPriorityStrictRateLimiting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSQoSMapPriorityStrictRateLimiting.setStatus("current")
_AdGenAOSQoSInterfaceTable_Object = MibTable
adGenAOSQoSInterfaceTable = _AdGenAOSQoSInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 1, 3)
)
if mibBuilder.loadTexts:
    adGenAOSQoSInterfaceTable.setStatus("current")
_AdGenAOSQoSInterfaceEntry_Object = MibTableRow
adGenAOSQoSInterfaceEntry = _AdGenAOSQoSInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 1, 3, 1)
)
adGenAOSQoSInterfaceEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenAOSQoSInterfaceEntry.setStatus("current")
_AdGenAOSQoSInterfaceName_Type = DisplayString
_AdGenAOSQoSInterfaceName_Object = MibTableColumn
adGenAOSQoSInterfaceName = _AdGenAOSQoSInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 1, 3, 1, 1),
    _AdGenAOSQoSInterfaceName_Type()
)
adGenAOSQoSInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSQoSInterfaceName.setStatus("current")
_AdGenAOSQoSInterfaceOutboundMapSetName_Type = DisplayString
_AdGenAOSQoSInterfaceOutboundMapSetName_Object = MibTableColumn
adGenAOSQoSInterfaceOutboundMapSetName = _AdGenAOSQoSInterfaceOutboundMapSetName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 1, 3, 1, 2),
    _AdGenAOSQoSInterfaceOutboundMapSetName_Type()
)
adGenAOSQoSInterfaceOutboundMapSetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSQoSInterfaceOutboundMapSetName.setStatus("current")
_AdGenAOSQoSInterfaceInboundMapSetName_Type = DisplayString
_AdGenAOSQoSInterfaceInboundMapSetName_Object = MibTableColumn
adGenAOSQoSInterfaceInboundMapSetName = _AdGenAOSQoSInterfaceInboundMapSetName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 1, 3, 1, 3),
    _AdGenAOSQoSInterfaceInboundMapSetName_Type()
)
adGenAOSQoSInterfaceInboundMapSetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSQoSInterfaceInboundMapSetName.setStatus("current")


class _AdGenAOSQoSInterfaceMapState_Type(Integer32):
    """Custom type adGenAOSQoSInterfaceMapState based on Integer32"""
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


_AdGenAOSQoSInterfaceMapState_Type.__name__ = "Integer32"
_AdGenAOSQoSInterfaceMapState_Object = MibTableColumn
adGenAOSQoSInterfaceMapState = _AdGenAOSQoSInterfaceMapState_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 1, 3, 1, 4),
    _AdGenAOSQoSInterfaceMapState_Type()
)
adGenAOSQoSInterfaceMapState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSQoSInterfaceMapState.setStatus("current")


class _AdGenAOSQoSInterfaceTXQType_Type(Integer32):
    """Custom type adGenAOSQoSInterfaceTXQType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("fifo", 1),
          ("fifoAged", 2),
          ("none", 6),
          ("priority", 5),
          ("roundRobin", 4),
          ("weightedFair", 3))
    )


_AdGenAOSQoSInterfaceTXQType_Type.__name__ = "Integer32"
_AdGenAOSQoSInterfaceTXQType_Object = MibTableColumn
adGenAOSQoSInterfaceTXQType = _AdGenAOSQoSInterfaceTXQType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 1, 3, 1, 5),
    _AdGenAOSQoSInterfaceTXQType_Type()
)
adGenAOSQoSInterfaceTXQType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSQoSInterfaceTXQType.setStatus("current")
_AdGenAOSQoSInterfaceTXQSubqPktLimit_Type = Unsigned32
_AdGenAOSQoSInterfaceTXQSubqPktLimit_Object = MibTableColumn
adGenAOSQoSInterfaceTXQSubqPktLimit = _AdGenAOSQoSInterfaceTXQSubqPktLimit_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 1, 3, 1, 6),
    _AdGenAOSQoSInterfaceTXQSubqPktLimit_Type()
)
adGenAOSQoSInterfaceTXQSubqPktLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSQoSInterfaceTXQSubqPktLimit.setStatus("current")
_AdGenAOSQoSInterfaceTXQSize_Type = Unsigned32
_AdGenAOSQoSInterfaceTXQSize_Object = MibTableColumn
adGenAOSQoSInterfaceTXQSize = _AdGenAOSQoSInterfaceTXQSize_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 1, 3, 1, 7),
    _AdGenAOSQoSInterfaceTXQSize_Type()
)
adGenAOSQoSInterfaceTXQSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSQoSInterfaceTXQSize.setStatus("current")
_AdGenAOSQoSInterfaceTXQPktHighWater_Type = Unsigned32
_AdGenAOSQoSInterfaceTXQPktHighWater_Object = MibTableColumn
adGenAOSQoSInterfaceTXQPktHighWater = _AdGenAOSQoSInterfaceTXQPktHighWater_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 1, 3, 1, 8),
    _AdGenAOSQoSInterfaceTXQPktHighWater_Type()
)
adGenAOSQoSInterfaceTXQPktHighWater.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSQoSInterfaceTXQPktHighWater.setStatus("current")
_AdGenAOSQoSInterfaceTXQMaxTotal_Type = Unsigned32
_AdGenAOSQoSInterfaceTXQMaxTotal_Object = MibTableColumn
adGenAOSQoSInterfaceTXQMaxTotal = _AdGenAOSQoSInterfaceTXQMaxTotal_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 1, 3, 1, 9),
    _AdGenAOSQoSInterfaceTXQMaxTotal_Type()
)
adGenAOSQoSInterfaceTXQMaxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSQoSInterfaceTXQMaxTotal.setStatus("current")
_AdGenAOSQoSInterfaceTXQDrops_Type = Unsigned32
_AdGenAOSQoSInterfaceTXQDrops_Object = MibTableColumn
adGenAOSQoSInterfaceTXQDrops = _AdGenAOSQoSInterfaceTXQDrops_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 1, 3, 1, 10),
    _AdGenAOSQoSInterfaceTXQDrops_Type()
)
adGenAOSQoSInterfaceTXQDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSQoSInterfaceTXQDrops.setStatus("current")
_AdGenAOSQoSInterfaceTXQHdlcRingLimit_Type = Unsigned32
_AdGenAOSQoSInterfaceTXQHdlcRingLimit_Object = MibTableColumn
adGenAOSQoSInterfaceTXQHdlcRingLimit = _AdGenAOSQoSInterfaceTXQHdlcRingLimit_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 1, 3, 1, 11),
    _AdGenAOSQoSInterfaceTXQHdlcRingLimit_Type()
)
adGenAOSQoSInterfaceTXQHdlcRingLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSQoSInterfaceTXQHdlcRingLimit.setStatus("current")
_AdGenAOSQoSInterfaceTXQAvailableBW_Type = Unsigned32
_AdGenAOSQoSInterfaceTXQAvailableBW_Object = MibTableColumn
adGenAOSQoSInterfaceTXQAvailableBW = _AdGenAOSQoSInterfaceTXQAvailableBW_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 1, 3, 1, 12),
    _AdGenAOSQoSInterfaceTXQAvailableBW_Type()
)
adGenAOSQoSInterfaceTXQAvailableBW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSQoSInterfaceTXQAvailableBW.setStatus("current")
_AdGenAOSQoSInterfaceTXQConvActive_Type = Unsigned32
_AdGenAOSQoSInterfaceTXQConvActive_Object = MibTableColumn
adGenAOSQoSInterfaceTXQConvActive = _AdGenAOSQoSInterfaceTXQConvActive_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 1, 3, 1, 13),
    _AdGenAOSQoSInterfaceTXQConvActive_Type()
)
adGenAOSQoSInterfaceTXQConvActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSQoSInterfaceTXQConvActive.setStatus("current")
_AdGenAOSQoSInterfaceTXQConvMaxActive_Type = Unsigned32
_AdGenAOSQoSInterfaceTXQConvMaxActive_Object = MibTableColumn
adGenAOSQoSInterfaceTXQConvMaxActive = _AdGenAOSQoSInterfaceTXQConvMaxActive_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 1, 3, 1, 14),
    _AdGenAOSQoSInterfaceTXQConvMaxActive_Type()
)
adGenAOSQoSInterfaceTXQConvMaxActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSQoSInterfaceTXQConvMaxActive.setStatus("current")
_AdGenAOSQoSInterfaceTXQConvMaxTotal_Type = Unsigned32
_AdGenAOSQoSInterfaceTXQConvMaxTotal_Object = MibTableColumn
adGenAOSQoSInterfaceTXQConvMaxTotal = _AdGenAOSQoSInterfaceTXQConvMaxTotal_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 1, 3, 1, 15),
    _AdGenAOSQoSInterfaceTXQConvMaxTotal_Type()
)
adGenAOSQoSInterfaceTXQConvMaxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSQoSInterfaceTXQConvMaxTotal.setStatus("current")
_AdGenAOSQoSInterfaceTrafficShapingRate_Type = Unsigned32
_AdGenAOSQoSInterfaceTrafficShapingRate_Object = MibTableColumn
adGenAOSQoSInterfaceTrafficShapingRate = _AdGenAOSQoSInterfaceTrafficShapingRate_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 1, 3, 1, 16),
    _AdGenAOSQoSInterfaceTrafficShapingRate_Type()
)
adGenAOSQoSInterfaceTrafficShapingRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSQoSInterfaceTrafficShapingRate.setStatus("current")
_AdGenAOSQoSInterfaceTrafficShapingBurst_Type = Unsigned32
_AdGenAOSQoSInterfaceTrafficShapingBurst_Object = MibTableColumn
adGenAOSQoSInterfaceTrafficShapingBurst = _AdGenAOSQoSInterfaceTrafficShapingBurst_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 1, 3, 1, 17),
    _AdGenAOSQoSInterfaceTrafficShapingBurst_Type()
)
adGenAOSQoSInterfaceTrafficShapingBurst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSQoSInterfaceTrafficShapingBurst.setStatus("current")
_AdGenAOSQoSInterfaceShaperValue_Type = Unsigned32
_AdGenAOSQoSInterfaceShaperValue_Object = MibTableColumn
adGenAOSQoSInterfaceShaperValue = _AdGenAOSQoSInterfaceShaperValue_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 1, 3, 1, 18),
    _AdGenAOSQoSInterfaceShaperValue_Type()
)
adGenAOSQoSInterfaceShaperValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSQoSInterfaceShaperValue.setStatus("current")
_AdGenAOSQoSInterfaceShaperCurrentBudgetSize_Type = Unsigned32
_AdGenAOSQoSInterfaceShaperCurrentBudgetSize_Object = MibTableColumn
adGenAOSQoSInterfaceShaperCurrentBudgetSize = _AdGenAOSQoSInterfaceShaperCurrentBudgetSize_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 1, 3, 1, 19),
    _AdGenAOSQoSInterfaceShaperCurrentBudgetSize_Type()
)
adGenAOSQoSInterfaceShaperCurrentBudgetSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSQoSInterfaceShaperCurrentBudgetSize.setStatus("current")
_AdGenAOSQoSInterfaceShaperMaxBudgetSize_Type = Unsigned32
_AdGenAOSQoSInterfaceShaperMaxBudgetSize_Object = MibTableColumn
adGenAOSQoSInterfaceShaperMaxBudgetSize = _AdGenAOSQoSInterfaceShaperMaxBudgetSize_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 1, 3, 1, 20),
    _AdGenAOSQoSInterfaceShaperMaxBudgetSize_Type()
)
adGenAOSQoSInterfaceShaperMaxBudgetSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSQoSInterfaceShaperMaxBudgetSize.setStatus("current")
_AdGenAOSQoSInterfaceShaperBytesPerTick_Type = Unsigned32
_AdGenAOSQoSInterfaceShaperBytesPerTick_Object = MibTableColumn
adGenAOSQoSInterfaceShaperBytesPerTick = _AdGenAOSQoSInterfaceShaperBytesPerTick_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 1, 3, 1, 21),
    _AdGenAOSQoSInterfaceShaperBytesPerTick_Type()
)
adGenAOSQoSInterfaceShaperBytesPerTick.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSQoSInterfaceShaperBytesPerTick.setStatus("current")
_AdGenAOSQoSInterfaceShaperTickRate_Type = Unsigned32
_AdGenAOSQoSInterfaceShaperTickRate_Object = MibTableColumn
adGenAOSQoSInterfaceShaperTickRate = _AdGenAOSQoSInterfaceShaperTickRate_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 1, 3, 1, 22),
    _AdGenAOSQoSInterfaceShaperTickRate_Type()
)
adGenAOSQoSInterfaceShaperTickRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSQoSInterfaceShaperTickRate.setStatus("current")
_AdGenAOSQoSInterfaceShaperQPktDepth_Type = Unsigned32
_AdGenAOSQoSInterfaceShaperQPktDepth_Object = MibTableColumn
adGenAOSQoSInterfaceShaperQPktDepth = _AdGenAOSQoSInterfaceShaperQPktDepth_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 1, 3, 1, 23),
    _AdGenAOSQoSInterfaceShaperQPktDepth_Type()
)
adGenAOSQoSInterfaceShaperQPktDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSQoSInterfaceShaperQPktDepth.setStatus("current")
_AdGenAOSQoSInterfaceShaperQPktDrops_Type = Unsigned32
_AdGenAOSQoSInterfaceShaperQPktDrops_Object = MibTableColumn
adGenAOSQoSInterfaceShaperQPktDrops = _AdGenAOSQoSInterfaceShaperQPktDrops_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 1, 3, 1, 24),
    _AdGenAOSQoSInterfaceShaperQPktDrops_Type()
)
adGenAOSQoSInterfaceShaperQPktDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSQoSInterfaceShaperQPktDrops.setStatus("current")
_AdGenAOSQoSInterfaceShaperQPktSent_Type = Unsigned32
_AdGenAOSQoSInterfaceShaperQPktSent_Object = MibTableColumn
adGenAOSQoSInterfaceShaperQPktSent = _AdGenAOSQoSInterfaceShaperQPktSent_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 1, 3, 1, 25),
    _AdGenAOSQoSInterfaceShaperQPktSent_Type()
)
adGenAOSQoSInterfaceShaperQPktSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSQoSInterfaceShaperQPktSent.setStatus("current")
_AdGenAOSQoSInterfaceShaperQPktDelayed_Type = Unsigned32
_AdGenAOSQoSInterfaceShaperQPktDelayed_Object = MibTableColumn
adGenAOSQoSInterfaceShaperQPktDelayed = _AdGenAOSQoSInterfaceShaperQPktDelayed_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 1, 3, 1, 26),
    _AdGenAOSQoSInterfaceShaperQPktDelayed_Type()
)
adGenAOSQoSInterfaceShaperQPktDelayed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSQoSInterfaceShaperQPktDelayed.setStatus("current")
_AdGenAOSQoSClassConvHistoryTable_Object = MibTable
adGenAOSQoSClassConvHistoryTable = _AdGenAOSQoSClassConvHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 1, 4)
)
if mibBuilder.loadTexts:
    adGenAOSQoSClassConvHistoryTable.setStatus("current")
_AdGenAOSQoSClassConvHistoryEntry_Object = MibTableRow
adGenAOSQoSClassConvHistoryEntry = _AdGenAOSQoSClassConvHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 1, 4, 1)
)
adGenAOSQoSClassConvHistoryEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-AOS-QOS", "adGenAOSQoSMapEntryId"),
    (0, "ADTRAN-AOS-QOS", "adGenAOSQoSMapParentEntryId"),
)
if mibBuilder.loadTexts:
    adGenAOSQoSClassConvHistoryEntry.setStatus("current")
_AdGenAOSQoSMapParentEntryId_Type = Unsigned32
_AdGenAOSQoSMapParentEntryId_Object = MibTableColumn
adGenAOSQoSMapParentEntryId = _AdGenAOSQoSMapParentEntryId_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 1, 4, 1, 1),
    _AdGenAOSQoSMapParentEntryId_Type()
)
adGenAOSQoSMapParentEntryId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSQoSMapParentEntryId.setStatus("current")
_AdGenAOSQoSClassConvSetId_Type = Unsigned32
_AdGenAOSQoSClassConvSetId_Object = MibTableColumn
adGenAOSQoSClassConvSetId = _AdGenAOSQoSClassConvSetId_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 1, 4, 1, 2),
    _AdGenAOSQoSClassConvSetId_Type()
)
adGenAOSQoSClassConvSetId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSQoSClassConvSetId.setStatus("current")
_AdGenAOSQoSHistoryClassConvId_Type = Unsigned32
_AdGenAOSQoSHistoryClassConvId_Object = MibTableColumn
adGenAOSQoSHistoryClassConvId = _AdGenAOSQoSHistoryClassConvId_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 1, 4, 1, 3),
    _AdGenAOSQoSHistoryClassConvId_Type()
)
adGenAOSQoSHistoryClassConvId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSQoSHistoryClassConvId.setStatus("current")
_AdGenAOSQoSClassConvHistoryMatches_Type = Counter32
_AdGenAOSQoSClassConvHistoryMatches_Object = MibTableColumn
adGenAOSQoSClassConvHistoryMatches = _AdGenAOSQoSClassConvHistoryMatches_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 1, 4, 1, 4),
    _AdGenAOSQoSClassConvHistoryMatches_Type()
)
adGenAOSQoSClassConvHistoryMatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSQoSClassConvHistoryMatches.setStatus("current")
_AdGenAOSQoSClassConvHistoryDiscards_Type = Counter32
_AdGenAOSQoSClassConvHistoryDiscards_Object = MibTableColumn
adGenAOSQoSClassConvHistoryDiscards = _AdGenAOSQoSClassConvHistoryDiscards_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 1, 4, 1, 5),
    _AdGenAOSQoSClassConvHistoryDiscards_Type()
)
adGenAOSQoSClassConvHistoryDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSQoSClassConvHistoryDiscards.setStatus("current")
_AdGenAOSQoSClassConvHistoryMatchesBytes_Type = Counter64
_AdGenAOSQoSClassConvHistoryMatchesBytes_Object = MibTableColumn
adGenAOSQoSClassConvHistoryMatchesBytes = _AdGenAOSQoSClassConvHistoryMatchesBytes_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 1, 4, 1, 6),
    _AdGenAOSQoSClassConvHistoryMatchesBytes_Type()
)
adGenAOSQoSClassConvHistoryMatchesBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSQoSClassConvHistoryMatchesBytes.setStatus("current")
_AdGenAOSQoSClassConvHistoryDiscardsBytes_Type = Counter64
_AdGenAOSQoSClassConvHistoryDiscardsBytes_Object = MibTableColumn
adGenAOSQoSClassConvHistoryDiscardsBytes = _AdGenAOSQoSClassConvHistoryDiscardsBytes_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 1, 4, 1, 7),
    _AdGenAOSQoSClassConvHistoryDiscardsBytes_Type()
)
adGenAOSQoSClassConvHistoryDiscardsBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSQoSClassConvHistoryDiscardsBytes.setStatus("current")
_AdGenAOSQoSClassConvHistoryDepth_Type = Unsigned32
_AdGenAOSQoSClassConvHistoryDepth_Object = MibTableColumn
adGenAOSQoSClassConvHistoryDepth = _AdGenAOSQoSClassConvHistoryDepth_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 1, 4, 1, 8),
    _AdGenAOSQoSClassConvHistoryDepth_Type()
)
adGenAOSQoSClassConvHistoryDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSQoSClassConvHistoryDepth.setStatus("current")
_AdGenAOSQoSClassConvHistoryHighWater_Type = Unsigned32
_AdGenAOSQoSClassConvHistoryHighWater_Object = MibTableColumn
adGenAOSQoSClassConvHistoryHighWater = _AdGenAOSQoSClassConvHistoryHighWater_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 1, 4, 1, 9),
    _AdGenAOSQoSClassConvHistoryHighWater_Type()
)
adGenAOSQoSClassConvHistoryHighWater.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSQoSClassConvHistoryHighWater.setStatus("current")
_AdGenAOSQoSClassConvHistoryByteMatchRate_Type = Unsigned32
_AdGenAOSQoSClassConvHistoryByteMatchRate_Object = MibTableColumn
adGenAOSQoSClassConvHistoryByteMatchRate = _AdGenAOSQoSClassConvHistoryByteMatchRate_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 1, 4, 1, 10),
    _AdGenAOSQoSClassConvHistoryByteMatchRate_Type()
)
adGenAOSQoSClassConvHistoryByteMatchRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSQoSClassConvHistoryByteMatchRate.setStatus("current")
_AdGenAOSQoSClassConvHistoryByteDiscardRate_Type = Unsigned32
_AdGenAOSQoSClassConvHistoryByteDiscardRate_Object = MibTableColumn
adGenAOSQoSClassConvHistoryByteDiscardRate = _AdGenAOSQoSClassConvHistoryByteDiscardRate_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 1, 4, 1, 11),
    _AdGenAOSQoSClassConvHistoryByteDiscardRate_Type()
)
adGenAOSQoSClassConvHistoryByteDiscardRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSQoSClassConvHistoryByteDiscardRate.setStatus("current")
_AdGenAOSQoSClassConvHistoryBitMatchRate_Type = Unsigned64
_AdGenAOSQoSClassConvHistoryBitMatchRate_Object = MibTableColumn
adGenAOSQoSClassConvHistoryBitMatchRate = _AdGenAOSQoSClassConvHistoryBitMatchRate_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 1, 4, 1, 12),
    _AdGenAOSQoSClassConvHistoryBitMatchRate_Type()
)
adGenAOSQoSClassConvHistoryBitMatchRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSQoSClassConvHistoryBitMatchRate.setStatus("current")
_AdGenAOSQoSClassConvHistoryBitDiscardRate_Type = Unsigned64
_AdGenAOSQoSClassConvHistoryBitDiscardRate_Object = MibTableColumn
adGenAOSQoSClassConvHistoryBitDiscardRate = _AdGenAOSQoSClassConvHistoryBitDiscardRate_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 1, 4, 1, 13),
    _AdGenAOSQoSClassConvHistoryBitDiscardRate_Type()
)
adGenAOSQoSClassConvHistoryBitDiscardRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSQoSClassConvHistoryBitDiscardRate.setStatus("current")
_AdGenAOSQoSConversationTable_Object = MibTable
adGenAOSQoSConversationTable = _AdGenAOSQoSConversationTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 1, 5)
)
if mibBuilder.loadTexts:
    adGenAOSQoSConversationTable.setStatus("current")
_AdGenAOSQoSConversationEntry_Object = MibTableRow
adGenAOSQoSConversationEntry = _AdGenAOSQoSConversationEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 1, 5, 1)
)
adGenAOSQoSConversationEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-AOS-QOS", "adGenAOSQoSConvId"),
    (0, "ADTRAN-AOS-QOS", "adGenAOSQoSMapConvParentEntryId"),
)
if mibBuilder.loadTexts:
    adGenAOSQoSConversationEntry.setStatus("current")
_AdGenAOSQoSConvId_Type = Unsigned32
_AdGenAOSQoSConvId_Object = MibTableColumn
adGenAOSQoSConvId = _AdGenAOSQoSConvId_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 1, 5, 1, 1),
    _AdGenAOSQoSConvId_Type()
)
adGenAOSQoSConvId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSQoSConvId.setStatus("current")
_AdGenAOSQoSMapConvParentEntryId_Type = Unsigned32
_AdGenAOSQoSMapConvParentEntryId_Object = MibTableColumn
adGenAOSQoSMapConvParentEntryId = _AdGenAOSQoSMapConvParentEntryId_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 1, 5, 1, 2),
    _AdGenAOSQoSMapConvParentEntryId_Type()
)
adGenAOSQoSMapConvParentEntryId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSQoSMapConvParentEntryId.setStatus("current")
_AdGenAOSQoSConvMatches_Type = Counter32
_AdGenAOSQoSConvMatches_Object = MibTableColumn
adGenAOSQoSConvMatches = _AdGenAOSQoSConvMatches_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 1, 5, 1, 3),
    _AdGenAOSQoSConvMatches_Type()
)
adGenAOSQoSConvMatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSQoSConvMatches.setStatus("current")
_AdGenAOSQoSConvDiscards_Type = Counter32
_AdGenAOSQoSConvDiscards_Object = MibTableColumn
adGenAOSQoSConvDiscards = _AdGenAOSQoSConvDiscards_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 1, 5, 1, 4),
    _AdGenAOSQoSConvDiscards_Type()
)
adGenAOSQoSConvDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSQoSConvDiscards.setStatus("current")
_AdGenAOSQoSConvMatchesBytes_Type = Counter64
_AdGenAOSQoSConvMatchesBytes_Object = MibTableColumn
adGenAOSQoSConvMatchesBytes = _AdGenAOSQoSConvMatchesBytes_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 1, 5, 1, 5),
    _AdGenAOSQoSConvMatchesBytes_Type()
)
adGenAOSQoSConvMatchesBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSQoSConvMatchesBytes.setStatus("current")
_AdGenAOSQoSConvDiscardsBytes_Type = Counter64
_AdGenAOSQoSConvDiscardsBytes_Object = MibTableColumn
adGenAOSQoSConvDiscardsBytes = _AdGenAOSQoSConvDiscardsBytes_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 1, 5, 1, 6),
    _AdGenAOSQoSConvDiscardsBytes_Type()
)
adGenAOSQoSConvDiscardsBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSQoSConvDiscardsBytes.setStatus("current")
_AdGenAOSQoSConvDepth_Type = Unsigned32
_AdGenAOSQoSConvDepth_Object = MibTableColumn
adGenAOSQoSConvDepth = _AdGenAOSQoSConvDepth_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 1, 5, 1, 7),
    _AdGenAOSQoSConvDepth_Type()
)
adGenAOSQoSConvDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSQoSConvDepth.setStatus("current")
_AdGenAOSQoSConvHighWater_Type = Unsigned32
_AdGenAOSQoSConvHighWater_Object = MibTableColumn
adGenAOSQoSConvHighWater = _AdGenAOSQoSConvHighWater_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 1, 5, 1, 8),
    _AdGenAOSQoSConvHighWater_Type()
)
adGenAOSQoSConvHighWater.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSQoSConvHighWater.setStatus("current")
_AdGenAOSQoSConvWeight_Type = Unsigned32
_AdGenAOSQoSConvWeight_Object = MibTableColumn
adGenAOSQoSConvWeight = _AdGenAOSQoSConvWeight_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 1, 5, 1, 9),
    _AdGenAOSQoSConvWeight_Type()
)
adGenAOSQoSConvWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSQoSConvWeight.setStatus("current")
_AdGenAOSQoSConvPktLen_Type = Unsigned32
_AdGenAOSQoSConvPktLen_Object = MibTableColumn
adGenAOSQoSConvPktLen = _AdGenAOSQoSConvPktLen_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 1, 5, 1, 10),
    _AdGenAOSQoSConvPktLen_Type()
)
adGenAOSQoSConvPktLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSQoSConvPktLen.setStatus("current")


class _AdGenAOSQoSConvProttype_Type(Integer32):
    """Custom type adGenAOSQoSConvProttype based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bridging", 3),
          ("ip", 2),
          ("unset", 1))
    )


_AdGenAOSQoSConvProttype_Type.__name__ = "Integer32"
_AdGenAOSQoSConvProttype_Object = MibTableColumn
adGenAOSQoSConvProttype = _AdGenAOSQoSConvProttype_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 1, 5, 1, 11),
    _AdGenAOSQoSConvProttype_Type()
)
adGenAOSQoSConvProttype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSQoSConvProttype.setStatus("current")


class _AdGenAOSQoSConvSubQType_Type(Integer32):
    """Custom type adGenAOSQoSConvSubQType based on Integer32"""
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
        *(("bestEffort", 1),
          ("classBased", 2),
          ("prioritySystem", 5),
          ("priorityUser", 4),
          ("unclassified", 3))
    )


_AdGenAOSQoSConvSubQType_Type.__name__ = "Integer32"
_AdGenAOSQoSConvSubQType_Object = MibTableColumn
adGenAOSQoSConvSubQType = _AdGenAOSQoSConvSubQType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 1, 5, 1, 12),
    _AdGenAOSQoSConvSubQType_Type()
)
adGenAOSQoSConvSubQType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSQoSConvSubQType.setStatus("current")


class _AdGenAOSQoSConvPktHeader_Type(OctetString):
    """Custom type adGenAOSQoSConvPktHeader based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_AdGenAOSQoSConvPktHeader_Type.__name__ = "OctetString"
_AdGenAOSQoSConvPktHeader_Object = MibTableColumn
adGenAOSQoSConvPktHeader = _AdGenAOSQoSConvPktHeader_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 1, 5, 1, 13),
    _AdGenAOSQoSConvPktHeader_Type()
)
adGenAOSQoSConvPktHeader.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSQoSConvPktHeader.setStatus("current")
_AdGenAOSQoSPriorityRateLimiterTable_Object = MibTable
adGenAOSQoSPriorityRateLimiterTable = _AdGenAOSQoSPriorityRateLimiterTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 1, 6)
)
if mibBuilder.loadTexts:
    adGenAOSQoSPriorityRateLimiterTable.setStatus("current")
_AdGenAOSQoSPriorityRateLimiterEntry_Object = MibTableRow
adGenAOSQoSPriorityRateLimiterEntry = _AdGenAOSQoSPriorityRateLimiterEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 1, 6, 1)
)
adGenAOSQoSPriorityRateLimiterEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-AOS-QOS", "adGenAOSQoSMapEntryId"),
    (0, "ADTRAN-AOS-QOS", "adGenAOSQoSPriorityRateLimiterParentEntryId"),
)
if mibBuilder.loadTexts:
    adGenAOSQoSPriorityRateLimiterEntry.setStatus("current")
_AdGenAOSQoSPriorityRateLimiterParentEntryId_Type = Unsigned32
_AdGenAOSQoSPriorityRateLimiterParentEntryId_Object = MibTableColumn
adGenAOSQoSPriorityRateLimiterParentEntryId = _AdGenAOSQoSPriorityRateLimiterParentEntryId_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 1, 6, 1, 1),
    _AdGenAOSQoSPriorityRateLimiterParentEntryId_Type()
)
adGenAOSQoSPriorityRateLimiterParentEntryId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSQoSPriorityRateLimiterParentEntryId.setStatus("current")
_AdGenAOSQoSPriorityRateLimiterSetId_Type = Unsigned32
_AdGenAOSQoSPriorityRateLimiterSetId_Object = MibTableColumn
adGenAOSQoSPriorityRateLimiterSetId = _AdGenAOSQoSPriorityRateLimiterSetId_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 1, 6, 1, 2),
    _AdGenAOSQoSPriorityRateLimiterSetId_Type()
)
adGenAOSQoSPriorityRateLimiterSetId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSQoSPriorityRateLimiterSetId.setStatus("current")
_AdGenAOSQoSPriorityRateLimiterCurrBudget_Type = Unsigned32
_AdGenAOSQoSPriorityRateLimiterCurrBudget_Object = MibTableColumn
adGenAOSQoSPriorityRateLimiterCurrBudget = _AdGenAOSQoSPriorityRateLimiterCurrBudget_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 1, 6, 1, 3),
    _AdGenAOSQoSPriorityRateLimiterCurrBudget_Type()
)
adGenAOSQoSPriorityRateLimiterCurrBudget.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSQoSPriorityRateLimiterCurrBudget.setStatus("current")
_AdGenAOSQoSPriorityRateLimiterMaxBudget_Type = Unsigned32
_AdGenAOSQoSPriorityRateLimiterMaxBudget_Object = MibTableColumn
adGenAOSQoSPriorityRateLimiterMaxBudget = _AdGenAOSQoSPriorityRateLimiterMaxBudget_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 1, 6, 1, 4),
    _AdGenAOSQoSPriorityRateLimiterMaxBudget_Type()
)
adGenAOSQoSPriorityRateLimiterMaxBudget.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSQoSPriorityRateLimiterMaxBudget.setStatus("current")
_AdGenAOSQoSPriorityRateLimiterUpdateTimestamp_Type = Unsigned32
_AdGenAOSQoSPriorityRateLimiterUpdateTimestamp_Object = MibTableColumn
adGenAOSQoSPriorityRateLimiterUpdateTimestamp = _AdGenAOSQoSPriorityRateLimiterUpdateTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 1, 6, 1, 5),
    _AdGenAOSQoSPriorityRateLimiterUpdateTimestamp_Type()
)
adGenAOSQoSPriorityRateLimiterUpdateTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSQoSPriorityRateLimiterUpdateTimestamp.setStatus("current")
_AdGenAOSQoSPriorityRateLimiterBudgetRate_Type = Unsigned32
_AdGenAOSQoSPriorityRateLimiterBudgetRate_Object = MibTableColumn
adGenAOSQoSPriorityRateLimiterBudgetRate = _AdGenAOSQoSPriorityRateLimiterBudgetRate_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 1, 6, 1, 6),
    _AdGenAOSQoSPriorityRateLimiterBudgetRate_Type()
)
adGenAOSQoSPriorityRateLimiterBudgetRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSQoSPriorityRateLimiterBudgetRate.setStatus("current")
_AdGenAOSQoSPriorityRateLimiterMaxFillTime_Type = Unsigned32
_AdGenAOSQoSPriorityRateLimiterMaxFillTime_Object = MibTableColumn
adGenAOSQoSPriorityRateLimiterMaxFillTime = _AdGenAOSQoSPriorityRateLimiterMaxFillTime_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 1, 6, 1, 7),
    _AdGenAOSQoSPriorityRateLimiterMaxFillTime_Type()
)
adGenAOSQoSPriorityRateLimiterMaxFillTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSQoSPriorityRateLimiterMaxFillTime.setStatus("current")
_AdGenAOSQoSPriorityRateLimiterMatches_Type = Counter32
_AdGenAOSQoSPriorityRateLimiterMatches_Object = MibTableColumn
adGenAOSQoSPriorityRateLimiterMatches = _AdGenAOSQoSPriorityRateLimiterMatches_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 1, 6, 1, 8),
    _AdGenAOSQoSPriorityRateLimiterMatches_Type()
)
adGenAOSQoSPriorityRateLimiterMatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSQoSPriorityRateLimiterMatches.setStatus("current")
_AdGenAOSQoSPriorityRateLimiterDrops_Type = Counter32
_AdGenAOSQoSPriorityRateLimiterDrops_Object = MibTableColumn
adGenAOSQoSPriorityRateLimiterDrops = _AdGenAOSQoSPriorityRateLimiterDrops_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 1, 6, 1, 9),
    _AdGenAOSQoSPriorityRateLimiterDrops_Type()
)
adGenAOSQoSPriorityRateLimiterDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSQoSPriorityRateLimiterDrops.setStatus("current")
_AdGenAOSQoSPriorityRateLimiterMatchesBytes_Type = Counter64
_AdGenAOSQoSPriorityRateLimiterMatchesBytes_Object = MibTableColumn
adGenAOSQoSPriorityRateLimiterMatchesBytes = _AdGenAOSQoSPriorityRateLimiterMatchesBytes_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 1, 6, 1, 10),
    _AdGenAOSQoSPriorityRateLimiterMatchesBytes_Type()
)
adGenAOSQoSPriorityRateLimiterMatchesBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSQoSPriorityRateLimiterMatchesBytes.setStatus("current")
_AdGenAOSQoSPriorityRateLimiterDropsBytes_Type = Counter64
_AdGenAOSQoSPriorityRateLimiterDropsBytes_Object = MibTableColumn
adGenAOSQoSPriorityRateLimiterDropsBytes = _AdGenAOSQoSPriorityRateLimiterDropsBytes_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 1, 6, 1, 11),
    _AdGenAOSQoSPriorityRateLimiterDropsBytes_Type()
)
adGenAOSQoSPriorityRateLimiterDropsBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSQoSPriorityRateLimiterDropsBytes.setStatus("current")


class _AdGenAOSQoSPriorityRateLimiterClearCounters_Type(Integer32):
    """Custom type adGenAOSQoSPriorityRateLimiterClearCounters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear", 1)
    )


_AdGenAOSQoSPriorityRateLimiterClearCounters_Type.__name__ = "Integer32"
_AdGenAOSQoSPriorityRateLimiterClearCounters_Object = MibTableColumn
adGenAOSQoSPriorityRateLimiterClearCounters = _AdGenAOSQoSPriorityRateLimiterClearCounters_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 1, 6, 1, 12),
    _AdGenAOSQoSPriorityRateLimiterClearCounters_Type()
)
adGenAOSQoSPriorityRateLimiterClearCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSQoSPriorityRateLimiterClearCounters.setStatus("current")
_AdGenAOSQoSPriorityRateLimiterByteMatchRate_Type = Unsigned32
_AdGenAOSQoSPriorityRateLimiterByteMatchRate_Object = MibTableColumn
adGenAOSQoSPriorityRateLimiterByteMatchRate = _AdGenAOSQoSPriorityRateLimiterByteMatchRate_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 1, 6, 1, 13),
    _AdGenAOSQoSPriorityRateLimiterByteMatchRate_Type()
)
adGenAOSQoSPriorityRateLimiterByteMatchRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSQoSPriorityRateLimiterByteMatchRate.setStatus("current")
_AdGenAOSQoSPriorityRateLimiterByteDiscardRate_Type = Unsigned32
_AdGenAOSQoSPriorityRateLimiterByteDiscardRate_Object = MibTableColumn
adGenAOSQoSPriorityRateLimiterByteDiscardRate = _AdGenAOSQoSPriorityRateLimiterByteDiscardRate_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 1, 6, 1, 14),
    _AdGenAOSQoSPriorityRateLimiterByteDiscardRate_Type()
)
adGenAOSQoSPriorityRateLimiterByteDiscardRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSQoSPriorityRateLimiterByteDiscardRate.setStatus("current")
_AdGenAOSQoSPriorityRateLimiterBitMatchRate_Type = Unsigned64
_AdGenAOSQoSPriorityRateLimiterBitMatchRate_Object = MibTableColumn
adGenAOSQoSPriorityRateLimiterBitMatchRate = _AdGenAOSQoSPriorityRateLimiterBitMatchRate_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 1, 6, 1, 15),
    _AdGenAOSQoSPriorityRateLimiterBitMatchRate_Type()
)
adGenAOSQoSPriorityRateLimiterBitMatchRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSQoSPriorityRateLimiterBitMatchRate.setStatus("current")
_AdGenAOSQoSPriorityRateLimiterBitDiscardRate_Type = Unsigned64
_AdGenAOSQoSPriorityRateLimiterBitDiscardRate_Object = MibTableColumn
adGenAOSQoSPriorityRateLimiterBitDiscardRate = _AdGenAOSQoSPriorityRateLimiterBitDiscardRate_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 1, 6, 1, 16),
    _AdGenAOSQoSPriorityRateLimiterBitDiscardRate_Type()
)
adGenAOSQoSPriorityRateLimiterBitDiscardRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSQoSPriorityRateLimiterBitDiscardRate.setStatus("current")
_AdGenAOSQoSMapClassifierStatsTable_Object = MibTable
adGenAOSQoSMapClassifierStatsTable = _AdGenAOSQoSMapClassifierStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 1, 7)
)
if mibBuilder.loadTexts:
    adGenAOSQoSMapClassifierStatsTable.setStatus("current")
_AdGenAOSQoSMapClassifierStatsEntry_Object = MibTableRow
adGenAOSQoSMapClassifierStatsEntry = _AdGenAOSQoSMapClassifierStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 1, 7, 1)
)
adGenAOSQoSMapClassifierStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-AOS-QOS", "adGenAOSQoSMapEntryId"),
    (0, "ADTRAN-AOS-QOS", "adGenAOSQoSMapClassifierParentEntryId"),
)
if mibBuilder.loadTexts:
    adGenAOSQoSMapClassifierStatsEntry.setStatus("current")
_AdGenAOSQoSMapClassifierParentEntryId_Type = Unsigned32
_AdGenAOSQoSMapClassifierParentEntryId_Object = MibTableColumn
adGenAOSQoSMapClassifierParentEntryId = _AdGenAOSQoSMapClassifierParentEntryId_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 1, 7, 1, 1),
    _AdGenAOSQoSMapClassifierParentEntryId_Type()
)
adGenAOSQoSMapClassifierParentEntryId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSQoSMapClassifierParentEntryId.setStatus("current")
_AdGenAOSQoSClassifierMatches_Type = Counter32
_AdGenAOSQoSClassifierMatches_Object = MibTableColumn
adGenAOSQoSClassifierMatches = _AdGenAOSQoSClassifierMatches_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 1, 7, 1, 2),
    _AdGenAOSQoSClassifierMatches_Type()
)
adGenAOSQoSClassifierMatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSQoSClassifierMatches.setStatus("current")
_AdGenAOSQoSClassifierDrops_Type = Counter32
_AdGenAOSQoSClassifierDrops_Object = MibTableColumn
adGenAOSQoSClassifierDrops = _AdGenAOSQoSClassifierDrops_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 1, 7, 1, 3),
    _AdGenAOSQoSClassifierDrops_Type()
)
adGenAOSQoSClassifierDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSQoSClassifierDrops.setStatus("current")
_AdGenAOSQoSClassifierMatchBytes_Type = Counter64
_AdGenAOSQoSClassifierMatchBytes_Object = MibTableColumn
adGenAOSQoSClassifierMatchBytes = _AdGenAOSQoSClassifierMatchBytes_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 1, 7, 1, 4),
    _AdGenAOSQoSClassifierMatchBytes_Type()
)
adGenAOSQoSClassifierMatchBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSQoSClassifierMatchBytes.setStatus("current")
_AdGenAOSQoSClassifierDropBytes_Type = Counter64
_AdGenAOSQoSClassifierDropBytes_Object = MibTableColumn
adGenAOSQoSClassifierDropBytes = _AdGenAOSQoSClassifierDropBytes_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 1, 7, 1, 5),
    _AdGenAOSQoSClassifierDropBytes_Type()
)
adGenAOSQoSClassifierDropBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSQoSClassifierDropBytes.setStatus("current")
_AdGenAOSQoSClassifierPktMatchRate_Type = Unsigned32
_AdGenAOSQoSClassifierPktMatchRate_Object = MibTableColumn
adGenAOSQoSClassifierPktMatchRate = _AdGenAOSQoSClassifierPktMatchRate_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 1, 7, 1, 6),
    _AdGenAOSQoSClassifierPktMatchRate_Type()
)
adGenAOSQoSClassifierPktMatchRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSQoSClassifierPktMatchRate.setStatus("current")
_AdGenAOSQoSClassifierPktDropRate_Type = Unsigned32
_AdGenAOSQoSClassifierPktDropRate_Object = MibTableColumn
adGenAOSQoSClassifierPktDropRate = _AdGenAOSQoSClassifierPktDropRate_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 1, 7, 1, 7),
    _AdGenAOSQoSClassifierPktDropRate_Type()
)
adGenAOSQoSClassifierPktDropRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSQoSClassifierPktDropRate.setStatus("current")
_AdGenAOSQoSClassifierByteMatchRate_Type = Unsigned32
_AdGenAOSQoSClassifierByteMatchRate_Object = MibTableColumn
adGenAOSQoSClassifierByteMatchRate = _AdGenAOSQoSClassifierByteMatchRate_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 1, 7, 1, 8),
    _AdGenAOSQoSClassifierByteMatchRate_Type()
)
adGenAOSQoSClassifierByteMatchRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSQoSClassifierByteMatchRate.setStatus("current")
_AdGenAOSQoSClassifierByteDropRate_Type = Unsigned32
_AdGenAOSQoSClassifierByteDropRate_Object = MibTableColumn
adGenAOSQoSClassifierByteDropRate = _AdGenAOSQoSClassifierByteDropRate_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 1, 7, 1, 9),
    _AdGenAOSQoSClassifierByteDropRate_Type()
)
adGenAOSQoSClassifierByteDropRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSQoSClassifierByteDropRate.setStatus("current")
_AdGenAOSQoSClassifierBitMatchRate_Type = Unsigned64
_AdGenAOSQoSClassifierBitMatchRate_Object = MibTableColumn
adGenAOSQoSClassifierBitMatchRate = _AdGenAOSQoSClassifierBitMatchRate_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 1, 7, 1, 10),
    _AdGenAOSQoSClassifierBitMatchRate_Type()
)
adGenAOSQoSClassifierBitMatchRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSQoSClassifierBitMatchRate.setStatus("current")
_AdGenAOSQoSClassifierBitDropRate_Type = Unsigned64
_AdGenAOSQoSClassifierBitDropRate_Object = MibTableColumn
adGenAOSQoSClassifierBitDropRate = _AdGenAOSQoSClassifierBitDropRate_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 1, 7, 1, 11),
    _AdGenAOSQoSClassifierBitDropRate_Type()
)
adGenAOSQoSClassifierBitDropRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSQoSClassifierBitDropRate.setStatus("current")
_AdGenAOSQoSMapMatchTable_Object = MibTable
adGenAOSQoSMapMatchTable = _AdGenAOSQoSMapMatchTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 1, 8)
)
if mibBuilder.loadTexts:
    adGenAOSQoSMapMatchTable.setStatus("current")
_AdGenAOSQoSMapMatchEntry_Object = MibTableRow
adGenAOSQoSMapMatchEntry = _AdGenAOSQoSMapMatchEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 1, 8, 1)
)
adGenAOSQoSMapMatchEntry.setIndexNames(
    (0, "ADTRAN-AOS-QOS", "adGenAOSQoSMapSetId"),
    (0, "ADTRAN-AOS-QOS", "adGenAOSQoSMapEntryId"),
    (0, "ADTRAN-AOS-QOS", "adGenAOSQoSMapMatchEntryId"),
)
if mibBuilder.loadTexts:
    adGenAOSQoSMapMatchEntry.setStatus("current")
_AdGenAOSQoSMapMatchEntryId_Type = Unsigned32
_AdGenAOSQoSMapMatchEntryId_Object = MibTableColumn
adGenAOSQoSMapMatchEntryId = _AdGenAOSQoSMapMatchEntryId_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 1, 8, 1, 1),
    _AdGenAOSQoSMapMatchEntryId_Type()
)
adGenAOSQoSMapMatchEntryId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSQoSMapMatchEntryId.setStatus("current")


class _AdGenAOSQoSMapMatchType_Type(Integer32):
    """Custom type adGenAOSQoSMapMatchType based on Integer32"""
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
              10,
              11,
              12,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("acl", 2),
          ("aclIpv6", 15),
          ("any", 10),
          ("dscp", 5),
          ("dscpIpv4", 11),
          ("dscpIpv6", 12),
          ("frameRelayDLCI", 8),
          ("ipRTP", 3),
          ("ipRTPIpv6", 16),
          ("precedence", 6),
          ("precedenceIpv4", 13),
          ("precedenceIpv6", 14),
          ("protocol", 4),
          ("unknown", 1),
          ("vlan", 7))
    )


_AdGenAOSQoSMapMatchType_Type.__name__ = "Integer32"
_AdGenAOSQoSMapMatchType_Object = MibTableColumn
adGenAOSQoSMapMatchType = _AdGenAOSQoSMapMatchType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 1, 8, 1, 2),
    _AdGenAOSQoSMapMatchType_Type()
)
adGenAOSQoSMapMatchType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSQoSMapMatchType.setStatus("current")
_AdGenAOSQoSMapMatchACL_Type = DisplayString
_AdGenAOSQoSMapMatchACL_Object = MibTableColumn
adGenAOSQoSMapMatchACL = _AdGenAOSQoSMapMatchACL_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 1, 8, 1, 3),
    _AdGenAOSQoSMapMatchACL_Type()
)
adGenAOSQoSMapMatchACL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSQoSMapMatchACL.setStatus("current")


class _AdGenAOSQoSMapRTPMatchStartPort_Type(Unsigned32):
    """Custom type adGenAOSQoSMapRTPMatchStartPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AdGenAOSQoSMapRTPMatchStartPort_Type.__name__ = "Unsigned32"
_AdGenAOSQoSMapRTPMatchStartPort_Object = MibTableColumn
adGenAOSQoSMapRTPMatchStartPort = _AdGenAOSQoSMapRTPMatchStartPort_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 1, 8, 1, 4),
    _AdGenAOSQoSMapRTPMatchStartPort_Type()
)
adGenAOSQoSMapRTPMatchStartPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSQoSMapRTPMatchStartPort.setStatus("current")


class _AdGenAOSQoSMapRTPMatchEndPort_Type(Unsigned32):
    """Custom type adGenAOSQoSMapRTPMatchEndPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AdGenAOSQoSMapRTPMatchEndPort_Type.__name__ = "Unsigned32"
_AdGenAOSQoSMapRTPMatchEndPort_Object = MibTableColumn
adGenAOSQoSMapRTPMatchEndPort = _AdGenAOSQoSMapRTPMatchEndPort_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 1, 8, 1, 5),
    _AdGenAOSQoSMapRTPMatchEndPort_Type()
)
adGenAOSQoSMapRTPMatchEndPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSQoSMapRTPMatchEndPort.setStatus("current")


class _AdGenAOSQoSMapRTPMatchPorts_Type(Integer32):
    """Custom type adGenAOSQoSMapRTPMatchPorts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("all", 3),
          ("even", 1),
          ("odd", 2))
    )


_AdGenAOSQoSMapRTPMatchPorts_Type.__name__ = "Integer32"
_AdGenAOSQoSMapRTPMatchPorts_Object = MibTableColumn
adGenAOSQoSMapRTPMatchPorts = _AdGenAOSQoSMapRTPMatchPorts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 1, 8, 1, 6),
    _AdGenAOSQoSMapRTPMatchPorts_Type()
)
adGenAOSQoSMapRTPMatchPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSQoSMapRTPMatchPorts.setStatus("current")
_AdGenAOSQoSMapDscpMatchValue_Type = DisplayString
_AdGenAOSQoSMapDscpMatchValue_Object = MibTableColumn
adGenAOSQoSMapDscpMatchValue = _AdGenAOSQoSMapDscpMatchValue_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 1, 8, 1, 7),
    _AdGenAOSQoSMapDscpMatchValue_Type()
)
adGenAOSQoSMapDscpMatchValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSQoSMapDscpMatchValue.setStatus("current")
_AdGenAOSQoSMapPrecedenceMatchValue_Type = Unsigned32
_AdGenAOSQoSMapPrecedenceMatchValue_Object = MibTableColumn
adGenAOSQoSMapPrecedenceMatchValue = _AdGenAOSQoSMapPrecedenceMatchValue_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 1, 8, 1, 8),
    _AdGenAOSQoSMapPrecedenceMatchValue_Type()
)
adGenAOSQoSMapPrecedenceMatchValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSQoSMapPrecedenceMatchValue.setStatus("current")


class _AdGenAOSQoSMapProtocolMatchType_Type(Integer32):
    """Custom type adGenAOSQoSMapProtocolMatchType based on Integer32"""
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
        *(("bridged", 2),
          ("netBEIU", 3),
          ("none", 1),
          ("protocolIpv4", 4),
          ("protocolIpv6", 5))
    )


_AdGenAOSQoSMapProtocolMatchType_Type.__name__ = "Integer32"
_AdGenAOSQoSMapProtocolMatchType_Object = MibTableColumn
adGenAOSQoSMapProtocolMatchType = _AdGenAOSQoSMapProtocolMatchType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 1, 8, 1, 9),
    _AdGenAOSQoSMapProtocolMatchType_Type()
)
adGenAOSQoSMapProtocolMatchType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSQoSMapProtocolMatchType.setStatus("current")
_AdGenAOSQoSMapVlanMatchValue_Type = Unsigned32
_AdGenAOSQoSMapVlanMatchValue_Object = MibTableColumn
adGenAOSQoSMapVlanMatchValue = _AdGenAOSQoSMapVlanMatchValue_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 1, 8, 1, 10),
    _AdGenAOSQoSMapVlanMatchValue_Type()
)
adGenAOSQoSMapVlanMatchValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSQoSMapVlanMatchValue.setStatus("current")
_AdGenAOSQoSMapFrDlciMatchValue_Type = Unsigned32
_AdGenAOSQoSMapFrDlciMatchValue_Object = MibTableColumn
adGenAOSQoSMapFrDlciMatchValue = _AdGenAOSQoSMapFrDlciMatchValue_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 1, 8, 1, 11),
    _AdGenAOSQoSMapFrDlciMatchValue_Type()
)
adGenAOSQoSMapFrDlciMatchValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSQoSMapFrDlciMatchValue.setStatus("current")
_AdGenAOSQoSMapShaperTable_Object = MibTable
adGenAOSQoSMapShaperTable = _AdGenAOSQoSMapShaperTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 1, 9)
)
if mibBuilder.loadTexts:
    adGenAOSQoSMapShaperTable.setStatus("current")
_AdGenAOSQoSMapShaperEntry_Object = MibTableRow
adGenAOSQoSMapShaperEntry = _AdGenAOSQoSMapShaperEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 1, 9, 1)
)
adGenAOSQoSMapShaperEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-AOS-QOS", "adGenAOSQoSMapEntryId"),
)
if mibBuilder.loadTexts:
    adGenAOSQoSMapShaperEntry.setStatus("current")
_AdGenAOSQoSMapShaperShapeValue_Type = Unsigned32
_AdGenAOSQoSMapShaperShapeValue_Object = MibTableColumn
adGenAOSQoSMapShaperShapeValue = _AdGenAOSQoSMapShaperShapeValue_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 1, 9, 1, 1),
    _AdGenAOSQoSMapShaperShapeValue_Type()
)
adGenAOSQoSMapShaperShapeValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSQoSMapShaperShapeValue.setStatus("current")
_AdGenAOSQoSMapShaperCurrentBudgetSize_Type = Unsigned32
_AdGenAOSQoSMapShaperCurrentBudgetSize_Object = MibTableColumn
adGenAOSQoSMapShaperCurrentBudgetSize = _AdGenAOSQoSMapShaperCurrentBudgetSize_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 1, 9, 1, 2),
    _AdGenAOSQoSMapShaperCurrentBudgetSize_Type()
)
adGenAOSQoSMapShaperCurrentBudgetSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSQoSMapShaperCurrentBudgetSize.setStatus("current")
_AdGenAOSQoSMapShaperMaxBudgetSize_Type = Unsigned32
_AdGenAOSQoSMapShaperMaxBudgetSize_Object = MibTableColumn
adGenAOSQoSMapShaperMaxBudgetSize = _AdGenAOSQoSMapShaperMaxBudgetSize_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 1, 9, 1, 3),
    _AdGenAOSQoSMapShaperMaxBudgetSize_Type()
)
adGenAOSQoSMapShaperMaxBudgetSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSQoSMapShaperMaxBudgetSize.setStatus("current")
_AdGenAOSQoSMapShaperBytesPerTick_Type = Unsigned32
_AdGenAOSQoSMapShaperBytesPerTick_Object = MibTableColumn
adGenAOSQoSMapShaperBytesPerTick = _AdGenAOSQoSMapShaperBytesPerTick_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 1, 9, 1, 4),
    _AdGenAOSQoSMapShaperBytesPerTick_Type()
)
adGenAOSQoSMapShaperBytesPerTick.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSQoSMapShaperBytesPerTick.setStatus("current")
_AdGenAOSQoSMapShaperTickRate_Type = Unsigned32
_AdGenAOSQoSMapShaperTickRate_Object = MibTableColumn
adGenAOSQoSMapShaperTickRate = _AdGenAOSQoSMapShaperTickRate_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 1, 9, 1, 5),
    _AdGenAOSQoSMapShaperTickRate_Type()
)
adGenAOSQoSMapShaperTickRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSQoSMapShaperTickRate.setStatus("current")
_AdGenAOSQoSMapShaperQueuePktDepth_Type = Counter32
_AdGenAOSQoSMapShaperQueuePktDepth_Object = MibTableColumn
adGenAOSQoSMapShaperQueuePktDepth = _AdGenAOSQoSMapShaperQueuePktDepth_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 1, 9, 1, 6),
    _AdGenAOSQoSMapShaperQueuePktDepth_Type()
)
adGenAOSQoSMapShaperQueuePktDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSQoSMapShaperQueuePktDepth.setStatus("current")
_AdGenAOSQoSMapShaperQueuePktDrops_Type = Counter32
_AdGenAOSQoSMapShaperQueuePktDrops_Object = MibTableColumn
adGenAOSQoSMapShaperQueuePktDrops = _AdGenAOSQoSMapShaperQueuePktDrops_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 1, 9, 1, 7),
    _AdGenAOSQoSMapShaperQueuePktDrops_Type()
)
adGenAOSQoSMapShaperQueuePktDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSQoSMapShaperQueuePktDrops.setStatus("current")
_AdGenAOSQoSMapShaperQueuePktsSent_Type = Counter32
_AdGenAOSQoSMapShaperQueuePktsSent_Object = MibTableColumn
adGenAOSQoSMapShaperQueuePktsSent = _AdGenAOSQoSMapShaperQueuePktsSent_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 1, 9, 1, 8),
    _AdGenAOSQoSMapShaperQueuePktsSent_Type()
)
adGenAOSQoSMapShaperQueuePktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSQoSMapShaperQueuePktsSent.setStatus("current")
_AdGenAOSQoSMapShaperQueuePktsDelayed_Type = Counter32
_AdGenAOSQoSMapShaperQueuePktsDelayed_Object = MibTableColumn
adGenAOSQoSMapShaperQueuePktsDelayed = _AdGenAOSQoSMapShaperQueuePktsDelayed_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 1, 9, 1, 9),
    _AdGenAOSQoSMapShaperQueuePktsDelayed_Type()
)
adGenAOSQoSMapShaperQueuePktsDelayed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSQoSMapShaperQueuePktsDelayed.setStatus("current")
_AdGenAOSQoSConformance_ObjectIdentity = ObjectIdentity
adGenAOSQoSConformance = _AdGenAOSQoSConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 8)
)
_AdGenAOSQoSGroup_ObjectIdentity = ObjectIdentity
adGenAOSQoSGroup = _AdGenAOSQoSGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 8, 1)
)
_AdGenAOSQoSCompliances_ObjectIdentity = ObjectIdentity
adGenAOSQoSCompliances = _AdGenAOSQoSCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 8, 2)
)

# Managed Objects groups

adGenAOSQoSMapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 8, 1, 1)
)
adGenAOSQoSMapGroup.setObjects(
      *(("ADTRAN-AOS-QOS", "adGenAOSQoSMapSetId"),
        ("ADTRAN-AOS-QOS", "adGenAOSQoSMapSetName"),
        ("ADTRAN-AOS-QOS", "adGenAOSQoSMapIsChild"))
)
if mibBuilder.loadTexts:
    adGenAOSQoSMapGroup.setStatus("current")

adGenAOSQoSMapEntryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 8, 1, 2)
)
adGenAOSQoSMapEntryGroup.setObjects(
      *(("ADTRAN-AOS-QOS", "adGenAOSQoSMapEntryId"),
        ("ADTRAN-AOS-QOS", "adGenAOSQoSMapSeqNum"),
        ("ADTRAN-AOS-QOS", "adGenAOSQoSMapEntrySetName"),
        ("ADTRAN-AOS-QOS", "adGenAOSQoSMapChildSetName"),
        ("ADTRAN-AOS-QOS", "adGenAOSQoSMapQueuingActionType"),
        ("ADTRAN-AOS-QOS", "adGenAOSQoSMapQueuingBWType"),
        ("ADTRAN-AOS-QOS", "adGenAOSQoSMapQueuingBWValue"),
        ("ADTRAN-AOS-QOS", "adGenAOSQoSMapQueuingBurstValue"),
        ("ADTRAN-AOS-QOS", "adGenAOSQoSMapMatchAll"),
        ("ADTRAN-AOS-QOS", "adGenAOSQoSMapDscpMarkState"),
        ("ADTRAN-AOS-QOS", "adGenAOSQoSMapDscpMarkValue"),
        ("ADTRAN-AOS-QOS", "adGenAOSQoSMapDscpMarkString"),
        ("ADTRAN-AOS-QOS", "adGenAOSQoSMapPrecedenceMarkState"),
        ("ADTRAN-AOS-QOS", "adGenAOSQoSMapPrecedenceMarkValue"),
        ("ADTRAN-AOS-QOS", "adGenAOSQoSMapCosMarkState"),
        ("ADTRAN-AOS-QOS", "adGenAOSQoSMapCosMarkValue"),
        ("ADTRAN-AOS-QOS", "adGenAOSQoSMapShapeState"),
        ("ADTRAN-AOS-QOS", "adGenAOSQoSMapShapeValue"),
        ("ADTRAN-AOS-QOS", "adGenAOSQoSMapShapeBurst"),
        ("ADTRAN-AOS-QOS", "adGenAOSQoSMapShapeEthOverhead"),
        ("ADTRAN-AOS-QOS", "adGenAOSQoSMapClearCounters"),
        ("ADTRAN-AOS-QOS", "adGenAOSQoSMapPriorityStrictRateLimiting"))
)
if mibBuilder.loadTexts:
    adGenAOSQoSMapEntryGroup.setStatus("current")

adGenAOSQoSInterfaceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 8, 1, 3)
)
adGenAOSQoSInterfaceGroup.setObjects(
      *(("ADTRAN-AOS-QOS", "adGenAOSQoSInterfaceName"),
        ("ADTRAN-AOS-QOS", "adGenAOSQoSInterfaceOutboundMapSetName"),
        ("ADTRAN-AOS-QOS", "adGenAOSQoSInterfaceInboundMapSetName"),
        ("ADTRAN-AOS-QOS", "adGenAOSQoSInterfaceMapState"),
        ("ADTRAN-AOS-QOS", "adGenAOSQoSInterfaceTXQType"),
        ("ADTRAN-AOS-QOS", "adGenAOSQoSInterfaceTXQSubqPktLimit"),
        ("ADTRAN-AOS-QOS", "adGenAOSQoSInterfaceTXQSize"),
        ("ADTRAN-AOS-QOS", "adGenAOSQoSInterfaceTXQPktHighWater"),
        ("ADTRAN-AOS-QOS", "adGenAOSQoSInterfaceTXQMaxTotal"),
        ("ADTRAN-AOS-QOS", "adGenAOSQoSInterfaceTXQDrops"),
        ("ADTRAN-AOS-QOS", "adGenAOSQoSInterfaceTXQHdlcRingLimit"),
        ("ADTRAN-AOS-QOS", "adGenAOSQoSInterfaceTXQAvailableBW"),
        ("ADTRAN-AOS-QOS", "adGenAOSQoSInterfaceTXQConvActive"),
        ("ADTRAN-AOS-QOS", "adGenAOSQoSInterfaceTXQConvMaxActive"),
        ("ADTRAN-AOS-QOS", "adGenAOSQoSInterfaceTXQConvMaxTotal"),
        ("ADTRAN-AOS-QOS", "adGenAOSQoSInterfaceTrafficShapingRate"),
        ("ADTRAN-AOS-QOS", "adGenAOSQoSInterfaceTrafficShapingBurst"),
        ("ADTRAN-AOS-QOS", "adGenAOSQoSInterfaceShaperValue"),
        ("ADTRAN-AOS-QOS", "adGenAOSQoSInterfaceShaperCurrentBudgetSize"),
        ("ADTRAN-AOS-QOS", "adGenAOSQoSInterfaceShaperMaxBudgetSize"),
        ("ADTRAN-AOS-QOS", "adGenAOSQoSInterfaceShaperBytesPerTick"),
        ("ADTRAN-AOS-QOS", "adGenAOSQoSInterfaceShaperTickRate"),
        ("ADTRAN-AOS-QOS", "adGenAOSQoSInterfaceShaperQPktDepth"),
        ("ADTRAN-AOS-QOS", "adGenAOSQoSInterfaceShaperQPktDrops"),
        ("ADTRAN-AOS-QOS", "adGenAOSQoSInterfaceShaperQPktSent"),
        ("ADTRAN-AOS-QOS", "adGenAOSQoSInterfaceShaperQPktDelayed"))
)
if mibBuilder.loadTexts:
    adGenAOSQoSInterfaceGroup.setStatus("current")

adGenAOSQoSClassConvHistoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 8, 1, 4)
)
adGenAOSQoSClassConvHistoryGroup.setObjects(
      *(("ADTRAN-AOS-QOS", "adGenAOSQoSMapParentEntryId"),
        ("ADTRAN-AOS-QOS", "adGenAOSQoSClassConvSetId"),
        ("ADTRAN-AOS-QOS", "adGenAOSQoSHistoryClassConvId"),
        ("ADTRAN-AOS-QOS", "adGenAOSQoSClassConvHistoryMatches"),
        ("ADTRAN-AOS-QOS", "adGenAOSQoSClassConvHistoryDiscards"),
        ("ADTRAN-AOS-QOS", "adGenAOSQoSClassConvHistoryMatchesBytes"),
        ("ADTRAN-AOS-QOS", "adGenAOSQoSClassConvHistoryDiscardsBytes"),
        ("ADTRAN-AOS-QOS", "adGenAOSQoSClassConvHistoryDepth"),
        ("ADTRAN-AOS-QOS", "adGenAOSQoSClassConvHistoryHighWater"),
        ("ADTRAN-AOS-QOS", "adGenAOSQoSClassConvHistoryByteMatchRate"),
        ("ADTRAN-AOS-QOS", "adGenAOSQoSClassConvHistoryByteDiscardRate"),
        ("ADTRAN-AOS-QOS", "adGenAOSQoSClassConvHistoryBitMatchRate"),
        ("ADTRAN-AOS-QOS", "adGenAOSQoSClassConvHistoryBitDiscardRate"))
)
if mibBuilder.loadTexts:
    adGenAOSQoSClassConvHistoryGroup.setStatus("current")

adGenAOSQoSConversationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 8, 1, 5)
)
adGenAOSQoSConversationGroup.setObjects(
      *(("ADTRAN-AOS-QOS", "adGenAOSQoSConvId"),
        ("ADTRAN-AOS-QOS", "adGenAOSQoSMapConvParentEntryId"),
        ("ADTRAN-AOS-QOS", "adGenAOSQoSConvMatches"),
        ("ADTRAN-AOS-QOS", "adGenAOSQoSConvDiscards"),
        ("ADTRAN-AOS-QOS", "adGenAOSQoSConvMatchesBytes"),
        ("ADTRAN-AOS-QOS", "adGenAOSQoSConvDiscardsBytes"),
        ("ADTRAN-AOS-QOS", "adGenAOSQoSConvDepth"),
        ("ADTRAN-AOS-QOS", "adGenAOSQoSConvHighWater"),
        ("ADTRAN-AOS-QOS", "adGenAOSQoSConvWeight"),
        ("ADTRAN-AOS-QOS", "adGenAOSQoSConvPktLen"),
        ("ADTRAN-AOS-QOS", "adGenAOSQoSConvProttype"),
        ("ADTRAN-AOS-QOS", "adGenAOSQoSConvSubQType"),
        ("ADTRAN-AOS-QOS", "adGenAOSQoSConvPktHeader"))
)
if mibBuilder.loadTexts:
    adGenAOSQoSConversationGroup.setStatus("current")

adGenAOSQoSPriorityRateLimiterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 8, 1, 6)
)
adGenAOSQoSPriorityRateLimiterGroup.setObjects(
      *(("ADTRAN-AOS-QOS", "adGenAOSQoSPriorityRateLimiterParentEntryId"),
        ("ADTRAN-AOS-QOS", "adGenAOSQoSPriorityRateLimiterSetId"),
        ("ADTRAN-AOS-QOS", "adGenAOSQoSPriorityRateLimiterCurrBudget"),
        ("ADTRAN-AOS-QOS", "adGenAOSQoSPriorityRateLimiterMaxBudget"),
        ("ADTRAN-AOS-QOS", "adGenAOSQoSPriorityRateLimiterUpdateTimestamp"),
        ("ADTRAN-AOS-QOS", "adGenAOSQoSPriorityRateLimiterBudgetRate"),
        ("ADTRAN-AOS-QOS", "adGenAOSQoSPriorityRateLimiterMaxFillTime"),
        ("ADTRAN-AOS-QOS", "adGenAOSQoSPriorityRateLimiterMatches"),
        ("ADTRAN-AOS-QOS", "adGenAOSQoSPriorityRateLimiterDrops"),
        ("ADTRAN-AOS-QOS", "adGenAOSQoSPriorityRateLimiterMatchesBytes"),
        ("ADTRAN-AOS-QOS", "adGenAOSQoSPriorityRateLimiterDropsBytes"),
        ("ADTRAN-AOS-QOS", "adGenAOSQoSPriorityRateLimiterClearCounters"),
        ("ADTRAN-AOS-QOS", "adGenAOSQoSPriorityRateLimiterByteMatchRate"),
        ("ADTRAN-AOS-QOS", "adGenAOSQoSPriorityRateLimiterByteDiscardRate"),
        ("ADTRAN-AOS-QOS", "adGenAOSQoSPriorityRateLimiterBitMatchRate"),
        ("ADTRAN-AOS-QOS", "adGenAOSQoSPriorityRateLimiterBitDiscardRate"))
)
if mibBuilder.loadTexts:
    adGenAOSQoSPriorityRateLimiterGroup.setStatus("current")

adGenAOSQoSClassifierGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 8, 1, 7)
)
adGenAOSQoSClassifierGroup.setObjects(
      *(("ADTRAN-AOS-QOS", "adGenAOSQoSMapClassifierParentEntryId"),
        ("ADTRAN-AOS-QOS", "adGenAOSQoSClassifierMatches"),
        ("ADTRAN-AOS-QOS", "adGenAOSQoSClassifierDrops"),
        ("ADTRAN-AOS-QOS", "adGenAOSQoSClassifierMatchBytes"),
        ("ADTRAN-AOS-QOS", "adGenAOSQoSClassifierDropBytes"),
        ("ADTRAN-AOS-QOS", "adGenAOSQoSClassifierPktMatchRate"),
        ("ADTRAN-AOS-QOS", "adGenAOSQoSClassifierPktDropRate"),
        ("ADTRAN-AOS-QOS", "adGenAOSQoSClassifierByteMatchRate"),
        ("ADTRAN-AOS-QOS", "adGenAOSQoSClassifierByteDropRate"),
        ("ADTRAN-AOS-QOS", "adGenAOSQoSClassifierBitMatchRate"),
        ("ADTRAN-AOS-QOS", "adGenAOSQoSClassifierBitDropRate"))
)
if mibBuilder.loadTexts:
    adGenAOSQoSClassifierGroup.setStatus("current")

adGenAOSQoSMapMatchGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 8, 1, 8)
)
adGenAOSQoSMapMatchGroup.setObjects(
      *(("ADTRAN-AOS-QOS", "adGenAOSQoSMapSetId"),
        ("ADTRAN-AOS-QOS", "adGenAOSQoSMapSetName"),
        ("ADTRAN-AOS-QOS", "adGenAOSQoSMapMatchEntryId"),
        ("ADTRAN-AOS-QOS", "adGenAOSQoSMapMatchType"),
        ("ADTRAN-AOS-QOS", "adGenAOSQoSMapMatchACL"),
        ("ADTRAN-AOS-QOS", "adGenAOSQoSMapRTPMatchStartPort"),
        ("ADTRAN-AOS-QOS", "adGenAOSQoSMapRTPMatchEndPort"),
        ("ADTRAN-AOS-QOS", "adGenAOSQoSMapRTPMatchPorts"),
        ("ADTRAN-AOS-QOS", "adGenAOSQoSMapDscpMatchValue"),
        ("ADTRAN-AOS-QOS", "adGenAOSQoSMapPrecedenceMatchValue"),
        ("ADTRAN-AOS-QOS", "adGenAOSQoSMapProtocolMatchType"),
        ("ADTRAN-AOS-QOS", "adGenAOSQoSMapVlanMatchValue"),
        ("ADTRAN-AOS-QOS", "adGenAOSQoSMapFrDlciMatchValue"))
)
if mibBuilder.loadTexts:
    adGenAOSQoSMapMatchGroup.setStatus("current")

adGenAOSQoSMapShaperGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 8, 1, 9)
)
adGenAOSQoSMapShaperGroup.setObjects(
      *(("ADTRAN-AOS-QOS", "adGenAOSQoSMapShaperShapeValue"),
        ("ADTRAN-AOS-QOS", "adGenAOSQoSMapShaperCurrentBudgetSize"),
        ("ADTRAN-AOS-QOS", "adGenAOSQoSMapShaperMaxBudgetSize"),
        ("ADTRAN-AOS-QOS", "adGenAOSQoSMapShaperBytesPerTick"),
        ("ADTRAN-AOS-QOS", "adGenAOSQoSMapShaperTickRate"),
        ("ADTRAN-AOS-QOS", "adGenAOSQoSMapShaperQueuePktDepth"),
        ("ADTRAN-AOS-QOS", "adGenAOSQoSMapShaperQueuePktDrops"),
        ("ADTRAN-AOS-QOS", "adGenAOSQoSMapShaperQueuePktsSent"),
        ("ADTRAN-AOS-QOS", "adGenAOSQoSMapShaperQueuePktsDelayed"))
)
if mibBuilder.loadTexts:
    adGenAOSQoSMapShaperGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

adGenAOSQoSFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 8, 2, 1)
)
if mibBuilder.loadTexts:
    adGenAOSQoSFullCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-AOS-QOS",
    **{"Unsigned64": Unsigned64,
       "adGenAOSQos": adGenAOSQos,
       "adGenAOSQoSMapSetTable": adGenAOSQoSMapSetTable,
       "adGenAOSQoSMapSetEntry": adGenAOSQoSMapSetEntry,
       "adGenAOSQoSMapSetId": adGenAOSQoSMapSetId,
       "adGenAOSQoSMapSetName": adGenAOSQoSMapSetName,
       "adGenAOSQoSMapIsChild": adGenAOSQoSMapIsChild,
       "adGenAOSQoSMapEntriesTable": adGenAOSQoSMapEntriesTable,
       "adGenAOSQoSMapEntriesEntry": adGenAOSQoSMapEntriesEntry,
       "adGenAOSQoSMapEntryId": adGenAOSQoSMapEntryId,
       "adGenAOSQoSMapSeqNum": adGenAOSQoSMapSeqNum,
       "adGenAOSQoSMapEntrySetName": adGenAOSQoSMapEntrySetName,
       "adGenAOSQoSMapChildSetName": adGenAOSQoSMapChildSetName,
       "adGenAOSQoSMapQueuingActionType": adGenAOSQoSMapQueuingActionType,
       "adGenAOSQoSMapQueuingBWType": adGenAOSQoSMapQueuingBWType,
       "adGenAOSQoSMapQueuingBWValue": adGenAOSQoSMapQueuingBWValue,
       "adGenAOSQoSMapQueuingBurstValue": adGenAOSQoSMapQueuingBurstValue,
       "adGenAOSQoSMapMatchAll": adGenAOSQoSMapMatchAll,
       "adGenAOSQoSMapDscpMarkState": adGenAOSQoSMapDscpMarkState,
       "adGenAOSQoSMapDscpMarkValue": adGenAOSQoSMapDscpMarkValue,
       "adGenAOSQoSMapDscpMarkString": adGenAOSQoSMapDscpMarkString,
       "adGenAOSQoSMapPrecedenceMarkState": adGenAOSQoSMapPrecedenceMarkState,
       "adGenAOSQoSMapPrecedenceMarkValue": adGenAOSQoSMapPrecedenceMarkValue,
       "adGenAOSQoSMapCosMarkState": adGenAOSQoSMapCosMarkState,
       "adGenAOSQoSMapCosMarkValue": adGenAOSQoSMapCosMarkValue,
       "adGenAOSQoSMapShapeState": adGenAOSQoSMapShapeState,
       "adGenAOSQoSMapShapeValue": adGenAOSQoSMapShapeValue,
       "adGenAOSQoSMapShapeBurst": adGenAOSQoSMapShapeBurst,
       "adGenAOSQoSMapShapeEthOverhead": adGenAOSQoSMapShapeEthOverhead,
       "adGenAOSQoSMapClearCounters": adGenAOSQoSMapClearCounters,
       "adGenAOSQoSMapPriorityStrictRateLimiting": adGenAOSQoSMapPriorityStrictRateLimiting,
       "adGenAOSQoSInterfaceTable": adGenAOSQoSInterfaceTable,
       "adGenAOSQoSInterfaceEntry": adGenAOSQoSInterfaceEntry,
       "adGenAOSQoSInterfaceName": adGenAOSQoSInterfaceName,
       "adGenAOSQoSInterfaceOutboundMapSetName": adGenAOSQoSInterfaceOutboundMapSetName,
       "adGenAOSQoSInterfaceInboundMapSetName": adGenAOSQoSInterfaceInboundMapSetName,
       "adGenAOSQoSInterfaceMapState": adGenAOSQoSInterfaceMapState,
       "adGenAOSQoSInterfaceTXQType": adGenAOSQoSInterfaceTXQType,
       "adGenAOSQoSInterfaceTXQSubqPktLimit": adGenAOSQoSInterfaceTXQSubqPktLimit,
       "adGenAOSQoSInterfaceTXQSize": adGenAOSQoSInterfaceTXQSize,
       "adGenAOSQoSInterfaceTXQPktHighWater": adGenAOSQoSInterfaceTXQPktHighWater,
       "adGenAOSQoSInterfaceTXQMaxTotal": adGenAOSQoSInterfaceTXQMaxTotal,
       "adGenAOSQoSInterfaceTXQDrops": adGenAOSQoSInterfaceTXQDrops,
       "adGenAOSQoSInterfaceTXQHdlcRingLimit": adGenAOSQoSInterfaceTXQHdlcRingLimit,
       "adGenAOSQoSInterfaceTXQAvailableBW": adGenAOSQoSInterfaceTXQAvailableBW,
       "adGenAOSQoSInterfaceTXQConvActive": adGenAOSQoSInterfaceTXQConvActive,
       "adGenAOSQoSInterfaceTXQConvMaxActive": adGenAOSQoSInterfaceTXQConvMaxActive,
       "adGenAOSQoSInterfaceTXQConvMaxTotal": adGenAOSQoSInterfaceTXQConvMaxTotal,
       "adGenAOSQoSInterfaceTrafficShapingRate": adGenAOSQoSInterfaceTrafficShapingRate,
       "adGenAOSQoSInterfaceTrafficShapingBurst": adGenAOSQoSInterfaceTrafficShapingBurst,
       "adGenAOSQoSInterfaceShaperValue": adGenAOSQoSInterfaceShaperValue,
       "adGenAOSQoSInterfaceShaperCurrentBudgetSize": adGenAOSQoSInterfaceShaperCurrentBudgetSize,
       "adGenAOSQoSInterfaceShaperMaxBudgetSize": adGenAOSQoSInterfaceShaperMaxBudgetSize,
       "adGenAOSQoSInterfaceShaperBytesPerTick": adGenAOSQoSInterfaceShaperBytesPerTick,
       "adGenAOSQoSInterfaceShaperTickRate": adGenAOSQoSInterfaceShaperTickRate,
       "adGenAOSQoSInterfaceShaperQPktDepth": adGenAOSQoSInterfaceShaperQPktDepth,
       "adGenAOSQoSInterfaceShaperQPktDrops": adGenAOSQoSInterfaceShaperQPktDrops,
       "adGenAOSQoSInterfaceShaperQPktSent": adGenAOSQoSInterfaceShaperQPktSent,
       "adGenAOSQoSInterfaceShaperQPktDelayed": adGenAOSQoSInterfaceShaperQPktDelayed,
       "adGenAOSQoSClassConvHistoryTable": adGenAOSQoSClassConvHistoryTable,
       "adGenAOSQoSClassConvHistoryEntry": adGenAOSQoSClassConvHistoryEntry,
       "adGenAOSQoSMapParentEntryId": adGenAOSQoSMapParentEntryId,
       "adGenAOSQoSClassConvSetId": adGenAOSQoSClassConvSetId,
       "adGenAOSQoSHistoryClassConvId": adGenAOSQoSHistoryClassConvId,
       "adGenAOSQoSClassConvHistoryMatches": adGenAOSQoSClassConvHistoryMatches,
       "adGenAOSQoSClassConvHistoryDiscards": adGenAOSQoSClassConvHistoryDiscards,
       "adGenAOSQoSClassConvHistoryMatchesBytes": adGenAOSQoSClassConvHistoryMatchesBytes,
       "adGenAOSQoSClassConvHistoryDiscardsBytes": adGenAOSQoSClassConvHistoryDiscardsBytes,
       "adGenAOSQoSClassConvHistoryDepth": adGenAOSQoSClassConvHistoryDepth,
       "adGenAOSQoSClassConvHistoryHighWater": adGenAOSQoSClassConvHistoryHighWater,
       "adGenAOSQoSClassConvHistoryByteMatchRate": adGenAOSQoSClassConvHistoryByteMatchRate,
       "adGenAOSQoSClassConvHistoryByteDiscardRate": adGenAOSQoSClassConvHistoryByteDiscardRate,
       "adGenAOSQoSClassConvHistoryBitMatchRate": adGenAOSQoSClassConvHistoryBitMatchRate,
       "adGenAOSQoSClassConvHistoryBitDiscardRate": adGenAOSQoSClassConvHistoryBitDiscardRate,
       "adGenAOSQoSConversationTable": adGenAOSQoSConversationTable,
       "adGenAOSQoSConversationEntry": adGenAOSQoSConversationEntry,
       "adGenAOSQoSConvId": adGenAOSQoSConvId,
       "adGenAOSQoSMapConvParentEntryId": adGenAOSQoSMapConvParentEntryId,
       "adGenAOSQoSConvMatches": adGenAOSQoSConvMatches,
       "adGenAOSQoSConvDiscards": adGenAOSQoSConvDiscards,
       "adGenAOSQoSConvMatchesBytes": adGenAOSQoSConvMatchesBytes,
       "adGenAOSQoSConvDiscardsBytes": adGenAOSQoSConvDiscardsBytes,
       "adGenAOSQoSConvDepth": adGenAOSQoSConvDepth,
       "adGenAOSQoSConvHighWater": adGenAOSQoSConvHighWater,
       "adGenAOSQoSConvWeight": adGenAOSQoSConvWeight,
       "adGenAOSQoSConvPktLen": adGenAOSQoSConvPktLen,
       "adGenAOSQoSConvProttype": adGenAOSQoSConvProttype,
       "adGenAOSQoSConvSubQType": adGenAOSQoSConvSubQType,
       "adGenAOSQoSConvPktHeader": adGenAOSQoSConvPktHeader,
       "adGenAOSQoSPriorityRateLimiterTable": adGenAOSQoSPriorityRateLimiterTable,
       "adGenAOSQoSPriorityRateLimiterEntry": adGenAOSQoSPriorityRateLimiterEntry,
       "adGenAOSQoSPriorityRateLimiterParentEntryId": adGenAOSQoSPriorityRateLimiterParentEntryId,
       "adGenAOSQoSPriorityRateLimiterSetId": adGenAOSQoSPriorityRateLimiterSetId,
       "adGenAOSQoSPriorityRateLimiterCurrBudget": adGenAOSQoSPriorityRateLimiterCurrBudget,
       "adGenAOSQoSPriorityRateLimiterMaxBudget": adGenAOSQoSPriorityRateLimiterMaxBudget,
       "adGenAOSQoSPriorityRateLimiterUpdateTimestamp": adGenAOSQoSPriorityRateLimiterUpdateTimestamp,
       "adGenAOSQoSPriorityRateLimiterBudgetRate": adGenAOSQoSPriorityRateLimiterBudgetRate,
       "adGenAOSQoSPriorityRateLimiterMaxFillTime": adGenAOSQoSPriorityRateLimiterMaxFillTime,
       "adGenAOSQoSPriorityRateLimiterMatches": adGenAOSQoSPriorityRateLimiterMatches,
       "adGenAOSQoSPriorityRateLimiterDrops": adGenAOSQoSPriorityRateLimiterDrops,
       "adGenAOSQoSPriorityRateLimiterMatchesBytes": adGenAOSQoSPriorityRateLimiterMatchesBytes,
       "adGenAOSQoSPriorityRateLimiterDropsBytes": adGenAOSQoSPriorityRateLimiterDropsBytes,
       "adGenAOSQoSPriorityRateLimiterClearCounters": adGenAOSQoSPriorityRateLimiterClearCounters,
       "adGenAOSQoSPriorityRateLimiterByteMatchRate": adGenAOSQoSPriorityRateLimiterByteMatchRate,
       "adGenAOSQoSPriorityRateLimiterByteDiscardRate": adGenAOSQoSPriorityRateLimiterByteDiscardRate,
       "adGenAOSQoSPriorityRateLimiterBitMatchRate": adGenAOSQoSPriorityRateLimiterBitMatchRate,
       "adGenAOSQoSPriorityRateLimiterBitDiscardRate": adGenAOSQoSPriorityRateLimiterBitDiscardRate,
       "adGenAOSQoSMapClassifierStatsTable": adGenAOSQoSMapClassifierStatsTable,
       "adGenAOSQoSMapClassifierStatsEntry": adGenAOSQoSMapClassifierStatsEntry,
       "adGenAOSQoSMapClassifierParentEntryId": adGenAOSQoSMapClassifierParentEntryId,
       "adGenAOSQoSClassifierMatches": adGenAOSQoSClassifierMatches,
       "adGenAOSQoSClassifierDrops": adGenAOSQoSClassifierDrops,
       "adGenAOSQoSClassifierMatchBytes": adGenAOSQoSClassifierMatchBytes,
       "adGenAOSQoSClassifierDropBytes": adGenAOSQoSClassifierDropBytes,
       "adGenAOSQoSClassifierPktMatchRate": adGenAOSQoSClassifierPktMatchRate,
       "adGenAOSQoSClassifierPktDropRate": adGenAOSQoSClassifierPktDropRate,
       "adGenAOSQoSClassifierByteMatchRate": adGenAOSQoSClassifierByteMatchRate,
       "adGenAOSQoSClassifierByteDropRate": adGenAOSQoSClassifierByteDropRate,
       "adGenAOSQoSClassifierBitMatchRate": adGenAOSQoSClassifierBitMatchRate,
       "adGenAOSQoSClassifierBitDropRate": adGenAOSQoSClassifierBitDropRate,
       "adGenAOSQoSMapMatchTable": adGenAOSQoSMapMatchTable,
       "adGenAOSQoSMapMatchEntry": adGenAOSQoSMapMatchEntry,
       "adGenAOSQoSMapMatchEntryId": adGenAOSQoSMapMatchEntryId,
       "adGenAOSQoSMapMatchType": adGenAOSQoSMapMatchType,
       "adGenAOSQoSMapMatchACL": adGenAOSQoSMapMatchACL,
       "adGenAOSQoSMapRTPMatchStartPort": adGenAOSQoSMapRTPMatchStartPort,
       "adGenAOSQoSMapRTPMatchEndPort": adGenAOSQoSMapRTPMatchEndPort,
       "adGenAOSQoSMapRTPMatchPorts": adGenAOSQoSMapRTPMatchPorts,
       "adGenAOSQoSMapDscpMatchValue": adGenAOSQoSMapDscpMatchValue,
       "adGenAOSQoSMapPrecedenceMatchValue": adGenAOSQoSMapPrecedenceMatchValue,
       "adGenAOSQoSMapProtocolMatchType": adGenAOSQoSMapProtocolMatchType,
       "adGenAOSQoSMapVlanMatchValue": adGenAOSQoSMapVlanMatchValue,
       "adGenAOSQoSMapFrDlciMatchValue": adGenAOSQoSMapFrDlciMatchValue,
       "adGenAOSQoSMapShaperTable": adGenAOSQoSMapShaperTable,
       "adGenAOSQoSMapShaperEntry": adGenAOSQoSMapShaperEntry,
       "adGenAOSQoSMapShaperShapeValue": adGenAOSQoSMapShaperShapeValue,
       "adGenAOSQoSMapShaperCurrentBudgetSize": adGenAOSQoSMapShaperCurrentBudgetSize,
       "adGenAOSQoSMapShaperMaxBudgetSize": adGenAOSQoSMapShaperMaxBudgetSize,
       "adGenAOSQoSMapShaperBytesPerTick": adGenAOSQoSMapShaperBytesPerTick,
       "adGenAOSQoSMapShaperTickRate": adGenAOSQoSMapShaperTickRate,
       "adGenAOSQoSMapShaperQueuePktDepth": adGenAOSQoSMapShaperQueuePktDepth,
       "adGenAOSQoSMapShaperQueuePktDrops": adGenAOSQoSMapShaperQueuePktDrops,
       "adGenAOSQoSMapShaperQueuePktsSent": adGenAOSQoSMapShaperQueuePktsSent,
       "adGenAOSQoSMapShaperQueuePktsDelayed": adGenAOSQoSMapShaperQueuePktsDelayed,
       "adGenAOSQoSConformance": adGenAOSQoSConformance,
       "adGenAOSQoSGroup": adGenAOSQoSGroup,
       "adGenAOSQoSMapGroup": adGenAOSQoSMapGroup,
       "adGenAOSQoSMapEntryGroup": adGenAOSQoSMapEntryGroup,
       "adGenAOSQoSInterfaceGroup": adGenAOSQoSInterfaceGroup,
       "adGenAOSQoSClassConvHistoryGroup": adGenAOSQoSClassConvHistoryGroup,
       "adGenAOSQoSConversationGroup": adGenAOSQoSConversationGroup,
       "adGenAOSQoSPriorityRateLimiterGroup": adGenAOSQoSPriorityRateLimiterGroup,
       "adGenAOSQoSClassifierGroup": adGenAOSQoSClassifierGroup,
       "adGenAOSQoSMapMatchGroup": adGenAOSQoSMapMatchGroup,
       "adGenAOSQoSMapShaperGroup": adGenAOSQoSMapShaperGroup,
       "adGenAOSQoSCompliances": adGenAOSQoSCompliances,
       "adGenAOSQoSFullCompliance": adGenAOSQoSFullCompliance,
       "adGenAOSQoSMib": adGenAOSQoSMib}
)
