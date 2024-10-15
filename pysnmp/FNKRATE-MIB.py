# SNMP MIB module (FNKRATE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/FNKRATE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:45:19 2024
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

(funkSbr,) = mibBuilder.importSymbols(
    "FNKSBRTR-MIB",
    "funkSbr")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

_FunkSbrExtensions_ObjectIdentity = ObjectIdentity
funkSbrExtensions = _FunkSbrExtensions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1411, 1, 2)
)
_FunkSbrRateVars_ObjectIdentity = ObjectIdentity
funkSbrRateVars = _FunkSbrRateVars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1411, 1, 2, 1)
)


class _FunkSbrRatesSecondsPerInterval_Type(Integer32):
    """Custom type funkSbrRatesSecondsPerInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FunkSbrRatesSecondsPerInterval_Type.__name__ = "Integer32"
_FunkSbrRatesSecondsPerInterval_Object = MibScalar
funkSbrRatesSecondsPerInterval = _FunkSbrRatesSecondsPerInterval_Object(
    (1, 3, 6, 1, 4, 1, 1411, 1, 2, 1, 1),
    _FunkSbrRatesSecondsPerInterval_Type()
)
funkSbrRatesSecondsPerInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    funkSbrRatesSecondsPerInterval.setStatus("current")


class _FunkSbrRatesAuthRequestCurrentRate_Type(Integer32):
    """Custom type funkSbrRatesAuthRequestCurrentRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FunkSbrRatesAuthRequestCurrentRate_Type.__name__ = "Integer32"
_FunkSbrRatesAuthRequestCurrentRate_Object = MibScalar
funkSbrRatesAuthRequestCurrentRate = _FunkSbrRatesAuthRequestCurrentRate_Object(
    (1, 3, 6, 1, 4, 1, 1411, 1, 2, 1, 2),
    _FunkSbrRatesAuthRequestCurrentRate_Type()
)
funkSbrRatesAuthRequestCurrentRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    funkSbrRatesAuthRequestCurrentRate.setStatus("current")


class _FunkSbrRatesAuthRequestAverageRate_Type(Integer32):
    """Custom type funkSbrRatesAuthRequestAverageRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FunkSbrRatesAuthRequestAverageRate_Type.__name__ = "Integer32"
_FunkSbrRatesAuthRequestAverageRate_Object = MibScalar
funkSbrRatesAuthRequestAverageRate = _FunkSbrRatesAuthRequestAverageRate_Object(
    (1, 3, 6, 1, 4, 1, 1411, 1, 2, 1, 3),
    _FunkSbrRatesAuthRequestAverageRate_Type()
)
funkSbrRatesAuthRequestAverageRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    funkSbrRatesAuthRequestAverageRate.setStatus("current")


class _FunkSbrRatesAuthRequestPeakRate_Type(Integer32):
    """Custom type funkSbrRatesAuthRequestPeakRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FunkSbrRatesAuthRequestPeakRate_Type.__name__ = "Integer32"
_FunkSbrRatesAuthRequestPeakRate_Object = MibScalar
funkSbrRatesAuthRequestPeakRate = _FunkSbrRatesAuthRequestPeakRate_Object(
    (1, 3, 6, 1, 4, 1, 1411, 1, 2, 1, 4),
    _FunkSbrRatesAuthRequestPeakRate_Type()
)
funkSbrRatesAuthRequestPeakRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    funkSbrRatesAuthRequestPeakRate.setStatus("current")


class _FunkSbrRatesAuthAcceptCurrentRate_Type(Integer32):
    """Custom type funkSbrRatesAuthAcceptCurrentRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FunkSbrRatesAuthAcceptCurrentRate_Type.__name__ = "Integer32"
_FunkSbrRatesAuthAcceptCurrentRate_Object = MibScalar
funkSbrRatesAuthAcceptCurrentRate = _FunkSbrRatesAuthAcceptCurrentRate_Object(
    (1, 3, 6, 1, 4, 1, 1411, 1, 2, 1, 5),
    _FunkSbrRatesAuthAcceptCurrentRate_Type()
)
funkSbrRatesAuthAcceptCurrentRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    funkSbrRatesAuthAcceptCurrentRate.setStatus("current")


class _FunkSbrRatesAuthAcceptAverageRate_Type(Integer32):
    """Custom type funkSbrRatesAuthAcceptAverageRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FunkSbrRatesAuthAcceptAverageRate_Type.__name__ = "Integer32"
_FunkSbrRatesAuthAcceptAverageRate_Object = MibScalar
funkSbrRatesAuthAcceptAverageRate = _FunkSbrRatesAuthAcceptAverageRate_Object(
    (1, 3, 6, 1, 4, 1, 1411, 1, 2, 1, 6),
    _FunkSbrRatesAuthAcceptAverageRate_Type()
)
funkSbrRatesAuthAcceptAverageRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    funkSbrRatesAuthAcceptAverageRate.setStatus("current")


