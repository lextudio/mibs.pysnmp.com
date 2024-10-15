# SNMP MIB module (CISCO-IETF-VDSL-LINE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-IETF-VDSL-LINE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:02:03 2024
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

(ciscoExperiment,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoExperiment")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoIetfVdslMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 87)
)
ciscoIetfVdslMIB.setRevisions(
        ("2002-04-18 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CVdslLineCodingType(Integer32, TextualConvention):
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



class CVdslLineEntity(Integer32, TextualConvention):
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

_CvdslLineMib_ObjectIdentity = ObjectIdentity
cvdslLineMib = _CvdslLineMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 87, 1)
)
_CvdslNotifications_ObjectIdentity = ObjectIdentity
cvdslNotifications = _CvdslNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 0)
)
_CvdslMibObjects_ObjectIdentity = ObjectIdentity
cvdslMibObjects = _CvdslMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1)
)
_CvdslLineTable_Object = MibTable
cvdslLineTable = _CvdslLineTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cvdslLineTable.setStatus("current")
_CvdslLineEntry_Object = MibTableRow
cvdslLineEntry = _CvdslLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 1, 1)
)
cvdslLineEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cvdslLineEntry.setStatus("current")
_CvdslLineCoding_Type = CVdslLineCodingType
_CvdslLineCoding_Object = MibTableColumn
cvdslLineCoding = _CvdslLineCoding_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 1, 1, 1),
    _CvdslLineCoding_Type()
)
cvdslLineCoding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvdslLineCoding.setStatus("current")


class _CvdslLineType_Type(Integer32):
    """Custom type cvdslLineType based on Integer32"""
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
        *(("both", 5),
          ("either", 4),
          ("fastOnly", 2),
          ("noChannel", 1),
          ("slowOnly", 3))
    )


_CvdslLineType_Type.__name__ = "Integer32"
_CvdslLineType_Object = MibTableColumn
cvdslLineType = _CvdslLineType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 1, 1, 2),
    _CvdslLineType_Type()
)
cvdslLineType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvdslLineType.setStatus("current")
_CvdslLineConfProfile_Type = Integer32
_CvdslLineConfProfile_Object = MibTableColumn
cvdslLineConfProfile = _CvdslLineConfProfile_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 1, 1, 3),
    _CvdslLineConfProfile_Type()
)
cvdslLineConfProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvdslLineConfProfile.setStatus("current")
_CvdslLineAlarmConfProfile_Type = Integer32
_CvdslLineAlarmConfProfile_Object = MibTableColumn
cvdslLineAlarmConfProfile = _CvdslLineAlarmConfProfile_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 1, 1, 4),
    _CvdslLineAlarmConfProfile_Type()
)
cvdslLineAlarmConfProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvdslLineAlarmConfProfile.setStatus("current")
_CvdslPhysTable_Object = MibTable
cvdslPhysTable = _CvdslPhysTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cvdslPhysTable.setStatus("current")
_CvdslPhysEntry_Object = MibTableRow
cvdslPhysEntry = _CvdslPhysEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 2, 1)
)
cvdslPhysEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-IETF-VDSL-LINE-MIB", "cvdslPhysSide"),
)
if mibBuilder.loadTexts:
    cvdslPhysEntry.setStatus("current")
_CvdslPhysSide_Type = CVdslLineEntity
_CvdslPhysSide_Object = MibTableColumn
cvdslPhysSide = _CvdslPhysSide_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 2, 1, 1),
    _CvdslPhysSide_Type()
)
cvdslPhysSide.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cvdslPhysSide.setStatus("current")


class _CvdslInvSerialNumber_Type(SnmpAdminString):
    """Custom type cvdslInvSerialNumber based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CvdslInvSerialNumber_Type.__name__ = "SnmpAdminString"
_CvdslInvSerialNumber_Object = MibTableColumn
cvdslInvSerialNumber = _CvdslInvSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 2, 1, 2),
    _CvdslInvSerialNumber_Type()
)
cvdslInvSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvdslInvSerialNumber.setStatus("current")


class _CvdslInvVendorID_Type(SnmpAdminString):
    """Custom type cvdslInvVendorID based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CvdslInvVendorID_Type.__name__ = "SnmpAdminString"
_CvdslInvVendorID_Object = MibTableColumn
cvdslInvVendorID = _CvdslInvVendorID_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 2, 1, 3),
    _CvdslInvVendorID_Type()
)
cvdslInvVendorID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvdslInvVendorID.setStatus("current")


class _CvdslInvVersionNumber_Type(SnmpAdminString):
    """Custom type cvdslInvVersionNumber based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CvdslInvVersionNumber_Type.__name__ = "SnmpAdminString"
_CvdslInvVersionNumber_Object = MibTableColumn
cvdslInvVersionNumber = _CvdslInvVersionNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 2, 1, 4),
    _CvdslInvVersionNumber_Type()
)
cvdslInvVersionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvdslInvVersionNumber.setStatus("current")


class _CvdslCurrSnrMgn_Type(Integer32):
    """Custom type cvdslCurrSnrMgn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-640, 640),
    )


_CvdslCurrSnrMgn_Type.__name__ = "Integer32"
_CvdslCurrSnrMgn_Object = MibTableColumn
cvdslCurrSnrMgn = _CvdslCurrSnrMgn_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 2, 1, 5),
    _CvdslCurrSnrMgn_Type()
)
cvdslCurrSnrMgn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvdslCurrSnrMgn.setStatus("current")
if mibBuilder.loadTexts:
    cvdslCurrSnrMgn.setUnits("tenth dB")


class _CvdslCurrAtn_Type(Gauge32):
    """Custom type cvdslCurrAtn based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 630),
    )


_CvdslCurrAtn_Type.__name__ = "Gauge32"
_CvdslCurrAtn_Object = MibTableColumn
cvdslCurrAtn = _CvdslCurrAtn_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 2, 1, 6),
    _CvdslCurrAtn_Type()
)
cvdslCurrAtn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvdslCurrAtn.setStatus("current")
if mibBuilder.loadTexts:
    cvdslCurrAtn.setUnits("tenth dB")


class _CvdslCurrStatus_Type(Bits):
    """Custom type cvdslCurrStatus based on Bits"""
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

_CvdslCurrStatus_Type.__name__ = "Bits"
_CvdslCurrStatus_Object = MibTableColumn
cvdslCurrStatus = _CvdslCurrStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 2, 1, 7),
    _CvdslCurrStatus_Type()
)
cvdslCurrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvdslCurrStatus.setStatus("current")


class _CvdslCurrOutputPwr_Type(Integer32):
    """Custom type cvdslCurrOutputPwr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-310, 310),
    )


_CvdslCurrOutputPwr_Type.__name__ = "Integer32"
_CvdslCurrOutputPwr_Object = MibTableColumn
cvdslCurrOutputPwr = _CvdslCurrOutputPwr_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 2, 1, 8),
    _CvdslCurrOutputPwr_Type()
)
cvdslCurrOutputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvdslCurrOutputPwr.setStatus("current")
if mibBuilder.loadTexts:
    cvdslCurrOutputPwr.setUnits("tenth dBm")
