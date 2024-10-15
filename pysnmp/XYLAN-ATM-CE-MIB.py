# SNMP MIB module (XYLAN-ATM-CE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/XYLAN-ATM-CE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:18:52 2024
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
 NotificationType,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(xylanAtmArch,) = mibBuilder.importSymbols(
    "XYLAN-BASE-MIB",
    "xylanAtmArch")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AtmxCesGroup_ObjectIdentity = ObjectIdentity
atmxCesGroup = _AtmxCesGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 10)
)
_AtmxCesMIBObjects_ObjectIdentity = ObjectIdentity
atmxCesMIBObjects = _AtmxCesMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1)
)
_AtmxCesService_ObjectIdentity = ObjectIdentity
atmxCesService = _AtmxCesService_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 1)
)
_AtmxCesServiceTable_Object = MibTable
atmxCesServiceTable = _AtmxCesServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 1, 1)
)
if mibBuilder.loadTexts:
    atmxCesServiceTable.setStatus("mandatory")
_AtmxCesServiceEntry_Object = MibTableRow
atmxCesServiceEntry = _AtmxCesServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 1, 1, 1)
)
atmxCesServiceEntry.setIndexNames(
    (0, "XYLAN-ATM-CE-MIB", "atmxCesServiceSlotIndex"),
    (0, "XYLAN-ATM-CE-MIB", "atmxCesServicePortIndex"),
)
if mibBuilder.loadTexts:
    atmxCesServiceEntry.setStatus("mandatory")


class _AtmxCesServiceSlotIndex_Type(Integer32):
    """Custom type atmxCesServiceSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_AtmxCesServiceSlotIndex_Type.__name__ = "Integer32"
_AtmxCesServiceSlotIndex_Object = MibTableColumn
atmxCesServiceSlotIndex = _AtmxCesServiceSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 1, 1, 1, 1),
    _AtmxCesServiceSlotIndex_Type()
)
atmxCesServiceSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxCesServiceSlotIndex.setStatus("mandatory")


class _AtmxCesServicePortIndex_Type(Integer32):
    """Custom type atmxCesServicePortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_AtmxCesServicePortIndex_Type.__name__ = "Integer32"
_AtmxCesServicePortIndex_Object = MibTableColumn
atmxCesServicePortIndex = _AtmxCesServicePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 1, 1, 1, 2),
    _AtmxCesServicePortIndex_Type()
)
atmxCesServicePortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxCesServicePortIndex.setStatus("mandatory")


class _AtmxCesServiceDescription_Type(DisplayString):
    """Custom type atmxCesServiceDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AtmxCesServiceDescription_Type.__name__ = "DisplayString"
_AtmxCesServiceDescription_Object = MibTableColumn
atmxCesServiceDescription = _AtmxCesServiceDescription_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 1, 1, 1, 3),
    _AtmxCesServiceDescription_Type()
)
atmxCesServiceDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxCesServiceDescription.setStatus("mandatory")


class _AtmxCesServiceAdminStatus_Type(Integer32):
    """Custom type atmxCesServiceAdminStatus based on Integer32"""
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


_AtmxCesServiceAdminStatus_Type.__name__ = "Integer32"
_AtmxCesServiceAdminStatus_Object = MibTableColumn
atmxCesServiceAdminStatus = _AtmxCesServiceAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 1, 1, 1, 4),
    _AtmxCesServiceAdminStatus_Type()
)
atmxCesServiceAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxCesServiceAdminStatus.setStatus("mandatory")


class _AtmxCesServiceOperStatus_Type(Integer32):
    """Custom type atmxCesServiceOperStatus based on Integer32"""
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


_AtmxCesServiceOperStatus_Type.__name__ = "Integer32"
_AtmxCesServiceOperStatus_Object = MibTableColumn
atmxCesServiceOperStatus = _AtmxCesServiceOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 1, 1, 1, 5),
    _AtmxCesServiceOperStatus_Type()
)
atmxCesServiceOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxCesServiceOperStatus.setStatus("mandatory")


class _AtmxCesServiceServiceMode_Type(Integer32):
    """Custom type atmxCesServiceServiceMode based on Integer32"""
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


_AtmxCesServiceServiceMode_Type.__name__ = "Integer32"
_AtmxCesServiceServiceMode_Object = MibTableColumn
atmxCesServiceServiceMode = _AtmxCesServiceServiceMode_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 1, 1, 1, 6),
    _AtmxCesServiceServiceMode_Type()
)
atmxCesServiceServiceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxCesServiceServiceMode.setStatus("mandatory")


class _AtmxCesServiceServiceClock_Type(Integer32):
    """Custom type atmxCesServiceServiceClock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("adaptive", 3),
          ("srts", 2),
          ("synchronous", 1))
    )


_AtmxCesServiceServiceClock_Type.__name__ = "Integer32"
_AtmxCesServiceServiceClock_Object = MibTableColumn
atmxCesServiceServiceClock = _AtmxCesServiceServiceClock_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 1, 1, 1, 7),
    _AtmxCesServiceServiceClock_Type()
)
atmxCesServiceServiceClock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxCesServiceServiceClock.setStatus("mandatory")


