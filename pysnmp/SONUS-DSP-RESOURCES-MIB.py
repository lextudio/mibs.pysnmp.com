# SNMP MIB module (SONUS-DSP-RESOURCES-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SONUS-DSP-RESOURCES-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:56:56 2024
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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")

(sonusEventClass,
 sonusEventDescription,
 sonusEventLevel,
 sonusShelfIndex) = mibBuilder.importSymbols(
    "SONUS-COMMON-MIB",
    "sonusEventClass",
    "sonusEventDescription",
    "sonusEventLevel",
    "sonusShelfIndex")

(sonusResourcesMIBs,) = mibBuilder.importSymbols(
    "SONUS-SMI",
    "sonusResourcesMIBs")

(SonusAdminState,
 SonusName,
 SonusShelfIndex) = mibBuilder.importSymbols(
    "SONUS-TC",
    "SonusAdminState",
    "SonusName",
    "SonusShelfIndex")


# MODULE-IDENTITY

sonusDspResourcesMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SonusDspResourcesMIBObjects_ObjectIdentity = ObjectIdentity
sonusDspResourcesMIBObjects = _SonusDspResourcesMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 1, 1)
)
_SonusChannelStatTable_ObjectIdentity = ObjectIdentity
sonusChannelStatTable = _SonusChannelStatTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 1, 1, 1)
)
_SonusDspAdmnTable_Object = MibTable
sonusDspAdmnTable = _SonusDspAdmnTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 1, 1, 2)
)
if mibBuilder.loadTexts:
    sonusDspAdmnTable.setStatus("current")
_SonusDspAdmnEntry_Object = MibTableRow
sonusDspAdmnEntry = _SonusDspAdmnEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 1, 1, 2, 1)
)
sonusDspAdmnEntry.setIndexNames(
    (0, "SONUS-DSP-RESOURCES-MIB", "sonusDspAdmnShelfIndex"),
    (0, "SONUS-DSP-RESOURCES-MIB", "sonusDspAdmnSlotIndex"),
    (0, "SONUS-DSP-RESOURCES-MIB", "sonusDspAdmnDspIndex"),
)
if mibBuilder.loadTexts:
    sonusDspAdmnEntry.setStatus("current")
_SonusDspAdmnShelfIndex_Type = Integer32
_SonusDspAdmnShelfIndex_Object = MibTableColumn
sonusDspAdmnShelfIndex = _SonusDspAdmnShelfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 1, 1, 2, 1, 1),
    _SonusDspAdmnShelfIndex_Type()
)
sonusDspAdmnShelfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusDspAdmnShelfIndex.setStatus("current")
_SonusDspAdmnSlotIndex_Type = Integer32
_SonusDspAdmnSlotIndex_Object = MibTableColumn
sonusDspAdmnSlotIndex = _SonusDspAdmnSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 1, 1, 2, 1, 2),
    _SonusDspAdmnSlotIndex_Type()
)
sonusDspAdmnSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusDspAdmnSlotIndex.setStatus("current")
_SonusDspAdmnDspIndex_Type = Integer32
_SonusDspAdmnDspIndex_Object = MibTableColumn
sonusDspAdmnDspIndex = _SonusDspAdmnDspIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 1, 1, 2, 1, 3),
    _SonusDspAdmnDspIndex_Type()
)
sonusDspAdmnDspIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusDspAdmnDspIndex.setStatus("current")


class _SonusDspAdmnType_Type(Integer32):
    """Custom type sonusDspAdmnType based on Integer32"""
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
        *(("g729AB", 3),
          ("hdlc", 2),
          ("tone", 4),
          ("vpad", 1))
    )


_SonusDspAdmnType_Type.__name__ = "Integer32"
_SonusDspAdmnType_Object = MibTableColumn
sonusDspAdmnType = _SonusDspAdmnType_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 1, 1, 2, 1, 4),
    _SonusDspAdmnType_Type()
)
sonusDspAdmnType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDspAdmnType.setStatus("current")
_SonusDspAdmnNumChannels_Type = Integer32
_SonusDspAdmnNumChannels_Object = MibTableColumn
sonusDspAdmnNumChannels = _SonusDspAdmnNumChannels_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 1, 1, 2, 1, 5),
    _SonusDspAdmnNumChannels_Type()
)
sonusDspAdmnNumChannels.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDspAdmnNumChannels.setStatus("current")


class _SonusDspAdmnMaxTail_Type(Integer32):
    """Custom type sonusDspAdmnMaxTail based on Integer32"""
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
        *(("millisec32", 2),
          ("millisec48", 3),
          ("millisec64", 4),
          ("millisecs24", 1))
    )


_SonusDspAdmnMaxTail_Type.__name__ = "Integer32"
_SonusDspAdmnMaxTail_Object = MibTableColumn
sonusDspAdmnMaxTail = _SonusDspAdmnMaxTail_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 1, 1, 2, 1, 6),
    _SonusDspAdmnMaxTail_Type()
)
sonusDspAdmnMaxTail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDspAdmnMaxTail.setStatus("current")


class _SonusDspAdmnEcAudioType_Type(Integer32):
    """Custom type sonusDspAdmnEcAudioType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("aLaw", 2),
          ("uLaw", 1))
    )


_SonusDspAdmnEcAudioType_Type.__name__ = "Integer32"
_SonusDspAdmnEcAudioType_Object = MibTableColumn
sonusDspAdmnEcAudioType = _SonusDspAdmnEcAudioType_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 1, 1, 2, 1, 7),
    _SonusDspAdmnEcAudioType_Type()
)
sonusDspAdmnEcAudioType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDspAdmnEcAudioType.setStatus("current")


class _SonusDspAdmnEcSignallingTone_Type(Integer32):
    """Custom type sonusDspAdmnEcSignallingTone based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("c5", 2),
          ("none", 1))
    )


_SonusDspAdmnEcSignallingTone_Type.__name__ = "Integer32"
_SonusDspAdmnEcSignallingTone_Object = MibTableColumn
sonusDspAdmnEcSignallingTone = _SonusDspAdmnEcSignallingTone_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 1, 1, 2, 1, 8),
    _SonusDspAdmnEcSignallingTone_Type()
)
sonusDspAdmnEcSignallingTone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDspAdmnEcSignallingTone.setStatus("current")


