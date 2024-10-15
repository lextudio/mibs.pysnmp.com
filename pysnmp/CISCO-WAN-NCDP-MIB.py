# SNMP MIB module (CISCO-WAN-NCDP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-WAN-NCDP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:13:10 2024
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

(InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero",
    "ifIndex")

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

ciscoWanNcdpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 223)
)
ciscoWanNcdpMIB.setRevisions(
        ("2001-11-07 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class ClockStratum(Integer32, TextualConvention):
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
        *(("other", 1),
          ("s1", 2),
          ("s2", 4),
          ("s2e", 3),
          ("s3", 6),
          ("s3e", 5),
          ("s4", 8),
          ("s4e", 7))
    )



class ClockHealthStatus(Integer32, TextualConvention):
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



class ClockSourceIndex(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )



# MIB Managed Objects in the order of their OIDs

_CwnMIBObjects_ObjectIdentity = ObjectIdentity
cwnMIBObjects = _CwnMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 223, 1)
)
_CwnGlobal_ObjectIdentity = ObjectIdentity
cwnGlobal = _CwnGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 223, 1, 1)
)


class _CwnDistributionMethod_Type(Integer32):
    """Custom type cwnDistributionMethod based on Integer32"""
    defaultValue = 1

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


_CwnDistributionMethod_Type.__name__ = "Integer32"
_CwnDistributionMethod_Object = MibScalar
cwnDistributionMethod = _CwnDistributionMethod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 223, 1, 1, 1),
    _CwnDistributionMethod_Type()
)
cwnDistributionMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwnDistributionMethod.setStatus("current")


class _CwnNodeStratum_Type(ClockStratum):
    """Custom type cwnNodeStratum based on ClockStratum"""


_CwnNodeStratum_Object = MibScalar
cwnNodeStratum = _CwnNodeStratum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 223, 1, 1, 2),
    _CwnNodeStratum_Type()
)
cwnNodeStratum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwnNodeStratum.setStatus("current")