class _AtmxCesServiceAvailTimeSlot_Type(OctetString):
    """Custom type atmxCesServiceAvailTimeSlot based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_AtmxCesServiceAvailTimeSlot_Type.__name__ = "OctetString"
_AtmxCesServiceAvailTimeSlot_Object = MibTableColumn
atmxCesServiceAvailTimeSlot = _AtmxCesServiceAvailTimeSlot_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 1, 1, 1, 8),
    _AtmxCesServiceAvailTimeSlot_Type()
)
atmxCesServiceAvailTimeSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxCesServiceAvailTimeSlot.setStatus("mandatory")
_AtmxCesVccGroup_ObjectIdentity = ObjectIdentity
atmxCesVccGroup = _AtmxCesVccGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 2)
)
_AtmxCesVccTable_Object = MibTable
atmxCesVccTable = _AtmxCesVccTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 2, 1)
)
if mibBuilder.loadTexts:
    atmxCesVccTable.setStatus("mandatory")
_AtmxCesVccEntry_Object = MibTableRow
atmxCesVccEntry = _AtmxCesVccEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 2, 1, 1)
)
atmxCesVccEntry.setIndexNames(
    (0, "XYLAN-ATM-CE-MIB", "atmxCesVccSlotIndex"),
    (0, "XYLAN-ATM-CE-MIB", "atmxCesVccPortIndex"),
    (0, "XYLAN-ATM-CE-MIB", "atmxCesVccVci"),
)
if mibBuilder.loadTexts:
    atmxCesVccEntry.setStatus("mandatory")


class _AtmxCesVccSlotIndex_Type(Integer32):
    """Custom type atmxCesVccSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_AtmxCesVccSlotIndex_Type.__name__ = "Integer32"
_AtmxCesVccSlotIndex_Object = MibTableColumn
atmxCesVccSlotIndex = _AtmxCesVccSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 2, 1, 1, 1),
    _AtmxCesVccSlotIndex_Type()
)
atmxCesVccSlotIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxCesVccSlotIndex.setStatus("mandatory")


class _AtmxCesVccPortIndex_Type(Integer32):
    """Custom type atmxCesVccPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_AtmxCesVccPortIndex_Type.__name__ = "Integer32"
_AtmxCesVccPortIndex_Object = MibTableColumn
atmxCesVccPortIndex = _AtmxCesVccPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 2, 1, 1, 2),
    _AtmxCesVccPortIndex_Type()
)
atmxCesVccPortIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxCesVccPortIndex.setStatus("mandatory")


class _AtmxCesVccVpi_Type(Integer32):
    """Custom type atmxCesVccVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_AtmxCesVccVpi_Type.__name__ = "Integer32"
_AtmxCesVccVpi_Object = MibTableColumn
atmxCesVccVpi = _AtmxCesVccVpi_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 2, 1, 1, 3),
    _AtmxCesVccVpi_Type()
)
atmxCesVccVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxCesVccVpi.setStatus("mandatory")


class _AtmxCesVccVci_Type(Integer32):
    """Custom type atmxCesVccVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1023),
    )


_AtmxCesVccVci_Type.__name__ = "Integer32"
_AtmxCesVccVci_Object = MibTableColumn
atmxCesVccVci = _AtmxCesVccVci_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 2, 1, 1, 4),
    _AtmxCesVccVci_Type()
)
atmxCesVccVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxCesVccVci.setStatus("mandatory")


class _AtmxCesVccAtmUplinkSlotIndex_Type(Integer32):
    """Custom type atmxCesVccAtmUplinkSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_AtmxCesVccAtmUplinkSlotIndex_Type.__name__ = "Integer32"
_AtmxCesVccAtmUplinkSlotIndex_Object = MibTableColumn
atmxCesVccAtmUplinkSlotIndex = _AtmxCesVccAtmUplinkSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 2, 1, 1, 5),
    _AtmxCesVccAtmUplinkSlotIndex_Type()
)
atmxCesVccAtmUplinkSlotIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxCesVccAtmUplinkSlotIndex.setStatus("mandatory")


class _AtmxCesVccAtmUplinkPortIndex_Type(Integer32):
    """Custom type atmxCesVccAtmUplinkPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_AtmxCesVccAtmUplinkPortIndex_Type.__name__ = "Integer32"
_AtmxCesVccAtmUplinkPortIndex_Object = MibTableColumn
atmxCesVccAtmUplinkPortIndex = _AtmxCesVccAtmUplinkPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 2, 1, 1, 6),
    _AtmxCesVccAtmUplinkPortIndex_Type()
)
atmxCesVccAtmUplinkPortIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxCesVccAtmUplinkPortIndex.setStatus("mandatory")


class _AtmxCesVccDescription_Type(DisplayString):
    """Custom type atmxCesVccDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AtmxCesVccDescription_Type.__name__ = "DisplayString"
_AtmxCesVccDescription_Object = MibTableColumn
atmxCesVccDescription = _AtmxCesVccDescription_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 2, 1, 1, 7),
    _AtmxCesVccDescription_Type()
)
atmxCesVccDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxCesVccDescription.setStatus("mandatory")


class _AtmxCesVccAdminStatus_Type(Integer32):
    """Custom type atmxCesVccAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("delete", 3),
          ("down", 2),
          ("up", 1))
    )


_AtmxCesVccAdminStatus_Type.__name__ = "Integer32"
_AtmxCesVccAdminStatus_Object = MibTableColumn
atmxCesVccAdminStatus = _AtmxCesVccAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 2, 1, 1, 8),
    _AtmxCesVccAdminStatus_Type()
)
atmxCesVccAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxCesVccAdminStatus.setStatus("mandatory")


class _AtmxCesVccOperStatus_Type(Integer32):
    """Custom type atmxCesVccOperStatus based on Integer32"""
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


_AtmxCesVccOperStatus_Type.__name__ = "Integer32"
_AtmxCesVccOperStatus_Object = MibTableColumn
atmxCesVccOperStatus = _AtmxCesVccOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 2, 1, 1, 9),
    _AtmxCesVccOperStatus_Type()
)
atmxCesVccOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxCesVccOperStatus.setStatus("mandatory")


class _AtmxCesVccConnType_Type(Integer32):
    """Custom type atmxCesVccConnType based on Integer32"""
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
        *(("activeSvc", 3),
          ("initialSvc", 5),
          ("other", 1),
          ("passiveSvc", 4),
          ("pvc", 2))
    )


_AtmxCesVccConnType_Type.__name__ = "Integer32"
_AtmxCesVccConnType_Object = MibTableColumn
atmxCesVccConnType = _AtmxCesVccConnType_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 2, 1, 1, 10),
    _AtmxCesVccConnType_Type()
)
atmxCesVccConnType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxCesVccConnType.setStatus("mandatory")


class _AtmxCesVccPartialFill_Type(Integer32):
    """Custom type atmxCesVccPartialFill based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 47),
    )