class _SonusDspAdmnNlpDisable_Type(Integer32):
    """Custom type sonusDspAdmnNlpDisable based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_SonusDspAdmnNlpDisable_Type.__name__ = "Integer32"
_SonusDspAdmnNlpDisable_Object = MibTableColumn
sonusDspAdmnNlpDisable = _SonusDspAdmnNlpDisable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 1, 1, 2, 1, 9),
    _SonusDspAdmnNlpDisable_Type()
)
sonusDspAdmnNlpDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDspAdmnNlpDisable.setStatus("current")


class _SonusDspAdmnNlpEnable_Type(Integer32):
    """Custom type sonusDspAdmnNlpEnable based on Integer32"""
    defaultValue = 12

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_SonusDspAdmnNlpEnable_Type.__name__ = "Integer32"
_SonusDspAdmnNlpEnable_Object = MibTableColumn
sonusDspAdmnNlpEnable = _SonusDspAdmnNlpEnable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 1, 1, 2, 1, 10),
    _SonusDspAdmnNlpEnable_Type()
)
sonusDspAdmnNlpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDspAdmnNlpEnable.setStatus("current")


class _SonusDspAdmnJitterEvalPeriod_Type(Integer32):
    """Custom type sonusDspAdmnJitterEvalPeriod based on Integer32"""
    defaultValue = 800

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SonusDspAdmnJitterEvalPeriod_Type.__name__ = "Integer32"
_SonusDspAdmnJitterEvalPeriod_Object = MibTableColumn
sonusDspAdmnJitterEvalPeriod = _SonusDspAdmnJitterEvalPeriod_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 1, 1, 2, 1, 11),
    _SonusDspAdmnJitterEvalPeriod_Type()
)
sonusDspAdmnJitterEvalPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDspAdmnJitterEvalPeriod.setStatus("current")


class _SonusDspAdmnJitterMinOccThsh_Type(Integer32):
    """Custom type sonusDspAdmnJitterMinOccThsh based on Integer32"""
    defaultValue = 160

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 65535),
    )


_SonusDspAdmnJitterMinOccThsh_Type.__name__ = "Integer32"
_SonusDspAdmnJitterMinOccThsh_Object = MibTableColumn
sonusDspAdmnJitterMinOccThsh = _SonusDspAdmnJitterMinOccThsh_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 1, 1, 2, 1, 12),
    _SonusDspAdmnJitterMinOccThsh_Type()
)
sonusDspAdmnJitterMinOccThsh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDspAdmnJitterMinOccThsh.setStatus("current")


class _SonusDspResidualEchoControl_Type(Integer32):
    """Custom type sonusDspResidualEchoControl based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("cancelOnly", 1),
          ("comfortNoise", 4),
          ("suppressResidual", 2))
    )


_SonusDspResidualEchoControl_Type.__name__ = "Integer32"
_SonusDspResidualEchoControl_Object = MibTableColumn
sonusDspResidualEchoControl = _SonusDspResidualEchoControl_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 1, 1, 2, 1, 13),
    _SonusDspResidualEchoControl_Type()
)
sonusDspResidualEchoControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDspResidualEchoControl.setStatus("current")


class _SonusDspEchoReturnLoss_Type(Integer32):
    """Custom type sonusDspEchoReturnLoss based on Integer32"""
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
        *(("dB0", 3),
          ("dB3", 2),
          ("dB6", 1))
    )


_SonusDspEchoReturnLoss_Type.__name__ = "Integer32"
_SonusDspEchoReturnLoss_Object = MibTableColumn
sonusDspEchoReturnLoss = _SonusDspEchoReturnLoss_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 1, 1, 2, 1, 14),
    _SonusDspEchoReturnLoss_Type()
)
sonusDspEchoReturnLoss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDspEchoReturnLoss.setStatus("current")


class _SonusDspModemDisable_Type(Integer32):
    """Custom type sonusDspModemDisable based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("g164", 2),
          ("g165", 4),
          ("ignore2100Hz", 1))
    )


_SonusDspModemDisable_Type.__name__ = "Integer32"
_SonusDspModemDisable_Object = MibTableColumn
sonusDspModemDisable = _SonusDspModemDisable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 1, 1, 2, 1, 15),
    _SonusDspModemDisable_Type()
)
sonusDspModemDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDspModemDisable.setStatus("current")


class _SonusDspHighLevelComp_Type(Integer32):
    """Custom type sonusDspHighLevelComp based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dB6", 2),
          ("none", 1))
    )


_SonusDspHighLevelComp_Type.__name__ = "Integer32"
_SonusDspHighLevelComp_Object = MibTableColumn
sonusDspHighLevelComp = _SonusDspHighLevelComp_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 1, 1, 2, 1, 16),
    _SonusDspHighLevelComp_Type()
)
sonusDspHighLevelComp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDspHighLevelComp.setStatus("current")
_SonusDspStatTable_ObjectIdentity = ObjectIdentity
sonusDspStatTable = _SonusDspStatTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 1, 1, 3)
)
_SonusDspSlotStatTable_Object = MibTable
sonusDspSlotStatTable = _SonusDspSlotStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 1, 1, 4)
)
if mibBuilder.loadTexts:
    sonusDspSlotStatTable.setStatus("current")
_SonusDspSlotStatEntry_Object = MibTableRow
sonusDspSlotStatEntry = _SonusDspSlotStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 1, 1, 4, 1)
)
sonusDspSlotStatEntry.setIndexNames(
    (0, "SONUS-DSP-RESOURCES-MIB", "sonusDspSlotStatShelfIndex"),
    (0, "SONUS-DSP-RESOURCES-MIB", "sonusDspSlotStatSlotIndex"),
)
if mibBuilder.loadTexts:
    sonusDspSlotStatEntry.setStatus("current")