_CvdslCurrAttainableRate_Type = Gauge32
_CvdslCurrAttainableRate_Object = MibTableColumn
cvdslCurrAttainableRate = _CvdslCurrAttainableRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 2, 1, 9),
    _CvdslCurrAttainableRate_Type()
)
cvdslCurrAttainableRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvdslCurrAttainableRate.setStatus("current")
if mibBuilder.loadTexts:
    cvdslCurrAttainableRate.setUnits("bps")
_CvdslChanTable_Object = MibTable
cvdslChanTable = _CvdslChanTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 3)
)
if mibBuilder.loadTexts:
    cvdslChanTable.setStatus("current")
_CvdslChanEntry_Object = MibTableRow
cvdslChanEntry = _CvdslChanEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 3, 1)
)
cvdslChanEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-IETF-VDSL-LINE-MIB", "cvdslPhysSide"),
)
if mibBuilder.loadTexts:
    cvdslChanEntry.setStatus("current")
_CvdslChanInterleaveDelay_Type = Gauge32
_CvdslChanInterleaveDelay_Object = MibTableColumn
cvdslChanInterleaveDelay = _CvdslChanInterleaveDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 3, 1, 1),
    _CvdslChanInterleaveDelay_Type()
)
cvdslChanInterleaveDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvdslChanInterleaveDelay.setStatus("current")
if mibBuilder.loadTexts:
    cvdslChanInterleaveDelay.setUnits("milli-seconds")
_CvdslChanCrcBlockLength_Type = Gauge32
_CvdslChanCrcBlockLength_Object = MibTableColumn
cvdslChanCrcBlockLength = _CvdslChanCrcBlockLength_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 3, 1, 2),
    _CvdslChanCrcBlockLength_Type()
)
cvdslChanCrcBlockLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvdslChanCrcBlockLength.setStatus("current")
if mibBuilder.loadTexts:
    cvdslChanCrcBlockLength.setUnits("byte")
_CvdslLineConfProfileTable_Object = MibTable
cvdslLineConfProfileTable = _CvdslLineConfProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 8)
)
if mibBuilder.loadTexts:
    cvdslLineConfProfileTable.setStatus("current")
_CvdslLineConfProfileEntry_Object = MibTableRow
cvdslLineConfProfileEntry = _CvdslLineConfProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 8, 1)
)
cvdslLineConfProfileEntry.setIndexNames(
    (0, "CISCO-IETF-VDSL-LINE-MIB", "cvdslPhysSide"),
    (0, "CISCO-IETF-VDSL-LINE-MIB", "cvdslLineConfProfileIndex"),
)
if mibBuilder.loadTexts:
    cvdslLineConfProfileEntry.setStatus("current")


class _CvdslLineConfProfileIndex_Type(Integer32):
    """Custom type cvdslLineConfProfileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CvdslLineConfProfileIndex_Type.__name__ = "Integer32"
_CvdslLineConfProfileIndex_Object = MibTableColumn
cvdslLineConfProfileIndex = _CvdslLineConfProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 8, 1, 1),
    _CvdslLineConfProfileIndex_Type()
)
cvdslLineConfProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cvdslLineConfProfileIndex.setStatus("current")


class _CvdslLineConfProfileName_Type(SnmpAdminString):
    """Custom type cvdslLineConfProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CvdslLineConfProfileName_Type.__name__ = "SnmpAdminString"
_CvdslLineConfProfileName_Object = MibTableColumn
cvdslLineConfProfileName = _CvdslLineConfProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 8, 1, 2),
    _CvdslLineConfProfileName_Type()
)
cvdslLineConfProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cvdslLineConfProfileName.setStatus("current")


class _CvdslLineConfTargetSnrMgn_Type(Integer32):
    """Custom type cvdslLineConfTargetSnrMgn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 310),
    )


_CvdslLineConfTargetSnrMgn_Type.__name__ = "Integer32"
_CvdslLineConfTargetSnrMgn_Object = MibTableColumn
cvdslLineConfTargetSnrMgn = _CvdslLineConfTargetSnrMgn_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 8, 1, 3),
    _CvdslLineConfTargetSnrMgn_Type()
)
cvdslLineConfTargetSnrMgn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cvdslLineConfTargetSnrMgn.setStatus("current")
if mibBuilder.loadTexts:
    cvdslLineConfTargetSnrMgn.setUnits("tenth dB")


class _CvdslLineConfTxSpeed_Type(Integer32):
    """Custom type cvdslLineConfTxSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CvdslLineConfTxSpeed_Type.__name__ = "Integer32"
_CvdslLineConfTxSpeed_Object = MibTableColumn
cvdslLineConfTxSpeed = _CvdslLineConfTxSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 8, 1, 4),
    _CvdslLineConfTxSpeed_Type()
)
cvdslLineConfTxSpeed.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cvdslLineConfTxSpeed.setStatus("current")
if mibBuilder.loadTexts:
    cvdslLineConfTxSpeed.setUnits("bits per second")


class _CvdslLineConfRxSpeed_Type(Integer32):
    """Custom type cvdslLineConfRxSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CvdslLineConfRxSpeed_Type.__name__ = "Integer32"
_CvdslLineConfRxSpeed_Object = MibTableColumn
cvdslLineConfRxSpeed = _CvdslLineConfRxSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 8, 1, 5),
    _CvdslLineConfRxSpeed_Type()
)
cvdslLineConfRxSpeed.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cvdslLineConfRxSpeed.setStatus("current")
if mibBuilder.loadTexts:
    cvdslLineConfRxSpeed.setUnits("bits per second")
_CvdslLineConfProfileRowStatus_Type = RowStatus
_CvdslLineConfProfileRowStatus_Object = MibTableColumn
cvdslLineConfProfileRowStatus = _CvdslLineConfProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 8, 1, 6),
    _CvdslLineConfProfileRowStatus_Type()
)
cvdslLineConfProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cvdslLineConfProfileRowStatus.setStatus("current")
_CvdslLineMCMConfProfileTable_Object = MibTable
cvdslLineMCMConfProfileTable = _CvdslLineMCMConfProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 9)
)
if mibBuilder.loadTexts:
    cvdslLineMCMConfProfileTable.setStatus("current")
_CvdslLineMCMConfProfileEntry_Object = MibTableRow
cvdslLineMCMConfProfileEntry = _CvdslLineMCMConfProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 9, 1)
)
cvdslLineMCMConfProfileEntry.setIndexNames(
    (0, "CISCO-IETF-VDSL-LINE-MIB", "cvdslPhysSide"),
    (0, "CISCO-IETF-VDSL-LINE-MIB", "cvdslLineConfProfileIndex"),
)
if mibBuilder.loadTexts:
    cvdslLineMCMConfProfileEntry.setStatus("current")


class _CvdslMCMConfProfileTxWindowLength_Type(Integer32):
    """Custom type cvdslMCMConfProfileTxWindowLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_CvdslMCMConfProfileTxWindowLength_Type.__name__ = "Integer32"
_CvdslMCMConfProfileTxWindowLength_Object = MibTableColumn
cvdslMCMConfProfileTxWindowLength = _CvdslMCMConfProfileTxWindowLength_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 9, 1, 1),
    _CvdslMCMConfProfileTxWindowLength_Type()
)
cvdslMCMConfProfileTxWindowLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cvdslMCMConfProfileTxWindowLength.setStatus("current")
if mibBuilder.loadTexts:
    cvdslMCMConfProfileTxWindowLength.setUnits("samples")
