# SNMP MIB module (BIANCA-BRICK-ATM2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BIANCA-BRICK-ATM2-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:47:21 2024
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
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Bintec_ObjectIdentity = ObjectIdentity
bintec = _Bintec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272)
)
_Bibo_ObjectIdentity = ObjectIdentity
bibo = _Bibo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272, 4)
)
_Atm_ObjectIdentity = ObjectIdentity
atm = _Atm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272, 4, 16)
)
_AtmIfTable_Object = MibTable
atmIfTable = _AtmIfTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 10)
)
if mibBuilder.loadTexts:
    atmIfTable.setStatus("mandatory")
_AtmIfEntry_Object = MibTableRow
atmIfEntry = _AtmIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 10, 1)
)
atmIfEntry.setIndexNames(
    (0, "BIANCA-BRICK-ATM2-MIB", "atmIfIndex"),
)
if mibBuilder.loadTexts:
    atmIfEntry.setStatus("mandatory")
_AtmIfIndex_Type = Integer32
_AtmIfIndex_Object = MibTableColumn
atmIfIndex = _AtmIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 10, 1, 1),
    _AtmIfIndex_Type()
)
atmIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfIndex.setStatus("mandatory")


class _AtmIfType_Type(Integer32):
    """Custom type atmIfType based on Integer32"""
    defaultValue = 1

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
        *(("adsl", 2),
          ("other", 1),
          ("shdsl", 3),
          ("vdsl", 4))
    )


_AtmIfType_Type.__name__ = "Integer32"
_AtmIfType_Object = MibTableColumn
atmIfType = _AtmIfType_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 10, 1, 2),
    _AtmIfType_Type()
)
atmIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfType.setStatus("mandatory")
_AtmIfDescr_Type = DisplayString
_AtmIfDescr_Object = MibTableColumn
atmIfDescr = _AtmIfDescr_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 10, 1, 3),
    _AtmIfDescr_Type()
)
atmIfDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfDescr.setStatus("mandatory")


class _AtmIfAdminStatus_Type(Integer32):
    """Custom type atmIfAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_AtmIfAdminStatus_Type.__name__ = "Integer32"
_AtmIfAdminStatus_Object = MibTableColumn
atmIfAdminStatus = _AtmIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 10, 1, 4),
    _AtmIfAdminStatus_Type()
)
atmIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfAdminStatus.setStatus("mandatory")


class _AtmIfOperStatus_Type(Integer32):
    """Custom type atmIfOperStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_AtmIfOperStatus_Type.__name__ = "Integer32"
_AtmIfOperStatus_Object = MibTableColumn
atmIfOperStatus = _AtmIfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 10, 1, 5),
    _AtmIfOperStatus_Type()
)
atmIfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfOperStatus.setStatus("mandatory")
_AtmIfLastChange_Type = TimeTicks
_AtmIfLastChange_Object = MibTableColumn
atmIfLastChange = _AtmIfLastChange_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 10, 1, 6),
    _AtmIfLastChange_Type()
)
atmIfLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfLastChange.setStatus("mandatory")


class _AtmIfMaxTxRate_Type(Integer32):
    """Custom type atmIfMaxTxRate based on Integer32"""
    defaultValue = 0


_AtmIfMaxTxRate_Object = MibTableColumn
atmIfMaxTxRate = _AtmIfMaxTxRate_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 10, 1, 7),
    _AtmIfMaxTxRate_Type()
)
atmIfMaxTxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfMaxTxRate.setStatus("mandatory")


class _AtmIfOperMode_Type(Integer32):
    """Custom type atmIfOperMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("atm", 1),
          ("efm", 2))
    )


_AtmIfOperMode_Type.__name__ = "Integer32"
_AtmIfOperMode_Object = MibTableColumn
atmIfOperMode = _AtmIfOperMode_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 10, 1, 8),
    _AtmIfOperMode_Type()
)
atmIfOperMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfOperMode.setStatus("mandatory")
_AtmIfInPkts_Type = Integer32
_AtmIfInPkts_Object = MibTableColumn
atmIfInPkts = _AtmIfInPkts_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 10, 1, 22),
    _AtmIfInPkts_Type()
)
atmIfInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfInPkts.setStatus("mandatory")
_AtmIfOutPkts_Type = Integer32
_AtmIfOutPkts_Object = MibTableColumn
atmIfOutPkts = _AtmIfOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 10, 1, 23),
    _AtmIfOutPkts_Type()
)
atmIfOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfOutPkts.setStatus("mandatory")
_AtmIfRxSpeed_Type = Integer32
_AtmIfRxSpeed_Object = MibTableColumn
atmIfRxSpeed = _AtmIfRxSpeed_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 10, 1, 24),
    _AtmIfRxSpeed_Type()
)
atmIfRxSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfRxSpeed.setStatus("mandatory")
_AtmIfTxSpeed_Type = Integer32
_AtmIfTxSpeed_Object = MibTableColumn
atmIfTxSpeed = _AtmIfTxSpeed_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 10, 1, 25),
    _AtmIfTxSpeed_Type()
)
atmIfTxSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfTxSpeed.setStatus("mandatory")
_AtmIfInOctets_Type = Counter32
_AtmIfInOctets_Object = MibTableColumn
atmIfInOctets = _AtmIfInOctets_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 10, 1, 26),
    _AtmIfInOctets_Type()
)
atmIfInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfInOctets.setStatus("mandatory")
_AtmIfInDiscards_Type = Counter32
_AtmIfInDiscards_Object = MibTableColumn
atmIfInDiscards = _AtmIfInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 10, 1, 27),
    _AtmIfInDiscards_Type()
)
atmIfInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfInDiscards.setStatus("mandatory")
_AtmIfInErrors_Type = Counter32
_AtmIfInErrors_Object = MibTableColumn
atmIfInErrors = _AtmIfInErrors_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 10, 1, 28),
    _AtmIfInErrors_Type()
)
atmIfInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfInErrors.setStatus("mandatory")
_AtmIfOutOctets_Type = Counter32
_AtmIfOutOctets_Object = MibTableColumn
atmIfOutOctets = _AtmIfOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 10, 1, 29),
    _AtmIfOutOctets_Type()
)
atmIfOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfOutOctets.setStatus("mandatory")
_AtmIfOutDiscards_Type = Counter32
_AtmIfOutDiscards_Object = MibTableColumn
atmIfOutDiscards = _AtmIfOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 10, 1, 30),
    _AtmIfOutDiscards_Type()
)
atmIfOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfOutDiscards.setStatus("mandatory")
_AtmIfOutErrors_Type = Counter32
_AtmIfOutErrors_Object = MibTableColumn
atmIfOutErrors = _AtmIfOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 10, 1, 31),
    _AtmIfOutErrors_Type()
)
atmIfOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfOutErrors.setStatus("mandatory")
_AtmVpcTable_Object = MibTable
atmVpcTable = _AtmVpcTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 11)
)
if mibBuilder.loadTexts:
    atmVpcTable.setStatus("mandatory")
_AtmVpcEntry_Object = MibTableRow
atmVpcEntry = _AtmVpcEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 11, 1)
)
atmVpcEntry.setIndexNames(
    (0, "BIANCA-BRICK-ATM2-MIB", "atmVpcPortIndex"),
    (0, "BIANCA-BRICK-ATM2-MIB", "atmVpcVpi"),
)
if mibBuilder.loadTexts:
    atmVpcEntry.setStatus("mandatory")
_AtmVpcPortIndex_Type = Integer32
_AtmVpcPortIndex_Object = MibTableColumn
atmVpcPortIndex = _AtmVpcPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 11, 1, 1),
    _AtmVpcPortIndex_Type()
)
atmVpcPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVpcPortIndex.setStatus("mandatory")


class _AtmVpcVpi_Type(Integer32):
    """Custom type atmVpcVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AtmVpcVpi_Type.__name__ = "Integer32"
_AtmVpcVpi_Object = MibTableColumn
atmVpcVpi = _AtmVpcVpi_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 11, 1, 2),
    _AtmVpcVpi_Type()
)
atmVpcVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVpcVpi.setStatus("mandatory")


class _AtmVpcOperStatus_Type(Integer32):
    """Custom type atmVpcOperStatus based on Integer32"""
    defaultValue = 1

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
        *(("end2endDown", 3),
          ("end2endUp", 2),
          ("localDown", 5),
          ("localUpEnd2endUnknown", 4),
          ("unknown", 1))
    )


_AtmVpcOperStatus_Type.__name__ = "Integer32"
_AtmVpcOperStatus_Object = MibTableColumn
atmVpcOperStatus = _AtmVpcOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 11, 1, 3),
    _AtmVpcOperStatus_Type()
)
atmVpcOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVpcOperStatus.setStatus("mandatory")
_AtmVccTable_Object = MibTable
atmVccTable = _AtmVccTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 12)
)
if mibBuilder.loadTexts:
    atmVccTable.setStatus("mandatory")
_AtmVccEntry_Object = MibTableRow
atmVccEntry = _AtmVccEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 12, 1)
)
atmVccEntry.setIndexNames(
    (0, "BIANCA-BRICK-ATM2-MIB", "atmVccPortIndex"),
    (0, "BIANCA-BRICK-ATM2-MIB", "atmVccVpi"),
    (0, "BIANCA-BRICK-ATM2-MIB", "atmVccVci"),
)
if mibBuilder.loadTexts:
    atmVccEntry.setStatus("mandatory")
_AtmVccPortIndex_Type = Integer32
_AtmVccPortIndex_Object = MibTableColumn
atmVccPortIndex = _AtmVccPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 12, 1, 1),
    _AtmVccPortIndex_Type()
)
atmVccPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVccPortIndex.setStatus("mandatory")


