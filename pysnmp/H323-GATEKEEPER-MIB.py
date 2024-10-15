# SNMP MIB module (H323-GATEKEEPER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/H323-GATEKEEPER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:49:42 2024
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

(MmControlsCommands,
 MmErrorProbableCause,
 MmErrorSeverity,
 MmGatekeeperID,
 MmTAddressTag,
 mmH323Root) = mibBuilder.importSymbols(
    "MULTI-MEDIA-MIB-TC",
    "MmControlsCommands",
    "MmErrorProbableCause",
    "MmErrorSeverity",
    "MmGatekeeperID",
    "MmTAddressTag",
    "mmH323Root")

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

(DateAndTime,
 DisplayString,
 RowStatus,
 TAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "TAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

h323Gatekeeper = ModuleIdentity(
    (0, 0, 8, 341, 1, 1, 6)
)
h323Gatekeeper.setRevisions(
        ("1998-05-10 12:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H323GatekeeperZone_ObjectIdentity = ObjectIdentity
h323GatekeeperZone = _H323GatekeeperZone_ObjectIdentity(
    (0, 0, 8, 341, 1, 1, 6, 1)
)
_H323ZoneTable_Object = MibTable
h323ZoneTable = _H323ZoneTable_Object(
    (0, 0, 8, 341, 1, 1, 6, 1, 1)
)
if mibBuilder.loadTexts:
    h323ZoneTable.setStatus("current")
_H323ZoneEntry_Object = MibTableRow
h323ZoneEntry = _H323ZoneEntry_Object(
    (0, 0, 8, 341, 1, 1, 6, 1, 1, 1)
)
h323ZoneEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "H323-GATEKEEPER-MIB", "h323ZoneIndex"),
)
if mibBuilder.loadTexts:
    h323ZoneEntry.setStatus("current")
_H323ZoneIndex_Type = Integer32
_H323ZoneIndex_Object = MibTableColumn
h323ZoneIndex = _H323ZoneIndex_Object(
    (0, 0, 8, 341, 1, 1, 6, 1, 1, 1, 1),
    _H323ZoneIndex_Type()
)
h323ZoneIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h323ZoneIndex.setStatus("current")
_H323ZoneZoneName_Type = MmGatekeeperID
_H323ZoneZoneName_Object = MibTableColumn
h323ZoneZoneName = _H323ZoneZoneName_Object(
    (0, 0, 8, 341, 1, 1, 6, 1, 1, 1, 2),
    _H323ZoneZoneName_Type()
)
h323ZoneZoneName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h323ZoneZoneName.setStatus("current")


class _H323ZoneRasSignalAddressTag_Type(MmTAddressTag):
    """Custom type h323ZoneRasSignalAddressTag based on MmTAddressTag"""


_H323ZoneRasSignalAddressTag_Object = MibTableColumn
h323ZoneRasSignalAddressTag = _H323ZoneRasSignalAddressTag_Object(
    (0, 0, 8, 341, 1, 1, 6, 1, 1, 1, 3),
    _H323ZoneRasSignalAddressTag_Type()
)
h323ZoneRasSignalAddressTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h323ZoneRasSignalAddressTag.setStatus("current")


class _H323ZoneRasSignalAddress_Type(TAddress):
    """Custom type h323ZoneRasSignalAddress based on TAddress"""
    defaultHexValue = "00000000"


_H323ZoneRasSignalAddress_Object = MibTableColumn
h323ZoneRasSignalAddress = _H323ZoneRasSignalAddress_Object(
    (0, 0, 8, 341, 1, 1, 6, 1, 1, 1, 4),
    _H323ZoneRasSignalAddress_Type()
)
h323ZoneRasSignalAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h323ZoneRasSignalAddress.setStatus("current")


class _H323ZoneMaxBandwidth_Type(Unsigned32):
    """Custom type h323ZoneMaxBandwidth based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_H323ZoneMaxBandwidth_Type.__name__ = "Unsigned32"
_H323ZoneMaxBandwidth_Object = MibTableColumn
h323ZoneMaxBandwidth = _H323ZoneMaxBandwidth_Object(
    (0, 0, 8, 341, 1, 1, 6, 1, 1, 1, 5),
    _H323ZoneMaxBandwidth_Type()
)
h323ZoneMaxBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h323ZoneMaxBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    h323ZoneMaxBandwidth.setUnits("100 bps")
_H323ZoneAllocatedBandwidth_Type = Integer32
_H323ZoneAllocatedBandwidth_Object = MibTableColumn
h323ZoneAllocatedBandwidth = _H323ZoneAllocatedBandwidth_Object(
    (0, 0, 8, 341, 1, 1, 6, 1, 1, 1, 6),
    _H323ZoneAllocatedBandwidth_Type()
)
h323ZoneAllocatedBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323ZoneAllocatedBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    h323ZoneAllocatedBandwidth.setUnits("100 bps")


class _H323ZoneIrrFrequency_Type(Integer32):
    """Custom type h323ZoneIrrFrequency based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_H323ZoneIrrFrequency_Type.__name__ = "Integer32"
_H323ZoneIrrFrequency_Object = MibTableColumn
h323ZoneIrrFrequency = _H323ZoneIrrFrequency_Object(
    (0, 0, 8, 341, 1, 1, 6, 1, 1, 1, 7),
    _H323ZoneIrrFrequency_Type()
)
h323ZoneIrrFrequency.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h323ZoneIrrFrequency.setStatus("current")


class _H323ZoneLocalZone_Type(TruthValue):
    """Custom type h323ZoneLocalZone based on TruthValue"""


_H323ZoneLocalZone_Object = MibTableColumn
h323ZoneLocalZone = _H323ZoneLocalZone_Object(
    (0, 0, 8, 341, 1, 1, 6, 1, 1, 1, 8),
    _H323ZoneLocalZone_Type()
)
h323ZoneLocalZone.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h323ZoneLocalZone.setStatus("current")
_H323ZoneAdmissions_Type = Counter32
_H323ZoneAdmissions_Object = MibTableColumn
h323ZoneAdmissions = _H323ZoneAdmissions_Object(
    (0, 0, 8, 341, 1, 1, 6, 1, 1, 1, 9),
    _H323ZoneAdmissions_Type()
)
h323ZoneAdmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323ZoneAdmissions.setStatus("current")
_H323ZoneAdmissionsRejected_Type = Counter32
_H323ZoneAdmissionsRejected_Object = MibTableColumn
h323ZoneAdmissionsRejected = _H323ZoneAdmissionsRejected_Object(
    (0, 0, 8, 341, 1, 1, 6, 1, 1, 1, 10),
    _H323ZoneAdmissionsRejected_Type()
)
h323ZoneAdmissionsRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323ZoneAdmissionsRejected.setStatus("current")
_H323ZoneRowStatus_Type = RowStatus
_H323ZoneRowStatus_Object = MibTableColumn
h323ZoneRowStatus = _H323ZoneRowStatus_Object(
    (0, 0, 8, 341, 1, 1, 6, 1, 1, 1, 11),
    _H323ZoneRowStatus_Type()
)
h323ZoneRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h323ZoneRowStatus.setStatus("current")
_H323GatekeeperSystem_ObjectIdentity = ObjectIdentity
h323GatekeeperSystem = _H323GatekeeperSystem_ObjectIdentity(
    (0, 0, 8, 341, 1, 1, 6, 2)
)
_H323GatekeeperSystemTable_Object = MibTable
h323GatekeeperSystemTable = _H323GatekeeperSystemTable_Object(
    (0, 0, 8, 341, 1, 1, 6, 2, 1)
)
if mibBuilder.loadTexts:
    h323GatekeeperSystemTable.setStatus("current")
_H323GatekeeperSystemEntry_Object = MibTableRow
h323GatekeeperSystemEntry = _H323GatekeeperSystemEntry_Object(
    (0, 0, 8, 341, 1, 1, 6, 2, 1, 1)
)
h323GatekeeperSystemEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    h323GatekeeperSystemEntry.setStatus("current")


class _H323GatekeeperSystemNameAndMaker_Type(DisplayString):
    """Custom type h323GatekeeperSystemNameAndMaker based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_H323GatekeeperSystemNameAndMaker_Type.__name__ = "DisplayString"
_H323GatekeeperSystemNameAndMaker_Object = MibTableColumn
h323GatekeeperSystemNameAndMaker = _H323GatekeeperSystemNameAndMaker_Object(
    (0, 0, 8, 341, 1, 1, 6, 2, 1, 1, 1),
    _H323GatekeeperSystemNameAndMaker_Type()
)
h323GatekeeperSystemNameAndMaker.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323GatekeeperSystemNameAndMaker.setStatus("current")
_H323GatekeeperSystemSoftwareVersionNumber_Type = DisplayString
_H323GatekeeperSystemSoftwareVersionNumber_Object = MibTableColumn
h323GatekeeperSystemSoftwareVersionNumber = _H323GatekeeperSystemSoftwareVersionNumber_Object(
    (0, 0, 8, 341, 1, 1, 6, 2, 1, 1, 2),
    _H323GatekeeperSystemSoftwareVersionNumber_Type()
)
h323GatekeeperSystemSoftwareVersionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323GatekeeperSystemSoftwareVersionNumber.setStatus("current")
_H323GatekeeperSystemHardwareVersionNumber_Type = DisplayString
_H323GatekeeperSystemHardwareVersionNumber_Object = MibTableColumn
h323GatekeeperSystemHardwareVersionNumber = _H323GatekeeperSystemHardwareVersionNumber_Object(
    (0, 0, 8, 341, 1, 1, 6, 2, 1, 1, 3),
    _H323GatekeeperSystemHardwareVersionNumber_Type()
)
h323GatekeeperSystemHardwareVersionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323GatekeeperSystemHardwareVersionNumber.setStatus("current")


class _H323GatekeeperSystemContact_Type(DisplayString):
    """Custom type h323GatekeeperSystemContact based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_H323GatekeeperSystemContact_Type.__name__ = "DisplayString"
_H323GatekeeperSystemContact_Object = MibTableColumn
h323GatekeeperSystemContact = _H323GatekeeperSystemContact_Object(
    (0, 0, 8, 341, 1, 1, 6, 2, 1, 1, 4),
    _H323GatekeeperSystemContact_Type()
)
h323GatekeeperSystemContact.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323GatekeeperSystemContact.setStatus("current")


class _H323GatekeeperSystemt35CountryCode_Type(Integer32):
    """Custom type h323GatekeeperSystemt35CountryCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_H323GatekeeperSystemt35CountryCode_Type.__name__ = "Integer32"
_H323GatekeeperSystemt35CountryCode_Object = MibTableColumn
h323GatekeeperSystemt35CountryCode = _H323GatekeeperSystemt35CountryCode_Object(
    (0, 0, 8, 341, 1, 1, 6, 2, 1, 1, 5),
    _H323GatekeeperSystemt35CountryCode_Type()
)
h323GatekeeperSystemt35CountryCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323GatekeeperSystemt35CountryCode.setStatus("current")


class _H323GatekeeperSystemt35CountryCodeExtention_Type(Integer32):
    """Custom type h323GatekeeperSystemt35CountryCodeExtention based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_H323GatekeeperSystemt35CountryCodeExtention_Type.__name__ = "Integer32"
_H323GatekeeperSystemt35CountryCodeExtention_Object = MibTableColumn
h323GatekeeperSystemt35CountryCodeExtention = _H323GatekeeperSystemt35CountryCodeExtention_Object(
    (0, 0, 8, 341, 1, 1, 6, 2, 1, 1, 6),
    _H323GatekeeperSystemt35CountryCodeExtention_Type()
)
h323GatekeeperSystemt35CountryCodeExtention.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323GatekeeperSystemt35CountryCodeExtention.setStatus("current")


class _H323GatekeeperSystemt35ManufacturerCode_Type(Integer32):
    """Custom type h323GatekeeperSystemt35ManufacturerCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_H323GatekeeperSystemt35ManufacturerCode_Type.__name__ = "Integer32"
_H323GatekeeperSystemt35ManufacturerCode_Object = MibTableColumn
h323GatekeeperSystemt35ManufacturerCode = _H323GatekeeperSystemt35ManufacturerCode_Object(
    (0, 0, 8, 341, 1, 1, 6, 2, 1, 1, 7),
    _H323GatekeeperSystemt35ManufacturerCode_Type()
)
h323GatekeeperSystemt35ManufacturerCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323GatekeeperSystemt35ManufacturerCode.setStatus("current")


class _H323GatekeeperSystemLocation_Type(DisplayString):
    """Custom type h323GatekeeperSystemLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_H323GatekeeperSystemLocation_Type.__name__ = "DisplayString"
_H323GatekeeperSystemLocation_Object = MibTableColumn
h323GatekeeperSystemLocation = _H323GatekeeperSystemLocation_Object(
    (0, 0, 8, 341, 1, 1, 6, 2, 1, 1, 8),
    _H323GatekeeperSystemLocation_Type()
)
h323GatekeeperSystemLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323GatekeeperSystemLocation.setStatus("current")
_H323GatekeeperSystemUptime_Type = TimeTicks
_H323GatekeeperSystemUptime_Object = MibTableColumn
h323GatekeeperSystemUptime = _H323GatekeeperSystemUptime_Object(
    (0, 0, 8, 341, 1, 1, 6, 2, 1, 1, 9),
    _H323GatekeeperSystemUptime_Type()
)
h323GatekeeperSystemUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323GatekeeperSystemUptime.setStatus("current")
_H323GatekeeperSystemLocalTime_Type = DateAndTime
_H323GatekeeperSystemLocalTime_Object = MibTableColumn
h323GatekeeperSystemLocalTime = _H323GatekeeperSystemLocalTime_Object(
    (0, 0, 8, 341, 1, 1, 6, 2, 1, 1, 10),
    _H323GatekeeperSystemLocalTime_Type()
)
h323GatekeeperSystemLocalTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323GatekeeperSystemLocalTime.setStatus("current")
_H323GatekeeperConfiguration_ObjectIdentity = ObjectIdentity
h323GatekeeperConfiguration = _H323GatekeeperConfiguration_ObjectIdentity(
    (0, 0, 8, 341, 1, 1, 6, 3)
)
_H323GatekeeperConfigurationTable_Object = MibTable
h323GatekeeperConfigurationTable = _H323GatekeeperConfigurationTable_Object(
    (0, 0, 8, 341, 1, 1, 6, 3, 1)
)
if mibBuilder.loadTexts:
    h323GatekeeperConfigurationTable.setStatus("current")
_H323GatekeeperConfigurationEntry_Object = MibTableRow
h323GatekeeperConfigurationEntry = _H323GatekeeperConfigurationEntry_Object(
    (0, 0, 8, 341, 1, 1, 6, 3, 1, 1)
)
h323GatekeeperConfigurationEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    h323GatekeeperConfigurationEntry.setStatus("current")


class _H323GatekeeperConfigurationEnableNotifications_Type(Integer32):
    """Custom type h323GatekeeperConfigurationEnableNotifications based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_H323GatekeeperConfigurationEnableNotifications_Type.__name__ = "Integer32"
_H323GatekeeperConfigurationEnableNotifications_Object = MibTableColumn
h323GatekeeperConfigurationEnableNotifications = _H323GatekeeperConfigurationEnableNotifications_Object(
    (0, 0, 8, 341, 1, 1, 6, 3, 1, 1, 1),
    _H323GatekeeperConfigurationEnableNotifications_Type()
)
h323GatekeeperConfigurationEnableNotifications.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323GatekeeperConfigurationEnableNotifications.setStatus("current")


class _H323GatekeeperConfigurationRegistrationMode_Type(Integer32):
    """Custom type h323GatekeeperConfigurationRegistrationMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("acceptAll", 1),
          ("acceptNone", 2),
          ("acceptPredefined", 3))
    )


