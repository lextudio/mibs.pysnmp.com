# SNMP MIB module (MCAST-FILTER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MCAST-FILTER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:20:39 2024
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

(dlink_common_mgmt,) = mibBuilder.importSymbols(
    "DLINK-ID-REC-MIB",
    "dlink-common-mgmt")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

swMcastFilterMgmt = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 53)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class Ipv6Address(OctetString, TextualConvention):
    status = "current"
    displayHint = "2x:"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )



# MIB Managed Objects in the order of their OIDs

_SwMcastFilterProfileInfoTable_Object = MibTable
swMcastFilterProfileInfoTable = _SwMcastFilterProfileInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 53, 1)
)
if mibBuilder.loadTexts:
    swMcastFilterProfileInfoTable.setStatus("current")
_SwMcastFilterProfileInfoEntry_Object = MibTableRow
swMcastFilterProfileInfoEntry = _SwMcastFilterProfileInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 53, 1, 1)
)
swMcastFilterProfileInfoEntry.setIndexNames(
    (0, "MCAST-FILTER-MIB", "swMcastFilterProfileInfoIndex"),
)
if mibBuilder.loadTexts:
    swMcastFilterProfileInfoEntry.setStatus("current")


class _SwMcastFilterProfileInfoIndex_Type(Integer32):
    """Custom type swMcastFilterProfileInfoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SwMcastFilterProfileInfoIndex_Type.__name__ = "Integer32"
_SwMcastFilterProfileInfoIndex_Object = MibTableColumn
swMcastFilterProfileInfoIndex = _SwMcastFilterProfileInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 53, 1, 1, 1),
    _SwMcastFilterProfileInfoIndex_Type()
)
swMcastFilterProfileInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMcastFilterProfileInfoIndex.setStatus("current")


class _SwMcastFilterProfileInfoDescription_Type(DisplayString):
    """Custom type swMcastFilterProfileInfoDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SwMcastFilterProfileInfoDescription_Type.__name__ = "DisplayString"
_SwMcastFilterProfileInfoDescription_Object = MibTableColumn
swMcastFilterProfileInfoDescription = _SwMcastFilterProfileInfoDescription_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 53, 1, 1, 2),
    _SwMcastFilterProfileInfoDescription_Type()
)
swMcastFilterProfileInfoDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swMcastFilterProfileInfoDescription.setStatus("current")
_SwMcastFilterProfileInfoRowStatus_Type = RowStatus
_SwMcastFilterProfileInfoRowStatus_Object = MibTableColumn
swMcastFilterProfileInfoRowStatus = _SwMcastFilterProfileInfoRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 53, 1, 1, 3),
    _SwMcastFilterProfileInfoRowStatus_Type()
)
swMcastFilterProfileInfoRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swMcastFilterProfileInfoRowStatus.setStatus("current")
_SwMcastFilterProfileCtrlTable_Object = MibTable
swMcastFilterProfileCtrlTable = _SwMcastFilterProfileCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 53, 2)
)
if mibBuilder.loadTexts:
    swMcastFilterProfileCtrlTable.setStatus("current")
_SwMcastFilterProfileCtrlEntry_Object = MibTableRow
swMcastFilterProfileCtrlEntry = _SwMcastFilterProfileCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 53, 2, 1)
)
swMcastFilterProfileCtrlEntry.setIndexNames(
    (0, "MCAST-FILTER-MIB", "swMcastFilterProfileCtrlProfileIndex"),
    (0, "MCAST-FILTER-MIB", "swMcastFilterProfileCtrlStartAddress"),
    (0, "MCAST-FILTER-MIB", "swMcastFilterProfileCtrlEndAddress"),
)
if mibBuilder.loadTexts:
    swMcastFilterProfileCtrlEntry.setStatus("current")


class _SwMcastFilterProfileCtrlProfileIndex_Type(Integer32):
    """Custom type swMcastFilterProfileCtrlProfileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SwMcastFilterProfileCtrlProfileIndex_Type.__name__ = "Integer32"
_SwMcastFilterProfileCtrlProfileIndex_Object = MibTableColumn
swMcastFilterProfileCtrlProfileIndex = _SwMcastFilterProfileCtrlProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 53, 2, 1, 1),
    _SwMcastFilterProfileCtrlProfileIndex_Type()
)
swMcastFilterProfileCtrlProfileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMcastFilterProfileCtrlProfileIndex.setStatus("current")
_SwMcastFilterProfileCtrlStartAddress_Type = IpAddress
_SwMcastFilterProfileCtrlStartAddress_Object = MibTableColumn
swMcastFilterProfileCtrlStartAddress = _SwMcastFilterProfileCtrlStartAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 53, 2, 1, 2),
    _SwMcastFilterProfileCtrlStartAddress_Type()
)
swMcastFilterProfileCtrlStartAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMcastFilterProfileCtrlStartAddress.setStatus("current")
_SwMcastFilterProfileCtrlEndAddress_Type = IpAddress
_SwMcastFilterProfileCtrlEndAddress_Object = MibTableColumn
swMcastFilterProfileCtrlEndAddress = _SwMcastFilterProfileCtrlEndAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 53, 2, 1, 3),
    _SwMcastFilterProfileCtrlEndAddress_Type()
)
swMcastFilterProfileCtrlEndAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMcastFilterProfileCtrlEndAddress.setStatus("current")
_SwMcastFilterProfileCtrlRowStatus_Type = RowStatus
_SwMcastFilterProfileCtrlRowStatus_Object = MibTableColumn
swMcastFilterProfileCtrlRowStatus = _SwMcastFilterProfileCtrlRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 53, 2, 1, 4),
    _SwMcastFilterProfileCtrlRowStatus_Type()
)
swMcastFilterProfileCtrlRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swMcastFilterProfileCtrlRowStatus.setStatus("current")
_SwMcastFilterPortGroupTable_Object = MibTable
swMcastFilterPortGroupTable = _SwMcastFilterPortGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 53, 3)
)
if mibBuilder.loadTexts:
    swMcastFilterPortGroupTable.setStatus("current")
_SwMcastFilterPortGroupEntry_Object = MibTableRow
swMcastFilterPortGroupEntry = _SwMcastFilterPortGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 53, 3, 1)
)
swMcastFilterPortGroupEntry.setIndexNames(
    (0, "MCAST-FILTER-MIB", "swMcastFilterPortGroupPortIndex"),
    (0, "MCAST-FILTER-MIB", "swMcastFilterPortGroupProfileId"),
)
if mibBuilder.loadTexts:
    swMcastFilterPortGroupEntry.setStatus("current")


class _SwMcastFilterPortGroupPortIndex_Type(Integer32):
    """Custom type swMcastFilterPortGroupPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SwMcastFilterPortGroupPortIndex_Type.__name__ = "Integer32"
