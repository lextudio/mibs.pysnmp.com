# SNMP MIB module (WINS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WINS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:13:59 2024
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

(microsoft,
 software) = mibBuilder.importSymbols(
    "MSFT-MIB",
    "microsoft",
    "software")

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
 enterprises,
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
    "enterprises",
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

_Wins_ObjectIdentity = ObjectIdentity
wins = _Wins_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 311, 1, 2)
)
_Par_ObjectIdentity = ObjectIdentity
par = _Par_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 311, 1, 2, 1)
)


class _ParWinsStartTime_Type(DisplayString):
    """Custom type parWinsStartTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 30),
    )


_ParWinsStartTime_Type.__name__ = "DisplayString"
_ParWinsStartTime_Object = MibScalar
parWinsStartTime = _ParWinsStartTime_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 2, 1, 1),
    _ParWinsStartTime_Type()
)
parWinsStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parWinsStartTime.setStatus("mandatory")


class _ParLastPScvTime_Type(DisplayString):
    """Custom type parLastPScvTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 30),
    )


_ParLastPScvTime_Type.__name__ = "DisplayString"
_ParLastPScvTime_Object = MibScalar
parLastPScvTime = _ParLastPScvTime_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 2, 1, 2),
    _ParLastPScvTime_Type()
)
parLastPScvTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parLastPScvTime.setStatus("mandatory")


class _ParLastATScvTime_Type(DisplayString):
    """Custom type parLastATScvTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 30),
    )


_ParLastATScvTime_Type.__name__ = "DisplayString"
_ParLastATScvTime_Object = MibScalar
parLastATScvTime = _ParLastATScvTime_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 2, 1, 3),
    _ParLastATScvTime_Type()
)
parLastATScvTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parLastATScvTime.setStatus("mandatory")


class _ParLastTombScvTime_Type(DisplayString):
    """Custom type parLastTombScvTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 30),
    )


_ParLastTombScvTime_Type.__name__ = "DisplayString"
_ParLastTombScvTime_Object = MibScalar
parLastTombScvTime = _ParLastTombScvTime_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 2, 1, 4),
    _ParLastTombScvTime_Type()
)
parLastTombScvTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parLastTombScvTime.setStatus("mandatory")


class _ParLastVerifyScvTime_Type(DisplayString):
    """Custom type parLastVerifyScvTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 30),
    )


_ParLastVerifyScvTime_Type.__name__ = "DisplayString"
_ParLastVerifyScvTime_Object = MibScalar
parLastVerifyScvTime = _ParLastVerifyScvTime_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 2, 1, 5),
    _ParLastVerifyScvTime_Type()
)
parLastVerifyScvTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parLastVerifyScvTime.setStatus("mandatory")


class _ParLastPRplTime_Type(DisplayString):
    """Custom type parLastPRplTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 30),
    )


_ParLastPRplTime_Type.__name__ = "DisplayString"
_ParLastPRplTime_Object = MibScalar
parLastPRplTime = _ParLastPRplTime_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 2, 1, 6),
    _ParLastPRplTime_Type()
)
parLastPRplTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parLastPRplTime.setStatus("mandatory")


class _ParLastATRplTime_Type(DisplayString):
    """Custom type parLastATRplTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 30),
    )


_ParLastATRplTime_Type.__name__ = "DisplayString"
_ParLastATRplTime_Object = MibScalar
parLastATRplTime = _ParLastATRplTime_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 2, 1, 7),
    _ParLastATRplTime_Type()
)
parLastATRplTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parLastATRplTime.setStatus("mandatory")


class _ParLastNTRplTime_Type(DisplayString):
    """Custom type parLastNTRplTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 30),
    )


_ParLastNTRplTime_Type.__name__ = "DisplayString"
_ParLastNTRplTime_Object = MibScalar
parLastNTRplTime = _ParLastNTRplTime_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 2, 1, 8),
    _ParLastNTRplTime_Type()
)
parLastNTRplTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parLastNTRplTime.setStatus("mandatory")


