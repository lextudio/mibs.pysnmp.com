# SNMP MIB module (HUAWEI-ATM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-ATM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:02:50 2024
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

(AtmVcIdentifier,
 AtmVpIdentifier) = mibBuilder.importSymbols(
    "ATM-TC-MIB",
    "AtmVcIdentifier",
    "AtmVpIdentifier")

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

hwAtmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 156)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwAtmObjects_ObjectIdentity = ObjectIdentity
hwAtmObjects = _HwAtmObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 156, 1)
)
_HwAtmTable_Object = MibTable
hwAtmTable = _HwAtmTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 156, 1, 1)
)
if mibBuilder.loadTexts:
    hwAtmTable.setStatus("current")
_HwAtmEntry_Object = MibTableRow
hwAtmEntry = _HwAtmEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 156, 1, 1, 1)
)
hwAtmEntry.setIndexNames(
    (0, "HUAWEI-ATM-MIB", "hwAtmIfIndex"),
)
if mibBuilder.loadTexts:
    hwAtmEntry.setStatus("current")
_HwAtmIfIndex_Type = InterfaceIndex
_HwAtmIfIndex_Object = MibTableColumn
hwAtmIfIndex = _HwAtmIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 156, 1, 1, 1, 1),
    _HwAtmIfIndex_Type()
)
hwAtmIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwAtmIfIndex.setStatus("current")


class _HwAtmIfType_Type(Integer32):
    """Custom type hwAtmIfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("oc12OrStm4", 2),
          ("oc3OrStm1", 1))
    )


_HwAtmIfType_Type.__name__ = "Integer32"
_HwAtmIfType_Object = MibTableColumn
hwAtmIfType = _HwAtmIfType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 156, 1, 1, 1, 11),
    _HwAtmIfType_Type()
)
hwAtmIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAtmIfType.setStatus("current")


class _HwAtmClock_Type(Integer32):
    """Custom type hwAtmClock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("master", 1),
          ("slave", 2))
    )


_HwAtmClock_Type.__name__ = "Integer32"
_HwAtmClock_Object = MibTableColumn
hwAtmClock = _HwAtmClock_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 156, 1, 1, 1, 12),
    _HwAtmClock_Type()
)
hwAtmClock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwAtmClock.setStatus("current")


class _HwAtmFrameFormat_Type(Integer32):
    """Custom type hwAtmFrameFormat based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sdh", 1),
          ("sonet", 2))
    )


_HwAtmFrameFormat_Type.__name__ = "Integer32"
_HwAtmFrameFormat_Object = MibTableColumn
hwAtmFrameFormat = _HwAtmFrameFormat_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 156, 1, 1, 1, 13),
    _HwAtmFrameFormat_Type()
)
hwAtmFrameFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwAtmFrameFormat.setStatus("current")


class _HwAtmScramble_Type(TruthValue):
    """Custom type hwAtmScramble based on TruthValue"""


_HwAtmScramble_Object = MibTableColumn
hwAtmScramble = _HwAtmScramble_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 156, 1, 1, 1, 14),
    _HwAtmScramble_Type()
)
hwAtmScramble.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwAtmScramble.setStatus("current")


class _HwAtmLoopback_Type(Integer32):
    """Custom type hwAtmLoopback based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("none", 255),
          ("payload", 3),
          ("remote", 2))
    )


_HwAtmLoopback_Type.__name__ = "Integer32"
_HwAtmLoopback_Object = MibTableColumn
hwAtmLoopback = _HwAtmLoopback_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 156, 1, 1, 1, 15),
    _HwAtmLoopback_Type()
)
hwAtmLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwAtmLoopback.setStatus("current")
_HwAtmMapPvpTable_Object = MibTable
hwAtmMapPvpTable = _HwAtmMapPvpTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 156, 1, 2)
)
if mibBuilder.loadTexts:
    hwAtmMapPvpTable.setStatus("current")
_HwAtmMapPvpEntry_Object = MibTableRow
hwAtmMapPvpEntry = _HwAtmMapPvpEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 156, 1, 2, 1)
)
hwAtmMapPvpEntry.setIndexNames(
    (0, "HUAWEI-ATM-MIB", "hwAtmMapPvpIfIndex"),
    (0, "HUAWEI-ATM-MIB", "hwAtmMapPvpVplVpi"),
)
if mibBuilder.loadTexts:
    hwAtmMapPvpEntry.setStatus("current")
_HwAtmMapPvpIfIndex_Type = InterfaceIndex
_HwAtmMapPvpIfIndex_Object = MibTableColumn
hwAtmMapPvpIfIndex = _HwAtmMapPvpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 156, 1, 2, 1, 1),
    _HwAtmMapPvpIfIndex_Type()
)
hwAtmMapPvpIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwAtmMapPvpIfIndex.setStatus("current")
_HwAtmMapPvpVplVpi_Type = AtmVpIdentifier
_HwAtmMapPvpVplVpi_Object = MibTableColumn
hwAtmMapPvpVplVpi = _HwAtmMapPvpVplVpi_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 156, 1, 2, 1, 2),
    _HwAtmMapPvpVplVpi_Type()
)
hwAtmMapPvpVplVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwAtmMapPvpVplVpi.setStatus("current")
_HwAtmMapPvpRemoteVplVpi_Type = AtmVpIdentifier
_HwAtmMapPvpRemoteVplVpi_Object = MibTableColumn
hwAtmMapPvpRemoteVplVpi = _HwAtmMapPvpRemoteVplVpi_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 156, 1, 2, 1, 11),
    _HwAtmMapPvpRemoteVplVpi_Type()
)
hwAtmMapPvpRemoteVplVpi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAtmMapPvpRemoteVplVpi.setStatus("current")
_HwAtmMapPvpRowStatus_Type = RowStatus
_HwAtmMapPvpRowStatus_Object = MibTableColumn
hwAtmMapPvpRowStatus = _HwAtmMapPvpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 156, 1, 2, 1, 51),
    _HwAtmMapPvpRowStatus_Type()
)
hwAtmMapPvpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAtmMapPvpRowStatus.setStatus("current")
_HwAtmMapPvcTable_Object = MibTable
hwAtmMapPvcTable = _HwAtmMapPvcTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 156, 1, 3)
)
if mibBuilder.loadTexts:
    hwAtmMapPvcTable.setStatus("current")
