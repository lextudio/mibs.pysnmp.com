# SNMP MIB module (NSNICMIB-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NSNICMIB-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:29:34 2024
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

_Hp_ObjectIdentity = ObjectIdentity
hp = _Hp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11)
)
_Nm_ObjectIdentity = ObjectIdentity
nm = _Nm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2)
)
_Hpnsa_ObjectIdentity = ObjectIdentity
hpnsa = _Hpnsa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23)
)
_NicObject_ObjectIdentity = ObjectIdentity
nicObject = _NicObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18)
)
_NicDrvConfig_ObjectIdentity = ObjectIdentity
nicDrvConfig = _NicDrvConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 1)
)
_NicDrvConfigTable_Object = MibTable
nicDrvConfigTable = _NicDrvConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 1, 1)
)
if mibBuilder.loadTexts:
    nicDrvConfigTable.setStatus("mandatory")
_NicDrvConfigEntry_Object = MibTableRow
nicDrvConfigEntry = _NicDrvConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 1, 1, 1)
)
nicDrvConfigEntry.setIndexNames(
    (0, "NSNICMIB-MIB", "nicDrvConfigIndex"),
)
if mibBuilder.loadTexts:
    nicDrvConfigEntry.setStatus("mandatory")
_NicDrvConfigIndex_Type = Integer32
_NicDrvConfigIndex_Object = MibTableColumn
nicDrvConfigIndex = _NicDrvConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 1, 1, 1, 1),
    _NicDrvConfigIndex_Type()
)
nicDrvConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicDrvConfigIndex.setStatus("mandatory")


class _NicDrvcfgName_Type(DisplayString):
    """Custom type nicDrvcfgName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NicDrvcfgName_Type.__name__ = "DisplayString"
_NicDrvcfgName_Object = MibTableColumn
nicDrvcfgName = _NicDrvcfgName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 1, 1, 1, 2),
    _NicDrvcfgName_Type()
)
nicDrvcfgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicDrvcfgName.setStatus("mandatory")


class _NicDrvcfgDescript_Type(DisplayString):
    """Custom type nicDrvcfgDescript based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NicDrvcfgDescript_Type.__name__ = "DisplayString"
_NicDrvcfgDescript_Object = MibTableColumn
nicDrvcfgDescript = _NicDrvcfgDescript_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 1, 1, 1, 3),
    _NicDrvcfgDescript_Type()
)
nicDrvcfgDescript.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicDrvcfgDescript.setStatus("mandatory")


class _NicDrvcfgType_Type(Integer32):
    """Custom type nicDrvcfgType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("hp-busmaster", 3),
          ("hp-shasta", 4),
          ("hp-starfighter", 1),
          ("hp-twister", 2),
          ("unknown", 0))
    )


_NicDrvcfgType_Type.__name__ = "Integer32"
_NicDrvcfgType_Object = MibTableColumn
nicDrvcfgType = _NicDrvcfgType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 1, 1, 1, 4),
    _NicDrvcfgType_Type()
)
nicDrvcfgType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicDrvcfgType.setStatus("mandatory")


class _NicDrvcfgPhyAddr_Type(PhysAddress):
    """Custom type nicDrvcfgPhyAddr based on PhysAddress"""
    subtypeSpec = PhysAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_NicDrvcfgPhyAddr_Type.__name__ = "PhysAddress"
_NicDrvcfgPhyAddr_Object = MibTableColumn
nicDrvcfgPhyAddr = _NicDrvcfgPhyAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 1, 1, 1, 5),
    _NicDrvcfgPhyAddr_Type()
)
nicDrvcfgPhyAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicDrvcfgPhyAddr.setStatus("mandatory")


class _NicDrvcfgMajor_Type(Integer32):
    """Custom type nicDrvcfgMajor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NicDrvcfgMajor_Type.__name__ = "Integer32"
_NicDrvcfgMajor_Object = MibTableColumn
nicDrvcfgMajor = _NicDrvcfgMajor_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 1, 1, 1, 6),
    _NicDrvcfgMajor_Type()
)
nicDrvcfgMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicDrvcfgMajor.setStatus("mandatory")


class _NicDrvcfgMinor_Type(Integer32):
    """Custom type nicDrvcfgMinor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NicDrvcfgMinor_Type.__name__ = "Integer32"
_NicDrvcfgMinor_Object = MibTableColumn
nicDrvcfgMinor = _NicDrvcfgMinor_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 1, 1, 1, 7),
    _NicDrvcfgMinor_Type()
)
nicDrvcfgMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicDrvcfgMinor.setStatus("mandatory")


class _NicDrvcfgSlot_Type(Integer32):
    """Custom type nicDrvcfgSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_NicDrvcfgSlot_Type.__name__ = "Integer32"
_NicDrvcfgSlot_Object = MibTableColumn
nicDrvcfgSlot = _NicDrvcfgSlot_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 1, 1, 1, 8),
    _NicDrvcfgSlot_Type()
)
nicDrvcfgSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicDrvcfgSlot.setStatus("mandatory")


class _NicDrvcfgIOport0_Type(OctetString):
    """Custom type nicDrvcfgIOport0 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_NicDrvcfgIOport0_Type.__name__ = "OctetString"
_NicDrvcfgIOport0_Object = MibTableColumn
nicDrvcfgIOport0 = _NicDrvcfgIOport0_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 1, 1, 1, 9),
    _NicDrvcfgIOport0_Type()
)
nicDrvcfgIOport0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicDrvcfgIOport0.setStatus("mandatory")


class _NicDrvcfgIOport1_Type(OctetString):
    """Custom type nicDrvcfgIOport1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_NicDrvcfgIOport1_Type.__name__ = "OctetString"
_NicDrvcfgIOport1_Object = MibTableColumn
nicDrvcfgIOport1 = _NicDrvcfgIOport1_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 1, 1, 1, 10),
    _NicDrvcfgIOport1_Type()
)
nicDrvcfgIOport1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicDrvcfgIOport1.setStatus("mandatory")


class _NicDrvcfgInterrupt0_Type(Integer32):
    """Custom type nicDrvcfgInterrupt0 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            255
        )
    )
    namedValues = NamedValues(
        ("unused", 255)
    )


_NicDrvcfgInterrupt0_Type.__name__ = "Integer32"
_NicDrvcfgInterrupt0_Object = MibTableColumn
nicDrvcfgInterrupt0 = _NicDrvcfgInterrupt0_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 1, 1, 1, 11),
    _NicDrvcfgInterrupt0_Type()
)
nicDrvcfgInterrupt0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicDrvcfgInterrupt0.setStatus("mandatory")


class _NicDrvcfgInterrupt1_Type(Integer32):
    """Custom type nicDrvcfgInterrupt1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            255
        )
    )
    namedValues = NamedValues(
        ("unused", 255)
    )


_NicDrvcfgInterrupt1_Type.__name__ = "Integer32"
_NicDrvcfgInterrupt1_Object = MibTableColumn
nicDrvcfgInterrupt1 = _NicDrvcfgInterrupt1_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 1, 1, 1, 12),
    _NicDrvcfgInterrupt1_Type()
)
nicDrvcfgInterrupt1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicDrvcfgInterrupt1.setStatus("mandatory")


class _NicDrvcfgDMA0_Type(Integer32):
    """Custom type nicDrvcfgDMA0 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            255
        )
    )
    namedValues = NamedValues(
        ("unused", 255)
    )


_NicDrvcfgDMA0_Type.__name__ = "Integer32"
_NicDrvcfgDMA0_Object = MibTableColumn
nicDrvcfgDMA0 = _NicDrvcfgDMA0_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 1, 1, 1, 13),
    _NicDrvcfgDMA0_Type()
)
nicDrvcfgDMA0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicDrvcfgDMA0.setStatus("mandatory")


class _NicDrvcfgDMA1_Type(Integer32):
    """Custom type nicDrvcfgDMA1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            255
        )
    )
    namedValues = NamedValues(
        ("unused", 255)
    )


_NicDrvcfgDMA1_Type.__name__ = "Integer32"
_NicDrvcfgDMA1_Object = MibTableColumn
nicDrvcfgDMA1 = _NicDrvcfgDMA1_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 1, 1, 1, 14),
    _NicDrvcfgDMA1_Type()
)
nicDrvcfgDMA1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicDrvcfgDMA1.setStatus("mandatory")


class _NicDrvcfgMemory0_Type(OctetString):
    """Custom type nicDrvcfgMemory0 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_NicDrvcfgMemory0_Type.__name__ = "OctetString"
_NicDrvcfgMemory0_Object = MibTableColumn
nicDrvcfgMemory0 = _NicDrvcfgMemory0_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 1, 1, 1, 15),
    _NicDrvcfgMemory0_Type()
)
nicDrvcfgMemory0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicDrvcfgMemory0.setStatus("mandatory")


class _NicDrvcfgMemory1_Type(OctetString):
    """Custom type nicDrvcfgMemory1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_NicDrvcfgMemory1_Type.__name__ = "OctetString"
_NicDrvcfgMemory1_Object = MibTableColumn
nicDrvcfgMemory1 = _NicDrvcfgMemory1_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 1, 1, 1, 16),
    _NicDrvcfgMemory1_Type()
)
nicDrvcfgMemory1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicDrvcfgMemory1.setStatus("mandatory")


class _NicDrvcfgMulticast_Type(Integer32):
    """Custom type nicDrvcfgMulticast based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_NicDrvcfgMulticast_Type.__name__ = "Integer32"
_NicDrvcfgMulticast_Object = MibTableColumn
nicDrvcfgMulticast = _NicDrvcfgMulticast_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 1, 1, 1, 17),
    _NicDrvcfgMulticast_Type()
)
nicDrvcfgMulticast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicDrvcfgMulticast.setStatus("mandatory")


class _NicDrvcfgPromiscuous_Type(Integer32):
    """Custom type nicDrvcfgPromiscuous based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_NicDrvcfgPromiscuous_Type.__name__ = "Integer32"
_NicDrvcfgPromiscuous_Object = MibTableColumn
nicDrvcfgPromiscuous = _NicDrvcfgPromiscuous_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 1, 1, 1, 18),
    _NicDrvcfgPromiscuous_Type()
)
nicDrvcfgPromiscuous.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicDrvcfgPromiscuous.setStatus("mandatory")
_NicDrvcfgMaximumSize_Type = Integer32
_NicDrvcfgMaximumSize_Object = MibTableColumn
nicDrvcfgMaximumSize = _NicDrvcfgMaximumSize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 1, 1, 1, 19),
    _NicDrvcfgMaximumSize_Type()
)
nicDrvcfgMaximumSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicDrvcfgMaximumSize.setStatus("mandatory")
_NicDrvcfgSpeed_Type = Integer32
_NicDrvcfgSpeed_Object = MibTableColumn
nicDrvcfgSpeed = _NicDrvcfgSpeed_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 1, 1, 1, 20),
    _NicDrvcfgSpeed_Type()
)
nicDrvcfgSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicDrvcfgSpeed.setStatus("mandatory")
_NicDrvcfgTransportTime_Type = Integer32
_NicDrvcfgTransportTime_Object = MibTableColumn
nicDrvcfgTransportTime = _NicDrvcfgTransportTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 1, 1, 1, 21),
    _NicDrvcfgTransportTime_Type()
)
nicDrvcfgTransportTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicDrvcfgTransportTime.setStatus("mandatory")
_NicDrvcfgSendRetries_Type = Integer32
_NicDrvcfgSendRetries_Object = MibTableColumn
nicDrvcfgSendRetries = _NicDrvcfgSendRetries_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 1, 1, 1, 22),
    _NicDrvcfgSendRetries_Type()
)
nicDrvcfgSendRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicDrvcfgSendRetries.setStatus("mandatory")


class _NicDrvcfgMode_Type(Integer32):
    """Custom type nicDrvcfgMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("non-100VG", 0),
          ("vg-100", 1))
    )


_NicDrvcfgMode_Type.__name__ = "Integer32"
_NicDrvcfgMode_Object = MibTableColumn
nicDrvcfgMode = _NicDrvcfgMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 1, 1, 1, 23),
    _NicDrvcfgMode_Type()
)
nicDrvcfgMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicDrvcfgMode.setStatus("mandatory")
_NicDrvcfgBindFrames_Type = Integer32
_NicDrvcfgBindFrames_Object = MibScalar
nicDrvcfgBindFrames = _NicDrvcfgBindFrames_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 1, 1, 1, 24),
    _NicDrvcfgBindFrames_Type()
)
nicDrvcfgBindFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicDrvcfgBindFrames.setStatus("mandatory")


class _NicDrvcfgAftGroupId_Type(Integer32):
    """Custom type nicDrvcfgAftGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_NicDrvcfgAftGroupId_Type.__name__ = "Integer32"
_NicDrvcfgAftGroupId_Object = MibTableColumn
nicDrvcfgAftGroupId = _NicDrvcfgAftGroupId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 1, 1, 1, 25),
    _NicDrvcfgAftGroupId_Type()
)
nicDrvcfgAftGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicDrvcfgAftGroupId.setStatus("mandatory")


class _NicDrvcfgAftBusNo_Type(OctetString):
    """Custom type nicDrvcfgAftBusNo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_NicDrvcfgAftBusNo_Type.__name__ = "OctetString"
_NicDrvcfgAftBusNo_Object = MibTableColumn
nicDrvcfgAftBusNo = _NicDrvcfgAftBusNo_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 1, 1, 1, 26),
    _NicDrvcfgAftBusNo_Type()
)
nicDrvcfgAftBusNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicDrvcfgAftBusNo.setStatus("mandatory")


class _NicDrvcfgAftBusDeviceId_Type(OctetString):
    """Custom type nicDrvcfgAftBusDeviceId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_NicDrvcfgAftBusDeviceId_Type.__name__ = "OctetString"
_NicDrvcfgAftBusDeviceId_Object = MibTableColumn
nicDrvcfgAftBusDeviceId = _NicDrvcfgAftBusDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 1, 1, 1, 27),
    _NicDrvcfgAftBusDeviceId_Type()
)
nicDrvcfgAftBusDeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicDrvcfgAftBusDeviceId.setStatus("mandatory")