class _ParLastACTRplTime_Type(DisplayString):
    """Custom type parLastACTRplTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 30),
    )


_ParLastACTRplTime_Type.__name__ = "DisplayString"
_ParLastACTRplTime_Object = MibScalar
parLastACTRplTime = _ParLastACTRplTime_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 2, 1, 9),
    _ParLastACTRplTime_Type()
)
parLastACTRplTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parLastACTRplTime.setStatus("mandatory")


class _ParLastInitDbTime_Type(DisplayString):
    """Custom type parLastInitDbTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 30),
    )


_ParLastInitDbTime_Type.__name__ = "DisplayString"
_ParLastInitDbTime_Object = MibScalar
parLastInitDbTime = _ParLastInitDbTime_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 2, 1, 10),
    _ParLastInitDbTime_Type()
)
parLastInitDbTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parLastInitDbTime.setStatus("mandatory")


class _ParLastCounterResetTime_Type(DisplayString):
    """Custom type parLastCounterResetTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 30),
    )


_ParLastCounterResetTime_Type.__name__ = "DisplayString"
_ParLastCounterResetTime_Object = MibScalar
parLastCounterResetTime = _ParLastCounterResetTime_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 2, 1, 11),
    _ParLastCounterResetTime_Type()
)
parLastCounterResetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parLastCounterResetTime.setStatus("mandatory")
_ParWinsTotalNoOfReg_Type = Counter32
_ParWinsTotalNoOfReg_Object = MibScalar
parWinsTotalNoOfReg = _ParWinsTotalNoOfReg_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 2, 1, 12),
    _ParWinsTotalNoOfReg_Type()
)
parWinsTotalNoOfReg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parWinsTotalNoOfReg.setStatus("mandatory")
_ParWinsTotalNoOfQueries_Type = Counter32
_ParWinsTotalNoOfQueries_Object = MibScalar
parWinsTotalNoOfQueries = _ParWinsTotalNoOfQueries_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 2, 1, 13),
    _ParWinsTotalNoOfQueries_Type()
)
parWinsTotalNoOfQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parWinsTotalNoOfQueries.setStatus("mandatory")
_ParWinsTotalNoOfRel_Type = Counter32
_ParWinsTotalNoOfRel_Object = MibScalar
parWinsTotalNoOfRel = _ParWinsTotalNoOfRel_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 2, 1, 14),
    _ParWinsTotalNoOfRel_Type()
)
parWinsTotalNoOfRel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parWinsTotalNoOfRel.setStatus("mandatory")
_ParWinsTotalNoOfSuccRel_Type = Counter32
_ParWinsTotalNoOfSuccRel_Object = MibScalar
parWinsTotalNoOfSuccRel = _ParWinsTotalNoOfSuccRel_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 2, 1, 15),
    _ParWinsTotalNoOfSuccRel_Type()
)
parWinsTotalNoOfSuccRel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parWinsTotalNoOfSuccRel.setStatus("mandatory")
_ParWinsTotalNoOfFailRel_Type = Counter32
_ParWinsTotalNoOfFailRel_Object = MibScalar
parWinsTotalNoOfFailRel = _ParWinsTotalNoOfFailRel_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 2, 1, 16),
    _ParWinsTotalNoOfFailRel_Type()
)
parWinsTotalNoOfFailRel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parWinsTotalNoOfFailRel.setStatus("mandatory")
_ParWinsTotalNoOfSuccQueries_Type = Counter32
_ParWinsTotalNoOfSuccQueries_Object = MibScalar
parWinsTotalNoOfSuccQueries = _ParWinsTotalNoOfSuccQueries_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 2, 1, 17),
    _ParWinsTotalNoOfSuccQueries_Type()
)
parWinsTotalNoOfSuccQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parWinsTotalNoOfSuccQueries.setStatus("mandatory")
_ParWinsTotalNoOfFailQueries_Type = Counter32
_ParWinsTotalNoOfFailQueries_Object = MibScalar
parWinsTotalNoOfFailQueries = _ParWinsTotalNoOfFailQueries_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 2, 1, 18),
    _ParWinsTotalNoOfFailQueries_Type()
)
parWinsTotalNoOfFailQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parWinsTotalNoOfFailQueries.setStatus("mandatory")
_ParRefreshInterval_Type = Integer32
_ParRefreshInterval_Object = MibScalar
parRefreshInterval = _ParRefreshInterval_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 2, 1, 19),
    _ParRefreshInterval_Type()
)
parRefreshInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    parRefreshInterval.setStatus("mandatory")
_ParTombstoneInterval_Type = Integer32
_ParTombstoneInterval_Object = MibScalar
parTombstoneInterval = _ParTombstoneInterval_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 2, 1, 20),
    _ParTombstoneInterval_Type()
)
parTombstoneInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    parTombstoneInterval.setStatus("mandatory")
_ParTombstoneTimeout_Type = Integer32
_ParTombstoneTimeout_Object = MibScalar
parTombstoneTimeout = _ParTombstoneTimeout_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 2, 1, 21),
    _ParTombstoneTimeout_Type()
)
parTombstoneTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    parTombstoneTimeout.setStatus("mandatory")
_ParVerifyInterval_Type = Integer32
_ParVerifyInterval_Object = MibScalar
parVerifyInterval = _ParVerifyInterval_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 2, 1, 22),
    _ParVerifyInterval_Type()
)
parVerifyInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    parVerifyInterval.setStatus("mandatory")
_ParVersCounterStartValLowWord_Type = Counter32
_ParVersCounterStartValLowWord_Object = MibScalar
parVersCounterStartValLowWord = _ParVersCounterStartValLowWord_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 2, 1, 23),
    _ParVersCounterStartValLowWord_Type()
)
parVersCounterStartValLowWord.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    parVersCounterStartValLowWord.setStatus("mandatory")
_ParVersCounterStartValHighWord_Type = Counter32
_ParVersCounterStartValHighWord_Object = MibScalar
parVersCounterStartValHighWord = _ParVersCounterStartValHighWord_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 2, 1, 24),
    _ParVersCounterStartValHighWord_Type()
)
parVersCounterStartValHighWord.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    parVersCounterStartValHighWord.setStatus("mandatory")
_ParRplOnlyWCnfPnrs_Type = Integer32
_ParRplOnlyWCnfPnrs_Object = MibScalar
parRplOnlyWCnfPnrs = _ParRplOnlyWCnfPnrs_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 2, 1, 25),
    _ParRplOnlyWCnfPnrs_Type()
)
parRplOnlyWCnfPnrs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    parRplOnlyWCnfPnrs.setStatus("mandatory")
_ParStaticDataInit_Type = Integer32
_ParStaticDataInit_Object = MibScalar
parStaticDataInit = _ParStaticDataInit_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 2, 1, 26),
    _ParStaticDataInit_Type()
)
parStaticDataInit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    parStaticDataInit.setStatus("mandatory")
_ParLogFlag_Type = Integer32
_ParLogFlag_Object = MibScalar
parLogFlag = _ParLogFlag_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 2, 1, 27),
    _ParLogFlag_Type()
)
parLogFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    parLogFlag.setStatus("mandatory")
_ParLogFileName_Type = DisplayString
_ParLogFileName_Object = MibScalar
parLogFileName = _ParLogFileName_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 2, 1, 28),
    _ParLogFileName_Type()
)
parLogFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    parLogFileName.setStatus("mandatory")
_ParBackupDirPath_Type = DisplayString
_ParBackupDirPath_Object = MibScalar
parBackupDirPath = _ParBackupDirPath_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 2, 1, 29),
    _ParBackupDirPath_Type()
)
parBackupDirPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    parBackupDirPath.setStatus("mandatory")


class _ParDoBackupOnTerm_Type(Integer32):
    """Custom type parDoBackupOnTerm based on Integer32"""
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


_ParDoBackupOnTerm_Type.__name__ = "Integer32"
_ParDoBackupOnTerm_Object = MibScalar
parDoBackupOnTerm = _ParDoBackupOnTerm_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 2, 1, 30),
    _ParDoBackupOnTerm_Type()
)
parDoBackupOnTerm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    parDoBackupOnTerm.setStatus("mandatory")


class _ParMigrateOn_Type(Integer32):
    """Custom type parMigrateOn based on Integer32"""
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


_ParMigrateOn_Type.__name__ = "Integer32"
_ParMigrateOn_Object = MibScalar
parMigrateOn = _ParMigrateOn_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 2, 1, 31),
    _ParMigrateOn_Type()
)
parMigrateOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    parMigrateOn.setStatus("mandatory")
_Pull_ObjectIdentity = ObjectIdentity
pull = _Pull_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 311, 1, 2, 2)
)
_PullInitTime_Type = Integer32
_PullInitTime_Object = MibScalar
pullInitTime = _PullInitTime_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 2, 2, 1),
    _PullInitTime_Type()
)
pullInitTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pullInitTime.setStatus("mandatory")
_PullCommRetryCount_Type = Integer32
_PullCommRetryCount_Object = MibScalar
pullCommRetryCount = _PullCommRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 2, 2, 2),
    _PullCommRetryCount_Type()
)
pullCommRetryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pullCommRetryCount.setStatus("mandatory")
_PullPnrTable_Object = MibTable
pullPnrTable = _PullPnrTable_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 2, 2, 3)
)
if mibBuilder.loadTexts:
    pullPnrTable.setStatus("mandatory")
_PPullPnrEntry_Object = MibTableRow
pPullPnrEntry = _PPullPnrEntry_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 2, 2, 3, 1)
)
pPullPnrEntry.setIndexNames(
    (0, "WINS-MIB", "pullPnrAdd"),
)
if mibBuilder.loadTexts:
    pPullPnrEntry.setStatus("mandatory")
_PullPnrAdd_Type = IpAddress
_PullPnrAdd_Object = MibTableColumn
pullPnrAdd = _PullPnrAdd_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 2, 2, 3, 1, 1),
    _PullPnrAdd_Type()
)
pullPnrAdd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pullPnrAdd.setStatus("mandatory")
_PullPnrSpTime_Type = DisplayString
_PullPnrSpTime_Object = MibTableColumn
pullPnrSpTime = _PullPnrSpTime_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 2, 2, 3, 1, 2),
    _PullPnrSpTime_Type()
)
pullPnrSpTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pullPnrSpTime.setStatus("mandatory")
_PullPnrTimeInterval_Type = Integer32
_PullPnrTimeInterval_Object = MibTableColumn
pullPnrTimeInterval = _PullPnrTimeInterval_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 2, 2, 3, 1, 3),
    _PullPnrTimeInterval_Type()
)
pullPnrTimeInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pullPnrTimeInterval.setStatus("mandatory")


class _PullPnrMemberPrec_Type(Integer32):
    """Custom type pullPnrMemberPrec based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("low", 0))
    )


