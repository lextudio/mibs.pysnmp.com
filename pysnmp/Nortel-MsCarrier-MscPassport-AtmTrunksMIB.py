# SNMP MIB module (Nortel-MsCarrier-MscPassport-AtmTrunksMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-MsCarrier-MscPassport-AtmTrunksMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:31:56 2024
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
    "Nortel-MsCarrier-MscPassport-StandardTextualConventionsMIB",
    "DisplayString",
    "Gauge32",
    "RowStatus",
    "StorageType",
    "Unsigned32")

(FixedPoint1,
 Link,
 NonReplicated) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-TextualConventionsMIB",
    "FixedPoint1",
    "Link",
    "NonReplicated")

(mscTrk,
 mscTrkIndex) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-TrunksMIB",
    "mscTrk",
    "mscTrkIndex")

(mscPassportMIBs,) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-UsefulDefinitionsMIB",
    "mscPassportMIBs")

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

_MscTrkAtm_ObjectIdentity = ObjectIdentity
mscTrkAtm = _MscTrkAtm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 3)
)
_MscTrkAtmRowStatusTable_Object = MibTable
mscTrkAtmRowStatusTable = _MscTrkAtmRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 3, 1)
)
if mibBuilder.loadTexts:
    mscTrkAtmRowStatusTable.setStatus("mandatory")
_MscTrkAtmRowStatusEntry_Object = MibTableRow
mscTrkAtmRowStatusEntry = _MscTrkAtmRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 3, 1, 1)
)
mscTrkAtmRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TrunksMIB", "mscTrkIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmTrunksMIB", "mscTrkAtmIndex"),
)
if mibBuilder.loadTexts:
    mscTrkAtmRowStatusEntry.setStatus("mandatory")
_MscTrkAtmRowStatus_Type = RowStatus
_MscTrkAtmRowStatus_Object = MibTableColumn
mscTrkAtmRowStatus = _MscTrkAtmRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 3, 1, 1, 1),
    _MscTrkAtmRowStatus_Type()
)
mscTrkAtmRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscTrkAtmRowStatus.setStatus("mandatory")
_MscTrkAtmComponentName_Type = DisplayString
_MscTrkAtmComponentName_Object = MibTableColumn
mscTrkAtmComponentName = _MscTrkAtmComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 3, 1, 1, 2),
    _MscTrkAtmComponentName_Type()
)
mscTrkAtmComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkAtmComponentName.setStatus("mandatory")
_MscTrkAtmStorageType_Type = StorageType
_MscTrkAtmStorageType_Object = MibTableColumn
mscTrkAtmStorageType = _MscTrkAtmStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 3, 1, 1, 4),
    _MscTrkAtmStorageType_Type()
)
mscTrkAtmStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkAtmStorageType.setStatus("mandatory")
_MscTrkAtmIndex_Type = NonReplicated
_MscTrkAtmIndex_Object = MibTableColumn
mscTrkAtmIndex = _MscTrkAtmIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 3, 1, 1, 10),
    _MscTrkAtmIndex_Type()
)
mscTrkAtmIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscTrkAtmIndex.setStatus("mandatory")
_MscTrkAtmProvTable_Object = MibTable
mscTrkAtmProvTable = _MscTrkAtmProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 3, 10)
)
if mibBuilder.loadTexts:
    mscTrkAtmProvTable.setStatus("mandatory")
_MscTrkAtmProvEntry_Object = MibTableRow
mscTrkAtmProvEntry = _MscTrkAtmProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 3, 10, 1)
)
mscTrkAtmProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TrunksMIB", "mscTrkIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmTrunksMIB", "mscTrkAtmIndex"),
)
if mibBuilder.loadTexts:
    mscTrkAtmProvEntry.setStatus("mandatory")


class _MscTrkAtmMaximumErroredInterval_Type(Unsigned32):
    """Custom type mscTrkAtmMaximumErroredInterval based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 15),
    )


_MscTrkAtmMaximumErroredInterval_Type.__name__ = "Unsigned32"
_MscTrkAtmMaximumErroredInterval_Object = MibTableColumn
mscTrkAtmMaximumErroredInterval = _MscTrkAtmMaximumErroredInterval_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 3, 10, 1, 1),
    _MscTrkAtmMaximumErroredInterval_Type()
)
mscTrkAtmMaximumErroredInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscTrkAtmMaximumErroredInterval.setStatus("obsolete")


class _MscTrkAtmReceiveErrorSensitivity_Type(Unsigned32):
    """Custom type mscTrkAtmReceiveErrorSensitivity based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 10),
    )


