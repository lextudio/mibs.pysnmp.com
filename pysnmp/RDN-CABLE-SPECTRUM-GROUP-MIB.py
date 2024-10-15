# SNMP MIB module (RDN-CABLE-SPECTRUM-GROUP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RDN-CABLE-SPECTRUM-GROUP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:45:59 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(rdnCableSpectrumObjects,) = mibBuilder.importSymbols(
    "RDN-CABLE-SPECTRUM-MIB",
    "rdnCableSpectrumObjects")

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

(DateAndTime,
 DisplayString,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

rdnCableSpectrumGroup = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4981, 6, 1, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class SchedulingWeekDay(Integer32, TextualConvention):
    status = "current"
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("everyday", 8),
          ("friday", 6),
          ("monday", 2),
          ("saturday", 7),
          ("sunday", 1),
          ("thursday", 5),
          ("tuesday", 3),
          ("wednesday", 4))
    )



class SpectrumHopSelections(Integer32, TextualConvention):
    status = "current"
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
        *(("band", 2),
          ("channel-width", 6),
          ("frequency", 1),
          ("modulation-profile", 5),
          ("power-default", 3),
          ("power-level", 4))
    )



class SpecDataArray(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 400),
    )



# MIB Managed Objects in the order of their OIDs

_RdnSpectrumGroupTable_Object = MibTable
rdnSpectrumGroupTable = _RdnSpectrumGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 4981, 6, 1, 2, 1)
)
if mibBuilder.loadTexts:
    rdnSpectrumGroupTable.setStatus("current")
_RdnSpectrumGroupEntry_Object = MibTableRow
rdnSpectrumGroupEntry = _RdnSpectrumGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 4981, 6, 1, 2, 1, 1)
)
rdnSpectrumGroupEntry.setIndexNames(
    (0, "RDN-CABLE-SPECTRUM-GROUP-MIB", "rdnSpectrumGroupName"),
)
if mibBuilder.loadTexts:
    rdnSpectrumGroupEntry.setStatus("current")


class _RdnSpectrumGroupName_Type(DisplayString):
    """Custom type rdnSpectrumGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_RdnSpectrumGroupName_Type.__name__ = "DisplayString"
_RdnSpectrumGroupName_Object = MibTableColumn
rdnSpectrumGroupName = _RdnSpectrumGroupName_Object(
    (1, 3, 6, 1, 4, 1, 4981, 6, 1, 2, 1, 1, 1),
    _RdnSpectrumGroupName_Type()
)
rdnSpectrumGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnSpectrumGroupName.setStatus("current")
_RdnSpectrumGroupId_Type = Unsigned32
_RdnSpectrumGroupId_Object = MibTableColumn
rdnSpectrumGroupId = _RdnSpectrumGroupId_Object(
    (1, 3, 6, 1, 4, 1, 4981, 6, 1, 2, 1, 1, 2),
    _RdnSpectrumGroupId_Type()
)
rdnSpectrumGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnSpectrumGroupId.setStatus("current")


class _RdnSpectrumGroupHopPeriod_Type(Unsigned32):
    """Custom type rdnSpectrumGroupHopPeriod based on Unsigned32"""
    defaultValue = 300

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 3600),
    )


_RdnSpectrumGroupHopPeriod_Type.__name__ = "Unsigned32"
_RdnSpectrumGroupHopPeriod_Object = MibTableColumn
rdnSpectrumGroupHopPeriod = _RdnSpectrumGroupHopPeriod_Object(
    (1, 3, 6, 1, 4, 1, 4981, 6, 1, 2, 1, 1, 3),
    _RdnSpectrumGroupHopPeriod_Type()
)
rdnSpectrumGroupHopPeriod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rdnSpectrumGroupHopPeriod.setStatus("current")


class _RdnSpectrumGroupHopThresholdFlap_Type(Unsigned32):
    """Custom type rdnSpectrumGroupHopThresholdFlap based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RdnSpectrumGroupHopThresholdFlap_Type.__name__ = "Unsigned32"
_RdnSpectrumGroupHopThresholdFlap_Object = MibTableColumn
rdnSpectrumGroupHopThresholdFlap = _RdnSpectrumGroupHopThresholdFlap_Object(
    (1, 3, 6, 1, 4, 1, 4981, 6, 1, 2, 1, 1, 4),
    _RdnSpectrumGroupHopThresholdFlap_Type()
)
rdnSpectrumGroupHopThresholdFlap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rdnSpectrumGroupHopThresholdFlap.setStatus("current")


