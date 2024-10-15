# SNMP MIB module (TIARA-NETWORKS-DSX-TE3-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TIARA-NETWORKS-DSX-TE3-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:01:39 2024
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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")

(LEDState,
 dsxT3E3IfGroup) = mibBuilder.importSymbols(
    "TIARA-NETWORKS-DSX-TC-MIB",
    "LEDState",
    "dsxT3E3IfGroup")


# MODULE-IDENTITY

dsxT3E3MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1)
)
dsxT3E3MIB.setRevisions(
        ("1999-04-23 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DsxT3E3IfConfigGroup_ObjectIdentity = ObjectIdentity
dsxT3E3IfConfigGroup = _DsxT3E3IfConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 1)
)
_DsxT3E3IfConfigLineTable_Object = MibTable
dsxT3E3IfConfigLineTable = _DsxT3E3IfConfigLineTable_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 1, 1)
)
if mibBuilder.loadTexts:
    dsxT3E3IfConfigLineTable.setStatus("current")
_DsxT3E3IfConfigLineEntry_Object = MibTableRow
dsxT3E3IfConfigLineEntry = _DsxT3E3IfConfigLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 1, 1, 1)
)
dsxT3E3IfConfigLineEntry.setIndexNames(
    (0, "TIARA-NETWORKS-DSX-TE3-MIB", "dsxT3E3IfIndex"),
)
if mibBuilder.loadTexts:
    dsxT3E3IfConfigLineEntry.setStatus("current")
_DsxT3E3IfIndex_Type = Integer32
_DsxT3E3IfIndex_Object = MibTableColumn
dsxT3E3IfIndex = _DsxT3E3IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 1, 1, 1, 1),
    _DsxT3E3IfIndex_Type()
)
dsxT3E3IfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dsxT3E3IfIndex.setStatus("current")


class _DsxT3E3IfConfigLineType_Type(Integer32):
    """Custom type dsxT3E3IfConfigLineType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("linetype-cbitparity", 4),
          ("linetype-m13", 2))
    )


_DsxT3E3IfConfigLineType_Type.__name__ = "Integer32"
_DsxT3E3IfConfigLineType_Object = MibTableColumn
dsxT3E3IfConfigLineType = _DsxT3E3IfConfigLineType_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 1, 1, 1, 2),
    _DsxT3E3IfConfigLineType_Type()
)
dsxT3E3IfConfigLineType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsxT3E3IfConfigLineType.setStatus("current")


class _DsxT3E3IfConfigLineCode_Type(Integer32):
    """Custom type dsxT3E3IfConfigLineCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("linecode-b3zs", 2),
          ("linecode-hdb3", 3))
    )


_DsxT3E3IfConfigLineCode_Type.__name__ = "Integer32"
_DsxT3E3IfConfigLineCode_Object = MibTableColumn
dsxT3E3IfConfigLineCode = _DsxT3E3IfConfigLineCode_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 1, 1, 1, 3),
    _DsxT3E3IfConfigLineCode_Type()
)
dsxT3E3IfConfigLineCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT3E3IfConfigLineCode.setStatus("current")


class _DsxT3E3IfConfigCableLength_Type(Integer32):
    """Custom type dsxT3E3IfConfigCableLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cable-length-0-to-225", 1),
          ("cable-length-225-to-450", 2))
    )


_DsxT3E3IfConfigCableLength_Type.__name__ = "Integer32"
_DsxT3E3IfConfigCableLength_Object = MibTableColumn
dsxT3E3IfConfigCableLength = _DsxT3E3IfConfigCableLength_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 1, 1, 1, 4),
    _DsxT3E3IfConfigCableLength_Type()
)
dsxT3E3IfConfigCableLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsxT3E3IfConfigCableLength.setStatus("current")


class _DsxT3E3IfConfigTransmitClock_Type(Integer32):
    """Custom type dsxT3E3IfConfigTransmitClock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("timing-internal", 2),
          ("timing-line", 1))
    )


_DsxT3E3IfConfigTransmitClock_Type.__name__ = "Integer32"
_DsxT3E3IfConfigTransmitClock_Object = MibTableColumn
dsxT3E3IfConfigTransmitClock = _DsxT3E3IfConfigTransmitClock_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 1, 1, 1, 5),
    _DsxT3E3IfConfigTransmitClock_Type()
)
dsxT3E3IfConfigTransmitClock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsxT3E3IfConfigTransmitClock.setStatus("current")


class _DsxT3E3IfConfigDS3ScramblingMode_Type(Integer32):
    """Custom type dsxT3E3IfConfigDS3ScramblingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mode-0", 1),
          ("mode-1", 2),
          ("mode-2", 3))
    )


_DsxT3E3IfConfigDS3ScramblingMode_Type.__name__ = "Integer32"
_DsxT3E3IfConfigDS3ScramblingMode_Object = MibTableColumn
dsxT3E3IfConfigDS3ScramblingMode = _DsxT3E3IfConfigDS3ScramblingMode_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 1, 1, 1, 6),
    _DsxT3E3IfConfigDS3ScramblingMode_Type()
)
dsxT3E3IfConfigDS3ScramblingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsxT3E3IfConfigDS3ScramblingMode.setStatus("current")
_DsxT3E3IfConfigDS3ScramblingEnable_Type = TruthValue
_DsxT3E3IfConfigDS3ScramblingEnable_Object = MibTableColumn
dsxT3E3IfConfigDS3ScramblingEnable = _DsxT3E3IfConfigDS3ScramblingEnable_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 1, 1, 1, 7),
    _DsxT3E3IfConfigDS3ScramblingEnable_Type()
)
dsxT3E3IfConfigDS3ScramblingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsxT3E3IfConfigDS3ScramblingEnable.setStatus("current")
_DsxT3E3IfConfigMdlTable_Object = MibTable
dsxT3E3IfConfigMdlTable = _DsxT3E3IfConfigMdlTable_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 1, 2)
)
if mibBuilder.loadTexts:
    dsxT3E3IfConfigMdlTable.setStatus("current")
_DsxT3E3IfConfigMdlEntry_Object = MibTableRow
dsxT3E3IfConfigMdlEntry = _DsxT3E3IfConfigMdlEntry_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    dsxT3E3IfConfigMdlEntry.setStatus("current")


class _DsxT3E3IfConfigMdlEIC_Type(OctetString):
    """Custom type dsxT3E3IfConfigMdlEIC based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )


_DsxT3E3IfConfigMdlEIC_Type.__name__ = "OctetString"
_DsxT3E3IfConfigMdlEIC_Object = MibTableColumn
dsxT3E3IfConfigMdlEIC = _DsxT3E3IfConfigMdlEIC_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 1, 2, 1, 1),
    _DsxT3E3IfConfigMdlEIC_Type()
)
dsxT3E3IfConfigMdlEIC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsxT3E3IfConfigMdlEIC.setStatus("current")


class _DsxT3E3IfConfigMdlLIC_Type(OctetString):
    """Custom type dsxT3E3IfConfigMdlLIC based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(11, 11),
    )


_DsxT3E3IfConfigMdlLIC_Type.__name__ = "OctetString"
_DsxT3E3IfConfigMdlLIC_Object = MibTableColumn
dsxT3E3IfConfigMdlLIC = _DsxT3E3IfConfigMdlLIC_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 1, 2, 1, 2),
    _DsxT3E3IfConfigMdlLIC_Type()
)
dsxT3E3IfConfigMdlLIC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsxT3E3IfConfigMdlLIC.setStatus("current")


class _DsxT3E3IfConfigMdlFIC_Type(OctetString):
    """Custom type dsxT3E3IfConfigMdlFIC based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )


_DsxT3E3IfConfigMdlFIC_Type.__name__ = "OctetString"
_DsxT3E3IfConfigMdlFIC_Object = MibTableColumn
dsxT3E3IfConfigMdlFIC = _DsxT3E3IfConfigMdlFIC_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 1, 2, 1, 3),
    _DsxT3E3IfConfigMdlFIC_Type()
)
dsxT3E3IfConfigMdlFIC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsxT3E3IfConfigMdlFIC.setStatus("current")


class _DsxT3E3IfConfigMdlUIC_Type(OctetString):
    """Custom type dsxT3E3IfConfigMdlUIC based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_DsxT3E3IfConfigMdlUIC_Type.__name__ = "OctetString"
_DsxT3E3IfConfigMdlUIC_Object = MibTableColumn
dsxT3E3IfConfigMdlUIC = _DsxT3E3IfConfigMdlUIC_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 1, 2, 1, 4),
    _DsxT3E3IfConfigMdlUIC_Type()
)
dsxT3E3IfConfigMdlUIC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsxT3E3IfConfigMdlUIC.setStatus("current")


class _DsxT3E3IfConfigMdlPFI_Type(OctetString):
    """Custom type dsxT3E3IfConfigMdlPFI based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(38, 38),
    )


_DsxT3E3IfConfigMdlPFI_Type.__name__ = "OctetString"
_DsxT3E3IfConfigMdlPFI_Object = MibTableColumn
dsxT3E3IfConfigMdlPFI = _DsxT3E3IfConfigMdlPFI_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 1, 2, 1, 5),
    _DsxT3E3IfConfigMdlPFI_Type()
)
dsxT3E3IfConfigMdlPFI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsxT3E3IfConfigMdlPFI.setStatus("current")


class _DsxT3E3IfConfigMdlPort_Type(OctetString):
    """Custom type dsxT3E3IfConfigMdlPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(38, 38),
    )


_DsxT3E3IfConfigMdlPort_Type.__name__ = "OctetString"
_DsxT3E3IfConfigMdlPort_Object = MibTableColumn
dsxT3E3IfConfigMdlPort = _DsxT3E3IfConfigMdlPort_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 1, 2, 1, 6),
    _DsxT3E3IfConfigMdlPort_Type()
)
dsxT3E3IfConfigMdlPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsxT3E3IfConfigMdlPort.setStatus("current")


class _DsxT3E3IfConfigMdlGenerator_Type(OctetString):
    """Custom type dsxT3E3IfConfigMdlGenerator based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(38, 38),
    )


_DsxT3E3IfConfigMdlGenerator_Type.__name__ = "OctetString"
_DsxT3E3IfConfigMdlGenerator_Object = MibTableColumn
dsxT3E3IfConfigMdlGenerator = _DsxT3E3IfConfigMdlGenerator_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 1, 2, 1, 7),
    _DsxT3E3IfConfigMdlGenerator_Type()
)
dsxT3E3IfConfigMdlGenerator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsxT3E3IfConfigMdlGenerator.setStatus("current")
_DsxT3E3IfAlarmConfigGroup_ObjectIdentity = ObjectIdentity
dsxT3E3IfAlarmConfigGroup = _DsxT3E3IfAlarmConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 1, 3)
)
_DsxT3E3IfAlarmThresholdConfigTable_Object = MibTable
dsxT3E3IfAlarmThresholdConfigTable = _DsxT3E3IfAlarmThresholdConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    dsxT3E3IfAlarmThresholdConfigTable.setStatus("current")
_DsxT3E3IfAlarmThresholdConfigEntry_Object = MibTableRow
dsxT3E3IfAlarmThresholdConfigEntry = _DsxT3E3IfAlarmThresholdConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 1, 3, 1, 1)
)
dsxT3E3IfAlarmThresholdConfigEntry.setIndexNames(
    (0, "TIARA-NETWORKS-DSX-TE3-MIB", "dsxT3E3IfIndex"),
    (0, "TIARA-NETWORKS-DSX-TE3-MIB", "dsxT3E3IfAlarmThresholdConfigIndex"),
)
if mibBuilder.loadTexts:
    dsxT3E3IfAlarmThresholdConfigEntry.setStatus("current")
_DsxT3E3IfAlarmThresholdConfigIndex_Type = Integer32
_DsxT3E3IfAlarmThresholdConfigIndex_Object = MibTableColumn
dsxT3E3IfAlarmThresholdConfigIndex = _DsxT3E3IfAlarmThresholdConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 1, 3, 1, 1, 1),
    _DsxT3E3IfAlarmThresholdConfigIndex_Type()
)
dsxT3E3IfAlarmThresholdConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dsxT3E3IfAlarmThresholdConfigIndex.setStatus("current")


class _DsxT3E3IfAlarmThresholdConfigObject_Type(Integer32):
    """Custom type dsxT3E3IfAlarmThresholdConfigObject based on Integer32"""
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
        *(("te3-object-cofa", 7),
          ("te3-object-cpbe", 4),
          ("te3-object-exz", 6),
          ("te3-object-fbe", 2),
          ("te3-object-febe", 5),
          ("te3-object-lcv", 1),
          ("te3-object-pbe", 3))
    )


_DsxT3E3IfAlarmThresholdConfigObject_Type.__name__ = "Integer32"
_DsxT3E3IfAlarmThresholdConfigObject_Object = MibTableColumn
dsxT3E3IfAlarmThresholdConfigObject = _DsxT3E3IfAlarmThresholdConfigObject_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 1, 3, 1, 1, 2),
    _DsxT3E3IfAlarmThresholdConfigObject_Type()
)
dsxT3E3IfAlarmThresholdConfigObject.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsxT3E3IfAlarmThresholdConfigObject.setStatus("current")


class _DsxT3E3IfAlarmThresholdConfigSamplingInterval_Type(Integer32):
    """Custom type dsxT3E3IfAlarmThresholdConfigSamplingInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_DsxT3E3IfAlarmThresholdConfigSamplingInterval_Type.__name__ = "Integer32"
_DsxT3E3IfAlarmThresholdConfigSamplingInterval_Object = MibTableColumn
dsxT3E3IfAlarmThresholdConfigSamplingInterval = _DsxT3E3IfAlarmThresholdConfigSamplingInterval_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 1, 3, 1, 1, 3),
    _DsxT3E3IfAlarmThresholdConfigSamplingInterval_Type()
)
dsxT3E3IfAlarmThresholdConfigSamplingInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsxT3E3IfAlarmThresholdConfigSamplingInterval.setStatus("current")


class _DsxT3E3IfAlarmThresholdConfigSampleType_Type(Integer32):
    """Custom type dsxT3E3IfAlarmThresholdConfigSampleType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sample-absolute", 1),
          ("sample-delta", 2))
    )


_DsxT3E3IfAlarmThresholdConfigSampleType_Type.__name__ = "Integer32"
_DsxT3E3IfAlarmThresholdConfigSampleType_Object = MibTableColumn
dsxT3E3IfAlarmThresholdConfigSampleType = _DsxT3E3IfAlarmThresholdConfigSampleType_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 1, 3, 1, 1, 4),
    _DsxT3E3IfAlarmThresholdConfigSampleType_Type()
)
dsxT3E3IfAlarmThresholdConfigSampleType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsxT3E3IfAlarmThresholdConfigSampleType.setStatus("current")
_DsxT3E3IfAlarmThresholdConfigStartupType_Type = TruthValue
_DsxT3E3IfAlarmThresholdConfigStartupType_Object = MibTableColumn
dsxT3E3IfAlarmThresholdConfigStartupType = _DsxT3E3IfAlarmThresholdConfigStartupType_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 1, 3, 1, 1, 5),
    _DsxT3E3IfAlarmThresholdConfigStartupType_Type()
)
dsxT3E3IfAlarmThresholdConfigStartupType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsxT3E3IfAlarmThresholdConfigStartupType.setStatus("current")
_DsxT3E3IfAlarmThresholdConfigRisingThreshold_Type = Integer32
_DsxT3E3IfAlarmThresholdConfigRisingThreshold_Object = MibTableColumn
dsxT3E3IfAlarmThresholdConfigRisingThreshold = _DsxT3E3IfAlarmThresholdConfigRisingThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 1, 3, 1, 1, 6),
    _DsxT3E3IfAlarmThresholdConfigRisingThreshold_Type()
)
dsxT3E3IfAlarmThresholdConfigRisingThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsxT3E3IfAlarmThresholdConfigRisingThreshold.setStatus("current")
_DsxT3E3IfAlarmThresholdConfigFallingThreshold_Type = Integer32
_DsxT3E3IfAlarmThresholdConfigFallingThreshold_Object = MibTableColumn
dsxT3E3IfAlarmThresholdConfigFallingThreshold = _DsxT3E3IfAlarmThresholdConfigFallingThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 1, 3, 1, 1, 7),
    _DsxT3E3IfAlarmThresholdConfigFallingThreshold_Type()
)
dsxT3E3IfAlarmThresholdConfigFallingThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsxT3E3IfAlarmThresholdConfigFallingThreshold.setStatus("current")
_DsxT3E3IfTestConfigTable_Object = MibTable
dsxT3E3IfTestConfigTable = _DsxT3E3IfTestConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 1, 4)
)
if mibBuilder.loadTexts:
    dsxT3E3IfTestConfigTable.setStatus("current")