class _FunkSbrRatesAuthAcceptPeakRate_Type(Integer32):
    """Custom type funkSbrRatesAuthAcceptPeakRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FunkSbrRatesAuthAcceptPeakRate_Type.__name__ = "Integer32"
_FunkSbrRatesAuthAcceptPeakRate_Object = MibScalar
funkSbrRatesAuthAcceptPeakRate = _FunkSbrRatesAuthAcceptPeakRate_Object(
    (1, 3, 6, 1, 4, 1, 1411, 1, 2, 1, 7),
    _FunkSbrRatesAuthAcceptPeakRate_Type()
)
funkSbrRatesAuthAcceptPeakRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    funkSbrRatesAuthAcceptPeakRate.setStatus("current")


class _FunkSbrRatesAuthRejectCurrentRate_Type(Integer32):
    """Custom type funkSbrRatesAuthRejectCurrentRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FunkSbrRatesAuthRejectCurrentRate_Type.__name__ = "Integer32"
_FunkSbrRatesAuthRejectCurrentRate_Object = MibScalar
funkSbrRatesAuthRejectCurrentRate = _FunkSbrRatesAuthRejectCurrentRate_Object(
    (1, 3, 6, 1, 4, 1, 1411, 1, 2, 1, 8),
    _FunkSbrRatesAuthRejectCurrentRate_Type()
)
funkSbrRatesAuthRejectCurrentRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    funkSbrRatesAuthRejectCurrentRate.setStatus("current")


class _FunkSbrRatesAuthRejectAverageRate_Type(Integer32):
    """Custom type funkSbrRatesAuthRejectAverageRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FunkSbrRatesAuthRejectAverageRate_Type.__name__ = "Integer32"
_FunkSbrRatesAuthRejectAverageRate_Object = MibScalar
funkSbrRatesAuthRejectAverageRate = _FunkSbrRatesAuthRejectAverageRate_Object(
    (1, 3, 6, 1, 4, 1, 1411, 1, 2, 1, 9),
    _FunkSbrRatesAuthRejectAverageRate_Type()
)
funkSbrRatesAuthRejectAverageRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    funkSbrRatesAuthRejectAverageRate.setStatus("current")


class _FunkSbrRatesAuthRejectPeakRate_Type(Integer32):
    """Custom type funkSbrRatesAuthRejectPeakRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FunkSbrRatesAuthRejectPeakRate_Type.__name__ = "Integer32"
_FunkSbrRatesAuthRejectPeakRate_Object = MibScalar
funkSbrRatesAuthRejectPeakRate = _FunkSbrRatesAuthRejectPeakRate_Object(
    (1, 3, 6, 1, 4, 1, 1411, 1, 2, 1, 10),
    _FunkSbrRatesAuthRejectPeakRate_Type()
)
funkSbrRatesAuthRejectPeakRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    funkSbrRatesAuthRejectPeakRate.setStatus("current")


class _FunkSbrRatesAcctStartCurrentRate_Type(Integer32):
    """Custom type funkSbrRatesAcctStartCurrentRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FunkSbrRatesAcctStartCurrentRate_Type.__name__ = "Integer32"
_FunkSbrRatesAcctStartCurrentRate_Object = MibScalar
funkSbrRatesAcctStartCurrentRate = _FunkSbrRatesAcctStartCurrentRate_Object(
    (1, 3, 6, 1, 4, 1, 1411, 1, 2, 1, 11),
    _FunkSbrRatesAcctStartCurrentRate_Type()
)
funkSbrRatesAcctStartCurrentRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    funkSbrRatesAcctStartCurrentRate.setStatus("current")


class _FunkSbrRatesAcctStartAverageRate_Type(Integer32):
    """Custom type funkSbrRatesAcctStartAverageRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FunkSbrRatesAcctStartAverageRate_Type.__name__ = "Integer32"
_FunkSbrRatesAcctStartAverageRate_Object = MibScalar
funkSbrRatesAcctStartAverageRate = _FunkSbrRatesAcctStartAverageRate_Object(
    (1, 3, 6, 1, 4, 1, 1411, 1, 2, 1, 12),
    _FunkSbrRatesAcctStartAverageRate_Type()
)
funkSbrRatesAcctStartAverageRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    funkSbrRatesAcctStartAverageRate.setStatus("current")


class _FunkSbrRatesAcctStartPeakRate_Type(Integer32):
    """Custom type funkSbrRatesAcctStartPeakRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FunkSbrRatesAcctStartPeakRate_Type.__name__ = "Integer32"
_FunkSbrRatesAcctStartPeakRate_Object = MibScalar
funkSbrRatesAcctStartPeakRate = _FunkSbrRatesAcctStartPeakRate_Object(
    (1, 3, 6, 1, 4, 1, 1411, 1, 2, 1, 13),
    _FunkSbrRatesAcctStartPeakRate_Type()
)
funkSbrRatesAcctStartPeakRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    funkSbrRatesAcctStartPeakRate.setStatus("current")


class _FunkSbrRatesAcctStopCurrentRate_Type(Integer32):
    """Custom type funkSbrRatesAcctStopCurrentRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FunkSbrRatesAcctStopCurrentRate_Type.__name__ = "Integer32"
_FunkSbrRatesAcctStopCurrentRate_Object = MibScalar
funkSbrRatesAcctStopCurrentRate = _FunkSbrRatesAcctStopCurrentRate_Object(
    (1, 3, 6, 1, 4, 1, 1411, 1, 2, 1, 14),
    _FunkSbrRatesAcctStopCurrentRate_Type()
)
funkSbrRatesAcctStopCurrentRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    funkSbrRatesAcctStopCurrentRate.setStatus("current")