_CvdslMCMConfProfileRowStatus_Type = RowStatus
_CvdslMCMConfProfileRowStatus_Object = MibTableColumn
cvdslMCMConfProfileRowStatus = _CvdslMCMConfProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 9, 1, 2),
    _CvdslMCMConfProfileRowStatus_Type()
)
cvdslMCMConfProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cvdslMCMConfProfileRowStatus.setStatus("current")
_CvdslLineMCMConfProfileTxBandTable_Object = MibTable
cvdslLineMCMConfProfileTxBandTable = _CvdslLineMCMConfProfileTxBandTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 10)
)
if mibBuilder.loadTexts:
    cvdslLineMCMConfProfileTxBandTable.setStatus("current")
_CvdslLineMCMConfProfileTxBandEntry_Object = MibTableRow
cvdslLineMCMConfProfileTxBandEntry = _CvdslLineMCMConfProfileTxBandEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 10, 1)
)
cvdslLineMCMConfProfileTxBandEntry.setIndexNames(
    (0, "CISCO-IETF-VDSL-LINE-MIB", "cvdslPhysSide"),
    (0, "CISCO-IETF-VDSL-LINE-MIB", "cvdslLineConfProfileIndex"),
    (0, "CISCO-IETF-VDSL-LINE-MIB", "cvdslMCMConfProfileTxBandNumber"),
)
if mibBuilder.loadTexts:
    cvdslLineMCMConfProfileTxBandEntry.setStatus("current")


class _CvdslMCMConfProfileTxBandNumber_Type(Integer32):
    """Custom type cvdslMCMConfProfileTxBandNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CvdslMCMConfProfileTxBandNumber_Type.__name__ = "Integer32"
_CvdslMCMConfProfileTxBandNumber_Object = MibTableColumn
cvdslMCMConfProfileTxBandNumber = _CvdslMCMConfProfileTxBandNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 10, 1, 1),
    _CvdslMCMConfProfileTxBandNumber_Type()
)
cvdslMCMConfProfileTxBandNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cvdslMCMConfProfileTxBandNumber.setStatus("current")


class _CvdslMCMConfProfileTxBandStart_Type(Integer32):
    """Custom type cvdslMCMConfProfileTxBandStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CvdslMCMConfProfileTxBandStart_Type.__name__ = "Integer32"
_CvdslMCMConfProfileTxBandStart_Object = MibTableColumn
cvdslMCMConfProfileTxBandStart = _CvdslMCMConfProfileTxBandStart_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 10, 1, 2),
    _CvdslMCMConfProfileTxBandStart_Type()
)
cvdslMCMConfProfileTxBandStart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cvdslMCMConfProfileTxBandStart.setStatus("current")


class _CvdslMCMConfProfileTxBandStop_Type(Integer32):
    """Custom type cvdslMCMConfProfileTxBandStop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CvdslMCMConfProfileTxBandStop_Type.__name__ = "Integer32"
_CvdslMCMConfProfileTxBandStop_Object = MibTableColumn
cvdslMCMConfProfileTxBandStop = _CvdslMCMConfProfileTxBandStop_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 10, 1, 3),
    _CvdslMCMConfProfileTxBandStop_Type()
)
cvdslMCMConfProfileTxBandStop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cvdslMCMConfProfileTxBandStop.setStatus("current")
_CvdslMCMConfProfileTxBandRowStatus_Type = RowStatus
_CvdslMCMConfProfileTxBandRowStatus_Object = MibTableColumn
cvdslMCMConfProfileTxBandRowStatus = _CvdslMCMConfProfileTxBandRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 10, 1, 4),
    _CvdslMCMConfProfileTxBandRowStatus_Type()
)
cvdslMCMConfProfileTxBandRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cvdslMCMConfProfileTxBandRowStatus.setStatus("current")
_CvdslLineMCMConfProfileRxBandTable_Object = MibTable
cvdslLineMCMConfProfileRxBandTable = _CvdslLineMCMConfProfileRxBandTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 11)
)
if mibBuilder.loadTexts:
    cvdslLineMCMConfProfileRxBandTable.setStatus("current")
_CvdslLineMCMConfProfileRxBandEntry_Object = MibTableRow
cvdslLineMCMConfProfileRxBandEntry = _CvdslLineMCMConfProfileRxBandEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 11, 1)
)
cvdslLineMCMConfProfileRxBandEntry.setIndexNames(
    (0, "CISCO-IETF-VDSL-LINE-MIB", "cvdslPhysSide"),
    (0, "CISCO-IETF-VDSL-LINE-MIB", "cvdslLineConfProfileIndex"),
    (0, "CISCO-IETF-VDSL-LINE-MIB", "cvdslMCMConfProfileRxBandNumber"),
)
if mibBuilder.loadTexts:
    cvdslLineMCMConfProfileRxBandEntry.setStatus("current")


class _CvdslMCMConfProfileRxBandNumber_Type(Integer32):
    """Custom type cvdslMCMConfProfileRxBandNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CvdslMCMConfProfileRxBandNumber_Type.__name__ = "Integer32"
_CvdslMCMConfProfileRxBandNumber_Object = MibTableColumn
cvdslMCMConfProfileRxBandNumber = _CvdslMCMConfProfileRxBandNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 11, 1, 1),
    _CvdslMCMConfProfileRxBandNumber_Type()
)
cvdslMCMConfProfileRxBandNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cvdslMCMConfProfileRxBandNumber.setStatus("current")


class _CvdslMCMConfProfileRxBandStart_Type(Integer32):
    """Custom type cvdslMCMConfProfileRxBandStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CvdslMCMConfProfileRxBandStart_Type.__name__ = "Integer32"
_CvdslMCMConfProfileRxBandStart_Object = MibTableColumn
cvdslMCMConfProfileRxBandStart = _CvdslMCMConfProfileRxBandStart_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 11, 1, 2),
    _CvdslMCMConfProfileRxBandStart_Type()
)
cvdslMCMConfProfileRxBandStart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cvdslMCMConfProfileRxBandStart.setStatus("current")


class _CvdslMCMConfProfileRxBandStop_Type(Integer32):
    """Custom type cvdslMCMConfProfileRxBandStop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CvdslMCMConfProfileRxBandStop_Type.__name__ = "Integer32"
_CvdslMCMConfProfileRxBandStop_Object = MibTableColumn
cvdslMCMConfProfileRxBandStop = _CvdslMCMConfProfileRxBandStop_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 11, 1, 3),
    _CvdslMCMConfProfileRxBandStop_Type()
)
cvdslMCMConfProfileRxBandStop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cvdslMCMConfProfileRxBandStop.setStatus("current")
_CvdslMCMConfProfileRxBandRowStatus_Type = RowStatus
_CvdslMCMConfProfileRxBandRowStatus_Object = MibTableColumn
cvdslMCMConfProfileRxBandRowStatus = _CvdslMCMConfProfileRxBandRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 11, 1, 4),
    _CvdslMCMConfProfileRxBandRowStatus_Type()
)
cvdslMCMConfProfileRxBandRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cvdslMCMConfProfileRxBandRowStatus.setStatus("current")
_CvdslLineMCMConfProfileTxPSDTable_Object = MibTable
cvdslLineMCMConfProfileTxPSDTable = _CvdslLineMCMConfProfileTxPSDTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 12)
)
if mibBuilder.loadTexts:
    cvdslLineMCMConfProfileTxPSDTable.setStatus("current")