_MscTrkAtmReceiveErrorSensitivity_Type.__name__ = "Unsigned32"
_MscTrkAtmReceiveErrorSensitivity_Object = MibTableColumn
mscTrkAtmReceiveErrorSensitivity = _MscTrkAtmReceiveErrorSensitivity_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 3, 10, 1, 2),
    _MscTrkAtmReceiveErrorSensitivity_Type()
)
mscTrkAtmReceiveErrorSensitivity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscTrkAtmReceiveErrorSensitivity.setStatus("mandatory")


class _MscTrkAtmAtmAccMaximumErroredInterval_Type(FixedPoint1):
    """Custom type mscTrkAtmAtmAccMaximumErroredInterval based on FixedPoint1"""
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


_MscTrkAtmAtmAccMaximumErroredInterval_Type.__name__ = "FixedPoint1"
_MscTrkAtmAtmAccMaximumErroredInterval_Object = MibTableColumn
mscTrkAtmAtmAccMaximumErroredInterval = _MscTrkAtmAtmAccMaximumErroredInterval_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 3, 10, 1, 3),
    _MscTrkAtmAtmAccMaximumErroredInterval_Type()
)
mscTrkAtmAtmAccMaximumErroredInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscTrkAtmAtmAccMaximumErroredInterval.setStatus("mandatory")
_MscTrkAtmInterfaceTable_Object = MibTable
mscTrkAtmInterfaceTable = _MscTrkAtmInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 3, 11)
)
if mibBuilder.loadTexts:
    mscTrkAtmInterfaceTable.setStatus("mandatory")
_MscTrkAtmInterfaceEntry_Object = MibTableRow
mscTrkAtmInterfaceEntry = _MscTrkAtmInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 3, 11, 1)
)
mscTrkAtmInterfaceEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TrunksMIB", "mscTrkIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmTrunksMIB", "mscTrkAtmIndex"),
)
if mibBuilder.loadTexts:
    mscTrkAtmInterfaceEntry.setStatus("mandatory")
_MscTrkAtmAtmConnection_Type = Link
_MscTrkAtmAtmConnection_Object = MibTableColumn
mscTrkAtmAtmConnection = _MscTrkAtmAtmConnection_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 3, 11, 1, 1),
    _MscTrkAtmAtmConnection_Type()
)
mscTrkAtmAtmConnection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscTrkAtmAtmConnection.setStatus("mandatory")


class _MscTrkAtmBwElastic_Type(Integer32):
    """Custom type mscTrkAtmBwElastic based on Integer32"""
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


_MscTrkAtmBwElastic_Type.__name__ = "Integer32"
_MscTrkAtmBwElastic_Object = MibTableColumn
mscTrkAtmBwElastic = _MscTrkAtmBwElastic_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 3, 11, 1, 2),
    _MscTrkAtmBwElastic_Type()
)
mscTrkAtmBwElastic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscTrkAtmBwElastic.setStatus("mandatory")


class _MscTrkAtmVccReportingBw_Type(Integer32):
    """Custom type mscTrkAtmVccReportingBw based on Integer32"""
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


_MscTrkAtmVccReportingBw_Type.__name__ = "Integer32"
_MscTrkAtmVccReportingBw_Object = MibTableColumn
mscTrkAtmVccReportingBw = _MscTrkAtmVccReportingBw_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 3, 11, 1, 3),
    _MscTrkAtmVccReportingBw_Type()
)
mscTrkAtmVccReportingBw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscTrkAtmVccReportingBw.setStatus("mandatory")
_MscTrkAtmStateTable_Object = MibTable
mscTrkAtmStateTable = _MscTrkAtmStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 3, 12)
)
if mibBuilder.loadTexts:
    mscTrkAtmStateTable.setStatus("mandatory")