_HwAtmMapPvcEntry_Object = MibTableRow
hwAtmMapPvcEntry = _HwAtmMapPvcEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 156, 1, 3, 1)
)
hwAtmMapPvcEntry.setIndexNames(
    (0, "HUAWEI-ATM-MIB", "hwAtmVclIfIndex"),
    (0, "HUAWEI-ATM-MIB", "hwAtmVclVpi"),
    (0, "HUAWEI-ATM-MIB", "hwAtmVclVci"),
)
if mibBuilder.loadTexts:
    hwAtmMapPvcEntry.setStatus("current")
_HwAtmMapPvcRemoteVclVci_Type = AtmVcIdentifier
_HwAtmMapPvcRemoteVclVci_Object = MibTableColumn
hwAtmMapPvcRemoteVclVci = _HwAtmMapPvcRemoteVclVci_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 156, 1, 3, 1, 11),
    _HwAtmMapPvcRemoteVclVci_Type()
)
hwAtmMapPvcRemoteVclVci.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAtmMapPvcRemoteVclVci.setStatus("current")
_HwAtmMapPvcRemoteVclVpi_Type = AtmVpIdentifier
_HwAtmMapPvcRemoteVclVpi_Object = MibTableColumn
hwAtmMapPvcRemoteVclVpi = _HwAtmMapPvcRemoteVclVpi_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 156, 1, 3, 1, 12),
    _HwAtmMapPvcRemoteVclVpi_Type()
)
hwAtmMapPvcRemoteVclVpi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAtmMapPvcRemoteVclVpi.setStatus("current")
_HwAtmMapPvcRowStatus_Type = RowStatus
_HwAtmMapPvcRowStatus_Object = MibTableColumn
hwAtmMapPvcRowStatus = _HwAtmMapPvcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 156, 1, 3, 1, 51),
    _HwAtmMapPvcRowStatus_Type()
)
hwAtmMapPvcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAtmMapPvcRowStatus.setStatus("current")
_HwAtmServiceTable_Object = MibTable
hwAtmServiceTable = _HwAtmServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 156, 1, 4)
)
if mibBuilder.loadTexts:
    hwAtmServiceTable.setStatus("current")
_HwAtmServiceEntry_Object = MibTableRow
hwAtmServiceEntry = _HwAtmServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 156, 1, 4, 1)
)
hwAtmServiceEntry.setIndexNames(
    (0, "HUAWEI-ATM-MIB", "hwAtmServiceName"),
)
if mibBuilder.loadTexts:
    hwAtmServiceEntry.setStatus("current")


class _HwAtmServiceName_Type(OctetString):
    """Custom type hwAtmServiceName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwAtmServiceName_Type.__name__ = "OctetString"
_HwAtmServiceName_Object = MibTableColumn
hwAtmServiceName = _HwAtmServiceName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 156, 1, 4, 1, 1),
    _HwAtmServiceName_Type()
)
hwAtmServiceName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwAtmServiceName.setStatus("current")


class _HwAtmServiceType_Type(Integer32):
    """Custom type hwAtmServiceType based on Integer32"""
    defaultValue = 4

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
        *(("cbr", 1),
          ("ubr", 4),
          ("ubrPlus", 5),
          ("vbrNrt", 2),
          ("vbrRt", 3))
    )


_HwAtmServiceType_Type.__name__ = "Integer32"
_HwAtmServiceType_Object = MibTableColumn
hwAtmServiceType = _HwAtmServiceType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 156, 1, 4, 1, 11),
    _HwAtmServiceType_Type()
)
hwAtmServiceType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAtmServiceType.setStatus("current")


class _HwAtmServiceOutputPcr_Type(Integer32):
    """Custom type hwAtmServiceOutputPcr based on Integer32"""
    defaultValue = 149760

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(64, 149760),
    )


_HwAtmServiceOutputPcr_Type.__name__ = "Integer32"
_HwAtmServiceOutputPcr_Object = MibTableColumn
hwAtmServiceOutputPcr = _HwAtmServiceOutputPcr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 156, 1, 4, 1, 12),
    _HwAtmServiceOutputPcr_Type()
)
hwAtmServiceOutputPcr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAtmServiceOutputPcr.setStatus("current")


class _HwAtmServiceOutputScr_Type(Integer32):
    """Custom type hwAtmServiceOutputScr based on Integer32"""
    defaultValue = 149760

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(64, 149760),
    )


_HwAtmServiceOutputScr_Type.__name__ = "Integer32"
_HwAtmServiceOutputScr_Object = MibTableColumn
hwAtmServiceOutputScr = _HwAtmServiceOutputScr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 156, 1, 4, 1, 13),
    _HwAtmServiceOutputScr_Type()
)
hwAtmServiceOutputScr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAtmServiceOutputScr.setStatus("current")


class _HwAtmServiceOutputMbs_Type(Integer32):
    """Custom type hwAtmServiceOutputMbs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 512),
    )


_HwAtmServiceOutputMbs_Type.__name__ = "Integer32"
_HwAtmServiceOutputMbs_Object = MibTableColumn
hwAtmServiceOutputMbs = _HwAtmServiceOutputMbs_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 156, 1, 4, 1, 14),
    _HwAtmServiceOutputMbs_Type()
)
hwAtmServiceOutputMbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAtmServiceOutputMbs.setStatus("current")


class _HwAtmServiceCbrCdvtValue_Type(Integer32):
    """Custom type hwAtmServiceCbrCdvtValue based on Integer32"""
    defaultValue = 500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_HwAtmServiceCbrCdvtValue_Type.__name__ = "Integer32"
_HwAtmServiceCbrCdvtValue_Object = MibTableColumn
hwAtmServiceCbrCdvtValue = _HwAtmServiceCbrCdvtValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 156, 1, 4, 1, 15),
    _HwAtmServiceCbrCdvtValue_Type()
)
hwAtmServiceCbrCdvtValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAtmServiceCbrCdvtValue.setStatus("current")


class _HwAtmServiceOutputMcr_Type(Integer32):
    """Custom type hwAtmServiceOutputMcr based on Integer32"""
    defaultValue = 149760

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(64, 149760),
    )