class _AtmVccVpi_Type(Integer32):
    """Custom type atmVccVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AtmVccVpi_Type.__name__ = "Integer32"
_AtmVccVpi_Object = MibTableColumn
atmVccVpi = _AtmVccVpi_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 12, 1, 2),
    _AtmVccVpi_Type()
)
atmVccVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVccVpi.setStatus("mandatory")


class _AtmVccVci_Type(Integer32):
    """Custom type atmVccVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AtmVccVci_Type.__name__ = "Integer32"
_AtmVccVci_Object = MibTableColumn
atmVccVci = _AtmVccVci_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 12, 1, 3),
    _AtmVccVci_Type()
)
atmVccVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVccVci.setStatus("mandatory")


class _AtmVccOperStatus_Type(Integer32):
    """Custom type atmVccOperStatus based on Integer32"""
    defaultValue = 1

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
        *(("end2endDown", 3),
          ("end2endUp", 2),
          ("localDown", 5),
          ("localUpEnd2endUnknown", 4),
          ("unknown", 1))
    )


_AtmVccOperStatus_Type.__name__ = "Integer32"
_AtmVccOperStatus_Object = MibTableColumn
atmVccOperStatus = _AtmVccOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 12, 1, 4),
    _AtmVccOperStatus_Type()
)
atmVccOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVccOperStatus.setStatus("mandatory")
_AtmOamTable_Object = MibTable
atmOamTable = _AtmOamTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 13)
)
if mibBuilder.loadTexts:
    atmOamTable.setStatus("mandatory")
_AtmOamEntry_Object = MibTableRow
atmOamEntry = _AtmOamEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 13, 1)
)
atmOamEntry.setIndexNames(
    (0, "BIANCA-BRICK-ATM2-MIB", "atmOamAtmIfIndex"),
    (0, "BIANCA-BRICK-ATM2-MIB", "atmOamVpi"),
    (0, "BIANCA-BRICK-ATM2-MIB", "atmOamVci"),
)
if mibBuilder.loadTexts:
    atmOamEntry.setStatus("mandatory")
_AtmOamAtmIfIndex_Type = Integer32
_AtmOamAtmIfIndex_Object = MibTableColumn
atmOamAtmIfIndex = _AtmOamAtmIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 13, 1, 1),
    _AtmOamAtmIfIndex_Type()
)
atmOamAtmIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmOamAtmIfIndex.setStatus("mandatory")


class _AtmOamVpi_Type(Integer32):
    """Custom type atmOamVpi based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AtmOamVpi_Type.__name__ = "Integer32"
_AtmOamVpi_Object = MibTableColumn
atmOamVpi = _AtmOamVpi_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 13, 1, 2),
    _AtmOamVpi_Type()
)
atmOamVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmOamVpi.setStatus("mandatory")


class _AtmOamVci_Type(Integer32):
    """Custom type atmOamVci based on Integer32"""
    defaultValue = 32

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AtmOamVci_Type.__name__ = "Integer32"
_AtmOamVci_Object = MibTableColumn
atmOamVci = _AtmOamVci_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 13, 1, 3),
    _AtmOamVci_Type()
)
atmOamVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmOamVci.setStatus("mandatory")


class _AtmOamFlowLevel_Type(Integer32):
    """Custom type atmOamFlowLevel based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              10)
        )
    )
    namedValues = NamedValues(
        *(("delete", 10),
          ("f4", 2),
          ("f5", 1))
    )


_AtmOamFlowLevel_Type.__name__ = "Integer32"
_AtmOamFlowLevel_Object = MibTableColumn
atmOamFlowLevel = _AtmOamFlowLevel_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 13, 1, 4),
    _AtmOamFlowLevel_Type()
)
atmOamFlowLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmOamFlowLevel.setStatus("mandatory")


class _AtmOamLoopbackEnd2End_Type(Integer32):
    """Custom type atmOamLoopbackEnd2End based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_AtmOamLoopbackEnd2End_Type.__name__ = "Integer32"
_AtmOamLoopbackEnd2End_Object = MibTableColumn
atmOamLoopbackEnd2End = _AtmOamLoopbackEnd2End_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 13, 1, 5),
    _AtmOamLoopbackEnd2End_Type()
)
atmOamLoopbackEnd2End.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmOamLoopbackEnd2End.setStatus("mandatory")


class _AtmOamLoopbackSegment_Type(Integer32):
    """Custom type atmOamLoopbackSegment based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_AtmOamLoopbackSegment_Type.__name__ = "Integer32"
_AtmOamLoopbackSegment_Object = MibTableColumn
atmOamLoopbackSegment = _AtmOamLoopbackSegment_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 13, 1, 6),
    _AtmOamLoopbackSegment_Type()
)
atmOamLoopbackSegment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmOamLoopbackSegment.setStatus("mandatory")


class _AtmOamLoopbackEnd2EndInterval_Type(Integer32):
    """Custom type atmOamLoopbackEnd2EndInterval based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_AtmOamLoopbackEnd2EndInterval_Type.__name__ = "Integer32"
_AtmOamLoopbackEnd2EndInterval_Object = MibTableColumn
atmOamLoopbackEnd2EndInterval = _AtmOamLoopbackEnd2EndInterval_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 13, 1, 7),
    _AtmOamLoopbackEnd2EndInterval_Type()
)
atmOamLoopbackEnd2EndInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmOamLoopbackEnd2EndInterval.setStatus("mandatory")


class _AtmOamLoopbackSegmentInterval_Type(Integer32):
    """Custom type atmOamLoopbackSegmentInterval based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_AtmOamLoopbackSegmentInterval_Type.__name__ = "Integer32"
_AtmOamLoopbackSegmentInterval_Object = MibTableColumn
atmOamLoopbackSegmentInterval = _AtmOamLoopbackSegmentInterval_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 13, 1, 8),
    _AtmOamLoopbackSegmentInterval_Type()
)
atmOamLoopbackSegmentInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmOamLoopbackSegmentInterval.setStatus("mandatory")


class _AtmOamLoopbackEnd2EndMaxPending_Type(Integer32):
    """Custom type atmOamLoopbackEnd2EndMaxPending based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_AtmOamLoopbackEnd2EndMaxPending_Type.__name__ = "Integer32"
_AtmOamLoopbackEnd2EndMaxPending_Object = MibTableColumn
atmOamLoopbackEnd2EndMaxPending = _AtmOamLoopbackEnd2EndMaxPending_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 13, 1, 9),
    _AtmOamLoopbackEnd2EndMaxPending_Type()
)
atmOamLoopbackEnd2EndMaxPending.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmOamLoopbackEnd2EndMaxPending.setStatus("mandatory")


class _AtmOamLoopbackSegmentMaxPending_Type(Integer32):
    """Custom type atmOamLoopbackSegmentMaxPending based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_AtmOamLoopbackSegmentMaxPending_Type.__name__ = "Integer32"
_AtmOamLoopbackSegmentMaxPending_Object = MibTableColumn
atmOamLoopbackSegmentMaxPending = _AtmOamLoopbackSegmentMaxPending_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 13, 1, 10),
    _AtmOamLoopbackSegmentMaxPending_Type()
)
atmOamLoopbackSegmentMaxPending.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmOamLoopbackSegmentMaxPending.setStatus("mandatory")


class _AtmOamCCEnd2EndActivation_Type(Integer32):
    """Custom type atmOamCCEnd2EndActivation based on Integer32"""
    defaultValue = 1

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
        *(("active", 2),
          ("both", 3),
          ("no-negotiation", 4),
          ("none", 5),
          ("passive", 1))
    )


_AtmOamCCEnd2EndActivation_Type.__name__ = "Integer32"
_AtmOamCCEnd2EndActivation_Object = MibTableColumn
atmOamCCEnd2EndActivation = _AtmOamCCEnd2EndActivation_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 13, 1, 11),
    _AtmOamCCEnd2EndActivation_Type()
)
atmOamCCEnd2EndActivation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmOamCCEnd2EndActivation.setStatus("mandatory")


class _AtmOamCCSegmentActivation_Type(Integer32):
    """Custom type atmOamCCSegmentActivation based on Integer32"""
    defaultValue = 1

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
        *(("active", 2),
          ("both", 3),
          ("no-negotiation", 4),
          ("none", 5),
          ("passive", 1))
    )


_AtmOamCCSegmentActivation_Type.__name__ = "Integer32"
_AtmOamCCSegmentActivation_Object = MibTableColumn
atmOamCCSegmentActivation = _AtmOamCCSegmentActivation_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 13, 1, 12),
    _AtmOamCCSegmentActivation_Type()
)
atmOamCCSegmentActivation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmOamCCSegmentActivation.setStatus("mandatory")


class _AtmOamCCEnd2EndDirection_Type(Integer32):
    """Custom type atmOamCCEnd2EndDirection based on Integer32"""
    defaultValue = 3

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
        *(("both", 3),
          ("none", 4),
          ("sink", 1),
          ("source", 2))
    )


_AtmOamCCEnd2EndDirection_Type.__name__ = "Integer32"
_AtmOamCCEnd2EndDirection_Object = MibTableColumn
atmOamCCEnd2EndDirection = _AtmOamCCEnd2EndDirection_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 13, 1, 13),
    _AtmOamCCEnd2EndDirection_Type()
)
atmOamCCEnd2EndDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmOamCCEnd2EndDirection.setStatus("mandatory")