_AtmxCesVccPartialFill_Type.__name__ = "Integer32"
_AtmxCesVccPartialFill_Object = MibTableColumn
atmxCesVccPartialFill = _AtmxCesVccPartialFill_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 2, 1, 1, 11),
    _AtmxCesVccPartialFill_Type()
)
atmxCesVccPartialFill.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxCesVccPartialFill.setStatus("mandatory")


class _AtmxCesVccBufMaxSize_Type(Integer32):
    """Custom type atmxCesVccBufMaxSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512),
    )


_AtmxCesVccBufMaxSize_Type.__name__ = "Integer32"
_AtmxCesVccBufMaxSize_Object = MibTableColumn
atmxCesVccBufMaxSize = _AtmxCesVccBufMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 2, 1, 1, 12),
    _AtmxCesVccBufMaxSize_Type()
)
atmxCesVccBufMaxSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxCesVccBufMaxSize.setStatus("mandatory")


class _AtmxCesVccCDVT_Type(Integer32):
    """Custom type atmxCesVccCDVT based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2400),
    )


_AtmxCesVccCDVT_Type.__name__ = "Integer32"
_AtmxCesVccCDVT_Object = MibTableColumn
atmxCesVccCDVT = _AtmxCesVccCDVT_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 2, 1, 1, 13),
    _AtmxCesVccCDVT_Type()
)
atmxCesVccCDVT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxCesVccCDVT.setStatus("mandatory")


class _AtmxCesVccCellLossIntegrationPeriod_Type(Integer32):
    """Custom type atmxCesVccCellLossIntegrationPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_AtmxCesVccCellLossIntegrationPeriod_Type.__name__ = "Integer32"
_AtmxCesVccCellLossIntegrationPeriod_Object = MibTableColumn
atmxCesVccCellLossIntegrationPeriod = _AtmxCesVccCellLossIntegrationPeriod_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 2, 1, 1, 14),
    _AtmxCesVccCellLossIntegrationPeriod_Type()
)
atmxCesVccCellLossIntegrationPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxCesVccCellLossIntegrationPeriod.setStatus("mandatory")


class _AtmxCesVccIdleCode_Type(Integer32):
    """Custom type atmxCesVccIdleCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AtmxCesVccIdleCode_Type.__name__ = "Integer32"
_AtmxCesVccIdleCode_Object = MibTableColumn
atmxCesVccIdleCode = _AtmxCesVccIdleCode_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 2, 1, 1, 15),
    _AtmxCesVccIdleCode_Type()
)
atmxCesVccIdleCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxCesVccIdleCode.setStatus("mandatory")


class _AtmxCesVccTimeSlots_Type(OctetString):
    """Custom type atmxCesVccTimeSlots based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_AtmxCesVccTimeSlots_Type.__name__ = "OctetString"
_AtmxCesVccTimeSlots_Object = MibTableColumn
atmxCesVccTimeSlots = _AtmxCesVccTimeSlots_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 2, 1, 1, 16),
    _AtmxCesVccTimeSlots_Type()
)
atmxCesVccTimeSlots.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxCesVccTimeSlots.setStatus("mandatory")


class _AtmxCesVccAtmUplinkVccVpi_Type(Integer32):
    """Custom type atmxCesVccAtmUplinkVccVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AtmxCesVccAtmUplinkVccVpi_Type.__name__ = "Integer32"
_AtmxCesVccAtmUplinkVccVpi_Object = MibTableColumn
atmxCesVccAtmUplinkVccVpi = _AtmxCesVccAtmUplinkVccVpi_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 2, 1, 1, 17),
    _AtmxCesVccAtmUplinkVccVpi_Type()
)
atmxCesVccAtmUplinkVccVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxCesVccAtmUplinkVccVpi.setStatus("mandatory")


class _AtmxCesVccAtmUplinkVccVci_Type(Integer32):
    """Custom type atmxCesVccAtmUplinkVccVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AtmxCesVccAtmUplinkVccVci_Type.__name__ = "Integer32"
_AtmxCesVccAtmUplinkVccVci_Object = MibTableColumn
atmxCesVccAtmUplinkVccVci = _AtmxCesVccAtmUplinkVccVci_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 2, 1, 1, 18),
    _AtmxCesVccAtmUplinkVccVci_Type()
)
atmxCesVccAtmUplinkVccVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxCesVccAtmUplinkVccVci.setStatus("mandatory")


class _AtmxCesVccLocalAtmAddr_Type(OctetString):
    """Custom type atmxCesVccLocalAtmAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_AtmxCesVccLocalAtmAddr_Type.__name__ = "OctetString"
_AtmxCesVccLocalAtmAddr_Object = MibTableColumn
atmxCesVccLocalAtmAddr = _AtmxCesVccLocalAtmAddr_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 2, 1, 1, 19),
    _AtmxCesVccLocalAtmAddr_Type()
)
atmxCesVccLocalAtmAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxCesVccLocalAtmAddr.setStatus("mandatory")
_AtmxCesVccStatsGroup_ObjectIdentity = ObjectIdentity
atmxCesVccStatsGroup = _AtmxCesVccStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 3)
)
_AtmxCesVccStatsTable_Object = MibTable
atmxCesVccStatsTable = _AtmxCesVccStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 3, 1)
)
if mibBuilder.loadTexts:
    atmxCesVccStatsTable.setStatus("mandatory")
