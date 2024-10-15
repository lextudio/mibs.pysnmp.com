# SNMP MIB module (NMC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NMC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:27:35 2024
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
 experimental,
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
    "experimental",
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

_Usr_ObjectIdentity = ObjectIdentity
usr = _Usr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429)
)
_Nas_ObjectIdentity = ObjectIdentity
nas = _Nas_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1)
)
_Nmc_ObjectIdentity = ObjectIdentity
nmc = _Nmc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 2)
)
_NmcCfg_ObjectIdentity = ObjectIdentity
nmcCfg = _NmcCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 1)
)


class _NmcCfgSystemTime_Type(DisplayString):
    """Custom type nmcCfgSystemTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_NmcCfgSystemTime_Type.__name__ = "DisplayString"
_NmcCfgSystemTime_Object = MibScalar
nmcCfgSystemTime = _NmcCfgSystemTime_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 1, 1),
    _NmcCfgSystemTime_Type()
)
nmcCfgSystemTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmcCfgSystemTime.setStatus("mandatory")


class _NmcCfgSystemDate_Type(DisplayString):
    """Custom type nmcCfgSystemDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_NmcCfgSystemDate_Type.__name__ = "DisplayString"
_NmcCfgSystemDate_Object = MibScalar
nmcCfgSystemDate = _NmcCfgSystemDate_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 1, 2),
    _NmcCfgSystemDate_Type()
)
nmcCfgSystemDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmcCfgSystemDate.setStatus("mandatory")
_NmcGmtime_Type = Integer32
_NmcGmtime_Object = MibScalar
nmcGmtime = _NmcGmtime_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 1, 3),
    _NmcGmtime_Type()
)
nmcGmtime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmcGmtime.setStatus("mandatory")


class _NmcTimezone_Type(Integer32):
    """Custom type nmcTimezone based on Integer32"""
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
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30)
        )
    )
    namedValues = NamedValues(
        *(("adelaide-gmtPlus9-30", 30),
          ("bombay-gmtPlus5-30", 29),
          ("centralUSA-gmtMinus6", 2),
          ("easternUSA-gmtMinus5", 1),
          ("gmt", 21),
          ("gmtMinus1", 22),
          ("gmtMinus10", 6),
          ("gmtMinus11", 7),
          ("gmtMinus12", 8),
          ("gmtMinus2", 23),
          ("gmtMinus3", 24),
          ("gmtMinus4", 25),
          ("gmtMinus9", 5),
          ("gmtPlus1", 20),
          ("gmtPlus10", 11),
          ("gmtPlus11", 10),
          ("gmtPlus12", 9),
          ("gmtPlus2", 19),
          ("gmtPlus3", 18),
          ("gmtPlus4", 17),
          ("gmtPlus5", 16),
          ("gmtPlus6", 15),
          ("gmtPlus7", 14),
          ("gmtPlus8", 13),
          ("gmtPlus9", 12),
          ("kabul-gmtPlus4-30", 28),
          ("mountainUSA-gmtMinus7", 3),
          ("newfoundland-gmtMinus3-30", 26),
          ("pacificUSA-gmtMinus8", 4),
          ("tehran-gmtPlus3-30", 27))
    )


_NmcTimezone_Type.__name__ = "Integer32"
_NmcTimezone_Object = MibScalar
nmcTimezone = _NmcTimezone_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 1, 4),
    _NmcTimezone_Type()
)
nmcTimezone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmcTimezone.setStatus("mandatory")


class _NmcCfgAuthFailTrapEnable_Type(Integer32):
    """Custom type nmcCfgAuthFailTrapEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_NmcCfgAuthFailTrapEnable_Type.__name__ = "Integer32"
_NmcCfgAuthFailTrapEnable_Object = MibScalar
nmcCfgAuthFailTrapEnable = _NmcCfgAuthFailTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 1, 5),
    _NmcCfgAuthFailTrapEnable_Type()
)
nmcCfgAuthFailTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmcCfgAuthFailTrapEnable.setStatus("mandatory")


class _NmcDaySavingTime_Type(Integer32):
    """Custom type nmcDaySavingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_NmcDaySavingTime_Type.__name__ = "Integer32"
_NmcDaySavingTime_Object = MibScalar
nmcDaySavingTime = _NmcDaySavingTime_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 1, 6),
    _NmcDaySavingTime_Type()
)
nmcDaySavingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmcDaySavingTime.setStatus("mandatory")


class _NmcCfgWanDialOutPhoneNum_Type(DisplayString):
    """Custom type nmcCfgWanDialOutPhoneNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 39),
    )


_NmcCfgWanDialOutPhoneNum_Type.__name__ = "DisplayString"
_NmcCfgWanDialOutPhoneNum_Object = MibScalar
nmcCfgWanDialOutPhoneNum = _NmcCfgWanDialOutPhoneNum_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 1, 7),
    _NmcCfgWanDialOutPhoneNum_Type()
)
nmcCfgWanDialOutPhoneNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmcCfgWanDialOutPhoneNum.setStatus("mandatory")


class _NmcCfgAtString_Type(DisplayString):
    """Custom type nmcCfgAtString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 39),
    )


_NmcCfgAtString_Type.__name__ = "DisplayString"
_NmcCfgAtString_Object = MibScalar
nmcCfgAtString = _NmcCfgAtString_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 1, 8),
    _NmcCfgAtString_Type()
)
nmcCfgAtString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmcCfgAtString.setStatus("mandatory")


class _NmcPowerUpAutoCfgEnable_Type(Integer32):
    """Custom type nmcPowerUpAutoCfgEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_NmcPowerUpAutoCfgEnable_Type.__name__ = "Integer32"
_NmcPowerUpAutoCfgEnable_Object = MibScalar
nmcPowerUpAutoCfgEnable = _NmcPowerUpAutoCfgEnable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 1, 9),
    _NmcPowerUpAutoCfgEnable_Type()
)
nmcPowerUpAutoCfgEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmcPowerUpAutoCfgEnable.setStatus("mandatory")


class _NmcCfgNumWanRetries_Type(Integer32):
    """Custom type nmcCfgNumWanRetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_NmcCfgNumWanRetries_Type.__name__ = "Integer32"
_NmcCfgNumWanRetries_Object = MibScalar
nmcCfgNumWanRetries = _NmcCfgNumWanRetries_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 1, 10),
    _NmcCfgNumWanRetries_Type()
)
nmcCfgNumWanRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmcCfgNumWanRetries.setStatus("mandatory")


class _NmcCfgWanRetryPause_Type(Integer32):
    """Custom type nmcCfgWanRetryPause based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 120),
    )


_NmcCfgWanRetryPause_Type.__name__ = "Integer32"
_NmcCfgWanRetryPause_Object = MibScalar
nmcCfgWanRetryPause = _NmcCfgWanRetryPause_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 1, 11),
    _NmcCfgWanRetryPause_Type()
)
nmcCfgWanRetryPause.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmcCfgWanRetryPause.setStatus("mandatory")


class _NmcCfgWanRetrySuspendTime_Type(Integer32):
    """Custom type nmcCfgWanRetrySuspendTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 300),
    )


_NmcCfgWanRetrySuspendTime_Type.__name__ = "Integer32"
_NmcCfgWanRetrySuspendTime_Object = MibScalar
nmcCfgWanRetrySuspendTime = _NmcCfgWanRetrySuspendTime_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 1, 12),
    _NmcCfgWanRetrySuspendTime_Type()
)
nmcCfgWanRetrySuspendTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmcCfgWanRetrySuspendTime.setStatus("mandatory")


class _NmcCfgNumFailBefSuspend_Type(Integer32):
    """Custom type nmcCfgNumFailBefSuspend based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
    )


_NmcCfgNumFailBefSuspend_Type.__name__ = "Integer32"
_NmcCfgNumFailBefSuspend_Object = MibScalar
nmcCfgNumFailBefSuspend = _NmcCfgNumFailBefSuspend_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 1, 13),
    _NmcCfgNumFailBefSuspend_Type()
)
nmcCfgNumFailBefSuspend.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmcCfgNumFailBefSuspend.setStatus("mandatory")


class _NmcCfgLogSrvrSelect_Type(Integer32):
    """Custom type nmcCfgLogSrvrSelect based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("eighth", 9),
          ("fifth", 6),
          ("fourth", 5),
          ("none", 3),
          ("primary", 1),
          ("secondary", 2),
          ("seventh", 8),
          ("sixth", 7),
          ("third", 4))
    )


_NmcCfgLogSrvrSelect_Type.__name__ = "Integer32"
_NmcCfgLogSrvrSelect_Object = MibScalar
nmcCfgLogSrvrSelect = _NmcCfgLogSrvrSelect_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 1, 14),
    _NmcCfgLogSrvrSelect_Type()
)
nmcCfgLogSrvrSelect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmcCfgLogSrvrSelect.setStatus("mandatory")
_NmcCfgLogPriSrvrAddr_Type = IpAddress
_NmcCfgLogPriSrvrAddr_Object = MibScalar
nmcCfgLogPriSrvrAddr = _NmcCfgLogPriSrvrAddr_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 1, 15),
    _NmcCfgLogPriSrvrAddr_Type()
)
nmcCfgLogPriSrvrAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmcCfgLogPriSrvrAddr.setStatus("mandatory")
_NmcCfgLogSecSrvrAddr_Type = IpAddress
_NmcCfgLogSecSrvrAddr_Object = MibScalar
nmcCfgLogSecSrvrAddr = _NmcCfgLogSecSrvrAddr_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 1, 16),
    _NmcCfgLogSecSrvrAddr_Type()
)
nmcCfgLogSecSrvrAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmcCfgLogSecSrvrAddr.setStatus("mandatory")


class _NmcCfgLogUdpPortNum_Type(Integer32):
    """Custom type nmcCfgLogUdpPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NmcCfgLogUdpPortNum_Type.__name__ = "Integer32"
_NmcCfgLogUdpPortNum_Object = MibScalar
nmcCfgLogUdpPortNum = _NmcCfgLogUdpPortNum_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 1, 17),
    _NmcCfgLogUdpPortNum_Type()
)
nmcCfgLogUdpPortNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmcCfgLogUdpPortNum.setStatus("mandatory")


class _NmcCfgLogRetryCnt_Type(Integer32):
    """Custom type nmcCfgLogRetryCnt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_NmcCfgLogRetryCnt_Type.__name__ = "Integer32"
_NmcCfgLogRetryCnt_Object = MibScalar
nmcCfgLogRetryCnt = _NmcCfgLogRetryCnt_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 1, 18),
    _NmcCfgLogRetryCnt_Type()
)
nmcCfgLogRetryCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmcCfgLogRetryCnt.setStatus("mandatory")


class _NmcCfgLogCallStatGrpSel_Type(Integer32):
    """Custom type nmcCfgLogCallStatGrpSel based on Integer32"""
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
              10,
              11,
              12,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("group2", 2),
          ("group23", 5),
          ("group234", 8),
          ("group2345", 16),
          ("group235", 13),
          ("group24", 6),
          ("group245", 14),
          ("group25", 10),
          ("group3", 3),
          ("group34", 7),
          ("group345", 15),
          ("group35", 11),
          ("group4", 4),
          ("group45", 12),
          ("group5", 9),
          ("none", 1))
    )


_NmcCfgLogCallStatGrpSel_Type.__name__ = "Integer32"
_NmcCfgLogCallStatGrpSel_Object = MibScalar
nmcCfgLogCallStatGrpSel = _NmcCfgLogCallStatGrpSel_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 1, 19),
    _NmcCfgLogCallStatGrpSel_Type()
)
nmcCfgLogCallStatGrpSel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmcCfgLogCallStatGrpSel.setStatus("mandatory")


class _NmcCfgLogMD5Calc_Type(Integer32):
    """Custom type nmcCfgLogMD5Calc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_NmcCfgLogMD5Calc_Type.__name__ = "Integer32"
_NmcCfgLogMD5Calc_Object = MibScalar
nmcCfgLogMD5Calc = _NmcCfgLogMD5Calc_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 1, 20),
    _NmcCfgLogMD5Calc_Type()
)
nmcCfgLogMD5Calc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmcCfgLogMD5Calc.setStatus("optional")


class _NmcCfgTFTPTimeout_Type(Integer32):
    """Custom type nmcCfgTFTPTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_NmcCfgTFTPTimeout_Type.__name__ = "Integer32"