_CvdslLineMCMConfProfileTxPSDEntry_Object = MibTableRow
cvdslLineMCMConfProfileTxPSDEntry = _CvdslLineMCMConfProfileTxPSDEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 12, 1)
)
cvdslLineMCMConfProfileTxPSDEntry.setIndexNames(
    (0, "CISCO-IETF-VDSL-LINE-MIB", "cvdslPhysSide"),
    (0, "CISCO-IETF-VDSL-LINE-MIB", "cvdslLineConfProfileIndex"),
    (0, "CISCO-IETF-VDSL-LINE-MIB", "cvdslMCMConfProfileTxPSDNumber"),
)
if mibBuilder.loadTexts:
    cvdslLineMCMConfProfileTxPSDEntry.setStatus("current")


class _CvdslMCMConfProfileTxPSDNumber_Type(Integer32):
    """Custom type cvdslMCMConfProfileTxPSDNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CvdslMCMConfProfileTxPSDNumber_Type.__name__ = "Integer32"
_CvdslMCMConfProfileTxPSDNumber_Object = MibTableColumn
cvdslMCMConfProfileTxPSDNumber = _CvdslMCMConfProfileTxPSDNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 12, 1, 1),
    _CvdslMCMConfProfileTxPSDNumber_Type()
)
cvdslMCMConfProfileTxPSDNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cvdslMCMConfProfileTxPSDNumber.setStatus("current")


class _CvdslMCMConfProfileTxPSDTone_Type(Integer32):
    """Custom type cvdslMCMConfProfileTxPSDTone based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CvdslMCMConfProfileTxPSDTone_Type.__name__ = "Integer32"
_CvdslMCMConfProfileTxPSDTone_Object = MibTableColumn
cvdslMCMConfProfileTxPSDTone = _CvdslMCMConfProfileTxPSDTone_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 12, 1, 2),
    _CvdslMCMConfProfileTxPSDTone_Type()
)
cvdslMCMConfProfileTxPSDTone.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cvdslMCMConfProfileTxPSDTone.setStatus("current")


class _CvdslMCMConfProfileTxPSDPSD_Type(Integer32):
    """Custom type cvdslMCMConfProfileTxPSDPSD based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CvdslMCMConfProfileTxPSDPSD_Type.__name__ = "Integer32"
_CvdslMCMConfProfileTxPSDPSD_Object = MibTableColumn
cvdslMCMConfProfileTxPSDPSD = _CvdslMCMConfProfileTxPSDPSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 12, 1, 3),
    _CvdslMCMConfProfileTxPSDPSD_Type()
)
cvdslMCMConfProfileTxPSDPSD.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cvdslMCMConfProfileTxPSDPSD.setStatus("current")
if mibBuilder.loadTexts:
    cvdslMCMConfProfileTxPSDPSD.setUnits("0.5dB")
_CvdslMCMConfProfileTxPSDRowStatus_Type = RowStatus
_CvdslMCMConfProfileTxPSDRowStatus_Object = MibTableColumn
cvdslMCMConfProfileTxPSDRowStatus = _CvdslMCMConfProfileTxPSDRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 12, 1, 4),
    _CvdslMCMConfProfileTxPSDRowStatus_Type()
)
cvdslMCMConfProfileTxPSDRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cvdslMCMConfProfileTxPSDRowStatus.setStatus("current")
_CvdslLineMCMConfProfileMaxTxPSDTable_Object = MibTable
cvdslLineMCMConfProfileMaxTxPSDTable = _CvdslLineMCMConfProfileMaxTxPSDTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 13)
)
if mibBuilder.loadTexts:
    cvdslLineMCMConfProfileMaxTxPSDTable.setStatus("current")
_CvdslLineMCMConfProfileMaxTxPSDEntry_Object = MibTableRow
cvdslLineMCMConfProfileMaxTxPSDEntry = _CvdslLineMCMConfProfileMaxTxPSDEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 13, 1)
)
cvdslLineMCMConfProfileMaxTxPSDEntry.setIndexNames(
    (0, "CISCO-IETF-VDSL-LINE-MIB", "cvdslPhysSide"),
    (0, "CISCO-IETF-VDSL-LINE-MIB", "cvdslLineConfProfileIndex"),
    (0, "CISCO-IETF-VDSL-LINE-MIB", "cvdslMCMConfProfileMaxTxPSDNumber"),
)
if mibBuilder.loadTexts:
    cvdslLineMCMConfProfileMaxTxPSDEntry.setStatus("current")


class _CvdslMCMConfProfileMaxTxPSDNumber_Type(Integer32):
    """Custom type cvdslMCMConfProfileMaxTxPSDNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CvdslMCMConfProfileMaxTxPSDNumber_Type.__name__ = "Integer32"
_CvdslMCMConfProfileMaxTxPSDNumber_Object = MibTableColumn
cvdslMCMConfProfileMaxTxPSDNumber = _CvdslMCMConfProfileMaxTxPSDNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 13, 1, 1),
    _CvdslMCMConfProfileMaxTxPSDNumber_Type()
)
cvdslMCMConfProfileMaxTxPSDNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cvdslMCMConfProfileMaxTxPSDNumber.setStatus("current")


class _CvdslMCMConfProfileMaxTxPSDTone_Type(Integer32):
    """Custom type cvdslMCMConfProfileMaxTxPSDTone based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CvdslMCMConfProfileMaxTxPSDTone_Type.__name__ = "Integer32"
_CvdslMCMConfProfileMaxTxPSDTone_Object = MibTableColumn
cvdslMCMConfProfileMaxTxPSDTone = _CvdslMCMConfProfileMaxTxPSDTone_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 13, 1, 2),
    _CvdslMCMConfProfileMaxTxPSDTone_Type()
)
cvdslMCMConfProfileMaxTxPSDTone.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cvdslMCMConfProfileMaxTxPSDTone.setStatus("current")


class _CvdslMCMConfProfileMaxTxPSDPSD_Type(Integer32):
    """Custom type cvdslMCMConfProfileMaxTxPSDPSD based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CvdslMCMConfProfileMaxTxPSDPSD_Type.__name__ = "Integer32"
_CvdslMCMConfProfileMaxTxPSDPSD_Object = MibTableColumn
cvdslMCMConfProfileMaxTxPSDPSD = _CvdslMCMConfProfileMaxTxPSDPSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 13, 1, 3),
    _CvdslMCMConfProfileMaxTxPSDPSD_Type()
)
cvdslMCMConfProfileMaxTxPSDPSD.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cvdslMCMConfProfileMaxTxPSDPSD.setStatus("current")
if mibBuilder.loadTexts:
    cvdslMCMConfProfileMaxTxPSDPSD.setUnits("0.5dB")
_CvdslMCMConfProfileMaxTxPSDRowStatus_Type = RowStatus
_CvdslMCMConfProfileMaxTxPSDRowStatus_Object = MibTableColumn
cvdslMCMConfProfileMaxTxPSDRowStatus = _CvdslMCMConfProfileMaxTxPSDRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 13, 1, 4),
    _CvdslMCMConfProfileMaxTxPSDRowStatus_Type()
)
cvdslMCMConfProfileMaxTxPSDRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cvdslMCMConfProfileMaxTxPSDRowStatus.setStatus("current")
_CvdslLineMCMConfProfileMaxRxPSDTable_Object = MibTable
cvdslLineMCMConfProfileMaxRxPSDTable = _CvdslLineMCMConfProfileMaxRxPSDTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 14)
)
if mibBuilder.loadTexts:
    cvdslLineMCMConfProfileMaxRxPSDTable.setStatus("current")