class _NicDrvcfgAftPciVenodrId_Type(OctetString):
    """Custom type nicDrvcfgAftPciVenodrId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_NicDrvcfgAftPciVenodrId_Type.__name__ = "OctetString"
_NicDrvcfgAftPciVenodrId_Object = MibScalar
nicDrvcfgAftPciVenodrId = _NicDrvcfgAftPciVenodrId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 1, 1, 1, 28),
    _NicDrvcfgAftPciVenodrId_Type()
)
nicDrvcfgAftPciVenodrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicDrvcfgAftPciVenodrId.setStatus("mandatory")


class _NicDrvcfgAftPciDeviceId_Type(OctetString):
    """Custom type nicDrvcfgAftPciDeviceId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_NicDrvcfgAftPciDeviceId_Type.__name__ = "OctetString"
_NicDrvcfgAftPciDeviceId_Object = MibTableColumn
nicDrvcfgAftPciDeviceId = _NicDrvcfgAftPciDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 1, 1, 1, 29),
    _NicDrvcfgAftPciDeviceId_Type()
)
nicDrvcfgAftPciDeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicDrvcfgAftPciDeviceId.setStatus("mandatory")


class _NicDrvcfgAftPciSubSysVendorId_Type(OctetString):
    """Custom type nicDrvcfgAftPciSubSysVendorId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_NicDrvcfgAftPciSubSysVendorId_Type.__name__ = "OctetString"
_NicDrvcfgAftPciSubSysVendorId_Object = MibTableColumn
nicDrvcfgAftPciSubSysVendorId = _NicDrvcfgAftPciSubSysVendorId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 1, 1, 1, 30),
    _NicDrvcfgAftPciSubSysVendorId_Type()
)
nicDrvcfgAftPciSubSysVendorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicDrvcfgAftPciSubSysVendorId.setStatus("mandatory")


class _NicDrvcfgAftPciSubSysDeviceId_Type(OctetString):
    """Custom type nicDrvcfgAftPciSubSysDeviceId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_NicDrvcfgAftPciSubSysDeviceId_Type.__name__ = "OctetString"
_NicDrvcfgAftPciSubSysDeviceId_Object = MibTableColumn
nicDrvcfgAftPciSubSysDeviceId = _NicDrvcfgAftPciSubSysDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 1, 1, 1, 31),
    _NicDrvcfgAftPciSubSysDeviceId_Type()
)
nicDrvcfgAftPciSubSysDeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicDrvcfgAftPciSubSysDeviceId.setStatus("mandatory")


class _NicDrvcfgAftStatus_Type(Integer32):
    """Custom type nicDrvcfgAftStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("failed", 2),
          ("standby", 0))
    )


_NicDrvcfgAftStatus_Type.__name__ = "Integer32"
_NicDrvcfgAftStatus_Object = MibTableColumn
nicDrvcfgAftStatus = _NicDrvcfgAftStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 1, 1, 1, 32),
    _NicDrvcfgAftStatus_Type()
)
nicDrvcfgAftStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicDrvcfgAftStatus.setStatus("mandatory")


class _NicDrvcfgAftMode_Type(Integer32):
    """Custom type nicDrvcfgAftMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 0))
    )


_NicDrvcfgAftMode_Type.__name__ = "Integer32"
_NicDrvcfgAftMode_Object = MibTableColumn
nicDrvcfgAftMode = _NicDrvcfgAftMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 1, 1, 1, 33),
    _NicDrvcfgAftMode_Type()
)
nicDrvcfgAftMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicDrvcfgAftMode.setStatus("mandatory")
_NicStatistics_ObjectIdentity = ObjectIdentity
nicStatistics = _NicStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 2)
)
_NicStatisticsTable_Object = MibTable
nicStatisticsTable = _NicStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 2, 1)
)
if mibBuilder.loadTexts:
    nicStatisticsTable.setStatus("mandatory")
_NicStatisticsEntry_Object = MibTableRow
nicStatisticsEntry = _NicStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 2, 1, 1)
)
nicStatisticsEntry.setIndexNames(
    (0, "NSNICMIB-MIB", "nicStatisticsIndex"),
)
if mibBuilder.loadTexts:
    nicStatisticsEntry.setStatus("mandatory")
_NicStatisticsIndex_Type = Integer32
_NicStatisticsIndex_Object = MibTableColumn
nicStatisticsIndex = _NicStatisticsIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 2, 1, 1, 1),
    _NicStatisticsIndex_Type()
)
nicStatisticsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicStatisticsIndex.setStatus("mandatory")
_NicTtlTxPacket_Type = Counter32
_NicTtlTxPacket_Object = MibTableColumn
nicTtlTxPacket = _NicTtlTxPacket_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 2, 1, 1, 2),
    _NicTtlTxPacket_Type()
)
nicTtlTxPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicTtlTxPacket.setStatus("mandatory")
_NicDeltaTtlTxPacket_Type = Integer32
_NicDeltaTtlTxPacket_Object = MibTableColumn
nicDeltaTtlTxPacket = _NicDeltaTtlTxPacket_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 2, 1, 1, 3),
    _NicDeltaTtlTxPacket_Type()
)
nicDeltaTtlTxPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicDeltaTtlTxPacket.setStatus("mandatory")
_NicTtlRxPacket_Type = Counter32
_NicTtlRxPacket_Object = MibTableColumn
nicTtlRxPacket = _NicTtlRxPacket_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 2, 1, 1, 4),
    _NicTtlRxPacket_Type()
)
nicTtlRxPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicTtlRxPacket.setStatus("mandatory")
_NicDeltaTtlRxPacket_Type = Integer32
_NicDeltaTtlRxPacket_Object = MibTableColumn
nicDeltaTtlRxPacket = _NicDeltaTtlRxPacket_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 2, 1, 1, 5),
    _NicDeltaTtlRxPacket_Type()
)
nicDeltaTtlRxPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicDeltaTtlRxPacket.setStatus("mandatory")
_NicGetECBFails_Type = Counter32
_NicGetECBFails_Object = MibTableColumn
nicGetECBFails = _NicGetECBFails_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 2, 1, 1, 6),
    _NicGetECBFails_Type()
)
nicGetECBFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicGetECBFails.setStatus("mandatory")
_NicTxTooBig_Type = Counter32
_NicTxTooBig_Object = MibTableColumn
nicTxTooBig = _NicTxTooBig_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 2, 1, 1, 7),
    _NicTxTooBig_Type()
)
nicTxTooBig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicTxTooBig.setStatus("mandatory")
_NicRxTooBig_Type = Counter32
_NicRxTooBig_Object = MibTableColumn
nicRxTooBig = _NicRxTooBig_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 2, 1, 1, 8),
    _NicRxTooBig_Type()
)
nicRxTooBig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicRxTooBig.setStatus("mandatory")
_NicRxOverflow_Type = Counter32
_NicRxOverflow_Object = MibTableColumn
nicRxOverflow = _NicRxOverflow_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 2, 1, 1, 9),
    _NicRxOverflow_Type()
)
nicRxOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicRxOverflow.setStatus("mandatory")
_NicTxMisc_Type = Counter32
_NicTxMisc_Object = MibTableColumn
nicTxMisc = _NicTxMisc_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 2, 1, 1, 10),
    _NicTxMisc_Type()
)
nicTxMisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicTxMisc.setStatus("mandatory")
_NicRxMisc_Type = Counter32
_NicRxMisc_Object = MibTableColumn
nicRxMisc = _NicRxMisc_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 2, 1, 1, 11),
    _NicRxMisc_Type()
)
nicRxMisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicRxMisc.setStatus("mandatory")
_NicRxCRC_Type = Counter32
_NicRxCRC_Object = MibTableColumn
nicRxCRC = _NicRxCRC_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 2, 1, 1, 12),
    _NicRxCRC_Type()
)
nicRxCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicRxCRC.setStatus("mandatory")
_NicTxOKByte_Type = Counter32
_NicTxOKByte_Object = MibTableColumn
nicTxOKByte = _NicTxOKByte_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 2, 1, 1, 13),
    _NicTxOKByte_Type()
)
nicTxOKByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicTxOKByte.setStatus("mandatory")
_NicDeltaTxOKByte_Type = Integer32
_NicDeltaTxOKByte_Object = MibTableColumn
nicDeltaTxOKByte = _NicDeltaTxOKByte_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 2, 1, 1, 14),
    _NicDeltaTxOKByte_Type()
)
nicDeltaTxOKByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicDeltaTxOKByte.setStatus("mandatory")
_NicRxOKByte_Type = Counter32
_NicRxOKByte_Object = MibTableColumn
nicRxOKByte = _NicRxOKByte_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 2, 1, 1, 15),
    _NicRxOKByte_Type()
)
nicRxOKByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicRxOKByte.setStatus("mandatory")
_NicDeltaRxOKByte_Type = Integer32
_NicDeltaRxOKByte_Object = MibTableColumn
nicDeltaRxOKByte = _NicDeltaRxOKByte_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 2, 1, 1, 16),
    _NicDeltaRxOKByte_Type()
)
nicDeltaRxOKByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicDeltaRxOKByte.setStatus("mandatory")
_NicTxGroup_Type = Counter32
_NicTxGroup_Object = MibTableColumn
nicTxGroup = _NicTxGroup_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 2, 1, 1, 17),
    _NicTxGroup_Type()
)
nicTxGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicTxGroup.setStatus("mandatory")
_NicDeltaTxGroup_Type = Integer32
_NicDeltaTxGroup_Object = MibTableColumn
nicDeltaTxGroup = _NicDeltaTxGroup_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 2, 1, 1, 18),
    _NicDeltaTxGroup_Type()
)
nicDeltaTxGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicDeltaTxGroup.setStatus("mandatory")
_NicRxGroup_Type = Counter32
_NicRxGroup_Object = MibTableColumn
nicRxGroup = _NicRxGroup_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 2, 1, 1, 19),
    _NicRxGroup_Type()
)
nicRxGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicRxGroup.setStatus("mandatory")
_NicDeltaRxGroup_Type = Integer32
_NicDeltaRxGroup_Object = MibTableColumn
nicDeltaRxGroup = _NicDeltaRxGroup_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 2, 1, 1, 20),
    _NicDeltaRxGroup_Type()
)
nicDeltaRxGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicDeltaRxGroup.setStatus("mandatory")
_NicAdapterReset_Type = Counter32
_NicAdapterReset_Object = MibTableColumn
nicAdapterReset = _NicAdapterReset_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 2, 1, 1, 21),
    _NicAdapterReset_Type()
)
nicAdapterReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicAdapterReset.setStatus("mandatory")
_NicQDepth_Type = Counter32
_NicQDepth_Object = MibTableColumn
nicQDepth = _NicQDepth_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 2, 1, 1, 22),
    _NicQDepth_Type()
)
nicQDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicQDepth.setStatus("mandatory")
_NicRcvBuffers_Type = Counter32
_NicRcvBuffers_Object = MibTableColumn
nicRcvBuffers = _NicRcvBuffers_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 2, 1, 1, 23),
    _NicRcvBuffers_Type()
)
nicRcvBuffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicRcvBuffers.setStatus("mandatory")
_NicRcvBuffers75Pct_Type = Counter32
_NicRcvBuffers75Pct_Object = MibTableColumn
nicRcvBuffers75Pct = _NicRcvBuffers75Pct_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 2, 1, 1, 24),
    _NicRcvBuffers75Pct_Type()
)
nicRcvBuffers75Pct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicRcvBuffers75Pct.setStatus("mandatory")
_NicRcvBuffersCkOut_Type = Counter32
_NicRcvBuffersCkOut_Object = MibTableColumn
nicRcvBuffersCkOut = _NicRcvBuffersCkOut_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 2, 1, 1, 25),
    _NicRcvBuffersCkOut_Type()
)
nicRcvBuffersCkOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicRcvBuffersCkOut.setStatus("mandatory")
_NicRcvBuffersMaxSize_Type = Integer32
_NicRcvBuffersMaxSize_Object = MibTableColumn
nicRcvBuffersMaxSize = _NicRcvBuffersMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 2, 1, 1, 26),
    _NicRcvBuffersMaxSize_Type()
)
nicRcvBuffersMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicRcvBuffersMaxSize.setStatus("mandatory")
_NicNumCustCounter_Type = Integer32
_NicNumCustCounter_Object = MibTableColumn
nicNumCustCounter = _NicNumCustCounter_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 2, 1, 1, 27),
    _NicNumCustCounter_Type()
)
nicNumCustCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicNumCustCounter.setStatus("mandatory")
_NicCustomStats_ObjectIdentity = ObjectIdentity
nicCustomStats = _NicCustomStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 3)
)
_NicCustStatTable_Object = MibTable
nicCustStatTable = _NicCustStatTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 3, 1)
)
if mibBuilder.loadTexts:
    nicCustStatTable.setStatus("mandatory")
_NicCustEntry_Object = MibTableRow
nicCustEntry = _NicCustEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 3, 1, 1)
)
nicCustEntry.setIndexNames(
    (0, "NSNICMIB-MIB", "nicCustIndex"),
    (0, "NSNICMIB-MIB", "nicIndex"),
)
if mibBuilder.loadTexts:
    nicCustEntry.setStatus("mandatory")
_NicCustIndex_Type = Integer32
_NicCustIndex_Object = MibTableColumn
nicCustIndex = _NicCustIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 3, 1, 1, 1),
    _NicCustIndex_Type()
)
nicCustIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicCustIndex.setStatus("mandatory")
_NicIndex_Type = Integer32
_NicIndex_Object = MibTableColumn
nicIndex = _NicIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 3, 1, 1, 2),
    _NicIndex_Type()
)
nicIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicIndex.setStatus("mandatory")
_NicCustCounter_Type = Counter32
_NicCustCounter_Object = MibTableColumn
nicCustCounter = _NicCustCounter_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 3, 1, 1, 3),
    _NicCustCounter_Type()
)
nicCustCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicCustCounter.setStatus("mandatory")


