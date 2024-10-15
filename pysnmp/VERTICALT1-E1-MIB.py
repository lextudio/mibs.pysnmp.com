# SNMP MIB module (VERTICALT1-E1-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/VERTICALT1-E1-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:12:23 2024
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Vertical_ObjectIdentity = ObjectIdentity
vertical = _Vertical_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2338)
)
_Vds1_ObjectIdentity = ObjectIdentity
vds1 = _Vds1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2338, 3)
)
_Vdsx1CardTable_Object = MibTable
vdsx1CardTable = _Vdsx1CardTable_Object(
    (1, 3, 6, 1, 4, 1, 2338, 3, 1)
)
if mibBuilder.loadTexts:
    vdsx1CardTable.setStatus("mandatory")
_Vdsx1CardEntry_Object = MibTableRow
vdsx1CardEntry = _Vdsx1CardEntry_Object(
    (1, 3, 6, 1, 4, 1, 2338, 3, 1, 1)
)
vdsx1CardEntry.setIndexNames(
    (0, "VERTICALT1-E1-MIB", "vdsx1cardSlotNumber"),
)
if mibBuilder.loadTexts:
    vdsx1CardEntry.setStatus("mandatory")


class _Vdsx1cardSlotNumber_Type(Integer32):
    """Custom type vdsx1cardSlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
    )


_Vdsx1cardSlotNumber_Type.__name__ = "Integer32"
_Vdsx1cardSlotNumber_Object = MibTableColumn
vdsx1cardSlotNumber = _Vdsx1cardSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 2338, 3, 1, 1, 1),
    _Vdsx1cardSlotNumber_Type()
)
vdsx1cardSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdsx1cardSlotNumber.setStatus("mandatory")


class _Vdsx1cardType_Type(Integer32):
    """Custom type vdsx1cardType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4,
              100)
        )
    )
    namedValues = NamedValues(
        *(("cardTYPE-8-CHANNEL-CO-POTS", 3),
          ("cardTYPE-BRIDGE1", 4),
          ("cardTYPE-DUAL-T1", 1),
          ("cardTYPE-NOT-CONFIGURED", 100))
    )


_Vdsx1cardType_Type.__name__ = "Integer32"
_Vdsx1cardType_Object = MibTableColumn
vdsx1cardType = _Vdsx1cardType_Object(
    (1, 3, 6, 1, 4, 1, 2338, 3, 1, 1, 2),
    _Vdsx1cardType_Type()
)
vdsx1cardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdsx1cardType.setStatus("mandatory")


class _Vdsx1cardDescr_Type(Integer32):
    """Custom type vdsx1cardDescr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Vdsx1cardDescr_Type.__name__ = "Integer32"
_Vdsx1cardDescr_Object = MibTableColumn
vdsx1cardDescr = _Vdsx1cardDescr_Object(
    (1, 3, 6, 1, 4, 1, 2338, 3, 1, 1, 3),
    _Vdsx1cardDescr_Type()
)
vdsx1cardDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdsx1cardDescr.setStatus("mandatory")


class _Vdsx1cardRevision_Type(Integer32):
    """Custom type vdsx1cardRevision based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Vdsx1cardRevision_Type.__name__ = "Integer32"
_Vdsx1cardRevision_Object = MibTableColumn
vdsx1cardRevision = _Vdsx1cardRevision_Object(
    (1, 3, 6, 1, 4, 1, 2338, 3, 1, 1, 4),
    _Vdsx1cardRevision_Type()
)
vdsx1cardRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdsx1cardRevision.setStatus("mandatory")


class _Vdsx1cardDriverVersion_Type(Integer32):
    """Custom type vdsx1cardDriverVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Vdsx1cardDriverVersion_Type.__name__ = "Integer32"
_Vdsx1cardDriverVersion_Object = MibTableColumn
vdsx1cardDriverVersion = _Vdsx1cardDriverVersion_Object(
    (1, 3, 6, 1, 4, 1, 2338, 3, 1, 1, 5),
    _Vdsx1cardDriverVersion_Type()
)
vdsx1cardDriverVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdsx1cardDriverVersion.setStatus("mandatory")


class _Vdsx1cardIOPortAddress_Type(Integer32):
    """Custom type vdsx1cardIOPortAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Vdsx1cardIOPortAddress_Type.__name__ = "Integer32"
_Vdsx1cardIOPortAddress_Object = MibTableColumn
vdsx1cardIOPortAddress = _Vdsx1cardIOPortAddress_Object(
    (1, 3, 6, 1, 4, 1, 2338, 3, 1, 1, 6),
    _Vdsx1cardIOPortAddress_Type()
)
vdsx1cardIOPortAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdsx1cardIOPortAddress.setStatus("mandatory")


class _Vdsx1cardErrorLED_Type(Integer32):
    """Custom type vdsx1cardErrorLED based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Vdsx1cardErrorLED_Type.__name__ = "Integer32"
_Vdsx1cardErrorLED_Object = MibTableColumn
vdsx1cardErrorLED = _Vdsx1cardErrorLED_Object(
    (1, 3, 6, 1, 4, 1, 2338, 3, 1, 1, 7),
    _Vdsx1cardErrorLED_Type()
)
vdsx1cardErrorLED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdsx1cardErrorLED.setStatus("mandatory")


class _Vdsx1cardReadyLED_Type(Integer32):
    """Custom type vdsx1cardReadyLED based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Vdsx1cardReadyLED_Type.__name__ = "Integer32"