class _CwnMaxDiameter_Type(Integer32):
    """Custom type cwnMaxDiameter based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 255),
    )


_CwnMaxDiameter_Type.__name__ = "Integer32"
_CwnMaxDiameter_Object = MibScalar
cwnMaxDiameter = _CwnMaxDiameter_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 223, 1, 1, 3),
    _CwnMaxDiameter_Type()
)
cwnMaxDiameter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwnMaxDiameter.setStatus("current")


class _CwnMessageInterval_Type(Integer32):
    """Custom type cwnMessageInterval based on Integer32"""
    defaultValue = 500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(75, 60000),
    )


_CwnMessageInterval_Type.__name__ = "Integer32"
_CwnMessageInterval_Object = MibScalar
cwnMessageInterval = _CwnMessageInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 223, 1, 1, 4),
    _CwnMessageInterval_Type()
)
cwnMessageInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwnMessageInterval.setStatus("current")
if mibBuilder.loadTexts:
    cwnMessageInterval.setUnits("milliseconds")


class _CwnHoldTime_Type(Integer32):
    """Custom type cwnHoldTime based on Integer32"""
    defaultValue = 500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(75, 60000),
    )


_CwnHoldTime_Type.__name__ = "Integer32"
_CwnHoldTime_Object = MibScalar
cwnHoldTime = _CwnHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 223, 1, 1, 5),
    _CwnHoldTime_Type()
)
cwnHoldTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwnHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    cwnHoldTime.setUnits("milliseconds")


class _CwnChangeReason_Type(Integer32):
    """Custom type cwnChangeReason based on Integer32"""
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
        *(("lossOfActivity", 4),
          ("lossOfLock", 3),
          ("ncdpRestructure", 5),
          ("none", 2),
          ("other", 1))
    )


_CwnChangeReason_Type.__name__ = "Integer32"
_CwnChangeReason_Object = MibScalar
cwnChangeReason = _CwnChangeReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 223, 1, 1, 6),
    _CwnChangeReason_Type()
)
cwnChangeReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwnChangeReason.setStatus("current")


class _CwnChangeTimeStamp_Type(TimeStamp):
    """Custom type cwnChangeTimeStamp based on TimeStamp"""
    defaultValue = 0


_CwnChangeTimeStamp_Object = MibScalar
cwnChangeTimeStamp = _CwnChangeTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 223, 1, 1, 7),
    _CwnChangeTimeStamp_Type()
)
cwnChangeTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwnChangeTimeStamp.setStatus("current")
_CwnRootClockSource_Type = ClockSourceIndex
_CwnRootClockSource_Object = MibScalar
cwnRootClockSource = _CwnRootClockSource_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 223, 1, 1, 8),
    _CwnRootClockSource_Type()
)
cwnRootClockSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwnRootClockSource.setStatus("current")
_CwnClockSource_ObjectIdentity = ObjectIdentity
cwnClockSource = _CwnClockSource_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 223, 1, 2)
)
_CwnClockSourceTable_Object = MibTable
cwnClockSourceTable = _CwnClockSourceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 223, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cwnClockSourceTable.setStatus("current")
_CwnClockSourceEntry_Object = MibTableRow
cwnClockSourceEntry = _CwnClockSourceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 223, 1, 2, 1, 1)
)
cwnClockSourceEntry.setIndexNames(
    (0, "CISCO-WAN-NCDP-MIB", "cwnClockSourceIndex"),
)
if mibBuilder.loadTexts:
    cwnClockSourceEntry.setStatus("current")
_CwnClockSourceIndex_Type = ClockSourceIndex
_CwnClockSourceIndex_Object = MibTableColumn
cwnClockSourceIndex = _CwnClockSourceIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 223, 1, 2, 1, 1, 1),
    _CwnClockSourceIndex_Type()
)
cwnClockSourceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwnClockSourceIndex.setStatus("current")
_CwnClockSourceDesc_Type = DisplayString
_CwnClockSourceDesc_Object = MibTableColumn
cwnClockSourceDesc = _CwnClockSourceDesc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 223, 1, 2, 1, 1, 2),
    _CwnClockSourceDesc_Type()
)
cwnClockSourceDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwnClockSourceDesc.setStatus("current")
_CwnInterfaceIndex_Type = InterfaceIndexOrZero
_CwnInterfaceIndex_Object = MibTableColumn
cwnInterfaceIndex = _CwnInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 223, 1, 2, 1, 1, 3),
    _CwnInterfaceIndex_Type()
)
cwnInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwnInterfaceIndex.setStatus("current")


class _CwnOtherClockSource_Type(Integer32):
    """Custom type cwnOtherClockSource based on Integer32"""
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
        *(("bitsClockE1", 3),
          ("bitsClockT1", 4),
          ("internalOscillator", 2),
          ("none", 1))
    )


_CwnOtherClockSource_Type.__name__ = "Integer32"
_CwnOtherClockSource_Object = MibTableColumn
cwnOtherClockSource = _CwnOtherClockSource_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 223, 1, 2, 1, 1, 4),
    _CwnOtherClockSource_Type()
)
cwnOtherClockSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwnOtherClockSource.setStatus("current")
_CwnManualSource_ObjectIdentity = ObjectIdentity
cwnManualSource = _CwnManualSource_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 223, 1, 3)
)
_CwnManualSourceTable_Object = MibTable
cwnManualSourceTable = _CwnManualSourceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 223, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cwnManualSourceTable.setStatus("current")
_CwnManualSourceEntry_Object = MibTableRow
cwnManualSourceEntry = _CwnManualSourceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 223, 1, 3, 1, 1)
)
cwnManualSourceEntry.setIndexNames(
    (0, "CISCO-WAN-NCDP-MIB", "cwnManualSourcePriority"),
)
if mibBuilder.loadTexts:
    cwnManualSourceEntry.setStatus("current")


class _CwnManualSourcePriority_Type(Integer32):
    """Custom type cwnManualSourcePriority based on Integer32"""
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


_CwnManualSourcePriority_Type.__name__ = "Integer32"
_CwnManualSourcePriority_Object = MibTableColumn
cwnManualSourcePriority = _CwnManualSourcePriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 223, 1, 3, 1, 1, 1),
    _CwnManualSourcePriority_Type()
)
cwnManualSourcePriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwnManualSourcePriority.setStatus("current")
_CwnManualSourceIndex_Type = ClockSourceIndex
_CwnManualSourceIndex_Object = MibTableColumn
cwnManualSourceIndex = _CwnManualSourceIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 223, 1, 3, 1, 1, 2),
    _CwnManualSourceIndex_Type()
)
cwnManualSourceIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwnManualSourceIndex.setStatus("current")
_CwnManualClockHealth_Type = ClockHealthStatus
_CwnManualClockHealth_Object = MibTableColumn
cwnManualClockHealth = _CwnManualClockHealth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 223, 1, 3, 1, 1, 3),
    _CwnManualClockHealth_Type()
)
cwnManualClockHealth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwnManualClockHealth.setStatus("current")
_CwnManualRowStatus_Type = RowStatus
_CwnManualRowStatus_Object = MibTableColumn
cwnManualRowStatus = _CwnManualRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 223, 1, 3, 1, 1, 4),
    _CwnManualRowStatus_Type()
)
cwnManualRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwnManualRowStatus.setStatus("current")
_CwnAtmSource_ObjectIdentity = ObjectIdentity
cwnAtmSource = _CwnAtmSource_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 223, 1, 4)
)
_CwnAtmSourceTable_Object = MibTable
cwnAtmSourceTable = _CwnAtmSourceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 223, 1, 4, 1)
)
if mibBuilder.loadTexts:
    cwnAtmSourceTable.setStatus("current")
_CwnAtmSourceEntry_Object = MibTableRow
cwnAtmSourceEntry = _CwnAtmSourceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 223, 1, 4, 1, 1)
)
cwnAtmSourceEntry.setIndexNames(
    (0, "CISCO-WAN-NCDP-MIB", "cwnClockSourceIndex"),
)
if mibBuilder.loadTexts:
    cwnAtmSourceEntry.setStatus("current")
_CwnAtmSourceBestClockSource_Type = TruthValue
_CwnAtmSourceBestClockSource_Object = MibTableColumn
cwnAtmSourceBestClockSource = _CwnAtmSourceBestClockSource_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 223, 1, 4, 1, 1, 1),
    _CwnAtmSourceBestClockSource_Type()
)
cwnAtmSourceBestClockSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwnAtmSourceBestClockSource.setStatus("current")


class _CwnAtmSourcePriority_Type(Integer32):
    """Custom type cwnAtmSourcePriority based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_CwnAtmSourcePriority_Type.__name__ = "Integer32"
