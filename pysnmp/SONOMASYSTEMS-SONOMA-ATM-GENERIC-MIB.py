# SNMP MIB module (SONOMASYSTEMS-SONOMA-ATM-GENERIC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SONOMASYSTEMS-SONOMA-ATM-GENERIC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:56:41 2024
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

(sonomaATM,) = mibBuilder.importSymbols(
    "SONOMASYSTEMS-SONOMA-MIB",
    "sonomaATM")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SonomaGenericATMGroup_ObjectIdentity = ObjectIdentity
sonomaGenericATMGroup = _SonomaGenericATMGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1)
)
_AtmGenericPhysGroup_ObjectIdentity = ObjectIdentity
atmGenericPhysGroup = _AtmGenericPhysGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 1)
)
_AtmGenPhysTable_Object = MibTable
atmGenPhysTable = _AtmGenPhysTable_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 1, 1)
)
if mibBuilder.loadTexts:
    atmGenPhysTable.setStatus("mandatory")
_AtmGenPhysEntry_Object = MibTableRow
atmGenPhysEntry = _AtmGenPhysEntry_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 1, 1, 1)
)
atmGenPhysEntry.setIndexNames(
    (0, "SONOMASYSTEMS-SONOMA-ATM-GENERIC-MIB", "atmGenPhysIndex"),
)
if mibBuilder.loadTexts:
    atmGenPhysEntry.setStatus("mandatory")
_AtmGenPhysIndex_Type = Integer32
_AtmGenPhysIndex_Object = MibTableColumn
atmGenPhysIndex = _AtmGenPhysIndex_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 1, 1, 1, 1),
    _AtmGenPhysIndex_Type()
)
atmGenPhysIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmGenPhysIndex.setStatus("mandatory")
_AtmGenPhysAal5Mtu_Type = Integer32
_AtmGenPhysAal5Mtu_Object = MibTableColumn
atmGenPhysAal5Mtu = _AtmGenPhysAal5Mtu_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 1, 1, 1, 2),
    _AtmGenPhysAal5Mtu_Type()
)
atmGenPhysAal5Mtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmGenPhysAal5Mtu.setStatus("mandatory")
_AtmGenPhysAal5CrcErrors_Type = Counter32
_AtmGenPhysAal5CrcErrors_Object = MibTableColumn
atmGenPhysAal5CrcErrors = _AtmGenPhysAal5CrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 1, 1, 1, 3),
    _AtmGenPhysAal5CrcErrors_Type()
)
atmGenPhysAal5CrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmGenPhysAal5CrcErrors.setStatus("mandatory")
_AtmGenPhysAal5OverSizedSDUs_Type = Counter32
_AtmGenPhysAal5OverSizedSDUs_Object = MibTableColumn
atmGenPhysAal5OverSizedSDUs = _AtmGenPhysAal5OverSizedSDUs_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 1, 1, 1, 4),
    _AtmGenPhysAal5OverSizedSDUs_Type()
)
atmGenPhysAal5OverSizedSDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmGenPhysAal5OverSizedSDUs.setStatus("mandatory")
_AtmGenPhysAal5DiscardPDU_Type = Counter32
_AtmGenPhysAal5DiscardPDU_Object = MibTableColumn
atmGenPhysAal5DiscardPDU = _AtmGenPhysAal5DiscardPDU_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 1, 1, 1, 5),
    _AtmGenPhysAal5DiscardPDU_Type()
)
atmGenPhysAal5DiscardPDU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmGenPhysAal5DiscardPDU.setStatus("mandatory")
_AtmGenPhysHECErrors_Type = Counter32
_AtmGenPhysHECErrors_Object = MibTableColumn
atmGenPhysHECErrors = _AtmGenPhysHECErrors_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 1, 1, 1, 6),
    _AtmGenPhysHECErrors_Type()
)
atmGenPhysHECErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmGenPhysHECErrors.setStatus("mandatory")
_AtmGenPhysUnknownProtocols_Type = Counter32
_AtmGenPhysUnknownProtocols_Object = MibTableColumn
atmGenPhysUnknownProtocols = _AtmGenPhysUnknownProtocols_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 1, 1, 1, 7),
    _AtmGenPhysUnknownProtocols_Type()
)
atmGenPhysUnknownProtocols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmGenPhysUnknownProtocols.setStatus("mandatory")
_AtmGenPhysCellsReceived_Type = Counter32
_AtmGenPhysCellsReceived_Object = MibTableColumn
atmGenPhysCellsReceived = _AtmGenPhysCellsReceived_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 1, 1, 1, 8),
    _AtmGenPhysCellsReceived_Type()
)
atmGenPhysCellsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmGenPhysCellsReceived.setStatus("mandatory")
_AtmGenPhysCellsTransmitted_Type = Counter32
_AtmGenPhysCellsTransmitted_Object = MibTableColumn
atmGenPhysCellsTransmitted = _AtmGenPhysCellsTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 1, 1, 1, 9),
    _AtmGenPhysCellsTransmitted_Type()
)
atmGenPhysCellsTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmGenPhysCellsTransmitted.setStatus("mandatory")
_AtmGenPhysRxBufStarvation_Type = Counter32
_AtmGenPhysRxBufStarvation_Object = MibTableColumn
atmGenPhysRxBufStarvation = _AtmGenPhysRxBufStarvation_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 1, 1, 1, 10),
    _AtmGenPhysRxBufStarvation_Type()
)
atmGenPhysRxBufStarvation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmGenPhysRxBufStarvation.setStatus("mandatory")
_AtmGenPhysRxFreeze_Type = Counter32
_AtmGenPhysRxFreeze_Object = MibTableColumn
atmGenPhysRxFreeze = _AtmGenPhysRxFreeze_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 1, 1, 1, 11),
    _AtmGenPhysRxFreeze_Type()
)
atmGenPhysRxFreeze.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmGenPhysRxFreeze.setStatus("mandatory")
_AtmGenPhysTxFreeze_Type = Counter32
_AtmGenPhysTxFreeze_Object = MibTableColumn
atmGenPhysTxFreeze = _AtmGenPhysTxFreeze_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 1, 1, 1, 12),
    _AtmGenPhysTxFreeze_Type()
)
atmGenPhysTxFreeze.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmGenPhysTxFreeze.setStatus("mandatory")
_AtmGenRateTable_Object = MibTable
atmGenRateTable = _AtmGenRateTable_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 1, 2)
)
if mibBuilder.loadTexts:
    atmGenRateTable.setStatus("mandatory")
_AtmGenRateEntry_Object = MibTableRow
atmGenRateEntry = _AtmGenRateEntry_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 1, 2, 1)
)
atmGenRateEntry.setIndexNames(
    (0, "SONOMASYSTEMS-SONOMA-ATM-GENERIC-MIB", "atmGenRatePhysIndex"),
)
if mibBuilder.loadTexts:
    atmGenRateEntry.setStatus("mandatory")


class _AtmGenRatePhysIndex_Type(Integer32):
    """Custom type atmGenRatePhysIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_AtmGenRatePhysIndex_Type.__name__ = "Integer32"
_AtmGenRatePhysIndex_Object = MibTableColumn
atmGenRatePhysIndex = _AtmGenRatePhysIndex_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 1, 2, 1, 1),
    _AtmGenRatePhysIndex_Type()
)
atmGenRatePhysIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmGenRatePhysIndex.setStatus("mandatory")


class _AtmGenRateQueOne_Type(Integer32):
    """Custom type atmGenRateQueOne based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 135150),
    )


_AtmGenRateQueOne_Type.__name__ = "Integer32"
_AtmGenRateQueOne_Object = MibTableColumn
atmGenRateQueOne = _AtmGenRateQueOne_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 1, 2, 1, 2),
    _AtmGenRateQueOne_Type()
)
atmGenRateQueOne.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmGenRateQueOne.setStatus("mandatory")


class _AtmGenRateQueTwo_Type(Integer32):
    """Custom type atmGenRateQueTwo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 135150),
    )


_AtmGenRateQueTwo_Type.__name__ = "Integer32"
_AtmGenRateQueTwo_Object = MibTableColumn
atmGenRateQueTwo = _AtmGenRateQueTwo_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 1, 2, 1, 3),
    _AtmGenRateQueTwo_Type()
)
atmGenRateQueTwo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmGenRateQueTwo.setStatus("mandatory")


class _AtmGenRateQueThree_Type(Integer32):
    """Custom type atmGenRateQueThree based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 135150),
    )


_AtmGenRateQueThree_Type.__name__ = "Integer32"
_AtmGenRateQueThree_Object = MibTableColumn
atmGenRateQueThree = _AtmGenRateQueThree_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 1, 2, 1, 4),
    _AtmGenRateQueThree_Type()
)
atmGenRateQueThree.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmGenRateQueThree.setStatus("mandatory")


class _AtmGenRateQueFour_Type(Integer32):
    """Custom type atmGenRateQueFour based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 135150),
    )


_AtmGenRateQueFour_Type.__name__ = "Integer32"
_AtmGenRateQueFour_Object = MibTableColumn
atmGenRateQueFour = _AtmGenRateQueFour_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 1, 2, 1, 5),
    _AtmGenRateQueFour_Type()
)
atmGenRateQueFour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmGenRateQueFour.setStatus("mandatory")


class _AtmGenRateQueFive_Type(Integer32):
    """Custom type atmGenRateQueFive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 135150),
    )


_AtmGenRateQueFive_Type.__name__ = "Integer32"
_AtmGenRateQueFive_Object = MibTableColumn
atmGenRateQueFive = _AtmGenRateQueFive_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 1, 2, 1, 6),
    _AtmGenRateQueFive_Type()
)
atmGenRateQueFive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmGenRateQueFive.setStatus("mandatory")


