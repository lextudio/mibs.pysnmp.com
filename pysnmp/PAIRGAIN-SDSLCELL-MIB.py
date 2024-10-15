# SNMP MIB module (PAIRGAIN-SDSLCELL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PAIRGAIN-SDSLCELL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:36:25 2024
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

(pgainSDSLCell,) = mibBuilder.importSymbols(
    "PAIRGAIN-COMMON-HD-MIB",
    "pgainSDSLCell")

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

pgsdslCellMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 927, 1, 14, 1)
)


# Types definitions



class PgSdslcellLineProfileType(Integer32):
    """Custom type PgSdslcellLineProfileType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )





class PgSdslcellAlarmProfileType(Integer32):
    """Custom type PgSdslcellAlarmProfileType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PgsdslCellMibObjects_ObjectIdentity = ObjectIdentity
pgsdslCellMibObjects = _PgsdslCellMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 1)
)
_PgSdslCellLineTable_Object = MibTable
pgSdslCellLineTable = _PgSdslCellLineTable_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 1, 1)
)
if mibBuilder.loadTexts:
    pgSdslCellLineTable.setStatus("current")
_PgSdslCellLineEntry_Object = MibTableRow
pgSdslCellLineEntry = _PgSdslCellLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 1, 1, 1)
)
pgSdslCellLineEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    pgSdslCellLineEntry.setStatus("current")
_PgSdslCellLineProfile_Type = PgSdslcellLineProfileType
_PgSdslCellLineProfile_Object = MibTableColumn
pgSdslCellLineProfile = _PgSdslCellLineProfile_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 1, 1, 1, 1),
    _PgSdslCellLineProfile_Type()
)
pgSdslCellLineProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgSdslCellLineProfile.setStatus("current")
_PgSdslCellAlarmProfile_Type = PgSdslcellAlarmProfileType
_PgSdslCellAlarmProfile_Object = MibTableColumn
pgSdslCellAlarmProfile = _PgSdslCellAlarmProfile_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 1, 1, 1, 2),
    _PgSdslCellAlarmProfile_Type()
)
pgSdslCellAlarmProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgSdslCellAlarmProfile.setStatus("current")
_PgSdslCellPhysTable_Object = MibTable
pgSdslCellPhysTable = _PgSdslCellPhysTable_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 1, 2)
)
if mibBuilder.loadTexts:
    pgSdslCellPhysTable.setStatus("current")
_PgSdslCellPhysEntry_Object = MibTableRow
pgSdslCellPhysEntry = _PgSdslCellPhysEntry_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 1, 2, 1)
)
pgSdslCellPhysEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    pgSdslCellPhysEntry.setStatus("current")


class _PgSdslCellInvSerialNumber_Type(DisplayString):
    """Custom type pgSdslCellInvSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PgSdslCellInvSerialNumber_Type.__name__ = "DisplayString"
_PgSdslCellInvSerialNumber_Object = MibTableColumn
pgSdslCellInvSerialNumber = _PgSdslCellInvSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 1, 2, 1, 1),
    _PgSdslCellInvSerialNumber_Type()
)
pgSdslCellInvSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgSdslCellInvSerialNumber.setStatus("current")
_PgSdslCellInvVendorID_Type = Integer32
_PgSdslCellInvVendorID_Object = MibTableColumn
pgSdslCellInvVendorID = _PgSdslCellInvVendorID_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 1, 2, 1, 2),
    _PgSdslCellInvVendorID_Type()
)
pgSdslCellInvVendorID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgSdslCellInvVendorID.setStatus("current")
_PgSdslCellInvVersionNumber_Type = Integer32
_PgSdslCellInvVersionNumber_Object = MibTableColumn
pgSdslCellInvVersionNumber = _PgSdslCellInvVersionNumber_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 1, 2, 1, 3),
    _PgSdslCellInvVersionNumber_Type()
)
pgSdslCellInvVersionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgSdslCellInvVersionNumber.setStatus("current")


class _PgSdslCellCurrSnrMgn_Type(Integer32):
    """Custom type pgSdslCellCurrSnrMgn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 310),
    )


_PgSdslCellCurrSnrMgn_Type.__name__ = "Integer32"
_PgSdslCellCurrSnrMgn_Object = MibTableColumn
pgSdslCellCurrSnrMgn = _PgSdslCellCurrSnrMgn_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 1, 2, 1, 4),
    _PgSdslCellCurrSnrMgn_Type()
)
pgSdslCellCurrSnrMgn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgSdslCellCurrSnrMgn.setStatus("current")
if mibBuilder.loadTexts:
    pgSdslCellCurrSnrMgn.setUnits("tenth dB")


class _PgSdslCellCurrAtn_Type(Integer32):
    """Custom type pgSdslCellCurrAtn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 630),
    )


_PgSdslCellCurrAtn_Type.__name__ = "Integer32"
_PgSdslCellCurrAtn_Object = MibTableColumn
pgSdslCellCurrAtn = _PgSdslCellCurrAtn_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 1, 2, 1, 5),
    _PgSdslCellCurrAtn_Type()
)
pgSdslCellCurrAtn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgSdslCellCurrAtn.setStatus("current")
if mibBuilder.loadTexts:
    pgSdslCellCurrAtn.setUnits("tenth dB")


class _PgSdslCellCurrStatus_Type(Integer32):
    """Custom type pgSdslCellCurrStatus based on Integer32"""
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
        *(("down", 2),
          ("fail", 5),
          ("hand", 3),
          ("test", 4),
          ("up", 1))
    )


_PgSdslCellCurrStatus_Type.__name__ = "Integer32"
_PgSdslCellCurrStatus_Object = MibTableColumn
pgSdslCellCurrStatus = _PgSdslCellCurrStatus_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 1, 2, 1, 6),
    _PgSdslCellCurrStatus_Type()
)
pgSdslCellCurrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgSdslCellCurrStatus.setStatus("current")


class _PgSdslCellLineProfileIndexNext_Type(Integer32):
    """Custom type pgSdslCellLineProfileIndexNext based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PgSdslCellLineProfileIndexNext_Type.__name__ = "Integer32"