_MscTrkAtmStateEntry_Object = MibTableRow
mscTrkAtmStateEntry = _MscTrkAtmStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 3, 12, 1)
)
mscTrkAtmStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TrunksMIB", "mscTrkIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmTrunksMIB", "mscTrkAtmIndex"),
)
if mibBuilder.loadTexts:
    mscTrkAtmStateEntry.setStatus("mandatory")


class _MscTrkAtmAdminState_Type(Integer32):
    """Custom type mscTrkAtmAdminState based on Integer32"""
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


_MscTrkAtmAdminState_Type.__name__ = "Integer32"
_MscTrkAtmAdminState_Object = MibTableColumn
mscTrkAtmAdminState = _MscTrkAtmAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 3, 12, 1, 1),
    _MscTrkAtmAdminState_Type()
)
mscTrkAtmAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkAtmAdminState.setStatus("mandatory")


class _MscTrkAtmOperationalState_Type(Integer32):
    """Custom type mscTrkAtmOperationalState based on Integer32"""
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


_MscTrkAtmOperationalState_Type.__name__ = "Integer32"
_MscTrkAtmOperationalState_Object = MibTableColumn
mscTrkAtmOperationalState = _MscTrkAtmOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 3, 12, 1, 2),
    _MscTrkAtmOperationalState_Type()
)
mscTrkAtmOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkAtmOperationalState.setStatus("mandatory")


class _MscTrkAtmUsageState_Type(Integer32):
    """Custom type mscTrkAtmUsageState based on Integer32"""
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


_MscTrkAtmUsageState_Type.__name__ = "Integer32"
_MscTrkAtmUsageState_Object = MibTableColumn
mscTrkAtmUsageState = _MscTrkAtmUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 3, 12, 1, 3),
    _MscTrkAtmUsageState_Type()
)
mscTrkAtmUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkAtmUsageState.setStatus("mandatory")


class _MscTrkAtmAvailabilityStatus_Type(OctetString):
    """Custom type mscTrkAtmAvailabilityStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_MscTrkAtmAvailabilityStatus_Type.__name__ = "OctetString"
_MscTrkAtmAvailabilityStatus_Object = MibTableColumn
mscTrkAtmAvailabilityStatus = _MscTrkAtmAvailabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 3, 12, 1, 4),
    _MscTrkAtmAvailabilityStatus_Type()
)
mscTrkAtmAvailabilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkAtmAvailabilityStatus.setStatus("mandatory")


class _MscTrkAtmProceduralStatus_Type(OctetString):
    """Custom type mscTrkAtmProceduralStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscTrkAtmProceduralStatus_Type.__name__ = "OctetString"
_MscTrkAtmProceduralStatus_Object = MibTableColumn
mscTrkAtmProceduralStatus = _MscTrkAtmProceduralStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 3, 12, 1, 5),
    _MscTrkAtmProceduralStatus_Type()
)
mscTrkAtmProceduralStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkAtmProceduralStatus.setStatus("mandatory")


class _MscTrkAtmControlStatus_Type(OctetString):
    """Custom type mscTrkAtmControlStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscTrkAtmControlStatus_Type.__name__ = "OctetString"
_MscTrkAtmControlStatus_Object = MibTableColumn
mscTrkAtmControlStatus = _MscTrkAtmControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 3, 12, 1, 6),
    _MscTrkAtmControlStatus_Type()
)
mscTrkAtmControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkAtmControlStatus.setStatus("mandatory")


class _MscTrkAtmAlarmStatus_Type(OctetString):
    """Custom type mscTrkAtmAlarmStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscTrkAtmAlarmStatus_Type.__name__ = "OctetString"
_MscTrkAtmAlarmStatus_Object = MibTableColumn
mscTrkAtmAlarmStatus = _MscTrkAtmAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 3, 12, 1, 7),
    _MscTrkAtmAlarmStatus_Type()
)
mscTrkAtmAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkAtmAlarmStatus.setStatus("mandatory")


class _MscTrkAtmStandbyStatus_Type(Integer32):
    """Custom type mscTrkAtmStandbyStatus based on Integer32"""
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