_CwnAtmSourcePriority_Object = MibTableColumn
cwnAtmSourcePriority = _CwnAtmSourcePriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 223, 1, 4, 1, 1, 2),
    _CwnAtmSourcePriority_Type()
)
cwnAtmSourcePriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwnAtmSourcePriority.setStatus("current")


class _CwnAtmSourceStratum_Type(ClockStratum):
    """Custom type cwnAtmSourceStratum based on ClockStratum"""


_CwnAtmSourceStratum_Object = MibTableColumn
cwnAtmSourceStratum = _CwnAtmSourceStratum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 223, 1, 4, 1, 1, 3),
    _CwnAtmSourceStratum_Type()
)
cwnAtmSourceStratum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwnAtmSourceStratum.setStatus("current")


class _CwnAtmSourcePRSReference_Type(Integer32):
    """Custom type cwnAtmSourcePRSReference based on Integer32"""
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


_CwnAtmSourcePRSReference_Type.__name__ = "Integer32"
_CwnAtmSourcePRSReference_Object = MibTableColumn
cwnAtmSourcePRSReference = _CwnAtmSourcePRSReference_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 223, 1, 4, 1, 1, 4),
    _CwnAtmSourcePRSReference_Type()
)
cwnAtmSourcePRSReference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwnAtmSourcePRSReference.setStatus("current")
_CwnAtmSourceClockHealth_Type = ClockHealthStatus
_CwnAtmSourceClockHealth_Object = MibTableColumn
cwnAtmSourceClockHealth = _CwnAtmSourceClockHealth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 223, 1, 4, 1, 1, 5),
    _CwnAtmSourceClockHealth_Type()
)
cwnAtmSourceClockHealth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwnAtmSourceClockHealth.setStatus("current")
_CwnAtmSourceRowStatus_Type = RowStatus
_CwnAtmSourceRowStatus_Object = MibTableColumn
cwnAtmSourceRowStatus = _CwnAtmSourceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 223, 1, 4, 1, 1, 6),
    _CwnAtmSourceRowStatus_Type()
)
cwnAtmSourceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwnAtmSourceRowStatus.setStatus("current")
_CwnAtmInterface_ObjectIdentity = ObjectIdentity
cwnAtmInterface = _CwnAtmInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 223, 1, 5)
)
_CwnAtmInterfaceTable_Object = MibTable
cwnAtmInterfaceTable = _CwnAtmInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 223, 1, 5, 1)
)
if mibBuilder.loadTexts:
    cwnAtmInterfaceTable.setStatus("current")