class _AtmGenRateQueSix_Type(Integer32):
    """Custom type atmGenRateQueSix based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 135150),
    )


_AtmGenRateQueSix_Type.__name__ = "Integer32"
_AtmGenRateQueSix_Object = MibTableColumn
atmGenRateQueSix = _AtmGenRateQueSix_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 1, 2, 1, 7),
    _AtmGenRateQueSix_Type()
)
atmGenRateQueSix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmGenRateQueSix.setStatus("mandatory")


class _AtmGenRateQueSeven_Type(Integer32):
    """Custom type atmGenRateQueSeven based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 135150),
    )


_AtmGenRateQueSeven_Type.__name__ = "Integer32"
_AtmGenRateQueSeven_Object = MibTableColumn
atmGenRateQueSeven = _AtmGenRateQueSeven_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 1, 2, 1, 8),
    _AtmGenRateQueSeven_Type()
)
atmGenRateQueSeven.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmGenRateQueSeven.setStatus("mandatory")


class _AtmGenRateQueEight_Type(Integer32):
    """Custom type atmGenRateQueEight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 135150),
    )


_AtmGenRateQueEight_Type.__name__ = "Integer32"
_AtmGenRateQueEight_Object = MibTableColumn
atmGenRateQueEight = _AtmGenRateQueEight_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 1, 2, 1, 9),
    _AtmGenRateQueEight_Type()
)
atmGenRateQueEight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmGenRateQueEight.setStatus("mandatory")
_AtmGenRateQTable_Object = MibTable
atmGenRateQTable = _AtmGenRateQTable_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 1, 3)
)
if mibBuilder.loadTexts:
    atmGenRateQTable.setStatus("mandatory")
_AtmGenRateQEntry_Object = MibTableRow
atmGenRateQEntry = _AtmGenRateQEntry_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 1, 3, 1)
)
atmGenRateQEntry.setIndexNames(
    (0, "SONOMASYSTEMS-SONOMA-ATM-GENERIC-MIB", "atmGenRateQPhysIndex"),
    (0, "SONOMASYSTEMS-SONOMA-ATM-GENERIC-MIB", "atmGenRateQNumber"),
)
if mibBuilder.loadTexts:
    atmGenRateQEntry.setStatus("mandatory")


class _AtmGenRateQPhysIndex_Type(Integer32):
    """Custom type atmGenRateQPhysIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_AtmGenRateQPhysIndex_Type.__name__ = "Integer32"
_AtmGenRateQPhysIndex_Object = MibTableColumn
atmGenRateQPhysIndex = _AtmGenRateQPhysIndex_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 1, 3, 1, 1),
    _AtmGenRateQPhysIndex_Type()
)
atmGenRateQPhysIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmGenRateQPhysIndex.setStatus("mandatory")


class _AtmGenRateQNumber_Type(Integer32):
    """Custom type atmGenRateQNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AtmGenRateQNumber_Type.__name__ = "Integer32"
_AtmGenRateQNumber_Object = MibTableColumn
atmGenRateQNumber = _AtmGenRateQNumber_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 1, 3, 1, 2),
    _AtmGenRateQNumber_Type()
)
atmGenRateQNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmGenRateQNumber.setStatus("mandatory")


class _AtmGenRateQueue_Type(Integer32):
    """Custom type atmGenRateQueue based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 135150),
    )


_AtmGenRateQueue_Type.__name__ = "Integer32"
_AtmGenRateQueue_Object = MibTableColumn
atmGenRateQueue = _AtmGenRateQueue_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 1, 3, 1, 3),
    _AtmGenRateQueue_Type()
)
atmGenRateQueue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmGenRateQueue.setStatus("mandatory")
_AtmGenericVclGroup_ObjectIdentity = ObjectIdentity
atmGenericVclGroup = _AtmGenericVclGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 2)
)
_AtmGenVclTable_Object = MibTable
atmGenVclTable = _AtmGenVclTable_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 2, 1)
)
if mibBuilder.loadTexts:
    atmGenVclTable.setStatus("mandatory")
_AtmGenVclEntry_Object = MibTableRow
atmGenVclEntry = _AtmGenVclEntry_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 2, 1, 1)
)
atmGenVclEntry.setIndexNames(
    (0, "SONOMASYSTEMS-SONOMA-ATM-GENERIC-MIB", "atmGenVclIfIndex"),
    (0, "SONOMASYSTEMS-SONOMA-ATM-GENERIC-MIB", "atmGenVclVpi"),
    (0, "SONOMASYSTEMS-SONOMA-ATM-GENERIC-MIB", "atmGenVclVci"),
)
if mibBuilder.loadTexts:
    atmGenVclEntry.setStatus("mandatory")
_AtmGenVclIfIndex_Type = Integer32
_AtmGenVclIfIndex_Object = MibTableColumn
atmGenVclIfIndex = _AtmGenVclIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 2, 1, 1, 1),
    _AtmGenVclIfIndex_Type()
)
atmGenVclIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmGenVclIfIndex.setStatus("mandatory")


class _AtmGenVclVpi_Type(Integer32):
    """Custom type atmGenVclVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AtmGenVclVpi_Type.__name__ = "Integer32"
_AtmGenVclVpi_Object = MibTableColumn
atmGenVclVpi = _AtmGenVclVpi_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 2, 1, 1, 2),
    _AtmGenVclVpi_Type()
)
atmGenVclVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmGenVclVpi.setStatus("mandatory")


class _AtmGenVclVci_Type(Integer32):
    """Custom type atmGenVclVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1023),
    )


_AtmGenVclVci_Type.__name__ = "Integer32"
_AtmGenVclVci_Object = MibTableColumn
atmGenVclVci = _AtmGenVclVci_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 2, 1, 1, 3),
    _AtmGenVclVci_Type()
)
atmGenVclVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmGenVclVci.setStatus("mandatory")


class _AtmGenVclRateQ_Type(Integer32):
    """Custom type atmGenVclRateQ based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AtmGenVclRateQ_Type.__name__ = "Integer32"
_AtmGenVclRateQ_Object = MibTableColumn
atmGenVclRateQ = _AtmGenVclRateQ_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 2, 1, 1, 4),
    _AtmGenVclRateQ_Type()
)
atmGenVclRateQ.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmGenVclRateQ.setStatus("mandatory")


class _AtmGenVclAction_Type(Integer32):
    """Custom type atmGenVclAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("create", 5),
          ("destroy", 6))
    )


_AtmGenVclAction_Type.__name__ = "Integer32"
_AtmGenVclAction_Object = MibTableColumn
atmGenVclAction = _AtmGenVclAction_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 2, 1, 1, 5),
    _AtmGenVclAction_Type()
)
atmGenVclAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmGenVclAction.setStatus("mandatory")
_AtmGenVclTmTable_Object = MibTable
atmGenVclTmTable = _AtmGenVclTmTable_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 2, 2)
)
if mibBuilder.loadTexts:
    atmGenVclTmTable.setStatus("mandatory")
_AtmGenVclTmEntry_Object = MibTableRow
atmGenVclTmEntry = _AtmGenVclTmEntry_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 2, 2, 1)
)
atmGenVclTmEntry.setIndexNames(
    (0, "SONOMASYSTEMS-SONOMA-ATM-GENERIC-MIB", "atmGenVclTmIfIndex"),
    (0, "SONOMASYSTEMS-SONOMA-ATM-GENERIC-MIB", "atmGenVclTmVpi"),
    (0, "SONOMASYSTEMS-SONOMA-ATM-GENERIC-MIB", "atmGenVclTmVci"),
)
if mibBuilder.loadTexts:
    atmGenVclTmEntry.setStatus("mandatory")
_AtmGenVclTmIfIndex_Type = Integer32
_AtmGenVclTmIfIndex_Object = MibTableColumn
atmGenVclTmIfIndex = _AtmGenVclTmIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 2, 2, 1, 1),
    _AtmGenVclTmIfIndex_Type()
)
atmGenVclTmIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmGenVclTmIfIndex.setStatus("mandatory")


class _AtmGenVclTmVpi_Type(Integer32):
    """Custom type atmGenVclTmVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AtmGenVclTmVpi_Type.__name__ = "Integer32"
_AtmGenVclTmVpi_Object = MibTableColumn
atmGenVclTmVpi = _AtmGenVclTmVpi_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 2, 2, 1, 2),
    _AtmGenVclTmVpi_Type()
)
atmGenVclTmVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmGenVclTmVpi.setStatus("mandatory")


class _AtmGenVclTmVci_Type(Integer32):
    """Custom type atmGenVclTmVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_AtmGenVclTmVci_Type.__name__ = "Integer32"
_AtmGenVclTmVci_Object = MibTableColumn
atmGenVclTmVci = _AtmGenVclTmVci_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 2, 2, 1, 3),
    _AtmGenVclTmVci_Type()
)
atmGenVclTmVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmGenVclTmVci.setStatus("mandatory")


class _AtmGenVclTmPCR_Type(Integer32):
    """Custom type atmGenVclTmPCR based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_AtmGenVclTmPCR_Type.__name__ = "Integer32"
_AtmGenVclTmPCR_Object = MibTableColumn
atmGenVclTmPCR = _AtmGenVclTmPCR_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 2, 2, 1, 4),
    _AtmGenVclTmPCR_Type()
)
atmGenVclTmPCR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmGenVclTmPCR.setStatus("mandatory")


class _AtmGenVclTmSCR_Type(Integer32):
    """Custom type atmGenVclTmSCR based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_AtmGenVclTmSCR_Type.__name__ = "Integer32"
_AtmGenVclTmSCR_Object = MibTableColumn
atmGenVclTmSCR = _AtmGenVclTmSCR_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 2, 2, 1, 5),
    _AtmGenVclTmSCR_Type()
)
atmGenVclTmSCR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmGenVclTmSCR.setStatus("mandatory")