_PgSdslCellLineProfileIndexNext_Object = MibScalar
pgSdslCellLineProfileIndexNext = _PgSdslCellLineProfileIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 1, 3),
    _PgSdslCellLineProfileIndexNext_Type()
)
pgSdslCellLineProfileIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgSdslCellLineProfileIndexNext.setStatus("current")
_PgSdslCellLineProfileTable_Object = MibTable
pgSdslCellLineProfileTable = _PgSdslCellLineProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 1, 4)
)
if mibBuilder.loadTexts:
    pgSdslCellLineProfileTable.setStatus("current")
_PgSdslCellLineProfileEntry_Object = MibTableRow
pgSdslCellLineProfileEntry = _PgSdslCellLineProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 1, 4, 1)
)
pgSdslCellLineProfileEntry.setIndexNames(
    (0, "PAIRGAIN-SDSLCELL-MIB", "pgSdslCellLineProfileIndex"),
)
if mibBuilder.loadTexts:
    pgSdslCellLineProfileEntry.setStatus("current")
_PgSdslCellLineProfileIndex_Type = PgSdslcellLineProfileType
_PgSdslCellLineProfileIndex_Object = MibTableColumn
pgSdslCellLineProfileIndex = _PgSdslCellLineProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 1, 4, 1, 1),
    _PgSdslCellLineProfileIndex_Type()
)
pgSdslCellLineProfileIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgSdslCellLineProfileIndex.setStatus("current")
_PgSdslCellLineProfileRowStatus_Type = RowStatus
_PgSdslCellLineProfileRowStatus_Object = MibTableColumn
pgSdslCellLineProfileRowStatus = _PgSdslCellLineProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 1, 4, 1, 2),
    _PgSdslCellLineProfileRowStatus_Type()
)
pgSdslCellLineProfileRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgSdslCellLineProfileRowStatus.setStatus("current")


class _PgSdslCellLineCode_Type(Integer32):
    """Custom type pgSdslCellLineCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("twoB1Q", 2))
    )


_PgSdslCellLineCode_Type.__name__ = "Integer32"
_PgSdslCellLineCode_Object = MibTableColumn
pgSdslCellLineCode = _PgSdslCellLineCode_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 1, 4, 1, 3),
    _PgSdslCellLineCode_Type()
)
pgSdslCellLineCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgSdslCellLineCode.setStatus("current")


class _PgSdslCellLineRateMode_Type(Integer32):
    """Custom type pgSdslCellLineRateMode based on Integer32"""
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
        *(("autoBaud", 2),
          ("autoConex", 3),
          ("fixed", 4),
          ("other", 1))
    )


_PgSdslCellLineRateMode_Type.__name__ = "Integer32"
_PgSdslCellLineRateMode_Object = MibTableColumn
pgSdslCellLineRateMode = _PgSdslCellLineRateMode_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 1, 4, 1, 4),
    _PgSdslCellLineRateMode_Type()
)
pgSdslCellLineRateMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgSdslCellLineRateMode.setStatus("current")


class _PgSdslCellLineRate_Type(Integer32):
    """Custom type pgSdslCellLineRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 2320),
    )


_PgSdslCellLineRate_Type.__name__ = "Integer32"
_PgSdslCellLineRate_Object = MibTableColumn
pgSdslCellLineRate = _PgSdslCellLineRate_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 1, 4, 1, 5),
    _PgSdslCellLineRate_Type()
)
pgSdslCellLineRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgSdslCellLineRate.setStatus("current")
if mibBuilder.loadTexts:
    pgSdslCellLineRate.setUnits("kbps")


class _PgSdslCellLineTermType_Type(Integer32):
    """Custom type pgSdslCellLineTermType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("co", 1),
          ("rt", 2))
    )


_PgSdslCellLineTermType_Type.__name__ = "Integer32"
_PgSdslCellLineTermType_Object = MibTableColumn
pgSdslCellLineTermType = _PgSdslCellLineTermType_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 1, 4, 1, 6),
    _PgSdslCellLineTermType_Type()
)
pgSdslCellLineTermType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgSdslCellLineTermType.setStatus("current")


class _PgSdslCellLineProfileInUse_Type(Integer32):
    """Custom type pgSdslCellLineProfileInUse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inuse", 2),
          ("notused", 1))
    )


_PgSdslCellLineProfileInUse_Type.__name__ = "Integer32"
_PgSdslCellLineProfileInUse_Object = MibTableColumn
pgSdslCellLineProfileInUse = _PgSdslCellLineProfileInUse_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 1, 4, 1, 7),
    _PgSdslCellLineProfileInUse_Type()
)
pgSdslCellLineProfileInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgSdslCellLineProfileInUse.setStatus("current")