_HwAtmServiceOutputMcr_Type.__name__ = "Integer32"
_HwAtmServiceOutputMcr_Object = MibTableColumn
hwAtmServiceOutputMcr = _HwAtmServiceOutputMcr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 156, 1, 4, 1, 16),
    _HwAtmServiceOutputMcr_Type()
)
hwAtmServiceOutputMcr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAtmServiceOutputMcr.setStatus("current")
_HwAtmServiceRowStatus_Type = RowStatus
_HwAtmServiceRowStatus_Object = MibTableColumn
hwAtmServiceRowStatus = _HwAtmServiceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 156, 1, 4, 1, 51),
    _HwAtmServiceRowStatus_Type()
)
hwAtmServiceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAtmServiceRowStatus.setStatus("current")
_HwAtmPvcServiceTable_Object = MibTable
hwAtmPvcServiceTable = _HwAtmPvcServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 156, 1, 5)
)
if mibBuilder.loadTexts:
    hwAtmPvcServiceTable.setStatus("current")
_HwAtmPvcServiceEntry_Object = MibTableRow
hwAtmPvcServiceEntry = _HwAtmPvcServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 156, 1, 5, 1)
)
hwAtmPvcServiceEntry.setIndexNames(
    (0, "HUAWEI-ATM-MIB", "hwAtmVclIfIndex"),
    (0, "HUAWEI-ATM-MIB", "hwAtmVclVpi"),
    (0, "HUAWEI-ATM-MIB", "hwAtmVclVci"),
)
if mibBuilder.loadTexts:
    hwAtmPvcServiceEntry.setStatus("current")


class _HwAtmPvcServiceName_Type(OctetString):
    """Custom type hwAtmPvcServiceName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwAtmPvcServiceName_Type.__name__ = "OctetString"
_HwAtmPvcServiceName_Object = MibTableColumn
hwAtmPvcServiceName = _HwAtmPvcServiceName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 156, 1, 5, 1, 11),
    _HwAtmPvcServiceName_Type()
)
hwAtmPvcServiceName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAtmPvcServiceName.setStatus("current")


class _HwAtmPvcTransmittalDirection_Type(Integer32):
    """Custom type hwAtmPvcTransmittalDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("input", 1),
          ("output", 2))
    )


_HwAtmPvcTransmittalDirection_Type.__name__ = "Integer32"
_HwAtmPvcTransmittalDirection_Object = MibTableColumn
hwAtmPvcTransmittalDirection = _HwAtmPvcTransmittalDirection_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 156, 1, 5, 1, 21),
    _HwAtmPvcTransmittalDirection_Type()
)
hwAtmPvcTransmittalDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAtmPvcTransmittalDirection.setStatus("current")
_HwAtmPvcServiceRowStatus_Type = RowStatus
_HwAtmPvcServiceRowStatus_Object = MibTableColumn
hwAtmPvcServiceRowStatus = _HwAtmPvcServiceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 156, 1, 5, 1, 51),
    _HwAtmPvcServiceRowStatus_Type()
)
hwAtmPvcServiceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAtmPvcServiceRowStatus.setStatus("current")
_HwAtmIfConfTable_Object = MibTable
hwAtmIfConfTable = _HwAtmIfConfTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 156, 1, 11)
)
if mibBuilder.loadTexts:
    hwAtmIfConfTable.setStatus("current")
_HwAtmIfConfEntry_Object = MibTableRow
hwAtmIfConfEntry = _HwAtmIfConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 156, 1, 11, 1)
)
hwAtmIfConfEntry.setIndexNames(
    (0, "HUAWEI-ATM-MIB", "hwAtmIfConfIfIndex"),
)
if mibBuilder.loadTexts:
    hwAtmIfConfEntry.setStatus("current")
_HwAtmIfConfIfIndex_Type = InterfaceIndex
_HwAtmIfConfIfIndex_Object = MibTableColumn
hwAtmIfConfIfIndex = _HwAtmIfConfIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 156, 1, 11, 1, 1),
    _HwAtmIfConfIfIndex_Type()
)
hwAtmIfConfIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwAtmIfConfIfIndex.setStatus("current")


class _HwAtmIfConfMaxVccs_Type(Integer32):
    """Custom type hwAtmIfConfMaxVccs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2048),
    )


_HwAtmIfConfMaxVccs_Type.__name__ = "Integer32"
_HwAtmIfConfMaxVccs_Object = MibTableColumn
hwAtmIfConfMaxVccs = _HwAtmIfConfMaxVccs_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 156, 1, 11, 1, 11),
    _HwAtmIfConfMaxVccs_Type()
)
hwAtmIfConfMaxVccs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwAtmIfConfMaxVccs.setStatus("current")
_HwAtmIfConfOperVccs_Type = Integer32
_HwAtmIfConfOperVccs_Object = MibTableColumn
hwAtmIfConfOperVccs = _HwAtmIfConfOperVccs_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 156, 1, 11, 1, 12),
    _HwAtmIfConfOperVccs_Type()
)
hwAtmIfConfOperVccs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAtmIfConfOperVccs.setStatus("current")


class _HwAtmIfConfIntfType_Type(Integer32):
    """Custom type hwAtmIfConfIntfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nni", 2),
          ("uni", 1))
    )


_HwAtmIfConfIntfType_Type.__name__ = "Integer32"
_HwAtmIfConfIntfType_Object = MibTableColumn
hwAtmIfConfIntfType = _HwAtmIfConfIntfType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 156, 1, 11, 1, 13),
    _HwAtmIfConfIntfType_Type()
)
hwAtmIfConfIntfType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwAtmIfConfIntfType.setStatus("current")
_HwAtmVplTable_Object = MibTable
hwAtmVplTable = _HwAtmVplTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 156, 1, 12)
)
if mibBuilder.loadTexts:
    hwAtmVplTable.setStatus("current")
_HwAtmVplEntry_Object = MibTableRow
hwAtmVplEntry = _HwAtmVplEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 156, 1, 12, 1)
)
hwAtmVplEntry.setIndexNames(
    (0, "HUAWEI-ATM-MIB", "hwAtmVplIfIndex"),
    (0, "HUAWEI-ATM-MIB", "hwAtmVplVpi"),
)
if mibBuilder.loadTexts:
    hwAtmVplEntry.setStatus("current")