_SwMcastFilterPortGroupPortIndex_Object = MibTableColumn
swMcastFilterPortGroupPortIndex = _SwMcastFilterPortGroupPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 53, 3, 1, 1),
    _SwMcastFilterPortGroupPortIndex_Type()
)
swMcastFilterPortGroupPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMcastFilterPortGroupPortIndex.setStatus("current")


class _SwMcastFilterPortGroupProfileId_Type(Integer32):
    """Custom type swMcastFilterPortGroupProfileId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SwMcastFilterPortGroupProfileId_Type.__name__ = "Integer32"
_SwMcastFilterPortGroupProfileId_Object = MibTableColumn
swMcastFilterPortGroupProfileId = _SwMcastFilterPortGroupProfileId_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 53, 3, 1, 2),
    _SwMcastFilterPortGroupProfileId_Type()
)
swMcastFilterPortGroupProfileId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMcastFilterPortGroupProfileId.setStatus("current")
_SwMcastFilterPortGroupRowStatus_Type = RowStatus
_SwMcastFilterPortGroupRowStatus_Object = MibTableColumn
swMcastFilterPortGroupRowStatus = _SwMcastFilterPortGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 53, 3, 1, 3),
    _SwMcastFilterPortGroupRowStatus_Type()
)
swMcastFilterPortGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swMcastFilterPortGroupRowStatus.setStatus("current")
_SwMcastFilterPortAccessTable_Object = MibTable
swMcastFilterPortAccessTable = _SwMcastFilterPortAccessTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 53, 4)
)
if mibBuilder.loadTexts:
    swMcastFilterPortAccessTable.setStatus("current")
_SwMcastFilterPortAccessEntry_Object = MibTableRow
swMcastFilterPortAccessEntry = _SwMcastFilterPortAccessEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 53, 4, 1)
)
swMcastFilterPortAccessEntry.setIndexNames(
    (0, "MCAST-FILTER-MIB", "swMcastFilterPortAccessPortIndex"),
)
if mibBuilder.loadTexts:
    swMcastFilterPortAccessEntry.setStatus("current")


class _SwMcastFilterPortAccessPortIndex_Type(Integer32):
    """Custom type swMcastFilterPortAccessPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SwMcastFilterPortAccessPortIndex_Type.__name__ = "Integer32"
_SwMcastFilterPortAccessPortIndex_Object = MibTableColumn
swMcastFilterPortAccessPortIndex = _SwMcastFilterPortAccessPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 53, 4, 1, 1),
    _SwMcastFilterPortAccessPortIndex_Type()
)
swMcastFilterPortAccessPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMcastFilterPortAccessPortIndex.setStatus("current")


class _SwMcastFilterPortAccessState_Type(Integer32):
    """Custom type swMcastFilterPortAccessState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 2),
          ("permit", 1))
    )


_SwMcastFilterPortAccessState_Type.__name__ = "Integer32"
_SwMcastFilterPortAccessState_Object = MibTableColumn
swMcastFilterPortAccessState = _SwMcastFilterPortAccessState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 53, 4, 1, 2),
    _SwMcastFilterPortAccessState_Type()
)
swMcastFilterPortAccessState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swMcastFilterPortAccessState.setStatus("current")
_SwMcastFilterPortMaxGroupTable_Object = MibTable
swMcastFilterPortMaxGroupTable = _SwMcastFilterPortMaxGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 53, 5)
)
if mibBuilder.loadTexts:
    swMcastFilterPortMaxGroupTable.setStatus("current")
_SwMcastFilterPortMaxGroupEntry_Object = MibTableRow
swMcastFilterPortMaxGroupEntry = _SwMcastFilterPortMaxGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 53, 5, 1)
)
swMcastFilterPortMaxGroupEntry.setIndexNames(
    (0, "MCAST-FILTER-MIB", "swMcastFilterPortMaxGroupPortIndex"),
)
if mibBuilder.loadTexts:
    swMcastFilterPortMaxGroupEntry.setStatus("current")


class _SwMcastFilterPortMaxGroupPortIndex_Type(Integer32):
    """Custom type swMcastFilterPortMaxGroupPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SwMcastFilterPortMaxGroupPortIndex_Type.__name__ = "Integer32"
_SwMcastFilterPortMaxGroupPortIndex_Object = MibTableColumn
swMcastFilterPortMaxGroupPortIndex = _SwMcastFilterPortMaxGroupPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 53, 5, 1, 1),
    _SwMcastFilterPortMaxGroupPortIndex_Type()
)
swMcastFilterPortMaxGroupPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMcastFilterPortMaxGroupPortIndex.setStatus("current")
_SwMcastFilterPortMaxGroup_Type = Integer32
_SwMcastFilterPortMaxGroup_Object = MibTableColumn
swMcastFilterPortMaxGroup = _SwMcastFilterPortMaxGroup_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 53, 5, 1, 2),
    _SwMcastFilterPortMaxGroup_Type()
)
swMcastFilterPortMaxGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swMcastFilterPortMaxGroup.setStatus("current")


class _SwMcastFilterPortCurrentCount_Type(Integer32):
    """Custom type swMcastFilterPortCurrentCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwMcastFilterPortCurrentCount_Type.__name__ = "Integer32"
_SwMcastFilterPortCurrentCount_Object = MibTableColumn
swMcastFilterPortCurrentCount = _SwMcastFilterPortCurrentCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 53, 5, 1, 3),
    _SwMcastFilterPortCurrentCount_Type()
)
swMcastFilterPortCurrentCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMcastFilterPortCurrentCount.setStatus("current")


class _SwMcastFilterPortMaxGroupAction_Type(Integer32):
    """Custom type swMcastFilterPortMaxGroupAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("drop", 1),
          ("replace", 2))
    )


_SwMcastFilterPortMaxGroupAction_Type.__name__ = "Integer32"
_SwMcastFilterPortMaxGroupAction_Object = MibTableColumn
swMcastFilterPortMaxGroupAction = _SwMcastFilterPortMaxGroupAction_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 53, 5, 1, 4),
    _SwMcastFilterPortMaxGroupAction_Type()
)
swMcastFilterPortMaxGroupAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swMcastFilterPortMaxGroupAction.setStatus("current")
_SwMcastFilterVLANGroupTable_Object = MibTable
swMcastFilterVLANGroupTable = _SwMcastFilterVLANGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 53, 6)
)
if mibBuilder.loadTexts:
    swMcastFilterVLANGroupTable.setStatus("current")
