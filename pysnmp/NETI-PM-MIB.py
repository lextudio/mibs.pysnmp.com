# SNMP MIB module (NETI-PM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NETI-PM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:26:35 2024
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

(netiExperimentalGeneric,) = mibBuilder.importSymbols(
    "NETI-COMMON-MIB",
    "netiExperimentalGeneric")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

netiPMMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17)
)
netiPMMIB.setRevisions(
        ("2008-12-12 12:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class Counter15m(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 910),
    )



class Counter24h(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86410),
    )



# MIB Managed Objects in the order of their OIDs

_NetiPMMIBObjects_ObjectIdentity = ObjectIdentity
netiPMMIBObjects = _NetiPMMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1)
)
_PmTifGroup_ObjectIdentity = ObjectIdentity
pmTifGroup = _PmTifGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 1)
)
_PmTifTable_Object = MibTable
pmTifTable = _PmTifTable_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 1, 1)
)
if mibBuilder.loadTexts:
    pmTifTable.setStatus("current")
_PmTifEntry_Object = MibTableRow
pmTifEntry = _PmTifEntry_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 1, 1, 1)
)
pmTifEntry.setIndexNames(
    (0, "NETI-PM-MIB", "pmTifIndex"),
)
if mibBuilder.loadTexts:
    pmTifEntry.setStatus("current")
_PmTifIndex_Type = Unsigned32
_PmTifIndex_Object = MibTableColumn
pmTifIndex = _PmTifIndex_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 1, 1, 1, 1),
    _PmTifIndex_Type()
)
pmTifIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pmTifIndex.setStatus("current")


class _PmTifAdminStatus_Type(Integer32):
    """Custom type pmTifAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_PmTifAdminStatus_Type.__name__ = "Integer32"
_PmTifAdminStatus_Object = MibTableColumn
pmTifAdminStatus = _PmTifAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 1, 1, 1, 2),
    _PmTifAdminStatus_Type()
)
pmTifAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmTifAdminStatus.setStatus("current")


class _PmTifOperStatus_Type(Integer32):
    """Custom type pmTifOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_PmTifOperStatus_Type.__name__ = "Integer32"
_PmTifOperStatus_Object = MibTableColumn
pmTifOperStatus = _PmTifOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 1, 1, 1, 3),
    _PmTifOperStatus_Type()
)
pmTifOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmTifOperStatus.setStatus("current")
_PmTifFailure_Type = DisplayString
_PmTifFailure_Object = MibTableColumn
pmTifFailure = _PmTifFailure_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 1, 1, 1, 4),
    _PmTifFailure_Type()
)
pmTifFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmTifFailure.setStatus("current")
_PmTifDataSource_Type = ObjectIdentifier
_PmTifDataSource_Object = MibTableColumn
pmTifDataSource = _PmTifDataSource_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 1, 1, 1, 5),
    _PmTifDataSource_Type()
)
pmTifDataSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmTifDataSource.setStatus("current")
_PmTifDataSourceName_Type = DisplayString
_PmTifDataSourceName_Object = MibTableColumn
pmTifDataSourceName = _PmTifDataSourceName_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 1, 1, 1, 6),
    _PmTifDataSourceName_Type()
)
pmTifDataSourceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmTifDataSourceName.setStatus("current")
_PmTifUatAlarmsEnabled_Type = TruthValue
_PmTifUatAlarmsEnabled_Object = MibTableColumn
pmTifUatAlarmsEnabled = _PmTifUatAlarmsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 1, 1, 1, 7),
    _PmTifUatAlarmsEnabled_Type()
)
pmTifUatAlarmsEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmTifUatAlarmsEnabled.setStatus("current")
_PmTifTresholdAlarmsEnabled_Type = TruthValue
_PmTifTresholdAlarmsEnabled_Object = MibTableColumn
pmTifTresholdAlarmsEnabled = _PmTifTresholdAlarmsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 1, 1, 1, 8),
    _PmTifTresholdAlarmsEnabled_Type()
)
pmTifTresholdAlarmsEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmTifTresholdAlarmsEnabled.setStatus("current")
_PmTifPeriodicEventsEnabled_Type = TruthValue
_PmTifPeriodicEventsEnabled_Object = MibTableColumn
pmTifPeriodicEventsEnabled = _PmTifPeriodicEventsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 1, 1, 1, 9),
    _PmTifPeriodicEventsEnabled_Type()
)
pmTifPeriodicEventsEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmTifPeriodicEventsEnabled.setStatus("current")
_PmTifZeroSuppressionEnabled_Type = TruthValue
_PmTifZeroSuppressionEnabled_Object = MibTableColumn
pmTifZeroSuppressionEnabled = _PmTifZeroSuppressionEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 1, 1, 1, 10),
    _PmTifZeroSuppressionEnabled_Type()
)
pmTifZeroSuppressionEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmTifZeroSuppressionEnabled.setStatus("current")


