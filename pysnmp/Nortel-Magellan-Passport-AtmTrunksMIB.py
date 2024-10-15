# SNMP MIB module (Nortel-Magellan-Passport-AtmTrunksMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-Magellan-Passport-AtmTrunksMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:30:22 2024
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

(DisplayString,
 Gauge32,
 RowStatus,
 StorageType,
 Unsigned32) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-StandardTextualConventionsMIB",
    "DisplayString",
    "Gauge32",
    "RowStatus",
    "StorageType",
    "Unsigned32")

(FixedPoint1,
 Link,
 NonReplicated) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-TextualConventionsMIB",
    "FixedPoint1",
    "Link",
    "NonReplicated")

(trk,
 trkIndex) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-TrunksMIB",
    "trk",
    "trkIndex")

(passportMIBs,) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-UsefulDefinitionsMIB",
    "passportMIBs")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TrkAtm_ObjectIdentity = ObjectIdentity
trkAtm = _TrkAtm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 3)
)
_TrkAtmRowStatusTable_Object = MibTable
trkAtmRowStatusTable = _TrkAtmRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 3, 1)
)
if mibBuilder.loadTexts:
    trkAtmRowStatusTable.setStatus("mandatory")
_TrkAtmRowStatusEntry_Object = MibTableRow
trkAtmRowStatusEntry = _TrkAtmRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 3, 1, 1)
)
trkAtmRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TrunksMIB", "trkIndex"),
    (0, "Nortel-Magellan-Passport-AtmTrunksMIB", "trkAtmIndex"),
)
if mibBuilder.loadTexts:
    trkAtmRowStatusEntry.setStatus("mandatory")
_TrkAtmRowStatus_Type = RowStatus
_TrkAtmRowStatus_Object = MibTableColumn
trkAtmRowStatus = _TrkAtmRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 3, 1, 1, 1),
    _TrkAtmRowStatus_Type()
)
trkAtmRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trkAtmRowStatus.setStatus("mandatory")
_TrkAtmComponentName_Type = DisplayString
_TrkAtmComponentName_Object = MibTableColumn
trkAtmComponentName = _TrkAtmComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 3, 1, 1, 2),
    _TrkAtmComponentName_Type()
)
trkAtmComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkAtmComponentName.setStatus("mandatory")
_TrkAtmStorageType_Type = StorageType
_TrkAtmStorageType_Object = MibTableColumn
trkAtmStorageType = _TrkAtmStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 3, 1, 1, 4),
    _TrkAtmStorageType_Type()
)
trkAtmStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkAtmStorageType.setStatus("mandatory")
_TrkAtmIndex_Type = NonReplicated
_TrkAtmIndex_Object = MibTableColumn
trkAtmIndex = _TrkAtmIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 3, 1, 1, 10),
    _TrkAtmIndex_Type()
)
trkAtmIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trkAtmIndex.setStatus("mandatory")
_TrkAtmProvTable_Object = MibTable
trkAtmProvTable = _TrkAtmProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 3, 10)
)
if mibBuilder.loadTexts:
    trkAtmProvTable.setStatus("mandatory")
_TrkAtmProvEntry_Object = MibTableRow
trkAtmProvEntry = _TrkAtmProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 3, 10, 1)
)
trkAtmProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TrunksMIB", "trkIndex"),
    (0, "Nortel-Magellan-Passport-AtmTrunksMIB", "trkAtmIndex"),
)
if mibBuilder.loadTexts:
    trkAtmProvEntry.setStatus("mandatory")


class _TrkAtmMaximumErroredInterval_Type(Unsigned32):
    """Custom type trkAtmMaximumErroredInterval based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 15),
    )


_TrkAtmMaximumErroredInterval_Type.__name__ = "Unsigned32"
_TrkAtmMaximumErroredInterval_Object = MibTableColumn
trkAtmMaximumErroredInterval = _TrkAtmMaximumErroredInterval_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 3, 10, 1, 1),
    _TrkAtmMaximumErroredInterval_Type()
)
trkAtmMaximumErroredInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trkAtmMaximumErroredInterval.setStatus("obsolete")


class _TrkAtmReceiveErrorSensitivity_Type(Unsigned32):
    """Custom type trkAtmReceiveErrorSensitivity based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 10),
    )