class _AtmOamCCSegmentDirection_Type(Integer32):
    """Custom type atmOamCCSegmentDirection based on Integer32"""
    defaultValue = 3

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
        *(("both", 3),
          ("none", 4),
          ("sink", 1),
          ("source", 2))
    )


_AtmOamCCSegmentDirection_Type.__name__ = "Integer32"
_AtmOamCCSegmentDirection_Object = MibTableColumn
atmOamCCSegmentDirection = _AtmOamCCSegmentDirection_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 13, 1, 14),
    _AtmOamCCSegmentDirection_Type()
)
atmOamCCSegmentDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmOamCCSegmentDirection.setStatus("mandatory")
_AtmOamStatTable_Object = MibTable
atmOamStatTable = _AtmOamStatTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 14)
)
if mibBuilder.loadTexts:
    atmOamStatTable.setStatus("mandatory")
_AtmOamStatEntry_Object = MibTableRow
atmOamStatEntry = _AtmOamStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 14, 1)
)
atmOamStatEntry.setIndexNames(
    (0, "BIANCA-BRICK-ATM2-MIB", "atmOamStatAtmIfIndex"),
    (0, "BIANCA-BRICK-ATM2-MIB", "atmOamStatVpi"),
    (0, "BIANCA-BRICK-ATM2-MIB", "atmOamStatVci"),
)
if mibBuilder.loadTexts:
    atmOamStatEntry.setStatus("mandatory")
_AtmOamStatAtmIfIndex_Type = Integer32
_AtmOamStatAtmIfIndex_Object = MibTableColumn
atmOamStatAtmIfIndex = _AtmOamStatAtmIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 14, 1, 1),
    _AtmOamStatAtmIfIndex_Type()
)
atmOamStatAtmIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmOamStatAtmIfIndex.setStatus("mandatory")


class _AtmOamStatVpi_Type(Integer32):
    """Custom type atmOamStatVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AtmOamStatVpi_Type.__name__ = "Integer32"
_AtmOamStatVpi_Object = MibTableColumn
atmOamStatVpi = _AtmOamStatVpi_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 14, 1, 2),
    _AtmOamStatVpi_Type()
)
atmOamStatVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmOamStatVpi.setStatus("mandatory")


class _AtmOamStatVci_Type(Integer32):
    """Custom type atmOamStatVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AtmOamStatVci_Type.__name__ = "Integer32"
_AtmOamStatVci_Object = MibTableColumn
atmOamStatVci = _AtmOamStatVci_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 14, 1, 3),
    _AtmOamStatVci_Type()
)
atmOamStatVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmOamStatVci.setStatus("mandatory")


class _AtmOamStatFlowType_Type(Integer32):
    """Custom type atmOamStatFlowType based on Integer32"""
    defaultValue = 2

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
        *(("f4-end2end", 4),
          ("f4-segment", 3),
          ("f5-end2end", 2),
          ("f5-segment", 1))
    )


_AtmOamStatFlowType_Type.__name__ = "Integer32"
_AtmOamStatFlowType_Object = MibTableColumn
atmOamStatFlowType = _AtmOamStatFlowType_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 14, 1, 4),
    _AtmOamStatFlowType_Type()
)
atmOamStatFlowType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmOamStatFlowType.setStatus("mandatory")
_AtmOamStatLoopbackTxCells_Type = Counter32
_AtmOamStatLoopbackTxCells_Object = MibTableColumn
atmOamStatLoopbackTxCells = _AtmOamStatLoopbackTxCells_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 14, 1, 6),
    _AtmOamStatLoopbackTxCells_Type()
)
atmOamStatLoopbackTxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmOamStatLoopbackTxCells.setStatus("mandatory")
_AtmOamStatLoopbackRxCells_Type = Counter32
_AtmOamStatLoopbackRxCells_Object = MibTableColumn
atmOamStatLoopbackRxCells = _AtmOamStatLoopbackRxCells_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 14, 1, 7),
    _AtmOamStatLoopbackRxCells_Type()
)
atmOamStatLoopbackRxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmOamStatLoopbackRxCells.setStatus("mandatory")
_AtmOamStatLoopbackPending_Type = Counter32
_AtmOamStatLoopbackPending_Object = MibTableColumn
atmOamStatLoopbackPending = _AtmOamStatLoopbackPending_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 14, 1, 8),
    _AtmOamStatLoopbackPending_Type()
)
atmOamStatLoopbackPending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmOamStatLoopbackPending.setStatus("mandatory")
_AtmOamStatLoopbackCorr_Type = Integer32
_AtmOamStatLoopbackCorr_Object = MibTableColumn
atmOamStatLoopbackCorr = _AtmOamStatLoopbackCorr_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 14, 1, 9),
    _AtmOamStatLoopbackCorr_Type()
)
atmOamStatLoopbackCorr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmOamStatLoopbackCorr.setStatus("mandatory")


class _AtmOamStatAisState_Type(Integer32):
    """Custom type atmOamStatAisState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_AtmOamStatAisState_Type.__name__ = "Integer32"
_AtmOamStatAisState_Object = MibTableColumn
atmOamStatAisState = _AtmOamStatAisState_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 14, 1, 10),
    _AtmOamStatAisState_Type()
)
atmOamStatAisState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmOamStatAisState.setStatus("mandatory")
_AtmOamStatAisTxCells_Type = Counter32
_AtmOamStatAisTxCells_Object = MibTableColumn
atmOamStatAisTxCells = _AtmOamStatAisTxCells_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 14, 1, 11),
    _AtmOamStatAisTxCells_Type()
)
atmOamStatAisTxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmOamStatAisTxCells.setStatus("mandatory")
_AtmOamStatAisRxCells_Type = Counter32
_AtmOamStatAisRxCells_Object = MibTableColumn
atmOamStatAisRxCells = _AtmOamStatAisRxCells_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 14, 1, 12),
    _AtmOamStatAisRxCells_Type()
)
atmOamStatAisRxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmOamStatAisRxCells.setStatus("mandatory")
_AtmOamStatTotalAisTxCells_Type = Counter32
_AtmOamStatTotalAisTxCells_Object = MibTableColumn
atmOamStatTotalAisTxCells = _AtmOamStatTotalAisTxCells_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 14, 1, 13),
    _AtmOamStatTotalAisTxCells_Type()
)
atmOamStatTotalAisTxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmOamStatTotalAisTxCells.setStatus("mandatory")
_AtmOamStatTotalAisRxCells_Type = Counter32
_AtmOamStatTotalAisRxCells_Object = MibTableColumn
atmOamStatTotalAisRxCells = _AtmOamStatTotalAisRxCells_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 14, 1, 14),
    _AtmOamStatTotalAisRxCells_Type()
)
atmOamStatTotalAisRxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmOamStatTotalAisRxCells.setStatus("mandatory")


class _AtmOamStatRdiState_Type(Integer32):
    """Custom type atmOamStatRdiState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_AtmOamStatRdiState_Type.__name__ = "Integer32"
_AtmOamStatRdiState_Object = MibTableColumn
atmOamStatRdiState = _AtmOamStatRdiState_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 14, 1, 15),
    _AtmOamStatRdiState_Type()
)
atmOamStatRdiState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmOamStatRdiState.setStatus("mandatory")
_AtmOamStatRdiTxCells_Type = Counter32
_AtmOamStatRdiTxCells_Object = MibTableColumn
atmOamStatRdiTxCells = _AtmOamStatRdiTxCells_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 14, 1, 16),
    _AtmOamStatRdiTxCells_Type()
)
atmOamStatRdiTxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmOamStatRdiTxCells.setStatus("mandatory")
_AtmOamStatRdiRxCells_Type = Counter32
_AtmOamStatRdiRxCells_Object = MibTableColumn
atmOamStatRdiRxCells = _AtmOamStatRdiRxCells_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 14, 1, 17),
    _AtmOamStatRdiRxCells_Type()
)
atmOamStatRdiRxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmOamStatRdiRxCells.setStatus("mandatory")
_AtmOamStatTotalRdiTxCells_Type = Integer32
_AtmOamStatTotalRdiTxCells_Object = MibTableColumn
atmOamStatTotalRdiTxCells = _AtmOamStatTotalRdiTxCells_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 14, 1, 18),
    _AtmOamStatTotalRdiTxCells_Type()
)
atmOamStatTotalRdiTxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmOamStatTotalRdiTxCells.setStatus("mandatory")
_AtmOamStatTotalRdiRxCells_Type = Counter32
_AtmOamStatTotalRdiRxCells_Object = MibTableColumn
atmOamStatTotalRdiRxCells = _AtmOamStatTotalRdiRxCells_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 14, 1, 19),
    _AtmOamStatTotalRdiRxCells_Type()
)
atmOamStatTotalRdiRxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmOamStatTotalRdiRxCells.setStatus("mandatory")


class _AtmOamStatCCActivatorState_Type(Integer32):
    """Custom type atmOamStatCCActivatorState based on Integer32"""
    defaultValue = 1

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
        *(("active", 3),
          ("inactive", 1),
          ("wait-act-con", 2),
          ("wait-deact-con", 4))
    )


_AtmOamStatCCActivatorState_Type.__name__ = "Integer32"
_AtmOamStatCCActivatorState_Object = MibTableColumn
atmOamStatCCActivatorState = _AtmOamStatCCActivatorState_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 14, 1, 20),
    _AtmOamStatCCActivatorState_Type()
)
atmOamStatCCActivatorState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmOamStatCCActivatorState.setStatus("mandatory")


class _AtmOamStatCCActivatorDirection_Type(Integer32):
    """Custom type atmOamStatCCActivatorDirection based on Integer32"""
    defaultValue = 4

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
        *(("both", 3),
          ("not-applicable", 4),
          ("sink", 1),
          ("source", 2))
    )


