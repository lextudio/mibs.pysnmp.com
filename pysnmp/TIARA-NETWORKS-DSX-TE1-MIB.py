# SNMP MIB module (TIARA-NETWORKS-DSX-TE1-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TIARA-NETWORKS-DSX-TE1-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:01:38 2024
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

(dsxT1E1IfGroup,) = mibBuilder.importSymbols(
    "TIARA-NETWORKS-DSX-TC-MIB",
    "dsxT1E1IfGroup")


# MODULE-IDENTITY

dsxT1E1MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1)
)
dsxT1E1MIB.setRevisions(
        ("1999-04-23 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DsxT1E1IfConfigGroup_ObjectIdentity = ObjectIdentity
dsxT1E1IfConfigGroup = _DsxT1E1IfConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 1)
)
_DsxT1E1IfConfigLineTable_Object = MibTable
dsxT1E1IfConfigLineTable = _DsxT1E1IfConfigLineTable_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    dsxT1E1IfConfigLineTable.setStatus("current")
_DsxT1E1IfConfigLineEntry_Object = MibTableRow
dsxT1E1IfConfigLineEntry = _DsxT1E1IfConfigLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 1, 1, 1)
)
dsxT1E1IfConfigLineEntry.setIndexNames(
    (0, "TIARA-NETWORKS-DSX-TE1-MIB", "dsxT1E1IfIndex"),
)
if mibBuilder.loadTexts:
    dsxT1E1IfConfigLineEntry.setStatus("current")
_DsxT1E1IfIndex_Type = Integer32
_DsxT1E1IfIndex_Object = MibTableColumn
dsxT1E1IfIndex = _DsxT1E1IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 1, 1, 1, 1),
    _DsxT1E1IfIndex_Type()
)
dsxT1E1IfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dsxT1E1IfIndex.setStatus("current")
_DsxT1E1IfConfigServiceMode_Type = TruthValue
_DsxT1E1IfConfigServiceMode_Object = MibTableColumn
dsxT1E1IfConfigServiceMode = _DsxT1E1IfConfigServiceMode_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 1, 1, 1, 2),
    _DsxT1E1IfConfigServiceMode_Type()
)
dsxT1E1IfConfigServiceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsxT1E1IfConfigServiceMode.setStatus("current")


class _DsxT1E1IfConfigLineMode_Type(Integer32):
    """Custom type dsxT1E1IfConfigLineMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("linemode-csu", 1),
          ("linemode-dsx", 2))
    )


_DsxT1E1IfConfigLineMode_Type.__name__ = "Integer32"
_DsxT1E1IfConfigLineMode_Object = MibTableColumn
dsxT1E1IfConfigLineMode = _DsxT1E1IfConfigLineMode_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 1, 1, 1, 3),
    _DsxT1E1IfConfigLineMode_Type()
)
dsxT1E1IfConfigLineMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsxT1E1IfConfigLineMode.setStatus("current")


class _DsxT1E1IfConfigLineType_Type(Integer32):
    """Custom type dsxT1E1IfConfigLineType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("linetype-d4", 3),
          ("linetype-esf", 2))
    )


_DsxT1E1IfConfigLineType_Type.__name__ = "Integer32"
_DsxT1E1IfConfigLineType_Object = MibTableColumn
dsxT1E1IfConfigLineType = _DsxT1E1IfConfigLineType_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 1, 1, 1, 4),
    _DsxT1E1IfConfigLineType_Type()
)
dsxT1E1IfConfigLineType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsxT1E1IfConfigLineType.setStatus("current")


class _DsxT1E1IfConfigLineCode_Type(Integer32):
    """Custom type dsxT1E1IfConfigLineCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              5)
        )
    )
    namedValues = NamedValues(
        *(("linecode-ami", 5),
          ("linecode-b8zs", 2))
    )


_DsxT1E1IfConfigLineCode_Type.__name__ = "Integer32"
_DsxT1E1IfConfigLineCode_Object = MibTableColumn
dsxT1E1IfConfigLineCode = _DsxT1E1IfConfigLineCode_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 1, 1, 1, 5),
    _DsxT1E1IfConfigLineCode_Type()
)
dsxT1E1IfConfigLineCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsxT1E1IfConfigLineCode.setStatus("current")


class _DsxT1E1IfConfigLBO_Type(Integer32):
    """Custom type dsxT1E1IfConfigLBO based on Integer32"""
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
        *(("lbo-15-db", 3),
          ("lbo-225-db", 4),
          ("lbo-75-db", 2),
          ("lbo-zero-db", 1))
    )


_DsxT1E1IfConfigLBO_Type.__name__ = "Integer32"
_DsxT1E1IfConfigLBO_Object = MibTableColumn
dsxT1E1IfConfigLBO = _DsxT1E1IfConfigLBO_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 1, 1, 1, 6),
    _DsxT1E1IfConfigLBO_Type()
)
dsxT1E1IfConfigLBO.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsxT1E1IfConfigLBO.setStatus("current")


class _DsxT1E1IfConfigCableLength_Type(Integer32):
    """Custom type dsxT1E1IfConfigCableLength based on Integer32"""
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
        *(("cable-length-0-133", 1),
          ("cable-length-133-266", 2),
          ("cable-length-266-399", 3),
          ("cable-length-399-533", 4),
          ("cable-length-533-655", 5))
    )


_DsxT1E1IfConfigCableLength_Type.__name__ = "Integer32"
_DsxT1E1IfConfigCableLength_Object = MibTableColumn
dsxT1E1IfConfigCableLength = _DsxT1E1IfConfigCableLength_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 1, 1, 1, 7),
    _DsxT1E1IfConfigCableLength_Type()
)
dsxT1E1IfConfigCableLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsxT1E1IfConfigCableLength.setStatus("current")


class _DsxT1E1IfConfigRaiAlarm_Type(Integer32):
    """Custom type dsxT1E1IfConfigRaiAlarm based on Integer32"""
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
        *(("rai-det-enable", 2),
          ("rai-disable", 4),
          ("rai-gen-det-enable", 3),
          ("rai-gen-enable", 1))
    )


_DsxT1E1IfConfigRaiAlarm_Type.__name__ = "Integer32"
_DsxT1E1IfConfigRaiAlarm_Object = MibTableColumn
dsxT1E1IfConfigRaiAlarm = _DsxT1E1IfConfigRaiAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 1, 1, 1, 8),
    _DsxT1E1IfConfigRaiAlarm_Type()
)
dsxT1E1IfConfigRaiAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsxT1E1IfConfigRaiAlarm.setStatus("current")


class _DsxT1E1IfConfigTransmitClock_Type(Integer32):
    """Custom type dsxT1E1IfConfigTransmitClock based on Integer32"""
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


_DsxT1E1IfConfigTransmitClock_Type.__name__ = "Integer32"
_DsxT1E1IfConfigTransmitClock_Object = MibTableColumn
dsxT1E1IfConfigTransmitClock = _DsxT1E1IfConfigTransmitClock_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 1, 1, 1, 9),
    _DsxT1E1IfConfigTransmitClock_Type()
)
dsxT1E1IfConfigTransmitClock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsxT1E1IfConfigTransmitClock.setStatus("current")


class _DsxT1E1IfConfigTimeSlotMap_Type(OctetString):
    """Custom type dsxT1E1IfConfigTimeSlotMap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_DsxT1E1IfConfigTimeSlotMap_Type.__name__ = "OctetString"
_DsxT1E1IfConfigTimeSlotMap_Object = MibTableColumn
dsxT1E1IfConfigTimeSlotMap = _DsxT1E1IfConfigTimeSlotMap_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 1, 1, 1, 10),
    _DsxT1E1IfConfigTimeSlotMap_Type()
)
dsxT1E1IfConfigTimeSlotMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfConfigTimeSlotMap.setStatus("current")
_DsxT1E1IfCircuitId_Type = DisplayString
_DsxT1E1IfCircuitId_Object = MibTableColumn
dsxT1E1IfCircuitId = _DsxT1E1IfCircuitId_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 1, 1, 1, 11),
    _DsxT1E1IfCircuitId_Type()
)
dsxT1E1IfCircuitId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsxT1E1IfCircuitId.setStatus("current")
_DsxT1E1IfContactInfo_Type = DisplayString
_DsxT1E1IfContactInfo_Object = MibTableColumn
dsxT1E1IfContactInfo = _DsxT1E1IfContactInfo_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 1, 1, 1, 12),
    _DsxT1E1IfContactInfo_Type()
)
dsxT1E1IfContactInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsxT1E1IfContactInfo.setStatus("current")
_DsxT1E1IfDescription_Type = DisplayString
_DsxT1E1IfDescription_Object = MibTableColumn
dsxT1E1IfDescription = _DsxT1E1IfDescription_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 1, 1, 1, 13),
    _DsxT1E1IfDescription_Type()
)
dsxT1E1IfDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsxT1E1IfDescription.setStatus("current")
_DsxT1E1IfConfigFdlTable_Object = MibTable
dsxT1E1IfConfigFdlTable = _DsxT1E1IfConfigFdlTable_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 1, 2)
)
if mibBuilder.loadTexts:
    dsxT1E1IfConfigFdlTable.setStatus("current")
_DsxT1E1IfConfigFdlEntry_Object = MibTableRow
dsxT1E1IfConfigFdlEntry = _DsxT1E1IfConfigFdlEntry_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    dsxT1E1IfConfigFdlEntry.setStatus("current")


class _DsxT1E1IfConfigFdl_Type(Integer32):
    """Custom type dsxT1E1IfConfigFdl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fdl-ansi-att", 3),
          ("fdl-ansi-only", 1),
          ("fdl-att-only", 2))
    )


_DsxT1E1IfConfigFdl_Type.__name__ = "Integer32"
_DsxT1E1IfConfigFdl_Object = MibTableColumn
dsxT1E1IfConfigFdl = _DsxT1E1IfConfigFdl_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 1, 2, 1, 1),
    _DsxT1E1IfConfigFdl_Type()
)
dsxT1E1IfConfigFdl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsxT1E1IfConfigFdl.setStatus("current")


class _DsxT1E1IfConfigFdlCsuDsuType_Type(Integer32):
    """Custom type dsxT1E1IfConfigFdlCsuDsuType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fdl-csu", 1),
          ("fdl-csudsu", 3),
          ("fdl-dsu", 2))
    )


_DsxT1E1IfConfigFdlCsuDsuType_Type.__name__ = "Integer32"
_DsxT1E1IfConfigFdlCsuDsuType_Object = MibTableColumn
dsxT1E1IfConfigFdlCsuDsuType = _DsxT1E1IfConfigFdlCsuDsuType_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 1, 2, 1, 2),
    _DsxT1E1IfConfigFdlCsuDsuType_Type()
)
dsxT1E1IfConfigFdlCsuDsuType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsxT1E1IfConfigFdlCsuDsuType.setStatus("current")
_DsxT1E1IfAlarmConfigGroup_ObjectIdentity = ObjectIdentity
dsxT1E1IfAlarmConfigGroup = _DsxT1E1IfAlarmConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 1, 3)
)
_DsxT1E1IfAlarmThresholdConfigTable_Object = MibTable
dsxT1E1IfAlarmThresholdConfigTable = _DsxT1E1IfAlarmThresholdConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    dsxT1E1IfAlarmThresholdConfigTable.setStatus("current")
_DsxT1E1IfAlarmThresholdConfigEntry_Object = MibTableRow
dsxT1E1IfAlarmThresholdConfigEntry = _DsxT1E1IfAlarmThresholdConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 1, 3, 1, 1)
)
dsxT1E1IfAlarmThresholdConfigEntry.setIndexNames(
    (0, "TIARA-NETWORKS-DSX-TE1-MIB", "dsxT1E1IfIndex"),
    (0, "TIARA-NETWORKS-DSX-TE1-MIB", "dsxT1E1IfAlarmThresholdConfigIndex"),
)
if mibBuilder.loadTexts:
    dsxT1E1IfAlarmThresholdConfigEntry.setStatus("current")
_DsxT1E1IfAlarmThresholdConfigIndex_Type = Integer32
_DsxT1E1IfAlarmThresholdConfigIndex_Object = MibTableColumn
dsxT1E1IfAlarmThresholdConfigIndex = _DsxT1E1IfAlarmThresholdConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 1, 3, 1, 1, 1),
    _DsxT1E1IfAlarmThresholdConfigIndex_Type()
)
dsxT1E1IfAlarmThresholdConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dsxT1E1IfAlarmThresholdConfigIndex.setStatus("current")


class _DsxT1E1IfAlarmThresholdConfigObject_Type(Integer32):
    """Custom type dsxT1E1IfAlarmThresholdConfigObject based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("te1-object-bes", 4),
          ("te1-object-bpv", 8),
          ("te1-object-crc", 10),
          ("te1-object-css", 7),
          ("te1-object-eev", 1),
          ("te1-object-es", 2),
          ("te1-object-lofc", 6),
          ("te1-object-oof", 9),
          ("te1-object-ses", 5),
          ("te1-object-uas", 3))
    )


_DsxT1E1IfAlarmThresholdConfigObject_Type.__name__ = "Integer32"
_DsxT1E1IfAlarmThresholdConfigObject_Object = MibTableColumn
dsxT1E1IfAlarmThresholdConfigObject = _DsxT1E1IfAlarmThresholdConfigObject_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 1, 3, 1, 1, 2),
    _DsxT1E1IfAlarmThresholdConfigObject_Type()
)
dsxT1E1IfAlarmThresholdConfigObject.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsxT1E1IfAlarmThresholdConfigObject.setStatus("current")


class _DsxT1E1IfAlarmThresholdConfigSamplingInterval_Type(Integer32):
    """Custom type dsxT1E1IfAlarmThresholdConfigSamplingInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_DsxT1E1IfAlarmThresholdConfigSamplingInterval_Type.__name__ = "Integer32"
_DsxT1E1IfAlarmThresholdConfigSamplingInterval_Object = MibTableColumn
dsxT1E1IfAlarmThresholdConfigSamplingInterval = _DsxT1E1IfAlarmThresholdConfigSamplingInterval_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 1, 3, 1, 1, 3),
    _DsxT1E1IfAlarmThresholdConfigSamplingInterval_Type()
)
dsxT1E1IfAlarmThresholdConfigSamplingInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsxT1E1IfAlarmThresholdConfigSamplingInterval.setStatus("current")


class _DsxT1E1IfAlarmThresholdConfigSampleType_Type(Integer32):
    """Custom type dsxT1E1IfAlarmThresholdConfigSampleType based on Integer32"""
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


_DsxT1E1IfAlarmThresholdConfigSampleType_Type.__name__ = "Integer32"
_DsxT1E1IfAlarmThresholdConfigSampleType_Object = MibTableColumn
dsxT1E1IfAlarmThresholdConfigSampleType = _DsxT1E1IfAlarmThresholdConfigSampleType_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 1, 3, 1, 1, 4),
    _DsxT1E1IfAlarmThresholdConfigSampleType_Type()
)
dsxT1E1IfAlarmThresholdConfigSampleType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsxT1E1IfAlarmThresholdConfigSampleType.setStatus("current")
_DsxT1E1IfAlarmThresholdConfigStartupType_Type = TruthValue
_DsxT1E1IfAlarmThresholdConfigStartupType_Object = MibTableColumn
dsxT1E1IfAlarmThresholdConfigStartupType = _DsxT1E1IfAlarmThresholdConfigStartupType_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 1, 3, 1, 1, 5),
    _DsxT1E1IfAlarmThresholdConfigStartupType_Type()
)
dsxT1E1IfAlarmThresholdConfigStartupType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsxT1E1IfAlarmThresholdConfigStartupType.setStatus("current")
_DsxT1E1IfAlarmThresholdConfigRisingThreshold_Type = Integer32
_DsxT1E1IfAlarmThresholdConfigRisingThreshold_Object = MibTableColumn
dsxT1E1IfAlarmThresholdConfigRisingThreshold = _DsxT1E1IfAlarmThresholdConfigRisingThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 1, 3, 1, 1, 6),
    _DsxT1E1IfAlarmThresholdConfigRisingThreshold_Type()
)
dsxT1E1IfAlarmThresholdConfigRisingThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsxT1E1IfAlarmThresholdConfigRisingThreshold.setStatus("current")
_DsxT1E1IfAlarmThresholdConfigFallingThreshold_Type = Integer32
_DsxT1E1IfAlarmThresholdConfigFallingThreshold_Object = MibTableColumn
dsxT1E1IfAlarmThresholdConfigFallingThreshold = _DsxT1E1IfAlarmThresholdConfigFallingThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 1, 3, 1, 1, 7),
    _DsxT1E1IfAlarmThresholdConfigFallingThreshold_Type()
)
dsxT1E1IfAlarmThresholdConfigFallingThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsxT1E1IfAlarmThresholdConfigFallingThreshold.setStatus("current")
_DsxT1E1IfTestConfigTable_Object = MibTable
dsxT1E1IfTestConfigTable = _DsxT1E1IfTestConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 1, 4)
)
if mibBuilder.loadTexts:
    dsxT1E1IfTestConfigTable.setStatus("current")
_DsxT1E1IfTestConfigEntry_Object = MibTableRow
dsxT1E1IfTestConfigEntry = _DsxT1E1IfTestConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    dsxT1E1IfTestConfigEntry.setStatus("current")


class _DsxT1E1IfTestConfigType_Type(Integer32):
    """Custom type dsxT1E1IfTestConfigType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("line-loopback-test", 3),
          ("no-test", 1),
          ("pattern-test", 6),
          ("payload-loopback-test", 2),
          ("remote-lpdn-test", 8),
          ("remote-lpup-test", 7))
    )


_DsxT1E1IfTestConfigType_Type.__name__ = "Integer32"
_DsxT1E1IfTestConfigType_Object = MibTableColumn
dsxT1E1IfTestConfigType = _DsxT1E1IfTestConfigType_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 1, 4, 1, 1),
    _DsxT1E1IfTestConfigType_Type()
)
dsxT1E1IfTestConfigType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsxT1E1IfTestConfigType.setStatus("current")
_DsxT1E1IfTestConfigTime_Type = Unsigned32
_DsxT1E1IfTestConfigTime_Object = MibTableColumn
dsxT1E1IfTestConfigTime = _DsxT1E1IfTestConfigTime_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 1, 4, 1, 2),
    _DsxT1E1IfTestConfigTime_Type()
)
dsxT1E1IfTestConfigTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsxT1E1IfTestConfigTime.setStatus("current")


class _DsxT1E1IfTestConfigPattern_Type(Integer32):
    """Custom type dsxT1E1IfTestConfigPattern based on Integer32"""
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
        *(("pattern-215minus1", 13),
          ("pattern-223minus1", 16),
          ("pattern-all-ones", 1),
          ("pattern-all-zeros", 2),
          ("pattern-qrw", 15),
          ("reserved1", 3),
          ("reserved10", 11),
          ("reserved11", 12),
          ("reserved12", 14),
          ("reserved2", 4),
          ("reserved3", 5),
          ("reserved4", 6),
          ("reserved5", 7),
          ("reserved6", 8),
          ("reserved7", 9),
          ("reserved9", 10))
    )


_DsxT1E1IfTestConfigPattern_Type.__name__ = "Integer32"
_DsxT1E1IfTestConfigPattern_Object = MibTableColumn
dsxT1E1IfTestConfigPattern = _DsxT1E1IfTestConfigPattern_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 1, 4, 1, 3),
    _DsxT1E1IfTestConfigPattern_Type()
)
dsxT1E1IfTestConfigPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsxT1E1IfTestConfigPattern.setStatus("current")


class _DsxT1E1IfTestConfigLoopCode_Type(Integer32):
    """Custom type dsxT1E1IfTestConfigLoopCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("loopcode-line-ATTFDL", 4),
          ("loopcode-line-alternate", 3),
          ("loopcode-line-standard", 2),
          ("loopcode-none", 1),
          ("loopcode-payload-ATTFDL", 6),
          ("loopcode-payload-ansiFDL", 7))
    )