_PullPnrMemberPrec_Type.__name__ = "Integer32"
_PullPnrMemberPrec_Object = MibTableColumn
pullPnrMemberPrec = _PullPnrMemberPrec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 2, 2, 3, 1, 4),
    _PullPnrMemberPrec_Type()
)
pullPnrMemberPrec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pullPnrMemberPrec.setStatus("mandatory")
_PullPnrNoOfSuccRpls_Type = Counter32
_PullPnrNoOfSuccRpls_Object = MibTableColumn
pullPnrNoOfSuccRpls = _PullPnrNoOfSuccRpls_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 2, 2, 3, 1, 5),
    _PullPnrNoOfSuccRpls_Type()
)
pullPnrNoOfSuccRpls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pullPnrNoOfSuccRpls.setStatus("mandatory")
_PullPnrNoOfCommFails_Type = Counter32
_PullPnrNoOfCommFails_Object = MibTableColumn
pullPnrNoOfCommFails = _PullPnrNoOfCommFails_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 2, 2, 3, 1, 6),
    _PullPnrNoOfCommFails_Type()
)
pullPnrNoOfCommFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pullPnrNoOfCommFails.setStatus("mandatory")
_PullPnrVersNoLowWord_Type = Counter32
_PullPnrVersNoLowWord_Object = MibTableColumn
pullPnrVersNoLowWord = _PullPnrVersNoLowWord_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 2, 2, 3, 1, 7),
    _PullPnrVersNoLowWord_Type()
)
pullPnrVersNoLowWord.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pullPnrVersNoLowWord.setStatus("mandatory")
_PullPnrVersNoHighWord_Type = Counter32
_PullPnrVersNoHighWord_Object = MibTableColumn
pullPnrVersNoHighWord = _PullPnrVersNoHighWord_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 2, 2, 3, 1, 8),
    _PullPnrVersNoHighWord_Type()
)
pullPnrVersNoHighWord.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pullPnrVersNoHighWord.setStatus("mandatory")
_Push_ObjectIdentity = ObjectIdentity
push = _Push_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 311, 1, 2, 3)
)
_PushInitTime_Type = Integer32
_PushInitTime_Object = MibScalar
pushInitTime = _PushInitTime_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 2, 3, 1),
    _PushInitTime_Type()
)
pushInitTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pushInitTime.setStatus("mandatory")
_PushRplOnAddChg_Type = Integer32
_PushRplOnAddChg_Object = MibScalar
pushRplOnAddChg = _PushRplOnAddChg_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 2, 3, 2),
    _PushRplOnAddChg_Type()
)
pushRplOnAddChg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pushRplOnAddChg.setStatus("mandatory")
_PushPnrTable_Object = MibTable
pushPnrTable = _PushPnrTable_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 2, 3, 3)
)
if mibBuilder.loadTexts:
    pushPnrTable.setStatus("mandatory")
