# SNMP MIB module (CISCO-ATM-NETWORK-CLOCK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-ATM-NETWORK-CLOCK-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:55:54 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(PhysicalIndex,
 entPhysicalIndex) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "PhysicalIndex",
    "entPhysicalIndex")

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
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoAtmNetworkClockMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 121)
)
ciscoAtmNetworkClockMIB.setRevisions(
        ("2008-02-18 00:00",
         "2001-12-11 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CncStratum(Integer32, TextualConvention):
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
        *(("other", 8),
          ("s1", 1),
          ("s2", 3),
          ("s2e", 2),
          ("s3", 5),
          ("s3e", 4),
          ("s4", 7),
          ("s4e", 6))
    )



class CncHealth(Integer32, TextualConvention):
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
        *(("bad", 2),
          ("good", 1),
          ("unknown", 3))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoAtmNetworkClockMIBObjects_ObjectIdentity = ObjectIdentity
ciscoAtmNetworkClockMIBObjects = _CiscoAtmNetworkClockMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 121, 1)
)
_CncGlobal_ObjectIdentity = ObjectIdentity
cncGlobal = _CncGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 121, 1, 1)
)


class _CncDistributionMethod_Type(Integer32):
    """Custom type cncDistributionMethod based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("manual", 2),
          ("ncdp", 1))
    )


_CncDistributionMethod_Type.__name__ = "Integer32"
_CncDistributionMethod_Object = MibScalar
cncDistributionMethod = _CncDistributionMethod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 121, 1, 1, 1),
    _CncDistributionMethod_Type()
)
cncDistributionMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cncDistributionMethod.setStatus("current")


class _CncNotificationOnChange_Type(TruthValue):
    """Custom type cncNotificationOnChange based on TruthValue"""


_CncNotificationOnChange_Object = MibScalar
cncNotificationOnChange = _CncNotificationOnChange_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 121, 1, 1, 2),
    _CncNotificationOnChange_Type()
)
cncNotificationOnChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cncNotificationOnChange.setStatus("current")
_CncNodeStratum_Type = CncStratum
_CncNodeStratum_Object = MibScalar
cncNodeStratum = _CncNodeStratum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 121, 1, 1, 3),
    _CncNodeStratum_Type()
)
cncNodeStratum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cncNodeStratum.setStatus("current")


class _CncNcdpMaxDiameter_Type(Integer32):
    """Custom type cncNcdpMaxDiameter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 255),
    )


_CncNcdpMaxDiameter_Type.__name__ = "Integer32"
_CncNcdpMaxDiameter_Object = MibScalar
cncNcdpMaxDiameter = _CncNcdpMaxDiameter_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 121, 1, 1, 4),
    _CncNcdpMaxDiameter_Type()
)
cncNcdpMaxDiameter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cncNcdpMaxDiameter.setStatus("current")


class _CncNcdpMessageInterval_Type(Integer32):
    """Custom type cncNcdpMessageInterval based on Integer32"""
    defaultValue = 500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(75, 60000),
    )


_CncNcdpMessageInterval_Type.__name__ = "Integer32"
_CncNcdpMessageInterval_Object = MibScalar
cncNcdpMessageInterval = _CncNcdpMessageInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 121, 1, 1, 5),
    _CncNcdpMessageInterval_Type()
)
cncNcdpMessageInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cncNcdpMessageInterval.setStatus("current")
if mibBuilder.loadTexts:
    cncNcdpMessageInterval.setUnits("milliseconds")


class _CncNcdpHoldTime_Type(Integer32):
    """Custom type cncNcdpHoldTime based on Integer32"""
    defaultValue = 500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(75, 60000),
    )


_CncNcdpHoldTime_Type.__name__ = "Integer32"
_CncNcdpHoldTime_Object = MibScalar
cncNcdpHoldTime = _CncNcdpHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 121, 1, 1, 6),
    _CncNcdpHoldTime_Type()
)
cncNcdpHoldTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cncNcdpHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    cncNcdpHoldTime.setUnits("milliseconds")