class _AtmGenVclTmMBS_Type(Integer32):
    """Custom type atmGenVclTmMBS based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_AtmGenVclTmMBS_Type.__name__ = "Integer32"
_AtmGenVclTmMBS_Object = MibTableColumn
atmGenVclTmMBS = _AtmGenVclTmMBS_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 2, 2, 1, 6),
    _AtmGenVclTmMBS_Type()
)
atmGenVclTmMBS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmGenVclTmMBS.setStatus("mandatory")


class _AtmGenVclTmAction_Type(Integer32):
    """Custom type atmGenVclTmAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("create", 5),
          ("destroy", 6))
    )


_AtmGenVclTmAction_Type.__name__ = "Integer32"
_AtmGenVclTmAction_Object = MibTableColumn
atmGenVclTmAction = _AtmGenVclTmAction_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 2, 2, 1, 7),
    _AtmGenVclTmAction_Type()
)
atmGenVclTmAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmGenVclTmAction.setStatus("mandatory")
_AtmGenVclStatsTable_Object = MibTable
atmGenVclStatsTable = _AtmGenVclStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 2, 3)
)
if mibBuilder.loadTexts:
    atmGenVclStatsTable.setStatus("mandatory")
_AtmGenVclStatsEntry_Object = MibTableRow
atmGenVclStatsEntry = _AtmGenVclStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 2, 3, 1)
)
atmGenVclStatsEntry.setIndexNames(
    (0, "SONOMASYSTEMS-SONOMA-ATM-GENERIC-MIB", "atmGenVclStatsIfIndex"),
    (0, "SONOMASYSTEMS-SONOMA-ATM-GENERIC-MIB", "atmGenVclStatsVpi"),
    (0, "SONOMASYSTEMS-SONOMA-ATM-GENERIC-MIB", "atmGenVclStatsVci"),
)
if mibBuilder.loadTexts:
    atmGenVclStatsEntry.setStatus("mandatory")
_AtmGenVclStatsIfIndex_Type = Integer32
_AtmGenVclStatsIfIndex_Object = MibTableColumn
atmGenVclStatsIfIndex = _AtmGenVclStatsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 2, 3, 1, 1),
    _AtmGenVclStatsIfIndex_Type()
)
atmGenVclStatsIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmGenVclStatsIfIndex.setStatus("mandatory")


class _AtmGenVclStatsVpi_Type(Integer32):
    """Custom type atmGenVclStatsVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AtmGenVclStatsVpi_Type.__name__ = "Integer32"
_AtmGenVclStatsVpi_Object = MibTableColumn
atmGenVclStatsVpi = _AtmGenVclStatsVpi_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 2, 3, 1, 2),
    _AtmGenVclStatsVpi_Type()
)
atmGenVclStatsVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmGenVclStatsVpi.setStatus("mandatory")


class _AtmGenVclStatsVci_Type(Integer32):
    """Custom type atmGenVclStatsVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(35, 1023),
    )


_AtmGenVclStatsVci_Type.__name__ = "Integer32"
_AtmGenVclStatsVci_Object = MibTableColumn
atmGenVclStatsVci = _AtmGenVclStatsVci_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 2, 3, 1, 3),
    _AtmGenVclStatsVci_Type()
)
atmGenVclStatsVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmGenVclStatsVci.setStatus("mandatory")
_AtmGenVclStatsCellsReceived_Type = Counter32
_AtmGenVclStatsCellsReceived_Object = MibTableColumn
atmGenVclStatsCellsReceived = _AtmGenVclStatsCellsReceived_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 2, 3, 1, 4),
    _AtmGenVclStatsCellsReceived_Type()
)
atmGenVclStatsCellsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmGenVclStatsCellsReceived.setStatus("mandatory")
_AtmGenVclStatsCellsTransmitted_Type = Counter32
_AtmGenVclStatsCellsTransmitted_Object = MibTableColumn
atmGenVclStatsCellsTransmitted = _AtmGenVclStatsCellsTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 2, 3, 1, 5),
    _AtmGenVclStatsCellsTransmitted_Type()
)
atmGenVclStatsCellsTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmGenVclStatsCellsTransmitted.setStatus("mandatory")
_AtmGenVclStatsOamAisRcvCells_Type = Counter32
_AtmGenVclStatsOamAisRcvCells_Object = MibTableColumn
atmGenVclStatsOamAisRcvCells = _AtmGenVclStatsOamAisRcvCells_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 2, 3, 1, 6),
    _AtmGenVclStatsOamAisRcvCells_Type()
)
atmGenVclStatsOamAisRcvCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmGenVclStatsOamAisRcvCells.setStatus("mandatory")
_AtmGenVclStatsOamAisXmtCells_Type = Counter32
_AtmGenVclStatsOamAisXmtCells_Object = MibTableColumn
atmGenVclStatsOamAisXmtCells = _AtmGenVclStatsOamAisXmtCells_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 2, 3, 1, 7),
    _AtmGenVclStatsOamAisXmtCells_Type()
)
atmGenVclStatsOamAisXmtCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmGenVclStatsOamAisXmtCells.setStatus("mandatory")
_AtmGenVclStatsOamRdiRcvCells_Type = Counter32
_AtmGenVclStatsOamRdiRcvCells_Object = MibTableColumn
atmGenVclStatsOamRdiRcvCells = _AtmGenVclStatsOamRdiRcvCells_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 2, 3, 1, 8),
    _AtmGenVclStatsOamRdiRcvCells_Type()
)
atmGenVclStatsOamRdiRcvCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmGenVclStatsOamRdiRcvCells.setStatus("mandatory")
_AtmGenVclStatsOamRdiXmtCells_Type = Counter32
_AtmGenVclStatsOamRdiXmtCells_Object = MibTableColumn
atmGenVclStatsOamRdiXmtCells = _AtmGenVclStatsOamRdiXmtCells_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 2, 3, 1, 9),
    _AtmGenVclStatsOamRdiXmtCells_Type()
)
atmGenVclStatsOamRdiXmtCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmGenVclStatsOamRdiXmtCells.setStatus("mandatory")
_AtmGenVclStatsOamLoopbackRcvCells_Type = Counter32
_AtmGenVclStatsOamLoopbackRcvCells_Object = MibTableColumn
atmGenVclStatsOamLoopbackRcvCells = _AtmGenVclStatsOamLoopbackRcvCells_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 2, 3, 1, 10),
    _AtmGenVclStatsOamLoopbackRcvCells_Type()
)
atmGenVclStatsOamLoopbackRcvCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmGenVclStatsOamLoopbackRcvCells.setStatus("mandatory")
_AtmGenVclStatsOamLoopbackXmtCells_Type = Counter32
_AtmGenVclStatsOamLoopbackXmtCells_Object = MibTableColumn
atmGenVclStatsOamLoopbackXmtCells = _AtmGenVclStatsOamLoopbackXmtCells_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 2, 3, 1, 11),
    _AtmGenVclStatsOamLoopbackXmtCells_Type()
)
atmGenVclStatsOamLoopbackXmtCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmGenVclStatsOamLoopbackXmtCells.setStatus("mandatory")
_AtmGenericLpGroup_ObjectIdentity = ObjectIdentity
atmGenericLpGroup = _AtmGenericLpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 3)
)
_AtmGenLogicalPortTable_Object = MibTable
atmGenLogicalPortTable = _AtmGenLogicalPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 3, 1)
)
if mibBuilder.loadTexts:
    atmGenLogicalPortTable.setStatus("mandatory")
_AtmGenLogicalPortEntry_Object = MibTableRow
atmGenLogicalPortEntry = _AtmGenLogicalPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 3, 1, 1)
)
atmGenLogicalPortEntry.setIndexNames(
    (0, "SONOMASYSTEMS-SONOMA-ATM-GENERIC-MIB", "atmGenLpIfIndex"),
)
if mibBuilder.loadTexts:
    atmGenLogicalPortEntry.setStatus("mandatory")


class _AtmGenLpIfIndex_Type(Integer32):
    """Custom type atmGenLpIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(257, 512),
    )


_AtmGenLpIfIndex_Type.__name__ = "Integer32"
_AtmGenLpIfIndex_Object = MibTableColumn
atmGenLpIfIndex = _AtmGenLpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 3, 1, 1, 1),
    _AtmGenLpIfIndex_Type()
)
atmGenLpIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmGenLpIfIndex.setStatus("mandatory")


class _AtmGenLpPhysIf_Type(Integer32):
    """Custom type atmGenLpPhysIf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_AtmGenLpPhysIf_Type.__name__ = "Integer32"
_AtmGenLpPhysIf_Object = MibTableColumn
atmGenLpPhysIf = _AtmGenLpPhysIf_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 3, 1, 1, 2),
    _AtmGenLpPhysIf_Type()
)
atmGenLpPhysIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmGenLpPhysIf.setStatus("mandatory")


class _AtmGenLpLoopTime_Type(Integer32):
    """Custom type atmGenLpLoopTime based on Integer32"""
    defaultValue = 0


_AtmGenLpLoopTime_Object = MibTableColumn
atmGenLpLoopTime = _AtmGenLpLoopTime_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 3, 1, 1, 3),
    _AtmGenLpLoopTime_Type()
)
atmGenLpLoopTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmGenLpLoopTime.setStatus("mandatory")


class _AtmGenLpProtocol_Type(Integer32):
    """Custom type atmGenLpProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(7,
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("ethernet", 7),
          ("ethernet8023", 9),
          ("ethernetII", 8),
          ("fddi", 11),
          ("tokenRing", 10))
    )


_AtmGenLpProtocol_Type.__name__ = "Integer32"
_AtmGenLpProtocol_Object = MibTableColumn
atmGenLpProtocol = _AtmGenLpProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 3, 1, 1, 4),
    _AtmGenLpProtocol_Type()
)
atmGenLpProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmGenLpProtocol.setStatus("mandatory")


class _AtmGenLpAal5EncapsType_Type(Integer32):
    """Custom type atmGenLpAal5EncapsType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rfc1483-llc", 2),
          ("rfc1483-vc", 1))
    )