_NmcCfgTFTPTimeout_Object = MibScalar
nmcCfgTFTPTimeout = _NmcCfgTFTPTimeout_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 1, 21),
    _NmcCfgTFTPTimeout_Type()
)
nmcCfgTFTPTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmcCfgTFTPTimeout.setStatus("mandatory")
_NmcCfgDnsPriSrvrAddr_Type = IpAddress
_NmcCfgDnsPriSrvrAddr_Object = MibScalar
nmcCfgDnsPriSrvrAddr = _NmcCfgDnsPriSrvrAddr_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 1, 22),
    _NmcCfgDnsPriSrvrAddr_Type()
)
nmcCfgDnsPriSrvrAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmcCfgDnsPriSrvrAddr.setStatus("mandatory")
_NmcCfgDnsSecSrvrAddr_Type = IpAddress
_NmcCfgDnsSecSrvrAddr_Object = MibScalar
nmcCfgDnsSecSrvrAddr = _NmcCfgDnsSecSrvrAddr_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 1, 23),
    _NmcCfgDnsSecSrvrAddr_Type()
)
nmcCfgDnsSecSrvrAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmcCfgDnsSecSrvrAddr.setStatus("mandatory")
_NmcCfgLog3SrvrAddr_Type = IpAddress
_NmcCfgLog3SrvrAddr_Object = MibScalar
nmcCfgLog3SrvrAddr = _NmcCfgLog3SrvrAddr_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 1, 24),
    _NmcCfgLog3SrvrAddr_Type()
)
nmcCfgLog3SrvrAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmcCfgLog3SrvrAddr.setStatus("mandatory")
_NmcCfgLog4SrvrAddr_Type = IpAddress
_NmcCfgLog4SrvrAddr_Object = MibScalar
nmcCfgLog4SrvrAddr = _NmcCfgLog4SrvrAddr_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 1, 25),
    _NmcCfgLog4SrvrAddr_Type()
)
nmcCfgLog4SrvrAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmcCfgLog4SrvrAddr.setStatus("mandatory")
_NmcCfgLog5SrvrAddr_Type = IpAddress
_NmcCfgLog5SrvrAddr_Object = MibScalar
nmcCfgLog5SrvrAddr = _NmcCfgLog5SrvrAddr_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 1, 26),
    _NmcCfgLog5SrvrAddr_Type()
)
nmcCfgLog5SrvrAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmcCfgLog5SrvrAddr.setStatus("mandatory")
_NmcCfgLog6SrvrAddr_Type = IpAddress
_NmcCfgLog6SrvrAddr_Object = MibScalar
nmcCfgLog6SrvrAddr = _NmcCfgLog6SrvrAddr_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 1, 27),
    _NmcCfgLog6SrvrAddr_Type()
)
nmcCfgLog6SrvrAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmcCfgLog6SrvrAddr.setStatus("mandatory")
_NmcCfgLog7SrvrAddr_Type = IpAddress
_NmcCfgLog7SrvrAddr_Object = MibScalar
nmcCfgLog7SrvrAddr = _NmcCfgLog7SrvrAddr_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 1, 28),
    _NmcCfgLog7SrvrAddr_Type()
)
nmcCfgLog7SrvrAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmcCfgLog7SrvrAddr.setStatus("mandatory")
_NmcCfgLog8SrvrAddr_Type = IpAddress
_NmcCfgLog8SrvrAddr_Object = MibScalar
nmcCfgLog8SrvrAddr = _NmcCfgLog8SrvrAddr_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 1, 29),
    _NmcCfgLog8SrvrAddr_Type()
)
nmcCfgLog8SrvrAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmcCfgLog8SrvrAddr.setStatus("mandatory")


class _NmcCfgLogSrvrName_Type(DisplayString):
    """Custom type nmcCfgLogSrvrName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_NmcCfgLogSrvrName_Type.__name__ = "DisplayString"
_NmcCfgLogSrvrName_Object = MibScalar
nmcCfgLogSrvrName = _NmcCfgLogSrvrName_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 1, 30),
    _NmcCfgLogSrvrName_Type()
)
nmcCfgLogSrvrName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmcCfgLogSrvrName.setStatus("mandatory")


class _NmcCfgDnsRetryCnt_Type(Integer32):
    """Custom type nmcCfgDnsRetryCnt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_NmcCfgDnsRetryCnt_Type.__name__ = "Integer32"
_NmcCfgDnsRetryCnt_Object = MibScalar
nmcCfgDnsRetryCnt = _NmcCfgDnsRetryCnt_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 1, 31),
    _NmcCfgDnsRetryCnt_Type()
)
nmcCfgDnsRetryCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmcCfgDnsRetryCnt.setStatus("mandatory")


class _NmcCfgDnsUdpPortNum_Type(Integer32):
    """Custom type nmcCfgDnsUdpPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NmcCfgDnsUdpPortNum_Type.__name__ = "Integer32"
_NmcCfgDnsUdpPortNum_Object = MibScalar
nmcCfgDnsUdpPortNum = _NmcCfgDnsUdpPortNum_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 1, 32),
    _NmcCfgDnsUdpPortNum_Type()
)
nmcCfgDnsUdpPortNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmcCfgDnsUdpPortNum.setStatus("mandatory")


class _NmcCfgDnsSrvrSelect_Type(Integer32):
    """Custom type nmcCfgDnsSrvrSelect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("primary", 2),
          ("secondary", 3))
    )


_NmcCfgDnsSrvrSelect_Type.__name__ = "Integer32"
_NmcCfgDnsSrvrSelect_Object = MibScalar
nmcCfgDnsSrvrSelect = _NmcCfgDnsSrvrSelect_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 1, 33),
    _NmcCfgDnsSrvrSelect_Type()
)
nmcCfgDnsSrvrSelect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmcCfgDnsSrvrSelect.setStatus("mandatory")


class _NmcCfgLogDnsEna_Type(Integer32):
    """Custom type nmcCfgLogDnsEna based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_NmcCfgLogDnsEna_Type.__name__ = "Integer32"
_NmcCfgLogDnsEna_Object = MibScalar
nmcCfgLogDnsEna = _NmcCfgLogDnsEna_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 1, 34),
    _NmcCfgLogDnsEna_Type()
)
nmcCfgLogDnsEna.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmcCfgLogDnsEna.setStatus("mandatory")


class _NmcCfgLogStatusInterval_Type(Integer32):
    """Custom type nmcCfgLogStatusInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 65535),
    )


_NmcCfgLogStatusInterval_Type.__name__ = "Integer32"
_NmcCfgLogStatusInterval_Object = MibScalar
nmcCfgLogStatusInterval = _NmcCfgLogStatusInterval_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 1, 35),
    _NmcCfgLogStatusInterval_Type()
)
nmcCfgLogStatusInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmcCfgLogStatusInterval.setStatus("mandatory")


class _NmcCfgDnsSrvrFailure_Type(Integer32):
    """Custom type nmcCfgDnsSrvrFailure based on Integer32"""
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
        *(("commFailure", 3),
          ("invalidEntry", 4),
          ("none", 1),
          ("other", 2))
    )


_NmcCfgDnsSrvrFailure_Type.__name__ = "Integer32"
_NmcCfgDnsSrvrFailure_Object = MibScalar
nmcCfgDnsSrvrFailure = _NmcCfgDnsSrvrFailure_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 1, 36),
    _NmcCfgDnsSrvrFailure_Type()
)
nmcCfgDnsSrvrFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmcCfgDnsSrvrFailure.setStatus("mandatory")


class _NmcCfgLogSrvrFailure_Type(Integer32):
    """Custom type nmcCfgLogSrvrFailure based on Integer32"""
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
        *(("commFailure", 3),
          ("disabledServer", 5),
          ("invalidResponse", 4),
          ("none", 1),
          ("other", 2))
    )


_NmcCfgLogSrvrFailure_Type.__name__ = "Integer32"
_NmcCfgLogSrvrFailure_Object = MibScalar
nmcCfgLogSrvrFailure = _NmcCfgLogSrvrFailure_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 1, 37),
    _NmcCfgLogSrvrFailure_Type()
)
nmcCfgLogSrvrFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmcCfgLogSrvrFailure.setStatus("mandatory")


class _NmcCfgSessionIDNewFmt_Type(Integer32):
    """Custom type nmcCfgSessionIDNewFmt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_NmcCfgSessionIDNewFmt_Type.__name__ = "Integer32"
_NmcCfgSessionIDNewFmt_Object = MibScalar
nmcCfgSessionIDNewFmt = _NmcCfgSessionIDNewFmt_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 1, 38),
    _NmcCfgSessionIDNewFmt_Type()
)
nmcCfgSessionIDNewFmt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmcCfgSessionIDNewFmt.setStatus("optional")
_NmcStat_ObjectIdentity = ObjectIdentity
nmcStat = _NmcStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 2)
)


class _NmcStatStatus_Type(Integer32):
    """Custom type nmcStatStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("nonCriticalFailure", 3),
          ("ok", 2),
          ("other", 1))
    )


_NmcStatStatus_Type.__name__ = "Integer32"
_NmcStatStatus_Object = MibScalar
nmcStatStatus = _NmcStatStatus_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 2, 1),
    _NmcStatStatus_Type()
)
nmcStatStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmcStatStatus.setStatus("mandatory")
_NmcStatDramInstalled_Type = Integer32
_NmcStatDramInstalled_Object = MibScalar
nmcStatDramInstalled = _NmcStatDramInstalled_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 2, 2),
    _NmcStatDramInstalled_Type()
)
nmcStatDramInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmcStatDramInstalled.setStatus("mandatory")
_NmcStatNVRAMInstalled_Type = Integer32
_NmcStatNVRAMInstalled_Object = MibScalar
nmcStatNVRAMInstalled = _NmcStatNVRAMInstalled_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 2, 3),
    _NmcStatNVRAMInstalled_Type()
)
nmcStatNVRAMInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmcStatNVRAMInstalled.setStatus("mandatory")
_NmcStatEventId_Type = Integer32
_NmcStatEventId_Object = MibScalar
nmcStatEventId = _NmcStatEventId_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 2, 4),
    _NmcStatEventId_Type()
)
nmcStatEventId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmcStatEventId.setStatus("mandatory")
_NmcStatTemperature_Type = Integer32
_NmcStatTemperature_Object = MibScalar
nmcStatTemperature = _NmcStatTemperature_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 2, 5),
    _NmcStatTemperature_Type()
)
nmcStatTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmcStatTemperature.setStatus("optional")
_NmcStatPowerUpTstFailures_Type = Counter32
_NmcStatPowerUpTstFailures_Object = MibScalar
nmcStatPowerUpTstFailures = _NmcStatPowerUpTstFailures_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 2, 6),
    _NmcStatPowerUpTstFailures_Type()
)
nmcStatPowerUpTstFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmcStatPowerUpTstFailures.setStatus("mandatory")
_NmcStatPowerUpTstFailBMap_Type = Integer32
_NmcStatPowerUpTstFailBMap_Object = MibScalar
nmcStatPowerUpTstFailBMap = _NmcStatPowerUpTstFailBMap_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 2, 7),
    _NmcStatPowerUpTstFailBMap_Type()
)
nmcStatPowerUpTstFailBMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmcStatPowerUpTstFailBMap.setStatus("mandatory")
_NmcStatTestResult_Type = Integer32
_NmcStatTestResult_Object = MibScalar
nmcStatTestResult = _NmcStatTestResult_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 2, 8),
    _NmcStatTestResult_Type()
)
nmcStatTestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmcStatTestResult.setStatus("mandatory")