class _PmTifHistorySize_Type(Integer32):
    """Custom type pmTifHistorySize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("large", 3),
          ("none", 1),
          ("small", 2))
    )


_PmTifHistorySize_Type.__name__ = "Integer32"
_PmTifHistorySize_Object = MibTableColumn
pmTifHistorySize = _PmTifHistorySize_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 1, 1, 1, 11),
    _PmTifHistorySize_Type()
)
pmTifHistorySize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmTifHistorySize.setStatus("current")
_PmTif15mTresholdES_Type = Counter15m
_PmTif15mTresholdES_Object = MibTableColumn
pmTif15mTresholdES = _PmTif15mTresholdES_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 1, 1, 1, 12),
    _PmTif15mTresholdES_Type()
)
pmTif15mTresholdES.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmTif15mTresholdES.setStatus("current")
_PmTif15mTresholdSES_Type = Counter15m
_PmTif15mTresholdSES_Object = MibTableColumn
pmTif15mTresholdSES = _PmTif15mTresholdSES_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 1, 1, 1, 13),
    _PmTif15mTresholdSES_Type()
)
pmTif15mTresholdSES.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmTif15mTresholdSES.setStatus("current")
_PmTif15mTresholdBBE_Type = Gauge32
_PmTif15mTresholdBBE_Object = MibTableColumn
pmTif15mTresholdBBE = _PmTif15mTresholdBBE_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 1, 1, 1, 14),
    _PmTif15mTresholdBBE_Type()
)
pmTif15mTresholdBBE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmTif15mTresholdBBE.setStatus("current")
_PmTif15mTresholdSS_Type = Counter15m
_PmTif15mTresholdSS_Object = MibTableColumn
pmTif15mTresholdSS = _PmTif15mTresholdSS_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 1, 1, 1, 15),
    _PmTif15mTresholdSS_Type()
)
pmTif15mTresholdSS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmTif15mTresholdSS.setStatus("current")
_PmTif24hTresholdES_Type = Counter24h
_PmTif24hTresholdES_Object = MibTableColumn
pmTif24hTresholdES = _PmTif24hTresholdES_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 1, 1, 1, 16),
    _PmTif24hTresholdES_Type()
)
pmTif24hTresholdES.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmTif24hTresholdES.setStatus("current")
_PmTif24hTresholdSES_Type = Counter24h
_PmTif24hTresholdSES_Object = MibTableColumn
pmTif24hTresholdSES = _PmTif24hTresholdSES_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 1, 1, 1, 17),
    _PmTif24hTresholdSES_Type()
)
pmTif24hTresholdSES.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmTif24hTresholdSES.setStatus("current")
_PmTif24hTresholdBBE_Type = Gauge32
_PmTif24hTresholdBBE_Object = MibTableColumn
pmTif24hTresholdBBE = _PmTif24hTresholdBBE_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 1, 1, 1, 18),
    _PmTif24hTresholdBBE_Type()
)
pmTif24hTresholdBBE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmTif24hTresholdBBE.setStatus("current")
_PmTif24hTresholdSS_Type = Counter24h
_PmTif24hTresholdSS_Object = MibTableColumn
pmTif24hTresholdSS = _PmTif24hTresholdSS_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 1, 1, 1, 19),
    _PmTif24hTresholdSS_Type()
)
pmTif24hTresholdSS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmTif24hTresholdSS.setStatus("current")
_PmTifCurrentTable_Object = MibTable
pmTifCurrentTable = _PmTifCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 1, 2)
)
if mibBuilder.loadTexts:
    pmTifCurrentTable.setStatus("current")
_PmTifCurrentEntry_Object = MibTableRow
pmTifCurrentEntry = _PmTifCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 1, 2, 1)
)
pmTifCurrentEntry.setIndexNames(
    (0, "NETI-PM-MIB", "pmTifIndex"),
)
if mibBuilder.loadTexts:
    pmTifCurrentEntry.setStatus("current")
_PmTifCurrentTime_Type = Counter15m
_PmTifCurrentTime_Object = MibTableColumn
pmTifCurrentTime = _PmTifCurrentTime_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 1, 2, 1, 2),
    _PmTifCurrentTime_Type()
)
pmTifCurrentTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmTifCurrentTime.setStatus("current")
_PmTifCurrentSuspect_Type = TruthValue
_PmTifCurrentSuspect_Object = MibTableColumn
pmTifCurrentSuspect = _PmTifCurrentSuspect_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 1, 2, 1, 3),
    _PmTifCurrentSuspect_Type()
)
pmTifCurrentSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmTifCurrentSuspect.setStatus("current")
_PmTifCurrentZS_Type = Counter32
_PmTifCurrentZS_Object = MibTableColumn
pmTifCurrentZS = _PmTifCurrentZS_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 1, 2, 1, 4),
    _PmTifCurrentZS_Type()
)
pmTifCurrentZS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmTifCurrentZS.setStatus("current")
_PmTifCurrentESs_Type = Counter15m
_PmTifCurrentESs_Object = MibTableColumn
pmTifCurrentESs = _PmTifCurrentESs_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 1, 2, 1, 5),
    _PmTifCurrentESs_Type()
)
pmTifCurrentESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmTifCurrentESs.setStatus("current")
_PmTifCurrentSESs_Type = Counter15m
_PmTifCurrentSESs_Object = MibTableColumn
pmTifCurrentSESs = _PmTifCurrentSESs_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 1, 2, 1, 6),
    _PmTifCurrentSESs_Type()
)
pmTifCurrentSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmTifCurrentSESs.setStatus("current")
_PmTifCurrentBBEs_Type = Gauge32
_PmTifCurrentBBEs_Object = MibTableColumn
pmTifCurrentBBEs = _PmTifCurrentBBEs_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 1, 2, 1, 7),
    _PmTifCurrentBBEs_Type()
)
pmTifCurrentBBEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmTifCurrentBBEs.setStatus("current")
_PmTifCurrentUASs_Type = Counter15m
_PmTifCurrentUASs_Object = MibTableColumn
pmTifCurrentUASs = _PmTifCurrentUASs_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 1, 2, 1, 8),
    _PmTifCurrentUASs_Type()
)
pmTifCurrentUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmTifCurrentUASs.setStatus("current")
_PmTifCurrentSSs_Type = Counter15m
_PmTifCurrentSSs_Object = MibTableColumn
pmTifCurrentSSs = _PmTifCurrentSSs_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 1, 2, 1, 9),
    _PmTifCurrentSSs_Type()
)
pmTifCurrentSSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmTifCurrentSSs.setStatus("current")
_PmTif15mTable_Object = MibTable
pmTif15mTable = _PmTif15mTable_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 1, 3)
)
if mibBuilder.loadTexts:
    pmTif15mTable.setStatus("current")
_PmTif15mEntry_Object = MibTableRow
pmTif15mEntry = _PmTif15mEntry_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 1, 3, 1)
)
pmTif15mEntry.setIndexNames(
    (0, "NETI-PM-MIB", "pmTifIndex"),
    (0, "NETI-PM-MIB", "pmTif15mIndex"),
)
if mibBuilder.loadTexts:
    pmTif15mEntry.setStatus("current")
_PmTif15mIndex_Type = Unsigned32
_PmTif15mIndex_Object = MibTableColumn
pmTif15mIndex = _PmTif15mIndex_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 1, 3, 1, 1),
    _PmTif15mIndex_Type()
)
pmTif15mIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pmTif15mIndex.setStatus("current")
_PmTif15mTime_Type = DateAndTime
_PmTif15mTime_Object = MibTableColumn
pmTif15mTime = _PmTif15mTime_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 1, 3, 1, 2),
    _PmTif15mTime_Type()
)
pmTif15mTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmTif15mTime.setStatus("current")
_PmTif15mSuspect_Type = TruthValue
_PmTif15mSuspect_Object = MibTableColumn
pmTif15mSuspect = _PmTif15mSuspect_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 1, 3, 1, 3),
    _PmTif15mSuspect_Type()
)
pmTif15mSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmTif15mSuspect.setStatus("current")
_PmTif15mZS_Type = Counter32
_PmTif15mZS_Object = MibTableColumn
pmTif15mZS = _PmTif15mZS_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 1, 3, 1, 4),
    _PmTif15mZS_Type()
)
pmTif15mZS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmTif15mZS.setStatus("current")
_PmTif15mESs_Type = Counter15m
_PmTif15mESs_Object = MibTableColumn
pmTif15mESs = _PmTif15mESs_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 1, 3, 1, 5),
    _PmTif15mESs_Type()
)
pmTif15mESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmTif15mESs.setStatus("current")
_PmTif15mSESs_Type = Counter15m
_PmTif15mSESs_Object = MibTableColumn
pmTif15mSESs = _PmTif15mSESs_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 1, 3, 1, 6),
    _PmTif15mSESs_Type()
)
pmTif15mSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmTif15mSESs.setStatus("current")
_PmTif15mBBEs_Type = Gauge32
_PmTif15mBBEs_Object = MibTableColumn
pmTif15mBBEs = _PmTif15mBBEs_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 1, 3, 1, 7),
    _PmTif15mBBEs_Type()
)
pmTif15mBBEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmTif15mBBEs.setStatus("current")
_PmTif15mUASs_Type = Counter15m
_PmTif15mUASs_Object = MibTableColumn
pmTif15mUASs = _PmTif15mUASs_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 1, 3, 1, 8),
    _PmTif15mUASs_Type()
)
pmTif15mUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmTif15mUASs.setStatus("current")
_PmTif15mSSs_Type = Counter15m
_PmTif15mSSs_Object = MibTableColumn
pmTif15mSSs = _PmTif15mSSs_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 1, 3, 1, 9),
    _PmTif15mSSs_Type()
)
pmTif15mSSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmTif15mSSs.setStatus("current")
_PmTif24hTable_Object = MibTable
pmTif24hTable = _PmTif24hTable_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 1, 4)
)
if mibBuilder.loadTexts:
    pmTif24hTable.setStatus("current")
_PmTif24hEntry_Object = MibTableRow
pmTif24hEntry = _PmTif24hEntry_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 1, 4, 1)
)
pmTif24hEntry.setIndexNames(
    (0, "NETI-PM-MIB", "pmTifIndex"),
    (0, "NETI-PM-MIB", "pmTif24hIndex"),
)
if mibBuilder.loadTexts:
    pmTif24hEntry.setStatus("current")
_PmTif24hIndex_Type = Unsigned32
_PmTif24hIndex_Object = MibTableColumn
pmTif24hIndex = _PmTif24hIndex_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 1, 4, 1, 1),
    _PmTif24hIndex_Type()
)
pmTif24hIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pmTif24hIndex.setStatus("current")
_PmTif24hTime_Type = DateAndTime
_PmTif24hTime_Object = MibTableColumn
pmTif24hTime = _PmTif24hTime_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 1, 4, 1, 2),
    _PmTif24hTime_Type()
)
pmTif24hTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmTif24hTime.setStatus("current")
_PmTif24hSuspect_Type = TruthValue
_PmTif24hSuspect_Object = MibTableColumn
pmTif24hSuspect = _PmTif24hSuspect_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 1, 4, 1, 3),
    _PmTif24hSuspect_Type()
)
pmTif24hSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmTif24hSuspect.setStatus("current")
_PmTif24hZS_Type = Counter32
_PmTif24hZS_Object = MibTableColumn
pmTif24hZS = _PmTif24hZS_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 1, 4, 1, 4),
    _PmTif24hZS_Type()
)
pmTif24hZS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmTif24hZS.setStatus("current")
_PmTif24hESs_Type = Counter24h
_PmTif24hESs_Object = MibTableColumn
pmTif24hESs = _PmTif24hESs_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 1, 4, 1, 5),
    _PmTif24hESs_Type()
)
pmTif24hESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmTif24hESs.setStatus("current")
_PmTif24hSESs_Type = Counter24h
_PmTif24hSESs_Object = MibTableColumn
pmTif24hSESs = _PmTif24hSESs_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 1, 4, 1, 6),
    _PmTif24hSESs_Type()
)
pmTif24hSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmTif24hSESs.setStatus("current")
_PmTif24hBBEs_Type = Gauge32
_PmTif24hBBEs_Object = MibTableColumn
pmTif24hBBEs = _PmTif24hBBEs_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 1, 4, 1, 7),
    _PmTif24hBBEs_Type()
)
pmTif24hBBEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmTif24hBBEs.setStatus("current")
_PmTif24hUASs_Type = Counter24h
_PmTif24hUASs_Object = MibTableColumn
pmTif24hUASs = _PmTif24hUASs_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 1, 4, 1, 8),
    _PmTif24hUASs_Type()
)
pmTif24hUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmTif24hUASs.setStatus("current")
_PmTif24hSSs_Type = Counter24h
_PmTif24hSSs_Object = MibTableColumn
pmTif24hSSs = _PmTif24hSSs_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 1, 4, 1, 9),
    _PmTif24hSSs_Type()
)
pmTif24hSSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmTif24hSSs.setStatus("current")
_PmTif24hCurrentTable_Object = MibTable
pmTif24hCurrentTable = _PmTif24hCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 1, 5)
)
if mibBuilder.loadTexts:
    pmTif24hCurrentTable.setStatus("current")
_PmTif24hCurrentEntry_Object = MibTableRow
pmTif24hCurrentEntry = _PmTif24hCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 1, 5, 1)
)
pmTif24hCurrentEntry.setIndexNames(
    (0, "NETI-PM-MIB", "pmTifIndex"),
)
if mibBuilder.loadTexts:
    pmTif24hCurrentEntry.setStatus("current")
_PmTif24hCurrentTime_Type = Counter15m
_PmTif24hCurrentTime_Object = MibTableColumn
pmTif24hCurrentTime = _PmTif24hCurrentTime_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 1, 5, 1, 2),
    _PmTif24hCurrentTime_Type()
)
pmTif24hCurrentTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmTif24hCurrentTime.setStatus("current")
_PmTif24hCurrentSuspect_Type = TruthValue
_PmTif24hCurrentSuspect_Object = MibTableColumn
pmTif24hCurrentSuspect = _PmTif24hCurrentSuspect_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 1, 5, 1, 3),
    _PmTif24hCurrentSuspect_Type()
)
pmTif24hCurrentSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmTif24hCurrentSuspect.setStatus("current")
_PmTif24hCurrentZS_Type = Counter32
_PmTif24hCurrentZS_Object = MibTableColumn
pmTif24hCurrentZS = _PmTif24hCurrentZS_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 1, 5, 1, 4),
    _PmTif24hCurrentZS_Type()
)
pmTif24hCurrentZS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmTif24hCurrentZS.setStatus("current")
_PmTif24hCurrentESs_Type = Counter15m
_PmTif24hCurrentESs_Object = MibTableColumn
pmTif24hCurrentESs = _PmTif24hCurrentESs_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 1, 5, 1, 5),
    _PmTif24hCurrentESs_Type()
)
pmTif24hCurrentESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmTif24hCurrentESs.setStatus("current")
_PmTif24hCurrentSESs_Type = Counter15m
_PmTif24hCurrentSESs_Object = MibTableColumn
pmTif24hCurrentSESs = _PmTif24hCurrentSESs_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 1, 5, 1, 6),
    _PmTif24hCurrentSESs_Type()
)
pmTif24hCurrentSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmTif24hCurrentSESs.setStatus("current")
_PmTif24hCurrentBBEs_Type = Gauge32
_PmTif24hCurrentBBEs_Object = MibTableColumn
pmTif24hCurrentBBEs = _PmTif24hCurrentBBEs_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 1, 5, 1, 7),
    _PmTif24hCurrentBBEs_Type()
)
pmTif24hCurrentBBEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmTif24hCurrentBBEs.setStatus("current")
_PmTif24hCurrentUASs_Type = Counter15m
_PmTif24hCurrentUASs_Object = MibTableColumn
pmTif24hCurrentUASs = _PmTif24hCurrentUASs_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 1, 5, 1, 8),
    _PmTif24hCurrentUASs_Type()
)
pmTif24hCurrentUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmTif24hCurrentUASs.setStatus("current")
_PmTif24hCurrentSSs_Type = Counter15m
_PmTif24hCurrentSSs_Object = MibTableColumn
pmTif24hCurrentSSs = _PmTif24hCurrentSSs_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 1, 5, 1, 9),
    _PmTif24hCurrentSSs_Type()
)
pmTif24hCurrentSSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmTif24hCurrentSSs.setStatus("current")
_PmAifGroup_ObjectIdentity = ObjectIdentity
pmAifGroup = _PmAifGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 2)
)
_PmAifTable_Object = MibTable
pmAifTable = _PmAifTable_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 2, 1)
)
if mibBuilder.loadTexts:
    pmAifTable.setStatus("current")
_PmAifEntry_Object = MibTableRow
pmAifEntry = _PmAifEntry_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 2, 1, 1)
)
pmAifEntry.setIndexNames(
    (0, "NETI-PM-MIB", "pmAifIndex"),
)
if mibBuilder.loadTexts:
    pmAifEntry.setStatus("current")
_PmAifIndex_Type = Unsigned32
_PmAifIndex_Object = MibTableColumn
pmAifIndex = _PmAifIndex_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 2, 1, 1, 1),
    _PmAifIndex_Type()
)
pmAifIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pmAifIndex.setStatus("current")


class _PmAifAdminStatus_Type(Integer32):
    """Custom type pmAifAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_PmAifAdminStatus_Type.__name__ = "Integer32"