_AtmGenLpAal5EncapsType_Type.__name__ = "Integer32"
_AtmGenLpAal5EncapsType_Object = MibTableColumn
atmGenLpAal5EncapsType = _AtmGenLpAal5EncapsType_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 3, 1, 1, 5),
    _AtmGenLpAal5EncapsType_Type()
)
atmGenLpAal5EncapsType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmGenLpAal5EncapsType.setStatus("mandatory")
_AtmGenLpAal5Mtu_Type = Integer32
_AtmGenLpAal5Mtu_Object = MibTableColumn
atmGenLpAal5Mtu = _AtmGenLpAal5Mtu_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 3, 1, 1, 6),
    _AtmGenLpAal5Mtu_Type()
)
atmGenLpAal5Mtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmGenLpAal5Mtu.setStatus("mandatory")
_AtmGenLpAal5RateQ_Type = Integer32
_AtmGenLpAal5RateQ_Object = MibTableColumn
atmGenLpAal5RateQ = _AtmGenLpAal5RateQ_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 3, 1, 1, 7),
    _AtmGenLpAal5RateQ_Type()
)
atmGenLpAal5RateQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmGenLpAal5RateQ.setStatus("mandatory")


class _AtmGenLpAdminStatus_Type(Integer32):
    """Custom type atmGenLpAdminStatus based on Integer32"""
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


_AtmGenLpAdminStatus_Type.__name__ = "Integer32"
_AtmGenLpAdminStatus_Object = MibTableColumn
atmGenLpAdminStatus = _AtmGenLpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 3, 1, 1, 8),
    _AtmGenLpAdminStatus_Type()
)
atmGenLpAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmGenLpAdminStatus.setStatus("mandatory")


class _AtmGenLpLoopThreshold_Type(Integer32):
    """Custom type atmGenLpLoopThreshold based on Integer32"""
    defaultValue = 5


_AtmGenLpLoopThreshold_Object = MibTableColumn
atmGenLpLoopThreshold = _AtmGenLpLoopThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 3, 1, 1, 9),
    _AtmGenLpLoopThreshold_Type()
)
atmGenLpLoopThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmGenLpLoopThreshold.setStatus("mandatory")


class _AtmGenLpLoopTrapTime_Type(Integer32):
    """Custom type atmGenLpLoopTrapTime based on Integer32"""
    defaultValue = 5


_AtmGenLpLoopTrapTime_Object = MibTableColumn
atmGenLpLoopTrapTime = _AtmGenLpLoopTrapTime_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 3, 1, 1, 10),
    _AtmGenLpLoopTrapTime_Type()
)
atmGenLpLoopTrapTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmGenLpLoopTrapTime.setStatus("mandatory")


class _AtmGenLpOamGeneration_Type(Integer32):
    """Custom type atmGenLpOamGeneration based on Integer32"""
    defaultValue = 1


_AtmGenLpOamGeneration_Object = MibTableColumn
atmGenLpOamGeneration = _AtmGenLpOamGeneration_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 3, 1, 1, 11),
    _AtmGenLpOamGeneration_Type()
)
atmGenLpOamGeneration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmGenLpOamGeneration.setStatus("mandatory")
_AtmCesGroup_ObjectIdentity = ObjectIdentity
atmCesGroup = _AtmCesGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 4)
)
_CesConfTable_Object = MibTable
cesConfTable = _CesConfTable_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 4, 1)
)
if mibBuilder.loadTexts:
    cesConfTable.setStatus("mandatory")
_CesConfEntry_Object = MibTableRow
cesConfEntry = _CesConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 4, 1, 1)
)
cesConfEntry.setIndexNames(
    (0, "SONOMASYSTEMS-SONOMA-ATM-GENERIC-MIB", "cesAtmPhysPort"),
    (0, "SONOMASYSTEMS-SONOMA-ATM-GENERIC-MIB", "cesAtmVpi"),
    (0, "SONOMASYSTEMS-SONOMA-ATM-GENERIC-MIB", "cesAtmVci"),
)
if mibBuilder.loadTexts:
    cesConfEntry.setStatus("mandatory")
_CesAtmPhysPort_Type = Integer32
_CesAtmPhysPort_Object = MibTableColumn
cesAtmPhysPort = _CesAtmPhysPort_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 4, 1, 1, 1),
    _CesAtmPhysPort_Type()
)
cesAtmPhysPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesAtmPhysPort.setStatus("mandatory")


class _CesAtmVpi_Type(Integer32):
    """Custom type cesAtmVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CesAtmVpi_Type.__name__ = "Integer32"
_CesAtmVpi_Object = MibTableColumn
cesAtmVpi = _CesAtmVpi_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 4, 1, 1, 2),
    _CesAtmVpi_Type()
)
cesAtmVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesAtmVpi.setStatus("mandatory")


class _CesAtmVci_Type(Integer32):
    """Custom type cesAtmVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1023),
    )


_CesAtmVci_Type.__name__ = "Integer32"
_CesAtmVci_Object = MibTableColumn
cesAtmVci = _CesAtmVci_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 4, 1, 1, 3),
    _CesAtmVci_Type()
)
cesAtmVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesAtmVci.setStatus("mandatory")


class _CesCbrService_Type(Integer32):
    """Custom type cesCbrService based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("structured", 2),
          ("unstructured", 1))
    )


_CesCbrService_Type.__name__ = "Integer32"
_CesCbrService_Object = MibTableColumn
cesCbrService = _CesCbrService_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 4, 1, 1, 4),
    _CesCbrService_Type()
)
cesCbrService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cesCbrService.setStatus("mandatory")


class _CesCbrClockMode_Type(Integer32):
    """Custom type cesCbrClockMode based on Integer32"""
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
        *(("adaptive", 3),
          ("srts-master", 2),
          ("srts-slave", 4),
          ("synchronous", 1))
    )


_CesCbrClockMode_Type.__name__ = "Integer32"
_CesCbrClockMode_Object = MibTableColumn
cesCbrClockMode = _CesCbrClockMode_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 4, 1, 1, 5),
    _CesCbrClockMode_Type()
)
cesCbrClockMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cesCbrClockMode.setStatus("mandatory")


class _CesCas_Type(Integer32):
    """Custom type cesCas based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("with", 2),
          ("without", 1))
    )


_CesCas_Type.__name__ = "Integer32"
_CesCas_Object = MibTableColumn
cesCas = _CesCas_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 4, 1, 1, 6),
    _CesCas_Type()
)
cesCas.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cesCas.setStatus("mandatory")


class _CesPartialFill_Type(Integer32):
    """Custom type cesPartialFill based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 47),
    )


_CesPartialFill_Type.__name__ = "Integer32"
_CesPartialFill_Object = MibTableColumn
cesPartialFill = _CesPartialFill_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 4, 1, 1, 7),
    _CesPartialFill_Type()
)
cesPartialFill.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cesPartialFill.setStatus("mandatory")


class _CesBufMaxSize_Type(Integer32):
    """Custom type cesBufMaxSize based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65536),
    )


_CesBufMaxSize_Type.__name__ = "Integer32"
_CesBufMaxSize_Object = MibTableColumn
cesBufMaxSize = _CesBufMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 4, 1, 1, 8),
    _CesBufMaxSize_Type()
)
cesBufMaxSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cesBufMaxSize.setStatus("mandatory")


class _CesCdvRxT_Type(Integer32):
    """Custom type cesCdvRxT based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CesCdvRxT_Type.__name__ = "Integer32"
_CesCdvRxT_Object = MibTableColumn
cesCdvRxT = _CesCdvRxT_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 4, 1, 1, 9),
    _CesCdvRxT_Type()
)
cesCdvRxT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cesCdvRxT.setStatus("mandatory")


class _CesCellLossIntegrationPeriod_Type(Integer32):
    """Custom type cesCellLossIntegrationPeriod based on Integer32"""
    defaultValue = 2500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 65535),
    )


_CesCellLossIntegrationPeriod_Type.__name__ = "Integer32"
_CesCellLossIntegrationPeriod_Object = MibTableColumn
cesCellLossIntegrationPeriod = _CesCellLossIntegrationPeriod_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 4, 1, 1, 10),
    _CesCellLossIntegrationPeriod_Type()
)
cesCellLossIntegrationPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cesCellLossIntegrationPeriod.setStatus("mandatory")


class _CesConnType_Type(Integer32):
    """Custom type cesConnType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            2
        )
    )
    namedValues = NamedValues(
        ("pvc", 2)
    )


_CesConnType_Type.__name__ = "Integer32"
_CesConnType_Object = MibTableColumn
cesConnType = _CesConnType_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 4, 1, 1, 11),
    _CesConnType_Type()
)
cesConnType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cesConnType.setStatus("mandatory")


class _CesDynBw_Type(Integer32):
    """Custom type cesDynBw based on Integer32"""
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


_CesDynBw_Type.__name__ = "Integer32"
_CesDynBw_Object = MibTableColumn
cesDynBw = _CesDynBw_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 4, 1, 1, 12),
    _CesDynBw_Type()
)
cesDynBw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cesDynBw.setStatus("mandatory")


class _CesSigType_Type(Integer32):
    """Custom type cesSigType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("e-and-m", 6),
          ("fxo-ground", 4),
          ("fxo-loop", 2),
          ("fxs-ground", 5),
          ("fxs-loop", 3),
          ("other", 1),
          ("r2", 7))
    )


_CesSigType_Type.__name__ = "Integer32"
_CesSigType_Object = MibTableColumn
cesSigType = _CesSigType_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 4, 1, 1, 13),
    _CesSigType_Type()
)
cesSigType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cesSigType.setStatus("mandatory")


class _CesConfAction_Type(Integer32):
    """Custom type cesConfAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("attach", 5),
          ("remove", 6))
    )