_AtmOamStatCCActivatorDirection_Type.__name__ = "Integer32"
_AtmOamStatCCActivatorDirection_Object = MibTableColumn
atmOamStatCCActivatorDirection = _AtmOamStatCCActivatorDirection_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 14, 1, 21),
    _AtmOamStatCCActivatorDirection_Type()
)
atmOamStatCCActivatorDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmOamStatCCActivatorDirection.setStatus("mandatory")
_AtmOamStatCCActivatorCorr_Type = Integer32
_AtmOamStatCCActivatorCorr_Object = MibTableColumn
atmOamStatCCActivatorCorr = _AtmOamStatCCActivatorCorr_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 14, 1, 22),
    _AtmOamStatCCActivatorCorr_Type()
)
atmOamStatCCActivatorCorr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmOamStatCCActivatorCorr.setStatus("mandatory")


class _AtmOamStatCCResponderState_Type(Integer32):
    """Custom type atmOamStatCCResponderState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("active", 3),
          ("inactive", 1),
          ("wait-deact-con", 4))
    )


_AtmOamStatCCResponderState_Type.__name__ = "Integer32"
_AtmOamStatCCResponderState_Object = MibTableColumn
atmOamStatCCResponderState = _AtmOamStatCCResponderState_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 14, 1, 23),
    _AtmOamStatCCResponderState_Type()
)
atmOamStatCCResponderState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmOamStatCCResponderState.setStatus("mandatory")


class _AtmOamStatCCResponderDirection_Type(Integer32):
    """Custom type atmOamStatCCResponderDirection based on Integer32"""
    defaultValue = 4

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
        *(("both", 3),
          ("not-applicable", 4),
          ("sink", 2),
          ("source", 1))
    )


_AtmOamStatCCResponderDirection_Type.__name__ = "Integer32"
_AtmOamStatCCResponderDirection_Object = MibTableColumn
atmOamStatCCResponderDirection = _AtmOamStatCCResponderDirection_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 14, 1, 24),
    _AtmOamStatCCResponderDirection_Type()
)
atmOamStatCCResponderDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmOamStatCCResponderDirection.setStatus("mandatory")
_AtmOamStatCCResponderCorr_Type = Integer32
_AtmOamStatCCResponderCorr_Object = MibTableColumn
atmOamStatCCResponderCorr = _AtmOamStatCCResponderCorr_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 14, 1, 25),
    _AtmOamStatCCResponderCorr_Type()
)
atmOamStatCCResponderCorr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmOamStatCCResponderCorr.setStatus("mandatory")
_AtmOamStatCCTxCells_Type = Counter32
_AtmOamStatCCTxCells_Object = MibTableColumn
atmOamStatCCTxCells = _AtmOamStatCCTxCells_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 14, 1, 26),
    _AtmOamStatCCTxCells_Type()
)
atmOamStatCCTxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmOamStatCCTxCells.setStatus("mandatory")
_AtmOamStatCCRxCells_Type = Counter32
_AtmOamStatCCRxCells_Object = MibTableColumn
atmOamStatCCRxCells = _AtmOamStatCCRxCells_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 14, 1, 27),
    _AtmOamStatCCRxCells_Type()
)
atmOamStatCCRxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmOamStatCCRxCells.setStatus("mandatory")
_EthoaPvcTable_Object = MibTable
ethoaPvcTable = _EthoaPvcTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 15)
)
if mibBuilder.loadTexts:
    ethoaPvcTable.setStatus("mandatory")
_EthoaPvcEntry_Object = MibTableRow
ethoaPvcEntry = _EthoaPvcEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 15, 1)
)
ethoaPvcEntry.setIndexNames(
    (0, "BIANCA-BRICK-ATM2-MIB", "ethoaPvcVpi"),
    (0, "BIANCA-BRICK-ATM2-MIB", "ethoaPvcVci"),
    (0, "BIANCA-BRICK-ATM2-MIB", "ethoaPvcAtmIfIndex"),
)
if mibBuilder.loadTexts:
    ethoaPvcEntry.setStatus("mandatory")


class _EthoaPvcIfIndex_Type(Integer32):
    """Custom type ethoaPvcIfIndex based on Integer32"""
    defaultValue = 0


_EthoaPvcIfIndex_Object = MibTableColumn
ethoaPvcIfIndex = _EthoaPvcIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 15, 1, 1),
    _EthoaPvcIfIndex_Type()
)
ethoaPvcIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethoaPvcIfIndex.setStatus("mandatory")
_EthoaPvcDescr_Type = DisplayString
_EthoaPvcDescr_Object = MibTableColumn
ethoaPvcDescr = _EthoaPvcDescr_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 15, 1, 2),
    _EthoaPvcDescr_Type()
)
ethoaPvcDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethoaPvcDescr.setStatus("mandatory")
_EthoaPvcAtmIfIndex_Type = Integer32
_EthoaPvcAtmIfIndex_Object = MibTableColumn
ethoaPvcAtmIfIndex = _EthoaPvcAtmIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 15, 1, 3),
    _EthoaPvcAtmIfIndex_Type()
)
ethoaPvcAtmIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethoaPvcAtmIfIndex.setStatus("mandatory")


class _EthoaPvcVpi_Type(Integer32):
    """Custom type ethoaPvcVpi based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_EthoaPvcVpi_Type.__name__ = "Integer32"
_EthoaPvcVpi_Object = MibTableColumn
ethoaPvcVpi = _EthoaPvcVpi_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 15, 1, 4),
    _EthoaPvcVpi_Type()
)
ethoaPvcVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethoaPvcVpi.setStatus("mandatory")


class _EthoaPvcVci_Type(Integer32):
    """Custom type ethoaPvcVci based on Integer32"""
    defaultValue = 32

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_EthoaPvcVci_Type.__name__ = "Integer32"
_EthoaPvcVci_Object = MibTableColumn
ethoaPvcVci = _EthoaPvcVci_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 15, 1, 5),
    _EthoaPvcVci_Type()
)
ethoaPvcVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethoaPvcVci.setStatus("mandatory")


class _EthoaPvcEncapsulation_Type(Integer32):
    """Custom type ethoaPvcEncapsulation based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              10)
        )
    )
    namedValues = NamedValues(
        *(("bridged-fcs", 2),
          ("bridged-no-fcs", 1),
          ("delete", 10),
          ("vc-multiplexed", 3))
    )


_EthoaPvcEncapsulation_Type.__name__ = "Integer32"
_EthoaPvcEncapsulation_Object = MibTableColumn
ethoaPvcEncapsulation = _EthoaPvcEncapsulation_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 15, 1, 6),
    _EthoaPvcEncapsulation_Type()
)
ethoaPvcEncapsulation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethoaPvcEncapsulation.setStatus("mandatory")
_EthoaPvcPhysAddress_Type = PhysAddress
_EthoaPvcPhysAddress_Object = MibTableColumn
ethoaPvcPhysAddress = _EthoaPvcPhysAddress_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 15, 1, 7),
    _EthoaPvcPhysAddress_Type()
)
ethoaPvcPhysAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethoaPvcPhysAddress.setStatus("mandatory")
_RpoaPvcTable_Object = MibTable
rpoaPvcTable = _RpoaPvcTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 16)
)
if mibBuilder.loadTexts:
    rpoaPvcTable.setStatus("mandatory")
_RpoaPvcEntry_Object = MibTableRow
rpoaPvcEntry = _RpoaPvcEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 16, 1)
)
rpoaPvcEntry.setIndexNames(
    (0, "BIANCA-BRICK-ATM2-MIB", "rpoaPvcVpi"),
    (0, "BIANCA-BRICK-ATM2-MIB", "rpoaPvcVci"),
    (0, "BIANCA-BRICK-ATM2-MIB", "rpoaPvcAtmIfIndex"),
)
if mibBuilder.loadTexts:
    rpoaPvcEntry.setStatus("mandatory")


class _RpoaPvcIfIndex_Type(Integer32):
    """Custom type rpoaPvcIfIndex based on Integer32"""
    defaultValue = 0


_RpoaPvcIfIndex_Object = MibTableColumn
rpoaPvcIfIndex = _RpoaPvcIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 16, 1, 1),
    _RpoaPvcIfIndex_Type()
)
rpoaPvcIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpoaPvcIfIndex.setStatus("mandatory")
_RpoaPvcDescr_Type = DisplayString
_RpoaPvcDescr_Object = MibTableColumn
rpoaPvcDescr = _RpoaPvcDescr_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 16, 1, 2),
    _RpoaPvcDescr_Type()
)
rpoaPvcDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rpoaPvcDescr.setStatus("mandatory")
_RpoaPvcAtmIfIndex_Type = Integer32
_RpoaPvcAtmIfIndex_Object = MibTableColumn
rpoaPvcAtmIfIndex = _RpoaPvcAtmIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 16, 1, 3),
    _RpoaPvcAtmIfIndex_Type()
)
rpoaPvcAtmIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rpoaPvcAtmIfIndex.setStatus("mandatory")


class _RpoaPvcVpi_Type(Integer32):
    """Custom type rpoaPvcVpi based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RpoaPvcVpi_Type.__name__ = "Integer32"
_RpoaPvcVpi_Object = MibTableColumn
rpoaPvcVpi = _RpoaPvcVpi_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 16, 1, 4),
    _RpoaPvcVpi_Type()
)
rpoaPvcVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rpoaPvcVpi.setStatus("mandatory")