_Vdsx1cardReadyLED_Object = MibTableColumn
vdsx1cardReadyLED = _Vdsx1cardReadyLED_Object(
    (1, 3, 6, 1, 4, 1, 2338, 3, 1, 1, 8),
    _Vdsx1cardReadyLED_Type()
)
vdsx1cardReadyLED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdsx1cardReadyLED.setStatus("mandatory")
_Vdsx1TrunkTable_Object = MibTable
vdsx1TrunkTable = _Vdsx1TrunkTable_Object(
    (1, 3, 6, 1, 4, 1, 2338, 3, 2)
)
if mibBuilder.loadTexts:
    vdsx1TrunkTable.setStatus("mandatory")
_Vdsx1TrunkEntry_Object = MibTableRow
vdsx1TrunkEntry = _Vdsx1TrunkEntry_Object(
    (1, 3, 6, 1, 4, 1, 2338, 3, 2, 1)
)
vdsx1TrunkEntry.setIndexNames(
    (0, "VERTICALT1-E1-MIB", "vdsx1TrunkIfIndex"),
)
if mibBuilder.loadTexts:
    vdsx1TrunkEntry.setStatus("mandatory")


class _Vdsx1TrunkIfIndex_Type(Integer32):
    """Custom type vdsx1TrunkIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Vdsx1TrunkIfIndex_Type.__name__ = "Integer32"
_Vdsx1TrunkIfIndex_Object = MibTableColumn
vdsx1TrunkIfIndex = _Vdsx1TrunkIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2338, 3, 2, 1, 1),
    _Vdsx1TrunkIfIndex_Type()
)
vdsx1TrunkIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdsx1TrunkIfIndex.setStatus("mandatory")


class _Vdsx1TrunkIndex_Type(Integer32):
    """Custom type vdsx1TrunkIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Vdsx1TrunkIndex_Type.__name__ = "Integer32"
_Vdsx1TrunkIndex_Object = MibTableColumn
vdsx1TrunkIndex = _Vdsx1TrunkIndex_Object(
    (1, 3, 6, 1, 4, 1, 2338, 3, 2, 1, 2),
    _Vdsx1TrunkIndex_Type()
)
vdsx1TrunkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdsx1TrunkIndex.setStatus("mandatory")


class _Vdsx1TrunkIdentifier_Type(DisplayString):
    """Custom type vdsx1TrunkIdentifier based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Vdsx1TrunkIdentifier_Type.__name__ = "DisplayString"
_Vdsx1TrunkIdentifier_Object = MibTableColumn
vdsx1TrunkIdentifier = _Vdsx1TrunkIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 2338, 3, 2, 1, 3),
    _Vdsx1TrunkIdentifier_Type()
)
vdsx1TrunkIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdsx1TrunkIdentifier.setStatus("mandatory")


class _Vdsx1TrunkSlotNumber_Type(Integer32):
    """Custom type vdsx1TrunkSlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Vdsx1TrunkSlotNumber_Type.__name__ = "Integer32"
_Vdsx1TrunkSlotNumber_Object = MibTableColumn
vdsx1TrunkSlotNumber = _Vdsx1TrunkSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 2338, 3, 2, 1, 4),
    _Vdsx1TrunkSlotNumber_Type()
)
vdsx1TrunkSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdsx1TrunkSlotNumber.setStatus("mandatory")


class _Vdsx1TrunkDeviceNumber_Type(Integer32):
    """Custom type vdsx1TrunkDeviceNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Vdsx1TrunkDeviceNumber_Type.__name__ = "Integer32"
_Vdsx1TrunkDeviceNumber_Object = MibTableColumn
vdsx1TrunkDeviceNumber = _Vdsx1TrunkDeviceNumber_Object(
    (1, 3, 6, 1, 4, 1, 2338, 3, 2, 1, 5),
    _Vdsx1TrunkDeviceNumber_Type()
)
vdsx1TrunkDeviceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdsx1TrunkDeviceNumber.setStatus("mandatory")


class _Vdsx1TrunkInterrupt_Type(Integer32):
    """Custom type vdsx1TrunkInterrupt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Vdsx1TrunkInterrupt_Type.__name__ = "Integer32"
_Vdsx1TrunkInterrupt_Object = MibTableColumn
vdsx1TrunkInterrupt = _Vdsx1TrunkInterrupt_Object(
    (1, 3, 6, 1, 4, 1, 2338, 3, 2, 1, 6),
    _Vdsx1TrunkInterrupt_Type()
)
vdsx1TrunkInterrupt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdsx1TrunkInterrupt.setStatus("mandatory")


class _Vdsx1TrunkEnabled_Type(Integer32):
    """Custom type vdsx1TrunkEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              100)
        )
    )
    namedValues = NamedValues(
        *(("vdsx1TrunkActivated", 1),
          ("vdsx1TrunkDeactivated", 100),
          ("vdsx1TrunkNotConfigured", 2))
    )


_Vdsx1TrunkEnabled_Type.__name__ = "Integer32"
_Vdsx1TrunkEnabled_Object = MibTableColumn
vdsx1TrunkEnabled = _Vdsx1TrunkEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2338, 3, 2, 1, 7),
    _Vdsx1TrunkEnabled_Type()
)
vdsx1TrunkEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vdsx1TrunkEnabled.setStatus("mandatory")


class _Vdsx1TrunkMasterPriority_Type(Integer32):
    """Custom type vdsx1TrunkMasterPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              100)
        )
    )
    namedValues = NamedValues(
        *(("firstAlternate", 2),
          ("notUsed", 100),
          ("primary", 1),
          ("secondAlternate", 3))
    )