_CwnAtmInterfaceEntry_Object = MibTableRow
cwnAtmInterfaceEntry = _CwnAtmInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 223, 1, 5, 1, 1)
)
cwnAtmInterfaceEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cwnAtmInterfaceEntry.setStatus("current")


class _CwnAtmInterfaceEnable_Type(TruthValue):
    """Custom type cwnAtmInterfaceEnable based on TruthValue"""


_CwnAtmInterfaceEnable_Object = MibTableColumn
cwnAtmInterfaceEnable = _CwnAtmInterfaceEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 223, 1, 5, 1, 1, 1),
    _CwnAtmInterfaceEnable_Type()
)
cwnAtmInterfaceEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwnAtmInterfaceEnable.setStatus("current")


class _CwnAtmInterfaceAdminWeight_Type(Integer32):
    """Custom type cwnAtmInterfaceAdminWeight based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16777215),
    )


_CwnAtmInterfaceAdminWeight_Type.__name__ = "Integer32"
_CwnAtmInterfaceAdminWeight_Object = MibTableColumn
cwnAtmInterfaceAdminWeight = _CwnAtmInterfaceAdminWeight_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 223, 1, 5, 1, 1, 2),
    _CwnAtmInterfaceAdminWeight_Type()
)
cwnAtmInterfaceAdminWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwnAtmInterfaceAdminWeight.setStatus("current")


class _CwnAtmInterfaceVpi_Type(Integer32):
    """Custom type cwnAtmInterfaceVpi based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_CwnAtmInterfaceVpi_Type.__name__ = "Integer32"
_CwnAtmInterfaceVpi_Object = MibTableColumn
cwnAtmInterfaceVpi = _CwnAtmInterfaceVpi_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 223, 1, 5, 1, 1, 3),
    _CwnAtmInterfaceVpi_Type()
)
cwnAtmInterfaceVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwnAtmInterfaceVpi.setStatus("current")