class _RdnSpectrumGroupHopThresholdError_Type(Unsigned32):
    """Custom type rdnSpectrumGroupHopThresholdError based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_RdnSpectrumGroupHopThresholdError_Type.__name__ = "Unsigned32"
_RdnSpectrumGroupHopThresholdError_Object = MibTableColumn
rdnSpectrumGroupHopThresholdError = _RdnSpectrumGroupHopThresholdError_Object(
    (1, 3, 6, 1, 4, 1, 4981, 6, 1, 2, 1, 1, 5),
    _RdnSpectrumGroupHopThresholdError_Type()
)
rdnSpectrumGroupHopThresholdError.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rdnSpectrumGroupHopThresholdError.setStatus("current")


class _RdnSpectrumGroupHopRollbackEnable_Type(Integer32):
    """Custom type rdnSpectrumGroupHopRollbackEnable based on Integer32"""
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


_RdnSpectrumGroupHopRollbackEnable_Type.__name__ = "Integer32"
_RdnSpectrumGroupHopRollbackEnable_Object = MibTableColumn
rdnSpectrumGroupHopRollbackEnable = _RdnSpectrumGroupHopRollbackEnable_Object(
    (1, 3, 6, 1, 4, 1, 4981, 6, 1, 2, 1, 1, 6),
    _RdnSpectrumGroupHopRollbackEnable_Type()
)
rdnSpectrumGroupHopRollbackEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rdnSpectrumGroupHopRollbackEnable.setStatus("current")


class _RdnSpectrumDataCollectResolution_Type(Unsigned32):
    """Custom type rdnSpectrumDataCollectResolution based on Unsigned32"""
    defaultValue = 200000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(200000, 400000),
    )


_RdnSpectrumDataCollectResolution_Type.__name__ = "Unsigned32"
_RdnSpectrumDataCollectResolution_Object = MibTableColumn
rdnSpectrumDataCollectResolution = _RdnSpectrumDataCollectResolution_Object(
    (1, 3, 6, 1, 4, 1, 4981, 6, 1, 2, 1, 1, 7),
    _RdnSpectrumDataCollectResolution_Type()
)
rdnSpectrumDataCollectResolution.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rdnSpectrumDataCollectResolution.setStatus("current")


class _RdnSpectrumDataCollectInterval_Type(Unsigned32):
    """Custom type rdnSpectrumDataCollectInterval based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(60, 65535),
    )


_RdnSpectrumDataCollectInterval_Type.__name__ = "Unsigned32"
_RdnSpectrumDataCollectInterval_Object = MibTableColumn
rdnSpectrumDataCollectInterval = _RdnSpectrumDataCollectInterval_Object(
    (1, 3, 6, 1, 4, 1, 4981, 6, 1, 2, 1, 1, 8),
    _RdnSpectrumDataCollectInterval_Type()
)
rdnSpectrumDataCollectInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rdnSpectrumDataCollectInterval.setStatus("current")