class _NmcStatCompSwVer_Type(DisplayString):
    """Custom type nmcStatCompSwVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 9),
    )


_NmcStatCompSwVer_Type.__name__ = "DisplayString"
_NmcStatCompSwVer_Object = MibScalar
nmcStatCompSwVer = _NmcStatCompSwVer_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 2, 9),
    _NmcStatCompSwVer_Type()
)
nmcStatCompSwVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmcStatCompSwVer.setStatus("mandatory")


class _NmcStatPktBusClkSrc_Type(Integer32):
    """Custom type nmcStatPktBusClkSrc based on Integer32"""
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
        *(("backplaneActive", 2),
          ("backplaneActive1ClkFail", 3),
          ("nmcActive", 4),
          ("notApplicable", 1))
    )


_NmcStatPktBusClkSrc_Type.__name__ = "Integer32"
_NmcStatPktBusClkSrc_Object = MibScalar
nmcStatPktBusClkSrc = _NmcStatPktBusClkSrc_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 2, 10),
    _NmcStatPktBusClkSrc_Type()
)
nmcStatPktBusClkSrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmcStatPktBusClkSrc.setStatus("optional")


class _NmcStatNmcPktBusClk_Type(Integer32):
    """Custom type nmcStatNmcPktBusClk based on Integer32"""
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
        *(("active", 3),
          ("available", 2),
          ("failed", 4),
          ("notApplicable", 1))
    )


_NmcStatNmcPktBusClk_Type.__name__ = "Integer32"
_NmcStatNmcPktBusClk_Object = MibScalar
nmcStatNmcPktBusClk = _NmcStatNmcPktBusClk_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 2, 11),
    _NmcStatNmcPktBusClk_Type()
)
nmcStatNmcPktBusClk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmcStatNmcPktBusClk.setStatus("optional")


class _NmcStatRedLed_Type(Integer32):
    """Custom type nmcStatRedLed based on Integer32"""
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
        *(("chassisFanFailure", 3),
          ("chassisTemperatureHigh", 2),
          ("failureofPSU", 5),
          ("incompatibleTokenRingNIC", 8),
          ("interfaceCardFailure", 7),
          ("managementBusFailure", 6),
          ("none", 1),
          ("voltageWarningforPSU", 4))
    )


_NmcStatRedLed_Type.__name__ = "Integer32"
_NmcStatRedLed_Object = MibScalar
nmcStatRedLed = _NmcStatRedLed_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 2, 12),
    _NmcStatRedLed_Type()
)
nmcStatRedLed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmcStatRedLed.setStatus("optional")


class _NmcAuxIn1Sts_Type(Integer32):
    """Custom type nmcAuxIn1Sts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("portClosed", 2),
          ("portNotApplicable", 3),
          ("portOpen", 1))
    )


_NmcAuxIn1Sts_Type.__name__ = "Integer32"
_NmcAuxIn1Sts_Object = MibScalar
nmcAuxIn1Sts = _NmcAuxIn1Sts_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 2, 13),
    _NmcAuxIn1Sts_Type()
)
nmcAuxIn1Sts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmcAuxIn1Sts.setStatus("mandatory")


class _NmcAuxIn2Sts_Type(Integer32):
    """Custom type nmcAuxIn2Sts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("portClosed", 2),
          ("portNotApplicable", 3),
          ("portOpen", 1))
    )


_NmcAuxIn2Sts_Type.__name__ = "Integer32"
_NmcAuxIn2Sts_Object = MibScalar
nmcAuxIn2Sts = _NmcAuxIn2Sts_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 2, 14),
    _NmcAuxIn2Sts_Type()
)
nmcAuxIn2Sts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmcAuxIn2Sts.setStatus("mandatory")


class _NmcAuxOut1Sts_Type(Integer32):
    """Custom type nmcAuxOut1Sts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("portClosed", 2),
          ("portNotApplicable", 3),
          ("portOpen", 1))
    )


_NmcAuxOut1Sts_Type.__name__ = "Integer32"
_NmcAuxOut1Sts_Object = MibScalar
nmcAuxOut1Sts = _NmcAuxOut1Sts_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 2, 15),
    _NmcAuxOut1Sts_Type()
)
nmcAuxOut1Sts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmcAuxOut1Sts.setStatus("mandatory")


class _NmcAuxOut2Sts_Type(Integer32):
    """Custom type nmcAuxOut2Sts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("portClosed", 2),
          ("portNotApplicable", 3),
          ("portOpen", 1))
    )


_NmcAuxOut2Sts_Type.__name__ = "Integer32"
_NmcAuxOut2Sts_Object = MibScalar
nmcAuxOut2Sts = _NmcAuxOut2Sts_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 2, 16),
    _NmcAuxOut2Sts_Type()
)
nmcAuxOut2Sts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmcAuxOut2Sts.setStatus("mandatory")
_NmcTrap_ObjectIdentity = ObjectIdentity
nmcTrap = _NmcTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 3)
)
_NmcTrapSequenceNumber_Type = Integer32
_NmcTrapSequenceNumber_Object = MibScalar
nmcTrapSequenceNumber = _NmcTrapSequenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 3, 1),
    _NmcTrapSequenceNumber_Type()
)
nmcTrapSequenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmcTrapSequenceNumber.setStatus("mandatory")
_NmcTrapDestTable_Object = MibTable
nmcTrapDestTable = _NmcTrapDestTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 3, 2)
)
if mibBuilder.loadTexts:
    nmcTrapDestTable.setStatus("mandatory")
_NmcTrapDestEntry_Object = MibTableRow
nmcTrapDestEntry = _NmcTrapDestEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 3, 2, 1)
)
nmcTrapDestEntry.setIndexNames(
    (0, "NMC-MIB", "nmcTrapDestIP"),
)
if mibBuilder.loadTexts:
    nmcTrapDestEntry.setStatus("mandatory")
_NmcTrapDestIP_Type = IpAddress
_NmcTrapDestIP_Object = MibTableColumn
nmcTrapDestIP = _NmcTrapDestIP_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 3, 2, 1, 1),
    _NmcTrapDestIP_Type()
)
nmcTrapDestIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmcTrapDestIP.setStatus("mandatory")


class _NmcTrapDestCommunity_Type(OctetString):
    """Custom type nmcTrapDestCommunity based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_NmcTrapDestCommunity_Type.__name__ = "OctetString"
_NmcTrapDestCommunity_Object = MibTableColumn
nmcTrapDestCommunity = _NmcTrapDestCommunity_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 3, 2, 1, 2),
    _NmcTrapDestCommunity_Type()
)
nmcTrapDestCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmcTrapDestCommunity.setStatus("mandatory")


class _NmcTrapDestDescr_Type(DisplayString):
    """Custom type nmcTrapDestDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_NmcTrapDestDescr_Type.__name__ = "DisplayString"
_NmcTrapDestDescr_Object = MibTableColumn
nmcTrapDestDescr = _NmcTrapDestDescr_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 3, 2, 1, 3),
    _NmcTrapDestDescr_Type()
)
nmcTrapDestDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmcTrapDestDescr.setStatus("mandatory")


class _NmcArTrapId_Type(Integer32):
    """Custom type nmcArTrapId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_NmcArTrapId_Type.__name__ = "Integer32"
_NmcArTrapId_Object = MibScalar
nmcArTrapId = _NmcArTrapId_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 3, 3),
    _NmcArTrapId_Type()
)
nmcArTrapId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmcArTrapId.setStatus("optional")
_NmcCmd_ObjectIdentity = ObjectIdentity
nmcCmd = _NmcCmd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 4)
)


class _NmcCmdMgtStationId_Type(OctetString):
    """Custom type nmcCmdMgtStationId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_NmcCmdMgtStationId_Type.__name__ = "OctetString"
_NmcCmdMgtStationId_Object = MibScalar
nmcCmdMgtStationId = _NmcCmdMgtStationId_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 4, 1),
    _NmcCmdMgtStationId_Type()
)
nmcCmdMgtStationId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmcCmdMgtStationId.setStatus("mandatory")
_NmcCmdReqId_Type = Integer32
_NmcCmdReqId_Object = MibScalar
nmcCmdReqId = _NmcCmdReqId_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 4, 2),
    _NmcCmdReqId_Type()
)
nmcCmdReqId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmcCmdReqId.setStatus("mandatory")


class _NmcCmdFunction_Type(Integer32):
    """Custom type nmcCmdFunction based on Integer32"""
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
              10,
              11,
              12,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("bulkFileDownload", 11),
          ("bulkFileUpload", 10),
          ("closeAuxOutputPort1", 14),
          ("closeAuxOutputPort2", 15),
          ("noCommand", 1),
          ("nonDisruptSelfTest", 5),
          ("openAuxOutputPort1", 12),
          ("openAuxOutputPort2", 13),
          ("restoreFromDefaults", 3),
          ("restoreFromNvram", 4),
          ("restoreNmcFromDefaults", 8),
          ("restoreNmcFromNvram", 9),
          ("saveToNvram", 2),
          ("saveUiParmsToEEPROM", 7),
          ("softwareReset", 6))
    )


_NmcCmdFunction_Type.__name__ = "Integer32"
_NmcCmdFunction_Object = MibScalar
nmcCmdFunction = _NmcCmdFunction_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 4, 3),
    _NmcCmdFunction_Type()
)
nmcCmdFunction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmcCmdFunction.setStatus("mandatory")


class _NmcCmdForce_Type(Integer32):
    """Custom type nmcCmdForce based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("force", 2),
          ("noForce", 1))
    )


_NmcCmdForce_Type.__name__ = "Integer32"
_NmcCmdForce_Object = MibScalar
nmcCmdForce = _NmcCmdForce_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 4, 4),
    _NmcCmdForce_Type()
)
nmcCmdForce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmcCmdForce.setStatus("mandatory")


class _NmcCmdParam_Type(OctetString):
    """Custom type nmcCmdParam based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_NmcCmdParam_Type.__name__ = "OctetString"
_NmcCmdParam_Object = MibScalar
nmcCmdParam = _NmcCmdParam_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 4, 5),
    _NmcCmdParam_Type()
)
nmcCmdParam.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmcCmdParam.setStatus("mandatory")


class _NmcCmdResult_Type(Integer32):
    """Custom type nmcCmdResult based on Integer32"""
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
        *(("aborted", 6),
          ("failed", 7),
          ("inProgress", 3),
          ("none", 1),
          ("notSupported", 4),
          ("success", 2),
          ("unAbleToRun", 5))
    )


_NmcCmdResult_Type.__name__ = "Integer32"
_NmcCmdResult_Object = MibScalar
nmcCmdResult = _NmcCmdResult_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 4, 6),
    _NmcCmdResult_Type()
)
nmcCmdResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmcCmdResult.setStatus("mandatory")


class _NmcCmdCode_Type(Integer32):
    """Custom type nmcCmdCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              5,
              6,
              8,
              20,
              25,
              27,
              63,
              72,
              73,
              81,
              86,
              88,
              93,
              115)
        )
    )
    namedValues = NamedValues(
        *(("badCRC", 72),
          ("erasingFlash", 81),
          ("erasingFlashError", 63),
          ("fileTransferInProgress", 93),
          ("fileTransferTimedOut", 86),
          ("noError", 1),
          ("nvramAccessConflict", 27),
          ("pendingFileTransfer", 115),
          ("pendingSoftwareDownload", 73),
          ("slotEmpty", 8),
          ("testFailed", 25),
          ("unable", 2),
          ("unrecognizedCommand", 6),
          ("unrecognizedData", 5),
          ("unrecognizedFile", 88),
          ("unsupportedCommand", 20))
    )


_NmcCmdCode_Type.__name__ = "Integer32"
_NmcCmdCode_Object = MibScalar
nmcCmdCode = _NmcCmdCode_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 4, 7),
    _NmcCmdCode_Type()
)
nmcCmdCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmcCmdCode.setStatus("mandatory")
_NmcHs_ObjectIdentity = ObjectIdentity
nmcHs = _NmcHs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 6)
)