_H323GatekeeperConfigurationRegistrationMode_Type.__name__ = "Integer32"
_H323GatekeeperConfigurationRegistrationMode_Object = MibTableColumn
h323GatekeeperConfigurationRegistrationMode = _H323GatekeeperConfigurationRegistrationMode_Object(
    (0, 0, 8, 341, 1, 1, 6, 3, 1, 1, 2),
    _H323GatekeeperConfigurationRegistrationMode_Type()
)
h323GatekeeperConfigurationRegistrationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323GatekeeperConfigurationRegistrationMode.setStatus("current")
_H323GatekeeperStatistics_ObjectIdentity = ObjectIdentity
h323GatekeeperStatistics = _H323GatekeeperStatistics_ObjectIdentity(
    (0, 0, 8, 341, 1, 1, 6, 4)
)
_H323GatekeeperStatisticsTable_Object = MibTable
h323GatekeeperStatisticsTable = _H323GatekeeperStatisticsTable_Object(
    (0, 0, 8, 341, 1, 1, 6, 4, 1)
)
if mibBuilder.loadTexts:
    h323GatekeeperStatisticsTable.setStatus("current")
_H323GatekeeperStatisticsEntry_Object = MibTableRow
h323GatekeeperStatisticsEntry = _H323GatekeeperStatisticsEntry_Object(
    (0, 0, 8, 341, 1, 1, 6, 4, 1, 1)
)
h323GatekeeperStatisticsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    h323GatekeeperStatisticsEntry.setStatus("current")
_H323GatekeeperStatisticsTotalErrors_Type = Counter32
_H323GatekeeperStatisticsTotalErrors_Object = MibTableColumn
h323GatekeeperStatisticsTotalErrors = _H323GatekeeperStatisticsTotalErrors_Object(
    (0, 0, 8, 341, 1, 1, 6, 4, 1, 1, 1),
    _H323GatekeeperStatisticsTotalErrors_Type()
)
h323GatekeeperStatisticsTotalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323GatekeeperStatisticsTotalErrors.setStatus("current")
_H323GatekeeperStatisticsLastErrorEventTime_Type = DateAndTime
_H323GatekeeperStatisticsLastErrorEventTime_Object = MibTableColumn
h323GatekeeperStatisticsLastErrorEventTime = _H323GatekeeperStatisticsLastErrorEventTime_Object(
    (0, 0, 8, 341, 1, 1, 6, 4, 1, 1, 2),
    _H323GatekeeperStatisticsLastErrorEventTime_Type()
)
h323GatekeeperStatisticsLastErrorEventTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323GatekeeperStatisticsLastErrorEventTime.setStatus("current")
_H323GatekeeperStatisticsLastErrorSeverity_Type = MmErrorSeverity
_H323GatekeeperStatisticsLastErrorSeverity_Object = MibTableColumn
h323GatekeeperStatisticsLastErrorSeverity = _H323GatekeeperStatisticsLastErrorSeverity_Object(
    (0, 0, 8, 341, 1, 1, 6, 4, 1, 1, 3),
    _H323GatekeeperStatisticsLastErrorSeverity_Type()
)
h323GatekeeperStatisticsLastErrorSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323GatekeeperStatisticsLastErrorSeverity.setStatus("current")
_H323GatekeeperStatisticsLastErrorProbableCause_Type = MmErrorProbableCause
_H323GatekeeperStatisticsLastErrorProbableCause_Object = MibTableColumn
h323GatekeeperStatisticsLastErrorProbableCause = _H323GatekeeperStatisticsLastErrorProbableCause_Object(
    (0, 0, 8, 341, 1, 1, 6, 4, 1, 1, 4),
    _H323GatekeeperStatisticsLastErrorProbableCause_Type()
)
h323GatekeeperStatisticsLastErrorProbableCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323GatekeeperStatisticsLastErrorProbableCause.setStatus("current")
_H323GatekeeperStatisticsLastErrorAdditionalText_Type = DisplayString
_H323GatekeeperStatisticsLastErrorAdditionalText_Object = MibTableColumn
h323GatekeeperStatisticsLastErrorAdditionalText = _H323GatekeeperStatisticsLastErrorAdditionalText_Object(
    (0, 0, 8, 341, 1, 1, 6, 4, 1, 1, 5),
    _H323GatekeeperStatisticsLastErrorAdditionalText_Type()
)
h323GatekeeperStatisticsLastErrorAdditionalText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323GatekeeperStatisticsLastErrorAdditionalText.setStatus("current")
_H323GatekeeperStatisticsZoneNo_Type = Counter32
_H323GatekeeperStatisticsZoneNo_Object = MibTableColumn
h323GatekeeperStatisticsZoneNo = _H323GatekeeperStatisticsZoneNo_Object(
    (0, 0, 8, 341, 1, 1, 6, 4, 1, 1, 6),
    _H323GatekeeperStatisticsZoneNo_Type()
)
h323GatekeeperStatisticsZoneNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323GatekeeperStatisticsZoneNo.setStatus("current")
_H323GatekeeperControls_ObjectIdentity = ObjectIdentity
h323GatekeeperControls = _H323GatekeeperControls_ObjectIdentity(
    (0, 0, 8, 341, 1, 1, 6, 5)
)
_H323GatekeeperControlsCommands_Type = MmControlsCommands
_H323GatekeeperControlsCommands_Object = MibScalar
h323GatekeeperControlsCommands = _H323GatekeeperControlsCommands_Object(
    (0, 0, 8, 341, 1, 1, 6, 5, 1),
    _H323GatekeeperControlsCommands_Type()
)
h323GatekeeperControlsCommands.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323GatekeeperControlsCommands.setStatus("current")
_H323GatekeeperNotifications_ObjectIdentity = ObjectIdentity
h323GatekeeperNotifications = _H323GatekeeperNotifications_ObjectIdentity(
    (0, 0, 8, 341, 1, 1, 6, 6)
)
_H323GatekeeperMIBConformance_ObjectIdentity = ObjectIdentity
h323GatekeeperMIBConformance = _H323GatekeeperMIBConformance_ObjectIdentity(
    (0, 0, 8, 341, 1, 1, 6, 7)
)
_H323GatekeeperMIBCompliance_ObjectIdentity = ObjectIdentity
h323GatekeeperMIBCompliance = _H323GatekeeperMIBCompliance_ObjectIdentity(
    (0, 0, 8, 341, 1, 1, 6, 7, 1)
)
_H323GatekeeperMIBGroups_ObjectIdentity = ObjectIdentity
h323GatekeeperMIBGroups = _H323GatekeeperMIBGroups_ObjectIdentity(
    (0, 0, 8, 341, 1, 1, 6, 7, 2)
)

