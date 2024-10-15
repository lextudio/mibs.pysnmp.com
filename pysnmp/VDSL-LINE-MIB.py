# SNMP MIB module (VDSL-LINE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/VDSL-LINE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:11:52 2024
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

(HCPerfCurrentCount,
 HCPerfIntervalCount,
 HCPerfIntervalThreshold,
 HCPerfInvalidIntervals,
 HCPerfTimeElapsed,
 HCPerfValidIntervals) = mibBuilder.importSymbols(
    "HC-PerfHist-TC-MIB",
    "HCPerfCurrentCount",
    "HCPerfIntervalCount",
    "HCPerfIntervalThreshold",
    "HCPerfInvalidIntervals",
    "HCPerfTimeElapsed",
    "HCPerfValidIntervals")

(ZeroBasedCounter64,) = mibBuilder.importSymbols(
    "HCNUM-TC",
    "ZeroBasedCounter64")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

vdslMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 10, 97)
)
vdslMIB.setRevisions(
        ("2004-02-19 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class VdslLineCodingType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mcm", 2),
          ("other", 1),
          ("scm", 3))
    )



class VdslLineEntity(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("vtuc", 1),
          ("vtur", 2))
    )



# MIB Managed Objects in the order of their OIDs

_VdslLineMib_ObjectIdentity = ObjectIdentity
vdslLineMib = _VdslLineMib_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 97, 1)
)
_VdslNotifications_ObjectIdentity = ObjectIdentity
vdslNotifications = _VdslNotifications_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 0)
)
_VdslMibObjects_ObjectIdentity = ObjectIdentity
vdslMibObjects = _VdslMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1)
)
_VdslLineTable_Object = MibTable
vdslLineTable = _VdslLineTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 1)
)
if mibBuilder.loadTexts:
    vdslLineTable.setStatus("current")
_VdslLineEntry_Object = MibTableRow
vdslLineEntry = _VdslLineEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 1, 1)
)
vdslLineEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    vdslLineEntry.setStatus("current")
_VdslLineCoding_Type = VdslLineCodingType
_VdslLineCoding_Object = MibTableColumn
vdslLineCoding = _VdslLineCoding_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 1, 1, 1),
    _VdslLineCoding_Type()
)
vdslLineCoding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslLineCoding.setStatus("current")


class _VdslLineType_Type(Integer32):
    """Custom type vdslLineType based on Integer32"""
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


_VdslLineType_Type.__name__ = "Integer32"
_VdslLineType_Object = MibTableColumn
vdslLineType = _VdslLineType_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 1, 1, 2),
    _VdslLineType_Type()
)
vdslLineType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslLineType.setStatus("current")


class _VdslLineConfProfile_Type(SnmpAdminString):
    """Custom type vdslLineConfProfile based on SnmpAdminString"""
    defaultValue = OctetString("DEFVAL")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_VdslLineConfProfile_Type.__name__ = "SnmpAdminString"
_VdslLineConfProfile_Object = MibTableColumn
vdslLineConfProfile = _VdslLineConfProfile_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 1, 1, 3),
    _VdslLineConfProfile_Type()
)
vdslLineConfProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vdslLineConfProfile.setStatus("current")


class _VdslLineAlarmConfProfile_Type(SnmpAdminString):
    """Custom type vdslLineAlarmConfProfile based on SnmpAdminString"""
    defaultValue = OctetString("DEFVAL")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_VdslLineAlarmConfProfile_Type.__name__ = "SnmpAdminString"
_VdslLineAlarmConfProfile_Object = MibTableColumn
vdslLineAlarmConfProfile = _VdslLineAlarmConfProfile_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 1, 1, 4),
    _VdslLineAlarmConfProfile_Type()
)
vdslLineAlarmConfProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vdslLineAlarmConfProfile.setStatus("current")
_VdslPhysTable_Object = MibTable
vdslPhysTable = _VdslPhysTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 2)
)
if mibBuilder.loadTexts:
    vdslPhysTable.setStatus("current")
_VdslPhysEntry_Object = MibTableRow
vdslPhysEntry = _VdslPhysEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 2, 1)
)
vdslPhysEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "VDSL-LINE-MIB", "vdslPhysSide"),
)
if mibBuilder.loadTexts:
    vdslPhysEntry.setStatus("current")
_VdslPhysSide_Type = VdslLineEntity
_VdslPhysSide_Object = MibTableColumn
vdslPhysSide = _VdslPhysSide_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 2, 1, 1),
    _VdslPhysSide_Type()
)
vdslPhysSide.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vdslPhysSide.setStatus("current")


class _VdslPhysInvSerialNumber_Type(SnmpAdminString):
    """Custom type vdslPhysInvSerialNumber based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_VdslPhysInvSerialNumber_Type.__name__ = "SnmpAdminString"
_VdslPhysInvSerialNumber_Object = MibTableColumn
vdslPhysInvSerialNumber = _VdslPhysInvSerialNumber_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 2, 1, 2),
    _VdslPhysInvSerialNumber_Type()
)
vdslPhysInvSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslPhysInvSerialNumber.setStatus("current")


class _VdslPhysInvVendorID_Type(SnmpAdminString):
    """Custom type vdslPhysInvVendorID based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_VdslPhysInvVendorID_Type.__name__ = "SnmpAdminString"
_VdslPhysInvVendorID_Object = MibTableColumn
vdslPhysInvVendorID = _VdslPhysInvVendorID_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 2, 1, 3),
    _VdslPhysInvVendorID_Type()
)
vdslPhysInvVendorID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslPhysInvVendorID.setStatus("current")


class _VdslPhysInvVersionNumber_Type(SnmpAdminString):
    """Custom type vdslPhysInvVersionNumber based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_VdslPhysInvVersionNumber_Type.__name__ = "SnmpAdminString"
_VdslPhysInvVersionNumber_Object = MibTableColumn
vdslPhysInvVersionNumber = _VdslPhysInvVersionNumber_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 2, 1, 4),
    _VdslPhysInvVersionNumber_Type()
)
vdslPhysInvVersionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslPhysInvVersionNumber.setStatus("current")


class _VdslPhysCurrSnrMgn_Type(Integer32):
    """Custom type vdslPhysCurrSnrMgn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-127, 127),
    )


_VdslPhysCurrSnrMgn_Type.__name__ = "Integer32"
_VdslPhysCurrSnrMgn_Object = MibTableColumn
vdslPhysCurrSnrMgn = _VdslPhysCurrSnrMgn_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 2, 1, 5),
    _VdslPhysCurrSnrMgn_Type()
)
vdslPhysCurrSnrMgn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslPhysCurrSnrMgn.setStatus("current")
if mibBuilder.loadTexts:
    vdslPhysCurrSnrMgn.setUnits("0.25dBm")


class _VdslPhysCurrAtn_Type(Gauge32):
    """Custom type vdslPhysCurrAtn based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VdslPhysCurrAtn_Type.__name__ = "Gauge32"
_VdslPhysCurrAtn_Object = MibTableColumn
vdslPhysCurrAtn = _VdslPhysCurrAtn_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 2, 1, 6),
    _VdslPhysCurrAtn_Type()
)
vdslPhysCurrAtn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslPhysCurrAtn.setStatus("current")
if mibBuilder.loadTexts:
    vdslPhysCurrAtn.setUnits("0.25dBm")


class _VdslPhysCurrStatus_Type(Bits):
    """Custom type vdslPhysCurrStatus based on Bits"""
    namedValues = NamedValues(
        *(("configInitFailure", 7),
          ("dataInitFailure", 6),
          ("lossOfFraming", 1),
          ("lossOfLink", 5),
          ("lossOfPower", 3),
          ("lossOfSignal", 2),
          ("lossOfSignalQuality", 4),
          ("noDefect", 0),
          ("noPeerVtuPresent", 9),
          ("protocolInitFailure", 8))
    )

_VdslPhysCurrStatus_Type.__name__ = "Bits"
_VdslPhysCurrStatus_Object = MibTableColumn
vdslPhysCurrStatus = _VdslPhysCurrStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 2, 1, 7),
    _VdslPhysCurrStatus_Type()
)
vdslPhysCurrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslPhysCurrStatus.setStatus("current")


class _VdslPhysCurrOutputPwr_Type(Integer32):
    """Custom type vdslPhysCurrOutputPwr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 160),
    )


_VdslPhysCurrOutputPwr_Type.__name__ = "Integer32"
_VdslPhysCurrOutputPwr_Object = MibTableColumn
vdslPhysCurrOutputPwr = _VdslPhysCurrOutputPwr_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 2, 1, 8),
    _VdslPhysCurrOutputPwr_Type()
)
vdslPhysCurrOutputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslPhysCurrOutputPwr.setStatus("current")
if mibBuilder.loadTexts:
    vdslPhysCurrOutputPwr.setUnits("0.1dBm")
_VdslPhysCurrAttainableRate_Type = Gauge32
_VdslPhysCurrAttainableRate_Object = MibTableColumn
vdslPhysCurrAttainableRate = _VdslPhysCurrAttainableRate_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 2, 1, 9),
    _VdslPhysCurrAttainableRate_Type()
)
vdslPhysCurrAttainableRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslPhysCurrAttainableRate.setStatus("current")
if mibBuilder.loadTexts:
    vdslPhysCurrAttainableRate.setUnits("kbps")
_VdslPhysCurrLineRate_Type = Gauge32
_VdslPhysCurrLineRate_Object = MibTableColumn
vdslPhysCurrLineRate = _VdslPhysCurrLineRate_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 2, 1, 10),
    _VdslPhysCurrLineRate_Type()
)
vdslPhysCurrLineRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslPhysCurrLineRate.setStatus("current")
if mibBuilder.loadTexts:
    vdslPhysCurrLineRate.setUnits("kbps")
_VdslChanTable_Object = MibTable
vdslChanTable = _VdslChanTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 3)
)
if mibBuilder.loadTexts:
    vdslChanTable.setStatus("current")
_VdslChanEntry_Object = MibTableRow
vdslChanEntry = _VdslChanEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 3, 1)
)
vdslChanEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "VDSL-LINE-MIB", "vdslPhysSide"),
)
if mibBuilder.loadTexts:
    vdslChanEntry.setStatus("current")
_VdslChanInterleaveDelay_Type = Gauge32
_VdslChanInterleaveDelay_Object = MibTableColumn
vdslChanInterleaveDelay = _VdslChanInterleaveDelay_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 3, 1, 1),
    _VdslChanInterleaveDelay_Type()
)
vdslChanInterleaveDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslChanInterleaveDelay.setStatus("current")
if mibBuilder.loadTexts:
    vdslChanInterleaveDelay.setUnits("milliseconds")
_VdslChanCrcBlockLength_Type = Gauge32
_VdslChanCrcBlockLength_Object = MibTableColumn
vdslChanCrcBlockLength = _VdslChanCrcBlockLength_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 3, 1, 2),
    _VdslChanCrcBlockLength_Type()
)
vdslChanCrcBlockLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslChanCrcBlockLength.setStatus("current")
if mibBuilder.loadTexts:
    vdslChanCrcBlockLength.setUnits("bytes")
_VdslChanCurrTxRate_Type = Gauge32
_VdslChanCurrTxRate_Object = MibTableColumn
vdslChanCurrTxRate = _VdslChanCurrTxRate_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 3, 1, 3),
    _VdslChanCurrTxRate_Type()
)
vdslChanCurrTxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslChanCurrTxRate.setStatus("current")
if mibBuilder.loadTexts:
    vdslChanCurrTxRate.setUnits("kbps")


class _VdslChanCurrTxSlowBurstProtect_Type(Gauge32):
    """Custom type vdslChanCurrTxSlowBurstProtect based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1275),
    )


_VdslChanCurrTxSlowBurstProtect_Type.__name__ = "Gauge32"
_VdslChanCurrTxSlowBurstProtect_Object = MibTableColumn
vdslChanCurrTxSlowBurstProtect = _VdslChanCurrTxSlowBurstProtect_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 3, 1, 4),
    _VdslChanCurrTxSlowBurstProtect_Type()
)
vdslChanCurrTxSlowBurstProtect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslChanCurrTxSlowBurstProtect.setStatus("current")
if mibBuilder.loadTexts:
    vdslChanCurrTxSlowBurstProtect.setUnits("microseconds")


class _VdslChanCurrTxFastFec_Type(Gauge32):
    """Custom type vdslChanCurrTxFastFec based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
    )


_VdslChanCurrTxFastFec_Type.__name__ = "Gauge32"
_VdslChanCurrTxFastFec_Object = MibTableColumn
vdslChanCurrTxFastFec = _VdslChanCurrTxFastFec_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 3, 1, 5),
    _VdslChanCurrTxFastFec_Type()
)
vdslChanCurrTxFastFec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslChanCurrTxFastFec.setStatus("current")
if mibBuilder.loadTexts:
    vdslChanCurrTxFastFec.setUnits("%")
_VdslPerfDataTable_Object = MibTable
vdslPerfDataTable = _VdslPerfDataTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 4)
)
if mibBuilder.loadTexts:
    vdslPerfDataTable.setStatus("current")
_VdslPerfDataEntry_Object = MibTableRow
vdslPerfDataEntry = _VdslPerfDataEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 4, 1)
)
vdslPerfDataEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "VDSL-LINE-MIB", "vdslPhysSide"),
)
if mibBuilder.loadTexts:
    vdslPerfDataEntry.setStatus("current")
_VdslPerfDataValidIntervals_Type = HCPerfValidIntervals
_VdslPerfDataValidIntervals_Object = MibTableColumn
vdslPerfDataValidIntervals = _VdslPerfDataValidIntervals_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 4, 1, 1),
    _VdslPerfDataValidIntervals_Type()
)
vdslPerfDataValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslPerfDataValidIntervals.setStatus("current")
if mibBuilder.loadTexts:
    vdslPerfDataValidIntervals.setUnits("intervals")
_VdslPerfDataInvalidIntervals_Type = HCPerfInvalidIntervals
_VdslPerfDataInvalidIntervals_Object = MibTableColumn
vdslPerfDataInvalidIntervals = _VdslPerfDataInvalidIntervals_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 4, 1, 2),
    _VdslPerfDataInvalidIntervals_Type()
)
vdslPerfDataInvalidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslPerfDataInvalidIntervals.setStatus("current")
if mibBuilder.loadTexts:
    vdslPerfDataInvalidIntervals.setUnits("intervals")
_VdslPerfDataLofs_Type = Unsigned32
_VdslPerfDataLofs_Object = MibTableColumn
vdslPerfDataLofs = _VdslPerfDataLofs_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 4, 1, 3),
    _VdslPerfDataLofs_Type()
)
vdslPerfDataLofs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslPerfDataLofs.setStatus("current")
if mibBuilder.loadTexts:
    vdslPerfDataLofs.setUnits("seconds")
_VdslPerfDataLoss_Type = Unsigned32
_VdslPerfDataLoss_Object = MibTableColumn
vdslPerfDataLoss = _VdslPerfDataLoss_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 4, 1, 4),
    _VdslPerfDataLoss_Type()
)
vdslPerfDataLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslPerfDataLoss.setStatus("current")
if mibBuilder.loadTexts:
    vdslPerfDataLoss.setUnits("seconds")