_PushPnrEntry_Object = MibTableRow
pushPnrEntry = _PushPnrEntry_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 2, 3, 3, 1)
)
pushPnrEntry.setIndexNames(
    (0, "WINS-MIB", "pushPnrAdd"),
)
if mibBuilder.loadTexts:
    pushPnrEntry.setStatus("mandatory")
_PushPnrAdd_Type = IpAddress
_PushPnrAdd_Object = MibTableColumn
pushPnrAdd = _PushPnrAdd_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 2, 3, 3, 1, 1),
    _PushPnrAdd_Type()
)
pushPnrAdd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pushPnrAdd.setStatus("mandatory")
_PushPnrUpdateCount_Type = Integer32
_PushPnrUpdateCount_Object = MibTableColumn
pushPnrUpdateCount = _PushPnrUpdateCount_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 2, 3, 3, 1, 2),
    _PushPnrUpdateCount_Type()
)
pushPnrUpdateCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pushPnrUpdateCount.setStatus("mandatory")
_Datafiles_ObjectIdentity = ObjectIdentity
datafiles = _Datafiles_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 311, 1, 2, 4)
)
_DfDatafilesTable_Object = MibTable
dfDatafilesTable = _DfDatafilesTable_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 2, 4, 1)
)
if mibBuilder.loadTexts:
    dfDatafilesTable.setStatus("mandatory")