_PmAifAdminStatus_Object = MibTableColumn
pmAifAdminStatus = _PmAifAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 2, 1, 1, 2),
    _PmAifAdminStatus_Type()
)
pmAifAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmAifAdminStatus.setStatus("current")


class _PmAifOperStatus_Type(Integer32):
    """Custom type pmAifOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_PmAifOperStatus_Type.__name__ = "Integer32"
_PmAifOperStatus_Object = MibTableColumn
pmAifOperStatus = _PmAifOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 2, 1, 1, 3),
    _PmAifOperStatus_Type()
)
pmAifOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmAifOperStatus.setStatus("current")
_PmAifFailure_Type = DisplayString
_PmAifFailure_Object = MibTableColumn
pmAifFailure = _PmAifFailure_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 2, 1, 1, 4),
    _PmAifFailure_Type()
)
pmAifFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmAifFailure.setStatus("current")
_PmAifDataSource_Type = ObjectIdentifier
_PmAifDataSource_Object = MibTableColumn
pmAifDataSource = _PmAifDataSource_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 2, 1, 1, 5),
    _PmAifDataSource_Type()
)
pmAifDataSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmAifDataSource.setStatus("current")
_PmAifDataSourceName_Type = DisplayString
_PmAifDataSourceName_Object = MibTableColumn
pmAifDataSourceName = _PmAifDataSourceName_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 2, 1, 1, 6),
    _PmAifDataSourceName_Type()
)
pmAifDataSourceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmAifDataSourceName.setStatus("current")
_PmAifUatAlarmsEnabled_Type = TruthValue
_PmAifUatAlarmsEnabled_Object = MibTableColumn
pmAifUatAlarmsEnabled = _PmAifUatAlarmsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 2, 1, 1, 7),
    _PmAifUatAlarmsEnabled_Type()
)
pmAifUatAlarmsEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmAifUatAlarmsEnabled.setStatus("current")
_PmAifTresholdAlarmsEnabled_Type = TruthValue
_PmAifTresholdAlarmsEnabled_Object = MibTableColumn
pmAifTresholdAlarmsEnabled = _PmAifTresholdAlarmsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 2, 1, 1, 8),
    _PmAifTresholdAlarmsEnabled_Type()
)
pmAifTresholdAlarmsEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmAifTresholdAlarmsEnabled.setStatus("current")
_PmAifPeriodicEventsEnabled_Type = TruthValue
_PmAifPeriodicEventsEnabled_Object = MibTableColumn
pmAifPeriodicEventsEnabled = _PmAifPeriodicEventsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 2, 1, 1, 9),
    _PmAifPeriodicEventsEnabled_Type()
)
pmAifPeriodicEventsEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmAifPeriodicEventsEnabled.setStatus("current")
_PmAifZeroSuppressionEnabled_Type = TruthValue
_PmAifZeroSuppressionEnabled_Object = MibTableColumn
pmAifZeroSuppressionEnabled = _PmAifZeroSuppressionEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 2, 1, 1, 10),
    _PmAifZeroSuppressionEnabled_Type()
)
pmAifZeroSuppressionEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmAifZeroSuppressionEnabled.setStatus("current")


class _PmAifHistorySize_Type(Integer32):
    """Custom type pmAifHistorySize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("large", 3),
          ("none", 1),
          ("small", 2))
    )


_PmAifHistorySize_Type.__name__ = "Integer32"
_PmAifHistorySize_Object = MibTableColumn
pmAifHistorySize = _PmAifHistorySize_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 2, 1, 1, 11),
    _PmAifHistorySize_Type()
)
pmAifHistorySize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmAifHistorySize.setStatus("current")
_PmAif15mTresholdES_Type = Counter15m
_PmAif15mTresholdES_Object = MibTableColumn
pmAif15mTresholdES = _PmAif15mTresholdES_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 2, 1, 1, 12),
    _PmAif15mTresholdES_Type()
)
pmAif15mTresholdES.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmAif15mTresholdES.setStatus("current")
_PmAif15mTresholdSES_Type = Counter15m
_PmAif15mTresholdSES_Object = MibTableColumn
pmAif15mTresholdSES = _PmAif15mTresholdSES_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 2, 1, 1, 13),
    _PmAif15mTresholdSES_Type()
)
pmAif15mTresholdSES.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmAif15mTresholdSES.setStatus("current")
_PmAif15mTresholdBBE_Type = Gauge32
_PmAif15mTresholdBBE_Object = MibTableColumn
pmAif15mTresholdBBE = _PmAif15mTresholdBBE_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 2, 1, 1, 14),
    _PmAif15mTresholdBBE_Type()
)
pmAif15mTresholdBBE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmAif15mTresholdBBE.setStatus("current")
_PmAif24hTresholdES_Type = Counter24h
_PmAif24hTresholdES_Object = MibTableColumn
pmAif24hTresholdES = _PmAif24hTresholdES_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 2, 1, 1, 15),
    _PmAif24hTresholdES_Type()
)
pmAif24hTresholdES.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmAif24hTresholdES.setStatus("current")
_PmAif24hTresholdSES_Type = Counter24h
_PmAif24hTresholdSES_Object = MibTableColumn
pmAif24hTresholdSES = _PmAif24hTresholdSES_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 2, 1, 1, 16),
    _PmAif24hTresholdSES_Type()
)
pmAif24hTresholdSES.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmAif24hTresholdSES.setStatus("current")
_PmAif24hTresholdBBE_Type = Gauge32
_PmAif24hTresholdBBE_Object = MibTableColumn
pmAif24hTresholdBBE = _PmAif24hTresholdBBE_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 2, 1, 1, 17),
    _PmAif24hTresholdBBE_Type()
)
pmAif24hTresholdBBE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmAif24hTresholdBBE.setStatus("current")
_PmAifCurrentTable_Object = MibTable
pmAifCurrentTable = _PmAifCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 2, 2)
)
if mibBuilder.loadTexts:
    pmAifCurrentTable.setStatus("current")
_PmAifCurrentEntry_Object = MibTableRow
pmAifCurrentEntry = _PmAifCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 2, 2, 1)
)
pmAifCurrentEntry.setIndexNames(
    (0, "NETI-PM-MIB", "pmAifIndex"),
)
if mibBuilder.loadTexts:
    pmAifCurrentEntry.setStatus("current")
_PmAifCurrentTime_Type = Counter15m
_PmAifCurrentTime_Object = MibTableColumn
pmAifCurrentTime = _PmAifCurrentTime_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 2, 2, 1, 2),
    _PmAifCurrentTime_Type()
)
pmAifCurrentTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmAifCurrentTime.setStatus("current")
_PmAifCurrentSuspect_Type = TruthValue
_PmAifCurrentSuspect_Object = MibTableColumn
pmAifCurrentSuspect = _PmAifCurrentSuspect_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 2, 2, 1, 3),
    _PmAifCurrentSuspect_Type()
)
pmAifCurrentSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmAifCurrentSuspect.setStatus("current")
_PmAifCurrentZS_Type = Counter32
_PmAifCurrentZS_Object = MibTableColumn
pmAifCurrentZS = _PmAifCurrentZS_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 2, 2, 1, 4),
    _PmAifCurrentZS_Type()
)
pmAifCurrentZS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmAifCurrentZS.setStatus("current")
_PmAifCurrentESs_Type = Counter15m
_PmAifCurrentESs_Object = MibTableColumn
pmAifCurrentESs = _PmAifCurrentESs_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 2, 2, 1, 5),
    _PmAifCurrentESs_Type()
)
pmAifCurrentESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmAifCurrentESs.setStatus("current")
_PmAifCurrentSESs_Type = Counter15m
_PmAifCurrentSESs_Object = MibTableColumn
pmAifCurrentSESs = _PmAifCurrentSESs_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 2, 2, 1, 6),
    _PmAifCurrentSESs_Type()
)
pmAifCurrentSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmAifCurrentSESs.setStatus("current")
_PmAifCurrentBBEs_Type = Gauge32
_PmAifCurrentBBEs_Object = MibTableColumn
pmAifCurrentBBEs = _PmAifCurrentBBEs_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 2, 2, 1, 7),
    _PmAifCurrentBBEs_Type()
)
pmAifCurrentBBEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmAifCurrentBBEs.setStatus("current")
_PmAifCurrentUASs_Type = Counter15m
_PmAifCurrentUASs_Object = MibTableColumn
pmAifCurrentUASs = _PmAifCurrentUASs_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 2, 2, 1, 8),
    _PmAifCurrentUASs_Type()
)
pmAifCurrentUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmAifCurrentUASs.setStatus("current")
_PmAif15mTable_Object = MibTable
pmAif15mTable = _PmAif15mTable_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 2, 3)
)
if mibBuilder.loadTexts:
    pmAif15mTable.setStatus("current")