_HwAtmVplIfIndex_Type = InterfaceIndex
_HwAtmVplIfIndex_Object = MibTableColumn
hwAtmVplIfIndex = _HwAtmVplIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 156, 1, 12, 1, 1),
    _HwAtmVplIfIndex_Type()
)
hwAtmVplIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwAtmVplIfIndex.setStatus("current")
_HwAtmVplVpi_Type = AtmVpIdentifier
_HwAtmVplVpi_Object = MibTableColumn
hwAtmVplVpi = _HwAtmVplVpi_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 156, 1, 12, 1, 2),
    _HwAtmVplVpi_Type()
)
hwAtmVplVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwAtmVplVpi.setStatus("current")
_HwAtmVplRowStatus_Type = RowStatus
_HwAtmVplRowStatus_Object = MibTableColumn
hwAtmVplRowStatus = _HwAtmVplRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 156, 1, 12, 1, 51),
    _HwAtmVplRowStatus_Type()
)
hwAtmVplRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAtmVplRowStatus.setStatus("current")
_HwAtmVclTable_Object = MibTable
hwAtmVclTable = _HwAtmVclTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 156, 1, 13)
)
if mibBuilder.loadTexts:
    hwAtmVclTable.setStatus("current")
_HwAtmVclEntry_Object = MibTableRow
hwAtmVclEntry = _HwAtmVclEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 156, 1, 13, 1)
)
hwAtmVclEntry.setIndexNames(
    (0, "HUAWEI-ATM-MIB", "hwAtmVclIfIndex"),
    (0, "HUAWEI-ATM-MIB", "hwAtmVclVpi"),
    (0, "HUAWEI-ATM-MIB", "hwAtmVclVci"),
)
if mibBuilder.loadTexts:
    hwAtmVclEntry.setStatus("current")
_HwAtmVclIfIndex_Type = InterfaceIndex
_HwAtmVclIfIndex_Object = MibTableColumn
hwAtmVclIfIndex = _HwAtmVclIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 156, 1, 13, 1, 1),
    _HwAtmVclIfIndex_Type()
)
hwAtmVclIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwAtmVclIfIndex.setStatus("current")
_HwAtmVclVpi_Type = AtmVpIdentifier
_HwAtmVclVpi_Object = MibTableColumn
hwAtmVclVpi = _HwAtmVclVpi_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 156, 1, 13, 1, 2),
    _HwAtmVclVpi_Type()
)
hwAtmVclVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwAtmVclVpi.setStatus("current")
_HwAtmVclVci_Type = AtmVcIdentifier
_HwAtmVclVci_Object = MibTableColumn
hwAtmVclVci = _HwAtmVclVci_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 156, 1, 13, 1, 3),
    _HwAtmVclVci_Type()
)
hwAtmVclVci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwAtmVclVci.setStatus("current")


class _HwAtmVclName_Type(OctetString):
    """Custom type hwAtmVclName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_HwAtmVclName_Type.__name__ = "OctetString"
_HwAtmVclName_Object = MibTableColumn
hwAtmVclName = _HwAtmVclName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 156, 1, 13, 1, 11),
    _HwAtmVclName_Type()
)
hwAtmVclName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAtmVclName.setStatus("current")


class _HwAtmVccAal5EncapsType_Type(Integer32):
    """Custom type hwAtmVccAal5EncapsType based on Integer32"""

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
        *(("aal5Mux", 2),
          ("aal5MuxNonstandard", 3),
          ("aal5Nlpid", 4),
          ("aal5Snap", 1))
    )


_HwAtmVccAal5EncapsType_Type.__name__ = "Integer32"
_HwAtmVccAal5EncapsType_Object = MibTableColumn
hwAtmVccAal5EncapsType = _HwAtmVccAal5EncapsType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 156, 1, 13, 1, 12),
    _HwAtmVccAal5EncapsType_Type()
)
hwAtmVccAal5EncapsType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAtmVccAal5EncapsType.setStatus("current")
_HwAtmVclRowStatus_Type = RowStatus
_HwAtmVclRowStatus_Object = MibTableColumn
hwAtmVclRowStatus = _HwAtmVclRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 156, 1, 13, 1, 51),
    _HwAtmVclRowStatus_Type()
)
hwAtmVclRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAtmVclRowStatus.setStatus("current")
_HwAtmPvcIpoaTable_Object = MibTable
hwAtmPvcIpoaTable = _HwAtmPvcIpoaTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 156, 1, 14)
)
if mibBuilder.loadTexts:
    hwAtmPvcIpoaTable.setStatus("current")
_HwAtmPvcIpoaEntry_Object = MibTableRow
hwAtmPvcIpoaEntry = _HwAtmPvcIpoaEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 156, 1, 14, 1)
)
hwAtmPvcIpoaEntry.setIndexNames(
    (0, "HUAWEI-ATM-MIB", "hwAtmVclIfIndex"),
    (0, "HUAWEI-ATM-MIB", "hwAtmVclVpi"),
    (0, "HUAWEI-ATM-MIB", "hwAtmVclVci"),
    (0, "HUAWEI-ATM-MIB", "hwAtmPvcIpoaType"),
    (0, "HUAWEI-ATM-MIB", "hwAtmPvcIpoaIpAddress"),
)
if mibBuilder.loadTexts:
    hwAtmPvcIpoaEntry.setStatus("current")


class _HwAtmPvcIpoaType_Type(Integer32):
    """Custom type hwAtmPvcIpoaType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("default", 2),
          ("inarp", 3),
          ("ip", 1))
    )


_HwAtmPvcIpoaType_Type.__name__ = "Integer32"
_HwAtmPvcIpoaType_Object = MibTableColumn
hwAtmPvcIpoaType = _HwAtmPvcIpoaType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 156, 1, 14, 1, 3),
    _HwAtmPvcIpoaType_Type()
)
hwAtmPvcIpoaType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwAtmPvcIpoaType.setStatus("current")
_HwAtmPvcIpoaIpAddress_Type = IpAddress
_HwAtmPvcIpoaIpAddress_Object = MibTableColumn
hwAtmPvcIpoaIpAddress = _HwAtmPvcIpoaIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 156, 1, 14, 1, 4),
    _HwAtmPvcIpoaIpAddress_Type()
)
hwAtmPvcIpoaIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwAtmPvcIpoaIpAddress.setStatus("current")
_HwAtmPvcIpoaIpMask_Type = IpAddress
_HwAtmPvcIpoaIpMask_Object = MibTableColumn
hwAtmPvcIpoaIpMask = _HwAtmPvcIpoaIpMask_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 156, 1, 14, 1, 11),
    _HwAtmPvcIpoaIpMask_Type()
)
hwAtmPvcIpoaIpMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAtmPvcIpoaIpMask.setStatus("current")