class _CncSourceChangeReason_Type(Integer32):
    """Custom type cncSourceChangeReason based on Integer32"""
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
        *(("lossOfActivity", 3),
          ("lossOfLock", 2),
          ("ncdpRestructure", 4),
          ("none", 1),
          ("other", 5))
    )


_CncSourceChangeReason_Type.__name__ = "Integer32"
_CncSourceChangeReason_Object = MibScalar
cncSourceChangeReason = _CncSourceChangeReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 121, 1, 1, 7),
    _CncSourceChangeReason_Type()
)
cncSourceChangeReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cncSourceChangeReason.setStatus("current")


class _CncSourceChangeTimeStamp_Type(TimeStamp):
    """Custom type cncSourceChangeTimeStamp based on TimeStamp"""
    defaultValue = 0


_CncSourceChangeTimeStamp_Object = MibScalar
cncSourceChangeTimeStamp = _CncSourceChangeTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 121, 1, 1, 8),
    _CncSourceChangeTimeStamp_Type()
)
cncSourceChangeTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cncSourceChangeTimeStamp.setStatus("current")
_CncRootClockSource_Type = PhysicalIndex
_CncRootClockSource_Object = MibScalar
cncRootClockSource = _CncRootClockSource_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 121, 1, 1, 9),
    _CncRootClockSource_Type()
)
cncRootClockSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cncRootClockSource.setStatus("current")
_CncManualSource_ObjectIdentity = ObjectIdentity
cncManualSource = _CncManualSource_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 121, 1, 2)
)
_CncManualSourceTable_Object = MibTable
cncManualSourceTable = _CncManualSourceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 121, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cncManualSourceTable.setStatus("current")
_CncManualSourceEntry_Object = MibTableRow
cncManualSourceEntry = _CncManualSourceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 121, 1, 2, 1, 1)
)
cncManualSourceEntry.setIndexNames(
    (0, "CISCO-ATM-NETWORK-CLOCK-MIB", "cncManualSourcePriority"),
)
if mibBuilder.loadTexts:
    cncManualSourceEntry.setStatus("current")


class _CncManualSourcePriority_Type(Integer32):
    """Custom type cncManualSourcePriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("default", 3),
          ("primary", 1),
          ("secondary", 2))
    )


_CncManualSourcePriority_Type.__name__ = "Integer32"
_CncManualSourcePriority_Object = MibTableColumn
cncManualSourcePriority = _CncManualSourcePriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 121, 1, 2, 1, 1, 1),
    _CncManualSourcePriority_Type()
)
cncManualSourcePriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cncManualSourcePriority.setStatus("current")
_CncManualSourceId_Type = PhysicalIndex
_CncManualSourceId_Object = MibTableColumn
cncManualSourceId = _CncManualSourceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 121, 1, 2, 1, 1, 2),
    _CncManualSourceId_Type()
)
cncManualSourceId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cncManualSourceId.setStatus("current")
_CncManualSourceHealth_Type = CncHealth
_CncManualSourceHealth_Object = MibTableColumn
cncManualSourceHealth = _CncManualSourceHealth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 121, 1, 2, 1, 1, 3),
    _CncManualSourceHealth_Type()
)
cncManualSourceHealth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cncManualSourceHealth.setStatus("current")
_CncManualRowStatus_Type = RowStatus
_CncManualRowStatus_Object = MibTableColumn
cncManualRowStatus = _CncManualRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 121, 1, 2, 1, 1, 4),
    _CncManualRowStatus_Type()
)
cncManualRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cncManualRowStatus.setStatus("current")
_CncNcdpSource_ObjectIdentity = ObjectIdentity
cncNcdpSource = _CncNcdpSource_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 121, 1, 3)
)
_CncNcdpSourceTable_Object = MibTable
cncNcdpSourceTable = _CncNcdpSourceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 121, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cncNcdpSourceTable.setStatus("current")
_CncNcdpSourceEntry_Object = MibTableRow
cncNcdpSourceEntry = _CncNcdpSourceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 121, 1, 3, 1, 1)
)
cncNcdpSourceEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    cncNcdpSourceEntry.setStatus("current")
_CncNcdpBestClockSource_Type = TruthValue
_CncNcdpBestClockSource_Object = MibTableColumn
cncNcdpBestClockSource = _CncNcdpBestClockSource_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 121, 1, 3, 1, 1, 1),
    _CncNcdpBestClockSource_Type()
)
cncNcdpBestClockSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cncNcdpBestClockSource.setStatus("current")


class _CncNcdpPriority_Type(Integer32):
    """Custom type cncNcdpPriority based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_CncNcdpPriority_Type.__name__ = "Integer32"