_TrkAtmReceiveErrorSensitivity_Type.__name__ = "Unsigned32"
_TrkAtmReceiveErrorSensitivity_Object = MibTableColumn
trkAtmReceiveErrorSensitivity = _TrkAtmReceiveErrorSensitivity_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 3, 10, 1, 2),
    _TrkAtmReceiveErrorSensitivity_Type()
)
trkAtmReceiveErrorSensitivity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trkAtmReceiveErrorSensitivity.setStatus("mandatory")


class _TrkAtmAtmAccMaximumErroredInterval_Type(FixedPoint1):
    """Custom type trkAtmAtmAccMaximumErroredInterval based on FixedPoint1"""
    defaultValue = 0

    subtypeSpec = FixedPoint1.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(5, 5),
        ValueRangeConstraint(10, 10),
        ValueRangeConstraint(15, 15),
        ValueRangeConstraint(20, 20),
        ValueRangeConstraint(25, 25),
        ValueRangeConstraint(30, 30),
        ValueRangeConstraint(35, 35),
        ValueRangeConstraint(40, 40),
        ValueRangeConstraint(45, 45),
        ValueRangeConstraint(50, 50),
        ValueRangeConstraint(60, 60),
        ValueRangeConstraint(70, 70),
        ValueRangeConstraint(80, 80),
        ValueRangeConstraint(90, 90),
        ValueRangeConstraint(100, 100),
        ValueRangeConstraint(110, 110),
        ValueRangeConstraint(120, 120),
        ValueRangeConstraint(130, 130),
        ValueRangeConstraint(140, 140),
        ValueRangeConstraint(150, 150),
    )


_TrkAtmAtmAccMaximumErroredInterval_Type.__name__ = "FixedPoint1"
_TrkAtmAtmAccMaximumErroredInterval_Object = MibTableColumn
trkAtmAtmAccMaximumErroredInterval = _TrkAtmAtmAccMaximumErroredInterval_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 3, 10, 1, 3),
    _TrkAtmAtmAccMaximumErroredInterval_Type()
)
trkAtmAtmAccMaximumErroredInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trkAtmAtmAccMaximumErroredInterval.setStatus("mandatory")
_TrkAtmInterfaceTable_Object = MibTable
trkAtmInterfaceTable = _TrkAtmInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 3, 11)
)
if mibBuilder.loadTexts:
    trkAtmInterfaceTable.setStatus("mandatory")
_TrkAtmInterfaceEntry_Object = MibTableRow
trkAtmInterfaceEntry = _TrkAtmInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 3, 11, 1)
)
trkAtmInterfaceEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TrunksMIB", "trkIndex"),
    (0, "Nortel-Magellan-Passport-AtmTrunksMIB", "trkAtmIndex"),
)
if mibBuilder.loadTexts:
    trkAtmInterfaceEntry.setStatus("mandatory")
_TrkAtmAtmConnection_Type = Link
_TrkAtmAtmConnection_Object = MibTableColumn
trkAtmAtmConnection = _TrkAtmAtmConnection_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 3, 11, 1, 1),
    _TrkAtmAtmConnection_Type()
)
trkAtmAtmConnection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trkAtmAtmConnection.setStatus("mandatory")


class _TrkAtmBwElastic_Type(Integer32):
    """Custom type trkAtmBwElastic based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_TrkAtmBwElastic_Type.__name__ = "Integer32"
_TrkAtmBwElastic_Object = MibTableColumn
trkAtmBwElastic = _TrkAtmBwElastic_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 3, 11, 1, 2),
    _TrkAtmBwElastic_Type()
)
trkAtmBwElastic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trkAtmBwElastic.setStatus("mandatory")


class _TrkAtmVccReportingBw_Type(Integer32):
    """Custom type trkAtmVccReportingBw based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("acr", 1),
          ("pcr", 0))
    )


