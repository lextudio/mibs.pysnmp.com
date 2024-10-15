# SNMP MIB module (HUAWEI-MUSA-MA5100-CONFMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-MUSA-MA5100-CONFMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:05:18 2024
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

(musa,) = mibBuilder.importSymbols(
    "HUAWEI-MIB",
    "musa")

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



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwMa5100Mib_ObjectIdentity = ObjectIdentity
hwMa5100Mib = _HwMa5100Mib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5)
)
_HwMusaSysMib_ObjectIdentity = ObjectIdentity
hwMusaSysMib = _HwMusaSysMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1)
)
_HwMusaSlotGroup_ObjectIdentity = ObjectIdentity
hwMusaSlotGroup = _HwMusaSlotGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 6)
)
_HwMusaFrame_ObjectIdentity = ObjectIdentity
hwMusaFrame = _HwMusaFrame_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 6, 2)
)
_HwMusaFrameNumber_Type = Integer32
_HwMusaFrameNumber_Object = MibScalar
hwMusaFrameNumber = _HwMusaFrameNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 6, 2, 1),
    _HwMusaFrameNumber_Type()
)
hwMusaFrameNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMusaFrameNumber.setStatus("mandatory")
_HwMusaFrameConfTable_Object = MibTable
hwMusaFrameConfTable = _HwMusaFrameConfTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 6, 2, 2)
)
if mibBuilder.loadTexts:
    hwMusaFrameConfTable.setStatus("mandatory")
_HwMusaFrameConfEntry_Object = MibTableRow
hwMusaFrameConfEntry = _HwMusaFrameConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 6, 2, 2, 1)
)
hwMusaFrameConfEntry.setIndexNames(
    (0, "HUAWEI-MUSA-MA5100-CONFMIB", "hwMusaShelfIndex"),
    (0, "HUAWEI-MUSA-MA5100-CONFMIB", "hwMusaFrameIndex"),
)
if mibBuilder.loadTexts:
    hwMusaFrameConfEntry.setStatus("mandatory")
_HwMusaFrameIndex_Type = Integer32
_HwMusaFrameIndex_Object = MibTableColumn
hwMusaFrameIndex = _HwMusaFrameIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 6, 2, 2, 1, 1),
    _HwMusaFrameIndex_Type()
)
hwMusaFrameIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMusaFrameIndex.setStatus("mandatory")
_HwMusaSlot_ObjectIdentity = ObjectIdentity
hwMusaSlot = _HwMusaSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 6, 3)
)
_HwMusaSlotConfTable_Object = MibTable
hwMusaSlotConfTable = _HwMusaSlotConfTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 6, 3, 2)
)
if mibBuilder.loadTexts:
    hwMusaSlotConfTable.setStatus("mandatory")
_HwMusaSlotConfEntry_Object = MibTableRow
hwMusaSlotConfEntry = _HwMusaSlotConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 6, 3, 2, 1)
)
hwMusaSlotConfEntry.setIndexNames(
    (0, "HUAWEI-MUSA-MA5100-CONFMIB", "hwMusaFrameIndex"),
    (0, "HUAWEI-MUSA-MA5100-CONFMIB", "hwMusaSlotIndex"),
)
if mibBuilder.loadTexts:
    hwMusaSlotConfEntry.setStatus("mandatory")


class _HwMusaSlotIndex_Type(Integer32):
    """Custom type hwMusaSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_HwMusaSlotIndex_Type.__name__ = "Integer32"
_HwMusaSlotIndex_Object = MibTableColumn
hwMusaSlotIndex = _HwMusaSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 6, 3, 2, 1, 1),
    _HwMusaSlotIndex_Type()
)
hwMusaSlotIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMusaSlotIndex.setStatus("mandatory")
_HwMusaRegionPvcConfTable_Object = MibTable
hwMusaRegionPvcConfTable = _HwMusaRegionPvcConfTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 15)
)
if mibBuilder.loadTexts:
    hwMusaRegionPvcConfTable.setStatus("mandatory")
_HwMusaRegionPvcConfEntry_Object = MibTableRow
hwMusaRegionPvcConfEntry = _HwMusaRegionPvcConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 15, 1)
)
hwMusaRegionPvcConfEntry.setIndexNames(
    (0, "HUAWEI-MUSA-MA5100-CONFMIB", "hwMusaFrameIndex"),
    (0, "HUAWEI-MUSA-MA5100-CONFMIB", "hwMusaSlotIndex"),
    (0, "HUAWEI-MUSA-MA5100-CONFMIB", "hwMusaVlanId"),
    (0, "HUAWEI-MUSA-MA5100-CONFMIB", "hwMusaVlanIciIndex"),
)
if mibBuilder.loadTexts:
    hwMusaRegionPvcConfEntry.setStatus("mandatory")


class _HwMusaVlanId_Type(Integer32):
    """Custom type hwMusaVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )


_HwMusaVlanId_Type.__name__ = "Integer32"
_HwMusaVlanId_Object = MibTableColumn
hwMusaVlanId = _HwMusaVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 15, 1, 1),
    _HwMusaVlanId_Type()
)
hwMusaVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMusaVlanId.setStatus("mandatory")
_HwMusaVlanIciIndex_Type = Integer32
_HwMusaVlanIciIndex_Object = MibTableColumn
hwMusaVlanIciIndex = _HwMusaVlanIciIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 15, 1, 2),
    _HwMusaVlanIciIndex_Type()
)
hwMusaVlanIciIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMusaVlanIciIndex.setStatus("mandatory")


class _HwMusaAdlFrameId_Type(Integer32):
    """Custom type hwMusaAdlFrameId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_HwMusaAdlFrameId_Type.__name__ = "Integer32"
_HwMusaAdlFrameId_Object = MibTableColumn
hwMusaAdlFrameId = _HwMusaAdlFrameId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 15, 1, 4),
    _HwMusaAdlFrameId_Type()
)
hwMusaAdlFrameId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaAdlFrameId.setStatus("mandatory")


class _HwMusaAdlSlotId_Type(Integer32):
    """Custom type hwMusaAdlSlotId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_HwMusaAdlSlotId_Type.__name__ = "Integer32"
_HwMusaAdlSlotId_Object = MibTableColumn
hwMusaAdlSlotId = _HwMusaAdlSlotId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 15, 1, 5),
    _HwMusaAdlSlotId_Type()
)
hwMusaAdlSlotId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaAdlSlotId.setStatus("mandatory")


class _HwMusaAdlPortId_Type(Integer32):
    """Custom type hwMusaAdlPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_HwMusaAdlPortId_Type.__name__ = "Integer32"
_HwMusaAdlPortId_Object = MibTableColumn
hwMusaAdlPortId = _HwMusaAdlPortId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 15, 1, 6),
    _HwMusaAdlPortId_Type()
)
hwMusaAdlPortId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaAdlPortId.setStatus("mandatory")


class _HwMusaAdlVpi_Type(Integer32):
    """Custom type hwMusaAdlVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_HwMusaAdlVpi_Type.__name__ = "Integer32"
_HwMusaAdlVpi_Object = MibTableColumn
hwMusaAdlVpi = _HwMusaAdlVpi_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 15, 1, 7),
    _HwMusaAdlVpi_Type()
)
hwMusaAdlVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMusaAdlVpi.setStatus("mandatory")


class _HwMusaAdlVci_Type(Integer32):
    """Custom type hwMusaAdlVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 127),
    )


_HwMusaAdlVci_Type.__name__ = "Integer32"
_HwMusaAdlVci_Object = MibTableColumn
hwMusaAdlVci = _HwMusaAdlVci_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 15, 1, 8),
    _HwMusaAdlVci_Type()
)
hwMusaAdlVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMusaAdlVci.setStatus("mandatory")
_HwMusaToLanTrafficId_Type = Integer32
_HwMusaToLanTrafficId_Object = MibTableColumn
hwMusaToLanTrafficId = _HwMusaToLanTrafficId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 15, 1, 9),
    _HwMusaToLanTrafficId_Type()
)
hwMusaToLanTrafficId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaToLanTrafficId.setStatus("mandatory")
_HwMusaFromLanTrafficId_Type = Integer32
_HwMusaFromLanTrafficId_Object = MibTableColumn
hwMusaFromLanTrafficId = _HwMusaFromLanTrafficId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 15, 1, 10),
    _HwMusaFromLanTrafficId_Type()
)
hwMusaFromLanTrafficId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaFromLanTrafficId.setStatus("mandatory")


class _HwMusaAdlPortOperat_Type(Integer32):
    """Custom type hwMusaAdlPortOperat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("add", 0),
          ("del", 1))
    )


_HwMusaAdlPortOperat_Type.__name__ = "Integer32"
_HwMusaAdlPortOperat_Object = MibTableColumn
hwMusaAdlPortOperat = _HwMusaAdlPortOperat_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 15, 1, 11),
    _HwMusaAdlPortOperat_Type()
)
hwMusaAdlPortOperat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaAdlPortOperat.setStatus("mandatory")
_HwMusaAllPvcConfTable_Object = MibTable
hwMusaAllPvcConfTable = _HwMusaAllPvcConfTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 22)
)
if mibBuilder.loadTexts:
    hwMusaAllPvcConfTable.setStatus("mandatory")
_HwMusaAllPvcConfEntry_Object = MibTableRow
hwMusaAllPvcConfEntry = _HwMusaAllPvcConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 22, 1)
)
hwMusaAllPvcConfEntry.setIndexNames(
    (0, "HUAWEI-MUSA-MA5100-CONFMIB", "hwMusaTypeOfPvcPvpindex"),
    (0, "HUAWEI-MUSA-MA5100-CONFMIB", "hwMusaCidIndex"),
)
if mibBuilder.loadTexts:
    hwMusaAllPvcConfEntry.setStatus("mandatory")
_HwMusaCidIndex_Type = Counter32
_HwMusaCidIndex_Object = MibTableColumn
hwMusaCidIndex = _HwMusaCidIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 22, 1, 1),
    _HwMusaCidIndex_Type()
)
hwMusaCidIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMusaCidIndex.setStatus("mandatory")
_HwMusaSrcFrameId_Type = Integer32
_HwMusaSrcFrameId_Object = MibTableColumn
hwMusaSrcFrameId = _HwMusaSrcFrameId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 22, 1, 2),
    _HwMusaSrcFrameId_Type()
)
hwMusaSrcFrameId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaSrcFrameId.setStatus("mandatory")
_HwMuasSrcSlotId_Type = Integer32
_HwMuasSrcSlotId_Object = MibTableColumn
hwMuasSrcSlotId = _HwMuasSrcSlotId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 22, 1, 3),
    _HwMuasSrcSlotId_Type()
)
hwMuasSrcSlotId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMuasSrcSlotId.setStatus("mandatory")
_HwMusaSrcPortVlanVccId_Type = Integer32
_HwMusaSrcPortVlanVccId_Object = MibTableColumn
hwMusaSrcPortVlanVccId = _HwMusaSrcPortVlanVccId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 22, 1, 4),
    _HwMusaSrcPortVlanVccId_Type()
)
hwMusaSrcPortVlanVccId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaSrcPortVlanVccId.setStatus("mandatory")
_HwMusaSrcBoardVpi_Type = Integer32
_HwMusaSrcBoardVpi_Object = MibTableColumn
hwMusaSrcBoardVpi = _HwMusaSrcBoardVpi_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 22, 1, 6),
    _HwMusaSrcBoardVpi_Type()
)
hwMusaSrcBoardVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaSrcBoardVpi.setStatus("mandatory")
_HwMusaSrcBoardVci_Type = Integer32
_HwMusaSrcBoardVci_Object = MibTableColumn
hwMusaSrcBoardVci = _HwMusaSrcBoardVci_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 22, 1, 7),
    _HwMusaSrcBoardVci_Type()
)
hwMusaSrcBoardVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaSrcBoardVci.setStatus("mandatory")
_HwMusaSrcUpcEpdPpd_Type = Integer32
_HwMusaSrcUpcEpdPpd_Object = MibTableColumn
hwMusaSrcUpcEpdPpd = _HwMusaSrcUpcEpdPpd_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 22, 1, 16),
    _HwMusaSrcUpcEpdPpd_Type()
)
hwMusaSrcUpcEpdPpd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaSrcUpcEpdPpd.setStatus("mandatory")
_HwMusaDestFrameId_Type = Integer32
_HwMusaDestFrameId_Object = MibTableColumn
hwMusaDestFrameId = _HwMusaDestFrameId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 22, 1, 20),
    _HwMusaDestFrameId_Type()
)
hwMusaDestFrameId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaDestFrameId.setStatus("mandatory")
_HwMusaDestSlotId_Type = Integer32
_HwMusaDestSlotId_Object = MibTableColumn
hwMusaDestSlotId = _HwMusaDestSlotId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 22, 1, 21),
    _HwMusaDestSlotId_Type()
)
hwMusaDestSlotId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaDestSlotId.setStatus("mandatory")
_HwMusaDestPortVlanVccId_Type = Integer32
_HwMusaDestPortVlanVccId_Object = MibTableColumn
hwMusaDestPortVlanVccId = _HwMusaDestPortVlanVccId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 22, 1, 22),
    _HwMusaDestPortVlanVccId_Type()
)
hwMusaDestPortVlanVccId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaDestPortVlanVccId.setStatus("mandatory")
_HwMusaDestBoardVpi_Type = Integer32
_HwMusaDestBoardVpi_Object = MibTableColumn
hwMusaDestBoardVpi = _HwMusaDestBoardVpi_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 22, 1, 24),
    _HwMusaDestBoardVpi_Type()
)
hwMusaDestBoardVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaDestBoardVpi.setStatus("mandatory")
_HwMusaDestBoardVci_Type = Integer32
_HwMusaDestBoardVci_Object = MibTableColumn
hwMusaDestBoardVci = _HwMusaDestBoardVci_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 22, 1, 25),
    _HwMusaDestBoardVci_Type()
)
hwMusaDestBoardVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaDestBoardVci.setStatus("mandatory")
_HwMusaDestUpcEpdPpd_Type = Integer32
_HwMusaDestUpcEpdPpd_Object = MibTableColumn
hwMusaDestUpcEpdPpd = _HwMusaDestUpcEpdPpd_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 22, 1, 34),
    _HwMusaDestUpcEpdPpd_Type()
)
hwMusaDestUpcEpdPpd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaDestUpcEpdPpd.setStatus("mandatory")
_HwMusaSrcToDestTraffic_Type = Integer32
_HwMusaSrcToDestTraffic_Object = MibTableColumn
hwMusaSrcToDestTraffic = _HwMusaSrcToDestTraffic_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 22, 1, 38),
    _HwMusaSrcToDestTraffic_Type()
)
hwMusaSrcToDestTraffic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaSrcToDestTraffic.setStatus("mandatory")
_HwMusaDestToSrcTraffic_Type = Integer32
_HwMusaDestToSrcTraffic_Object = MibTableColumn
hwMusaDestToSrcTraffic = _HwMusaDestToSrcTraffic_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 22, 1, 39),
    _HwMusaDestToSrcTraffic_Type()
)
hwMusaDestToSrcTraffic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaDestToSrcTraffic.setStatus("mandatory")


class _HwMusaAllPvcOperater_Type(Integer32):
    """Custom type hwMusaAllPvcOperater based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("add", 0),
          ("del", 1))
    )


_HwMusaAllPvcOperater_Type.__name__ = "Integer32"
_HwMusaAllPvcOperater_Object = MibTableColumn
hwMusaAllPvcOperater = _HwMusaAllPvcOperater_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 22, 1, 40),
    _HwMusaAllPvcOperater_Type()
)
hwMusaAllPvcOperater.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaAllPvcOperater.setStatus("mandatory")


class _HwMusaTypeOfPvcPvpindex_Type(Integer32):
    """Custom type hwMusaTypeOfPvcPvpindex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("pvc", 0),
          ("pvp", 1))
    )


_HwMusaTypeOfPvcPvpindex_Type.__name__ = "Integer32"
_HwMusaTypeOfPvcPvpindex_Object = MibTableColumn
hwMusaTypeOfPvcPvpindex = _HwMusaTypeOfPvcPvpindex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 22, 1, 41),
    _HwMusaTypeOfPvcPvpindex_Type()
)
hwMusaTypeOfPvcPvpindex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaTypeOfPvcPvpindex.setStatus("mandatory")


class _HwMusaPvcPvpState_Type(Integer32):
    """Custom type hwMusaPvcPvpState based on Integer32"""
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
          ("invalid", 2),
          ("normal", 1))
    )


_HwMusaPvcPvpState_Type.__name__ = "Integer32"
_HwMusaPvcPvpState_Object = MibTableColumn
hwMusaPvcPvpState = _HwMusaPvcPvpState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 22, 1, 42),
    _HwMusaPvcPvpState_Type()
)
hwMusaPvcPvpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMusaPvcPvpState.setStatus("mandatory")
_HwMusaAdlb_ObjectIdentity = ObjectIdentity
hwMusaAdlb = _HwMusaAdlb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6)
)
_HwMusaAdlbBoard_ObjectIdentity = ObjectIdentity
hwMusaAdlbBoard = _HwMusaAdlbBoard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 1)
)
_HwMusaAdlbBoardInfoTable_Object = MibTable
hwMusaAdlbBoardInfoTable = _HwMusaAdlbBoardInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 1, 1)
)
if mibBuilder.loadTexts:
    hwMusaAdlbBoardInfoTable.setStatus("mandatory")
_HwMusaAdlbBoardInfoEntry_Object = MibTableRow
hwMusaAdlbBoardInfoEntry = _HwMusaAdlbBoardInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 1, 1, 1)
)
hwMusaAdlbBoardInfoEntry.setIndexNames(
    (0, "HUAWEI-MUSA-MA5100-CONFMIB", "hwMusaFrameIndex"),
    (0, "HUAWEI-MUSA-MA5100-CONFMIB", "hwMusaSlotIndex"),
)
if mibBuilder.loadTexts:
    hwMusaAdlbBoardInfoEntry.setStatus("mandatory")
_AdlbProductId_Type = Integer32
_AdlbProductId_Object = MibTableColumn
adlbProductId = _AdlbProductId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 1, 1, 1, 1),
    _AdlbProductId_Type()
)
adlbProductId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbProductId.setStatus("mandatory")


class _AdlbCustomId_Type(Integer32):
    """Custom type adlbCustomId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("isdn", 1),
          ("pots", 2),
          ("unknown", 0))
    )


_AdlbCustomId_Type.__name__ = "Integer32"
_AdlbCustomId_Object = MibTableColumn
adlbCustomId = _AdlbCustomId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 1, 1, 1, 2),
    _AdlbCustomId_Type()
)
adlbCustomId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbCustomId.setStatus("mandatory")
_AdlbAtucRomSwVer_Type = DisplayString
_AdlbAtucRomSwVer_Object = MibTableColumn
adlbAtucRomSwVer = _AdlbAtucRomSwVer_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 1, 1, 1, 3),
    _AdlbAtucRomSwVer_Type()
)
adlbAtucRomSwVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAtucRomSwVer.setStatus("mandatory")
_AdlbAtucRomSwBuildDate_Type = DisplayString
_AdlbAtucRomSwBuildDate_Object = MibTableColumn
adlbAtucRomSwBuildDate = _AdlbAtucRomSwBuildDate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 1, 1, 1, 4),
    _AdlbAtucRomSwBuildDate_Type()
)
adlbAtucRomSwBuildDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAtucRomSwBuildDate.setStatus("mandatory")
_AdlbAtucOamSwVer_Type = DisplayString
_AdlbAtucOamSwVer_Object = MibTableColumn
adlbAtucOamSwVer = _AdlbAtucOamSwVer_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 1, 1, 1, 5),
    _AdlbAtucOamSwVer_Type()
)
adlbAtucOamSwVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAtucOamSwVer.setStatus("mandatory")
_AdlbAtucOamSwBuildDate_Type = DisplayString
_AdlbAtucOamSwBuildDate_Object = MibTableColumn
adlbAtucOamSwBuildDate = _AdlbAtucOamSwBuildDate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 1, 1, 1, 6),
    _AdlbAtucOamSwBuildDate_Type()
)
adlbAtucOamSwBuildDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAtucOamSwBuildDate.setStatus("mandatory")
_AdlbByDiagCodeVer_Type = DisplayString
_AdlbByDiagCodeVer_Object = MibTableColumn
adlbByDiagCodeVer = _AdlbByDiagCodeVer_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 1, 1, 1, 7),
    _AdlbByDiagCodeVer_Type()
)
adlbByDiagCodeVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbByDiagCodeVer.setStatus("mandatory")
_AdlbByModemCodeVer_Type = DisplayString
_AdlbByModemCodeVer_Object = MibTableColumn
adlbByModemCodeVer = _AdlbByModemCodeVer_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 1, 1, 1, 8),
    _AdlbByModemCodeVer_Type()
)
adlbByModemCodeVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbByModemCodeVer.setStatus("mandatory")
_AdlbAtucVendorId_Type = Integer32
_AdlbAtucVendorId_Object = MibTableColumn
adlbAtucVendorId = _AdlbAtucVendorId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 1, 1, 1, 9),
    _AdlbAtucVendorId_Type()
)
adlbAtucVendorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAtucVendorId.setStatus("mandatory")
_AdlbAtucVersionNo_Type = Integer32
_AdlbAtucVersionNo_Object = MibTableColumn
adlbAtucVersionNo = _AdlbAtucVersionNo_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 1, 1, 1, 10),
    _AdlbAtucVersionNo_Type()
)
adlbAtucVersionNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAtucVersionNo.setStatus("mandatory")
_AdlbItuCountryCode_Type = Integer32
_AdlbItuCountryCode_Object = MibTableColumn
adlbItuCountryCode = _AdlbItuCountryCode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 1, 1, 1, 11),
    _AdlbItuCountryCode_Type()
)
adlbItuCountryCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbItuCountryCode.setStatus("mandatory")
_AdlbItuProviderCode_Type = DisplayString
_AdlbItuProviderCode_Object = MibTableColumn
adlbItuProviderCode = _AdlbItuProviderCode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 1, 1, 1, 12),
    _AdlbItuProviderCode_Type()
)
adlbItuProviderCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbItuProviderCode.setStatus("mandatory")
_HwMusaAdlbChipset_ObjectIdentity = ObjectIdentity
hwMusaAdlbChipset = _HwMusaAdlbChipset_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 2)
)
_HwMusaAdlbChipsetMtTable_Object = MibTable
hwMusaAdlbChipsetMtTable = _HwMusaAdlbChipsetMtTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 2, 1)
)
if mibBuilder.loadTexts:
    hwMusaAdlbChipsetMtTable.setStatus("mandatory")
_HwMusaAdlbChipsetMtEntry_Object = MibTableRow
hwMusaAdlbChipsetMtEntry = _HwMusaAdlbChipsetMtEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 2, 1, 1)
)
hwMusaAdlbChipsetMtEntry.setIndexNames(
    (0, "HUAWEI-MUSA-MA5100-CONFMIB", "hwMusaFrameIndex"),
    (0, "HUAWEI-MUSA-MA5100-CONFMIB", "hwMusaSlotIndex"),
    (0, "HUAWEI-MUSA-MA5100-CONFMIB", "adlbChipsetIndex"),
)
if mibBuilder.loadTexts:
    hwMusaAdlbChipsetMtEntry.setStatus("mandatory")


class _AdlbChipsetIndex_Type(Integer32):
    """Custom type adlbChipsetIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_AdlbChipsetIndex_Type.__name__ = "Integer32"
_AdlbChipsetIndex_Object = MibTableColumn
adlbChipsetIndex = _AdlbChipsetIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 2, 1, 1, 1),
    _AdlbChipsetIndex_Type()
)
adlbChipsetIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adlbChipsetIndex.setStatus("mandatory")
_AdlbChipsetOper_Type = Integer32
_AdlbChipsetOper_Object = MibTableColumn
adlbChipsetOper = _AdlbChipsetOper_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 2, 1, 1, 2),
    _AdlbChipsetOper_Type()
)
adlbChipsetOper.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    adlbChipsetOper.setStatus("mandatory")
_HwMusaAdlbConf_ObjectIdentity = ObjectIdentity
hwMusaAdlbConf = _HwMusaAdlbConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 3)
)
_HwMusaAdlbPortDeviceTable_Object = MibTable
hwMusaAdlbPortDeviceTable = _HwMusaAdlbPortDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 3, 1)
)
if mibBuilder.loadTexts:
    hwMusaAdlbPortDeviceTable.setStatus("mandatory")