_DsxT3E3IfTestConfigEntry_Object = MibTableRow
dsxT3E3IfTestConfigEntry = _DsxT3E3IfTestConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    dsxT3E3IfTestConfigEntry.setStatus("current")


class _DsxT3E3IfTestConfigType_Type(Integer32):
    """Custom type dsxT3E3IfTestConfigType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("line-loopback-test", 3),
          ("no-test", 1),
          ("remote-lpdn-test", 9),
          ("remote-lpup-test", 8))
    )


_DsxT3E3IfTestConfigType_Type.__name__ = "Integer32"
_DsxT3E3IfTestConfigType_Object = MibTableColumn
dsxT3E3IfTestConfigType = _DsxT3E3IfTestConfigType_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 1, 4, 1, 1),
    _DsxT3E3IfTestConfigType_Type()
)
dsxT3E3IfTestConfigType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsxT3E3IfTestConfigType.setStatus("current")


class _DsxT3E3IfTestConfigLoopCode_Type(Integer32):
    """Custom type dsxT3E3IfTestConfigLoopCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("loopcode-feac", 2),
          ("loopcode-none", 1))
    )


_DsxT3E3IfTestConfigLoopCode_Type.__name__ = "Integer32"
_DsxT3E3IfTestConfigLoopCode_Object = MibTableColumn
dsxT3E3IfTestConfigLoopCode = _DsxT3E3IfTestConfigLoopCode_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 1, 4, 1, 2),
    _DsxT3E3IfTestConfigLoopCode_Type()
)
dsxT3E3IfTestConfigLoopCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsxT3E3IfTestConfigLoopCode.setStatus("current")
_DsxT3E3IfStatusGroup_ObjectIdentity = ObjectIdentity
dsxT3E3IfStatusGroup = _DsxT3E3IfStatusGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 2)
)
_DsxT3E3IfStatusTable_Object = MibTable
dsxT3E3IfStatusTable = _DsxT3E3IfStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 2, 1)
)
if mibBuilder.loadTexts:
    dsxT3E3IfStatusTable.setStatus("current")
_DsxT3E3IfStatusEntry_Object = MibTableRow
dsxT3E3IfStatusEntry = _DsxT3E3IfStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    dsxT3E3IfStatusEntry.setStatus("current")


class _DsxT3E3IfStatusLineStatus_Type(Bits):
    """Custom type dsxT3E3IfStatusLineStatus based on Bits"""
    namedValues = NamedValues(
        *(("febeStatus", 14),
          ("loopbackStatus", 24),
          ("lorcStatus", 16),
          ("no-alarm", 31),
          ("pdeStatus", 15),
          ("raisStatus", 28),
          ("rcvTestCode", 23),
          ("reserved", 0),
          ("reserved1", 1),
          ("reserved10", 18),
          ("reserved11", 22),
          ("reserved2", 2),
          ("reserved3", 3),
          ("reserved4", 4),
          ("reserved5", 5),
          ("reserved6", 6),
          ("reserved7", 7),
          ("reserved8", 13),
          ("reserved9", 17),
          ("rexzStatus", 21),
          ("rfebeStatus", 19),
          ("risStatus", 20),
          ("rlofStatus", 26),
          ("rlosStatus", 25),
          ("rraiStatus", 30),
          ("sendLineCode", 12),
          ("sendPattern", 8),
          ("sendPayloadCode", 11),
          ("sendResetCode", 10),
          ("sendTE3Code", 9),
          ("taisStatus", 27),
          ("traiStatus", 29))
    )

_DsxT3E3IfStatusLineStatus_Type.__name__ = "Bits"
_DsxT3E3IfStatusLineStatus_Object = MibTableColumn
dsxT3E3IfStatusLineStatus = _DsxT3E3IfStatusLineStatus_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 2, 1, 1, 1),
    _DsxT3E3IfStatusLineStatus_Type()
)
dsxT3E3IfStatusLineStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT3E3IfStatusLineStatus.setStatus("current")


class _DsxT3E3IfStatusTransmitClock_Type(Integer32):
    """Custom type dsxT3E3IfStatusTransmitClock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("timing-internal", 2),
          ("timing-line", 1))
    )


_DsxT3E3IfStatusTransmitClock_Type.__name__ = "Integer32"
_DsxT3E3IfStatusTransmitClock_Object = MibTableColumn
dsxT3E3IfStatusTransmitClock = _DsxT3E3IfStatusTransmitClock_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 2, 1, 1, 2),
    _DsxT3E3IfStatusTransmitClock_Type()
)
dsxT3E3IfStatusTransmitClock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT3E3IfStatusTransmitClock.setStatus("current")
_DsxT3E3IfStatusTestLED_Type = LEDState
_DsxT3E3IfStatusTestLED_Object = MibTableColumn
dsxT3E3IfStatusTestLED = _DsxT3E3IfStatusTestLED_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 2, 1, 1, 3),
    _DsxT3E3IfStatusTestLED_Type()
)
dsxT3E3IfStatusTestLED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT3E3IfStatusTestLED.setStatus("current")
_DsxT3E3IfStatusErrorLED_Type = LEDState
_DsxT3E3IfStatusErrorLED_Object = MibTableColumn
dsxT3E3IfStatusErrorLED = _DsxT3E3IfStatusErrorLED_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 2, 1, 1, 4),
    _DsxT3E3IfStatusErrorLED_Type()
)
dsxT3E3IfStatusErrorLED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT3E3IfStatusErrorLED.setStatus("current")
_DsxT3E3IfStatusAisLED_Type = LEDState
_DsxT3E3IfStatusAisLED_Object = MibTableColumn
dsxT3E3IfStatusAisLED = _DsxT3E3IfStatusAisLED_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 2, 1, 1, 5),
    _DsxT3E3IfStatusAisLED_Type()
)
dsxT3E3IfStatusAisLED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT3E3IfStatusAisLED.setStatus("current")
_DsxT3E3IfStatusSignalLED_Type = LEDState
_DsxT3E3IfStatusSignalLED_Object = MibTableColumn
dsxT3E3IfStatusSignalLED = _DsxT3E3IfStatusSignalLED_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 2, 1, 1, 6),
    _DsxT3E3IfStatusSignalLED_Type()
)
dsxT3E3IfStatusSignalLED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT3E3IfStatusSignalLED.setStatus("current")
_DsxT3E3IfStatusFrameLED_Type = LEDState
_DsxT3E3IfStatusFrameLED_Object = MibTableColumn
dsxT3E3IfStatusFrameLED = _DsxT3E3IfStatusFrameLED_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 2, 1, 1, 7),
    _DsxT3E3IfStatusFrameLED_Type()
)
dsxT3E3IfStatusFrameLED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT3E3IfStatusFrameLED.setStatus("current")
_DsxT3E3IfStatusYellowLED_Type = LEDState
_DsxT3E3IfStatusYellowLED_Object = MibTableColumn
dsxT3E3IfStatusYellowLED = _DsxT3E3IfStatusYellowLED_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 2, 1, 1, 8),
    _DsxT3E3IfStatusYellowLED_Type()
)
dsxT3E3IfStatusYellowLED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT3E3IfStatusYellowLED.setStatus("current")
_DsxT3E3IfAlarmStatusTable_Object = MibTable
dsxT3E3IfAlarmStatusTable = _DsxT3E3IfAlarmStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 2, 2)
)
if mibBuilder.loadTexts:
    dsxT3E3IfAlarmStatusTable.setStatus("current")
_DsxT3E3IfAlarmStatusEntry_Object = MibTableRow
dsxT3E3IfAlarmStatusEntry = _DsxT3E3IfAlarmStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    dsxT3E3IfAlarmStatusEntry.setStatus("current")


class _DsxT3E3IfAlarmStatusAlarmStatus_Type(Bits):
    """Custom type dsxT3E3IfAlarmStatusAlarmStatus based on Bits"""
    namedValues = NamedValues(
        *(("loopbackStateAlarm", 6),
          ("lorcAlarm", 14),
          ("noAlarm", 0),
          ("rbluAlarm", 8),
          ("rcpeAlarm", 13),
          ("rcvTestCode", 7),
          ("rexzAlarm", 10),
          ("rfbeAlarm", 11),
          ("risAlarm", 9),
          ("rlofAlarm", 4),
          ("rlosAlarm", 5),
          ("rpeAlarm", 12),
          ("rraiAlarm", 1),
          ("taisAlarm", 3),
          ("tfebeAlarm", 16),
          ("tpdeAlarm", 15),
          ("traiAlarm", 2))
    )

_DsxT3E3IfAlarmStatusAlarmStatus_Type.__name__ = "Bits"
_DsxT3E3IfAlarmStatusAlarmStatus_Object = MibTableColumn
dsxT3E3IfAlarmStatusAlarmStatus = _DsxT3E3IfAlarmStatusAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 2, 2, 1, 1),
    _DsxT3E3IfAlarmStatusAlarmStatus_Type()
)
dsxT3E3IfAlarmStatusAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT3E3IfAlarmStatusAlarmStatus.setStatus("current")


class _DsxT3E3IfAlarmStatusThresholdStatus_Type(Bits):
    """Custom type dsxT3E3IfAlarmStatusThresholdStatus based on Bits"""
    namedValues = NamedValues(
        *(("threshold1", 0),
          ("threshold10", 9),
          ("threshold2", 1),
          ("threshold3", 2),
          ("threshold4", 3),
          ("threshold5", 4),
          ("threshold6", 5),
          ("threshold7", 6),
          ("threshold8", 7),
          ("threshold9", 8))
    )

_DsxT3E3IfAlarmStatusThresholdStatus_Type.__name__ = "Bits"
_DsxT3E3IfAlarmStatusThresholdStatus_Object = MibTableColumn
dsxT3E3IfAlarmStatusThresholdStatus = _DsxT3E3IfAlarmStatusThresholdStatus_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 2, 2, 1, 2),
    _DsxT3E3IfAlarmStatusThresholdStatus_Type()
)
dsxT3E3IfAlarmStatusThresholdStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT3E3IfAlarmStatusThresholdStatus.setStatus("current")
_DsxT3E3IfTestStatusTable_Object = MibTable
dsxT3E3IfTestStatusTable = _DsxT3E3IfTestStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 2, 3)
)
if mibBuilder.loadTexts:
    dsxT3E3IfTestStatusTable.setStatus("current")
_DsxT3E3IfTestStatusEntry_Object = MibTableRow
dsxT3E3IfTestStatusEntry = _DsxT3E3IfTestStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 2, 3, 1)
)
if mibBuilder.loadTexts:
    dsxT3E3IfTestStatusEntry.setStatus("current")


class _DsxT3E3IfTestStatusTestType_Type(Integer32):
    """Custom type dsxT3E3IfTestStatusTestType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("line-loopback", 3),
          ("no-test", 1),
          ("other-loopback", 4),
          ("remote-lpdn", 7),
          ("remote-lpup", 6))
    )


_DsxT3E3IfTestStatusTestType_Type.__name__ = "Integer32"
_DsxT3E3IfTestStatusTestType_Object = MibTableColumn
dsxT3E3IfTestStatusTestType = _DsxT3E3IfTestStatusTestType_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 2, 3, 1, 1),
    _DsxT3E3IfTestStatusTestType_Type()
)
dsxT3E3IfTestStatusTestType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT3E3IfTestStatusTestType.setStatus("current")


class _DsxT3E3IfTestStatusTestState_Type(Integer32):
    """Custom type dsxT3E3IfTestStatusTestState based on Integer32"""
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
        *(("state-failed", 7),
          ("state-idle", 1),
          ("state-in-progress", 5),
          ("state-locked", 3),
          ("state-passed", 6),
          ("state-relocked", 4),
          ("state-searching", 2))
    )


_DsxT3E3IfTestStatusTestState_Type.__name__ = "Integer32"
_DsxT3E3IfTestStatusTestState_Object = MibTableColumn
dsxT3E3IfTestStatusTestState = _DsxT3E3IfTestStatusTestState_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 2, 3, 1, 2),
    _DsxT3E3IfTestStatusTestState_Type()
)
dsxT3E3IfTestStatusTestState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT3E3IfTestStatusTestState.setStatus("current")


class _DsxT3E3IfTestStatusLoopCode_Type(Integer32):
    """Custom type dsxT3E3IfTestStatusLoopCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("loopcode-feac", 1)
    )


_DsxT3E3IfTestStatusLoopCode_Type.__name__ = "Integer32"
_DsxT3E3IfTestStatusLoopCode_Object = MibTableColumn
dsxT3E3IfTestStatusLoopCode = _DsxT3E3IfTestStatusLoopCode_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 2, 3, 1, 3),
    _DsxT3E3IfTestStatusLoopCode_Type()
)
dsxT3E3IfTestStatusLoopCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT3E3IfTestStatusLoopCode.setStatus("current")
_DsxT3E3IfLastTestResultTable_Object = MibTable
dsxT3E3IfLastTestResultTable = _DsxT3E3IfLastTestResultTable_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 2, 4)
)
if mibBuilder.loadTexts:
    dsxT3E3IfLastTestResultTable.setStatus("current")
_DsxT3E3IfLastTestResultEntry_Object = MibTableRow
dsxT3E3IfLastTestResultEntry = _DsxT3E3IfLastTestResultEntry_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 2, 4, 1)
)
if mibBuilder.loadTexts:
    dsxT3E3IfLastTestResultEntry.setStatus("current")


class _DsxT3E3IfLastTestResultTestType_Type(Integer32):
    """Custom type dsxT3E3IfLastTestResultTestType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("line-loopback", 3),
          ("no-test", 1),
          ("other-loopback", 4),
          ("remote-lpdn", 7),
          ("remote-lpup", 6))
    )


_DsxT3E3IfLastTestResultTestType_Type.__name__ = "Integer32"
_DsxT3E3IfLastTestResultTestType_Object = MibTableColumn
dsxT3E3IfLastTestResultTestType = _DsxT3E3IfLastTestResultTestType_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 2, 4, 1, 1),
    _DsxT3E3IfLastTestResultTestType_Type()
)
dsxT3E3IfLastTestResultTestType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT3E3IfLastTestResultTestType.setStatus("current")


class _DsxT3E3IfLastTestResultTestState_Type(Integer32):
    """Custom type dsxT3E3IfLastTestResultTestState based on Integer32"""
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
        *(("state-failed", 7),
          ("state-idle", 1),
          ("state-in-progress", 5),
          ("state-locked", 3),
          ("state-passed", 6),
          ("state-relocked", 4),
          ("state-searching", 2))
    )


_DsxT3E3IfLastTestResultTestState_Type.__name__ = "Integer32"
_DsxT3E3IfLastTestResultTestState_Object = MibTableColumn
dsxT3E3IfLastTestResultTestState = _DsxT3E3IfLastTestResultTestState_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 2, 4, 1, 2),
    _DsxT3E3IfLastTestResultTestState_Type()
)
dsxT3E3IfLastTestResultTestState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT3E3IfLastTestResultTestState.setStatus("current")