_SonusDspSlotStatShelfIndex_Type = Integer32
_SonusDspSlotStatShelfIndex_Object = MibTableColumn
sonusDspSlotStatShelfIndex = _SonusDspSlotStatShelfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 1, 1, 4, 1, 1),
    _SonusDspSlotStatShelfIndex_Type()
)
sonusDspSlotStatShelfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusDspSlotStatShelfIndex.setStatus("current")
_SonusDspSlotStatSlotIndex_Type = Integer32
_SonusDspSlotStatSlotIndex_Object = MibTableColumn
sonusDspSlotStatSlotIndex = _SonusDspSlotStatSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 1, 1, 4, 1, 2),
    _SonusDspSlotStatSlotIndex_Type()
)
sonusDspSlotStatSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusDspSlotStatSlotIndex.setStatus("current")
_SonusDspSlotStatG711EcTotal_Type = Integer32
_SonusDspSlotStatG711EcTotal_Object = MibTableColumn
sonusDspSlotStatG711EcTotal = _SonusDspSlotStatG711EcTotal_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 1, 1, 4, 1, 3),
    _SonusDspSlotStatG711EcTotal_Type()
)
sonusDspSlotStatG711EcTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusDspSlotStatG711EcTotal.setStatus("current")
_SonusDspSlotStatG711Total_Type = Integer32
_SonusDspSlotStatG711Total_Object = MibTableColumn
sonusDspSlotStatG711Total = _SonusDspSlotStatG711Total_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 1, 1, 4, 1, 4),
    _SonusDspSlotStatG711Total_Type()
)
sonusDspSlotStatG711Total.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusDspSlotStatG711Total.setStatus("current")
_SonusDspSlotStatHdlcTotal_Type = Integer32
_SonusDspSlotStatHdlcTotal_Object = MibTableColumn
sonusDspSlotStatHdlcTotal = _SonusDspSlotStatHdlcTotal_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 1, 1, 4, 1, 5),
    _SonusDspSlotStatHdlcTotal_Type()
)
sonusDspSlotStatHdlcTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusDspSlotStatHdlcTotal.setStatus("current")
_SonusDspSlotStatToneTotal_Type = Integer32
_SonusDspSlotStatToneTotal_Object = MibTableColumn
sonusDspSlotStatToneTotal = _SonusDspSlotStatToneTotal_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 1, 1, 4, 1, 6),
    _SonusDspSlotStatToneTotal_Type()
)
sonusDspSlotStatToneTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusDspSlotStatToneTotal.setStatus("current")
_SonusDspSlotStatG729AbTotal_Type = Integer32
_SonusDspSlotStatG729AbTotal_Object = MibTableColumn
sonusDspSlotStatG729AbTotal = _SonusDspSlotStatG729AbTotal_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 1, 1, 4, 1, 7),
    _SonusDspSlotStatG729AbTotal_Type()
)
sonusDspSlotStatG729AbTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusDspSlotStatG729AbTotal.setStatus("current")
_SonusDspSlotStatG711EcUtilization_Type = Integer32
_SonusDspSlotStatG711EcUtilization_Object = MibTableColumn
sonusDspSlotStatG711EcUtilization = _SonusDspSlotStatG711EcUtilization_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 1, 1, 4, 1, 8),
    _SonusDspSlotStatG711EcUtilization_Type()
)
sonusDspSlotStatG711EcUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusDspSlotStatG711EcUtilization.setStatus("current")
_SonusDspSlotStatG711EcAllocFailures_Type = Integer32
_SonusDspSlotStatG711EcAllocFailures_Object = MibTableColumn
sonusDspSlotStatG711EcAllocFailures = _SonusDspSlotStatG711EcAllocFailures_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 1, 1, 4, 1, 9),
    _SonusDspSlotStatG711EcAllocFailures_Type()
)
sonusDspSlotStatG711EcAllocFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusDspSlotStatG711EcAllocFailures.setStatus("current")
_SonusDspSlotStatG711Utilization_Type = Integer32
_SonusDspSlotStatG711Utilization_Object = MibTableColumn
sonusDspSlotStatG711Utilization = _SonusDspSlotStatG711Utilization_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 1, 1, 4, 1, 10),
    _SonusDspSlotStatG711Utilization_Type()
)
sonusDspSlotStatG711Utilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusDspSlotStatG711Utilization.setStatus("current")
_SonusDspSlotStatG711AllocFailures_Type = Integer32
_SonusDspSlotStatG711AllocFailures_Object = MibTableColumn
sonusDspSlotStatG711AllocFailures = _SonusDspSlotStatG711AllocFailures_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 1, 1, 4, 1, 11),
    _SonusDspSlotStatG711AllocFailures_Type()
)
sonusDspSlotStatG711AllocFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusDspSlotStatG711AllocFailures.setStatus("current")
_SonusDspSlotStatHdlcUtilization_Type = Integer32
_SonusDspSlotStatHdlcUtilization_Object = MibTableColumn
sonusDspSlotStatHdlcUtilization = _SonusDspSlotStatHdlcUtilization_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 1, 1, 4, 1, 12),
    _SonusDspSlotStatHdlcUtilization_Type()
)
sonusDspSlotStatHdlcUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusDspSlotStatHdlcUtilization.setStatus("current")
_SonusDspSlotStatHdlcAllocFailures_Type = Integer32
_SonusDspSlotStatHdlcAllocFailures_Object = MibTableColumn
sonusDspSlotStatHdlcAllocFailures = _SonusDspSlotStatHdlcAllocFailures_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 1, 1, 4, 1, 13),
    _SonusDspSlotStatHdlcAllocFailures_Type()
)
sonusDspSlotStatHdlcAllocFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusDspSlotStatHdlcAllocFailures.setStatus("current")
_SonusDspSlotStatToneUtilization_Type = Integer32
_SonusDspSlotStatToneUtilization_Object = MibTableColumn
sonusDspSlotStatToneUtilization = _SonusDspSlotStatToneUtilization_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 1, 1, 4, 1, 14),
    _SonusDspSlotStatToneUtilization_Type()
)
sonusDspSlotStatToneUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusDspSlotStatToneUtilization.setStatus("current")
_SonusDspSlotStatToneAllocFailures_Type = Integer32
_SonusDspSlotStatToneAllocFailures_Object = MibTableColumn
sonusDspSlotStatToneAllocFailures = _SonusDspSlotStatToneAllocFailures_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 1, 1, 4, 1, 15),
    _SonusDspSlotStatToneAllocFailures_Type()
)
sonusDspSlotStatToneAllocFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusDspSlotStatToneAllocFailures.setStatus("current")
_SonusDspSlotStatG729AbUtilization_Type = Integer32
_SonusDspSlotStatG729AbUtilization_Object = MibTableColumn
sonusDspSlotStatG729AbUtilization = _SonusDspSlotStatG729AbUtilization_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 1, 1, 4, 1, 16),
    _SonusDspSlotStatG729AbUtilization_Type()
)
sonusDspSlotStatG729AbUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusDspSlotStatG729AbUtilization.setStatus("current")
_SonusDspSlotStatG729AbAllocFailures_Type = Integer32
_SonusDspSlotStatG729AbAllocFailures_Object = MibTableColumn
sonusDspSlotStatG729AbAllocFailures = _SonusDspSlotStatG729AbAllocFailures_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 1, 1, 4, 1, 17),
    _SonusDspSlotStatG729AbAllocFailures_Type()
)
sonusDspSlotStatG729AbAllocFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusDspSlotStatG729AbAllocFailures.setStatus("current")
_SonusPadAdmnTable_Object = MibTable
sonusPadAdmnTable = _SonusPadAdmnTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 1, 1, 5)
)
if mibBuilder.loadTexts:
    sonusPadAdmnTable.setStatus("current")