_PmAif15mEntry_Object = MibTableRow
pmAif15mEntry = _PmAif15mEntry_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 2, 3, 1)
)
pmAif15mEntry.setIndexNames(
    (0, "NETI-PM-MIB", "pmAifIndex"),
    (0, "NETI-PM-MIB", "pmAif15mIndex"),
)
if mibBuilder.loadTexts:
    pmAif15mEntry.setStatus("current")
_PmAif15mIndex_Type = Unsigned32
_PmAif15mIndex_Object = MibTableColumn
pmAif15mIndex = _PmAif15mIndex_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 2, 3, 1, 1),
    _PmAif15mIndex_Type()
)
pmAif15mIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pmAif15mIndex.setStatus("current")
_PmAif15mTime_Type = DateAndTime
_PmAif15mTime_Object = MibTableColumn
pmAif15mTime = _PmAif15mTime_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 2, 3, 1, 2),
    _PmAif15mTime_Type()
)
pmAif15mTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmAif15mTime.setStatus("current")
_PmAif15mSuspect_Type = TruthValue
_PmAif15mSuspect_Object = MibTableColumn
pmAif15mSuspect = _PmAif15mSuspect_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 2, 3, 1, 3),
    _PmAif15mSuspect_Type()
)
pmAif15mSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmAif15mSuspect.setStatus("current")
_PmAif15mZS_Type = Counter32
_PmAif15mZS_Object = MibTableColumn
pmAif15mZS = _PmAif15mZS_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 2, 3, 1, 4),
    _PmAif15mZS_Type()
)
pmAif15mZS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmAif15mZS.setStatus("current")
_PmAif15mESs_Type = Counter15m
_PmAif15mESs_Object = MibTableColumn
pmAif15mESs = _PmAif15mESs_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 2, 3, 1, 5),
    _PmAif15mESs_Type()
)
pmAif15mESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmAif15mESs.setStatus("current")
_PmAif15mSESs_Type = Counter15m
_PmAif15mSESs_Object = MibTableColumn
pmAif15mSESs = _PmAif15mSESs_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 2, 3, 1, 6),
    _PmAif15mSESs_Type()
)
pmAif15mSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmAif15mSESs.setStatus("current")
_PmAif15mBBEs_Type = Gauge32
_PmAif15mBBEs_Object = MibTableColumn
pmAif15mBBEs = _PmAif15mBBEs_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 2, 3, 1, 7),
    _PmAif15mBBEs_Type()
)
pmAif15mBBEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmAif15mBBEs.setStatus("current")
_PmAif15mUASs_Type = Counter15m
_PmAif15mUASs_Object = MibTableColumn
pmAif15mUASs = _PmAif15mUASs_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 2, 3, 1, 8),
    _PmAif15mUASs_Type()
)
pmAif15mUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmAif15mUASs.setStatus("current")
_PmAif24hTable_Object = MibTable
pmAif24hTable = _PmAif24hTable_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 2, 4)
)
if mibBuilder.loadTexts:
    pmAif24hTable.setStatus("current")
_PmAif24hEntry_Object = MibTableRow
pmAif24hEntry = _PmAif24hEntry_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 2, 4, 1)
)
pmAif24hEntry.setIndexNames(
    (0, "NETI-PM-MIB", "pmAifIndex"),
    (0, "NETI-PM-MIB", "pmAif24hIndex"),
)
if mibBuilder.loadTexts:
    pmAif24hEntry.setStatus("current")
_PmAif24hIndex_Type = Unsigned32
_PmAif24hIndex_Object = MibTableColumn
pmAif24hIndex = _PmAif24hIndex_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 2, 4, 1, 1),
    _PmAif24hIndex_Type()
)
pmAif24hIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pmAif24hIndex.setStatus("current")
_PmAif24hTime_Type = DateAndTime
_PmAif24hTime_Object = MibTableColumn
pmAif24hTime = _PmAif24hTime_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 2, 4, 1, 2),
    _PmAif24hTime_Type()
)
pmAif24hTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmAif24hTime.setStatus("current")
_PmAif24hSuspect_Type = TruthValue
_PmAif24hSuspect_Object = MibTableColumn
pmAif24hSuspect = _PmAif24hSuspect_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 2, 4, 1, 3),
    _PmAif24hSuspect_Type()
)
pmAif24hSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmAif24hSuspect.setStatus("current")
_PmAif24hZS_Type = Counter32
_PmAif24hZS_Object = MibTableColumn
pmAif24hZS = _PmAif24hZS_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 2, 4, 1, 4),
    _PmAif24hZS_Type()
)
pmAif24hZS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmAif24hZS.setStatus("current")
_PmAif24hESs_Type = Counter24h
_PmAif24hESs_Object = MibTableColumn
pmAif24hESs = _PmAif24hESs_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 2, 4, 1, 5),
    _PmAif24hESs_Type()
)
pmAif24hESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmAif24hESs.setStatus("current")
_PmAif24hSESs_Type = Counter24h
_PmAif24hSESs_Object = MibTableColumn
pmAif24hSESs = _PmAif24hSESs_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 2, 4, 1, 6),
    _PmAif24hSESs_Type()
)
pmAif24hSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmAif24hSESs.setStatus("current")
_PmAif24hBBEs_Type = Gauge32
_PmAif24hBBEs_Object = MibTableColumn
pmAif24hBBEs = _PmAif24hBBEs_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 2, 4, 1, 7),
    _PmAif24hBBEs_Type()
)
pmAif24hBBEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmAif24hBBEs.setStatus("current")
_PmAif24hUASs_Type = Counter24h
_PmAif24hUASs_Object = MibTableColumn
pmAif24hUASs = _PmAif24hUASs_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 2, 4, 1, 8),
    _PmAif24hUASs_Type()
)
pmAif24hUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmAif24hUASs.setStatus("current")
_PmAif24hCurrentTable_Object = MibTable
pmAif24hCurrentTable = _PmAif24hCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 2, 5)
)
if mibBuilder.loadTexts:
    pmAif24hCurrentTable.setStatus("current")
_PmAif24hCurrentEntry_Object = MibTableRow
pmAif24hCurrentEntry = _PmAif24hCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 2, 5, 1)
)
pmAif24hCurrentEntry.setIndexNames(
    (0, "NETI-PM-MIB", "pmAifIndex"),
)
if mibBuilder.loadTexts:
    pmAif24hCurrentEntry.setStatus("current")
_PmAif24hCurrentTime_Type = Counter15m
_PmAif24hCurrentTime_Object = MibTableColumn
pmAif24hCurrentTime = _PmAif24hCurrentTime_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 2, 5, 1, 2),
    _PmAif24hCurrentTime_Type()
)
pmAif24hCurrentTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmAif24hCurrentTime.setStatus("current")
_PmAif24hCurrentSuspect_Type = TruthValue
_PmAif24hCurrentSuspect_Object = MibTableColumn
pmAif24hCurrentSuspect = _PmAif24hCurrentSuspect_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 2, 5, 1, 3),
    _PmAif24hCurrentSuspect_Type()
)
pmAif24hCurrentSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmAif24hCurrentSuspect.setStatus("current")
_PmAif24hCurrentZS_Type = Counter32
_PmAif24hCurrentZS_Object = MibTableColumn
pmAif24hCurrentZS = _PmAif24hCurrentZS_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 2, 5, 1, 4),
    _PmAif24hCurrentZS_Type()
)
pmAif24hCurrentZS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmAif24hCurrentZS.setStatus("current")
_PmAif24hCurrentESs_Type = Counter15m
_PmAif24hCurrentESs_Object = MibTableColumn
pmAif24hCurrentESs = _PmAif24hCurrentESs_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 2, 5, 1, 5),
    _PmAif24hCurrentESs_Type()
)
pmAif24hCurrentESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmAif24hCurrentESs.setStatus("current")
_PmAif24hCurrentSESs_Type = Counter15m
_PmAif24hCurrentSESs_Object = MibTableColumn
pmAif24hCurrentSESs = _PmAif24hCurrentSESs_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 2, 5, 1, 6),
    _PmAif24hCurrentSESs_Type()
)
pmAif24hCurrentSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmAif24hCurrentSESs.setStatus("current")
_PmAif24hCurrentBBEs_Type = Gauge32
_PmAif24hCurrentBBEs_Object = MibTableColumn
pmAif24hCurrentBBEs = _PmAif24hCurrentBBEs_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 2, 5, 1, 7),
    _PmAif24hCurrentBBEs_Type()
)
pmAif24hCurrentBBEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmAif24hCurrentBBEs.setStatus("current")
_PmAif24hCurrentUASs_Type = Counter15m
_PmAif24hCurrentUASs_Object = MibTableColumn
pmAif24hCurrentUASs = _PmAif24hCurrentUASs_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 2, 5, 1, 8),
    _PmAif24hCurrentUASs_Type()
)
pmAif24hCurrentUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmAif24hCurrentUASs.setStatus("current")
_PmDchGroup_ObjectIdentity = ObjectIdentity
pmDchGroup = _PmDchGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 3)
)
_PmDchTable_Object = MibTable
pmDchTable = _PmDchTable_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 3, 1)
)
if mibBuilder.loadTexts:
    pmDchTable.setStatus("current")
_PmDchEntry_Object = MibTableRow
pmDchEntry = _PmDchEntry_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 3, 1, 1)
)
pmDchEntry.setIndexNames(
    (0, "NETI-PM-MIB", "pmDchIndex"),
)
if mibBuilder.loadTexts:
    pmDchEntry.setStatus("current")