class _HwAtmPvcIpoaInarpInterval_Type(Integer32):
    """Custom type hwAtmPvcIpoaInarpInterval based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 600),
    )


_HwAtmPvcIpoaInarpInterval_Type.__name__ = "Integer32"
_HwAtmPvcIpoaInarpInterval_Object = MibTableColumn
hwAtmPvcIpoaInarpInterval = _HwAtmPvcIpoaInarpInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 156, 1, 14, 1, 12),
    _HwAtmPvcIpoaInarpInterval_Type()
)
hwAtmPvcIpoaInarpInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAtmPvcIpoaInarpInterval.setStatus("current")


class _HwAtmPvcIpoaBroadcast_Type(TruthValue):
    """Custom type hwAtmPvcIpoaBroadcast based on TruthValue"""


_HwAtmPvcIpoaBroadcast_Object = MibTableColumn
hwAtmPvcIpoaBroadcast = _HwAtmPvcIpoaBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 156, 1, 14, 1, 13),
    _HwAtmPvcIpoaBroadcast_Type()
)
hwAtmPvcIpoaBroadcast.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAtmPvcIpoaBroadcast.setStatus("current")
_HwAtmPvcIpoaRowStatus_Type = RowStatus
_HwAtmPvcIpoaRowStatus_Object = MibTableColumn
hwAtmPvcIpoaRowStatus = _HwAtmPvcIpoaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 156, 1, 14, 1, 51),
    _HwAtmPvcIpoaRowStatus_Type()
)
hwAtmPvcIpoaRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAtmPvcIpoaRowStatus.setStatus("current")
_HwAtmPvcBridgeTable_Object = MibTable
hwAtmPvcBridgeTable = _HwAtmPvcBridgeTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 156, 1, 15)
)
if mibBuilder.loadTexts:
    hwAtmPvcBridgeTable.setStatus("current")
_HwAtmPvcBridgeEntry_Object = MibTableRow
hwAtmPvcBridgeEntry = _HwAtmPvcBridgeEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 156, 1, 15, 1)
)
hwAtmPvcBridgeEntry.setIndexNames(
    (0, "HUAWEI-ATM-MIB", "hwAtmVclIfIndex"),
    (0, "HUAWEI-ATM-MIB", "hwAtmVclVpi"),
    (0, "HUAWEI-ATM-MIB", "hwAtmVclVci"),
)
if mibBuilder.loadTexts:
    hwAtmPvcBridgeEntry.setStatus("current")
_HwAtmPvcBridgeDstIfIndex_Type = InterfaceIndex
_HwAtmPvcBridgeDstIfIndex_Object = MibTableColumn
hwAtmPvcBridgeDstIfIndex = _HwAtmPvcBridgeDstIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 156, 1, 15, 1, 11),
    _HwAtmPvcBridgeDstIfIndex_Type()
)
hwAtmPvcBridgeDstIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAtmPvcBridgeDstIfIndex.setStatus("current")
_HwAtmPvcBridgeRowStatus_Type = RowStatus
_HwAtmPvcBridgeRowStatus_Object = MibTableColumn
hwAtmPvcBridgeRowStatus = _HwAtmPvcBridgeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 156, 1, 15, 1, 51),
    _HwAtmPvcBridgeRowStatus_Type()
)
hwAtmPvcBridgeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAtmPvcBridgeRowStatus.setStatus("current")
_HwAtmPvcOamLoopbackTable_Object = MibTable
hwAtmPvcOamLoopbackTable = _HwAtmPvcOamLoopbackTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 156, 1, 17)
)
if mibBuilder.loadTexts:
    hwAtmPvcOamLoopbackTable.setStatus("current")
_HwAtmPvcOAMLoopbackEntry_Object = MibTableRow
hwAtmPvcOAMLoopbackEntry = _HwAtmPvcOAMLoopbackEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 156, 1, 17, 1)
)
hwAtmPvcOAMLoopbackEntry.setIndexNames(
    (0, "HUAWEI-ATM-MIB", "hwAtmVclIfIndex"),
    (0, "HUAWEI-ATM-MIB", "hwAtmVclVpi"),
    (0, "HUAWEI-ATM-MIB", "hwAtmVclVci"),
)
if mibBuilder.loadTexts:
    hwAtmPvcOAMLoopbackEntry.setStatus("current")


class _HwAtmPvcOAMLoopbackFrequency_Type(Integer32):
    """Custom type hwAtmPvcOAMLoopbackFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_HwAtmPvcOAMLoopbackFrequency_Type.__name__ = "Integer32"
_HwAtmPvcOAMLoopbackFrequency_Object = MibTableColumn
hwAtmPvcOAMLoopbackFrequency = _HwAtmPvcOAMLoopbackFrequency_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 156, 1, 17, 1, 11),
    _HwAtmPvcOAMLoopbackFrequency_Type()
)
hwAtmPvcOAMLoopbackFrequency.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAtmPvcOAMLoopbackFrequency.setStatus("current")


class _HwAtmPvcOAMLoopbackUpCount_Type(Integer32):
    """Custom type hwAtmPvcOAMLoopbackUpCount based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_HwAtmPvcOAMLoopbackUpCount_Type.__name__ = "Integer32"
_HwAtmPvcOAMLoopbackUpCount_Object = MibTableColumn
hwAtmPvcOAMLoopbackUpCount = _HwAtmPvcOAMLoopbackUpCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 156, 1, 17, 1, 12),
    _HwAtmPvcOAMLoopbackUpCount_Type()
)
hwAtmPvcOAMLoopbackUpCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAtmPvcOAMLoopbackUpCount.setStatus("current")


class _HwAtmPvcOAMLoopbackDownCount_Type(Integer32):
    """Custom type hwAtmPvcOAMLoopbackDownCount based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_HwAtmPvcOAMLoopbackDownCount_Type.__name__ = "Integer32"
