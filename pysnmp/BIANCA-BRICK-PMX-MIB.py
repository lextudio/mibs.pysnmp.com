# SNMP MIB module (BIANCA-BRICK-PMX-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BIANCA-BRICK-PMX-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:47:38 2024
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



class Date(Integer32):
    """Custom type Date based on Integer32"""




class HexValue(Integer32):
    """Custom type HexValue based on Integer32"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Org_ObjectIdentity = ObjectIdentity
org = _Org_ObjectIdentity(
    (1, 3)
)
_Dod_ObjectIdentity = ObjectIdentity
dod = _Dod_ObjectIdentity(
    (1, 3, 6)
)
_Internet_ObjectIdentity = ObjectIdentity
internet = _Internet_ObjectIdentity(
    (1, 3, 6, 1)
)
_Private_ObjectIdentity = ObjectIdentity
private = _Private_ObjectIdentity(
    (1, 3, 6, 1, 4)
)
_Enterprises_ObjectIdentity = ObjectIdentity
enterprises = _Enterprises_ObjectIdentity(
    (1, 3, 6, 1, 4, 1)
)
_Bintec_ObjectIdentity = ObjectIdentity
bintec = _Bintec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272)
)
_Bibo_ObjectIdentity = ObjectIdentity
bibo = _Bibo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272, 4)
)
_Pmx_ObjectIdentity = ObjectIdentity
pmx = _Pmx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272, 4, 12)
)
_PmxIfTable_Object = MibTable
pmxIfTable = _PmxIfTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 12, 1)
)
if mibBuilder.loadTexts:
    pmxIfTable.setStatus("mandatory")
_PmxIfEntry_Object = MibTableRow
pmxIfEntry = _PmxIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 12, 1, 1)
)
pmxIfEntry.setIndexNames(
    (0, "BIANCA-BRICK-PMX-MIB", "pmxIfIndex"),
)
if mibBuilder.loadTexts:
    pmxIfEntry.setStatus("mandatory")
_PmxIfIndex_Type = Integer32
_PmxIfIndex_Object = MibTableColumn
pmxIfIndex = _PmxIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 12, 1, 1, 1),
    _PmxIfIndex_Type()
)
pmxIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmxIfIndex.setStatus("mandatory")


class _PmxIfSelftest_Type(Integer32):
    """Custom type pmxIfSelftest based on Integer32"""
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
        *(("acfa-failure", 2),
          ("m32-failure", 3),
          ("mem-failure", 4),
          ("successful", 1))
    )


_PmxIfSelftest_Type.__name__ = "Integer32"
_PmxIfSelftest_Object = MibTableColumn
pmxIfSelftest = _PmxIfSelftest_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 12, 1, 1, 2),
    _PmxIfSelftest_Type()
)
pmxIfSelftest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmxIfSelftest.setStatus("mandatory")


class _PmxIfLayer1State_Type(Integer32):
    """Custom type pmxIfLayer1State based on Integer32"""
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
        *(("active", 1),
          ("crc-error", 5),
          ("no-signal", 3),
          ("no-sync", 4),
          ("power-on", 6),
          ("remote-alarm", 2),
          ("resync", 7))
    )


_PmxIfLayer1State_Type.__name__ = "Integer32"
_PmxIfLayer1State_Object = MibTableColumn
pmxIfLayer1State = _PmxIfLayer1State_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 12, 1, 1, 3),
    _PmxIfLayer1State_Type()
)
pmxIfLayer1State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmxIfLayer1State.setStatus("mandatory")


class _PmxIfLayer1Mode_Type(Integer32):
    """Custom type pmxIfLayer1Mode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e1", 1),
          ("t1", 2))
    )


_PmxIfLayer1Mode_Type.__name__ = "Integer32"
_PmxIfLayer1Mode_Object = MibTableColumn
pmxIfLayer1Mode = _PmxIfLayer1Mode_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 12, 1, 1, 4),
    _PmxIfLayer1Mode_Type()
)
pmxIfLayer1Mode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmxIfLayer1Mode.setStatus("mandatory")


class _PmxIfLayer1Framing_Type(Integer32):
    """Custom type pmxIfLayer1Framing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("e1", 1),
          ("e1-crc", 3),
          ("e1-mf", 2),
          ("e1-mf-crc", 4),
          ("t1-d4", 6),
          ("t1-esf", 5))
    )


_PmxIfLayer1Framing_Type.__name__ = "Integer32"
_PmxIfLayer1Framing_Object = MibTableColumn
pmxIfLayer1Framing = _PmxIfLayer1Framing_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 12, 1, 1, 5),
    _PmxIfLayer1Framing_Type()
)
pmxIfLayer1Framing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmxIfLayer1Framing.setStatus("mandatory")


class _PmxIfLayer1LineCode_Type(Integer32):
    """Custom type pmxIfLayer1LineCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("e1-hdb3", 1),
          ("t1-ami", 3),
          ("t1-b8zs", 2))
    )


_PmxIfLayer1LineCode_Type.__name__ = "Integer32"
_PmxIfLayer1LineCode_Object = MibTableColumn
pmxIfLayer1LineCode = _PmxIfLayer1LineCode_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 12, 1, 1, 6),
    _PmxIfLayer1LineCode_Type()
)
pmxIfLayer1LineCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmxIfLayer1LineCode.setStatus("mandatory")