_Vdsx1TrunkMasterPriority_Type.__name__ = "Integer32"
_Vdsx1TrunkMasterPriority_Object = MibTableColumn
vdsx1TrunkMasterPriority = _Vdsx1TrunkMasterPriority_Object(
    (1, 3, 6, 1, 4, 1, 2338, 3, 2, 1, 8),
    _Vdsx1TrunkMasterPriority_Type()
)
vdsx1TrunkMasterPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vdsx1TrunkMasterPriority.setStatus("mandatory")


class _Vdsx1TrunkStream_Type(Integer32):
    """Custom type vdsx1TrunkStream based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Vdsx1TrunkStream_Type.__name__ = "Integer32"
_Vdsx1TrunkStream_Object = MibTableColumn
vdsx1TrunkStream = _Vdsx1TrunkStream_Object(
    (1, 3, 6, 1, 4, 1, 2338, 3, 2, 1, 9),
    _Vdsx1TrunkStream_Type()
)
vdsx1TrunkStream.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdsx1TrunkStream.setStatus("mandatory")


class _Vdsx1TrunkStartingChannel_Type(Integer32):
    """Custom type vdsx1TrunkStartingChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24),
    )


_Vdsx1TrunkStartingChannel_Type.__name__ = "Integer32"
_Vdsx1TrunkStartingChannel_Object = MibTableColumn
vdsx1TrunkStartingChannel = _Vdsx1TrunkStartingChannel_Object(
    (1, 3, 6, 1, 4, 1, 2338, 3, 2, 1, 10),
    _Vdsx1TrunkStartingChannel_Type()
)
vdsx1TrunkStartingChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdsx1TrunkStartingChannel.setStatus("mandatory")


class _Vdsx1TrunkType_Type(Integer32):
    """Custom type vdsx1TrunkType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              7,
              100)
        )
    )
    namedValues = NamedValues(
        *(("dev-coPots", 7),
          ("dev-t1CAS", 1),
          ("dev-t1CCS", 2),
          ("dev-undef", 100))
    )


_Vdsx1TrunkType_Type.__name__ = "Integer32"
_Vdsx1TrunkType_Object = MibTableColumn
vdsx1TrunkType = _Vdsx1TrunkType_Object(
    (1, 3, 6, 1, 4, 1, 2338, 3, 2, 1, 11),
    _Vdsx1TrunkType_Type()
)
vdsx1TrunkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdsx1TrunkType.setStatus("mandatory")


class _Vdsx1TrunkIsdnSignalingProtocol_Type(Integer32):
    """Custom type vdsx1TrunkIsdnSignalingProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              5,
              6,
              7,
              10,
              263)
        )
    )
    namedValues = NamedValues(
        *(("dms100", 7),
          ("dms100s100", 263),
          ("ess4", 5),
          ("ess5", 6),
          ("ni2", 10),
          ("other", 1))
    )


_Vdsx1TrunkIsdnSignalingProtocol_Type.__name__ = "Integer32"
_Vdsx1TrunkIsdnSignalingProtocol_Object = MibTableColumn
vdsx1TrunkIsdnSignalingProtocol = _Vdsx1TrunkIsdnSignalingProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2338, 3, 2, 1, 12),
    _Vdsx1TrunkIsdnSignalingProtocol_Type()
)
vdsx1TrunkIsdnSignalingProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vdsx1TrunkIsdnSignalingProtocol.setStatus("mandatory")


class _Vdsx1TrunkLineCoding_Type(Integer32):
    """Custom type vdsx1TrunkLineCoding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("ami", 5),
          ("b8zs", 2),
          ("other", 6))
    )


_Vdsx1TrunkLineCoding_Type.__name__ = "Integer32"
_Vdsx1TrunkLineCoding_Object = MibTableColumn
vdsx1TrunkLineCoding = _Vdsx1TrunkLineCoding_Object(
    (1, 3, 6, 1, 4, 1, 2338, 3, 2, 1, 13),
    _Vdsx1TrunkLineCoding_Type()
)
vdsx1TrunkLineCoding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vdsx1TrunkLineCoding.setStatus("mandatory")


class _Vdsx1TrunkFraming_Type(Integer32):
    """Custom type vdsx1TrunkFraming based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("d4", 3),
          ("esf", 2),
          ("other", 1))
    )


_Vdsx1TrunkFraming_Type.__name__ = "Integer32"
_Vdsx1TrunkFraming_Object = MibTableColumn
vdsx1TrunkFraming = _Vdsx1TrunkFraming_Object(
    (1, 3, 6, 1, 4, 1, 2338, 3, 2, 1, 14),
    _Vdsx1TrunkFraming_Type()
)
vdsx1TrunkFraming.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vdsx1TrunkFraming.setStatus("mandatory")


