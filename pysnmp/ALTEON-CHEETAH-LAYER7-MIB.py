# SNMP MIB module (ALTEON-CHEETAH-LAYER7-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALTEON-CHEETAH-LAYER7-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:37:50 2024
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

(aws_switch,) = mibBuilder.importSymbols(
    "ALTEON-ROOT-MIB",
    "aws-switch")

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

layer7 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5)
)
layer7.setRevisions(
        ("2009-08-05 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Layer7Configs_ObjectIdentity = ObjectIdentity
layer7Configs = _Layer7Configs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1)
)
_UrlCfg_ObjectIdentity = ObjectIdentity
urlCfg = _UrlCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 1)
)
_SlbUrlRedir_ObjectIdentity = ObjectIdentity
slbUrlRedir = _SlbUrlRedir_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 1, 1)
)


class _SlbCurCfgUrlRedirNonGetOrigSrv_Type(Integer32):
    """Custom type slbCurCfgUrlRedirNonGetOrigSrv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SlbCurCfgUrlRedirNonGetOrigSrv_Type.__name__ = "Integer32"
_SlbCurCfgUrlRedirNonGetOrigSrv_Object = MibScalar
slbCurCfgUrlRedirNonGetOrigSrv = _SlbCurCfgUrlRedirNonGetOrigSrv_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 1, 1, 3),
    _SlbCurCfgUrlRedirNonGetOrigSrv_Type()
)
slbCurCfgUrlRedirNonGetOrigSrv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgUrlRedirNonGetOrigSrv.setStatus("current")


class _SlbNewCfgUrlRedirNonGetOrigSrv_Type(Integer32):
    """Custom type slbNewCfgUrlRedirNonGetOrigSrv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SlbNewCfgUrlRedirNonGetOrigSrv_Type.__name__ = "Integer32"
_SlbNewCfgUrlRedirNonGetOrigSrv_Object = MibScalar
slbNewCfgUrlRedirNonGetOrigSrv = _SlbNewCfgUrlRedirNonGetOrigSrv_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 1, 1, 4),
    _SlbNewCfgUrlRedirNonGetOrigSrv_Type()
)
slbNewCfgUrlRedirNonGetOrigSrv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgUrlRedirNonGetOrigSrv.setStatus("current")


class _SlbCurCfgUrlRedirCookieOrigSrv_Type(Integer32):
    """Custom type slbCurCfgUrlRedirCookieOrigSrv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SlbCurCfgUrlRedirCookieOrigSrv_Type.__name__ = "Integer32"
_SlbCurCfgUrlRedirCookieOrigSrv_Object = MibScalar
slbCurCfgUrlRedirCookieOrigSrv = _SlbCurCfgUrlRedirCookieOrigSrv_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 1, 1, 5),
    _SlbCurCfgUrlRedirCookieOrigSrv_Type()
)
slbCurCfgUrlRedirCookieOrigSrv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgUrlRedirCookieOrigSrv.setStatus("current")


class _SlbNewCfgUrlRedirCookieOrigSrv_Type(Integer32):
    """Custom type slbNewCfgUrlRedirCookieOrigSrv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SlbNewCfgUrlRedirCookieOrigSrv_Type.__name__ = "Integer32"
_SlbNewCfgUrlRedirCookieOrigSrv_Object = MibScalar
slbNewCfgUrlRedirCookieOrigSrv = _SlbNewCfgUrlRedirCookieOrigSrv_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 1, 1, 6),
    _SlbNewCfgUrlRedirCookieOrigSrv_Type()
)
slbNewCfgUrlRedirCookieOrigSrv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgUrlRedirCookieOrigSrv.setStatus("current")


class _SlbCurCfgUrlRedirNoCacheOrigSrv_Type(Integer32):
    """Custom type slbCurCfgUrlRedirNoCacheOrigSrv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SlbCurCfgUrlRedirNoCacheOrigSrv_Type.__name__ = "Integer32"
_SlbCurCfgUrlRedirNoCacheOrigSrv_Object = MibScalar
slbCurCfgUrlRedirNoCacheOrigSrv = _SlbCurCfgUrlRedirNoCacheOrigSrv_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 1, 1, 7),
    _SlbCurCfgUrlRedirNoCacheOrigSrv_Type()
)
slbCurCfgUrlRedirNoCacheOrigSrv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgUrlRedirNoCacheOrigSrv.setStatus("current")


class _SlbNewCfgUrlRedirNoCacheOrigSrv_Type(Integer32):
    """Custom type slbNewCfgUrlRedirNoCacheOrigSrv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SlbNewCfgUrlRedirNoCacheOrigSrv_Type.__name__ = "Integer32"
_SlbNewCfgUrlRedirNoCacheOrigSrv_Object = MibScalar
slbNewCfgUrlRedirNoCacheOrigSrv = _SlbNewCfgUrlRedirNoCacheOrigSrv_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 1, 1, 8),
    _SlbNewCfgUrlRedirNoCacheOrigSrv_Type()
)
slbNewCfgUrlRedirNoCacheOrigSrv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgUrlRedirNoCacheOrigSrv.setStatus("current")


class _SlbCurCfgUrlRedirUriHashLength_Type(Integer32):
    """Custom type slbCurCfgUrlRedirUriHashLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SlbCurCfgUrlRedirUriHashLength_Type.__name__ = "Integer32"
_SlbCurCfgUrlRedirUriHashLength_Object = MibScalar
slbCurCfgUrlRedirUriHashLength = _SlbCurCfgUrlRedirUriHashLength_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 1, 1, 9),
    _SlbCurCfgUrlRedirUriHashLength_Type()
)
slbCurCfgUrlRedirUriHashLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgUrlRedirUriHashLength.setStatus("current")


class _SlbNewCfgUrlRedirUriHashLength_Type(Integer32):
    """Custom type slbNewCfgUrlRedirUriHashLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SlbNewCfgUrlRedirUriHashLength_Type.__name__ = "Integer32"
_SlbNewCfgUrlRedirUriHashLength_Object = MibScalar
slbNewCfgUrlRedirUriHashLength = _SlbNewCfgUrlRedirUriHashLength_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 1, 1, 10),
    _SlbNewCfgUrlRedirUriHashLength_Type()
)
slbNewCfgUrlRedirUriHashLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgUrlRedirUriHashLength.setStatus("current")


class _SlbCurCfgUrlRedirHeader_Type(Integer32):
    """Custom type slbCurCfgUrlRedirHeader based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SlbCurCfgUrlRedirHeader_Type.__name__ = "Integer32"
_SlbCurCfgUrlRedirHeader_Object = MibScalar
slbCurCfgUrlRedirHeader = _SlbCurCfgUrlRedirHeader_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 1, 1, 11),
    _SlbCurCfgUrlRedirHeader_Type()
)
slbCurCfgUrlRedirHeader.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgUrlRedirHeader.setStatus("current")


class _SlbNewCfgUrlRedirHeader_Type(Integer32):
    """Custom type slbNewCfgUrlRedirHeader based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SlbNewCfgUrlRedirHeader_Type.__name__ = "Integer32"
_SlbNewCfgUrlRedirHeader_Object = MibScalar
slbNewCfgUrlRedirHeader = _SlbNewCfgUrlRedirHeader_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 1, 1, 12),
    _SlbNewCfgUrlRedirHeader_Type()
)
slbNewCfgUrlRedirHeader.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgUrlRedirHeader.setStatus("current")


class _SlbCurCfgUrlRedirHeaderName_Type(DisplayString):
    """Custom type slbCurCfgUrlRedirHeaderName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SlbCurCfgUrlRedirHeaderName_Type.__name__ = "DisplayString"
_SlbCurCfgUrlRedirHeaderName_Object = MibScalar
slbCurCfgUrlRedirHeaderName = _SlbCurCfgUrlRedirHeaderName_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 1, 1, 13),
    _SlbCurCfgUrlRedirHeaderName_Type()
)
slbCurCfgUrlRedirHeaderName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgUrlRedirHeaderName.setStatus("current")


class _SlbNewCfgUrlRedirHeaderName_Type(DisplayString):
    """Custom type slbNewCfgUrlRedirHeaderName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SlbNewCfgUrlRedirHeaderName_Type.__name__ = "DisplayString"
_SlbNewCfgUrlRedirHeaderName_Object = MibScalar
slbNewCfgUrlRedirHeaderName = _SlbNewCfgUrlRedirHeaderName_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 1, 1, 14),
    _SlbNewCfgUrlRedirHeaderName_Type()
)
slbNewCfgUrlRedirHeaderName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgUrlRedirHeaderName.setStatus("current")


class _SlbCurCfgUrlHashing_Type(Integer32):
    """Custom type slbCurCfgUrlHashing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SlbCurCfgUrlHashing_Type.__name__ = "Integer32"
_SlbCurCfgUrlHashing_Object = MibScalar
slbCurCfgUrlHashing = _SlbCurCfgUrlHashing_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 1, 1, 15),
    _SlbCurCfgUrlHashing_Type()
)
slbCurCfgUrlHashing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgUrlHashing.setStatus("current")


class _SlbNewCfgUrlHashing_Type(Integer32):
    """Custom type slbNewCfgUrlHashing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SlbNewCfgUrlHashing_Type.__name__ = "Integer32"
_SlbNewCfgUrlHashing_Object = MibScalar
slbNewCfgUrlHashing = _SlbNewCfgUrlHashing_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 1, 1, 16),
    _SlbNewCfgUrlHashing_Type()
)
slbNewCfgUrlHashing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgUrlHashing.setStatus("current")


class _SlbCurCfgUrlRedirHeaderNameType_Type(Integer32):
    """Custom type slbCurCfgUrlRedirHeaderNameType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("host", 1),
          ("others", 3),
          ("useragent", 2))
    )


_SlbCurCfgUrlRedirHeaderNameType_Type.__name__ = "Integer32"
_SlbCurCfgUrlRedirHeaderNameType_Object = MibScalar
slbCurCfgUrlRedirHeaderNameType = _SlbCurCfgUrlRedirHeaderNameType_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 1, 1, 17),
    _SlbCurCfgUrlRedirHeaderNameType_Type()
)
slbCurCfgUrlRedirHeaderNameType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgUrlRedirHeaderNameType.setStatus("current")


class _SlbNewCfgUrlRedirHeaderNameType_Type(Integer32):
    """Custom type slbNewCfgUrlRedirHeaderNameType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("host", 1),
          ("others", 3),
          ("useragent", 2))
    )


_SlbNewCfgUrlRedirHeaderNameType_Type.__name__ = "Integer32"
_SlbNewCfgUrlRedirHeaderNameType_Object = MibScalar
slbNewCfgUrlRedirHeaderNameType = _SlbNewCfgUrlRedirHeaderNameType_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 1, 1, 18),
    _SlbNewCfgUrlRedirHeaderNameType_Type()
)
slbNewCfgUrlRedirHeaderNameType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgUrlRedirHeaderNameType.setStatus("current")
_SlbUrlBalance_ObjectIdentity = ObjectIdentity
slbUrlBalance = _SlbUrlBalance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 1, 2)
)
_SlbUrlLbPathTableMaxSize_Type = Integer32
_SlbUrlLbPathTableMaxSize_Object = MibScalar
slbUrlLbPathTableMaxSize = _SlbUrlLbPathTableMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 1, 2, 1),
    _SlbUrlLbPathTableMaxSize_Type()
)
slbUrlLbPathTableMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbUrlLbPathTableMaxSize.setStatus("current")
_SlbCurCfgUrlLbPathTable_Object = MibTable
slbCurCfgUrlLbPathTable = _SlbCurCfgUrlLbPathTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    slbCurCfgUrlLbPathTable.setStatus("current")
_SlbCurCfgUrlLbPathTableEntry_Object = MibTableRow
slbCurCfgUrlLbPathTableEntry = _SlbCurCfgUrlLbPathTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 1, 2, 2, 1)
)
slbCurCfgUrlLbPathTableEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-LAYER7-MIB", "slbCurCfgUrlLbPathIndex"),
)
if mibBuilder.loadTexts:
    slbCurCfgUrlLbPathTableEntry.setStatus("current")
_SlbCurCfgUrlLbPathIndex_Type = Integer32
_SlbCurCfgUrlLbPathIndex_Object = MibTableColumn
slbCurCfgUrlLbPathIndex = _SlbCurCfgUrlLbPathIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 1, 2, 2, 1, 1),
    _SlbCurCfgUrlLbPathIndex_Type()
)
slbCurCfgUrlLbPathIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgUrlLbPathIndex.setStatus("current")


class _SlbCurCfgUrlLbPathString_Type(DisplayString):
    """Custom type slbCurCfgUrlLbPathString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 96),
    )


_SlbCurCfgUrlLbPathString_Type.__name__ = "DisplayString"
_SlbCurCfgUrlLbPathString_Object = MibTableColumn
slbCurCfgUrlLbPathString = _SlbCurCfgUrlLbPathString_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 1, 2, 2, 1, 2),
    _SlbCurCfgUrlLbPathString_Type()
)
slbCurCfgUrlLbPathString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgUrlLbPathString.setStatus("current")
_SlbCurCfgUrlLbBwmContract_Type = Integer32
_SlbCurCfgUrlLbBwmContract_Object = MibTableColumn
slbCurCfgUrlLbBwmContract = _SlbCurCfgUrlLbBwmContract_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 1, 2, 2, 1, 3),
    _SlbCurCfgUrlLbBwmContract_Type()
)
slbCurCfgUrlLbBwmContract.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgUrlLbBwmContract.setStatus("current")


class _SlbCurCfgUrlLbPathHTTPHeader_Type(DisplayString):
    """Custom type slbCurCfgUrlLbPathHTTPHeader based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SlbCurCfgUrlLbPathHTTPHeader_Type.__name__ = "DisplayString"
_SlbCurCfgUrlLbPathHTTPHeader_Object = MibTableColumn
slbCurCfgUrlLbPathHTTPHeader = _SlbCurCfgUrlLbPathHTTPHeader_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 1, 2, 2, 1, 4),
    _SlbCurCfgUrlLbPathHTTPHeader_Type()
)
slbCurCfgUrlLbPathHTTPHeader.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgUrlLbPathHTTPHeader.setStatus("current")


class _SlbCurCfgUrlLbPathHTTPHeaderValue_Type(DisplayString):
    """Custom type slbCurCfgUrlLbPathHTTPHeaderValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_SlbCurCfgUrlLbPathHTTPHeaderValue_Type.__name__ = "DisplayString"
_SlbCurCfgUrlLbPathHTTPHeaderValue_Object = MibTableColumn
slbCurCfgUrlLbPathHTTPHeaderValue = _SlbCurCfgUrlLbPathHTTPHeaderValue_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 1, 2, 2, 1, 5),
    _SlbCurCfgUrlLbPathHTTPHeaderValue_Type()
)
slbCurCfgUrlLbPathHTTPHeaderValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgUrlLbPathHTTPHeaderValue.setStatus("current")


class _SlbCurCfgUrlLbPathPatternStringType_Type(Integer32):
    """Custom type slbCurCfgUrlLbPathPatternStringType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ascii", 1),
          ("binary", 2),
          ("none", 3))
    )


_SlbCurCfgUrlLbPathPatternStringType_Type.__name__ = "Integer32"
_SlbCurCfgUrlLbPathPatternStringType_Object = MibTableColumn
slbCurCfgUrlLbPathPatternStringType = _SlbCurCfgUrlLbPathPatternStringType_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 1, 2, 2, 1, 6),
    _SlbCurCfgUrlLbPathPatternStringType_Type()
)
slbCurCfgUrlLbPathPatternStringType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgUrlLbPathPatternStringType.setStatus("current")


class _SlbCurCfgUrlLbPathOffset_Type(Integer32):
    """Custom type slbCurCfgUrlLbPathOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1500),
    )


_SlbCurCfgUrlLbPathOffset_Type.__name__ = "Integer32"
_SlbCurCfgUrlLbPathOffset_Object = MibTableColumn
slbCurCfgUrlLbPathOffset = _SlbCurCfgUrlLbPathOffset_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 1, 2, 2, 1, 7),
    _SlbCurCfgUrlLbPathOffset_Type()
)
slbCurCfgUrlLbPathOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgUrlLbPathOffset.setStatus("current")


class _SlbCurCfgUrlLbPathDepth_Type(Integer32):
    """Custom type slbCurCfgUrlLbPathDepth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1500),
    )


_SlbCurCfgUrlLbPathDepth_Type.__name__ = "Integer32"
_SlbCurCfgUrlLbPathDepth_Object = MibTableColumn
slbCurCfgUrlLbPathDepth = _SlbCurCfgUrlLbPathDepth_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 1, 2, 2, 1, 8),
    _SlbCurCfgUrlLbPathDepth_Type()
)
slbCurCfgUrlLbPathDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgUrlLbPathDepth.setStatus("current")


class _SlbCurCfgUrlLbPathOper_Type(Integer32):
    """Custom type slbCurCfgUrlLbPathOper based on Integer32"""
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
        *(("eq", 1),
          ("gt", 2),
          ("lt", 3),
          ("none", 4))
    )


_SlbCurCfgUrlLbPathOper_Type.__name__ = "Integer32"
_SlbCurCfgUrlLbPathOper_Object = MibTableColumn
slbCurCfgUrlLbPathOper = _SlbCurCfgUrlLbPathOper_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 1, 2, 2, 1, 9),
    _SlbCurCfgUrlLbPathOper_Type()
)
slbCurCfgUrlLbPathOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgUrlLbPathOper.setStatus("current")


class _SlbCurCfgUrlLbPathDnsQueryTypes_Type(DisplayString):
    """Custom type slbCurCfgUrlLbPathDnsQueryTypes based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 96),
    )


_SlbCurCfgUrlLbPathDnsQueryTypes_Type.__name__ = "DisplayString"
_SlbCurCfgUrlLbPathDnsQueryTypes_Object = MibTableColumn
slbCurCfgUrlLbPathDnsQueryTypes = _SlbCurCfgUrlLbPathDnsQueryTypes_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 1, 2, 2, 1, 10),
    _SlbCurCfgUrlLbPathDnsQueryTypes_Type()
)
slbCurCfgUrlLbPathDnsQueryTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgUrlLbPathDnsQueryTypes.setStatus("current")


class _SlbCurCfgUrlLbPathCompleteString_Type(DisplayString):
    """Custom type slbCurCfgUrlLbPathCompleteString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SlbCurCfgUrlLbPathCompleteString_Type.__name__ = "DisplayString"
_SlbCurCfgUrlLbPathCompleteString_Object = MibTableColumn
slbCurCfgUrlLbPathCompleteString = _SlbCurCfgUrlLbPathCompleteString_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 1, 2, 2, 1, 11),
    _SlbCurCfgUrlLbPathCompleteString_Type()
)
slbCurCfgUrlLbPathCompleteString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgUrlLbPathCompleteString.setStatus("current")


class _SlbCurCfgUrlLbPathAllowRegExp_Type(Integer32):
    """Custom type slbCurCfgUrlLbPathAllowRegExp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_SlbCurCfgUrlLbPathAllowRegExp_Type.__name__ = "Integer32"
_SlbCurCfgUrlLbPathAllowRegExp_Object = MibTableColumn
slbCurCfgUrlLbPathAllowRegExp = _SlbCurCfgUrlLbPathAllowRegExp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 1, 2, 2, 1, 12),
    _SlbCurCfgUrlLbPathAllowRegExp_Type()
)
slbCurCfgUrlLbPathAllowRegExp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgUrlLbPathAllowRegExp.setStatus("current")


class _SlbCurCfgUrlLbPathDnsType_Type(Integer32):
    """Custom type slbCurCfgUrlLbPathDnsType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("any", 3),
          ("dns", 1),
          ("dnssec", 2))
    )


_SlbCurCfgUrlLbPathDnsType_Type.__name__ = "Integer32"
_SlbCurCfgUrlLbPathDnsType_Object = MibTableColumn
slbCurCfgUrlLbPathDnsType = _SlbCurCfgUrlLbPathDnsType_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 1, 2, 2, 1, 13),
    _SlbCurCfgUrlLbPathDnsType_Type()
)
slbCurCfgUrlLbPathDnsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgUrlLbPathDnsType.setStatus("current")


class _SlbCurCfgUrlLbPathApplication_Type(Integer32):
    """Custom type slbCurCfgUrlLbPathApplication based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dns", 2),
          ("http", 1),
          ("other", 3))
    )


_SlbCurCfgUrlLbPathApplication_Type.__name__ = "Integer32"
_SlbCurCfgUrlLbPathApplication_Object = MibTableColumn
slbCurCfgUrlLbPathApplication = _SlbCurCfgUrlLbPathApplication_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 1, 2, 2, 1, 14),
    _SlbCurCfgUrlLbPathApplication_Type()
)
slbCurCfgUrlLbPathApplication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgUrlLbPathApplication.setStatus("current")
_SlbNewCfgUrlLbPathTable_Object = MibTable
slbNewCfgUrlLbPathTable = _SlbNewCfgUrlLbPathTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 1, 2, 3)
)
if mibBuilder.loadTexts:
    slbNewCfgUrlLbPathTable.setStatus("current")
_SlbNewCfgUrlLbPathTableEntry_Object = MibTableRow
slbNewCfgUrlLbPathTableEntry = _SlbNewCfgUrlLbPathTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 1, 2, 3, 1)
)
slbNewCfgUrlLbPathTableEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-LAYER7-MIB", "slbNewCfgUrlLbPathIndex"),
)
if mibBuilder.loadTexts:
    slbNewCfgUrlLbPathTableEntry.setStatus("current")
_SlbNewCfgUrlLbPathIndex_Type = Integer32
_SlbNewCfgUrlLbPathIndex_Object = MibTableColumn
slbNewCfgUrlLbPathIndex = _SlbNewCfgUrlLbPathIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 1, 2, 3, 1, 1),
    _SlbNewCfgUrlLbPathIndex_Type()
)
slbNewCfgUrlLbPathIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbNewCfgUrlLbPathIndex.setStatus("current")


class _SlbNewCfgUrlLbPathString_Type(DisplayString):
    """Custom type slbNewCfgUrlLbPathString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 96),
    )


_SlbNewCfgUrlLbPathString_Type.__name__ = "DisplayString"
_SlbNewCfgUrlLbPathString_Object = MibTableColumn
slbNewCfgUrlLbPathString = _SlbNewCfgUrlLbPathString_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 1, 2, 3, 1, 2),
    _SlbNewCfgUrlLbPathString_Type()
)
slbNewCfgUrlLbPathString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgUrlLbPathString.setStatus("current")


class _SlbNewCfgUrlLbPathDelete_Type(Integer32):
    """Custom type slbNewCfgUrlLbPathDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delete", 2),
          ("other", 1))
    )


_SlbNewCfgUrlLbPathDelete_Type.__name__ = "Integer32"
_SlbNewCfgUrlLbPathDelete_Object = MibTableColumn
slbNewCfgUrlLbPathDelete = _SlbNewCfgUrlLbPathDelete_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 1, 2, 3, 1, 3),
    _SlbNewCfgUrlLbPathDelete_Type()
)
slbNewCfgUrlLbPathDelete.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgUrlLbPathDelete.setStatus("current")
_SlbNewCfgUrlLbBwmContract_Type = Integer32
_SlbNewCfgUrlLbBwmContract_Object = MibTableColumn
slbNewCfgUrlLbBwmContract = _SlbNewCfgUrlLbBwmContract_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 1, 2, 3, 1, 4),
    _SlbNewCfgUrlLbBwmContract_Type()
)
slbNewCfgUrlLbBwmContract.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgUrlLbBwmContract.setStatus("current")


class _SlbNewCfgUrlLbPathHTTPHeader_Type(DisplayString):
    """Custom type slbNewCfgUrlLbPathHTTPHeader based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_SlbNewCfgUrlLbPathHTTPHeader_Type.__name__ = "DisplayString"
_SlbNewCfgUrlLbPathHTTPHeader_Object = MibTableColumn
slbNewCfgUrlLbPathHTTPHeader = _SlbNewCfgUrlLbPathHTTPHeader_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 1, 2, 3, 1, 5),
    _SlbNewCfgUrlLbPathHTTPHeader_Type()
)
slbNewCfgUrlLbPathHTTPHeader.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgUrlLbPathHTTPHeader.setStatus("current")


class _SlbNewCfgUrlLbPathHTTPHeaderValue_Type(DisplayString):
    """Custom type slbNewCfgUrlLbPathHTTPHeaderValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_SlbNewCfgUrlLbPathHTTPHeaderValue_Type.__name__ = "DisplayString"
_SlbNewCfgUrlLbPathHTTPHeaderValue_Object = MibTableColumn
slbNewCfgUrlLbPathHTTPHeaderValue = _SlbNewCfgUrlLbPathHTTPHeaderValue_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 1, 2, 3, 1, 6),
    _SlbNewCfgUrlLbPathHTTPHeaderValue_Type()
)
slbNewCfgUrlLbPathHTTPHeaderValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgUrlLbPathHTTPHeaderValue.setStatus("current")


class _SlbNewCfgUrlLbPathPatternStringType_Type(Integer32):
    """Custom type slbNewCfgUrlLbPathPatternStringType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ascii", 1),
          ("binary", 2),
          ("none", 3))
    )


_SlbNewCfgUrlLbPathPatternStringType_Type.__name__ = "Integer32"
_SlbNewCfgUrlLbPathPatternStringType_Object = MibTableColumn
slbNewCfgUrlLbPathPatternStringType = _SlbNewCfgUrlLbPathPatternStringType_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 1, 2, 3, 1, 7),
    _SlbNewCfgUrlLbPathPatternStringType_Type()
)
slbNewCfgUrlLbPathPatternStringType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgUrlLbPathPatternStringType.setStatus("current")


class _SlbNewCfgUrlLbPathOffset_Type(Integer32):
    """Custom type slbNewCfgUrlLbPathOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1500),
    )


_SlbNewCfgUrlLbPathOffset_Type.__name__ = "Integer32"
_SlbNewCfgUrlLbPathOffset_Object = MibTableColumn
slbNewCfgUrlLbPathOffset = _SlbNewCfgUrlLbPathOffset_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 1, 2, 3, 1, 8),
    _SlbNewCfgUrlLbPathOffset_Type()
)
slbNewCfgUrlLbPathOffset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgUrlLbPathOffset.setStatus("current")


class _SlbNewCfgUrlLbPathDepth_Type(Integer32):
    """Custom type slbNewCfgUrlLbPathDepth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1500),
    )


_SlbNewCfgUrlLbPathDepth_Type.__name__ = "Integer32"
_SlbNewCfgUrlLbPathDepth_Object = MibTableColumn
slbNewCfgUrlLbPathDepth = _SlbNewCfgUrlLbPathDepth_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 1, 2, 3, 1, 9),
    _SlbNewCfgUrlLbPathDepth_Type()
)
slbNewCfgUrlLbPathDepth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgUrlLbPathDepth.setStatus("current")


class _SlbNewCfgUrlLbPathOper_Type(Integer32):
    """Custom type slbNewCfgUrlLbPathOper based on Integer32"""
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
        *(("eq", 1),
          ("gt", 2),
          ("lt", 3),
          ("none", 4))
    )


_SlbNewCfgUrlLbPathOper_Type.__name__ = "Integer32"
_SlbNewCfgUrlLbPathOper_Object = MibTableColumn
slbNewCfgUrlLbPathOper = _SlbNewCfgUrlLbPathOper_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 1, 2, 3, 1, 10),
    _SlbNewCfgUrlLbPathOper_Type()
)
slbNewCfgUrlLbPathOper.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgUrlLbPathOper.setStatus("current")


class _SlbNewCfgUrlLbPathDnsQueryTypes_Type(DisplayString):
    """Custom type slbNewCfgUrlLbPathDnsQueryTypes based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 96),
    )


_SlbNewCfgUrlLbPathDnsQueryTypes_Type.__name__ = "DisplayString"
_SlbNewCfgUrlLbPathDnsQueryTypes_Object = MibTableColumn
slbNewCfgUrlLbPathDnsQueryTypes = _SlbNewCfgUrlLbPathDnsQueryTypes_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 1, 2, 3, 1, 11),
    _SlbNewCfgUrlLbPathDnsQueryTypes_Type()
)
slbNewCfgUrlLbPathDnsQueryTypes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgUrlLbPathDnsQueryTypes.setStatus("current")


class _SlbNewCfgUrlLbPathCompleteString_Type(DisplayString):
    """Custom type slbNewCfgUrlLbPathCompleteString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SlbNewCfgUrlLbPathCompleteString_Type.__name__ = "DisplayString"
_SlbNewCfgUrlLbPathCompleteString_Object = MibTableColumn
slbNewCfgUrlLbPathCompleteString = _SlbNewCfgUrlLbPathCompleteString_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 1, 2, 3, 1, 12),
    _SlbNewCfgUrlLbPathCompleteString_Type()
)
slbNewCfgUrlLbPathCompleteString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbNewCfgUrlLbPathCompleteString.setStatus("current")


class _SlbNewCfgUrlLbPathAllowRegExp_Type(Integer32):
    """Custom type slbNewCfgUrlLbPathAllowRegExp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_SlbNewCfgUrlLbPathAllowRegExp_Type.__name__ = "Integer32"
_SlbNewCfgUrlLbPathAllowRegExp_Object = MibTableColumn
slbNewCfgUrlLbPathAllowRegExp = _SlbNewCfgUrlLbPathAllowRegExp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 1, 2, 3, 1, 13),
    _SlbNewCfgUrlLbPathAllowRegExp_Type()
)
slbNewCfgUrlLbPathAllowRegExp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgUrlLbPathAllowRegExp.setStatus("current")


class _SlbNewCfgUrlLbPathDnsType_Type(Integer32):
    """Custom type slbNewCfgUrlLbPathDnsType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("any", 3),
          ("dns", 1),
          ("dnssec", 2))
    )


_SlbNewCfgUrlLbPathDnsType_Type.__name__ = "Integer32"
_SlbNewCfgUrlLbPathDnsType_Object = MibTableColumn
slbNewCfgUrlLbPathDnsType = _SlbNewCfgUrlLbPathDnsType_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 1, 2, 3, 1, 14),
    _SlbNewCfgUrlLbPathDnsType_Type()
)
slbNewCfgUrlLbPathDnsType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgUrlLbPathDnsType.setStatus("current")


class _SlbNewCfgUrlLbPathApplication_Type(Integer32):
    """Custom type slbNewCfgUrlLbPathApplication based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dns", 2),
          ("http", 1),
          ("other", 3))
    )


_SlbNewCfgUrlLbPathApplication_Type.__name__ = "Integer32"
_SlbNewCfgUrlLbPathApplication_Object = MibTableColumn
slbNewCfgUrlLbPathApplication = _SlbNewCfgUrlLbPathApplication_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 1, 2, 3, 1, 15),
    _SlbNewCfgUrlLbPathApplication_Type()
)
slbNewCfgUrlLbPathApplication.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgUrlLbPathApplication.setStatus("current")


class _SlbCurCfgUrlLbErrorMsg_Type(DisplayString):
    """Custom type slbCurCfgUrlLbErrorMsg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SlbCurCfgUrlLbErrorMsg_Type.__name__ = "DisplayString"
_SlbCurCfgUrlLbErrorMsg_Object = MibScalar
slbCurCfgUrlLbErrorMsg = _SlbCurCfgUrlLbErrorMsg_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 1, 2, 4),
    _SlbCurCfgUrlLbErrorMsg_Type()
)
slbCurCfgUrlLbErrorMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgUrlLbErrorMsg.setStatus("current")


class _SlbNewCfgUrlLbErrorMsg_Type(DisplayString):
    """Custom type slbNewCfgUrlLbErrorMsg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SlbNewCfgUrlLbErrorMsg_Type.__name__ = "DisplayString"
_SlbNewCfgUrlLbErrorMsg_Object = MibScalar
slbNewCfgUrlLbErrorMsg = _SlbNewCfgUrlLbErrorMsg_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 1, 2, 5),
    _SlbNewCfgUrlLbErrorMsg_Type()
)
slbNewCfgUrlLbErrorMsg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgUrlLbErrorMsg.setStatus("current")


class _SlbCurCfgUrlLbCaseSensitiveStrMatch_Type(Integer32):
    """Custom type slbCurCfgUrlLbCaseSensitiveStrMatch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SlbCurCfgUrlLbCaseSensitiveStrMatch_Type.__name__ = "Integer32"
_SlbCurCfgUrlLbCaseSensitiveStrMatch_Object = MibScalar
slbCurCfgUrlLbCaseSensitiveStrMatch = _SlbCurCfgUrlLbCaseSensitiveStrMatch_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 1, 2, 6),
    _SlbCurCfgUrlLbCaseSensitiveStrMatch_Type()
)
slbCurCfgUrlLbCaseSensitiveStrMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgUrlLbCaseSensitiveStrMatch.setStatus("current")


class _SlbNewCfgUrlLbCaseSensitiveStrMatch_Type(Integer32):
    """Custom type slbNewCfgUrlLbCaseSensitiveStrMatch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SlbNewCfgUrlLbCaseSensitiveStrMatch_Type.__name__ = "Integer32"
_SlbNewCfgUrlLbCaseSensitiveStrMatch_Object = MibScalar
slbNewCfgUrlLbCaseSensitiveStrMatch = _SlbNewCfgUrlLbCaseSensitiveStrMatch_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 1, 2, 7),
    _SlbNewCfgUrlLbCaseSensitiveStrMatch_Type()
)
slbNewCfgUrlLbCaseSensitiveStrMatch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgUrlLbCaseSensitiveStrMatch.setStatus("current")
_SlbUrlHttpMethods_ObjectIdentity = ObjectIdentity
slbUrlHttpMethods = _SlbUrlHttpMethods_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 1, 3)
)
_SlbUrlHttpMethodsTableMaxSize_Type = Integer32
_SlbUrlHttpMethodsTableMaxSize_Object = MibScalar
slbUrlHttpMethodsTableMaxSize = _SlbUrlHttpMethodsTableMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 1, 3, 1),
    _SlbUrlHttpMethodsTableMaxSize_Type()
)
slbUrlHttpMethodsTableMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbUrlHttpMethodsTableMaxSize.setStatus("current")
_SlbCurCfgUrlHttpMethodsTable_Object = MibTable
slbCurCfgUrlHttpMethodsTable = _SlbCurCfgUrlHttpMethodsTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 1, 3, 2)
)
if mibBuilder.loadTexts:
    slbCurCfgUrlHttpMethodsTable.setStatus("current")
_SlbCurCfgUrlHttpMethodsTableEntry_Object = MibTableRow
slbCurCfgUrlHttpMethodsTableEntry = _SlbCurCfgUrlHttpMethodsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 1, 3, 2, 1)
)
slbCurCfgUrlHttpMethodsTableEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-LAYER7-MIB", "slbCurCfgUrlHttpMethodIndex"),
)
if mibBuilder.loadTexts:
    slbCurCfgUrlHttpMethodsTableEntry.setStatus("current")
_SlbCurCfgUrlHttpMethodIndex_Type = Integer32
_SlbCurCfgUrlHttpMethodIndex_Object = MibTableColumn
slbCurCfgUrlHttpMethodIndex = _SlbCurCfgUrlHttpMethodIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 1, 3, 2, 1, 1),
    _SlbCurCfgUrlHttpMethodIndex_Type()
)
slbCurCfgUrlHttpMethodIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgUrlHttpMethodIndex.setStatus("current")


class _SlbCurCfgUrlHttpMethodString_Type(DisplayString):
    """Custom type slbCurCfgUrlHttpMethodString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SlbCurCfgUrlHttpMethodString_Type.__name__ = "DisplayString"
_SlbCurCfgUrlHttpMethodString_Object = MibTableColumn
slbCurCfgUrlHttpMethodString = _SlbCurCfgUrlHttpMethodString_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 1, 3, 2, 1, 2),
    _SlbCurCfgUrlHttpMethodString_Type()
)
slbCurCfgUrlHttpMethodString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgUrlHttpMethodString.setStatus("current")
_SlbNewCfgUrlHttpMethodsTable_Object = MibTable
slbNewCfgUrlHttpMethodsTable = _SlbNewCfgUrlHttpMethodsTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 1, 3, 3)
)
if mibBuilder.loadTexts:
    slbNewCfgUrlHttpMethodsTable.setStatus("current")
_SlbNewCfgUrlHttpMethodsTableEntry_Object = MibTableRow
slbNewCfgUrlHttpMethodsTableEntry = _SlbNewCfgUrlHttpMethodsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 1, 3, 3, 1)
)
slbNewCfgUrlHttpMethodsTableEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-LAYER7-MIB", "slbNewCfgUrlHttpMethodIndex"),
)
if mibBuilder.loadTexts:
    slbNewCfgUrlHttpMethodsTableEntry.setStatus("current")
_SlbNewCfgUrlHttpMethodIndex_Type = Integer32
_SlbNewCfgUrlHttpMethodIndex_Object = MibTableColumn
slbNewCfgUrlHttpMethodIndex = _SlbNewCfgUrlHttpMethodIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 1, 3, 3, 1, 1),
    _SlbNewCfgUrlHttpMethodIndex_Type()
)
slbNewCfgUrlHttpMethodIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbNewCfgUrlHttpMethodIndex.setStatus("current")


class _SlbNewCfgUrlHttpMethodString_Type(DisplayString):
    """Custom type slbNewCfgUrlHttpMethodString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SlbNewCfgUrlHttpMethodString_Type.__name__ = "DisplayString"
_SlbNewCfgUrlHttpMethodString_Object = MibTableColumn
slbNewCfgUrlHttpMethodString = _SlbNewCfgUrlHttpMethodString_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 1, 3, 3, 1, 2),
    _SlbNewCfgUrlHttpMethodString_Type()
)
slbNewCfgUrlHttpMethodString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgUrlHttpMethodString.setStatus("current")


class _SlbNewCfgUrlHttpMethodDelete_Type(Integer32):
    """Custom type slbNewCfgUrlHttpMethodDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delete", 2),
          ("other", 1))
    )


_SlbNewCfgUrlHttpMethodDelete_Type.__name__ = "Integer32"
_SlbNewCfgUrlHttpMethodDelete_Object = MibTableColumn
slbNewCfgUrlHttpMethodDelete = _SlbNewCfgUrlHttpMethodDelete_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 1, 3, 3, 1, 3),
    _SlbNewCfgUrlHttpMethodDelete_Type()
)
slbNewCfgUrlHttpMethodDelete.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgUrlHttpMethodDelete.setStatus("current")
_Layer7GeneralCfg_ObjectIdentity = ObjectIdentity
layer7GeneralCfg = _Layer7GeneralCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 2)
)


class _Layer7CurCfgDbindTimeout_Type(Integer32):
    """Custom type layer7CurCfgDbindTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 60),
    )


_Layer7CurCfgDbindTimeout_Type.__name__ = "Integer32"
_Layer7CurCfgDbindTimeout_Object = MibScalar
layer7CurCfgDbindTimeout = _Layer7CurCfgDbindTimeout_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 2, 1),
    _Layer7CurCfgDbindTimeout_Type()
)
layer7CurCfgDbindTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgDbindTimeout.setStatus("current")


class _Layer7NewCfgDbindTimeout_Type(Integer32):
    """Custom type layer7NewCfgDbindTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 60),
    )


_Layer7NewCfgDbindTimeout_Type.__name__ = "Integer32"
_Layer7NewCfgDbindTimeout_Object = MibScalar
layer7NewCfgDbindTimeout = _Layer7NewCfgDbindTimeout_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 2, 2),
    _Layer7NewCfgDbindTimeout_Type()
)
layer7NewCfgDbindTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    layer7NewCfgDbindTimeout.setStatus("current")
_SdpCfg_ObjectIdentity = ObjectIdentity
sdpCfg = _SdpCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 3)
)
_SlbSdpTableMaxSize_Type = Integer32
_SlbSdpTableMaxSize_Object = MibScalar
slbSdpTableMaxSize = _SlbSdpTableMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 3, 1),
    _SlbSdpTableMaxSize_Type()
)
slbSdpTableMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbSdpTableMaxSize.setStatus("current")
_SlbCurCfgSdpTable_Object = MibTable
slbCurCfgSdpTable = _SlbCurCfgSdpTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 3, 2)
)
if mibBuilder.loadTexts:
    slbCurCfgSdpTable.setStatus("current")
_SlbCurCfgSdpTableEntry_Object = MibTableRow
slbCurCfgSdpTableEntry = _SlbCurCfgSdpTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 3, 2, 1)
)
slbCurCfgSdpTableEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-LAYER7-MIB", "slbCurCfgSdpIndex"),
)
if mibBuilder.loadTexts:
    slbCurCfgSdpTableEntry.setStatus("current")
_SlbCurCfgSdpIndex_Type = Integer32
_SlbCurCfgSdpIndex_Object = MibTableColumn
slbCurCfgSdpIndex = _SlbCurCfgSdpIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 3, 2, 1, 1),
    _SlbCurCfgSdpIndex_Type()
)
slbCurCfgSdpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgSdpIndex.setStatus("current")
_SlbCurCfgSdpPrivAddr_Type = IpAddress
_SlbCurCfgSdpPrivAddr_Object = MibTableColumn
slbCurCfgSdpPrivAddr = _SlbCurCfgSdpPrivAddr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 3, 2, 1, 2),
    _SlbCurCfgSdpPrivAddr_Type()
)
slbCurCfgSdpPrivAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgSdpPrivAddr.setStatus("current")
_SlbCurCfgSdpPublicAddr_Type = IpAddress
_SlbCurCfgSdpPublicAddr_Object = MibTableColumn
slbCurCfgSdpPublicAddr = _SlbCurCfgSdpPublicAddr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 3, 2, 1, 3),
    _SlbCurCfgSdpPublicAddr_Type()
)
slbCurCfgSdpPublicAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgSdpPublicAddr.setStatus("current")
_SlbNewCfgSdpTable_Object = MibTable
slbNewCfgSdpTable = _SlbNewCfgSdpTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 3, 3)
)
if mibBuilder.loadTexts:
    slbNewCfgSdpTable.setStatus("current")
_SlbNewCfgSdpTableEntry_Object = MibTableRow
slbNewCfgSdpTableEntry = _SlbNewCfgSdpTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 3, 3, 1)
)
slbNewCfgSdpTableEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-LAYER7-MIB", "slbNewCfgSdpIndex"),
)
if mibBuilder.loadTexts:
    slbNewCfgSdpTableEntry.setStatus("current")
_SlbNewCfgSdpIndex_Type = Integer32
_SlbNewCfgSdpIndex_Object = MibTableColumn
slbNewCfgSdpIndex = _SlbNewCfgSdpIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 3, 3, 1, 1),
    _SlbNewCfgSdpIndex_Type()
)
slbNewCfgSdpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbNewCfgSdpIndex.setStatus("current")
_SlbNewCfgSdpPrivAddr_Type = IpAddress
_SlbNewCfgSdpPrivAddr_Object = MibTableColumn
slbNewCfgSdpPrivAddr = _SlbNewCfgSdpPrivAddr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 3, 3, 1, 2),
    _SlbNewCfgSdpPrivAddr_Type()
)
slbNewCfgSdpPrivAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgSdpPrivAddr.setStatus("current")
_SlbNewCfgSdpPublicAddr_Type = IpAddress
_SlbNewCfgSdpPublicAddr_Object = MibTableColumn
slbNewCfgSdpPublicAddr = _SlbNewCfgSdpPublicAddr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 3, 3, 1, 3),
    _SlbNewCfgSdpPublicAddr_Type()
)
slbNewCfgSdpPublicAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgSdpPublicAddr.setStatus("current")


class _SlbNewCfgSdpDelete_Type(Integer32):
    """Custom type slbNewCfgSdpDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delete", 2),
          ("other", 1))
    )


_SlbNewCfgSdpDelete_Type.__name__ = "Integer32"
_SlbNewCfgSdpDelete_Object = MibTableColumn
slbNewCfgSdpDelete = _SlbNewCfgSdpDelete_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 3, 3, 1, 4),
    _SlbNewCfgSdpDelete_Type()
)
slbNewCfgSdpDelete.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgSdpDelete.setStatus("current")
_HttpModCfg_ObjectIdentity = ObjectIdentity
httpModCfg = _HttpModCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4)
)
_Layer7CurCfgHttpmodListTable_Object = MibTable
layer7CurCfgHttpmodListTable = _Layer7CurCfgHttpmodListTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 1)
)
if mibBuilder.loadTexts:
    layer7CurCfgHttpmodListTable.setStatus("current")
_Layer7CurCfgHttpmodListEntry_Object = MibTableRow
layer7CurCfgHttpmodListEntry = _Layer7CurCfgHttpmodListEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 1, 1)
)
layer7CurCfgHttpmodListEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-LAYER7-MIB", "layer7CurCfgHttpmodListNameIdIndex"),
)
if mibBuilder.loadTexts:
    layer7CurCfgHttpmodListEntry.setStatus("current")


class _Layer7CurCfgHttpmodListNameIdIndex_Type(DisplayString):
    """Custom type layer7CurCfgHttpmodListNameIdIndex based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Layer7CurCfgHttpmodListNameIdIndex_Type.__name__ = "DisplayString"
_Layer7CurCfgHttpmodListNameIdIndex_Object = MibTableColumn
layer7CurCfgHttpmodListNameIdIndex = _Layer7CurCfgHttpmodListNameIdIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 1, 1, 1),
    _Layer7CurCfgHttpmodListNameIdIndex_Type()
)
layer7CurCfgHttpmodListNameIdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgHttpmodListNameIdIndex.setStatus("current")


class _Layer7CurCfgHttpmodListName_Type(DisplayString):
    """Custom type layer7CurCfgHttpmodListName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Layer7CurCfgHttpmodListName_Type.__name__ = "DisplayString"
_Layer7CurCfgHttpmodListName_Object = MibTableColumn
layer7CurCfgHttpmodListName = _Layer7CurCfgHttpmodListName_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 1, 1, 2),
    _Layer7CurCfgHttpmodListName_Type()
)
layer7CurCfgHttpmodListName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgHttpmodListName.setStatus("current")


class _Layer7CurCfgHttpmodListAdminStatus_Type(Integer32):
    """Custom type layer7CurCfgHttpmodListAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Layer7CurCfgHttpmodListAdminStatus_Type.__name__ = "Integer32"
_Layer7CurCfgHttpmodListAdminStatus_Object = MibTableColumn
layer7CurCfgHttpmodListAdminStatus = _Layer7CurCfgHttpmodListAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 1, 1, 3),
    _Layer7CurCfgHttpmodListAdminStatus_Type()
)
layer7CurCfgHttpmodListAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgHttpmodListAdminStatus.setStatus("current")
_Layer7NewCfgHttpmodListTable_Object = MibTable
layer7NewCfgHttpmodListTable = _Layer7NewCfgHttpmodListTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 2)
)
if mibBuilder.loadTexts:
    layer7NewCfgHttpmodListTable.setStatus("current")
_Layer7NewCfgHttpmodListEntry_Object = MibTableRow
layer7NewCfgHttpmodListEntry = _Layer7NewCfgHttpmodListEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 2, 1)
)
layer7NewCfgHttpmodListEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-LAYER7-MIB", "layer7NewCfgHttpmodListNameIdIndex"),
)
if mibBuilder.loadTexts:
    layer7NewCfgHttpmodListEntry.setStatus("current")


class _Layer7NewCfgHttpmodListNameIdIndex_Type(DisplayString):
    """Custom type layer7NewCfgHttpmodListNameIdIndex based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Layer7NewCfgHttpmodListNameIdIndex_Type.__name__ = "DisplayString"
_Layer7NewCfgHttpmodListNameIdIndex_Object = MibTableColumn
layer7NewCfgHttpmodListNameIdIndex = _Layer7NewCfgHttpmodListNameIdIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 2, 1, 1),
    _Layer7NewCfgHttpmodListNameIdIndex_Type()
)
layer7NewCfgHttpmodListNameIdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7NewCfgHttpmodListNameIdIndex.setStatus("current")


class _Layer7NewCfgHttpmodListName_Type(DisplayString):
    """Custom type layer7NewCfgHttpmodListName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Layer7NewCfgHttpmodListName_Type.__name__ = "DisplayString"
_Layer7NewCfgHttpmodListName_Object = MibTableColumn
layer7NewCfgHttpmodListName = _Layer7NewCfgHttpmodListName_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 2, 1, 2),
    _Layer7NewCfgHttpmodListName_Type()
)
layer7NewCfgHttpmodListName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    layer7NewCfgHttpmodListName.setStatus("current")


class _Layer7NewCfgHttpmodListAdminStatus_Type(Integer32):
    """Custom type layer7NewCfgHttpmodListAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Layer7NewCfgHttpmodListAdminStatus_Type.__name__ = "Integer32"
_Layer7NewCfgHttpmodListAdminStatus_Object = MibTableColumn
layer7NewCfgHttpmodListAdminStatus = _Layer7NewCfgHttpmodListAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 2, 1, 3),
    _Layer7NewCfgHttpmodListAdminStatus_Type()
)
layer7NewCfgHttpmodListAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    layer7NewCfgHttpmodListAdminStatus.setStatus("current")


class _Layer7NewCfgHttpmodListCopy_Type(DisplayString):
    """Custom type layer7NewCfgHttpmodListCopy based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Layer7NewCfgHttpmodListCopy_Type.__name__ = "DisplayString"
_Layer7NewCfgHttpmodListCopy_Object = MibTableColumn
layer7NewCfgHttpmodListCopy = _Layer7NewCfgHttpmodListCopy_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 2, 1, 4),
    _Layer7NewCfgHttpmodListCopy_Type()
)
layer7NewCfgHttpmodListCopy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    layer7NewCfgHttpmodListCopy.setStatus("current")


class _Layer7NewCfgHttpmodListDelete_Type(Integer32):
    """Custom type layer7NewCfgHttpmodListDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delete", 2),
          ("other", 1))
    )


_Layer7NewCfgHttpmodListDelete_Type.__name__ = "Integer32"
_Layer7NewCfgHttpmodListDelete_Object = MibTableColumn
layer7NewCfgHttpmodListDelete = _Layer7NewCfgHttpmodListDelete_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 2, 1, 5),
    _Layer7NewCfgHttpmodListDelete_Type()
)
layer7NewCfgHttpmodListDelete.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    layer7NewCfgHttpmodListDelete.setStatus("current")
_Layer7CurCfgHttpmodRuleTable_Object = MibTable
layer7CurCfgHttpmodRuleTable = _Layer7CurCfgHttpmodRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 3)
)
if mibBuilder.loadTexts:
    layer7CurCfgHttpmodRuleTable.setStatus("current")
_Layer7CurCfgHttpmodRuleEntry_Object = MibTableRow
layer7CurCfgHttpmodRuleEntry = _Layer7CurCfgHttpmodRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 3, 1)
)
layer7CurCfgHttpmodRuleEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-LAYER7-MIB", "layer7CurCfgHttpmodRuleListIdIndex"),
    (0, "ALTEON-CHEETAH-LAYER7-MIB", "layer7CurCfgHttpmodRuleIndex"),
)
if mibBuilder.loadTexts:
    layer7CurCfgHttpmodRuleEntry.setStatus("current")


class _Layer7CurCfgHttpmodRuleListIdIndex_Type(DisplayString):
    """Custom type layer7CurCfgHttpmodRuleListIdIndex based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Layer7CurCfgHttpmodRuleListIdIndex_Type.__name__ = "DisplayString"
_Layer7CurCfgHttpmodRuleListIdIndex_Object = MibTableColumn
layer7CurCfgHttpmodRuleListIdIndex = _Layer7CurCfgHttpmodRuleListIdIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 3, 1, 1),
    _Layer7CurCfgHttpmodRuleListIdIndex_Type()
)
layer7CurCfgHttpmodRuleListIdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgHttpmodRuleListIdIndex.setStatus("current")
_Layer7CurCfgHttpmodRuleIndex_Type = Integer32
_Layer7CurCfgHttpmodRuleIndex_Object = MibTableColumn
layer7CurCfgHttpmodRuleIndex = _Layer7CurCfgHttpmodRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 3, 1, 2),
    _Layer7CurCfgHttpmodRuleIndex_Type()
)
layer7CurCfgHttpmodRuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgHttpmodRuleIndex.setStatus("current")


class _Layer7CurCfgHttpmodRuleName_Type(DisplayString):
    """Custom type layer7CurCfgHttpmodRuleName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Layer7CurCfgHttpmodRuleName_Type.__name__ = "DisplayString"
_Layer7CurCfgHttpmodRuleName_Object = MibTableColumn
layer7CurCfgHttpmodRuleName = _Layer7CurCfgHttpmodRuleName_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 3, 1, 3),
    _Layer7CurCfgHttpmodRuleName_Type()
)
layer7CurCfgHttpmodRuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgHttpmodRuleName.setStatus("current")


class _Layer7CurCfgHttpmodRuleDirectn_Type(Integer32):
    """Custom type layer7CurCfgHttpmodRuleDirectn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bidirectional", 3),
          ("request", 1),
          ("response", 2))
    )


_Layer7CurCfgHttpmodRuleDirectn_Type.__name__ = "Integer32"
_Layer7CurCfgHttpmodRuleDirectn_Object = MibTableColumn
layer7CurCfgHttpmodRuleDirectn = _Layer7CurCfgHttpmodRuleDirectn_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 3, 1, 4),
    _Layer7CurCfgHttpmodRuleDirectn_Type()
)
layer7CurCfgHttpmodRuleDirectn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgHttpmodRuleDirectn.setStatus("current")


class _Layer7CurCfgHttpmodRuleAction_Type(Integer32):
    """Custom type layer7CurCfgHttpmodRuleAction based on Integer32"""
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
        *(("insert", 1),
          ("none", 4),
          ("remove", 3),
          ("replace", 2))
    )


_Layer7CurCfgHttpmodRuleAction_Type.__name__ = "Integer32"
_Layer7CurCfgHttpmodRuleAction_Object = MibTableColumn
layer7CurCfgHttpmodRuleAction = _Layer7CurCfgHttpmodRuleAction_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 3, 1, 5),
    _Layer7CurCfgHttpmodRuleAction_Type()
)
layer7CurCfgHttpmodRuleAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgHttpmodRuleAction.setStatus("current")


class _Layer7CurCfgHttpmodRuleAdminStatus_Type(Integer32):
    """Custom type layer7CurCfgHttpmodRuleAdminStatus based on Integer32"""
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


_Layer7CurCfgHttpmodRuleAdminStatus_Type.__name__ = "Integer32"
_Layer7CurCfgHttpmodRuleAdminStatus_Object = MibTableColumn
layer7CurCfgHttpmodRuleAdminStatus = _Layer7CurCfgHttpmodRuleAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 3, 1, 6),
    _Layer7CurCfgHttpmodRuleAdminStatus_Type()
)
layer7CurCfgHttpmodRuleAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgHttpmodRuleAdminStatus.setStatus("current")


class _Layer7CurCfgHttpmodRuleElement_Type(Integer32):
    """Custom type layer7CurCfgHttpmodRuleElement based on Integer32"""
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
        *(("cookie", 3),
          ("filetype", 4),
          ("header", 2),
          ("statusline", 5),
          ("text", 6),
          ("url", 1))
    )


_Layer7CurCfgHttpmodRuleElement_Type.__name__ = "Integer32"
_Layer7CurCfgHttpmodRuleElement_Object = MibTableColumn
layer7CurCfgHttpmodRuleElement = _Layer7CurCfgHttpmodRuleElement_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 3, 1, 7),
    _Layer7CurCfgHttpmodRuleElement_Type()
)
layer7CurCfgHttpmodRuleElement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgHttpmodRuleElement.setStatus("current")


class _Layer7CurCfgHttpmodRuleHttpBody_Type(Integer32):
    """Custom type layer7CurCfgHttpmodRuleHttpBody based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("exclude", 2),
          ("include", 1))
    )


_Layer7CurCfgHttpmodRuleHttpBody_Type.__name__ = "Integer32"
_Layer7CurCfgHttpmodRuleHttpBody_Object = MibTableColumn
layer7CurCfgHttpmodRuleHttpBody = _Layer7CurCfgHttpmodRuleHttpBody_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 3, 1, 8),
    _Layer7CurCfgHttpmodRuleHttpBody_Type()
)
layer7CurCfgHttpmodRuleHttpBody.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgHttpmodRuleHttpBody.setStatus("current")
_Layer7NewCfgHttpmodRuleTable_Object = MibTable
layer7NewCfgHttpmodRuleTable = _Layer7NewCfgHttpmodRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 4)
)
if mibBuilder.loadTexts:
    layer7NewCfgHttpmodRuleTable.setStatus("current")
_Layer7NewCfgHttpmodRuleEntry_Object = MibTableRow
layer7NewCfgHttpmodRuleEntry = _Layer7NewCfgHttpmodRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 4, 1)
)
layer7NewCfgHttpmodRuleEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-LAYER7-MIB", "layer7NewCfgHttpmodRuleListIdIndex"),
    (0, "ALTEON-CHEETAH-LAYER7-MIB", "layer7NewCfgHttpmodRuleIndex"),
)
if mibBuilder.loadTexts:
    layer7NewCfgHttpmodRuleEntry.setStatus("current")


class _Layer7NewCfgHttpmodRuleListIdIndex_Type(DisplayString):
    """Custom type layer7NewCfgHttpmodRuleListIdIndex based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Layer7NewCfgHttpmodRuleListIdIndex_Type.__name__ = "DisplayString"
_Layer7NewCfgHttpmodRuleListIdIndex_Object = MibTableColumn
layer7NewCfgHttpmodRuleListIdIndex = _Layer7NewCfgHttpmodRuleListIdIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 4, 1, 1),
    _Layer7NewCfgHttpmodRuleListIdIndex_Type()
)
layer7NewCfgHttpmodRuleListIdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7NewCfgHttpmodRuleListIdIndex.setStatus("current")
_Layer7NewCfgHttpmodRuleIndex_Type = Integer32
_Layer7NewCfgHttpmodRuleIndex_Object = MibTableColumn
layer7NewCfgHttpmodRuleIndex = _Layer7NewCfgHttpmodRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 4, 1, 2),
    _Layer7NewCfgHttpmodRuleIndex_Type()
)
layer7NewCfgHttpmodRuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7NewCfgHttpmodRuleIndex.setStatus("current")


class _Layer7NewCfgHttpmodRuleName_Type(DisplayString):
    """Custom type layer7NewCfgHttpmodRuleName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Layer7NewCfgHttpmodRuleName_Type.__name__ = "DisplayString"
_Layer7NewCfgHttpmodRuleName_Object = MibTableColumn
layer7NewCfgHttpmodRuleName = _Layer7NewCfgHttpmodRuleName_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 4, 1, 3),
    _Layer7NewCfgHttpmodRuleName_Type()
)
layer7NewCfgHttpmodRuleName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    layer7NewCfgHttpmodRuleName.setStatus("current")


class _Layer7NewCfgHttpmodRuleDirectn_Type(Integer32):
    """Custom type layer7NewCfgHttpmodRuleDirectn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bidirectional", 3),
          ("request", 1),
          ("response", 2))
    )


_Layer7NewCfgHttpmodRuleDirectn_Type.__name__ = "Integer32"
_Layer7NewCfgHttpmodRuleDirectn_Object = MibTableColumn
layer7NewCfgHttpmodRuleDirectn = _Layer7NewCfgHttpmodRuleDirectn_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 4, 1, 4),
    _Layer7NewCfgHttpmodRuleDirectn_Type()
)
layer7NewCfgHttpmodRuleDirectn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    layer7NewCfgHttpmodRuleDirectn.setStatus("current")


class _Layer7NewCfgHttpmodRuleAction_Type(Integer32):
    """Custom type layer7NewCfgHttpmodRuleAction based on Integer32"""
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
        *(("insert", 1),
          ("none", 4),
          ("remove", 3),
          ("replace", 2))
    )


_Layer7NewCfgHttpmodRuleAction_Type.__name__ = "Integer32"
_Layer7NewCfgHttpmodRuleAction_Object = MibTableColumn
layer7NewCfgHttpmodRuleAction = _Layer7NewCfgHttpmodRuleAction_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 4, 1, 5),
    _Layer7NewCfgHttpmodRuleAction_Type()
)
layer7NewCfgHttpmodRuleAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    layer7NewCfgHttpmodRuleAction.setStatus("current")


class _Layer7NewCfgHttpmodRuleAdminStatus_Type(Integer32):
    """Custom type layer7NewCfgHttpmodRuleAdminStatus based on Integer32"""
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


_Layer7NewCfgHttpmodRuleAdminStatus_Type.__name__ = "Integer32"
_Layer7NewCfgHttpmodRuleAdminStatus_Object = MibTableColumn
layer7NewCfgHttpmodRuleAdminStatus = _Layer7NewCfgHttpmodRuleAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 4, 1, 6),
    _Layer7NewCfgHttpmodRuleAdminStatus_Type()
)
layer7NewCfgHttpmodRuleAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    layer7NewCfgHttpmodRuleAdminStatus.setStatus("current")
_Layer7NewCfgHttpmodRuleCopy_Type = DisplayString
_Layer7NewCfgHttpmodRuleCopy_Object = MibTableColumn
layer7NewCfgHttpmodRuleCopy = _Layer7NewCfgHttpmodRuleCopy_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 4, 1, 7),
    _Layer7NewCfgHttpmodRuleCopy_Type()
)
layer7NewCfgHttpmodRuleCopy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    layer7NewCfgHttpmodRuleCopy.setStatus("current")


class _Layer7NewCfgHttpmodRuleDelete_Type(Integer32):
    """Custom type layer7NewCfgHttpmodRuleDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delete", 2),
          ("other", 1))
    )


_Layer7NewCfgHttpmodRuleDelete_Type.__name__ = "Integer32"
_Layer7NewCfgHttpmodRuleDelete_Object = MibTableColumn
layer7NewCfgHttpmodRuleDelete = _Layer7NewCfgHttpmodRuleDelete_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 4, 1, 8),
    _Layer7NewCfgHttpmodRuleDelete_Type()
)
layer7NewCfgHttpmodRuleDelete.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    layer7NewCfgHttpmodRuleDelete.setStatus("current")


class _Layer7NewCfgHttpmodRuleElement_Type(Integer32):
    """Custom type layer7NewCfgHttpmodRuleElement based on Integer32"""
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
        *(("cookie", 3),
          ("filetype", 4),
          ("header", 2),
          ("statusline", 5),
          ("text", 6),
          ("url", 1))
    )


_Layer7NewCfgHttpmodRuleElement_Type.__name__ = "Integer32"
_Layer7NewCfgHttpmodRuleElement_Object = MibTableColumn
layer7NewCfgHttpmodRuleElement = _Layer7NewCfgHttpmodRuleElement_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 4, 1, 9),
    _Layer7NewCfgHttpmodRuleElement_Type()
)
layer7NewCfgHttpmodRuleElement.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    layer7NewCfgHttpmodRuleElement.setStatus("current")


class _Layer7NewCfgHttpmodRuleHttpBody_Type(Integer32):
    """Custom type layer7NewCfgHttpmodRuleHttpBody based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("exclude", 2),
          ("include", 1))
    )


_Layer7NewCfgHttpmodRuleHttpBody_Type.__name__ = "Integer32"
_Layer7NewCfgHttpmodRuleHttpBody_Object = MibTableColumn
layer7NewCfgHttpmodRuleHttpBody = _Layer7NewCfgHttpmodRuleHttpBody_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 4, 1, 10),
    _Layer7NewCfgHttpmodRuleHttpBody_Type()
)
layer7NewCfgHttpmodRuleHttpBody.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    layer7NewCfgHttpmodRuleHttpBody.setStatus("current")
_Layer7CurCfgHttpmodRuleUrlTable_Object = MibTable
layer7CurCfgHttpmodRuleUrlTable = _Layer7CurCfgHttpmodRuleUrlTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 5)
)
if mibBuilder.loadTexts:
    layer7CurCfgHttpmodRuleUrlTable.setStatus("current")
_Layer7CurCfgHttpmodRuleUrlEntry_Object = MibTableRow
layer7CurCfgHttpmodRuleUrlEntry = _Layer7CurCfgHttpmodRuleUrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 5, 1)
)
layer7CurCfgHttpmodRuleUrlEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-LAYER7-MIB", "layer7CurCfgHttpmodRuleUrlListIdIndex"),
    (0, "ALTEON-CHEETAH-LAYER7-MIB", "layer7CurCfgHttpmodRuleUrlIndex"),
)
if mibBuilder.loadTexts:
    layer7CurCfgHttpmodRuleUrlEntry.setStatus("current")


class _Layer7CurCfgHttpmodRuleUrlListIdIndex_Type(DisplayString):
    """Custom type layer7CurCfgHttpmodRuleUrlListIdIndex based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Layer7CurCfgHttpmodRuleUrlListIdIndex_Type.__name__ = "DisplayString"
_Layer7CurCfgHttpmodRuleUrlListIdIndex_Object = MibTableColumn
layer7CurCfgHttpmodRuleUrlListIdIndex = _Layer7CurCfgHttpmodRuleUrlListIdIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 5, 1, 1),
    _Layer7CurCfgHttpmodRuleUrlListIdIndex_Type()
)
layer7CurCfgHttpmodRuleUrlListIdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgHttpmodRuleUrlListIdIndex.setStatus("current")
_Layer7CurCfgHttpmodRuleUrlIndex_Type = Integer32
_Layer7CurCfgHttpmodRuleUrlIndex_Object = MibTableColumn
layer7CurCfgHttpmodRuleUrlIndex = _Layer7CurCfgHttpmodRuleUrlIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 5, 1, 2),
    _Layer7CurCfgHttpmodRuleUrlIndex_Type()
)
layer7CurCfgHttpmodRuleUrlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgHttpmodRuleUrlIndex.setStatus("current")


class _Layer7CurCfgHttpmodRuleUrlMtchProtcol_Type(Integer32):
    """Custom type layer7CurCfgHttpmodRuleUrlMtchProtcol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("http", 1),
          ("https", 2))
    )


_Layer7CurCfgHttpmodRuleUrlMtchProtcol_Type.__name__ = "Integer32"
_Layer7CurCfgHttpmodRuleUrlMtchProtcol_Object = MibTableColumn
layer7CurCfgHttpmodRuleUrlMtchProtcol = _Layer7CurCfgHttpmodRuleUrlMtchProtcol_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 5, 1, 3),
    _Layer7CurCfgHttpmodRuleUrlMtchProtcol_Type()
)
layer7CurCfgHttpmodRuleUrlMtchProtcol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgHttpmodRuleUrlMtchProtcol.setStatus("current")
_Layer7CurCfgHttpmodRuleUrlMtchPort_Type = Integer32
_Layer7CurCfgHttpmodRuleUrlMtchPort_Object = MibTableColumn
layer7CurCfgHttpmodRuleUrlMtchPort = _Layer7CurCfgHttpmodRuleUrlMtchPort_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 5, 1, 4),
    _Layer7CurCfgHttpmodRuleUrlMtchPort_Type()
)
layer7CurCfgHttpmodRuleUrlMtchPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgHttpmodRuleUrlMtchPort.setStatus("current")


class _Layer7CurCfgHttpmodRuleUrlMtchHostTyp_Type(Integer32):
    """Custom type layer7CurCfgHttpmodRuleUrlMtchHostTyp based on Integer32"""
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
        *(("any", 5),
          ("equal", 3),
          ("include", 4),
          ("prefix", 2),
          ("suffix", 1))
    )


_Layer7CurCfgHttpmodRuleUrlMtchHostTyp_Type.__name__ = "Integer32"
_Layer7CurCfgHttpmodRuleUrlMtchHostTyp_Object = MibTableColumn
layer7CurCfgHttpmodRuleUrlMtchHostTyp = _Layer7CurCfgHttpmodRuleUrlMtchHostTyp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 5, 1, 5),
    _Layer7CurCfgHttpmodRuleUrlMtchHostTyp_Type()
)
layer7CurCfgHttpmodRuleUrlMtchHostTyp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgHttpmodRuleUrlMtchHostTyp.setStatus("current")


class _Layer7CurCfgHttpmodRuleUrlMtchHost_Type(DisplayString):
    """Custom type layer7CurCfgHttpmodRuleUrlMtchHost based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Layer7CurCfgHttpmodRuleUrlMtchHost_Type.__name__ = "DisplayString"
_Layer7CurCfgHttpmodRuleUrlMtchHost_Object = MibTableColumn
layer7CurCfgHttpmodRuleUrlMtchHost = _Layer7CurCfgHttpmodRuleUrlMtchHost_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 5, 1, 6),
    _Layer7CurCfgHttpmodRuleUrlMtchHost_Type()
)
layer7CurCfgHttpmodRuleUrlMtchHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgHttpmodRuleUrlMtchHost.setStatus("current")


class _Layer7CurCfgHttpmodRuleUrlMtchPathTyp_Type(Integer32):
    """Custom type layer7CurCfgHttpmodRuleUrlMtchPathTyp based on Integer32"""
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
        *(("any", 5),
          ("equal", 3),
          ("include", 4),
          ("prefix", 2),
          ("suffix", 1))
    )


_Layer7CurCfgHttpmodRuleUrlMtchPathTyp_Type.__name__ = "Integer32"
_Layer7CurCfgHttpmodRuleUrlMtchPathTyp_Object = MibTableColumn
layer7CurCfgHttpmodRuleUrlMtchPathTyp = _Layer7CurCfgHttpmodRuleUrlMtchPathTyp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 5, 1, 7),
    _Layer7CurCfgHttpmodRuleUrlMtchPathTyp_Type()
)
layer7CurCfgHttpmodRuleUrlMtchPathTyp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgHttpmodRuleUrlMtchPathTyp.setStatus("current")


class _Layer7CurCfgHttpmodRuleUrlMtchPath_Type(DisplayString):
    """Custom type layer7CurCfgHttpmodRuleUrlMtchPath based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Layer7CurCfgHttpmodRuleUrlMtchPath_Type.__name__ = "DisplayString"
_Layer7CurCfgHttpmodRuleUrlMtchPath_Object = MibTableColumn
layer7CurCfgHttpmodRuleUrlMtchPath = _Layer7CurCfgHttpmodRuleUrlMtchPath_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 5, 1, 8),
    _Layer7CurCfgHttpmodRuleUrlMtchPath_Type()
)
layer7CurCfgHttpmodRuleUrlMtchPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgHttpmodRuleUrlMtchPath.setStatus("current")


class _Layer7CurCfgHttpmodRuleUrlMtchPgName_Type(DisplayString):
    """Custom type layer7CurCfgHttpmodRuleUrlMtchPgName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Layer7CurCfgHttpmodRuleUrlMtchPgName_Type.__name__ = "DisplayString"
_Layer7CurCfgHttpmodRuleUrlMtchPgName_Object = MibTableColumn
layer7CurCfgHttpmodRuleUrlMtchPgName = _Layer7CurCfgHttpmodRuleUrlMtchPgName_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 5, 1, 9),
    _Layer7CurCfgHttpmodRuleUrlMtchPgName_Type()
)
layer7CurCfgHttpmodRuleUrlMtchPgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgHttpmodRuleUrlMtchPgName.setStatus("current")


class _Layer7CurCfgHttpmodRuleUrlMtchPgTyp_Type(DisplayString):
    """Custom type layer7CurCfgHttpmodRuleUrlMtchPgTyp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Layer7CurCfgHttpmodRuleUrlMtchPgTyp_Type.__name__ = "DisplayString"
_Layer7CurCfgHttpmodRuleUrlMtchPgTyp_Object = MibTableColumn
layer7CurCfgHttpmodRuleUrlMtchPgTyp = _Layer7CurCfgHttpmodRuleUrlMtchPgTyp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 5, 1, 10),
    _Layer7CurCfgHttpmodRuleUrlMtchPgTyp_Type()
)
layer7CurCfgHttpmodRuleUrlMtchPgTyp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgHttpmodRuleUrlMtchPgTyp.setStatus("current")


class _Layer7CurCfgHttpmodRuleUrlActnProtcl_Type(Integer32):
    """Custom type layer7CurCfgHttpmodRuleUrlActnProtcl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("http", 1),
          ("https", 2))
    )


_Layer7CurCfgHttpmodRuleUrlActnProtcl_Type.__name__ = "Integer32"
_Layer7CurCfgHttpmodRuleUrlActnProtcl_Object = MibTableColumn
layer7CurCfgHttpmodRuleUrlActnProtcl = _Layer7CurCfgHttpmodRuleUrlActnProtcl_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 5, 1, 11),
    _Layer7CurCfgHttpmodRuleUrlActnProtcl_Type()
)
layer7CurCfgHttpmodRuleUrlActnProtcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgHttpmodRuleUrlActnProtcl.setStatus("current")
_Layer7CurCfgHttpmodRuleUrlActnPort_Type = Integer32
_Layer7CurCfgHttpmodRuleUrlActnPort_Object = MibTableColumn
layer7CurCfgHttpmodRuleUrlActnPort = _Layer7CurCfgHttpmodRuleUrlActnPort_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 5, 1, 12),
    _Layer7CurCfgHttpmodRuleUrlActnPort_Type()
)
layer7CurCfgHttpmodRuleUrlActnPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgHttpmodRuleUrlActnPort.setStatus("current")


class _Layer7CurCfgHttpmodRuleUrlActnHostTyp_Type(Integer32):
    """Custom type layer7CurCfgHttpmodRuleUrlActnHostTyp based on Integer32"""
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
        *(("insert", 1),
          ("none", 4),
          ("remove", 3),
          ("replace", 2))
    )


_Layer7CurCfgHttpmodRuleUrlActnHostTyp_Type.__name__ = "Integer32"
_Layer7CurCfgHttpmodRuleUrlActnHostTyp_Object = MibTableColumn
layer7CurCfgHttpmodRuleUrlActnHostTyp = _Layer7CurCfgHttpmodRuleUrlActnHostTyp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 5, 1, 13),
    _Layer7CurCfgHttpmodRuleUrlActnHostTyp_Type()
)
layer7CurCfgHttpmodRuleUrlActnHostTyp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgHttpmodRuleUrlActnHostTyp.setStatus("current")


class _Layer7CurCfgHttpmodRuleUrlActnHost_Type(DisplayString):
    """Custom type layer7CurCfgHttpmodRuleUrlActnHost based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Layer7CurCfgHttpmodRuleUrlActnHost_Type.__name__ = "DisplayString"
_Layer7CurCfgHttpmodRuleUrlActnHost_Object = MibTableColumn
layer7CurCfgHttpmodRuleUrlActnHost = _Layer7CurCfgHttpmodRuleUrlActnHost_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 5, 1, 14),
    _Layer7CurCfgHttpmodRuleUrlActnHost_Type()
)
layer7CurCfgHttpmodRuleUrlActnHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgHttpmodRuleUrlActnHost.setStatus("current")


class _Layer7CurCfgHttpmodRuleUrlActnHstSec_Type(Integer32):
    """Custom type layer7CurCfgHttpmodRuleUrlActnHstSec based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("after", 2),
          ("before", 1))
    )


_Layer7CurCfgHttpmodRuleUrlActnHstSec_Type.__name__ = "Integer32"
_Layer7CurCfgHttpmodRuleUrlActnHstSec_Object = MibTableColumn
layer7CurCfgHttpmodRuleUrlActnHstSec = _Layer7CurCfgHttpmodRuleUrlActnHstSec_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 5, 1, 15),
    _Layer7CurCfgHttpmodRuleUrlActnHstSec_Type()
)
layer7CurCfgHttpmodRuleUrlActnHstSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgHttpmodRuleUrlActnHstSec.setStatus("current")


class _Layer7CurCfgHttpmodRuleUrlActnHstRplc_Type(DisplayString):
    """Custom type layer7CurCfgHttpmodRuleUrlActnHstRplc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Layer7CurCfgHttpmodRuleUrlActnHstRplc_Type.__name__ = "DisplayString"
_Layer7CurCfgHttpmodRuleUrlActnHstRplc_Object = MibTableColumn
layer7CurCfgHttpmodRuleUrlActnHstRplc = _Layer7CurCfgHttpmodRuleUrlActnHstRplc_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 5, 1, 16),
    _Layer7CurCfgHttpmodRuleUrlActnHstRplc_Type()
)
layer7CurCfgHttpmodRuleUrlActnHstRplc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgHttpmodRuleUrlActnHstRplc.setStatus("current")


class _Layer7CurCfgHttpmodRuleUrlActnPathTyp_Type(Integer32):
    """Custom type layer7CurCfgHttpmodRuleUrlActnPathTyp based on Integer32"""
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
        *(("insert", 1),
          ("none", 4),
          ("remove", 3),
          ("replace", 2))
    )


_Layer7CurCfgHttpmodRuleUrlActnPathTyp_Type.__name__ = "Integer32"
_Layer7CurCfgHttpmodRuleUrlActnPathTyp_Object = MibTableColumn
layer7CurCfgHttpmodRuleUrlActnPathTyp = _Layer7CurCfgHttpmodRuleUrlActnPathTyp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 5, 1, 17),
    _Layer7CurCfgHttpmodRuleUrlActnPathTyp_Type()
)
layer7CurCfgHttpmodRuleUrlActnPathTyp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgHttpmodRuleUrlActnPathTyp.setStatus("current")


class _Layer7CurCfgHttpmodRuleUrlActnPath_Type(DisplayString):
    """Custom type layer7CurCfgHttpmodRuleUrlActnPath based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Layer7CurCfgHttpmodRuleUrlActnPath_Type.__name__ = "DisplayString"
_Layer7CurCfgHttpmodRuleUrlActnPath_Object = MibTableColumn
layer7CurCfgHttpmodRuleUrlActnPath = _Layer7CurCfgHttpmodRuleUrlActnPath_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 5, 1, 18),
    _Layer7CurCfgHttpmodRuleUrlActnPath_Type()
)
layer7CurCfgHttpmodRuleUrlActnPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgHttpmodRuleUrlActnPath.setStatus("current")


class _Layer7CurCfgHttpmodRuleUrlActnPthSctn_Type(Integer32):
    """Custom type layer7CurCfgHttpmodRuleUrlActnPthSctn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("after", 2),
          ("before", 1))
    )


_Layer7CurCfgHttpmodRuleUrlActnPthSctn_Type.__name__ = "Integer32"
_Layer7CurCfgHttpmodRuleUrlActnPthSctn_Object = MibTableColumn
layer7CurCfgHttpmodRuleUrlActnPthSctn = _Layer7CurCfgHttpmodRuleUrlActnPthSctn_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 5, 1, 19),
    _Layer7CurCfgHttpmodRuleUrlActnPthSctn_Type()
)
layer7CurCfgHttpmodRuleUrlActnPthSctn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgHttpmodRuleUrlActnPthSctn.setStatus("current")


class _Layer7CurCfgHttpmodRuleUrlActnPthRplc_Type(DisplayString):
    """Custom type layer7CurCfgHttpmodRuleUrlActnPthRplc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Layer7CurCfgHttpmodRuleUrlActnPthRplc_Type.__name__ = "DisplayString"
_Layer7CurCfgHttpmodRuleUrlActnPthRplc_Object = MibTableColumn
layer7CurCfgHttpmodRuleUrlActnPthRplc = _Layer7CurCfgHttpmodRuleUrlActnPthRplc_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 5, 1, 20),
    _Layer7CurCfgHttpmodRuleUrlActnPthRplc_Type()
)
layer7CurCfgHttpmodRuleUrlActnPthRplc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgHttpmodRuleUrlActnPthRplc.setStatus("current")


class _Layer7CurCfgHttpmodRuleUrlActnPgName_Type(DisplayString):
    """Custom type layer7CurCfgHttpmodRuleUrlActnPgName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Layer7CurCfgHttpmodRuleUrlActnPgName_Type.__name__ = "DisplayString"
_Layer7CurCfgHttpmodRuleUrlActnPgName_Object = MibTableColumn
layer7CurCfgHttpmodRuleUrlActnPgName = _Layer7CurCfgHttpmodRuleUrlActnPgName_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 5, 1, 21),
    _Layer7CurCfgHttpmodRuleUrlActnPgName_Type()
)
layer7CurCfgHttpmodRuleUrlActnPgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgHttpmodRuleUrlActnPgName.setStatus("current")


class _Layer7CurCfgHttpmodRuleUrlActnPgTyp_Type(DisplayString):
    """Custom type layer7CurCfgHttpmodRuleUrlActnPgTyp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Layer7CurCfgHttpmodRuleUrlActnPgTyp_Type.__name__ = "DisplayString"
_Layer7CurCfgHttpmodRuleUrlActnPgTyp_Object = MibTableColumn
layer7CurCfgHttpmodRuleUrlActnPgTyp = _Layer7CurCfgHttpmodRuleUrlActnPgTyp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 5, 1, 22),
    _Layer7CurCfgHttpmodRuleUrlActnPgTyp_Type()
)
layer7CurCfgHttpmodRuleUrlActnPgTyp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgHttpmodRuleUrlActnPgTyp.setStatus("current")
_Layer7NewCfgHttpmodRuleUrlTable_Object = MibTable
layer7NewCfgHttpmodRuleUrlTable = _Layer7NewCfgHttpmodRuleUrlTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 6)
)
if mibBuilder.loadTexts:
    layer7NewCfgHttpmodRuleUrlTable.setStatus("current")
_Layer7NewCfgHttpmodRuleUrlEntry_Object = MibTableRow
layer7NewCfgHttpmodRuleUrlEntry = _Layer7NewCfgHttpmodRuleUrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 6, 1)
)
layer7NewCfgHttpmodRuleUrlEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-LAYER7-MIB", "layer7NewCfgHttpmodRuleUrlListIdIndex"),
    (0, "ALTEON-CHEETAH-LAYER7-MIB", "layer7NewCfgHttpmodRuleUrlIndex"),
)
if mibBuilder.loadTexts:
    layer7NewCfgHttpmodRuleUrlEntry.setStatus("current")


class _Layer7NewCfgHttpmodRuleUrlListIdIndex_Type(DisplayString):
    """Custom type layer7NewCfgHttpmodRuleUrlListIdIndex based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Layer7NewCfgHttpmodRuleUrlListIdIndex_Type.__name__ = "DisplayString"
_Layer7NewCfgHttpmodRuleUrlListIdIndex_Object = MibTableColumn
layer7NewCfgHttpmodRuleUrlListIdIndex = _Layer7NewCfgHttpmodRuleUrlListIdIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 6, 1, 1),
    _Layer7NewCfgHttpmodRuleUrlListIdIndex_Type()
)
layer7NewCfgHttpmodRuleUrlListIdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7NewCfgHttpmodRuleUrlListIdIndex.setStatus("current")
_Layer7NewCfgHttpmodRuleUrlIndex_Type = Integer32
_Layer7NewCfgHttpmodRuleUrlIndex_Object = MibTableColumn
layer7NewCfgHttpmodRuleUrlIndex = _Layer7NewCfgHttpmodRuleUrlIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 6, 1, 2),
    _Layer7NewCfgHttpmodRuleUrlIndex_Type()
)
layer7NewCfgHttpmodRuleUrlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7NewCfgHttpmodRuleUrlIndex.setStatus("current")


class _Layer7NewCfgHttpmodRuleUrlMtchProtcol_Type(Integer32):
    """Custom type layer7NewCfgHttpmodRuleUrlMtchProtcol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("http", 1),
          ("https", 2))
    )


_Layer7NewCfgHttpmodRuleUrlMtchProtcol_Type.__name__ = "Integer32"
_Layer7NewCfgHttpmodRuleUrlMtchProtcol_Object = MibTableColumn
layer7NewCfgHttpmodRuleUrlMtchProtcol = _Layer7NewCfgHttpmodRuleUrlMtchProtcol_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 6, 1, 3),
    _Layer7NewCfgHttpmodRuleUrlMtchProtcol_Type()
)
layer7NewCfgHttpmodRuleUrlMtchProtcol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    layer7NewCfgHttpmodRuleUrlMtchProtcol.setStatus("current")
_Layer7NewCfgHttpmodRuleUrlMtchPort_Type = Integer32
_Layer7NewCfgHttpmodRuleUrlMtchPort_Object = MibTableColumn
layer7NewCfgHttpmodRuleUrlMtchPort = _Layer7NewCfgHttpmodRuleUrlMtchPort_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 6, 1, 4),
    _Layer7NewCfgHttpmodRuleUrlMtchPort_Type()
)
layer7NewCfgHttpmodRuleUrlMtchPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    layer7NewCfgHttpmodRuleUrlMtchPort.setStatus("current")


class _Layer7NewCfgHttpmodRuleUrlMtchHostTyp_Type(Integer32):
    """Custom type layer7NewCfgHttpmodRuleUrlMtchHostTyp based on Integer32"""
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
        *(("any", 5),
          ("equal", 3),
          ("include", 4),
          ("prefix", 2),
          ("suffix", 1))
    )


_Layer7NewCfgHttpmodRuleUrlMtchHostTyp_Type.__name__ = "Integer32"
_Layer7NewCfgHttpmodRuleUrlMtchHostTyp_Object = MibTableColumn
layer7NewCfgHttpmodRuleUrlMtchHostTyp = _Layer7NewCfgHttpmodRuleUrlMtchHostTyp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 6, 1, 5),
    _Layer7NewCfgHttpmodRuleUrlMtchHostTyp_Type()
)
layer7NewCfgHttpmodRuleUrlMtchHostTyp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    layer7NewCfgHttpmodRuleUrlMtchHostTyp.setStatus("current")


class _Layer7NewCfgHttpmodRuleUrlMtchHost_Type(DisplayString):
    """Custom type layer7NewCfgHttpmodRuleUrlMtchHost based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Layer7NewCfgHttpmodRuleUrlMtchHost_Type.__name__ = "DisplayString"
_Layer7NewCfgHttpmodRuleUrlMtchHost_Object = MibTableColumn
layer7NewCfgHttpmodRuleUrlMtchHost = _Layer7NewCfgHttpmodRuleUrlMtchHost_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 6, 1, 6),
    _Layer7NewCfgHttpmodRuleUrlMtchHost_Type()
)
layer7NewCfgHttpmodRuleUrlMtchHost.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    layer7NewCfgHttpmodRuleUrlMtchHost.setStatus("current")


class _Layer7NewCfgHttpmodRuleUrlMtchPathTyp_Type(Integer32):
    """Custom type layer7NewCfgHttpmodRuleUrlMtchPathTyp based on Integer32"""
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
        *(("any", 5),
          ("equal", 3),
          ("include", 4),
          ("prefix", 2),
          ("suffix", 1))
    )


_Layer7NewCfgHttpmodRuleUrlMtchPathTyp_Type.__name__ = "Integer32"
_Layer7NewCfgHttpmodRuleUrlMtchPathTyp_Object = MibTableColumn
layer7NewCfgHttpmodRuleUrlMtchPathTyp = _Layer7NewCfgHttpmodRuleUrlMtchPathTyp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 6, 1, 7),
    _Layer7NewCfgHttpmodRuleUrlMtchPathTyp_Type()
)
layer7NewCfgHttpmodRuleUrlMtchPathTyp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    layer7NewCfgHttpmodRuleUrlMtchPathTyp.setStatus("current")


class _Layer7NewCfgHttpmodRuleUrlMtchPath_Type(DisplayString):
    """Custom type layer7NewCfgHttpmodRuleUrlMtchPath based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Layer7NewCfgHttpmodRuleUrlMtchPath_Type.__name__ = "DisplayString"
_Layer7NewCfgHttpmodRuleUrlMtchPath_Object = MibTableColumn
layer7NewCfgHttpmodRuleUrlMtchPath = _Layer7NewCfgHttpmodRuleUrlMtchPath_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 6, 1, 8),
    _Layer7NewCfgHttpmodRuleUrlMtchPath_Type()
)
layer7NewCfgHttpmodRuleUrlMtchPath.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    layer7NewCfgHttpmodRuleUrlMtchPath.setStatus("current")


class _Layer7NewCfgHttpmodRuleUrlMtchPgName_Type(DisplayString):
    """Custom type layer7NewCfgHttpmodRuleUrlMtchPgName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Layer7NewCfgHttpmodRuleUrlMtchPgName_Type.__name__ = "DisplayString"
_Layer7NewCfgHttpmodRuleUrlMtchPgName_Object = MibTableColumn
layer7NewCfgHttpmodRuleUrlMtchPgName = _Layer7NewCfgHttpmodRuleUrlMtchPgName_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 6, 1, 9),
    _Layer7NewCfgHttpmodRuleUrlMtchPgName_Type()
)
layer7NewCfgHttpmodRuleUrlMtchPgName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    layer7NewCfgHttpmodRuleUrlMtchPgName.setStatus("current")


class _Layer7NewCfgHttpmodRuleUrlMtchPgTyp_Type(DisplayString):
    """Custom type layer7NewCfgHttpmodRuleUrlMtchPgTyp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Layer7NewCfgHttpmodRuleUrlMtchPgTyp_Type.__name__ = "DisplayString"
_Layer7NewCfgHttpmodRuleUrlMtchPgTyp_Object = MibTableColumn
layer7NewCfgHttpmodRuleUrlMtchPgTyp = _Layer7NewCfgHttpmodRuleUrlMtchPgTyp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 6, 1, 10),
    _Layer7NewCfgHttpmodRuleUrlMtchPgTyp_Type()
)
layer7NewCfgHttpmodRuleUrlMtchPgTyp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    layer7NewCfgHttpmodRuleUrlMtchPgTyp.setStatus("current")


class _Layer7NewCfgHttpmodRuleUrlActnProtcl_Type(Integer32):
    """Custom type layer7NewCfgHttpmodRuleUrlActnProtcl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("http", 1),
          ("https", 2))
    )


_Layer7NewCfgHttpmodRuleUrlActnProtcl_Type.__name__ = "Integer32"
_Layer7NewCfgHttpmodRuleUrlActnProtcl_Object = MibTableColumn
layer7NewCfgHttpmodRuleUrlActnProtcl = _Layer7NewCfgHttpmodRuleUrlActnProtcl_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 6, 1, 11),
    _Layer7NewCfgHttpmodRuleUrlActnProtcl_Type()
)
layer7NewCfgHttpmodRuleUrlActnProtcl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    layer7NewCfgHttpmodRuleUrlActnProtcl.setStatus("current")
_Layer7NewCfgHttpmodRuleUrlActnPort_Type = Integer32
_Layer7NewCfgHttpmodRuleUrlActnPort_Object = MibTableColumn
layer7NewCfgHttpmodRuleUrlActnPort = _Layer7NewCfgHttpmodRuleUrlActnPort_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 6, 1, 12),
    _Layer7NewCfgHttpmodRuleUrlActnPort_Type()
)
layer7NewCfgHttpmodRuleUrlActnPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    layer7NewCfgHttpmodRuleUrlActnPort.setStatus("current")


class _Layer7NewCfgHttpmodRuleUrlActnHostTyp_Type(Integer32):
    """Custom type layer7NewCfgHttpmodRuleUrlActnHostTyp based on Integer32"""
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
        *(("insert", 1),
          ("none", 4),
          ("remove", 3),
          ("replace", 2))
    )


_Layer7NewCfgHttpmodRuleUrlActnHostTyp_Type.__name__ = "Integer32"
_Layer7NewCfgHttpmodRuleUrlActnHostTyp_Object = MibTableColumn
layer7NewCfgHttpmodRuleUrlActnHostTyp = _Layer7NewCfgHttpmodRuleUrlActnHostTyp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 6, 1, 13),
    _Layer7NewCfgHttpmodRuleUrlActnHostTyp_Type()
)
layer7NewCfgHttpmodRuleUrlActnHostTyp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    layer7NewCfgHttpmodRuleUrlActnHostTyp.setStatus("current")


class _Layer7NewCfgHttpmodRuleUrlActnHost_Type(DisplayString):
    """Custom type layer7NewCfgHttpmodRuleUrlActnHost based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Layer7NewCfgHttpmodRuleUrlActnHost_Type.__name__ = "DisplayString"
_Layer7NewCfgHttpmodRuleUrlActnHost_Object = MibTableColumn
layer7NewCfgHttpmodRuleUrlActnHost = _Layer7NewCfgHttpmodRuleUrlActnHost_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 6, 1, 14),
    _Layer7NewCfgHttpmodRuleUrlActnHost_Type()
)
layer7NewCfgHttpmodRuleUrlActnHost.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    layer7NewCfgHttpmodRuleUrlActnHost.setStatus("current")


class _Layer7NewCfgHttpmodRuleUrlActnHstSec_Type(Integer32):
    """Custom type layer7NewCfgHttpmodRuleUrlActnHstSec based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("after", 2),
          ("before", 1))
    )


_Layer7NewCfgHttpmodRuleUrlActnHstSec_Type.__name__ = "Integer32"
_Layer7NewCfgHttpmodRuleUrlActnHstSec_Object = MibTableColumn
layer7NewCfgHttpmodRuleUrlActnHstSec = _Layer7NewCfgHttpmodRuleUrlActnHstSec_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 6, 1, 15),
    _Layer7NewCfgHttpmodRuleUrlActnHstSec_Type()
)
layer7NewCfgHttpmodRuleUrlActnHstSec.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    layer7NewCfgHttpmodRuleUrlActnHstSec.setStatus("current")


class _Layer7NewCfgHttpmodRuleUrlActnHstRplc_Type(DisplayString):
    """Custom type layer7NewCfgHttpmodRuleUrlActnHstRplc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Layer7NewCfgHttpmodRuleUrlActnHstRplc_Type.__name__ = "DisplayString"
_Layer7NewCfgHttpmodRuleUrlActnHstRplc_Object = MibTableColumn
layer7NewCfgHttpmodRuleUrlActnHstRplc = _Layer7NewCfgHttpmodRuleUrlActnHstRplc_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 6, 1, 16),
    _Layer7NewCfgHttpmodRuleUrlActnHstRplc_Type()
)
layer7NewCfgHttpmodRuleUrlActnHstRplc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    layer7NewCfgHttpmodRuleUrlActnHstRplc.setStatus("current")


class _Layer7NewCfgHttpmodRuleUrlActnPathTyp_Type(Integer32):
    """Custom type layer7NewCfgHttpmodRuleUrlActnPathTyp based on Integer32"""
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
        *(("insert", 1),
          ("none", 4),
          ("remove", 3),
          ("replace", 2))
    )


_Layer7NewCfgHttpmodRuleUrlActnPathTyp_Type.__name__ = "Integer32"
_Layer7NewCfgHttpmodRuleUrlActnPathTyp_Object = MibTableColumn
layer7NewCfgHttpmodRuleUrlActnPathTyp = _Layer7NewCfgHttpmodRuleUrlActnPathTyp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 6, 1, 17),
    _Layer7NewCfgHttpmodRuleUrlActnPathTyp_Type()
)
layer7NewCfgHttpmodRuleUrlActnPathTyp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    layer7NewCfgHttpmodRuleUrlActnPathTyp.setStatus("current")


class _Layer7NewCfgHttpmodRuleUrlActnPath_Type(DisplayString):
    """Custom type layer7NewCfgHttpmodRuleUrlActnPath based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Layer7NewCfgHttpmodRuleUrlActnPath_Type.__name__ = "DisplayString"
_Layer7NewCfgHttpmodRuleUrlActnPath_Object = MibTableColumn
layer7NewCfgHttpmodRuleUrlActnPath = _Layer7NewCfgHttpmodRuleUrlActnPath_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 6, 1, 18),
    _Layer7NewCfgHttpmodRuleUrlActnPath_Type()
)
layer7NewCfgHttpmodRuleUrlActnPath.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    layer7NewCfgHttpmodRuleUrlActnPath.setStatus("current")


class _Layer7NewCfgHttpmodRuleUrlActnPthSctn_Type(Integer32):
    """Custom type layer7NewCfgHttpmodRuleUrlActnPthSctn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("after", 2),
          ("before", 1))
    )


_Layer7NewCfgHttpmodRuleUrlActnPthSctn_Type.__name__ = "Integer32"
_Layer7NewCfgHttpmodRuleUrlActnPthSctn_Object = MibTableColumn
layer7NewCfgHttpmodRuleUrlActnPthSctn = _Layer7NewCfgHttpmodRuleUrlActnPthSctn_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 6, 1, 19),
    _Layer7NewCfgHttpmodRuleUrlActnPthSctn_Type()
)
layer7NewCfgHttpmodRuleUrlActnPthSctn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    layer7NewCfgHttpmodRuleUrlActnPthSctn.setStatus("current")


class _Layer7NewCfgHttpmodRuleUrlActnPthRplc_Type(DisplayString):
    """Custom type layer7NewCfgHttpmodRuleUrlActnPthRplc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Layer7NewCfgHttpmodRuleUrlActnPthRplc_Type.__name__ = "DisplayString"
_Layer7NewCfgHttpmodRuleUrlActnPthRplc_Object = MibTableColumn
layer7NewCfgHttpmodRuleUrlActnPthRplc = _Layer7NewCfgHttpmodRuleUrlActnPthRplc_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 6, 1, 20),
    _Layer7NewCfgHttpmodRuleUrlActnPthRplc_Type()
)
layer7NewCfgHttpmodRuleUrlActnPthRplc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    layer7NewCfgHttpmodRuleUrlActnPthRplc.setStatus("current")


class _Layer7NewCfgHttpmodRuleUrlActnPgName_Type(DisplayString):
    """Custom type layer7NewCfgHttpmodRuleUrlActnPgName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Layer7NewCfgHttpmodRuleUrlActnPgName_Type.__name__ = "DisplayString"
_Layer7NewCfgHttpmodRuleUrlActnPgName_Object = MibTableColumn
layer7NewCfgHttpmodRuleUrlActnPgName = _Layer7NewCfgHttpmodRuleUrlActnPgName_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 6, 1, 21),
    _Layer7NewCfgHttpmodRuleUrlActnPgName_Type()
)
layer7NewCfgHttpmodRuleUrlActnPgName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    layer7NewCfgHttpmodRuleUrlActnPgName.setStatus("current")


class _Layer7NewCfgHttpmodRuleUrlActnPgTyp_Type(DisplayString):
    """Custom type layer7NewCfgHttpmodRuleUrlActnPgTyp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Layer7NewCfgHttpmodRuleUrlActnPgTyp_Type.__name__ = "DisplayString"
_Layer7NewCfgHttpmodRuleUrlActnPgTyp_Object = MibTableColumn
layer7NewCfgHttpmodRuleUrlActnPgTyp = _Layer7NewCfgHttpmodRuleUrlActnPgTyp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 6, 1, 22),
    _Layer7NewCfgHttpmodRuleUrlActnPgTyp_Type()
)
layer7NewCfgHttpmodRuleUrlActnPgTyp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    layer7NewCfgHttpmodRuleUrlActnPgTyp.setStatus("current")
_Layer7CurCfgHttpmodRuleHdrTable_Object = MibTable
layer7CurCfgHttpmodRuleHdrTable = _Layer7CurCfgHttpmodRuleHdrTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 7)
)
if mibBuilder.loadTexts:
    layer7CurCfgHttpmodRuleHdrTable.setStatus("current")
_Layer7CurCfgHttpmodRuleHdrEntry_Object = MibTableRow
layer7CurCfgHttpmodRuleHdrEntry = _Layer7CurCfgHttpmodRuleHdrEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 7, 1)
)
layer7CurCfgHttpmodRuleHdrEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-LAYER7-MIB", "layer7CurCfgHttpmodRuleHdrListIdIndex"),
    (0, "ALTEON-CHEETAH-LAYER7-MIB", "layer7CurCfgHttpmodRuleHdrIndex"),
)
if mibBuilder.loadTexts:
    layer7CurCfgHttpmodRuleHdrEntry.setStatus("current")


class _Layer7CurCfgHttpmodRuleHdrListIdIndex_Type(DisplayString):
    """Custom type layer7CurCfgHttpmodRuleHdrListIdIndex based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Layer7CurCfgHttpmodRuleHdrListIdIndex_Type.__name__ = "DisplayString"
_Layer7CurCfgHttpmodRuleHdrListIdIndex_Object = MibTableColumn
layer7CurCfgHttpmodRuleHdrListIdIndex = _Layer7CurCfgHttpmodRuleHdrListIdIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 7, 1, 1),
    _Layer7CurCfgHttpmodRuleHdrListIdIndex_Type()
)
layer7CurCfgHttpmodRuleHdrListIdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgHttpmodRuleHdrListIdIndex.setStatus("current")
_Layer7CurCfgHttpmodRuleHdrIndex_Type = Integer32
_Layer7CurCfgHttpmodRuleHdrIndex_Object = MibTableColumn
layer7CurCfgHttpmodRuleHdrIndex = _Layer7CurCfgHttpmodRuleHdrIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 7, 1, 2),
    _Layer7CurCfgHttpmodRuleHdrIndex_Type()
)
layer7CurCfgHttpmodRuleHdrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgHttpmodRuleHdrIndex.setStatus("current")


class _Layer7CurCfgHttpmodRuleHdrInsert_Type(DisplayString):
    """Custom type layer7CurCfgHttpmodRuleHdrInsert based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Layer7CurCfgHttpmodRuleHdrInsert_Type.__name__ = "DisplayString"
_Layer7CurCfgHttpmodRuleHdrInsert_Object = MibTableColumn
layer7CurCfgHttpmodRuleHdrInsert = _Layer7CurCfgHttpmodRuleHdrInsert_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 7, 1, 3),
    _Layer7CurCfgHttpmodRuleHdrInsert_Type()
)
layer7CurCfgHttpmodRuleHdrInsert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgHttpmodRuleHdrInsert.setStatus("current")


class _Layer7CurCfgHttpmodRuleHdrValue_Type(DisplayString):
    """Custom type layer7CurCfgHttpmodRuleHdrValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Layer7CurCfgHttpmodRuleHdrValue_Type.__name__ = "DisplayString"
_Layer7CurCfgHttpmodRuleHdrValue_Object = MibTableColumn
layer7CurCfgHttpmodRuleHdrValue = _Layer7CurCfgHttpmodRuleHdrValue_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 7, 1, 4),
    _Layer7CurCfgHttpmodRuleHdrValue_Type()
)
layer7CurCfgHttpmodRuleHdrValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgHttpmodRuleHdrValue.setStatus("current")


class _Layer7CurCfgHttpmodRuleHdrElmnt_Type(Integer32):
    """Custom type layer7CurCfgHttpmodRuleHdrElmnt based on Integer32"""
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
        *(("cookie", 3),
          ("filetype", 4),
          ("header", 2),
          ("none", 8),
          ("regex", 7),
          ("statusline", 5),
          ("text", 6),
          ("url", 1))
    )


_Layer7CurCfgHttpmodRuleHdrElmnt_Type.__name__ = "Integer32"
_Layer7CurCfgHttpmodRuleHdrElmnt_Object = MibTableColumn
layer7CurCfgHttpmodRuleHdrElmnt = _Layer7CurCfgHttpmodRuleHdrElmnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 7, 1, 5),
    _Layer7CurCfgHttpmodRuleHdrElmnt_Type()
)
layer7CurCfgHttpmodRuleHdrElmnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgHttpmodRuleHdrElmnt.setStatus("current")


class _Layer7CurCfgHttpmodRuleHdrElmntUrlHost_Type(DisplayString):
    """Custom type layer7CurCfgHttpmodRuleHdrElmntUrlHost based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Layer7CurCfgHttpmodRuleHdrElmntUrlHost_Type.__name__ = "DisplayString"
_Layer7CurCfgHttpmodRuleHdrElmntUrlHost_Object = MibTableColumn
layer7CurCfgHttpmodRuleHdrElmntUrlHost = _Layer7CurCfgHttpmodRuleHdrElmntUrlHost_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 7, 1, 6),
    _Layer7CurCfgHttpmodRuleHdrElmntUrlHost_Type()
)
layer7CurCfgHttpmodRuleHdrElmntUrlHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgHttpmodRuleHdrElmntUrlHost.setStatus("current")


class _Layer7CurCfgHttpmodRuleHdrElmntUrlPath_Type(DisplayString):
    """Custom type layer7CurCfgHttpmodRuleHdrElmntUrlPath based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Layer7CurCfgHttpmodRuleHdrElmntUrlPath_Type.__name__ = "DisplayString"
_Layer7CurCfgHttpmodRuleHdrElmntUrlPath_Object = MibTableColumn
layer7CurCfgHttpmodRuleHdrElmntUrlPath = _Layer7CurCfgHttpmodRuleHdrElmntUrlPath_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 7, 1, 7),
    _Layer7CurCfgHttpmodRuleHdrElmntUrlPath_Type()
)
layer7CurCfgHttpmodRuleHdrElmntUrlPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgHttpmodRuleHdrElmntUrlPath.setStatus("current")


class _Layer7CurCfgHttpmodRuleHdrElmntHdrField_Type(DisplayString):
    """Custom type layer7CurCfgHttpmodRuleHdrElmntHdrField based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Layer7CurCfgHttpmodRuleHdrElmntHdrField_Type.__name__ = "DisplayString"
_Layer7CurCfgHttpmodRuleHdrElmntHdrField_Object = MibTableColumn
layer7CurCfgHttpmodRuleHdrElmntHdrField = _Layer7CurCfgHttpmodRuleHdrElmntHdrField_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 7, 1, 8),
    _Layer7CurCfgHttpmodRuleHdrElmntHdrField_Type()
)
layer7CurCfgHttpmodRuleHdrElmntHdrField.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgHttpmodRuleHdrElmntHdrField.setStatus("current")


class _Layer7CurCfgHttpmodRuleHdrElmntHdrVal_Type(DisplayString):
    """Custom type layer7CurCfgHttpmodRuleHdrElmntHdrVal based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Layer7CurCfgHttpmodRuleHdrElmntHdrVal_Type.__name__ = "DisplayString"
_Layer7CurCfgHttpmodRuleHdrElmntHdrVal_Object = MibTableColumn
layer7CurCfgHttpmodRuleHdrElmntHdrVal = _Layer7CurCfgHttpmodRuleHdrElmntHdrVal_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 7, 1, 9),
    _Layer7CurCfgHttpmodRuleHdrElmntHdrVal_Type()
)
layer7CurCfgHttpmodRuleHdrElmntHdrVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgHttpmodRuleHdrElmntHdrVal.setStatus("current")


class _Layer7CurCfgHttpmodRuleHdrElmntCookey_Type(DisplayString):
    """Custom type layer7CurCfgHttpmodRuleHdrElmntCookey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_Layer7CurCfgHttpmodRuleHdrElmntCookey_Type.__name__ = "DisplayString"
_Layer7CurCfgHttpmodRuleHdrElmntCookey_Object = MibTableColumn
layer7CurCfgHttpmodRuleHdrElmntCookey = _Layer7CurCfgHttpmodRuleHdrElmntCookey_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 7, 1, 10),
    _Layer7CurCfgHttpmodRuleHdrElmntCookey_Type()
)
layer7CurCfgHttpmodRuleHdrElmntCookey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgHttpmodRuleHdrElmntCookey.setStatus("current")


class _Layer7CurCfgHttpmodRuleHdrElmntCkieVal_Type(DisplayString):
    """Custom type layer7CurCfgHttpmodRuleHdrElmntCkieVal based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_Layer7CurCfgHttpmodRuleHdrElmntCkieVal_Type.__name__ = "DisplayString"
_Layer7CurCfgHttpmodRuleHdrElmntCkieVal_Object = MibTableColumn
layer7CurCfgHttpmodRuleHdrElmntCkieVal = _Layer7CurCfgHttpmodRuleHdrElmntCkieVal_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 7, 1, 11),
    _Layer7CurCfgHttpmodRuleHdrElmntCkieVal_Type()
)
layer7CurCfgHttpmodRuleHdrElmntCkieVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgHttpmodRuleHdrElmntCkieVal.setStatus("current")


class _Layer7CurCfgHttpmodRuleHdrElmntFileTyp_Type(DisplayString):
    """Custom type layer7CurCfgHttpmodRuleHdrElmntFileTyp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Layer7CurCfgHttpmodRuleHdrElmntFileTyp_Type.__name__ = "DisplayString"
_Layer7CurCfgHttpmodRuleHdrElmntFileTyp_Object = MibTableColumn
layer7CurCfgHttpmodRuleHdrElmntFileTyp = _Layer7CurCfgHttpmodRuleHdrElmntFileTyp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 7, 1, 12),
    _Layer7CurCfgHttpmodRuleHdrElmntFileTyp_Type()
)
layer7CurCfgHttpmodRuleHdrElmntFileTyp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgHttpmodRuleHdrElmntFileTyp.setStatus("current")
_Layer7CurCfgHttpmodRuleHdrElmntStatusCode_Type = Integer32
_Layer7CurCfgHttpmodRuleHdrElmntStatusCode_Object = MibTableColumn
layer7CurCfgHttpmodRuleHdrElmntStatusCode = _Layer7CurCfgHttpmodRuleHdrElmntStatusCode_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 7, 1, 13),
    _Layer7CurCfgHttpmodRuleHdrElmntStatusCode_Type()
)
layer7CurCfgHttpmodRuleHdrElmntStatusCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgHttpmodRuleHdrElmntStatusCode.setStatus("current")


class _Layer7CurCfgHttpmodRuleHdrElmntStatusTxt_Type(DisplayString):
    """Custom type layer7CurCfgHttpmodRuleHdrElmntStatusTxt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Layer7CurCfgHttpmodRuleHdrElmntStatusTxt_Type.__name__ = "DisplayString"
_Layer7CurCfgHttpmodRuleHdrElmntStatusTxt_Object = MibTableColumn
layer7CurCfgHttpmodRuleHdrElmntStatusTxt = _Layer7CurCfgHttpmodRuleHdrElmntStatusTxt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 7, 1, 14),
    _Layer7CurCfgHttpmodRuleHdrElmntStatusTxt_Type()
)
layer7CurCfgHttpmodRuleHdrElmntStatusTxt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgHttpmodRuleHdrElmntStatusTxt.setStatus("current")


class _Layer7CurCfgHttpmodRuleHdrElmntTxt_Type(DisplayString):
    """Custom type layer7CurCfgHttpmodRuleHdrElmntTxt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Layer7CurCfgHttpmodRuleHdrElmntTxt_Type.__name__ = "DisplayString"
_Layer7CurCfgHttpmodRuleHdrElmntTxt_Object = MibTableColumn
layer7CurCfgHttpmodRuleHdrElmntTxt = _Layer7CurCfgHttpmodRuleHdrElmntTxt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 7, 1, 15),
    _Layer7CurCfgHttpmodRuleHdrElmntTxt_Type()
)
layer7CurCfgHttpmodRuleHdrElmntTxt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgHttpmodRuleHdrElmntTxt.setStatus("current")


class _Layer7CurCfgHttpmodRuleHdrElmntRegx_Type(DisplayString):
    """Custom type layer7CurCfgHttpmodRuleHdrElmntRegx based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Layer7CurCfgHttpmodRuleHdrElmntRegx_Type.__name__ = "DisplayString"
_Layer7CurCfgHttpmodRuleHdrElmntRegx_Object = MibTableColumn
layer7CurCfgHttpmodRuleHdrElmntRegx = _Layer7CurCfgHttpmodRuleHdrElmntRegx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 7, 1, 16),
    _Layer7CurCfgHttpmodRuleHdrElmntRegx_Type()
)
layer7CurCfgHttpmodRuleHdrElmntRegx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgHttpmodRuleHdrElmntRegx.setStatus("current")


class _Layer7CurCfgHttpmodRuleHdrReplacHdr_Type(DisplayString):
    """Custom type layer7CurCfgHttpmodRuleHdrReplacHdr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Layer7CurCfgHttpmodRuleHdrReplacHdr_Type.__name__ = "DisplayString"
_Layer7CurCfgHttpmodRuleHdrReplacHdr_Object = MibTableColumn
layer7CurCfgHttpmodRuleHdrReplacHdr = _Layer7CurCfgHttpmodRuleHdrReplacHdr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 7, 1, 17),
    _Layer7CurCfgHttpmodRuleHdrReplacHdr_Type()
)
layer7CurCfgHttpmodRuleHdrReplacHdr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgHttpmodRuleHdrReplacHdr.setStatus("current")


class _Layer7CurCfgHttpmodRuleHdrReplacVal_Type(DisplayString):
    """Custom type layer7CurCfgHttpmodRuleHdrReplacVal based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Layer7CurCfgHttpmodRuleHdrReplacVal_Type.__name__ = "DisplayString"
_Layer7CurCfgHttpmodRuleHdrReplacVal_Object = MibTableColumn
layer7CurCfgHttpmodRuleHdrReplacVal = _Layer7CurCfgHttpmodRuleHdrReplacVal_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 7, 1, 18),
    _Layer7CurCfgHttpmodRuleHdrReplacVal_Type()
)
layer7CurCfgHttpmodRuleHdrReplacVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgHttpmodRuleHdrReplacVal.setStatus("current")


class _Layer7CurCfgHttpmodRuleHdrReplacNewHdr_Type(DisplayString):
    """Custom type layer7CurCfgHttpmodRuleHdrReplacNewHdr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Layer7CurCfgHttpmodRuleHdrReplacNewHdr_Type.__name__ = "DisplayString"
_Layer7CurCfgHttpmodRuleHdrReplacNewHdr_Object = MibTableColumn
layer7CurCfgHttpmodRuleHdrReplacNewHdr = _Layer7CurCfgHttpmodRuleHdrReplacNewHdr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 7, 1, 19),
    _Layer7CurCfgHttpmodRuleHdrReplacNewHdr_Type()
)
layer7CurCfgHttpmodRuleHdrReplacNewHdr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgHttpmodRuleHdrReplacNewHdr.setStatus("current")


class _Layer7CurCfgHttpmodRuleHdrReplacNewVal_Type(DisplayString):
    """Custom type layer7CurCfgHttpmodRuleHdrReplacNewVal based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Layer7CurCfgHttpmodRuleHdrReplacNewVal_Type.__name__ = "DisplayString"
_Layer7CurCfgHttpmodRuleHdrReplacNewVal_Object = MibTableColumn
layer7CurCfgHttpmodRuleHdrReplacNewVal = _Layer7CurCfgHttpmodRuleHdrReplacNewVal_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 7, 1, 20),
    _Layer7CurCfgHttpmodRuleHdrReplacNewVal_Type()
)
layer7CurCfgHttpmodRuleHdrReplacNewVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgHttpmodRuleHdrReplacNewVal.setStatus("current")


class _Layer7CurCfgHttpmodRuleHdrRemvHdr_Type(DisplayString):
    """Custom type layer7CurCfgHttpmodRuleHdrRemvHdr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Layer7CurCfgHttpmodRuleHdrRemvHdr_Type.__name__ = "DisplayString"
_Layer7CurCfgHttpmodRuleHdrRemvHdr_Object = MibTableColumn
layer7CurCfgHttpmodRuleHdrRemvHdr = _Layer7CurCfgHttpmodRuleHdrRemvHdr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 7, 1, 21),
    _Layer7CurCfgHttpmodRuleHdrRemvHdr_Type()
)
layer7CurCfgHttpmodRuleHdrRemvHdr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgHttpmodRuleHdrRemvHdr.setStatus("current")


class _Layer7CurCfgHttpmodRuleHdrRemvVal_Type(DisplayString):
    """Custom type layer7CurCfgHttpmodRuleHdrRemvVal based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Layer7CurCfgHttpmodRuleHdrRemvVal_Type.__name__ = "DisplayString"
_Layer7CurCfgHttpmodRuleHdrRemvVal_Object = MibTableColumn
layer7CurCfgHttpmodRuleHdrRemvVal = _Layer7CurCfgHttpmodRuleHdrRemvVal_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 7, 1, 22),
    _Layer7CurCfgHttpmodRuleHdrRemvVal_Type()
)
layer7CurCfgHttpmodRuleHdrRemvVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgHttpmodRuleHdrRemvVal.setStatus("current")
_Layer7NewCfgHttpmodRuleHdrTable_Object = MibTable
layer7NewCfgHttpmodRuleHdrTable = _Layer7NewCfgHttpmodRuleHdrTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 8)
)
if mibBuilder.loadTexts:
    layer7NewCfgHttpmodRuleHdrTable.setStatus("current")
_Layer7NewCfgHttpmodRuleHdrEntry_Object = MibTableRow
layer7NewCfgHttpmodRuleHdrEntry = _Layer7NewCfgHttpmodRuleHdrEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 8, 1)
)
layer7NewCfgHttpmodRuleHdrEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-LAYER7-MIB", "layer7NewCfgHttpmodRuleHdrListIdIndex"),
    (0, "ALTEON-CHEETAH-LAYER7-MIB", "layer7NewCfgHttpmodRuleHdrIndex"),
)
if mibBuilder.loadTexts:
    layer7NewCfgHttpmodRuleHdrEntry.setStatus("current")


class _Layer7NewCfgHttpmodRuleHdrListIdIndex_Type(DisplayString):
    """Custom type layer7NewCfgHttpmodRuleHdrListIdIndex based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Layer7NewCfgHttpmodRuleHdrListIdIndex_Type.__name__ = "DisplayString"
_Layer7NewCfgHttpmodRuleHdrListIdIndex_Object = MibTableColumn
layer7NewCfgHttpmodRuleHdrListIdIndex = _Layer7NewCfgHttpmodRuleHdrListIdIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 8, 1, 1),
    _Layer7NewCfgHttpmodRuleHdrListIdIndex_Type()
)
layer7NewCfgHttpmodRuleHdrListIdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7NewCfgHttpmodRuleHdrListIdIndex.setStatus("current")
_Layer7NewCfgHttpmodRuleHdrIndex_Type = Integer32
_Layer7NewCfgHttpmodRuleHdrIndex_Object = MibTableColumn
layer7NewCfgHttpmodRuleHdrIndex = _Layer7NewCfgHttpmodRuleHdrIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 8, 1, 2),
    _Layer7NewCfgHttpmodRuleHdrIndex_Type()
)
layer7NewCfgHttpmodRuleHdrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7NewCfgHttpmodRuleHdrIndex.setStatus("current")


class _Layer7NewCfgHttpmodRuleHdrInsert_Type(DisplayString):
    """Custom type layer7NewCfgHttpmodRuleHdrInsert based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Layer7NewCfgHttpmodRuleHdrInsert_Type.__name__ = "DisplayString"
_Layer7NewCfgHttpmodRuleHdrInsert_Object = MibTableColumn
layer7NewCfgHttpmodRuleHdrInsert = _Layer7NewCfgHttpmodRuleHdrInsert_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 8, 1, 3),
    _Layer7NewCfgHttpmodRuleHdrInsert_Type()
)
layer7NewCfgHttpmodRuleHdrInsert.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    layer7NewCfgHttpmodRuleHdrInsert.setStatus("current")


class _Layer7NewCfgHttpmodRuleHdrValue_Type(DisplayString):
    """Custom type layer7NewCfgHttpmodRuleHdrValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Layer7NewCfgHttpmodRuleHdrValue_Type.__name__ = "DisplayString"
_Layer7NewCfgHttpmodRuleHdrValue_Object = MibTableColumn
layer7NewCfgHttpmodRuleHdrValue = _Layer7NewCfgHttpmodRuleHdrValue_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 8, 1, 4),
    _Layer7NewCfgHttpmodRuleHdrValue_Type()
)
layer7NewCfgHttpmodRuleHdrValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    layer7NewCfgHttpmodRuleHdrValue.setStatus("current")


class _Layer7NewCfgHttpmodRuleHdrElmnt_Type(Integer32):
    """Custom type layer7NewCfgHttpmodRuleHdrElmnt based on Integer32"""
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
        *(("cookie", 3),
          ("filetype", 4),
          ("header", 2),
          ("none", 8),
          ("regex", 7),
          ("statusline", 5),
          ("text", 6),
          ("url", 1))
    )


_Layer7NewCfgHttpmodRuleHdrElmnt_Type.__name__ = "Integer32"
_Layer7NewCfgHttpmodRuleHdrElmnt_Object = MibTableColumn
layer7NewCfgHttpmodRuleHdrElmnt = _Layer7NewCfgHttpmodRuleHdrElmnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 8, 1, 5),
    _Layer7NewCfgHttpmodRuleHdrElmnt_Type()
)
layer7NewCfgHttpmodRuleHdrElmnt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    layer7NewCfgHttpmodRuleHdrElmnt.setStatus("current")


class _Layer7NewCfgHttpmodRuleHdrElmntUrlHost_Type(DisplayString):
    """Custom type layer7NewCfgHttpmodRuleHdrElmntUrlHost based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Layer7NewCfgHttpmodRuleHdrElmntUrlHost_Type.__name__ = "DisplayString"
_Layer7NewCfgHttpmodRuleHdrElmntUrlHost_Object = MibTableColumn
layer7NewCfgHttpmodRuleHdrElmntUrlHost = _Layer7NewCfgHttpmodRuleHdrElmntUrlHost_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 8, 1, 6),
    _Layer7NewCfgHttpmodRuleHdrElmntUrlHost_Type()
)
layer7NewCfgHttpmodRuleHdrElmntUrlHost.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    layer7NewCfgHttpmodRuleHdrElmntUrlHost.setStatus("current")


class _Layer7NewCfgHttpmodRuleHdrElmntUrlPath_Type(DisplayString):
    """Custom type layer7NewCfgHttpmodRuleHdrElmntUrlPath based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Layer7NewCfgHttpmodRuleHdrElmntUrlPath_Type.__name__ = "DisplayString"
_Layer7NewCfgHttpmodRuleHdrElmntUrlPath_Object = MibTableColumn
layer7NewCfgHttpmodRuleHdrElmntUrlPath = _Layer7NewCfgHttpmodRuleHdrElmntUrlPath_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 8, 1, 7),
    _Layer7NewCfgHttpmodRuleHdrElmntUrlPath_Type()
)
layer7NewCfgHttpmodRuleHdrElmntUrlPath.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    layer7NewCfgHttpmodRuleHdrElmntUrlPath.setStatus("current")


class _Layer7NewCfgHttpmodRuleHdrElmntHdrField_Type(DisplayString):
    """Custom type layer7NewCfgHttpmodRuleHdrElmntHdrField based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Layer7NewCfgHttpmodRuleHdrElmntHdrField_Type.__name__ = "DisplayString"
_Layer7NewCfgHttpmodRuleHdrElmntHdrField_Object = MibTableColumn
layer7NewCfgHttpmodRuleHdrElmntHdrField = _Layer7NewCfgHttpmodRuleHdrElmntHdrField_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 8, 1, 8),
    _Layer7NewCfgHttpmodRuleHdrElmntHdrField_Type()
)
layer7NewCfgHttpmodRuleHdrElmntHdrField.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    layer7NewCfgHttpmodRuleHdrElmntHdrField.setStatus("current")


class _Layer7NewCfgHttpmodRuleHdrElmntHdrVal_Type(DisplayString):
    """Custom type layer7NewCfgHttpmodRuleHdrElmntHdrVal based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Layer7NewCfgHttpmodRuleHdrElmntHdrVal_Type.__name__ = "DisplayString"
_Layer7NewCfgHttpmodRuleHdrElmntHdrVal_Object = MibTableColumn
layer7NewCfgHttpmodRuleHdrElmntHdrVal = _Layer7NewCfgHttpmodRuleHdrElmntHdrVal_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 8, 1, 9),
    _Layer7NewCfgHttpmodRuleHdrElmntHdrVal_Type()
)
layer7NewCfgHttpmodRuleHdrElmntHdrVal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    layer7NewCfgHttpmodRuleHdrElmntHdrVal.setStatus("current")


class _Layer7NewCfgHttpmodRuleHdrElmntCookey_Type(DisplayString):
    """Custom type layer7NewCfgHttpmodRuleHdrElmntCookey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_Layer7NewCfgHttpmodRuleHdrElmntCookey_Type.__name__ = "DisplayString"
_Layer7NewCfgHttpmodRuleHdrElmntCookey_Object = MibTableColumn
layer7NewCfgHttpmodRuleHdrElmntCookey = _Layer7NewCfgHttpmodRuleHdrElmntCookey_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 8, 1, 10),
    _Layer7NewCfgHttpmodRuleHdrElmntCookey_Type()
)
layer7NewCfgHttpmodRuleHdrElmntCookey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    layer7NewCfgHttpmodRuleHdrElmntCookey.setStatus("current")


class _Layer7NewCfgHttpmodRuleHdrElmntCkieVal_Type(DisplayString):
    """Custom type layer7NewCfgHttpmodRuleHdrElmntCkieVal based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_Layer7NewCfgHttpmodRuleHdrElmntCkieVal_Type.__name__ = "DisplayString"
_Layer7NewCfgHttpmodRuleHdrElmntCkieVal_Object = MibTableColumn
layer7NewCfgHttpmodRuleHdrElmntCkieVal = _Layer7NewCfgHttpmodRuleHdrElmntCkieVal_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 8, 1, 11),
    _Layer7NewCfgHttpmodRuleHdrElmntCkieVal_Type()
)
layer7NewCfgHttpmodRuleHdrElmntCkieVal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    layer7NewCfgHttpmodRuleHdrElmntCkieVal.setStatus("current")


class _Layer7NewCfgHttpmodRuleHdrElmntFileTyp_Type(DisplayString):
    """Custom type layer7NewCfgHttpmodRuleHdrElmntFileTyp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Layer7NewCfgHttpmodRuleHdrElmntFileTyp_Type.__name__ = "DisplayString"
_Layer7NewCfgHttpmodRuleHdrElmntFileTyp_Object = MibTableColumn
layer7NewCfgHttpmodRuleHdrElmntFileTyp = _Layer7NewCfgHttpmodRuleHdrElmntFileTyp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 8, 1, 12),
    _Layer7NewCfgHttpmodRuleHdrElmntFileTyp_Type()
)
layer7NewCfgHttpmodRuleHdrElmntFileTyp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    layer7NewCfgHttpmodRuleHdrElmntFileTyp.setStatus("current")
_Layer7NewCfgHttpmodRuleHdrElmntStatusCode_Type = Integer32
_Layer7NewCfgHttpmodRuleHdrElmntStatusCode_Object = MibTableColumn
layer7NewCfgHttpmodRuleHdrElmntStatusCode = _Layer7NewCfgHttpmodRuleHdrElmntStatusCode_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 8, 1, 13),
    _Layer7NewCfgHttpmodRuleHdrElmntStatusCode_Type()
)
layer7NewCfgHttpmodRuleHdrElmntStatusCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    layer7NewCfgHttpmodRuleHdrElmntStatusCode.setStatus("current")


class _Layer7NewCfgHttpmodRuleHdrElmntStatusTxt_Type(DisplayString):
    """Custom type layer7NewCfgHttpmodRuleHdrElmntStatusTxt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Layer7NewCfgHttpmodRuleHdrElmntStatusTxt_Type.__name__ = "DisplayString"
_Layer7NewCfgHttpmodRuleHdrElmntStatusTxt_Object = MibTableColumn
layer7NewCfgHttpmodRuleHdrElmntStatusTxt = _Layer7NewCfgHttpmodRuleHdrElmntStatusTxt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 8, 1, 14),
    _Layer7NewCfgHttpmodRuleHdrElmntStatusTxt_Type()
)
layer7NewCfgHttpmodRuleHdrElmntStatusTxt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    layer7NewCfgHttpmodRuleHdrElmntStatusTxt.setStatus("current")


class _Layer7NewCfgHttpmodRuleHdrElmntTxt_Type(DisplayString):
    """Custom type layer7NewCfgHttpmodRuleHdrElmntTxt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Layer7NewCfgHttpmodRuleHdrElmntTxt_Type.__name__ = "DisplayString"
_Layer7NewCfgHttpmodRuleHdrElmntTxt_Object = MibTableColumn
layer7NewCfgHttpmodRuleHdrElmntTxt = _Layer7NewCfgHttpmodRuleHdrElmntTxt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 8, 1, 15),
    _Layer7NewCfgHttpmodRuleHdrElmntTxt_Type()
)
layer7NewCfgHttpmodRuleHdrElmntTxt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    layer7NewCfgHttpmodRuleHdrElmntTxt.setStatus("current")


class _Layer7NewCfgHttpmodRuleHdrElmntRegx_Type(DisplayString):
    """Custom type layer7NewCfgHttpmodRuleHdrElmntRegx based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Layer7NewCfgHttpmodRuleHdrElmntRegx_Type.__name__ = "DisplayString"
_Layer7NewCfgHttpmodRuleHdrElmntRegx_Object = MibTableColumn
layer7NewCfgHttpmodRuleHdrElmntRegx = _Layer7NewCfgHttpmodRuleHdrElmntRegx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 8, 1, 16),
    _Layer7NewCfgHttpmodRuleHdrElmntRegx_Type()
)
layer7NewCfgHttpmodRuleHdrElmntRegx.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    layer7NewCfgHttpmodRuleHdrElmntRegx.setStatus("current")


class _Layer7NewCfgHttpmodRuleHdrReplacHdr_Type(DisplayString):
    """Custom type layer7NewCfgHttpmodRuleHdrReplacHdr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Layer7NewCfgHttpmodRuleHdrReplacHdr_Type.__name__ = "DisplayString"
_Layer7NewCfgHttpmodRuleHdrReplacHdr_Object = MibTableColumn
layer7NewCfgHttpmodRuleHdrReplacHdr = _Layer7NewCfgHttpmodRuleHdrReplacHdr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 8, 1, 17),
    _Layer7NewCfgHttpmodRuleHdrReplacHdr_Type()
)
layer7NewCfgHttpmodRuleHdrReplacHdr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    layer7NewCfgHttpmodRuleHdrReplacHdr.setStatus("current")


class _Layer7NewCfgHttpmodRuleHdrReplacVal_Type(DisplayString):
    """Custom type layer7NewCfgHttpmodRuleHdrReplacVal based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Layer7NewCfgHttpmodRuleHdrReplacVal_Type.__name__ = "DisplayString"
_Layer7NewCfgHttpmodRuleHdrReplacVal_Object = MibTableColumn
layer7NewCfgHttpmodRuleHdrReplacVal = _Layer7NewCfgHttpmodRuleHdrReplacVal_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 8, 1, 18),
    _Layer7NewCfgHttpmodRuleHdrReplacVal_Type()
)
layer7NewCfgHttpmodRuleHdrReplacVal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    layer7NewCfgHttpmodRuleHdrReplacVal.setStatus("current")


class _Layer7NewCfgHttpmodRuleHdrReplacNewHdr_Type(DisplayString):
    """Custom type layer7NewCfgHttpmodRuleHdrReplacNewHdr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Layer7NewCfgHttpmodRuleHdrReplacNewHdr_Type.__name__ = "DisplayString"
_Layer7NewCfgHttpmodRuleHdrReplacNewHdr_Object = MibTableColumn
layer7NewCfgHttpmodRuleHdrReplacNewHdr = _Layer7NewCfgHttpmodRuleHdrReplacNewHdr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 8, 1, 19),
    _Layer7NewCfgHttpmodRuleHdrReplacNewHdr_Type()
)
layer7NewCfgHttpmodRuleHdrReplacNewHdr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    layer7NewCfgHttpmodRuleHdrReplacNewHdr.setStatus("current")


class _Layer7NewCfgHttpmodRuleHdrReplacNewVal_Type(DisplayString):
    """Custom type layer7NewCfgHttpmodRuleHdrReplacNewVal based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Layer7NewCfgHttpmodRuleHdrReplacNewVal_Type.__name__ = "DisplayString"
_Layer7NewCfgHttpmodRuleHdrReplacNewVal_Object = MibTableColumn
layer7NewCfgHttpmodRuleHdrReplacNewVal = _Layer7NewCfgHttpmodRuleHdrReplacNewVal_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 8, 1, 20),
    _Layer7NewCfgHttpmodRuleHdrReplacNewVal_Type()
)
layer7NewCfgHttpmodRuleHdrReplacNewVal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    layer7NewCfgHttpmodRuleHdrReplacNewVal.setStatus("current")


class _Layer7NewCfgHttpmodRuleHdrRemvHdr_Type(DisplayString):
    """Custom type layer7NewCfgHttpmodRuleHdrRemvHdr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Layer7NewCfgHttpmodRuleHdrRemvHdr_Type.__name__ = "DisplayString"
_Layer7NewCfgHttpmodRuleHdrRemvHdr_Object = MibTableColumn
layer7NewCfgHttpmodRuleHdrRemvHdr = _Layer7NewCfgHttpmodRuleHdrRemvHdr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 8, 1, 21),
    _Layer7NewCfgHttpmodRuleHdrRemvHdr_Type()
)
layer7NewCfgHttpmodRuleHdrRemvHdr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    layer7NewCfgHttpmodRuleHdrRemvHdr.setStatus("current")


class _Layer7NewCfgHttpmodRuleHdrRemvVal_Type(DisplayString):
    """Custom type layer7NewCfgHttpmodRuleHdrRemvVal based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Layer7NewCfgHttpmodRuleHdrRemvVal_Type.__name__ = "DisplayString"
_Layer7NewCfgHttpmodRuleHdrRemvVal_Object = MibTableColumn
layer7NewCfgHttpmodRuleHdrRemvVal = _Layer7NewCfgHttpmodRuleHdrRemvVal_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 8, 1, 22),
    _Layer7NewCfgHttpmodRuleHdrRemvVal_Type()
)
layer7NewCfgHttpmodRuleHdrRemvVal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    layer7NewCfgHttpmodRuleHdrRemvVal.setStatus("current")
_Layer7CurCfgHttpmodRuleCookieTable_Object = MibTable
layer7CurCfgHttpmodRuleCookieTable = _Layer7CurCfgHttpmodRuleCookieTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 9)
)
if mibBuilder.loadTexts:
    layer7CurCfgHttpmodRuleCookieTable.setStatus("current")
_Layer7CurCfgHttpmodRuleCookieEntry_Object = MibTableRow
layer7CurCfgHttpmodRuleCookieEntry = _Layer7CurCfgHttpmodRuleCookieEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 9, 1)
)
layer7CurCfgHttpmodRuleCookieEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-LAYER7-MIB", "layer7CurCfgHttpmodRuleCookieListIdIndex"),
    (0, "ALTEON-CHEETAH-LAYER7-MIB", "layer7CurCfgHttpmodRuleCookieIndex"),
)
if mibBuilder.loadTexts:
    layer7CurCfgHttpmodRuleCookieEntry.setStatus("current")


class _Layer7CurCfgHttpmodRuleCookieListIdIndex_Type(DisplayString):
    """Custom type layer7CurCfgHttpmodRuleCookieListIdIndex based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Layer7CurCfgHttpmodRuleCookieListIdIndex_Type.__name__ = "DisplayString"
_Layer7CurCfgHttpmodRuleCookieListIdIndex_Object = MibTableColumn
layer7CurCfgHttpmodRuleCookieListIdIndex = _Layer7CurCfgHttpmodRuleCookieListIdIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 9, 1, 1),
    _Layer7CurCfgHttpmodRuleCookieListIdIndex_Type()
)
layer7CurCfgHttpmodRuleCookieListIdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgHttpmodRuleCookieListIdIndex.setStatus("current")
_Layer7CurCfgHttpmodRuleCookieIndex_Type = Integer32
_Layer7CurCfgHttpmodRuleCookieIndex_Object = MibTableColumn
layer7CurCfgHttpmodRuleCookieIndex = _Layer7CurCfgHttpmodRuleCookieIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 9, 1, 2),
    _Layer7CurCfgHttpmodRuleCookieIndex_Type()
)
layer7CurCfgHttpmodRuleCookieIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgHttpmodRuleCookieIndex.setStatus("current")


class _Layer7CurCfgHttpmodRuleCookieInsrtKey_Type(DisplayString):
    """Custom type layer7CurCfgHttpmodRuleCookieInsrtKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_Layer7CurCfgHttpmodRuleCookieInsrtKey_Type.__name__ = "DisplayString"
_Layer7CurCfgHttpmodRuleCookieInsrtKey_Object = MibTableColumn
layer7CurCfgHttpmodRuleCookieInsrtKey = _Layer7CurCfgHttpmodRuleCookieInsrtKey_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 9, 1, 3),
    _Layer7CurCfgHttpmodRuleCookieInsrtKey_Type()
)
layer7CurCfgHttpmodRuleCookieInsrtKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgHttpmodRuleCookieInsrtKey.setStatus("current")


class _Layer7CurCfgHttpmodRuleCookieInsrtVal_Type(DisplayString):
    """Custom type layer7CurCfgHttpmodRuleCookieInsrtVal based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_Layer7CurCfgHttpmodRuleCookieInsrtVal_Type.__name__ = "DisplayString"
_Layer7CurCfgHttpmodRuleCookieInsrtVal_Object = MibTableColumn
layer7CurCfgHttpmodRuleCookieInsrtVal = _Layer7CurCfgHttpmodRuleCookieInsrtVal_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 9, 1, 4),
    _Layer7CurCfgHttpmodRuleCookieInsrtVal_Type()
)
layer7CurCfgHttpmodRuleCookieInsrtVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgHttpmodRuleCookieInsrtVal.setStatus("current")


class _Layer7CurCfgHttpmodRuleCookieInsrtPath_Type(DisplayString):
    """Custom type layer7CurCfgHttpmodRuleCookieInsrtPath based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Layer7CurCfgHttpmodRuleCookieInsrtPath_Type.__name__ = "DisplayString"
_Layer7CurCfgHttpmodRuleCookieInsrtPath_Object = MibTableColumn
layer7CurCfgHttpmodRuleCookieInsrtPath = _Layer7CurCfgHttpmodRuleCookieInsrtPath_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 9, 1, 5),
    _Layer7CurCfgHttpmodRuleCookieInsrtPath_Type()
)
layer7CurCfgHttpmodRuleCookieInsrtPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgHttpmodRuleCookieInsrtPath.setStatus("current")


class _Layer7CurCfgHttpmodRuleCookieInsrtDomn_Type(DisplayString):
    """Custom type layer7CurCfgHttpmodRuleCookieInsrtDomn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65),
    )


_Layer7CurCfgHttpmodRuleCookieInsrtDomn_Type.__name__ = "DisplayString"
_Layer7CurCfgHttpmodRuleCookieInsrtDomn_Object = MibTableColumn
layer7CurCfgHttpmodRuleCookieInsrtDomn = _Layer7CurCfgHttpmodRuleCookieInsrtDomn_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 9, 1, 6),
    _Layer7CurCfgHttpmodRuleCookieInsrtDomn_Type()
)
layer7CurCfgHttpmodRuleCookieInsrtDomn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgHttpmodRuleCookieInsrtDomn.setStatus("current")


class _Layer7CurCfgHttpmodRuleCookieInsrtExp_Type(DisplayString):
    """Custom type layer7CurCfgHttpmodRuleCookieInsrtExp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Layer7CurCfgHttpmodRuleCookieInsrtExp_Type.__name__ = "DisplayString"
_Layer7CurCfgHttpmodRuleCookieInsrtExp_Object = MibTableColumn
layer7CurCfgHttpmodRuleCookieInsrtExp = _Layer7CurCfgHttpmodRuleCookieInsrtExp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 9, 1, 7),
    _Layer7CurCfgHttpmodRuleCookieInsrtExp_Type()
)
layer7CurCfgHttpmodRuleCookieInsrtExp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgHttpmodRuleCookieInsrtExp.setStatus("current")


class _Layer7CurCfgHttpmodRuleCookieInsrtElem_Type(Integer32):
    """Custom type layer7CurCfgHttpmodRuleCookieInsrtElem based on Integer32"""
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
        *(("cookie", 3),
          ("filetype", 4),
          ("header", 2),
          ("none", 8),
          ("regex", 7),
          ("statusline", 5),
          ("text", 6),
          ("url", 1))
    )


_Layer7CurCfgHttpmodRuleCookieInsrtElem_Type.__name__ = "Integer32"
_Layer7CurCfgHttpmodRuleCookieInsrtElem_Object = MibTableColumn
layer7CurCfgHttpmodRuleCookieInsrtElem = _Layer7CurCfgHttpmodRuleCookieInsrtElem_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 9, 1, 8),
    _Layer7CurCfgHttpmodRuleCookieInsrtElem_Type()
)
layer7CurCfgHttpmodRuleCookieInsrtElem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgHttpmodRuleCookieInsrtElem.setStatus("current")


class _Layer7CurCfgHttpmodRuleCookieInsrtUrlHost_Type(DisplayString):
    """Custom type layer7CurCfgHttpmodRuleCookieInsrtUrlHost based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Layer7CurCfgHttpmodRuleCookieInsrtUrlHost_Type.__name__ = "DisplayString"
_Layer7CurCfgHttpmodRuleCookieInsrtUrlHost_Object = MibTableColumn
layer7CurCfgHttpmodRuleCookieInsrtUrlHost = _Layer7CurCfgHttpmodRuleCookieInsrtUrlHost_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 9, 1, 9),
    _Layer7CurCfgHttpmodRuleCookieInsrtUrlHost_Type()
)
layer7CurCfgHttpmodRuleCookieInsrtUrlHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgHttpmodRuleCookieInsrtUrlHost.setStatus("current")


class _Layer7CurCfgHttpmodRuleCookieInsrtUrlPath_Type(DisplayString):
    """Custom type layer7CurCfgHttpmodRuleCookieInsrtUrlPath based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Layer7CurCfgHttpmodRuleCookieInsrtUrlPath_Type.__name__ = "DisplayString"
_Layer7CurCfgHttpmodRuleCookieInsrtUrlPath_Object = MibTableColumn
layer7CurCfgHttpmodRuleCookieInsrtUrlPath = _Layer7CurCfgHttpmodRuleCookieInsrtUrlPath_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 9, 1, 10),
    _Layer7CurCfgHttpmodRuleCookieInsrtUrlPath_Type()
)
layer7CurCfgHttpmodRuleCookieInsrtUrlPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgHttpmodRuleCookieInsrtUrlPath.setStatus("current")


class _Layer7CurCfgHttpmodRuleCookieInsrtHdrFld_Type(DisplayString):
    """Custom type layer7CurCfgHttpmodRuleCookieInsrtHdrFld based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Layer7CurCfgHttpmodRuleCookieInsrtHdrFld_Type.__name__ = "DisplayString"
_Layer7CurCfgHttpmodRuleCookieInsrtHdrFld_Object = MibTableColumn
layer7CurCfgHttpmodRuleCookieInsrtHdrFld = _Layer7CurCfgHttpmodRuleCookieInsrtHdrFld_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 9, 1, 11),
    _Layer7CurCfgHttpmodRuleCookieInsrtHdrFld_Type()
)
layer7CurCfgHttpmodRuleCookieInsrtHdrFld.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgHttpmodRuleCookieInsrtHdrFld.setStatus("current")


class _Layer7CurCfgHttpmodRuleCookieInsrtHdrVal_Type(DisplayString):
    """Custom type layer7CurCfgHttpmodRuleCookieInsrtHdrVal based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Layer7CurCfgHttpmodRuleCookieInsrtHdrVal_Type.__name__ = "DisplayString"
_Layer7CurCfgHttpmodRuleCookieInsrtHdrVal_Object = MibTableColumn
layer7CurCfgHttpmodRuleCookieInsrtHdrVal = _Layer7CurCfgHttpmodRuleCookieInsrtHdrVal_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 9, 1, 12),
    _Layer7CurCfgHttpmodRuleCookieInsrtHdrVal_Type()
)
layer7CurCfgHttpmodRuleCookieInsrtHdrVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgHttpmodRuleCookieInsrtHdrVal.setStatus("current")


class _Layer7CurCfgHttpmodRuleCookieInsrtCookey_Type(DisplayString):
    """Custom type layer7CurCfgHttpmodRuleCookieInsrtCookey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_Layer7CurCfgHttpmodRuleCookieInsrtCookey_Type.__name__ = "DisplayString"
_Layer7CurCfgHttpmodRuleCookieInsrtCookey_Object = MibTableColumn
layer7CurCfgHttpmodRuleCookieInsrtCookey = _Layer7CurCfgHttpmodRuleCookieInsrtCookey_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 9, 1, 13),
    _Layer7CurCfgHttpmodRuleCookieInsrtCookey_Type()
)
layer7CurCfgHttpmodRuleCookieInsrtCookey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgHttpmodRuleCookieInsrtCookey.setStatus("current")


class _Layer7CurCfgHttpmodRuleCookieInsrtCookieVal_Type(DisplayString):
    """Custom type layer7CurCfgHttpmodRuleCookieInsrtCookieVal based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_Layer7CurCfgHttpmodRuleCookieInsrtCookieVal_Type.__name__ = "DisplayString"
_Layer7CurCfgHttpmodRuleCookieInsrtCookieVal_Object = MibTableColumn
layer7CurCfgHttpmodRuleCookieInsrtCookieVal = _Layer7CurCfgHttpmodRuleCookieInsrtCookieVal_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 9, 1, 14),
    _Layer7CurCfgHttpmodRuleCookieInsrtCookieVal_Type()
)
layer7CurCfgHttpmodRuleCookieInsrtCookieVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgHttpmodRuleCookieInsrtCookieVal.setStatus("current")


class _Layer7CurCfgHttpmodRuleCookieInsrtFiletyp_Type(DisplayString):
    """Custom type layer7CurCfgHttpmodRuleCookieInsrtFiletyp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Layer7CurCfgHttpmodRuleCookieInsrtFiletyp_Type.__name__ = "DisplayString"
_Layer7CurCfgHttpmodRuleCookieInsrtFiletyp_Object = MibTableColumn
layer7CurCfgHttpmodRuleCookieInsrtFiletyp = _Layer7CurCfgHttpmodRuleCookieInsrtFiletyp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 9, 1, 15),
    _Layer7CurCfgHttpmodRuleCookieInsrtFiletyp_Type()
)
layer7CurCfgHttpmodRuleCookieInsrtFiletyp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgHttpmodRuleCookieInsrtFiletyp.setStatus("current")
_Layer7CurCfgHttpmodRuleCookieInsrtStatsCode_Type = Integer32
_Layer7CurCfgHttpmodRuleCookieInsrtStatsCode_Object = MibTableColumn
layer7CurCfgHttpmodRuleCookieInsrtStatsCode = _Layer7CurCfgHttpmodRuleCookieInsrtStatsCode_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 9, 1, 16),
    _Layer7CurCfgHttpmodRuleCookieInsrtStatsCode_Type()
)
layer7CurCfgHttpmodRuleCookieInsrtStatsCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgHttpmodRuleCookieInsrtStatsCode.setStatus("current")


class _Layer7CurCfgHttpmodRuleCookieInsrtStatsTxt_Type(DisplayString):
    """Custom type layer7CurCfgHttpmodRuleCookieInsrtStatsTxt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Layer7CurCfgHttpmodRuleCookieInsrtStatsTxt_Type.__name__ = "DisplayString"
_Layer7CurCfgHttpmodRuleCookieInsrtStatsTxt_Object = MibTableColumn
layer7CurCfgHttpmodRuleCookieInsrtStatsTxt = _Layer7CurCfgHttpmodRuleCookieInsrtStatsTxt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 9, 1, 17),
    _Layer7CurCfgHttpmodRuleCookieInsrtStatsTxt_Type()
)
layer7CurCfgHttpmodRuleCookieInsrtStatsTxt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgHttpmodRuleCookieInsrtStatsTxt.setStatus("current")


class _Layer7CurCfgHttpmodRuleCookieInsrtTxt_Type(DisplayString):
    """Custom type layer7CurCfgHttpmodRuleCookieInsrtTxt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Layer7CurCfgHttpmodRuleCookieInsrtTxt_Type.__name__ = "DisplayString"
_Layer7CurCfgHttpmodRuleCookieInsrtTxt_Object = MibTableColumn
layer7CurCfgHttpmodRuleCookieInsrtTxt = _Layer7CurCfgHttpmodRuleCookieInsrtTxt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 9, 1, 18),
    _Layer7CurCfgHttpmodRuleCookieInsrtTxt_Type()
)
layer7CurCfgHttpmodRuleCookieInsrtTxt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgHttpmodRuleCookieInsrtTxt.setStatus("current")


class _Layer7CurCfgHttpmodRuleCookieInsrtRegx_Type(DisplayString):
    """Custom type layer7CurCfgHttpmodRuleCookieInsrtRegx based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Layer7CurCfgHttpmodRuleCookieInsrtRegx_Type.__name__ = "DisplayString"
_Layer7CurCfgHttpmodRuleCookieInsrtRegx_Object = MibTableColumn
layer7CurCfgHttpmodRuleCookieInsrtRegx = _Layer7CurCfgHttpmodRuleCookieInsrtRegx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 9, 1, 19),
    _Layer7CurCfgHttpmodRuleCookieInsrtRegx_Type()
)
layer7CurCfgHttpmodRuleCookieInsrtRegx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgHttpmodRuleCookieInsrtRegx.setStatus("current")


class _Layer7CurCfgHttpmodRuleCookieReplcCookey_Type(DisplayString):
    """Custom type layer7CurCfgHttpmodRuleCookieReplcCookey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_Layer7CurCfgHttpmodRuleCookieReplcCookey_Type.__name__ = "DisplayString"
_Layer7CurCfgHttpmodRuleCookieReplcCookey_Object = MibTableColumn
layer7CurCfgHttpmodRuleCookieReplcCookey = _Layer7CurCfgHttpmodRuleCookieReplcCookey_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 9, 1, 20),
    _Layer7CurCfgHttpmodRuleCookieReplcCookey_Type()
)
layer7CurCfgHttpmodRuleCookieReplcCookey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgHttpmodRuleCookieReplcCookey.setStatus("current")


class _Layer7CurCfgHttpmodRuleCookieReplcVal_Type(DisplayString):
    """Custom type layer7CurCfgHttpmodRuleCookieReplcVal based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_Layer7CurCfgHttpmodRuleCookieReplcVal_Type.__name__ = "DisplayString"
_Layer7CurCfgHttpmodRuleCookieReplcVal_Object = MibTableColumn
layer7CurCfgHttpmodRuleCookieReplcVal = _Layer7CurCfgHttpmodRuleCookieReplcVal_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 9, 1, 21),
    _Layer7CurCfgHttpmodRuleCookieReplcVal_Type()
)
layer7CurCfgHttpmodRuleCookieReplcVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgHttpmodRuleCookieReplcVal.setStatus("current")


class _Layer7CurCfgHttpmodRuleCookieReplcNewKey_Type(DisplayString):
    """Custom type layer7CurCfgHttpmodRuleCookieReplcNewKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_Layer7CurCfgHttpmodRuleCookieReplcNewKey_Type.__name__ = "DisplayString"
_Layer7CurCfgHttpmodRuleCookieReplcNewKey_Object = MibTableColumn
layer7CurCfgHttpmodRuleCookieReplcNewKey = _Layer7CurCfgHttpmodRuleCookieReplcNewKey_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 9, 1, 22),
    _Layer7CurCfgHttpmodRuleCookieReplcNewKey_Type()
)
layer7CurCfgHttpmodRuleCookieReplcNewKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgHttpmodRuleCookieReplcNewKey.setStatus("current")


class _Layer7CurCfgHttpmodRuleCookieReplcNewVal_Type(DisplayString):
    """Custom type layer7CurCfgHttpmodRuleCookieReplcNewVal based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_Layer7CurCfgHttpmodRuleCookieReplcNewVal_Type.__name__ = "DisplayString"
_Layer7CurCfgHttpmodRuleCookieReplcNewVal_Object = MibTableColumn
layer7CurCfgHttpmodRuleCookieReplcNewVal = _Layer7CurCfgHttpmodRuleCookieReplcNewVal_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 9, 1, 23),
    _Layer7CurCfgHttpmodRuleCookieReplcNewVal_Type()
)
layer7CurCfgHttpmodRuleCookieReplcNewVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgHttpmodRuleCookieReplcNewVal.setStatus("current")


class _Layer7CurCfgHttpmodRuleCookieRemvCookey_Type(DisplayString):
    """Custom type layer7CurCfgHttpmodRuleCookieRemvCookey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_Layer7CurCfgHttpmodRuleCookieRemvCookey_Type.__name__ = "DisplayString"
_Layer7CurCfgHttpmodRuleCookieRemvCookey_Object = MibTableColumn
layer7CurCfgHttpmodRuleCookieRemvCookey = _Layer7CurCfgHttpmodRuleCookieRemvCookey_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 9, 1, 24),
    _Layer7CurCfgHttpmodRuleCookieRemvCookey_Type()
)
layer7CurCfgHttpmodRuleCookieRemvCookey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgHttpmodRuleCookieRemvCookey.setStatus("current")


class _Layer7CurCfgHttpmodRuleCookieRemvCookieVal_Type(DisplayString):
    """Custom type layer7CurCfgHttpmodRuleCookieRemvCookieVal based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_Layer7CurCfgHttpmodRuleCookieRemvCookieVal_Type.__name__ = "DisplayString"
_Layer7CurCfgHttpmodRuleCookieRemvCookieVal_Object = MibTableColumn
layer7CurCfgHttpmodRuleCookieRemvCookieVal = _Layer7CurCfgHttpmodRuleCookieRemvCookieVal_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 9, 1, 25),
    _Layer7CurCfgHttpmodRuleCookieRemvCookieVal_Type()
)
layer7CurCfgHttpmodRuleCookieRemvCookieVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgHttpmodRuleCookieRemvCookieVal.setStatus("current")
_Layer7NewCfgHttpmodRuleCookieTable_Object = MibTable
layer7NewCfgHttpmodRuleCookieTable = _Layer7NewCfgHttpmodRuleCookieTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 10)
)
if mibBuilder.loadTexts:
    layer7NewCfgHttpmodRuleCookieTable.setStatus("current")
_Layer7NewCfgHttpmodRuleCookieEntry_Object = MibTableRow
layer7NewCfgHttpmodRuleCookieEntry = _Layer7NewCfgHttpmodRuleCookieEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 10, 1)
)
layer7NewCfgHttpmodRuleCookieEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-LAYER7-MIB", "layer7NewCfgHttpmodRuleCookieListIdIndex"),
    (0, "ALTEON-CHEETAH-LAYER7-MIB", "layer7NewCfgHttpmodRuleCookieIndex"),
)
if mibBuilder.loadTexts:
    layer7NewCfgHttpmodRuleCookieEntry.setStatus("current")


class _Layer7NewCfgHttpmodRuleCookieListIdIndex_Type(DisplayString):
    """Custom type layer7NewCfgHttpmodRuleCookieListIdIndex based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Layer7NewCfgHttpmodRuleCookieListIdIndex_Type.__name__ = "DisplayString"
_Layer7NewCfgHttpmodRuleCookieListIdIndex_Object = MibTableColumn
layer7NewCfgHttpmodRuleCookieListIdIndex = _Layer7NewCfgHttpmodRuleCookieListIdIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 10, 1, 1),
    _Layer7NewCfgHttpmodRuleCookieListIdIndex_Type()
)
layer7NewCfgHttpmodRuleCookieListIdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7NewCfgHttpmodRuleCookieListIdIndex.setStatus("current")
_Layer7NewCfgHttpmodRuleCookieIndex_Type = Integer32
_Layer7NewCfgHttpmodRuleCookieIndex_Object = MibTableColumn
layer7NewCfgHttpmodRuleCookieIndex = _Layer7NewCfgHttpmodRuleCookieIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 10, 1, 2),
    _Layer7NewCfgHttpmodRuleCookieIndex_Type()
)
layer7NewCfgHttpmodRuleCookieIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7NewCfgHttpmodRuleCookieIndex.setStatus("current")


class _Layer7NewCfgHttpmodRuleCookieInsrtKey_Type(DisplayString):
    """Custom type layer7NewCfgHttpmodRuleCookieInsrtKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_Layer7NewCfgHttpmodRuleCookieInsrtKey_Type.__name__ = "DisplayString"
_Layer7NewCfgHttpmodRuleCookieInsrtKey_Object = MibTableColumn
layer7NewCfgHttpmodRuleCookieInsrtKey = _Layer7NewCfgHttpmodRuleCookieInsrtKey_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 10, 1, 3),
    _Layer7NewCfgHttpmodRuleCookieInsrtKey_Type()
)
layer7NewCfgHttpmodRuleCookieInsrtKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    layer7NewCfgHttpmodRuleCookieInsrtKey.setStatus("current")


class _Layer7NewCfgHttpmodRuleCookieInsrtVal_Type(DisplayString):
    """Custom type layer7NewCfgHttpmodRuleCookieInsrtVal based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_Layer7NewCfgHttpmodRuleCookieInsrtVal_Type.__name__ = "DisplayString"
_Layer7NewCfgHttpmodRuleCookieInsrtVal_Object = MibTableColumn
layer7NewCfgHttpmodRuleCookieInsrtVal = _Layer7NewCfgHttpmodRuleCookieInsrtVal_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 10, 1, 4),
    _Layer7NewCfgHttpmodRuleCookieInsrtVal_Type()
)
layer7NewCfgHttpmodRuleCookieInsrtVal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    layer7NewCfgHttpmodRuleCookieInsrtVal.setStatus("current")


class _Layer7NewCfgHttpmodRuleCookieInsrtPath_Type(DisplayString):
    """Custom type layer7NewCfgHttpmodRuleCookieInsrtPath based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Layer7NewCfgHttpmodRuleCookieInsrtPath_Type.__name__ = "DisplayString"
_Layer7NewCfgHttpmodRuleCookieInsrtPath_Object = MibTableColumn
layer7NewCfgHttpmodRuleCookieInsrtPath = _Layer7NewCfgHttpmodRuleCookieInsrtPath_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 10, 1, 5),
    _Layer7NewCfgHttpmodRuleCookieInsrtPath_Type()
)
layer7NewCfgHttpmodRuleCookieInsrtPath.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    layer7NewCfgHttpmodRuleCookieInsrtPath.setStatus("current")


class _Layer7NewCfgHttpmodRuleCookieInsrtDomn_Type(DisplayString):
    """Custom type layer7NewCfgHttpmodRuleCookieInsrtDomn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65),
    )


_Layer7NewCfgHttpmodRuleCookieInsrtDomn_Type.__name__ = "DisplayString"
_Layer7NewCfgHttpmodRuleCookieInsrtDomn_Object = MibTableColumn
layer7NewCfgHttpmodRuleCookieInsrtDomn = _Layer7NewCfgHttpmodRuleCookieInsrtDomn_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 10, 1, 6),
    _Layer7NewCfgHttpmodRuleCookieInsrtDomn_Type()
)
layer7NewCfgHttpmodRuleCookieInsrtDomn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    layer7NewCfgHttpmodRuleCookieInsrtDomn.setStatus("current")


class _Layer7NewCfgHttpmodRuleCookieInsrtExp_Type(DisplayString):
    """Custom type layer7NewCfgHttpmodRuleCookieInsrtExp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Layer7NewCfgHttpmodRuleCookieInsrtExp_Type.__name__ = "DisplayString"
_Layer7NewCfgHttpmodRuleCookieInsrtExp_Object = MibTableColumn
layer7NewCfgHttpmodRuleCookieInsrtExp = _Layer7NewCfgHttpmodRuleCookieInsrtExp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 10, 1, 7),
    _Layer7NewCfgHttpmodRuleCookieInsrtExp_Type()
)
layer7NewCfgHttpmodRuleCookieInsrtExp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    layer7NewCfgHttpmodRuleCookieInsrtExp.setStatus("current")


class _Layer7NewCfgHttpmodRuleCookieInsrtElem_Type(Integer32):
    """Custom type layer7NewCfgHttpmodRuleCookieInsrtElem based on Integer32"""
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
        *(("cookie", 3),
          ("filetype", 4),
          ("header", 2),
          ("none", 8),
          ("regex", 7),
          ("statusline", 5),
          ("text", 6),
          ("url", 1))
    )


_Layer7NewCfgHttpmodRuleCookieInsrtElem_Type.__name__ = "Integer32"
_Layer7NewCfgHttpmodRuleCookieInsrtElem_Object = MibTableColumn
layer7NewCfgHttpmodRuleCookieInsrtElem = _Layer7NewCfgHttpmodRuleCookieInsrtElem_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 10, 1, 8),
    _Layer7NewCfgHttpmodRuleCookieInsrtElem_Type()
)
layer7NewCfgHttpmodRuleCookieInsrtElem.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    layer7NewCfgHttpmodRuleCookieInsrtElem.setStatus("current")


class _Layer7NewCfgHttpmodRuleCookieInsrtUrlHost_Type(DisplayString):
    """Custom type layer7NewCfgHttpmodRuleCookieInsrtUrlHost based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Layer7NewCfgHttpmodRuleCookieInsrtUrlHost_Type.__name__ = "DisplayString"
_Layer7NewCfgHttpmodRuleCookieInsrtUrlHost_Object = MibTableColumn
layer7NewCfgHttpmodRuleCookieInsrtUrlHost = _Layer7NewCfgHttpmodRuleCookieInsrtUrlHost_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 10, 1, 9),
    _Layer7NewCfgHttpmodRuleCookieInsrtUrlHost_Type()
)
layer7NewCfgHttpmodRuleCookieInsrtUrlHost.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    layer7NewCfgHttpmodRuleCookieInsrtUrlHost.setStatus("current")


class _Layer7NewCfgHttpmodRuleCookieInsrtUrlPath_Type(DisplayString):
    """Custom type layer7NewCfgHttpmodRuleCookieInsrtUrlPath based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Layer7NewCfgHttpmodRuleCookieInsrtUrlPath_Type.__name__ = "DisplayString"
_Layer7NewCfgHttpmodRuleCookieInsrtUrlPath_Object = MibTableColumn
layer7NewCfgHttpmodRuleCookieInsrtUrlPath = _Layer7NewCfgHttpmodRuleCookieInsrtUrlPath_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 10, 1, 10),
    _Layer7NewCfgHttpmodRuleCookieInsrtUrlPath_Type()
)
layer7NewCfgHttpmodRuleCookieInsrtUrlPath.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    layer7NewCfgHttpmodRuleCookieInsrtUrlPath.setStatus("current")


class _Layer7NewCfgHttpmodRuleCookieInsrtHdrFld_Type(DisplayString):
    """Custom type layer7NewCfgHttpmodRuleCookieInsrtHdrFld based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Layer7NewCfgHttpmodRuleCookieInsrtHdrFld_Type.__name__ = "DisplayString"
_Layer7NewCfgHttpmodRuleCookieInsrtHdrFld_Object = MibTableColumn
layer7NewCfgHttpmodRuleCookieInsrtHdrFld = _Layer7NewCfgHttpmodRuleCookieInsrtHdrFld_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 10, 1, 11),
    _Layer7NewCfgHttpmodRuleCookieInsrtHdrFld_Type()
)
layer7NewCfgHttpmodRuleCookieInsrtHdrFld.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    layer7NewCfgHttpmodRuleCookieInsrtHdrFld.setStatus("current")


class _Layer7NewCfgHttpmodRuleCookieInsrtHdrVal_Type(DisplayString):
    """Custom type layer7NewCfgHttpmodRuleCookieInsrtHdrVal based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Layer7NewCfgHttpmodRuleCookieInsrtHdrVal_Type.__name__ = "DisplayString"
_Layer7NewCfgHttpmodRuleCookieInsrtHdrVal_Object = MibTableColumn
layer7NewCfgHttpmodRuleCookieInsrtHdrVal = _Layer7NewCfgHttpmodRuleCookieInsrtHdrVal_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 10, 1, 12),
    _Layer7NewCfgHttpmodRuleCookieInsrtHdrVal_Type()
)
layer7NewCfgHttpmodRuleCookieInsrtHdrVal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    layer7NewCfgHttpmodRuleCookieInsrtHdrVal.setStatus("current")


class _Layer7NewCfgHttpmodRuleCookieInsrtCookey_Type(DisplayString):
    """Custom type layer7NewCfgHttpmodRuleCookieInsrtCookey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_Layer7NewCfgHttpmodRuleCookieInsrtCookey_Type.__name__ = "DisplayString"
_Layer7NewCfgHttpmodRuleCookieInsrtCookey_Object = MibTableColumn
layer7NewCfgHttpmodRuleCookieInsrtCookey = _Layer7NewCfgHttpmodRuleCookieInsrtCookey_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 10, 1, 13),
    _Layer7NewCfgHttpmodRuleCookieInsrtCookey_Type()
)
layer7NewCfgHttpmodRuleCookieInsrtCookey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    layer7NewCfgHttpmodRuleCookieInsrtCookey.setStatus("current")


class _Layer7NewCfgHttpmodRuleCookieInsrtCookieVal_Type(DisplayString):
    """Custom type layer7NewCfgHttpmodRuleCookieInsrtCookieVal based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_Layer7NewCfgHttpmodRuleCookieInsrtCookieVal_Type.__name__ = "DisplayString"
_Layer7NewCfgHttpmodRuleCookieInsrtCookieVal_Object = MibTableColumn
layer7NewCfgHttpmodRuleCookieInsrtCookieVal = _Layer7NewCfgHttpmodRuleCookieInsrtCookieVal_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 10, 1, 14),
    _Layer7NewCfgHttpmodRuleCookieInsrtCookieVal_Type()
)
layer7NewCfgHttpmodRuleCookieInsrtCookieVal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    layer7NewCfgHttpmodRuleCookieInsrtCookieVal.setStatus("current")


class _Layer7NewCfgHttpmodRuleCookieInsrtFiletyp_Type(DisplayString):
    """Custom type layer7NewCfgHttpmodRuleCookieInsrtFiletyp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Layer7NewCfgHttpmodRuleCookieInsrtFiletyp_Type.__name__ = "DisplayString"
_Layer7NewCfgHttpmodRuleCookieInsrtFiletyp_Object = MibTableColumn
layer7NewCfgHttpmodRuleCookieInsrtFiletyp = _Layer7NewCfgHttpmodRuleCookieInsrtFiletyp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 10, 1, 15),
    _Layer7NewCfgHttpmodRuleCookieInsrtFiletyp_Type()
)
layer7NewCfgHttpmodRuleCookieInsrtFiletyp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    layer7NewCfgHttpmodRuleCookieInsrtFiletyp.setStatus("current")
_Layer7NewCfgHttpmodRuleCookieInsrtStatsCode_Type = Integer32
_Layer7NewCfgHttpmodRuleCookieInsrtStatsCode_Object = MibTableColumn
layer7NewCfgHttpmodRuleCookieInsrtStatsCode = _Layer7NewCfgHttpmodRuleCookieInsrtStatsCode_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 10, 1, 16),
    _Layer7NewCfgHttpmodRuleCookieInsrtStatsCode_Type()
)
layer7NewCfgHttpmodRuleCookieInsrtStatsCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    layer7NewCfgHttpmodRuleCookieInsrtStatsCode.setStatus("current")


class _Layer7NewCfgHttpmodRuleCookieInsrtStatsTxt_Type(DisplayString):
    """Custom type layer7NewCfgHttpmodRuleCookieInsrtStatsTxt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Layer7NewCfgHttpmodRuleCookieInsrtStatsTxt_Type.__name__ = "DisplayString"
_Layer7NewCfgHttpmodRuleCookieInsrtStatsTxt_Object = MibTableColumn
layer7NewCfgHttpmodRuleCookieInsrtStatsTxt = _Layer7NewCfgHttpmodRuleCookieInsrtStatsTxt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 10, 1, 17),
    _Layer7NewCfgHttpmodRuleCookieInsrtStatsTxt_Type()
)
layer7NewCfgHttpmodRuleCookieInsrtStatsTxt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    layer7NewCfgHttpmodRuleCookieInsrtStatsTxt.setStatus("current")


class _Layer7NewCfgHttpmodRuleCookieInsrtTxt_Type(DisplayString):
    """Custom type layer7NewCfgHttpmodRuleCookieInsrtTxt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Layer7NewCfgHttpmodRuleCookieInsrtTxt_Type.__name__ = "DisplayString"
_Layer7NewCfgHttpmodRuleCookieInsrtTxt_Object = MibTableColumn
layer7NewCfgHttpmodRuleCookieInsrtTxt = _Layer7NewCfgHttpmodRuleCookieInsrtTxt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 10, 1, 18),
    _Layer7NewCfgHttpmodRuleCookieInsrtTxt_Type()
)
layer7NewCfgHttpmodRuleCookieInsrtTxt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    layer7NewCfgHttpmodRuleCookieInsrtTxt.setStatus("current")


class _Layer7NewCfgHttpmodRuleCookieInsrtRegx_Type(DisplayString):
    """Custom type layer7NewCfgHttpmodRuleCookieInsrtRegx based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Layer7NewCfgHttpmodRuleCookieInsrtRegx_Type.__name__ = "DisplayString"
_Layer7NewCfgHttpmodRuleCookieInsrtRegx_Object = MibTableColumn
layer7NewCfgHttpmodRuleCookieInsrtRegx = _Layer7NewCfgHttpmodRuleCookieInsrtRegx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 10, 1, 19),
    _Layer7NewCfgHttpmodRuleCookieInsrtRegx_Type()
)
layer7NewCfgHttpmodRuleCookieInsrtRegx.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    layer7NewCfgHttpmodRuleCookieInsrtRegx.setStatus("current")


class _Layer7NewCfgHttpmodRuleCookieReplcCookey_Type(DisplayString):
    """Custom type layer7NewCfgHttpmodRuleCookieReplcCookey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_Layer7NewCfgHttpmodRuleCookieReplcCookey_Type.__name__ = "DisplayString"
_Layer7NewCfgHttpmodRuleCookieReplcCookey_Object = MibTableColumn
layer7NewCfgHttpmodRuleCookieReplcCookey = _Layer7NewCfgHttpmodRuleCookieReplcCookey_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 10, 1, 20),
    _Layer7NewCfgHttpmodRuleCookieReplcCookey_Type()
)
layer7NewCfgHttpmodRuleCookieReplcCookey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    layer7NewCfgHttpmodRuleCookieReplcCookey.setStatus("current")


class _Layer7NewCfgHttpmodRuleCookieReplcVal_Type(DisplayString):
    """Custom type layer7NewCfgHttpmodRuleCookieReplcVal based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_Layer7NewCfgHttpmodRuleCookieReplcVal_Type.__name__ = "DisplayString"
_Layer7NewCfgHttpmodRuleCookieReplcVal_Object = MibTableColumn
layer7NewCfgHttpmodRuleCookieReplcVal = _Layer7NewCfgHttpmodRuleCookieReplcVal_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 10, 1, 21),
    _Layer7NewCfgHttpmodRuleCookieReplcVal_Type()
)
layer7NewCfgHttpmodRuleCookieReplcVal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    layer7NewCfgHttpmodRuleCookieReplcVal.setStatus("current")


class _Layer7NewCfgHttpmodRuleCookieReplcNewKey_Type(DisplayString):
    """Custom type layer7NewCfgHttpmodRuleCookieReplcNewKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_Layer7NewCfgHttpmodRuleCookieReplcNewKey_Type.__name__ = "DisplayString"
_Layer7NewCfgHttpmodRuleCookieReplcNewKey_Object = MibTableColumn
layer7NewCfgHttpmodRuleCookieReplcNewKey = _Layer7NewCfgHttpmodRuleCookieReplcNewKey_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 10, 1, 22),
    _Layer7NewCfgHttpmodRuleCookieReplcNewKey_Type()
)
layer7NewCfgHttpmodRuleCookieReplcNewKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    layer7NewCfgHttpmodRuleCookieReplcNewKey.setStatus("current")


class _Layer7NewCfgHttpmodRuleCookieReplcNewVal_Type(DisplayString):
    """Custom type layer7NewCfgHttpmodRuleCookieReplcNewVal based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_Layer7NewCfgHttpmodRuleCookieReplcNewVal_Type.__name__ = "DisplayString"
_Layer7NewCfgHttpmodRuleCookieReplcNewVal_Object = MibTableColumn
layer7NewCfgHttpmodRuleCookieReplcNewVal = _Layer7NewCfgHttpmodRuleCookieReplcNewVal_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 10, 1, 23),
    _Layer7NewCfgHttpmodRuleCookieReplcNewVal_Type()
)
layer7NewCfgHttpmodRuleCookieReplcNewVal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    layer7NewCfgHttpmodRuleCookieReplcNewVal.setStatus("current")


class _Layer7NewCfgHttpmodRuleCookieRemvCookey_Type(DisplayString):
    """Custom type layer7NewCfgHttpmodRuleCookieRemvCookey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_Layer7NewCfgHttpmodRuleCookieRemvCookey_Type.__name__ = "DisplayString"
_Layer7NewCfgHttpmodRuleCookieRemvCookey_Object = MibTableColumn
layer7NewCfgHttpmodRuleCookieRemvCookey = _Layer7NewCfgHttpmodRuleCookieRemvCookey_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 10, 1, 24),
    _Layer7NewCfgHttpmodRuleCookieRemvCookey_Type()
)
layer7NewCfgHttpmodRuleCookieRemvCookey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    layer7NewCfgHttpmodRuleCookieRemvCookey.setStatus("current")


class _Layer7NewCfgHttpmodRuleCookieRemvCookieVal_Type(DisplayString):
    """Custom type layer7NewCfgHttpmodRuleCookieRemvCookieVal based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_Layer7NewCfgHttpmodRuleCookieRemvCookieVal_Type.__name__ = "DisplayString"
_Layer7NewCfgHttpmodRuleCookieRemvCookieVal_Object = MibTableColumn
layer7NewCfgHttpmodRuleCookieRemvCookieVal = _Layer7NewCfgHttpmodRuleCookieRemvCookieVal_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 10, 1, 25),
    _Layer7NewCfgHttpmodRuleCookieRemvCookieVal_Type()
)
layer7NewCfgHttpmodRuleCookieRemvCookieVal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    layer7NewCfgHttpmodRuleCookieRemvCookieVal.setStatus("current")
_Layer7CurCfgHttpmodRuleFileLineTextTable_Object = MibTable
layer7CurCfgHttpmodRuleFileLineTextTable = _Layer7CurCfgHttpmodRuleFileLineTextTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 11)
)
if mibBuilder.loadTexts:
    layer7CurCfgHttpmodRuleFileLineTextTable.setStatus("current")
_Layer7CurCfgHttpmodRuleFileLineTextEntry_Object = MibTableRow
layer7CurCfgHttpmodRuleFileLineTextEntry = _Layer7CurCfgHttpmodRuleFileLineTextEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 11, 1)
)
layer7CurCfgHttpmodRuleFileLineTextEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-LAYER7-MIB", "layer7CurCfgHttpmodRuleFileLineTextListIdIndex"),
    (0, "ALTEON-CHEETAH-LAYER7-MIB", "layer7CurCfgHttpmodRuleFileLineTextIndex"),
)
if mibBuilder.loadTexts:
    layer7CurCfgHttpmodRuleFileLineTextEntry.setStatus("current")


class _Layer7CurCfgHttpmodRuleFileLineTextListIdIndex_Type(DisplayString):
    """Custom type layer7CurCfgHttpmodRuleFileLineTextListIdIndex based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Layer7CurCfgHttpmodRuleFileLineTextListIdIndex_Type.__name__ = "DisplayString"
_Layer7CurCfgHttpmodRuleFileLineTextListIdIndex_Object = MibTableColumn
layer7CurCfgHttpmodRuleFileLineTextListIdIndex = _Layer7CurCfgHttpmodRuleFileLineTextListIdIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 11, 1, 1),
    _Layer7CurCfgHttpmodRuleFileLineTextListIdIndex_Type()
)
layer7CurCfgHttpmodRuleFileLineTextListIdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgHttpmodRuleFileLineTextListIdIndex.setStatus("current")
_Layer7CurCfgHttpmodRuleFileLineTextIndex_Type = Integer32
_Layer7CurCfgHttpmodRuleFileLineTextIndex_Object = MibTableColumn
layer7CurCfgHttpmodRuleFileLineTextIndex = _Layer7CurCfgHttpmodRuleFileLineTextIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 11, 1, 2),
    _Layer7CurCfgHttpmodRuleFileLineTextIndex_Type()
)
layer7CurCfgHttpmodRuleFileLineTextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgHttpmodRuleFileLineTextIndex.setStatus("current")


class _Layer7CurCfgHttpmodRuleFileTypRep_Type(DisplayString):
    """Custom type layer7CurCfgHttpmodRuleFileTypRep based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Layer7CurCfgHttpmodRuleFileTypRep_Type.__name__ = "DisplayString"
_Layer7CurCfgHttpmodRuleFileTypRep_Object = MibTableColumn
layer7CurCfgHttpmodRuleFileTypRep = _Layer7CurCfgHttpmodRuleFileTypRep_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 11, 1, 3),
    _Layer7CurCfgHttpmodRuleFileTypRep_Type()
)
layer7CurCfgHttpmodRuleFileTypRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgHttpmodRuleFileTypRep.setStatus("current")


class _Layer7CurCfgHttpmodRuleFileTypNew_Type(DisplayString):
    """Custom type layer7CurCfgHttpmodRuleFileTypNew based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Layer7CurCfgHttpmodRuleFileTypNew_Type.__name__ = "DisplayString"
_Layer7CurCfgHttpmodRuleFileTypNew_Object = MibTableColumn
layer7CurCfgHttpmodRuleFileTypNew = _Layer7CurCfgHttpmodRuleFileTypNew_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 11, 1, 4),
    _Layer7CurCfgHttpmodRuleFileTypNew_Type()
)
layer7CurCfgHttpmodRuleFileTypNew.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgHttpmodRuleFileTypNew.setStatus("current")
_Layer7CurCfgHttpmodRuleStatlineCode_Type = Integer32
_Layer7CurCfgHttpmodRuleStatlineCode_Object = MibTableColumn
layer7CurCfgHttpmodRuleStatlineCode = _Layer7CurCfgHttpmodRuleStatlineCode_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 11, 1, 5),
    _Layer7CurCfgHttpmodRuleStatlineCode_Type()
)
layer7CurCfgHttpmodRuleStatlineCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgHttpmodRuleStatlineCode.setStatus("current")


class _Layer7CurCfgHttpmodRuleStatlineTxt_Type(DisplayString):
    """Custom type layer7CurCfgHttpmodRuleStatlineTxt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Layer7CurCfgHttpmodRuleStatlineTxt_Type.__name__ = "DisplayString"
_Layer7CurCfgHttpmodRuleStatlineTxt_Object = MibTableColumn
layer7CurCfgHttpmodRuleStatlineTxt = _Layer7CurCfgHttpmodRuleStatlineTxt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 11, 1, 6),
    _Layer7CurCfgHttpmodRuleStatlineTxt_Type()
)
layer7CurCfgHttpmodRuleStatlineTxt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgHttpmodRuleStatlineTxt.setStatus("current")
_Layer7CurCfgHttpmodRuleStatlineNewCode_Type = Integer32
_Layer7CurCfgHttpmodRuleStatlineNewCode_Object = MibTableColumn
layer7CurCfgHttpmodRuleStatlineNewCode = _Layer7CurCfgHttpmodRuleStatlineNewCode_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 11, 1, 7),
    _Layer7CurCfgHttpmodRuleStatlineNewCode_Type()
)
layer7CurCfgHttpmodRuleStatlineNewCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgHttpmodRuleStatlineNewCode.setStatus("current")


class _Layer7CurCfgHttpmodRuleStatlineNewTxt_Type(DisplayString):
    """Custom type layer7CurCfgHttpmodRuleStatlineNewTxt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Layer7CurCfgHttpmodRuleStatlineNewTxt_Type.__name__ = "DisplayString"
_Layer7CurCfgHttpmodRuleStatlineNewTxt_Object = MibTableColumn
layer7CurCfgHttpmodRuleStatlineNewTxt = _Layer7CurCfgHttpmodRuleStatlineNewTxt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 11, 1, 8),
    _Layer7CurCfgHttpmodRuleStatlineNewTxt_Type()
)
layer7CurCfgHttpmodRuleStatlineNewTxt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgHttpmodRuleStatlineNewTxt.setStatus("current")


class _Layer7CurCfgHttpmodRuleTextReplace_Type(DisplayString):
    """Custom type layer7CurCfgHttpmodRuleTextReplace based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Layer7CurCfgHttpmodRuleTextReplace_Type.__name__ = "DisplayString"
_Layer7CurCfgHttpmodRuleTextReplace_Object = MibTableColumn
layer7CurCfgHttpmodRuleTextReplace = _Layer7CurCfgHttpmodRuleTextReplace_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 11, 1, 9),
    _Layer7CurCfgHttpmodRuleTextReplace_Type()
)
layer7CurCfgHttpmodRuleTextReplace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgHttpmodRuleTextReplace.setStatus("current")


class _Layer7CurCfgHttpmodRuleTextNewText_Type(DisplayString):
    """Custom type layer7CurCfgHttpmodRuleTextNewText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Layer7CurCfgHttpmodRuleTextNewText_Type.__name__ = "DisplayString"
_Layer7CurCfgHttpmodRuleTextNewText_Object = MibTableColumn
layer7CurCfgHttpmodRuleTextNewText = _Layer7CurCfgHttpmodRuleTextNewText_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 11, 1, 10),
    _Layer7CurCfgHttpmodRuleTextNewText_Type()
)
layer7CurCfgHttpmodRuleTextNewText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgHttpmodRuleTextNewText.setStatus("current")


class _Layer7CurCfgHttpmodRuleTextRemove_Type(DisplayString):
    """Custom type layer7CurCfgHttpmodRuleTextRemove based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Layer7CurCfgHttpmodRuleTextRemove_Type.__name__ = "DisplayString"
_Layer7CurCfgHttpmodRuleTextRemove_Object = MibTableColumn
layer7CurCfgHttpmodRuleTextRemove = _Layer7CurCfgHttpmodRuleTextRemove_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 11, 1, 11),
    _Layer7CurCfgHttpmodRuleTextRemove_Type()
)
layer7CurCfgHttpmodRuleTextRemove.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgHttpmodRuleTextRemove.setStatus("current")
_Layer7NewCfgHttpmodRuleFileLineTextTable_Object = MibTable
layer7NewCfgHttpmodRuleFileLineTextTable = _Layer7NewCfgHttpmodRuleFileLineTextTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 12)
)
if mibBuilder.loadTexts:
    layer7NewCfgHttpmodRuleFileLineTextTable.setStatus("current")
_Layer7NewCfgHttpmodRuleFileLineTextEntry_Object = MibTableRow
layer7NewCfgHttpmodRuleFileLineTextEntry = _Layer7NewCfgHttpmodRuleFileLineTextEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 12, 1)
)
layer7NewCfgHttpmodRuleFileLineTextEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-LAYER7-MIB", "layer7NewCfgHttpmodRuleFileLineTextListIdIndex"),
    (0, "ALTEON-CHEETAH-LAYER7-MIB", "layer7NewCfgHttpmodRuleFileLineTextIndex"),
)
if mibBuilder.loadTexts:
    layer7NewCfgHttpmodRuleFileLineTextEntry.setStatus("current")


class _Layer7NewCfgHttpmodRuleFileLineTextListIdIndex_Type(DisplayString):
    """Custom type layer7NewCfgHttpmodRuleFileLineTextListIdIndex based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Layer7NewCfgHttpmodRuleFileLineTextListIdIndex_Type.__name__ = "DisplayString"
_Layer7NewCfgHttpmodRuleFileLineTextListIdIndex_Object = MibTableColumn
layer7NewCfgHttpmodRuleFileLineTextListIdIndex = _Layer7NewCfgHttpmodRuleFileLineTextListIdIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 12, 1, 1),
    _Layer7NewCfgHttpmodRuleFileLineTextListIdIndex_Type()
)
layer7NewCfgHttpmodRuleFileLineTextListIdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7NewCfgHttpmodRuleFileLineTextListIdIndex.setStatus("current")
_Layer7NewCfgHttpmodRuleFileLineTextIndex_Type = Integer32
_Layer7NewCfgHttpmodRuleFileLineTextIndex_Object = MibTableColumn
layer7NewCfgHttpmodRuleFileLineTextIndex = _Layer7NewCfgHttpmodRuleFileLineTextIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 12, 1, 2),
    _Layer7NewCfgHttpmodRuleFileLineTextIndex_Type()
)
layer7NewCfgHttpmodRuleFileLineTextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7NewCfgHttpmodRuleFileLineTextIndex.setStatus("current")


class _Layer7NewCfgHttpmodRuleFileTypRep_Type(DisplayString):
    """Custom type layer7NewCfgHttpmodRuleFileTypRep based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Layer7NewCfgHttpmodRuleFileTypRep_Type.__name__ = "DisplayString"
_Layer7NewCfgHttpmodRuleFileTypRep_Object = MibTableColumn
layer7NewCfgHttpmodRuleFileTypRep = _Layer7NewCfgHttpmodRuleFileTypRep_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 12, 1, 3),
    _Layer7NewCfgHttpmodRuleFileTypRep_Type()
)
layer7NewCfgHttpmodRuleFileTypRep.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    layer7NewCfgHttpmodRuleFileTypRep.setStatus("current")


class _Layer7NewCfgHttpmodRuleFileTypNew_Type(DisplayString):
    """Custom type layer7NewCfgHttpmodRuleFileTypNew based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Layer7NewCfgHttpmodRuleFileTypNew_Type.__name__ = "DisplayString"
_Layer7NewCfgHttpmodRuleFileTypNew_Object = MibTableColumn
layer7NewCfgHttpmodRuleFileTypNew = _Layer7NewCfgHttpmodRuleFileTypNew_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 12, 1, 4),
    _Layer7NewCfgHttpmodRuleFileTypNew_Type()
)
layer7NewCfgHttpmodRuleFileTypNew.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    layer7NewCfgHttpmodRuleFileTypNew.setStatus("current")
_Layer7NewCfgHttpmodRuleStatlineCode_Type = Integer32
_Layer7NewCfgHttpmodRuleStatlineCode_Object = MibTableColumn
layer7NewCfgHttpmodRuleStatlineCode = _Layer7NewCfgHttpmodRuleStatlineCode_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 12, 1, 5),
    _Layer7NewCfgHttpmodRuleStatlineCode_Type()
)
layer7NewCfgHttpmodRuleStatlineCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    layer7NewCfgHttpmodRuleStatlineCode.setStatus("current")


class _Layer7NewCfgHttpmodRuleStatlineTxt_Type(DisplayString):
    """Custom type layer7NewCfgHttpmodRuleStatlineTxt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Layer7NewCfgHttpmodRuleStatlineTxt_Type.__name__ = "DisplayString"
_Layer7NewCfgHttpmodRuleStatlineTxt_Object = MibTableColumn
layer7NewCfgHttpmodRuleStatlineTxt = _Layer7NewCfgHttpmodRuleStatlineTxt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 12, 1, 6),
    _Layer7NewCfgHttpmodRuleStatlineTxt_Type()
)
layer7NewCfgHttpmodRuleStatlineTxt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    layer7NewCfgHttpmodRuleStatlineTxt.setStatus("current")
_Layer7NewCfgHttpmodRuleStatlineNewCode_Type = Integer32
_Layer7NewCfgHttpmodRuleStatlineNewCode_Object = MibTableColumn
layer7NewCfgHttpmodRuleStatlineNewCode = _Layer7NewCfgHttpmodRuleStatlineNewCode_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 12, 1, 7),
    _Layer7NewCfgHttpmodRuleStatlineNewCode_Type()
)
layer7NewCfgHttpmodRuleStatlineNewCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    layer7NewCfgHttpmodRuleStatlineNewCode.setStatus("current")


class _Layer7NewCfgHttpmodRuleStatlineNewTxt_Type(DisplayString):
    """Custom type layer7NewCfgHttpmodRuleStatlineNewTxt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Layer7NewCfgHttpmodRuleStatlineNewTxt_Type.__name__ = "DisplayString"
_Layer7NewCfgHttpmodRuleStatlineNewTxt_Object = MibTableColumn
layer7NewCfgHttpmodRuleStatlineNewTxt = _Layer7NewCfgHttpmodRuleStatlineNewTxt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 12, 1, 8),
    _Layer7NewCfgHttpmodRuleStatlineNewTxt_Type()
)
layer7NewCfgHttpmodRuleStatlineNewTxt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    layer7NewCfgHttpmodRuleStatlineNewTxt.setStatus("current")


class _Layer7NewCfgHttpmodRuleTextReplace_Type(DisplayString):
    """Custom type layer7NewCfgHttpmodRuleTextReplace based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Layer7NewCfgHttpmodRuleTextReplace_Type.__name__ = "DisplayString"
_Layer7NewCfgHttpmodRuleTextReplace_Object = MibTableColumn
layer7NewCfgHttpmodRuleTextReplace = _Layer7NewCfgHttpmodRuleTextReplace_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 12, 1, 9),
    _Layer7NewCfgHttpmodRuleTextReplace_Type()
)
layer7NewCfgHttpmodRuleTextReplace.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    layer7NewCfgHttpmodRuleTextReplace.setStatus("current")


class _Layer7NewCfgHttpmodRuleTextNewText_Type(DisplayString):
    """Custom type layer7NewCfgHttpmodRuleTextNewText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Layer7NewCfgHttpmodRuleTextNewText_Type.__name__ = "DisplayString"
_Layer7NewCfgHttpmodRuleTextNewText_Object = MibTableColumn
layer7NewCfgHttpmodRuleTextNewText = _Layer7NewCfgHttpmodRuleTextNewText_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 12, 1, 10),
    _Layer7NewCfgHttpmodRuleTextNewText_Type()
)
layer7NewCfgHttpmodRuleTextNewText.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    layer7NewCfgHttpmodRuleTextNewText.setStatus("current")


class _Layer7NewCfgHttpmodRuleTextRemove_Type(DisplayString):
    """Custom type layer7NewCfgHttpmodRuleTextRemove based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Layer7NewCfgHttpmodRuleTextRemove_Type.__name__ = "DisplayString"
_Layer7NewCfgHttpmodRuleTextRemove_Object = MibTableColumn
layer7NewCfgHttpmodRuleTextRemove = _Layer7NewCfgHttpmodRuleTextRemove_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 4, 12, 1, 11),
    _Layer7NewCfgHttpmodRuleTextRemove_Type()
)
layer7NewCfgHttpmodRuleTextRemove.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    layer7NewCfgHttpmodRuleTextRemove.setStatus("current")
_RuleCfg_ObjectIdentity = ObjectIdentity
ruleCfg = _RuleCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 5)
)
_SlbCurCfgSipUdpRuleTable_Object = MibTable
slbCurCfgSipUdpRuleTable = _SlbCurCfgSipUdpRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 5, 1)
)
if mibBuilder.loadTexts:
    slbCurCfgSipUdpRuleTable.setStatus("current")
_SlbCurCfgSipUdpRuleTableEntry_Object = MibTableRow
slbCurCfgSipUdpRuleTableEntry = _SlbCurCfgSipUdpRuleTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 5, 1, 1)
)
slbCurCfgSipUdpRuleTableEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-LAYER7-MIB", "slbCurCfgSipUdpRuleIndex"),
)
if mibBuilder.loadTexts:
    slbCurCfgSipUdpRuleTableEntry.setStatus("current")
_SlbCurCfgSipUdpRuleIndex_Type = Integer32
_SlbCurCfgSipUdpRuleIndex_Object = MibTableColumn
slbCurCfgSipUdpRuleIndex = _SlbCurCfgSipUdpRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 5, 1, 1, 1),
    _SlbCurCfgSipUdpRuleIndex_Type()
)
slbCurCfgSipUdpRuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgSipUdpRuleIndex.setStatus("current")


class _SlbCurCfgSipUdpRuleHdrFld_Type(Integer32):
    """Custom type slbCurCfgSipUdpRuleHdrFld based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("callid", 1),
          ("contact", 2),
          ("contentlen", 3),
          ("cseq", 4),
          ("expires", 5),
          ("from", 6),
          ("method", 11),
          ("none", 0),
          ("replyto", 7),
          ("reqline", 10),
          ("sdpcontent", 12),
          ("to", 8),
          ("via", 9))
    )


_SlbCurCfgSipUdpRuleHdrFld_Type.__name__ = "Integer32"
_SlbCurCfgSipUdpRuleHdrFld_Object = MibTableColumn
slbCurCfgSipUdpRuleHdrFld = _SlbCurCfgSipUdpRuleHdrFld_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 5, 1, 1, 2),
    _SlbCurCfgSipUdpRuleHdrFld_Type()
)
slbCurCfgSipUdpRuleHdrFld.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgSipUdpRuleHdrFld.setStatus("current")


class _SlbCurCfgSipUdpRuleContent_Type(DisplayString):
    """Custom type slbCurCfgSipUdpRuleContent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_SlbCurCfgSipUdpRuleContent_Type.__name__ = "DisplayString"
_SlbCurCfgSipUdpRuleContent_Object = MibTableColumn
slbCurCfgSipUdpRuleContent = _SlbCurCfgSipUdpRuleContent_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 5, 1, 1, 3),
    _SlbCurCfgSipUdpRuleContent_Type()
)
slbCurCfgSipUdpRuleContent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgSipUdpRuleContent.setStatus("current")


class _SlbCurCfgSipUdpRuleContract_Type(Integer32):
    """Custom type slbCurCfgSipUdpRuleContract based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_SlbCurCfgSipUdpRuleContract_Type.__name__ = "Integer32"
_SlbCurCfgSipUdpRuleContract_Object = MibTableColumn
slbCurCfgSipUdpRuleContract = _SlbCurCfgSipUdpRuleContract_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 5, 1, 1, 4),
    _SlbCurCfgSipUdpRuleContract_Type()
)
slbCurCfgSipUdpRuleContract.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgSipUdpRuleContract.setStatus("current")


class _SlbCurCfgSipUdpRuleMsg_Type(DisplayString):
    """Custom type slbCurCfgSipUdpRuleMsg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_SlbCurCfgSipUdpRuleMsg_Type.__name__ = "DisplayString"
_SlbCurCfgSipUdpRuleMsg_Object = MibTableColumn
slbCurCfgSipUdpRuleMsg = _SlbCurCfgSipUdpRuleMsg_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 5, 1, 1, 5),
    _SlbCurCfgSipUdpRuleMsg_Type()
)
slbCurCfgSipUdpRuleMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgSipUdpRuleMsg.setStatus("current")


class _SlbCurCfgSipUdpRuleSeverity_Type(Integer32):
    """Custom type slbCurCfgSipUdpRuleSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_SlbCurCfgSipUdpRuleSeverity_Type.__name__ = "Integer32"
_SlbCurCfgSipUdpRuleSeverity_Object = MibTableColumn
slbCurCfgSipUdpRuleSeverity = _SlbCurCfgSipUdpRuleSeverity_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 5, 1, 1, 6),
    _SlbCurCfgSipUdpRuleSeverity_Type()
)
slbCurCfgSipUdpRuleSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgSipUdpRuleSeverity.setStatus("current")


class _SlbCurCfgSipUdpRuleAdd_Type(DisplayString):
    """Custom type slbCurCfgSipUdpRuleAdd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SlbCurCfgSipUdpRuleAdd_Type.__name__ = "DisplayString"
_SlbCurCfgSipUdpRuleAdd_Object = MibTableColumn
slbCurCfgSipUdpRuleAdd = _SlbCurCfgSipUdpRuleAdd_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 5, 1, 1, 7),
    _SlbCurCfgSipUdpRuleAdd_Type()
)
slbCurCfgSipUdpRuleAdd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgSipUdpRuleAdd.setStatus("current")


class _SlbCurCfgSipUdpRuleState_Type(Integer32):
    """Custom type slbCurCfgSipUdpRuleState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SlbCurCfgSipUdpRuleState_Type.__name__ = "Integer32"
_SlbCurCfgSipUdpRuleState_Object = MibTableColumn
slbCurCfgSipUdpRuleState = _SlbCurCfgSipUdpRuleState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 5, 1, 1, 8),
    _SlbCurCfgSipUdpRuleState_Type()
)
slbCurCfgSipUdpRuleState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgSipUdpRuleState.setStatus("current")
_SlbCurCfgSipUdpRuleBmap_Type = OctetString
_SlbCurCfgSipUdpRuleBmap_Object = MibTableColumn
slbCurCfgSipUdpRuleBmap = _SlbCurCfgSipUdpRuleBmap_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 5, 1, 1, 9),
    _SlbCurCfgSipUdpRuleBmap_Type()
)
slbCurCfgSipUdpRuleBmap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgSipUdpRuleBmap.setStatus("current")
_SlbNewCfgSipUdpRuleTable_Object = MibTable
slbNewCfgSipUdpRuleTable = _SlbNewCfgSipUdpRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 5, 2)
)
if mibBuilder.loadTexts:
    slbNewCfgSipUdpRuleTable.setStatus("current")
_SlbNewCfgSipUdpRuleTableEntry_Object = MibTableRow
slbNewCfgSipUdpRuleTableEntry = _SlbNewCfgSipUdpRuleTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 5, 2, 1)
)
slbNewCfgSipUdpRuleTableEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-LAYER7-MIB", "slbNewCfgSipUdpRuleIndex"),
)
if mibBuilder.loadTexts:
    slbNewCfgSipUdpRuleTableEntry.setStatus("current")
_SlbNewCfgSipUdpRuleIndex_Type = Integer32
_SlbNewCfgSipUdpRuleIndex_Object = MibTableColumn
slbNewCfgSipUdpRuleIndex = _SlbNewCfgSipUdpRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 5, 2, 1, 1),
    _SlbNewCfgSipUdpRuleIndex_Type()
)
slbNewCfgSipUdpRuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbNewCfgSipUdpRuleIndex.setStatus("current")


class _SlbNewCfgSipUdpRuleHdrFld_Type(Integer32):
    """Custom type slbNewCfgSipUdpRuleHdrFld based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("callid", 1),
          ("contact", 2),
          ("contentlen", 3),
          ("cseq", 4),
          ("expires", 5),
          ("from", 6),
          ("method", 11),
          ("none", 0),
          ("replyto", 7),
          ("reqline", 10),
          ("sdpcontent", 12),
          ("to", 8),
          ("via", 9))
    )


_SlbNewCfgSipUdpRuleHdrFld_Type.__name__ = "Integer32"
_SlbNewCfgSipUdpRuleHdrFld_Object = MibTableColumn
slbNewCfgSipUdpRuleHdrFld = _SlbNewCfgSipUdpRuleHdrFld_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 5, 2, 1, 2),
    _SlbNewCfgSipUdpRuleHdrFld_Type()
)
slbNewCfgSipUdpRuleHdrFld.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgSipUdpRuleHdrFld.setStatus("current")


class _SlbNewCfgSipUdpRuleContent_Type(DisplayString):
    """Custom type slbNewCfgSipUdpRuleContent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_SlbNewCfgSipUdpRuleContent_Type.__name__ = "DisplayString"
_SlbNewCfgSipUdpRuleContent_Object = MibTableColumn
slbNewCfgSipUdpRuleContent = _SlbNewCfgSipUdpRuleContent_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 5, 2, 1, 3),
    _SlbNewCfgSipUdpRuleContent_Type()
)
slbNewCfgSipUdpRuleContent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgSipUdpRuleContent.setStatus("current")


class _SlbNewCfgSipUdpRuleContract_Type(Integer32):
    """Custom type slbNewCfgSipUdpRuleContract based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_SlbNewCfgSipUdpRuleContract_Type.__name__ = "Integer32"
_SlbNewCfgSipUdpRuleContract_Object = MibTableColumn
slbNewCfgSipUdpRuleContract = _SlbNewCfgSipUdpRuleContract_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 5, 2, 1, 4),
    _SlbNewCfgSipUdpRuleContract_Type()
)
slbNewCfgSipUdpRuleContract.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgSipUdpRuleContract.setStatus("current")


class _SlbNewCfgSipUdpRuleMsg_Type(DisplayString):
    """Custom type slbNewCfgSipUdpRuleMsg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_SlbNewCfgSipUdpRuleMsg_Type.__name__ = "DisplayString"
_SlbNewCfgSipUdpRuleMsg_Object = MibTableColumn
slbNewCfgSipUdpRuleMsg = _SlbNewCfgSipUdpRuleMsg_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 5, 2, 1, 5),
    _SlbNewCfgSipUdpRuleMsg_Type()
)
slbNewCfgSipUdpRuleMsg.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgSipUdpRuleMsg.setStatus("current")


class _SlbNewCfgSipUdpRuleSeverity_Type(Integer32):
    """Custom type slbNewCfgSipUdpRuleSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_SlbNewCfgSipUdpRuleSeverity_Type.__name__ = "Integer32"
_SlbNewCfgSipUdpRuleSeverity_Object = MibTableColumn
slbNewCfgSipUdpRuleSeverity = _SlbNewCfgSipUdpRuleSeverity_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 5, 2, 1, 6),
    _SlbNewCfgSipUdpRuleSeverity_Type()
)
slbNewCfgSipUdpRuleSeverity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgSipUdpRuleSeverity.setStatus("current")


class _SlbNewCfgSipUdpRuleAdd_Type(Integer32):
    """Custom type slbNewCfgSipUdpRuleAdd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_SlbNewCfgSipUdpRuleAdd_Type.__name__ = "Integer32"
_SlbNewCfgSipUdpRuleAdd_Object = MibTableColumn
slbNewCfgSipUdpRuleAdd = _SlbNewCfgSipUdpRuleAdd_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 5, 2, 1, 7),
    _SlbNewCfgSipUdpRuleAdd_Type()
)
slbNewCfgSipUdpRuleAdd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgSipUdpRuleAdd.setStatus("current")


class _SlbNewCfgSipUdpRuleRem_Type(Integer32):
    """Custom type slbNewCfgSipUdpRuleRem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_SlbNewCfgSipUdpRuleRem_Type.__name__ = "Integer32"
_SlbNewCfgSipUdpRuleRem_Object = MibTableColumn
slbNewCfgSipUdpRuleRem = _SlbNewCfgSipUdpRuleRem_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 5, 2, 1, 8),
    _SlbNewCfgSipUdpRuleRem_Type()
)
slbNewCfgSipUdpRuleRem.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgSipUdpRuleRem.setStatus("current")


class _SlbNewCfgSipUdpRuleState_Type(Integer32):
    """Custom type slbNewCfgSipUdpRuleState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SlbNewCfgSipUdpRuleState_Type.__name__ = "Integer32"
_SlbNewCfgSipUdpRuleState_Object = MibTableColumn
slbNewCfgSipUdpRuleState = _SlbNewCfgSipUdpRuleState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 5, 2, 1, 9),
    _SlbNewCfgSipUdpRuleState_Type()
)
slbNewCfgSipUdpRuleState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgSipUdpRuleState.setStatus("current")


class _SlbNewCfgSipUdpRuleDelete_Type(Integer32):
    """Custom type slbNewCfgSipUdpRuleDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delete", 2),
          ("other", 1))
    )


_SlbNewCfgSipUdpRuleDelete_Type.__name__ = "Integer32"
_SlbNewCfgSipUdpRuleDelete_Object = MibTableColumn
slbNewCfgSipUdpRuleDelete = _SlbNewCfgSipUdpRuleDelete_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 5, 2, 1, 10),
    _SlbNewCfgSipUdpRuleDelete_Type()
)
slbNewCfgSipUdpRuleDelete.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgSipUdpRuleDelete.setStatus("current")
_SlbNewCfgSipUdpRuleBmap_Type = OctetString
_SlbNewCfgSipUdpRuleBmap_Object = MibTableColumn
slbNewCfgSipUdpRuleBmap = _SlbNewCfgSipUdpRuleBmap_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 5, 2, 1, 11),
    _SlbNewCfgSipUdpRuleBmap_Type()
)
slbNewCfgSipUdpRuleBmap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbNewCfgSipUdpRuleBmap.setStatus("current")
_ContentClass_ObjectIdentity = ObjectIdentity
contentClass = _ContentClass_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6)
)
_Layer7CurCfgContentClassTable_Object = MibTable
layer7CurCfgContentClassTable = _Layer7CurCfgContentClassTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 1)
)
if mibBuilder.loadTexts:
    layer7CurCfgContentClassTable.setStatus("current")
_Layer7CurCfgContentClassEntry_Object = MibTableRow
layer7CurCfgContentClassEntry = _Layer7CurCfgContentClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 1, 1)
)
layer7CurCfgContentClassEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-LAYER7-MIB", "layer7CurCfgContentClassID"),
)
if mibBuilder.loadTexts:
    layer7CurCfgContentClassEntry.setStatus("current")


class _Layer7CurCfgContentClassID_Type(DisplayString):
    """Custom type layer7CurCfgContentClassID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Layer7CurCfgContentClassID_Type.__name__ = "DisplayString"
_Layer7CurCfgContentClassID_Object = MibTableColumn
layer7CurCfgContentClassID = _Layer7CurCfgContentClassID_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 1, 1, 1),
    _Layer7CurCfgContentClassID_Type()
)
layer7CurCfgContentClassID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgContentClassID.setStatus("current")


class _Layer7CurCfgContentClassName_Type(DisplayString):
    """Custom type layer7CurCfgContentClassName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Layer7CurCfgContentClassName_Type.__name__ = "DisplayString"
_Layer7CurCfgContentClassName_Object = MibTableColumn
layer7CurCfgContentClassName = _Layer7CurCfgContentClassName_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 1, 1, 2),
    _Layer7CurCfgContentClassName_Type()
)
layer7CurCfgContentClassName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgContentClassName.setStatus("current")


class _Layer7CurCfgContentClassLogicalExpression_Type(DisplayString):
    """Custom type layer7CurCfgContentClassLogicalExpression based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Layer7CurCfgContentClassLogicalExpression_Type.__name__ = "DisplayString"
_Layer7CurCfgContentClassLogicalExpression_Object = MibTableColumn
layer7CurCfgContentClassLogicalExpression = _Layer7CurCfgContentClassLogicalExpression_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 1, 1, 3),
    _Layer7CurCfgContentClassLogicalExpression_Type()
)
layer7CurCfgContentClassLogicalExpression.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgContentClassLogicalExpression.setStatus("current")


class _Layer7CurCfgContentClassHostName_Type(Integer32):
    """Custom type layer7CurCfgContentClassHostName based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_Layer7CurCfgContentClassHostName_Type.__name__ = "Integer32"
_Layer7CurCfgContentClassHostName_Object = MibTableColumn
layer7CurCfgContentClassHostName = _Layer7CurCfgContentClassHostName_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 1, 1, 4),
    _Layer7CurCfgContentClassHostName_Type()
)
layer7CurCfgContentClassHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgContentClassHostName.setStatus("current")


class _Layer7CurCfgContentClassPath_Type(Integer32):
    """Custom type layer7CurCfgContentClassPath based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_Layer7CurCfgContentClassPath_Type.__name__ = "Integer32"
_Layer7CurCfgContentClassPath_Object = MibTableColumn
layer7CurCfgContentClassPath = _Layer7CurCfgContentClassPath_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 1, 1, 5),
    _Layer7CurCfgContentClassPath_Type()
)
layer7CurCfgContentClassPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgContentClassPath.setStatus("current")


class _Layer7CurCfgContentClassFileName_Type(Integer32):
    """Custom type layer7CurCfgContentClassFileName based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_Layer7CurCfgContentClassFileName_Type.__name__ = "Integer32"
_Layer7CurCfgContentClassFileName_Object = MibTableColumn
layer7CurCfgContentClassFileName = _Layer7CurCfgContentClassFileName_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 1, 1, 6),
    _Layer7CurCfgContentClassFileName_Type()
)
layer7CurCfgContentClassFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgContentClassFileName.setStatus("current")


class _Layer7CurCfgContentClassFileType_Type(Integer32):
    """Custom type layer7CurCfgContentClassFileType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_Layer7CurCfgContentClassFileType_Type.__name__ = "Integer32"
_Layer7CurCfgContentClassFileType_Object = MibTableColumn
layer7CurCfgContentClassFileType = _Layer7CurCfgContentClassFileType_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 1, 1, 7),
    _Layer7CurCfgContentClassFileType_Type()
)
layer7CurCfgContentClassFileType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgContentClassFileType.setStatus("current")


class _Layer7CurCfgContentClassHeader_Type(Integer32):
    """Custom type layer7CurCfgContentClassHeader based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_Layer7CurCfgContentClassHeader_Type.__name__ = "Integer32"
_Layer7CurCfgContentClassHeader_Object = MibTableColumn
layer7CurCfgContentClassHeader = _Layer7CurCfgContentClassHeader_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 1, 1, 8),
    _Layer7CurCfgContentClassHeader_Type()
)
layer7CurCfgContentClassHeader.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgContentClassHeader.setStatus("current")


class _Layer7CurCfgContentClassCookie_Type(Integer32):
    """Custom type layer7CurCfgContentClassCookie based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_Layer7CurCfgContentClassCookie_Type.__name__ = "Integer32"
_Layer7CurCfgContentClassCookie_Object = MibTableColumn
layer7CurCfgContentClassCookie = _Layer7CurCfgContentClassCookie_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 1, 1, 9),
    _Layer7CurCfgContentClassCookie_Type()
)
layer7CurCfgContentClassCookie.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgContentClassCookie.setStatus("current")


class _Layer7CurCfgContentClassText_Type(Integer32):
    """Custom type layer7CurCfgContentClassText based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_Layer7CurCfgContentClassText_Type.__name__ = "Integer32"
_Layer7CurCfgContentClassText_Object = MibTableColumn
layer7CurCfgContentClassText = _Layer7CurCfgContentClassText_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 1, 1, 10),
    _Layer7CurCfgContentClassText_Type()
)
layer7CurCfgContentClassText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgContentClassText.setStatus("current")


class _Layer7CurCfgContentClassXMLTag_Type(Integer32):
    """Custom type layer7CurCfgContentClassXMLTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_Layer7CurCfgContentClassXMLTag_Type.__name__ = "Integer32"
_Layer7CurCfgContentClassXMLTag_Object = MibTableColumn
layer7CurCfgContentClassXMLTag = _Layer7CurCfgContentClassXMLTag_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 1, 1, 11),
    _Layer7CurCfgContentClassXMLTag_Type()
)
layer7CurCfgContentClassXMLTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgContentClassXMLTag.setStatus("current")
_Layer7NewCfgContentClassTable_Object = MibTable
layer7NewCfgContentClassTable = _Layer7NewCfgContentClassTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 2)
)
if mibBuilder.loadTexts:
    layer7NewCfgContentClassTable.setStatus("current")
_Layer7NewCfgContentClassEntry_Object = MibTableRow
layer7NewCfgContentClassEntry = _Layer7NewCfgContentClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 2, 1)
)
layer7NewCfgContentClassEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-LAYER7-MIB", "layer7NewCfgContentClassID"),
)
if mibBuilder.loadTexts:
    layer7NewCfgContentClassEntry.setStatus("current")


class _Layer7NewCfgContentClassID_Type(DisplayString):
    """Custom type layer7NewCfgContentClassID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Layer7NewCfgContentClassID_Type.__name__ = "DisplayString"
_Layer7NewCfgContentClassID_Object = MibTableColumn
layer7NewCfgContentClassID = _Layer7NewCfgContentClassID_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 2, 1, 1),
    _Layer7NewCfgContentClassID_Type()
)
layer7NewCfgContentClassID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    layer7NewCfgContentClassID.setStatus("current")


class _Layer7NewCfgContentClassName_Type(DisplayString):
    """Custom type layer7NewCfgContentClassName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Layer7NewCfgContentClassName_Type.__name__ = "DisplayString"
_Layer7NewCfgContentClassName_Object = MibTableColumn
layer7NewCfgContentClassName = _Layer7NewCfgContentClassName_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 2, 1, 2),
    _Layer7NewCfgContentClassName_Type()
)
layer7NewCfgContentClassName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    layer7NewCfgContentClassName.setStatus("current")


class _Layer7NewCfgContentClassLogicalExpression_Type(DisplayString):
    """Custom type layer7NewCfgContentClassLogicalExpression based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Layer7NewCfgContentClassLogicalExpression_Type.__name__ = "DisplayString"
_Layer7NewCfgContentClassLogicalExpression_Object = MibTableColumn
layer7NewCfgContentClassLogicalExpression = _Layer7NewCfgContentClassLogicalExpression_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 2, 1, 3),
    _Layer7NewCfgContentClassLogicalExpression_Type()
)
layer7NewCfgContentClassLogicalExpression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    layer7NewCfgContentClassLogicalExpression.setStatus("current")


class _Layer7NewCfgContentClassHostName_Type(Integer32):
    """Custom type layer7NewCfgContentClassHostName based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_Layer7NewCfgContentClassHostName_Type.__name__ = "Integer32"
_Layer7NewCfgContentClassHostName_Object = MibTableColumn
layer7NewCfgContentClassHostName = _Layer7NewCfgContentClassHostName_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 2, 1, 4),
    _Layer7NewCfgContentClassHostName_Type()
)
layer7NewCfgContentClassHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7NewCfgContentClassHostName.setStatus("current")


class _Layer7NewCfgContentClassPath_Type(Integer32):
    """Custom type layer7NewCfgContentClassPath based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_Layer7NewCfgContentClassPath_Type.__name__ = "Integer32"
_Layer7NewCfgContentClassPath_Object = MibTableColumn
layer7NewCfgContentClassPath = _Layer7NewCfgContentClassPath_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 2, 1, 5),
    _Layer7NewCfgContentClassPath_Type()
)
layer7NewCfgContentClassPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7NewCfgContentClassPath.setStatus("current")


class _Layer7NewCfgContentClassFileName_Type(Integer32):
    """Custom type layer7NewCfgContentClassFileName based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_Layer7NewCfgContentClassFileName_Type.__name__ = "Integer32"
_Layer7NewCfgContentClassFileName_Object = MibTableColumn
layer7NewCfgContentClassFileName = _Layer7NewCfgContentClassFileName_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 2, 1, 6),
    _Layer7NewCfgContentClassFileName_Type()
)
layer7NewCfgContentClassFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7NewCfgContentClassFileName.setStatus("current")


class _Layer7NewCfgContentClassFileType_Type(Integer32):
    """Custom type layer7NewCfgContentClassFileType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_Layer7NewCfgContentClassFileType_Type.__name__ = "Integer32"
_Layer7NewCfgContentClassFileType_Object = MibTableColumn
layer7NewCfgContentClassFileType = _Layer7NewCfgContentClassFileType_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 2, 1, 7),
    _Layer7NewCfgContentClassFileType_Type()
)
layer7NewCfgContentClassFileType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7NewCfgContentClassFileType.setStatus("current")


class _Layer7NewCfgContentClassHeader_Type(Integer32):
    """Custom type layer7NewCfgContentClassHeader based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_Layer7NewCfgContentClassHeader_Type.__name__ = "Integer32"
_Layer7NewCfgContentClassHeader_Object = MibTableColumn
layer7NewCfgContentClassHeader = _Layer7NewCfgContentClassHeader_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 2, 1, 8),
    _Layer7NewCfgContentClassHeader_Type()
)
layer7NewCfgContentClassHeader.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7NewCfgContentClassHeader.setStatus("current")


class _Layer7NewCfgContentClassCookie_Type(Integer32):
    """Custom type layer7NewCfgContentClassCookie based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_Layer7NewCfgContentClassCookie_Type.__name__ = "Integer32"
_Layer7NewCfgContentClassCookie_Object = MibTableColumn
layer7NewCfgContentClassCookie = _Layer7NewCfgContentClassCookie_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 2, 1, 9),
    _Layer7NewCfgContentClassCookie_Type()
)
layer7NewCfgContentClassCookie.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7NewCfgContentClassCookie.setStatus("current")


class _Layer7NewCfgContentClassText_Type(Integer32):
    """Custom type layer7NewCfgContentClassText based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_Layer7NewCfgContentClassText_Type.__name__ = "Integer32"
_Layer7NewCfgContentClassText_Object = MibTableColumn
layer7NewCfgContentClassText = _Layer7NewCfgContentClassText_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 2, 1, 10),
    _Layer7NewCfgContentClassText_Type()
)
layer7NewCfgContentClassText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7NewCfgContentClassText.setStatus("current")


class _Layer7NewCfgContentClassXMLTag_Type(Integer32):
    """Custom type layer7NewCfgContentClassXMLTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_Layer7NewCfgContentClassXMLTag_Type.__name__ = "Integer32"
_Layer7NewCfgContentClassXMLTag_Object = MibTableColumn
layer7NewCfgContentClassXMLTag = _Layer7NewCfgContentClassXMLTag_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 2, 1, 11),
    _Layer7NewCfgContentClassXMLTag_Type()
)
layer7NewCfgContentClassXMLTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7NewCfgContentClassXMLTag.setStatus("current")


class _Layer7NewCfgContentClassDelete_Type(Integer32):
    """Custom type layer7NewCfgContentClassDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delete", 2),
          ("other", 1))
    )


_Layer7NewCfgContentClassDelete_Type.__name__ = "Integer32"
_Layer7NewCfgContentClassDelete_Object = MibTableColumn
layer7NewCfgContentClassDelete = _Layer7NewCfgContentClassDelete_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 2, 1, 12),
    _Layer7NewCfgContentClassDelete_Type()
)
layer7NewCfgContentClassDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    layer7NewCfgContentClassDelete.setStatus("current")


class _Layer7NewCfgContentClassCopy_Type(DisplayString):
    """Custom type layer7NewCfgContentClassCopy based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Layer7NewCfgContentClassCopy_Type.__name__ = "DisplayString"
_Layer7NewCfgContentClassCopy_Object = MibTableColumn
layer7NewCfgContentClassCopy = _Layer7NewCfgContentClassCopy_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 2, 1, 13),
    _Layer7NewCfgContentClassCopy_Type()
)
layer7NewCfgContentClassCopy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    layer7NewCfgContentClassCopy.setStatus("current")
_Layer7CurCfgContentClassHostNameTable_Object = MibTable
layer7CurCfgContentClassHostNameTable = _Layer7CurCfgContentClassHostNameTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 3)
)
if mibBuilder.loadTexts:
    layer7CurCfgContentClassHostNameTable.setStatus("current")
_Layer7CurCfgContentClassHostNameEntry_Object = MibTableRow
layer7CurCfgContentClassHostNameEntry = _Layer7CurCfgContentClassHostNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 3, 1)
)
layer7CurCfgContentClassHostNameEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-LAYER7-MIB", "layer7CurCfgContentClassHostNameContentClassID"),
    (0, "ALTEON-CHEETAH-LAYER7-MIB", "layer7CurCfgContentClassHostNameID"),
)
if mibBuilder.loadTexts:
    layer7CurCfgContentClassHostNameEntry.setStatus("current")


class _Layer7CurCfgContentClassHostNameContentClassID_Type(DisplayString):
    """Custom type layer7CurCfgContentClassHostNameContentClassID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Layer7CurCfgContentClassHostNameContentClassID_Type.__name__ = "DisplayString"
_Layer7CurCfgContentClassHostNameContentClassID_Object = MibTableColumn
layer7CurCfgContentClassHostNameContentClassID = _Layer7CurCfgContentClassHostNameContentClassID_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 3, 1, 1),
    _Layer7CurCfgContentClassHostNameContentClassID_Type()
)
layer7CurCfgContentClassHostNameContentClassID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgContentClassHostNameContentClassID.setStatus("current")


class _Layer7CurCfgContentClassHostNameID_Type(DisplayString):
    """Custom type layer7CurCfgContentClassHostNameID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Layer7CurCfgContentClassHostNameID_Type.__name__ = "DisplayString"
_Layer7CurCfgContentClassHostNameID_Object = MibTableColumn
layer7CurCfgContentClassHostNameID = _Layer7CurCfgContentClassHostNameID_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 3, 1, 2),
    _Layer7CurCfgContentClassHostNameID_Type()
)
layer7CurCfgContentClassHostNameID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgContentClassHostNameID.setStatus("current")


class _Layer7CurCfgContentClassHostNameHostName_Type(DisplayString):
    """Custom type layer7CurCfgContentClassHostNameHostName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_Layer7CurCfgContentClassHostNameHostName_Type.__name__ = "DisplayString"
_Layer7CurCfgContentClassHostNameHostName_Object = MibTableColumn
layer7CurCfgContentClassHostNameHostName = _Layer7CurCfgContentClassHostNameHostName_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 3, 1, 3),
    _Layer7CurCfgContentClassHostNameHostName_Type()
)
layer7CurCfgContentClassHostNameHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgContentClassHostNameHostName.setStatus("current")


class _Layer7CurCfgContentClassHostNameMatchType_Type(Integer32):
    """Custom type layer7CurCfgContentClassHostNameMatchType based on Integer32"""
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
        *(("equal", 3),
          ("include", 4),
          ("prefx", 2),
          ("regex", 5),
          ("sufx", 1))
    )


_Layer7CurCfgContentClassHostNameMatchType_Type.__name__ = "Integer32"
_Layer7CurCfgContentClassHostNameMatchType_Object = MibTableColumn
layer7CurCfgContentClassHostNameMatchType = _Layer7CurCfgContentClassHostNameMatchType_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 3, 1, 4),
    _Layer7CurCfgContentClassHostNameMatchType_Type()
)
layer7CurCfgContentClassHostNameMatchType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgContentClassHostNameMatchType.setStatus("current")
_Layer7NewCfgContentClassHostNameTable_Object = MibTable
layer7NewCfgContentClassHostNameTable = _Layer7NewCfgContentClassHostNameTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 4)
)
if mibBuilder.loadTexts:
    layer7NewCfgContentClassHostNameTable.setStatus("current")
_Layer7NewCfgContentClassHostNameEntry_Object = MibTableRow
layer7NewCfgContentClassHostNameEntry = _Layer7NewCfgContentClassHostNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 4, 1)
)
layer7NewCfgContentClassHostNameEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-LAYER7-MIB", "layer7NewCfgContentClassHostNameContentClassID"),
    (0, "ALTEON-CHEETAH-LAYER7-MIB", "layer7NewCfgContentClassHostNameID"),
)
if mibBuilder.loadTexts:
    layer7NewCfgContentClassHostNameEntry.setStatus("current")


class _Layer7NewCfgContentClassHostNameContentClassID_Type(DisplayString):
    """Custom type layer7NewCfgContentClassHostNameContentClassID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Layer7NewCfgContentClassHostNameContentClassID_Type.__name__ = "DisplayString"
_Layer7NewCfgContentClassHostNameContentClassID_Object = MibTableColumn
layer7NewCfgContentClassHostNameContentClassID = _Layer7NewCfgContentClassHostNameContentClassID_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 4, 1, 1),
    _Layer7NewCfgContentClassHostNameContentClassID_Type()
)
layer7NewCfgContentClassHostNameContentClassID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    layer7NewCfgContentClassHostNameContentClassID.setStatus("current")


class _Layer7NewCfgContentClassHostNameID_Type(DisplayString):
    """Custom type layer7NewCfgContentClassHostNameID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Layer7NewCfgContentClassHostNameID_Type.__name__ = "DisplayString"
_Layer7NewCfgContentClassHostNameID_Object = MibTableColumn
layer7NewCfgContentClassHostNameID = _Layer7NewCfgContentClassHostNameID_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 4, 1, 2),
    _Layer7NewCfgContentClassHostNameID_Type()
)
layer7NewCfgContentClassHostNameID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    layer7NewCfgContentClassHostNameID.setStatus("current")


class _Layer7NewCfgContentClassHostNameHostName_Type(DisplayString):
    """Custom type layer7NewCfgContentClassHostNameHostName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_Layer7NewCfgContentClassHostNameHostName_Type.__name__ = "DisplayString"
_Layer7NewCfgContentClassHostNameHostName_Object = MibTableColumn
layer7NewCfgContentClassHostNameHostName = _Layer7NewCfgContentClassHostNameHostName_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 4, 1, 3),
    _Layer7NewCfgContentClassHostNameHostName_Type()
)
layer7NewCfgContentClassHostNameHostName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    layer7NewCfgContentClassHostNameHostName.setStatus("current")


class _Layer7NewCfgContentClassHostNameMatchType_Type(Integer32):
    """Custom type layer7NewCfgContentClassHostNameMatchType based on Integer32"""
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
        *(("equal", 3),
          ("include", 4),
          ("prefx", 2),
          ("regex", 5),
          ("sufx", 1))
    )


_Layer7NewCfgContentClassHostNameMatchType_Type.__name__ = "Integer32"
_Layer7NewCfgContentClassHostNameMatchType_Object = MibTableColumn
layer7NewCfgContentClassHostNameMatchType = _Layer7NewCfgContentClassHostNameMatchType_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 4, 1, 4),
    _Layer7NewCfgContentClassHostNameMatchType_Type()
)
layer7NewCfgContentClassHostNameMatchType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    layer7NewCfgContentClassHostNameMatchType.setStatus("current")


class _Layer7NewCfgContentClassHostNameDelete_Type(Integer32):
    """Custom type layer7NewCfgContentClassHostNameDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delete", 2),
          ("other", 1))
    )


_Layer7NewCfgContentClassHostNameDelete_Type.__name__ = "Integer32"
_Layer7NewCfgContentClassHostNameDelete_Object = MibTableColumn
layer7NewCfgContentClassHostNameDelete = _Layer7NewCfgContentClassHostNameDelete_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 4, 1, 5),
    _Layer7NewCfgContentClassHostNameDelete_Type()
)
layer7NewCfgContentClassHostNameDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    layer7NewCfgContentClassHostNameDelete.setStatus("current")
_Layer7CurCfgContentClassPathTable_Object = MibTable
layer7CurCfgContentClassPathTable = _Layer7CurCfgContentClassPathTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 5)
)
if mibBuilder.loadTexts:
    layer7CurCfgContentClassPathTable.setStatus("current")
_Layer7CurCfgContentClassPathEntry_Object = MibTableRow
layer7CurCfgContentClassPathEntry = _Layer7CurCfgContentClassPathEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 5, 1)
)
layer7CurCfgContentClassPathEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-LAYER7-MIB", "layer7CurCfgContentClassPathContentClassID"),
    (0, "ALTEON-CHEETAH-LAYER7-MIB", "layer7CurCfgContentClassPathID"),
)
if mibBuilder.loadTexts:
    layer7CurCfgContentClassPathEntry.setStatus("current")


class _Layer7CurCfgContentClassPathContentClassID_Type(DisplayString):
    """Custom type layer7CurCfgContentClassPathContentClassID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Layer7CurCfgContentClassPathContentClassID_Type.__name__ = "DisplayString"
_Layer7CurCfgContentClassPathContentClassID_Object = MibTableColumn
layer7CurCfgContentClassPathContentClassID = _Layer7CurCfgContentClassPathContentClassID_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 5, 1, 1),
    _Layer7CurCfgContentClassPathContentClassID_Type()
)
layer7CurCfgContentClassPathContentClassID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgContentClassPathContentClassID.setStatus("current")


class _Layer7CurCfgContentClassPathID_Type(DisplayString):
    """Custom type layer7CurCfgContentClassPathID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Layer7CurCfgContentClassPathID_Type.__name__ = "DisplayString"
_Layer7CurCfgContentClassPathID_Object = MibTableColumn
layer7CurCfgContentClassPathID = _Layer7CurCfgContentClassPathID_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 5, 1, 2),
    _Layer7CurCfgContentClassPathID_Type()
)
layer7CurCfgContentClassPathID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgContentClassPathID.setStatus("current")


class _Layer7CurCfgContentClassPathFilePath_Type(DisplayString):
    """Custom type layer7CurCfgContentClassPathFilePath based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Layer7CurCfgContentClassPathFilePath_Type.__name__ = "DisplayString"
_Layer7CurCfgContentClassPathFilePath_Object = MibTableColumn
layer7CurCfgContentClassPathFilePath = _Layer7CurCfgContentClassPathFilePath_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 5, 1, 3),
    _Layer7CurCfgContentClassPathFilePath_Type()
)
layer7CurCfgContentClassPathFilePath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgContentClassPathFilePath.setStatus("current")


class _Layer7CurCfgContentClassPathMatchType_Type(Integer32):
    """Custom type layer7CurCfgContentClassPathMatchType based on Integer32"""
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
        *(("equal", 3),
          ("include", 4),
          ("prefx", 2),
          ("regex", 5),
          ("sufx", 1))
    )


_Layer7CurCfgContentClassPathMatchType_Type.__name__ = "Integer32"
_Layer7CurCfgContentClassPathMatchType_Object = MibTableColumn
layer7CurCfgContentClassPathMatchType = _Layer7CurCfgContentClassPathMatchType_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 5, 1, 4),
    _Layer7CurCfgContentClassPathMatchType_Type()
)
layer7CurCfgContentClassPathMatchType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgContentClassPathMatchType.setStatus("current")


class _Layer7CurCfgContentClassPathCase_Type(Integer32):
    """Custom type layer7CurCfgContentClassPathCase based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Layer7CurCfgContentClassPathCase_Type.__name__ = "Integer32"
_Layer7CurCfgContentClassPathCase_Object = MibTableColumn
layer7CurCfgContentClassPathCase = _Layer7CurCfgContentClassPathCase_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 5, 1, 5),
    _Layer7CurCfgContentClassPathCase_Type()
)
layer7CurCfgContentClassPathCase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgContentClassPathCase.setStatus("current")
_Layer7NewCfgContentClassPathTable_Object = MibTable
layer7NewCfgContentClassPathTable = _Layer7NewCfgContentClassPathTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 6)
)
if mibBuilder.loadTexts:
    layer7NewCfgContentClassPathTable.setStatus("current")
_Layer7NewCfgContentClassPathEntry_Object = MibTableRow
layer7NewCfgContentClassPathEntry = _Layer7NewCfgContentClassPathEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 6, 1)
)
layer7NewCfgContentClassPathEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-LAYER7-MIB", "layer7NewCfgContentClassPathContentClassID"),
    (0, "ALTEON-CHEETAH-LAYER7-MIB", "layer7NewCfgContentClassPathID"),
)
if mibBuilder.loadTexts:
    layer7NewCfgContentClassPathEntry.setStatus("current")


class _Layer7NewCfgContentClassPathContentClassID_Type(DisplayString):
    """Custom type layer7NewCfgContentClassPathContentClassID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Layer7NewCfgContentClassPathContentClassID_Type.__name__ = "DisplayString"
_Layer7NewCfgContentClassPathContentClassID_Object = MibTableColumn
layer7NewCfgContentClassPathContentClassID = _Layer7NewCfgContentClassPathContentClassID_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 6, 1, 1),
    _Layer7NewCfgContentClassPathContentClassID_Type()
)
layer7NewCfgContentClassPathContentClassID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    layer7NewCfgContentClassPathContentClassID.setStatus("current")


class _Layer7NewCfgContentClassPathID_Type(DisplayString):
    """Custom type layer7NewCfgContentClassPathID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Layer7NewCfgContentClassPathID_Type.__name__ = "DisplayString"
_Layer7NewCfgContentClassPathID_Object = MibTableColumn
layer7NewCfgContentClassPathID = _Layer7NewCfgContentClassPathID_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 6, 1, 2),
    _Layer7NewCfgContentClassPathID_Type()
)
layer7NewCfgContentClassPathID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    layer7NewCfgContentClassPathID.setStatus("current")


class _Layer7NewCfgContentClassPathFilePath_Type(DisplayString):
    """Custom type layer7NewCfgContentClassPathFilePath based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Layer7NewCfgContentClassPathFilePath_Type.__name__ = "DisplayString"
_Layer7NewCfgContentClassPathFilePath_Object = MibTableColumn
layer7NewCfgContentClassPathFilePath = _Layer7NewCfgContentClassPathFilePath_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 6, 1, 3),
    _Layer7NewCfgContentClassPathFilePath_Type()
)
layer7NewCfgContentClassPathFilePath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    layer7NewCfgContentClassPathFilePath.setStatus("current")


class _Layer7NewCfgContentClassPathMatchType_Type(Integer32):
    """Custom type layer7NewCfgContentClassPathMatchType based on Integer32"""
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
        *(("equal", 3),
          ("include", 4),
          ("prefx", 2),
          ("regex", 5),
          ("sufx", 1))
    )


_Layer7NewCfgContentClassPathMatchType_Type.__name__ = "Integer32"
_Layer7NewCfgContentClassPathMatchType_Object = MibTableColumn
layer7NewCfgContentClassPathMatchType = _Layer7NewCfgContentClassPathMatchType_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 6, 1, 4),
    _Layer7NewCfgContentClassPathMatchType_Type()
)
layer7NewCfgContentClassPathMatchType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    layer7NewCfgContentClassPathMatchType.setStatus("current")


class _Layer7NewCfgContentClassPathCase_Type(Integer32):
    """Custom type layer7NewCfgContentClassPathCase based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Layer7NewCfgContentClassPathCase_Type.__name__ = "Integer32"
_Layer7NewCfgContentClassPathCase_Object = MibTableColumn
layer7NewCfgContentClassPathCase = _Layer7NewCfgContentClassPathCase_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 6, 1, 5),
    _Layer7NewCfgContentClassPathCase_Type()
)
layer7NewCfgContentClassPathCase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    layer7NewCfgContentClassPathCase.setStatus("current")


class _Layer7NewCfgContentClassPathDelete_Type(Integer32):
    """Custom type layer7NewCfgContentClassPathDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delete", 2),
          ("other", 1))
    )


_Layer7NewCfgContentClassPathDelete_Type.__name__ = "Integer32"
_Layer7NewCfgContentClassPathDelete_Object = MibTableColumn
layer7NewCfgContentClassPathDelete = _Layer7NewCfgContentClassPathDelete_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 6, 1, 7),
    _Layer7NewCfgContentClassPathDelete_Type()
)
layer7NewCfgContentClassPathDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    layer7NewCfgContentClassPathDelete.setStatus("current")
_Layer7CurCfgContentClassFileNameTable_Object = MibTable
layer7CurCfgContentClassFileNameTable = _Layer7CurCfgContentClassFileNameTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 7)
)
if mibBuilder.loadTexts:
    layer7CurCfgContentClassFileNameTable.setStatus("current")
_Layer7CurCfgContentClassFileNameEntry_Object = MibTableRow
layer7CurCfgContentClassFileNameEntry = _Layer7CurCfgContentClassFileNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 7, 1)
)
layer7CurCfgContentClassFileNameEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-LAYER7-MIB", "layer7CurCfgContentClassFileNameContentClassID"),
    (0, "ALTEON-CHEETAH-LAYER7-MIB", "layer7CurCfgContentClassFileNameID"),
)
if mibBuilder.loadTexts:
    layer7CurCfgContentClassFileNameEntry.setStatus("current")


class _Layer7CurCfgContentClassFileNameContentClassID_Type(DisplayString):
    """Custom type layer7CurCfgContentClassFileNameContentClassID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Layer7CurCfgContentClassFileNameContentClassID_Type.__name__ = "DisplayString"
_Layer7CurCfgContentClassFileNameContentClassID_Object = MibTableColumn
layer7CurCfgContentClassFileNameContentClassID = _Layer7CurCfgContentClassFileNameContentClassID_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 7, 1, 1),
    _Layer7CurCfgContentClassFileNameContentClassID_Type()
)
layer7CurCfgContentClassFileNameContentClassID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgContentClassFileNameContentClassID.setStatus("current")


class _Layer7CurCfgContentClassFileNameID_Type(DisplayString):
    """Custom type layer7CurCfgContentClassFileNameID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Layer7CurCfgContentClassFileNameID_Type.__name__ = "DisplayString"
_Layer7CurCfgContentClassFileNameID_Object = MibTableColumn
layer7CurCfgContentClassFileNameID = _Layer7CurCfgContentClassFileNameID_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 7, 1, 2),
    _Layer7CurCfgContentClassFileNameID_Type()
)
layer7CurCfgContentClassFileNameID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgContentClassFileNameID.setStatus("current")


class _Layer7CurCfgContentClassFileNameFileName_Type(DisplayString):
    """Custom type layer7CurCfgContentClassFileNameFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_Layer7CurCfgContentClassFileNameFileName_Type.__name__ = "DisplayString"
_Layer7CurCfgContentClassFileNameFileName_Object = MibTableColumn
layer7CurCfgContentClassFileNameFileName = _Layer7CurCfgContentClassFileNameFileName_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 7, 1, 3),
    _Layer7CurCfgContentClassFileNameFileName_Type()
)
layer7CurCfgContentClassFileNameFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgContentClassFileNameFileName.setStatus("current")


class _Layer7CurCfgContentClassFileNameMatchType_Type(Integer32):
    """Custom type layer7CurCfgContentClassFileNameMatchType based on Integer32"""
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
        *(("equal", 3),
          ("include", 4),
          ("prefx", 2),
          ("regex", 5),
          ("sufx", 1))
    )


_Layer7CurCfgContentClassFileNameMatchType_Type.__name__ = "Integer32"
_Layer7CurCfgContentClassFileNameMatchType_Object = MibTableColumn
layer7CurCfgContentClassFileNameMatchType = _Layer7CurCfgContentClassFileNameMatchType_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 7, 1, 4),
    _Layer7CurCfgContentClassFileNameMatchType_Type()
)
layer7CurCfgContentClassFileNameMatchType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgContentClassFileNameMatchType.setStatus("current")


class _Layer7CurCfgContentClassFileNameCase_Type(Integer32):
    """Custom type layer7CurCfgContentClassFileNameCase based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Layer7CurCfgContentClassFileNameCase_Type.__name__ = "Integer32"
_Layer7CurCfgContentClassFileNameCase_Object = MibTableColumn
layer7CurCfgContentClassFileNameCase = _Layer7CurCfgContentClassFileNameCase_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 7, 1, 5),
    _Layer7CurCfgContentClassFileNameCase_Type()
)
layer7CurCfgContentClassFileNameCase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgContentClassFileNameCase.setStatus("current")
_Layer7NewCfgContentClassFileNameTable_Object = MibTable
layer7NewCfgContentClassFileNameTable = _Layer7NewCfgContentClassFileNameTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 8)
)
if mibBuilder.loadTexts:
    layer7NewCfgContentClassFileNameTable.setStatus("current")
_Layer7NewCfgContentClassFileNameEntry_Object = MibTableRow
layer7NewCfgContentClassFileNameEntry = _Layer7NewCfgContentClassFileNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 8, 1)
)
layer7NewCfgContentClassFileNameEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-LAYER7-MIB", "layer7NewCfgContentClassFileNameContentClassID"),
    (0, "ALTEON-CHEETAH-LAYER7-MIB", "layer7NewCfgContentClassFileNameID"),
)
if mibBuilder.loadTexts:
    layer7NewCfgContentClassFileNameEntry.setStatus("current")


class _Layer7NewCfgContentClassFileNameContentClassID_Type(DisplayString):
    """Custom type layer7NewCfgContentClassFileNameContentClassID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Layer7NewCfgContentClassFileNameContentClassID_Type.__name__ = "DisplayString"
_Layer7NewCfgContentClassFileNameContentClassID_Object = MibTableColumn
layer7NewCfgContentClassFileNameContentClassID = _Layer7NewCfgContentClassFileNameContentClassID_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 8, 1, 1),
    _Layer7NewCfgContentClassFileNameContentClassID_Type()
)
layer7NewCfgContentClassFileNameContentClassID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    layer7NewCfgContentClassFileNameContentClassID.setStatus("current")


class _Layer7NewCfgContentClassFileNameID_Type(DisplayString):
    """Custom type layer7NewCfgContentClassFileNameID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Layer7NewCfgContentClassFileNameID_Type.__name__ = "DisplayString"
_Layer7NewCfgContentClassFileNameID_Object = MibTableColumn
layer7NewCfgContentClassFileNameID = _Layer7NewCfgContentClassFileNameID_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 8, 1, 2),
    _Layer7NewCfgContentClassFileNameID_Type()
)
layer7NewCfgContentClassFileNameID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    layer7NewCfgContentClassFileNameID.setStatus("current")


class _Layer7NewCfgContentClassFileNameFileName_Type(DisplayString):
    """Custom type layer7NewCfgContentClassFileNameFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_Layer7NewCfgContentClassFileNameFileName_Type.__name__ = "DisplayString"
_Layer7NewCfgContentClassFileNameFileName_Object = MibTableColumn
layer7NewCfgContentClassFileNameFileName = _Layer7NewCfgContentClassFileNameFileName_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 8, 1, 3),
    _Layer7NewCfgContentClassFileNameFileName_Type()
)
layer7NewCfgContentClassFileNameFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    layer7NewCfgContentClassFileNameFileName.setStatus("current")


class _Layer7NewCfgContentClassFileNameMatchType_Type(Integer32):
    """Custom type layer7NewCfgContentClassFileNameMatchType based on Integer32"""
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
        *(("equal", 3),
          ("include", 4),
          ("prefx", 2),
          ("regex", 5),
          ("sufx", 1))
    )


_Layer7NewCfgContentClassFileNameMatchType_Type.__name__ = "Integer32"
_Layer7NewCfgContentClassFileNameMatchType_Object = MibTableColumn
layer7NewCfgContentClassFileNameMatchType = _Layer7NewCfgContentClassFileNameMatchType_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 8, 1, 4),
    _Layer7NewCfgContentClassFileNameMatchType_Type()
)
layer7NewCfgContentClassFileNameMatchType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    layer7NewCfgContentClassFileNameMatchType.setStatus("current")


class _Layer7NewCfgContentClassFileNameCase_Type(Integer32):
    """Custom type layer7NewCfgContentClassFileNameCase based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Layer7NewCfgContentClassFileNameCase_Type.__name__ = "Integer32"
_Layer7NewCfgContentClassFileNameCase_Object = MibTableColumn
layer7NewCfgContentClassFileNameCase = _Layer7NewCfgContentClassFileNameCase_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 8, 1, 5),
    _Layer7NewCfgContentClassFileNameCase_Type()
)
layer7NewCfgContentClassFileNameCase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    layer7NewCfgContentClassFileNameCase.setStatus("current")


class _Layer7NewCfgContentClassFileNameDelete_Type(Integer32):
    """Custom type layer7NewCfgContentClassFileNameDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delete", 2),
          ("other", 1))
    )


_Layer7NewCfgContentClassFileNameDelete_Type.__name__ = "Integer32"
_Layer7NewCfgContentClassFileNameDelete_Object = MibTableColumn
layer7NewCfgContentClassFileNameDelete = _Layer7NewCfgContentClassFileNameDelete_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 8, 1, 6),
    _Layer7NewCfgContentClassFileNameDelete_Type()
)
layer7NewCfgContentClassFileNameDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    layer7NewCfgContentClassFileNameDelete.setStatus("current")
_Layer7CurCfgContentClassFileTypeTable_Object = MibTable
layer7CurCfgContentClassFileTypeTable = _Layer7CurCfgContentClassFileTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 9)
)
if mibBuilder.loadTexts:
    layer7CurCfgContentClassFileTypeTable.setStatus("current")
_Layer7CurCfgContentClassFileTypeEntry_Object = MibTableRow
layer7CurCfgContentClassFileTypeEntry = _Layer7CurCfgContentClassFileTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 9, 1)
)
layer7CurCfgContentClassFileTypeEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-LAYER7-MIB", "layer7CurCfgContentClassFileTypeContentClassID"),
    (0, "ALTEON-CHEETAH-LAYER7-MIB", "layer7CurCfgContentClassFileTypeID"),
)
if mibBuilder.loadTexts:
    layer7CurCfgContentClassFileTypeEntry.setStatus("current")


class _Layer7CurCfgContentClassFileTypeContentClassID_Type(DisplayString):
    """Custom type layer7CurCfgContentClassFileTypeContentClassID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Layer7CurCfgContentClassFileTypeContentClassID_Type.__name__ = "DisplayString"
_Layer7CurCfgContentClassFileTypeContentClassID_Object = MibTableColumn
layer7CurCfgContentClassFileTypeContentClassID = _Layer7CurCfgContentClassFileTypeContentClassID_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 9, 1, 1),
    _Layer7CurCfgContentClassFileTypeContentClassID_Type()
)
layer7CurCfgContentClassFileTypeContentClassID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgContentClassFileTypeContentClassID.setStatus("current")


class _Layer7CurCfgContentClassFileTypeID_Type(DisplayString):
    """Custom type layer7CurCfgContentClassFileTypeID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Layer7CurCfgContentClassFileTypeID_Type.__name__ = "DisplayString"
_Layer7CurCfgContentClassFileTypeID_Object = MibTableColumn
layer7CurCfgContentClassFileTypeID = _Layer7CurCfgContentClassFileTypeID_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 9, 1, 2),
    _Layer7CurCfgContentClassFileTypeID_Type()
)
layer7CurCfgContentClassFileTypeID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgContentClassFileTypeID.setStatus("current")


class _Layer7CurCfgContentClassFileTypeFileType_Type(DisplayString):
    """Custom type layer7CurCfgContentClassFileTypeFileType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_Layer7CurCfgContentClassFileTypeFileType_Type.__name__ = "DisplayString"
_Layer7CurCfgContentClassFileTypeFileType_Object = MibTableColumn
layer7CurCfgContentClassFileTypeFileType = _Layer7CurCfgContentClassFileTypeFileType_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 9, 1, 3),
    _Layer7CurCfgContentClassFileTypeFileType_Type()
)
layer7CurCfgContentClassFileTypeFileType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgContentClassFileTypeFileType.setStatus("current")


class _Layer7CurCfgContentClassFileTypeMatchType_Type(Integer32):
    """Custom type layer7CurCfgContentClassFileTypeMatchType based on Integer32"""
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
        *(("equal", 3),
          ("include", 4),
          ("prefx", 2),
          ("regex", 5),
          ("sufx", 1))
    )


_Layer7CurCfgContentClassFileTypeMatchType_Type.__name__ = "Integer32"
_Layer7CurCfgContentClassFileTypeMatchType_Object = MibTableColumn
layer7CurCfgContentClassFileTypeMatchType = _Layer7CurCfgContentClassFileTypeMatchType_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 9, 1, 4),
    _Layer7CurCfgContentClassFileTypeMatchType_Type()
)
layer7CurCfgContentClassFileTypeMatchType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgContentClassFileTypeMatchType.setStatus("current")


class _Layer7CurCfgContentClassFileTypeCase_Type(Integer32):
    """Custom type layer7CurCfgContentClassFileTypeCase based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Layer7CurCfgContentClassFileTypeCase_Type.__name__ = "Integer32"
_Layer7CurCfgContentClassFileTypeCase_Object = MibTableColumn
layer7CurCfgContentClassFileTypeCase = _Layer7CurCfgContentClassFileTypeCase_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 9, 1, 5),
    _Layer7CurCfgContentClassFileTypeCase_Type()
)
layer7CurCfgContentClassFileTypeCase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgContentClassFileTypeCase.setStatus("current")
_Layer7NewCfgContentClassFileTypeTable_Object = MibTable
layer7NewCfgContentClassFileTypeTable = _Layer7NewCfgContentClassFileTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 10)
)
if mibBuilder.loadTexts:
    layer7NewCfgContentClassFileTypeTable.setStatus("current")
_Layer7NewCfgContentClassFileTypeEntry_Object = MibTableRow
layer7NewCfgContentClassFileTypeEntry = _Layer7NewCfgContentClassFileTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 10, 1)
)
layer7NewCfgContentClassFileTypeEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-LAYER7-MIB", "layer7NewCfgContentClassFileTypeContentClassID"),
    (0, "ALTEON-CHEETAH-LAYER7-MIB", "layer7NewCfgContentClassFileTypeID"),
)
if mibBuilder.loadTexts:
    layer7NewCfgContentClassFileTypeEntry.setStatus("current")


class _Layer7NewCfgContentClassFileTypeContentClassID_Type(DisplayString):
    """Custom type layer7NewCfgContentClassFileTypeContentClassID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Layer7NewCfgContentClassFileTypeContentClassID_Type.__name__ = "DisplayString"
_Layer7NewCfgContentClassFileTypeContentClassID_Object = MibTableColumn
layer7NewCfgContentClassFileTypeContentClassID = _Layer7NewCfgContentClassFileTypeContentClassID_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 10, 1, 1),
    _Layer7NewCfgContentClassFileTypeContentClassID_Type()
)
layer7NewCfgContentClassFileTypeContentClassID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    layer7NewCfgContentClassFileTypeContentClassID.setStatus("current")


class _Layer7NewCfgContentClassFileTypeID_Type(DisplayString):
    """Custom type layer7NewCfgContentClassFileTypeID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Layer7NewCfgContentClassFileTypeID_Type.__name__ = "DisplayString"
_Layer7NewCfgContentClassFileTypeID_Object = MibTableColumn
layer7NewCfgContentClassFileTypeID = _Layer7NewCfgContentClassFileTypeID_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 10, 1, 2),
    _Layer7NewCfgContentClassFileTypeID_Type()
)
layer7NewCfgContentClassFileTypeID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    layer7NewCfgContentClassFileTypeID.setStatus("current")


class _Layer7NewCfgContentClassFileTypeFileType_Type(DisplayString):
    """Custom type layer7NewCfgContentClassFileTypeFileType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_Layer7NewCfgContentClassFileTypeFileType_Type.__name__ = "DisplayString"
_Layer7NewCfgContentClassFileTypeFileType_Object = MibTableColumn
layer7NewCfgContentClassFileTypeFileType = _Layer7NewCfgContentClassFileTypeFileType_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 10, 1, 3),
    _Layer7NewCfgContentClassFileTypeFileType_Type()
)
layer7NewCfgContentClassFileTypeFileType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    layer7NewCfgContentClassFileTypeFileType.setStatus("current")


class _Layer7NewCfgContentClassFileTypeMatchType_Type(Integer32):
    """Custom type layer7NewCfgContentClassFileTypeMatchType based on Integer32"""
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
        *(("equal", 3),
          ("include", 4),
          ("prefx", 2),
          ("regex", 5),
          ("sufx", 1))
    )


_Layer7NewCfgContentClassFileTypeMatchType_Type.__name__ = "Integer32"
_Layer7NewCfgContentClassFileTypeMatchType_Object = MibTableColumn
layer7NewCfgContentClassFileTypeMatchType = _Layer7NewCfgContentClassFileTypeMatchType_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 10, 1, 4),
    _Layer7NewCfgContentClassFileTypeMatchType_Type()
)
layer7NewCfgContentClassFileTypeMatchType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    layer7NewCfgContentClassFileTypeMatchType.setStatus("current")


class _Layer7NewCfgContentClassFileTypeCase_Type(Integer32):
    """Custom type layer7NewCfgContentClassFileTypeCase based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Layer7NewCfgContentClassFileTypeCase_Type.__name__ = "Integer32"
_Layer7NewCfgContentClassFileTypeCase_Object = MibTableColumn
layer7NewCfgContentClassFileTypeCase = _Layer7NewCfgContentClassFileTypeCase_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 10, 1, 5),
    _Layer7NewCfgContentClassFileTypeCase_Type()
)
layer7NewCfgContentClassFileTypeCase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    layer7NewCfgContentClassFileTypeCase.setStatus("current")


class _Layer7NewCfgContentClassFileTypeDelete_Type(Integer32):
    """Custom type layer7NewCfgContentClassFileTypeDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delete", 2),
          ("other", 1))
    )


_Layer7NewCfgContentClassFileTypeDelete_Type.__name__ = "Integer32"
_Layer7NewCfgContentClassFileTypeDelete_Object = MibTableColumn
layer7NewCfgContentClassFileTypeDelete = _Layer7NewCfgContentClassFileTypeDelete_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 10, 1, 6),
    _Layer7NewCfgContentClassFileTypeDelete_Type()
)
layer7NewCfgContentClassFileTypeDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    layer7NewCfgContentClassFileTypeDelete.setStatus("current")
_Layer7CurCfgContentClassHeaderTable_Object = MibTable
layer7CurCfgContentClassHeaderTable = _Layer7CurCfgContentClassHeaderTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 11)
)
if mibBuilder.loadTexts:
    layer7CurCfgContentClassHeaderTable.setStatus("current")
_Layer7CurCfgContentClassHeaderEntry_Object = MibTableRow
layer7CurCfgContentClassHeaderEntry = _Layer7CurCfgContentClassHeaderEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 11, 1)
)
layer7CurCfgContentClassHeaderEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-LAYER7-MIB", "layer7CurCfgContentClassHeaderContentClassID"),
    (0, "ALTEON-CHEETAH-LAYER7-MIB", "layer7CurCfgContentClassHeaderID"),
)
if mibBuilder.loadTexts:
    layer7CurCfgContentClassHeaderEntry.setStatus("current")


class _Layer7CurCfgContentClassHeaderContentClassID_Type(DisplayString):
    """Custom type layer7CurCfgContentClassHeaderContentClassID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Layer7CurCfgContentClassHeaderContentClassID_Type.__name__ = "DisplayString"
_Layer7CurCfgContentClassHeaderContentClassID_Object = MibTableColumn
layer7CurCfgContentClassHeaderContentClassID = _Layer7CurCfgContentClassHeaderContentClassID_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 11, 1, 1),
    _Layer7CurCfgContentClassHeaderContentClassID_Type()
)
layer7CurCfgContentClassHeaderContentClassID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgContentClassHeaderContentClassID.setStatus("current")


class _Layer7CurCfgContentClassHeaderID_Type(DisplayString):
    """Custom type layer7CurCfgContentClassHeaderID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Layer7CurCfgContentClassHeaderID_Type.__name__ = "DisplayString"
_Layer7CurCfgContentClassHeaderID_Object = MibTableColumn
layer7CurCfgContentClassHeaderID = _Layer7CurCfgContentClassHeaderID_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 11, 1, 2),
    _Layer7CurCfgContentClassHeaderID_Type()
)
layer7CurCfgContentClassHeaderID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgContentClassHeaderID.setStatus("current")


class _Layer7CurCfgContentClassHeaderName_Type(DisplayString):
    """Custom type layer7CurCfgContentClassHeaderName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_Layer7CurCfgContentClassHeaderName_Type.__name__ = "DisplayString"
_Layer7CurCfgContentClassHeaderName_Object = MibTableColumn
layer7CurCfgContentClassHeaderName = _Layer7CurCfgContentClassHeaderName_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 11, 1, 3),
    _Layer7CurCfgContentClassHeaderName_Type()
)
layer7CurCfgContentClassHeaderName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgContentClassHeaderName.setStatus("current")


class _Layer7CurCfgContentClassHeaderVal_Type(DisplayString):
    """Custom type layer7CurCfgContentClassHeaderVal based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_Layer7CurCfgContentClassHeaderVal_Type.__name__ = "DisplayString"
_Layer7CurCfgContentClassHeaderVal_Object = MibTableColumn
layer7CurCfgContentClassHeaderVal = _Layer7CurCfgContentClassHeaderVal_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 11, 1, 4),
    _Layer7CurCfgContentClassHeaderVal_Type()
)
layer7CurCfgContentClassHeaderVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgContentClassHeaderVal.setStatus("current")


class _Layer7CurCfgContentClassHeaderMatchTypeName_Type(Integer32):
    """Custom type layer7CurCfgContentClassHeaderMatchTypeName based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("equal", 3),
          ("include", 4),
          ("regex", 5))
    )


_Layer7CurCfgContentClassHeaderMatchTypeName_Type.__name__ = "Integer32"
_Layer7CurCfgContentClassHeaderMatchTypeName_Object = MibTableColumn
layer7CurCfgContentClassHeaderMatchTypeName = _Layer7CurCfgContentClassHeaderMatchTypeName_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 11, 1, 5),
    _Layer7CurCfgContentClassHeaderMatchTypeName_Type()
)
layer7CurCfgContentClassHeaderMatchTypeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgContentClassHeaderMatchTypeName.setStatus("current")


class _Layer7CurCfgContentClassHeaderMatchTypeVal_Type(Integer32):
    """Custom type layer7CurCfgContentClassHeaderMatchTypeVal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("equal", 3),
          ("include", 4),
          ("regex", 5))
    )


_Layer7CurCfgContentClassHeaderMatchTypeVal_Type.__name__ = "Integer32"
_Layer7CurCfgContentClassHeaderMatchTypeVal_Object = MibTableColumn
layer7CurCfgContentClassHeaderMatchTypeVal = _Layer7CurCfgContentClassHeaderMatchTypeVal_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 11, 1, 6),
    _Layer7CurCfgContentClassHeaderMatchTypeVal_Type()
)
layer7CurCfgContentClassHeaderMatchTypeVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgContentClassHeaderMatchTypeVal.setStatus("current")


class _Layer7CurCfgContentClassHeaderCase_Type(Integer32):
    """Custom type layer7CurCfgContentClassHeaderCase based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Layer7CurCfgContentClassHeaderCase_Type.__name__ = "Integer32"
_Layer7CurCfgContentClassHeaderCase_Object = MibTableColumn
layer7CurCfgContentClassHeaderCase = _Layer7CurCfgContentClassHeaderCase_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 11, 1, 7),
    _Layer7CurCfgContentClassHeaderCase_Type()
)
layer7CurCfgContentClassHeaderCase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgContentClassHeaderCase.setStatus("current")
_Layer7NewCfgContentClassHeaderTable_Object = MibTable
layer7NewCfgContentClassHeaderTable = _Layer7NewCfgContentClassHeaderTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 12)
)
if mibBuilder.loadTexts:
    layer7NewCfgContentClassHeaderTable.setStatus("current")
_Layer7NewCfgContentClassHeaderEntry_Object = MibTableRow
layer7NewCfgContentClassHeaderEntry = _Layer7NewCfgContentClassHeaderEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 12, 1)
)
layer7NewCfgContentClassHeaderEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-LAYER7-MIB", "layer7NewCfgContentClassHeaderContentClassID"),
    (0, "ALTEON-CHEETAH-LAYER7-MIB", "layer7NewCfgContentClassHeaderID"),
)
if mibBuilder.loadTexts:
    layer7NewCfgContentClassHeaderEntry.setStatus("current")


class _Layer7NewCfgContentClassHeaderContentClassID_Type(DisplayString):
    """Custom type layer7NewCfgContentClassHeaderContentClassID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Layer7NewCfgContentClassHeaderContentClassID_Type.__name__ = "DisplayString"
_Layer7NewCfgContentClassHeaderContentClassID_Object = MibTableColumn
layer7NewCfgContentClassHeaderContentClassID = _Layer7NewCfgContentClassHeaderContentClassID_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 12, 1, 1),
    _Layer7NewCfgContentClassHeaderContentClassID_Type()
)
layer7NewCfgContentClassHeaderContentClassID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    layer7NewCfgContentClassHeaderContentClassID.setStatus("current")


class _Layer7NewCfgContentClassHeaderID_Type(DisplayString):
    """Custom type layer7NewCfgContentClassHeaderID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Layer7NewCfgContentClassHeaderID_Type.__name__ = "DisplayString"
_Layer7NewCfgContentClassHeaderID_Object = MibTableColumn
layer7NewCfgContentClassHeaderID = _Layer7NewCfgContentClassHeaderID_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 12, 1, 2),
    _Layer7NewCfgContentClassHeaderID_Type()
)
layer7NewCfgContentClassHeaderID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    layer7NewCfgContentClassHeaderID.setStatus("current")


class _Layer7NewCfgContentClassHeaderName_Type(DisplayString):
    """Custom type layer7NewCfgContentClassHeaderName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_Layer7NewCfgContentClassHeaderName_Type.__name__ = "DisplayString"
_Layer7NewCfgContentClassHeaderName_Object = MibTableColumn
layer7NewCfgContentClassHeaderName = _Layer7NewCfgContentClassHeaderName_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 12, 1, 3),
    _Layer7NewCfgContentClassHeaderName_Type()
)
layer7NewCfgContentClassHeaderName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    layer7NewCfgContentClassHeaderName.setStatus("current")


class _Layer7NewCfgContentClassHeaderVal_Type(DisplayString):
    """Custom type layer7NewCfgContentClassHeaderVal based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_Layer7NewCfgContentClassHeaderVal_Type.__name__ = "DisplayString"
_Layer7NewCfgContentClassHeaderVal_Object = MibTableColumn
layer7NewCfgContentClassHeaderVal = _Layer7NewCfgContentClassHeaderVal_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 12, 1, 4),
    _Layer7NewCfgContentClassHeaderVal_Type()
)
layer7NewCfgContentClassHeaderVal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    layer7NewCfgContentClassHeaderVal.setStatus("current")


class _Layer7NewCfgContentClassHeaderMatchTypeName_Type(Integer32):
    """Custom type layer7NewCfgContentClassHeaderMatchTypeName based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("equal", 3),
          ("include", 4),
          ("regex", 5))
    )


_Layer7NewCfgContentClassHeaderMatchTypeName_Type.__name__ = "Integer32"
_Layer7NewCfgContentClassHeaderMatchTypeName_Object = MibTableColumn
layer7NewCfgContentClassHeaderMatchTypeName = _Layer7NewCfgContentClassHeaderMatchTypeName_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 12, 1, 5),
    _Layer7NewCfgContentClassHeaderMatchTypeName_Type()
)
layer7NewCfgContentClassHeaderMatchTypeName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    layer7NewCfgContentClassHeaderMatchTypeName.setStatus("current")


class _Layer7NewCfgContentClassHeaderMatchTypeVal_Type(Integer32):
    """Custom type layer7NewCfgContentClassHeaderMatchTypeVal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("equal", 3),
          ("include", 4),
          ("regex", 5))
    )


_Layer7NewCfgContentClassHeaderMatchTypeVal_Type.__name__ = "Integer32"
_Layer7NewCfgContentClassHeaderMatchTypeVal_Object = MibTableColumn
layer7NewCfgContentClassHeaderMatchTypeVal = _Layer7NewCfgContentClassHeaderMatchTypeVal_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 12, 1, 6),
    _Layer7NewCfgContentClassHeaderMatchTypeVal_Type()
)
layer7NewCfgContentClassHeaderMatchTypeVal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    layer7NewCfgContentClassHeaderMatchTypeVal.setStatus("current")


class _Layer7NewCfgContentClassHeaderCase_Type(Integer32):
    """Custom type layer7NewCfgContentClassHeaderCase based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Layer7NewCfgContentClassHeaderCase_Type.__name__ = "Integer32"
_Layer7NewCfgContentClassHeaderCase_Object = MibTableColumn
layer7NewCfgContentClassHeaderCase = _Layer7NewCfgContentClassHeaderCase_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 12, 1, 7),
    _Layer7NewCfgContentClassHeaderCase_Type()
)
layer7NewCfgContentClassHeaderCase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    layer7NewCfgContentClassHeaderCase.setStatus("current")


class _Layer7NewCfgContentClassHeaderDelete_Type(Integer32):
    """Custom type layer7NewCfgContentClassHeaderDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delete", 2),
          ("other", 1))
    )


_Layer7NewCfgContentClassHeaderDelete_Type.__name__ = "Integer32"
_Layer7NewCfgContentClassHeaderDelete_Object = MibTableColumn
layer7NewCfgContentClassHeaderDelete = _Layer7NewCfgContentClassHeaderDelete_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 12, 1, 8),
    _Layer7NewCfgContentClassHeaderDelete_Type()
)
layer7NewCfgContentClassHeaderDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    layer7NewCfgContentClassHeaderDelete.setStatus("current")
_Layer7CurCfgContentClassCookieTable_Object = MibTable
layer7CurCfgContentClassCookieTable = _Layer7CurCfgContentClassCookieTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 13)
)
if mibBuilder.loadTexts:
    layer7CurCfgContentClassCookieTable.setStatus("current")
_Layer7CurCfgContentClassCookieEntry_Object = MibTableRow
layer7CurCfgContentClassCookieEntry = _Layer7CurCfgContentClassCookieEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 13, 1)
)
layer7CurCfgContentClassCookieEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-LAYER7-MIB", "layer7CurCfgContentClassCookieContentClassID"),
    (0, "ALTEON-CHEETAH-LAYER7-MIB", "layer7CurCfgContentClassCookieID"),
)
if mibBuilder.loadTexts:
    layer7CurCfgContentClassCookieEntry.setStatus("current")


class _Layer7CurCfgContentClassCookieContentClassID_Type(DisplayString):
    """Custom type layer7CurCfgContentClassCookieContentClassID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Layer7CurCfgContentClassCookieContentClassID_Type.__name__ = "DisplayString"
_Layer7CurCfgContentClassCookieContentClassID_Object = MibTableColumn
layer7CurCfgContentClassCookieContentClassID = _Layer7CurCfgContentClassCookieContentClassID_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 13, 1, 1),
    _Layer7CurCfgContentClassCookieContentClassID_Type()
)
layer7CurCfgContentClassCookieContentClassID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgContentClassCookieContentClassID.setStatus("current")


class _Layer7CurCfgContentClassCookieID_Type(DisplayString):
    """Custom type layer7CurCfgContentClassCookieID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Layer7CurCfgContentClassCookieID_Type.__name__ = "DisplayString"
_Layer7CurCfgContentClassCookieID_Object = MibTableColumn
layer7CurCfgContentClassCookieID = _Layer7CurCfgContentClassCookieID_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 13, 1, 2),
    _Layer7CurCfgContentClassCookieID_Type()
)
layer7CurCfgContentClassCookieID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgContentClassCookieID.setStatus("current")


class _Layer7CurCfgContentClassCookieKey_Type(DisplayString):
    """Custom type layer7CurCfgContentClassCookieKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_Layer7CurCfgContentClassCookieKey_Type.__name__ = "DisplayString"
_Layer7CurCfgContentClassCookieKey_Object = MibTableColumn
layer7CurCfgContentClassCookieKey = _Layer7CurCfgContentClassCookieKey_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 13, 1, 3),
    _Layer7CurCfgContentClassCookieKey_Type()
)
layer7CurCfgContentClassCookieKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgContentClassCookieKey.setStatus("current")


class _Layer7CurCfgContentClassCookieVal_Type(DisplayString):
    """Custom type layer7CurCfgContentClassCookieVal based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_Layer7CurCfgContentClassCookieVal_Type.__name__ = "DisplayString"
_Layer7CurCfgContentClassCookieVal_Object = MibTableColumn
layer7CurCfgContentClassCookieVal = _Layer7CurCfgContentClassCookieVal_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 13, 1, 4),
    _Layer7CurCfgContentClassCookieVal_Type()
)
layer7CurCfgContentClassCookieVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgContentClassCookieVal.setStatus("current")


class _Layer7CurCfgContentClassCookieMatchTypeKey_Type(Integer32):
    """Custom type layer7CurCfgContentClassCookieMatchTypeKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("equal", 3),
          ("include", 4),
          ("regex", 5))
    )


_Layer7CurCfgContentClassCookieMatchTypeKey_Type.__name__ = "Integer32"
_Layer7CurCfgContentClassCookieMatchTypeKey_Object = MibTableColumn
layer7CurCfgContentClassCookieMatchTypeKey = _Layer7CurCfgContentClassCookieMatchTypeKey_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 13, 1, 5),
    _Layer7CurCfgContentClassCookieMatchTypeKey_Type()
)
layer7CurCfgContentClassCookieMatchTypeKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgContentClassCookieMatchTypeKey.setStatus("current")


class _Layer7CurCfgContentClassCookieMatchTypeVal_Type(Integer32):
    """Custom type layer7CurCfgContentClassCookieMatchTypeVal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("equal", 3),
          ("include", 4),
          ("regex", 5))
    )


_Layer7CurCfgContentClassCookieMatchTypeVal_Type.__name__ = "Integer32"
_Layer7CurCfgContentClassCookieMatchTypeVal_Object = MibTableColumn
layer7CurCfgContentClassCookieMatchTypeVal = _Layer7CurCfgContentClassCookieMatchTypeVal_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 13, 1, 6),
    _Layer7CurCfgContentClassCookieMatchTypeVal_Type()
)
layer7CurCfgContentClassCookieMatchTypeVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgContentClassCookieMatchTypeVal.setStatus("current")


class _Layer7CurCfgContentClassCookieCase_Type(Integer32):
    """Custom type layer7CurCfgContentClassCookieCase based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Layer7CurCfgContentClassCookieCase_Type.__name__ = "Integer32"
_Layer7CurCfgContentClassCookieCase_Object = MibTableColumn
layer7CurCfgContentClassCookieCase = _Layer7CurCfgContentClassCookieCase_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 13, 1, 7),
    _Layer7CurCfgContentClassCookieCase_Type()
)
layer7CurCfgContentClassCookieCase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgContentClassCookieCase.setStatus("current")
_Layer7NewCfgContentClassCookieTable_Object = MibTable
layer7NewCfgContentClassCookieTable = _Layer7NewCfgContentClassCookieTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 14)
)
if mibBuilder.loadTexts:
    layer7NewCfgContentClassCookieTable.setStatus("current")
_Layer7NewCfgContentClassCookieEntry_Object = MibTableRow
layer7NewCfgContentClassCookieEntry = _Layer7NewCfgContentClassCookieEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 14, 1)
)
layer7NewCfgContentClassCookieEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-LAYER7-MIB", "layer7NewCfgContentClassCookieContentClassID"),
    (0, "ALTEON-CHEETAH-LAYER7-MIB", "layer7NewCfgContentClassCookieID"),
)
if mibBuilder.loadTexts:
    layer7NewCfgContentClassCookieEntry.setStatus("current")


class _Layer7NewCfgContentClassCookieContentClassID_Type(DisplayString):
    """Custom type layer7NewCfgContentClassCookieContentClassID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Layer7NewCfgContentClassCookieContentClassID_Type.__name__ = "DisplayString"
_Layer7NewCfgContentClassCookieContentClassID_Object = MibTableColumn
layer7NewCfgContentClassCookieContentClassID = _Layer7NewCfgContentClassCookieContentClassID_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 14, 1, 1),
    _Layer7NewCfgContentClassCookieContentClassID_Type()
)
layer7NewCfgContentClassCookieContentClassID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7NewCfgContentClassCookieContentClassID.setStatus("current")


class _Layer7NewCfgContentClassCookieID_Type(DisplayString):
    """Custom type layer7NewCfgContentClassCookieID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Layer7NewCfgContentClassCookieID_Type.__name__ = "DisplayString"
_Layer7NewCfgContentClassCookieID_Object = MibTableColumn
layer7NewCfgContentClassCookieID = _Layer7NewCfgContentClassCookieID_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 14, 1, 2),
    _Layer7NewCfgContentClassCookieID_Type()
)
layer7NewCfgContentClassCookieID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7NewCfgContentClassCookieID.setStatus("current")


class _Layer7NewCfgContentClassCookieKey_Type(DisplayString):
    """Custom type layer7NewCfgContentClassCookieKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_Layer7NewCfgContentClassCookieKey_Type.__name__ = "DisplayString"
_Layer7NewCfgContentClassCookieKey_Object = MibTableColumn
layer7NewCfgContentClassCookieKey = _Layer7NewCfgContentClassCookieKey_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 14, 1, 3),
    _Layer7NewCfgContentClassCookieKey_Type()
)
layer7NewCfgContentClassCookieKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    layer7NewCfgContentClassCookieKey.setStatus("current")


class _Layer7NewCfgContentClassCookieVal_Type(DisplayString):
    """Custom type layer7NewCfgContentClassCookieVal based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_Layer7NewCfgContentClassCookieVal_Type.__name__ = "DisplayString"
_Layer7NewCfgContentClassCookieVal_Object = MibTableColumn
layer7NewCfgContentClassCookieVal = _Layer7NewCfgContentClassCookieVal_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 14, 1, 4),
    _Layer7NewCfgContentClassCookieVal_Type()
)
layer7NewCfgContentClassCookieVal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    layer7NewCfgContentClassCookieVal.setStatus("current")


class _Layer7NewCfgContentClassCookieMatchTypeKey_Type(Integer32):
    """Custom type layer7NewCfgContentClassCookieMatchTypeKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("equal", 3),
          ("include", 4),
          ("regex", 5))
    )


_Layer7NewCfgContentClassCookieMatchTypeKey_Type.__name__ = "Integer32"
_Layer7NewCfgContentClassCookieMatchTypeKey_Object = MibTableColumn
layer7NewCfgContentClassCookieMatchTypeKey = _Layer7NewCfgContentClassCookieMatchTypeKey_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 14, 1, 5),
    _Layer7NewCfgContentClassCookieMatchTypeKey_Type()
)
layer7NewCfgContentClassCookieMatchTypeKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    layer7NewCfgContentClassCookieMatchTypeKey.setStatus("current")


class _Layer7NewCfgContentClassCookieMatchTypeVal_Type(Integer32):
    """Custom type layer7NewCfgContentClassCookieMatchTypeVal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("equal", 3),
          ("include", 4),
          ("regex", 5))
    )


_Layer7NewCfgContentClassCookieMatchTypeVal_Type.__name__ = "Integer32"
_Layer7NewCfgContentClassCookieMatchTypeVal_Object = MibTableColumn
layer7NewCfgContentClassCookieMatchTypeVal = _Layer7NewCfgContentClassCookieMatchTypeVal_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 14, 1, 6),
    _Layer7NewCfgContentClassCookieMatchTypeVal_Type()
)
layer7NewCfgContentClassCookieMatchTypeVal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    layer7NewCfgContentClassCookieMatchTypeVal.setStatus("current")


class _Layer7NewCfgContentClassCookieCase_Type(Integer32):
    """Custom type layer7NewCfgContentClassCookieCase based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Layer7NewCfgContentClassCookieCase_Type.__name__ = "Integer32"
_Layer7NewCfgContentClassCookieCase_Object = MibTableColumn
layer7NewCfgContentClassCookieCase = _Layer7NewCfgContentClassCookieCase_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 14, 1, 7),
    _Layer7NewCfgContentClassCookieCase_Type()
)
layer7NewCfgContentClassCookieCase.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    layer7NewCfgContentClassCookieCase.setStatus("current")


class _Layer7NewCfgContentClassCookieDelete_Type(Integer32):
    """Custom type layer7NewCfgContentClassCookieDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delete", 2),
          ("other", 1))
    )


_Layer7NewCfgContentClassCookieDelete_Type.__name__ = "Integer32"
_Layer7NewCfgContentClassCookieDelete_Object = MibTableColumn
layer7NewCfgContentClassCookieDelete = _Layer7NewCfgContentClassCookieDelete_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 14, 1, 8),
    _Layer7NewCfgContentClassCookieDelete_Type()
)
layer7NewCfgContentClassCookieDelete.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    layer7NewCfgContentClassCookieDelete.setStatus("current")
_Layer7CurCfgContentClassTextTable_Object = MibTable
layer7CurCfgContentClassTextTable = _Layer7CurCfgContentClassTextTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 15)
)
if mibBuilder.loadTexts:
    layer7CurCfgContentClassTextTable.setStatus("current")
_Layer7CurCfgContentClassTextEntry_Object = MibTableRow
layer7CurCfgContentClassTextEntry = _Layer7CurCfgContentClassTextEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 15, 1)
)
layer7CurCfgContentClassTextEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-LAYER7-MIB", "layer7CurCfgContentClassTextContentClassID"),
    (0, "ALTEON-CHEETAH-LAYER7-MIB", "layer7CurCfgContentClassTextID"),
)
if mibBuilder.loadTexts:
    layer7CurCfgContentClassTextEntry.setStatus("current")


class _Layer7CurCfgContentClassTextContentClassID_Type(DisplayString):
    """Custom type layer7CurCfgContentClassTextContentClassID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Layer7CurCfgContentClassTextContentClassID_Type.__name__ = "DisplayString"
_Layer7CurCfgContentClassTextContentClassID_Object = MibTableColumn
layer7CurCfgContentClassTextContentClassID = _Layer7CurCfgContentClassTextContentClassID_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 15, 1, 1),
    _Layer7CurCfgContentClassTextContentClassID_Type()
)
layer7CurCfgContentClassTextContentClassID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgContentClassTextContentClassID.setStatus("current")


class _Layer7CurCfgContentClassTextID_Type(DisplayString):
    """Custom type layer7CurCfgContentClassTextID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Layer7CurCfgContentClassTextID_Type.__name__ = "DisplayString"
_Layer7CurCfgContentClassTextID_Object = MibTableColumn
layer7CurCfgContentClassTextID = _Layer7CurCfgContentClassTextID_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 15, 1, 2),
    _Layer7CurCfgContentClassTextID_Type()
)
layer7CurCfgContentClassTextID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgContentClassTextID.setStatus("current")


class _Layer7CurCfgContentClassTextText_Type(DisplayString):
    """Custom type layer7CurCfgContentClassTextText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_Layer7CurCfgContentClassTextText_Type.__name__ = "DisplayString"
_Layer7CurCfgContentClassTextText_Object = MibTableColumn
layer7CurCfgContentClassTextText = _Layer7CurCfgContentClassTextText_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 15, 1, 3),
    _Layer7CurCfgContentClassTextText_Type()
)
layer7CurCfgContentClassTextText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgContentClassTextText.setStatus("current")


class _Layer7CurCfgContentClassTextMatchType_Type(Integer32):
    """Custom type layer7CurCfgContentClassTextMatchType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("include", 4),
          ("regex", 5))
    )


_Layer7CurCfgContentClassTextMatchType_Type.__name__ = "Integer32"
_Layer7CurCfgContentClassTextMatchType_Object = MibTableColumn
layer7CurCfgContentClassTextMatchType = _Layer7CurCfgContentClassTextMatchType_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 15, 1, 4),
    _Layer7CurCfgContentClassTextMatchType_Type()
)
layer7CurCfgContentClassTextMatchType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgContentClassTextMatchType.setStatus("current")


class _Layer7CurCfgContentClassTextLookupArea_Type(Integer32):
    """Custom type layer7CurCfgContentClassTextLookupArea based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("body", 2),
          ("both", 3),
          ("header", 1))
    )


_Layer7CurCfgContentClassTextLookupArea_Type.__name__ = "Integer32"
_Layer7CurCfgContentClassTextLookupArea_Object = MibTableColumn
layer7CurCfgContentClassTextLookupArea = _Layer7CurCfgContentClassTextLookupArea_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 15, 1, 5),
    _Layer7CurCfgContentClassTextLookupArea_Type()
)
layer7CurCfgContentClassTextLookupArea.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgContentClassTextLookupArea.setStatus("current")


class _Layer7CurCfgContentClassTextCase_Type(Integer32):
    """Custom type layer7CurCfgContentClassTextCase based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Layer7CurCfgContentClassTextCase_Type.__name__ = "Integer32"
_Layer7CurCfgContentClassTextCase_Object = MibTableColumn
layer7CurCfgContentClassTextCase = _Layer7CurCfgContentClassTextCase_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 15, 1, 6),
    _Layer7CurCfgContentClassTextCase_Type()
)
layer7CurCfgContentClassTextCase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgContentClassTextCase.setStatus("current")
_Layer7NewCfgContentClassTextTable_Object = MibTable
layer7NewCfgContentClassTextTable = _Layer7NewCfgContentClassTextTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 16)
)
if mibBuilder.loadTexts:
    layer7NewCfgContentClassTextTable.setStatus("current")
_Layer7NewCfgContentClassTextEntry_Object = MibTableRow
layer7NewCfgContentClassTextEntry = _Layer7NewCfgContentClassTextEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 16, 1)
)
layer7NewCfgContentClassTextEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-LAYER7-MIB", "layer7NewCfgContentClassTextContentClassID"),
    (0, "ALTEON-CHEETAH-LAYER7-MIB", "layer7NewCfgContentClassTextID"),
)
if mibBuilder.loadTexts:
    layer7NewCfgContentClassTextEntry.setStatus("current")


class _Layer7NewCfgContentClassTextContentClassID_Type(DisplayString):
    """Custom type layer7NewCfgContentClassTextContentClassID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Layer7NewCfgContentClassTextContentClassID_Type.__name__ = "DisplayString"
_Layer7NewCfgContentClassTextContentClassID_Object = MibTableColumn
layer7NewCfgContentClassTextContentClassID = _Layer7NewCfgContentClassTextContentClassID_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 16, 1, 1),
    _Layer7NewCfgContentClassTextContentClassID_Type()
)
layer7NewCfgContentClassTextContentClassID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7NewCfgContentClassTextContentClassID.setStatus("current")


class _Layer7NewCfgContentClassTextID_Type(DisplayString):
    """Custom type layer7NewCfgContentClassTextID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Layer7NewCfgContentClassTextID_Type.__name__ = "DisplayString"
_Layer7NewCfgContentClassTextID_Object = MibTableColumn
layer7NewCfgContentClassTextID = _Layer7NewCfgContentClassTextID_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 16, 1, 2),
    _Layer7NewCfgContentClassTextID_Type()
)
layer7NewCfgContentClassTextID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7NewCfgContentClassTextID.setStatus("current")


class _Layer7NewCfgContentClassTextText_Type(DisplayString):
    """Custom type layer7NewCfgContentClassTextText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_Layer7NewCfgContentClassTextText_Type.__name__ = "DisplayString"
_Layer7NewCfgContentClassTextText_Object = MibTableColumn
layer7NewCfgContentClassTextText = _Layer7NewCfgContentClassTextText_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 16, 1, 3),
    _Layer7NewCfgContentClassTextText_Type()
)
layer7NewCfgContentClassTextText.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    layer7NewCfgContentClassTextText.setStatus("current")


class _Layer7NewCfgContentClassTextMatchType_Type(Integer32):
    """Custom type layer7NewCfgContentClassTextMatchType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("include", 4),
          ("regex", 5))
    )


_Layer7NewCfgContentClassTextMatchType_Type.__name__ = "Integer32"
_Layer7NewCfgContentClassTextMatchType_Object = MibTableColumn
layer7NewCfgContentClassTextMatchType = _Layer7NewCfgContentClassTextMatchType_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 16, 1, 4),
    _Layer7NewCfgContentClassTextMatchType_Type()
)
layer7NewCfgContentClassTextMatchType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    layer7NewCfgContentClassTextMatchType.setStatus("current")


class _Layer7NewCfgContentClassTextLookupArea_Type(Integer32):
    """Custom type layer7NewCfgContentClassTextLookupArea based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("body", 2),
          ("both", 3),
          ("header", 1))
    )


_Layer7NewCfgContentClassTextLookupArea_Type.__name__ = "Integer32"
_Layer7NewCfgContentClassTextLookupArea_Object = MibTableColumn
layer7NewCfgContentClassTextLookupArea = _Layer7NewCfgContentClassTextLookupArea_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 16, 1, 5),
    _Layer7NewCfgContentClassTextLookupArea_Type()
)
layer7NewCfgContentClassTextLookupArea.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    layer7NewCfgContentClassTextLookupArea.setStatus("current")


class _Layer7NewCfgContentClassTextCase_Type(Integer32):
    """Custom type layer7NewCfgContentClassTextCase based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Layer7NewCfgContentClassTextCase_Type.__name__ = "Integer32"
_Layer7NewCfgContentClassTextCase_Object = MibTableColumn
layer7NewCfgContentClassTextCase = _Layer7NewCfgContentClassTextCase_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 16, 1, 6),
    _Layer7NewCfgContentClassTextCase_Type()
)
layer7NewCfgContentClassTextCase.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    layer7NewCfgContentClassTextCase.setStatus("current")


class _Layer7NewCfgContentClassTextDelete_Type(Integer32):
    """Custom type layer7NewCfgContentClassTextDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delete", 2),
          ("other", 1))
    )


_Layer7NewCfgContentClassTextDelete_Type.__name__ = "Integer32"
_Layer7NewCfgContentClassTextDelete_Object = MibTableColumn
layer7NewCfgContentClassTextDelete = _Layer7NewCfgContentClassTextDelete_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 16, 1, 7),
    _Layer7NewCfgContentClassTextDelete_Type()
)
layer7NewCfgContentClassTextDelete.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    layer7NewCfgContentClassTextDelete.setStatus("current")
_Layer7CurCfgContentClassXmlTable_Object = MibTable
layer7CurCfgContentClassXmlTable = _Layer7CurCfgContentClassXmlTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 17)
)
if mibBuilder.loadTexts:
    layer7CurCfgContentClassXmlTable.setStatus("current")
_Layer7CurCfgContentClassXmlEntry_Object = MibTableRow
layer7CurCfgContentClassXmlEntry = _Layer7CurCfgContentClassXmlEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 17, 1)
)
layer7CurCfgContentClassXmlEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-LAYER7-MIB", "layer7CurCfgContentClassXmlTagContentClassID"),
    (0, "ALTEON-CHEETAH-LAYER7-MIB", "layer7CurCfgContentClassXmlTagID"),
)
if mibBuilder.loadTexts:
    layer7CurCfgContentClassXmlEntry.setStatus("current")


class _Layer7CurCfgContentClassXmlTagContentClassID_Type(DisplayString):
    """Custom type layer7CurCfgContentClassXmlTagContentClassID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Layer7CurCfgContentClassXmlTagContentClassID_Type.__name__ = "DisplayString"
_Layer7CurCfgContentClassXmlTagContentClassID_Object = MibTableColumn
layer7CurCfgContentClassXmlTagContentClassID = _Layer7CurCfgContentClassXmlTagContentClassID_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 17, 1, 1),
    _Layer7CurCfgContentClassXmlTagContentClassID_Type()
)
layer7CurCfgContentClassXmlTagContentClassID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgContentClassXmlTagContentClassID.setStatus("current")


class _Layer7CurCfgContentClassXmlTagID_Type(DisplayString):
    """Custom type layer7CurCfgContentClassXmlTagID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Layer7CurCfgContentClassXmlTagID_Type.__name__ = "DisplayString"
_Layer7CurCfgContentClassXmlTagID_Object = MibTableColumn
layer7CurCfgContentClassXmlTagID = _Layer7CurCfgContentClassXmlTagID_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 17, 1, 2),
    _Layer7CurCfgContentClassXmlTagID_Type()
)
layer7CurCfgContentClassXmlTagID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgContentClassXmlTagID.setStatus("current")


class _Layer7CurCfgContentClassXmlTagName_Type(DisplayString):
    """Custom type layer7CurCfgContentClassXmlTagName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_Layer7CurCfgContentClassXmlTagName_Type.__name__ = "DisplayString"
_Layer7CurCfgContentClassXmlTagName_Object = MibTableColumn
layer7CurCfgContentClassXmlTagName = _Layer7CurCfgContentClassXmlTagName_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 17, 1, 3),
    _Layer7CurCfgContentClassXmlTagName_Type()
)
layer7CurCfgContentClassXmlTagName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgContentClassXmlTagName.setStatus("current")


class _Layer7CurCfgContentClassXmlTagVal_Type(DisplayString):
    """Custom type layer7CurCfgContentClassXmlTagVal based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_Layer7CurCfgContentClassXmlTagVal_Type.__name__ = "DisplayString"
_Layer7CurCfgContentClassXmlTagVal_Object = MibTableColumn
layer7CurCfgContentClassXmlTagVal = _Layer7CurCfgContentClassXmlTagVal_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 17, 1, 4),
    _Layer7CurCfgContentClassXmlTagVal_Type()
)
layer7CurCfgContentClassXmlTagVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgContentClassXmlTagVal.setStatus("current")


class _Layer7CurCfgContentClassXmlTagMatchTypeName_Type(Integer32):
    """Custom type layer7CurCfgContentClassXmlTagMatchTypeName based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("equal", 3),
          ("sufx", 1))
    )


_Layer7CurCfgContentClassXmlTagMatchTypeName_Type.__name__ = "Integer32"
_Layer7CurCfgContentClassXmlTagMatchTypeName_Object = MibTableColumn
layer7CurCfgContentClassXmlTagMatchTypeName = _Layer7CurCfgContentClassXmlTagMatchTypeName_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 17, 1, 5),
    _Layer7CurCfgContentClassXmlTagMatchTypeName_Type()
)
layer7CurCfgContentClassXmlTagMatchTypeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgContentClassXmlTagMatchTypeName.setStatus("current")


class _Layer7CurCfgContentClassXmlTagMatchTypeVal_Type(Integer32):
    """Custom type layer7CurCfgContentClassXmlTagMatchTypeVal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("equal", 3),
          ("include", 4),
          ("sufx", 1))
    )


_Layer7CurCfgContentClassXmlTagMatchTypeVal_Type.__name__ = "Integer32"
_Layer7CurCfgContentClassXmlTagMatchTypeVal_Object = MibTableColumn
layer7CurCfgContentClassXmlTagMatchTypeVal = _Layer7CurCfgContentClassXmlTagMatchTypeVal_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 17, 1, 6),
    _Layer7CurCfgContentClassXmlTagMatchTypeVal_Type()
)
layer7CurCfgContentClassXmlTagMatchTypeVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgContentClassXmlTagMatchTypeVal.setStatus("current")


class _Layer7CurCfgContentClassXmlTagCase_Type(Integer32):
    """Custom type layer7CurCfgContentClassXmlTagCase based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Layer7CurCfgContentClassXmlTagCase_Type.__name__ = "Integer32"
_Layer7CurCfgContentClassXmlTagCase_Object = MibTableColumn
layer7CurCfgContentClassXmlTagCase = _Layer7CurCfgContentClassXmlTagCase_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 17, 1, 7),
    _Layer7CurCfgContentClassXmlTagCase_Type()
)
layer7CurCfgContentClassXmlTagCase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgContentClassXmlTagCase.setStatus("current")
_Layer7NewCfgContentClassXmlTable_Object = MibTable
layer7NewCfgContentClassXmlTable = _Layer7NewCfgContentClassXmlTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 18)
)
if mibBuilder.loadTexts:
    layer7NewCfgContentClassXmlTable.setStatus("current")
_Layer7NewCfgContentClassXmlEntry_Object = MibTableRow
layer7NewCfgContentClassXmlEntry = _Layer7NewCfgContentClassXmlEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 18, 1)
)
layer7NewCfgContentClassXmlEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-LAYER7-MIB", "layer7NewCfgContentClassXmlTagContentClassID"),
    (0, "ALTEON-CHEETAH-LAYER7-MIB", "layer7NewCfgContentClassXmlTagID"),
)
if mibBuilder.loadTexts:
    layer7NewCfgContentClassXmlEntry.setStatus("current")


class _Layer7NewCfgContentClassXmlTagContentClassID_Type(DisplayString):
    """Custom type layer7NewCfgContentClassXmlTagContentClassID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Layer7NewCfgContentClassXmlTagContentClassID_Type.__name__ = "DisplayString"
_Layer7NewCfgContentClassXmlTagContentClassID_Object = MibTableColumn
layer7NewCfgContentClassXmlTagContentClassID = _Layer7NewCfgContentClassXmlTagContentClassID_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 18, 1, 1),
    _Layer7NewCfgContentClassXmlTagContentClassID_Type()
)
layer7NewCfgContentClassXmlTagContentClassID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7NewCfgContentClassXmlTagContentClassID.setStatus("current")


class _Layer7NewCfgContentClassXmlTagID_Type(DisplayString):
    """Custom type layer7NewCfgContentClassXmlTagID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Layer7NewCfgContentClassXmlTagID_Type.__name__ = "DisplayString"
_Layer7NewCfgContentClassXmlTagID_Object = MibTableColumn
layer7NewCfgContentClassXmlTagID = _Layer7NewCfgContentClassXmlTagID_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 18, 1, 2),
    _Layer7NewCfgContentClassXmlTagID_Type()
)
layer7NewCfgContentClassXmlTagID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7NewCfgContentClassXmlTagID.setStatus("current")


class _Layer7NewCfgContentClassXmlTagName_Type(DisplayString):
    """Custom type layer7NewCfgContentClassXmlTagName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_Layer7NewCfgContentClassXmlTagName_Type.__name__ = "DisplayString"
_Layer7NewCfgContentClassXmlTagName_Object = MibTableColumn
layer7NewCfgContentClassXmlTagName = _Layer7NewCfgContentClassXmlTagName_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 18, 1, 3),
    _Layer7NewCfgContentClassXmlTagName_Type()
)
layer7NewCfgContentClassXmlTagName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    layer7NewCfgContentClassXmlTagName.setStatus("current")


class _Layer7NewCfgContentClassXmlTagVal_Type(DisplayString):
    """Custom type layer7NewCfgContentClassXmlTagVal based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_Layer7NewCfgContentClassXmlTagVal_Type.__name__ = "DisplayString"
_Layer7NewCfgContentClassXmlTagVal_Object = MibTableColumn
layer7NewCfgContentClassXmlTagVal = _Layer7NewCfgContentClassXmlTagVal_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 18, 1, 4),
    _Layer7NewCfgContentClassXmlTagVal_Type()
)
layer7NewCfgContentClassXmlTagVal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    layer7NewCfgContentClassXmlTagVal.setStatus("current")


class _Layer7NewCfgContentClassXmlTagMatchTypeName_Type(Integer32):
    """Custom type layer7NewCfgContentClassXmlTagMatchTypeName based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("equal", 3),
          ("sufx", 1))
    )


_Layer7NewCfgContentClassXmlTagMatchTypeName_Type.__name__ = "Integer32"
_Layer7NewCfgContentClassXmlTagMatchTypeName_Object = MibTableColumn
layer7NewCfgContentClassXmlTagMatchTypeName = _Layer7NewCfgContentClassXmlTagMatchTypeName_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 18, 1, 5),
    _Layer7NewCfgContentClassXmlTagMatchTypeName_Type()
)
layer7NewCfgContentClassXmlTagMatchTypeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    layer7NewCfgContentClassXmlTagMatchTypeName.setStatus("current")


class _Layer7NewCfgContentClassXmlTagMatchTypeVal_Type(Integer32):
    """Custom type layer7NewCfgContentClassXmlTagMatchTypeVal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("equal", 3),
          ("include", 4),
          ("sufx", 1))
    )


_Layer7NewCfgContentClassXmlTagMatchTypeVal_Type.__name__ = "Integer32"
_Layer7NewCfgContentClassXmlTagMatchTypeVal_Object = MibTableColumn
layer7NewCfgContentClassXmlTagMatchTypeVal = _Layer7NewCfgContentClassXmlTagMatchTypeVal_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 18, 1, 6),
    _Layer7NewCfgContentClassXmlTagMatchTypeVal_Type()
)
layer7NewCfgContentClassXmlTagMatchTypeVal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    layer7NewCfgContentClassXmlTagMatchTypeVal.setStatus("current")


class _Layer7NewCfgContentClassXmlTagCase_Type(Integer32):
    """Custom type layer7NewCfgContentClassXmlTagCase based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Layer7NewCfgContentClassXmlTagCase_Type.__name__ = "Integer32"
_Layer7NewCfgContentClassXmlTagCase_Object = MibTableColumn
layer7NewCfgContentClassXmlTagCase = _Layer7NewCfgContentClassXmlTagCase_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 18, 1, 7),
    _Layer7NewCfgContentClassXmlTagCase_Type()
)
layer7NewCfgContentClassXmlTagCase.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    layer7NewCfgContentClassXmlTagCase.setStatus("current")


class _Layer7NewCfgContentClassXmlTagDelete_Type(Integer32):
    """Custom type layer7NewCfgContentClassXmlTagDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delete", 2),
          ("other", 1))
    )


_Layer7NewCfgContentClassXmlTagDelete_Type.__name__ = "Integer32"
_Layer7NewCfgContentClassXmlTagDelete_Object = MibTableColumn
layer7NewCfgContentClassXmlTagDelete = _Layer7NewCfgContentClassXmlTagDelete_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 6, 18, 1, 8),
    _Layer7NewCfgContentClassXmlTagDelete_Type()
)
layer7NewCfgContentClassXmlTagDelete.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    layer7NewCfgContentClassXmlTagDelete.setStatus("current")
_Layer7Stats_ObjectIdentity = ObjectIdentity
layer7Stats = _Layer7Stats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 2)
)
_UrlStats_ObjectIdentity = ObjectIdentity
urlStats = _UrlStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 2, 1)
)
_UrlRedirStats_ObjectIdentity = ObjectIdentity
urlRedirStats = _UrlRedirStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 2, 1, 1)
)
_UrlStatRedRedirs_Type = Counter32
_UrlStatRedRedirs_Object = MibScalar
urlStatRedRedirs = _UrlStatRedRedirs_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 2, 1, 1, 1),
    _UrlStatRedRedirs_Type()
)
urlStatRedRedirs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    urlStatRedRedirs.setStatus("current")
_UrlStatRedOrigSrvs_Type = Counter32
_UrlStatRedOrigSrvs_Object = MibScalar
urlStatRedOrigSrvs = _UrlStatRedOrigSrvs_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 2, 1, 1, 2),
    _UrlStatRedOrigSrvs_Type()
)
urlStatRedOrigSrvs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    urlStatRedOrigSrvs.setStatus("current")
_UrlStatRedNonGets_Type = Counter32
_UrlStatRedNonGets_Object = MibScalar
urlStatRedNonGets = _UrlStatRedNonGets_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 2, 1, 1, 3),
    _UrlStatRedNonGets_Type()
)
urlStatRedNonGets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    urlStatRedNonGets.setStatus("current")
_UrlStatRedCookie_Type = Counter32
_UrlStatRedCookie_Object = MibScalar
urlStatRedCookie = _UrlStatRedCookie_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 2, 1, 1, 4),
    _UrlStatRedCookie_Type()
)
urlStatRedCookie.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    urlStatRedCookie.setStatus("current")
_UrlStatRedNoCache_Type = Counter32
_UrlStatRedNoCache_Object = MibScalar
urlStatRedNoCache = _UrlStatRedNoCache_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 2, 1, 1, 5),
    _UrlStatRedNoCache_Type()
)
urlStatRedNoCache.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    urlStatRedNoCache.setStatus("current")
_UrlStatRedStraightOrigSrvs_Type = Counter32
_UrlStatRedStraightOrigSrvs_Object = MibScalar
urlStatRedStraightOrigSrvs = _UrlStatRedStraightOrigSrvs_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 2, 1, 1, 6),
    _UrlStatRedStraightOrigSrvs_Type()
)
urlStatRedStraightOrigSrvs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    urlStatRedStraightOrigSrvs.setStatus("current")
_UrlStatRedRtspCacheSrvs_Type = Counter32
_UrlStatRedRtspCacheSrvs_Object = MibScalar
urlStatRedRtspCacheSrvs = _UrlStatRedRtspCacheSrvs_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 2, 1, 1, 7),
    _UrlStatRedRtspCacheSrvs_Type()
)
urlStatRedRtspCacheSrvs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    urlStatRedRtspCacheSrvs.setStatus("current")
_UrlStatRedRtspOrigSrvs_Type = Counter32
_UrlStatRedRtspOrigSrvs_Object = MibScalar
urlStatRedRtspOrigSrvs = _UrlStatRedRtspOrigSrvs_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 2, 1, 1, 8),
    _UrlStatRedRtspOrigSrvs_Type()
)
urlStatRedRtspOrigSrvs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    urlStatRedRtspOrigSrvs.setStatus("current")
_UrlSlbStats_ObjectIdentity = ObjectIdentity
urlSlbStats = _UrlSlbStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 2, 1, 2)
)
_UrlStatSlbPathTable_Object = MibTable
urlStatSlbPathTable = _UrlStatSlbPathTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    urlStatSlbPathTable.setStatus("current")
_UrlStatSlbPathTableEntry_Object = MibTableRow
urlStatSlbPathTableEntry = _UrlStatSlbPathTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 2, 1, 2, 1, 1)
)
urlStatSlbPathTableEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-LAYER7-MIB", "urlStatSlbPathIndex"),
)
if mibBuilder.loadTexts:
    urlStatSlbPathTableEntry.setStatus("current")
_UrlStatSlbPathIndex_Type = Integer32
_UrlStatSlbPathIndex_Object = MibTableColumn
urlStatSlbPathIndex = _UrlStatSlbPathIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 2, 1, 2, 1, 1, 1),
    _UrlStatSlbPathIndex_Type()
)
urlStatSlbPathIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    urlStatSlbPathIndex.setStatus("current")
_UrlStatSlbPathHits_Type = Counter32
_UrlStatSlbPathHits_Object = MibTableColumn
urlStatSlbPathHits = _UrlStatSlbPathHits_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 2, 1, 2, 1, 1, 2),
    _UrlStatSlbPathHits_Type()
)
urlStatSlbPathHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    urlStatSlbPathHits.setStatus("current")
_UrlMaintStats_ObjectIdentity = ObjectIdentity
urlMaintStats = _UrlMaintStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 2, 1, 3)
)
_UrlMaintStatClientReset_Type = Counter32
_UrlMaintStatClientReset_Object = MibScalar
urlMaintStatClientReset = _UrlMaintStatClientReset_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 2, 1, 3, 1),
    _UrlMaintStatClientReset_Type()
)
urlMaintStatClientReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    urlMaintStatClientReset.setStatus("current")
_UrlMaintStatServerReset_Type = Counter32
_UrlMaintStatServerReset_Object = MibScalar
urlMaintStatServerReset = _UrlMaintStatServerReset_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 2, 1, 3, 2),
    _UrlMaintStatServerReset_Type()
)
urlMaintStatServerReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    urlMaintStatServerReset.setStatus("current")
_UrlMaintStatConnSplicing_Type = Counter32
_UrlMaintStatConnSplicing_Object = MibScalar
urlMaintStatConnSplicing = _UrlMaintStatConnSplicing_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 2, 1, 3, 3),
    _UrlMaintStatConnSplicing_Type()
)
urlMaintStatConnSplicing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    urlMaintStatConnSplicing.setStatus("current")
_UrlMaintStatHalfOpens_Type = Gauge32
_UrlMaintStatHalfOpens_Object = MibScalar
urlMaintStatHalfOpens = _UrlMaintStatHalfOpens_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 2, 1, 3, 4),
    _UrlMaintStatHalfOpens_Type()
)
urlMaintStatHalfOpens.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    urlMaintStatHalfOpens.setStatus("current")
_UrlMaintStatSwitchRetries_Type = Counter32
_UrlMaintStatSwitchRetries_Object = MibScalar
urlMaintStatSwitchRetries = _UrlMaintStatSwitchRetries_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 2, 1, 3, 5),
    _UrlMaintStatSwitchRetries_Type()
)
urlMaintStatSwitchRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    urlMaintStatSwitchRetries.setStatus("current")
_UrlMaintStatRandomEarlyDrops_Type = Counter32
_UrlMaintStatRandomEarlyDrops_Object = MibScalar
urlMaintStatRandomEarlyDrops = _UrlMaintStatRandomEarlyDrops_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 2, 1, 3, 6),
    _UrlMaintStatRandomEarlyDrops_Type()
)
urlMaintStatRandomEarlyDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    urlMaintStatRandomEarlyDrops.setStatus("current")
_UrlMaintStatReqTooLong_Type = Counter32
_UrlMaintStatReqTooLong_Object = MibScalar
urlMaintStatReqTooLong = _UrlMaintStatReqTooLong_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 2, 1, 3, 7),
    _UrlMaintStatReqTooLong_Type()
)
urlMaintStatReqTooLong.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    urlMaintStatReqTooLong.setStatus("current")
_UrlMaintStatInvalidHandshakes_Type = Counter32
_UrlMaintStatInvalidHandshakes_Object = MibScalar
urlMaintStatInvalidHandshakes = _UrlMaintStatInvalidHandshakes_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 2, 1, 3, 8),
    _UrlMaintStatInvalidHandshakes_Type()
)
urlMaintStatInvalidHandshakes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    urlMaintStatInvalidHandshakes.setStatus("current")
_UrlMaintStatCurSPMemUnits_Type = Gauge32
_UrlMaintStatCurSPMemUnits_Object = MibScalar
urlMaintStatCurSPMemUnits = _UrlMaintStatCurSPMemUnits_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 2, 1, 3, 9),
    _UrlMaintStatCurSPMemUnits_Type()
)
urlMaintStatCurSPMemUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    urlMaintStatCurSPMemUnits.setStatus("current")
_UrlMaintStatCurSEQBufEntries_Type = Gauge32
_UrlMaintStatCurSEQBufEntries_Object = MibScalar
urlMaintStatCurSEQBufEntries = _UrlMaintStatCurSEQBufEntries_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 2, 1, 3, 10),
    _UrlMaintStatCurSEQBufEntries_Type()
)
urlMaintStatCurSEQBufEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    urlMaintStatCurSEQBufEntries.setStatus("current")
_UrlMaintStatHighestSEQBufEntries_Type = Counter32
_UrlMaintStatHighestSEQBufEntries_Object = MibScalar
urlMaintStatHighestSEQBufEntries = _UrlMaintStatHighestSEQBufEntries_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 2, 1, 3, 11),
    _UrlMaintStatHighestSEQBufEntries_Type()
)
urlMaintStatHighestSEQBufEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    urlMaintStatHighestSEQBufEntries.setStatus("current")
_UrlMaintStatCurDataBufUse_Type = Gauge32
_UrlMaintStatCurDataBufUse_Object = MibScalar
urlMaintStatCurDataBufUse = _UrlMaintStatCurDataBufUse_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 2, 1, 3, 12),
    _UrlMaintStatCurDataBufUse_Type()
)
urlMaintStatCurDataBufUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    urlMaintStatCurDataBufUse.setStatus("current")
_UrlMaintStatHighestDataBufUse_Type = Counter32
_UrlMaintStatHighestDataBufUse_Object = MibScalar
urlMaintStatHighestDataBufUse = _UrlMaintStatHighestDataBufUse_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 2, 1, 3, 13),
    _UrlMaintStatHighestDataBufUse_Type()
)
urlMaintStatHighestDataBufUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    urlMaintStatHighestDataBufUse.setStatus("current")
_UrlMaintStatCurSPBufEntries_Type = Gauge32
_UrlMaintStatCurSPBufEntries_Object = MibScalar
urlMaintStatCurSPBufEntries = _UrlMaintStatCurSPBufEntries_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 2, 1, 3, 14),
    _UrlMaintStatCurSPBufEntries_Type()
)
urlMaintStatCurSPBufEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    urlMaintStatCurSPBufEntries.setStatus("current")
_UrlMaintStatHighestSPBufEntries_Type = Counter32
_UrlMaintStatHighestSPBufEntries_Object = MibScalar
urlMaintStatHighestSPBufEntries = _UrlMaintStatHighestSPBufEntries_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 2, 1, 3, 15),
    _UrlMaintStatHighestSPBufEntries_Type()
)
urlMaintStatHighestSPBufEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    urlMaintStatHighestSPBufEntries.setStatus("current")
_UrlMaintStatTotalNonZeroSEQAlloc_Type = Counter32
_UrlMaintStatTotalNonZeroSEQAlloc_Object = MibScalar
urlMaintStatTotalNonZeroSEQAlloc = _UrlMaintStatTotalNonZeroSEQAlloc_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 2, 1, 3, 16),
    _UrlMaintStatTotalNonZeroSEQAlloc_Type()
)
urlMaintStatTotalNonZeroSEQAlloc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    urlMaintStatTotalNonZeroSEQAlloc.setStatus("current")
_UrlMaintStatTotalSEQBufAllocs_Type = Counter32
_UrlMaintStatTotalSEQBufAllocs_Object = MibScalar
urlMaintStatTotalSEQBufAllocs = _UrlMaintStatTotalSEQBufAllocs_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 2, 1, 3, 17),
    _UrlMaintStatTotalSEQBufAllocs_Type()
)
urlMaintStatTotalSEQBufAllocs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    urlMaintStatTotalSEQBufAllocs.setStatus("current")
_UrlMaintStatTotalSEQBufFrees_Type = Counter32
_UrlMaintStatTotalSEQBufFrees_Object = MibScalar
urlMaintStatTotalSEQBufFrees = _UrlMaintStatTotalSEQBufFrees_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 2, 1, 3, 18),
    _UrlMaintStatTotalSEQBufFrees_Type()
)
urlMaintStatTotalSEQBufFrees.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    urlMaintStatTotalSEQBufFrees.setStatus("current")
_UrlMaintStatTotalDataBufAllocs_Type = Counter32
_UrlMaintStatTotalDataBufAllocs_Object = MibScalar
urlMaintStatTotalDataBufAllocs = _UrlMaintStatTotalDataBufAllocs_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 2, 1, 3, 19),
    _UrlMaintStatTotalDataBufAllocs_Type()
)
urlMaintStatTotalDataBufAllocs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    urlMaintStatTotalDataBufAllocs.setStatus("current")
_UrlMaintStatTotalDataBufFrees_Type = Counter32
_UrlMaintStatTotalDataBufFrees_Object = MibScalar
urlMaintStatTotalDataBufFrees = _UrlMaintStatTotalDataBufFrees_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 2, 1, 3, 20),
    _UrlMaintStatTotalDataBufFrees_Type()
)
urlMaintStatTotalDataBufFrees.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    urlMaintStatTotalDataBufFrees.setStatus("current")
_UrlMaintStatSeqBufAllocFails_Type = Counter32
_UrlMaintStatSeqBufAllocFails_Object = MibScalar
urlMaintStatSeqBufAllocFails = _UrlMaintStatSeqBufAllocFails_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 2, 1, 3, 21),
    _UrlMaintStatSeqBufAllocFails_Type()
)
urlMaintStatSeqBufAllocFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    urlMaintStatSeqBufAllocFails.setStatus("current")
_UrlMaintStatUBufAllocFails_Type = Counter32
_UrlMaintStatUBufAllocFails_Object = MibScalar
urlMaintStatUBufAllocFails = _UrlMaintStatUBufAllocFails_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 2, 1, 3, 22),
    _UrlMaintStatUBufAllocFails_Type()
)
urlMaintStatUBufAllocFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    urlMaintStatUBufAllocFails.setStatus("current")
_UrlMaintStatMaxSessPerBucket_Type = Counter32
_UrlMaintStatMaxSessPerBucket_Object = MibScalar
urlMaintStatMaxSessPerBucket = _UrlMaintStatMaxSessPerBucket_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 2, 1, 3, 23),
    _UrlMaintStatMaxSessPerBucket_Type()
)
urlMaintStatMaxSessPerBucket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    urlMaintStatMaxSessPerBucket.setStatus("current")
_UrlMaintStatMaxFramesPerSess_Type = Counter32
_UrlMaintStatMaxFramesPerSess_Object = MibScalar
urlMaintStatMaxFramesPerSess = _UrlMaintStatMaxFramesPerSess_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 2, 1, 3, 24),
    _UrlMaintStatMaxFramesPerSess_Type()
)
urlMaintStatMaxFramesPerSess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    urlMaintStatMaxFramesPerSess.setStatus("current")
_UrlMaintStatMaxBytesBuffered_Type = Counter32
_UrlMaintStatMaxBytesBuffered_Object = MibScalar
urlMaintStatMaxBytesBuffered = _UrlMaintStatMaxBytesBuffered_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 2, 1, 3, 25),
    _UrlMaintStatMaxBytesBuffered_Type()
)
urlMaintStatMaxBytesBuffered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    urlMaintStatMaxBytesBuffered.setStatus("current")
_UrlMaintStatInvalidMethods_Type = Counter32
_UrlMaintStatInvalidMethods_Object = MibScalar
urlMaintStatInvalidMethods = _UrlMaintStatInvalidMethods_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 2, 1, 3, 26),
    _UrlMaintStatInvalidMethods_Type()
)
urlMaintStatInvalidMethods.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    urlMaintStatInvalidMethods.setStatus("current")
_UrlMaintStatAgedSessions_Type = Counter32
_UrlMaintStatAgedSessions_Object = MibScalar
urlMaintStatAgedSessions = _UrlMaintStatAgedSessions_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 2, 1, 3, 27),
    _UrlMaintStatAgedSessions_Type()
)
urlMaintStatAgedSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    urlMaintStatAgedSessions.setStatus("current")
_UrlMaintStatLowestSPMemUnits_Type = Gauge32
_UrlMaintStatLowestSPMemUnits_Object = MibScalar
urlMaintStatLowestSPMemUnits = _UrlMaintStatLowestSPMemUnits_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 2, 1, 3, 28),
    _UrlMaintStatLowestSPMemUnits_Type()
)
urlMaintStatLowestSPMemUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    urlMaintStatLowestSPMemUnits.setStatus("current")
_UrlSpMaintStatsTable_Object = MibTable
urlSpMaintStatsTable = _UrlSpMaintStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 2, 1, 4)
)
if mibBuilder.loadTexts:
    urlSpMaintStatsTable.setStatus("current")
_UrlSpMaintStatsTableEntry_Object = MibTableRow
urlSpMaintStatsTableEntry = _UrlSpMaintStatsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 2, 1, 4, 1)
)
urlSpMaintStatsTableEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-LAYER7-MIB", "urlSpMaintStatsSpIndex"),
)
if mibBuilder.loadTexts:
    urlSpMaintStatsTableEntry.setStatus("current")
_UrlSpMaintStatsSpIndex_Type = Integer32
_UrlSpMaintStatsSpIndex_Object = MibTableColumn
urlSpMaintStatsSpIndex = _UrlSpMaintStatsSpIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 2, 1, 4, 1, 1),
    _UrlSpMaintStatsSpIndex_Type()
)
urlSpMaintStatsSpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    urlSpMaintStatsSpIndex.setStatus("current")
_UrlSpMaintStatsCurMemUnits_Type = Gauge32
_UrlSpMaintStatsCurMemUnits_Object = MibTableColumn
urlSpMaintStatsCurMemUnits = _UrlSpMaintStatsCurMemUnits_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 2, 1, 4, 1, 2),
    _UrlSpMaintStatsCurMemUnits_Type()
)
urlSpMaintStatsCurMemUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    urlSpMaintStatsCurMemUnits.setStatus("current")
_UrlSpMaintStatsLowestMemUnits_Type = Gauge32
_UrlSpMaintStatsLowestMemUnits_Object = MibTableColumn
urlSpMaintStatsLowestMemUnits = _UrlSpMaintStatsLowestMemUnits_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 2, 1, 4, 1, 3),
    _UrlSpMaintStatsLowestMemUnits_Type()
)
urlSpMaintStatsLowestMemUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    urlSpMaintStatsLowestMemUnits.setStatus("current")
_ConnPoolingStats_ObjectIdentity = ObjectIdentity
connPoolingStats = _ConnPoolingStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 2, 2)
)
_CurrOpenedServerConns_Type = Counter32
_CurrOpenedServerConns_Object = MibScalar
currOpenedServerConns = _CurrOpenedServerConns_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 2, 2, 1),
    _CurrOpenedServerConns_Type()
)
currOpenedServerConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currOpenedServerConns.setStatus("current")
_ActiveServerConns_Type = Gauge32
_ActiveServerConns_Object = MibScalar
activeServerConns = _ActiveServerConns_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 2, 2, 2),
    _ActiveServerConns_Type()
)
activeServerConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeServerConns.setStatus("current")
_AvailServerConns_Type = Gauge32
_AvailServerConns_Object = MibScalar
availServerConns = _AvailServerConns_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 2, 2, 3),
    _AvailServerConns_Type()
)
availServerConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    availServerConns.setStatus("current")
_AgedOutClientConns_Type = Counter32
_AgedOutClientConns_Object = MibScalar
agedOutClientConns = _AgedOutClientConns_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 2, 2, 4),
    _AgedOutClientConns_Type()
)
agedOutClientConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agedOutClientConns.setStatus("current")
_AgedOutServerConns_Type = Counter32
_AgedOutServerConns_Object = MibScalar
agedOutServerConns = _AgedOutServerConns_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 2, 2, 5),
    _AgedOutServerConns_Type()
)
agedOutServerConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agedOutServerConns.setStatus("current")
_Layer7Info_ObjectIdentity = ObjectIdentity
layer7Info = _Layer7Info_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 3)
)
_SlbParsing_ObjectIdentity = ObjectIdentity
slbParsing = _SlbParsing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 3, 1)
)


class _SlbParsingString_Type(DisplayString):
    """Custom type slbParsingString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 78),
    )


_SlbParsingString_Type.__name__ = "DisplayString"
_SlbParsingString_Object = MibScalar
slbParsingString = _SlbParsingString_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 3, 1, 1),
    _SlbParsingString_Type()
)
slbParsingString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbParsingString.setStatus("current")


class _SlbParsingVip_Type(DisplayString):
    """Custom type slbParsingVip based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 46),
    )


_SlbParsingVip_Type.__name__ = "DisplayString"
_SlbParsingVip_Object = MibScalar
slbParsingVip = _SlbParsingVip_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 3, 1, 2),
    _SlbParsingVip_Type()
)
slbParsingVip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbParsingVip.setStatus("current")


class _SlbParsingRip_Type(DisplayString):
    """Custom type slbParsingRip based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 46),
    )


_SlbParsingRip_Type.__name__ = "DisplayString"
_SlbParsingRip_Object = MibScalar
slbParsingRip = _SlbParsingRip_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 3, 1, 3),
    _SlbParsingRip_Type()
)
slbParsingRip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbParsingRip.setStatus("current")


class _SlbParsingRport_Type(Integer32):
    """Custom type slbParsingRport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SlbParsingRport_Type.__name__ = "Integer32"
_SlbParsingRport_Object = MibScalar
slbParsingRport = _SlbParsingRport_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 3, 1, 4),
    _SlbParsingRport_Type()
)
slbParsingRport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbParsingRport.setStatus("current")


class _SlbParsingCip_Type(DisplayString):
    """Custom type slbParsingCip based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 46),
    )


_SlbParsingCip_Type.__name__ = "DisplayString"
_SlbParsingCip_Object = MibScalar
slbParsingCip = _SlbParsingCip_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 3, 1, 5),
    _SlbParsingCip_Type()
)
slbParsingCip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbParsingCip.setStatus("current")
_Layer7Oper_ObjectIdentity = ObjectIdentity
layer7Oper = _Layer7Oper_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 4)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALTEON-CHEETAH-LAYER7-MIB",
    **{"layer7": layer7,
       "layer7Configs": layer7Configs,
       "urlCfg": urlCfg,
       "slbUrlRedir": slbUrlRedir,
       "slbCurCfgUrlRedirNonGetOrigSrv": slbCurCfgUrlRedirNonGetOrigSrv,
       "slbNewCfgUrlRedirNonGetOrigSrv": slbNewCfgUrlRedirNonGetOrigSrv,
       "slbCurCfgUrlRedirCookieOrigSrv": slbCurCfgUrlRedirCookieOrigSrv,
       "slbNewCfgUrlRedirCookieOrigSrv": slbNewCfgUrlRedirCookieOrigSrv,
       "slbCurCfgUrlRedirNoCacheOrigSrv": slbCurCfgUrlRedirNoCacheOrigSrv,
       "slbNewCfgUrlRedirNoCacheOrigSrv": slbNewCfgUrlRedirNoCacheOrigSrv,
       "slbCurCfgUrlRedirUriHashLength": slbCurCfgUrlRedirUriHashLength,
       "slbNewCfgUrlRedirUriHashLength": slbNewCfgUrlRedirUriHashLength,
       "slbCurCfgUrlRedirHeader": slbCurCfgUrlRedirHeader,
       "slbNewCfgUrlRedirHeader": slbNewCfgUrlRedirHeader,
       "slbCurCfgUrlRedirHeaderName": slbCurCfgUrlRedirHeaderName,
       "slbNewCfgUrlRedirHeaderName": slbNewCfgUrlRedirHeaderName,
       "slbCurCfgUrlHashing": slbCurCfgUrlHashing,
       "slbNewCfgUrlHashing": slbNewCfgUrlHashing,
       "slbCurCfgUrlRedirHeaderNameType": slbCurCfgUrlRedirHeaderNameType,
       "slbNewCfgUrlRedirHeaderNameType": slbNewCfgUrlRedirHeaderNameType,
       "slbUrlBalance": slbUrlBalance,
       "slbUrlLbPathTableMaxSize": slbUrlLbPathTableMaxSize,
       "slbCurCfgUrlLbPathTable": slbCurCfgUrlLbPathTable,
       "slbCurCfgUrlLbPathTableEntry": slbCurCfgUrlLbPathTableEntry,
       "slbCurCfgUrlLbPathIndex": slbCurCfgUrlLbPathIndex,
       "slbCurCfgUrlLbPathString": slbCurCfgUrlLbPathString,
       "slbCurCfgUrlLbBwmContract": slbCurCfgUrlLbBwmContract,
       "slbCurCfgUrlLbPathHTTPHeader": slbCurCfgUrlLbPathHTTPHeader,
       "slbCurCfgUrlLbPathHTTPHeaderValue": slbCurCfgUrlLbPathHTTPHeaderValue,
       "slbCurCfgUrlLbPathPatternStringType": slbCurCfgUrlLbPathPatternStringType,
       "slbCurCfgUrlLbPathOffset": slbCurCfgUrlLbPathOffset,
       "slbCurCfgUrlLbPathDepth": slbCurCfgUrlLbPathDepth,
       "slbCurCfgUrlLbPathOper": slbCurCfgUrlLbPathOper,
       "slbCurCfgUrlLbPathDnsQueryTypes": slbCurCfgUrlLbPathDnsQueryTypes,
       "slbCurCfgUrlLbPathCompleteString": slbCurCfgUrlLbPathCompleteString,
       "slbCurCfgUrlLbPathAllowRegExp": slbCurCfgUrlLbPathAllowRegExp,
       "slbCurCfgUrlLbPathDnsType": slbCurCfgUrlLbPathDnsType,
       "slbCurCfgUrlLbPathApplication": slbCurCfgUrlLbPathApplication,
       "slbNewCfgUrlLbPathTable": slbNewCfgUrlLbPathTable,
       "slbNewCfgUrlLbPathTableEntry": slbNewCfgUrlLbPathTableEntry,
       "slbNewCfgUrlLbPathIndex": slbNewCfgUrlLbPathIndex,
       "slbNewCfgUrlLbPathString": slbNewCfgUrlLbPathString,
       "slbNewCfgUrlLbPathDelete": slbNewCfgUrlLbPathDelete,
       "slbNewCfgUrlLbBwmContract": slbNewCfgUrlLbBwmContract,
       "slbNewCfgUrlLbPathHTTPHeader": slbNewCfgUrlLbPathHTTPHeader,
       "slbNewCfgUrlLbPathHTTPHeaderValue": slbNewCfgUrlLbPathHTTPHeaderValue,
       "slbNewCfgUrlLbPathPatternStringType": slbNewCfgUrlLbPathPatternStringType,
       "slbNewCfgUrlLbPathOffset": slbNewCfgUrlLbPathOffset,
       "slbNewCfgUrlLbPathDepth": slbNewCfgUrlLbPathDepth,
       "slbNewCfgUrlLbPathOper": slbNewCfgUrlLbPathOper,
       "slbNewCfgUrlLbPathDnsQueryTypes": slbNewCfgUrlLbPathDnsQueryTypes,
       "slbNewCfgUrlLbPathCompleteString": slbNewCfgUrlLbPathCompleteString,
       "slbNewCfgUrlLbPathAllowRegExp": slbNewCfgUrlLbPathAllowRegExp,
       "slbNewCfgUrlLbPathDnsType": slbNewCfgUrlLbPathDnsType,
       "slbNewCfgUrlLbPathApplication": slbNewCfgUrlLbPathApplication,
       "slbCurCfgUrlLbErrorMsg": slbCurCfgUrlLbErrorMsg,
       "slbNewCfgUrlLbErrorMsg": slbNewCfgUrlLbErrorMsg,
       "slbCurCfgUrlLbCaseSensitiveStrMatch": slbCurCfgUrlLbCaseSensitiveStrMatch,
       "slbNewCfgUrlLbCaseSensitiveStrMatch": slbNewCfgUrlLbCaseSensitiveStrMatch,
       "slbUrlHttpMethods": slbUrlHttpMethods,
       "slbUrlHttpMethodsTableMaxSize": slbUrlHttpMethodsTableMaxSize,
       "slbCurCfgUrlHttpMethodsTable": slbCurCfgUrlHttpMethodsTable,
       "slbCurCfgUrlHttpMethodsTableEntry": slbCurCfgUrlHttpMethodsTableEntry,
       "slbCurCfgUrlHttpMethodIndex": slbCurCfgUrlHttpMethodIndex,
       "slbCurCfgUrlHttpMethodString": slbCurCfgUrlHttpMethodString,
       "slbNewCfgUrlHttpMethodsTable": slbNewCfgUrlHttpMethodsTable,
       "slbNewCfgUrlHttpMethodsTableEntry": slbNewCfgUrlHttpMethodsTableEntry,
       "slbNewCfgUrlHttpMethodIndex": slbNewCfgUrlHttpMethodIndex,
       "slbNewCfgUrlHttpMethodString": slbNewCfgUrlHttpMethodString,
       "slbNewCfgUrlHttpMethodDelete": slbNewCfgUrlHttpMethodDelete,
       "layer7GeneralCfg": layer7GeneralCfg,
       "layer7CurCfgDbindTimeout": layer7CurCfgDbindTimeout,
       "layer7NewCfgDbindTimeout": layer7NewCfgDbindTimeout,
       "sdpCfg": sdpCfg,
       "slbSdpTableMaxSize": slbSdpTableMaxSize,
       "slbCurCfgSdpTable": slbCurCfgSdpTable,
       "slbCurCfgSdpTableEntry": slbCurCfgSdpTableEntry,
       "slbCurCfgSdpIndex": slbCurCfgSdpIndex,
       "slbCurCfgSdpPrivAddr": slbCurCfgSdpPrivAddr,
       "slbCurCfgSdpPublicAddr": slbCurCfgSdpPublicAddr,
       "slbNewCfgSdpTable": slbNewCfgSdpTable,
       "slbNewCfgSdpTableEntry": slbNewCfgSdpTableEntry,
       "slbNewCfgSdpIndex": slbNewCfgSdpIndex,
       "slbNewCfgSdpPrivAddr": slbNewCfgSdpPrivAddr,
       "slbNewCfgSdpPublicAddr": slbNewCfgSdpPublicAddr,
       "slbNewCfgSdpDelete": slbNewCfgSdpDelete,
       "httpModCfg": httpModCfg,
       "layer7CurCfgHttpmodListTable": layer7CurCfgHttpmodListTable,
       "layer7CurCfgHttpmodListEntry": layer7CurCfgHttpmodListEntry,
       "layer7CurCfgHttpmodListNameIdIndex": layer7CurCfgHttpmodListNameIdIndex,
       "layer7CurCfgHttpmodListName": layer7CurCfgHttpmodListName,
       "layer7CurCfgHttpmodListAdminStatus": layer7CurCfgHttpmodListAdminStatus,
       "layer7NewCfgHttpmodListTable": layer7NewCfgHttpmodListTable,
       "layer7NewCfgHttpmodListEntry": layer7NewCfgHttpmodListEntry,
       "layer7NewCfgHttpmodListNameIdIndex": layer7NewCfgHttpmodListNameIdIndex,
       "layer7NewCfgHttpmodListName": layer7NewCfgHttpmodListName,
       "layer7NewCfgHttpmodListAdminStatus": layer7NewCfgHttpmodListAdminStatus,
       "layer7NewCfgHttpmodListCopy": layer7NewCfgHttpmodListCopy,
       "layer7NewCfgHttpmodListDelete": layer7NewCfgHttpmodListDelete,
       "layer7CurCfgHttpmodRuleTable": layer7CurCfgHttpmodRuleTable,
       "layer7CurCfgHttpmodRuleEntry": layer7CurCfgHttpmodRuleEntry,
       "layer7CurCfgHttpmodRuleListIdIndex": layer7CurCfgHttpmodRuleListIdIndex,
       "layer7CurCfgHttpmodRuleIndex": layer7CurCfgHttpmodRuleIndex,
       "layer7CurCfgHttpmodRuleName": layer7CurCfgHttpmodRuleName,
       "layer7CurCfgHttpmodRuleDirectn": layer7CurCfgHttpmodRuleDirectn,
       "layer7CurCfgHttpmodRuleAction": layer7CurCfgHttpmodRuleAction,
       "layer7CurCfgHttpmodRuleAdminStatus": layer7CurCfgHttpmodRuleAdminStatus,
       "layer7CurCfgHttpmodRuleElement": layer7CurCfgHttpmodRuleElement,
       "layer7CurCfgHttpmodRuleHttpBody": layer7CurCfgHttpmodRuleHttpBody,
       "layer7NewCfgHttpmodRuleTable": layer7NewCfgHttpmodRuleTable,
       "layer7NewCfgHttpmodRuleEntry": layer7NewCfgHttpmodRuleEntry,
       "layer7NewCfgHttpmodRuleListIdIndex": layer7NewCfgHttpmodRuleListIdIndex,
       "layer7NewCfgHttpmodRuleIndex": layer7NewCfgHttpmodRuleIndex,
       "layer7NewCfgHttpmodRuleName": layer7NewCfgHttpmodRuleName,
       "layer7NewCfgHttpmodRuleDirectn": layer7NewCfgHttpmodRuleDirectn,
       "layer7NewCfgHttpmodRuleAction": layer7NewCfgHttpmodRuleAction,
       "layer7NewCfgHttpmodRuleAdminStatus": layer7NewCfgHttpmodRuleAdminStatus,
       "layer7NewCfgHttpmodRuleCopy": layer7NewCfgHttpmodRuleCopy,
       "layer7NewCfgHttpmodRuleDelete": layer7NewCfgHttpmodRuleDelete,
       "layer7NewCfgHttpmodRuleElement": layer7NewCfgHttpmodRuleElement,
       "layer7NewCfgHttpmodRuleHttpBody": layer7NewCfgHttpmodRuleHttpBody,
       "layer7CurCfgHttpmodRuleUrlTable": layer7CurCfgHttpmodRuleUrlTable,
       "layer7CurCfgHttpmodRuleUrlEntry": layer7CurCfgHttpmodRuleUrlEntry,
       "layer7CurCfgHttpmodRuleUrlListIdIndex": layer7CurCfgHttpmodRuleUrlListIdIndex,
       "layer7CurCfgHttpmodRuleUrlIndex": layer7CurCfgHttpmodRuleUrlIndex,
       "layer7CurCfgHttpmodRuleUrlMtchProtcol": layer7CurCfgHttpmodRuleUrlMtchProtcol,
       "layer7CurCfgHttpmodRuleUrlMtchPort": layer7CurCfgHttpmodRuleUrlMtchPort,
       "layer7CurCfgHttpmodRuleUrlMtchHostTyp": layer7CurCfgHttpmodRuleUrlMtchHostTyp,
       "layer7CurCfgHttpmodRuleUrlMtchHost": layer7CurCfgHttpmodRuleUrlMtchHost,
       "layer7CurCfgHttpmodRuleUrlMtchPathTyp": layer7CurCfgHttpmodRuleUrlMtchPathTyp,
       "layer7CurCfgHttpmodRuleUrlMtchPath": layer7CurCfgHttpmodRuleUrlMtchPath,
       "layer7CurCfgHttpmodRuleUrlMtchPgName": layer7CurCfgHttpmodRuleUrlMtchPgName,
       "layer7CurCfgHttpmodRuleUrlMtchPgTyp": layer7CurCfgHttpmodRuleUrlMtchPgTyp,
       "layer7CurCfgHttpmodRuleUrlActnProtcl": layer7CurCfgHttpmodRuleUrlActnProtcl,
       "layer7CurCfgHttpmodRuleUrlActnPort": layer7CurCfgHttpmodRuleUrlActnPort,
       "layer7CurCfgHttpmodRuleUrlActnHostTyp": layer7CurCfgHttpmodRuleUrlActnHostTyp,
       "layer7CurCfgHttpmodRuleUrlActnHost": layer7CurCfgHttpmodRuleUrlActnHost,
       "layer7CurCfgHttpmodRuleUrlActnHstSec": layer7CurCfgHttpmodRuleUrlActnHstSec,
       "layer7CurCfgHttpmodRuleUrlActnHstRplc": layer7CurCfgHttpmodRuleUrlActnHstRplc,
       "layer7CurCfgHttpmodRuleUrlActnPathTyp": layer7CurCfgHttpmodRuleUrlActnPathTyp,
       "layer7CurCfgHttpmodRuleUrlActnPath": layer7CurCfgHttpmodRuleUrlActnPath,
       "layer7CurCfgHttpmodRuleUrlActnPthSctn": layer7CurCfgHttpmodRuleUrlActnPthSctn,
       "layer7CurCfgHttpmodRuleUrlActnPthRplc": layer7CurCfgHttpmodRuleUrlActnPthRplc,
       "layer7CurCfgHttpmodRuleUrlActnPgName": layer7CurCfgHttpmodRuleUrlActnPgName,
       "layer7CurCfgHttpmodRuleUrlActnPgTyp": layer7CurCfgHttpmodRuleUrlActnPgTyp,
       "layer7NewCfgHttpmodRuleUrlTable": layer7NewCfgHttpmodRuleUrlTable,
       "layer7NewCfgHttpmodRuleUrlEntry": layer7NewCfgHttpmodRuleUrlEntry,
       "layer7NewCfgHttpmodRuleUrlListIdIndex": layer7NewCfgHttpmodRuleUrlListIdIndex,
       "layer7NewCfgHttpmodRuleUrlIndex": layer7NewCfgHttpmodRuleUrlIndex,
       "layer7NewCfgHttpmodRuleUrlMtchProtcol": layer7NewCfgHttpmodRuleUrlMtchProtcol,
       "layer7NewCfgHttpmodRuleUrlMtchPort": layer7NewCfgHttpmodRuleUrlMtchPort,
       "layer7NewCfgHttpmodRuleUrlMtchHostTyp": layer7NewCfgHttpmodRuleUrlMtchHostTyp,
       "layer7NewCfgHttpmodRuleUrlMtchHost": layer7NewCfgHttpmodRuleUrlMtchHost,
       "layer7NewCfgHttpmodRuleUrlMtchPathTyp": layer7NewCfgHttpmodRuleUrlMtchPathTyp,
       "layer7NewCfgHttpmodRuleUrlMtchPath": layer7NewCfgHttpmodRuleUrlMtchPath,
       "layer7NewCfgHttpmodRuleUrlMtchPgName": layer7NewCfgHttpmodRuleUrlMtchPgName,
       "layer7NewCfgHttpmodRuleUrlMtchPgTyp": layer7NewCfgHttpmodRuleUrlMtchPgTyp,
       "layer7NewCfgHttpmodRuleUrlActnProtcl": layer7NewCfgHttpmodRuleUrlActnProtcl,
       "layer7NewCfgHttpmodRuleUrlActnPort": layer7NewCfgHttpmodRuleUrlActnPort,
       "layer7NewCfgHttpmodRuleUrlActnHostTyp": layer7NewCfgHttpmodRuleUrlActnHostTyp,
       "layer7NewCfgHttpmodRuleUrlActnHost": layer7NewCfgHttpmodRuleUrlActnHost,
       "layer7NewCfgHttpmodRuleUrlActnHstSec": layer7NewCfgHttpmodRuleUrlActnHstSec,
       "layer7NewCfgHttpmodRuleUrlActnHstRplc": layer7NewCfgHttpmodRuleUrlActnHstRplc,
       "layer7NewCfgHttpmodRuleUrlActnPathTyp": layer7NewCfgHttpmodRuleUrlActnPathTyp,
       "layer7NewCfgHttpmodRuleUrlActnPath": layer7NewCfgHttpmodRuleUrlActnPath,
       "layer7NewCfgHttpmodRuleUrlActnPthSctn": layer7NewCfgHttpmodRuleUrlActnPthSctn,
       "layer7NewCfgHttpmodRuleUrlActnPthRplc": layer7NewCfgHttpmodRuleUrlActnPthRplc,
       "layer7NewCfgHttpmodRuleUrlActnPgName": layer7NewCfgHttpmodRuleUrlActnPgName,
       "layer7NewCfgHttpmodRuleUrlActnPgTyp": layer7NewCfgHttpmodRuleUrlActnPgTyp,
       "layer7CurCfgHttpmodRuleHdrTable": layer7CurCfgHttpmodRuleHdrTable,
       "layer7CurCfgHttpmodRuleHdrEntry": layer7CurCfgHttpmodRuleHdrEntry,
       "layer7CurCfgHttpmodRuleHdrListIdIndex": layer7CurCfgHttpmodRuleHdrListIdIndex,
       "layer7CurCfgHttpmodRuleHdrIndex": layer7CurCfgHttpmodRuleHdrIndex,
       "layer7CurCfgHttpmodRuleHdrInsert": layer7CurCfgHttpmodRuleHdrInsert,
       "layer7CurCfgHttpmodRuleHdrValue": layer7CurCfgHttpmodRuleHdrValue,
       "layer7CurCfgHttpmodRuleHdrElmnt": layer7CurCfgHttpmodRuleHdrElmnt,
       "layer7CurCfgHttpmodRuleHdrElmntUrlHost": layer7CurCfgHttpmodRuleHdrElmntUrlHost,
       "layer7CurCfgHttpmodRuleHdrElmntUrlPath": layer7CurCfgHttpmodRuleHdrElmntUrlPath,
       "layer7CurCfgHttpmodRuleHdrElmntHdrField": layer7CurCfgHttpmodRuleHdrElmntHdrField,
       "layer7CurCfgHttpmodRuleHdrElmntHdrVal": layer7CurCfgHttpmodRuleHdrElmntHdrVal,
       "layer7CurCfgHttpmodRuleHdrElmntCookey": layer7CurCfgHttpmodRuleHdrElmntCookey,
       "layer7CurCfgHttpmodRuleHdrElmntCkieVal": layer7CurCfgHttpmodRuleHdrElmntCkieVal,
       "layer7CurCfgHttpmodRuleHdrElmntFileTyp": layer7CurCfgHttpmodRuleHdrElmntFileTyp,
       "layer7CurCfgHttpmodRuleHdrElmntStatusCode": layer7CurCfgHttpmodRuleHdrElmntStatusCode,
       "layer7CurCfgHttpmodRuleHdrElmntStatusTxt": layer7CurCfgHttpmodRuleHdrElmntStatusTxt,
       "layer7CurCfgHttpmodRuleHdrElmntTxt": layer7CurCfgHttpmodRuleHdrElmntTxt,
       "layer7CurCfgHttpmodRuleHdrElmntRegx": layer7CurCfgHttpmodRuleHdrElmntRegx,
       "layer7CurCfgHttpmodRuleHdrReplacHdr": layer7CurCfgHttpmodRuleHdrReplacHdr,
       "layer7CurCfgHttpmodRuleHdrReplacVal": layer7CurCfgHttpmodRuleHdrReplacVal,
       "layer7CurCfgHttpmodRuleHdrReplacNewHdr": layer7CurCfgHttpmodRuleHdrReplacNewHdr,
       "layer7CurCfgHttpmodRuleHdrReplacNewVal": layer7CurCfgHttpmodRuleHdrReplacNewVal,
       "layer7CurCfgHttpmodRuleHdrRemvHdr": layer7CurCfgHttpmodRuleHdrRemvHdr,
       "layer7CurCfgHttpmodRuleHdrRemvVal": layer7CurCfgHttpmodRuleHdrRemvVal,
       "layer7NewCfgHttpmodRuleHdrTable": layer7NewCfgHttpmodRuleHdrTable,
       "layer7NewCfgHttpmodRuleHdrEntry": layer7NewCfgHttpmodRuleHdrEntry,
       "layer7NewCfgHttpmodRuleHdrListIdIndex": layer7NewCfgHttpmodRuleHdrListIdIndex,
       "layer7NewCfgHttpmodRuleHdrIndex": layer7NewCfgHttpmodRuleHdrIndex,
       "layer7NewCfgHttpmodRuleHdrInsert": layer7NewCfgHttpmodRuleHdrInsert,
       "layer7NewCfgHttpmodRuleHdrValue": layer7NewCfgHttpmodRuleHdrValue,
       "layer7NewCfgHttpmodRuleHdrElmnt": layer7NewCfgHttpmodRuleHdrElmnt,
       "layer7NewCfgHttpmodRuleHdrElmntUrlHost": layer7NewCfgHttpmodRuleHdrElmntUrlHost,
       "layer7NewCfgHttpmodRuleHdrElmntUrlPath": layer7NewCfgHttpmodRuleHdrElmntUrlPath,
       "layer7NewCfgHttpmodRuleHdrElmntHdrField": layer7NewCfgHttpmodRuleHdrElmntHdrField,
       "layer7NewCfgHttpmodRuleHdrElmntHdrVal": layer7NewCfgHttpmodRuleHdrElmntHdrVal,
       "layer7NewCfgHttpmodRuleHdrElmntCookey": layer7NewCfgHttpmodRuleHdrElmntCookey,
       "layer7NewCfgHttpmodRuleHdrElmntCkieVal": layer7NewCfgHttpmodRuleHdrElmntCkieVal,
       "layer7NewCfgHttpmodRuleHdrElmntFileTyp": layer7NewCfgHttpmodRuleHdrElmntFileTyp,
       "layer7NewCfgHttpmodRuleHdrElmntStatusCode": layer7NewCfgHttpmodRuleHdrElmntStatusCode,
       "layer7NewCfgHttpmodRuleHdrElmntStatusTxt": layer7NewCfgHttpmodRuleHdrElmntStatusTxt,
       "layer7NewCfgHttpmodRuleHdrElmntTxt": layer7NewCfgHttpmodRuleHdrElmntTxt,
       "layer7NewCfgHttpmodRuleHdrElmntRegx": layer7NewCfgHttpmodRuleHdrElmntRegx,
       "layer7NewCfgHttpmodRuleHdrReplacHdr": layer7NewCfgHttpmodRuleHdrReplacHdr,
       "layer7NewCfgHttpmodRuleHdrReplacVal": layer7NewCfgHttpmodRuleHdrReplacVal,
       "layer7NewCfgHttpmodRuleHdrReplacNewHdr": layer7NewCfgHttpmodRuleHdrReplacNewHdr,
       "layer7NewCfgHttpmodRuleHdrReplacNewVal": layer7NewCfgHttpmodRuleHdrReplacNewVal,
       "layer7NewCfgHttpmodRuleHdrRemvHdr": layer7NewCfgHttpmodRuleHdrRemvHdr,
       "layer7NewCfgHttpmodRuleHdrRemvVal": layer7NewCfgHttpmodRuleHdrRemvVal,
       "layer7CurCfgHttpmodRuleCookieTable": layer7CurCfgHttpmodRuleCookieTable,
       "layer7CurCfgHttpmodRuleCookieEntry": layer7CurCfgHttpmodRuleCookieEntry,
       "layer7CurCfgHttpmodRuleCookieListIdIndex": layer7CurCfgHttpmodRuleCookieListIdIndex,
       "layer7CurCfgHttpmodRuleCookieIndex": layer7CurCfgHttpmodRuleCookieIndex,
       "layer7CurCfgHttpmodRuleCookieInsrtKey": layer7CurCfgHttpmodRuleCookieInsrtKey,
       "layer7CurCfgHttpmodRuleCookieInsrtVal": layer7CurCfgHttpmodRuleCookieInsrtVal,
       "layer7CurCfgHttpmodRuleCookieInsrtPath": layer7CurCfgHttpmodRuleCookieInsrtPath,
       "layer7CurCfgHttpmodRuleCookieInsrtDomn": layer7CurCfgHttpmodRuleCookieInsrtDomn,
       "layer7CurCfgHttpmodRuleCookieInsrtExp": layer7CurCfgHttpmodRuleCookieInsrtExp,
       "layer7CurCfgHttpmodRuleCookieInsrtElem": layer7CurCfgHttpmodRuleCookieInsrtElem,
       "layer7CurCfgHttpmodRuleCookieInsrtUrlHost": layer7CurCfgHttpmodRuleCookieInsrtUrlHost,
       "layer7CurCfgHttpmodRuleCookieInsrtUrlPath": layer7CurCfgHttpmodRuleCookieInsrtUrlPath,
       "layer7CurCfgHttpmodRuleCookieInsrtHdrFld": layer7CurCfgHttpmodRuleCookieInsrtHdrFld,
       "layer7CurCfgHttpmodRuleCookieInsrtHdrVal": layer7CurCfgHttpmodRuleCookieInsrtHdrVal,
       "layer7CurCfgHttpmodRuleCookieInsrtCookey": layer7CurCfgHttpmodRuleCookieInsrtCookey,
       "layer7CurCfgHttpmodRuleCookieInsrtCookieVal": layer7CurCfgHttpmodRuleCookieInsrtCookieVal,
       "layer7CurCfgHttpmodRuleCookieInsrtFiletyp": layer7CurCfgHttpmodRuleCookieInsrtFiletyp,
       "layer7CurCfgHttpmodRuleCookieInsrtStatsCode": layer7CurCfgHttpmodRuleCookieInsrtStatsCode,
       "layer7CurCfgHttpmodRuleCookieInsrtStatsTxt": layer7CurCfgHttpmodRuleCookieInsrtStatsTxt,
       "layer7CurCfgHttpmodRuleCookieInsrtTxt": layer7CurCfgHttpmodRuleCookieInsrtTxt,
       "layer7CurCfgHttpmodRuleCookieInsrtRegx": layer7CurCfgHttpmodRuleCookieInsrtRegx,
       "layer7CurCfgHttpmodRuleCookieReplcCookey": layer7CurCfgHttpmodRuleCookieReplcCookey,
       "layer7CurCfgHttpmodRuleCookieReplcVal": layer7CurCfgHttpmodRuleCookieReplcVal,
       "layer7CurCfgHttpmodRuleCookieReplcNewKey": layer7CurCfgHttpmodRuleCookieReplcNewKey,
       "layer7CurCfgHttpmodRuleCookieReplcNewVal": layer7CurCfgHttpmodRuleCookieReplcNewVal,
       "layer7CurCfgHttpmodRuleCookieRemvCookey": layer7CurCfgHttpmodRuleCookieRemvCookey,
       "layer7CurCfgHttpmodRuleCookieRemvCookieVal": layer7CurCfgHttpmodRuleCookieRemvCookieVal,
       "layer7NewCfgHttpmodRuleCookieTable": layer7NewCfgHttpmodRuleCookieTable,
       "layer7NewCfgHttpmodRuleCookieEntry": layer7NewCfgHttpmodRuleCookieEntry,
       "layer7NewCfgHttpmodRuleCookieListIdIndex": layer7NewCfgHttpmodRuleCookieListIdIndex,
       "layer7NewCfgHttpmodRuleCookieIndex": layer7NewCfgHttpmodRuleCookieIndex,
       "layer7NewCfgHttpmodRuleCookieInsrtKey": layer7NewCfgHttpmodRuleCookieInsrtKey,
       "layer7NewCfgHttpmodRuleCookieInsrtVal": layer7NewCfgHttpmodRuleCookieInsrtVal,
       "layer7NewCfgHttpmodRuleCookieInsrtPath": layer7NewCfgHttpmodRuleCookieInsrtPath,
       "layer7NewCfgHttpmodRuleCookieInsrtDomn": layer7NewCfgHttpmodRuleCookieInsrtDomn,
       "layer7NewCfgHttpmodRuleCookieInsrtExp": layer7NewCfgHttpmodRuleCookieInsrtExp,
       "layer7NewCfgHttpmodRuleCookieInsrtElem": layer7NewCfgHttpmodRuleCookieInsrtElem,
       "layer7NewCfgHttpmodRuleCookieInsrtUrlHost": layer7NewCfgHttpmodRuleCookieInsrtUrlHost,
       "layer7NewCfgHttpmodRuleCookieInsrtUrlPath": layer7NewCfgHttpmodRuleCookieInsrtUrlPath,
       "layer7NewCfgHttpmodRuleCookieInsrtHdrFld": layer7NewCfgHttpmodRuleCookieInsrtHdrFld,
       "layer7NewCfgHttpmodRuleCookieInsrtHdrVal": layer7NewCfgHttpmodRuleCookieInsrtHdrVal,
       "layer7NewCfgHttpmodRuleCookieInsrtCookey": layer7NewCfgHttpmodRuleCookieInsrtCookey,
       "layer7NewCfgHttpmodRuleCookieInsrtCookieVal": layer7NewCfgHttpmodRuleCookieInsrtCookieVal,
       "layer7NewCfgHttpmodRuleCookieInsrtFiletyp": layer7NewCfgHttpmodRuleCookieInsrtFiletyp,
       "layer7NewCfgHttpmodRuleCookieInsrtStatsCode": layer7NewCfgHttpmodRuleCookieInsrtStatsCode,
       "layer7NewCfgHttpmodRuleCookieInsrtStatsTxt": layer7NewCfgHttpmodRuleCookieInsrtStatsTxt,
       "layer7NewCfgHttpmodRuleCookieInsrtTxt": layer7NewCfgHttpmodRuleCookieInsrtTxt,
       "layer7NewCfgHttpmodRuleCookieInsrtRegx": layer7NewCfgHttpmodRuleCookieInsrtRegx,
       "layer7NewCfgHttpmodRuleCookieReplcCookey": layer7NewCfgHttpmodRuleCookieReplcCookey,
       "layer7NewCfgHttpmodRuleCookieReplcVal": layer7NewCfgHttpmodRuleCookieReplcVal,
       "layer7NewCfgHttpmodRuleCookieReplcNewKey": layer7NewCfgHttpmodRuleCookieReplcNewKey,
       "layer7NewCfgHttpmodRuleCookieReplcNewVal": layer7NewCfgHttpmodRuleCookieReplcNewVal,
       "layer7NewCfgHttpmodRuleCookieRemvCookey": layer7NewCfgHttpmodRuleCookieRemvCookey,
       "layer7NewCfgHttpmodRuleCookieRemvCookieVal": layer7NewCfgHttpmodRuleCookieRemvCookieVal,
       "layer7CurCfgHttpmodRuleFileLineTextTable": layer7CurCfgHttpmodRuleFileLineTextTable,
       "layer7CurCfgHttpmodRuleFileLineTextEntry": layer7CurCfgHttpmodRuleFileLineTextEntry,
       "layer7CurCfgHttpmodRuleFileLineTextListIdIndex": layer7CurCfgHttpmodRuleFileLineTextListIdIndex,
       "layer7CurCfgHttpmodRuleFileLineTextIndex": layer7CurCfgHttpmodRuleFileLineTextIndex,
       "layer7CurCfgHttpmodRuleFileTypRep": layer7CurCfgHttpmodRuleFileTypRep,
       "layer7CurCfgHttpmodRuleFileTypNew": layer7CurCfgHttpmodRuleFileTypNew,
       "layer7CurCfgHttpmodRuleStatlineCode": layer7CurCfgHttpmodRuleStatlineCode,
       "layer7CurCfgHttpmodRuleStatlineTxt": layer7CurCfgHttpmodRuleStatlineTxt,
       "layer7CurCfgHttpmodRuleStatlineNewCode": layer7CurCfgHttpmodRuleStatlineNewCode,
       "layer7CurCfgHttpmodRuleStatlineNewTxt": layer7CurCfgHttpmodRuleStatlineNewTxt,
       "layer7CurCfgHttpmodRuleTextReplace": layer7CurCfgHttpmodRuleTextReplace,
       "layer7CurCfgHttpmodRuleTextNewText": layer7CurCfgHttpmodRuleTextNewText,
       "layer7CurCfgHttpmodRuleTextRemove": layer7CurCfgHttpmodRuleTextRemove,
       "layer7NewCfgHttpmodRuleFileLineTextTable": layer7NewCfgHttpmodRuleFileLineTextTable,
       "layer7NewCfgHttpmodRuleFileLineTextEntry": layer7NewCfgHttpmodRuleFileLineTextEntry,
       "layer7NewCfgHttpmodRuleFileLineTextListIdIndex": layer7NewCfgHttpmodRuleFileLineTextListIdIndex,
       "layer7NewCfgHttpmodRuleFileLineTextIndex": layer7NewCfgHttpmodRuleFileLineTextIndex,
       "layer7NewCfgHttpmodRuleFileTypRep": layer7NewCfgHttpmodRuleFileTypRep,
       "layer7NewCfgHttpmodRuleFileTypNew": layer7NewCfgHttpmodRuleFileTypNew,
       "layer7NewCfgHttpmodRuleStatlineCode": layer7NewCfgHttpmodRuleStatlineCode,
       "layer7NewCfgHttpmodRuleStatlineTxt": layer7NewCfgHttpmodRuleStatlineTxt,
       "layer7NewCfgHttpmodRuleStatlineNewCode": layer7NewCfgHttpmodRuleStatlineNewCode,
       "layer7NewCfgHttpmodRuleStatlineNewTxt": layer7NewCfgHttpmodRuleStatlineNewTxt,
       "layer7NewCfgHttpmodRuleTextReplace": layer7NewCfgHttpmodRuleTextReplace,
       "layer7NewCfgHttpmodRuleTextNewText": layer7NewCfgHttpmodRuleTextNewText,
       "layer7NewCfgHttpmodRuleTextRemove": layer7NewCfgHttpmodRuleTextRemove,
       "ruleCfg": ruleCfg,
       "slbCurCfgSipUdpRuleTable": slbCurCfgSipUdpRuleTable,
       "slbCurCfgSipUdpRuleTableEntry": slbCurCfgSipUdpRuleTableEntry,
       "slbCurCfgSipUdpRuleIndex": slbCurCfgSipUdpRuleIndex,
       "slbCurCfgSipUdpRuleHdrFld": slbCurCfgSipUdpRuleHdrFld,
       "slbCurCfgSipUdpRuleContent": slbCurCfgSipUdpRuleContent,
       "slbCurCfgSipUdpRuleContract": slbCurCfgSipUdpRuleContract,
       "slbCurCfgSipUdpRuleMsg": slbCurCfgSipUdpRuleMsg,
       "slbCurCfgSipUdpRuleSeverity": slbCurCfgSipUdpRuleSeverity,
       "slbCurCfgSipUdpRuleAdd": slbCurCfgSipUdpRuleAdd,
       "slbCurCfgSipUdpRuleState": slbCurCfgSipUdpRuleState,
       "slbCurCfgSipUdpRuleBmap": slbCurCfgSipUdpRuleBmap,
       "slbNewCfgSipUdpRuleTable": slbNewCfgSipUdpRuleTable,
       "slbNewCfgSipUdpRuleTableEntry": slbNewCfgSipUdpRuleTableEntry,
       "slbNewCfgSipUdpRuleIndex": slbNewCfgSipUdpRuleIndex,
       "slbNewCfgSipUdpRuleHdrFld": slbNewCfgSipUdpRuleHdrFld,
       "slbNewCfgSipUdpRuleContent": slbNewCfgSipUdpRuleContent,
       "slbNewCfgSipUdpRuleContract": slbNewCfgSipUdpRuleContract,
       "slbNewCfgSipUdpRuleMsg": slbNewCfgSipUdpRuleMsg,
       "slbNewCfgSipUdpRuleSeverity": slbNewCfgSipUdpRuleSeverity,
       "slbNewCfgSipUdpRuleAdd": slbNewCfgSipUdpRuleAdd,
       "slbNewCfgSipUdpRuleRem": slbNewCfgSipUdpRuleRem,
       "slbNewCfgSipUdpRuleState": slbNewCfgSipUdpRuleState,
       "slbNewCfgSipUdpRuleDelete": slbNewCfgSipUdpRuleDelete,
       "slbNewCfgSipUdpRuleBmap": slbNewCfgSipUdpRuleBmap,
       "contentClass": contentClass,
       "layer7CurCfgContentClassTable": layer7CurCfgContentClassTable,
       "layer7CurCfgContentClassEntry": layer7CurCfgContentClassEntry,
       "layer7CurCfgContentClassID": layer7CurCfgContentClassID,
       "layer7CurCfgContentClassName": layer7CurCfgContentClassName,
       "layer7CurCfgContentClassLogicalExpression": layer7CurCfgContentClassLogicalExpression,
       "layer7CurCfgContentClassHostName": layer7CurCfgContentClassHostName,
       "layer7CurCfgContentClassPath": layer7CurCfgContentClassPath,
       "layer7CurCfgContentClassFileName": layer7CurCfgContentClassFileName,
       "layer7CurCfgContentClassFileType": layer7CurCfgContentClassFileType,
       "layer7CurCfgContentClassHeader": layer7CurCfgContentClassHeader,
       "layer7CurCfgContentClassCookie": layer7CurCfgContentClassCookie,
       "layer7CurCfgContentClassText": layer7CurCfgContentClassText,
       "layer7CurCfgContentClassXMLTag": layer7CurCfgContentClassXMLTag,
       "layer7NewCfgContentClassTable": layer7NewCfgContentClassTable,
       "layer7NewCfgContentClassEntry": layer7NewCfgContentClassEntry,
       "layer7NewCfgContentClassID": layer7NewCfgContentClassID,
       "layer7NewCfgContentClassName": layer7NewCfgContentClassName,
       "layer7NewCfgContentClassLogicalExpression": layer7NewCfgContentClassLogicalExpression,
       "layer7NewCfgContentClassHostName": layer7NewCfgContentClassHostName,
       "layer7NewCfgContentClassPath": layer7NewCfgContentClassPath,
       "layer7NewCfgContentClassFileName": layer7NewCfgContentClassFileName,
       "layer7NewCfgContentClassFileType": layer7NewCfgContentClassFileType,
       "layer7NewCfgContentClassHeader": layer7NewCfgContentClassHeader,
       "layer7NewCfgContentClassCookie": layer7NewCfgContentClassCookie,
       "layer7NewCfgContentClassText": layer7NewCfgContentClassText,
       "layer7NewCfgContentClassXMLTag": layer7NewCfgContentClassXMLTag,
       "layer7NewCfgContentClassDelete": layer7NewCfgContentClassDelete,
       "layer7NewCfgContentClassCopy": layer7NewCfgContentClassCopy,
       "layer7CurCfgContentClassHostNameTable": layer7CurCfgContentClassHostNameTable,
       "layer7CurCfgContentClassHostNameEntry": layer7CurCfgContentClassHostNameEntry,
       "layer7CurCfgContentClassHostNameContentClassID": layer7CurCfgContentClassHostNameContentClassID,
       "layer7CurCfgContentClassHostNameID": layer7CurCfgContentClassHostNameID,
       "layer7CurCfgContentClassHostNameHostName": layer7CurCfgContentClassHostNameHostName,
       "layer7CurCfgContentClassHostNameMatchType": layer7CurCfgContentClassHostNameMatchType,
       "layer7NewCfgContentClassHostNameTable": layer7NewCfgContentClassHostNameTable,
       "layer7NewCfgContentClassHostNameEntry": layer7NewCfgContentClassHostNameEntry,
       "layer7NewCfgContentClassHostNameContentClassID": layer7NewCfgContentClassHostNameContentClassID,
       "layer7NewCfgContentClassHostNameID": layer7NewCfgContentClassHostNameID,
       "layer7NewCfgContentClassHostNameHostName": layer7NewCfgContentClassHostNameHostName,
       "layer7NewCfgContentClassHostNameMatchType": layer7NewCfgContentClassHostNameMatchType,
       "layer7NewCfgContentClassHostNameDelete": layer7NewCfgContentClassHostNameDelete,
       "layer7CurCfgContentClassPathTable": layer7CurCfgContentClassPathTable,
       "layer7CurCfgContentClassPathEntry": layer7CurCfgContentClassPathEntry,
       "layer7CurCfgContentClassPathContentClassID": layer7CurCfgContentClassPathContentClassID,
       "layer7CurCfgContentClassPathID": layer7CurCfgContentClassPathID,
       "layer7CurCfgContentClassPathFilePath": layer7CurCfgContentClassPathFilePath,
       "layer7CurCfgContentClassPathMatchType": layer7CurCfgContentClassPathMatchType,
       "layer7CurCfgContentClassPathCase": layer7CurCfgContentClassPathCase,
       "layer7NewCfgContentClassPathTable": layer7NewCfgContentClassPathTable,
       "layer7NewCfgContentClassPathEntry": layer7NewCfgContentClassPathEntry,
       "layer7NewCfgContentClassPathContentClassID": layer7NewCfgContentClassPathContentClassID,
       "layer7NewCfgContentClassPathID": layer7NewCfgContentClassPathID,
       "layer7NewCfgContentClassPathFilePath": layer7NewCfgContentClassPathFilePath,
       "layer7NewCfgContentClassPathMatchType": layer7NewCfgContentClassPathMatchType,
       "layer7NewCfgContentClassPathCase": layer7NewCfgContentClassPathCase,
       "layer7NewCfgContentClassPathDelete": layer7NewCfgContentClassPathDelete,
       "layer7CurCfgContentClassFileNameTable": layer7CurCfgContentClassFileNameTable,
       "layer7CurCfgContentClassFileNameEntry": layer7CurCfgContentClassFileNameEntry,
       "layer7CurCfgContentClassFileNameContentClassID": layer7CurCfgContentClassFileNameContentClassID,
       "layer7CurCfgContentClassFileNameID": layer7CurCfgContentClassFileNameID,
       "layer7CurCfgContentClassFileNameFileName": layer7CurCfgContentClassFileNameFileName,
       "layer7CurCfgContentClassFileNameMatchType": layer7CurCfgContentClassFileNameMatchType,
       "layer7CurCfgContentClassFileNameCase": layer7CurCfgContentClassFileNameCase,
       "layer7NewCfgContentClassFileNameTable": layer7NewCfgContentClassFileNameTable,
       "layer7NewCfgContentClassFileNameEntry": layer7NewCfgContentClassFileNameEntry,
       "layer7NewCfgContentClassFileNameContentClassID": layer7NewCfgContentClassFileNameContentClassID,
       "layer7NewCfgContentClassFileNameID": layer7NewCfgContentClassFileNameID,
       "layer7NewCfgContentClassFileNameFileName": layer7NewCfgContentClassFileNameFileName,
       "layer7NewCfgContentClassFileNameMatchType": layer7NewCfgContentClassFileNameMatchType,
       "layer7NewCfgContentClassFileNameCase": layer7NewCfgContentClassFileNameCase,
       "layer7NewCfgContentClassFileNameDelete": layer7NewCfgContentClassFileNameDelete,
       "layer7CurCfgContentClassFileTypeTable": layer7CurCfgContentClassFileTypeTable,
       "layer7CurCfgContentClassFileTypeEntry": layer7CurCfgContentClassFileTypeEntry,
       "layer7CurCfgContentClassFileTypeContentClassID": layer7CurCfgContentClassFileTypeContentClassID,
       "layer7CurCfgContentClassFileTypeID": layer7CurCfgContentClassFileTypeID,
       "layer7CurCfgContentClassFileTypeFileType": layer7CurCfgContentClassFileTypeFileType,
       "layer7CurCfgContentClassFileTypeMatchType": layer7CurCfgContentClassFileTypeMatchType,
       "layer7CurCfgContentClassFileTypeCase": layer7CurCfgContentClassFileTypeCase,
       "layer7NewCfgContentClassFileTypeTable": layer7NewCfgContentClassFileTypeTable,
       "layer7NewCfgContentClassFileTypeEntry": layer7NewCfgContentClassFileTypeEntry,
       "layer7NewCfgContentClassFileTypeContentClassID": layer7NewCfgContentClassFileTypeContentClassID,
       "layer7NewCfgContentClassFileTypeID": layer7NewCfgContentClassFileTypeID,
       "layer7NewCfgContentClassFileTypeFileType": layer7NewCfgContentClassFileTypeFileType,
       "layer7NewCfgContentClassFileTypeMatchType": layer7NewCfgContentClassFileTypeMatchType,
       "layer7NewCfgContentClassFileTypeCase": layer7NewCfgContentClassFileTypeCase,
       "layer7NewCfgContentClassFileTypeDelete": layer7NewCfgContentClassFileTypeDelete,
       "layer7CurCfgContentClassHeaderTable": layer7CurCfgContentClassHeaderTable,
       "layer7CurCfgContentClassHeaderEntry": layer7CurCfgContentClassHeaderEntry,
       "layer7CurCfgContentClassHeaderContentClassID": layer7CurCfgContentClassHeaderContentClassID,
       "layer7CurCfgContentClassHeaderID": layer7CurCfgContentClassHeaderID,
       "layer7CurCfgContentClassHeaderName": layer7CurCfgContentClassHeaderName,
       "layer7CurCfgContentClassHeaderVal": layer7CurCfgContentClassHeaderVal,
       "layer7CurCfgContentClassHeaderMatchTypeName": layer7CurCfgContentClassHeaderMatchTypeName,
       "layer7CurCfgContentClassHeaderMatchTypeVal": layer7CurCfgContentClassHeaderMatchTypeVal,
       "layer7CurCfgContentClassHeaderCase": layer7CurCfgContentClassHeaderCase,
       "layer7NewCfgContentClassHeaderTable": layer7NewCfgContentClassHeaderTable,
       "layer7NewCfgContentClassHeaderEntry": layer7NewCfgContentClassHeaderEntry,
       "layer7NewCfgContentClassHeaderContentClassID": layer7NewCfgContentClassHeaderContentClassID,
       "layer7NewCfgContentClassHeaderID": layer7NewCfgContentClassHeaderID,
       "layer7NewCfgContentClassHeaderName": layer7NewCfgContentClassHeaderName,
       "layer7NewCfgContentClassHeaderVal": layer7NewCfgContentClassHeaderVal,
       "layer7NewCfgContentClassHeaderMatchTypeName": layer7NewCfgContentClassHeaderMatchTypeName,
       "layer7NewCfgContentClassHeaderMatchTypeVal": layer7NewCfgContentClassHeaderMatchTypeVal,
       "layer7NewCfgContentClassHeaderCase": layer7NewCfgContentClassHeaderCase,
       "layer7NewCfgContentClassHeaderDelete": layer7NewCfgContentClassHeaderDelete,
       "layer7CurCfgContentClassCookieTable": layer7CurCfgContentClassCookieTable,
       "layer7CurCfgContentClassCookieEntry": layer7CurCfgContentClassCookieEntry,
       "layer7CurCfgContentClassCookieContentClassID": layer7CurCfgContentClassCookieContentClassID,
       "layer7CurCfgContentClassCookieID": layer7CurCfgContentClassCookieID,
       "layer7CurCfgContentClassCookieKey": layer7CurCfgContentClassCookieKey,
       "layer7CurCfgContentClassCookieVal": layer7CurCfgContentClassCookieVal,
       "layer7CurCfgContentClassCookieMatchTypeKey": layer7CurCfgContentClassCookieMatchTypeKey,
       "layer7CurCfgContentClassCookieMatchTypeVal": layer7CurCfgContentClassCookieMatchTypeVal,
       "layer7CurCfgContentClassCookieCase": layer7CurCfgContentClassCookieCase,
       "layer7NewCfgContentClassCookieTable": layer7NewCfgContentClassCookieTable,
       "layer7NewCfgContentClassCookieEntry": layer7NewCfgContentClassCookieEntry,
       "layer7NewCfgContentClassCookieContentClassID": layer7NewCfgContentClassCookieContentClassID,
       "layer7NewCfgContentClassCookieID": layer7NewCfgContentClassCookieID,
       "layer7NewCfgContentClassCookieKey": layer7NewCfgContentClassCookieKey,
       "layer7NewCfgContentClassCookieVal": layer7NewCfgContentClassCookieVal,
       "layer7NewCfgContentClassCookieMatchTypeKey": layer7NewCfgContentClassCookieMatchTypeKey,
       "layer7NewCfgContentClassCookieMatchTypeVal": layer7NewCfgContentClassCookieMatchTypeVal,
       "layer7NewCfgContentClassCookieCase": layer7NewCfgContentClassCookieCase,
       "layer7NewCfgContentClassCookieDelete": layer7NewCfgContentClassCookieDelete,
       "layer7CurCfgContentClassTextTable": layer7CurCfgContentClassTextTable,
       "layer7CurCfgContentClassTextEntry": layer7CurCfgContentClassTextEntry,
       "layer7CurCfgContentClassTextContentClassID": layer7CurCfgContentClassTextContentClassID,
       "layer7CurCfgContentClassTextID": layer7CurCfgContentClassTextID,
       "layer7CurCfgContentClassTextText": layer7CurCfgContentClassTextText,
       "layer7CurCfgContentClassTextMatchType": layer7CurCfgContentClassTextMatchType,
       "layer7CurCfgContentClassTextLookupArea": layer7CurCfgContentClassTextLookupArea,
       "layer7CurCfgContentClassTextCase": layer7CurCfgContentClassTextCase,
       "layer7NewCfgContentClassTextTable": layer7NewCfgContentClassTextTable,
       "layer7NewCfgContentClassTextEntry": layer7NewCfgContentClassTextEntry,
       "layer7NewCfgContentClassTextContentClassID": layer7NewCfgContentClassTextContentClassID,
       "layer7NewCfgContentClassTextID": layer7NewCfgContentClassTextID,
       "layer7NewCfgContentClassTextText": layer7NewCfgContentClassTextText,
       "layer7NewCfgContentClassTextMatchType": layer7NewCfgContentClassTextMatchType,
       "layer7NewCfgContentClassTextLookupArea": layer7NewCfgContentClassTextLookupArea,
       "layer7NewCfgContentClassTextCase": layer7NewCfgContentClassTextCase,
       "layer7NewCfgContentClassTextDelete": layer7NewCfgContentClassTextDelete,
       "layer7CurCfgContentClassXmlTable": layer7CurCfgContentClassXmlTable,
       "layer7CurCfgContentClassXmlEntry": layer7CurCfgContentClassXmlEntry,
       "layer7CurCfgContentClassXmlTagContentClassID": layer7CurCfgContentClassXmlTagContentClassID,
       "layer7CurCfgContentClassXmlTagID": layer7CurCfgContentClassXmlTagID,
       "layer7CurCfgContentClassXmlTagName": layer7CurCfgContentClassXmlTagName,
       "layer7CurCfgContentClassXmlTagVal": layer7CurCfgContentClassXmlTagVal,
       "layer7CurCfgContentClassXmlTagMatchTypeName": layer7CurCfgContentClassXmlTagMatchTypeName,
       "layer7CurCfgContentClassXmlTagMatchTypeVal": layer7CurCfgContentClassXmlTagMatchTypeVal,
       "layer7CurCfgContentClassXmlTagCase": layer7CurCfgContentClassXmlTagCase,
       "layer7NewCfgContentClassXmlTable": layer7NewCfgContentClassXmlTable,
       "layer7NewCfgContentClassXmlEntry": layer7NewCfgContentClassXmlEntry,
       "layer7NewCfgContentClassXmlTagContentClassID": layer7NewCfgContentClassXmlTagContentClassID,
       "layer7NewCfgContentClassXmlTagID": layer7NewCfgContentClassXmlTagID,
       "layer7NewCfgContentClassXmlTagName": layer7NewCfgContentClassXmlTagName,
       "layer7NewCfgContentClassXmlTagVal": layer7NewCfgContentClassXmlTagVal,
       "layer7NewCfgContentClassXmlTagMatchTypeName": layer7NewCfgContentClassXmlTagMatchTypeName,
       "layer7NewCfgContentClassXmlTagMatchTypeVal": layer7NewCfgContentClassXmlTagMatchTypeVal,
       "layer7NewCfgContentClassXmlTagCase": layer7NewCfgContentClassXmlTagCase,
       "layer7NewCfgContentClassXmlTagDelete": layer7NewCfgContentClassXmlTagDelete,
       "layer7Stats": layer7Stats,
       "urlStats": urlStats,
       "urlRedirStats": urlRedirStats,
       "urlStatRedRedirs": urlStatRedRedirs,
       "urlStatRedOrigSrvs": urlStatRedOrigSrvs,
       "urlStatRedNonGets": urlStatRedNonGets,
       "urlStatRedCookie": urlStatRedCookie,
       "urlStatRedNoCache": urlStatRedNoCache,
       "urlStatRedStraightOrigSrvs": urlStatRedStraightOrigSrvs,
       "urlStatRedRtspCacheSrvs": urlStatRedRtspCacheSrvs,
       "urlStatRedRtspOrigSrvs": urlStatRedRtspOrigSrvs,
       "urlSlbStats": urlSlbStats,
       "urlStatSlbPathTable": urlStatSlbPathTable,
       "urlStatSlbPathTableEntry": urlStatSlbPathTableEntry,
       "urlStatSlbPathIndex": urlStatSlbPathIndex,
       "urlStatSlbPathHits": urlStatSlbPathHits,
       "urlMaintStats": urlMaintStats,
       "urlMaintStatClientReset": urlMaintStatClientReset,
       "urlMaintStatServerReset": urlMaintStatServerReset,
       "urlMaintStatConnSplicing": urlMaintStatConnSplicing,
       "urlMaintStatHalfOpens": urlMaintStatHalfOpens,
       "urlMaintStatSwitchRetries": urlMaintStatSwitchRetries,
       "urlMaintStatRandomEarlyDrops": urlMaintStatRandomEarlyDrops,
       "urlMaintStatReqTooLong": urlMaintStatReqTooLong,
       "urlMaintStatInvalidHandshakes": urlMaintStatInvalidHandshakes,
       "urlMaintStatCurSPMemUnits": urlMaintStatCurSPMemUnits,
       "urlMaintStatCurSEQBufEntries": urlMaintStatCurSEQBufEntries,
       "urlMaintStatHighestSEQBufEntries": urlMaintStatHighestSEQBufEntries,
       "urlMaintStatCurDataBufUse": urlMaintStatCurDataBufUse,
       "urlMaintStatHighestDataBufUse": urlMaintStatHighestDataBufUse,
       "urlMaintStatCurSPBufEntries": urlMaintStatCurSPBufEntries,
       "urlMaintStatHighestSPBufEntries": urlMaintStatHighestSPBufEntries,
       "urlMaintStatTotalNonZeroSEQAlloc": urlMaintStatTotalNonZeroSEQAlloc,
       "urlMaintStatTotalSEQBufAllocs": urlMaintStatTotalSEQBufAllocs,
       "urlMaintStatTotalSEQBufFrees": urlMaintStatTotalSEQBufFrees,
       "urlMaintStatTotalDataBufAllocs": urlMaintStatTotalDataBufAllocs,
       "urlMaintStatTotalDataBufFrees": urlMaintStatTotalDataBufFrees,
       "urlMaintStatSeqBufAllocFails": urlMaintStatSeqBufAllocFails,
       "urlMaintStatUBufAllocFails": urlMaintStatUBufAllocFails,
       "urlMaintStatMaxSessPerBucket": urlMaintStatMaxSessPerBucket,
       "urlMaintStatMaxFramesPerSess": urlMaintStatMaxFramesPerSess,
       "urlMaintStatMaxBytesBuffered": urlMaintStatMaxBytesBuffered,
       "urlMaintStatInvalidMethods": urlMaintStatInvalidMethods,
       "urlMaintStatAgedSessions": urlMaintStatAgedSessions,
       "urlMaintStatLowestSPMemUnits": urlMaintStatLowestSPMemUnits,
       "urlSpMaintStatsTable": urlSpMaintStatsTable,
       "urlSpMaintStatsTableEntry": urlSpMaintStatsTableEntry,
       "urlSpMaintStatsSpIndex": urlSpMaintStatsSpIndex,
       "urlSpMaintStatsCurMemUnits": urlSpMaintStatsCurMemUnits,
       "urlSpMaintStatsLowestMemUnits": urlSpMaintStatsLowestMemUnits,
       "connPoolingStats": connPoolingStats,
       "currOpenedServerConns": currOpenedServerConns,
       "activeServerConns": activeServerConns,
       "availServerConns": availServerConns,
       "agedOutClientConns": agedOutClientConns,
       "agedOutServerConns": agedOutServerConns,
       "layer7Info": layer7Info,
       "slbParsing": slbParsing,
       "slbParsingString": slbParsingString,
       "slbParsingVip": slbParsingVip,
       "slbParsingRip": slbParsingRip,
       "slbParsingRport": slbParsingRport,
       "slbParsingCip": slbParsingCip,
       "layer7Oper": layer7Oper}
)