_AtmxCesVccStatsEntry_Object = MibTableRow
atmxCesVccStatsEntry = _AtmxCesVccStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 3, 1, 1)
)
atmxCesVccStatsEntry.setIndexNames(
    (0, "XYLAN-ATM-CE-MIB", "atmxCesVccStatsSlotIndex"),
    (0, "XYLAN-ATM-CE-MIB", "atmxCesVccStatsPortIndex"),
    (0, "XYLAN-ATM-CE-MIB", "atmCesVccStatsVci"),
)
if mibBuilder.loadTexts:
    atmxCesVccStatsEntry.setStatus("mandatory")


class _AtmxCesVccStatsSlotIndex_Type(Integer32):
    """Custom type atmxCesVccStatsSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_AtmxCesVccStatsSlotIndex_Type.__name__ = "Integer32"
_AtmxCesVccStatsSlotIndex_Object = MibTableColumn
atmxCesVccStatsSlotIndex = _AtmxCesVccStatsSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 3, 1, 1, 1),
    _AtmxCesVccStatsSlotIndex_Type()
)
atmxCesVccStatsSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxCesVccStatsSlotIndex.setStatus("mandatory")


class _AtmxCesVccStatsPortIndex_Type(Integer32):
    """Custom type atmxCesVccStatsPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_AtmxCesVccStatsPortIndex_Type.__name__ = "Integer32"
_AtmxCesVccStatsPortIndex_Object = MibTableColumn
atmxCesVccStatsPortIndex = _AtmxCesVccStatsPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 3, 1, 1, 2),
    _AtmxCesVccStatsPortIndex_Type()
)
atmxCesVccStatsPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxCesVccStatsPortIndex.setStatus("mandatory")
_AtmCesVccStatsVci_Type = Integer32
_AtmCesVccStatsVci_Object = MibTableColumn
atmCesVccStatsVci = _AtmCesVccStatsVci_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 3, 1, 1, 3),
    _AtmCesVccStatsVci_Type()
)
atmCesVccStatsVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmCesVccStatsVci.setStatus("mandatory")
_AtmxCesVccStatsTxDataCells_Type = Counter32
_AtmxCesVccStatsTxDataCells_Object = MibTableColumn
atmxCesVccStatsTxDataCells = _AtmxCesVccStatsTxDataCells_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 3, 1, 1, 4),
    _AtmxCesVccStatsTxDataCells_Type()
)
atmxCesVccStatsTxDataCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxCesVccStatsTxDataCells.setStatus("mandatory")
_AtmxCesVccStatsTxCondCells_Type = Counter32
_AtmxCesVccStatsTxCondCells_Object = MibTableColumn
atmxCesVccStatsTxCondCells = _AtmxCesVccStatsTxCondCells_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 3, 1, 1, 5),
    _AtmxCesVccStatsTxCondCells_Type()
)
atmxCesVccStatsTxCondCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxCesVccStatsTxCondCells.setStatus("mandatory")
_AtmxCesVccStatsSuppressedTxCells_Type = Counter32
_AtmxCesVccStatsSuppressedTxCells_Object = MibTableColumn
atmxCesVccStatsSuppressedTxCells = _AtmxCesVccStatsSuppressedTxCells_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 3, 1, 1, 6),
    _AtmxCesVccStatsSuppressedTxCells_Type()
)
atmxCesVccStatsSuppressedTxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxCesVccStatsSuppressedTxCells.setStatus("mandatory")
_AtmxCesVccStatsRxCells_Type = Counter32
_AtmxCesVccStatsRxCells_Object = MibTableColumn
atmxCesVccStatsRxCells = _AtmxCesVccStatsRxCells_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 3, 1, 1, 7),
    _AtmxCesVccStatsRxCells_Type()
)
atmxCesVccStatsRxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxCesVccStatsRxCells.setStatus("mandatory")
_AtmxCesVccStatsSnpErrors_Type = Counter32
_AtmxCesVccStatsSnpErrors_Object = MibTableColumn
atmxCesVccStatsSnpErrors = _AtmxCesVccStatsSnpErrors_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 3, 1, 1, 8),
    _AtmxCesVccStatsSnpErrors_Type()
)
atmxCesVccStatsSnpErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxCesVccStatsSnpErrors.setStatus("mandatory")
_AtmxCesVccStatsSeqNumErrors_Type = Counter32
_AtmxCesVccStatsSeqNumErrors_Object = MibTableColumn
atmxCesVccStatsSeqNumErrors = _AtmxCesVccStatsSeqNumErrors_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 3, 1, 1, 9),
    _AtmxCesVccStatsSeqNumErrors_Type()
)
atmxCesVccStatsSeqNumErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxCesVccStatsSeqNumErrors.setStatus("mandatory")
_AtmxCesVccStatsDroppedRxCellUnderrun_Type = Counter32
_AtmxCesVccStatsDroppedRxCellUnderrun_Object = MibTableColumn
atmxCesVccStatsDroppedRxCellUnderrun = _AtmxCesVccStatsDroppedRxCellUnderrun_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 3, 1, 1, 10),
    _AtmxCesVccStatsDroppedRxCellUnderrun_Type()
)
atmxCesVccStatsDroppedRxCellUnderrun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxCesVccStatsDroppedRxCellUnderrun.setStatus("mandatory")
_AtmxCesVccStatsDroppedRxCellOverrun_Type = Counter32
_AtmxCesVccStatsDroppedRxCellOverrun_Object = MibTableColumn
atmxCesVccStatsDroppedRxCellOverrun = _AtmxCesVccStatsDroppedRxCellOverrun_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 3, 1, 1, 11),
    _AtmxCesVccStatsDroppedRxCellOverrun_Type()
)
atmxCesVccStatsDroppedRxCellOverrun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxCesVccStatsDroppedRxCellOverrun.setStatus("mandatory")


class _AtmxCesVccStatsCellLossStatus_Type(Integer32):
    """Custom type atmxCesVccStatsCellLossStatus based on Integer32"""
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