_DsxT1E1IfTestConfigLoopCode_Type.__name__ = "Integer32"
_DsxT1E1IfTestConfigLoopCode_Object = MibTableColumn
dsxT1E1IfTestConfigLoopCode = _DsxT1E1IfTestConfigLoopCode_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 1, 4, 1, 4),
    _DsxT1E1IfTestConfigLoopCode_Type()
)
dsxT1E1IfTestConfigLoopCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsxT1E1IfTestConfigLoopCode.setStatus("current")
_DsxT1E1IfStatusGroup_ObjectIdentity = ObjectIdentity
dsxT1E1IfStatusGroup = _DsxT1E1IfStatusGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 2)
)
_DsxT1E1IfStatusTable_Object = MibTable
dsxT1E1IfStatusTable = _DsxT1E1IfStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    dsxT1E1IfStatusTable.setStatus("current")
_DsxT1E1IfStatusEntry_Object = MibTableRow
dsxT1E1IfStatusEntry = _DsxT1E1IfStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    dsxT1E1IfStatusEntry.setStatus("current")


class _DsxT1E1IfStatusLineStatus_Type(Bits):
    """Custom type dsxT1E1IfStatusLineStatus based on Bits"""
    namedValues = NamedValues(
        *(("loopbackStatus", 24),
          ("lorcStatus", 10),
          ("raisStatus", 28),
          ("rcvTestCode", 20),
          ("reserved1", 0),
          ("reserved10", 22),
          ("reserved11", 23),
          ("reserved12", 25),
          ("reserved13", 26),
          ("reserved14", 29),
          ("reserved15", 31),
          ("reserved2", 1),
          ("reserved3", 7),
          ("reserved4", 8),
          ("reserved5", 9),
          ("reserved6", 12),
          ("reserved7", 13),
          ("reserved8", 19),
          ("reserved9", 21),
          ("rexzStatus", 6),
          ("risStatus", 5),
          ("rlofStatus", 30),
          ("rlosStatus", 4),
          ("rraiStatus", 2),
          ("sendLineCode", 14),
          ("sendPattern", 18),
          ("sendPayLoadCode", 15),
          ("sendResetCode", 16),
          ("sendTE1Code", 17),
          ("taisStatus", 27),
          ("tpdeStatus", 11),
          ("traiStatus", 3))
    )

_DsxT1E1IfStatusLineStatus_Type.__name__ = "Bits"
_DsxT1E1IfStatusLineStatus_Object = MibTableColumn
dsxT1E1IfStatusLineStatus = _DsxT1E1IfStatusLineStatus_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 2, 1, 1, 1),
    _DsxT1E1IfStatusLineStatus_Type()
)
dsxT1E1IfStatusLineStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfStatusLineStatus.setStatus("current")


class _DsxT1E1IfStatusTransmitClock_Type(Integer32):
    """Custom type dsxT1E1IfStatusTransmitClock based on Integer32"""
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


_DsxT1E1IfStatusTransmitClock_Type.__name__ = "Integer32"
_DsxT1E1IfStatusTransmitClock_Object = MibTableColumn
dsxT1E1IfStatusTransmitClock = _DsxT1E1IfStatusTransmitClock_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 2, 1, 1, 2),
    _DsxT1E1IfStatusTransmitClock_Type()
)
dsxT1E1IfStatusTransmitClock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfStatusTransmitClock.setStatus("current")
_DsxT1E1IfAlarmStatusTable_Object = MibTable
dsxT1E1IfAlarmStatusTable = _DsxT1E1IfAlarmStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 2, 2)
)
if mibBuilder.loadTexts:
    dsxT1E1IfAlarmStatusTable.setStatus("current")
_DsxT1E1IfAlarmStatusEntry_Object = MibTableRow
dsxT1E1IfAlarmStatusEntry = _DsxT1E1IfAlarmStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    dsxT1E1IfAlarmStatusEntry.setStatus("current")


class _DsxT1E1IfAlarmStatusAlarmStatus_Type(Bits):
    """Custom type dsxT1E1IfAlarmStatusAlarmStatus based on Bits"""
    namedValues = NamedValues(
        *(("ibTestAlarm", 16),
          ("loopbackStateAlarm", 6),
          ("lorcAlarm", 13),
          ("raisAlarm", 2),
          ("rcpeAlarm", 12),
          ("rcvTestCode", 7),
          ("rexzAlarm", 9),
          ("rfebeAlarm", 10),
          ("risAlarm", 8),
          ("rlofAlarm", 4),
          ("rlosAlarm", 5),
          ("rpeAlarm", 11),
          ("rraiAlarm", 0),
          ("taisAlarm", 3),
          ("tfebeAlarm", 15),
          ("tpdeAlarm", 14),
          ("traiAlarm", 1))
    )

_DsxT1E1IfAlarmStatusAlarmStatus_Type.__name__ = "Bits"
_DsxT1E1IfAlarmStatusAlarmStatus_Object = MibTableColumn
dsxT1E1IfAlarmStatusAlarmStatus = _DsxT1E1IfAlarmStatusAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 2, 2, 1, 1),
    _DsxT1E1IfAlarmStatusAlarmStatus_Type()
)
dsxT1E1IfAlarmStatusAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfAlarmStatusAlarmStatus.setStatus("current")


class _DsxT1E1IfAlarmStatusThresholdStatus_Type(Bits):
    """Custom type dsxT1E1IfAlarmStatusThresholdStatus based on Bits"""
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

_DsxT1E1IfAlarmStatusThresholdStatus_Type.__name__ = "Bits"
_DsxT1E1IfAlarmStatusThresholdStatus_Object = MibTableColumn
dsxT1E1IfAlarmStatusThresholdStatus = _DsxT1E1IfAlarmStatusThresholdStatus_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 2, 2, 1, 2),
    _DsxT1E1IfAlarmStatusThresholdStatus_Type()
)
dsxT1E1IfAlarmStatusThresholdStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfAlarmStatusThresholdStatus.setStatus("current")
_DsxT1E1IfTestStatusTable_Object = MibTable
dsxT1E1IfTestStatusTable = _DsxT1E1IfTestStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 2, 3)
)
if mibBuilder.loadTexts:
    dsxT1E1IfTestStatusTable.setStatus("current")
_DsxT1E1IfTestStatusEntry_Object = MibTableRow
dsxT1E1IfTestStatusEntry = _DsxT1E1IfTestStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 2, 3, 1)
)
if mibBuilder.loadTexts:
    dsxT1E1IfTestStatusEntry.setStatus("current")


class _DsxT1E1IfTestStatusTestType_Type(Integer32):
    """Custom type dsxT1E1IfTestStatusTestType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("testtype-line-loopback", 3),
          ("testtype-notest", 1),
          ("testtype-pattern", 6),
          ("testtype-payload-loopback", 2),
          ("testtype-remote-lpdn", 8),
          ("testtype-remote-lpup", 7))
    )


_DsxT1E1IfTestStatusTestType_Type.__name__ = "Integer32"
_DsxT1E1IfTestStatusTestType_Object = MibTableColumn
dsxT1E1IfTestStatusTestType = _DsxT1E1IfTestStatusTestType_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 2, 3, 1, 1),
    _DsxT1E1IfTestStatusTestType_Type()
)
dsxT1E1IfTestStatusTestType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfTestStatusTestType.setStatus("current")
_DsxT1E1IfTestStatusTestTime_Type = Unsigned32
_DsxT1E1IfTestStatusTestTime_Object = MibTableColumn
dsxT1E1IfTestStatusTestTime = _DsxT1E1IfTestStatusTestTime_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 2, 3, 1, 2),
    _DsxT1E1IfTestStatusTestTime_Type()
)
dsxT1E1IfTestStatusTestTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfTestStatusTestTime.setStatus("current")


class _DsxT1E1IfTestStatusTestState_Type(Integer32):
    """Custom type dsxT1E1IfTestStatusTestState based on Integer32"""
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
        *(("test-state-failed", 7),
          ("test-state-idle", 1),
          ("test-state-inprogress", 5),
          ("test-state-locked", 3),
          ("test-state-passed", 6),
          ("test-state-relocked", 4),
          ("test-state-searching", 2))
    )


_DsxT1E1IfTestStatusTestState_Type.__name__ = "Integer32"
_DsxT1E1IfTestStatusTestState_Object = MibTableColumn
dsxT1E1IfTestStatusTestState = _DsxT1E1IfTestStatusTestState_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 2, 3, 1, 3),
    _DsxT1E1IfTestStatusTestState_Type()
)
dsxT1E1IfTestStatusTestState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfTestStatusTestState.setStatus("current")


class _DsxT1E1IfTestStatusTestPattern_Type(Integer32):
    """Custom type dsxT1E1IfTestStatusTestPattern based on Integer32"""
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
        *(("pattern-1in3", 5),
          ("pattern-1in5", 6),
          ("pattern-1in7", 7),
          ("pattern-215minus1", 13),
          ("pattern-220minus1", 14),
          ("pattern-223minus1", 16),
          ("pattern-29minus1", 12),
          ("pattern-3in24", 4),
          ("pattern-all-ones", 1),
          ("pattern-all-zeros", 2),
          ("pattern-alternating", 3),
          ("pattern-qrss", 15),
          ("pattern-smartjack-lpdown", 9),
          ("pattern-smartjack-lpup", 8),
          ("pattern-user1", 10),
          ("pattern-user2", 11))
    )


_DsxT1E1IfTestStatusTestPattern_Type.__name__ = "Integer32"
_DsxT1E1IfTestStatusTestPattern_Object = MibTableColumn
dsxT1E1IfTestStatusTestPattern = _DsxT1E1IfTestStatusTestPattern_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 2, 3, 1, 4),
    _DsxT1E1IfTestStatusTestPattern_Type()
)
dsxT1E1IfTestStatusTestPattern.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfTestStatusTestPattern.setStatus("current")
_DsxT1E1IfTestStatusLockedSeconds_Type = Unsigned32
_DsxT1E1IfTestStatusLockedSeconds_Object = MibTableColumn
dsxT1E1IfTestStatusLockedSeconds = _DsxT1E1IfTestStatusLockedSeconds_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 2, 3, 1, 5),
    _DsxT1E1IfTestStatusLockedSeconds_Type()
)
dsxT1E1IfTestStatusLockedSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfTestStatusLockedSeconds.setStatus("current")
_DsxT1E1IfTestStatusSyncLossCount_Type = Unsigned32
_DsxT1E1IfTestStatusSyncLossCount_Object = MibTableColumn
dsxT1E1IfTestStatusSyncLossCount = _DsxT1E1IfTestStatusSyncLossCount_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 2, 3, 1, 6),
    _DsxT1E1IfTestStatusSyncLossCount_Type()
)
dsxT1E1IfTestStatusSyncLossCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfTestStatusSyncLossCount.setStatus("current")
_DsxT1E1IfTestStatusErrorCount_Type = Unsigned32
_DsxT1E1IfTestStatusErrorCount_Object = MibTableColumn
dsxT1E1IfTestStatusErrorCount = _DsxT1E1IfTestStatusErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 2, 3, 1, 7),
    _DsxT1E1IfTestStatusErrorCount_Type()
)
dsxT1E1IfTestStatusErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfTestStatusErrorCount.setStatus("current")


class _DsxT1E1IfTestStatusLoopCode_Type(Integer32):
    """Custom type dsxT1E1IfTestStatusLoopCode based on Integer32"""
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
        *(("loopcode-line-ATTFDL", 4),
          ("loopcode-line-alternate", 3),
          ("loopcode-line-standard", 2),
          ("loopcode-none", 1),
          ("loopcode-payload-ATTFDL", 5),
          ("loopcode-payload-ansiFDL", 6),
          ("loopcode-v54", 7))
    )


_DsxT1E1IfTestStatusLoopCode_Type.__name__ = "Integer32"
_DsxT1E1IfTestStatusLoopCode_Object = MibTableColumn
dsxT1E1IfTestStatusLoopCode = _DsxT1E1IfTestStatusLoopCode_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 2, 3, 1, 8),
    _DsxT1E1IfTestStatusLoopCode_Type()
)
dsxT1E1IfTestStatusLoopCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfTestStatusLoopCode.setStatus("current")
_DsxT1E1IfLastTestResultTable_Object = MibTable
dsxT1E1IfLastTestResultTable = _DsxT1E1IfLastTestResultTable_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 2, 4)
)
if mibBuilder.loadTexts:
    dsxT1E1IfLastTestResultTable.setStatus("current")
_DsxT1E1IfLastTestResultEntry_Object = MibTableRow
dsxT1E1IfLastTestResultEntry = _DsxT1E1IfLastTestResultEntry_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 2, 4, 1)
)
if mibBuilder.loadTexts:
    dsxT1E1IfLastTestResultEntry.setStatus("current")


class _DsxT1E1IfLastTestResultTestType_Type(Integer32):
    """Custom type dsxT1E1IfLastTestResultTestType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("testtype-line-loopback", 3),
          ("testtype-notest", 1),
          ("testtype-pattern", 6),
          ("testtype-payload-loopback", 2),
          ("testtype-remote-lpdn", 8),
          ("testtype-remote-lpup", 7))
    )


_DsxT1E1IfLastTestResultTestType_Type.__name__ = "Integer32"
_DsxT1E1IfLastTestResultTestType_Object = MibTableColumn
dsxT1E1IfLastTestResultTestType = _DsxT1E1IfLastTestResultTestType_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 2, 4, 1, 1),
    _DsxT1E1IfLastTestResultTestType_Type()
)
dsxT1E1IfLastTestResultTestType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfLastTestResultTestType.setStatus("current")
_DsxT1E1IfLastTestResultTestTime_Type = Unsigned32
_DsxT1E1IfLastTestResultTestTime_Object = MibTableColumn
dsxT1E1IfLastTestResultTestTime = _DsxT1E1IfLastTestResultTestTime_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 2, 4, 1, 2),
    _DsxT1E1IfLastTestResultTestTime_Type()
)
dsxT1E1IfLastTestResultTestTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfLastTestResultTestTime.setStatus("current")


class _DsxT1E1IfLastTestResultTestState_Type(Integer32):
    """Custom type dsxT1E1IfLastTestResultTestState based on Integer32"""
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
        *(("test-state-failed", 7),
          ("test-state-idle", 1),
          ("test-state-inprogress", 5),
          ("test-state-locked", 3),
          ("test-state-passed", 6),
          ("test-state-relocked", 4),
          ("test-state-searching", 2))
    )


_DsxT1E1IfLastTestResultTestState_Type.__name__ = "Integer32"
_DsxT1E1IfLastTestResultTestState_Object = MibTableColumn
dsxT1E1IfLastTestResultTestState = _DsxT1E1IfLastTestResultTestState_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 2, 4, 1, 3),
    _DsxT1E1IfLastTestResultTestState_Type()
)
dsxT1E1IfLastTestResultTestState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfLastTestResultTestState.setStatus("current")


class _DsxT1E1IfLastTestResultTestPattern_Type(Integer32):
    """Custom type dsxT1E1IfLastTestResultTestPattern based on Integer32"""
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
        *(("pattern-1in3", 5),
          ("pattern-1in5", 6),
          ("pattern-1in7", 7),
          ("pattern-215minus1", 13),
          ("pattern-220minus1", 14),
          ("pattern-223minus1", 16),
          ("pattern-29minus1", 12),
          ("pattern-3in24", 4),
          ("pattern-all-ones", 1),
          ("pattern-all-zeros", 2),
          ("pattern-alternating", 3),
          ("pattern-qrss", 15),
          ("pattern-smartjack-lpdown", 9),
          ("pattern-smartjack-lpup", 8),
          ("pattern-user1", 10),
          ("pattern-user2", 11))
    )


_DsxT1E1IfLastTestResultTestPattern_Type.__name__ = "Integer32"
_DsxT1E1IfLastTestResultTestPattern_Object = MibTableColumn
dsxT1E1IfLastTestResultTestPattern = _DsxT1E1IfLastTestResultTestPattern_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 2, 4, 1, 4),
    _DsxT1E1IfLastTestResultTestPattern_Type()
)
dsxT1E1IfLastTestResultTestPattern.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfLastTestResultTestPattern.setStatus("current")
_DsxT1E1IfLastTestResultLockedSeconds_Type = Unsigned32
_DsxT1E1IfLastTestResultLockedSeconds_Object = MibTableColumn
dsxT1E1IfLastTestResultLockedSeconds = _DsxT1E1IfLastTestResultLockedSeconds_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 2, 4, 1, 5),
    _DsxT1E1IfLastTestResultLockedSeconds_Type()
)
dsxT1E1IfLastTestResultLockedSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfLastTestResultLockedSeconds.setStatus("current")
_DsxT1E1IfLastTestResultSyncLossCount_Type = Unsigned32
_DsxT1E1IfLastTestResultSyncLossCount_Object = MibTableColumn
dsxT1E1IfLastTestResultSyncLossCount = _DsxT1E1IfLastTestResultSyncLossCount_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 2, 4, 1, 6),
    _DsxT1E1IfLastTestResultSyncLossCount_Type()
)
dsxT1E1IfLastTestResultSyncLossCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfLastTestResultSyncLossCount.setStatus("current")
_DsxT1E1IfLastTestResultErrorCount_Type = Unsigned32
_DsxT1E1IfLastTestResultErrorCount_Object = MibTableColumn
dsxT1E1IfLastTestResultErrorCount = _DsxT1E1IfLastTestResultErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 2, 4, 1, 7),
    _DsxT1E1IfLastTestResultErrorCount_Type()
)
dsxT1E1IfLastTestResultErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfLastTestResultErrorCount.setStatus("current")


class _DsxT1E1IfLastTestResultLoopCode_Type(Integer32):
    """Custom type dsxT1E1IfLastTestResultLoopCode based on Integer32"""
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
        *(("loopcode-line-ATTFDL", 4),
          ("loopcode-line-alternate", 3),
          ("loopcode-line-standard", 2),
          ("loopcode-none", 1),
          ("loopcode-payload-ATTFDL", 5),
          ("loopcode-payload-ansiFDL", 6),
          ("loopcode-v54", 7))
    )


_DsxT1E1IfLastTestResultLoopCode_Type.__name__ = "Integer32"
_DsxT1E1IfLastTestResultLoopCode_Object = MibTableColumn
dsxT1E1IfLastTestResultLoopCode = _DsxT1E1IfLastTestResultLoopCode_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 2, 4, 1, 8),
    _DsxT1E1IfLastTestResultLoopCode_Type()
)
dsxT1E1IfLastTestResultLoopCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfLastTestResultLoopCode.setStatus("current")
_DsxT1E1IfStatsGroup_ObjectIdentity = ObjectIdentity
dsxT1E1IfStatsGroup = _DsxT1E1IfStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3)
)
_DsxT1E1IfArchiveStatsValidIntervalsTable_Object = MibTable
dsxT1E1IfArchiveStatsValidIntervalsTable = _DsxT1E1IfArchiveStatsValidIntervalsTable_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 1)
)
if mibBuilder.loadTexts:
    dsxT1E1IfArchiveStatsValidIntervalsTable.setStatus("current")