_CvdslLineMCMConfProfileMaxRxPSDEntry_Object = MibTableRow
cvdslLineMCMConfProfileMaxRxPSDEntry = _CvdslLineMCMConfProfileMaxRxPSDEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 14, 1)
)
cvdslLineMCMConfProfileMaxRxPSDEntry.setIndexNames(
    (0, "CISCO-IETF-VDSL-LINE-MIB", "cvdslPhysSide"),
    (0, "CISCO-IETF-VDSL-LINE-MIB", "cvdslLineConfProfileIndex"),
    (0, "CISCO-IETF-VDSL-LINE-MIB", "cvdslMCMConfProfileMaxRxPSDNumber"),
)
if mibBuilder.loadTexts:
    cvdslLineMCMConfProfileMaxRxPSDEntry.setStatus("current")


class _CvdslMCMConfProfileMaxRxPSDNumber_Type(Integer32):
    """Custom type cvdslMCMConfProfileMaxRxPSDNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CvdslMCMConfProfileMaxRxPSDNumber_Type.__name__ = "Integer32"
_CvdslMCMConfProfileMaxRxPSDNumber_Object = MibTableColumn
cvdslMCMConfProfileMaxRxPSDNumber = _CvdslMCMConfProfileMaxRxPSDNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 14, 1, 1),
    _CvdslMCMConfProfileMaxRxPSDNumber_Type()
)
cvdslMCMConfProfileMaxRxPSDNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cvdslMCMConfProfileMaxRxPSDNumber.setStatus("current")


class _CvdslMCMConfProfileMaxRxPSDTone_Type(Integer32):
    """Custom type cvdslMCMConfProfileMaxRxPSDTone based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CvdslMCMConfProfileMaxRxPSDTone_Type.__name__ = "Integer32"
_CvdslMCMConfProfileMaxRxPSDTone_Object = MibTableColumn
cvdslMCMConfProfileMaxRxPSDTone = _CvdslMCMConfProfileMaxRxPSDTone_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 14, 1, 2),
    _CvdslMCMConfProfileMaxRxPSDTone_Type()
)
cvdslMCMConfProfileMaxRxPSDTone.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cvdslMCMConfProfileMaxRxPSDTone.setStatus("current")


class _CvdslMCMConfProfileMaxRxPSDPSD_Type(Integer32):
    """Custom type cvdslMCMConfProfileMaxRxPSDPSD based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CvdslMCMConfProfileMaxRxPSDPSD_Type.__name__ = "Integer32"
_CvdslMCMConfProfileMaxRxPSDPSD_Object = MibTableColumn
cvdslMCMConfProfileMaxRxPSDPSD = _CvdslMCMConfProfileMaxRxPSDPSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 14, 1, 3),
    _CvdslMCMConfProfileMaxRxPSDPSD_Type()
)
cvdslMCMConfProfileMaxRxPSDPSD.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cvdslMCMConfProfileMaxRxPSDPSD.setStatus("current")
if mibBuilder.loadTexts:
    cvdslMCMConfProfileMaxRxPSDPSD.setUnits("0.5dB")
_CvdslMCMConfProfileMaxRxPSDRowStatus_Type = RowStatus
_CvdslMCMConfProfileMaxRxPSDRowStatus_Object = MibTableColumn
cvdslMCMConfProfileMaxRxPSDRowStatus = _CvdslMCMConfProfileMaxRxPSDRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 14, 1, 4),
    _CvdslMCMConfProfileMaxRxPSDRowStatus_Type()
)
cvdslMCMConfProfileMaxRxPSDRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cvdslMCMConfProfileMaxRxPSDRowStatus.setStatus("current")
_CvdslLineSCMConfProfileTable_Object = MibTable
cvdslLineSCMConfProfileTable = _CvdslLineSCMConfProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 15)
)
if mibBuilder.loadTexts:
    cvdslLineSCMConfProfileTable.setStatus("current")
_CvdslLineSCMConfProfileEntry_Object = MibTableRow
cvdslLineSCMConfProfileEntry = _CvdslLineSCMConfProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 15, 1)
)
cvdslLineSCMConfProfileEntry.setIndexNames(
    (0, "CISCO-IETF-VDSL-LINE-MIB", "cvdslPhysSide"),
    (0, "CISCO-IETF-VDSL-LINE-MIB", "cvdslLineConfProfileIndex"),
)
if mibBuilder.loadTexts:
    cvdslLineSCMConfProfileEntry.setStatus("current")


class _CvdslSCMConfProfileInterleaveDepth_Type(Integer32):
    """Custom type cvdslSCMConfProfileInterleaveDepth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CvdslSCMConfProfileInterleaveDepth_Type.__name__ = "Integer32"
_CvdslSCMConfProfileInterleaveDepth_Object = MibTableColumn
cvdslSCMConfProfileInterleaveDepth = _CvdslSCMConfProfileInterleaveDepth_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 15, 1, 1),
    _CvdslSCMConfProfileInterleaveDepth_Type()
)
cvdslSCMConfProfileInterleaveDepth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cvdslSCMConfProfileInterleaveDepth.setStatus("current")
if mibBuilder.loadTexts:
    cvdslSCMConfProfileInterleaveDepth.setUnits("octets")


class _CvdslSCMConfProfileFastCodewordSize_Type(Integer32):
    """Custom type cvdslSCMConfProfileFastCodewordSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 180),
    )


_CvdslSCMConfProfileFastCodewordSize_Type.__name__ = "Integer32"
_CvdslSCMConfProfileFastCodewordSize_Object = MibTableColumn
cvdslSCMConfProfileFastCodewordSize = _CvdslSCMConfProfileFastCodewordSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 15, 1, 2),
    _CvdslSCMConfProfileFastCodewordSize_Type()
)
cvdslSCMConfProfileFastCodewordSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cvdslSCMConfProfileFastCodewordSize.setStatus("current")
if mibBuilder.loadTexts:
    cvdslSCMConfProfileFastCodewordSize.setUnits("octets")


class _CvdslSCMConfProfileTransmitPSDMask_Type(Bits):
    """Custom type cvdslSCMConfProfileTransmitPSDMask based on Bits"""
    namedValues = NamedValues(
        *(("amateurBand160m", 5),
          ("amateurBand30m", 2),
          ("amateurBand40m", 3),
          ("amateurBand80m", 4),
          ("vendorNotch1", 0),
          ("vendorNotch2", 1))
    )

_CvdslSCMConfProfileTransmitPSDMask_Type.__name__ = "Bits"
_CvdslSCMConfProfileTransmitPSDMask_Object = MibTableColumn
cvdslSCMConfProfileTransmitPSDMask = _CvdslSCMConfProfileTransmitPSDMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 15, 1, 3),
    _CvdslSCMConfProfileTransmitPSDMask_Type()
)
cvdslSCMConfProfileTransmitPSDMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cvdslSCMConfProfileTransmitPSDMask.setStatus("current")


class _CvdslSCMConfProfileTransmitPSDLevel_Type(Integer32):
    """Custom type cvdslSCMConfProfileTransmitPSDLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CvdslSCMConfProfileTransmitPSDLevel_Type.__name__ = "Integer32"