_VdslPerfDataLprs_Type = Unsigned32
_VdslPerfDataLprs_Object = MibTableColumn
vdslPerfDataLprs = _VdslPerfDataLprs_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 4, 1, 5),
    _VdslPerfDataLprs_Type()
)
vdslPerfDataLprs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslPerfDataLprs.setStatus("current")
if mibBuilder.loadTexts:
    vdslPerfDataLprs.setUnits("seconds")
_VdslPerfDataLols_Type = Unsigned32
_VdslPerfDataLols_Object = MibTableColumn
vdslPerfDataLols = _VdslPerfDataLols_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 4, 1, 6),
    _VdslPerfDataLols_Type()
)
vdslPerfDataLols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslPerfDataLols.setStatus("current")
if mibBuilder.loadTexts:
    vdslPerfDataLols.setUnits("seconds")
_VdslPerfDataESs_Type = Unsigned32
_VdslPerfDataESs_Object = MibTableColumn
vdslPerfDataESs = _VdslPerfDataESs_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 4, 1, 7),
    _VdslPerfDataESs_Type()
)
vdslPerfDataESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslPerfDataESs.setStatus("current")
if mibBuilder.loadTexts:
    vdslPerfDataESs.setUnits("seconds")
_VdslPerfDataSESs_Type = Unsigned32
_VdslPerfDataSESs_Object = MibTableColumn
vdslPerfDataSESs = _VdslPerfDataSESs_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 4, 1, 8),
    _VdslPerfDataSESs_Type()
)
vdslPerfDataSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslPerfDataSESs.setStatus("current")
if mibBuilder.loadTexts:
    vdslPerfDataSESs.setUnits("seconds")
_VdslPerfDataUASs_Type = Unsigned32
_VdslPerfDataUASs_Object = MibTableColumn
vdslPerfDataUASs = _VdslPerfDataUASs_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 4, 1, 9),
    _VdslPerfDataUASs_Type()
)
vdslPerfDataUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslPerfDataUASs.setStatus("current")
if mibBuilder.loadTexts:
    vdslPerfDataUASs.setUnits("seconds")
_VdslPerfDataInits_Type = Unsigned32
_VdslPerfDataInits_Object = MibTableColumn
vdslPerfDataInits = _VdslPerfDataInits_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 4, 1, 10),
    _VdslPerfDataInits_Type()
)
vdslPerfDataInits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslPerfDataInits.setStatus("current")
if mibBuilder.loadTexts:
    vdslPerfDataInits.setUnits("occurrences")
_VdslPerfDataCurr15MinTimeElapsed_Type = HCPerfTimeElapsed
_VdslPerfDataCurr15MinTimeElapsed_Object = MibTableColumn
vdslPerfDataCurr15MinTimeElapsed = _VdslPerfDataCurr15MinTimeElapsed_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 4, 1, 11),
    _VdslPerfDataCurr15MinTimeElapsed_Type()
)
vdslPerfDataCurr15MinTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslPerfDataCurr15MinTimeElapsed.setStatus("current")
if mibBuilder.loadTexts:
    vdslPerfDataCurr15MinTimeElapsed.setUnits("seconds")
_VdslPerfDataCurr15MinLofs_Type = HCPerfCurrentCount
_VdslPerfDataCurr15MinLofs_Object = MibTableColumn
vdslPerfDataCurr15MinLofs = _VdslPerfDataCurr15MinLofs_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 4, 1, 12),
    _VdslPerfDataCurr15MinLofs_Type()
)
vdslPerfDataCurr15MinLofs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslPerfDataCurr15MinLofs.setStatus("current")
if mibBuilder.loadTexts:
    vdslPerfDataCurr15MinLofs.setUnits("seconds")
_VdslPerfDataCurr15MinLoss_Type = HCPerfCurrentCount
_VdslPerfDataCurr15MinLoss_Object = MibTableColumn
vdslPerfDataCurr15MinLoss = _VdslPerfDataCurr15MinLoss_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 4, 1, 13),
    _VdslPerfDataCurr15MinLoss_Type()
)
vdslPerfDataCurr15MinLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslPerfDataCurr15MinLoss.setStatus("current")
if mibBuilder.loadTexts:
    vdslPerfDataCurr15MinLoss.setUnits("seconds")
_VdslPerfDataCurr15MinLprs_Type = HCPerfCurrentCount
_VdslPerfDataCurr15MinLprs_Object = MibTableColumn
vdslPerfDataCurr15MinLprs = _VdslPerfDataCurr15MinLprs_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 4, 1, 14),
    _VdslPerfDataCurr15MinLprs_Type()
)
vdslPerfDataCurr15MinLprs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslPerfDataCurr15MinLprs.setStatus("current")
if mibBuilder.loadTexts:
    vdslPerfDataCurr15MinLprs.setUnits("seconds")
_VdslPerfDataCurr15MinLols_Type = HCPerfCurrentCount
_VdslPerfDataCurr15MinLols_Object = MibTableColumn
vdslPerfDataCurr15MinLols = _VdslPerfDataCurr15MinLols_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 4, 1, 15),
    _VdslPerfDataCurr15MinLols_Type()
)
vdslPerfDataCurr15MinLols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslPerfDataCurr15MinLols.setStatus("current")
if mibBuilder.loadTexts:
    vdslPerfDataCurr15MinLols.setUnits("seconds")
_VdslPerfDataCurr15MinESs_Type = HCPerfCurrentCount
_VdslPerfDataCurr15MinESs_Object = MibTableColumn
vdslPerfDataCurr15MinESs = _VdslPerfDataCurr15MinESs_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 4, 1, 16),
    _VdslPerfDataCurr15MinESs_Type()
)
vdslPerfDataCurr15MinESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslPerfDataCurr15MinESs.setStatus("current")
if mibBuilder.loadTexts:
    vdslPerfDataCurr15MinESs.setUnits("seconds")
_VdslPerfDataCurr15MinSESs_Type = HCPerfCurrentCount
_VdslPerfDataCurr15MinSESs_Object = MibTableColumn
vdslPerfDataCurr15MinSESs = _VdslPerfDataCurr15MinSESs_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 4, 1, 17),
    _VdslPerfDataCurr15MinSESs_Type()
)
vdslPerfDataCurr15MinSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslPerfDataCurr15MinSESs.setStatus("current")
if mibBuilder.loadTexts:
    vdslPerfDataCurr15MinSESs.setUnits("seconds")
_VdslPerfDataCurr15MinUASs_Type = HCPerfCurrentCount
_VdslPerfDataCurr15MinUASs_Object = MibTableColumn
vdslPerfDataCurr15MinUASs = _VdslPerfDataCurr15MinUASs_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 4, 1, 18),
    _VdslPerfDataCurr15MinUASs_Type()
)
vdslPerfDataCurr15MinUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslPerfDataCurr15MinUASs.setStatus("current")
if mibBuilder.loadTexts:
    vdslPerfDataCurr15MinUASs.setUnits("seconds")
_VdslPerfDataCurr15MinInits_Type = HCPerfCurrentCount
_VdslPerfDataCurr15MinInits_Object = MibTableColumn
vdslPerfDataCurr15MinInits = _VdslPerfDataCurr15MinInits_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 4, 1, 19),
    _VdslPerfDataCurr15MinInits_Type()
)
vdslPerfDataCurr15MinInits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslPerfDataCurr15MinInits.setStatus("current")
if mibBuilder.loadTexts:
    vdslPerfDataCurr15MinInits.setUnits("occurrences")
_VdslPerfData1DayValidIntervals_Type = HCPerfValidIntervals
_VdslPerfData1DayValidIntervals_Object = MibTableColumn
vdslPerfData1DayValidIntervals = _VdslPerfData1DayValidIntervals_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 4, 1, 20),
    _VdslPerfData1DayValidIntervals_Type()
)
vdslPerfData1DayValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslPerfData1DayValidIntervals.setStatus("current")
if mibBuilder.loadTexts:
    vdslPerfData1DayValidIntervals.setUnits("intervals")
_VdslPerfData1DayInvalidIntervals_Type = HCPerfInvalidIntervals
_VdslPerfData1DayInvalidIntervals_Object = MibTableColumn
vdslPerfData1DayInvalidIntervals = _VdslPerfData1DayInvalidIntervals_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 4, 1, 21),
    _VdslPerfData1DayInvalidIntervals_Type()
)
vdslPerfData1DayInvalidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslPerfData1DayInvalidIntervals.setStatus("current")
if mibBuilder.loadTexts:
    vdslPerfData1DayInvalidIntervals.setUnits("intervals")
_VdslPerfDataCurr1DayTimeElapsed_Type = HCPerfTimeElapsed
_VdslPerfDataCurr1DayTimeElapsed_Object = MibTableColumn
vdslPerfDataCurr1DayTimeElapsed = _VdslPerfDataCurr1DayTimeElapsed_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 4, 1, 22),
    _VdslPerfDataCurr1DayTimeElapsed_Type()
)
vdslPerfDataCurr1DayTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslPerfDataCurr1DayTimeElapsed.setStatus("current")
if mibBuilder.loadTexts:
    vdslPerfDataCurr1DayTimeElapsed.setUnits("seconds")
_VdslPerfDataCurr1DayLofs_Type = Unsigned32
_VdslPerfDataCurr1DayLofs_Object = MibTableColumn
vdslPerfDataCurr1DayLofs = _VdslPerfDataCurr1DayLofs_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 4, 1, 23),
    _VdslPerfDataCurr1DayLofs_Type()
)
vdslPerfDataCurr1DayLofs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslPerfDataCurr1DayLofs.setStatus("current")
if mibBuilder.loadTexts:
    vdslPerfDataCurr1DayLofs.setUnits("seconds")
_VdslPerfDataCurr1DayLoss_Type = Unsigned32
_VdslPerfDataCurr1DayLoss_Object = MibTableColumn
vdslPerfDataCurr1DayLoss = _VdslPerfDataCurr1DayLoss_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 4, 1, 24),
    _VdslPerfDataCurr1DayLoss_Type()
)
vdslPerfDataCurr1DayLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslPerfDataCurr1DayLoss.setStatus("current")
if mibBuilder.loadTexts:
    vdslPerfDataCurr1DayLoss.setUnits("seconds")
_VdslPerfDataCurr1DayLprs_Type = Unsigned32
_VdslPerfDataCurr1DayLprs_Object = MibTableColumn
vdslPerfDataCurr1DayLprs = _VdslPerfDataCurr1DayLprs_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 4, 1, 25),
    _VdslPerfDataCurr1DayLprs_Type()
)
vdslPerfDataCurr1DayLprs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslPerfDataCurr1DayLprs.setStatus("current")
if mibBuilder.loadTexts:
    vdslPerfDataCurr1DayLprs.setUnits("seconds")
_VdslPerfDataCurr1DayLols_Type = Unsigned32
_VdslPerfDataCurr1DayLols_Object = MibTableColumn
vdslPerfDataCurr1DayLols = _VdslPerfDataCurr1DayLols_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 4, 1, 26),
    _VdslPerfDataCurr1DayLols_Type()
)
vdslPerfDataCurr1DayLols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslPerfDataCurr1DayLols.setStatus("current")
if mibBuilder.loadTexts:
    vdslPerfDataCurr1DayLols.setUnits("seconds")
_VdslPerfDataCurr1DayESs_Type = Unsigned32
_VdslPerfDataCurr1DayESs_Object = MibTableColumn
vdslPerfDataCurr1DayESs = _VdslPerfDataCurr1DayESs_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 4, 1, 27),
    _VdslPerfDataCurr1DayESs_Type()
)
vdslPerfDataCurr1DayESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslPerfDataCurr1DayESs.setStatus("current")
if mibBuilder.loadTexts:
    vdslPerfDataCurr1DayESs.setUnits("seconds")
_VdslPerfDataCurr1DaySESs_Type = Unsigned32
_VdslPerfDataCurr1DaySESs_Object = MibTableColumn
vdslPerfDataCurr1DaySESs = _VdslPerfDataCurr1DaySESs_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 4, 1, 28),
    _VdslPerfDataCurr1DaySESs_Type()
)
vdslPerfDataCurr1DaySESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslPerfDataCurr1DaySESs.setStatus("current")
if mibBuilder.loadTexts:
    vdslPerfDataCurr1DaySESs.setUnits("seconds")
_VdslPerfDataCurr1DayUASs_Type = Unsigned32
_VdslPerfDataCurr1DayUASs_Object = MibTableColumn
vdslPerfDataCurr1DayUASs = _VdslPerfDataCurr1DayUASs_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 4, 1, 29),
    _VdslPerfDataCurr1DayUASs_Type()
)
vdslPerfDataCurr1DayUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslPerfDataCurr1DayUASs.setStatus("current")
if mibBuilder.loadTexts:
    vdslPerfDataCurr1DayUASs.setUnits("seconds")
_VdslPerfDataCurr1DayInits_Type = Unsigned32
_VdslPerfDataCurr1DayInits_Object = MibTableColumn
vdslPerfDataCurr1DayInits = _VdslPerfDataCurr1DayInits_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 4, 1, 30),
    _VdslPerfDataCurr1DayInits_Type()
)
vdslPerfDataCurr1DayInits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslPerfDataCurr1DayInits.setStatus("current")
if mibBuilder.loadTexts:
    vdslPerfDataCurr1DayInits.setUnits("seconds")
_VdslPerfIntervalTable_Object = MibTable
vdslPerfIntervalTable = _VdslPerfIntervalTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 5)
)
if mibBuilder.loadTexts:
    vdslPerfIntervalTable.setStatus("current")
_VdslPerfIntervalEntry_Object = MibTableRow
vdslPerfIntervalEntry = _VdslPerfIntervalEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 5, 1)
)
vdslPerfIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "VDSL-LINE-MIB", "vdslPhysSide"),
    (0, "VDSL-LINE-MIB", "vdslPerfIntervalNumber"),
)
if mibBuilder.loadTexts:
    vdslPerfIntervalEntry.setStatus("current")