_HwMusaAdlbPortDeviceEntry_Object = MibTableRow
hwMusaAdlbPortDeviceEntry = _HwMusaAdlbPortDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 3, 1, 1)
)
hwMusaAdlbPortDeviceEntry.setIndexNames(
    (0, "HUAWEI-MUSA-MA5100-CONFMIB", "hwMusaFrameIndex"),
    (0, "HUAWEI-MUSA-MA5100-CONFMIB", "hwMusaSlotIndex"),
    (0, "HUAWEI-MUSA-MA5100-CONFMIB", "adlbPortIndex"),
)
if mibBuilder.loadTexts:
    hwMusaAdlbPortDeviceEntry.setStatus("mandatory")


class _AdlbPortIndex_Type(Integer32):
    """Custom type adlbPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_AdlbPortIndex_Type.__name__ = "Integer32"
_AdlbPortIndex_Object = MibTableColumn
adlbPortIndex = _AdlbPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 3, 1, 1, 1),
    _AdlbPortIndex_Type()
)
adlbPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adlbPortIndex.setStatus("mandatory")
_AdlbAturVendorId_Type = Integer32
_AdlbAturVendorId_Object = MibTableColumn
adlbAturVendorId = _AdlbAturVendorId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 3, 1, 1, 2),
    _AdlbAturVendorId_Type()
)
adlbAturVendorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAturVendorId.setStatus("mandatory")
_AdlbAturVersion_Type = Integer32
_AdlbAturVersion_Object = MibTableColumn
adlbAturVersion = _AdlbAturVersion_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 3, 1, 1, 3),
    _AdlbAturVersion_Type()
)
adlbAturVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAturVersion.setStatus("mandatory")
_AdlbAturCountryCode_Type = Integer32
_AdlbAturCountryCode_Object = MibTableColumn
adlbAturCountryCode = _AdlbAturCountryCode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 3, 1, 1, 4),
    _AdlbAturCountryCode_Type()
)
adlbAturCountryCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAturCountryCode.setStatus("mandatory")
_AdlbAturProviderCode_Type = Integer32
_AdlbAturProviderCode_Object = MibTableColumn
adlbAturProviderCode = _AdlbAturProviderCode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 3, 1, 1, 5),
    _AdlbAturProviderCode_Type()
)
adlbAturProviderCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAturProviderCode.setStatus("mandatory")
_AdlbAturAdslCapability_Type = Integer32
_AdlbAturAdslCapability_Object = MibTableColumn
adlbAturAdslCapability = _AdlbAturAdslCapability_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 3, 1, 1, 6),
    _AdlbAturAdslCapability_Type()
)
adlbAturAdslCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAturAdslCapability.setStatus("mandatory")
_HwMusaAdlbPortTable_Object = MibTable
hwMusaAdlbPortTable = _HwMusaAdlbPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 3, 2)
)
if mibBuilder.loadTexts:
    hwMusaAdlbPortTable.setStatus("mandatory")
_HwMusaAdlbPortEntry_Object = MibTableRow
hwMusaAdlbPortEntry = _HwMusaAdlbPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 3, 2, 1)
)
hwMusaAdlbPortEntry.setIndexNames(
    (0, "HUAWEI-MUSA-MA5100-CONFMIB", "hwMusaFrameIndex"),
    (0, "HUAWEI-MUSA-MA5100-CONFMIB", "hwMusaSlotIndex"),
    (0, "HUAWEI-MUSA-MA5100-CONFMIB", "adlbPortIndex"),
)
if mibBuilder.loadTexts:
    hwMusaAdlbPortEntry.setStatus("mandatory")


class _AdlbPortState_Type(Integer32):
    """Custom type adlbPortState based on Integer32"""
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
              255)
        )
    )
    namedValues = NamedValues(
        *(("activating", 3),
          ("active", 0),
          ("bad", 2),
          ("block", 5),
          ("deactivating", 4),
          ("deactive", 1),
          ("other", 255),
          ("unblock", 6))
    )


_AdlbPortState_Type.__name__ = "Integer32"
_AdlbPortState_Object = MibTableColumn
adlbPortState = _AdlbPortState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 3, 2, 1, 1),
    _AdlbPortState_Type()
)
adlbPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbPortState.setStatus("mandatory")


class _AdlbPortTrainStandard_Type(Integer32):
    """Custom type adlbPortTrainStandard based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dmt", 1),
          ("glite", 2),
          ("none", 0),
          ("t1413", 3))
    )


_AdlbPortTrainStandard_Type.__name__ = "Integer32"
_AdlbPortTrainStandard_Object = MibTableColumn
adlbPortTrainStandard = _AdlbPortTrainStandard_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 3, 2, 1, 2),
    _AdlbPortTrainStandard_Type()
)
adlbPortTrainStandard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbPortTrainStandard.setStatus("mandatory")


class _AdlbPortOper_Type(Integer32):
    """Custom type adlbPortOper based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("block", 1),
          ("clearCellStat", 3),
          ("deact", 0),
          ("unblock", 2))
    )


_AdlbPortOper_Type.__name__ = "Integer32"
_AdlbPortOper_Object = MibTableColumn
adlbPortOper = _AdlbPortOper_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 3, 2, 1, 3),
    _AdlbPortOper_Type()
)
adlbPortOper.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    adlbPortOper.setStatus("mandatory")


class _AdlbPortTemplateId_Type(Integer32):
    """Custom type adlbPortTemplateId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_AdlbPortTemplateId_Type.__name__ = "Integer32"
_AdlbPortTemplateId_Object = MibTableColumn
adlbPortTemplateId = _AdlbPortTemplateId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 3, 2, 1, 4),
    _AdlbPortTemplateId_Type()
)
adlbPortTemplateId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adlbPortTemplateId.setStatus("mandatory")
_AdlbPortTxCell_Type = Integer32
_AdlbPortTxCell_Object = MibTableColumn
adlbPortTxCell = _AdlbPortTxCell_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 3, 2, 1, 5),
    _AdlbPortTxCell_Type()
)
adlbPortTxCell.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbPortTxCell.setStatus("mandatory")
_AdlbPortRxCell_Type = Integer32
_AdlbPortRxCell_Object = MibTableColumn
adlbPortRxCell = _AdlbPortRxCell_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 3, 2, 1, 6),
    _AdlbPortRxCell_Type()
)
adlbPortRxCell.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbPortRxCell.setStatus("mandatory")
_HwMusaAdlbPortActTable_Object = MibTable
hwMusaAdlbPortActTable = _HwMusaAdlbPortActTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 3, 3)
)
if mibBuilder.loadTexts:
    hwMusaAdlbPortActTable.setStatus("mandatory")
_HwMusaAdlbPortActEntry_Object = MibTableRow
hwMusaAdlbPortActEntry = _HwMusaAdlbPortActEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 3, 3, 1)
)
hwMusaAdlbPortActEntry.setIndexNames(
    (0, "HUAWEI-MUSA-MA5100-CONFMIB", "adlbPortTemplateId"),
)
if mibBuilder.loadTexts:
    hwMusaAdlbPortActEntry.setStatus("mandatory")


class _AdlbIfConfigSetToDefault_Type(Integer32):
    """Custom type adlbIfConfigSetToDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("manual", 0))
    )


_AdlbIfConfigSetToDefault_Type.__name__ = "Integer32"
_AdlbIfConfigSetToDefault_Object = MibTableColumn
adlbIfConfigSetToDefault = _AdlbIfConfigSetToDefault_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 3, 3, 1, 1),
    _AdlbIfConfigSetToDefault_Type()
)
adlbIfConfigSetToDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adlbIfConfigSetToDefault.setStatus("mandatory")


class _AdlbServiceType_Type(Integer32):
    """Custom type adlbServiceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("all", 0),
          ("fullrate", 1),
          ("g9922", 4),
          ("ghs", 5),
          ("glite", 2),
          ("t1413", 3))
    )


_AdlbServiceType_Type.__name__ = "Integer32"
_AdlbServiceType_Object = MibTableColumn
adlbServiceType = _AdlbServiceType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 3, 3, 1, 2),
    _AdlbServiceType_Type()
)
adlbServiceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adlbServiceType.setStatus("mandatory")


class _AdlbConfigOrAutoDelay_Type(Integer32):
    """Custom type adlbConfigOrAutoDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("manual", 0))
    )


_AdlbConfigOrAutoDelay_Type.__name__ = "Integer32"
_AdlbConfigOrAutoDelay_Object = MibTableColumn
adlbConfigOrAutoDelay = _AdlbConfigOrAutoDelay_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 3, 3, 1, 3),
    _AdlbConfigOrAutoDelay_Type()
)
adlbConfigOrAutoDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adlbConfigOrAutoDelay.setStatus("mandatory")


class _AdlbDelayOrDepth_Type(Integer32):
    """Custom type adlbDelayOrDepth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("depth", 0),
          ("ms", 1))
    )


_AdlbDelayOrDepth_Type.__name__ = "Integer32"
_AdlbDelayOrDepth_Object = MibTableColumn
adlbDelayOrDepth = _AdlbDelayOrDepth_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 3, 3, 1, 4),
    _AdlbDelayOrDepth_Type()
)
adlbDelayOrDepth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adlbDelayOrDepth.setStatus("mandatory")


class _AdlbFrameMode_Type(Integer32):
    """Custom type adlbFrameMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mode0", 0),
          ("mode1", 1),
          ("mode2", 2),
          ("mode3", 3))
    )


_AdlbFrameMode_Type.__name__ = "Integer32"
_AdlbFrameMode_Object = MibTableColumn
adlbFrameMode = _AdlbFrameMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 3, 3, 1, 5),
    _AdlbFrameMode_Type()
)
adlbFrameMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adlbFrameMode.setStatus("mandatory")


class _AdlbNTROptionEnable_Type(Integer32):
    """Custom type adlbNTROptionEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AdlbNTROptionEnable_Type.__name__ = "Integer32"
_AdlbNTROptionEnable_Object = MibTableColumn
adlbNTROptionEnable = _AdlbNTROptionEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 3, 3, 1, 6),
    _AdlbNTROptionEnable_Type()
)
adlbNTROptionEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adlbNTROptionEnable.setStatus("mandatory")


class _AdlbTrellisModeEnable_Type(Integer32):
    """Custom type adlbTrellisModeEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AdlbTrellisModeEnable_Type.__name__ = "Integer32"
_AdlbTrellisModeEnable_Object = MibTableColumn
adlbTrellisModeEnable = _AdlbTrellisModeEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 3, 3, 1, 7),
    _AdlbTrellisModeEnable_Type()
)
adlbTrellisModeEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adlbTrellisModeEnable.setStatus("mandatory")


class _AdlbEocClearChannelMode_Type(Integer32):
    """Custom type adlbEocClearChannelMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("hdlcframing", 1),
          ("transparent", 0))
    )


_AdlbEocClearChannelMode_Type.__name__ = "Integer32"
_AdlbEocClearChannelMode_Object = MibTableColumn
adlbEocClearChannelMode = _AdlbEocClearChannelMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 3, 3, 1, 8),
    _AdlbEocClearChannelMode_Type()
)
adlbEocClearChannelMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adlbEocClearChannelMode.setStatus("mandatory")


class _AdlbDsSingleOrDual_Type(Integer32):
    """Custom type adlbDsSingleOrDual based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dual", 3),
          ("single", 1))
    )


_AdlbDsSingleOrDual_Type.__name__ = "Integer32"
_AdlbDsSingleOrDual_Object = MibTableColumn
adlbDsSingleOrDual = _AdlbDsSingleOrDual_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 3, 3, 1, 9),
    _AdlbDsSingleOrDual_Type()
)
adlbDsSingleOrDual.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adlbDsSingleOrDual.setStatus("mandatory")


class _AdlbUsSingleOrDual_Type(Integer32):
    """Custom type adlbUsSingleOrDual based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dual", 3),
          ("single", 1))
    )


_AdlbUsSingleOrDual_Type.__name__ = "Integer32"
_AdlbUsSingleOrDual_Object = MibTableColumn
adlbUsSingleOrDual = _AdlbUsSingleOrDual_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 3, 3, 1, 10),
    _AdlbUsSingleOrDual_Type()
)
adlbUsSingleOrDual.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adlbUsSingleOrDual.setStatus("mandatory")


class _AdlbFastOrInterleave_Type(Integer32):
    """Custom type adlbFastOrInterleave based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fast", 3),
          ("interleaved", 2))
    )


_AdlbFastOrInterleave_Type.__name__ = "Integer32"
_AdlbFastOrInterleave_Object = MibTableColumn
adlbFastOrInterleave = _AdlbFastOrInterleave_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 3, 3, 1, 11),
    _AdlbFastOrInterleave_Type()
)
adlbFastOrInterleave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adlbFastOrInterleave.setStatus("mandatory")


class _AdlbDsTargetMargin_Type(Integer32):
    """Custom type adlbDsTargetMargin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_AdlbDsTargetMargin_Type.__name__ = "Integer32"
_AdlbDsTargetMargin_Object = MibTableColumn
adlbDsTargetMargin = _AdlbDsTargetMargin_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 3, 3, 1, 13),
    _AdlbDsTargetMargin_Type()
)
adlbDsTargetMargin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adlbDsTargetMargin.setStatus("mandatory")
_AdlbDsMinMargin_Type = Integer32
_AdlbDsMinMargin_Object = MibTableColumn
adlbDsMinMargin = _AdlbDsMinMargin_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 3, 3, 1, 14),
    _AdlbDsMinMargin_Type()
)
adlbDsMinMargin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adlbDsMinMargin.setStatus("mandatory")


class _AdlbUsTargetMargin_Type(Integer32):
    """Custom type adlbUsTargetMargin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_AdlbUsTargetMargin_Type.__name__ = "Integer32"
_AdlbUsTargetMargin_Object = MibTableColumn
adlbUsTargetMargin = _AdlbUsTargetMargin_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 3, 3, 1, 15),
    _AdlbUsTargetMargin_Type()
)
adlbUsTargetMargin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adlbUsTargetMargin.setStatus("mandatory")
_AdlbUsMinMargin_Type = Integer32
_AdlbUsMinMargin_Object = MibTableColumn
adlbUsMinMargin = _AdlbUsMinMargin_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 3, 3, 1, 16),
    _AdlbUsMinMargin_Type()
)
adlbUsMinMargin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adlbUsMinMargin.setStatus("mandatory")
_AdlbMaxDsRateC0_Type = Integer32
_AdlbMaxDsRateC0_Object = MibTableColumn
adlbMaxDsRateC0 = _AdlbMaxDsRateC0_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 3, 3, 1, 17),
    _AdlbMaxDsRateC0_Type()
)
adlbMaxDsRateC0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adlbMaxDsRateC0.setStatus("mandatory")
_AdlbMinDsRateC0_Type = Integer32
_AdlbMinDsRateC0_Object = MibTableColumn
adlbMinDsRateC0 = _AdlbMinDsRateC0_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 3, 3, 1, 18),
    _AdlbMinDsRateC0_Type()
)
adlbMinDsRateC0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adlbMinDsRateC0.setStatus("mandatory")
_AdlbMaxUsRateC0_Type = Integer32
_AdlbMaxUsRateC0_Object = MibTableColumn
adlbMaxUsRateC0 = _AdlbMaxUsRateC0_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 3, 3, 1, 19),
    _AdlbMaxUsRateC0_Type()
)
adlbMaxUsRateC0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adlbMaxUsRateC0.setStatus("mandatory")
_AdlbMinUsRateC0_Type = Integer32
_AdlbMinUsRateC0_Object = MibTableColumn
adlbMinUsRateC0 = _AdlbMinUsRateC0_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 3, 3, 1, 20),
    _AdlbMinUsRateC0_Type()
)
adlbMinUsRateC0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adlbMinUsRateC0.setStatus("mandatory")
_AdlbUsMsOrDmtNumber_Type = Integer32
_AdlbUsMsOrDmtNumber_Object = MibTableColumn
adlbUsMsOrDmtNumber = _AdlbUsMsOrDmtNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 3, 3, 1, 21),
    _AdlbUsMsOrDmtNumber_Type()
)
adlbUsMsOrDmtNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adlbUsMsOrDmtNumber.setStatus("mandatory")
_AdlbDsMsOrDmtNumber_Type = Integer32
_AdlbDsMsOrDmtNumber_Object = MibTableColumn
adlbDsMsOrDmtNumber = _AdlbDsMsOrDmtNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 3, 3, 1, 22),
    _AdlbDsMsOrDmtNumber_Type()
)
adlbDsMsOrDmtNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adlbDsMsOrDmtNumber.setStatus("mandatory")
_AdlbUsExcessRatio_Type = Integer32
_AdlbUsExcessRatio_Object = MibTableColumn
adlbUsExcessRatio = _AdlbUsExcessRatio_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 3, 3, 1, 23),
    _AdlbUsExcessRatio_Type()
)
adlbUsExcessRatio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adlbUsExcessRatio.setStatus("mandatory")
_AdlbDsExcessRatio_Type = Integer32
_AdlbDsExcessRatio_Object = MibTableColumn
adlbDsExcessRatio = _AdlbDsExcessRatio_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 3, 3, 1, 24),
    _AdlbDsExcessRatio_Type()
)
adlbDsExcessRatio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adlbDsExcessRatio.setStatus("mandatory")
_AdlbMaxDsRateC1_Type = Integer32
_AdlbMaxDsRateC1_Object = MibTableColumn
adlbMaxDsRateC1 = _AdlbMaxDsRateC1_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 3, 3, 1, 25),
    _AdlbMaxDsRateC1_Type()
)
adlbMaxDsRateC1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adlbMaxDsRateC1.setStatus("mandatory")
_AdlbMinDsRateC1_Type = Integer32
_AdlbMinDsRateC1_Object = MibTableColumn
adlbMinDsRateC1 = _AdlbMinDsRateC1_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 3, 3, 1, 26),
    _AdlbMinDsRateC1_Type()
)
adlbMinDsRateC1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adlbMinDsRateC1.setStatus("mandatory")
_AdlbMaxUsRateC1_Type = Integer32
_AdlbMaxUsRateC1_Object = MibTableColumn
adlbMaxUsRateC1 = _AdlbMaxUsRateC1_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 3, 3, 1, 27),
    _AdlbMaxUsRateC1_Type()
)
adlbMaxUsRateC1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adlbMaxUsRateC1.setStatus("mandatory")
_AdlbMinUsRateC1_Type = Integer32
_AdlbMinUsRateC1_Object = MibTableColumn
adlbMinUsRateC1 = _AdlbMinUsRateC1_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 3, 3, 1, 28),
    _AdlbMinUsRateC1_Type()
)
adlbMinUsRateC1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adlbMinUsRateC1.setStatus("mandatory")


class _AdlbTemplateOperate_Type(Integer32):
    """Custom type adlbTemplateOperate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("add", 0),
          ("del", 1))
    )


_AdlbTemplateOperate_Type.__name__ = "Integer32"
_AdlbTemplateOperate_Object = MibTableColumn
adlbTemplateOperate = _AdlbTemplateOperate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 3, 3, 1, 29),
    _AdlbTemplateOperate_Type()
)
adlbTemplateOperate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adlbTemplateOperate.setStatus("mandatory")
_HwMusaAdlbPortPfmThresTable_Object = MibTable
hwMusaAdlbPortPfmThresTable = _HwMusaAdlbPortPfmThresTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 3, 4)
)
if mibBuilder.loadTexts:
    hwMusaAdlbPortPfmThresTable.setStatus("mandatory")
_HwMusaAdlbPortPfmThresEntry_Object = MibTableRow
hwMusaAdlbPortPfmThresEntry = _HwMusaAdlbPortPfmThresEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 3, 4, 1)
)
hwMusaAdlbPortPfmThresEntry.setIndexNames(
    (0, "HUAWEI-MUSA-MA5100-CONFMIB", "hwMusaFrameIndex"),
    (0, "HUAWEI-MUSA-MA5100-CONFMIB", "hwMusaSlotIndex"),
    (0, "HUAWEI-MUSA-MA5100-CONFMIB", "adlbPortIndex"),
)
if mibBuilder.loadTexts:
    hwMusaAdlbPortPfmThresEntry.setStatus("mandatory")


class _AdlbPortPfmThresId1_Type(Integer32):
    """Custom type adlbPortPfmThresId1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_AdlbPortPfmThresId1_Type.__name__ = "Integer32"
_AdlbPortPfmThresId1_Object = MibTableColumn
adlbPortPfmThresId1 = _AdlbPortPfmThresId1_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 3, 4, 1, 1),
    _AdlbPortPfmThresId1_Type()
)
adlbPortPfmThresId1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adlbPortPfmThresId1.setStatus("mandatory")
_AdlbPortPfmThresValue1_Type = Integer32
_AdlbPortPfmThresValue1_Object = MibTableColumn
adlbPortPfmThresValue1 = _AdlbPortPfmThresValue1_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 3, 4, 1, 2),
    _AdlbPortPfmThresValue1_Type()
)
adlbPortPfmThresValue1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adlbPortPfmThresValue1.setStatus("mandatory")


class _AdlbPortPfmThresId2_Type(Integer32):
    """Custom type adlbPortPfmThresId2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_AdlbPortPfmThresId2_Type.__name__ = "Integer32"
_AdlbPortPfmThresId2_Object = MibTableColumn
adlbPortPfmThresId2 = _AdlbPortPfmThresId2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 3, 4, 1, 3),
    _AdlbPortPfmThresId2_Type()
)
adlbPortPfmThresId2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adlbPortPfmThresId2.setStatus("mandatory")
_AdlbPortPfmThresValue2_Type = Integer32
_AdlbPortPfmThresValue2_Object = MibTableColumn
adlbPortPfmThresValue2 = _AdlbPortPfmThresValue2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 3, 4, 1, 4),
    _AdlbPortPfmThresValue2_Type()
)
adlbPortPfmThresValue2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adlbPortPfmThresValue2.setStatus("mandatory")


class _AdlbPortPfmThresId3_Type(Integer32):
    """Custom type adlbPortPfmThresId3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_AdlbPortPfmThresId3_Type.__name__ = "Integer32"
_AdlbPortPfmThresId3_Object = MibTableColumn
adlbPortPfmThresId3 = _AdlbPortPfmThresId3_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 3, 4, 1, 5),
    _AdlbPortPfmThresId3_Type()
)
adlbPortPfmThresId3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adlbPortPfmThresId3.setStatus("mandatory")
_AdlbPortPfmThresValue3_Type = Integer32
_AdlbPortPfmThresValue3_Object = MibTableColumn
adlbPortPfmThresValue3 = _AdlbPortPfmThresValue3_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 3, 4, 1, 6),
    _AdlbPortPfmThresValue3_Type()
)
adlbPortPfmThresValue3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adlbPortPfmThresValue3.setStatus("mandatory")


class _AdlbPortPfmThresId4_Type(Integer32):
    """Custom type adlbPortPfmThresId4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_AdlbPortPfmThresId4_Type.__name__ = "Integer32"
_AdlbPortPfmThresId4_Object = MibTableColumn
adlbPortPfmThresId4 = _AdlbPortPfmThresId4_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 3, 4, 1, 7),
    _AdlbPortPfmThresId4_Type()
)
adlbPortPfmThresId4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adlbPortPfmThresId4.setStatus("mandatory")
_AdlbPortPfmThresValue4_Type = Integer32
_AdlbPortPfmThresValue4_Object = MibTableColumn
adlbPortPfmThresValue4 = _AdlbPortPfmThresValue4_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 3, 4, 1, 8),
    _AdlbPortPfmThresValue4_Type()
)
adlbPortPfmThresValue4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adlbPortPfmThresValue4.setStatus("mandatory")