class _NmcHsDialInOutNamePrompt_Type(DisplayString):
    """Custom type nmcHsDialInOutNamePrompt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_NmcHsDialInOutNamePrompt_Type.__name__ = "DisplayString"
_NmcHsDialInOutNamePrompt_Object = MibScalar
nmcHsDialInOutNamePrompt = _NmcHsDialInOutNamePrompt_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 6, 1),
    _NmcHsDialInOutNamePrompt_Type()
)
nmcHsDialInOutNamePrompt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmcHsDialInOutNamePrompt.setStatus("optional")


class _NmcHsDialInOutPsswdPrompt_Type(DisplayString):
    """Custom type nmcHsDialInOutPsswdPrompt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_NmcHsDialInOutPsswdPrompt_Type.__name__ = "DisplayString"
_NmcHsDialInOutPsswdPrompt_Object = MibScalar
nmcHsDialInOutPsswdPrompt = _NmcHsDialInOutPsswdPrompt_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 6, 2),
    _NmcHsDialInOutPsswdPrompt_Type()
)
nmcHsDialInOutPsswdPrompt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmcHsDialInOutPsswdPrompt.setStatus("optional")


class _NmcHsDialBackNamePrompt_Type(DisplayString):
    """Custom type nmcHsDialBackNamePrompt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_NmcHsDialBackNamePrompt_Type.__name__ = "DisplayString"
_NmcHsDialBackNamePrompt_Object = MibScalar
nmcHsDialBackNamePrompt = _NmcHsDialBackNamePrompt_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 6, 3),
    _NmcHsDialBackNamePrompt_Type()
)
nmcHsDialBackNamePrompt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmcHsDialBackNamePrompt.setStatus("optional")


class _NmcHsDialBackPsswdPrompt_Type(DisplayString):
    """Custom type nmcHsDialBackPsswdPrompt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_NmcHsDialBackPsswdPrompt_Type.__name__ = "DisplayString"
_NmcHsDialBackPsswdPrompt_Object = MibScalar
nmcHsDialBackPsswdPrompt = _NmcHsDialBackPsswdPrompt_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 6, 4),
    _NmcHsDialBackPsswdPrompt_Type()
)
nmcHsDialBackPsswdPrompt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmcHsDialBackPsswdPrompt.setStatus("optional")


class _NmcHsDialBackPhonePrompt_Type(DisplayString):
    """Custom type nmcHsDialBackPhonePrompt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_NmcHsDialBackPhonePrompt_Type.__name__ = "DisplayString"
_NmcHsDialBackPhonePrompt_Object = MibScalar
nmcHsDialBackPhonePrompt = _NmcHsDialBackPhonePrompt_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 6, 5),
    _NmcHsDialBackPhonePrompt_Type()
)
nmcHsDialBackPhonePrompt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmcHsDialBackPhonePrompt.setStatus("optional")


class _NmcHsDialBackPendPrompt_Type(DisplayString):
    """Custom type nmcHsDialBackPendPrompt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_NmcHsDialBackPendPrompt_Type.__name__ = "DisplayString"
_NmcHsDialBackPendPrompt_Object = MibScalar
nmcHsDialBackPendPrompt = _NmcHsDialBackPendPrompt_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 6, 6),
    _NmcHsDialBackPendPrompt_Type()
)
nmcHsDialBackPendPrompt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmcHsDialBackPendPrompt.setStatus("optional")


class _NmcHsMdmSelectPrompt_Type(DisplayString):
    """Custom type nmcHsMdmSelectPrompt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_NmcHsMdmSelectPrompt_Type.__name__ = "DisplayString"
_NmcHsMdmSelectPrompt_Object = MibScalar
nmcHsMdmSelectPrompt = _NmcHsMdmSelectPrompt_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 6, 7),
    _NmcHsMdmSelectPrompt_Type()
)
nmcHsMdmSelectPrompt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmcHsMdmSelectPrompt.setStatus("optional")


class _NmcHsLoginFailedMsg_Type(DisplayString):
    """Custom type nmcHsLoginFailedMsg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_NmcHsLoginFailedMsg_Type.__name__ = "DisplayString"
_NmcHsLoginFailedMsg_Object = MibScalar
nmcHsLoginFailedMsg = _NmcHsLoginFailedMsg_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 6, 8),
    _NmcHsLoginFailedMsg_Type()
)
nmcHsLoginFailedMsg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmcHsLoginFailedMsg.setStatus("optional")


class _NmcHsPhoneRestrictPrompt_Type(DisplayString):
    """Custom type nmcHsPhoneRestrictPrompt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_NmcHsPhoneRestrictPrompt_Type.__name__ = "DisplayString"
_NmcHsPhoneRestrictPrompt_Object = MibScalar
nmcHsPhoneRestrictPrompt = _NmcHsPhoneRestrictPrompt_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 6, 9),
    _NmcHsPhoneRestrictPrompt_Type()
)
nmcHsPhoneRestrictPrompt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmcHsPhoneRestrictPrompt.setStatus("optional")


class _NmcHsInvalidMdmSelecMsg_Type(DisplayString):
    """Custom type nmcHsInvalidMdmSelecMsg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_NmcHsInvalidMdmSelecMsg_Type.__name__ = "DisplayString"
_NmcHsInvalidMdmSelecMsg_Object = MibScalar
nmcHsInvalidMdmSelecMsg = _NmcHsInvalidMdmSelecMsg_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 6, 10),
    _NmcHsInvalidMdmSelecMsg_Type()
)
nmcHsInvalidMdmSelecMsg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmcHsInvalidMdmSelecMsg.setStatus("optional")


class _NmcHsNoMdnsAvailMsg_Type(DisplayString):
    """Custom type nmcHsNoMdnsAvailMsg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_NmcHsNoMdnsAvailMsg_Type.__name__ = "DisplayString"
_NmcHsNoMdnsAvailMsg_Object = MibScalar
nmcHsNoMdnsAvailMsg = _NmcHsNoMdnsAvailMsg_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 6, 11),
    _NmcHsNoMdnsAvailMsg_Type()
)
nmcHsNoMdnsAvailMsg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmcHsNoMdnsAvailMsg.setStatus("optional")


class _NmcHsConnectSuccessMsg_Type(DisplayString):
    """Custom type nmcHsConnectSuccessMsg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_NmcHsConnectSuccessMsg_Type.__name__ = "DisplayString"
_NmcHsConnectSuccessMsg_Object = MibScalar
nmcHsConnectSuccessMsg = _NmcHsConnectSuccessMsg_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 6, 12),
    _NmcHsConnectSuccessMsg_Type()
)
nmcHsConnectSuccessMsg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmcHsConnectSuccessMsg.setStatus("optional")


class _NmcHsNewPasswordPrompt_Type(DisplayString):
    """Custom type nmcHsNewPasswordPrompt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_NmcHsNewPasswordPrompt_Type.__name__ = "DisplayString"
_NmcHsNewPasswordPrompt_Object = MibScalar
nmcHsNewPasswordPrompt = _NmcHsNewPasswordPrompt_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 6, 13),
    _NmcHsNewPasswordPrompt_Type()
)
nmcHsNewPasswordPrompt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmcHsNewPasswordPrompt.setStatus("optional")


class _NmcHsChangePasswordMsg_Type(DisplayString):
    """Custom type nmcHsChangePasswordMsg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_NmcHsChangePasswordMsg_Type.__name__ = "DisplayString"
_NmcHsChangePasswordMsg_Object = MibScalar
nmcHsChangePasswordMsg = _NmcHsChangePasswordMsg_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 6, 14),
    _NmcHsChangePasswordMsg_Type()
)
nmcHsChangePasswordMsg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmcHsChangePasswordMsg.setStatus("optional")


class _NmcHsPromptRspTimeout_Type(Integer32):
    """Custom type nmcHsPromptRspTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 255),
    )


_NmcHsPromptRspTimeout_Type.__name__ = "Integer32"
_NmcHsPromptRspTimeout_Object = MibScalar
nmcHsPromptRspTimeout = _NmcHsPromptRspTimeout_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 6, 15),
    _NmcHsPromptRspTimeout_Type()
)
nmcHsPromptRspTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmcHsPromptRspTimeout.setStatus("optional")


class _NmcHsPromptRspAttempts_Type(Integer32):
    """Custom type nmcHsPromptRspAttempts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_NmcHsPromptRspAttempts_Type.__name__ = "Integer32"
_NmcHsPromptRspAttempts_Object = MibScalar
nmcHsPromptRspAttempts = _NmcHsPromptRspAttempts_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 6, 16),
    _NmcHsPromptRspAttempts_Type()
)
nmcHsPromptRspAttempts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmcHsPromptRspAttempts.setStatus("optional")


class _NmcHsPromptRspEchoEna_Type(Integer32):
    """Custom type nmcHsPromptRspEchoEna based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_NmcHsPromptRspEchoEna_Type.__name__ = "Integer32"
_NmcHsPromptRspEchoEna_Object = MibScalar
nmcHsPromptRspEchoEna = _NmcHsPromptRspEchoEna_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 6, 17),
    _NmcHsPromptRspEchoEna_Type()
)
nmcHsPromptRspEchoEna.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmcHsPromptRspEchoEna.setStatus("optional")


class _NmcHsDialBackDelay_Type(Integer32):
    """Custom type nmcHsDialBackDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_NmcHsDialBackDelay_Type.__name__ = "Integer32"
_NmcHsDialBackDelay_Object = MibScalar
nmcHsDialBackDelay = _NmcHsDialBackDelay_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 6, 18),
    _NmcHsDialBackDelay_Type()
)
nmcHsDialBackDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmcHsDialBackDelay.setStatus("optional")


class _NmcHsDialBackAttempts_Type(Integer32):
    """Custom type nmcHsDialBackAttempts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_NmcHsDialBackAttempts_Type.__name__ = "Integer32"
_NmcHsDialBackAttempts_Object = MibScalar
nmcHsDialBackAttempts = _NmcHsDialBackAttempts_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 6, 19),
    _NmcHsDialBackAttempts_Type()
)
nmcHsDialBackAttempts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmcHsDialBackAttempts.setStatus("optional")
_NmcHsSecuritySrvrAddr_Type = IpAddress
_NmcHsSecuritySrvrAddr_Object = MibScalar
nmcHsSecuritySrvrAddr = _NmcHsSecuritySrvrAddr_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 6, 20),
    _NmcHsSecuritySrvrAddr_Type()
)
nmcHsSecuritySrvrAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmcHsSecuritySrvrAddr.setStatus("mandatory")


class _NmcHsSecuritySrvrPort_Type(Integer32):
    """Custom type nmcHsSecuritySrvrPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NmcHsSecuritySrvrPort_Type.__name__ = "Integer32"
_NmcHsSecuritySrvrPort_Object = MibScalar
nmcHsSecuritySrvrPort = _NmcHsSecuritySrvrPort_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 6, 21),
    _NmcHsSecuritySrvrPort_Type()
)
nmcHsSecuritySrvrPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmcHsSecuritySrvrPort.setStatus("mandatory")


class _NmcHsSecuritySrvrRetries_Type(Integer32):
    """Custom type nmcHsSecuritySrvrRetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_NmcHsSecuritySrvrRetries_Type.__name__ = "Integer32"
_NmcHsSecuritySrvrRetries_Object = MibScalar
nmcHsSecuritySrvrRetries = _NmcHsSecuritySrvrRetries_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 6, 22),
    _NmcHsSecuritySrvrRetries_Type()
)
nmcHsSecuritySrvrRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmcHsSecuritySrvrRetries.setStatus("mandatory")


class _NmcHsMdmAttemptLimit_Type(Integer32):
    """Custom type nmcHsMdmAttemptLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_NmcHsMdmAttemptLimit_Type.__name__ = "Integer32"
_NmcHsMdmAttemptLimit_Object = MibScalar
nmcHsMdmAttemptLimit = _NmcHsMdmAttemptLimit_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 6, 23),
    _NmcHsMdmAttemptLimit_Type()
)
nmcHsMdmAttemptLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmcHsMdmAttemptLimit.setStatus("mandatory")