# Managed Objects groups

h323GatekeeperSystemGroup = ObjectGroup(
    (0, 0, 8, 341, 1, 1, 6, 7, 2, 1)
)
h323GatekeeperSystemGroup.setObjects(
      *(("H323-GATEKEEPER-MIB", "h323GatekeeperSystemNameAndMaker"),
        ("H323-GATEKEEPER-MIB", "h323GatekeeperSystemSoftwareVersionNumber"),
        ("H323-GATEKEEPER-MIB", "h323GatekeeperSystemHardwareVersionNumber"),
        ("H323-GATEKEEPER-MIB", "h323GatekeeperSystemContact"),
        ("H323-GATEKEEPER-MIB", "h323GatekeeperSystemt35CountryCode"),
        ("H323-GATEKEEPER-MIB", "h323GatekeeperSystemt35CountryCodeExtention"),
        ("H323-GATEKEEPER-MIB", "h323GatekeeperSystemt35ManufacturerCode"),
        ("H323-GATEKEEPER-MIB", "h323GatekeeperSystemLocation"),
        ("H323-GATEKEEPER-MIB", "h323GatekeeperSystemUptime"),
        ("H323-GATEKEEPER-MIB", "h323GatekeeperSystemLocalTime"))
)
if mibBuilder.loadTexts:
    h323GatekeeperSystemGroup.setStatus("current")