class _VdslPerfIntervalNumber_Type(Unsigned32):
    """Custom type vdslPerfIntervalNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_VdslPerfIntervalNumber_Type.__name__ = "Unsigned32"
_VdslPerfIntervalNumber_Object = MibTableColumn
vdslPerfIntervalNumber = _VdslPerfIntervalNumber_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 5, 1, 1),
    _VdslPerfIntervalNumber_Type()
)
vdslPerfIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vdslPerfIntervalNumber.setStatus("current")
_VdslPerfIntervalLofs_Type = HCPerfIntervalCount
_VdslPerfIntervalLofs_Object = MibTableColumn
vdslPerfIntervalLofs = _VdslPerfIntervalLofs_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 5, 1, 2),
    _VdslPerfIntervalLofs_Type()
)
vdslPerfIntervalLofs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslPerfIntervalLofs.setStatus("current")
if mibBuilder.loadTexts:
    vdslPerfIntervalLofs.setUnits("seconds")
_VdslPerfIntervalLoss_Type = HCPerfIntervalCount
_VdslPerfIntervalLoss_Object = MibTableColumn
vdslPerfIntervalLoss = _VdslPerfIntervalLoss_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 5, 1, 3),
    _VdslPerfIntervalLoss_Type()
)
vdslPerfIntervalLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslPerfIntervalLoss.setStatus("current")
if mibBuilder.loadTexts:
    vdslPerfIntervalLoss.setUnits("seconds")
_VdslPerfIntervalLprs_Type = HCPerfIntervalCount
_VdslPerfIntervalLprs_Object = MibTableColumn
vdslPerfIntervalLprs = _VdslPerfIntervalLprs_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 5, 1, 4),
    _VdslPerfIntervalLprs_Type()
)
vdslPerfIntervalLprs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslPerfIntervalLprs.setStatus("current")
if mibBuilder.loadTexts:
    vdslPerfIntervalLprs.setUnits("seconds")
_VdslPerfIntervalLols_Type = HCPerfIntervalCount
_VdslPerfIntervalLols_Object = MibTableColumn
vdslPerfIntervalLols = _VdslPerfIntervalLols_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 5, 1, 5),
    _VdslPerfIntervalLols_Type()
)
vdslPerfIntervalLols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslPerfIntervalLols.setStatus("current")
if mibBuilder.loadTexts:
    vdslPerfIntervalLols.setUnits("seconds")
_VdslPerfIntervalESs_Type = HCPerfIntervalCount
_VdslPerfIntervalESs_Object = MibTableColumn
vdslPerfIntervalESs = _VdslPerfIntervalESs_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 5, 1, 6),
    _VdslPerfIntervalESs_Type()
)
vdslPerfIntervalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslPerfIntervalESs.setStatus("current")
if mibBuilder.loadTexts:
    vdslPerfIntervalESs.setUnits("seconds")
_VdslPerfIntervalSESs_Type = HCPerfIntervalCount
_VdslPerfIntervalSESs_Object = MibTableColumn
vdslPerfIntervalSESs = _VdslPerfIntervalSESs_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 5, 1, 7),
    _VdslPerfIntervalSESs_Type()
)
vdslPerfIntervalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslPerfIntervalSESs.setStatus("current")
if mibBuilder.loadTexts:
    vdslPerfIntervalSESs.setUnits("seconds")
_VdslPerfIntervalUASs_Type = HCPerfIntervalCount
_VdslPerfIntervalUASs_Object = MibTableColumn
vdslPerfIntervalUASs = _VdslPerfIntervalUASs_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 5, 1, 8),
    _VdslPerfIntervalUASs_Type()
)
vdslPerfIntervalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslPerfIntervalUASs.setStatus("current")
if mibBuilder.loadTexts:
    vdslPerfIntervalUASs.setUnits("seconds")
_VdslPerfIntervalInits_Type = HCPerfIntervalCount
_VdslPerfIntervalInits_Object = MibTableColumn
vdslPerfIntervalInits = _VdslPerfIntervalInits_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 5, 1, 9),
    _VdslPerfIntervalInits_Type()
)
vdslPerfIntervalInits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslPerfIntervalInits.setStatus("current")
_VdslPerf1DayIntervalTable_Object = MibTable
vdslPerf1DayIntervalTable = _VdslPerf1DayIntervalTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 6)
)
if mibBuilder.loadTexts:
    vdslPerf1DayIntervalTable.setStatus("current")
_VdslPerf1DayIntervalEntry_Object = MibTableRow
vdslPerf1DayIntervalEntry = _VdslPerf1DayIntervalEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 6, 1)
)
vdslPerf1DayIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "VDSL-LINE-MIB", "vdslPhysSide"),
    (0, "VDSL-LINE-MIB", "vdslPerf1DayIntervalNumber"),
)
if mibBuilder.loadTexts:
    vdslPerf1DayIntervalEntry.setStatus("current")


class _VdslPerf1DayIntervalNumber_Type(Unsigned32):
    """Custom type vdslPerf1DayIntervalNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_VdslPerf1DayIntervalNumber_Type.__name__ = "Unsigned32"
_VdslPerf1DayIntervalNumber_Object = MibTableColumn
vdslPerf1DayIntervalNumber = _VdslPerf1DayIntervalNumber_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 6, 1, 1),
    _VdslPerf1DayIntervalNumber_Type()
)
vdslPerf1DayIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vdslPerf1DayIntervalNumber.setStatus("current")
_VdslPerf1DayIntervalMoniSecs_Type = HCPerfTimeElapsed
_VdslPerf1DayIntervalMoniSecs_Object = MibTableColumn
vdslPerf1DayIntervalMoniSecs = _VdslPerf1DayIntervalMoniSecs_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 6, 1, 2),
    _VdslPerf1DayIntervalMoniSecs_Type()
)
vdslPerf1DayIntervalMoniSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslPerf1DayIntervalMoniSecs.setStatus("current")
if mibBuilder.loadTexts:
    vdslPerf1DayIntervalMoniSecs.setUnits("seconds")
_VdslPerf1DayIntervalLofs_Type = Unsigned32
_VdslPerf1DayIntervalLofs_Object = MibTableColumn
vdslPerf1DayIntervalLofs = _VdslPerf1DayIntervalLofs_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 6, 1, 3),
    _VdslPerf1DayIntervalLofs_Type()
)
vdslPerf1DayIntervalLofs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslPerf1DayIntervalLofs.setStatus("current")
if mibBuilder.loadTexts:
    vdslPerf1DayIntervalLofs.setUnits("seconds")
_VdslPerf1DayIntervalLoss_Type = Unsigned32
_VdslPerf1DayIntervalLoss_Object = MibTableColumn
vdslPerf1DayIntervalLoss = _VdslPerf1DayIntervalLoss_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 6, 1, 4),
    _VdslPerf1DayIntervalLoss_Type()
)
vdslPerf1DayIntervalLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslPerf1DayIntervalLoss.setStatus("current")
if mibBuilder.loadTexts:
    vdslPerf1DayIntervalLoss.setUnits("seconds")
_VdslPerf1DayIntervalLprs_Type = Unsigned32
_VdslPerf1DayIntervalLprs_Object = MibTableColumn
vdslPerf1DayIntervalLprs = _VdslPerf1DayIntervalLprs_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 6, 1, 5),
    _VdslPerf1DayIntervalLprs_Type()
)
vdslPerf1DayIntervalLprs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslPerf1DayIntervalLprs.setStatus("current")
if mibBuilder.loadTexts:
    vdslPerf1DayIntervalLprs.setUnits("seconds")
_VdslPerf1DayIntervalLols_Type = Unsigned32
_VdslPerf1DayIntervalLols_Object = MibTableColumn
vdslPerf1DayIntervalLols = _VdslPerf1DayIntervalLols_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 6, 1, 6),
    _VdslPerf1DayIntervalLols_Type()
)
vdslPerf1DayIntervalLols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslPerf1DayIntervalLols.setStatus("current")
if mibBuilder.loadTexts:
    vdslPerf1DayIntervalLols.setUnits("seconds")
_VdslPerf1DayIntervalESs_Type = Unsigned32
_VdslPerf1DayIntervalESs_Object = MibTableColumn
vdslPerf1DayIntervalESs = _VdslPerf1DayIntervalESs_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 6, 1, 7),
    _VdslPerf1DayIntervalESs_Type()
)
vdslPerf1DayIntervalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslPerf1DayIntervalESs.setStatus("current")
if mibBuilder.loadTexts:
    vdslPerf1DayIntervalESs.setUnits("seconds")
_VdslPerf1DayIntervalSESs_Type = Unsigned32
_VdslPerf1DayIntervalSESs_Object = MibTableColumn
vdslPerf1DayIntervalSESs = _VdslPerf1DayIntervalSESs_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 6, 1, 8),
    _VdslPerf1DayIntervalSESs_Type()
)
vdslPerf1DayIntervalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslPerf1DayIntervalSESs.setStatus("current")
if mibBuilder.loadTexts:
    vdslPerf1DayIntervalSESs.setUnits("seconds")
_VdslPerf1DayIntervalUASs_Type = Unsigned32
_VdslPerf1DayIntervalUASs_Object = MibTableColumn
vdslPerf1DayIntervalUASs = _VdslPerf1DayIntervalUASs_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 6, 1, 9),
    _VdslPerf1DayIntervalUASs_Type()
)
vdslPerf1DayIntervalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslPerf1DayIntervalUASs.setStatus("current")
if mibBuilder.loadTexts:
    vdslPerf1DayIntervalUASs.setUnits("seconds")
_VdslPerf1DayIntervalInits_Type = Unsigned32
_VdslPerf1DayIntervalInits_Object = MibTableColumn
vdslPerf1DayIntervalInits = _VdslPerf1DayIntervalInits_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 6, 1, 10),
    _VdslPerf1DayIntervalInits_Type()
)
vdslPerf1DayIntervalInits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslPerf1DayIntervalInits.setStatus("current")
if mibBuilder.loadTexts:
    vdslPerf1DayIntervalInits.setUnits("seconds")
_VdslChanPerfDataTable_Object = MibTable
vdslChanPerfDataTable = _VdslChanPerfDataTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 7)
)
if mibBuilder.loadTexts:
    vdslChanPerfDataTable.setStatus("current")
_VdslChanPerfDataEntry_Object = MibTableRow
vdslChanPerfDataEntry = _VdslChanPerfDataEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 7, 1)
)
vdslChanPerfDataEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "VDSL-LINE-MIB", "vdslPhysSide"),
)
if mibBuilder.loadTexts:
    vdslChanPerfDataEntry.setStatus("current")
_VdslChanValidIntervals_Type = HCPerfValidIntervals
_VdslChanValidIntervals_Object = MibTableColumn
vdslChanValidIntervals = _VdslChanValidIntervals_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 7, 1, 1),
    _VdslChanValidIntervals_Type()
)
vdslChanValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslChanValidIntervals.setStatus("current")
if mibBuilder.loadTexts:
    vdslChanValidIntervals.setUnits("intervals")
_VdslChanInvalidIntervals_Type = HCPerfInvalidIntervals
_VdslChanInvalidIntervals_Object = MibTableColumn
vdslChanInvalidIntervals = _VdslChanInvalidIntervals_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 7, 1, 2),
    _VdslChanInvalidIntervals_Type()
)
vdslChanInvalidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslChanInvalidIntervals.setStatus("current")
if mibBuilder.loadTexts:
    vdslChanInvalidIntervals.setUnits("intervals")
_VdslChanFixedOctets_Type = ZeroBasedCounter64
_VdslChanFixedOctets_Object = MibTableColumn
vdslChanFixedOctets = _VdslChanFixedOctets_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 7, 1, 3),
    _VdslChanFixedOctets_Type()
)
vdslChanFixedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslChanFixedOctets.setStatus("current")
if mibBuilder.loadTexts:
    vdslChanFixedOctets.setUnits("octets")
_VdslChanBadBlks_Type = ZeroBasedCounter64
_VdslChanBadBlks_Object = MibTableColumn
vdslChanBadBlks = _VdslChanBadBlks_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 7, 1, 4),
    _VdslChanBadBlks_Type()
)
vdslChanBadBlks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslChanBadBlks.setStatus("current")
if mibBuilder.loadTexts:
    vdslChanBadBlks.setUnits("blocks")
_VdslChanCurr15MinTimeElapsed_Type = HCPerfTimeElapsed
_VdslChanCurr15MinTimeElapsed_Object = MibTableColumn
vdslChanCurr15MinTimeElapsed = _VdslChanCurr15MinTimeElapsed_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 7, 1, 5),
    _VdslChanCurr15MinTimeElapsed_Type()
)
vdslChanCurr15MinTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslChanCurr15MinTimeElapsed.setStatus("current")
if mibBuilder.loadTexts:
    vdslChanCurr15MinTimeElapsed.setUnits("seconds")
_VdslChanCurr15MinFixedOctets_Type = HCPerfCurrentCount
_VdslChanCurr15MinFixedOctets_Object = MibTableColumn
vdslChanCurr15MinFixedOctets = _VdslChanCurr15MinFixedOctets_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 7, 1, 6),
    _VdslChanCurr15MinFixedOctets_Type()
)
vdslChanCurr15MinFixedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslChanCurr15MinFixedOctets.setStatus("current")
if mibBuilder.loadTexts:
    vdslChanCurr15MinFixedOctets.setUnits("octets")
_VdslChanCurr15MinBadBlks_Type = HCPerfCurrentCount
_VdslChanCurr15MinBadBlks_Object = MibTableColumn
vdslChanCurr15MinBadBlks = _VdslChanCurr15MinBadBlks_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 7, 1, 7),
    _VdslChanCurr15MinBadBlks_Type()
)
vdslChanCurr15MinBadBlks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslChanCurr15MinBadBlks.setStatus("current")
if mibBuilder.loadTexts:
    vdslChanCurr15MinBadBlks.setUnits("blocks")
_VdslChan1DayValidIntervals_Type = HCPerfValidIntervals
_VdslChan1DayValidIntervals_Object = MibTableColumn
vdslChan1DayValidIntervals = _VdslChan1DayValidIntervals_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 7, 1, 8),
    _VdslChan1DayValidIntervals_Type()
)
vdslChan1DayValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslChan1DayValidIntervals.setStatus("current")
_VdslChan1DayInvalidIntervals_Type = HCPerfInvalidIntervals
_VdslChan1DayInvalidIntervals_Object = MibTableColumn
vdslChan1DayInvalidIntervals = _VdslChan1DayInvalidIntervals_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 7, 1, 9),
    _VdslChan1DayInvalidIntervals_Type()
)
vdslChan1DayInvalidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslChan1DayInvalidIntervals.setStatus("current")
_VdslChanCurr1DayTimeElapsed_Type = HCPerfTimeElapsed
_VdslChanCurr1DayTimeElapsed_Object = MibTableColumn
vdslChanCurr1DayTimeElapsed = _VdslChanCurr1DayTimeElapsed_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 7, 1, 10),
    _VdslChanCurr1DayTimeElapsed_Type()
)
vdslChanCurr1DayTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslChanCurr1DayTimeElapsed.setStatus("current")
if mibBuilder.loadTexts:
    vdslChanCurr1DayTimeElapsed.setUnits("seconds")
_VdslChanCurr1DayFixedOctets_Type = HCPerfCurrentCount
_VdslChanCurr1DayFixedOctets_Object = MibTableColumn
vdslChanCurr1DayFixedOctets = _VdslChanCurr1DayFixedOctets_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 7, 1, 11),
    _VdslChanCurr1DayFixedOctets_Type()
)
vdslChanCurr1DayFixedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslChanCurr1DayFixedOctets.setStatus("current")
if mibBuilder.loadTexts:
    vdslChanCurr1DayFixedOctets.setUnits("octets")
_VdslChanCurr1DayBadBlks_Type = HCPerfCurrentCount
_VdslChanCurr1DayBadBlks_Object = MibTableColumn
vdslChanCurr1DayBadBlks = _VdslChanCurr1DayBadBlks_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 7, 1, 12),
    _VdslChanCurr1DayBadBlks_Type()
)
vdslChanCurr1DayBadBlks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslChanCurr1DayBadBlks.setStatus("current")
if mibBuilder.loadTexts:
    vdslChanCurr1DayBadBlks.setUnits("blocks")