_DsxT1E1IfArchiveStatsValidIntervalsEntry_Object = MibTableRow
dsxT1E1IfArchiveStatsValidIntervalsEntry = _DsxT1E1IfArchiveStatsValidIntervalsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    dsxT1E1IfArchiveStatsValidIntervalsEntry.setStatus("current")
_DsxT1E1IfAnsiArchiveStatsValidIntervals_Type = Unsigned32
_DsxT1E1IfAnsiArchiveStatsValidIntervals_Object = MibTableColumn
dsxT1E1IfAnsiArchiveStatsValidIntervals = _DsxT1E1IfAnsiArchiveStatsValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 1, 1, 1),
    _DsxT1E1IfAnsiArchiveStatsValidIntervals_Type()
)
dsxT1E1IfAnsiArchiveStatsValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfAnsiArchiveStatsValidIntervals.setStatus("current")
_DsxT1E1IfAttArchiveStatsValidIntervals_Type = Unsigned32
_DsxT1E1IfAttArchiveStatsValidIntervals_Object = MibTableColumn
dsxT1E1IfAttArchiveStatsValidIntervals = _DsxT1E1IfAttArchiveStatsValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 1, 1, 2),
    _DsxT1E1IfAttArchiveStatsValidIntervals_Type()
)
dsxT1E1IfAttArchiveStatsValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfAttArchiveStatsValidIntervals.setStatus("current")
_DsxT1E1IfIetfArchiveStatsValidIntervals_Type = Unsigned32
_DsxT1E1IfIetfArchiveStatsValidIntervals_Object = MibTableColumn
dsxT1E1IfIetfArchiveStatsValidIntervals = _DsxT1E1IfIetfArchiveStatsValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 1, 1, 3),
    _DsxT1E1IfIetfArchiveStatsValidIntervals_Type()
)
dsxT1E1IfIetfArchiveStatsValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfIetfArchiveStatsValidIntervals.setStatus("current")
_DsxT1E1IfUserTotalStatsValidDays_Type = Unsigned32
_DsxT1E1IfUserTotalStatsValidDays_Object = MibTableColumn
dsxT1E1IfUserTotalStatsValidDays = _DsxT1E1IfUserTotalStatsValidDays_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 1, 1, 4),
    _DsxT1E1IfUserTotalStatsValidDays_Type()
)
dsxT1E1IfUserTotalStatsValidDays.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfUserTotalStatsValidDays.setStatus("current")
_DsxT1E1IfUserArchiveStatsValidIntervals_Type = Integer32
_DsxT1E1IfUserArchiveStatsValidIntervals_Object = MibTableColumn
dsxT1E1IfUserArchiveStatsValidIntervals = _DsxT1E1IfUserArchiveStatsValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 1, 1, 5),
    _DsxT1E1IfUserArchiveStatsValidIntervals_Type()
)
dsxT1E1IfUserArchiveStatsValidIntervals.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsxT1E1IfUserArchiveStatsValidIntervals.setStatus("current")
_DsxT1E1IfAnsiStatsGroup_ObjectIdentity = ObjectIdentity
dsxT1E1IfAnsiStatsGroup = _DsxT1E1IfAnsiStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 2)
)
_DsxT1E1IfAnsiCurrentStatsTable_Object = MibTable
dsxT1E1IfAnsiCurrentStatsTable = _DsxT1E1IfAnsiCurrentStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 2, 1)
)
if mibBuilder.loadTexts:
    dsxT1E1IfAnsiCurrentStatsTable.setStatus("current")
_DsxT1E1IfAnsiCurrentStatsEntry_Object = MibTableRow
dsxT1E1IfAnsiCurrentStatsEntry = _DsxT1E1IfAnsiCurrentStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 2, 1, 1)
)
if mibBuilder.loadTexts:
    dsxT1E1IfAnsiCurrentStatsEntry.setStatus("current")
_DsxT1E1IfAnsiCurrentStatsUASState_Type = TruthValue
_DsxT1E1IfAnsiCurrentStatsUASState_Object = MibTableColumn
dsxT1E1IfAnsiCurrentStatsUASState = _DsxT1E1IfAnsiCurrentStatsUASState_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 2, 1, 1, 1),
    _DsxT1E1IfAnsiCurrentStatsUASState_Type()
)
dsxT1E1IfAnsiCurrentStatsUASState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfAnsiCurrentStatsUASState.setStatus("current")
_DsxT1E1IfAnsiCurrentStatsTimeInCurrent_Type = Unsigned32
_DsxT1E1IfAnsiCurrentStatsTimeInCurrent_Object = MibTableColumn
dsxT1E1IfAnsiCurrentStatsTimeInCurrent = _DsxT1E1IfAnsiCurrentStatsTimeInCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 2, 1, 1, 2),
    _DsxT1E1IfAnsiCurrentStatsTimeInCurrent_Type()
)
dsxT1E1IfAnsiCurrentStatsTimeInCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfAnsiCurrentStatsTimeInCurrent.setStatus("current")
_DsxT1E1IfAnsiCurrentPathStatsCV_Type = Unsigned32
_DsxT1E1IfAnsiCurrentPathStatsCV_Object = MibTableColumn
dsxT1E1IfAnsiCurrentPathStatsCV = _DsxT1E1IfAnsiCurrentPathStatsCV_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 2, 1, 1, 3),
    _DsxT1E1IfAnsiCurrentPathStatsCV_Type()
)
dsxT1E1IfAnsiCurrentPathStatsCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfAnsiCurrentPathStatsCV.setStatus("current")
_DsxT1E1IfAnsiCurrentPathStatsES_Type = Unsigned32
_DsxT1E1IfAnsiCurrentPathStatsES_Object = MibTableColumn
dsxT1E1IfAnsiCurrentPathStatsES = _DsxT1E1IfAnsiCurrentPathStatsES_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 2, 1, 1, 4),
    _DsxT1E1IfAnsiCurrentPathStatsES_Type()
)
dsxT1E1IfAnsiCurrentPathStatsES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfAnsiCurrentPathStatsES.setStatus("current")
_DsxT1E1IfAnsiCurrentPathStatsSES_Type = Unsigned32
_DsxT1E1IfAnsiCurrentPathStatsSES_Object = MibTableColumn
dsxT1E1IfAnsiCurrentPathStatsSES = _DsxT1E1IfAnsiCurrentPathStatsSES_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 2, 1, 1, 5),
    _DsxT1E1IfAnsiCurrentPathStatsSES_Type()
)
dsxT1E1IfAnsiCurrentPathStatsSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfAnsiCurrentPathStatsSES.setStatus("current")
_DsxT1E1IfAnsiCurrentPathStatsSAS_Type = Unsigned32
_DsxT1E1IfAnsiCurrentPathStatsSAS_Object = MibTableColumn
dsxT1E1IfAnsiCurrentPathStatsSAS = _DsxT1E1IfAnsiCurrentPathStatsSAS_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 2, 1, 1, 6),
    _DsxT1E1IfAnsiCurrentPathStatsSAS_Type()
)
dsxT1E1IfAnsiCurrentPathStatsSAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfAnsiCurrentPathStatsSAS.setStatus("current")
_DsxT1E1IfAnsiCurrentPathStatsCSS_Type = Unsigned32
_DsxT1E1IfAnsiCurrentPathStatsCSS_Object = MibTableColumn
dsxT1E1IfAnsiCurrentPathStatsCSS = _DsxT1E1IfAnsiCurrentPathStatsCSS_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 2, 1, 1, 7),
    _DsxT1E1IfAnsiCurrentPathStatsCSS_Type()
)
dsxT1E1IfAnsiCurrentPathStatsCSS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfAnsiCurrentPathStatsCSS.setStatus("current")
_DsxT1E1IfAnsiCurrentPathStatsUAS_Type = Unsigned32
_DsxT1E1IfAnsiCurrentPathStatsUAS_Object = MibTableColumn
dsxT1E1IfAnsiCurrentPathStatsUAS = _DsxT1E1IfAnsiCurrentPathStatsUAS_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 2, 1, 1, 8),
    _DsxT1E1IfAnsiCurrentPathStatsUAS_Type()
)
dsxT1E1IfAnsiCurrentPathStatsUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfAnsiCurrentPathStatsUAS.setStatus("current")
_DsxT1E1IfAnsiCurrentLineStatsCV_Type = Unsigned32
_DsxT1E1IfAnsiCurrentLineStatsCV_Object = MibTableColumn
dsxT1E1IfAnsiCurrentLineStatsCV = _DsxT1E1IfAnsiCurrentLineStatsCV_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 2, 1, 1, 9),
    _DsxT1E1IfAnsiCurrentLineStatsCV_Type()
)
dsxT1E1IfAnsiCurrentLineStatsCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfAnsiCurrentLineStatsCV.setStatus("current")
_DsxT1E1IfAnsiCurrentLineStatsES_Type = Unsigned32
_DsxT1E1IfAnsiCurrentLineStatsES_Object = MibTableColumn
dsxT1E1IfAnsiCurrentLineStatsES = _DsxT1E1IfAnsiCurrentLineStatsES_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 2, 1, 1, 10),
    _DsxT1E1IfAnsiCurrentLineStatsES_Type()
)
dsxT1E1IfAnsiCurrentLineStatsES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfAnsiCurrentLineStatsES.setStatus("current")
_DsxT1E1IfAnsiCurrentLineStatsSES_Type = Unsigned32
_DsxT1E1IfAnsiCurrentLineStatsSES_Object = MibTableColumn
dsxT1E1IfAnsiCurrentLineStatsSES = _DsxT1E1IfAnsiCurrentLineStatsSES_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 2, 1, 1, 11),
    _DsxT1E1IfAnsiCurrentLineStatsSES_Type()
)
dsxT1E1IfAnsiCurrentLineStatsSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfAnsiCurrentLineStatsSES.setStatus("current")
_DsxT1E1IfAnsiTotalStatsTable_Object = MibTable
dsxT1E1IfAnsiTotalStatsTable = _DsxT1E1IfAnsiTotalStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 2, 2)
)
if mibBuilder.loadTexts:
    dsxT1E1IfAnsiTotalStatsTable.setStatus("current")
_DsxT1E1IfAnsiTotalStatsEntry_Object = MibTableRow
dsxT1E1IfAnsiTotalStatsEntry = _DsxT1E1IfAnsiTotalStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 2, 2, 1)
)
if mibBuilder.loadTexts:
    dsxT1E1IfAnsiTotalStatsEntry.setStatus("current")
_DsxT1E1IfAnsiTotalPathStatsCV_Type = Unsigned32
_DsxT1E1IfAnsiTotalPathStatsCV_Object = MibTableColumn
dsxT1E1IfAnsiTotalPathStatsCV = _DsxT1E1IfAnsiTotalPathStatsCV_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 2, 2, 1, 1),
    _DsxT1E1IfAnsiTotalPathStatsCV_Type()
)
dsxT1E1IfAnsiTotalPathStatsCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfAnsiTotalPathStatsCV.setStatus("current")
_DsxT1E1IfAnsiTotalPathStatsES_Type = Unsigned32
_DsxT1E1IfAnsiTotalPathStatsES_Object = MibTableColumn
dsxT1E1IfAnsiTotalPathStatsES = _DsxT1E1IfAnsiTotalPathStatsES_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 2, 2, 1, 2),
    _DsxT1E1IfAnsiTotalPathStatsES_Type()
)
dsxT1E1IfAnsiTotalPathStatsES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfAnsiTotalPathStatsES.setStatus("current")
_DsxT1E1IfAnsiTotalPathStatsSES_Type = Unsigned32
_DsxT1E1IfAnsiTotalPathStatsSES_Object = MibTableColumn
dsxT1E1IfAnsiTotalPathStatsSES = _DsxT1E1IfAnsiTotalPathStatsSES_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 2, 2, 1, 3),
    _DsxT1E1IfAnsiTotalPathStatsSES_Type()
)
dsxT1E1IfAnsiTotalPathStatsSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfAnsiTotalPathStatsSES.setStatus("current")
_DsxT1E1IfAnsiTotalPathStatsSAS_Type = Unsigned32
_DsxT1E1IfAnsiTotalPathStatsSAS_Object = MibTableColumn
dsxT1E1IfAnsiTotalPathStatsSAS = _DsxT1E1IfAnsiTotalPathStatsSAS_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 2, 2, 1, 4),
    _DsxT1E1IfAnsiTotalPathStatsSAS_Type()
)
dsxT1E1IfAnsiTotalPathStatsSAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfAnsiTotalPathStatsSAS.setStatus("current")
_DsxT1E1IfAnsiTotalPathStatsCSS_Type = Unsigned32
_DsxT1E1IfAnsiTotalPathStatsCSS_Object = MibTableColumn
dsxT1E1IfAnsiTotalPathStatsCSS = _DsxT1E1IfAnsiTotalPathStatsCSS_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 2, 2, 1, 5),
    _DsxT1E1IfAnsiTotalPathStatsCSS_Type()
)
dsxT1E1IfAnsiTotalPathStatsCSS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfAnsiTotalPathStatsCSS.setStatus("current")
_DsxT1E1IfAnsiTotalPathStatsUAS_Type = Unsigned32
_DsxT1E1IfAnsiTotalPathStatsUAS_Object = MibTableColumn
dsxT1E1IfAnsiTotalPathStatsUAS = _DsxT1E1IfAnsiTotalPathStatsUAS_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 2, 2, 1, 6),
    _DsxT1E1IfAnsiTotalPathStatsUAS_Type()
)
dsxT1E1IfAnsiTotalPathStatsUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfAnsiTotalPathStatsUAS.setStatus("current")
_DsxT1E1IfAnsiTotalLineStatsCV_Type = Unsigned32
_DsxT1E1IfAnsiTotalLineStatsCV_Object = MibTableColumn
dsxT1E1IfAnsiTotalLineStatsCV = _DsxT1E1IfAnsiTotalLineStatsCV_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 2, 2, 1, 7),
    _DsxT1E1IfAnsiTotalLineStatsCV_Type()
)
dsxT1E1IfAnsiTotalLineStatsCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfAnsiTotalLineStatsCV.setStatus("current")
_DsxT1E1IfAnsiTotalLineStatsES_Type = Unsigned32
_DsxT1E1IfAnsiTotalLineStatsES_Object = MibTableColumn
dsxT1E1IfAnsiTotalLineStatsES = _DsxT1E1IfAnsiTotalLineStatsES_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 2, 2, 1, 8),
    _DsxT1E1IfAnsiTotalLineStatsES_Type()
)
dsxT1E1IfAnsiTotalLineStatsES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfAnsiTotalLineStatsES.setStatus("current")
_DsxT1E1IfAnsiTotalLineStatsSES_Type = Unsigned32
_DsxT1E1IfAnsiTotalLineStatsSES_Object = MibTableColumn
dsxT1E1IfAnsiTotalLineStatsSES = _DsxT1E1IfAnsiTotalLineStatsSES_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 2, 2, 1, 9),
    _DsxT1E1IfAnsiTotalLineStatsSES_Type()
)
dsxT1E1IfAnsiTotalLineStatsSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfAnsiTotalLineStatsSES.setStatus("current")
_DsxT1E1IfAnsiArchiveIntervalStatsTable_Object = MibTable
dsxT1E1IfAnsiArchiveIntervalStatsTable = _DsxT1E1IfAnsiArchiveIntervalStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 2, 3)
)
if mibBuilder.loadTexts:
    dsxT1E1IfAnsiArchiveIntervalStatsTable.setStatus("current")
_DsxT1E1IfAnsiArchiveIntervalStatsEntry_Object = MibTableRow
dsxT1E1IfAnsiArchiveIntervalStatsEntry = _DsxT1E1IfAnsiArchiveIntervalStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 2, 3, 1)
)
dsxT1E1IfAnsiArchiveIntervalStatsEntry.setIndexNames(
    (0, "TIARA-NETWORKS-DSX-TE1-MIB", "dsxT1E1IfIndex"),
    (0, "TIARA-NETWORKS-DSX-TE1-MIB", "dsxT1E1IfAnsiArchiveStatsInterval"),
)
if mibBuilder.loadTexts:
    dsxT1E1IfAnsiArchiveIntervalStatsEntry.setStatus("current")