_SwMcastFilterVLANGroupEntry_Object = MibTableRow
swMcastFilterVLANGroupEntry = _SwMcastFilterVLANGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 53, 6, 1)
)
swMcastFilterVLANGroupEntry.setIndexNames(
    (0, "MCAST-FILTER-MIB", "swMcastFilterVLANGroupVLANIndex"),
    (0, "MCAST-FILTER-MIB", "swMcastFilterVLANGroupProfileId"),
)
if mibBuilder.loadTexts:
    swMcastFilterVLANGroupEntry.setStatus("current")


class _SwMcastFilterVLANGroupVLANIndex_Type(Integer32):
    """Custom type swMcastFilterVLANGroupVLANIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SwMcastFilterVLANGroupVLANIndex_Type.__name__ = "Integer32"
_SwMcastFilterVLANGroupVLANIndex_Object = MibTableColumn
swMcastFilterVLANGroupVLANIndex = _SwMcastFilterVLANGroupVLANIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 53, 6, 1, 1),
    _SwMcastFilterVLANGroupVLANIndex_Type()
)
swMcastFilterVLANGroupVLANIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMcastFilterVLANGroupVLANIndex.setStatus("current")


class _SwMcastFilterVLANGroupProfileId_Type(Integer32):
    """Custom type swMcastFilterVLANGroupProfileId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SwMcastFilterVLANGroupProfileId_Type.__name__ = "Integer32"
_SwMcastFilterVLANGroupProfileId_Object = MibTableColumn
swMcastFilterVLANGroupProfileId = _SwMcastFilterVLANGroupProfileId_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 53, 6, 1, 2),
    _SwMcastFilterVLANGroupProfileId_Type()
)
swMcastFilterVLANGroupProfileId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMcastFilterVLANGroupProfileId.setStatus("current")
_SwMcastFilterVLANGroupRowStatus_Type = RowStatus
_SwMcastFilterVLANGroupRowStatus_Object = MibTableColumn
swMcastFilterVLANGroupRowStatus = _SwMcastFilterVLANGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 53, 6, 1, 3),
    _SwMcastFilterVLANGroupRowStatus_Type()
)
swMcastFilterVLANGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swMcastFilterVLANGroupRowStatus.setStatus("current")
_SwMcastFilterVLANAccessTable_Object = MibTable
swMcastFilterVLANAccessTable = _SwMcastFilterVLANAccessTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 53, 7)
)
if mibBuilder.loadTexts:
    swMcastFilterVLANAccessTable.setStatus("current")
_SwMcastFilterVLANAccessEntry_Object = MibTableRow
swMcastFilterVLANAccessEntry = _SwMcastFilterVLANAccessEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 53, 7, 1)
)
swMcastFilterVLANAccessEntry.setIndexNames(
    (0, "MCAST-FILTER-MIB", "swMcastFilterVLANAccessVLANIndex"),
)
if mibBuilder.loadTexts:
    swMcastFilterVLANAccessEntry.setStatus("current")


class _SwMcastFilterVLANAccessVLANIndex_Type(Integer32):
    """Custom type swMcastFilterVLANAccessVLANIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SwMcastFilterVLANAccessVLANIndex_Type.__name__ = "Integer32"
_SwMcastFilterVLANAccessVLANIndex_Object = MibTableColumn
swMcastFilterVLANAccessVLANIndex = _SwMcastFilterVLANAccessVLANIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 53, 7, 1, 1),
    _SwMcastFilterVLANAccessVLANIndex_Type()
)
swMcastFilterVLANAccessVLANIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMcastFilterVLANAccessVLANIndex.setStatus("current")


class _SwMcastFilterVLANAccessState_Type(Integer32):
    """Custom type swMcastFilterVLANAccessState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 2),
          ("permit", 1))
    )


_SwMcastFilterVLANAccessState_Type.__name__ = "Integer32"
_SwMcastFilterVLANAccessState_Object = MibTableColumn
swMcastFilterVLANAccessState = _SwMcastFilterVLANAccessState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 53, 7, 1, 2),
    _SwMcastFilterVLANAccessState_Type()
)
swMcastFilterVLANAccessState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swMcastFilterVLANAccessState.setStatus("current")
_SwMcastFilterVLANMaxGroupTable_Object = MibTable
swMcastFilterVLANMaxGroupTable = _SwMcastFilterVLANMaxGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 53, 8)
)
if mibBuilder.loadTexts:
    swMcastFilterVLANMaxGroupTable.setStatus("current")
_SwMcastFilterVLANMaxGroupEntry_Object = MibTableRow
swMcastFilterVLANMaxGroupEntry = _SwMcastFilterVLANMaxGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 53, 8, 1)
)
swMcastFilterVLANMaxGroupEntry.setIndexNames(
    (0, "MCAST-FILTER-MIB", "swMcastFilterVLANMaxGroupVLANIndex"),
)
if mibBuilder.loadTexts:
    swMcastFilterVLANMaxGroupEntry.setStatus("current")


class _SwMcastFilterVLANMaxGroupVLANIndex_Type(Integer32):
    """Custom type swMcastFilterVLANMaxGroupVLANIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SwMcastFilterVLANMaxGroupVLANIndex_Type.__name__ = "Integer32"
_SwMcastFilterVLANMaxGroupVLANIndex_Object = MibTableColumn
swMcastFilterVLANMaxGroupVLANIndex = _SwMcastFilterVLANMaxGroupVLANIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 53, 8, 1, 1),
    _SwMcastFilterVLANMaxGroupVLANIndex_Type()
)
swMcastFilterVLANMaxGroupVLANIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMcastFilterVLANMaxGroupVLANIndex.setStatus("current")
_SwMcastFilterVLANMaxGroup_Type = Integer32
_SwMcastFilterVLANMaxGroup_Object = MibTableColumn
swMcastFilterVLANMaxGroup = _SwMcastFilterVLANMaxGroup_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 53, 8, 1, 2),
    _SwMcastFilterVLANMaxGroup_Type()
)
swMcastFilterVLANMaxGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swMcastFilterVLANMaxGroup.setStatus("current")


class _SwMcastFilterVLANCurrentCount_Type(Integer32):
    """Custom type swMcastFilterVLANCurrentCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwMcastFilterVLANCurrentCount_Type.__name__ = "Integer32"
_SwMcastFilterVLANCurrentCount_Object = MibTableColumn
swMcastFilterVLANCurrentCount = _SwMcastFilterVLANCurrentCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 53, 8, 1, 3),
    _SwMcastFilterVLANCurrentCount_Type()
)
swMcastFilterVLANCurrentCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMcastFilterVLANCurrentCount.setStatus("current")