class _RdnSpectrumGroupGuardBand_Type(Unsigned32):
    """Custom type rdnSpectrumGroupGuardBand based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000000),
    )


_RdnSpectrumGroupGuardBand_Type.__name__ = "Unsigned32"
_RdnSpectrumGroupGuardBand_Object = MibTableColumn
rdnSpectrumGroupGuardBand = _RdnSpectrumGroupGuardBand_Object(
    (1, 3, 6, 1, 4, 1, 4981, 6, 1, 2, 1, 1, 9),
    _RdnSpectrumGroupGuardBand_Type()
)
rdnSpectrumGroupGuardBand.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rdnSpectrumGroupGuardBand.setStatus("current")
_RdnSpectrumGroupRowStatus_Type = RowStatus
_RdnSpectrumGroupRowStatus_Object = MibTableColumn
rdnSpectrumGroupRowStatus = _RdnSpectrumGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4981, 6, 1, 2, 1, 1, 10),
    _RdnSpectrumGroupRowStatus_Type()
)
rdnSpectrumGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rdnSpectrumGroupRowStatus.setStatus("current")
_RdnOfflineModemCount_Type = Integer32
_RdnOfflineModemCount_Object = MibTableColumn
rdnOfflineModemCount = _RdnOfflineModemCount_Object(
    (1, 3, 6, 1, 4, 1, 4981, 6, 1, 2, 1, 1, 11),
    _RdnOfflineModemCount_Type()
)
rdnOfflineModemCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnOfflineModemCount.setStatus("current")
_RdnOnlineModemCount_Type = Integer32
_RdnOnlineModemCount_Object = MibTableColumn
rdnOnlineModemCount = _RdnOnlineModemCount_Object(
    (1, 3, 6, 1, 4, 1, 4981, 6, 1, 2, 1, 1, 12),
    _RdnOnlineModemCount_Type()
)
rdnOnlineModemCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnOnlineModemCount.setStatus("current")
_RdnActiveModemCount_Type = Integer32
_RdnActiveModemCount_Object = MibTableColumn
rdnActiveModemCount = _RdnActiveModemCount_Object(
    (1, 3, 6, 1, 4, 1, 4981, 6, 1, 2, 1, 1, 13),
    _RdnActiveModemCount_Type()
)
rdnActiveModemCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnActiveModemCount.setStatus("current")
_RdnRegisteredModemCount_Type = Integer32
_RdnRegisteredModemCount_Object = MibTableColumn
rdnRegisteredModemCount = _RdnRegisteredModemCount_Object(
    (1, 3, 6, 1, 4, 1, 4981, 6, 1, 2, 1, 1, 14),
    _RdnRegisteredModemCount_Type()
)
rdnRegisteredModemCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnRegisteredModemCount.setStatus("current")
_RdnProvisionedModemCount_Type = Integer32
_RdnProvisionedModemCount_Object = MibTableColumn
rdnProvisionedModemCount = _RdnProvisionedModemCount_Object(
    (1, 3, 6, 1, 4, 1, 4981, 6, 1, 2, 1, 1, 15),
    _RdnProvisionedModemCount_Type()
)
rdnProvisionedModemCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnProvisionedModemCount.setStatus("current")
_RdnUnregisteredModemCount_Type = Integer32
_RdnUnregisteredModemCount_Object = MibTableColumn
rdnUnregisteredModemCount = _RdnUnregisteredModemCount_Object(
    (1, 3, 6, 1, 4, 1, 4981, 6, 1, 2, 1, 1, 16),
    _RdnUnregisteredModemCount_Type()
)
rdnUnregisteredModemCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnUnregisteredModemCount.setStatus("current")
_RdnSpectrumBandSchedTable_Object = MibTable
rdnSpectrumBandSchedTable = _RdnSpectrumBandSchedTable_Object(
    (1, 3, 6, 1, 4, 1, 4981, 6, 1, 2, 2)
)
if mibBuilder.loadTexts:
    rdnSpectrumBandSchedTable.setStatus("current")
_RdnSpectrumBandSchedEntry_Object = MibTableRow
rdnSpectrumBandSchedEntry = _RdnSpectrumBandSchedEntry_Object(
    (1, 3, 6, 1, 4, 1, 4981, 6, 1, 2, 2, 1)
)
rdnSpectrumBandSchedEntry.setIndexNames(
    (0, "RDN-CABLE-SPECTRUM-GROUP-MIB", "rdnSpectrumGroupId"),
    (0, "RDN-CABLE-SPECTRUM-GROUP-MIB", "rdnSpectrumBandSchedId"),
    (0, "RDN-CABLE-SPECTRUM-GROUP-MIB", "rdnSpectrumBandSchedAction"),
)
if mibBuilder.loadTexts:
    rdnSpectrumBandSchedEntry.setStatus("current")
_RdnSpectrumBandSchedId_Type = Unsigned32
_RdnSpectrumBandSchedId_Object = MibTableColumn
rdnSpectrumBandSchedId = _RdnSpectrumBandSchedId_Object(
    (1, 3, 6, 1, 4, 1, 4981, 6, 1, 2, 2, 1, 1),
    _RdnSpectrumBandSchedId_Type()
)
rdnSpectrumBandSchedId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rdnSpectrumBandSchedId.setStatus("current")
_RdnSpectrumBandSchedAction_Type = Unsigned32
_RdnSpectrumBandSchedAction_Object = MibTableColumn
rdnSpectrumBandSchedAction = _RdnSpectrumBandSchedAction_Object(
    (1, 3, 6, 1, 4, 1, 4981, 6, 1, 2, 2, 1, 2),
    _RdnSpectrumBandSchedAction_Type()
)
rdnSpectrumBandSchedAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnSpectrumBandSchedAction.setStatus("current")


class _RdnSpectrumBandFreqLow_Type(Unsigned32):
    """Custom type rdnSpectrumBandFreqLow based on Unsigned32"""
    defaultValue = 5000000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5000000, 65000000),
    )


_RdnSpectrumBandFreqLow_Type.__name__ = "Unsigned32"
_RdnSpectrumBandFreqLow_Object = MibTableColumn
rdnSpectrumBandFreqLow = _RdnSpectrumBandFreqLow_Object(
    (1, 3, 6, 1, 4, 1, 4981, 6, 1, 2, 2, 1, 3),
    _RdnSpectrumBandFreqLow_Type()
)
rdnSpectrumBandFreqLow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rdnSpectrumBandFreqLow.setStatus("current")


class _RdnSpectrumBandFreqHigh_Type(Unsigned32):
    """Custom type rdnSpectrumBandFreqHigh based on Unsigned32"""
    defaultValue = 42000000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5000000, 65000000),
    )


_RdnSpectrumBandFreqHigh_Type.__name__ = "Unsigned32"
_RdnSpectrumBandFreqHigh_Object = MibTableColumn
rdnSpectrumBandFreqHigh = _RdnSpectrumBandFreqHigh_Object(
    (1, 3, 6, 1, 4, 1, 4981, 6, 1, 2, 2, 1, 4),
    _RdnSpectrumBandFreqHigh_Type()
)
rdnSpectrumBandFreqHigh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rdnSpectrumBandFreqHigh.setStatus("current")


class _RdnSpectrumBandSchedWeekDay_Type(SchedulingWeekDay):
    """Custom type rdnSpectrumBandSchedWeekDay based on SchedulingWeekDay"""


_RdnSpectrumBandSchedWeekDay_Object = MibTableColumn
rdnSpectrumBandSchedWeekDay = _RdnSpectrumBandSchedWeekDay_Object(
    (1, 3, 6, 1, 4, 1, 4981, 6, 1, 2, 2, 1, 5),
    _RdnSpectrumBandSchedWeekDay_Type()
)
rdnSpectrumBandSchedWeekDay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rdnSpectrumBandSchedWeekDay.setStatus("current")


class _RdnSpectrumBandSchedHour_Type(Unsigned32):
    """Custom type rdnSpectrumBandSchedHour based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_RdnSpectrumBandSchedHour_Type.__name__ = "Unsigned32"
_RdnSpectrumBandSchedHour_Object = MibTableColumn
rdnSpectrumBandSchedHour = _RdnSpectrumBandSchedHour_Object(
    (1, 3, 6, 1, 4, 1, 4981, 6, 1, 2, 2, 1, 6),
    _RdnSpectrumBandSchedHour_Type()
)
rdnSpectrumBandSchedHour.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rdnSpectrumBandSchedHour.setStatus("current")