class _Vdsx1TrunkDChannelSlot_Type(Integer32):
    """Custom type vdsx1TrunkDChannelSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 18),
    )


_Vdsx1TrunkDChannelSlot_Type.__name__ = "Integer32"
_Vdsx1TrunkDChannelSlot_Object = MibTableColumn
vdsx1TrunkDChannelSlot = _Vdsx1TrunkDChannelSlot_Object(
    (1, 3, 6, 1, 4, 1, 2338, 3, 2, 1, 15),
    _Vdsx1TrunkDChannelSlot_Type()
)
vdsx1TrunkDChannelSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vdsx1TrunkDChannelSlot.setStatus("mandatory")


class _Vdsx1TrunkDChannelDevice_Type(Integer32):
    """Custom type vdsx1TrunkDChannelDevice based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_Vdsx1TrunkDChannelDevice_Type.__name__ = "Integer32"
_Vdsx1TrunkDChannelDevice_Object = MibTableColumn
vdsx1TrunkDChannelDevice = _Vdsx1TrunkDChannelDevice_Object(
    (1, 3, 6, 1, 4, 1, 2338, 3, 2, 1, 16),
    _Vdsx1TrunkDChannelDevice_Type()
)
vdsx1TrunkDChannelDevice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vdsx1TrunkDChannelDevice.setStatus("mandatory")


class _Vdsx1TrunkNumberOfChannels_Type(Integer32):
    """Custom type vdsx1TrunkNumberOfChannels based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24),
    )


_Vdsx1TrunkNumberOfChannels_Type.__name__ = "Integer32"
_Vdsx1TrunkNumberOfChannels_Object = MibTableColumn
vdsx1TrunkNumberOfChannels = _Vdsx1TrunkNumberOfChannels_Object(
    (1, 3, 6, 1, 4, 1, 2338, 3, 2, 1, 17),
    _Vdsx1TrunkNumberOfChannels_Type()
)
vdsx1TrunkNumberOfChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdsx1TrunkNumberOfChannels.setStatus("mandatory")


class _Vdsx1TrunkLineBuildOut_Type(Integer32):
    """Custom type vdsx1TrunkLineBuildOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              100)
        )
    )
    namedValues = NamedValues(
        *(("buildOut-0dB", 2),
          ("buildOut-minus15dB", 1),
          ("buildOut-minus7point5dB", 3),
          ("notApplicable", 100))
    )


_Vdsx1TrunkLineBuildOut_Type.__name__ = "Integer32"
_Vdsx1TrunkLineBuildOut_Object = MibTableColumn
vdsx1TrunkLineBuildOut = _Vdsx1TrunkLineBuildOut_Object(
    (1, 3, 6, 1, 4, 1, 2338, 3, 2, 1, 18),
    _Vdsx1TrunkLineBuildOut_Type()
)
vdsx1TrunkLineBuildOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vdsx1TrunkLineBuildOut.setStatus("mandatory")


class _Vdsx1TrunkLoopback_Type(Integer32):
    """Custom type vdsx1TrunkLoopback based on Integer32"""
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
        *(("vdsx1LineLoop", 3),
          ("vdsx1NoLoop", 1),
          ("vdsx1OtherLoop", 4),
          ("vdsx1PayloadLoop", 2))
    )


_Vdsx1TrunkLoopback_Type.__name__ = "Integer32"
_Vdsx1TrunkLoopback_Object = MibTableColumn
vdsx1TrunkLoopback = _Vdsx1TrunkLoopback_Object(
    (1, 3, 6, 1, 4, 1, 2338, 3, 2, 1, 19),
    _Vdsx1TrunkLoopback_Type()
)
vdsx1TrunkLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vdsx1TrunkLoopback.setStatus("mandatory")


class _Vdsx1TrunkRedLED_Type(Integer32):
    """Custom type vdsx1TrunkRedLED based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Vdsx1TrunkRedLED_Type.__name__ = "Integer32"
_Vdsx1TrunkRedLED_Object = MibTableColumn
vdsx1TrunkRedLED = _Vdsx1TrunkRedLED_Object(
    (1, 3, 6, 1, 4, 1, 2338, 3, 2, 1, 20),
    _Vdsx1TrunkRedLED_Type()
)
vdsx1TrunkRedLED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdsx1TrunkRedLED.setStatus("mandatory")


class _Vdsx1TrunkYellowLED_Type(Integer32):
    """Custom type vdsx1TrunkYellowLED based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Vdsx1TrunkYellowLED_Type.__name__ = "Integer32"
_Vdsx1TrunkYellowLED_Object = MibTableColumn
vdsx1TrunkYellowLED = _Vdsx1TrunkYellowLED_Object(
    (1, 3, 6, 1, 4, 1, 2338, 3, 2, 1, 21),
    _Vdsx1TrunkYellowLED_Type()
)
vdsx1TrunkYellowLED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdsx1TrunkYellowLED.setStatus("mandatory")


class _Vdsx1TrunkChangePending_Type(Integer32):
    """Custom type vdsx1TrunkChangePending based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Vdsx1TrunkChangePending_Type.__name__ = "Integer32"
_Vdsx1TrunkChangePending_Object = MibTableColumn
vdsx1TrunkChangePending = _Vdsx1TrunkChangePending_Object(
    (1, 3, 6, 1, 4, 1, 2338, 3, 2, 1, 22),
    _Vdsx1TrunkChangePending_Type()
)
vdsx1TrunkChangePending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdsx1TrunkChangePending.setStatus("mandatory")
_Vdsx1ChannelTable_Object = MibTable
vdsx1ChannelTable = _Vdsx1ChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 2338, 3, 9)
)
if mibBuilder.loadTexts:
    vdsx1ChannelTable.setStatus("mandatory")
_Vdsx1ChannelEntry_Object = MibTableRow
vdsx1ChannelEntry = _Vdsx1ChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 2338, 3, 9, 1)
)
vdsx1ChannelEntry.setIndexNames(
    (0, "VERTICALT1-E1-MIB", "vdsx1TrunkIfIndex"),
    (0, "VERTICALT1-E1-MIB", "vdsx1channelIndex"),
)
if mibBuilder.loadTexts:
    vdsx1ChannelEntry.setStatus("mandatory")


class _Vdsx1channelIndex_Type(Integer32):
    """Custom type vdsx1channelIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_Vdsx1channelIndex_Type.__name__ = "Integer32"