class _NicCustCounterString_Type(DisplayString):
    """Custom type nicCustCounterString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_NicCustCounterString_Type.__name__ = "DisplayString"
_NicCustCounterString_Object = MibTableColumn
nicCustCounterString = _NicCustCounterString_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 3, 1, 1, 4),
    _NicCustCounterString_Type()
)
nicCustCounterString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicCustCounterString.setStatus("mandatory")
_NicErrors_ObjectIdentity = ObjectIdentity
nicErrors = _NicErrors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 4)
)
_NicErrorsTable_Object = MibTable
nicErrorsTable = _NicErrorsTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 4, 1)
)
if mibBuilder.loadTexts:
    nicErrorsTable.setStatus("mandatory")
_NicErrorsEntry_Object = MibTableRow
nicErrorsEntry = _NicErrorsEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 4, 1, 1)
)
nicErrorsEntry.setIndexNames(
    (0, "NSNICMIB-MIB", "nicErrorsIndex"),
)
if mibBuilder.loadTexts:
    nicErrorsEntry.setStatus("mandatory")
_NicErrorsIndex_Type = Integer32
_NicErrorsIndex_Object = MibTableColumn
nicErrorsIndex = _NicErrorsIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 4, 1, 1, 1),
    _NicErrorsIndex_Type()
)
nicErrorsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicErrorsIndex.setStatus("mandatory")
_NicTxOKSingleCollision_Type = Counter32
_NicTxOKSingleCollision_Object = MibTableColumn
nicTxOKSingleCollision = _NicTxOKSingleCollision_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 4, 1, 1, 2),
    _NicTxOKSingleCollision_Type()
)
nicTxOKSingleCollision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicTxOKSingleCollision.setStatus("mandatory")
_NicTxOKMultipleCollision_Type = Counter32
_NicTxOKMultipleCollision_Object = MibTableColumn
nicTxOKMultipleCollision = _NicTxOKMultipleCollision_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 4, 1, 1, 3),
    _NicTxOKMultipleCollision_Type()
)
nicTxOKMultipleCollision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicTxOKMultipleCollision.setStatus("mandatory")
_NicTxOKDeferred_Type = Counter32
_NicTxOKDeferred_Object = MibTableColumn
nicTxOKDeferred = _NicTxOKDeferred_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 4, 1, 1, 4),
    _NicTxOKDeferred_Type()
)
nicTxOKDeferred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicTxOKDeferred.setStatus("mandatory")
_NicTxAbortLateCollision_Type = Counter32
_NicTxAbortLateCollision_Object = MibTableColumn
nicTxAbortLateCollision = _NicTxAbortLateCollision_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 4, 1, 1, 5),
    _NicTxAbortLateCollision_Type()
)
nicTxAbortLateCollision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicTxAbortLateCollision.setStatus("mandatory")
_NicTxAbortExcessCollision_Type = Counter32
_NicTxAbortExcessCollision_Object = MibTableColumn
nicTxAbortExcessCollision = _NicTxAbortExcessCollision_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 4, 1, 1, 6),
    _NicTxAbortExcessCollision_Type()
)
nicTxAbortExcessCollision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicTxAbortExcessCollision.setStatus("mandatory")
_NicTxAbortCarrierSense_Type = Counter32
_NicTxAbortCarrierSense_Object = MibTableColumn
nicTxAbortCarrierSense = _NicTxAbortCarrierSense_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 4, 1, 1, 7),
    _NicTxAbortCarrierSense_Type()
)
nicTxAbortCarrierSense.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicTxAbortCarrierSense.setStatus("mandatory")
_NicTxAbortExcessiveDeferral_Type = Counter32
_NicTxAbortExcessiveDeferral_Object = MibTableColumn
nicTxAbortExcessiveDeferral = _NicTxAbortExcessiveDeferral_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 4, 1, 1, 8),
    _NicTxAbortExcessiveDeferral_Type()
)
nicTxAbortExcessiveDeferral.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicTxAbortExcessiveDeferral.setStatus("mandatory")
_NicRxAbortFrameAlignment_Type = Counter32
_NicRxAbortFrameAlignment_Object = MibTableColumn
nicRxAbortFrameAlignment = _NicRxAbortFrameAlignment_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 4, 1, 1, 9),
    _NicRxAbortFrameAlignment_Type()
)
nicRxAbortFrameAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicRxAbortFrameAlignment.setStatus("mandatory")
_NicHWRxMismatch_Type = Counter32
_NicHWRxMismatch_Object = MibTableColumn
nicHWRxMismatch = _NicHWRxMismatch_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 4, 1, 1, 10),
    _NicHWRxMismatch_Type()
)
nicHWRxMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicHWRxMismatch.setStatus("mandatory")
_NicTtlTxErrPacket_Type = Integer32
_NicTtlTxErrPacket_Object = MibTableColumn
nicTtlTxErrPacket = _NicTtlTxErrPacket_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 4, 1, 1, 11),
    _NicTtlTxErrPacket_Type()
)
nicTtlTxErrPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicTtlTxErrPacket.setStatus("mandatory")
_NicTtlRxErrPacket_Type = Integer32
_NicTtlRxErrPacket_Object = MibTableColumn
nicTtlRxErrPacket = _NicTtlRxErrPacket_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 4, 1, 1, 12),
    _NicTtlRxErrPacket_Type()
)
nicTtlRxErrPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicTtlRxErrPacket.setStatus("mandatory")
_NicMiscellaneous_ObjectIdentity = ObjectIdentity
nicMiscellaneous = _NicMiscellaneous_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 5)
)
_NicNumBoards_Type = Integer32
_NicNumBoards_Object = MibScalar
nicNumBoards = _NicNumBoards_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 5, 1),
    _NicNumBoards_Type()
)
nicNumBoards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicNumBoards.setStatus("mandatory")
_NicAdapterType_Type = Integer32
_NicAdapterType_Object = MibScalar
nicAdapterType = _NicAdapterType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 5, 2),
    _NicAdapterType_Type()
)
nicAdapterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicAdapterType.setStatus("mandatory")
_NicFrameType_ObjectIdentity = ObjectIdentity
nicFrameType = _NicFrameType_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 6)
)
_NicFrameTypeTable_Object = MibTable
nicFrameTypeTable = _NicFrameTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 6, 1)
)
if mibBuilder.loadTexts:
    nicFrameTypeTable.setStatus("mandatory")
_NicFrameTypeEntry_Object = MibTableRow
nicFrameTypeEntry = _NicFrameTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 6, 1, 1)
)
nicFrameTypeEntry.setIndexNames(
    (0, "NSNICMIB-MIB", "nicFrameTypeIndex"),
    (0, "NSNICMIB-MIB", "nicCardIndex"),
)
if mibBuilder.loadTexts:
    nicFrameTypeEntry.setStatus("mandatory")
_NicFrameTypeIndex_Type = Integer32
_NicFrameTypeIndex_Object = MibTableColumn
nicFrameTypeIndex = _NicFrameTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 6, 1, 1, 1),
    _NicFrameTypeIndex_Type()
)
nicFrameTypeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicFrameTypeIndex.setStatus("mandatory")
_NicCardIndex_Type = Integer32
_NicCardIndex_Object = MibTableColumn
nicCardIndex = _NicCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 6, 1, 1, 2),
    _NicCardIndex_Type()
)
nicCardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicCardIndex.setStatus("mandatory")


class _NicFrameTypeString_Type(DisplayString):
    """Custom type nicFrameTypeString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_NicFrameTypeString_Type.__name__ = "DisplayString"
_NicFrameTypeString_Object = MibTableColumn
nicFrameTypeString = _NicFrameTypeString_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 6, 1, 1, 3),
    _NicFrameTypeString_Type()
)
nicFrameTypeString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicFrameTypeString.setStatus("mandatory")
_NicParms_ObjectIdentity = ObjectIdentity
nicParms = _NicParms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 7)
)
_NicCommonParms_ObjectIdentity = ObjectIdentity
nicCommonParms = _NicCommonParms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 7, 1)
)
_NicParmSampling_Type = Integer32
_NicParmSampling_Object = MibScalar
nicParmSampling = _NicParmSampling_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 7, 1, 1),
    _NicParmSampling_Type()
)
nicParmSampling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nicParmSampling.setStatus("mandatory")
_NicParmProcessing_Type = Integer32
_NicParmProcessing_Object = MibScalar
nicParmProcessing = _NicParmProcessing_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 7, 1, 2),
    _NicParmProcessing_Type()
)
nicParmProcessing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nicParmProcessing.setStatus("mandatory")
_NicParmRxErrCount_Type = Integer32
_NicParmRxErrCount_Object = MibScalar
nicParmRxErrCount = _NicParmRxErrCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 7, 1, 3),
    _NicParmRxErrCount_Type()
)
nicParmRxErrCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nicParmRxErrCount.setStatus("mandatory")
_NicParmRxErrDelta_Type = Integer32
_NicParmRxErrDelta_Object = MibScalar
nicParmRxErrDelta = _NicParmRxErrDelta_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 7, 1, 4),
    _NicParmRxErrDelta_Type()
)
nicParmRxErrDelta.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nicParmRxErrDelta.setStatus("mandatory")


class _NicParmRxErrPct_Type(DisplayString):
    """Custom type nicParmRxErrPct based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_NicParmRxErrPct_Type.__name__ = "DisplayString"
_NicParmRxErrPct_Object = MibScalar
nicParmRxErrPct = _NicParmRxErrPct_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 7, 1, 5),
    _NicParmRxErrPct_Type()
)
nicParmRxErrPct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nicParmRxErrPct.setStatus("mandatory")
_NicParmTxErrCount_Type = Integer32
_NicParmTxErrCount_Object = MibScalar
nicParmTxErrCount = _NicParmTxErrCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 7, 1, 6),
    _NicParmTxErrCount_Type()
)
nicParmTxErrCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nicParmTxErrCount.setStatus("mandatory")
_NicParmTxErrDelta_Type = Integer32
_NicParmTxErrDelta_Object = MibScalar
nicParmTxErrDelta = _NicParmTxErrDelta_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 7, 1, 7),
    _NicParmTxErrDelta_Type()
)
nicParmTxErrDelta.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nicParmTxErrDelta.setStatus("mandatory")


class _NicParmTxErrPct_Type(DisplayString):
    """Custom type nicParmTxErrPct based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_NicParmTxErrPct_Type.__name__ = "DisplayString"
_NicParmTxErrPct_Object = MibScalar
nicParmTxErrPct = _NicParmTxErrPct_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 7, 1, 8),
    _NicParmTxErrPct_Type()
)
nicParmTxErrPct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nicParmTxErrPct.setStatus("mandatory")
_NicParmAdapterResetCount_Type = Integer32
_NicParmAdapterResetCount_Object = MibScalar
nicParmAdapterResetCount = _NicParmAdapterResetCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 7, 1, 9),
    _NicParmAdapterResetCount_Type()
)
nicParmAdapterResetCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nicParmAdapterResetCount.setStatus("mandatory")
_NicParmAdapterResetDelta_Type = Integer32
_NicParmAdapterResetDelta_Object = MibScalar
nicParmAdapterResetDelta = _NicParmAdapterResetDelta_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 7, 1, 10),
    _NicParmAdapterResetDelta_Type()
)
nicParmAdapterResetDelta.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nicParmAdapterResetDelta.setStatus("mandatory")


class _NicParmAdapterResetPct_Type(DisplayString):
    """Custom type nicParmAdapterResetPct based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_NicParmAdapterResetPct_Type.__name__ = "DisplayString"
_NicParmAdapterResetPct_Object = MibScalar
nicParmAdapterResetPct = _NicParmAdapterResetPct_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 7, 1, 11),
    _NicParmAdapterResetPct_Type()
)
nicParmAdapterResetPct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nicParmAdapterResetPct.setStatus("mandatory")
_NicParmAlignmentCount_Type = Integer32
_NicParmAlignmentCount_Object = MibScalar
nicParmAlignmentCount = _NicParmAlignmentCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 7, 1, 12),
    _NicParmAlignmentCount_Type()
)
nicParmAlignmentCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nicParmAlignmentCount.setStatus("mandatory")
_NicParmAlignmentDelta_Type = Integer32
_NicParmAlignmentDelta_Object = MibScalar
nicParmAlignmentDelta = _NicParmAlignmentDelta_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 7, 1, 13),
    _NicParmAlignmentDelta_Type()
)
nicParmAlignmentDelta.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nicParmAlignmentDelta.setStatus("mandatory")


class _NicParmAlignmentPct_Type(DisplayString):
    """Custom type nicParmAlignmentPct based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_NicParmAlignmentPct_Type.__name__ = "DisplayString"
_NicParmAlignmentPct_Object = MibScalar
nicParmAlignmentPct = _NicParmAlignmentPct_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 7, 1, 14),
    _NicParmAlignmentPct_Type()
)
nicParmAlignmentPct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nicParmAlignmentPct.setStatus("mandatory")
_NicParmFrameTooLongCount_Type = Integer32
_NicParmFrameTooLongCount_Object = MibScalar
nicParmFrameTooLongCount = _NicParmFrameTooLongCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 7, 1, 15),
    _NicParmFrameTooLongCount_Type()
)
nicParmFrameTooLongCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nicParmFrameTooLongCount.setStatus("mandatory")
_NicParmFrameTooLongDelta_Type = Integer32
_NicParmFrameTooLongDelta_Object = MibScalar
nicParmFrameTooLongDelta = _NicParmFrameTooLongDelta_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 7, 1, 16),
    _NicParmFrameTooLongDelta_Type()
)
nicParmFrameTooLongDelta.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nicParmFrameTooLongDelta.setStatus("mandatory")


class _NicParmFrameTooLongPct_Type(DisplayString):
    """Custom type nicParmFrameTooLongPct based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_NicParmFrameTooLongPct_Type.__name__ = "DisplayString"
_NicParmFrameTooLongPct_Object = MibScalar
nicParmFrameTooLongPct = _NicParmFrameTooLongPct_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 7, 1, 17),
    _NicParmFrameTooLongPct_Type()
)
nicParmFrameTooLongPct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nicParmFrameTooLongPct.setStatus("mandatory")
_NicParmHardwareMismatchCount_Type = Integer32
_NicParmHardwareMismatchCount_Object = MibScalar
nicParmHardwareMismatchCount = _NicParmHardwareMismatchCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 7, 1, 18),
    _NicParmHardwareMismatchCount_Type()
)
nicParmHardwareMismatchCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nicParmHardwareMismatchCount.setStatus("mandatory")
_NicParmHardwareMismatchDelta_Type = Integer32
_NicParmHardwareMismatchDelta_Object = MibScalar
nicParmHardwareMismatchDelta = _NicParmHardwareMismatchDelta_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 7, 1, 19),
    _NicParmHardwareMismatchDelta_Type()
)
nicParmHardwareMismatchDelta.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nicParmHardwareMismatchDelta.setStatus("mandatory")


class _NicParmHardwareMismatchPct_Type(DisplayString):
    """Custom type nicParmHardwareMismatchPct based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_NicParmHardwareMismatchPct_Type.__name__ = "DisplayString"