h323GatekeeperConfigurationGroup = ObjectGroup(
    (0, 0, 8, 341, 1, 1, 6, 7, 2, 2)
)
h323GatekeeperConfigurationGroup.setObjects(
    ("H323-GATEKEEPER-MIB", "h323GatekeeperConfigurationEnableNotifications")
)
if mibBuilder.loadTexts:
    h323GatekeeperConfigurationGroup.setStatus("current")

h323GatekeeperZoneGroup = ObjectGroup(
    (0, 0, 8, 341, 1, 1, 6, 7, 2, 3)
)
h323GatekeeperZoneGroup.setObjects(
      *(("H323-GATEKEEPER-MIB", "h323ZoneZoneName"),
        ("H323-GATEKEEPER-MIB", "h323ZoneRasSignalAddressTag"),
        ("H323-GATEKEEPER-MIB", "h323ZoneRasSignalAddress"),
        ("H323-GATEKEEPER-MIB", "h323ZoneMaxBandwidth"),
        ("H323-GATEKEEPER-MIB", "h323ZoneAllocatedBandwidth"),
        ("H323-GATEKEEPER-MIB", "h323ZoneIrrFrequency"),
        ("H323-GATEKEEPER-MIB", "h323ZoneLocalZone"),
        ("H323-GATEKEEPER-MIB", "h323ZoneAdmissions"),
        ("H323-GATEKEEPER-MIB", "h323ZoneAdmissionsRejected"),
        ("H323-GATEKEEPER-MIB", "h323ZoneRowStatus"))
)
if mibBuilder.loadTexts:
    h323GatekeeperZoneGroup.setStatus("current")