class _FunkSbrRatesAcctStopAverageRate_Type(Integer32):
    """Custom type funkSbrRatesAcctStopAverageRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FunkSbrRatesAcctStopAverageRate_Type.__name__ = "Integer32"
_FunkSbrRatesAcctStopAverageRate_Object = MibScalar
funkSbrRatesAcctStopAverageRate = _FunkSbrRatesAcctStopAverageRate_Object(
    (1, 3, 6, 1, 4, 1, 1411, 1, 2, 1, 15),
    _FunkSbrRatesAcctStopAverageRate_Type()
)
funkSbrRatesAcctStopAverageRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    funkSbrRatesAcctStopAverageRate.setStatus("current")


class _FunkSbrRatesAcctStopPeakRate_Type(Integer32):
    """Custom type funkSbrRatesAcctStopPeakRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FunkSbrRatesAcctStopPeakRate_Type.__name__ = "Integer32"
_FunkSbrRatesAcctStopPeakRate_Object = MibScalar
funkSbrRatesAcctStopPeakRate = _FunkSbrRatesAcctStopPeakRate_Object(
    (1, 3, 6, 1, 4, 1, 1411, 1, 2, 1, 16),
    _FunkSbrRatesAcctStopPeakRate_Type()
)
funkSbrRatesAcctStopPeakRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    funkSbrRatesAcctStopPeakRate.setStatus("current")


class _FunkSbrRatesProxyAuthRequestCurrentRate_Type(Integer32):
    """Custom type funkSbrRatesProxyAuthRequestCurrentRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FunkSbrRatesProxyAuthRequestCurrentRate_Type.__name__ = "Integer32"
_FunkSbrRatesProxyAuthRequestCurrentRate_Object = MibScalar
funkSbrRatesProxyAuthRequestCurrentRate = _FunkSbrRatesProxyAuthRequestCurrentRate_Object(
    (1, 3, 6, 1, 4, 1, 1411, 1, 2, 1, 17),
    _FunkSbrRatesProxyAuthRequestCurrentRate_Type()
)
funkSbrRatesProxyAuthRequestCurrentRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    funkSbrRatesProxyAuthRequestCurrentRate.setStatus("current")


class _FunkSbrRatesProxyAuthRequestAverageRate_Type(Integer32):
    """Custom type funkSbrRatesProxyAuthRequestAverageRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FunkSbrRatesProxyAuthRequestAverageRate_Type.__name__ = "Integer32"
_FunkSbrRatesProxyAuthRequestAverageRate_Object = MibScalar
funkSbrRatesProxyAuthRequestAverageRate = _FunkSbrRatesProxyAuthRequestAverageRate_Object(
    (1, 3, 6, 1, 4, 1, 1411, 1, 2, 1, 18),
    _FunkSbrRatesProxyAuthRequestAverageRate_Type()
)
funkSbrRatesProxyAuthRequestAverageRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    funkSbrRatesProxyAuthRequestAverageRate.setStatus("current")


class _FunkSbrRatesProxyAuthRequestPeakRate_Type(Integer32):
    """Custom type funkSbrRatesProxyAuthRequestPeakRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FunkSbrRatesProxyAuthRequestPeakRate_Type.__name__ = "Integer32"
_FunkSbrRatesProxyAuthRequestPeakRate_Object = MibScalar
funkSbrRatesProxyAuthRequestPeakRate = _FunkSbrRatesProxyAuthRequestPeakRate_Object(
    (1, 3, 6, 1, 4, 1, 1411, 1, 2, 1, 19),
    _FunkSbrRatesProxyAuthRequestPeakRate_Type()
)
funkSbrRatesProxyAuthRequestPeakRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    funkSbrRatesProxyAuthRequestPeakRate.setStatus("current")


class _FunkSbrRatesProxyAcctRequestCurrentRate_Type(Integer32):
    """Custom type funkSbrRatesProxyAcctRequestCurrentRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FunkSbrRatesProxyAcctRequestCurrentRate_Type.__name__ = "Integer32"
_FunkSbrRatesProxyAcctRequestCurrentRate_Object = MibScalar
funkSbrRatesProxyAcctRequestCurrentRate = _FunkSbrRatesProxyAcctRequestCurrentRate_Object(
    (1, 3, 6, 1, 4, 1, 1411, 1, 2, 1, 20),
    _FunkSbrRatesProxyAcctRequestCurrentRate_Type()
)
funkSbrRatesProxyAcctRequestCurrentRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    funkSbrRatesProxyAcctRequestCurrentRate.setStatus("current")


class _FunkSbrRatesProxyAcctRequestAverageRate_Type(Integer32):
    """Custom type funkSbrRatesProxyAcctRequestAverageRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FunkSbrRatesProxyAcctRequestAverageRate_Type.__name__ = "Integer32"
_FunkSbrRatesProxyAcctRequestAverageRate_Object = MibScalar
funkSbrRatesProxyAcctRequestAverageRate = _FunkSbrRatesProxyAcctRequestAverageRate_Object(
    (1, 3, 6, 1, 4, 1, 1411, 1, 2, 1, 21),
    _FunkSbrRatesProxyAcctRequestAverageRate_Type()
)
funkSbrRatesProxyAcctRequestAverageRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    funkSbrRatesProxyAcctRequestAverageRate.setStatus("current")


class _FunkSbrRatesProxyAcctRequestPeakRate_Type(Integer32):
    """Custom type funkSbrRatesProxyAcctRequestPeakRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FunkSbrRatesProxyAcctRequestPeakRate_Type.__name__ = "Integer32"