_NicParmHardwareMismatchPct_Object = MibScalar
nicParmHardwareMismatchPct = _NicParmHardwareMismatchPct_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 7, 1, 20),
    _NicParmHardwareMismatchPct_Type()
)
nicParmHardwareMismatchPct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nicParmHardwareMismatchPct.setStatus("mandatory")
_NicParmLateCollisionCount_Type = Integer32
_NicParmLateCollisionCount_Object = MibScalar
nicParmLateCollisionCount = _NicParmLateCollisionCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 7, 1, 21),
    _NicParmLateCollisionCount_Type()
)
nicParmLateCollisionCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nicParmLateCollisionCount.setStatus("mandatory")
_NicParmLateCollisionDelta_Type = Integer32
_NicParmLateCollisionDelta_Object = MibScalar
nicParmLateCollisionDelta = _NicParmLateCollisionDelta_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 7, 1, 22),
    _NicParmLateCollisionDelta_Type()
)
nicParmLateCollisionDelta.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nicParmLateCollisionDelta.setStatus("mandatory")


class _NicParmLateCollisionPct_Type(DisplayString):
    """Custom type nicParmLateCollisionPct based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_NicParmLateCollisionPct_Type.__name__ = "DisplayString"
_NicParmLateCollisionPct_Object = MibScalar
nicParmLateCollisionPct = _NicParmLateCollisionPct_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 7, 1, 23),
    _NicParmLateCollisionPct_Type()
)
nicParmLateCollisionPct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nicParmLateCollisionPct.setStatus("mandatory")
_NicParmExcessCollisionCount_Type = Integer32
_NicParmExcessCollisionCount_Object = MibScalar
nicParmExcessCollisionCount = _NicParmExcessCollisionCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 7, 1, 24),
    _NicParmExcessCollisionCount_Type()
)
nicParmExcessCollisionCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nicParmExcessCollisionCount.setStatus("mandatory")
_NicParmExcessCollisionDelta_Type = Integer32
_NicParmExcessCollisionDelta_Object = MibScalar
nicParmExcessCollisionDelta = _NicParmExcessCollisionDelta_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 7, 1, 25),
    _NicParmExcessCollisionDelta_Type()
)
nicParmExcessCollisionDelta.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nicParmExcessCollisionDelta.setStatus("mandatory")


class _NicParmExcessCollisionPct_Type(DisplayString):
    """Custom type nicParmExcessCollisionPct based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_NicParmExcessCollisionPct_Type.__name__ = "DisplayString"
_NicParmExcessCollisionPct_Object = MibScalar
nicParmExcessCollisionPct = _NicParmExcessCollisionPct_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 7, 1, 26),
    _NicParmExcessCollisionPct_Type()
)
nicParmExcessCollisionPct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nicParmExcessCollisionPct.setStatus("mandatory")
_NicParmCarrierSenseCount_Type = Integer32
_NicParmCarrierSenseCount_Object = MibScalar
nicParmCarrierSenseCount = _NicParmCarrierSenseCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 7, 1, 27),
    _NicParmCarrierSenseCount_Type()
)
nicParmCarrierSenseCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nicParmCarrierSenseCount.setStatus("mandatory")
_NicParmCarrierSenseDelta_Type = Integer32
_NicParmCarrierSenseDelta_Object = MibScalar
nicParmCarrierSenseDelta = _NicParmCarrierSenseDelta_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 7, 1, 28),
    _NicParmCarrierSenseDelta_Type()
)
nicParmCarrierSenseDelta.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nicParmCarrierSenseDelta.setStatus("mandatory")


class _NicParmCarrierSensePct_Type(DisplayString):
    """Custom type nicParmCarrierSensePct based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_NicParmCarrierSensePct_Type.__name__ = "DisplayString"
_NicParmCarrierSensePct_Object = MibScalar
nicParmCarrierSensePct = _NicParmCarrierSensePct_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 7, 1, 29),
    _NicParmCarrierSensePct_Type()
)
nicParmCarrierSensePct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nicParmCarrierSensePct.setStatus("mandatory")
_NicParmDeferralCount_Type = Integer32
_NicParmDeferralCount_Object = MibScalar
nicParmDeferralCount = _NicParmDeferralCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 7, 1, 30),
    _NicParmDeferralCount_Type()
)
nicParmDeferralCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nicParmDeferralCount.setStatus("mandatory")
_NicParmDeferralDelta_Type = Integer32
_NicParmDeferralDelta_Object = MibScalar
nicParmDeferralDelta = _NicParmDeferralDelta_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 7, 1, 31),
    _NicParmDeferralDelta_Type()
)
nicParmDeferralDelta.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nicParmDeferralDelta.setStatus("mandatory")


class _NicParmDeferralPct_Type(DisplayString):
    """Custom type nicParmDeferralPct based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_NicParmDeferralPct_Type.__name__ = "DisplayString"
_NicParmDeferralPct_Object = MibScalar
nicParmDeferralPct = _NicParmDeferralPct_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 7, 1, 32),
    _NicParmDeferralPct_Type()
)
nicParmDeferralPct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nicParmDeferralPct.setStatus("mandatory")
_NicParmNoECBCount_Type = Integer32
_NicParmNoECBCount_Object = MibScalar
nicParmNoECBCount = _NicParmNoECBCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 7, 1, 33),
    _NicParmNoECBCount_Type()
)
nicParmNoECBCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nicParmNoECBCount.setStatus("mandatory")
_NicParmNoECBDelta_Type = Integer32
_NicParmNoECBDelta_Object = MibScalar
nicParmNoECBDelta = _NicParmNoECBDelta_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 7, 1, 34),
    _NicParmNoECBDelta_Type()
)
nicParmNoECBDelta.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nicParmNoECBDelta.setStatus("mandatory")


class _NicParmNoECBPct_Type(DisplayString):
    """Custom type nicParmNoECBPct based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_NicParmNoECBPct_Type.__name__ = "DisplayString"
_NicParmNoECBPct_Object = MibScalar
nicParmNoECBPct = _NicParmNoECBPct_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 7, 1, 35),
    _NicParmNoECBPct_Type()
)
nicParmNoECBPct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nicParmNoECBPct.setStatus("mandatory")
_NicParmRxOverflowCount_Type = Integer32
_NicParmRxOverflowCount_Object = MibScalar
nicParmRxOverflowCount = _NicParmRxOverflowCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 7, 1, 36),
    _NicParmRxOverflowCount_Type()
)
nicParmRxOverflowCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nicParmRxOverflowCount.setStatus("mandatory")
_NicParmRxOverflowDelta_Type = Integer32
_NicParmRxOverflowDelta_Object = MibScalar
nicParmRxOverflowDelta = _NicParmRxOverflowDelta_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 7, 1, 37),
    _NicParmRxOverflowDelta_Type()
)
nicParmRxOverflowDelta.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nicParmRxOverflowDelta.setStatus("mandatory")


class _NicParmRxOverflowPct_Type(DisplayString):
    """Custom type nicParmRxOverflowPct based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_NicParmRxOverflowPct_Type.__name__ = "DisplayString"
_NicParmRxOverflowPct_Object = MibScalar
nicParmRxOverflowPct = _NicParmRxOverflowPct_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 7, 1, 38),
    _NicParmRxOverflowPct_Type()
)
nicParmRxOverflowPct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nicParmRxOverflowPct.setStatus("mandatory")
_NicParmUtilizationCount_Type = Integer32
_NicParmUtilizationCount_Object = MibScalar
nicParmUtilizationCount = _NicParmUtilizationCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 7, 1, 39),
    _NicParmUtilizationCount_Type()
)
nicParmUtilizationCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nicParmUtilizationCount.setStatus("mandatory")
_NicParmAdapterType_Type = Integer32
_NicParmAdapterType_Object = MibScalar
nicParmAdapterType = _NicParmAdapterType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 7, 1, 40),
    _NicParmAdapterType_Type()
)
nicParmAdapterType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nicParmAdapterType.setStatus("mandatory")
_NicParmLineErrCount_Type = Integer32
_NicParmLineErrCount_Object = MibScalar
nicParmLineErrCount = _NicParmLineErrCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 7, 1, 41),
    _NicParmLineErrCount_Type()
)
nicParmLineErrCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nicParmLineErrCount.setStatus("mandatory")
_NicParmLineErrDelta_Type = Integer32
_NicParmLineErrDelta_Object = MibScalar
nicParmLineErrDelta = _NicParmLineErrDelta_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 7, 1, 42),
    _NicParmLineErrDelta_Type()
)
nicParmLineErrDelta.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nicParmLineErrDelta.setStatus("mandatory")


class _NicParmLineErrPct_Type(DisplayString):
    """Custom type nicParmLineErrPct based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_NicParmLineErrPct_Type.__name__ = "DisplayString"
_NicParmLineErrPct_Object = MibScalar
nicParmLineErrPct = _NicParmLineErrPct_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 7, 1, 43),
    _NicParmLineErrPct_Type()
)
nicParmLineErrPct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nicParmLineErrPct.setStatus("mandatory")
_NicParmLostFramesCount_Type = Integer32
_NicParmLostFramesCount_Object = MibScalar
nicParmLostFramesCount = _NicParmLostFramesCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 7, 1, 44),
    _NicParmLostFramesCount_Type()
)
nicParmLostFramesCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nicParmLostFramesCount.setStatus("mandatory")
_NicParmLostFramesDelta_Type = Integer32
_NicParmLostFramesDelta_Object = MibScalar
nicParmLostFramesDelta = _NicParmLostFramesDelta_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 7, 1, 45),
    _NicParmLostFramesDelta_Type()
)
nicParmLostFramesDelta.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nicParmLostFramesDelta.setStatus("mandatory")


class _NicParmLostFramesPct_Type(DisplayString):
    """Custom type nicParmLostFramesPct based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_NicParmLostFramesPct_Type.__name__ = "DisplayString"
_NicParmLostFramesPct_Object = MibScalar
nicParmLostFramesPct = _NicParmLostFramesPct_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 7, 1, 46),
    _NicParmLostFramesPct_Type()
)
nicParmLostFramesPct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nicParmLostFramesPct.setStatus("mandatory")
_NicParmBurstErrCount_Type = Integer32
_NicParmBurstErrCount_Object = MibScalar
nicParmBurstErrCount = _NicParmBurstErrCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 7, 1, 47),
    _NicParmBurstErrCount_Type()
)
nicParmBurstErrCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nicParmBurstErrCount.setStatus("mandatory")
_NicParmBurstErrDelta_Type = Integer32
_NicParmBurstErrDelta_Object = MibScalar
nicParmBurstErrDelta = _NicParmBurstErrDelta_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 7, 1, 48),
    _NicParmBurstErrDelta_Type()
)
nicParmBurstErrDelta.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nicParmBurstErrDelta.setStatus("mandatory")


class _NicParmBurstErrPct_Type(DisplayString):
    """Custom type nicParmBurstErrPct based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_NicParmBurstErrPct_Type.__name__ = "DisplayString"
_NicParmBurstErrPct_Object = MibScalar
nicParmBurstErrPct = _NicParmBurstErrPct_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 7, 1, 49),
    _NicParmBurstErrPct_Type()
)
nicParmBurstErrPct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nicParmBurstErrPct.setStatus("mandatory")
_NicParmACErrCount_Type = Integer32
_NicParmACErrCount_Object = MibScalar
nicParmACErrCount = _NicParmACErrCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 7, 1, 50),
    _NicParmACErrCount_Type()
)
nicParmACErrCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nicParmACErrCount.setStatus("mandatory")
_NicParmACErrDelta_Type = Integer32
_NicParmACErrDelta_Object = MibScalar
nicParmACErrDelta = _NicParmACErrDelta_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 7, 1, 51),
    _NicParmACErrDelta_Type()
)
nicParmACErrDelta.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nicParmACErrDelta.setStatus("mandatory")


class _NicParmACErrPct_Type(DisplayString):
    """Custom type nicParmACErrPct based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_NicParmACErrPct_Type.__name__ = "DisplayString"
_NicParmACErrPct_Object = MibScalar
nicParmACErrPct = _NicParmACErrPct_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 7, 1, 52),
    _NicParmACErrPct_Type()
)
nicParmACErrPct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nicParmACErrPct.setStatus("mandatory")
_NicParmAbortDelimitersCount_Type = Integer32
_NicParmAbortDelimitersCount_Object = MibScalar
nicParmAbortDelimitersCount = _NicParmAbortDelimitersCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 7, 1, 53),
    _NicParmAbortDelimitersCount_Type()
)
nicParmAbortDelimitersCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nicParmAbortDelimitersCount.setStatus("mandatory")
_NicParmAbortDelimitersDelta_Type = Integer32
_NicParmAbortDelimitersDelta_Object = MibScalar
nicParmAbortDelimitersDelta = _NicParmAbortDelimitersDelta_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 7, 1, 54),
    _NicParmAbortDelimitersDelta_Type()
)
nicParmAbortDelimitersDelta.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nicParmAbortDelimitersDelta.setStatus("mandatory")