_SonusPadAdmnEntry_Object = MibTableRow
sonusPadAdmnEntry = _SonusPadAdmnEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 1, 1, 5, 1)
)
sonusPadAdmnEntry.setIndexNames(
    (0, "SONUS-DSP-RESOURCES-MIB", "sonusPadAdmnShelfIndex"),
)
if mibBuilder.loadTexts:
    sonusPadAdmnEntry.setStatus("current")
_SonusPadAdmnShelfIndex_Type = SonusShelfIndex
_SonusPadAdmnShelfIndex_Object = MibTableColumn
sonusPadAdmnShelfIndex = _SonusPadAdmnShelfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 1, 1, 5, 1, 1),
    _SonusPadAdmnShelfIndex_Type()
)
sonusPadAdmnShelfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusPadAdmnShelfIndex.setStatus("current")


class _SonusPadAdmnJitterEvalPeriod_Type(Integer32):
    """Custom type sonusPadAdmnJitterEvalPeriod based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 300000),
    )


_SonusPadAdmnJitterEvalPeriod_Type.__name__ = "Integer32"
_SonusPadAdmnJitterEvalPeriod_Object = MibTableColumn
sonusPadAdmnJitterEvalPeriod = _SonusPadAdmnJitterEvalPeriod_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 1, 1, 5, 1, 2),
    _SonusPadAdmnJitterEvalPeriod_Type()
)
sonusPadAdmnJitterEvalPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusPadAdmnJitterEvalPeriod.setStatus("current")


class _SonusPadAdmnJitterMinOccThsh_Type(Integer32):
    """Custom type sonusPadAdmnJitterMinOccThsh based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 200),
    )


_SonusPadAdmnJitterMinOccThsh_Type.__name__ = "Integer32"
_SonusPadAdmnJitterMinOccThsh_Object = MibTableColumn
sonusPadAdmnJitterMinOccThsh = _SonusPadAdmnJitterMinOccThsh_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 1, 1, 5, 1, 3),
    _SonusPadAdmnJitterMinOccThsh_Type()
)
sonusPadAdmnJitterMinOccThsh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusPadAdmnJitterMinOccThsh.setStatus("current")


class _SonusPadAdmnRtpG711ALaw_Type(Integer32):
    """Custom type sonusPadAdmnRtpG711ALaw based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_SonusPadAdmnRtpG711ALaw_Type.__name__ = "Integer32"
_SonusPadAdmnRtpG711ALaw_Object = MibTableColumn
sonusPadAdmnRtpG711ALaw = _SonusPadAdmnRtpG711ALaw_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 1, 1, 5, 1, 4),
    _SonusPadAdmnRtpG711ALaw_Type()
)
sonusPadAdmnRtpG711ALaw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusPadAdmnRtpG711ALaw.setStatus("obsolete")


class _SonusPadAdmnRtpG711ULaw_Type(Integer32):
    """Custom type sonusPadAdmnRtpG711ULaw based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_SonusPadAdmnRtpG711ULaw_Type.__name__ = "Integer32"
_SonusPadAdmnRtpG711ULaw_Object = MibTableColumn
sonusPadAdmnRtpG711ULaw = _SonusPadAdmnRtpG711ULaw_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 1, 1, 5, 1, 5),
    _SonusPadAdmnRtpG711ULaw_Type()
)
sonusPadAdmnRtpG711ULaw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusPadAdmnRtpG711ULaw.setStatus("obsolete")


class _SonusPadAdmnRtpG729A_Type(Integer32):
    """Custom type sonusPadAdmnRtpG729A based on Integer32"""
    defaultValue = 18

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_SonusPadAdmnRtpG729A_Type.__name__ = "Integer32"
_SonusPadAdmnRtpG729A_Object = MibTableColumn
sonusPadAdmnRtpG729A = _SonusPadAdmnRtpG729A_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 1, 1, 5, 1, 6),
    _SonusPadAdmnRtpG729A_Type()
)
sonusPadAdmnRtpG729A.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusPadAdmnRtpG729A.setStatus("obsolete")


class _SonusPadAdmnRtpG729AB_Type(Integer32):
    """Custom type sonusPadAdmnRtpG729AB based on Integer32"""
    defaultValue = 18

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_SonusPadAdmnRtpG729AB_Type.__name__ = "Integer32"
_SonusPadAdmnRtpG729AB_Object = MibTableColumn
sonusPadAdmnRtpG729AB = _SonusPadAdmnRtpG729AB_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 1, 1, 5, 1, 7),
    _SonusPadAdmnRtpG729AB_Type()
)
sonusPadAdmnRtpG729AB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusPadAdmnRtpG729AB.setStatus("obsolete")


class _SonusPadAdmnG729ABThreshold_Type(Integer32):
    """Custom type sonusPadAdmnG729ABThreshold based on Integer32"""
    defaultValue = 90

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_SonusPadAdmnG729ABThreshold_Type.__name__ = "Integer32"
_SonusPadAdmnG729ABThreshold_Object = MibTableColumn
sonusPadAdmnG729ABThreshold = _SonusPadAdmnG729ABThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 1, 1, 5, 1, 8),
    _SonusPadAdmnG729ABThreshold_Type()
)
sonusPadAdmnG729ABThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusPadAdmnG729ABThreshold.setStatus("current")


class _SonusPadAdmnG729ABThresholdState_Type(SonusAdminState):
    """Custom type sonusPadAdmnG729ABThresholdState based on SonusAdminState"""


_SonusPadAdmnG729ABThresholdState_Object = MibTableColumn
sonusPadAdmnG729ABThresholdState = _SonusPadAdmnG729ABThresholdState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 1, 1, 5, 1, 9),
    _SonusPadAdmnG729ABThresholdState_Type()
)
sonusPadAdmnG729ABThresholdState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusPadAdmnG729ABThresholdState.setStatus("current")


class _SonusPadAdmnToneThreshold_Type(Integer32):
    """Custom type sonusPadAdmnToneThreshold based on Integer32"""
    defaultValue = 90

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_SonusPadAdmnToneThreshold_Type.__name__ = "Integer32"
_SonusPadAdmnToneThreshold_Object = MibTableColumn
sonusPadAdmnToneThreshold = _SonusPadAdmnToneThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 1, 1, 5, 1, 10),
    _SonusPadAdmnToneThreshold_Type()
)
sonusPadAdmnToneThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusPadAdmnToneThreshold.setStatus("current")


