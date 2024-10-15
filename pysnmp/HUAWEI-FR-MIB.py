# SNMP MIB module (HUAWEI-FR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-FR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:03:49 2024
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

(hwDatacomm,) = mibBuilder.importSymbols(
    "HUAWEI-MIB",
    "hwDatacomm")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hwFrMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 168)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwFrObjects_ObjectIdentity = ObjectIdentity
hwFrObjects = _HwFrObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 168, 1)
)
_HwFrTable_Object = MibTable
hwFrTable = _HwFrTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 168, 1, 1)
)
if mibBuilder.loadTexts:
    hwFrTable.setStatus("current")
_HwFrEntry_Object = MibTableRow
hwFrEntry = _HwFrEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 168, 1, 1, 1)
)
hwFrEntry.setIndexNames(
    (0, "HUAWEI-FR-MIB", "hwFrIfIndex"),
)
if mibBuilder.loadTexts:
    hwFrEntry.setStatus("current")
_HwFrIfIndex_Type = InterfaceIndex
_HwFrIfIndex_Object = MibTableColumn
hwFrIfIndex = _HwFrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 168, 1, 1, 1, 1),
    _HwFrIfIndex_Type()
)
hwFrIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwFrIfIndex.setStatus("current")


class _HwFrEncapType_Type(Integer32):
    """Custom type hwFrEncapType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ietf", 2),
          ("nonstandard", 1))
    )


_HwFrEncapType_Type.__name__ = "Integer32"
_HwFrEncapType_Object = MibTableColumn
hwFrEncapType = _HwFrEncapType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 168, 1, 1, 1, 2),
    _HwFrEncapType_Type()
)
hwFrEncapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwFrEncapType.setStatus("current")


class _HwFrIfType_Type(Integer32):
    """Custom type hwFrIfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dce", 2),
          ("dte", 1),
          ("nni", 3))
    )


_HwFrIfType_Type.__name__ = "Integer32"
_HwFrIfType_Object = MibTableColumn
hwFrIfType = _HwFrIfType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 168, 1, 1, 1, 3),
    _HwFrIfType_Type()
)
hwFrIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwFrIfType.setStatus("current")


class _HwFrLmiType_Type(Integer32):
    """Custom type hwFrLmiType based on Integer32"""
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
        *(("ansi", 3),
          ("nonstandard", 2),
          ("notset", 1),
          ("q933a", 4))
    )


_HwFrLmiType_Type.__name__ = "Integer32"
_HwFrLmiType_Object = MibTableColumn
hwFrLmiType = _HwFrLmiType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 168, 1, 1, 1, 4),
    _HwFrLmiType_Type()
)
hwFrLmiType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwFrLmiType.setStatus("current")


class _HwFrLmiN391DteValue_Type(Integer32):
    """Custom type hwFrLmiN391DteValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
        ValueRangeConstraint(65535, 65535),
    )


_HwFrLmiN391DteValue_Type.__name__ = "Integer32"
_HwFrLmiN391DteValue_Object = MibTableColumn
hwFrLmiN391DteValue = _HwFrLmiN391DteValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 168, 1, 1, 1, 5),
    _HwFrLmiN391DteValue_Type()
)
hwFrLmiN391DteValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwFrLmiN391DteValue.setStatus("current")


class _HwFrLmiN392DteValue_Type(Integer32):
    """Custom type hwFrLmiN392DteValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
        ValueRangeConstraint(65535, 65535),
    )


_HwFrLmiN392DteValue_Type.__name__ = "Integer32"
_HwFrLmiN392DteValue_Object = MibTableColumn
hwFrLmiN392DteValue = _HwFrLmiN392DteValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 168, 1, 1, 1, 6),
    _HwFrLmiN392DteValue_Type()
)
hwFrLmiN392DteValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwFrLmiN392DteValue.setStatus("current")


class _HwFrLmiN392DceValue_Type(Integer32):
    """Custom type hwFrLmiN392DceValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
        ValueRangeConstraint(65535, 65535),
    )


_HwFrLmiN392DceValue_Type.__name__ = "Integer32"
_HwFrLmiN392DceValue_Object = MibTableColumn
hwFrLmiN392DceValue = _HwFrLmiN392DceValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 168, 1, 1, 1, 7),
    _HwFrLmiN392DceValue_Type()
)
hwFrLmiN392DceValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwFrLmiN392DceValue.setStatus("current")


class _HwFrLmiN393DteValue_Type(Integer32):
    """Custom type hwFrLmiN393DteValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
        ValueRangeConstraint(65535, 65535),
    )


_HwFrLmiN393DteValue_Type.__name__ = "Integer32"
_HwFrLmiN393DteValue_Object = MibTableColumn
hwFrLmiN393DteValue = _HwFrLmiN393DteValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 168, 1, 1, 1, 8),
    _HwFrLmiN393DteValue_Type()
)
hwFrLmiN393DteValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwFrLmiN393DteValue.setStatus("current")


class _HwFrLmiN393DceValue_Type(Integer32):
    """Custom type hwFrLmiN393DceValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
        ValueRangeConstraint(65535, 65535),
    )


_HwFrLmiN393DceValue_Type.__name__ = "Integer32"
_HwFrLmiN393DceValue_Object = MibTableColumn
hwFrLmiN393DceValue = _HwFrLmiN393DceValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 168, 1, 1, 1, 9),
    _HwFrLmiN393DceValue_Type()
)
hwFrLmiN393DceValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwFrLmiN393DceValue.setStatus("current")


class _HwFrLmiT391DteValue_Type(Integer32):
    """Custom type hwFrLmiT391DteValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
        ValueRangeConstraint(65535, 65535),
    )