class _AdlbPortPfmThresId5_Type(Integer32):
    """Custom type adlbPortPfmThresId5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_AdlbPortPfmThresId5_Type.__name__ = "Integer32"
_AdlbPortPfmThresId5_Object = MibTableColumn
adlbPortPfmThresId5 = _AdlbPortPfmThresId5_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 3, 4, 1, 9),
    _AdlbPortPfmThresId5_Type()
)
adlbPortPfmThresId5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adlbPortPfmThresId5.setStatus("mandatory")
_AdlbPortPfmThresValue5_Type = Integer32
_AdlbPortPfmThresValue5_Object = MibTableColumn
adlbPortPfmThresValue5 = _AdlbPortPfmThresValue5_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 3, 4, 1, 10),
    _AdlbPortPfmThresValue5_Type()
)
adlbPortPfmThresValue5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adlbPortPfmThresValue5.setStatus("mandatory")


class _AdlbPortPfmThresId6_Type(Integer32):
    """Custom type adlbPortPfmThresId6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_AdlbPortPfmThresId6_Type.__name__ = "Integer32"
_AdlbPortPfmThresId6_Object = MibTableColumn
adlbPortPfmThresId6 = _AdlbPortPfmThresId6_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 3, 4, 1, 11),
    _AdlbPortPfmThresId6_Type()
)
adlbPortPfmThresId6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adlbPortPfmThresId6.setStatus("mandatory")
_AdlbPortPfmThresValue6_Type = Integer32
_AdlbPortPfmThresValue6_Object = MibTableColumn
adlbPortPfmThresValue6 = _AdlbPortPfmThresValue6_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 3, 4, 1, 12),
    _AdlbPortPfmThresValue6_Type()
)
adlbPortPfmThresValue6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adlbPortPfmThresValue6.setStatus("mandatory")


class _AdlbPortPfmThresId7_Type(Integer32):
    """Custom type adlbPortPfmThresId7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_AdlbPortPfmThresId7_Type.__name__ = "Integer32"
_AdlbPortPfmThresId7_Object = MibTableColumn
adlbPortPfmThresId7 = _AdlbPortPfmThresId7_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 3, 4, 1, 13),
    _AdlbPortPfmThresId7_Type()
)
adlbPortPfmThresId7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adlbPortPfmThresId7.setStatus("mandatory")
_AdlbPortPfmThresValue7_Type = Integer32
_AdlbPortPfmThresValue7_Object = MibTableColumn
adlbPortPfmThresValue7 = _AdlbPortPfmThresValue7_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 3, 4, 1, 14),
    _AdlbPortPfmThresValue7_Type()
)
adlbPortPfmThresValue7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adlbPortPfmThresValue7.setStatus("mandatory")


class _AdlbPortPfmThresId8_Type(Integer32):
    """Custom type adlbPortPfmThresId8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_AdlbPortPfmThresId8_Type.__name__ = "Integer32"
_AdlbPortPfmThresId8_Object = MibTableColumn
adlbPortPfmThresId8 = _AdlbPortPfmThresId8_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 3, 4, 1, 15),
    _AdlbPortPfmThresId8_Type()
)
adlbPortPfmThresId8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adlbPortPfmThresId8.setStatus("mandatory")
_AdlbPortPfmThresValue8_Type = Integer32
_AdlbPortPfmThresValue8_Object = MibTableColumn
adlbPortPfmThresValue8 = _AdlbPortPfmThresValue8_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 3, 4, 1, 16),
    _AdlbPortPfmThresValue8_Type()
)
adlbPortPfmThresValue8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adlbPortPfmThresValue8.setStatus("mandatory")
_HwMusaAdlbPfm_ObjectIdentity = ObjectIdentity
hwMusaAdlbPfm = _HwMusaAdlbPfm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4)
)
_HwMusaAdlbPortLineDataTable_Object = MibTable
hwMusaAdlbPortLineDataTable = _HwMusaAdlbPortLineDataTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 1)
)
if mibBuilder.loadTexts:
    hwMusaAdlbPortLineDataTable.setStatus("mandatory")
_HwMusaAdlbPortLineDataEntry_Object = MibTableRow
hwMusaAdlbPortLineDataEntry = _HwMusaAdlbPortLineDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 1, 1)
)
hwMusaAdlbPortLineDataEntry.setIndexNames(
    (0, "HUAWEI-MUSA-MA5100-CONFMIB", "hwMusaFrameIndex"),
    (0, "HUAWEI-MUSA-MA5100-CONFMIB", "hwMusaSlotIndex"),
    (0, "HUAWEI-MUSA-MA5100-CONFMIB", "adlbPortIndex"),
)
if mibBuilder.loadTexts:
    hwMusaAdlbPortLineDataEntry.setStatus("mandatory")
_AdlbAs0DnRate_Type = Integer32
_AdlbAs0DnRate_Object = MibTableColumn
adlbAs0DnRate = _AdlbAs0DnRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 1, 1, 1),
    _AdlbAs0DnRate_Type()
)
adlbAs0DnRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAs0DnRate.setStatus("mandatory")
_AdlbLs0DnRate_Type = Integer32
_AdlbLs0DnRate_Object = MibTableColumn
adlbLs0DnRate = _AdlbLs0DnRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 1, 1, 2),
    _AdlbLs0DnRate_Type()
)
adlbLs0DnRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbLs0DnRate.setStatus("mandatory")
_AdlbAs1DnRate_Type = Integer32
_AdlbAs1DnRate_Object = MibTableColumn
adlbAs1DnRate = _AdlbAs1DnRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 1, 1, 3),
    _AdlbAs1DnRate_Type()
)
adlbAs1DnRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAs1DnRate.setStatus("mandatory")
_AdlbLs0UpRate_Type = Integer32
_AdlbLs0UpRate_Object = MibTableColumn
adlbLs0UpRate = _AdlbLs0UpRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 1, 1, 4),
    _AdlbLs0UpRate_Type()
)
adlbLs0UpRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbLs0UpRate.setStatus("mandatory")
_AdlbLs1UpRate_Type = Integer32
_AdlbLs1UpRate_Object = MibTableColumn
adlbLs1UpRate = _AdlbLs1UpRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 1, 1, 5),
    _AdlbLs1UpRate_Type()
)
adlbLs1UpRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbLs1UpRate.setStatus("mandatory")
_AdlbUpInterleaveDelay_Type = Integer32
_AdlbUpInterleaveDelay_Object = MibTableColumn
adlbUpInterleaveDelay = _AdlbUpInterleaveDelay_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 1, 1, 6),
    _AdlbUpInterleaveDelay_Type()
)
adlbUpInterleaveDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbUpInterleaveDelay.setStatus("mandatory")
_AdlbDnInterleaveDelay_Type = Integer32
_AdlbDnInterleaveDelay_Object = MibTableColumn
adlbDnInterleaveDelay = _AdlbDnInterleaveDelay_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 1, 1, 7),
    _AdlbDnInterleaveDelay_Type()
)
adlbDnInterleaveDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbDnInterleaveDelay.setStatus("mandatory")
_AdlbDnNoiseMargin_Type = Integer32
_AdlbDnNoiseMargin_Object = MibTableColumn
adlbDnNoiseMargin = _AdlbDnNoiseMargin_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 1, 1, 8),
    _AdlbDnNoiseMargin_Type()
)
adlbDnNoiseMargin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbDnNoiseMargin.setStatus("mandatory")
_AdlbUpNoiseMargin_Type = Integer32
_AdlbUpNoiseMargin_Object = MibTableColumn
adlbUpNoiseMargin = _AdlbUpNoiseMargin_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 1, 1, 9),
    _AdlbUpNoiseMargin_Type()
)
adlbUpNoiseMargin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbUpNoiseMargin.setStatus("mandatory")
_AdlbDnAttenuation_Type = Integer32
_AdlbDnAttenuation_Object = MibTableColumn
adlbDnAttenuation = _AdlbDnAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 1, 1, 10),
    _AdlbDnAttenuation_Type()
)
adlbDnAttenuation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbDnAttenuation.setStatus("mandatory")
_AdlbUpAttenuation_Type = Integer32
_AdlbUpAttenuation_Object = MibTableColumn
adlbUpAttenuation = _AdlbUpAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 1, 1, 11),
    _AdlbUpAttenuation_Type()
)
adlbUpAttenuation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbUpAttenuation.setStatus("mandatory")
_AdlbDnParityInterleave_Type = Integer32
_AdlbDnParityInterleave_Object = MibTableColumn
adlbDnParityInterleave = _AdlbDnParityInterleave_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 1, 1, 12),
    _AdlbDnParityInterleave_Type()
)
adlbDnParityInterleave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbDnParityInterleave.setStatus("mandatory")
_AdlbDnParityFast_Type = Integer32
_AdlbDnParityFast_Object = MibTableColumn
adlbDnParityFast = _AdlbDnParityFast_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 1, 1, 13),
    _AdlbDnParityFast_Type()
)
adlbDnParityFast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbDnParityFast.setStatus("mandatory")
_AdlbUpParityInterleave_Type = Integer32
_AdlbUpParityInterleave_Object = MibTableColumn
adlbUpParityInterleave = _AdlbUpParityInterleave_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 1, 1, 14),
    _AdlbUpParityInterleave_Type()
)
adlbUpParityInterleave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbUpParityInterleave.setStatus("mandatory")
_AdlbUpParityFast_Type = Integer32
_AdlbUpParityFast_Object = MibTableColumn
adlbUpParityFast = _AdlbUpParityFast_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 1, 1, 15),
    _AdlbUpParityFast_Type()
)
adlbUpParityFast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbUpParityFast.setStatus("mandatory")
_AdlbDnSymbolPerCodeInterleave_Type = Integer32
_AdlbDnSymbolPerCodeInterleave_Object = MibTableColumn
adlbDnSymbolPerCodeInterleave = _AdlbDnSymbolPerCodeInterleave_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 1, 1, 16),
    _AdlbDnSymbolPerCodeInterleave_Type()
)
adlbDnSymbolPerCodeInterleave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbDnSymbolPerCodeInterleave.setStatus("mandatory")
_AdlbDnSymbolPerCodeFast_Type = Integer32
_AdlbDnSymbolPerCodeFast_Object = MibTableColumn
adlbDnSymbolPerCodeFast = _AdlbDnSymbolPerCodeFast_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 1, 1, 17),
    _AdlbDnSymbolPerCodeFast_Type()
)
adlbDnSymbolPerCodeFast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbDnSymbolPerCodeFast.setStatus("mandatory")
_AdlbUpSymbolPerCodeInterleave_Type = Integer32
_AdlbUpSymbolPerCodeInterleave_Object = MibTableColumn
adlbUpSymbolPerCodeInterleave = _AdlbUpSymbolPerCodeInterleave_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 1, 1, 18),
    _AdlbUpSymbolPerCodeInterleave_Type()
)
adlbUpSymbolPerCodeInterleave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbUpSymbolPerCodeInterleave.setStatus("mandatory")
_AdlbUpSymbolPerCodeFast_Type = Integer32
_AdlbUpSymbolPerCodeFast_Object = MibTableColumn
adlbUpSymbolPerCodeFast = _AdlbUpSymbolPerCodeFast_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 1, 1, 19),
    _AdlbUpSymbolPerCodeFast_Type()
)
adlbUpSymbolPerCodeFast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbUpSymbolPerCodeFast.setStatus("mandatory")
_AdlbDnInterleaveDepth_Type = Integer32
_AdlbDnInterleaveDepth_Object = MibTableColumn
adlbDnInterleaveDepth = _AdlbDnInterleaveDepth_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 1, 1, 20),
    _AdlbDnInterleaveDepth_Type()
)
adlbDnInterleaveDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbDnInterleaveDepth.setStatus("mandatory")
_AdlbUpInterleaveDepth_Type = Integer32
_AdlbUpInterleaveDepth_Object = MibTableColumn
adlbUpInterleaveDepth = _AdlbUpInterleaveDepth_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 1, 1, 21),
    _AdlbUpInterleaveDepth_Type()
)
adlbUpInterleaveDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbUpInterleaveDepth.setStatus("mandatory")
_AdlbMaxDnAttainableRate_Type = Integer32
_AdlbMaxDnAttainableRate_Object = MibTableColumn
adlbMaxDnAttainableRate = _AdlbMaxDnAttainableRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 1, 1, 22),
    _AdlbMaxDnAttainableRate_Type()
)
adlbMaxDnAttainableRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbMaxDnAttainableRate.setStatus("mandatory")
_AdlbMaxUpAttainableRate_Type = Integer32
_AdlbMaxUpAttainableRate_Object = MibTableColumn
adlbMaxUpAttainableRate = _AdlbMaxUpAttainableRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 1, 1, 23),
    _AdlbMaxUpAttainableRate_Type()
)
adlbMaxUpAttainableRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbMaxUpAttainableRate.setStatus("mandatory")
_AdlbTotalOutputPower_Type = Integer32
_AdlbTotalOutputPower_Object = MibTableColumn
adlbTotalOutputPower = _AdlbTotalOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 1, 1, 24),
    _AdlbTotalOutputPower_Type()
)
adlbTotalOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbTotalOutputPower.setStatus("mandatory")
_HwMusaAdlbAtucAlarmDataTable_Object = MibTable
hwMusaAdlbAtucAlarmDataTable = _HwMusaAdlbAtucAlarmDataTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 2)
)
if mibBuilder.loadTexts:
    hwMusaAdlbAtucAlarmDataTable.setStatus("mandatory")
_HwMusaAdlbAtucAlarmDataEntry_Object = MibTableRow
hwMusaAdlbAtucAlarmDataEntry = _HwMusaAdlbAtucAlarmDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 2, 1)
)
hwMusaAdlbAtucAlarmDataEntry.setIndexNames(
    (0, "HUAWEI-MUSA-MA5100-CONFMIB", "hwMusaFrameIndex"),
    (0, "HUAWEI-MUSA-MA5100-CONFMIB", "hwMusaSlotIndex"),
    (0, "HUAWEI-MUSA-MA5100-CONFMIB", "adlbPortIndex"),
)
if mibBuilder.loadTexts:
    hwMusaAdlbAtucAlarmDataEntry.setStatus("mandatory")
_AdlbAtucLos_Type = Integer32
_AdlbAtucLos_Object = MibTableColumn
adlbAtucLos = _AdlbAtucLos_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 2, 1, 1),
    _AdlbAtucLos_Type()
)
adlbAtucLos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAtucLos.setStatus("mandatory")
_AdlbAtucHighBitErr_Type = Integer32
_AdlbAtucHighBitErr_Object = MibTableColumn
adlbAtucHighBitErr = _AdlbAtucHighBitErr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 2, 1, 2),
    _AdlbAtucHighBitErr_Type()
)
adlbAtucHighBitErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAtucHighBitErr.setStatus("mandatory")
_AdlbAtucRetrain_Type = Integer32
_AdlbAtucRetrain_Object = MibTableColumn
adlbAtucRetrain = _AdlbAtucRetrain_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 2, 1, 3),
    _AdlbAtucRetrain_Type()
)
adlbAtucRetrain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAtucRetrain.setStatus("mandatory")
_AdlbAtucLof_Type = Integer32
_AdlbAtucLof_Object = MibTableColumn
adlbAtucLof = _AdlbAtucLof_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 2, 1, 4),
    _AdlbAtucLof_Type()
)
adlbAtucLof.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAtucLof.setStatus("mandatory")
_AdlbAtucAlarmValidIntervals_Type = Integer32
_AdlbAtucAlarmValidIntervals_Object = MibTableColumn
adlbAtucAlarmValidIntervals = _AdlbAtucAlarmValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 2, 1, 5),
    _AdlbAtucAlarmValidIntervals_Type()
)
adlbAtucAlarmValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAtucAlarmValidIntervals.setStatus("mandatory")
_AdlbAtucPrev15MinLos_Type = Integer32
_AdlbAtucPrev15MinLos_Object = MibTableColumn
adlbAtucPrev15MinLos = _AdlbAtucPrev15MinLos_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 2, 1, 6),
    _AdlbAtucPrev15MinLos_Type()
)
adlbAtucPrev15MinLos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAtucPrev15MinLos.setStatus("mandatory")
_AdlbAtucPrev15MinHighBitErr_Type = Integer32
_AdlbAtucPrev15MinHighBitErr_Object = MibTableColumn
adlbAtucPrev15MinHighBitErr = _AdlbAtucPrev15MinHighBitErr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 2, 1, 7),
    _AdlbAtucPrev15MinHighBitErr_Type()
)
adlbAtucPrev15MinHighBitErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAtucPrev15MinHighBitErr.setStatus("mandatory")
_AdlbAtucPrev15MinRetrain_Type = Integer32
_AdlbAtucPrev15MinRetrain_Object = MibTableColumn
adlbAtucPrev15MinRetrain = _AdlbAtucPrev15MinRetrain_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 2, 1, 8),
    _AdlbAtucPrev15MinRetrain_Type()
)
adlbAtucPrev15MinRetrain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAtucPrev15MinRetrain.setStatus("mandatory")
_AdlbAtucPrev15MinLof_Type = Integer32
_AdlbAtucPrev15MinLof_Object = MibTableColumn
adlbAtucPrev15MinLof = _AdlbAtucPrev15MinLof_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 2, 1, 9),
    _AdlbAtucPrev15MinLof_Type()
)
adlbAtucPrev15MinLof.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAtucPrev15MinLof.setStatus("mandatory")
_AdlbAtucCurr1DayLos_Type = Integer32
_AdlbAtucCurr1DayLos_Object = MibTableColumn
adlbAtucCurr1DayLos = _AdlbAtucCurr1DayLos_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 2, 1, 10),
    _AdlbAtucCurr1DayLos_Type()
)
adlbAtucCurr1DayLos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAtucCurr1DayLos.setStatus("mandatory")
_AdlbAtucCurr1DayHighBitErr_Type = Integer32
_AdlbAtucCurr1DayHighBitErr_Object = MibTableColumn
adlbAtucCurr1DayHighBitErr = _AdlbAtucCurr1DayHighBitErr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 2, 1, 11),
    _AdlbAtucCurr1DayHighBitErr_Type()
)
adlbAtucCurr1DayHighBitErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAtucCurr1DayHighBitErr.setStatus("mandatory")
_AdlbAtucCurr1DayRetrain_Type = Integer32
_AdlbAtucCurr1DayRetrain_Object = MibTableColumn
adlbAtucCurr1DayRetrain = _AdlbAtucCurr1DayRetrain_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 2, 1, 12),
    _AdlbAtucCurr1DayRetrain_Type()
)
adlbAtucCurr1DayRetrain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAtucCurr1DayRetrain.setStatus("mandatory")
_AdlbAtucCurr1DayLof_Type = Integer32
_AdlbAtucCurr1DayLof_Object = MibTableColumn
adlbAtucCurr1DayLof = _AdlbAtucCurr1DayLof_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 2, 1, 13),
    _AdlbAtucCurr1DayLof_Type()
)
adlbAtucCurr1DayLof.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAtucCurr1DayLof.setStatus("mandatory")
_AdlbAtucPrev1DayLos_Type = Integer32
_AdlbAtucPrev1DayLos_Object = MibTableColumn
adlbAtucPrev1DayLos = _AdlbAtucPrev1DayLos_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 2, 1, 14),
    _AdlbAtucPrev1DayLos_Type()
)
adlbAtucPrev1DayLos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAtucPrev1DayLos.setStatus("mandatory")
_AdlbAtucPrev1DayHighBitErr_Type = Integer32
_AdlbAtucPrev1DayHighBitErr_Object = MibTableColumn
adlbAtucPrev1DayHighBitErr = _AdlbAtucPrev1DayHighBitErr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 2, 1, 15),
    _AdlbAtucPrev1DayHighBitErr_Type()
)
adlbAtucPrev1DayHighBitErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAtucPrev1DayHighBitErr.setStatus("mandatory")
_AdlbAtucPrev1DayRetrain_Type = Integer32
_AdlbAtucPrev1DayRetrain_Object = MibTableColumn
adlbAtucPrev1DayRetrain = _AdlbAtucPrev1DayRetrain_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 2, 1, 16),
    _AdlbAtucPrev1DayRetrain_Type()
)
adlbAtucPrev1DayRetrain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAtucPrev1DayRetrain.setStatus("mandatory")
_AdlbAtucPrev1DayLof_Type = Integer32
_AdlbAtucPrev1DayLof_Object = MibTableColumn
adlbAtucPrev1DayLof = _AdlbAtucPrev1DayLof_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 2, 1, 17),
    _AdlbAtucPrev1DayLof_Type()
)
adlbAtucPrev1DayLof.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAtucPrev1DayLof.setStatus("mandatory")
_AdlbClearAlarmstatistics_Type = Integer32
_AdlbClearAlarmstatistics_Object = MibTableColumn
adlbClearAlarmstatistics = _AdlbClearAlarmstatistics_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 2, 1, 18),
    _AdlbClearAlarmstatistics_Type()
)
adlbClearAlarmstatistics.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    adlbClearAlarmstatistics.setStatus("mandatory")
_HwMusaAdlbAturAlarmDataTable_Object = MibTable
hwMusaAdlbAturAlarmDataTable = _HwMusaAdlbAturAlarmDataTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 3)
)
if mibBuilder.loadTexts:
    hwMusaAdlbAturAlarmDataTable.setStatus("mandatory")
_HwMusaAdlbAturAlarmDataEntry_Object = MibTableRow
hwMusaAdlbAturAlarmDataEntry = _HwMusaAdlbAturAlarmDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 3, 1)
)
hwMusaAdlbAturAlarmDataEntry.setIndexNames(
    (0, "HUAWEI-MUSA-MA5100-CONFMIB", "hwMusaFrameIndex"),
    (0, "HUAWEI-MUSA-MA5100-CONFMIB", "hwMusaSlotIndex"),
    (0, "HUAWEI-MUSA-MA5100-CONFMIB", "adlbPortIndex"),
)
if mibBuilder.loadTexts:
    hwMusaAdlbAturAlarmDataEntry.setStatus("mandatory")