class _CwnAtmInterfaceVci_Type(Integer32):
    """Custom type cwnAtmInterfaceVci based on Integer32"""
    defaultValue = 34

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CwnAtmInterfaceVci_Type.__name__ = "Integer32"
_CwnAtmInterfaceVci_Object = MibTableColumn
cwnAtmInterfaceVci = _CwnAtmInterfaceVci_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 223, 1, 5, 1, 1, 4),
    _CwnAtmInterfaceVci_Type()
)
cwnAtmInterfaceVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwnAtmInterfaceVci.setStatus("current")
_CiscoWanNcdpMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
ciscoWanNcdpMIBNotificationPrefix = _CiscoWanNcdpMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 223, 2)
)
_CiscoWanNcdpMIBNotifications_ObjectIdentity = ObjectIdentity
ciscoWanNcdpMIBNotifications = _CiscoWanNcdpMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 223, 2, 0)
)
_CiscoWanNcdpMIBConformance_ObjectIdentity = ObjectIdentity
ciscoWanNcdpMIBConformance = _CiscoWanNcdpMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 223, 3)
)
_CiscoWanNcdpMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoWanNcdpMIBCompliances = _CiscoWanNcdpMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 223, 3, 1)
)
_CiscoWanNcdpMIBGroups_ObjectIdentity = ObjectIdentity
ciscoWanNcdpMIBGroups = _CiscoWanNcdpMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 223, 3, 2)
)

# Managed Objects groups

ciscoWanNcdpGlobalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 223, 3, 2, 1)
)
ciscoWanNcdpGlobalGroup.setObjects(
      *(("CISCO-WAN-NCDP-MIB", "cwnDistributionMethod"),
        ("CISCO-WAN-NCDP-MIB", "cwnNodeStratum"),
        ("CISCO-WAN-NCDP-MIB", "cwnMaxDiameter"),
        ("CISCO-WAN-NCDP-MIB", "cwnMessageInterval"),
        ("CISCO-WAN-NCDP-MIB", "cwnHoldTime"),
        ("CISCO-WAN-NCDP-MIB", "cwnChangeReason"),
        ("CISCO-WAN-NCDP-MIB", "cwnChangeTimeStamp"),
        ("CISCO-WAN-NCDP-MIB", "cwnRootClockSource"))
)
if mibBuilder.loadTexts:
    ciscoWanNcdpGlobalGroup.setStatus("current")

ciscoWanNcdpClockSourceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 223, 3, 2, 2)
)
ciscoWanNcdpClockSourceGroup.setObjects(
      *(("CISCO-WAN-NCDP-MIB", "cwnClockSourceDesc"),
        ("CISCO-WAN-NCDP-MIB", "cwnInterfaceIndex"),
        ("CISCO-WAN-NCDP-MIB", "cwnOtherClockSource"))
)
if mibBuilder.loadTexts:
    ciscoWanNcdpClockSourceGroup.setStatus("current")

ciscoWanNcdpManualGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 223, 3, 2, 3)
)
ciscoWanNcdpManualGroup.setObjects(
      *(("CISCO-WAN-NCDP-MIB", "cwnManualSourceIndex"),
        ("CISCO-WAN-NCDP-MIB", "cwnManualClockHealth"),
        ("CISCO-WAN-NCDP-MIB", "cwnManualRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoWanNcdpManualGroup.setStatus("current")

ciscoWanNcdpAtmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 223, 3, 2, 4)
)
ciscoWanNcdpAtmGroup.setObjects(
      *(("CISCO-WAN-NCDP-MIB", "cwnAtmSourceBestClockSource"),
        ("CISCO-WAN-NCDP-MIB", "cwnAtmSourcePriority"),
        ("CISCO-WAN-NCDP-MIB", "cwnAtmSourceStratum"),
        ("CISCO-WAN-NCDP-MIB", "cwnAtmSourcePRSReference"),
        ("CISCO-WAN-NCDP-MIB", "cwnAtmSourceClockHealth"),
        ("CISCO-WAN-NCDP-MIB", "cwnAtmSourceRowStatus"),
        ("CISCO-WAN-NCDP-MIB", "cwnAtmInterfaceEnable"),
        ("CISCO-WAN-NCDP-MIB", "cwnAtmInterfaceAdminWeight"),
        ("CISCO-WAN-NCDP-MIB", "cwnAtmInterfaceVpi"),
        ("CISCO-WAN-NCDP-MIB", "cwnAtmInterfaceVci"))
)
if mibBuilder.loadTexts:
    ciscoWanNcdpAtmGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoWanMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 223, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoWanMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-WAN-NCDP-MIB",
    **{"ClockStratum": ClockStratum,
       "ClockHealthStatus": ClockHealthStatus,
       "ClockSourceIndex": ClockSourceIndex,
       "ciscoWanNcdpMIB": ciscoWanNcdpMIB,
       "cwnMIBObjects": cwnMIBObjects,
       "cwnGlobal": cwnGlobal,
       "cwnDistributionMethod": cwnDistributionMethod,
       "cwnNodeStratum": cwnNodeStratum,
       "cwnMaxDiameter": cwnMaxDiameter,
       "cwnMessageInterval": cwnMessageInterval,
       "cwnHoldTime": cwnHoldTime,
       "cwnChangeReason": cwnChangeReason,
       "cwnChangeTimeStamp": cwnChangeTimeStamp,
       "cwnRootClockSource": cwnRootClockSource,
       "cwnClockSource": cwnClockSource,
       "cwnClockSourceTable": cwnClockSourceTable,
       "cwnClockSourceEntry": cwnClockSourceEntry,
       "cwnClockSourceIndex": cwnClockSourceIndex,
       "cwnClockSourceDesc": cwnClockSourceDesc,
       "cwnInterfaceIndex": cwnInterfaceIndex,
       "cwnOtherClockSource": cwnOtherClockSource,
       "cwnManualSource": cwnManualSource,
       "cwnManualSourceTable": cwnManualSourceTable,
       "cwnManualSourceEntry": cwnManualSourceEntry,
       "cwnManualSourcePriority": cwnManualSourcePriority,
       "cwnManualSourceIndex": cwnManualSourceIndex,
       "cwnManualClockHealth": cwnManualClockHealth,
       "cwnManualRowStatus": cwnManualRowStatus,
       "cwnAtmSource": cwnAtmSource,
       "cwnAtmSourceTable": cwnAtmSourceTable,
       "cwnAtmSourceEntry": cwnAtmSourceEntry,
       "cwnAtmSourceBestClockSource": cwnAtmSourceBestClockSource,
       "cwnAtmSourcePriority": cwnAtmSourcePriority,
       "cwnAtmSourceStratum": cwnAtmSourceStratum,
       "cwnAtmSourcePRSReference": cwnAtmSourcePRSReference,
       "cwnAtmSourceClockHealth": cwnAtmSourceClockHealth,
       "cwnAtmSourceRowStatus": cwnAtmSourceRowStatus,
       "cwnAtmInterface": cwnAtmInterface,
       "cwnAtmInterfaceTable": cwnAtmInterfaceTable,
       "cwnAtmInterfaceEntry": cwnAtmInterfaceEntry,
       "cwnAtmInterfaceEnable": cwnAtmInterfaceEnable,
       "cwnAtmInterfaceAdminWeight": cwnAtmInterfaceAdminWeight,
       "cwnAtmInterfaceVpi": cwnAtmInterfaceVpi,
       "cwnAtmInterfaceVci": cwnAtmInterfaceVci,
       "ciscoWanNcdpMIBNotificationPrefix": ciscoWanNcdpMIBNotificationPrefix,
       "ciscoWanNcdpMIBNotifications": ciscoWanNcdpMIBNotifications,
       "ciscoWanNcdpMIBConformance": ciscoWanNcdpMIBConformance,
       "ciscoWanNcdpMIBCompliances": ciscoWanNcdpMIBCompliances,
       "ciscoWanMIBCompliance": ciscoWanMIBCompliance,
       "ciscoWanNcdpMIBGroups": ciscoWanNcdpMIBGroups,
       "ciscoWanNcdpGlobalGroup": ciscoWanNcdpGlobalGroup,
       "ciscoWanNcdpClockSourceGroup": ciscoWanNcdpClockSourceGroup,
       "ciscoWanNcdpManualGroup": ciscoWanNcdpManualGroup,
       "ciscoWanNcdpAtmGroup": ciscoWanNcdpAtmGroup}
)