class _SonusPadAdmnToneThresholdState_Type(SonusAdminState):
    """Custom type sonusPadAdmnToneThresholdState based on SonusAdminState"""


_SonusPadAdmnToneThresholdState_Object = MibTableColumn
sonusPadAdmnToneThresholdState = _SonusPadAdmnToneThresholdState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 1, 1, 5, 1, 11),
    _SonusPadAdmnToneThresholdState_Type()
)
sonusPadAdmnToneThresholdState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusPadAdmnToneThresholdState.setStatus("current")
_SonusPadAdmnRowStatus_Type = RowStatus
_SonusPadAdmnRowStatus_Object = MibTableColumn
sonusPadAdmnRowStatus = _SonusPadAdmnRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 1, 1, 5, 1, 12),
    _SonusPadAdmnRowStatus_Type()
)
sonusPadAdmnRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusPadAdmnRowStatus.setStatus("current")


class _SonusPadAdmnRtpDtmfRelay_Type(Integer32):
    """Custom type sonusPadAdmnRtpDtmfRelay based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_SonusPadAdmnRtpDtmfRelay_Type.__name__ = "Integer32"
_SonusPadAdmnRtpDtmfRelay_Object = MibTableColumn
sonusPadAdmnRtpDtmfRelay = _SonusPadAdmnRtpDtmfRelay_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 1, 1, 5, 1, 13),
    _SonusPadAdmnRtpDtmfRelay_Type()
)
sonusPadAdmnRtpDtmfRelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusPadAdmnRtpDtmfRelay.setStatus("current")


class _SonusPadAdmnRtpFaxRelay_Type(Integer32):
    """Custom type sonusPadAdmnRtpFaxRelay based on Integer32"""
    defaultValue = 101

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_SonusPadAdmnRtpFaxRelay_Type.__name__ = "Integer32"
_SonusPadAdmnRtpFaxRelay_Object = MibTableColumn
sonusPadAdmnRtpFaxRelay = _SonusPadAdmnRtpFaxRelay_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 1, 1, 5, 1, 14),
    _SonusPadAdmnRtpFaxRelay_Type()
)
sonusPadAdmnRtpFaxRelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusPadAdmnRtpFaxRelay.setStatus("current")


class _SonusPadAdmnSidMinTime_Type(Integer32):
    """Custom type sonusPadAdmnSidMinTime based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 300000),
    )


_SonusPadAdmnSidMinTime_Type.__name__ = "Integer32"
_SonusPadAdmnSidMinTime_Object = MibTableColumn
sonusPadAdmnSidMinTime = _SonusPadAdmnSidMinTime_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 1, 1, 5, 1, 15),
    _SonusPadAdmnSidMinTime_Type()
)
sonusPadAdmnSidMinTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusPadAdmnSidMinTime.setStatus("current")


class _SonusPadAdmnSidMaxTime_Type(Integer32):
    """Custom type sonusPadAdmnSidMaxTime based on Integer32"""
    defaultValue = 2000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 300000),
    )


_SonusPadAdmnSidMaxTime_Type.__name__ = "Integer32"
_SonusPadAdmnSidMaxTime_Object = MibTableColumn
sonusPadAdmnSidMaxTime = _SonusPadAdmnSidMaxTime_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 1, 1, 5, 1, 16),
    _SonusPadAdmnSidMaxTime_Type()
)
sonusPadAdmnSidMaxTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusPadAdmnSidMaxTime.setStatus("current")


class _SonusPadAdmnSidHangoverTime_Type(Integer32):
    """Custom type sonusPadAdmnSidHangoverTime based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(80, 2560),
    )


_SonusPadAdmnSidHangoverTime_Type.__name__ = "Integer32"
_SonusPadAdmnSidHangoverTime_Object = MibTableColumn
sonusPadAdmnSidHangoverTime = _SonusPadAdmnSidHangoverTime_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 1, 1, 5, 1, 17),
    _SonusPadAdmnSidHangoverTime_Type()
)
sonusPadAdmnSidHangoverTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusPadAdmnSidHangoverTime.setStatus("current")


class _SonusPadAdmnSidMinNoiseFloor_Type(Integer32):
    """Custom type sonusPadAdmnSidMinNoiseFloor based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(24, 62),
    )


_SonusPadAdmnSidMinNoiseFloor_Type.__name__ = "Integer32"
_SonusPadAdmnSidMinNoiseFloor_Object = MibTableColumn
sonusPadAdmnSidMinNoiseFloor = _SonusPadAdmnSidMinNoiseFloor_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 1, 1, 5, 1, 18),
    _SonusPadAdmnSidMinNoiseFloor_Type()
)
sonusPadAdmnSidMinNoiseFloor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusPadAdmnSidMinNoiseFloor.setStatus("current")


class _SonusPadAdmnSidMaxNoiseFloor_Type(Integer32):
    """Custom type sonusPadAdmnSidMaxNoiseFloor based on Integer32"""
    defaultValue = 48

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(24, 62),
    )


_SonusPadAdmnSidMaxNoiseFloor_Type.__name__ = "Integer32"
_SonusPadAdmnSidMaxNoiseFloor_Object = MibTableColumn
sonusPadAdmnSidMaxNoiseFloor = _SonusPadAdmnSidMaxNoiseFloor_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 1, 1, 5, 1, 19),
    _SonusPadAdmnSidMaxNoiseFloor_Type()
)
sonusPadAdmnSidMaxNoiseFloor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusPadAdmnSidMaxNoiseFloor.setStatus("current")


class _SonusPadAdmnComfortEnergy_Type(Integer32):
    """Custom type sonusPadAdmnComfortEnergy based on Integer32"""
    defaultValue = 56

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(35, 90),
    )


_SonusPadAdmnComfortEnergy_Type.__name__ = "Integer32"
_SonusPadAdmnComfortEnergy_Object = MibTableColumn
sonusPadAdmnComfortEnergy = _SonusPadAdmnComfortEnergy_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 1, 1, 5, 1, 20),
    _SonusPadAdmnComfortEnergy_Type()
)
sonusPadAdmnComfortEnergy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusPadAdmnComfortEnergy.setStatus("current")
_SonusEchoCancellorProfile_ObjectIdentity = ObjectIdentity
sonusEchoCancellorProfile = _SonusEchoCancellorProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 1, 1, 6)
)
_SonusEchoCancellorProfileNextIndex_Type = Integer32
_SonusEchoCancellorProfileNextIndex_Object = MibScalar
sonusEchoCancellorProfileNextIndex = _SonusEchoCancellorProfileNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 1, 1, 6, 1),
    _SonusEchoCancellorProfileNextIndex_Type()
)
sonusEchoCancellorProfileNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusEchoCancellorProfileNextIndex.setStatus("current")
_SonusEchoCancellorProfileTable_Object = MibTable
sonusEchoCancellorProfileTable = _SonusEchoCancellorProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 1, 1, 6, 2)
)
if mibBuilder.loadTexts:
    sonusEchoCancellorProfileTable.setStatus("current")