_VdslChanIntervalTable_Object = MibTable
vdslChanIntervalTable = _VdslChanIntervalTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 8)
)
if mibBuilder.loadTexts:
    vdslChanIntervalTable.setStatus("current")
_VdslChanIntervalEntry_Object = MibTableRow
vdslChanIntervalEntry = _VdslChanIntervalEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 8, 1)
)
vdslChanIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "VDSL-LINE-MIB", "vdslPhysSide"),
    (0, "VDSL-LINE-MIB", "vdslChanIntervalNumber"),
)
if mibBuilder.loadTexts:
    vdslChanIntervalEntry.setStatus("current")


class _VdslChanIntervalNumber_Type(Unsigned32):
    """Custom type vdslChanIntervalNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_VdslChanIntervalNumber_Type.__name__ = "Unsigned32"
_VdslChanIntervalNumber_Object = MibTableColumn
vdslChanIntervalNumber = _VdslChanIntervalNumber_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 8, 1, 1),
    _VdslChanIntervalNumber_Type()
)
vdslChanIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vdslChanIntervalNumber.setStatus("current")
_VdslChanIntervalFixedOctets_Type = HCPerfIntervalCount
_VdslChanIntervalFixedOctets_Object = MibTableColumn
vdslChanIntervalFixedOctets = _VdslChanIntervalFixedOctets_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 8, 1, 2),
    _VdslChanIntervalFixedOctets_Type()
)
vdslChanIntervalFixedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslChanIntervalFixedOctets.setStatus("current")
if mibBuilder.loadTexts:
    vdslChanIntervalFixedOctets.setUnits("octets")
_VdslChanIntervalBadBlks_Type = HCPerfIntervalCount
_VdslChanIntervalBadBlks_Object = MibTableColumn
vdslChanIntervalBadBlks = _VdslChanIntervalBadBlks_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 8, 1, 3),
    _VdslChanIntervalBadBlks_Type()
)
vdslChanIntervalBadBlks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslChanIntervalBadBlks.setStatus("current")
if mibBuilder.loadTexts:
    vdslChanIntervalBadBlks.setUnits("blocks")
_VdslChan1DayIntervalTable_Object = MibTable
vdslChan1DayIntervalTable = _VdslChan1DayIntervalTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 9)
)
if mibBuilder.loadTexts:
    vdslChan1DayIntervalTable.setStatus("current")
_VdslChan1DayIntervalEntry_Object = MibTableRow
vdslChan1DayIntervalEntry = _VdslChan1DayIntervalEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 9, 1)
)
vdslChan1DayIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "VDSL-LINE-MIB", "vdslPhysSide"),
    (0, "VDSL-LINE-MIB", "vdslChan1DayIntervalNumber"),
)
if mibBuilder.loadTexts:
    vdslChan1DayIntervalEntry.setStatus("current")


class _VdslChan1DayIntervalNumber_Type(Unsigned32):
    """Custom type vdslChan1DayIntervalNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_VdslChan1DayIntervalNumber_Type.__name__ = "Unsigned32"
_VdslChan1DayIntervalNumber_Object = MibTableColumn
vdslChan1DayIntervalNumber = _VdslChan1DayIntervalNumber_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 9, 1, 1),
    _VdslChan1DayIntervalNumber_Type()
)
vdslChan1DayIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vdslChan1DayIntervalNumber.setStatus("current")
_VdslChan1DayIntervalMoniSecs_Type = HCPerfTimeElapsed
_VdslChan1DayIntervalMoniSecs_Object = MibTableColumn
vdslChan1DayIntervalMoniSecs = _VdslChan1DayIntervalMoniSecs_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 9, 1, 2),
    _VdslChan1DayIntervalMoniSecs_Type()
)
vdslChan1DayIntervalMoniSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslChan1DayIntervalMoniSecs.setStatus("current")
if mibBuilder.loadTexts:
    vdslChan1DayIntervalMoniSecs.setUnits("seconds")
_VdslChan1DayIntervalFixedOctets_Type = HCPerfCurrentCount
_VdslChan1DayIntervalFixedOctets_Object = MibTableColumn
vdslChan1DayIntervalFixedOctets = _VdslChan1DayIntervalFixedOctets_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 9, 1, 3),
    _VdslChan1DayIntervalFixedOctets_Type()
)
vdslChan1DayIntervalFixedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslChan1DayIntervalFixedOctets.setStatus("current")
if mibBuilder.loadTexts:
    vdslChan1DayIntervalFixedOctets.setUnits("octets")
_VdslChan1DayIntervalBadBlks_Type = HCPerfCurrentCount
_VdslChan1DayIntervalBadBlks_Object = MibTableColumn
vdslChan1DayIntervalBadBlks = _VdslChan1DayIntervalBadBlks_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 9, 1, 4),
    _VdslChan1DayIntervalBadBlks_Type()
)
vdslChan1DayIntervalBadBlks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslChan1DayIntervalBadBlks.setStatus("current")
if mibBuilder.loadTexts:
    vdslChan1DayIntervalBadBlks.setUnits("blocks")
_VdslLineConfProfileTable_Object = MibTable
vdslLineConfProfileTable = _VdslLineConfProfileTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 11)
)
if mibBuilder.loadTexts:
    vdslLineConfProfileTable.setStatus("current")
_VdslLineConfProfileEntry_Object = MibTableRow
vdslLineConfProfileEntry = _VdslLineConfProfileEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 11, 1)
)
vdslLineConfProfileEntry.setIndexNames(
    (0, "VDSL-LINE-MIB", "vdslLineConfProfileName"),
)
if mibBuilder.loadTexts:
    vdslLineConfProfileEntry.setStatus("current")


class _VdslLineConfProfileName_Type(SnmpAdminString):
    """Custom type vdslLineConfProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_VdslLineConfProfileName_Type.__name__ = "SnmpAdminString"
_VdslLineConfProfileName_Object = MibTableColumn
vdslLineConfProfileName = _VdslLineConfProfileName_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 11, 1, 1),
    _VdslLineConfProfileName_Type()
)
vdslLineConfProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vdslLineConfProfileName.setStatus("current")


class _VdslLineConfDownRateMode_Type(Integer32):
    """Custom type vdslLineConfDownRateMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("adaptAtInit", 2),
          ("manual", 1))
    )


_VdslLineConfDownRateMode_Type.__name__ = "Integer32"
_VdslLineConfDownRateMode_Object = MibTableColumn
vdslLineConfDownRateMode = _VdslLineConfDownRateMode_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 11, 1, 2),
    _VdslLineConfDownRateMode_Type()
)
vdslLineConfDownRateMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vdslLineConfDownRateMode.setStatus("current")


class _VdslLineConfUpRateMode_Type(Integer32):
    """Custom type vdslLineConfUpRateMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("adaptAtInit", 2),
          ("manual", 1))
    )


_VdslLineConfUpRateMode_Type.__name__ = "Integer32"
_VdslLineConfUpRateMode_Object = MibTableColumn
vdslLineConfUpRateMode = _VdslLineConfUpRateMode_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 11, 1, 3),
    _VdslLineConfUpRateMode_Type()
)
vdslLineConfUpRateMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vdslLineConfUpRateMode.setStatus("current")


class _VdslLineConfDownMaxPwr_Type(Unsigned32):
    """Custom type vdslLineConfDownMaxPwr based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 58),
    )


_VdslLineConfDownMaxPwr_Type.__name__ = "Unsigned32"
_VdslLineConfDownMaxPwr_Object = MibTableColumn
vdslLineConfDownMaxPwr = _VdslLineConfDownMaxPwr_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 11, 1, 4),
    _VdslLineConfDownMaxPwr_Type()
)
vdslLineConfDownMaxPwr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vdslLineConfDownMaxPwr.setStatus("current")
if mibBuilder.loadTexts:
    vdslLineConfDownMaxPwr.setUnits("0.25dBm")


class _VdslLineConfUpMaxPwr_Type(Unsigned32):
    """Custom type vdslLineConfUpMaxPwr based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 58),
    )


_VdslLineConfUpMaxPwr_Type.__name__ = "Unsigned32"
_VdslLineConfUpMaxPwr_Object = MibTableColumn
vdslLineConfUpMaxPwr = _VdslLineConfUpMaxPwr_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 11, 1, 5),
    _VdslLineConfUpMaxPwr_Type()
)
vdslLineConfUpMaxPwr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vdslLineConfUpMaxPwr.setStatus("current")
if mibBuilder.loadTexts:
    vdslLineConfUpMaxPwr.setUnits("0.25dBm")


class _VdslLineConfDownMaxSnrMgn_Type(Unsigned32):
    """Custom type vdslLineConfDownMaxSnrMgn based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_VdslLineConfDownMaxSnrMgn_Type.__name__ = "Unsigned32"
_VdslLineConfDownMaxSnrMgn_Object = MibTableColumn
vdslLineConfDownMaxSnrMgn = _VdslLineConfDownMaxSnrMgn_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 11, 1, 6),
    _VdslLineConfDownMaxSnrMgn_Type()
)
vdslLineConfDownMaxSnrMgn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vdslLineConfDownMaxSnrMgn.setStatus("current")
if mibBuilder.loadTexts:
    vdslLineConfDownMaxSnrMgn.setUnits("0.25dBm")


class _VdslLineConfDownMinSnrMgn_Type(Unsigned32):
    """Custom type vdslLineConfDownMinSnrMgn based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_VdslLineConfDownMinSnrMgn_Type.__name__ = "Unsigned32"
_VdslLineConfDownMinSnrMgn_Object = MibTableColumn
vdslLineConfDownMinSnrMgn = _VdslLineConfDownMinSnrMgn_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 11, 1, 7),
    _VdslLineConfDownMinSnrMgn_Type()
)
vdslLineConfDownMinSnrMgn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vdslLineConfDownMinSnrMgn.setStatus("current")
if mibBuilder.loadTexts:
    vdslLineConfDownMinSnrMgn.setUnits("0.25dBm")


class _VdslLineConfDownTargetSnrMgn_Type(Unsigned32):
    """Custom type vdslLineConfDownTargetSnrMgn based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_VdslLineConfDownTargetSnrMgn_Type.__name__ = "Unsigned32"
_VdslLineConfDownTargetSnrMgn_Object = MibTableColumn
vdslLineConfDownTargetSnrMgn = _VdslLineConfDownTargetSnrMgn_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 11, 1, 8),
    _VdslLineConfDownTargetSnrMgn_Type()
)
vdslLineConfDownTargetSnrMgn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vdslLineConfDownTargetSnrMgn.setStatus("current")
if mibBuilder.loadTexts:
    vdslLineConfDownTargetSnrMgn.setUnits("0.25dBm")


class _VdslLineConfUpMaxSnrMgn_Type(Unsigned32):
    """Custom type vdslLineConfUpMaxSnrMgn based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_VdslLineConfUpMaxSnrMgn_Type.__name__ = "Unsigned32"
_VdslLineConfUpMaxSnrMgn_Object = MibTableColumn
vdslLineConfUpMaxSnrMgn = _VdslLineConfUpMaxSnrMgn_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 11, 1, 9),
    _VdslLineConfUpMaxSnrMgn_Type()
)
vdslLineConfUpMaxSnrMgn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vdslLineConfUpMaxSnrMgn.setStatus("current")
if mibBuilder.loadTexts:
    vdslLineConfUpMaxSnrMgn.setUnits("0.25dBm")


class _VdslLineConfUpMinSnrMgn_Type(Unsigned32):
    """Custom type vdslLineConfUpMinSnrMgn based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_VdslLineConfUpMinSnrMgn_Type.__name__ = "Unsigned32"
_VdslLineConfUpMinSnrMgn_Object = MibTableColumn
vdslLineConfUpMinSnrMgn = _VdslLineConfUpMinSnrMgn_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 11, 1, 10),
    _VdslLineConfUpMinSnrMgn_Type()
)
vdslLineConfUpMinSnrMgn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vdslLineConfUpMinSnrMgn.setStatus("current")
if mibBuilder.loadTexts:
    vdslLineConfUpMinSnrMgn.setUnits("0.25dBm")


class _VdslLineConfUpTargetSnrMgn_Type(Unsigned32):
    """Custom type vdslLineConfUpTargetSnrMgn based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_VdslLineConfUpTargetSnrMgn_Type.__name__ = "Unsigned32"
_VdslLineConfUpTargetSnrMgn_Object = MibTableColumn
vdslLineConfUpTargetSnrMgn = _VdslLineConfUpTargetSnrMgn_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 11, 1, 11),
    _VdslLineConfUpTargetSnrMgn_Type()
)
vdslLineConfUpTargetSnrMgn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vdslLineConfUpTargetSnrMgn.setStatus("current")
if mibBuilder.loadTexts:
    vdslLineConfUpTargetSnrMgn.setUnits("0.25dBm")


class _VdslLineConfDownFastMaxDataRate_Type(Unsigned32):
    """Custom type vdslLineConfDownFastMaxDataRate based on Unsigned32"""
    defaultValue = 0


_VdslLineConfDownFastMaxDataRate_Object = MibTableColumn
vdslLineConfDownFastMaxDataRate = _VdslLineConfDownFastMaxDataRate_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 11, 1, 12),
    _VdslLineConfDownFastMaxDataRate_Type()
)
vdslLineConfDownFastMaxDataRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vdslLineConfDownFastMaxDataRate.setStatus("current")
if mibBuilder.loadTexts:
    vdslLineConfDownFastMaxDataRate.setUnits("kbps")


class _VdslLineConfDownFastMinDataRate_Type(Unsigned32):
    """Custom type vdslLineConfDownFastMinDataRate based on Unsigned32"""
    defaultValue = 0


_VdslLineConfDownFastMinDataRate_Object = MibTableColumn
vdslLineConfDownFastMinDataRate = _VdslLineConfDownFastMinDataRate_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 11, 1, 13),
    _VdslLineConfDownFastMinDataRate_Type()
)
vdslLineConfDownFastMinDataRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vdslLineConfDownFastMinDataRate.setStatus("current")
if mibBuilder.loadTexts:
    vdslLineConfDownFastMinDataRate.setUnits("kbps")


class _VdslLineConfDownSlowMaxDataRate_Type(Unsigned32):
    """Custom type vdslLineConfDownSlowMaxDataRate based on Unsigned32"""
    defaultValue = 0


_VdslLineConfDownSlowMaxDataRate_Object = MibTableColumn
vdslLineConfDownSlowMaxDataRate = _VdslLineConfDownSlowMaxDataRate_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 11, 1, 14),
    _VdslLineConfDownSlowMaxDataRate_Type()
)
vdslLineConfDownSlowMaxDataRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vdslLineConfDownSlowMaxDataRate.setStatus("current")
if mibBuilder.loadTexts:
    vdslLineConfDownSlowMaxDataRate.setUnits("kbps")


class _VdslLineConfDownSlowMinDataRate_Type(Unsigned32):
    """Custom type vdslLineConfDownSlowMinDataRate based on Unsigned32"""
    defaultValue = 0


_VdslLineConfDownSlowMinDataRate_Object = MibTableColumn
vdslLineConfDownSlowMinDataRate = _VdslLineConfDownSlowMinDataRate_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 11, 1, 15),
    _VdslLineConfDownSlowMinDataRate_Type()
)
vdslLineConfDownSlowMinDataRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vdslLineConfDownSlowMinDataRate.setStatus("current")
if mibBuilder.loadTexts:
    vdslLineConfDownSlowMinDataRate.setUnits("kbps")


class _VdslLineConfUpFastMaxDataRate_Type(Unsigned32):
    """Custom type vdslLineConfUpFastMaxDataRate based on Unsigned32"""
    defaultValue = 0


_VdslLineConfUpFastMaxDataRate_Object = MibTableColumn
vdslLineConfUpFastMaxDataRate = _VdslLineConfUpFastMaxDataRate_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 11, 1, 16),
    _VdslLineConfUpFastMaxDataRate_Type()
)
vdslLineConfUpFastMaxDataRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vdslLineConfUpFastMaxDataRate.setStatus("current")
if mibBuilder.loadTexts:
    vdslLineConfUpFastMaxDataRate.setUnits("kbps")


class _VdslLineConfUpFastMinDataRate_Type(Unsigned32):
    """Custom type vdslLineConfUpFastMinDataRate based on Unsigned32"""
    defaultValue = 0


_VdslLineConfUpFastMinDataRate_Object = MibTableColumn
vdslLineConfUpFastMinDataRate = _VdslLineConfUpFastMinDataRate_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 11, 1, 17),
    _VdslLineConfUpFastMinDataRate_Type()
)
vdslLineConfUpFastMinDataRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vdslLineConfUpFastMinDataRate.setStatus("current")
if mibBuilder.loadTexts:
    vdslLineConfUpFastMinDataRate.setUnits("kbps")


class _VdslLineConfUpSlowMaxDataRate_Type(Unsigned32):
    """Custom type vdslLineConfUpSlowMaxDataRate based on Unsigned32"""
    defaultValue = 0


_VdslLineConfUpSlowMaxDataRate_Object = MibTableColumn
vdslLineConfUpSlowMaxDataRate = _VdslLineConfUpSlowMaxDataRate_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 11, 1, 18),
    _VdslLineConfUpSlowMaxDataRate_Type()
)
vdslLineConfUpSlowMaxDataRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vdslLineConfUpSlowMaxDataRate.setStatus("current")
if mibBuilder.loadTexts:
    vdslLineConfUpSlowMaxDataRate.setUnits("kbps")


class _VdslLineConfUpSlowMinDataRate_Type(Unsigned32):
    """Custom type vdslLineConfUpSlowMinDataRate based on Unsigned32"""
    defaultValue = 0


_VdslLineConfUpSlowMinDataRate_Object = MibTableColumn
vdslLineConfUpSlowMinDataRate = _VdslLineConfUpSlowMinDataRate_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 11, 1, 19),
    _VdslLineConfUpSlowMinDataRate_Type()
)
vdslLineConfUpSlowMinDataRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vdslLineConfUpSlowMinDataRate.setStatus("current")
if mibBuilder.loadTexts:
    vdslLineConfUpSlowMinDataRate.setUnits("kbps")


class _VdslLineConfDownRateRatio_Type(Unsigned32):
    """Custom type vdslLineConfDownRateRatio based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_VdslLineConfDownRateRatio_Type.__name__ = "Unsigned32"