class _SwMcastFilterVLANMaxGroupAction_Type(Integer32):
    """Custom type swMcastFilterVLANMaxGroupAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("drop", 1),
          ("replace", 2))
    )


_SwMcastFilterVLANMaxGroupAction_Type.__name__ = "Integer32"
_SwMcastFilterVLANMaxGroupAction_Object = MibTableColumn
swMcastFilterVLANMaxGroupAction = _SwMcastFilterVLANMaxGroupAction_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 53, 8, 1, 4),
    _SwMcastFilterVLANMaxGroupAction_Type()
)
swMcastFilterVLANMaxGroupAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swMcastFilterVLANMaxGroupAction.setStatus("current")
_SwMcastFilterIpv6ProfileInfoTable_Object = MibTable
swMcastFilterIpv6ProfileInfoTable = _SwMcastFilterIpv6ProfileInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 53, 20)
)
if mibBuilder.loadTexts:
    swMcastFilterIpv6ProfileInfoTable.setStatus("current")
_SwMcastFilterIpv6ProfileInfoEntry_Object = MibTableRow
swMcastFilterIpv6ProfileInfoEntry = _SwMcastFilterIpv6ProfileInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 53, 20, 1)
)
swMcastFilterIpv6ProfileInfoEntry.setIndexNames(
    (0, "MCAST-FILTER-MIB", "swMcastFilterIpv6ProfileInfoIndex"),
)
if mibBuilder.loadTexts:
    swMcastFilterIpv6ProfileInfoEntry.setStatus("current")


class _SwMcastFilterIpv6ProfileInfoIndex_Type(Integer32):
    """Custom type swMcastFilterIpv6ProfileInfoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SwMcastFilterIpv6ProfileInfoIndex_Type.__name__ = "Integer32"
_SwMcastFilterIpv6ProfileInfoIndex_Object = MibTableColumn
swMcastFilterIpv6ProfileInfoIndex = _SwMcastFilterIpv6ProfileInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 53, 20, 1, 1),
    _SwMcastFilterIpv6ProfileInfoIndex_Type()
)
swMcastFilterIpv6ProfileInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMcastFilterIpv6ProfileInfoIndex.setStatus("current")


class _SwMcastFilterIpv6ProfileInfoDescription_Type(DisplayString):
    """Custom type swMcastFilterIpv6ProfileInfoDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SwMcastFilterIpv6ProfileInfoDescription_Type.__name__ = "DisplayString"
_SwMcastFilterIpv6ProfileInfoDescription_Object = MibTableColumn
swMcastFilterIpv6ProfileInfoDescription = _SwMcastFilterIpv6ProfileInfoDescription_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 53, 20, 1, 2),
    _SwMcastFilterIpv6ProfileInfoDescription_Type()
)
swMcastFilterIpv6ProfileInfoDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swMcastFilterIpv6ProfileInfoDescription.setStatus("current")
_SwMcastFilterIpv6ProfileInfoRowStatus_Type = RowStatus
_SwMcastFilterIpv6ProfileInfoRowStatus_Object = MibTableColumn
swMcastFilterIpv6ProfileInfoRowStatus = _SwMcastFilterIpv6ProfileInfoRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 53, 20, 1, 3),
    _SwMcastFilterIpv6ProfileInfoRowStatus_Type()
)
swMcastFilterIpv6ProfileInfoRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swMcastFilterIpv6ProfileInfoRowStatus.setStatus("current")
_SwMcastFilterIpv6ProfileCtrlTable_Object = MibTable
swMcastFilterIpv6ProfileCtrlTable = _SwMcastFilterIpv6ProfileCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 53, 21)
)
if mibBuilder.loadTexts:
    swMcastFilterIpv6ProfileCtrlTable.setStatus("current")
_SwMcastFilterIpv6ProfileCtrlEntry_Object = MibTableRow
swMcastFilterIpv6ProfileCtrlEntry = _SwMcastFilterIpv6ProfileCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 53, 21, 1)
)
swMcastFilterIpv6ProfileCtrlEntry.setIndexNames(
    (0, "MCAST-FILTER-MIB", "swMcastFilterIpv6ProfileCtrlProfileIndex"),
    (0, "MCAST-FILTER-MIB", "swMcastFilterIpv6ProfileCtrlStartAddress"),
    (0, "MCAST-FILTER-MIB", "swMcastFilterIpv6ProfileCtrlEndAddress"),
)
if mibBuilder.loadTexts:
    swMcastFilterIpv6ProfileCtrlEntry.setStatus("current")


class _SwMcastFilterIpv6ProfileCtrlProfileIndex_Type(Integer32):
    """Custom type swMcastFilterIpv6ProfileCtrlProfileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SwMcastFilterIpv6ProfileCtrlProfileIndex_Type.__name__ = "Integer32"
_SwMcastFilterIpv6ProfileCtrlProfileIndex_Object = MibTableColumn
swMcastFilterIpv6ProfileCtrlProfileIndex = _SwMcastFilterIpv6ProfileCtrlProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 53, 21, 1, 1),
    _SwMcastFilterIpv6ProfileCtrlProfileIndex_Type()
)
swMcastFilterIpv6ProfileCtrlProfileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMcastFilterIpv6ProfileCtrlProfileIndex.setStatus("current")
_SwMcastFilterIpv6ProfileCtrlStartAddress_Type = Ipv6Address
_SwMcastFilterIpv6ProfileCtrlStartAddress_Object = MibTableColumn
swMcastFilterIpv6ProfileCtrlStartAddress = _SwMcastFilterIpv6ProfileCtrlStartAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 53, 21, 1, 2),
    _SwMcastFilterIpv6ProfileCtrlStartAddress_Type()
)
swMcastFilterIpv6ProfileCtrlStartAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMcastFilterIpv6ProfileCtrlStartAddress.setStatus("current")
_SwMcastFilterIpv6ProfileCtrlEndAddress_Type = Ipv6Address
_SwMcastFilterIpv6ProfileCtrlEndAddress_Object = MibTableColumn
swMcastFilterIpv6ProfileCtrlEndAddress = _SwMcastFilterIpv6ProfileCtrlEndAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 53, 21, 1, 3),
    _SwMcastFilterIpv6ProfileCtrlEndAddress_Type()
)
swMcastFilterIpv6ProfileCtrlEndAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMcastFilterIpv6ProfileCtrlEndAddress.setStatus("current")
_SwMcastFilterIpv6ProfileCtrlRowStatus_Type = RowStatus
_SwMcastFilterIpv6ProfileCtrlRowStatus_Object = MibTableColumn
swMcastFilterIpv6ProfileCtrlRowStatus = _SwMcastFilterIpv6ProfileCtrlRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 53, 21, 1, 4),
    _SwMcastFilterIpv6ProfileCtrlRowStatus_Type()
)
swMcastFilterIpv6ProfileCtrlRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swMcastFilterIpv6ProfileCtrlRowStatus.setStatus("current")
_SwMcastFilterIpv6PortGroupTable_Object = MibTable
swMcastFilterIpv6PortGroupTable = _SwMcastFilterIpv6PortGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 53, 22)
)
if mibBuilder.loadTexts:
    swMcastFilterIpv6PortGroupTable.setStatus("current")