_TrkAtmVccReportingBw_Type.__name__ = "Integer32"
_TrkAtmVccReportingBw_Object = MibTableColumn
trkAtmVccReportingBw = _TrkAtmVccReportingBw_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 3, 11, 1, 3),
    _TrkAtmVccReportingBw_Type()
)
trkAtmVccReportingBw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trkAtmVccReportingBw.setStatus("mandatory")
_TrkAtmStateTable_Object = MibTable
trkAtmStateTable = _TrkAtmStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 3, 12)
)
if mibBuilder.loadTexts:
    trkAtmStateTable.setStatus("mandatory")
_TrkAtmStateEntry_Object = MibTableRow
trkAtmStateEntry = _TrkAtmStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 3, 12, 1)
)
trkAtmStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TrunksMIB", "trkIndex"),
    (0, "Nortel-Magellan-Passport-AtmTrunksMIB", "trkAtmIndex"),
)
if mibBuilder.loadTexts:
    trkAtmStateEntry.setStatus("mandatory")


class _TrkAtmAdminState_Type(Integer32):
    """Custom type trkAtmAdminState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("locked", 0),
          ("shuttingDown", 2),
          ("unlocked", 1))
    )


_TrkAtmAdminState_Type.__name__ = "Integer32"
_TrkAtmAdminState_Object = MibTableColumn
trkAtmAdminState = _TrkAtmAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 3, 12, 1, 1),
    _TrkAtmAdminState_Type()
)
trkAtmAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkAtmAdminState.setStatus("mandatory")


class _TrkAtmOperationalState_Type(Integer32):
    """Custom type trkAtmOperationalState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_TrkAtmOperationalState_Type.__name__ = "Integer32"
_TrkAtmOperationalState_Object = MibTableColumn
trkAtmOperationalState = _TrkAtmOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 3, 12, 1, 2),
    _TrkAtmOperationalState_Type()
)
trkAtmOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkAtmOperationalState.setStatus("mandatory")


class _TrkAtmUsageState_Type(Integer32):
    """Custom type trkAtmUsageState based on Integer32"""
    defaultValue = 0

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
          ("busy", 2),
          ("idle", 0))
    )


_TrkAtmUsageState_Type.__name__ = "Integer32"
_TrkAtmUsageState_Object = MibTableColumn
trkAtmUsageState = _TrkAtmUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 3, 12, 1, 3),
    _TrkAtmUsageState_Type()
)
trkAtmUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkAtmUsageState.setStatus("mandatory")


class _TrkAtmAvailabilityStatus_Type(OctetString):
    """Custom type trkAtmAvailabilityStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_TrkAtmAvailabilityStatus_Type.__name__ = "OctetString"
_TrkAtmAvailabilityStatus_Object = MibTableColumn
trkAtmAvailabilityStatus = _TrkAtmAvailabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 3, 12, 1, 4),
    _TrkAtmAvailabilityStatus_Type()
)
trkAtmAvailabilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkAtmAvailabilityStatus.setStatus("mandatory")


class _TrkAtmProceduralStatus_Type(OctetString):
    """Custom type trkAtmProceduralStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_TrkAtmProceduralStatus_Type.__name__ = "OctetString"
_TrkAtmProceduralStatus_Object = MibTableColumn
trkAtmProceduralStatus = _TrkAtmProceduralStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 3, 12, 1, 5),
    _TrkAtmProceduralStatus_Type()
)
trkAtmProceduralStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkAtmProceduralStatus.setStatus("mandatory")


class _TrkAtmControlStatus_Type(OctetString):
    """Custom type trkAtmControlStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_TrkAtmControlStatus_Type.__name__ = "OctetString"
_TrkAtmControlStatus_Object = MibTableColumn
trkAtmControlStatus = _TrkAtmControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 3, 12, 1, 6),
    _TrkAtmControlStatus_Type()
)
trkAtmControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkAtmControlStatus.setStatus("mandatory")


class _TrkAtmAlarmStatus_Type(OctetString):
    """Custom type trkAtmAlarmStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_TrkAtmAlarmStatus_Type.__name__ = "OctetString"