_CvdslSCMConfProfileTransmitPSDLevel_Object = MibTableColumn
cvdslSCMConfProfileTransmitPSDLevel = _CvdslSCMConfProfileTransmitPSDLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 15, 1, 4),
    _CvdslSCMConfProfileTransmitPSDLevel_Type()
)
cvdslSCMConfProfileTransmitPSDLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cvdslSCMConfProfileTransmitPSDLevel.setStatus("current")
if mibBuilder.loadTexts:
    cvdslSCMConfProfileTransmitPSDLevel.setUnits("dBm/Hz")


class _CvdslSCMConfProfileSymbolRateProfile_Type(Integer32):
    """Custom type cvdslSCMConfProfileSymbolRateProfile based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CvdslSCMConfProfileSymbolRateProfile_Type.__name__ = "Integer32"
_CvdslSCMConfProfileSymbolRateProfile_Object = MibTableColumn
cvdslSCMConfProfileSymbolRateProfile = _CvdslSCMConfProfileSymbolRateProfile_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 15, 1, 5),
    _CvdslSCMConfProfileSymbolRateProfile_Type()
)
cvdslSCMConfProfileSymbolRateProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cvdslSCMConfProfileSymbolRateProfile.setStatus("current")
if mibBuilder.loadTexts:
    cvdslSCMConfProfileSymbolRateProfile.setUnits("kbaud")


class _CvdslSCMConfProfileConstellationSize_Type(Integer32):
    """Custom type cvdslSCMConfProfileConstellationSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_CvdslSCMConfProfileConstellationSize_Type.__name__ = "Integer32"
_CvdslSCMConfProfileConstellationSize_Object = MibTableColumn
cvdslSCMConfProfileConstellationSize = _CvdslSCMConfProfileConstellationSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 15, 1, 6),
    _CvdslSCMConfProfileConstellationSize_Type()
)
cvdslSCMConfProfileConstellationSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cvdslSCMConfProfileConstellationSize.setStatus("current")
if mibBuilder.loadTexts:
    cvdslSCMConfProfileConstellationSize.setUnits("log2")


class _CvdslSCMConfProfileCenterFrequency_Type(Integer32):
    """Custom type cvdslSCMConfProfileCenterFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 511),
    )


_CvdslSCMConfProfileCenterFrequency_Type.__name__ = "Integer32"
_CvdslSCMConfProfileCenterFrequency_Object = MibTableColumn
cvdslSCMConfProfileCenterFrequency = _CvdslSCMConfProfileCenterFrequency_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 15, 1, 7),
    _CvdslSCMConfProfileCenterFrequency_Type()
)
cvdslSCMConfProfileCenterFrequency.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cvdslSCMConfProfileCenterFrequency.setStatus("current")
if mibBuilder.loadTexts:
    cvdslSCMConfProfileCenterFrequency.setUnits("kHz")
_CvdslSCMConfProfileRowStatus_Type = RowStatus
_CvdslSCMConfProfileRowStatus_Object = MibTableColumn
cvdslSCMConfProfileRowStatus = _CvdslSCMConfProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 15, 1, 8),
    _CvdslSCMConfProfileRowStatus_Type()
)
cvdslSCMConfProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cvdslSCMConfProfileRowStatus.setStatus("current")
_CvdslLineAlarmConfProfileTable_Object = MibTable
cvdslLineAlarmConfProfileTable = _CvdslLineAlarmConfProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 16)
)
if mibBuilder.loadTexts:
    cvdslLineAlarmConfProfileTable.setStatus("current")
_CvdslLineAlarmConfProfileEntry_Object = MibTableRow
cvdslLineAlarmConfProfileEntry = _CvdslLineAlarmConfProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 16, 1)
)
cvdslLineAlarmConfProfileEntry.setIndexNames(
    (0, "CISCO-IETF-VDSL-LINE-MIB", "cvdslPhysSide"),
    (0, "CISCO-IETF-VDSL-LINE-MIB", "cvdslLineAlarmConfProfileIndex"),
)
if mibBuilder.loadTexts:
    cvdslLineAlarmConfProfileEntry.setStatus("current")


class _CvdslLineAlarmConfProfileIndex_Type(Integer32):
    """Custom type cvdslLineAlarmConfProfileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CvdslLineAlarmConfProfileIndex_Type.__name__ = "Integer32"
_CvdslLineAlarmConfProfileIndex_Object = MibTableColumn
cvdslLineAlarmConfProfileIndex = _CvdslLineAlarmConfProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 16, 1, 1),
    _CvdslLineAlarmConfProfileIndex_Type()
)
cvdslLineAlarmConfProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cvdslLineAlarmConfProfileIndex.setStatus("current")