class _RpoaPvcVci_Type(Integer32):
    """Custom type rpoaPvcVci based on Integer32"""
    defaultValue = 32

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RpoaPvcVci_Type.__name__ = "Integer32"
_RpoaPvcVci_Object = MibTableColumn
rpoaPvcVci = _RpoaPvcVci_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 16, 1, 5),
    _RpoaPvcVci_Type()
)
rpoaPvcVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rpoaPvcVci.setStatus("mandatory")


class _RpoaPvcEncapsulation_Type(Integer32):
    """Custom type rpoaPvcEncapsulation based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              10)
        )
    )
    namedValues = NamedValues(
        *(("delete", 10),
          ("iso", 2),
          ("non-iso", 1),
          ("vc-multiplexed", 3))
    )


_RpoaPvcEncapsulation_Type.__name__ = "Integer32"
_RpoaPvcEncapsulation_Object = MibTableColumn
rpoaPvcEncapsulation = _RpoaPvcEncapsulation_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 16, 1, 6),
    _RpoaPvcEncapsulation_Type()
)
rpoaPvcEncapsulation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rpoaPvcEncapsulation.setStatus("mandatory")
_PppoaPvcTable_Object = MibTable
pppoaPvcTable = _PppoaPvcTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 17)
)
if mibBuilder.loadTexts:
    pppoaPvcTable.setStatus("mandatory")
_PppoaPvcEntry_Object = MibTableRow
pppoaPvcEntry = _PppoaPvcEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 17, 1)
)
pppoaPvcEntry.setIndexNames(
    (0, "BIANCA-BRICK-ATM2-MIB", "pppoaPvcVpi"),
    (0, "BIANCA-BRICK-ATM2-MIB", "pppoaPvcVci"),
    (0, "BIANCA-BRICK-ATM2-MIB", "pppoaPvcAtmIfIndex"),
)
if mibBuilder.loadTexts:
    pppoaPvcEntry.setStatus("mandatory")


class _PppoaPvcIfIndex_Type(Integer32):
    """Custom type pppoaPvcIfIndex based on Integer32"""
    defaultValue = 0


_PppoaPvcIfIndex_Object = MibTableColumn
pppoaPvcIfIndex = _PppoaPvcIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 17, 1, 1),
    _PppoaPvcIfIndex_Type()
)
pppoaPvcIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppoaPvcIfIndex.setStatus("mandatory")
_PppoaPvcDescr_Type = DisplayString
_PppoaPvcDescr_Object = MibTableColumn
pppoaPvcDescr = _PppoaPvcDescr_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 17, 1, 2),
    _PppoaPvcDescr_Type()
)
pppoaPvcDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppoaPvcDescr.setStatus("mandatory")
_PppoaPvcAtmIfIndex_Type = Integer32
_PppoaPvcAtmIfIndex_Object = MibTableColumn
pppoaPvcAtmIfIndex = _PppoaPvcAtmIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 17, 1, 3),
    _PppoaPvcAtmIfIndex_Type()
)
pppoaPvcAtmIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppoaPvcAtmIfIndex.setStatus("mandatory")


class _PppoaPvcVpi_Type(Integer32):
    """Custom type pppoaPvcVpi based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PppoaPvcVpi_Type.__name__ = "Integer32"
_PppoaPvcVpi_Object = MibTableColumn
pppoaPvcVpi = _PppoaPvcVpi_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 17, 1, 4),
    _PppoaPvcVpi_Type()
)
pppoaPvcVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppoaPvcVpi.setStatus("mandatory")


class _PppoaPvcVci_Type(Integer32):
    """Custom type pppoaPvcVci based on Integer32"""
    defaultValue = 32

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PppoaPvcVci_Type.__name__ = "Integer32"
_PppoaPvcVci_Object = MibTableColumn
pppoaPvcVci = _PppoaPvcVci_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 17, 1, 5),
    _PppoaPvcVci_Type()
)
pppoaPvcVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppoaPvcVci.setStatus("mandatory")


class _PppoaPvcEncapsulation_Type(Integer32):
    """Custom type pppoaPvcEncapsulation based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              10)
        )
    )
    namedValues = NamedValues(
        *(("delete", 10),
          ("llc", 2),
          ("vc-multiplexed", 1))
    )


_PppoaPvcEncapsulation_Type.__name__ = "Integer32"
_PppoaPvcEncapsulation_Object = MibTableColumn
pppoaPvcEncapsulation = _PppoaPvcEncapsulation_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 17, 1, 6),
    _PppoaPvcEncapsulation_Type()
)
pppoaPvcEncapsulation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppoaPvcEncapsulation.setStatus("mandatory")


class _PppoaPvcClientType_Type(Integer32):
    """Custom type pppoaPvcClientType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on-demand", 2),
          ("permanent", 1))
    )


_PppoaPvcClientType_Type.__name__ = "Integer32"
_PppoaPvcClientType_Object = MibTableColumn
pppoaPvcClientType = _PppoaPvcClientType_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 17, 1, 7),
    _PppoaPvcClientType_Type()
)
pppoaPvcClientType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppoaPvcClientType.setStatus("mandatory")
_AtmQosVccTable_Object = MibTable
atmQosVccTable = _AtmQosVccTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 19)
)
if mibBuilder.loadTexts:
    atmQosVccTable.setStatus("mandatory")
_AtmQosVccEntry_Object = MibTableRow
atmQosVccEntry = _AtmQosVccEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 19, 1)
)
atmQosVccEntry.setIndexNames(
    (0, "BIANCA-BRICK-ATM2-MIB", "atmQosVccAtmIfIndex"),
    (0, "BIANCA-BRICK-ATM2-MIB", "atmQosVccVpi"),
    (0, "BIANCA-BRICK-ATM2-MIB", "atmQosVccVci"),
)
if mibBuilder.loadTexts:
    atmQosVccEntry.setStatus("mandatory")
_AtmQosVccAtmIfIndex_Type = Integer32
_AtmQosVccAtmIfIndex_Object = MibTableColumn
atmQosVccAtmIfIndex = _AtmQosVccAtmIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 19, 1, 1),
    _AtmQosVccAtmIfIndex_Type()
)
atmQosVccAtmIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmQosVccAtmIfIndex.setStatus("mandatory")


class _AtmQosVccVpi_Type(Integer32):
    """Custom type atmQosVccVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AtmQosVccVpi_Type.__name__ = "Integer32"
_AtmQosVccVpi_Object = MibTableColumn
atmQosVccVpi = _AtmQosVccVpi_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 19, 1, 2),
    _AtmQosVccVpi_Type()
)
atmQosVccVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmQosVccVpi.setStatus("mandatory")


class _AtmQosVccVci_Type(Integer32):
    """Custom type atmQosVccVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AtmQosVccVci_Type.__name__ = "Integer32"
_AtmQosVccVci_Object = MibTableColumn
atmQosVccVci = _AtmQosVccVci_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 19, 1, 3),
    _AtmQosVccVci_Type()
)
atmQosVccVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmQosVccVci.setStatus("mandatory")


class _AtmQosVccService_Type(Integer32):
    """Custom type atmQosVccService based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              20)
        )
    )
    namedValues = NamedValues(
        *(("cbr", 1),
          ("delete", 20),
          ("ubr", 8),
          ("vbr", 2),
          ("vbr3", 4))
    )


_AtmQosVccService_Type.__name__ = "Integer32"
_AtmQosVccService_Object = MibTableColumn
atmQosVccService = _AtmQosVccService_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 19, 1, 4),
    _AtmQosVccService_Type()
)
atmQosVccService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmQosVccService.setStatus("mandatory")
_AtmQosVccOutPcr_Type = Integer32
_AtmQosVccOutPcr_Object = MibTableColumn
atmQosVccOutPcr = _AtmQosVccOutPcr_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 19, 1, 5),
    _AtmQosVccOutPcr_Type()
)
atmQosVccOutPcr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmQosVccOutPcr.setStatus("mandatory")
_AtmQosVccOutScr_Type = Integer32
_AtmQosVccOutScr_Object = MibTableColumn
atmQosVccOutScr = _AtmQosVccOutScr_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 19, 1, 6),
    _AtmQosVccOutScr_Type()
)
atmQosVccOutScr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmQosVccOutScr.setStatus("mandatory")
_AtmQosVccOutMbs_Type = Integer32
_AtmQosVccOutMbs_Object = MibTableColumn
atmQosVccOutMbs = _AtmQosVccOutMbs_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 19, 1, 7),
    _AtmQosVccOutMbs_Type()
)
atmQosVccOutMbs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmQosVccOutMbs.setStatus("mandatory")
_AtmQosVccOutMcr_Type = Integer32
_AtmQosVccOutMcr_Object = MibTableColumn
atmQosVccOutMcr = _AtmQosVccOutMcr_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 19, 1, 8),
    _AtmQosVccOutMcr_Type()
)
atmQosVccOutMcr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmQosVccOutMcr.setStatus("mandatory")
_AtmAturPerfDataTable_Object = MibTable
atmAturPerfDataTable = _AtmAturPerfDataTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 20)
)
if mibBuilder.loadTexts:
    atmAturPerfDataTable.setStatus("mandatory")
_AtmAturPerfDataEntry_Object = MibTableRow
atmAturPerfDataEntry = _AtmAturPerfDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 20, 1)
)
atmAturPerfDataEntry.setIndexNames(
    (0, "BIANCA-BRICK-ATM2-MIB", "atmAturPerfIfIndex"),
)
if mibBuilder.loadTexts:
    atmAturPerfDataEntry.setStatus("mandatory")
_AtmAturPerfIfIndex_Type = Integer32
_AtmAturPerfIfIndex_Object = MibTableColumn
atmAturPerfIfIndex = _AtmAturPerfIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 20, 1, 1),
    _AtmAturPerfIfIndex_Type()
)
atmAturPerfIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmAturPerfIfIndex.setStatus("mandatory")
_AtmAturPerfIdleCells_Type = Integer32
_AtmAturPerfIdleCells_Object = MibTableColumn
atmAturPerfIdleCells = _AtmAturPerfIdleCells_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 20, 1, 2),
    _AtmAturPerfIdleCells_Type()
)
atmAturPerfIdleCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmAturPerfIdleCells.setStatus("mandatory")
_AtmAturPerfDataCells_Type = Integer32
_AtmAturPerfDataCells_Object = MibTableColumn
atmAturPerfDataCells = _AtmAturPerfDataCells_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 20, 1, 3),
    _AtmAturPerfDataCells_Type()
)
atmAturPerfDataCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmAturPerfDataCells.setStatus("mandatory")
_AtmAturPerfLcds_Type = Integer32
_AtmAturPerfLcds_Object = MibTableColumn
atmAturPerfLcds = _AtmAturPerfLcds_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 20, 1, 4),
    _AtmAturPerfLcds_Type()
)
atmAturPerfLcds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmAturPerfLcds.setStatus("mandatory")
_AtmAturPerfHecs_Type = Integer32
_AtmAturPerfHecs_Object = MibTableColumn
atmAturPerfHecs = _AtmAturPerfHecs_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 20, 1, 5),
    _AtmAturPerfHecs_Type()
)
atmAturPerfHecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmAturPerfHecs.setStatus("mandatory")


class _AtmAturPerfCurr15MinTimeElapsed_Type(Integer32):
    """Custom type atmAturPerfCurr15MinTimeElapsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 899),
    )