class _NmcHsServerUnavailable_Type(Integer32):
    """Custom type nmcHsServerUnavailable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allowCall", 2),
          ("denyCall", 1))
    )


_NmcHsServerUnavailable_Type.__name__ = "Integer32"
_NmcHsServerUnavailable_Object = MibScalar
nmcHsServerUnavailable = _NmcHsServerUnavailable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 6, 24),
    _NmcHsServerUnavailable_Type()
)
nmcHsServerUnavailable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmcHsServerUnavailable.setStatus("mandatory")


class _NmcHsServerSelect_Type(Integer32):
    """Custom type nmcHsServerSelect based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("eighth", 9),
          ("fifth", 6),
          ("fourth", 5),
          ("none", 3),
          ("primary", 1),
          ("secondary", 2),
          ("seventh", 8),
          ("sixth", 7),
          ("third", 4))
    )


_NmcHsServerSelect_Type.__name__ = "Integer32"
_NmcHsServerSelect_Object = MibScalar
nmcHsServerSelect = _NmcHsServerSelect_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 6, 25),
    _NmcHsServerSelect_Type()
)
nmcHsServerSelect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmcHsServerSelect.setStatus("mandatory")
_NmcHsSecondarySrvrAddr_Type = IpAddress
_NmcHsSecondarySrvrAddr_Object = MibScalar
nmcHsSecondarySrvrAddr = _NmcHsSecondarySrvrAddr_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 6, 26),
    _NmcHsSecondarySrvrAddr_Type()
)
nmcHsSecondarySrvrAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmcHsSecondarySrvrAddr.setStatus("mandatory")


class _NmcHsDiPasswdEnaDis_Type(Integer32):
    """Custom type nmcHsDiPasswdEnaDis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_NmcHsDiPasswdEnaDis_Type.__name__ = "Integer32"
_NmcHsDiPasswdEnaDis_Object = MibScalar
nmcHsDiPasswdEnaDis = _NmcHsDiPasswdEnaDis_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 6, 27),
    _NmcHsDiPasswdEnaDis_Type()
)
nmcHsDiPasswdEnaDis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmcHsDiPasswdEnaDis.setStatus("optional")
_NmcHsSecurity3SrvrAddr_Type = IpAddress
_NmcHsSecurity3SrvrAddr_Object = MibScalar
nmcHsSecurity3SrvrAddr = _NmcHsSecurity3SrvrAddr_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 6, 28),
    _NmcHsSecurity3SrvrAddr_Type()
)
nmcHsSecurity3SrvrAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmcHsSecurity3SrvrAddr.setStatus("mandatory")
_NmcHsSecurity4SrvrAddr_Type = IpAddress
_NmcHsSecurity4SrvrAddr_Object = MibScalar
nmcHsSecurity4SrvrAddr = _NmcHsSecurity4SrvrAddr_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 6, 29),
    _NmcHsSecurity4SrvrAddr_Type()
)
nmcHsSecurity4SrvrAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmcHsSecurity4SrvrAddr.setStatus("mandatory")
_NmcHsSecurity5SrvrAddr_Type = IpAddress
_NmcHsSecurity5SrvrAddr_Object = MibScalar
nmcHsSecurity5SrvrAddr = _NmcHsSecurity5SrvrAddr_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 6, 30),
    _NmcHsSecurity5SrvrAddr_Type()
)
nmcHsSecurity5SrvrAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmcHsSecurity5SrvrAddr.setStatus("mandatory")
_NmcHsSecurity6SrvrAddr_Type = IpAddress
_NmcHsSecurity6SrvrAddr_Object = MibScalar
nmcHsSecurity6SrvrAddr = _NmcHsSecurity6SrvrAddr_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 6, 31),
    _NmcHsSecurity6SrvrAddr_Type()
)
nmcHsSecurity6SrvrAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmcHsSecurity6SrvrAddr.setStatus("mandatory")
_NmcHsSecurity7SrvrAddr_Type = IpAddress
_NmcHsSecurity7SrvrAddr_Object = MibScalar
nmcHsSecurity7SrvrAddr = _NmcHsSecurity7SrvrAddr_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 6, 32),
    _NmcHsSecurity7SrvrAddr_Type()
)
nmcHsSecurity7SrvrAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmcHsSecurity7SrvrAddr.setStatus("mandatory")
_NmcHsSecurity8SrvrAddr_Type = IpAddress
_NmcHsSecurity8SrvrAddr_Object = MibScalar
nmcHsSecurity8SrvrAddr = _NmcHsSecurity8SrvrAddr_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 6, 33),
    _NmcHsSecurity8SrvrAddr_Type()
)
nmcHsSecurity8SrvrAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmcHsSecurity8SrvrAddr.setStatus("mandatory")


class _NmcHsSecuritySrvrName_Type(DisplayString):
    """Custom type nmcHsSecuritySrvrName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_NmcHsSecuritySrvrName_Type.__name__ = "DisplayString"
_NmcHsSecuritySrvrName_Object = MibScalar
nmcHsSecuritySrvrName = _NmcHsSecuritySrvrName_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 6, 34),
    _NmcHsSecuritySrvrName_Type()
)
nmcHsSecuritySrvrName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmcHsSecuritySrvrName.setStatus("mandatory")


class _NmcHsSecuritySrvrDnsEna_Type(Integer32):
    """Custom type nmcHsSecuritySrvrDnsEna based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_NmcHsSecuritySrvrDnsEna_Type.__name__ = "Integer32"
_NmcHsSecuritySrvrDnsEna_Object = MibScalar
nmcHsSecuritySrvrDnsEna = _NmcHsSecuritySrvrDnsEna_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 6, 35),
    _NmcHsSecuritySrvrDnsEna_Type()
)
nmcHsSecuritySrvrDnsEna.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmcHsSecuritySrvrDnsEna.setStatus("mandatory")


class _NmcHsSecurityStatusInt_Type(Integer32):
    """Custom type nmcHsSecurityStatusInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 65535),
    )


_NmcHsSecurityStatusInt_Type.__name__ = "Integer32"
_NmcHsSecurityStatusInt_Object = MibScalar
nmcHsSecurityStatusInt = _NmcHsSecurityStatusInt_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 6, 36),
    _NmcHsSecurityStatusInt_Type()
)
nmcHsSecurityStatusInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmcHsSecurityStatusInt.setStatus("mandatory")


class _NmcHsSecurityFailure_Type(Integer32):
    """Custom type nmcHsSecurityFailure based on Integer32"""
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
        *(("commFailure", 3),
          ("disabledServer", 5),
          ("invalidResponse", 4),
          ("none", 1),
          ("other", 2))
    )


_NmcHsSecurityFailure_Type.__name__ = "Integer32"
_NmcHsSecurityFailure_Object = MibScalar
nmcHsSecurityFailure = _NmcHsSecurityFailure_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 6, 37),
    _NmcHsSecurityFailure_Type()
)
nmcHsSecurityFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmcHsSecurityFailure.setStatus("mandatory")
_NmcTe_ObjectIdentity = ObjectIdentity
nmcTe = _NmcTe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 7)
)


class _NmcTeDialOutLoginFail_Type(Integer32):
    """Custom type nmcTeDialOutLoginFail based on Integer32"""
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
        *(("disableAll", 2),
          ("enableAll", 4),
          ("enableLog", 3),
          ("enableTrap", 1))
    )


_NmcTeDialOutLoginFail_Type.__name__ = "Integer32"
_NmcTeDialOutLoginFail_Object = MibScalar
nmcTeDialOutLoginFail = _NmcTeDialOutLoginFail_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 7, 1),
    _NmcTeDialOutLoginFail_Type()
)
nmcTeDialOutLoginFail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmcTeDialOutLoginFail.setStatus("optional")


class _NmcTeDialInLoginFail_Type(Integer32):
    """Custom type nmcTeDialInLoginFail based on Integer32"""
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
        *(("disableAll", 2),
          ("enableAll", 4),
          ("enableLog", 3),
          ("enableTrap", 1))
    )


_NmcTeDialInLoginFail_Type.__name__ = "Integer32"
_NmcTeDialInLoginFail_Object = MibScalar
nmcTeDialInLoginFail = _NmcTeDialInLoginFail_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 7, 2),
    _NmcTeDialInLoginFail_Type()
)
nmcTeDialInLoginFail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmcTeDialInLoginFail.setStatus("optional")


class _NmcTeDialOutRestrictNum_Type(Integer32):
    """Custom type nmcTeDialOutRestrictNum based on Integer32"""
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
        *(("disableAll", 2),
          ("enableAll", 4),
          ("enableLog", 3),
          ("enableTrap", 1))
    )


_NmcTeDialOutRestrictNum_Type.__name__ = "Integer32"
_NmcTeDialOutRestrictNum_Object = MibScalar
nmcTeDialOutRestrictNum = _NmcTeDialOutRestrictNum_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 7, 3),
    _NmcTeDialOutRestrictNum_Type()
)
nmcTeDialOutRestrictNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmcTeDialOutRestrictNum.setStatus("optional")


class _NmcTeDialBackRestrictNum_Type(Integer32):
    """Custom type nmcTeDialBackRestrictNum based on Integer32"""
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
        *(("disableAll", 2),
          ("enableAll", 4),
          ("enableLog", 3),
          ("enableTrap", 1))
    )


_NmcTeDialBackRestrictNum_Type.__name__ = "Integer32"
_NmcTeDialBackRestrictNum_Object = MibScalar
nmcTeDialBackRestrictNum = _NmcTeDialBackRestrictNum_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 7, 4),
    _NmcTeDialBackRestrictNum_Type()
)
nmcTeDialBackRestrictNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmcTeDialBackRestrictNum.setStatus("optional")


class _NmcTeUserBlacklist_Type(Integer32):
    """Custom type nmcTeUserBlacklist based on Integer32"""
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
        *(("disableAll", 2),
          ("enableAll", 4),
          ("enableLog", 3),
          ("enableTrap", 1))
    )


_NmcTeUserBlacklist_Type.__name__ = "Integer32"
_NmcTeUserBlacklist_Object = MibScalar
nmcTeUserBlacklist = _NmcTeUserBlacklist_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 7, 5),
    _NmcTeUserBlacklist_Type()
)
nmcTeUserBlacklist.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmcTeUserBlacklist.setStatus("optional")


class _NmcTeUserBlacklistLogin_Type(Integer32):
    """Custom type nmcTeUserBlacklistLogin based on Integer32"""
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
        *(("disableAll", 2),
          ("enableAll", 4),
          ("enableLog", 3),
          ("enableTrap", 1))
    )


_NmcTeUserBlacklistLogin_Type.__name__ = "Integer32"
_NmcTeUserBlacklistLogin_Object = MibScalar
nmcTeUserBlacklistLogin = _NmcTeUserBlacklistLogin_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 7, 6),
    _NmcTeUserBlacklistLogin_Type()
)
nmcTeUserBlacklistLogin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmcTeUserBlacklistLogin.setStatus("optional")


class _NmcTeRespAttmptLimExceed_Type(Integer32):
    """Custom type nmcTeRespAttmptLimExceed based on Integer32"""
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
        *(("disableAll", 2),
          ("enableAll", 4),
          ("enableLog", 3),
          ("enableTrap", 1))
    )


_NmcTeRespAttmptLimExceed_Type.__name__ = "Integer32"
_NmcTeRespAttmptLimExceed_Object = MibScalar
nmcTeRespAttmptLimExceed = _NmcTeRespAttmptLimExceed_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 7, 7),
    _NmcTeRespAttmptLimExceed_Type()
)
nmcTeRespAttmptLimExceed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmcTeRespAttmptLimExceed.setStatus("optional")


class _NmcTeLoginAttmptLimExceed_Type(Integer32):
    """Custom type nmcTeLoginAttmptLimExceed based on Integer32"""
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
        *(("disableAll", 2),
          ("enableAll", 4),
          ("enableLog", 3),
          ("enableTrap", 1))
    )


_NmcTeLoginAttmptLimExceed_Type.__name__ = "Integer32"
_NmcTeLoginAttmptLimExceed_Object = MibScalar
nmcTeLoginAttmptLimExceed = _NmcTeLoginAttmptLimExceed_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 7, 8),
    _NmcTeLoginAttmptLimExceed_Type()
)
nmcTeLoginAttmptLimExceed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmcTeLoginAttmptLimExceed.setStatus("optional")