_SonusEchoCancellorProfileEntry_Object = MibTableRow
sonusEchoCancellorProfileEntry = _SonusEchoCancellorProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 1, 1, 6, 2, 1)
)
sonusEchoCancellorProfileEntry.setIndexNames(
    (0, "SONUS-DSP-RESOURCES-MIB", "sonusEchoCancellorProfileIndex"),
)
if mibBuilder.loadTexts:
    sonusEchoCancellorProfileEntry.setStatus("current")
_SonusEchoCancellorProfileIndex_Type = Integer32
_SonusEchoCancellorProfileIndex_Object = MibTableColumn
sonusEchoCancellorProfileIndex = _SonusEchoCancellorProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 1, 1, 6, 2, 1, 1),
    _SonusEchoCancellorProfileIndex_Type()
)
sonusEchoCancellorProfileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusEchoCancellorProfileIndex.setStatus("current")
_SonusEchoCancellorProfileName_Type = SonusName
_SonusEchoCancellorProfileName_Object = MibTableColumn
sonusEchoCancellorProfileName = _SonusEchoCancellorProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 1, 1, 6, 2, 1, 2),
    _SonusEchoCancellorProfileName_Type()
)
sonusEchoCancellorProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusEchoCancellorProfileName.setStatus("current")


class _SonusEchoCancellorProfileState_Type(SonusAdminState):
    """Custom type sonusEchoCancellorProfileState based on SonusAdminState"""


_SonusEchoCancellorProfileState_Object = MibTableColumn
sonusEchoCancellorProfileState = _SonusEchoCancellorProfileState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 1, 1, 6, 2, 1, 3),
    _SonusEchoCancellorProfileState_Type()
)
sonusEchoCancellorProfileState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusEchoCancellorProfileState.setStatus("current")


class _SonusEchoCancellorProfileMaxTail_Type(Integer32):
    """Custom type sonusEchoCancellorProfileMaxTail based on Integer32"""
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
        *(("millisec24", 1),
          ("millisec32", 2),
          ("millisec48", 3),
          ("millisec64", 4))
    )


_SonusEchoCancellorProfileMaxTail_Type.__name__ = "Integer32"
_SonusEchoCancellorProfileMaxTail_Object = MibTableColumn
sonusEchoCancellorProfileMaxTail = _SonusEchoCancellorProfileMaxTail_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 1, 1, 6, 2, 1, 4),
    _SonusEchoCancellorProfileMaxTail_Type()
)
sonusEchoCancellorProfileMaxTail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusEchoCancellorProfileMaxTail.setStatus("current")


class _SonusEchoCancellorProfileAudioType_Type(Integer32):
    """Custom type sonusEchoCancellorProfileAudioType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("aLaw", 2),
          ("uLaw", 1))
    )


_SonusEchoCancellorProfileAudioType_Type.__name__ = "Integer32"
_SonusEchoCancellorProfileAudioType_Object = MibTableColumn
sonusEchoCancellorProfileAudioType = _SonusEchoCancellorProfileAudioType_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 1, 1, 6, 2, 1, 5),
    _SonusEchoCancellorProfileAudioType_Type()
)
sonusEchoCancellorProfileAudioType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusEchoCancellorProfileAudioType.setStatus("current")


class _SonusEchoCancellorProfileSignallingTone_Type(Integer32):
    """Custom type sonusEchoCancellorProfileSignallingTone based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("c5", 2),
          ("none", 1))
    )


_SonusEchoCancellorProfileSignallingTone_Type.__name__ = "Integer32"
_SonusEchoCancellorProfileSignallingTone_Object = MibTableColumn
sonusEchoCancellorProfileSignallingTone = _SonusEchoCancellorProfileSignallingTone_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 1, 1, 6, 2, 1, 6),
    _SonusEchoCancellorProfileSignallingTone_Type()
)
sonusEchoCancellorProfileSignallingTone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusEchoCancellorProfileSignallingTone.setStatus("current")


class _SonusEchoCancellorProfileNlpDisable_Type(Integer32):
    """Custom type sonusEchoCancellorProfileNlpDisable based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_SonusEchoCancellorProfileNlpDisable_Type.__name__ = "Integer32"
_SonusEchoCancellorProfileNlpDisable_Object = MibTableColumn
sonusEchoCancellorProfileNlpDisable = _SonusEchoCancellorProfileNlpDisable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 1, 1, 6, 2, 1, 7),
    _SonusEchoCancellorProfileNlpDisable_Type()
)
sonusEchoCancellorProfileNlpDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusEchoCancellorProfileNlpDisable.setStatus("current")


class _SonusEchoCancellorProfileNlpEnable_Type(Integer32):
    """Custom type sonusEchoCancellorProfileNlpEnable based on Integer32"""
    defaultValue = 75

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 80),
    )


_SonusEchoCancellorProfileNlpEnable_Type.__name__ = "Integer32"
_SonusEchoCancellorProfileNlpEnable_Object = MibTableColumn
sonusEchoCancellorProfileNlpEnable = _SonusEchoCancellorProfileNlpEnable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 1, 1, 6, 2, 1, 8),
    _SonusEchoCancellorProfileNlpEnable_Type()
)
sonusEchoCancellorProfileNlpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusEchoCancellorProfileNlpEnable.setStatus("current")


class _SonusEchoCancellorProfileReturnLoss_Type(Integer32):
    """Custom type sonusEchoCancellorProfileReturnLoss based on Integer32"""
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
        *(("dB0", 3),
          ("dB3", 2),
          ("dB6", 1))
    )


_SonusEchoCancellorProfileReturnLoss_Type.__name__ = "Integer32"
_SonusEchoCancellorProfileReturnLoss_Object = MibTableColumn
sonusEchoCancellorProfileReturnLoss = _SonusEchoCancellorProfileReturnLoss_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 1, 1, 6, 2, 1, 9),
    _SonusEchoCancellorProfileReturnLoss_Type()
)
sonusEchoCancellorProfileReturnLoss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusEchoCancellorProfileReturnLoss.setStatus("current")


class _SonusEchoCancellorProfileResidualEcho_Type(Integer32):
    """Custom type sonusEchoCancellorProfileResidualEcho based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("cancelOnly", 1),
          ("comfortNoise", 4),
          ("suppressResidual", 2))
    )