_VdslLineConfDownRateRatio_Object = MibTableColumn
vdslLineConfDownRateRatio = _VdslLineConfDownRateRatio_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 11, 1, 20),
    _VdslLineConfDownRateRatio_Type()
)
vdslLineConfDownRateRatio.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vdslLineConfDownRateRatio.setStatus("current")
if mibBuilder.loadTexts:
    vdslLineConfDownRateRatio.setUnits("percent")


class _VdslLineConfUpRateRatio_Type(Unsigned32):
    """Custom type vdslLineConfUpRateRatio based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_VdslLineConfUpRateRatio_Type.__name__ = "Unsigned32"
_VdslLineConfUpRateRatio_Object = MibTableColumn
vdslLineConfUpRateRatio = _VdslLineConfUpRateRatio_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 11, 1, 21),
    _VdslLineConfUpRateRatio_Type()
)
vdslLineConfUpRateRatio.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vdslLineConfUpRateRatio.setStatus("current")
if mibBuilder.loadTexts:
    vdslLineConfUpRateRatio.setUnits("percent")


class _VdslLineConfDownMaxInterDelay_Type(Unsigned32):
    """Custom type vdslLineConfDownMaxInterDelay based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VdslLineConfDownMaxInterDelay_Type.__name__ = "Unsigned32"
_VdslLineConfDownMaxInterDelay_Object = MibTableColumn
vdslLineConfDownMaxInterDelay = _VdslLineConfDownMaxInterDelay_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 11, 1, 22),
    _VdslLineConfDownMaxInterDelay_Type()
)
vdslLineConfDownMaxInterDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vdslLineConfDownMaxInterDelay.setStatus("current")
if mibBuilder.loadTexts:
    vdslLineConfDownMaxInterDelay.setUnits("milliseconds")


class _VdslLineConfUpMaxInterDelay_Type(Unsigned32):
    """Custom type vdslLineConfUpMaxInterDelay based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VdslLineConfUpMaxInterDelay_Type.__name__ = "Unsigned32"
_VdslLineConfUpMaxInterDelay_Object = MibTableColumn
vdslLineConfUpMaxInterDelay = _VdslLineConfUpMaxInterDelay_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 11, 1, 23),
    _VdslLineConfUpMaxInterDelay_Type()
)
vdslLineConfUpMaxInterDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vdslLineConfUpMaxInterDelay.setStatus("current")
if mibBuilder.loadTexts:
    vdslLineConfUpMaxInterDelay.setUnits("milliseconds")


class _VdslLineConfDownPboControl_Type(Integer32):
    """Custom type vdslLineConfDownPboControl based on Integer32"""
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
        *(("auto", 2),
          ("disabled", 1),
          ("manual", 3))
    )


_VdslLineConfDownPboControl_Type.__name__ = "Integer32"
_VdslLineConfDownPboControl_Object = MibTableColumn
vdslLineConfDownPboControl = _VdslLineConfDownPboControl_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 11, 1, 24),
    _VdslLineConfDownPboControl_Type()
)
vdslLineConfDownPboControl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vdslLineConfDownPboControl.setStatus("current")


class _VdslLineConfUpPboControl_Type(Integer32):
    """Custom type vdslLineConfUpPboControl based on Integer32"""
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
        *(("auto", 2),
          ("disabled", 1),
          ("manual", 3))
    )


_VdslLineConfUpPboControl_Type.__name__ = "Integer32"
_VdslLineConfUpPboControl_Object = MibTableColumn
vdslLineConfUpPboControl = _VdslLineConfUpPboControl_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 11, 1, 25),
    _VdslLineConfUpPboControl_Type()
)
vdslLineConfUpPboControl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vdslLineConfUpPboControl.setStatus("current")


class _VdslLineConfDownPboLevel_Type(Unsigned32):
    """Custom type vdslLineConfDownPboLevel based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 160),
    )


_VdslLineConfDownPboLevel_Type.__name__ = "Unsigned32"
_VdslLineConfDownPboLevel_Object = MibTableColumn
vdslLineConfDownPboLevel = _VdslLineConfDownPboLevel_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 11, 1, 26),
    _VdslLineConfDownPboLevel_Type()
)
vdslLineConfDownPboLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vdslLineConfDownPboLevel.setStatus("current")
if mibBuilder.loadTexts:
    vdslLineConfDownPboLevel.setUnits("0.25dB")


class _VdslLineConfUpPboLevel_Type(Unsigned32):
    """Custom type vdslLineConfUpPboLevel based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 160),
    )


_VdslLineConfUpPboLevel_Type.__name__ = "Unsigned32"
_VdslLineConfUpPboLevel_Object = MibTableColumn
vdslLineConfUpPboLevel = _VdslLineConfUpPboLevel_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 11, 1, 27),
    _VdslLineConfUpPboLevel_Type()
)
vdslLineConfUpPboLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vdslLineConfUpPboLevel.setStatus("current")
if mibBuilder.loadTexts:
    vdslLineConfUpPboLevel.setUnits("0.25dB")


class _VdslLineConfDeploymentScenario_Type(Integer32):
    """Custom type vdslLineConfDeploymentScenario based on Integer32"""
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
        *(("fttCab", 1),
          ("fttEx", 2),
          ("other", 3))
    )


_VdslLineConfDeploymentScenario_Type.__name__ = "Integer32"
_VdslLineConfDeploymentScenario_Object = MibTableColumn
vdslLineConfDeploymentScenario = _VdslLineConfDeploymentScenario_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 11, 1, 28),
    _VdslLineConfDeploymentScenario_Type()
)
vdslLineConfDeploymentScenario.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vdslLineConfDeploymentScenario.setStatus("current")


class _VdslLineConfAdslPresence_Type(Integer32):
    """Custom type vdslLineConfAdslPresence based on Integer32"""
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
        *(("adslOverISDN", 3),
          ("adslOverPots", 2),
          ("none", 1))
    )


_VdslLineConfAdslPresence_Type.__name__ = "Integer32"
_VdslLineConfAdslPresence_Object = MibTableColumn
vdslLineConfAdslPresence = _VdslLineConfAdslPresence_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 11, 1, 29),
    _VdslLineConfAdslPresence_Type()
)
vdslLineConfAdslPresence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vdslLineConfAdslPresence.setStatus("current")


class _VdslLineConfApplicableStandard_Type(Integer32):
    """Custom type vdslLineConfApplicableStandard based on Integer32"""
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
        *(("ansi", 1),
          ("etsi", 2),
          ("itu", 3),
          ("other", 4))
    )


_VdslLineConfApplicableStandard_Type.__name__ = "Integer32"
_VdslLineConfApplicableStandard_Object = MibTableColumn
vdslLineConfApplicableStandard = _VdslLineConfApplicableStandard_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 11, 1, 30),
    _VdslLineConfApplicableStandard_Type()
)
vdslLineConfApplicableStandard.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vdslLineConfApplicableStandard.setStatus("current")


class _VdslLineConfBandPlan_Type(Integer32):
    """Custom type vdslLineConfBandPlan based on Integer32"""
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
        *(("bandPlan997", 1),
          ("bandPlan998", 2),
          ("bandPlanFx", 3),
          ("other", 4))
    )


_VdslLineConfBandPlan_Type.__name__ = "Integer32"
_VdslLineConfBandPlan_Object = MibTableColumn
vdslLineConfBandPlan = _VdslLineConfBandPlan_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 11, 1, 31),
    _VdslLineConfBandPlan_Type()
)
vdslLineConfBandPlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vdslLineConfBandPlan.setStatus("current")


class _VdslLineConfBandPlanFx_Type(Unsigned32):
    """Custom type vdslLineConfBandPlanFx based on Unsigned32"""
    defaultValue = 3750

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3750, 12000),
    )


_VdslLineConfBandPlanFx_Type.__name__ = "Unsigned32"
_VdslLineConfBandPlanFx_Object = MibTableColumn
vdslLineConfBandPlanFx = _VdslLineConfBandPlanFx_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 11, 1, 32),
    _VdslLineConfBandPlanFx_Type()
)
vdslLineConfBandPlanFx.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vdslLineConfBandPlanFx.setStatus("current")
if mibBuilder.loadTexts:
    vdslLineConfBandPlanFx.setUnits("kHz")


class _VdslLineConfBandOptUsage_Type(Integer32):
    """Custom type vdslLineConfBandOptUsage based on Integer32"""
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
        *(("downstream", 3),
          ("unused", 1),
          ("upstream", 2))
    )


_VdslLineConfBandOptUsage_Type.__name__ = "Integer32"
_VdslLineConfBandOptUsage_Object = MibTableColumn
vdslLineConfBandOptUsage = _VdslLineConfBandOptUsage_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 11, 1, 33),
    _VdslLineConfBandOptUsage_Type()
)
vdslLineConfBandOptUsage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vdslLineConfBandOptUsage.setStatus("current")


class _VdslLineConfUpPsdTemplate_Type(Integer32):
    """Custom type vdslLineConfUpPsdTemplate based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("templateMask1", 1),
          ("templateMask2", 2))
    )


_VdslLineConfUpPsdTemplate_Type.__name__ = "Integer32"
_VdslLineConfUpPsdTemplate_Object = MibTableColumn
vdslLineConfUpPsdTemplate = _VdslLineConfUpPsdTemplate_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 11, 1, 34),
    _VdslLineConfUpPsdTemplate_Type()
)
vdslLineConfUpPsdTemplate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vdslLineConfUpPsdTemplate.setStatus("current")


class _VdslLineConfDownPsdTemplate_Type(Integer32):
    """Custom type vdslLineConfDownPsdTemplate based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("templateMask1", 1),
          ("templateMask2", 2))
    )


_VdslLineConfDownPsdTemplate_Type.__name__ = "Integer32"
_VdslLineConfDownPsdTemplate_Object = MibTableColumn
vdslLineConfDownPsdTemplate = _VdslLineConfDownPsdTemplate_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 11, 1, 35),
    _VdslLineConfDownPsdTemplate_Type()
)
vdslLineConfDownPsdTemplate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vdslLineConfDownPsdTemplate.setStatus("current")


class _VdslLineConfHamBandMask_Type(Bits):
    """Custom type vdslLineConfHamBandMask based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("amateurBand160m", 5),
          ("amateurBand30m", 2),
          ("amateurBand40m", 3),
          ("amateurBand80m", 4),
          ("customNotch1", 0),
          ("customNotch2", 1))
    )

_VdslLineConfHamBandMask_Type.__name__ = "Bits"
_VdslLineConfHamBandMask_Object = MibTableColumn
vdslLineConfHamBandMask = _VdslLineConfHamBandMask_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 11, 1, 36),
    _VdslLineConfHamBandMask_Type()
)
vdslLineConfHamBandMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vdslLineConfHamBandMask.setStatus("current")


class _VdslLineConfCustomNotch1Start_Type(Unsigned32):
    """Custom type vdslLineConfCustomNotch1Start based on Unsigned32"""
    defaultValue = 0


_VdslLineConfCustomNotch1Start_Object = MibTableColumn
vdslLineConfCustomNotch1Start = _VdslLineConfCustomNotch1Start_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 11, 1, 37),
    _VdslLineConfCustomNotch1Start_Type()
)
vdslLineConfCustomNotch1Start.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vdslLineConfCustomNotch1Start.setStatus("current")
if mibBuilder.loadTexts:
    vdslLineConfCustomNotch1Start.setUnits("kHz")


class _VdslLineConfCustomNotch1Stop_Type(Unsigned32):
    """Custom type vdslLineConfCustomNotch1Stop based on Unsigned32"""
    defaultValue = 0


_VdslLineConfCustomNotch1Stop_Object = MibTableColumn
vdslLineConfCustomNotch1Stop = _VdslLineConfCustomNotch1Stop_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 11, 1, 38),
    _VdslLineConfCustomNotch1Stop_Type()
)
vdslLineConfCustomNotch1Stop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vdslLineConfCustomNotch1Stop.setStatus("current")
if mibBuilder.loadTexts:
    vdslLineConfCustomNotch1Stop.setUnits("kHz")