class _NmcTeLogSrvrLoss_Type(Integer32):
    """Custom type nmcTeLogSrvrLoss based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_NmcTeLogSrvrLoss_Type.__name__ = "Integer32"
_NmcTeLogSrvrLoss_Object = MibScalar
nmcTeLogSrvrLoss = _NmcTeLogSrvrLoss_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 7, 9),
    _NmcTeLogSrvrLoss_Type()
)
nmcTeLogSrvrLoss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmcTeLogSrvrLoss.setStatus("mandatory")


class _NmcTeSecSrvrLoss_Type(Integer32):
    """Custom type nmcTeSecSrvrLoss based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_NmcTeSecSrvrLoss_Type.__name__ = "Integer32"
_NmcTeSecSrvrLoss_Object = MibScalar
nmcTeSecSrvrLoss = _NmcTeSecSrvrLoss_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 7, 10),
    _NmcTeSecSrvrLoss_Type()
)
nmcTeSecSrvrLoss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmcTeSecSrvrLoss.setStatus("mandatory")


class _NmcTeSinglePbClockFail_Type(Integer32):
    """Custom type nmcTeSinglePbClockFail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_NmcTeSinglePbClockFail_Type.__name__ = "Integer32"
_NmcTeSinglePbClockFail_Object = MibScalar
nmcTeSinglePbClockFail = _NmcTeSinglePbClockFail_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 7, 11),
    _NmcTeSinglePbClockFail_Type()
)
nmcTeSinglePbClockFail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmcTeSinglePbClockFail.setStatus("mandatory")


class _NmcTePbClockSwitch_Type(Integer32):
    """Custom type nmcTePbClockSwitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_NmcTePbClockSwitch_Type.__name__ = "Integer32"
_NmcTePbClockSwitch_Object = MibScalar
nmcTePbClockSwitch = _NmcTePbClockSwitch_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 7, 12),
    _NmcTePbClockSwitch_Type()
)
nmcTePbClockSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmcTePbClockSwitch.setStatus("mandatory")


class _NmcTePbClockFail_Type(Integer32):
    """Custom type nmcTePbClockFail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_NmcTePbClockFail_Type.__name__ = "Integer32"
_NmcTePbClockFail_Object = MibScalar
nmcTePbClockFail = _NmcTePbClockFail_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 7, 13),
    _NmcTePbClockFail_Type()
)
nmcTePbClockFail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmcTePbClockFail.setStatus("mandatory")


class _NmcTeDnsSrvrLoss_Type(Integer32):
    """Custom type nmcTeDnsSrvrLoss based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_NmcTeDnsSrvrLoss_Type.__name__ = "Integer32"
_NmcTeDnsSrvrLoss_Object = MibScalar
nmcTeDnsSrvrLoss = _NmcTeDnsSrvrLoss_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 7, 14),
    _NmcTeDnsSrvrLoss_Type()
)
nmcTeDnsSrvrLoss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmcTeDnsSrvrLoss.setStatus("mandatory")


class _NmcTeNtpSrvrLoss_Type(Integer32):
    """Custom type nmcTeNtpSrvrLoss based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_NmcTeNtpSrvrLoss_Type.__name__ = "Integer32"
_NmcTeNtpSrvrLoss_Object = MibScalar
nmcTeNtpSrvrLoss = _NmcTeNtpSrvrLoss_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 7, 15),
    _NmcTeNtpSrvrLoss_Type()
)
nmcTeNtpSrvrLoss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmcTeNtpSrvrLoss.setStatus("mandatory")


class _NmcTeNtpSrvrRestore_Type(Integer32):
    """Custom type nmcTeNtpSrvrRestore based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_NmcTeNtpSrvrRestore_Type.__name__ = "Integer32"
_NmcTeNtpSrvrRestore_Object = MibScalar
nmcTeNtpSrvrRestore = _NmcTeNtpSrvrRestore_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 7, 16),
    _NmcTeNtpSrvrRestore_Type()
)
nmcTeNtpSrvrRestore.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmcTeNtpSrvrRestore.setStatus("mandatory")


class _NmcTeNtpSrvrDegraded_Type(Integer32):
    """Custom type nmcTeNtpSrvrDegraded based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_NmcTeNtpSrvrDegraded_Type.__name__ = "Integer32"
_NmcTeNtpSrvrDegraded_Object = MibScalar
nmcTeNtpSrvrDegraded = _NmcTeNtpSrvrDegraded_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 7, 17),
    _NmcTeNtpSrvrDegraded_Type()
)
nmcTeNtpSrvrDegraded.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmcTeNtpSrvrDegraded.setStatus("mandatory")


class _NmcTeDnsSrvrRestore_Type(Integer32):
    """Custom type nmcTeDnsSrvrRestore based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_NmcTeDnsSrvrRestore_Type.__name__ = "Integer32"
_NmcTeDnsSrvrRestore_Object = MibScalar
nmcTeDnsSrvrRestore = _NmcTeDnsSrvrRestore_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 7, 18),
    _NmcTeDnsSrvrRestore_Type()
)
nmcTeDnsSrvrRestore.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmcTeDnsSrvrRestore.setStatus("mandatory")


class _NmcTeDnsSrvrDegraded_Type(Integer32):
    """Custom type nmcTeDnsSrvrDegraded based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_NmcTeDnsSrvrDegraded_Type.__name__ = "Integer32"
_NmcTeDnsSrvrDegraded_Object = MibScalar
nmcTeDnsSrvrDegraded = _NmcTeDnsSrvrDegraded_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 7, 19),
    _NmcTeDnsSrvrDegraded_Type()
)
nmcTeDnsSrvrDegraded.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmcTeDnsSrvrDegraded.setStatus("mandatory")


class _NmcTeLogSrvrRestore_Type(Integer32):
    """Custom type nmcTeLogSrvrRestore based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_NmcTeLogSrvrRestore_Type.__name__ = "Integer32"
_NmcTeLogSrvrRestore_Object = MibScalar
nmcTeLogSrvrRestore = _NmcTeLogSrvrRestore_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 7, 20),
    _NmcTeLogSrvrRestore_Type()
)
nmcTeLogSrvrRestore.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmcTeLogSrvrRestore.setStatus("mandatory")


class _NmcTeLogSrvrGroupOper_Type(Integer32):
    """Custom type nmcTeLogSrvrGroupOper based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_NmcTeLogSrvrGroupOper_Type.__name__ = "Integer32"
_NmcTeLogSrvrGroupOper_Object = MibScalar
nmcTeLogSrvrGroupOper = _NmcTeLogSrvrGroupOper_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 7, 21),
    _NmcTeLogSrvrGroupOper_Type()
)
nmcTeLogSrvrGroupOper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmcTeLogSrvrGroupOper.setStatus("mandatory")


class _NmcTeLogSrvrGroupDegr_Type(Integer32):
    """Custom type nmcTeLogSrvrGroupDegr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_NmcTeLogSrvrGroupDegr_Type.__name__ = "Integer32"
_NmcTeLogSrvrGroupDegr_Object = MibScalar
nmcTeLogSrvrGroupDegr = _NmcTeLogSrvrGroupDegr_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 7, 22),
    _NmcTeLogSrvrGroupDegr_Type()
)
nmcTeLogSrvrGroupDegr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmcTeLogSrvrGroupDegr.setStatus("mandatory")


class _NmcTeLogSrvrGroupNonOp_Type(Integer32):
    """Custom type nmcTeLogSrvrGroupNonOp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_NmcTeLogSrvrGroupNonOp_Type.__name__ = "Integer32"
_NmcTeLogSrvrGroupNonOp_Object = MibScalar
nmcTeLogSrvrGroupNonOp = _NmcTeLogSrvrGroupNonOp_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 7, 23),
    _NmcTeLogSrvrGroupNonOp_Type()
)
nmcTeLogSrvrGroupNonOp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmcTeLogSrvrGroupNonOp.setStatus("mandatory")


class _NmcTeSecSrvrRestore_Type(Integer32):
    """Custom type nmcTeSecSrvrRestore based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_NmcTeSecSrvrRestore_Type.__name__ = "Integer32"
_NmcTeSecSrvrRestore_Object = MibScalar
nmcTeSecSrvrRestore = _NmcTeSecSrvrRestore_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 7, 24),
    _NmcTeSecSrvrRestore_Type()
)
nmcTeSecSrvrRestore.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmcTeSecSrvrRestore.setStatus("mandatory")


class _NmcTeSecSrvrGroupOper_Type(Integer32):
    """Custom type nmcTeSecSrvrGroupOper based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_NmcTeSecSrvrGroupOper_Type.__name__ = "Integer32"
_NmcTeSecSrvrGroupOper_Object = MibScalar
nmcTeSecSrvrGroupOper = _NmcTeSecSrvrGroupOper_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 7, 25),
    _NmcTeSecSrvrGroupOper_Type()
)
nmcTeSecSrvrGroupOper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmcTeSecSrvrGroupOper.setStatus("mandatory")


class _NmcTeSecSrvrGroupDegr_Type(Integer32):
    """Custom type nmcTeSecSrvrGroupDegr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_NmcTeSecSrvrGroupDegr_Type.__name__ = "Integer32"
_NmcTeSecSrvrGroupDegr_Object = MibScalar
nmcTeSecSrvrGroupDegr = _NmcTeSecSrvrGroupDegr_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 7, 26),
    _NmcTeSecSrvrGroupDegr_Type()
)
nmcTeSecSrvrGroupDegr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmcTeSecSrvrGroupDegr.setStatus("mandatory")


class _NmcTeSecSrvrGroupNonOp_Type(Integer32):
    """Custom type nmcTeSecSrvrGroupNonOp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_NmcTeSecSrvrGroupNonOp_Type.__name__ = "Integer32"
_NmcTeSecSrvrGroupNonOp_Object = MibScalar
nmcTeSecSrvrGroupNonOp = _NmcTeSecSrvrGroupNonOp_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 7, 27),
    _NmcTeSecSrvrGroupNonOp_Type()
)
nmcTeSecSrvrGroupNonOp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmcTeSecSrvrGroupNonOp.setStatus("mandatory")
_NmcUiCfg_ObjectIdentity = ObjectIdentity
nmcUiCfg = _NmcUiCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 8)
)
_NmcUiCfgLanIPAddr_Type = IpAddress
_NmcUiCfgLanIPAddr_Object = MibScalar
nmcUiCfgLanIPAddr = _NmcUiCfgLanIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 8, 1),
    _NmcUiCfgLanIPAddr_Type()
)
nmcUiCfgLanIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmcUiCfgLanIPAddr.setStatus("mandatory")
_NmcUiCfgLanSubnetMask_Type = IpAddress
_NmcUiCfgLanSubnetMask_Object = MibScalar
nmcUiCfgLanSubnetMask = _NmcUiCfgLanSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 8, 2),
    _NmcUiCfgLanSubnetMask_Type()
)
nmcUiCfgLanSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmcUiCfgLanSubnetMask.setStatus("mandatory")
_NmcUiCfgWanIPAddr_Type = IpAddress
_NmcUiCfgWanIPAddr_Object = MibScalar
nmcUiCfgWanIPAddr = _NmcUiCfgWanIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 8, 3),
    _NmcUiCfgWanIPAddr_Type()
)
nmcUiCfgWanIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmcUiCfgWanIPAddr.setStatus("mandatory")
_NmcUiCfgWanSubnetMask_Type = IpAddress
_NmcUiCfgWanSubnetMask_Object = MibScalar
nmcUiCfgWanSubnetMask = _NmcUiCfgWanSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 8, 4),
    _NmcUiCfgWanSubnetMask_Type()
)
nmcUiCfgWanSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmcUiCfgWanSubnetMask.setStatus("mandatory")
_NmcUiCfgDefaultGwyIP_Type = IpAddress
_NmcUiCfgDefaultGwyIP_Object = MibScalar
nmcUiCfgDefaultGwyIP = _NmcUiCfgDefaultGwyIP_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 8, 5),
    _NmcUiCfgDefaultGwyIP_Type()
)
nmcUiCfgDefaultGwyIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmcUiCfgDefaultGwyIP.setStatus("mandatory")


class _NmcUiCfgLocalTrIeeeAddr_Type(OctetString):
    """Custom type nmcUiCfgLocalTrIeeeAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_NmcUiCfgLocalTrIeeeAddr_Type.__name__ = "OctetString"