class _DsxT3E3IfLastTestResultLoopCode_Type(Integer32):
    """Custom type dsxT3E3IfLastTestResultLoopCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("loopcode-feac", 2),
          ("loopcode-none", 1))
    )


_DsxT3E3IfLastTestResultLoopCode_Type.__name__ = "Integer32"
_DsxT3E3IfLastTestResultLoopCode_Object = MibTableColumn
dsxT3E3IfLastTestResultLoopCode = _DsxT3E3IfLastTestResultLoopCode_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 2, 4, 1, 3),
    _DsxT3E3IfLastTestResultLoopCode_Type()
)
dsxT3E3IfLastTestResultLoopCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT3E3IfLastTestResultLoopCode.setStatus("current")
_DsxT3E3IfStatsGroup_ObjectIdentity = ObjectIdentity
dsxT3E3IfStatsGroup = _DsxT3E3IfStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 3)
)
_DsxT3E3IfArchiveStatsValidIntervalsTable_Object = MibTable
dsxT3E3IfArchiveStatsValidIntervalsTable = _DsxT3E3IfArchiveStatsValidIntervalsTable_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 3, 1)
)
if mibBuilder.loadTexts:
    dsxT3E3IfArchiveStatsValidIntervalsTable.setStatus("current")
_DsxT3E3IfArchiveStatsValidIntervalsEntry_Object = MibTableRow
dsxT3E3IfArchiveStatsValidIntervalsEntry = _DsxT3E3IfArchiveStatsValidIntervalsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    dsxT3E3IfArchiveStatsValidIntervalsEntry.setStatus("current")
_DsxT3E3IfAnsiArchiveStatsValidIntervals_Type = Unsigned32
_DsxT3E3IfAnsiArchiveStatsValidIntervals_Object = MibTableColumn
dsxT3E3IfAnsiArchiveStatsValidIntervals = _DsxT3E3IfAnsiArchiveStatsValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 3, 1, 1, 1),
    _DsxT3E3IfAnsiArchiveStatsValidIntervals_Type()
)
dsxT3E3IfAnsiArchiveStatsValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT3E3IfAnsiArchiveStatsValidIntervals.setStatus("current")
_DsxT3E3IfIetfArchiveStatsValidIntervals_Type = Unsigned32
_DsxT3E3IfIetfArchiveStatsValidIntervals_Object = MibTableColumn
dsxT3E3IfIetfArchiveStatsValidIntervals = _DsxT3E3IfIetfArchiveStatsValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 3, 1, 1, 2),
    _DsxT3E3IfIetfArchiveStatsValidIntervals_Type()
)
dsxT3E3IfIetfArchiveStatsValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT3E3IfIetfArchiveStatsValidIntervals.setStatus("current")
_DsxT3E3IfUserTotalStatsValidDays_Type = Unsigned32
_DsxT3E3IfUserTotalStatsValidDays_Object = MibTableColumn
dsxT3E3IfUserTotalStatsValidDays = _DsxT3E3IfUserTotalStatsValidDays_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 3, 1, 1, 3),
    _DsxT3E3IfUserTotalStatsValidDays_Type()
)
dsxT3E3IfUserTotalStatsValidDays.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT3E3IfUserTotalStatsValidDays.setStatus("current")
_DsxT3E3IfUserArchiveStatsValidIntervals_Type = Integer32
_DsxT3E3IfUserArchiveStatsValidIntervals_Object = MibTableColumn
dsxT3E3IfUserArchiveStatsValidIntervals = _DsxT3E3IfUserArchiveStatsValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 3, 1, 1, 4),
    _DsxT3E3IfUserArchiveStatsValidIntervals_Type()
)
dsxT3E3IfUserArchiveStatsValidIntervals.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsxT3E3IfUserArchiveStatsValidIntervals.setStatus("current")
_DsxT3E3IfErrorEventStatsTable_Object = MibTable
dsxT3E3IfErrorEventStatsTable = _DsxT3E3IfErrorEventStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 3, 2)
)
if mibBuilder.loadTexts:
    dsxT3E3IfErrorEventStatsTable.setStatus("current")
_DsxT3E3IfErrorEventStatsEntry_Object = MibTableRow
dsxT3E3IfErrorEventStatsEntry = _DsxT3E3IfErrorEventStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 3, 2, 1)
)
if mibBuilder.loadTexts:
    dsxT3E3IfErrorEventStatsEntry.setStatus("current")
_DsxT3E3IfErrorEventStatsEXZ_Type = Unsigned32
_DsxT3E3IfErrorEventStatsEXZ_Object = MibTableColumn
dsxT3E3IfErrorEventStatsEXZ = _DsxT3E3IfErrorEventStatsEXZ_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 3, 2, 1, 1),
    _DsxT3E3IfErrorEventStatsEXZ_Type()
)
dsxT3E3IfErrorEventStatsEXZ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT3E3IfErrorEventStatsEXZ.setStatus("current")
_DsxT3E3IfErrorEventStatsPBE_Type = Unsigned32
_DsxT3E3IfErrorEventStatsPBE_Object = MibTableColumn
dsxT3E3IfErrorEventStatsPBE = _DsxT3E3IfErrorEventStatsPBE_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 3, 2, 1, 2),
    _DsxT3E3IfErrorEventStatsPBE_Type()
)
dsxT3E3IfErrorEventStatsPBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT3E3IfErrorEventStatsPBE.setStatus("current")
_DsxT3E3IfErrorEventStatsFEBE_Type = Unsigned32
_DsxT3E3IfErrorEventStatsFEBE_Object = MibTableColumn
dsxT3E3IfErrorEventStatsFEBE = _DsxT3E3IfErrorEventStatsFEBE_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 3, 2, 1, 3),
    _DsxT3E3IfErrorEventStatsFEBE_Type()
)
dsxT3E3IfErrorEventStatsFEBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT3E3IfErrorEventStatsFEBE.setStatus("current")
_DsxT3E3IfAnsiStatsGroup_ObjectIdentity = ObjectIdentity
dsxT3E3IfAnsiStatsGroup = _DsxT3E3IfAnsiStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 3, 3)
)
_DsxT3E3IfAnsiCurrentStatsTable_Object = MibTable
dsxT3E3IfAnsiCurrentStatsTable = _DsxT3E3IfAnsiCurrentStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 3, 3, 1)
)
if mibBuilder.loadTexts:
    dsxT3E3IfAnsiCurrentStatsTable.setStatus("current")
_DsxT3E3IfAnsiCurrentStatsEntry_Object = MibTableRow
dsxT3E3IfAnsiCurrentStatsEntry = _DsxT3E3IfAnsiCurrentStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 3, 3, 1, 1)
)
if mibBuilder.loadTexts:
    dsxT3E3IfAnsiCurrentStatsEntry.setStatus("current")
_DsxT3E3IfAnsiCurrentStatsUASState_Type = TruthValue
_DsxT3E3IfAnsiCurrentStatsUASState_Object = MibTableColumn
dsxT3E3IfAnsiCurrentStatsUASState = _DsxT3E3IfAnsiCurrentStatsUASState_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 3, 3, 1, 1, 1),
    _DsxT3E3IfAnsiCurrentStatsUASState_Type()
)
dsxT3E3IfAnsiCurrentStatsUASState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT3E3IfAnsiCurrentStatsUASState.setStatus("current")
_DsxT3E3IfAnsiCurrentStatsTimeInCurrent_Type = Unsigned32
_DsxT3E3IfAnsiCurrentStatsTimeInCurrent_Object = MibTableColumn
dsxT3E3IfAnsiCurrentStatsTimeInCurrent = _DsxT3E3IfAnsiCurrentStatsTimeInCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 3, 3, 1, 1, 2),
    _DsxT3E3IfAnsiCurrentStatsTimeInCurrent_Type()
)
dsxT3E3IfAnsiCurrentStatsTimeInCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT3E3IfAnsiCurrentStatsTimeInCurrent.setStatus("current")
_DsxT3E3IfAnsiCurrentPathStatsCV_Type = Unsigned32
_DsxT3E3IfAnsiCurrentPathStatsCV_Object = MibTableColumn
dsxT3E3IfAnsiCurrentPathStatsCV = _DsxT3E3IfAnsiCurrentPathStatsCV_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 3, 3, 1, 1, 3),
    _DsxT3E3IfAnsiCurrentPathStatsCV_Type()
)
dsxT3E3IfAnsiCurrentPathStatsCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT3E3IfAnsiCurrentPathStatsCV.setStatus("current")
_DsxT3E3IfAnsiCurrentPathStatsES_Type = Unsigned32
_DsxT3E3IfAnsiCurrentPathStatsES_Object = MibTableColumn
dsxT3E3IfAnsiCurrentPathStatsES = _DsxT3E3IfAnsiCurrentPathStatsES_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 3, 3, 1, 1, 4),
    _DsxT3E3IfAnsiCurrentPathStatsES_Type()
)
dsxT3E3IfAnsiCurrentPathStatsES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT3E3IfAnsiCurrentPathStatsES.setStatus("current")
_DsxT3E3IfAnsiCurrentPathStatsSES_Type = Unsigned32
_DsxT3E3IfAnsiCurrentPathStatsSES_Object = MibTableColumn
dsxT3E3IfAnsiCurrentPathStatsSES = _DsxT3E3IfAnsiCurrentPathStatsSES_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 3, 3, 1, 1, 5),
    _DsxT3E3IfAnsiCurrentPathStatsSES_Type()
)
dsxT3E3IfAnsiCurrentPathStatsSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT3E3IfAnsiCurrentPathStatsSES.setStatus("current")
_DsxT3E3IfAnsiCurrentPathStatsSAS_Type = Unsigned32
_DsxT3E3IfAnsiCurrentPathStatsSAS_Object = MibTableColumn
dsxT3E3IfAnsiCurrentPathStatsSAS = _DsxT3E3IfAnsiCurrentPathStatsSAS_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 3, 3, 1, 1, 6),
    _DsxT3E3IfAnsiCurrentPathStatsSAS_Type()
)
dsxT3E3IfAnsiCurrentPathStatsSAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT3E3IfAnsiCurrentPathStatsSAS.setStatus("current")
_DsxT3E3IfAnsiCurrentPathStatsUAS_Type = Unsigned32
_DsxT3E3IfAnsiCurrentPathStatsUAS_Object = MibTableColumn
dsxT3E3IfAnsiCurrentPathStatsUAS = _DsxT3E3IfAnsiCurrentPathStatsUAS_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 3, 3, 1, 1, 7),
    _DsxT3E3IfAnsiCurrentPathStatsUAS_Type()
)
dsxT3E3IfAnsiCurrentPathStatsUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT3E3IfAnsiCurrentPathStatsUAS.setStatus("current")
_DsxT3E3IfAnsiCurrentLineStatsCV_Type = Unsigned32
_DsxT3E3IfAnsiCurrentLineStatsCV_Object = MibTableColumn
dsxT3E3IfAnsiCurrentLineStatsCV = _DsxT3E3IfAnsiCurrentLineStatsCV_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 3, 3, 1, 1, 8),
    _DsxT3E3IfAnsiCurrentLineStatsCV_Type()
)
dsxT3E3IfAnsiCurrentLineStatsCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT3E3IfAnsiCurrentLineStatsCV.setStatus("current")
_DsxT3E3IfAnsiCurrentLineStatsES_Type = Unsigned32
_DsxT3E3IfAnsiCurrentLineStatsES_Object = MibTableColumn
dsxT3E3IfAnsiCurrentLineStatsES = _DsxT3E3IfAnsiCurrentLineStatsES_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 3, 3, 1, 1, 9),
    _DsxT3E3IfAnsiCurrentLineStatsES_Type()
)
dsxT3E3IfAnsiCurrentLineStatsES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT3E3IfAnsiCurrentLineStatsES.setStatus("current")
_DsxT3E3IfAnsiCurrentLineStatsSES_Type = Unsigned32
_DsxT3E3IfAnsiCurrentLineStatsSES_Object = MibTableColumn
dsxT3E3IfAnsiCurrentLineStatsSES = _DsxT3E3IfAnsiCurrentLineStatsSES_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 3, 3, 1, 1, 10),
    _DsxT3E3IfAnsiCurrentLineStatsSES_Type()
)
dsxT3E3IfAnsiCurrentLineStatsSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT3E3IfAnsiCurrentLineStatsSES.setStatus("current")
_DsxT3E3IfAnsiTotalStatsTable_Object = MibTable
dsxT3E3IfAnsiTotalStatsTable = _DsxT3E3IfAnsiTotalStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 3, 3, 2)
)
if mibBuilder.loadTexts:
    dsxT3E3IfAnsiTotalStatsTable.setStatus("current")
_DsxT3E3IfAnsiTotalStatsEntry_Object = MibTableRow
dsxT3E3IfAnsiTotalStatsEntry = _DsxT3E3IfAnsiTotalStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 3, 3, 2, 1)
)
if mibBuilder.loadTexts:
    dsxT3E3IfAnsiTotalStatsEntry.setStatus("current")
_DsxT3E3IfAnsiTotalPathStatsCV_Type = Unsigned32
_DsxT3E3IfAnsiTotalPathStatsCV_Object = MibTableColumn
dsxT3E3IfAnsiTotalPathStatsCV = _DsxT3E3IfAnsiTotalPathStatsCV_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 3, 3, 2, 1, 1),
    _DsxT3E3IfAnsiTotalPathStatsCV_Type()
)
dsxT3E3IfAnsiTotalPathStatsCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT3E3IfAnsiTotalPathStatsCV.setStatus("current")
_DsxT3E3IfAnsiTotalPathStatsES_Type = Unsigned32
_DsxT3E3IfAnsiTotalPathStatsES_Object = MibTableColumn
dsxT3E3IfAnsiTotalPathStatsES = _DsxT3E3IfAnsiTotalPathStatsES_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 3, 3, 2, 1, 2),
    _DsxT3E3IfAnsiTotalPathStatsES_Type()
)
dsxT3E3IfAnsiTotalPathStatsES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT3E3IfAnsiTotalPathStatsES.setStatus("current")
_DsxT3E3IfAnsiTotalPathStatsSES_Type = Unsigned32
_DsxT3E3IfAnsiTotalPathStatsSES_Object = MibTableColumn
dsxT3E3IfAnsiTotalPathStatsSES = _DsxT3E3IfAnsiTotalPathStatsSES_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 3, 3, 2, 1, 3),
    _DsxT3E3IfAnsiTotalPathStatsSES_Type()
)
dsxT3E3IfAnsiTotalPathStatsSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT3E3IfAnsiTotalPathStatsSES.setStatus("current")
_DsxT3E3IfAnsiTotalPathStatsSAS_Type = Unsigned32
_DsxT3E3IfAnsiTotalPathStatsSAS_Object = MibTableColumn
dsxT3E3IfAnsiTotalPathStatsSAS = _DsxT3E3IfAnsiTotalPathStatsSAS_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 3, 3, 2, 1, 4),
    _DsxT3E3IfAnsiTotalPathStatsSAS_Type()
)
dsxT3E3IfAnsiTotalPathStatsSAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT3E3IfAnsiTotalPathStatsSAS.setStatus("current")
_DsxT3E3IfAnsiTotalPathStatsUAS_Type = Unsigned32
_DsxT3E3IfAnsiTotalPathStatsUAS_Object = MibTableColumn
dsxT3E3IfAnsiTotalPathStatsUAS = _DsxT3E3IfAnsiTotalPathStatsUAS_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 3, 3, 2, 1, 5),
    _DsxT3E3IfAnsiTotalPathStatsUAS_Type()
)
dsxT3E3IfAnsiTotalPathStatsUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT3E3IfAnsiTotalPathStatsUAS.setStatus("current")
_DsxT3E3IfAnsiTotalLineStatsCV_Type = Unsigned32
_DsxT3E3IfAnsiTotalLineStatsCV_Object = MibTableColumn
dsxT3E3IfAnsiTotalLineStatsCV = _DsxT3E3IfAnsiTotalLineStatsCV_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 3, 3, 2, 1, 6),
    _DsxT3E3IfAnsiTotalLineStatsCV_Type()
)
dsxT3E3IfAnsiTotalLineStatsCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT3E3IfAnsiTotalLineStatsCV.setStatus("current")
_DsxT3E3IfAnsiTotalLineStatsES_Type = Unsigned32
_DsxT3E3IfAnsiTotalLineStatsES_Object = MibTableColumn
dsxT3E3IfAnsiTotalLineStatsES = _DsxT3E3IfAnsiTotalLineStatsES_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 3, 3, 2, 1, 7),
    _DsxT3E3IfAnsiTotalLineStatsES_Type()
)
dsxT3E3IfAnsiTotalLineStatsES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT3E3IfAnsiTotalLineStatsES.setStatus("current")
_DsxT3E3IfAnsiTotalLineStatsSES_Type = Unsigned32
_DsxT3E3IfAnsiTotalLineStatsSES_Object = MibTableColumn
dsxT3E3IfAnsiTotalLineStatsSES = _DsxT3E3IfAnsiTotalLineStatsSES_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 3, 3, 2, 1, 8),
    _DsxT3E3IfAnsiTotalLineStatsSES_Type()
)
dsxT3E3IfAnsiTotalLineStatsSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT3E3IfAnsiTotalLineStatsSES.setStatus("current")
_DsxT3E3IfAnsiArchiveIntervalStatsTable_Object = MibTable
dsxT3E3IfAnsiArchiveIntervalStatsTable = _DsxT3E3IfAnsiArchiveIntervalStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 3, 3, 3)
)
if mibBuilder.loadTexts:
    dsxT3E3IfAnsiArchiveIntervalStatsTable.setStatus("current")
_DsxT3E3IfAnsiArchiveIntervalStatsEntry_Object = MibTableRow
dsxT3E3IfAnsiArchiveIntervalStatsEntry = _DsxT3E3IfAnsiArchiveIntervalStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 3, 3, 3, 1)
)
dsxT3E3IfAnsiArchiveIntervalStatsEntry.setIndexNames(
    (0, "TIARA-NETWORKS-DSX-TE3-MIB", "dsxT3E3IfIndex"),
    (0, "TIARA-NETWORKS-DSX-TE3-MIB", "dsxT3E3IfAnsiArchiveStatsInterval"),
)
if mibBuilder.loadTexts:
    dsxT3E3IfAnsiArchiveIntervalStatsEntry.setStatus("current")
_DsxT3E3IfAnsiArchiveStatsInterval_Type = Unsigned32
_DsxT3E3IfAnsiArchiveStatsInterval_Object = MibTableColumn
dsxT3E3IfAnsiArchiveStatsInterval = _DsxT3E3IfAnsiArchiveStatsInterval_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 3, 3, 3, 1, 1),
    _DsxT3E3IfAnsiArchiveStatsInterval_Type()
)
dsxT3E3IfAnsiArchiveStatsInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dsxT3E3IfAnsiArchiveStatsInterval.setStatus("current")
_DsxT3E3IfAnsiArchiveIntervalPathStatsCV_Type = Unsigned32
_DsxT3E3IfAnsiArchiveIntervalPathStatsCV_Object = MibTableColumn
dsxT3E3IfAnsiArchiveIntervalPathStatsCV = _DsxT3E3IfAnsiArchiveIntervalPathStatsCV_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 3, 3, 3, 1, 2),
    _DsxT3E3IfAnsiArchiveIntervalPathStatsCV_Type()
)
dsxT3E3IfAnsiArchiveIntervalPathStatsCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT3E3IfAnsiArchiveIntervalPathStatsCV.setStatus("current")
_DsxT3E3IfAnsiArchiveIntervalPathStatsES_Type = Unsigned32
_DsxT3E3IfAnsiArchiveIntervalPathStatsES_Object = MibTableColumn
dsxT3E3IfAnsiArchiveIntervalPathStatsES = _DsxT3E3IfAnsiArchiveIntervalPathStatsES_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 3, 3, 3, 1, 3),
    _DsxT3E3IfAnsiArchiveIntervalPathStatsES_Type()
)
dsxT3E3IfAnsiArchiveIntervalPathStatsES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT3E3IfAnsiArchiveIntervalPathStatsES.setStatus("current")
_DsxT3E3IfAnsiArchiveIntervalPathStatsSES_Type = Unsigned32
_DsxT3E3IfAnsiArchiveIntervalPathStatsSES_Object = MibTableColumn
dsxT3E3IfAnsiArchiveIntervalPathStatsSES = _DsxT3E3IfAnsiArchiveIntervalPathStatsSES_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 3, 3, 3, 1, 4),
    _DsxT3E3IfAnsiArchiveIntervalPathStatsSES_Type()
)
dsxT3E3IfAnsiArchiveIntervalPathStatsSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT3E3IfAnsiArchiveIntervalPathStatsSES.setStatus("current")
_DsxT3E3IfAnsiArchiveIntervalPathStatsSAS_Type = Unsigned32
_DsxT3E3IfAnsiArchiveIntervalPathStatsSAS_Object = MibTableColumn
dsxT3E3IfAnsiArchiveIntervalPathStatsSAS = _DsxT3E3IfAnsiArchiveIntervalPathStatsSAS_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 3, 3, 3, 1, 5),
    _DsxT3E3IfAnsiArchiveIntervalPathStatsSAS_Type()
)
dsxT3E3IfAnsiArchiveIntervalPathStatsSAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT3E3IfAnsiArchiveIntervalPathStatsSAS.setStatus("current")
_DsxT3E3IfAnsiArchiveIntervalPathStatsUAS_Type = Unsigned32
_DsxT3E3IfAnsiArchiveIntervalPathStatsUAS_Object = MibTableColumn
dsxT3E3IfAnsiArchiveIntervalPathStatsUAS = _DsxT3E3IfAnsiArchiveIntervalPathStatsUAS_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 3, 3, 3, 1, 6),
    _DsxT3E3IfAnsiArchiveIntervalPathStatsUAS_Type()
)
dsxT3E3IfAnsiArchiveIntervalPathStatsUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT3E3IfAnsiArchiveIntervalPathStatsUAS.setStatus("current")
_DsxT3E3IfAnsiArchiveIntervalLineStatsCV_Type = Unsigned32
_DsxT3E3IfAnsiArchiveIntervalLineStatsCV_Object = MibTableColumn
dsxT3E3IfAnsiArchiveIntervalLineStatsCV = _DsxT3E3IfAnsiArchiveIntervalLineStatsCV_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 3, 3, 3, 1, 7),
    _DsxT3E3IfAnsiArchiveIntervalLineStatsCV_Type()
)
dsxT3E3IfAnsiArchiveIntervalLineStatsCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT3E3IfAnsiArchiveIntervalLineStatsCV.setStatus("current")
_DsxT3E3IfAnsiArchiveIntervalLineStatsES_Type = Unsigned32
_DsxT3E3IfAnsiArchiveIntervalLineStatsES_Object = MibTableColumn
dsxT3E3IfAnsiArchiveIntervalLineStatsES = _DsxT3E3IfAnsiArchiveIntervalLineStatsES_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 3, 3, 3, 1, 8),
    _DsxT3E3IfAnsiArchiveIntervalLineStatsES_Type()
)
dsxT3E3IfAnsiArchiveIntervalLineStatsES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT3E3IfAnsiArchiveIntervalLineStatsES.setStatus("current")
_DsxT3E3IfAnsiArchiveIntervalLineStatsSES_Type = Unsigned32
_DsxT3E3IfAnsiArchiveIntervalLineStatsSES_Object = MibTableColumn
dsxT3E3IfAnsiArchiveIntervalLineStatsSES = _DsxT3E3IfAnsiArchiveIntervalLineStatsSES_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 3, 3, 3, 1, 9),
    _DsxT3E3IfAnsiArchiveIntervalLineStatsSES_Type()
)
dsxT3E3IfAnsiArchiveIntervalLineStatsSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT3E3IfAnsiArchiveIntervalLineStatsSES.setStatus("current")
_DsxT3E3IfIetfStatsGroup_ObjectIdentity = ObjectIdentity
dsxT3E3IfIetfStatsGroup = _DsxT3E3IfIetfStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 3, 4)
)
_DsxT3E3IfIetfCurrentStatsTable_Object = MibTable
dsxT3E3IfIetfCurrentStatsTable = _DsxT3E3IfIetfCurrentStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 3, 4, 1)
)
if mibBuilder.loadTexts:
    dsxT3E3IfIetfCurrentStatsTable.setStatus("current")
_DsxT3E3IfIetfCurrentStatsEntry_Object = MibTableRow
dsxT3E3IfIetfCurrentStatsEntry = _DsxT3E3IfIetfCurrentStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 3, 4, 1, 1)
)
if mibBuilder.loadTexts:
    dsxT3E3IfIetfCurrentStatsEntry.setStatus("current")
_DsxT3E3IfIetfCurrentStatsUASState_Type = TruthValue
_DsxT3E3IfIetfCurrentStatsUASState_Object = MibTableColumn
dsxT3E3IfIetfCurrentStatsUASState = _DsxT3E3IfIetfCurrentStatsUASState_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 3, 4, 1, 1, 1),
    _DsxT3E3IfIetfCurrentStatsUASState_Type()
)
dsxT3E3IfIetfCurrentStatsUASState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT3E3IfIetfCurrentStatsUASState.setStatus("current")
_DsxT3E3IfIetfCurrentStatsTimeInCurrent_Type = Unsigned32
_DsxT3E3IfIetfCurrentStatsTimeInCurrent_Object = MibTableColumn
dsxT3E3IfIetfCurrentStatsTimeInCurrent = _DsxT3E3IfIetfCurrentStatsTimeInCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 3, 4, 1, 1, 2),
    _DsxT3E3IfIetfCurrentStatsTimeInCurrent_Type()
)
dsxT3E3IfIetfCurrentStatsTimeInCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT3E3IfIetfCurrentStatsTimeInCurrent.setStatus("current")
_DsxT3E3IfIetfCurrentStatsPES_Type = Unsigned32
_DsxT3E3IfIetfCurrentStatsPES_Object = MibTableColumn
dsxT3E3IfIetfCurrentStatsPES = _DsxT3E3IfIetfCurrentStatsPES_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 3, 4, 1, 1, 3),
    _DsxT3E3IfIetfCurrentStatsPES_Type()
)
dsxT3E3IfIetfCurrentStatsPES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT3E3IfIetfCurrentStatsPES.setStatus("current")
_DsxT3E3IfIetfCurrentStatsPSES_Type = Unsigned32
_DsxT3E3IfIetfCurrentStatsPSES_Object = MibTableColumn
dsxT3E3IfIetfCurrentStatsPSES = _DsxT3E3IfIetfCurrentStatsPSES_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 3, 4, 1, 1, 4),
    _DsxT3E3IfIetfCurrentStatsPSES_Type()
)
dsxT3E3IfIetfCurrentStatsPSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT3E3IfIetfCurrentStatsPSES.setStatus("current")
_DsxT3E3IfIetfCurrentStatsSEFS_Type = Unsigned32
_DsxT3E3IfIetfCurrentStatsSEFS_Object = MibTableColumn
dsxT3E3IfIetfCurrentStatsSEFS = _DsxT3E3IfIetfCurrentStatsSEFS_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 3, 4, 1, 1, 5),
    _DsxT3E3IfIetfCurrentStatsSEFS_Type()
)
dsxT3E3IfIetfCurrentStatsSEFS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT3E3IfIetfCurrentStatsSEFS.setStatus("current")
_DsxT3E3IfIetfCurrentStatsUAS_Type = Unsigned32
_DsxT3E3IfIetfCurrentStatsUAS_Object = MibTableColumn
dsxT3E3IfIetfCurrentStatsUAS = _DsxT3E3IfIetfCurrentStatsUAS_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 3, 4, 1, 1, 6),
    _DsxT3E3IfIetfCurrentStatsUAS_Type()
)
dsxT3E3IfIetfCurrentStatsUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT3E3IfIetfCurrentStatsUAS.setStatus("current")
_DsxT3E3IfIetfCurrentStatsLCV_Type = Unsigned32
_DsxT3E3IfIetfCurrentStatsLCV_Object = MibTableColumn
dsxT3E3IfIetfCurrentStatsLCV = _DsxT3E3IfIetfCurrentStatsLCV_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 3, 4, 1, 1, 7),
    _DsxT3E3IfIetfCurrentStatsLCV_Type()
)
dsxT3E3IfIetfCurrentStatsLCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT3E3IfIetfCurrentStatsLCV.setStatus("current")
_DsxT3E3IfIetfCurrentStatsPCV_Type = Unsigned32
_DsxT3E3IfIetfCurrentStatsPCV_Object = MibTableColumn
dsxT3E3IfIetfCurrentStatsPCV = _DsxT3E3IfIetfCurrentStatsPCV_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 3, 4, 1, 1, 8),
    _DsxT3E3IfIetfCurrentStatsPCV_Type()
)
dsxT3E3IfIetfCurrentStatsPCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT3E3IfIetfCurrentStatsPCV.setStatus("current")
_DsxT3E3IfIetfCurrentStatsLES_Type = Unsigned32
_DsxT3E3IfIetfCurrentStatsLES_Object = MibTableColumn
dsxT3E3IfIetfCurrentStatsLES = _DsxT3E3IfIetfCurrentStatsLES_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 3, 4, 1, 1, 9),
    _DsxT3E3IfIetfCurrentStatsLES_Type()
)
dsxT3E3IfIetfCurrentStatsLES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT3E3IfIetfCurrentStatsLES.setStatus("current")
_DsxT3E3IfIetfCurrentStatsCCV_Type = Unsigned32
_DsxT3E3IfIetfCurrentStatsCCV_Object = MibTableColumn
dsxT3E3IfIetfCurrentStatsCCV = _DsxT3E3IfIetfCurrentStatsCCV_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 3, 4, 1, 1, 10),
    _DsxT3E3IfIetfCurrentStatsCCV_Type()
)
dsxT3E3IfIetfCurrentStatsCCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT3E3IfIetfCurrentStatsCCV.setStatus("current")
_DsxT3E3IfIetfCurrentStatsCES_Type = Unsigned32
_DsxT3E3IfIetfCurrentStatsCES_Object = MibTableColumn
dsxT3E3IfIetfCurrentStatsCES = _DsxT3E3IfIetfCurrentStatsCES_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 3, 4, 1, 1, 11),
    _DsxT3E3IfIetfCurrentStatsCES_Type()
)
dsxT3E3IfIetfCurrentStatsCES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT3E3IfIetfCurrentStatsCES.setStatus("current")
_DsxT3E3IfIetfCurrentStatsCSES_Type = Unsigned32
_DsxT3E3IfIetfCurrentStatsCSES_Object = MibTableColumn
dsxT3E3IfIetfCurrentStatsCSES = _DsxT3E3IfIetfCurrentStatsCSES_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 3, 4, 1, 1, 12),
    _DsxT3E3IfIetfCurrentStatsCSES_Type()
)
dsxT3E3IfIetfCurrentStatsCSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT3E3IfIetfCurrentStatsCSES.setStatus("current")
_DsxT3E3IfIetfTotalStatsTable_Object = MibTable
dsxT3E3IfIetfTotalStatsTable = _DsxT3E3IfIetfTotalStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 3, 4, 2)
)
if mibBuilder.loadTexts:
    dsxT3E3IfIetfTotalStatsTable.setStatus("current")
_DsxT3E3IfIetfTotalStatsEntry_Object = MibTableRow
dsxT3E3IfIetfTotalStatsEntry = _DsxT3E3IfIetfTotalStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 3, 4, 2, 1)
)
if mibBuilder.loadTexts:
    dsxT3E3IfIetfTotalStatsEntry.setStatus("current")
_DsxT3E3IfIetfTotalStatsPES_Type = Unsigned32
_DsxT3E3IfIetfTotalStatsPES_Object = MibTableColumn
dsxT3E3IfIetfTotalStatsPES = _DsxT3E3IfIetfTotalStatsPES_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 3, 4, 2, 1, 1),
    _DsxT3E3IfIetfTotalStatsPES_Type()
)
dsxT3E3IfIetfTotalStatsPES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT3E3IfIetfTotalStatsPES.setStatus("current")
_DsxT3E3IfIetfTotalStatsPSES_Type = Unsigned32
_DsxT3E3IfIetfTotalStatsPSES_Object = MibTableColumn
dsxT3E3IfIetfTotalStatsPSES = _DsxT3E3IfIetfTotalStatsPSES_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 3, 4, 2, 1, 2),
    _DsxT3E3IfIetfTotalStatsPSES_Type()
)
dsxT3E3IfIetfTotalStatsPSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT3E3IfIetfTotalStatsPSES.setStatus("current")
_DsxT3E3IfIetfTotalStatsSEFS_Type = Unsigned32
_DsxT3E3IfIetfTotalStatsSEFS_Object = MibTableColumn
dsxT3E3IfIetfTotalStatsSEFS = _DsxT3E3IfIetfTotalStatsSEFS_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 3, 4, 2, 1, 3),
    _DsxT3E3IfIetfTotalStatsSEFS_Type()
)
dsxT3E3IfIetfTotalStatsSEFS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT3E3IfIetfTotalStatsSEFS.setStatus("current")
_DsxT3E3IfIetfTotalStatsUAS_Type = Unsigned32
_DsxT3E3IfIetfTotalStatsUAS_Object = MibTableColumn
dsxT3E3IfIetfTotalStatsUAS = _DsxT3E3IfIetfTotalStatsUAS_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 3, 4, 2, 1, 4),
    _DsxT3E3IfIetfTotalStatsUAS_Type()
)
dsxT3E3IfIetfTotalStatsUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT3E3IfIetfTotalStatsUAS.setStatus("current")
_DsxT3E3IfIetfTotalStatsLCV_Type = Unsigned32
_DsxT3E3IfIetfTotalStatsLCV_Object = MibTableColumn
dsxT3E3IfIetfTotalStatsLCV = _DsxT3E3IfIetfTotalStatsLCV_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 3, 4, 2, 1, 5),
    _DsxT3E3IfIetfTotalStatsLCV_Type()
)
dsxT3E3IfIetfTotalStatsLCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT3E3IfIetfTotalStatsLCV.setStatus("current")
_DsxT3E3IfIetfTotalStatsPCV_Type = Unsigned32
_DsxT3E3IfIetfTotalStatsPCV_Object = MibTableColumn
dsxT3E3IfIetfTotalStatsPCV = _DsxT3E3IfIetfTotalStatsPCV_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 3, 4, 2, 1, 6),
    _DsxT3E3IfIetfTotalStatsPCV_Type()
)
dsxT3E3IfIetfTotalStatsPCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT3E3IfIetfTotalStatsPCV.setStatus("current")
_DsxT3E3IfIetfTotalStatsLES_Type = Unsigned32
_DsxT3E3IfIetfTotalStatsLES_Object = MibTableColumn
dsxT3E3IfIetfTotalStatsLES = _DsxT3E3IfIetfTotalStatsLES_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 3, 4, 2, 1, 7),
    _DsxT3E3IfIetfTotalStatsLES_Type()
)
dsxT3E3IfIetfTotalStatsLES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT3E3IfIetfTotalStatsLES.setStatus("current")
_DsxT3E3IfIetfTotalStatsCCV_Type = Unsigned32
_DsxT3E3IfIetfTotalStatsCCV_Object = MibTableColumn
dsxT3E3IfIetfTotalStatsCCV = _DsxT3E3IfIetfTotalStatsCCV_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 3, 4, 2, 1, 8),
    _DsxT3E3IfIetfTotalStatsCCV_Type()
)
dsxT3E3IfIetfTotalStatsCCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT3E3IfIetfTotalStatsCCV.setStatus("current")
_DsxT3E3IfIetfTotalStatsCES_Type = Unsigned32
_DsxT3E3IfIetfTotalStatsCES_Object = MibTableColumn
dsxT3E3IfIetfTotalStatsCES = _DsxT3E3IfIetfTotalStatsCES_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 3, 4, 2, 1, 9),
    _DsxT3E3IfIetfTotalStatsCES_Type()
)
dsxT3E3IfIetfTotalStatsCES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT3E3IfIetfTotalStatsCES.setStatus("current")
_DsxT3E3IfIetfTotalStatsCSES_Type = Unsigned32
_DsxT3E3IfIetfTotalStatsCSES_Object = MibTableColumn
dsxT3E3IfIetfTotalStatsCSES = _DsxT3E3IfIetfTotalStatsCSES_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 3, 4, 2, 1, 10),
    _DsxT3E3IfIetfTotalStatsCSES_Type()
)
dsxT3E3IfIetfTotalStatsCSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT3E3IfIetfTotalStatsCSES.setStatus("current")
_DsxT3E3IfIetfArchiveStatsTable_Object = MibTable
dsxT3E3IfIetfArchiveStatsTable = _DsxT3E3IfIetfArchiveStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 3, 4, 3)
)
if mibBuilder.loadTexts:
    dsxT3E3IfIetfArchiveStatsTable.setStatus("current")
_DsxT3E3IfIetfArchiveStatsEntry_Object = MibTableRow
dsxT3E3IfIetfArchiveStatsEntry = _DsxT3E3IfIetfArchiveStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 3, 4, 3, 1)
)
dsxT3E3IfIetfArchiveStatsEntry.setIndexNames(
    (0, "TIARA-NETWORKS-DSX-TE3-MIB", "dsxT3E3IfIndex"),
    (0, "TIARA-NETWORKS-DSX-TE3-MIB", "dsxT3E3IfIetfArchiveStatsInterval"),
)
if mibBuilder.loadTexts:
    dsxT3E3IfIetfArchiveStatsEntry.setStatus("current")
_DsxT3E3IfIetfArchiveStatsInterval_Type = Unsigned32
_DsxT3E3IfIetfArchiveStatsInterval_Object = MibTableColumn
dsxT3E3IfIetfArchiveStatsInterval = _DsxT3E3IfIetfArchiveStatsInterval_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 3, 4, 3, 1, 1),
    _DsxT3E3IfIetfArchiveStatsInterval_Type()
)
dsxT3E3IfIetfArchiveStatsInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dsxT3E3IfIetfArchiveStatsInterval.setStatus("current")
_DsxT3E3IfIetfArchiveStatsPES_Type = Unsigned32
_DsxT3E3IfIetfArchiveStatsPES_Object = MibTableColumn
dsxT3E3IfIetfArchiveStatsPES = _DsxT3E3IfIetfArchiveStatsPES_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 3, 4, 3, 1, 2),
    _DsxT3E3IfIetfArchiveStatsPES_Type()
)
dsxT3E3IfIetfArchiveStatsPES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT3E3IfIetfArchiveStatsPES.setStatus("current")
_DsxT3E3IfIetfArchiveStatsPSES_Type = Unsigned32
_DsxT3E3IfIetfArchiveStatsPSES_Object = MibTableColumn
dsxT3E3IfIetfArchiveStatsPSES = _DsxT3E3IfIetfArchiveStatsPSES_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 3, 4, 3, 1, 3),
    _DsxT3E3IfIetfArchiveStatsPSES_Type()
)
dsxT3E3IfIetfArchiveStatsPSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT3E3IfIetfArchiveStatsPSES.setStatus("current")
_DsxT3E3IfIetfArchiveStatsSEFS_Type = Unsigned32
_DsxT3E3IfIetfArchiveStatsSEFS_Object = MibTableColumn
dsxT3E3IfIetfArchiveStatsSEFS = _DsxT3E3IfIetfArchiveStatsSEFS_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 3, 4, 3, 1, 4),
    _DsxT3E3IfIetfArchiveStatsSEFS_Type()
)
dsxT3E3IfIetfArchiveStatsSEFS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT3E3IfIetfArchiveStatsSEFS.setStatus("current")
_DsxT3E3IfIetfArchiveStatsUAS_Type = Unsigned32
_DsxT3E3IfIetfArchiveStatsUAS_Object = MibTableColumn
dsxT3E3IfIetfArchiveStatsUAS = _DsxT3E3IfIetfArchiveStatsUAS_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 3, 4, 3, 1, 5),
    _DsxT3E3IfIetfArchiveStatsUAS_Type()
)
dsxT3E3IfIetfArchiveStatsUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT3E3IfIetfArchiveStatsUAS.setStatus("current")
_DsxT3E3IfIetfArchiveStatsLCV_Type = Unsigned32
_DsxT3E3IfIetfArchiveStatsLCV_Object = MibTableColumn
dsxT3E3IfIetfArchiveStatsLCV = _DsxT3E3IfIetfArchiveStatsLCV_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 3, 4, 3, 1, 6),
    _DsxT3E3IfIetfArchiveStatsLCV_Type()
)
dsxT3E3IfIetfArchiveStatsLCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT3E3IfIetfArchiveStatsLCV.setStatus("current")
_DsxT3E3IfIetfArchiveStatsPCV_Type = Unsigned32
_DsxT3E3IfIetfArchiveStatsPCV_Object = MibTableColumn
dsxT3E3IfIetfArchiveStatsPCV = _DsxT3E3IfIetfArchiveStatsPCV_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 3, 4, 3, 1, 7),
    _DsxT3E3IfIetfArchiveStatsPCV_Type()
)
dsxT3E3IfIetfArchiveStatsPCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT3E3IfIetfArchiveStatsPCV.setStatus("current")
_DsxT3E3IfIetfArchiveStatsLES_Type = Unsigned32
_DsxT3E3IfIetfArchiveStatsLES_Object = MibTableColumn
dsxT3E3IfIetfArchiveStatsLES = _DsxT3E3IfIetfArchiveStatsLES_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 3, 4, 3, 1, 8),
    _DsxT3E3IfIetfArchiveStatsLES_Type()
)
dsxT3E3IfIetfArchiveStatsLES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT3E3IfIetfArchiveStatsLES.setStatus("current")
_DsxT3E3IfIetfArchiveStatsCCV_Type = Unsigned32
_DsxT3E3IfIetfArchiveStatsCCV_Object = MibTableColumn
dsxT3E3IfIetfArchiveStatsCCV = _DsxT3E3IfIetfArchiveStatsCCV_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 3, 4, 3, 1, 9),
    _DsxT3E3IfIetfArchiveStatsCCV_Type()
)
dsxT3E3IfIetfArchiveStatsCCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT3E3IfIetfArchiveStatsCCV.setStatus("current")
_DsxT3E3IfIetfArchiveStatsCES_Type = Unsigned32
_DsxT3E3IfIetfArchiveStatsCES_Object = MibTableColumn
dsxT3E3IfIetfArchiveStatsCES = _DsxT3E3IfIetfArchiveStatsCES_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 3, 4, 3, 1, 10),
    _DsxT3E3IfIetfArchiveStatsCES_Type()
)
dsxT3E3IfIetfArchiveStatsCES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT3E3IfIetfArchiveStatsCES.setStatus("current")
_DsxT3E3IfIetfArchiveStatsCSES_Type = Unsigned32
_DsxT3E3IfIetfArchiveStatsCSES_Object = MibTableColumn
dsxT3E3IfIetfArchiveStatsCSES = _DsxT3E3IfIetfArchiveStatsCSES_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 3, 4, 3, 1, 11),
    _DsxT3E3IfIetfArchiveStatsCSES_Type()
)
dsxT3E3IfIetfArchiveStatsCSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT3E3IfIetfArchiveStatsCSES.setStatus("current")
_DsxT3E3IfUserStatsGroup_ObjectIdentity = ObjectIdentity
dsxT3E3IfUserStatsGroup = _DsxT3E3IfUserStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 3, 5)
)
_DsxT3E3IfUserCurrentStatsTable_Object = MibTable
dsxT3E3IfUserCurrentStatsTable = _DsxT3E3IfUserCurrentStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 3, 5, 1)
)
if mibBuilder.loadTexts:
    dsxT3E3IfUserCurrentStatsTable.setStatus("current")
_DsxT3E3IfUserCurrentStatsEntry_Object = MibTableRow
dsxT3E3IfUserCurrentStatsEntry = _DsxT3E3IfUserCurrentStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 3, 5, 1, 1)
)
if mibBuilder.loadTexts:
    dsxT3E3IfUserCurrentStatsEntry.setStatus("current")
_DsxT3E3IfUserCurrentStatsUASState_Type = TruthValue
_DsxT3E3IfUserCurrentStatsUASState_Object = MibTableColumn
dsxT3E3IfUserCurrentStatsUASState = _DsxT3E3IfUserCurrentStatsUASState_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 3, 5, 1, 1, 1),
    _DsxT3E3IfUserCurrentStatsUASState_Type()
)
dsxT3E3IfUserCurrentStatsUASState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT3E3IfUserCurrentStatsUASState.setStatus("current")
_DsxT3E3IfUserCurrentStatsTimeInCurrent_Type = Unsigned32
_DsxT3E3IfUserCurrentStatsTimeInCurrent_Object = MibTableColumn
dsxT3E3IfUserCurrentStatsTimeInCurrent = _DsxT3E3IfUserCurrentStatsTimeInCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 3, 5, 1, 1, 2),
    _DsxT3E3IfUserCurrentStatsTimeInCurrent_Type()
)
dsxT3E3IfUserCurrentStatsTimeInCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT3E3IfUserCurrentStatsTimeInCurrent.setStatus("current")
_DsxT3E3IfUserCurrentStatsLCV_Type = Unsigned32
_DsxT3E3IfUserCurrentStatsLCV_Object = MibTableColumn
dsxT3E3IfUserCurrentStatsLCV = _DsxT3E3IfUserCurrentStatsLCV_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 3, 5, 1, 1, 3),
    _DsxT3E3IfUserCurrentStatsLCV_Type()
)
dsxT3E3IfUserCurrentStatsLCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT3E3IfUserCurrentStatsLCV.setStatus("current")
_DsxT3E3IfUserCurrentStatsFBE_Type = Unsigned32
_DsxT3E3IfUserCurrentStatsFBE_Object = MibTableColumn
dsxT3E3IfUserCurrentStatsFBE = _DsxT3E3IfUserCurrentStatsFBE_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 3, 5, 1, 1, 4),
    _DsxT3E3IfUserCurrentStatsFBE_Type()
)
dsxT3E3IfUserCurrentStatsFBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT3E3IfUserCurrentStatsFBE.setStatus("current")
_DsxT3E3IfUserCurrentStatsPBE_Type = Unsigned32
_DsxT3E3IfUserCurrentStatsPBE_Object = MibTableColumn
dsxT3E3IfUserCurrentStatsPBE = _DsxT3E3IfUserCurrentStatsPBE_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 3, 5, 1, 1, 5),
    _DsxT3E3IfUserCurrentStatsPBE_Type()
)
dsxT3E3IfUserCurrentStatsPBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT3E3IfUserCurrentStatsPBE.setStatus("current")
_DsxT3E3IfUserCurrentStatsCPBE_Type = Unsigned32
_DsxT3E3IfUserCurrentStatsCPBE_Object = MibTableColumn
dsxT3E3IfUserCurrentStatsCPBE = _DsxT3E3IfUserCurrentStatsCPBE_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 3, 5, 1, 1, 6),
    _DsxT3E3IfUserCurrentStatsCPBE_Type()
)
dsxT3E3IfUserCurrentStatsCPBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT3E3IfUserCurrentStatsCPBE.setStatus("current")
_DsxT3E3IfUserCurrentStatsFEBE_Type = Unsigned32
_DsxT3E3IfUserCurrentStatsFEBE_Object = MibTableColumn
dsxT3E3IfUserCurrentStatsFEBE = _DsxT3E3IfUserCurrentStatsFEBE_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 3, 5, 1, 1, 7),
    _DsxT3E3IfUserCurrentStatsFEBE_Type()
)
dsxT3E3IfUserCurrentStatsFEBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT3E3IfUserCurrentStatsFEBE.setStatus("current")
_DsxT3E3IfUserCurrentStatsEXZ_Type = Unsigned32
_DsxT3E3IfUserCurrentStatsEXZ_Object = MibTableColumn
dsxT3E3IfUserCurrentStatsEXZ = _DsxT3E3IfUserCurrentStatsEXZ_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 3, 5, 1, 1, 8),
    _DsxT3E3IfUserCurrentStatsEXZ_Type()
)
dsxT3E3IfUserCurrentStatsEXZ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT3E3IfUserCurrentStatsEXZ.setStatus("current")
_DsxT3E3IfUserCurrentStatsCOFA_Type = Unsigned32
_DsxT3E3IfUserCurrentStatsCOFA_Object = MibTableColumn
dsxT3E3IfUserCurrentStatsCOFA = _DsxT3E3IfUserCurrentStatsCOFA_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 3, 5, 1, 1, 9),
    _DsxT3E3IfUserCurrentStatsCOFA_Type()
)
dsxT3E3IfUserCurrentStatsCOFA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT3E3IfUserCurrentStatsCOFA.setStatus("current")
_DsxT3E3IfUserTotalStatsTable_Object = MibTable
dsxT3E3IfUserTotalStatsTable = _DsxT3E3IfUserTotalStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 3, 5, 2)
)
if mibBuilder.loadTexts:
    dsxT3E3IfUserTotalStatsTable.setStatus("current")
_DsxT3E3IfUserTotalStatsEntry_Object = MibTableRow
dsxT3E3IfUserTotalStatsEntry = _DsxT3E3IfUserTotalStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 3, 5, 2, 1)
)
dsxT3E3IfUserTotalStatsEntry.setIndexNames(
    (0, "TIARA-NETWORKS-DSX-TE3-MIB", "dsxT3E3IfIndex"),
    (0, "TIARA-NETWORKS-DSX-TE3-MIB", "dsxT3E3IfUserTotalStatsDay"),
)
if mibBuilder.loadTexts:
    dsxT3E3IfUserTotalStatsEntry.setStatus("current")
_DsxT3E3IfUserTotalStatsDay_Type = Unsigned32
_DsxT3E3IfUserTotalStatsDay_Object = MibTableColumn
dsxT3E3IfUserTotalStatsDay = _DsxT3E3IfUserTotalStatsDay_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 3, 5, 2, 1, 1),
    _DsxT3E3IfUserTotalStatsDay_Type()
)
dsxT3E3IfUserTotalStatsDay.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dsxT3E3IfUserTotalStatsDay.setStatus("current")
_DsxT3E3IfUserTotalStatsLCV_Type = Unsigned32
_DsxT3E3IfUserTotalStatsLCV_Object = MibTableColumn
dsxT3E3IfUserTotalStatsLCV = _DsxT3E3IfUserTotalStatsLCV_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 3, 5, 2, 1, 2),
    _DsxT3E3IfUserTotalStatsLCV_Type()
)
dsxT3E3IfUserTotalStatsLCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT3E3IfUserTotalStatsLCV.setStatus("current")
_DsxT3E3IfUserTotalStatsFBE_Type = Unsigned32
_DsxT3E3IfUserTotalStatsFBE_Object = MibTableColumn
dsxT3E3IfUserTotalStatsFBE = _DsxT3E3IfUserTotalStatsFBE_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 3, 5, 2, 1, 3),
    _DsxT3E3IfUserTotalStatsFBE_Type()
)
dsxT3E3IfUserTotalStatsFBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT3E3IfUserTotalStatsFBE.setStatus("current")
_DsxT3E3IfUserTotalStatsPBE_Type = Unsigned32
_DsxT3E3IfUserTotalStatsPBE_Object = MibTableColumn
dsxT3E3IfUserTotalStatsPBE = _DsxT3E3IfUserTotalStatsPBE_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 3, 5, 2, 1, 4),
    _DsxT3E3IfUserTotalStatsPBE_Type()
)
dsxT3E3IfUserTotalStatsPBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT3E3IfUserTotalStatsPBE.setStatus("current")
_DsxT3E3IfUserTotalStatsCPBE_Type = Unsigned32
_DsxT3E3IfUserTotalStatsCPBE_Object = MibTableColumn
dsxT3E3IfUserTotalStatsCPBE = _DsxT3E3IfUserTotalStatsCPBE_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 3, 5, 2, 1, 5),
    _DsxT3E3IfUserTotalStatsCPBE_Type()
)
dsxT3E3IfUserTotalStatsCPBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT3E3IfUserTotalStatsCPBE.setStatus("current")
_DsxT3E3IfUserTotalStatsFEBE_Type = Unsigned32
_DsxT3E3IfUserTotalStatsFEBE_Object = MibTableColumn
dsxT3E3IfUserTotalStatsFEBE = _DsxT3E3IfUserTotalStatsFEBE_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 3, 5, 2, 1, 6),
    _DsxT3E3IfUserTotalStatsFEBE_Type()
)
dsxT3E3IfUserTotalStatsFEBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT3E3IfUserTotalStatsFEBE.setStatus("current")
_DsxT3E3IfUserTotalStatsEXZ_Type = Unsigned32
_DsxT3E3IfUserTotalStatsEXZ_Object = MibTableColumn
dsxT3E3IfUserTotalStatsEXZ = _DsxT3E3IfUserTotalStatsEXZ_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 3, 5, 2, 1, 7),
    _DsxT3E3IfUserTotalStatsEXZ_Type()
)
dsxT3E3IfUserTotalStatsEXZ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT3E3IfUserTotalStatsEXZ.setStatus("current")
_DsxT3E3IfUserTotalStatsCOFA_Type = Unsigned32
_DsxT3E3IfUserTotalStatsCOFA_Object = MibTableColumn
dsxT3E3IfUserTotalStatsCOFA = _DsxT3E3IfUserTotalStatsCOFA_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 3, 5, 2, 1, 8),
    _DsxT3E3IfUserTotalStatsCOFA_Type()
)
dsxT3E3IfUserTotalStatsCOFA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT3E3IfUserTotalStatsCOFA.setStatus("current")
_DsxT3E3IfUserLifetimeStatsTable_Object = MibTable
dsxT3E3IfUserLifetimeStatsTable = _DsxT3E3IfUserLifetimeStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 3, 5, 3)
)
if mibBuilder.loadTexts:
    dsxT3E3IfUserLifetimeStatsTable.setStatus("current")
_DsxT3E3IfUserLifetimeStatsEntry_Object = MibTableRow
dsxT3E3IfUserLifetimeStatsEntry = _DsxT3E3IfUserLifetimeStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 3, 5, 3, 1)
)
if mibBuilder.loadTexts:
    dsxT3E3IfUserLifetimeStatsEntry.setStatus("current")
_DsxT3E3IfUserLifetimeStatsPES_Type = Unsigned32
_DsxT3E3IfUserLifetimeStatsPES_Object = MibTableColumn
dsxT3E3IfUserLifetimeStatsPES = _DsxT3E3IfUserLifetimeStatsPES_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 3, 5, 3, 1, 1),
    _DsxT3E3IfUserLifetimeStatsPES_Type()
)
dsxT3E3IfUserLifetimeStatsPES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT3E3IfUserLifetimeStatsPES.setStatus("current")
_DsxT3E3IfUserLifetimeStatsPSES_Type = Unsigned32
_DsxT3E3IfUserLifetimeStatsPSES_Object = MibTableColumn
dsxT3E3IfUserLifetimeStatsPSES = _DsxT3E3IfUserLifetimeStatsPSES_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 3, 5, 3, 1, 2),
    _DsxT3E3IfUserLifetimeStatsPSES_Type()
)
dsxT3E3IfUserLifetimeStatsPSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT3E3IfUserLifetimeStatsPSES.setStatus("current")
_DsxT3E3IfUserLifetimeStatsSEFS_Type = Unsigned32
_DsxT3E3IfUserLifetimeStatsSEFS_Object = MibTableColumn
dsxT3E3IfUserLifetimeStatsSEFS = _DsxT3E3IfUserLifetimeStatsSEFS_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 3, 5, 3, 1, 3),
    _DsxT3E3IfUserLifetimeStatsSEFS_Type()
)
dsxT3E3IfUserLifetimeStatsSEFS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT3E3IfUserLifetimeStatsSEFS.setStatus("current")
_DsxT3E3IfUserLifetimeStatsUAS_Type = Unsigned32
_DsxT3E3IfUserLifetimeStatsUAS_Object = MibTableColumn
dsxT3E3IfUserLifetimeStatsUAS = _DsxT3E3IfUserLifetimeStatsUAS_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 3, 5, 3, 1, 4),
    _DsxT3E3IfUserLifetimeStatsUAS_Type()
)
dsxT3E3IfUserLifetimeStatsUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT3E3IfUserLifetimeStatsUAS.setStatus("current")
_DsxT3E3IfUserLifetimeStatsLCV_Type = Unsigned32
_DsxT3E3IfUserLifetimeStatsLCV_Object = MibTableColumn
dsxT3E3IfUserLifetimeStatsLCV = _DsxT3E3IfUserLifetimeStatsLCV_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 3, 5, 3, 1, 5),
    _DsxT3E3IfUserLifetimeStatsLCV_Type()
)
dsxT3E3IfUserLifetimeStatsLCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT3E3IfUserLifetimeStatsLCV.setStatus("current")
_DsxT3E3IfUserLifetimeStatsPCV_Type = Unsigned32
_DsxT3E3IfUserLifetimeStatsPCV_Object = MibTableColumn
dsxT3E3IfUserLifetimeStatsPCV = _DsxT3E3IfUserLifetimeStatsPCV_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 3, 5, 3, 1, 6),
    _DsxT3E3IfUserLifetimeStatsPCV_Type()
)
dsxT3E3IfUserLifetimeStatsPCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT3E3IfUserLifetimeStatsPCV.setStatus("current")
_DsxT3E3IfUserLifetimeStatsLES_Type = Unsigned32
_DsxT3E3IfUserLifetimeStatsLES_Object = MibTableColumn
dsxT3E3IfUserLifetimeStatsLES = _DsxT3E3IfUserLifetimeStatsLES_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 3, 5, 3, 1, 7),
    _DsxT3E3IfUserLifetimeStatsLES_Type()
)
dsxT3E3IfUserLifetimeStatsLES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT3E3IfUserLifetimeStatsLES.setStatus("current")
_DsxT3E3IfUserLifetimeStatsCCV_Type = Unsigned32
_DsxT3E3IfUserLifetimeStatsCCV_Object = MibTableColumn
dsxT3E3IfUserLifetimeStatsCCV = _DsxT3E3IfUserLifetimeStatsCCV_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 3, 5, 3, 1, 8),
    _DsxT3E3IfUserLifetimeStatsCCV_Type()
)
dsxT3E3IfUserLifetimeStatsCCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT3E3IfUserLifetimeStatsCCV.setStatus("current")
_DsxT3E3IfUserLifetimeStatsCES_Type = Unsigned32
_DsxT3E3IfUserLifetimeStatsCES_Object = MibTableColumn
dsxT3E3IfUserLifetimeStatsCES = _DsxT3E3IfUserLifetimeStatsCES_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 3, 5, 3, 1, 9),
    _DsxT3E3IfUserLifetimeStatsCES_Type()
)
dsxT3E3IfUserLifetimeStatsCES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT3E3IfUserLifetimeStatsCES.setStatus("current")
_DsxT3E3IfUserLifetimeStatsFBE_Type = Unsigned32
_DsxT3E3IfUserLifetimeStatsFBE_Object = MibTableColumn
dsxT3E3IfUserLifetimeStatsFBE = _DsxT3E3IfUserLifetimeStatsFBE_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 3, 5, 3, 1, 10),
    _DsxT3E3IfUserLifetimeStatsFBE_Type()
)
dsxT3E3IfUserLifetimeStatsFBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT3E3IfUserLifetimeStatsFBE.setStatus("current")
_DsxT3E3IfUserLifetimeStatsPBE_Type = Unsigned32
_DsxT3E3IfUserLifetimeStatsPBE_Object = MibTableColumn
dsxT3E3IfUserLifetimeStatsPBE = _DsxT3E3IfUserLifetimeStatsPBE_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 3, 5, 3, 1, 11),
    _DsxT3E3IfUserLifetimeStatsPBE_Type()
)
dsxT3E3IfUserLifetimeStatsPBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT3E3IfUserLifetimeStatsPBE.setStatus("current")
_DsxT3E3IfUserLifetimeStatsCPBE_Type = Unsigned32
_DsxT3E3IfUserLifetimeStatsCPBE_Object = MibTableColumn
dsxT3E3IfUserLifetimeStatsCPBE = _DsxT3E3IfUserLifetimeStatsCPBE_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 3, 5, 3, 1, 12),
    _DsxT3E3IfUserLifetimeStatsCPBE_Type()
)
dsxT3E3IfUserLifetimeStatsCPBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT3E3IfUserLifetimeStatsCPBE.setStatus("current")
_DsxT3E3IfUserLifetimeStatsFEBE_Type = Unsigned32
_DsxT3E3IfUserLifetimeStatsFEBE_Object = MibTableColumn
dsxT3E3IfUserLifetimeStatsFEBE = _DsxT3E3IfUserLifetimeStatsFEBE_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 3, 5, 3, 1, 13),
    _DsxT3E3IfUserLifetimeStatsFEBE_Type()
)
dsxT3E3IfUserLifetimeStatsFEBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT3E3IfUserLifetimeStatsFEBE.setStatus("current")
_DsxT3E3IfUserLifetimeStatsEXZ_Type = Unsigned32
_DsxT3E3IfUserLifetimeStatsEXZ_Object = MibTableColumn
dsxT3E3IfUserLifetimeStatsEXZ = _DsxT3E3IfUserLifetimeStatsEXZ_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 3, 5, 3, 1, 14),
    _DsxT3E3IfUserLifetimeStatsEXZ_Type()
)
dsxT3E3IfUserLifetimeStatsEXZ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT3E3IfUserLifetimeStatsEXZ.setStatus("current")
_DsxT3E3IfUserLifetimeStatsCOFA_Type = Unsigned32
_DsxT3E3IfUserLifetimeStatsCOFA_Object = MibTableColumn
dsxT3E3IfUserLifetimeStatsCOFA = _DsxT3E3IfUserLifetimeStatsCOFA_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 3, 5, 3, 1, 15),
    _DsxT3E3IfUserLifetimeStatsCOFA_Type()
)
dsxT3E3IfUserLifetimeStatsCOFA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT3E3IfUserLifetimeStatsCOFA.setStatus("current")
_DsxT3E3IfUserArchiveStatsTable_Object = MibTable
dsxT3E3IfUserArchiveStatsTable = _DsxT3E3IfUserArchiveStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 3, 5, 4)
)
if mibBuilder.loadTexts:
    dsxT3E3IfUserArchiveStatsTable.setStatus("current")
_DsxT3E3IfUserArchiveStatsEntry_Object = MibTableRow
dsxT3E3IfUserArchiveStatsEntry = _DsxT3E3IfUserArchiveStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 3, 5, 4, 1)
)
dsxT3E3IfUserArchiveStatsEntry.setIndexNames(
    (0, "TIARA-NETWORKS-DSX-TE3-MIB", "dsxT3E3IfIndex"),
    (0, "TIARA-NETWORKS-DSX-TE3-MIB", "dsxT3E3IfUserArchiveStatsInterval"),
)
if mibBuilder.loadTexts:
    dsxT3E3IfUserArchiveStatsEntry.setStatus("current")
_DsxT3E3IfUserArchiveStatsInterval_Type = Unsigned32
_DsxT3E3IfUserArchiveStatsInterval_Object = MibTableColumn
dsxT3E3IfUserArchiveStatsInterval = _DsxT3E3IfUserArchiveStatsInterval_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 3, 5, 4, 1, 1),
    _DsxT3E3IfUserArchiveStatsInterval_Type()
)
dsxT3E3IfUserArchiveStatsInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dsxT3E3IfUserArchiveStatsInterval.setStatus("current")
_DsxT3E3IfUserArchiveStatsLCV_Type = Unsigned32
_DsxT3E3IfUserArchiveStatsLCV_Object = MibTableColumn
dsxT3E3IfUserArchiveStatsLCV = _DsxT3E3IfUserArchiveStatsLCV_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 3, 5, 4, 1, 2),
    _DsxT3E3IfUserArchiveStatsLCV_Type()
)
dsxT3E3IfUserArchiveStatsLCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT3E3IfUserArchiveStatsLCV.setStatus("current")
_DsxT3E3IfUserArchiveStatsFBE_Type = Unsigned32
_DsxT3E3IfUserArchiveStatsFBE_Object = MibTableColumn
dsxT3E3IfUserArchiveStatsFBE = _DsxT3E3IfUserArchiveStatsFBE_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 3, 5, 4, 1, 3),
    _DsxT3E3IfUserArchiveStatsFBE_Type()
)
dsxT3E3IfUserArchiveStatsFBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT3E3IfUserArchiveStatsFBE.setStatus("current")
_DsxT3E3IfUserArchiveStatsPBE_Type = Unsigned32
_DsxT3E3IfUserArchiveStatsPBE_Object = MibTableColumn
dsxT3E3IfUserArchiveStatsPBE = _DsxT3E3IfUserArchiveStatsPBE_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 3, 5, 4, 1, 4),
    _DsxT3E3IfUserArchiveStatsPBE_Type()
)
dsxT3E3IfUserArchiveStatsPBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT3E3IfUserArchiveStatsPBE.setStatus("current")
_DsxT3E3IfUserArchiveStatsCPBE_Type = Unsigned32
_DsxT3E3IfUserArchiveStatsCPBE_Object = MibTableColumn
dsxT3E3IfUserArchiveStatsCPBE = _DsxT3E3IfUserArchiveStatsCPBE_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 3, 5, 4, 1, 5),
    _DsxT3E3IfUserArchiveStatsCPBE_Type()
)
dsxT3E3IfUserArchiveStatsCPBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT3E3IfUserArchiveStatsCPBE.setStatus("current")
_DsxT3E3IfUserArchiveStatsFEBE_Type = Unsigned32
_DsxT3E3IfUserArchiveStatsFEBE_Object = MibTableColumn
dsxT3E3IfUserArchiveStatsFEBE = _DsxT3E3IfUserArchiveStatsFEBE_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 3, 5, 4, 1, 6),
    _DsxT3E3IfUserArchiveStatsFEBE_Type()
)
dsxT3E3IfUserArchiveStatsFEBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT3E3IfUserArchiveStatsFEBE.setStatus("current")
_DsxT3E3IfUserArchiveStatsEXZ_Type = Unsigned32
_DsxT3E3IfUserArchiveStatsEXZ_Object = MibTableColumn
dsxT3E3IfUserArchiveStatsEXZ = _DsxT3E3IfUserArchiveStatsEXZ_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 3, 5, 4, 1, 7),
    _DsxT3E3IfUserArchiveStatsEXZ_Type()
)
dsxT3E3IfUserArchiveStatsEXZ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT3E3IfUserArchiveStatsEXZ.setStatus("current")
_DsxT3E3IfUserArchiveStatsCOFA_Type = Unsigned32
_DsxT3E3IfUserArchiveStatsCOFA_Object = MibTableColumn
dsxT3E3IfUserArchiveStatsCOFA = _DsxT3E3IfUserArchiveStatsCOFA_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 1, 3, 5, 4, 1, 8),
    _DsxT3E3IfUserArchiveStatsCOFA_Type()
)
dsxT3E3IfUserArchiveStatsCOFA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT3E3IfUserArchiveStatsCOFA.setStatus("current")
_DsxT3E3Traps_ObjectIdentity = ObjectIdentity
dsxT3E3Traps = _DsxT3E3Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 2)
)
_DsxT3E3TrapVariables_ObjectIdentity = ObjectIdentity
dsxT3E3TrapVariables = _DsxT3E3TrapVariables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 2, 1)
)
_DsxT3E3Number_Type = Integer32
_DsxT3E3Number_Object = MibScalar
dsxT3E3Number = _DsxT3E3Number_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 2, 1, 1),
    _DsxT3E3Number_Type()
)
dsxT3E3Number.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dsxT3E3Number.setStatus("current")


class _DsxT3E3AlarmType_Type(Integer32):
    """Custom type dsxT3E3AlarmType based on Integer32"""
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
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25)
        )
    )
    namedValues = NamedValues(
        *(("te1-alarm-threshold1", 16),
          ("te1-alarm-threshold10", 25),
          ("te1-alarm-threshold2", 17),
          ("te1-alarm-threshold3", 18),
          ("te1-alarm-threshold4", 19),
          ("te1-alarm-threshold5", 20),
          ("te1-alarm-threshold6", 21),
          ("te1-alarm-threshold7", 22),
          ("te1-alarm-threshold8", 23),
          ("te1-alarm-threshold9", 24),
          ("te3-alarm-lorc", 11),
          ("te3-alarm-rais", 1),
          ("te3-alarm-rcpe", 10),
          ("te3-alarm-rexz", 7),
          ("te3-alarm-rfebe", 8),
          ("te3-alarm-ris", 4),
          ("te3-alarm-rlof", 6),
          ("te3-alarm-rlos", 5),
          ("te3-alarm-roof", 2),
          ("te3-alarm-rpe", 9),
          ("te3-alarm-rrai", 3),
          ("te3-alarm-tais", 13),
          ("te3-alarm-tfebe", 15),
          ("te3-alarm-tpde", 12),
          ("te3-alarm-trai", 14))
    )


_DsxT3E3AlarmType_Type.__name__ = "Integer32"
_DsxT3E3AlarmType_Object = MibScalar
dsxT3E3AlarmType = _DsxT3E3AlarmType_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 2, 1, 2),
    _DsxT3E3AlarmType_Type()
)
dsxT3E3AlarmType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dsxT3E3AlarmType.setStatus("current")
dsxT3E3IfConfigLineEntry.registerAugmentions(
    ("TIARA-NETWORKS-DSX-TE3-MIB",
     "dsxT3E3IfConfigMdlEntry")
)
dsxT3E3IfConfigMdlEntry.setIndexNames(*dsxT3E3IfConfigLineEntry.getIndexNames())
dsxT3E3IfConfigLineEntry.registerAugmentions(
    ("TIARA-NETWORKS-DSX-TE3-MIB",
     "dsxT3E3IfTestConfigEntry")
)
dsxT3E3IfTestConfigEntry.setIndexNames(*dsxT3E3IfConfigLineEntry.getIndexNames())
dsxT3E3IfConfigLineEntry.registerAugmentions(
    ("TIARA-NETWORKS-DSX-TE3-MIB",
     "dsxT3E3IfStatusEntry")
)
dsxT3E3IfStatusEntry.setIndexNames(*dsxT3E3IfConfigLineEntry.getIndexNames())
dsxT3E3IfConfigLineEntry.registerAugmentions(
    ("TIARA-NETWORKS-DSX-TE3-MIB",
     "dsxT3E3IfAlarmStatusEntry")
)
dsxT3E3IfAlarmStatusEntry.setIndexNames(*dsxT3E3IfConfigLineEntry.getIndexNames())
dsxT3E3IfConfigLineEntry.registerAugmentions(
    ("TIARA-NETWORKS-DSX-TE3-MIB",
     "dsxT3E3IfTestStatusEntry")
)
dsxT3E3IfTestStatusEntry.setIndexNames(*dsxT3E3IfConfigLineEntry.getIndexNames())
dsxT3E3IfConfigLineEntry.registerAugmentions(
    ("TIARA-NETWORKS-DSX-TE3-MIB",
     "dsxT3E3IfLastTestResultEntry")
)
dsxT3E3IfLastTestResultEntry.setIndexNames(*dsxT3E3IfConfigLineEntry.getIndexNames())
dsxT3E3IfConfigLineEntry.registerAugmentions(
    ("TIARA-NETWORKS-DSX-TE3-MIB",
     "dsxT3E3IfArchiveStatsValidIntervalsEntry")
)
dsxT3E3IfArchiveStatsValidIntervalsEntry.setIndexNames(*dsxT3E3IfConfigLineEntry.getIndexNames())
dsxT3E3IfConfigLineEntry.registerAugmentions(
    ("TIARA-NETWORKS-DSX-TE3-MIB",
     "dsxT3E3IfErrorEventStatsEntry")
)
dsxT3E3IfErrorEventStatsEntry.setIndexNames(*dsxT3E3IfConfigLineEntry.getIndexNames())
dsxT3E3IfConfigLineEntry.registerAugmentions(
    ("TIARA-NETWORKS-DSX-TE3-MIB",
     "dsxT3E3IfAnsiCurrentStatsEntry")
)
dsxT3E3IfAnsiCurrentStatsEntry.setIndexNames(*dsxT3E3IfConfigLineEntry.getIndexNames())
dsxT3E3IfConfigLineEntry.registerAugmentions(
    ("TIARA-NETWORKS-DSX-TE3-MIB",
     "dsxT3E3IfAnsiTotalStatsEntry")
)
dsxT3E3IfAnsiTotalStatsEntry.setIndexNames(*dsxT3E3IfConfigLineEntry.getIndexNames())
dsxT3E3IfConfigLineEntry.registerAugmentions(
    ("TIARA-NETWORKS-DSX-TE3-MIB",
     "dsxT3E3IfIetfCurrentStatsEntry")
)
dsxT3E3IfIetfCurrentStatsEntry.setIndexNames(*dsxT3E3IfConfigLineEntry.getIndexNames())
dsxT3E3IfConfigLineEntry.registerAugmentions(
    ("TIARA-NETWORKS-DSX-TE3-MIB",
     "dsxT3E3IfIetfTotalStatsEntry")
)
dsxT3E3IfIetfTotalStatsEntry.setIndexNames(*dsxT3E3IfConfigLineEntry.getIndexNames())
dsxT3E3IfConfigLineEntry.registerAugmentions(
    ("TIARA-NETWORKS-DSX-TE3-MIB",
     "dsxT3E3IfUserCurrentStatsEntry")
)
dsxT3E3IfUserCurrentStatsEntry.setIndexNames(*dsxT3E3IfConfigLineEntry.getIndexNames())
dsxT3E3IfConfigLineEntry.registerAugmentions(
    ("TIARA-NETWORKS-DSX-TE3-MIB",
     "dsxT3E3IfUserLifetimeStatsEntry")
)
dsxT3E3IfUserLifetimeStatsEntry.setIndexNames(*dsxT3E3IfConfigLineEntry.getIndexNames())

# Managed Objects groups


# Notification objects

dsxT3E3AlarmOnTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 2, 0, 1)
)
dsxT3E3AlarmOnTrap.setObjects(
      *(("TIARA-NETWORKS-DSX-TE3-MIB", "dsxT3E3IfIndex"),
        ("TIARA-NETWORKS-DSX-TE3-MIB", "dsxT3E3Number"),
        ("TIARA-NETWORKS-DSX-TE3-MIB", "dsxT3E3AlarmType"))
)
if mibBuilder.loadTexts:
    dsxT3E3AlarmOnTrap.setStatus(
        ""
    )

dsxT3E3AlarmOffTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3, 2, 0, 2)
)
dsxT3E3AlarmOffTrap.setObjects(
      *(("TIARA-NETWORKS-DSX-TE3-MIB", "dsxT3E3IfIndex"),
        ("TIARA-NETWORKS-DSX-TE3-MIB", "dsxT3E3Number"),
        ("TIARA-NETWORKS-DSX-TE3-MIB", "dsxT3E3AlarmType"))
)
if mibBuilder.loadTexts:
    dsxT3E3AlarmOffTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIARA-NETWORKS-DSX-TE3-MIB",
    **{"dsxT3E3MIB": dsxT3E3MIB,
       "dsxT3E3IfConfigGroup": dsxT3E3IfConfigGroup,
       "dsxT3E3IfConfigLineTable": dsxT3E3IfConfigLineTable,
       "dsxT3E3IfConfigLineEntry": dsxT3E3IfConfigLineEntry,
       "dsxT3E3IfIndex": dsxT3E3IfIndex,
       "dsxT3E3IfConfigLineType": dsxT3E3IfConfigLineType,
       "dsxT3E3IfConfigLineCode": dsxT3E3IfConfigLineCode,
       "dsxT3E3IfConfigCableLength": dsxT3E3IfConfigCableLength,
       "dsxT3E3IfConfigTransmitClock": dsxT3E3IfConfigTransmitClock,
       "dsxT3E3IfConfigDS3ScramblingMode": dsxT3E3IfConfigDS3ScramblingMode,
       "dsxT3E3IfConfigDS3ScramblingEnable": dsxT3E3IfConfigDS3ScramblingEnable,
       "dsxT3E3IfConfigMdlTable": dsxT3E3IfConfigMdlTable,
       "dsxT3E3IfConfigMdlEntry": dsxT3E3IfConfigMdlEntry,
       "dsxT3E3IfConfigMdlEIC": dsxT3E3IfConfigMdlEIC,
       "dsxT3E3IfConfigMdlLIC": dsxT3E3IfConfigMdlLIC,
       "dsxT3E3IfConfigMdlFIC": dsxT3E3IfConfigMdlFIC,
       "dsxT3E3IfConfigMdlUIC": dsxT3E3IfConfigMdlUIC,
       "dsxT3E3IfConfigMdlPFI": dsxT3E3IfConfigMdlPFI,
       "dsxT3E3IfConfigMdlPort": dsxT3E3IfConfigMdlPort,
       "dsxT3E3IfConfigMdlGenerator": dsxT3E3IfConfigMdlGenerator,
       "dsxT3E3IfAlarmConfigGroup": dsxT3E3IfAlarmConfigGroup,
       "dsxT3E3IfAlarmThresholdConfigTable": dsxT3E3IfAlarmThresholdConfigTable,
       "dsxT3E3IfAlarmThresholdConfigEntry": dsxT3E3IfAlarmThresholdConfigEntry,
       "dsxT3E3IfAlarmThresholdConfigIndex": dsxT3E3IfAlarmThresholdConfigIndex,
       "dsxT3E3IfAlarmThresholdConfigObject": dsxT3E3IfAlarmThresholdConfigObject,
       "dsxT3E3IfAlarmThresholdConfigSamplingInterval": dsxT3E3IfAlarmThresholdConfigSamplingInterval,
       "dsxT3E3IfAlarmThresholdConfigSampleType": dsxT3E3IfAlarmThresholdConfigSampleType,
       "dsxT3E3IfAlarmThresholdConfigStartupType": dsxT3E3IfAlarmThresholdConfigStartupType,
       "dsxT3E3IfAlarmThresholdConfigRisingThreshold": dsxT3E3IfAlarmThresholdConfigRisingThreshold,
       "dsxT3E3IfAlarmThresholdConfigFallingThreshold": dsxT3E3IfAlarmThresholdConfigFallingThreshold,
       "dsxT3E3IfTestConfigTable": dsxT3E3IfTestConfigTable,
       "dsxT3E3IfTestConfigEntry": dsxT3E3IfTestConfigEntry,
       "dsxT3E3IfTestConfigType": dsxT3E3IfTestConfigType,
       "dsxT3E3IfTestConfigLoopCode": dsxT3E3IfTestConfigLoopCode,
       "dsxT3E3IfStatusGroup": dsxT3E3IfStatusGroup,
       "dsxT3E3IfStatusTable": dsxT3E3IfStatusTable,
       "dsxT3E3IfStatusEntry": dsxT3E3IfStatusEntry,
       "dsxT3E3IfStatusLineStatus": dsxT3E3IfStatusLineStatus,
       "dsxT3E3IfStatusTransmitClock": dsxT3E3IfStatusTransmitClock,
       "dsxT3E3IfStatusTestLED": dsxT3E3IfStatusTestLED,
       "dsxT3E3IfStatusErrorLED": dsxT3E3IfStatusErrorLED,
       "dsxT3E3IfStatusAisLED": dsxT3E3IfStatusAisLED,
       "dsxT3E3IfStatusSignalLED": dsxT3E3IfStatusSignalLED,
       "dsxT3E3IfStatusFrameLED": dsxT3E3IfStatusFrameLED,
       "dsxT3E3IfStatusYellowLED": dsxT3E3IfStatusYellowLED,
       "dsxT3E3IfAlarmStatusTable": dsxT3E3IfAlarmStatusTable,
       "dsxT3E3IfAlarmStatusEntry": dsxT3E3IfAlarmStatusEntry,
       "dsxT3E3IfAlarmStatusAlarmStatus": dsxT3E3IfAlarmStatusAlarmStatus,
       "dsxT3E3IfAlarmStatusThresholdStatus": dsxT3E3IfAlarmStatusThresholdStatus,
       "dsxT3E3IfTestStatusTable": dsxT3E3IfTestStatusTable,
       "dsxT3E3IfTestStatusEntry": dsxT3E3IfTestStatusEntry,
       "dsxT3E3IfTestStatusTestType": dsxT3E3IfTestStatusTestType,
       "dsxT3E3IfTestStatusTestState": dsxT3E3IfTestStatusTestState,
       "dsxT3E3IfTestStatusLoopCode": dsxT3E3IfTestStatusLoopCode,
       "dsxT3E3IfLastTestResultTable": dsxT3E3IfLastTestResultTable,
       "dsxT3E3IfLastTestResultEntry": dsxT3E3IfLastTestResultEntry,
       "dsxT3E3IfLastTestResultTestType": dsxT3E3IfLastTestResultTestType,
       "dsxT3E3IfLastTestResultTestState": dsxT3E3IfLastTestResultTestState,
       "dsxT3E3IfLastTestResultLoopCode": dsxT3E3IfLastTestResultLoopCode,
       "dsxT3E3IfStatsGroup": dsxT3E3IfStatsGroup,
       "dsxT3E3IfArchiveStatsValidIntervalsTable": dsxT3E3IfArchiveStatsValidIntervalsTable,
       "dsxT3E3IfArchiveStatsValidIntervalsEntry": dsxT3E3IfArchiveStatsValidIntervalsEntry,
       "dsxT3E3IfAnsiArchiveStatsValidIntervals": dsxT3E3IfAnsiArchiveStatsValidIntervals,
       "dsxT3E3IfIetfArchiveStatsValidIntervals": dsxT3E3IfIetfArchiveStatsValidIntervals,
       "dsxT3E3IfUserTotalStatsValidDays": dsxT3E3IfUserTotalStatsValidDays,
       "dsxT3E3IfUserArchiveStatsValidIntervals": dsxT3E3IfUserArchiveStatsValidIntervals,
       "dsxT3E3IfErrorEventStatsTable": dsxT3E3IfErrorEventStatsTable,
       "dsxT3E3IfErrorEventStatsEntry": dsxT3E3IfErrorEventStatsEntry,
       "dsxT3E3IfErrorEventStatsEXZ": dsxT3E3IfErrorEventStatsEXZ,
       "dsxT3E3IfErrorEventStatsPBE": dsxT3E3IfErrorEventStatsPBE,
       "dsxT3E3IfErrorEventStatsFEBE": dsxT3E3IfErrorEventStatsFEBE,
       "dsxT3E3IfAnsiStatsGroup": dsxT3E3IfAnsiStatsGroup,
       "dsxT3E3IfAnsiCurrentStatsTable": dsxT3E3IfAnsiCurrentStatsTable,
       "dsxT3E3IfAnsiCurrentStatsEntry": dsxT3E3IfAnsiCurrentStatsEntry,
       "dsxT3E3IfAnsiCurrentStatsUASState": dsxT3E3IfAnsiCurrentStatsUASState,
       "dsxT3E3IfAnsiCurrentStatsTimeInCurrent": dsxT3E3IfAnsiCurrentStatsTimeInCurrent,
       "dsxT3E3IfAnsiCurrentPathStatsCV": dsxT3E3IfAnsiCurrentPathStatsCV,
       "dsxT3E3IfAnsiCurrentPathStatsES": dsxT3E3IfAnsiCurrentPathStatsES,
       "dsxT3E3IfAnsiCurrentPathStatsSES": dsxT3E3IfAnsiCurrentPathStatsSES,
       "dsxT3E3IfAnsiCurrentPathStatsSAS": dsxT3E3IfAnsiCurrentPathStatsSAS,
       "dsxT3E3IfAnsiCurrentPathStatsUAS": dsxT3E3IfAnsiCurrentPathStatsUAS,
       "dsxT3E3IfAnsiCurrentLineStatsCV": dsxT3E3IfAnsiCurrentLineStatsCV,
       "dsxT3E3IfAnsiCurrentLineStatsES": dsxT3E3IfAnsiCurrentLineStatsES,
       "dsxT3E3IfAnsiCurrentLineStatsSES": dsxT3E3IfAnsiCurrentLineStatsSES,
       "dsxT3E3IfAnsiTotalStatsTable": dsxT3E3IfAnsiTotalStatsTable,
       "dsxT3E3IfAnsiTotalStatsEntry": dsxT3E3IfAnsiTotalStatsEntry,
       "dsxT3E3IfAnsiTotalPathStatsCV": dsxT3E3IfAnsiTotalPathStatsCV,
       "dsxT3E3IfAnsiTotalPathStatsES": dsxT3E3IfAnsiTotalPathStatsES,
       "dsxT3E3IfAnsiTotalPathStatsSES": dsxT3E3IfAnsiTotalPathStatsSES,
       "dsxT3E3IfAnsiTotalPathStatsSAS": dsxT3E3IfAnsiTotalPathStatsSAS,
       "dsxT3E3IfAnsiTotalPathStatsUAS": dsxT3E3IfAnsiTotalPathStatsUAS,
       "dsxT3E3IfAnsiTotalLineStatsCV": dsxT3E3IfAnsiTotalLineStatsCV,
       "dsxT3E3IfAnsiTotalLineStatsES": dsxT3E3IfAnsiTotalLineStatsES,
       "dsxT3E3IfAnsiTotalLineStatsSES": dsxT3E3IfAnsiTotalLineStatsSES,
       "dsxT3E3IfAnsiArchiveIntervalStatsTable": dsxT3E3IfAnsiArchiveIntervalStatsTable,
       "dsxT3E3IfAnsiArchiveIntervalStatsEntry": dsxT3E3IfAnsiArchiveIntervalStatsEntry,
       "dsxT3E3IfAnsiArchiveStatsInterval": dsxT3E3IfAnsiArchiveStatsInterval,
       "dsxT3E3IfAnsiArchiveIntervalPathStatsCV": dsxT3E3IfAnsiArchiveIntervalPathStatsCV,
       "dsxT3E3IfAnsiArchiveIntervalPathStatsES": dsxT3E3IfAnsiArchiveIntervalPathStatsES,
       "dsxT3E3IfAnsiArchiveIntervalPathStatsSES": dsxT3E3IfAnsiArchiveIntervalPathStatsSES,
       "dsxT3E3IfAnsiArchiveIntervalPathStatsSAS": dsxT3E3IfAnsiArchiveIntervalPathStatsSAS,
       "dsxT3E3IfAnsiArchiveIntervalPathStatsUAS": dsxT3E3IfAnsiArchiveIntervalPathStatsUAS,
       "dsxT3E3IfAnsiArchiveIntervalLineStatsCV": dsxT3E3IfAnsiArchiveIntervalLineStatsCV,
       "dsxT3E3IfAnsiArchiveIntervalLineStatsES": dsxT3E3IfAnsiArchiveIntervalLineStatsES,
       "dsxT3E3IfAnsiArchiveIntervalLineStatsSES": dsxT3E3IfAnsiArchiveIntervalLineStatsSES,
       "dsxT3E3IfIetfStatsGroup": dsxT3E3IfIetfStatsGroup,
       "dsxT3E3IfIetfCurrentStatsTable": dsxT3E3IfIetfCurrentStatsTable,
       "dsxT3E3IfIetfCurrentStatsEntry": dsxT3E3IfIetfCurrentStatsEntry,
       "dsxT3E3IfIetfCurrentStatsUASState": dsxT3E3IfIetfCurrentStatsUASState,
       "dsxT3E3IfIetfCurrentStatsTimeInCurrent": dsxT3E3IfIetfCurrentStatsTimeInCurrent,
       "dsxT3E3IfIetfCurrentStatsPES": dsxT3E3IfIetfCurrentStatsPES,
       "dsxT3E3IfIetfCurrentStatsPSES": dsxT3E3IfIetfCurrentStatsPSES,
       "dsxT3E3IfIetfCurrentStatsSEFS": dsxT3E3IfIetfCurrentStatsSEFS,
       "dsxT3E3IfIetfCurrentStatsUAS": dsxT3E3IfIetfCurrentStatsUAS,
       "dsxT3E3IfIetfCurrentStatsLCV": dsxT3E3IfIetfCurrentStatsLCV,
       "dsxT3E3IfIetfCurrentStatsPCV": dsxT3E3IfIetfCurrentStatsPCV,
       "dsxT3E3IfIetfCurrentStatsLES": dsxT3E3IfIetfCurrentStatsLES,
       "dsxT3E3IfIetfCurrentStatsCCV": dsxT3E3IfIetfCurrentStatsCCV,
       "dsxT3E3IfIetfCurrentStatsCES": dsxT3E3IfIetfCurrentStatsCES,
       "dsxT3E3IfIetfCurrentStatsCSES": dsxT3E3IfIetfCurrentStatsCSES,
       "dsxT3E3IfIetfTotalStatsTable": dsxT3E3IfIetfTotalStatsTable,
       "dsxT3E3IfIetfTotalStatsEntry": dsxT3E3IfIetfTotalStatsEntry,
       "dsxT3E3IfIetfTotalStatsPES": dsxT3E3IfIetfTotalStatsPES,
       "dsxT3E3IfIetfTotalStatsPSES": dsxT3E3IfIetfTotalStatsPSES,
       "dsxT3E3IfIetfTotalStatsSEFS": dsxT3E3IfIetfTotalStatsSEFS,
       "dsxT3E3IfIetfTotalStatsUAS": dsxT3E3IfIetfTotalStatsUAS,
       "dsxT3E3IfIetfTotalStatsLCV": dsxT3E3IfIetfTotalStatsLCV,
       "dsxT3E3IfIetfTotalStatsPCV": dsxT3E3IfIetfTotalStatsPCV,
       "dsxT3E3IfIetfTotalStatsLES": dsxT3E3IfIetfTotalStatsLES,
       "dsxT3E3IfIetfTotalStatsCCV": dsxT3E3IfIetfTotalStatsCCV,
       "dsxT3E3IfIetfTotalStatsCES": dsxT3E3IfIetfTotalStatsCES,
       "dsxT3E3IfIetfTotalStatsCSES": dsxT3E3IfIetfTotalStatsCSES,
       "dsxT3E3IfIetfArchiveStatsTable": dsxT3E3IfIetfArchiveStatsTable,
       "dsxT3E3IfIetfArchiveStatsEntry": dsxT3E3IfIetfArchiveStatsEntry,
       "dsxT3E3IfIetfArchiveStatsInterval": dsxT3E3IfIetfArchiveStatsInterval,
       "dsxT3E3IfIetfArchiveStatsPES": dsxT3E3IfIetfArchiveStatsPES,
       "dsxT3E3IfIetfArchiveStatsPSES": dsxT3E3IfIetfArchiveStatsPSES,
       "dsxT3E3IfIetfArchiveStatsSEFS": dsxT3E3IfIetfArchiveStatsSEFS,
       "dsxT3E3IfIetfArchiveStatsUAS": dsxT3E3IfIetfArchiveStatsUAS,
       "dsxT3E3IfIetfArchiveStatsLCV": dsxT3E3IfIetfArchiveStatsLCV,
       "dsxT3E3IfIetfArchiveStatsPCV": dsxT3E3IfIetfArchiveStatsPCV,
       "dsxT3E3IfIetfArchiveStatsLES": dsxT3E3IfIetfArchiveStatsLES,
       "dsxT3E3IfIetfArchiveStatsCCV": dsxT3E3IfIetfArchiveStatsCCV,
       "dsxT3E3IfIetfArchiveStatsCES": dsxT3E3IfIetfArchiveStatsCES,
       "dsxT3E3IfIetfArchiveStatsCSES": dsxT3E3IfIetfArchiveStatsCSES,
       "dsxT3E3IfUserStatsGroup": dsxT3E3IfUserStatsGroup,
       "dsxT3E3IfUserCurrentStatsTable": dsxT3E3IfUserCurrentStatsTable,
       "dsxT3E3IfUserCurrentStatsEntry": dsxT3E3IfUserCurrentStatsEntry,
       "dsxT3E3IfUserCurrentStatsUASState": dsxT3E3IfUserCurrentStatsUASState,
       "dsxT3E3IfUserCurrentStatsTimeInCurrent": dsxT3E3IfUserCurrentStatsTimeInCurrent,
       "dsxT3E3IfUserCurrentStatsLCV": dsxT3E3IfUserCurrentStatsLCV,
       "dsxT3E3IfUserCurrentStatsFBE": dsxT3E3IfUserCurrentStatsFBE,
       "dsxT3E3IfUserCurrentStatsPBE": dsxT3E3IfUserCurrentStatsPBE,
       "dsxT3E3IfUserCurrentStatsCPBE": dsxT3E3IfUserCurrentStatsCPBE,
       "dsxT3E3IfUserCurrentStatsFEBE": dsxT3E3IfUserCurrentStatsFEBE,
       "dsxT3E3IfUserCurrentStatsEXZ": dsxT3E3IfUserCurrentStatsEXZ,
       "dsxT3E3IfUserCurrentStatsCOFA": dsxT3E3IfUserCurrentStatsCOFA,
       "dsxT3E3IfUserTotalStatsTable": dsxT3E3IfUserTotalStatsTable,
       "dsxT3E3IfUserTotalStatsEntry": dsxT3E3IfUserTotalStatsEntry,
       "dsxT3E3IfUserTotalStatsDay": dsxT3E3IfUserTotalStatsDay,
       "dsxT3E3IfUserTotalStatsLCV": dsxT3E3IfUserTotalStatsLCV,
       "dsxT3E3IfUserTotalStatsFBE": dsxT3E3IfUserTotalStatsFBE,
       "dsxT3E3IfUserTotalStatsPBE": dsxT3E3IfUserTotalStatsPBE,
       "dsxT3E3IfUserTotalStatsCPBE": dsxT3E3IfUserTotalStatsCPBE,
       "dsxT3E3IfUserTotalStatsFEBE": dsxT3E3IfUserTotalStatsFEBE,
       "dsxT3E3IfUserTotalStatsEXZ": dsxT3E3IfUserTotalStatsEXZ,
       "dsxT3E3IfUserTotalStatsCOFA": dsxT3E3IfUserTotalStatsCOFA,
       "dsxT3E3IfUserLifetimeStatsTable": dsxT3E3IfUserLifetimeStatsTable,
       "dsxT3E3IfUserLifetimeStatsEntry": dsxT3E3IfUserLifetimeStatsEntry,
       "dsxT3E3IfUserLifetimeStatsPES": dsxT3E3IfUserLifetimeStatsPES,
       "dsxT3E3IfUserLifetimeStatsPSES": dsxT3E3IfUserLifetimeStatsPSES,
       "dsxT3E3IfUserLifetimeStatsSEFS": dsxT3E3IfUserLifetimeStatsSEFS,
       "dsxT3E3IfUserLifetimeStatsUAS": dsxT3E3IfUserLifetimeStatsUAS,
       "dsxT3E3IfUserLifetimeStatsLCV": dsxT3E3IfUserLifetimeStatsLCV,
       "dsxT3E3IfUserLifetimeStatsPCV": dsxT3E3IfUserLifetimeStatsPCV,
       "dsxT3E3IfUserLifetimeStatsLES": dsxT3E3IfUserLifetimeStatsLES,
       "dsxT3E3IfUserLifetimeStatsCCV": dsxT3E3IfUserLifetimeStatsCCV,
       "dsxT3E3IfUserLifetimeStatsCES": dsxT3E3IfUserLifetimeStatsCES,
       "dsxT3E3IfUserLifetimeStatsFBE": dsxT3E3IfUserLifetimeStatsFBE,
       "dsxT3E3IfUserLifetimeStatsPBE": dsxT3E3IfUserLifetimeStatsPBE,
       "dsxT3E3IfUserLifetimeStatsCPBE": dsxT3E3IfUserLifetimeStatsCPBE,
       "dsxT3E3IfUserLifetimeStatsFEBE": dsxT3E3IfUserLifetimeStatsFEBE,
       "dsxT3E3IfUserLifetimeStatsEXZ": dsxT3E3IfUserLifetimeStatsEXZ,
       "dsxT3E3IfUserLifetimeStatsCOFA": dsxT3E3IfUserLifetimeStatsCOFA,
       "dsxT3E3IfUserArchiveStatsTable": dsxT3E3IfUserArchiveStatsTable,
       "dsxT3E3IfUserArchiveStatsEntry": dsxT3E3IfUserArchiveStatsEntry,
       "dsxT3E3IfUserArchiveStatsInterval": dsxT3E3IfUserArchiveStatsInterval,
       "dsxT3E3IfUserArchiveStatsLCV": dsxT3E3IfUserArchiveStatsLCV,
       "dsxT3E3IfUserArchiveStatsFBE": dsxT3E3IfUserArchiveStatsFBE,
       "dsxT3E3IfUserArchiveStatsPBE": dsxT3E3IfUserArchiveStatsPBE,
       "dsxT3E3IfUserArchiveStatsCPBE": dsxT3E3IfUserArchiveStatsCPBE,
       "dsxT3E3IfUserArchiveStatsFEBE": dsxT3E3IfUserArchiveStatsFEBE,
       "dsxT3E3IfUserArchiveStatsEXZ": dsxT3E3IfUserArchiveStatsEXZ,
       "dsxT3E3IfUserArchiveStatsCOFA": dsxT3E3IfUserArchiveStatsCOFA,
       "dsxT3E3Traps": dsxT3E3Traps,
       "dsxT3E3AlarmOnTrap": dsxT3E3AlarmOnTrap,
       "dsxT3E3AlarmOffTrap": dsxT3E3AlarmOffTrap,
       "dsxT3E3TrapVariables": dsxT3E3TrapVariables,
       "dsxT3E3Number": dsxT3E3Number,
       "dsxT3E3AlarmType": dsxT3E3AlarmType}
)