class _NicParmAbortDelimitersPct_Type(DisplayString):
    """Custom type nicParmAbortDelimitersPct based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_NicParmAbortDelimitersPct_Type.__name__ = "DisplayString"
_NicParmAbortDelimitersPct_Object = MibScalar
nicParmAbortDelimitersPct = _NicParmAbortDelimitersPct_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 7, 1, 55),
    _NicParmAbortDelimitersPct_Type()
)
nicParmAbortDelimitersPct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nicParmAbortDelimitersPct.setStatus("mandatory")
_NicParmFrameCopiedErrCount_Type = Integer32
_NicParmFrameCopiedErrCount_Object = MibScalar
nicParmFrameCopiedErrCount = _NicParmFrameCopiedErrCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 7, 1, 56),
    _NicParmFrameCopiedErrCount_Type()
)
nicParmFrameCopiedErrCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nicParmFrameCopiedErrCount.setStatus("mandatory")
_NicParmFrameCopiedErrDelta_Type = Integer32
_NicParmFrameCopiedErrDelta_Object = MibScalar
nicParmFrameCopiedErrDelta = _NicParmFrameCopiedErrDelta_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 7, 1, 57),
    _NicParmFrameCopiedErrDelta_Type()
)
nicParmFrameCopiedErrDelta.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nicParmFrameCopiedErrDelta.setStatus("mandatory")


class _NicParmFrameCopiedErrPct_Type(DisplayString):
    """Custom type nicParmFrameCopiedErrPct based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_NicParmFrameCopiedErrPct_Type.__name__ = "DisplayString"
_NicParmFrameCopiedErrPct_Object = MibScalar
nicParmFrameCopiedErrPct = _NicParmFrameCopiedErrPct_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 7, 1, 58),
    _NicParmFrameCopiedErrPct_Type()
)
nicParmFrameCopiedErrPct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nicParmFrameCopiedErrPct.setStatus("mandatory")
_NicParmFrequencyErrCount_Type = Integer32
_NicParmFrequencyErrCount_Object = MibScalar
nicParmFrequencyErrCount = _NicParmFrequencyErrCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 7, 1, 59),
    _NicParmFrequencyErrCount_Type()
)
nicParmFrequencyErrCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nicParmFrequencyErrCount.setStatus("mandatory")
_NicParmFrequencyErrDelta_Type = Integer32
_NicParmFrequencyErrDelta_Object = MibScalar
nicParmFrequencyErrDelta = _NicParmFrequencyErrDelta_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 7, 1, 60),
    _NicParmFrequencyErrDelta_Type()
)
nicParmFrequencyErrDelta.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nicParmFrequencyErrDelta.setStatus("mandatory")


class _NicParmFrequencyErrPct_Type(DisplayString):
    """Custom type nicParmFrequencyErrPct based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_NicParmFrequencyErrPct_Type.__name__ = "DisplayString"
_NicParmFrequencyErrPct_Object = MibScalar
nicParmFrequencyErrPct = _NicParmFrequencyErrPct_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 7, 1, 61),
    _NicParmFrequencyErrPct_Type()
)
nicParmFrequencyErrPct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nicParmFrequencyErrPct.setStatus("mandatory")
_NicParmTokenErrCount_Type = Integer32
_NicParmTokenErrCount_Object = MibScalar
nicParmTokenErrCount = _NicParmTokenErrCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 7, 1, 62),
    _NicParmTokenErrCount_Type()
)
nicParmTokenErrCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nicParmTokenErrCount.setStatus("mandatory")
_NicParmTokenErrDelta_Type = Integer32
_NicParmTokenErrDelta_Object = MibScalar
nicParmTokenErrDelta = _NicParmTokenErrDelta_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 7, 1, 63),
    _NicParmTokenErrDelta_Type()
)
nicParmTokenErrDelta.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nicParmTokenErrDelta.setStatus("mandatory")


class _NicParmTokenErrPct_Type(DisplayString):
    """Custom type nicParmTokenErrPct based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_NicParmTokenErrPct_Type.__name__ = "DisplayString"
_NicParmTokenErrPct_Object = MibScalar
nicParmTokenErrPct = _NicParmTokenErrPct_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 7, 1, 64),
    _NicParmTokenErrPct_Type()
)
nicParmTokenErrPct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nicParmTokenErrPct.setStatus("mandatory")
_NicParmInternalErrCount_Type = Integer32
_NicParmInternalErrCount_Object = MibScalar
nicParmInternalErrCount = _NicParmInternalErrCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 7, 1, 65),
    _NicParmInternalErrCount_Type()
)
nicParmInternalErrCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nicParmInternalErrCount.setStatus("mandatory")
_NicParmInternalErrDelta_Type = Integer32
_NicParmInternalErrDelta_Object = MibScalar
nicParmInternalErrDelta = _NicParmInternalErrDelta_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 7, 1, 66),
    _NicParmInternalErrDelta_Type()
)
nicParmInternalErrDelta.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nicParmInternalErrDelta.setStatus("mandatory")


class _NicParmInternalErrPct_Type(DisplayString):
    """Custom type nicParmInternalErrPct based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_NicParmInternalErrPct_Type.__name__ = "DisplayString"
_NicParmInternalErrPct_Object = MibScalar
nicParmInternalErrPct = _NicParmInternalErrPct_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 7, 1, 67),
    _NicParmInternalErrPct_Type()
)
nicParmInternalErrPct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nicParmInternalErrPct.setStatus("mandatory")
_NicParmAftFailOverErrCount_Type = Integer32
_NicParmAftFailOverErrCount_Object = MibScalar
nicParmAftFailOverErrCount = _NicParmAftFailOverErrCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 7, 1, 68),
    _NicParmAftFailOverErrCount_Type()
)
nicParmAftFailOverErrCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nicParmAftFailOverErrCount.setStatus("mandatory")
_NicParmAftFailOverErrDelta_Type = Integer32
_NicParmAftFailOverErrDelta_Object = MibScalar
nicParmAftFailOverErrDelta = _NicParmAftFailOverErrDelta_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 7, 1, 69),
    _NicParmAftFailOverErrDelta_Type()
)
nicParmAftFailOverErrDelta.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nicParmAftFailOverErrDelta.setStatus("mandatory")
_NicParmAftRecoveryErrCount_Type = Integer32
_NicParmAftRecoveryErrCount_Object = MibScalar
nicParmAftRecoveryErrCount = _NicParmAftRecoveryErrCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 7, 1, 70),
    _NicParmAftRecoveryErrCount_Type()
)
nicParmAftRecoveryErrCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nicParmAftRecoveryErrCount.setStatus("mandatory")
_NicParmAftRecoveryErrDelta_Type = Integer32
_NicParmAftRecoveryErrDelta_Object = MibScalar
nicParmAftRecoveryErrDelta = _NicParmAftRecoveryErrDelta_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 7, 1, 71),
    _NicParmAftRecoveryErrDelta_Type()
)
nicParmAftRecoveryErrDelta.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nicParmAftRecoveryErrDelta.setStatus("mandatory")
_NicParmAftStandbyErrCount_Type = Integer32
_NicParmAftStandbyErrCount_Object = MibScalar
nicParmAftStandbyErrCount = _NicParmAftStandbyErrCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 7, 1, 72),
    _NicParmAftStandbyErrCount_Type()
)
nicParmAftStandbyErrCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nicParmAftStandbyErrCount.setStatus("mandatory")
_NicParmAftStandbyErrDelta_Type = Integer32
_NicParmAftStandbyErrDelta_Object = MibScalar
nicParmAftStandbyErrDelta = _NicParmAftStandbyErrDelta_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 7, 1, 73),
    _NicParmAftStandbyErrDelta_Type()
)
nicParmAftStandbyErrDelta.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nicParmAftStandbyErrDelta.setStatus("mandatory")
_NicParmAftGruoupFailErrCount_Type = Integer32
_NicParmAftGruoupFailErrCount_Object = MibScalar
nicParmAftGruoupFailErrCount = _NicParmAftGruoupFailErrCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 7, 1, 74),
    _NicParmAftGruoupFailErrCount_Type()
)
nicParmAftGruoupFailErrCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nicParmAftGruoupFailErrCount.setStatus("mandatory")
_NicParmAftGroupFailErrDelta_Type = Integer32
_NicParmAftGroupFailErrDelta_Object = MibScalar
nicParmAftGroupFailErrDelta = _NicParmAftGroupFailErrDelta_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 7, 1, 75),
    _NicParmAftGroupFailErrDelta_Type()
)
nicParmAftGroupFailErrDelta.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nicParmAftGroupFailErrDelta.setStatus("mandatory")
_NicStarfighterParms_ObjectIdentity = ObjectIdentity
nicStarfighterParms = _NicStarfighterParms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 7, 2)
)
_NicStarfighterParmTxFifoCount_Type = Integer32
_NicStarfighterParmTxFifoCount_Object = MibScalar
nicStarfighterParmTxFifoCount = _NicStarfighterParmTxFifoCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 7, 2, 1),
    _NicStarfighterParmTxFifoCount_Type()
)
nicStarfighterParmTxFifoCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nicStarfighterParmTxFifoCount.setStatus("mandatory")
_NicStarfighterParmTxFifoDelta_Type = Integer32
_NicStarfighterParmTxFifoDelta_Object = MibScalar
nicStarfighterParmTxFifoDelta = _NicStarfighterParmTxFifoDelta_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 7, 2, 2),
    _NicStarfighterParmTxFifoDelta_Type()
)
nicStarfighterParmTxFifoDelta.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nicStarfighterParmTxFifoDelta.setStatus("mandatory")


class _NicStarfighterParmTxFifoPct_Type(DisplayString):
    """Custom type nicStarfighterParmTxFifoPct based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_NicStarfighterParmTxFifoPct_Type.__name__ = "DisplayString"
_NicStarfighterParmTxFifoPct_Object = MibScalar
nicStarfighterParmTxFifoPct = _NicStarfighterParmTxFifoPct_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 7, 2, 3),
    _NicStarfighterParmTxFifoPct_Type()
)
nicStarfighterParmTxFifoPct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nicStarfighterParmTxFifoPct.setStatus("mandatory")
_NicStarfighterParmTxTimedOutCount_Type = Integer32
_NicStarfighterParmTxTimedOutCount_Object = MibScalar
nicStarfighterParmTxTimedOutCount = _NicStarfighterParmTxTimedOutCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 7, 2, 4),
    _NicStarfighterParmTxTimedOutCount_Type()
)
nicStarfighterParmTxTimedOutCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nicStarfighterParmTxTimedOutCount.setStatus("mandatory")
_NicStarfighterParmTxTimedOutDelta_Type = Integer32
_NicStarfighterParmTxTimedOutDelta_Object = MibScalar
nicStarfighterParmTxTimedOutDelta = _NicStarfighterParmTxTimedOutDelta_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 7, 2, 5),
    _NicStarfighterParmTxTimedOutDelta_Type()
)
nicStarfighterParmTxTimedOutDelta.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nicStarfighterParmTxTimedOutDelta.setStatus("mandatory")


class _NicStarfighterParmTxTimedOutPct_Type(DisplayString):
    """Custom type nicStarfighterParmTxTimedOutPct based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_NicStarfighterParmTxTimedOutPct_Type.__name__ = "DisplayString"
_NicStarfighterParmTxTimedOutPct_Object = MibScalar
nicStarfighterParmTxTimedOutPct = _NicStarfighterParmTxTimedOutPct_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 7, 2, 6),
    _NicStarfighterParmTxTimedOutPct_Type()
)
nicStarfighterParmTxTimedOutPct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nicStarfighterParmTxTimedOutPct.setStatus("mandatory")
_NicStarfighterParmRxFifoCount_Type = Integer32
_NicStarfighterParmRxFifoCount_Object = MibScalar
nicStarfighterParmRxFifoCount = _NicStarfighterParmRxFifoCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 7, 2, 7),
    _NicStarfighterParmRxFifoCount_Type()
)
nicStarfighterParmRxFifoCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nicStarfighterParmRxFifoCount.setStatus("mandatory")
_NicStarfighterParmRxFifoDelta_Type = Integer32
_NicStarfighterParmRxFifoDelta_Object = MibScalar
nicStarfighterParmRxFifoDelta = _NicStarfighterParmRxFifoDelta_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 7, 2, 8),
    _NicStarfighterParmRxFifoDelta_Type()
)
nicStarfighterParmRxFifoDelta.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nicStarfighterParmRxFifoDelta.setStatus("mandatory")


class _NicStarfighterParmRxFifoPct_Type(DisplayString):
    """Custom type nicStarfighterParmRxFifoPct based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_NicStarfighterParmRxFifoPct_Type.__name__ = "DisplayString"
_NicStarfighterParmRxFifoPct_Object = MibScalar
nicStarfighterParmRxFifoPct = _NicStarfighterParmRxFifoPct_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 7, 2, 9),
    _NicStarfighterParmRxFifoPct_Type()
)
nicStarfighterParmRxFifoPct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nicStarfighterParmRxFifoPct.setStatus("mandatory")
_NicStarfighterParmRxFalseInterruptCount_Type = Integer32
_NicStarfighterParmRxFalseInterruptCount_Object = MibScalar
nicStarfighterParmRxFalseInterruptCount = _NicStarfighterParmRxFalseInterruptCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 7, 2, 10),
    _NicStarfighterParmRxFalseInterruptCount_Type()
)
nicStarfighterParmRxFalseInterruptCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nicStarfighterParmRxFalseInterruptCount.setStatus("mandatory")
_NicStarfighterParmRxFalseInterruptDelta_Type = Integer32
_NicStarfighterParmRxFalseInterruptDelta_Object = MibScalar
nicStarfighterParmRxFalseInterruptDelta = _NicStarfighterParmRxFalseInterruptDelta_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 7, 2, 11),
    _NicStarfighterParmRxFalseInterruptDelta_Type()
)
nicStarfighterParmRxFalseInterruptDelta.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nicStarfighterParmRxFalseInterruptDelta.setStatus("mandatory")