_SwMcastFilterIpv6PortGroupEntry_Object = MibTableRow
swMcastFilterIpv6PortGroupEntry = _SwMcastFilterIpv6PortGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 53, 22, 1)
)
swMcastFilterIpv6PortGroupEntry.setIndexNames(
    (0, "MCAST-FILTER-MIB", "swMcastFilterIpv6PortGroupPortIndex"),
    (0, "MCAST-FILTER-MIB", "swMcastFilterIpv6PortGroupProfileId"),
)
if mibBuilder.loadTexts:
    swMcastFilterIpv6PortGroupEntry.setStatus("current")


class _SwMcastFilterIpv6PortGroupPortIndex_Type(Integer32):
    """Custom type swMcastFilterIpv6PortGroupPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SwMcastFilterIpv6PortGroupPortIndex_Type.__name__ = "Integer32"
_SwMcastFilterIpv6PortGroupPortIndex_Object = MibTableColumn
swMcastFilterIpv6PortGroupPortIndex = _SwMcastFilterIpv6PortGroupPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 53, 22, 1, 1),
    _SwMcastFilterIpv6PortGroupPortIndex_Type()
)
swMcastFilterIpv6PortGroupPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMcastFilterIpv6PortGroupPortIndex.setStatus("current")


class _SwMcastFilterIpv6PortGroupProfileId_Type(Integer32):
    """Custom type swMcastFilterIpv6PortGroupProfileId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SwMcastFilterIpv6PortGroupProfileId_Type.__name__ = "Integer32"
_SwMcastFilterIpv6PortGroupProfileId_Object = MibTableColumn
swMcastFilterIpv6PortGroupProfileId = _SwMcastFilterIpv6PortGroupProfileId_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 53, 22, 1, 2),
    _SwMcastFilterIpv6PortGroupProfileId_Type()
)
swMcastFilterIpv6PortGroupProfileId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMcastFilterIpv6PortGroupProfileId.setStatus("current")
_SwMcastFilterIpv6PortGroupRowStatus_Type = RowStatus
_SwMcastFilterIpv6PortGroupRowStatus_Object = MibTableColumn
swMcastFilterIpv6PortGroupRowStatus = _SwMcastFilterIpv6PortGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 53, 22, 1, 3),
    _SwMcastFilterIpv6PortGroupRowStatus_Type()
)
swMcastFilterIpv6PortGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swMcastFilterIpv6PortGroupRowStatus.setStatus("current")
_SwMcastFilterIpv6PortAccessTable_Object = MibTable
swMcastFilterIpv6PortAccessTable = _SwMcastFilterIpv6PortAccessTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 53, 23)
)
if mibBuilder.loadTexts:
    swMcastFilterIpv6PortAccessTable.setStatus("current")
_SwMcastFilterIpv6PortAccessEntry_Object = MibTableRow
swMcastFilterIpv6PortAccessEntry = _SwMcastFilterIpv6PortAccessEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 53, 23, 1)
)
swMcastFilterIpv6PortAccessEntry.setIndexNames(
    (0, "MCAST-FILTER-MIB", "swMcastFilterIpv6PortAccessPortIndex"),
)
if mibBuilder.loadTexts:
    swMcastFilterIpv6PortAccessEntry.setStatus("current")


class _SwMcastFilterIpv6PortAccessPortIndex_Type(Integer32):
    """Custom type swMcastFilterIpv6PortAccessPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SwMcastFilterIpv6PortAccessPortIndex_Type.__name__ = "Integer32"
_SwMcastFilterIpv6PortAccessPortIndex_Object = MibTableColumn
swMcastFilterIpv6PortAccessPortIndex = _SwMcastFilterIpv6PortAccessPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 53, 23, 1, 1),
    _SwMcastFilterIpv6PortAccessPortIndex_Type()
)
swMcastFilterIpv6PortAccessPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMcastFilterIpv6PortAccessPortIndex.setStatus("current")


class _SwMcastFilterIpv6PortAccessState_Type(Integer32):
    """Custom type swMcastFilterIpv6PortAccessState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 2),
          ("permit", 1))
    )


_SwMcastFilterIpv6PortAccessState_Type.__name__ = "Integer32"
_SwMcastFilterIpv6PortAccessState_Object = MibTableColumn
swMcastFilterIpv6PortAccessState = _SwMcastFilterIpv6PortAccessState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 53, 23, 1, 2),
    _SwMcastFilterIpv6PortAccessState_Type()
)
swMcastFilterIpv6PortAccessState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swMcastFilterIpv6PortAccessState.setStatus("current")
_SwMcastFilterIpv6PortMaxGroupTable_Object = MibTable
swMcastFilterIpv6PortMaxGroupTable = _SwMcastFilterIpv6PortMaxGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 53, 24)
)
if mibBuilder.loadTexts:
    swMcastFilterIpv6PortMaxGroupTable.setStatus("current")
_SwMcastFilterIpv6PortMaxGroupEntry_Object = MibTableRow
swMcastFilterIpv6PortMaxGroupEntry = _SwMcastFilterIpv6PortMaxGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 53, 24, 1)
)
swMcastFilterIpv6PortMaxGroupEntry.setIndexNames(
    (0, "MCAST-FILTER-MIB", "swMcastFilterIpv6PortMaxGroupPortIndex"),
)
if mibBuilder.loadTexts:
    swMcastFilterIpv6PortMaxGroupEntry.setStatus("current")


