# SNMP MIB module (CENTILLION-FILTERS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CENTILLION-FILTERS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:54:05 2024
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

(StatusIndicator,
 sysConfig) = mibBuilder.importSymbols(
    "CENTILLION-ROOT-MIB",
    "StatusIndicator",
    "sysConfig")

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



class GeneralFilterName(DisplayString):
    """Custom type GeneralFilterName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )





class NetbiosFilterName(DisplayString):
    """Custom type NetbiosFilterName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )





class NetbiosFilterAction(Integer32):
    """Custom type NetbiosFilterAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("discard", 1),
          ("forward", 2))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FilterGroup_ObjectIdentity = ObjectIdentity
filterGroup = _FilterGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 11)
)
_FilterGroupTable_Object = MibTable
filterGroupTable = _FilterGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 11, 1)
)
if mibBuilder.loadTexts:
    filterGroupTable.setStatus("mandatory")
_FilterGroupEntry_Object = MibTableRow
filterGroupEntry = _FilterGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 11, 1, 1)
)
filterGroupEntry.setIndexNames(
    (0, "CENTILLION-FILTERS-MIB", "filterGroupName"),
    (0, "CENTILLION-FILTERS-MIB", "filterGroupIndex"),
)
if mibBuilder.loadTexts:
    filterGroupEntry.setStatus("mandatory")
_FilterGroupName_Type = GeneralFilterName
_FilterGroupName_Object = MibTableColumn
filterGroupName = _FilterGroupName_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 11, 1, 1, 1),
    _FilterGroupName_Type()
)
filterGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterGroupName.setStatus("mandatory")
_FilterGroupIndex_Type = Integer32
_FilterGroupIndex_Object = MibTableColumn
filterGroupIndex = _FilterGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 11, 1, 1, 2),
    _FilterGroupIndex_Type()
)
filterGroupIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterGroupIndex.setStatus("mandatory")
_FilterGroupStatus_Type = StatusIndicator
_FilterGroupStatus_Object = MibTableColumn
filterGroupStatus = _FilterGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 11, 1, 1, 3),
    _FilterGroupStatus_Type()
)
filterGroupStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterGroupStatus.setStatus("mandatory")


class _FilterGroupMatch_Type(Integer32):
    """Custom type filterGroupMatch based on Integer32"""
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
        *(("eq", 2),
          ("ge", 6),
          ("gt", 4),
          ("le", 3),
          ("lt", 1),
          ("ne", 5))
    )


_FilterGroupMatch_Type.__name__ = "Integer32"
_FilterGroupMatch_Object = MibTableColumn
filterGroupMatch = _FilterGroupMatch_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 11, 1, 1, 4),
    _FilterGroupMatch_Type()
)
filterGroupMatch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterGroupMatch.setStatus("mandatory")


class _FilterGroupType_Type(Integer32):
    """Custom type filterGroupType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("llcFilter", 2),
          ("macFilter", 1),
          ("vlanFilter", 3))
    )


_FilterGroupType_Type.__name__ = "Integer32"
_FilterGroupType_Object = MibTableColumn
filterGroupType = _FilterGroupType_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 11, 1, 1, 5),
    _FilterGroupType_Type()
)
filterGroupType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterGroupType.setStatus("mandatory")
_FilterGroupOffset_Type = Integer32
_FilterGroupOffset_Object = MibTableColumn
filterGroupOffset = _FilterGroupOffset_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 11, 1, 1, 6),
    _FilterGroupOffset_Type()
)
filterGroupOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterGroupOffset.setStatus("mandatory")