_HwAtmPvcOAMLoopbackDownCount_Object = MibTableColumn
hwAtmPvcOAMLoopbackDownCount = _HwAtmPvcOAMLoopbackDownCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 156, 1, 17, 1, 13),
    _HwAtmPvcOAMLoopbackDownCount_Type()
)
hwAtmPvcOAMLoopbackDownCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAtmPvcOAMLoopbackDownCount.setStatus("current")


class _HwAtmPvcOAMLoopbackRetryFrequency_Type(Integer32):
    """Custom type hwAtmPvcOAMLoopbackRetryFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_HwAtmPvcOAMLoopbackRetryFrequency_Type.__name__ = "Integer32"
_HwAtmPvcOAMLoopbackRetryFrequency_Object = MibTableColumn
hwAtmPvcOAMLoopbackRetryFrequency = _HwAtmPvcOAMLoopbackRetryFrequency_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 156, 1, 17, 1, 14),
    _HwAtmPvcOAMLoopbackRetryFrequency_Type()
)
hwAtmPvcOAMLoopbackRetryFrequency.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAtmPvcOAMLoopbackRetryFrequency.setStatus("current")
_HwAtmPvcOAMLoopbackRowStatus_Type = RowStatus
_HwAtmPvcOAMLoopbackRowStatus_Object = MibTableColumn
hwAtmPvcOAMLoopbackRowStatus = _HwAtmPvcOAMLoopbackRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 156, 1, 17, 1, 51),
    _HwAtmPvcOAMLoopbackRowStatus_Type()
)
hwAtmPvcOAMLoopbackRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAtmPvcOAMLoopbackRowStatus.setStatus("current")
_HwAtmPvpLimitTable_Object = MibTable
hwAtmPvpLimitTable = _HwAtmPvpLimitTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 156, 1, 18)
)
if mibBuilder.loadTexts:
    hwAtmPvpLimitTable.setStatus("current")
_HwAtmPvpLimitEntry_Object = MibTableRow
hwAtmPvpLimitEntry = _HwAtmPvpLimitEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 156, 1, 18, 1)
)
hwAtmPvpLimitEntry.setIndexNames(
    (0, "HUAWEI-ATM-MIB", "hwAtmPvpLimitIfIndex"),
    (0, "HUAWEI-ATM-MIB", "hwAtmPvpLimitVpi"),
)
if mibBuilder.loadTexts:
    hwAtmPvpLimitEntry.setStatus("current")
_HwAtmPvpLimitIfIndex_Type = InterfaceIndex
_HwAtmPvpLimitIfIndex_Object = MibTableColumn
hwAtmPvpLimitIfIndex = _HwAtmPvpLimitIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 156, 1, 18, 1, 1),
    _HwAtmPvpLimitIfIndex_Type()
)
hwAtmPvpLimitIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwAtmPvpLimitIfIndex.setStatus("current")
_HwAtmPvpLimitVpi_Type = AtmVpIdentifier
_HwAtmPvpLimitVpi_Object = MibTableColumn
hwAtmPvpLimitVpi = _HwAtmPvpLimitVpi_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 156, 1, 18, 1, 2),
    _HwAtmPvpLimitVpi_Type()
)
hwAtmPvpLimitVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwAtmPvpLimitVpi.setStatus("current")
_HwAtmPvpLimitPeakRate_Type = Integer32
_HwAtmPvpLimitPeakRate_Object = MibTableColumn
hwAtmPvpLimitPeakRate = _HwAtmPvpLimitPeakRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 156, 1, 18, 1, 11),
    _HwAtmPvpLimitPeakRate_Type()
)
hwAtmPvpLimitPeakRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAtmPvpLimitPeakRate.setStatus("current")
_HwAtmPvpLimitRowStatus_Type = RowStatus
_HwAtmPvpLimitRowStatus_Object = MibTableColumn
hwAtmPvpLimitRowStatus = _HwAtmPvpLimitRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 156, 1, 18, 1, 51),
    _HwAtmPvpLimitRowStatus_Type()
)
hwAtmPvpLimitRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAtmPvpLimitRowStatus.setStatus("current")
_HwAtmConformance_ObjectIdentity = ObjectIdentity
hwAtmConformance = _HwAtmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 156, 11)
)
_HwAtmCompliances_ObjectIdentity = ObjectIdentity
hwAtmCompliances = _HwAtmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 156, 11, 1)
)
_HwAtmGroups_ObjectIdentity = ObjectIdentity
hwAtmGroups = _HwAtmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 156, 11, 2)
)

# Managed Objects groups

hwAtmObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 156, 11, 2, 1)
)
hwAtmObjectGroup.setObjects(
      *(("HUAWEI-ATM-MIB", "hwAtmIfType"),
        ("HUAWEI-ATM-MIB", "hwAtmClock"),
        ("HUAWEI-ATM-MIB", "hwAtmFrameFormat"),
        ("HUAWEI-ATM-MIB", "hwAtmScramble"),
        ("HUAWEI-ATM-MIB", "hwAtmLoopback"))
)
if mibBuilder.loadTexts:
    hwAtmObjectGroup.setStatus("current")

hwAtmIfConf = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 156, 11, 2, 2)
)
hwAtmIfConf.setObjects(
      *(("HUAWEI-ATM-MIB", "hwAtmIfConfMaxVccs"),
        ("HUAWEI-ATM-MIB", "hwAtmIfConfOperVccs"),
        ("HUAWEI-ATM-MIB", "hwAtmIfConfIntfType"))
)
if mibBuilder.loadTexts:
    hwAtmIfConf.setStatus("current")

hwAtmVplObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 156, 11, 2, 3)
)
hwAtmVplObjectGroup.setObjects(
      *(("HUAWEI-ATM-MIB", "hwAtmPvcBridgeDstIfIndex"),
        ("HUAWEI-ATM-MIB", "hwAtmPvcBridgeRowStatus"))
)
if mibBuilder.loadTexts:
    hwAtmVplObjectGroup.setStatus("current")

hwAtmVclObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 156, 11, 2, 4)
)
hwAtmVclObjectGroup.setObjects(
      *(("HUAWEI-ATM-MIB", "hwAtmVclName"),
        ("HUAWEI-ATM-MIB", "hwAtmVccAal5EncapsType"),
        ("HUAWEI-ATM-MIB", "hwAtmVclRowStatus"))
)
if mibBuilder.loadTexts:
    hwAtmVclObjectGroup.setStatus("current")

hwAtmMapPvpObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 156, 11, 2, 5)
)
hwAtmMapPvpObjectGroup.setObjects(
      *(("HUAWEI-ATM-MIB", "hwAtmMapPvpRemoteVplVpi"),
        ("HUAWEI-ATM-MIB", "hwAtmMapPvpRowStatus"))
)
if mibBuilder.loadTexts:
    hwAtmMapPvpObjectGroup.setStatus("current")

hwAtmMapPvcObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 156, 11, 2, 6)
)
hwAtmMapPvcObjectGroup.setObjects(
      *(("HUAWEI-ATM-MIB", "hwAtmMapPvcRemoteVclVpi"),
        ("HUAWEI-ATM-MIB", "hwAtmMapPvcRemoteVclVci"),
        ("HUAWEI-ATM-MIB", "hwAtmMapPvcRowStatus"))
)
if mibBuilder.loadTexts:
    hwAtmMapPvcObjectGroup.setStatus("current")

hwAtmServiceObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 156, 11, 2, 7)
)
hwAtmServiceObjectGroup.setObjects(
      *(("HUAWEI-ATM-MIB", "hwAtmServiceType"),
        ("HUAWEI-ATM-MIB", "hwAtmServiceOutputPcr"),
        ("HUAWEI-ATM-MIB", "hwAtmServiceOutputScr"),
        ("HUAWEI-ATM-MIB", "hwAtmServiceOutputMbs"),
        ("HUAWEI-ATM-MIB", "hwAtmServiceCbrCdvtValue"),
        ("HUAWEI-ATM-MIB", "hwAtmServiceOutputMcr"),
        ("HUAWEI-ATM-MIB", "hwAtmServiceRowStatus"))
)
if mibBuilder.loadTexts:
    hwAtmServiceObjectGroup.setStatus("current")

hwAtmPvcServiceObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 156, 11, 2, 8)
)
hwAtmPvcServiceObjectGroup.setObjects(
      *(("HUAWEI-ATM-MIB", "hwAtmPvcServiceName"),
        ("HUAWEI-ATM-MIB", "hwAtmPvcTransmittalDirection"),
        ("HUAWEI-ATM-MIB", "hwAtmPvcServiceRowStatus"))
)
if mibBuilder.loadTexts:
    hwAtmPvcServiceObjectGroup.setStatus("current")

hwAtmPvcIpoaObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 156, 11, 2, 9)
)
hwAtmPvcIpoaObjectGroup.setObjects(
      *(("HUAWEI-ATM-MIB", "hwAtmPvcIpoaIpMask"),
        ("HUAWEI-ATM-MIB", "hwAtmPvcIpoaInarpInterval"),
        ("HUAWEI-ATM-MIB", "hwAtmPvcIpoaBroadcast"),
        ("HUAWEI-ATM-MIB", "hwAtmPvcIpoaRowStatus"))
)
if mibBuilder.loadTexts:
    hwAtmPvcIpoaObjectGroup.setStatus("current")

hwAtmPvcBridgeObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 156, 11, 2, 10)
)
hwAtmPvcBridgeObjectGroup.setObjects(
    ("HUAWEI-ATM-MIB", "hwAtmVplRowStatus")
)
if mibBuilder.loadTexts:
    hwAtmPvcBridgeObjectGroup.setStatus("current")

hwAtmPvcOAMLoopbackObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 156, 11, 2, 11)
)
hwAtmPvcOAMLoopbackObjectGroup.setObjects(
      *(("HUAWEI-ATM-MIB", "hwAtmPvcOAMLoopbackFrequency"),
        ("HUAWEI-ATM-MIB", "hwAtmPvcOAMLoopbackUpCount"),
        ("HUAWEI-ATM-MIB", "hwAtmPvcOAMLoopbackDownCount"),
        ("HUAWEI-ATM-MIB", "hwAtmPvcOAMLoopbackRetryFrequency"),
        ("HUAWEI-ATM-MIB", "hwAtmPvcOAMLoopbackRowStatus"))
)
if mibBuilder.loadTexts:
    hwAtmPvcOAMLoopbackObjectGroup.setStatus("current")

hwAtmPvpLimitObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 156, 11, 2, 12)
)
hwAtmPvpLimitObjectGroup.setObjects(
      *(("HUAWEI-ATM-MIB", "hwAtmPvpLimitPeakRate"),
        ("HUAWEI-ATM-MIB", "hwAtmPvpLimitRowStatus"))
)
if mibBuilder.loadTexts:
    hwAtmPvpLimitObjectGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hwAtmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 156, 11, 1, 1)
)
if mibBuilder.loadTexts:
    hwAtmCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-ATM-MIB",
    **{"hwAtmMIB": hwAtmMIB,
       "hwAtmObjects": hwAtmObjects,
       "hwAtmTable": hwAtmTable,
       "hwAtmEntry": hwAtmEntry,
       "hwAtmIfIndex": hwAtmIfIndex,
       "hwAtmIfType": hwAtmIfType,
       "hwAtmClock": hwAtmClock,
       "hwAtmFrameFormat": hwAtmFrameFormat,
       "hwAtmScramble": hwAtmScramble,
       "hwAtmLoopback": hwAtmLoopback,
       "hwAtmMapPvpTable": hwAtmMapPvpTable,
       "hwAtmMapPvpEntry": hwAtmMapPvpEntry,
       "hwAtmMapPvpIfIndex": hwAtmMapPvpIfIndex,
       "hwAtmMapPvpVplVpi": hwAtmMapPvpVplVpi,
       "hwAtmMapPvpRemoteVplVpi": hwAtmMapPvpRemoteVplVpi,
       "hwAtmMapPvpRowStatus": hwAtmMapPvpRowStatus,
       "hwAtmMapPvcTable": hwAtmMapPvcTable,
       "hwAtmMapPvcEntry": hwAtmMapPvcEntry,
       "hwAtmMapPvcRemoteVclVci": hwAtmMapPvcRemoteVclVci,
       "hwAtmMapPvcRemoteVclVpi": hwAtmMapPvcRemoteVclVpi,
       "hwAtmMapPvcRowStatus": hwAtmMapPvcRowStatus,
       "hwAtmServiceTable": hwAtmServiceTable,
       "hwAtmServiceEntry": hwAtmServiceEntry,
       "hwAtmServiceName": hwAtmServiceName,
       "hwAtmServiceType": hwAtmServiceType,
       "hwAtmServiceOutputPcr": hwAtmServiceOutputPcr,
       "hwAtmServiceOutputScr": hwAtmServiceOutputScr,
       "hwAtmServiceOutputMbs": hwAtmServiceOutputMbs,
       "hwAtmServiceCbrCdvtValue": hwAtmServiceCbrCdvtValue,
       "hwAtmServiceOutputMcr": hwAtmServiceOutputMcr,
       "hwAtmServiceRowStatus": hwAtmServiceRowStatus,
       "hwAtmPvcServiceTable": hwAtmPvcServiceTable,
       "hwAtmPvcServiceEntry": hwAtmPvcServiceEntry,
       "hwAtmPvcServiceName": hwAtmPvcServiceName,
       "hwAtmPvcTransmittalDirection": hwAtmPvcTransmittalDirection,
       "hwAtmPvcServiceRowStatus": hwAtmPvcServiceRowStatus,
       "hwAtmIfConfTable": hwAtmIfConfTable,
       "hwAtmIfConfEntry": hwAtmIfConfEntry,
       "hwAtmIfConfIfIndex": hwAtmIfConfIfIndex,
       "hwAtmIfConfMaxVccs": hwAtmIfConfMaxVccs,
       "hwAtmIfConfOperVccs": hwAtmIfConfOperVccs,
       "hwAtmIfConfIntfType": hwAtmIfConfIntfType,
       "hwAtmVplTable": hwAtmVplTable,
       "hwAtmVplEntry": hwAtmVplEntry,
       "hwAtmVplIfIndex": hwAtmVplIfIndex,
       "hwAtmVplVpi": hwAtmVplVpi,
       "hwAtmVplRowStatus": hwAtmVplRowStatus,
       "hwAtmVclTable": hwAtmVclTable,
       "hwAtmVclEntry": hwAtmVclEntry,
       "hwAtmVclIfIndex": hwAtmVclIfIndex,
       "hwAtmVclVpi": hwAtmVclVpi,
       "hwAtmVclVci": hwAtmVclVci,
       "hwAtmVclName": hwAtmVclName,
       "hwAtmVccAal5EncapsType": hwAtmVccAal5EncapsType,
       "hwAtmVclRowStatus": hwAtmVclRowStatus,
       "hwAtmPvcIpoaTable": hwAtmPvcIpoaTable,
       "hwAtmPvcIpoaEntry": hwAtmPvcIpoaEntry,
       "hwAtmPvcIpoaType": hwAtmPvcIpoaType,
       "hwAtmPvcIpoaIpAddress": hwAtmPvcIpoaIpAddress,
       "hwAtmPvcIpoaIpMask": hwAtmPvcIpoaIpMask,
       "hwAtmPvcIpoaInarpInterval": hwAtmPvcIpoaInarpInterval,
       "hwAtmPvcIpoaBroadcast": hwAtmPvcIpoaBroadcast,
       "hwAtmPvcIpoaRowStatus": hwAtmPvcIpoaRowStatus,
       "hwAtmPvcBridgeTable": hwAtmPvcBridgeTable,
       "hwAtmPvcBridgeEntry": hwAtmPvcBridgeEntry,
       "hwAtmPvcBridgeDstIfIndex": hwAtmPvcBridgeDstIfIndex,
       "hwAtmPvcBridgeRowStatus": hwAtmPvcBridgeRowStatus,
       "hwAtmPvcOamLoopbackTable": hwAtmPvcOamLoopbackTable,
       "hwAtmPvcOAMLoopbackEntry": hwAtmPvcOAMLoopbackEntry,
       "hwAtmPvcOAMLoopbackFrequency": hwAtmPvcOAMLoopbackFrequency,
       "hwAtmPvcOAMLoopbackUpCount": hwAtmPvcOAMLoopbackUpCount,
       "hwAtmPvcOAMLoopbackDownCount": hwAtmPvcOAMLoopbackDownCount,
       "hwAtmPvcOAMLoopbackRetryFrequency": hwAtmPvcOAMLoopbackRetryFrequency,
       "hwAtmPvcOAMLoopbackRowStatus": hwAtmPvcOAMLoopbackRowStatus,
       "hwAtmPvpLimitTable": hwAtmPvpLimitTable,
       "hwAtmPvpLimitEntry": hwAtmPvpLimitEntry,
       "hwAtmPvpLimitIfIndex": hwAtmPvpLimitIfIndex,
       "hwAtmPvpLimitVpi": hwAtmPvpLimitVpi,
       "hwAtmPvpLimitPeakRate": hwAtmPvpLimitPeakRate,
       "hwAtmPvpLimitRowStatus": hwAtmPvpLimitRowStatus,
       "hwAtmConformance": hwAtmConformance,
       "hwAtmCompliances": hwAtmCompliances,
       "hwAtmCompliance": hwAtmCompliance,
       "hwAtmGroups": hwAtmGroups,
       "hwAtmObjectGroup": hwAtmObjectGroup,
       "hwAtmIfConf": hwAtmIfConf,
       "hwAtmVplObjectGroup": hwAtmVplObjectGroup,
       "hwAtmVclObjectGroup": hwAtmVclObjectGroup,
       "hwAtmMapPvpObjectGroup": hwAtmMapPvpObjectGroup,
       "hwAtmMapPvcObjectGroup": hwAtmMapPvcObjectGroup,
       "hwAtmServiceObjectGroup": hwAtmServiceObjectGroup,
       "hwAtmPvcServiceObjectGroup": hwAtmPvcServiceObjectGroup,
       "hwAtmPvcIpoaObjectGroup": hwAtmPvcIpoaObjectGroup,
       "hwAtmPvcBridgeObjectGroup": hwAtmPvcBridgeObjectGroup,
       "hwAtmPvcOAMLoopbackObjectGroup": hwAtmPvcOAMLoopbackObjectGroup,
       "hwAtmPvpLimitObjectGroup": hwAtmPvpLimitObjectGroup}
)