class _PgSdslCellAlarmProfileIndexNext_Type(Integer32):
    """Custom type pgSdslCellAlarmProfileIndexNext based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PgSdslCellAlarmProfileIndexNext_Type.__name__ = "Integer32"
_PgSdslCellAlarmProfileIndexNext_Object = MibScalar
pgSdslCellAlarmProfileIndexNext = _PgSdslCellAlarmProfileIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 1, 5),
    _PgSdslCellAlarmProfileIndexNext_Type()
)
pgSdslCellAlarmProfileIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgSdslCellAlarmProfileIndexNext.setStatus("current")
_PgSdslCellAlarmProfileTable_Object = MibTable
pgSdslCellAlarmProfileTable = _PgSdslCellAlarmProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 1, 6)
)
if mibBuilder.loadTexts:
    pgSdslCellAlarmProfileTable.setStatus("current")
_PgSdslCellAlarmProfileEntry_Object = MibTableRow
pgSdslCellAlarmProfileEntry = _PgSdslCellAlarmProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 1, 6, 1)
)
pgSdslCellAlarmProfileEntry.setIndexNames(
    (0, "PAIRGAIN-SDSLCELL-MIB", "pgSdslCellAlarmProfileIndex"),
)
if mibBuilder.loadTexts:
    pgSdslCellAlarmProfileEntry.setStatus("current")
_PgSdslCellAlarmProfileIndex_Type = PgSdslcellAlarmProfileType
_PgSdslCellAlarmProfileIndex_Object = MibTableColumn
pgSdslCellAlarmProfileIndex = _PgSdslCellAlarmProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 1, 6, 1, 1),
    _PgSdslCellAlarmProfileIndex_Type()
)
pgSdslCellAlarmProfileIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgSdslCellAlarmProfileIndex.setStatus("current")
_PgSdslCellAlarmProfileRowStatus_Type = RowStatus
_PgSdslCellAlarmProfileRowStatus_Object = MibTableColumn
pgSdslCellAlarmProfileRowStatus = _PgSdslCellAlarmProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 1, 6, 1, 2),
    _PgSdslCellAlarmProfileRowStatus_Type()
)
pgSdslCellAlarmProfileRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgSdslCellAlarmProfileRowStatus.setStatus("current")


class _PgSdslCellThresh15MinLOSS_Type(Integer32):
    """Custom type pgSdslCellThresh15MinLOSS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_PgSdslCellThresh15MinLOSS_Type.__name__ = "Integer32"
_PgSdslCellThresh15MinLOSS_Object = MibTableColumn
pgSdslCellThresh15MinLOSS = _PgSdslCellThresh15MinLOSS_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 1, 6, 1, 3),
    _PgSdslCellThresh15MinLOSS_Type()
)
pgSdslCellThresh15MinLOSS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgSdslCellThresh15MinLOSS.setStatus("current")
_PgSdslCellThresh15MinLOCD_Type = Integer32
_PgSdslCellThresh15MinLOCD_Object = MibTableColumn
pgSdslCellThresh15MinLOCD = _PgSdslCellThresh15MinLOCD_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 1, 6, 1, 4),
    _PgSdslCellThresh15MinLOCD_Type()
)
pgSdslCellThresh15MinLOCD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgSdslCellThresh15MinLOCD.setStatus("current")
_PgSdslCellThresh15MinSLOCD_Type = Integer32
_PgSdslCellThresh15MinSLOCD_Object = MibTableColumn
pgSdslCellThresh15MinSLOCD = _PgSdslCellThresh15MinSLOCD_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 1, 6, 1, 5),
    _PgSdslCellThresh15MinSLOCD_Type()
)
pgSdslCellThresh15MinSLOCD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgSdslCellThresh15MinSLOCD.setStatus("current")
_PgSdslCellThreshSNR_Type = Integer32
_PgSdslCellThreshSNR_Object = MibTableColumn
pgSdslCellThreshSNR = _PgSdslCellThreshSNR_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 1, 6, 1, 6),
    _PgSdslCellThreshSNR_Type()
)
pgSdslCellThreshSNR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgSdslCellThreshSNR.setStatus("current")


class _PgSdslCellAlarmProfileInUse_Type(Integer32):
    """Custom type pgSdslCellAlarmProfileInUse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inuse", 2),
          ("notused", 1))
    )


_PgSdslCellAlarmProfileInUse_Type.__name__ = "Integer32"
_PgSdslCellAlarmProfileInUse_Object = MibTableColumn
pgSdslCellAlarmProfileInUse = _PgSdslCellAlarmProfileInUse_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 1, 6, 1, 7),
    _PgSdslCellAlarmProfileInUse_Type()
)
pgSdslCellAlarmProfileInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgSdslCellAlarmProfileInUse.setStatus("current")
_PgSdslCellPerfCurrTable_Object = MibTable
pgSdslCellPerfCurrTable = _PgSdslCellPerfCurrTable_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 1, 7)
)
if mibBuilder.loadTexts:
    pgSdslCellPerfCurrTable.setStatus("current")
_PgSdslCellPerfCurrEntry_Object = MibTableRow
pgSdslCellPerfCurrEntry = _PgSdslCellPerfCurrEntry_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 1, 7, 1)
)
pgSdslCellPerfCurrEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    pgSdslCellPerfCurrEntry.setStatus("current")
_PgSdslCellPerfCurrLOSS_Type = Counter32
_PgSdslCellPerfCurrLOSS_Object = MibTableColumn
pgSdslCellPerfCurrLOSS = _PgSdslCellPerfCurrLOSS_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 1, 7, 1, 1),
    _PgSdslCellPerfCurrLOSS_Type()
)
pgSdslCellPerfCurrLOSS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgSdslCellPerfCurrLOSS.setStatus("current")
_PgSdslCellPerfCurrLOCD_Type = Counter32
_PgSdslCellPerfCurrLOCD_Object = MibTableColumn
pgSdslCellPerfCurrLOCD = _PgSdslCellPerfCurrLOCD_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 1, 7, 1, 2),
    _PgSdslCellPerfCurrLOCD_Type()
)
pgSdslCellPerfCurrLOCD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgSdslCellPerfCurrLOCD.setStatus("current")
_PgSdslCellPerfCurrSLOCD_Type = Counter32
_PgSdslCellPerfCurrSLOCD_Object = MibTableColumn
pgSdslCellPerfCurrSLOCD = _PgSdslCellPerfCurrSLOCD_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 1, 7, 1, 3),
    _PgSdslCellPerfCurrSLOCD_Type()
)
pgSdslCellPerfCurrSLOCD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgSdslCellPerfCurrSLOCD.setStatus("current")


class _PgSdslCellClearStats_Type(Integer32):
    """Custom type pgSdslCellClearStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear", 1)
    )