_FunkSbrRatesProxyAcctRequestPeakRate_Object = MibScalar
funkSbrRatesProxyAcctRequestPeakRate = _FunkSbrRatesProxyAcctRequestPeakRate_Object(
    (1, 3, 6, 1, 4, 1, 1411, 1, 2, 1, 22),
    _FunkSbrRatesProxyAcctRequestPeakRate_Type()
)
funkSbrRatesProxyAcctRequestPeakRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    funkSbrRatesProxyAcctRequestPeakRate.setStatus("current")


class _FunkSbrRatesProxyFailTimeoutCurrentRate_Type(Integer32):
    """Custom type funkSbrRatesProxyFailTimeoutCurrentRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FunkSbrRatesProxyFailTimeoutCurrentRate_Type.__name__ = "Integer32"
_FunkSbrRatesProxyFailTimeoutCurrentRate_Object = MibScalar
funkSbrRatesProxyFailTimeoutCurrentRate = _FunkSbrRatesProxyFailTimeoutCurrentRate_Object(
    (1, 3, 6, 1, 4, 1, 1411, 1, 2, 1, 23),
    _FunkSbrRatesProxyFailTimeoutCurrentRate_Type()
)
funkSbrRatesProxyFailTimeoutCurrentRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    funkSbrRatesProxyFailTimeoutCurrentRate.setStatus("current")


class _FunkSbrRatesProxyFailTimeoutAverageRate_Type(Integer32):
    """Custom type funkSbrRatesProxyFailTimeoutAverageRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FunkSbrRatesProxyFailTimeoutAverageRate_Type.__name__ = "Integer32"
_FunkSbrRatesProxyFailTimeoutAverageRate_Object = MibScalar
funkSbrRatesProxyFailTimeoutAverageRate = _FunkSbrRatesProxyFailTimeoutAverageRate_Object(
    (1, 3, 6, 1, 4, 1, 1411, 1, 2, 1, 24),
    _FunkSbrRatesProxyFailTimeoutAverageRate_Type()
)
funkSbrRatesProxyFailTimeoutAverageRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    funkSbrRatesProxyFailTimeoutAverageRate.setStatus("current")


class _FunkSbrRatesProxyFailTimeoutPeakRate_Type(Integer32):
    """Custom type funkSbrRatesProxyFailTimeoutPeakRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FunkSbrRatesProxyFailTimeoutPeakRate_Type.__name__ = "Integer32"
_FunkSbrRatesProxyFailTimeoutPeakRate_Object = MibScalar
funkSbrRatesProxyFailTimeoutPeakRate = _FunkSbrRatesProxyFailTimeoutPeakRate_Object(
    (1, 3, 6, 1, 4, 1, 1411, 1, 2, 1, 25),
    _FunkSbrRatesProxyFailTimeoutPeakRate_Type()
)
funkSbrRatesProxyFailTimeoutPeakRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    funkSbrRatesProxyFailTimeoutPeakRate.setStatus("current")


class _FunkSbrRatesProxyFailBadrespCurrentRate_Type(Integer32):
    """Custom type funkSbrRatesProxyFailBadrespCurrentRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FunkSbrRatesProxyFailBadrespCurrentRate_Type.__name__ = "Integer32"
_FunkSbrRatesProxyFailBadrespCurrentRate_Object = MibScalar
funkSbrRatesProxyFailBadrespCurrentRate = _FunkSbrRatesProxyFailBadrespCurrentRate_Object(
    (1, 3, 6, 1, 4, 1, 1411, 1, 2, 1, 26),
    _FunkSbrRatesProxyFailBadrespCurrentRate_Type()
)
funkSbrRatesProxyFailBadrespCurrentRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    funkSbrRatesProxyFailBadrespCurrentRate.setStatus("current")


class _FunkSbrRatesProxyFailBadrespAverageRate_Type(Integer32):
    """Custom type funkSbrRatesProxyFailBadrespAverageRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FunkSbrRatesProxyFailBadrespAverageRate_Type.__name__ = "Integer32"
_FunkSbrRatesProxyFailBadrespAverageRate_Object = MibScalar
funkSbrRatesProxyFailBadrespAverageRate = _FunkSbrRatesProxyFailBadrespAverageRate_Object(
    (1, 3, 6, 1, 4, 1, 1411, 1, 2, 1, 27),
    _FunkSbrRatesProxyFailBadrespAverageRate_Type()
)
funkSbrRatesProxyFailBadrespAverageRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    funkSbrRatesProxyFailBadrespAverageRate.setStatus("current")


class _FunkSbrRatesProxyFailBadrespPeakRate_Type(Integer32):
    """Custom type funkSbrRatesProxyFailBadrespPeakRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FunkSbrRatesProxyFailBadrespPeakRate_Type.__name__ = "Integer32"