class _NicStarfighterParmRxFalseInterruptPct_Type(DisplayString):
    """Custom type nicStarfighterParmRxFalseInterruptPct based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_NicStarfighterParmRxFalseInterruptPct_Type.__name__ = "DisplayString"
_NicStarfighterParmRxFalseInterruptPct_Object = MibScalar
nicStarfighterParmRxFalseInterruptPct = _NicStarfighterParmRxFalseInterruptPct_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 7, 2, 12),
    _NicStarfighterParmRxFalseInterruptPct_Type()
)
nicStarfighterParmRxFalseInterruptPct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nicStarfighterParmRxFalseInterruptPct.setStatus("mandatory")
_NicStarfighterParmRxPagingErrCount_Type = Integer32
_NicStarfighterParmRxPagingErrCount_Object = MibScalar
nicStarfighterParmRxPagingErrCount = _NicStarfighterParmRxPagingErrCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 7, 2, 13),
    _NicStarfighterParmRxPagingErrCount_Type()
)
nicStarfighterParmRxPagingErrCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nicStarfighterParmRxPagingErrCount.setStatus("mandatory")
_NicStarfighterParmRxPagingErrDelta_Type = Integer32
_NicStarfighterParmRxPagingErrDelta_Object = MibScalar
nicStarfighterParmRxPagingErrDelta = _NicStarfighterParmRxPagingErrDelta_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 7, 2, 14),
    _NicStarfighterParmRxPagingErrDelta_Type()
)
nicStarfighterParmRxPagingErrDelta.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nicStarfighterParmRxPagingErrDelta.setStatus("mandatory")


class _NicStarfighterParmRxPagingErrPct_Type(DisplayString):
    """Custom type nicStarfighterParmRxPagingErrPct based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_NicStarfighterParmRxPagingErrPct_Type.__name__ = "DisplayString"
_NicStarfighterParmRxPagingErrPct_Object = MibScalar
nicStarfighterParmRxPagingErrPct = _NicStarfighterParmRxPagingErrPct_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 7, 2, 15),
    _NicStarfighterParmRxPagingErrPct_Type()
)
nicStarfighterParmRxPagingErrPct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nicStarfighterParmRxPagingErrPct.setStatus("mandatory")
_NicTwisterParms_ObjectIdentity = ObjectIdentity
nicTwisterParms = _NicTwisterParms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 7, 3)
)
_NicTwisterParmTxFifoCount_Type = Integer32
_NicTwisterParmTxFifoCount_Object = MibScalar
nicTwisterParmTxFifoCount = _NicTwisterParmTxFifoCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 7, 3, 1),
    _NicTwisterParmTxFifoCount_Type()
)
nicTwisterParmTxFifoCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nicTwisterParmTxFifoCount.setStatus("mandatory")
_NicTwisterParmTxFifoDelta_Type = Integer32
_NicTwisterParmTxFifoDelta_Object = MibScalar
nicTwisterParmTxFifoDelta = _NicTwisterParmTxFifoDelta_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 7, 3, 2),
    _NicTwisterParmTxFifoDelta_Type()
)
nicTwisterParmTxFifoDelta.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nicTwisterParmTxFifoDelta.setStatus("mandatory")


class _NicTwisterParmTxFifoPct_Type(DisplayString):
    """Custom type nicTwisterParmTxFifoPct based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_NicTwisterParmTxFifoPct_Type.__name__ = "DisplayString"
_NicTwisterParmTxFifoPct_Object = MibScalar
nicTwisterParmTxFifoPct = _NicTwisterParmTxFifoPct_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 7, 3, 3),
    _NicTwisterParmTxFifoPct_Type()
)
nicTwisterParmTxFifoPct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nicTwisterParmTxFifoPct.setStatus("mandatory")
_NicTwisterParmTxTimedOutCount_Type = Integer32
_NicTwisterParmTxTimedOutCount_Object = MibScalar
nicTwisterParmTxTimedOutCount = _NicTwisterParmTxTimedOutCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 7, 3, 4),
    _NicTwisterParmTxTimedOutCount_Type()
)
nicTwisterParmTxTimedOutCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nicTwisterParmTxTimedOutCount.setStatus("mandatory")
_NicTwisterParmTxTimedOutDelta_Type = Integer32
_NicTwisterParmTxTimedOutDelta_Object = MibScalar
nicTwisterParmTxTimedOutDelta = _NicTwisterParmTxTimedOutDelta_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 7, 3, 5),
    _NicTwisterParmTxTimedOutDelta_Type()
)
nicTwisterParmTxTimedOutDelta.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nicTwisterParmTxTimedOutDelta.setStatus("mandatory")


class _NicTwisterParmTxTimedOutPct_Type(DisplayString):
    """Custom type nicTwisterParmTxTimedOutPct based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_NicTwisterParmTxTimedOutPct_Type.__name__ = "DisplayString"
_NicTwisterParmTxTimedOutPct_Object = MibScalar
nicTwisterParmTxTimedOutPct = _NicTwisterParmTxTimedOutPct_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 7, 3, 6),
    _NicTwisterParmTxTimedOutPct_Type()
)
nicTwisterParmTxTimedOutPct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nicTwisterParmTxTimedOutPct.setStatus("mandatory")
_NicTwisterParmRxFifoCount_Type = Integer32
_NicTwisterParmRxFifoCount_Object = MibScalar
nicTwisterParmRxFifoCount = _NicTwisterParmRxFifoCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 7, 3, 7),
    _NicTwisterParmRxFifoCount_Type()
)
nicTwisterParmRxFifoCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nicTwisterParmRxFifoCount.setStatus("mandatory")
_NicTwisterParmRxFifoDelta_Type = Integer32
_NicTwisterParmRxFifoDelta_Object = MibScalar
nicTwisterParmRxFifoDelta = _NicTwisterParmRxFifoDelta_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 7, 3, 8),
    _NicTwisterParmRxFifoDelta_Type()
)
nicTwisterParmRxFifoDelta.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nicTwisterParmRxFifoDelta.setStatus("mandatory")


class _NicTwisterParmRxFifoPct_Type(DisplayString):
    """Custom type nicTwisterParmRxFifoPct based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_NicTwisterParmRxFifoPct_Type.__name__ = "DisplayString"
_NicTwisterParmRxFifoPct_Object = MibScalar
nicTwisterParmRxFifoPct = _NicTwisterParmRxFifoPct_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 7, 3, 9),
    _NicTwisterParmRxFifoPct_Type()
)
nicTwisterParmRxFifoPct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nicTwisterParmRxFifoPct.setStatus("mandatory")
_NicTwisterParmRxFalseInterruptCount_Type = Integer32
_NicTwisterParmRxFalseInterruptCount_Object = MibScalar
nicTwisterParmRxFalseInterruptCount = _NicTwisterParmRxFalseInterruptCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 7, 3, 10),
    _NicTwisterParmRxFalseInterruptCount_Type()
)
nicTwisterParmRxFalseInterruptCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nicTwisterParmRxFalseInterruptCount.setStatus("mandatory")
_NicTwisterParmRxFalseInterruptDelta_Type = Integer32
_NicTwisterParmRxFalseInterruptDelta_Object = MibScalar
nicTwisterParmRxFalseInterruptDelta = _NicTwisterParmRxFalseInterruptDelta_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 7, 3, 11),
    _NicTwisterParmRxFalseInterruptDelta_Type()
)
nicTwisterParmRxFalseInterruptDelta.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nicTwisterParmRxFalseInterruptDelta.setStatus("mandatory")


class _NicTwisterParmRxFalseInterruptPct_Type(DisplayString):
    """Custom type nicTwisterParmRxFalseInterruptPct based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_NicTwisterParmRxFalseInterruptPct_Type.__name__ = "DisplayString"
_NicTwisterParmRxFalseInterruptPct_Object = MibScalar
nicTwisterParmRxFalseInterruptPct = _NicTwisterParmRxFalseInterruptPct_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 7, 3, 12),
    _NicTwisterParmRxFalseInterruptPct_Type()
)
nicTwisterParmRxFalseInterruptPct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nicTwisterParmRxFalseInterruptPct.setStatus("mandatory")
_NicTwisterParmRxPagingErrCount_Type = Integer32
_NicTwisterParmRxPagingErrCount_Object = MibScalar
nicTwisterParmRxPagingErrCount = _NicTwisterParmRxPagingErrCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 7, 3, 13),
    _NicTwisterParmRxPagingErrCount_Type()
)
nicTwisterParmRxPagingErrCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nicTwisterParmRxPagingErrCount.setStatus("mandatory")
_NicTwisterParmRxPagingErrDelta_Type = Integer32
_NicTwisterParmRxPagingErrDelta_Object = MibScalar
nicTwisterParmRxPagingErrDelta = _NicTwisterParmRxPagingErrDelta_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 7, 3, 14),
    _NicTwisterParmRxPagingErrDelta_Type()
)
nicTwisterParmRxPagingErrDelta.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nicTwisterParmRxPagingErrDelta.setStatus("mandatory")


class _NicTwisterParmRxPagingErrPct_Type(DisplayString):
    """Custom type nicTwisterParmRxPagingErrPct based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_NicTwisterParmRxPagingErrPct_Type.__name__ = "DisplayString"
_NicTwisterParmRxPagingErrPct_Object = MibScalar
nicTwisterParmRxPagingErrPct = _NicTwisterParmRxPagingErrPct_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 7, 3, 15),
    _NicTwisterParmRxPagingErrPct_Type()
)
nicTwisterParmRxPagingErrPct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nicTwisterParmRxPagingErrPct.setStatus("mandatory")
_NicTwisterParmDMATimedOutCount_Type = Integer32
_NicTwisterParmDMATimedOutCount_Object = MibScalar
nicTwisterParmDMATimedOutCount = _NicTwisterParmDMATimedOutCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 7, 3, 16),
    _NicTwisterParmDMATimedOutCount_Type()
)
nicTwisterParmDMATimedOutCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nicTwisterParmDMATimedOutCount.setStatus("mandatory")
_NicTwisterParmDMATimedOutDelta_Type = Integer32
_NicTwisterParmDMATimedOutDelta_Object = MibScalar
nicTwisterParmDMATimedOutDelta = _NicTwisterParmDMATimedOutDelta_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 7, 3, 17),
    _NicTwisterParmDMATimedOutDelta_Type()
)
nicTwisterParmDMATimedOutDelta.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nicTwisterParmDMATimedOutDelta.setStatus("mandatory")


class _NicTwisterParmDMATimedOutPct_Type(DisplayString):
    """Custom type nicTwisterParmDMATimedOutPct based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_NicTwisterParmDMATimedOutPct_Type.__name__ = "DisplayString"
_NicTwisterParmDMATimedOutPct_Object = MibScalar
nicTwisterParmDMATimedOutPct = _NicTwisterParmDMATimedOutPct_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 7, 3, 18),
    _NicTwisterParmDMATimedOutPct_Type()
)
nicTwisterParmDMATimedOutPct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nicTwisterParmDMATimedOutPct.setStatus("mandatory")
_NicMasterParms_ObjectIdentity = ObjectIdentity
nicMasterParms = _NicMasterParms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 7, 4)
)
_NicMasterParmTxNoResourcesCount_Type = Integer32
_NicMasterParmTxNoResourcesCount_Object = MibScalar
nicMasterParmTxNoResourcesCount = _NicMasterParmTxNoResourcesCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 7, 4, 1),
    _NicMasterParmTxNoResourcesCount_Type()
)
nicMasterParmTxNoResourcesCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nicMasterParmTxNoResourcesCount.setStatus("mandatory")
_NicMasterParmTxNoResourcesDelta_Type = Integer32
_NicMasterParmTxNoResourcesDelta_Object = MibScalar
nicMasterParmTxNoResourcesDelta = _NicMasterParmTxNoResourcesDelta_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 7, 4, 2),
    _NicMasterParmTxNoResourcesDelta_Type()
)
nicMasterParmTxNoResourcesDelta.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nicMasterParmTxNoResourcesDelta.setStatus("mandatory")


class _NicMasterParmTxNoResourcesPct_Type(DisplayString):
    """Custom type nicMasterParmTxNoResourcesPct based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_NicMasterParmTxNoResourcesPct_Type.__name__ = "DisplayString"
_NicMasterParmTxNoResourcesPct_Object = MibScalar
nicMasterParmTxNoResourcesPct = _NicMasterParmTxNoResourcesPct_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 7, 4, 3),
    _NicMasterParmTxNoResourcesPct_Type()
)
nicMasterParmTxNoResourcesPct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nicMasterParmTxNoResourcesPct.setStatus("mandatory")
_NicMasterParmTxExcessFragsCount_Type = Integer32
_NicMasterParmTxExcessFragsCount_Object = MibScalar
nicMasterParmTxExcessFragsCount = _NicMasterParmTxExcessFragsCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 7, 4, 4),
    _NicMasterParmTxExcessFragsCount_Type()
)
nicMasterParmTxExcessFragsCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nicMasterParmTxExcessFragsCount.setStatus("mandatory")
_NicMasterParmTxExcessFragsDelta_Type = Integer32
_NicMasterParmTxExcessFragsDelta_Object = MibScalar
nicMasterParmTxExcessFragsDelta = _NicMasterParmTxExcessFragsDelta_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 7, 4, 5),
    _NicMasterParmTxExcessFragsDelta_Type()
)
nicMasterParmTxExcessFragsDelta.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nicMasterParmTxExcessFragsDelta.setStatus("mandatory")


class _NicMasterParmTxExcessFragsPct_Type(DisplayString):
    """Custom type nicMasterParmTxExcessFragsPct based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_NicMasterParmTxExcessFragsPct_Type.__name__ = "DisplayString"
_NicMasterParmTxExcessFragsPct_Object = MibScalar
nicMasterParmTxExcessFragsPct = _NicMasterParmTxExcessFragsPct_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 7, 4, 6),
    _NicMasterParmTxExcessFragsPct_Type()
)
nicMasterParmTxExcessFragsPct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nicMasterParmTxExcessFragsPct.setStatus("mandatory")
_NicMasterParmRxLowCount_Type = Integer32
_NicMasterParmRxLowCount_Object = MibScalar
nicMasterParmRxLowCount = _NicMasterParmRxLowCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 7, 4, 7),
    _NicMasterParmRxLowCount_Type()
)
nicMasterParmRxLowCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nicMasterParmRxLowCount.setStatus("mandatory")
_NicMasterParmRxLowDelta_Type = Integer32
_NicMasterParmRxLowDelta_Object = MibScalar
nicMasterParmRxLowDelta = _NicMasterParmRxLowDelta_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 7, 4, 8),
    _NicMasterParmRxLowDelta_Type()
)
nicMasterParmRxLowDelta.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nicMasterParmRxLowDelta.setStatus("mandatory")