class _SwMcastFilterIpv6PortMaxGroupPortIndex_Type(Integer32):
    """Custom type swMcastFilterIpv6PortMaxGroupPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SwMcastFilterIpv6PortMaxGroupPortIndex_Type.__name__ = "Integer32"
_SwMcastFilterIpv6PortMaxGroupPortIndex_Object = MibTableColumn
swMcastFilterIpv6PortMaxGroupPortIndex = _SwMcastFilterIpv6PortMaxGroupPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 53, 24, 1, 1),
    _SwMcastFilterIpv6PortMaxGroupPortIndex_Type()
)
swMcastFilterIpv6PortMaxGroupPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMcastFilterIpv6PortMaxGroupPortIndex.setStatus("current")
_SwMcastFilterIpv6PortMaxGroup_Type = Integer32
_SwMcastFilterIpv6PortMaxGroup_Object = MibTableColumn
swMcastFilterIpv6PortMaxGroup = _SwMcastFilterIpv6PortMaxGroup_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 53, 24, 1, 2),
    _SwMcastFilterIpv6PortMaxGroup_Type()
)
swMcastFilterIpv6PortMaxGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swMcastFilterIpv6PortMaxGroup.setStatus("current")


class _SwMcastFilterIpv6PortCurrentCount_Type(Integer32):
    """Custom type swMcastFilterIpv6PortCurrentCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwMcastFilterIpv6PortCurrentCount_Type.__name__ = "Integer32"
_SwMcastFilterIpv6PortCurrentCount_Object = MibTableColumn
swMcastFilterIpv6PortCurrentCount = _SwMcastFilterIpv6PortCurrentCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 53, 24, 1, 3),
    _SwMcastFilterIpv6PortCurrentCount_Type()
)
swMcastFilterIpv6PortCurrentCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMcastFilterIpv6PortCurrentCount.setStatus("current")


class _SwMcastFilterIpv6PortMaxGroupAction_Type(Integer32):
    """Custom type swMcastFilterIpv6PortMaxGroupAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("drop", 1),
          ("replace", 2))
    )


_SwMcastFilterIpv6PortMaxGroupAction_Type.__name__ = "Integer32"
_SwMcastFilterIpv6PortMaxGroupAction_Object = MibTableColumn
swMcastFilterIpv6PortMaxGroupAction = _SwMcastFilterIpv6PortMaxGroupAction_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 53, 24, 1, 4),
    _SwMcastFilterIpv6PortMaxGroupAction_Type()
)
swMcastFilterIpv6PortMaxGroupAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swMcastFilterIpv6PortMaxGroupAction.setStatus("current")
_SwMcastFilterIpv6VLANGroupTable_Object = MibTable
swMcastFilterIpv6VLANGroupTable = _SwMcastFilterIpv6VLANGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 53, 25)
)
if mibBuilder.loadTexts:
    swMcastFilterIpv6VLANGroupTable.setStatus("current")
_SwMcastFilterIpv6VLANGroupEntry_Object = MibTableRow
swMcastFilterIpv6VLANGroupEntry = _SwMcastFilterIpv6VLANGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 53, 25, 1)
)
swMcastFilterIpv6VLANGroupEntry.setIndexNames(
    (0, "MCAST-FILTER-MIB", "swMcastFilterIpv6VLANGroupVLANIndex"),
    (0, "MCAST-FILTER-MIB", "swMcastFilterIpv6VLANGroupProfileId"),
)
if mibBuilder.loadTexts:
    swMcastFilterIpv6VLANGroupEntry.setStatus("current")


class _SwMcastFilterIpv6VLANGroupVLANIndex_Type(Integer32):
    """Custom type swMcastFilterIpv6VLANGroupVLANIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SwMcastFilterIpv6VLANGroupVLANIndex_Type.__name__ = "Integer32"
_SwMcastFilterIpv6VLANGroupVLANIndex_Object = MibTableColumn
swMcastFilterIpv6VLANGroupVLANIndex = _SwMcastFilterIpv6VLANGroupVLANIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 53, 25, 1, 1),
    _SwMcastFilterIpv6VLANGroupVLANIndex_Type()
)
swMcastFilterIpv6VLANGroupVLANIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMcastFilterIpv6VLANGroupVLANIndex.setStatus("current")


class _SwMcastFilterIpv6VLANGroupProfileId_Type(Integer32):
    """Custom type swMcastFilterIpv6VLANGroupProfileId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SwMcastFilterIpv6VLANGroupProfileId_Type.__name__ = "Integer32"
_SwMcastFilterIpv6VLANGroupProfileId_Object = MibTableColumn
swMcastFilterIpv6VLANGroupProfileId = _SwMcastFilterIpv6VLANGroupProfileId_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 53, 25, 1, 2),
    _SwMcastFilterIpv6VLANGroupProfileId_Type()
)
swMcastFilterIpv6VLANGroupProfileId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMcastFilterIpv6VLANGroupProfileId.setStatus("current")
_SwMcastFilterIpv6VLANGroupRowStatus_Type = RowStatus
_SwMcastFilterIpv6VLANGroupRowStatus_Object = MibTableColumn
swMcastFilterIpv6VLANGroupRowStatus = _SwMcastFilterIpv6VLANGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 53, 25, 1, 3),
    _SwMcastFilterIpv6VLANGroupRowStatus_Type()
)
swMcastFilterIpv6VLANGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swMcastFilterIpv6VLANGroupRowStatus.setStatus("current")
_SwMcastFilterIpv6VLANAccessTable_Object = MibTable
swMcastFilterIpv6VLANAccessTable = _SwMcastFilterIpv6VLANAccessTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 53, 26)
)
if mibBuilder.loadTexts:
    swMcastFilterIpv6VLANAccessTable.setStatus("current")
_SwMcastFilterIpv6VLANAccessEntry_Object = MibTableRow
swMcastFilterIpv6VLANAccessEntry = _SwMcastFilterIpv6VLANAccessEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 53, 26, 1)
)
swMcastFilterIpv6VLANAccessEntry.setIndexNames(
    (0, "MCAST-FILTER-MIB", "swMcastFilterIpv6VLANAccessVLANIndex"),
)
if mibBuilder.loadTexts:
    swMcastFilterIpv6VLANAccessEntry.setStatus("current")


class _SwMcastFilterIpv6VLANAccessVLANIndex_Type(Integer32):
    """Custom type swMcastFilterIpv6VLANAccessVLANIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SwMcastFilterIpv6VLANAccessVLANIndex_Type.__name__ = "Integer32"
_SwMcastFilterIpv6VLANAccessVLANIndex_Object = MibTableColumn
swMcastFilterIpv6VLANAccessVLANIndex = _SwMcastFilterIpv6VLANAccessVLANIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 53, 26, 1, 1),
    _SwMcastFilterIpv6VLANAccessVLANIndex_Type()
)
swMcastFilterIpv6VLANAccessVLANIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMcastFilterIpv6VLANAccessVLANIndex.setStatus("current")