class _RdnSpectrumBandSchedMinute_Type(Unsigned32):
    """Custom type rdnSpectrumBandSchedMinute based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_RdnSpectrumBandSchedMinute_Type.__name__ = "Unsigned32"
_RdnSpectrumBandSchedMinute_Object = MibTableColumn
rdnSpectrumBandSchedMinute = _RdnSpectrumBandSchedMinute_Object(
    (1, 3, 6, 1, 4, 1, 4981, 6, 1, 2, 2, 1, 7),
    _RdnSpectrumBandSchedMinute_Type()
)
rdnSpectrumBandSchedMinute.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rdnSpectrumBandSchedMinute.setStatus("current")


class _RdnSpectrumBandSchedSecond_Type(Unsigned32):
    """Custom type rdnSpectrumBandSchedSecond based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_RdnSpectrumBandSchedSecond_Type.__name__ = "Unsigned32"
_RdnSpectrumBandSchedSecond_Object = MibTableColumn
rdnSpectrumBandSchedSecond = _RdnSpectrumBandSchedSecond_Object(
    (1, 3, 6, 1, 4, 1, 4981, 6, 1, 2, 2, 1, 8),
    _RdnSpectrumBandSchedSecond_Type()
)
rdnSpectrumBandSchedSecond.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rdnSpectrumBandSchedSecond.setStatus("current")
_RdnSpectrumBandSchedRowStatus_Type = RowStatus
_RdnSpectrumBandSchedRowStatus_Object = MibTableColumn
rdnSpectrumBandSchedRowStatus = _RdnSpectrumBandSchedRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4981, 6, 1, 2, 2, 1, 9),
    _RdnSpectrumBandSchedRowStatus_Type()
)
rdnSpectrumBandSchedRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rdnSpectrumBandSchedRowStatus.setStatus("current")
_RdnSpectrumHopTable_Object = MibTable
rdnSpectrumHopTable = _RdnSpectrumHopTable_Object(
    (1, 3, 6, 1, 4, 1, 4981, 6, 1, 2, 3)
)
if mibBuilder.loadTexts:
    rdnSpectrumHopTable.setStatus("current")
_RdnSpectrumHopEntry_Object = MibTableRow
rdnSpectrumHopEntry = _RdnSpectrumHopEntry_Object(
    (1, 3, 6, 1, 4, 1, 4981, 6, 1, 2, 3, 1)
)
rdnSpectrumHopEntry.setIndexNames(
    (0, "RDN-CABLE-SPECTRUM-GROUP-MIB", "rdnSpectrumGroupId"),
    (0, "RDN-CABLE-SPECTRUM-GROUP-MIB", "rdnSpectrumHopId"),
)
if mibBuilder.loadTexts:
    rdnSpectrumHopEntry.setStatus("current")
_RdnSpectrumHopId_Type = Unsigned32
_RdnSpectrumHopId_Object = MibTableColumn
rdnSpectrumHopId = _RdnSpectrumHopId_Object(
    (1, 3, 6, 1, 4, 1, 4981, 6, 1, 2, 3, 1, 1),
    _RdnSpectrumHopId_Type()
)
rdnSpectrumHopId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rdnSpectrumHopId.setStatus("current")


class _RdnSpectrumHopSelection_Type(SpectrumHopSelections):
    """Custom type rdnSpectrumHopSelection based on SpectrumHopSelections"""


_RdnSpectrumHopSelection_Object = MibTableColumn
rdnSpectrumHopSelection = _RdnSpectrumHopSelection_Object(
    (1, 3, 6, 1, 4, 1, 4981, 6, 1, 2, 3, 1, 2),
    _RdnSpectrumHopSelection_Type()
)
rdnSpectrumHopSelection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rdnSpectrumHopSelection.setStatus("current")