_FunkSbrRatesProxyFailBadrespPeakRate_Object = MibScalar
funkSbrRatesProxyFailBadrespPeakRate = _FunkSbrRatesProxyFailBadrespPeakRate_Object(
    (1, 3, 6, 1, 4, 1, 1411, 1, 2, 1, 28),
    _FunkSbrRatesProxyFailBadrespPeakRate_Type()
)
funkSbrRatesProxyFailBadrespPeakRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    funkSbrRatesProxyFailBadrespPeakRate.setStatus("current")


class _FunkSbrRatesProxyFailBadsecretCurrentRate_Type(Integer32):
    """Custom type funkSbrRatesProxyFailBadsecretCurrentRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FunkSbrRatesProxyFailBadsecretCurrentRate_Type.__name__ = "Integer32"
_FunkSbrRatesProxyFailBadsecretCurrentRate_Object = MibScalar
funkSbrRatesProxyFailBadsecretCurrentRate = _FunkSbrRatesProxyFailBadsecretCurrentRate_Object(
    (1, 3, 6, 1, 4, 1, 1411, 1, 2, 1, 29),
    _FunkSbrRatesProxyFailBadsecretCurrentRate_Type()
)
funkSbrRatesProxyFailBadsecretCurrentRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    funkSbrRatesProxyFailBadsecretCurrentRate.setStatus("current")


class _FunkSbrRatesProxyFailBadsecretAverageRate_Type(Integer32):
    """Custom type funkSbrRatesProxyFailBadsecretAverageRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FunkSbrRatesProxyFailBadsecretAverageRate_Type.__name__ = "Integer32"
_FunkSbrRatesProxyFailBadsecretAverageRate_Object = MibScalar
funkSbrRatesProxyFailBadsecretAverageRate = _FunkSbrRatesProxyFailBadsecretAverageRate_Object(
    (1, 3, 6, 1, 4, 1, 1411, 1, 2, 1, 30),
    _FunkSbrRatesProxyFailBadsecretAverageRate_Type()
)
funkSbrRatesProxyFailBadsecretAverageRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    funkSbrRatesProxyFailBadsecretAverageRate.setStatus("current")


class _FunkSbrRatesProxyFailBadsecretPeakRate_Type(Integer32):
    """Custom type funkSbrRatesProxyFailBadsecretPeakRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FunkSbrRatesProxyFailBadsecretPeakRate_Type.__name__ = "Integer32"
_FunkSbrRatesProxyFailBadsecretPeakRate_Object = MibScalar
funkSbrRatesProxyFailBadsecretPeakRate = _FunkSbrRatesProxyFailBadsecretPeakRate_Object(
    (1, 3, 6, 1, 4, 1, 1411, 1, 2, 1, 31),
    _FunkSbrRatesProxyFailBadsecretPeakRate_Type()
)
funkSbrRatesProxyFailBadsecretPeakRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    funkSbrRatesProxyFailBadsecretPeakRate.setStatus("current")


class _FunkSbrRatesProxyFailMissingresrCurrentRate_Type(Integer32):
    """Custom type funkSbrRatesProxyFailMissingresrCurrentRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FunkSbrRatesProxyFailMissingresrCurrentRate_Type.__name__ = "Integer32"
_FunkSbrRatesProxyFailMissingresrCurrentRate_Object = MibScalar
funkSbrRatesProxyFailMissingresrCurrentRate = _FunkSbrRatesProxyFailMissingresrCurrentRate_Object(
    (1, 3, 6, 1, 4, 1, 1411, 1, 2, 1, 32),
    _FunkSbrRatesProxyFailMissingresrCurrentRate_Type()
)
funkSbrRatesProxyFailMissingresrCurrentRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    funkSbrRatesProxyFailMissingresrCurrentRate.setStatus("current")


class _FunkSbrRatesProxyFailMissingresrAverageRate_Type(Integer32):
    """Custom type funkSbrRatesProxyFailMissingresrAverageRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FunkSbrRatesProxyFailMissingresrAverageRate_Type.__name__ = "Integer32"
_FunkSbrRatesProxyFailMissingresrAverageRate_Object = MibScalar
funkSbrRatesProxyFailMissingresrAverageRate = _FunkSbrRatesProxyFailMissingresrAverageRate_Object(
    (1, 3, 6, 1, 4, 1, 1411, 1, 2, 1, 33),
    _FunkSbrRatesProxyFailMissingresrAverageRate_Type()
)
funkSbrRatesProxyFailMissingresrAverageRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    funkSbrRatesProxyFailMissingresrAverageRate.setStatus("current")


class _FunkSbrRatesProxyFailMissingresrPeakRate_Type(Integer32):
    """Custom type funkSbrRatesProxyFailMissingresrPeakRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FunkSbrRatesProxyFailMissingresrPeakRate_Type.__name__ = "Integer32"
_FunkSbrRatesProxyFailMissingresrPeakRate_Object = MibScalar
funkSbrRatesProxyFailMissingresrPeakRate = _FunkSbrRatesProxyFailMissingresrPeakRate_Object(
    (1, 3, 6, 1, 4, 1, 1411, 1, 2, 1, 34),
    _FunkSbrRatesProxyFailMissingresrPeakRate_Type()
)
funkSbrRatesProxyFailMissingresrPeakRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    funkSbrRatesProxyFailMissingresrPeakRate.setStatus("current")