_CncNcdpPriority_Object = MibTableColumn
cncNcdpPriority = _CncNcdpPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 121, 1, 3, 1, 1, 2),
    _CncNcdpPriority_Type()
)
cncNcdpPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cncNcdpPriority.setStatus("current")
_CncNcdpStratum_Type = CncStratum
_CncNcdpStratum_Object = MibTableColumn
cncNcdpStratum = _CncNcdpStratum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 121, 1, 3, 1, 1, 3),
    _CncNcdpStratum_Type()
)
cncNcdpStratum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cncNcdpStratum.setStatus("current")


class _CncNcdpPRSReference_Type(Integer32):
    """Custom type cncNcdpPRSReference based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("external", 2),
          ("internal", 1))
    )


_CncNcdpPRSReference_Type.__name__ = "Integer32"
_CncNcdpPRSReference_Object = MibTableColumn
cncNcdpPRSReference = _CncNcdpPRSReference_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 121, 1, 3, 1, 1, 4),
    _CncNcdpPRSReference_Type()
)
cncNcdpPRSReference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cncNcdpPRSReference.setStatus("current")
_CncNcdpSourceHealth_Type = CncHealth
_CncNcdpSourceHealth_Object = MibTableColumn
cncNcdpSourceHealth = _CncNcdpSourceHealth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 121, 1, 3, 1, 1, 5),
    _CncNcdpSourceHealth_Type()
)
cncNcdpSourceHealth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cncNcdpSourceHealth.setStatus("current")
_CncNcdpRowStatus_Type = RowStatus
_CncNcdpRowStatus_Object = MibTableColumn
cncNcdpRowStatus = _CncNcdpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 121, 1, 3, 1, 1, 6),
    _CncNcdpRowStatus_Type()
)
cncNcdpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cncNcdpRowStatus.setStatus("current")
_CncNcdp_ObjectIdentity = ObjectIdentity
cncNcdp = _CncNcdp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 121, 1, 4)
)
_CncNcdpAtmTable_Object = MibTable
cncNcdpAtmTable = _CncNcdpAtmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 121, 1, 4, 1)
)
if mibBuilder.loadTexts:
    cncNcdpAtmTable.setStatus("current")
_CncNcdpAtmEntry_Object = MibTableRow
cncNcdpAtmEntry = _CncNcdpAtmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 121, 1, 4, 1, 1)
)
cncNcdpAtmEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    cncNcdpAtmEntry.setStatus("current")
_CncNcdpEnable_Type = TruthValue
_CncNcdpEnable_Object = MibTableColumn
cncNcdpEnable = _CncNcdpEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 121, 1, 4, 1, 1, 1),
    _CncNcdpEnable_Type()
)
cncNcdpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cncNcdpEnable.setStatus("current")


class _CncNcdpAdminWeight_Type(Integer32):
    """Custom type cncNcdpAdminWeight based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16777215),
    )


_CncNcdpAdminWeight_Type.__name__ = "Integer32"
_CncNcdpAdminWeight_Object = MibTableColumn
cncNcdpAdminWeight = _CncNcdpAdminWeight_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 121, 1, 4, 1, 1, 2),
    _CncNcdpAdminWeight_Type()
)
cncNcdpAdminWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cncNcdpAdminWeight.setStatus("current")