_Vdsx1channelIndex_Object = MibTableColumn
vdsx1channelIndex = _Vdsx1channelIndex_Object(
    (1, 3, 6, 1, 4, 1, 2338, 3, 9, 1, 1),
    _Vdsx1channelIndex_Type()
)
vdsx1channelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdsx1channelIndex.setStatus("mandatory")


class _Vdsx1channelTrunkIndex_Type(Integer32):
    """Custom type vdsx1channelTrunkIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Vdsx1channelTrunkIndex_Type.__name__ = "Integer32"
_Vdsx1channelTrunkIndex_Object = MibTableColumn
vdsx1channelTrunkIndex = _Vdsx1channelTrunkIndex_Object(
    (1, 3, 6, 1, 4, 1, 2338, 3, 9, 1, 2),
    _Vdsx1channelTrunkIndex_Type()
)
vdsx1channelTrunkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdsx1channelTrunkIndex.setStatus("mandatory")


class _Vdsx1channelSlotNumber_Type(Integer32):
    """Custom type vdsx1channelSlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Vdsx1channelSlotNumber_Type.__name__ = "Integer32"
_Vdsx1channelSlotNumber_Object = MibTableColumn
vdsx1channelSlotNumber = _Vdsx1channelSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 2338, 3, 9, 1, 3),
    _Vdsx1channelSlotNumber_Type()
)
vdsx1channelSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdsx1channelSlotNumber.setStatus("mandatory")


class _Vdsx1channelTrunkDeviceNumber_Type(Integer32):
    """Custom type vdsx1channelTrunkDeviceNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Vdsx1channelTrunkDeviceNumber_Type.__name__ = "Integer32"
_Vdsx1channelTrunkDeviceNumber_Object = MibTableColumn
vdsx1channelTrunkDeviceNumber = _Vdsx1channelTrunkDeviceNumber_Object(
    (1, 3, 6, 1, 4, 1, 2338, 3, 9, 1, 4),
    _Vdsx1channelTrunkDeviceNumber_Type()
)
vdsx1channelTrunkDeviceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdsx1channelTrunkDeviceNumber.setStatus("mandatory")


class _Vdsx1channelEnabled_Type(Integer32):
    """Custom type vdsx1channelEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              100)
        )
    )
    namedValues = NamedValues(
        *(("vdsx1channelActivated", 1),
          ("vdsx1channelDeactivated", 100),
          ("vdsx1channelNotConfigured", 2))
    )


_Vdsx1channelEnabled_Type.__name__ = "Integer32"
_Vdsx1channelEnabled_Object = MibTableColumn
vdsx1channelEnabled = _Vdsx1channelEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2338, 3, 9, 1, 5),
    _Vdsx1channelEnabled_Type()
)
vdsx1channelEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vdsx1channelEnabled.setStatus("mandatory")


class _Vdsx1channelType_Type(Integer32):
    """Custom type vdsx1channelType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              5,
              6,
              7,
              8,
              9,
              11,
              12,
              13,
              14,
              100)
        )
    )
    namedValues = NamedValues(
        *(("vdsx1channelTypeAnalogDID", 14),
          ("vdsx1channelTypeAnalogDt", 11),
          ("vdsx1channelTypeAnalogGs", 12),
          ("vdsx1channelTypeAnalogImm", 7),
          ("vdsx1channelTypeBChan", 8),
          ("vdsx1channelTypeClear", 6),
          ("vdsx1channelTypeDChan", 9),
          ("vdsx1channelTypeDDS", 13),
          ("vdsx1channelTypeGS", 5),
          ("vdsx1channelTypeUnknown", 100),
          ("vdsx1channelTypeWink", 2))
    )


_Vdsx1channelType_Type.__name__ = "Integer32"
_Vdsx1channelType_Object = MibTableColumn
vdsx1channelType = _Vdsx1channelType_Object(
    (1, 3, 6, 1, 4, 1, 2338, 3, 9, 1, 6),
    _Vdsx1channelType_Type()
)
vdsx1channelType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdsx1channelType.setStatus("mandatory")


class _Vdsx1channelState_Type(Integer32):
    """Custom type vdsx1channelState based on Integer32"""
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
              9,
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
        *(("channelStateData", 7),
          ("channelStateDigitRcv", 12),
          ("channelStateDigitSend", 11),
          ("channelStateError", 8),
          ("channelStateFeRinging", 9),
          ("channelStateIdle", 2),
          ("channelStateInCall", 3),
          ("channelStateIncallClear", 15),
          ("channelStateIncallEst", 13),
          ("channelStateNeRinging", 10),
          ("channelStateOOS", 1),
          ("channelStateOffline", 5),
          ("channelStateOther", 6),
          ("channelStateOutCall", 4),
          ("channelStateOutcallClear", 16),
          ("channelStateOutcallEst", 14))
    )


_Vdsx1channelState_Type.__name__ = "Integer32"
_Vdsx1channelState_Object = MibTableColumn
vdsx1channelState = _Vdsx1channelState_Object(
    (1, 3, 6, 1, 4, 1, 2338, 3, 9, 1, 7),
    _Vdsx1channelState_Type()
)
vdsx1channelState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vdsx1channelState.setStatus("mandatory")


class _Vdsx1channelCallerID_Type(DisplayString):
    """Custom type vdsx1channelCallerID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Vdsx1channelCallerID_Type.__name__ = "DisplayString"