_DfDatafileEntry_Object = MibTableRow
dfDatafileEntry = _DfDatafileEntry_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 2, 4, 1, 1)
)
dfDatafileEntry.setIndexNames(
    (0, "WINS-MIB", "dfDatafileIndex"),
)
if mibBuilder.loadTexts:
    dfDatafileEntry.setStatus("mandatory")
_DfDatafileIndex_Type = Integer32
_DfDatafileIndex_Object = MibTableColumn
dfDatafileIndex = _DfDatafileIndex_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 2, 4, 1, 1, 1),
    _DfDatafileIndex_Type()
)
dfDatafileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfDatafileIndex.setStatus("mandatory")
_DfDatafileName_Type = DisplayString
_DfDatafileName_Object = MibTableColumn
dfDatafileName = _DfDatafileName_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 2, 4, 1, 1, 2),
    _DfDatafileName_Type()
)
dfDatafileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dfDatafileName.setStatus("mandatory")
_Cmd_ObjectIdentity = ObjectIdentity
cmd = _Cmd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 311, 1, 2, 5)
)
_CmdPullTrigger_Type = IpAddress
_CmdPullTrigger_Object = MibScalar
cmdPullTrigger = _CmdPullTrigger_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 2, 5, 1),
    _CmdPullTrigger_Type()
)
cmdPullTrigger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmdPullTrigger.setStatus("mandatory")
_CmdPushTrigger_Type = IpAddress
_CmdPushTrigger_Object = MibScalar
cmdPushTrigger = _CmdPushTrigger_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 2, 5, 2),
    _CmdPushTrigger_Type()
)
cmdPushTrigger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmdPushTrigger.setStatus("mandatory")
_CmdDeleteWins_Type = IpAddress
_CmdDeleteWins_Object = MibScalar
cmdDeleteWins = _CmdDeleteWins_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 2, 5, 3),
    _CmdDeleteWins_Type()
)
cmdDeleteWins.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmdDeleteWins.setStatus("mandatory")