class _NicMasterParmRxLowPct_Type(DisplayString):
    """Custom type nicMasterParmRxLowPct based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_NicMasterParmRxLowPct_Type.__name__ = "DisplayString"
_NicMasterParmRxLowPct_Object = MibScalar
nicMasterParmRxLowPct = _NicMasterParmRxLowPct_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 7, 4, 9),
    _NicMasterParmRxLowPct_Type()
)
nicMasterParmRxLowPct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nicMasterParmRxLowPct.setStatus("mandatory")
_NicMasterParmRxEmptyCount_Type = Integer32
_NicMasterParmRxEmptyCount_Object = MibScalar
nicMasterParmRxEmptyCount = _NicMasterParmRxEmptyCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 7, 4, 10),
    _NicMasterParmRxEmptyCount_Type()
)
nicMasterParmRxEmptyCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nicMasterParmRxEmptyCount.setStatus("mandatory")
_NicMasterParmRxEmptyDelta_Type = Integer32
_NicMasterParmRxEmptyDelta_Object = MibScalar
nicMasterParmRxEmptyDelta = _NicMasterParmRxEmptyDelta_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 7, 4, 11),
    _NicMasterParmRxEmptyDelta_Type()
)
nicMasterParmRxEmptyDelta.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nicMasterParmRxEmptyDelta.setStatus("mandatory")


class _NicMasterParmRxEmptyPct_Type(DisplayString):
    """Custom type nicMasterParmRxEmptyPct based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_NicMasterParmRxEmptyPct_Type.__name__ = "DisplayString"
_NicMasterParmRxEmptyPct_Object = MibScalar
nicMasterParmRxEmptyPct = _NicMasterParmRxEmptyPct_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 7, 4, 12),
    _NicMasterParmRxEmptyPct_Type()
)
nicMasterParmRxEmptyPct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nicMasterParmRxEmptyPct.setStatus("mandatory")
_NicShastaParms_ObjectIdentity = ObjectIdentity
nicShastaParms = _NicShastaParms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 7, 5)
)
_NicShastaParmTxNoResourcesCount_Type = Integer32
_NicShastaParmTxNoResourcesCount_Object = MibScalar
nicShastaParmTxNoResourcesCount = _NicShastaParmTxNoResourcesCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 7, 5, 1),
    _NicShastaParmTxNoResourcesCount_Type()
)
nicShastaParmTxNoResourcesCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nicShastaParmTxNoResourcesCount.setStatus("mandatory")
_NicShastaParmTxNoResourcesDelta_Type = Integer32
_NicShastaParmTxNoResourcesDelta_Object = MibScalar
nicShastaParmTxNoResourcesDelta = _NicShastaParmTxNoResourcesDelta_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 7, 5, 2),
    _NicShastaParmTxNoResourcesDelta_Type()
)
nicShastaParmTxNoResourcesDelta.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nicShastaParmTxNoResourcesDelta.setStatus("mandatory")


class _NicShastaParmTxNoResourcesPct_Type(DisplayString):
    """Custom type nicShastaParmTxNoResourcesPct based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_NicShastaParmTxNoResourcesPct_Type.__name__ = "DisplayString"
_NicShastaParmTxNoResourcesPct_Object = MibScalar
nicShastaParmTxNoResourcesPct = _NicShastaParmTxNoResourcesPct_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 7, 5, 3),
    _NicShastaParmTxNoResourcesPct_Type()
)
nicShastaParmTxNoResourcesPct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nicShastaParmTxNoResourcesPct.setStatus("mandatory")
_NicTokenRingStatistics_ObjectIdentity = ObjectIdentity
nicTokenRingStatistics = _NicTokenRingStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 8)
)
_NicTokenRingStatisticsTable_Object = MibTable
nicTokenRingStatisticsTable = _NicTokenRingStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 8, 1)
)
if mibBuilder.loadTexts:
    nicTokenRingStatisticsTable.setStatus("mandatory")
_NicTokenRingStatisticsEntry_Object = MibTableRow
nicTokenRingStatisticsEntry = _NicTokenRingStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 8, 1, 1)
)
nicTokenRingStatisticsEntry.setIndexNames(
    (0, "NSNICMIB-MIB", "nicTokenRingStatisticsIndex"),
)
if mibBuilder.loadTexts:
    nicTokenRingStatisticsEntry.setStatus("mandatory")
_NicTokenRingStatisticsIndex_Type = Integer32
_NicTokenRingStatisticsIndex_Object = MibTableColumn
nicTokenRingStatisticsIndex = _NicTokenRingStatisticsIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 8, 1, 1, 1),
    _NicTokenRingStatisticsIndex_Type()
)
nicTokenRingStatisticsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicTokenRingStatisticsIndex.setStatus("mandatory")
_NicFunctionalAddress_Type = OctetString
_NicFunctionalAddress_Object = MibTableColumn
nicFunctionalAddress = _NicFunctionalAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 8, 1, 1, 2),
    _NicFunctionalAddress_Type()
)
nicFunctionalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicFunctionalAddress.setStatus("mandatory")
_NicGroupAddress_Type = OctetString
_NicGroupAddress_Object = MibTableColumn
nicGroupAddress = _NicGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 8, 1, 1, 3),
    _NicGroupAddress_Type()
)
nicGroupAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicGroupAddress.setStatus("mandatory")
_NicLastOpenStatus_Type = Integer32
_NicLastOpenStatus_Object = MibTableColumn
nicLastOpenStatus = _NicLastOpenStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 8, 1, 1, 4),
    _NicLastOpenStatus_Type()
)
nicLastOpenStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicLastOpenStatus.setStatus("mandatory")


class _NicRingStatus_Type(Integer32):
    """Custom type nicRingStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              64,
              128,
              256,
              512,
              1024,
              2048,
              4096,
              8192,
              16384)
        )
    )
    namedValues = NamedValues(
        *(("autoremovalerror", 1024),
          ("counteroverflow", 256),
          ("harderror", 16384),
          ("lobewirefault", 2048),
          ("nostatus", 0),
          ("removereceived", 512),
          ("ringrecovery", 64),
          ("singlestation", 128),
          ("softerror", 8192),
          ("transmitbeacon", 4096))
    )


_NicRingStatus_Type.__name__ = "Integer32"
_NicRingStatus_Object = MibTableColumn
nicRingStatus = _NicRingStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 8, 1, 1, 5),
    _NicRingStatus_Type()
)
nicRingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicRingStatus.setStatus("mandatory")


class _NicRingState_Type(Integer32):
    """Custom type nicRingState based on Integer32"""
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
        *(("closed", 2),
          ("closing", 4),
          ("opened", 1),
          ("openfailure", 5),
          ("opening", 3),
          ("ringfailure", 6))
    )


_NicRingState_Type.__name__ = "Integer32"
_NicRingState_Object = MibTableColumn
nicRingState = _NicRingState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 8, 1, 1, 6),
    _NicRingState_Type()
)
nicRingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicRingState.setStatus("mandatory")
_NicTokenRingErrors_ObjectIdentity = ObjectIdentity
nicTokenRingErrors = _NicTokenRingErrors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 9)
)
_NicTokenRingErrorsTable_Object = MibTable
nicTokenRingErrorsTable = _NicTokenRingErrorsTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 9, 1)
)
if mibBuilder.loadTexts:
    nicTokenRingErrorsTable.setStatus("mandatory")
_NicTokenRingErrorsEntry_Object = MibTableRow
nicTokenRingErrorsEntry = _NicTokenRingErrorsEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 9, 1, 1)
)
nicTokenRingErrorsEntry.setIndexNames(
    (0, "NSNICMIB-MIB", "nicTokenRingErrorsIndex"),
)
if mibBuilder.loadTexts:
    nicTokenRingErrorsEntry.setStatus("mandatory")