h323GatekeeperStatisticsGroup = ObjectGroup(
    (0, 0, 8, 341, 1, 1, 6, 7, 2, 4)
)
h323GatekeeperStatisticsGroup.setObjects(
      *(("H323-GATEKEEPER-MIB", "h323GatekeeperStatisticsTotalErrors"),
        ("H323-GATEKEEPER-MIB", "h323GatekeeperStatisticsLastErrorEventTime"),
        ("H323-GATEKEEPER-MIB", "h323GatekeeperStatisticsLastErrorSeverity"),
        ("H323-GATEKEEPER-MIB", "h323GatekeeperStatisticsLastErrorProbableCause"),
        ("H323-GATEKEEPER-MIB", "h323GatekeeperStatisticsLastErrorAdditionalText"),
        ("H323-GATEKEEPER-MIB", "h323GatekeeperStatisticsZoneNo"))
)
if mibBuilder.loadTexts:
    h323GatekeeperStatisticsGroup.setStatus("current")

h323GatekeeperControlsGroup = ObjectGroup(
    (0, 0, 8, 341, 1, 1, 6, 7, 2, 5)
)
h323GatekeeperControlsGroup.setObjects(
    ("H323-GATEKEEPER-MIB", "h323GatekeeperControlsCommands")
)
if mibBuilder.loadTexts:
    h323GatekeeperControlsGroup.setStatus("current")