class _CmdDoScavenging_Type(Integer32):
    """Custom type cmdDoScavenging based on Integer32"""
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


_CmdDoScavenging_Type.__name__ = "Integer32"
_CmdDoScavenging_Object = MibScalar
cmdDoScavenging = _CmdDoScavenging_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 2, 5, 4),
    _CmdDoScavenging_Type()
)
cmdDoScavenging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmdDoScavenging.setStatus("mandatory")
_CmdDoStaticInit_Type = DisplayString
_CmdDoStaticInit_Object = MibScalar
cmdDoStaticInit = _CmdDoStaticInit_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 2, 5, 5),
    _CmdDoStaticInit_Type()
)
cmdDoStaticInit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmdDoStaticInit.setStatus("mandatory")


class _CmdNoOfWrkThds_Type(Integer32):
    """Custom type cmdNoOfWrkThds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_CmdNoOfWrkThds_Type.__name__ = "Integer32"
_CmdNoOfWrkThds_Object = MibScalar
cmdNoOfWrkThds = _CmdNoOfWrkThds_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 2, 5, 6),
    _CmdNoOfWrkThds_Type()
)
cmdNoOfWrkThds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmdNoOfWrkThds.setStatus("mandatory")


class _CmdPriorityClass_Type(Integer32):
    """Custom type cmdPriorityClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("normal", 0))
    )


_CmdPriorityClass_Type.__name__ = "Integer32"
_CmdPriorityClass_Object = MibScalar
cmdPriorityClass = _CmdPriorityClass_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 2, 5, 7),
    _CmdPriorityClass_Type()
)
cmdPriorityClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmdPriorityClass.setStatus("mandatory")
_CmdResetCounters_Type = Integer32
_CmdResetCounters_Object = MibScalar
cmdResetCounters = _CmdResetCounters_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 2, 5, 8),
    _CmdResetCounters_Type()
)
cmdResetCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmdResetCounters.setStatus("mandatory")
_CmdDeleteDbRecs_Type = IpAddress
_CmdDeleteDbRecs_Object = MibScalar
cmdDeleteDbRecs = _CmdDeleteDbRecs_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 2, 5, 9),
    _CmdDeleteDbRecs_Type()
)
cmdDeleteDbRecs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmdDeleteDbRecs.setStatus("mandatory")
_CmdDRPopulateTable_Type = IpAddress
_CmdDRPopulateTable_Object = MibScalar
cmdDRPopulateTable = _CmdDRPopulateTable_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 2, 5, 10),
    _CmdDRPopulateTable_Type()
)
cmdDRPopulateTable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmdDRPopulateTable.setStatus("mandatory")
_CmdDRDataRecordsTable_Object = MibTable
cmdDRDataRecordsTable = _CmdDRDataRecordsTable_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 2, 5, 11)
)
if mibBuilder.loadTexts:
    cmdDRDataRecordsTable.setStatus("mandatory")
_CmdDRRecordEntry_Object = MibTableRow
cmdDRRecordEntry = _CmdDRRecordEntry_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 2, 5, 11, 1)
)
cmdDRRecordEntry.setIndexNames(
    (0, "WINS-MIB", "cmdDRRecordName"),
)
if mibBuilder.loadTexts:
    cmdDRRecordEntry.setStatus("mandatory")