class _RdnSpectrumHopPriority_Type(Integer32):
    """Custom type rdnSpectrumHopPriority based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_RdnSpectrumHopPriority_Type.__name__ = "Integer32"
_RdnSpectrumHopPriority_Object = MibTableColumn
rdnSpectrumHopPriority = _RdnSpectrumHopPriority_Object(
    (1, 3, 6, 1, 4, 1, 4981, 6, 1, 2, 3, 1, 3),
    _RdnSpectrumHopPriority_Type()
)
rdnSpectrumHopPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rdnSpectrumHopPriority.setStatus("current")


class _RdnSpectrumHopFrequency_Type(Unsigned32):
    """Custom type rdnSpectrumHopFrequency based on Unsigned32"""
    defaultValue = 10000000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5000000, 65000000),
    )


_RdnSpectrumHopFrequency_Type.__name__ = "Unsigned32"
_RdnSpectrumHopFrequency_Object = MibTableColumn
rdnSpectrumHopFrequency = _RdnSpectrumHopFrequency_Object(
    (1, 3, 6, 1, 4, 1, 4981, 6, 1, 2, 3, 1, 4),
    _RdnSpectrumHopFrequency_Type()
)
rdnSpectrumHopFrequency.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rdnSpectrumHopFrequency.setStatus("current")


class _RdnSpectrumHopBandLow_Type(Unsigned32):
    """Custom type rdnSpectrumHopBandLow based on Unsigned32"""
    defaultValue = 8400000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5000000, 65000000),
    )


_RdnSpectrumHopBandLow_Type.__name__ = "Unsigned32"
_RdnSpectrumHopBandLow_Object = MibTableColumn
rdnSpectrumHopBandLow = _RdnSpectrumHopBandLow_Object(
    (1, 3, 6, 1, 4, 1, 4981, 6, 1, 2, 3, 1, 5),
    _RdnSpectrumHopBandLow_Type()
)
rdnSpectrumHopBandLow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rdnSpectrumHopBandLow.setStatus("current")


class _RdnSpectrumHopBandHigh_Type(Unsigned32):
    """Custom type rdnSpectrumHopBandHigh based on Unsigned32"""
    defaultValue = 42000000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5000000, 65000000),
    )


_RdnSpectrumHopBandHigh_Type.__name__ = "Unsigned32"
_RdnSpectrumHopBandHigh_Object = MibTableColumn
rdnSpectrumHopBandHigh = _RdnSpectrumHopBandHigh_Object(
    (1, 3, 6, 1, 4, 1, 4981, 6, 1, 2, 3, 1, 6),
    _RdnSpectrumHopBandHigh_Type()
)
rdnSpectrumHopBandHigh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rdnSpectrumHopBandHigh.setStatus("current")


class _RdnSpectrumHopChannelWidth_Type(Integer32):
    """Custom type rdnSpectrumHopChannelWidth based on Integer32"""
    defaultValue = 3200000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(200000,
              400000,
              800000,
              1600000,
              3200000)
        )
    )
    namedValues = NamedValues(
        *(("channel-width1", 200000),
          ("channel-width2", 400000),
          ("channel-width3", 800000),
          ("channel-width4", 1600000),
          ("channel-width5", 3200000))
    )


_RdnSpectrumHopChannelWidth_Type.__name__ = "Integer32"
_RdnSpectrumHopChannelWidth_Object = MibTableColumn
rdnSpectrumHopChannelWidth = _RdnSpectrumHopChannelWidth_Object(
    (1, 3, 6, 1, 4, 1, 4981, 6, 1, 2, 3, 1, 7),
    _RdnSpectrumHopChannelWidth_Type()
)
rdnSpectrumHopChannelWidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rdnSpectrumHopChannelWidth.setStatus("current")


class _RdnSpectrumHopPowerLevel_Type(Integer32):
    """Custom type rdnSpectrumHopPowerLevel based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-160, 260),
    )


_RdnSpectrumHopPowerLevel_Type.__name__ = "Integer32"
_RdnSpectrumHopPowerLevel_Object = MibTableColumn
rdnSpectrumHopPowerLevel = _RdnSpectrumHopPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 4981, 6, 1, 2, 3, 1, 8),
    _RdnSpectrumHopPowerLevel_Type()
)
rdnSpectrumHopPowerLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rdnSpectrumHopPowerLevel.setStatus("current")


class _RdnSpectrumHopModulationProfile_Type(Integer32):
    """Custom type rdnSpectrumHopModulationProfile based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_RdnSpectrumHopModulationProfile_Type.__name__ = "Integer32"
_RdnSpectrumHopModulationProfile_Object = MibTableColumn
rdnSpectrumHopModulationProfile = _RdnSpectrumHopModulationProfile_Object(
    (1, 3, 6, 1, 4, 1, 4981, 6, 1, 2, 3, 1, 9),
    _RdnSpectrumHopModulationProfile_Type()
)
rdnSpectrumHopModulationProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rdnSpectrumHopModulationProfile.setStatus("current")
_RdnSpectrumHopRowStatus_Type = RowStatus
_RdnSpectrumHopRowStatus_Object = MibTableColumn
rdnSpectrumHopRowStatus = _RdnSpectrumHopRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4981, 6, 1, 2, 3, 1, 10),
    _RdnSpectrumHopRowStatus_Type()
)
rdnSpectrumHopRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rdnSpectrumHopRowStatus.setStatus("current")
_RdnSpectrumMemberChannelTable_Object = MibTable
rdnSpectrumMemberChannelTable = _RdnSpectrumMemberChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 4981, 6, 1, 2, 4)
)
if mibBuilder.loadTexts:
    rdnSpectrumMemberChannelTable.setStatus("current")
_RdnSpectrumMemberChannelEntry_Object = MibTableRow
rdnSpectrumMemberChannelEntry = _RdnSpectrumMemberChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 4981, 6, 1, 2, 4, 1)
)
rdnSpectrumMemberChannelEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    rdnSpectrumMemberChannelEntry.setStatus("current")
_RdnUsChannelId_Type = Integer32
_RdnUsChannelId_Object = MibTableColumn
rdnUsChannelId = _RdnUsChannelId_Object(
    (1, 3, 6, 1, 4, 1, 4981, 6, 1, 2, 4, 1, 1),
    _RdnUsChannelId_Type()
)
rdnUsChannelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnUsChannelId.setStatus("current")


class _RdnMemChSpectrumGroupId_Type(Unsigned32):
    """Custom type rdnMemChSpectrumGroupId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RdnMemChSpectrumGroupId_Type.__name__ = "Unsigned32"
_RdnMemChSpectrumGroupId_Object = MibTableColumn
rdnMemChSpectrumGroupId = _RdnMemChSpectrumGroupId_Object(
    (1, 3, 6, 1, 4, 1, 4981, 6, 1, 2, 4, 1, 2),
    _RdnMemChSpectrumGroupId_Type()
)
rdnMemChSpectrumGroupId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdnMemChSpectrumGroupId.setStatus("current")
_RdnMemChSpectrumGroupName_Type = DisplayString
_RdnMemChSpectrumGroupName_Object = MibTableColumn
rdnMemChSpectrumGroupName = _RdnMemChSpectrumGroupName_Object(
    (1, 3, 6, 1, 4, 1, 4981, 6, 1, 2, 4, 1, 3),
    _RdnMemChSpectrumGroupName_Type()
)
rdnMemChSpectrumGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnMemChSpectrumGroupName.setStatus("current")
_RdnSpectrumDataTable_Object = MibTable
rdnSpectrumDataTable = _RdnSpectrumDataTable_Object(
    (1, 3, 6, 1, 4, 1, 4981, 6, 1, 2, 5)
)
if mibBuilder.loadTexts:
    rdnSpectrumDataTable.setStatus("current")
