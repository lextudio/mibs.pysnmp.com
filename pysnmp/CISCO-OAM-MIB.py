# SNMP MIB module (CISCO-OAM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-OAM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:06:20 2024
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

(OwnerString,) = mibBuilder.importSymbols(
    "RMON-MIB",
    "OwnerString")

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

ciscoOamPingMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 15)
)
ciscoOamPingMIB.setRevisions(
        ("2006-02-17 00:00",
         "2003-06-27 00:00",
         "2003-04-04 00:00",
         "1996-05-01 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CiscoOAMPingDir(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("backward", 2),
          ("forward", 1))
    )



class CiscoOAMPingStatus(Integer32, TextualConvention):
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("aborted", 4),
          ("failToStart", 7),
          ("inProgress", 5),
          ("noResponseData", 6),
          ("resourceNotAvailable", 3),
          ("success", 1),
          ("timeOut", 2))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoOamPingMIBObjects_ObjectIdentity = ObjectIdentity
ciscoOamPingMIBObjects = _CiscoOamPingMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 15, 1)
)
_OamLoopbackPingTable_Object = MibTable
oamLoopbackPingTable = _OamLoopbackPingTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 15, 1, 1)
)
if mibBuilder.loadTexts:
    oamLoopbackPingTable.setStatus("current")
_OamLoopbackPingEntry_Object = MibTableRow
oamLoopbackPingEntry = _OamLoopbackPingEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 15, 1, 1, 1)
)
oamLoopbackPingEntry.setIndexNames(
    (0, "CISCO-OAM-MIB", "oamLoopbackPingSerialNumber"),
)
if mibBuilder.loadTexts:
    oamLoopbackPingEntry.setStatus("current")


class _OamLoopbackPingSerialNumber_Type(Integer32):
    """Custom type oamLoopbackPingSerialNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OamLoopbackPingSerialNumber_Type.__name__ = "Integer32"
_OamLoopbackPingSerialNumber_Object = MibTableColumn
oamLoopbackPingSerialNumber = _OamLoopbackPingSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 15, 1, 1, 1, 1),
    _OamLoopbackPingSerialNumber_Type()
)
oamLoopbackPingSerialNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    oamLoopbackPingSerialNumber.setStatus("current")


class _OamLoopbackPingInterface_Type(Integer32):
    """Custom type oamLoopbackPingInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OamLoopbackPingInterface_Type.__name__ = "Integer32"
_OamLoopbackPingInterface_Object = MibTableColumn
oamLoopbackPingInterface = _OamLoopbackPingInterface_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 15, 1, 1, 1, 2),
    _OamLoopbackPingInterface_Type()
)
oamLoopbackPingInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oamLoopbackPingInterface.setStatus("current")


class _OamLoopbackPingVpi_Type(Integer32):
    """Custom type oamLoopbackPingVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_OamLoopbackPingVpi_Type.__name__ = "Integer32"
_OamLoopbackPingVpi_Object = MibTableColumn
oamLoopbackPingVpi = _OamLoopbackPingVpi_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 15, 1, 1, 1, 3),
    _OamLoopbackPingVpi_Type()
)
oamLoopbackPingVpi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oamLoopbackPingVpi.setStatus("current")


class _OamLoopbackPingVci_Type(Integer32):
    """Custom type oamLoopbackPingVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_OamLoopbackPingVci_Type.__name__ = "Integer32"
_OamLoopbackPingVci_Object = MibTableColumn
oamLoopbackPingVci = _OamLoopbackPingVci_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 15, 1, 1, 1, 4),
    _OamLoopbackPingVci_Type()
)
oamLoopbackPingVci.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oamLoopbackPingVci.setStatus("current")