_TrkAtmAlarmStatus_Object = MibTableColumn
trkAtmAlarmStatus = _TrkAtmAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 3, 12, 1, 7),
    _TrkAtmAlarmStatus_Type()
)
trkAtmAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkAtmAlarmStatus.setStatus("mandatory")


class _TrkAtmStandbyStatus_Type(Integer32):
    """Custom type trkAtmStandbyStatus based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              15)
        )
    )
    namedValues = NamedValues(
        *(("coldStandby", 1),
          ("hotStandby", 0),
          ("notSet", 15),
          ("providingService", 2))
    )


_TrkAtmStandbyStatus_Type.__name__ = "Integer32"
_TrkAtmStandbyStatus_Object = MibTableColumn
trkAtmStandbyStatus = _TrkAtmStandbyStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 3, 12, 1, 8),
    _TrkAtmStandbyStatus_Type()
)
trkAtmStandbyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkAtmStandbyStatus.setStatus("mandatory")


class _TrkAtmUnknownStatus_Type(Integer32):
    """Custom type trkAtmUnknownStatus based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_TrkAtmUnknownStatus_Type.__name__ = "Integer32"
_TrkAtmUnknownStatus_Object = MibTableColumn
trkAtmUnknownStatus = _TrkAtmUnknownStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 3, 12, 1, 9),
    _TrkAtmUnknownStatus_Type()
)
trkAtmUnknownStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkAtmUnknownStatus.setStatus("mandatory")
_TrkAtmUtilTable_Object = MibTable
trkAtmUtilTable = _TrkAtmUtilTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 3, 14)
)
if mibBuilder.loadTexts:
    trkAtmUtilTable.setStatus("mandatory")
_TrkAtmUtilEntry_Object = MibTableRow
trkAtmUtilEntry = _TrkAtmUtilEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 3, 14, 1)
)
trkAtmUtilEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TrunksMIB", "trkIndex"),
    (0, "Nortel-Magellan-Passport-AtmTrunksMIB", "trkAtmIndex"),
)
if mibBuilder.loadTexts:
    trkAtmUtilEntry.setStatus("mandatory")


class _TrkAtmMinorVccUtilAlarmThreshold_Type(Unsigned32):
    """Custom type trkAtmMinorVccUtilAlarmThreshold based on Unsigned32"""
    defaultValue = 75

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_TrkAtmMinorVccUtilAlarmThreshold_Type.__name__ = "Unsigned32"
_TrkAtmMinorVccUtilAlarmThreshold_Object = MibTableColumn
trkAtmMinorVccUtilAlarmThreshold = _TrkAtmMinorVccUtilAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 3, 14, 1, 1),
    _TrkAtmMinorVccUtilAlarmThreshold_Type()
)
trkAtmMinorVccUtilAlarmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trkAtmMinorVccUtilAlarmThreshold.setStatus("mandatory")


class _TrkAtmMajorVccUtilAlarmThreshold_Type(Unsigned32):
    """Custom type trkAtmMajorVccUtilAlarmThreshold based on Unsigned32"""
    defaultValue = 85

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_TrkAtmMajorVccUtilAlarmThreshold_Type.__name__ = "Unsigned32"
_TrkAtmMajorVccUtilAlarmThreshold_Object = MibTableColumn
trkAtmMajorVccUtilAlarmThreshold = _TrkAtmMajorVccUtilAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 3, 14, 1, 2),
    _TrkAtmMajorVccUtilAlarmThreshold_Type()
)
trkAtmMajorVccUtilAlarmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trkAtmMajorVccUtilAlarmThreshold.setStatus("mandatory")


class _TrkAtmCriticalVccUtilAlarmThreshold_Type(Unsigned32):
    """Custom type trkAtmCriticalVccUtilAlarmThreshold based on Unsigned32"""
    defaultValue = 95

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_TrkAtmCriticalVccUtilAlarmThreshold_Type.__name__ = "Unsigned32"
_TrkAtmCriticalVccUtilAlarmThreshold_Object = MibTableColumn
trkAtmCriticalVccUtilAlarmThreshold = _TrkAtmCriticalVccUtilAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 3, 14, 1, 3),
    _TrkAtmCriticalVccUtilAlarmThreshold_Type()
)
trkAtmCriticalVccUtilAlarmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trkAtmCriticalVccUtilAlarmThreshold.setStatus("mandatory")