class _SwMcastFilterIpv6VLANAccessState_Type(Integer32):
    """Custom type swMcastFilterIpv6VLANAccessState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 2),
          ("permit", 1))
    )


_SwMcastFilterIpv6VLANAccessState_Type.__name__ = "Integer32"
_SwMcastFilterIpv6VLANAccessState_Object = MibTableColumn
swMcastFilterIpv6VLANAccessState = _SwMcastFilterIpv6VLANAccessState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 53, 26, 1, 2),
    _SwMcastFilterIpv6VLANAccessState_Type()
)
swMcastFilterIpv6VLANAccessState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swMcastFilterIpv6VLANAccessState.setStatus("current")
_SwMcastFilterIpv6VLANMaxGroupTable_Object = MibTable
swMcastFilterIpv6VLANMaxGroupTable = _SwMcastFilterIpv6VLANMaxGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 53, 27)
)
if mibBuilder.loadTexts:
    swMcastFilterIpv6VLANMaxGroupTable.setStatus("current")
_SwMcastFilterIpv6VLANMaxGroupEntry_Object = MibTableRow
swMcastFilterIpv6VLANMaxGroupEntry = _SwMcastFilterIpv6VLANMaxGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 53, 27, 1)
)
swMcastFilterIpv6VLANMaxGroupEntry.setIndexNames(
    (0, "MCAST-FILTER-MIB", "swMcastFilterIpv6VLANMaxGroupVLANIndex"),
)
if mibBuilder.loadTexts:
    swMcastFilterIpv6VLANMaxGroupEntry.setStatus("current")


class _SwMcastFilterIpv6VLANMaxGroupVLANIndex_Type(Integer32):
    """Custom type swMcastFilterIpv6VLANMaxGroupVLANIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SwMcastFilterIpv6VLANMaxGroupVLANIndex_Type.__name__ = "Integer32"
_SwMcastFilterIpv6VLANMaxGroupVLANIndex_Object = MibTableColumn
swMcastFilterIpv6VLANMaxGroupVLANIndex = _SwMcastFilterIpv6VLANMaxGroupVLANIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 53, 27, 1, 1),
    _SwMcastFilterIpv6VLANMaxGroupVLANIndex_Type()
)
swMcastFilterIpv6VLANMaxGroupVLANIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMcastFilterIpv6VLANMaxGroupVLANIndex.setStatus("current")
_SwMcastFilterIpv6VLANMaxGroup_Type = Integer32
_SwMcastFilterIpv6VLANMaxGroup_Object = MibTableColumn
swMcastFilterIpv6VLANMaxGroup = _SwMcastFilterIpv6VLANMaxGroup_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 53, 27, 1, 2),
    _SwMcastFilterIpv6VLANMaxGroup_Type()
)
swMcastFilterIpv6VLANMaxGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swMcastFilterIpv6VLANMaxGroup.setStatus("current")


class _SwMcastFilterIpv6VLANCurrentCount_Type(Integer32):
    """Custom type swMcastFilterIpv6VLANCurrentCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwMcastFilterIpv6VLANCurrentCount_Type.__name__ = "Integer32"
_SwMcastFilterIpv6VLANCurrentCount_Object = MibTableColumn
swMcastFilterIpv6VLANCurrentCount = _SwMcastFilterIpv6VLANCurrentCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 53, 27, 1, 3),
    _SwMcastFilterIpv6VLANCurrentCount_Type()
)
swMcastFilterIpv6VLANCurrentCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMcastFilterIpv6VLANCurrentCount.setStatus("current")


class _SwMcastFilterIpv6VLANMaxGroupAction_Type(Integer32):
    """Custom type swMcastFilterIpv6VLANMaxGroupAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("drop", 1),
          ("replace", 2))
    )