_AtmAturPerfCurr15MinTimeElapsed_Type.__name__ = "Integer32"
_AtmAturPerfCurr15MinTimeElapsed_Object = MibTableColumn
atmAturPerfCurr15MinTimeElapsed = _AtmAturPerfCurr15MinTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 20, 1, 11),
    _AtmAturPerfCurr15MinTimeElapsed_Type()
)
atmAturPerfCurr15MinTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmAturPerfCurr15MinTimeElapsed.setStatus("mandatory")
_AtmAturPerfCurr15MinIdleCells_Type = Integer32
_AtmAturPerfCurr15MinIdleCells_Object = MibTableColumn
atmAturPerfCurr15MinIdleCells = _AtmAturPerfCurr15MinIdleCells_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 20, 1, 12),
    _AtmAturPerfCurr15MinIdleCells_Type()
)
atmAturPerfCurr15MinIdleCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmAturPerfCurr15MinIdleCells.setStatus("mandatory")
_AtmAturPerfCurr15MinDataCells_Type = Integer32
_AtmAturPerfCurr15MinDataCells_Object = MibTableColumn
atmAturPerfCurr15MinDataCells = _AtmAturPerfCurr15MinDataCells_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 20, 1, 13),
    _AtmAturPerfCurr15MinDataCells_Type()
)
atmAturPerfCurr15MinDataCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmAturPerfCurr15MinDataCells.setStatus("mandatory")
_AtmAturPerfCurr15MinLcds_Type = Integer32
_AtmAturPerfCurr15MinLcds_Object = MibTableColumn
atmAturPerfCurr15MinLcds = _AtmAturPerfCurr15MinLcds_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 20, 1, 14),
    _AtmAturPerfCurr15MinLcds_Type()
)
atmAturPerfCurr15MinLcds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmAturPerfCurr15MinLcds.setStatus("mandatory")
_AtmAturPerfCurr15MinHecs_Type = Integer32
_AtmAturPerfCurr15MinHecs_Object = MibTableColumn
atmAturPerfCurr15MinHecs = _AtmAturPerfCurr15MinHecs_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 20, 1, 15),
    _AtmAturPerfCurr15MinHecs_Type()
)
atmAturPerfCurr15MinHecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmAturPerfCurr15MinHecs.setStatus("mandatory")


class _AtmAturPerfCurr1DayTimeElapsed_Type(Integer32):
    """Custom type atmAturPerfCurr1DayTimeElapsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86399),
    )


_AtmAturPerfCurr1DayTimeElapsed_Type.__name__ = "Integer32"
_AtmAturPerfCurr1DayTimeElapsed_Object = MibTableColumn
atmAturPerfCurr1DayTimeElapsed = _AtmAturPerfCurr1DayTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 20, 1, 18),
    _AtmAturPerfCurr1DayTimeElapsed_Type()
)
atmAturPerfCurr1DayTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmAturPerfCurr1DayTimeElapsed.setStatus("mandatory")
_AtmAturPerfCurr1DayIdleCells_Type = Integer32
_AtmAturPerfCurr1DayIdleCells_Object = MibTableColumn
atmAturPerfCurr1DayIdleCells = _AtmAturPerfCurr1DayIdleCells_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 20, 1, 19),
    _AtmAturPerfCurr1DayIdleCells_Type()
)
atmAturPerfCurr1DayIdleCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmAturPerfCurr1DayIdleCells.setStatus("mandatory")
_AtmAturPerfCurr1DayDataCells_Type = Integer32
_AtmAturPerfCurr1DayDataCells_Object = MibTableColumn
atmAturPerfCurr1DayDataCells = _AtmAturPerfCurr1DayDataCells_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 20, 1, 20),
    _AtmAturPerfCurr1DayDataCells_Type()
)
atmAturPerfCurr1DayDataCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmAturPerfCurr1DayDataCells.setStatus("mandatory")
_AtmAturPerfCurr1DayLcds_Type = Integer32
_AtmAturPerfCurr1DayLcds_Object = MibTableColumn
atmAturPerfCurr1DayLcds = _AtmAturPerfCurr1DayLcds_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 20, 1, 21),
    _AtmAturPerfCurr1DayLcds_Type()
)
atmAturPerfCurr1DayLcds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmAturPerfCurr1DayLcds.setStatus("mandatory")
_AtmAturPerfCurr1DayHecs_Type = Integer32
_AtmAturPerfCurr1DayHecs_Object = MibTableColumn
atmAturPerfCurr1DayHecs = _AtmAturPerfCurr1DayHecs_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 20, 1, 22),
    _AtmAturPerfCurr1DayHecs_Type()
)
atmAturPerfCurr1DayHecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmAturPerfCurr1DayHecs.setStatus("mandatory")
_AtmAturPerfPrev1DayIdleCells_Type = Integer32
_AtmAturPerfPrev1DayIdleCells_Object = MibTableColumn
atmAturPerfPrev1DayIdleCells = _AtmAturPerfPrev1DayIdleCells_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 20, 1, 26),
    _AtmAturPerfPrev1DayIdleCells_Type()
)
atmAturPerfPrev1DayIdleCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmAturPerfPrev1DayIdleCells.setStatus("mandatory")
_AtmAturPerfPrev1DayDataCells_Type = Integer32
_AtmAturPerfPrev1DayDataCells_Object = MibTableColumn
atmAturPerfPrev1DayDataCells = _AtmAturPerfPrev1DayDataCells_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 20, 1, 27),
    _AtmAturPerfPrev1DayDataCells_Type()
)
atmAturPerfPrev1DayDataCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmAturPerfPrev1DayDataCells.setStatus("mandatory")
_AtmAturPerfPrev1DayLcds_Type = Integer32
_AtmAturPerfPrev1DayLcds_Object = MibTableColumn
atmAturPerfPrev1DayLcds = _AtmAturPerfPrev1DayLcds_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 20, 1, 28),
    _AtmAturPerfPrev1DayLcds_Type()
)
atmAturPerfPrev1DayLcds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmAturPerfPrev1DayLcds.setStatus("mandatory")
_AtmAturPerfPrev1DayHecs_Type = Integer32
_AtmAturPerfPrev1DayHecs_Object = MibTableColumn
atmAturPerfPrev1DayHecs = _AtmAturPerfPrev1DayHecs_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 20, 1, 29),
    _AtmAturPerfPrev1DayHecs_Type()
)
atmAturPerfPrev1DayHecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmAturPerfPrev1DayHecs.setStatus("mandatory")
_AtmAtucPerfDataTable_Object = MibTable
atmAtucPerfDataTable = _AtmAtucPerfDataTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 21)
)
if mibBuilder.loadTexts:
    atmAtucPerfDataTable.setStatus("mandatory")
_AtmAtucPerfDataEntry_Object = MibTableRow
atmAtucPerfDataEntry = _AtmAtucPerfDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 21, 1)
)
atmAtucPerfDataEntry.setIndexNames(
    (0, "BIANCA-BRICK-ATM2-MIB", "atmAtucPerfIfIndex"),
)
if mibBuilder.loadTexts:
    atmAtucPerfDataEntry.setStatus("mandatory")
_AtmAtucPerfIfIndex_Type = Integer32
_AtmAtucPerfIfIndex_Object = MibTableColumn
atmAtucPerfIfIndex = _AtmAtucPerfIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 21, 1, 1),
    _AtmAtucPerfIfIndex_Type()
)
atmAtucPerfIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmAtucPerfIfIndex.setStatus("mandatory")
_AtmAtucPerfIdleCells_Type = Integer32
_AtmAtucPerfIdleCells_Object = MibTableColumn
atmAtucPerfIdleCells = _AtmAtucPerfIdleCells_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 21, 1, 2),
    _AtmAtucPerfIdleCells_Type()
)
atmAtucPerfIdleCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmAtucPerfIdleCells.setStatus("mandatory")
_AtmAtucPerfDataCells_Type = Integer32
_AtmAtucPerfDataCells_Object = MibTableColumn
atmAtucPerfDataCells = _AtmAtucPerfDataCells_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 21, 1, 3),
    _AtmAtucPerfDataCells_Type()
)
atmAtucPerfDataCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmAtucPerfDataCells.setStatus("mandatory")
_AtmAtucPerfLcds_Type = Integer32
_AtmAtucPerfLcds_Object = MibTableColumn
atmAtucPerfLcds = _AtmAtucPerfLcds_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 21, 1, 4),
    _AtmAtucPerfLcds_Type()
)
atmAtucPerfLcds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmAtucPerfLcds.setStatus("mandatory")
_AtmAtucPerfHecs_Type = Integer32
_AtmAtucPerfHecs_Object = MibTableColumn
atmAtucPerfHecs = _AtmAtucPerfHecs_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 21, 1, 5),
    _AtmAtucPerfHecs_Type()
)
atmAtucPerfHecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmAtucPerfHecs.setStatus("mandatory")


class _AtmAtucPerfCurr15MinTimeElapsed_Type(Integer32):
    """Custom type atmAtucPerfCurr15MinTimeElapsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 899),
    )