_NmcUiCfgLocalTrIeeeAddr_Object = MibScalar
nmcUiCfgLocalTrIeeeAddr = _NmcUiCfgLocalTrIeeeAddr_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 8, 6),
    _NmcUiCfgLocalTrIeeeAddr_Type()
)
nmcUiCfgLocalTrIeeeAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmcUiCfgLocalTrIeeeAddr.setStatus("mandatory")


class _NmcUiCfgPrivateString_Type(DisplayString):
    """Custom type nmcUiCfgPrivateString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NmcUiCfgPrivateString_Type.__name__ = "DisplayString"
_NmcUiCfgPrivateString_Object = MibScalar
nmcUiCfgPrivateString = _NmcUiCfgPrivateString_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 8, 7),
    _NmcUiCfgPrivateString_Type()
)
nmcUiCfgPrivateString.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    nmcUiCfgPrivateString.setStatus("mandatory")


class _NmcUiCfgLanIfEnable_Type(Integer32):
    """Custom type nmcUiCfgLanIfEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_NmcUiCfgLanIfEnable_Type.__name__ = "Integer32"
_NmcUiCfgLanIfEnable_Object = MibScalar
nmcUiCfgLanIfEnable = _NmcUiCfgLanIfEnable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 8, 8),
    _NmcUiCfgLanIfEnable_Type()
)
nmcUiCfgLanIfEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmcUiCfgLanIfEnable.setStatus("optional")


class _NmcUiCfgPublicString_Type(DisplayString):
    """Custom type nmcUiCfgPublicString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NmcUiCfgPublicString_Type.__name__ = "DisplayString"
_NmcUiCfgPublicString_Object = MibScalar
nmcUiCfgPublicString = _NmcUiCfgPublicString_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 8, 9),
    _NmcUiCfgPublicString_Type()
)
nmcUiCfgPublicString.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    nmcUiCfgPublicString.setStatus("mandatory")


class _NmcUiCfgRouteEnable_Type(Integer32):
    """Custom type nmcUiCfgRouteEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_NmcUiCfgRouteEnable_Type.__name__ = "Integer32"
_NmcUiCfgRouteEnable_Object = MibScalar
nmcUiCfgRouteEnable = _NmcUiCfgRouteEnable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 8, 10),
    _NmcUiCfgRouteEnable_Type()
)
nmcUiCfgRouteEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmcUiCfgRouteEnable.setStatus("optional")


class _NmcUiCfgUiSlipCfg_Type(Integer32):
    """Custom type nmcUiCfgUiSlipCfg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("slipport", 2),
          ("uiport", 1))
    )


_NmcUiCfgUiSlipCfg_Type.__name__ = "Integer32"
_NmcUiCfgUiSlipCfg_Object = MibScalar
nmcUiCfgUiSlipCfg = _NmcUiCfgUiSlipCfg_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 8, 11),
    _NmcUiCfgUiSlipCfg_Type()
)
nmcUiCfgUiSlipCfg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmcUiCfgUiSlipCfg.setStatus("optional")
_NmcUiCfgWan2IpAddr_Type = IpAddress
_NmcUiCfgWan2IpAddr_Object = MibScalar
nmcUiCfgWan2IpAddr = _NmcUiCfgWan2IpAddr_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 8, 12),
    _NmcUiCfgWan2IpAddr_Type()
)
nmcUiCfgWan2IpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmcUiCfgWan2IpAddr.setStatus("mandatory")
_NmcUiCfgWan2SubnetMask_Type = IpAddress
_NmcUiCfgWan2SubnetMask_Object = MibScalar
nmcUiCfgWan2SubnetMask = _NmcUiCfgWan2SubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 8, 13),
    _NmcUiCfgWan2SubnetMask_Type()
)
nmcUiCfgWan2SubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmcUiCfgWan2SubnetMask.setStatus("mandatory")


class _NmcUiCfgInactiveTime_Type(Integer32):
    """Custom type nmcUiCfgInactiveTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_NmcUiCfgInactiveTime_Type.__name__ = "Integer32"
_NmcUiCfgInactiveTime_Object = MibScalar
nmcUiCfgInactiveTime = _NmcUiCfgInactiveTime_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 8, 14),
    _NmcUiCfgInactiveTime_Type()
)
nmcUiCfgInactiveTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmcUiCfgInactiveTime.setStatus("optional")


class _NmcUiCfgPassword_Type(Integer32):
    """Custom type nmcUiCfgPassword based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_NmcUiCfgPassword_Type.__name__ = "Integer32"
_NmcUiCfgPassword_Object = MibScalar
nmcUiCfgPassword = _NmcUiCfgPassword_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 8, 15),
    _NmcUiCfgPassword_Type()
)
nmcUiCfgPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmcUiCfgPassword.setStatus("optional")
_NmcAuth_ObjectIdentity = ObjectIdentity
nmcAuth = _NmcAuth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 9)
)
_NmcAuthAccTable_Object = MibTable
nmcAuthAccTable = _NmcAuthAccTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 9, 1)
)
if mibBuilder.loadTexts:
    nmcAuthAccTable.setStatus("mandatory")
_NmcAuthAccEntry_Object = MibTableRow
nmcAuthAccEntry = _NmcAuthAccEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 9, 1, 1)
)
nmcAuthAccEntry.setIndexNames(
    (0, "NMC-MIB", "nmcAuthAccIpAddr"),
)
if mibBuilder.loadTexts:
    nmcAuthAccEntry.setStatus("mandatory")
_NmcAuthAccIpAddr_Type = IpAddress
_NmcAuthAccIpAddr_Object = MibTableColumn
nmcAuthAccIpAddr = _NmcAuthAccIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 9, 1, 1, 1),
    _NmcAuthAccIpAddr_Type()
)
nmcAuthAccIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmcAuthAccIpAddr.setStatus("mandatory")
_NmcAuthAccNetMask_Type = IpAddress
_NmcAuthAccNetMask_Object = MibTableColumn
nmcAuthAccNetMask = _NmcAuthAccNetMask_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 9, 1, 1, 2),
    _NmcAuthAccNetMask_Type()
)
nmcAuthAccNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmcAuthAccNetMask.setStatus("mandatory")


class _NmcAuthAccDescr_Type(DisplayString):
    """Custom type nmcAuthAccDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_NmcAuthAccDescr_Type.__name__ = "DisplayString"
_NmcAuthAccDescr_Object = MibTableColumn
nmcAuthAccDescr = _NmcAuthAccDescr_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 9, 1, 1, 3),
    _NmcAuthAccDescr_Type()
)
nmcAuthAccDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmcAuthAccDescr.setStatus("mandatory")
_NmcNtp_ObjectIdentity = ObjectIdentity
nmcNtp = _NmcNtp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 10)
)
_NmcNtpSrvrPrimAddr_Type = IpAddress
_NmcNtpSrvrPrimAddr_Object = MibScalar
nmcNtpSrvrPrimAddr = _NmcNtpSrvrPrimAddr_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 10, 1),
    _NmcNtpSrvrPrimAddr_Type()
)
nmcNtpSrvrPrimAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmcNtpSrvrPrimAddr.setStatus("mandatory")
_NmcNtpSrvrSecdAddr_Type = IpAddress
_NmcNtpSrvrSecdAddr_Object = MibScalar
nmcNtpSrvrSecdAddr = _NmcNtpSrvrSecdAddr_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 10, 2),
    _NmcNtpSrvrSecdAddr_Type()
)
nmcNtpSrvrSecdAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmcNtpSrvrSecdAddr.setStatus("mandatory")


class _NmcNtpSyncInterval_Type(Integer32):
    """Custom type nmcNtpSyncInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(600, 86400),
    )


_NmcNtpSyncInterval_Type.__name__ = "Integer32"
_NmcNtpSyncInterval_Object = MibScalar
nmcNtpSyncInterval = _NmcNtpSyncInterval_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 10, 3),
    _NmcNtpSyncInterval_Type()
)
nmcNtpSyncInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmcNtpSyncInterval.setStatus("mandatory")


class _NmcNtpOperationalMode_Type(Integer32):
    """Custom type nmcNtpOperationalMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("unicast", 2))
    )


_NmcNtpOperationalMode_Type.__name__ = "Integer32"
_NmcNtpOperationalMode_Object = MibScalar
nmcNtpOperationalMode = _NmcNtpOperationalMode_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 10, 4),
    _NmcNtpOperationalMode_Type()
)
nmcNtpOperationalMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmcNtpOperationalMode.setStatus("mandatory")
_NmcNtpLastSyncTime_Type = Integer32
_NmcNtpLastSyncTime_Object = MibScalar
nmcNtpLastSyncTime = _NmcNtpLastSyncTime_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 10, 5),
    _NmcNtpLastSyncTime_Type()
)
nmcNtpLastSyncTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmcNtpLastSyncTime.setStatus("mandatory")


class _NmcNtpLastSyncServer_Type(Integer32):
    """Custom type nmcNtpLastSyncServer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("primary", 2),
          ("secondary", 3))
    )


_NmcNtpLastSyncServer_Type.__name__ = "Integer32"
_NmcNtpLastSyncServer_Object = MibScalar
nmcNtpLastSyncServer = _NmcNtpLastSyncServer_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 10, 6),
    _NmcNtpLastSyncServer_Type()
)
nmcNtpLastSyncServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmcNtpLastSyncServer.setStatus("mandatory")
_NmcNtpLastFailedTime_Type = Integer32
_NmcNtpLastFailedTime_Object = MibScalar
nmcNtpLastFailedTime = _NmcNtpLastFailedTime_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 10, 7),
    _NmcNtpLastFailedTime_Type()
)
nmcNtpLastFailedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmcNtpLastFailedTime.setStatus("mandatory")


class _NmcNtpLastFailedServer_Type(Integer32):
    """Custom type nmcNtpLastFailedServer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("primary", 2),
          ("secondary", 3))
    )