_CesConfAction_Type.__name__ = "Integer32"
_CesConfAction_Object = MibTableColumn
cesConfAction = _CesConfAction_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 4, 1, 1, 14),
    _CesConfAction_Type()
)
cesConfAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cesConfAction.setStatus("mandatory")
_CesStatsTable_Object = MibTable
cesStatsTable = _CesStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 4, 3)
)
if mibBuilder.loadTexts:
    cesStatsTable.setStatus("mandatory")
_CesStatsEntry_Object = MibTableRow
cesStatsEntry = _CesStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 4, 3, 1)
)
cesStatsEntry.setIndexNames(
    (0, "SONOMASYSTEMS-SONOMA-ATM-GENERIC-MIB", "cesStatsAtmPhyPort"),
    (0, "SONOMASYSTEMS-SONOMA-ATM-GENERIC-MIB", "cesStatsAtmVpi"),
    (0, "SONOMASYSTEMS-SONOMA-ATM-GENERIC-MIB", "cesStatsAtmVci"),
)
if mibBuilder.loadTexts:
    cesStatsEntry.setStatus("mandatory")
_CesStatsAtmPhyPort_Type = Integer32
_CesStatsAtmPhyPort_Object = MibTableColumn
cesStatsAtmPhyPort = _CesStatsAtmPhyPort_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 4, 3, 1, 1),
    _CesStatsAtmPhyPort_Type()
)
cesStatsAtmPhyPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesStatsAtmPhyPort.setStatus("mandatory")


class _CesStatsAtmVpi_Type(Integer32):
    """Custom type cesStatsAtmVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CesStatsAtmVpi_Type.__name__ = "Integer32"
_CesStatsAtmVpi_Object = MibTableColumn
cesStatsAtmVpi = _CesStatsAtmVpi_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 4, 3, 1, 2),
    _CesStatsAtmVpi_Type()
)
cesStatsAtmVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesStatsAtmVpi.setStatus("mandatory")


class _CesStatsAtmVci_Type(Integer32):
    """Custom type cesStatsAtmVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(35, 1023),
    )


_CesStatsAtmVci_Type.__name__ = "Integer32"
_CesStatsAtmVci_Object = MibTableColumn
cesStatsAtmVci = _CesStatsAtmVci_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 4, 3, 1, 3),
    _CesStatsAtmVci_Type()
)
cesStatsAtmVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesStatsAtmVci.setStatus("mandatory")
_CesReassCells_Type = Counter32
_CesReassCells_Object = MibTableColumn
cesReassCells = _CesReassCells_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 4, 3, 1, 4),
    _CesReassCells_Type()
)
cesReassCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesReassCells.setStatus("mandatory")
_CesHdrErrors_Type = Counter32
_CesHdrErrors_Object = MibTableColumn
cesHdrErrors = _CesHdrErrors_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 4, 3, 1, 5),
    _CesHdrErrors_Type()
)
cesHdrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesHdrErrors.setStatus("mandatory")
_CesPointerReframes_Type = Counter32
_CesPointerReframes_Object = MibTableColumn
cesPointerReframes = _CesPointerReframes_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 4, 3, 1, 6),
    _CesPointerReframes_Type()
)
cesPointerReframes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesPointerReframes.setStatus("mandatory")
_CesPointerParityErrors_Type = Counter32
_CesPointerParityErrors_Object = MibTableColumn
cesPointerParityErrors = _CesPointerParityErrors_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 4, 3, 1, 7),
    _CesPointerParityErrors_Type()
)
cesPointerParityErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesPointerParityErrors.setStatus("mandatory")
_CesAal1SeqErrors_Type = Counter32
_CesAal1SeqErrors_Object = MibTableColumn
cesAal1SeqErrors = _CesAal1SeqErrors_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 4, 3, 1, 8),
    _CesAal1SeqErrors_Type()
)
cesAal1SeqErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesAal1SeqErrors.setStatus("mandatory")
_CesLostCells_Type = Counter32
_CesLostCells_Object = MibTableColumn
cesLostCells = _CesLostCells_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 4, 3, 1, 9),
    _CesLostCells_Type()
)
cesLostCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesLostCells.setStatus("mandatory")
_CesMisinsertedCells_Type = Counter32
_CesMisinsertedCells_Object = MibTableColumn
cesMisinsertedCells = _CesMisinsertedCells_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 4, 3, 1, 10),
    _CesMisinsertedCells_Type()
)
cesMisinsertedCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesMisinsertedCells.setStatus("mandatory")
_CesBufUnderflows_Type = Counter32
_CesBufUnderflows_Object = MibTableColumn
cesBufUnderflows = _CesBufUnderflows_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 4, 3, 1, 11),
    _CesBufUnderflows_Type()
)
cesBufUnderflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesBufUnderflows.setStatus("mandatory")
_CesBufOverflows_Type = Counter32
_CesBufOverflows_Object = MibTableColumn
cesBufOverflows = _CesBufOverflows_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 4, 3, 1, 12),
    _CesBufOverflows_Type()
)
cesBufOverflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesBufOverflows.setStatus("mandatory")


class _CesCellLossStatus_Type(Integer32):
    """Custom type cesCellLossStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("loss", 2),
          ("noLoss", 1))
    )


_CesCellLossStatus_Type.__name__ = "Integer32"
_CesCellLossStatus_Object = MibTableColumn
cesCellLossStatus = _CesCellLossStatus_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 4, 3, 1, 13),
    _CesCellLossStatus_Type()
)
cesCellLossStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesCellLossStatus.setStatus("deprecated")
_CesAttachmentTable_Object = MibTable
cesAttachmentTable = _CesAttachmentTable_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 4, 4)
)
if mibBuilder.loadTexts:
    cesAttachmentTable.setStatus("mandatory")
_CesAttachmentEntry_Object = MibTableRow
cesAttachmentEntry = _CesAttachmentEntry_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 4, 4, 1)
)
cesAttachmentEntry.setIndexNames(
    (0, "SONOMASYSTEMS-SONOMA-ATM-GENERIC-MIB", "cesAttachmentPhysPort"),
    (0, "SONOMASYSTEMS-SONOMA-ATM-GENERIC-MIB", "cesAttachmentBundle"),
    (0, "SONOMASYSTEMS-SONOMA-ATM-GENERIC-MIB", "cesAttachmentChan"),
)
if mibBuilder.loadTexts:
    cesAttachmentEntry.setStatus("mandatory")


class _CesAttachmentPhysPort_Type(Integer32):
    """Custom type cesAttachmentPhysPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_CesAttachmentPhysPort_Type.__name__ = "Integer32"
_CesAttachmentPhysPort_Object = MibTableColumn
cesAttachmentPhysPort = _CesAttachmentPhysPort_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 4, 4, 1, 1),
    _CesAttachmentPhysPort_Type()
)
cesAttachmentPhysPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesAttachmentPhysPort.setStatus("mandatory")


class _CesAttachmentBundle_Type(Integer32):
    """Custom type cesAttachmentBundle based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1025, 1536),
    )


_CesAttachmentBundle_Type.__name__ = "Integer32"
_CesAttachmentBundle_Object = MibTableColumn
cesAttachmentBundle = _CesAttachmentBundle_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 4, 4, 1, 2),
    _CesAttachmentBundle_Type()
)
cesAttachmentBundle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesAttachmentBundle.setStatus("mandatory")


class _CesAttachmentChan_Type(Integer32):
    """Custom type cesAttachmentChan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_CesAttachmentChan_Type.__name__ = "Integer32"
_CesAttachmentChan_Object = MibTableColumn
cesAttachmentChan = _CesAttachmentChan_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 4, 4, 1, 3),
    _CesAttachmentChan_Type()
)
cesAttachmentChan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesAttachmentChan.setStatus("mandatory")


class _CesAttachmentAction_Type(Integer32):
    """Custom type cesAttachmentAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("attach", 5),
          ("remove", 6))
    )


_CesAttachmentAction_Type.__name__ = "Integer32"
_CesAttachmentAction_Object = MibTableColumn
cesAttachmentAction = _CesAttachmentAction_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 4, 4, 1, 4),
    _CesAttachmentAction_Type()
)
cesAttachmentAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cesAttachmentAction.setStatus("mandatory")
_AtmAsiPhysGroup_ObjectIdentity = ObjectIdentity
atmAsiPhysGroup = _AtmAsiPhysGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 5)
)
_AtmAsiConfGroup_ObjectIdentity = ObjectIdentity
atmAsiConfGroup = _AtmAsiConfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 5, 1)
)
_AtmAsiConfPhyTable_Object = MibTable
atmAsiConfPhyTable = _AtmAsiConfPhyTable_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 5, 1, 1)
)
if mibBuilder.loadTexts:
    atmAsiConfPhyTable.setStatus("mandatory")
_AtmAsiConfPhyEntry_Object = MibTableRow
atmAsiConfPhyEntry = _AtmAsiConfPhyEntry_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 5, 1, 1, 1)
)
atmAsiConfPhyEntry.setIndexNames(
    (0, "SONOMASYSTEMS-SONOMA-ATM-GENERIC-MIB", "atmAsiConfPhysIndex"),
)
if mibBuilder.loadTexts:
    atmAsiConfPhyEntry.setStatus("mandatory")
_AtmAsiConfPhysIndex_Type = Integer32
_AtmAsiConfPhysIndex_Object = MibTableColumn
atmAsiConfPhysIndex = _AtmAsiConfPhysIndex_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 5, 1, 1, 1, 1),
    _AtmAsiConfPhysIndex_Type()
)
atmAsiConfPhysIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmAsiConfPhysIndex.setStatus("mandatory")


class _AtmAsiConfLineType_Type(Integer32):
    """Custom type atmAsiConfLineType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("d4", 3),
          ("e1", 4),
          ("e1-cas", 6),
          ("e1-crc", 5),
          ("e1-crc-cas", 7),
          ("esf", 2))
    )