_NicTokenRingErrorsIndex_Type = Integer32
_NicTokenRingErrorsIndex_Object = MibTableColumn
nicTokenRingErrorsIndex = _NicTokenRingErrorsIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 9, 1, 1, 1),
    _NicTokenRingErrorsIndex_Type()
)
nicTokenRingErrorsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicTokenRingErrorsIndex.setStatus("mandatory")
_NicLineErrors_Type = Integer32
_NicLineErrors_Object = MibTableColumn
nicLineErrors = _NicLineErrors_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 9, 1, 1, 2),
    _NicLineErrors_Type()
)
nicLineErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicLineErrors.setStatus("mandatory")
_NicLostFrames_Type = Integer32
_NicLostFrames_Object = MibTableColumn
nicLostFrames = _NicLostFrames_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 9, 1, 1, 3),
    _NicLostFrames_Type()
)
nicLostFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicLostFrames.setStatus("mandatory")
_NicBurstErrors_Type = Integer32
_NicBurstErrors_Object = MibTableColumn
nicBurstErrors = _NicBurstErrors_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 9, 1, 1, 4),
    _NicBurstErrors_Type()
)
nicBurstErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicBurstErrors.setStatus("mandatory")
_NicACErrors_Type = Integer32
_NicACErrors_Object = MibTableColumn
nicACErrors = _NicACErrors_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 9, 1, 1, 5),
    _NicACErrors_Type()
)
nicACErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicACErrors.setStatus("mandatory")
_NicAbortDelimiters_Type = Integer32
_NicAbortDelimiters_Object = MibTableColumn
nicAbortDelimiters = _NicAbortDelimiters_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 9, 1, 1, 6),
    _NicAbortDelimiters_Type()
)
nicAbortDelimiters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicAbortDelimiters.setStatus("mandatory")
_NicFrameCopiedErrors_Type = Integer32
_NicFrameCopiedErrors_Object = MibTableColumn
nicFrameCopiedErrors = _NicFrameCopiedErrors_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 9, 1, 1, 7),
    _NicFrameCopiedErrors_Type()
)
nicFrameCopiedErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicFrameCopiedErrors.setStatus("mandatory")
_NicFrequencyErrors_Type = Integer32
_NicFrequencyErrors_Object = MibTableColumn
nicFrequencyErrors = _NicFrequencyErrors_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 9, 1, 1, 8),
    _NicFrequencyErrors_Type()
)
nicFrequencyErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicFrequencyErrors.setStatus("mandatory")
_NicTokenErrors_Type = Integer32
_NicTokenErrors_Object = MibTableColumn
nicTokenErrors = _NicTokenErrors_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 9, 1, 1, 9),
    _NicTokenErrors_Type()
)
nicTokenErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicTokenErrors.setStatus("mandatory")
_NicInternalErrors_Type = Integer32
_NicInternalErrors_Object = MibTableColumn
nicInternalErrors = _NicInternalErrors_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 18, 9, 1, 1, 10),
    _NicInternalErrors_Type()
)
nicInternalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicInternalErrors.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NSNICMIB-MIB",
    **{"hp": hp,
       "nm": nm,
       "hpnsa": hpnsa,
       "nicObject": nicObject,
       "nicDrvConfig": nicDrvConfig,
       "nicDrvConfigTable": nicDrvConfigTable,
       "nicDrvConfigEntry": nicDrvConfigEntry,
       "nicDrvConfigIndex": nicDrvConfigIndex,
       "nicDrvcfgName": nicDrvcfgName,
       "nicDrvcfgDescript": nicDrvcfgDescript,
       "nicDrvcfgType": nicDrvcfgType,
       "nicDrvcfgPhyAddr": nicDrvcfgPhyAddr,
       "nicDrvcfgMajor": nicDrvcfgMajor,
       "nicDrvcfgMinor": nicDrvcfgMinor,
       "nicDrvcfgSlot": nicDrvcfgSlot,
       "nicDrvcfgIOport0": nicDrvcfgIOport0,
       "nicDrvcfgIOport1": nicDrvcfgIOport1,
       "nicDrvcfgInterrupt0": nicDrvcfgInterrupt0,
       "nicDrvcfgInterrupt1": nicDrvcfgInterrupt1,
       "nicDrvcfgDMA0": nicDrvcfgDMA0,
       "nicDrvcfgDMA1": nicDrvcfgDMA1,
       "nicDrvcfgMemory0": nicDrvcfgMemory0,
       "nicDrvcfgMemory1": nicDrvcfgMemory1,
       "nicDrvcfgMulticast": nicDrvcfgMulticast,
       "nicDrvcfgPromiscuous": nicDrvcfgPromiscuous,
       "nicDrvcfgMaximumSize": nicDrvcfgMaximumSize,
       "nicDrvcfgSpeed": nicDrvcfgSpeed,
       "nicDrvcfgTransportTime": nicDrvcfgTransportTime,
       "nicDrvcfgSendRetries": nicDrvcfgSendRetries,
       "nicDrvcfgMode": nicDrvcfgMode,
       "nicDrvcfgBindFrames": nicDrvcfgBindFrames,
       "nicDrvcfgAftGroupId": nicDrvcfgAftGroupId,
       "nicDrvcfgAftBusNo": nicDrvcfgAftBusNo,
       "nicDrvcfgAftBusDeviceId": nicDrvcfgAftBusDeviceId,
       "nicDrvcfgAftPciVenodrId": nicDrvcfgAftPciVenodrId,
       "nicDrvcfgAftPciDeviceId": nicDrvcfgAftPciDeviceId,
       "nicDrvcfgAftPciSubSysVendorId": nicDrvcfgAftPciSubSysVendorId,
       "nicDrvcfgAftPciSubSysDeviceId": nicDrvcfgAftPciSubSysDeviceId,
       "nicDrvcfgAftStatus": nicDrvcfgAftStatus,
       "nicDrvcfgAftMode": nicDrvcfgAftMode,
       "nicStatistics": nicStatistics,
       "nicStatisticsTable": nicStatisticsTable,
       "nicStatisticsEntry": nicStatisticsEntry,
       "nicStatisticsIndex": nicStatisticsIndex,
       "nicTtlTxPacket": nicTtlTxPacket,
       "nicDeltaTtlTxPacket": nicDeltaTtlTxPacket,
       "nicTtlRxPacket": nicTtlRxPacket,
       "nicDeltaTtlRxPacket": nicDeltaTtlRxPacket,
       "nicGetECBFails": nicGetECBFails,
       "nicTxTooBig": nicTxTooBig,
       "nicRxTooBig": nicRxTooBig,
       "nicRxOverflow": nicRxOverflow,
       "nicTxMisc": nicTxMisc,
       "nicRxMisc": nicRxMisc,
       "nicRxCRC": nicRxCRC,
       "nicTxOKByte": nicTxOKByte,
       "nicDeltaTxOKByte": nicDeltaTxOKByte,
       "nicRxOKByte": nicRxOKByte,
       "nicDeltaRxOKByte": nicDeltaRxOKByte,
       "nicTxGroup": nicTxGroup,
       "nicDeltaTxGroup": nicDeltaTxGroup,
       "nicRxGroup": nicRxGroup,
       "nicDeltaRxGroup": nicDeltaRxGroup,
       "nicAdapterReset": nicAdapterReset,
       "nicQDepth": nicQDepth,
       "nicRcvBuffers": nicRcvBuffers,
       "nicRcvBuffers75Pct": nicRcvBuffers75Pct,
       "nicRcvBuffersCkOut": nicRcvBuffersCkOut,
       "nicRcvBuffersMaxSize": nicRcvBuffersMaxSize,
       "nicNumCustCounter": nicNumCustCounter,
       "nicCustomStats": nicCustomStats,
       "nicCustStatTable": nicCustStatTable,
       "nicCustEntry": nicCustEntry,
       "nicCustIndex": nicCustIndex,
       "nicIndex": nicIndex,
       "nicCustCounter": nicCustCounter,
       "nicCustCounterString": nicCustCounterString,
       "nicErrors": nicErrors,
       "nicErrorsTable": nicErrorsTable,
       "nicErrorsEntry": nicErrorsEntry,
       "nicErrorsIndex": nicErrorsIndex,
       "nicTxOKSingleCollision": nicTxOKSingleCollision,
       "nicTxOKMultipleCollision": nicTxOKMultipleCollision,
       "nicTxOKDeferred": nicTxOKDeferred,
       "nicTxAbortLateCollision": nicTxAbortLateCollision,
       "nicTxAbortExcessCollision": nicTxAbortExcessCollision,
       "nicTxAbortCarrierSense": nicTxAbortCarrierSense,
       "nicTxAbortExcessiveDeferral": nicTxAbortExcessiveDeferral,
       "nicRxAbortFrameAlignment": nicRxAbortFrameAlignment,
       "nicHWRxMismatch": nicHWRxMismatch,
       "nicTtlTxErrPacket": nicTtlTxErrPacket,
       "nicTtlRxErrPacket": nicTtlRxErrPacket,
       "nicMiscellaneous": nicMiscellaneous,
       "nicNumBoards": nicNumBoards,
       "nicAdapterType": nicAdapterType,
       "nicFrameType": nicFrameType,
       "nicFrameTypeTable": nicFrameTypeTable,
       "nicFrameTypeEntry": nicFrameTypeEntry,
       "nicFrameTypeIndex": nicFrameTypeIndex,
       "nicCardIndex": nicCardIndex,
       "nicFrameTypeString": nicFrameTypeString,
       "nicParms": nicParms,
       "nicCommonParms": nicCommonParms,
       "nicParmSampling": nicParmSampling,
       "nicParmProcessing": nicParmProcessing,
       "nicParmRxErrCount": nicParmRxErrCount,
       "nicParmRxErrDelta": nicParmRxErrDelta,
       "nicParmRxErrPct": nicParmRxErrPct,
       "nicParmTxErrCount": nicParmTxErrCount,
       "nicParmTxErrDelta": nicParmTxErrDelta,
       "nicParmTxErrPct": nicParmTxErrPct,
       "nicParmAdapterResetCount": nicParmAdapterResetCount,
       "nicParmAdapterResetDelta": nicParmAdapterResetDelta,
       "nicParmAdapterResetPct": nicParmAdapterResetPct,
       "nicParmAlignmentCount": nicParmAlignmentCount,
       "nicParmAlignmentDelta": nicParmAlignmentDelta,
       "nicParmAlignmentPct": nicParmAlignmentPct,
       "nicParmFrameTooLongCount": nicParmFrameTooLongCount,
       "nicParmFrameTooLongDelta": nicParmFrameTooLongDelta,
       "nicParmFrameTooLongPct": nicParmFrameTooLongPct,
       "nicParmHardwareMismatchCount": nicParmHardwareMismatchCount,
       "nicParmHardwareMismatchDelta": nicParmHardwareMismatchDelta,
       "nicParmHardwareMismatchPct": nicParmHardwareMismatchPct,
       "nicParmLateCollisionCount": nicParmLateCollisionCount,
       "nicParmLateCollisionDelta": nicParmLateCollisionDelta,
       "nicParmLateCollisionPct": nicParmLateCollisionPct,
       "nicParmExcessCollisionCount": nicParmExcessCollisionCount,
       "nicParmExcessCollisionDelta": nicParmExcessCollisionDelta,
       "nicParmExcessCollisionPct": nicParmExcessCollisionPct,
       "nicParmCarrierSenseCount": nicParmCarrierSenseCount,
       "nicParmCarrierSenseDelta": nicParmCarrierSenseDelta,
       "nicParmCarrierSensePct": nicParmCarrierSensePct,
       "nicParmDeferralCount": nicParmDeferralCount,
       "nicParmDeferralDelta": nicParmDeferralDelta,
       "nicParmDeferralPct": nicParmDeferralPct,
       "nicParmNoECBCount": nicParmNoECBCount,
       "nicParmNoECBDelta": nicParmNoECBDelta,
       "nicParmNoECBPct": nicParmNoECBPct,
       "nicParmRxOverflowCount": nicParmRxOverflowCount,
       "nicParmRxOverflowDelta": nicParmRxOverflowDelta,
       "nicParmRxOverflowPct": nicParmRxOverflowPct,
       "nicParmUtilizationCount": nicParmUtilizationCount,
       "nicParmAdapterType": nicParmAdapterType,
       "nicParmLineErrCount": nicParmLineErrCount,
       "nicParmLineErrDelta": nicParmLineErrDelta,
       "nicParmLineErrPct": nicParmLineErrPct,
       "nicParmLostFramesCount": nicParmLostFramesCount,
       "nicParmLostFramesDelta": nicParmLostFramesDelta,
       "nicParmLostFramesPct": nicParmLostFramesPct,
       "nicParmBurstErrCount": nicParmBurstErrCount,
       "nicParmBurstErrDelta": nicParmBurstErrDelta,
       "nicParmBurstErrPct": nicParmBurstErrPct,
       "nicParmACErrCount": nicParmACErrCount,
       "nicParmACErrDelta": nicParmACErrDelta,
       "nicParmACErrPct": nicParmACErrPct,
       "nicParmAbortDelimitersCount": nicParmAbortDelimitersCount,
       "nicParmAbortDelimitersDelta": nicParmAbortDelimitersDelta,
       "nicParmAbortDelimitersPct": nicParmAbortDelimitersPct,
       "nicParmFrameCopiedErrCount": nicParmFrameCopiedErrCount,
       "nicParmFrameCopiedErrDelta": nicParmFrameCopiedErrDelta,
       "nicParmFrameCopiedErrPct": nicParmFrameCopiedErrPct,
       "nicParmFrequencyErrCount": nicParmFrequencyErrCount,
       "nicParmFrequencyErrDelta": nicParmFrequencyErrDelta,
       "nicParmFrequencyErrPct": nicParmFrequencyErrPct,
       "nicParmTokenErrCount": nicParmTokenErrCount,
       "nicParmTokenErrDelta": nicParmTokenErrDelta,
       "nicParmTokenErrPct": nicParmTokenErrPct,
       "nicParmInternalErrCount": nicParmInternalErrCount,
       "nicParmInternalErrDelta": nicParmInternalErrDelta,
       "nicParmInternalErrPct": nicParmInternalErrPct,
       "nicParmAftFailOverErrCount": nicParmAftFailOverErrCount,
       "nicParmAftFailOverErrDelta": nicParmAftFailOverErrDelta,
       "nicParmAftRecoveryErrCount": nicParmAftRecoveryErrCount,
       "nicParmAftRecoveryErrDelta": nicParmAftRecoveryErrDelta,
       "nicParmAftStandbyErrCount": nicParmAftStandbyErrCount,
       "nicParmAftStandbyErrDelta": nicParmAftStandbyErrDelta,
       "nicParmAftGruoupFailErrCount": nicParmAftGruoupFailErrCount,
       "nicParmAftGroupFailErrDelta": nicParmAftGroupFailErrDelta,
       "nicStarfighterParms": nicStarfighterParms,
       "nicStarfighterParmTxFifoCount": nicStarfighterParmTxFifoCount,
       "nicStarfighterParmTxFifoDelta": nicStarfighterParmTxFifoDelta,
       "nicStarfighterParmTxFifoPct": nicStarfighterParmTxFifoPct,
       "nicStarfighterParmTxTimedOutCount": nicStarfighterParmTxTimedOutCount,
       "nicStarfighterParmTxTimedOutDelta": nicStarfighterParmTxTimedOutDelta,
       "nicStarfighterParmTxTimedOutPct": nicStarfighterParmTxTimedOutPct,
       "nicStarfighterParmRxFifoCount": nicStarfighterParmRxFifoCount,
       "nicStarfighterParmRxFifoDelta": nicStarfighterParmRxFifoDelta,
       "nicStarfighterParmRxFifoPct": nicStarfighterParmRxFifoPct,
       "nicStarfighterParmRxFalseInterruptCount": nicStarfighterParmRxFalseInterruptCount,
       "nicStarfighterParmRxFalseInterruptDelta": nicStarfighterParmRxFalseInterruptDelta,
       "nicStarfighterParmRxFalseInterruptPct": nicStarfighterParmRxFalseInterruptPct,
       "nicStarfighterParmRxPagingErrCount": nicStarfighterParmRxPagingErrCount,
       "nicStarfighterParmRxPagingErrDelta": nicStarfighterParmRxPagingErrDelta,
       "nicStarfighterParmRxPagingErrPct": nicStarfighterParmRxPagingErrPct,
       "nicTwisterParms": nicTwisterParms,
       "nicTwisterParmTxFifoCount": nicTwisterParmTxFifoCount,
       "nicTwisterParmTxFifoDelta": nicTwisterParmTxFifoDelta,
       "nicTwisterParmTxFifoPct": nicTwisterParmTxFifoPct,
       "nicTwisterParmTxTimedOutCount": nicTwisterParmTxTimedOutCount,
       "nicTwisterParmTxTimedOutDelta": nicTwisterParmTxTimedOutDelta,
       "nicTwisterParmTxTimedOutPct": nicTwisterParmTxTimedOutPct,
       "nicTwisterParmRxFifoCount": nicTwisterParmRxFifoCount,
       "nicTwisterParmRxFifoDelta": nicTwisterParmRxFifoDelta,
       "nicTwisterParmRxFifoPct": nicTwisterParmRxFifoPct,
       "nicTwisterParmRxFalseInterruptCount": nicTwisterParmRxFalseInterruptCount,
       "nicTwisterParmRxFalseInterruptDelta": nicTwisterParmRxFalseInterruptDelta,
       "nicTwisterParmRxFalseInterruptPct": nicTwisterParmRxFalseInterruptPct,
       "nicTwisterParmRxPagingErrCount": nicTwisterParmRxPagingErrCount,
       "nicTwisterParmRxPagingErrDelta": nicTwisterParmRxPagingErrDelta,
       "nicTwisterParmRxPagingErrPct": nicTwisterParmRxPagingErrPct,
       "nicTwisterParmDMATimedOutCount": nicTwisterParmDMATimedOutCount,
       "nicTwisterParmDMATimedOutDelta": nicTwisterParmDMATimedOutDelta,
       "nicTwisterParmDMATimedOutPct": nicTwisterParmDMATimedOutPct,
       "nicMasterParms": nicMasterParms,
       "nicMasterParmTxNoResourcesCount": nicMasterParmTxNoResourcesCount,
       "nicMasterParmTxNoResourcesDelta": nicMasterParmTxNoResourcesDelta,
       "nicMasterParmTxNoResourcesPct": nicMasterParmTxNoResourcesPct,
       "nicMasterParmTxExcessFragsCount": nicMasterParmTxExcessFragsCount,
       "nicMasterParmTxExcessFragsDelta": nicMasterParmTxExcessFragsDelta,
       "nicMasterParmTxExcessFragsPct": nicMasterParmTxExcessFragsPct,
       "nicMasterParmRxLowCount": nicMasterParmRxLowCount,
       "nicMasterParmRxLowDelta": nicMasterParmRxLowDelta,
       "nicMasterParmRxLowPct": nicMasterParmRxLowPct,
       "nicMasterParmRxEmptyCount": nicMasterParmRxEmptyCount,
       "nicMasterParmRxEmptyDelta": nicMasterParmRxEmptyDelta,
       "nicMasterParmRxEmptyPct": nicMasterParmRxEmptyPct,
       "nicShastaParms": nicShastaParms,
       "nicShastaParmTxNoResourcesCount": nicShastaParmTxNoResourcesCount,
       "nicShastaParmTxNoResourcesDelta": nicShastaParmTxNoResourcesDelta,
       "nicShastaParmTxNoResourcesPct": nicShastaParmTxNoResourcesPct,
       "nicTokenRingStatistics": nicTokenRingStatistics,
       "nicTokenRingStatisticsTable": nicTokenRingStatisticsTable,
       "nicTokenRingStatisticsEntry": nicTokenRingStatisticsEntry,
       "nicTokenRingStatisticsIndex": nicTokenRingStatisticsIndex,
       "nicFunctionalAddress": nicFunctionalAddress,
       "nicGroupAddress": nicGroupAddress,
       "nicLastOpenStatus": nicLastOpenStatus,
       "nicRingStatus": nicRingStatus,
       "nicRingState": nicRingState,
       "nicTokenRingErrors": nicTokenRingErrors,
       "nicTokenRingErrorsTable": nicTokenRingErrorsTable,
       "nicTokenRingErrorsEntry": nicTokenRingErrorsEntry,
       "nicTokenRingErrorsIndex": nicTokenRingErrorsIndex,
       "nicLineErrors": nicLineErrors,
       "nicLostFrames": nicLostFrames,
       "nicBurstErrors": nicBurstErrors,
       "nicACErrors": nicACErrors,
       "nicAbortDelimiters": nicAbortDelimiters,
       "nicFrameCopiedErrors": nicFrameCopiedErrors,
       "nicFrequencyErrors": nicFrequencyErrors,
       "nicTokenErrors": nicTokenErrors,
       "nicInternalErrors": nicInternalErrors}
)