# Notification objects

h323GatekeeperStart = NotificationType(
    (0, 0, 8, 341, 1, 1, 6, 6, 1)
)
h323GatekeeperStart.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    h323GatekeeperStart.setStatus(
        "current"
    )

h323GatekeeperGoingDown = NotificationType(
    (0, 0, 8, 341, 1, 1, 6, 6, 2)
)
h323GatekeeperGoingDown.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    h323GatekeeperGoingDown.setStatus(
        "current"
    )

h323GatekeeperError = NotificationType(
    (0, 0, 8, 341, 1, 1, 6, 6, 3)
)
h323GatekeeperError.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("H323-GATEKEEPER-MIB", "h323GatekeeperStatisticsLastErrorEventTime"),
        ("H323-GATEKEEPER-MIB", "h323GatekeeperStatisticsLastErrorSeverity"),
        ("H323-GATEKEEPER-MIB", "h323GatekeeperStatisticsLastErrorProbableCause"))
)
if mibBuilder.loadTexts:
    h323GatekeeperError.setStatus(
        "current"
    )


# Notifications groups

h323GatekeeperNotificationsGroup = NotificationGroup(
    (0, 0, 8, 341, 1, 1, 6, 7, 2, 6)
)
h323GatekeeperNotificationsGroup.setObjects(
      *(("H323-GATEKEEPER-MIB", "h323GatekeeperStart"),
        ("H323-GATEKEEPER-MIB", "h323GatekeeperGoingDown"),
        ("H323-GATEKEEPER-MIB", "h323GatekeeperError"))
)
if mibBuilder.loadTexts:
    h323GatekeeperNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