_HwFrLmiT391DteValue_Type.__name__ = "Integer32"
_HwFrLmiT391DteValue_Object = MibTableColumn
hwFrLmiT391DteValue = _HwFrLmiT391DteValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 168, 1, 1, 1, 10),
    _HwFrLmiT391DteValue_Type()
)
hwFrLmiT391DteValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwFrLmiT391DteValue.setStatus("current")


class _HwFrLmiT392DceValue_Type(Integer32):
    """Custom type hwFrLmiT392DceValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 30),
        ValueRangeConstraint(65535, 65535),
    )


_HwFrLmiT392DceValue_Type.__name__ = "Integer32"
_HwFrLmiT392DceValue_Object = MibTableColumn
hwFrLmiT392DceValue = _HwFrLmiT392DceValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 168, 1, 1, 1, 11),
    _HwFrLmiT392DceValue_Type()
)
hwFrLmiT392DceValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwFrLmiT392DceValue.setStatus("current")
_HwFrIphcEnable_Type = TruthValue
_HwFrIphcEnable_Object = MibTableColumn
hwFrIphcEnable = _HwFrIphcEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 168, 1, 1, 1, 12),
    _HwFrIphcEnable_Type()
)
hwFrIphcEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwFrIphcEnable.setStatus("current")
_HwFrIphcNonstandardFormat_Type = TruthValue
_HwFrIphcNonstandardFormat_Object = MibTableColumn
hwFrIphcNonstandardFormat = _HwFrIphcNonstandardFormat_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 168, 1, 1, 1, 13),
    _HwFrIphcNonstandardFormat_Type()
)
hwFrIphcNonstandardFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwFrIphcNonstandardFormat.setStatus("current")
_HwFrIphcTcpInclude_Type = TruthValue
_HwFrIphcTcpInclude_Object = MibTableColumn
hwFrIphcTcpInclude = _HwFrIphcTcpInclude_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 168, 1, 1, 1, 14),
    _HwFrIphcTcpInclude_Type()
)
hwFrIphcTcpInclude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwFrIphcTcpInclude.setStatus("current")
_HwFrInarpEnable_Type = TruthValue
_HwFrInarpEnable_Object = MibTableColumn
hwFrInarpEnable = _HwFrInarpEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 168, 1, 1, 1, 15),
    _HwFrInarpEnable_Type()
)
hwFrInarpEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwFrInarpEnable.setStatus("current")


class _HwFrIphcTcpConnection_Type(Integer32):
    """Custom type hwFrIphcTcpConnection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 255),
        ValueRangeConstraint(256, 256),
        ValueRangeConstraint(65535, 65535),
    )


_HwFrIphcTcpConnection_Type.__name__ = "Integer32"
_HwFrIphcTcpConnection_Object = MibTableColumn
hwFrIphcTcpConnection = _HwFrIphcTcpConnection_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 168, 1, 1, 1, 16),
    _HwFrIphcTcpConnection_Type()
)
hwFrIphcTcpConnection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwFrIphcTcpConnection.setStatus("current")


class _HwFrIphcRtpConnection_Type(Integer32):
    """Custom type hwFrIphcRtpConnection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 255),
        ValueRangeConstraint(256, 256),
        ValueRangeConstraint(65535, 65535),
    )


_HwFrIphcRtpConnection_Type.__name__ = "Integer32"
_HwFrIphcRtpConnection_Object = MibTableColumn
hwFrIphcRtpConnection = _HwFrIphcRtpConnection_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 168, 1, 1, 1, 17),
    _HwFrIphcRtpConnection_Type()
)
hwFrIphcRtpConnection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwFrIphcRtpConnection.setStatus("current")
_HwFrPvcTable_Object = MibTable
hwFrPvcTable = _HwFrPvcTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 168, 1, 2)
)
if mibBuilder.loadTexts:
    hwFrPvcTable.setStatus("current")
_HwFrPvcEntry_Object = MibTableRow
hwFrPvcEntry = _HwFrPvcEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 168, 1, 2, 1)
)
hwFrPvcEntry.setIndexNames(
    (0, "HUAWEI-FR-MIB", "hwFrPvcIfIndex"),
    (0, "HUAWEI-FR-MIB", "hwFrPvcDlciNumber"),
)
if mibBuilder.loadTexts:
    hwFrPvcEntry.setStatus("current")
_HwFrPvcIfIndex_Type = InterfaceIndex
_HwFrPvcIfIndex_Object = MibTableColumn
hwFrPvcIfIndex = _HwFrPvcIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 168, 1, 2, 1, 1),
    _HwFrPvcIfIndex_Type()
)
hwFrPvcIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwFrPvcIfIndex.setStatus("current")


class _HwFrPvcDlciNumber_Type(Integer32):
    """Custom type hwFrPvcDlciNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1022),
    )


_HwFrPvcDlciNumber_Type.__name__ = "Integer32"
_HwFrPvcDlciNumber_Object = MibTableColumn
hwFrPvcDlciNumber = _HwFrPvcDlciNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 168, 1, 2, 1, 2),
    _HwFrPvcDlciNumber_Type()
)
hwFrPvcDlciNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwFrPvcDlciNumber.setStatus("current")