_PmDchIndex_Type = Unsigned32
_PmDchIndex_Object = MibTableColumn
pmDchIndex = _PmDchIndex_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 3, 1, 1, 1),
    _PmDchIndex_Type()
)
pmDchIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pmDchIndex.setStatus("current")


class _PmDchAdminStatus_Type(Integer32):
    """Custom type pmDchAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_PmDchAdminStatus_Type.__name__ = "Integer32"
_PmDchAdminStatus_Object = MibTableColumn
pmDchAdminStatus = _PmDchAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 3, 1, 1, 2),
    _PmDchAdminStatus_Type()
)
pmDchAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmDchAdminStatus.setStatus("current")


class _PmDchOperStatus_Type(Integer32):
    """Custom type pmDchOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_PmDchOperStatus_Type.__name__ = "Integer32"
_PmDchOperStatus_Object = MibTableColumn
pmDchOperStatus = _PmDchOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 3, 1, 1, 3),
    _PmDchOperStatus_Type()
)
pmDchOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmDchOperStatus.setStatus("current")
_PmDchFailure_Type = DisplayString
_PmDchFailure_Object = MibTableColumn
pmDchFailure = _PmDchFailure_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 3, 1, 1, 4),
    _PmDchFailure_Type()
)
pmDchFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmDchFailure.setStatus("current")
_PmDchDataSource_Type = ObjectIdentifier
_PmDchDataSource_Object = MibTableColumn
pmDchDataSource = _PmDchDataSource_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 3, 1, 1, 5),
    _PmDchDataSource_Type()
)
pmDchDataSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmDchDataSource.setStatus("current")
_PmDchDataSourceName_Type = DisplayString
_PmDchDataSourceName_Object = MibTableColumn
pmDchDataSourceName = _PmDchDataSourceName_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 3, 1, 1, 6),
    _PmDchDataSourceName_Type()
)
pmDchDataSourceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmDchDataSourceName.setStatus("current")
_PmDchUatAlarmsEnabled_Type = TruthValue
_PmDchUatAlarmsEnabled_Object = MibTableColumn
pmDchUatAlarmsEnabled = _PmDchUatAlarmsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 3, 1, 1, 7),
    _PmDchUatAlarmsEnabled_Type()
)
pmDchUatAlarmsEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmDchUatAlarmsEnabled.setStatus("current")
_PmDchTresholdAlarmsEnabled_Type = TruthValue
_PmDchTresholdAlarmsEnabled_Object = MibTableColumn
pmDchTresholdAlarmsEnabled = _PmDchTresholdAlarmsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 3, 1, 1, 8),
    _PmDchTresholdAlarmsEnabled_Type()
)
pmDchTresholdAlarmsEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmDchTresholdAlarmsEnabled.setStatus("current")
_PmDchPeriodicEventsEnabled_Type = TruthValue
_PmDchPeriodicEventsEnabled_Object = MibTableColumn
pmDchPeriodicEventsEnabled = _PmDchPeriodicEventsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 3, 1, 1, 9),
    _PmDchPeriodicEventsEnabled_Type()
)
pmDchPeriodicEventsEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmDchPeriodicEventsEnabled.setStatus("current")
_PmDchZeroSuppressionEnabled_Type = TruthValue
_PmDchZeroSuppressionEnabled_Object = MibTableColumn
pmDchZeroSuppressionEnabled = _PmDchZeroSuppressionEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 3, 1, 1, 10),
    _PmDchZeroSuppressionEnabled_Type()
)
pmDchZeroSuppressionEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmDchZeroSuppressionEnabled.setStatus("current")