class _VdslLineConfCustomNotch2Start_Type(Unsigned32):
    """Custom type vdslLineConfCustomNotch2Start based on Unsigned32"""
    defaultValue = 0


_VdslLineConfCustomNotch2Start_Object = MibTableColumn
vdslLineConfCustomNotch2Start = _VdslLineConfCustomNotch2Start_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 11, 1, 39),
    _VdslLineConfCustomNotch2Start_Type()
)
vdslLineConfCustomNotch2Start.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vdslLineConfCustomNotch2Start.setStatus("current")
if mibBuilder.loadTexts:
    vdslLineConfCustomNotch2Start.setUnits("kHz")


class _VdslLineConfCustomNotch2Stop_Type(Unsigned32):
    """Custom type vdslLineConfCustomNotch2Stop based on Unsigned32"""
    defaultValue = 0


_VdslLineConfCustomNotch2Stop_Object = MibTableColumn
vdslLineConfCustomNotch2Stop = _VdslLineConfCustomNotch2Stop_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 11, 1, 40),
    _VdslLineConfCustomNotch2Stop_Type()
)
vdslLineConfCustomNotch2Stop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vdslLineConfCustomNotch2Stop.setStatus("current")
if mibBuilder.loadTexts:
    vdslLineConfCustomNotch2Stop.setUnits("kHz")


class _VdslLineConfDownTargetSlowBurst_Type(Unsigned32):
    """Custom type vdslLineConfDownTargetSlowBurst based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1275),
    )


_VdslLineConfDownTargetSlowBurst_Type.__name__ = "Unsigned32"
_VdslLineConfDownTargetSlowBurst_Object = MibTableColumn
vdslLineConfDownTargetSlowBurst = _VdslLineConfDownTargetSlowBurst_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 11, 1, 41),
    _VdslLineConfDownTargetSlowBurst_Type()
)
vdslLineConfDownTargetSlowBurst.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vdslLineConfDownTargetSlowBurst.setStatus("current")
if mibBuilder.loadTexts:
    vdslLineConfDownTargetSlowBurst.setUnits("microseconds")


class _VdslLineConfUpTargetSlowBurst_Type(Unsigned32):
    """Custom type vdslLineConfUpTargetSlowBurst based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1275),
    )


_VdslLineConfUpTargetSlowBurst_Type.__name__ = "Unsigned32"
_VdslLineConfUpTargetSlowBurst_Object = MibTableColumn
vdslLineConfUpTargetSlowBurst = _VdslLineConfUpTargetSlowBurst_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 11, 1, 42),
    _VdslLineConfUpTargetSlowBurst_Type()
)
vdslLineConfUpTargetSlowBurst.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vdslLineConfUpTargetSlowBurst.setStatus("current")
if mibBuilder.loadTexts:
    vdslLineConfUpTargetSlowBurst.setUnits("microseconds")


class _VdslLineConfDownMaxFastFec_Type(Unsigned32):
    """Custom type vdslLineConfDownMaxFastFec based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
    )


_VdslLineConfDownMaxFastFec_Type.__name__ = "Unsigned32"
_VdslLineConfDownMaxFastFec_Object = MibTableColumn
vdslLineConfDownMaxFastFec = _VdslLineConfDownMaxFastFec_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 11, 1, 43),
    _VdslLineConfDownMaxFastFec_Type()
)
vdslLineConfDownMaxFastFec.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vdslLineConfDownMaxFastFec.setStatus("current")
if mibBuilder.loadTexts:
    vdslLineConfDownMaxFastFec.setUnits("%")


class _VdslLineConfUpMaxFastFec_Type(Unsigned32):
    """Custom type vdslLineConfUpMaxFastFec based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
    )


_VdslLineConfUpMaxFastFec_Type.__name__ = "Unsigned32"
_VdslLineConfUpMaxFastFec_Object = MibTableColumn
vdslLineConfUpMaxFastFec = _VdslLineConfUpMaxFastFec_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 11, 1, 44),
    _VdslLineConfUpMaxFastFec_Type()
)
vdslLineConfUpMaxFastFec.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vdslLineConfUpMaxFastFec.setStatus("current")
if mibBuilder.loadTexts:
    vdslLineConfUpMaxFastFec.setUnits("%")


class _VdslLineConfLineType_Type(Integer32):
    """Custom type vdslLineConfLineType based on Integer32"""
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
        *(("fastAndInterleaved", 5),
          ("fastOnly", 2),
          ("fastOrInterleaved", 4),
          ("interleavedOnly", 3),
          ("noChannel", 1))
    )


_VdslLineConfLineType_Type.__name__ = "Integer32"
_VdslLineConfLineType_Object = MibTableColumn
vdslLineConfLineType = _VdslLineConfLineType_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 11, 1, 45),
    _VdslLineConfLineType_Type()
)
vdslLineConfLineType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vdslLineConfLineType.setStatus("current")
_VdslLineConfProfRowStatus_Type = RowStatus
_VdslLineConfProfRowStatus_Object = MibTableColumn
vdslLineConfProfRowStatus = _VdslLineConfProfRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 11, 1, 46),
    _VdslLineConfProfRowStatus_Type()
)
vdslLineConfProfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vdslLineConfProfRowStatus.setStatus("current")
_VdslLineAlarmConfProfileTable_Object = MibTable
vdslLineAlarmConfProfileTable = _VdslLineAlarmConfProfileTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 20)
)
if mibBuilder.loadTexts:
    vdslLineAlarmConfProfileTable.setStatus("current")
_VdslLineAlarmConfProfileEntry_Object = MibTableRow
vdslLineAlarmConfProfileEntry = _VdslLineAlarmConfProfileEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 20, 1)
)
vdslLineAlarmConfProfileEntry.setIndexNames(
    (0, "VDSL-LINE-MIB", "vdslLineAlarmConfProfileName"),
)
if mibBuilder.loadTexts:
    vdslLineAlarmConfProfileEntry.setStatus("current")