class _HwFrPvcState_Type(Integer32):
    """Custom type hwFrPvcState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 1))
    )


_HwFrPvcState_Type.__name__ = "Integer32"
_HwFrPvcState_Object = MibTableColumn
hwFrPvcState = _HwFrPvcState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 168, 1, 2, 1, 3),
    _HwFrPvcState_Type()
)
hwFrPvcState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwFrPvcState.setStatus("current")
_HwFrPvcInarpEnable_Type = TruthValue
_HwFrPvcInarpEnable_Object = MibTableColumn
hwFrPvcInarpEnable = _HwFrPvcInarpEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 168, 1, 2, 1, 4),
    _HwFrPvcInarpEnable_Type()
)
hwFrPvcInarpEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwFrPvcInarpEnable.setStatus("current")
_HwFrPvcGroupTable_Object = MibTable
hwFrPvcGroupTable = _HwFrPvcGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 168, 1, 3)
)
if mibBuilder.loadTexts:
    hwFrPvcGroupTable.setStatus("current")
_HwFrPvcGroupEntry_Object = MibTableRow
hwFrPvcGroupEntry = _HwFrPvcGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 168, 1, 3, 1)
)
hwFrPvcGroupEntry.setIndexNames(
    (0, "HUAWEI-FR-MIB", "hwFrPvcGroupIfIndex"),
    (0, "HUAWEI-FR-MIB", "hwFrPvcGroupName"),
)
if mibBuilder.loadTexts:
    hwFrPvcGroupEntry.setStatus("current")
_HwFrPvcGroupIfIndex_Type = InterfaceIndex
_HwFrPvcGroupIfIndex_Object = MibTableColumn
hwFrPvcGroupIfIndex = _HwFrPvcGroupIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 168, 1, 3, 1, 1),
    _HwFrPvcGroupIfIndex_Type()
)
hwFrPvcGroupIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwFrPvcGroupIfIndex.setStatus("current")


class _HwFrPvcGroupName_Type(OctetString):
    """Custom type hwFrPvcGroupName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_HwFrPvcGroupName_Type.__name__ = "OctetString"
_HwFrPvcGroupName_Object = MibTableColumn
hwFrPvcGroupName = _HwFrPvcGroupName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 168, 1, 3, 1, 2),
    _HwFrPvcGroupName_Type()
)
hwFrPvcGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwFrPvcGroupName.setStatus("current")


class _HwFrPvcGroupState_Type(Integer32):
    """Custom type hwFrPvcGroupState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 1))
    )


_HwFrPvcGroupState_Type.__name__ = "Integer32"
_HwFrPvcGroupState_Object = MibTableColumn
hwFrPvcGroupState = _HwFrPvcGroupState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 168, 1, 3, 1, 3),
    _HwFrPvcGroupState_Type()
)
hwFrPvcGroupState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwFrPvcGroupState.setStatus("current")


class _HwFrPvcGroupTosType_Type(Integer32):
    """Custom type hwFrPvcGroupTosType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dscp", 3),
          ("none", 1),
          ("precedence", 2))
    )


_HwFrPvcGroupTosType_Type.__name__ = "Integer32"
_HwFrPvcGroupTosType_Object = MibTableColumn
hwFrPvcGroupTosType = _HwFrPvcGroupTosType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 168, 1, 3, 1, 4),
    _HwFrPvcGroupTosType_Type()
)
hwFrPvcGroupTosType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwFrPvcGroupTosType.setStatus("current")
_HwFrPvcGroupInArpEnable_Type = TruthValue
_HwFrPvcGroupInArpEnable_Object = MibTableColumn
hwFrPvcGroupInArpEnable = _HwFrPvcGroupInArpEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 168, 1, 3, 1, 5),
    _HwFrPvcGroupInArpEnable_Type()
)
hwFrPvcGroupInArpEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwFrPvcGroupInArpEnable.setStatus("current")
_HwFrPvcGroupMemTable_Object = MibTable
hwFrPvcGroupMemTable = _HwFrPvcGroupMemTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 168, 1, 4)
)
if mibBuilder.loadTexts:
    hwFrPvcGroupMemTable.setStatus("current")
_HwFrPvcGroupMemEntry_Object = MibTableRow
hwFrPvcGroupMemEntry = _HwFrPvcGroupMemEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 168, 1, 4, 1)
)
hwFrPvcGroupMemEntry.setIndexNames(
    (0, "HUAWEI-FR-MIB", "hwFrPvcGroupMemIfIndex"),
    (0, "HUAWEI-FR-MIB", "hwFrPvcGroupMemPvcGroupName"),
    (0, "HUAWEI-FR-MIB", "hwFrPvcGroupMemDlciNumber"),
)
if mibBuilder.loadTexts:
    hwFrPvcGroupMemEntry.setStatus("current")
_HwFrPvcGroupMemIfIndex_Type = InterfaceIndex
_HwFrPvcGroupMemIfIndex_Object = MibTableColumn
hwFrPvcGroupMemIfIndex = _HwFrPvcGroupMemIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 168, 1, 4, 1, 1),
    _HwFrPvcGroupMemIfIndex_Type()
)
hwFrPvcGroupMemIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwFrPvcGroupMemIfIndex.setStatus("current")


class _HwFrPvcGroupMemPvcGroupName_Type(OctetString):
    """Custom type hwFrPvcGroupMemPvcGroupName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_HwFrPvcGroupMemPvcGroupName_Type.__name__ = "OctetString"
_HwFrPvcGroupMemPvcGroupName_Object = MibTableColumn
hwFrPvcGroupMemPvcGroupName = _HwFrPvcGroupMemPvcGroupName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 168, 1, 4, 1, 2),
    _HwFrPvcGroupMemPvcGroupName_Type()
)
hwFrPvcGroupMemPvcGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwFrPvcGroupMemPvcGroupName.setStatus("current")


class _HwFrPvcGroupMemDlciNumber_Type(Integer32):
    """Custom type hwFrPvcGroupMemDlciNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1022),
    )