class _CmdDRRecordName_Type(OctetString):
    """Custom type cmdDRRecordName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CmdDRRecordName_Type.__name__ = "OctetString"
_CmdDRRecordName_Object = MibTableColumn
cmdDRRecordName = _CmdDRRecordName_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 2, 5, 11, 1, 1),
    _CmdDRRecordName_Type()
)
cmdDRRecordName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmdDRRecordName.setStatus("mandatory")
_CmdDRRecordAddress_Type = OctetString
_CmdDRRecordAddress_Object = MibTableColumn
cmdDRRecordAddress = _CmdDRRecordAddress_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 2, 5, 11, 1, 2),
    _CmdDRRecordAddress_Type()
)
cmdDRRecordAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmdDRRecordAddress.setStatus("mandatory")


class _CmdDRRecordType_Type(Integer32):
    """Custom type cmdDRRecordType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("multihomed", 3),
          ("normalgroup", 1),
          ("specialgroup", 2),
          ("unique", 0))
    )


_CmdDRRecordType_Type.__name__ = "Integer32"
_CmdDRRecordType_Object = MibTableColumn
cmdDRRecordType = _CmdDRRecordType_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 2, 5, 11, 1, 3),
    _CmdDRRecordType_Type()
)
cmdDRRecordType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmdDRRecordType.setStatus("mandatory")


class _CmdDRRecordPersistenceType_Type(Integer32):
    """Custom type cmdDRRecordPersistenceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 1),
          ("static", 0))
    )


_CmdDRRecordPersistenceType_Type.__name__ = "Integer32"
_CmdDRRecordPersistenceType_Object = MibTableColumn
cmdDRRecordPersistenceType = _CmdDRRecordPersistenceType_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 2, 5, 11, 1, 4),
    _CmdDRRecordPersistenceType_Type()
)
cmdDRRecordPersistenceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmdDRRecordPersistenceType.setStatus("mandatory")


class _CmdDRRecordState_Type(Integer32):
    """Custom type cmdDRRecordState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 0),
          ("deleted", 3),
          ("released", 1),
          ("tombstone", 2))
    )