class _FilterGroupValue_Type(OctetString):
    """Custom type filterGroupValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 12),
    )


_FilterGroupValue_Type.__name__ = "OctetString"
_FilterGroupValue_Object = MibTableColumn
filterGroupValue = _FilterGroupValue_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 11, 1, 1, 7),
    _FilterGroupValue_Type()
)
filterGroupValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterGroupValue.setStatus("mandatory")


class _FilterGroupForward_Type(Integer32):
    """Custom type filterGroupForward based on Integer32"""
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
        *(("add", 3),
          ("addAlt", 4),
          ("alt", 2),
          ("drop", 9),
          ("norm", 5),
          ("normAdd", 7),
          ("normAddAlt", 8),
          ("normAlt", 6),
          ("normClear", 1))
    )


_FilterGroupForward_Type.__name__ = "Integer32"
_FilterGroupForward_Object = MibTableColumn
filterGroupForward = _FilterGroupForward_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 11, 1, 1, 8),
    _FilterGroupForward_Type()
)
filterGroupForward.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterGroupForward.setStatus("mandatory")
_FilterGroupNextIfMatch_Type = Integer32
_FilterGroupNextIfMatch_Object = MibTableColumn
filterGroupNextIfMatch = _FilterGroupNextIfMatch_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 11, 1, 1, 9),
    _FilterGroupNextIfMatch_Type()
)
filterGroupNextIfMatch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterGroupNextIfMatch.setStatus("mandatory")
_FilterGroupNextIfFail_Type = Integer32
_FilterGroupNextIfFail_Object = MibTableColumn
filterGroupNextIfFail = _FilterGroupNextIfFail_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 11, 1, 1, 10),
    _FilterGroupNextIfFail_Type()
)
filterGroupNextIfFail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterGroupNextIfFail.setStatus("mandatory")


class _FilterGroupAdditionalDests_Type(OctetString):
    """Custom type filterGroupAdditionalDests based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_FilterGroupAdditionalDests_Type.__name__ = "OctetString"
_FilterGroupAdditionalDests_Object = MibTableColumn
filterGroupAdditionalDests = _FilterGroupAdditionalDests_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 11, 1, 1, 11),
    _FilterGroupAdditionalDests_Type()
)
filterGroupAdditionalDests.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterGroupAdditionalDests.setStatus("deprecated")


class _FilterGroupMonitorDests_Type(OctetString):
    """Custom type filterGroupMonitorDests based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1),
    )


_FilterGroupMonitorDests_Type.__name__ = "OctetString"
_FilterGroupMonitorDests_Object = MibTableColumn
filterGroupMonitorDests = _FilterGroupMonitorDests_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 11, 1, 1, 12),
    _FilterGroupMonitorDests_Type()
)
filterGroupMonitorDests.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterGroupMonitorDests.setStatus("deprecated")


class _FilterGroupAdditionalDestinations_Type(OctetString):
    """Custom type filterGroupAdditionalDestinations based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_FilterGroupAdditionalDestinations_Type.__name__ = "OctetString"
_FilterGroupAdditionalDestinations_Object = MibTableColumn
filterGroupAdditionalDestinations = _FilterGroupAdditionalDestinations_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 11, 1, 1, 13),
    _FilterGroupAdditionalDestinations_Type()
)
filterGroupAdditionalDestinations.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterGroupAdditionalDestinations.setStatus("mandatory")