class _CncNcdpVpi_Type(Integer32):
    """Custom type cncNcdpVpi based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_CncNcdpVpi_Type.__name__ = "Integer32"
_CncNcdpVpi_Object = MibTableColumn
cncNcdpVpi = _CncNcdpVpi_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 121, 1, 4, 1, 1, 3),
    _CncNcdpVpi_Type()
)
cncNcdpVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cncNcdpVpi.setStatus("current")


class _CncNcdpVci_Type(Integer32):
    """Custom type cncNcdpVci based on Integer32"""
    defaultValue = 34

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CncNcdpVci_Type.__name__ = "Integer32"
_CncNcdpVci_Object = MibTableColumn
cncNcdpVci = _CncNcdpVci_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 121, 1, 4, 1, 1, 4),
    _CncNcdpVci_Type()
)
cncNcdpVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cncNcdpVci.setStatus("current")
_CncNcdpHealth_Type = CncHealth
_CncNcdpHealth_Object = MibTableColumn
cncNcdpHealth = _CncNcdpHealth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 121, 1, 4, 1, 1, 5),
    _CncNcdpHealth_Type()
)
cncNcdpHealth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cncNcdpHealth.setStatus("current")
_CiscoAtmNetworkClockNotificationPrefix_ObjectIdentity = ObjectIdentity
ciscoAtmNetworkClockNotificationPrefix = _CiscoAtmNetworkClockNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 121, 2)
)
_CiscoAtmNetworkClockMIBNotifications_ObjectIdentity = ObjectIdentity
ciscoAtmNetworkClockMIBNotifications = _CiscoAtmNetworkClockMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 121, 2, 0)
)
_CiscoAtmNetworkClockConformance_ObjectIdentity = ObjectIdentity
ciscoAtmNetworkClockConformance = _CiscoAtmNetworkClockConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 121, 3)
)
_CiscoAtmNetworkClockMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoAtmNetworkClockMIBCompliances = _CiscoAtmNetworkClockMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 121, 3, 1)
)
_CiscoAtmNetworkClockMIBGroups_ObjectIdentity = ObjectIdentity
ciscoAtmNetworkClockMIBGroups = _CiscoAtmNetworkClockMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 121, 3, 2)
)

# Managed Objects groups

cncGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 121, 3, 2, 1)
)
cncGroup.setObjects(
      *(("CISCO-ATM-NETWORK-CLOCK-MIB", "cncDistributionMethod"),
        ("CISCO-ATM-NETWORK-CLOCK-MIB", "cncNotificationOnChange"),
        ("CISCO-ATM-NETWORK-CLOCK-MIB", "cncNodeStratum"),
        ("CISCO-ATM-NETWORK-CLOCK-MIB", "cncNcdpMaxDiameter"),
        ("CISCO-ATM-NETWORK-CLOCK-MIB", "cncNcdpMessageInterval"),
        ("CISCO-ATM-NETWORK-CLOCK-MIB", "cncNcdpHoldTime"),
        ("CISCO-ATM-NETWORK-CLOCK-MIB", "cncSourceChangeReason"),
        ("CISCO-ATM-NETWORK-CLOCK-MIB", "cncSourceChangeTimeStamp"),
        ("CISCO-ATM-NETWORK-CLOCK-MIB", "cncRootClockSource"),
        ("CISCO-ATM-NETWORK-CLOCK-MIB", "cncManualSourceId"),
        ("CISCO-ATM-NETWORK-CLOCK-MIB", "cncManualSourceHealth"),
        ("CISCO-ATM-NETWORK-CLOCK-MIB", "cncManualRowStatus"),
        ("CISCO-ATM-NETWORK-CLOCK-MIB", "cncNcdpBestClockSource"),
        ("CISCO-ATM-NETWORK-CLOCK-MIB", "cncNcdpPriority"),
        ("CISCO-ATM-NETWORK-CLOCK-MIB", "cncNcdpStratum"),
        ("CISCO-ATM-NETWORK-CLOCK-MIB", "cncNcdpPRSReference"),
        ("CISCO-ATM-NETWORK-CLOCK-MIB", "cncNcdpSourceHealth"),
        ("CISCO-ATM-NETWORK-CLOCK-MIB", "cncNcdpRowStatus"),
        ("CISCO-ATM-NETWORK-CLOCK-MIB", "cncNcdpEnable"),
        ("CISCO-ATM-NETWORK-CLOCK-MIB", "cncNcdpAdminWeight"),
        ("CISCO-ATM-NETWORK-CLOCK-MIB", "cncNcdpVpi"),
        ("CISCO-ATM-NETWORK-CLOCK-MIB", "cncNcdpVci"),
        ("CISCO-ATM-NETWORK-CLOCK-MIB", "cncNcdpHealth"))
)
if mibBuilder.loadTexts:
    cncGroup.setStatus("current")


# Notification objects

cncNotifySourceChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 121, 2, 0, 1)
)
cncNotifySourceChange.setObjects(
    ("CISCO-ATM-NETWORK-CLOCK-MIB", "cncSourceChangeReason")
)
if mibBuilder.loadTexts:
    cncNotifySourceChange.setStatus(
        "current"
    )


# Notifications groups

cncNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 121, 3, 2, 2)
)
cncNotificationGroup.setObjects(
    ("CISCO-ATM-NETWORK-CLOCK-MIB", "cncNotifySourceChange")
)
if mibBuilder.loadTexts:
    cncNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

cncMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 121, 3, 1, 1)
)
if mibBuilder.loadTexts:
    cncMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-ATM-NETWORK-CLOCK-MIB",
    **{"CncStratum": CncStratum,
       "CncHealth": CncHealth,
       "ciscoAtmNetworkClockMIB": ciscoAtmNetworkClockMIB,
       "ciscoAtmNetworkClockMIBObjects": ciscoAtmNetworkClockMIBObjects,
       "cncGlobal": cncGlobal,
       "cncDistributionMethod": cncDistributionMethod,
       "cncNotificationOnChange": cncNotificationOnChange,
       "cncNodeStratum": cncNodeStratum,
       "cncNcdpMaxDiameter": cncNcdpMaxDiameter,
       "cncNcdpMessageInterval": cncNcdpMessageInterval,
       "cncNcdpHoldTime": cncNcdpHoldTime,
       "cncSourceChangeReason": cncSourceChangeReason,
       "cncSourceChangeTimeStamp": cncSourceChangeTimeStamp,
       "cncRootClockSource": cncRootClockSource,
       "cncManualSource": cncManualSource,
       "cncManualSourceTable": cncManualSourceTable,
       "cncManualSourceEntry": cncManualSourceEntry,
       "cncManualSourcePriority": cncManualSourcePriority,
       "cncManualSourceId": cncManualSourceId,
       "cncManualSourceHealth": cncManualSourceHealth,
       "cncManualRowStatus": cncManualRowStatus,
       "cncNcdpSource": cncNcdpSource,
       "cncNcdpSourceTable": cncNcdpSourceTable,
       "cncNcdpSourceEntry": cncNcdpSourceEntry,
       "cncNcdpBestClockSource": cncNcdpBestClockSource,
       "cncNcdpPriority": cncNcdpPriority,
       "cncNcdpStratum": cncNcdpStratum,
       "cncNcdpPRSReference": cncNcdpPRSReference,
       "cncNcdpSourceHealth": cncNcdpSourceHealth,
       "cncNcdpRowStatus": cncNcdpRowStatus,
       "cncNcdp": cncNcdp,
       "cncNcdpAtmTable": cncNcdpAtmTable,
       "cncNcdpAtmEntry": cncNcdpAtmEntry,
       "cncNcdpEnable": cncNcdpEnable,
       "cncNcdpAdminWeight": cncNcdpAdminWeight,
       "cncNcdpVpi": cncNcdpVpi,
       "cncNcdpVci": cncNcdpVci,
       "cncNcdpHealth": cncNcdpHealth,
       "ciscoAtmNetworkClockNotificationPrefix": ciscoAtmNetworkClockNotificationPrefix,
       "ciscoAtmNetworkClockMIBNotifications": ciscoAtmNetworkClockMIBNotifications,
       "cncNotifySourceChange": cncNotifySourceChange,
       "ciscoAtmNetworkClockConformance": ciscoAtmNetworkClockConformance,
       "ciscoAtmNetworkClockMIBCompliances": ciscoAtmNetworkClockMIBCompliances,
       "cncMIBCompliance": cncMIBCompliance,
       "ciscoAtmNetworkClockMIBGroups": ciscoAtmNetworkClockMIBGroups,
       "cncGroup": cncGroup,
       "cncNotificationGroup": cncNotificationGroup}
)
