# SNMP MIB module (ADSL-LINE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ADSL-LINE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:33:55 2024
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

(AdslLineCodingType,
 AdslPerfCurrDayCount,
 AdslPerfPrevDayCount,
 AdslPerfTimeElapsed) = mibBuilder.importSymbols(
    "ADSL-TC-MIB",
    "AdslLineCodingType",
    "AdslPerfCurrDayCount",
    "AdslPerfPrevDayCount",
    "AdslPerfTimeElapsed")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(PerfCurrentCount,
 PerfIntervalCount) = mibBuilder.importSymbols(
    "PerfHist-TC-MIB",
    "PerfCurrentCount",
    "PerfIntervalCount")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 iso,
 transmission) = mibBuilder.importSymbols(
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
    "iso",
    "transmission")

(DisplayString,
 RowStatus,
 TextualConvention,
 TruthValue,
 VariablePointer) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue",
    "VariablePointer")


# MODULE-IDENTITY

adslMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 10, 94)
)
adslMIB.setRevisions(
        ("1999-08-19 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AdslLineMib_ObjectIdentity = ObjectIdentity
adslLineMib = _AdslLineMib_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 94, 1)
)
_AdslMibObjects_ObjectIdentity = ObjectIdentity
adslMibObjects = _AdslMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1)
)
_AdslLineTable_Object = MibTable
adslLineTable = _AdslLineTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 1)
)
if mibBuilder.loadTexts:
    adslLineTable.setStatus("current")
_AdslLineEntry_Object = MibTableRow
adslLineEntry = _AdslLineEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 1, 1)
)
adslLineEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adslLineEntry.setStatus("current")
_AdslLineCoding_Type = AdslLineCodingType
_AdslLineCoding_Object = MibTableColumn
adslLineCoding = _AdslLineCoding_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 1, 1, 1),
    _AdslLineCoding_Type()
)
adslLineCoding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslLineCoding.setStatus("current")


class _AdslLineType_Type(Integer32):
    """Custom type adslLineType based on Integer32"""
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
        *(("fastAndInterleaved", 5),
          ("fastOnly", 2),
          ("fastOrInterleaved", 4),
          ("interleavedOnly", 3),
          ("noChannel", 1))
    )


_AdslLineType_Type.__name__ = "Integer32"
_AdslLineType_Object = MibTableColumn
adslLineType = _AdslLineType_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 1, 1, 2),
    _AdslLineType_Type()
)
adslLineType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslLineType.setStatus("current")
_AdslLineSpecific_Type = VariablePointer
_AdslLineSpecific_Object = MibTableColumn
adslLineSpecific = _AdslLineSpecific_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 1, 1, 3),
    _AdslLineSpecific_Type()
)
adslLineSpecific.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslLineSpecific.setStatus("current")


class _AdslLineConfProfile_Type(SnmpAdminString):
    """Custom type adslLineConfProfile based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AdslLineConfProfile_Type.__name__ = "SnmpAdminString"
_AdslLineConfProfile_Object = MibTableColumn
adslLineConfProfile = _AdslLineConfProfile_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 1, 1, 4),
    _AdslLineConfProfile_Type()
)
adslLineConfProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adslLineConfProfile.setStatus("current")


class _AdslLineAlarmConfProfile_Type(SnmpAdminString):
    """Custom type adslLineAlarmConfProfile based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AdslLineAlarmConfProfile_Type.__name__ = "SnmpAdminString"
_AdslLineAlarmConfProfile_Object = MibTableColumn
adslLineAlarmConfProfile = _AdslLineAlarmConfProfile_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 1, 1, 5),
    _AdslLineAlarmConfProfile_Type()
)
adslLineAlarmConfProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adslLineAlarmConfProfile.setStatus("current")
_AdslAtucPhysTable_Object = MibTable
adslAtucPhysTable = _AdslAtucPhysTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 2)
)
if mibBuilder.loadTexts:
    adslAtucPhysTable.setStatus("current")
_AdslAtucPhysEntry_Object = MibTableRow
adslAtucPhysEntry = _AdslAtucPhysEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 2, 1)
)
adslAtucPhysEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adslAtucPhysEntry.setStatus("current")


class _AdslAtucInvSerialNumber_Type(SnmpAdminString):
    """Custom type adslAtucInvSerialNumber based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AdslAtucInvSerialNumber_Type.__name__ = "SnmpAdminString"
_AdslAtucInvSerialNumber_Object = MibTableColumn
adslAtucInvSerialNumber = _AdslAtucInvSerialNumber_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 2, 1, 1),
    _AdslAtucInvSerialNumber_Type()
)
adslAtucInvSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAtucInvSerialNumber.setStatus("current")


class _AdslAtucInvVendorID_Type(SnmpAdminString):
    """Custom type adslAtucInvVendorID based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_AdslAtucInvVendorID_Type.__name__ = "SnmpAdminString"
_AdslAtucInvVendorID_Object = MibTableColumn
adslAtucInvVendorID = _AdslAtucInvVendorID_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 2, 1, 2),
    _AdslAtucInvVendorID_Type()
)
adslAtucInvVendorID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAtucInvVendorID.setStatus("current")


class _AdslAtucInvVersionNumber_Type(SnmpAdminString):
    """Custom type adslAtucInvVersionNumber based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_AdslAtucInvVersionNumber_Type.__name__ = "SnmpAdminString"
_AdslAtucInvVersionNumber_Object = MibTableColumn
adslAtucInvVersionNumber = _AdslAtucInvVersionNumber_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 2, 1, 3),
    _AdslAtucInvVersionNumber_Type()
)
adslAtucInvVersionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAtucInvVersionNumber.setStatus("current")


class _AdslAtucCurrSnrMgn_Type(Integer32):
    """Custom type adslAtucCurrSnrMgn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-640, 640),
    )


_AdslAtucCurrSnrMgn_Type.__name__ = "Integer32"
_AdslAtucCurrSnrMgn_Object = MibTableColumn
adslAtucCurrSnrMgn = _AdslAtucCurrSnrMgn_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 2, 1, 4),
    _AdslAtucCurrSnrMgn_Type()
)
adslAtucCurrSnrMgn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAtucCurrSnrMgn.setStatus("current")
if mibBuilder.loadTexts:
    adslAtucCurrSnrMgn.setUnits("tenth dB")


class _AdslAtucCurrAtn_Type(Gauge32):
    """Custom type adslAtucCurrAtn based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 630),
    )


_AdslAtucCurrAtn_Type.__name__ = "Gauge32"
_AdslAtucCurrAtn_Object = MibTableColumn
adslAtucCurrAtn = _AdslAtucCurrAtn_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 2, 1, 5),
    _AdslAtucCurrAtn_Type()
)
adslAtucCurrAtn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAtucCurrAtn.setStatus("current")
if mibBuilder.loadTexts:
    adslAtucCurrAtn.setUnits("tenth dB")


class _AdslAtucCurrStatus_Type(Bits):
    """Custom type adslAtucCurrStatus based on Bits"""
    namedValues = NamedValues(
        *(("configInitFailure", 7),
          ("dataInitFailure", 6),
          ("lossOfFraming", 1),
          ("lossOfLink", 5),
          ("lossOfPower", 3),
          ("lossOfSignal", 2),
          ("lossOfSignalQuality", 4),
          ("noDefect", 0),
          ("noPeerAtuPresent", 9),
          ("protocolInitFailure", 8))
    )

_AdslAtucCurrStatus_Type.__name__ = "Bits"
_AdslAtucCurrStatus_Object = MibTableColumn
adslAtucCurrStatus = _AdslAtucCurrStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 2, 1, 6),
    _AdslAtucCurrStatus_Type()
)
adslAtucCurrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAtucCurrStatus.setStatus("current")


class _AdslAtucCurrOutputPwr_Type(Integer32):
    """Custom type adslAtucCurrOutputPwr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-310, 310),
    )


_AdslAtucCurrOutputPwr_Type.__name__ = "Integer32"
_AdslAtucCurrOutputPwr_Object = MibTableColumn
adslAtucCurrOutputPwr = _AdslAtucCurrOutputPwr_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 2, 1, 7),
    _AdslAtucCurrOutputPwr_Type()
)
adslAtucCurrOutputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAtucCurrOutputPwr.setStatus("current")
if mibBuilder.loadTexts:
    adslAtucCurrOutputPwr.setUnits("tenth dBm")
_AdslAtucCurrAttainableRate_Type = Gauge32
_AdslAtucCurrAttainableRate_Object = MibTableColumn
adslAtucCurrAttainableRate = _AdslAtucCurrAttainableRate_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 2, 1, 8),
    _AdslAtucCurrAttainableRate_Type()
)
adslAtucCurrAttainableRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAtucCurrAttainableRate.setStatus("current")
if mibBuilder.loadTexts:
    adslAtucCurrAttainableRate.setUnits("bps")
_AdslAturPhysTable_Object = MibTable
adslAturPhysTable = _AdslAturPhysTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 3)
)
if mibBuilder.loadTexts:
    adslAturPhysTable.setStatus("current")
_AdslAturPhysEntry_Object = MibTableRow
adslAturPhysEntry = _AdslAturPhysEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 3, 1)
)
adslAturPhysEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adslAturPhysEntry.setStatus("current")


class _AdslAturInvSerialNumber_Type(SnmpAdminString):
    """Custom type adslAturInvSerialNumber based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AdslAturInvSerialNumber_Type.__name__ = "SnmpAdminString"
_AdslAturInvSerialNumber_Object = MibTableColumn
adslAturInvSerialNumber = _AdslAturInvSerialNumber_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 3, 1, 1),
    _AdslAturInvSerialNumber_Type()
)
adslAturInvSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAturInvSerialNumber.setStatus("current")


class _AdslAturInvVendorID_Type(SnmpAdminString):
    """Custom type adslAturInvVendorID based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_AdslAturInvVendorID_Type.__name__ = "SnmpAdminString"
_AdslAturInvVendorID_Object = MibTableColumn
adslAturInvVendorID = _AdslAturInvVendorID_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 3, 1, 2),
    _AdslAturInvVendorID_Type()
)
adslAturInvVendorID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAturInvVendorID.setStatus("current")


class _AdslAturInvVersionNumber_Type(SnmpAdminString):
    """Custom type adslAturInvVersionNumber based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_AdslAturInvVersionNumber_Type.__name__ = "SnmpAdminString"
_AdslAturInvVersionNumber_Object = MibTableColumn
adslAturInvVersionNumber = _AdslAturInvVersionNumber_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 3, 1, 3),
    _AdslAturInvVersionNumber_Type()
)
adslAturInvVersionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAturInvVersionNumber.setStatus("current")


class _AdslAturCurrSnrMgn_Type(Integer32):
    """Custom type adslAturCurrSnrMgn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-640, 640),
    )


_AdslAturCurrSnrMgn_Type.__name__ = "Integer32"
_AdslAturCurrSnrMgn_Object = MibTableColumn
adslAturCurrSnrMgn = _AdslAturCurrSnrMgn_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 3, 1, 4),
    _AdslAturCurrSnrMgn_Type()
)
adslAturCurrSnrMgn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAturCurrSnrMgn.setStatus("current")
if mibBuilder.loadTexts:
    adslAturCurrSnrMgn.setUnits("tenth dB")


class _AdslAturCurrAtn_Type(Gauge32):
    """Custom type adslAturCurrAtn based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 630),
    )


_AdslAturCurrAtn_Type.__name__ = "Gauge32"
_AdslAturCurrAtn_Object = MibTableColumn
adslAturCurrAtn = _AdslAturCurrAtn_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 3, 1, 5),
    _AdslAturCurrAtn_Type()
)
adslAturCurrAtn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAturCurrAtn.setStatus("current")
if mibBuilder.loadTexts:
    adslAturCurrAtn.setUnits("tenth dB")


class _AdslAturCurrStatus_Type(Bits):
    """Custom type adslAturCurrStatus based on Bits"""
    namedValues = NamedValues(
        *(("lossOfFraming", 1),
          ("lossOfPower", 3),
          ("lossOfSignal", 2),
          ("lossOfSignalQuality", 4),
          ("noDefect", 0))
    )

_AdslAturCurrStatus_Type.__name__ = "Bits"
_AdslAturCurrStatus_Object = MibTableColumn
adslAturCurrStatus = _AdslAturCurrStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 3, 1, 6),
    _AdslAturCurrStatus_Type()
)
adslAturCurrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAturCurrStatus.setStatus("current")


class _AdslAturCurrOutputPwr_Type(Integer32):
    """Custom type adslAturCurrOutputPwr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-310, 310),
    )


_AdslAturCurrOutputPwr_Type.__name__ = "Integer32"
_AdslAturCurrOutputPwr_Object = MibTableColumn
adslAturCurrOutputPwr = _AdslAturCurrOutputPwr_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 3, 1, 7),
    _AdslAturCurrOutputPwr_Type()
)
adslAturCurrOutputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAturCurrOutputPwr.setStatus("current")
if mibBuilder.loadTexts:
    adslAturCurrOutputPwr.setUnits("tenth dBm")
_AdslAturCurrAttainableRate_Type = Gauge32
_AdslAturCurrAttainableRate_Object = MibTableColumn
adslAturCurrAttainableRate = _AdslAturCurrAttainableRate_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 3, 1, 8),
    _AdslAturCurrAttainableRate_Type()
)
adslAturCurrAttainableRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAturCurrAttainableRate.setStatus("current")
if mibBuilder.loadTexts:
    adslAturCurrAttainableRate.setUnits("bps")
_AdslAtucChanTable_Object = MibTable
adslAtucChanTable = _AdslAtucChanTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 4)
)
if mibBuilder.loadTexts:
    adslAtucChanTable.setStatus("current")
_AdslAtucChanEntry_Object = MibTableRow
adslAtucChanEntry = _AdslAtucChanEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 4, 1)
)
adslAtucChanEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adslAtucChanEntry.setStatus("current")
_AdslAtucChanInterleaveDelay_Type = Gauge32
_AdslAtucChanInterleaveDelay_Object = MibTableColumn
adslAtucChanInterleaveDelay = _AdslAtucChanInterleaveDelay_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 4, 1, 1),
    _AdslAtucChanInterleaveDelay_Type()
)
adslAtucChanInterleaveDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAtucChanInterleaveDelay.setStatus("current")
if mibBuilder.loadTexts:
    adslAtucChanInterleaveDelay.setUnits("milli-seconds")
_AdslAtucChanCurrTxRate_Type = Gauge32
_AdslAtucChanCurrTxRate_Object = MibTableColumn
adslAtucChanCurrTxRate = _AdslAtucChanCurrTxRate_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 4, 1, 2),
    _AdslAtucChanCurrTxRate_Type()
)
adslAtucChanCurrTxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAtucChanCurrTxRate.setStatus("current")
if mibBuilder.loadTexts:
    adslAtucChanCurrTxRate.setUnits("bps")
_AdslAtucChanPrevTxRate_Type = Gauge32
_AdslAtucChanPrevTxRate_Object = MibTableColumn
adslAtucChanPrevTxRate = _AdslAtucChanPrevTxRate_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 4, 1, 3),
    _AdslAtucChanPrevTxRate_Type()
)
adslAtucChanPrevTxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAtucChanPrevTxRate.setStatus("current")
if mibBuilder.loadTexts:
    adslAtucChanPrevTxRate.setUnits("bps")
_AdslAtucChanCrcBlockLength_Type = Gauge32
_AdslAtucChanCrcBlockLength_Object = MibTableColumn
adslAtucChanCrcBlockLength = _AdslAtucChanCrcBlockLength_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 4, 1, 4),
    _AdslAtucChanCrcBlockLength_Type()
)
adslAtucChanCrcBlockLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAtucChanCrcBlockLength.setStatus("current")
if mibBuilder.loadTexts:
    adslAtucChanCrcBlockLength.setUnits("byte")
_AdslAturChanTable_Object = MibTable
adslAturChanTable = _AdslAturChanTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 5)
)
if mibBuilder.loadTexts:
    adslAturChanTable.setStatus("current")
_AdslAturChanEntry_Object = MibTableRow
adslAturChanEntry = _AdslAturChanEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 5, 1)
)
adslAturChanEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adslAturChanEntry.setStatus("current")
_AdslAturChanInterleaveDelay_Type = Gauge32
_AdslAturChanInterleaveDelay_Object = MibTableColumn
adslAturChanInterleaveDelay = _AdslAturChanInterleaveDelay_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 5, 1, 1),
    _AdslAturChanInterleaveDelay_Type()
)
adslAturChanInterleaveDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAturChanInterleaveDelay.setStatus("current")
if mibBuilder.loadTexts:
    adslAturChanInterleaveDelay.setUnits("milli-seconds")
_AdslAturChanCurrTxRate_Type = Gauge32
_AdslAturChanCurrTxRate_Object = MibTableColumn
adslAturChanCurrTxRate = _AdslAturChanCurrTxRate_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 5, 1, 2),
    _AdslAturChanCurrTxRate_Type()
)
adslAturChanCurrTxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAturChanCurrTxRate.setStatus("current")
if mibBuilder.loadTexts:
    adslAturChanCurrTxRate.setUnits("bps")
_AdslAturChanPrevTxRate_Type = Gauge32
_AdslAturChanPrevTxRate_Object = MibTableColumn
adslAturChanPrevTxRate = _AdslAturChanPrevTxRate_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 5, 1, 3),
    _AdslAturChanPrevTxRate_Type()
)
adslAturChanPrevTxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAturChanPrevTxRate.setStatus("current")
if mibBuilder.loadTexts:
    adslAturChanPrevTxRate.setUnits("bps")
_AdslAturChanCrcBlockLength_Type = Gauge32
_AdslAturChanCrcBlockLength_Object = MibTableColumn
adslAturChanCrcBlockLength = _AdslAturChanCrcBlockLength_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 5, 1, 4),
    _AdslAturChanCrcBlockLength_Type()
)
adslAturChanCrcBlockLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAturChanCrcBlockLength.setStatus("current")
_AdslAtucPerfDataTable_Object = MibTable
adslAtucPerfDataTable = _AdslAtucPerfDataTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 6)
)
if mibBuilder.loadTexts:
    adslAtucPerfDataTable.setStatus("current")
_AdslAtucPerfDataEntry_Object = MibTableRow
adslAtucPerfDataEntry = _AdslAtucPerfDataEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 6, 1)
)
adslAtucPerfDataEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adslAtucPerfDataEntry.setStatus("current")
_AdslAtucPerfLofs_Type = Counter32
_AdslAtucPerfLofs_Object = MibTableColumn
adslAtucPerfLofs = _AdslAtucPerfLofs_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 6, 1, 1),
    _AdslAtucPerfLofs_Type()
)
adslAtucPerfLofs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAtucPerfLofs.setStatus("current")
_AdslAtucPerfLoss_Type = Counter32
_AdslAtucPerfLoss_Object = MibTableColumn
adslAtucPerfLoss = _AdslAtucPerfLoss_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 6, 1, 2),
    _AdslAtucPerfLoss_Type()
)
adslAtucPerfLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAtucPerfLoss.setStatus("current")
_AdslAtucPerfLols_Type = Counter32
_AdslAtucPerfLols_Object = MibTableColumn
adslAtucPerfLols = _AdslAtucPerfLols_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 6, 1, 3),
    _AdslAtucPerfLols_Type()
)
adslAtucPerfLols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAtucPerfLols.setStatus("current")
_AdslAtucPerfLprs_Type = Counter32
_AdslAtucPerfLprs_Object = MibTableColumn
adslAtucPerfLprs = _AdslAtucPerfLprs_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 6, 1, 4),
    _AdslAtucPerfLprs_Type()
)
adslAtucPerfLprs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAtucPerfLprs.setStatus("current")
_AdslAtucPerfESs_Type = Counter32
_AdslAtucPerfESs_Object = MibTableColumn
adslAtucPerfESs = _AdslAtucPerfESs_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 6, 1, 5),
    _AdslAtucPerfESs_Type()
)
adslAtucPerfESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAtucPerfESs.setStatus("current")
_AdslAtucPerfInits_Type = Counter32
_AdslAtucPerfInits_Object = MibTableColumn
adslAtucPerfInits = _AdslAtucPerfInits_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 6, 1, 6),
    _AdslAtucPerfInits_Type()
)
adslAtucPerfInits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAtucPerfInits.setStatus("current")


class _AdslAtucPerfValidIntervals_Type(Integer32):
    """Custom type adslAtucPerfValidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_AdslAtucPerfValidIntervals_Type.__name__ = "Integer32"
_AdslAtucPerfValidIntervals_Object = MibTableColumn
adslAtucPerfValidIntervals = _AdslAtucPerfValidIntervals_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 6, 1, 7),
    _AdslAtucPerfValidIntervals_Type()
)
adslAtucPerfValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAtucPerfValidIntervals.setStatus("current")


class _AdslAtucPerfInvalidIntervals_Type(Integer32):
    """Custom type adslAtucPerfInvalidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_AdslAtucPerfInvalidIntervals_Type.__name__ = "Integer32"
_AdslAtucPerfInvalidIntervals_Object = MibTableColumn
adslAtucPerfInvalidIntervals = _AdslAtucPerfInvalidIntervals_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 6, 1, 8),
    _AdslAtucPerfInvalidIntervals_Type()
)
adslAtucPerfInvalidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAtucPerfInvalidIntervals.setStatus("current")


class _AdslAtucPerfCurr15MinTimeElapsed_Type(AdslPerfTimeElapsed):
    """Custom type adslAtucPerfCurr15MinTimeElapsed based on AdslPerfTimeElapsed"""
    subtypeSpec = AdslPerfTimeElapsed.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 899),
    )


_AdslAtucPerfCurr15MinTimeElapsed_Type.__name__ = "AdslPerfTimeElapsed"
_AdslAtucPerfCurr15MinTimeElapsed_Object = MibTableColumn
adslAtucPerfCurr15MinTimeElapsed = _AdslAtucPerfCurr15MinTimeElapsed_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 6, 1, 9),
    _AdslAtucPerfCurr15MinTimeElapsed_Type()
)
adslAtucPerfCurr15MinTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAtucPerfCurr15MinTimeElapsed.setStatus("current")
if mibBuilder.loadTexts:
    adslAtucPerfCurr15MinTimeElapsed.setUnits("seconds")
_AdslAtucPerfCurr15MinLofs_Type = PerfCurrentCount
_AdslAtucPerfCurr15MinLofs_Object = MibTableColumn
adslAtucPerfCurr15MinLofs = _AdslAtucPerfCurr15MinLofs_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 6, 1, 10),
    _AdslAtucPerfCurr15MinLofs_Type()
)
adslAtucPerfCurr15MinLofs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAtucPerfCurr15MinLofs.setStatus("current")
if mibBuilder.loadTexts:
    adslAtucPerfCurr15MinLofs.setUnits("seconds")