class _OamLoopbackPingType_Type(Integer32):
    """Custom type oamLoopbackPingType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("end2end", 2),
          ("segment", 1))
    )


_OamLoopbackPingType_Type.__name__ = "Integer32"
_OamLoopbackPingType_Object = MibTableColumn
oamLoopbackPingType = _OamLoopbackPingType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 15, 1, 1, 1, 5),
    _OamLoopbackPingType_Type()
)
oamLoopbackPingType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oamLoopbackPingType.setStatus("current")


class _OamLoopbackPingLocation_Type(OctetString):
    """Custom type oamLoopbackPingLocation based on OctetString"""
    defaultHexValue = "FF"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_OamLoopbackPingLocation_Type.__name__ = "OctetString"
_OamLoopbackPingLocation_Object = MibTableColumn
oamLoopbackPingLocation = _OamLoopbackPingLocation_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 15, 1, 1, 1, 6),
    _OamLoopbackPingLocation_Type()
)
oamLoopbackPingLocation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oamLoopbackPingLocation.setStatus("current")


class _OamLoopbackPingLocationFlag_Type(Integer32):
    """Custom type oamLoopbackPingLocationFlag based on Integer32"""
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
        *(("fixed16byteValue", 3),
          ("ipAddress", 1),
          ("nsapPrefix", 2))
    )


_OamLoopbackPingLocationFlag_Type.__name__ = "Integer32"
_OamLoopbackPingLocationFlag_Object = MibTableColumn
oamLoopbackPingLocationFlag = _OamLoopbackPingLocationFlag_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 15, 1, 1, 1, 7),
    _OamLoopbackPingLocationFlag_Type()
)
oamLoopbackPingLocationFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oamLoopbackPingLocationFlag.setStatus("current")


class _OamLoopbackPingCount_Type(Integer32):
    """Custom type oamLoopbackPingCount based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_OamLoopbackPingCount_Type.__name__ = "Integer32"
_OamLoopbackPingCount_Object = MibTableColumn
oamLoopbackPingCount = _OamLoopbackPingCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 15, 1, 1, 1, 8),
    _OamLoopbackPingCount_Type()
)
oamLoopbackPingCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oamLoopbackPingCount.setStatus("current")


class _OamLoopbackPingTimeout_Type(Integer32):
    """Custom type oamLoopbackPingTimeout based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600000),
    )


_OamLoopbackPingTimeout_Type.__name__ = "Integer32"
_OamLoopbackPingTimeout_Object = MibTableColumn
oamLoopbackPingTimeout = _OamLoopbackPingTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 15, 1, 1, 1, 9),
    _OamLoopbackPingTimeout_Type()
)
oamLoopbackPingTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oamLoopbackPingTimeout.setStatus("current")
if mibBuilder.loadTexts:
    oamLoopbackPingTimeout.setUnits("milliseconds")


class _OamLoopbackPingDelay_Type(Integer32):
    """Custom type oamLoopbackPingDelay based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600000),
    )


_OamLoopbackPingDelay_Type.__name__ = "Integer32"
_OamLoopbackPingDelay_Object = MibTableColumn
oamLoopbackPingDelay = _OamLoopbackPingDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 15, 1, 1, 1, 10),
    _OamLoopbackPingDelay_Type()
)
oamLoopbackPingDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oamLoopbackPingDelay.setStatus("current")
if mibBuilder.loadTexts:
    oamLoopbackPingDelay.setUnits("milliseconds")


class _OamLoopbackPingTrapOnCompletion_Type(TruthValue):
    """Custom type oamLoopbackPingTrapOnCompletion based on TruthValue"""


_OamLoopbackPingTrapOnCompletion_Object = MibTableColumn
oamLoopbackPingTrapOnCompletion = _OamLoopbackPingTrapOnCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 15, 1, 1, 1, 11),
    _OamLoopbackPingTrapOnCompletion_Type()
)
oamLoopbackPingTrapOnCompletion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oamLoopbackPingTrapOnCompletion.setStatus("current")
_OamLoopbackPingSentCells_Type = Counter32
_OamLoopbackPingSentCells_Object = MibTableColumn
oamLoopbackPingSentCells = _OamLoopbackPingSentCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 15, 1, 1, 1, 12),
    _OamLoopbackPingSentCells_Type()
)
oamLoopbackPingSentCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oamLoopbackPingSentCells.setStatus("current")
_OamLoopbackPingReceivedCells_Type = Counter32
_OamLoopbackPingReceivedCells_Object = MibTableColumn
oamLoopbackPingReceivedCells = _OamLoopbackPingReceivedCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 15, 1, 1, 1, 13),
    _OamLoopbackPingReceivedCells_Type()
)
oamLoopbackPingReceivedCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oamLoopbackPingReceivedCells.setStatus("current")