_AtmAsiConfLineType_Type.__name__ = "Integer32"
_AtmAsiConfLineType_Object = MibTableColumn
atmAsiConfLineType = _AtmAsiConfLineType_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 5, 1, 1, 1, 2),
    _AtmAsiConfLineType_Type()
)
atmAsiConfLineType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmAsiConfLineType.setStatus("mandatory")


class _AtmAsiConfLineCoding_Type(Integer32):
    """Custom type atmAsiConfLineCoding based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("ami", 5),
          ("b8zs", 2),
          ("hdb3", 3),
          ("zbtsi", 4))
    )


_AtmAsiConfLineCoding_Type.__name__ = "Integer32"
_AtmAsiConfLineCoding_Object = MibTableColumn
atmAsiConfLineCoding = _AtmAsiConfLineCoding_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 5, 1, 1, 1, 4),
    _AtmAsiConfLineCoding_Type()
)
atmAsiConfLineCoding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmAsiConfLineCoding.setStatus("mandatory")


class _AtmAsiConfTxClkSelect_Type(Integer32):
    """Custom type atmAsiConfTxClkSelect based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("internal", 1),
          ("line", 2),
          ("through", 3))
    )


_AtmAsiConfTxClkSelect_Type.__name__ = "Integer32"
_AtmAsiConfTxClkSelect_Object = MibTableColumn
atmAsiConfTxClkSelect = _AtmAsiConfTxClkSelect_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 5, 1, 1, 1, 5),
    _AtmAsiConfTxClkSelect_Type()
)
atmAsiConfTxClkSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmAsiConfTxClkSelect.setStatus("mandatory")


class _AtmAsiConfSignalMode_Type(Integer32):
    """Custom type atmAsiConfSignalMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bit-oriented", 3),
          ("none", 1),
          ("robbed-bit", 2))
    )


_AtmAsiConfSignalMode_Type.__name__ = "Integer32"
_AtmAsiConfSignalMode_Object = MibTableColumn
atmAsiConfSignalMode = _AtmAsiConfSignalMode_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 5, 1, 1, 1, 6),
    _AtmAsiConfSignalMode_Type()
)
atmAsiConfSignalMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmAsiConfSignalMode.setStatus("mandatory")


class _AtmAsiConfLIUType_Type(Integer32):
    """Custom type atmAsiConfLIUType based on Integer32"""
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
        *(("dsx1-short", 4),
          ("itu-120", 2),
          ("itu-75", 3),
          ("t1-long", 1))
    )


_AtmAsiConfLIUType_Type.__name__ = "Integer32"
_AtmAsiConfLIUType_Object = MibTableColumn
atmAsiConfLIUType = _AtmAsiConfLIUType_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 5, 1, 1, 1, 7),
    _AtmAsiConfLIUType_Type()
)
atmAsiConfLIUType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmAsiConfLIUType.setStatus("mandatory")


class _AtmAsiConfLBOType_Type(Integer32):
    """Custom type atmAsiConfLBOType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("long-0", 8),
          ("long-150", 10),
          ("long-225", 11),
          ("long-75", 9),
          ("short-133", 1),
          ("short-266", 2),
          ("short-399", 3),
          ("short-533", 4),
          ("short-655", 5))
    )


_AtmAsiConfLBOType_Type.__name__ = "Integer32"
_AtmAsiConfLBOType_Object = MibTableColumn
atmAsiConfLBOType = _AtmAsiConfLBOType_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 5, 1, 1, 1, 8),
    _AtmAsiConfLBOType_Type()
)
atmAsiConfLBOType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmAsiConfLBOType.setStatus("mandatory")


class _AtmAsiConfIdlePattern_Type(Integer32):
    """Custom type atmAsiConfIdlePattern based on Integer32"""
    defaultValue = 127

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AtmAsiConfIdlePattern_Type.__name__ = "Integer32"
_AtmAsiConfIdlePattern_Object = MibTableColumn
atmAsiConfIdlePattern = _AtmAsiConfIdlePattern_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 5, 1, 1, 1, 9),
    _AtmAsiConfIdlePattern_Type()
)
atmAsiConfIdlePattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmAsiConfIdlePattern.setStatus("mandatory")


class _AtmAsiConfLoopbackMode_Type(Integer32):
    """Custom type atmAsiConfLoopbackMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("external", 3),
          ("internal", 2))
    )


_AtmAsiConfLoopbackMode_Type.__name__ = "Integer32"
_AtmAsiConfLoopbackMode_Object = MibTableColumn
atmAsiConfLoopbackMode = _AtmAsiConfLoopbackMode_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 5, 1, 1, 1, 10),
    _AtmAsiConfLoopbackMode_Type()
)
atmAsiConfLoopbackMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmAsiConfLoopbackMode.setStatus("mandatory")


class _AtmAsiConfStopMode_Type(Integer32):
    """Custom type atmAsiConfStopMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("immediate", 1),
          ("on-idle", 2))
    )


_AtmAsiConfStopMode_Type.__name__ = "Integer32"
_AtmAsiConfStopMode_Object = MibTableColumn
atmAsiConfStopMode = _AtmAsiConfStopMode_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 5, 1, 1, 1, 11),
    _AtmAsiConfStopMode_Type()
)
atmAsiConfStopMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmAsiConfStopMode.setStatus("mandatory")


class _AtmAsiConfRecoveredClkSource_Type(Integer32):
    """Custom type atmAsiConfRecoveredClkSource based on Integer32"""
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
        *(("first-port", 4),
          ("fourth-port", 1),
          ("phy-port", 5),
          ("second-port", 3),
          ("third-port", 2))
    )


_AtmAsiConfRecoveredClkSource_Type.__name__ = "Integer32"
_AtmAsiConfRecoveredClkSource_Object = MibTableColumn
atmAsiConfRecoveredClkSource = _AtmAsiConfRecoveredClkSource_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 5, 1, 1, 1, 12),
    _AtmAsiConfRecoveredClkSource_Type()
)
atmAsiConfRecoveredClkSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmAsiConfRecoveredClkSource.setStatus("mandatory")


class _AtmAsiDebugAddr_Type(Integer32):
    """Custom type atmAsiDebugAddr based on Integer32"""
    defaultValue = 0


_AtmAsiDebugAddr_Object = MibTableColumn
atmAsiDebugAddr = _AtmAsiDebugAddr_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 5, 1, 1, 1, 13),
    _AtmAsiDebugAddr_Type()
)
atmAsiDebugAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmAsiDebugAddr.setStatus("mandatory")


class _AtmAsiDebugReadValue_Type(Integer32):
    """Custom type atmAsiDebugReadValue based on Integer32"""
    defaultValue = 0


_AtmAsiDebugReadValue_Object = MibTableColumn
atmAsiDebugReadValue = _AtmAsiDebugReadValue_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 5, 1, 1, 1, 14),
    _AtmAsiDebugReadValue_Type()
)
atmAsiDebugReadValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmAsiDebugReadValue.setStatus("mandatory")


class _AtmAsiDebugWriteValue_Type(Integer32):
    """Custom type atmAsiDebugWriteValue based on Integer32"""
    defaultValue = 0


_AtmAsiDebugWriteValue_Object = MibTableColumn
atmAsiDebugWriteValue = _AtmAsiDebugWriteValue_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 5, 1, 1, 1, 15),
    _AtmAsiDebugWriteValue_Type()
)
atmAsiDebugWriteValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmAsiDebugWriteValue.setStatus("mandatory")