_SwMcastFilterIpv6VLANMaxGroupAction_Type.__name__ = "Integer32"
_SwMcastFilterIpv6VLANMaxGroupAction_Object = MibTableColumn
swMcastFilterIpv6VLANMaxGroupAction = _SwMcastFilterIpv6VLANMaxGroupAction_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 53, 27, 1, 4),
    _SwMcastFilterIpv6VLANMaxGroupAction_Type()
)
swMcastFilterIpv6VLANMaxGroupAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swMcastFilterIpv6VLANMaxGroupAction.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MCAST-FILTER-MIB",
    **{"Ipv6Address": Ipv6Address,
       "swMcastFilterMgmt": swMcastFilterMgmt,
       "swMcastFilterProfileInfoTable": swMcastFilterProfileInfoTable,
       "swMcastFilterProfileInfoEntry": swMcastFilterProfileInfoEntry,
       "swMcastFilterProfileInfoIndex": swMcastFilterProfileInfoIndex,
       "swMcastFilterProfileInfoDescription": swMcastFilterProfileInfoDescription,
       "swMcastFilterProfileInfoRowStatus": swMcastFilterProfileInfoRowStatus,
       "swMcastFilterProfileCtrlTable": swMcastFilterProfileCtrlTable,
       "swMcastFilterProfileCtrlEntry": swMcastFilterProfileCtrlEntry,
       "swMcastFilterProfileCtrlProfileIndex": swMcastFilterProfileCtrlProfileIndex,
       "swMcastFilterProfileCtrlStartAddress": swMcastFilterProfileCtrlStartAddress,
       "swMcastFilterProfileCtrlEndAddress": swMcastFilterProfileCtrlEndAddress,
       "swMcastFilterProfileCtrlRowStatus": swMcastFilterProfileCtrlRowStatus,
       "swMcastFilterPortGroupTable": swMcastFilterPortGroupTable,
       "swMcastFilterPortGroupEntry": swMcastFilterPortGroupEntry,
       "swMcastFilterPortGroupPortIndex": swMcastFilterPortGroupPortIndex,
       "swMcastFilterPortGroupProfileId": swMcastFilterPortGroupProfileId,
       "swMcastFilterPortGroupRowStatus": swMcastFilterPortGroupRowStatus,
       "swMcastFilterPortAccessTable": swMcastFilterPortAccessTable,
       "swMcastFilterPortAccessEntry": swMcastFilterPortAccessEntry,
       "swMcastFilterPortAccessPortIndex": swMcastFilterPortAccessPortIndex,
       "swMcastFilterPortAccessState": swMcastFilterPortAccessState,
       "swMcastFilterPortMaxGroupTable": swMcastFilterPortMaxGroupTable,
       "swMcastFilterPortMaxGroupEntry": swMcastFilterPortMaxGroupEntry,
       "swMcastFilterPortMaxGroupPortIndex": swMcastFilterPortMaxGroupPortIndex,
       "swMcastFilterPortMaxGroup": swMcastFilterPortMaxGroup,
       "swMcastFilterPortCurrentCount": swMcastFilterPortCurrentCount,
       "swMcastFilterPortMaxGroupAction": swMcastFilterPortMaxGroupAction,
       "swMcastFilterVLANGroupTable": swMcastFilterVLANGroupTable,
       "swMcastFilterVLANGroupEntry": swMcastFilterVLANGroupEntry,
       "swMcastFilterVLANGroupVLANIndex": swMcastFilterVLANGroupVLANIndex,
       "swMcastFilterVLANGroupProfileId": swMcastFilterVLANGroupProfileId,
       "swMcastFilterVLANGroupRowStatus": swMcastFilterVLANGroupRowStatus,
       "swMcastFilterVLANAccessTable": swMcastFilterVLANAccessTable,
       "swMcastFilterVLANAccessEntry": swMcastFilterVLANAccessEntry,
       "swMcastFilterVLANAccessVLANIndex": swMcastFilterVLANAccessVLANIndex,
       "swMcastFilterVLANAccessState": swMcastFilterVLANAccessState,
       "swMcastFilterVLANMaxGroupTable": swMcastFilterVLANMaxGroupTable,
       "swMcastFilterVLANMaxGroupEntry": swMcastFilterVLANMaxGroupEntry,
       "swMcastFilterVLANMaxGroupVLANIndex": swMcastFilterVLANMaxGroupVLANIndex,
       "swMcastFilterVLANMaxGroup": swMcastFilterVLANMaxGroup,
       "swMcastFilterVLANCurrentCount": swMcastFilterVLANCurrentCount,
       "swMcastFilterVLANMaxGroupAction": swMcastFilterVLANMaxGroupAction,
       "swMcastFilterIpv6ProfileInfoTable": swMcastFilterIpv6ProfileInfoTable,
       "swMcastFilterIpv6ProfileInfoEntry": swMcastFilterIpv6ProfileInfoEntry,
       "swMcastFilterIpv6ProfileInfoIndex": swMcastFilterIpv6ProfileInfoIndex,
       "swMcastFilterIpv6ProfileInfoDescription": swMcastFilterIpv6ProfileInfoDescription,
       "swMcastFilterIpv6ProfileInfoRowStatus": swMcastFilterIpv6ProfileInfoRowStatus,
       "swMcastFilterIpv6ProfileCtrlTable": swMcastFilterIpv6ProfileCtrlTable,
       "swMcastFilterIpv6ProfileCtrlEntry": swMcastFilterIpv6ProfileCtrlEntry,
       "swMcastFilterIpv6ProfileCtrlProfileIndex": swMcastFilterIpv6ProfileCtrlProfileIndex,
       "swMcastFilterIpv6ProfileCtrlStartAddress": swMcastFilterIpv6ProfileCtrlStartAddress,
       "swMcastFilterIpv6ProfileCtrlEndAddress": swMcastFilterIpv6ProfileCtrlEndAddress,
       "swMcastFilterIpv6ProfileCtrlRowStatus": swMcastFilterIpv6ProfileCtrlRowStatus,
       "swMcastFilterIpv6PortGroupTable": swMcastFilterIpv6PortGroupTable,
       "swMcastFilterIpv6PortGroupEntry": swMcastFilterIpv6PortGroupEntry,
       "swMcastFilterIpv6PortGroupPortIndex": swMcastFilterIpv6PortGroupPortIndex,
       "swMcastFilterIpv6PortGroupProfileId": swMcastFilterIpv6PortGroupProfileId,
       "swMcastFilterIpv6PortGroupRowStatus": swMcastFilterIpv6PortGroupRowStatus,
       "swMcastFilterIpv6PortAccessTable": swMcastFilterIpv6PortAccessTable,
       "swMcastFilterIpv6PortAccessEntry": swMcastFilterIpv6PortAccessEntry,
       "swMcastFilterIpv6PortAccessPortIndex": swMcastFilterIpv6PortAccessPortIndex,
       "swMcastFilterIpv6PortAccessState": swMcastFilterIpv6PortAccessState,
       "swMcastFilterIpv6PortMaxGroupTable": swMcastFilterIpv6PortMaxGroupTable,
       "swMcastFilterIpv6PortMaxGroupEntry": swMcastFilterIpv6PortMaxGroupEntry,
       "swMcastFilterIpv6PortMaxGroupPortIndex": swMcastFilterIpv6PortMaxGroupPortIndex,
       "swMcastFilterIpv6PortMaxGroup": swMcastFilterIpv6PortMaxGroup,
       "swMcastFilterIpv6PortCurrentCount": swMcastFilterIpv6PortCurrentCount,
       "swMcastFilterIpv6PortMaxGroupAction": swMcastFilterIpv6PortMaxGroupAction,
       "swMcastFilterIpv6VLANGroupTable": swMcastFilterIpv6VLANGroupTable,
       "swMcastFilterIpv6VLANGroupEntry": swMcastFilterIpv6VLANGroupEntry,
       "swMcastFilterIpv6VLANGroupVLANIndex": swMcastFilterIpv6VLANGroupVLANIndex,
       "swMcastFilterIpv6VLANGroupProfileId": swMcastFilterIpv6VLANGroupProfileId,
       "swMcastFilterIpv6VLANGroupRowStatus": swMcastFilterIpv6VLANGroupRowStatus,
       "swMcastFilterIpv6VLANAccessTable": swMcastFilterIpv6VLANAccessTable,
       "swMcastFilterIpv6VLANAccessEntry": swMcastFilterIpv6VLANAccessEntry,
       "swMcastFilterIpv6VLANAccessVLANIndex": swMcastFilterIpv6VLANAccessVLANIndex,
       "swMcastFilterIpv6VLANAccessState": swMcastFilterIpv6VLANAccessState,
       "swMcastFilterIpv6VLANMaxGroupTable": swMcastFilterIpv6VLANMaxGroupTable,
       "swMcastFilterIpv6VLANMaxGroupEntry": swMcastFilterIpv6VLANMaxGroupEntry,
       "swMcastFilterIpv6VLANMaxGroupVLANIndex": swMcastFilterIpv6VLANMaxGroupVLANIndex,
       "swMcastFilterIpv6VLANMaxGroup": swMcastFilterIpv6VLANMaxGroup,
       "swMcastFilterIpv6VLANCurrentCount": swMcastFilterIpv6VLANCurrentCount,
       "swMcastFilterIpv6VLANMaxGroupAction": swMcastFilterIpv6VLANMaxGroupAction}
)