class _VdslLineAlarmConfProfileName_Type(SnmpAdminString):
    """Custom type vdslLineAlarmConfProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_VdslLineAlarmConfProfileName_Type.__name__ = "SnmpAdminString"
_VdslLineAlarmConfProfileName_Object = MibTableColumn
vdslLineAlarmConfProfileName = _VdslLineAlarmConfProfileName_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 20, 1, 1),
    _VdslLineAlarmConfProfileName_Type()
)
vdslLineAlarmConfProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vdslLineAlarmConfProfileName.setStatus("current")


class _VdslLineAlarmConfThresh15MinLofs_Type(HCPerfIntervalThreshold):
    """Custom type vdslLineAlarmConfThresh15MinLofs based on HCPerfIntervalThreshold"""
    defaultValue = 0


_VdslLineAlarmConfThresh15MinLofs_Object = MibTableColumn
vdslLineAlarmConfThresh15MinLofs = _VdslLineAlarmConfThresh15MinLofs_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 20, 1, 2),
    _VdslLineAlarmConfThresh15MinLofs_Type()
)
vdslLineAlarmConfThresh15MinLofs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vdslLineAlarmConfThresh15MinLofs.setStatus("current")
if mibBuilder.loadTexts:
    vdslLineAlarmConfThresh15MinLofs.setUnits("seconds")


class _VdslLineAlarmConfThresh15MinLoss_Type(HCPerfIntervalThreshold):
    """Custom type vdslLineAlarmConfThresh15MinLoss based on HCPerfIntervalThreshold"""
    defaultValue = 0


_VdslLineAlarmConfThresh15MinLoss_Object = MibTableColumn
vdslLineAlarmConfThresh15MinLoss = _VdslLineAlarmConfThresh15MinLoss_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 20, 1, 3),
    _VdslLineAlarmConfThresh15MinLoss_Type()
)
vdslLineAlarmConfThresh15MinLoss.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vdslLineAlarmConfThresh15MinLoss.setStatus("current")
if mibBuilder.loadTexts:
    vdslLineAlarmConfThresh15MinLoss.setUnits("seconds")


class _VdslLineAlarmConfThresh15MinLprs_Type(HCPerfIntervalThreshold):
    """Custom type vdslLineAlarmConfThresh15MinLprs based on HCPerfIntervalThreshold"""
    defaultValue = 0


_VdslLineAlarmConfThresh15MinLprs_Object = MibTableColumn
vdslLineAlarmConfThresh15MinLprs = _VdslLineAlarmConfThresh15MinLprs_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 20, 1, 4),
    _VdslLineAlarmConfThresh15MinLprs_Type()
)
vdslLineAlarmConfThresh15MinLprs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vdslLineAlarmConfThresh15MinLprs.setStatus("current")
if mibBuilder.loadTexts:
    vdslLineAlarmConfThresh15MinLprs.setUnits("seconds")


class _VdslLineAlarmConfThresh15MinLols_Type(HCPerfIntervalThreshold):
    """Custom type vdslLineAlarmConfThresh15MinLols based on HCPerfIntervalThreshold"""
    defaultValue = 0


_VdslLineAlarmConfThresh15MinLols_Object = MibTableColumn
vdslLineAlarmConfThresh15MinLols = _VdslLineAlarmConfThresh15MinLols_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 20, 1, 5),
    _VdslLineAlarmConfThresh15MinLols_Type()
)
vdslLineAlarmConfThresh15MinLols.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vdslLineAlarmConfThresh15MinLols.setStatus("current")
if mibBuilder.loadTexts:
    vdslLineAlarmConfThresh15MinLols.setUnits("seconds")


class _VdslLineAlarmConfThresh15MinESs_Type(HCPerfIntervalThreshold):
    """Custom type vdslLineAlarmConfThresh15MinESs based on HCPerfIntervalThreshold"""
    defaultValue = 0


_VdslLineAlarmConfThresh15MinESs_Object = MibTableColumn
vdslLineAlarmConfThresh15MinESs = _VdslLineAlarmConfThresh15MinESs_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 20, 1, 6),
    _VdslLineAlarmConfThresh15MinESs_Type()
)
vdslLineAlarmConfThresh15MinESs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vdslLineAlarmConfThresh15MinESs.setStatus("current")
if mibBuilder.loadTexts:
    vdslLineAlarmConfThresh15MinESs.setUnits("seconds")


class _VdslLineAlarmConfThresh15MinSESs_Type(HCPerfIntervalThreshold):
    """Custom type vdslLineAlarmConfThresh15MinSESs based on HCPerfIntervalThreshold"""
    defaultValue = 0


_VdslLineAlarmConfThresh15MinSESs_Object = MibTableColumn
vdslLineAlarmConfThresh15MinSESs = _VdslLineAlarmConfThresh15MinSESs_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 20, 1, 7),
    _VdslLineAlarmConfThresh15MinSESs_Type()
)
vdslLineAlarmConfThresh15MinSESs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vdslLineAlarmConfThresh15MinSESs.setStatus("current")
if mibBuilder.loadTexts:
    vdslLineAlarmConfThresh15MinSESs.setUnits("seconds")


class _VdslLineAlarmConfThresh15MinUASs_Type(HCPerfIntervalThreshold):
    """Custom type vdslLineAlarmConfThresh15MinUASs based on HCPerfIntervalThreshold"""
    defaultValue = 0


_VdslLineAlarmConfThresh15MinUASs_Object = MibTableColumn
vdslLineAlarmConfThresh15MinUASs = _VdslLineAlarmConfThresh15MinUASs_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 20, 1, 8),
    _VdslLineAlarmConfThresh15MinUASs_Type()
)
vdslLineAlarmConfThresh15MinUASs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vdslLineAlarmConfThresh15MinUASs.setStatus("current")
if mibBuilder.loadTexts:
    vdslLineAlarmConfThresh15MinUASs.setUnits("seconds")


class _VdslLineAlarmConfInitFailure_Type(TruthValue):
    """Custom type vdslLineAlarmConfInitFailure based on TruthValue"""


_VdslLineAlarmConfInitFailure_Object = MibTableColumn
vdslLineAlarmConfInitFailure = _VdslLineAlarmConfInitFailure_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 20, 1, 9),
    _VdslLineAlarmConfInitFailure_Type()
)
vdslLineAlarmConfInitFailure.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vdslLineAlarmConfInitFailure.setStatus("current")
_VdslLineAlarmConfProfRowStatus_Type = RowStatus
_VdslLineAlarmConfProfRowStatus_Object = MibTableColumn
vdslLineAlarmConfProfRowStatus = _VdslLineAlarmConfProfRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 1, 20, 1, 10),
    _VdslLineAlarmConfProfRowStatus_Type()
)
vdslLineAlarmConfProfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vdslLineAlarmConfProfRowStatus.setStatus("current")
_VdslConformance_ObjectIdentity = ObjectIdentity
vdslConformance = _VdslConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 3)
)
_VdslGroups_ObjectIdentity = ObjectIdentity
vdslGroups = _VdslGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 3, 1)
)
_VdslCompliances_ObjectIdentity = ObjectIdentity
vdslCompliances = _VdslCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 3, 2)
)

# Managed Objects groups

vdslGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 3, 1, 1)
)
vdslGroup.setObjects(
      *(("VDSL-LINE-MIB", "vdslLineCoding"),
        ("VDSL-LINE-MIB", "vdslLineType"),
        ("VDSL-LINE-MIB", "vdslLineConfProfile"),
        ("VDSL-LINE-MIB", "vdslLineAlarmConfProfile"),
        ("VDSL-LINE-MIB", "vdslPhysInvSerialNumber"),
        ("VDSL-LINE-MIB", "vdslPhysInvVendorID"),
        ("VDSL-LINE-MIB", "vdslPhysInvVersionNumber"),
        ("VDSL-LINE-MIB", "vdslPhysCurrSnrMgn"),
        ("VDSL-LINE-MIB", "vdslPhysCurrAtn"),
        ("VDSL-LINE-MIB", "vdslPhysCurrStatus"),
        ("VDSL-LINE-MIB", "vdslPhysCurrOutputPwr"),
        ("VDSL-LINE-MIB", "vdslPhysCurrAttainableRate"),
        ("VDSL-LINE-MIB", "vdslPhysCurrLineRate"),
        ("VDSL-LINE-MIB", "vdslChanInterleaveDelay"),
        ("VDSL-LINE-MIB", "vdslChanCrcBlockLength"),
        ("VDSL-LINE-MIB", "vdslChanCurrTxRate"),
        ("VDSL-LINE-MIB", "vdslChanCurrTxSlowBurstProtect"),
        ("VDSL-LINE-MIB", "vdslChanCurrTxFastFec"),
        ("VDSL-LINE-MIB", "vdslPerfDataValidIntervals"),
        ("VDSL-LINE-MIB", "vdslPerfDataInvalidIntervals"),
        ("VDSL-LINE-MIB", "vdslPerfDataLofs"),
        ("VDSL-LINE-MIB", "vdslPerfDataLoss"),
        ("VDSL-LINE-MIB", "vdslPerfDataLprs"),
        ("VDSL-LINE-MIB", "vdslPerfDataLols"),
        ("VDSL-LINE-MIB", "vdslPerfDataESs"),
        ("VDSL-LINE-MIB", "vdslPerfDataSESs"),
        ("VDSL-LINE-MIB", "vdslPerfDataUASs"),
        ("VDSL-LINE-MIB", "vdslPerfDataInits"),
        ("VDSL-LINE-MIB", "vdslPerfDataCurr15MinTimeElapsed"),
        ("VDSL-LINE-MIB", "vdslPerfDataCurr15MinLofs"),
        ("VDSL-LINE-MIB", "vdslPerfDataCurr15MinLoss"),
        ("VDSL-LINE-MIB", "vdslPerfDataCurr15MinLprs"),
        ("VDSL-LINE-MIB", "vdslPerfDataCurr15MinLols"),
        ("VDSL-LINE-MIB", "vdslPerfDataCurr15MinESs"),
        ("VDSL-LINE-MIB", "vdslPerfDataCurr15MinSESs"),
        ("VDSL-LINE-MIB", "vdslPerfDataCurr15MinUASs"),
        ("VDSL-LINE-MIB", "vdslPerfDataCurr15MinInits"),
        ("VDSL-LINE-MIB", "vdslPerfData1DayValidIntervals"),
        ("VDSL-LINE-MIB", "vdslPerfData1DayInvalidIntervals"),
        ("VDSL-LINE-MIB", "vdslPerfDataCurr1DayTimeElapsed"),
        ("VDSL-LINE-MIB", "vdslPerfDataCurr1DayLofs"),
        ("VDSL-LINE-MIB", "vdslPerfDataCurr1DayLoss"),
        ("VDSL-LINE-MIB", "vdslPerfDataCurr1DayLprs"),
        ("VDSL-LINE-MIB", "vdslPerfDataCurr1DayLols"),
        ("VDSL-LINE-MIB", "vdslPerfDataCurr1DayESs"),
        ("VDSL-LINE-MIB", "vdslPerfDataCurr1DaySESs"),
        ("VDSL-LINE-MIB", "vdslPerfDataCurr1DayUASs"),
        ("VDSL-LINE-MIB", "vdslPerfDataCurr1DayInits"),
        ("VDSL-LINE-MIB", "vdslPerfIntervalLofs"),
        ("VDSL-LINE-MIB", "vdslPerfIntervalLoss"),
        ("VDSL-LINE-MIB", "vdslPerfIntervalLprs"),
        ("VDSL-LINE-MIB", "vdslPerfIntervalLols"),
        ("VDSL-LINE-MIB", "vdslPerfIntervalESs"),
        ("VDSL-LINE-MIB", "vdslPerfIntervalSESs"),
        ("VDSL-LINE-MIB", "vdslPerfIntervalUASs"),
        ("VDSL-LINE-MIB", "vdslPerfIntervalInits"),
        ("VDSL-LINE-MIB", "vdslPerf1DayIntervalMoniSecs"),
        ("VDSL-LINE-MIB", "vdslPerf1DayIntervalLofs"),
        ("VDSL-LINE-MIB", "vdslPerf1DayIntervalLoss"),
        ("VDSL-LINE-MIB", "vdslPerf1DayIntervalLprs"),
        ("VDSL-LINE-MIB", "vdslPerf1DayIntervalLols"),
        ("VDSL-LINE-MIB", "vdslPerf1DayIntervalESs"),
        ("VDSL-LINE-MIB", "vdslPerf1DayIntervalSESs"),
        ("VDSL-LINE-MIB", "vdslPerf1DayIntervalUASs"),
        ("VDSL-LINE-MIB", "vdslPerf1DayIntervalInits"),
        ("VDSL-LINE-MIB", "vdslChanValidIntervals"),
        ("VDSL-LINE-MIB", "vdslChanInvalidIntervals"),
        ("VDSL-LINE-MIB", "vdslChanFixedOctets"),
        ("VDSL-LINE-MIB", "vdslChanBadBlks"),
        ("VDSL-LINE-MIB", "vdslChanCurr15MinTimeElapsed"),
        ("VDSL-LINE-MIB", "vdslChanCurr15MinFixedOctets"),
        ("VDSL-LINE-MIB", "vdslChanCurr15MinBadBlks"),
        ("VDSL-LINE-MIB", "vdslChan1DayValidIntervals"),
        ("VDSL-LINE-MIB", "vdslChan1DayInvalidIntervals"),
        ("VDSL-LINE-MIB", "vdslChanCurr1DayTimeElapsed"),
        ("VDSL-LINE-MIB", "vdslChanCurr1DayFixedOctets"),
        ("VDSL-LINE-MIB", "vdslChanCurr1DayBadBlks"),
        ("VDSL-LINE-MIB", "vdslChanIntervalFixedOctets"),
        ("VDSL-LINE-MIB", "vdslChanIntervalBadBlks"),
        ("VDSL-LINE-MIB", "vdslChan1DayIntervalMoniSecs"),
        ("VDSL-LINE-MIB", "vdslChan1DayIntervalFixedOctets"),
        ("VDSL-LINE-MIB", "vdslChan1DayIntervalBadBlks"),
        ("VDSL-LINE-MIB", "vdslLineConfDownRateMode"),
        ("VDSL-LINE-MIB", "vdslLineConfUpRateMode"),
        ("VDSL-LINE-MIB", "vdslLineConfDownMaxPwr"),
        ("VDSL-LINE-MIB", "vdslLineConfUpMaxPwr"),
        ("VDSL-LINE-MIB", "vdslLineConfDownMaxSnrMgn"),
        ("VDSL-LINE-MIB", "vdslLineConfDownMinSnrMgn"),
        ("VDSL-LINE-MIB", "vdslLineConfDownTargetSnrMgn"),
        ("VDSL-LINE-MIB", "vdslLineConfUpMaxSnrMgn"),
        ("VDSL-LINE-MIB", "vdslLineConfUpMinSnrMgn"),
        ("VDSL-LINE-MIB", "vdslLineConfUpTargetSnrMgn"),
        ("VDSL-LINE-MIB", "vdslLineConfDownFastMaxDataRate"),
        ("VDSL-LINE-MIB", "vdslLineConfDownFastMinDataRate"),
        ("VDSL-LINE-MIB", "vdslLineConfDownSlowMaxDataRate"),
        ("VDSL-LINE-MIB", "vdslLineConfDownSlowMinDataRate"),
        ("VDSL-LINE-MIB", "vdslLineConfUpFastMaxDataRate"),
        ("VDSL-LINE-MIB", "vdslLineConfUpFastMinDataRate"),
        ("VDSL-LINE-MIB", "vdslLineConfUpSlowMaxDataRate"),
        ("VDSL-LINE-MIB", "vdslLineConfUpSlowMinDataRate"),
        ("VDSL-LINE-MIB", "vdslLineConfDownRateRatio"),
        ("VDSL-LINE-MIB", "vdslLineConfUpRateRatio"),
        ("VDSL-LINE-MIB", "vdslLineConfDownMaxInterDelay"),
        ("VDSL-LINE-MIB", "vdslLineConfUpMaxInterDelay"),
        ("VDSL-LINE-MIB", "vdslLineConfDownPboControl"),
        ("VDSL-LINE-MIB", "vdslLineConfUpPboControl"),
        ("VDSL-LINE-MIB", "vdslLineConfDownPboLevel"),
        ("VDSL-LINE-MIB", "vdslLineConfUpPboLevel"),
        ("VDSL-LINE-MIB", "vdslLineConfDeploymentScenario"),
        ("VDSL-LINE-MIB", "vdslLineConfAdslPresence"),
        ("VDSL-LINE-MIB", "vdslLineConfApplicableStandard"),
        ("VDSL-LINE-MIB", "vdslLineConfBandPlan"),
        ("VDSL-LINE-MIB", "vdslLineConfBandPlanFx"),
        ("VDSL-LINE-MIB", "vdslLineConfBandOptUsage"),
        ("VDSL-LINE-MIB", "vdslLineConfUpPsdTemplate"),
        ("VDSL-LINE-MIB", "vdslLineConfDownPsdTemplate"),
        ("VDSL-LINE-MIB", "vdslLineConfHamBandMask"),
        ("VDSL-LINE-MIB", "vdslLineConfCustomNotch1Start"),
        ("VDSL-LINE-MIB", "vdslLineConfCustomNotch1Stop"),
        ("VDSL-LINE-MIB", "vdslLineConfCustomNotch2Start"),
        ("VDSL-LINE-MIB", "vdslLineConfCustomNotch2Stop"),
        ("VDSL-LINE-MIB", "vdslLineConfDownTargetSlowBurst"),
        ("VDSL-LINE-MIB", "vdslLineConfUpTargetSlowBurst"),
        ("VDSL-LINE-MIB", "vdslLineConfDownMaxFastFec"),
        ("VDSL-LINE-MIB", "vdslLineConfUpMaxFastFec"),
        ("VDSL-LINE-MIB", "vdslLineConfLineType"),
        ("VDSL-LINE-MIB", "vdslLineConfProfRowStatus"),
        ("VDSL-LINE-MIB", "vdslLineAlarmConfThresh15MinLofs"),
        ("VDSL-LINE-MIB", "vdslLineAlarmConfThresh15MinLoss"),
        ("VDSL-LINE-MIB", "vdslLineAlarmConfThresh15MinLprs"),
        ("VDSL-LINE-MIB", "vdslLineAlarmConfThresh15MinLols"),
        ("VDSL-LINE-MIB", "vdslLineAlarmConfThresh15MinESs"),
        ("VDSL-LINE-MIB", "vdslLineAlarmConfThresh15MinSESs"),
        ("VDSL-LINE-MIB", "vdslLineAlarmConfThresh15MinUASs"),
        ("VDSL-LINE-MIB", "vdslLineAlarmConfInitFailure"),
        ("VDSL-LINE-MIB", "vdslLineAlarmConfProfRowStatus"))
)
if mibBuilder.loadTexts:
    vdslGroup.setStatus("current")


# Notification objects

vdslPerfLofsThreshNotification = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 0, 1)
)
vdslPerfLofsThreshNotification.setObjects(
    ("VDSL-LINE-MIB", "vdslPerfDataCurr15MinLofs")
)
if mibBuilder.loadTexts:
    vdslPerfLofsThreshNotification.setStatus(
        "current"
    )

vdslPerfLossThreshNotification = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 0, 2)
)
vdslPerfLossThreshNotification.setObjects(
    ("VDSL-LINE-MIB", "vdslPerfDataCurr15MinLoss")
)
if mibBuilder.loadTexts:
    vdslPerfLossThreshNotification.setStatus(
        "current"
    )

vdslPerfLprsThreshNotification = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 0, 3)
)
vdslPerfLprsThreshNotification.setObjects(
    ("VDSL-LINE-MIB", "vdslPerfDataCurr15MinLprs")
)
if mibBuilder.loadTexts:
    vdslPerfLprsThreshNotification.setStatus(
        "current"
    )

vdslPerfLolsThreshNotification = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 0, 4)
)
vdslPerfLolsThreshNotification.setObjects(
    ("VDSL-LINE-MIB", "vdslPerfDataCurr15MinLols")
)
if mibBuilder.loadTexts:
    vdslPerfLolsThreshNotification.setStatus(
        "current"
    )

vdslPerfESsThreshNotification = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 0, 5)
)
vdslPerfESsThreshNotification.setObjects(
    ("VDSL-LINE-MIB", "vdslPerfDataCurr15MinESs")
)
if mibBuilder.loadTexts:
    vdslPerfESsThreshNotification.setStatus(
        "current"
    )

vdslPerfSESsThreshNotification = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 0, 6)
)
vdslPerfSESsThreshNotification.setObjects(
    ("VDSL-LINE-MIB", "vdslPerfDataCurr15MinSESs")
)
if mibBuilder.loadTexts:
    vdslPerfSESsThreshNotification.setStatus(
        "current"
    )

vdslPerfUASsThreshNotification = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 0, 7)
)
vdslPerfUASsThreshNotification.setObjects(
    ("VDSL-LINE-MIB", "vdslPerfDataCurr15MinUASs")
)
if mibBuilder.loadTexts:
    vdslPerfUASsThreshNotification.setStatus(
        "current"
    )

vdslDownMaxSnrMgnNotification = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 0, 8)
)
vdslDownMaxSnrMgnNotification.setObjects(
    ("VDSL-LINE-MIB", "vdslPhysCurrSnrMgn")
)
if mibBuilder.loadTexts:
    vdslDownMaxSnrMgnNotification.setStatus(
        "current"
    )

vdslDownMinSnrMgnNotification = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 0, 9)
)
vdslDownMinSnrMgnNotification.setObjects(
    ("VDSL-LINE-MIB", "vdslPhysCurrSnrMgn")
)
if mibBuilder.loadTexts:
    vdslDownMinSnrMgnNotification.setStatus(
        "current"
    )

vdslUpMaxSnrMgnNotification = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 0, 10)
)
vdslUpMaxSnrMgnNotification.setObjects(
    ("VDSL-LINE-MIB", "vdslPhysCurrSnrMgn")
)
if mibBuilder.loadTexts:
    vdslUpMaxSnrMgnNotification.setStatus(
        "current"
    )

vdslUpMinSnrMgnNotification = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 0, 11)
)
vdslUpMinSnrMgnNotification.setObjects(
    ("VDSL-LINE-MIB", "vdslPhysCurrSnrMgn")
)
if mibBuilder.loadTexts:
    vdslUpMinSnrMgnNotification.setStatus(
        "current"
    )

vdslInitFailureNotification = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 0, 12)
)
vdslInitFailureNotification.setObjects(
    ("VDSL-LINE-MIB", "vdslPhysCurrStatus")
)
if mibBuilder.loadTexts:
    vdslInitFailureNotification.setStatus(
        "current"
    )


# Notifications groups

vdslNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 3, 1, 2)
)
vdslNotificationGroup.setObjects(
      *(("VDSL-LINE-MIB", "vdslPerfLofsThreshNotification"),
        ("VDSL-LINE-MIB", "vdslPerfLossThreshNotification"),
        ("VDSL-LINE-MIB", "vdslPerfLprsThreshNotification"),
        ("VDSL-LINE-MIB", "vdslPerfLolsThreshNotification"),
        ("VDSL-LINE-MIB", "vdslPerfESsThreshNotification"),
        ("VDSL-LINE-MIB", "vdslPerfSESsThreshNotification"),
        ("VDSL-LINE-MIB", "vdslPerfUASsThreshNotification"),
        ("VDSL-LINE-MIB", "vdslDownMaxSnrMgnNotification"),
        ("VDSL-LINE-MIB", "vdslDownMinSnrMgnNotification"),
        ("VDSL-LINE-MIB", "vdslUpMaxSnrMgnNotification"),
        ("VDSL-LINE-MIB", "vdslUpMinSnrMgnNotification"),
        ("VDSL-LINE-MIB", "vdslInitFailureNotification"))
)
if mibBuilder.loadTexts:
    vdslNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

vdslLineMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 10, 97, 1, 3, 2, 1)
)
if mibBuilder.loadTexts:
    vdslLineMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VDSL-LINE-MIB",
    **{"VdslLineCodingType": VdslLineCodingType,
       "VdslLineEntity": VdslLineEntity,
       "vdslMIB": vdslMIB,
       "vdslLineMib": vdslLineMib,
       "vdslNotifications": vdslNotifications,
       "vdslPerfLofsThreshNotification": vdslPerfLofsThreshNotification,
       "vdslPerfLossThreshNotification": vdslPerfLossThreshNotification,
       "vdslPerfLprsThreshNotification": vdslPerfLprsThreshNotification,
       "vdslPerfLolsThreshNotification": vdslPerfLolsThreshNotification,
       "vdslPerfESsThreshNotification": vdslPerfESsThreshNotification,
       "vdslPerfSESsThreshNotification": vdslPerfSESsThreshNotification,
       "vdslPerfUASsThreshNotification": vdslPerfUASsThreshNotification,
       "vdslDownMaxSnrMgnNotification": vdslDownMaxSnrMgnNotification,
       "vdslDownMinSnrMgnNotification": vdslDownMinSnrMgnNotification,
       "vdslUpMaxSnrMgnNotification": vdslUpMaxSnrMgnNotification,
       "vdslUpMinSnrMgnNotification": vdslUpMinSnrMgnNotification,
       "vdslInitFailureNotification": vdslInitFailureNotification,
       "vdslMibObjects": vdslMibObjects,
       "vdslLineTable": vdslLineTable,
       "vdslLineEntry": vdslLineEntry,
       "vdslLineCoding": vdslLineCoding,
       "vdslLineType": vdslLineType,
       "vdslLineConfProfile": vdslLineConfProfile,
       "vdslLineAlarmConfProfile": vdslLineAlarmConfProfile,
       "vdslPhysTable": vdslPhysTable,
       "vdslPhysEntry": vdslPhysEntry,
       "vdslPhysSide": vdslPhysSide,
       "vdslPhysInvSerialNumber": vdslPhysInvSerialNumber,
       "vdslPhysInvVendorID": vdslPhysInvVendorID,
       "vdslPhysInvVersionNumber": vdslPhysInvVersionNumber,
       "vdslPhysCurrSnrMgn": vdslPhysCurrSnrMgn,
       "vdslPhysCurrAtn": vdslPhysCurrAtn,
       "vdslPhysCurrStatus": vdslPhysCurrStatus,
       "vdslPhysCurrOutputPwr": vdslPhysCurrOutputPwr,
       "vdslPhysCurrAttainableRate": vdslPhysCurrAttainableRate,
       "vdslPhysCurrLineRate": vdslPhysCurrLineRate,
       "vdslChanTable": vdslChanTable,
       "vdslChanEntry": vdslChanEntry,
       "vdslChanInterleaveDelay": vdslChanInterleaveDelay,
       "vdslChanCrcBlockLength": vdslChanCrcBlockLength,
       "vdslChanCurrTxRate": vdslChanCurrTxRate,
       "vdslChanCurrTxSlowBurstProtect": vdslChanCurrTxSlowBurstProtect,
       "vdslChanCurrTxFastFec": vdslChanCurrTxFastFec,
       "vdslPerfDataTable": vdslPerfDataTable,
       "vdslPerfDataEntry": vdslPerfDataEntry,
       "vdslPerfDataValidIntervals": vdslPerfDataValidIntervals,
       "vdslPerfDataInvalidIntervals": vdslPerfDataInvalidIntervals,
       "vdslPerfDataLofs": vdslPerfDataLofs,
       "vdslPerfDataLoss": vdslPerfDataLoss,
       "vdslPerfDataLprs": vdslPerfDataLprs,
       "vdslPerfDataLols": vdslPerfDataLols,
       "vdslPerfDataESs": vdslPerfDataESs,
       "vdslPerfDataSESs": vdslPerfDataSESs,
       "vdslPerfDataUASs": vdslPerfDataUASs,
       "vdslPerfDataInits": vdslPerfDataInits,
       "vdslPerfDataCurr15MinTimeElapsed": vdslPerfDataCurr15MinTimeElapsed,
       "vdslPerfDataCurr15MinLofs": vdslPerfDataCurr15MinLofs,
       "vdslPerfDataCurr15MinLoss": vdslPerfDataCurr15MinLoss,
       "vdslPerfDataCurr15MinLprs": vdslPerfDataCurr15MinLprs,
       "vdslPerfDataCurr15MinLols": vdslPerfDataCurr15MinLols,
       "vdslPerfDataCurr15MinESs": vdslPerfDataCurr15MinESs,
       "vdslPerfDataCurr15MinSESs": vdslPerfDataCurr15MinSESs,
       "vdslPerfDataCurr15MinUASs": vdslPerfDataCurr15MinUASs,
       "vdslPerfDataCurr15MinInits": vdslPerfDataCurr15MinInits,
       "vdslPerfData1DayValidIntervals": vdslPerfData1DayValidIntervals,
       "vdslPerfData1DayInvalidIntervals": vdslPerfData1DayInvalidIntervals,
       "vdslPerfDataCurr1DayTimeElapsed": vdslPerfDataCurr1DayTimeElapsed,
       "vdslPerfDataCurr1DayLofs": vdslPerfDataCurr1DayLofs,
       "vdslPerfDataCurr1DayLoss": vdslPerfDataCurr1DayLoss,
       "vdslPerfDataCurr1DayLprs": vdslPerfDataCurr1DayLprs,
       "vdslPerfDataCurr1DayLols": vdslPerfDataCurr1DayLols,
       "vdslPerfDataCurr1DayESs": vdslPerfDataCurr1DayESs,
       "vdslPerfDataCurr1DaySESs": vdslPerfDataCurr1DaySESs,
       "vdslPerfDataCurr1DayUASs": vdslPerfDataCurr1DayUASs,
       "vdslPerfDataCurr1DayInits": vdslPerfDataCurr1DayInits,
       "vdslPerfIntervalTable": vdslPerfIntervalTable,
       "vdslPerfIntervalEntry": vdslPerfIntervalEntry,
       "vdslPerfIntervalNumber": vdslPerfIntervalNumber,
       "vdslPerfIntervalLofs": vdslPerfIntervalLofs,
       "vdslPerfIntervalLoss": vdslPerfIntervalLoss,
       "vdslPerfIntervalLprs": vdslPerfIntervalLprs,
       "vdslPerfIntervalLols": vdslPerfIntervalLols,
       "vdslPerfIntervalESs": vdslPerfIntervalESs,
       "vdslPerfIntervalSESs": vdslPerfIntervalSESs,
       "vdslPerfIntervalUASs": vdslPerfIntervalUASs,
       "vdslPerfIntervalInits": vdslPerfIntervalInits,
       "vdslPerf1DayIntervalTable": vdslPerf1DayIntervalTable,
       "vdslPerf1DayIntervalEntry": vdslPerf1DayIntervalEntry,
       "vdslPerf1DayIntervalNumber": vdslPerf1DayIntervalNumber,
       "vdslPerf1DayIntervalMoniSecs": vdslPerf1DayIntervalMoniSecs,
       "vdslPerf1DayIntervalLofs": vdslPerf1DayIntervalLofs,
       "vdslPerf1DayIntervalLoss": vdslPerf1DayIntervalLoss,
       "vdslPerf1DayIntervalLprs": vdslPerf1DayIntervalLprs,
       "vdslPerf1DayIntervalLols": vdslPerf1DayIntervalLols,
       "vdslPerf1DayIntervalESs": vdslPerf1DayIntervalESs,
       "vdslPerf1DayIntervalSESs": vdslPerf1DayIntervalSESs,
       "vdslPerf1DayIntervalUASs": vdslPerf1DayIntervalUASs,
       "vdslPerf1DayIntervalInits": vdslPerf1DayIntervalInits,
       "vdslChanPerfDataTable": vdslChanPerfDataTable,
       "vdslChanPerfDataEntry": vdslChanPerfDataEntry,
       "vdslChanValidIntervals": vdslChanValidIntervals,
       "vdslChanInvalidIntervals": vdslChanInvalidIntervals,
       "vdslChanFixedOctets": vdslChanFixedOctets,
       "vdslChanBadBlks": vdslChanBadBlks,
       "vdslChanCurr15MinTimeElapsed": vdslChanCurr15MinTimeElapsed,
       "vdslChanCurr15MinFixedOctets": vdslChanCurr15MinFixedOctets,
       "vdslChanCurr15MinBadBlks": vdslChanCurr15MinBadBlks,
       "vdslChan1DayValidIntervals": vdslChan1DayValidIntervals,
       "vdslChan1DayInvalidIntervals": vdslChan1DayInvalidIntervals,
       "vdslChanCurr1DayTimeElapsed": vdslChanCurr1DayTimeElapsed,
       "vdslChanCurr1DayFixedOctets": vdslChanCurr1DayFixedOctets,
       "vdslChanCurr1DayBadBlks": vdslChanCurr1DayBadBlks,
       "vdslChanIntervalTable": vdslChanIntervalTable,
       "vdslChanIntervalEntry": vdslChanIntervalEntry,
       "vdslChanIntervalNumber": vdslChanIntervalNumber,
       "vdslChanIntervalFixedOctets": vdslChanIntervalFixedOctets,
       "vdslChanIntervalBadBlks": vdslChanIntervalBadBlks,
       "vdslChan1DayIntervalTable": vdslChan1DayIntervalTable,
       "vdslChan1DayIntervalEntry": vdslChan1DayIntervalEntry,
       "vdslChan1DayIntervalNumber": vdslChan1DayIntervalNumber,
       "vdslChan1DayIntervalMoniSecs": vdslChan1DayIntervalMoniSecs,
       "vdslChan1DayIntervalFixedOctets": vdslChan1DayIntervalFixedOctets,
       "vdslChan1DayIntervalBadBlks": vdslChan1DayIntervalBadBlks,
       "vdslLineConfProfileTable": vdslLineConfProfileTable,
       "vdslLineConfProfileEntry": vdslLineConfProfileEntry,
       "vdslLineConfProfileName": vdslLineConfProfileName,
       "vdslLineConfDownRateMode": vdslLineConfDownRateMode,
       "vdslLineConfUpRateMode": vdslLineConfUpRateMode,
       "vdslLineConfDownMaxPwr": vdslLineConfDownMaxPwr,
       "vdslLineConfUpMaxPwr": vdslLineConfUpMaxPwr,
       "vdslLineConfDownMaxSnrMgn": vdslLineConfDownMaxSnrMgn,
       "vdslLineConfDownMinSnrMgn": vdslLineConfDownMinSnrMgn,
       "vdslLineConfDownTargetSnrMgn": vdslLineConfDownTargetSnrMgn,
       "vdslLineConfUpMaxSnrMgn": vdslLineConfUpMaxSnrMgn,
       "vdslLineConfUpMinSnrMgn": vdslLineConfUpMinSnrMgn,
       "vdslLineConfUpTargetSnrMgn": vdslLineConfUpTargetSnrMgn,
       "vdslLineConfDownFastMaxDataRate": vdslLineConfDownFastMaxDataRate,
       "vdslLineConfDownFastMinDataRate": vdslLineConfDownFastMinDataRate,
       "vdslLineConfDownSlowMaxDataRate": vdslLineConfDownSlowMaxDataRate,
       "vdslLineConfDownSlowMinDataRate": vdslLineConfDownSlowMinDataRate,
       "vdslLineConfUpFastMaxDataRate": vdslLineConfUpFastMaxDataRate,
       "vdslLineConfUpFastMinDataRate": vdslLineConfUpFastMinDataRate,
       "vdslLineConfUpSlowMaxDataRate": vdslLineConfUpSlowMaxDataRate,
       "vdslLineConfUpSlowMinDataRate": vdslLineConfUpSlowMinDataRate,
       "vdslLineConfDownRateRatio": vdslLineConfDownRateRatio,
       "vdslLineConfUpRateRatio": vdslLineConfUpRateRatio,
       "vdslLineConfDownMaxInterDelay": vdslLineConfDownMaxInterDelay,
       "vdslLineConfUpMaxInterDelay": vdslLineConfUpMaxInterDelay,
       "vdslLineConfDownPboControl": vdslLineConfDownPboControl,
       "vdslLineConfUpPboControl": vdslLineConfUpPboControl,
       "vdslLineConfDownPboLevel": vdslLineConfDownPboLevel,
       "vdslLineConfUpPboLevel": vdslLineConfUpPboLevel,
       "vdslLineConfDeploymentScenario": vdslLineConfDeploymentScenario,
       "vdslLineConfAdslPresence": vdslLineConfAdslPresence,
       "vdslLineConfApplicableStandard": vdslLineConfApplicableStandard,
       "vdslLineConfBandPlan": vdslLineConfBandPlan,
       "vdslLineConfBandPlanFx": vdslLineConfBandPlanFx,
       "vdslLineConfBandOptUsage": vdslLineConfBandOptUsage,
       "vdslLineConfUpPsdTemplate": vdslLineConfUpPsdTemplate,
       "vdslLineConfDownPsdTemplate": vdslLineConfDownPsdTemplate,
       "vdslLineConfHamBandMask": vdslLineConfHamBandMask,
       "vdslLineConfCustomNotch1Start": vdslLineConfCustomNotch1Start,
       "vdslLineConfCustomNotch1Stop": vdslLineConfCustomNotch1Stop,
       "vdslLineConfCustomNotch2Start": vdslLineConfCustomNotch2Start,
       "vdslLineConfCustomNotch2Stop": vdslLineConfCustomNotch2Stop,
       "vdslLineConfDownTargetSlowBurst": vdslLineConfDownTargetSlowBurst,
       "vdslLineConfUpTargetSlowBurst": vdslLineConfUpTargetSlowBurst,
       "vdslLineConfDownMaxFastFec": vdslLineConfDownMaxFastFec,
       "vdslLineConfUpMaxFastFec": vdslLineConfUpMaxFastFec,
       "vdslLineConfLineType": vdslLineConfLineType,
       "vdslLineConfProfRowStatus": vdslLineConfProfRowStatus,
       "vdslLineAlarmConfProfileTable": vdslLineAlarmConfProfileTable,
       "vdslLineAlarmConfProfileEntry": vdslLineAlarmConfProfileEntry,
       "vdslLineAlarmConfProfileName": vdslLineAlarmConfProfileName,
       "vdslLineAlarmConfThresh15MinLofs": vdslLineAlarmConfThresh15MinLofs,
       "vdslLineAlarmConfThresh15MinLoss": vdslLineAlarmConfThresh15MinLoss,
       "vdslLineAlarmConfThresh15MinLprs": vdslLineAlarmConfThresh15MinLprs,
       "vdslLineAlarmConfThresh15MinLols": vdslLineAlarmConfThresh15MinLols,
       "vdslLineAlarmConfThresh15MinESs": vdslLineAlarmConfThresh15MinESs,
       "vdslLineAlarmConfThresh15MinSESs": vdslLineAlarmConfThresh15MinSESs,
       "vdslLineAlarmConfThresh15MinUASs": vdslLineAlarmConfThresh15MinUASs,
       "vdslLineAlarmConfInitFailure": vdslLineAlarmConfInitFailure,
       "vdslLineAlarmConfProfRowStatus": vdslLineAlarmConfProfRowStatus,
       "vdslConformance": vdslConformance,
       "vdslGroups": vdslGroups,
       "vdslGroup": vdslGroup,
       "vdslNotificationGroup": vdslNotificationGroup,
       "vdslCompliances": vdslCompliances,
       "vdslLineMibCompliance": vdslLineMibCompliance}
)