_MscTrkAtmStandbyStatus_Type.__name__ = "Integer32"
_MscTrkAtmStandbyStatus_Object = MibTableColumn
mscTrkAtmStandbyStatus = _MscTrkAtmStandbyStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 3, 12, 1, 8),
    _MscTrkAtmStandbyStatus_Type()
)
mscTrkAtmStandbyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkAtmStandbyStatus.setStatus("mandatory")


class _MscTrkAtmUnknownStatus_Type(Integer32):
    """Custom type mscTrkAtmUnknownStatus based on Integer32"""
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


_MscTrkAtmUnknownStatus_Type.__name__ = "Integer32"
_MscTrkAtmUnknownStatus_Object = MibTableColumn
mscTrkAtmUnknownStatus = _MscTrkAtmUnknownStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 3, 12, 1, 9),
    _MscTrkAtmUnknownStatus_Type()
)
mscTrkAtmUnknownStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkAtmUnknownStatus.setStatus("mandatory")
_MscTrkAtmUtilTable_Object = MibTable
mscTrkAtmUtilTable = _MscTrkAtmUtilTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 3, 14)
)
if mibBuilder.loadTexts:
    mscTrkAtmUtilTable.setStatus("mandatory")
_MscTrkAtmUtilEntry_Object = MibTableRow
mscTrkAtmUtilEntry = _MscTrkAtmUtilEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 3, 14, 1)
)
mscTrkAtmUtilEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TrunksMIB", "mscTrkIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmTrunksMIB", "mscTrkAtmIndex"),
)
if mibBuilder.loadTexts:
    mscTrkAtmUtilEntry.setStatus("mandatory")


class _MscTrkAtmMinorVccUtilAlarmThreshold_Type(Unsigned32):
    """Custom type mscTrkAtmMinorVccUtilAlarmThreshold based on Unsigned32"""
    defaultValue = 75

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_MscTrkAtmMinorVccUtilAlarmThreshold_Type.__name__ = "Unsigned32"
_MscTrkAtmMinorVccUtilAlarmThreshold_Object = MibTableColumn
mscTrkAtmMinorVccUtilAlarmThreshold = _MscTrkAtmMinorVccUtilAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 3, 14, 1, 1),
    _MscTrkAtmMinorVccUtilAlarmThreshold_Type()
)
mscTrkAtmMinorVccUtilAlarmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscTrkAtmMinorVccUtilAlarmThreshold.setStatus("mandatory")


class _MscTrkAtmMajorVccUtilAlarmThreshold_Type(Unsigned32):
    """Custom type mscTrkAtmMajorVccUtilAlarmThreshold based on Unsigned32"""
    defaultValue = 85

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_MscTrkAtmMajorVccUtilAlarmThreshold_Type.__name__ = "Unsigned32"
_MscTrkAtmMajorVccUtilAlarmThreshold_Object = MibTableColumn
mscTrkAtmMajorVccUtilAlarmThreshold = _MscTrkAtmMajorVccUtilAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 3, 14, 1, 2),
    _MscTrkAtmMajorVccUtilAlarmThreshold_Type()
)
mscTrkAtmMajorVccUtilAlarmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscTrkAtmMajorVccUtilAlarmThreshold.setStatus("mandatory")


class _MscTrkAtmCriticalVccUtilAlarmThreshold_Type(Unsigned32):
    """Custom type mscTrkAtmCriticalVccUtilAlarmThreshold based on Unsigned32"""
    defaultValue = 95

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_MscTrkAtmCriticalVccUtilAlarmThreshold_Type.__name__ = "Unsigned32"
_MscTrkAtmCriticalVccUtilAlarmThreshold_Object = MibTableColumn
mscTrkAtmCriticalVccUtilAlarmThreshold = _MscTrkAtmCriticalVccUtilAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 3, 14, 1, 3),
    _MscTrkAtmCriticalVccUtilAlarmThreshold_Type()
)
mscTrkAtmCriticalVccUtilAlarmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscTrkAtmCriticalVccUtilAlarmThreshold.setStatus("mandatory")


class _MscTrkAtmVccUtilAlarmStatus_Type(Integer32):
    """Custom type mscTrkAtmVccUtilAlarmStatus based on Integer32"""
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


