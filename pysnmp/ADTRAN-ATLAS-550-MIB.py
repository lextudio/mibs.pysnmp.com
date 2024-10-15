# SNMP MIB module (ADTRAN-ATLAS-550-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ADTRAN-ATLAS-550-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:34:20 2024
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

_Adtran_ObjectIdentity = ObjectIdentity
adtran = _Adtran_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664)
)
_AdMgmt_ObjectIdentity = ObjectIdentity
adMgmt = _AdMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 2)
)
_AdATLAS550mg_ObjectIdentity = ObjectIdentity
adATLAS550mg = _AdATLAS550mg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 2, 219)
)
_AdATLAS550Fpnl_ObjectIdentity = ObjectIdentity
adATLAS550Fpnl = _AdATLAS550Fpnl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 2, 219, 1)
)
_AdATLAS550FpnlSysLeds_ObjectIdentity = ObjectIdentity
adATLAS550FpnlSysLeds = _AdATLAS550FpnlSysLeds_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 2, 219, 1, 1)
)


class _AdATLAS550FpnlPow_Type(Integer32):
    """Custom type adATLAS550FpnlPow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sysoff", 2),
          ("syson", 1))
    )


_AdATLAS550FpnlPow_Type.__name__ = "Integer32"
_AdATLAS550FpnlPow_Object = MibScalar
adATLAS550FpnlPow = _AdATLAS550FpnlPow_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 219, 1, 1, 1),
    _AdATLAS550FpnlPow_Type()
)
adATLAS550FpnlPow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adATLAS550FpnlPow.setStatus("mandatory")


class _AdATLAS550FpnlSys_Type(Integer32):
    """Custom type adATLAS550FpnlSys based on Integer32"""
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
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("greenslow", 7),
          ("redslow", 10),
          ("syserr", 2),
          ("sysflasherror", 5),
          ("sysflashupdate", 4),
          ("sysoff", 6),
          ("sysok", 1),
          ("syswarn", 3),
          ("yellowfast", 9),
          ("yellowslow", 8))
    )


_AdATLAS550FpnlSys_Type.__name__ = "Integer32"
_AdATLAS550FpnlSys_Object = MibScalar
adATLAS550FpnlSys = _AdATLAS550FpnlSys_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 219, 1, 1, 2),
    _AdATLAS550FpnlSys_Type()
)
adATLAS550FpnlSys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adATLAS550FpnlSys.setStatus("mandatory")


class _AdATLAS550FpnlEth_Type(Integer32):
    """Custom type adATLAS550FpnlEth based on Integer32"""
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
        *(("etherflashfast", 4),
          ("etherflashslow", 3),
          ("etheroff", 2),
          ("etheron", 1))
    )


_AdATLAS550FpnlEth_Type.__name__ = "Integer32"
_AdATLAS550FpnlEth_Object = MibScalar
adATLAS550FpnlEth = _AdATLAS550FpnlEth_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 219, 1, 1, 3),
    _AdATLAS550FpnlEth_Type()
)
adATLAS550FpnlEth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adATLAS550FpnlEth.setStatus("mandatory")


class _AdATLAS550FpnlRem_Type(Integer32):
    """Custom type adATLAS550FpnlRem based on Integer32"""
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
        *(("remflashfast", 4),
          ("remflashslow", 3),
          ("remoff", 2),
          ("remon", 1))
    )


_AdATLAS550FpnlRem_Type.__name__ = "Integer32"
_AdATLAS550FpnlRem_Object = MibScalar
adATLAS550FpnlRem = _AdATLAS550FpnlRem_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 219, 1, 1, 4),
    _AdATLAS550FpnlRem_Type()
)
adATLAS550FpnlRem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adATLAS550FpnlRem.setStatus("mandatory")
_AdATLAS550FpnlNtwkLeds_ObjectIdentity = ObjectIdentity
adATLAS550FpnlNtwkLeds = _AdATLAS550FpnlNtwkLeds_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 2, 219, 1, 2)
)
_AdATLAS550FpnlNwTable_Object = MibTable
adATLAS550FpnlNwTable = _AdATLAS550FpnlNwTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 219, 1, 2, 1)
)
if mibBuilder.loadTexts:
    adATLAS550FpnlNwTable.setStatus("mandatory")
_AdATLAS550FpnlNwEntry_Object = MibTableRow
adATLAS550FpnlNwEntry = _AdATLAS550FpnlNwEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 219, 1, 2, 1, 1)
)
adATLAS550FpnlNwEntry.setIndexNames(
    (0, "ADTRAN-ATLAS-550-MIB", "adATLAS550FpnlNwIndex"),
)
if mibBuilder.loadTexts:
    adATLAS550FpnlNwEntry.setStatus("mandatory")
_AdATLAS550FpnlNwIndex_Type = Integer32
_AdATLAS550FpnlNwIndex_Object = MibTableColumn
adATLAS550FpnlNwIndex = _AdATLAS550FpnlNwIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 219, 1, 2, 1, 1, 1),
    _AdATLAS550FpnlNwIndex_Type()
)
adATLAS550FpnlNwIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adATLAS550FpnlNwIndex.setStatus("mandatory")


class _AdATLAS550FpnlNwOK_Type(Integer32):
    """Custom type adATLAS550FpnlNwOK based on Integer32"""
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
        *(("nwokflashfast", 3),
          ("nwokflashslow", 2),
          ("nwokoff", 4),
          ("nwokon", 1))
    )


_AdATLAS550FpnlNwOK_Type.__name__ = "Integer32"
_AdATLAS550FpnlNwOK_Object = MibTableColumn
adATLAS550FpnlNwOK = _AdATLAS550FpnlNwOK_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 219, 1, 2, 1, 1, 2),
    _AdATLAS550FpnlNwOK_Type()
)
adATLAS550FpnlNwOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adATLAS550FpnlNwOK.setStatus("mandatory")


class _AdATLAS550FpnlNwTest_Type(Integer32):
    """Custom type adATLAS550FpnlNwTest based on Integer32"""
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
        *(("testflashfast", 3),
          ("testflashslow", 2),
          ("testoff", 4),
          ("teston", 1))
    )


_AdATLAS550FpnlNwTest_Type.__name__ = "Integer32"
_AdATLAS550FpnlNwTest_Object = MibTableColumn
adATLAS550FpnlNwTest = _AdATLAS550FpnlNwTest_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 219, 1, 2, 1, 1, 3),
    _AdATLAS550FpnlNwTest_Type()
)
adATLAS550FpnlNwTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adATLAS550FpnlNwTest.setStatus("mandatory")


class _AdATLAS550FpnlNwError_Type(Integer32):
    """Custom type adATLAS550FpnlNwError based on Integer32"""
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
        *(("errorflashfast", 3),
          ("errorflashslow", 2),
          ("erroroff", 4),
          ("erroron", 1))
    )


_AdATLAS550FpnlNwError_Type.__name__ = "Integer32"
_AdATLAS550FpnlNwError_Object = MibTableColumn
adATLAS550FpnlNwError = _AdATLAS550FpnlNwError_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 219, 1, 2, 1, 1, 4),
    _AdATLAS550FpnlNwError_Type()
)
adATLAS550FpnlNwError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adATLAS550FpnlNwError.setStatus("mandatory")


class _AdATLAS550FpnlNwAlarm_Type(Integer32):
    """Custom type adATLAS550FpnlNwAlarm based on Integer32"""
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
        *(("alarmflashfast", 3),
          ("alarmflashslow", 2),
          ("alarmoff", 4),
          ("alarmon", 1))
    )


_AdATLAS550FpnlNwAlarm_Type.__name__ = "Integer32"
_AdATLAS550FpnlNwAlarm_Object = MibTableColumn
adATLAS550FpnlNwAlarm = _AdATLAS550FpnlNwAlarm_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 219, 1, 2, 1, 1, 5),
    _AdATLAS550FpnlNwAlarm_Type()
)
adATLAS550FpnlNwAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adATLAS550FpnlNwAlarm.setStatus("mandatory")
_AdATLAS550FpnlModLeds_ObjectIdentity = ObjectIdentity
adATLAS550FpnlModLeds = _AdATLAS550FpnlModLeds_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 2, 219, 1, 3)
)
_AdATLAS550FpnlModNumber_Type = Integer32
_AdATLAS550FpnlModNumber_Object = MibScalar
adATLAS550FpnlModNumber = _AdATLAS550FpnlModNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 219, 1, 3, 1),
    _AdATLAS550FpnlModNumber_Type()
)
adATLAS550FpnlModNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adATLAS550FpnlModNumber.setStatus("mandatory")
_AdATLAS550FpnlMLTable_Object = MibTable
adATLAS550FpnlMLTable = _AdATLAS550FpnlMLTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 219, 1, 3, 2)
)
if mibBuilder.loadTexts:
    adATLAS550FpnlMLTable.setStatus("mandatory")
_AdATLAS550FpnlMLEntry_Object = MibTableRow
adATLAS550FpnlMLEntry = _AdATLAS550FpnlMLEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 219, 1, 3, 2, 1)
)
adATLAS550FpnlMLEntry.setIndexNames(
    (0, "ADTRAN-ATLAS-550-MIB", "adATLAS550FpnlMLIndex"),
)
if mibBuilder.loadTexts:
    adATLAS550FpnlMLEntry.setStatus("mandatory")
_AdATLAS550FpnlMLIndex_Type = Integer32
_AdATLAS550FpnlMLIndex_Object = MibTableColumn
adATLAS550FpnlMLIndex = _AdATLAS550FpnlMLIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 219, 1, 3, 2, 1, 1),
    _AdATLAS550FpnlMLIndex_Type()
)
adATLAS550FpnlMLIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adATLAS550FpnlMLIndex.setStatus("mandatory")


class _AdATLAS550FpnlMLStatus_Type(Integer32):
    """Custom type adATLAS550FpnlMLStatus based on Integer32"""
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
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("mlstatuserr", 3),
          ("mlstatusflashfastgreen", 5),
          ("mlstatusflashfastred", 9),
          ("mlstatusflashfastyellow", 7),
          ("mlstatusflashslowgreen", 4),
          ("mlstatusflashslowred", 8),
          ("mlstatusflashslowyellow", 6),
          ("mlstatusoff", 10),
          ("mlstatusok", 1),
          ("mlstatuswarn", 2))
    )


_AdATLAS550FpnlMLStatus_Type.__name__ = "Integer32"
_AdATLAS550FpnlMLStatus_Object = MibTableColumn
adATLAS550FpnlMLStatus = _AdATLAS550FpnlMLStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 219, 1, 3, 2, 1, 2),
    _AdATLAS550FpnlMLStatus_Type()
)
adATLAS550FpnlMLStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adATLAS550FpnlMLStatus.setStatus("mandatory")


class _AdATLAS550FpnlMLOnline_Type(Integer32):
    """Custom type adATLAS550FpnlMLOnline based on Integer32"""
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
        *(("mlonlineflashfast", 3),
          ("mlonlineflashslow", 2),
          ("mlonlineoff", 4),
          ("mlonlineon", 1))
    )


_AdATLAS550FpnlMLOnline_Type.__name__ = "Integer32"
_AdATLAS550FpnlMLOnline_Object = MibTableColumn
adATLAS550FpnlMLOnline = _AdATLAS550FpnlMLOnline_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 219, 1, 3, 2, 1, 3),
    _AdATLAS550FpnlMLOnline_Type()
)
adATLAS550FpnlMLOnline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adATLAS550FpnlMLOnline.setStatus("mandatory")


class _AdATLAS550FpnlMLTest_Type(Integer32):
    """Custom type adATLAS550FpnlMLTest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mltestflash", 2),
          ("mltestoff", 3),
          ("mlteston", 1))
    )