class _FunkSbrRatesProxyRetriesCurrentRate_Type(Integer32):
    """Custom type funkSbrRatesProxyRetriesCurrentRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FunkSbrRatesProxyRetriesCurrentRate_Type.__name__ = "Integer32"
_FunkSbrRatesProxyRetriesCurrentRate_Object = MibScalar
funkSbrRatesProxyRetriesCurrentRate = _FunkSbrRatesProxyRetriesCurrentRate_Object(
    (1, 3, 6, 1, 4, 1, 1411, 1, 2, 1, 35),
    _FunkSbrRatesProxyRetriesCurrentRate_Type()
)
funkSbrRatesProxyRetriesCurrentRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    funkSbrRatesProxyRetriesCurrentRate.setStatus("current")


class _FunkSbrRatesProxyRetriesAverageRate_Type(Integer32):
    """Custom type funkSbrRatesProxyRetriesAverageRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FunkSbrRatesProxyRetriesAverageRate_Type.__name__ = "Integer32"
_FunkSbrRatesProxyRetriesAverageRate_Object = MibScalar
funkSbrRatesProxyRetriesAverageRate = _FunkSbrRatesProxyRetriesAverageRate_Object(
    (1, 3, 6, 1, 4, 1, 1411, 1, 2, 1, 36),
    _FunkSbrRatesProxyRetriesAverageRate_Type()
)
funkSbrRatesProxyRetriesAverageRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    funkSbrRatesProxyRetriesAverageRate.setStatus("current")


class _FunkSbrRatesProxyRetriesPeakRate_Type(Integer32):
    """Custom type funkSbrRatesProxyRetriesPeakRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FunkSbrRatesProxyRetriesPeakRate_Type.__name__ = "Integer32"
_FunkSbrRatesProxyRetriesPeakRate_Object = MibScalar
funkSbrRatesProxyRetriesPeakRate = _FunkSbrRatesProxyRetriesPeakRate_Object(
    (1, 3, 6, 1, 4, 1, 1411, 1, 2, 1, 37),
    _FunkSbrRatesProxyRetriesPeakRate_Type()
)
funkSbrRatesProxyRetriesPeakRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    funkSbrRatesProxyRetriesPeakRate.setStatus("current")


class _FunkSbrRatesProxyAuthRejProxyCurrentRate_Type(Integer32):
    """Custom type funkSbrRatesProxyAuthRejProxyCurrentRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FunkSbrRatesProxyAuthRejProxyCurrentRate_Type.__name__ = "Integer32"
_FunkSbrRatesProxyAuthRejProxyCurrentRate_Object = MibScalar
funkSbrRatesProxyAuthRejProxyCurrentRate = _FunkSbrRatesProxyAuthRejProxyCurrentRate_Object(
    (1, 3, 6, 1, 4, 1, 1411, 1, 2, 1, 38),
    _FunkSbrRatesProxyAuthRejProxyCurrentRate_Type()
)
funkSbrRatesProxyAuthRejProxyCurrentRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    funkSbrRatesProxyAuthRejProxyCurrentRate.setStatus("current")


class _FunkSbrRatesProxyAuthRejProxyAverageRate_Type(Integer32):
    """Custom type funkSbrRatesProxyAuthRejProxyAverageRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FunkSbrRatesProxyAuthRejProxyAverageRate_Type.__name__ = "Integer32"
_FunkSbrRatesProxyAuthRejProxyAverageRate_Object = MibScalar
funkSbrRatesProxyAuthRejProxyAverageRate = _FunkSbrRatesProxyAuthRejProxyAverageRate_Object(
    (1, 3, 6, 1, 4, 1, 1411, 1, 2, 1, 39),
    _FunkSbrRatesProxyAuthRejProxyAverageRate_Type()
)
funkSbrRatesProxyAuthRejProxyAverageRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    funkSbrRatesProxyAuthRejProxyAverageRate.setStatus("current")


class _FunkSbrRatesProxyAuthRejProxyPeakRate_Type(Integer32):
    """Custom type funkSbrRatesProxyAuthRejProxyPeakRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FunkSbrRatesProxyAuthRejProxyPeakRate_Type.__name__ = "Integer32"
_FunkSbrRatesProxyAuthRejProxyPeakRate_Object = MibScalar
funkSbrRatesProxyAuthRejProxyPeakRate = _FunkSbrRatesProxyAuthRejProxyPeakRate_Object(
    (1, 3, 6, 1, 4, 1, 1411, 1, 2, 1, 40),
    _FunkSbrRatesProxyAuthRejProxyPeakRate_Type()
)
funkSbrRatesProxyAuthRejProxyPeakRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    funkSbrRatesProxyAuthRejProxyPeakRate.setStatus("current")