class _PmxIfChannelMode_Type(Integer32):
    """Custom type pmxIfChannelMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              10,
              11,
              12,
              13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("e1-1tr6", 2),
          ("e1-H0", 3),
          ("e1-H12", 4),
          ("e1-burst", 5),
          ("e1-raw", 6),
          ("e1-standard", 1),
          ("t1-H0", 11),
          ("t1-H11", 12),
          ("t1-burst", 13),
          ("t1-raw", 14),
          ("t1-standard", 10))
    )


_PmxIfChannelMode_Type.__name__ = "Integer32"
_PmxIfChannelMode_Object = MibTableColumn
pmxIfChannelMode = _PmxIfChannelMode_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 12, 1, 1, 7),
    _PmxIfChannelMode_Type()
)
pmxIfChannelMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmxIfChannelMode.setStatus("mandatory")


class _PmxIfLoopbackMode_Type(Integer32):
    """Custom type pmxIfLoopbackMode based on Integer32"""
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
        *(("all-channels", 3),
          ("full-loop", 2),
          ("no-loop", 1),
          ("only-bchannels", 4))
    )


_PmxIfLoopbackMode_Type.__name__ = "Integer32"
_PmxIfLoopbackMode_Object = MibTableColumn
pmxIfLoopbackMode = _PmxIfLoopbackMode_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 12, 1, 1, 8),
    _PmxIfLoopbackMode_Type()
)
pmxIfLoopbackMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmxIfLoopbackMode.setStatus("mandatory")
_PmxIfErrors_Type = Counter32
_PmxIfErrors_Object = MibTableColumn
pmxIfErrors = _PmxIfErrors_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 12, 1, 1, 9),
    _PmxIfErrors_Type()
)
pmxIfErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmxIfErrors.setStatus("mandatory")


class _PmxIfPortMode_Type(Integer32):
    """Custom type pmxIfPortMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("go-thru", 2),
          ("go-thru-tst", 3),
          ("normal", 1))
    )


_PmxIfPortMode_Type.__name__ = "Integer32"
_PmxIfPortMode_Object = MibTableColumn
pmxIfPortMode = _PmxIfPortMode_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 12, 1, 1, 10),
    _PmxIfPortMode_Type()
)
pmxIfPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmxIfPortMode.setStatus("mandatory")
_PmxIfLOS_Type = Counter32
_PmxIfLOS_Object = MibTableColumn
pmxIfLOS = _PmxIfLOS_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 12, 1, 1, 21),
    _PmxIfLOS_Type()
)
pmxIfLOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmxIfLOS.setStatus("mandatory")
_PmxIfNoFAS_Type = Counter32
_PmxIfNoFAS_Object = MibTableColumn
pmxIfNoFAS = _PmxIfNoFAS_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 12, 1, 1, 22),
    _PmxIfNoFAS_Type()
)
pmxIfNoFAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmxIfNoFAS.setStatus("mandatory")
_PmxIfRemoteAlarms_Type = Counter32
_PmxIfRemoteAlarms_Object = MibTableColumn
pmxIfRemoteAlarms = _PmxIfRemoteAlarms_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 12, 1, 1, 23),
    _PmxIfRemoteAlarms_Type()
)
pmxIfRemoteAlarms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmxIfRemoteAlarms.setStatus("mandatory")
_PmxIfAlarmInds_Type = Counter32
_PmxIfAlarmInds_Object = MibTableColumn
pmxIfAlarmInds = _PmxIfAlarmInds_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 12, 1, 1, 24),
    _PmxIfAlarmInds_Type()
)
pmxIfAlarmInds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmxIfAlarmInds.setStatus("mandatory")
_PmxIfCRC4Errors_Type = Counter32
_PmxIfCRC4Errors_Object = MibTableColumn
pmxIfCRC4Errors = _PmxIfCRC4Errors_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 12, 1, 1, 25),
    _PmxIfCRC4Errors_Type()
)
pmxIfCRC4Errors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmxIfCRC4Errors.setStatus("mandatory")
_PmxIfSlipPositive_Type = Counter32
_PmxIfSlipPositive_Object = MibScalar
pmxIfSlipPositive = _PmxIfSlipPositive_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 12, 1, 1, 26),
    _PmxIfSlipPositive_Type()
)
pmxIfSlipPositive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmxIfSlipPositive.setStatus("mandatory")
_PmxIfSlipNegative_Type = Counter32
_PmxIfSlipNegative_Object = MibScalar
pmxIfSlipNegative = _PmxIfSlipNegative_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 12, 1, 1, 27),
    _PmxIfSlipNegative_Type()
)
pmxIfSlipNegative.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmxIfSlipNegative.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BIANCA-BRICK-PMX-MIB",
    **{"Date": Date,
       "HexValue": HexValue,
       "org": org,
       "dod": dod,
       "internet": internet,
       "private": private,
       "enterprises": enterprises,
       "bintec": bintec,
       "bibo": bibo,
       "pmx": pmx,
       "pmxIfTable": pmxIfTable,
       "pmxIfEntry": pmxIfEntry,
       "pmxIfIndex": pmxIfIndex,
       "pmxIfSelftest": pmxIfSelftest,
       "pmxIfLayer1State": pmxIfLayer1State,
       "pmxIfLayer1Mode": pmxIfLayer1Mode,
       "pmxIfLayer1Framing": pmxIfLayer1Framing,
       "pmxIfLayer1LineCode": pmxIfLayer1LineCode,
       "pmxIfChannelMode": pmxIfChannelMode,
       "pmxIfLoopbackMode": pmxIfLoopbackMode,
       "pmxIfErrors": pmxIfErrors,
       "pmxIfPortMode": pmxIfPortMode,
       "pmxIfLOS": pmxIfLOS,
       "pmxIfNoFAS": pmxIfNoFAS,
       "pmxIfRemoteAlarms": pmxIfRemoteAlarms,
       "pmxIfAlarmInds": pmxIfAlarmInds,
       "pmxIfCRC4Errors": pmxIfCRC4Errors,
       "pmxIfSlipPositive": pmxIfSlipPositive,
       "pmxIfSlipNegative": pmxIfSlipNegative}
)