_AdATLAS550FpnlMLTest_Type.__name__ = "Integer32"
_AdATLAS550FpnlMLTest_Object = MibTableColumn
adATLAS550FpnlMLTest = _AdATLAS550FpnlMLTest_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 219, 1, 3, 2, 1, 4),
    _AdATLAS550FpnlMLTest_Type()
)
adATLAS550FpnlMLTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adATLAS550FpnlMLTest.setStatus("mandatory")

# Managed Objects groups


# Notification objects

adATLAS550ExtAlarmActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 2, 219, 0, 21900)
)
if mibBuilder.loadTexts:
    adATLAS550ExtAlarmActive.setStatus(
        ""
    )

adATLAS550ExtAlarmInactive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 2, 219, 0, 21901)
)
if mibBuilder.loadTexts:
    adATLAS550ExtAlarmInactive.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-ATLAS-550-MIB",
    **{"adtran": adtran,
       "adMgmt": adMgmt,
       "adATLAS550mg": adATLAS550mg,
       "adATLAS550ExtAlarmActive": adATLAS550ExtAlarmActive,
       "adATLAS550ExtAlarmInactive": adATLAS550ExtAlarmInactive,
       "adATLAS550Fpnl": adATLAS550Fpnl,
       "adATLAS550FpnlSysLeds": adATLAS550FpnlSysLeds,
       "adATLAS550FpnlPow": adATLAS550FpnlPow,
       "adATLAS550FpnlSys": adATLAS550FpnlSys,
       "adATLAS550FpnlEth": adATLAS550FpnlEth,
       "adATLAS550FpnlRem": adATLAS550FpnlRem,
       "adATLAS550FpnlNtwkLeds": adATLAS550FpnlNtwkLeds,
       "adATLAS550FpnlNwTable": adATLAS550FpnlNwTable,
       "adATLAS550FpnlNwEntry": adATLAS550FpnlNwEntry,
       "adATLAS550FpnlNwIndex": adATLAS550FpnlNwIndex,
       "adATLAS550FpnlNwOK": adATLAS550FpnlNwOK,
       "adATLAS550FpnlNwTest": adATLAS550FpnlNwTest,
       "adATLAS550FpnlNwError": adATLAS550FpnlNwError,
       "adATLAS550FpnlNwAlarm": adATLAS550FpnlNwAlarm,
       "adATLAS550FpnlModLeds": adATLAS550FpnlModLeds,
       "adATLAS550FpnlModNumber": adATLAS550FpnlModNumber,
       "adATLAS550FpnlMLTable": adATLAS550FpnlMLTable,
       "adATLAS550FpnlMLEntry": adATLAS550FpnlMLEntry,
       "adATLAS550FpnlMLIndex": adATLAS550FpnlMLIndex,
       "adATLAS550FpnlMLStatus": adATLAS550FpnlMLStatus,
       "adATLAS550FpnlMLOnline": adATLAS550FpnlMLOnline,
       "adATLAS550FpnlMLTest": adATLAS550FpnlMLTest}
)