_AdlbAturLos_Type = Integer32
_AdlbAturLos_Object = MibTableColumn
adlbAturLos = _AdlbAturLos_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 3, 1, 1),
    _AdlbAturLos_Type()
)
adlbAturLos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAturLos.setStatus("mandatory")
_AdlbAturHighBitErr_Type = Integer32
_AdlbAturHighBitErr_Object = MibTableColumn
adlbAturHighBitErr = _AdlbAturHighBitErr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 3, 1, 2),
    _AdlbAturHighBitErr_Type()
)
adlbAturHighBitErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAturHighBitErr.setStatus("mandatory")
_AdlbAturRfi_Type = Integer32
_AdlbAturRfi_Object = MibTableColumn
adlbAturRfi = _AdlbAturRfi_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 3, 1, 3),
    _AdlbAturRfi_Type()
)
adlbAturRfi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAturRfi.setStatus("mandatory")
_AdlbAturLpr_Type = Integer32
_AdlbAturLpr_Object = MibTableColumn
adlbAturLpr = _AdlbAturLpr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 3, 1, 4),
    _AdlbAturLpr_Type()
)
adlbAturLpr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAturLpr.setStatus("mandatory")
_AdlbAturAlarmValidIntervals_Type = Integer32
_AdlbAturAlarmValidIntervals_Object = MibTableColumn
adlbAturAlarmValidIntervals = _AdlbAturAlarmValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 3, 1, 5),
    _AdlbAturAlarmValidIntervals_Type()
)
adlbAturAlarmValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAturAlarmValidIntervals.setStatus("mandatory")
_AdlbAturPrev15MinLos_Type = Integer32
_AdlbAturPrev15MinLos_Object = MibTableColumn
adlbAturPrev15MinLos = _AdlbAturPrev15MinLos_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 3, 1, 6),
    _AdlbAturPrev15MinLos_Type()
)
adlbAturPrev15MinLos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAturPrev15MinLos.setStatus("mandatory")
_AdlbAturPrev15MinHighBitErr_Type = Integer32
_AdlbAturPrev15MinHighBitErr_Object = MibTableColumn
adlbAturPrev15MinHighBitErr = _AdlbAturPrev15MinHighBitErr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 3, 1, 7),
    _AdlbAturPrev15MinHighBitErr_Type()
)
adlbAturPrev15MinHighBitErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAturPrev15MinHighBitErr.setStatus("mandatory")
_AdlbAturPrev15MinRfi_Type = Integer32
_AdlbAturPrev15MinRfi_Object = MibTableColumn
adlbAturPrev15MinRfi = _AdlbAturPrev15MinRfi_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 3, 1, 8),
    _AdlbAturPrev15MinRfi_Type()
)
adlbAturPrev15MinRfi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAturPrev15MinRfi.setStatus("mandatory")
_AdlbAturPrev15MinLpr_Type = Integer32
_AdlbAturPrev15MinLpr_Object = MibTableColumn
adlbAturPrev15MinLpr = _AdlbAturPrev15MinLpr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 3, 1, 9),
    _AdlbAturPrev15MinLpr_Type()
)
adlbAturPrev15MinLpr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAturPrev15MinLpr.setStatus("mandatory")
_AdlbAturCurr1DayLos_Type = Integer32
_AdlbAturCurr1DayLos_Object = MibTableColumn
adlbAturCurr1DayLos = _AdlbAturCurr1DayLos_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 3, 1, 10),
    _AdlbAturCurr1DayLos_Type()
)
adlbAturCurr1DayLos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAturCurr1DayLos.setStatus("mandatory")
_AdlbAturCurr1DayHighBitErr_Type = Integer32
_AdlbAturCurr1DayHighBitErr_Object = MibTableColumn
adlbAturCurr1DayHighBitErr = _AdlbAturCurr1DayHighBitErr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 3, 1, 11),
    _AdlbAturCurr1DayHighBitErr_Type()
)
adlbAturCurr1DayHighBitErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAturCurr1DayHighBitErr.setStatus("mandatory")
_AdlbAturCurr1DayRfi_Type = Integer32
_AdlbAturCurr1DayRfi_Object = MibTableColumn
adlbAturCurr1DayRfi = _AdlbAturCurr1DayRfi_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 3, 1, 12),
    _AdlbAturCurr1DayRfi_Type()
)
adlbAturCurr1DayRfi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAturCurr1DayRfi.setStatus("mandatory")
_AdlbAturCurr1DayLpr_Type = Integer32
_AdlbAturCurr1DayLpr_Object = MibTableColumn
adlbAturCurr1DayLpr = _AdlbAturCurr1DayLpr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 3, 1, 13),
    _AdlbAturCurr1DayLpr_Type()
)
adlbAturCurr1DayLpr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAturCurr1DayLpr.setStatus("mandatory")
_AdlbAturPrev1DayLos_Type = Integer32
_AdlbAturPrev1DayLos_Object = MibTableColumn
adlbAturPrev1DayLos = _AdlbAturPrev1DayLos_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 3, 1, 14),
    _AdlbAturPrev1DayLos_Type()
)
adlbAturPrev1DayLos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAturPrev1DayLos.setStatus("mandatory")
_AdlbAturPrev1DayHighBitErr_Type = Integer32
_AdlbAturPrev1DayHighBitErr_Object = MibTableColumn
adlbAturPrev1DayHighBitErr = _AdlbAturPrev1DayHighBitErr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 3, 1, 15),
    _AdlbAturPrev1DayHighBitErr_Type()
)
adlbAturPrev1DayHighBitErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAturPrev1DayHighBitErr.setStatus("mandatory")
_AdlbAturPrev1DayRfi_Type = Integer32
_AdlbAturPrev1DayRfi_Object = MibTableColumn
adlbAturPrev1DayRfi = _AdlbAturPrev1DayRfi_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 3, 1, 16),
    _AdlbAturPrev1DayRfi_Type()
)
adlbAturPrev1DayRfi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAturPrev1DayRfi.setStatus("mandatory")
_AdlbAturPrev1DayLpr_Type = Integer32
_AdlbAturPrev1DayLpr_Object = MibTableColumn
adlbAturPrev1DayLpr = _AdlbAturPrev1DayLpr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 3, 1, 17),
    _AdlbAturPrev1DayLpr_Type()
)
adlbAturPrev1DayLpr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAturPrev1DayLpr.setStatus("mandatory")
_HwMusaAdlbAtucPerfDataTable_Object = MibTable
hwMusaAdlbAtucPerfDataTable = _HwMusaAdlbAtucPerfDataTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 4)
)
if mibBuilder.loadTexts:
    hwMusaAdlbAtucPerfDataTable.setStatus("mandatory")
_HwMusaAdlbAtucPerfDataEntry_Object = MibTableRow
hwMusaAdlbAtucPerfDataEntry = _HwMusaAdlbAtucPerfDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 4, 1)
)
hwMusaAdlbAtucPerfDataEntry.setIndexNames(
    (0, "HUAWEI-MUSA-MA5100-CONFMIB", "hwMusaFrameIndex"),
    (0, "HUAWEI-MUSA-MA5100-CONFMIB", "hwMusaSlotIndex"),
    (0, "HUAWEI-MUSA-MA5100-CONFMIB", "adlbPortIndex"),
)
if mibBuilder.loadTexts:
    hwMusaAdlbAtucPerfDataEntry.setStatus("mandatory")
_AdlbAtucCrcErrInterleave_Type = Integer32
_AdlbAtucCrcErrInterleave_Object = MibTableColumn
adlbAtucCrcErrInterleave = _AdlbAtucCrcErrInterleave_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 4, 1, 1),
    _AdlbAtucCrcErrInterleave_Type()
)
adlbAtucCrcErrInterleave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAtucCrcErrInterleave.setStatus("mandatory")
_AdlbAtucCrcErrFast_Type = Integer32
_AdlbAtucCrcErrFast_Object = MibTableColumn
adlbAtucCrcErrFast = _AdlbAtucCrcErrFast_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 4, 1, 2),
    _AdlbAtucCrcErrFast_Type()
)
adlbAtucCrcErrFast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAtucCrcErrFast.setStatus("mandatory")
_AdlbAtucFecErrInterleave_Type = Integer32
_AdlbAtucFecErrInterleave_Object = MibTableColumn
adlbAtucFecErrInterleave = _AdlbAtucFecErrInterleave_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 4, 1, 3),
    _AdlbAtucFecErrInterleave_Type()
)
adlbAtucFecErrInterleave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAtucFecErrInterleave.setStatus("mandatory")
_AdlbAtucFecErrFast_Type = Integer32
_AdlbAtucFecErrFast_Object = MibTableColumn
adlbAtucFecErrFast = _AdlbAtucFecErrFast_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 4, 1, 4),
    _AdlbAtucFecErrFast_Type()
)
adlbAtucFecErrFast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAtucFecErrFast.setStatus("mandatory")
_AdlbAtucSuperFrameSent_Type = Integer32
_AdlbAtucSuperFrameSent_Object = MibTableColumn
adlbAtucSuperFrameSent = _AdlbAtucSuperFrameSent_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 4, 1, 5),
    _AdlbAtucSuperFrameSent_Type()
)
adlbAtucSuperFrameSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAtucSuperFrameSent.setStatus("mandatory")
_AdlbAtucSuperFrameReceived_Type = Integer32
_AdlbAtucSuperFrameReceived_Object = MibTableColumn
adlbAtucSuperFrameReceived = _AdlbAtucSuperFrameReceived_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 4, 1, 6),
    _AdlbAtucSuperFrameReceived_Type()
)
adlbAtucSuperFrameReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAtucSuperFrameReceived.setStatus("mandatory")
_AdlbAtucTimeCount_Type = Integer32
_AdlbAtucTimeCount_Object = MibTableColumn
adlbAtucTimeCount = _AdlbAtucTimeCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 4, 1, 7),
    _AdlbAtucTimeCount_Type()
)
adlbAtucTimeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAtucTimeCount.setStatus("mandatory")
_AdlbAtucErrFrames_Type = Integer32
_AdlbAtucErrFrames_Object = MibTableColumn
adlbAtucErrFrames = _AdlbAtucErrFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 4, 1, 8),
    _AdlbAtucErrFrames_Type()
)
adlbAtucErrFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAtucErrFrames.setStatus("mandatory")
_AdlbAtucBgBENotSES_Type = Integer32
_AdlbAtucBgBENotSES_Object = MibTableColumn
adlbAtucBgBENotSES = _AdlbAtucBgBENotSES_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 4, 1, 9),
    _AdlbAtucBgBENotSES_Type()
)
adlbAtucBgBENotSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAtucBgBENotSES.setStatus("mandatory")
_AdlbAtucErrSecond_Type = Integer32
_AdlbAtucErrSecond_Object = MibTableColumn
adlbAtucErrSecond = _AdlbAtucErrSecond_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 4, 1, 10),
    _AdlbAtucErrSecond_Type()
)
adlbAtucErrSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAtucErrSecond.setStatus("mandatory")
_AdlbAtucSevereErrSecond_Type = Integer32
_AdlbAtucSevereErrSecond_Object = MibTableColumn
adlbAtucSevereErrSecond = _AdlbAtucSevereErrSecond_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 4, 1, 11),
    _AdlbAtucSevereErrSecond_Type()
)
adlbAtucSevereErrSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAtucSevereErrSecond.setStatus("mandatory")
_AdlbAtucNonSESFrames_Type = Integer32
_AdlbAtucNonSESFrames_Object = MibTableColumn
adlbAtucNonSESFrames = _AdlbAtucNonSESFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 4, 1, 12),
    _AdlbAtucNonSESFrames_Type()
)
adlbAtucNonSESFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAtucNonSESFrames.setStatus("mandatory")
_AdlbAtucUnavailableSecond_Type = Integer32
_AdlbAtucUnavailableSecond_Object = MibTableColumn
adlbAtucUnavailableSecond = _AdlbAtucUnavailableSecond_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 4, 1, 13),
    _AdlbAtucUnavailableSecond_Type()
)
adlbAtucUnavailableSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAtucUnavailableSecond.setStatus("mandatory")
_AdlbAtucBitswaps_Type = Integer32
_AdlbAtucBitswaps_Object = MibTableColumn
adlbAtucBitswaps = _AdlbAtucBitswaps_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 4, 1, 14),
    _AdlbAtucBitswaps_Type()
)
adlbAtucBitswaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAtucBitswaps.setStatus("mandatory")
_AdlbAtucLossSecond_Type = Integer32
_AdlbAtucLossSecond_Object = MibTableColumn
adlbAtucLossSecond = _AdlbAtucLossSecond_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 4, 1, 15),
    _AdlbAtucLossSecond_Type()
)
adlbAtucLossSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAtucLossSecond.setStatus("mandatory")
_AdlbAtucFecSecond_Type = Integer32
_AdlbAtucFecSecond_Object = MibTableColumn
adlbAtucFecSecond = _AdlbAtucFecSecond_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 4, 1, 16),
    _AdlbAtucFecSecond_Type()
)
adlbAtucFecSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAtucFecSecond.setStatus("mandatory")
_AdlbAtucFastRetrain_Type = Integer32
_AdlbAtucFastRetrain_Object = MibTableColumn
adlbAtucFastRetrain = _AdlbAtucFastRetrain_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 4, 1, 17),
    _AdlbAtucFastRetrain_Type()
)
adlbAtucFastRetrain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAtucFastRetrain.setStatus("mandatory")
_AdlbAtucFastRetrainFail_Type = Integer32
_AdlbAtucFastRetrainFail_Object = MibTableColumn
adlbAtucFastRetrainFail = _AdlbAtucFastRetrainFail_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 4, 1, 18),
    _AdlbAtucFastRetrainFail_Type()
)
adlbAtucFastRetrainFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAtucFastRetrainFail.setStatus("mandatory")
_AdlbAtucPerfValidIntervals_Type = Integer32
_AdlbAtucPerfValidIntervals_Object = MibTableColumn
adlbAtucPerfValidIntervals = _AdlbAtucPerfValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 4, 1, 19),
    _AdlbAtucPerfValidIntervals_Type()
)
adlbAtucPerfValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAtucPerfValidIntervals.setStatus("mandatory")
_AdlbClearPerfstatistics_Type = Integer32
_AdlbClearPerfstatistics_Object = MibTableColumn
adlbClearPerfstatistics = _AdlbClearPerfstatistics_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 4, 1, 20),
    _AdlbClearPerfstatistics_Type()
)
adlbClearPerfstatistics.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    adlbClearPerfstatistics.setStatus("mandatory")
_HwMusaAdlbAtucPerfPrev15mDataTable_Object = MibTable
hwMusaAdlbAtucPerfPrev15mDataTable = _HwMusaAdlbAtucPerfPrev15mDataTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 5)
)
if mibBuilder.loadTexts:
    hwMusaAdlbAtucPerfPrev15mDataTable.setStatus("mandatory")
_HwMusaAdlbAtucPerfPrev15mDataEntry_Object = MibTableRow
hwMusaAdlbAtucPerfPrev15mDataEntry = _HwMusaAdlbAtucPerfPrev15mDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 5, 1)
)
hwMusaAdlbAtucPerfPrev15mDataEntry.setIndexNames(
    (0, "HUAWEI-MUSA-MA5100-CONFMIB", "hwMusaFrameIndex"),
    (0, "HUAWEI-MUSA-MA5100-CONFMIB", "hwMusaSlotIndex"),
    (0, "HUAWEI-MUSA-MA5100-CONFMIB", "adlbPortIndex"),
)
if mibBuilder.loadTexts:
    hwMusaAdlbAtucPerfPrev15mDataEntry.setStatus("mandatory")
_AdlbAtucPrev15MinCrcErrInterleave_Type = Integer32
_AdlbAtucPrev15MinCrcErrInterleave_Object = MibTableColumn
adlbAtucPrev15MinCrcErrInterleave = _AdlbAtucPrev15MinCrcErrInterleave_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 5, 1, 1),
    _AdlbAtucPrev15MinCrcErrInterleave_Type()
)
adlbAtucPrev15MinCrcErrInterleave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAtucPrev15MinCrcErrInterleave.setStatus("mandatory")
_AdlbAtucPrev15MinCrcErrFast_Type = Integer32
_AdlbAtucPrev15MinCrcErrFast_Object = MibTableColumn
adlbAtucPrev15MinCrcErrFast = _AdlbAtucPrev15MinCrcErrFast_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 5, 1, 2),
    _AdlbAtucPrev15MinCrcErrFast_Type()
)
adlbAtucPrev15MinCrcErrFast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAtucPrev15MinCrcErrFast.setStatus("mandatory")
_AdlbAtucPrev15MinFecErrInterleave_Type = Integer32
_AdlbAtucPrev15MinFecErrInterleave_Object = MibTableColumn
adlbAtucPrev15MinFecErrInterleave = _AdlbAtucPrev15MinFecErrInterleave_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 5, 1, 3),
    _AdlbAtucPrev15MinFecErrInterleave_Type()
)
adlbAtucPrev15MinFecErrInterleave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAtucPrev15MinFecErrInterleave.setStatus("mandatory")
_AdlbAtucPrev15MinFecErrFast_Type = Integer32
_AdlbAtucPrev15MinFecErrFast_Object = MibTableColumn
adlbAtucPrev15MinFecErrFast = _AdlbAtucPrev15MinFecErrFast_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 5, 1, 4),
    _AdlbAtucPrev15MinFecErrFast_Type()
)
adlbAtucPrev15MinFecErrFast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAtucPrev15MinFecErrFast.setStatus("mandatory")
_AdlbAtucPrev15MinSuperFrameSent_Type = Integer32
_AdlbAtucPrev15MinSuperFrameSent_Object = MibTableColumn
adlbAtucPrev15MinSuperFrameSent = _AdlbAtucPrev15MinSuperFrameSent_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 5, 1, 5),
    _AdlbAtucPrev15MinSuperFrameSent_Type()
)
adlbAtucPrev15MinSuperFrameSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAtucPrev15MinSuperFrameSent.setStatus("mandatory")
_AdlbAtucPrev15MinSuperFrameReceived_Type = Integer32
_AdlbAtucPrev15MinSuperFrameReceived_Object = MibTableColumn
adlbAtucPrev15MinSuperFrameReceived = _AdlbAtucPrev15MinSuperFrameReceived_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 5, 1, 6),
    _AdlbAtucPrev15MinSuperFrameReceived_Type()
)
adlbAtucPrev15MinSuperFrameReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAtucPrev15MinSuperFrameReceived.setStatus("mandatory")
_AdlbAtucPrev15MinTimeCount_Type = Integer32
_AdlbAtucPrev15MinTimeCount_Object = MibTableColumn
adlbAtucPrev15MinTimeCount = _AdlbAtucPrev15MinTimeCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 5, 1, 7),
    _AdlbAtucPrev15MinTimeCount_Type()
)
adlbAtucPrev15MinTimeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAtucPrev15MinTimeCount.setStatus("mandatory")
_AdlbAtucPrev15MinErrFrames_Type = Integer32
_AdlbAtucPrev15MinErrFrames_Object = MibTableColumn
adlbAtucPrev15MinErrFrames = _AdlbAtucPrev15MinErrFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 5, 1, 8),
    _AdlbAtucPrev15MinErrFrames_Type()
)
adlbAtucPrev15MinErrFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAtucPrev15MinErrFrames.setStatus("mandatory")
_AdlbAtucPrev15MinBgBENotSES_Type = Integer32
_AdlbAtucPrev15MinBgBENotSES_Object = MibTableColumn
adlbAtucPrev15MinBgBENotSES = _AdlbAtucPrev15MinBgBENotSES_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 5, 1, 9),
    _AdlbAtucPrev15MinBgBENotSES_Type()
)
adlbAtucPrev15MinBgBENotSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAtucPrev15MinBgBENotSES.setStatus("mandatory")
_AdlbAtucPrev15MinErrSecond_Type = Integer32
_AdlbAtucPrev15MinErrSecond_Object = MibTableColumn
adlbAtucPrev15MinErrSecond = _AdlbAtucPrev15MinErrSecond_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 5, 1, 10),
    _AdlbAtucPrev15MinErrSecond_Type()
)
adlbAtucPrev15MinErrSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAtucPrev15MinErrSecond.setStatus("mandatory")
_AdlbAtucPrev15MinSevereErrSecond_Type = Integer32
_AdlbAtucPrev15MinSevereErrSecond_Object = MibTableColumn
adlbAtucPrev15MinSevereErrSecond = _AdlbAtucPrev15MinSevereErrSecond_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 5, 1, 11),
    _AdlbAtucPrev15MinSevereErrSecond_Type()
)
adlbAtucPrev15MinSevereErrSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAtucPrev15MinSevereErrSecond.setStatus("mandatory")
_AdlbAtucPrev15MinNonSESFrames_Type = Integer32
_AdlbAtucPrev15MinNonSESFrames_Object = MibTableColumn
adlbAtucPrev15MinNonSESFrames = _AdlbAtucPrev15MinNonSESFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 5, 1, 12),
    _AdlbAtucPrev15MinNonSESFrames_Type()
)
adlbAtucPrev15MinNonSESFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAtucPrev15MinNonSESFrames.setStatus("mandatory")
_AdlbAtucPrev15MinUnavailableSecond_Type = Integer32
_AdlbAtucPrev15MinUnavailableSecond_Object = MibTableColumn
adlbAtucPrev15MinUnavailableSecond = _AdlbAtucPrev15MinUnavailableSecond_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 5, 1, 13),
    _AdlbAtucPrev15MinUnavailableSecond_Type()
)
adlbAtucPrev15MinUnavailableSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAtucPrev15MinUnavailableSecond.setStatus("mandatory")
_AdlbAtucPrev15MinBitswaps_Type = Integer32
_AdlbAtucPrev15MinBitswaps_Object = MibTableColumn
adlbAtucPrev15MinBitswaps = _AdlbAtucPrev15MinBitswaps_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 5, 1, 14),
    _AdlbAtucPrev15MinBitswaps_Type()
)
adlbAtucPrev15MinBitswaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAtucPrev15MinBitswaps.setStatus("mandatory")
_AdlbAtucPrev15MinLossSecond_Type = Integer32
_AdlbAtucPrev15MinLossSecond_Object = MibTableColumn
adlbAtucPrev15MinLossSecond = _AdlbAtucPrev15MinLossSecond_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 5, 1, 15),
    _AdlbAtucPrev15MinLossSecond_Type()
)
adlbAtucPrev15MinLossSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAtucPrev15MinLossSecond.setStatus("mandatory")
_AdlbAtucPrev15MinFecSecond_Type = Integer32
_AdlbAtucPrev15MinFecSecond_Object = MibTableColumn
adlbAtucPrev15MinFecSecond = _AdlbAtucPrev15MinFecSecond_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 5, 1, 16),
    _AdlbAtucPrev15MinFecSecond_Type()
)
adlbAtucPrev15MinFecSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAtucPrev15MinFecSecond.setStatus("mandatory")
_AdlbAtucPrev15MinFastRetrain_Type = Integer32
_AdlbAtucPrev15MinFastRetrain_Object = MibTableColumn
adlbAtucPrev15MinFastRetrain = _AdlbAtucPrev15MinFastRetrain_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 5, 1, 17),
    _AdlbAtucPrev15MinFastRetrain_Type()
)
adlbAtucPrev15MinFastRetrain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAtucPrev15MinFastRetrain.setStatus("mandatory")
_AdlbAtucPrev15MinFastRetrainFail_Type = Integer32
_AdlbAtucPrev15MinFastRetrainFail_Object = MibTableColumn
adlbAtucPrev15MinFastRetrainFail = _AdlbAtucPrev15MinFastRetrainFail_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 5, 1, 18),
    _AdlbAtucPrev15MinFastRetrainFail_Type()
)
adlbAtucPrev15MinFastRetrainFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAtucPrev15MinFastRetrainFail.setStatus("mandatory")
_HwMusaAdlbAtucPerfCurr24hDataTable_Object = MibTable
hwMusaAdlbAtucPerfCurr24hDataTable = _HwMusaAdlbAtucPerfCurr24hDataTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 6)
)
if mibBuilder.loadTexts:
    hwMusaAdlbAtucPerfCurr24hDataTable.setStatus("mandatory")
_HwMusaAdlbAtucPerfCurr24hDataEntry_Object = MibTableRow
hwMusaAdlbAtucPerfCurr24hDataEntry = _HwMusaAdlbAtucPerfCurr24hDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 6, 1)
)
hwMusaAdlbAtucPerfCurr24hDataEntry.setIndexNames(
    (0, "HUAWEI-MUSA-MA5100-CONFMIB", "hwMusaFrameIndex"),
    (0, "HUAWEI-MUSA-MA5100-CONFMIB", "hwMusaSlotIndex"),
    (0, "HUAWEI-MUSA-MA5100-CONFMIB", "adlbPortIndex"),
)
if mibBuilder.loadTexts:
    hwMusaAdlbAtucPerfCurr24hDataEntry.setStatus("mandatory")