_AdslAtucPerfCurr15MinLoss_Type = PerfCurrentCount
_AdslAtucPerfCurr15MinLoss_Object = MibTableColumn
adslAtucPerfCurr15MinLoss = _AdslAtucPerfCurr15MinLoss_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 6, 1, 11),
    _AdslAtucPerfCurr15MinLoss_Type()
)
adslAtucPerfCurr15MinLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAtucPerfCurr15MinLoss.setStatus("current")
if mibBuilder.loadTexts:
    adslAtucPerfCurr15MinLoss.setUnits("seconds")
_AdslAtucPerfCurr15MinLols_Type = PerfCurrentCount
_AdslAtucPerfCurr15MinLols_Object = MibTableColumn
adslAtucPerfCurr15MinLols = _AdslAtucPerfCurr15MinLols_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 6, 1, 12),
    _AdslAtucPerfCurr15MinLols_Type()
)
adslAtucPerfCurr15MinLols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAtucPerfCurr15MinLols.setStatus("current")
if mibBuilder.loadTexts:
    adslAtucPerfCurr15MinLols.setUnits("seconds")
_AdslAtucPerfCurr15MinLprs_Type = PerfCurrentCount
_AdslAtucPerfCurr15MinLprs_Object = MibTableColumn
adslAtucPerfCurr15MinLprs = _AdslAtucPerfCurr15MinLprs_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 6, 1, 13),
    _AdslAtucPerfCurr15MinLprs_Type()
)
adslAtucPerfCurr15MinLprs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAtucPerfCurr15MinLprs.setStatus("current")
if mibBuilder.loadTexts:
    adslAtucPerfCurr15MinLprs.setUnits("seconds")
_AdslAtucPerfCurr15MinESs_Type = PerfCurrentCount
_AdslAtucPerfCurr15MinESs_Object = MibTableColumn
adslAtucPerfCurr15MinESs = _AdslAtucPerfCurr15MinESs_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 6, 1, 14),
    _AdslAtucPerfCurr15MinESs_Type()
)
adslAtucPerfCurr15MinESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAtucPerfCurr15MinESs.setStatus("current")
if mibBuilder.loadTexts:
    adslAtucPerfCurr15MinESs.setUnits("seconds")
_AdslAtucPerfCurr15MinInits_Type = PerfCurrentCount
_AdslAtucPerfCurr15MinInits_Object = MibTableColumn
adslAtucPerfCurr15MinInits = _AdslAtucPerfCurr15MinInits_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 6, 1, 15),
    _AdslAtucPerfCurr15MinInits_Type()
)
adslAtucPerfCurr15MinInits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAtucPerfCurr15MinInits.setStatus("current")


class _AdslAtucPerfCurr1DayTimeElapsed_Type(AdslPerfTimeElapsed):
    """Custom type adslAtucPerfCurr1DayTimeElapsed based on AdslPerfTimeElapsed"""
    subtypeSpec = AdslPerfTimeElapsed.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86399),
    )


_AdslAtucPerfCurr1DayTimeElapsed_Type.__name__ = "AdslPerfTimeElapsed"
_AdslAtucPerfCurr1DayTimeElapsed_Object = MibTableColumn
adslAtucPerfCurr1DayTimeElapsed = _AdslAtucPerfCurr1DayTimeElapsed_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 6, 1, 16),
    _AdslAtucPerfCurr1DayTimeElapsed_Type()
)
adslAtucPerfCurr1DayTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAtucPerfCurr1DayTimeElapsed.setStatus("current")
if mibBuilder.loadTexts:
    adslAtucPerfCurr1DayTimeElapsed.setUnits("seconds")
_AdslAtucPerfCurr1DayLofs_Type = AdslPerfCurrDayCount
_AdslAtucPerfCurr1DayLofs_Object = MibTableColumn
adslAtucPerfCurr1DayLofs = _AdslAtucPerfCurr1DayLofs_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 6, 1, 17),
    _AdslAtucPerfCurr1DayLofs_Type()
)
adslAtucPerfCurr1DayLofs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAtucPerfCurr1DayLofs.setStatus("current")
if mibBuilder.loadTexts:
    adslAtucPerfCurr1DayLofs.setUnits("seconds")
_AdslAtucPerfCurr1DayLoss_Type = AdslPerfCurrDayCount
_AdslAtucPerfCurr1DayLoss_Object = MibTableColumn
adslAtucPerfCurr1DayLoss = _AdslAtucPerfCurr1DayLoss_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 6, 1, 18),
    _AdslAtucPerfCurr1DayLoss_Type()
)
adslAtucPerfCurr1DayLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAtucPerfCurr1DayLoss.setStatus("current")
if mibBuilder.loadTexts:
    adslAtucPerfCurr1DayLoss.setUnits("seconds")
_AdslAtucPerfCurr1DayLols_Type = AdslPerfCurrDayCount
_AdslAtucPerfCurr1DayLols_Object = MibTableColumn
adslAtucPerfCurr1DayLols = _AdslAtucPerfCurr1DayLols_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 6, 1, 19),
    _AdslAtucPerfCurr1DayLols_Type()
)
adslAtucPerfCurr1DayLols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAtucPerfCurr1DayLols.setStatus("current")
if mibBuilder.loadTexts:
    adslAtucPerfCurr1DayLols.setUnits("seconds")
_AdslAtucPerfCurr1DayLprs_Type = AdslPerfCurrDayCount
_AdslAtucPerfCurr1DayLprs_Object = MibTableColumn
adslAtucPerfCurr1DayLprs = _AdslAtucPerfCurr1DayLprs_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 6, 1, 20),
    _AdslAtucPerfCurr1DayLprs_Type()
)
adslAtucPerfCurr1DayLprs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAtucPerfCurr1DayLprs.setStatus("current")
if mibBuilder.loadTexts:
    adslAtucPerfCurr1DayLprs.setUnits("seconds")
_AdslAtucPerfCurr1DayESs_Type = AdslPerfCurrDayCount
_AdslAtucPerfCurr1DayESs_Object = MibTableColumn
adslAtucPerfCurr1DayESs = _AdslAtucPerfCurr1DayESs_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 6, 1, 21),
    _AdslAtucPerfCurr1DayESs_Type()
)
adslAtucPerfCurr1DayESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAtucPerfCurr1DayESs.setStatus("current")
if mibBuilder.loadTexts:
    adslAtucPerfCurr1DayESs.setUnits("seconds")
_AdslAtucPerfCurr1DayInits_Type = AdslPerfCurrDayCount
_AdslAtucPerfCurr1DayInits_Object = MibTableColumn
adslAtucPerfCurr1DayInits = _AdslAtucPerfCurr1DayInits_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 6, 1, 22),
    _AdslAtucPerfCurr1DayInits_Type()
)
adslAtucPerfCurr1DayInits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAtucPerfCurr1DayInits.setStatus("current")


class _AdslAtucPerfPrev1DayMoniSecs_Type(Integer32):
    """Custom type adslAtucPerfPrev1DayMoniSecs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_AdslAtucPerfPrev1DayMoniSecs_Type.__name__ = "Integer32"
_AdslAtucPerfPrev1DayMoniSecs_Object = MibTableColumn
adslAtucPerfPrev1DayMoniSecs = _AdslAtucPerfPrev1DayMoniSecs_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 6, 1, 23),
    _AdslAtucPerfPrev1DayMoniSecs_Type()
)
adslAtucPerfPrev1DayMoniSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAtucPerfPrev1DayMoniSecs.setStatus("current")
if mibBuilder.loadTexts:
    adslAtucPerfPrev1DayMoniSecs.setUnits("seconds")
_AdslAtucPerfPrev1DayLofs_Type = AdslPerfPrevDayCount
_AdslAtucPerfPrev1DayLofs_Object = MibTableColumn
adslAtucPerfPrev1DayLofs = _AdslAtucPerfPrev1DayLofs_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 6, 1, 24),
    _AdslAtucPerfPrev1DayLofs_Type()
)
adslAtucPerfPrev1DayLofs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAtucPerfPrev1DayLofs.setStatus("current")
if mibBuilder.loadTexts:
    adslAtucPerfPrev1DayLofs.setUnits("seconds")
_AdslAtucPerfPrev1DayLoss_Type = AdslPerfPrevDayCount
_AdslAtucPerfPrev1DayLoss_Object = MibTableColumn
adslAtucPerfPrev1DayLoss = _AdslAtucPerfPrev1DayLoss_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 6, 1, 25),
    _AdslAtucPerfPrev1DayLoss_Type()
)
adslAtucPerfPrev1DayLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAtucPerfPrev1DayLoss.setStatus("current")
if mibBuilder.loadTexts:
    adslAtucPerfPrev1DayLoss.setUnits("seconds")
_AdslAtucPerfPrev1DayLols_Type = AdslPerfPrevDayCount
_AdslAtucPerfPrev1DayLols_Object = MibTableColumn
adslAtucPerfPrev1DayLols = _AdslAtucPerfPrev1DayLols_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 6, 1, 26),
    _AdslAtucPerfPrev1DayLols_Type()
)
adslAtucPerfPrev1DayLols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAtucPerfPrev1DayLols.setStatus("current")
if mibBuilder.loadTexts:
    adslAtucPerfPrev1DayLols.setUnits("seconds")
_AdslAtucPerfPrev1DayLprs_Type = AdslPerfPrevDayCount
_AdslAtucPerfPrev1DayLprs_Object = MibTableColumn
adslAtucPerfPrev1DayLprs = _AdslAtucPerfPrev1DayLprs_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 6, 1, 27),
    _AdslAtucPerfPrev1DayLprs_Type()
)
adslAtucPerfPrev1DayLprs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAtucPerfPrev1DayLprs.setStatus("current")
if mibBuilder.loadTexts:
    adslAtucPerfPrev1DayLprs.setUnits("seconds")
_AdslAtucPerfPrev1DayESs_Type = AdslPerfPrevDayCount
_AdslAtucPerfPrev1DayESs_Object = MibTableColumn
adslAtucPerfPrev1DayESs = _AdslAtucPerfPrev1DayESs_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 6, 1, 28),
    _AdslAtucPerfPrev1DayESs_Type()
)
adslAtucPerfPrev1DayESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAtucPerfPrev1DayESs.setStatus("current")
if mibBuilder.loadTexts:
    adslAtucPerfPrev1DayESs.setUnits("seconds")
_AdslAtucPerfPrev1DayInits_Type = AdslPerfPrevDayCount
_AdslAtucPerfPrev1DayInits_Object = MibTableColumn
adslAtucPerfPrev1DayInits = _AdslAtucPerfPrev1DayInits_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 6, 1, 29),
    _AdslAtucPerfPrev1DayInits_Type()
)
adslAtucPerfPrev1DayInits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAtucPerfPrev1DayInits.setStatus("current")
_AdslAturPerfDataTable_Object = MibTable
adslAturPerfDataTable = _AdslAturPerfDataTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 7)
)
if mibBuilder.loadTexts:
    adslAturPerfDataTable.setStatus("current")
_AdslAturPerfDataEntry_Object = MibTableRow
adslAturPerfDataEntry = _AdslAturPerfDataEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 7, 1)
)
adslAturPerfDataEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adslAturPerfDataEntry.setStatus("current")
_AdslAturPerfLofs_Type = Counter32
_AdslAturPerfLofs_Object = MibTableColumn
adslAturPerfLofs = _AdslAturPerfLofs_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 7, 1, 1),
    _AdslAturPerfLofs_Type()
)
adslAturPerfLofs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAturPerfLofs.setStatus("current")
if mibBuilder.loadTexts:
    adslAturPerfLofs.setUnits("seconds")
_AdslAturPerfLoss_Type = Counter32
_AdslAturPerfLoss_Object = MibTableColumn
adslAturPerfLoss = _AdslAturPerfLoss_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 7, 1, 2),
    _AdslAturPerfLoss_Type()
)
adslAturPerfLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAturPerfLoss.setStatus("current")
if mibBuilder.loadTexts:
    adslAturPerfLoss.setUnits("seconds")
_AdslAturPerfLprs_Type = Counter32
_AdslAturPerfLprs_Object = MibTableColumn
adslAturPerfLprs = _AdslAturPerfLprs_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 7, 1, 3),
    _AdslAturPerfLprs_Type()
)
adslAturPerfLprs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAturPerfLprs.setStatus("current")
if mibBuilder.loadTexts:
    adslAturPerfLprs.setUnits("seconds")
_AdslAturPerfESs_Type = Counter32
_AdslAturPerfESs_Object = MibTableColumn
adslAturPerfESs = _AdslAturPerfESs_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 7, 1, 4),
    _AdslAturPerfESs_Type()
)
adslAturPerfESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAturPerfESs.setStatus("current")
if mibBuilder.loadTexts:
    adslAturPerfESs.setUnits("seconds")


class _AdslAturPerfValidIntervals_Type(Integer32):
    """Custom type adslAturPerfValidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_AdslAturPerfValidIntervals_Type.__name__ = "Integer32"
_AdslAturPerfValidIntervals_Object = MibTableColumn
adslAturPerfValidIntervals = _AdslAturPerfValidIntervals_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 7, 1, 5),
    _AdslAturPerfValidIntervals_Type()
)
adslAturPerfValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAturPerfValidIntervals.setStatus("current")


class _AdslAturPerfInvalidIntervals_Type(Integer32):
    """Custom type adslAturPerfInvalidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_AdslAturPerfInvalidIntervals_Type.__name__ = "Integer32"
_AdslAturPerfInvalidIntervals_Object = MibTableColumn
adslAturPerfInvalidIntervals = _AdslAturPerfInvalidIntervals_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 7, 1, 6),
    _AdslAturPerfInvalidIntervals_Type()
)
adslAturPerfInvalidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAturPerfInvalidIntervals.setStatus("current")


class _AdslAturPerfCurr15MinTimeElapsed_Type(AdslPerfTimeElapsed):
    """Custom type adslAturPerfCurr15MinTimeElapsed based on AdslPerfTimeElapsed"""
    subtypeSpec = AdslPerfTimeElapsed.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 899),
    )


_AdslAturPerfCurr15MinTimeElapsed_Type.__name__ = "AdslPerfTimeElapsed"
_AdslAturPerfCurr15MinTimeElapsed_Object = MibTableColumn
adslAturPerfCurr15MinTimeElapsed = _AdslAturPerfCurr15MinTimeElapsed_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 7, 1, 7),
    _AdslAturPerfCurr15MinTimeElapsed_Type()
)
adslAturPerfCurr15MinTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAturPerfCurr15MinTimeElapsed.setStatus("current")
if mibBuilder.loadTexts:
    adslAturPerfCurr15MinTimeElapsed.setUnits("seconds")
_AdslAturPerfCurr15MinLofs_Type = PerfCurrentCount
_AdslAturPerfCurr15MinLofs_Object = MibTableColumn
adslAturPerfCurr15MinLofs = _AdslAturPerfCurr15MinLofs_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 7, 1, 8),
    _AdslAturPerfCurr15MinLofs_Type()
)
adslAturPerfCurr15MinLofs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAturPerfCurr15MinLofs.setStatus("current")
if mibBuilder.loadTexts:
    adslAturPerfCurr15MinLofs.setUnits("seconds")
_AdslAturPerfCurr15MinLoss_Type = PerfCurrentCount
_AdslAturPerfCurr15MinLoss_Object = MibTableColumn
adslAturPerfCurr15MinLoss = _AdslAturPerfCurr15MinLoss_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 7, 1, 9),
    _AdslAturPerfCurr15MinLoss_Type()
)
adslAturPerfCurr15MinLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAturPerfCurr15MinLoss.setStatus("current")
if mibBuilder.loadTexts:
    adslAturPerfCurr15MinLoss.setUnits("seconds")
_AdslAturPerfCurr15MinLprs_Type = PerfCurrentCount
_AdslAturPerfCurr15MinLprs_Object = MibTableColumn
adslAturPerfCurr15MinLprs = _AdslAturPerfCurr15MinLprs_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 7, 1, 10),
    _AdslAturPerfCurr15MinLprs_Type()
)
adslAturPerfCurr15MinLprs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAturPerfCurr15MinLprs.setStatus("current")
if mibBuilder.loadTexts:
    adslAturPerfCurr15MinLprs.setUnits("seconds")
_AdslAturPerfCurr15MinESs_Type = PerfCurrentCount
_AdslAturPerfCurr15MinESs_Object = MibTableColumn
adslAturPerfCurr15MinESs = _AdslAturPerfCurr15MinESs_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 7, 1, 11),
    _AdslAturPerfCurr15MinESs_Type()
)
adslAturPerfCurr15MinESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAturPerfCurr15MinESs.setStatus("current")
if mibBuilder.loadTexts:
    adslAturPerfCurr15MinESs.setUnits("seconds")


class _AdslAturPerfCurr1DayTimeElapsed_Type(AdslPerfTimeElapsed):
    """Custom type adslAturPerfCurr1DayTimeElapsed based on AdslPerfTimeElapsed"""
    subtypeSpec = AdslPerfTimeElapsed.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86399),
    )


_AdslAturPerfCurr1DayTimeElapsed_Type.__name__ = "AdslPerfTimeElapsed"
_AdslAturPerfCurr1DayTimeElapsed_Object = MibTableColumn
adslAturPerfCurr1DayTimeElapsed = _AdslAturPerfCurr1DayTimeElapsed_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 7, 1, 12),
    _AdslAturPerfCurr1DayTimeElapsed_Type()
)
adslAturPerfCurr1DayTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAturPerfCurr1DayTimeElapsed.setStatus("current")
if mibBuilder.loadTexts:
    adslAturPerfCurr1DayTimeElapsed.setUnits("seconds")
_AdslAturPerfCurr1DayLofs_Type = AdslPerfCurrDayCount
_AdslAturPerfCurr1DayLofs_Object = MibTableColumn
adslAturPerfCurr1DayLofs = _AdslAturPerfCurr1DayLofs_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 7, 1, 13),
    _AdslAturPerfCurr1DayLofs_Type()
)
adslAturPerfCurr1DayLofs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAturPerfCurr1DayLofs.setStatus("current")
if mibBuilder.loadTexts:
    adslAturPerfCurr1DayLofs.setUnits("seconds")
_AdslAturPerfCurr1DayLoss_Type = AdslPerfCurrDayCount
_AdslAturPerfCurr1DayLoss_Object = MibTableColumn
adslAturPerfCurr1DayLoss = _AdslAturPerfCurr1DayLoss_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 7, 1, 14),
    _AdslAturPerfCurr1DayLoss_Type()
)
adslAturPerfCurr1DayLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAturPerfCurr1DayLoss.setStatus("current")
if mibBuilder.loadTexts:
    adslAturPerfCurr1DayLoss.setUnits("seconds")
_AdslAturPerfCurr1DayLprs_Type = AdslPerfCurrDayCount
_AdslAturPerfCurr1DayLprs_Object = MibTableColumn
adslAturPerfCurr1DayLprs = _AdslAturPerfCurr1DayLprs_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 7, 1, 15),
    _AdslAturPerfCurr1DayLprs_Type()
)
adslAturPerfCurr1DayLprs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAturPerfCurr1DayLprs.setStatus("current")
if mibBuilder.loadTexts:
    adslAturPerfCurr1DayLprs.setUnits("seconds")
_AdslAturPerfCurr1DayESs_Type = AdslPerfCurrDayCount
_AdslAturPerfCurr1DayESs_Object = MibTableColumn
adslAturPerfCurr1DayESs = _AdslAturPerfCurr1DayESs_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 7, 1, 16),
    _AdslAturPerfCurr1DayESs_Type()
)
adslAturPerfCurr1DayESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAturPerfCurr1DayESs.setStatus("current")
if mibBuilder.loadTexts:
    adslAturPerfCurr1DayESs.setUnits("seconds")


class _AdslAturPerfPrev1DayMoniSecs_Type(Integer32):
    """Custom type adslAturPerfPrev1DayMoniSecs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_AdslAturPerfPrev1DayMoniSecs_Type.__name__ = "Integer32"
_AdslAturPerfPrev1DayMoniSecs_Object = MibTableColumn
adslAturPerfPrev1DayMoniSecs = _AdslAturPerfPrev1DayMoniSecs_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 7, 1, 17),
    _AdslAturPerfPrev1DayMoniSecs_Type()
)
adslAturPerfPrev1DayMoniSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAturPerfPrev1DayMoniSecs.setStatus("current")
if mibBuilder.loadTexts:
    adslAturPerfPrev1DayMoniSecs.setUnits("seconds")
_AdslAturPerfPrev1DayLofs_Type = AdslPerfPrevDayCount
_AdslAturPerfPrev1DayLofs_Object = MibTableColumn
adslAturPerfPrev1DayLofs = _AdslAturPerfPrev1DayLofs_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 7, 1, 18),
    _AdslAturPerfPrev1DayLofs_Type()
)
adslAturPerfPrev1DayLofs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAturPerfPrev1DayLofs.setStatus("current")
if mibBuilder.loadTexts:
    adslAturPerfPrev1DayLofs.setUnits("seconds")
_AdslAturPerfPrev1DayLoss_Type = AdslPerfPrevDayCount
_AdslAturPerfPrev1DayLoss_Object = MibTableColumn
adslAturPerfPrev1DayLoss = _AdslAturPerfPrev1DayLoss_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 7, 1, 19),
    _AdslAturPerfPrev1DayLoss_Type()
)
adslAturPerfPrev1DayLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAturPerfPrev1DayLoss.setStatus("current")
if mibBuilder.loadTexts:
    adslAturPerfPrev1DayLoss.setUnits("seconds")
_AdslAturPerfPrev1DayLprs_Type = AdslPerfPrevDayCount
_AdslAturPerfPrev1DayLprs_Object = MibTableColumn
adslAturPerfPrev1DayLprs = _AdslAturPerfPrev1DayLprs_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 7, 1, 20),
    _AdslAturPerfPrev1DayLprs_Type()
)
adslAturPerfPrev1DayLprs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAturPerfPrev1DayLprs.setStatus("current")
if mibBuilder.loadTexts:
    adslAturPerfPrev1DayLprs.setUnits("seconds")
_AdslAturPerfPrev1DayESs_Type = AdslPerfPrevDayCount
_AdslAturPerfPrev1DayESs_Object = MibTableColumn
adslAturPerfPrev1DayESs = _AdslAturPerfPrev1DayESs_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 7, 1, 21),
    _AdslAturPerfPrev1DayESs_Type()
)
adslAturPerfPrev1DayESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAturPerfPrev1DayESs.setStatus("current")
if mibBuilder.loadTexts:
    adslAturPerfPrev1DayESs.setUnits("seconds")