_RdnSpectrumDataEntry_Object = MibTableRow
rdnSpectrumDataEntry = _RdnSpectrumDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 4981, 6, 1, 2, 5, 1)
)
rdnSpectrumDataEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    rdnSpectrumDataEntry.setStatus("current")
_RdnSpectrumDataIndex_Type = Integer32
_RdnSpectrumDataIndex_Object = MibTableColumn
rdnSpectrumDataIndex = _RdnSpectrumDataIndex_Object(
    (1, 3, 6, 1, 4, 1, 4981, 6, 1, 2, 5, 1, 1),
    _RdnSpectrumDataIndex_Type()
)
rdnSpectrumDataIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnSpectrumDataIndex.setStatus("current")
_RdnSpecDataUsChannelId_Type = Integer32
_RdnSpecDataUsChannelId_Object = MibTableColumn
rdnSpecDataUsChannelId = _RdnSpecDataUsChannelId_Object(
    (1, 3, 6, 1, 4, 1, 4981, 6, 1, 2, 5, 1, 2),
    _RdnSpecDataUsChannelId_Type()
)
rdnSpecDataUsChannelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnSpecDataUsChannelId.setStatus("current")
_RdnSpectrumDataStartFrequency_Type = Unsigned32
_RdnSpectrumDataStartFrequency_Object = MibTableColumn
rdnSpectrumDataStartFrequency = _RdnSpectrumDataStartFrequency_Object(
    (1, 3, 6, 1, 4, 1, 4981, 6, 1, 2, 5, 1, 3),
    _RdnSpectrumDataStartFrequency_Type()
)
rdnSpectrumDataStartFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnSpectrumDataStartFrequency.setStatus("current")
_RdnSpectrumDataResolution_Type = Integer32
_RdnSpectrumDataResolution_Object = MibTableColumn
rdnSpectrumDataResolution = _RdnSpectrumDataResolution_Object(
    (1, 3, 6, 1, 4, 1, 4981, 6, 1, 2, 5, 1, 4),
    _RdnSpectrumDataResolution_Type()
)
rdnSpectrumDataResolution.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnSpectrumDataResolution.setStatus("current")
_RdnSpectrumDataSamples_Type = Integer32
_RdnSpectrumDataSamples_Object = MibTableColumn
rdnSpectrumDataSamples = _RdnSpectrumDataSamples_Object(
    (1, 3, 6, 1, 4, 1, 4981, 6, 1, 2, 5, 1, 5),
    _RdnSpectrumDataSamples_Type()
)
rdnSpectrumDataSamples.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnSpectrumDataSamples.setStatus("current")
_RdnSpectrumDataLastUpdate_Type = DateAndTime
_RdnSpectrumDataLastUpdate_Object = MibTableColumn
rdnSpectrumDataLastUpdate = _RdnSpectrumDataLastUpdate_Object(
    (1, 3, 6, 1, 4, 1, 4981, 6, 1, 2, 5, 1, 6),
    _RdnSpectrumDataLastUpdate_Type()
)
rdnSpectrumDataLastUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnSpectrumDataLastUpdate.setStatus("current")


class _RdnSpectrumDataArray_Type(SpecDataArray):
    """Custom type rdnSpectrumDataArray based on SpecDataArray"""
    subtypeSpec = SpecDataArray.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 400),
    )


_RdnSpectrumDataArray_Type.__name__ = "SpecDataArray"
_RdnSpectrumDataArray_Object = MibTableColumn
rdnSpectrumDataArray = _RdnSpectrumDataArray_Object(
    (1, 3, 6, 1, 4, 1, 4981, 6, 1, 2, 5, 1, 7),
    _RdnSpectrumDataArray_Type()
)
rdnSpectrumDataArray.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnSpectrumDataArray.setStatus("current")
_RdnSpectrumQualityTable_Object = MibTable
rdnSpectrumQualityTable = _RdnSpectrumQualityTable_Object(
    (1, 3, 6, 1, 4, 1, 4981, 6, 1, 2, 6)
)
if mibBuilder.loadTexts:
    rdnSpectrumQualityTable.setStatus("current")