_HwFrPvcGroupMemDlciNumber_Type.__name__ = "Integer32"
_HwFrPvcGroupMemDlciNumber_Object = MibTableColumn
hwFrPvcGroupMemDlciNumber = _HwFrPvcGroupMemDlciNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 168, 1, 4, 1, 3),
    _HwFrPvcGroupMemDlciNumber_Type()
)
hwFrPvcGroupMemDlciNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwFrPvcGroupMemDlciNumber.setStatus("current")


class _HwFrPvcGroupMemTosType_Type(Integer32):
    """Custom type hwFrPvcGroupMemTosType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dscp", 3),
          ("none", 1),
          ("precedence", 2))
    )


_HwFrPvcGroupMemTosType_Type.__name__ = "Integer32"
_HwFrPvcGroupMemTosType_Object = MibTableColumn
hwFrPvcGroupMemTosType = _HwFrPvcGroupMemTosType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 168, 1, 4, 1, 4),
    _HwFrPvcGroupMemTosType_Type()
)
hwFrPvcGroupMemTosType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwFrPvcGroupMemTosType.setStatus("current")


class _HwFrPvcGroupMemDefault_Type(TruthValue):
    """Custom type hwFrPvcGroupMemDefault based on TruthValue"""


_HwFrPvcGroupMemDefault_Object = MibTableColumn
hwFrPvcGroupMemDefault = _HwFrPvcGroupMemDefault_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 168, 1, 4, 1, 5),
    _HwFrPvcGroupMemDefault_Type()
)
hwFrPvcGroupMemDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwFrPvcGroupMemDefault.setStatus("current")


class _HwFrPvcGroupMemMinGrade_Type(Integer32):
    """Custom type hwFrPvcGroupMemMinGrade based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
        ValueRangeConstraint(255, 255),
    )


_HwFrPvcGroupMemMinGrade_Type.__name__ = "Integer32"
_HwFrPvcGroupMemMinGrade_Object = MibTableColumn
hwFrPvcGroupMemMinGrade = _HwFrPvcGroupMemMinGrade_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 168, 1, 4, 1, 6),
    _HwFrPvcGroupMemMinGrade_Type()
)
hwFrPvcGroupMemMinGrade.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwFrPvcGroupMemMinGrade.setStatus("current")


class _HwFrPvcGroupMemMaxGrade_Type(Integer32):
    """Custom type hwFrPvcGroupMemMaxGrade based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
        ValueRangeConstraint(255, 255),
    )


_HwFrPvcGroupMemMaxGrade_Type.__name__ = "Integer32"
_HwFrPvcGroupMemMaxGrade_Object = MibTableColumn
hwFrPvcGroupMemMaxGrade = _HwFrPvcGroupMemMaxGrade_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 168, 1, 4, 1, 7),
    _HwFrPvcGroupMemMaxGrade_Type()
)
hwFrPvcGroupMemMaxGrade.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwFrPvcGroupMemMaxGrade.setStatus("current")
_HwFrPvcGroupMapIpTable_Object = MibTable
hwFrPvcGroupMapIpTable = _HwFrPvcGroupMapIpTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 168, 1, 5)
)
if mibBuilder.loadTexts:
    hwFrPvcGroupMapIpTable.setStatus("current")
_HwFrPvcGroupMapIpEntry_Object = MibTableRow
hwFrPvcGroupMapIpEntry = _HwFrPvcGroupMapIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 168, 1, 5, 1)
)
hwFrPvcGroupMapIpEntry.setIndexNames(
    (0, "HUAWEI-FR-MIB", "hwFrPvcGroupMapIpIfIndex"),
    (0, "HUAWEI-FR-MIB", "hwFrPvcGroupMapIpName"),
    (0, "HUAWEI-FR-MIB", "hwFrPvcGroupMapIpIpAddr"),
)
if mibBuilder.loadTexts:
    hwFrPvcGroupMapIpEntry.setStatus("current")
_HwFrPvcGroupMapIpIfIndex_Type = InterfaceIndex
_HwFrPvcGroupMapIpIfIndex_Object = MibTableColumn
hwFrPvcGroupMapIpIfIndex = _HwFrPvcGroupMapIpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 168, 1, 5, 1, 1),
    _HwFrPvcGroupMapIpIfIndex_Type()
)
hwFrPvcGroupMapIpIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwFrPvcGroupMapIpIfIndex.setStatus("current")


class _HwFrPvcGroupMapIpName_Type(OctetString):
    """Custom type hwFrPvcGroupMapIpName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_HwFrPvcGroupMapIpName_Type.__name__ = "OctetString"
_HwFrPvcGroupMapIpName_Object = MibTableColumn
hwFrPvcGroupMapIpName = _HwFrPvcGroupMapIpName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 168, 1, 5, 1, 2),
    _HwFrPvcGroupMapIpName_Type()
)
hwFrPvcGroupMapIpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwFrPvcGroupMapIpName.setStatus("current")
_HwFrPvcGroupMapIpIpAddr_Type = IpAddress
_HwFrPvcGroupMapIpIpAddr_Object = MibTableColumn
hwFrPvcGroupMapIpIpAddr = _HwFrPvcGroupMapIpIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 168, 1, 5, 1, 3),
    _HwFrPvcGroupMapIpIpAddr_Type()
)
hwFrPvcGroupMapIpIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwFrPvcGroupMapIpIpAddr.setStatus("current")
_HwFrPvcGroupMapIpMask_Type = IpAddress
_HwFrPvcGroupMapIpMask_Object = MibTableColumn
hwFrPvcGroupMapIpMask = _HwFrPvcGroupMapIpMask_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 168, 1, 5, 1, 4),
    _HwFrPvcGroupMapIpMask_Type()
)
hwFrPvcGroupMapIpMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwFrPvcGroupMapIpMask.setStatus("current")