_AdslAtucIntervalTable_Object = MibTable
adslAtucIntervalTable = _AdslAtucIntervalTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 8)
)
if mibBuilder.loadTexts:
    adslAtucIntervalTable.setStatus("current")
_AdslAtucIntervalEntry_Object = MibTableRow
adslAtucIntervalEntry = _AdslAtucIntervalEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 8, 1)
)
adslAtucIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADSL-LINE-MIB", "adslAtucIntervalNumber"),
)
if mibBuilder.loadTexts:
    adslAtucIntervalEntry.setStatus("current")


class _AdslAtucIntervalNumber_Type(Integer32):
    """Custom type adslAtucIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_AdslAtucIntervalNumber_Type.__name__ = "Integer32"
_AdslAtucIntervalNumber_Object = MibTableColumn
adslAtucIntervalNumber = _AdslAtucIntervalNumber_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 8, 1, 1),
    _AdslAtucIntervalNumber_Type()
)
adslAtucIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adslAtucIntervalNumber.setStatus("current")
_AdslAtucIntervalLofs_Type = PerfIntervalCount
_AdslAtucIntervalLofs_Object = MibTableColumn
adslAtucIntervalLofs = _AdslAtucIntervalLofs_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 8, 1, 2),
    _AdslAtucIntervalLofs_Type()
)
adslAtucIntervalLofs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAtucIntervalLofs.setStatus("current")
if mibBuilder.loadTexts:
    adslAtucIntervalLofs.setUnits("seconds")
_AdslAtucIntervalLoss_Type = PerfIntervalCount
_AdslAtucIntervalLoss_Object = MibTableColumn
adslAtucIntervalLoss = _AdslAtucIntervalLoss_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 8, 1, 3),
    _AdslAtucIntervalLoss_Type()
)
adslAtucIntervalLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAtucIntervalLoss.setStatus("current")
if mibBuilder.loadTexts:
    adslAtucIntervalLoss.setUnits("seconds")
_AdslAtucIntervalLols_Type = PerfIntervalCount
_AdslAtucIntervalLols_Object = MibTableColumn
adslAtucIntervalLols = _AdslAtucIntervalLols_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 8, 1, 4),
    _AdslAtucIntervalLols_Type()
)
adslAtucIntervalLols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAtucIntervalLols.setStatus("current")
if mibBuilder.loadTexts:
    adslAtucIntervalLols.setUnits("seconds")
_AdslAtucIntervalLprs_Type = PerfIntervalCount
_AdslAtucIntervalLprs_Object = MibTableColumn
adslAtucIntervalLprs = _AdslAtucIntervalLprs_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 8, 1, 5),
    _AdslAtucIntervalLprs_Type()
)
adslAtucIntervalLprs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAtucIntervalLprs.setStatus("current")
if mibBuilder.loadTexts:
    adslAtucIntervalLprs.setUnits("seconds")
_AdslAtucIntervalESs_Type = PerfIntervalCount
_AdslAtucIntervalESs_Object = MibTableColumn
adslAtucIntervalESs = _AdslAtucIntervalESs_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 8, 1, 6),
    _AdslAtucIntervalESs_Type()
)
adslAtucIntervalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAtucIntervalESs.setStatus("current")
if mibBuilder.loadTexts:
    adslAtucIntervalESs.setUnits("seconds")
_AdslAtucIntervalInits_Type = PerfIntervalCount
_AdslAtucIntervalInits_Object = MibTableColumn
adslAtucIntervalInits = _AdslAtucIntervalInits_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 8, 1, 7),
    _AdslAtucIntervalInits_Type()
)
adslAtucIntervalInits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAtucIntervalInits.setStatus("current")
_AdslAtucIntervalValidData_Type = TruthValue
_AdslAtucIntervalValidData_Object = MibTableColumn
adslAtucIntervalValidData = _AdslAtucIntervalValidData_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 8, 1, 8),
    _AdslAtucIntervalValidData_Type()
)
adslAtucIntervalValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAtucIntervalValidData.setStatus("current")
_AdslAturIntervalTable_Object = MibTable
adslAturIntervalTable = _AdslAturIntervalTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 9)
)
if mibBuilder.loadTexts:
    adslAturIntervalTable.setStatus("current")
_AdslAturIntervalEntry_Object = MibTableRow
adslAturIntervalEntry = _AdslAturIntervalEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 9, 1)
)
adslAturIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADSL-LINE-MIB", "adslAturIntervalNumber"),
)
if mibBuilder.loadTexts:
    adslAturIntervalEntry.setStatus("current")


class _AdslAturIntervalNumber_Type(Integer32):
    """Custom type adslAturIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_AdslAturIntervalNumber_Type.__name__ = "Integer32"
_AdslAturIntervalNumber_Object = MibTableColumn
adslAturIntervalNumber = _AdslAturIntervalNumber_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 9, 1, 1),
    _AdslAturIntervalNumber_Type()
)
adslAturIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adslAturIntervalNumber.setStatus("current")
_AdslAturIntervalLofs_Type = PerfIntervalCount
_AdslAturIntervalLofs_Object = MibTableColumn
adslAturIntervalLofs = _AdslAturIntervalLofs_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 9, 1, 2),
    _AdslAturIntervalLofs_Type()
)
adslAturIntervalLofs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAturIntervalLofs.setStatus("current")
if mibBuilder.loadTexts:
    adslAturIntervalLofs.setUnits("seconds")
_AdslAturIntervalLoss_Type = PerfIntervalCount
_AdslAturIntervalLoss_Object = MibTableColumn
adslAturIntervalLoss = _AdslAturIntervalLoss_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 9, 1, 3),
    _AdslAturIntervalLoss_Type()
)
adslAturIntervalLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAturIntervalLoss.setStatus("current")
if mibBuilder.loadTexts:
    adslAturIntervalLoss.setUnits("seconds")
_AdslAturIntervalLprs_Type = PerfIntervalCount
_AdslAturIntervalLprs_Object = MibTableColumn
adslAturIntervalLprs = _AdslAturIntervalLprs_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 9, 1, 4),
    _AdslAturIntervalLprs_Type()
)
adslAturIntervalLprs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAturIntervalLprs.setStatus("current")
if mibBuilder.loadTexts:
    adslAturIntervalLprs.setUnits("seconds")
_AdslAturIntervalESs_Type = PerfIntervalCount
_AdslAturIntervalESs_Object = MibTableColumn
adslAturIntervalESs = _AdslAturIntervalESs_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 9, 1, 5),
    _AdslAturIntervalESs_Type()
)
adslAturIntervalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAturIntervalESs.setStatus("current")
if mibBuilder.loadTexts:
    adslAturIntervalESs.setUnits("seconds")
_AdslAturIntervalValidData_Type = TruthValue
_AdslAturIntervalValidData_Object = MibTableColumn
adslAturIntervalValidData = _AdslAturIntervalValidData_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 9, 1, 6),
    _AdslAturIntervalValidData_Type()
)
adslAturIntervalValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAturIntervalValidData.setStatus("current")
_AdslAtucChanPerfDataTable_Object = MibTable
adslAtucChanPerfDataTable = _AdslAtucChanPerfDataTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 10)
)
if mibBuilder.loadTexts:
    adslAtucChanPerfDataTable.setStatus("current")
_AdslAtucChanPerfDataEntry_Object = MibTableRow
adslAtucChanPerfDataEntry = _AdslAtucChanPerfDataEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 10, 1)
)
adslAtucChanPerfDataEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adslAtucChanPerfDataEntry.setStatus("current")
_AdslAtucChanReceivedBlks_Type = Counter32
_AdslAtucChanReceivedBlks_Object = MibTableColumn
adslAtucChanReceivedBlks = _AdslAtucChanReceivedBlks_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 10, 1, 1),
    _AdslAtucChanReceivedBlks_Type()
)
adslAtucChanReceivedBlks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAtucChanReceivedBlks.setStatus("current")
_AdslAtucChanTransmittedBlks_Type = Counter32
_AdslAtucChanTransmittedBlks_Object = MibTableColumn
adslAtucChanTransmittedBlks = _AdslAtucChanTransmittedBlks_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 10, 1, 2),
    _AdslAtucChanTransmittedBlks_Type()
)
adslAtucChanTransmittedBlks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAtucChanTransmittedBlks.setStatus("current")
_AdslAtucChanCorrectedBlks_Type = Counter32
_AdslAtucChanCorrectedBlks_Object = MibTableColumn
adslAtucChanCorrectedBlks = _AdslAtucChanCorrectedBlks_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 10, 1, 3),
    _AdslAtucChanCorrectedBlks_Type()
)
adslAtucChanCorrectedBlks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAtucChanCorrectedBlks.setStatus("current")
_AdslAtucChanUncorrectBlks_Type = Counter32
_AdslAtucChanUncorrectBlks_Object = MibTableColumn
adslAtucChanUncorrectBlks = _AdslAtucChanUncorrectBlks_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 10, 1, 4),
    _AdslAtucChanUncorrectBlks_Type()
)
adslAtucChanUncorrectBlks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAtucChanUncorrectBlks.setStatus("current")


class _AdslAtucChanPerfValidIntervals_Type(Integer32):
    """Custom type adslAtucChanPerfValidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_AdslAtucChanPerfValidIntervals_Type.__name__ = "Integer32"
_AdslAtucChanPerfValidIntervals_Object = MibTableColumn
adslAtucChanPerfValidIntervals = _AdslAtucChanPerfValidIntervals_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 10, 1, 5),
    _AdslAtucChanPerfValidIntervals_Type()
)
adslAtucChanPerfValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAtucChanPerfValidIntervals.setStatus("current")


class _AdslAtucChanPerfInvalidIntervals_Type(Integer32):
    """Custom type adslAtucChanPerfInvalidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_AdslAtucChanPerfInvalidIntervals_Type.__name__ = "Integer32"
_AdslAtucChanPerfInvalidIntervals_Object = MibTableColumn
adslAtucChanPerfInvalidIntervals = _AdslAtucChanPerfInvalidIntervals_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 10, 1, 6),
    _AdslAtucChanPerfInvalidIntervals_Type()
)
adslAtucChanPerfInvalidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAtucChanPerfInvalidIntervals.setStatus("current")


class _AdslAtucChanPerfCurr15MinTimeElapsed_Type(AdslPerfTimeElapsed):
    """Custom type adslAtucChanPerfCurr15MinTimeElapsed based on AdslPerfTimeElapsed"""
    subtypeSpec = AdslPerfTimeElapsed.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 899),
    )


_AdslAtucChanPerfCurr15MinTimeElapsed_Type.__name__ = "AdslPerfTimeElapsed"
_AdslAtucChanPerfCurr15MinTimeElapsed_Object = MibTableColumn
adslAtucChanPerfCurr15MinTimeElapsed = _AdslAtucChanPerfCurr15MinTimeElapsed_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 10, 1, 7),
    _AdslAtucChanPerfCurr15MinTimeElapsed_Type()
)
adslAtucChanPerfCurr15MinTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAtucChanPerfCurr15MinTimeElapsed.setStatus("current")
if mibBuilder.loadTexts:
    adslAtucChanPerfCurr15MinTimeElapsed.setUnits("seconds")
_AdslAtucChanPerfCurr15MinReceivedBlks_Type = PerfCurrentCount
_AdslAtucChanPerfCurr15MinReceivedBlks_Object = MibTableColumn
adslAtucChanPerfCurr15MinReceivedBlks = _AdslAtucChanPerfCurr15MinReceivedBlks_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 10, 1, 8),
    _AdslAtucChanPerfCurr15MinReceivedBlks_Type()
)
adslAtucChanPerfCurr15MinReceivedBlks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAtucChanPerfCurr15MinReceivedBlks.setStatus("current")
_AdslAtucChanPerfCurr15MinTransmittedBlks_Type = PerfCurrentCount
_AdslAtucChanPerfCurr15MinTransmittedBlks_Object = MibTableColumn
adslAtucChanPerfCurr15MinTransmittedBlks = _AdslAtucChanPerfCurr15MinTransmittedBlks_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 10, 1, 9),
    _AdslAtucChanPerfCurr15MinTransmittedBlks_Type()
)
adslAtucChanPerfCurr15MinTransmittedBlks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAtucChanPerfCurr15MinTransmittedBlks.setStatus("current")
_AdslAtucChanPerfCurr15MinCorrectedBlks_Type = PerfCurrentCount
_AdslAtucChanPerfCurr15MinCorrectedBlks_Object = MibTableColumn
adslAtucChanPerfCurr15MinCorrectedBlks = _AdslAtucChanPerfCurr15MinCorrectedBlks_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 10, 1, 10),
    _AdslAtucChanPerfCurr15MinCorrectedBlks_Type()
)
adslAtucChanPerfCurr15MinCorrectedBlks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAtucChanPerfCurr15MinCorrectedBlks.setStatus("current")
_AdslAtucChanPerfCurr15MinUncorrectBlks_Type = PerfCurrentCount
_AdslAtucChanPerfCurr15MinUncorrectBlks_Object = MibTableColumn
adslAtucChanPerfCurr15MinUncorrectBlks = _AdslAtucChanPerfCurr15MinUncorrectBlks_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 10, 1, 11),
    _AdslAtucChanPerfCurr15MinUncorrectBlks_Type()
)
adslAtucChanPerfCurr15MinUncorrectBlks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAtucChanPerfCurr15MinUncorrectBlks.setStatus("current")


class _AdslAtucChanPerfCurr1DayTimeElapsed_Type(AdslPerfTimeElapsed):
    """Custom type adslAtucChanPerfCurr1DayTimeElapsed based on AdslPerfTimeElapsed"""
    subtypeSpec = AdslPerfTimeElapsed.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86399),
    )


_AdslAtucChanPerfCurr1DayTimeElapsed_Type.__name__ = "AdslPerfTimeElapsed"
_AdslAtucChanPerfCurr1DayTimeElapsed_Object = MibTableColumn
adslAtucChanPerfCurr1DayTimeElapsed = _AdslAtucChanPerfCurr1DayTimeElapsed_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 10, 1, 12),
    _AdslAtucChanPerfCurr1DayTimeElapsed_Type()
)
adslAtucChanPerfCurr1DayTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAtucChanPerfCurr1DayTimeElapsed.setStatus("current")
if mibBuilder.loadTexts:
    adslAtucChanPerfCurr1DayTimeElapsed.setUnits("seconds")
_AdslAtucChanPerfCurr1DayReceivedBlks_Type = AdslPerfCurrDayCount
_AdslAtucChanPerfCurr1DayReceivedBlks_Object = MibTableColumn
adslAtucChanPerfCurr1DayReceivedBlks = _AdslAtucChanPerfCurr1DayReceivedBlks_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 10, 1, 13),
    _AdslAtucChanPerfCurr1DayReceivedBlks_Type()
)
adslAtucChanPerfCurr1DayReceivedBlks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAtucChanPerfCurr1DayReceivedBlks.setStatus("current")
_AdslAtucChanPerfCurr1DayTransmittedBlks_Type = AdslPerfCurrDayCount
_AdslAtucChanPerfCurr1DayTransmittedBlks_Object = MibTableColumn
adslAtucChanPerfCurr1DayTransmittedBlks = _AdslAtucChanPerfCurr1DayTransmittedBlks_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 10, 1, 14),
    _AdslAtucChanPerfCurr1DayTransmittedBlks_Type()
)
adslAtucChanPerfCurr1DayTransmittedBlks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAtucChanPerfCurr1DayTransmittedBlks.setStatus("current")
_AdslAtucChanPerfCurr1DayCorrectedBlks_Type = AdslPerfCurrDayCount
_AdslAtucChanPerfCurr1DayCorrectedBlks_Object = MibTableColumn
adslAtucChanPerfCurr1DayCorrectedBlks = _AdslAtucChanPerfCurr1DayCorrectedBlks_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 10, 1, 15),
    _AdslAtucChanPerfCurr1DayCorrectedBlks_Type()
)
adslAtucChanPerfCurr1DayCorrectedBlks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAtucChanPerfCurr1DayCorrectedBlks.setStatus("current")
_AdslAtucChanPerfCurr1DayUncorrectBlks_Type = AdslPerfCurrDayCount
_AdslAtucChanPerfCurr1DayUncorrectBlks_Object = MibTableColumn
adslAtucChanPerfCurr1DayUncorrectBlks = _AdslAtucChanPerfCurr1DayUncorrectBlks_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 10, 1, 16),
    _AdslAtucChanPerfCurr1DayUncorrectBlks_Type()
)
adslAtucChanPerfCurr1DayUncorrectBlks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAtucChanPerfCurr1DayUncorrectBlks.setStatus("current")


class _AdslAtucChanPerfPrev1DayMoniSecs_Type(Integer32):
    """Custom type adslAtucChanPerfPrev1DayMoniSecs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_AdslAtucChanPerfPrev1DayMoniSecs_Type.__name__ = "Integer32"
_AdslAtucChanPerfPrev1DayMoniSecs_Object = MibTableColumn
adslAtucChanPerfPrev1DayMoniSecs = _AdslAtucChanPerfPrev1DayMoniSecs_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 10, 1, 17),
    _AdslAtucChanPerfPrev1DayMoniSecs_Type()
)
adslAtucChanPerfPrev1DayMoniSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAtucChanPerfPrev1DayMoniSecs.setStatus("current")
if mibBuilder.loadTexts:
    adslAtucChanPerfPrev1DayMoniSecs.setUnits("seconds")
_AdslAtucChanPerfPrev1DayReceivedBlks_Type = AdslPerfPrevDayCount
_AdslAtucChanPerfPrev1DayReceivedBlks_Object = MibTableColumn
adslAtucChanPerfPrev1DayReceivedBlks = _AdslAtucChanPerfPrev1DayReceivedBlks_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 10, 1, 18),
    _AdslAtucChanPerfPrev1DayReceivedBlks_Type()
)
adslAtucChanPerfPrev1DayReceivedBlks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAtucChanPerfPrev1DayReceivedBlks.setStatus("current")
_AdslAtucChanPerfPrev1DayTransmittedBlks_Type = AdslPerfPrevDayCount
_AdslAtucChanPerfPrev1DayTransmittedBlks_Object = MibTableColumn
adslAtucChanPerfPrev1DayTransmittedBlks = _AdslAtucChanPerfPrev1DayTransmittedBlks_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 10, 1, 19),
    _AdslAtucChanPerfPrev1DayTransmittedBlks_Type()
)
adslAtucChanPerfPrev1DayTransmittedBlks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAtucChanPerfPrev1DayTransmittedBlks.setStatus("current")
_AdslAtucChanPerfPrev1DayCorrectedBlks_Type = AdslPerfPrevDayCount
_AdslAtucChanPerfPrev1DayCorrectedBlks_Object = MibTableColumn
adslAtucChanPerfPrev1DayCorrectedBlks = _AdslAtucChanPerfPrev1DayCorrectedBlks_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 10, 1, 20),
    _AdslAtucChanPerfPrev1DayCorrectedBlks_Type()
)
adslAtucChanPerfPrev1DayCorrectedBlks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAtucChanPerfPrev1DayCorrectedBlks.setStatus("current")
_AdslAtucChanPerfPrev1DayUncorrectBlks_Type = AdslPerfPrevDayCount
_AdslAtucChanPerfPrev1DayUncorrectBlks_Object = MibTableColumn
adslAtucChanPerfPrev1DayUncorrectBlks = _AdslAtucChanPerfPrev1DayUncorrectBlks_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 10, 1, 21),
    _AdslAtucChanPerfPrev1DayUncorrectBlks_Type()
)
adslAtucChanPerfPrev1DayUncorrectBlks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAtucChanPerfPrev1DayUncorrectBlks.setStatus("current")
_AdslAturChanPerfDataTable_Object = MibTable
adslAturChanPerfDataTable = _AdslAturChanPerfDataTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 11)
)
if mibBuilder.loadTexts:
    adslAturChanPerfDataTable.setStatus("current")
_AdslAturChanPerfDataEntry_Object = MibTableRow
adslAturChanPerfDataEntry = _AdslAturChanPerfDataEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 11, 1)
)
adslAturChanPerfDataEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adslAturChanPerfDataEntry.setStatus("current")
_AdslAturChanReceivedBlks_Type = Counter32
_AdslAturChanReceivedBlks_Object = MibTableColumn
adslAturChanReceivedBlks = _AdslAturChanReceivedBlks_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 11, 1, 1),
    _AdslAturChanReceivedBlks_Type()
)
adslAturChanReceivedBlks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAturChanReceivedBlks.setStatus("current")
_AdslAturChanTransmittedBlks_Type = Counter32
_AdslAturChanTransmittedBlks_Object = MibTableColumn
adslAturChanTransmittedBlks = _AdslAturChanTransmittedBlks_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 11, 1, 2),
    _AdslAturChanTransmittedBlks_Type()
)
adslAturChanTransmittedBlks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAturChanTransmittedBlks.setStatus("current")
_AdslAturChanCorrectedBlks_Type = Counter32
_AdslAturChanCorrectedBlks_Object = MibTableColumn
adslAturChanCorrectedBlks = _AdslAturChanCorrectedBlks_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 11, 1, 3),
    _AdslAturChanCorrectedBlks_Type()
)
adslAturChanCorrectedBlks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAturChanCorrectedBlks.setStatus("current")
_AdslAturChanUncorrectBlks_Type = Counter32
_AdslAturChanUncorrectBlks_Object = MibTableColumn
adslAturChanUncorrectBlks = _AdslAturChanUncorrectBlks_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 11, 1, 4),
    _AdslAturChanUncorrectBlks_Type()
)
adslAturChanUncorrectBlks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAturChanUncorrectBlks.setStatus("current")


class _AdslAturChanPerfValidIntervals_Type(Integer32):
    """Custom type adslAturChanPerfValidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_AdslAturChanPerfValidIntervals_Type.__name__ = "Integer32"
_AdslAturChanPerfValidIntervals_Object = MibTableColumn
adslAturChanPerfValidIntervals = _AdslAturChanPerfValidIntervals_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 11, 1, 5),
    _AdslAturChanPerfValidIntervals_Type()
)
adslAturChanPerfValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAturChanPerfValidIntervals.setStatus("current")