_RdnSpectrumQualityEntry_Object = MibTableRow
rdnSpectrumQualityEntry = _RdnSpectrumQualityEntry_Object(
    (1, 3, 6, 1, 4, 1, 4981, 6, 1, 2, 6, 1)
)
rdnSpectrumQualityEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    rdnSpectrumQualityEntry.setStatus("current")
_RdnSpecQualityUsChId_Type = Integer32
_RdnSpecQualityUsChId_Object = MibTableColumn
rdnSpecQualityUsChId = _RdnSpecQualityUsChId_Object(
    (1, 3, 6, 1, 4, 1, 4981, 6, 1, 2, 6, 1, 1),
    _RdnSpecQualityUsChId_Type()
)
rdnSpecQualityUsChId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnSpecQualityUsChId.setStatus("current")
_RdnSpectrumQualityDataLastUpdate_Type = DateAndTime
_RdnSpectrumQualityDataLastUpdate_Object = MibTableColumn
rdnSpectrumQualityDataLastUpdate = _RdnSpectrumQualityDataLastUpdate_Object(
    (1, 3, 6, 1, 4, 1, 4981, 6, 1, 2, 6, 1, 2),
    _RdnSpectrumQualityDataLastUpdate_Type()
)
rdnSpectrumQualityDataLastUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnSpectrumQualityDataLastUpdate.setStatus("current")
_RdnSpectrumDataInBandPower_Type = Integer32
_RdnSpectrumDataInBandPower_Object = MibTableColumn
rdnSpectrumDataInBandPower = _RdnSpectrumDataInBandPower_Object(
    (1, 3, 6, 1, 4, 1, 4981, 6, 1, 2, 6, 1, 3),
    _RdnSpectrumDataInBandPower_Type()
)
rdnSpectrumDataInBandPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnSpectrumDataInBandPower.setStatus("current")
_RdnSpectrumTotCodeWord_Type = Unsigned32
_RdnSpectrumTotCodeWord_Object = MibTableColumn
rdnSpectrumTotCodeWord = _RdnSpectrumTotCodeWord_Object(
    (1, 3, 6, 1, 4, 1, 4981, 6, 1, 2, 6, 1, 4),
    _RdnSpectrumTotCodeWord_Type()
)
rdnSpectrumTotCodeWord.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnSpectrumTotCodeWord.setStatus("current")
_RdnSpectrumErrorCodeWord_Type = Unsigned32
_RdnSpectrumErrorCodeWord_Object = MibTableColumn
rdnSpectrumErrorCodeWord = _RdnSpectrumErrorCodeWord_Object(
    (1, 3, 6, 1, 4, 1, 4981, 6, 1, 2, 6, 1, 5),
    _RdnSpectrumErrorCodeWord_Type()
)
rdnSpectrumErrorCodeWord.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnSpectrumErrorCodeWord.setStatus("current")
_RdnSpectrumMapTable_Object = MibTable
rdnSpectrumMapTable = _RdnSpectrumMapTable_Object(
    (1, 3, 6, 1, 4, 1, 4981, 6, 1, 2, 7)
)
if mibBuilder.loadTexts:
    rdnSpectrumMapTable.setStatus("current")
_RdnSpectrumMapEntry_Object = MibTableRow
rdnSpectrumMapEntry = _RdnSpectrumMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 4981, 6, 1, 2, 7, 1)
)
rdnSpectrumMapEntry.setIndexNames(
    (0, "RDN-CABLE-SPECTRUM-GROUP-MIB", "rdnSpectrumGroupId"),
    (0, "RDN-CABLE-SPECTRUM-GROUP-MIB", "rdnSpectrumMapIndex"),
)
if mibBuilder.loadTexts:
    rdnSpectrumMapEntry.setStatus("current")