class _AtmAsiDebugRead_Type(Integer32):
    """Custom type atmAsiDebugRead based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("read", 1),
          ("write", 2))
    )


_AtmAsiDebugRead_Type.__name__ = "Integer32"
_AtmAsiDebugRead_Object = MibTableColumn
atmAsiDebugRead = _AtmAsiDebugRead_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 5, 1, 1, 1, 16),
    _AtmAsiDebugRead_Type()
)
atmAsiDebugRead.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmAsiDebugRead.setStatus("mandatory")
_AtmAsiStatsGroup_ObjectIdentity = ObjectIdentity
atmAsiStatsGroup = _AtmAsiStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 5, 2)
)
_AtmAsiStatsTable_Object = MibTable
atmAsiStatsTable = _AtmAsiStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 5, 2, 1)
)
if mibBuilder.loadTexts:
    atmAsiStatsTable.setStatus("mandatory")
_AtmAsiStatsEntry_Object = MibTableRow
atmAsiStatsEntry = _AtmAsiStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 5, 2, 1, 1)
)
atmAsiStatsEntry.setIndexNames(
    (0, "SONOMASYSTEMS-SONOMA-ATM-GENERIC-MIB", "atmAsiStatsPhysIndex"),
)
if mibBuilder.loadTexts:
    atmAsiStatsEntry.setStatus("mandatory")
_AtmAsiStatsPhysIndex_Type = Integer32
_AtmAsiStatsPhysIndex_Object = MibTableColumn
atmAsiStatsPhysIndex = _AtmAsiStatsPhysIndex_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 5, 2, 1, 1, 1),
    _AtmAsiStatsPhysIndex_Type()
)
atmAsiStatsPhysIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmAsiStatsPhysIndex.setStatus("mandatory")
_AtmAsiStatsNoSignals_Type = Counter32
_AtmAsiStatsNoSignals_Object = MibTableColumn
atmAsiStatsNoSignals = _AtmAsiStatsNoSignals_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 5, 2, 1, 1, 2),
    _AtmAsiStatsNoSignals_Type()
)
atmAsiStatsNoSignals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmAsiStatsNoSignals.setStatus("mandatory")
_AtmAsiStatsAISDetects_Type = Counter32
_AtmAsiStatsAISDetects_Object = MibTableColumn
atmAsiStatsAISDetects = _AtmAsiStatsAISDetects_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 5, 2, 1, 1, 3),
    _AtmAsiStatsAISDetects_Type()
)
atmAsiStatsAISDetects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmAsiStatsAISDetects.setStatus("mandatory")
_AtmAsiStatsYelAlarmCount_Type = Counter32
_AtmAsiStatsYelAlarmCount_Object = MibTableColumn
atmAsiStatsYelAlarmCount = _AtmAsiStatsYelAlarmCount_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 5, 2, 1, 1, 4),
    _AtmAsiStatsYelAlarmCount_Type()
)
atmAsiStatsYelAlarmCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmAsiStatsYelAlarmCount.setStatus("mandatory")
_AtmAsiStatsLCVErrors_Type = Counter32
_AtmAsiStatsLCVErrors_Object = MibTableColumn
atmAsiStatsLCVErrors = _AtmAsiStatsLCVErrors_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 5, 2, 1, 1, 5),
    _AtmAsiStatsLCVErrors_Type()
)
atmAsiStatsLCVErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmAsiStatsLCVErrors.setStatus("mandatory")
_AtmAsiStatsPCVErrors_Type = Counter32
_AtmAsiStatsPCVErrors_Object = MibTableColumn
atmAsiStatsPCVErrors = _AtmAsiStatsPCVErrors_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 5, 2, 1, 1, 6),
    _AtmAsiStatsPCVErrors_Type()
)
atmAsiStatsPCVErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmAsiStatsPCVErrors.setStatus("mandatory")
_AtmAsiStatsMOSErrors_Type = Counter32
_AtmAsiStatsMOSErrors_Object = MibTableColumn
atmAsiStatsMOSErrors = _AtmAsiStatsMOSErrors_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 5, 2, 1, 1, 7),
    _AtmAsiStatsMOSErrors_Type()
)
atmAsiStatsMOSErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmAsiStatsMOSErrors.setStatus("mandatory")
_AtmAsiStatsSyncLossCount_Type = Counter32
_AtmAsiStatsSyncLossCount_Object = MibTableColumn
atmAsiStatsSyncLossCount = _AtmAsiStatsSyncLossCount_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 5, 2, 1, 1, 8),
    _AtmAsiStatsSyncLossCount_Type()
)
atmAsiStatsSyncLossCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmAsiStatsSyncLossCount.setStatus("mandatory")
_AtmAsiStatsHECErrors_Type = Counter32
_AtmAsiStatsHECErrors_Object = MibTableColumn
atmAsiStatsHECErrors = _AtmAsiStatsHECErrors_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 5, 2, 1, 1, 9),
    _AtmAsiStatsHECErrors_Type()
)
atmAsiStatsHECErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmAsiStatsHECErrors.setStatus("mandatory")


class _AtmAsiStatsSignalLoss_Type(Integer32):
    """Custom type atmAsiStatsSignalLoss based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_AtmAsiStatsSignalLoss_Type.__name__ = "Integer32"
_AtmAsiStatsSignalLoss_Object = MibTableColumn
atmAsiStatsSignalLoss = _AtmAsiStatsSignalLoss_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 5, 2, 1, 1, 10),
    _AtmAsiStatsSignalLoss_Type()
)
atmAsiStatsSignalLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmAsiStatsSignalLoss.setStatus("mandatory")


class _AtmAsiStatsAISDetect_Type(Integer32):
    """Custom type atmAsiStatsAISDetect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_AtmAsiStatsAISDetect_Type.__name__ = "Integer32"
_AtmAsiStatsAISDetect_Object = MibTableColumn
atmAsiStatsAISDetect = _AtmAsiStatsAISDetect_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 5, 2, 1, 1, 11),
    _AtmAsiStatsAISDetect_Type()
)
atmAsiStatsAISDetect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmAsiStatsAISDetect.setStatus("mandatory")


class _AtmAsiStatsYellowAlarm_Type(Integer32):
    """Custom type atmAsiStatsYellowAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_AtmAsiStatsYellowAlarm_Type.__name__ = "Integer32"
_AtmAsiStatsYellowAlarm_Object = MibTableColumn
atmAsiStatsYellowAlarm = _AtmAsiStatsYellowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 5, 2, 1, 1, 12),
    _AtmAsiStatsYellowAlarm_Type()
)
atmAsiStatsYellowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmAsiStatsYellowAlarm.setStatus("mandatory")


class _AtmAsiStatsSyncLoss_Type(Integer32):
    """Custom type atmAsiStatsSyncLoss based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_AtmAsiStatsSyncLoss_Type.__name__ = "Integer32"
_AtmAsiStatsSyncLoss_Object = MibTableColumn
atmAsiStatsSyncLoss = _AtmAsiStatsSyncLoss_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 5, 2, 1, 1, 13),
    _AtmAsiStatsSyncLoss_Type()
)
atmAsiStatsSyncLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmAsiStatsSyncLoss.setStatus("mandatory")


class _AtmAsiStatsTxClockLoss_Type(Integer32):
    """Custom type atmAsiStatsTxClockLoss based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_AtmAsiStatsTxClockLoss_Type.__name__ = "Integer32"
_AtmAsiStatsTxClockLoss_Object = MibTableColumn
atmAsiStatsTxClockLoss = _AtmAsiStatsTxClockLoss_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 5, 2, 1, 1, 14),
    _AtmAsiStatsTxClockLoss_Type()
)
atmAsiStatsTxClockLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmAsiStatsTxClockLoss.setStatus("mandatory")


class _AtmAsiStatsClearCounters_Type(Integer32):
    """Custom type atmAsiStatsClearCounters based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_AtmAsiStatsClearCounters_Type.__name__ = "Integer32"
_AtmAsiStatsClearCounters_Object = MibTableColumn
atmAsiStatsClearCounters = _AtmAsiStatsClearCounters_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 5, 2, 1, 1, 15),
    _AtmAsiStatsClearCounters_Type()
)
atmAsiStatsClearCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmAsiStatsClearCounters.setStatus("mandatory")
_AtmAsmPhysGroup_ObjectIdentity = ObjectIdentity
atmAsmPhysGroup = _AtmAsmPhysGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 6)
)
_AtmAsmPhyConfGroup_ObjectIdentity = ObjectIdentity
atmAsmPhyConfGroup = _AtmAsmPhyConfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 6, 1)
)
_AtmAsmPhyConfTable_Object = MibTable
atmAsmPhyConfTable = _AtmAsmPhyConfTable_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 6, 1, 1)
)
if mibBuilder.loadTexts:
    atmAsmPhyConfTable.setStatus("mandatory")
_AtmAsmPhyConfEntry_Object = MibTableRow
atmAsmPhyConfEntry = _AtmAsmPhyConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 6, 1, 1, 1)
)
atmAsmPhyConfEntry.setIndexNames(
    (0, "SONOMASYSTEMS-SONOMA-ATM-GENERIC-MIB", "atmAsmPhyConfIndex"),
)
if mibBuilder.loadTexts:
    atmAsmPhyConfEntry.setStatus("mandatory")
_AtmAsmPhyConfIndex_Type = Integer32
_AtmAsmPhyConfIndex_Object = MibTableColumn
atmAsmPhyConfIndex = _AtmAsmPhyConfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 6, 1, 1, 1, 1),
    _AtmAsmPhyConfIndex_Type()
)
atmAsmPhyConfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmAsmPhyConfIndex.setStatus("mandatory")


class _AtmAsmPhyConfAdminLineUsage_Type(Integer32):
    """Custom type atmAsmPhyConfAdminLineUsage based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("ces-sdt", 2),
          ("ces-udt", 1),
          ("ima", 5),
          ("uni", 4))
    )


_AtmAsmPhyConfAdminLineUsage_Type.__name__ = "Integer32"
_AtmAsmPhyConfAdminLineUsage_Object = MibTableColumn
atmAsmPhyConfAdminLineUsage = _AtmAsmPhyConfAdminLineUsage_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 6, 1, 1, 1, 2),
    _AtmAsmPhyConfAdminLineUsage_Type()
)
atmAsmPhyConfAdminLineUsage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmAsmPhyConfAdminLineUsage.setStatus("mandatory")