_AdlbAtucCurr1DayCrcErrInterleave_Type = Integer32
_AdlbAtucCurr1DayCrcErrInterleave_Object = MibTableColumn
adlbAtucCurr1DayCrcErrInterleave = _AdlbAtucCurr1DayCrcErrInterleave_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 6, 1, 1),
    _AdlbAtucCurr1DayCrcErrInterleave_Type()
)
adlbAtucCurr1DayCrcErrInterleave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAtucCurr1DayCrcErrInterleave.setStatus("mandatory")
_AdlbAtucCurr1DayCrcErrFast_Type = Integer32
_AdlbAtucCurr1DayCrcErrFast_Object = MibTableColumn
adlbAtucCurr1DayCrcErrFast = _AdlbAtucCurr1DayCrcErrFast_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 6, 1, 2),
    _AdlbAtucCurr1DayCrcErrFast_Type()
)
adlbAtucCurr1DayCrcErrFast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAtucCurr1DayCrcErrFast.setStatus("mandatory")
_AdlbAtucCurr1DayFecErrInterleave_Type = Integer32
_AdlbAtucCurr1DayFecErrInterleave_Object = MibTableColumn
adlbAtucCurr1DayFecErrInterleave = _AdlbAtucCurr1DayFecErrInterleave_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 6, 1, 3),
    _AdlbAtucCurr1DayFecErrInterleave_Type()
)
adlbAtucCurr1DayFecErrInterleave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAtucCurr1DayFecErrInterleave.setStatus("mandatory")
_AdlbAtucCurr1DayFecErrFast_Type = Integer32
_AdlbAtucCurr1DayFecErrFast_Object = MibTableColumn
adlbAtucCurr1DayFecErrFast = _AdlbAtucCurr1DayFecErrFast_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 6, 1, 4),
    _AdlbAtucCurr1DayFecErrFast_Type()
)
adlbAtucCurr1DayFecErrFast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAtucCurr1DayFecErrFast.setStatus("mandatory")
_AdlbAtucCurr1DaySuperFrameSent_Type = Integer32
_AdlbAtucCurr1DaySuperFrameSent_Object = MibTableColumn
adlbAtucCurr1DaySuperFrameSent = _AdlbAtucCurr1DaySuperFrameSent_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 6, 1, 5),
    _AdlbAtucCurr1DaySuperFrameSent_Type()
)
adlbAtucCurr1DaySuperFrameSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAtucCurr1DaySuperFrameSent.setStatus("mandatory")
_AdlbAtucCurr1DaySuperFrameReceived_Type = Integer32
_AdlbAtucCurr1DaySuperFrameReceived_Object = MibTableColumn
adlbAtucCurr1DaySuperFrameReceived = _AdlbAtucCurr1DaySuperFrameReceived_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 6, 1, 6),
    _AdlbAtucCurr1DaySuperFrameReceived_Type()
)
adlbAtucCurr1DaySuperFrameReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAtucCurr1DaySuperFrameReceived.setStatus("mandatory")
_AdlbAtucCurr1DayTimeCount_Type = Integer32
_AdlbAtucCurr1DayTimeCount_Object = MibTableColumn
adlbAtucCurr1DayTimeCount = _AdlbAtucCurr1DayTimeCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 6, 1, 7),
    _AdlbAtucCurr1DayTimeCount_Type()
)
adlbAtucCurr1DayTimeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAtucCurr1DayTimeCount.setStatus("mandatory")
_AdlbAtucCurr1DayErrFrames_Type = Integer32
_AdlbAtucCurr1DayErrFrames_Object = MibTableColumn
adlbAtucCurr1DayErrFrames = _AdlbAtucCurr1DayErrFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 6, 1, 8),
    _AdlbAtucCurr1DayErrFrames_Type()
)
adlbAtucCurr1DayErrFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAtucCurr1DayErrFrames.setStatus("mandatory")
_AdlbAtucCurr1DayBgBENotSES_Type = Integer32
_AdlbAtucCurr1DayBgBENotSES_Object = MibTableColumn
adlbAtucCurr1DayBgBENotSES = _AdlbAtucCurr1DayBgBENotSES_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 6, 1, 9),
    _AdlbAtucCurr1DayBgBENotSES_Type()
)
adlbAtucCurr1DayBgBENotSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAtucCurr1DayBgBENotSES.setStatus("mandatory")
_AdlbAtucCurr1DayErrSecond_Type = Integer32
_AdlbAtucCurr1DayErrSecond_Object = MibTableColumn
adlbAtucCurr1DayErrSecond = _AdlbAtucCurr1DayErrSecond_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 6, 1, 10),
    _AdlbAtucCurr1DayErrSecond_Type()
)
adlbAtucCurr1DayErrSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAtucCurr1DayErrSecond.setStatus("mandatory")
_AdlbAtucCurr1DaySevereErrSecond_Type = Integer32
_AdlbAtucCurr1DaySevereErrSecond_Object = MibTableColumn
adlbAtucCurr1DaySevereErrSecond = _AdlbAtucCurr1DaySevereErrSecond_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 6, 1, 11),
    _AdlbAtucCurr1DaySevereErrSecond_Type()
)
adlbAtucCurr1DaySevereErrSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAtucCurr1DaySevereErrSecond.setStatus("mandatory")
_AdlbAtucCurr1DayNonSESFrames_Type = Integer32
_AdlbAtucCurr1DayNonSESFrames_Object = MibTableColumn
adlbAtucCurr1DayNonSESFrames = _AdlbAtucCurr1DayNonSESFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 6, 1, 12),
    _AdlbAtucCurr1DayNonSESFrames_Type()
)
adlbAtucCurr1DayNonSESFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAtucCurr1DayNonSESFrames.setStatus("mandatory")
_AdlbAtucCurr1DayUnavailableSecond_Type = Integer32
_AdlbAtucCurr1DayUnavailableSecond_Object = MibTableColumn
adlbAtucCurr1DayUnavailableSecond = _AdlbAtucCurr1DayUnavailableSecond_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 6, 1, 13),
    _AdlbAtucCurr1DayUnavailableSecond_Type()
)
adlbAtucCurr1DayUnavailableSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAtucCurr1DayUnavailableSecond.setStatus("mandatory")
_AdlbAtucCurr1DayBitswaps_Type = Integer32
_AdlbAtucCurr1DayBitswaps_Object = MibTableColumn
adlbAtucCurr1DayBitswaps = _AdlbAtucCurr1DayBitswaps_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 6, 1, 14),
    _AdlbAtucCurr1DayBitswaps_Type()
)
adlbAtucCurr1DayBitswaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAtucCurr1DayBitswaps.setStatus("mandatory")
_AdlbAtucCurr1DayLossSecond_Type = Integer32
_AdlbAtucCurr1DayLossSecond_Object = MibTableColumn
adlbAtucCurr1DayLossSecond = _AdlbAtucCurr1DayLossSecond_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 6, 1, 15),
    _AdlbAtucCurr1DayLossSecond_Type()
)
adlbAtucCurr1DayLossSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAtucCurr1DayLossSecond.setStatus("mandatory")
_AdlbAtucCurr1DayFecSecond_Type = Integer32
_AdlbAtucCurr1DayFecSecond_Object = MibTableColumn
adlbAtucCurr1DayFecSecond = _AdlbAtucCurr1DayFecSecond_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 6, 1, 16),
    _AdlbAtucCurr1DayFecSecond_Type()
)
adlbAtucCurr1DayFecSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAtucCurr1DayFecSecond.setStatus("mandatory")
_AdlbAtucCurr1DayFastRetrain_Type = Integer32
_AdlbAtucCurr1DayFastRetrain_Object = MibTableColumn
adlbAtucCurr1DayFastRetrain = _AdlbAtucCurr1DayFastRetrain_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 6, 1, 17),
    _AdlbAtucCurr1DayFastRetrain_Type()
)
adlbAtucCurr1DayFastRetrain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAtucCurr1DayFastRetrain.setStatus("mandatory")
_AdlbAtucCurr1DayFastRetrainFail_Type = Integer32
_AdlbAtucCurr1DayFastRetrainFail_Object = MibTableColumn
adlbAtucCurr1DayFastRetrainFail = _AdlbAtucCurr1DayFastRetrainFail_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 6, 1, 18),
    _AdlbAtucCurr1DayFastRetrainFail_Type()
)
adlbAtucCurr1DayFastRetrainFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAtucCurr1DayFastRetrainFail.setStatus("mandatory")
_HwMusaAdlbAtucPerfPrev24hDataTable_Object = MibTable
hwMusaAdlbAtucPerfPrev24hDataTable = _HwMusaAdlbAtucPerfPrev24hDataTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 7)
)
if mibBuilder.loadTexts:
    hwMusaAdlbAtucPerfPrev24hDataTable.setStatus("mandatory")
_HwMusaAdlbAtucPerfPrev24hDataEntry_Object = MibTableRow
hwMusaAdlbAtucPerfPrev24hDataEntry = _HwMusaAdlbAtucPerfPrev24hDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 7, 1)
)
hwMusaAdlbAtucPerfPrev24hDataEntry.setIndexNames(
    (0, "HUAWEI-MUSA-MA5100-CONFMIB", "hwMusaFrameIndex"),
    (0, "HUAWEI-MUSA-MA5100-CONFMIB", "hwMusaSlotIndex"),
    (0, "HUAWEI-MUSA-MA5100-CONFMIB", "adlbPortIndex"),
)
if mibBuilder.loadTexts:
    hwMusaAdlbAtucPerfPrev24hDataEntry.setStatus("mandatory")
_AdlbAtucPrev1DayCrcErrInterleave_Type = Integer32
_AdlbAtucPrev1DayCrcErrInterleave_Object = MibTableColumn
adlbAtucPrev1DayCrcErrInterleave = _AdlbAtucPrev1DayCrcErrInterleave_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 7, 1, 1),
    _AdlbAtucPrev1DayCrcErrInterleave_Type()
)
adlbAtucPrev1DayCrcErrInterleave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAtucPrev1DayCrcErrInterleave.setStatus("mandatory")
_AdlbAtucPrev1DayCrcErrFast_Type = Integer32
_AdlbAtucPrev1DayCrcErrFast_Object = MibTableColumn
adlbAtucPrev1DayCrcErrFast = _AdlbAtucPrev1DayCrcErrFast_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 7, 1, 2),
    _AdlbAtucPrev1DayCrcErrFast_Type()
)
adlbAtucPrev1DayCrcErrFast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAtucPrev1DayCrcErrFast.setStatus("mandatory")
_AdlbAtucPrev1DayFecErrInterleave_Type = Integer32
_AdlbAtucPrev1DayFecErrInterleave_Object = MibTableColumn
adlbAtucPrev1DayFecErrInterleave = _AdlbAtucPrev1DayFecErrInterleave_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 7, 1, 3),
    _AdlbAtucPrev1DayFecErrInterleave_Type()
)
adlbAtucPrev1DayFecErrInterleave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAtucPrev1DayFecErrInterleave.setStatus("mandatory")
_AdlbAtucPrev1DayFecErrFast_Type = Integer32
_AdlbAtucPrev1DayFecErrFast_Object = MibTableColumn
adlbAtucPrev1DayFecErrFast = _AdlbAtucPrev1DayFecErrFast_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 7, 1, 4),
    _AdlbAtucPrev1DayFecErrFast_Type()
)
adlbAtucPrev1DayFecErrFast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAtucPrev1DayFecErrFast.setStatus("mandatory")
_AdlbAtucPrev1DaySuperFrameSent_Type = Integer32
_AdlbAtucPrev1DaySuperFrameSent_Object = MibTableColumn
adlbAtucPrev1DaySuperFrameSent = _AdlbAtucPrev1DaySuperFrameSent_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 7, 1, 5),
    _AdlbAtucPrev1DaySuperFrameSent_Type()
)
adlbAtucPrev1DaySuperFrameSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAtucPrev1DaySuperFrameSent.setStatus("mandatory")
_AdlbAtucPrev1DaySuperFrameReceived_Type = Integer32
_AdlbAtucPrev1DaySuperFrameReceived_Object = MibTableColumn
adlbAtucPrev1DaySuperFrameReceived = _AdlbAtucPrev1DaySuperFrameReceived_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 7, 1, 6),
    _AdlbAtucPrev1DaySuperFrameReceived_Type()
)
adlbAtucPrev1DaySuperFrameReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAtucPrev1DaySuperFrameReceived.setStatus("mandatory")
_AdlbAtucPrev1DayTimeCount_Type = Integer32
_AdlbAtucPrev1DayTimeCount_Object = MibTableColumn
adlbAtucPrev1DayTimeCount = _AdlbAtucPrev1DayTimeCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 7, 1, 7),
    _AdlbAtucPrev1DayTimeCount_Type()
)
adlbAtucPrev1DayTimeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAtucPrev1DayTimeCount.setStatus("mandatory")
_AdlbAtucPrev1DayErrFrames_Type = Integer32
_AdlbAtucPrev1DayErrFrames_Object = MibTableColumn
adlbAtucPrev1DayErrFrames = _AdlbAtucPrev1DayErrFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 7, 1, 8),
    _AdlbAtucPrev1DayErrFrames_Type()
)
adlbAtucPrev1DayErrFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAtucPrev1DayErrFrames.setStatus("mandatory")
_AdlbAtucPrev1DayBgBENotSES_Type = Integer32
_AdlbAtucPrev1DayBgBENotSES_Object = MibTableColumn
adlbAtucPrev1DayBgBENotSES = _AdlbAtucPrev1DayBgBENotSES_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 7, 1, 9),
    _AdlbAtucPrev1DayBgBENotSES_Type()
)
adlbAtucPrev1DayBgBENotSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAtucPrev1DayBgBENotSES.setStatus("mandatory")
_AdlbAtucPrev1DayErrSecond_Type = Integer32
_AdlbAtucPrev1DayErrSecond_Object = MibTableColumn
adlbAtucPrev1DayErrSecond = _AdlbAtucPrev1DayErrSecond_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 7, 1, 10),
    _AdlbAtucPrev1DayErrSecond_Type()
)
adlbAtucPrev1DayErrSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAtucPrev1DayErrSecond.setStatus("mandatory")
_AdlbAtucPrev1DaySevereErrSecond_Type = Integer32
_AdlbAtucPrev1DaySevereErrSecond_Object = MibTableColumn
adlbAtucPrev1DaySevereErrSecond = _AdlbAtucPrev1DaySevereErrSecond_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 7, 1, 11),
    _AdlbAtucPrev1DaySevereErrSecond_Type()
)
adlbAtucPrev1DaySevereErrSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAtucPrev1DaySevereErrSecond.setStatus("mandatory")
_AdlbAtucPrev1DayNonSESFrames_Type = Integer32
_AdlbAtucPrev1DayNonSESFrames_Object = MibTableColumn
adlbAtucPrev1DayNonSESFrames = _AdlbAtucPrev1DayNonSESFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 7, 1, 12),
    _AdlbAtucPrev1DayNonSESFrames_Type()
)
adlbAtucPrev1DayNonSESFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAtucPrev1DayNonSESFrames.setStatus("mandatory")
_AdlbAtucPrev1DayUnavailableSecond_Type = Integer32
_AdlbAtucPrev1DayUnavailableSecond_Object = MibTableColumn
adlbAtucPrev1DayUnavailableSecond = _AdlbAtucPrev1DayUnavailableSecond_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 7, 1, 13),
    _AdlbAtucPrev1DayUnavailableSecond_Type()
)
adlbAtucPrev1DayUnavailableSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAtucPrev1DayUnavailableSecond.setStatus("mandatory")
_AdlbAtucPrev1DayBitswaps_Type = Integer32
_AdlbAtucPrev1DayBitswaps_Object = MibTableColumn
adlbAtucPrev1DayBitswaps = _AdlbAtucPrev1DayBitswaps_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 7, 1, 14),
    _AdlbAtucPrev1DayBitswaps_Type()
)
adlbAtucPrev1DayBitswaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAtucPrev1DayBitswaps.setStatus("mandatory")
_AdlbAtucPrev1DayLossSecond_Type = Integer32
_AdlbAtucPrev1DayLossSecond_Object = MibTableColumn
adlbAtucPrev1DayLossSecond = _AdlbAtucPrev1DayLossSecond_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 7, 1, 15),
    _AdlbAtucPrev1DayLossSecond_Type()
)
adlbAtucPrev1DayLossSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAtucPrev1DayLossSecond.setStatus("mandatory")
_AdlbAtucPrev1DayFecSecond_Type = Integer32
_AdlbAtucPrev1DayFecSecond_Object = MibTableColumn
adlbAtucPrev1DayFecSecond = _AdlbAtucPrev1DayFecSecond_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 7, 1, 16),
    _AdlbAtucPrev1DayFecSecond_Type()
)
adlbAtucPrev1DayFecSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAtucPrev1DayFecSecond.setStatus("mandatory")
_AdlbAtucPrev1DayFastRetrain_Type = Integer32
_AdlbAtucPrev1DayFastRetrain_Object = MibTableColumn
adlbAtucPrev1DayFastRetrain = _AdlbAtucPrev1DayFastRetrain_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 7, 1, 17),
    _AdlbAtucPrev1DayFastRetrain_Type()
)
adlbAtucPrev1DayFastRetrain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAtucPrev1DayFastRetrain.setStatus("mandatory")
_AdlbAtucPrev1DayFastRetrainFail_Type = Integer32
_AdlbAtucPrev1DayFastRetrainFail_Object = MibTableColumn
adlbAtucPrev1DayFastRetrainFail = _AdlbAtucPrev1DayFastRetrainFail_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 7, 1, 18),
    _AdlbAtucPrev1DayFastRetrainFail_Type()
)
adlbAtucPrev1DayFastRetrainFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAtucPrev1DayFastRetrainFail.setStatus("mandatory")
_HwMusaAdlbAturPerfDataTable_Object = MibTable
hwMusaAdlbAturPerfDataTable = _HwMusaAdlbAturPerfDataTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 8)
)
if mibBuilder.loadTexts:
    hwMusaAdlbAturPerfDataTable.setStatus("mandatory")
_HwMusaAdlbAturPerfDataEntry_Object = MibTableRow
hwMusaAdlbAturPerfDataEntry = _HwMusaAdlbAturPerfDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 8, 1)
)
hwMusaAdlbAturPerfDataEntry.setIndexNames(
    (0, "HUAWEI-MUSA-MA5100-CONFMIB", "hwMusaFrameIndex"),
    (0, "HUAWEI-MUSA-MA5100-CONFMIB", "hwMusaSlotIndex"),
    (0, "HUAWEI-MUSA-MA5100-CONFMIB", "adlbPortIndex"),
)
if mibBuilder.loadTexts:
    hwMusaAdlbAturPerfDataEntry.setStatus("mandatory")
_AdlbAturCrcErrInterleave_Type = Integer32
_AdlbAturCrcErrInterleave_Object = MibTableColumn
adlbAturCrcErrInterleave = _AdlbAturCrcErrInterleave_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 8, 1, 1),
    _AdlbAturCrcErrInterleave_Type()
)
adlbAturCrcErrInterleave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAturCrcErrInterleave.setStatus("mandatory")
_AdlbAturCrcErrFast_Type = Integer32
_AdlbAturCrcErrFast_Object = MibTableColumn
adlbAturCrcErrFast = _AdlbAturCrcErrFast_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 8, 1, 2),
    _AdlbAturCrcErrFast_Type()
)
adlbAturCrcErrFast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAturCrcErrFast.setStatus("mandatory")
_AdlbAturFecErrInterleave_Type = Integer32
_AdlbAturFecErrInterleave_Object = MibTableColumn
adlbAturFecErrInterleave = _AdlbAturFecErrInterleave_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 8, 1, 3),
    _AdlbAturFecErrInterleave_Type()
)
adlbAturFecErrInterleave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAturFecErrInterleave.setStatus("mandatory")
_AdlbAturFecErrFast_Type = Integer32
_AdlbAturFecErrFast_Object = MibTableColumn
adlbAturFecErrFast = _AdlbAturFecErrFast_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 8, 1, 4),
    _AdlbAturFecErrFast_Type()
)
adlbAturFecErrFast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAturFecErrFast.setStatus("mandatory")
_AdlbAturTimeCount_Type = Integer32
_AdlbAturTimeCount_Object = MibTableColumn
adlbAturTimeCount = _AdlbAturTimeCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 8, 1, 5),
    _AdlbAturTimeCount_Type()
)
adlbAturTimeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAturTimeCount.setStatus("mandatory")
_AdlbAturErrFrames_Type = Integer32
_AdlbAturErrFrames_Object = MibTableColumn
adlbAturErrFrames = _AdlbAturErrFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 8, 1, 6),
    _AdlbAturErrFrames_Type()
)
adlbAturErrFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAturErrFrames.setStatus("mandatory")
_AdlbAturBgBENotSES_Type = Integer32
_AdlbAturBgBENotSES_Object = MibTableColumn
adlbAturBgBENotSES = _AdlbAturBgBENotSES_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 8, 1, 7),
    _AdlbAturBgBENotSES_Type()
)
adlbAturBgBENotSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAturBgBENotSES.setStatus("mandatory")
_AdlbAturErrSecond_Type = Integer32
_AdlbAturErrSecond_Object = MibTableColumn
adlbAturErrSecond = _AdlbAturErrSecond_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 8, 1, 8),
    _AdlbAturErrSecond_Type()
)
adlbAturErrSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAturErrSecond.setStatus("mandatory")
_AdlbAturSevereErrSecond_Type = Integer32
_AdlbAturSevereErrSecond_Object = MibTableColumn
adlbAturSevereErrSecond = _AdlbAturSevereErrSecond_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 8, 1, 9),
    _AdlbAturSevereErrSecond_Type()
)
adlbAturSevereErrSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAturSevereErrSecond.setStatus("mandatory")
_AdlbAturNonSESFrames_Type = Integer32
_AdlbAturNonSESFrames_Object = MibTableColumn
adlbAturNonSESFrames = _AdlbAturNonSESFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 8, 1, 10),
    _AdlbAturNonSESFrames_Type()
)
adlbAturNonSESFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAturNonSESFrames.setStatus("mandatory")
_AdlbAturUnavailableSecond_Type = Integer32
_AdlbAturUnavailableSecond_Object = MibTableColumn
adlbAturUnavailableSecond = _AdlbAturUnavailableSecond_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 8, 1, 11),
    _AdlbAturUnavailableSecond_Type()
)
adlbAturUnavailableSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAturUnavailableSecond.setStatus("mandatory")
_AdlbAturLossSecond_Type = Integer32
_AdlbAturLossSecond_Object = MibTableColumn
adlbAturLossSecond = _AdlbAturLossSecond_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 8, 1, 12),
    _AdlbAturLossSecond_Type()
)
adlbAturLossSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAturLossSecond.setStatus("mandatory")
_AdlbAturFecSecond_Type = Integer32
_AdlbAturFecSecond_Object = MibTableColumn
adlbAturFecSecond = _AdlbAturFecSecond_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 8, 1, 13),
    _AdlbAturFecSecond_Type()
)
adlbAturFecSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAturFecSecond.setStatus("mandatory")
_AdlbAturPerfValidIntervals_Type = Integer32
_AdlbAturPerfValidIntervals_Object = MibTableColumn
adlbAturPerfValidIntervals = _AdlbAturPerfValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 8, 1, 14),
    _AdlbAturPerfValidIntervals_Type()
)
adlbAturPerfValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAturPerfValidIntervals.setStatus("mandatory")
_HwMusaAdlbAturPerfPrev15mDataTable_Object = MibTable
hwMusaAdlbAturPerfPrev15mDataTable = _HwMusaAdlbAturPerfPrev15mDataTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 9)
)
if mibBuilder.loadTexts:
    hwMusaAdlbAturPerfPrev15mDataTable.setStatus("mandatory")
_HwMusaAdlbAturPerfPrev15mDataEntry_Object = MibTableRow
hwMusaAdlbAturPerfPrev15mDataEntry = _HwMusaAdlbAturPerfPrev15mDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 9, 1)
)
hwMusaAdlbAturPerfPrev15mDataEntry.setIndexNames(
    (0, "HUAWEI-MUSA-MA5100-CONFMIB", "hwMusaFrameIndex"),
    (0, "HUAWEI-MUSA-MA5100-CONFMIB", "hwMusaSlotIndex"),
    (0, "HUAWEI-MUSA-MA5100-CONFMIB", "adlbPortIndex"),
)
if mibBuilder.loadTexts:
    hwMusaAdlbAturPerfPrev15mDataEntry.setStatus("mandatory")