class _HwFrPvcGroupMapIpEncapType_Type(Integer32):
    """Custom type hwFrPvcGroupMapIpEncapType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ietf", 2),
          ("nonstandard", 1))
    )


_HwFrPvcGroupMapIpEncapType_Type.__name__ = "Integer32"
_HwFrPvcGroupMapIpEncapType_Object = MibTableColumn
hwFrPvcGroupMapIpEncapType = _HwFrPvcGroupMapIpEncapType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 168, 1, 5, 1, 5),
    _HwFrPvcGroupMapIpEncapType_Type()
)
hwFrPvcGroupMapIpEncapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwFrPvcGroupMapIpEncapType.setStatus("current")
_HwFrPvcGroupMapIpBroadcast_Type = TruthValue
_HwFrPvcGroupMapIpBroadcast_Object = MibTableColumn
hwFrPvcGroupMapIpBroadcast = _HwFrPvcGroupMapIpBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 168, 1, 5, 1, 6),
    _HwFrPvcGroupMapIpBroadcast_Type()
)
hwFrPvcGroupMapIpBroadcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwFrPvcGroupMapIpBroadcast.setStatus("current")
_HwFrPvcGroupMapIpDefault_Type = TruthValue
_HwFrPvcGroupMapIpDefault_Object = MibTableColumn
hwFrPvcGroupMapIpDefault = _HwFrPvcGroupMapIpDefault_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 168, 1, 5, 1, 7),
    _HwFrPvcGroupMapIpDefault_Type()
)
hwFrPvcGroupMapIpDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwFrPvcGroupMapIpDefault.setStatus("current")
_HwFrMapIpTable_Object = MibTable
hwFrMapIpTable = _HwFrMapIpTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 168, 1, 6)
)
if mibBuilder.loadTexts:
    hwFrMapIpTable.setStatus("current")
_HwFrMapIpEntry_Object = MibTableRow
hwFrMapIpEntry = _HwFrMapIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 168, 1, 6, 1)
)
hwFrMapIpEntry.setIndexNames(
    (0, "HUAWEI-FR-MIB", "hwFrMapIpIfIndex"),
    (0, "HUAWEI-FR-MIB", "hwFrMapIpDlciNumber"),
    (0, "HUAWEI-FR-MIB", "hwFrMapIpAddress"),
)
if mibBuilder.loadTexts:
    hwFrMapIpEntry.setStatus("current")
_HwFrMapIpIfIndex_Type = InterfaceIndex
_HwFrMapIpIfIndex_Object = MibTableColumn
hwFrMapIpIfIndex = _HwFrMapIpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 168, 1, 6, 1, 1),
    _HwFrMapIpIfIndex_Type()
)
hwFrMapIpIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwFrMapIpIfIndex.setStatus("current")


class _HwFrMapIpDlciNumber_Type(Integer32):
    """Custom type hwFrMapIpDlciNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1022),
    )


_HwFrMapIpDlciNumber_Type.__name__ = "Integer32"
_HwFrMapIpDlciNumber_Object = MibTableColumn
hwFrMapIpDlciNumber = _HwFrMapIpDlciNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 168, 1, 6, 1, 2),
    _HwFrMapIpDlciNumber_Type()
)
hwFrMapIpDlciNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwFrMapIpDlciNumber.setStatus("current")
_HwFrMapIpAddress_Type = IpAddress
_HwFrMapIpAddress_Object = MibTableColumn
hwFrMapIpAddress = _HwFrMapIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 168, 1, 6, 1, 3),
    _HwFrMapIpAddress_Type()
)
hwFrMapIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwFrMapIpAddress.setStatus("current")
_HwFrMapIpMask_Type = IpAddress
_HwFrMapIpMask_Object = MibTableColumn
hwFrMapIpMask = _HwFrMapIpMask_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 168, 1, 6, 1, 4),
    _HwFrMapIpMask_Type()
)
hwFrMapIpMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwFrMapIpMask.setStatus("current")
_HwFrMapIpBroadcast_Type = TruthValue
_HwFrMapIpBroadcast_Object = MibTableColumn
hwFrMapIpBroadcast = _HwFrMapIpBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 168, 1, 6, 1, 5),
    _HwFrMapIpBroadcast_Type()
)
hwFrMapIpBroadcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwFrMapIpBroadcast.setStatus("current")