h323GatekeeperCompliance = ModuleCompliance(
    (0, 0, 8, 341, 1, 1, 6, 7, 1, 1)
)
if mibBuilder.loadTexts:
    h323GatekeeperCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H323-GATEKEEPER-MIB",
    **{"h323Gatekeeper": h323Gatekeeper,
       "h323GatekeeperZone": h323GatekeeperZone,
       "h323ZoneTable": h323ZoneTable,
       "h323ZoneEntry": h323ZoneEntry,
       "h323ZoneIndex": h323ZoneIndex,
       "h323ZoneZoneName": h323ZoneZoneName,
       "h323ZoneRasSignalAddressTag": h323ZoneRasSignalAddressTag,
       "h323ZoneRasSignalAddress": h323ZoneRasSignalAddress,
       "h323ZoneMaxBandwidth": h323ZoneMaxBandwidth,
       "h323ZoneAllocatedBandwidth": h323ZoneAllocatedBandwidth,
       "h323ZoneIrrFrequency": h323ZoneIrrFrequency,
       "h323ZoneLocalZone": h323ZoneLocalZone,
       "h323ZoneAdmissions": h323ZoneAdmissions,
       "h323ZoneAdmissionsRejected": h323ZoneAdmissionsRejected,
       "h323ZoneRowStatus": h323ZoneRowStatus,
       "h323GatekeeperSystem": h323GatekeeperSystem,
       "h323GatekeeperSystemTable": h323GatekeeperSystemTable,
       "h323GatekeeperSystemEntry": h323GatekeeperSystemEntry,
       "h323GatekeeperSystemNameAndMaker": h323GatekeeperSystemNameAndMaker,
       "h323GatekeeperSystemSoftwareVersionNumber": h323GatekeeperSystemSoftwareVersionNumber,
       "h323GatekeeperSystemHardwareVersionNumber": h323GatekeeperSystemHardwareVersionNumber,
       "h323GatekeeperSystemContact": h323GatekeeperSystemContact,
       "h323GatekeeperSystemt35CountryCode": h323GatekeeperSystemt35CountryCode,
       "h323GatekeeperSystemt35CountryCodeExtention": h323GatekeeperSystemt35CountryCodeExtention,
       "h323GatekeeperSystemt35ManufacturerCode": h323GatekeeperSystemt35ManufacturerCode,
       "h323GatekeeperSystemLocation": h323GatekeeperSystemLocation,
       "h323GatekeeperSystemUptime": h323GatekeeperSystemUptime,
       "h323GatekeeperSystemLocalTime": h323GatekeeperSystemLocalTime,
       "h323GatekeeperConfiguration": h323GatekeeperConfiguration,
       "h323GatekeeperConfigurationTable": h323GatekeeperConfigurationTable,
       "h323GatekeeperConfigurationEntry": h323GatekeeperConfigurationEntry,
       "h323GatekeeperConfigurationEnableNotifications": h323GatekeeperConfigurationEnableNotifications,
       "h323GatekeeperConfigurationRegistrationMode": h323GatekeeperConfigurationRegistrationMode,
       "h323GatekeeperStatistics": h323GatekeeperStatistics,
       "h323GatekeeperStatisticsTable": h323GatekeeperStatisticsTable,
       "h323GatekeeperStatisticsEntry": h323GatekeeperStatisticsEntry,
       "h323GatekeeperStatisticsTotalErrors": h323GatekeeperStatisticsTotalErrors,
       "h323GatekeeperStatisticsLastErrorEventTime": h323GatekeeperStatisticsLastErrorEventTime,
       "h323GatekeeperStatisticsLastErrorSeverity": h323GatekeeperStatisticsLastErrorSeverity,
       "h323GatekeeperStatisticsLastErrorProbableCause": h323GatekeeperStatisticsLastErrorProbableCause,
       "h323GatekeeperStatisticsLastErrorAdditionalText": h323GatekeeperStatisticsLastErrorAdditionalText,
       "h323GatekeeperStatisticsZoneNo": h323GatekeeperStatisticsZoneNo,
       "h323GatekeeperControls": h323GatekeeperControls,
       "h323GatekeeperControlsCommands": h323GatekeeperControlsCommands,
       "h323GatekeeperNotifications": h323GatekeeperNotifications,
       "h323GatekeeperStart": h323GatekeeperStart,
       "h323GatekeeperGoingDown": h323GatekeeperGoingDown,
       "h323GatekeeperError": h323GatekeeperError,
       "h323GatekeeperMIBConformance": h323GatekeeperMIBConformance,
       "h323GatekeeperMIBCompliance": h323GatekeeperMIBCompliance,
       "h323GatekeeperCompliance": h323GatekeeperCompliance,
       "h323GatekeeperMIBGroups": h323GatekeeperMIBGroups,
       "h323GatekeeperSystemGroup": h323GatekeeperSystemGroup,
       "h323GatekeeperConfigurationGroup": h323GatekeeperConfigurationGroup,
       "h323GatekeeperZoneGroup": h323GatekeeperZoneGroup,
       "h323GatekeeperStatisticsGroup": h323GatekeeperStatisticsGroup,
       "h323GatekeeperControlsGroup": h323GatekeeperControlsGroup,
       "h323GatekeeperNotificationsGroup": h323GatekeeperNotificationsGroup}
)