_AtmxCesVccStatsCellLossStatus_Type.__name__ = "Integer32"
_AtmxCesVccStatsCellLossStatus_Object = MibTableColumn
atmxCesVccStatsCellLossStatus = _AtmxCesVccStatsCellLossStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 3, 1, 1, 12),
    _AtmxCesVccStatsCellLossStatus_Type()
)
atmxCesVccStatsCellLossStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxCesVccStatsCellLossStatus.setStatus("mandatory")
_AtmxCesVccRateTable_Object = MibTable
atmxCesVccRateTable = _AtmxCesVccRateTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 3, 2)
)
if mibBuilder.loadTexts:
    atmxCesVccRateTable.setStatus("mandatory")
_AtmxCesVccRateEntry_Object = MibTableRow
atmxCesVccRateEntry = _AtmxCesVccRateEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 3, 2, 1)
)
atmxCesVccRateEntry.setIndexNames(
    (0, "XYLAN-ATM-CE-MIB", "atmxCesVccRateSlotIndex"),
    (0, "XYLAN-ATM-CE-MIB", "atmxCesVccRatePortIndex"),
    (0, "XYLAN-ATM-CE-MIB", "atmCesVccRateVci"),
)
if mibBuilder.loadTexts:
    atmxCesVccRateEntry.setStatus("mandatory")


class _AtmxCesVccRateSlotIndex_Type(Integer32):
    """Custom type atmxCesVccRateSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_AtmxCesVccRateSlotIndex_Type.__name__ = "Integer32"
_AtmxCesVccRateSlotIndex_Object = MibTableColumn
atmxCesVccRateSlotIndex = _AtmxCesVccRateSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 3, 2, 1, 1),
    _AtmxCesVccRateSlotIndex_Type()
)
atmxCesVccRateSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxCesVccRateSlotIndex.setStatus("mandatory")


class _AtmxCesVccRatePortIndex_Type(Integer32):
    """Custom type atmxCesVccRatePortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_AtmxCesVccRatePortIndex_Type.__name__ = "Integer32"
_AtmxCesVccRatePortIndex_Object = MibTableColumn
atmxCesVccRatePortIndex = _AtmxCesVccRatePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 3, 2, 1, 2),
    _AtmxCesVccRatePortIndex_Type()
)
atmxCesVccRatePortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxCesVccRatePortIndex.setStatus("mandatory")
_AtmCesVccRateVci_Type = Integer32
_AtmCesVccRateVci_Object = MibTableColumn
atmCesVccRateVci = _AtmCesVccRateVci_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 3, 2, 1, 3),
    _AtmCesVccRateVci_Type()
)
atmCesVccRateVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmCesVccRateVci.setStatus("mandatory")
_AtmxCesVccRateTxDataCells_Type = Counter32
_AtmxCesVccRateTxDataCells_Object = MibTableColumn
atmxCesVccRateTxDataCells = _AtmxCesVccRateTxDataCells_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 3, 2, 1, 4),
    _AtmxCesVccRateTxDataCells_Type()
)
atmxCesVccRateTxDataCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxCesVccRateTxDataCells.setStatus("mandatory")
_AtmxCesVccRateTxCondCells_Type = Counter32
_AtmxCesVccRateTxCondCells_Object = MibTableColumn
atmxCesVccRateTxCondCells = _AtmxCesVccRateTxCondCells_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 3, 2, 1, 5),
    _AtmxCesVccRateTxCondCells_Type()
)
atmxCesVccRateTxCondCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxCesVccRateTxCondCells.setStatus("mandatory")
_AtmxCesVccRateSuppressedTxCells_Type = Counter32
_AtmxCesVccRateSuppressedTxCells_Object = MibTableColumn
atmxCesVccRateSuppressedTxCells = _AtmxCesVccRateSuppressedTxCells_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 3, 2, 1, 6),
    _AtmxCesVccRateSuppressedTxCells_Type()
)
atmxCesVccRateSuppressedTxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxCesVccRateSuppressedTxCells.setStatus("mandatory")
_AtmxCesVccRateRxCells_Type = Counter32
_AtmxCesVccRateRxCells_Object = MibTableColumn
atmxCesVccRateRxCells = _AtmxCesVccRateRxCells_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 3, 2, 1, 7),
    _AtmxCesVccRateRxCells_Type()
)
atmxCesVccRateRxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxCesVccRateRxCells.setStatus("mandatory")
_AtmxCesVccRateSnpErrors_Type = Counter32
_AtmxCesVccRateSnpErrors_Object = MibTableColumn
atmxCesVccRateSnpErrors = _AtmxCesVccRateSnpErrors_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 3, 2, 1, 8),
    _AtmxCesVccRateSnpErrors_Type()
)
atmxCesVccRateSnpErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxCesVccRateSnpErrors.setStatus("mandatory")
_AtmxCesVccRateSeqNumErrors_Type = Counter32
_AtmxCesVccRateSeqNumErrors_Object = MibTableColumn
atmxCesVccRateSeqNumErrors = _AtmxCesVccRateSeqNumErrors_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 3, 2, 1, 9),
    _AtmxCesVccRateSeqNumErrors_Type()
)
atmxCesVccRateSeqNumErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxCesVccRateSeqNumErrors.setStatus("mandatory")
_AtmxCesVccRateDroppedRxCellUnderrun_Type = Counter32
_AtmxCesVccRateDroppedRxCellUnderrun_Object = MibTableColumn
atmxCesVccRateDroppedRxCellUnderrun = _AtmxCesVccRateDroppedRxCellUnderrun_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 3, 2, 1, 10),
    _AtmxCesVccRateDroppedRxCellUnderrun_Type()
)
atmxCesVccRateDroppedRxCellUnderrun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxCesVccRateDroppedRxCellUnderrun.setStatus("mandatory")
_AtmxCesVccRateDroppedRxCellOverrun_Type = Counter32
_AtmxCesVccRateDroppedRxCellOverrun_Object = MibTableColumn
atmxCesVccRateDroppedRxCellOverrun = _AtmxCesVccRateDroppedRxCellOverrun_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 3, 2, 1, 11),
    _AtmxCesVccRateDroppedRxCellOverrun_Type()
)
atmxCesVccRateDroppedRxCellOverrun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxCesVccRateDroppedRxCellOverrun.setStatus("mandatory")
_AtmxCesSvcConfigGroup_ObjectIdentity = ObjectIdentity
atmxCesSvcConfigGroup = _AtmxCesSvcConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 4)
)
_AtmxCesSvcConfigTable_Object = MibTable
atmxCesSvcConfigTable = _AtmxCesSvcConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 4, 1)
)
if mibBuilder.loadTexts:
    atmxCesSvcConfigTable.setStatus("mandatory")