class _HwFrMapIpEncapType_Type(Integer32):
    """Custom type hwFrMapIpEncapType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ietf", 2),
          ("nonstandard", 1))
    )


_HwFrMapIpEncapType_Type.__name__ = "Integer32"
_HwFrMapIpEncapType_Object = MibTableColumn
hwFrMapIpEncapType = _HwFrMapIpEncapType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 168, 1, 6, 1, 6),
    _HwFrMapIpEncapType_Type()
)
hwFrMapIpEncapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwFrMapIpEncapType.setStatus("current")
_HwFrMapIpDefault_Type = TruthValue
_HwFrMapIpDefault_Object = MibTableColumn
hwFrMapIpDefault = _HwFrMapIpDefault_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 168, 1, 6, 1, 7),
    _HwFrMapIpDefault_Type()
)
hwFrMapIpDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwFrMapIpDefault.setStatus("current")
_HwFrMapIpFrf9Enable_Type = TruthValue
_HwFrMapIpFrf9Enable_Object = MibTableColumn
hwFrMapIpFrf9Enable = _HwFrMapIpFrf9Enable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 168, 1, 6, 1, 8),
    _HwFrMapIpFrf9Enable_Type()
)
hwFrMapIpFrf9Enable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwFrMapIpFrf9Enable.setStatus("current")
_HwFrMapIpIphcEnable_Type = TruthValue
_HwFrMapIpIphcEnable_Object = MibTableColumn
hwFrMapIpIphcEnable = _HwFrMapIpIphcEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 168, 1, 6, 1, 9),
    _HwFrMapIpIphcEnable_Type()
)
hwFrMapIpIphcEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwFrMapIpIphcEnable.setStatus("current")


class _HwFrMapIpRtpConnNumber_Type(Integer32):
    """Custom type hwFrMapIpRtpConnNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 256),
        ValueRangeConstraint(65535, 65535),
    )


_HwFrMapIpRtpConnNumber_Type.__name__ = "Integer32"
_HwFrMapIpRtpConnNumber_Object = MibTableColumn
hwFrMapIpRtpConnNumber = _HwFrMapIpRtpConnNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 168, 1, 6, 1, 10),
    _HwFrMapIpRtpConnNumber_Type()
)
hwFrMapIpRtpConnNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwFrMapIpRtpConnNumber.setStatus("current")
_HwFrMapPppTable_Object = MibTable
hwFrMapPppTable = _HwFrMapPppTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 168, 1, 7)
)
if mibBuilder.loadTexts:
    hwFrMapPppTable.setStatus("current")
_HwFrMapPppEntry_Object = MibTableRow
hwFrMapPppEntry = _HwFrMapPppEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 168, 1, 7, 1)
)
hwFrMapPppEntry.setIndexNames(
    (0, "HUAWEI-FR-MIB", "hwFrMapPppIfIndex"),
    (0, "HUAWEI-FR-MIB", "hwFrMapPppDlciNumber"),
)
if mibBuilder.loadTexts:
    hwFrMapPppEntry.setStatus("current")
_HwFrMapPppIfIndex_Type = InterfaceIndex
_HwFrMapPppIfIndex_Object = MibTableColumn
hwFrMapPppIfIndex = _HwFrMapPppIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 168, 1, 7, 1, 1),
    _HwFrMapPppIfIndex_Type()
)
hwFrMapPppIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwFrMapPppIfIndex.setStatus("current")


class _HwFrMapPppDlciNumber_Type(Integer32):
    """Custom type hwFrMapPppDlciNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1022),
    )


_HwFrMapPppDlciNumber_Type.__name__ = "Integer32"
_HwFrMapPppDlciNumber_Object = MibTableColumn
hwFrMapPppDlciNumber = _HwFrMapPppDlciNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 168, 1, 7, 1, 2),
    _HwFrMapPppDlciNumber_Type()
)
hwFrMapPppDlciNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwFrMapPppDlciNumber.setStatus("current")
_HwFrMapPppVTIfIndex_Type = Integer32
_HwFrMapPppVTIfIndex_Object = MibTableColumn
hwFrMapPppVTIfIndex = _HwFrMapPppVTIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 168, 1, 7, 1, 3),
    _HwFrMapPppVTIfIndex_Type()
)
hwFrMapPppVTIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwFrMapPppVTIfIndex.setStatus("current")


class _HwFrMapPppState_Type(Integer32):
    """Custom type hwFrMapPppState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 1))
    )


_HwFrMapPppState_Type.__name__ = "Integer32"
_HwFrMapPppState_Object = MibTableColumn
hwFrMapPppState = _HwFrMapPppState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 168, 1, 7, 1, 4),
    _HwFrMapPppState_Type()
)
hwFrMapPppState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwFrMapPppState.setStatus("current")
_HwFrMapBridgeTable_Object = MibTable
hwFrMapBridgeTable = _HwFrMapBridgeTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 168, 1, 8)
)
if mibBuilder.loadTexts:
    hwFrMapBridgeTable.setStatus("current")
_HwFrMapBridgeEntry_Object = MibTableRow
hwFrMapBridgeEntry = _HwFrMapBridgeEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 168, 1, 8, 1)
)
hwFrMapBridgeEntry.setIndexNames(
    (0, "HUAWEI-FR-MIB", "hwFrMapBridgeIfIndex"),
    (0, "HUAWEI-FR-MIB", "hwFrMapBridgeDlciNumber"),
)
if mibBuilder.loadTexts:
    hwFrMapBridgeEntry.setStatus("current")
_HwFrMapBridgeIfIndex_Type = InterfaceIndex
_HwFrMapBridgeIfIndex_Object = MibTableColumn
hwFrMapBridgeIfIndex = _HwFrMapBridgeIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 168, 1, 8, 1, 1),
    _HwFrMapBridgeIfIndex_Type()
)
hwFrMapBridgeIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwFrMapBridgeIfIndex.setStatus("current")


class _HwFrMapBridgeDlciNumber_Type(Integer32):
    """Custom type hwFrMapBridgeDlciNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1022),
    )


_HwFrMapBridgeDlciNumber_Type.__name__ = "Integer32"
_HwFrMapBridgeDlciNumber_Object = MibTableColumn
hwFrMapBridgeDlciNumber = _HwFrMapBridgeDlciNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 168, 1, 8, 1, 2),
    _HwFrMapBridgeDlciNumber_Type()
)
hwFrMapBridgeDlciNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwFrMapBridgeDlciNumber.setStatus("current")


class _HwFrMapBridgeState_Type(Integer32):
    """Custom type hwFrMapBridgeState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 1))
    )