class _FilterGroupAlternateDestination_Type(OctetString):
    """Custom type filterGroupAlternateDestination based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )


_FilterGroupAlternateDestination_Type.__name__ = "OctetString"
_FilterGroupAlternateDestination_Object = MibTableColumn
filterGroupAlternateDestination = _FilterGroupAlternateDestination_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 11, 1, 1, 14),
    _FilterGroupAlternateDestination_Type()
)
filterGroupAlternateDestination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterGroupAlternateDestination.setStatus("mandatory")
_FilterPortTable_Object = MibTable
filterPortTable = _FilterPortTable_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 11, 2)
)
if mibBuilder.loadTexts:
    filterPortTable.setStatus("mandatory")
_FilterPortEntry_Object = MibTableRow
filterPortEntry = _FilterPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 11, 2, 1)
)
filterPortEntry.setIndexNames(
    (0, "CENTILLION-FILTERS-MIB", "filterPortCardNumber"),
    (0, "CENTILLION-FILTERS-MIB", "filterPortPortNumber"),
    (0, "CENTILLION-FILTERS-MIB", "filterPortIndex"),
)
if mibBuilder.loadTexts:
    filterPortEntry.setStatus("mandatory")
_FilterPortCardNumber_Type = Integer32
_FilterPortCardNumber_Object = MibTableColumn
filterPortCardNumber = _FilterPortCardNumber_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 11, 2, 1, 1),
    _FilterPortCardNumber_Type()
)
filterPortCardNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterPortCardNumber.setStatus("mandatory")
_FilterPortPortNumber_Type = Integer32
_FilterPortPortNumber_Object = MibTableColumn
filterPortPortNumber = _FilterPortPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 11, 2, 1, 2),
    _FilterPortPortNumber_Type()
)
filterPortPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterPortPortNumber.setStatus("mandatory")
_FilterPortIndex_Type = Integer32
_FilterPortIndex_Object = MibTableColumn
filterPortIndex = _FilterPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 11, 2, 1, 3),
    _FilterPortIndex_Type()
)
filterPortIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterPortIndex.setStatus("mandatory")
_FilterPortStatus_Type = StatusIndicator
_FilterPortStatus_Object = MibTableColumn
filterPortStatus = _FilterPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 11, 2, 1, 4),
    _FilterPortStatus_Type()
)
filterPortStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterPortStatus.setStatus("mandatory")
_FilterPortGroupName_Type = GeneralFilterName
_FilterPortGroupName_Object = MibTableColumn
filterPortGroupName = _FilterPortGroupName_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 11, 2, 1, 5),
    _FilterPortGroupName_Type()
)
filterPortGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterPortGroupName.setStatus("mandatory")
_NetbiosFilterPortTable_Object = MibTable
netbiosFilterPortTable = _NetbiosFilterPortTable_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 11, 3)
)
if mibBuilder.loadTexts:
    netbiosFilterPortTable.setStatus("mandatory")
_NetbiosFilterPortEntry_Object = MibTableRow
netbiosFilterPortEntry = _NetbiosFilterPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 11, 3, 1)
)
netbiosFilterPortEntry.setIndexNames(
    (0, "CENTILLION-FILTERS-MIB", "netbiosFilterPortCardNumber"),
    (0, "CENTILLION-FILTERS-MIB", "netbiosFilterPortPortNumber"),
    (0, "CENTILLION-FILTERS-MIB", "netbiosFilterPortIndex"),
)
if mibBuilder.loadTexts:
    netbiosFilterPortEntry.setStatus("mandatory")
_NetbiosFilterPortCardNumber_Type = Integer32
_NetbiosFilterPortCardNumber_Object = MibTableColumn
netbiosFilterPortCardNumber = _NetbiosFilterPortCardNumber_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 11, 3, 1, 1),
    _NetbiosFilterPortCardNumber_Type()
)
netbiosFilterPortCardNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netbiosFilterPortCardNumber.setStatus("mandatory")
_NetbiosFilterPortPortNumber_Type = Integer32
_NetbiosFilterPortPortNumber_Object = MibTableColumn
netbiosFilterPortPortNumber = _NetbiosFilterPortPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 11, 3, 1, 2),
    _NetbiosFilterPortPortNumber_Type()
)
netbiosFilterPortPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netbiosFilterPortPortNumber.setStatus("mandatory")
_NetbiosFilterPortIndex_Type = Integer32
_NetbiosFilterPortIndex_Object = MibTableColumn
netbiosFilterPortIndex = _NetbiosFilterPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 11, 3, 1, 3),
    _NetbiosFilterPortIndex_Type()
)
netbiosFilterPortIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netbiosFilterPortIndex.setStatus("mandatory")
_NetbiosFilterPortStatus_Type = StatusIndicator
_NetbiosFilterPortStatus_Object = MibTableColumn
netbiosFilterPortStatus = _NetbiosFilterPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 11, 3, 1, 4),
    _NetbiosFilterPortStatus_Type()
)
netbiosFilterPortStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netbiosFilterPortStatus.setStatus("mandatory")
_NetbiosFilterPortName_Type = NetbiosFilterName
_NetbiosFilterPortName_Object = MibTableColumn
netbiosFilterPortName = _NetbiosFilterPortName_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 11, 3, 1, 5),
    _NetbiosFilterPortName_Type()
)
netbiosFilterPortName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netbiosFilterPortName.setStatus("mandatory")
_NetbiosFilterPortAction_Type = NetbiosFilterAction
_NetbiosFilterPortAction_Object = MibTableColumn
netbiosFilterPortAction = _NetbiosFilterPortAction_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 11, 3, 1, 6),
    _NetbiosFilterPortAction_Type()
)
netbiosFilterPortAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netbiosFilterPortAction.setStatus("mandatory")
_NetbiosFilterRingTable_Object = MibTable
netbiosFilterRingTable = _NetbiosFilterRingTable_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 11, 4)
)
if mibBuilder.loadTexts:
    netbiosFilterRingTable.setStatus("mandatory")
_NetbiosFilterRingEntry_Object = MibTableRow
netbiosFilterRingEntry = _NetbiosFilterRingEntry_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 11, 4, 1)
)
netbiosFilterRingEntry.setIndexNames(
    (0, "CENTILLION-FILTERS-MIB", "netbiosFilterRingNumber"),
    (0, "CENTILLION-FILTERS-MIB", "netbiosFilterRingIndex"),
)
if mibBuilder.loadTexts:
    netbiosFilterRingEntry.setStatus("mandatory")
_NetbiosFilterRingNumber_Type = Integer32
_NetbiosFilterRingNumber_Object = MibTableColumn
netbiosFilterRingNumber = _NetbiosFilterRingNumber_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 11, 4, 1, 1),
    _NetbiosFilterRingNumber_Type()
)
netbiosFilterRingNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netbiosFilterRingNumber.setStatus("mandatory")
_NetbiosFilterRingIndex_Type = Integer32
_NetbiosFilterRingIndex_Object = MibTableColumn
netbiosFilterRingIndex = _NetbiosFilterRingIndex_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 11, 4, 1, 2),
    _NetbiosFilterRingIndex_Type()
)
netbiosFilterRingIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netbiosFilterRingIndex.setStatus("mandatory")
_NetbiosFilterRingStatus_Type = StatusIndicator
_NetbiosFilterRingStatus_Object = MibTableColumn
netbiosFilterRingStatus = _NetbiosFilterRingStatus_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 11, 4, 1, 3),
    _NetbiosFilterRingStatus_Type()
)
netbiosFilterRingStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netbiosFilterRingStatus.setStatus("mandatory")
_NetbiosFilterRingName_Type = NetbiosFilterName
_NetbiosFilterRingName_Object = MibTableColumn
netbiosFilterRingName = _NetbiosFilterRingName_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 11, 4, 1, 4),
    _NetbiosFilterRingName_Type()
)
netbiosFilterRingName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netbiosFilterRingName.setStatus("mandatory")
_NetbiosFilterRingAction_Type = NetbiosFilterAction
_NetbiosFilterRingAction_Object = MibTableColumn
netbiosFilterRingAction = _NetbiosFilterRingAction_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 11, 4, 1, 5),
    _NetbiosFilterRingAction_Type()
)
netbiosFilterRingAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netbiosFilterRingAction.setStatus("mandatory")
_OutputFilterPortTable_Object = MibTable
outputFilterPortTable = _OutputFilterPortTable_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 11, 5)
)
if mibBuilder.loadTexts:
    outputFilterPortTable.setStatus("mandatory")
_OutputFilterPortEntry_Object = MibTableRow
outputFilterPortEntry = _OutputFilterPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 11, 5, 1)
)
outputFilterPortEntry.setIndexNames(
    (0, "CENTILLION-FILTERS-MIB", "outputFilterPortCardNumber"),
    (0, "CENTILLION-FILTERS-MIB", "outputFilterPortPortNumber"),
    (0, "CENTILLION-FILTERS-MIB", "outputFilterPortIndex"),
)
if mibBuilder.loadTexts:
    outputFilterPortEntry.setStatus("mandatory")
_OutputFilterPortCardNumber_Type = Integer32
_OutputFilterPortCardNumber_Object = MibTableColumn
outputFilterPortCardNumber = _OutputFilterPortCardNumber_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 11, 5, 1, 1),
    _OutputFilterPortCardNumber_Type()
)
outputFilterPortCardNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outputFilterPortCardNumber.setStatus("mandatory")
_OutputFilterPortPortNumber_Type = Integer32
_OutputFilterPortPortNumber_Object = MibTableColumn
outputFilterPortPortNumber = _OutputFilterPortPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 11, 5, 1, 2),
    _OutputFilterPortPortNumber_Type()
)
outputFilterPortPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outputFilterPortPortNumber.setStatus("mandatory")
_OutputFilterPortIndex_Type = Integer32
_OutputFilterPortIndex_Object = MibTableColumn
outputFilterPortIndex = _OutputFilterPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 11, 5, 1, 3),
    _OutputFilterPortIndex_Type()
)
outputFilterPortIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outputFilterPortIndex.setStatus("mandatory")
_OutputFilterPortStatus_Type = StatusIndicator
_OutputFilterPortStatus_Object = MibTableColumn
outputFilterPortStatus = _OutputFilterPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 11, 5, 1, 4),
    _OutputFilterPortStatus_Type()
)
outputFilterPortStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outputFilterPortStatus.setStatus("mandatory")
_OutputFilterPortGroupName_Type = GeneralFilterName
_OutputFilterPortGroupName_Object = MibTableColumn
outputFilterPortGroupName = _OutputFilterPortGroupName_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 11, 5, 1, 5),
    _OutputFilterPortGroupName_Type()
)
outputFilterPortGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outputFilterPortGroupName.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CENTILLION-FILTERS-MIB",
    **{"GeneralFilterName": GeneralFilterName,
       "NetbiosFilterName": NetbiosFilterName,
       "NetbiosFilterAction": NetbiosFilterAction,
       "filterGroup": filterGroup,
       "filterGroupTable": filterGroupTable,
       "filterGroupEntry": filterGroupEntry,
       "filterGroupName": filterGroupName,
       "filterGroupIndex": filterGroupIndex,
       "filterGroupStatus": filterGroupStatus,
       "filterGroupMatch": filterGroupMatch,
       "filterGroupType": filterGroupType,
       "filterGroupOffset": filterGroupOffset,
       "filterGroupValue": filterGroupValue,
       "filterGroupForward": filterGroupForward,
       "filterGroupNextIfMatch": filterGroupNextIfMatch,
       "filterGroupNextIfFail": filterGroupNextIfFail,
       "filterGroupAdditionalDests": filterGroupAdditionalDests,
       "filterGroupMonitorDests": filterGroupMonitorDests,
       "filterGroupAdditionalDestinations": filterGroupAdditionalDestinations,
       "filterGroupAlternateDestination": filterGroupAlternateDestination,
       "filterPortTable": filterPortTable,
       "filterPortEntry": filterPortEntry,
       "filterPortCardNumber": filterPortCardNumber,
       "filterPortPortNumber": filterPortPortNumber,
       "filterPortIndex": filterPortIndex,
       "filterPortStatus": filterPortStatus,
       "filterPortGroupName": filterPortGroupName,
       "netbiosFilterPortTable": netbiosFilterPortTable,
       "netbiosFilterPortEntry": netbiosFilterPortEntry,
       "netbiosFilterPortCardNumber": netbiosFilterPortCardNumber,
       "netbiosFilterPortPortNumber": netbiosFilterPortPortNumber,
       "netbiosFilterPortIndex": netbiosFilterPortIndex,
       "netbiosFilterPortStatus": netbiosFilterPortStatus,
       "netbiosFilterPortName": netbiosFilterPortName,
       "netbiosFilterPortAction": netbiosFilterPortAction,
       "netbiosFilterRingTable": netbiosFilterRingTable,
       "netbiosFilterRingEntry": netbiosFilterRingEntry,
       "netbiosFilterRingNumber": netbiosFilterRingNumber,
       "netbiosFilterRingIndex": netbiosFilterRingIndex,
       "netbiosFilterRingStatus": netbiosFilterRingStatus,
       "netbiosFilterRingName": netbiosFilterRingName,
       "netbiosFilterRingAction": netbiosFilterRingAction,
       "outputFilterPortTable": outputFilterPortTable,
       "outputFilterPortEntry": outputFilterPortEntry,
       "outputFilterPortCardNumber": outputFilterPortCardNumber,
       "outputFilterPortPortNumber": outputFilterPortPortNumber,
       "outputFilterPortIndex": outputFilterPortIndex,
       "outputFilterPortStatus": outputFilterPortStatus,
       "outputFilterPortGroupName": outputFilterPortGroupName}
)