_PgSdslCellClearStats_Type.__name__ = "Integer32"
_PgSdslCellClearStats_Object = MibTableColumn
pgSdslCellClearStats = _PgSdslCellClearStats_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 1, 7, 1, 4),
    _PgSdslCellClearStats_Type()
)
pgSdslCellClearStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgSdslCellClearStats.setStatus("current")
_PgSdslCellStatsLastCleared_Type = TimeStamp
_PgSdslCellStatsLastCleared_Object = MibTableColumn
pgSdslCellStatsLastCleared = _PgSdslCellStatsLastCleared_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 1, 7, 1, 5),
    _PgSdslCellStatsLastCleared_Type()
)
pgSdslCellStatsLastCleared.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgSdslCellStatsLastCleared.setStatus("current")
_PgSdslCellPerfCurr15MinTable_Object = MibTable
pgSdslCellPerfCurr15MinTable = _PgSdslCellPerfCurr15MinTable_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 1, 8)
)
if mibBuilder.loadTexts:
    pgSdslCellPerfCurr15MinTable.setStatus("current")
_PgSdslCellPerfCurr15MinEntry_Object = MibTableRow
pgSdslCellPerfCurr15MinEntry = _PgSdslCellPerfCurr15MinEntry_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 1, 8, 1)
)
pgSdslCellPerfCurr15MinEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    pgSdslCellPerfCurr15MinEntry.setStatus("current")
_PgSdslCellPerfCurr15MinLOSS_Type = Counter32
_PgSdslCellPerfCurr15MinLOSS_Object = MibTableColumn
pgSdslCellPerfCurr15MinLOSS = _PgSdslCellPerfCurr15MinLOSS_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 1, 8, 1, 1),
    _PgSdslCellPerfCurr15MinLOSS_Type()
)
pgSdslCellPerfCurr15MinLOSS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgSdslCellPerfCurr15MinLOSS.setStatus("current")
_PgSdslCellPerfCurr15MinLOCD_Type = Counter32
_PgSdslCellPerfCurr15MinLOCD_Object = MibTableColumn
pgSdslCellPerfCurr15MinLOCD = _PgSdslCellPerfCurr15MinLOCD_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 1, 8, 1, 2),
    _PgSdslCellPerfCurr15MinLOCD_Type()
)
pgSdslCellPerfCurr15MinLOCD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgSdslCellPerfCurr15MinLOCD.setStatus("current")
_PgSdslCellPerfCurr15MinSLOCD_Type = Counter32
_PgSdslCellPerfCurr15MinSLOCD_Object = MibTableColumn
pgSdslCellPerfCurr15MinSLOCD = _PgSdslCellPerfCurr15MinSLOCD_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 1, 8, 1, 3),
    _PgSdslCellPerfCurr15MinSLOCD_Type()
)
pgSdslCellPerfCurr15MinSLOCD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgSdslCellPerfCurr15MinSLOCD.setStatus("current")


class _PgSdslCellClearHistory_Type(Integer32):
    """Custom type pgSdslCellClearHistory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear", 1)
    )


_PgSdslCellClearHistory_Type.__name__ = "Integer32"
_PgSdslCellClearHistory_Object = MibTableColumn
pgSdslCellClearHistory = _PgSdslCellClearHistory_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 1, 8, 1, 4),
    _PgSdslCellClearHistory_Type()
)
pgSdslCellClearHistory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgSdslCellClearHistory.setStatus("current")
_PgSdslCellHistoryLastCleared_Type = TimeStamp
_PgSdslCellHistoryLastCleared_Object = MibTableColumn
pgSdslCellHistoryLastCleared = _PgSdslCellHistoryLastCleared_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 1, 8, 1, 5),
    _PgSdslCellHistoryLastCleared_Type()
)
pgSdslCellHistoryLastCleared.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgSdslCellHistoryLastCleared.setStatus("current")
_PgSdslCellPerf15MinIntervalTable_Object = MibTable
pgSdslCellPerf15MinIntervalTable = _PgSdslCellPerf15MinIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 1, 9)
)
if mibBuilder.loadTexts:
    pgSdslCellPerf15MinIntervalTable.setStatus("current")
_PgSdslCellPerf15MinIntervalEntry_Object = MibTableRow
pgSdslCellPerf15MinIntervalEntry = _PgSdslCellPerf15MinIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 1, 9, 1)
)
pgSdslCellPerf15MinIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "PAIRGAIN-SDSLCELL-MIB", "pgSdslCellPerf15MinIntervalIndex"),
)
if mibBuilder.loadTexts:
    pgSdslCellPerf15MinIntervalEntry.setStatus("current")


class _PgSdslCellPerf15MinIntervalIndex_Type(Integer32):
    """Custom type pgSdslCellPerf15MinIntervalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_PgSdslCellPerf15MinIntervalIndex_Type.__name__ = "Integer32"