_DsxT1E1IfAnsiArchiveStatsInterval_Type = Unsigned32
_DsxT1E1IfAnsiArchiveStatsInterval_Object = MibTableColumn
dsxT1E1IfAnsiArchiveStatsInterval = _DsxT1E1IfAnsiArchiveStatsInterval_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 2, 3, 1, 1),
    _DsxT1E1IfAnsiArchiveStatsInterval_Type()
)
dsxT1E1IfAnsiArchiveStatsInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dsxT1E1IfAnsiArchiveStatsInterval.setStatus("current")
_DsxT1E1IfAnsiArchiveIntervalPathStatsCV_Type = Unsigned32
_DsxT1E1IfAnsiArchiveIntervalPathStatsCV_Object = MibTableColumn
dsxT1E1IfAnsiArchiveIntervalPathStatsCV = _DsxT1E1IfAnsiArchiveIntervalPathStatsCV_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 2, 3, 1, 2),
    _DsxT1E1IfAnsiArchiveIntervalPathStatsCV_Type()
)
dsxT1E1IfAnsiArchiveIntervalPathStatsCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfAnsiArchiveIntervalPathStatsCV.setStatus("current")
_DsxT1E1IfAnsiArchiveIntervalPathStatsES_Type = Unsigned32
_DsxT1E1IfAnsiArchiveIntervalPathStatsES_Object = MibTableColumn
dsxT1E1IfAnsiArchiveIntervalPathStatsES = _DsxT1E1IfAnsiArchiveIntervalPathStatsES_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 2, 3, 1, 3),
    _DsxT1E1IfAnsiArchiveIntervalPathStatsES_Type()
)
dsxT1E1IfAnsiArchiveIntervalPathStatsES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfAnsiArchiveIntervalPathStatsES.setStatus("current")
_DsxT1E1IfAnsiArchiveIntervalPathStatsSES_Type = Unsigned32
_DsxT1E1IfAnsiArchiveIntervalPathStatsSES_Object = MibTableColumn
dsxT1E1IfAnsiArchiveIntervalPathStatsSES = _DsxT1E1IfAnsiArchiveIntervalPathStatsSES_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 2, 3, 1, 4),
    _DsxT1E1IfAnsiArchiveIntervalPathStatsSES_Type()
)
dsxT1E1IfAnsiArchiveIntervalPathStatsSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfAnsiArchiveIntervalPathStatsSES.setStatus("current")
_DsxT1E1IfAnsiArchiveIntervalPathStatsSAS_Type = Unsigned32
_DsxT1E1IfAnsiArchiveIntervalPathStatsSAS_Object = MibTableColumn
dsxT1E1IfAnsiArchiveIntervalPathStatsSAS = _DsxT1E1IfAnsiArchiveIntervalPathStatsSAS_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 2, 3, 1, 5),
    _DsxT1E1IfAnsiArchiveIntervalPathStatsSAS_Type()
)
dsxT1E1IfAnsiArchiveIntervalPathStatsSAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfAnsiArchiveIntervalPathStatsSAS.setStatus("current")
_DsxT1E1IfAnsiArchiveIntervalPathStatsCSS_Type = Unsigned32
_DsxT1E1IfAnsiArchiveIntervalPathStatsCSS_Object = MibTableColumn
dsxT1E1IfAnsiArchiveIntervalPathStatsCSS = _DsxT1E1IfAnsiArchiveIntervalPathStatsCSS_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 2, 3, 1, 6),
    _DsxT1E1IfAnsiArchiveIntervalPathStatsCSS_Type()
)
dsxT1E1IfAnsiArchiveIntervalPathStatsCSS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfAnsiArchiveIntervalPathStatsCSS.setStatus("current")
_DsxT1E1IfAnsiArchiveIntervalPathStatsUAS_Type = Unsigned32
_DsxT1E1IfAnsiArchiveIntervalPathStatsUAS_Object = MibTableColumn
dsxT1E1IfAnsiArchiveIntervalPathStatsUAS = _DsxT1E1IfAnsiArchiveIntervalPathStatsUAS_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 2, 3, 1, 7),
    _DsxT1E1IfAnsiArchiveIntervalPathStatsUAS_Type()
)
dsxT1E1IfAnsiArchiveIntervalPathStatsUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfAnsiArchiveIntervalPathStatsUAS.setStatus("current")
_DsxT1E1IfAnsiArchiveIntervalLineStatsCV_Type = Unsigned32
_DsxT1E1IfAnsiArchiveIntervalLineStatsCV_Object = MibTableColumn
dsxT1E1IfAnsiArchiveIntervalLineStatsCV = _DsxT1E1IfAnsiArchiveIntervalLineStatsCV_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 2, 3, 1, 8),
    _DsxT1E1IfAnsiArchiveIntervalLineStatsCV_Type()
)
dsxT1E1IfAnsiArchiveIntervalLineStatsCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfAnsiArchiveIntervalLineStatsCV.setStatus("current")
_DsxT1E1IfAnsiArchiveIntervalLineStatsES_Type = Unsigned32
_DsxT1E1IfAnsiArchiveIntervalLineStatsES_Object = MibTableColumn
dsxT1E1IfAnsiArchiveIntervalLineStatsES = _DsxT1E1IfAnsiArchiveIntervalLineStatsES_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 2, 3, 1, 9),
    _DsxT1E1IfAnsiArchiveIntervalLineStatsES_Type()
)
dsxT1E1IfAnsiArchiveIntervalLineStatsES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfAnsiArchiveIntervalLineStatsES.setStatus("current")
_DsxT1E1IfAnsiArchiveIntervalLineStatsSES_Type = Unsigned32
_DsxT1E1IfAnsiArchiveIntervalLineStatsSES_Object = MibTableColumn
dsxT1E1IfAnsiArchiveIntervalLineStatsSES = _DsxT1E1IfAnsiArchiveIntervalLineStatsSES_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 2, 3, 1, 10),
    _DsxT1E1IfAnsiArchiveIntervalLineStatsSES_Type()
)
dsxT1E1IfAnsiArchiveIntervalLineStatsSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfAnsiArchiveIntervalLineStatsSES.setStatus("current")
_DsxT1E1IfAttStatsGroup_ObjectIdentity = ObjectIdentity
dsxT1E1IfAttStatsGroup = _DsxT1E1IfAttStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 3)
)
_DsxT1E1IfAttCurrentStatsTable_Object = MibTable
dsxT1E1IfAttCurrentStatsTable = _DsxT1E1IfAttCurrentStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 3, 1)
)
if mibBuilder.loadTexts:
    dsxT1E1IfAttCurrentStatsTable.setStatus("current")
_DsxT1E1IfAttCurrentStatsEntry_Object = MibTableRow
dsxT1E1IfAttCurrentStatsEntry = _DsxT1E1IfAttCurrentStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 3, 1, 1)
)
if mibBuilder.loadTexts:
    dsxT1E1IfAttCurrentStatsEntry.setStatus("current")
_DsxT1E1IfAttCurrentStatsUASState_Type = TruthValue
_DsxT1E1IfAttCurrentStatsUASState_Object = MibTableColumn
dsxT1E1IfAttCurrentStatsUASState = _DsxT1E1IfAttCurrentStatsUASState_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 3, 1, 1, 1),
    _DsxT1E1IfAttCurrentStatsUASState_Type()
)
dsxT1E1IfAttCurrentStatsUASState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfAttCurrentStatsUASState.setStatus("current")
_DsxT1E1IfAttCurrentStatsTimeInCurrent_Type = Unsigned32
_DsxT1E1IfAttCurrentStatsTimeInCurrent_Object = MibTableColumn
dsxT1E1IfAttCurrentStatsTimeInCurrent = _DsxT1E1IfAttCurrentStatsTimeInCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 3, 1, 1, 2),
    _DsxT1E1IfAttCurrentStatsTimeInCurrent_Type()
)
dsxT1E1IfAttCurrentStatsTimeInCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfAttCurrentStatsTimeInCurrent.setStatus("current")
_DsxT1E1IfAttCurrentStatsEEV_Type = Unsigned32
_DsxT1E1IfAttCurrentStatsEEV_Object = MibTableColumn
dsxT1E1IfAttCurrentStatsEEV = _DsxT1E1IfAttCurrentStatsEEV_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 3, 1, 1, 3),
    _DsxT1E1IfAttCurrentStatsEEV_Type()
)
dsxT1E1IfAttCurrentStatsEEV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfAttCurrentStatsEEV.setStatus("current")
_DsxT1E1IfAttCurrentStatsES_Type = Unsigned32
_DsxT1E1IfAttCurrentStatsES_Object = MibTableColumn
dsxT1E1IfAttCurrentStatsES = _DsxT1E1IfAttCurrentStatsES_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 3, 1, 1, 4),
    _DsxT1E1IfAttCurrentStatsES_Type()
)
dsxT1E1IfAttCurrentStatsES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfAttCurrentStatsES.setStatus("current")
_DsxT1E1IfAttCurrentStatsUAS_Type = Unsigned32
_DsxT1E1IfAttCurrentStatsUAS_Object = MibTableColumn
dsxT1E1IfAttCurrentStatsUAS = _DsxT1E1IfAttCurrentStatsUAS_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 3, 1, 1, 5),
    _DsxT1E1IfAttCurrentStatsUAS_Type()
)
dsxT1E1IfAttCurrentStatsUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfAttCurrentStatsUAS.setStatus("current")
_DsxT1E1IfAttCurrentStatsBES_Type = Unsigned32
_DsxT1E1IfAttCurrentStatsBES_Object = MibTableColumn
dsxT1E1IfAttCurrentStatsBES = _DsxT1E1IfAttCurrentStatsBES_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 3, 1, 1, 6),
    _DsxT1E1IfAttCurrentStatsBES_Type()
)
dsxT1E1IfAttCurrentStatsBES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfAttCurrentStatsBES.setStatus("current")
_DsxT1E1IfAttCurrentStatsSES_Type = Unsigned32
_DsxT1E1IfAttCurrentStatsSES_Object = MibTableColumn
dsxT1E1IfAttCurrentStatsSES = _DsxT1E1IfAttCurrentStatsSES_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 3, 1, 1, 7),
    _DsxT1E1IfAttCurrentStatsSES_Type()
)
dsxT1E1IfAttCurrentStatsSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfAttCurrentStatsSES.setStatus("current")
_DsxT1E1IfAttCurrentStatsLOFC_Type = Unsigned32
_DsxT1E1IfAttCurrentStatsLOFC_Object = MibTableColumn
dsxT1E1IfAttCurrentStatsLOFC = _DsxT1E1IfAttCurrentStatsLOFC_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 3, 1, 1, 8),
    _DsxT1E1IfAttCurrentStatsLOFC_Type()
)
dsxT1E1IfAttCurrentStatsLOFC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfAttCurrentStatsLOFC.setStatus("current")
_DsxT1E1IfAttCurrentStatsCSS_Type = Unsigned32
_DsxT1E1IfAttCurrentStatsCSS_Object = MibTableColumn
dsxT1E1IfAttCurrentStatsCSS = _DsxT1E1IfAttCurrentStatsCSS_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 3, 1, 1, 9),
    _DsxT1E1IfAttCurrentStatsCSS_Type()
)
dsxT1E1IfAttCurrentStatsCSS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfAttCurrentStatsCSS.setStatus("current")
_DsxT1E1IfAttTotalStatsTable_Object = MibTable
dsxT1E1IfAttTotalStatsTable = _DsxT1E1IfAttTotalStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 3, 2)
)
if mibBuilder.loadTexts:
    dsxT1E1IfAttTotalStatsTable.setStatus("current")
_DsxT1E1IfAttTotalStatsEntry_Object = MibTableRow
dsxT1E1IfAttTotalStatsEntry = _DsxT1E1IfAttTotalStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 3, 2, 1)
)
if mibBuilder.loadTexts:
    dsxT1E1IfAttTotalStatsEntry.setStatus("current")
_DsxT1E1IfAttTotalStatsEEV_Type = Unsigned32
_DsxT1E1IfAttTotalStatsEEV_Object = MibTableColumn
dsxT1E1IfAttTotalStatsEEV = _DsxT1E1IfAttTotalStatsEEV_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 3, 2, 1, 1),
    _DsxT1E1IfAttTotalStatsEEV_Type()
)
dsxT1E1IfAttTotalStatsEEV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfAttTotalStatsEEV.setStatus("current")
_DsxT1E1IfAttTotalStatsES_Type = Unsigned32
_DsxT1E1IfAttTotalStatsES_Object = MibTableColumn
dsxT1E1IfAttTotalStatsES = _DsxT1E1IfAttTotalStatsES_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 3, 2, 1, 2),
    _DsxT1E1IfAttTotalStatsES_Type()
)
dsxT1E1IfAttTotalStatsES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfAttTotalStatsES.setStatus("current")
_DsxT1E1IfAttTotalStatsUAS_Type = Unsigned32
_DsxT1E1IfAttTotalStatsUAS_Object = MibTableColumn
dsxT1E1IfAttTotalStatsUAS = _DsxT1E1IfAttTotalStatsUAS_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 3, 2, 1, 3),
    _DsxT1E1IfAttTotalStatsUAS_Type()
)
dsxT1E1IfAttTotalStatsUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfAttTotalStatsUAS.setStatus("current")
_DsxT1E1IfAttTotalStatsBES_Type = Unsigned32
_DsxT1E1IfAttTotalStatsBES_Object = MibTableColumn
dsxT1E1IfAttTotalStatsBES = _DsxT1E1IfAttTotalStatsBES_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 3, 2, 1, 4),
    _DsxT1E1IfAttTotalStatsBES_Type()
)
dsxT1E1IfAttTotalStatsBES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfAttTotalStatsBES.setStatus("current")
_DsxT1E1IfAttTotalStatsSES_Type = Unsigned32
_DsxT1E1IfAttTotalStatsSES_Object = MibTableColumn
dsxT1E1IfAttTotalStatsSES = _DsxT1E1IfAttTotalStatsSES_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 3, 2, 1, 5),
    _DsxT1E1IfAttTotalStatsSES_Type()
)
dsxT1E1IfAttTotalStatsSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfAttTotalStatsSES.setStatus("current")
_DsxT1E1IfAttTotalStatsLOFC_Type = Unsigned32
_DsxT1E1IfAttTotalStatsLOFC_Object = MibTableColumn
dsxT1E1IfAttTotalStatsLOFC = _DsxT1E1IfAttTotalStatsLOFC_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 3, 2, 1, 6),
    _DsxT1E1IfAttTotalStatsLOFC_Type()
)
dsxT1E1IfAttTotalStatsLOFC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfAttTotalStatsLOFC.setStatus("current")
_DsxT1E1IfAttTotalStatsCSS_Type = Unsigned32
_DsxT1E1IfAttTotalStatsCSS_Object = MibTableColumn
dsxT1E1IfAttTotalStatsCSS = _DsxT1E1IfAttTotalStatsCSS_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 3, 2, 1, 7),
    _DsxT1E1IfAttTotalStatsCSS_Type()
)
dsxT1E1IfAttTotalStatsCSS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfAttTotalStatsCSS.setStatus("current")
_DsxT1E1IfAttArchiveStatsTable_Object = MibTable
dsxT1E1IfAttArchiveStatsTable = _DsxT1E1IfAttArchiveStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 3, 3)
)
if mibBuilder.loadTexts:
    dsxT1E1IfAttArchiveStatsTable.setStatus("current")
_DsxT1E1IfAttArchiveStatsEntry_Object = MibTableRow
dsxT1E1IfAttArchiveStatsEntry = _DsxT1E1IfAttArchiveStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 3, 3, 1)
)
dsxT1E1IfAttArchiveStatsEntry.setIndexNames(
    (0, "TIARA-NETWORKS-DSX-TE1-MIB", "dsxT1E1IfIndex"),
    (0, "TIARA-NETWORKS-DSX-TE1-MIB", "dsxT1E1IfAttArchiveInterval"),
)
if mibBuilder.loadTexts:
    dsxT1E1IfAttArchiveStatsEntry.setStatus("current")
_DsxT1E1IfAttArchiveInterval_Type = Unsigned32
_DsxT1E1IfAttArchiveInterval_Object = MibTableColumn
dsxT1E1IfAttArchiveInterval = _DsxT1E1IfAttArchiveInterval_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 3, 3, 1, 1),
    _DsxT1E1IfAttArchiveInterval_Type()
)
dsxT1E1IfAttArchiveInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dsxT1E1IfAttArchiveInterval.setStatus("current")
_DsxT1E1IfAttArchiveStatsEEV_Type = Unsigned32
_DsxT1E1IfAttArchiveStatsEEV_Object = MibTableColumn
dsxT1E1IfAttArchiveStatsEEV = _DsxT1E1IfAttArchiveStatsEEV_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 3, 3, 1, 2),
    _DsxT1E1IfAttArchiveStatsEEV_Type()
)
dsxT1E1IfAttArchiveStatsEEV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfAttArchiveStatsEEV.setStatus("current")
_DsxT1E1IfAttArchiveStatsES_Type = Unsigned32
_DsxT1E1IfAttArchiveStatsES_Object = MibTableColumn
dsxT1E1IfAttArchiveStatsES = _DsxT1E1IfAttArchiveStatsES_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 3, 3, 1, 3),
    _DsxT1E1IfAttArchiveStatsES_Type()
)
dsxT1E1IfAttArchiveStatsES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfAttArchiveStatsES.setStatus("current")
_DsxT1E1IfAttArchiveStatsUAS_Type = Unsigned32
_DsxT1E1IfAttArchiveStatsUAS_Object = MibTableColumn
dsxT1E1IfAttArchiveStatsUAS = _DsxT1E1IfAttArchiveStatsUAS_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 3, 3, 1, 4),
    _DsxT1E1IfAttArchiveStatsUAS_Type()
)
dsxT1E1IfAttArchiveStatsUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfAttArchiveStatsUAS.setStatus("current")
_DsxT1E1IfAttArchiveStatsBES_Type = Unsigned32
_DsxT1E1IfAttArchiveStatsBES_Object = MibTableColumn
dsxT1E1IfAttArchiveStatsBES = _DsxT1E1IfAttArchiveStatsBES_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 3, 3, 1, 5),
    _DsxT1E1IfAttArchiveStatsBES_Type()
)
dsxT1E1IfAttArchiveStatsBES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfAttArchiveStatsBES.setStatus("current")
_DsxT1E1IfAttArchiveStatsSES_Type = Unsigned32
_DsxT1E1IfAttArchiveStatsSES_Object = MibTableColumn
dsxT1E1IfAttArchiveStatsSES = _DsxT1E1IfAttArchiveStatsSES_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 3, 3, 1, 6),
    _DsxT1E1IfAttArchiveStatsSES_Type()
)
dsxT1E1IfAttArchiveStatsSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfAttArchiveStatsSES.setStatus("current")
_DsxT1E1IfAttArchiveStatsLOFC_Type = Unsigned32
_DsxT1E1IfAttArchiveStatsLOFC_Object = MibTableColumn
dsxT1E1IfAttArchiveStatsLOFC = _DsxT1E1IfAttArchiveStatsLOFC_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 3, 3, 1, 7),
    _DsxT1E1IfAttArchiveStatsLOFC_Type()
)
dsxT1E1IfAttArchiveStatsLOFC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfAttArchiveStatsLOFC.setStatus("current")
_DsxT1E1IfAttArchiveStatsCSS_Type = Unsigned32
_DsxT1E1IfAttArchiveStatsCSS_Object = MibTableColumn
dsxT1E1IfAttArchiveStatsCSS = _DsxT1E1IfAttArchiveStatsCSS_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 3, 3, 1, 8),
    _DsxT1E1IfAttArchiveStatsCSS_Type()
)
dsxT1E1IfAttArchiveStatsCSS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfAttArchiveStatsCSS.setStatus("current")
_DsxT1E1IfIetfStatsGroup_ObjectIdentity = ObjectIdentity
dsxT1E1IfIetfStatsGroup = _DsxT1E1IfIetfStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 4)
)
_DsxT1E1IfIetfCurrentStatsTable_Object = MibTable
dsxT1E1IfIetfCurrentStatsTable = _DsxT1E1IfIetfCurrentStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 4, 1)
)
if mibBuilder.loadTexts:
    dsxT1E1IfIetfCurrentStatsTable.setStatus("current")
_DsxT1E1IfIetfCurrentStatsEntry_Object = MibTableRow
dsxT1E1IfIetfCurrentStatsEntry = _DsxT1E1IfIetfCurrentStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 4, 1, 1)
)
if mibBuilder.loadTexts:
    dsxT1E1IfIetfCurrentStatsEntry.setStatus("current")