class _CvdslLineAlarmConfProfileName_Type(SnmpAdminString):
    """Custom type cvdslLineAlarmConfProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CvdslLineAlarmConfProfileName_Type.__name__ = "SnmpAdminString"
_CvdslLineAlarmConfProfileName_Object = MibTableColumn
cvdslLineAlarmConfProfileName = _CvdslLineAlarmConfProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 16, 1, 2),
    _CvdslLineAlarmConfProfileName_Type()
)
cvdslLineAlarmConfProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cvdslLineAlarmConfProfileName.setStatus("current")
_CvdslInitFailureNotificationEnable_Type = TruthValue
_CvdslInitFailureNotificationEnable_Object = MibTableColumn
cvdslInitFailureNotificationEnable = _CvdslInitFailureNotificationEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 16, 1, 3),
    _CvdslInitFailureNotificationEnable_Type()
)
cvdslInitFailureNotificationEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cvdslInitFailureNotificationEnable.setStatus("current")
_CvdslLineAlarmConfProfileRowStatus_Type = RowStatus
_CvdslLineAlarmConfProfileRowStatus_Object = MibTableColumn
cvdslLineAlarmConfProfileRowStatus = _CvdslLineAlarmConfProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 16, 1, 4),
    _CvdslLineAlarmConfProfileRowStatus_Type()
)
cvdslLineAlarmConfProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cvdslLineAlarmConfProfileRowStatus.setStatus("current")
_CvdslConformance_ObjectIdentity = ObjectIdentity
cvdslConformance = _CvdslConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 3)
)
_CvdslGroups_ObjectIdentity = ObjectIdentity
cvdslGroups = _CvdslGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 3, 1)
)
_CvdslCompliances_ObjectIdentity = ObjectIdentity
cvdslCompliances = _CvdslCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 3, 2)
)

# Managed Objects groups

cvdslGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 3, 1, 1)
)
cvdslGroup.setObjects(
      *(("CISCO-IETF-VDSL-LINE-MIB", "cvdslLineCoding"),
        ("CISCO-IETF-VDSL-LINE-MIB", "cvdslLineType"),
        ("CISCO-IETF-VDSL-LINE-MIB", "cvdslLineConfProfile"),
        ("CISCO-IETF-VDSL-LINE-MIB", "cvdslLineAlarmConfProfile"),
        ("CISCO-IETF-VDSL-LINE-MIB", "cvdslInvSerialNumber"),
        ("CISCO-IETF-VDSL-LINE-MIB", "cvdslInvVendorID"),
        ("CISCO-IETF-VDSL-LINE-MIB", "cvdslInvVersionNumber"),
        ("CISCO-IETF-VDSL-LINE-MIB", "cvdslCurrSnrMgn"),
        ("CISCO-IETF-VDSL-LINE-MIB", "cvdslCurrAtn"),
        ("CISCO-IETF-VDSL-LINE-MIB", "cvdslCurrStatus"),
        ("CISCO-IETF-VDSL-LINE-MIB", "cvdslCurrOutputPwr"),
        ("CISCO-IETF-VDSL-LINE-MIB", "cvdslCurrAttainableRate"),
        ("CISCO-IETF-VDSL-LINE-MIB", "cvdslChanInterleaveDelay"),
        ("CISCO-IETF-VDSL-LINE-MIB", "cvdslChanCrcBlockLength"),
        ("CISCO-IETF-VDSL-LINE-MIB", "cvdslLineConfProfileName"),
        ("CISCO-IETF-VDSL-LINE-MIB", "cvdslLineConfTargetSnrMgn"),
        ("CISCO-IETF-VDSL-LINE-MIB", "cvdslLineConfTxSpeed"),
        ("CISCO-IETF-VDSL-LINE-MIB", "cvdslLineConfRxSpeed"),
        ("CISCO-IETF-VDSL-LINE-MIB", "cvdslLineConfProfileRowStatus"),
        ("CISCO-IETF-VDSL-LINE-MIB", "cvdslLineAlarmConfProfileName"),
        ("CISCO-IETF-VDSL-LINE-MIB", "cvdslInitFailureNotificationEnable"),
        ("CISCO-IETF-VDSL-LINE-MIB", "cvdslLineAlarmConfProfileRowStatus"))
)
if mibBuilder.loadTexts:
    cvdslGroup.setStatus("current")

cvdslMCMGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 3, 1, 2)
)
cvdslMCMGroup.setObjects(
      *(("CISCO-IETF-VDSL-LINE-MIB", "cvdslMCMConfProfileTxWindowLength"),
        ("CISCO-IETF-VDSL-LINE-MIB", "cvdslMCMConfProfileRowStatus"),
        ("CISCO-IETF-VDSL-LINE-MIB", "cvdslMCMConfProfileTxBandStart"),
        ("CISCO-IETF-VDSL-LINE-MIB", "cvdslMCMConfProfileTxBandStop"),
        ("CISCO-IETF-VDSL-LINE-MIB", "cvdslMCMConfProfileTxBandRowStatus"),
        ("CISCO-IETF-VDSL-LINE-MIB", "cvdslMCMConfProfileRxBandStart"),
        ("CISCO-IETF-VDSL-LINE-MIB", "cvdslMCMConfProfileRxBandStop"),
        ("CISCO-IETF-VDSL-LINE-MIB", "cvdslMCMConfProfileRxBandRowStatus"),
        ("CISCO-IETF-VDSL-LINE-MIB", "cvdslMCMConfProfileTxPSDTone"),
        ("CISCO-IETF-VDSL-LINE-MIB", "cvdslMCMConfProfileTxPSDPSD"),
        ("CISCO-IETF-VDSL-LINE-MIB", "cvdslMCMConfProfileTxPSDRowStatus"),
        ("CISCO-IETF-VDSL-LINE-MIB", "cvdslMCMConfProfileMaxTxPSDTone"),
        ("CISCO-IETF-VDSL-LINE-MIB", "cvdslMCMConfProfileMaxTxPSDPSD"),
        ("CISCO-IETF-VDSL-LINE-MIB", "cvdslMCMConfProfileMaxTxPSDRowStatus"),
        ("CISCO-IETF-VDSL-LINE-MIB", "cvdslMCMConfProfileMaxRxPSDTone"),
        ("CISCO-IETF-VDSL-LINE-MIB", "cvdslMCMConfProfileMaxRxPSDPSD"),
        ("CISCO-IETF-VDSL-LINE-MIB", "cvdslMCMConfProfileMaxRxPSDRowStatus"))
)
if mibBuilder.loadTexts:
    cvdslMCMGroup.setStatus("current")

cvdslSCMGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 3, 1, 3)
)
cvdslSCMGroup.setObjects(
      *(("CISCO-IETF-VDSL-LINE-MIB", "cvdslSCMConfProfileInterleaveDepth"),
        ("CISCO-IETF-VDSL-LINE-MIB", "cvdslSCMConfProfileFastCodewordSize"),
        ("CISCO-IETF-VDSL-LINE-MIB", "cvdslSCMConfProfileTransmitPSDMask"),
        ("CISCO-IETF-VDSL-LINE-MIB", "cvdslSCMConfProfileTransmitPSDLevel"),
        ("CISCO-IETF-VDSL-LINE-MIB", "cvdslSCMConfProfileSymbolRateProfile"),
        ("CISCO-IETF-VDSL-LINE-MIB", "cvdslSCMConfProfileConstellationSize"),
        ("CISCO-IETF-VDSL-LINE-MIB", "cvdslSCMConfProfileCenterFrequency"),
        ("CISCO-IETF-VDSL-LINE-MIB", "cvdslSCMConfProfileRowStatus"))
)
if mibBuilder.loadTexts:
    cvdslSCMGroup.setStatus("current")


# Notification objects

cvdslInitFailureNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 0, 1)
)
cvdslInitFailureNotification.setObjects(
    ("CISCO-IETF-VDSL-LINE-MIB", "cvdslCurrStatus")
)
if mibBuilder.loadTexts:
    cvdslInitFailureNotification.setStatus(
        "current"
    )


# Notifications groups

cvdslNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 3, 1, 4)
)
cvdslNotificationGroup.setObjects(
    ("CISCO-IETF-VDSL-LINE-MIB", "cvdslInitFailureNotification")
)
if mibBuilder.loadTexts:
    cvdslNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

cvdslLineMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 3, 2, 1)
)
if mibBuilder.loadTexts:
    cvdslLineMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-IETF-VDSL-LINE-MIB",
    **{"CVdslLineCodingType": CVdslLineCodingType,
       "CVdslLineEntity": CVdslLineEntity,
       "ciscoIetfVdslMIB": ciscoIetfVdslMIB,
       "cvdslLineMib": cvdslLineMib,
       "cvdslNotifications": cvdslNotifications,
       "cvdslInitFailureNotification": cvdslInitFailureNotification,
       "cvdslMibObjects": cvdslMibObjects,
       "cvdslLineTable": cvdslLineTable,
       "cvdslLineEntry": cvdslLineEntry,
       "cvdslLineCoding": cvdslLineCoding,
       "cvdslLineType": cvdslLineType,
       "cvdslLineConfProfile": cvdslLineConfProfile,
       "cvdslLineAlarmConfProfile": cvdslLineAlarmConfProfile,
       "cvdslPhysTable": cvdslPhysTable,
       "cvdslPhysEntry": cvdslPhysEntry,
       "cvdslPhysSide": cvdslPhysSide,
       "cvdslInvSerialNumber": cvdslInvSerialNumber,
       "cvdslInvVendorID": cvdslInvVendorID,
       "cvdslInvVersionNumber": cvdslInvVersionNumber,
       "cvdslCurrSnrMgn": cvdslCurrSnrMgn,
       "cvdslCurrAtn": cvdslCurrAtn,
       "cvdslCurrStatus": cvdslCurrStatus,
       "cvdslCurrOutputPwr": cvdslCurrOutputPwr,
       "cvdslCurrAttainableRate": cvdslCurrAttainableRate,
       "cvdslChanTable": cvdslChanTable,
       "cvdslChanEntry": cvdslChanEntry,
       "cvdslChanInterleaveDelay": cvdslChanInterleaveDelay,
       "cvdslChanCrcBlockLength": cvdslChanCrcBlockLength,
       "cvdslLineConfProfileTable": cvdslLineConfProfileTable,
       "cvdslLineConfProfileEntry": cvdslLineConfProfileEntry,
       "cvdslLineConfProfileIndex": cvdslLineConfProfileIndex,
       "cvdslLineConfProfileName": cvdslLineConfProfileName,
       "cvdslLineConfTargetSnrMgn": cvdslLineConfTargetSnrMgn,
       "cvdslLineConfTxSpeed": cvdslLineConfTxSpeed,
       "cvdslLineConfRxSpeed": cvdslLineConfRxSpeed,
       "cvdslLineConfProfileRowStatus": cvdslLineConfProfileRowStatus,
       "cvdslLineMCMConfProfileTable": cvdslLineMCMConfProfileTable,
       "cvdslLineMCMConfProfileEntry": cvdslLineMCMConfProfileEntry,
       "cvdslMCMConfProfileTxWindowLength": cvdslMCMConfProfileTxWindowLength,
       "cvdslMCMConfProfileRowStatus": cvdslMCMConfProfileRowStatus,
       "cvdslLineMCMConfProfileTxBandTable": cvdslLineMCMConfProfileTxBandTable,
       "cvdslLineMCMConfProfileTxBandEntry": cvdslLineMCMConfProfileTxBandEntry,
       "cvdslMCMConfProfileTxBandNumber": cvdslMCMConfProfileTxBandNumber,
       "cvdslMCMConfProfileTxBandStart": cvdslMCMConfProfileTxBandStart,
       "cvdslMCMConfProfileTxBandStop": cvdslMCMConfProfileTxBandStop,
       "cvdslMCMConfProfileTxBandRowStatus": cvdslMCMConfProfileTxBandRowStatus,
       "cvdslLineMCMConfProfileRxBandTable": cvdslLineMCMConfProfileRxBandTable,
       "cvdslLineMCMConfProfileRxBandEntry": cvdslLineMCMConfProfileRxBandEntry,
       "cvdslMCMConfProfileRxBandNumber": cvdslMCMConfProfileRxBandNumber,
       "cvdslMCMConfProfileRxBandStart": cvdslMCMConfProfileRxBandStart,
       "cvdslMCMConfProfileRxBandStop": cvdslMCMConfProfileRxBandStop,
       "cvdslMCMConfProfileRxBandRowStatus": cvdslMCMConfProfileRxBandRowStatus,
       "cvdslLineMCMConfProfileTxPSDTable": cvdslLineMCMConfProfileTxPSDTable,
       "cvdslLineMCMConfProfileTxPSDEntry": cvdslLineMCMConfProfileTxPSDEntry,
       "cvdslMCMConfProfileTxPSDNumber": cvdslMCMConfProfileTxPSDNumber,
       "cvdslMCMConfProfileTxPSDTone": cvdslMCMConfProfileTxPSDTone,
       "cvdslMCMConfProfileTxPSDPSD": cvdslMCMConfProfileTxPSDPSD,
       "cvdslMCMConfProfileTxPSDRowStatus": cvdslMCMConfProfileTxPSDRowStatus,
       "cvdslLineMCMConfProfileMaxTxPSDTable": cvdslLineMCMConfProfileMaxTxPSDTable,
       "cvdslLineMCMConfProfileMaxTxPSDEntry": cvdslLineMCMConfProfileMaxTxPSDEntry,
       "cvdslMCMConfProfileMaxTxPSDNumber": cvdslMCMConfProfileMaxTxPSDNumber,
       "cvdslMCMConfProfileMaxTxPSDTone": cvdslMCMConfProfileMaxTxPSDTone,
       "cvdslMCMConfProfileMaxTxPSDPSD": cvdslMCMConfProfileMaxTxPSDPSD,
       "cvdslMCMConfProfileMaxTxPSDRowStatus": cvdslMCMConfProfileMaxTxPSDRowStatus,
       "cvdslLineMCMConfProfileMaxRxPSDTable": cvdslLineMCMConfProfileMaxRxPSDTable,
       "cvdslLineMCMConfProfileMaxRxPSDEntry": cvdslLineMCMConfProfileMaxRxPSDEntry,
       "cvdslMCMConfProfileMaxRxPSDNumber": cvdslMCMConfProfileMaxRxPSDNumber,
       "cvdslMCMConfProfileMaxRxPSDTone": cvdslMCMConfProfileMaxRxPSDTone,
       "cvdslMCMConfProfileMaxRxPSDPSD": cvdslMCMConfProfileMaxRxPSDPSD,
       "cvdslMCMConfProfileMaxRxPSDRowStatus": cvdslMCMConfProfileMaxRxPSDRowStatus,
       "cvdslLineSCMConfProfileTable": cvdslLineSCMConfProfileTable,
       "cvdslLineSCMConfProfileEntry": cvdslLineSCMConfProfileEntry,
       "cvdslSCMConfProfileInterleaveDepth": cvdslSCMConfProfileInterleaveDepth,
       "cvdslSCMConfProfileFastCodewordSize": cvdslSCMConfProfileFastCodewordSize,
       "cvdslSCMConfProfileTransmitPSDMask": cvdslSCMConfProfileTransmitPSDMask,
       "cvdslSCMConfProfileTransmitPSDLevel": cvdslSCMConfProfileTransmitPSDLevel,
       "cvdslSCMConfProfileSymbolRateProfile": cvdslSCMConfProfileSymbolRateProfile,
       "cvdslSCMConfProfileConstellationSize": cvdslSCMConfProfileConstellationSize,
       "cvdslSCMConfProfileCenterFrequency": cvdslSCMConfProfileCenterFrequency,
       "cvdslSCMConfProfileRowStatus": cvdslSCMConfProfileRowStatus,
       "cvdslLineAlarmConfProfileTable": cvdslLineAlarmConfProfileTable,
       "cvdslLineAlarmConfProfileEntry": cvdslLineAlarmConfProfileEntry,
       "cvdslLineAlarmConfProfileIndex": cvdslLineAlarmConfProfileIndex,
       "cvdslLineAlarmConfProfileName": cvdslLineAlarmConfProfileName,
       "cvdslInitFailureNotificationEnable": cvdslInitFailureNotificationEnable,
       "cvdslLineAlarmConfProfileRowStatus": cvdslLineAlarmConfProfileRowStatus,
       "cvdslConformance": cvdslConformance,
       "cvdslGroups": cvdslGroups,
       "cvdslGroup": cvdslGroup,
       "cvdslMCMGroup": cvdslMCMGroup,
       "cvdslSCMGroup": cvdslSCMGroup,
       "cvdslNotificationGroup": cvdslNotificationGroup,
       "cvdslCompliances": cvdslCompliances,
       "cvdslLineMibCompliance": cvdslLineMibCompliance}
)