_AdlbAturPrev15MinCrcErrInterleave_Type = Integer32
_AdlbAturPrev15MinCrcErrInterleave_Object = MibTableColumn
adlbAturPrev15MinCrcErrInterleave = _AdlbAturPrev15MinCrcErrInterleave_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 9, 1, 1),
    _AdlbAturPrev15MinCrcErrInterleave_Type()
)
adlbAturPrev15MinCrcErrInterleave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAturPrev15MinCrcErrInterleave.setStatus("mandatory")
_AdlbAturPrev15MinCrcErrFast_Type = Integer32
_AdlbAturPrev15MinCrcErrFast_Object = MibTableColumn
adlbAturPrev15MinCrcErrFast = _AdlbAturPrev15MinCrcErrFast_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 9, 1, 2),
    _AdlbAturPrev15MinCrcErrFast_Type()
)
adlbAturPrev15MinCrcErrFast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAturPrev15MinCrcErrFast.setStatus("mandatory")
_AdlbAturPrev15MinFecErrInterleave_Type = Integer32
_AdlbAturPrev15MinFecErrInterleave_Object = MibTableColumn
adlbAturPrev15MinFecErrInterleave = _AdlbAturPrev15MinFecErrInterleave_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 9, 1, 3),
    _AdlbAturPrev15MinFecErrInterleave_Type()
)
adlbAturPrev15MinFecErrInterleave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAturPrev15MinFecErrInterleave.setStatus("mandatory")
_AdlbAturPrev15MinFecErrFast_Type = Integer32
_AdlbAturPrev15MinFecErrFast_Object = MibTableColumn
adlbAturPrev15MinFecErrFast = _AdlbAturPrev15MinFecErrFast_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 9, 1, 4),
    _AdlbAturPrev15MinFecErrFast_Type()
)
adlbAturPrev15MinFecErrFast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAturPrev15MinFecErrFast.setStatus("mandatory")
_AdlbAturPrev15MinTimeCount_Type = Integer32
_AdlbAturPrev15MinTimeCount_Object = MibTableColumn
adlbAturPrev15MinTimeCount = _AdlbAturPrev15MinTimeCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 9, 1, 5),
    _AdlbAturPrev15MinTimeCount_Type()
)
adlbAturPrev15MinTimeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAturPrev15MinTimeCount.setStatus("mandatory")
_AdlbAturPrev15MinErrFrames_Type = Integer32
_AdlbAturPrev15MinErrFrames_Object = MibTableColumn
adlbAturPrev15MinErrFrames = _AdlbAturPrev15MinErrFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 9, 1, 6),
    _AdlbAturPrev15MinErrFrames_Type()
)
adlbAturPrev15MinErrFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAturPrev15MinErrFrames.setStatus("mandatory")
_AdlbAturPrev15MinBgBENotSES_Type = Integer32
_AdlbAturPrev15MinBgBENotSES_Object = MibTableColumn
adlbAturPrev15MinBgBENotSES = _AdlbAturPrev15MinBgBENotSES_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 9, 1, 7),
    _AdlbAturPrev15MinBgBENotSES_Type()
)
adlbAturPrev15MinBgBENotSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAturPrev15MinBgBENotSES.setStatus("mandatory")
_AdlbAturPrev15MinErrSecond_Type = Integer32
_AdlbAturPrev15MinErrSecond_Object = MibTableColumn
adlbAturPrev15MinErrSecond = _AdlbAturPrev15MinErrSecond_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 9, 1, 8),
    _AdlbAturPrev15MinErrSecond_Type()
)
adlbAturPrev15MinErrSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAturPrev15MinErrSecond.setStatus("mandatory")
_AdlbAturPrev15MinSevereErrSecond_Type = Integer32
_AdlbAturPrev15MinSevereErrSecond_Object = MibTableColumn
adlbAturPrev15MinSevereErrSecond = _AdlbAturPrev15MinSevereErrSecond_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 9, 1, 9),
    _AdlbAturPrev15MinSevereErrSecond_Type()
)
adlbAturPrev15MinSevereErrSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAturPrev15MinSevereErrSecond.setStatus("mandatory")
_AdlbAturPrev15MinNonSESFrames_Type = Integer32
_AdlbAturPrev15MinNonSESFrames_Object = MibTableColumn
adlbAturPrev15MinNonSESFrames = _AdlbAturPrev15MinNonSESFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 9, 1, 10),
    _AdlbAturPrev15MinNonSESFrames_Type()
)
adlbAturPrev15MinNonSESFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAturPrev15MinNonSESFrames.setStatus("mandatory")
_AdlbAturPrev15MinUnavailableSecond_Type = Integer32
_AdlbAturPrev15MinUnavailableSecond_Object = MibTableColumn
adlbAturPrev15MinUnavailableSecond = _AdlbAturPrev15MinUnavailableSecond_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 9, 1, 11),
    _AdlbAturPrev15MinUnavailableSecond_Type()
)
adlbAturPrev15MinUnavailableSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAturPrev15MinUnavailableSecond.setStatus("mandatory")
_AdlbAturPrev15MinLossSecond_Type = Integer32
_AdlbAturPrev15MinLossSecond_Object = MibTableColumn
adlbAturPrev15MinLossSecond = _AdlbAturPrev15MinLossSecond_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 9, 1, 12),
    _AdlbAturPrev15MinLossSecond_Type()
)
adlbAturPrev15MinLossSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAturPrev15MinLossSecond.setStatus("mandatory")
_AdlbAturPrev15MinFecSecond_Type = Integer32
_AdlbAturPrev15MinFecSecond_Object = MibTableColumn
adlbAturPrev15MinFecSecond = _AdlbAturPrev15MinFecSecond_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 9, 1, 13),
    _AdlbAturPrev15MinFecSecond_Type()
)
adlbAturPrev15MinFecSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAturPrev15MinFecSecond.setStatus("mandatory")
_HwMusaAdlbAturPerfCurr24hDataTable_Object = MibTable
hwMusaAdlbAturPerfCurr24hDataTable = _HwMusaAdlbAturPerfCurr24hDataTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 10)
)
if mibBuilder.loadTexts:
    hwMusaAdlbAturPerfCurr24hDataTable.setStatus("mandatory")
_HwMusaAdlbAturPerfCurr24hDataEntry_Object = MibTableRow
hwMusaAdlbAturPerfCurr24hDataEntry = _HwMusaAdlbAturPerfCurr24hDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 10, 1)
)
hwMusaAdlbAturPerfCurr24hDataEntry.setIndexNames(
    (0, "HUAWEI-MUSA-MA5100-CONFMIB", "hwMusaFrameIndex"),
    (0, "HUAWEI-MUSA-MA5100-CONFMIB", "hwMusaSlotIndex"),
    (0, "HUAWEI-MUSA-MA5100-CONFMIB", "adlbPortIndex"),
)
if mibBuilder.loadTexts:
    hwMusaAdlbAturPerfCurr24hDataEntry.setStatus("mandatory")
_AdlbAturCurr1DayCrcErrInterleave_Type = Integer32
_AdlbAturCurr1DayCrcErrInterleave_Object = MibTableColumn
adlbAturCurr1DayCrcErrInterleave = _AdlbAturCurr1DayCrcErrInterleave_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 10, 1, 1),
    _AdlbAturCurr1DayCrcErrInterleave_Type()
)
adlbAturCurr1DayCrcErrInterleave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAturCurr1DayCrcErrInterleave.setStatus("mandatory")
_AdlbAturCurr1DayCrcErrFast_Type = Integer32
_AdlbAturCurr1DayCrcErrFast_Object = MibTableColumn
adlbAturCurr1DayCrcErrFast = _AdlbAturCurr1DayCrcErrFast_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 10, 1, 2),
    _AdlbAturCurr1DayCrcErrFast_Type()
)
adlbAturCurr1DayCrcErrFast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAturCurr1DayCrcErrFast.setStatus("mandatory")
_AdlbAturCurr1DayFecErrInterleave_Type = Integer32
_AdlbAturCurr1DayFecErrInterleave_Object = MibTableColumn
adlbAturCurr1DayFecErrInterleave = _AdlbAturCurr1DayFecErrInterleave_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 10, 1, 3),
    _AdlbAturCurr1DayFecErrInterleave_Type()
)
adlbAturCurr1DayFecErrInterleave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAturCurr1DayFecErrInterleave.setStatus("mandatory")
_AdlbAturCurr1DayFecErrFast_Type = Integer32
_AdlbAturCurr1DayFecErrFast_Object = MibTableColumn
adlbAturCurr1DayFecErrFast = _AdlbAturCurr1DayFecErrFast_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 10, 1, 4),
    _AdlbAturCurr1DayFecErrFast_Type()
)
adlbAturCurr1DayFecErrFast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAturCurr1DayFecErrFast.setStatus("mandatory")
_AdlbAturCurr1DayTimeCount_Type = Integer32
_AdlbAturCurr1DayTimeCount_Object = MibTableColumn
adlbAturCurr1DayTimeCount = _AdlbAturCurr1DayTimeCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 10, 1, 5),
    _AdlbAturCurr1DayTimeCount_Type()
)
adlbAturCurr1DayTimeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAturCurr1DayTimeCount.setStatus("mandatory")
_AdlbAturCurr1DayErrFrames_Type = Integer32
_AdlbAturCurr1DayErrFrames_Object = MibTableColumn
adlbAturCurr1DayErrFrames = _AdlbAturCurr1DayErrFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 10, 1, 6),
    _AdlbAturCurr1DayErrFrames_Type()
)
adlbAturCurr1DayErrFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAturCurr1DayErrFrames.setStatus("mandatory")
_AdlbAturCurr1DayBgBENotSES_Type = Integer32
_AdlbAturCurr1DayBgBENotSES_Object = MibTableColumn
adlbAturCurr1DayBgBENotSES = _AdlbAturCurr1DayBgBENotSES_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 10, 1, 7),
    _AdlbAturCurr1DayBgBENotSES_Type()
)
adlbAturCurr1DayBgBENotSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAturCurr1DayBgBENotSES.setStatus("mandatory")
_AdlbAturCurr1DayErrSecond_Type = Integer32
_AdlbAturCurr1DayErrSecond_Object = MibTableColumn
adlbAturCurr1DayErrSecond = _AdlbAturCurr1DayErrSecond_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 10, 1, 8),
    _AdlbAturCurr1DayErrSecond_Type()
)
adlbAturCurr1DayErrSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAturCurr1DayErrSecond.setStatus("mandatory")
_AdlbAturCurr1DaySevereErrSecond_Type = Integer32
_AdlbAturCurr1DaySevereErrSecond_Object = MibTableColumn
adlbAturCurr1DaySevereErrSecond = _AdlbAturCurr1DaySevereErrSecond_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 10, 1, 9),
    _AdlbAturCurr1DaySevereErrSecond_Type()
)
adlbAturCurr1DaySevereErrSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAturCurr1DaySevereErrSecond.setStatus("mandatory")
_AdlbAturCurr1DayNonSESFrames_Type = Integer32
_AdlbAturCurr1DayNonSESFrames_Object = MibTableColumn
adlbAturCurr1DayNonSESFrames = _AdlbAturCurr1DayNonSESFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 10, 1, 10),
    _AdlbAturCurr1DayNonSESFrames_Type()
)
adlbAturCurr1DayNonSESFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAturCurr1DayNonSESFrames.setStatus("mandatory")
_AdlbAturCurr1DayUnavailableSecond_Type = Integer32
_AdlbAturCurr1DayUnavailableSecond_Object = MibTableColumn
adlbAturCurr1DayUnavailableSecond = _AdlbAturCurr1DayUnavailableSecond_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 10, 1, 11),
    _AdlbAturCurr1DayUnavailableSecond_Type()
)
adlbAturCurr1DayUnavailableSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAturCurr1DayUnavailableSecond.setStatus("mandatory")
_AdlbAturCurr1DayLossSecond_Type = Integer32
_AdlbAturCurr1DayLossSecond_Object = MibTableColumn
adlbAturCurr1DayLossSecond = _AdlbAturCurr1DayLossSecond_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 10, 1, 12),
    _AdlbAturCurr1DayLossSecond_Type()
)
adlbAturCurr1DayLossSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAturCurr1DayLossSecond.setStatus("mandatory")
_AdlbAturCurr1DayFecSecond_Type = Integer32
_AdlbAturCurr1DayFecSecond_Object = MibTableColumn
adlbAturCurr1DayFecSecond = _AdlbAturCurr1DayFecSecond_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 10, 1, 13),
    _AdlbAturCurr1DayFecSecond_Type()
)
adlbAturCurr1DayFecSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAturCurr1DayFecSecond.setStatus("mandatory")
_HwMusaAdlbAturPerfPrev24hDataTable_Object = MibTable
hwMusaAdlbAturPerfPrev24hDataTable = _HwMusaAdlbAturPerfPrev24hDataTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 11)
)
if mibBuilder.loadTexts:
    hwMusaAdlbAturPerfPrev24hDataTable.setStatus("mandatory")
_HwMusaAdlbAturPerfPrev24hDataEntry_Object = MibTableRow
hwMusaAdlbAturPerfPrev24hDataEntry = _HwMusaAdlbAturPerfPrev24hDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 11, 1)
)
hwMusaAdlbAturPerfPrev24hDataEntry.setIndexNames(
    (0, "HUAWEI-MUSA-MA5100-CONFMIB", "hwMusaFrameIndex"),
    (0, "HUAWEI-MUSA-MA5100-CONFMIB", "hwMusaSlotIndex"),
    (0, "HUAWEI-MUSA-MA5100-CONFMIB", "adlbPortIndex"),
)
if mibBuilder.loadTexts:
    hwMusaAdlbAturPerfPrev24hDataEntry.setStatus("mandatory")
_AdlbAturPrev1DayCrcErrInterleave_Type = Integer32
_AdlbAturPrev1DayCrcErrInterleave_Object = MibTableColumn
adlbAturPrev1DayCrcErrInterleave = _AdlbAturPrev1DayCrcErrInterleave_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 11, 1, 1),
    _AdlbAturPrev1DayCrcErrInterleave_Type()
)
adlbAturPrev1DayCrcErrInterleave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAturPrev1DayCrcErrInterleave.setStatus("mandatory")
_AdlbAturPrev1DayCrcErrFast_Type = Integer32
_AdlbAturPrev1DayCrcErrFast_Object = MibTableColumn
adlbAturPrev1DayCrcErrFast = _AdlbAturPrev1DayCrcErrFast_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 11, 1, 2),
    _AdlbAturPrev1DayCrcErrFast_Type()
)
adlbAturPrev1DayCrcErrFast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAturPrev1DayCrcErrFast.setStatus("mandatory")
_AdlbAturPrev1DayFecErrInterleave_Type = Integer32
_AdlbAturPrev1DayFecErrInterleave_Object = MibTableColumn
adlbAturPrev1DayFecErrInterleave = _AdlbAturPrev1DayFecErrInterleave_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 11, 1, 3),
    _AdlbAturPrev1DayFecErrInterleave_Type()
)
adlbAturPrev1DayFecErrInterleave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAturPrev1DayFecErrInterleave.setStatus("mandatory")
_AdlbAturPrev1DayFecErrFast_Type = Integer32
_AdlbAturPrev1DayFecErrFast_Object = MibTableColumn
adlbAturPrev1DayFecErrFast = _AdlbAturPrev1DayFecErrFast_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 11, 1, 4),
    _AdlbAturPrev1DayFecErrFast_Type()
)
adlbAturPrev1DayFecErrFast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAturPrev1DayFecErrFast.setStatus("mandatory")
_AdlbAturPrev1DayTimeCount_Type = Integer32
_AdlbAturPrev1DayTimeCount_Object = MibTableColumn
adlbAturPrev1DayTimeCount = _AdlbAturPrev1DayTimeCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 11, 1, 5),
    _AdlbAturPrev1DayTimeCount_Type()
)
adlbAturPrev1DayTimeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAturPrev1DayTimeCount.setStatus("mandatory")
_AdlbAturPrev1DayErrFrames_Type = Integer32
_AdlbAturPrev1DayErrFrames_Object = MibTableColumn
adlbAturPrev1DayErrFrames = _AdlbAturPrev1DayErrFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 11, 1, 6),
    _AdlbAturPrev1DayErrFrames_Type()
)
adlbAturPrev1DayErrFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAturPrev1DayErrFrames.setStatus("mandatory")
_AdlbAturPrev1DayBgBENotSES_Type = Integer32
_AdlbAturPrev1DayBgBENotSES_Object = MibTableColumn
adlbAturPrev1DayBgBENotSES = _AdlbAturPrev1DayBgBENotSES_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 11, 1, 7),
    _AdlbAturPrev1DayBgBENotSES_Type()
)
adlbAturPrev1DayBgBENotSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAturPrev1DayBgBENotSES.setStatus("mandatory")
_AdlbAturPrev1DayErrSecond_Type = Integer32
_AdlbAturPrev1DayErrSecond_Object = MibTableColumn
adlbAturPrev1DayErrSecond = _AdlbAturPrev1DayErrSecond_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 11, 1, 8),
    _AdlbAturPrev1DayErrSecond_Type()
)
adlbAturPrev1DayErrSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAturPrev1DayErrSecond.setStatus("mandatory")
_AdlbAturPrev1DaySevereErrSecond_Type = Integer32
_AdlbAturPrev1DaySevereErrSecond_Object = MibTableColumn
adlbAturPrev1DaySevereErrSecond = _AdlbAturPrev1DaySevereErrSecond_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 11, 1, 9),
    _AdlbAturPrev1DaySevereErrSecond_Type()
)
adlbAturPrev1DaySevereErrSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAturPrev1DaySevereErrSecond.setStatus("mandatory")
_AdlbAturPrev1DayNonSESFrames_Type = Integer32
_AdlbAturPrev1DayNonSESFrames_Object = MibTableColumn
adlbAturPrev1DayNonSESFrames = _AdlbAturPrev1DayNonSESFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 11, 1, 10),
    _AdlbAturPrev1DayNonSESFrames_Type()
)
adlbAturPrev1DayNonSESFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAturPrev1DayNonSESFrames.setStatus("mandatory")
_AdlbAturPrev1DayUnavailableSecond_Type = Integer32
_AdlbAturPrev1DayUnavailableSecond_Object = MibTableColumn
adlbAturPrev1DayUnavailableSecond = _AdlbAturPrev1DayUnavailableSecond_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 11, 1, 11),
    _AdlbAturPrev1DayUnavailableSecond_Type()
)
adlbAturPrev1DayUnavailableSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAturPrev1DayUnavailableSecond.setStatus("mandatory")
_AdlbAturPrev1DayLossSecond_Type = Integer32
_AdlbAturPrev1DayLossSecond_Object = MibTableColumn
adlbAturPrev1DayLossSecond = _AdlbAturPrev1DayLossSecond_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 11, 1, 12),
    _AdlbAturPrev1DayLossSecond_Type()
)
adlbAturPrev1DayLossSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAturPrev1DayLossSecond.setStatus("mandatory")
_AdlbAturPrev1DayFecSecond_Type = Integer32
_AdlbAturPrev1DayFecSecond_Object = MibTableColumn
adlbAturPrev1DayFecSecond = _AdlbAturPrev1DayFecSecond_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 11, 1, 13),
    _AdlbAturPrev1DayFecSecond_Type()
)
adlbAturPrev1DayFecSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAturPrev1DayFecSecond.setStatus("mandatory")
_HwMusaAdlbAtucLineDefectTable_Object = MibTable
hwMusaAdlbAtucLineDefectTable = _HwMusaAdlbAtucLineDefectTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 12)
)
if mibBuilder.loadTexts:
    hwMusaAdlbAtucLineDefectTable.setStatus("mandatory")
_HwMusaAdlbAtucLineDefectEntry_Object = MibTableRow
hwMusaAdlbAtucLineDefectEntry = _HwMusaAdlbAtucLineDefectEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 12, 1)
)
hwMusaAdlbAtucLineDefectEntry.setIndexNames(
    (0, "HUAWEI-MUSA-MA5100-CONFMIB", "hwMusaFrameIndex"),
    (0, "HUAWEI-MUSA-MA5100-CONFMIB", "hwMusaSlotIndex"),
    (0, "HUAWEI-MUSA-MA5100-CONFMIB", "adlbPortIndex"),
)
if mibBuilder.loadTexts:
    hwMusaAdlbAtucLineDefectEntry.setStatus("mandatory")
_AdlbAtucLpsState_Type = Integer32
_AdlbAtucLpsState_Object = MibTableColumn
adlbAtucLpsState = _AdlbAtucLpsState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 12, 1, 1),
    _AdlbAtucLpsState_Type()
)
adlbAtucLpsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAtucLpsState.setStatus("mandatory")
_AdlbAtucSefState_Type = Integer32
_AdlbAtucSefState_Object = MibTableColumn
adlbAtucSefState = _AdlbAtucSefState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 12, 1, 2),
    _AdlbAtucSefState_Type()
)
adlbAtucSefState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAtucSefState.setStatus("mandatory")
_AdlbAtucLosState_Type = Integer32
_AdlbAtucLosState_Object = MibTableColumn
adlbAtucLosState = _AdlbAtucLosState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 12, 1, 3),
    _AdlbAtucLosState_Type()
)
adlbAtucLosState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAtucLosState.setStatus("mandatory")
_AdlbAtucLofState_Type = Integer32
_AdlbAtucLofState_Object = MibTableColumn
adlbAtucLofState = _AdlbAtucLofState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 12, 1, 4),
    _AdlbAtucLofState_Type()
)
adlbAtucLofState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAtucLofState.setStatus("mandatory")
_AdlbAtucFebeInterleaveState_Type = Integer32
_AdlbAtucFebeInterleaveState_Object = MibTableColumn
adlbAtucFebeInterleaveState = _AdlbAtucFebeInterleaveState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 12, 1, 5),
    _AdlbAtucFebeInterleaveState_Type()
)
adlbAtucFebeInterleaveState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAtucFebeInterleaveState.setStatus("mandatory")
_AdlbAtucFebeFastState_Type = Integer32
_AdlbAtucFebeFastState_Object = MibTableColumn
adlbAtucFebeFastState = _AdlbAtucFebeFastState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 12, 1, 6),
    _AdlbAtucFebeFastState_Type()
)
adlbAtucFebeFastState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAtucFebeFastState.setStatus("mandatory")
_AdlbAtucFecInterleaveState_Type = Integer32
_AdlbAtucFecInterleaveState_Object = MibTableColumn
adlbAtucFecInterleaveState = _AdlbAtucFecInterleaveState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 12, 1, 7),
    _AdlbAtucFecInterleaveState_Type()
)
adlbAtucFecInterleaveState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAtucFecInterleaveState.setStatus("mandatory")
_AdlbAtucFecFastState_Type = Integer32
_AdlbAtucFecFastState_Object = MibTableColumn
adlbAtucFecFastState = _AdlbAtucFecFastState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 12, 1, 8),
    _AdlbAtucFecFastState_Type()
)
adlbAtucFecFastState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAtucFecFastState.setStatus("mandatory")
_HwMusaAdlbAturLineDefectTable_Object = MibTable
hwMusaAdlbAturLineDefectTable = _HwMusaAdlbAturLineDefectTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 13)
)
if mibBuilder.loadTexts:
    hwMusaAdlbAturLineDefectTable.setStatus("mandatory")
_HwMusaAdlbAturLineDefectEntry_Object = MibTableRow
hwMusaAdlbAturLineDefectEntry = _HwMusaAdlbAturLineDefectEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 13, 1)
)
hwMusaAdlbAturLineDefectEntry.setIndexNames(
    (0, "HUAWEI-MUSA-MA5100-CONFMIB", "hwMusaFrameIndex"),
    (0, "HUAWEI-MUSA-MA5100-CONFMIB", "hwMusaSlotIndex"),
    (0, "HUAWEI-MUSA-MA5100-CONFMIB", "adlbPortIndex"),
)
if mibBuilder.loadTexts:
    hwMusaAdlbAturLineDefectEntry.setStatus("mandatory")