_MscTrkAtmVccUtilAlarmStatus_Type.__name__ = "Integer32"
_MscTrkAtmVccUtilAlarmStatus_Object = MibTableColumn
mscTrkAtmVccUtilAlarmStatus = _MscTrkAtmVccUtilAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 3, 14, 1, 4),
    _MscTrkAtmVccUtilAlarmStatus_Type()
)
mscTrkAtmVccUtilAlarmStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscTrkAtmVccUtilAlarmStatus.setStatus("mandatory")
_MscTrkAtmStatsTable_Object = MibTable
mscTrkAtmStatsTable = _MscTrkAtmStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 3, 15)
)
if mibBuilder.loadTexts:
    mscTrkAtmStatsTable.setStatus("mandatory")
_MscTrkAtmStatsEntry_Object = MibTableRow
mscTrkAtmStatsEntry = _MscTrkAtmStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 3, 15, 1)
)
mscTrkAtmStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TrunksMIB", "mscTrkIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmTrunksMIB", "mscTrkAtmIndex"),
)
if mibBuilder.loadTexts:
    mscTrkAtmStatsEntry.setStatus("mandatory")


class _MscTrkAtmLastCalculatedVccUtilization_Type(Gauge32):
    """Custom type mscTrkAtmLastCalculatedVccUtilization based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_MscTrkAtmLastCalculatedVccUtilization_Type.__name__ = "Gauge32"
_MscTrkAtmLastCalculatedVccUtilization_Object = MibTableColumn
mscTrkAtmLastCalculatedVccUtilization = _MscTrkAtmLastCalculatedVccUtilization_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 3, 15, 1, 1),
    _MscTrkAtmLastCalculatedVccUtilization_Type()
)
mscTrkAtmLastCalculatedVccUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkAtmLastCalculatedVccUtilization.setStatus("mandatory")


class _MscTrkAtmLastCalculatedTxVccUtilization_Type(Gauge32):
    """Custom type mscTrkAtmLastCalculatedTxVccUtilization based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_MscTrkAtmLastCalculatedTxVccUtilization_Type.__name__ = "Gauge32"