class _TrkAtmVccUtilAlarmStatus_Type(Integer32):
    """Custom type trkAtmVccUtilAlarmStatus based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_TrkAtmVccUtilAlarmStatus_Type.__name__ = "Integer32"
_TrkAtmVccUtilAlarmStatus_Object = MibTableColumn
trkAtmVccUtilAlarmStatus = _TrkAtmVccUtilAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 3, 14, 1, 4),
    _TrkAtmVccUtilAlarmStatus_Type()
)
trkAtmVccUtilAlarmStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trkAtmVccUtilAlarmStatus.setStatus("mandatory")
_TrkAtmStatsTable_Object = MibTable
trkAtmStatsTable = _TrkAtmStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 3, 15)
)
if mibBuilder.loadTexts:
    trkAtmStatsTable.setStatus("mandatory")
_TrkAtmStatsEntry_Object = MibTableRow
trkAtmStatsEntry = _TrkAtmStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 3, 15, 1)
)
trkAtmStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TrunksMIB", "trkIndex"),
    (0, "Nortel-Magellan-Passport-AtmTrunksMIB", "trkAtmIndex"),
)
if mibBuilder.loadTexts:
    trkAtmStatsEntry.setStatus("mandatory")


class _TrkAtmLastCalculatedVccUtilization_Type(Gauge32):
    """Custom type trkAtmLastCalculatedVccUtilization based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_TrkAtmLastCalculatedVccUtilization_Type.__name__ = "Gauge32"
_TrkAtmLastCalculatedVccUtilization_Object = MibTableColumn
trkAtmLastCalculatedVccUtilization = _TrkAtmLastCalculatedVccUtilization_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 3, 15, 1, 1),
    _TrkAtmLastCalculatedVccUtilization_Type()
)
trkAtmLastCalculatedVccUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkAtmLastCalculatedVccUtilization.setStatus("mandatory")