class _AdslAturChanPerfInvalidIntervals_Type(Integer32):
    """Custom type adslAturChanPerfInvalidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_AdslAturChanPerfInvalidIntervals_Type.__name__ = "Integer32"
_AdslAturChanPerfInvalidIntervals_Object = MibTableColumn
adslAturChanPerfInvalidIntervals = _AdslAturChanPerfInvalidIntervals_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 11, 1, 6),
    _AdslAturChanPerfInvalidIntervals_Type()
)
adslAturChanPerfInvalidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAturChanPerfInvalidIntervals.setStatus("current")


class _AdslAturChanPerfCurr15MinTimeElapsed_Type(AdslPerfTimeElapsed):
    """Custom type adslAturChanPerfCurr15MinTimeElapsed based on AdslPerfTimeElapsed"""
    subtypeSpec = AdslPerfTimeElapsed.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 899),
    )


_AdslAturChanPerfCurr15MinTimeElapsed_Type.__name__ = "AdslPerfTimeElapsed"
_AdslAturChanPerfCurr15MinTimeElapsed_Object = MibTableColumn
adslAturChanPerfCurr15MinTimeElapsed = _AdslAturChanPerfCurr15MinTimeElapsed_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 11, 1, 7),
    _AdslAturChanPerfCurr15MinTimeElapsed_Type()
)
adslAturChanPerfCurr15MinTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAturChanPerfCurr15MinTimeElapsed.setStatus("current")
if mibBuilder.loadTexts:
    adslAturChanPerfCurr15MinTimeElapsed.setUnits("seconds")
_AdslAturChanPerfCurr15MinReceivedBlks_Type = PerfCurrentCount
_AdslAturChanPerfCurr15MinReceivedBlks_Object = MibTableColumn
adslAturChanPerfCurr15MinReceivedBlks = _AdslAturChanPerfCurr15MinReceivedBlks_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 11, 1, 8),
    _AdslAturChanPerfCurr15MinReceivedBlks_Type()
)
adslAturChanPerfCurr15MinReceivedBlks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAturChanPerfCurr15MinReceivedBlks.setStatus("current")
_AdslAturChanPerfCurr15MinTransmittedBlks_Type = PerfCurrentCount
_AdslAturChanPerfCurr15MinTransmittedBlks_Object = MibTableColumn
adslAturChanPerfCurr15MinTransmittedBlks = _AdslAturChanPerfCurr15MinTransmittedBlks_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 11, 1, 9),
    _AdslAturChanPerfCurr15MinTransmittedBlks_Type()
)
adslAturChanPerfCurr15MinTransmittedBlks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAturChanPerfCurr15MinTransmittedBlks.setStatus("current")
_AdslAturChanPerfCurr15MinCorrectedBlks_Type = PerfCurrentCount
_AdslAturChanPerfCurr15MinCorrectedBlks_Object = MibTableColumn
adslAturChanPerfCurr15MinCorrectedBlks = _AdslAturChanPerfCurr15MinCorrectedBlks_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 11, 1, 10),
    _AdslAturChanPerfCurr15MinCorrectedBlks_Type()
)
adslAturChanPerfCurr15MinCorrectedBlks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAturChanPerfCurr15MinCorrectedBlks.setStatus("current")
_AdslAturChanPerfCurr15MinUncorrectBlks_Type = PerfCurrentCount
_AdslAturChanPerfCurr15MinUncorrectBlks_Object = MibTableColumn
adslAturChanPerfCurr15MinUncorrectBlks = _AdslAturChanPerfCurr15MinUncorrectBlks_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 11, 1, 11),
    _AdslAturChanPerfCurr15MinUncorrectBlks_Type()
)
adslAturChanPerfCurr15MinUncorrectBlks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAturChanPerfCurr15MinUncorrectBlks.setStatus("current")


class _AdslAturChanPerfCurr1DayTimeElapsed_Type(AdslPerfTimeElapsed):
    """Custom type adslAturChanPerfCurr1DayTimeElapsed based on AdslPerfTimeElapsed"""
    subtypeSpec = AdslPerfTimeElapsed.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86399),
    )


_AdslAturChanPerfCurr1DayTimeElapsed_Type.__name__ = "AdslPerfTimeElapsed"
_AdslAturChanPerfCurr1DayTimeElapsed_Object = MibTableColumn
adslAturChanPerfCurr1DayTimeElapsed = _AdslAturChanPerfCurr1DayTimeElapsed_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 11, 1, 12),
    _AdslAturChanPerfCurr1DayTimeElapsed_Type()
)
adslAturChanPerfCurr1DayTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAturChanPerfCurr1DayTimeElapsed.setStatus("current")
if mibBuilder.loadTexts:
    adslAturChanPerfCurr1DayTimeElapsed.setUnits("seconds")
_AdslAturChanPerfCurr1DayReceivedBlks_Type = AdslPerfCurrDayCount
_AdslAturChanPerfCurr1DayReceivedBlks_Object = MibTableColumn
adslAturChanPerfCurr1DayReceivedBlks = _AdslAturChanPerfCurr1DayReceivedBlks_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 11, 1, 13),
    _AdslAturChanPerfCurr1DayReceivedBlks_Type()
)
adslAturChanPerfCurr1DayReceivedBlks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAturChanPerfCurr1DayReceivedBlks.setStatus("current")
_AdslAturChanPerfCurr1DayTransmittedBlks_Type = AdslPerfCurrDayCount
_AdslAturChanPerfCurr1DayTransmittedBlks_Object = MibTableColumn
adslAturChanPerfCurr1DayTransmittedBlks = _AdslAturChanPerfCurr1DayTransmittedBlks_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 11, 1, 14),
    _AdslAturChanPerfCurr1DayTransmittedBlks_Type()
)
adslAturChanPerfCurr1DayTransmittedBlks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAturChanPerfCurr1DayTransmittedBlks.setStatus("current")
_AdslAturChanPerfCurr1DayCorrectedBlks_Type = AdslPerfCurrDayCount
_AdslAturChanPerfCurr1DayCorrectedBlks_Object = MibTableColumn
adslAturChanPerfCurr1DayCorrectedBlks = _AdslAturChanPerfCurr1DayCorrectedBlks_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 11, 1, 15),
    _AdslAturChanPerfCurr1DayCorrectedBlks_Type()
)
adslAturChanPerfCurr1DayCorrectedBlks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAturChanPerfCurr1DayCorrectedBlks.setStatus("current")
_AdslAturChanPerfCurr1DayUncorrectBlks_Type = AdslPerfCurrDayCount
_AdslAturChanPerfCurr1DayUncorrectBlks_Object = MibTableColumn
adslAturChanPerfCurr1DayUncorrectBlks = _AdslAturChanPerfCurr1DayUncorrectBlks_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 11, 1, 16),
    _AdslAturChanPerfCurr1DayUncorrectBlks_Type()
)
adslAturChanPerfCurr1DayUncorrectBlks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAturChanPerfCurr1DayUncorrectBlks.setStatus("current")


class _AdslAturChanPerfPrev1DayMoniSecs_Type(Integer32):
    """Custom type adslAturChanPerfPrev1DayMoniSecs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_AdslAturChanPerfPrev1DayMoniSecs_Type.__name__ = "Integer32"
_AdslAturChanPerfPrev1DayMoniSecs_Object = MibTableColumn
adslAturChanPerfPrev1DayMoniSecs = _AdslAturChanPerfPrev1DayMoniSecs_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 11, 1, 17),
    _AdslAturChanPerfPrev1DayMoniSecs_Type()
)
adslAturChanPerfPrev1DayMoniSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAturChanPerfPrev1DayMoniSecs.setStatus("current")
if mibBuilder.loadTexts:
    adslAturChanPerfPrev1DayMoniSecs.setUnits("seconds")
_AdslAturChanPerfPrev1DayReceivedBlks_Type = AdslPerfPrevDayCount
_AdslAturChanPerfPrev1DayReceivedBlks_Object = MibTableColumn
adslAturChanPerfPrev1DayReceivedBlks = _AdslAturChanPerfPrev1DayReceivedBlks_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 11, 1, 18),
    _AdslAturChanPerfPrev1DayReceivedBlks_Type()
)
adslAturChanPerfPrev1DayReceivedBlks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAturChanPerfPrev1DayReceivedBlks.setStatus("current")
_AdslAturChanPerfPrev1DayTransmittedBlks_Type = AdslPerfPrevDayCount
_AdslAturChanPerfPrev1DayTransmittedBlks_Object = MibTableColumn
adslAturChanPerfPrev1DayTransmittedBlks = _AdslAturChanPerfPrev1DayTransmittedBlks_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 11, 1, 19),
    _AdslAturChanPerfPrev1DayTransmittedBlks_Type()
)
adslAturChanPerfPrev1DayTransmittedBlks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAturChanPerfPrev1DayTransmittedBlks.setStatus("current")
_AdslAturChanPerfPrev1DayCorrectedBlks_Type = AdslPerfPrevDayCount
_AdslAturChanPerfPrev1DayCorrectedBlks_Object = MibTableColumn
adslAturChanPerfPrev1DayCorrectedBlks = _AdslAturChanPerfPrev1DayCorrectedBlks_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 11, 1, 20),
    _AdslAturChanPerfPrev1DayCorrectedBlks_Type()
)
adslAturChanPerfPrev1DayCorrectedBlks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAturChanPerfPrev1DayCorrectedBlks.setStatus("current")
_AdslAturChanPerfPrev1DayUncorrectBlks_Type = AdslPerfPrevDayCount
_AdslAturChanPerfPrev1DayUncorrectBlks_Object = MibTableColumn
adslAturChanPerfPrev1DayUncorrectBlks = _AdslAturChanPerfPrev1DayUncorrectBlks_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 11, 1, 21),
    _AdslAturChanPerfPrev1DayUncorrectBlks_Type()
)
adslAturChanPerfPrev1DayUncorrectBlks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAturChanPerfPrev1DayUncorrectBlks.setStatus("current")
_AdslAtucChanIntervalTable_Object = MibTable
adslAtucChanIntervalTable = _AdslAtucChanIntervalTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 12)
)
if mibBuilder.loadTexts:
    adslAtucChanIntervalTable.setStatus("current")
_AdslAtucChanIntervalEntry_Object = MibTableRow
adslAtucChanIntervalEntry = _AdslAtucChanIntervalEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 12, 1)
)
adslAtucChanIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADSL-LINE-MIB", "adslAtucChanIntervalNumber"),
)
if mibBuilder.loadTexts:
    adslAtucChanIntervalEntry.setStatus("current")


class _AdslAtucChanIntervalNumber_Type(Integer32):
    """Custom type adslAtucChanIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_AdslAtucChanIntervalNumber_Type.__name__ = "Integer32"
_AdslAtucChanIntervalNumber_Object = MibTableColumn
adslAtucChanIntervalNumber = _AdslAtucChanIntervalNumber_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 12, 1, 1),
    _AdslAtucChanIntervalNumber_Type()
)
adslAtucChanIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adslAtucChanIntervalNumber.setStatus("current")
_AdslAtucChanIntervalReceivedBlks_Type = PerfIntervalCount
_AdslAtucChanIntervalReceivedBlks_Object = MibTableColumn
adslAtucChanIntervalReceivedBlks = _AdslAtucChanIntervalReceivedBlks_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 12, 1, 2),
    _AdslAtucChanIntervalReceivedBlks_Type()
)
adslAtucChanIntervalReceivedBlks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAtucChanIntervalReceivedBlks.setStatus("current")
_AdslAtucChanIntervalTransmittedBlks_Type = PerfIntervalCount
_AdslAtucChanIntervalTransmittedBlks_Object = MibTableColumn
adslAtucChanIntervalTransmittedBlks = _AdslAtucChanIntervalTransmittedBlks_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 12, 1, 3),
    _AdslAtucChanIntervalTransmittedBlks_Type()
)
adslAtucChanIntervalTransmittedBlks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAtucChanIntervalTransmittedBlks.setStatus("current")
_AdslAtucChanIntervalCorrectedBlks_Type = PerfIntervalCount
_AdslAtucChanIntervalCorrectedBlks_Object = MibTableColumn
adslAtucChanIntervalCorrectedBlks = _AdslAtucChanIntervalCorrectedBlks_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 12, 1, 4),
    _AdslAtucChanIntervalCorrectedBlks_Type()
)
adslAtucChanIntervalCorrectedBlks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAtucChanIntervalCorrectedBlks.setStatus("current")
_AdslAtucChanIntervalUncorrectBlks_Type = PerfIntervalCount
_AdslAtucChanIntervalUncorrectBlks_Object = MibTableColumn
adslAtucChanIntervalUncorrectBlks = _AdslAtucChanIntervalUncorrectBlks_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 12, 1, 5),
    _AdslAtucChanIntervalUncorrectBlks_Type()
)
adslAtucChanIntervalUncorrectBlks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAtucChanIntervalUncorrectBlks.setStatus("current")
_AdslAtucChanIntervalValidData_Type = TruthValue
_AdslAtucChanIntervalValidData_Object = MibTableColumn
adslAtucChanIntervalValidData = _AdslAtucChanIntervalValidData_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 12, 1, 6),
    _AdslAtucChanIntervalValidData_Type()
)
adslAtucChanIntervalValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAtucChanIntervalValidData.setStatus("current")
_AdslAturChanIntervalTable_Object = MibTable
adslAturChanIntervalTable = _AdslAturChanIntervalTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 13)
)
if mibBuilder.loadTexts:
    adslAturChanIntervalTable.setStatus("current")
_AdslAturChanIntervalEntry_Object = MibTableRow
adslAturChanIntervalEntry = _AdslAturChanIntervalEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 13, 1)
)
adslAturChanIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADSL-LINE-MIB", "adslAturChanIntervalNumber"),
)
if mibBuilder.loadTexts:
    adslAturChanIntervalEntry.setStatus("current")


class _AdslAturChanIntervalNumber_Type(Integer32):
    """Custom type adslAturChanIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_AdslAturChanIntervalNumber_Type.__name__ = "Integer32"
_AdslAturChanIntervalNumber_Object = MibTableColumn
adslAturChanIntervalNumber = _AdslAturChanIntervalNumber_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 13, 1, 1),
    _AdslAturChanIntervalNumber_Type()
)
adslAturChanIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adslAturChanIntervalNumber.setStatus("current")
_AdslAturChanIntervalReceivedBlks_Type = PerfIntervalCount
_AdslAturChanIntervalReceivedBlks_Object = MibTableColumn
adslAturChanIntervalReceivedBlks = _AdslAturChanIntervalReceivedBlks_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 13, 1, 2),
    _AdslAturChanIntervalReceivedBlks_Type()
)
adslAturChanIntervalReceivedBlks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAturChanIntervalReceivedBlks.setStatus("current")
_AdslAturChanIntervalTransmittedBlks_Type = PerfIntervalCount
_AdslAturChanIntervalTransmittedBlks_Object = MibTableColumn
adslAturChanIntervalTransmittedBlks = _AdslAturChanIntervalTransmittedBlks_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 13, 1, 3),
    _AdslAturChanIntervalTransmittedBlks_Type()
)
adslAturChanIntervalTransmittedBlks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAturChanIntervalTransmittedBlks.setStatus("current")
_AdslAturChanIntervalCorrectedBlks_Type = PerfIntervalCount
_AdslAturChanIntervalCorrectedBlks_Object = MibTableColumn
adslAturChanIntervalCorrectedBlks = _AdslAturChanIntervalCorrectedBlks_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 13, 1, 4),
    _AdslAturChanIntervalCorrectedBlks_Type()
)
adslAturChanIntervalCorrectedBlks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAturChanIntervalCorrectedBlks.setStatus("current")
_AdslAturChanIntervalUncorrectBlks_Type = PerfIntervalCount
_AdslAturChanIntervalUncorrectBlks_Object = MibTableColumn
adslAturChanIntervalUncorrectBlks = _AdslAturChanIntervalUncorrectBlks_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 13, 1, 5),
    _AdslAturChanIntervalUncorrectBlks_Type()
)
adslAturChanIntervalUncorrectBlks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAturChanIntervalUncorrectBlks.setStatus("current")
_AdslAturChanIntervalValidData_Type = TruthValue
_AdslAturChanIntervalValidData_Object = MibTableColumn
adslAturChanIntervalValidData = _AdslAturChanIntervalValidData_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 13, 1, 6),
    _AdslAturChanIntervalValidData_Type()
)
adslAturChanIntervalValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAturChanIntervalValidData.setStatus("current")
_AdslLineConfProfileTable_Object = MibTable
adslLineConfProfileTable = _AdslLineConfProfileTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 14)
)
if mibBuilder.loadTexts:
    adslLineConfProfileTable.setStatus("current")
_AdslLineConfProfileEntry_Object = MibTableRow
adslLineConfProfileEntry = _AdslLineConfProfileEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 14, 1)
)
adslLineConfProfileEntry.setIndexNames(
    (1, "ADSL-LINE-MIB", "adslLineConfProfileName"),
)
if mibBuilder.loadTexts:
    adslLineConfProfileEntry.setStatus("current")


class _AdslLineConfProfileName_Type(SnmpAdminString):
    """Custom type adslLineConfProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AdslLineConfProfileName_Type.__name__ = "SnmpAdminString"
_AdslLineConfProfileName_Object = MibTableColumn
adslLineConfProfileName = _AdslLineConfProfileName_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 14, 1, 1),
    _AdslLineConfProfileName_Type()
)
adslLineConfProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adslLineConfProfileName.setStatus("current")


class _AdslAtucConfRateMode_Type(Integer32):
    """Custom type adslAtucConfRateMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("adaptAtRuntime", 3),
          ("adaptAtStartup", 2),
          ("fixed", 1))
    )


_AdslAtucConfRateMode_Type.__name__ = "Integer32"
_AdslAtucConfRateMode_Object = MibTableColumn
adslAtucConfRateMode = _AdslAtucConfRateMode_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 14, 1, 2),
    _AdslAtucConfRateMode_Type()
)
adslAtucConfRateMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adslAtucConfRateMode.setStatus("current")


class _AdslAtucConfRateChanRatio_Type(Integer32):
    """Custom type adslAtucConfRateChanRatio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AdslAtucConfRateChanRatio_Type.__name__ = "Integer32"
_AdslAtucConfRateChanRatio_Object = MibTableColumn
adslAtucConfRateChanRatio = _AdslAtucConfRateChanRatio_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 14, 1, 3),
    _AdslAtucConfRateChanRatio_Type()
)
adslAtucConfRateChanRatio.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adslAtucConfRateChanRatio.setStatus("current")
if mibBuilder.loadTexts:
    adslAtucConfRateChanRatio.setUnits("%")


class _AdslAtucConfTargetSnrMgn_Type(Integer32):
    """Custom type adslAtucConfTargetSnrMgn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 310),
    )


_AdslAtucConfTargetSnrMgn_Type.__name__ = "Integer32"
_AdslAtucConfTargetSnrMgn_Object = MibTableColumn
adslAtucConfTargetSnrMgn = _AdslAtucConfTargetSnrMgn_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 14, 1, 4),
    _AdslAtucConfTargetSnrMgn_Type()
)
adslAtucConfTargetSnrMgn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adslAtucConfTargetSnrMgn.setStatus("current")
if mibBuilder.loadTexts:
    adslAtucConfTargetSnrMgn.setUnits("tenth dB")


class _AdslAtucConfMaxSnrMgn_Type(Integer32):
    """Custom type adslAtucConfMaxSnrMgn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 310),
    )


_AdslAtucConfMaxSnrMgn_Type.__name__ = "Integer32"
_AdslAtucConfMaxSnrMgn_Object = MibTableColumn
adslAtucConfMaxSnrMgn = _AdslAtucConfMaxSnrMgn_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 14, 1, 5),
    _AdslAtucConfMaxSnrMgn_Type()
)
adslAtucConfMaxSnrMgn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adslAtucConfMaxSnrMgn.setStatus("current")
if mibBuilder.loadTexts:
    adslAtucConfMaxSnrMgn.setUnits("tenth dB")


class _AdslAtucConfMinSnrMgn_Type(Integer32):
    """Custom type adslAtucConfMinSnrMgn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 310),
    )


_AdslAtucConfMinSnrMgn_Type.__name__ = "Integer32"
_AdslAtucConfMinSnrMgn_Object = MibTableColumn
adslAtucConfMinSnrMgn = _AdslAtucConfMinSnrMgn_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 14, 1, 6),
    _AdslAtucConfMinSnrMgn_Type()
)
adslAtucConfMinSnrMgn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adslAtucConfMinSnrMgn.setStatus("current")
if mibBuilder.loadTexts:
    adslAtucConfMinSnrMgn.setUnits("tenth dB")


class _AdslAtucConfDownshiftSnrMgn_Type(Integer32):
    """Custom type adslAtucConfDownshiftSnrMgn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 310),
    )


_AdslAtucConfDownshiftSnrMgn_Type.__name__ = "Integer32"
_AdslAtucConfDownshiftSnrMgn_Object = MibTableColumn
adslAtucConfDownshiftSnrMgn = _AdslAtucConfDownshiftSnrMgn_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 14, 1, 7),
    _AdslAtucConfDownshiftSnrMgn_Type()
)
adslAtucConfDownshiftSnrMgn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adslAtucConfDownshiftSnrMgn.setStatus("current")
if mibBuilder.loadTexts:
    adslAtucConfDownshiftSnrMgn.setUnits("tenth dB")


class _AdslAtucConfUpshiftSnrMgn_Type(Integer32):
    """Custom type adslAtucConfUpshiftSnrMgn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 310),
    )


_AdslAtucConfUpshiftSnrMgn_Type.__name__ = "Integer32"
_AdslAtucConfUpshiftSnrMgn_Object = MibTableColumn
adslAtucConfUpshiftSnrMgn = _AdslAtucConfUpshiftSnrMgn_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 14, 1, 8),
    _AdslAtucConfUpshiftSnrMgn_Type()
)
adslAtucConfUpshiftSnrMgn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adslAtucConfUpshiftSnrMgn.setStatus("current")
if mibBuilder.loadTexts:
    adslAtucConfUpshiftSnrMgn.setUnits("tenth dB")


class _AdslAtucConfMinUpshiftTime_Type(Integer32):
    """Custom type adslAtucConfMinUpshiftTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16383),
    )


_AdslAtucConfMinUpshiftTime_Type.__name__ = "Integer32"
_AdslAtucConfMinUpshiftTime_Object = MibTableColumn
adslAtucConfMinUpshiftTime = _AdslAtucConfMinUpshiftTime_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 14, 1, 9),
    _AdslAtucConfMinUpshiftTime_Type()
)
adslAtucConfMinUpshiftTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adslAtucConfMinUpshiftTime.setStatus("current")
if mibBuilder.loadTexts:
    adslAtucConfMinUpshiftTime.setUnits("seconds")


class _AdslAtucConfMinDownshiftTime_Type(Integer32):
    """Custom type adslAtucConfMinDownshiftTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16383),
    )