class _OamLoopbackPingMinRtt_Type(Integer32):
    """Custom type oamLoopbackPingMinRtt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_OamLoopbackPingMinRtt_Type.__name__ = "Integer32"
_OamLoopbackPingMinRtt_Object = MibTableColumn
oamLoopbackPingMinRtt = _OamLoopbackPingMinRtt_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 15, 1, 1, 1, 14),
    _OamLoopbackPingMinRtt_Type()
)
oamLoopbackPingMinRtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oamLoopbackPingMinRtt.setStatus("current")
if mibBuilder.loadTexts:
    oamLoopbackPingMinRtt.setUnits("milliseconds")


class _OamLoopbackPingAvgRtt_Type(Integer32):
    """Custom type oamLoopbackPingAvgRtt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_OamLoopbackPingAvgRtt_Type.__name__ = "Integer32"
_OamLoopbackPingAvgRtt_Object = MibTableColumn
oamLoopbackPingAvgRtt = _OamLoopbackPingAvgRtt_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 15, 1, 1, 1, 15),
    _OamLoopbackPingAvgRtt_Type()
)
oamLoopbackPingAvgRtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oamLoopbackPingAvgRtt.setStatus("current")
if mibBuilder.loadTexts:
    oamLoopbackPingAvgRtt.setUnits("milliseconds")


class _OamLoopbackPingMaxRtt_Type(Integer32):
    """Custom type oamLoopbackPingMaxRtt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_OamLoopbackPingMaxRtt_Type.__name__ = "Integer32"
_OamLoopbackPingMaxRtt_Object = MibTableColumn
oamLoopbackPingMaxRtt = _OamLoopbackPingMaxRtt_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 15, 1, 1, 1, 16),
    _OamLoopbackPingMaxRtt_Type()
)
oamLoopbackPingMaxRtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oamLoopbackPingMaxRtt.setStatus("current")
if mibBuilder.loadTexts:
    oamLoopbackPingMaxRtt.setUnits("milliseconds")
_OamLoopbackPingCompleted_Type = TruthValue
_OamLoopbackPingCompleted_Object = MibTableColumn
oamLoopbackPingCompleted = _OamLoopbackPingCompleted_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 15, 1, 1, 1, 17),
    _OamLoopbackPingCompleted_Type()
)
oamLoopbackPingCompleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oamLoopbackPingCompleted.setStatus("current")
_OamLoopbackPingEntryOwner_Type = OwnerString
_OamLoopbackPingEntryOwner_Object = MibTableColumn
oamLoopbackPingEntryOwner = _OamLoopbackPingEntryOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 15, 1, 1, 1, 18),
    _OamLoopbackPingEntryOwner_Type()
)
oamLoopbackPingEntryOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oamLoopbackPingEntryOwner.setStatus("current")
_OamLoopbackPingEntryStatus_Type = RowStatus
_OamLoopbackPingEntryStatus_Object = MibTableColumn
oamLoopbackPingEntryStatus = _OamLoopbackPingEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 15, 1, 1, 1, 19),
    _OamLoopbackPingEntryStatus_Type()
)
oamLoopbackPingEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oamLoopbackPingEntryStatus.setStatus("current")
_OamLoopbackPingDir_Type = CiscoOAMPingDir
_OamLoopbackPingDir_Object = MibTableColumn
oamLoopbackPingDir = _OamLoopbackPingDir_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 15, 1, 1, 1, 20),
    _OamLoopbackPingDir_Type()
)
oamLoopbackPingDir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oamLoopbackPingDir.setStatus("current")
_OamLoopbackPingOperStatus_Type = CiscoOAMPingStatus
_OamLoopbackPingOperStatus_Object = MibTableColumn
oamLoopbackPingOperStatus = _OamLoopbackPingOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 15, 1, 1, 1, 21),
    _OamLoopbackPingOperStatus_Type()
)
oamLoopbackPingOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oamLoopbackPingOperStatus.setStatus("current")
_OamLoopbackPingExecTime_Type = TimeStamp
_OamLoopbackPingExecTime_Object = MibTableColumn
oamLoopbackPingExecTime = _OamLoopbackPingExecTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 15, 1, 1, 1, 22),
    _OamLoopbackPingExecTime_Type()
)
oamLoopbackPingExecTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oamLoopbackPingExecTime.setStatus("current")


class _OamLoopbackPingMinRttuSec_Type(Integer32):
    """Custom type oamLoopbackPingMinRttuSec based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_OamLoopbackPingMinRttuSec_Type.__name__ = "Integer32"