_CmdDRRecordState_Type.__name__ = "Integer32"
_CmdDRRecordState_Object = MibTableColumn
cmdDRRecordState = _CmdDRRecordState_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 2, 5, 11, 1, 5),
    _CmdDRRecordState_Type()
)
cmdDRRecordState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmdDRRecordState.setStatus("mandatory")
_CmdWinsVersNoLowWord_Type = Integer32
_CmdWinsVersNoLowWord_Object = MibScalar
cmdWinsVersNoLowWord = _CmdWinsVersNoLowWord_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 2, 5, 12),
    _CmdWinsVersNoLowWord_Type()
)
cmdWinsVersNoLowWord.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmdWinsVersNoLowWord.setStatus("mandatory")
_CmdWinsVersNoHighWord_Type = Integer32
_CmdWinsVersNoHighWord_Object = MibScalar
cmdWinsVersNoHighWord = _CmdWinsVersNoHighWord_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 2, 5, 13),
    _CmdWinsVersNoHighWord_Type()
)
cmdWinsVersNoHighWord.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmdWinsVersNoHighWord.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WINS-MIB",
    **{"wins": wins,
       "par": par,
       "parWinsStartTime": parWinsStartTime,
       "parLastPScvTime": parLastPScvTime,
       "parLastATScvTime": parLastATScvTime,
       "parLastTombScvTime": parLastTombScvTime,
       "parLastVerifyScvTime": parLastVerifyScvTime,
       "parLastPRplTime": parLastPRplTime,
       "parLastATRplTime": parLastATRplTime,
       "parLastNTRplTime": parLastNTRplTime,
       "parLastACTRplTime": parLastACTRplTime,
       "parLastInitDbTime": parLastInitDbTime,
       "parLastCounterResetTime": parLastCounterResetTime,
       "parWinsTotalNoOfReg": parWinsTotalNoOfReg,
       "parWinsTotalNoOfQueries": parWinsTotalNoOfQueries,
       "parWinsTotalNoOfRel": parWinsTotalNoOfRel,
       "parWinsTotalNoOfSuccRel": parWinsTotalNoOfSuccRel,
       "parWinsTotalNoOfFailRel": parWinsTotalNoOfFailRel,
       "parWinsTotalNoOfSuccQueries": parWinsTotalNoOfSuccQueries,
       "parWinsTotalNoOfFailQueries": parWinsTotalNoOfFailQueries,
       "parRefreshInterval": parRefreshInterval,
       "parTombstoneInterval": parTombstoneInterval,
       "parTombstoneTimeout": parTombstoneTimeout,
       "parVerifyInterval": parVerifyInterval,
       "parVersCounterStartValLowWord": parVersCounterStartValLowWord,
       "parVersCounterStartValHighWord": parVersCounterStartValHighWord,
       "parRplOnlyWCnfPnrs": parRplOnlyWCnfPnrs,
       "parStaticDataInit": parStaticDataInit,
       "parLogFlag": parLogFlag,
       "parLogFileName": parLogFileName,
       "parBackupDirPath": parBackupDirPath,
       "parDoBackupOnTerm": parDoBackupOnTerm,
       "parMigrateOn": parMigrateOn,
       "pull": pull,
       "pullInitTime": pullInitTime,
       "pullCommRetryCount": pullCommRetryCount,
       "pullPnrTable": pullPnrTable,
       "pPullPnrEntry": pPullPnrEntry,
       "pullPnrAdd": pullPnrAdd,
       "pullPnrSpTime": pullPnrSpTime,
       "pullPnrTimeInterval": pullPnrTimeInterval,
       "pullPnrMemberPrec": pullPnrMemberPrec,
       "pullPnrNoOfSuccRpls": pullPnrNoOfSuccRpls,
       "pullPnrNoOfCommFails": pullPnrNoOfCommFails,
       "pullPnrVersNoLowWord": pullPnrVersNoLowWord,
       "pullPnrVersNoHighWord": pullPnrVersNoHighWord,
       "push": push,
       "pushInitTime": pushInitTime,
       "pushRplOnAddChg": pushRplOnAddChg,
       "pushPnrTable": pushPnrTable,
       "pushPnrEntry": pushPnrEntry,
       "pushPnrAdd": pushPnrAdd,
       "pushPnrUpdateCount": pushPnrUpdateCount,
       "datafiles": datafiles,
       "dfDatafilesTable": dfDatafilesTable,
       "dfDatafileEntry": dfDatafileEntry,
       "dfDatafileIndex": dfDatafileIndex,
       "dfDatafileName": dfDatafileName,
       "cmd": cmd,
       "cmdPullTrigger": cmdPullTrigger,
       "cmdPushTrigger": cmdPushTrigger,
       "cmdDeleteWins": cmdDeleteWins,
       "cmdDoScavenging": cmdDoScavenging,
       "cmdDoStaticInit": cmdDoStaticInit,
       "cmdNoOfWrkThds": cmdNoOfWrkThds,
       "cmdPriorityClass": cmdPriorityClass,
       "cmdResetCounters": cmdResetCounters,
       "cmdDeleteDbRecs": cmdDeleteDbRecs,
       "cmdDRPopulateTable": cmdDRPopulateTable,
       "cmdDRDataRecordsTable": cmdDRDataRecordsTable,
       "cmdDRRecordEntry": cmdDRRecordEntry,
       "cmdDRRecordName": cmdDRRecordName,
       "cmdDRRecordAddress": cmdDRRecordAddress,
       "cmdDRRecordType": cmdDRRecordType,
       "cmdDRRecordPersistenceType": cmdDRRecordPersistenceType,
       "cmdDRRecordState": cmdDRRecordState,
       "cmdWinsVersNoLowWord": cmdWinsVersNoLowWord,
       "cmdWinsVersNoHighWord": cmdWinsVersNoHighWord}
)