_PgSdslCellPerf15MinIntervalIndex_Object = MibTableColumn
pgSdslCellPerf15MinIntervalIndex = _PgSdslCellPerf15MinIntervalIndex_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 1, 9, 1, 1),
    _PgSdslCellPerf15MinIntervalIndex_Type()
)
pgSdslCellPerf15MinIntervalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgSdslCellPerf15MinIntervalIndex.setStatus("current")
_PgSdslCellPerf15MinIntervalLOSS_Type = Counter32
_PgSdslCellPerf15MinIntervalLOSS_Object = MibTableColumn
pgSdslCellPerf15MinIntervalLOSS = _PgSdslCellPerf15MinIntervalLOSS_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 1, 9, 1, 2),
    _PgSdslCellPerf15MinIntervalLOSS_Type()
)
pgSdslCellPerf15MinIntervalLOSS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgSdslCellPerf15MinIntervalLOSS.setStatus("current")
_PgSdslCellPerf15MinIntervalLOCD_Type = Counter32
_PgSdslCellPerf15MinIntervalLOCD_Object = MibTableColumn
pgSdslCellPerf15MinIntervalLOCD = _PgSdslCellPerf15MinIntervalLOCD_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 1, 9, 1, 3),
    _PgSdslCellPerf15MinIntervalLOCD_Type()
)
pgSdslCellPerf15MinIntervalLOCD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgSdslCellPerf15MinIntervalLOCD.setStatus("current")
_PgSdslCellPerf15MinIntervalSLOCD_Type = Counter32
_PgSdslCellPerf15MinIntervalSLOCD_Object = MibTableColumn
pgSdslCellPerf15MinIntervalSLOCD = _PgSdslCellPerf15MinIntervalSLOCD_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 1, 9, 1, 4),
    _PgSdslCellPerf15MinIntervalSLOCD_Type()
)
pgSdslCellPerf15MinIntervalSLOCD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgSdslCellPerf15MinIntervalSLOCD.setStatus("current")
_PgSdslCellPerfCurr24hTable_Object = MibTable
pgSdslCellPerfCurr24hTable = _PgSdslCellPerfCurr24hTable_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 1, 10)
)
if mibBuilder.loadTexts:
    pgSdslCellPerfCurr24hTable.setStatus("current")
_PgSdslCellPerfCurr24hEntry_Object = MibTableRow
pgSdslCellPerfCurr24hEntry = _PgSdslCellPerfCurr24hEntry_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 1, 10, 1)
)
pgSdslCellPerfCurr24hEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    pgSdslCellPerfCurr24hEntry.setStatus("current")
_PgSdslCellPerfCurr24hLOSS_Type = Counter32
_PgSdslCellPerfCurr24hLOSS_Object = MibTableColumn
pgSdslCellPerfCurr24hLOSS = _PgSdslCellPerfCurr24hLOSS_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 1, 10, 1, 1),
    _PgSdslCellPerfCurr24hLOSS_Type()
)
pgSdslCellPerfCurr24hLOSS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgSdslCellPerfCurr24hLOSS.setStatus("current")
_PgSdslCellPerfCurr24hLOCD_Type = Counter32
_PgSdslCellPerfCurr24hLOCD_Object = MibTableColumn
pgSdslCellPerfCurr24hLOCD = _PgSdslCellPerfCurr24hLOCD_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 1, 10, 1, 2),
    _PgSdslCellPerfCurr24hLOCD_Type()
)
pgSdslCellPerfCurr24hLOCD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgSdslCellPerfCurr24hLOCD.setStatus("current")
_PgSdslCellPerfCurr24hSLOCD_Type = Counter32
_PgSdslCellPerfCurr24hSLOCD_Object = MibTableColumn
pgSdslCellPerfCurr24hSLOCD = _PgSdslCellPerfCurr24hSLOCD_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 1, 10, 1, 3),
    _PgSdslCellPerfCurr24hSLOCD_Type()
)
pgSdslCellPerfCurr24hSLOCD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgSdslCellPerfCurr24hSLOCD.setStatus("current")
_PgSdslCellPerf24hIntervalTable_Object = MibTable
pgSdslCellPerf24hIntervalTable = _PgSdslCellPerf24hIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 1, 11)
)
if mibBuilder.loadTexts:
    pgSdslCellPerf24hIntervalTable.setStatus("current")
_PgSdslCellPerf24hIntervalEntry_Object = MibTableRow
pgSdslCellPerf24hIntervalEntry = _PgSdslCellPerf24hIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 1, 11, 1)
)
pgSdslCellPerf24hIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "PAIRGAIN-SDSLCELL-MIB", "pgSdslCellPerf24hIntervalIndex"),
)
if mibBuilder.loadTexts:
    pgSdslCellPerf24hIntervalEntry.setStatus("current")