_Vdsx1channelCallerID_Object = MibTableColumn
vdsx1channelCallerID = _Vdsx1channelCallerID_Object(
    (1, 3, 6, 1, 4, 1, 2338, 3, 9, 1, 8),
    _Vdsx1channelCallerID_Type()
)
vdsx1channelCallerID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vdsx1channelCallerID.setStatus("mandatory")


class _Vdsx1channelExternalAddress_Type(DisplayString):
    """Custom type vdsx1channelExternalAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Vdsx1channelExternalAddress_Type.__name__ = "DisplayString"
_Vdsx1channelExternalAddress_Object = MibTableColumn
vdsx1channelExternalAddress = _Vdsx1channelExternalAddress_Object(
    (1, 3, 6, 1, 4, 1, 2338, 3, 9, 1, 9),
    _Vdsx1channelExternalAddress_Type()
)
vdsx1channelExternalAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vdsx1channelExternalAddress.setStatus("mandatory")


class _Vdsx1channelExternalSubAddress_Type(DisplayString):
    """Custom type vdsx1channelExternalSubAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Vdsx1channelExternalSubAddress_Type.__name__ = "DisplayString"
_Vdsx1channelExternalSubAddress_Object = MibTableColumn
vdsx1channelExternalSubAddress = _Vdsx1channelExternalSubAddress_Object(
    (1, 3, 6, 1, 4, 1, 2338, 3, 9, 1, 10),
    _Vdsx1channelExternalSubAddress_Type()
)
vdsx1channelExternalSubAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vdsx1channelExternalSubAddress.setStatus("mandatory")


class _Vdsx1channelLocalAddress_Type(DisplayString):
    """Custom type vdsx1channelLocalAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Vdsx1channelLocalAddress_Type.__name__ = "DisplayString"
_Vdsx1channelLocalAddress_Object = MibTableColumn
vdsx1channelLocalAddress = _Vdsx1channelLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 2338, 3, 9, 1, 11),
    _Vdsx1channelLocalAddress_Type()
)
vdsx1channelLocalAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vdsx1channelLocalAddress.setStatus("mandatory")


class _Vdsx1channelLocalSubAddress_Type(DisplayString):
    """Custom type vdsx1channelLocalSubAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Vdsx1channelLocalSubAddress_Type.__name__ = "DisplayString"
_Vdsx1channelLocalSubAddress_Object = MibTableColumn
vdsx1channelLocalSubAddress = _Vdsx1channelLocalSubAddress_Object(
    (1, 3, 6, 1, 4, 1, 2338, 3, 9, 1, 12),
    _Vdsx1channelLocalSubAddress_Type()
)
vdsx1channelLocalSubAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vdsx1channelLocalSubAddress.setStatus("mandatory")