_HwFrMapBridgeState_Type.__name__ = "Integer32"
_HwFrMapBridgeState_Object = MibTableColumn
hwFrMapBridgeState = _HwFrMapBridgeState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 168, 1, 8, 1, 3),
    _HwFrMapBridgeState_Type()
)
hwFrMapBridgeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwFrMapBridgeState.setStatus("current")
_HwFrConformance_ObjectIdentity = ObjectIdentity
hwFrConformance = _HwFrConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 168, 2)
)
_HwFrCompliances_ObjectIdentity = ObjectIdentity
hwFrCompliances = _HwFrCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 168, 2, 1)
)
_HwFrGroups_ObjectIdentity = ObjectIdentity
hwFrGroups = _HwFrGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 168, 2, 2)
)

# Managed Objects groups

hwFrObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 168, 2, 2, 1)
)
hwFrObjectGroup.setObjects(
    ("HUAWEI-FR-MIB", "hwFrIfIndex")
)
if mibBuilder.loadTexts:
    hwFrObjectGroup.setStatus("current")

hwFrPvcObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 168, 2, 2, 2)
)
hwFrPvcObjectGroup.setObjects(
      *(("HUAWEI-FR-MIB", "hwFrPvcIfIndex"),
        ("HUAWEI-FR-MIB", "hwFrPvcDlciNumber"))
)
if mibBuilder.loadTexts:
    hwFrPvcObjectGroup.setStatus("current")

hwFrPvcGroupObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 168, 2, 2, 3)
)
hwFrPvcGroupObjectGroup.setObjects(
      *(("HUAWEI-FR-MIB", "hwFrPvcGroupIfIndex"),
        ("HUAWEI-FR-MIB", "hwFrPvcGroupName"))
)
if mibBuilder.loadTexts:
    hwFrPvcGroupObjectGroup.setStatus("current")

hwFrPvcGroupMemObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 168, 2, 2, 4)
)
hwFrPvcGroupMemObjectGroup.setObjects(
      *(("HUAWEI-FR-MIB", "hwFrPvcGroupMemIfIndex"),
        ("HUAWEI-FR-MIB", "hwFrPvcGroupMemPvcGroupName"),
        ("HUAWEI-FR-MIB", "hwFrPvcGroupMemDlciNumber"))
)
if mibBuilder.loadTexts:
    hwFrPvcGroupMemObjectGroup.setStatus("current")

hwFrPvcGroupMapIpObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 168, 2, 2, 5)
)
hwFrPvcGroupMapIpObjectGroup.setObjects(
      *(("HUAWEI-FR-MIB", "hwFrPvcGroupMapIpIfIndex"),
        ("HUAWEI-FR-MIB", "hwFrPvcGroupMapIpName"),
        ("HUAWEI-FR-MIB", "hwFrPvcGroupMapIpIpAddr"))
)
if mibBuilder.loadTexts:
    hwFrPvcGroupMapIpObjectGroup.setStatus("current")

hwFrMapIpObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 168, 2, 2, 6)
)
hwFrMapIpObjectGroup.setObjects(
      *(("HUAWEI-FR-MIB", "hwFrMapIpIfIndex"),
        ("HUAWEI-FR-MIB", "hwFrMapIpAddress"),
        ("HUAWEI-FR-MIB", "hwFrMapIpDlciNumber"))
)
if mibBuilder.loadTexts:
    hwFrMapIpObjectGroup.setStatus("current")

hwFrMapPppObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 168, 2, 2, 7)
)
hwFrMapPppObjectGroup.setObjects(
      *(("HUAWEI-FR-MIB", "hwFrMapPppIfIndex"),
        ("HUAWEI-FR-MIB", "hwFrMapPppDlciNumber"))
)
if mibBuilder.loadTexts:
    hwFrMapPppObjectGroup.setStatus("current")

hwFrMapBridgeObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 168, 2, 2, 8)
)
hwFrMapBridgeObjectGroup.setObjects(
      *(("HUAWEI-FR-MIB", "hwFrMapBridgeIfIndex"),
        ("HUAWEI-FR-MIB", "hwFrMapBridgeDlciNumber"))
)
if mibBuilder.loadTexts:
    hwFrMapBridgeObjectGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hwFrCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 168, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hwFrCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-FR-MIB",
    **{"hwFrMIB": hwFrMIB,
       "hwFrObjects": hwFrObjects,
       "hwFrTable": hwFrTable,
       "hwFrEntry": hwFrEntry,
       "hwFrIfIndex": hwFrIfIndex,
       "hwFrEncapType": hwFrEncapType,
       "hwFrIfType": hwFrIfType,
       "hwFrLmiType": hwFrLmiType,
       "hwFrLmiN391DteValue": hwFrLmiN391DteValue,
       "hwFrLmiN392DteValue": hwFrLmiN392DteValue,
       "hwFrLmiN392DceValue": hwFrLmiN392DceValue,
       "hwFrLmiN393DteValue": hwFrLmiN393DteValue,
       "hwFrLmiN393DceValue": hwFrLmiN393DceValue,
       "hwFrLmiT391DteValue": hwFrLmiT391DteValue,
       "hwFrLmiT392DceValue": hwFrLmiT392DceValue,
       "hwFrIphcEnable": hwFrIphcEnable,
       "hwFrIphcNonstandardFormat": hwFrIphcNonstandardFormat,
       "hwFrIphcTcpInclude": hwFrIphcTcpInclude,
       "hwFrInarpEnable": hwFrInarpEnable,
       "hwFrIphcTcpConnection": hwFrIphcTcpConnection,
       "hwFrIphcRtpConnection": hwFrIphcRtpConnection,
       "hwFrPvcTable": hwFrPvcTable,
       "hwFrPvcEntry": hwFrPvcEntry,
       "hwFrPvcIfIndex": hwFrPvcIfIndex,
       "hwFrPvcDlciNumber": hwFrPvcDlciNumber,
       "hwFrPvcState": hwFrPvcState,
       "hwFrPvcInarpEnable": hwFrPvcInarpEnable,
       "hwFrPvcGroupTable": hwFrPvcGroupTable,
       "hwFrPvcGroupEntry": hwFrPvcGroupEntry,
       "hwFrPvcGroupIfIndex": hwFrPvcGroupIfIndex,
       "hwFrPvcGroupName": hwFrPvcGroupName,
       "hwFrPvcGroupState": hwFrPvcGroupState,
       "hwFrPvcGroupTosType": hwFrPvcGroupTosType,
       "hwFrPvcGroupInArpEnable": hwFrPvcGroupInArpEnable,
       "hwFrPvcGroupMemTable": hwFrPvcGroupMemTable,
       "hwFrPvcGroupMemEntry": hwFrPvcGroupMemEntry,
       "hwFrPvcGroupMemIfIndex": hwFrPvcGroupMemIfIndex,
       "hwFrPvcGroupMemPvcGroupName": hwFrPvcGroupMemPvcGroupName,
       "hwFrPvcGroupMemDlciNumber": hwFrPvcGroupMemDlciNumber,
       "hwFrPvcGroupMemTosType": hwFrPvcGroupMemTosType,
       "hwFrPvcGroupMemDefault": hwFrPvcGroupMemDefault,
       "hwFrPvcGroupMemMinGrade": hwFrPvcGroupMemMinGrade,
       "hwFrPvcGroupMemMaxGrade": hwFrPvcGroupMemMaxGrade,
       "hwFrPvcGroupMapIpTable": hwFrPvcGroupMapIpTable,
       "hwFrPvcGroupMapIpEntry": hwFrPvcGroupMapIpEntry,
       "hwFrPvcGroupMapIpIfIndex": hwFrPvcGroupMapIpIfIndex,
       "hwFrPvcGroupMapIpName": hwFrPvcGroupMapIpName,
       "hwFrPvcGroupMapIpIpAddr": hwFrPvcGroupMapIpIpAddr,
       "hwFrPvcGroupMapIpMask": hwFrPvcGroupMapIpMask,
       "hwFrPvcGroupMapIpEncapType": hwFrPvcGroupMapIpEncapType,
       "hwFrPvcGroupMapIpBroadcast": hwFrPvcGroupMapIpBroadcast,
       "hwFrPvcGroupMapIpDefault": hwFrPvcGroupMapIpDefault,
       "hwFrMapIpTable": hwFrMapIpTable,
       "hwFrMapIpEntry": hwFrMapIpEntry,
       "hwFrMapIpIfIndex": hwFrMapIpIfIndex,
       "hwFrMapIpDlciNumber": hwFrMapIpDlciNumber,
       "hwFrMapIpAddress": hwFrMapIpAddress,
       "hwFrMapIpMask": hwFrMapIpMask,
       "hwFrMapIpBroadcast": hwFrMapIpBroadcast,
       "hwFrMapIpEncapType": hwFrMapIpEncapType,
       "hwFrMapIpDefault": hwFrMapIpDefault,
       "hwFrMapIpFrf9Enable": hwFrMapIpFrf9Enable,
       "hwFrMapIpIphcEnable": hwFrMapIpIphcEnable,
       "hwFrMapIpRtpConnNumber": hwFrMapIpRtpConnNumber,
       "hwFrMapPppTable": hwFrMapPppTable,
       "hwFrMapPppEntry": hwFrMapPppEntry,
       "hwFrMapPppIfIndex": hwFrMapPppIfIndex,
       "hwFrMapPppDlciNumber": hwFrMapPppDlciNumber,
       "hwFrMapPppVTIfIndex": hwFrMapPppVTIfIndex,
       "hwFrMapPppState": hwFrMapPppState,
       "hwFrMapBridgeTable": hwFrMapBridgeTable,
       "hwFrMapBridgeEntry": hwFrMapBridgeEntry,
       "hwFrMapBridgeIfIndex": hwFrMapBridgeIfIndex,
       "hwFrMapBridgeDlciNumber": hwFrMapBridgeDlciNumber,
       "hwFrMapBridgeState": hwFrMapBridgeState,
       "hwFrConformance": hwFrConformance,
       "hwFrCompliances": hwFrCompliances,
       "hwFrCompliance": hwFrCompliance,
       "hwFrGroups": hwFrGroups,
       "hwFrObjectGroup": hwFrObjectGroup,
       "hwFrPvcObjectGroup": hwFrPvcObjectGroup,
       "hwFrPvcGroupObjectGroup": hwFrPvcGroupObjectGroup,
       "hwFrPvcGroupMemObjectGroup": hwFrPvcGroupMemObjectGroup,
       "hwFrPvcGroupMapIpObjectGroup": hwFrPvcGroupMapIpObjectGroup,
       "hwFrMapIpObjectGroup": hwFrMapIpObjectGroup,
       "hwFrMapPppObjectGroup": hwFrMapPppObjectGroup,
       "hwFrMapBridgeObjectGroup": hwFrMapBridgeObjectGroup}
)