_SonusEchoCancellorProfileResidualEcho_Type.__name__ = "Integer32"
_SonusEchoCancellorProfileResidualEcho_Object = MibTableColumn
sonusEchoCancellorProfileResidualEcho = _SonusEchoCancellorProfileResidualEcho_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 1, 1, 6, 2, 1, 10),
    _SonusEchoCancellorProfileResidualEcho_Type()
)
sonusEchoCancellorProfileResidualEcho.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusEchoCancellorProfileResidualEcho.setStatus("current")


class _SonusEchoCancellorProfileHiLevelComp_Type(Integer32):
    """Custom type sonusEchoCancellorProfileHiLevelComp based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dB6", 2),
          ("none", 1))
    )


_SonusEchoCancellorProfileHiLevelComp_Type.__name__ = "Integer32"
_SonusEchoCancellorProfileHiLevelComp_Object = MibTableColumn
sonusEchoCancellorProfileHiLevelComp = _SonusEchoCancellorProfileHiLevelComp_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 1, 1, 6, 2, 1, 11),
    _SonusEchoCancellorProfileHiLevelComp_Type()
)
sonusEchoCancellorProfileHiLevelComp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusEchoCancellorProfileHiLevelComp.setStatus("current")


class _SonusEchoCancellorProfileModemDisable_Type(Integer32):
    """Custom type sonusEchoCancellorProfileModemDisable based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("g164", 2),
          ("g165", 4),
          ("ignore2100Hz", 1))
    )


_SonusEchoCancellorProfileModemDisable_Type.__name__ = "Integer32"
_SonusEchoCancellorProfileModemDisable_Object = MibTableColumn
sonusEchoCancellorProfileModemDisable = _SonusEchoCancellorProfileModemDisable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 1, 1, 6, 2, 1, 12),
    _SonusEchoCancellorProfileModemDisable_Type()
)
sonusEchoCancellorProfileModemDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusEchoCancellorProfileModemDisable.setStatus("current")
_SonusEchoCancellorProfileRowStatus_Type = RowStatus
_SonusEchoCancellorProfileRowStatus_Object = MibTableColumn
sonusEchoCancellorProfileRowStatus = _SonusEchoCancellorProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 1, 1, 6, 2, 1, 13),
    _SonusEchoCancellorProfileRowStatus_Type()
)
sonusEchoCancellorProfileRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusEchoCancellorProfileRowStatus.setStatus("current")


class _SonusEchoCancellorProfileNarrowbandDetection_Type(Integer32):
    """Custom type sonusEchoCancellorProfileNarrowbandDetection based on Integer32"""
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


_SonusEchoCancellorProfileNarrowbandDetection_Type.__name__ = "Integer32"
_SonusEchoCancellorProfileNarrowbandDetection_Object = MibTableColumn
sonusEchoCancellorProfileNarrowbandDetection = _SonusEchoCancellorProfileNarrowbandDetection_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 1, 1, 6, 2, 1, 14),
    _SonusEchoCancellorProfileNarrowbandDetection_Type()
)
sonusEchoCancellorProfileNarrowbandDetection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusEchoCancellorProfileNarrowbandDetection.setStatus("current")
_SonusPadMIBNotifications_ObjectIdentity = ObjectIdentity
sonusPadMIBNotifications = _SonusPadMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 1, 2)
)
_SonusPadMIBNotificationsPrefix_ObjectIdentity = ObjectIdentity
sonusPadMIBNotificationsPrefix = _SonusPadMIBNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 1, 2, 0)
)
_SonusPadMIBNotificationsObjects_ObjectIdentity = ObjectIdentity
sonusPadMIBNotificationsObjects = _SonusPadMIBNotificationsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 1, 2, 1)
)