_AtmAtucPerfCurr15MinTimeElapsed_Type.__name__ = "Integer32"
_AtmAtucPerfCurr15MinTimeElapsed_Object = MibTableColumn
atmAtucPerfCurr15MinTimeElapsed = _AtmAtucPerfCurr15MinTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 21, 1, 11),
    _AtmAtucPerfCurr15MinTimeElapsed_Type()
)
atmAtucPerfCurr15MinTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmAtucPerfCurr15MinTimeElapsed.setStatus("mandatory")
_AtmAtucPerfCurr15MinIdleCells_Type = Integer32
_AtmAtucPerfCurr15MinIdleCells_Object = MibTableColumn
atmAtucPerfCurr15MinIdleCells = _AtmAtucPerfCurr15MinIdleCells_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 21, 1, 12),
    _AtmAtucPerfCurr15MinIdleCells_Type()
)
atmAtucPerfCurr15MinIdleCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmAtucPerfCurr15MinIdleCells.setStatus("mandatory")
_AtmAtucPerfCurr15MinDataCells_Type = Integer32
_AtmAtucPerfCurr15MinDataCells_Object = MibTableColumn
atmAtucPerfCurr15MinDataCells = _AtmAtucPerfCurr15MinDataCells_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 21, 1, 13),
    _AtmAtucPerfCurr15MinDataCells_Type()
)
atmAtucPerfCurr15MinDataCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmAtucPerfCurr15MinDataCells.setStatus("mandatory")
_AtmAtucPerfCurr15MinLcds_Type = Integer32
_AtmAtucPerfCurr15MinLcds_Object = MibTableColumn
atmAtucPerfCurr15MinLcds = _AtmAtucPerfCurr15MinLcds_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 21, 1, 14),
    _AtmAtucPerfCurr15MinLcds_Type()
)
atmAtucPerfCurr15MinLcds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmAtucPerfCurr15MinLcds.setStatus("mandatory")
_AtmAtucPerfCurr15MinHecs_Type = Integer32
_AtmAtucPerfCurr15MinHecs_Object = MibTableColumn
atmAtucPerfCurr15MinHecs = _AtmAtucPerfCurr15MinHecs_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 21, 1, 15),
    _AtmAtucPerfCurr15MinHecs_Type()
)
atmAtucPerfCurr15MinHecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmAtucPerfCurr15MinHecs.setStatus("mandatory")