class _Vdsx1channelChangePending_Type(Integer32):
    """Custom type vdsx1channelChangePending based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Vdsx1channelChangePending_Type.__name__ = "Integer32"
_Vdsx1channelChangePending_Object = MibTableColumn
vdsx1channelChangePending = _Vdsx1channelChangePending_Object(
    (1, 3, 6, 1, 4, 1, 2338, 3, 9, 1, 13),
    _Vdsx1channelChangePending_Type()
)
vdsx1channelChangePending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdsx1channelChangePending.setStatus("mandatory")

# Managed Objects groups


# Notification objects

vdsx1TrunkRedClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2338, 0, 1)
)
vdsx1TrunkRedClear.setObjects(
      *(("VERTICALT1-E1-MIB", "vdsx1TrunkIdentifier"),
        ("VERTICALT1-E1-MIB", "vdsx1cardSlotNumber"),
        ("VERTICALT1-E1-MIB", "vdsx1TrunkDeviceNumber"),
        ("VERTICALT1-E1-MIB", "vdsx1TrunkIndex"))
)
if mibBuilder.loadTexts:
    vdsx1TrunkRedClear.setStatus(
        ""
    )

vdsx1TrunkRed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2338, 0, 2)
)
vdsx1TrunkRed.setObjects(
      *(("VERTICALT1-E1-MIB", "vdsx1TrunkIdentifier"),
        ("VERTICALT1-E1-MIB", "vdsx1cardSlotNumber"),
        ("VERTICALT1-E1-MIB", "vdsx1TrunkDeviceNumber"),
        ("VERTICALT1-E1-MIB", "vdsx1TrunkIndex"))
)
if mibBuilder.loadTexts:
    vdsx1TrunkRed.setStatus(
        ""
    )

vdsx1TrunkYellowClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2338, 0, 3)
)
vdsx1TrunkYellowClear.setObjects(
      *(("VERTICALT1-E1-MIB", "vdsx1TrunkIdentifier"),
        ("VERTICALT1-E1-MIB", "vdsx1cardSlotNumber"),
        ("VERTICALT1-E1-MIB", "vdsx1TrunkDeviceNumber"),
        ("VERTICALT1-E1-MIB", "vdsx1TrunkIndex"))
)
if mibBuilder.loadTexts:
    vdsx1TrunkYellowClear.setStatus(
        ""
    )

vdsx1TrunkYellow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2338, 0, 4)
)
vdsx1TrunkYellow.setObjects(
      *(("VERTICALT1-E1-MIB", "vdsx1TrunkIdentifier"),
        ("VERTICALT1-E1-MIB", "vdsx1cardSlotNumber"),
        ("VERTICALT1-E1-MIB", "vdsx1TrunkDeviceNumber"),
        ("VERTICALT1-E1-MIB", "vdsx1TrunkIndex"))
)
if mibBuilder.loadTexts:
    vdsx1TrunkYellow.setStatus(
        ""
    )

vdsx1TrunkBlueClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2338, 0, 5)
)
vdsx1TrunkBlueClear.setObjects(
      *(("VERTICALT1-E1-MIB", "vdsx1TrunkIdentifier"),
        ("VERTICALT1-E1-MIB", "vdsx1cardSlotNumber"),
        ("VERTICALT1-E1-MIB", "vdsx1TrunkDeviceNumber"),
        ("VERTICALT1-E1-MIB", "vdsx1TrunkIndex"))
)
if mibBuilder.loadTexts:
    vdsx1TrunkBlueClear.setStatus(
        ""
    )

vdsx1TrunkBlue = NotificationType(
    (1, 3, 6, 1, 4, 1, 2338, 0, 6)
)
vdsx1TrunkBlue.setObjects(
      *(("VERTICALT1-E1-MIB", "vdsx1TrunkIdentifier"),
        ("VERTICALT1-E1-MIB", "vdsx1cardSlotNumber"),
        ("VERTICALT1-E1-MIB", "vdsx1TrunkDeviceNumber"),
        ("VERTICALT1-E1-MIB", "vdsx1TrunkIndex"))
)
if mibBuilder.loadTexts:
    vdsx1TrunkBlue.setStatus(
        ""
    )

vdsx1TrunkReconfigComplete = NotificationType(
    (1, 3, 6, 1, 4, 1, 2338, 0, 7)
)
vdsx1TrunkReconfigComplete.setObjects(
      *(("VERTICALT1-E1-MIB", "vdsx1TrunkIdentifier"),
        ("VERTICALT1-E1-MIB", "vdsx1cardSlotNumber"),
        ("VERTICALT1-E1-MIB", "vdsx1TrunkDeviceNumber"),
        ("VERTICALT1-E1-MIB", "vdsx1TrunkIndex"))
)
if mibBuilder.loadTexts:
    vdsx1TrunkReconfigComplete.setStatus(
        ""
    )

vdsx1TrunkReconfigError = NotificationType(
    (1, 3, 6, 1, 4, 1, 2338, 0, 8)
)
vdsx1TrunkReconfigError.setObjects(
      *(("VERTICALT1-E1-MIB", "vdsx1TrunkIdentifier"),
        ("VERTICALT1-E1-MIB", "vdsx1cardSlotNumber"),
        ("VERTICALT1-E1-MIB", "vdsx1TrunkDeviceNumber"),
        ("VERTICALT1-E1-MIB", "vdsx1TrunkIndex"))
)
if mibBuilder.loadTexts:
    vdsx1TrunkReconfigError.setStatus(
        ""
    )

vdsx1TrunkLoopbackPayloadOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 2338, 0, 43)
)
vdsx1TrunkLoopbackPayloadOn.setObjects(
      *(("VERTICALT1-E1-MIB", "vdsx1TrunkIdentifier"),
        ("VERTICALT1-E1-MIB", "vdsx1cardSlotNumber"),
        ("VERTICALT1-E1-MIB", "vdsx1TrunkDeviceNumber"),
        ("VERTICALT1-E1-MIB", "vdsx1TrunkIndex"))
)
if mibBuilder.loadTexts:
    vdsx1TrunkLoopbackPayloadOn.setStatus(
        ""
    )

vdsx1TrunkLoopbackPayloadOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 2338, 0, 44)
)
vdsx1TrunkLoopbackPayloadOff.setObjects(
      *(("VERTICALT1-E1-MIB", "vdsx1TrunkIdentifier"),
        ("VERTICALT1-E1-MIB", "vdsx1cardSlotNumber"),
        ("VERTICALT1-E1-MIB", "vdsx1TrunkDeviceNumber"),
        ("VERTICALT1-E1-MIB", "vdsx1TrunkIndex"))
)
if mibBuilder.loadTexts:
    vdsx1TrunkLoopbackPayloadOff.setStatus(
        ""
    )

vdsx1TrunkLoopbackLineOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 2338, 0, 45)
)
vdsx1TrunkLoopbackLineOn.setObjects(
      *(("VERTICALT1-E1-MIB", "vdsx1TrunkIdentifier"),
        ("VERTICALT1-E1-MIB", "vdsx1cardSlotNumber"),
        ("VERTICALT1-E1-MIB", "vdsx1TrunkDeviceNumber"),
        ("VERTICALT1-E1-MIB", "vdsx1TrunkIndex"))
)
if mibBuilder.loadTexts:
    vdsx1TrunkLoopbackLineOn.setStatus(
        ""
    )

vdsx1TrunkLoopbackLineOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 2338, 0, 46)
)
vdsx1TrunkLoopbackLineOff.setObjects(
      *(("VERTICALT1-E1-MIB", "vdsx1TrunkIdentifier"),
        ("VERTICALT1-E1-MIB", "vdsx1cardSlotNumber"),
        ("VERTICALT1-E1-MIB", "vdsx1TrunkDeviceNumber"),
        ("VERTICALT1-E1-MIB", "vdsx1TrunkIndex"))
)
if mibBuilder.loadTexts:
    vdsx1TrunkLoopbackLineOff.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VERTICALT1-E1-MIB",
    **{"vertical": vertical,
       "vdsx1TrunkRedClear": vdsx1TrunkRedClear,
       "vdsx1TrunkRed": vdsx1TrunkRed,
       "vdsx1TrunkYellowClear": vdsx1TrunkYellowClear,
       "vdsx1TrunkYellow": vdsx1TrunkYellow,
       "vdsx1TrunkBlueClear": vdsx1TrunkBlueClear,
       "vdsx1TrunkBlue": vdsx1TrunkBlue,
       "vdsx1TrunkReconfigComplete": vdsx1TrunkReconfigComplete,
       "vdsx1TrunkReconfigError": vdsx1TrunkReconfigError,
       "vdsx1TrunkLoopbackPayloadOn": vdsx1TrunkLoopbackPayloadOn,
       "vdsx1TrunkLoopbackPayloadOff": vdsx1TrunkLoopbackPayloadOff,
       "vdsx1TrunkLoopbackLineOn": vdsx1TrunkLoopbackLineOn,
       "vdsx1TrunkLoopbackLineOff": vdsx1TrunkLoopbackLineOff,
       "vds1": vds1,
       "vdsx1CardTable": vdsx1CardTable,
       "vdsx1CardEntry": vdsx1CardEntry,
       "vdsx1cardSlotNumber": vdsx1cardSlotNumber,
       "vdsx1cardType": vdsx1cardType,
       "vdsx1cardDescr": vdsx1cardDescr,
       "vdsx1cardRevision": vdsx1cardRevision,
       "vdsx1cardDriverVersion": vdsx1cardDriverVersion,
       "vdsx1cardIOPortAddress": vdsx1cardIOPortAddress,
       "vdsx1cardErrorLED": vdsx1cardErrorLED,
       "vdsx1cardReadyLED": vdsx1cardReadyLED,
       "vdsx1TrunkTable": vdsx1TrunkTable,
       "vdsx1TrunkEntry": vdsx1TrunkEntry,
       "vdsx1TrunkIfIndex": vdsx1TrunkIfIndex,
       "vdsx1TrunkIndex": vdsx1TrunkIndex,
       "vdsx1TrunkIdentifier": vdsx1TrunkIdentifier,
       "vdsx1TrunkSlotNumber": vdsx1TrunkSlotNumber,
       "vdsx1TrunkDeviceNumber": vdsx1TrunkDeviceNumber,
       "vdsx1TrunkInterrupt": vdsx1TrunkInterrupt,
       "vdsx1TrunkEnabled": vdsx1TrunkEnabled,
       "vdsx1TrunkMasterPriority": vdsx1TrunkMasterPriority,
       "vdsx1TrunkStream": vdsx1TrunkStream,
       "vdsx1TrunkStartingChannel": vdsx1TrunkStartingChannel,
       "vdsx1TrunkType": vdsx1TrunkType,
       "vdsx1TrunkIsdnSignalingProtocol": vdsx1TrunkIsdnSignalingProtocol,
       "vdsx1TrunkLineCoding": vdsx1TrunkLineCoding,
       "vdsx1TrunkFraming": vdsx1TrunkFraming,
       "vdsx1TrunkDChannelSlot": vdsx1TrunkDChannelSlot,
       "vdsx1TrunkDChannelDevice": vdsx1TrunkDChannelDevice,
       "vdsx1TrunkNumberOfChannels": vdsx1TrunkNumberOfChannels,
       "vdsx1TrunkLineBuildOut": vdsx1TrunkLineBuildOut,
       "vdsx1TrunkLoopback": vdsx1TrunkLoopback,
       "vdsx1TrunkRedLED": vdsx1TrunkRedLED,
       "vdsx1TrunkYellowLED": vdsx1TrunkYellowLED,
       "vdsx1TrunkChangePending": vdsx1TrunkChangePending,
       "vdsx1ChannelTable": vdsx1ChannelTable,
       "vdsx1ChannelEntry": vdsx1ChannelEntry,
       "vdsx1channelIndex": vdsx1channelIndex,
       "vdsx1channelTrunkIndex": vdsx1channelTrunkIndex,
       "vdsx1channelSlotNumber": vdsx1channelSlotNumber,
       "vdsx1channelTrunkDeviceNumber": vdsx1channelTrunkDeviceNumber,
       "vdsx1channelEnabled": vdsx1channelEnabled,
       "vdsx1channelType": vdsx1channelType,
       "vdsx1channelState": vdsx1channelState,
       "vdsx1channelCallerID": vdsx1channelCallerID,
       "vdsx1channelExternalAddress": vdsx1channelExternalAddress,
       "vdsx1channelExternalSubAddress": vdsx1channelExternalSubAddress,
       "vdsx1channelLocalAddress": vdsx1channelLocalAddress,
       "vdsx1channelLocalSubAddress": vdsx1channelLocalSubAddress,
       "vdsx1channelChangePending": vdsx1channelChangePending}
)