_AtmxCesSvcConfigEntry_Object = MibTableRow
atmxCesSvcConfigEntry = _AtmxCesSvcConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 4, 1, 1)
)
atmxCesSvcConfigEntry.setIndexNames(
    (0, "XYLAN-ATM-CE-MIB", "atmxCesSvcSlotIndex"),
    (0, "XYLAN-ATM-CE-MIB", "atmxCesSvcPortIndex"),
    (0, "XYLAN-ATM-CE-MIB", "atmxCesSvcVciIndex"),
)
if mibBuilder.loadTexts:
    atmxCesSvcConfigEntry.setStatus("mandatory")


class _AtmxCesSvcSlotIndex_Type(Integer32):
    """Custom type atmxCesSvcSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_AtmxCesSvcSlotIndex_Type.__name__ = "Integer32"
_AtmxCesSvcSlotIndex_Object = MibTableColumn
atmxCesSvcSlotIndex = _AtmxCesSvcSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 4, 1, 1, 1),
    _AtmxCesSvcSlotIndex_Type()
)
atmxCesSvcSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxCesSvcSlotIndex.setStatus("mandatory")


class _AtmxCesSvcPortIndex_Type(Integer32):
    """Custom type atmxCesSvcPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_AtmxCesSvcPortIndex_Type.__name__ = "Integer32"
_AtmxCesSvcPortIndex_Object = MibTableColumn
atmxCesSvcPortIndex = _AtmxCesSvcPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 4, 1, 1, 2),
    _AtmxCesSvcPortIndex_Type()
)
atmxCesSvcPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxCesSvcPortIndex.setStatus("mandatory")
_AtmxCesSvcVciIndex_Type = Integer32
_AtmxCesSvcVciIndex_Object = MibTableColumn
atmxCesSvcVciIndex = _AtmxCesSvcVciIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 4, 1, 1, 3),
    _AtmxCesSvcVciIndex_Type()
)
atmxCesSvcVciIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxCesSvcVciIndex.setStatus("mandatory")


class _AtmxCesSvcRemoteAddr_Type(OctetString):
    """Custom type atmxCesSvcRemoteAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_AtmxCesSvcRemoteAddr_Type.__name__ = "OctetString"
_AtmxCesSvcRemoteAddr_Object = MibTableColumn
atmxCesSvcRemoteAddr = _AtmxCesSvcRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 4, 1, 1, 4),
    _AtmxCesSvcRemoteAddr_Type()
)
atmxCesSvcRemoteAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxCesSvcRemoteAddr.setStatus("mandatory")
_AtmxCesSvcRemoteVpi_Type = Integer32
_AtmxCesSvcRemoteVpi_Object = MibTableColumn
atmxCesSvcRemoteVpi = _AtmxCesSvcRemoteVpi_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 4, 1, 1, 5),
    _AtmxCesSvcRemoteVpi_Type()
)
atmxCesSvcRemoteVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxCesSvcRemoteVpi.setStatus("mandatory")
_AtmxCesSvcRemoteVci_Type = Integer32
_AtmxCesSvcRemoteVci_Object = MibTableColumn
atmxCesSvcRemoteVci = _AtmxCesSvcRemoteVci_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 4, 1, 1, 6),
    _AtmxCesSvcRemoteVci_Type()
)
atmxCesSvcRemoteVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxCesSvcRemoteVci.setStatus("mandatory")


class _AtmxCesSvcFirstRetryInterval_Type(Integer32):
    """Custom type atmxCesSvcFirstRetryInterval based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 36000),
    )


_AtmxCesSvcFirstRetryInterval_Type.__name__ = "Integer32"
_AtmxCesSvcFirstRetryInterval_Object = MibTableColumn
atmxCesSvcFirstRetryInterval = _AtmxCesSvcFirstRetryInterval_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 4, 1, 1, 7),
    _AtmxCesSvcFirstRetryInterval_Type()
)
atmxCesSvcFirstRetryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxCesSvcFirstRetryInterval.setStatus("mandatory")


class _AtmxCesSvcRetryTimer_Type(Integer32):
    """Custom type atmxCesSvcRetryTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_AtmxCesSvcRetryTimer_Type.__name__ = "Integer32"
_AtmxCesSvcRetryTimer_Object = MibTableColumn
atmxCesSvcRetryTimer = _AtmxCesSvcRetryTimer_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 4, 1, 1, 8),
    _AtmxCesSvcRetryTimer_Type()
)
atmxCesSvcRetryTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxCesSvcRetryTimer.setStatus("mandatory")


class _AtmxCesSvcRetryLimit_Type(Integer32):
    """Custom type atmxCesSvcRetryLimit based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AtmxCesSvcRetryLimit_Type.__name__ = "Integer32"
_AtmxCesSvcRetryLimit_Object = MibTableColumn
atmxCesSvcRetryLimit = _AtmxCesSvcRetryLimit_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 4, 1, 1, 9),
    _AtmxCesSvcRetryLimit_Type()
)
atmxCesSvcRetryLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxCesSvcRetryLimit.setStatus("mandatory")
_AtmxCesSvcRetryFailures_Type = Integer32
_AtmxCesSvcRetryFailures_Object = MibTableColumn
atmxCesSvcRetryFailures = _AtmxCesSvcRetryFailures_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 4, 1, 1, 10),
    _AtmxCesSvcRetryFailures_Type()
)
atmxCesSvcRetryFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxCesSvcRetryFailures.setStatus("mandatory")