_MscTrkAtmLastCalculatedTxVccUtilization_Object = MibTableColumn
mscTrkAtmLastCalculatedTxVccUtilization = _MscTrkAtmLastCalculatedTxVccUtilization_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 3, 15, 1, 2),
    _MscTrkAtmLastCalculatedTxVccUtilization_Type()
)
mscTrkAtmLastCalculatedTxVccUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkAtmLastCalculatedTxVccUtilization.setStatus("mandatory")
_AtmTrunksMIB_ObjectIdentity = ObjectIdentity
atmTrunksMIB = _AtmTrunksMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 59)
)
_AtmTrunksGroup_ObjectIdentity = ObjectIdentity
atmTrunksGroup = _AtmTrunksGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 59, 1)
)
_AtmTrunksGroupCA_ObjectIdentity = ObjectIdentity
atmTrunksGroupCA = _AtmTrunksGroupCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 59, 1, 1)
)
_AtmTrunksGroupCA02_ObjectIdentity = ObjectIdentity
atmTrunksGroupCA02 = _AtmTrunksGroupCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 59, 1, 1, 3)
)
_AtmTrunksGroupCA02A_ObjectIdentity = ObjectIdentity
atmTrunksGroupCA02A = _AtmTrunksGroupCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 59, 1, 1, 3, 2)
)
_AtmTrunksCapabilities_ObjectIdentity = ObjectIdentity
atmTrunksCapabilities = _AtmTrunksCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 59, 3)
)
_AtmTrunksCapabilitiesCA_ObjectIdentity = ObjectIdentity
atmTrunksCapabilitiesCA = _AtmTrunksCapabilitiesCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 59, 3, 1)
)
_AtmTrunksCapabilitiesCA02_ObjectIdentity = ObjectIdentity
atmTrunksCapabilitiesCA02 = _AtmTrunksCapabilitiesCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 59, 3, 1, 3)
)
_AtmTrunksCapabilitiesCA02A_ObjectIdentity = ObjectIdentity
atmTrunksCapabilitiesCA02A = _AtmTrunksCapabilitiesCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 59, 3, 1, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-MsCarrier-MscPassport-AtmTrunksMIB",
    **{"mscTrkAtm": mscTrkAtm,
       "mscTrkAtmRowStatusTable": mscTrkAtmRowStatusTable,
       "mscTrkAtmRowStatusEntry": mscTrkAtmRowStatusEntry,
       "mscTrkAtmRowStatus": mscTrkAtmRowStatus,
       "mscTrkAtmComponentName": mscTrkAtmComponentName,
       "mscTrkAtmStorageType": mscTrkAtmStorageType,
       "mscTrkAtmIndex": mscTrkAtmIndex,
       "mscTrkAtmProvTable": mscTrkAtmProvTable,
       "mscTrkAtmProvEntry": mscTrkAtmProvEntry,
       "mscTrkAtmMaximumErroredInterval": mscTrkAtmMaximumErroredInterval,
       "mscTrkAtmReceiveErrorSensitivity": mscTrkAtmReceiveErrorSensitivity,
       "mscTrkAtmAtmAccMaximumErroredInterval": mscTrkAtmAtmAccMaximumErroredInterval,
       "mscTrkAtmInterfaceTable": mscTrkAtmInterfaceTable,
       "mscTrkAtmInterfaceEntry": mscTrkAtmInterfaceEntry,
       "mscTrkAtmAtmConnection": mscTrkAtmAtmConnection,
       "mscTrkAtmBwElastic": mscTrkAtmBwElastic,
       "mscTrkAtmVccReportingBw": mscTrkAtmVccReportingBw,
       "mscTrkAtmStateTable": mscTrkAtmStateTable,
       "mscTrkAtmStateEntry": mscTrkAtmStateEntry,
       "mscTrkAtmAdminState": mscTrkAtmAdminState,
       "mscTrkAtmOperationalState": mscTrkAtmOperationalState,
       "mscTrkAtmUsageState": mscTrkAtmUsageState,
       "mscTrkAtmAvailabilityStatus": mscTrkAtmAvailabilityStatus,
       "mscTrkAtmProceduralStatus": mscTrkAtmProceduralStatus,
       "mscTrkAtmControlStatus": mscTrkAtmControlStatus,
       "mscTrkAtmAlarmStatus": mscTrkAtmAlarmStatus,
       "mscTrkAtmStandbyStatus": mscTrkAtmStandbyStatus,
       "mscTrkAtmUnknownStatus": mscTrkAtmUnknownStatus,
       "mscTrkAtmUtilTable": mscTrkAtmUtilTable,
       "mscTrkAtmUtilEntry": mscTrkAtmUtilEntry,
       "mscTrkAtmMinorVccUtilAlarmThreshold": mscTrkAtmMinorVccUtilAlarmThreshold,
       "mscTrkAtmMajorVccUtilAlarmThreshold": mscTrkAtmMajorVccUtilAlarmThreshold,
       "mscTrkAtmCriticalVccUtilAlarmThreshold": mscTrkAtmCriticalVccUtilAlarmThreshold,
       "mscTrkAtmVccUtilAlarmStatus": mscTrkAtmVccUtilAlarmStatus,
       "mscTrkAtmStatsTable": mscTrkAtmStatsTable,
       "mscTrkAtmStatsEntry": mscTrkAtmStatsEntry,
       "mscTrkAtmLastCalculatedVccUtilization": mscTrkAtmLastCalculatedVccUtilization,
       "mscTrkAtmLastCalculatedTxVccUtilization": mscTrkAtmLastCalculatedTxVccUtilization,
       "atmTrunksMIB": atmTrunksMIB,
       "atmTrunksGroup": atmTrunksGroup,
       "atmTrunksGroupCA": atmTrunksGroupCA,
       "atmTrunksGroupCA02": atmTrunksGroupCA02,
       "atmTrunksGroupCA02A": atmTrunksGroupCA02A,
       "atmTrunksCapabilities": atmTrunksCapabilities,
       "atmTrunksCapabilitiesCA": atmTrunksCapabilitiesCA,
       "atmTrunksCapabilitiesCA02": atmTrunksCapabilitiesCA02,
       "atmTrunksCapabilitiesCA02A": atmTrunksCapabilitiesCA02A}
)