class _SonusPadThresholdType_Type(Integer32):
    """Custom type sonusPadThresholdType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("g729AB", 1),
          ("tone", 2))
    )


_SonusPadThresholdType_Type.__name__ = "Integer32"
_SonusPadThresholdType_Object = MibScalar
sonusPadThresholdType = _SonusPadThresholdType_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 1, 2, 1, 1),
    _SonusPadThresholdType_Type()
)
sonusPadThresholdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusPadThresholdType.setStatus("current")


class _SonusPadThresholdState_Type(Integer32):
    """Custom type sonusPadThresholdState based on Integer32"""
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


_SonusPadThresholdState_Type.__name__ = "Integer32"
_SonusPadThresholdState_Object = MibScalar
sonusPadThresholdState = _SonusPadThresholdState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 1, 2, 1, 2),
    _SonusPadThresholdState_Type()
)
sonusPadThresholdState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusPadThresholdState.setStatus("current")

# Managed Objects groups


# Notification objects

sonusPadThresholdNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 1, 2, 0, 1)
)
sonusPadThresholdNotification.setObjects(
      *(("SONUS-COMMON-MIB", "sonusShelfIndex"),
        ("SONUS-DSP-RESOURCES-MIB", "sonusPadThresholdType"),
        ("SONUS-DSP-RESOURCES-MIB", "sonusPadThresholdState"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusPadThresholdNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SONUS-DSP-RESOURCES-MIB",
    **{"sonusDspResourcesMIB": sonusDspResourcesMIB,
       "sonusDspResourcesMIBObjects": sonusDspResourcesMIBObjects,
       "sonusChannelStatTable": sonusChannelStatTable,
       "sonusDspAdmnTable": sonusDspAdmnTable,
       "sonusDspAdmnEntry": sonusDspAdmnEntry,
       "sonusDspAdmnShelfIndex": sonusDspAdmnShelfIndex,
       "sonusDspAdmnSlotIndex": sonusDspAdmnSlotIndex,
       "sonusDspAdmnDspIndex": sonusDspAdmnDspIndex,
       "sonusDspAdmnType": sonusDspAdmnType,
       "sonusDspAdmnNumChannels": sonusDspAdmnNumChannels,
       "sonusDspAdmnMaxTail": sonusDspAdmnMaxTail,
       "sonusDspAdmnEcAudioType": sonusDspAdmnEcAudioType,
       "sonusDspAdmnEcSignallingTone": sonusDspAdmnEcSignallingTone,
       "sonusDspAdmnNlpDisable": sonusDspAdmnNlpDisable,
       "sonusDspAdmnNlpEnable": sonusDspAdmnNlpEnable,
       "sonusDspAdmnJitterEvalPeriod": sonusDspAdmnJitterEvalPeriod,
       "sonusDspAdmnJitterMinOccThsh": sonusDspAdmnJitterMinOccThsh,
       "sonusDspResidualEchoControl": sonusDspResidualEchoControl,
       "sonusDspEchoReturnLoss": sonusDspEchoReturnLoss,
       "sonusDspModemDisable": sonusDspModemDisable,
       "sonusDspHighLevelComp": sonusDspHighLevelComp,
       "sonusDspStatTable": sonusDspStatTable,
       "sonusDspSlotStatTable": sonusDspSlotStatTable,
       "sonusDspSlotStatEntry": sonusDspSlotStatEntry,
       "sonusDspSlotStatShelfIndex": sonusDspSlotStatShelfIndex,
       "sonusDspSlotStatSlotIndex": sonusDspSlotStatSlotIndex,
       "sonusDspSlotStatG711EcTotal": sonusDspSlotStatG711EcTotal,
       "sonusDspSlotStatG711Total": sonusDspSlotStatG711Total,
       "sonusDspSlotStatHdlcTotal": sonusDspSlotStatHdlcTotal,
       "sonusDspSlotStatToneTotal": sonusDspSlotStatToneTotal,
       "sonusDspSlotStatG729AbTotal": sonusDspSlotStatG729AbTotal,
       "sonusDspSlotStatG711EcUtilization": sonusDspSlotStatG711EcUtilization,
       "sonusDspSlotStatG711EcAllocFailures": sonusDspSlotStatG711EcAllocFailures,
       "sonusDspSlotStatG711Utilization": sonusDspSlotStatG711Utilization,
       "sonusDspSlotStatG711AllocFailures": sonusDspSlotStatG711AllocFailures,
       "sonusDspSlotStatHdlcUtilization": sonusDspSlotStatHdlcUtilization,
       "sonusDspSlotStatHdlcAllocFailures": sonusDspSlotStatHdlcAllocFailures,
       "sonusDspSlotStatToneUtilization": sonusDspSlotStatToneUtilization,
       "sonusDspSlotStatToneAllocFailures": sonusDspSlotStatToneAllocFailures,
       "sonusDspSlotStatG729AbUtilization": sonusDspSlotStatG729AbUtilization,
       "sonusDspSlotStatG729AbAllocFailures": sonusDspSlotStatG729AbAllocFailures,
       "sonusPadAdmnTable": sonusPadAdmnTable,
       "sonusPadAdmnEntry": sonusPadAdmnEntry,
       "sonusPadAdmnShelfIndex": sonusPadAdmnShelfIndex,
       "sonusPadAdmnJitterEvalPeriod": sonusPadAdmnJitterEvalPeriod,
       "sonusPadAdmnJitterMinOccThsh": sonusPadAdmnJitterMinOccThsh,
       "sonusPadAdmnRtpG711ALaw": sonusPadAdmnRtpG711ALaw,
       "sonusPadAdmnRtpG711ULaw": sonusPadAdmnRtpG711ULaw,
       "sonusPadAdmnRtpG729A": sonusPadAdmnRtpG729A,
       "sonusPadAdmnRtpG729AB": sonusPadAdmnRtpG729AB,
       "sonusPadAdmnG729ABThreshold": sonusPadAdmnG729ABThreshold,
       "sonusPadAdmnG729ABThresholdState": sonusPadAdmnG729ABThresholdState,
       "sonusPadAdmnToneThreshold": sonusPadAdmnToneThreshold,
       "sonusPadAdmnToneThresholdState": sonusPadAdmnToneThresholdState,
       "sonusPadAdmnRowStatus": sonusPadAdmnRowStatus,
       "sonusPadAdmnRtpDtmfRelay": sonusPadAdmnRtpDtmfRelay,
       "sonusPadAdmnRtpFaxRelay": sonusPadAdmnRtpFaxRelay,
       "sonusPadAdmnSidMinTime": sonusPadAdmnSidMinTime,
       "sonusPadAdmnSidMaxTime": sonusPadAdmnSidMaxTime,
       "sonusPadAdmnSidHangoverTime": sonusPadAdmnSidHangoverTime,
       "sonusPadAdmnSidMinNoiseFloor": sonusPadAdmnSidMinNoiseFloor,
       "sonusPadAdmnSidMaxNoiseFloor": sonusPadAdmnSidMaxNoiseFloor,
       "sonusPadAdmnComfortEnergy": sonusPadAdmnComfortEnergy,
       "sonusEchoCancellorProfile": sonusEchoCancellorProfile,
       "sonusEchoCancellorProfileNextIndex": sonusEchoCancellorProfileNextIndex,
       "sonusEchoCancellorProfileTable": sonusEchoCancellorProfileTable,
       "sonusEchoCancellorProfileEntry": sonusEchoCancellorProfileEntry,
       "sonusEchoCancellorProfileIndex": sonusEchoCancellorProfileIndex,
       "sonusEchoCancellorProfileName": sonusEchoCancellorProfileName,
       "sonusEchoCancellorProfileState": sonusEchoCancellorProfileState,
       "sonusEchoCancellorProfileMaxTail": sonusEchoCancellorProfileMaxTail,
       "sonusEchoCancellorProfileAudioType": sonusEchoCancellorProfileAudioType,
       "sonusEchoCancellorProfileSignallingTone": sonusEchoCancellorProfileSignallingTone,
       "sonusEchoCancellorProfileNlpDisable": sonusEchoCancellorProfileNlpDisable,
       "sonusEchoCancellorProfileNlpEnable": sonusEchoCancellorProfileNlpEnable,
       "sonusEchoCancellorProfileReturnLoss": sonusEchoCancellorProfileReturnLoss,
       "sonusEchoCancellorProfileResidualEcho": sonusEchoCancellorProfileResidualEcho,
       "sonusEchoCancellorProfileHiLevelComp": sonusEchoCancellorProfileHiLevelComp,
       "sonusEchoCancellorProfileModemDisable": sonusEchoCancellorProfileModemDisable,
       "sonusEchoCancellorProfileRowStatus": sonusEchoCancellorProfileRowStatus,
       "sonusEchoCancellorProfileNarrowbandDetection": sonusEchoCancellorProfileNarrowbandDetection,
       "sonusPadMIBNotifications": sonusPadMIBNotifications,
       "sonusPadMIBNotificationsPrefix": sonusPadMIBNotificationsPrefix,
       "sonusPadThresholdNotification": sonusPadThresholdNotification,
       "sonusPadMIBNotificationsObjects": sonusPadMIBNotificationsObjects,
       "sonusPadThresholdType": sonusPadThresholdType,
       "sonusPadThresholdState": sonusPadThresholdState}
)