_OamLoopbackPingMinRttuSec_Object = MibTableColumn
oamLoopbackPingMinRttuSec = _OamLoopbackPingMinRttuSec_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 15, 1, 1, 1, 23),
    _OamLoopbackPingMinRttuSec_Type()
)
oamLoopbackPingMinRttuSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oamLoopbackPingMinRttuSec.setStatus("current")
if mibBuilder.loadTexts:
    oamLoopbackPingMinRttuSec.setUnits("microseconds")


class _OamLoopbackPingAvgRttuSec_Type(Integer32):
    """Custom type oamLoopbackPingAvgRttuSec based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_OamLoopbackPingAvgRttuSec_Type.__name__ = "Integer32"
_OamLoopbackPingAvgRttuSec_Object = MibTableColumn
oamLoopbackPingAvgRttuSec = _OamLoopbackPingAvgRttuSec_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 15, 1, 1, 1, 24),
    _OamLoopbackPingAvgRttuSec_Type()
)
oamLoopbackPingAvgRttuSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oamLoopbackPingAvgRttuSec.setStatus("current")
if mibBuilder.loadTexts:
    oamLoopbackPingAvgRttuSec.setUnits("microseconds")


class _OamLoopbackPingMaxRttuSec_Type(Integer32):
    """Custom type oamLoopbackPingMaxRttuSec based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_OamLoopbackPingMaxRttuSec_Type.__name__ = "Integer32"
_OamLoopbackPingMaxRttuSec_Object = MibTableColumn
oamLoopbackPingMaxRttuSec = _OamLoopbackPingMaxRttuSec_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 15, 1, 1, 1, 25),
    _OamLoopbackPingMaxRttuSec_Type()
)
oamLoopbackPingMaxRttuSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oamLoopbackPingMaxRttuSec.setStatus("current")
if mibBuilder.loadTexts:
    oamLoopbackPingMaxRttuSec.setUnits("microseconds")
_OamLoopbackSegEndPointTable_Object = MibTable
oamLoopbackSegEndPointTable = _OamLoopbackSegEndPointTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 15, 1, 2)
)
if mibBuilder.loadTexts:
    oamLoopbackSegEndPointTable.setStatus("current")
_OamLoopbackSegEndPointEntry_Object = MibTableRow
oamLoopbackSegEndPointEntry = _OamLoopbackSegEndPointEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 15, 1, 2, 1)
)
oamLoopbackSegEndPointEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-OAM-MIB", "oamLoopSegVpi"),
    (0, "CISCO-OAM-MIB", "oamLoopSegVci"),
)
if mibBuilder.loadTexts:
    oamLoopbackSegEndPointEntry.setStatus("current")


class _OamLoopSegVpi_Type(Unsigned32):
    """Custom type oamLoopSegVpi based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_OamLoopSegVpi_Type.__name__ = "Unsigned32"
_OamLoopSegVpi_Object = MibTableColumn
oamLoopSegVpi = _OamLoopSegVpi_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 15, 1, 2, 1, 1),
    _OamLoopSegVpi_Type()
)
oamLoopSegVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    oamLoopSegVpi.setStatus("current")


class _OamLoopSegVci_Type(Unsigned32):
    """Custom type oamLoopSegVci based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_OamLoopSegVci_Type.__name__ = "Unsigned32"