class _PgSdslCellPerf24hIntervalIndex_Type(Integer32):
    """Custom type pgSdslCellPerf24hIntervalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_PgSdslCellPerf24hIntervalIndex_Type.__name__ = "Integer32"
_PgSdslCellPerf24hIntervalIndex_Object = MibTableColumn
pgSdslCellPerf24hIntervalIndex = _PgSdslCellPerf24hIntervalIndex_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 1, 11, 1, 1),
    _PgSdslCellPerf24hIntervalIndex_Type()
)
pgSdslCellPerf24hIntervalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgSdslCellPerf24hIntervalIndex.setStatus("current")
_PgSdslCellPerf24hIntervalLOSS_Type = Counter32
_PgSdslCellPerf24hIntervalLOSS_Object = MibTableColumn
pgSdslCellPerf24hIntervalLOSS = _PgSdslCellPerf24hIntervalLOSS_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 1, 11, 1, 2),
    _PgSdslCellPerf24hIntervalLOSS_Type()
)
pgSdslCellPerf24hIntervalLOSS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgSdslCellPerf24hIntervalLOSS.setStatus("current")
_PgSdslCellPerf24hIntervalLOCD_Type = Counter32
_PgSdslCellPerf24hIntervalLOCD_Object = MibTableColumn
pgSdslCellPerf24hIntervalLOCD = _PgSdslCellPerf24hIntervalLOCD_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 1, 11, 1, 3),
    _PgSdslCellPerf24hIntervalLOCD_Type()
)
pgSdslCellPerf24hIntervalLOCD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgSdslCellPerf24hIntervalLOCD.setStatus("current")
_PgSdslCellPerf24hIntervalSLOCD_Type = Counter32
_PgSdslCellPerf24hIntervalSLOCD_Object = MibTableColumn
pgSdslCellPerf24hIntervalSLOCD = _PgSdslCellPerf24hIntervalSLOCD_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 1, 11, 1, 4),
    _PgSdslCellPerf24hIntervalSLOCD_Type()
)
pgSdslCellPerf24hIntervalSLOCD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgSdslCellPerf24hIntervalSLOCD.setStatus("current")
_PgSdslCellAlarmTable_Object = MibTable
pgSdslCellAlarmTable = _PgSdslCellAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 1, 12)
)
if mibBuilder.loadTexts:
    pgSdslCellAlarmTable.setStatus("current")
_PgSdslCellAlarmEntry_Object = MibTableRow
pgSdslCellAlarmEntry = _PgSdslCellAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 1, 12, 1)
)
pgSdslCellAlarmEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    pgSdslCellAlarmEntry.setStatus("current")


class _PgSdslCellCrossThreshLOSS_Type(Integer32):
    """Custom type pgSdslCellCrossThreshLOSS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 1))
    )


_PgSdslCellCrossThreshLOSS_Type.__name__ = "Integer32"
_PgSdslCellCrossThreshLOSS_Object = MibTableColumn
pgSdslCellCrossThreshLOSS = _PgSdslCellCrossThreshLOSS_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 1, 12, 1, 1),
    _PgSdslCellCrossThreshLOSS_Type()
)
pgSdslCellCrossThreshLOSS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgSdslCellCrossThreshLOSS.setStatus("current")


class _PgSdslCellCrossThreshLOCD_Type(Integer32):
    """Custom type pgSdslCellCrossThreshLOCD based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 1))
    )


_PgSdslCellCrossThreshLOCD_Type.__name__ = "Integer32"
_PgSdslCellCrossThreshLOCD_Object = MibTableColumn
pgSdslCellCrossThreshLOCD = _PgSdslCellCrossThreshLOCD_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 1, 12, 1, 2),
    _PgSdslCellCrossThreshLOCD_Type()
)
pgSdslCellCrossThreshLOCD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgSdslCellCrossThreshLOCD.setStatus("current")


class _PgSdslCellCrossThreshSLOCD_Type(Integer32):
    """Custom type pgSdslCellCrossThreshSLOCD based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 1))
    )


_PgSdslCellCrossThreshSLOCD_Type.__name__ = "Integer32"
_PgSdslCellCrossThreshSLOCD_Object = MibTableColumn
pgSdslCellCrossThreshSLOCD = _PgSdslCellCrossThreshSLOCD_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 1, 12, 1, 3),
    _PgSdslCellCrossThreshSLOCD_Type()
)
pgSdslCellCrossThreshSLOCD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgSdslCellCrossThreshSLOCD.setStatus("current")


class _PgSdslCellCrossThreshSNR_Type(Integer32):
    """Custom type pgSdslCellCrossThreshSNR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 1))
    )


_PgSdslCellCrossThreshSNR_Type.__name__ = "Integer32"
_PgSdslCellCrossThreshSNR_Object = MibTableColumn
pgSdslCellCrossThreshSNR = _PgSdslCellCrossThreshSNR_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 1, 12, 1, 4),
    _PgSdslCellCrossThreshSNR_Type()
)
pgSdslCellCrossThreshSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgSdslCellCrossThreshSNR.setStatus("current")


class _PgSdslCellHardwareCause_Type(Integer32):
    """Custom type pgSdslCellHardwareCause based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("otherfail", 3),
          ("xcvrfail", 2))
    )