_AdslAtucConfMinDownshiftTime_Type.__name__ = "Integer32"
_AdslAtucConfMinDownshiftTime_Object = MibTableColumn
adslAtucConfMinDownshiftTime = _AdslAtucConfMinDownshiftTime_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 14, 1, 10),
    _AdslAtucConfMinDownshiftTime_Type()
)
adslAtucConfMinDownshiftTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adslAtucConfMinDownshiftTime.setStatus("current")
if mibBuilder.loadTexts:
    adslAtucConfMinDownshiftTime.setUnits("seconds")
_AdslAtucChanConfFastMinTxRate_Type = Unsigned32
_AdslAtucChanConfFastMinTxRate_Object = MibTableColumn
adslAtucChanConfFastMinTxRate = _AdslAtucChanConfFastMinTxRate_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 14, 1, 11),
    _AdslAtucChanConfFastMinTxRate_Type()
)
adslAtucChanConfFastMinTxRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adslAtucChanConfFastMinTxRate.setStatus("current")
if mibBuilder.loadTexts:
    adslAtucChanConfFastMinTxRate.setUnits("bps")
_AdslAtucChanConfInterleaveMinTxRate_Type = Unsigned32
_AdslAtucChanConfInterleaveMinTxRate_Object = MibTableColumn
adslAtucChanConfInterleaveMinTxRate = _AdslAtucChanConfInterleaveMinTxRate_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 14, 1, 12),
    _AdslAtucChanConfInterleaveMinTxRate_Type()
)
adslAtucChanConfInterleaveMinTxRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adslAtucChanConfInterleaveMinTxRate.setStatus("current")
if mibBuilder.loadTexts:
    adslAtucChanConfInterleaveMinTxRate.setUnits("bps")
_AdslAtucChanConfFastMaxTxRate_Type = Unsigned32
_AdslAtucChanConfFastMaxTxRate_Object = MibTableColumn
adslAtucChanConfFastMaxTxRate = _AdslAtucChanConfFastMaxTxRate_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 14, 1, 13),
    _AdslAtucChanConfFastMaxTxRate_Type()
)
adslAtucChanConfFastMaxTxRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adslAtucChanConfFastMaxTxRate.setStatus("current")
if mibBuilder.loadTexts:
    adslAtucChanConfFastMaxTxRate.setUnits("bps")
_AdslAtucChanConfInterleaveMaxTxRate_Type = Unsigned32
_AdslAtucChanConfInterleaveMaxTxRate_Object = MibTableColumn
adslAtucChanConfInterleaveMaxTxRate = _AdslAtucChanConfInterleaveMaxTxRate_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 14, 1, 14),
    _AdslAtucChanConfInterleaveMaxTxRate_Type()
)
adslAtucChanConfInterleaveMaxTxRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adslAtucChanConfInterleaveMaxTxRate.setStatus("current")
if mibBuilder.loadTexts:
    adslAtucChanConfInterleaveMaxTxRate.setUnits("bps")


class _AdslAtucChanConfMaxInterleaveDelay_Type(Integer32):
    """Custom type adslAtucChanConfMaxInterleaveDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AdslAtucChanConfMaxInterleaveDelay_Type.__name__ = "Integer32"
_AdslAtucChanConfMaxInterleaveDelay_Object = MibTableColumn
adslAtucChanConfMaxInterleaveDelay = _AdslAtucChanConfMaxInterleaveDelay_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 14, 1, 15),
    _AdslAtucChanConfMaxInterleaveDelay_Type()
)
adslAtucChanConfMaxInterleaveDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adslAtucChanConfMaxInterleaveDelay.setStatus("current")
if mibBuilder.loadTexts:
    adslAtucChanConfMaxInterleaveDelay.setUnits("milli-seconds")


class _AdslAturConfRateMode_Type(Integer32):
    """Custom type adslAturConfRateMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("adaptAtRuntime", 3),
          ("adaptAtStartup", 2),
          ("fixed", 1))
    )


_AdslAturConfRateMode_Type.__name__ = "Integer32"
_AdslAturConfRateMode_Object = MibTableColumn
adslAturConfRateMode = _AdslAturConfRateMode_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 14, 1, 16),
    _AdslAturConfRateMode_Type()
)
adslAturConfRateMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adslAturConfRateMode.setStatus("current")


class _AdslAturConfRateChanRatio_Type(Integer32):
    """Custom type adslAturConfRateChanRatio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AdslAturConfRateChanRatio_Type.__name__ = "Integer32"
_AdslAturConfRateChanRatio_Object = MibTableColumn
adslAturConfRateChanRatio = _AdslAturConfRateChanRatio_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 14, 1, 17),
    _AdslAturConfRateChanRatio_Type()
)
adslAturConfRateChanRatio.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adslAturConfRateChanRatio.setStatus("current")
if mibBuilder.loadTexts:
    adslAturConfRateChanRatio.setUnits("%")


class _AdslAturConfTargetSnrMgn_Type(Integer32):
    """Custom type adslAturConfTargetSnrMgn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 310),
    )


_AdslAturConfTargetSnrMgn_Type.__name__ = "Integer32"
_AdslAturConfTargetSnrMgn_Object = MibTableColumn
adslAturConfTargetSnrMgn = _AdslAturConfTargetSnrMgn_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 14, 1, 18),
    _AdslAturConfTargetSnrMgn_Type()
)
adslAturConfTargetSnrMgn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adslAturConfTargetSnrMgn.setStatus("current")
if mibBuilder.loadTexts:
    adslAturConfTargetSnrMgn.setUnits("tenth dB")


class _AdslAturConfMaxSnrMgn_Type(Integer32):
    """Custom type adslAturConfMaxSnrMgn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 310),
    )


_AdslAturConfMaxSnrMgn_Type.__name__ = "Integer32"
_AdslAturConfMaxSnrMgn_Object = MibTableColumn
adslAturConfMaxSnrMgn = _AdslAturConfMaxSnrMgn_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 14, 1, 19),
    _AdslAturConfMaxSnrMgn_Type()
)
adslAturConfMaxSnrMgn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adslAturConfMaxSnrMgn.setStatus("current")
if mibBuilder.loadTexts:
    adslAturConfMaxSnrMgn.setUnits("tenth dB")


class _AdslAturConfMinSnrMgn_Type(Integer32):
    """Custom type adslAturConfMinSnrMgn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 310),
    )


_AdslAturConfMinSnrMgn_Type.__name__ = "Integer32"
_AdslAturConfMinSnrMgn_Object = MibTableColumn
adslAturConfMinSnrMgn = _AdslAturConfMinSnrMgn_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 14, 1, 20),
    _AdslAturConfMinSnrMgn_Type()
)
adslAturConfMinSnrMgn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adslAturConfMinSnrMgn.setStatus("current")
if mibBuilder.loadTexts:
    adslAturConfMinSnrMgn.setUnits("tenth dB")


class _AdslAturConfDownshiftSnrMgn_Type(Integer32):
    """Custom type adslAturConfDownshiftSnrMgn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 310),
    )


_AdslAturConfDownshiftSnrMgn_Type.__name__ = "Integer32"
_AdslAturConfDownshiftSnrMgn_Object = MibTableColumn
adslAturConfDownshiftSnrMgn = _AdslAturConfDownshiftSnrMgn_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 14, 1, 21),
    _AdslAturConfDownshiftSnrMgn_Type()
)
adslAturConfDownshiftSnrMgn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adslAturConfDownshiftSnrMgn.setStatus("current")
if mibBuilder.loadTexts:
    adslAturConfDownshiftSnrMgn.setUnits("tenth dB")


class _AdslAturConfUpshiftSnrMgn_Type(Integer32):
    """Custom type adslAturConfUpshiftSnrMgn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 310),
    )


_AdslAturConfUpshiftSnrMgn_Type.__name__ = "Integer32"
_AdslAturConfUpshiftSnrMgn_Object = MibTableColumn
adslAturConfUpshiftSnrMgn = _AdslAturConfUpshiftSnrMgn_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 14, 1, 22),
    _AdslAturConfUpshiftSnrMgn_Type()
)
adslAturConfUpshiftSnrMgn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adslAturConfUpshiftSnrMgn.setStatus("current")
if mibBuilder.loadTexts:
    adslAturConfUpshiftSnrMgn.setUnits("tenth dB")


class _AdslAturConfMinUpshiftTime_Type(Integer32):
    """Custom type adslAturConfMinUpshiftTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16383),
    )


_AdslAturConfMinUpshiftTime_Type.__name__ = "Integer32"
_AdslAturConfMinUpshiftTime_Object = MibTableColumn
adslAturConfMinUpshiftTime = _AdslAturConfMinUpshiftTime_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 14, 1, 23),
    _AdslAturConfMinUpshiftTime_Type()
)
adslAturConfMinUpshiftTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adslAturConfMinUpshiftTime.setStatus("current")
if mibBuilder.loadTexts:
    adslAturConfMinUpshiftTime.setUnits("seconds")


class _AdslAturConfMinDownshiftTime_Type(Integer32):
    """Custom type adslAturConfMinDownshiftTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16383),
    )


_AdslAturConfMinDownshiftTime_Type.__name__ = "Integer32"
_AdslAturConfMinDownshiftTime_Object = MibTableColumn
adslAturConfMinDownshiftTime = _AdslAturConfMinDownshiftTime_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 14, 1, 24),
    _AdslAturConfMinDownshiftTime_Type()
)
adslAturConfMinDownshiftTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adslAturConfMinDownshiftTime.setStatus("current")
if mibBuilder.loadTexts:
    adslAturConfMinDownshiftTime.setUnits("seconds")
_AdslAturChanConfFastMinTxRate_Type = Unsigned32
_AdslAturChanConfFastMinTxRate_Object = MibTableColumn
adslAturChanConfFastMinTxRate = _AdslAturChanConfFastMinTxRate_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 14, 1, 25),
    _AdslAturChanConfFastMinTxRate_Type()
)
adslAturChanConfFastMinTxRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adslAturChanConfFastMinTxRate.setStatus("current")
if mibBuilder.loadTexts:
    adslAturChanConfFastMinTxRate.setUnits("bps")
_AdslAturChanConfInterleaveMinTxRate_Type = Unsigned32
_AdslAturChanConfInterleaveMinTxRate_Object = MibTableColumn
adslAturChanConfInterleaveMinTxRate = _AdslAturChanConfInterleaveMinTxRate_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 14, 1, 26),
    _AdslAturChanConfInterleaveMinTxRate_Type()
)
adslAturChanConfInterleaveMinTxRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adslAturChanConfInterleaveMinTxRate.setStatus("current")
if mibBuilder.loadTexts:
    adslAturChanConfInterleaveMinTxRate.setUnits("bps")
_AdslAturChanConfFastMaxTxRate_Type = Unsigned32
_AdslAturChanConfFastMaxTxRate_Object = MibTableColumn
adslAturChanConfFastMaxTxRate = _AdslAturChanConfFastMaxTxRate_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 14, 1, 27),
    _AdslAturChanConfFastMaxTxRate_Type()
)
adslAturChanConfFastMaxTxRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adslAturChanConfFastMaxTxRate.setStatus("current")
if mibBuilder.loadTexts:
    adslAturChanConfFastMaxTxRate.setUnits("bps")
_AdslAturChanConfInterleaveMaxTxRate_Type = Unsigned32
_AdslAturChanConfInterleaveMaxTxRate_Object = MibTableColumn
adslAturChanConfInterleaveMaxTxRate = _AdslAturChanConfInterleaveMaxTxRate_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 14, 1, 28),
    _AdslAturChanConfInterleaveMaxTxRate_Type()
)
adslAturChanConfInterleaveMaxTxRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adslAturChanConfInterleaveMaxTxRate.setStatus("current")
if mibBuilder.loadTexts:
    adslAturChanConfInterleaveMaxTxRate.setUnits("bps")


class _AdslAturChanConfMaxInterleaveDelay_Type(Integer32):
    """Custom type adslAturChanConfMaxInterleaveDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AdslAturChanConfMaxInterleaveDelay_Type.__name__ = "Integer32"
_AdslAturChanConfMaxInterleaveDelay_Object = MibTableColumn
adslAturChanConfMaxInterleaveDelay = _AdslAturChanConfMaxInterleaveDelay_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 14, 1, 29),
    _AdslAturChanConfMaxInterleaveDelay_Type()
)
adslAturChanConfMaxInterleaveDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adslAturChanConfMaxInterleaveDelay.setStatus("current")
if mibBuilder.loadTexts:
    adslAturChanConfMaxInterleaveDelay.setUnits("milli-seconds")
_AdslLineConfProfileRowStatus_Type = RowStatus
_AdslLineConfProfileRowStatus_Object = MibTableColumn
adslLineConfProfileRowStatus = _AdslLineConfProfileRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 14, 1, 30),
    _AdslLineConfProfileRowStatus_Type()
)
adslLineConfProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adslLineConfProfileRowStatus.setStatus("current")
_AdslLineAlarmConfProfileTable_Object = MibTable
adslLineAlarmConfProfileTable = _AdslLineAlarmConfProfileTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 15)
)
if mibBuilder.loadTexts:
    adslLineAlarmConfProfileTable.setStatus("current")
_AdslLineAlarmConfProfileEntry_Object = MibTableRow
adslLineAlarmConfProfileEntry = _AdslLineAlarmConfProfileEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 15, 1)
)
adslLineAlarmConfProfileEntry.setIndexNames(
    (1, "ADSL-LINE-MIB", "adslLineAlarmConfProfileName"),
)
if mibBuilder.loadTexts:
    adslLineAlarmConfProfileEntry.setStatus("current")


class _AdslLineAlarmConfProfileName_Type(SnmpAdminString):
    """Custom type adslLineAlarmConfProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AdslLineAlarmConfProfileName_Type.__name__ = "SnmpAdminString"
_AdslLineAlarmConfProfileName_Object = MibTableColumn
adslLineAlarmConfProfileName = _AdslLineAlarmConfProfileName_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 15, 1, 1),
    _AdslLineAlarmConfProfileName_Type()
)
adslLineAlarmConfProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adslLineAlarmConfProfileName.setStatus("current")


class _AdslAtucThresh15MinLofs_Type(Integer32):
    """Custom type adslAtucThresh15MinLofs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_AdslAtucThresh15MinLofs_Type.__name__ = "Integer32"
_AdslAtucThresh15MinLofs_Object = MibTableColumn
adslAtucThresh15MinLofs = _AdslAtucThresh15MinLofs_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 15, 1, 2),
    _AdslAtucThresh15MinLofs_Type()
)
adslAtucThresh15MinLofs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adslAtucThresh15MinLofs.setStatus("current")
if mibBuilder.loadTexts:
    adslAtucThresh15MinLofs.setUnits("seconds")


class _AdslAtucThresh15MinLoss_Type(Integer32):
    """Custom type adslAtucThresh15MinLoss based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_AdslAtucThresh15MinLoss_Type.__name__ = "Integer32"
_AdslAtucThresh15MinLoss_Object = MibTableColumn
adslAtucThresh15MinLoss = _AdslAtucThresh15MinLoss_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 15, 1, 3),
    _AdslAtucThresh15MinLoss_Type()
)
adslAtucThresh15MinLoss.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adslAtucThresh15MinLoss.setStatus("current")
if mibBuilder.loadTexts:
    adslAtucThresh15MinLoss.setUnits("seconds")


class _AdslAtucThresh15MinLols_Type(Integer32):
    """Custom type adslAtucThresh15MinLols based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_AdslAtucThresh15MinLols_Type.__name__ = "Integer32"
_AdslAtucThresh15MinLols_Object = MibTableColumn
adslAtucThresh15MinLols = _AdslAtucThresh15MinLols_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 15, 1, 4),
    _AdslAtucThresh15MinLols_Type()
)
adslAtucThresh15MinLols.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adslAtucThresh15MinLols.setStatus("current")
if mibBuilder.loadTexts:
    adslAtucThresh15MinLols.setUnits("seconds")


class _AdslAtucThresh15MinLprs_Type(Integer32):
    """Custom type adslAtucThresh15MinLprs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_AdslAtucThresh15MinLprs_Type.__name__ = "Integer32"
_AdslAtucThresh15MinLprs_Object = MibTableColumn
adslAtucThresh15MinLprs = _AdslAtucThresh15MinLprs_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 15, 1, 5),
    _AdslAtucThresh15MinLprs_Type()
)
adslAtucThresh15MinLprs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adslAtucThresh15MinLprs.setStatus("current")
if mibBuilder.loadTexts:
    adslAtucThresh15MinLprs.setUnits("seconds")


class _AdslAtucThresh15MinESs_Type(Integer32):
    """Custom type adslAtucThresh15MinESs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_AdslAtucThresh15MinESs_Type.__name__ = "Integer32"
_AdslAtucThresh15MinESs_Object = MibTableColumn
adslAtucThresh15MinESs = _AdslAtucThresh15MinESs_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 15, 1, 6),
    _AdslAtucThresh15MinESs_Type()
)
adslAtucThresh15MinESs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adslAtucThresh15MinESs.setStatus("current")
if mibBuilder.loadTexts:
    adslAtucThresh15MinESs.setUnits("seconds")
_AdslAtucThreshFastRateUp_Type = Unsigned32
_AdslAtucThreshFastRateUp_Object = MibTableColumn
adslAtucThreshFastRateUp = _AdslAtucThreshFastRateUp_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 15, 1, 7),
    _AdslAtucThreshFastRateUp_Type()
)
adslAtucThreshFastRateUp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adslAtucThreshFastRateUp.setStatus("current")
if mibBuilder.loadTexts:
    adslAtucThreshFastRateUp.setUnits("bps")
_AdslAtucThreshInterleaveRateUp_Type = Unsigned32
_AdslAtucThreshInterleaveRateUp_Object = MibTableColumn
adslAtucThreshInterleaveRateUp = _AdslAtucThreshInterleaveRateUp_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 15, 1, 8),
    _AdslAtucThreshInterleaveRateUp_Type()
)
adslAtucThreshInterleaveRateUp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adslAtucThreshInterleaveRateUp.setStatus("current")
if mibBuilder.loadTexts:
    adslAtucThreshInterleaveRateUp.setUnits("bps")
_AdslAtucThreshFastRateDown_Type = Unsigned32
_AdslAtucThreshFastRateDown_Object = MibTableColumn
adslAtucThreshFastRateDown = _AdslAtucThreshFastRateDown_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 15, 1, 9),
    _AdslAtucThreshFastRateDown_Type()
)
adslAtucThreshFastRateDown.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adslAtucThreshFastRateDown.setStatus("current")
if mibBuilder.loadTexts:
    adslAtucThreshFastRateDown.setUnits("bps")
_AdslAtucThreshInterleaveRateDown_Type = Unsigned32
_AdslAtucThreshInterleaveRateDown_Object = MibTableColumn
adslAtucThreshInterleaveRateDown = _AdslAtucThreshInterleaveRateDown_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 15, 1, 10),
    _AdslAtucThreshInterleaveRateDown_Type()
)
adslAtucThreshInterleaveRateDown.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adslAtucThreshInterleaveRateDown.setStatus("current")
if mibBuilder.loadTexts:
    adslAtucThreshInterleaveRateDown.setUnits("bps")


class _AdslAtucInitFailureTrapEnable_Type(Integer32):
    """Custom type adslAtucInitFailureTrapEnable based on Integer32"""
    defaultValue = 2

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


_AdslAtucInitFailureTrapEnable_Type.__name__ = "Integer32"
_AdslAtucInitFailureTrapEnable_Object = MibTableColumn
adslAtucInitFailureTrapEnable = _AdslAtucInitFailureTrapEnable_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 15, 1, 11),
    _AdslAtucInitFailureTrapEnable_Type()
)
adslAtucInitFailureTrapEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adslAtucInitFailureTrapEnable.setStatus("current")


class _AdslAturThresh15MinLofs_Type(Integer32):
    """Custom type adslAturThresh15MinLofs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_AdslAturThresh15MinLofs_Type.__name__ = "Integer32"
_AdslAturThresh15MinLofs_Object = MibTableColumn
adslAturThresh15MinLofs = _AdslAturThresh15MinLofs_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 15, 1, 12),
    _AdslAturThresh15MinLofs_Type()
)
adslAturThresh15MinLofs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adslAturThresh15MinLofs.setStatus("current")
if mibBuilder.loadTexts:
    adslAturThresh15MinLofs.setUnits("seconds")


class _AdslAturThresh15MinLoss_Type(Integer32):
    """Custom type adslAturThresh15MinLoss based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_AdslAturThresh15MinLoss_Type.__name__ = "Integer32"
_AdslAturThresh15MinLoss_Object = MibTableColumn
adslAturThresh15MinLoss = _AdslAturThresh15MinLoss_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 15, 1, 13),
    _AdslAturThresh15MinLoss_Type()
)
adslAturThresh15MinLoss.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adslAturThresh15MinLoss.setStatus("current")
if mibBuilder.loadTexts:
    adslAturThresh15MinLoss.setUnits("seconds")


class _AdslAturThresh15MinLprs_Type(Integer32):
    """Custom type adslAturThresh15MinLprs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_AdslAturThresh15MinLprs_Type.__name__ = "Integer32"
_AdslAturThresh15MinLprs_Object = MibTableColumn
adslAturThresh15MinLprs = _AdslAturThresh15MinLprs_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 15, 1, 14),
    _AdslAturThresh15MinLprs_Type()
)
adslAturThresh15MinLprs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adslAturThresh15MinLprs.setStatus("current")
if mibBuilder.loadTexts:
    adslAturThresh15MinLprs.setUnits("seconds")