_DsxT1E1IfIetfCurrentStatsUASState_Type = TruthValue
_DsxT1E1IfIetfCurrentStatsUASState_Object = MibTableColumn
dsxT1E1IfIetfCurrentStatsUASState = _DsxT1E1IfIetfCurrentStatsUASState_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 4, 1, 1, 1),
    _DsxT1E1IfIetfCurrentStatsUASState_Type()
)
dsxT1E1IfIetfCurrentStatsUASState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfIetfCurrentStatsUASState.setStatus("current")
_DsxT1E1IfIetfCurrentStatsTimeInCurrent_Type = Unsigned32
_DsxT1E1IfIetfCurrentStatsTimeInCurrent_Object = MibTableColumn
dsxT1E1IfIetfCurrentStatsTimeInCurrent = _DsxT1E1IfIetfCurrentStatsTimeInCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 4, 1, 1, 2),
    _DsxT1E1IfIetfCurrentStatsTimeInCurrent_Type()
)
dsxT1E1IfIetfCurrentStatsTimeInCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfIetfCurrentStatsTimeInCurrent.setStatus("current")
_DsxT1E1IfIetfCurrentStatsES_Type = Unsigned32
_DsxT1E1IfIetfCurrentStatsES_Object = MibTableColumn
dsxT1E1IfIetfCurrentStatsES = _DsxT1E1IfIetfCurrentStatsES_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 4, 1, 1, 3),
    _DsxT1E1IfIetfCurrentStatsES_Type()
)
dsxT1E1IfIetfCurrentStatsES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfIetfCurrentStatsES.setStatus("current")
_DsxT1E1IfIetfCurrentStatsSES_Type = Unsigned32
_DsxT1E1IfIetfCurrentStatsSES_Object = MibTableColumn
dsxT1E1IfIetfCurrentStatsSES = _DsxT1E1IfIetfCurrentStatsSES_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 4, 1, 1, 4),
    _DsxT1E1IfIetfCurrentStatsSES_Type()
)
dsxT1E1IfIetfCurrentStatsSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfIetfCurrentStatsSES.setStatus("current")
_DsxT1E1IfIetfCurrentStatsSEFS_Type = Unsigned32
_DsxT1E1IfIetfCurrentStatsSEFS_Object = MibTableColumn
dsxT1E1IfIetfCurrentStatsSEFS = _DsxT1E1IfIetfCurrentStatsSEFS_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 4, 1, 1, 5),
    _DsxT1E1IfIetfCurrentStatsSEFS_Type()
)
dsxT1E1IfIetfCurrentStatsSEFS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfIetfCurrentStatsSEFS.setStatus("current")
_DsxT1E1IfIetfCurrentStatsUAS_Type = Unsigned32
_DsxT1E1IfIetfCurrentStatsUAS_Object = MibTableColumn
dsxT1E1IfIetfCurrentStatsUAS = _DsxT1E1IfIetfCurrentStatsUAS_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 4, 1, 1, 6),
    _DsxT1E1IfIetfCurrentStatsUAS_Type()
)
dsxT1E1IfIetfCurrentStatsUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfIetfCurrentStatsUAS.setStatus("current")
_DsxT1E1IfIetfCurrentStatsCSS_Type = Unsigned32
_DsxT1E1IfIetfCurrentStatsCSS_Object = MibTableColumn
dsxT1E1IfIetfCurrentStatsCSS = _DsxT1E1IfIetfCurrentStatsCSS_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 4, 1, 1, 7),
    _DsxT1E1IfIetfCurrentStatsCSS_Type()
)
dsxT1E1IfIetfCurrentStatsCSS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfIetfCurrentStatsCSS.setStatus("current")
_DsxT1E1IfIetfCurrentStatsPCV_Type = Unsigned32
_DsxT1E1IfIetfCurrentStatsPCV_Object = MibTableColumn
dsxT1E1IfIetfCurrentStatsPCV = _DsxT1E1IfIetfCurrentStatsPCV_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 4, 1, 1, 8),
    _DsxT1E1IfIetfCurrentStatsPCV_Type()
)
dsxT1E1IfIetfCurrentStatsPCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfIetfCurrentStatsPCV.setStatus("current")
_DsxT1E1IfIetfCurrentStatsLES_Type = Unsigned32
_DsxT1E1IfIetfCurrentStatsLES_Object = MibTableColumn
dsxT1E1IfIetfCurrentStatsLES = _DsxT1E1IfIetfCurrentStatsLES_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 4, 1, 1, 9),
    _DsxT1E1IfIetfCurrentStatsLES_Type()
)
dsxT1E1IfIetfCurrentStatsLES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfIetfCurrentStatsLES.setStatus("current")
_DsxT1E1IfIetfCurrentStatsBES_Type = Unsigned32
_DsxT1E1IfIetfCurrentStatsBES_Object = MibTableColumn
dsxT1E1IfIetfCurrentStatsBES = _DsxT1E1IfIetfCurrentStatsBES_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 4, 1, 1, 10),
    _DsxT1E1IfIetfCurrentStatsBES_Type()
)
dsxT1E1IfIetfCurrentStatsBES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfIetfCurrentStatsBES.setStatus("current")
_DsxT1E1IfIetfCurrentStatsDM_Type = Unsigned32
_DsxT1E1IfIetfCurrentStatsDM_Object = MibTableColumn
dsxT1E1IfIetfCurrentStatsDM = _DsxT1E1IfIetfCurrentStatsDM_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 4, 1, 1, 11),
    _DsxT1E1IfIetfCurrentStatsDM_Type()
)
dsxT1E1IfIetfCurrentStatsDM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfIetfCurrentStatsDM.setStatus("current")
_DsxT1E1IfIetfCurrentStatsLCV_Type = Unsigned32
_DsxT1E1IfIetfCurrentStatsLCV_Object = MibTableColumn
dsxT1E1IfIetfCurrentStatsLCV = _DsxT1E1IfIetfCurrentStatsLCV_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 4, 1, 1, 12),
    _DsxT1E1IfIetfCurrentStatsLCV_Type()
)
dsxT1E1IfIetfCurrentStatsLCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfIetfCurrentStatsLCV.setStatus("current")
_DsxT1E1IfIetfTotalStatsTable_Object = MibTable
dsxT1E1IfIetfTotalStatsTable = _DsxT1E1IfIetfTotalStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 4, 2)
)
if mibBuilder.loadTexts:
    dsxT1E1IfIetfTotalStatsTable.setStatus("current")
_DsxT1E1IfIetfTotalStatsEntry_Object = MibTableRow
dsxT1E1IfIetfTotalStatsEntry = _DsxT1E1IfIetfTotalStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 4, 2, 1)
)
if mibBuilder.loadTexts:
    dsxT1E1IfIetfTotalStatsEntry.setStatus("current")
_DsxT1E1IfIetfTotalStatsES_Type = Unsigned32
_DsxT1E1IfIetfTotalStatsES_Object = MibTableColumn
dsxT1E1IfIetfTotalStatsES = _DsxT1E1IfIetfTotalStatsES_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 4, 2, 1, 1),
    _DsxT1E1IfIetfTotalStatsES_Type()
)
dsxT1E1IfIetfTotalStatsES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfIetfTotalStatsES.setStatus("current")
_DsxT1E1IfIetfTotalStatsSES_Type = Unsigned32
_DsxT1E1IfIetfTotalStatsSES_Object = MibTableColumn
dsxT1E1IfIetfTotalStatsSES = _DsxT1E1IfIetfTotalStatsSES_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 4, 2, 1, 2),
    _DsxT1E1IfIetfTotalStatsSES_Type()
)
dsxT1E1IfIetfTotalStatsSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfIetfTotalStatsSES.setStatus("current")
_DsxT1E1IfIetfTotalStatsSEFS_Type = Unsigned32
_DsxT1E1IfIetfTotalStatsSEFS_Object = MibTableColumn
dsxT1E1IfIetfTotalStatsSEFS = _DsxT1E1IfIetfTotalStatsSEFS_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 4, 2, 1, 3),
    _DsxT1E1IfIetfTotalStatsSEFS_Type()
)
dsxT1E1IfIetfTotalStatsSEFS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfIetfTotalStatsSEFS.setStatus("current")
_DsxT1E1IfIetfTotalStatsUAS_Type = Unsigned32
_DsxT1E1IfIetfTotalStatsUAS_Object = MibTableColumn
dsxT1E1IfIetfTotalStatsUAS = _DsxT1E1IfIetfTotalStatsUAS_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 4, 2, 1, 4),
    _DsxT1E1IfIetfTotalStatsUAS_Type()
)
dsxT1E1IfIetfTotalStatsUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfIetfTotalStatsUAS.setStatus("current")
_DsxT1E1IfIetfTotalStatsCSS_Type = Unsigned32
_DsxT1E1IfIetfTotalStatsCSS_Object = MibTableColumn
dsxT1E1IfIetfTotalStatsCSS = _DsxT1E1IfIetfTotalStatsCSS_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 4, 2, 1, 5),
    _DsxT1E1IfIetfTotalStatsCSS_Type()
)
dsxT1E1IfIetfTotalStatsCSS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfIetfTotalStatsCSS.setStatus("current")
_DsxT1E1IfIetfTotalStatsPCV_Type = Unsigned32
_DsxT1E1IfIetfTotalStatsPCV_Object = MibTableColumn
dsxT1E1IfIetfTotalStatsPCV = _DsxT1E1IfIetfTotalStatsPCV_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 4, 2, 1, 6),
    _DsxT1E1IfIetfTotalStatsPCV_Type()
)
dsxT1E1IfIetfTotalStatsPCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfIetfTotalStatsPCV.setStatus("current")
_DsxT1E1IfIetfTotalStatsLES_Type = Unsigned32
_DsxT1E1IfIetfTotalStatsLES_Object = MibTableColumn
dsxT1E1IfIetfTotalStatsLES = _DsxT1E1IfIetfTotalStatsLES_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 4, 2, 1, 7),
    _DsxT1E1IfIetfTotalStatsLES_Type()
)
dsxT1E1IfIetfTotalStatsLES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfIetfTotalStatsLES.setStatus("current")
_DsxT1E1IfIetfTotalStatsBES_Type = Unsigned32
_DsxT1E1IfIetfTotalStatsBES_Object = MibTableColumn
dsxT1E1IfIetfTotalStatsBES = _DsxT1E1IfIetfTotalStatsBES_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 4, 2, 1, 8),
    _DsxT1E1IfIetfTotalStatsBES_Type()
)
dsxT1E1IfIetfTotalStatsBES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfIetfTotalStatsBES.setStatus("current")
_DsxT1E1IfIetfTotalStatsDM_Type = Unsigned32
_DsxT1E1IfIetfTotalStatsDM_Object = MibTableColumn
dsxT1E1IfIetfTotalStatsDM = _DsxT1E1IfIetfTotalStatsDM_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 4, 2, 1, 9),
    _DsxT1E1IfIetfTotalStatsDM_Type()
)
dsxT1E1IfIetfTotalStatsDM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfIetfTotalStatsDM.setStatus("current")
_DsxT1E1IfIetfTotalStatsLCV_Type = Unsigned32
_DsxT1E1IfIetfTotalStatsLCV_Object = MibTableColumn
dsxT1E1IfIetfTotalStatsLCV = _DsxT1E1IfIetfTotalStatsLCV_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 4, 2, 1, 10),
    _DsxT1E1IfIetfTotalStatsLCV_Type()
)
dsxT1E1IfIetfTotalStatsLCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfIetfTotalStatsLCV.setStatus("current")
_DsxT1E1IfIetfArchiveStatsTable_Object = MibTable
dsxT1E1IfIetfArchiveStatsTable = _DsxT1E1IfIetfArchiveStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 4, 3)
)
if mibBuilder.loadTexts:
    dsxT1E1IfIetfArchiveStatsTable.setStatus("current")
_DsxT1E1IfIetfArchiveStatsEntry_Object = MibTableRow
dsxT1E1IfIetfArchiveStatsEntry = _DsxT1E1IfIetfArchiveStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 4, 3, 1)
)
dsxT1E1IfIetfArchiveStatsEntry.setIndexNames(
    (0, "TIARA-NETWORKS-DSX-TE1-MIB", "dsxT1E1IfIndex"),
    (0, "TIARA-NETWORKS-DSX-TE1-MIB", "dsxT1E1IfIetfArchiveStatsInterval"),
)
if mibBuilder.loadTexts:
    dsxT1E1IfIetfArchiveStatsEntry.setStatus("current")
_DsxT1E1IfIetfArchiveStatsInterval_Type = Unsigned32
_DsxT1E1IfIetfArchiveStatsInterval_Object = MibTableColumn
dsxT1E1IfIetfArchiveStatsInterval = _DsxT1E1IfIetfArchiveStatsInterval_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 4, 3, 1, 1),
    _DsxT1E1IfIetfArchiveStatsInterval_Type()
)
dsxT1E1IfIetfArchiveStatsInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dsxT1E1IfIetfArchiveStatsInterval.setStatus("current")
_DsxT1E1IfIetfArchiveStatsES_Type = Unsigned32
_DsxT1E1IfIetfArchiveStatsES_Object = MibTableColumn
dsxT1E1IfIetfArchiveStatsES = _DsxT1E1IfIetfArchiveStatsES_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 4, 3, 1, 2),
    _DsxT1E1IfIetfArchiveStatsES_Type()
)
dsxT1E1IfIetfArchiveStatsES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfIetfArchiveStatsES.setStatus("current")
_DsxT1E1IfIetfArchiveStatsSES_Type = Unsigned32
_DsxT1E1IfIetfArchiveStatsSES_Object = MibTableColumn
dsxT1E1IfIetfArchiveStatsSES = _DsxT1E1IfIetfArchiveStatsSES_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 4, 3, 1, 3),
    _DsxT1E1IfIetfArchiveStatsSES_Type()
)
dsxT1E1IfIetfArchiveStatsSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfIetfArchiveStatsSES.setStatus("current")
_DsxT1E1IfIetfArchiveStatsSEFS_Type = Unsigned32
_DsxT1E1IfIetfArchiveStatsSEFS_Object = MibTableColumn
dsxT1E1IfIetfArchiveStatsSEFS = _DsxT1E1IfIetfArchiveStatsSEFS_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 4, 3, 1, 4),
    _DsxT1E1IfIetfArchiveStatsSEFS_Type()
)
dsxT1E1IfIetfArchiveStatsSEFS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfIetfArchiveStatsSEFS.setStatus("current")
_DsxT1E1IfIetfArchiveStatsUAS_Type = Unsigned32
_DsxT1E1IfIetfArchiveStatsUAS_Object = MibTableColumn
dsxT1E1IfIetfArchiveStatsUAS = _DsxT1E1IfIetfArchiveStatsUAS_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 4, 3, 1, 5),
    _DsxT1E1IfIetfArchiveStatsUAS_Type()
)
dsxT1E1IfIetfArchiveStatsUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfIetfArchiveStatsUAS.setStatus("current")
_DsxT1E1IfIetfArchiveStatsCSS_Type = Unsigned32
_DsxT1E1IfIetfArchiveStatsCSS_Object = MibTableColumn
dsxT1E1IfIetfArchiveStatsCSS = _DsxT1E1IfIetfArchiveStatsCSS_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 4, 3, 1, 6),
    _DsxT1E1IfIetfArchiveStatsCSS_Type()
)
dsxT1E1IfIetfArchiveStatsCSS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfIetfArchiveStatsCSS.setStatus("current")
_DsxT1E1IfIetfArchiveStatsPCV_Type = Unsigned32
_DsxT1E1IfIetfArchiveStatsPCV_Object = MibTableColumn
dsxT1E1IfIetfArchiveStatsPCV = _DsxT1E1IfIetfArchiveStatsPCV_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 4, 3, 1, 7),
    _DsxT1E1IfIetfArchiveStatsPCV_Type()
)
dsxT1E1IfIetfArchiveStatsPCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfIetfArchiveStatsPCV.setStatus("current")
_DsxT1E1IfIetfArchiveStatsLES_Type = Unsigned32
_DsxT1E1IfIetfArchiveStatsLES_Object = MibTableColumn
dsxT1E1IfIetfArchiveStatsLES = _DsxT1E1IfIetfArchiveStatsLES_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 4, 3, 1, 8),
    _DsxT1E1IfIetfArchiveStatsLES_Type()
)
dsxT1E1IfIetfArchiveStatsLES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfIetfArchiveStatsLES.setStatus("current")
_DsxT1E1IfIetfArchiveStatsBES_Type = Unsigned32
_DsxT1E1IfIetfArchiveStatsBES_Object = MibTableColumn
dsxT1E1IfIetfArchiveStatsBES = _DsxT1E1IfIetfArchiveStatsBES_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 4, 3, 1, 9),
    _DsxT1E1IfIetfArchiveStatsBES_Type()
)
dsxT1E1IfIetfArchiveStatsBES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfIetfArchiveStatsBES.setStatus("current")
_DsxT1E1IfIetfArchiveStatsDM_Type = Unsigned32
_DsxT1E1IfIetfArchiveStatsDM_Object = MibTableColumn
dsxT1E1IfIetfArchiveStatsDM = _DsxT1E1IfIetfArchiveStatsDM_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 4, 3, 1, 10),
    _DsxT1E1IfIetfArchiveStatsDM_Type()
)
dsxT1E1IfIetfArchiveStatsDM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfIetfArchiveStatsDM.setStatus("current")
_DsxT1E1IfIetfArchiveStatsLCV_Type = Unsigned32
_DsxT1E1IfIetfArchiveStatsLCV_Object = MibTableColumn
dsxT1E1IfIetfArchiveStatsLCV = _DsxT1E1IfIetfArchiveStatsLCV_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 4, 3, 1, 11),
    _DsxT1E1IfIetfArchiveStatsLCV_Type()
)
dsxT1E1IfIetfArchiveStatsLCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfIetfArchiveStatsLCV.setStatus("current")
_DsxT1E1IfUserStatsGroup_ObjectIdentity = ObjectIdentity
dsxT1E1IfUserStatsGroup = _DsxT1E1IfUserStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 5)
)
_DsxT1E1IfUserCurrentStatsTable_Object = MibTable
dsxT1E1IfUserCurrentStatsTable = _DsxT1E1IfUserCurrentStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 5, 1)
)
if mibBuilder.loadTexts:
    dsxT1E1IfUserCurrentStatsTable.setStatus("current")
_DsxT1E1IfUserCurrentStatsEntry_Object = MibTableRow
dsxT1E1IfUserCurrentStatsEntry = _DsxT1E1IfUserCurrentStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 5, 1, 1)
)
if mibBuilder.loadTexts:
    dsxT1E1IfUserCurrentStatsEntry.setStatus("current")