class _FunkSbrRatesProxyAcctFailProxCurrentRate_Type(Integer32):
    """Custom type funkSbrRatesProxyAcctFailProxCurrentRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FunkSbrRatesProxyAcctFailProxCurrentRate_Type.__name__ = "Integer32"
_FunkSbrRatesProxyAcctFailProxCurrentRate_Object = MibScalar
funkSbrRatesProxyAcctFailProxCurrentRate = _FunkSbrRatesProxyAcctFailProxCurrentRate_Object(
    (1, 3, 6, 1, 4, 1, 1411, 1, 2, 1, 41),
    _FunkSbrRatesProxyAcctFailProxCurrentRate_Type()
)
funkSbrRatesProxyAcctFailProxCurrentRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    funkSbrRatesProxyAcctFailProxCurrentRate.setStatus("current")


class _FunkSbrRatesProxyAcctFailProxAverageRate_Type(Integer32):
    """Custom type funkSbrRatesProxyAcctFailProxAverageRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FunkSbrRatesProxyAcctFailProxAverageRate_Type.__name__ = "Integer32"
_FunkSbrRatesProxyAcctFailProxAverageRate_Object = MibScalar
funkSbrRatesProxyAcctFailProxAverageRate = _FunkSbrRatesProxyAcctFailProxAverageRate_Object(
    (1, 3, 6, 1, 4, 1, 1411, 1, 2, 1, 42),
    _FunkSbrRatesProxyAcctFailProxAverageRate_Type()
)
funkSbrRatesProxyAcctFailProxAverageRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    funkSbrRatesProxyAcctFailProxAverageRate.setStatus("current")


class _FunkSbrRatesProxyAcctFailProxPeakRate_Type(Integer32):
    """Custom type funkSbrRatesProxyAcctFailProxPeakRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FunkSbrRatesProxyAcctFailProxPeakRate_Type.__name__ = "Integer32"
_FunkSbrRatesProxyAcctFailProxPeakRate_Object = MibScalar
funkSbrRatesProxyAcctFailProxPeakRate = _FunkSbrRatesProxyAcctFailProxPeakRate_Object(
    (1, 3, 6, 1, 4, 1, 1411, 1, 2, 1, 43),
    _FunkSbrRatesProxyAcctFailProxPeakRate_Type()
)
funkSbrRatesProxyAcctFailProxPeakRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    funkSbrRatesProxyAcctFailProxPeakRate.setStatus("current")


class _FunkSbrRatesProxyAuthRejProxyErrorCurrentRate_Type(Integer32):
    """Custom type funkSbrRatesProxyAuthRejProxyErrorCurrentRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FunkSbrRatesProxyAuthRejProxyErrorCurrentRate_Type.__name__ = "Integer32"
_FunkSbrRatesProxyAuthRejProxyErrorCurrentRate_Object = MibScalar
funkSbrRatesProxyAuthRejProxyErrorCurrentRate = _FunkSbrRatesProxyAuthRejProxyErrorCurrentRate_Object(
    (1, 3, 6, 1, 4, 1, 1411, 1, 2, 1, 44),
    _FunkSbrRatesProxyAuthRejProxyErrorCurrentRate_Type()
)
funkSbrRatesProxyAuthRejProxyErrorCurrentRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    funkSbrRatesProxyAuthRejProxyErrorCurrentRate.setStatus("current")


class _FunkSbrRatesProxyAuthRejProxyErrorAverageRate_Type(Integer32):
    """Custom type funkSbrRatesProxyAuthRejProxyErrorAverageRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FunkSbrRatesProxyAuthRejProxyErrorAverageRate_Type.__name__ = "Integer32"
_FunkSbrRatesProxyAuthRejProxyErrorAverageRate_Object = MibScalar
funkSbrRatesProxyAuthRejProxyErrorAverageRate = _FunkSbrRatesProxyAuthRejProxyErrorAverageRate_Object(
    (1, 3, 6, 1, 4, 1, 1411, 1, 2, 1, 45),
    _FunkSbrRatesProxyAuthRejProxyErrorAverageRate_Type()
)
funkSbrRatesProxyAuthRejProxyErrorAverageRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    funkSbrRatesProxyAuthRejProxyErrorAverageRate.setStatus("current")


class _FunkSbrRatesProxyAuthRejProxyErrorPeakRate_Type(Integer32):
    """Custom type funkSbrRatesProxyAuthRejProxyErrorPeakRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FunkSbrRatesProxyAuthRejProxyErrorPeakRate_Type.__name__ = "Integer32"