class _AtmAsmPhyConfOperLineUsage_Type(Integer32):
    """Custom type atmAsmPhyConfOperLineUsage based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("ces-sdt", 2),
          ("ces-udt", 1),
          ("ima", 5),
          ("uni", 4))
    )


_AtmAsmPhyConfOperLineUsage_Type.__name__ = "Integer32"
_AtmAsmPhyConfOperLineUsage_Object = MibTableColumn
atmAsmPhyConfOperLineUsage = _AtmAsmPhyConfOperLineUsage_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 1, 6, 1, 1, 1, 3),
    _AtmAsmPhyConfOperLineUsage_Type()
)
atmAsmPhyConfOperLineUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmAsmPhyConfOperLineUsage.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SONOMASYSTEMS-SONOMA-ATM-GENERIC-MIB",
    **{"sonomaGenericATMGroup": sonomaGenericATMGroup,
       "atmGenericPhysGroup": atmGenericPhysGroup,
       "atmGenPhysTable": atmGenPhysTable,
       "atmGenPhysEntry": atmGenPhysEntry,
       "atmGenPhysIndex": atmGenPhysIndex,
       "atmGenPhysAal5Mtu": atmGenPhysAal5Mtu,
       "atmGenPhysAal5CrcErrors": atmGenPhysAal5CrcErrors,
       "atmGenPhysAal5OverSizedSDUs": atmGenPhysAal5OverSizedSDUs,
       "atmGenPhysAal5DiscardPDU": atmGenPhysAal5DiscardPDU,
       "atmGenPhysHECErrors": atmGenPhysHECErrors,
       "atmGenPhysUnknownProtocols": atmGenPhysUnknownProtocols,
       "atmGenPhysCellsReceived": atmGenPhysCellsReceived,
       "atmGenPhysCellsTransmitted": atmGenPhysCellsTransmitted,
       "atmGenPhysRxBufStarvation": atmGenPhysRxBufStarvation,
       "atmGenPhysRxFreeze": atmGenPhysRxFreeze,
       "atmGenPhysTxFreeze": atmGenPhysTxFreeze,
       "atmGenRateTable": atmGenRateTable,
       "atmGenRateEntry": atmGenRateEntry,
       "atmGenRatePhysIndex": atmGenRatePhysIndex,
       "atmGenRateQueOne": atmGenRateQueOne,
       "atmGenRateQueTwo": atmGenRateQueTwo,
       "atmGenRateQueThree": atmGenRateQueThree,
       "atmGenRateQueFour": atmGenRateQueFour,
       "atmGenRateQueFive": atmGenRateQueFive,
       "atmGenRateQueSix": atmGenRateQueSix,
       "atmGenRateQueSeven": atmGenRateQueSeven,
       "atmGenRateQueEight": atmGenRateQueEight,
       "atmGenRateQTable": atmGenRateQTable,
       "atmGenRateQEntry": atmGenRateQEntry,
       "atmGenRateQPhysIndex": atmGenRateQPhysIndex,
       "atmGenRateQNumber": atmGenRateQNumber,
       "atmGenRateQueue": atmGenRateQueue,
       "atmGenericVclGroup": atmGenericVclGroup,
       "atmGenVclTable": atmGenVclTable,
       "atmGenVclEntry": atmGenVclEntry,
       "atmGenVclIfIndex": atmGenVclIfIndex,
       "atmGenVclVpi": atmGenVclVpi,
       "atmGenVclVci": atmGenVclVci,
       "atmGenVclRateQ": atmGenVclRateQ,
       "atmGenVclAction": atmGenVclAction,
       "atmGenVclTmTable": atmGenVclTmTable,
       "atmGenVclTmEntry": atmGenVclTmEntry,
       "atmGenVclTmIfIndex": atmGenVclTmIfIndex,
       "atmGenVclTmVpi": atmGenVclTmVpi,
       "atmGenVclTmVci": atmGenVclTmVci,
       "atmGenVclTmPCR": atmGenVclTmPCR,
       "atmGenVclTmSCR": atmGenVclTmSCR,
       "atmGenVclTmMBS": atmGenVclTmMBS,
       "atmGenVclTmAction": atmGenVclTmAction,
       "atmGenVclStatsTable": atmGenVclStatsTable,
       "atmGenVclStatsEntry": atmGenVclStatsEntry,
       "atmGenVclStatsIfIndex": atmGenVclStatsIfIndex,
       "atmGenVclStatsVpi": atmGenVclStatsVpi,
       "atmGenVclStatsVci": atmGenVclStatsVci,
       "atmGenVclStatsCellsReceived": atmGenVclStatsCellsReceived,
       "atmGenVclStatsCellsTransmitted": atmGenVclStatsCellsTransmitted,
       "atmGenVclStatsOamAisRcvCells": atmGenVclStatsOamAisRcvCells,
       "atmGenVclStatsOamAisXmtCells": atmGenVclStatsOamAisXmtCells,
       "atmGenVclStatsOamRdiRcvCells": atmGenVclStatsOamRdiRcvCells,
       "atmGenVclStatsOamRdiXmtCells": atmGenVclStatsOamRdiXmtCells,
       "atmGenVclStatsOamLoopbackRcvCells": atmGenVclStatsOamLoopbackRcvCells,
       "atmGenVclStatsOamLoopbackXmtCells": atmGenVclStatsOamLoopbackXmtCells,
       "atmGenericLpGroup": atmGenericLpGroup,
       "atmGenLogicalPortTable": atmGenLogicalPortTable,
       "atmGenLogicalPortEntry": atmGenLogicalPortEntry,
       "atmGenLpIfIndex": atmGenLpIfIndex,
       "atmGenLpPhysIf": atmGenLpPhysIf,
       "atmGenLpLoopTime": atmGenLpLoopTime,
       "atmGenLpProtocol": atmGenLpProtocol,
       "atmGenLpAal5EncapsType": atmGenLpAal5EncapsType,
       "atmGenLpAal5Mtu": atmGenLpAal5Mtu,
       "atmGenLpAal5RateQ": atmGenLpAal5RateQ,
       "atmGenLpAdminStatus": atmGenLpAdminStatus,
       "atmGenLpLoopThreshold": atmGenLpLoopThreshold,
       "atmGenLpLoopTrapTime": atmGenLpLoopTrapTime,
       "atmGenLpOamGeneration": atmGenLpOamGeneration,
       "atmCesGroup": atmCesGroup,
       "cesConfTable": cesConfTable,
       "cesConfEntry": cesConfEntry,
       "cesAtmPhysPort": cesAtmPhysPort,
       "cesAtmVpi": cesAtmVpi,
       "cesAtmVci": cesAtmVci,
       "cesCbrService": cesCbrService,
       "cesCbrClockMode": cesCbrClockMode,
       "cesCas": cesCas,
       "cesPartialFill": cesPartialFill,
       "cesBufMaxSize": cesBufMaxSize,
       "cesCdvRxT": cesCdvRxT,
       "cesCellLossIntegrationPeriod": cesCellLossIntegrationPeriod,
       "cesConnType": cesConnType,
       "cesDynBw": cesDynBw,
       "cesSigType": cesSigType,
       "cesConfAction": cesConfAction,
       "cesStatsTable": cesStatsTable,
       "cesStatsEntry": cesStatsEntry,
       "cesStatsAtmPhyPort": cesStatsAtmPhyPort,
       "cesStatsAtmVpi": cesStatsAtmVpi,
       "cesStatsAtmVci": cesStatsAtmVci,
       "cesReassCells": cesReassCells,
       "cesHdrErrors": cesHdrErrors,
       "cesPointerReframes": cesPointerReframes,
       "cesPointerParityErrors": cesPointerParityErrors,
       "cesAal1SeqErrors": cesAal1SeqErrors,
       "cesLostCells": cesLostCells,
       "cesMisinsertedCells": cesMisinsertedCells,
       "cesBufUnderflows": cesBufUnderflows,
       "cesBufOverflows": cesBufOverflows,
       "cesCellLossStatus": cesCellLossStatus,
       "cesAttachmentTable": cesAttachmentTable,
       "cesAttachmentEntry": cesAttachmentEntry,
       "cesAttachmentPhysPort": cesAttachmentPhysPort,
       "cesAttachmentBundle": cesAttachmentBundle,
       "cesAttachmentChan": cesAttachmentChan,
       "cesAttachmentAction": cesAttachmentAction,
       "atmAsiPhysGroup": atmAsiPhysGroup,
       "atmAsiConfGroup": atmAsiConfGroup,
       "atmAsiConfPhyTable": atmAsiConfPhyTable,
       "atmAsiConfPhyEntry": atmAsiConfPhyEntry,
       "atmAsiConfPhysIndex": atmAsiConfPhysIndex,
       "atmAsiConfLineType": atmAsiConfLineType,
       "atmAsiConfLineCoding": atmAsiConfLineCoding,
       "atmAsiConfTxClkSelect": atmAsiConfTxClkSelect,
       "atmAsiConfSignalMode": atmAsiConfSignalMode,
       "atmAsiConfLIUType": atmAsiConfLIUType,
       "atmAsiConfLBOType": atmAsiConfLBOType,
       "atmAsiConfIdlePattern": atmAsiConfIdlePattern,
       "atmAsiConfLoopbackMode": atmAsiConfLoopbackMode,
       "atmAsiConfStopMode": atmAsiConfStopMode,
       "atmAsiConfRecoveredClkSource": atmAsiConfRecoveredClkSource,
       "atmAsiDebugAddr": atmAsiDebugAddr,
       "atmAsiDebugReadValue": atmAsiDebugReadValue,
       "atmAsiDebugWriteValue": atmAsiDebugWriteValue,
       "atmAsiDebugRead": atmAsiDebugRead,
       "atmAsiStatsGroup": atmAsiStatsGroup,
       "atmAsiStatsTable": atmAsiStatsTable,
       "atmAsiStatsEntry": atmAsiStatsEntry,
       "atmAsiStatsPhysIndex": atmAsiStatsPhysIndex,
       "atmAsiStatsNoSignals": atmAsiStatsNoSignals,
       "atmAsiStatsAISDetects": atmAsiStatsAISDetects,
       "atmAsiStatsYelAlarmCount": atmAsiStatsYelAlarmCount,
       "atmAsiStatsLCVErrors": atmAsiStatsLCVErrors,
       "atmAsiStatsPCVErrors": atmAsiStatsPCVErrors,
       "atmAsiStatsMOSErrors": atmAsiStatsMOSErrors,
       "atmAsiStatsSyncLossCount": atmAsiStatsSyncLossCount,
       "atmAsiStatsHECErrors": atmAsiStatsHECErrors,
       "atmAsiStatsSignalLoss": atmAsiStatsSignalLoss,
       "atmAsiStatsAISDetect": atmAsiStatsAISDetect,
       "atmAsiStatsYellowAlarm": atmAsiStatsYellowAlarm,
       "atmAsiStatsSyncLoss": atmAsiStatsSyncLoss,
       "atmAsiStatsTxClockLoss": atmAsiStatsTxClockLoss,
       "atmAsiStatsClearCounters": atmAsiStatsClearCounters,
       "atmAsmPhysGroup": atmAsmPhysGroup,
       "atmAsmPhyConfGroup": atmAsmPhyConfGroup,
       "atmAsmPhyConfTable": atmAsmPhyConfTable,
       "atmAsmPhyConfEntry": atmAsmPhyConfEntry,
       "atmAsmPhyConfIndex": atmAsmPhyConfIndex,
       "atmAsmPhyConfAdminLineUsage": atmAsmPhyConfAdminLineUsage,
       "atmAsmPhyConfOperLineUsage": atmAsmPhyConfOperLineUsage}
)