_DsxT1E1IfUserCurrentStatsUASState_Type = TruthValue
_DsxT1E1IfUserCurrentStatsUASState_Object = MibTableColumn
dsxT1E1IfUserCurrentStatsUASState = _DsxT1E1IfUserCurrentStatsUASState_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 5, 1, 1, 1),
    _DsxT1E1IfUserCurrentStatsUASState_Type()
)
dsxT1E1IfUserCurrentStatsUASState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfUserCurrentStatsUASState.setStatus("current")
_DsxT1E1IfUserCurrentStatsTimeInCurrent_Type = Unsigned32
_DsxT1E1IfUserCurrentStatsTimeInCurrent_Object = MibTableColumn
dsxT1E1IfUserCurrentStatsTimeInCurrent = _DsxT1E1IfUserCurrentStatsTimeInCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 5, 1, 1, 2),
    _DsxT1E1IfUserCurrentStatsTimeInCurrent_Type()
)
dsxT1E1IfUserCurrentStatsTimeInCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfUserCurrentStatsTimeInCurrent.setStatus("current")
_DsxT1E1IfUserCurrentStatsEEV_Type = Unsigned32
_DsxT1E1IfUserCurrentStatsEEV_Object = MibTableColumn
dsxT1E1IfUserCurrentStatsEEV = _DsxT1E1IfUserCurrentStatsEEV_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 5, 1, 1, 3),
    _DsxT1E1IfUserCurrentStatsEEV_Type()
)
dsxT1E1IfUserCurrentStatsEEV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfUserCurrentStatsEEV.setStatus("current")
_DsxT1E1IfUserCurrentStatsES_Type = Unsigned32
_DsxT1E1IfUserCurrentStatsES_Object = MibTableColumn
dsxT1E1IfUserCurrentStatsES = _DsxT1E1IfUserCurrentStatsES_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 5, 1, 1, 4),
    _DsxT1E1IfUserCurrentStatsES_Type()
)
dsxT1E1IfUserCurrentStatsES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfUserCurrentStatsES.setStatus("current")
_DsxT1E1IfUserCurrentStatsUAS_Type = Unsigned32
_DsxT1E1IfUserCurrentStatsUAS_Object = MibTableColumn
dsxT1E1IfUserCurrentStatsUAS = _DsxT1E1IfUserCurrentStatsUAS_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 5, 1, 1, 5),
    _DsxT1E1IfUserCurrentStatsUAS_Type()
)
dsxT1E1IfUserCurrentStatsUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfUserCurrentStatsUAS.setStatus("current")
_DsxT1E1IfUserCurrentStatsBES_Type = Unsigned32
_DsxT1E1IfUserCurrentStatsBES_Object = MibTableColumn
dsxT1E1IfUserCurrentStatsBES = _DsxT1E1IfUserCurrentStatsBES_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 5, 1, 1, 6),
    _DsxT1E1IfUserCurrentStatsBES_Type()
)
dsxT1E1IfUserCurrentStatsBES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfUserCurrentStatsBES.setStatus("current")
_DsxT1E1IfUserCurrentStatsSES_Type = Unsigned32
_DsxT1E1IfUserCurrentStatsSES_Object = MibTableColumn
dsxT1E1IfUserCurrentStatsSES = _DsxT1E1IfUserCurrentStatsSES_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 5, 1, 1, 7),
    _DsxT1E1IfUserCurrentStatsSES_Type()
)
dsxT1E1IfUserCurrentStatsSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfUserCurrentStatsSES.setStatus("current")
_DsxT1E1IfUserCurrentStatsLOFC_Type = Unsigned32
_DsxT1E1IfUserCurrentStatsLOFC_Object = MibTableColumn
dsxT1E1IfUserCurrentStatsLOFC = _DsxT1E1IfUserCurrentStatsLOFC_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 5, 1, 1, 8),
    _DsxT1E1IfUserCurrentStatsLOFC_Type()
)
dsxT1E1IfUserCurrentStatsLOFC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfUserCurrentStatsLOFC.setStatus("current")
_DsxT1E1IfUserCurrentStatsCSS_Type = Unsigned32
_DsxT1E1IfUserCurrentStatsCSS_Object = MibTableColumn
dsxT1E1IfUserCurrentStatsCSS = _DsxT1E1IfUserCurrentStatsCSS_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 5, 1, 1, 9),
    _DsxT1E1IfUserCurrentStatsCSS_Type()
)
dsxT1E1IfUserCurrentStatsCSS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfUserCurrentStatsCSS.setStatus("current")
_DsxT1E1IfUserCurrentStatsBPV_Type = Unsigned32
_DsxT1E1IfUserCurrentStatsBPV_Object = MibTableColumn
dsxT1E1IfUserCurrentStatsBPV = _DsxT1E1IfUserCurrentStatsBPV_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 5, 1, 1, 10),
    _DsxT1E1IfUserCurrentStatsBPV_Type()
)
dsxT1E1IfUserCurrentStatsBPV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfUserCurrentStatsBPV.setStatus("current")
_DsxT1E1IfUserCurrentStatsOOF_Type = Unsigned32
_DsxT1E1IfUserCurrentStatsOOF_Object = MibTableColumn
dsxT1E1IfUserCurrentStatsOOF = _DsxT1E1IfUserCurrentStatsOOF_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 5, 1, 1, 11),
    _DsxT1E1IfUserCurrentStatsOOF_Type()
)
dsxT1E1IfUserCurrentStatsOOF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfUserCurrentStatsOOF.setStatus("current")
_DsxT1E1IfUserCurrentStatsCRC_Type = Unsigned32
_DsxT1E1IfUserCurrentStatsCRC_Object = MibTableColumn
dsxT1E1IfUserCurrentStatsCRC = _DsxT1E1IfUserCurrentStatsCRC_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 5, 1, 1, 12),
    _DsxT1E1IfUserCurrentStatsCRC_Type()
)
dsxT1E1IfUserCurrentStatsCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfUserCurrentStatsCRC.setStatus("current")
_DsxT1E1IfUserTotalStatsTable_Object = MibTable
dsxT1E1IfUserTotalStatsTable = _DsxT1E1IfUserTotalStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 5, 2)
)
if mibBuilder.loadTexts:
    dsxT1E1IfUserTotalStatsTable.setStatus("current")
_DsxT1E1IfUserTotalStatsEntry_Object = MibTableRow
dsxT1E1IfUserTotalStatsEntry = _DsxT1E1IfUserTotalStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 5, 2, 1)
)
dsxT1E1IfUserTotalStatsEntry.setIndexNames(
    (0, "TIARA-NETWORKS-DSX-TE1-MIB", "dsxT1E1IfIndex"),
    (0, "TIARA-NETWORKS-DSX-TE1-MIB", "dsxT1E1IfUserTotalStatsDay"),
)
if mibBuilder.loadTexts:
    dsxT1E1IfUserTotalStatsEntry.setStatus("current")
_DsxT1E1IfUserTotalStatsDay_Type = Unsigned32
_DsxT1E1IfUserTotalStatsDay_Object = MibTableColumn
dsxT1E1IfUserTotalStatsDay = _DsxT1E1IfUserTotalStatsDay_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 5, 2, 1, 1),
    _DsxT1E1IfUserTotalStatsDay_Type()
)
dsxT1E1IfUserTotalStatsDay.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dsxT1E1IfUserTotalStatsDay.setStatus("current")
_DsxT1E1IfUserTotalStatsEEV_Type = Unsigned32
_DsxT1E1IfUserTotalStatsEEV_Object = MibTableColumn
dsxT1E1IfUserTotalStatsEEV = _DsxT1E1IfUserTotalStatsEEV_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 5, 2, 1, 2),
    _DsxT1E1IfUserTotalStatsEEV_Type()
)
dsxT1E1IfUserTotalStatsEEV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfUserTotalStatsEEV.setStatus("current")
_DsxT1E1IfUserTotalStatsES_Type = Unsigned32
_DsxT1E1IfUserTotalStatsES_Object = MibTableColumn
dsxT1E1IfUserTotalStatsES = _DsxT1E1IfUserTotalStatsES_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 5, 2, 1, 3),
    _DsxT1E1IfUserTotalStatsES_Type()
)
dsxT1E1IfUserTotalStatsES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfUserTotalStatsES.setStatus("current")
_DsxT1E1IfUserTotalStatsUAS_Type = Unsigned32
_DsxT1E1IfUserTotalStatsUAS_Object = MibTableColumn
dsxT1E1IfUserTotalStatsUAS = _DsxT1E1IfUserTotalStatsUAS_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 5, 2, 1, 4),
    _DsxT1E1IfUserTotalStatsUAS_Type()
)
dsxT1E1IfUserTotalStatsUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfUserTotalStatsUAS.setStatus("current")
_DsxT1E1IfUserTotalStatsBES_Type = Unsigned32
_DsxT1E1IfUserTotalStatsBES_Object = MibTableColumn
dsxT1E1IfUserTotalStatsBES = _DsxT1E1IfUserTotalStatsBES_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 5, 2, 1, 5),
    _DsxT1E1IfUserTotalStatsBES_Type()
)
dsxT1E1IfUserTotalStatsBES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfUserTotalStatsBES.setStatus("current")
_DsxT1E1IfUserTotalStatsSES_Type = Unsigned32
_DsxT1E1IfUserTotalStatsSES_Object = MibTableColumn
dsxT1E1IfUserTotalStatsSES = _DsxT1E1IfUserTotalStatsSES_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 5, 2, 1, 6),
    _DsxT1E1IfUserTotalStatsSES_Type()
)
dsxT1E1IfUserTotalStatsSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfUserTotalStatsSES.setStatus("current")
_DsxT1E1IfUserTotalStatsLOFC_Type = Unsigned32
_DsxT1E1IfUserTotalStatsLOFC_Object = MibTableColumn
dsxT1E1IfUserTotalStatsLOFC = _DsxT1E1IfUserTotalStatsLOFC_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 5, 2, 1, 7),
    _DsxT1E1IfUserTotalStatsLOFC_Type()
)
dsxT1E1IfUserTotalStatsLOFC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfUserTotalStatsLOFC.setStatus("current")
_DsxT1E1IfUserTotalStatsCSS_Type = Unsigned32
_DsxT1E1IfUserTotalStatsCSS_Object = MibTableColumn
dsxT1E1IfUserTotalStatsCSS = _DsxT1E1IfUserTotalStatsCSS_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 5, 2, 1, 8),
    _DsxT1E1IfUserTotalStatsCSS_Type()
)
dsxT1E1IfUserTotalStatsCSS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfUserTotalStatsCSS.setStatus("current")
_DsxT1E1IfUserTotalStatsBPV_Type = Unsigned32
_DsxT1E1IfUserTotalStatsBPV_Object = MibTableColumn
dsxT1E1IfUserTotalStatsBPV = _DsxT1E1IfUserTotalStatsBPV_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 5, 2, 1, 9),
    _DsxT1E1IfUserTotalStatsBPV_Type()
)
dsxT1E1IfUserTotalStatsBPV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfUserTotalStatsBPV.setStatus("current")
_DsxT1E1IfUserTotalStatsOOF_Type = Unsigned32
_DsxT1E1IfUserTotalStatsOOF_Object = MibTableColumn
dsxT1E1IfUserTotalStatsOOF = _DsxT1E1IfUserTotalStatsOOF_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 5, 2, 1, 10),
    _DsxT1E1IfUserTotalStatsOOF_Type()
)
dsxT1E1IfUserTotalStatsOOF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfUserTotalStatsOOF.setStatus("current")
_DsxT1E1IfUserTotalStatsCRC_Type = Unsigned32
_DsxT1E1IfUserTotalStatsCRC_Object = MibTableColumn
dsxT1E1IfUserTotalStatsCRC = _DsxT1E1IfUserTotalStatsCRC_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 5, 2, 1, 11),
    _DsxT1E1IfUserTotalStatsCRC_Type()
)
dsxT1E1IfUserTotalStatsCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfUserTotalStatsCRC.setStatus("current")
_DsxT1E1IfUserLifetimeStatsTable_Object = MibTable
dsxT1E1IfUserLifetimeStatsTable = _DsxT1E1IfUserLifetimeStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 5, 3)
)
if mibBuilder.loadTexts:
    dsxT1E1IfUserLifetimeStatsTable.setStatus("current")
_DsxT1E1IfUserLifetimeStatsEntry_Object = MibTableRow
dsxT1E1IfUserLifetimeStatsEntry = _DsxT1E1IfUserLifetimeStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 5, 3, 1)
)
if mibBuilder.loadTexts:
    dsxT1E1IfUserLifetimeStatsEntry.setStatus("current")
_DsxT1E1IfUserLifetimeStatsEEV_Type = Unsigned32
_DsxT1E1IfUserLifetimeStatsEEV_Object = MibTableColumn
dsxT1E1IfUserLifetimeStatsEEV = _DsxT1E1IfUserLifetimeStatsEEV_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 5, 3, 1, 1),
    _DsxT1E1IfUserLifetimeStatsEEV_Type()
)
dsxT1E1IfUserLifetimeStatsEEV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfUserLifetimeStatsEEV.setStatus("current")
_DsxT1E1IfUserLifetimeStatsES_Type = Unsigned32
_DsxT1E1IfUserLifetimeStatsES_Object = MibTableColumn
dsxT1E1IfUserLifetimeStatsES = _DsxT1E1IfUserLifetimeStatsES_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 5, 3, 1, 2),
    _DsxT1E1IfUserLifetimeStatsES_Type()
)
dsxT1E1IfUserLifetimeStatsES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfUserLifetimeStatsES.setStatus("current")
_DsxT1E1IfUserLifetimeStatsUAS_Type = Unsigned32
_DsxT1E1IfUserLifetimeStatsUAS_Object = MibTableColumn
dsxT1E1IfUserLifetimeStatsUAS = _DsxT1E1IfUserLifetimeStatsUAS_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 5, 3, 1, 3),
    _DsxT1E1IfUserLifetimeStatsUAS_Type()
)
dsxT1E1IfUserLifetimeStatsUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfUserLifetimeStatsUAS.setStatus("current")
_DsxT1E1IfUserLifetimeStatsBES_Type = Unsigned32
_DsxT1E1IfUserLifetimeStatsBES_Object = MibTableColumn
dsxT1E1IfUserLifetimeStatsBES = _DsxT1E1IfUserLifetimeStatsBES_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 5, 3, 1, 4),
    _DsxT1E1IfUserLifetimeStatsBES_Type()
)
dsxT1E1IfUserLifetimeStatsBES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfUserLifetimeStatsBES.setStatus("current")
_DsxT1E1IfUserLifetimeStatsSES_Type = Unsigned32
_DsxT1E1IfUserLifetimeStatsSES_Object = MibTableColumn
dsxT1E1IfUserLifetimeStatsSES = _DsxT1E1IfUserLifetimeStatsSES_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 5, 3, 1, 5),
    _DsxT1E1IfUserLifetimeStatsSES_Type()
)
dsxT1E1IfUserLifetimeStatsSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfUserLifetimeStatsSES.setStatus("current")
_DsxT1E1IfUserLifetimeStatsLOFC_Type = Unsigned32
_DsxT1E1IfUserLifetimeStatsLOFC_Object = MibTableColumn
dsxT1E1IfUserLifetimeStatsLOFC = _DsxT1E1IfUserLifetimeStatsLOFC_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 5, 3, 1, 6),
    _DsxT1E1IfUserLifetimeStatsLOFC_Type()
)
dsxT1E1IfUserLifetimeStatsLOFC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfUserLifetimeStatsLOFC.setStatus("current")
_DsxT1E1IfUserLifetimeStatsCSS_Type = Unsigned32
_DsxT1E1IfUserLifetimeStatsCSS_Object = MibTableColumn
dsxT1E1IfUserLifetimeStatsCSS = _DsxT1E1IfUserLifetimeStatsCSS_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 5, 3, 1, 7),
    _DsxT1E1IfUserLifetimeStatsCSS_Type()
)
dsxT1E1IfUserLifetimeStatsCSS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfUserLifetimeStatsCSS.setStatus("current")
_DsxT1E1IfUserLifetimeStatsBPV_Type = Unsigned32
_DsxT1E1IfUserLifetimeStatsBPV_Object = MibTableColumn
dsxT1E1IfUserLifetimeStatsBPV = _DsxT1E1IfUserLifetimeStatsBPV_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 5, 3, 1, 8),
    _DsxT1E1IfUserLifetimeStatsBPV_Type()
)
dsxT1E1IfUserLifetimeStatsBPV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfUserLifetimeStatsBPV.setStatus("current")
_DsxT1E1IfUserLifetimeStatsOOF_Type = Unsigned32
_DsxT1E1IfUserLifetimeStatsOOF_Object = MibTableColumn
dsxT1E1IfUserLifetimeStatsOOF = _DsxT1E1IfUserLifetimeStatsOOF_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 5, 3, 1, 9),
    _DsxT1E1IfUserLifetimeStatsOOF_Type()
)
dsxT1E1IfUserLifetimeStatsOOF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfUserLifetimeStatsOOF.setStatus("current")
_DsxT1E1IfUserLifetimeStatsCRC_Type = Unsigned32
_DsxT1E1IfUserLifetimeStatsCRC_Object = MibTableColumn
dsxT1E1IfUserLifetimeStatsCRC = _DsxT1E1IfUserLifetimeStatsCRC_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 5, 3, 1, 10),
    _DsxT1E1IfUserLifetimeStatsCRC_Type()
)
dsxT1E1IfUserLifetimeStatsCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfUserLifetimeStatsCRC.setStatus("current")
_DsxT1E1IfUserArchiveStatsTable_Object = MibTable
dsxT1E1IfUserArchiveStatsTable = _DsxT1E1IfUserArchiveStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 5, 4)
)
if mibBuilder.loadTexts:
    dsxT1E1IfUserArchiveStatsTable.setStatus("current")
_DsxT1E1IfUserArchiveStatsEntry_Object = MibTableRow
dsxT1E1IfUserArchiveStatsEntry = _DsxT1E1IfUserArchiveStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 5, 4, 1)
)
dsxT1E1IfUserArchiveStatsEntry.setIndexNames(
    (0, "TIARA-NETWORKS-DSX-TE1-MIB", "dsxT1E1IfIndex"),
    (0, "TIARA-NETWORKS-DSX-TE1-MIB", "dsxT1E1IfUserArchiveStatsInterval"),
)
if mibBuilder.loadTexts:
    dsxT1E1IfUserArchiveStatsEntry.setStatus("current")
_DsxT1E1IfUserArchiveStatsInterval_Type = Unsigned32
_DsxT1E1IfUserArchiveStatsInterval_Object = MibTableColumn
dsxT1E1IfUserArchiveStatsInterval = _DsxT1E1IfUserArchiveStatsInterval_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 5, 4, 1, 1),
    _DsxT1E1IfUserArchiveStatsInterval_Type()
)
dsxT1E1IfUserArchiveStatsInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dsxT1E1IfUserArchiveStatsInterval.setStatus("current")
_DsxT1E1IfUserArchiveStatsEEV_Type = Unsigned32
_DsxT1E1IfUserArchiveStatsEEV_Object = MibTableColumn
dsxT1E1IfUserArchiveStatsEEV = _DsxT1E1IfUserArchiveStatsEEV_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 5, 4, 1, 2),
    _DsxT1E1IfUserArchiveStatsEEV_Type()
)
dsxT1E1IfUserArchiveStatsEEV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfUserArchiveStatsEEV.setStatus("current")
_DsxT1E1IfUserArchiveStatsES_Type = Unsigned32
_DsxT1E1IfUserArchiveStatsES_Object = MibTableColumn
dsxT1E1IfUserArchiveStatsES = _DsxT1E1IfUserArchiveStatsES_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 5, 4, 1, 3),
    _DsxT1E1IfUserArchiveStatsES_Type()
)
dsxT1E1IfUserArchiveStatsES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfUserArchiveStatsES.setStatus("current")
_DsxT1E1IfUserArchiveStatsUAS_Type = Unsigned32
_DsxT1E1IfUserArchiveStatsUAS_Object = MibTableColumn
dsxT1E1IfUserArchiveStatsUAS = _DsxT1E1IfUserArchiveStatsUAS_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 5, 4, 1, 4),
    _DsxT1E1IfUserArchiveStatsUAS_Type()
)
dsxT1E1IfUserArchiveStatsUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfUserArchiveStatsUAS.setStatus("current")
_DsxT1E1IfUserArchiveStatsBES_Type = Unsigned32
_DsxT1E1IfUserArchiveStatsBES_Object = MibTableColumn
dsxT1E1IfUserArchiveStatsBES = _DsxT1E1IfUserArchiveStatsBES_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 5, 4, 1, 5),
    _DsxT1E1IfUserArchiveStatsBES_Type()
)
dsxT1E1IfUserArchiveStatsBES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfUserArchiveStatsBES.setStatus("current")
_DsxT1E1IfUserArchiveStatsSES_Type = Unsigned32
_DsxT1E1IfUserArchiveStatsSES_Object = MibTableColumn
dsxT1E1IfUserArchiveStatsSES = _DsxT1E1IfUserArchiveStatsSES_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 5, 4, 1, 6),
    _DsxT1E1IfUserArchiveStatsSES_Type()
)
dsxT1E1IfUserArchiveStatsSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfUserArchiveStatsSES.setStatus("current")
_DsxT1E1IfUserArchiveStatsLOFC_Type = Unsigned32
_DsxT1E1IfUserArchiveStatsLOFC_Object = MibTableColumn
dsxT1E1IfUserArchiveStatsLOFC = _DsxT1E1IfUserArchiveStatsLOFC_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 5, 4, 1, 7),
    _DsxT1E1IfUserArchiveStatsLOFC_Type()
)
dsxT1E1IfUserArchiveStatsLOFC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfUserArchiveStatsLOFC.setStatus("current")
_DsxT1E1IfUserArchiveStatsCSS_Type = Unsigned32
_DsxT1E1IfUserArchiveStatsCSS_Object = MibTableColumn
dsxT1E1IfUserArchiveStatsCSS = _DsxT1E1IfUserArchiveStatsCSS_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 5, 4, 1, 8),
    _DsxT1E1IfUserArchiveStatsCSS_Type()
)
dsxT1E1IfUserArchiveStatsCSS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfUserArchiveStatsCSS.setStatus("current")
_DsxT1E1IfUserArchiveStatsBPV_Type = Unsigned32
_DsxT1E1IfUserArchiveStatsBPV_Object = MibTableColumn
dsxT1E1IfUserArchiveStatsBPV = _DsxT1E1IfUserArchiveStatsBPV_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 5, 4, 1, 9),
    _DsxT1E1IfUserArchiveStatsBPV_Type()
)
dsxT1E1IfUserArchiveStatsBPV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfUserArchiveStatsBPV.setStatus("current")
_DsxT1E1IfUserArchiveStatsOOF_Type = Unsigned32
_DsxT1E1IfUserArchiveStatsOOF_Object = MibTableColumn
dsxT1E1IfUserArchiveStatsOOF = _DsxT1E1IfUserArchiveStatsOOF_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 5, 4, 1, 10),
    _DsxT1E1IfUserArchiveStatsOOF_Type()
)
dsxT1E1IfUserArchiveStatsOOF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfUserArchiveStatsOOF.setStatus("current")
_DsxT1E1IfUserArchiveStatsCRC_Type = Unsigned32
_DsxT1E1IfUserArchiveStatsCRC_Object = MibTableColumn
dsxT1E1IfUserArchiveStatsCRC = _DsxT1E1IfUserArchiveStatsCRC_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 1, 3, 5, 4, 1, 11),
    _DsxT1E1IfUserArchiveStatsCRC_Type()
)
dsxT1E1IfUserArchiveStatsCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsxT1E1IfUserArchiveStatsCRC.setStatus("current")
_DsxT1E1Traps_ObjectIdentity = ObjectIdentity
dsxT1E1Traps = _DsxT1E1Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 2)
)
_DsxT1E1TrapVariables_ObjectIdentity = ObjectIdentity
dsxT1E1TrapVariables = _DsxT1E1TrapVariables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 2, 1)
)
_DsxT1E1Number_Type = Integer32
_DsxT1E1Number_Object = MibScalar
dsxT1E1Number = _DsxT1E1Number_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 2, 1, 1),
    _DsxT1E1Number_Type()
)
dsxT1E1Number.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dsxT1E1Number.setStatus("current")