class _TrkAtmLastCalculatedTxVccUtilization_Type(Gauge32):
    """Custom type trkAtmLastCalculatedTxVccUtilization based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_TrkAtmLastCalculatedTxVccUtilization_Type.__name__ = "Gauge32"
_TrkAtmLastCalculatedTxVccUtilization_Object = MibTableColumn
trkAtmLastCalculatedTxVccUtilization = _TrkAtmLastCalculatedTxVccUtilization_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 3, 15, 1, 2),
    _TrkAtmLastCalculatedTxVccUtilization_Type()
)
trkAtmLastCalculatedTxVccUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkAtmLastCalculatedTxVccUtilization.setStatus("mandatory")
_AtmTrunksMIB_ObjectIdentity = ObjectIdentity
atmTrunksMIB = _AtmTrunksMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 59)
)
_AtmTrunksGroup_ObjectIdentity = ObjectIdentity
atmTrunksGroup = _AtmTrunksGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 59, 1)
)
_AtmTrunksGroupBE_ObjectIdentity = ObjectIdentity
atmTrunksGroupBE = _AtmTrunksGroupBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 59, 1, 5)
)
_AtmTrunksGroupBE01_ObjectIdentity = ObjectIdentity
atmTrunksGroupBE01 = _AtmTrunksGroupBE01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 59, 1, 5, 2)
)
_AtmTrunksGroupBE01A_ObjectIdentity = ObjectIdentity
atmTrunksGroupBE01A = _AtmTrunksGroupBE01A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 59, 1, 5, 2, 2)
)
_AtmTrunksCapabilities_ObjectIdentity = ObjectIdentity
atmTrunksCapabilities = _AtmTrunksCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 59, 3)
)
_AtmTrunksCapabilitiesBE_ObjectIdentity = ObjectIdentity
atmTrunksCapabilitiesBE = _AtmTrunksCapabilitiesBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 59, 3, 5)
)
_AtmTrunksCapabilitiesBE01_ObjectIdentity = ObjectIdentity
atmTrunksCapabilitiesBE01 = _AtmTrunksCapabilitiesBE01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 59, 3, 5, 2)
)
_AtmTrunksCapabilitiesBE01A_ObjectIdentity = ObjectIdentity
atmTrunksCapabilitiesBE01A = _AtmTrunksCapabilitiesBE01A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 59, 3, 5, 2, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-Magellan-Passport-AtmTrunksMIB",
    **{"trkAtm": trkAtm,
       "trkAtmRowStatusTable": trkAtmRowStatusTable,
       "trkAtmRowStatusEntry": trkAtmRowStatusEntry,
       "trkAtmRowStatus": trkAtmRowStatus,
       "trkAtmComponentName": trkAtmComponentName,
       "trkAtmStorageType": trkAtmStorageType,
       "trkAtmIndex": trkAtmIndex,
       "trkAtmProvTable": trkAtmProvTable,
       "trkAtmProvEntry": trkAtmProvEntry,
       "trkAtmMaximumErroredInterval": trkAtmMaximumErroredInterval,
       "trkAtmReceiveErrorSensitivity": trkAtmReceiveErrorSensitivity,
       "trkAtmAtmAccMaximumErroredInterval": trkAtmAtmAccMaximumErroredInterval,
       "trkAtmInterfaceTable": trkAtmInterfaceTable,
       "trkAtmInterfaceEntry": trkAtmInterfaceEntry,
       "trkAtmAtmConnection": trkAtmAtmConnection,
       "trkAtmBwElastic": trkAtmBwElastic,
       "trkAtmVccReportingBw": trkAtmVccReportingBw,
       "trkAtmStateTable": trkAtmStateTable,
       "trkAtmStateEntry": trkAtmStateEntry,
       "trkAtmAdminState": trkAtmAdminState,
       "trkAtmOperationalState": trkAtmOperationalState,
       "trkAtmUsageState": trkAtmUsageState,
       "trkAtmAvailabilityStatus": trkAtmAvailabilityStatus,
       "trkAtmProceduralStatus": trkAtmProceduralStatus,
       "trkAtmControlStatus": trkAtmControlStatus,
       "trkAtmAlarmStatus": trkAtmAlarmStatus,
       "trkAtmStandbyStatus": trkAtmStandbyStatus,
       "trkAtmUnknownStatus": trkAtmUnknownStatus,
       "trkAtmUtilTable": trkAtmUtilTable,
       "trkAtmUtilEntry": trkAtmUtilEntry,
       "trkAtmMinorVccUtilAlarmThreshold": trkAtmMinorVccUtilAlarmThreshold,
       "trkAtmMajorVccUtilAlarmThreshold": trkAtmMajorVccUtilAlarmThreshold,
       "trkAtmCriticalVccUtilAlarmThreshold": trkAtmCriticalVccUtilAlarmThreshold,
       "trkAtmVccUtilAlarmStatus": trkAtmVccUtilAlarmStatus,
       "trkAtmStatsTable": trkAtmStatsTable,
       "trkAtmStatsEntry": trkAtmStatsEntry,
       "trkAtmLastCalculatedVccUtilization": trkAtmLastCalculatedVccUtilization,
       "trkAtmLastCalculatedTxVccUtilization": trkAtmLastCalculatedTxVccUtilization,
       "atmTrunksMIB": atmTrunksMIB,
       "atmTrunksGroup": atmTrunksGroup,
       "atmTrunksGroupBE": atmTrunksGroupBE,
       "atmTrunksGroupBE01": atmTrunksGroupBE01,
       "atmTrunksGroupBE01A": atmTrunksGroupBE01A,
       "atmTrunksCapabilities": atmTrunksCapabilities,
       "atmTrunksCapabilitiesBE": atmTrunksCapabilitiesBE,
       "atmTrunksCapabilitiesBE01": atmTrunksCapabilitiesBE01,
       "atmTrunksCapabilitiesBE01A": atmTrunksCapabilitiesBE01A}
)