class _AdslAturThresh15MinESs_Type(Integer32):
    """Custom type adslAturThresh15MinESs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_AdslAturThresh15MinESs_Type.__name__ = "Integer32"
_AdslAturThresh15MinESs_Object = MibTableColumn
adslAturThresh15MinESs = _AdslAturThresh15MinESs_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 15, 1, 15),
    _AdslAturThresh15MinESs_Type()
)
adslAturThresh15MinESs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adslAturThresh15MinESs.setStatus("current")
if mibBuilder.loadTexts:
    adslAturThresh15MinESs.setUnits("seconds")
_AdslAturThreshFastRateUp_Type = Unsigned32
_AdslAturThreshFastRateUp_Object = MibTableColumn
adslAturThreshFastRateUp = _AdslAturThreshFastRateUp_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 15, 1, 16),
    _AdslAturThreshFastRateUp_Type()
)
adslAturThreshFastRateUp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adslAturThreshFastRateUp.setStatus("current")
if mibBuilder.loadTexts:
    adslAturThreshFastRateUp.setUnits("bps")
_AdslAturThreshInterleaveRateUp_Type = Unsigned32
_AdslAturThreshInterleaveRateUp_Object = MibTableColumn
adslAturThreshInterleaveRateUp = _AdslAturThreshInterleaveRateUp_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 15, 1, 17),
    _AdslAturThreshInterleaveRateUp_Type()
)
adslAturThreshInterleaveRateUp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adslAturThreshInterleaveRateUp.setStatus("current")
if mibBuilder.loadTexts:
    adslAturThreshInterleaveRateUp.setUnits("bps")
_AdslAturThreshFastRateDown_Type = Unsigned32
_AdslAturThreshFastRateDown_Object = MibTableColumn
adslAturThreshFastRateDown = _AdslAturThreshFastRateDown_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 15, 1, 18),
    _AdslAturThreshFastRateDown_Type()
)
adslAturThreshFastRateDown.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adslAturThreshFastRateDown.setStatus("current")
if mibBuilder.loadTexts:
    adslAturThreshFastRateDown.setUnits("bps")
_AdslAturThreshInterleaveRateDown_Type = Unsigned32
_AdslAturThreshInterleaveRateDown_Object = MibTableColumn
adslAturThreshInterleaveRateDown = _AdslAturThreshInterleaveRateDown_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 15, 1, 19),
    _AdslAturThreshInterleaveRateDown_Type()
)
adslAturThreshInterleaveRateDown.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adslAturThreshInterleaveRateDown.setStatus("current")
if mibBuilder.loadTexts:
    adslAturThreshInterleaveRateDown.setUnits("bps")
_AdslLineAlarmConfProfileRowStatus_Type = RowStatus
_AdslLineAlarmConfProfileRowStatus_Object = MibTableColumn
adslLineAlarmConfProfileRowStatus = _AdslLineAlarmConfProfileRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 15, 1, 20),
    _AdslLineAlarmConfProfileRowStatus_Type()
)
adslLineAlarmConfProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adslLineAlarmConfProfileRowStatus.setStatus("current")
_AdslLCSMib_ObjectIdentity = ObjectIdentity
adslLCSMib = _AdslLCSMib_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 1, 16)
)
_AdslTraps_ObjectIdentity = ObjectIdentity
adslTraps = _AdslTraps_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 2)
)
_AdslAtucTraps_ObjectIdentity = ObjectIdentity
adslAtucTraps = _AdslAtucTraps_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 2, 1)
)
_AdslAturTraps_ObjectIdentity = ObjectIdentity
adslAturTraps = _AdslAturTraps_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 2, 2)
)
_AdslConformance_ObjectIdentity = ObjectIdentity
adslConformance = _AdslConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 3)
)
_AdslGroups_ObjectIdentity = ObjectIdentity
adslGroups = _AdslGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 3, 1)
)
_AdslCompliances_ObjectIdentity = ObjectIdentity
adslCompliances = _AdslCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 3, 2)
)

# Managed Objects groups

adslLineGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 3, 1, 1)
)
adslLineGroup.setObjects(
      *(("ADSL-LINE-MIB", "adslLineCoding"),
        ("ADSL-LINE-MIB", "adslLineType"),
        ("ADSL-LINE-MIB", "adslLineSpecific"))
)
if mibBuilder.loadTexts:
    adslLineGroup.setStatus("current")

adslPhysicalGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 3, 1, 2)
)
adslPhysicalGroup.setObjects(
      *(("ADSL-LINE-MIB", "adslAtucInvSerialNumber"),
        ("ADSL-LINE-MIB", "adslAtucInvVendorID"),
        ("ADSL-LINE-MIB", "adslAtucInvVersionNumber"),
        ("ADSL-LINE-MIB", "adslAtucCurrSnrMgn"),
        ("ADSL-LINE-MIB", "adslAtucCurrAtn"),
        ("ADSL-LINE-MIB", "adslAtucCurrStatus"),
        ("ADSL-LINE-MIB", "adslAtucCurrOutputPwr"),
        ("ADSL-LINE-MIB", "adslAtucCurrAttainableRate"),
        ("ADSL-LINE-MIB", "adslAturInvSerialNumber"),
        ("ADSL-LINE-MIB", "adslAturInvVendorID"),
        ("ADSL-LINE-MIB", "adslAturInvVersionNumber"),
        ("ADSL-LINE-MIB", "adslAturCurrSnrMgn"),
        ("ADSL-LINE-MIB", "adslAturCurrAtn"),
        ("ADSL-LINE-MIB", "adslAturCurrStatus"),
        ("ADSL-LINE-MIB", "adslAturCurrOutputPwr"),
        ("ADSL-LINE-MIB", "adslAturCurrAttainableRate"))
)
if mibBuilder.loadTexts:
    adslPhysicalGroup.setStatus("current")

adslChannelGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 3, 1, 3)
)
adslChannelGroup.setObjects(
      *(("ADSL-LINE-MIB", "adslAtucChanInterleaveDelay"),
        ("ADSL-LINE-MIB", "adslAtucChanCurrTxRate"),
        ("ADSL-LINE-MIB", "adslAtucChanPrevTxRate"),
        ("ADSL-LINE-MIB", "adslAtucChanCrcBlockLength"),
        ("ADSL-LINE-MIB", "adslAturChanInterleaveDelay"),
        ("ADSL-LINE-MIB", "adslAturChanCurrTxRate"),
        ("ADSL-LINE-MIB", "adslAturChanPrevTxRate"),
        ("ADSL-LINE-MIB", "adslAturChanCrcBlockLength"))
)
if mibBuilder.loadTexts:
    adslChannelGroup.setStatus("current")

adslAtucPhysPerfRawCounterGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 3, 1, 4)
)
adslAtucPhysPerfRawCounterGroup.setObjects(
      *(("ADSL-LINE-MIB", "adslAtucPerfLofs"),
        ("ADSL-LINE-MIB", "adslAtucPerfLoss"),
        ("ADSL-LINE-MIB", "adslAtucPerfLols"),
        ("ADSL-LINE-MIB", "adslAtucPerfLprs"),
        ("ADSL-LINE-MIB", "adslAtucPerfESs"),
        ("ADSL-LINE-MIB", "adslAtucPerfInits"))
)
if mibBuilder.loadTexts:
    adslAtucPhysPerfRawCounterGroup.setStatus("current")

adslAtucPhysPerfIntervalGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 3, 1, 5)
)
adslAtucPhysPerfIntervalGroup.setObjects(
      *(("ADSL-LINE-MIB", "adslAtucPerfValidIntervals"),
        ("ADSL-LINE-MIB", "adslAtucPerfInvalidIntervals"),
        ("ADSL-LINE-MIB", "adslAtucPerfCurr15MinTimeElapsed"),
        ("ADSL-LINE-MIB", "adslAtucPerfCurr15MinLofs"),
        ("ADSL-LINE-MIB", "adslAtucPerfCurr15MinLoss"),
        ("ADSL-LINE-MIB", "adslAtucPerfCurr15MinLols"),
        ("ADSL-LINE-MIB", "adslAtucPerfCurr15MinLprs"),
        ("ADSL-LINE-MIB", "adslAtucPerfCurr15MinESs"),
        ("ADSL-LINE-MIB", "adslAtucPerfCurr15MinInits"),
        ("ADSL-LINE-MIB", "adslAtucPerfCurr1DayLofs"),
        ("ADSL-LINE-MIB", "adslAtucPerfCurr1DayLoss"),
        ("ADSL-LINE-MIB", "adslAtucPerfCurr1DayLols"),
        ("ADSL-LINE-MIB", "adslAtucPerfCurr1DayLprs"),
        ("ADSL-LINE-MIB", "adslAtucPerfCurr1DayESs"),
        ("ADSL-LINE-MIB", "adslAtucPerfCurr1DayInits"),
        ("ADSL-LINE-MIB", "adslAtucPerfPrev1DayMoniSecs"),
        ("ADSL-LINE-MIB", "adslAtucPerfPrev1DayLofs"),
        ("ADSL-LINE-MIB", "adslAtucPerfPrev1DayLoss"),
        ("ADSL-LINE-MIB", "adslAtucPerfPrev1DayLols"),
        ("ADSL-LINE-MIB", "adslAtucPerfPrev1DayLprs"),
        ("ADSL-LINE-MIB", "adslAtucPerfPrev1DayESs"),
        ("ADSL-LINE-MIB", "adslAtucPerfPrev1DayInits"),
        ("ADSL-LINE-MIB", "adslAtucIntervalLofs"),
        ("ADSL-LINE-MIB", "adslAtucIntervalLoss"),
        ("ADSL-LINE-MIB", "adslAtucIntervalLols"),
        ("ADSL-LINE-MIB", "adslAtucIntervalLprs"),
        ("ADSL-LINE-MIB", "adslAtucIntervalESs"),
        ("ADSL-LINE-MIB", "adslAtucIntervalInits"),
        ("ADSL-LINE-MIB", "adslAtucIntervalValidData"))
)
if mibBuilder.loadTexts:
    adslAtucPhysPerfIntervalGroup.setStatus("current")

adslAturPhysPerfRawCounterGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 3, 1, 6)
)
adslAturPhysPerfRawCounterGroup.setObjects(
      *(("ADSL-LINE-MIB", "adslAturPerfLofs"),
        ("ADSL-LINE-MIB", "adslAturPerfLoss"),
        ("ADSL-LINE-MIB", "adslAturPerfLprs"),
        ("ADSL-LINE-MIB", "adslAturPerfESs"))
)
if mibBuilder.loadTexts:
    adslAturPhysPerfRawCounterGroup.setStatus("current")

adslAturPhysPerfIntervalGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 3, 1, 7)
)
adslAturPhysPerfIntervalGroup.setObjects(
      *(("ADSL-LINE-MIB", "adslAturPerfValidIntervals"),
        ("ADSL-LINE-MIB", "adslAturPerfInvalidIntervals"),
        ("ADSL-LINE-MIB", "adslAturPerfCurr15MinTimeElapsed"),
        ("ADSL-LINE-MIB", "adslAturPerfCurr15MinLofs"),
        ("ADSL-LINE-MIB", "adslAturPerfCurr15MinLoss"),
        ("ADSL-LINE-MIB", "adslAturPerfCurr15MinLprs"),
        ("ADSL-LINE-MIB", "adslAturPerfCurr15MinESs"),
        ("ADSL-LINE-MIB", "adslAturPerfCurr1DayTimeElapsed"),
        ("ADSL-LINE-MIB", "adslAturPerfCurr1DayLofs"),
        ("ADSL-LINE-MIB", "adslAturPerfCurr1DayLoss"),
        ("ADSL-LINE-MIB", "adslAturPerfCurr1DayLprs"),
        ("ADSL-LINE-MIB", "adslAturPerfCurr1DayESs"),
        ("ADSL-LINE-MIB", "adslAturPerfPrev1DayMoniSecs"),
        ("ADSL-LINE-MIB", "adslAturPerfPrev1DayLofs"),
        ("ADSL-LINE-MIB", "adslAturPerfPrev1DayLoss"),
        ("ADSL-LINE-MIB", "adslAturPerfPrev1DayLprs"),
        ("ADSL-LINE-MIB", "adslAturPerfPrev1DayESs"),
        ("ADSL-LINE-MIB", "adslAturIntervalLofs"),
        ("ADSL-LINE-MIB", "adslAturIntervalLoss"),
        ("ADSL-LINE-MIB", "adslAturIntervalLprs"),
        ("ADSL-LINE-MIB", "adslAturIntervalESs"),
        ("ADSL-LINE-MIB", "adslAturIntervalValidData"))
)
if mibBuilder.loadTexts:
    adslAturPhysPerfIntervalGroup.setStatus("current")

adslAtucChanPerformanceGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 3, 1, 8)
)
adslAtucChanPerformanceGroup.setObjects(
      *(("ADSL-LINE-MIB", "adslAtucChanReceivedBlks"),
        ("ADSL-LINE-MIB", "adslAtucChanTransmittedBlks"),
        ("ADSL-LINE-MIB", "adslAtucChanCorrectedBlks"),
        ("ADSL-LINE-MIB", "adslAtucChanUncorrectBlks"),
        ("ADSL-LINE-MIB", "adslAtucChanPerfValidIntervals"),
        ("ADSL-LINE-MIB", "adslAtucChanPerfInvalidIntervals"),
        ("ADSL-LINE-MIB", "adslAtucChanPerfCurr15MinTimeElapsed"),
        ("ADSL-LINE-MIB", "adslAtucChanPerfCurr15MinReceivedBlks"),
        ("ADSL-LINE-MIB", "adslAtucChanPerfCurr15MinTransmittedBlks"),
        ("ADSL-LINE-MIB", "adslAtucChanPerfCurr15MinCorrectedBlks"),
        ("ADSL-LINE-MIB", "adslAtucChanPerfCurr15MinUncorrectBlks"),
        ("ADSL-LINE-MIB", "adslAtucChanPerfCurr1DayTimeElapsed"),
        ("ADSL-LINE-MIB", "adslAtucChanPerfCurr1DayReceivedBlks"),
        ("ADSL-LINE-MIB", "adslAtucChanPerfCurr1DayTransmittedBlks"),
        ("ADSL-LINE-MIB", "adslAtucChanPerfCurr1DayCorrectedBlks"),
        ("ADSL-LINE-MIB", "adslAtucChanPerfCurr1DayUncorrectBlks"),
        ("ADSL-LINE-MIB", "adslAtucChanPerfPrev1DayMoniSecs"),
        ("ADSL-LINE-MIB", "adslAtucChanPerfPrev1DayReceivedBlks"),
        ("ADSL-LINE-MIB", "adslAtucChanPerfPrev1DayTransmittedBlks"),
        ("ADSL-LINE-MIB", "adslAtucChanPerfPrev1DayCorrectedBlks"),
        ("ADSL-LINE-MIB", "adslAtucChanPerfPrev1DayUncorrectBlks"),
        ("ADSL-LINE-MIB", "adslAtucChanIntervalReceivedBlks"),
        ("ADSL-LINE-MIB", "adslAtucChanIntervalTransmittedBlks"),
        ("ADSL-LINE-MIB", "adslAtucChanIntervalCorrectedBlks"),
        ("ADSL-LINE-MIB", "adslAtucChanIntervalUncorrectBlks"),
        ("ADSL-LINE-MIB", "adslAtucChanIntervalValidData"))
)
if mibBuilder.loadTexts:
    adslAtucChanPerformanceGroup.setStatus("current")

adslAturChanPerformanceGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 3, 1, 9)
)
adslAturChanPerformanceGroup.setObjects(
      *(("ADSL-LINE-MIB", "adslAturChanReceivedBlks"),
        ("ADSL-LINE-MIB", "adslAturChanTransmittedBlks"),
        ("ADSL-LINE-MIB", "adslAturChanCorrectedBlks"),
        ("ADSL-LINE-MIB", "adslAturChanUncorrectBlks"),
        ("ADSL-LINE-MIB", "adslAturChanPerfValidIntervals"),
        ("ADSL-LINE-MIB", "adslAturChanPerfInvalidIntervals"),
        ("ADSL-LINE-MIB", "adslAturChanPerfCurr15MinTimeElapsed"),
        ("ADSL-LINE-MIB", "adslAturChanPerfCurr15MinReceivedBlks"),
        ("ADSL-LINE-MIB", "adslAturChanPerfCurr15MinTransmittedBlks"),
        ("ADSL-LINE-MIB", "adslAturChanPerfCurr15MinCorrectedBlks"),
        ("ADSL-LINE-MIB", "adslAturChanPerfCurr15MinUncorrectBlks"),
        ("ADSL-LINE-MIB", "adslAturChanPerfCurr1DayTimeElapsed"),
        ("ADSL-LINE-MIB", "adslAturChanPerfCurr1DayReceivedBlks"),
        ("ADSL-LINE-MIB", "adslAturChanPerfCurr1DayTransmittedBlks"),
        ("ADSL-LINE-MIB", "adslAturChanPerfCurr1DayCorrectedBlks"),
        ("ADSL-LINE-MIB", "adslAturChanPerfCurr1DayUncorrectBlks"),
        ("ADSL-LINE-MIB", "adslAturChanPerfPrev1DayMoniSecs"),
        ("ADSL-LINE-MIB", "adslAturChanPerfPrev1DayReceivedBlks"),
        ("ADSL-LINE-MIB", "adslAturChanPerfPrev1DayTransmittedBlks"),
        ("ADSL-LINE-MIB", "adslAturChanPerfPrev1DayCorrectedBlks"),
        ("ADSL-LINE-MIB", "adslAturChanPerfPrev1DayUncorrectBlks"),
        ("ADSL-LINE-MIB", "adslAturChanIntervalReceivedBlks"),
        ("ADSL-LINE-MIB", "adslAturChanIntervalTransmittedBlks"),
        ("ADSL-LINE-MIB", "adslAturChanIntervalCorrectedBlks"),
        ("ADSL-LINE-MIB", "adslAturChanIntervalUncorrectBlks"),
        ("ADSL-LINE-MIB", "adslAturChanIntervalValidData"))
)
if mibBuilder.loadTexts:
    adslAturChanPerformanceGroup.setStatus("current")

adslLineConfProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 3, 1, 10)
)
adslLineConfProfileGroup.setObjects(
      *(("ADSL-LINE-MIB", "adslAtucConfRateMode"),
        ("ADSL-LINE-MIB", "adslAtucConfRateChanRatio"),
        ("ADSL-LINE-MIB", "adslAtucConfTargetSnrMgn"),
        ("ADSL-LINE-MIB", "adslAtucConfMaxSnrMgn"),
        ("ADSL-LINE-MIB", "adslAtucConfMinSnrMgn"),
        ("ADSL-LINE-MIB", "adslAtucConfDownshiftSnrMgn"),
        ("ADSL-LINE-MIB", "adslAtucConfUpshiftSnrMgn"),
        ("ADSL-LINE-MIB", "adslAtucConfMinUpshiftTime"),
        ("ADSL-LINE-MIB", "adslAtucConfMinDownshiftTime"),
        ("ADSL-LINE-MIB", "adslAtucChanConfFastMinTxRate"),
        ("ADSL-LINE-MIB", "adslAtucChanConfInterleaveMinTxRate"),
        ("ADSL-LINE-MIB", "adslAtucChanConfFastMaxTxRate"),
        ("ADSL-LINE-MIB", "adslAtucChanConfInterleaveMaxTxRate"),
        ("ADSL-LINE-MIB", "adslAtucChanConfMaxInterleaveDelay"),
        ("ADSL-LINE-MIB", "adslAturConfRateMode"),
        ("ADSL-LINE-MIB", "adslAturConfRateChanRatio"),
        ("ADSL-LINE-MIB", "adslAturConfTargetSnrMgn"),
        ("ADSL-LINE-MIB", "adslAturConfMaxSnrMgn"),
        ("ADSL-LINE-MIB", "adslAturConfMinSnrMgn"),
        ("ADSL-LINE-MIB", "adslAturConfDownshiftSnrMgn"),
        ("ADSL-LINE-MIB", "adslAturConfUpshiftSnrMgn"),
        ("ADSL-LINE-MIB", "adslAturConfMinUpshiftTime"),
        ("ADSL-LINE-MIB", "adslAturConfMinDownshiftTime"),
        ("ADSL-LINE-MIB", "adslAturChanConfFastMinTxRate"),
        ("ADSL-LINE-MIB", "adslAturChanConfInterleaveMinTxRate"),
        ("ADSL-LINE-MIB", "adslAturChanConfFastMaxTxRate"),
        ("ADSL-LINE-MIB", "adslAturChanConfInterleaveMaxTxRate"),
        ("ADSL-LINE-MIB", "adslAturChanConfMaxInterleaveDelay"))
)
if mibBuilder.loadTexts:
    adslLineConfProfileGroup.setStatus("current")

adslLineAlarmConfProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 3, 1, 11)
)
adslLineAlarmConfProfileGroup.setObjects(
      *(("ADSL-LINE-MIB", "adslAtucThresh15MinLofs"),
        ("ADSL-LINE-MIB", "adslAtucThresh15MinLoss"),
        ("ADSL-LINE-MIB", "adslAtucThresh15MinLols"),
        ("ADSL-LINE-MIB", "adslAtucThresh15MinLprs"),
        ("ADSL-LINE-MIB", "adslAtucThresh15MinESs"),
        ("ADSL-LINE-MIB", "adslAtucThreshFastRateUp"),
        ("ADSL-LINE-MIB", "adslAtucThreshInterleaveRateUp"),
        ("ADSL-LINE-MIB", "adslAtucThreshFastRateDown"),
        ("ADSL-LINE-MIB", "adslAtucThreshInterleaveRateDown"),
        ("ADSL-LINE-MIB", "adslAtucInitFailureTrapEnable"),
        ("ADSL-LINE-MIB", "adslAturThresh15MinLofs"),
        ("ADSL-LINE-MIB", "adslAturThresh15MinLoss"),
        ("ADSL-LINE-MIB", "adslAturThresh15MinLprs"),
        ("ADSL-LINE-MIB", "adslAturThresh15MinESs"),
        ("ADSL-LINE-MIB", "adslAturThreshFastRateUp"),
        ("ADSL-LINE-MIB", "adslAturThreshInterleaveRateUp"),
        ("ADSL-LINE-MIB", "adslAturThreshFastRateDown"),
        ("ADSL-LINE-MIB", "adslAturThreshInterleaveRateDown"))
)
if mibBuilder.loadTexts:
    adslLineAlarmConfProfileGroup.setStatus("current")

adslLineConfProfileControlGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 3, 1, 12)
)
adslLineConfProfileControlGroup.setObjects(
      *(("ADSL-LINE-MIB", "adslLineConfProfile"),
        ("ADSL-LINE-MIB", "adslLineAlarmConfProfile"),
        ("ADSL-LINE-MIB", "adslLineConfProfileRowStatus"),
        ("ADSL-LINE-MIB", "adslLineAlarmConfProfileRowStatus"))
)
if mibBuilder.loadTexts:
    adslLineConfProfileControlGroup.setStatus("current")

adslAturLineGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 3, 1, 14)
)
adslAturLineGroup.setObjects(
    ("ADSL-LINE-MIB", "adslLineCoding")
)
if mibBuilder.loadTexts:
    adslAturLineGroup.setStatus("current")

adslAturPhysicalGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 3, 1, 15)
)
adslAturPhysicalGroup.setObjects(
      *(("ADSL-LINE-MIB", "adslAtucInvVendorID"),
        ("ADSL-LINE-MIB", "adslAtucInvVersionNumber"),
        ("ADSL-LINE-MIB", "adslAtucCurrOutputPwr"),
        ("ADSL-LINE-MIB", "adslAtucCurrAttainableRate"),
        ("ADSL-LINE-MIB", "adslAturInvSerialNumber"),
        ("ADSL-LINE-MIB", "adslAturInvVendorID"),
        ("ADSL-LINE-MIB", "adslAturInvVersionNumber"),
        ("ADSL-LINE-MIB", "adslAturCurrSnrMgn"),
        ("ADSL-LINE-MIB", "adslAturCurrAtn"),
        ("ADSL-LINE-MIB", "adslAturCurrStatus"),
        ("ADSL-LINE-MIB", "adslAturCurrOutputPwr"),
        ("ADSL-LINE-MIB", "adslAturCurrAttainableRate"),
        ("ADSL-LINE-MIB", "adslAtucCurrStatus"))
)
if mibBuilder.loadTexts:
    adslAturPhysicalGroup.setStatus("current")

adslAturChannelGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 3, 1, 16)
)
adslAturChannelGroup.setObjects(
      *(("ADSL-LINE-MIB", "adslAtucChanInterleaveDelay"),
        ("ADSL-LINE-MIB", "adslAtucChanCurrTxRate"),
        ("ADSL-LINE-MIB", "adslAtucChanPrevTxRate"),
        ("ADSL-LINE-MIB", "adslAturChanInterleaveDelay"),
        ("ADSL-LINE-MIB", "adslAturChanCurrTxRate"),
        ("ADSL-LINE-MIB", "adslAturChanPrevTxRate"),
        ("ADSL-LINE-MIB", "adslAturChanCrcBlockLength"))
)
if mibBuilder.loadTexts:
    adslAturChannelGroup.setStatus("current")

adslAturAtucPhysPerfRawCounterGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 3, 1, 17)
)
adslAturAtucPhysPerfRawCounterGroup.setObjects(
      *(("ADSL-LINE-MIB", "adslAtucPerfLofs"),
        ("ADSL-LINE-MIB", "adslAtucPerfLoss"),
        ("ADSL-LINE-MIB", "adslAtucPerfESs"),
        ("ADSL-LINE-MIB", "adslAtucPerfInits"))
)
if mibBuilder.loadTexts:
    adslAturAtucPhysPerfRawCounterGroup.setStatus("current")

adslAturAtucPhysPerfIntervalGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 3, 1, 18)
)
adslAturAtucPhysPerfIntervalGroup.setObjects(
      *(("ADSL-LINE-MIB", "adslAtucPerfValidIntervals"),
        ("ADSL-LINE-MIB", "adslAtucPerfInvalidIntervals"),
        ("ADSL-LINE-MIB", "adslAtucPerfCurr15MinTimeElapsed"),
        ("ADSL-LINE-MIB", "adslAtucPerfCurr15MinLofs"),
        ("ADSL-LINE-MIB", "adslAtucPerfCurr15MinLoss"),
        ("ADSL-LINE-MIB", "adslAtucPerfCurr15MinESs"),
        ("ADSL-LINE-MIB", "adslAtucPerfCurr15MinInits"),
        ("ADSL-LINE-MIB", "adslAtucPerfCurr1DayTimeElapsed"),
        ("ADSL-LINE-MIB", "adslAtucPerfCurr1DayLofs"),
        ("ADSL-LINE-MIB", "adslAtucPerfCurr1DayLoss"),
        ("ADSL-LINE-MIB", "adslAtucPerfCurr1DayESs"),
        ("ADSL-LINE-MIB", "adslAtucPerfCurr1DayInits"),
        ("ADSL-LINE-MIB", "adslAtucPerfPrev1DayMoniSecs"),
        ("ADSL-LINE-MIB", "adslAtucPerfPrev1DayLofs"),
        ("ADSL-LINE-MIB", "adslAtucPerfPrev1DayLoss"),
        ("ADSL-LINE-MIB", "adslAtucPerfPrev1DayESs"),
        ("ADSL-LINE-MIB", "adslAtucPerfPrev1DayInits"),
        ("ADSL-LINE-MIB", "adslAtucIntervalLofs"),
        ("ADSL-LINE-MIB", "adslAtucIntervalLoss"),
        ("ADSL-LINE-MIB", "adslAtucIntervalESs"),
        ("ADSL-LINE-MIB", "adslAtucIntervalInits"),
        ("ADSL-LINE-MIB", "adslAtucIntervalValidData"))
)
if mibBuilder.loadTexts:
    adslAturAtucPhysPerfIntervalGroup.setStatus("current")

adslAturAturPhysPerfRawCounterGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 3, 1, 19)
)
adslAturAturPhysPerfRawCounterGroup.setObjects(
      *(("ADSL-LINE-MIB", "adslAturPerfLofs"),
        ("ADSL-LINE-MIB", "adslAturPerfLoss"),
        ("ADSL-LINE-MIB", "adslAturPerfLprs"),
        ("ADSL-LINE-MIB", "adslAturPerfESs"))
)
if mibBuilder.loadTexts:
    adslAturAturPhysPerfRawCounterGroup.setStatus("current")

adslAturAturPhysPerfIntervalGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 3, 1, 20)
)
adslAturAturPhysPerfIntervalGroup.setObjects(
      *(("ADSL-LINE-MIB", "adslAturPerfValidIntervals"),
        ("ADSL-LINE-MIB", "adslAturPerfInvalidIntervals"),
        ("ADSL-LINE-MIB", "adslAturPerfCurr15MinTimeElapsed"),
        ("ADSL-LINE-MIB", "adslAturPerfCurr15MinLofs"),
        ("ADSL-LINE-MIB", "adslAturPerfCurr15MinLoss"),
        ("ADSL-LINE-MIB", "adslAturPerfCurr15MinLprs"),
        ("ADSL-LINE-MIB", "adslAturPerfCurr15MinESs"),
        ("ADSL-LINE-MIB", "adslAturPerfCurr1DayTimeElapsed"),
        ("ADSL-LINE-MIB", "adslAturPerfCurr1DayLofs"),
        ("ADSL-LINE-MIB", "adslAturPerfCurr1DayLoss"),
        ("ADSL-LINE-MIB", "adslAturPerfCurr1DayLprs"),
        ("ADSL-LINE-MIB", "adslAturPerfCurr1DayESs"),
        ("ADSL-LINE-MIB", "adslAturPerfPrev1DayMoniSecs"),
        ("ADSL-LINE-MIB", "adslAturPerfPrev1DayLofs"),
        ("ADSL-LINE-MIB", "adslAturPerfPrev1DayLoss"),
        ("ADSL-LINE-MIB", "adslAturPerfPrev1DayLprs"),
        ("ADSL-LINE-MIB", "adslAturPerfPrev1DayESs"),
        ("ADSL-LINE-MIB", "adslAturIntervalLofs"),
        ("ADSL-LINE-MIB", "adslAturIntervalLoss"),
        ("ADSL-LINE-MIB", "adslAturIntervalLprs"),
        ("ADSL-LINE-MIB", "adslAturIntervalESs"),
        ("ADSL-LINE-MIB", "adslAturIntervalValidData"))
)
if mibBuilder.loadTexts:
    adslAturAturPhysPerfIntervalGroup.setStatus("current")

adslAturAtucChanPerformanceGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 3, 1, 21)
)
adslAturAtucChanPerformanceGroup.setObjects(
      *(("ADSL-LINE-MIB", "adslAtucChanReceivedBlks"),
        ("ADSL-LINE-MIB", "adslAtucChanTransmittedBlks"),
        ("ADSL-LINE-MIB", "adslAtucChanCorrectedBlks"),
        ("ADSL-LINE-MIB", "adslAtucChanUncorrectBlks"),
        ("ADSL-LINE-MIB", "adslAtucChanPerfCurr15MinTimeElapsed"),
        ("ADSL-LINE-MIB", "adslAtucChanPerfCurr15MinReceivedBlks"),
        ("ADSL-LINE-MIB", "adslAtucChanPerfCurr15MinTransmittedBlks"),
        ("ADSL-LINE-MIB", "adslAtucChanPerfCurr15MinCorrectedBlks"),
        ("ADSL-LINE-MIB", "adslAtucChanPerfCurr15MinUncorrectBlks"),
        ("ADSL-LINE-MIB", "adslAtucChanPerfCurr1DayTimeElapsed"),
        ("ADSL-LINE-MIB", "adslAtucChanPerfCurr1DayReceivedBlks"),
        ("ADSL-LINE-MIB", "adslAtucChanPerfCurr1DayTransmittedBlks"),
        ("ADSL-LINE-MIB", "adslAtucChanPerfCurr1DayCorrectedBlks"),
        ("ADSL-LINE-MIB", "adslAtucChanPerfCurr1DayUncorrectBlks"),
        ("ADSL-LINE-MIB", "adslAtucChanPerfPrev1DayMoniSecs"),
        ("ADSL-LINE-MIB", "adslAtucChanPerfPrev1DayReceivedBlks"),
        ("ADSL-LINE-MIB", "adslAtucChanPerfPrev1DayTransmittedBlks"),
        ("ADSL-LINE-MIB", "adslAtucChanPerfPrev1DayCorrectedBlks"),
        ("ADSL-LINE-MIB", "adslAtucChanPerfPrev1DayUncorrectBlks"),
        ("ADSL-LINE-MIB", "adslAtucChanPerfValidIntervals"),
        ("ADSL-LINE-MIB", "adslAtucChanPerfInvalidIntervals"),
        ("ADSL-LINE-MIB", "adslAtucChanIntervalReceivedBlks"),
        ("ADSL-LINE-MIB", "adslAtucChanIntervalTransmittedBlks"),
        ("ADSL-LINE-MIB", "adslAtucChanIntervalCorrectedBlks"),
        ("ADSL-LINE-MIB", "adslAtucChanIntervalUncorrectBlks"),
        ("ADSL-LINE-MIB", "adslAtucChanIntervalValidData"))
)
if mibBuilder.loadTexts:
    adslAturAtucChanPerformanceGroup.setStatus("current")

adslAturAturChanPerformanceGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 3, 1, 22)
)
adslAturAturChanPerformanceGroup.setObjects(
      *(("ADSL-LINE-MIB", "adslAturChanReceivedBlks"),
        ("ADSL-LINE-MIB", "adslAturChanTransmittedBlks"),
        ("ADSL-LINE-MIB", "adslAturChanCorrectedBlks"),
        ("ADSL-LINE-MIB", "adslAturChanUncorrectBlks"),
        ("ADSL-LINE-MIB", "adslAturChanPerfValidIntervals"),
        ("ADSL-LINE-MIB", "adslAturChanPerfInvalidIntervals"),
        ("ADSL-LINE-MIB", "adslAturChanPerfCurr15MinTimeElapsed"),
        ("ADSL-LINE-MIB", "adslAturChanPerfCurr15MinReceivedBlks"),
        ("ADSL-LINE-MIB", "adslAturChanPerfCurr15MinTransmittedBlks"),
        ("ADSL-LINE-MIB", "adslAturChanPerfCurr15MinCorrectedBlks"),
        ("ADSL-LINE-MIB", "adslAturChanPerfCurr15MinUncorrectBlks"),
        ("ADSL-LINE-MIB", "adslAturChanPerfCurr1DayTimeElapsed"),
        ("ADSL-LINE-MIB", "adslAturChanPerfCurr1DayReceivedBlks"),
        ("ADSL-LINE-MIB", "adslAturChanPerfCurr1DayTransmittedBlks"),
        ("ADSL-LINE-MIB", "adslAturChanPerfCurr1DayCorrectedBlks"),
        ("ADSL-LINE-MIB", "adslAturChanPerfCurr1DayUncorrectBlks"),
        ("ADSL-LINE-MIB", "adslAturChanPerfPrev1DayMoniSecs"),
        ("ADSL-LINE-MIB", "adslAturChanPerfPrev1DayReceivedBlks"),
        ("ADSL-LINE-MIB", "adslAturChanPerfPrev1DayTransmittedBlks"),
        ("ADSL-LINE-MIB", "adslAturChanPerfPrev1DayCorrectedBlks"),
        ("ADSL-LINE-MIB", "adslAturChanPerfPrev1DayUncorrectBlks"),
        ("ADSL-LINE-MIB", "adslAturChanIntervalReceivedBlks"),
        ("ADSL-LINE-MIB", "adslAturChanIntervalTransmittedBlks"),
        ("ADSL-LINE-MIB", "adslAturChanIntervalCorrectedBlks"),
        ("ADSL-LINE-MIB", "adslAturChanIntervalUncorrectBlks"),
        ("ADSL-LINE-MIB", "adslAturChanIntervalValidData"))
)
if mibBuilder.loadTexts:
    adslAturAturChanPerformanceGroup.setStatus("current")

adslAturLineAlarmConfProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 3, 1, 23)
)
adslAturLineAlarmConfProfileGroup.setObjects(
      *(("ADSL-LINE-MIB", "adslAtucThresh15MinLofs"),
        ("ADSL-LINE-MIB", "adslAtucThresh15MinLoss"),
        ("ADSL-LINE-MIB", "adslAtucThresh15MinESs"),
        ("ADSL-LINE-MIB", "adslAtucThreshFastRateUp"),
        ("ADSL-LINE-MIB", "adslAtucThreshInterleaveRateUp"),
        ("ADSL-LINE-MIB", "adslAtucThreshFastRateDown"),
        ("ADSL-LINE-MIB", "adslAtucThreshInterleaveRateDown"),
        ("ADSL-LINE-MIB", "adslAtucInitFailureTrapEnable"),
        ("ADSL-LINE-MIB", "adslAturThresh15MinLofs"),
        ("ADSL-LINE-MIB", "adslAturThresh15MinLoss"),
        ("ADSL-LINE-MIB", "adslAturThresh15MinLprs"),
        ("ADSL-LINE-MIB", "adslAturThresh15MinESs"),
        ("ADSL-LINE-MIB", "adslAturThreshFastRateUp"),
        ("ADSL-LINE-MIB", "adslAturThreshInterleaveRateUp"),
        ("ADSL-LINE-MIB", "adslAturThreshFastRateDown"),
        ("ADSL-LINE-MIB", "adslAturThreshInterleaveRateDown"))
)
if mibBuilder.loadTexts:
    adslAturLineAlarmConfProfileGroup.setStatus("current")

adslAturLineConfProfileControlGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 3, 1, 24)
)
adslAturLineConfProfileControlGroup.setObjects(
      *(("ADSL-LINE-MIB", "adslLineAlarmConfProfile"),
        ("ADSL-LINE-MIB", "adslLineAlarmConfProfileRowStatus"))
)
if mibBuilder.loadTexts:
    adslAturLineConfProfileControlGroup.setStatus("current")


# Notification objects

adslAtucPerfLofsThreshTrap = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 2, 1, 0, 1)
)
adslAtucPerfLofsThreshTrap.setObjects(
      *(("ADSL-LINE-MIB", "adslAtucPerfCurr15MinLofs"),
        ("ADSL-LINE-MIB", "adslAtucThresh15MinLofs"))
)
if mibBuilder.loadTexts:
    adslAtucPerfLofsThreshTrap.setStatus(
        "current"
    )

adslAtucPerfLossThreshTrap = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 2, 1, 0, 2)
)
adslAtucPerfLossThreshTrap.setObjects(
      *(("ADSL-LINE-MIB", "adslAtucPerfCurr15MinLoss"),
        ("ADSL-LINE-MIB", "adslAtucThresh15MinLoss"))
)
if mibBuilder.loadTexts:
    adslAtucPerfLossThreshTrap.setStatus(
        "current"
    )

adslAtucPerfLprsThreshTrap = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 2, 1, 0, 3)
)
adslAtucPerfLprsThreshTrap.setObjects(
      *(("ADSL-LINE-MIB", "adslAtucPerfCurr15MinLprs"),
        ("ADSL-LINE-MIB", "adslAtucThresh15MinLprs"))
)
if mibBuilder.loadTexts:
    adslAtucPerfLprsThreshTrap.setStatus(
        "current"
    )

adslAtucPerfESsThreshTrap = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 2, 1, 0, 4)
)
adslAtucPerfESsThreshTrap.setObjects(
      *(("ADSL-LINE-MIB", "adslAtucPerfCurr15MinESs"),
        ("ADSL-LINE-MIB", "adslAtucThresh15MinESs"))
)
if mibBuilder.loadTexts:
    adslAtucPerfESsThreshTrap.setStatus(
        "current"
    )

adslAtucRateChangeTrap = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 2, 1, 0, 5)
)
adslAtucRateChangeTrap.setObjects(
      *(("ADSL-LINE-MIB", "adslAtucChanCurrTxRate"),
        ("ADSL-LINE-MIB", "adslAtucChanPrevTxRate"))
)
if mibBuilder.loadTexts:
    adslAtucRateChangeTrap.setStatus(
        "current"
    )

adslAtucPerfLolsThreshTrap = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 2, 1, 0, 6)
)
adslAtucPerfLolsThreshTrap.setObjects(
      *(("ADSL-LINE-MIB", "adslAtucPerfCurr15MinLols"),
        ("ADSL-LINE-MIB", "adslAtucThresh15MinLols"))
)
if mibBuilder.loadTexts:
    adslAtucPerfLolsThreshTrap.setStatus(
        "current"
    )

adslAtucInitFailureTrap = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 2, 1, 0, 7)
)
adslAtucInitFailureTrap.setObjects(
    ("ADSL-LINE-MIB", "adslAtucCurrStatus")
)
if mibBuilder.loadTexts:
    adslAtucInitFailureTrap.setStatus(
        "current"
    )

adslAturPerfLofsThreshTrap = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 2, 2, 0, 1)
)
adslAturPerfLofsThreshTrap.setObjects(
      *(("ADSL-LINE-MIB", "adslAturPerfCurr15MinLofs"),
        ("ADSL-LINE-MIB", "adslAturThresh15MinLofs"))
)
if mibBuilder.loadTexts:
    adslAturPerfLofsThreshTrap.setStatus(
        "current"
    )

adslAturPerfLossThreshTrap = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 2, 2, 0, 2)
)
adslAturPerfLossThreshTrap.setObjects(
      *(("ADSL-LINE-MIB", "adslAturPerfCurr15MinLoss"),
        ("ADSL-LINE-MIB", "adslAturThresh15MinLoss"))
)
if mibBuilder.loadTexts:
    adslAturPerfLossThreshTrap.setStatus(
        "current"
    )

adslAturPerfLprsThreshTrap = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 2, 2, 0, 3)
)
adslAturPerfLprsThreshTrap.setObjects(
      *(("ADSL-LINE-MIB", "adslAturPerfCurr15MinLprs"),
        ("ADSL-LINE-MIB", "adslAturThresh15MinLprs"))
)
if mibBuilder.loadTexts:
    adslAturPerfLprsThreshTrap.setStatus(
        "current"
    )

adslAturPerfESsThreshTrap = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 2, 2, 0, 4)
)
adslAturPerfESsThreshTrap.setObjects(
      *(("ADSL-LINE-MIB", "adslAturPerfCurr15MinESs"),
        ("ADSL-LINE-MIB", "adslAturThresh15MinESs"))
)
if mibBuilder.loadTexts:
    adslAturPerfESsThreshTrap.setStatus(
        "current"
    )

adslAturRateChangeTrap = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 2, 2, 0, 5)
)
adslAturRateChangeTrap.setObjects(
      *(("ADSL-LINE-MIB", "adslAturChanCurrTxRate"),
        ("ADSL-LINE-MIB", "adslAturChanPrevTxRate"))
)
if mibBuilder.loadTexts:
    adslAturRateChangeTrap.setStatus(
        "current"
    )


# Notifications groups

adslNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 3, 1, 13)
)
adslNotificationsGroup.setObjects(
      *(("ADSL-LINE-MIB", "adslAtucPerfLofsThreshTrap"),
        ("ADSL-LINE-MIB", "adslAtucPerfLossThreshTrap"),
        ("ADSL-LINE-MIB", "adslAtucPerfLprsThreshTrap"),
        ("ADSL-LINE-MIB", "adslAtucPerfESsThreshTrap"),
        ("ADSL-LINE-MIB", "adslAtucRateChangeTrap"),
        ("ADSL-LINE-MIB", "adslAtucPerfLolsThreshTrap"),
        ("ADSL-LINE-MIB", "adslAtucInitFailureTrap"),
        ("ADSL-LINE-MIB", "adslAturPerfLofsThreshTrap"),
        ("ADSL-LINE-MIB", "adslAturPerfLossThreshTrap"),
        ("ADSL-LINE-MIB", "adslAturPerfLprsThreshTrap"),
        ("ADSL-LINE-MIB", "adslAturPerfESsThreshTrap"),
        ("ADSL-LINE-MIB", "adslAturRateChangeTrap"))
)
if mibBuilder.loadTexts:
    adslNotificationsGroup.setStatus(
        "current"
    )

adslAturNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 3, 1, 25)
)
adslAturNotificationsGroup.setObjects(
      *(("ADSL-LINE-MIB", "adslAtucPerfLofsThreshTrap"),
        ("ADSL-LINE-MIB", "adslAtucPerfLossThreshTrap"),
        ("ADSL-LINE-MIB", "adslAtucPerfESsThreshTrap"),
        ("ADSL-LINE-MIB", "adslAtucRateChangeTrap"),
        ("ADSL-LINE-MIB", "adslAturPerfLofsThreshTrap"),
        ("ADSL-LINE-MIB", "adslAturPerfLossThreshTrap"),
        ("ADSL-LINE-MIB", "adslAturPerfLprsThreshTrap"),
        ("ADSL-LINE-MIB", "adslAturPerfESsThreshTrap"),
        ("ADSL-LINE-MIB", "adslAturRateChangeTrap"))
)
if mibBuilder.loadTexts:
    adslAturNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

adslLineMibAtucCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 3, 2, 1)
)
if mibBuilder.loadTexts:
    adslLineMibAtucCompliance.setStatus(
        "current"
    )

adslLineMibAturCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 10, 94, 1, 3, 2, 2)
)
if mibBuilder.loadTexts:
    adslLineMibAturCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADSL-LINE-MIB",
    **{"adslMIB": adslMIB,
       "adslLineMib": adslLineMib,
       "adslMibObjects": adslMibObjects,
       "adslLineTable": adslLineTable,
       "adslLineEntry": adslLineEntry,
       "adslLineCoding": adslLineCoding,
       "adslLineType": adslLineType,
       "adslLineSpecific": adslLineSpecific,
       "adslLineConfProfile": adslLineConfProfile,
       "adslLineAlarmConfProfile": adslLineAlarmConfProfile,
       "adslAtucPhysTable": adslAtucPhysTable,
       "adslAtucPhysEntry": adslAtucPhysEntry,
       "adslAtucInvSerialNumber": adslAtucInvSerialNumber,
       "adslAtucInvVendorID": adslAtucInvVendorID,
       "adslAtucInvVersionNumber": adslAtucInvVersionNumber,
       "adslAtucCurrSnrMgn": adslAtucCurrSnrMgn,
       "adslAtucCurrAtn": adslAtucCurrAtn,
       "adslAtucCurrStatus": adslAtucCurrStatus,
       "adslAtucCurrOutputPwr": adslAtucCurrOutputPwr,
       "adslAtucCurrAttainableRate": adslAtucCurrAttainableRate,
       "adslAturPhysTable": adslAturPhysTable,
       "adslAturPhysEntry": adslAturPhysEntry,
       "adslAturInvSerialNumber": adslAturInvSerialNumber,
       "adslAturInvVendorID": adslAturInvVendorID,
       "adslAturInvVersionNumber": adslAturInvVersionNumber,
       "adslAturCurrSnrMgn": adslAturCurrSnrMgn,
       "adslAturCurrAtn": adslAturCurrAtn,
       "adslAturCurrStatus": adslAturCurrStatus,
       "adslAturCurrOutputPwr": adslAturCurrOutputPwr,
       "adslAturCurrAttainableRate": adslAturCurrAttainableRate,
       "adslAtucChanTable": adslAtucChanTable,
       "adslAtucChanEntry": adslAtucChanEntry,
       "adslAtucChanInterleaveDelay": adslAtucChanInterleaveDelay,
       "adslAtucChanCurrTxRate": adslAtucChanCurrTxRate,
       "adslAtucChanPrevTxRate": adslAtucChanPrevTxRate,
       "adslAtucChanCrcBlockLength": adslAtucChanCrcBlockLength,
       "adslAturChanTable": adslAturChanTable,
       "adslAturChanEntry": adslAturChanEntry,
       "adslAturChanInterleaveDelay": adslAturChanInterleaveDelay,
       "adslAturChanCurrTxRate": adslAturChanCurrTxRate,
       "adslAturChanPrevTxRate": adslAturChanPrevTxRate,
       "adslAturChanCrcBlockLength": adslAturChanCrcBlockLength,
       "adslAtucPerfDataTable": adslAtucPerfDataTable,
       "adslAtucPerfDataEntry": adslAtucPerfDataEntry,
       "adslAtucPerfLofs": adslAtucPerfLofs,
       "adslAtucPerfLoss": adslAtucPerfLoss,
       "adslAtucPerfLols": adslAtucPerfLols,
       "adslAtucPerfLprs": adslAtucPerfLprs,
       "adslAtucPerfESs": adslAtucPerfESs,
       "adslAtucPerfInits": adslAtucPerfInits,
       "adslAtucPerfValidIntervals": adslAtucPerfValidIntervals,
       "adslAtucPerfInvalidIntervals": adslAtucPerfInvalidIntervals,
       "adslAtucPerfCurr15MinTimeElapsed": adslAtucPerfCurr15MinTimeElapsed,
       "adslAtucPerfCurr15MinLofs": adslAtucPerfCurr15MinLofs,
       "adslAtucPerfCurr15MinLoss": adslAtucPerfCurr15MinLoss,
       "adslAtucPerfCurr15MinLols": adslAtucPerfCurr15MinLols,
       "adslAtucPerfCurr15MinLprs": adslAtucPerfCurr15MinLprs,
       "adslAtucPerfCurr15MinESs": adslAtucPerfCurr15MinESs,
       "adslAtucPerfCurr15MinInits": adslAtucPerfCurr15MinInits,
       "adslAtucPerfCurr1DayTimeElapsed": adslAtucPerfCurr1DayTimeElapsed,
       "adslAtucPerfCurr1DayLofs": adslAtucPerfCurr1DayLofs,
       "adslAtucPerfCurr1DayLoss": adslAtucPerfCurr1DayLoss,
       "adslAtucPerfCurr1DayLols": adslAtucPerfCurr1DayLols,
       "adslAtucPerfCurr1DayLprs": adslAtucPerfCurr1DayLprs,
       "adslAtucPerfCurr1DayESs": adslAtucPerfCurr1DayESs,
       "adslAtucPerfCurr1DayInits": adslAtucPerfCurr1DayInits,
       "adslAtucPerfPrev1DayMoniSecs": adslAtucPerfPrev1DayMoniSecs,
       "adslAtucPerfPrev1DayLofs": adslAtucPerfPrev1DayLofs,
       "adslAtucPerfPrev1DayLoss": adslAtucPerfPrev1DayLoss,
       "adslAtucPerfPrev1DayLols": adslAtucPerfPrev1DayLols,
       "adslAtucPerfPrev1DayLprs": adslAtucPerfPrev1DayLprs,
       "adslAtucPerfPrev1DayESs": adslAtucPerfPrev1DayESs,
       "adslAtucPerfPrev1DayInits": adslAtucPerfPrev1DayInits,
       "adslAturPerfDataTable": adslAturPerfDataTable,
       "adslAturPerfDataEntry": adslAturPerfDataEntry,
       "adslAturPerfLofs": adslAturPerfLofs,
       "adslAturPerfLoss": adslAturPerfLoss,
       "adslAturPerfLprs": adslAturPerfLprs,
       "adslAturPerfESs": adslAturPerfESs,
       "adslAturPerfValidIntervals": adslAturPerfValidIntervals,
       "adslAturPerfInvalidIntervals": adslAturPerfInvalidIntervals,
       "adslAturPerfCurr15MinTimeElapsed": adslAturPerfCurr15MinTimeElapsed,
       "adslAturPerfCurr15MinLofs": adslAturPerfCurr15MinLofs,
       "adslAturPerfCurr15MinLoss": adslAturPerfCurr15MinLoss,
       "adslAturPerfCurr15MinLprs": adslAturPerfCurr15MinLprs,
       "adslAturPerfCurr15MinESs": adslAturPerfCurr15MinESs,
       "adslAturPerfCurr1DayTimeElapsed": adslAturPerfCurr1DayTimeElapsed,
       "adslAturPerfCurr1DayLofs": adslAturPerfCurr1DayLofs,
       "adslAturPerfCurr1DayLoss": adslAturPerfCurr1DayLoss,
       "adslAturPerfCurr1DayLprs": adslAturPerfCurr1DayLprs,
       "adslAturPerfCurr1DayESs": adslAturPerfCurr1DayESs,
       "adslAturPerfPrev1DayMoniSecs": adslAturPerfPrev1DayMoniSecs,
       "adslAturPerfPrev1DayLofs": adslAturPerfPrev1DayLofs,
       "adslAturPerfPrev1DayLoss": adslAturPerfPrev1DayLoss,
       "adslAturPerfPrev1DayLprs": adslAturPerfPrev1DayLprs,
       "adslAturPerfPrev1DayESs": adslAturPerfPrev1DayESs,
       "adslAtucIntervalTable": adslAtucIntervalTable,
       "adslAtucIntervalEntry": adslAtucIntervalEntry,
       "adslAtucIntervalNumber": adslAtucIntervalNumber,
       "adslAtucIntervalLofs": adslAtucIntervalLofs,
       "adslAtucIntervalLoss": adslAtucIntervalLoss,
       "adslAtucIntervalLols": adslAtucIntervalLols,
       "adslAtucIntervalLprs": adslAtucIntervalLprs,
       "adslAtucIntervalESs": adslAtucIntervalESs,
       "adslAtucIntervalInits": adslAtucIntervalInits,
       "adslAtucIntervalValidData": adslAtucIntervalValidData,
       "adslAturIntervalTable": adslAturIntervalTable,
       "adslAturIntervalEntry": adslAturIntervalEntry,
       "adslAturIntervalNumber": adslAturIntervalNumber,
       "adslAturIntervalLofs": adslAturIntervalLofs,
       "adslAturIntervalLoss": adslAturIntervalLoss,
       "adslAturIntervalLprs": adslAturIntervalLprs,
       "adslAturIntervalESs": adslAturIntervalESs,
       "adslAturIntervalValidData": adslAturIntervalValidData,
       "adslAtucChanPerfDataTable": adslAtucChanPerfDataTable,
       "adslAtucChanPerfDataEntry": adslAtucChanPerfDataEntry,
       "adslAtucChanReceivedBlks": adslAtucChanReceivedBlks,
       "adslAtucChanTransmittedBlks": adslAtucChanTransmittedBlks,
       "adslAtucChanCorrectedBlks": adslAtucChanCorrectedBlks,
       "adslAtucChanUncorrectBlks": adslAtucChanUncorrectBlks,
       "adslAtucChanPerfValidIntervals": adslAtucChanPerfValidIntervals,
       "adslAtucChanPerfInvalidIntervals": adslAtucChanPerfInvalidIntervals,
       "adslAtucChanPerfCurr15MinTimeElapsed": adslAtucChanPerfCurr15MinTimeElapsed,
       "adslAtucChanPerfCurr15MinReceivedBlks": adslAtucChanPerfCurr15MinReceivedBlks,
       "adslAtucChanPerfCurr15MinTransmittedBlks": adslAtucChanPerfCurr15MinTransmittedBlks,
       "adslAtucChanPerfCurr15MinCorrectedBlks": adslAtucChanPerfCurr15MinCorrectedBlks,
       "adslAtucChanPerfCurr15MinUncorrectBlks": adslAtucChanPerfCurr15MinUncorrectBlks,
       "adslAtucChanPerfCurr1DayTimeElapsed": adslAtucChanPerfCurr1DayTimeElapsed,
       "adslAtucChanPerfCurr1DayReceivedBlks": adslAtucChanPerfCurr1DayReceivedBlks,
       "adslAtucChanPerfCurr1DayTransmittedBlks": adslAtucChanPerfCurr1DayTransmittedBlks,
       "adslAtucChanPerfCurr1DayCorrectedBlks": adslAtucChanPerfCurr1DayCorrectedBlks,
       "adslAtucChanPerfCurr1DayUncorrectBlks": adslAtucChanPerfCurr1DayUncorrectBlks,
       "adslAtucChanPerfPrev1DayMoniSecs": adslAtucChanPerfPrev1DayMoniSecs,
       "adslAtucChanPerfPrev1DayReceivedBlks": adslAtucChanPerfPrev1DayReceivedBlks,
       "adslAtucChanPerfPrev1DayTransmittedBlks": adslAtucChanPerfPrev1DayTransmittedBlks,
       "adslAtucChanPerfPrev1DayCorrectedBlks": adslAtucChanPerfPrev1DayCorrectedBlks,
       "adslAtucChanPerfPrev1DayUncorrectBlks": adslAtucChanPerfPrev1DayUncorrectBlks,
       "adslAturChanPerfDataTable": adslAturChanPerfDataTable,
       "adslAturChanPerfDataEntry": adslAturChanPerfDataEntry,
       "adslAturChanReceivedBlks": adslAturChanReceivedBlks,
       "adslAturChanTransmittedBlks": adslAturChanTransmittedBlks,
       "adslAturChanCorrectedBlks": adslAturChanCorrectedBlks,
       "adslAturChanUncorrectBlks": adslAturChanUncorrectBlks,
       "adslAturChanPerfValidIntervals": adslAturChanPerfValidIntervals,
       "adslAturChanPerfInvalidIntervals": adslAturChanPerfInvalidIntervals,
       "adslAturChanPerfCurr15MinTimeElapsed": adslAturChanPerfCurr15MinTimeElapsed,
       "adslAturChanPerfCurr15MinReceivedBlks": adslAturChanPerfCurr15MinReceivedBlks,
       "adslAturChanPerfCurr15MinTransmittedBlks": adslAturChanPerfCurr15MinTransmittedBlks,
       "adslAturChanPerfCurr15MinCorrectedBlks": adslAturChanPerfCurr15MinCorrectedBlks,
       "adslAturChanPerfCurr15MinUncorrectBlks": adslAturChanPerfCurr15MinUncorrectBlks,
       "adslAturChanPerfCurr1DayTimeElapsed": adslAturChanPerfCurr1DayTimeElapsed,
       "adslAturChanPerfCurr1DayReceivedBlks": adslAturChanPerfCurr1DayReceivedBlks,
       "adslAturChanPerfCurr1DayTransmittedBlks": adslAturChanPerfCurr1DayTransmittedBlks,
       "adslAturChanPerfCurr1DayCorrectedBlks": adslAturChanPerfCurr1DayCorrectedBlks,
       "adslAturChanPerfCurr1DayUncorrectBlks": adslAturChanPerfCurr1DayUncorrectBlks,
       "adslAturChanPerfPrev1DayMoniSecs": adslAturChanPerfPrev1DayMoniSecs,
       "adslAturChanPerfPrev1DayReceivedBlks": adslAturChanPerfPrev1DayReceivedBlks,
       "adslAturChanPerfPrev1DayTransmittedBlks": adslAturChanPerfPrev1DayTransmittedBlks,
       "adslAturChanPerfPrev1DayCorrectedBlks": adslAturChanPerfPrev1DayCorrectedBlks,
       "adslAturChanPerfPrev1DayUncorrectBlks": adslAturChanPerfPrev1DayUncorrectBlks,
       "adslAtucChanIntervalTable": adslAtucChanIntervalTable,
       "adslAtucChanIntervalEntry": adslAtucChanIntervalEntry,
       "adslAtucChanIntervalNumber": adslAtucChanIntervalNumber,
       "adslAtucChanIntervalReceivedBlks": adslAtucChanIntervalReceivedBlks,
       "adslAtucChanIntervalTransmittedBlks": adslAtucChanIntervalTransmittedBlks,
       "adslAtucChanIntervalCorrectedBlks": adslAtucChanIntervalCorrectedBlks,
       "adslAtucChanIntervalUncorrectBlks": adslAtucChanIntervalUncorrectBlks,
       "adslAtucChanIntervalValidData": adslAtucChanIntervalValidData,
       "adslAturChanIntervalTable": adslAturChanIntervalTable,
       "adslAturChanIntervalEntry": adslAturChanIntervalEntry,
       "adslAturChanIntervalNumber": adslAturChanIntervalNumber,
       "adslAturChanIntervalReceivedBlks": adslAturChanIntervalReceivedBlks,
       "adslAturChanIntervalTransmittedBlks": adslAturChanIntervalTransmittedBlks,
       "adslAturChanIntervalCorrectedBlks": adslAturChanIntervalCorrectedBlks,
       "adslAturChanIntervalUncorrectBlks": adslAturChanIntervalUncorrectBlks,
       "adslAturChanIntervalValidData": adslAturChanIntervalValidData,
       "adslLineConfProfileTable": adslLineConfProfileTable,
       "adslLineConfProfileEntry": adslLineConfProfileEntry,
       "adslLineConfProfileName": adslLineConfProfileName,
       "adslAtucConfRateMode": adslAtucConfRateMode,
       "adslAtucConfRateChanRatio": adslAtucConfRateChanRatio,
       "adslAtucConfTargetSnrMgn": adslAtucConfTargetSnrMgn,
       "adslAtucConfMaxSnrMgn": adslAtucConfMaxSnrMgn,
       "adslAtucConfMinSnrMgn": adslAtucConfMinSnrMgn,
       "adslAtucConfDownshiftSnrMgn": adslAtucConfDownshiftSnrMgn,
       "adslAtucConfUpshiftSnrMgn": adslAtucConfUpshiftSnrMgn,
       "adslAtucConfMinUpshiftTime": adslAtucConfMinUpshiftTime,
       "adslAtucConfMinDownshiftTime": adslAtucConfMinDownshiftTime,
       "adslAtucChanConfFastMinTxRate": adslAtucChanConfFastMinTxRate,
       "adslAtucChanConfInterleaveMinTxRate": adslAtucChanConfInterleaveMinTxRate,
       "adslAtucChanConfFastMaxTxRate": adslAtucChanConfFastMaxTxRate,
       "adslAtucChanConfInterleaveMaxTxRate": adslAtucChanConfInterleaveMaxTxRate,
       "adslAtucChanConfMaxInterleaveDelay": adslAtucChanConfMaxInterleaveDelay,
       "adslAturConfRateMode": adslAturConfRateMode,
       "adslAturConfRateChanRatio": adslAturConfRateChanRatio,
       "adslAturConfTargetSnrMgn": adslAturConfTargetSnrMgn,
       "adslAturConfMaxSnrMgn": adslAturConfMaxSnrMgn,
       "adslAturConfMinSnrMgn": adslAturConfMinSnrMgn,
       "adslAturConfDownshiftSnrMgn": adslAturConfDownshiftSnrMgn,
       "adslAturConfUpshiftSnrMgn": adslAturConfUpshiftSnrMgn,
       "adslAturConfMinUpshiftTime": adslAturConfMinUpshiftTime,
       "adslAturConfMinDownshiftTime": adslAturConfMinDownshiftTime,
       "adslAturChanConfFastMinTxRate": adslAturChanConfFastMinTxRate,
       "adslAturChanConfInterleaveMinTxRate": adslAturChanConfInterleaveMinTxRate,
       "adslAturChanConfFastMaxTxRate": adslAturChanConfFastMaxTxRate,
       "adslAturChanConfInterleaveMaxTxRate": adslAturChanConfInterleaveMaxTxRate,
       "adslAturChanConfMaxInterleaveDelay": adslAturChanConfMaxInterleaveDelay,
       "adslLineConfProfileRowStatus": adslLineConfProfileRowStatus,
       "adslLineAlarmConfProfileTable": adslLineAlarmConfProfileTable,
       "adslLineAlarmConfProfileEntry": adslLineAlarmConfProfileEntry,
       "adslLineAlarmConfProfileName": adslLineAlarmConfProfileName,
       "adslAtucThresh15MinLofs": adslAtucThresh15MinLofs,
       "adslAtucThresh15MinLoss": adslAtucThresh15MinLoss,
       "adslAtucThresh15MinLols": adslAtucThresh15MinLols,
       "adslAtucThresh15MinLprs": adslAtucThresh15MinLprs,
       "adslAtucThresh15MinESs": adslAtucThresh15MinESs,
       "adslAtucThreshFastRateUp": adslAtucThreshFastRateUp,
       "adslAtucThreshInterleaveRateUp": adslAtucThreshInterleaveRateUp,
       "adslAtucThreshFastRateDown": adslAtucThreshFastRateDown,
       "adslAtucThreshInterleaveRateDown": adslAtucThreshInterleaveRateDown,
       "adslAtucInitFailureTrapEnable": adslAtucInitFailureTrapEnable,
       "adslAturThresh15MinLofs": adslAturThresh15MinLofs,
       "adslAturThresh15MinLoss": adslAturThresh15MinLoss,
       "adslAturThresh15MinLprs": adslAturThresh15MinLprs,
       "adslAturThresh15MinESs": adslAturThresh15MinESs,
       "adslAturThreshFastRateUp": adslAturThreshFastRateUp,
       "adslAturThreshInterleaveRateUp": adslAturThreshInterleaveRateUp,
       "adslAturThreshFastRateDown": adslAturThreshFastRateDown,
       "adslAturThreshInterleaveRateDown": adslAturThreshInterleaveRateDown,
       "adslLineAlarmConfProfileRowStatus": adslLineAlarmConfProfileRowStatus,
       "adslLCSMib": adslLCSMib,
       "adslTraps": adslTraps,
       "adslAtucTraps": adslAtucTraps,
       "adslAtucPerfLofsThreshTrap": adslAtucPerfLofsThreshTrap,
       "adslAtucPerfLossThreshTrap": adslAtucPerfLossThreshTrap,
       "adslAtucPerfLprsThreshTrap": adslAtucPerfLprsThreshTrap,
       "adslAtucPerfESsThreshTrap": adslAtucPerfESsThreshTrap,
       "adslAtucRateChangeTrap": adslAtucRateChangeTrap,
       "adslAtucPerfLolsThreshTrap": adslAtucPerfLolsThreshTrap,
       "adslAtucInitFailureTrap": adslAtucInitFailureTrap,
       "adslAturTraps": adslAturTraps,
       "adslAturPerfLofsThreshTrap": adslAturPerfLofsThreshTrap,
       "adslAturPerfLossThreshTrap": adslAturPerfLossThreshTrap,
       "adslAturPerfLprsThreshTrap": adslAturPerfLprsThreshTrap,
       "adslAturPerfESsThreshTrap": adslAturPerfESsThreshTrap,
       "adslAturRateChangeTrap": adslAturRateChangeTrap,
       "adslConformance": adslConformance,
       "adslGroups": adslGroups,
       "adslLineGroup": adslLineGroup,
       "adslPhysicalGroup": adslPhysicalGroup,
       "adslChannelGroup": adslChannelGroup,
       "adslAtucPhysPerfRawCounterGroup": adslAtucPhysPerfRawCounterGroup,
       "adslAtucPhysPerfIntervalGroup": adslAtucPhysPerfIntervalGroup,
       "adslAturPhysPerfRawCounterGroup": adslAturPhysPerfRawCounterGroup,
       "adslAturPhysPerfIntervalGroup": adslAturPhysPerfIntervalGroup,
       "adslAtucChanPerformanceGroup": adslAtucChanPerformanceGroup,
       "adslAturChanPerformanceGroup": adslAturChanPerformanceGroup,
       "adslLineConfProfileGroup": adslLineConfProfileGroup,
       "adslLineAlarmConfProfileGroup": adslLineAlarmConfProfileGroup,
       "adslLineConfProfileControlGroup": adslLineConfProfileControlGroup,
       "adslNotificationsGroup": adslNotificationsGroup,
       "adslAturLineGroup": adslAturLineGroup,
       "adslAturPhysicalGroup": adslAturPhysicalGroup,
       "adslAturChannelGroup": adslAturChannelGroup,
       "adslAturAtucPhysPerfRawCounterGroup": adslAturAtucPhysPerfRawCounterGroup,
       "adslAturAtucPhysPerfIntervalGroup": adslAturAtucPhysPerfIntervalGroup,
       "adslAturAturPhysPerfRawCounterGroup": adslAturAturPhysPerfRawCounterGroup,
       "adslAturAturPhysPerfIntervalGroup": adslAturAturPhysPerfIntervalGroup,
       "adslAturAtucChanPerformanceGroup": adslAturAtucChanPerformanceGroup,
       "adslAturAturChanPerformanceGroup": adslAturAturChanPerformanceGroup,
       "adslAturLineAlarmConfProfileGroup": adslAturLineAlarmConfProfileGroup,
       "adslAturLineConfProfileControlGroup": adslAturLineConfProfileControlGroup,
       "adslAturNotificationsGroup": adslAturNotificationsGroup,
       "adslCompliances": adslCompliances,
       "adslLineMibAtucCompliance": adslLineMibAtucCompliance,
       "adslLineMibAturCompliance": adslLineMibAturCompliance}
)