_FunkSbrRatesProxyAuthRejProxyErrorPeakRate_Object = MibScalar
funkSbrRatesProxyAuthRejProxyErrorPeakRate = _FunkSbrRatesProxyAuthRejProxyErrorPeakRate_Object(
    (1, 3, 6, 1, 4, 1, 1411, 1, 2, 1, 46),
    _FunkSbrRatesProxyAuthRejProxyErrorPeakRate_Type()
)
funkSbrRatesProxyAuthRejProxyErrorPeakRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    funkSbrRatesProxyAuthRejProxyErrorPeakRate.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FNKRATE-MIB",
    **{"funkSbrExtensions": funkSbrExtensions,
       "funkSbrRateVars": funkSbrRateVars,
       "funkSbrRatesSecondsPerInterval": funkSbrRatesSecondsPerInterval,
       "funkSbrRatesAuthRequestCurrentRate": funkSbrRatesAuthRequestCurrentRate,
       "funkSbrRatesAuthRequestAverageRate": funkSbrRatesAuthRequestAverageRate,
       "funkSbrRatesAuthRequestPeakRate": funkSbrRatesAuthRequestPeakRate,
       "funkSbrRatesAuthAcceptCurrentRate": funkSbrRatesAuthAcceptCurrentRate,
       "funkSbrRatesAuthAcceptAverageRate": funkSbrRatesAuthAcceptAverageRate,
       "funkSbrRatesAuthAcceptPeakRate": funkSbrRatesAuthAcceptPeakRate,
       "funkSbrRatesAuthRejectCurrentRate": funkSbrRatesAuthRejectCurrentRate,
       "funkSbrRatesAuthRejectAverageRate": funkSbrRatesAuthRejectAverageRate,
       "funkSbrRatesAuthRejectPeakRate": funkSbrRatesAuthRejectPeakRate,
       "funkSbrRatesAcctStartCurrentRate": funkSbrRatesAcctStartCurrentRate,
       "funkSbrRatesAcctStartAverageRate": funkSbrRatesAcctStartAverageRate,
       "funkSbrRatesAcctStartPeakRate": funkSbrRatesAcctStartPeakRate,
       "funkSbrRatesAcctStopCurrentRate": funkSbrRatesAcctStopCurrentRate,
       "funkSbrRatesAcctStopAverageRate": funkSbrRatesAcctStopAverageRate,
       "funkSbrRatesAcctStopPeakRate": funkSbrRatesAcctStopPeakRate,
       "funkSbrRatesProxyAuthRequestCurrentRate": funkSbrRatesProxyAuthRequestCurrentRate,
       "funkSbrRatesProxyAuthRequestAverageRate": funkSbrRatesProxyAuthRequestAverageRate,
       "funkSbrRatesProxyAuthRequestPeakRate": funkSbrRatesProxyAuthRequestPeakRate,
       "funkSbrRatesProxyAcctRequestCurrentRate": funkSbrRatesProxyAcctRequestCurrentRate,
       "funkSbrRatesProxyAcctRequestAverageRate": funkSbrRatesProxyAcctRequestAverageRate,
       "funkSbrRatesProxyAcctRequestPeakRate": funkSbrRatesProxyAcctRequestPeakRate,
       "funkSbrRatesProxyFailTimeoutCurrentRate": funkSbrRatesProxyFailTimeoutCurrentRate,
       "funkSbrRatesProxyFailTimeoutAverageRate": funkSbrRatesProxyFailTimeoutAverageRate,
       "funkSbrRatesProxyFailTimeoutPeakRate": funkSbrRatesProxyFailTimeoutPeakRate,
       "funkSbrRatesProxyFailBadrespCurrentRate": funkSbrRatesProxyFailBadrespCurrentRate,
       "funkSbrRatesProxyFailBadrespAverageRate": funkSbrRatesProxyFailBadrespAverageRate,
       "funkSbrRatesProxyFailBadrespPeakRate": funkSbrRatesProxyFailBadrespPeakRate,
       "funkSbrRatesProxyFailBadsecretCurrentRate": funkSbrRatesProxyFailBadsecretCurrentRate,
       "funkSbrRatesProxyFailBadsecretAverageRate": funkSbrRatesProxyFailBadsecretAverageRate,
       "funkSbrRatesProxyFailBadsecretPeakRate": funkSbrRatesProxyFailBadsecretPeakRate,
       "funkSbrRatesProxyFailMissingresrCurrentRate": funkSbrRatesProxyFailMissingresrCurrentRate,
       "funkSbrRatesProxyFailMissingresrAverageRate": funkSbrRatesProxyFailMissingresrAverageRate,
       "funkSbrRatesProxyFailMissingresrPeakRate": funkSbrRatesProxyFailMissingresrPeakRate,
       "funkSbrRatesProxyRetriesCurrentRate": funkSbrRatesProxyRetriesCurrentRate,
       "funkSbrRatesProxyRetriesAverageRate": funkSbrRatesProxyRetriesAverageRate,
       "funkSbrRatesProxyRetriesPeakRate": funkSbrRatesProxyRetriesPeakRate,
       "funkSbrRatesProxyAuthRejProxyCurrentRate": funkSbrRatesProxyAuthRejProxyCurrentRate,
       "funkSbrRatesProxyAuthRejProxyAverageRate": funkSbrRatesProxyAuthRejProxyAverageRate,
       "funkSbrRatesProxyAuthRejProxyPeakRate": funkSbrRatesProxyAuthRejProxyPeakRate,
       "funkSbrRatesProxyAcctFailProxCurrentRate": funkSbrRatesProxyAcctFailProxCurrentRate,
       "funkSbrRatesProxyAcctFailProxAverageRate": funkSbrRatesProxyAcctFailProxAverageRate,
       "funkSbrRatesProxyAcctFailProxPeakRate": funkSbrRatesProxyAcctFailProxPeakRate,
       "funkSbrRatesProxyAuthRejProxyErrorCurrentRate": funkSbrRatesProxyAuthRejProxyErrorCurrentRate,
       "funkSbrRatesProxyAuthRejProxyErrorAverageRate": funkSbrRatesProxyAuthRejProxyErrorAverageRate,
       "funkSbrRatesProxyAuthRejProxyErrorPeakRate": funkSbrRatesProxyAuthRejProxyErrorPeakRate}
)