class _AtmxCesSvcConfigRestart_Type(Integer32):
    """Custom type atmxCesSvcConfigRestart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noop", 2),
          ("restart", 1))
    )


_AtmxCesSvcConfigRestart_Type.__name__ = "Integer32"
_AtmxCesSvcConfigRestart_Object = MibTableColumn
atmxCesSvcConfigRestart = _AtmxCesSvcConfigRestart_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 4, 1, 1, 11),
    _AtmxCesSvcConfigRestart_Type()
)
atmxCesSvcConfigRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxCesSvcConfigRestart.setStatus("mandatory")


class _AtmxCesSvcConfigOperStatus_Type(Integer32):
    """Custom type atmxCesSvcConfigOperStatus based on Integer32"""
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
        *(("connected", 3),
          ("establishmentInProgress", 2),
          ("lowerLayerDown", 6),
          ("noAddressSupplied", 5),
          ("other", 1),
          ("retriesExhausted", 4))
    )


_AtmxCesSvcConfigOperStatus_Type.__name__ = "Integer32"
_AtmxCesSvcConfigOperStatus_Object = MibTableColumn
atmxCesSvcConfigOperStatus = _AtmxCesSvcConfigOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 4, 1, 1, 12),
    _AtmxCesSvcConfigOperStatus_Type()
)
atmxCesSvcConfigOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxCesSvcConfigOperStatus.setStatus("mandatory")


class _AtmxCesSvcLastReleaseCause_Type(Integer32):
    """Custom type atmxCesSvcLastReleaseCause based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_AtmxCesSvcLastReleaseCause_Type.__name__ = "Integer32"
_AtmxCesSvcLastReleaseCause_Object = MibTableColumn
atmxCesSvcLastReleaseCause = _AtmxCesSvcLastReleaseCause_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 4, 1, 1, 13),
    _AtmxCesSvcLastReleaseCause_Type()
)
atmxCesSvcLastReleaseCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxCesSvcLastReleaseCause.setStatus("mandatory")