_OamLoopSegVci_Object = MibTableColumn
oamLoopSegVci = _OamLoopSegVci_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 15, 1, 2, 1, 2),
    _OamLoopSegVci_Type()
)
oamLoopSegVci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    oamLoopSegVci.setStatus("current")
_OamLoopSegRowStatus_Type = RowStatus
_OamLoopSegRowStatus_Object = MibTableColumn
oamLoopSegRowStatus = _OamLoopSegRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 15, 1, 2, 1, 3),
    _OamLoopSegRowStatus_Type()
)
oamLoopSegRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oamLoopSegRowStatus.setStatus("current")
_OamLoopbackPingMIBTrapPrefix_ObjectIdentity = ObjectIdentity
oamLoopbackPingMIBTrapPrefix = _OamLoopbackPingMIBTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 15, 2)
)
_OamLoopbackPingMIBTraps_ObjectIdentity = ObjectIdentity
oamLoopbackPingMIBTraps = _OamLoopbackPingMIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 15, 2, 0)
)
_CiscoOamPingMIBConformance_ObjectIdentity = ObjectIdentity
ciscoOamPingMIBConformance = _CiscoOamPingMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 15, 3)
)
_CiscoOamPingMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoOamPingMIBCompliances = _CiscoOamPingMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 15, 3, 1)
)
_CiscoOamPingMIBGroups_ObjectIdentity = ObjectIdentity
ciscoOamPingMIBGroups = _CiscoOamPingMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 15, 3, 2)
)

# Managed Objects groups

ciscoOamPingMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 15, 3, 2, 1)
)
ciscoOamPingMIBGroup.setObjects(
      *(("CISCO-OAM-MIB", "oamLoopbackPingInterface"),
        ("CISCO-OAM-MIB", "oamLoopbackPingVpi"),
        ("CISCO-OAM-MIB", "oamLoopbackPingVci"),
        ("CISCO-OAM-MIB", "oamLoopbackPingCount"),
        ("CISCO-OAM-MIB", "oamLoopbackPingType"),
        ("CISCO-OAM-MIB", "oamLoopbackPingLocation"),
        ("CISCO-OAM-MIB", "oamLoopbackPingLocationFlag"),
        ("CISCO-OAM-MIB", "oamLoopbackPingTimeout"),
        ("CISCO-OAM-MIB", "oamLoopbackPingDelay"),
        ("CISCO-OAM-MIB", "oamLoopbackPingTrapOnCompletion"),
        ("CISCO-OAM-MIB", "oamLoopbackPingSentCells"),
        ("CISCO-OAM-MIB", "oamLoopbackPingReceivedCells"),
        ("CISCO-OAM-MIB", "oamLoopbackPingMinRtt"),
        ("CISCO-OAM-MIB", "oamLoopbackPingAvgRtt"),
        ("CISCO-OAM-MIB", "oamLoopbackPingMaxRtt"),
        ("CISCO-OAM-MIB", "oamLoopbackPingCompleted"),
        ("CISCO-OAM-MIB", "oamLoopbackPingEntryOwner"),
        ("CISCO-OAM-MIB", "oamLoopbackPingEntryStatus"))
)
if mibBuilder.loadTexts:
    ciscoOamPingMIBGroup.setStatus("deprecated")

ciscoOamPing2MIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 15, 3, 2, 2)
)
ciscoOamPing2MIBGroup.setObjects(
      *(("CISCO-OAM-MIB", "oamLoopbackPingInterface"),
        ("CISCO-OAM-MIB", "oamLoopbackPingVpi"),
        ("CISCO-OAM-MIB", "oamLoopbackPingVci"),
        ("CISCO-OAM-MIB", "oamLoopbackPingCount"),
        ("CISCO-OAM-MIB", "oamLoopbackPingType"),
        ("CISCO-OAM-MIB", "oamLoopbackPingLocation"),
        ("CISCO-OAM-MIB", "oamLoopbackPingLocationFlag"),
        ("CISCO-OAM-MIB", "oamLoopbackPingTimeout"),
        ("CISCO-OAM-MIB", "oamLoopbackPingDelay"),
        ("CISCO-OAM-MIB", "oamLoopbackPingTrapOnCompletion"),
        ("CISCO-OAM-MIB", "oamLoopbackPingSentCells"),
        ("CISCO-OAM-MIB", "oamLoopbackPingReceivedCells"),
        ("CISCO-OAM-MIB", "oamLoopbackPingMinRtt"),
        ("CISCO-OAM-MIB", "oamLoopbackPingAvgRtt"),
        ("CISCO-OAM-MIB", "oamLoopbackPingMaxRtt"),
        ("CISCO-OAM-MIB", "oamLoopbackPingCompleted"),
        ("CISCO-OAM-MIB", "oamLoopbackPingEntryOwner"),
        ("CISCO-OAM-MIB", "oamLoopbackPingEntryStatus"),
        ("CISCO-OAM-MIB", "oamLoopbackPingDir"),
        ("CISCO-OAM-MIB", "oamLoopbackPingOperStatus"),
        ("CISCO-OAM-MIB", "oamLoopbackPingExecTime"))
)
if mibBuilder.loadTexts:
    ciscoOamPing2MIBGroup.setStatus("deprecated")

ciscoOamPingSegEndPointGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 15, 3, 2, 3)
)
ciscoOamPingSegEndPointGroup.setObjects(
    ("CISCO-OAM-MIB", "oamLoopSegRowStatus")
)
if mibBuilder.loadTexts:
    ciscoOamPingSegEndPointGroup.setStatus("current")

ciscoOamPingMIBGroupRev3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 15, 3, 2, 5)
)
ciscoOamPingMIBGroupRev3.setObjects(
      *(("CISCO-OAM-MIB", "oamLoopbackPingInterface"),
        ("CISCO-OAM-MIB", "oamLoopbackPingVpi"),
        ("CISCO-OAM-MIB", "oamLoopbackPingVci"),
        ("CISCO-OAM-MIB", "oamLoopbackPingCount"),
        ("CISCO-OAM-MIB", "oamLoopbackPingType"),
        ("CISCO-OAM-MIB", "oamLoopbackPingLocation"),
        ("CISCO-OAM-MIB", "oamLoopbackPingLocationFlag"),
        ("CISCO-OAM-MIB", "oamLoopbackPingTimeout"),
        ("CISCO-OAM-MIB", "oamLoopbackPingDelay"),
        ("CISCO-OAM-MIB", "oamLoopbackPingTrapOnCompletion"),
        ("CISCO-OAM-MIB", "oamLoopbackPingSentCells"),
        ("CISCO-OAM-MIB", "oamLoopbackPingReceivedCells"),
        ("CISCO-OAM-MIB", "oamLoopbackPingMinRtt"),
        ("CISCO-OAM-MIB", "oamLoopbackPingAvgRtt"),
        ("CISCO-OAM-MIB", "oamLoopbackPingMaxRtt"),
        ("CISCO-OAM-MIB", "oamLoopbackPingCompleted"),
        ("CISCO-OAM-MIB", "oamLoopbackPingEntryOwner"),
        ("CISCO-OAM-MIB", "oamLoopbackPingEntryStatus"),
        ("CISCO-OAM-MIB", "oamLoopbackPingDir"),
        ("CISCO-OAM-MIB", "oamLoopbackPingOperStatus"),
        ("CISCO-OAM-MIB", "oamLoopbackPingExecTime"),
        ("CISCO-OAM-MIB", "oamLoopbackPingAvgRttuSec"),
        ("CISCO-OAM-MIB", "oamLoopbackPingMinRttuSec"),
        ("CISCO-OAM-MIB", "oamLoopbackPingMaxRttuSec"))
)
if mibBuilder.loadTexts:
    ciscoOamPingMIBGroupRev3.setStatus("current")


# Notification objects

oamLoopbackPingCompletionTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 15, 2, 0, 1)
)
oamLoopbackPingCompletionTrap.setObjects(
    ("CISCO-OAM-MIB", "oamLoopbackPingCompleted")
)
if mibBuilder.loadTexts:
    oamLoopbackPingCompletionTrap.setStatus(
        "current"
    )


# Notifications groups

oamLoopbackNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 15, 3, 2, 4)
)
oamLoopbackNotificationsGroup.setObjects(
    ("CISCO-OAM-MIB", "oamLoopbackPingCompletionTrap")
)
if mibBuilder.loadTexts:
    oamLoopbackNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoOamPingMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 15, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoOamPingMIBCompliance.setStatus(
        "deprecated"
    )

ciscoOamPingMIBCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 15, 3, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoOamPingMIBCompliance2.setStatus(
        "deprecated"
    )

ciscoOamPingMIBCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 15, 3, 1, 3)
)
if mibBuilder.loadTexts:
    ciscoOamPingMIBCompliance3.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-OAM-MIB",
    **{"CiscoOAMPingDir": CiscoOAMPingDir,
       "CiscoOAMPingStatus": CiscoOAMPingStatus,
       "ciscoOamPingMIB": ciscoOamPingMIB,
       "ciscoOamPingMIBObjects": ciscoOamPingMIBObjects,
       "oamLoopbackPingTable": oamLoopbackPingTable,
       "oamLoopbackPingEntry": oamLoopbackPingEntry,
       "oamLoopbackPingSerialNumber": oamLoopbackPingSerialNumber,
       "oamLoopbackPingInterface": oamLoopbackPingInterface,
       "oamLoopbackPingVpi": oamLoopbackPingVpi,
       "oamLoopbackPingVci": oamLoopbackPingVci,
       "oamLoopbackPingType": oamLoopbackPingType,
       "oamLoopbackPingLocation": oamLoopbackPingLocation,
       "oamLoopbackPingLocationFlag": oamLoopbackPingLocationFlag,
       "oamLoopbackPingCount": oamLoopbackPingCount,
       "oamLoopbackPingTimeout": oamLoopbackPingTimeout,
       "oamLoopbackPingDelay": oamLoopbackPingDelay,
       "oamLoopbackPingTrapOnCompletion": oamLoopbackPingTrapOnCompletion,
       "oamLoopbackPingSentCells": oamLoopbackPingSentCells,
       "oamLoopbackPingReceivedCells": oamLoopbackPingReceivedCells,
       "oamLoopbackPingMinRtt": oamLoopbackPingMinRtt,
       "oamLoopbackPingAvgRtt": oamLoopbackPingAvgRtt,
       "oamLoopbackPingMaxRtt": oamLoopbackPingMaxRtt,
       "oamLoopbackPingCompleted": oamLoopbackPingCompleted,
       "oamLoopbackPingEntryOwner": oamLoopbackPingEntryOwner,
       "oamLoopbackPingEntryStatus": oamLoopbackPingEntryStatus,
       "oamLoopbackPingDir": oamLoopbackPingDir,
       "oamLoopbackPingOperStatus": oamLoopbackPingOperStatus,
       "oamLoopbackPingExecTime": oamLoopbackPingExecTime,
       "oamLoopbackPingMinRttuSec": oamLoopbackPingMinRttuSec,
       "oamLoopbackPingAvgRttuSec": oamLoopbackPingAvgRttuSec,
       "oamLoopbackPingMaxRttuSec": oamLoopbackPingMaxRttuSec,
       "oamLoopbackSegEndPointTable": oamLoopbackSegEndPointTable,
       "oamLoopbackSegEndPointEntry": oamLoopbackSegEndPointEntry,
       "oamLoopSegVpi": oamLoopSegVpi,
       "oamLoopSegVci": oamLoopSegVci,
       "oamLoopSegRowStatus": oamLoopSegRowStatus,
       "oamLoopbackPingMIBTrapPrefix": oamLoopbackPingMIBTrapPrefix,
       "oamLoopbackPingMIBTraps": oamLoopbackPingMIBTraps,
       "oamLoopbackPingCompletionTrap": oamLoopbackPingCompletionTrap,
       "ciscoOamPingMIBConformance": ciscoOamPingMIBConformance,
       "ciscoOamPingMIBCompliances": ciscoOamPingMIBCompliances,
       "ciscoOamPingMIBCompliance": ciscoOamPingMIBCompliance,
       "ciscoOamPingMIBCompliance2": ciscoOamPingMIBCompliance2,
       "ciscoOamPingMIBCompliance3": ciscoOamPingMIBCompliance3,
       "ciscoOamPingMIBGroups": ciscoOamPingMIBGroups,
       "ciscoOamPingMIBGroup": ciscoOamPingMIBGroup,
       "ciscoOamPing2MIBGroup": ciscoOamPing2MIBGroup,
       "ciscoOamPingSegEndPointGroup": ciscoOamPingSegEndPointGroup,
       "oamLoopbackNotificationsGroup": oamLoopbackNotificationsGroup,
       "ciscoOamPingMIBGroupRev3": ciscoOamPingMIBGroupRev3}
)