_AdlbAturLpsState_Type = Integer32
_AdlbAturLpsState_Object = MibTableColumn
adlbAturLpsState = _AdlbAturLpsState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 13, 1, 1),
    _AdlbAturLpsState_Type()
)
adlbAturLpsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAturLpsState.setStatus("mandatory")
_AdlbAturRdiState_Type = Integer32
_AdlbAturRdiState_Object = MibTableColumn
adlbAturRdiState = _AdlbAturRdiState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 13, 1, 2),
    _AdlbAturRdiState_Type()
)
adlbAturRdiState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAturRdiState.setStatus("mandatory")
_AdlbAturLosState_Type = Integer32
_AdlbAturLosState_Object = MibTableColumn
adlbAturLosState = _AdlbAturLosState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 13, 1, 3),
    _AdlbAturLosState_Type()
)
adlbAturLosState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAturLosState.setStatus("mandatory")
_AdlbAturFriState_Type = Integer32
_AdlbAturFriState_Object = MibTableColumn
adlbAturFriState = _AdlbAturFriState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 13, 1, 4),
    _AdlbAturFriState_Type()
)
adlbAturFriState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAturFriState.setStatus("mandatory")
_AdlbAturFebeInterleaveState_Type = Integer32
_AdlbAturFebeInterleaveState_Object = MibTableColumn
adlbAturFebeInterleaveState = _AdlbAturFebeInterleaveState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 13, 1, 5),
    _AdlbAturFebeInterleaveState_Type()
)
adlbAturFebeInterleaveState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAturFebeInterleaveState.setStatus("mandatory")
_AdlbAturFebeFastState_Type = Integer32
_AdlbAturFebeFastState_Object = MibTableColumn
adlbAturFebeFastState = _AdlbAturFebeFastState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 13, 1, 6),
    _AdlbAturFebeFastState_Type()
)
adlbAturFebeFastState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAturFebeFastState.setStatus("mandatory")
_AdlbAturFecInterleaveState_Type = Integer32
_AdlbAturFecInterleaveState_Object = MibTableColumn
adlbAturFecInterleaveState = _AdlbAturFecInterleaveState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 13, 1, 7),
    _AdlbAturFecInterleaveState_Type()
)
adlbAturFecInterleaveState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAturFecInterleaveState.setStatus("mandatory")
_AdlbAturFecFastState_Type = Integer32
_AdlbAturFecFastState_Object = MibTableColumn
adlbAturFecFastState = _AdlbAturFecFastState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 13, 1, 8),
    _AdlbAturFecFastState_Type()
)
adlbAturFecFastState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAturFecFastState.setStatus("mandatory")
_HwMusaAdlbAtucAtmDefectTable_Object = MibTable
hwMusaAdlbAtucAtmDefectTable = _HwMusaAdlbAtucAtmDefectTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 14)
)
if mibBuilder.loadTexts:
    hwMusaAdlbAtucAtmDefectTable.setStatus("mandatory")
_HwMusaAdlbAtucAtmDefectEntry_Object = MibTableRow
hwMusaAdlbAtucAtmDefectEntry = _HwMusaAdlbAtucAtmDefectEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 14, 1)
)
hwMusaAdlbAtucAtmDefectEntry.setIndexNames(
    (0, "HUAWEI-MUSA-MA5100-CONFMIB", "hwMusaFrameIndex"),
    (0, "HUAWEI-MUSA-MA5100-CONFMIB", "hwMusaSlotIndex"),
    (0, "HUAWEI-MUSA-MA5100-CONFMIB", "adlbPortIndex"),
)
if mibBuilder.loadTexts:
    hwMusaAdlbAtucAtmDefectEntry.setStatus("mandatory")
_AdlbAtucHecInterleave_Type = Integer32
_AdlbAtucHecInterleave_Object = MibTableColumn
adlbAtucHecInterleave = _AdlbAtucHecInterleave_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 14, 1, 1),
    _AdlbAtucHecInterleave_Type()
)
adlbAtucHecInterleave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAtucHecInterleave.setStatus("mandatory")
_AdlbAtucHecFast_Type = Integer32
_AdlbAtucHecFast_Object = MibTableColumn
adlbAtucHecFast = _AdlbAtucHecFast_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 14, 1, 2),
    _AdlbAtucHecFast_Type()
)
adlbAtucHecFast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAtucHecFast.setStatus("mandatory")
_AdlbAtucNcdInterleave_Type = Integer32
_AdlbAtucNcdInterleave_Object = MibTableColumn
adlbAtucNcdInterleave = _AdlbAtucNcdInterleave_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 14, 1, 3),
    _AdlbAtucNcdInterleave_Type()
)
adlbAtucNcdInterleave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAtucNcdInterleave.setStatus("mandatory")
_AdlbAtucNcdFast_Type = Integer32
_AdlbAtucNcdFast_Object = MibTableColumn
adlbAtucNcdFast = _AdlbAtucNcdFast_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 14, 1, 4),
    _AdlbAtucNcdFast_Type()
)
adlbAtucNcdFast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAtucNcdFast.setStatus("mandatory")
_AdlbAtucOcdInterleave_Type = Integer32
_AdlbAtucOcdInterleave_Object = MibTableColumn
adlbAtucOcdInterleave = _AdlbAtucOcdInterleave_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 14, 1, 5),
    _AdlbAtucOcdInterleave_Type()
)
adlbAtucOcdInterleave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAtucOcdInterleave.setStatus("mandatory")
_AdlbAtucOcdFast_Type = Integer32
_AdlbAtucOcdFast_Object = MibTableColumn
adlbAtucOcdFast = _AdlbAtucOcdFast_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 14, 1, 6),
    _AdlbAtucOcdFast_Type()
)
adlbAtucOcdFast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAtucOcdFast.setStatus("mandatory")
_AdlbAtucLcdInterleave_Type = Integer32
_AdlbAtucLcdInterleave_Object = MibTableColumn
adlbAtucLcdInterleave = _AdlbAtucLcdInterleave_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 14, 1, 7),
    _AdlbAtucLcdInterleave_Type()
)
adlbAtucLcdInterleave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAtucLcdInterleave.setStatus("mandatory")
_AdlbAtucLcdFast_Type = Integer32
_AdlbAtucLcdFast_Object = MibTableColumn
adlbAtucLcdFast = _AdlbAtucLcdFast_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 14, 1, 8),
    _AdlbAtucLcdFast_Type()
)
adlbAtucLcdFast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAtucLcdFast.setStatus("mandatory")
_HwMusaAdlbAturAtmDefectTable_Object = MibTable
hwMusaAdlbAturAtmDefectTable = _HwMusaAdlbAturAtmDefectTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 15)
)
if mibBuilder.loadTexts:
    hwMusaAdlbAturAtmDefectTable.setStatus("mandatory")
_HwMusaAdlbAturAtmDefectEntry_Object = MibTableRow
hwMusaAdlbAturAtmDefectEntry = _HwMusaAdlbAturAtmDefectEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 15, 1)
)
hwMusaAdlbAturAtmDefectEntry.setIndexNames(
    (0, "HUAWEI-MUSA-MA5100-CONFMIB", "hwMusaFrameIndex"),
    (0, "HUAWEI-MUSA-MA5100-CONFMIB", "hwMusaSlotIndex"),
    (0, "HUAWEI-MUSA-MA5100-CONFMIB", "adlbPortIndex"),
)
if mibBuilder.loadTexts:
    hwMusaAdlbAturAtmDefectEntry.setStatus("mandatory")
_AdlbAturHecInterleave_Type = Integer32
_AdlbAturHecInterleave_Object = MibTableColumn
adlbAturHecInterleave = _AdlbAturHecInterleave_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 15, 1, 1),
    _AdlbAturHecInterleave_Type()
)
adlbAturHecInterleave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAturHecInterleave.setStatus("mandatory")
_AdlbAturHecFast_Type = Integer32
_AdlbAturHecFast_Object = MibTableColumn
adlbAturHecFast = _AdlbAturHecFast_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 15, 1, 2),
    _AdlbAturHecFast_Type()
)
adlbAturHecFast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAturHecFast.setStatus("mandatory")
_AdlbAturNcdInterleave_Type = Integer32
_AdlbAturNcdInterleave_Object = MibTableColumn
adlbAturNcdInterleave = _AdlbAturNcdInterleave_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 15, 1, 3),
    _AdlbAturNcdInterleave_Type()
)
adlbAturNcdInterleave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAturNcdInterleave.setStatus("mandatory")
_AdlbAturNcdFast_Type = Integer32
_AdlbAturNcdFast_Object = MibTableColumn
adlbAturNcdFast = _AdlbAturNcdFast_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 15, 1, 4),
    _AdlbAturNcdFast_Type()
)
adlbAturNcdFast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAturNcdFast.setStatus("mandatory")
_AdlbAturOcdInterleave_Type = Integer32
_AdlbAturOcdInterleave_Object = MibTableColumn
adlbAturOcdInterleave = _AdlbAturOcdInterleave_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 15, 1, 5),
    _AdlbAturOcdInterleave_Type()
)
adlbAturOcdInterleave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAturOcdInterleave.setStatus("mandatory")
_AdlbAturOcdFast_Type = Integer32
_AdlbAturOcdFast_Object = MibTableColumn
adlbAturOcdFast = _AdlbAturOcdFast_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 15, 1, 6),
    _AdlbAturOcdFast_Type()
)
adlbAturOcdFast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAturOcdFast.setStatus("mandatory")
_AdlbAturLcdInterleave_Type = Integer32
_AdlbAturLcdInterleave_Object = MibTableColumn
adlbAturLcdInterleave = _AdlbAturLcdInterleave_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 15, 1, 7),
    _AdlbAturLcdInterleave_Type()
)
adlbAturLcdInterleave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAturLcdInterleave.setStatus("mandatory")
_AdlbAturLcdFast_Type = Integer32
_AdlbAturLcdFast_Object = MibTableColumn
adlbAturLcdFast = _AdlbAturLcdFast_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 15, 1, 8),
    _AdlbAturLcdFast_Type()
)
adlbAturLcdFast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbAturLcdFast.setStatus("mandatory")
_HwMusaAdlbPortBitsTable_Object = MibTable
hwMusaAdlbPortBitsTable = _HwMusaAdlbPortBitsTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 16)
)
if mibBuilder.loadTexts:
    hwMusaAdlbPortBitsTable.setStatus("mandatory")
_HwMusaAdlbPortBitsEntry_Object = MibTableRow
hwMusaAdlbPortBitsEntry = _HwMusaAdlbPortBitsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 16, 1)
)
hwMusaAdlbPortBitsEntry.setIndexNames(
    (0, "HUAWEI-MUSA-MA5100-CONFMIB", "hwMusaFrameIndex"),
    (0, "HUAWEI-MUSA-MA5100-CONFMIB", "hwMusaSlotIndex"),
    (0, "HUAWEI-MUSA-MA5100-CONFMIB", "adlbPortIndex"),
)
if mibBuilder.loadTexts:
    hwMusaAdlbPortBitsEntry.setStatus("mandatory")
_AdlbDnBitsPerFrame_Type = Integer32
_AdlbDnBitsPerFrame_Object = MibTableColumn
adlbDnBitsPerFrame = _AdlbDnBitsPerFrame_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 16, 1, 1),
    _AdlbDnBitsPerFrame_Type()
)
adlbDnBitsPerFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbDnBitsPerFrame.setStatus("mandatory")
_AdlbUpBitsPerFrame_Type = Integer32
_AdlbUpBitsPerFrame_Object = MibTableColumn
adlbUpBitsPerFrame = _AdlbUpBitsPerFrame_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 16, 1, 2),
    _AdlbUpBitsPerFrame_Type()
)
adlbUpBitsPerFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbUpBitsPerFrame.setStatus("mandatory")
_AdlbDnBitAllocate_Type = DisplayString
_AdlbDnBitAllocate_Object = MibTableColumn
adlbDnBitAllocate = _AdlbDnBitAllocate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 16, 1, 3),
    _AdlbDnBitAllocate_Type()
)
adlbDnBitAllocate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbDnBitAllocate.setStatus("mandatory")
_AdlbUpBitAllocate_Type = DisplayString
_AdlbUpBitAllocate_Object = MibTableColumn
adlbUpBitAllocate = _AdlbUpBitAllocate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 16, 1, 4),
    _AdlbUpBitAllocate_Type()
)
adlbUpBitAllocate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbUpBitAllocate.setStatus("mandatory")
_HwMusaAdlbCarrierSnrTable_Object = MibTable
hwMusaAdlbCarrierSnrTable = _HwMusaAdlbCarrierSnrTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 17)
)
if mibBuilder.loadTexts:
    hwMusaAdlbCarrierSnrTable.setStatus("mandatory")
_HwMusaAdlbCarrierSnrEntry_Object = MibTableRow
hwMusaAdlbCarrierSnrEntry = _HwMusaAdlbCarrierSnrEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 17, 1)
)
hwMusaAdlbCarrierSnrEntry.setIndexNames(
    (0, "HUAWEI-MUSA-MA5100-CONFMIB", "hwMusaFrameIndex"),
    (0, "HUAWEI-MUSA-MA5100-CONFMIB", "hwMusaSlotIndex"),
    (0, "HUAWEI-MUSA-MA5100-CONFMIB", "adlbPortIndex"),
)
if mibBuilder.loadTexts:
    hwMusaAdlbCarrierSnrEntry.setStatus("mandatory")
_AdlbDnSnrAllocate_Type = DisplayString
_AdlbDnSnrAllocate_Object = MibTableColumn
adlbDnSnrAllocate = _AdlbDnSnrAllocate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 17, 1, 1),
    _AdlbDnSnrAllocate_Type()
)
adlbDnSnrAllocate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbDnSnrAllocate.setStatus("mandatory")
_AdlbUpSnrAllocate_Type = DisplayString
_AdlbUpSnrAllocate_Object = MibTableColumn
adlbUpSnrAllocate = _AdlbUpSnrAllocate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 4, 17, 1, 2),
    _AdlbUpSnrAllocate_Type()
)
adlbUpSnrAllocate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adlbUpSnrAllocate.setStatus("mandatory")
_HwMusaAdlbTest_ObjectIdentity = ObjectIdentity
hwMusaAdlbTest = _HwMusaAdlbTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 5)
)
_HwMusaAdlbPortTestTable_Object = MibTable
hwMusaAdlbPortTestTable = _HwMusaAdlbPortTestTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 5, 1)
)
if mibBuilder.loadTexts:
    hwMusaAdlbPortTestTable.setStatus("mandatory")
_HwMusaAdlbPortTestEntry_Object = MibTableRow
hwMusaAdlbPortTestEntry = _HwMusaAdlbPortTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 5, 1, 1)
)
hwMusaAdlbPortTestEntry.setIndexNames(
    (0, "HUAWEI-MUSA-MA5100-CONFMIB", "hwMusaFrameIndex"),
    (0, "HUAWEI-MUSA-MA5100-CONFMIB", "hwMusaSlotIndex"),
    (0, "HUAWEI-MUSA-MA5100-CONFMIB", "adlbPortIndex"),
)
if mibBuilder.loadTexts:
    hwMusaAdlbPortTestEntry.setStatus("mandatory")


class _AdlbPortTestOper_Type(Integer32):
    """Custom type adlbPortTestOper based on Integer32"""
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
        *(("atmLoop", 1),
          ("aturAutoLoop", 6),
          ("aturChgLoopParam", 7),
          ("aturErrCrc", 2),
          ("sendErrCrc", 4),
          ("stopAturErrCrc", 3),
          ("stopSendErrCrc", 5))
    )