_PgSdslCellHardwareCause_Type.__name__ = "Integer32"
_PgSdslCellHardwareCause_Object = MibTableColumn
pgSdslCellHardwareCause = _PgSdslCellHardwareCause_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 1, 12, 1, 5),
    _PgSdslCellHardwareCause_Type()
)
pgSdslCellHardwareCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgSdslCellHardwareCause.setStatus("current")
_PgSdslCellAlarmLastChanged_Type = TimeStamp
_PgSdslCellAlarmLastChanged_Object = MibTableColumn
pgSdslCellAlarmLastChanged = _PgSdslCellAlarmLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 1, 12, 1, 6),
    _PgSdslCellAlarmLastChanged_Type()
)
pgSdslCellAlarmLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgSdslCellAlarmLastChanged.setStatus("current")
_PgSdslCellTraps_ObjectIdentity = ObjectIdentity
pgSdslCellTraps = _PgSdslCellTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 2)
)
_PgSdslCellTrap_ObjectIdentity = ObjectIdentity
pgSdslCellTrap = _PgSdslCellTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 2, 0)
)

# Managed Objects groups


# Notification objects

pgSdslCellThreshLOSSTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 2, 0, 1)
)
pgSdslCellThreshLOSSTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("PAIRGAIN-SDSLCELL-MIB", "pgSdslCellCrossThreshLOSS"),
        ("PAIRGAIN-SDSLCELL-MIB", "pgSdslCellAlarmLastChanged"))
)
if mibBuilder.loadTexts:
    pgSdslCellThreshLOSSTrap.setStatus(
        "current"
    )

pgSdslCellThreshLOCDTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 2, 0, 2)
)
pgSdslCellThreshLOCDTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("PAIRGAIN-SDSLCELL-MIB", "pgSdslCellCrossThreshLOCD"),
        ("PAIRGAIN-SDSLCELL-MIB", "pgSdslCellAlarmLastChanged"))
)
if mibBuilder.loadTexts:
    pgSdslCellThreshLOCDTrap.setStatus(
        "current"
    )

pgSdslCellThreshSLOCDTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 2, 0, 3)
)
pgSdslCellThreshSLOCDTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("PAIRGAIN-SDSLCELL-MIB", "pgSdslCellCrossThreshSLOCD"),
        ("PAIRGAIN-SDSLCELL-MIB", "pgSdslCellAlarmLastChanged"))
)
if mibBuilder.loadTexts:
    pgSdslCellThreshSLOCDTrap.setStatus(
        "current"
    )

pgSdslCellThreshSNRTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 2, 0, 4)
)
pgSdslCellThreshSNRTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("PAIRGAIN-SDSLCELL-MIB", "pgSdslCellCrossThreshSNR"),
        ("PAIRGAIN-SDSLCELL-MIB", "pgSdslCellAlarmLastChanged"))
)
if mibBuilder.loadTexts:
    pgSdslCellThreshSNRTrap.setStatus(
        "current"
    )

pgSdslCellHardwareFaultTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 2, 0, 5)
)
pgSdslCellHardwareFaultTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("PAIRGAIN-SDSLCELL-MIB", "pgSdslCellHardwareCause"),
        ("PAIRGAIN-SDSLCELL-MIB", "pgSdslCellAlarmLastChanged"))
)
if mibBuilder.loadTexts:
    pgSdslCellHardwareFaultTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PAIRGAIN-SDSLCELL-MIB",
    **{"PgSdslcellLineProfileType": PgSdslcellLineProfileType,
       "PgSdslcellAlarmProfileType": PgSdslcellAlarmProfileType,
       "pgsdslCellMIB": pgsdslCellMIB,
       "pgsdslCellMibObjects": pgsdslCellMibObjects,
       "pgSdslCellLineTable": pgSdslCellLineTable,
       "pgSdslCellLineEntry": pgSdslCellLineEntry,
       "pgSdslCellLineProfile": pgSdslCellLineProfile,
       "pgSdslCellAlarmProfile": pgSdslCellAlarmProfile,
       "pgSdslCellPhysTable": pgSdslCellPhysTable,
       "pgSdslCellPhysEntry": pgSdslCellPhysEntry,
       "pgSdslCellInvSerialNumber": pgSdslCellInvSerialNumber,
       "pgSdslCellInvVendorID": pgSdslCellInvVendorID,
       "pgSdslCellInvVersionNumber": pgSdslCellInvVersionNumber,
       "pgSdslCellCurrSnrMgn": pgSdslCellCurrSnrMgn,
       "pgSdslCellCurrAtn": pgSdslCellCurrAtn,
       "pgSdslCellCurrStatus": pgSdslCellCurrStatus,
       "pgSdslCellLineProfileIndexNext": pgSdslCellLineProfileIndexNext,
       "pgSdslCellLineProfileTable": pgSdslCellLineProfileTable,
       "pgSdslCellLineProfileEntry": pgSdslCellLineProfileEntry,
       "pgSdslCellLineProfileIndex": pgSdslCellLineProfileIndex,
       "pgSdslCellLineProfileRowStatus": pgSdslCellLineProfileRowStatus,
       "pgSdslCellLineCode": pgSdslCellLineCode,
       "pgSdslCellLineRateMode": pgSdslCellLineRateMode,
       "pgSdslCellLineRate": pgSdslCellLineRate,
       "pgSdslCellLineTermType": pgSdslCellLineTermType,
       "pgSdslCellLineProfileInUse": pgSdslCellLineProfileInUse,
       "pgSdslCellAlarmProfileIndexNext": pgSdslCellAlarmProfileIndexNext,
       "pgSdslCellAlarmProfileTable": pgSdslCellAlarmProfileTable,
       "pgSdslCellAlarmProfileEntry": pgSdslCellAlarmProfileEntry,
       "pgSdslCellAlarmProfileIndex": pgSdslCellAlarmProfileIndex,
       "pgSdslCellAlarmProfileRowStatus": pgSdslCellAlarmProfileRowStatus,
       "pgSdslCellThresh15MinLOSS": pgSdslCellThresh15MinLOSS,
       "pgSdslCellThresh15MinLOCD": pgSdslCellThresh15MinLOCD,
       "pgSdslCellThresh15MinSLOCD": pgSdslCellThresh15MinSLOCD,
       "pgSdslCellThreshSNR": pgSdslCellThreshSNR,
       "pgSdslCellAlarmProfileInUse": pgSdslCellAlarmProfileInUse,
       "pgSdslCellPerfCurrTable": pgSdslCellPerfCurrTable,
       "pgSdslCellPerfCurrEntry": pgSdslCellPerfCurrEntry,
       "pgSdslCellPerfCurrLOSS": pgSdslCellPerfCurrLOSS,
       "pgSdslCellPerfCurrLOCD": pgSdslCellPerfCurrLOCD,
       "pgSdslCellPerfCurrSLOCD": pgSdslCellPerfCurrSLOCD,
       "pgSdslCellClearStats": pgSdslCellClearStats,
       "pgSdslCellStatsLastCleared": pgSdslCellStatsLastCleared,
       "pgSdslCellPerfCurr15MinTable": pgSdslCellPerfCurr15MinTable,
       "pgSdslCellPerfCurr15MinEntry": pgSdslCellPerfCurr15MinEntry,
       "pgSdslCellPerfCurr15MinLOSS": pgSdslCellPerfCurr15MinLOSS,
       "pgSdslCellPerfCurr15MinLOCD": pgSdslCellPerfCurr15MinLOCD,
       "pgSdslCellPerfCurr15MinSLOCD": pgSdslCellPerfCurr15MinSLOCD,
       "pgSdslCellClearHistory": pgSdslCellClearHistory,
       "pgSdslCellHistoryLastCleared": pgSdslCellHistoryLastCleared,
       "pgSdslCellPerf15MinIntervalTable": pgSdslCellPerf15MinIntervalTable,
       "pgSdslCellPerf15MinIntervalEntry": pgSdslCellPerf15MinIntervalEntry,
       "pgSdslCellPerf15MinIntervalIndex": pgSdslCellPerf15MinIntervalIndex,
       "pgSdslCellPerf15MinIntervalLOSS": pgSdslCellPerf15MinIntervalLOSS,
       "pgSdslCellPerf15MinIntervalLOCD": pgSdslCellPerf15MinIntervalLOCD,
       "pgSdslCellPerf15MinIntervalSLOCD": pgSdslCellPerf15MinIntervalSLOCD,
       "pgSdslCellPerfCurr24hTable": pgSdslCellPerfCurr24hTable,
       "pgSdslCellPerfCurr24hEntry": pgSdslCellPerfCurr24hEntry,
       "pgSdslCellPerfCurr24hLOSS": pgSdslCellPerfCurr24hLOSS,
       "pgSdslCellPerfCurr24hLOCD": pgSdslCellPerfCurr24hLOCD,
       "pgSdslCellPerfCurr24hSLOCD": pgSdslCellPerfCurr24hSLOCD,
       "pgSdslCellPerf24hIntervalTable": pgSdslCellPerf24hIntervalTable,
       "pgSdslCellPerf24hIntervalEntry": pgSdslCellPerf24hIntervalEntry,
       "pgSdslCellPerf24hIntervalIndex": pgSdslCellPerf24hIntervalIndex,
       "pgSdslCellPerf24hIntervalLOSS": pgSdslCellPerf24hIntervalLOSS,
       "pgSdslCellPerf24hIntervalLOCD": pgSdslCellPerf24hIntervalLOCD,
       "pgSdslCellPerf24hIntervalSLOCD": pgSdslCellPerf24hIntervalSLOCD,
       "pgSdslCellAlarmTable": pgSdslCellAlarmTable,
       "pgSdslCellAlarmEntry": pgSdslCellAlarmEntry,
       "pgSdslCellCrossThreshLOSS": pgSdslCellCrossThreshLOSS,
       "pgSdslCellCrossThreshLOCD": pgSdslCellCrossThreshLOCD,
       "pgSdslCellCrossThreshSLOCD": pgSdslCellCrossThreshSLOCD,
       "pgSdslCellCrossThreshSNR": pgSdslCellCrossThreshSNR,
       "pgSdslCellHardwareCause": pgSdslCellHardwareCause,
       "pgSdslCellAlarmLastChanged": pgSdslCellAlarmLastChanged,
       "pgSdslCellTraps": pgSdslCellTraps,
       "pgSdslCellTrap": pgSdslCellTrap,
       "pgSdslCellThreshLOSSTrap": pgSdslCellThreshLOSSTrap,
       "pgSdslCellThreshLOCDTrap": pgSdslCellThreshLOCDTrap,
       "pgSdslCellThreshSLOCDTrap": pgSdslCellThreshSLOCDTrap,
       "pgSdslCellThreshSNRTrap": pgSdslCellThreshSNRTrap,
       "pgSdslCellHardwareFaultTrap": pgSdslCellHardwareFaultTrap}
)