_NmcNtpLastFailedServer_Type.__name__ = "Integer32"
_NmcNtpLastFailedServer_Object = MibScalar
nmcNtpLastFailedServer = _NmcNtpLastFailedServer_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 2, 10, 8),
    _NmcNtpLastFailedServer_Type()
)
nmcNtpLastFailedServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmcNtpLastFailedServer.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NMC-MIB",
    **{"usr": usr,
       "nas": nas,
       "nmc": nmc,
       "nmcCfg": nmcCfg,
       "nmcCfgSystemTime": nmcCfgSystemTime,
       "nmcCfgSystemDate": nmcCfgSystemDate,
       "nmcGmtime": nmcGmtime,
       "nmcTimezone": nmcTimezone,
       "nmcCfgAuthFailTrapEnable": nmcCfgAuthFailTrapEnable,
       "nmcDaySavingTime": nmcDaySavingTime,
       "nmcCfgWanDialOutPhoneNum": nmcCfgWanDialOutPhoneNum,
       "nmcCfgAtString": nmcCfgAtString,
       "nmcPowerUpAutoCfgEnable": nmcPowerUpAutoCfgEnable,
       "nmcCfgNumWanRetries": nmcCfgNumWanRetries,
       "nmcCfgWanRetryPause": nmcCfgWanRetryPause,
       "nmcCfgWanRetrySuspendTime": nmcCfgWanRetrySuspendTime,
       "nmcCfgNumFailBefSuspend": nmcCfgNumFailBefSuspend,
       "nmcCfgLogSrvrSelect": nmcCfgLogSrvrSelect,
       "nmcCfgLogPriSrvrAddr": nmcCfgLogPriSrvrAddr,
       "nmcCfgLogSecSrvrAddr": nmcCfgLogSecSrvrAddr,
       "nmcCfgLogUdpPortNum": nmcCfgLogUdpPortNum,
       "nmcCfgLogRetryCnt": nmcCfgLogRetryCnt,
       "nmcCfgLogCallStatGrpSel": nmcCfgLogCallStatGrpSel,
       "nmcCfgLogMD5Calc": nmcCfgLogMD5Calc,
       "nmcCfgTFTPTimeout": nmcCfgTFTPTimeout,
       "nmcCfgDnsPriSrvrAddr": nmcCfgDnsPriSrvrAddr,
       "nmcCfgDnsSecSrvrAddr": nmcCfgDnsSecSrvrAddr,
       "nmcCfgLog3SrvrAddr": nmcCfgLog3SrvrAddr,
       "nmcCfgLog4SrvrAddr": nmcCfgLog4SrvrAddr,
       "nmcCfgLog5SrvrAddr": nmcCfgLog5SrvrAddr,
       "nmcCfgLog6SrvrAddr": nmcCfgLog6SrvrAddr,
       "nmcCfgLog7SrvrAddr": nmcCfgLog7SrvrAddr,
       "nmcCfgLog8SrvrAddr": nmcCfgLog8SrvrAddr,
       "nmcCfgLogSrvrName": nmcCfgLogSrvrName,
       "nmcCfgDnsRetryCnt": nmcCfgDnsRetryCnt,
       "nmcCfgDnsUdpPortNum": nmcCfgDnsUdpPortNum,
       "nmcCfgDnsSrvrSelect": nmcCfgDnsSrvrSelect,
       "nmcCfgLogDnsEna": nmcCfgLogDnsEna,
       "nmcCfgLogStatusInterval": nmcCfgLogStatusInterval,
       "nmcCfgDnsSrvrFailure": nmcCfgDnsSrvrFailure,
       "nmcCfgLogSrvrFailure": nmcCfgLogSrvrFailure,
       "nmcCfgSessionIDNewFmt": nmcCfgSessionIDNewFmt,
       "nmcStat": nmcStat,
       "nmcStatStatus": nmcStatStatus,
       "nmcStatDramInstalled": nmcStatDramInstalled,
       "nmcStatNVRAMInstalled": nmcStatNVRAMInstalled,
       "nmcStatEventId": nmcStatEventId,
       "nmcStatTemperature": nmcStatTemperature,
       "nmcStatPowerUpTstFailures": nmcStatPowerUpTstFailures,
       "nmcStatPowerUpTstFailBMap": nmcStatPowerUpTstFailBMap,
       "nmcStatTestResult": nmcStatTestResult,
       "nmcStatCompSwVer": nmcStatCompSwVer,
       "nmcStatPktBusClkSrc": nmcStatPktBusClkSrc,
       "nmcStatNmcPktBusClk": nmcStatNmcPktBusClk,
       "nmcStatRedLed": nmcStatRedLed,
       "nmcAuxIn1Sts": nmcAuxIn1Sts,
       "nmcAuxIn2Sts": nmcAuxIn2Sts,
       "nmcAuxOut1Sts": nmcAuxOut1Sts,
       "nmcAuxOut2Sts": nmcAuxOut2Sts,
       "nmcTrap": nmcTrap,
       "nmcTrapSequenceNumber": nmcTrapSequenceNumber,
       "nmcTrapDestTable": nmcTrapDestTable,
       "nmcTrapDestEntry": nmcTrapDestEntry,
       "nmcTrapDestIP": nmcTrapDestIP,
       "nmcTrapDestCommunity": nmcTrapDestCommunity,
       "nmcTrapDestDescr": nmcTrapDestDescr,
       "nmcArTrapId": nmcArTrapId,
       "nmcCmd": nmcCmd,
       "nmcCmdMgtStationId": nmcCmdMgtStationId,
       "nmcCmdReqId": nmcCmdReqId,
       "nmcCmdFunction": nmcCmdFunction,
       "nmcCmdForce": nmcCmdForce,
       "nmcCmdParam": nmcCmdParam,
       "nmcCmdResult": nmcCmdResult,
       "nmcCmdCode": nmcCmdCode,
       "nmcHs": nmcHs,
       "nmcHsDialInOutNamePrompt": nmcHsDialInOutNamePrompt,
       "nmcHsDialInOutPsswdPrompt": nmcHsDialInOutPsswdPrompt,
       "nmcHsDialBackNamePrompt": nmcHsDialBackNamePrompt,
       "nmcHsDialBackPsswdPrompt": nmcHsDialBackPsswdPrompt,
       "nmcHsDialBackPhonePrompt": nmcHsDialBackPhonePrompt,
       "nmcHsDialBackPendPrompt": nmcHsDialBackPendPrompt,
       "nmcHsMdmSelectPrompt": nmcHsMdmSelectPrompt,
       "nmcHsLoginFailedMsg": nmcHsLoginFailedMsg,
       "nmcHsPhoneRestrictPrompt": nmcHsPhoneRestrictPrompt,
       "nmcHsInvalidMdmSelecMsg": nmcHsInvalidMdmSelecMsg,
       "nmcHsNoMdnsAvailMsg": nmcHsNoMdnsAvailMsg,
       "nmcHsConnectSuccessMsg": nmcHsConnectSuccessMsg,
       "nmcHsNewPasswordPrompt": nmcHsNewPasswordPrompt,
       "nmcHsChangePasswordMsg": nmcHsChangePasswordMsg,
       "nmcHsPromptRspTimeout": nmcHsPromptRspTimeout,
       "nmcHsPromptRspAttempts": nmcHsPromptRspAttempts,
       "nmcHsPromptRspEchoEna": nmcHsPromptRspEchoEna,
       "nmcHsDialBackDelay": nmcHsDialBackDelay,
       "nmcHsDialBackAttempts": nmcHsDialBackAttempts,
       "nmcHsSecuritySrvrAddr": nmcHsSecuritySrvrAddr,
       "nmcHsSecuritySrvrPort": nmcHsSecuritySrvrPort,
       "nmcHsSecuritySrvrRetries": nmcHsSecuritySrvrRetries,
       "nmcHsMdmAttemptLimit": nmcHsMdmAttemptLimit,
       "nmcHsServerUnavailable": nmcHsServerUnavailable,
       "nmcHsServerSelect": nmcHsServerSelect,
       "nmcHsSecondarySrvrAddr": nmcHsSecondarySrvrAddr,
       "nmcHsDiPasswdEnaDis": nmcHsDiPasswdEnaDis,
       "nmcHsSecurity3SrvrAddr": nmcHsSecurity3SrvrAddr,
       "nmcHsSecurity4SrvrAddr": nmcHsSecurity4SrvrAddr,
       "nmcHsSecurity5SrvrAddr": nmcHsSecurity5SrvrAddr,
       "nmcHsSecurity6SrvrAddr": nmcHsSecurity6SrvrAddr,
       "nmcHsSecurity7SrvrAddr": nmcHsSecurity7SrvrAddr,
       "nmcHsSecurity8SrvrAddr": nmcHsSecurity8SrvrAddr,
       "nmcHsSecuritySrvrName": nmcHsSecuritySrvrName,
       "nmcHsSecuritySrvrDnsEna": nmcHsSecuritySrvrDnsEna,
       "nmcHsSecurityStatusInt": nmcHsSecurityStatusInt,
       "nmcHsSecurityFailure": nmcHsSecurityFailure,
       "nmcTe": nmcTe,
       "nmcTeDialOutLoginFail": nmcTeDialOutLoginFail,
       "nmcTeDialInLoginFail": nmcTeDialInLoginFail,
       "nmcTeDialOutRestrictNum": nmcTeDialOutRestrictNum,
       "nmcTeDialBackRestrictNum": nmcTeDialBackRestrictNum,
       "nmcTeUserBlacklist": nmcTeUserBlacklist,
       "nmcTeUserBlacklistLogin": nmcTeUserBlacklistLogin,
       "nmcTeRespAttmptLimExceed": nmcTeRespAttmptLimExceed,
       "nmcTeLoginAttmptLimExceed": nmcTeLoginAttmptLimExceed,
       "nmcTeLogSrvrLoss": nmcTeLogSrvrLoss,
       "nmcTeSecSrvrLoss": nmcTeSecSrvrLoss,
       "nmcTeSinglePbClockFail": nmcTeSinglePbClockFail,
       "nmcTePbClockSwitch": nmcTePbClockSwitch,
       "nmcTePbClockFail": nmcTePbClockFail,
       "nmcTeDnsSrvrLoss": nmcTeDnsSrvrLoss,
       "nmcTeNtpSrvrLoss": nmcTeNtpSrvrLoss,
       "nmcTeNtpSrvrRestore": nmcTeNtpSrvrRestore,
       "nmcTeNtpSrvrDegraded": nmcTeNtpSrvrDegraded,
       "nmcTeDnsSrvrRestore": nmcTeDnsSrvrRestore,
       "nmcTeDnsSrvrDegraded": nmcTeDnsSrvrDegraded,
       "nmcTeLogSrvrRestore": nmcTeLogSrvrRestore,
       "nmcTeLogSrvrGroupOper": nmcTeLogSrvrGroupOper,
       "nmcTeLogSrvrGroupDegr": nmcTeLogSrvrGroupDegr,
       "nmcTeLogSrvrGroupNonOp": nmcTeLogSrvrGroupNonOp,
       "nmcTeSecSrvrRestore": nmcTeSecSrvrRestore,
       "nmcTeSecSrvrGroupOper": nmcTeSecSrvrGroupOper,
       "nmcTeSecSrvrGroupDegr": nmcTeSecSrvrGroupDegr,
       "nmcTeSecSrvrGroupNonOp": nmcTeSecSrvrGroupNonOp,
       "nmcUiCfg": nmcUiCfg,
       "nmcUiCfgLanIPAddr": nmcUiCfgLanIPAddr,
       "nmcUiCfgLanSubnetMask": nmcUiCfgLanSubnetMask,
       "nmcUiCfgWanIPAddr": nmcUiCfgWanIPAddr,
       "nmcUiCfgWanSubnetMask": nmcUiCfgWanSubnetMask,
       "nmcUiCfgDefaultGwyIP": nmcUiCfgDefaultGwyIP,
       "nmcUiCfgLocalTrIeeeAddr": nmcUiCfgLocalTrIeeeAddr,
       "nmcUiCfgPrivateString": nmcUiCfgPrivateString,
       "nmcUiCfgLanIfEnable": nmcUiCfgLanIfEnable,
       "nmcUiCfgPublicString": nmcUiCfgPublicString,
       "nmcUiCfgRouteEnable": nmcUiCfgRouteEnable,
       "nmcUiCfgUiSlipCfg": nmcUiCfgUiSlipCfg,
       "nmcUiCfgWan2IpAddr": nmcUiCfgWan2IpAddr,
       "nmcUiCfgWan2SubnetMask": nmcUiCfgWan2SubnetMask,
       "nmcUiCfgInactiveTime": nmcUiCfgInactiveTime,
       "nmcUiCfgPassword": nmcUiCfgPassword,
       "nmcAuth": nmcAuth,
       "nmcAuthAccTable": nmcAuthAccTable,
       "nmcAuthAccEntry": nmcAuthAccEntry,
       "nmcAuthAccIpAddr": nmcAuthAccIpAddr,
       "nmcAuthAccNetMask": nmcAuthAccNetMask,
       "nmcAuthAccDescr": nmcAuthAccDescr,
       "nmcNtp": nmcNtp,
       "nmcNtpSrvrPrimAddr": nmcNtpSrvrPrimAddr,
       "nmcNtpSrvrSecdAddr": nmcNtpSrvrSecdAddr,
       "nmcNtpSyncInterval": nmcNtpSyncInterval,
       "nmcNtpOperationalMode": nmcNtpOperationalMode,
       "nmcNtpLastSyncTime": nmcNtpLastSyncTime,
       "nmcNtpLastSyncServer": nmcNtpLastSyncServer,
       "nmcNtpLastFailedTime": nmcNtpLastFailedTime,
       "nmcNtpLastFailedServer": nmcNtpLastFailedServer}
)