_AdlbPortTestOper_Type.__name__ = "Integer32"
_AdlbPortTestOper_Object = MibTableColumn
adlbPortTestOper = _AdlbPortTestOper_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 6, 5, 1, 1, 1),
    _AdlbPortTestOper_Type()
)
adlbPortTestOper.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    adlbPortTestOper.setStatus("mandatory")
_HwMusaEndOfMib_ObjectIdentity = ObjectIdentity
hwMusaEndOfMib = _HwMusaEndOfMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 100)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-MUSA-MA5100-CONFMIB",
    **{"DisplayString": DisplayString,
       "hwMa5100Mib": hwMa5100Mib,
       "hwMusaSysMib": hwMusaSysMib,
       "hwMusaSlotGroup": hwMusaSlotGroup,
       "hwMusaFrame": hwMusaFrame,
       "hwMusaFrameNumber": hwMusaFrameNumber,
       "hwMusaFrameConfTable": hwMusaFrameConfTable,
       "hwMusaFrameConfEntry": hwMusaFrameConfEntry,
       "hwMusaFrameIndex": hwMusaFrameIndex,
       "hwMusaSlot": hwMusaSlot,
       "hwMusaSlotConfTable": hwMusaSlotConfTable,
       "hwMusaSlotConfEntry": hwMusaSlotConfEntry,
       "hwMusaSlotIndex": hwMusaSlotIndex,
       "hwMusaRegionPvcConfTable": hwMusaRegionPvcConfTable,
       "hwMusaRegionPvcConfEntry": hwMusaRegionPvcConfEntry,
       "hwMusaVlanId": hwMusaVlanId,
       "hwMusaVlanIciIndex": hwMusaVlanIciIndex,
       "hwMusaAdlFrameId": hwMusaAdlFrameId,
       "hwMusaAdlSlotId": hwMusaAdlSlotId,
       "hwMusaAdlPortId": hwMusaAdlPortId,
       "hwMusaAdlVpi": hwMusaAdlVpi,
       "hwMusaAdlVci": hwMusaAdlVci,
       "hwMusaToLanTrafficId": hwMusaToLanTrafficId,
       "hwMusaFromLanTrafficId": hwMusaFromLanTrafficId,
       "hwMusaAdlPortOperat": hwMusaAdlPortOperat,
       "hwMusaAllPvcConfTable": hwMusaAllPvcConfTable,
       "hwMusaAllPvcConfEntry": hwMusaAllPvcConfEntry,
       "hwMusaCidIndex": hwMusaCidIndex,
       "hwMusaSrcFrameId": hwMusaSrcFrameId,
       "hwMuasSrcSlotId": hwMuasSrcSlotId,
       "hwMusaSrcPortVlanVccId": hwMusaSrcPortVlanVccId,
       "hwMusaSrcBoardVpi": hwMusaSrcBoardVpi,
       "hwMusaSrcBoardVci": hwMusaSrcBoardVci,
       "hwMusaSrcUpcEpdPpd": hwMusaSrcUpcEpdPpd,
       "hwMusaDestFrameId": hwMusaDestFrameId,
       "hwMusaDestSlotId": hwMusaDestSlotId,
       "hwMusaDestPortVlanVccId": hwMusaDestPortVlanVccId,
       "hwMusaDestBoardVpi": hwMusaDestBoardVpi,
       "hwMusaDestBoardVci": hwMusaDestBoardVci,
       "hwMusaDestUpcEpdPpd": hwMusaDestUpcEpdPpd,
       "hwMusaSrcToDestTraffic": hwMusaSrcToDestTraffic,
       "hwMusaDestToSrcTraffic": hwMusaDestToSrcTraffic,
       "hwMusaAllPvcOperater": hwMusaAllPvcOperater,
       "hwMusaTypeOfPvcPvpindex": hwMusaTypeOfPvcPvpindex,
       "hwMusaPvcPvpState": hwMusaPvcPvpState,
       "hwMusaAdlb": hwMusaAdlb,
       "hwMusaAdlbBoard": hwMusaAdlbBoard,
       "hwMusaAdlbBoardInfoTable": hwMusaAdlbBoardInfoTable,
       "hwMusaAdlbBoardInfoEntry": hwMusaAdlbBoardInfoEntry,
       "adlbProductId": adlbProductId,
       "adlbCustomId": adlbCustomId,
       "adlbAtucRomSwVer": adlbAtucRomSwVer,
       "adlbAtucRomSwBuildDate": adlbAtucRomSwBuildDate,
       "adlbAtucOamSwVer": adlbAtucOamSwVer,
       "adlbAtucOamSwBuildDate": adlbAtucOamSwBuildDate,
       "adlbByDiagCodeVer": adlbByDiagCodeVer,
       "adlbByModemCodeVer": adlbByModemCodeVer,
       "adlbAtucVendorId": adlbAtucVendorId,
       "adlbAtucVersionNo": adlbAtucVersionNo,
       "adlbItuCountryCode": adlbItuCountryCode,
       "adlbItuProviderCode": adlbItuProviderCode,
       "hwMusaAdlbChipset": hwMusaAdlbChipset,
       "hwMusaAdlbChipsetMtTable": hwMusaAdlbChipsetMtTable,
       "hwMusaAdlbChipsetMtEntry": hwMusaAdlbChipsetMtEntry,
       "adlbChipsetIndex": adlbChipsetIndex,
       "adlbChipsetOper": adlbChipsetOper,
       "hwMusaAdlbConf": hwMusaAdlbConf,
       "hwMusaAdlbPortDeviceTable": hwMusaAdlbPortDeviceTable,
       "hwMusaAdlbPortDeviceEntry": hwMusaAdlbPortDeviceEntry,
       "adlbPortIndex": adlbPortIndex,
       "adlbAturVendorId": adlbAturVendorId,
       "adlbAturVersion": adlbAturVersion,
       "adlbAturCountryCode": adlbAturCountryCode,
       "adlbAturProviderCode": adlbAturProviderCode,
       "adlbAturAdslCapability": adlbAturAdslCapability,
       "hwMusaAdlbPortTable": hwMusaAdlbPortTable,
       "hwMusaAdlbPortEntry": hwMusaAdlbPortEntry,
       "adlbPortState": adlbPortState,
       "adlbPortTrainStandard": adlbPortTrainStandard,
       "adlbPortOper": adlbPortOper,
       "adlbPortTemplateId": adlbPortTemplateId,
       "adlbPortTxCell": adlbPortTxCell,
       "adlbPortRxCell": adlbPortRxCell,
       "hwMusaAdlbPortActTable": hwMusaAdlbPortActTable,
       "hwMusaAdlbPortActEntry": hwMusaAdlbPortActEntry,
       "adlbIfConfigSetToDefault": adlbIfConfigSetToDefault,
       "adlbServiceType": adlbServiceType,
       "adlbConfigOrAutoDelay": adlbConfigOrAutoDelay,
       "adlbDelayOrDepth": adlbDelayOrDepth,
       "adlbFrameMode": adlbFrameMode,
       "adlbNTROptionEnable": adlbNTROptionEnable,
       "adlbTrellisModeEnable": adlbTrellisModeEnable,
       "adlbEocClearChannelMode": adlbEocClearChannelMode,
       "adlbDsSingleOrDual": adlbDsSingleOrDual,
       "adlbUsSingleOrDual": adlbUsSingleOrDual,
       "adlbFastOrInterleave": adlbFastOrInterleave,
       "adlbDsTargetMargin": adlbDsTargetMargin,
       "adlbDsMinMargin": adlbDsMinMargin,
       "adlbUsTargetMargin": adlbUsTargetMargin,
       "adlbUsMinMargin": adlbUsMinMargin,
       "adlbMaxDsRateC0": adlbMaxDsRateC0,
       "adlbMinDsRateC0": adlbMinDsRateC0,
       "adlbMaxUsRateC0": adlbMaxUsRateC0,
       "adlbMinUsRateC0": adlbMinUsRateC0,
       "adlbUsMsOrDmtNumber": adlbUsMsOrDmtNumber,
       "adlbDsMsOrDmtNumber": adlbDsMsOrDmtNumber,
       "adlbUsExcessRatio": adlbUsExcessRatio,
       "adlbDsExcessRatio": adlbDsExcessRatio,
       "adlbMaxDsRateC1": adlbMaxDsRateC1,
       "adlbMinDsRateC1": adlbMinDsRateC1,
       "adlbMaxUsRateC1": adlbMaxUsRateC1,
       "adlbMinUsRateC1": adlbMinUsRateC1,
       "adlbTemplateOperate": adlbTemplateOperate,
       "hwMusaAdlbPortPfmThresTable": hwMusaAdlbPortPfmThresTable,
       "hwMusaAdlbPortPfmThresEntry": hwMusaAdlbPortPfmThresEntry,
       "adlbPortPfmThresId1": adlbPortPfmThresId1,
       "adlbPortPfmThresValue1": adlbPortPfmThresValue1,
       "adlbPortPfmThresId2": adlbPortPfmThresId2,
       "adlbPortPfmThresValue2": adlbPortPfmThresValue2,
       "adlbPortPfmThresId3": adlbPortPfmThresId3,
       "adlbPortPfmThresValue3": adlbPortPfmThresValue3,
       "adlbPortPfmThresId4": adlbPortPfmThresId4,
       "adlbPortPfmThresValue4": adlbPortPfmThresValue4,
       "adlbPortPfmThresId5": adlbPortPfmThresId5,
       "adlbPortPfmThresValue5": adlbPortPfmThresValue5,
       "adlbPortPfmThresId6": adlbPortPfmThresId6,
       "adlbPortPfmThresValue6": adlbPortPfmThresValue6,
       "adlbPortPfmThresId7": adlbPortPfmThresId7,
       "adlbPortPfmThresValue7": adlbPortPfmThresValue7,
       "adlbPortPfmThresId8": adlbPortPfmThresId8,
       "adlbPortPfmThresValue8": adlbPortPfmThresValue8,
       "hwMusaAdlbPfm": hwMusaAdlbPfm,
       "hwMusaAdlbPortLineDataTable": hwMusaAdlbPortLineDataTable,
       "hwMusaAdlbPortLineDataEntry": hwMusaAdlbPortLineDataEntry,
       "adlbAs0DnRate": adlbAs0DnRate,
       "adlbLs0DnRate": adlbLs0DnRate,
       "adlbAs1DnRate": adlbAs1DnRate,
       "adlbLs0UpRate": adlbLs0UpRate,
       "adlbLs1UpRate": adlbLs1UpRate,
       "adlbUpInterleaveDelay": adlbUpInterleaveDelay,
       "adlbDnInterleaveDelay": adlbDnInterleaveDelay,
       "adlbDnNoiseMargin": adlbDnNoiseMargin,
       "adlbUpNoiseMargin": adlbUpNoiseMargin,
       "adlbDnAttenuation": adlbDnAttenuation,
       "adlbUpAttenuation": adlbUpAttenuation,
       "adlbDnParityInterleave": adlbDnParityInterleave,
       "adlbDnParityFast": adlbDnParityFast,
       "adlbUpParityInterleave": adlbUpParityInterleave,
       "adlbUpParityFast": adlbUpParityFast,
       "adlbDnSymbolPerCodeInterleave": adlbDnSymbolPerCodeInterleave,
       "adlbDnSymbolPerCodeFast": adlbDnSymbolPerCodeFast,
       "adlbUpSymbolPerCodeInterleave": adlbUpSymbolPerCodeInterleave,
       "adlbUpSymbolPerCodeFast": adlbUpSymbolPerCodeFast,
       "adlbDnInterleaveDepth": adlbDnInterleaveDepth,
       "adlbUpInterleaveDepth": adlbUpInterleaveDepth,
       "adlbMaxDnAttainableRate": adlbMaxDnAttainableRate,
       "adlbMaxUpAttainableRate": adlbMaxUpAttainableRate,
       "adlbTotalOutputPower": adlbTotalOutputPower,
       "hwMusaAdlbAtucAlarmDataTable": hwMusaAdlbAtucAlarmDataTable,
       "hwMusaAdlbAtucAlarmDataEntry": hwMusaAdlbAtucAlarmDataEntry,
       "adlbAtucLos": adlbAtucLos,
       "adlbAtucHighBitErr": adlbAtucHighBitErr,
       "adlbAtucRetrain": adlbAtucRetrain,
       "adlbAtucLof": adlbAtucLof,
       "adlbAtucAlarmValidIntervals": adlbAtucAlarmValidIntervals,
       "adlbAtucPrev15MinLos": adlbAtucPrev15MinLos,
       "adlbAtucPrev15MinHighBitErr": adlbAtucPrev15MinHighBitErr,
       "adlbAtucPrev15MinRetrain": adlbAtucPrev15MinRetrain,
       "adlbAtucPrev15MinLof": adlbAtucPrev15MinLof,
       "adlbAtucCurr1DayLos": adlbAtucCurr1DayLos,
       "adlbAtucCurr1DayHighBitErr": adlbAtucCurr1DayHighBitErr,
       "adlbAtucCurr1DayRetrain": adlbAtucCurr1DayRetrain,
       "adlbAtucCurr1DayLof": adlbAtucCurr1DayLof,
       "adlbAtucPrev1DayLos": adlbAtucPrev1DayLos,
       "adlbAtucPrev1DayHighBitErr": adlbAtucPrev1DayHighBitErr,
       "adlbAtucPrev1DayRetrain": adlbAtucPrev1DayRetrain,
       "adlbAtucPrev1DayLof": adlbAtucPrev1DayLof,
       "adlbClearAlarmstatistics": adlbClearAlarmstatistics,
       "hwMusaAdlbAturAlarmDataTable": hwMusaAdlbAturAlarmDataTable,
       "hwMusaAdlbAturAlarmDataEntry": hwMusaAdlbAturAlarmDataEntry,
       "adlbAturLos": adlbAturLos,
       "adlbAturHighBitErr": adlbAturHighBitErr,
       "adlbAturRfi": adlbAturRfi,
       "adlbAturLpr": adlbAturLpr,
       "adlbAturAlarmValidIntervals": adlbAturAlarmValidIntervals,
       "adlbAturPrev15MinLos": adlbAturPrev15MinLos,
       "adlbAturPrev15MinHighBitErr": adlbAturPrev15MinHighBitErr,
       "adlbAturPrev15MinRfi": adlbAturPrev15MinRfi,
       "adlbAturPrev15MinLpr": adlbAturPrev15MinLpr,
       "adlbAturCurr1DayLos": adlbAturCurr1DayLos,
       "adlbAturCurr1DayHighBitErr": adlbAturCurr1DayHighBitErr,
       "adlbAturCurr1DayRfi": adlbAturCurr1DayRfi,
       "adlbAturCurr1DayLpr": adlbAturCurr1DayLpr,
       "adlbAturPrev1DayLos": adlbAturPrev1DayLos,
       "adlbAturPrev1DayHighBitErr": adlbAturPrev1DayHighBitErr,
       "adlbAturPrev1DayRfi": adlbAturPrev1DayRfi,
       "adlbAturPrev1DayLpr": adlbAturPrev1DayLpr,
       "hwMusaAdlbAtucPerfDataTable": hwMusaAdlbAtucPerfDataTable,
       "hwMusaAdlbAtucPerfDataEntry": hwMusaAdlbAtucPerfDataEntry,
       "adlbAtucCrcErrInterleave": adlbAtucCrcErrInterleave,
       "adlbAtucCrcErrFast": adlbAtucCrcErrFast,
       "adlbAtucFecErrInterleave": adlbAtucFecErrInterleave,
       "adlbAtucFecErrFast": adlbAtucFecErrFast,
       "adlbAtucSuperFrameSent": adlbAtucSuperFrameSent,
       "adlbAtucSuperFrameReceived": adlbAtucSuperFrameReceived,
       "adlbAtucTimeCount": adlbAtucTimeCount,
       "adlbAtucErrFrames": adlbAtucErrFrames,
       "adlbAtucBgBENotSES": adlbAtucBgBENotSES,
       "adlbAtucErrSecond": adlbAtucErrSecond,
       "adlbAtucSevereErrSecond": adlbAtucSevereErrSecond,
       "adlbAtucNonSESFrames": adlbAtucNonSESFrames,
       "adlbAtucUnavailableSecond": adlbAtucUnavailableSecond,
       "adlbAtucBitswaps": adlbAtucBitswaps,
       "adlbAtucLossSecond": adlbAtucLossSecond,
       "adlbAtucFecSecond": adlbAtucFecSecond,
       "adlbAtucFastRetrain": adlbAtucFastRetrain,
       "adlbAtucFastRetrainFail": adlbAtucFastRetrainFail,
       "adlbAtucPerfValidIntervals": adlbAtucPerfValidIntervals,
       "adlbClearPerfstatistics": adlbClearPerfstatistics,
       "hwMusaAdlbAtucPerfPrev15mDataTable": hwMusaAdlbAtucPerfPrev15mDataTable,
       "hwMusaAdlbAtucPerfPrev15mDataEntry": hwMusaAdlbAtucPerfPrev15mDataEntry,
       "adlbAtucPrev15MinCrcErrInterleave": adlbAtucPrev15MinCrcErrInterleave,
       "adlbAtucPrev15MinCrcErrFast": adlbAtucPrev15MinCrcErrFast,
       "adlbAtucPrev15MinFecErrInterleave": adlbAtucPrev15MinFecErrInterleave,
       "adlbAtucPrev15MinFecErrFast": adlbAtucPrev15MinFecErrFast,
       "adlbAtucPrev15MinSuperFrameSent": adlbAtucPrev15MinSuperFrameSent,
       "adlbAtucPrev15MinSuperFrameReceived": adlbAtucPrev15MinSuperFrameReceived,
       "adlbAtucPrev15MinTimeCount": adlbAtucPrev15MinTimeCount,
       "adlbAtucPrev15MinErrFrames": adlbAtucPrev15MinErrFrames,
       "adlbAtucPrev15MinBgBENotSES": adlbAtucPrev15MinBgBENotSES,
       "adlbAtucPrev15MinErrSecond": adlbAtucPrev15MinErrSecond,
       "adlbAtucPrev15MinSevereErrSecond": adlbAtucPrev15MinSevereErrSecond,
       "adlbAtucPrev15MinNonSESFrames": adlbAtucPrev15MinNonSESFrames,
       "adlbAtucPrev15MinUnavailableSecond": adlbAtucPrev15MinUnavailableSecond,
       "adlbAtucPrev15MinBitswaps": adlbAtucPrev15MinBitswaps,
       "adlbAtucPrev15MinLossSecond": adlbAtucPrev15MinLossSecond,
       "adlbAtucPrev15MinFecSecond": adlbAtucPrev15MinFecSecond,
       "adlbAtucPrev15MinFastRetrain": adlbAtucPrev15MinFastRetrain,
       "adlbAtucPrev15MinFastRetrainFail": adlbAtucPrev15MinFastRetrainFail,
       "hwMusaAdlbAtucPerfCurr24hDataTable": hwMusaAdlbAtucPerfCurr24hDataTable,
       "hwMusaAdlbAtucPerfCurr24hDataEntry": hwMusaAdlbAtucPerfCurr24hDataEntry,
       "adlbAtucCurr1DayCrcErrInterleave": adlbAtucCurr1DayCrcErrInterleave,
       "adlbAtucCurr1DayCrcErrFast": adlbAtucCurr1DayCrcErrFast,
       "adlbAtucCurr1DayFecErrInterleave": adlbAtucCurr1DayFecErrInterleave,
       "adlbAtucCurr1DayFecErrFast": adlbAtucCurr1DayFecErrFast,
       "adlbAtucCurr1DaySuperFrameSent": adlbAtucCurr1DaySuperFrameSent,
       "adlbAtucCurr1DaySuperFrameReceived": adlbAtucCurr1DaySuperFrameReceived,
       "adlbAtucCurr1DayTimeCount": adlbAtucCurr1DayTimeCount,
       "adlbAtucCurr1DayErrFrames": adlbAtucCurr1DayErrFrames,
       "adlbAtucCurr1DayBgBENotSES": adlbAtucCurr1DayBgBENotSES,
       "adlbAtucCurr1DayErrSecond": adlbAtucCurr1DayErrSecond,
       "adlbAtucCurr1DaySevereErrSecond": adlbAtucCurr1DaySevereErrSecond,
       "adlbAtucCurr1DayNonSESFrames": adlbAtucCurr1DayNonSESFrames,
       "adlbAtucCurr1DayUnavailableSecond": adlbAtucCurr1DayUnavailableSecond,
       "adlbAtucCurr1DayBitswaps": adlbAtucCurr1DayBitswaps,
       "adlbAtucCurr1DayLossSecond": adlbAtucCurr1DayLossSecond,
       "adlbAtucCurr1DayFecSecond": adlbAtucCurr1DayFecSecond,
       "adlbAtucCurr1DayFastRetrain": adlbAtucCurr1DayFastRetrain,
       "adlbAtucCurr1DayFastRetrainFail": adlbAtucCurr1DayFastRetrainFail,
       "hwMusaAdlbAtucPerfPrev24hDataTable": hwMusaAdlbAtucPerfPrev24hDataTable,
       "hwMusaAdlbAtucPerfPrev24hDataEntry": hwMusaAdlbAtucPerfPrev24hDataEntry,
       "adlbAtucPrev1DayCrcErrInterleave": adlbAtucPrev1DayCrcErrInterleave,
       "adlbAtucPrev1DayCrcErrFast": adlbAtucPrev1DayCrcErrFast,
       "adlbAtucPrev1DayFecErrInterleave": adlbAtucPrev1DayFecErrInterleave,
       "adlbAtucPrev1DayFecErrFast": adlbAtucPrev1DayFecErrFast,
       "adlbAtucPrev1DaySuperFrameSent": adlbAtucPrev1DaySuperFrameSent,
       "adlbAtucPrev1DaySuperFrameReceived": adlbAtucPrev1DaySuperFrameReceived,
       "adlbAtucPrev1DayTimeCount": adlbAtucPrev1DayTimeCount,
       "adlbAtucPrev1DayErrFrames": adlbAtucPrev1DayErrFrames,
       "adlbAtucPrev1DayBgBENotSES": adlbAtucPrev1DayBgBENotSES,
       "adlbAtucPrev1DayErrSecond": adlbAtucPrev1DayErrSecond,
       "adlbAtucPrev1DaySevereErrSecond": adlbAtucPrev1DaySevereErrSecond,
       "adlbAtucPrev1DayNonSESFrames": adlbAtucPrev1DayNonSESFrames,
       "adlbAtucPrev1DayUnavailableSecond": adlbAtucPrev1DayUnavailableSecond,
       "adlbAtucPrev1DayBitswaps": adlbAtucPrev1DayBitswaps,
       "adlbAtucPrev1DayLossSecond": adlbAtucPrev1DayLossSecond,
       "adlbAtucPrev1DayFecSecond": adlbAtucPrev1DayFecSecond,
       "adlbAtucPrev1DayFastRetrain": adlbAtucPrev1DayFastRetrain,
       "adlbAtucPrev1DayFastRetrainFail": adlbAtucPrev1DayFastRetrainFail,
       "hwMusaAdlbAturPerfDataTable": hwMusaAdlbAturPerfDataTable,
       "hwMusaAdlbAturPerfDataEntry": hwMusaAdlbAturPerfDataEntry,
       "adlbAturCrcErrInterleave": adlbAturCrcErrInterleave,
       "adlbAturCrcErrFast": adlbAturCrcErrFast,
       "adlbAturFecErrInterleave": adlbAturFecErrInterleave,
       "adlbAturFecErrFast": adlbAturFecErrFast,
       "adlbAturTimeCount": adlbAturTimeCount,
       "adlbAturErrFrames": adlbAturErrFrames,
       "adlbAturBgBENotSES": adlbAturBgBENotSES,
       "adlbAturErrSecond": adlbAturErrSecond,
       "adlbAturSevereErrSecond": adlbAturSevereErrSecond,
       "adlbAturNonSESFrames": adlbAturNonSESFrames,
       "adlbAturUnavailableSecond": adlbAturUnavailableSecond,
       "adlbAturLossSecond": adlbAturLossSecond,
       "adlbAturFecSecond": adlbAturFecSecond,
       "adlbAturPerfValidIntervals": adlbAturPerfValidIntervals,
       "hwMusaAdlbAturPerfPrev15mDataTable": hwMusaAdlbAturPerfPrev15mDataTable,
       "hwMusaAdlbAturPerfPrev15mDataEntry": hwMusaAdlbAturPerfPrev15mDataEntry,
       "adlbAturPrev15MinCrcErrInterleave": adlbAturPrev15MinCrcErrInterleave,
       "adlbAturPrev15MinCrcErrFast": adlbAturPrev15MinCrcErrFast,
       "adlbAturPrev15MinFecErrInterleave": adlbAturPrev15MinFecErrInterleave,
       "adlbAturPrev15MinFecErrFast": adlbAturPrev15MinFecErrFast,
       "adlbAturPrev15MinTimeCount": adlbAturPrev15MinTimeCount,
       "adlbAturPrev15MinErrFrames": adlbAturPrev15MinErrFrames,
       "adlbAturPrev15MinBgBENotSES": adlbAturPrev15MinBgBENotSES,
       "adlbAturPrev15MinErrSecond": adlbAturPrev15MinErrSecond,
       "adlbAturPrev15MinSevereErrSecond": adlbAturPrev15MinSevereErrSecond,
       "adlbAturPrev15MinNonSESFrames": adlbAturPrev15MinNonSESFrames,
       "adlbAturPrev15MinUnavailableSecond": adlbAturPrev15MinUnavailableSecond,
       "adlbAturPrev15MinLossSecond": adlbAturPrev15MinLossSecond,
       "adlbAturPrev15MinFecSecond": adlbAturPrev15MinFecSecond,
       "hwMusaAdlbAturPerfCurr24hDataTable": hwMusaAdlbAturPerfCurr24hDataTable,
       "hwMusaAdlbAturPerfCurr24hDataEntry": hwMusaAdlbAturPerfCurr24hDataEntry,
       "adlbAturCurr1DayCrcErrInterleave": adlbAturCurr1DayCrcErrInterleave,
       "adlbAturCurr1DayCrcErrFast": adlbAturCurr1DayCrcErrFast,
       "adlbAturCurr1DayFecErrInterleave": adlbAturCurr1DayFecErrInterleave,
       "adlbAturCurr1DayFecErrFast": adlbAturCurr1DayFecErrFast,
       "adlbAturCurr1DayTimeCount": adlbAturCurr1DayTimeCount,
       "adlbAturCurr1DayErrFrames": adlbAturCurr1DayErrFrames,
       "adlbAturCurr1DayBgBENotSES": adlbAturCurr1DayBgBENotSES,
       "adlbAturCurr1DayErrSecond": adlbAturCurr1DayErrSecond,
       "adlbAturCurr1DaySevereErrSecond": adlbAturCurr1DaySevereErrSecond,
       "adlbAturCurr1DayNonSESFrames": adlbAturCurr1DayNonSESFrames,
       "adlbAturCurr1DayUnavailableSecond": adlbAturCurr1DayUnavailableSecond,
       "adlbAturCurr1DayLossSecond": adlbAturCurr1DayLossSecond,
       "adlbAturCurr1DayFecSecond": adlbAturCurr1DayFecSecond,
       "hwMusaAdlbAturPerfPrev24hDataTable": hwMusaAdlbAturPerfPrev24hDataTable,
       "hwMusaAdlbAturPerfPrev24hDataEntry": hwMusaAdlbAturPerfPrev24hDataEntry,
       "adlbAturPrev1DayCrcErrInterleave": adlbAturPrev1DayCrcErrInterleave,
       "adlbAturPrev1DayCrcErrFast": adlbAturPrev1DayCrcErrFast,
       "adlbAturPrev1DayFecErrInterleave": adlbAturPrev1DayFecErrInterleave,
       "adlbAturPrev1DayFecErrFast": adlbAturPrev1DayFecErrFast,
       "adlbAturPrev1DayTimeCount": adlbAturPrev1DayTimeCount,
       "adlbAturPrev1DayErrFrames": adlbAturPrev1DayErrFrames,
       "adlbAturPrev1DayBgBENotSES": adlbAturPrev1DayBgBENotSES,
       "adlbAturPrev1DayErrSecond": adlbAturPrev1DayErrSecond,
       "adlbAturPrev1DaySevereErrSecond": adlbAturPrev1DaySevereErrSecond,
       "adlbAturPrev1DayNonSESFrames": adlbAturPrev1DayNonSESFrames,
       "adlbAturPrev1DayUnavailableSecond": adlbAturPrev1DayUnavailableSecond,
       "adlbAturPrev1DayLossSecond": adlbAturPrev1DayLossSecond,
       "adlbAturPrev1DayFecSecond": adlbAturPrev1DayFecSecond,
       "hwMusaAdlbAtucLineDefectTable": hwMusaAdlbAtucLineDefectTable,
       "hwMusaAdlbAtucLineDefectEntry": hwMusaAdlbAtucLineDefectEntry,
       "adlbAtucLpsState": adlbAtucLpsState,
       "adlbAtucSefState": adlbAtucSefState,
       "adlbAtucLosState": adlbAtucLosState,
       "adlbAtucLofState": adlbAtucLofState,
       "adlbAtucFebeInterleaveState": adlbAtucFebeInterleaveState,
       "adlbAtucFebeFastState": adlbAtucFebeFastState,
       "adlbAtucFecInterleaveState": adlbAtucFecInterleaveState,
       "adlbAtucFecFastState": adlbAtucFecFastState,
       "hwMusaAdlbAturLineDefectTable": hwMusaAdlbAturLineDefectTable,
       "hwMusaAdlbAturLineDefectEntry": hwMusaAdlbAturLineDefectEntry,
       "adlbAturLpsState": adlbAturLpsState,
       "adlbAturRdiState": adlbAturRdiState,
       "adlbAturLosState": adlbAturLosState,
       "adlbAturFriState": adlbAturFriState,
       "adlbAturFebeInterleaveState": adlbAturFebeInterleaveState,
       "adlbAturFebeFastState": adlbAturFebeFastState,
       "adlbAturFecInterleaveState": adlbAturFecInterleaveState,
       "adlbAturFecFastState": adlbAturFecFastState,
       "hwMusaAdlbAtucAtmDefectTable": hwMusaAdlbAtucAtmDefectTable,
       "hwMusaAdlbAtucAtmDefectEntry": hwMusaAdlbAtucAtmDefectEntry,
       "adlbAtucHecInterleave": adlbAtucHecInterleave,
       "adlbAtucHecFast": adlbAtucHecFast,
       "adlbAtucNcdInterleave": adlbAtucNcdInterleave,
       "adlbAtucNcdFast": adlbAtucNcdFast,
       "adlbAtucOcdInterleave": adlbAtucOcdInterleave,
       "adlbAtucOcdFast": adlbAtucOcdFast,
       "adlbAtucLcdInterleave": adlbAtucLcdInterleave,
       "adlbAtucLcdFast": adlbAtucLcdFast,
       "hwMusaAdlbAturAtmDefectTable": hwMusaAdlbAturAtmDefectTable,
       "hwMusaAdlbAturAtmDefectEntry": hwMusaAdlbAturAtmDefectEntry,
       "adlbAturHecInterleave": adlbAturHecInterleave,
       "adlbAturHecFast": adlbAturHecFast,
       "adlbAturNcdInterleave": adlbAturNcdInterleave,
       "adlbAturNcdFast": adlbAturNcdFast,
       "adlbAturOcdInterleave": adlbAturOcdInterleave,
       "adlbAturOcdFast": adlbAturOcdFast,
       "adlbAturLcdInterleave": adlbAturLcdInterleave,
       "adlbAturLcdFast": adlbAturLcdFast,
       "hwMusaAdlbPortBitsTable": hwMusaAdlbPortBitsTable,
       "hwMusaAdlbPortBitsEntry": hwMusaAdlbPortBitsEntry,
       "adlbDnBitsPerFrame": adlbDnBitsPerFrame,
       "adlbUpBitsPerFrame": adlbUpBitsPerFrame,
       "adlbDnBitAllocate": adlbDnBitAllocate,
       "adlbUpBitAllocate": adlbUpBitAllocate,
       "hwMusaAdlbCarrierSnrTable": hwMusaAdlbCarrierSnrTable,
       "hwMusaAdlbCarrierSnrEntry": hwMusaAdlbCarrierSnrEntry,
       "adlbDnSnrAllocate": adlbDnSnrAllocate,
       "adlbUpSnrAllocate": adlbUpSnrAllocate,
       "hwMusaAdlbTest": hwMusaAdlbTest,
       "hwMusaAdlbPortTestTable": hwMusaAdlbPortTestTable,
       "hwMusaAdlbPortTestEntry": hwMusaAdlbPortTestEntry,
       "adlbPortTestOper": adlbPortTestOper,
       "hwMusaEndOfMib": hwMusaEndOfMib}
)