class _DsxT1E1Type_Type(Integer32):
    """Custom type dsxT1E1Type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("type-t1", 1),
          ("type-t1-within-ct3", 2))
    )


_DsxT1E1Type_Type.__name__ = "Integer32"
_DsxT1E1Type_Object = MibScalar
dsxT1E1Type = _DsxT1E1Type_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 2, 1, 2),
    _DsxT1E1Type_Type()
)
dsxT1E1Type.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dsxT1E1Type.setStatus("current")
_DsxT1E1T3Number_Type = Integer32
_DsxT1E1T3Number_Object = MibScalar
dsxT1E1T3Number = _DsxT1E1T3Number_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 2, 1, 3),
    _DsxT1E1T3Number_Type()
)
dsxT1E1T3Number.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dsxT1E1T3Number.setStatus("current")


class _DsxT1E1AlarmType_Type(Integer32):
    """Custom type dsxT1E1AlarmType based on Integer32"""
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
              22)
        )
    )
    namedValues = NamedValues(
        *(("te1-alarm-lorc", 8),
          ("te1-alarm-rais", 1),
          ("te1-alarm-rexz", 6),
          ("te1-alarm-rfbe", 7),
          ("te1-alarm-rlof", 5),
          ("te1-alarm-rlos", 4),
          ("te1-alarm-roof", 3),
          ("te1-alarm-rrai", 2),
          ("te1-alarm-tais", 10),
          ("te1-alarm-tblu", 11),
          ("te1-alarm-threshold1", 13),
          ("te1-alarm-threshold10", 22),
          ("te1-alarm-threshold2", 14),
          ("te1-alarm-threshold3", 15),
          ("te1-alarm-threshold4", 16),
          ("te1-alarm-threshold5", 17),
          ("te1-alarm-threshold6", 18),
          ("te1-alarm-threshold7", 19),
          ("te1-alarm-threshold8", 20),
          ("te1-alarm-threshold9", 21),
          ("te1-alarm-tpde", 9),
          ("te1-alarm-trai", 12))
    )


_DsxT1E1AlarmType_Type.__name__ = "Integer32"
_DsxT1E1AlarmType_Object = MibScalar
dsxT1E1AlarmType = _DsxT1E1AlarmType_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 2, 1, 4),
    _DsxT1E1AlarmType_Type()
)
dsxT1E1AlarmType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dsxT1E1AlarmType.setStatus("current")
dsxT1E1IfConfigLineEntry.registerAugmentions(
    ("TIARA-NETWORKS-DSX-TE1-MIB",
     "dsxT1E1IfConfigFdlEntry")
)
dsxT1E1IfConfigFdlEntry.setIndexNames(*dsxT1E1IfConfigLineEntry.getIndexNames())
dsxT1E1IfConfigLineEntry.registerAugmentions(
    ("TIARA-NETWORKS-DSX-TE1-MIB",
     "dsxT1E1IfTestConfigEntry")
)
dsxT1E1IfTestConfigEntry.setIndexNames(*dsxT1E1IfConfigLineEntry.getIndexNames())
dsxT1E1IfConfigLineEntry.registerAugmentions(
    ("TIARA-NETWORKS-DSX-TE1-MIB",
     "dsxT1E1IfStatusEntry")
)
dsxT1E1IfStatusEntry.setIndexNames(*dsxT1E1IfConfigLineEntry.getIndexNames())
dsxT1E1IfConfigLineEntry.registerAugmentions(
    ("TIARA-NETWORKS-DSX-TE1-MIB",
     "dsxT1E1IfAlarmStatusEntry")
)
dsxT1E1IfAlarmStatusEntry.setIndexNames(*dsxT1E1IfConfigLineEntry.getIndexNames())
dsxT1E1IfConfigLineEntry.registerAugmentions(
    ("TIARA-NETWORKS-DSX-TE1-MIB",
     "dsxT1E1IfTestStatusEntry")
)
dsxT1E1IfTestStatusEntry.setIndexNames(*dsxT1E1IfConfigLineEntry.getIndexNames())
dsxT1E1IfConfigLineEntry.registerAugmentions(
    ("TIARA-NETWORKS-DSX-TE1-MIB",
     "dsxT1E1IfLastTestResultEntry")
)
dsxT1E1IfLastTestResultEntry.setIndexNames(*dsxT1E1IfConfigLineEntry.getIndexNames())
dsxT1E1IfConfigLineEntry.registerAugmentions(
    ("TIARA-NETWORKS-DSX-TE1-MIB",
     "dsxT1E1IfArchiveStatsValidIntervalsEntry")
)
dsxT1E1IfArchiveStatsValidIntervalsEntry.setIndexNames(*dsxT1E1IfConfigLineEntry.getIndexNames())
dsxT1E1IfConfigLineEntry.registerAugmentions(
    ("TIARA-NETWORKS-DSX-TE1-MIB",
     "dsxT1E1IfAnsiCurrentStatsEntry")
)
dsxT1E1IfAnsiCurrentStatsEntry.setIndexNames(*dsxT1E1IfConfigLineEntry.getIndexNames())
dsxT1E1IfConfigLineEntry.registerAugmentions(
    ("TIARA-NETWORKS-DSX-TE1-MIB",
     "dsxT1E1IfAnsiTotalStatsEntry")
)
dsxT1E1IfAnsiTotalStatsEntry.setIndexNames(*dsxT1E1IfConfigLineEntry.getIndexNames())
dsxT1E1IfConfigLineEntry.registerAugmentions(
    ("TIARA-NETWORKS-DSX-TE1-MIB",
     "dsxT1E1IfAttCurrentStatsEntry")
)
dsxT1E1IfAttCurrentStatsEntry.setIndexNames(*dsxT1E1IfConfigLineEntry.getIndexNames())
dsxT1E1IfConfigLineEntry.registerAugmentions(
    ("TIARA-NETWORKS-DSX-TE1-MIB",
     "dsxT1E1IfAttTotalStatsEntry")
)
dsxT1E1IfAttTotalStatsEntry.setIndexNames(*dsxT1E1IfConfigLineEntry.getIndexNames())
dsxT1E1IfConfigLineEntry.registerAugmentions(
    ("TIARA-NETWORKS-DSX-TE1-MIB",
     "dsxT1E1IfIetfCurrentStatsEntry")
)
dsxT1E1IfIetfCurrentStatsEntry.setIndexNames(*dsxT1E1IfConfigLineEntry.getIndexNames())
dsxT1E1IfConfigLineEntry.registerAugmentions(
    ("TIARA-NETWORKS-DSX-TE1-MIB",
     "dsxT1E1IfIetfTotalStatsEntry")
)
dsxT1E1IfIetfTotalStatsEntry.setIndexNames(*dsxT1E1IfConfigLineEntry.getIndexNames())
dsxT1E1IfConfigLineEntry.registerAugmentions(
    ("TIARA-NETWORKS-DSX-TE1-MIB",
     "dsxT1E1IfUserCurrentStatsEntry")
)
dsxT1E1IfUserCurrentStatsEntry.setIndexNames(*dsxT1E1IfConfigLineEntry.getIndexNames())
dsxT1E1IfConfigLineEntry.registerAugmentions(
    ("TIARA-NETWORKS-DSX-TE1-MIB",
     "dsxT1E1IfUserLifetimeStatsEntry")
)
dsxT1E1IfUserLifetimeStatsEntry.setIndexNames(*dsxT1E1IfConfigLineEntry.getIndexNames())

# Managed Objects groups


# Notification objects

dsxT1E1AlarmOnTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 2, 0, 1)
)
dsxT1E1AlarmOnTrap.setObjects(
      *(("TIARA-NETWORKS-DSX-TE1-MIB", "dsxT1E1IfIndex"),
        ("TIARA-NETWORKS-DSX-TE1-MIB", "dsxT1E1Number"),
        ("TIARA-NETWORKS-DSX-TE1-MIB", "dsxT1E1Type"),
        ("TIARA-NETWORKS-DSX-TE1-MIB", "dsxT1E1T3Number"),
        ("TIARA-NETWORKS-DSX-TE1-MIB", "dsxT1E1AlarmType"))
)
if mibBuilder.loadTexts:
    dsxT1E1AlarmOnTrap.setStatus(
        ""
    )

dsxT1E1AlarmOffTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2, 2, 0, 2)
)
dsxT1E1AlarmOffTrap.setObjects(
      *(("TIARA-NETWORKS-DSX-TE1-MIB", "dsxT1E1IfIndex"),
        ("TIARA-NETWORKS-DSX-TE1-MIB", "dsxT1E1Number"),
        ("TIARA-NETWORKS-DSX-TE1-MIB", "dsxT1E1Type"),
        ("TIARA-NETWORKS-DSX-TE1-MIB", "dsxT1E1T3Number"),
        ("TIARA-NETWORKS-DSX-TE1-MIB", "dsxT1E1AlarmType"))
)
if mibBuilder.loadTexts:
    dsxT1E1AlarmOffTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIARA-NETWORKS-DSX-TE1-MIB",
    **{"dsxT1E1MIB": dsxT1E1MIB,
       "dsxT1E1IfConfigGroup": dsxT1E1IfConfigGroup,
       "dsxT1E1IfConfigLineTable": dsxT1E1IfConfigLineTable,
       "dsxT1E1IfConfigLineEntry": dsxT1E1IfConfigLineEntry,
       "dsxT1E1IfIndex": dsxT1E1IfIndex,
       "dsxT1E1IfConfigServiceMode": dsxT1E1IfConfigServiceMode,
       "dsxT1E1IfConfigLineMode": dsxT1E1IfConfigLineMode,
       "dsxT1E1IfConfigLineType": dsxT1E1IfConfigLineType,
       "dsxT1E1IfConfigLineCode": dsxT1E1IfConfigLineCode,
       "dsxT1E1IfConfigLBO": dsxT1E1IfConfigLBO,
       "dsxT1E1IfConfigCableLength": dsxT1E1IfConfigCableLength,
       "dsxT1E1IfConfigRaiAlarm": dsxT1E1IfConfigRaiAlarm,
       "dsxT1E1IfConfigTransmitClock": dsxT1E1IfConfigTransmitClock,
       "dsxT1E1IfConfigTimeSlotMap": dsxT1E1IfConfigTimeSlotMap,
       "dsxT1E1IfCircuitId": dsxT1E1IfCircuitId,
       "dsxT1E1IfContactInfo": dsxT1E1IfContactInfo,
       "dsxT1E1IfDescription": dsxT1E1IfDescription,
       "dsxT1E1IfConfigFdlTable": dsxT1E1IfConfigFdlTable,
       "dsxT1E1IfConfigFdlEntry": dsxT1E1IfConfigFdlEntry,
       "dsxT1E1IfConfigFdl": dsxT1E1IfConfigFdl,
       "dsxT1E1IfConfigFdlCsuDsuType": dsxT1E1IfConfigFdlCsuDsuType,
       "dsxT1E1IfAlarmConfigGroup": dsxT1E1IfAlarmConfigGroup,
       "dsxT1E1IfAlarmThresholdConfigTable": dsxT1E1IfAlarmThresholdConfigTable,
       "dsxT1E1IfAlarmThresholdConfigEntry": dsxT1E1IfAlarmThresholdConfigEntry,
       "dsxT1E1IfAlarmThresholdConfigIndex": dsxT1E1IfAlarmThresholdConfigIndex,
       "dsxT1E1IfAlarmThresholdConfigObject": dsxT1E1IfAlarmThresholdConfigObject,
       "dsxT1E1IfAlarmThresholdConfigSamplingInterval": dsxT1E1IfAlarmThresholdConfigSamplingInterval,
       "dsxT1E1IfAlarmThresholdConfigSampleType": dsxT1E1IfAlarmThresholdConfigSampleType,
       "dsxT1E1IfAlarmThresholdConfigStartupType": dsxT1E1IfAlarmThresholdConfigStartupType,
       "dsxT1E1IfAlarmThresholdConfigRisingThreshold": dsxT1E1IfAlarmThresholdConfigRisingThreshold,
       "dsxT1E1IfAlarmThresholdConfigFallingThreshold": dsxT1E1IfAlarmThresholdConfigFallingThreshold,
       "dsxT1E1IfTestConfigTable": dsxT1E1IfTestConfigTable,
       "dsxT1E1IfTestConfigEntry": dsxT1E1IfTestConfigEntry,
       "dsxT1E1IfTestConfigType": dsxT1E1IfTestConfigType,
       "dsxT1E1IfTestConfigTime": dsxT1E1IfTestConfigTime,
       "dsxT1E1IfTestConfigPattern": dsxT1E1IfTestConfigPattern,
       "dsxT1E1IfTestConfigLoopCode": dsxT1E1IfTestConfigLoopCode,
       "dsxT1E1IfStatusGroup": dsxT1E1IfStatusGroup,
       "dsxT1E1IfStatusTable": dsxT1E1IfStatusTable,
       "dsxT1E1IfStatusEntry": dsxT1E1IfStatusEntry,
       "dsxT1E1IfStatusLineStatus": dsxT1E1IfStatusLineStatus,
       "dsxT1E1IfStatusTransmitClock": dsxT1E1IfStatusTransmitClock,
       "dsxT1E1IfAlarmStatusTable": dsxT1E1IfAlarmStatusTable,
       "dsxT1E1IfAlarmStatusEntry": dsxT1E1IfAlarmStatusEntry,
       "dsxT1E1IfAlarmStatusAlarmStatus": dsxT1E1IfAlarmStatusAlarmStatus,
       "dsxT1E1IfAlarmStatusThresholdStatus": dsxT1E1IfAlarmStatusThresholdStatus,
       "dsxT1E1IfTestStatusTable": dsxT1E1IfTestStatusTable,
       "dsxT1E1IfTestStatusEntry": dsxT1E1IfTestStatusEntry,
       "dsxT1E1IfTestStatusTestType": dsxT1E1IfTestStatusTestType,
       "dsxT1E1IfTestStatusTestTime": dsxT1E1IfTestStatusTestTime,
       "dsxT1E1IfTestStatusTestState": dsxT1E1IfTestStatusTestState,
       "dsxT1E1IfTestStatusTestPattern": dsxT1E1IfTestStatusTestPattern,
       "dsxT1E1IfTestStatusLockedSeconds": dsxT1E1IfTestStatusLockedSeconds,
       "dsxT1E1IfTestStatusSyncLossCount": dsxT1E1IfTestStatusSyncLossCount,
       "dsxT1E1IfTestStatusErrorCount": dsxT1E1IfTestStatusErrorCount,
       "dsxT1E1IfTestStatusLoopCode": dsxT1E1IfTestStatusLoopCode,
       "dsxT1E1IfLastTestResultTable": dsxT1E1IfLastTestResultTable,
       "dsxT1E1IfLastTestResultEntry": dsxT1E1IfLastTestResultEntry,
       "dsxT1E1IfLastTestResultTestType": dsxT1E1IfLastTestResultTestType,
       "dsxT1E1IfLastTestResultTestTime": dsxT1E1IfLastTestResultTestTime,
       "dsxT1E1IfLastTestResultTestState": dsxT1E1IfLastTestResultTestState,
       "dsxT1E1IfLastTestResultTestPattern": dsxT1E1IfLastTestResultTestPattern,
       "dsxT1E1IfLastTestResultLockedSeconds": dsxT1E1IfLastTestResultLockedSeconds,
       "dsxT1E1IfLastTestResultSyncLossCount": dsxT1E1IfLastTestResultSyncLossCount,
       "dsxT1E1IfLastTestResultErrorCount": dsxT1E1IfLastTestResultErrorCount,
       "dsxT1E1IfLastTestResultLoopCode": dsxT1E1IfLastTestResultLoopCode,
       "dsxT1E1IfStatsGroup": dsxT1E1IfStatsGroup,
       "dsxT1E1IfArchiveStatsValidIntervalsTable": dsxT1E1IfArchiveStatsValidIntervalsTable,
       "dsxT1E1IfArchiveStatsValidIntervalsEntry": dsxT1E1IfArchiveStatsValidIntervalsEntry,
       "dsxT1E1IfAnsiArchiveStatsValidIntervals": dsxT1E1IfAnsiArchiveStatsValidIntervals,
       "dsxT1E1IfAttArchiveStatsValidIntervals": dsxT1E1IfAttArchiveStatsValidIntervals,
       "dsxT1E1IfIetfArchiveStatsValidIntervals": dsxT1E1IfIetfArchiveStatsValidIntervals,
       "dsxT1E1IfUserTotalStatsValidDays": dsxT1E1IfUserTotalStatsValidDays,
       "dsxT1E1IfUserArchiveStatsValidIntervals": dsxT1E1IfUserArchiveStatsValidIntervals,
       "dsxT1E1IfAnsiStatsGroup": dsxT1E1IfAnsiStatsGroup,
       "dsxT1E1IfAnsiCurrentStatsTable": dsxT1E1IfAnsiCurrentStatsTable,
       "dsxT1E1IfAnsiCurrentStatsEntry": dsxT1E1IfAnsiCurrentStatsEntry,
       "dsxT1E1IfAnsiCurrentStatsUASState": dsxT1E1IfAnsiCurrentStatsUASState,
       "dsxT1E1IfAnsiCurrentStatsTimeInCurrent": dsxT1E1IfAnsiCurrentStatsTimeInCurrent,
       "dsxT1E1IfAnsiCurrentPathStatsCV": dsxT1E1IfAnsiCurrentPathStatsCV,
       "dsxT1E1IfAnsiCurrentPathStatsES": dsxT1E1IfAnsiCurrentPathStatsES,
       "dsxT1E1IfAnsiCurrentPathStatsSES": dsxT1E1IfAnsiCurrentPathStatsSES,
       "dsxT1E1IfAnsiCurrentPathStatsSAS": dsxT1E1IfAnsiCurrentPathStatsSAS,
       "dsxT1E1IfAnsiCurrentPathStatsCSS": dsxT1E1IfAnsiCurrentPathStatsCSS,
       "dsxT1E1IfAnsiCurrentPathStatsUAS": dsxT1E1IfAnsiCurrentPathStatsUAS,
       "dsxT1E1IfAnsiCurrentLineStatsCV": dsxT1E1IfAnsiCurrentLineStatsCV,
       "dsxT1E1IfAnsiCurrentLineStatsES": dsxT1E1IfAnsiCurrentLineStatsES,
       "dsxT1E1IfAnsiCurrentLineStatsSES": dsxT1E1IfAnsiCurrentLineStatsSES,
       "dsxT1E1IfAnsiTotalStatsTable": dsxT1E1IfAnsiTotalStatsTable,
       "dsxT1E1IfAnsiTotalStatsEntry": dsxT1E1IfAnsiTotalStatsEntry,
       "dsxT1E1IfAnsiTotalPathStatsCV": dsxT1E1IfAnsiTotalPathStatsCV,
       "dsxT1E1IfAnsiTotalPathStatsES": dsxT1E1IfAnsiTotalPathStatsES,
       "dsxT1E1IfAnsiTotalPathStatsSES": dsxT1E1IfAnsiTotalPathStatsSES,
       "dsxT1E1IfAnsiTotalPathStatsSAS": dsxT1E1IfAnsiTotalPathStatsSAS,
       "dsxT1E1IfAnsiTotalPathStatsCSS": dsxT1E1IfAnsiTotalPathStatsCSS,
       "dsxT1E1IfAnsiTotalPathStatsUAS": dsxT1E1IfAnsiTotalPathStatsUAS,
       "dsxT1E1IfAnsiTotalLineStatsCV": dsxT1E1IfAnsiTotalLineStatsCV,
       "dsxT1E1IfAnsiTotalLineStatsES": dsxT1E1IfAnsiTotalLineStatsES,
       "dsxT1E1IfAnsiTotalLineStatsSES": dsxT1E1IfAnsiTotalLineStatsSES,
       "dsxT1E1IfAnsiArchiveIntervalStatsTable": dsxT1E1IfAnsiArchiveIntervalStatsTable,
       "dsxT1E1IfAnsiArchiveIntervalStatsEntry": dsxT1E1IfAnsiArchiveIntervalStatsEntry,
       "dsxT1E1IfAnsiArchiveStatsInterval": dsxT1E1IfAnsiArchiveStatsInterval,
       "dsxT1E1IfAnsiArchiveIntervalPathStatsCV": dsxT1E1IfAnsiArchiveIntervalPathStatsCV,
       "dsxT1E1IfAnsiArchiveIntervalPathStatsES": dsxT1E1IfAnsiArchiveIntervalPathStatsES,
       "dsxT1E1IfAnsiArchiveIntervalPathStatsSES": dsxT1E1IfAnsiArchiveIntervalPathStatsSES,
       "dsxT1E1IfAnsiArchiveIntervalPathStatsSAS": dsxT1E1IfAnsiArchiveIntervalPathStatsSAS,
       "dsxT1E1IfAnsiArchiveIntervalPathStatsCSS": dsxT1E1IfAnsiArchiveIntervalPathStatsCSS,
       "dsxT1E1IfAnsiArchiveIntervalPathStatsUAS": dsxT1E1IfAnsiArchiveIntervalPathStatsUAS,
       "dsxT1E1IfAnsiArchiveIntervalLineStatsCV": dsxT1E1IfAnsiArchiveIntervalLineStatsCV,
       "dsxT1E1IfAnsiArchiveIntervalLineStatsES": dsxT1E1IfAnsiArchiveIntervalLineStatsES,
       "dsxT1E1IfAnsiArchiveIntervalLineStatsSES": dsxT1E1IfAnsiArchiveIntervalLineStatsSES,
       "dsxT1E1IfAttStatsGroup": dsxT1E1IfAttStatsGroup,
       "dsxT1E1IfAttCurrentStatsTable": dsxT1E1IfAttCurrentStatsTable,
       "dsxT1E1IfAttCurrentStatsEntry": dsxT1E1IfAttCurrentStatsEntry,
       "dsxT1E1IfAttCurrentStatsUASState": dsxT1E1IfAttCurrentStatsUASState,
       "dsxT1E1IfAttCurrentStatsTimeInCurrent": dsxT1E1IfAttCurrentStatsTimeInCurrent,
       "dsxT1E1IfAttCurrentStatsEEV": dsxT1E1IfAttCurrentStatsEEV,
       "dsxT1E1IfAttCurrentStatsES": dsxT1E1IfAttCurrentStatsES,
       "dsxT1E1IfAttCurrentStatsUAS": dsxT1E1IfAttCurrentStatsUAS,
       "dsxT1E1IfAttCurrentStatsBES": dsxT1E1IfAttCurrentStatsBES,
       "dsxT1E1IfAttCurrentStatsSES": dsxT1E1IfAttCurrentStatsSES,
       "dsxT1E1IfAttCurrentStatsLOFC": dsxT1E1IfAttCurrentStatsLOFC,
       "dsxT1E1IfAttCurrentStatsCSS": dsxT1E1IfAttCurrentStatsCSS,
       "dsxT1E1IfAttTotalStatsTable": dsxT1E1IfAttTotalStatsTable,
       "dsxT1E1IfAttTotalStatsEntry": dsxT1E1IfAttTotalStatsEntry,
       "dsxT1E1IfAttTotalStatsEEV": dsxT1E1IfAttTotalStatsEEV,
       "dsxT1E1IfAttTotalStatsES": dsxT1E1IfAttTotalStatsES,
       "dsxT1E1IfAttTotalStatsUAS": dsxT1E1IfAttTotalStatsUAS,
       "dsxT1E1IfAttTotalStatsBES": dsxT1E1IfAttTotalStatsBES,
       "dsxT1E1IfAttTotalStatsSES": dsxT1E1IfAttTotalStatsSES,
       "dsxT1E1IfAttTotalStatsLOFC": dsxT1E1IfAttTotalStatsLOFC,
       "dsxT1E1IfAttTotalStatsCSS": dsxT1E1IfAttTotalStatsCSS,
       "dsxT1E1IfAttArchiveStatsTable": dsxT1E1IfAttArchiveStatsTable,
       "dsxT1E1IfAttArchiveStatsEntry": dsxT1E1IfAttArchiveStatsEntry,
       "dsxT1E1IfAttArchiveInterval": dsxT1E1IfAttArchiveInterval,
       "dsxT1E1IfAttArchiveStatsEEV": dsxT1E1IfAttArchiveStatsEEV,
       "dsxT1E1IfAttArchiveStatsES": dsxT1E1IfAttArchiveStatsES,
       "dsxT1E1IfAttArchiveStatsUAS": dsxT1E1IfAttArchiveStatsUAS,
       "dsxT1E1IfAttArchiveStatsBES": dsxT1E1IfAttArchiveStatsBES,
       "dsxT1E1IfAttArchiveStatsSES": dsxT1E1IfAttArchiveStatsSES,
       "dsxT1E1IfAttArchiveStatsLOFC": dsxT1E1IfAttArchiveStatsLOFC,
       "dsxT1E1IfAttArchiveStatsCSS": dsxT1E1IfAttArchiveStatsCSS,
       "dsxT1E1IfIetfStatsGroup": dsxT1E1IfIetfStatsGroup,
       "dsxT1E1IfIetfCurrentStatsTable": dsxT1E1IfIetfCurrentStatsTable,
       "dsxT1E1IfIetfCurrentStatsEntry": dsxT1E1IfIetfCurrentStatsEntry,
       "dsxT1E1IfIetfCurrentStatsUASState": dsxT1E1IfIetfCurrentStatsUASState,
       "dsxT1E1IfIetfCurrentStatsTimeInCurrent": dsxT1E1IfIetfCurrentStatsTimeInCurrent,
       "dsxT1E1IfIetfCurrentStatsES": dsxT1E1IfIetfCurrentStatsES,
       "dsxT1E1IfIetfCurrentStatsSES": dsxT1E1IfIetfCurrentStatsSES,
       "dsxT1E1IfIetfCurrentStatsSEFS": dsxT1E1IfIetfCurrentStatsSEFS,
       "dsxT1E1IfIetfCurrentStatsUAS": dsxT1E1IfIetfCurrentStatsUAS,
       "dsxT1E1IfIetfCurrentStatsCSS": dsxT1E1IfIetfCurrentStatsCSS,
       "dsxT1E1IfIetfCurrentStatsPCV": dsxT1E1IfIetfCurrentStatsPCV,
       "dsxT1E1IfIetfCurrentStatsLES": dsxT1E1IfIetfCurrentStatsLES,
       "dsxT1E1IfIetfCurrentStatsBES": dsxT1E1IfIetfCurrentStatsBES,
       "dsxT1E1IfIetfCurrentStatsDM": dsxT1E1IfIetfCurrentStatsDM,
       "dsxT1E1IfIetfCurrentStatsLCV": dsxT1E1IfIetfCurrentStatsLCV,
       "dsxT1E1IfIetfTotalStatsTable": dsxT1E1IfIetfTotalStatsTable,
       "dsxT1E1IfIetfTotalStatsEntry": dsxT1E1IfIetfTotalStatsEntry,
       "dsxT1E1IfIetfTotalStatsES": dsxT1E1IfIetfTotalStatsES,
       "dsxT1E1IfIetfTotalStatsSES": dsxT1E1IfIetfTotalStatsSES,
       "dsxT1E1IfIetfTotalStatsSEFS": dsxT1E1IfIetfTotalStatsSEFS,
       "dsxT1E1IfIetfTotalStatsUAS": dsxT1E1IfIetfTotalStatsUAS,
       "dsxT1E1IfIetfTotalStatsCSS": dsxT1E1IfIetfTotalStatsCSS,
       "dsxT1E1IfIetfTotalStatsPCV": dsxT1E1IfIetfTotalStatsPCV,
       "dsxT1E1IfIetfTotalStatsLES": dsxT1E1IfIetfTotalStatsLES,
       "dsxT1E1IfIetfTotalStatsBES": dsxT1E1IfIetfTotalStatsBES,
       "dsxT1E1IfIetfTotalStatsDM": dsxT1E1IfIetfTotalStatsDM,
       "dsxT1E1IfIetfTotalStatsLCV": dsxT1E1IfIetfTotalStatsLCV,
       "dsxT1E1IfIetfArchiveStatsTable": dsxT1E1IfIetfArchiveStatsTable,
       "dsxT1E1IfIetfArchiveStatsEntry": dsxT1E1IfIetfArchiveStatsEntry,
       "dsxT1E1IfIetfArchiveStatsInterval": dsxT1E1IfIetfArchiveStatsInterval,
       "dsxT1E1IfIetfArchiveStatsES": dsxT1E1IfIetfArchiveStatsES,
       "dsxT1E1IfIetfArchiveStatsSES": dsxT1E1IfIetfArchiveStatsSES,
       "dsxT1E1IfIetfArchiveStatsSEFS": dsxT1E1IfIetfArchiveStatsSEFS,
       "dsxT1E1IfIetfArchiveStatsUAS": dsxT1E1IfIetfArchiveStatsUAS,
       "dsxT1E1IfIetfArchiveStatsCSS": dsxT1E1IfIetfArchiveStatsCSS,
       "dsxT1E1IfIetfArchiveStatsPCV": dsxT1E1IfIetfArchiveStatsPCV,
       "dsxT1E1IfIetfArchiveStatsLES": dsxT1E1IfIetfArchiveStatsLES,
       "dsxT1E1IfIetfArchiveStatsBES": dsxT1E1IfIetfArchiveStatsBES,
       "dsxT1E1IfIetfArchiveStatsDM": dsxT1E1IfIetfArchiveStatsDM,
       "dsxT1E1IfIetfArchiveStatsLCV": dsxT1E1IfIetfArchiveStatsLCV,
       "dsxT1E1IfUserStatsGroup": dsxT1E1IfUserStatsGroup,
       "dsxT1E1IfUserCurrentStatsTable": dsxT1E1IfUserCurrentStatsTable,
       "dsxT1E1IfUserCurrentStatsEntry": dsxT1E1IfUserCurrentStatsEntry,
       "dsxT1E1IfUserCurrentStatsUASState": dsxT1E1IfUserCurrentStatsUASState,
       "dsxT1E1IfUserCurrentStatsTimeInCurrent": dsxT1E1IfUserCurrentStatsTimeInCurrent,
       "dsxT1E1IfUserCurrentStatsEEV": dsxT1E1IfUserCurrentStatsEEV,
       "dsxT1E1IfUserCurrentStatsES": dsxT1E1IfUserCurrentStatsES,
       "dsxT1E1IfUserCurrentStatsUAS": dsxT1E1IfUserCurrentStatsUAS,
       "dsxT1E1IfUserCurrentStatsBES": dsxT1E1IfUserCurrentStatsBES,
       "dsxT1E1IfUserCurrentStatsSES": dsxT1E1IfUserCurrentStatsSES,
       "dsxT1E1IfUserCurrentStatsLOFC": dsxT1E1IfUserCurrentStatsLOFC,
       "dsxT1E1IfUserCurrentStatsCSS": dsxT1E1IfUserCurrentStatsCSS,
       "dsxT1E1IfUserCurrentStatsBPV": dsxT1E1IfUserCurrentStatsBPV,
       "dsxT1E1IfUserCurrentStatsOOF": dsxT1E1IfUserCurrentStatsOOF,
       "dsxT1E1IfUserCurrentStatsCRC": dsxT1E1IfUserCurrentStatsCRC,
       "dsxT1E1IfUserTotalStatsTable": dsxT1E1IfUserTotalStatsTable,
       "dsxT1E1IfUserTotalStatsEntry": dsxT1E1IfUserTotalStatsEntry,
       "dsxT1E1IfUserTotalStatsDay": dsxT1E1IfUserTotalStatsDay,
       "dsxT1E1IfUserTotalStatsEEV": dsxT1E1IfUserTotalStatsEEV,
       "dsxT1E1IfUserTotalStatsES": dsxT1E1IfUserTotalStatsES,
       "dsxT1E1IfUserTotalStatsUAS": dsxT1E1IfUserTotalStatsUAS,
       "dsxT1E1IfUserTotalStatsBES": dsxT1E1IfUserTotalStatsBES,
       "dsxT1E1IfUserTotalStatsSES": dsxT1E1IfUserTotalStatsSES,
       "dsxT1E1IfUserTotalStatsLOFC": dsxT1E1IfUserTotalStatsLOFC,
       "dsxT1E1IfUserTotalStatsCSS": dsxT1E1IfUserTotalStatsCSS,
       "dsxT1E1IfUserTotalStatsBPV": dsxT1E1IfUserTotalStatsBPV,
       "dsxT1E1IfUserTotalStatsOOF": dsxT1E1IfUserTotalStatsOOF,
       "dsxT1E1IfUserTotalStatsCRC": dsxT1E1IfUserTotalStatsCRC,
       "dsxT1E1IfUserLifetimeStatsTable": dsxT1E1IfUserLifetimeStatsTable,
       "dsxT1E1IfUserLifetimeStatsEntry": dsxT1E1IfUserLifetimeStatsEntry,
       "dsxT1E1IfUserLifetimeStatsEEV": dsxT1E1IfUserLifetimeStatsEEV,
       "dsxT1E1IfUserLifetimeStatsES": dsxT1E1IfUserLifetimeStatsES,
       "dsxT1E1IfUserLifetimeStatsUAS": dsxT1E1IfUserLifetimeStatsUAS,
       "dsxT1E1IfUserLifetimeStatsBES": dsxT1E1IfUserLifetimeStatsBES,
       "dsxT1E1IfUserLifetimeStatsSES": dsxT1E1IfUserLifetimeStatsSES,
       "dsxT1E1IfUserLifetimeStatsLOFC": dsxT1E1IfUserLifetimeStatsLOFC,
       "dsxT1E1IfUserLifetimeStatsCSS": dsxT1E1IfUserLifetimeStatsCSS,
       "dsxT1E1IfUserLifetimeStatsBPV": dsxT1E1IfUserLifetimeStatsBPV,
       "dsxT1E1IfUserLifetimeStatsOOF": dsxT1E1IfUserLifetimeStatsOOF,
       "dsxT1E1IfUserLifetimeStatsCRC": dsxT1E1IfUserLifetimeStatsCRC,
       "dsxT1E1IfUserArchiveStatsTable": dsxT1E1IfUserArchiveStatsTable,
       "dsxT1E1IfUserArchiveStatsEntry": dsxT1E1IfUserArchiveStatsEntry,
       "dsxT1E1IfUserArchiveStatsInterval": dsxT1E1IfUserArchiveStatsInterval,
       "dsxT1E1IfUserArchiveStatsEEV": dsxT1E1IfUserArchiveStatsEEV,
       "dsxT1E1IfUserArchiveStatsES": dsxT1E1IfUserArchiveStatsES,
       "dsxT1E1IfUserArchiveStatsUAS": dsxT1E1IfUserArchiveStatsUAS,
       "dsxT1E1IfUserArchiveStatsBES": dsxT1E1IfUserArchiveStatsBES,
       "dsxT1E1IfUserArchiveStatsSES": dsxT1E1IfUserArchiveStatsSES,
       "dsxT1E1IfUserArchiveStatsLOFC": dsxT1E1IfUserArchiveStatsLOFC,
       "dsxT1E1IfUserArchiveStatsCSS": dsxT1E1IfUserArchiveStatsCSS,
       "dsxT1E1IfUserArchiveStatsBPV": dsxT1E1IfUserArchiveStatsBPV,
       "dsxT1E1IfUserArchiveStatsOOF": dsxT1E1IfUserArchiveStatsOOF,
       "dsxT1E1IfUserArchiveStatsCRC": dsxT1E1IfUserArchiveStatsCRC,
       "dsxT1E1Traps": dsxT1E1Traps,
       "dsxT1E1AlarmOnTrap": dsxT1E1AlarmOnTrap,
       "dsxT1E1AlarmOffTrap": dsxT1E1AlarmOffTrap,
       "dsxT1E1TrapVariables": dsxT1E1TrapVariables,
       "dsxT1E1Number": dsxT1E1Number,
       "dsxT1E1Type": dsxT1E1Type,
       "dsxT1E1T3Number": dsxT1E1T3Number,
       "dsxT1E1AlarmType": dsxT1E1AlarmType}
)