class _AtmAtucPerfCurr1DayTimeElapsed_Type(Integer32):
    """Custom type atmAtucPerfCurr1DayTimeElapsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86399),
    )


_AtmAtucPerfCurr1DayTimeElapsed_Type.__name__ = "Integer32"
_AtmAtucPerfCurr1DayTimeElapsed_Object = MibTableColumn
atmAtucPerfCurr1DayTimeElapsed = _AtmAtucPerfCurr1DayTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 21, 1, 18),
    _AtmAtucPerfCurr1DayTimeElapsed_Type()
)
atmAtucPerfCurr1DayTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmAtucPerfCurr1DayTimeElapsed.setStatus("mandatory")
_AtmAtucPerfCurr1DayIdleCells_Type = Integer32
_AtmAtucPerfCurr1DayIdleCells_Object = MibTableColumn
atmAtucPerfCurr1DayIdleCells = _AtmAtucPerfCurr1DayIdleCells_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 21, 1, 19),
    _AtmAtucPerfCurr1DayIdleCells_Type()
)
atmAtucPerfCurr1DayIdleCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmAtucPerfCurr1DayIdleCells.setStatus("mandatory")
_AtmAtucPerfCurr1DayDataCells_Type = Integer32
_AtmAtucPerfCurr1DayDataCells_Object = MibTableColumn
atmAtucPerfCurr1DayDataCells = _AtmAtucPerfCurr1DayDataCells_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 21, 1, 20),
    _AtmAtucPerfCurr1DayDataCells_Type()
)
atmAtucPerfCurr1DayDataCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmAtucPerfCurr1DayDataCells.setStatus("mandatory")
_AtmAtucPerfCurr1DayLcds_Type = Integer32
_AtmAtucPerfCurr1DayLcds_Object = MibTableColumn
atmAtucPerfCurr1DayLcds = _AtmAtucPerfCurr1DayLcds_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 21, 1, 21),
    _AtmAtucPerfCurr1DayLcds_Type()
)
atmAtucPerfCurr1DayLcds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmAtucPerfCurr1DayLcds.setStatus("mandatory")
_AtmAtucPerfCurr1DayHecs_Type = Integer32
_AtmAtucPerfCurr1DayHecs_Object = MibTableColumn
atmAtucPerfCurr1DayHecs = _AtmAtucPerfCurr1DayHecs_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 21, 1, 22),
    _AtmAtucPerfCurr1DayHecs_Type()
)
atmAtucPerfCurr1DayHecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmAtucPerfCurr1DayHecs.setStatus("mandatory")
_AtmAtucPerfPrev1DayIdleCells_Type = Integer32
_AtmAtucPerfPrev1DayIdleCells_Object = MibTableColumn
atmAtucPerfPrev1DayIdleCells = _AtmAtucPerfPrev1DayIdleCells_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 21, 1, 26),
    _AtmAtucPerfPrev1DayIdleCells_Type()
)
atmAtucPerfPrev1DayIdleCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmAtucPerfPrev1DayIdleCells.setStatus("mandatory")
_AtmAtucPerfPrev1DayDataCells_Type = Integer32
_AtmAtucPerfPrev1DayDataCells_Object = MibTableColumn
atmAtucPerfPrev1DayDataCells = _AtmAtucPerfPrev1DayDataCells_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 21, 1, 27),
    _AtmAtucPerfPrev1DayDataCells_Type()
)
atmAtucPerfPrev1DayDataCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmAtucPerfPrev1DayDataCells.setStatus("mandatory")
_AtmAtucPerfPrev1DayLcds_Type = Integer32
_AtmAtucPerfPrev1DayLcds_Object = MibTableColumn
atmAtucPerfPrev1DayLcds = _AtmAtucPerfPrev1DayLcds_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 21, 1, 28),
    _AtmAtucPerfPrev1DayLcds_Type()
)
atmAtucPerfPrev1DayLcds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmAtucPerfPrev1DayLcds.setStatus("mandatory")
_AtmAtucPerfPrev1DayHecs_Type = Integer32
_AtmAtucPerfPrev1DayHecs_Object = MibTableColumn
atmAtucPerfPrev1DayHecs = _AtmAtucPerfPrev1DayHecs_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 16, 21, 1, 29),
    _AtmAtucPerfPrev1DayHecs_Type()
)
atmAtucPerfPrev1DayHecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmAtucPerfPrev1DayHecs.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BIANCA-BRICK-ATM2-MIB",
    **{"bintec": bintec,
       "bibo": bibo,
       "atm": atm,
       "atmIfTable": atmIfTable,
       "atmIfEntry": atmIfEntry,
       "atmIfIndex": atmIfIndex,
       "atmIfType": atmIfType,
       "atmIfDescr": atmIfDescr,
       "atmIfAdminStatus": atmIfAdminStatus,
       "atmIfOperStatus": atmIfOperStatus,
       "atmIfLastChange": atmIfLastChange,
       "atmIfMaxTxRate": atmIfMaxTxRate,
       "atmIfOperMode": atmIfOperMode,
       "atmIfInPkts": atmIfInPkts,
       "atmIfOutPkts": atmIfOutPkts,
       "atmIfRxSpeed": atmIfRxSpeed,
       "atmIfTxSpeed": atmIfTxSpeed,
       "atmIfInOctets": atmIfInOctets,
       "atmIfInDiscards": atmIfInDiscards,
       "atmIfInErrors": atmIfInErrors,
       "atmIfOutOctets": atmIfOutOctets,
       "atmIfOutDiscards": atmIfOutDiscards,
       "atmIfOutErrors": atmIfOutErrors,
       "atmVpcTable": atmVpcTable,
       "atmVpcEntry": atmVpcEntry,
       "atmVpcPortIndex": atmVpcPortIndex,
       "atmVpcVpi": atmVpcVpi,
       "atmVpcOperStatus": atmVpcOperStatus,
       "atmVccTable": atmVccTable,
       "atmVccEntry": atmVccEntry,
       "atmVccPortIndex": atmVccPortIndex,
       "atmVccVpi": atmVccVpi,
       "atmVccVci": atmVccVci,
       "atmVccOperStatus": atmVccOperStatus,
       "atmOamTable": atmOamTable,
       "atmOamEntry": atmOamEntry,
       "atmOamAtmIfIndex": atmOamAtmIfIndex,
       "atmOamVpi": atmOamVpi,
       "atmOamVci": atmOamVci,
       "atmOamFlowLevel": atmOamFlowLevel,
       "atmOamLoopbackEnd2End": atmOamLoopbackEnd2End,
       "atmOamLoopbackSegment": atmOamLoopbackSegment,
       "atmOamLoopbackEnd2EndInterval": atmOamLoopbackEnd2EndInterval,
       "atmOamLoopbackSegmentInterval": atmOamLoopbackSegmentInterval,
       "atmOamLoopbackEnd2EndMaxPending": atmOamLoopbackEnd2EndMaxPending,
       "atmOamLoopbackSegmentMaxPending": atmOamLoopbackSegmentMaxPending,
       "atmOamCCEnd2EndActivation": atmOamCCEnd2EndActivation,
       "atmOamCCSegmentActivation": atmOamCCSegmentActivation,
       "atmOamCCEnd2EndDirection": atmOamCCEnd2EndDirection,
       "atmOamCCSegmentDirection": atmOamCCSegmentDirection,
       "atmOamStatTable": atmOamStatTable,
       "atmOamStatEntry": atmOamStatEntry,
       "atmOamStatAtmIfIndex": atmOamStatAtmIfIndex,
       "atmOamStatVpi": atmOamStatVpi,
       "atmOamStatVci": atmOamStatVci,
       "atmOamStatFlowType": atmOamStatFlowType,
       "atmOamStatLoopbackTxCells": atmOamStatLoopbackTxCells,
       "atmOamStatLoopbackRxCells": atmOamStatLoopbackRxCells,
       "atmOamStatLoopbackPending": atmOamStatLoopbackPending,
       "atmOamStatLoopbackCorr": atmOamStatLoopbackCorr,
       "atmOamStatAisState": atmOamStatAisState,
       "atmOamStatAisTxCells": atmOamStatAisTxCells,
       "atmOamStatAisRxCells": atmOamStatAisRxCells,
       "atmOamStatTotalAisTxCells": atmOamStatTotalAisTxCells,
       "atmOamStatTotalAisRxCells": atmOamStatTotalAisRxCells,
       "atmOamStatRdiState": atmOamStatRdiState,
       "atmOamStatRdiTxCells": atmOamStatRdiTxCells,
       "atmOamStatRdiRxCells": atmOamStatRdiRxCells,
       "atmOamStatTotalRdiTxCells": atmOamStatTotalRdiTxCells,
       "atmOamStatTotalRdiRxCells": atmOamStatTotalRdiRxCells,
       "atmOamStatCCActivatorState": atmOamStatCCActivatorState,
       "atmOamStatCCActivatorDirection": atmOamStatCCActivatorDirection,
       "atmOamStatCCActivatorCorr": atmOamStatCCActivatorCorr,
       "atmOamStatCCResponderState": atmOamStatCCResponderState,
       "atmOamStatCCResponderDirection": atmOamStatCCResponderDirection,
       "atmOamStatCCResponderCorr": atmOamStatCCResponderCorr,
       "atmOamStatCCTxCells": atmOamStatCCTxCells,
       "atmOamStatCCRxCells": atmOamStatCCRxCells,
       "ethoaPvcTable": ethoaPvcTable,
       "ethoaPvcEntry": ethoaPvcEntry,
       "ethoaPvcIfIndex": ethoaPvcIfIndex,
       "ethoaPvcDescr": ethoaPvcDescr,
       "ethoaPvcAtmIfIndex": ethoaPvcAtmIfIndex,
       "ethoaPvcVpi": ethoaPvcVpi,
       "ethoaPvcVci": ethoaPvcVci,
       "ethoaPvcEncapsulation": ethoaPvcEncapsulation,
       "ethoaPvcPhysAddress": ethoaPvcPhysAddress,
       "rpoaPvcTable": rpoaPvcTable,
       "rpoaPvcEntry": rpoaPvcEntry,
       "rpoaPvcIfIndex": rpoaPvcIfIndex,
       "rpoaPvcDescr": rpoaPvcDescr,
       "rpoaPvcAtmIfIndex": rpoaPvcAtmIfIndex,
       "rpoaPvcVpi": rpoaPvcVpi,
       "rpoaPvcVci": rpoaPvcVci,
       "rpoaPvcEncapsulation": rpoaPvcEncapsulation,
       "pppoaPvcTable": pppoaPvcTable,
       "pppoaPvcEntry": pppoaPvcEntry,
       "pppoaPvcIfIndex": pppoaPvcIfIndex,
       "pppoaPvcDescr": pppoaPvcDescr,
       "pppoaPvcAtmIfIndex": pppoaPvcAtmIfIndex,
       "pppoaPvcVpi": pppoaPvcVpi,
       "pppoaPvcVci": pppoaPvcVci,
       "pppoaPvcEncapsulation": pppoaPvcEncapsulation,
       "pppoaPvcClientType": pppoaPvcClientType,
       "atmQosVccTable": atmQosVccTable,
       "atmQosVccEntry": atmQosVccEntry,
       "atmQosVccAtmIfIndex": atmQosVccAtmIfIndex,
       "atmQosVccVpi": atmQosVccVpi,
       "atmQosVccVci": atmQosVccVci,
       "atmQosVccService": atmQosVccService,
       "atmQosVccOutPcr": atmQosVccOutPcr,
       "atmQosVccOutScr": atmQosVccOutScr,
       "atmQosVccOutMbs": atmQosVccOutMbs,
       "atmQosVccOutMcr": atmQosVccOutMcr,
       "atmAturPerfDataTable": atmAturPerfDataTable,
       "atmAturPerfDataEntry": atmAturPerfDataEntry,
       "atmAturPerfIfIndex": atmAturPerfIfIndex,
       "atmAturPerfIdleCells": atmAturPerfIdleCells,
       "atmAturPerfDataCells": atmAturPerfDataCells,
       "atmAturPerfLcds": atmAturPerfLcds,
       "atmAturPerfHecs": atmAturPerfHecs,
       "atmAturPerfCurr15MinTimeElapsed": atmAturPerfCurr15MinTimeElapsed,
       "atmAturPerfCurr15MinIdleCells": atmAturPerfCurr15MinIdleCells,
       "atmAturPerfCurr15MinDataCells": atmAturPerfCurr15MinDataCells,
       "atmAturPerfCurr15MinLcds": atmAturPerfCurr15MinLcds,
       "atmAturPerfCurr15MinHecs": atmAturPerfCurr15MinHecs,
       "atmAturPerfCurr1DayTimeElapsed": atmAturPerfCurr1DayTimeElapsed,
       "atmAturPerfCurr1DayIdleCells": atmAturPerfCurr1DayIdleCells,
       "atmAturPerfCurr1DayDataCells": atmAturPerfCurr1DayDataCells,
       "atmAturPerfCurr1DayLcds": atmAturPerfCurr1DayLcds,
       "atmAturPerfCurr1DayHecs": atmAturPerfCurr1DayHecs,
       "atmAturPerfPrev1DayIdleCells": atmAturPerfPrev1DayIdleCells,
       "atmAturPerfPrev1DayDataCells": atmAturPerfPrev1DayDataCells,
       "atmAturPerfPrev1DayLcds": atmAturPerfPrev1DayLcds,
       "atmAturPerfPrev1DayHecs": atmAturPerfPrev1DayHecs,
       "atmAtucPerfDataTable": atmAtucPerfDataTable,
       "atmAtucPerfDataEntry": atmAtucPerfDataEntry,
       "atmAtucPerfIfIndex": atmAtucPerfIfIndex,
       "atmAtucPerfIdleCells": atmAtucPerfIdleCells,
       "atmAtucPerfDataCells": atmAtucPerfDataCells,
       "atmAtucPerfLcds": atmAtucPerfLcds,
       "atmAtucPerfHecs": atmAtucPerfHecs,
       "atmAtucPerfCurr15MinTimeElapsed": atmAtucPerfCurr15MinTimeElapsed,
       "atmAtucPerfCurr15MinIdleCells": atmAtucPerfCurr15MinIdleCells,
       "atmAtucPerfCurr15MinDataCells": atmAtucPerfCurr15MinDataCells,
       "atmAtucPerfCurr15MinLcds": atmAtucPerfCurr15MinLcds,
       "atmAtucPerfCurr15MinHecs": atmAtucPerfCurr15MinHecs,
       "atmAtucPerfCurr1DayTimeElapsed": atmAtucPerfCurr1DayTimeElapsed,
       "atmAtucPerfCurr1DayIdleCells": atmAtucPerfCurr1DayIdleCells,
       "atmAtucPerfCurr1DayDataCells": atmAtucPerfCurr1DayDataCells,
       "atmAtucPerfCurr1DayLcds": atmAtucPerfCurr1DayLcds,
       "atmAtucPerfCurr1DayHecs": atmAtucPerfCurr1DayHecs,
       "atmAtucPerfPrev1DayIdleCells": atmAtucPerfPrev1DayIdleCells,
       "atmAtucPerfPrev1DayDataCells": atmAtucPerfPrev1DayDataCells,
       "atmAtucPerfPrev1DayLcds": atmAtucPerfPrev1DayLcds,
       "atmAtucPerfPrev1DayHecs": atmAtucPerfPrev1DayHecs}
)