_RdnSpectrumMapIndex_Type = Integer32
_RdnSpectrumMapIndex_Object = MibTableColumn
rdnSpectrumMapIndex = _RdnSpectrumMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 4981, 6, 1, 2, 7, 1, 1),
    _RdnSpectrumMapIndex_Type()
)
rdnSpectrumMapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rdnSpectrumMapIndex.setStatus("current")
_RdnSpectrumMapStartFrequency_Type = Unsigned32
_RdnSpectrumMapStartFrequency_Object = MibTableColumn
rdnSpectrumMapStartFrequency = _RdnSpectrumMapStartFrequency_Object(
    (1, 3, 6, 1, 4, 1, 4981, 6, 1, 2, 7, 1, 2),
    _RdnSpectrumMapStartFrequency_Type()
)
rdnSpectrumMapStartFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnSpectrumMapStartFrequency.setStatus("current")
_RdnSpectrumMapStopFrequency_Type = Unsigned32
_RdnSpectrumMapStopFrequency_Object = MibTableColumn
rdnSpectrumMapStopFrequency = _RdnSpectrumMapStopFrequency_Object(
    (1, 3, 6, 1, 4, 1, 4981, 6, 1, 2, 7, 1, 3),
    _RdnSpectrumMapStopFrequency_Type()
)
rdnSpectrumMapStopFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnSpectrumMapStopFrequency.setStatus("current")
_RdnSpectrumMapStatus_Type = Integer32
_RdnSpectrumMapStatus_Object = MibTableColumn
rdnSpectrumMapStatus = _RdnSpectrumMapStatus_Object(
    (1, 3, 6, 1, 4, 1, 4981, 6, 1, 2, 7, 1, 4),
    _RdnSpectrumMapStatus_Type()
)
rdnSpectrumMapStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnSpectrumMapStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RDN-CABLE-SPECTRUM-GROUP-MIB",
    **{"SchedulingWeekDay": SchedulingWeekDay,
       "SpectrumHopSelections": SpectrumHopSelections,
       "SpecDataArray": SpecDataArray,
       "rdnCableSpectrumGroup": rdnCableSpectrumGroup,
       "rdnSpectrumGroupTable": rdnSpectrumGroupTable,
       "rdnSpectrumGroupEntry": rdnSpectrumGroupEntry,
       "rdnSpectrumGroupName": rdnSpectrumGroupName,
       "rdnSpectrumGroupId": rdnSpectrumGroupId,
       "rdnSpectrumGroupHopPeriod": rdnSpectrumGroupHopPeriod,
       "rdnSpectrumGroupHopThresholdFlap": rdnSpectrumGroupHopThresholdFlap,
       "rdnSpectrumGroupHopThresholdError": rdnSpectrumGroupHopThresholdError,
       "rdnSpectrumGroupHopRollbackEnable": rdnSpectrumGroupHopRollbackEnable,
       "rdnSpectrumDataCollectResolution": rdnSpectrumDataCollectResolution,
       "rdnSpectrumDataCollectInterval": rdnSpectrumDataCollectInterval,
       "rdnSpectrumGroupGuardBand": rdnSpectrumGroupGuardBand,
       "rdnSpectrumGroupRowStatus": rdnSpectrumGroupRowStatus,
       "rdnOfflineModemCount": rdnOfflineModemCount,
       "rdnOnlineModemCount": rdnOnlineModemCount,
       "rdnActiveModemCount": rdnActiveModemCount,
       "rdnRegisteredModemCount": rdnRegisteredModemCount,
       "rdnProvisionedModemCount": rdnProvisionedModemCount,
       "rdnUnregisteredModemCount": rdnUnregisteredModemCount,
       "rdnSpectrumBandSchedTable": rdnSpectrumBandSchedTable,
       "rdnSpectrumBandSchedEntry": rdnSpectrumBandSchedEntry,
       "rdnSpectrumBandSchedId": rdnSpectrumBandSchedId,
       "rdnSpectrumBandSchedAction": rdnSpectrumBandSchedAction,
       "rdnSpectrumBandFreqLow": rdnSpectrumBandFreqLow,
       "rdnSpectrumBandFreqHigh": rdnSpectrumBandFreqHigh,
       "rdnSpectrumBandSchedWeekDay": rdnSpectrumBandSchedWeekDay,
       "rdnSpectrumBandSchedHour": rdnSpectrumBandSchedHour,
       "rdnSpectrumBandSchedMinute": rdnSpectrumBandSchedMinute,
       "rdnSpectrumBandSchedSecond": rdnSpectrumBandSchedSecond,
       "rdnSpectrumBandSchedRowStatus": rdnSpectrumBandSchedRowStatus,
       "rdnSpectrumHopTable": rdnSpectrumHopTable,
       "rdnSpectrumHopEntry": rdnSpectrumHopEntry,
       "rdnSpectrumHopId": rdnSpectrumHopId,
       "rdnSpectrumHopSelection": rdnSpectrumHopSelection,
       "rdnSpectrumHopPriority": rdnSpectrumHopPriority,
       "rdnSpectrumHopFrequency": rdnSpectrumHopFrequency,
       "rdnSpectrumHopBandLow": rdnSpectrumHopBandLow,
       "rdnSpectrumHopBandHigh": rdnSpectrumHopBandHigh,
       "rdnSpectrumHopChannelWidth": rdnSpectrumHopChannelWidth,
       "rdnSpectrumHopPowerLevel": rdnSpectrumHopPowerLevel,
       "rdnSpectrumHopModulationProfile": rdnSpectrumHopModulationProfile,
       "rdnSpectrumHopRowStatus": rdnSpectrumHopRowStatus,
       "rdnSpectrumMemberChannelTable": rdnSpectrumMemberChannelTable,
       "rdnSpectrumMemberChannelEntry": rdnSpectrumMemberChannelEntry,
       "rdnUsChannelId": rdnUsChannelId,
       "rdnMemChSpectrumGroupId": rdnMemChSpectrumGroupId,
       "rdnMemChSpectrumGroupName": rdnMemChSpectrumGroupName,
       "rdnSpectrumDataTable": rdnSpectrumDataTable,
       "rdnSpectrumDataEntry": rdnSpectrumDataEntry,
       "rdnSpectrumDataIndex": rdnSpectrumDataIndex,
       "rdnSpecDataUsChannelId": rdnSpecDataUsChannelId,
       "rdnSpectrumDataStartFrequency": rdnSpectrumDataStartFrequency,
       "rdnSpectrumDataResolution": rdnSpectrumDataResolution,
       "rdnSpectrumDataSamples": rdnSpectrumDataSamples,
       "rdnSpectrumDataLastUpdate": rdnSpectrumDataLastUpdate,
       "rdnSpectrumDataArray": rdnSpectrumDataArray,
       "rdnSpectrumQualityTable": rdnSpectrumQualityTable,
       "rdnSpectrumQualityEntry": rdnSpectrumQualityEntry,
       "rdnSpecQualityUsChId": rdnSpecQualityUsChId,
       "rdnSpectrumQualityDataLastUpdate": rdnSpectrumQualityDataLastUpdate,
       "rdnSpectrumDataInBandPower": rdnSpectrumDataInBandPower,
       "rdnSpectrumTotCodeWord": rdnSpectrumTotCodeWord,
       "rdnSpectrumErrorCodeWord": rdnSpectrumErrorCodeWord,
       "rdnSpectrumMapTable": rdnSpectrumMapTable,
       "rdnSpectrumMapEntry": rdnSpectrumMapEntry,
       "rdnSpectrumMapIndex": rdnSpectrumMapIndex,
       "rdnSpectrumMapStartFrequency": rdnSpectrumMapStartFrequency,
       "rdnSpectrumMapStopFrequency": rdnSpectrumMapStopFrequency,
       "rdnSpectrumMapStatus": rdnSpectrumMapStatus}
)