class _AtmxCesSvcLastReleaseDiagnostics_Type(OctetString):
    """Custom type atmxCesSvcLastReleaseDiagnostics based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_AtmxCesSvcLastReleaseDiagnostics_Type.__name__ = "OctetString"
_AtmxCesSvcLastReleaseDiagnostics_Object = MibTableColumn
atmxCesSvcLastReleaseDiagnostics = _AtmxCesSvcLastReleaseDiagnostics_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 1, 4, 1, 1, 14),
    _AtmxCesSvcLastReleaseDiagnostics_Type()
)
atmxCesSvcLastReleaseDiagnostics.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxCesSvcLastReleaseDiagnostics.setStatus("mandatory")
_AtmxCesMIBTraps_ObjectIdentity = ObjectIdentity
atmxCesMIBTraps = _AtmxCesMIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 2)
)
_AtmxCesVccTraps_ObjectIdentity = ObjectIdentity
atmxCesVccTraps = _AtmxCesVccTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 2, 1)
)

# Managed Objects groups


# Notification objects

atmCesVccCreate = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 2, 1, 0, 1)
)
atmCesVccCreate.setObjects(
      *(("XYLAN-ATM-CE-MIB", "atmxCesVccSlotIndex"),
        ("XYLAN-ATM-CE-MIB", "atmxCesVccPortIndex"),
        ("XYLAN-ATM-CE-MIB", "atmxCesVccVpi"),
        ("XYLAN-ATM-CE-MIB", "atmxCesVccVci"),
        ("XYLAN-ATM-CE-MIB", "atmxCesVccAtmUplinkSlotIndex"),
        ("XYLAN-ATM-CE-MIB", "atmxCesVccAtmUplinkPortIndex"))
)
if mibBuilder.loadTexts:
    atmCesVccCreate.setStatus(
        ""
    )

atmCesVccDelete = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 2, 4, 10, 2, 1, 0, 2)
)
atmCesVccDelete.setObjects(
      *(("XYLAN-ATM-CE-MIB", "atmxCesVccSlotIndex"),
        ("XYLAN-ATM-CE-MIB", "atmxCesVccPortIndex"),
        ("XYLAN-ATM-CE-MIB", "atmxCesVccVpi"),
        ("XYLAN-ATM-CE-MIB", "atmxCesVccVci"),
        ("XYLAN-ATM-CE-MIB", "atmxCesVccAtmUplinkSlotIndex"),
        ("XYLAN-ATM-CE-MIB", "atmxCesVccAtmUplinkPortIndex"))
)
if mibBuilder.loadTexts:
    atmCesVccDelete.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "XYLAN-ATM-CE-MIB",
    **{"atmxCesGroup": atmxCesGroup,
       "atmxCesMIBObjects": atmxCesMIBObjects,
       "atmxCesService": atmxCesService,
       "atmxCesServiceTable": atmxCesServiceTable,
       "atmxCesServiceEntry": atmxCesServiceEntry,
       "atmxCesServiceSlotIndex": atmxCesServiceSlotIndex,
       "atmxCesServicePortIndex": atmxCesServicePortIndex,
       "atmxCesServiceDescription": atmxCesServiceDescription,
       "atmxCesServiceAdminStatus": atmxCesServiceAdminStatus,
       "atmxCesServiceOperStatus": atmxCesServiceOperStatus,
       "atmxCesServiceServiceMode": atmxCesServiceServiceMode,
       "atmxCesServiceServiceClock": atmxCesServiceServiceClock,
       "atmxCesServiceAvailTimeSlot": atmxCesServiceAvailTimeSlot,
       "atmxCesVccGroup": atmxCesVccGroup,
       "atmxCesVccTable": atmxCesVccTable,
       "atmxCesVccEntry": atmxCesVccEntry,
       "atmxCesVccSlotIndex": atmxCesVccSlotIndex,
       "atmxCesVccPortIndex": atmxCesVccPortIndex,
       "atmxCesVccVpi": atmxCesVccVpi,
       "atmxCesVccVci": atmxCesVccVci,
       "atmxCesVccAtmUplinkSlotIndex": atmxCesVccAtmUplinkSlotIndex,
       "atmxCesVccAtmUplinkPortIndex": atmxCesVccAtmUplinkPortIndex,
       "atmxCesVccDescription": atmxCesVccDescription,
       "atmxCesVccAdminStatus": atmxCesVccAdminStatus,
       "atmxCesVccOperStatus": atmxCesVccOperStatus,
       "atmxCesVccConnType": atmxCesVccConnType,
       "atmxCesVccPartialFill": atmxCesVccPartialFill,
       "atmxCesVccBufMaxSize": atmxCesVccBufMaxSize,
       "atmxCesVccCDVT": atmxCesVccCDVT,
       "atmxCesVccCellLossIntegrationPeriod": atmxCesVccCellLossIntegrationPeriod,
       "atmxCesVccIdleCode": atmxCesVccIdleCode,
       "atmxCesVccTimeSlots": atmxCesVccTimeSlots,
       "atmxCesVccAtmUplinkVccVpi": atmxCesVccAtmUplinkVccVpi,
       "atmxCesVccAtmUplinkVccVci": atmxCesVccAtmUplinkVccVci,
       "atmxCesVccLocalAtmAddr": atmxCesVccLocalAtmAddr,
       "atmxCesVccStatsGroup": atmxCesVccStatsGroup,
       "atmxCesVccStatsTable": atmxCesVccStatsTable,
       "atmxCesVccStatsEntry": atmxCesVccStatsEntry,
       "atmxCesVccStatsSlotIndex": atmxCesVccStatsSlotIndex,
       "atmxCesVccStatsPortIndex": atmxCesVccStatsPortIndex,
       "atmCesVccStatsVci": atmCesVccStatsVci,
       "atmxCesVccStatsTxDataCells": atmxCesVccStatsTxDataCells,
       "atmxCesVccStatsTxCondCells": atmxCesVccStatsTxCondCells,
       "atmxCesVccStatsSuppressedTxCells": atmxCesVccStatsSuppressedTxCells,
       "atmxCesVccStatsRxCells": atmxCesVccStatsRxCells,
       "atmxCesVccStatsSnpErrors": atmxCesVccStatsSnpErrors,
       "atmxCesVccStatsSeqNumErrors": atmxCesVccStatsSeqNumErrors,
       "atmxCesVccStatsDroppedRxCellUnderrun": atmxCesVccStatsDroppedRxCellUnderrun,
       "atmxCesVccStatsDroppedRxCellOverrun": atmxCesVccStatsDroppedRxCellOverrun,
       "atmxCesVccStatsCellLossStatus": atmxCesVccStatsCellLossStatus,
       "atmxCesVccRateTable": atmxCesVccRateTable,
       "atmxCesVccRateEntry": atmxCesVccRateEntry,
       "atmxCesVccRateSlotIndex": atmxCesVccRateSlotIndex,
       "atmxCesVccRatePortIndex": atmxCesVccRatePortIndex,
       "atmCesVccRateVci": atmCesVccRateVci,
       "atmxCesVccRateTxDataCells": atmxCesVccRateTxDataCells,
       "atmxCesVccRateTxCondCells": atmxCesVccRateTxCondCells,
       "atmxCesVccRateSuppressedTxCells": atmxCesVccRateSuppressedTxCells,
       "atmxCesVccRateRxCells": atmxCesVccRateRxCells,
       "atmxCesVccRateSnpErrors": atmxCesVccRateSnpErrors,
       "atmxCesVccRateSeqNumErrors": atmxCesVccRateSeqNumErrors,
       "atmxCesVccRateDroppedRxCellUnderrun": atmxCesVccRateDroppedRxCellUnderrun,
       "atmxCesVccRateDroppedRxCellOverrun": atmxCesVccRateDroppedRxCellOverrun,
       "atmxCesSvcConfigGroup": atmxCesSvcConfigGroup,
       "atmxCesSvcConfigTable": atmxCesSvcConfigTable,
       "atmxCesSvcConfigEntry": atmxCesSvcConfigEntry,
       "atmxCesSvcSlotIndex": atmxCesSvcSlotIndex,
       "atmxCesSvcPortIndex": atmxCesSvcPortIndex,
       "atmxCesSvcVciIndex": atmxCesSvcVciIndex,
       "atmxCesSvcRemoteAddr": atmxCesSvcRemoteAddr,
       "atmxCesSvcRemoteVpi": atmxCesSvcRemoteVpi,
       "atmxCesSvcRemoteVci": atmxCesSvcRemoteVci,
       "atmxCesSvcFirstRetryInterval": atmxCesSvcFirstRetryInterval,
       "atmxCesSvcRetryTimer": atmxCesSvcRetryTimer,
       "atmxCesSvcRetryLimit": atmxCesSvcRetryLimit,
       "atmxCesSvcRetryFailures": atmxCesSvcRetryFailures,
       "atmxCesSvcConfigRestart": atmxCesSvcConfigRestart,
       "atmxCesSvcConfigOperStatus": atmxCesSvcConfigOperStatus,
       "atmxCesSvcLastReleaseCause": atmxCesSvcLastReleaseCause,
       "atmxCesSvcLastReleaseDiagnostics": atmxCesSvcLastReleaseDiagnostics,
       "atmxCesMIBTraps": atmxCesMIBTraps,
       "atmxCesVccTraps": atmxCesVccTraps,
       "atmCesVccCreate": atmCesVccCreate,
       "atmCesVccDelete": atmCesVccDelete}
)