class _PmDchHistorySize_Type(Integer32):
    """Custom type pmDchHistorySize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("large", 3),
          ("none", 1),
          ("small", 2))
    )


_PmDchHistorySize_Type.__name__ = "Integer32"
_PmDchHistorySize_Object = MibTableColumn
pmDchHistorySize = _PmDchHistorySize_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 3, 1, 1, 11),
    _PmDchHistorySize_Type()
)
pmDchHistorySize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmDchHistorySize.setStatus("current")
_PmDch15mTresholdES_Type = Counter15m
_PmDch15mTresholdES_Object = MibTableColumn
pmDch15mTresholdES = _PmDch15mTresholdES_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 3, 1, 1, 12),
    _PmDch15mTresholdES_Type()
)
pmDch15mTresholdES.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmDch15mTresholdES.setStatus("current")
_PmDch15mTresholdSES_Type = Counter15m
_PmDch15mTresholdSES_Object = MibTableColumn
pmDch15mTresholdSES = _PmDch15mTresholdSES_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 3, 1, 1, 13),
    _PmDch15mTresholdSES_Type()
)
pmDch15mTresholdSES.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmDch15mTresholdSES.setStatus("current")
_PmDch15mTresholdBBE_Type = Gauge32
_PmDch15mTresholdBBE_Object = MibTableColumn
pmDch15mTresholdBBE = _PmDch15mTresholdBBE_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 3, 1, 1, 14),
    _PmDch15mTresholdBBE_Type()
)
pmDch15mTresholdBBE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmDch15mTresholdBBE.setStatus("current")
_PmDch24hTresholdES_Type = Counter24h
_PmDch24hTresholdES_Object = MibTableColumn
pmDch24hTresholdES = _PmDch24hTresholdES_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 3, 1, 1, 15),
    _PmDch24hTresholdES_Type()
)
pmDch24hTresholdES.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmDch24hTresholdES.setStatus("current")
_PmDch24hTresholdSES_Type = Counter24h
_PmDch24hTresholdSES_Object = MibTableColumn
pmDch24hTresholdSES = _PmDch24hTresholdSES_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 3, 1, 1, 16),
    _PmDch24hTresholdSES_Type()
)
pmDch24hTresholdSES.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmDch24hTresholdSES.setStatus("current")
_PmDch24hTresholdBBE_Type = Gauge32
_PmDch24hTresholdBBE_Object = MibTableColumn
pmDch24hTresholdBBE = _PmDch24hTresholdBBE_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 3, 1, 1, 17),
    _PmDch24hTresholdBBE_Type()
)
pmDch24hTresholdBBE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmDch24hTresholdBBE.setStatus("current")
_PmDchCurrentTable_Object = MibTable
pmDchCurrentTable = _PmDchCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 3, 2)
)
if mibBuilder.loadTexts:
    pmDchCurrentTable.setStatus("current")
_PmDchCurrentEntry_Object = MibTableRow
pmDchCurrentEntry = _PmDchCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 3, 2, 1)
)
pmDchCurrentEntry.setIndexNames(
    (0, "NETI-PM-MIB", "pmDchIndex"),
)
if mibBuilder.loadTexts:
    pmDchCurrentEntry.setStatus("current")
_PmDchCurrentTime_Type = Counter15m
_PmDchCurrentTime_Object = MibTableColumn
pmDchCurrentTime = _PmDchCurrentTime_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 3, 2, 1, 2),
    _PmDchCurrentTime_Type()
)
pmDchCurrentTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmDchCurrentTime.setStatus("current")
_PmDchCurrentSuspect_Type = TruthValue
_PmDchCurrentSuspect_Object = MibTableColumn
pmDchCurrentSuspect = _PmDchCurrentSuspect_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 3, 2, 1, 3),
    _PmDchCurrentSuspect_Type()
)
pmDchCurrentSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmDchCurrentSuspect.setStatus("current")
_PmDchCurrentZS_Type = Counter32
_PmDchCurrentZS_Object = MibTableColumn
pmDchCurrentZS = _PmDchCurrentZS_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 3, 2, 1, 4),
    _PmDchCurrentZS_Type()
)
pmDchCurrentZS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmDchCurrentZS.setStatus("current")
_PmDchCurrentESs_Type = Counter15m
_PmDchCurrentESs_Object = MibTableColumn
pmDchCurrentESs = _PmDchCurrentESs_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 3, 2, 1, 5),
    _PmDchCurrentESs_Type()
)
pmDchCurrentESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmDchCurrentESs.setStatus("current")
_PmDchCurrentSESs_Type = Counter15m
_PmDchCurrentSESs_Object = MibTableColumn
pmDchCurrentSESs = _PmDchCurrentSESs_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 3, 2, 1, 6),
    _PmDchCurrentSESs_Type()
)
pmDchCurrentSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmDchCurrentSESs.setStatus("current")
_PmDchCurrentBBEs_Type = Gauge32
_PmDchCurrentBBEs_Object = MibTableColumn
pmDchCurrentBBEs = _PmDchCurrentBBEs_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 3, 2, 1, 7),
    _PmDchCurrentBBEs_Type()
)
pmDchCurrentBBEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmDchCurrentBBEs.setStatus("current")
_PmDchCurrentUASs_Type = Counter15m
_PmDchCurrentUASs_Object = MibTableColumn
pmDchCurrentUASs = _PmDchCurrentUASs_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 3, 2, 1, 8),
    _PmDchCurrentUASs_Type()
)
pmDchCurrentUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmDchCurrentUASs.setStatus("current")
_PmDch15mTable_Object = MibTable
pmDch15mTable = _PmDch15mTable_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 3, 3)
)
if mibBuilder.loadTexts:
    pmDch15mTable.setStatus("current")
_PmDch15mEntry_Object = MibTableRow
pmDch15mEntry = _PmDch15mEntry_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 3, 3, 1)
)
pmDch15mEntry.setIndexNames(
    (0, "NETI-PM-MIB", "pmDchIndex"),
    (0, "NETI-PM-MIB", "pmDch15mIndex"),
)
if mibBuilder.loadTexts:
    pmDch15mEntry.setStatus("current")
_PmDch15mIndex_Type = Unsigned32
_PmDch15mIndex_Object = MibTableColumn
pmDch15mIndex = _PmDch15mIndex_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 3, 3, 1, 1),
    _PmDch15mIndex_Type()
)
pmDch15mIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pmDch15mIndex.setStatus("current")
_PmDch15mTime_Type = DateAndTime
_PmDch15mTime_Object = MibTableColumn
pmDch15mTime = _PmDch15mTime_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 3, 3, 1, 2),
    _PmDch15mTime_Type()
)
pmDch15mTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmDch15mTime.setStatus("current")
_PmDch15mSuspect_Type = TruthValue
_PmDch15mSuspect_Object = MibTableColumn
pmDch15mSuspect = _PmDch15mSuspect_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 3, 3, 1, 3),
    _PmDch15mSuspect_Type()
)
pmDch15mSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmDch15mSuspect.setStatus("current")
_PmDch15mZS_Type = Counter32
_PmDch15mZS_Object = MibTableColumn
pmDch15mZS = _PmDch15mZS_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 3, 3, 1, 4),
    _PmDch15mZS_Type()
)
pmDch15mZS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmDch15mZS.setStatus("current")
_PmDch15mESs_Type = Counter15m
_PmDch15mESs_Object = MibTableColumn
pmDch15mESs = _PmDch15mESs_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 3, 3, 1, 5),
    _PmDch15mESs_Type()
)
pmDch15mESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmDch15mESs.setStatus("current")
_PmDch15mSESs_Type = Counter15m
_PmDch15mSESs_Object = MibTableColumn
pmDch15mSESs = _PmDch15mSESs_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 3, 3, 1, 6),
    _PmDch15mSESs_Type()
)
pmDch15mSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmDch15mSESs.setStatus("current")
_PmDch15mBBEs_Type = Gauge32
_PmDch15mBBEs_Object = MibTableColumn
pmDch15mBBEs = _PmDch15mBBEs_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 3, 3, 1, 7),
    _PmDch15mBBEs_Type()
)
pmDch15mBBEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmDch15mBBEs.setStatus("current")
_PmDch15mUASs_Type = Counter15m
_PmDch15mUASs_Object = MibTableColumn
pmDch15mUASs = _PmDch15mUASs_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 3, 3, 1, 8),
    _PmDch15mUASs_Type()
)
pmDch15mUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmDch15mUASs.setStatus("current")
_PmDch24hTable_Object = MibTable
pmDch24hTable = _PmDch24hTable_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 3, 4)
)
if mibBuilder.loadTexts:
    pmDch24hTable.setStatus("current")
_PmDch24hEntry_Object = MibTableRow
pmDch24hEntry = _PmDch24hEntry_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 3, 4, 1)
)
pmDch24hEntry.setIndexNames(
    (0, "NETI-PM-MIB", "pmDchIndex"),
    (0, "NETI-PM-MIB", "pmDch24hIndex"),
)
if mibBuilder.loadTexts:
    pmDch24hEntry.setStatus("current")
_PmDch24hIndex_Type = Unsigned32
_PmDch24hIndex_Object = MibTableColumn
pmDch24hIndex = _PmDch24hIndex_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 3, 4, 1, 1),
    _PmDch24hIndex_Type()
)
pmDch24hIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pmDch24hIndex.setStatus("current")
_PmDch24hTime_Type = DateAndTime
_PmDch24hTime_Object = MibTableColumn
pmDch24hTime = _PmDch24hTime_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 3, 4, 1, 2),
    _PmDch24hTime_Type()
)
pmDch24hTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmDch24hTime.setStatus("current")
_PmDch24hSuspect_Type = TruthValue
_PmDch24hSuspect_Object = MibTableColumn
pmDch24hSuspect = _PmDch24hSuspect_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 3, 4, 1, 3),
    _PmDch24hSuspect_Type()
)
pmDch24hSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmDch24hSuspect.setStatus("current")
_PmDch24hZS_Type = Counter32
_PmDch24hZS_Object = MibTableColumn
pmDch24hZS = _PmDch24hZS_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 3, 4, 1, 4),
    _PmDch24hZS_Type()
)
pmDch24hZS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmDch24hZS.setStatus("current")
_PmDch24hESs_Type = Counter24h
_PmDch24hESs_Object = MibTableColumn
pmDch24hESs = _PmDch24hESs_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 3, 4, 1, 5),
    _PmDch24hESs_Type()
)
pmDch24hESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmDch24hESs.setStatus("current")
_PmDch24hSESs_Type = Counter24h
_PmDch24hSESs_Object = MibTableColumn
pmDch24hSESs = _PmDch24hSESs_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 3, 4, 1, 6),
    _PmDch24hSESs_Type()
)
pmDch24hSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmDch24hSESs.setStatus("current")
_PmDch24hBBEs_Type = Gauge32
_PmDch24hBBEs_Object = MibTableColumn
pmDch24hBBEs = _PmDch24hBBEs_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 3, 4, 1, 7),
    _PmDch24hBBEs_Type()
)
pmDch24hBBEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmDch24hBBEs.setStatus("current")
_PmDch24hUASs_Type = Counter24h
_PmDch24hUASs_Object = MibTableColumn
pmDch24hUASs = _PmDch24hUASs_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 3, 4, 1, 8),
    _PmDch24hUASs_Type()
)
pmDch24hUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmDch24hUASs.setStatus("current")
_PmDch24hCurrentTable_Object = MibTable
pmDch24hCurrentTable = _PmDch24hCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 3, 5)
)
if mibBuilder.loadTexts:
    pmDch24hCurrentTable.setStatus("current")
_PmDch24hCurrentEntry_Object = MibTableRow
pmDch24hCurrentEntry = _PmDch24hCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 3, 5, 1)
)
pmDch24hCurrentEntry.setIndexNames(
    (0, "NETI-PM-MIB", "pmDchIndex"),
)
if mibBuilder.loadTexts:
    pmDch24hCurrentEntry.setStatus("current")
_PmDch24hCurrentTime_Type = Counter15m
_PmDch24hCurrentTime_Object = MibTableColumn
pmDch24hCurrentTime = _PmDch24hCurrentTime_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 3, 5, 1, 2),
    _PmDch24hCurrentTime_Type()
)
pmDch24hCurrentTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmDch24hCurrentTime.setStatus("current")
_PmDch24hCurrentSuspect_Type = TruthValue
_PmDch24hCurrentSuspect_Object = MibTableColumn
pmDch24hCurrentSuspect = _PmDch24hCurrentSuspect_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 3, 5, 1, 3),
    _PmDch24hCurrentSuspect_Type()
)
pmDch24hCurrentSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmDch24hCurrentSuspect.setStatus("current")
_PmDch24hCurrentZS_Type = Counter32
_PmDch24hCurrentZS_Object = MibTableColumn
pmDch24hCurrentZS = _PmDch24hCurrentZS_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 3, 5, 1, 4),
    _PmDch24hCurrentZS_Type()
)
pmDch24hCurrentZS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmDch24hCurrentZS.setStatus("current")
_PmDch24hCurrentESs_Type = Counter15m
_PmDch24hCurrentESs_Object = MibTableColumn
pmDch24hCurrentESs = _PmDch24hCurrentESs_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 3, 5, 1, 5),
    _PmDch24hCurrentESs_Type()
)
pmDch24hCurrentESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmDch24hCurrentESs.setStatus("current")
_PmDch24hCurrentSESs_Type = Counter15m
_PmDch24hCurrentSESs_Object = MibTableColumn
pmDch24hCurrentSESs = _PmDch24hCurrentSESs_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 3, 5, 1, 6),
    _PmDch24hCurrentSESs_Type()
)
pmDch24hCurrentSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmDch24hCurrentSESs.setStatus("current")
_PmDch24hCurrentBBEs_Type = Gauge32
_PmDch24hCurrentBBEs_Object = MibTableColumn
pmDch24hCurrentBBEs = _PmDch24hCurrentBBEs_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 3, 5, 1, 7),
    _PmDch24hCurrentBBEs_Type()
)
pmDch24hCurrentBBEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmDch24hCurrentBBEs.setStatus("current")
_PmDch24hCurrentUASs_Type = Counter15m
_PmDch24hCurrentUASs_Object = MibTableColumn
pmDch24hCurrentUASs = _PmDch24hCurrentUASs_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 3, 5, 1, 8),
    _PmDch24hCurrentUASs_Type()
)
pmDch24hCurrentUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmDch24hCurrentUASs.setStatus("current")
_PmConformanceGroups_ObjectIdentity = ObjectIdentity
pmConformanceGroups = _PmConformanceGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 4)
)

# Managed Objects groups

pmTifConformanceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 4, 1)
)
pmTifConformanceGroup.setObjects(
      *(("NETI-PM-MIB", "pmTifAdminStatus"),
        ("NETI-PM-MIB", "pmTifOperStatus"),
        ("NETI-PM-MIB", "pmTifFailure"),
        ("NETI-PM-MIB", "pmTifDataSource"),
        ("NETI-PM-MIB", "pmTifDataSourceName"),
        ("NETI-PM-MIB", "pmTifUatAlarmsEnabled"),
        ("NETI-PM-MIB", "pmTifTresholdAlarmsEnabled"),
        ("NETI-PM-MIB", "pmTifPeriodicEventsEnabled"),
        ("NETI-PM-MIB", "pmTifZeroSuppressionEnabled"),
        ("NETI-PM-MIB", "pmTifHistorySize"),
        ("NETI-PM-MIB", "pmTif15mTresholdES"),
        ("NETI-PM-MIB", "pmTif15mTresholdSES"),
        ("NETI-PM-MIB", "pmTif15mTresholdBBE"),
        ("NETI-PM-MIB", "pmTif15mTresholdSS"),
        ("NETI-PM-MIB", "pmTif24hTresholdES"),
        ("NETI-PM-MIB", "pmTif24hTresholdSES"),
        ("NETI-PM-MIB", "pmTif24hTresholdBBE"),
        ("NETI-PM-MIB", "pmTif24hTresholdSS"),
        ("NETI-PM-MIB", "pmTifCurrentTime"),
        ("NETI-PM-MIB", "pmTifCurrentSuspect"),
        ("NETI-PM-MIB", "pmTifCurrentZS"),
        ("NETI-PM-MIB", "pmTifCurrentESs"),
        ("NETI-PM-MIB", "pmTifCurrentSESs"),
        ("NETI-PM-MIB", "pmTifCurrentBBEs"),
        ("NETI-PM-MIB", "pmTifCurrentUASs"),
        ("NETI-PM-MIB", "pmTifCurrentSSs"),
        ("NETI-PM-MIB", "pmTif15mTime"),
        ("NETI-PM-MIB", "pmTif15mSuspect"),
        ("NETI-PM-MIB", "pmTif15mZS"),
        ("NETI-PM-MIB", "pmTif15mESs"),
        ("NETI-PM-MIB", "pmTif15mSESs"),
        ("NETI-PM-MIB", "pmTif15mBBEs"),
        ("NETI-PM-MIB", "pmTif15mUASs"),
        ("NETI-PM-MIB", "pmTif15mSSs"),
        ("NETI-PM-MIB", "pmTif24hTime"),
        ("NETI-PM-MIB", "pmTif24hSuspect"),
        ("NETI-PM-MIB", "pmTif24hZS"),
        ("NETI-PM-MIB", "pmTif24hESs"),
        ("NETI-PM-MIB", "pmTif24hSESs"),
        ("NETI-PM-MIB", "pmTif24hBBEs"),
        ("NETI-PM-MIB", "pmTif24hUASs"),
        ("NETI-PM-MIB", "pmTif24hSSs"),
        ("NETI-PM-MIB", "pmTif24hCurrentTime"),
        ("NETI-PM-MIB", "pmTif24hCurrentSuspect"),
        ("NETI-PM-MIB", "pmTif24hCurrentZS"),
        ("NETI-PM-MIB", "pmTif24hCurrentESs"),
        ("NETI-PM-MIB", "pmTif24hCurrentSESs"),
        ("NETI-PM-MIB", "pmTif24hCurrentBBEs"),
        ("NETI-PM-MIB", "pmTif24hCurrentUASs"),
        ("NETI-PM-MIB", "pmTif24hCurrentSSs"))
)
if mibBuilder.loadTexts:
    pmTifConformanceGroup.setStatus("current")

pmAifConformanceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 4, 2)
)
pmAifConformanceGroup.setObjects(
      *(("NETI-PM-MIB", "pmAifAdminStatus"),
        ("NETI-PM-MIB", "pmAifOperStatus"),
        ("NETI-PM-MIB", "pmAifFailure"),
        ("NETI-PM-MIB", "pmAifDataSource"),
        ("NETI-PM-MIB", "pmAifDataSourceName"),
        ("NETI-PM-MIB", "pmAifUatAlarmsEnabled"),
        ("NETI-PM-MIB", "pmAifTresholdAlarmsEnabled"),
        ("NETI-PM-MIB", "pmAifPeriodicEventsEnabled"),
        ("NETI-PM-MIB", "pmAifZeroSuppressionEnabled"),
        ("NETI-PM-MIB", "pmAifHistorySize"),
        ("NETI-PM-MIB", "pmAif15mTresholdES"),
        ("NETI-PM-MIB", "pmAif15mTresholdSES"),
        ("NETI-PM-MIB", "pmAif15mTresholdBBE"),
        ("NETI-PM-MIB", "pmAif24hTresholdES"),
        ("NETI-PM-MIB", "pmAif24hTresholdSES"),
        ("NETI-PM-MIB", "pmAif24hTresholdBBE"),
        ("NETI-PM-MIB", "pmAifCurrentTime"),
        ("NETI-PM-MIB", "pmAifCurrentSuspect"),
        ("NETI-PM-MIB", "pmAifCurrentZS"),
        ("NETI-PM-MIB", "pmAifCurrentESs"),
        ("NETI-PM-MIB", "pmAifCurrentSESs"),
        ("NETI-PM-MIB", "pmAifCurrentBBEs"),
        ("NETI-PM-MIB", "pmAifCurrentUASs"),
        ("NETI-PM-MIB", "pmAif15mTime"),
        ("NETI-PM-MIB", "pmAif15mSuspect"),
        ("NETI-PM-MIB", "pmAif15mZS"),
        ("NETI-PM-MIB", "pmAif15mESs"),
        ("NETI-PM-MIB", "pmAif15mSESs"),
        ("NETI-PM-MIB", "pmAif15mBBEs"),
        ("NETI-PM-MIB", "pmAif15mUASs"),
        ("NETI-PM-MIB", "pmAif24hTime"),
        ("NETI-PM-MIB", "pmAif24hSuspect"),
        ("NETI-PM-MIB", "pmAif24hZS"),
        ("NETI-PM-MIB", "pmAif24hESs"),
        ("NETI-PM-MIB", "pmAif24hSESs"),
        ("NETI-PM-MIB", "pmAif24hBBEs"),
        ("NETI-PM-MIB", "pmAif24hUASs"),
        ("NETI-PM-MIB", "pmAif24hCurrentTime"),
        ("NETI-PM-MIB", "pmAif24hCurrentSuspect"),
        ("NETI-PM-MIB", "pmAif24hCurrentZS"),
        ("NETI-PM-MIB", "pmAif24hCurrentESs"),
        ("NETI-PM-MIB", "pmAif24hCurrentSESs"),
        ("NETI-PM-MIB", "pmAif24hCurrentBBEs"),
        ("NETI-PM-MIB", "pmAif24hCurrentUASs"))
)
if mibBuilder.loadTexts:
    pmAifConformanceGroup.setStatus("current")

pmDchConformanceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 17, 1, 4, 3)
)
pmDchConformanceGroup.setObjects(
      *(("NETI-PM-MIB", "pmDchAdminStatus"),
        ("NETI-PM-MIB", "pmDchOperStatus"),
        ("NETI-PM-MIB", "pmDchFailure"),
        ("NETI-PM-MIB", "pmDchDataSource"),
        ("NETI-PM-MIB", "pmDchDataSourceName"),
        ("NETI-PM-MIB", "pmDchUatAlarmsEnabled"),
        ("NETI-PM-MIB", "pmDchTresholdAlarmsEnabled"),
        ("NETI-PM-MIB", "pmDchPeriodicEventsEnabled"),
        ("NETI-PM-MIB", "pmDchZeroSuppressionEnabled"),
        ("NETI-PM-MIB", "pmDchHistorySize"),
        ("NETI-PM-MIB", "pmDch15mTresholdES"),
        ("NETI-PM-MIB", "pmDch15mTresholdSES"),
        ("NETI-PM-MIB", "pmDch15mTresholdBBE"),
        ("NETI-PM-MIB", "pmDch24hTresholdES"),
        ("NETI-PM-MIB", "pmDch24hTresholdSES"),
        ("NETI-PM-MIB", "pmDch24hTresholdBBE"),
        ("NETI-PM-MIB", "pmDchCurrentTime"),
        ("NETI-PM-MIB", "pmDchCurrentSuspect"),
        ("NETI-PM-MIB", "pmDchCurrentZS"),
        ("NETI-PM-MIB", "pmDchCurrentESs"),
        ("NETI-PM-MIB", "pmDchCurrentSESs"),
        ("NETI-PM-MIB", "pmDchCurrentBBEs"),
        ("NETI-PM-MIB", "pmDchCurrentUASs"),
        ("NETI-PM-MIB", "pmDch15mTime"),
        ("NETI-PM-MIB", "pmDch15mSuspect"),
        ("NETI-PM-MIB", "pmDch15mZS"),
        ("NETI-PM-MIB", "pmDch15mESs"),
        ("NETI-PM-MIB", "pmDch15mSESs"),
        ("NETI-PM-MIB", "pmDch15mBBEs"),
        ("NETI-PM-MIB", "pmDch15mUASs"),
        ("NETI-PM-MIB", "pmDch24hTime"),
        ("NETI-PM-MIB", "pmDch24hSuspect"),
        ("NETI-PM-MIB", "pmDch24hZS"),
        ("NETI-PM-MIB", "pmDch24hESs"),
        ("NETI-PM-MIB", "pmDch24hSESs"),
        ("NETI-PM-MIB", "pmDch24hBBEs"),
        ("NETI-PM-MIB", "pmDch24hUASs"),
        ("NETI-PM-MIB", "pmDch24hCurrentTime"),
        ("NETI-PM-MIB", "pmDch24hCurrentSuspect"),
        ("NETI-PM-MIB", "pmDch24hCurrentZS"),
        ("NETI-PM-MIB", "pmDch24hCurrentESs"),
        ("NETI-PM-MIB", "pmDch24hCurrentSESs"),
        ("NETI-PM-MIB", "pmDch24hCurrentBBEs"),
        ("NETI-PM-MIB", "pmDch24hCurrentUASs"))
)
if mibBuilder.loadTexts:
    pmDchConformanceGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NETI-PM-MIB",
    **{"Counter15m": Counter15m,
       "Counter24h": Counter24h,
       "netiPMMIB": netiPMMIB,
       "netiPMMIBObjects": netiPMMIBObjects,
       "pmTifGroup": pmTifGroup,
       "pmTifTable": pmTifTable,
       "pmTifEntry": pmTifEntry,
       "pmTifIndex": pmTifIndex,
       "pmTifAdminStatus": pmTifAdminStatus,
       "pmTifOperStatus": pmTifOperStatus,
       "pmTifFailure": pmTifFailure,
       "pmTifDataSource": pmTifDataSource,
       "pmTifDataSourceName": pmTifDataSourceName,
       "pmTifUatAlarmsEnabled": pmTifUatAlarmsEnabled,
       "pmTifTresholdAlarmsEnabled": pmTifTresholdAlarmsEnabled,
       "pmTifPeriodicEventsEnabled": pmTifPeriodicEventsEnabled,
       "pmTifZeroSuppressionEnabled": pmTifZeroSuppressionEnabled,
       "pmTifHistorySize": pmTifHistorySize,
       "pmTif15mTresholdES": pmTif15mTresholdES,
       "pmTif15mTresholdSES": pmTif15mTresholdSES,
       "pmTif15mTresholdBBE": pmTif15mTresholdBBE,
       "pmTif15mTresholdSS": pmTif15mTresholdSS,
       "pmTif24hTresholdES": pmTif24hTresholdES,
       "pmTif24hTresholdSES": pmTif24hTresholdSES,
       "pmTif24hTresholdBBE": pmTif24hTresholdBBE,
       "pmTif24hTresholdSS": pmTif24hTresholdSS,
       "pmTifCurrentTable": pmTifCurrentTable,
       "pmTifCurrentEntry": pmTifCurrentEntry,
       "pmTifCurrentTime": pmTifCurrentTime,
       "pmTifCurrentSuspect": pmTifCurrentSuspect,
       "pmTifCurrentZS": pmTifCurrentZS,
       "pmTifCurrentESs": pmTifCurrentESs,
       "pmTifCurrentSESs": pmTifCurrentSESs,
       "pmTifCurrentBBEs": pmTifCurrentBBEs,
       "pmTifCurrentUASs": pmTifCurrentUASs,
       "pmTifCurrentSSs": pmTifCurrentSSs,
       "pmTif15mTable": pmTif15mTable,
       "pmTif15mEntry": pmTif15mEntry,
       "pmTif15mIndex": pmTif15mIndex,
       "pmTif15mTime": pmTif15mTime,
       "pmTif15mSuspect": pmTif15mSuspect,
       "pmTif15mZS": pmTif15mZS,
       "pmTif15mESs": pmTif15mESs,
       "pmTif15mSESs": pmTif15mSESs,
       "pmTif15mBBEs": pmTif15mBBEs,
       "pmTif15mUASs": pmTif15mUASs,
       "pmTif15mSSs": pmTif15mSSs,
       "pmTif24hTable": pmTif24hTable,
       "pmTif24hEntry": pmTif24hEntry,
       "pmTif24hIndex": pmTif24hIndex,
       "pmTif24hTime": pmTif24hTime,
       "pmTif24hSuspect": pmTif24hSuspect,
       "pmTif24hZS": pmTif24hZS,
       "pmTif24hESs": pmTif24hESs,
       "pmTif24hSESs": pmTif24hSESs,
       "pmTif24hBBEs": pmTif24hBBEs,
       "pmTif24hUASs": pmTif24hUASs,
       "pmTif24hSSs": pmTif24hSSs,
       "pmTif24hCurrentTable": pmTif24hCurrentTable,
       "pmTif24hCurrentEntry": pmTif24hCurrentEntry,
       "pmTif24hCurrentTime": pmTif24hCurrentTime,
       "pmTif24hCurrentSuspect": pmTif24hCurrentSuspect,
       "pmTif24hCurrentZS": pmTif24hCurrentZS,
       "pmTif24hCurrentESs": pmTif24hCurrentESs,
       "pmTif24hCurrentSESs": pmTif24hCurrentSESs,
       "pmTif24hCurrentBBEs": pmTif24hCurrentBBEs,
       "pmTif24hCurrentUASs": pmTif24hCurrentUASs,
       "pmTif24hCurrentSSs": pmTif24hCurrentSSs,
       "pmAifGroup": pmAifGroup,
       "pmAifTable": pmAifTable,
       "pmAifEntry": pmAifEntry,
       "pmAifIndex": pmAifIndex,
       "pmAifAdminStatus": pmAifAdminStatus,
       "pmAifOperStatus": pmAifOperStatus,
       "pmAifFailure": pmAifFailure,
       "pmAifDataSource": pmAifDataSource,
       "pmAifDataSourceName": pmAifDataSourceName,
       "pmAifUatAlarmsEnabled": pmAifUatAlarmsEnabled,
       "pmAifTresholdAlarmsEnabled": pmAifTresholdAlarmsEnabled,
       "pmAifPeriodicEventsEnabled": pmAifPeriodicEventsEnabled,
       "pmAifZeroSuppressionEnabled": pmAifZeroSuppressionEnabled,
       "pmAifHistorySize": pmAifHistorySize,
       "pmAif15mTresholdES": pmAif15mTresholdES,
       "pmAif15mTresholdSES": pmAif15mTresholdSES,
       "pmAif15mTresholdBBE": pmAif15mTresholdBBE,
       "pmAif24hTresholdES": pmAif24hTresholdES,
       "pmAif24hTresholdSES": pmAif24hTresholdSES,
       "pmAif24hTresholdBBE": pmAif24hTresholdBBE,
       "pmAifCurrentTable": pmAifCurrentTable,
       "pmAifCurrentEntry": pmAifCurrentEntry,
       "pmAifCurrentTime": pmAifCurrentTime,
       "pmAifCurrentSuspect": pmAifCurrentSuspect,
       "pmAifCurrentZS": pmAifCurrentZS,
       "pmAifCurrentESs": pmAifCurrentESs,
       "pmAifCurrentSESs": pmAifCurrentSESs,
       "pmAifCurrentBBEs": pmAifCurrentBBEs,
       "pmAifCurrentUASs": pmAifCurrentUASs,
       "pmAif15mTable": pmAif15mTable,
       "pmAif15mEntry": pmAif15mEntry,
       "pmAif15mIndex": pmAif15mIndex,
       "pmAif15mTime": pmAif15mTime,
       "pmAif15mSuspect": pmAif15mSuspect,
       "pmAif15mZS": pmAif15mZS,
       "pmAif15mESs": pmAif15mESs,
       "pmAif15mSESs": pmAif15mSESs,
       "pmAif15mBBEs": pmAif15mBBEs,
       "pmAif15mUASs": pmAif15mUASs,
       "pmAif24hTable": pmAif24hTable,
       "pmAif24hEntry": pmAif24hEntry,
       "pmAif24hIndex": pmAif24hIndex,
       "pmAif24hTime": pmAif24hTime,
       "pmAif24hSuspect": pmAif24hSuspect,
       "pmAif24hZS": pmAif24hZS,
       "pmAif24hESs": pmAif24hESs,
       "pmAif24hSESs": pmAif24hSESs,
       "pmAif24hBBEs": pmAif24hBBEs,
       "pmAif24hUASs": pmAif24hUASs,
       "pmAif24hCurrentTable": pmAif24hCurrentTable,
       "pmAif24hCurrentEntry": pmAif24hCurrentEntry,
       "pmAif24hCurrentTime": pmAif24hCurrentTime,
       "pmAif24hCurrentSuspect": pmAif24hCurrentSuspect,
       "pmAif24hCurrentZS": pmAif24hCurrentZS,
       "pmAif24hCurrentESs": pmAif24hCurrentESs,
       "pmAif24hCurrentSESs": pmAif24hCurrentSESs,
       "pmAif24hCurrentBBEs": pmAif24hCurrentBBEs,
       "pmAif24hCurrentUASs": pmAif24hCurrentUASs,
       "pmDchGroup": pmDchGroup,
       "pmDchTable": pmDchTable,
       "pmDchEntry": pmDchEntry,
       "pmDchIndex": pmDchIndex,
       "pmDchAdminStatus": pmDchAdminStatus,
       "pmDchOperStatus": pmDchOperStatus,
       "pmDchFailure": pmDchFailure,
       "pmDchDataSource": pmDchDataSource,
       "pmDchDataSourceName": pmDchDataSourceName,
       "pmDchUatAlarmsEnabled": pmDchUatAlarmsEnabled,
       "pmDchTresholdAlarmsEnabled": pmDchTresholdAlarmsEnabled,
       "pmDchPeriodicEventsEnabled": pmDchPeriodicEventsEnabled,
       "pmDchZeroSuppressionEnabled": pmDchZeroSuppressionEnabled,
       "pmDchHistorySize": pmDchHistorySize,
       "pmDch15mTresholdES": pmDch15mTresholdES,
       "pmDch15mTresholdSES": pmDch15mTresholdSES,
       "pmDch15mTresholdBBE": pmDch15mTresholdBBE,
       "pmDch24hTresholdES": pmDch24hTresholdES,
       "pmDch24hTresholdSES": pmDch24hTresholdSES,
       "pmDch24hTresholdBBE": pmDch24hTresholdBBE,
       "pmDchCurrentTable": pmDchCurrentTable,
       "pmDchCurrentEntry": pmDchCurrentEntry,
       "pmDchCurrentTime": pmDchCurrentTime,
       "pmDchCurrentSuspect": pmDchCurrentSuspect,
       "pmDchCurrentZS": pmDchCurrentZS,
       "pmDchCurrentESs": pmDchCurrentESs,
       "pmDchCurrentSESs": pmDchCurrentSESs,
       "pmDchCurrentBBEs": pmDchCurrentBBEs,
       "pmDchCurrentUASs": pmDchCurrentUASs,
       "pmDch15mTable": pmDch15mTable,
       "pmDch15mEntry": pmDch15mEntry,
       "pmDch15mIndex": pmDch15mIndex,
       "pmDch15mTime": pmDch15mTime,
       "pmDch15mSuspect": pmDch15mSuspect,
       "pmDch15mZS": pmDch15mZS,
       "pmDch15mESs": pmDch15mESs,
       "pmDch15mSESs": pmDch15mSESs,
       "pmDch15mBBEs": pmDch15mBBEs,
       "pmDch15mUASs": pmDch15mUASs,
       "pmDch24hTable": pmDch24hTable,
       "pmDch24hEntry": pmDch24hEntry,
       "pmDch24hIndex": pmDch24hIndex,
       "pmDch24hTime": pmDch24hTime,
       "pmDch24hSuspect": pmDch24hSuspect,
       "pmDch24hZS": pmDch24hZS,
       "pmDch24hESs": pmDch24hESs,
       "pmDch24hSESs": pmDch24hSESs,
       "pmDch24hBBEs": pmDch24hBBEs,
       "pmDch24hUASs": pmDch24hUASs,
       "pmDch24hCurrentTable": pmDch24hCurrentTable,
       "pmDch24hCurrentEntry": pmDch24hCurrentEntry,
       "pmDch24hCurrentTime": pmDch24hCurrentTime,
       "pmDch24hCurrentSuspect": pmDch24hCurrentSuspect,
       "pmDch24hCurrentZS": pmDch24hCurrentZS,
       "pmDch24hCurrentESs": pmDch24hCurrentESs,
       "pmDch24hCurrentSESs": pmDch24hCurrentSESs,
       "pmDch24hCurrentBBEs": pmDch24hCurrentBBEs,
       "pmDch24hCurrentUASs": pmDch24hCurrentUASs,
       "pmConformanceGroups": pmConformanceGroups,
       "pmTifConformanceGroup": pmTifConformanceGroup,
       "pmAifConformanceGroup": pmAifConformanceGroup,
       "pmDchConformanceGroup": pmDchConformanceGroup}
)
